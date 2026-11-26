"""Contenido de los borradores de prioridad 1 (pestaña 'Google orgánico (SEO)' del estudio).

Regla: solo datos ya publicados en crmformeta.com o en el estudio de keywords.
Todo lo demás va en 'pend' (bloque amarillo visible) para Carlos.
"""

CIFRA = "Cifra única de empresas atendidas: el Excel propone «Gold Partner de Kommo desde 2020» y «+260 implementaciones». Hoy el sitio dice 250, 500, 260, 200, 400 y 150, y /kommo10x/ dice «desde 2014». Carlos define una sola."

LICENCIAS_TABLA = """<div class="tbl"><table>
<tr><th>Plan</th><th>Precio desde</th><th>Para quién</th><th>Incluye</th></tr>
<tr><td>Básico</td><td>USD 20 por usuario al mes</td><td>Equipos pequeños y operaciones simples</td><td>Embudo de ventas, integraciones de mensajería, correo, chat en vivo, REST-API y webhooks</td></tr>
<tr><td>Avanzado</td><td>USD 30 por usuario al mes</td><td>Equipos que necesitan automatización y ventas conversacionales</td><td>Todo lo del Básico, más Salesbot, automatizaciones avanzadas, KPIs, pronósticos y análisis de llamadas</td></tr>
<tr><td>Pro</td><td>USD 45 por usuario al mes</td><td>Alto volumen, varios canales, IA avanzada, reservas y medición de ROI</td><td>Todo lo del Avanzado, más lead scoring, copias de seguridad, seguimiento de actividad y soporte prioritario</td></tr>
<tr><td>Empresarial</td><td>Cotización</td><td>Operaciones de alto volumen con necesidades a la medida</td><td>Límites ampliados, más almacenamiento, soporte dedicado y SLA</td></tr>
</table></div><p>Compra mínima de 6 meses en todos los planes.</p>"""

# Calculadora de licencias: asesores × plan × meses. Precios = tabla LICENCIAS_TABLA.
CALC_ASESORES = """<div class="gm-calc" id="calc-asesores">
<h3>Calcula las licencias de tu equipo</h3>
<div class="gm-calc-row">
<label>Asesores <input id="ca-n" type="number" min="1" max="200" value="5"></label>
<label>Plan <select id="ca-p"><option value="20">Básico (USD 20)</option><option value="30" selected>Avanzado (USD 30)</option><option value="45">Pro (USD 45)</option></select></label>
<label>Meses <select id="ca-m"><option value="6">6</option><option value="8">8</option><option value="10">10</option><option value="12" selected>12</option><option value="18">18</option></select></label>
</div>
<p class="gm-calc-out" id="ca-out"></p>
<p class="gm-calc-note">Precio de lista de Kommo por usuario al mes, compra mínima de 6 meses. No incluye mensajes de WhatsApp API ni implementación.</p>
<script>(function(){var n=document.getElementById('ca-n'),p=document.getElementById('ca-p'),m=document.getElementById('ca-m'),o=document.getElementById('ca-out');
function f(x){return 'USD '+x.toLocaleString('es-CO')}
function c(){var a=Math.max(1,parseInt(n.value||1,10)),pr=+p.value,me=+m.value,mes=a*pr;o.textContent=a+' asesores en '+p.options[p.selectedIndex].text.split(' (')[0]+': '+f(mes)+' al mes · '+f(mes*me)+' por '+me+' meses.'}
[n,p,m].forEach(function(e){e.addEventListener('input',c)});c();})();</script>
</div>"""

