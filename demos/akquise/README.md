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
| Architekt Dieter Ankerne | Puchheim | architekt-ankerne.de | sehr alte Optik | `ankerne/` | gesendet 12.11.2026 |
| Architektur Achim Hildebrand | Friedrichshafen | architektur-hildebrand.de | Grafik-Navigation, Dateien von 2015 | `hildebrand/` | gesendet 12.11.2026 |
| Arnes Hausverwaltung GmbH | Gaggenau / Stuttgart | arnes-hv.de | Baukasten, alte Optik | `arnes/` | gesendet 12.11.2026 |
| BMI Immobilienmanagement GmbH | Münsing | bmi-im.de | Copyright 2014 | `bmi/` | gesendet 12.11.2026 |
| CS Hausverwaltung | Böblingen | cshausverwaltung.de | Baukasten, alte Optik | `cs/` | gesendet 12.11.2026 |
| Bienek Immobilien Management | Heidelberg | heidelberg-immobilien-bienek.de | Gerüst von 2009 | `bienek/` | gesendet 12.11.2026 |
| Immobilienverwaltung Graf | Piding | iv-graf.de | sehr alte Optik | `graf/` | gesendet 12.11.2026 |
| Architekturbüro Lehmann & Schiefer | Lauffen a. N. | lehmann-schiefer.de | nur eine Visitenkarte, Copyright 2005 | `lehmann-schiefer/` | gesendet 12.11.2026 |
| YK Architektur | Kornwestheim | yk-architektur.de | alte Optik, Projekte als Liste | `yk/` | gesendet 12.11.2026 |

Weitere geprüfte Kandidaten (noch ohne Entwurf): Max Neuner Gewerbe- und Wohnimmobilien (Garmisch-Partenkirchen, maxneuner-immobilien.de, sehr karg), Ritter Bauträger & Immobilien GmbH (Deisenhofen, ritter-bautraeger.de, mittel), Rainer Beger Immobilien und Wohnbau (Lindau, immobilien-beger.de, mittel).
Nicht geeignet, weil bereits modern: Locate Immobilien, Kern Bau, Loibl Bau, Füsser, BMI.

## Sammelversand mit dem Velaro-Beispiel (13.11.2026)

Ein Link für alle: https://peterallrich1-dotcom.github.io/Website/velaro/ – kein eigener Entwurf je Firma, Preis 990 €.

Mit geprüfter Beobachtung zur eigenen Website: anton-steininger.de, rinne-emv.de (beide nicht für Smartphones ausgelegt), huebner-vv.de (Copyright 2014), gbg-stadtamhof.de (Copyright 2016).

Allgemeine Mail: locate-immobilien.com, immobilien-piesch.de, remaon.de, goldwasser-immobilien.de, akurat.net, stege-immo.de, hahn-keller.com, langmayer-immobilien.de, dsimmoservice.de, housemaster24.de, immobauprojekt.com, hoschka-immo.de, draexl-immobilien.de, ingvest.de, dragon24.de, bausolide.de, 1516-immobilien.de, immobilien-bausch.de, hvi.immo, bvgiesing.de, bayerische-wohnungsbau.de, barth-architekten.de, twiehaus.de, architektur-berthold.de, hv-minerva.de, img-hv.de, wohnbaureichenhall.de, werkraum-a.net, jenkel-architekten.de, ebh-architekten.de, tolnai-immo.de, medwohnbau.de.

Diese 36 Firmen nicht noch einmal anschreiben.

## Entscheidungen (13.11.2026)

**Muster-Erstmail (freigegeben, Vorlage für jede Firma).** Nur echte Beobachtungen von der Firmen-Website, kein Objekt erfinden.

> Betreff: Eine Website-Idee für {Firma}
>
> Guten Tag {Vorname Nachname},
>
> auf Ihrer Seite habe ich {konkretes Objekt/Detail von der Website} gesehen. So ein Objekt würde ich nicht als Foto zeigen, sondern als Film, der beim Scrollen durch das Haus fliegt.
>
> So sieht eine meiner Websites aus:
> [Hier klicken und das Beispiel ansehen]
>
> Welche Bilder, Videos und Texte zu sehen sind, entscheiden allein Sie, zum Beispiel {Bezug}.
>
> Ich würde mich freuen, wenn Ihnen das Beispiel gefällt.
>
> Peter Allrich

