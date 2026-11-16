"""Website grob bewerten und Impressum lesen.
python3 check.py URL  ->  Signale + Impressum-Auszug (Name, E-Mail)"""
import sys, re, html, urllib.request, urllib.parse, ssl
def get(u):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=20)
        return r.geturl(), r.read(600000).decode("utf-8", "ignore")
    except Exception as e:
        return u, ""
def text(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", s, flags=re.S))).strip()
import signal; signal.signal(signal.SIGPIPE, signal.SIG_DFL)
url = sys.argv[1]
final, s = get(url)
if not s: print("NICHT ERREICHBAR"); sys.exit()
sig = []
sig.append("https" if final.startswith("https") else "KEIN-https")
sig.append("viewport" if re.search(r'name=["\']viewport', s, re.I) else "KEIN-viewport")
yrs = [int(y) for y in re.findall(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?(20\d\d|19\d\d)", s, re.I)]
if yrs: sig.append(f"©{max(yrs)}")
gen = re.search(r'name=["\']generator["\'] content=["\']([^"\']+)', s, re.I)
if gen: sig.append("gen:" + gen.group(1)[:30])
for k in ["jimdo", "wix", "1und1", "ionos", "strato", "homepagebaukasten", "webnode", "wordpress", "flash", "<table"]:
    if k in s.lower(): sig.append(k)
sig.append(f"{len(s)//1000}kB")
print("SIGNALE:", " ".join(sig))
print("TITEL:", text(re.search(r"<title>(.*?)</title>", s, re.S | re.I).group(1))[:100] if re.search(r"<title>", s, re.I) else "")
print("START:", text(s)[:700])
links = re.findall(r'href=["\']([^"\']+)["\'][^>]*>([^<]{0,40})', s, re.I)
imp = next((h for h, t in links if re.search(r"impressum|imprint", h + t, re.I)), None)
if imp:
    iu = urllib.parse.urljoin(final, imp); _, si = get(iu); t = text(si)
    i = t.lower().find("impressum")
    print("IMPRESSUM:", iu, "\n", t[max(0, i):max(0, i) + 900])
    print("MAILS:", sorted(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", si)))[:5])
