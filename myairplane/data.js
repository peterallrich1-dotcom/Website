/* myAirplane – Inhalte. Alle Fakten von myairplane.de (Stand Nov. 2026). */

/* Scroll-Filme. Solange keine KI-Filme da sind, läuft eine Kamerafahrt über echte Fotos ("photos").
   Sobald die Higgsfield-Filme da sind: z. B. hero: { dir: "film/a", sd: "film/a-sd", n: 241, mob: { dir: "film/a-m", n: 241 } } */
window.FILMS = {
  hero: { photos: [
    { src: "img/clouds-sun.webp",    from: [1.18, .5, .62], to: [1.02, .5, .5] },
    { src: "img/cirrus-hangar.webp", from: [1.02, .55, .6], to: [1.22, .62, .58] },
    { src: "img/cirrus-cockpit.webp",from: [1.04, .5, .5],  to: [1.3, .46, .42] },
    { src: "img/cessna-alps.webp",   from: [1.25, .42, .55],to: [1.04, .5, .5] }
  ] },
  drive: { photos: [
    { src: "img/cirrus-salzburg.webp", from: [1.02, .5, .5], to: [1.2, .45, .55] },
    { src: "img/clouds-wing.webp",     from: [1.2, .4, .5],  to: [1.02, .5, .5] },
    { src: "img/cessna-night.webp",    from: [1.04, .5, .5], to: [1.22, .58, .6] }
  ] }
};

window.PLANES = [
  {
    id: "cirrus", reg: "D-EMYA", maker: "Cirrus", name: "SR22 G2", year: 2005, hall: "Halle V",
    lead: "Der schnelle Reiseflieger mit Glascockpit, Fallschirm-Rettungssystem und Enteisung. Vollausstattung, Ledersitze, Sauerstoff an Bord.",
    hp: 310, ktas: 180, seats: 4, range: "ca. 1.000 NM",
    fuel: "Avgas, Standard-Betankung für ca. 3 h mit 4 Personen",
    price: { charter: 349, member: 299, day: 99 },
    stats: [["310", "PS"], ["180", "kt Reise"], ["4", "Sitze"], ["CAPS", "Rettungsschirm"]],
    gallery: ["cirrus-hangar", "cirrus-cockpit", "cirrus-runway", "cirrus-salzburg", "cirrus-jets", "cirrus-tail", "cirrus-cabin", "cirrus-apron", "cirrus-salzburg-b", "cirrus-strausberg", "cirrus-hangar-b", "cirrus-hangar-c"],
    spec: [
      ["Zelle & Motor", ["TCM IO-550-N, 310 PS", "6-Punkt-Motoraufhängung", "Cirrus Airframe Parachute System (CAPS)", "Single Movement Power Lever (SIMPLE)", "Hartzell 3-Blatt-Propeller, polierter Spinner", "TKS-Enteisung"]],
      ["Avionik", ["Avidyne Entegra PFD", "Avidyne EX5000C MFD", "2× Garmin GNS 430 GPS/COM/NAV", "DFC90 digitaler Autopilot", "Garmin GTX 330 Mode-S-Transponder", "Garmin GMA 340 Audio Panel", "Avidyne MLX770 Satelliten-Wetter (Iridium)", "WX-500 Stormscope (Blitze in Echtzeit)", "L3 SkyWatch Verkehrsinformation", "E-TAWS Terrain-Warnung", "EMAX Motor- & Fuel-Monitor", "CMAX elektronische Anflugkarten"]],
      ["Sonstiges", ["Semi-portabler Sauerstoff", "Zweifarbiges Lederinterieur"]]
    ]
  },
  {
    id: "cessna", reg: "D-EVEL", maker: "Cessna", name: "172 N Diesel", year: null, hall: "Halle W",
    lead: "Der sparsame Klassiker mit Thielert-Turbodiesel: außergewöhnliche Steigleistung, nur rund 20 Liter pro Stunde. Ideal für kurze Strecken und günstige Stunden.",
    hp: 155, ktas: 110, seats: 4, range: "ca. 600 NM",
    fuel: "Jet A-1 / Diesel, ca. 20 l pro Stunde",
    price: { charter: 209, member: 189, day: 49 },
    stats: [["155", "PS Diesel"], ["20", "l / Stunde"], ["4", "Sitze"], ["FADEC", "Motorsteuerung"]],
    gallery: ["cessna-alps", "cessna-hangar", "cessna-low", "cessna-cockpit", "cessna-side", "cessna-night", "cessna-tower", "cessna-apron", "cessna-field", "cessna-wing", "cessna-hall"],
    spec: [
      ["Zelle & Motor", ["Thielert 2.0 TDI, 155 PS, Einspritzer", "FADEC, automatisch überwachte Motorsteuerung", "3-Blatt-Verstellpropeller, polierter Spinner"]],
      ["Avionik", ["Klassische Cessna-172-Avionik", "Digitales AED (Fuel Monitoring)", "Digitales CED (Engine Monitoring)"]],
      ["Sonstiges", ["Lederinterieur", "Panorama-Dachfenster", "Innenheizung inkl. Scheiben"]]
    ]
  }
];