- Keine Nachfass-Mails. Jede Firma bekommt genau eine Mail.
- Antwortvorlagen erst schreiben, wenn eine echte Antwort da ist.
- Kein eigenes Stilprofil nötig, die Muster-Mail ist der Maßstab.
- Preise: Start 990 € (voll personalisierte Seite mit Scroll-Video oben), Plus 1.490 € (Extras: mehr Videos, aufwendigere Darstellung, 3D, mehrere Bereiche), Hosting inkl. Pflege 29 €/Monat (Hosting, Domain und kleine Änderungen immer enthalten; Kosten für Peter ca. 1 €/Monat über Cloudflare Pages). Graf: 990 € plus 29 €/Monat, ohne Hinweis auf „erster Kunde“ oder Rabatt.
- Versand Montag bis Samstag, kein Versand am Sonntag.
- Eigene Absender-Domain mit SPF/DKIM/DMARC erst nach dem ersten Verkauf. Bis dahin Gmail, höchstens 30 bis 40 Mails am Tag.

## Versand 14.11.2026 (ganz Deutschland + Wien)

40 Firmen (34 Makler/Verwalter/Bauträger, 4 Architekten, 2 in Wien), Quelle: Gelbe Seiten und Herold, inhabergeführt, Name aus dem Impressum geprüft. Jede Mail mit eigenem ersten Satz zu einem konkreten Objekt oder Schwerpunkt der Firma, Link zu /Website/velaro/, ohne Preis. Versand in 4 Durchgängen à 10 (10:00, 11:30, 13:00, 14:00 Uhr), keine Rückläufer.

richardemaier.de, flachsbarthkullick.de, wiegand-immobilien.de, merzenich.de, immobilien-demski.de, michaelruland.de, schneider-immobilien.com, dr-reise-immobilien.de, immosax.de, wilbrand-immobilien.de, strassberger.de, fredebeul-immobilien.de, haeuser-simmen.de, thyzel-immobilien.de, koppius-schwartz.de, tofa-immo.com, epunktimmobilien.com, weyel-immobilien.de, kallen.de, proficon-immobilien.de, immofinanzvp.de, werz-immobilien.de, eden-ehbrecht-immobilien.de, architektin-im-wasserturm.de, aip-immobilien.de, rehm-immobilien.de, kotschenreuther24.de, gick-architekten.de, fassbender-immobilien.de, kokon-architektur.de, saale-immobilien.de, jena-makler.de, architekturbuero-drewniok.de, imak-immobilien.de, vista-immobilien.de, immobilienvogel.de, aplusarchitektur.com, schwelme.de, huebl-partner.com, ar-immobilien.at.

Diese 40 Firmen nicht noch einmal anschreiben.

Hinweis: Das Gmail-Werkzeug wandelt jeden Link in einen google.com/url-Umleitungslink um (Empfänger sehen eine Weiterleitungsseite, ein Klick mehr). Abhilfe: eigene Domain mit eigenem Versandweg.

## Antworten und Rückläufer (Stand 14.11.2026)

- Hoschka Immobilien: Inhaberin geht zum Jahresende in den Ruhestand. Freundlich geantwortet, erledigt.
- Architektur Hildebrand: kein Interesse.
- Immobilienverwaltung Graf: Kritik am ersten Entwurf (zu sehr Makler, kein Trackrecord, keine Objekte). Entwurf /graf/ am 13.11. überarbeitet (Verwaltung, Bilanz, Objekte, Verwalterwechsel), Antwort gesendet, wartet auf Fotos, Videos und Kennzahlen.
- Rückläufer (Strato-Spamfilter, „No SPAM please! (B-SCORE)“): twiehaus.de, dragon24.de, housemaster24.de.

## Eigene Website „Allrich Webdesign“ (pausiert, Stand 14.11.2026)

Entwurf liegt in `allrich/` (online unter /Website/allrich/, noindex, nirgends verlinkt). Peter will sie erst später fertigstellen.
- Name: Allrich Webdesign. Zielgruppe: alle Branchen. Preis auf der Seite: „ab 990 €“. Kein Foto.
- Impressum: Peter Allrich, 14476 Potsdam, E-Mail peter.allrich1@gmail.com. Es fehlen noch Straße und Hausnummer. Keine Steuernummer, kein Gewerbe erwähnen.
- Offen: „wir“ oder „ich“, Domain allrich-webdesign.de (Peter kauft sie selbst), danach Weiterleitung per Cloudflare und Versand per Brevo mit eigener Domain, damit Links nicht über google.com/url laufen.
- Hinweis an Peter: Vor dem ersten bezahlten Auftrag die Gewerbeanmeldung klären.

