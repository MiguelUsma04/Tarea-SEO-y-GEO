"""/privacidad/ y /garantia/ con la misma plantilla de las páginas AEO.

El texto es el que ya estaba publicado en los modales del home (aprobado).
Uso: python3 paginas_legales.py  -> escribe en ../publicado/
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from plantilla import render  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "publicado")

LEGALES = [
    {
        "slug": "/privacidad/", "crumb": "Política de privacidad", "kind": "page", "draft": False, "hl": "privacidad",
        "title": "Política de privacidad | CRMformeta - Gmarketing",
        "desc": "Cómo Gmarketing S.A.S. y Gmarketing USA LLC tratan los datos personales que recibe por crmformeta.com y cómo consultarlos, corregirlos o eliminarlos.",
        "h1": "Política de privacidad",
        "lead": "Tenemos un especial cuidado en el tratamiento de los datos. Todo el personal con acceso a datos de carácter personal ha recibido la formación necesaria para mantener la total confidencialidad e integridad de los datos de acuerdo a la ley de protección de datos.",
        "sections": [
            {"q": "¿Quién es responsable de los datos?", "faq": False,
             "a": "<strong>Gmarketing S.A.S.</strong>, Calle 26N # 5AN-50, Cali, Colombia, y <strong>Gmarketing USA LLC</strong>, 31 SE 5th St, Apto 3310, Miami, FL 33131, EE. UU. Correo: <a href=\"mailto:comercial@gmarketing.co\">comercial@gmarketing.co</a>. Teléfono y WhatsApp: +57 321 6319137."},
            {"q": "¿Cómo consulto, corrijo o elimino mis datos?", "faq": False,
             "a": "Escribe a <a href=\"mailto:comercial@gmarketing.co\">comercial@gmarketing.co</a> con tu nombre, el teléfono o correo con el que te registraste y la solicitud: consulta, corrección o eliminación."},
        ],
        "cta": ("¿Tienes dudas sobre tus datos o sobre Kommo? Escríbenos o agenda una llamada.", "Agendar diagnóstico gratuito"),
    },
    {
        "slug": "/garantia/", "crumb": "Garantía Kommo10X", "kind": "page", "draft": False, "hl": "Kommo10X",
        "title": "Garantía de la implementación Kommo10X | CRMformeta",
        "desc": "Condiciones de la garantía de 35 días de Kommo10X: métricas, reembolso de la implementación y costos no incluidos como IA en n8n y WhatsApp Cloud API.",
        "h1": "Garantía de la implementación Kommo10X",
        "lead": "Si después de 35 días, y cumpliendo el CLIENTE con todas sus obligaciones, no se alcanzan las métricas definidas, GMARKETING reembolsará el valor del servicio de implementación Kommo10X.",
        "sections": [
            {"q": "¿Qué garantiza la implementación Kommo10X?", "faq": False,
             "a": "Si después de 35 días, y cumpliendo el CLIENTE con todas sus obligaciones, no se alcanzan las métricas definidas, GMARKETING reembolsará el valor del servicio de implementación Kommo10X. Las métricas son:",
             "more": "<ul><li>Mejora de la productividad en un 34%.</li><li>Reducción de los tiempos de respuesta a 10 seg a los prospectos.</li><li>Incremento en las ventas conversacionales en un 10%.</li></ul>"},
            {"q": "¿Qué no cubre la garantía?", "faq": False,
             "a": "Esta garantía no aplica a licencias de usuarios KOMMO ni a causas atribuibles al cliente."},
            {"q": "¿Qué costos no están incluidos en la implementación?", "faq": False,
             "a": "El setup y la parametrización de agentes avanzados de IA con n8n sí están incluidos; sin embargo, el servicio de IA tiene un costo mensual aproximado de <strong>USD $100/mes</strong>, que cubre hosting, soporte y actualizaciones. Este costo aplica en caso de que se requiera activar IA avanzada.",
             "more": "<ul><li>El uso de WhatsApp Cloud API (conversaciones, plantillas y difusiones) no está incluido. El cobro se realiza por conversación iniciada cada 24 horas.</li></ul><p>Más detalles en: <a href=\"https://www.kommo.com/es/precios/\" target=\"_blank\" rel=\"noopener\">Calculadora de Precios Kommo</a>.</p>"},
        ],
    },
]

if __name__ == "__main__":
    for p in LEGALES:
        fp = os.path.join(OUT, p["slug"].strip("/"), "index.html")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w").write(render(p))
        print(p["slug"], "ok")
