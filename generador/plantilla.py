"""Plantilla AEO de crmformeta.com.

Cada página se define como un dict en paginas.py. Este módulo arma el HTML:
encabezado, breadcrumbs, H1, respuesta directa, secciones con pregunta en H2,
bloques PENDIENTE visibles, CTA, pie y schema JSON-LD (WebPage, BreadcrumbList,
FAQPage y Service o Article).

Con draft=True la página sale con <meta name="robots" content="noindex, nofollow">
y una franja de BORRADOR. Para publicar: draft=False, regenerar, subir y agregar
la URL al sitemap.
"""
import json
import html as h

BASE = "https://crmformeta.com"
ORG = {"@id": f"{BASE}/#organization"}
HOY = "2026-11-25"
HOY_TXT = "25 de noviembre de 2026"
GA4 = "G-R05L91RDJD"
GTM = "GTM-TPMR57QR"
AGENDA = "/kommo10x/agenda/"

CSS = """
@font-face{font-family:'monse';src:url('/fonts/Montserrat-Bold.otf');font-display:swap}
@font-face{font-family:'monse2';src:url('/fonts/Montserrat-ExtraBold.otf');font-display:swap}
@font-face{font-family:'monse4';src:url('/fonts/Montserrat-Regular.ttf');font-display:swap}
:root{--bg:#0e0142;--grad:linear-gradient(180deg,#0c072a,#11026f,#0e0055);--green:#03FF90;--cyan:#0faab6;--text:#00003e;--muted:#4b4b6b;--line:#e3e4ee;--paper:#f5f6fa}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'monse4',Arial,sans-serif;background:var(--paper);color:var(--text);line-height:1.65;font-size:17px}
a{color:#11026f}
.wrap{max-width:900px;margin:0 auto;padding:0 16px}
.draft{background:#ffcc00;color:#000;text-align:center;font-family:'monse',sans-serif;font-size:.85rem;padding:6px 16px}
header.top{background:var(--grad)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:14px;padding-bottom:14px}
header.top img{height:42px;width:auto;display:block}
header.top nav{display:flex;gap:18px;align-items:center}
header.top nav a{color:#fff;text-decoration:none;font-family:'monse',sans-serif;font-size:.85rem}
header.top nav a.cta{background:var(--green);color:var(--bg);padding:9px 16px;border-radius:40px;white-space:nowrap}
.hero{background:var(--grad);color:#fff;padding:34px 0 40px}
.crumbs{font-size:.8rem;margin-bottom:14px;color:#c9c6ff}
.crumbs a{color:var(--green)}
h1{font-family:'monse2',sans-serif;font-size:clamp(1.7rem,4.5vw,2.6rem);line-height:1.15;margin-bottom:14px}
.lead{font-size:1.1rem;max-width:760px}
.updated{font-size:.8rem;color:#c9c6ff;margin-top:14px}
main{padding:34px 0 50px}
section.q{background:#fff;border:1px solid var(--line);border-radius:10px;padding:22px 22px 14px;margin-bottom:18px}
h2{font-family:'monse',sans-serif;font-size:1.3rem;line-height:1.3;margin-bottom:10px}
h3{font-family:'monse',sans-serif;font-size:1.05rem;margin:14px 0 6px}
p,li{margin-bottom:10px}
ul,ol{padding-left:22px}
.answer{font-size:1.05rem}
table{width:100%;border-collapse:collapse;margin:8px 0 14px;font-size:.95rem}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:#eef0fb;font-family:'monse',sans-serif}
.tbl{overflow-x:auto}
.pend{background:#fff7d1;color:#3a2e00;border:1px dashed #c9a400;border-radius:8px;padding:12px 14px;margin:10px 0 14px;font-size:.92rem}
.pend strong{font-family:'monse',sans-serif;color:#3a2e00}
.pend li{color:#3a2e00}
.ctabox{background:var(--grad);color:#fff;border-radius:12px;padding:26px 22px;margin-top:26px;text-align:center}
.ctabox p{margin-bottom:16px}
.btn{display:inline-block;background:var(--green);color:var(--bg);font-family:'monse',sans-serif;padding:13px 24px;border-radius:40px;text-decoration:none}
.rel{margin-top:26px}
.rel ul{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px}
.rel li a{display:block;background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px 14px;text-decoration:none}
footer{background:var(--bg);color:#c9c6ff;padding:26px 0;font-size:.85rem}
footer a{color:#fff;margin-right:14px;display:inline-block;margin-bottom:6px}
@media(max-width:640px){header.top nav a:not(.cta){display:none}header.top img{height:32px}header.top nav a.cta{font-size:.78rem;padding:8px 12px}section.q{padding:18px 16px 10px}}
"""

NAV = [("/kommo-crm/", "Kommo CRM"), ("/agente-ia-whatsapp/", "Agente IA"), ("/blog/mejor-crm-whatsapp/", "Guías")]
FOOT = [("/", "Inicio"), ("/kommo-crm/", "Implementación Kommo"), ("/partner-kommo-colombia/", "Partner Kommo Colombia"),
        ("/agente-ia-whatsapp/", "Agente de IA para WhatsApp"), ("/whatsapp-multiagente/", "WhatsApp multiagente"),
        ("/privacidad/", "Privacidad"), ("/garantia/", "Garantía")]


