"""Erzeugt ../en/index.html (englische Startseite unter allrich-webdesign.com/en/) aus allrich/index.html.
Nach jeder Änderung an allrich/index.html neu ausführen: python3 allrich/build-en.py
Jeder deutsche Text, der übersetzt werden soll, steht unten in T. Fehlt ein Treffer, bricht das Skript ab."""
import pathlib, re
here = pathlib.Path(__file__).parent
s = (here / "index.html").read_text()

T = [
# head
('<html lang="de">', '<html lang="en">'),
('<title>ALLRICH WEBDESIGN · Potsdam</title>', '<title>ALLRICH WEBDESIGN · Websites with scroll film</title>'),
('<meta property="og:title" content="ALLRICH WEBDESIGN · Potsdam">', '<meta property="og:title" content="ALLRICH WEBDESIGN · Websites with scroll film">'),
('Websites mit Scroll-Film: eigenes Design, top auf dem Handy, bei Google gut zu finden. Dazu KI-Assistent und Hosting. Kostenloser Entwurf, ab 990 €.',
 'Websites with a scroll film: custom design, perfect on mobile, easy to find on Google. Plus AI assistant and hosting. Free draft, from €990.'),
('<link rel="canonical" href="https://allrich-webdesign.com/">', '<link rel="canonical" href="https://allrich-webdesign.com/en/">'),
('<span lang="en">This page is also available in English.</span> <a href="/en/" hreflang="en" lang="en">Switch to English →</a>', ''),
('<meta property="og:locale" content="de_DE">', '<meta property="og:locale" content="en_GB">'),
('<meta property="og:url" content="https://allrich-webdesign.com/">', '<meta property="og:url" content="https://allrich-webdesign.com/en/">'),
# header / nav
('aria-label="Allrich Webdesign, zur Startseite"', 'aria-label="Allrich Webdesign, home"'),
('aria-label="Hauptnavigation"', 'aria-label="Main navigation"'),
('<a href="#arbeiten">Arbeiten</a><a href="#ueber">Über mich</a><a href="#ablauf">Ablauf</a><a href="#preis">Preis</a><a href="#fragen" data-qa>Fragen</a>',
 '<a href="#arbeiten">Work</a><a href="#ueber">About</a><a href="#ablauf">Process</a><a href="#preis">Pricing</a><a href="#fragen" data-qa>Questions</a>'),
('<a href="#kontakt">Kontakt</a>', '<a href="#kontakt">Contact</a>'),
('Kostenlosen Entwurf anfragen', 'Request a free draft'),
('aria-label="Menü öffnen"', 'aria-label="Open menu"'),
('aria-label="Menü schließen"', 'aria-label="Close menu"'),
# hero / trust
('aria-label="Einleitung"', 'aria-label="Introduction"'),
('<h1>Websites, die bleiben.</h1>', '<h1>Websites that stay with you.</h1>'),
('aria-label="Auf einen Blick"', 'aria-label="At a glance"'),
('<div><b><em>0 €</em> Entwurf</b><span>Sie sehen Ihre Seite, bevor Sie sich entscheiden</span></div>',
 '<div><b><em>€0</em> draft</b><span>See your site before you decide</span></div>'),
('<div><b>ab 990 €</b><span>für die komplette Website, einmalig</span></div>', '<div><b>from €990</b><span>for the complete website, one-off</span></div>'),
('<div><b>1 Kontakt</b><span>von der ersten Idee bis zum Livegang</span></div>', '<div><b>1 contact</b><span>from the first idea to launch</span></div>'),
('<div><b>Jede Branche</b><span>vom Makler bis zum Café</span></div>', '<div><b>Any industry</b><span>from estate agents to cafés</span></div>'),
# work
('<p class="kicker">Arbeiten</p><h2 class="h h2">So fühlt sich<br>das <em>an.</em></h2>', '<p class="kicker">Work</p><h2 class="h h2">This is how<br>it <em>feels.</em></h2>'),
('Zwei Konzeptseiten aus verschiedenen Branchen. Öffnen Sie sie am besten auf dem Handy und scrollen Sie langsam.',
 'Two concept sites from different industries. Best opened on your phone, then scroll slowly.'),
('alt="Blick in eine moderne Villa mit offener Treppe"', 'alt="View into a modern villa with an open staircase"'),
('<span class="tag">Immobilien · Scroll-Film</span>', '<span class="tag">Real estate · Scroll film</span>'),
('Beim Scrollen fliegt man wie eine Drohne durch eine Villa am Meer.', 'As you scroll, you fly like a drone through a villa by the sea.'),
('alt="Iced Latte mit Milch, die sich im Glas verteilt"', 'alt="Iced latte with milk swirling in the glass"'),
('<span class="tag">Gastronomie · Scroll-Film</span>', '<span class="tag">Food &amp; drink · Scroll film</span>'),
('Ein Iced Latte entsteht Schicht für Schicht.', 'An iced latte comes together layer by layer.'),
('>Als Nächstes</span>', '>Up next</span>'),
('<h3>Ihre Branche</h3><p>Schicken Sie mir Ihre Website-Adresse. Sie erhalten einen kostenlosen Entwurf mit Ihren Inhalten.</p>',
 '<h3>Your business</h3><p>Send me your website address. You get a free draft with your own content.</p>'),
('Velaro und Milla sind Beispielmarken zur Veranschaulichung.', 'Velaro and Milla are example brands for illustration.'),
# sectors
('<p class="kicker">Für jede Branche</p><h2 class="h h2">Was Sie zeigen,<br>wird <em>Bewegung.</em></h2>',
 '<p class="kicker">For every industry</p><h2 class="h h2">What you show<br>comes <em>alive.</em></h2>'),
('Ein Flug durch das Objekt, ein Gericht, das entsteht, ein Werkstück, das Form annimmt: Jede Branche bekommt ihren eigenen Film und ihre eigenen Farben.',
 'A flight through a property, a dish being made, a workpiece taking shape: every industry gets its own film and its own colours.'),
('<span class="b">Immobilien</span><span>Hausverwaltung</span><span>Architektur</span><span>Bauträger</span><span>Handwerk</span><span>Gastronomie</span><span>Cafés</span><span>Hotels</span><span>Ferienwohnungen</span><span>Autohäuser</span><span>Praxen</span><span>Kanzleien</span><span>Garten- und Landschaftsbau</span><span>Sanitär und Heizung</span><span>Friseure</span><span>Fitness</span><span>Einzelhandel</span><span>und mehr</span>',
 '<span class="b">Real estate</span><span>Property management</span><span>Architecture</span><span>Developers</span><span>Trades</span><span>Restaurants</span><span>Cafés</span><span>Hotels</span><span>Holiday homes</span><span>Car dealers</span><span>Clinics</span><span>Law firms</span><span>Landscaping</span><span>Plumbing and heating</span><span>Hair salons</span><span>Fitness</span><span>Retail</span><span>and more</span>'),
# about
('<p class="kicker">Über mich</p>', '<p class="kicker">About me</p>'),
('<h2 class="h h2">Ein Ansprech&shy;partner. <em>Von A bis Z.</em></h2>', '<h2 class="h h2">One contact. <em>From A to Z.</em></h2>'),
('Hinter Allrich Webdesign stehe ich, Peter Allrich aus Potsdam. Ich gestalte und programmiere jede Website selbst, vom ersten Entwurf bis zum Livegang. Sie schreiben nicht mit einer Agentur oder einem Callcenter, sondern direkt mit mir.',
 'I am Peter Allrich from Potsdam, Germany, the person behind Allrich Webdesign. I design and code every website myself, from the first draft to launch. You never deal with an agency or a call centre, only with me.'),
('Mein Schwerpunkt sind Websites, die mit Bewegung erzählen: Ein Film läuft beim Scrollen und zeigt Ihr Objekt, Ihr Produkt oder Ihren Betrieb so, wie Fotos allein es nicht können.',
 'I specialise in websites that tell a story through motion: a film plays as you scroll and shows your property, product or business in a way photos alone cannot.'),
('<li>Persönliche Antwort, in der Regel am selben Tag</li>', '<li>Personal reply, usually the same day</li>'),
('<li>Erst der kostenlose Entwurf, dann Ihre Entscheidung</li>', '<li>Free draft first, then your decision</li>'),
('<li>Klare Preise, schriftlich vorab</li>', '<li>Clear prices, in writing up front</li>'),
('<dt>Unternehmen</dt>', '<dt>Business</dt>'),
('<dt>Größe</dt><dd>Einzelunternehmen, eine Person. Sie haben immer denselben Ansprechpartner.</dd>',
 '<dt>Size</dt><dd>Sole trader, one person. You always talk to the same person.</dd>'),
('<dt>Standort</dt><dd>Potsdam</dd>', '<dt>Location</dt><dd>Potsdam, Germany</dd>'),
('<dt>Arbeitsgebiet</dt><dd>Deutschland und Österreich. Alles läuft bequem per E-Mail und Telefon, ein Termin vor Ort ist nicht nötig.</dd>',
 '<dt>Area</dt><dd>Germany, Austria and remote worldwide. Everything runs by email, phone or video call, no on-site meeting needed.</dd>'),
('<dt>Schwerpunkt</dt><dd>Websites mit Scroll-Film für Immobilien, Architektur, Hausverwaltung, Handwerk und Gastronomie</dd>',
 '<dt>Focus</dt><dd>Websites with a scroll film for real estate, architecture, property management, trades and hospitality</dd>'),
('<dt>Technik</dt><dd>Kein Baukasten: selbst programmiert, schnell geladen, zuerst für das Handy gestaltet</dd>',
 '<dt>Technology</dt><dd>No website builder: hand-coded, fast to load, designed mobile-first</dd>'),
('<dt>Kontakt</dt>', '<dt>Contact</dt>'),
('<a href="tel:+491712269877">0171 2269877</a></dd>', '<a href="tel:+491712269877">+49 171 2269877</a></dd>'),
# process
('<p class="kicker">Ablauf</p><h2 class="h h2">In vier Schritten<br><em>online.</em></h2>', '<p class="kicker">Process</p><h2 class="h h2">Online in<br><em>four steps.</em></h2>'),
('Sie liefern Ihr Material oder Ihre Ideen. Ich kümmere mich um den Rest.', 'You provide your material or ideas. I take care of the rest.'),
('<h3>Anfrage</h3><p>Sie schicken mir Ihre bisherige Website oder ein paar Sätze zu Ihrem Betrieb.</p>', '<h3>Request</h3><p>Send me your current website or a few lines about your business.</p>'),
('<h3>Gratis-Entwurf</h3><p>Sie erhalten einen persönlichen Entwurf zum Anklicken, kostenlos und unverbindlich.</p>', '<h3>Free draft</h3><p>You get a personal, clickable draft, free and with no obligation.</p>'),
('<h3>Ihr Material</h3><p>Fotos, Videos und Texte von Ihnen. Was fehlt, ergänzen wir gemeinsam.</p>', '<h3>Your material</h3><p>Your photos, videos and texts. Anything missing, we add together.</p>'),
('<h3>Livegang</h3><p>Nach Ihrer Freigabe geht die Website unter Ihrer Domain online.</p>', '<h3>Launch</h3><p>Once you approve, the website goes live on your domain.</p>'),
# pricing
('<p class="kicker">Preis</p><h2 class="h h2">Klar kalkuliert.<br><em>Ohne Überraschung.</em></h2>', '<p class="kicker">Pricing</p><h2 class="h h2">Clear pricing.<br><em>No surprises.</em></h2>'),
('Sie wissen vorher, was Ihre Website kostet. Zwei feste Pakete, größere Projekte biete ich individuell an.', 'You know the cost before we start. Two fixed packages, larger projects quoted individually.'),
('<p class="amt">990 €<small>einmalig</small></p>', '<p class="amt">€990<small>one-off</small></p>'),
('Die komplette Website. Das genaue Angebot erhalten Sie vorab schriftlich.', 'The complete website. You get the exact quote in writing up front.'),
('<li>Ein Scroll-Film aus Ihrem Material</li>', '<li>One scroll film made from your material</li>'),
('<li>Eigenes Design in Ihren Farben</li>', '<li>Custom design in your colours</li>'),
('<li>Optimiert für Handy, Tablet und Computer</li>', '<li>Optimised for phone, tablet and desktop</li>'),
('<li>Kontaktformular, Anfahrt, Impressum und Datenschutzseite</li>', '<li>Contact form, directions, legal notice and privacy page</li>'),
('<li>Für Google optimiert, damit Kunden Sie finden</li>', '<li>Optimised for Google so customers find you</li>'),
('<li>Abstimmung, bis Sie zufrieden sind</li>', '<li>Revisions until you are happy</li>'),
('<span class="badge">Empfehlung</span>', '<span class="badge">Recommended</span>'),
('<p class="amt">1.490 €<small>einmalig</small></p>', '<p class="amt">€1,490<small>one-off</small></p>'),
('Für einen besonders hochwertigen Auftritt mit mehr Bewegung und mehr Inhalt.', 'For a premium presence with more motion and more content.'),
('<li class="all">Alles aus Start, dazu:</li>', '<li class="all">Everything in Start, plus:</li>'),
('<b>Ihr Name im Film.</b> Ihr Logo oder Schriftzug wird Teil der Szene, so wie ALLRICH auf meiner Seite.', '<b>Your name in the film.</b> Your logo or lettering becomes part of the scene, like ALLRICH on my site.'),
('<b>Bis zu drei Scroll-Filme.</b> Jedes wichtige Objekt, Projekt oder jeder Raum bekommt seinen eigenen Film.', '<b>Up to three scroll films.</b> Every key property, project or room gets its own film.'),
('<b>Eigene Projektseiten.</b> Jedes Projekt mit Galerie, Kennzahlen und Lage, statt einer Liste.', '<b>Project pages.</b> Each project with gallery, key figures and location, instead of a list.'),
('<b>Interaktive Extras.</b> Zum Beispiel 3D-Ansicht, Vorher-nachher-Regler oder ein Rechner für Ihre Kunden.', '<b>Interactive extras.</b> For example a 3D view, a before-and-after slider or a calculator for your customers.'),
('<b>Texte aus einer Hand.</b> Ich schreibe alle Inhalte, zugeschnitten auf Ihre Kunden.', '<b>Copywriting included.</b> I write all the content, tailored to your customers.'),
('<b>Ihr Google-Profil.</b> Ich richte Ihren Eintrag bei Google und Google Maps ein, mit Bildern, Leistungen und Öffnungszeiten.', '<b>Your Google profile.</b> I set up your Google and Google Maps listing with photos, services and opening hours.'),
('<b>Vorrang.</b> Ihr Projekt wird vor allen anderen umgesetzt.', '<b>Priority.</b> Your project comes first.'),
('<b>3 Monate Hosting und Pflege gratis.</b> Ich kümmere mich nach dem Start um Ihre Seite und helfe bei Änderungen, ohne Kosten.', '<b>3 months of hosting and care free.</b> After launch I look after your site and help with changes at no cost.'),
('<p class="lbl">Hosting und Pflege</p>', '<p class="lbl">Hosting and care</p>'),
('aria-label="Abrechnung"', 'aria-label="Billing"'),
('>Monatlich</button>', '>Monthly</button>'),
('>Jährlich <i>−17 %</i></button>', '>Yearly <i>−17%</i></button>'),
('<s class="old" aria-label="statt 39 €">39 €</s>', '<s class="old" aria-label="instead of €39">€39</s>'),
('<b class="py">32,50 €</b><b class="pm">39 €</b>', '<b class="py">€32.50</b><b class="pm">€39</b>'),
('<span class="py">/Monat, jährliche<br>Abrechnung</span><span class="pm">/Monat,<br>monatlich kündbar</span>', '<span class="py">/month, billed<br>yearly</span><span class="pm">/month,<br>cancel monthly</span>'),
('<span class="py">Jährlich buchen</span><span class="pm">Monatlich buchen</span><span class="hdisc py">−17 %<em></em>Spare 78 €</span>', '<span class="py">Book yearly</span><span class="pm">Book monthly</span><span class="hdisc py">−17%<em></em>Save €78</span>'),
('<span class="py">390 € pro Jahr statt 468 €. Optional.</span><span class="pm">Optional. Jährlich sparen Sie 78 €.</span>', '<span class="py">€390 per year instead of €468. Optional.</span><span class="pm">Optional. Save €78 with yearly billing.</span>'),
('<li>Hosting und Domain inklusive</li>', '<li>Hosting and domain included</li>'),
('<li>Kleine Änderungen an Texten und Bildern</li>', '<li>Small changes to texts and images</li>'),
('<li>Ihre Seite bleibt schnell und erreichbar</li>', '<li>Your site stays fast and online</li>'),
('>KI-Assistent fragen</a>', '>Ask the AI assistant</a>'),
# extras
('<summary class="xbtn">Extras ansehen<span class="xplus">+</span></summary>', '<summary class="xbtn">See extras<span class="xplus">+</span></summary>'),
('<p class="xs">Zu jedem Paket dazubuchbar.</p>', '<p class="xs">Can be added to any package.</p>'),
('<h3>Ihr eigener KI-Assistent</h3>', '<h3>Your own AI assistant</h3>'),
('Ein Chat auf Ihrer Website, der Kundenfragen rund um die Uhr beantwortet: zu Leistungen, Preisen, Öffnungszeiten und Anfahrt. Er kennt nur Ihre Angaben und verweist sonst an Sie. So wie der Assistent hier auf meiner Seite.',
 'A chat on your website that answers customer questions around the clock: services, prices, opening hours and directions. It only knows your information and refers everything else to you. Just like the assistant on this site.'),
('<p class="amt">95 €<small>einmalig</small></p>', '<p class="amt">€95<small>one-off</small></p>'),
('<h3>Weitere Sprachen</h3>', '<h3>More languages</h3>'),
('Ihre Website zusätzlich auf Englisch, Polnisch oder in einer anderen Sprache. Mit KI übersetzt und von mir geprüft. Ihr KI-Assistent antwortet dann automatisch in der Sprache Ihrer Besucher.',
 'Your website also in English, Polish or any other language. Translated with AI and checked by me. Your AI assistant then automatically replies in your visitors\' language.'),
('<p class="amt">149 €<small>pro Sprache</small></p>', '<p class="amt">€149<small>per language</small></p>'),
('<h3>Monatlicher Beitrag</h3>', '<h3>Monthly post</h3>'),
('Jeden Monat ein neuer Beitrag auf Ihrer Website, zum Beispiel ein neues Objekt, ein Projekt oder ein Angebot. Auf Wunsch auch in Ihrem Google-Profil. Das hält Ihre Seite aktuell und hilft bei Google.',
 'A new post on your website every month, for example a new property, a project or an offer. On request also on your Google profile. Keeps your site fresh and helps on Google.'),
('<p class="amt">39 €<small>pro Monat</small></p>', '<p class="amt">€39<small>per month</small></p>'),
# contact
('<p class="kicker">Kontakt</p>', '<p class="kicker">Contact</p>'),
('<h2 class="h h2">Ihr Entwurf.<br><em>Kostenlos.</em></h2>', '<h2 class="h h2">Your draft.<br><em>Free.</em></h2>'),
('Schreiben Sie mir kurz, worum es geht, gern mit der Adresse Ihrer bisherigen Website. Sie erhalten eine persönliche Antwort.',
 'Tell me briefly what you need, ideally with your current website address. You will get a personal reply. I reply in English or German.'),
('>Anrufen: 0171 2269877</a>', '>Call: +49 171 2269877</a>'),
('text=Hallo%20Herr%20Allrich%2C%20ich%20komme%20von%20Ihrer%20Website%20allrich-webdesign.com%20und%20interessiere%20mich%20f%C3%BCr%20eine%20Website.',
 'text=Hello%20Peter%2C%20I%20found%20you%20on%20allrich-webdesign.com%20and%20I%27m%20interested%20in%20a%20website.'),
('>WhatsApp schreiben</a>', '>Message on WhatsApp</a>'),
('placeholder="Vor- und Nachname"', 'placeholder="First and last name"'),
('<label for="fMail">E-Mail</label>', '<label for="fMail">Email</label>'),
('placeholder="name@firma.de"', 'placeholder="name@company.com"'),
('<label for="fTel">Telefon (optional)</label>', '<label for="fTel">Phone (optional)</label>'),
('placeholder="Für einen kurzen Rückruf"', 'placeholder="For a quick call back"'),
('<label for="fFirm">Unternehmen und Website</label>', '<label for="fFirm">Company and website</label>'),
('placeholder="z. B. Muster GmbH, muster.de"', 'placeholder="e.g. Example Ltd, example.com"'),
('<label for="fType">Branche</label><select id="fType"><option>Immobilien</option><option>Hausverwaltung</option><option>Architektur</option><option>Handwerk</option><option>Gastronomie</option><option>Hotel oder Ferienwohnung</option><option>Praxis oder Kanzlei</option><option>Andere Branche</option></select>',
 '<label for="fType">Industry</label><select id="fType"><option>Real estate</option><option>Property management</option><option>Architecture</option><option>Trades</option><option>Restaurant or café</option><option>Hotel or holiday home</option><option>Clinic or law firm</option><option>Other</option></select>'),
('<label for="fMsg">Ihr Anliegen</label>', '<label for="fMsg">Your request</label>'),
('placeholder="Was soll Ihre neue Website zeigen?"', 'placeholder="What should your new website show?"'),
('<label for="fHp">Bitte leer lassen</label>', '<label for="fHp">Please leave empty</label>'),
('Anfrage senden <span class="arr">→</span>', 'Send request <span class="arr">→</span>'),
('Vielen Dank! Ihre Anfrage ist angekommen. Ich melde mich persönlich innerhalb eines Werktags.', 'Thank you! Your request has arrived. I will get back to you personally within one working day.'),
('Ihre Angaben werden nur verwendet, um Ihre Anfrage zu beantworten. Mehr dazu in der <a href="datenschutz.html">Datenschutzerklärung</a>.',
 'Your details are only used to answer your request. More in the <a href="datenschutz.html">privacy policy</a> (German).'),
('"Bitte geben Sie Ihren Namen ein."', '"Please enter your name."'),
('"Bitte geben Sie eine gültige E-Mail-Adresse ein, damit ich antworten kann."', '"Please enter a valid email address so I can reply."'),
('"Bitte beschreiben Sie kurz Ihr Anliegen."', '"Please briefly describe your request."'),
('"Das Senden hat gerade nicht geklappt. Ihr E-Mail-Programm öffnet sich stattdessen mit Ihrer Anfrage."', '"Sending did not work just now. Your email app will open with your request instead."'),
('encodeURIComponent("Website-Anfrage: "', 'encodeURIComponent("Website request (EN): "'),
# footer
('aria-label="Rechtliches"><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a>',
 'aria-label="Legal"><a href="impressum.html">Legal notice</a><a href="datenschutz.html">Privacy</a>'),
# chat
('<i></i>Fragen?<span class="qa-l"> KI-Assistent</span>', '<i></i>Questions?<span class="qa-l"> AI assistant</span>'),
('aria-label="KI-Assistent">', 'aria-label="AI assistant">'),
('<div class="qa-hd"><div>KI-Assistent<small>', '<div class="qa-hd"><div>AI assistant<small>'),
('aria-label="Schließen">×</button>', 'aria-label="Close">×</button>'),
('placeholder="Ihre Frage …" aria-label="Ihre Frage"', 'placeholder="Your question …" aria-label="Your question"'),
('aria-label="Senden">', 'aria-label="Send">'),
("msg('Hallo! Ich bin der KI-Assistent von Allrich Webdesign. Fragen Sie mich alles zu unseren Websites mit Scroll-Film, zu Preisen oder zum Ablauf.')",
 "msg('Hello! I am the AI assistant of Allrich Webdesign. Ask me anything about our scroll-film websites, prices or the process. I reply in your language.')"),
("'KI-Antworten können Fehler enthalten. Bitte keine persönlichen Daten eingeben. <a href=\"datenschutz.html\">Datenschutz</a>'",
 "'AI answers can contain mistakes. Please do not enter personal data. <a href=\"datenschutz.html\">Privacy</a>'"),
("cur.textContent='Einen Moment, ich denke nach …'", "cur.textContent='One moment, thinking …'"),
("msg('Schreibt …','dots')", "msg('Typing …','dots')"),
("'Entschuldigung, ich bin gerade nicht erreichbar. Bitte versuchen Sie es gleich noch einmal oder fragen Sie Peter direkt: <a href=\"tel:+491712269877\">0171 2269877</a> (auch WhatsApp) oder über das <a href=\"#kontakt\">Formular</a>.'",
 "'Sorry, I am not available right now. Please try again shortly or ask Peter directly: <a href=\"tel:+491712269877\">+49 171 2269877</a> (also WhatsApp) or via the <a href=\"#kontakt\">form</a>.'"),
("hist.push({role:'user',content:q});", "hist.push({role:'user',content:(hist.length?'':'[Answer in English unless I write in another language] ')+q});"),
]

