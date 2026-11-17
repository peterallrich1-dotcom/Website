import sys, re, html, urllib.request, urllib.parse, signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
def get(u):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0", "Accept-Encoding": "identity"}), timeout=15)
        b = r.read(2000000)
        if b[:2] == b"\x1f\x8b": b = __import__("gzip").decompress(b)
        return r.geturl(), b.decode("utf-8", "ignore")
    except Exception: return u, ""
def text(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", s, flags=re.S))).strip()
base = sys.argv[1].rstrip("/")
f, s = get(base)
links = re.findall(r'href=["\']([^"\']+)["\']', s, re.I)
cands = [urllib.parse.urljoin(f, h) for h in links if re.search(r"impressum|imprint|kontakt", h, re.I)]
cands += [base + p for p in ["/impressum", "/impressum.html", "/impressum.php", "/impressum.htm", "/index.php/impressum"]]
frames = re.findall(r'<i?frame[^>]+src=["\']([^"\']+)', s, re.I)
for fr in frames: cands.append(urllib.parse.urljoin(f, fr))
seen = set()
for u in cands:
    if u in seen: continue
    seen.add(u); _, si = get(u); t = text(si)
    if re.search(r"impressum|Angaben gem", t, re.I) and len(t) > 200:
        i = max(t.lower().find("impressum"), 0)
        print("URL:", u); print(t[i:i + 1100]); print("MAILS:", sorted(set(re.findall(r"[\w.+-]+@[\w-]+\.[a-z.]{2,}", si)))[:6]); break
