<!--
  Keywords: NSFW AI スキル, NSFW エージェントスキル, Claude Code NSFW, Claude Code エロ画像生成, 無修正 AI スキル, NSFW MCP,
  NSFW AI API, エロ AI 画像生成 API, 無修正 AI 動画生成 API, AI 画像から動画 API, NSFW 画像から動画, NSFW AI 画像編集 API,
  Wan 2.2 Spicy API, Seedance Spicy API, Cursor NSFW, Codex スキル, OpenClaw スキル, SpicyAPI,
  nsfw ai skill, claude code nsfw, uncensored ai skill, nsfw image to video api, uncensored ai image generator api
-->

<p align="center"><a href="README.md">English</a> · <b>日本語</b> · <a href="README.ko.md">한국어</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a></p>

<h1 align="center">NSFW AI Skill</h1>

<p align="center">
  <b>Claude Code、Cursor、Codex、Windsurf、Gemini CLI、OpenClaw から、成人向け（18+）画像の生成、NSFW の画像から動画、無修正の画像編集、無検閲のテキスト生成ができるエージェントスキル。従量課金の API 1 つで動きます。</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skill-agentskills-8b5cf6" alt="エージェントスキル">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Claude Code プラグイン">
  <img src="https://img.shields.io/badge/python-3.9%2B%2C%20no%20deps-3776ab" alt="Python 3.9+、依存パッケージなし">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18 歳以上">
</p>

<p align="center">
  <a href="#インストール">インストール</a> ·
  <a href="#頼めること">頼めること</a> ·
  <a href="#対応モデルと料金">モデルと料金</a> ·
  <a href="#仕組み">仕組み</a> ·
  <a href="#エージェントなしで使う">CLI</a> ·
  <a href="#よくある質問">よくある質問</a>
</p>

<p align="center">
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4"><img src="assets/one-pace-closer.gif" width="30%" alt="Wan 2.2 Spicy の画像から動画の例"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4"><img src="assets/velvet-spiral-turn.gif" width="30%" alt="Seedance 2.0 Spicy の画像から動画の例"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4"><img src="assets/silk-draught-pull.gif" width="30%" alt="Wan 2.7 Spicy の画像から動画の例"></a>
  <br><sub>このスキルが呼び出すモデル（Wan 2.2 Spicy、Seedance 2.0 Spicy、Wan 2.7 Spicy）の実際の出力です。クリックすると動画全体を見られます。</sub>
</p>

> **18 歳以上限定。** このスキルは、未成年または未成年に見える人物が関わる性的コンテンツ、記録に残る同意のない実在の人物の性的コンテンツ（フェイススワップや写真の「脱がせ」を含む）、なりすましを拒否します。すべてのプロンプトには成人の年齢を明記して書きます。

---

## このスキルの特長

