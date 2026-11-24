# Scroll-Film „Drohnenflug ins Studio“ – Drehbuch für Higgsfield

Ein durchgehender Drohnenflug (One-Take, ca. 20 s): von draußen durchs Fenster in ein modernes
Homeoffice, auf ein Setup mit zwei Monitoren zu, dann direkt in den Bildschirm hinein, auf dem deine
Website läuft. Das letzte Bild ist fast nur noch dunkles Navy, also genau der Hintergrund deiner
Website. So geht der Film nahtlos in die Seite über.

Texte (Leistungen, Preise, Buttons) werden **nicht** ins Video gerendert, sondern als echter
HTML-Text darübergelegt (siehe `index.html`). Das hat drei Gründe: KI-Videos verwischen Schrift, HTML-Text ist
gestochen scharf, und Google kann ihn lesen. Außerdem kannst du Preise später ändern, ohne neu zu generieren.

## Ablauf

Damit der Flug wie aus einem Guss wirkt, werden zuerst drei Standbilder (Keyframes) erzeugt und
dann zwei Clips, die genau an diesen Bildern beginnen und enden. Clip A endet auf Keyframe 2, Clip B
beginnt dort. Die Naht ist dadurch unsichtbar.

| Schritt | Modell | Einstellungen | Credits |
|---|---|---|---|
| Keyframe 1–3 | `gpt_image_2_6` | 16:9, Logo als Referenz bei K2 und K3 | ca. 1 je Bild |
| Clip A (K1 → K2) | `seedance_2_5` | `omni_reference`, 10 s, 1080p, ohne Ton | 160 |
| Clip B (K2 → K3) | `seedance_2_5` | `omni_reference`, 10 s, 1080p, ohne Ton | 160 |
| **Summe** | | | **ca. 325** |

Die 500er-Aufladung bei Higgsfield reicht also mit Puffer für einen zweiten Versuch eines Clips.

Danach: `./extract-frames.sh clipA.mp4 clipB.mp4` erzeugt die Einzelbilder für den Player.

---

## Keyframe 1 – Anflug von außen

```text
Cinematic architectural photograph at blue hour, shot from a drone hovering at eye level about
ten meters in front of a modern minimalist flat-roof house nestled on a slope among tall pine trees.
The house has a huge floor-to-ceiling glass facade with one sliding panel open. Through the glass we
see a calm, dark, premium home office glowing with soft cool-blue LED light and a warm desk lamp:
a long dark walnut desk with two large ultra-thin monitors whose screens glow deep navy blue.
Deep navy sky with the last trace of light, subtle mist between the pines, wet stone terrace reflecting
the blue interior light. Color palette: midnight navy, electric blue accents (#5b8dff), warm amber
highlights. Shot on ARRI Alexa, 24mm lens, shallow haze, ultra-detailed, photorealistic, no people,
no text.
```

## Keyframe 2 – Im Raum, totale aufs Setup

Referenzbild: **Logo** (Rolle `image_references` / Bildreferenz).

```text
Photorealistic interior of a premium dark home office at night, camera about 2.5 meters from the desk,
slightly elevated, centered on the workstation. A long dark walnut desk with two large ultra-thin
frameless monitors side by side on a matte black arm. The LEFT monitor shows exactly the provided logo
image full screen: the word "ALLRICH" in huge bold white condensed letters with a glowing blue dot to
its left and the word "WEBDESIGN" letter-spaced below, on a deep navy gradient background. The RIGHT monitor
shows a sleek dark navy website with a large bold white headline and a bright blue rounded button,
with a browser frame. On the desk in front: a tablet and a smartphone on a stand, both showing the same
dark navy website in mobile layout, a mechanical keyboard, a mouse, a small concrete plant pot.
Behind the desk an indirect electric blue LED strip washes the dark wall, a tall plant in the corner,
floor-to-ceiling window on the left with pine trees at blue hour outside. Calm, expensive, focused
mood. Palette: midnight navy, electric blue #5b8dff, warm amber desk lamp. 35mm lens, cinematic lighting,
ultra-detailed, no people.
```

## Keyframe 3 – Im Bildschirm (Schlussbild)

Referenzbild: **Logo**.

```text
Extreme close-up straight-on view of the right monitor from Keyframe 2, the screen fills almost the
entire frame, only a thin dark bezel and a hint of blue LED glow visible at the very edges.
The screen shows a dark navy website (background #0a1230 fading to #05070f) in the style of the
provided image: at the top the bold white "ALLRICH" wordmark with the glowing blue dot, below it a
huge bold condensed headline in white and electric blue (#5b8dff), and two rounded pill buttons,
one solid blue and one white. Clean, minimal, lots of dark negative space, subtle screen glow,
photorealistic, razor sharp.
```

---

## Clip A – Durchs Fenster hinein (Start: K1, Ende: K2)

```text
Single continuous FPV cinema drone shot, one take, no cuts. The drone glides slowly and smoothly
forward across the misty terrace between the pine trees, through the open sliding glass door into
the dark home office, gently descending to desk height and settling into a centered view of the
two-monitor workstation. The monitors glow, the blue LED strip shimmers softly, a few dust particles
float in the light. Buttery smooth gimbal motion, constant slow speed, gentle ease-out at the end,
no shaking, no sudden turns. Photorealistic, cinematic, premium architectural film.
```

## Clip B – Rein in die Website (Start: K2, Ende: K3)

```text
Single continuous cinema drone shot, one take, no cuts. Starting from the centered view of the
workstation, the camera pushes slowly forward past the smartphone and tablet on the desk, with a subtle
arc to the right, toward the right monitor. On the right monitor the dark navy website scrolls smoothly
upward as if someone is browsing it, revealing sections with images and blue buttons. The camera keeps
pushing in until the screen fills the entire frame and the website headline is centered.
Buttery smooth, constant slow speed, gentle ease-out at the end, shallow depth of field on the
foreground devices, photorealistic.
```

### Parameter für beide Clips

```json
{
  "model": "seedance_2_5",
  "mode": "omni_reference",
  "duration": 10,
  "resolution": "1080p",
  "aspect_ratio": "16:9",
  "generate_audio": false,
  "medias": [
    { "role": "start_image", "value": "<Keyframe-Job-ID>" },
    { "role": "end_image",   "value": "<Keyframe-Job-ID>" }
  ]
}
```

## Prüfliste vor der Übernahme

- Logo auf dem linken Monitor gut lesbar? Wenn nicht: nur Keyframe 2 neu erzeugen (unter 1 Credit),
  dann Clip A und B neu.
- Kein Ruckeln an der Naht zwischen A und B (Bild 240 / 241).
- Letztes Bild überwiegend dunkles Navy, damit der Übergang in die Seite sauber ist.
