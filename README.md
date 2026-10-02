<!--
  Keywords: nsfw ai skill, nsfw agent skill, claude code nsfw, uncensored ai skill, nsfw mcp, nsfw ai api,
  nsfw image to video api, uncensored ai image generator api, uncensored ai video generator api, wan 2.2 spicy api,
  seedance spicy api, nsfw ai image editor api, cursor nsfw, codex skill, openclaw skill, spicyapi
-->

<p align="center"><b>English</b> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <a href="README.ru.md">Русский</a></p>

<h1 align="center">NSFW AI Skill</h1>

<p align="center">
  <b>An agent skill that lets Claude Code, Cursor, Codex, Windsurf, Gemini CLI and OpenClaw generate adult (18+) images, NSFW image-to-video clips, uncensored image edits and uncensored text, through one pay-per-use API.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skill-agentskills-8b5cf6" alt="Agent Skill">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Claude Code plugin">
  <img src="https://img.shields.io/badge/python-3.9%2B%2C%20no%20deps-3776ab" alt="Python 3.9+, no dependencies">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#what-you-can-ask">What you can ask</a> ·
  <a href="#supported-models-and-prices">Models &amp; prices</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#use-without-an-agent">CLI</a> ·
  <a href="#faq">FAQ</a>
</p>

<p align="center">
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4"><img src="assets/one-pace-closer.gif" width="30%" alt="Wan 2.2 Spicy image-to-video example"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4"><img src="assets/velvet-spiral-turn.gif" width="30%" alt="Seedance 2.0 Spicy image-to-video example"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4"><img src="assets/silk-draught-pull.gif" width="30%" alt="Wan 2.7 Spicy image-to-video example"></a>
  <br><sub>Real outputs from the models this skill calls (Wan 2.2 Spicy, Seedance 2.0 Spicy, Wan 2.7 Spicy). Click for the full clip.</sub>
</p>

> **18+ only.** The skill refuses sexual content involving minors or anyone who appears to be a minor, sexual content of real people without documented consent (including face swaps and "undressing" photos), and impersonation. It writes every prompt with an explicit adult age.

---

## Why this skill

