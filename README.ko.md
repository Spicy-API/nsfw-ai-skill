<!--
  Keywords: NSFW AI 스킬, 성인 AI 이미지 생성, NSFW AI 영상 생성, 무검열 AI, 무검열 AI 이미지 생성기 API,
  무검열 AI 영상 생성기 API, NSFW 이미지 투 비디오 API, AI 이미지 영상 변환, 19금 AI 이미지 생성,
  Claude Code NSFW, Cursor NSFW, 에이전트 스킬, NSFW MCP, Wan 2.2 Spicy API, Seedance Spicy API,
  nsfw ai skill, nsfw agent skill, claude code nsfw, uncensored ai skill, nsfw ai api, codex skill, openclaw skill, spicyapi
-->

<p align="center"><a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <b>한국어</b> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a></p>

<h1 align="center">NSFW AI Skill</h1>

<p align="center">
  <b>Claude Code, Cursor, Codex, Windsurf, Gemini CLI, OpenClaw에서 성인(18+) 이미지 생성, NSFW 이미지 투 비디오, 무검열 이미지 편집, 무검열 텍스트 생성을 할 수 있게 해 주는 에이전트 스킬입니다. 사용한 만큼만 결제하는 API 하나로 작동합니다.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skill-agentskills-8b5cf6" alt="에이전트 스킬">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Claude Code 플러그인">
  <img src="https://img.shields.io/badge/python-3.9%2B%2C%20no%20deps-3776ab" alt="Python 3.9+, 의존성 없음">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#설치">설치</a> ·
  <a href="#이렇게-요청할-수-있습니다">요청 예시</a> ·
  <a href="#지원-모델과-가격">모델 &amp; 가격</a> ·
  <a href="#작동-방식">작동 방식</a> ·
  <a href="#에이전트-없이-cli로-사용하기">CLI</a> ·
  <a href="#자주-묻는-질문-faq">FAQ</a>
</p>

<p align="center">
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4"><img src="assets/one-pace-closer.gif" width="30%" alt="Wan 2.2 Spicy 이미지 투 비디오 예시"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4"><img src="assets/velvet-spiral-turn.gif" width="30%" alt="Seedance 2.0 Spicy 이미지 투 비디오 예시"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4"><img src="assets/silk-draught-pull.gif" width="30%" alt="Wan 2.7 Spicy 이미지 투 비디오 예시"></a>
  <br><sub>이 스킬이 호출하는 모델(Wan 2.2 Spicy, Seedance 2.0 Spicy, Wan 2.7 Spicy)의 실제 결과물입니다. 클릭하면 전체 영상을 볼 수 있습니다.</sub>
</p>

> **18세 이상 전용.** 이 스킬은 미성년자 또는 미성년자로 보이는 사람이 등장하는 성적 콘텐츠, 문서로 된 동의 없이 실존 인물을 다루는 성적 콘텐츠(페이스 스왑과 사진 "탈의" 포함), 사칭을 거부합니다. 모든 프롬프트에는 성인 나이를 명시해서 작성합니다.

---

## 이 스킬을 쓰는 이유

