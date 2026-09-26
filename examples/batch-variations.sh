#!/usr/bin/env bash
# Render N seed variations of one prompt at 480p, then pick the best and re-render at 720p.
# Usage: SPICY_API_KEY=sk-spicy-... ./batch-variations.sh first-frame.jpg 4
set -euo pipefail
SPICY="python3 $(dirname "$0")/../skills/nsfw-ai/scripts/spicy.py"
IMAGE=${1:?first frame path or URL}
N=${2:-4}
PROMPT="She walks slowly toward the camera down the hotel corridor, hips swaying, warm sconce light, low-angle tracking shot"

echo "About to create $N tasks at up to \$0.095 each (Wan 2.2 Spicy, 480p, 5 s)."
for seed in $(seq 1 "$N"); do
  $SPICY generate alibaba/wan-2.2-spicy/image-to-video --image "$IMAGE" --prompt "$PROMPT" \
    --set duration_seconds=5 --set resolution=480p --set seed="$seed" --max-cost 0.10 --out "./spicy-output/seed-$seed"
done