## Stand 15.11.2026
- **Eigene Domain:** `allrich-webdesign.com` (gekauft bei INWX, DNS über Cloudflare, Nameserver hans/nucum.ns.cloudflare.com, A-Records auf GitHub Pages, `www` als CNAME). `CNAME`-Datei im Repo-Root. Alte Links `peterallrich1-dotcom.github.io/Website/...` leiten automatisch weiter. Neue Links ab jetzt: `https://allrich-webdesign.com/<slug>/`.
- **Startseite** `index.html` im Root ist eine Kopie von `allrich/index.html` mit angepassten Pfaden. Bei Änderungen an `allrich/index.html` die Root-Kopie neu erzeugen (Pfade `fonts/`, `film/`, `img-*`, `impressum.html`, `datenschutz.html` mit `allrich/` davor, `../` entfernen).
- **Hero-Film** `allrich/film/` aus Peters Video (dunkles Büro, New-York-Skyline). `film/screen.json` enthält pro Bild die Ecken des Monitors; darauf wird per Homografie eine saubere Seite ohne Text gelegt. Kein Foto auf der Seite (Peter will das nicht).
- **Impressum:** Peter Allrich, Am Föhrenhang 65, 14476 Potsdam (Neu Fahrland).
- **Kaya (YK Architektur, Kornwestheim):** heißer Lead, antwortete am 15.11. (Preis 990 € ok, Website stand wegen Rücken-OPs 2019–2024 still). Antwort am 15.11. abends gesendet: Link zu allrich-webdesign.com, Bitte um Visualisierungen, Fotos, Videos und Text. Nicht nachhaken, auf sein Material warten.
- **Gewerbe:** Anmeldung über eMeldung Potsdam scheiterte an der Straßenauswahl (Am Föhrenhang nicht auswählbar). Peter ruft Montag beim Gewerbeamt an (0331 289-1690).

## Live geschaltet 16.11.2026
- noindex auf der Startseite entfernt (Peter zufrieden). Titel „Peter Allrich · Webdesign Potsdam · Websites mit Scroll-Film“, Canonical, Open-Graph-Bild `allrich/og-image.jpg`, Favicon, strukturierte Daten (ProfessionalService + Person), `robots.txt`, `sitemap.xml`.
- Kundenentwürfe und Velaro bleiben noindex.
- Erledigt 16.11.: Google Search Console (Domain-Property bestätigt über Cloudflare), Sitemap eingereicht, Indexierung beantragt.
- Erledigt 16.11.: Bing Webmaster Tools (Import aus Search Console, Sitemap eingereicht). Google-Unternehmensprofil „Allrich Webdesign“ angelegt (Dienstleistungsunternehmen, Kategorie Webdesigner, Adresse verborgen, Mo–Sa 8–19 Uhr, 9 Leistungen, Beschreibung); Google prüft die Verifizierung (bis 5 Tage). Logo und Fotos ggf. noch hochladen.

## Täglicher Versand ab 16.11.2026 (Ablauf für jeden Durchgang)
**Takt (ab 17.11.2026, Peters Wunsch):** Montag bis Samstag 40 Mails pro Tag zwischen 8:30 und 12:00 Uhr Berlin, 4 Durchgänge à 10 (8:33, 9:33, 10:33, 11:33). Jeder Durchgang ist bis spätestens 12:00 fertig. Peter nicht fragen, selbstständig arbeiten (er vertraut darauf); nur echte Antworten von Firmen an ihn melden.
**STOPP seit 18.11.2026, 08:39 Uhr Berlin:** Brevo hat das Konto zur Prüfung gesperrt („E-Mail-Aktivitäten, die möglicherweise nicht unserer Anti-Spam-Richtlinie entsprechen“, Versand pausiert). D1 vom 18.11. ist noch zugestellt worden (alle 10 „delivered“). Bis Peter etwas anderes sagt: **keine Mails senden**, auch nicht über Gmail. Jeder Durchgang prüft nur Antworten und Rückläufer und meldet sie.
**Diese README hat Vorrang** vor dem Text der geplanten Aufgaben (dort steht teils noch der alte Stand: Gmail-Versand, Link nur auf die Startseite).
**Vor jedem Durchgang zuerst prüfen:** https://allrich-webdesign.com/ und https://allrich-webdesign.com/velaro/ laden mit HTTP 200 (Titel „Peter Allrich · Webdesign Potsdam …“ bzw. Velaro). Wenn nicht: nichts senden, Peter Bescheid geben.

