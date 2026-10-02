<!--
  Keywords: NSFW AI скилл, NSFW скилл для агента, Claude Code NSFW, нейросеть 18+, ИИ без цензуры, NSFW MCP,
  NSFW AI API, API генерации изображений без цензуры, API генерации видео без цензуры, генерация видео из изображения API,
  NSFW видео из фото, NSFW редактор изображений API, Wan 2.2 Spicy API, Seedance Spicy API, Cursor NSFW, Codex скилл,
  OpenClaw скилл, SpicyAPI, nsfw ai skill, claude code nsfw, uncensored ai skill, nsfw image to video api
-->

<p align="center"><a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <b>Русский</b></p>

<h1 align="center">NSFW AI Skill</h1>

<p align="center">
  <b>Скилл для агентов, с которым Claude Code, Cursor, Codex, Windsurf, Gemini CLI и OpenClaw генерируют изображения для взрослых (18+), NSFW-видео из изображений, редактируют картинки и пишут тексты без цензуры — через один API с оплатой по факту использования.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skill-agentskills-8b5cf6" alt="Скилл для агентов">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Плагин для Claude Code">
  <img src="https://img.shields.io/badge/python-3.9%2B%2C%20no%20deps-3776ab" alt="Python 3.9+, без зависимостей">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#установка">Установка</a> ·
  <a href="#что-можно-попросить">Что можно попросить</a> ·
  <a href="#поддерживаемые-модели-и-цены">Модели и цены</a> ·
  <a href="#как-это-работает">Как это работает</a> ·
  <a href="#использование-без-агента">CLI</a> ·
  <a href="#частые-вопросы">FAQ</a>
</p>

<p align="center">
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4"><img src="assets/one-pace-closer.gif" width="30%" alt="Пример генерации видео из изображения на Wan 2.2 Spicy"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4"><img src="assets/velvet-spiral-turn.gif" width="30%" alt="Пример генерации видео из изображения на Seedance 2.0 Spicy"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4"><img src="assets/silk-draught-pull.gif" width="30%" alt="Пример генерации видео из изображения на Wan 2.7 Spicy"></a>
  <br><sub>Реальные результаты моделей, которые вызывает этот скилл (Wan 2.2 Spicy, Seedance 2.0 Spicy, Wan 2.7 Spicy). Нажмите, чтобы посмотреть ролик целиком.</sub>
</p>

> **Только 18+.** Скилл отказывается создавать сексуальный контент с участием несовершеннолетних или тех, кто выглядит несовершеннолетним, сексуальный контент с реальными людьми без документально подтверждённого согласия (включая замену лиц и «раздевание» фотографий), а также выдавать себя за других людей. В каждом промпте он явно указывает взрослый возраст.

---

## Почему этот скилл

