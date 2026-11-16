"""Gelbe Seiten: Firmen einer Rubrik in einer Stadt mit Website auflisten.
python3 gs.py immobilienmakler erfurt  ->  TSV: name, website, adresse"""
import sys, re, base64, html, urllib.request
rub, city = sys.argv[1], sys.argv[2]
req = urllib.request.Request(f"https://www.gelbeseiten.de/branchen/{rub}/{city}", headers={"User-Agent": "Mozilla/5.0"})
s = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
import signal; signal.signal(signal.SIGPIPE, signal.SIG_DFL)
for a in re.findall(r"<article.*?</article>", s, re.S):
    m = re.search(r'data-webseiteLink="([^"]+)"', a)
    if not m: continue
    web = base64.b64decode(m.group(1)).decode()
    name = re.search(r'<h2[^>]*>(.*?)</h2>', a, re.S)
    name = html.unescape(re.sub(r"<[^>]+>", "", name.group(1)).strip()) if name else "?"
    adr = re.search(r'class="mod-AdresseKompakt__adress-text"[^>]*>(.*?)</', a, re.S)
    adr = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", adr.group(1))).strip()) if adr else ""
    print(f"{name}\t{web}\t{adr}")
