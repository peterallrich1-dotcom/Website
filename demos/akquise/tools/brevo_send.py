#!/usr/bin/env python3
"""Akquise-Mail über Brevo senden (Links bleiben unverändert).

Aufruf: python3 brevo_send.py EMPFAENGER "Vorname Nachname" "Betreff" mail.html
Der API-Schlüssel wird vom Proxy eingesetzt (Header api-key), daher hier nur ein Platzhalter.
Reply-To und BCC gehen an Gmail, damit Antworten und eine Kopie dort landen.
"""
import json, sys, re, html, urllib.request

GMAIL = "peter.allrich1@gmail.com"
to, name, subject, path = sys.argv[1:5]
body = open(path, encoding="utf-8").read()
text = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>([^<]+)</a>', r'\2: \1', body)
text = html.unescape(re.sub(r"<br\s*/?>|</p>", "\n", text))
text = re.sub(r"<[^>]+>", "", text).strip()
data = {
    "sender": {"name": "Peter Allrich", "email": "peter@allrich-webdesign.com"},
    "to": [{"email": to, "name": name}],
    "replyTo": {"email": GMAIL, "name": "Peter Allrich"},
    "bcc": [{"email": GMAIL}],
    "subject": subject,
    "htmlContent": body,
    "textContent": text,
    "tags": ["akquise"],
}
req = urllib.request.Request(
    "https://api.brevo.com/v3/smtp/email",
    data=json.dumps(data).encode(),
    headers={"api-key": "proxy-injected", "content-type": "application/json"},
)
print(urllib.request.urlopen(req, timeout=30).read().decode())
