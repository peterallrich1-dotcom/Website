// Prozedural gebauter Business-Jet (fiktives Modell „Aurelis 8“). Nase zeigt nach +X, oben ist +Y.
import * as THREE from "three";

const L = 30, RMAX = 1.32;

// Rumpfradius entlang der Länge (t = 0 Nase … 1 Heck)
function radius(t) {
  if (t < .15) { const u = t / .15; return RMAX * Math.pow(1 - Math.pow(1 - u, 2.3), .52); }
  if (t < .68) return RMAX;
  const u = (t - .68) / .32; return RMAX * Math.max(.06, 1 - .9 * Math.pow(u, 1.55));
}
function centerY(t) {
  if (t < .15) { const u = 1 - t / .15; return -.18 * u * u; }
  return t > .68 ? Math.pow((t - .68) / .32, 2) * .6 : 0;
}
const xAt = t => (.5 - t) * L;
const tAt = x => .5 - x / L;
const section = (a, r) => [Math.cos(a) * r * 1.03, Math.sin(a) * r * (Math.cos(a) < 0 ? 1.02 : .98)];

function paintMaps() {
  const W = 2048, H = 1024;
  const col = document.createElement("canvas"); col.width = W; col.height = H; const g = col.getContext("2d");
  const met = document.createElement("canvas"); met.width = W; met.height = H; const m = met.getContext("2d");
  g.fillStyle = "#f7f7f4"; g.fillRect(0, 0, W, H); m.fillStyle = "#000"; m.fillRect(0, 0, W, H);
  // u: 0 oben, .25 eine Seite, .5 unten, .75 andere Seite. v: 0 Nase … 1 Heck
  const band = (u0, u1, v0, v1, c, metal) => { for (const off of [0, 1]) { const a = (off ? 1 - u1 : u0) * W, b = (off ? 1 - u0 : u1) * W; g.fillStyle = c; g.fillRect(a, v0 * H, b - a, (v1 - v0) * H); if (metal) { m.fillStyle = "#fff"; m.fillRect(a, v0 * H, b - a, (v1 - v0) * H); } } };
  for (const [u0, u1, dir] of [[.3, .5, 1], [.5, .7, -1]]) {
    const gr = g.createLinearGradient((dir > 0 ? u0 : u1) * W, 0, (dir > 0 ? u1 : u0) * W, 0);
    gr.addColorStop(0, "rgba(22,35,61,0)"); gr.addColorStop(.22, "#16233d"); gr.addColorStop(1, "#16233d");
    g.fillStyle = gr; g.fillRect(u0 * W, .16 * H, (u1 - u0) * W, .8 * H);
  }
  band(.318, .324, .17, .95, "#c9a96b", true);
  // Cockpitscheiben (dunkles Glas) auf beiden Seiten und vorn
  g.fillStyle = "#0a0e15";
  for (const side of [1, -1]) {
    const U = u => (side > 0 ? u : 1 - u) * W, V = v => v * H;
    g.beginPath(); g.moveTo(U(.012), V(.088)); g.lineTo(U(.105), V(.083)); g.lineTo(U(.112), V(.104)); g.lineTo(U(.016), V(.108)); g.closePath(); g.fill();
    g.beginPath(); g.moveTo(U(.118), V(.084)); g.lineTo(U(.19), V(.092)); g.lineTo(U(.19), V(.113)); g.lineTo(U(.124), V(.106)); g.closePath(); g.fill();
    g.beginPath(); g.moveTo(U(.198), V(.094)); g.lineTo(U(.235), V(.101)); g.lineTo(U(.232), V(.116)); g.lineTo(U(.198), V(.114)); g.closePath(); g.fill();
  }
  band(.33, .332, .2, .93, "#c9a96b", true);
  const c = new THREE.CanvasTexture(col); c.colorSpace = THREE.SRGBColorSpace; c.anisotropy = 8;
  const mt = new THREE.CanvasTexture(met); mt.anisotropy = 8;
  return { c, mt };
}

