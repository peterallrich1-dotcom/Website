# Website-Akquise

Automatisierte Pipeline: Firmen mit schwachen Websites finden → Demo-Website bauen → persönliche E-Mail als Entwurf vorbereiten (Freigabe durch Mensch).

## Demos
- `demos/holzwerk-brandt/` – Beispielseite für eine erfundene Tischlerei in Potsdam (3D-Hero mit Three.js).
- `demos/atelier-havel/` – begehbarer 3D-Showroom (erfundenes Möbelstudio, Potsdam). Echte Möbelmodelle (Wayfair via Khronos glTF Sample Assets, CC BY 4.0 / CC0), HDRI von Poly Haven (CC0), Parkett-Texturen aus dem three.js-Repo. Binärdateien liegen als Base64-JSON vor, weil die Artifact-Plattform .glb/.hdr nicht ausliefert.
- `demos/fuge-stein/` – erfundener Badsanierer (Berlin). Beim Scrollen baut sich ein 3D-Bad vom Rohbau bis zur Übergabe auf („Tag 1 bis 14“). Alles selbst gehostet, Impressum/Datenschutz/Lizenzen als Muster.
- `demos/sagar-grillhaus/` – Redesign-Demo für ein echtes indisch-singapurisches Restaurant in Potsdam-Fahrland (Infos vom Flyer: Adresse, Telefon, Öffnungszeiten, Business Lunch, Happy Hour, 15 % Online-Rabatt). Komplette echte Speisekarte vom Flyer (~120 Gerichte mit Nummer, Preis, Allergenen, Schärfe; Suche, Filter, Mittagspreise), Platten/Menüs, Live-Status „geöffnet/Happy Hour läuft noch …“ nach Berliner Zeit, Glut-Partikel im Hero, Schema.org-Daten für lokales SEO, mobile Anruf-/Bestellleiste. Ohne Cookies und externe Dienste, Schriften lokal (Fraunces, DM Sans – SIL OFL). Impressum/Datenschutz als Muster.

## Rechts-Check (jede Seite muss das erfüllen, bevor sie rausgeht)
Stand November 2026, Prüfung aller Demos gegen die 6 typischen Abmahnfallen:

| Punkt | Regel | Holzwerk Brandt | Atelier Havel | Fuge & Stein | Sagar Grillhaus |
|---|---|---|---|---|---|
| 1 Schriften | Nur lokal, nie von Google Fonts laden (LG München I, 3 O 17493/20) | ✅ behoben | ✅ | ✅ | ✅ |
| 1b Skripte | Bibliotheken selbst hosten, keine CDNs (überträgt sonst IP-Adressen) | ✅ behoben | ✅ | ✅ | ✅ (keine) |
| 2 Impressum | § 5 DDG, im Footer immer erreichbar, bei Handwerk mit Kammer/Berufsbezeichnung | ✅ ergänzt | ✅ | ✅ | ✅ |
| 3 Cookies/Analytics | Keine Cookies, kein Tracking. Falls doch nötig: erst nach Einwilligung laden (§ 25 TDDDG) | ✅ keine | ✅ keine | ✅ keine | ✅ keine |
| 4 Newsletter | Nur mit Double-Opt-in und Einwilligungs-Protokoll | – kein Newsletter | – | – | – |
| 5 Bilder | Nur eigene oder lizenzierte Bilder, Quellen in „Lizenzen & Bildnachweise“ | ✅ keine Fotos | ✅ CC BY/CC0 genannt | ✅ | ✅ keine Fotos |
| 6 Datenschutz | Datenschutzerklärung mit Kontaktformular, Hoster, Rechten, Aufsichtsbehörde | ✅ ergänzt | ✅ | ✅ | ✅ erweitert |

Geprüft im Browser: keine Verbindungen zu fremden Servern, 0 Cookies, kein localStorage, keine Fehler.

**Vor Livegang beim Kunden:** Platzhalter in Impressum/Datenschutz (`[…]`) mit echten Angaben füllen, Hoster und AV-Vertrag eintragen, Kontaktformular an eine echte Adresse anbinden. Impressum und Datenschutz sind Muster und ersetzen keine Rechtsberatung.

**Achtung bei der Akquise (wichtig!):** Werbe-E-Mails an Firmen ohne deren vorherige Einwilligung sind in Deutschland unzulässig, auch zwischen Unternehmen (§ 7 Abs. 2 Nr. 2 UWG). Das gilt auch für Nachrichten über deren Kontaktformular. Kaltakquise per E-Mail kann also selbst eine Abmahnung auslösen. Sicherer Weg: den ersten Kontakt per Brief (mit Link oder QR-Code zur Demo) oder persönlich herstellen, erst danach per E-Mail weiter, wenn der Kunde das möchte. Echte Firmennamen in Demos (z. B. Sagar Grillhaus) immer deutlich als „Entwurf, keine offizielle Seite“ kennzeichnen und nicht öffentlich verlinken, bevor der Inhaber zugestimmt hat.
