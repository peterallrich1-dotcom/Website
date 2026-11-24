// Prozedural gebauter Business-Jet (fiktives Modell „Aurelis 8“). Achse: Nase zeigt nach +X, oben ist +Y.
import * as THREE from "three";

const L = 30;            // Rumpflänge
const RMAX = 1.3;        // größter Radius

// Radius entlang des Rumpfs (t = 0 Nase … 1 Heck)
function radius(t) {
  if (t < .15) { const u = t / .15; return RMAX * Math.pow(1 - Math.pow(1 - u, 2.4), .5); }
  if (t < .70) return RMAX;
  const u = (t - .70) / .30; return RMAX * (1 - .78 * Math.pow(u, 1.45));
}
// Mittellinie hebt sich am Heck leicht an
function centerY(t) { return t > .7 ? Math.pow((t - .7) / .3, 2) * .55 : 0; }

function liveryTexture() {
  const W = 2048, H = 1024, c = document.createElement("canvas"); c.width = W; c.height = H;
  const g = c.getContext("2d");
  g.fillStyle = "#f6f6f3"; g.fillRect(0, 0, W, H);
  // u (waagerecht) läuft um den Rumpf, v (senkrecht) entlang der Länge (0 Nase … 1 Heck)
  const band = (u0, u1, col, v0 = .1, v1 = .98) => { g.fillStyle = col; g.fillRect(u0 * W, v0 * H, (u1 - u0) * W, (v1 - v0) * H); };
  for (const side of [0, .5]) {
    band(side + .262, side + .272, "#16233d", .12, .97);   // dunkelblaue Zierlinie
    band(side + .274, side + .278, "#c8a86b", .14, .95);   // goldene Linie
  }
  // Kabinenfenster (oval) auf beiden Seiten
  g.fillStyle = "#1a2230";
  for (const side of [0, .5]) {
    for (let i = 0; i < 9; i++) {
      const v = .27 + i * .043, u = side + .225;
      g.beginPath(); g.ellipse(u * W, v * H, W * .0095, H * .012, 0, 0, Math.PI * 2); g.fill();
    }
  }
  // Cockpitscheiben
  g.fillStyle = "#121821";
  for (const side of [0, .5]) {
    g.beginPath(); g.moveTo((side + .17) * W, .085 * H); g.lineTo((side + .245) * W, .07 * H); g.lineTo((side + .25) * W, .11 * H); g.lineTo((side + .18) * W, .118 * H); g.closePath(); g.fill();
  }
  // Tür (nur Kontur) links
  g.strokeStyle = "rgba(20,30,45,.35)"; g.lineWidth = 3; g.strokeRect(.205 * W, .17 * H, .045 * W, .045 * H);
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  return tex;
}