**Vor jedem Durchgang**
1. Gmail prüfen: neue Antworten im Posteingang und Rückläufer (mailer-daemon, „Undelivered“, „Unzustellbar“). Antworten und Rückläufer hier in der Lead-Liste vermerken. Auf echte Antworten nicht selbst antworten, sondern Peter Bescheid geben (Ausnahme: nichts).
2. Lead-Liste und Gmail als Sperrliste (Gmail „Gesendet“ für Mails bis 16.11. mittags, ab dann die BCC-Kopien: Suche `from:peter@allrich-webdesign.com`): keine Firma, keine Domain, keine Person doppelt.

**Firmensuche (10 pro Durchgang)**
- Branchen: Immobilienmakler, Hausverwaltungen, Architekten. Gebiet: ganz Deutschland und Österreich, Städte rotieren (keine Stadt, die schon dran war, bevor alle anderen dran waren).
- Quellen: Gelbe Seiten `/branchen/{rubrik}/{stadt}` (Website base64 in `data-webseiteLink`), Herold `/gelbe-seiten/{stadt}/{rubrik}/` (`data-ht-label` `send_mail` / `go_to_website`). Skripte liegen in `demos/akquise/tools/`.
- **Seit 17.11. (Peter: ja):** auch Firmen mit mittelmäßiger Website (veraltet, aber mobil lesbar) anschreiben; in der Mail dann nur auf die Firma eingehen, nicht auf die Website. Architekten und Österreich stärker einbeziehen (scan.sh mit Rubrik architekten).
- **Bevorzugt Firmen mit schlechter Website** (veraltete Optik, nicht für Handy, kein https, Objekte nur als Liste, Baukasten-Look, kaum Bilder), sonst ohne Website (dann Mail aus dem Branchenbuch). Gute, moderne Websites überspringen.
- Inhabergeführt, keine Ketten/Franchise, höchstens 2 Firmen pro Stadt.
- Startseite und Impressum lesen: Vorname und Nachname der Inhaberin/des Inhabers bzw. Geschäftsführung, ein konkretes Objekt, Projekt oder Schwerpunkt für den ersten Satz.

**Versandweg ab 16.11.2026 nachmittags: Brevo** (nicht mehr das Gmail-Werkzeug, das jeden Link auf google.com/url umschreibt)
- Absender `Peter Allrich <peter@allrich-webdesign.com>`, Reply-To und BCC `peter.allrich1@gmail.com` (Antworten landen in Gmail).
- Senden: HTML der Mail in eine Datei schreiben, dann `python3 demos/akquise/tools/brevo_send.py EMPFAENGER "Vorname Nachname" "Betreff" mail.html`. Der API-Schlüssel wird vom Proxy für `api.brevo.com` eingesetzt (Platzhalter `proxy-injected`).
- Domain bei Brevo authentifiziert (Brevo-Code, DKIM brevo1/brevo2, DMARC in Cloudflare). Gratis-Tarif: 300 Mails/Tag. Test am 16.11.: Link führt ohne Zwischenseite direkt auf allrich-webdesign.com.
- Nach dem Senden die BCC-Kopien in Gmail aufräumen: Label „Akquise gesendet“ (Label_5) setzen, INBOX und UNREAD entfernen (Suche `from:peter@allrich-webdesign.com in:inbox`). Antworten der Firmen kommen trotzdem wieder in den Posteingang.
- Falls Brevo nicht erreichbar ist: nicht über Gmail ausweichen, sondern Peter Bescheid geben.

**Mail** (HTML)
- Betreff: `Eine Website-Idee für {Firma}`
- `Guten Tag {Vorname} {Nachname},`
- Erster Satz: konkret zu einem Objekt, Projekt oder Schwerpunkt der Firma (geprüft, nichts erfinden). Kritik an der Website nur, wenn geprüft und sachlich.
- `So sieht eine meiner Beispiel-Websites aus:` + Link **Hier klicken und das Beispiel ansehen** → `https://allrich-webdesign.com/velaro/` (die Villa-Seite Velaro; Velaro nie als Kunden bezeichnen)
- `Welche Bilder, Videos und Texte zu sehen sind, entscheiden allein Sie, zum Beispiel …` (passend zur Firma)
- `Ich würde mich freuen, wenn Ihnen das Beispiel gefällt.`
- `Peter Allrich`
- Darunter: `Meine Website: ` + Link `allrich-webdesign.com` → `https://allrich-webdesign.com` (geändert am 16.11.2026 auf Peters Wunsch)
- Verboten: Preis, „ausgedacht“, Velaro als Kunde, Anrufen, „melden Sie sich“.

