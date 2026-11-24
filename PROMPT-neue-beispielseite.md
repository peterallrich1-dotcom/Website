# Übergabe-Prompt: Neue Beispielseite im Ardena-Standard

Kopiere alles unterhalb der Linie in einen neuen Chat (Claude Code, Repo `peterallrich1-dotcom/Website`) und hänge dein neues KI-Video an.

---

Du arbeitest im Repo `peterallrich1-dotcom/Website` (meine Website **allrich-webdesign.com**, Allrich Webdesign aus Potsdam). Ich verkaufe Websites mit **Scroll-Film**: Beim Scrollen läuft ein kurzer Film Bild für Bild ab. Ich habe dir ein neues KI-Video angehängt (meist aus Higgsfield, 15 s, 1280×720, 24 fps). Baue daraus eine **neue Beispielseite für eine andere Branche**, im selben Standard wie meine beste Seite **Ardena** (`ardena/index.html`, live unter allrich-webdesign.com/ardena/). Qualität hat oberste Priorität. Gib dir richtig Mühe, das ist mein wichtigstes Produkt.

## Repo, Branches, Live-Gang
- Die Live-Seite wird per GitHub Pages aus dem Branch **`claude/elegant-fermi-bsu21u`** ausgeliefert (dort liegt die `CNAME`). Jede Beispielseite ist ein Ordner auf oberster Ebene, z. B. `ardena/`, `velaro/`, `cafe/`, `jet/`, `autovermietung/`.
- Arbeite auf dem Branch, den die Session vorgibt. Hol dir vorher den Live-Branch per Merge (`git fetch origin claude/elegant-fermi-bsu21u && git merge FETCH_HEAD`).
- **Auf den Live-Branch pushen nur nach meinem ausdrücklichen „Ja“**, und zwar jedes Mal neu. Vorher prüfen, ob ein Fast-Forward möglich ist (`git merge-base --is-ancestor origin/claude/elegant-fermi-bsu21u HEAD`), dann `git push origin HEAD:claude/elegant-fermi-bsu21u`.
- allrich-webdesign.com ist aus der Sandbox nicht erreichbar. Teste lokal mit `python3 -m http.server` und Playwright.

## Ablauf, der funktioniert hat
1. **Video ansehen:** Kontaktabzug mit ffmpeg (`fps=2,tile`) und Szenenwechsel suchen (`select='gt(scene,0.18)'`). Daraus die Kapitel des Films ableiten.
2. **Branche und Firma festlegen:** Die Firma ist erfunden. Wähle eine Branche, die zum Video passt und die es noch nicht gibt. Vorhanden sind: Immobilienmakler (Velaro), Café (Milla), Privatjet (Aurelis), Autovermietung (Noctis), Architektur & Bau (Ardena). Keine echten Marken- oder Personennamen. Im Footer und Impressum steht „fiktives Unternehmen, Beispielseite von Allrich Webdesign“.
3. **Alle Bilder des Videos herausziehen** (alle 24 fps, also ~361 Bilder): `ffmpeg -i video.mp4 raw/f%03d.png`.
4. **Mit KI auf Full HD hochskalieren** (Real-ESRGAN `realesr-general-x4v3`, das schärfste und natürlichste Modell im Test):
   - `pip install spandrel opencv-python-headless` (Torch kommt mit)
   - Gewichte: `https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth`
   - Kachelweise (Kachelgröße 384, 16 px Überlappung) ×4 hochrechnen, dann mit Lanczos auf 1920×1080 verkleinern.
   - Auf 4 CPU-Kernen braucht das ~14 s pro Bild, also ~85 min für 361 Bilder. Im Hintergrund mit `nohup` laufen lassen und die Wartezeit für die Seite nutzen.
   - Kein künstliches Nachschärfen, die Bilder sollen originalgetreu bleiben.
5. **Kodieren:**
   - Desktop: `film/hd/f001.webp`…, 1920×1080, WebP Qualität 86.
   - Handy: `film/m/f001.webp`…, ein 1440×1080-Ausschnitt um das Motiv (Fokus-Keyframes pro Bildnummer), verkleinert auf 1280×960, WebP Qualität 84.
   - Standbilder für Galerie und Klickpunkte: `img/*.webp`, 1920 px, Qualität 90.
   - Film zum Ansehen: H.264, CRF 18. Hintergrund-Loop: CRF 21.
   - Schriften selbst hosten (`fonts/`), kein Google-CDN.
6. **Seite bauen:** als eine HTML-Datei, nach dem Muster von `ardena/index.html` (siehe unten).
7. **Testen** mit Playwright auf Desktop 1440×900 (auch mit deviceScaleFactor 2) und auf Handy (iPhone 13, 375×600, 430×800): mehrere Film-Positionen, jeden Abschnitt und jede Interaktion per Klick. Keine JS-Fehler (der Cloudflare-Beacon ist in der Sandbox blockiert, das ist normal). Screenshots ansehen und Überlappungen beheben.
8. **In die Startseite einbinden** (siehe unten), committen, pushen und mich fragen, ob es live gehen soll.

