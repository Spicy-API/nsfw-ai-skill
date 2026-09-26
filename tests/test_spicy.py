"""Offline tests for skills/nsfw-ai/scripts/spicy.py. Run: python3 -m unittest discover tests"""

from __future__ import annotations

import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "nsfw-ai" / "scripts" / "spicy.py"
spec = importlib.util.spec_from_file_location("spicy", SCRIPT)
spicy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(spicy)

QUOTE = {"quoteId": "q1", "model": "m", "estimatedCost": "0.19", "maxCharge": "0.19", "currency": "USD",
         "quantity": "5", "unit": "per_second", "expiresAt": "2026-09-27T00:00:00Z"}


def run(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    code = 0
    with redirect_stdout(out), redirect_stderr(err):
        try:
            code = spicy.main(argv)
        except SystemExit as exc:
            code = exc.code
    return code, out.getvalue(), err.getvalue()


class InputTests(unittest.TestCase):
    def test_parse_value_types(self):
        self.assertEqual(spicy.parse_value("5"), 5)
        self.assertEqual(spicy.parse_value("0.8"), 0.8)
        self.assertIs(spicy.parse_value("true"), True)
        self.assertEqual(spicy.parse_value("720p"), "720p")
        self.assertEqual(spicy.parse_value("1216*832"), "1216*832")
        self.assertEqual(spicy.parse_value('[{"path":"https://x/l.safetensors","scale":0.8}]'),
                         [{"path": "https://x/l.safetensors", "scale": 0.8}])

    def test_build_input_merges_flags(self):
        ns = spicy.main.__globals__["argparse"].Namespace(
            input_file=None, input='{"seed": 1}', set=["duration_seconds=5", "resolution=720p"],
            prompt="hello", image="https://example.com/a.jpg", last_image=None, video=None, audio=None)
        self.assertEqual(spicy.build_input(ns), {"seed": 1, "duration_seconds": 5, "resolution": "720p",
                                                 "prompt": "hello", "image_url": "https://example.com/a.jpg"})

    def test_bad_set_and_missing_file(self):
        code, _, err = run(["quote", "m", "--set", "novalue"])
        self.assertEqual(code, 1)
        self.assertIn("key=value", err)
        code, _, err = run(["quote", "m", "--image", "/definitely/not/here.jpg"])
        self.assertEqual(code, 1)
        self.assertIn("not a local file", err)

    def test_spicy_uri_passthrough(self):
        self.assertEqual(spicy.resolve_media("spicy://f/fil_abc"), "spicy://f/fil_abc")


class GenerateTests(unittest.TestCase):
    def setUp(self):
        os.environ["SPICY_API_KEY"] = "sk-spicy-test"

    def test_requires_key(self):
        with mock.patch.dict(os.environ, {"SPICY_API_KEY": ""}):
            code, _, err = run(["generate", "m", "-p", "x"])
        self.assertEqual(code, 1)
        self.assertIn("SPICY_API_KEY is not set", err)

    def test_stops_for_confirmation(self):
        with mock.patch.object(spicy, "http_json", return_value={"code": 200, "data": QUOTE}) as http:
            code, out, _ = run(["generate", "m", "-p", "x"])
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(out)["status"], "needs_confirmation")
        self.assertEqual(http.call_count, 1)  # only the quote, no task created

    def test_max_cost_below_quote_does_not_run(self):
        with mock.patch.object(spicy, "http_json", return_value={"code": 200, "data": QUOTE}) as http:
            code, _, _ = run(["generate", "m", "-p", "x", "--max-cost", "0.10"])
        self.assertEqual(code, 2)
        self.assertEqual(http.call_count, 1)

    def test_full_flow_with_yes(self):
        created = {"taskId": "job_1", "model": "m", "state": "queued", "cost": "0.19", "settled": False,
                   "createdAt": "now"}
        done = dict(created, state="succeeded", settled=True,
                    output={"assets": [{"url": "https://cdn.example/x.mp4", "mime": "video/mp4"}]})
        calls = []

        def fake_http(method, url, body=None, headers=None, auth=True, timeout=60):
            calls.append((method, url, body, headers))
            if url.endswith("/jobs/quote"):
                return {"code": 200, "data": QUOTE}
            if url.endswith("/jobs/createTask"):
                return {"code": 200, "data": created}
            return {"code": 200, "data": done}

        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.object(spicy, "http_json", side_effect=fake_http), \
                mock.patch.object(spicy, "download", return_value=[f"{tmp}/job_1_0.mp4"]), \
                mock.patch.object(spicy.time, "sleep"):
            code, out, _ = run(["generate", "m", "-p", "x", "--yes", "--out", tmp])
        self.assertEqual(code, 0)
        result = json.loads(out)
        self.assertEqual(result["state"], "succeeded")
        self.assertEqual(result["assets"][0]["url"], "https://cdn.example/x.mp4")
        create = next(c for c in calls if c[1].endswith("/jobs/createTask"))
        self.assertEqual(create[2]["quoteId"], "q1")
        self.assertEqual(create[2]["expectedCost"], "0.19")
        self.assertIn("Idempotency-Key", create[3])

    def test_failed_task_exits_nonzero(self):
        failed = {"taskId": "job_2", "model": "m", "state": "failed", "cost": "0", "settled": True,
                  "createdAt": "now", "errorCode": "content_rejected", "errorMessage": "provider refused"}

        def fake_http(method, url, *_, **__):
            return {"code": 200, "data": QUOTE if url.endswith("/jobs/quote") else failed}

        with mock.patch.object(spicy, "http_json", side_effect=fake_http):
            code, out, _ = run(["generate", "m", "-p", "x", "--yes"])
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(out)["error"]["code"], "content_rejected")


class HttpTests(unittest.TestCase):
    def test_http_error_envelope(self):
        body = json.dumps({"code": 40004, "msg": "no deployment for resolution=1080p", "request_id": "req_1"})
        err = urllib.error.HTTPError("https://x", 400, "Bad Request", {"Retry-After": None}, io.BytesIO(body.encode()))
        with mock.patch.dict(os.environ, {"SPICY_API_KEY": "sk-spicy-test"}), \
                mock.patch.object(spicy.urllib.request, "urlopen", side_effect=err):
            with self.assertRaises(spicy.SpicyError) as ctx:
                spicy.http_json("POST", "https://x", {"a": 1})
        self.assertEqual(ctx.exception.code, 40004)
        self.assertEqual(ctx.exception.request_id, "req_1")

    def test_models_filter(self):
        catalog = {"code": 200, "data": {"items": [
            {"model": "a/wan-spicy/image-to-video", "familyDisplayName": "Wan Spicy", "modality": "video",
             "mature": True, "policyTier": "unrestricted", "price": {"amount": "0.019", "unit": "per_second"},
             "familyPageSlug": "wan-spicy"},
            {"model": "b/plain/text-to-image", "familyDisplayName": "Plain", "modality": "image",
             "mature": False, "policyTier": "filtered", "price": {"amount": "0.03", "unit": "per_image"},
             "familyPageSlug": "plain"},
        ]}}
        with mock.patch.object(spicy, "http_json", return_value=catalog):
            code, out, _ = run(["models", "--spicy", "--json"])
        self.assertEqual(code, 0)
        rows = json.loads(out)
        self.assertEqual([r["model"] for r in rows], ["a/wan-spicy/image-to-video"])


if __name__ == "__main__":
    unittest.main()
