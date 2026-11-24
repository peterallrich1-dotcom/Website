import sys,re
import os; T=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'template.html'),encoding='utf-8').read()
I={
'I_WA':'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
'I_PHONE':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
}
TICK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
CHK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>'
ICONS={
'roller':'<path d="M4 3h13a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/><path d="M18 5.5h2a1 1 0 0 1 1 1V10a1 1 0 0 1-1 1h-8v3"/><rect x="10" y="14" width="4" height="7" rx="1"/>',
'house':'<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/>',
'brush':'<path d="M9.06 11.9 18.1 2.9a2 2 0 0 1 2.9 2.9l-9 9"/><path d="M7.07 14.94c-1.66 0-3 1.35-3 3.02 0 1.33-2.5 1.52-2 2.02 1.08 1.1 2.49 2.02 4 2.02 2.2 0 4-1.8 4-4.04a3.01 3.01 0 0 0-3-3.02z"/>',
'wall':'<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 9h18M3 15h18M9 4v5M15 9v6M9 15v5"/>',
'shield':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
'layers':'<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
'cabinet':'<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M12 3v18M9 11v2M15 11v2"/>',
'door':'<path d="M5 21V4a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v17"/><path d="M3 21h18M15 12h.01"/>',
'stairs':'<path d="M3 21h4v-4h4v-4h4V9h4V5h2"/>',
'kitchen':'<rect x="3" y="10" width="18" height="11" rx="1"/><path d="M3 14h18M8 10V6a4 4 0 0 1 8 0v4"/>',
'tool':'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
'floor':'<path d="M3 7h18M3 12h18M3 17h18"/><path d="M8 7v5M15 12v5M11 17v4M17 3v4"/>',
}
def svgi(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
def build(c,out):
    d=dict(c); d.update(I)
    d['NAVLINKS']=''.join(f'<a href="#{h}">{t}</a>' for h,t in [('leistungen','Leistungen'),('sauber',c['NAVSAUBER']),('ablauf','Ablauf'),('arbeiten','Arbeiten'),('fragen','Fragen'),('kontakt','Kontakt')])
    d['TICKS']=''.join(f'<li>{TICK}{t}</li>' for t in c['ticks'])
    d['STATS']=''.join(f'<div class="s"><b>{a}</b><span>{b}</span></div>' for a,b in c['stats'])
    d['CLEANLIST']=''.join(f'<li class="rv">{CHK}<span><b>{a}</b> {b}</span></li>' for a,b in c['clean'])
    d['SERVICES']=''.join(f'<div class="svc rv{" d1" if i%3==1 else " d2" if i%3==2 else ""}"><div class="ic">{svgi(ic)}</div><h3>{h}</h3><p>{p}</p></div>' for i,(ic,h,p) in enumerate(c['services']))
    d['STEPS']=''.join(f'<div class="step rv d{i%3}"><div class="im"><img src="img/{im}" alt="{h}" loading="lazy"></div><span class="n">{i+1}</span><div class="tx"><h3>{h}</h3><p>{p}</p></div></div>' for i,(im,h,p) in enumerate(c['steps']))
    d['GALLERY']=''.join(f'<figure class="rv {cl}"><img src="img/{im}" alt="{t}" loading="lazy"><figcaption><b>{t}</b><span>Beispielbild</span></figcaption></figure>' for im,t,cl in c['gallery'])
    d['FAQ']=''.join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q,a in c['faq'])
    caps=[]
    for i,(ra,rb,k,h,pp,end) in enumerate(c['scaps']):
        row=f'<div class="row"><a class="btn wa" href="#anfrage">{I["I_WA"]}Foto per WhatsApp</a><a class="btn w" href="#anfrage">Angebot anfordern</a></div>' if end else ''
        caps.append(f'<div class="scap{" end" if end else ""}" data-a="{ra}" data-b="{rb}"><span class="k">{k}</span><h2>{h}</h2><p>{pp}</p>{row}</div>')
    d['SCAPS']='\n    '.join(caps)
    d['CHIPS']=', '.join('"'+x+'"' for x in c['chips']); d['CHIP1']=c['chips'][0]
    s=T
    for k,v in d.items():
        if isinstance(v,str): s=s.replace('{{'+k+'}}',v)
    left=re.findall(r'\{\{[A-Z0-9_]+\}\}',s); assert not left,left
    open(out,'w',encoding='utf-8').write(s); print('ok',out,len(s))