## Aufbau der Seite (Ardena als Vorlage)
- **Lade-Vorhang:** Das Logo zeichnet sich, bis die ersten 24 Bilder da sind (spätestens nach ~3 s). Ein Inline-Skript im Head lädt das erste Bild vor (`film/hd` oder `film/m`).
- **Scroll-Film auf Canvas:**
  - Bildsatz-Wahl: `const SET = innerWidth <= 860 && innerHeight > innerWidth*.9 ? "m" : "hd"`.
  - Schrittweises Laden: jedes 16., dann 8., 4., 2. Bild und zuletzt alle, mit 6 parallelen Anfragen. `nearest(k)` zeigt bis dahin das nächste geladene Bild.
  - Weiches Nachziehen per `requestAnimationFrame`, `imageSmoothingQuality = "high"`, DPR auf dem Handy bis 3, auf dem Desktop bis 2.
  - **Desktop:** Bild formatfüllend; Kapiteltexte unten links mit Kennzahlen; rechts eine Fortschrittsleiste (bei Ardena das „Bautagebuch“ mit Baumonaten).
  - **Handy:** Bild oben (Höhe `min(Breite*.98, Höhe*.47)` + 60 px), Text darunter auf dunklem Grund, ein dünner Fortschrittsbalken darüber. Bei Bildschirmen unter 760 px Höhe werden die Kennzahlen ausgeblendet.
  - **Klickpunkte im letzten Filmbild:** Positionen in Bild-Koordinaten, umgerechnet für Desktop und Handy-Ausschnitt. Info-Fenster mit Text; auf dem Handy nur die wichtigsten 3–4 Punkte, nicht unter die Kopfleiste, auf dem Desktop nicht über die Schlussüberschrift.
- **Darunter (Branche anpassen):**
  - Intro mit hochzählenden Kennzahlen.
  - Eine **interaktive Spielerei mit den Filmbildern** (bei Ardena ein Regler, mit dem man das Haus Phase für Phase hochzieht, mit Zeitraffer-Knopf, Phasenliste und Zahlungsplan).
  - **„Erkunden“ mit Klickpunkten** auf 2–3 Standbildern (Tabs, Infokarte, Weiter/Zurück).
  - Interaktiver Grundriss bzw. ein branchengerechtes Gegenstück.
  - Galerie (Bento-Raster mit Lightbox, Pfeiltasten).
  - Aktuelle Projekte mit Fortschrittsbalken.
  - Leistungen als Akkordeon mit wechselndem Bild.
  - Rechner (Preis, Kosten o. ä.), der den Wert ins Kontaktformular übernimmt.
  - Ablauf in 5 Schritten mit Versprechen-Kasten.
  - Karte (schematisch, SVG, Orte anklickbar).
  - Stimmen-Slider, Team, häufige Fragen.
  - Kontakt mit Video-Hintergrund und Demo-Formular („wird nicht übertragen“).
  - Footer, Dialoge für Impressum, Datenschutz und Bildnachweis.
  - Badge „Beispielseite von Allrich Webdesign“ unten links.
  - Cloudflare-Web-Analytics-Snippet wie in den anderen Seiten (Token aus `ardena/index.html` kopieren).
- **Design:**
  - Eigenständig pro Seite: eigene Farben als CSS-Variablen, ein Akzent, hell und dunkel wechselnde Abschnitte.
  - Serifen-Display-Schrift plus Sans-Schrift plus Mono für kleine Beschriftungen.
  - Überschriften blenden sich ein (Clip-Reveal), Elemente mit `.rv` erscheinen beim Scrollen.
  - Alles zuerst fürs Handy gedacht; Seitenrand mindestens 16–18 px; kein horizontales Scrollen.
- `<meta name="robots" content="noindex">`, OG-Tags mit Vorschaubild.

## In die Startseite einbinden
- **Deutsche Startseite:** Die Quelle ist `allrich/index.html`, Links dort mit `../ordner/`. Danach `cd allrich && python3 build-root.py`, das erzeugt `/index.html`.
  - Abschnitt „Arbeiten“: Kachel `<a class="tile rv" href="../ordner/">` mit Bild `allrich/img-<name>.jpg` (aus einem HD-Bild, ca. 1320×1080 bzw. 1200×675), dazu `.tag` (Branche · Scroll-Film), `h3` und Kurztext.
  - Anzahl im Einleitungstext anpassen („Fünf Konzeptseiten…“) und den Hinweis „… sind Beispielmarken“ ergänzen.
  - `.tile.big` ist das Aushängeschild (zurzeit Ardena), `.tile.next` geht über die volle Breite.
- **Englische Startseite** `en/index.html`: **von Hand** ändern, Links dort mit `/ordner/`. Das Skript `allrich/build-en.py` ist veraltet und bricht ab.
- **KI-Assistent:** In `allrich/ki-worker/worker.js` die Liste „Beispiele“ ergänzen und den Satz „… nie Kunden nennen“ erweitern. Den Cloudflare Worker veröffentliche ich selbst neu.
- In `README.md` unter „Demos“ einen Eintrag ergänzen.

## Was in diesem Chat sonst passiert ist (zur Info)
- **Noctis (`autovermietung/`):** Drei Higgsfield-Videos (roter, schwarzer, grauer Sportwagen) auf je ~9 s gekürzt (`clips/reel-*.mp4`, 540×960). Eingebaut als:
  - Showroom-Abschnitt mit drei Hochformat-Reels und „Wählen“-Knopf, der den Preisrechner übernimmt;
  - Flottenkarten mit Video statt Zeichnung (`clips/karte-*.mp4`);
  - ein Filmstreifen im hellen Scroll-Teil „Der Wagen“;
  - eine Detail-Reihe in der Nachtgalerie (`clips/detail-*.mp4`).
  - Gelernt: Bei kurzen Loops keine Ein- und Ausblendungen verwenden, sie wirken schwarz.
- **Ardena (`ardena/`):** neu gebaut und als großes erstes Beispiel auf der Startseite (DE und EN) live.

## Meine Erwartungen
- Allerbeste Qualität, auf dem Handy perfekt. Gründlich testen, bevor du sagst, dass es fertig ist.
- Antworte auf Deutsch, kurz und klar. Sag ehrlich, was noch nicht live ist.
- Wenn etwas fehlt (z. B. eine Hochformat-Version des Videos), sag es mir.
