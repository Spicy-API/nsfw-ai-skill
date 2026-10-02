<!--
  Mots-clés : skill IA NSFW, skill d'agent NSFW, Claude Code NSFW, skill IA sans censure, MCP NSFW, API IA NSFW,
  API image en vidéo NSFW, API générateur d'images IA sans censure, API générateur de vidéo IA sans censure,
  API Wan 2.2 Spicy, API Seedance Spicy, API éditeur d'images IA NSFW, IA pour adultes, Cursor NSFW, skill Codex,
  skill OpenClaw, spicyapi, nsfw ai skill, nsfw agent skill, claude code nsfw, uncensored ai skill, nsfw mcp, nsfw ai api
-->

<p align="center"><a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <b>Français</b> · <a href="README.es.md">Español</a> · <a href="README.ru.md">Русский</a></p>

<h1 align="center">NSFW AI Skill</h1>

<p align="center">
  <b>Une skill pour agents qui permet à Claude Code, Cursor, Codex, Windsurf, Gemini CLI et OpenClaw de générer des images pour adultes (18+), des clips NSFW en image en vidéo, des retouches d'images sans censure et du texte sans censure, via une seule API facturée à l'usage.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skill-agentskills-8b5cf6" alt="Skill pour agents">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Plugin Claude Code">
  <img src="https://img.shields.io/badge/python-3.9%2B%2C%20no%20deps-3776ab" alt="Python 3.9+, sans dépendances">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#installation">Installation</a> ·
  <a href="#ce-que-vous-pouvez-demander">Exemples de demandes</a> ·
  <a href="#modèles-pris-en-charge-et-prix">Modèles &amp; prix</a> ·
  <a href="#fonctionnement">Fonctionnement</a> ·
  <a href="#utilisation-sans-agent">CLI</a> ·
  <a href="#faq">FAQ</a>
</p>

<p align="center">
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4"><img src="assets/one-pace-closer.gif" width="30%" alt="Exemple d'image en vidéo avec Wan 2.2 Spicy"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4"><img src="assets/velvet-spiral-turn.gif" width="30%" alt="Exemple d'image en vidéo avec Seedance 2.0 Spicy"></a>
  <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4"><img src="assets/silk-draught-pull.gif" width="30%" alt="Exemple d'image en vidéo avec Wan 2.7 Spicy"></a>
  <br><sub>Résultats réels des modèles appelés par cette skill (Wan 2.2 Spicy, Seedance 2.0 Spicy, Wan 2.7 Spicy). Cliquez pour voir le clip complet.</sub>
</p>