- **Говорите, а не настраивайте.** «Оживи это фото: 5-секундный ролик в стиле будуар, медленный наезд камеры» → агент выбирает модель, читает её актуальную схему, пишет промпт, показывает цену и сохраняет MP4.
- **Выбор моделей подкреплён тестами.** Скилл опирается на публичный лидерборд SpicyAPI: по умолчанию он берёт модели, которые выполнили откровенные тестовые промпты так, как было запрошено (Wan 3.0, Seedance 2.5 Spicy, MiniMax H3 LoRA, Qwen Image 2.1…), и обходит те, что их смягчают.
- **Spicy-модели, которые действительно разрешают контент для взрослых.** Используются Spicy-версии моделей от [SpicyAPI](https://spicyapi.ai/ru?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=why-ru) (Wan 2.2 Spicy, Seedance 2.x Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy, Z-Image Spicy, Qwen Image Edit Spicy). SpicyAPI не добавляет поверх модели собственный фильтр платформы.
- **Цена видна до запуска.** Для каждой генерации сначала выставляется смета; агент продолжает только после вашего подтверждения (или в рамках заданного вами бюджета). Деньги за неудавшиеся задачи возвращаются автоматически.
- **Недорого.** NSFW-видео от **$0.012–$0.019 за секунду**, изображения без цензуры от **$0.024** на Qwen Image 2.1 (или $0.01235 на Z-Image Spicy). Баланс в долларах США, без подписки, оплата картой или криптовалютой.
- **Весь каталог моделей, а не только Spicy.** Те же команды запускают Seedance 2.5, Wan 3.0, Seedream 5.0, Qwen Image, апскейлеры, липсинк и чат-модели; передайте любой ID модели из `spicy.py models`.
- **Ноль зависимостей.** Один файл на Python только со стандартной библиотекой. Работает везде, где есть Python 3.9+.
- **Приватность по умолчанию.** API-ключ остаётся в переменной окружения. У промптов, загрузок и результатов есть сроки хранения, которые можно сократить в SpicyAPI.

---

## Установка

### 1. Получите API-ключ

Зарегистрируйтесь на [spicyapi.ai](https://spicyapi.ai/ru/register?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-ru), пополните баланс (карта, Apple Pay / Google Pay или криптовалюта) и создайте ключ в [Консоли](https://spicyapi.ai/ru/console?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-ru). При желании задайте для ключа лимит расходов.

```bash
export SPICY_API_KEY="sk-spicy-..."
```

### 2. Добавьте скилл в своего агента

**Любой агент (skills CLI: Claude Code, Cursor, Codex, Windsurf, Gemini CLI, OpenClaw и другие)**

```bash
npx skills add Spicy-API/nsfw-ai-skill
```

**Маркетплейс плагинов Claude Code**

```text
/plugin marketplace add Spicy-API/nsfw-ai-skill
/plugin install nsfw-ai@spicyapi-nsfw
```

**Вручную**

```bash
git clone https://github.com/Spicy-API/nsfw-ai-skill.git
cp -r nsfw-ai-skill/skills/nsfw-ai ~/.claude/skills/        # Claude Code
# или: cp -r nsfw-ai-skill/skills/nsfw-ai ~/.codex/skills/   # Codex
# или: направьте каталог skills вашего агента на skills/nsfw-ai
```

### 3. (Необязательно) Подключите официальный MCP-сервер SpicyAPI

Скилл работает сам по себе. Если ваш клиент поддерживает MCP, можно также подключить MCP-сервер SpicyAPI для списка моделей, смет и управления задачами:

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

## Что можно попросить

| Вы говорите | Что делает скилл |
|---|---|
| «Покажи Spicy-модели для видео и сколько они стоят». | Читает актуальный каталог (ключ не нужен) |
| «Сделай из `./frame.jpg` 5-секундный ролик: она поворачивается к камере, свет свечей, медленный наезд. Самый дешёвый вариант». | Загружает изображение, берёт Wan 2.2 Spicy в 480p, выставляет смету ~$0.095, ждёт вашего OK и сохраняет MP4 |
| «Фотореалистичный первый кадр: женщина за 30 в красном белье на атласных простынях, потом оживи его». | Qwen Image 2.1 → Wan 2.2 Spicy или Seedance, две сметы |
| «Перерендери это в 720p на Seedance 2.0 Spicy, последний кадр — из `end.jpg`». | Seedance 2.0 Spicy с `last_image_url` |
| «Аниме-кадр со взрослой королевой демонов, а потом заставь её двигаться». | Prefect Pony XL → Vidu Q3 Spicy |
| «Замени одежду на `me.png` на чёрное атласное платье-комбинацию». | Qwen Image 2.1 Edit (только вы, взрослый человек с его согласия или вымышленный персонаж) |
| «Напиши три NSFW-промпта для видео по этому кадру и оцени стоимость каждого». | Рецепт промпта + сметы; ничего не запускается, пока вы не выберете |
| «Продли мой последний ролик на 5 секунд с той же LoRA». | Wan 2.2 Spicy LoRA `video-extend` |
| «Четыре варианта с разными сидами в 480p, потом лучший — в 720p». | Пакетный запуск с подтверждением общей суммы |

Больше идей — в [examples/prompts.md](examples/prompts.md). Более 100 готовых промптов — в **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.ru.md)**.

---

## Поддерживаемые модели и цены

Скилл может вызвать **любую** модель из каталога SpicyAPI. Здесь перечислены те, что важны для контента 18+, в порядке каталога (сначала самые популярные, сначала новые версии), со Spicy Index и Freedom Score из публичных [лидербордов SpicyAPI](https://spicyapi.ai/ru/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ru) (✅ Freedom 90+ · ◐ 70–89 · ⚠️ ниже 70 · 🧪 меньше 15 тестовых прогонов). 🌶️ **Spicy**-версии настроены на контент для взрослых; у перечисленных здесь **стандартных** моделей в каталоге уровень `unrestricted`, поэтому они тоже принимают промпты 18+ и дополнительно умеют генерацию видео из текста и по референсам. Указан самый дешёвый тариф; перед запуском скилл всегда показывает точную смету. Каталог прочитан: <!-- catalog:date -->
2026-09-27
<!-- /catalog:date -->

**Видео**

<!-- catalog:video -->
| Модель | Тип | Задачи | Длительность | От | Spicy Index | Freedom |
|---|---|---|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/ru/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–30 s | $0.216/s | 56.5 | ✅ 96.7 |
| [Seedance 2.5](https://spicyapi.ai/ru/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 4–30 s | $0.1234/s | 69.5 | ◐ 80.9 |
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–15 s | $0.114/s | 61.5 | ✅ 93.3 |
| [Seedance 2.0](https://spicyapi.ai/ru/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 4–15 s | $0.07/s | 81.5 | ◐ 70.4 |
| [Wan 3.0 Prime](https://spicyapi.ai/ru/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 2–30 s | $0.0612/s | 76.5 | ◐ 78 |
| [Wan 3.0](https://spicyapi.ai/ru/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 2–30 s | $0.045/s | 76.5 | ✅ 96 |
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 3–15 s | $0.038/s | 29.5 | ✅ 97.5 |
| [MiniMax H3](https://spicyapi.ai/ru/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 4–15 s | $0.025/s | 72.5 | 🧪 33.3 |
| [MiniMax H3 Singularity LoRA](https://spicyapi.ai/ru/models/minimax-h3-singularity-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V | 3–15 s | $0.06/s | 72.8 | ✅ 100 |
| [LTX 2.5](https://spicyapi.ai/ru/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, T2V | 5–20 s | $0.09/s | 66 | ◐ 80.3 |
| [Wan 3.0 Pro Prime](https://spicyapi.ai/ru/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 2–30 s | $0.234/s | 76.5 | ◐ 82 |
| [Wan 3.0 Pro](https://spicyapi.ai/ru/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 2–30 s | $0.144/s | 76.5 | ◐ 82 |
| [MiniMax H3 LoRA](https://spicyapi.ai/ru/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 3–15 s | $0.05/s | 75.2 | ✅ 98.3 |
| [HappyHorse 1.1](https://spicyapi.ai/ru/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 3–15 s | $0.14/s | 62.5 | ⚠️ 65.1 |
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–15 s | $0.0387/s | 44.5 | ✅ 93.3 |
| [Seedance 2.0 Mini](https://spicyapi.ai/ru/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 4–15 s | $0.01097/s | 64.5 | ⚠️ 64.9 |
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 2–15 s | $0.1235/s | 46.5 | ✅ 100 |
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 3–20 s | $0.019/s | 33.5 | ◐ 89.2 |
| [LTX 2.3 Spicy LoRA](https://spicyapi.ai/ru/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 3–20 s | $0.0285/s | 34.8 | ◐ 83.8 |
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–15 s | $0.081/s | 44.5 | ✅ 90 |
| [Seedance 2.0 Fast](https://spicyapi.ai/ru/models/seedance-2-0-fast?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 4–15 s | $0.02254/s | 64.5 | ⚠️ 68.2 |
| [Vidu Q3 Turbo](https://spicyapi.ai/ru/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V | 1–16 s | $0.042/s | 39.5 | ✅ 93.3 |
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 1–16 s | $0.0665/s | 46.5 | ✅ 96.7 |
| [Vidu Q3](https://spicyapi.ai/ru/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V | 1–16 s | $0.07/s | 46.5 | ✅ 93.3 |
| [Vidu Q3 Pro](https://spicyapi.ai/ru/models/vidu-q3-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V | 1–16 s | $0.054/s | 36.5 | ✅ 93.3 |
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/ru/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–12 s | $0.012/s | 48.5 | ✅ 96.7 |
| [Seedance 1.5 Pro](https://spicyapi.ai/ru/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, T2V | 4–12 s | $0.0112/s | 46 | ✅ 90 |
| [Wan 2.6 Flash](https://spicyapi.ai/ru/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V | 5, 10, 15 s | $0.0225/s | 31.5 | ✅ 100 |
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 5, 10, 15 s | $0.095/s | 46.5 | ✅ 96.7 |
| [Wan 2.6](https://spicyapi.ai/ru/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, Ref2V, T2V | 5, 10, 15 s | $0.065/s | 58.5 | 🧪 8.7 |
| [Wan 2.5](https://spicyapi.ai/ru/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V, T2V | 5, 10 s | $0.045/s | 46 | ✅ 99 |
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 5, 8 s | $0.019/s | 23.5 | ✅ 91.2 |
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | I2V, Extend | 5, 8 s | $0.024/s | 25 | ◐ 74.8 |
| [Wan 2.2 LoRA](https://spicyapi.ai/ru/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | I2V | 5, 8 s | $0.024/s | 22.5 | ◐ 88.8 |
<!-- /catalog:video -->

**Изображения** (рекомендуем [Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ru), от $0.024)

<!-- catalog:image -->
| Модель | Тип | Задачи | От | Spicy Index | Freedom |
|---|---|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.024/image | 73 | ✅ 96.3 |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.03/image | 80.5 | ✅ 92 |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/ru/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.042/image | 74.5 | ✅ 100 |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/ru/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.04/image | 56 | ✅ 98 |
| [Qwen Image 3.0](https://spicyapi.ai/ru/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.03/image | 56 | ✅ 96 |
| [Seedream 5.0 Pro](https://spicyapi.ai/ru/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.036/image | 73 | ✅ 94.3 |
| [Qwen Image Edit Spicy](https://spicyapi.ai/ru/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | Edit | $0.038/image | 14 | ✅ 96 |
| [Seedream 5.0 Lite](https://spicyapi.ai/ru/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.0345/image | 73 | ✅ 96 |
| [Qwen Image 2](https://spicyapi.ai/ru/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.035/image | 34 | ✅ 96.7 |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/ru/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.03/image | 50.5 | ✅ 92.5 |
| [Z-Image Spicy Pro](https://spicyapi.ai/ru/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | T2I | $0.019/image | 38 | ✅ 100 |
| [Z-Image Spicy](https://spicyapi.ai/ru/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | 🌶️ Spicy | T2I | $0.01235/image | 32 | ✅ 98.8 |
| [Z-Image](https://spicyapi.ai/ru/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | T2I | $0.01/image | 17 | ✅ 100 |
| [Z-Image Turbo LoRA](https://spicyapi.ai/ru/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.012/image | 46.5 | ✅ 95 |
| [Seedream 4.0](https://spicyapi.ai/ru/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | Edit, T2I | $0.03/image | 74 | ◐ 74.7 |
| [Prefect Pony XL](https://spicyapi.ai/ru/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | T2I | $0.015/image | 30 | 🧪 36 |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/ru/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-ru) | Стандарт | T2I | $0.018/image | 32.5 | ◐ 75 |
<!-- /catalog:image -->

**Текст** (OpenAI-совместимая команда `chat`): [Grok 4.7](https://spicyapi.ai/ru/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ru), [DeepSeek V4.1 Flash](https://spicyapi.ai/ru/models/deepseek-v4-1-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-ru) и другие модели с уровнем каталога `unrestricted`, от $0.0012 за 1K токенов.

Полный справочник по полям: [skills/nsfw-ai/references/models.md](skills/nsfw-ai/references/models.md).

---

## Как это работает

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

По шагам: агент загружает SKILL.md и ① проверяет запрос на соответствие правилам «только для взрослых» и согласия, ② выбирает модель (или выводит список актуальных), ③ читает актуальную схему входных данных, ④ пишет промпт, ⑤ выставляет смету и просит подтверждения, ⑥ запускает генерацию после вашего OK.

- Локальные изображения загружаются через подписанную загрузку SpicyAPI и передаются как URI `spicy://`; публичные HTTPS-ссылки передаются как есть.
- У каждой задачи есть ключ идемпотентности (Idempotency-Key), поэтому повторный запрос никогда не приведёт к двойному списанию.
- Смета привязана к задаче (`quoteId` + `expectedCost`), поэтому итоговое списание никогда не превысит одобренную вами сумму.

---

## Использование без агента

Тот же скрипт — обычный CLI:

```bash
S=skills/nsfw-ai/scripts/spicy.py

python3 $S models --spicy --modality video          # ключ не нужен
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

Тесты запускаются командой `python3 -m unittest discover tests`. Примеры пайплайнов: [examples/image-to-video-pipeline.sh](examples/image-to-video-pipeline.sh), [examples/batch-variations.sh](examples/batch-variations.sh).

Предпочитаете SDK? У SpicyAPI есть официальные: `npm install @spicyapi/sdk`, `pip install spicyapi`, `go get github.com/Spicy-API/spicy-go`, `composer require spicyapi/spicyapi`, а также `@spicyapi/cli`. Подробнее — в [документации для разработчиков](https://docs.spicyapi.ai/docs?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=sdk).

---

## Структура репозитория

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

- `SKILL.md`: инструкции, которые загружает агент
- `scripts/spicy.py`: CLI для SpicyAPI без зависимостей
- `references/models.md`: ID моделей, поля, ценовые тарифы
- `references/prompting.md`: рецепт промпта, негативные промпты, пары, аниме
- `agents/openai.yaml`: метаданные для агентов Codex / OpenAI
- `.claude-plugin/`: манифесты плагина Claude Code и маркетплейса
- `examples/`: пайплайны и примеры запросов
- `tests/`: офлайн-юнит-тесты

---

## Частые вопросы

### Может ли Claude Code генерировать NSFW-изображения или видео?
Сам Claude Code медиа не генерирует. С этим скиллом Claude Code (а также Cursor, Codex, Windsurf, Gemini CLI, OpenClaw) вызывает Spicy-модели SpicyAPI, которые разрешают контент для взрослых, и сохраняет файлы локально. У скилла есть жёсткие ограничения: только взрослые, никаких реальных людей без их согласия.

### Какой NSFW API для генерации видео из изображения самый дешёвый?
В каталоге SpicyAPI (2026-09-27) самые дешёвые модели, прошедшие откровенные тесты, — Seedance 1.5 Pro Spicy (от $0.012/s в 480p, Freedom 96.7) и Wan 2.6 Flash ($0.0225/s в 720p, Freedom 100). Лучший результат за свои деньги даёт Wan 3.0: $0.45 за 5-секундный ролик в 720p при Freedom 96.

### Есть ли бесплатный NSFW AI скилл?
Сам скилл бесплатный и с открытым исходным кодом (MIT). Генерация на SpicyAPI оплачивается за каждый результат, потому что GPU стоят денег; подписки нет, а за неудавшиеся задачи деньги возвращаются. Для бесплатной генерации запускайте open-weight модели локально (см. [awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.ru.md#модели-для-самостоятельного-запуска-и-открытые-веса)).

### Можно ли вызывать модели, которые не «Spicy»?
Да. Для запросов 18+ по умолчанию используются Spicy-версии, но `spicy.py` принимает любой ID модели из каталога SpicyAPI: стандартные видеомодели Seedance / Wan / MiniMax, модели изображений Seedream / Qwen / Wan, апскейлеры, инструменты для лиц и липсинка, а также текстовые модели через `chat`. Выполните `spicy.py models` (без `--spicy`), чтобы увидеть список.

### Работает ли это с MCP?
Да. Используйте скилл отдельно или вместе с официальным MCP-сервером SpicyAPI (`@spicyapi/mcp`).

### Куда сохраняются файлы и что хранит SpicyAPI?
Результаты скачиваются в `./spicy-output/`. Ссылки на результаты истекают примерно через 20 минут. SpicyAPI хранит промпты, загрузки и результаты с отдельными сроками хранения, которые можно сократить, а содержимое завершённой задачи можно удалить; подробнее — на странице [Trust](https://spicyapi.ai/ru/trust?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=faq-ru).

### Какую модель выбрать для аниме и контента в стиле хентай?
Для кадра — Qwen Image 2.1 LoRA с аниме-LoRA (дизайн взрослого персонажа; №1 в лидерборде изображений, Freedom 92), затем для движения — Vidu Q3 Spicy (Freedom 96.7) или Wan 2.2 Spicy LoRA с той же LoRA. Prefect Pony XL работает с промптами из тегов, но тестовых данных по нему пока мало.

### Почему моя задача завершилась ошибкой?
Провайдер модели всё ещё может отклонять некоторые входные данные; тогда задача помечается как неудавшаяся, а списание возвращается. Измените формулировку или попробуйте другую Spicy-модель. Ошибка `40004` означает, что выбранная комбинация параметров недоступна; измените указанное в ошибке поле.

---

## Правила

Только для взрослых. Никакого сексуального контента с участием лиц младше 18 лет или выглядящих младше 18 лет — в любом стиле. Никакого сексуального контента с реальными людьми без документально подтверждённого согласия, никакой замены лиц в сексуальном контенте, никакого «раздевания» реальных фотографий. Соблюдайте законы страны, где находитесь вы и ваша аудитория. [Политика в отношении контента](https://spicyapi.ai/ru/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-ru) и [Правила допустимого использования](https://spicyapi.ai/ru/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-ru) SpicyAPI распространяются на каждый запрос.

## Связанные репозитории

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.ru.md)**: подборка инструментов, API и моделей ИИ без цензуры для изображений, видео и текста.
- **[nsfw-ai-image-prompts](https://github.com/Spicy-API/nsfw-ai-image-prompts/blob/main/README.ru.md)**: 104 NSFW-промпта для изображений и редактирования с реальными примерами результатов.
- **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.ru.md)**: более 100 NSFW-промптов для видео, промпты для первого кадра и проверенные примеры.
- **[spicy-skill](https://github.com/Spicy-API/spicy-skill)**: официальный универсальный скилл SpicyAPI.

## Лицензия

[MIT](LICENSE)

<p align="center">
  <a href="https://aiagentsdirectory.com" target="_blank" rel="noopener" title="Discover AI Agents Directory"><img src="https://aiagentsdirectory.com/featured-badge.svg?v=2024" alt="Featured on AI Agents Directory" width="200" height="50" /></a>
</p>

<p align="center"><sub>⭐ Поставьте звезду репозиторию, если он сэкономил вам полдня на чтение документации API.</sub></p>
