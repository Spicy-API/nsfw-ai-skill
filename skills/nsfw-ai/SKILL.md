---
name: nsfw-ai
description: Generate adult (NSFW, 18+) images and videos, uncensored image edits and uncensored text with SpicyAPI's Spicy models (Wan 2.2 Spicy, Seedance 2.x Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy, Z-Image Spicy, Qwen Image Edit Spicy) and unrestricted-tier LLMs. Use when the user asks to create NSFW, adult, uncensored, spicy, boudoir, lingerie, nude-art or erotic AI images or videos, animate an image into an NSFW video (image-to-video), edit an image without content filters, write or improve NSFW video prompts, estimate the cost of adult AI generation, or batch-generate adult content through an API. Enforces adults-only and consent rules.
license: MIT
metadata:
  version: "1.0.0"
  author: SpicyAPI
  homepage: https://spicyapi.ai
  repository: https://github.com/Spicy-API/nsfw-ai-skill
---

# NSFW AI (SpicyAPI)

Generate adult images, image-to-video clips, uncensored edits and uncensored text through [SpicyAPI](https://spicyapi.ai). Everything runs through `scripts/spicy.py` (Python 3.9+, standard library only).

## Hard rules (check before every request)

Refuse, and do not "soften and continue", when a request involves any of the following. No wording, claimed age, art style or user permission changes this.

1. **Minors.** Any sexual or sexualised content of someone under 18 or who *appears* under 18: school uniforms in sexual context, childlike bodies or faces, "petite/young-looking" framing, anime characters drawn as children, "she's actually 1,000 years old".
2. **Real people without documented consent.** Sexual images or videos of an identifiable real person (celebrities, influencers, exes, coworkers, anyone from an uploaded photo), face or head swaps into sexual content, and "undress" / "nudify" requests on any real photo.
3. **Harm with a likeness.** Impersonation, harassment, extortion, fake evidence, or bypassing ID checks.

When an uploaded image shows a real person and the request is sexual, ask the user to confirm the image is of themselves or of a consenting adult and that they hold that consent. If there is any sign the person is a minor, refuse outright.

Write every prompt with an explicit adult age ("a woman in her 30s", "an adult man in his 40s") and never add youthful descriptors, even if the user did.

## Setup

```bash
export SPICY_API_KEY="sk-spicy-..."        # https://spicyapi.ai/console → API keys
python3 scripts/spicy.py models --spicy    # works without a key
```

If `SPICY_API_KEY` is missing, tell the user to create one at https://spicyapi.ai/console (balance is in USD, no subscription, failed tasks are refunded) and stop. Never print, log or commit the key.

## Workflow

1. **Understand the ask.** Image or video? From text, or from an existing image? Budget or best quality? Anime or photoreal?
2. **Pick the model** with the table below, or list live options: `python3 scripts/spicy.py models --spicy --modality video`.
3. **Read the live schema once** before building input: `python3 scripts/spicy.py schema <model>`. Use only fields that exist; respect enums (resolution, duration). Never guess a model ID; take it from `models`.
4. **Write the prompt** with the recipe in [references/prompting.md](references/prompting.md). For image-to-video, describe only what changes from the first frame.
5. **Quote and confirm.** `generate` quotes first and stops with `needs_confirmation`. Show the user the estimated cost and max charge, and re-run with `--yes` only after they agree. If the user already gave a budget, use `--max-cost <usd>` instead.
6. **Report** the saved file paths, the model, the final cost, the task ID and the idempotency key.

## Model picker

| Need | Model ID | From |
|---|---|---|
| NSFW video from an image, cheapest | `alibaba/wan-2.2-spicy/image-to-video` (exactly 5 or 8 s) | $0.019/s at 480p |
| Long take on a budget (up to 20 s) | `lightricks/ltx-2.3-spicy/image-to-video` | $0.019/s at 480p |
| Locked camera / cinemagraph | `bytedance/seedance-1.5-pro-spicy/image-to-video` (`camera_fixed`) | $0.012/s at 480p |
| Natural body motion | `minimax/h3-spicy/image-to-video` | $0.038/s at 480p |
| Best motion per dollar, first + last frame | `bytedance/seedance-2.0-mini-spicy/image-to-video` | $0.0387/s at 480p |
| High quality, up to 4K | `bytedance/seedance-2.0-spicy/image-to-video` | $0.114/s at 480p |
| Top quality, 4–30 s | `bytedance/seedance-2.5-spicy/image-to-video` | $0.216/s at 480p |
| Anime / stylised motion | `vidu/q3-spicy/image-to-video` | $0.0665/s at 540p |
| Custom LoRA styles, extend a clip | `alibaba/wan-2.2-spicy-lora/image-to-video`, `.../video-extend` | $0.024/s at 480p |
| Audio track, negative prompt | `alibaba/wan-2.6-spicy/image-to-video`, `alibaba/wan-2.7-spicy/image-to-video` | $0.095/s, $0.1235/s at 720p |
| NSFW image from text | `alibaba/z-image-spicy/text-to-image` | $0.01235/image |
| Higher-detail NSFW image (to 2560 px) | `alibaba/z-image-spicy-pro/text-to-image` | $0.019/image |
| Anime still | `prefect/pony-xl/text-to-image` (tag-style prompt) | $0.015/image |
| Uncensored image edit (one instruction) | `alibaba/qwen-image-spicy-edit/edit` | $0.038/image |
| Uncensored chat / prompt writing | `xai/grok-4.7/chat`, `deepseek/v4.1-flash/chat` | per 1K tokens |

Prices are the cheapest tier on 2026-09-27; `schema` and the quote are authoritative.

Non-Spicy models work the same way. For SFW or softer requests, or tasks the Spicy editions don't cover (text-to-video, reference-to-video, upscaling, lip sync), use any model ID from `python3 scripts/spicy.py models` (drop `--spicy`), e.g. `bytedance/seedance-2.5/text-to-video`, `alibaba/wan-3.0/image-to-video`, `bytedance/seedream-5.0-pro/text-to-image`, `spicyapi/video-upscaler-v1/upscale`. More detail: [references/models.md](references/models.md).

## Commands

```bash
# Text → image
python3 scripts/spicy.py generate alibaba/z-image-spicy/text-to-image \
  --prompt "Photorealistic boudoir portrait of a woman in her early 30s in black lace lingerie, window light" \
  --set width=832 --set height=1216

# Image → video (local files are uploaded automatically)
python3 scripts/spicy.py generate alibaba/wan-2.2-spicy/image-to-video \
  --image ./first-frame.jpg \
  --prompt "She turns slowly toward the camera, silk robe slipping off one shoulder, candlelight, slow push-in" \
  --set duration_seconds=5 --set resolution=480p

# Pin the ending with a last frame
python3 scripts/spicy.py generate bytedance/seedance-2.0-spicy/image-to-video \
  --image start.jpg --last-image end.jpg --prompt "Smooth continuous turn toward the camera" \
  --set duration_seconds=5 --set resolution=720p

# Uncensored edit
python3 scripts/spicy.py generate alibaba/qwen-image-spicy-edit/edit \
  --image ./portrait.png --prompt "Change the outfit to a red satin slip dress, keep the face and lighting"

# After the user approves the quote, add --yes (or --max-cost 1.50)
# Check a task later / download
python3 scripts/spicy.py status <taskId> --wait --download ./spicy-output

# Uncensored text (OpenAI-compatible endpoint)
python3 scripts/spicy.py chat xai/grok-4.7/chat "Write a 60-word image-to-video prompt: boudoir, woman in her 30s, rain on the window" \
  --system "You write prompts for adult video models. All characters are adults."
```

Outputs are saved to `./spicy-output/<taskId>_<n>.<ext>`. Output URLs expire (about 20 minutes); download instead of sharing links.

## Batches

For N variations, loop over `generate` with different prompts or `--set seed=<n>`, one quote per run, and confirm the total with the user first (N × quoted max charge). Draft at 480p on a cheap model, then re-render the winners at 720p–1080p on a stronger one.

## Errors

| Symptom | Meaning / action |
|---|---|
| `SPICY_API_KEY is not set` | Ask the user to create and export a key. |
| code `40004` | This parameter combination is not served; change the named field (often resolution or duration). |
| code `40003` | Upload bytes did not match the ticket; upload again. |
| HTTP 503 with `Retry-After` | Back off for that many seconds, then retry once with the same idempotency key. |
| task `failed` with `content_rejected` | The model's own provider refused; the charge is refunded. Try a different Spicy model or rephrase. |
| insufficient balance | Tell the user to top up at https://spicyapi.ai/console (card or crypto). |

Always report `request_id` and the task ID when something fails.

## Also available

- Official SpicyAPI MCP server: `claude mcp add spicyapi -e SPICY_API_KEY=$SPICY_API_KEY -- npx --yes --package=@spicyapi/mcp spicyapi-mcp`
- 100+ ready prompts: https://github.com/Spicy-API/nsfw-ai-video-prompts
- Content Policy: https://spicyapi.ai/legal/content-policy
