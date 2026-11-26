#!/bin/sh
# scan_at.sh bundesland1 bundesland2 ...  (RUBRIKEN default: immobilienmakler immobilienverwaltung architekten)
D=$(grep -oE "[a-z0-9-]+\.(de|at|com|eu|net|info)" ../README.md | tr A-Z a-z | sort -u)
R=${RUBRIKEN:-"immobilienmakler immobilienverwaltung architekten"}
for l in "$@"; do for r in $R; do python3 herold.py $l $r 3; done; done | awk -F'\t' '!seen[$2]++' \
 | grep -viE "remax|engel|von-poll|sreal|raiffeisen|bank|facebook" \
 | while IFS="$(printf '\t')" read n w a; do dom=$(echo $w | sed -E 's#https?://(www\.)?##;s#/.*##' | tr A-Z a-z); echo "$D" | grep -qx "$dom" && continue; echo "$w|$a|$n"; done \
 | head -150 | tr -d "'" | xargs -P 12 -I{} sh -c 'w=$(echo "{}" | cut -d"|" -f1); s=$(timeout 25 python3 check.py "$w" 2>/dev/null | head -1); echo "{} | $s"' \
 | grep SIGNALE | grep -E "${FILTER:-KEIN-viewport|X5|cm4all|KEIN-https|©20(0|1)}" | grep -vE " 0kB| [1-3]kB"
