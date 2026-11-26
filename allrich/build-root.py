"""Erzeugt ../index.html (Startseite unter allrich-webdesign.com) aus allrich/index.html."""
import pathlib
here = pathlib.Path(__file__).parent
s = (here / "index.html").read_text()
s = s.replace('"../', '"')
for a in ["fonts/", "film/", "img-", "impressum.html", "datenschutz.html"]:
    s = s.replace('"' + a, '"allrich/' + a).replace("url(" + a, "url(allrich/" + a)
s = s.replace("<!doctype html>", "<!doctype html>\n<!-- generiert aus allrich/index.html mit allrich/build-root.py -->", 1)
(here.parent / "index.html").write_text(s)
print("index.html geschrieben")
