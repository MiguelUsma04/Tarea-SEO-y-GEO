# crmformeta.com: plan SEO, GEO y AEO

Tarea en Soporte: `77b2e52b-efdd-43fa-aeee-ffc14c41a060` ("Ejecutar plan SEO, GEO y AEO de crmformeta.com").
Responsable: Juan Pablo Acosta. Apoyo: María Camila Jaramillo. Aprobación: Carlos Chávez.

Repo de trabajo del plan. Rutas de los comandos relativas a la raíz del repo.

## Carpetas

| Carpeta | Qué tiene |
|---|---|
| `generador/` | `plantilla.py` (HTML, estilos y schema), `paginas.py` (contenido de las páginas AEO), `build.py` (genera), `paginas_legales.py` (/privacidad/ y /garantia/) |
| `publicado/` | Archivos tal como están hoy en el servidor: home, robots.txt, sitemap.xml, llms.txt, .htaccess, páginas legales y borradores |
| `respaldo-2026-11-25/` | Copia del sitio antes de los cambios del 25-nov-2026, sin `*.php` (tienen contraseñas SMTP) ni `/entregables/` (tienen tokens de clientes) |
| `subir.sh` | Sube un archivo al hosting por la API de Hostinger |

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

1. Revisa que la página no tenga bloques amarillos de PENDIENTE: María Camila los completa y Carlos aprueba precios y cifras.
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
