# crmformeta.com: plan SEO, GEO y AEO

Tarea en Soporte: `77b2e52b-efdd-43fa-aeee-ffc14c41a060` ("Ejecutar plan SEO, GEO y AEO de crmformeta.com").
Responsable: Juan Pablo Acosta. Aprobación y contenido: Carlos Chávez (María Camila Jaramillo ya no está en el equipo; sus tareas pasaron a Carlos el 26-nov-2026).

Repo de trabajo del plan. Rutas de los comandos relativas a la raíz del repo.

## Carpetas

| Carpeta | Qué tiene |
|---|---|
| `generador/` | `plantilla.py` (HTML, estilos y schema), `paginas.py` (contenido de las páginas AEO), `build.py` (genera), `paginas_legales.py` (/privacidad/ y /garantia/) |
| `publicado/` | Archivos tal como están hoy en el servidor: home, robots.txt, sitemap.xml, llms.txt, .htaccess, páginas legales y borradores |
| `respaldo-2026-11-25/` | Copia del sitio antes de los cambios del 25-nov-2026, sin `*.php` (tienen contraseñas SMTP) ni `/entregables/` (tienen tokens de clientes) |
| `subir.sh` | Sube un archivo al hosting por la API de Hostinger |
| `herramientas/rastreo.py` | Rastreo SEO del sitio (códigos HTTP, title, descripción, canonical, H1, enlaces rotos, cifras). Resultado en `reportes/` |

## Dónde vive el sitio

- Hosting compartido de Hostinger, cuenta `u806273835`, carpeta `domains/crmformeta.com/public_html`.
- HTML estático, sin WordPress. Cloudflare delante.
- El VPS `31.220.108.70` es el servidor de n8n, no el de los sitios.
- La API de Hostinger lista, lee y sube archivos. No borra: para "quitar" un archivo se sube vacío.

## Publicar un cambio

```bash
cd generador
python3 build.py
```

```bash
HOSTINGER_API_TOKEN=xxxx ../subir.sh crmformeta.com ../publicado/kommo-crm/index.html kommo-crm/index.html
```

Pide el token a Miguel. Nunca lo escribas en el repo.

Después de subir, abre la URL con `?v=123` al final para saltar la caché y revisa que cargue.

## Pasar un borrador a publicado

1. Revisa que la página no tenga bloques amarillos de PENDIENTE: Carlos los completa y aprueba precios y cifras.
2. En `generador/paginas.py`, agrega `"draft": False` a la página.
3. Corre `python3 build.py` y sube el `index.html` de esa página.
4. Agrega la URL a `publicado/sitemap.xml` y súbelo.
5. Enlaza la página desde el home (`publicado/index.html`) y sube el home.
6. Pásala por la prueba de resultados enriquecidos de Google.

## Estado al 25-nov-2026

Publicado y en el índice: home corregida, `/privacidad/`, `/garantia/`, `/llms.txt`, `robots.txt`, `sitemap.xml` y `.htaccess` (301 de www y /index.html).

Borradores en `noindex`, fuera del sitemap:
`/kommo-crm/`, `/partner-kommo-colombia/`, `/kommo-vs-leadsales/`, `/blog/mejor-crm-whatsapp/`,
`/whatsapp-multiagente/`, `/blog/precios-whatsapp-api-2026/`, `/agente-ia-whatsapp/`, `/blog/meta-business-agent/`.

Pendientes de Carlos:
- Cifra única de empresas atendidas: el sitio dice 250, 500, 260, 200, 400 y 150. El Excel propone "Gold Partner de Kommo desde 2020" y "+260 implementaciones". /kommo10x/ dice "desde 2014".
- Precio de los combos: N8X + Tracking GM vale USD 270 en el home y USD 300 en /soluciones_agenticas/.
- FAQ del home "¿Debo pagar mensualidades extra? No", que contradice los planes mensuales.
- Ficha de entidad para /quienes-somos/ y política de privacidad completa (Ley 1581).

Pendientes técnicos:
- Search Console, Bing Webmaster y canal "IA" en GA4 (`G-R05L91RDJD`).
- `/costos_api/` tiene el canonical apuntando a calculadora.dotsflow.ai y la marca "DotsCom Group".

## Avance 26-nov-2026 (Juan Pablo, parte técnica)