def _txt(s):
    """Quita etiquetas para el texto del schema."""
    import re
    return h.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def render(p):
    url = f"{BASE}{p['slug']}"
    draft = p.get("draft", True)
    kind = p.get("kind", "service")  # service | article
    crumbs = [("Inicio", "/")] + p.get("crumbs", []) + [(p["crumb"], p["slug"])]

    # ---------- schema ----------
    graph = [
        {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": p["title"], "description": p["desc"],
         "inLanguage": "es", "dateModified": HOY, "isPartOf": {"@id": f"{BASE}/#website"}, "publisher": ORG},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{BASE}{u}"} for i, (n, u) in enumerate(crumbs)]},
    ]
    faqs = [(s["q"], s["a"]) for s in p["sections"] if s.get("faq", True)]
    if faqs:
        graph.append({"@type": "FAQPage", "@id": f"{url}#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": _txt(a)}} for q, a in faqs]})
    if kind == "service" and p.get("service"):
        s = p["service"]
        svc = {"@type": "Service", "@id": f"{url}#service", "name": s["name"], "serviceType": s.get("type", s["name"]),
               "description": s["desc"], "provider": ORG, "areaServed": s.get("area", ["CO", "US", "LATAM"]), "url": url}
        if s.get("offers"):
            svc["offers"] = [{"@type": "Offer", "name": o[0], "price": o[1], "priceCurrency": "USD",
                              "description": o[2]} for o in s["offers"]]
        graph.append(svc)
    if kind == "article":
        graph.append({"@type": "Article", "@id": f"{url}#article", "headline": p["h1"], "description": p["desc"],
                      "inLanguage": "es", "datePublished": p.get("published", HOY), "dateModified": HOY,
                      "author": ORG, "publisher": ORG, "mainEntityOfPage": {"@id": f"{url}#webpage"},
                      "image": f"{BASE}/share.webp"})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)

    # ---------- cuerpo ----------
    def pend(items):
        if not items:
            return ""
        lis = "".join(f"<li>{i}</li>" for i in items)
        return f'<div class="pend"><strong>PENDIENTE antes de publicar:</strong><ul>{lis}</ul></div>'

    secs = []
    for s in p["sections"]:
        sid = s.get("id", "")
        sid = f' id="{sid}"' if sid else ""
        secs.append(f'<section class="q"{sid}><h2>{s["q"]}</h2><p class="answer">{s["a"]}</p>{s.get("more", "")}{pend(s.get("pend"))}</section>')
    rel = ""
    if p.get("related"):
        rel = '<div class="rel"><h2>Sigue leyendo</h2><ul>' + "".join(
            f'<li><a href="{u}">{n}</a></li>' for u, n in p["related"]) + "</ul></div>"
    crumb_html = " › ".join(f'<a href="{u}">{n}</a>' for n, u in crumbs[:-1]) + f" › {crumbs[-1][0]}"
    robots = '<meta name="robots" content="noindex, nofollow">' if draft else '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">'
    banner = '<div class="draft">BORRADOR · no indexado · revisar los bloques amarillos antes de publicar</div>' if draft else ""
    nav = "".join(f'<a href="{u}">{n}</a>' for u, n in NAV)
    foot = "".join(f'<a href="{u}">{n}</a>' for u, n in FOOT)
    cta = p.get("cta", ("Revisamos tu operación en una llamada de 20 a 30 minutos y te decimos qué plan de Kommo y qué automatizaciones necesitas.", "Agendar diagnóstico gratuito"))

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM}');</script>
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4}');</script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{h.escape(p['title'])}</title>
  <meta name="description" content="{h.escape(p['desc'])}">
  {robots}
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="{'article' if kind == 'article' else 'website'}">
  <meta property="og:locale" content="es_CO">
  <meta property="og:site_name" content="CRMformeta">
  <meta property="og:title" content="{h.escape(p['title'])}">
  <meta property="og:description" content="{h.escape(p['desc'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}/share.webp">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/media/favicon.ico">
  <script type="application/ld+json">{ld}</script>
  <style>{CSS}</style>
</head>
<body>
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  {banner}
  <header class="top"><div class="wrap"><a href="/"><img src="/media/logo.png" alt="CRMformeta - Gmarketing, partner de Kommo"></a><nav>{nav}<a class="cta" href="{AGENDA}">Agendar diagnóstico</a></nav></div></header>
  <div class="hero"><div class="wrap">
    <nav class="crumbs">{crumb_html}</nav>
    <h1>{p['h1']}</h1>
    <p class="lead">{p['lead']}</p>
    {pend(p.get('pend_top'))}
    <p class="updated">Última actualización: {HOY_TXT}</p>
  </div></div>
  <main><div class="wrap">
    {''.join(secs)}
    <div class="ctabox"><p>{cta[0]}</p><a class="btn" href="{AGENDA}">{cta[1]}</a></div>
    {rel}
  </div></main>
  <footer><div class="wrap">
    <p>{foot}</p>
    <p style="margin-top:8px">© Gmarketing S.A.S. (Cali) · Gmarketing USA LLC (Miami) · <a href="mailto:comercial@gmarketing.co">comercial@gmarketing.co</a> · +57 321 6319137</p>
  </div></footer>
</body>
</html>
"""
