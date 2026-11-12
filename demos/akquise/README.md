# Akquise: personalisierte Entwürfe

Pro Firma liegt ein Datensatz in `clients/<kürzel>.json`. `python3 build.py` baut daraus je eine Seite `<kürzel>/index.html` aus `template.html`.
Die Entwürfe nutzen Film-Frames und Schriften aus `../velaro/`, dieser Ordner muss also mit online stehen (z. B. GitHub Pages für das ganze Repo).

Jede Seite trägt unten den festen Hinweis „Designentwurf, nicht die offizielle Website" und `noindex`. Inhalte stammen von der jeweiligen Firmen-Website (Stand November 2026); es werden keine Logos oder Bilder der Firmen verwendet.

## Neue Firma anlegen
1. `clients/junker.json` kopieren, Felder anpassen (Name, Akzentfarbe, Texte, Projekte, Kontakt). `*Wort*` setzt das Akzentwort kursiv.
2. `python3 build.py <kürzel>`
3. E-Mail als Entwurf anlegen, Link zur Demo einsetzen, prüfen, selbst senden.

## Stand der Recherche (12.11.2026)
911 Firmen-Websites aus Gelbe-Seiten-Einträgen (Immobilienmakler, Bauträger) in 52 Orten in Süddeutschland automatisch geprüft, die auffälligsten per Screenshot angesehen.

| Firma | Ort | Website | Befund | Entwurf | Mail |
|---|---|---|---|---|---|
| Junker GmbH Wohnbau + Immobilien | Friedrichshafen | junker-wohnbau.de | feste Breite, nicht mobil, sehr alte Optik; Bauträger, 500+ Einheiten | `junker/` | Entwurf in Gmail |
| zbz Wohnen GmbH | Germering | zbz-wohnen.de | schmale, kleine Darstellung; Architekten-Bauträger | `zbz/` | gesendet 12.11.2026 |
| STREAM GmbH | Starnberg | stream-online.com | NetObjects Fusion 7.5, nicht mobil; Hausverwaltung | `stream/` | gesendet 12.11.2026 |
| RÜBA Immobiliengruppe | München | rueba.com | sehr alt, nicht mobil; Bauträger seit 1978 | `rueba/` | Entwurf in Gmail |
| LMI Immobilien & Hausverwaltung KG | Seefeld / Andechs | lmi-immobilien.de | sehr alt, nicht mobil | `lmi/` | Entwurf in Gmail |
| Steiner Immobilien GmbH | Garmisch-Partenkirchen | steiner-immo.de | gedrängt, alte Optik; Makler seit 55+ Jahren | `steiner/` | Entwurf in Gmail |
| Fahrländer Immobilien | Freiburg | fahrlaender-immobilien.de | alte Optik; Makler seit 1973 | `fahrlaender/` | Entwurf in Gmail |
| Licker Immobilien GmbH | Ludwigsburg | licker.de | ältere Optik, feste Breite | `licker/` | Entwurf in Gmail |
| Das Haus mit Pfiff Bauträger GmbH | Baierbrunn | breckerbohm.de | alte Optik, sichtbare Debug-Leiste | `breckerbohm/` | Entwurf in Gmail |
| Martin Weiß Immobilien | München | martin-weiss-immobilien.de | schlichte, ältere Optik | `martin-weiss/` | Entwurf in Gmail |
| Max Neuner Immobilien | Garmisch-Partenkirchen | maxneuner-immobilien.de | sehr karg | `maxneuner/` | Entwurf in Gmail |
| Holz & Stein GmbH | Traunstein | holzundstein.com | feste Breite, alte Optik | `holzundstein/` | Entwurf in Gmail |
| Goldmann & Partner | Starnberg | goldmann-partner.de | ältere Optik; Gewerbeimmobilien | `goldmann/` | Entwurf in Gmail |

Weitere geprüfte Kandidaten (noch ohne Entwurf): Max Neuner Gewerbe- und Wohnimmobilien (Garmisch-Partenkirchen, maxneuner-immobilien.de, sehr karg), Ritter Bauträger & Immobilien GmbH (Deisenhofen, ritter-bautraeger.de, mittel), Rainer Beger Immobilien und Wohnbau (Lindau, immobilien-beger.de, mittel).
Nicht geeignet, weil bereits modern: Locate Immobilien, Kern Bau, Loibl Bau, Füsser, BMI.
