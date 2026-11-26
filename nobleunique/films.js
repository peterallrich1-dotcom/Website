/* Scroll-Filme: Bildfolgen f001.webp ... (n Bilder). "mob" = Hochformat fürs Handy.
   Zurzeit Platzhalter aus den Instagram-Fotos (Kamerafahrt über KI-hochskalierte Bilder).
   Sobald die Higgsfield-Filme da sind, werden nur die Bildfolgen ersetzt. */
window.FILMS = {
  hero:  { dir: "film/a", sd: "film/a-sd", n: 241, mob: { dir: "film/a-m", n: 241 } },
  drive: { dir: "film/b", sd: "film/b-sd", n: 241, mob: { dir: "film/b-m", n: 241 } }
};

/* Highlights (horizontaler Teil) */
window.SIGNATURE = [
  { id: "ferrari-812-gts", img: 0 },
  { id: "porsche-911-turbo-cabriolet", img: 0 },
  { id: "ferrari-portofino", img: 1 },
  { id: "mercedes-amg-g63", img: 0 },
  { id: "audi-rs-q8", img: 0 }
];

/* Erlebnisse: eigene Bilder */
window.OCCASIONS = [
  { src: "img/ferrari-portofino/0.webp", k: "Côte d'Azur", t: "Die Riviera-Tour", p: "Nizza, Èze, Monaco, Menton. Wir planen die Route, reservieren die Hotels und stellen den Wagen bereit." },
  { src: "img/ferrari-portofino/2.webp", k: "Mai in Monaco", t: "Grand Prix", p: "Mit dem passenden Wagen zum Rennwochenende, auf der Strecke, die sonst der Formel 1 gehört." },
  { src: "img/audi-rs-q8/0.webp", k: "Am Hafen", t: "Auto & Yacht", p: "Der Wagen wartet am Steg, die Yacht mit Crew liegt bereit." },
  { src: "img/porsche-911-carrera-cabriolet/0.webp", k: "Starnberg", t: "Das Wochenende", p: "Offen um den See, über die Alpenpässe oder an den Gardasee." },
  { src: "img/extra/fiat-126.webp", k: "Mit Humor", t: "Alle Autos", p: "Und manchmal ist das schönste Auto an der Riviera ein Fiat 126." }
];
