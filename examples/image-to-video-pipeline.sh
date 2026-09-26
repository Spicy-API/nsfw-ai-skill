#!/usr/bin/env bash
# Text → first frame → NSFW image-to-video, with a price cap on every step.
# Usage: SPICY_API_KEY=sk-spicy-... ./image-to-video-pipeline.sh
set -euo pipefail
SPICY="python3 $(dirname "$0")/../skills/nsfw-ai/scripts/spicy.py"
OUT=./spicy-output

# 1) First frame with Z-Image Spicy (~$0.012)
FRAME_JSON=$($SPICY generate alibaba/z-image-spicy/text-to-image \
  --prompt "Photorealistic boudoir portrait of a woman in her early 30s in an ivory silk robe by a candlelit vanity, warm amber light, soft bokeh" \
  --set width=832 --set height=1216 --max-cost 0.02 --out "$OUT")
FRAME=$(echo "$FRAME_JSON" | python3 -c 'import json,sys; print(json.load(sys.stdin)["saved"][0])')
echo "first frame: $FRAME"

# 2) Draft motion with Wan 2.2 Spicy at 480p (~$0.095); the local file is uploaded automatically
$SPICY generate alibaba/wan-2.2-spicy/image-to-video \
  --image "$FRAME" \
  --prompt "The silk robe slowly slides off her shoulder as she turns toward the camera and smiles, candlelight flickers, slow push-in" \
  --set duration_seconds=5 --set resolution=480p --max-cost 0.12 --out "$OUT"
