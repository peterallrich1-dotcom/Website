"""Gelbe Seiten mit Telefonnummer: python3 gs_tel.py rubrik stadt -> TSV name, website, adresse, telefon"""
import sys, re, base64, html, urllib.request, signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
rub, city = sys.argv[1], sys.argv[2]
req = urllib.request.Request(f"https://www.gelbeseiten.de/branchen/{rub}/{city}", headers={"User-Agent": "Mozilla/5.0", "Accept-Encoding": "identity"})
s = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
b = lambda v: base64.b64decode(v).decode("utf-8", "ignore")
for a in re.findall(r"<article.*?</article>", s, re.S):
    m = re.search(r'data-webseiteLink="([^"]+)"', a)
    if not m: continue
    name = re.search(r'<h2[^>]*>(.*?)</h2>', a, re.S)
    name = html.unescape(re.sub(r"<[^>]+>", "", name.group(1)).strip()) if name else "?"
    adr = re.search(r'class="mod-AdresseKompakt__adress-text"[^>]*>(.*?)</', a, re.S)
    adr = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", adr.group(1))).strip()) if adr else ""
    t = re.search(r'phoneNumber[^>]*?data-prg="([^"]+)"', a, re.S)
    print(f"{name}\t{b(m.group(1))}\t{adr}\t{b(t.group(1)) if t else ''}")
