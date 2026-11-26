#!/bin/sh
# scan.sh stadt1 stadt2 ...  -> schwache Websites (Makler + Hausverwaltung), ohne bekannte Domains
D=$(grep -oE "[a-z0-9-]+\.(de|at|com|eu|net|info)" ../README.md | tr A-Z a-z | sort -u)
R=${RUBRIKEN:-"immobilienmakler hausverwaltungen"}
for c in "$@"; do for r in $R; do python3 gs.py $r $c; done; done | awk -F'\t' '!seen[$2]++' \
 | grep -viE "von-poll|engel|remax|postbank|sparkasse|volksbank|deutsche-bank|dkb|lbs|aengevelt|vr-|immowelt|commerz|hypo|facebook" \
 | while IFS="$(printf '\t')" read n w a; do dom=$(echo $w | sed -E 's#https?://(www\.)?##;s#/.*##' | tr A-Z a-z); echo "$D" | grep -qx "$dom" && continue; echo "$w|$a|$n"; done \
 | head -150 | tr -d "'" | xargs -P 12 -I{} sh -c 'w=$(echo "{}" | cut -d"|" -f1); s=$(timeout 25 python3 check.py "$w" 2>/dev/null | head -1); echo "{} | $s"' \
 | grep SIGNALE | grep -E "${FILTER:-KEIN-viewport|X5|cm4all|KEIN-https.*(jimdo|©20(0|1))}" | grep -vE " 0kB| [1-3]kB"
