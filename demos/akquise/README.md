# Akquise: personalisierte Entwürfe

Pro Firma liegt ein Datensatz in `clients/<kürzel>.json`. `python3 build.py` baut daraus je eine Seite `<kürzel>/index.html` aus `template.html`.
Die Entwürfe nutzen Film-Frames und Schriften aus `../velaro/`, dieser Ordner muss also mit online stehen (z. B. GitHub Pages für das ganze Repo).

Jede Seite trägt unten den festen Hinweis „Designentwurf, nicht die offizielle Website" und `noindex`. Inhalte stammen von der jeweiligen Firmen-Website (Stand November 2026); es werden keine Logos oder Bilder der Firmen verwendet.

## Neue Firma anlegen
1. `clients/junker.json` kopieren, Felder anpassen (Name, Akzentfarbe, Texte, Projekte, Kontakt). `*Wort*` setzt das Akzentwort kursiv.
2. `python3 build.py <kürzel>`
3. E-Mail als Entwurf anlegen, Link zur Demo einsetzen, prüfen, selbst senden.

## Stand der Recherche (12.11.2026)
308 Firmen-Websites aus Gelbe-Seiten-Einträgen (Immobilienmakler, Bauträger) in 18 Orten in Süddeutschland automatisch geprüft, die auffälligsten per Screenshot angesehen.

| Firma | Ort | Website | Befund | Entwurf | Mail |
|---|---|---|---|---|---|
| Junker GmbH Wohnbau + Immobilien | Friedrichshafen | junker-wohnbau.de | feste Breite, nicht mobil, sehr alte Optik; Bauträger, 500+ Einheiten | `junker/` | Entwurf in Gmail |
| zbz Wohnen GmbH | Germering | zbz-wohnen.de | schmale, kleine Darstellung; Architekten-Bauträger | `zbz/` | Entwurf in Gmail |
| STREAM GmbH | Starnberg | stream-online.com | NetObjects Fusion 7.5, nicht mobil; Hausverwaltung | `stream/` | Entwurf in Gmail |

Weitere geprüfte Kandidaten (noch ohne Entwurf): Max Neuner Gewerbe- und Wohnimmobilien (Garmisch-Partenkirchen, maxneuner-immobilien.de, sehr karg), Ritter Bauträger & Immobilien GmbH (Deisenhofen, ritter-bautraeger.de, mittel), Rainer Beger Immobilien und Wohnbau (Lindau, immobilien-beger.de, mittel).
Nicht geeignet, weil bereits modern: Locate Immobilien, Kern Bau, Loibl Bau, Füsser, BMI.