**Nach dem Durchgang:** Jede Firma als Zeile unten eintragen (Firma | Ort | Website | Befund | gesendet am), committen und pushen.

### Versandliste ab 16.11.2026
| Firma | Ort | Website | Befund | Gesendet |
|---|---|---|---|---|
| Immobilienservice Grimm (Steffen Grimm) | Erfurt | grimm24.de | kein https, kaum Inhalt | 16.11. D1 |
| Blümel & Rohde Immobilien-Service (Olaf Blümel) | Magdeburg | bluemel-rohde.de (kontakt@bris-verwaltung.de) | „Website im Aufbau“, kein https | 16.11. D1 |
| Thomas Hund Immobilien | Magdeburg | thomas-hund-immobilien.de | alter T-Online-Baukasten, nicht mobil | 16.11. D1 |
| HMC Immobilien (Michael Homberger) | Kassel | hmci.eu (info@hmci.de) | IONOS-Baukasten, kein https | 16.11. D1 |
| Lingelbach & Choukair Immobilien (Ayse Lingelbach) | Kassel | lingelbach-choukair-immobilien.de (info@luc-immo.de) | kein https, wenig Inhalt | 16.11. D1 |
| D-RENT Immobilien (Dirk Drischmann) | Chemnitz | d-rent.de | Tabellen-Layout, kein https, nicht mobil | 16.11. D1 |
| RSI Ronald Stopp Immobilien | Chemnitz | stoppimmo.de | kein https | 16.11. D1 |
| Windisch Immobilien (Anke Windisch-Zaremba) | Oldenburg | windisch-immo.de | veraltetes Layout | 16.11. D1 |
| Kai Arnold Immobilien | Oldenburg | kai-arnold.de | älteres Tabellen-Layout | 16.11. D1 |