function fuselageGeo() {
  const SEG = 160, RAD = 72, pos = [], uv = [], idx = [];
  for (let i = 0; i <= SEG; i++) {
    const t = i / SEG, r = Math.max(.0001, radius(t)), x = (.5 - t) * L, cy = centerY(t);
    for (let j = 0; j <= RAD; j++) {
      const a = j / RAD * Math.PI * 2;
      // leicht ovaler Querschnitt
      pos.push(x, cy + Math.cos(a) * r * 1.04, Math.sin(a) * r);
      uv.push(j / RAD, 1 - t);
    }
  }
  for (let i = 0; i < SEG; i++) for (let j = 0; j < RAD; j++) {
    const a = i * (RAD + 1) + j, b = a + RAD + 1;
    idx.push(a, b, a + 1, b, b + 1, a + 1);
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute("uv", new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx); g.computeVertexNormals();
  return g;
}

function sweptShape(root, tip, span, sweep) {
  const s = new THREE.Shape();
  s.moveTo(0, 0); s.lineTo(-root, 0); s.lineTo(-sweep - tip, span); s.lineTo(-sweep, span); s.closePath();
  return s;
}
function airfoil(shape, thick) {
  const g = new THREE.ExtrudeGeometry(shape, { depth: thick, bevelEnabled: true, bevelThickness: thick * .45, bevelSize: thick * .45, bevelSegments: 3, curveSegments: 4 });
  g.translate(0, 0, -thick / 2);
  return g;
}

export function buildJet(opts = {}) {
  const jet = new THREE.Group();
  const clip = opts.clippingPlanes || [];
  const white = new THREE.MeshPhysicalMaterial({ color: 0xf4f4f1, roughness: .28, metalness: .05, clearcoat: 1, clearcoatRoughness: .12, clippingPlanes: clip });
  const body = new THREE.MeshPhysicalMaterial({ map: liveryTexture(), roughness: .26, metalness: .04, clearcoat: 1, clearcoatRoughness: .1, clippingPlanes: clip, side: THREE.DoubleSide });
  const navy = new THREE.MeshPhysicalMaterial({ color: 0x16233d, roughness: .35, metalness: .2, clearcoat: .8, clippingPlanes: clip });
  const metal = new THREE.MeshStandardMaterial({ color: 0x9aa0a8, roughness: .35, metalness: .9, clippingPlanes: clip });
  const dark = new THREE.MeshStandardMaterial({ color: 0x0c0f14, roughness: .6, clippingPlanes: clip });

  const fus = new THREE.Mesh(fuselageGeo(), body); fus.name = "fuselage"; jet.add(fus);

  // Tragflächen mit V-Stellung und Winglets
  for (const s of [1, -1]) {
    const wing = new THREE.Mesh(airfoil(sweptShape(5.2, 1.5, 9.6, 5.4), .22), white);
    wing.rotation.x = s * Math.PI / 2; wing.position.set(2.6, -.75, s * .9);
    wing.rotateX(-s * .06);
    jet.add(wing);
    const wl = new THREE.Mesh(airfoil(sweptShape(1.5, .55, 1.6, 1.0), .1), navy);
    wl.position.set(2.6 - 5.4, -.75 + 0.5, s * (.9 + 9.55)); wl.rotation.x = s * -.25;
    jet.add(wl);
  }
  // Seitenleitwerk (T-Leitwerk)
  const fin = new THREE.Mesh(airfoil(sweptShape(4.4, 2.2, 4.6, 3.6), .2), navy);
  fin.position.set(-L * .5 + 5.2, .9, 0); jet.add(fin);
  for (const s of [1, -1]) {
    const hs = new THREE.Mesh(airfoil(sweptShape(2.3, 1.0, 4.0, 1.9), .14), white);
    hs.rotation.x = s * Math.PI / 2; hs.position.set(-L * .5 + 1.6, 5.45, s * .1); jet.add(hs);
  }
  // Triebwerke am Heck
  for (const s of [1, -1]) {
    const nac = new THREE.Group();
    const shell = new THREE.Mesh(new THREE.CylinderGeometry(.78, .68, 4.6, 48, 1, true), white); shell.rotation.z = Math.PI / 2; nac.add(shell);
    const lip = new THREE.Mesh(new THREE.TorusGeometry(.75, .07, 16, 48), metal); lip.rotation.y = Math.PI / 2; lip.position.x = 2.3; nac.add(lip);
    const fan = new THREE.Mesh(new THREE.CircleGeometry(.72, 48), dark); fan.rotation.y = Math.PI / 2; fan.position.x = 2.1; nac.add(fan);
    const cone = new THREE.Mesh(new THREE.ConeGeometry(.5, 1.0, 32), metal); cone.rotation.z = -Math.PI / 2; cone.position.x = -2.7; nac.add(cone);
    const stripe = new THREE.Mesh(new THREE.CylinderGeometry(.785, .78, .25, 48, 1, true), navy); stripe.rotation.z = Math.PI / 2; stripe.position.x = -1.2; nac.add(stripe);
    nac.position.set(-L * .5 + 8.2, 1.05, s * 2.05); jet.add(nac);
    const py = new THREE.Mesh(new THREE.BoxGeometry(2.2, .18, 1.1), white); py.position.set(-L * .5 + 8.2, 1.0, s * 1.25); jet.add(py);
  }

  // Innenraum für die Schnittansicht
  const interior = new THREE.Group(); interior.name = "interior"; interior.visible = !!opts.interior;
  const cream = new THREE.MeshStandardMaterial({ color: 0xe9dfcc, roughness: .7 });
  const walnut = new THREE.MeshStandardMaterial({ color: 0x5b3a23, roughness: .45, metalness: .1 });
  const carpet = new THREE.MeshStandardMaterial({ color: 0xbdb3a1, roughness: .95 });
  const wallIn = new THREE.MeshStandardMaterial({ color: 0xf1ece2, roughness: .8, side: THREE.BackSide });
  const floor = new THREE.Mesh(new THREE.BoxGeometry(19.5, .08, 2.1), carpet); floor.position.set(1.0, -.62, 0); interior.add(floor);
  const rb = (w, h, d, m, x, y, z, r = 0) => { const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m); b.position.set(x, y, z); b.rotation.y = r; interior.add(b); return b; };
  const seat = (x, z, face) => { rb(.78, .5, .72, cream, x, -.33, z); rb(.18, .75, .72, cream, x - face * .38, -.05, z); };
  // Cockpit
  seat(12.1, .45, 1); seat(12.1, -.45, 1); rb(.6, .5, 1.6, dark, 13.2, -.1, 0);
  // Bordküche
  rb(1.4, 1.2, .7, walnut, 10.2, -.0, .66);
  // Clubsitze mit Tischen
  for (const [x, f] of [[8.4, -1], [6.9, 1]]) { seat(x, .62, f); seat(x, -.62, f); }
  rb(.7, .06, .5, walnut, 7.65, -.12, .62); rb(.7, .06, .5, walnut, 7.65, -.12, -.62);
  // Esstisch
  for (const x of [5.3, 3.6]) { seat(x, .62, x > 4 ? -1 : 1); seat(x, -.62, x > 4 ? -1 : 1); }
  rb(1.0, .06, 1.4, walnut, 4.45, -.1, 0);
  // Sofa
  rb(3.0, .45, .7, cream, 1.0, -.36, .66); rb(3.0, .65, .2, cream, 1.0, -.08, .95);
  rb(.9, .05, .5, walnut, 1.0, -.25, -.4);
  // Trennwand + Schlafzimmer
  rb(.08, 1.6, 2.0, walnut, -1.2, .1, 0).scale.z = .55;
  rb(2.6, .35, 1.7, cream, -3.0, -.42, 0); rb(.5, .2, .9, new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: .9 }), -2.0, -.15, 0);
  rb(.2, .9, 1.7, walnut, -4.35, -.05, 0);
  // Bad
  rb(1.2, 1.1, .8, walnut, -5.6, -.05, .55); rb(.5, .45, .5, cream, -5.7, -.35, -.5);
  const inner = new THREE.Mesh(fuselageGeo(), wallIn); inner.scale.set(1, .985, .985); interior.add(inner);
  inner.material.clippingPlanes = clip;
  jet.add(interior);
  jet.userData = { L, interior };
  return jet;
}

export function cloudTexture(seed = 1) {
  const S = 256, c = document.createElement("canvas"); c.width = c.height = S; const g = c.getContext("2d");
  let r = seed * 9301 + 49297; const rnd = () => (r = (r * 9301 + 49297) % 233280) / 233280;
  for (let i = 0; i < 26; i++) {
    const x = S * (.25 + rnd() * .5), y = S * (.35 + rnd() * .35), rad = S * (.12 + rnd() * .2);
    const gr = g.createRadialGradient(x, y, 0, x, y, rad);
    gr.addColorStop(0, "rgba(255,255,255,.55)"); gr.addColorStop(.6, "rgba(255,255,255,.18)"); gr.addColorStop(1, "rgba(255,255,255,0)");
    g.fillStyle = gr; g.beginPath(); g.arc(x, y, rad, 0, Math.PI * 2); g.fill();
  }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
