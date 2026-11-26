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
/* Componentes propios de las páginas AEO. El resto (encabezado, hero, contacto, pie,
   botón de WhatsApp, tipografías y colores) viene de /style.css, la hoja del home. */
.gm-card,.gm-answer,.gm-more,.pend,.hero-subtitle{overflow-wrap:anywhere}
.gm-crumbs{font-family:var(--font-regular);font-size:.85rem;color:#a0a0b5;margin-bottom:18px}
.gm-crumbs a{color:var(--color-accent-green)}
.hero-section .main-title{margin-bottom:22px}
.gm-hero-cta{margin-top:30px}
.gm-updated{font-family:var(--font-regular);font-size:.85rem;color:#a0a0b5;margin-top:22px}
.gm-main{background:var(--color-bg-dark);padding:70px 0 40px}
.gm-narrow{max-width:960px}
.gm-card{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);border-radius:25px;box-shadow:0 5px 15px rgba(0,0,0,.2);padding:40px 44px;margin-bottom:30px}
.gm-card h2{font-family:var(--font-bold);font-size:1.7rem;line-height:1.3;color:#fff;margin-bottom:20px}
.gm-answer{background:rgba(3,255,144,.05);border-left:4px solid var(--color-accent-green);border-radius:8px;padding:22px 26px;font-family:var(--font-regular);font-size:1.08rem;line-height:1.7;color:#fff;margin-bottom:18px}
.gm-more{font-family:var(--font-regular);color:#ddd;font-size:1.02rem;line-height:1.7}
.gm-more p{margin:0 0 14px;line-height:1.7}
.gm-more h3{font-family:var(--font-bold);color:var(--color-accent-green);font-size:1.15rem;margin:22px 0 10px}
.gm-more ul,.gm-more ol{padding-left:22px;margin:0 0 14px}
.gm-more ul{list-style:none;padding-left:0}
.gm-more ul li{position:relative;padding-left:28px;margin-bottom:10px}
.gm-more ul li::before{content:"✔";position:absolute;left:0;color:var(--color-accent-green);font-weight:700}
.gm-more ol{list-style:decimal}
.gm-more ol li{margin-bottom:8px;padding-left:4px}
.gm-more ol li::marker{color:var(--color-accent-green);font-family:var(--font-bold)}
.gm-more a,.gm-answer a{color:var(--color-accent-green);text-decoration:underline}
.gm-more strong{color:#fff}
.gm-table-wrap{overflow-x:auto;border-radius:16px;border:1px solid rgba(255,255,255,.15);margin:6px 0 16px}
.gm-table-wrap table{width:100%;border-collapse:collapse;font-family:var(--font-regular)}
.gm-table-wrap th{font-family:var(--font-bold);text-align:left;padding:16px 18px;background:rgba(255,255,255,.08);color:#fff;font-size:1rem}
.gm-table-wrap td{padding:14px 18px;border-top:1px solid rgba(255,255,255,.1);font-size:1rem;color:#fff;vertical-align:top}
.gm-calc{background:rgba(255,255,255,.04);border:1px solid rgba(3,255,144,.25);border-radius:16px;padding:22px 24px;margin:10px 0 18px}
.gm-calc h3{margin-top:0}
.gm-calc .gm-calc-row{display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;margin-bottom:14px}
.gm-calc label{display:flex;flex-direction:column;gap:6px;font-family:var(--font-bold);font-size:.85rem;color:#ccc}
.gm-calc input,.gm-calc select{background:#0c072a;color:#fff;border:1px solid rgba(255,255,255,.2);border-radius:10px;padding:10px 12px;font-family:var(--font-regular);font-size:1rem}
.gm-calc input{width:100px}
.gm-calc .gm-calc-out{font-family:var(--font-bold);color:var(--color-accent-green);font-size:1.15rem;margin-bottom:6px}
.gm-calc .gm-calc-note{font-size:.85rem;color:#a0a0b5;margin:0}
.pend{background:#fff7d1;color:#3a2e00;border:1px dashed #c9a400;border-radius:8px;padding:12px 14px;margin:14px auto;font-family:var(--font-regular);font-size:.92rem;text-align:left;max-width:800px;line-height:1.5}
.pend strong{font-family:var(--font-bold);color:#3a2e00}
.pend ul{list-style:disc;padding-left:20px;margin-top:6px}
.pend li{color:#3a2e00;margin-bottom:4px}
.gm-card .pend{max-width:none}
.gm-draft{background:#ffcc00;color:#000;text-align:center;font-family:var(--font-bold);font-size:.85rem;padding:6px 16px}
.gm-cta{background:var(--color-bg-gradient);padding:70px 0;text-align:center}
.gm-cta p{font-family:var(--font-regular);color:#ccc;font-size:1.1rem;line-height:1.6;max-width:720px;margin:0 auto 30px}
.gm-rel{background:var(--color-bg-dark);padding:60px 0 70px}
.gm-rel-title{font-family:var(--font-bold);font-size:1.6rem;color:#fff;margin-bottom:30px}
.gm-rel-title span{border-bottom:3px solid var(--color-accent-cyan)}
.gm-rel-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}
.gm-rel-grid a{display:flex;justify-content:space-between;align-items:center;gap:12px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-bottom:2px solid rgba(15,170,182,.5);border-radius:12px;padding:20px 24px;font-family:var(--font-bold);color:#fff;transition:.3s}
.gm-rel-grid a:hover{border-color:var(--color-accent-green);transform:translateY(-3px)}
.gm-rel-grid a span{color:var(--color-accent-green);font-size:1.3rem}
@media(min-width:768px){.footer-links-grid{grid-template-columns:1fr 1fr 1fr;max-width:900px;gap:40px}}
@media(max-width:767px){.gm-table-wrap{border:0;overflow:visible}.gm-table-wrap table,.gm-table-wrap tbody,.gm-table-wrap tr,.gm-table-wrap td{display:block;width:100%}.gm-table-wrap tr:first-child{display:none}.gm-table-wrap tr{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:12px 16px;margin-bottom:10px}.gm-table-wrap td{border:0;padding:4px 0}.gm-table-wrap td::before{content:attr(data-label);display:block;font-family:var(--font-bold);font-size:.78rem;color:var(--color-accent-green);text-transform:uppercase;letter-spacing:.03em}.gm-table-wrap td:first-child{font-family:var(--font-bold);font-size:1.05rem}.gm-table-wrap td:first-child::before{display:none}}
@media(max-width:767px){.gm-card{padding:26px 20px;border-radius:18px}.gm-card h2{font-size:1.3rem}.gm-answer{padding:18px;font-size:1rem}.gm-main{padding:40px 0 20px}.gm-cta,.gm-rel{padding:50px 0}}
"""

FOOT_GUIAS = [("/kommo-crm/", "/kommo-crm"), ("/partner-kommo-colombia/", "/partner-kommo-colombia"),
              ("/agente-ia-whatsapp/", "/agente-ia-whatsapp"), ("/whatsapp-multiagente/", "/whatsapp-multiagente"),
              ("/costos_api/", "/costos_api"), ("/privacidad/", "/privacidad"), ("/garantia/", "/garantia")]

SVG_IG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>'
SVG_FB = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/></svg>'
SVG_LI = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/></svg>'

CONTACTO = f"""<section class="contact-section">
  <div class="container">
    <div class="contact-header"><h2 class="contact-title">NUESTRO CONTACTO</h2><div class="contact-line"></div></div>
    <div class="contact-grid">
      <a class="contact-card" href="mailto:comercial@gmarketing.co">
        <div class="contact-icon-top"><img src="/media/iconoemail.webp" alt="Email"></div>
        <div class="contact-text-center"><p>comercial@gmarketing.co</p></div>
      </a>
      <div class="contact-card location-card">
        <div class="contact-icon-top"><img src="/media/iconoplace.webp" alt="Ubicación"></div>
        <div class="contact-text-center">
          <div class="loc-item"><img src="/media/us.png" class="flag" alt="USA"> <strong>Gmarketing USA LLC</strong><br><span class="small-address">Apto 3310, 31 SE 5th St, Miami, FL 33131</span></div>
          <div class="loc-separator"></div>
          <div class="loc-item"><img src="/media/co.png" class="flag" alt="Colombia"> <strong>Gmarketing SAS</strong><br><span class="small-address">Calle 26N # 5AN -50, Cali-Colombia</span></div>
        </div>
      </div>
      <a class="contact-card clickllamar" href="tel:+573216319137">
        <div class="contact-icon-top"><img src="/media/iconotel.webp" alt="Teléfono"></div>
        <div class="contact-text-center"><p>+57 321 6319137</p></div>
      </a>
    </div>
    <div class="social-connect">
      <h3 class="social-title">Síguenos en nuestras redes</h3>
      <div class="social-icons-wrapper">
        <a href="https://www.instagram.com/gmarketing.co/" target="_blank" rel="noopener" class="social-btn instagram" aria-label="Instagram">{SVG_IG}</a>
        <a href="https://www.facebook.com/gmarketing.co/" target="_blank" rel="noopener" class="social-btn facebook" aria-label="Facebook">{SVG_FB}</a>
        <a href="https://www.linkedin.com/company/gmarketing-s-a-s/" target="_blank" rel="noopener" class="social-btn linkedin" aria-label="LinkedIn">{SVG_LI}</a>
      </div>
    </div>
  </div>
</section>"""

PIE = """<footer>
  <div class="container">
    <div class="logo-footer"><img src="/media/logo.png" alt="Gmarketing Logo"></div>
    <div class="copyright">
      © Copyright <span id="year"></span> | Una estrategia de Gmarketing S.A.S
      <a href="https://gmarketing.co/" target="_blank" rel="noopener">www.gmarketing.co</a>
      <div style="margin-top: 15px; font-size: 0.85rem;">
        <a href="/privacidad/" style="color: #aaa; margin-right: 15px; text-decoration: underline;">Política de Privacidad</a>
        <a href="/garantia/" style="color: #aaa; text-decoration: underline;">Política de Garantía</a>
      </div>
    </div>
    <div class="footer-links-grid">
      <div class="footer-column">
        <a href="https://crmformeta.com/" class="hover-button">www.crmformeta.com</a>
        <a href="https://crmformeta.com/kommo10x/" class="hover-button">/kommo10x</a>
        <a href="https://crmformeta.com/kommo10x/agenda/" class="hover-button">/agenda</a>
        <a href="https://crmformeta.com/documentacion/" class="hover-button">/documentacion</a>
        <a href="https://crmformeta.com/#casos" class="hover-button">/casos</a>
      </div>
      <div class="footer-column">
        __GUIAS__
      </div>
      <div class="footer-column">
        <a href="https://www.gmarketing.co/" target="_blank" rel="noopener" class="hover-button">www.gmarketing.co</a>
        <a href="http://amocrm.com.co/" target="_blank" rel="noopener" class="hover-button">www.amocrm.com.co</a>
        <a href="https://www.gmarketing.co/dircomercial/" target="_blank" rel="noopener" class="hover-button">/dircomercial</a>
      </div>
    </div>
  </div>
</footer>
<a class="butchatwhatsapp2" href="https://wa.me/573216319137" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp"><img src="/media/wpp.png" alt="WhatsApp"></a>
<script>document.getElementById('year').textContent=new Date().getFullYear();</script>"""

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

    def tablas(html_):
        import re as _re
        def etiquetar(m):
            t = m.group(0)
            heads = [_re.sub(r"<[^>]+>", "", x).strip() for x in _re.findall(r"<th[^>]*>(.*?)</th>", t, _re.S)]
            def fila(r):
                i = iter(heads)
                return _re.sub(r"<td(?![^>]*data-label)", lambda _: f'<td data-label="{h.escape(next(i, ""))}"', r.group(0))
            return _re.sub(r"<tr>(?:(?!</tr>).)*<td.*?</tr>", fila, t, flags=_re.S)
        html_ = _re.sub(r"<table>.*?</table>", etiquetar, html_, flags=_re.S)
        return html_.replace('<div class="tbl">', '<div class="gm-table-wrap">')

    secs = []
    for s in p["sections"]:
        sid = f' id="{s["id"]}"' if s.get("id") else ""
        more = f'<div class="gm-more">{tablas(s.get("more", ""))}</div>' if s.get("more") else ""
        secs.append(f'<article class="gm-card"{sid}><h2>{s["q"]}</h2><div class="gm-answer">{s["a"]}</div>{more}{pend(s.get("pend"))}</article>')
    rel = ""
    if p.get("related"):
        rel = ('<section class="gm-rel"><div class="container gm-narrow"><h2 class="gm-rel-title">Sigue <span>leyendo</span></h2><div class="gm-rel-grid">'
               + "".join(f'<a href="{u}">{n}<span>+</span></a>' for u, n in p["related"]) + "</div></div></section>")
    crumb_html = " › ".join(f'<a href="{u}">{n}</a>' for n, u in crumbs[:-1]) + f" › {crumbs[-1][0]}"
    robots = '<meta name="robots" content="noindex, nofollow">' if draft else '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">'
    banner = '<div class="gm-draft">BORRADOR · no indexado · revisar los bloques amarillos antes de publicar</div>' if draft else ""
    h1 = p["h1"]
    if p.get("hl") and p["hl"] in h1:
        h1 = h1.replace(p["hl"], f'<span class="highlight-text">{p["hl"]}</span>', 1)
    cta = p.get("cta", ("Revisamos tu operación en una llamada de 20 a 30 minutos y te decimos qué plan de Kommo y qué automatizaciones necesitas.", "Agendar diagnóstico gratuito"))
    guias = "\n        ".join(f'<a href="{u}" class="hover-button">{n}</a>' for u, n in FOOT_GUIAS)

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
  <link rel="stylesheet" href="/style.css">
  <script type="application/ld+json">{ld}</script>
  <style>{CSS}</style>
</head>
<body>
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  {banner}
  <header class="main-header">
    <div class="container"><div class="logo-header-wrapper"><a href="/"><img src="/media/logo.png" alt="Gmarketing, partner de Kommo" class="header-logo"></a></div></div>
    <div class="animated-border-bottom"></div>
  </header>
  <section class="hero-section">
    <div class="container">
      <nav class="gm-crumbs">{crumb_html}</nav>
      <h1 class="main-title">{h1}</h1>
      <p class="hero-subtitle">{p['lead']}</p>
      {pend(p.get('pend_top'))}
      <div class="gm-hero-cta"><a class="btn-neon-solid" href="{AGENDA}">Agendar diagnóstico</a></div>
      <p class="gm-updated">Última actualización: {HOY_TXT}</p>
    </div>
  </section>
  <main class="gm-main"><div class="container gm-narrow">
    {''.join(secs)}
  </div></main>
  <section class="gm-cta"><div class="container">
    <h2 class="section-title">Agenda tu diagnóstico comercial gratuito</h2>
    <p>{cta[0]}</p>
    <a class="btn-neon-solid" href="{AGENDA}">{cta[1]}</a>
  </div></section>
  {rel}
  {CONTACTO}
  {PIE.replace('__GUIAS__', guias)}
</body>
</html>
"""
