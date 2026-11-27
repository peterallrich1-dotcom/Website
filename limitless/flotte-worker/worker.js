// Cloudflare Worker "limitless-flotte": Fahrzeugliste für limitless/ mit Verwaltung.
// KV-Binding DB:  "cars" = JSON-Liste aller Autos (auch ausgeblendete),
//                 "img:<id>/<datei>" = hochgeladene Fotos neuer Autos.
// Secrets: USERS = JSON {"email":"sha256(salt+passwort) hex"}, SALT, TOKEN_KEY.
//
// GET  /cars.js          öffentlich: window.CARS=[...] nur sichtbare Autos
// GET  /img/<id>/<datei> öffentlich: Foto
// POST /login            {email,pw} -> {token}
// GET  /cars             (Login) alle Autos
// PUT  /cars             (Login) Liste speichern
// PUT  /img/<id>/<datei> (Login) Foto hochladen (webp/jpeg, max 4 MB)

const ORIGINS = [
  'https://allrich-webdesign.com', 'https://www.allrich-webdesign.com',
  'https://limitlessperformance.de', 'https://www.limitlessperformance.de',
];
const enc = new TextEncoder();
const hex = buf => [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
const b64u = s => btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const unb64u = s => atob(s.replace(/-/g, '+').replace(/_/g, '/'));

function cors(req) {
  const o = req.headers.get('Origin') || '';
  return {
    'Access-Control-Allow-Origin': ORIGINS.includes(o) ? o : ORIGINS[0],
    'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin',
  };
}
const json = (req, data, status = 200) => new Response(JSON.stringify(data), {
  status, headers: { ...cors(req), 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' },
});

async function hmac(env, msg) {
  const k = await crypto.subtle.importKey('raw', enc.encode(env.TOKEN_KEY), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return hex(await crypto.subtle.sign('HMAC', k, enc.encode(msg)));
}
function same(a, b) {
  if (a.length !== b.length) return false;
  let r = 0; for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}
async function makeToken(env, email) {
  const body = b64u(JSON.stringify({ e: email, x: Date.now() + 30 * 864e5 }));
  return body + '.' + await hmac(env, body);
}
async function authed(req, env) {
  const t = (req.headers.get('Authorization') || '').replace(/^Bearer\s+/, '');
  const [body, sig] = t.split('.');
  if (!body || !sig || !same(sig, await hmac(env, body))) return null;
  try {
    const p = JSON.parse(unb64u(body));
    const users = JSON.parse(env.USERS || '{}');
    return p.x > Date.now() && users[p.e] ? p.e : null;
  } catch { return null; }
}

const ID = /^[a-z0-9-]{2,80}$/;
const FILE = /^t?\d{1,2}\.(webp|jpg)$/;
const num = v => (v === null || v === '' || v === undefined) ? null : (Number.isFinite(+v) ? Math.round(+v) : null);
const str = (v, n = 120) => (v == null || v === '') ? undefined : String(v).slice(0, n);

function clean(list) {
  if (!Array.isArray(list) || list.length > 300) throw new Error('Liste ungültig');
  const seen = new Set();
  return list.map(c => {
    if (!c || !ID.test(c.id) || seen.has(c.id)) throw new Error('Ungültige ID: ' + (c && c.id));
    seen.add(c.id);
    const name = str(c.name), brand = str(c.brand, 60);
    if (!name || !brand) throw new Error('Name und Marke fehlen bei ' + c.id);
    const o = {
      id: c.id, name, brand, cat: str(c.cat, 40) || 'Sportwagen',
      price: num(c.price), n: Math.max(1, Math.min(30, num(c.n) || 1)),
      ps: num(c.ps), cyl: str(c.cyl, 30), ccm: num(c.ccm),
      range: str(c.range, 40), seats: str(c.seats, 20), tag: str(c.tag, 30),
    };
    if (c.hidden) o.hidden = true;
    if (c.up) o.up = true; // Fotos liegen im Worker statt auf der Website
    if (c.ext === 'jpg') o.ext = 'jpg';
    for (const k of Object.keys(o)) if (o[k] === undefined || o[k] === null && !['price', 'ps'].includes(k)) delete o[k];
    return o;
  });
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url), path = url.pathname;
    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors(req) });

    if (req.method === 'GET' && path === '/cars.js') {
      const all = JSON.parse(await env.DB.get('cars') || 'null');
      const base = url.origin + '/img/';
      const vis = all ? all.filter(c => !c.hidden).map(c => {
        const { hidden, up, ...rest } = c; return up ? { ...rest, base: base + c.id + '/' } : rest;
      }) : null;
      return new Response(vis ? 'window.CARS=' + JSON.stringify(vis) + ';' : '/* noch keine Daten */', {
        headers: { 'Content-Type': 'application/javascript; charset=utf-8', 'Cache-Control': 'public, max-age=30', 'Access-Control-Allow-Origin': '*' },
      });
    }

    const im = path.match(/^\/img\/([a-z0-9-]+)\/([^/]+)$/);
    if (req.method === 'GET' && im) {
      const { value, metadata } = await env.DB.getWithMetadata('img:' + im[1] + '/' + im[2], { type: 'arrayBuffer' });
      if (!value) return new Response('Nicht gefunden', { status: 404 });
      return new Response(value, { headers: { 'Content-Type': (metadata && metadata.type) || 'image/webp', 'Cache-Control': 'public, max-age=31536000, immutable', 'Access-Control-Allow-Origin': '*' } });
    }

    if (req.method === 'POST' && path === '/login') {
      let b = {}; try { b = await req.json(); } catch {}
      const email = String(b.email || '').trim().toLowerCase();
      const users = JSON.parse(env.USERS || '{}');
      const h = hex(await crypto.subtle.digest('SHA-256', enc.encode(env.SALT + String(b.pw || ''))));
      if (!users[email] || !same(users[email], h)) {
        await new Promise(r => setTimeout(r, 800));
        return json(req, { error: 'E-Mail oder Passwort falsch.' }, 401);
      }
      return json(req, { token: await makeToken(env, email), email });
    }

    const who = await authed(req, env);
    if (path === '/cars' || im) {
      if (!who) return json(req, { error: 'Bitte neu anmelden.' }, 401);
      if (req.method === 'GET' && path === '/cars') return json(req, { cars: JSON.parse(await env.DB.get('cars') || 'null') });
      if (req.method === 'PUT' && path === '/cars') {
        try {
          const list = clean((await req.json()).cars);
          await env.DB.put('cars', JSON.stringify(list));
          await env.DB.put('log:' + new Date().toISOString(), who, { expirationTtl: 60 * 864e2 });
          return json(req, { ok: true, count: list.length });
        } catch (e) { return json(req, { error: e.message }, 400); }
      }
      if (req.method === 'PUT' && im) {
        const type = req.headers.get('Content-Type') || '';
        if (!ID.test(im[1]) || !FILE.test(im[2]) || !/^image\/(webp|jpeg)$/.test(type)) return json(req, { error: 'Dateityp nicht erlaubt' }, 400);
        const buf = await req.arrayBuffer();
        if (buf.byteLength > 4 * 1024 * 1024) return json(req, { error: 'Foto zu groß' }, 413);
        await env.DB.put('img:' + im[1] + '/' + im[2], buf, { metadata: { type } });
        return json(req, { ok: true });
      }
    }
    return json(req, { error: 'Nicht gefunden' }, 404);
  },
};