| Wöhrl Immobilienservice (Dr. Martin Wöhrl) | Augsburg | woehrl-immobilien.de | nicht mobil, Tabellen-Layout | 16.11. D2 |
| Immobilien-Treuhand G. Michalsky (Stephan Lonzer) | Osnabrück | immobilien-treuhand.de | eine Seite, nicht mobil | 16.11. D2 |
| Gudrun KAPITZA Immobilien | Osnabrück | kapitza-immobilien.de | Jimdo-Baukasten | 16.11. D2 |
| Kleiber Haus (Norbert Kleiber) | Bielefeld | kleiber-haus.de (hausverwaltung@) | Joomla 2012, kein https | 16.11. D2 |
| Hausverwaltung Neuhaus / AMI (Sonja Neuhaus) | Göttingen | neuhaus-verwaltung-immobilien.de (HVN@) | Tabelle, nicht mobil | 16.11. D2 |
| H + G Göttingen (Anette Wittorf) | Göttingen | hug-goe.de (hv@) | Startseite nicht mobil | 16.11. D2 |
| Immobilien Mersinger (Gerti Mersinger) | Trier | immobilien-mersinger.de | „Homepage im Aufbau“ | 16.11. D2 |
| TRIDOMUS Immobilien (Anna Modestova-Lehnertz) | Trier | tridomus.de | „TESTSEITE“, nicht mobil | 16.11. D2 |
| Nicknig Immobilien (Hans-Uwe Nicknig) | Koblenz | nicknig.com (nicknigimm@aol.com) | „Time for a new Look“ | 16.11. D2 |
| Willam & Dr. Bechtloff Immobilien (Dr. Dagmar Bechtloff) | Celle | willam-bechtloff.de (info@w-b.immobilien) | kein https, nicht mobil | 16.11. D3 |
| Lehmann-Immobilienservice (Andrea Lehmann) | Goslar | lehmann-immobilienservice.de | WebSite-X5-Baukasten | 16.11. D3 |
| Torsten Geßner Immobilien | Zwickau | gessner-immobilien.de | kein https, nicht mobil | 16.11. D3 |
| Immobilien Scott (Thomas Scott) | Plauen | immobilien-scott.de | nicht mobil | 16.11. D3 |
| Schneider Immobilien Consulting (Uwe Schneider) | Gera | schneider-immobilien-consulting.de (u.schneider-immobilien@t-online.de) | Startseite ohne Objekte | 16.11. D3 |
| Singer Immobilien (Bert Singer) | Weimar | singer-immobilien.de (mail@) | Seite von 2005, nicht mobil | 16.11. D3 |
| SNM Immobilien & Hausverwaltung (Swantje Noé) | Troistedt/Weimar | snm-immobilien.de | kein https, nicht mobil | 16.11. D3 |
| Eilenriede Immobilien (Horst Prigge) | Hannover | eilenriede-immo.de | „Browserversion veraltet“-Hinweis | 16.11. D3 |
| Immobilien Brinkmann (Monica Brinkmann) | Bremen | immo-brinkmann.de | kein https | 16.11. D3 |
| Immobilien & Hausverwaltung C. Goller (Thomas Klein) | Plauen | immobilien-goller.de | nicht mobil | 16.11. D3 (Abwesenheitsnotiz bis 19.11.) |
| Schmeißer Immobilien (Jürgen Schmeißer) | Ebsdorfergrund/Marburg | schmeisser.eu | kein https, nicht mobil | 16.11. D4 |
| SHG Hausverwaltung (Norbert Stern) | Marburg | shg-hausverwaltung.com (stern@) | WebSite-X5, 2016 | 16.11. D4 |
| Yildiz Immobilien Plus (Zeynep Yildiz) | Wetzlar | yildizimmobilienplus.de | „Seite in Bearbeitung“ | 16.11. D4 |
| HVD Hausverwaltung Dessau (Mario Saalmann) | Dessau-Roßlau | hv-dessau.de (info@) | NetObjects, nicht mobil | 16.11. D4 |
| Maklerunternehmen Thomas Fiedler | Brandenburg a. d. H. | fiedler-maklerunternehmen.de (thomas@) | eine Textseite, kein https | 17.11. D1 |
| HGV Haus- und Grundstücksverwaltung (Stefan Koch) | Rathenow | hgv-rathenow.de (0173-7182538@web.de) | „Browserversion veraltet“ | 17.11. D1 |
| bios-consult Immobilien (Uwe Rosenkranz) | Bernau | bios-consult.de | kein https, nicht mobil | 17.11. D1 |
| Family Haus Immobilien (Wilfried Sell) | Frankfurt (Oder) | family-haus-immobilien.de | nicht mobil | 17.11. D1 |
| Eismann Hausverwaltung (Marina Brem) | Heidenau | eismann-hausverwaltung.de | nur Name und Mail | 17.11. D1 |
| Harald Braunheim Immobilien | Lüdenscheid | harald-braunheim.de (post@) | nur Name, Mail, Telefon | 17.11. D1 |
| Atlant Immobilien (Steffen Zimmermann) | Nordhausen | atlant-immo.de (atlant-immo-ndh@web.de) | nicht mobil | 17.11. D2 |
| Wahry Immobilien und Hausverwaltung (Mario Wahry) | Quedlinburg | wahry-dachdecker.de (wahry-immobilien@t-online.de) | nur Dachdecker-Seite, kein https | 17.11. D2 |
| Bendix Immobilien (Frank Bendix) | Gotha | bendix-immobilien.de | TYPO3 4.5, nicht mobil | 17.11. D2 |
| HWV Haus- und Wohnungsverwaltung (Frank Eichler) | Döbeln/Zeithain | hwv.de | nicht mobil | 17.11. D3 |
| Immobilien Finanzservice Appel (Siegmund Appel) | Grimma | appel-makler.de | nicht mobil | 17.11. D3 |
| reitmayr architekten (DI Peter Reitmayr) | Graz (AT) | reitmayr-architekten.at | Startseite leer, kein https | 17.11. D4 |
| Dr. Rudolf Galler Immobilientreuhand | Graz (AT) | dr-galler.at (immo@) | Objekte nur mit JavaScript | 17.11. D4 |
| Architekt Johannes Haberl | Pöls (AT) | architekt-haberl.at (arch-haberl@aon.at) | Website 2012, kein https | 17.11. D4 |
| Immobilien Lafenthaler (Gerhard Lafenthaler) | Bad Hofgastein (AT) | lafenthaler.com (info@) | nicht mobil | 17.11. D4 |
| architekturbuehne (Elfrid Wimmer-Repp) | Salzburg (AT) | architekturbuehne.at | kein https, nicht mobil | 17.11. D4 |
| LC4 architektur (W. Lankmayer) | Salzburg (AT) | lc4.at (office@) | nicht mobil | 17.11. D4 |
| Architekturbüro Karin Ritter | Görlitz | architekturbuero-ritter.de (ab.ritter@web.de) | FrontPage 4.0, nicht mobil | 18.11. D1 |
| AVV-Immobilien (Bernd Elechnowitsch) | Pforzheim | avv-immobilien.de (avv-immobilien@live.de) | kein https, Tabellen-Layout, nicht mobil | 18.11. D1 |
| Leuprecht Bauarchitektur (Ing. Gerold Leuprecht) | Dornbirn (AT) | bauarchitektur.at (g.leuprecht@) | TYPO3 2013, kein https, nicht mobil | 18.11. D1 |
| Beyer-Schubert Architektur (Matthias Beyer-Schubert) | Eisenach | beyer-schubert.de (mail@) | „Inhalte werden überarbeitet“ | 18.11. D1 |
| Büro 4 (Jan Krahmer) | Detmold | buero4.info (post@) | Adobe GoLive, nicht mobil | 18.11. D1 |
| Becker Immobilien (Gabriele Becker) | Detmold | immobilien-becker.de (info@) | nicht mobil | 18.11. D1 |
| HELLE Architekten (Silvia und Rolf Helle) | Paderborn | helle-architektur.de (hellearchitekten@gmx.de) | kein https, nicht mobil | 18.11. D1 |
| Hausverwaltung Dieckmann (Andreas Dieckmann) | Lage | hausverwaltung-dieckmann.de (info@) | nur eine Zeile | 18.11. D1 |
| Immobilien Wolff GmbH (Detlef Wolff) | Paderborn | immobilien-wolff.com (mail@) | nicht mobil, nur kleine Vorschaubilder | 18.11. D1 |
| zottele . mallin architekten (DI Christian Zottele) | Bludenz (AT) | zottele-mallin.com (office@) | nur Kontaktdaten, nicht mobil | 18.11. D1 |
Geprüft 18.11. D1, nicht angeschrieben: beaufort.at (kein Name, keine Mail), vontrottzusolz.de (kein Impressum, nur Bilder), bachmann-nothwang.de (nur Verweis auf Kammer), makler-arnold.de (Versicherungsmakler), mrw-architekten.de (Seite ok), klauswanko.at (nur JavaScript), dazu Sachverständige/Fremdbranchen aus Eisenach, Suhl, Ilmenau, Landshut. Städte D1: Görlitz, Pforzheim, Dornbirn, Eisenach, Detmold, Paderborn, Lage, Bludenz. Noch offen für später: grossmann-architekten.de, helms-architektur.de, architektur-kraus.com (Pforzheim-Umgebung), hagelgans-architektur.de, bauplanung-tegethoff.de, kornhardt.de (Minden), iv-schwabe.de.
Geprüft 17.11. D4, nicht angeschrieben: musker.at, hofstaetter-kletzenbauer.at (kein Impressum), sixl-zt.com, zt-schatz.at (3. in Graz, für später), immobilienaust.com, immobilien-rueck.at (kein Name). Österreich über tools/scan_at.sh (Herold nach Bundesland) bringt deutlich mehr Treffer.
Geprüft 17.11. D3, ohne Treffer: Güstrow, Parchim, Ludwigslust, Waren, Torgau, Oschatz, Annaberg, Mittweida, Glauchau; eurocaptura.de (kein Impressum), prosalus-immobilien.de.
Geprüft 17.11. D2, nicht angeschrieben: geyerimmobilien.de (keine Mail, „wird neu aufgebaut“), bauwert.info (kein Name), der-vermieter.info (keine Mail), grasemann-immobilien.de (Domain zu verkaufen), dazu Bayern/Franken (Hof, Bayreuth, Kulmbach, Coburg, Ansbach, Schweinfurt, Bad Kissingen, Aschaffenburg) ohne Treffer.
Hinweis 17.11.: check.py/imp.py lesen jetzt auch gzip-Antworten (vorher Fehlalarme „KEIN-viewport“ bei modernen Seiten). Geprüft 17.11. D1, nicht angeschrieben: schedler-immobilien.de, immobilien-w-wittstock.de, fws-hausverwaltung.de, bj-hausverwaltung.de (Fehlalarm, Seiten ok), styn.immobilien (kein Name), annenhoefe-brb.de (Gewerbeobjekt), am-sonnenufer.de (Seniorenwohnen), streibel-immobilien.de (keine Mail), wortmann-immobilienverwaltung.de (Einkaufszentrum), andreasgrewe.de (Privatvermieter), immo-cux.de, zarnack.de (ok). Städte: Brandenburg a. d. H., Rathenow, Bernau, Frankfurt (Oder), Heidenau, Lüdenscheid.
| Dittrich Immobilien (Hans-Jürgen Dittrich) | Bamberg | dittrichimmobilien.de (immobilien.dittrich@arcor.de) | WebSite X5, ©2015 | 16.11. D5 Brevo |
| Lotz Immobilien (Wolfgang Oetinger) | Bamberg | lotz-immobilien.de (lotz.immobilien@web.de) | Jimdo, nicht mobil | 16.11. D5 Brevo |
| Immobilien Donhauser (Karin Donhauser) | Amberg | immobiliendonhauser.de (info@) | web to date 2014, kein https, nicht mobil | 16.11. D5 Brevo |
| Immobilien Schloßberg GmbH (Gerda Mair) | Stephanskirchen/Rosenheim | immobilien-schlossberg.de (info@) | „Stand: 12.09.2007“ | 16.11. D5 Brevo |
| Schöner Wohnen Martin Walter Immobilien GmbH (Martin Walter) | Offenburg | schoenerwohnen-immo.de (info@) | Tabellen-Layout, nicht mobil | 16.11. D5 Brevo |
| Draxler Freie Architekten (Andrea und Markus Draxler) | Hirschberg | draxler-architekten.de (info@) | IONOS-Baukasten, Titel „Homepage-Titel“ | 16.11. D5 Brevo |
| Lorenz Immobilien (Matthias Lorenz) | Neuwied | lorenzimmobilien.com (info@) | Joomla 1.5, ©2011, nicht mobil | 16.11. D5 Brevo |
| Stein Immobilien (Tina Kindler) | Neuwied | hausverwaltung-neuwied.de (TinaKindler@arcor.de) | nicht mobil | 16.11. D5 Brevo |
Hinweis D5 (16.11. nachmittags, erstmals über Brevo, neue Vorlage mit Velaro-Link und „Meine Website“): Tagessumme 40. Geprüft, nicht angeschrieben: hausverwaltung-rinne.de (schon am 13.11. angeschrieben, mr@rinne-emv.de), img-daub.de (widerspricht Werbung im Impressum), hausverwaltung-strehler.de, hausverwaltung-richter.eu, wohnraumfreunde.de, hausverwaltung-aschaffenburg.de (keine Mail), hausverwaltung-tischer.de (kein Name), alpha-immobilien-fulda.de (Platzhalter), kuhn-immo.de (Domain zu verkaufen). Städte D5: Bamberg, Amberg, Rosenheim, Offenburg, Hirschberg, Neuwied.
Hinweis 16.11.: SNM Immobilien (Swantje Noé) hat jetzt die Adresse hausverwaltung@koehler-hausservice.de (automatische Antwort). Geprüft D4, nicht angeschrieben: bj-hausverwaltung.de (defekt), consultanta.de (Platzhalter), hausverwaltung-reinarz.de, immobilienverwaltung-oezen.de, wittenbergimmobilien.de, seibel-worms.de (keine Mail), aurum-ip.de (kein Name), bepe-immobilien.de (Wartung), stegri-immobilien.de (keine Seite), immobewertung-schmidt.de (Sachverständiger). Städte D4: Marburg, Wetzlar, Dessau.
Geprüft D3, nicht angeschrieben: immobilien.if-c.biz (kein Impressum), immobilien-wolf-plauen.de (keine Mail), heimundgrund.com (kein Name), city-immobilienmakler.de (Kette), ziemek-bau.de. Städte D3: Celle, Goslar, Zwickau, Plauen, Gera, Weimar, Hannover, Bremen. Tipp: Kleinstädte liefern deutlich mehr schwache Websites (tools/scan.sh stadt1 stadt2 ...).
Geprüft, nicht angeschrieben (nicht erneut prüfen): bredereck-immobilien.de (Ltd., Impressum unklar), machalett-immobilien.de (Wartungsseite), brandhuber-immobilien.de (Strato-Platzhalter), scheunpflug.de (Domain zu verkaufen), lange-immobilien.eu (Platzhalter), thaele.de (kein Impressum), sietan.de (Sachverständiger), wentzel-immobilien.com (3. in Magdeburg). Städte 16.11. D1: Erfurt, Magdeburg, Kassel, Chemnitz, Oldenburg (je max. 2).
Geprüft D2, nicht angeschrieben: premium-hv.de / riess-und-gerle.de (Mail nur per JS), overbeck-immobilien.com (keine Website, keine Mail), kleinimmobilien.com (3. Osnabrück), zilk-immobilien.de (kein Name), auer-regensburg.de (keine Mail), krueger-kg.de (kein Impressum gefunden), drechsler-immobilien.de (3. Göttingen), objekt-raum.com, am-hv.de, wm-hausverwaltung.de (kein Name), stoelzgen.de (offline), immobilien-mueller.de (kein Name). Städte D2: Augsburg, Osnabrück, Bielefeld, Göttingen, Trier, Koblenz.
