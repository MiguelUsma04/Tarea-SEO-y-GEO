"""Rastreo SEO de crmformeta.com (equivalente básico a Screaming Frog).

Uso: python3 herramientas/rastreo.py > reportes/rastreo-AAAA-MM-DD.md
Recorre las páginas HTML internas desde el home y el sitemap, respeta robots.txt
y revisa: código HTTP, title, meta description, canonical, robots, H1, enlaces
internos rotos, enlaces vacíos y cifras de empresas atendidas.
"""
import re, sys, html, urllib.request, urllib.parse, urllib.robotparser
from collections import defaultdict

BASE = "https://crmformeta.com"
UA = "Mozilla/5.0 (compatible; GmarketingSEOcheck/1.0)"

def get(url, method="GET"):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method=method)
    class NoRedir(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k): return None
    op = urllib.request.build_opener(NoRedir)
    try:
        r = op.open(req, timeout=30)
        return r.status, r.headers, (r.read().decode("utf-8", "replace") if method == "GET" else "")
    except urllib.error.HTTPError as e:
        return e.code, e.headers, ""
    except Exception as e:
        return 0, {}, str(e)

def norm(u, base):
    u = urllib.parse.urljoin(base, u.split("#")[0])
    p = urllib.parse.urlparse(u)
    if p.netloc not in ("crmformeta.com", "www.crmformeta.com"): return None
    return f"https://crmformeta.com{p.path or '/'}"

rp = urllib.robotparser.RobotFileParser()
rp.parse(get(BASE + "/robots.txt")[2].splitlines())  # se lee con UA propio: Cloudflare bloquea el UA de Python
sm = get(BASE + "/sitemap.xml")[2]
cola = [BASE + "/"] + re.findall(r"<loc>([^<]+)</loc>", sm)
vistas, filas, rotos, enlaces_de = set(), [], defaultdict(set), defaultdict(set)
CIFRA = re.compile(r"(?i)(m[aá]s de|\+)\s?(\d{3})\s*(empresas|pymes|casos|clientes|implementaciones)|(\d{3})\+")
while cola:
    u = cola.pop(0)
    if u in vistas: continue
    vistas.add(u)
    if not rp.can_fetch("*", u): continue
    code, hd, body = get(u)
    ct = (hd.get("Content-Type", "") if hd else "")
    if code in (301, 302, 307, 308):
        filas.append(dict(url=u, code=code, nota="redirige a " + hd.get("Location", ""))); continue
    if code != 200 or "html" not in ct:
        if code != 200: filas.append(dict(url=u, code=code, nota="")); continue
        continue
    t = lambda rx: (re.search(rx, body, re.I | re.S) or [None, ""])[1]
    title = html.unescape(t(r"<title>(.*?)</title>").strip())
    desc = html.unescape(t(r'<meta name="description" content="([^"]*)"'))
    canon = t(r'<link rel="canonical" href="([^"]*)"')
    robots = t(r'<meta name="robots" content="([^"]*)"') or (hd.get("X-Robots-Tag", "") if hd else "")
    h1 = len(re.findall(r"<h1[\s>]", body, re.I))
    vacios = len(re.findall(r'<a [^>]*href=""', body))
    texto = re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", body))
    cifras = sorted({m.group(0).strip() for m in CIFRA.finditer(texto)})
    filas.append(dict(url=u, code=code, title=title, desc=desc, canon=canon, robots=robots, h1=h1, vacios=vacios, cifras=cifras))
    for href in re.findall(r'href="([^"]+)"', body):
        if href.startswith(("mailto:", "tel:", "javascript:", "#", "data:")): continue
        n = norm(href, u)
        if not n or re.search(r"\.(css|js|png|jpe?g|webp|gif|ico|svg|pdf|mp4|woff2?|ttf|otf)$", n): continue
        if "/cdn-cgi/" in n: continue  # protección de correos de Cloudflare
        enlaces_de[n].add(u)
        if n not in vistas and rp.can_fetch("*", n) and "noindex" not in robots: cola.append(n)
for n, src in enlaces_de.items():
    c = next((f["code"] for f in filas if f["url"] == n), None)
    if c is None and rp.can_fetch("*", n): c = get(n, "HEAD")[0]
    if c and c >= 400: rotos[n] = src

print("# Rastreo de crmformeta.com\n")
print(f"Páginas revisadas: {len(filas)}\n")
print("| URL | HTTP | Title (largo) | Descripción (largo) | Canonical | Robots | H1 | href vacíos | Cifras |")
print("|---|---|---|---|---|---|---|---|---|")
for f in filas:
    if "title" not in f:
        print(f"| {f['url']} | {f['code']} | {f['nota']} |  |  |  |  |  |  |"); continue
    ok_c = "ok" if f["canon"] == f["url"] else (f["canon"] or "FALTA")
    print(f"| {f['url'].replace(BASE,'')} | {f['code']} | {len(f['title'])} | {len(f['desc']) or 'FALTA'} | {ok_c} | {f['robots'] or '-'} | {f['h1']} | {f['vacios']} | {', '.join(f['cifras']) or '-'} |")
print("\n## Enlaces internos rotos\n")
for n, src in rotos.items():
    print(f"- {n} (desde: {', '.join(sorted(s.replace(BASE,'') for s in src))})")
if not rotos: print("Ninguno.")
