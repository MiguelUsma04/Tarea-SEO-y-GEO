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