function fuselageGeo(scale = 1) {
  const SEG = 220, RAD = 96, pos = [], uv = [], idx = [];
  for (let i = 0; i <= SEG; i++) {
    const t = i / SEG, r = Math.max(.0005, radius(t) * scale), x = xAt(t), cy = centerY(t);
    for (let j = 0; j <= RAD; j++) { const a = j / RAD * Math.PI * 2, [y, z] = section(a, r); pos.push(x, cy + y, z); uv.push(j / RAD, 1 - t); }
  }
  for (let i = 0; i < SEG; i++) for (let j = 0; j < RAD; j++) { const a = i * (RAD + 1) + j, b = a + RAD + 1; idx.push(a, b, a + 1, b, b + 1, a + 1); }
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute("uv", new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx); g.computeVertexNormals(); return g;
}
function surf(x, a, lift = 0) {
  const t = tAt(x), r = radius(t), [y, z] = section(a, r);
  const n = new THREE.Vector3(0, Math.cos(a), Math.sin(a)).normalize();
  return { p: new THREE.Vector3(x, centerY(t) + y, z).addScaledVector(n, lift), n };
}

// NACA-00xx-Profil, geschlossener Umriss
function profile(n) {
  const pts = [];
  for (let i = 0; i <= n; i++) { const b = i / n * Math.PI, x = (1 - Math.cos(b)) / 2; pts.push([x, 5 * (.2969 * Math.sqrt(x) - .126 * x - .3516 * x * x + .2843 * x ** 3 - .1036 * x ** 4)]); }
  const out = []; for (let i = n; i >= 0; i--) out.push(pts[i]); for (let i = 1; i < n; i++) out.push([pts[i][0], -pts[i][1]]);
  return out;
}
// Flügel als Loft; Spannweite entlang axis ("z" waagerecht, "y" senkrecht)
function loftWing({ root, tip, span, sweep, thRoot = .12, thTip = .09, dihedral = 0, axis = "z", tipRound = .1 }) {
  const prof = profile(30), S = 30, pos = [], idx = [], M = prof.length;
  for (let s = 0; s <= S; s++) {
    const f = s / S, r0 = 1 - tipRound;
    const round = f > r0 && tipRound > 0 ? Math.sqrt(Math.max(.0001, 1 - Math.pow((f - r0) / tipRound, 2))) : 1;
    const chord = THREE.MathUtils.lerp(root, tip, f) * (.25 + .75 * round), th = THREE.MathUtils.lerp(thRoot, thTip, f) * round;
    const le = -sweep * f - (1 - round) * THREE.MathUtils.lerp(root, tip, f) * .38, sp = span * f, lift = Math.tan(dihedral) * sp;
    for (const [px, py] of prof) { const cx = le - px * chord, cy = py * th * chord; pos.push(...(axis === "z" ? [cx, cy + lift, sp] : [cx, sp, cy])); }
  }
  for (let s = 0; s < S; s++) for (let i = 0; i < M; i++) { const a = s * M + i, b = s * M + (i + 1) % M; idx.push(a, a + M, b, b, a + M, b + M); }
  const c0 = pos.length / 3; pos.push(-root * .5, 0, 0); for (let i = 0; i < M; i++) idx.push(c0, (i + 1) % M, i);
  const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals();
  return g;
}
function nacelleGeo() {
  const P = [[2.36, .6], [2.47, .69], [2.4, .78], [1.9, .84], [.6, .855], [-1.2, .78], [-2.0, .66], [-2.25, .6]];
  const curve = new THREE.CatmullRomCurve3(P.map(([x, r]) => new THREE.Vector3(r, x, 0)));
  const g = new THREE.LatheGeometry(curve.getPoints(70).map(v => new THREE.Vector2(v.x, v.y)), 80); g.rotateZ(-Math.PI / 2); return g;
}

