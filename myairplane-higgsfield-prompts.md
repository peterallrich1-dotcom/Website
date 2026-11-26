# myAirplane – Higgsfield-Prompts für die Scroll-Filme

Für die Website: allrich-webdesign.com/myairplane/ (Ordner `myairplane/` im Repo)

**Stand:** Auf der Seite läuft zurzeit eine Kamerafahrt über die echten Fotos von myairplane.de (Wolken → Cirrus vor Halle V → Glascockpit → Cessna vor den Alpen). Das Higgsfield-Konto zeigt 0 Credits.

**Kosten:** Seedance 2.5, Omni Reference, 10 s, 1080p, ohne Ton, Bitrate high = **160 Credits pro Video** (geprüft).
- Zwei Scroll-Filme, je 16:9 und 9:16: **640 Credits**.

Sobald Credits da sind: Video erzeugen, mit ffmpeg in 241 Bilder zerlegen (`film/a`, `film/a-sd`, `film/a-m`, ebenso `film/b…`) und in `myairplane/data.js` bei `FILMS` die Zeile `photos: [...]` durch `dir/sd/n/mob` ersetzen (Beispiel steht in der Datei). Sonst ändert sich nichts.

## Bereits in Higgsfield importierte Fotos (media_id)
| Foto | media_id |
|---|---|
| Cirrus D-EMYA vor Halle V (DSC7837) | a7c32030-ee24-4942-9720-628fc2426134 |
| Cirrus Seitenansicht Rotterdam (D-EMYA_EHRD) | 4d66091f-2953-42f2-9ee3-a9650b4fe371 |
| Cirrus vor Jet-Terminal, Türen offen | d11ed846-e68e-43d2-bc4c-ad29f02fefa8 |
| Cirrus Glascockpit (DSC7959) | 7a435df8-6278-49c3-8262-6e331ad6203c |
| Über den Wolken, Sonne (aus der Cirrus) | efbd00b1-e010-49ee-b4fd-9164c24e48c9 |
| Cessna D-EVEL Alpen mit Regenbogen (IMG_2390) | 02bae79d-db2e-4b1b-a73e-c026e303b601 |
| Cessna D-EVEL vor Halle W, tief (DSC7849) | 6f2526d1-499c-4c19-ad49-b38144990745 |

## Film 1 – Hero: Cirrus D-EMYA rollt aus Schönhagen los
Start-Bild: DSC7837. Referenzen: D-EMYA_EHRD, Jet-Terminal-Foto.
```
One continuous cinematic shot, no cuts. The exact white Cirrus SR22 with registration D-EMYA from the reference images stands on the paved apron in front of a large grey metal hangar marked "V" at a small German airfield. Golden hour, warm low sun, long soft shadows. The propeller starts to spin and becomes a blur, the navigation lights blink. The camera starts at the framing of the start image and moves in one smooth, slow, constant motion: a low dolly-in combined with a 70 degree orbit to the left while the aircraft slowly taxis forward past the camera, ending on a low front three-quarter view with open sky behind. Photorealistic, premium aviation commercial, shallow depth of field, 35mm anamorphic look. The aircraft's livery, registration, wheel fairings and tail stay identical to the references the entire time. No people visible, no text, no extra aircraft close to the camera, no camera shake.
```
Auf der Website: ganz oben unter dem Logo, mit „Fast wie ein eigenes Flugzeug“, „Moderne Maschinen. Faire Preise.“, „Sie zahlen nur, was Sie fliegen“ und der Fahrt-/Höhenanzeige bis 180 kt / 17.500 ft.

## Film 2 – „Heute Salzburg“: Cirrus über den Wolken
Keine Start-Bild-Vorgabe (Flug). Referenzen: D-EMYA_EHRD, Jet-Terminal-Foto, Wolken-Foto.
```
One continuous cinematic air-to-air shot, no cuts. The exact white Cirrus SR22 with registration D-EMYA from the reference images cruises smoothly above a closed white cloud layer at sunset, the Alps rising through the clouds on the horizon, warm orange light on the wings, propeller as a soft blur. The camera flies alongside at the same speed, starting at the rear three-quarter view and slowly moving forward to end on a front three-quarter view of the aircraft. Calm, luxurious, photorealistic premium aviation commercial, anamorphic lens look. The aircraft livery, registration and shape stay identical to the references the whole time. No text, no other aircraft, no camera shake.
```
Auf der Website: zweiter Scroll-Film nach dem Vergleich, mit „Heute Salzburg. Morgen zurück.“, „Fair für beide Seiten“ und „Starten, wann es Ihnen passt“.

## Optional – Cessna D-EVEL vor den Alpen
Start-Bild: IMG_2390.
```
One continuous cinematic shot, no cuts. The exact white Cessna 172 with red stripes and registration D-EVEL from the start image stands on the grass apron of an alpine airfield under a rainbow. The camera performs one slow, steady drone rise and 45 degree orbit around the aircraft while the clouds drift and the light turns golden. Photorealistic, calm, premium aviation commercial. The aircraft stays identical to the reference. No people, no text, no camera shake.
```
