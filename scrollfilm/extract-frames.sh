#!/usr/bin/env bash
# Zerlegt die Higgsfield-Clips in WebP-Einzelbilder für den Scroll-Film-Player.
#   ./extract-frames.sh clipA.mp4 clipB.mp4
# Ergebnis: frames/desktop (1600 px breit, 16:9), frames/mobile (900x1600, mittiger 9:16-Ausschnitt)
# und frames/manifest.json. 24 Bilder pro Sekunde, also ca. 480 Bilder für 2 x 10 s.
set -euo pipefail
cd "$(dirname "$0")"
[ $# -ge 1 ] || { echo "Aufruf: $0 clipA.mp4 [clipB.mp4 ...]"; exit 1; }

FPS="${FPS:-24}"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT

# Clips aneinanderhängen. Clip B beginnt mit dem Schlussbild von Clip A, daher wird dessen erstes Bild verworfen.
i=0; inputs=(); filter=""
for f in "$@"; do
  inputs+=(-i "$f")
  if [ $i -eq 0 ]; then filter+="[$i:v]fps=$FPS,setpts=PTS-STARTPTS[v$i];"
  else filter+="[$i:v]fps=$FPS,trim=start_frame=1,setpts=PTS-STARTPTS[v$i];"; fi
  i=$((i+1))
done
for ((k=0;k<i;k++)); do filter+="[v$k]"; done
filter+="concat=n=$i:v=1:a=0[out]"
ffmpeg -loglevel error -y "${inputs[@]}" -filter_complex "$filter" -map "[out]" -c:v libx264 -crf 12 -pix_fmt yuv420p "$tmp/film.mp4"

rm -rf frames && mkdir -p frames/desktop frames/mobile
ffmpeg -loglevel error -i "$tmp/film.mp4" -vf "scale=1600:-2:flags=lanczos" -c:v libwebp -quality 78 frames/desktop/f_%04d.webp
ffmpeg -loglevel error -i "$tmp/film.mp4" -vf "crop=ih*9/16:ih,scale=900:1600:flags=lanczos" -c:v libwebp -quality 74 frames/mobile/f_%04d.webp

count=$(ls frames/desktop | wc -l | tr -d ' ')
printf '{ "count": %s, "pad": 4, "desktop": "frames/desktop/f_{n}.webp", "mobile": "frames/mobile/f_{n}.webp" }\n' "$count" > frames/manifest.json
echo "Fertig: $count Bilder, $(du -sh frames | cut -f1) insgesamt."