export function buildJet(opts = {}) {
  const jet = new THREE.Group(), clip = opts.clippingPlanes || [], env = opts.envIntensity ?? 1;
  const { c: paint, mt } = paintMaps();
  const bodyMat = new THREE.MeshPhysicalMaterial({ map: paint, metalnessMap: mt, metalness: 1, roughness: .2, clearcoat: 1, clearcoatRoughness: .05, envMapIntensity: env, clippingPlanes: clip, side: THREE.DoubleSide });
  const white = new THREE.MeshPhysicalMaterial({ color: 0xf7f7f4, roughness: .22, clearcoat: 1, clearcoatRoughness: .05, envMapIntensity: env, clippingPlanes: clip });
  const navy = new THREE.MeshPhysicalMaterial({ color: 0x16233d, roughness: .28, metalness: .15, clearcoat: 1, clearcoatRoughness: .06, envMapIntensity: env, clippingPlanes: clip });
  const gold = new THREE.MeshPhysicalMaterial({ color: 0xc9a96b, roughness: .22, metalness: 1, clearcoat: .6, envMapIntensity: env, clippingPlanes: clip });
  const chrome = new THREE.MeshStandardMaterial({ color: 0xdfe3e8, roughness: .12, metalness: 1, envMapIntensity: env * 1.2, clippingPlanes: clip });
  const glass = new THREE.MeshPhysicalMaterial({ color: 0x04060a, roughness: .03, metalness: .3, clearcoat: 1, clearcoatRoughness: .02, envMapIntensity: env * 1.5, clippingPlanes: clip });
  const fanMat = new THREE.MeshStandardMaterial({ color: 0x15181d, roughness: .4, metalness: .85, clippingPlanes: clip });

  jet.add(new THREE.Mesh(fuselageGeo(), bodyMat));

  const winGeo = new THREE.CircleGeometry(.5, 40), rimGeo = new THREE.RingGeometry(.5, .62, 40);
  for (const s of [1, -1]) {
    for (let i = 0; i < 9; i++) {
      const { p, n } = surf(8.3 - i * 1.32, s * 1.42, .006), tgt = p.clone().add(n);
      const w = new THREE.Mesh(winGeo, glass); w.position.copy(p); w.lookAt(tgt); w.scale.set(.27, .36, 1); jet.add(w);
      const rim = new THREE.Mesh(rimGeo, chrome); rim.position.copy(p); rim.lookAt(tgt); rim.scale.set(.27, .36, 1); jet.add(rim);
    }
  }
  // Flügel, Winglets, Positionslichter
  const wingTipY = -.82 + Math.tan(.07) * 9.7;
  for (const s of [1, -1]) {
    const w = new THREE.Mesh(loftWing({ root: 5.4, tip: 1.45, span: 9.7, sweep: 5.3, dihedral: .07, tipRound: .04 }), white);
    w.position.set(2.9, -.82, s * .95); if (s < 0) w.scale.z = -1; jet.add(w);
    const wl = new THREE.Mesh(loftWing({ root: 1.45, tip: .5, span: 1.75, sweep: 1.15, thRoot: .1, thTip: .08, axis: "y", tipRound: .2 }), navy);
    wl.position.set(2.9 - 5.3 + .02, wingTipY - .03, s * 10.62); wl.rotation.x = s * -.24; jet.add(wl);
    const nav = new THREE.Mesh(new THREE.SphereGeometry(.07, 12, 12), new THREE.MeshBasicMaterial({ color: s > 0 ? 0x44ff77 : 0xff3030, clippingPlanes: clip }));
    nav.position.set(2.9 - 5.3 - .25, wingTipY + .05, s * 10.66); jet.add(nav);
  }
  const fair = new THREE.Mesh(new THREE.SphereGeometry(1, 64, 32), white); fair.scale.set(4.6, .55, 1.28); fair.position.set(1.0, -1.06, 0); jet.add(fair);

  const fin = new THREE.Mesh(loftWing({ root: 4.6, tip: 2.3, span: 4.75, sweep: 3.7, thRoot: .1, thTip: .09, axis: "y", tipRound: .03 }), navy);
  fin.position.set(-L * .5 + 5.6, .9, 0); jet.add(fin);
  for (const s of [1, -1]) {
    const hs = new THREE.Mesh(loftWing({ root: 2.4, tip: 1.05, span: 4.1, sweep: 2.0, thRoot: .1, thTip: .08, dihedral: -.02, tipRound: .06 }), white);
    hs.position.set(-L * .5 + 1.95, 5.62, 0); if (s < 0) hs.scale.z = -1; jet.add(hs);
  }
  const strobe = new THREE.Mesh(new THREE.SphereGeometry(.06, 10, 10), new THREE.MeshBasicMaterial({ color: 0xffffff, clippingPlanes: clip })); strobe.position.set(-L * .5 - .1, .66, 0); jet.add(strobe);

  const nacG = nacelleGeo();
  for (const s of [1, -1]) {
    const g = new THREE.Group();
    g.add(new THREE.Mesh(nacG, white));
    const lip = new THREE.Mesh(new THREE.TorusGeometry(.69, .085, 24, 80), chrome); lip.rotation.y = Math.PI / 2; lip.position.x = 2.41; g.add(lip);
    const fan = new THREE.Mesh(new THREE.CircleGeometry(.64, 72), fanMat); fan.rotation.y = Math.PI / 2; fan.position.x = 2.08; g.add(fan);
    for (let i = 0; i < 22; i++) { const b = new THREE.Mesh(new THREE.BoxGeometry(.02, .5, .08), chrome); b.position.set(2.1, 0, 0); b.rotation.x = i / 22 * Math.PI * 2; b.translateY(.34); b.rotateY(.5); g.add(b); }
    const spin = new THREE.Mesh(new THREE.SphereGeometry(.2, 24, 16), chrome); spin.scale.x = 1.6; spin.position.x = 2.12; g.add(spin);
    const cone = new THREE.Mesh(new THREE.ConeGeometry(.42, 1.1, 48), chrome); cone.rotation.z = -Math.PI / 2; cone.position.x = -2.65; g.add(cone);
    const band = new THREE.Mesh(new THREE.CylinderGeometry(.862, .86, .12, 80, 1, true), gold); band.rotation.z = Math.PI / 2; band.position.x = .2; g.add(band);
    g.position.set(-L * .5 + 8.5, 1.12, s * 2.12); jet.add(g);
    const py = new THREE.Mesh(loftWing({ root: 2.4, tip: 2.0, span: 1.2, sweep: .3, thRoot: .14, thTip: .12, tipRound: 0 }), white);
    py.position.set(-L * .5 + 9.7, 1.12, s * .82); if (s < 0) py.scale.z = -1; jet.add(py);
  }

  // Innenraum (Schnittansicht)
  const interior = new THREE.Group(); interior.visible = !!opts.interior;
  const cream = new THREE.MeshStandardMaterial({ color: 0xebe1cf, roughness: .65 });
  const walnut = new THREE.MeshPhysicalMaterial({ color: 0x5a3820, roughness: .3, clearcoat: .8 });
  const carpet = new THREE.MeshStandardMaterial({ color: 0xc2b8a6, roughness: .95 });
  const wallIn = new THREE.MeshStandardMaterial({ color: 0xf2ede3, roughness: .8, side: THREE.BackSide, clippingPlanes: clip });
  const rb = (w, h, d, m, x, y, z) => { const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m); b.position.set(x, y, z); interior.add(b); return b; };
  const seat = (x, z, f) => { rb(.8, .48, .74, cream, x, -.36, z); rb(.2, .78, .74, cream, x - f * .38, -.05, z); rb(.8, .1, .12, cream, x, -.06, z + .37); rb(.8, .1, .12, cream, x, -.06, z - .37); };
  rb(20, .08, 2.15, carpet, 1.2, -.64, 0);
  seat(12.0, .45, 1); seat(12.0, -.45, 1);
  rb(1.4, 1.25, .7, walnut, 10.2, 0, .68);
  for (const [x, f] of [[8.4, -1], [6.9, 1]]) { seat(x, .62, f); seat(x, -.62, f); }
  rb(.7, .05, .5, walnut, 7.65, -.12, .62); rb(.7, .05, .5, walnut, 7.65, -.12, -.62);
  for (const x of [5.3, 3.6]) { seat(x, .62, x > 4 ? -1 : 1); seat(x, -.62, x > 4 ? -1 : 1); }
  rb(1.0, .05, 1.4, walnut, 4.45, -.1, 0);
  rb(3.0, .45, .7, cream, 1.0, -.38, .68); rb(3.0, .65, .2, cream, 1.0, -.1, .97); rb(.9, .05, .5, walnut, 1.0, -.25, -.4);
  rb(.06, 1.6, 1.1, walnut, -1.2, .1, 0);
  rb(2.6, .35, 1.7, cream, -3.0, -.44, 0); rb(.55, .18, 1.5, new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: .9 }), -1.95, -.2, 0);
  rb(.18, .9, 1.7, walnut, -4.35, -.06, 0);
  rb(1.2, 1.1, .8, walnut, -5.6, -.06, .55); rb(.5, .45, .5, cream, -5.7, -.36, -.5);
  interior.add(new THREE.Mesh(fuselageGeo(.985), wallIn));
  jet.add(interior);
  jet.userData = { L, interior };
  return jet;
}

export function cloudTexture(seed = 1) {
  const S = 256, c = document.createElement("canvas"); c.width = c.height = S; const g = c.getContext("2d");
  let r = seed * 9301 + 49297; const rnd = () => (r = (r * 9301 + 49297) % 233280) / 233280;
  for (let i = 0; i < 30; i++) {
    const x = S * (.2 + rnd() * .6), y = S * (.38 + rnd() * .3), rad = S * (.1 + rnd() * .2);
    const gr = g.createRadialGradient(x, y - rad * .2, 0, x, y, rad);
    gr.addColorStop(0, "rgba(255,255,255,.7)"); gr.addColorStop(.55, "rgba(255,250,244,.22)"); gr.addColorStop(1, "rgba(255,255,255,0)");
    g.fillStyle = gr; g.beginPath(); g.arc(x, y, rad, 0, Math.PI * 2); g.fill();
  }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