missing = []
for de, en in T:
    if de not in s:
        missing.append(de[:80])
    s = s.replace(de, en)
if missing:
    raise SystemExit("Nicht gefunden:\n" + "\n".join(missing))

# German page switcher -> English page switcher (the language link block is inserted by add_lang())
s = s.replace('<a class="lang" href="/en/" hreflang="en" lang="en">EN</a>', '<a class="lang" href="/" hreflang="de" lang="de">DE</a>')
s = s.replace('<div class="langhint" id="langhint" hidden>', '<div class="langhint" id="langhint" hidden data-off>')

# paths: page lives at /en/, assets stay in /allrich/
s = s.replace('"../', '"/')
for a in ["fonts/", "film/", "img-", "impressum.html", "datenschutz.html"]:
    s = s.replace('"' + a, '"/allrich/' + a).replace("url(" + a, "url(/allrich/" + a)
s = s.replace("<!doctype html>", "<!doctype html>\n<!-- generiert aus allrich/index.html mit allrich/build-en.py -->", 1)

# leftovers check: common German words that should not remain in visible text
body = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
left = [w for w in [" und ", " Ihre ", " für ", " Sie ", "Kostenlos", "Entwurf"] if w in re.sub(r"<[^>]+>", " ", body)]
out = here.parent / "en" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(s)
print("en/index.html geschrieben", "| deutsche Reste:", left or "keine")
