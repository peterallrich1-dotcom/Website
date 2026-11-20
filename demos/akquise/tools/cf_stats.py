"""Besucherzahlen von allrich-webdesign.com aus Cloudflare Web Analytics holen und dauerhaft sammeln.
python3 cf_stats.py  ->  aktualisiert demos/akquise/stats/besucher.json (Zeilen je Tag, alte Tage bleiben erhalten).
Der API-Token wird vom Proxy für api.cloudflare.com eingesetzt (Platzhalter proxy-injected)."""
import json, urllib.request, datetime, pathlib
ACC = '053a3d442fff8e2da3a96649a428cb00'
OUT = pathlib.Path(__file__).resolve().parent.parent / 'stats' / 'besucher.json'
Q = '''query($acc:String!,$start:Time!,$end:Time!){viewer{accounts(filter:{accountTag:$acc}){
 rumPageloadEventsAdaptiveGroups(limit:1000,filter:{datetime_geq:$start,datetime_leq:$end,requestHost_like:"%allrich-webdesign.com"},orderBy:[date_ASC]){count sum{visits} dimensions{date}}}}}'''
now = datetime.datetime.now(datetime.timezone.utc)
var = {'acc': ACC, 'start': (now - datetime.timedelta(days=31)).strftime('%Y-%m-%dT00:00:00Z'), 'end': now.strftime('%Y-%m-%dT%H:%M:%SZ')}
req = urllib.request.Request('https://api.cloudflare.com/client/v4/graphql', data=json.dumps({'query': Q, 'variables': var}).encode(),
                             headers={'Authorization': 'Bearer proxy-injected', 'Content-Type': 'application/json'})
r = json.load(urllib.request.urlopen(req, timeout=60))
if r.get('errors'): raise SystemExit('Cloudflare-Fehler: %s' % r['errors'])
fresh = {g['dimensions']['date']: {'datum': g['dimensions']['date'], 'seitenaufrufe': g['count'], 'besuche': g['sum']['visits']}
         for g in r['data']['viewer']['accounts'][0]['rumPageloadEventsAdaptiveGroups']}
old = json.loads(OUT.read_text())['rows'] if OUT.exists() else []
rows = {x['datum']: x for x in old}
rows.update(fresh)   # die letzten 31 Tage neu, ältere Tage bleiben für immer
out = {'rows': sorted(rows.values(), key=lambda x: x['datum']),
       'meta': [{'label': 'Quelle', 'value': 'Cloudflare Web Analytics, allrich-webdesign.com (ohne Cookies)'},
                {'label': 'Stand', 'value': now.strftime('%Y-%m-%d %H:%M UTC')},
                {'label': 'cf_stats.py', 'value': pathlib.Path(__file__).read_text(), 'type': 'code', 'lang': 'python'}]}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(len(out['rows']), 'Tage gespeichert;', sum(x['besuche'] for x in out['rows']), 'Besuche gesamt')