PAGINAS = [
# ------------------------------------------------------------------ 1
{
 "slug": "/kommo-crm/", "hl": "Kommo CRM", "crumb": "Implementación de Kommo CRM", "kind": "service",
 "title": "Implementación de Kommo CRM: precio, tiempos y qué incluye | Gmarketing",
 "desc": "La implementación Kommo10X cuesta USD 1.500, dura 35 días e incluye embudos, WhatsApp API, 3 agentes de IA en n8n, manuales y acompañamiento semanal.",
 "h1": "Implementación de Kommo CRM: precio, tiempos y qué incluye",
 "lead": "Gmarketing implementa Kommo CRM en 35 días para equipos comerciales de 3 a 20 vendedores con la metodología Kommo10X. El proyecto cuesta USD 1.500 y se paga en dos partes: 50% al iniciar y 50% el día 35, solo si se cumplen las métricas de la garantía.",
 "pend_top": ["Carlos: confirmar que USD 1.500, la IA incluida (valor de referencia USD 1.200) y las «3 plazas» siguen vigentes."],
 "service": {"name": "Kommo10X: implementación de Kommo CRM", "type": "Implementación de CRM",
             "desc": "Implementación de Kommo CRM en 35 días: diagnóstico comercial, embudos, integración de WhatsApp, Instagram, Facebook y formularios, 3 agentes de IA en n8n, manuales y acompañamiento semanal.",
             "offers": [("Implementación Kommo10X", "1500", "50% al iniciar y 50% el día 35 si se cumplen las métricas de la garantía.")]},
 "sections": [
  {"q": "¿Cuánto cuesta implementar Kommo CRM?", "id": "precio",
   "a": "La implementación Kommo10X cuesta USD 1.500: 50% al iniciar y 50% el día 35, solo si se logran los resultados. Incluye la configuración de 3 agentes de IA, con valor de referencia de USD 1.200. Aparte se pagan las licencias de Kommo, desde USD 20 por usuario al mes, y el servidor de IA, cerca de USD 100 al mes.",
   "more": "<h3>Costos que no están incluidos</h3><ul><li>Licencias de Kommo, que se pagan a Kommo (ver tabla de planes abajo).</li><li>Infraestructura VPS para los agentes de IA: aproximadamente USD 100 al mes.</li><li>Mensajes de WhatsApp Business API, que Meta cobra por mensaje entregado.</li></ul>"},
  {"q": "¿Qué incluye la implementación Kommo10X?",
   "a": "La implementación incluye cuatro entregables: el sistema comercial armado (diagrama de flujo, embudos y tableros), 3 agentes de IA de respuesta, seguimiento y reactivación conectados por n8n, manuales de uso y guías de chat para el equipo, y reuniones semanales de seguimiento con soporte uno a uno durante la puesta en marcha.",
   "more": "<h3>Bonos de la oferta actual</h3><ul><li>Landing page de alta conversión.</li><li>Subcuenta de GoHighLevel.</li><li>Soporte grupal semanal.</li><li>Soporte uno a uno por 60 días.</li></ul>",
   "pend": ["Carlos: confirmar que los bonos siguen vigentes."]},
  {"q": "¿Cuánto tiempo tarda implementar Kommo CRM?",
   "a": "La implementación tarda 35 días y se hace en 8 reuniones. El director comercial dedica 2 horas a la semana a revisar el avance. Gmarketing hace la configuración: embudos, flujos, integraciones y agentes de IA. El equipo de ventas recibe capacitación en técnicas de venta por chat antes de empezar a operar en Kommo.",
   "more": "<ol><li>Introducción a Kommo CRM</li><li>Brief, expectativas y alcance</li><li>Capacitación y técnicas de venta por chat</li><li>Diseño de embudos y fases</li><li>Experiencia de chat entrante</li><li>Experiencia de seguimientos</li><li>Automatizaciones</li><li>Auditoría y entrega</li></ol>"},
  {"q": "¿Qué pasa si la implementación no da resultados?",
   "a": "Gmarketing reembolsa el valor de la implementación si a los 35 días no se cumplen tres métricas: 34% más de productividad, respuesta a los prospectos en 10 segundos y 10% más de ventas conversacionales. La garantía aplica cuando el cliente cumple sus obligaciones y no cubre las licencias de Kommo.",
   "more": '<p>Condiciones completas en la página de <a href="/garantia/">garantía</a>.</p>'},
  {"q": "¿Para qué empresas sirve la implementación?",
   "a": "Kommo10X está diseñada para empresas B2C con equipos de 3 a 20 vendedores que reciben más de 500 leads al mes por WhatsApp, web o redes sociales. Los sectores más frecuentes son turismo, educación, clínicas, bienes raíces, concesionarios y comercio de alto ticket.",
   "more": "<p>Señales de que la necesitas: los leads llegan por varios canales y se pierden, hay chats sin contestar fuera de horario, el equipo depende de uno o dos números de WhatsApp y la dirección no tiene métricas por vendedor, etapa o canal.</p>"},
  {"q": "¿Qué plan de Kommo necesito?", "id": "planes",
   "a": "La mayoría de equipos que venden por WhatsApp con salesbots necesitan el plan Avanzado, desde USD 30 por usuario al mes. Desde junio de 2026 el plan también depende de los leads activos, los canales conectados, las automatizaciones, el uso de IA y las integraciones. En el diagnóstico revisamos esos seis factores antes de comprar.",
   "more": LICENCIAS_TABLA,
   "pend": ["Carlos o Juan Pablo: confirmar los precios de licencias vigentes en kommo.com/es/precios/ el día de publicar.", "Carlos: validar la frase «la mayoría de equipos… necesitan el plan Avanzado»."]},
 ],
 "related": [("/partner-kommo-colombia/", "Partner de Kommo en Colombia"), ("/agente-ia-whatsapp/", "Agente de IA para WhatsApp"), ("/whatsapp-multiagente/", "WhatsApp multiagente para empresas")],
},
# ------------------------------------------------------------------ 2
{
 "slug": "/partner-kommo-colombia/", "hl": "Partner de Kommo", "crumb": "Partner de Kommo en Colombia", "kind": "service",
 "title": "Partner de Kommo en Colombia: Gmarketing (Cali y Miami)",
 "desc": "Gmarketing es partner oficial de Kommo con oficinas en Cali y Miami. Vende licencias, implementa Kommo con WhatsApp API e IA y opera Kommo por suscripción mensual.",
 "h1": "Partner de Kommo en Colombia: Gmarketing",
 "lead": "Gmarketing S.A.S. (Cali) y Gmarketing USA LLC (Miami) son partner oficial de Kommo y figuran en el directorio de partners de Kommo. Venden licencias, implementan Kommo con WhatsApp Business API e IA, y operan cuentas de Kommo con planes mensuales.",
 "pend_top": [CIFRA, "Carlos: confirmar nivel de partner (Gold) y año de inicio para el primer párrafo."],
 "service": {"name": "Partner de Kommo en Colombia", "type": "Reseller e implementador de Kommo CRM",
             "desc": "Venta de licencias de Kommo, implementación Kommo10X, agentes de IA en n8n, atribución de ventas con la API de Conversiones de Meta y operación de Kommo con IA."},
 "sections": [
  {"q": "¿Gmarketing es partner oficial de Kommo?",
   "a": 'Sí. Gmarketing S.A.S. y Gmarketing USA LLC aparecen en el directorio oficial de partners de Kommo. Como partner, Gmarketing vende las licencias, hace la implementación y da soporte en español a los equipos comerciales que usan Kommo en Colombia, Latinoamérica y Estados Unidos.',
   "more": '<p>Perfil en el directorio de Kommo: <a href="https://www.kommo.com/es/socios/encontrar-socio/gmarketing-s-a-s-gmarketing-usa-llc/" target="_blank" rel="noopener">Gmarketing S.A.S. / Gmarketing USA LLC</a>.</p>'},
  {"q": "¿Qué ventaja tiene comprar Kommo con un partner?",
   "a": "Comprar las licencias con Gmarketing da meses gratis según el plazo: 1 mes extra al comprar 6, 2 al comprar 8, 3 al comprar 10 y 7 al comprar 18. Además, el diagnóstico gratuito revisa qué plan necesitas antes de pagar, y la cuenta queda a nombre de tu empresa.",
   "pend": ["Carlos: confirmar que la promoción de meses gratis sigue vigente y si tiene fecha de cierre."]},
  {"q": "¿Qué servicios ofrece Gmarketing sobre Kommo?",
   "a": "Gmarketing ofrece cinco servicios sobre Kommo: venta de licencias, implementación Kommo10X en 35 días, N8X (agente de IA en n8n desde USD 200 al mes), Tracking GM (atribución de ventas con la API de Conversiones de Meta, USD 100 al mes) y KommoPower GM (reportes y auditoría mensual, USD 100 al mes).",
   "more": '<ul><li><a href="/kommo-crm/">Implementación de Kommo CRM</a></li><li><a href="/agente-ia-whatsapp/">Agente de IA para WhatsApp (N8X)</a></li><li><a href="/soluciones_agenticas/">Soluciones agénticas: N8X, Tracking GM y KommoPower GM</a></li></ul>',
   "pend": ["Carlos: los combos tienen precios distintos en el home (N8X + Tracking GM: USD 270) y en /soluciones_agenticas/ (USD 300). Definir cuál queda."]},
  {"q": "¿Dónde atiende Gmarketing?",
   "a": "Gmarketing atiende desde Cali, Colombia (Calle 26N # 5AN-50) y desde Miami, Estados Unidos (31 SE 5th St). Las implementaciones se hacen por videollamada, así que el equipo trabaja con empresas de cualquier país de Latinoamérica y con negocios hispanos en Estados Unidos.",
   "pend": ["Carlos: listar los países donde hay clientes activos para nombrarlos aquí."]},
  {"q": "¿Qué empresas han implementado Kommo con Gmarketing?",
   "a": "Entre los clientes publicados están Pink Rose, que gestiona más de 10.000 chats al mes con IA que responde en 5 segundos; Tryp by Wyndham Zahir, que automatizó el 80% de las consultas frecuentes; y Move Training, que recupera el 20% de los leads antiguos con embudos de retargeting.",
   "more": "<p>Otros casos publicados: Inversiones Transmundo (tablero en tiempo real y KPIs de conversión) e Impacto Solar (la IA asigna e inicia el chat con el lead en menos de 2 segundos).</p>",
   "pend": [CIFRA, "Carlos: confirmar autorización escrita de cada cliente para nombrarlo y que las cifras de cada caso siguen siendo correctas."]},
 ],
 "related": [("/kommo-crm/", "Implementación de Kommo CRM"), ("/kommo-vs-leadsales/", "Kommo vs Leadsales"), ("/blog/mejor-crm-whatsapp/", "Mejor CRM para WhatsApp")],
},
# ------------------------------------------------------------------ 3
{
 "slug": "/kommo-vs-leadsales/", "hl": "Kommo vs Leadsales", "crumb": "Kommo vs Leadsales", "kind": "article",
 "title": "Kommo vs Leadsales: comparativa para equipos que venden por WhatsApp",
 "desc": "Comparativa de Kommo y Leadsales: canales, automatización, IA, precios por usuario y para qué tipo de equipo comercial conviene cada uno.",
 "h1": "Kommo vs Leadsales: cuál conviene para vender por WhatsApp",
 "lead": "Kommo conviene a equipos que atienden por WhatsApp, Instagram, Facebook y web en una sola bandeja y necesitan automatizar con salesbots, IA e integraciones. Leadsales es un CRM mexicano enfocado en WhatsApp para pymes. La decisión depende de cuántos canales usas y de cuánto quieres automatizar.",
 "pend_top": ["Carlos: verificar en leadsales.io cada dato de Leadsales (canales, planes, precios, IA, integraciones) y anotar la fuente y la fecha. Gmarketing es partner de Kommo: dejarlo dicho en la página."],
 "sections": [
  {"q": "¿Cuál es la diferencia principal entre Kommo y Leadsales?",
   "a": "La diferencia principal está en los canales y la automatización. Kommo reúne WhatsApp, Instagram, Facebook Messenger, correo y formularios web en una bandeja, con embudos automáticos, salesbots, agentes de IA y API abierta. Leadsales se enfoca en WhatsApp para pymes.",
   "pend": ["Carlos: completar con lo que Leadsales ofrece hoy en otros canales e IA, con fuente."]},
  {"q": "¿Cómo se comparan en funciones?", "faq": False,
   "a": "Tabla de comparación por función. La columna de Kommo usa la información de los planes publicados por Kommo.",
   "more": """<div class="tbl"><table>
<tr><th>Función</th><th>Kommo</th><th>Leadsales</th></tr>
<tr><td>Canales</td><td>WhatsApp (Lite y API oficial), Instagram, Facebook Messenger, correo y formularios web</td><td>[verificar]</td></tr>
<tr><td>Multiagente</td><td>Sí: asignación de chats, notas internas y monitoreo del equipo</td><td>[verificar]</td></tr>
<tr><td>Automatización</td><td>Embudo automatizado, difusiones y bots sin código desde el plan Avanzado</td><td>[verificar]</td></tr>
<tr><td>IA</td><td>Respuestas sugeridas y resúmenes desde Básico; hasta 3 agentes de IA en Avanzado y hasta 50 en Pro</td><td>[verificar]</td></tr>
<tr><td>Precio</td><td>Desde USD 20 por usuario al mes, compra mínima de 6 meses</td><td>[verificar]</td></tr>
<tr><td>API y webhooks</td><td>Sí, desde Básico</td><td>[verificar]</td></tr>
</table></div>"""},
  {"q": "¿Cuál conviene para una clínica, inmobiliaria o rentadora?",
   "a": "Para una clínica, inmobiliaria o rentadora con varios asesores conviene Kommo cuando los leads llegan por más de un canal, cuando hay que agendar citas o visitas y cuando la dirección necesita tableros por asesor. Si el negocio atiende solo por WhatsApp con uno o dos asesores, una herramienta más simple puede alcanzar.",
   "pend": ["Carlos: agregar un caso de cliente por sector (clínica, inmobiliaria, rentadora) con autorización."]},
  {"q": "¿Cuánto cuesta cada uno?",
   "a": "Kommo cuesta desde USD 20 por usuario al mes en el plan Básico, USD 30 en Avanzado y USD 45 en Pro, con compra mínima de 6 meses. Un equipo de 5 asesores en Avanzado paga desde USD 150 al mes en licencias. Los precios de Leadsales están en su sitio oficial.",
   "pend": ["Carlos: precios de Leadsales con fuente y fecha.", "Juan Pablo: confirmar precios de Kommo vigentes el día de publicar."]},
 ],
 "related": [("/blog/mejor-crm-whatsapp/", "Mejor CRM para WhatsApp en 2026"), ("/kommo-crm/", "Implementación de Kommo CRM"), ("/whatsapp-multiagente/", "WhatsApp multiagente")],
},
# ------------------------------------------------------------------ 4
{
 "slug": "/blog/mejor-crm-whatsapp/", "hl": "CRM para WhatsApp", "crumb": "Mejor CRM para WhatsApp", "crumbs": [("Guías", "/blog/mejor-crm-whatsapp/")], "kind": "article",
 "title": "Mejor CRM para WhatsApp en 2026: cómo elegir y cuáles comparar",
 "desc": "Siete criterios para elegir un CRM para WhatsApp en 2026: API oficial, multiagente, embudos, automatización, IA, integraciones y precio por usuario.",
 "h1": "Mejor CRM para WhatsApp en 2026: cómo elegir",
 "lead": "Un CRM para WhatsApp debe conectarse a la API oficial de WhatsApp Business, repartir chats entre varios asesores, mover cada lead por un embudo y medir resultados por vendedor. Gmarketing recomienda Kommo y es partner oficial; esta guía explica los criterios para que compares con cualquier alternativa.",
 "pend_top": ["Carlos: armar la tabla de 5 a 6 CRM (Kommo, Leadsales, Clientify, Callbell, Respond.io, HubSpot) con fuente y fecha por dato. Ver pestaña «Competencia» del estudio."],
 "sections": [
  {"q": "¿Qué debe tener un CRM para WhatsApp?",
   "a": "Un CRM para WhatsApp debe tener siete cosas: conexión a la API oficial de WhatsApp Business, bandeja multiagente, embudo de ventas por etapas, automatizaciones y bots, IA para responder y resumir, integraciones con formularios y anuncios, y reportes por vendedor. Sin la API oficial, el número corre riesgo de bloqueo.",
   "more": "<ol><li><strong>API oficial de WhatsApp Business (WABA):</strong> sigue las políticas de Meta y reduce el riesgo de bloqueo.</li><li><strong>Multiagente:</strong> varios asesores en el mismo número, con asignación automática.</li><li><strong>Embudo:</strong> cada lead en una etapa visible para la dirección.</li><li><strong>Automatización:</strong> tareas, mensajes y cambios de etapa sin intervención manual.</li><li><strong>IA:</strong> respuesta inmediata fuera de horario y calificación del lead.</li><li><strong>Integraciones:</strong> formularios web, Meta Ads, Google Ads y analítica.</li><li><strong>Reportes:</strong> tiempo de respuesta y conversión por asesor.</li></ol>"},
  {"q": "¿Por qué recomendamos Kommo?",
   "a": "Recomendamos Kommo porque reúne WhatsApp, Instagram, Facebook y formularios web en una bandeja, mueve leads por el embudo de forma automática, trae salesbots sin código desde el plan Avanzado y permite conectar agentes de IA externos por API. Gmarketing es partner oficial de Kommo, así que esta recomendación no es neutral.",
   "more": '<p>Ver <a href="/kommo-crm/">qué incluye la implementación</a> y <a href="/kommo-crm/#planes">los planes de Kommo</a>.</p>'},
  {"q": "¿Cuáles son las alternativas a Kommo?",
   "a": "Las alternativas que más se buscan en Colombia son Clientify, Callbell y Leadsales. Cada una tiene un enfoque distinto: CRM con marketing, bandeja de atención y CRM centrado en WhatsApp para pymes. La tabla de abajo compara los siete criterios con datos de cada proveedor.",
   "pend": ["Carlos: tabla comparativa con fuente y fecha por dato."]},
  {"q": "¿Cuánto cuesta un CRM para WhatsApp?",
   "a": "Un CRM para WhatsApp cuesta por usuario al mes. En Kommo, el plan Básico arranca en USD 20, el Avanzado en USD 30 y el Pro en USD 45, con compra mínima de 6 meses. A eso se suman los mensajes de WhatsApp Business API, que Meta cobra por mensaje entregado según el país y el tipo de plantilla.",
   "more": '<p>Ver <a href="/blog/precios-whatsapp-api-2026/">precios de WhatsApp Business API en 2026</a>.</p>'},
 ],
 "related": [("/kommo-vs-leadsales/", "Kommo vs Leadsales"), ("/whatsapp-multiagente/", "WhatsApp multiagente"), ("/blog/precios-whatsapp-api-2026/", "Precios de WhatsApp API 2026")],
},
# ------------------------------------------------------------------ 5
{
 "slug": "/whatsapp-multiagente/", "hl": "WhatsApp multiagente", "crumb": "WhatsApp multiagente", "kind": "service",
 "title": "WhatsApp multiagente para empresas: cómo funciona y cuánto cuesta",
 "desc": "WhatsApp multiagente con Kommo: varios asesores en un mismo número, asignación automática de chats, notas internas y tableros. Desde USD 20 por usuario al mes.",
 "h1": "WhatsApp multiagente para empresas",
 "lead": "WhatsApp multiagente permite que varios asesores atiendan el mismo número de WhatsApp desde una bandeja compartida. Con Kommo, cada chat se asigna a un asesor, queda en una etapa del embudo y la dirección ve tiempos de respuesta y ventas por persona. Un equipo de 5 asesores paga desde USD 100 al mes en licencias.",
 "service": {"name": "WhatsApp multiagente con Kommo CRM", "type": "CRM multiagente para WhatsApp",
             "desc": "Configuración de WhatsApp Business API en Kommo para que varios asesores atiendan el mismo número con asignación automática, notas internas y reportes."},
 "sections": [
  {"q": "¿Cómo funciona WhatsApp multiagente?",
   "a": "WhatsApp multiagente funciona conectando el número a la API oficial de WhatsApp Business y esa API a un CRM como Kommo. Cada mensaje entra a una bandeja compartida, el sistema asigna el chat a un asesor por reglas o por turno, y el resto del equipo ve el historial y deja notas internas.",
   "more": "<ul><li>Asignación automática de chats al asesor adecuado.</li><li>Notas internas y chats entre el equipo dentro de cada conversación.</li><li>Monitoreo del equipo en tiempo real.</li><li>Aplicación móvil con notificaciones.</li></ul>"},
  {"q": "¿Cuánto cuesta WhatsApp multiagente?",
   "a": "WhatsApp multiagente con Kommo cuesta desde USD 20 por usuario al mes en el plan Básico. Un equipo de 5 asesores paga desde USD 100 al mes; con salesbots en el plan Avanzado, desde USD 150 al mes. A eso se suman los mensajes de WhatsApp Business API que cobra Meta.",
   "more": CALC_ASESORES + '<p>¿Quieres saber cuánto pierdes hoy sin CRM? Usa la <a href="/calculadora/">calculadora de costo de oportunidad</a>.</p>'},
  {"q": "¿Se puede usar WhatsApp Business app con varios asesores?",
   "a": "La app de WhatsApp Business admite pocos dispositivos vinculados y no reparte chats ni mide a cada asesor. Para un equipo de 3 o más vendedores, la API oficial conectada a un CRM es la opción estable: permite varios usuarios, automatizaciones y reportes, y sigue las políticas de Meta.",
   "pend": ["Carlos: confirmar con fuente oficial de Meta cuántos dispositivos admite hoy WhatsApp Business app."]},
  {"q": "¿Me pueden bloquear el número?",
   "a": "El riesgo de bloqueo baja casi a cero con la API oficial de WhatsApp Business (WABA), porque los mensajes salen por plantillas aprobadas por Meta y siguen sus políticas. El riesgo aumenta cuando se usan herramientas no oficiales o se envían difusiones masivas sin consentimiento desde la app."},
 ],
 "related": [("/kommo-crm/", "Implementación de Kommo CRM"), ("/blog/mejor-crm-whatsapp/", "Mejor CRM para WhatsApp"), ("/agente-ia-whatsapp/", "Agente de IA para WhatsApp")],
},
# ------------------------------------------------------------------ 6
{
 "slug": "/blog/precios-whatsapp-api-2026/", "hl": "WhatsApp Business API", "crumb": "Precios de WhatsApp API 2026", "crumbs": [("Guías", "/blog/mejor-crm-whatsapp/")], "kind": "article",
 "title": "Precios de WhatsApp Business API en 2026 para Colombia",
 "desc": "Tarifas de WhatsApp Business API en Colombia desde octubre de 2026: marketing USD 0,0125; utilidad, autenticación y servicio USD 0,0008 por mensaje.",
 "h1": "Precios de WhatsApp Business API en 2026 para Colombia",
 "lead": "Meta cobra WhatsApp Business API por mensaje entregado, según el país de quien lo recibe y la categoría de la plantilla. En Colombia, desde el 1 de octubre de 2026, un mensaje de marketing cuesta USD 0,0125 y uno de utilidad, autenticación o servicio USD 0,0008. Meta solo cambia tarifas el 1 de enero, abril, julio y octubre.",
 "pend_top": ["Juan Pablo o Carlos: antes de publicar, abrir developers.facebook.com/docs/whatsapp/pricing y confirmar que las tarifas de Colombia siguen iguales. Las cifras salen del rate card de Meta tomado el 2-sep-2026, el mismo que usa /costos_api/."],
 "sections": [
  {"q": "¿Cuánto cuesta un mensaje de WhatsApp Business API en Colombia?",
   "a": "En Colombia, un mensaje de marketing cuesta USD 0,0125 y uno de utilidad, autenticación o servicio cuesta USD 0,0008. Los precios son por mensaje entregado, sin impuestos y sin lo que cobre el proveedor de software. Utilidad y autenticación bajan por volumen desde 100.000 mensajes al mes; los primeros 1.000 de servicio son gratis.",
   "more": """<div class="tbl"><table><tr><th>Categoría</th><th>Precio por mensaje (USD)</th><th>Uso</th></tr>
<tr><td>Marketing</td><td>0,0125</td><td>Promociones, ofertas, reactivación</td></tr>
<tr><td>Utilidad</td><td>0,0008</td><td>Confirmaciones, recordatorios, estado de pedido</td></tr>
<tr><td>Autenticación</td><td>0,0008</td><td>Códigos de verificación</td></tr>
<tr><td>Servicio</td><td>0,0008 (primeros 1.000 al mes gratis)</td><td>Respuestas dentro de la ventana de 24 horas</td></tr></table></div>
<p>Calcula el costo de tu volumen y de otros países en la <a href="/costos_api/">calculadora de precios de WhatsApp Business API</a>.</p>"""},
  {"q": "¿Qué cambió en los precios de WhatsApp API en octubre de 2026?",
   "a": "Desde el 1 de octubre de 2026 Meta cobra los mensajes de servicio, que antes eran gratis: en Colombia cuestan USD 0,0008, sin descuentos por volumen, y los primeros 1.000 de cada mes no se cobran. También se cobran los avisos de utilidad enviados dentro de la ventana de 24 horas que abre el cliente.",
   "more": "<p>Sigue siendo gratis la ventana de 72 horas de las conversaciones que empiezan desde un anuncio Click-to-WhatsApp o un botón de Facebook o Instagram. Los mensajes del Meta Business Agent se cobran aparte desde el 1 de agosto de 2026: USD 2 por millón de tokens.</p>"},
  {"q": "¿Quién decide la categoría de cada mensaje?",
   "a": "Meta decide la categoría al aprobar cada plantilla. Si un aviso de utilidad incluye texto de promoción, Meta lo clasifica como marketing y en Colombia cuesta unas 15 veces más: USD 0,0125 contra USD 0,0008. Por eso conviene separar las plantillas de recordatorio de las de oferta y revisar la categoría aprobada de cada una."},
  {"q": "¿Cómo bajar el costo de WhatsApp API?",
   "a": "El costo baja resolviendo la conversación dentro de la ventana de 24 horas que abre el cliente: cada respuesta de servicio cuesta USD 0,0008 y los primeros 1.000 del mes son gratis, mientras que una plantilla de marketing cuesta USD 0,0125. Un agente de IA que responde al instante mantiene la conversación dentro de esa ventana.",
   "more": '<p>Ver <a href="/agente-ia-whatsapp/">agente de IA para WhatsApp</a>.</p>'},
 ],
 "related": [("/blog/mejor-crm-whatsapp/", "Mejor CRM para WhatsApp"), ("/whatsapp-multiagente/", "WhatsApp multiagente"), ("/agente-ia-whatsapp/", "Agente de IA para WhatsApp")],
},
# ------------------------------------------------------------------ 7
{
 "slug": "/agente-ia-whatsapp/", "hl": "Agente de IA", "crumb": "Agente de IA para WhatsApp", "kind": "service",
 "title": "Agente de IA para WhatsApp conectado a Kommo: N8X desde USD 200/mes",
 "desc": "N8X es un agente de IA para WhatsApp conectado a Kommo: responde 24/7, califica, agenda, mueve el lead en el embudo y llena los campos. Desde USD 200 al mes.",
 "h1": "Agente de IA para WhatsApp conectado a tu CRM",
 "lead": "N8X es el agente de IA de Gmarketing para WhatsApp. Funciona sobre n8n, lee y escribe en Kommo, responde a cualquier hora, hace las preguntas que califican al lead, agenda citas y mueve la oportunidad en el embudo. Cuesta USD 200 al mes, con 2 horas de soporte incluidas.",
 "service": {"name": "N8X: agente de IA para WhatsApp conectado a Kommo", "type": "Agente de IA para WhatsApp",
             "desc": "Agente de IA sobre n8n conectado a Kommo CRM que responde, califica, agenda, cambia la etapa del lead, llena campos y hace seguimiento.",
             "offers": [("N8X mensual", "200", "Pago mes a mes, 2 horas de soporte al mes."), ("N8X semestral", "900", "Pago anticipado por 6 meses."), ("N8X anual", "1200", "Pago anticipado por 12 meses.")]},
 "sections": [
  {"q": "¿Qué hace un agente de IA en WhatsApp?",
   "a": "Un agente de IA en WhatsApp responde al instante, de día, de noche y en fines de semana. N8X además precalifica con las preguntas que definen si el lead sirve, agenda la cita, cambia la etapa del lead en Kommo, guarda en los campos lo que el cliente cuenta y retoma a quien dejó de contestar.",
   "more": "<h3>Tres formas de usarlo</h3><ul><li><strong>Prefiltro:</strong> separa curiosos de compradores antes de que lleguen al equipo.</li><li><strong>Precalificador:</strong> entrega al asesor el lead con sus datos y su intención.</li><li><strong>Servicio al cliente:</strong> resuelve preguntas frecuentes sin ocupar a los asesores.</li></ul>"},
  {"q": "¿Cuánto cuesta un agente de IA para WhatsApp?", "id": "precios",
   "a": "N8X cuesta USD 200 al mes, USD 900 por 6 meses o USD 1.200 por 12 meses, con pago anticipado en los planes largos. Incluye 2 horas de soporte al mes; la hora adicional cuesta USD 50. Aparte se pagan los tokens de IA a OpenRouter según el uso, las licencias de Kommo y los mensajes de WhatsApp API.",
   "more": """<div class="tbl"><table><tr><th>Plan</th><th>Mensual</th><th>Semestral</th><th>Anual</th><th>Soporte</th></tr>
<tr><td>N8X</td><td>USD 200</td><td>USD 900</td><td>USD 1.200</td><td>2 horas al mes</td></tr></table></div>
<p>Sin permanencia en el plan mensual. Los planes semestral y anual se pagan completos al inicio y no tienen devolución si se cancela antes.</p>""",
   "pend": ["Carlos: definir los combos con Tracking GM y KommoPower GM (home: USD 270; /soluciones_agenticas/: USD 300) antes de agregarlos aquí.", "Carlos: agregar un ejemplo del costo mensual de tokens para un volumen típico (p. ej., 1.000 conversaciones)."]},
  {"q": "¿Cómo se conecta el agente de IA con Kommo?",
   "a": "El agente se conecta a Kommo con n8n. El cliente escribe por WhatsApp, el mensaje llega a Kommo, n8n se lo pasa al agente y el agente responde, actualiza los campos y mueve la etapa. Para activarlo necesitamos un usuario de soporte en tu Kommo; la cuenta y los datos siguen siendo de tu empresa."},
  {"q": "¿En qué se diferencia de un chatbot?",
   "a": "Un chatbot sigue un árbol de opciones fijo; un agente de IA entiende lo que el cliente escribe, decide la siguiente pregunta y actúa en el CRM. N8X no solo conversa: califica, agenda, cambia la etapa del lead y avisa al asesor cuando la conversación necesita a una persona.",
   "pend": ["Carlos: agregar dos ejemplos de conversación reales (sin datos del cliente) chatbot vs agente."]},
  {"q": "¿Cuánto tarda en estar funcionando?",
   "a": "El proceso tiene tres pasos: eliges el plan, firmas el contrato y pagas, y el agente queda operando sobre tu CRM con soporte por un grupo de WhatsApp de lunes a viernes, con respuesta en 24 horas o un día hábil.",
   "pend": ["Carlos: definir el tiempo típico de puesta en marcha en días para abrir la respuesta con ese dato."]},
 ],
 "related": [("/blog/meta-business-agent/", "Meta Business Agent vs agente propio"), ("/kommo-crm/", "Implementación de Kommo CRM"), ("/blog/precios-whatsapp-api-2026/", "Precios de WhatsApp API 2026")],
 "cta": ("Te mostramos el agente funcionando sobre un Kommo de prueba y revisamos qué preguntas debe hacer en tu negocio.", "Agendar demostración"),
},
# ------------------------------------------------------------------ 8
{
 "slug": "/blog/meta-business-agent/", "hl": "Meta Business Agent", "crumb": "Meta Business Agent vs agente propio", "crumbs": [("Guías", "/blog/mejor-crm-whatsapp/")], "kind": "article",
 "title": "Meta Business Agent vs agente de IA propio conectado a tu CRM",
 "desc": "Cuándo alcanza el agente de IA nativo de WhatsApp Business y cuándo conviene un agente propio conectado a Kommo, con embudo, campos y métricas.",
 "h1": "Meta Business Agent vs agente de IA propio conectado a tu CRM",
 "lead": "El agente de IA nativo de WhatsApp Business sirve para responder preguntas frecuentes dentro de WhatsApp. Un agente propio conectado al CRM además registra cada lead, lo mueve por el embudo, agenda y mide resultados por canal y por asesor. La elección depende de si tu equipo necesita esa trazabilidad.",
 "pend_top": ["Carlos: verificar en la documentación oficial de Meta qué hace hoy el agente nativo (nombre oficial, países disponibles, precio, si se conecta a un CRM) y citar la fuente con fecha."],
 "sections": [
  {"q": "¿Qué es Meta Business Agent?",
   "a": "Meta Business Agent es el agente de IA que Meta integra en WhatsApp Business para que pequeños negocios respondan de forma automática. Se configura dentro de WhatsApp y atiende las preguntas frecuentes con la información del negocio.",
   "pend": ["Completar con funciones, precio y disponibilidad verificados en fuente oficial."]},
  {"q": "¿Cuándo no alcanza el agente nativo de WhatsApp?",
   "a": "El agente nativo no alcanza cuando el negocio necesita CRM, embudo y métricas: registrar cada lead con su origen, moverlo por etapas, asignarlo a un asesor, agendar en un calendario propio y medir conversión por anuncio y por vendedor. Esas funciones requieren un agente conectado al CRM.",
   "pend": ["Validar contra la documentación de Meta que el agente nativo no ofrece estas funciones."]},
  {"q": "¿Qué hace un agente propio conectado a Kommo?",
   "a": "Un agente propio como N8X responde, precalifica, agenda, cambia la etapa del lead en Kommo, llena los campos con lo que cuenta el cliente y retoma a quien deja de contestar. Con Tracking GM, cada venta vuelve a Meta como conversión con el anuncio que la originó.",
   "more": '<p>Ver <a href="/agente-ia-whatsapp/">N8X, agente de IA para WhatsApp</a>.</p>'},
  {"q": "¿Se puede usar ChatGPT en WhatsApp Business API?",
   "a": "Las políticas de Meta distinguen entre chatbots de propósito general y agentes de negocio. Un agente que atiende a los clientes de una empresa sobre sus productos y servicios es un uso de negocio.",
   "pend": ["Carlos: citar la política vigente de Meta sobre chatbots de propósito general en WhatsApp Business API, con enlace y fecha, y reescribir la respuesta empezando con el dato."]},
 ],
 "related": [("/agente-ia-whatsapp/", "Agente de IA para WhatsApp"), ("/blog/precios-whatsapp-api-2026/", "Precios de WhatsApp API 2026"), ("/kommo-crm/", "Implementación de Kommo CRM")],
},
]