> **Réservé aux plus de 18 ans.** La skill refuse le contenu sexuel impliquant des mineurs ou toute personne qui paraît mineure, le contenu sexuel de personnes réelles sans consentement documenté (y compris l'échange de visage et les photos « déshabillées »), ainsi que l'usurpation d'identité. Elle écrit chaque prompt avec un âge adulte explicite.

---

## Pourquoi cette skill

- **Parlez, sans rien configurer.** « Anime cette photo en un clip boudoir de 5 secondes, slow push-in » → l'agent choisit le modèle, lit son schéma en direct, écrit le prompt, vous montre le prix et enregistre le MP4.
- **Des choix appuyés par des tests.** La skill suit le classement publié par SpicyAPI : par défaut, elle utilise les modèles qui ont rendu les prompts de test explicites comme demandé (Wan 3.0, Seedance 2.5 Spicy, MiniMax H3 LoRA, Qwen Image 2.1…) et évite ceux qui les adoucissent.
- **Des modèles Spicy qui autorisent vraiment le contenu adulte.** La skill utilise les éditions Spicy de [SpicyAPI](https://spicyapi.ai/fr?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=why-fr) (Wan 2.2 Spicy, Seedance 2.x Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy, Z-Image Spicy, Qwen Image Edit Spicy). SpicyAPI n'ajoute aucun filtre de plateforme par-dessus le modèle.
- **Vous voyez le prix avant tout lancement.** Chaque génération fait d'abord l'objet d'un devis ; l'agent ne continue qu'après votre accord (ou dans la limite d'un budget que vous fixez). Les tâches échouées sont remboursées automatiquement.
- **Pas cher.** Vidéo NSFW à partir de **$0.012–$0.019 par seconde**, images sans censure à partir de **$0.024** avec Qwen Image 2.1 (ou $0.01235 avec Z-Image Spicy). Solde en USD, sans abonnement, par carte ou en crypto.
- **Tous les modèles du catalogue, pas seulement les Spicy.** Les mêmes commandes font tourner Seedance 2.5, Wan 3.0, Seedream 5.0, Qwen Image, les upscalers, la synchronisation labiale et les modèles de chat ; passez n'importe quel ID de modèle issu de `spicy.py models`.
- **Zéro dépendance.** Un seul fichier Python qui n'utilise que la bibliothèque standard. Fonctionne partout où tourne Python 3.9+.
- **Confidentiel par conception.** Votre clé API reste dans une variable d'environnement. Les prompts, les fichiers envoyés et les résultats ont des durées de conservation que vous pouvez raccourcir sur SpicyAPI.

---

## Installation

### 1. Obtenir une clé API

Inscrivez-vous sur [spicyapi.ai](https://spicyapi.ai/fr/register?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-fr), rechargez votre solde (carte, Apple Pay / Google Pay ou crypto), puis créez une clé dans la [Console](https://spicyapi.ai/fr/console?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=install-fr). Vous pouvez fixer un plafond de dépenses sur la clé.

```bash
export SPICY_API_KEY="sk-spicy-..."
```

### 2. Ajouter la skill à votre agent

**N'importe quel agent (CLI skills : Claude Code, Cursor, Codex, Windsurf, Gemini CLI, OpenClaw et d'autres)**

```bash
npx skills add Spicy-API/nsfw-ai-skill
```

**Marketplace de plugins Claude Code**

```text
/plugin marketplace add Spicy-API/nsfw-ai-skill
/plugin install nsfw-ai@spicyapi-nsfw
```

**Installation manuelle**

```bash
git clone https://github.com/Spicy-API/nsfw-ai-skill.git
cp -r nsfw-ai-skill/skills/nsfw-ai ~/.claude/skills/        # Claude Code
# ou : cp -r nsfw-ai-skill/skills/nsfw-ai ~/.codex/skills/  # Codex
# ou : faites pointer le dossier de skills de votre agent vers skills/nsfw-ai
```

### 3. (Facultatif) Ajouter le serveur MCP officiel de SpicyAPI

La skill fonctionne seule. Si votre client prend en charge MCP, vous pouvez aussi ajouter le serveur MCP de SpicyAPI pour lister les modèles, obtenir des devis et gérer les tâches :

```bash
claude mcp add spicyapi -e SPICY_API_KEY=$SPICY_API_KEY -- npx --yes --package=@spicyapi/mcp spicyapi-mcp
```

Cursor / Claude Desktop / Windsurf (`mcp.json`) :

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

## Ce que vous pouvez demander

| Vous dites | La skill fait |
|---|---|
| « Liste les modèles vidéo Spicy et leurs prix. » | Lit le catalogue en direct (pas besoin de clé) |
| « Anime `./frame.jpg` en un clip de 5 secondes : elle se tourne vers la caméra, lumière de bougie, slow push-in. L'option la moins chère. » | Envoie l'image, utilise Wan 2.2 Spicy en 480p, annonce environ $0.095, attend votre accord, enregistre le MP4 |
| « Une première image photoréaliste : une femme d'une trentaine d'années en lingerie rouge sur des draps de satin, puis anime-la. » | Qwen Image 2.1 → Wan 2.2 Spicy ou Seedance, deux devis |
| « Refais-le en 720p avec Seedance 2.0 Spicy, avec `end.jpg` comme dernière image. » | Seedance 2.0 Spicy avec `last_image_url` |
| « Une image anime d'une reine démon adulte, puis fais-la bouger. » | Prefect Pony XL → Vidu Q3 Spicy |
| « Remplace la tenue dans `me.png` par une nuisette en satin noir. » | Qwen Image 2.1 Edit (uniquement vous, un adulte consentant ou un personnage fictif) |
| « Écris trois prompts vidéo NSFW pour cette image et estime le coût de chacun. » | Recette de prompt + devis, rien ne tourne tant que vous n'avez pas choisi |
| « Prolonge mon dernier clip de 5 secondes avec le même LoRA. » | `video-extend` de Wan 2.2 Spicy LoRA |
| « Quatre variantes de seed en 480p, puis la meilleure en 720p. » | Lot avec confirmation du prix total |

D'autres idées dans [examples/prompts.md](examples/prompts.md). Plus de 100 prompts prêts à l'emploi dans **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.fr.md)**.