/* Highlights (horizontal) */
window.HIGHLIGHTS = [
  { img: "cirrus-hangar", no: "D-EMYA", small: "Cirrus", t: "SR22 G2", dl: [["Leistung", "310 PS"], ["Reise", "180 kt"], ["Ab", "299 € / h"]], open: "cirrus", pos: "60% 60%" },
  { img: "cessna-alps", no: "D-EVEL", small: "Cessna", t: "172 Diesel", dl: [["Leistung", "155 PS"], ["Verbrauch", "20 l / h"], ["Ab", "189 € / h"]], open: "cessna", pos: "50% 60%" },
  { img: "cirrus-cockpit", no: "Avidyne", small: "Glascockpit", t: "Entegra", dl: [["Autopilot", "DFC90"], ["Wetter", "Satellit"], ["Traffic", "SkyWatch"]], open: "cirrus", pos: "50% 40%" },
  { img: "clouds-sun", no: "18.000 ft", small: "Über dem Wetter", t: "Sauerstoff an Bord", dl: [["Enteisung", "TKS"], ["Rettung", "CAPS"], ["Sitze", "4"]], open: "cirrus", pos: "50% 50%" },
  { img: "cessna-night", no: "Schlüssel am Tower", small: "Ihr Zeitplan", t: "Auch außerhalb der Öffnungszeiten", dl: [["Schlüssel", "Tower"], ["Member", "Eigener"], ["Halle", "V / W"]], open: "cessna", pos: "50% 50%" }
];

/* Ziele für die Reichweiten-Karte (lon, lat) */
window.PLACES = [
  ["Schönhagen", 13.164, 52.204, "home"],
  ["Heringsdorf", 14.152, 53.878], ["Sylt", 8.34, 54.913], ["Helgoland", 7.915, 54.185],
  ["Kopenhagen", 12.656, 55.618], ["Hamburg", 9.988, 53.63], ["Rotterdam", 4.437, 51.957],
  ["Prag", 14.266, 50.101], ["Wien", 16.57, 48.11], ["München", 11.786, 48.354],
  ["Salzburg", 13.004, 47.793], ["Zürich", 8.549, 47.458], ["Paris", 2.441, 48.969],
  ["Krakau", 19.785, 50.078], ["Venedig", 12.352, 45.505], ["Rom", 12.595, 41.8], ["Nizza", 7.215, 43.658],
  ["Danzig", 18.466, 54.378], ["Bornholm", 14.759, 55.063], ["Juist", 7.056, 53.681]
];

window.TEAM = [
  { n: "Sebastian Kortwich", r: "Geschäftsführer · Cirrus-Kunden", t: "PPL-A seit 2010. Bei myAirplane betreut er die Cirrus-Kunden." },
  { n: "Ulf Klett", r: "CRI · Checkflüge & Training", t: "Privatpilot seit 2004, Instrumentenflug seit 2014, mehr als 50 Stunden im Jahr. Zurzeit in der Ausbildung zur MEP-IR." },
  { n: "Sami Karaa", r: "Cessna-Kunden", t: "PPL-A und begeisterter Cessna-Pilot. Er betreut die Kunden der D-EVEL." },
  { n: "Christian Lunk", r: "Rechnungswesen & Finanzen", t: "Macht gerade selbst seinen PPL-A und kümmert sich um Abrechnung und Finanzen." }
];
