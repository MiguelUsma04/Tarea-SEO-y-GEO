import sys,json
def page(slug,title,desc,h1,body,crumb):
    ld={"@context":"https://schema.org","@graph":[
      {"@type":"WebPage","@id":f"https://crmformeta.com/{slug}/#webpage","url":f"https://crmformeta.com/{slug}/","name":title,"description":desc,"inLanguage":"es","dateModified":"2026-11-25","isPartOf":{"@id":"https://crmformeta.com/#website"},"publisher":{"@id":"https://crmformeta.com/#organization"}},
      {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":"https://crmformeta.com/"},{"@type":"ListItem","position":2,"name":crumb,"item":f"https://crmformeta.com/{slug}/"}]}]}
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-TPMR57QR');</script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-R05L91RDJD"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-R05L91RDJD');</script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://crmformeta.com/{slug}/">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_CO">
  <meta property="og:site_name" content="CRMformeta">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://crmformeta.com/{slug}/">
  <meta property="og:image" content="https://crmformeta.com/share.webp">
  <link rel="icon" href="/media/favicon.ico">
  <script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>
  <style>
    @font-face {{ font-family:'monse'; src:url('/fonts/Montserrat-Bold.otf'); }}
    @font-face {{ font-family:'monse4'; src:url('/fonts/Montserrat-Regular.ttf'); }}
    :root {{ --bg:#0e0142; --green:#03FF90; --cyan:#0faab6; --text:#00003e; }}
    * {{ box-sizing:border-box; margin:0; padding:0; }}
    body {{ font-family:'monse4',Arial,sans-serif; background:#f5f6fa; color:var(--text); line-height:1.65; }}
    header {{ background:linear-gradient(180deg,#0c072a,#11026f,#0e0055); padding:18px 16px; }}
    header .wrap {{ display:flex; align-items:center; justify-content:space-between; gap:12px; }}
    header img {{ height:44px; width:auto; }}
    header a.cta {{ background:var(--green); color:var(--bg); font-family:'monse',sans-serif; padding:10px 18px; border-radius:40px; text-decoration:none; font-size:.9rem; white-space:nowrap; }}
    .wrap {{ max-width:860px; margin:0 auto; }}
    main {{ padding:40px 16px 60px; }}
    nav.crumbs {{ font-size:.85rem; margin-bottom:18px; }}
    nav.crumbs a {{ color:var(--cyan); }}
    h1 {{ font-family:'monse',sans-serif; font-size:clamp(1.6rem,4vw,2.3rem); line-height:1.2; margin-bottom:8px; }}
    .updated {{ font-size:.85rem; color:#555; margin-bottom:28px; }}
    h2 {{ font-family:'monse',sans-serif; font-size:1.25rem; margin:30px 0 10px; }}
    p, li {{ margin-bottom:10px; }}
    ul {{ padding-left:22px; }}
    a {{ color:#11026f; }}
    .box {{ background:#fff; border-left:4px solid var(--green); padding:16px 18px; border-radius:6px; margin:16px 0; }}
    @media (max-width:480px) {{ header img {{ height:32px; }} header a.cta {{ padding:8px 12px; font-size:.78rem; }} }}
    footer {{ background:var(--bg); color:#ccc; padding:26px 16px; font-size:.85rem; }}
    footer a {{ color:#fff; margin-right:14px; }}
  </style>
</head>
<body>
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TPMR57QR" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <header><div class="wrap"><a href="/"><img src="/media/logo.png" alt="CRMformeta - Gmarketing"></a><a class="cta" href="/kommo10x/agenda/">Agendar diagnóstico</a></div></header>
  <main><div class="wrap">
    <nav class="crumbs"><a href="/">Inicio</a> › {crumb}</nav>
    <h1>{h1}</h1>
    <p class="updated">Última actualización: 25 de noviembre de 2026</p>
{body}
  </div></main>
  <footer><div class="wrap">
    <p>© Gmarketing S.A.S. · Gmarketing USA LLC · <a href="mailto:comercial@gmarketing.co">comercial@gmarketing.co</a> · +57 321 6319137</p>
    <p style="margin-top:8px"><a href="/">Inicio</a><a href="/kommo10x/">Kommo10X</a><a href="/privacidad/">Política de privacidad</a><a href="/garantia/">Garantía</a></p>
  </div></footer>
</body>
</html>
'''
priv='''    <p>Tenemos un especial cuidado en el tratamiento de los datos. Todo el personal con acceso a datos de carácter personal ha recibido la formación necesaria para mantener la total confidencialidad e integridad de los datos de acuerdo a la ley de protección de datos.</p>
    <h2>¿Quién es responsable de los datos?</h2>
    <div class="box">
      <p><strong>Gmarketing S.A.S.</strong>, Calle 26N # 5AN-50, Cali, Colombia.</p>
      <p><strong>Gmarketing USA LLC</strong>, 31 SE 5th St, Apto 3310, Miami, FL 33131, EE. UU.</p>
      <p>Correo: <a href="mailto:comercial@gmarketing.co">comercial@gmarketing.co</a> · Teléfono y WhatsApp: +57 321 6319137</p>
    </div>
    <h2>¿Cómo consulto, corrijo o elimino mis datos?</h2>
    <p>Escribe a <a href="mailto:comercial@gmarketing.co">comercial@gmarketing.co</a> con tu nombre, el teléfono o correo con el que te registraste y la solicitud: consulta, corrección o eliminación.</p>'''
gar='''    <h2>¿Qué garantiza la implementación Kommo10X?</h2>
    <p>Si después de 35 días, y cumpliendo el CLIENTE con todas sus obligaciones, no se alcanzan las métricas definidas, GMARKETING reembolsará el valor del servicio de implementación Kommo10X. Las métricas son:</p>
    <ul>
      <li>Mejora de la productividad en un 34%.</li>
      <li>Reducción de los tiempos de respuesta a 10 seg a los prospectos.</li>
      <li>Incremento en las ventas conversacionales en un 10%.</li>
    </ul>
    <h2>¿Qué no cubre la garantía?</h2>
    <p>Esta garantía no aplica a licencias de usuarios KOMMO ni a causas atribuibles al cliente.</p>
    <h2>¿Qué costos no están incluidos en la implementación?</h2>
    <ul>
      <li>El setup y la parametrización de agentes avanzados de IA con n8n sí están incluidos; sin embargo, el servicio de IA tiene un costo mensual aproximado de <strong>USD $100/mes</strong>, que cubre hosting, soporte y actualizaciones. Este costo aplica en caso de que se requiera activar IA avanzada.</li>
      <li>El uso de WhatsApp Cloud API (conversaciones, plantillas y difusiones) no está incluido. El cobro se realiza por conversación iniciada cada 24 horas.</li>
    </ul>
    <p>Más detalles en: <a href="https://www.kommo.com/es/precios/" target="_blank" rel="noopener">Calculadora de Precios Kommo</a>.</p>
    <p style="margin-top:28px"><a class="cta" style="background:#03FF90;color:#0e0142;padding:12px 22px;border-radius:40px;text-decoration:none;font-family:monse,sans-serif" href="/kommo10x/agenda/">Agendar diagnóstico gratuito</a></p>'''
o=sys.argv[1] if len(sys.argv)>1 else __import__('os').path.join(__import__('os').path.dirname(__file__),'..','publicado')
open(o+'/privacidad/index.html','w').write(page('privacidad','Política de privacidad | CRMformeta - Gmarketing','Cómo Gmarketing S.A.S. y Gmarketing USA LLC tratan los datos personales que recibe por crmformeta.com y cómo consultarlos, corregirlos o eliminarlos.','Política de privacidad',priv,'Política de privacidad'))
open(o+'/garantia/index.html','w').write(page('garantia','Garantía de la implementación Kommo10X | CRMformeta','Condiciones de la garantía de 35 días de Kommo10X: métricas, reembolso de la implementación y costos no incluidos como IA en n8n y WhatsApp Cloud API.','Garantía de la implementación Kommo10X',gar,'Garantía Kommo10X'))