---

## Modèles pris en charge et prix

La skill peut appeler **n'importe quel** modèle du catalogue SpicyAPI. Voici ceux qui comptent pour le contenu adulte, dans l'ordre du catalogue (les plus populaires d'abord, la version la plus récente d'abord), avec le Spicy Index et le Freedom Score issus des [classements publics de SpicyAPI](https://spicyapi.ai/fr/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-fr) (✅ Freedom 90+ · ◐ 70–89 · ⚠️ moins de 70 · 🧪 moins de 15 tests). Les éditions 🌶️ **Spicy** sont réglées pour le contenu adulte ; les modèles **Standard** listés ici sont classés `unrestricted` dans le catalogue : ils acceptent donc aussi les prompts pour adultes et ajoutent le texte en vidéo et la vidéo à partir de références. Le prix affiché est celui du palier le moins cher ; la skill montre toujours le devis exact avant de lancer quoi que ce soit. Catalogue consulté le <!-- catalog:date -->
2026-09-27
<!-- /catalog:date -->

**Vidéo**

<!-- catalog:video -->
| Modèle | Type | Tâches | Durée | À partir de | Spicy Index | Freedom |
|---|---|---|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/fr/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 4–30 s | $0.216/s | 56.5 | ✅ 96.7 |
| [Seedance 2.5](https://spicyapi.ai/fr/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 4–30 s | $0.1234/s | 69.5 | ◐ 80.9 |
| [Seedance 2.0 Spicy](https://spicyapi.ai/fr/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 4–15 s | $0.114/s | 61.5 | ✅ 93.3 |
| [Seedance 2.0](https://spicyapi.ai/fr/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 4–15 s | $0.07/s | 81.5 | ◐ 70.4 |
| [Wan 3.0 Prime](https://spicyapi.ai/fr/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 2–30 s | $0.0612/s | 76.5 | ◐ 78 |
| [Wan 3.0](https://spicyapi.ai/fr/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 2–30 s | $0.045/s | 76.5 | ✅ 96 |
| [MiniMax H3 Spicy](https://spicyapi.ai/fr/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 3–15 s | $0.038/s | 29.5 | ✅ 97.5 |
| [MiniMax H3](https://spicyapi.ai/fr/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 4–15 s | $0.025/s | 72.5 | 🧪 33.3 |
| [MiniMax H3 Singularity LoRA](https://spicyapi.ai/fr/models/minimax-h3-singularity-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V | 3–15 s | $0.06/s | 72.8 | ✅ 100 |
| [LTX 2.5](https://spicyapi.ai/fr/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, T2V | 5–20 s | $0.09/s | 66 | ◐ 80.3 |
| [Wan 3.0 Pro Prime](https://spicyapi.ai/fr/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 2–30 s | $0.234/s | 76.5 | ◐ 82 |
| [Wan 3.0 Pro](https://spicyapi.ai/fr/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 2–30 s | $0.144/s | 76.5 | ◐ 82 |
| [MiniMax H3 LoRA](https://spicyapi.ai/fr/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 3–15 s | $0.05/s | 75.2 | ✅ 98.3 |
| [HappyHorse 1.1](https://spicyapi.ai/fr/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 3–15 s | $0.14/s | 62.5 | ⚠️ 65.1 |
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/fr/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 4–15 s | $0.0387/s | 44.5 | ✅ 93.3 |
| [Seedance 2.0 Mini](https://spicyapi.ai/fr/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 4–15 s | $0.01097/s | 64.5 | ⚠️ 64.9 |
| [Wan 2.7 Spicy](https://spicyapi.ai/fr/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 2–15 s | $0.1235/s | 46.5 | ✅ 100 |
| [LTX 2.3 Spicy](https://spicyapi.ai/fr/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 3–20 s | $0.019/s | 33.5 | ◐ 89.2 |
| [LTX 2.3 Spicy LoRA](https://spicyapi.ai/fr/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 3–20 s | $0.0285/s | 34.8 | ◐ 83.8 |
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/fr/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 4–15 s | $0.081/s | 44.5 | ✅ 90 |
| [Seedance 2.0 Fast](https://spicyapi.ai/fr/models/seedance-2-0-fast?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 4–15 s | $0.02254/s | 64.5 | ⚠️ 68.2 |
| [Vidu Q3 Turbo](https://spicyapi.ai/fr/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V | 1–16 s | $0.042/s | 39.5 | ✅ 93.3 |
| [Vidu Q3 Spicy](https://spicyapi.ai/fr/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 1–16 s | $0.0665/s | 46.5 | ✅ 96.7 |
| [Vidu Q3](https://spicyapi.ai/fr/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V | 1–16 s | $0.07/s | 46.5 | ✅ 93.3 |
| [Vidu Q3 Pro](https://spicyapi.ai/fr/models/vidu-q3-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V | 1–16 s | $0.054/s | 36.5 | ✅ 93.3 |
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/fr/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 4–12 s | $0.012/s | 48.5 | ✅ 96.7 |
| [Seedance 1.5 Pro](https://spicyapi.ai/fr/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, T2V | 4–12 s | $0.0112/s | 46 | ✅ 90 |
| [Wan 2.6 Flash](https://spicyapi.ai/fr/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V | 5, 10, 15 s | $0.0225/s | 31.5 | ✅ 100 |
| [Wan 2.6 Spicy](https://spicyapi.ai/fr/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 5, 10, 15 s | $0.095/s | 46.5 | ✅ 96.7 |
| [Wan 2.6](https://spicyapi.ai/fr/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, Ref2V, T2V | 5, 10, 15 s | $0.065/s | 58.5 | 🧪 8.7 |
| [Wan 2.5](https://spicyapi.ai/fr/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V, T2V | 5, 10 s | $0.045/s | 46 | ✅ 99 |
| [Wan 2.2 Spicy](https://spicyapi.ai/fr/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V | 5, 8 s | $0.019/s | 23.5 | ✅ 91.2 |
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/fr/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | I2V, Extend | 5, 8 s | $0.024/s | 25 | ◐ 74.8 |
| [Wan 2.2 LoRA](https://spicyapi.ai/fr/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | I2V | 5, 8 s | $0.024/s | 22.5 | ◐ 88.8 |
<!-- /catalog:video -->

**Images** (recommandé : [Qwen Image 2.1](https://spicyapi.ai/fr/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-fr), à partir de $0.024)

<!-- catalog:image -->
| Modèle | Type | Tâches | À partir de | Spicy Index | Freedom |
|---|---|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/fr/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.024/image | 73 | ✅ 96.3 |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/fr/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.03/image | 80.5 | ✅ 92 |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/fr/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.042/image | 74.5 | ✅ 100 |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/fr/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.04/image | 56 | ✅ 98 |
| [Qwen Image 3.0](https://spicyapi.ai/fr/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.03/image | 56 | ✅ 96 |
| [Seedream 5.0 Pro](https://spicyapi.ai/fr/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.036/image | 73 | ✅ 94.3 |
| [Qwen Image Edit Spicy](https://spicyapi.ai/fr/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | Edit | $0.038/image | 14 | ✅ 96 |
| [Seedream 5.0 Lite](https://spicyapi.ai/fr/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.0345/image | 73 | ✅ 96 |
| [Qwen Image 2](https://spicyapi.ai/fr/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.035/image | 34 | ✅ 96.7 |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/fr/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.03/image | 50.5 | ✅ 92.5 |
| [Z-Image Spicy Pro](https://spicyapi.ai/fr/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | T2I | $0.019/image | 38 | ✅ 100 |
| [Z-Image Spicy](https://spicyapi.ai/fr/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | 🌶️ Spicy | T2I | $0.01235/image | 32 | ✅ 98.8 |
| [Z-Image](https://spicyapi.ai/fr/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | T2I | $0.01/image | 17 | ✅ 100 |
| [Z-Image Turbo LoRA](https://spicyapi.ai/fr/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.012/image | 46.5 | ✅ 95 |
| [Seedream 4.0](https://spicyapi.ai/fr/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | Edit, T2I | $0.03/image | 74 | ◐ 74.7 |
| [Prefect Pony XL](https://spicyapi.ai/fr/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | T2I | $0.015/image | 30 | 🧪 36 |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/fr/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=model-table-fr) | Standard | T2I | $0.018/image | 32.5 | ◐ 75 |
<!-- /catalog:image -->

**Texte** (commande `chat` compatible OpenAI) : [Grok 4.7](https://spicyapi.ai/fr/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-fr), [DeepSeek V4.1 Flash](https://spicyapi.ai/fr/models/deepseek-v4-1-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=models-fr) et d'autres modèles classés `unrestricted` dans le catalogue, à partir de $0.0012 pour 1K tokens.

Référence complète, champ par champ : [skills/nsfw-ai/references/models.md](skills/nsfw-ai/references/models.md).

---

## Fonctionnement

```
Vous ──► L'agent lit SKILL.md
          │  1. vérifie la demande au regard des règles (adultes uniquement, consentement)
          │  2. choisit un modèle (ou liste ceux en ligne)   spicy.py models --spicy
          │  3. lit le schéma d'entrée en direct             spicy.py schema <model>
          │  4. écrit le prompt (references/prompting.md)
          │  5. établit un devis et demande votre accord     spicy.py generate ...  → needs_confirmation
          │  6. lance après votre accord                     spicy.py generate ... --yes
          ▼
     SpicyAPI  /api/v1/jobs/quote → /jobs/createTask (Idempotency-Key) → /jobs/recordInfo
          ▼
     ./spicy-output/<taskId>_0.mp4
```

- Les images locales sont envoyées via le flux d'upload signé de SpicyAPI et transmises sous forme d'URI `spicy://` ; les URL HTTPS publiques sont transmises telles quelles.
- Chaque tâche porte une clé d'idempotence : une requête relancée ne crée jamais de double facturation.
- Le devis est lié à la tâche (`quoteId` + `expectedCost`) : le montant final facturé ne peut jamais dépasser le prix que vous avez approuvé.

---

## Utilisation sans agent

Le même script est une CLI classique :

```bash
S=skills/nsfw-ai/scripts/spicy.py

python3 $S models --spicy --modality video          # pas besoin de clé
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

Lancez les tests avec `python3 -m unittest discover tests`. Exemples de pipelines : [examples/image-to-video-pipeline.sh](examples/image-to-video-pipeline.sh), [examples/batch-variations.sh](examples/batch-variations.sh).

Vous préférez un SDK ? SpicyAPI en publie des officiels : `npm install @spicyapi/sdk`, `pip install spicyapi`, `go get github.com/Spicy-API/spicy-go`, `composer require spicyapi/spicyapi`, ainsi que `@spicyapi/cli`. Voir la [documentation développeur](https://docs.spicyapi.ai/docs?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=sdk).

---

## Structure du dépôt

```
nsfw-ai-skill/
├── skills/nsfw-ai/
│   ├── SKILL.md                 # instructions chargées par l'agent
│   ├── scripts/spicy.py         # CLI SpicyAPI sans dépendance
│   ├── references/models.md     # IDs de modèles, champs, paliers de prix
│   ├── references/prompting.md  # recette de prompt, négatifs, couples, anime
│   └── agents/openai.yaml       # métadonnées pour Codex / agents OpenAI
├── .claude-plugin/              # manifestes du plugin Claude Code et de la marketplace
├── examples/                    # pipelines et idées de demandes
└── tests/                       # tests unitaires hors ligne
```

---

## FAQ

### Claude Code peut-il générer des images ou des vidéos NSFW ?
Claude Code ne génère pas de médias lui-même. Avec cette skill installée, Claude Code (ainsi que Cursor, Codex, Windsurf, Gemini CLI, OpenClaw) appelle les modèles Spicy de SpicyAPI, qui autorisent le contenu adulte, et enregistre les fichiers en local. La skill garde des limites strictes : adultes uniquement, pas de personnes réelles sans consentement.

### Quelle est l'API image en vidéo NSFW la moins chère ?
Dans le catalogue SpicyAPI (2026-09-27), les modèles les moins chers qui réussissent les tests explicites sont Seedance 1.5 Pro Spicy (à partir de $0.012/s en 480p, Freedom 96.7) et Wan 2.6 Flash ($0.0225/s en 720p, Freedom 100). Pour le meilleur résultat par dollar, Wan 3.0 coûte $0.45 le clip de 5 secondes en 720p, avec un Freedom de 96.

### Existe-t-il une skill IA NSFW gratuite ?
La skill est gratuite et open source (MIT). La génération est facturée au résultat sur SpicyAPI parce que les GPU coûtent cher ; il n'y a pas d'abonnement et les tâches échouées sont remboursées. Pour générer gratuitement, faites tourner des modèles à poids ouverts en local (voir [awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.fr.md#modèles-auto-hébergés-et-à-poids-ouverts)).

### Peut-elle appeler des modèles qui ne sont pas « Spicy » ?
Oui. Les éditions Spicy sont utilisées par défaut pour les demandes pour adultes, mais `spicy.py` accepte n'importe quel ID de modèle du catalogue SpicyAPI : modèles vidéo standard Seedance / Wan / MiniMax, modèles d'image Seedream / Qwen / Wan, upscalers, outils de visage et de synchronisation labiale, et modèles de texte via `chat`. Lancez `spicy.py models` (sans `--spicy`) pour les lister.

### Fonctionne-t-elle avec MCP ?
Oui. Utilisez la skill seule, ou ajoutez à côté le serveur MCP officiel de SpicyAPI (`@spicyapi/mcp`).

### Où vont mes fichiers, et que conserve SpicyAPI ?
Les résultats sont téléchargés dans `./spicy-output/`. Les liens vers les résultats expirent au bout d'environ 20 minutes. SpicyAPI conserve les prompts, les fichiers envoyés et les résultats selon des durées distinctes que vous pouvez raccourcir, et vous pouvez détruire le contenu d'une tâche terminée ; voir [Trust](https://spicyapi.ai/fr/trust?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=faq-fr).

### Quel modèle utiliser pour du contenu style anime / hentai ?
Qwen Image 2.1 LoRA avec un LoRA anime pour l'image fixe (personnage conçu comme adulte ; n° 1 du classement image, Freedom 92), puis Vidu Q3 Spicy (Freedom 96.7) ou Wan 2.2 Spicy LoRA avec le même LoRA pour le mouvement. Prefect Pony XL fonctionne avec des prompts par tags, mais n'a encore que peu de données de test.

### Pourquoi ma tâche a-t-elle échoué ?
Le fournisseur du modèle peut encore refuser certaines entrées ; cela se traduit par une tâche échouée, et le montant est remboursé. Reformulez ou essayez un autre modèle Spicy. Une erreur `40004` signifie que la combinaison de paramètres choisie n'est pas proposée ; modifiez le champ indiqué.

---

## Règles

Adultes uniquement. Aucun contenu sexuel impliquant une personne de moins de 18 ans ou qui paraît avoir moins de 18 ans, quel que soit le style. Aucun contenu sexuel de personnes réelles sans consentement documenté, pas d'échange de visage dans un contenu sexuel, pas de « déshabillage » de photos réelles. Respectez la loi du pays où vous vivez et de celui de votre public. La [Politique de contenu](https://spicyapi.ai/fr/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-fr) et la [Politique d’utilisation acceptable](https://spicyapi.ai/fr/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-skill&utm_content=rules-fr) de SpicyAPI s'appliquent à chaque requête.

## Voir aussi

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.fr.md)** : sélection d'outils, d'API et de modèles IA sans censure pour l'image, la vidéo et le texte.
- **[nsfw-ai-image-prompts](https://github.com/Spicy-API/nsfw-ai-image-prompts/blob/main/README.fr.md)** : 104 prompts d'images NSFW et de retouche, avec des résultats réels.
- **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.fr.md)** : plus de 100 prompts vidéo NSFW, des prompts pour la première image et des exemples vérifiés.
- **[spicy-skill](https://github.com/Spicy-API/spicy-skill)** : la skill officielle et généraliste de SpicyAPI.

## Licence

[MIT](LICENSE)

<p align="center"><sub>⭐ Mettez une étoile au dépôt s'il vous a épargné un après-midi de documentation d'API.</sub></p>
