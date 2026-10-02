<!--
  Palabras clave: skill nsfw, skill de ia nsfw para agentes, claude code nsfw, skill de ia sin censura, mcp nsfw,
  api de ia nsfw, api de imagen a video nsfw, api de generador de imágenes ia sin censura, api de generador de videos ia sin censura,
  api wan 2.2 spicy, api seedance spicy, api de editor de imágenes ia nsfw, ia para adultos, cursor nsfw, skill para codex,
  skill para openclaw, spicyapi, nsfw ai skill, nsfw agent skill, uncensored ai skill, nsfw ai api, nsfw image to video api
-->

<p align="center"><a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fr.md">Français</a> · <b>Español</b> · <a href="README.ru.md">Русский</a></p>

<h1 align="center">NSFW AI Skill</h1>

<p align="center">
  <b>Una skill para agentes que permite a Claude Code, Cursor, Codex, Windsurf, Gemini CLI y OpenClaw generar imágenes para adultos (18+), clips NSFW de imagen a video, ediciones de imagen sin censura y texto sin censura, con una sola API de pago por uso.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skill-agentskills-8b5cf6" alt="Skill para agentes">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Plugin de Claude Code">
  <img src="https://img.shields.io/badge/python-3.9%2B%2C%20no%20deps-3776ab" alt="Python 3.9+, sin dependencias">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#instalación">Instalación</a> ·
  <a href="#qué-puedes-pedirle">Qué puedes pedirle</a> ·
  <a href="#modelos-compatibles-y-precios">Modelos y precios</a> ·
  <a href="#cómo-funciona">Cómo funciona</a> ·
  <a href="#uso-sin-agente">CLI</a> ·
  <a href="#preguntas-frecuentes">Preguntas frecuentes</a>
</p>

<p align="center">
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4"><img src="assets/one-pace-closer.gif" width="30%" alt="Ejemplo de imagen a video con Wan 2.2 Spicy"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4"><img src="assets/velvet-spiral-turn.gif" width="30%" alt="Ejemplo de imagen a video con Seedance 2.0 Spicy"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4"><img src="assets/silk-draught-pull.gif" width="30%" alt="Ejemplo de imagen a video con Wan 2.7 Spicy"></a>
  <br><sub>Resultados reales de los modelos que usa esta skill (Wan 2.2 Spicy, Seedance 2.0 Spicy, Wan 2.7 Spicy). Haz clic para ver el clip completo.</sub>
</p>

> **Solo para mayores de 18 años.** La skill rechaza el contenido sexual que involucre a menores o a cualquier persona que parezca menor, el contenido sexual de personas reales sin su consentimiento documentado (incluidos los cambios de cara y las fotos "desvestidas") y la suplantación de identidad. Escribe cada prompt con una edad adulta explícita.

---

## Por qué esta skill

