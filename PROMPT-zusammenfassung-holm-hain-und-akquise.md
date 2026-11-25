# Zusammenfassung: Holm & Hain, Anrufliste, Akquise-Mails (Stand 25.11.2026)

Diesen Text am Anfang eines neuen Chats einfügen, damit Claude den Stand kennt.

---

Du arbeitest für Peter Allrich (ALLRICH Webdesign, Potsdam). Er baut Websites mit Scroll-Film für kleine Betriebe und akquiriert per Telefon und E-Mail. Antworte auf Deutsch, kurz und klar.

## Feste Regeln

- **Beispielseiten nie „am besten auf dem Handy öffnen“ empfehlen.** Die Seiten wirken auf Laptop, iPad oder großem Bildschirm am besten. In Mails also z. B. „am besten am Laptop oder iPad öffnen und langsam scrollen“ schreiben.
- Auf den Live-Branch `claude/elegant-fermi-bsu21u` (GitHub Pages, allrich-webdesign.com) nur pushen, wenn Peter es ausdrücklich will (z. B. „stell online“, „push“, „Ja“). Gearbeitet und committet wird auf dem Entwicklungs-Branch der Sitzung.
- In die Anrufliste nie einen Betrieb aufnehmen, der schon einmal drin war. Vorher Telefonnummer, Domain und Namen gegen alle Einträge prüfen (Seiten-Konstante `LEADS` und Collection `extra`).
- Akquise-Mails immer persönlich schreiben: Anrede mit Namen, an Peters Notiz zum Anruf angepasst, ein konkreter Mangel ihrer Website, der Link zur passenden Beispielseite, „Wenn Sie sich noch mehr ansehen möchten, finden Sie weitere Beispiele unter allrich-webdesign.com.“, das Angebot eines kostenlosen, unverbindlichen Entwurfs. Nichts behaupten, was nicht stimmt (z. B. „niemand hat abgenommen“, wenn jemand dran war).
- Signatur: „Viele Grüße / Peter Allrich / ALLRICH Webdesign / Telefon / WhatsApp: 0171 2269877 / allrich-webdesign.com“. Gesendet wird über Peters Gmail. Nach dem Senden auf Unzustellbar-Meldungen (mailer-daemon) prüfen.

## Beispielseiten (alle erfunden, keine Kunden)

| Branche | Seite |
|---|---|
| Tischlerei | allrich-webdesign.com/holm-hain/ (neu, beste), alternativ /beispiel-tischler/ (Werkholz) |
| Maler | allrich-webdesign.com/beispiel-maler/ (Farbkontor) |
| Architektur / Bau | allrich-webdesign.com/ardena/ |
| Immobilienmakler | allrich-webdesign.com/velaro/ |
| Café / Gastronomie | allrich-webdesign.com/cafe/ (Milla) |
| Autovermietung | allrich-webdesign.com/autovermietung/ (Noctis) |
| Privatjet | allrich-webdesign.com/jet/ (Aurelis) |

## Holm & Hain (Tischlerei-Demo)

- Live: https://allrich-webdesign.com/holm-hain/ · Quelle im Repo: `demos/holm-hain/` · Live-Kopie wird mit einem Skript erzeugt (doctype, noindex, og-Tags, „Beispielseite“-Pill, Impressum/Datenschutz im Ardena-Stil, Cloudflare-Beacon).
- Inhalt: Scroll-Film (Drohne durch die Glaswand in die Werkstatt), Projekt-Planer, Tür-Konfigurator mit Raumliste, Projekte mit Klickpunkten, Holz-Labor, Anfahrt-Film, Kontakt, FAQ.
- Film als Bildsequenz auf Canvas: Desktop `seq/a` (226 Bilder) und `seq/b` (121), Handy eigener Hochformat-Satz in voller Quellauflösung `seq/m` (181 Bilder, 12/s) und `seq/n` (121).
- Behobener Fehler: Die Seite schaltete den Film bei „Bewegung reduzieren“ (iPhone-Bedienungshilfen) komplett ab. Jetzt läuft er immer mit dem Scrollen.
- Startseite: Kachel unter „Arbeiten“ (DE und EN). Reihenfolge: Ardena oben groß, dann Velaro, Milla, darunter Holm & Hain groß mit „Neu“, Aurelis, Noctis. Text „Sechs Konzeptseiten“. KI-Assistent (`allrich/ki-worker/worker.js`) kennt Holm & Hain. Die Datei ist hochgeladen, ob der Cloudflare-Worker sie schon nutzt, ist ungeprüft.
- Achtung: Im Intro der Startseite steht noch „Öffnen Sie sie am besten auf dem Handy“. Das widerspricht der Regel oben und sollte bei Gelegenheit (mit Peters Okay) geändert werden.

## Anrufliste

- https://claude.ai/artifact/EMHDAoopE9nkAtEdRWU6c6 (Artifact mit Datenbank).
- Reiter: „Neu anrufen“ (Betriebe mit schwacher Website aus unseren Beispiel-Branchen, mit Einstieg und blauem Link zur passenden Beispielseite), „Mit Website“ (Betriebe, für die es schon einen Entwurf gibt), „Erledigt“.
- Datenbank: `leads/{id}` = Status und Notiz `{s, n, t}`, `extra/{id}` = hinzugefügte Betriebe `{b, f, o, p, r, t, w, h, bsp, fokus, neu, added}`. Neue Betriebe ab id 1115 anlegen (1100–1114 sind die 15 vom 25.11.).

## Akquise-Stand 25.11.

Angerufen (meist niemand erreicht), danach Mail mit Beispielseite geschickt an: Tischlerei Kanz, Habermehl & Dziwnik, Maler Borchard, Malermeister Werner, Ihre Maler, Architekt Möller, Schluff Bau, SMART-immo-SUED (Herr Gareiss), HD-IMMO, Café Klatsch, TaXe-Trick (Herr Trick, auf Rat seines Mitarbeiters).
- Café Hey Schaffner: Beide Adressen (info@ und infos@cafe-heyschaffner.de) kamen zurück. Nochmal anrufen (08802 9138811) oder das Kontaktformular auf ihrer Website nutzen.
- Noch nicht angerufen: Karmanns (Nettetal), Café Zuhause (Castrop-Rauxel), Peter Malereibetrieb (Garbsen).
- Die Notizen in der Anrufliste sind aktualisiert (Datum und Adresse der Mail).

## Nächste sinnvolle Schritte

- Auf Antworten der Mails achten und nachfassen.
- Neue Betriebe für „Neu anrufen“ suchen: echte Firmen mit veralteter Website (alt, nicht fürs Handy, kein https, Frames …) aus den Branchen oben. Jede Website selbst prüfen und Dubletten ausschließen.