- Schema validado en validator.schema.org: home, /privacidad/, /garantia/ y borradores sin errores ni avisos.
- IndexNow activo: clave en `publicado/ccc854a102d5781b78e5ad4a162a96b0.txt`. Las 12 URLs del sitemap se enviaron a api.indexnow.org (respuesta 202). Al publicar una URL nueva, volver a enviarla.
- `.htaccess`: la 301 de `index.html` ahora aplica en todas las carpetas.
- Canonical agregado en /kommo10x/, /kommo10x/agenda/, /soluciones_agenticas/, /crm_para_whatsapp/, /documentacion/, /gestion_de_respuestas_de_prospectos/, /como_convertir_el_no_en_si/ y /5_razones_cliente_no_compra/.
- /kommo10x/: 4 enlaces vacíos a Calendly; quitado el botón de Google Business que apuntaba a `TU_LINK_GMB`. Ponerlo de nuevo cuando Carlos pase el enlace del perfil.
- Enlaces a /exito/ (404) cambiados a /#casos en /kommo10x/, /kommo10x/agenda/, /calculadora/ y /documentacion/.
- /calculadora/: title, descripción y canonical nuevos. Calcula el costo de no tener CRM, no licencias.
- Borrador /whatsapp-multiagente/: calculadora propia de asesores × plan × meses.
- Rastreo: `reportes/rastreo-2026-11-26.md`. Cero enlaces internos rotos.

Cuentas (hecho por Juan Pablo el 26-nov-2026):
- Search Console: propiedad de dominio `crmformeta.com` verificada. Sitemap enviado como `https://crmformeta.com/sitemap.xml` (en propiedad de dominio hay que poner la URL completa): correcto, 12 páginas.
- Bing Webmaster: importado desde Search Console. Sitemap enviado, en procesamiento.
- GA4 (`G-R05L91RDJD`): grupo de canales "Canales con IA" con el canal "IA" (fuente coincide parcialmente con la regex `chatgpt|openai|perplexity|gemini|claude|copilot|deepseek`), ubicado antes de Referral y Organic Search.
- Prueba de resultados enriquecidos del home: 4 elementos válidos (Empresas locales, Organización, 2 Vídeos), sin errores; avisos no críticos por campos opcionales.
- Pendiente: prueba de resultados enriquecidos de /kommo-crm/.

Hallazgos del rastreo de texto (tarea de Carlos):
- Descripciones de más de 160 caracteres: /kommo10x/ (254), /crm_para_whatsapp/ (310), /documentacion/ (166), /gestion_de_respuestas_de_prospectos/ (290), /como_convertir_el_no_en_si/ (301), /5_razones_cliente_no_compra/ (296).
- /kommo10x/agenda/ no tiene descripción.
- Varios H1 en una misma página: /documentacion/ (13), /kommo10x/, /calculadora/ y las 4 guías antiguas (2).
- /crm_para_whatsapp/ se desborda en celular (390 px de pantalla, 420 px de contenido).

## /costos_api/ adaptada a Gmarketing (26-nov-2026)

- Antes: marca "DotsCom Group", teléfono +57 316 9062242, correo de dotscomagency.com, voseo argentino y canonical hacia calculadora.dotsflow.ai.
- Ahora: marca Gmarketing, WhatsApp +57 321 6319137, comercial@gmarketing.co, español de Colombia, canonical propio, GTM y GA4, Colombia como país inicial. Está en el sitemap y en llms.txt, y se avisó por IndexNow.
- Lógica nueva: si la fecha de hoy ya pasó la vigencia de la tabla "próxima", esa pasa a ser la vigente. Antes mostraba julio como vigente en noviembre.
- Las tarifas están dentro del HTML (`const EMBEDDED`, rate card de Meta tomado el 2-sep-2026). **No se actualizan solas.** Meta cambia tarifas el 1 de enero, abril, julio y octubre: revisar developers.facebook.com/docs/whatsapp/pricing antes del 1-ene-2027 y actualizar `EMBEDDED`.
- Tarifas de Colombia en USD desde el 1-oct-2026: marketing 0,0125; utilidad, autenticación y servicio 0,0008 (primeros 1.000 de servicio al mes gratis).
- Corregido el borrador /blog/precios-whatsapp-api-2026/: tenía 0,0459 y 0,0029, que eran dírhams de Emiratos (AED), no dólares.