- **설정하지 말고 말로 요청하세요.** "이 사진을 5초짜리 부두아 영상으로 만들어 줘, 슬로 푸시인으로" → 에이전트가 모델을 고르고, 실시간 스키마를 읽고, 프롬프트를 쓰고, 가격을 보여 준 뒤 MP4를 저장합니다.
- **테스트로 뒷받침되는 모델 선택.** 스킬은 SpicyAPI가 공개한 리더보드를 따릅니다. 노골적인 테스트 프롬프트를 요청대로 렌더링한 모델(Wan 3.0, Seedance 2.5 Spicy, MiniMax H3 LoRA, Qwen Image 2.1…)을 기본으로 쓰고, 프롬프트를 순화하는 모델은 피합니다.
- **실제로 성인 콘텐츠 출력을 허용하는 Spicy 모델.** [SpicyAPI](https://spicyapi.ai/ko?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=why-ko)의 Spicy 에디션(Wan 2.2 Spicy, Seedance 2.x Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy, Z-Image Spicy, Qwen Image Edit Spicy)을 사용합니다. SpicyAPI는 모델 위에 자체 플랫폼 필터를 추가하지 않습니다.
- **실행 전에 가격을 먼저 확인합니다.** 모든 생성 작업은 먼저 견적을 내고, 사용자가 승인한 뒤에만(또는 사용자가 정한 예산 안에서만) 진행합니다. 실패한 작업은 자동으로 환불됩니다.
- **저렴합니다.** NSFW 영상은 **초당 $0.012–$0.019**부터, 무검열 이미지는 Qwen Image 2.1로 **$0.024**부터(Z-Image Spicy는 $0.01235부터)입니다. USD 잔액 방식이고 구독이 없으며, 카드나 암호화폐로 결제할 수 있습니다.
- **Spicy 모델만이 아니라 카탈로그의 모든 모델.** 같은 명령으로 Seedance 2.5, Wan 3.0, Seedream 5.0, Qwen Image, 업스케일러, 립싱크, 채팅 모델도 실행할 수 있습니다. `spicy.py models`에 나오는 모델 ID라면 무엇이든 넣으면 됩니다.
- **의존성 없음.** 표준 라이브러리만 쓰는 Python 파일 하나입니다. Python 3.9+가 돌아가는 곳이면 어디서든 작동합니다.
- **개인정보 보호를 기본으로 설계.** API 키는 환경 변수에만 둡니다. 프롬프트, 업로드 파일, 결과물은 SpicyAPI에서 보관 기간을 줄일 수 있습니다.

---

## 설치

### 1. API 키 발급

[spicyapi.ai](https://spicyapi.ai/ko/register?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-ko)에서 가입하고 잔액을 충전한 뒤(카드, Apple Pay / Google Pay, 암호화폐), [콘솔](https://spicyapi.ai/ko/console?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-ko)에서 키를 만드세요. 원한다면 키에 지출 한도를 설정할 수 있습니다.

```bash
export SPICY_API_KEY="sk-spicy-..."
```

### 2. 에이전트에 스킬 추가

**모든 에이전트 (skills CLI: Claude Code, Cursor, Codex, Windsurf, Gemini CLI, OpenClaw 등)**

```bash
npx skills add Spicy-API/nsfw-ai-skill
```

**Claude Code 플러그인 마켓플레이스**

```text
/plugin marketplace add Spicy-API/nsfw-ai-skill
/plugin install nsfw-ai@spicyapi-nsfw
```

**수동 설치**

```bash
git clone https://github.com/Spicy-API/nsfw-ai-skill.git
cp -r nsfw-ai-skill/skills/nsfw-ai ~/.claude/skills/        # Claude Code
# 또는: cp -r nsfw-ai-skill/skills/nsfw-ai ~/.codex/skills/   # Codex
# 또는: 에이전트의 skills 디렉터리가 skills/nsfw-ai를 가리키도록 설정
```

### 3. (선택) 공식 SpicyAPI MCP 서버 추가

스킬은 단독으로도 작동합니다. 클라이언트가 MCP를 지원한다면 모델 목록 조회, 견적, 작업 관리를 위해 SpicyAPI의 MCP 서버를 함께 추가할 수도 있습니다.

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

## 이렇게 요청할 수 있습니다

| 이렇게 말하면 | 스킬이 하는 일 |
|---|---|
| "Spicy 영상 모델 목록이랑 가격 알려 줘." | 실시간 카탈로그를 읽음 (키 불필요) |
| "`./frame.jpg`를 5초 영상으로 만들어 줘. 그녀가 카메라 쪽으로 돌아보고, 촛불 조명, 슬로 푸시인. 제일 싼 옵션으로." | 이미지를 업로드하고 Wan 2.2 Spicy 480p를 사용, 약 $0.095 견적을 보여 주고 승인을 기다린 뒤 MP4 저장 |
| "실사풍 첫 프레임: 새틴 시트 위 빨간 란제리를 입은 30대 여성. 그다음 그걸 영상으로 만들어 줘." | Qwen Image 2.1 → Wan 2.2 Spicy 또는 Seedance, 견적 두 번 |
| "그거 Seedance 2.0 Spicy로 720p 다시 렌더링하고, 마지막 프레임은 `end.jpg`로." | `last_image_url`을 넣어 Seedance 2.0 Spicy 실행 |
| "성인 데몬 퀸 애니 스틸 이미지를 만들고, 그걸 움직이게 해 줘." | Prefect Pony XL → Vidu Q3 Spicy |
| "`me.png`의 옷을 검은 새틴 슬립 드레스로 바꿔 줘." | Qwen Image 2.1 Edit (본인, 동의한 성인, 가상 캐릭터에만 사용) |
| "이 프레임용 NSFW 영상 프롬프트 세 개 써 주고 각각 비용 추정해 줘." | 프롬프트 레시피 + 견적, 사용자가 고를 때까지 아무것도 실행하지 않음 |
| "마지막 클립을 같은 LoRA로 5초 연장해 줘." | Wan 2.2 Spicy LoRA `video-extend` |
| "480p로 시드 변형 네 개 만들고, 제일 좋은 걸 720p로." | 총액 확인 후 일괄 실행 |

더 많은 예시는 [examples/prompts.md](examples/prompts.md)에 있습니다. 바로 쓸 수 있는 프롬프트 100개 이상은 **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.ko.md)** 저장소에 있습니다.

---

## 지원 모델과 가격

이 스킬은 SpicyAPI 카탈로그의 **모든** 모델을 호출할 수 있습니다. 아래는 성인 콘텐츠 작업에 중요한 모델로, 카탈로그 순서(인기순, 최신 버전순)이며 공개된 [SpicyAPI 리더보드](https://spicyapi.ai/ko/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ko)의 Spicy Index와 Freedom Score를 함께 실었습니다(✅ Freedom 90 이상 · ◐ 70–89 · ⚠️ 70 미만 · 🧪 테스트 실행 15회 미만). 🌶️ **Spicy** 에디션은 성인 콘텐츠 출력에 맞춰 튜닝된 버전입니다. 여기 실린 **Standard**(표준) 모델은 카탈로그 등급이 `unrestricted`여서 성인 프롬프트도 받아들이며, 텍스트 투 비디오와 레퍼런스 투 비디오도 지원합니다. 가격은 가장 저렴한 등급 기준이며, 스킬은 실행 전에 항상 정확한 견적을 보여 줍니다. 카탈로그 확인일: <!-- catalog:date -->
2026-09-27
<!-- /catalog:date -->

**영상**

<!-- catalog:video -->
| 모델 | 유형 | 작업 | 길이 | 최저가 | Spicy Index | Freedom |
|---|---|---|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/ko/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 4–30 s | $0.216/s | 56.5 | ✅ 96.7 |
| [Seedance 2.5](https://spicyapi.ai/ko/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 4–30 s | $0.1234/s | 69.5 | ◐ 80.9 |
| [Seedance 2.0 Spicy](https://spicyapi.ai/ko/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 4–15 s | $0.114/s | 61.5 | ✅ 93.3 |
| [Seedance 2.0](https://spicyapi.ai/ko/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 4–15 s | $0.07/s | 81.5 | ◐ 70.4 |
| [Wan 3.0 Prime](https://spicyapi.ai/ko/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 2–30 s | $0.0612/s | 76.5 | ◐ 78 |
| [Wan 3.0](https://spicyapi.ai/ko/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 2–30 s | $0.045/s | 76.5 | ✅ 96 |
| [MiniMax H3 Spicy](https://spicyapi.ai/ko/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 3–15 s | $0.038/s | 29.5 | ✅ 97.5 |
| [MiniMax H3](https://spicyapi.ai/ko/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 4–15 s | $0.025/s | 72.5 | 🧪 33.3 |
| [MiniMax H3 Singularity LoRA](https://spicyapi.ai/ko/models/minimax-h3-singularity-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V | 3–15 s | $0.06/s | 72.8 | ✅ 100 |
| [LTX 2.5](https://spicyapi.ai/ko/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, T2V | 5–20 s | $0.09/s | 66 | ◐ 80.3 |
| [Wan 3.0 Pro Prime](https://spicyapi.ai/ko/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 2–30 s | $0.234/s | 76.5 | ◐ 82 |
| [Wan 3.0 Pro](https://spicyapi.ai/ko/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 2–30 s | $0.144/s | 76.5 | ◐ 82 |
| [MiniMax H3 LoRA](https://spicyapi.ai/ko/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 3–15 s | $0.05/s | 75.2 | ✅ 98.3 |
| [HappyHorse 1.1](https://spicyapi.ai/ko/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 3–15 s | $0.14/s | 62.5 | ⚠️ 65.1 |
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ko/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 4–15 s | $0.0387/s | 44.5 | ✅ 93.3 |
| [Seedance 2.0 Mini](https://spicyapi.ai/ko/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 4–15 s | $0.01097/s | 64.5 | ⚠️ 64.9 |
| [Wan 2.7 Spicy](https://spicyapi.ai/ko/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 2–15 s | $0.1235/s | 46.5 | ✅ 100 |
| [LTX 2.3 Spicy](https://spicyapi.ai/ko/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 3–20 s | $0.019/s | 33.5 | ◐ 89.2 |
| [LTX 2.3 Spicy LoRA](https://spicyapi.ai/ko/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 3–20 s | $0.0285/s | 34.8 | ◐ 83.8 |
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ko/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 4–15 s | $0.081/s | 44.5 | ✅ 90 |
| [Seedance 2.0 Fast](https://spicyapi.ai/ko/models/seedance-2-0-fast?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 4–15 s | $0.02254/s | 64.5 | ⚠️ 68.2 |
| [Vidu Q3 Turbo](https://spicyapi.ai/ko/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V | 1–16 s | $0.042/s | 39.5 | ✅ 93.3 |
| [Vidu Q3 Spicy](https://spicyapi.ai/ko/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 1–16 s | $0.0665/s | 46.5 | ✅ 96.7 |
| [Vidu Q3](https://spicyapi.ai/ko/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V | 1–16 s | $0.07/s | 46.5 | ✅ 93.3 |
| [Vidu Q3 Pro](https://spicyapi.ai/ko/models/vidu-q3-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V | 1–16 s | $0.054/s | 36.5 | ✅ 93.3 |
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/ko/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 4–12 s | $0.012/s | 48.5 | ✅ 96.7 |
| [Seedance 1.5 Pro](https://spicyapi.ai/ko/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, T2V | 4–12 s | $0.0112/s | 46 | ✅ 90 |
| [Wan 2.6 Flash](https://spicyapi.ai/ko/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V | 5, 10, 15 s | $0.0225/s | 31.5 | ✅ 100 |
| [Wan 2.6 Spicy](https://spicyapi.ai/ko/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 5, 10, 15 s | $0.095/s | 46.5 | ✅ 96.7 |
| [Wan 2.6](https://spicyapi.ai/ko/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, Ref2V, T2V | 5, 10, 15 s | $0.065/s | 58.5 | 🧪 8.7 |
| [Wan 2.5](https://spicyapi.ai/ko/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V, T2V | 5, 10 s | $0.045/s | 46 | ✅ 99 |
| [Wan 2.2 Spicy](https://spicyapi.ai/ko/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V | 5, 8 s | $0.019/s | 23.5 | ✅ 91.2 |
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ko/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | I2V, Extend | 5, 8 s | $0.024/s | 25 | ◐ 74.8 |
| [Wan 2.2 LoRA](https://spicyapi.ai/ko/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | I2V | 5, 8 s | $0.024/s | 22.5 | ◐ 88.8 |
<!-- /catalog:video -->

**이미지** (추천: [Qwen Image 2.1](https://spicyapi.ai/ko/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ko), $0.024부터)

<!-- catalog:image -->
| 모델 | 유형 | 작업 | 최저가 | Spicy Index | Freedom |
|---|---|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/ko/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.024/image | 73 | ✅ 96.3 |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/ko/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.03/image | 80.5 | ✅ 92 |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/ko/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.042/image | 74.5 | ✅ 100 |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/ko/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.04/image | 56 | ✅ 98 |
| [Qwen Image 3.0](https://spicyapi.ai/ko/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.03/image | 56 | ✅ 96 |
| [Seedream 5.0 Pro](https://spicyapi.ai/ko/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.036/image | 73 | ✅ 94.3 |
| [Qwen Image Edit Spicy](https://spicyapi.ai/ko/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | Edit | $0.038/image | 14 | ✅ 96 |
| [Seedream 5.0 Lite](https://spicyapi.ai/ko/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.0345/image | 73 | ✅ 96 |
| [Qwen Image 2](https://spicyapi.ai/ko/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.035/image | 34 | ✅ 96.7 |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/ko/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.03/image | 50.5 | ✅ 92.5 |
| [Z-Image Spicy Pro](https://spicyapi.ai/ko/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | T2I | $0.019/image | 38 | ✅ 100 |
| [Z-Image Spicy](https://spicyapi.ai/ko/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 🌶️ Spicy | T2I | $0.01235/image | 32 | ✅ 98.8 |
| [Z-Image](https://spicyapi.ai/ko/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | T2I | $0.01/image | 17 | ✅ 100 |
| [Z-Image Turbo LoRA](https://spicyapi.ai/ko/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.012/image | 46.5 | ✅ 95 |
| [Seedream 4.0](https://spicyapi.ai/ko/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | Edit, T2I | $0.03/image | 74 | ◐ 74.7 |
| [Prefect Pony XL](https://spicyapi.ai/ko/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | T2I | $0.015/image | 30 | 🧪 36 |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/ko/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ko) | 표준 | T2I | $0.018/image | 32.5 | ◐ 75 |
<!-- /catalog:image -->

**텍스트** (OpenAI 호환 `chat` 명령): [Grok 4.7](https://spicyapi.ai/ko/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ko), [DeepSeek V4.1 Flash](https://spicyapi.ai/ko/models/deepseek-v4-1-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ko) 등 카탈로그 등급이 `unrestricted`인 모델, 1K 토큰당 $0.0012부터.

필드 단위 상세 레퍼런스: [skills/nsfw-ai/references/models.md](skills/nsfw-ai/references/models.md).

---

## 작동 방식

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

- 로컬 이미지는 SpicyAPI의 서명된 업로드 방식으로 올라가 `spicy://` URI로 전달됩니다. 공개 HTTPS URL은 그대로 전달됩니다.
- 모든 작업에는 멱등성 키(idempotency key)가 붙기 때문에, 요청을 재시도해도 중복 과금이 생기지 않습니다.
- 견적은 작업에 묶여 있어(`quoteId` + `expectedCost`), 최종 청구 금액이 승인한 가격을 넘을 수 없습니다.

---

## 에이전트 없이 CLI로 사용하기

같은 스크립트를 일반 CLI로 쓸 수 있습니다.

```bash
S=skills/nsfw-ai/scripts/spicy.py

python3 $S models --spicy --modality video          # 키 불필요
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

테스트는 `python3 -m unittest discover tests`로 실행합니다. 파이프라인 예시: [examples/image-to-video-pipeline.sh](examples/image-to-video-pipeline.sh), [examples/batch-variations.sh](examples/batch-variations.sh).

SDK를 선호한다면 SpicyAPI 공식 SDK가 있습니다: `npm install @spicyapi/sdk`, `pip install spicyapi`, `go get github.com/Spicy-API/spicy-go`, `composer require spicyapi/spicyapi`, 그리고 `@spicyapi/cli`. [개발자 문서](https://docs.spicyapi.ai/docs?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=sdk)를 참고하세요.

---

## 저장소 구조

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

## 자주 묻는 질문 (FAQ)

### Claude Code로 NSFW 이미지나 영상을 만들 수 있나요?
Claude Code 자체는 미디어를 생성하지 않습니다. 이 스킬을 설치하면 Claude Code(그리고 Cursor, Codex, Windsurf, Gemini CLI, OpenClaw)가 성인 콘텐츠 출력을 허용하는 SpicyAPI의 Spicy 모델을 호출하고, 결과 파일을 로컬에 저장합니다. 스킬에는 넘을 수 없는 제한이 있습니다. 성인만 허용되고, 동의 없는 실존 인물은 금지됩니다.

### 가장 저렴한 NSFW 이미지 투 비디오 API는?
SpicyAPI 카탈로그(2026-09-27) 기준으로 노골적 테스트를 통과한 가장 저렴한 모델은 Seedance 1.5 Pro Spicy(480p 초당 $0.012부터, Freedom 96.7)와 Wan 2.6 Flash(720p 초당 $0.0225, Freedom 100)입니다. 비용 대비 결과가 가장 좋은 모델은 Wan 3.0으로, 720p 5초 클립 하나에 $0.45이며 Freedom은 96입니다.

### 무료 NSFW AI 스킬이 있나요?
이 스킬 자체는 무료 오픈소스(MIT)입니다. 생성은 GPU 비용 때문에 SpicyAPI에서 결과물 단위로 유료이며, 구독은 없고 실패한 작업은 환불됩니다. 무료로 생성하려면 오픈 웨이트 모델을 로컬에서 실행하세요([awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.ko.md#셀프-호스팅-및-오픈-웨이트-모델) 참고).

### Spicy가 아닌 모델도 호출할 수 있나요?
네. 성인 콘텐츠 요청에는 Spicy 에디션이 기본값이지만, `spicy.py`는 SpicyAPI 카탈로그의 모든 모델 ID를 받습니다. 표준 Seedance / Wan / MiniMax 영상 모델, Seedream / Qwen / Wan 이미지 모델, 업스케일러, 얼굴 및 립싱크 도구, 그리고 `chat`을 통한 텍스트 모델까지 가능합니다. `spicy.py models`를 `--spicy` 없이 실행하면 목록을 볼 수 있습니다.

### MCP와 함께 쓸 수 있나요?
네. 스킬만 단독으로 쓰거나, 공식 SpicyAPI MCP 서버(`@spicyapi/mcp`)를 함께 추가할 수 있습니다.

### 파일은 어디에 저장되고, SpicyAPI는 무엇을 보관하나요?
결과물은 `./spicy-output/`에 다운로드됩니다. 결과물 링크는 약 20분 뒤 만료됩니다. SpicyAPI는 프롬프트, 업로드 파일, 결과물을 각각 별도의 보관 기간으로 관리하며 이 기간은 줄일 수 있고, 완료된 작업의 콘텐츠를 파기할 수도 있습니다. [Trust](https://spicyapi.ai/ko/trust?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=faq-ko) 페이지를 참고하세요.

### 애니메이션 / 헨타이 스타일에는 어떤 모델을 써야 하나요?
스틸 이미지는 애니 LoRA를 붙인 Qwen Image 2.1 LoRA(성인 캐릭터 디자인. 이미지 리더보드 1위, Freedom 92), 움직임은 Vidu Q3 Spicy(Freedom 96.7) 또는 같은 LoRA를 붙인 Wan 2.2 Spicy LoRA를 쓰세요. Prefect Pony XL은 태그 방식 프롬프트로 쓸 수 있지만 아직 테스트 데이터가 적습니다.

### 작업이 실패하는 이유는?
모델 제공업체가 일부 입력을 여전히 거부할 수 있습니다. 이 경우 실패한 작업으로 표시되고 요금은 환불됩니다. 표현을 바꾸거나 다른 Spicy 모델을 시도해 보세요. `40004` 오류는 선택한 파라미터 조합이 지원되지 않는다는 뜻이니, 오류에 나온 필드를 바꾸세요.

---

## 규칙

성인만 허용됩니다. 18세 미만이거나 18세 미만으로 보이는 사람이 등장하는 성적 콘텐츠는 어떤 스타일로도 금지됩니다. 문서로 된 동의가 없는 실존 인물의 성적 콘텐츠, 성적 콘텐츠로의 페이스 스왑, 실제 사진을 "탈의"시키는 행위는 금지됩니다. 본인과 시청자가 있는 곳의 법률을 지키세요. 모든 요청에는 SpicyAPI의 [콘텐츠 정책](https://spicyapi.ai/ko/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-ko)과 [허용 사용 정책](https://spicyapi.ai/ko/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-ko)이 적용됩니다.

## 관련 저장소

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.ko.md)**: 무검열 AI 이미지·영상·텍스트 도구, API, 모델을 엄선한 목록.
- **[nsfw-ai-image-prompts](https://github.com/Spicy-API/nsfw-ai-image-prompts/blob/main/README.ko.md)**: NSFW 이미지·편집 프롬프트 104개와 실제 결과물 사례.
- **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.ko.md)**: NSFW 영상 프롬프트 100개 이상, 첫 프레임 프롬프트, 검증된 예시.
- **[spicy-skill](https://github.com/Spicy-API/spicy-skill)**: SpicyAPI 공식 범용 스킬.

## 라이선스

[MIT](LICENSE)

<p align="center"><sub>⭐ API 문서 읽는 오후 시간을 아껴 줬다면 스타를 눌러 주세요.</sub></p>
