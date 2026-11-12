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
| Junker GmbH Wohnbau + Immobilien | Friedrichshafen | junker-wohnbau.de | feste Breite, nicht mobil, sehr alte Optik; Bauträger, 500+ Einheiten | `junker/` | gesendet 12.11.2026 |
| zbz Wohnen GmbH | Germering | zbz-wohnen.de | schmale, kleine Darstellung; Architekten-Bauträger | `zbz/` | gesendet 12.11.2026 |
| STREAM GmbH | Starnberg | stream-online.com | NetObjects Fusion 7.5, nicht mobil; Hausverwaltung | `stream/` | gesendet 12.11.2026 |
| RÜBA Immobiliengruppe | München | rueba.com | sehr alt, nicht mobil; Bauträger seit 1978 | `rueba/` | gesendet 12.11.2026 |
| LMI Immobilien & Hausverwaltung KG | Seefeld / Andechs | lmi-immobilien.de | sehr alt, nicht mobil | `lmi/` | gesendet 12.11.2026 |
| Steiner Immobilien GmbH | Garmisch-Partenkirchen | steiner-immo.de | gedrängt, alte Optik; Makler seit 55+ Jahren | `steiner/` | gesendet 12.11.2026 |
| Fahrländer Immobilien | Freiburg | fahrlaender-immobilien.de | alte Optik; Makler seit 1973 | `fahrlaender/` | gesendet 12.11.2026 |
| Licker Immobilien GmbH | Ludwigsburg | licker.de | ältere Optik, feste Breite | `licker/` | gesendet 12.11.2026 |
| Das Haus mit Pfiff Bauträger GmbH | Baierbrunn | breckerbohm.de | alte Optik, sichtbare Debug-Leiste | `breckerbohm/` | gesendet 12.11.2026 |
| Martin Weiß Immobilien | München | martin-weiss-immobilien.de | schlichte, ältere Optik | `martin-weiss/` | gesendet 12.11.2026 |
| Max Neuner Immobilien | Garmisch-Partenkirchen | maxneuner-immobilien.de | sehr karg | `maxneuner/` | gesendet 12.11.2026 |
| Holz & Stein GmbH | Traunstein | holzundstein.com | feste Breite, alte Optik | `holzundstein/` | gesendet 12.11.2026 |
| Goldmann & Partner | Starnberg | goldmann-partner.de | ältere Optik; Gewerbeimmobilien | `goldmann/` | gesendet 12.11.2026 |
| Architekt Dieter Ankerne | Puchheim | architekt-ankerne.de | sehr alte Optik | `ankerne/` | Entwurf |
| Architektur Achim Hildebrand | Friedrichshafen | architektur-hildebrand.de | Grafik-Navigation, Dateien von 2015 | `hildebrand/` | Entwurf |
| Arnes Hausverwaltung GmbH | Gaggenau / Stuttgart | arnes-hv.de | Baukasten, alte Optik | `arnes/` | Entwurf |
| BMI Immobilienmanagement GmbH | Münsing | bmi-im.de | Copyright 2014 | `bmi/` | Entwurf |
| CS Hausverwaltung | Böblingen | cshausverwaltung.de | Baukasten, alte Optik | `cs/` | Entwurf |
| Bienek Immobilien Management | Heidelberg | heidelberg-immobilien-bienek.de | Gerüst von 2009 | `bienek/` | Entwurf |
| Immobilienverwaltung Graf | Piding | iv-graf.de | sehr alte Optik | `graf/` | Entwurf |
| Architekturbüro Lehmann & Schiefer | Lauffen a. N. | lehmann-schiefer.de | nur eine Visitenkarte, Copyright 2005 | `lehmann-schiefer/` | Entwurf |
| YK Architektur | Kornwestheim | yk-architektur.de | alte Optik, Projekte als Liste | `yk/` | Entwurf |

Weitere geprüfte Kandidaten (noch ohne Entwurf): Max Neuner Gewerbe- und Wohnimmobilien (Garmisch-Partenkirchen, maxneuner-immobilien.de, sehr karg), Ritter Bauträger & Immobilien GmbH (Deisenhofen, ritter-bautraeger.de, mittel), Rainer Beger Immobilien und Wohnbau (Lindau, immobilien-beger.de, mittel).
Nicht geeignet, weil bereits modern: Locate Immobilien, Kern Bau, Loibl Bau, Füsser, BMI.