- **設定せずに、話すだけ。**「この写真を 5 秒のブドワール動画にして、ゆっくり寄るカメラで」と頼むと、エージェントがモデルを選び、最新のスキーマを読み、プロンプトを書き、価格を見せてから MP4 を保存します。
- **テスト結果にもとづくモデル選び。** スキルは SpicyAPI が公開しているリーダーボードに従います。露骨なテストプロンプトを指示どおりに生成できたモデル（Wan 3.0、Seedance 2.5 Spicy、MiniMax H3 LoRA、Qwen Image 2.1…）をデフォルトにし、表現を弱めてしまうモデルは避けます。
- **成人向けの出力が本当に通る Spicy モデル。** [SpicyAPI](https://spicyapi.ai/ja?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=why-ja) の Spicy 版（Wan 2.2 Spicy、Seedance 2.x Spicy、MiniMax H3 Spicy、LTX 2.3 Spicy、Vidu Q3 Spicy、Z-Image Spicy、Qwen Image Edit Spicy）を使います。SpicyAPI はモデルの上にプラットフォーム独自のフィルターを追加しません。
- **実行前に必ず価格がわかる。** すべての生成は先に見積もりを出し、あなたが承認するまで（または設定した予算の範囲内でなければ）実行しません。失敗したタスクは自動で返金されます。
- **安い。** NSFW 動画は **1 秒 $0.012〜$0.019** から、無修正の画像は Qwen Image 2.1 で **$0.024** から（Z-Image Spicy なら $0.01235）。USD 残高制、サブスクなし、カードか暗号資産で支払えます。
- **Spicy だけでなくカタログの全モデルに対応。** 同じコマンドで Seedance 2.5、Wan 3.0、Seedream 5.0、Qwen Image、アップスケーラー、リップシンク、チャットモデルも動きます。`spicy.py models` に出てくるモデル ID ならどれでも渡せます。
- **依存パッケージゼロ。** 標準ライブラリだけを使う Python ファイル 1 つ。Python 3.9 以上が動く環境ならどこでも使えます。
- **プライバシーに配慮した設計。** API キーは環境変数に置いたままです。プロンプト、アップロード、出力には保持期間があり、SpicyAPI 側で短くできます。

---

## インストール

### 1. API キーを取得する

[spicyapi.ai](https://spicyapi.ai/ja/register?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-ja) で登録し、残高をチャージ（カード、Apple Pay / Google Pay、暗号資産）してから、[コンソール](https://spicyapi.ai/ja/console?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-ja)でキーを作成します。必要ならキーに利用上限を設定できます。

```bash
export SPICY_API_KEY="sk-spicy-..."
```

### 2. エージェントにスキルを追加する

**どのエージェントでも（skills CLI：Claude Code、Cursor、Codex、Windsurf、Gemini CLI、OpenClaw など）**

```bash
npx skills add Spicy-API/nsfw-ai-skill
```

**Claude Code のプラグインマーケットプレイス**

```text
/plugin marketplace add Spicy-API/nsfw-ai-skill
/plugin install nsfw-ai@spicyapi-nsfw
```

**手動**

```bash
git clone https://github.com/Spicy-API/nsfw-ai-skill.git
cp -r nsfw-ai-skill/skills/nsfw-ai ~/.claude/skills/        # Claude Code
# または: cp -r nsfw-ai-skill/skills/nsfw-ai ~/.codex/skills/   # Codex
# または: エージェントの skills ディレクトリを skills/nsfw-ai に向ける
```

### 3. （任意）公式 SpicyAPI MCP サーバーを追加する

スキルは単体で動きます。クライアントが MCP に対応していれば、モデル一覧、見積もり、タスク管理のために SpicyAPI の MCP サーバーを追加することもできます。

```bash
claude mcp add spicyapi -e SPICY_API_KEY=$SPICY_API_KEY -- npx --yes --package=@spicyapi/mcp spicyapi-mcp
```

Cursor / Claude Desktop / Windsurf（`mcp.json`）：

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

## 頼めること

| あなたの言葉 | スキルがすること |
|---|---|
| 「Spicy の動画モデルと料金を一覧で見せて」 | 最新のカタログを読む（キー不要） |
| 「`./frame.jpg` を 5 秒の動画にして。彼女がカメラの方へ振り向く、キャンドルの光、ゆっくり寄る。いちばん安い方法で」 | 画像をアップロードし、Wan 2.2 Spicy の 480p を使い、約 $0.095 と見積もって、OK を待ってから MP4 を保存 |
| 「フォトリアルな開始フレームを作って。サテンのシーツの上で赤いランジェリーを着た 30 代の女性。それから動かして」 | Qwen Image 2.1 → Wan 2.2 Spicy または Seedance、見積もりは 2 回 |
| 「それを Seedance 2.0 Spicy の 720p で作り直して。最後のフレームは `end.jpg` で」 | `last_image_url` を指定して Seedance 2.0 Spicy |
| 「成人の魔王女王のアニメ静止画を作って、それを動かして」 | Prefect Pony XL → Vidu Q3 Spicy |
| 「`me.png` の服を黒いサテンのスリップドレスに変えて」 | Qwen Image 2.1 Edit（あなた自身、同意した成人、または架空のキャラクターのみ） |
| 「このフレーム用に NSFW 動画プロンプトを 3 つ書いて、それぞれ見積もって」 | プロンプトのレシピ + 見積もり。選ぶまで何も実行しない |
| 「さっきの動画を同じ LoRA で 5 秒延長して」 | Wan 2.2 Spicy LoRA の `video-extend` |
| 「480p でシード違いを 4 本、いちばん良いものを 720p で」 | 合計金額を確認してからバッチ実行 |

ほかのアイデアは [examples/prompts.md](examples/prompts.md) に。すぐ使えるプロンプト 100 本以上は **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.ja.md)** にあります。

---

## 対応モデルと料金

このスキルは SpicyAPI カタログの**どの**モデルでも呼び出せます。ここでは成人向けの制作で重要なものを、カタログ順（人気順、新しいバージョンが先）に、公開されている [SpicyAPI リーダーボード](https://spicyapi.ai/ja/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ja)の Spicy Index と Freedom Score を付けて載せています（✅ Freedom 90 以上 · ◐ 70–89 · ⚠️ 70 未満 · 🧪 テスト実行 15 回未満）。🌶️ **Spicy** 版は成人向けの出力に合わせて調整されています。ここに載せている**標準**モデルはカタログ上のティアが `unrestricted` なので、成人向けのプロンプトも通り、テキストから動画と参照画像から動画にも対応します。表示しているのは最安ティアで、スキルは実行前に必ず正確な見積もりを表示します。カタログ取得日: <!-- catalog:date -->
2026-09-27
<!-- /catalog:date -->

**動画**

<!-- catalog:video -->
| モデル | 種類 | タスク | 長さ | 最低価格 | Spicy Index | Freedom |
|---|---|---|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/ja/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 4–30 s | $0.216/s | 56.5 | ✅ 96.7 |
| [Seedance 2.5](https://spicyapi.ai/ja/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 4–30 s | $0.1234/s | 69.5 | ◐ 80.9 |
| [Seedance 2.0 Spicy](https://spicyapi.ai/ja/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 4–15 s | $0.114/s | 61.5 | ✅ 93.3 |
| [Seedance 2.0](https://spicyapi.ai/ja/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 4–15 s | $0.07/s | 81.5 | ◐ 70.4 |
| [Wan 3.0 Prime](https://spicyapi.ai/ja/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 2–30 s | $0.0612/s | 76.5 | ◐ 78 |
| [Wan 3.0](https://spicyapi.ai/ja/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 2–30 s | $0.045/s | 76.5 | ✅ 96 |
| [MiniMax H3 Spicy](https://spicyapi.ai/ja/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 3–15 s | $0.038/s | 29.5 | ✅ 97.5 |
| [MiniMax H3](https://spicyapi.ai/ja/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 4–15 s | $0.025/s | 72.5 | 🧪 33.3 |
| [MiniMax H3 Singularity LoRA](https://spicyapi.ai/ja/models/minimax-h3-singularity-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V | 3–15 s | $0.06/s | 72.8 | ✅ 100 |
| [LTX 2.5](https://spicyapi.ai/ja/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, T2V | 5–20 s | $0.09/s | 66 | ◐ 80.3 |
| [Wan 3.0 Pro Prime](https://spicyapi.ai/ja/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 2–30 s | $0.234/s | 76.5 | ◐ 82 |
| [Wan 3.0 Pro](https://spicyapi.ai/ja/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 2–30 s | $0.144/s | 76.5 | ◐ 82 |
| [MiniMax H3 LoRA](https://spicyapi.ai/ja/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 3–15 s | $0.05/s | 75.2 | ✅ 98.3 |
| [HappyHorse 1.1](https://spicyapi.ai/ja/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 3–15 s | $0.14/s | 62.5 | ⚠️ 65.1 |
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ja/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 4–15 s | $0.0387/s | 44.5 | ✅ 93.3 |
| [Seedance 2.0 Mini](https://spicyapi.ai/ja/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 4–15 s | $0.01097/s | 64.5 | ⚠️ 64.9 |
| [Wan 2.7 Spicy](https://spicyapi.ai/ja/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 2–15 s | $0.1235/s | 46.5 | ✅ 100 |
| [LTX 2.3 Spicy](https://spicyapi.ai/ja/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 3–20 s | $0.019/s | 33.5 | ◐ 89.2 |
| [LTX 2.3 Spicy LoRA](https://spicyapi.ai/ja/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 3–20 s | $0.0285/s | 34.8 | ◐ 83.8 |
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ja/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 4–15 s | $0.081/s | 44.5 | ✅ 90 |
| [Seedance 2.0 Fast](https://spicyapi.ai/ja/models/seedance-2-0-fast?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 4–15 s | $0.02254/s | 64.5 | ⚠️ 68.2 |
| [Vidu Q3 Turbo](https://spicyapi.ai/ja/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V | 1–16 s | $0.042/s | 39.5 | ✅ 93.3 |
| [Vidu Q3 Spicy](https://spicyapi.ai/ja/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 1–16 s | $0.0665/s | 46.5 | ✅ 96.7 |
| [Vidu Q3](https://spicyapi.ai/ja/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V | 1–16 s | $0.07/s | 46.5 | ✅ 93.3 |
| [Vidu Q3 Pro](https://spicyapi.ai/ja/models/vidu-q3-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V | 1–16 s | $0.054/s | 36.5 | ✅ 93.3 |
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/ja/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 4–12 s | $0.012/s | 48.5 | ✅ 96.7 |
| [Seedance 1.5 Pro](https://spicyapi.ai/ja/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, T2V | 4–12 s | $0.0112/s | 46 | ✅ 90 |
| [Wan 2.6 Flash](https://spicyapi.ai/ja/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V | 5, 10, 15 s | $0.0225/s | 31.5 | ✅ 100 |
| [Wan 2.6 Spicy](https://spicyapi.ai/ja/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 5, 10, 15 s | $0.095/s | 46.5 | ✅ 96.7 |
| [Wan 2.6](https://spicyapi.ai/ja/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, Ref2V, T2V | 5, 10, 15 s | $0.065/s | 58.5 | 🧪 8.7 |
| [Wan 2.5](https://spicyapi.ai/ja/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V, T2V | 5, 10 s | $0.045/s | 46 | ✅ 99 |
| [Wan 2.2 Spicy](https://spicyapi.ai/ja/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V | 5, 8 s | $0.019/s | 23.5 | ✅ 91.2 |
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ja/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | I2V, Extend | 5, 8 s | $0.024/s | 25 | ◐ 74.8 |
| [Wan 2.2 LoRA](https://spicyapi.ai/ja/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | I2V | 5, 8 s | $0.024/s | 22.5 | ◐ 88.8 |
<!-- /catalog:video -->

**画像**（おすすめ：[Qwen Image 2.1](https://spicyapi.ai/ja/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ja)、$0.024 から）

<!-- catalog:image -->
| モデル | 種類 | タスク | 最低価格 | Spicy Index | Freedom |
|---|---|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/ja/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.024/image | 73 | ✅ 96.3 |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/ja/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.03/image | 80.5 | ✅ 92 |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/ja/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.042/image | 74.5 | ✅ 100 |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/ja/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.04/image | 56 | ✅ 98 |
| [Qwen Image 3.0](https://spicyapi.ai/ja/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.03/image | 56 | ✅ 96 |
| [Seedream 5.0 Pro](https://spicyapi.ai/ja/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.036/image | 73 | ✅ 94.3 |
| [Qwen Image Edit Spicy](https://spicyapi.ai/ja/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | Edit | $0.038/image | 14 | ✅ 96 |
| [Seedream 5.0 Lite](https://spicyapi.ai/ja/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.0345/image | 73 | ✅ 96 |
| [Qwen Image 2](https://spicyapi.ai/ja/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.035/image | 34 | ✅ 96.7 |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/ja/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.03/image | 50.5 | ✅ 92.5 |
| [Z-Image Spicy Pro](https://spicyapi.ai/ja/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | T2I | $0.019/image | 38 | ✅ 100 |
| [Z-Image Spicy](https://spicyapi.ai/ja/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 🌶️ Spicy | T2I | $0.01235/image | 32 | ✅ 98.8 |
| [Z-Image](https://spicyapi.ai/ja/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | T2I | $0.01/image | 17 | ✅ 100 |
| [Z-Image Turbo LoRA](https://spicyapi.ai/ja/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.012/image | 46.5 | ✅ 95 |
| [Seedream 4.0](https://spicyapi.ai/ja/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | Edit, T2I | $0.03/image | 74 | ◐ 74.7 |
| [Prefect Pony XL](https://spicyapi.ai/ja/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | T2I | $0.015/image | 30 | 🧪 36 |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/ja/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ja) | 標準 | T2I | $0.018/image | 32.5 | ◐ 75 |
<!-- /catalog:image -->

**テキスト**（OpenAI 互換の `chat` コマンド）：[Grok 4.7](https://spicyapi.ai/ja/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ja)、[DeepSeek V4.1 Flash](https://spicyapi.ai/ja/models/deepseek-v4-1-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ja) など、カタログ上のティアが `unrestricted` のモデル。1K トークンあたり $0.0012 から。

フィールド単位の詳しいリファレンス：[skills/nsfw-ai/references/models.md](skills/nsfw-ai/references/models.md)。

---

## 仕組み

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

流れ：エージェントが SKILL.md を読み込み、① リクエストが成人限定・同意のルールに反していないか確認、② モデルを選ぶ（または最新のモデルを一覧表示）、③ 最新の入力スキーマを読む、④ プロンプトを書く、⑤ 見積もりを出して承認を求める、⑥ OK が出たら実行、という順で進みます。

- ローカルの画像は SpicyAPI の署名付きアップロードでアップロードされ、`spicy://` URI として渡されます。公開されている HTTPS の URL はそのまま渡されます。
- 各タスクには冪等キー（Idempotency-Key）が付くので、リクエストを再送しても二重に課金されることはありません。
- 見積もりはタスクに紐づけられる（`quoteId` + `expectedCost`）ため、確定した請求額が承認した金額を超えることはありません。

---

## エージェントなしで使う

同じスクリプトは普通の CLI としても使えます。

```bash
S=skills/nsfw-ai/scripts/spicy.py

python3 $S models --spicy --modality video          # キー不要
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

テストは `python3 -m unittest discover tests` で実行できます。パイプラインの例：[examples/image-to-video-pipeline.sh](examples/image-to-video-pipeline.sh)、[examples/batch-variations.sh](examples/batch-variations.sh)。

SDK を使いたい場合は、SpicyAPI の公式 SDK があります：`npm install @spicyapi/sdk`、`pip install spicyapi`、`go get github.com/Spicy-API/spicy-go`、`composer require spicyapi/spicyapi`、そして `@spicyapi/cli`。[開発者ドキュメント](https://docs.spicyapi.ai/docs?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=sdk)を参照してください。

---

## リポジトリ構成

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

- `SKILL.md`：エージェントが読み込む指示書
- `scripts/spicy.py`：依存パッケージゼロの SpicyAPI CLI
- `references/models.md`：モデル ID、フィールド、価格ティア
- `references/prompting.md`：プロンプトのレシピ、ネガティブ、カップル、アニメ
- `agents/openai.yaml`：Codex / OpenAI エージェント用のメタデータ
- `.claude-plugin/`：Claude Code プラグインとマーケットプレイスのマニフェスト
- `examples/`：パイプラインと頼み方の例
- `tests/`：オフラインのユニットテスト

---

## よくある質問

### Claude Code でエロ画像や NSFW 動画は生成できる？
Claude Code 自体はメディアを生成しません。このスキルを入れると、Claude Code（および Cursor、Codex、Windsurf、Gemini CLI、OpenClaw）が、成人向けの出力を許可している SpicyAPI の Spicy モデルを呼び出し、ファイルをローカルに保存します。スキルには越えられない制限があります：成人のみ、同意のない実在の人物は不可。

### いちばん安い NSFW 画像から動画 API は？
SpicyAPI のカタログ（2026-09-27）で、露骨なテストに合格したモデルの中でいちばん安いのは、Seedance 1.5 Pro Spicy（480p で $0.012/s から、Freedom 96.7）と Wan 2.6 Flash（720p で $0.0225/s、Freedom 100）です。1 ドルあたりの仕上がりで選ぶなら、Wan 3.0 が 720p の 5 秒動画 1 本 $0.45、Freedom 96 です。

### 無料の NSFW AI スキルはある？
このスキル自体は無料のオープンソース（MIT）です。生成は GPU にお金がかかるため SpicyAPI で出力ごとに課金されますが、サブスクリプションはなく、失敗したタスクは返金されます。無料で生成したいなら、オープンウェイトモデルをローカルで動かしてください（[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.ja.md#セルフホストオープンウェイトモデル) を参照）。

### 「Spicy」以外のモデルも呼び出せる？
呼び出せます。成人向けのリクエストでは Spicy 版がデフォルトですが、`spicy.py` は SpicyAPI カタログのどのモデル ID でも受け付けます。標準の Seedance / Wan / MiniMax 動画モデル、Seedream / Qwen / Wan 画像モデル、アップスケーラー、顔・リップシンクのツール、`chat` 経由のテキストモデルなどです。`spicy.py models`（`--spicy` なし）で一覧を表示できます。

### MCP でも使える？
使えます。スキル単体で使うことも、公式の SpicyAPI MCP サーバー（`@spicyapi/mcp`）と併用することもできます。

### ファイルはどこに保存される？SpicyAPI には何が残る？
出力は `./spicy-output/` にダウンロードされます。出力のリンクは約 20 分で失効します。SpicyAPI はプロンプト、アップロード、出力をそれぞれ別の保持期間で保管し、その期間は短くできます。完了したタスクの内容を削除することもできます。詳しくは [Trust](https://spicyapi.ai/ja/trust?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=faq-ja) を参照してください。

### アニメ・エロアニメ風のコンテンツにはどのモデルがいい？
静止画はアニメ LoRA を付けた Qwen Image 2.1 LoRA（成人のキャラクターデザイン。画像リーダーボード 1 位、Freedom 92）、動きは Vidu Q3 Spicy（Freedom 96.7）、または同じ LoRA を付けた Wan 2.2 Spicy LoRA です。Prefect Pony XL はタグ形式のプロンプトで使えますが、今のところテストデータがほとんどありません。

### タスクが失敗したのはなぜ？
モデルプロバイダー側で一部の入力が拒否されることがあります。その場合はタスクが失敗扱いになり、料金は返金されます。言い回しを変えるか、別の Spicy モデルを試してください。`40004` エラーは、選んだパラメーターの組み合わせが提供されていないという意味です。エラーに書かれたフィールドを変更してください。

---

## ルール

成人のみ。18 歳未満の人物、または 18 歳未満に見える人物が関わる性的コンテンツは、どんな画風でも禁止です。記録に残る同意のない実在の人物の性的コンテンツ、性的コンテンツへのフェイススワップ、実在の人物の写真の「脱がせ」は禁止です。あなたと視聴者がいる地域の法律に従ってください。SpicyAPI の[コンテンツポリシー](https://spicyapi.ai/ja/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-ja)と[利用上のルール](https://spicyapi.ai/ja/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-ja)がすべてのリクエストに適用されます。

## 関連リポジトリ

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.ja.md)**：無修正の AI 画像・動画・テキストツール、API、モデルをまとめたリスト。
- **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.ja.md)**：NSFW 動画プロンプト 100 本以上、開始フレーム用プロンプト、検証済みの例。
- **[spicy-skill](https://github.com/Spicy-API/spicy-skill)**：SpicyAPI 公式の汎用スキル。

## ライセンス

[MIT](LICENSE)

<p align="center"><sub>API ドキュメントを読む手間が省けたら ⭐ Star をお願いします。</sub></p>
