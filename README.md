# Website-Akquise

Automatisierte Pipeline: Firmen mit schwachen Websites finden → Demo-Website bauen → persönliche E-Mail als Entwurf vorbereiten (Freigabe durch Mensch).

## Demos
- `demos/holzwerk-brandt/` – Beispielseite für eine erfundene Tischlerei in Potsdam (3D-Hero mit Three.js).
- `demos/atelier-havel/` – begehbarer 3D-Showroom (erfundenes Möbelstudio, Potsdam). Echte Möbelmodelle (Wayfair via Khronos glTF Sample Assets, CC BY 4.0 / CC0), HDRI von Poly Haven (CC0), Parkett-Texturen aus dem three.js-Repo. Binärdateien liegen als Base64-JSON vor, weil die Artifact-Plattform .glb/.hdr nicht ausliefert.
- `demos/fuge-stein/` – erfundener Badsanierer (Berlin). Beim Scrollen baut sich ein 3D-Bad vom Rohbau bis zur Übergabe auf („Tag 1 bis 14“). Alles selbst gehostet, Impressum/Datenschutz/Lizenzen als Muster.
- `demos/velaro/` – erfundener Luxusmakler (Balearen). Hero: KI-generierter Drohnenflug durch eine Villa, als 240-Frame-Sequenz beim Scrollen abgespielt (Canvas, WebP in Full HD, per mit Real-ESRGAN hochskaliert; eigene Hochformat-Sequenz 810×1080 für Handys). Dazu Exposé mit Etagen-Grundrissen, Portfolio mit im Browser gezeichneten Ansichten, Wertrechner, Marktbericht, Kontaktformular (Demo) und Muster-Rechtstexte.
- `demos/akquise/` – personalisierte Entwürfe für echte Firmen (Vorlage + Datensatz pro Firma, `build.py`). Bisher: Junker (Friedrichshafen), zbz Wohnen (Germering), STREAM (Starnberg). Siehe `demos/akquise/README.md`.
- `demos/cafe/` – erfundenes Café (Muster für die Branche Gastronomie). „Milla Kaffeebar & Rösterei“: Beim Scrollen entsteht ein Iced Latte (Eis, Milch, Espresso) als 238-Frame-Sequenz aus einem vom Nutzer erzeugten KI-Video, auf dem Handy als Hochformat-Ausschnitt mit Text darunter. Dazu das Getränk in Schichten erklärt, Inhaber, Bohnen, Karte, Termine, Besuch. Kurzlink: `/cafe/`.
