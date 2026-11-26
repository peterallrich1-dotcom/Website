"""Herold (AT): Firmen einer Rubrik in einem Bundesland, Website und Mail.
python3 herold.py steiermark immobilienmakler [seiten]  ->  TSV: mail, website, (leer)"""
import sys, re, urllib.request, urllib.parse, signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
land, rub = sys.argv[1], sys.argv[2]; pages = int(sys.argv[3]) if len(sys.argv) > 3 else 2
seen = set()
for p in range(1, pages + 1):
    u = f"https://www.herold.at/gelbe-seiten/{urllib.parse.quote(land)}/{rub}/" + (f"?page={p}" if p > 1 else "")
    try: s = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read().decode("utf-8", "ignore")
    except Exception: break
    web = {v: h for h, v in re.findall(r'href="(http[^"]+)"[^>]*data-ht-label="go_to_website" data-ht-value="(\d+)"', s)}
    mail = {v: h for h, v in re.findall(r'href="mailto:([^"]+)"[^>]*data-ht-label="send_mail" data-ht-value="(\d+)"', s)}
    for v, w in web.items():
        if v in seen: continue
        seen.add(v); print(f"{mail.get(v, '')}\t{w}\t{land}")