- **Habla, no configures.** "Anima esta foto en un clip boudoir de 5 segundos, con un acercamiento lento" → el agente elige el modelo, lee su esquema en vivo, escribe el prompt, te muestra el precio y guarda el MP4.
- **Recomendaciones respaldadas por pruebas.** La skill sigue la clasificación publicada por SpicyAPI: usa por defecto los modelos que generaron los prompts de prueba explícitos tal como se pidió (Wan 3.0, Seedance 2.5 Spicy, MiniMax H3 LoRA, Qwen Image 2.1…) y evita los que los suavizan.
- **Modelos Spicy que de verdad permiten contenido adulto.** Usa las ediciones Spicy de [SpicyAPI](https://spicyapi.ai/es?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=why-es) (Wan 2.2 Spicy, Seedance 2.x Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy, Z-Image Spicy, Qwen Image Edit Spicy). SpicyAPI no añade ningún filtro propio encima del modelo.
- **Ves el precio antes de que se ejecute nada.** Cada generación se cotiza primero; el agente solo continúa cuando la apruebas (o dentro del presupuesto que fijes). Las tareas fallidas se reembolsan automáticamente.
- **Barato.** Video NSFW desde **$0.012–$0.019 por segundo**, imágenes sin censura desde **$0.024** con Qwen Image 2.1 (o $0.01235 con Z-Image Spicy). Saldo en USD, sin suscripción, con tarjeta o cripto.
- **Todos los modelos del catálogo, no solo los Spicy.** Los mismos comandos ejecutan Seedance 2.5, Wan 3.0, Seedream 5.0, Qwen Image, escaladores, sincronización labial y los modelos de chat; pasa cualquier ID de modelo que aparezca en `spicy.py models`.
- **Cero dependencias.** Un único archivo de Python que solo usa la biblioteca estándar. Funciona en cualquier sitio donde haya Python 3.9+.
- **Privada por diseño.** Tu clave de API se queda en una variable de entorno. Los prompts, los archivos subidos y los resultados tienen plazos de retención que puedes acortar en SpicyAPI.

---

## Instalación

### 1. Consigue una clave de API

Regístrate en [spicyapi.ai](https://spicyapi.ai/es/register?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-es), recarga saldo (tarjeta, Apple Pay / Google Pay o cripto) y crea una clave en la [Consola](https://spicyapi.ai/es/console?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-es). Si quieres, ponle un límite de gasto a la clave.

```bash
export SPICY_API_KEY="sk-spicy-..."
```

### 2. Añade la skill a tu agente

**Cualquier agente (CLI de skills: Claude Code, Cursor, Codex, Windsurf, Gemini CLI, OpenClaw y más)**

```bash
npx skills add Spicy-API/nsfw-ai-skill
```

**Marketplace de plugins de Claude Code**

```text
/plugin marketplace add Spicy-API/nsfw-ai-skill
/plugin install nsfw-ai@spicyapi-nsfw
```

**Manual**

```bash
git clone https://github.com/Spicy-API/nsfw-ai-skill.git
cp -r nsfw-ai-skill/skills/nsfw-ai ~/.claude/skills/        # Claude Code
# o bien: cp -r nsfw-ai-skill/skills/nsfw-ai ~/.codex/skills/   # Codex
# o bien: apunta el directorio de skills de tu agente a skills/nsfw-ai
```

### 3. (Opcional) Añade el servidor MCP oficial de SpicyAPI

La skill funciona por sí sola. Si tu cliente es compatible con MCP, también puedes añadir el servidor MCP de SpicyAPI para listar modelos, obtener cotizaciones y gestionar tareas:

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

## Qué puedes pedirle

| Tú dices | La skill hace |
|---|---|
| "Muéstrame los modelos de video Spicy y cuánto cuestan." | Lee el catálogo en vivo (no hace falta clave) |
| "Anima `./frame.jpg` en un clip de 5 segundos: se gira hacia la cámara, luz de velas, acercamiento lento. La opción más barata." | Sube la imagen, usa Wan 2.2 Spicy a 480p, cotiza ~$0.095, espera tu confirmación y guarda el MP4 |
| "Primer fotograma fotorrealista: una mujer de unos 30 años en lencería roja sobre sábanas de satén; luego anímalo." | Qwen Image 2.1 → Wan 2.2 Spicy o Seedance, dos cotizaciones |
| "Vuelve a renderizarlo a 720p con Seedance 2.0 Spicy, usando `end.jpg` como último fotograma." | Seedance 2.0 Spicy con `last_image_url` |
| "Una imagen anime de una reina demonio adulta y luego haz que se mueva." | Prefect Pony XL → Vidu Q3 Spicy |
| "Cambia la ropa de `me.png` por un vestido lencero de satén negro." | Qwen Image 2.1 Edit (solo contigo, con un adulto que dé su consentimiento o con un personaje ficticio) |
| "Escribe tres prompts de video NSFW para este fotograma y estima el costo de cada uno." | Receta de prompt + cotizaciones; no se ejecuta nada hasta que elijas |
| "Alarga mi último clip 5 segundos con el mismo LoRA." | Wan 2.2 Spicy LoRA `video-extend` |
| "Cuatro variaciones de semilla a 480p y luego la mejor a 720p." | Lote con confirmación del precio total |

Más ideas en [examples/prompts.md](examples/prompts.md). Más de 100 prompts listos en **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.es.md)**.

---

## Modelos compatibles y precios

La skill puede llamar a **cualquier** modelo del catálogo de SpicyAPI. Estos son los que importan para contenido adulto, en el orden del catálogo (primero los más populares y la versión más reciente), con el Spicy Index y el Freedom Score de las [clasificaciones públicas de SpicyAPI](https://spicyapi.ai/es/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-es) (✅ Freedom 90+ · ◐ 70–89 · ⚠️ menos de 70 · 🧪 menos de 15 pruebas). Las ediciones 🌶️ **Spicy** están ajustadas para contenido adulto; los modelos **estándar** de esta lista tienen el nivel `unrestricted` en el catálogo, así que también aceptan prompts para adultos y añaden texto a video y referencia a video. Se muestra el nivel más barato; la skill siempre enseña la cotización exacta antes de ejecutar. Catálogo consultado el <!-- catalog:date -->
2026-09-27
<!-- /catalog:date -->

**Video**

<!-- catalog:video -->
| Modelo | Tipo | Tareas | Duración | Desde | Spicy Index | Freedom |
|---|---|---|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/es/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–30 s | $0.216/s | 56.5 | ✅ 96.7 |
| [Seedance 2.5](https://spicyapi.ai/es/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–30 s | $0.1234/s | 69.5 | ◐ 80.9 |
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–15 s | $0.114/s | 61.5 | ✅ 93.3 |
| [Seedance 2.0](https://spicyapi.ai/es/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–15 s | $0.07/s | 81.5 | ◐ 70.4 |
| [Wan 3.0 Prime](https://spicyapi.ai/es/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 2–30 s | $0.0612/s | 76.5 | ◐ 78 |
| [Wan 3.0](https://spicyapi.ai/es/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 2–30 s | $0.045/s | 76.5 | ✅ 96 |
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 3–15 s | $0.038/s | 29.5 | ✅ 97.5 |
| [MiniMax H3](https://spicyapi.ai/es/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–15 s | $0.025/s | 72.5 | 🧪 33.3 |
| [MiniMax H3 Singularity LoRA](https://spicyapi.ai/es/models/minimax-h3-singularity-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V | 3–15 s | $0.06/s | 72.8 | ✅ 100 |
| [LTX 2.5](https://spicyapi.ai/es/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, T2V | 5–20 s | $0.09/s | 66 | ◐ 80.3 |
| [Wan 3.0 Pro Prime](https://spicyapi.ai/es/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 2–30 s | $0.234/s | 76.5 | ◐ 82 |
| [Wan 3.0 Pro](https://spicyapi.ai/es/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 2–30 s | $0.144/s | 76.5 | ◐ 82 |
| [MiniMax H3 LoRA](https://spicyapi.ai/es/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 3–15 s | $0.05/s | 75.2 | ✅ 98.3 |
| [HappyHorse 1.1](https://spicyapi.ai/es/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 3–15 s | $0.14/s | 62.5 | ⚠️ 65.1 |
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–15 s | $0.0387/s | 44.5 | ✅ 93.3 |
| [Seedance 2.0 Mini](https://spicyapi.ai/es/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–15 s | $0.01097/s | 64.5 | ⚠️ 64.9 |
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 2–15 s | $0.1235/s | 46.5 | ✅ 100 |
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 3–20 s | $0.019/s | 33.5 | ◐ 89.2 |
| [LTX 2.3 Spicy LoRA](https://spicyapi.ai/es/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 3–20 s | $0.0285/s | 34.8 | ◐ 83.8 |
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–15 s | $0.081/s | 44.5 | ✅ 90 |
| [Seedance 2.0 Fast](https://spicyapi.ai/es/models/seedance-2-0-fast?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–15 s | $0.02254/s | 64.5 | ⚠️ 68.2 |
| [Vidu Q3 Turbo](https://spicyapi.ai/es/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V | 1–16 s | $0.042/s | 39.5 | ✅ 93.3 |
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 1–16 s | $0.0665/s | 46.5 | ✅ 96.7 |
| [Vidu Q3](https://spicyapi.ai/es/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V | 1–16 s | $0.07/s | 46.5 | ✅ 93.3 |
| [Vidu Q3 Pro](https://spicyapi.ai/es/models/vidu-q3-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V | 1–16 s | $0.054/s | 36.5 | ✅ 93.3 |
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/es/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–12 s | $0.012/s | 48.5 | ✅ 96.7 |
| [Seedance 1.5 Pro](https://spicyapi.ai/es/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, T2V | 4–12 s | $0.0112/s | 46 | ✅ 90 |
| [Wan 2.6 Flash](https://spicyapi.ai/es/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V | 5, 10, 15 s | $0.0225/s | 31.5 | ✅ 100 |
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 5, 10, 15 s | $0.095/s | 46.5 | ✅ 96.7 |
| [Wan 2.6](https://spicyapi.ai/es/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 5, 10, 15 s | $0.065/s | 58.5 | 🧪 8.7 |
| [Wan 2.5](https://spicyapi.ai/es/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V, T2V | 5, 10 s | $0.045/s | 46 | ✅ 99 |
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V | 5, 8 s | $0.019/s | 23.5 | ✅ 91.2 |
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | I2V, Extend | 5, 8 s | $0.024/s | 25 | ◐ 74.8 |
| [Wan 2.2 LoRA](https://spicyapi.ai/es/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | I2V | 5, 8 s | $0.024/s | 22.5 | ◐ 88.8 |
<!-- /catalog:video -->

**Imágenes** (recomendado: [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-es), desde $0.024)

<!-- catalog:image -->
| Modelo | Tipo | Tareas | Desde | Spicy Index | Freedom |
|---|---|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.024/image | 73 | ✅ 96.3 |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/image | 80.5 | ✅ 92 |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/es/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.042/image | 74.5 | ✅ 100 |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.04/image | 56 | ✅ 98 |
| [Qwen Image 3.0](https://spicyapi.ai/es/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/image | 56 | ✅ 96 |
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.036/image | 73 | ✅ 94.3 |
| [Qwen Image Edit Spicy](https://spicyapi.ai/es/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | Edit | $0.038/image | 14 | ✅ 96 |
| [Seedream 5.0 Lite](https://spicyapi.ai/es/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.0345/image | 73 | ✅ 96 |
| [Qwen Image 2](https://spicyapi.ai/es/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.035/image | 34 | ✅ 96.7 |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/es/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/image | 50.5 | ✅ 92.5 |
| [Z-Image Spicy Pro](https://spicyapi.ai/es/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | T2I | $0.019/image | 38 | ✅ 100 |
| [Z-Image Spicy](https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | 🌶️ Spicy | T2I | $0.01235/image | 32 | ✅ 98.8 |
| [Z-Image](https://spicyapi.ai/es/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | T2I | $0.01/image | 17 | ✅ 100 |
| [Z-Image Turbo LoRA](https://spicyapi.ai/es/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.012/image | 46.5 | ✅ 95 |
| [Seedream 4.0](https://spicyapi.ai/es/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/image | 74 | ◐ 74.7 |
| [Prefect Pony XL](https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | T2I | $0.015/image | 30 | 🧪 36 |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/es/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-es) | Estándar | T2I | $0.018/image | 32.5 | ◐ 75 |
<!-- /catalog:image -->

**Texto** (comando `chat` compatible con OpenAI): [Grok 4.7](https://spicyapi.ai/es/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-es), [DeepSeek V4.1 Flash](https://spicyapi.ai/es/models/deepseek-v4-1-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-es) y otros modelos con nivel `unrestricted` en el catálogo, desde $0.0012 por 1K tokens.

Referencia completa campo por campo: [skills/nsfw-ai/references/models.md](skills/nsfw-ai/references/models.md).

---

## Cómo funciona

```
Tú ──► El agente lee SKILL.md
          │  1. comprueba la petición con las reglas de solo adultos / consentimiento
          │  2. elige un modelo (o lista los disponibles)  spicy.py models --spicy
          │  3. lee el esquema de entrada en vivo          spicy.py schema <model>
          │  4. escribe el prompt (references/prompting.md)
          │  5. cotiza y te pide aprobación                spicy.py generate ...  → needs_confirmation
          │  6. ejecuta cuando das el visto bueno          spicy.py generate ... --yes
          ▼
     SpicyAPI  /api/v1/jobs/quote → /jobs/createTask (Idempotency-Key) → /jobs/recordInfo
          ▼
     ./spicy-output/<taskId>_0.mp4
```

- Las imágenes locales se suben mediante el flujo de subida firmada de SpicyAPI y se pasan como URI `spicy://`; las URL HTTPS públicas se pasan tal cual.
- Cada tarea lleva una clave de idempotencia, así que reintentar una petición nunca genera un cobro duplicado.
- La cotización queda vinculada a la tarea (`quoteId` + `expectedCost`), de modo que el cargo final nunca puede superar el precio que aprobaste.

---

## Uso sin agente

El mismo script funciona como una CLI normal:

```bash
S=skills/nsfw-ai/scripts/spicy.py

python3 $S models --spicy --modality video          # no hace falta clave
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

Ejecuta las pruebas con `python3 -m unittest discover tests`. Flujos de ejemplo: [examples/image-to-video-pipeline.sh](examples/image-to-video-pipeline.sh), [examples/batch-variations.sh](examples/batch-variations.sh).

¿Prefieres un SDK? SpicyAPI publica SDK oficiales: `npm install @spicyapi/sdk`, `pip install spicyapi`, `go get github.com/Spicy-API/spicy-go`, `composer require spicyapi/spicyapi`, además de `@spicyapi/cli`. Consulta la [documentación para desarrolladores](https://docs.spicyapi.ai/docs?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=sdk).

---

## Estructura del repositorio

```
nsfw-ai-skill/
├── skills/nsfw-ai/
│   ├── SKILL.md                 # instrucciones que carga el agente
│   ├── scripts/spicy.py         # CLI de SpicyAPI sin dependencias
│   ├── references/models.md     # IDs de modelos, campos, niveles de precio
│   ├── references/prompting.md  # receta de prompts, negativos, parejas, anime
│   └── agents/openai.yaml       # metadatos para Codex / agentes de OpenAI
├── .claude-plugin/              # manifiestos del plugin y del marketplace de Claude Code
├── examples/                    # flujos y ejemplos de peticiones
└── tests/                       # pruebas unitarias sin conexión
```

---

## Preguntas frecuentes

### ¿Claude Code puede generar imágenes o videos NSFW?
Claude Code por sí solo no genera contenido multimedia. Con esta skill instalada, Claude Code (y Cursor, Codex, Windsurf, Gemini CLI y OpenClaw) llama a los modelos Spicy de SpicyAPI, que sí permiten contenido adulto, y guarda los archivos en local. La skill mantiene límites estrictos: solo adultos y nada de personas reales sin consentimiento.

### ¿Cuál es la API de imagen a video NSFW más barata?
En el catálogo de SpicyAPI (2026-09-27), los modelos más baratos que superan las pruebas explícitas son Seedance 1.5 Pro Spicy (desde $0.012/s a 480p, Freedom 96.7) y Wan 2.6 Flash ($0.0225/s a 720p, Freedom 100). Si buscas el mejor resultado por dólar, Wan 3.0 cuesta $0.45 por clip de 5 segundos a 720p, con Freedom 96.

### ¿Hay alguna skill de IA NSFW gratis?
La skill es gratuita y de código abierto (MIT). La generación se paga por resultado en SpicyAPI porque las GPU cuestan dinero; no hay suscripción y las tareas fallidas se reembolsan. Para generar gratis, ejecuta modelos de pesos abiertos en local (consulta [awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.es.md#modelos-autoalojados-y-de-pesos-abiertos)).

### ¿Puede llamar a modelos que no son "Spicy"?
Sí. Las ediciones Spicy son la opción por defecto para peticiones de contenido adulto, pero `spicy.py` acepta cualquier ID de modelo del catálogo de SpicyAPI: modelos de video estándar Seedance / Wan / MiniMax, modelos de imagen Seedream / Qwen / Wan, escaladores, herramientas de cara y sincronización labial, y modelos de texto mediante `chat`. Ejecuta `spicy.py models` (sin `--spicy`) para verlos todos.

### ¿Funciona con MCP?
Sí. Usa la skill sola o añade junto a ella el servidor MCP oficial de SpicyAPI (`@spicyapi/mcp`).

### ¿Dónde se guardan mis archivos y qué conserva SpicyAPI?
Los resultados se descargan en `./spicy-output/`. Los enlaces a los resultados caducan a los 20 minutos, aproximadamente. SpicyAPI guarda los prompts, los archivos subidos y los resultados con plazos de retención independientes que puedes acortar, y puedes destruir el contenido de una tarea terminada; consulta [Trust](https://spicyapi.ai/es/trust?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=faq-es).

### ¿Qué modelo uso para contenido estilo anime / hentai?
Qwen Image 2.1 LoRA con un LoRA de anime para la imagen (diseño de personaje adulto; #1 en la clasificación de imagen, Freedom 92) y después Vidu Q3 Spicy (Freedom 96.7) o Wan 2.2 Spicy LoRA con el mismo LoRA para el movimiento. Prefect Pony XL funciona con prompts por etiquetas, pero por ahora tiene pocos datos de prueba.

### ¿Por qué ha fallado mi tarea?
El proveedor del modelo puede seguir rechazando algunas entradas; eso aparece como una tarea fallida y el cobro se reembolsa. Cambia la redacción o prueba otro modelo Spicy. Un error `40004` significa que la combinación de parámetros elegida no está disponible; cambia el campo que se indica.

---

## Reglas

Solo adultos. Nada de contenido sexual que involucre a menores de 18 años o a quien parezca menor de 18, en ningún estilo. Nada de contenido sexual de personas reales sin su consentimiento documentado, nada de cambios de cara en contenido sexual, nada de fotos reales "desvestidas". Cumple la ley del lugar donde estés tú y donde esté tu público. La [Política de contenidos](https://spicyapi.ai/es/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-es) y la [Política de uso aceptable](https://spicyapi.ai/es/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-es) de SpicyAPI se aplican a todas las peticiones.

## Relacionados

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.es.md)**: lista seleccionada de herramientas, APIs y modelos de IA sin censura para imagen, video y texto.
- **[nsfw-ai-image-prompts](https://github.com/Spicy-API/nsfw-ai-image-prompts/blob/main/README.es.md)**: 104 prompts NSFW de imagen y de edición, con casos de resultados reales.
- **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.es.md)**: más de 100 prompts de video NSFW, prompts para el primer fotograma y ejemplos verificados.
- **[spicy-skill](https://github.com/Spicy-API/spicy-skill)**: la skill oficial de uso general de SpicyAPI.

## Licencia

[MIT](LICENSE)

<p align="center"><sub>⭐ Dale una estrella al repositorio si te ha ahorrado una tarde de documentación de APIs.</sub></p>
