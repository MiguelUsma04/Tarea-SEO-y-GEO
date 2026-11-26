# Velocidad de crmformeta.com: línea base (26-nov-2026)

Lighthouse 12.2.1 (laboratorio, conexión simulada). Los datos reales de usuarios (Core Web Vitals) aparecen en Search Console unas 4 semanas después de verificar el sitio. Repetir esta medición en la semana 12.

| URL | Móvil | LCP | TBT | CLS | MB | Escritorio | LCP | TBT | CLS | MB |
|---|---|---|---|---|---|---|---|---|---|---|
| / | 39 | 10.2 s | 4,170 ms | 0 | 17.0 | 62 | 1.7 s | 620 ms | 0 | 28.3 |
| /kommo10x/ | 45 | 10.5 s | 1,180 ms | 0.066 | 8.9 | 91 | 1.6 s | 80 ms | 0.001 | 12.2 |
| /kommo10x/agenda/ | 70 | 5.3 s | 180 ms | 0.002 | 10.2 | 93 | 1.2 s | 0 ms | 0.003 | 12.3 |
| /soluciones_agenticas/ | 95 | 2.3 s | 0 ms | 0 | 0.3 | 95 | 1.1 s | 0 ms | 0.031 | 0.3 |
| /costos_api/ | 73 | 1.7 s | 1,520 ms | 0 | 1.0 | 96 | 0.6 s | 160 ms | 0.003 | 1.0 |
| /garantia/ | 68 | 3.1 s | 1,430 ms | 0 | 1.3 | 96 | 0.9 s | 150 ms | 0 | 1.3 |
| /crm_para_whatsapp/ | 89 | 3.4 s | 70 ms | 0 | 0.9 | 98 | 0.9 s | 0 ms | 0.003 | 0.9 |

Puntaje 0-100 (90+ bueno, 50-89 mejorable, menos de 50 malo). LCP: cuándo aparece el elemento principal (meta: menos de 2,5 s). TBT: tiempo en que la página no responde a toques (meta: menos de 200 ms). CLS: cuánto se mueve el contenido al cargar (meta: menos de 0,1).

## Qué pesa en el home (móvil, 17 MB)

| Origen | MB | Qué es |
|---|---|---|
| crmformeta.com | 4,0 | Imágenes sin tamaño para celular (2,5 MB de ahorro posible) ni formato WebP (0,7 MB) |
| challenges.cloudflare.com | 3,7 | Cloudflare Turnstile (antispam de los formularios), se carga aunque nadie abra el formulario |
| assets.calendly.com | 3,2 | Calendario incrustado en la sección de agenda, se carga al abrir la página |
| vimeocdn.com | 2,8 | Videos de casos de éxito que empiezan a descargar al cargar |
| cdninstagram.com | 1,2 | Publicación de Instagram incrustada |
| googletagmanager.com | 1,0 | GTM y GA4. En páginas livianas como /garantia/ es la causa principal del TBT de 1,4 s |

## Mejoras propuestas (no aplicadas: tocan el home y requieren aprobación)

1. Calendly: cargar el calendario solo cuando la persona llega a la sección o da clic. Ahorro: unos 3 MB.
2. Turnstile: cargarlo cuando se abre el formulario de WhatsApp. Ahorro: unos 3,7 MB.
3. Videos de Vimeo e Instagram: mostrar una miniatura y cargar el reproductor al dar clic. Ahorro: unos 4 MB.
4. Imágenes: versiones WebP y tamaños para celular. Ahorro: unos 3 MB.
5. GTM: revisar las etiquetas del contenedor GTM-TPMR57QR y quitar las que no se usan.

## Después de las mejoras (26-nov-2026, en vivo)

| Medida | Antes (celular) | Después (celular) | Antes (escritorio) | Después (escritorio) |
|---|---|---|---|---|
| Puntaje Lighthouse | 39 | 65-66 | 62 | 84-87 |
| LCP (elemento principal) | 10,2 s | 2,6-2,8 s | 1,7 s | 0,8-1,2 s |
| Peso de la página | 17 MB | 1,8 MB | 28 MB | 13 MB |
| Peticiones al cargar | 182-282 | 42-45 | 181 | 78-90 |

Cambios aplicados al home (`publicado/index.html`, `publicado/script.js`, `publicado/style.css`, `publicado/fonts/*.woff2`):

1. **Videos de casos de éxito:** las 6 tarjetas tenían el atributo `data-vimeo-id`, que `player.js` de Vimeo incrusta solo al cargar: se descargaban 6 reproductores (cada uno con su verificación Turnstile de Vimeo) aunque nadie hiciera clic. Se renombró a `data-gm-video-id`; el video se crea al hacer clic, como estaba pensado.
2. **Calendly:** `widget.js` y el calendario de la sección «Agenda» se cargan cuando la persona se acerca a esa sección o da clic en un botón de agendar (`gmCalendlyPopup`).
3. **Turnstile del formulario de WhatsApp:** se carga al tocar o pasar el cursor sobre el botón de WhatsApp. Si alguien envía antes de que el token esté listo, el botón muestra «Verificando…» y espera hasta 10 s.
4. **Video principal:** se carga cuando entra en pantalla (en celular está debajo del primer pantallazo) y a 720p en lugar de 1080p.
5. **Instagram:** `embed.js` se carga al acercarse a la publicación.
6. **Imágenes:** `loading="lazy"` en las 68 imágenes que no están en el primer pantallazo.
7. **Fuentes:** WOFF2 con subconjunto latino (820 KB → 249 KB), con las OTF como respaldo, y `font-display: swap`.
8. **Etiquetas de Google:** había dos cargas de `gtag.js`; queda una con las tres cuentas configuradas (AW-17840789415, AW-832193848, G-R05L91RDJD). Verificado que las tres siguen enviando datos.

Pendiente: el resto del bloqueo en celular (TBT ~2,3 s) viene de Google Tag Manager (contenedor GTM-TPMR57QR, que además carga G-PGTRZE5XDF) y del píxel de Facebook. Revisar las etiquetas del contenedor con quien lo administra.

Caché: Cloudflare (cuenta de Gmarketing) guarda `style.css`; al cambiarlo, subir el número de versión en el `<link>` del home (`style.css?v=...`), porque desde la API de Hostinger no se puede purgar Cloudflare.
