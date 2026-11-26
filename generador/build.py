import os,sys,re,json
sys.path.insert(0,os.path.dirname(__file__))
from plantilla import render,_txt
from paginas import PAGINAS
OUT=os.path.join(os.path.dirname(__file__),'..','publicado')
for p in PAGINAS:
    html=render(p)
    for m in re.findall(r'(?s)application/ld\+json">(.*?)</script>',html): json.loads(m)
    fp=os.path.join(OUT,p['slug'].strip('/'),'index.html'); os.makedirs(os.path.dirname(fp),exist_ok=True)
    open(fp,'w').write(html)
    wc=[len(_txt(s['a']).split()) for s in p['sections']]
    npend=html.count('class="pend"')
    print(f"{p['slug']:34} {len(html):6}b  palabras/respuesta={wc}  pendientes={npend}  title={len(p['title'])} desc={len(p['desc'])}")
