#!/usr/bin/env python3
"""Builds one personalised draft site per client record in clients/*.json.

Usage: python3 build.py            (all clients)
       python3 build.py junker     (one client)
Each draft reuses the film frames and fonts of demos/velaro, so that folder must be hosted alongside.
"""
import json, re, sys, pathlib

here = pathlib.Path(__file__).parent
base = (here.parent / "velaro" / "index.html").read_text(encoding="utf-8")
css = re.search(r"<style>(.*?)</style>", base, re.S).group(1).replace("url(fonts/", "url(../../velaro/fonts/")
tpl = (here / "template.html").read_text(encoding="utf-8")
only = set(sys.argv[1:])
for f in sorted((here / "clients").glob("*.json")):
    if only and f.stem not in only:
        continue
    c = json.loads(f.read_text(encoding="utf-8"))
    out = (tpl.replace("__BASE_CSS__", css)
              .replace("__TITLE__", c["name"] + " · Designentwurf")
              .replace("__NAME__", c["name"])
              .replace("__ACCENT_DARK__", c["accentDark"]).replace("__ACCENT__", c["accent"])
              .replace("__CLIENT_JSON__", json.dumps(c, ensure_ascii=False).replace("</", "<\\/")))
    d = here / f.stem
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(out, encoding="utf-8")
    print("built", d / "index.html", len(out) // 1024, "KB")