- **Talk, don't configure.** "Animate this photo into a 5-second boudoir clip, slow push-in" → the agent picks the model, reads its live schema, writes the prompt, shows you the price, and saves the MP4.
- **Picks backed by tests.** The skill follows SpicyAPI's published leaderboard: it defaults to models that rendered explicit test prompts as asked (Wan 3.0, Seedance 2.5 Spicy, MiniMax H3 LoRA, Qwen Image 2.1…) and steers away from ones that soften them.
- **Spicy models that actually allow adult output.** Uses [SpicyAPI](https://spicyapi.ai/?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=why)'s Spicy editions (Wan 2.2 Spicy, Seedance 2.x Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy, Z-Image Spicy, Qwen Image Edit Spicy). SpicyAPI adds no platform filter of its own on top of the model.
- **You see the price before anything runs.** Every generation is quoted first; the agent only proceeds after you approve (or within a budget you set). Failed tasks are refunded automatically.
- **Cheap.** NSFW video from **$0.012–$0.019 per second**, uncensored images from **$0.024** with Qwen Image 2.1 (or $0.01235 with Z-Image Spicy). USD balance, no subscription, card or crypto.
- **Every model in the catalog, not only Spicy ones.** The same commands run Seedance 2.5, Wan 3.0, Seedream 5.0, Qwen Image, upscalers, lip sync and the chat models; pass any model ID from `spicy.py models`.
- **Zero dependencies.** One Python file using only the standard library. Works anywhere Python 3.9+ runs.
- **Private by design.** Your API key stays in an environment variable. Prompts, uploads and outputs have retention clocks you can shorten on SpicyAPI.

---

## Install

### 1. Get an API key

Sign up at [spicyapi.ai](https://spicyapi.ai/register?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install), top up (card, Apple Pay / Google Pay, or crypto), then create a key in the [Console](https://spicyapi.ai/console?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install). Set a spend cap on the key if you like.

```bash
export SPICY_API_KEY="sk-spicy-..."
```

### 2. Add the skill to your agent

**Any agent (skills CLI: Claude Code, Cursor, Codex, Windsurf, Gemini CLI, OpenClaw and more)**

```bash
npx skills add Spicy-API/nsfw-ai-skill
```

**Claude Code plugin marketplace**

```text
/plugin marketplace add Spicy-API/nsfw-ai-skill
/plugin install nsfw-ai@spicyapi-nsfw
```

**Manual**

```bash
git clone https://github.com/Spicy-API/nsfw-ai-skill.git
cp -r nsfw-ai-skill/skills/nsfw-ai ~/.claude/skills/        # Claude Code
# or: cp -r nsfw-ai-skill/skills/nsfw-ai ~/.codex/skills/   # Codex
# or: point your agent's skills directory at skills/nsfw-ai
```

### 3. (Optional) Add the official SpicyAPI MCP server

The skill works on its own. If your client supports MCP, you can also add SpicyAPI's MCP server for model listing, quotes and task management:

```bash
claude mcp add spicyapi -e SPICY_API_KEY=$SPICY_API_KEY -- npx --yes --package=@spicyapi/mcp spicyapi-mcp
```

Cursor / Claude Desktop / Windsurf (`mcp.json`):

```json
{
  "mcpServers": {
    "spicyapi": {
      "command": "npx",
      "args": ["--yes", "--package=@spicyapi/mcp", "spicyapi-mcp"],
      "env": { "SPICY_API_KEY": "sk-spicy-..." }
    }
  }
}
```

---

## What you can ask

| You say | The skill does |
|---|---|
| "List the Spicy video models and what they cost." | Reads the live catalog (no key needed) |
| "Animate `./frame.jpg` into a 5-second clip: she turns toward the camera, candlelight, slow push-in. Cheapest option." | Uploads the image, uses Wan 2.2 Spicy at 480p, quotes ~$0.095, waits for your OK, saves the MP4 |
| "Photoreal first frame: a woman in her 30s in red lingerie on satin sheets, then animate it." | Qwen Image 2.1 → Wan 2.2 Spicy or Seedance, two quotes |
| "Re-render that at 720p on Seedance 2.0 Spicy with a last frame from `end.jpg`." | Seedance 2.0 Spicy with `last_image_url` |
| "Anime still of an adult demon queen, then make it move." | Prefect Pony XL → Vidu Q3 Spicy |
| "Change the outfit in `me.png` to a black satin slip dress." | Qwen Image 2.1 Edit (you, a consenting adult, or a fictional character only) |
| "Write three NSFW video prompts for this frame and estimate each." | Prompt recipe + quotes, nothing runs until you choose |
| "Extend my last clip by 5 seconds with the same LoRA." | Wan 2.2 Spicy LoRA `video-extend` |
| "Four seed variations at 480p, then the best one at 720p." | Batch with a total price confirmation |

More ideas in [examples/prompts.md](examples/prompts.md). 100+ ready prompts in **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts)**.

---

## Supported models and prices

The skill can call **any** model in the SpicyAPI catalog. These are the ones that matter for adult work, in catalog order (most popular first, newest version first), with the Spicy Index and Freedom Score from the public [SpicyAPI leaderboards](https://spicyapi.ai/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models) (✅ Freedom 90+ · ◐ 70–89 · ⚠️ under 70 · 🧪 under 15 test runs). 🌶️ **Spicy** editions are tuned for adult output; **Standard** models here have the catalog tier `unrestricted`, so they take mature prompts too and add text-to-video and reference-to-video. Cheapest tier shown; the skill always shows the exact quote before running. Catalog read on <!-- catalog:date -->
2026-09-27
<!-- /catalog:date -->

**Video**

<!-- catalog:video -->
| Model | Type | Tasks | Duration | From | Spicy Index | Freedom |
|---|---|---|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 4–30 s | $0.216/s | 56.5 | ✅ 96.7 |
| [Seedance 2.5](https://spicyapi.ai/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 4–30 s | $0.1234/s | 69.5 | ◐ 80.9 |
| [Seedance 2.0 Spicy](https://spicyapi.ai/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 4–15 s | $0.114/s | 61.5 | ✅ 93.3 |
| [Seedance 2.0](https://spicyapi.ai/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 4–15 s | $0.07/s | 81.5 | ◐ 70.4 |
| [Wan 3.0 Prime](https://spicyapi.ai/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 2–30 s | $0.0612/s | 76.5 | ◐ 78 |
| [Wan 3.0](https://spicyapi.ai/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 2–30 s | $0.045/s | 76.5 | ✅ 96 |
| [MiniMax H3 Spicy](https://spicyapi.ai/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 3–15 s | $0.038/s | 29.5 | ✅ 97.5 |
| [MiniMax H3](https://spicyapi.ai/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 4–15 s | $0.025/s | 72.5 | 🧪 33.3 |
| [MiniMax H3 Singularity LoRA](https://spicyapi.ai/models/minimax-h3-singularity-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V | 3–15 s | $0.06/s | 72.8 | ✅ 100 |
| [LTX 2.5](https://spicyapi.ai/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, T2V | 5–20 s | $0.09/s | 66 | ◐ 80.3 |
| [Wan 3.0 Pro Prime](https://spicyapi.ai/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 2–30 s | $0.234/s | 76.5 | ◐ 82 |
| [Wan 3.0 Pro](https://spicyapi.ai/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 2–30 s | $0.144/s | 76.5 | ◐ 82 |
| [MiniMax H3 LoRA](https://spicyapi.ai/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 3–15 s | $0.05/s | 75.2 | ✅ 98.3 |
| [HappyHorse 1.1](https://spicyapi.ai/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 3–15 s | $0.14/s | 62.5 | ⚠️ 65.1 |
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 4–15 s | $0.0387/s | 44.5 | ✅ 93.3 |
| [Seedance 2.0 Mini](https://spicyapi.ai/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 4–15 s | $0.01097/s | 64.5 | ⚠️ 64.9 |
| [Wan 2.7 Spicy](https://spicyapi.ai/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 2–15 s | $0.1235/s | 46.5 | ✅ 100 |
| [LTX 2.3 Spicy](https://spicyapi.ai/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 3–20 s | $0.019/s | 33.5 | ◐ 89.2 |
| [LTX 2.3 Spicy LoRA](https://spicyapi.ai/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 3–20 s | $0.0285/s | 34.8 | ◐ 83.8 |
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 4–15 s | $0.081/s | 44.5 | ✅ 90 |
| [Seedance 2.0 Fast](https://spicyapi.ai/models/seedance-2-0-fast?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 4–15 s | $0.02254/s | 64.5 | ⚠️ 68.2 |
| [Vidu Q3 Turbo](https://spicyapi.ai/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V | 1–16 s | $0.042/s | 39.5 | ✅ 93.3 |
| [Vidu Q3 Spicy](https://spicyapi.ai/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 1–16 s | $0.0665/s | 46.5 | ✅ 96.7 |
| [Vidu Q3](https://spicyapi.ai/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V | 1–16 s | $0.07/s | 46.5 | ✅ 93.3 |
| [Vidu Q3 Pro](https://spicyapi.ai/models/vidu-q3-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V | 1–16 s | $0.054/s | 36.5 | ✅ 93.3 |
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 4–12 s | $0.012/s | 48.5 | ✅ 96.7 |
| [Seedance 1.5 Pro](https://spicyapi.ai/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, T2V | 4–12 s | $0.0112/s | 46 | ✅ 90 |
| [Wan 2.6 Flash](https://spicyapi.ai/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V | 5, 10, 15 s | $0.0225/s | 31.5 | ✅ 100 |
| [Wan 2.6 Spicy](https://spicyapi.ai/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 5, 10, 15 s | $0.095/s | 46.5 | ✅ 96.7 |
| [Wan 2.6](https://spicyapi.ai/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, Ref2V, T2V | 5, 10, 15 s | $0.065/s | 58.5 | 🧪 8.7 |
| [Wan 2.5](https://spicyapi.ai/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V, T2V | 5, 10 s | $0.045/s | 46 | ✅ 99 |
| [Wan 2.2 Spicy](https://spicyapi.ai/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V | 5, 8 s | $0.019/s | 23.5 | ✅ 91.2 |
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | I2V, Extend | 5, 8 s | $0.024/s | 25 | ◐ 74.8 |
| [Wan 2.2 LoRA](https://spicyapi.ai/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | I2V | 5, 8 s | $0.024/s | 22.5 | ◐ 88.8 |
<!-- /catalog:video -->

**Images** (recommended: [Qwen Image 2.1](https://spicyapi.ai/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models), from $0.024)

<!-- catalog:image -->
| Model | Type | Tasks | From | Spicy Index | Freedom |
|---|---|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.024/image | 73 | ✅ 96.3 |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.03/image | 80.5 | ✅ 92 |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.042/image | 74.5 | ✅ 100 |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.04/image | 56 | ✅ 98 |
| [Qwen Image 3.0](https://spicyapi.ai/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.03/image | 56 | ✅ 96 |
| [Seedream 5.0 Pro](https://spicyapi.ai/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.036/image | 73 | ✅ 94.3 |
| [Qwen Image Edit Spicy](https://spicyapi.ai/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | Edit | $0.038/image | 14 | ✅ 96 |
| [Seedream 5.0 Lite](https://spicyapi.ai/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.0345/image | 73 | ✅ 96 |
| [Qwen Image 2](https://spicyapi.ai/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.035/image | 34 | ✅ 96.7 |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.03/image | 50.5 | ✅ 92.5 |
| [Z-Image Spicy Pro](https://spicyapi.ai/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | T2I | $0.019/image | 38 | ✅ 100 |
| [Z-Image Spicy](https://spicyapi.ai/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | 🌶️ Spicy | T2I | $0.01235/image | 32 | ✅ 98.8 |
| [Z-Image](https://spicyapi.ai/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | T2I | $0.01/image | 17 | ✅ 100 |
| [Z-Image Turbo LoRA](https://spicyapi.ai/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.012/image | 46.5 | ✅ 95 |
| [Seedream 4.0](https://spicyapi.ai/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | Edit, T2I | $0.03/image | 74 | ◐ 74.7 |
| [Prefect Pony XL](https://spicyapi.ai/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | T2I | $0.015/image | 30 | 🧪 36 |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table) | Standard | T2I | $0.018/image | 32.5 | ◐ 75 |
<!-- /catalog:image -->

**Text** (OpenAI-compatible `chat` command): [Grok 4.7](https://spicyapi.ai/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models), [DeepSeek V4.1 Flash](https://spicyapi.ai/models/deepseek-v4-1-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models) and other models with catalog tier `unrestricted`, from $0.0012 per 1K tokens.

Full field-level reference: [skills/nsfw-ai/references/models.md](skills/nsfw-ai/references/models.md).

---

## How it works

```
You ──► Agent reads SKILL.md
          │  1. checks the request against the adults-only / consent rules
          │  2. picks a model (or lists live ones)       spicy.py models --spicy
          │  3. reads the live input schema              spicy.py schema <model>
          │  4. writes the prompt (references/prompting.md)
          │  5. quotes and asks you to approve           spicy.py generate ...  → needs_confirmation
          │  6. runs after your OK                       spicy.py generate ... --yes
          ▼
     SpicyAPI  /api/v1/jobs/quote → /jobs/createTask (Idempotency-Key) → /jobs/recordInfo
          ▼
     ./spicy-output/<taskId>_0.mp4
```

- Local images are uploaded through SpicyAPI's signed upload flow and passed as `spicy://` URIs; public HTTPS URLs are passed straight through.
- Each task carries an idempotency key, so a retried request never creates a duplicate charge.
- The quote is bound to the task (`quoteId` + `expectedCost`), so the settled charge can never exceed the price you approved.

---

## Use without an agent

The same script is a normal CLI:

```bash
S=skills/nsfw-ai/scripts/spicy.py

python3 $S models --spicy --modality video          # no key needed
python3 $S schema alibaba/wan-2.2-spicy/image-to-video

python3 $S generate alibaba/qwen-image-2.1/text-to-image \
  -p "Photorealistic boudoir portrait of a woman in her early 30s in black lace lingerie, window light" \
  --set aspect_ratio=2:3 --set resolution=1k --max-cost 0.03

python3 $S generate alibaba/wan-2.2-spicy/image-to-video \
  --image ./spicy-output/<taskId>_0.png \
  -p "She turns slowly toward the camera, lace strap slipping, warm lamp light, slow push-in" \
  --set duration_seconds=5 --set resolution=480p --yes

python3 $S status <taskId> --wait --download ./spicy-output
python3 $S chat xai/grok-4.7/chat "Write a 60-word image-to-video prompt for a rainy-window boudoir scene, woman in her 30s"
```

Run the tests with `python3 -m unittest discover tests`. Example pipelines: [examples/image-to-video-pipeline.sh](examples/image-to-video-pipeline.sh), [examples/batch-variations.sh](examples/batch-variations.sh).

Prefer an SDK? SpicyAPI ships official ones: `npm install @spicyapi/sdk`, `pip install spicyapi`, `go get github.com/Spicy-API/spicy-go`, `composer require spicyapi/spicyapi`, plus `@spicyapi/cli`. See the [developer docs](https://docs.spicyapi.ai/docs?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=sdk).

---

## Repository layout

```
nsfw-ai-skill/
├── skills/nsfw-ai/
│   ├── SKILL.md                 # instructions the agent loads
│   ├── scripts/spicy.py         # zero-dependency SpicyAPI CLI
│   ├── references/models.md     # model IDs, fields, price tiers
│   ├── references/prompting.md  # prompt recipe, negatives, couples, anime
│   └── agents/openai.yaml       # Codex / OpenAI agents metadata
├── .claude-plugin/              # Claude Code plugin + marketplace manifests
├── examples/                    # pipelines and things to ask
└── tests/                       # offline unit tests
```

---

## FAQ

### Can Claude Code generate NSFW images or videos?
Claude Code itself does not generate media. With this skill installed, Claude Code (and Cursor, Codex, Windsurf, Gemini CLI, OpenClaw) calls SpicyAPI's Spicy models, which do allow adult output, and saves the files locally. The skill keeps hard limits: adults only, no real people without consent.

### What is the cheapest NSFW image-to-video API?
On SpicyAPI's catalog (2026-09-27) the cheapest models that pass the explicit tests are Seedance 1.5 Pro Spicy (from $0.012/s at 480p, Freedom 96.7) and Wan 2.6 Flash ($0.0225/s at 720p, Freedom 100). For the best result per dollar, Wan 3.0 costs $0.45 per 5-second 720p clip with Freedom 96.

### Is there a free NSFW AI skill?
The skill is free and open source (MIT). Generation is paid per output on SpicyAPI because GPUs cost money; there is no subscription and failed tasks are refunded. For free generation, run open-weight models locally (see [awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai#self-hosted-and-open-weight-models)).

### Can it call models that are not "Spicy"?
Yes. The Spicy editions are the default for adult requests, but `spicy.py` accepts any model ID in the SpicyAPI catalog: standard Seedance / Wan / MiniMax video models, Seedream / Qwen / Wan image models, upscalers, face and lip-sync tools, and text models via `chat`. Run `spicy.py models` (without `--spicy`) to list them.

### Does it work with MCP?
Yes. Use the skill alone, or add the official SpicyAPI MCP server (`@spicyapi/mcp`) alongside it.

### Where do my files go, and what does SpicyAPI keep?
Outputs download to `./spicy-output/`. Output links expire after about 20 minutes. SpicyAPI keeps prompts, uploads and outputs on separate retention clocks that you can shorten, and you can destroy a finished task's content; see [Trust](https://spicyapi.ai/trust?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=faq).

### Which model should I use for anime / hentai-style content?
Qwen Image 2.1 LoRA with an anime LoRA for the still (adult character design; #1 on the image leaderboard, Freedom 92), then Vidu Q3 Spicy (Freedom 96.7) or Wan 2.2 Spicy LoRA with the same LoRA for motion. Prefect Pony XL works with tag-style prompts but has little test data so far.

### Why did my task fail?
The model provider may still refuse some inputs; that shows up as a failed task and the charge is refunded. Change the wording or try another Spicy model. A `40004` error means the chosen parameter combination is not offered; change the named field.

---

## Rules

Adults only. No sexual content involving anyone under 18 or who appears under 18, in any style. No sexual content of real people without documented consent, no face swaps into sexual content, no "undressing" real photos. Follow the law where you and your audience are. SpicyAPI's [Content Policy](https://spicyapi.ai/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules) and [Acceptable Use Policy](https://spicyapi.ai/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules) apply to every request.

## Related

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai)**: curated list of uncensored AI image, video and text tools, APIs and models.
- **[nsfw-ai-image-prompts](https://github.com/Spicy-API/nsfw-ai-image-prompts)**: 104 NSFW image and editing prompts with real output cases.
- **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts)**: 100+ NSFW video prompts, first-frame prompts and verified examples.
- **[spicy-skill](https://github.com/Spicy-API/spicy-skill)**: SpicyAPI's official general-purpose skill.

## License

[MIT](LICENSE)

<p align="center">
  <a href="https://aiagentsdirectory.com" target="_blank" rel="noopener" title="Discover AI Agents Directory"><img src="https://aiagentsdirectory.com/featured-badge.svg?v=2024" alt="Featured on AI Agents Directory" width="200" height="50" /></a>
</p>

<p align="center"><sub>⭐ Star the repo if it saved you an afternoon of API docs.</sub></p>
