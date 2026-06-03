#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de sitio HTML estático a partir de un export WordPress (WXR).
Convierte contenido Divi y Gutenberg en HTML limpio, conserva permalinks
y los metadatos SEO de Yoast/RankMath. Genera sitemap.xml y robots.txt.

Uso:
    python3 tools/generar_sitio.py
"""
import os, re, html, sys, glob
from xml.etree import ElementTree as ET
from datetime import datetime

# --- Configuración -----------------------------------------------------------
RAIZ      = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XML       = glob.glob(os.path.join(RAIZ, "origen-wordpress", "export", "*.xml"))
SALIDA    = os.path.join(RAIZ, "web-html")
UPLOADS   = os.path.join(RAIZ, "origen-wordpress", "uploads")
IMG_DIR   = os.path.join(SALIDA, "imagenes")   # imágenes localizadas
PLANTILLA = os.path.join(RAIZ, "plantilla-5", "assets")  # diseño base
DOMINIO   = "https://limpiezaincendiosnanonex.es"   # dominio final (canonical)
NS = {
    "wp":      "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "dc":      "http://purl.org/dc/elements/1.1/",
}

# Navegación principal (etiqueta, ruta)
NAV = [
    ("Inicio", "/"),
    ("Limpieza con láser", "/limpieza-con-laser/"),
    ("Limpieza con hielo seco", "/limpieza-con-hielo-seco/"),
    ("Zonas", "/zonas/"),
    ("Blog", "/blog/"),
    ("Contacto", "/contacto/"),
]

# Datos de contacto / marca (extraídos del WordPress original)
MARCA      = "Nano Nex"
MARCA_FULL = "Limpiezas de Incendios Nano Nex"
TEL        = "632107272"
TEL_FMT    = "632 107 272"
WHATSAPP   = "34632107272"          # wa.me/<este número>
EMAIL      = "info@nano-nex.es"
KEYWORD    = "Limpieza Post Incendio"
HORARIO    = "L-V 7:00-22:00 · Sáb-Dom 8:00-16:00"
OPENING    = ["Mo-Fr 07:00-22:00", "Sa-Su 08:00-16:00"]
GRUPO_URL  = "https://nano-nex.es"

# Términos para variar el enfoque de cada landing y no canibalizar keywords
TERMINOS = [
    ("humo", "eliminación de humo"),
    ("hollín", "limpieza de hollín"),
    ("incendio", "limpieza tras incendio"),
    ("post incendio", "limpieza post incendio"),
]

# Servicios reales de Nano Nex (icono, título, descripción). Solo limpieza/descontaminación.
SERVICIOS = [
    ("🔥", "Limpieza de Incendios y Post-Incendios",
     "Limpieza integral de viviendas y locales tras un incendio: hollín, cenizas y residuos."),
    ("💨", "Desodorización con Ozono",
     "Eliminamos por completo el olor a humo con tratamiento profesional de ozono."),
    ("✨", "Limpieza con Láser",
     "Tecnología láser para limpiar superficies delicadas sin dañar el material original."),
    ("❄️", "Limpieza con Hielo Seco",
     "Limpieza criogénica que elimina residuos sin abrasivos ni agua, ideal para maquinaria."),
    ("🏠", "Síndrome de Diógenes y Acumulación",
     "Limpieza y saneamiento de espacios con acumulación extrema, con total discreción."),
    ("🏭", "Descontaminación Industrial",
     "Equipos especializados para grandes superficies, naves y situaciones complejas."),
]

# ============================================================================
#  Extracción de contenido Divi  ->  HTML limpio
# ============================================================================
def attrs(s):
    return dict(re.findall(r'(\w+)="([^"]*)"', s or ""))

def img_html(a):
    src = a.get("src", "")
    if not src or src.startswith("@ET-DC@"):
        return ""
    alt = a.get("alt") or a.get("title_text") or ""
    return f'<p class="img"><img src="{src}" alt="{html.escape(alt)}" loading="lazy"></p>'

def limpiar_shortcodes(t):
    """Elimina cualquier shortcode Divi residual del texto interno."""
    t = re.sub(r'\[/?et_pb_[^\]]*\]', '', t)
    t = re.sub(r'\[/?[a-z_]+[^\]]*\]', '', t)  # otros shortcodes sueltos
    return t.strip()

def extraer_divi(c):
    """Recorre los módulos Divi en orden y devuelve HTML limpio."""
    trozos = []  # (inicio, fin, html)

    def add(m, htmltxt):
        if htmltxt and htmltxt.strip():
            trozos.append((m.start(), m.end(), htmltxt))

    # Texto
    for m in re.finditer(r'\[et_pb_text[^\]]*\](.*?)\[/et_pb_text\]', c, re.S):
        add(m, limpiar_shortcodes(m.group(1)))
    # Imágenes
    for m in re.finditer(r'\[et_pb_image([^\]]*)\]', c, re.S):
        add(m, img_html(attrs(m.group(1))))
    # Blurbs (icono/imagen + título + texto)
    for m in re.finditer(r'\[et_pb_blurb([^\]]*)\](.*?)\[/et_pb_blurb\]', c, re.S):
        a = attrs(m.group(1)); h = ""
        if a.get("title"): h += f"<h3>{html.escape(a['title'])}</h3>"
        h += img_html(a) + limpiar_shortcodes(m.group(2))
        add(m, h)
    # Cabeceras / slides / título de entrada
    for m in re.finditer(r'\[(et_pb_fullwidth_header|et_pb_slide|et_pb_post_title)([^\]]*)\](.*?)\[/\1\]', c, re.S):
        a = attrs(m.group(2)); h = ""
        if a.get("title"):    h += f"<h1>{html.escape(a['title'])}</h1>"
        if a.get("subhead"):  h += f"<p class='sub'>{html.escape(a['subhead'])}</p>"
        if a.get("heading"):  h += f"<h2>{html.escape(a['heading'])}</h2>"
        h += limpiar_shortcodes(m.group(3))
        add(m, h)
    # CTA
    for m in re.finditer(r'\[et_pb_cta([^\]]*)\](.*?)\[/et_pb_cta\]', c, re.S):
        a = attrs(m.group(1)); h = ""
        if a.get("title"): h += f"<h2>{html.escape(a['title'])}</h2>"
        h += limpiar_shortcodes(m.group(2))
        if a.get("button_text") and a.get("button_url"):
            h += f'<p><a class="btn" href="{a["button_url"]}">{html.escape(a["button_text"])}</a></p>'
        add(m, f'<div class="cta">{h}</div>')
    # Botones
    for m in re.finditer(r'\[et_pb_button([^\]]*)\]', c, re.S):
        a = attrs(m.group(1))
        if a.get("button_text") and a.get("button_url"):
            add(m, f'<p><a class="btn" href="{a["button_url"]}">{html.escape(a["button_text"])}</a></p>')
    # Contador
    for m in re.finditer(r'\[et_pb_number_counter([^\]]*)\]', c, re.S):
        a = attrs(m.group(1))
        if a.get("number"):
            add(m, f'<div class="counter"><span class="num">{html.escape(a["number"])}</span> {html.escape(a.get("title",""))}</div>')
    # Código embebido
    for m in re.finditer(r'\[(et_pb_code|et_pb_fullwidth_code)[^\]]*\](.*?)\[/\1\]', c, re.S):
        add(m, m.group(2))
    # Formulario de contacto -> formulario simple
    for m in re.finditer(r'\[et_pb_contact_form[^\]]*\]', c, re.S):
        add(m, FORM_CONTACTO)

    # Ordenar por posición y descartar solapados (anidados)
    trozos.sort()
    salida, ult = [], -1
    for ini, fin, h in trozos:
        if ini >= ult:
            salida.append(h); ult = fin
    out = "\n".join(salida)
    # Limpiar marcadores de salto de línea propios de Divi
    out = re.sub(r'<!--\s*\[et_pb_line_break_holder\]\s*-->', '\n', out)
    out = out.replace('[et_pb_line_break_holder]', '\n')
    return out

FORM_CONTACTO = """<form class="contacto" method="post" action="#">
  <label>Nombre<input type="text" name="nombre" required></label>
  <label>Email<input type="email" name="email" required></label>
  <label>Teléfono<input type="tel" name="telefono"></label>
  <label>Mensaje<textarea name="mensaje" rows="5" required></textarea></label>
  <button type="submit" class="btn">Enviar</button>
</form>"""

def limpiar_gutenberg(c):
    """Quita comentarios de bloque Gutenberg y shortcodes [caption]."""
    c = re.sub(r'<!--\s*/?wp:[^>]*-->', '', c)
    c = re.sub(r'\[caption[^\]]*\](.*?)\[/caption\]', r'\1', c, flags=re.S)
    c = re.sub(r'\[/?[a-z_]+[^\]]*\]', '', c)
    return c.strip()

def texto_a_parrafos(c):
    """Para contenido en texto plano: convierte dobles saltos en <p>."""
    if re.search(r'<(p|h[1-6]|ul|ol|div|figure|img|table)\b', c, re.I):
        return c
    bloques = [b.strip() for b in re.split(r'\n\s*\n', c) if b.strip()]
    return "\n".join(f"<p>{b}</p>" for b in bloques)

_REEMPLAZOS_LIMPIEZA = [
    (r'\brestauraci[oó]n\b', 'limpieza'), (r'\brehabilitaci[oó]n\b', 'limpieza'),
    (r'\breparaci[oó]n\b', 'limpieza'), (r'\breformas\b', 'limpiezas'),
    (r'\breforma\b', 'limpieza'),
    (r'\brestaurar\b', 'limpiar'), (r'\brehabilitar\b', 'limpiar'),
    (r'\breparar\b', 'limpiar'), (r'\breformar\b', 'limpiar'),
    (r'\brestauramos\b', 'limpiamos'), (r'\breparamos\b', 'limpiamos'),
    (r'\breformamos\b', 'limpiamos'), (r'\brehabilitamos\b', 'limpiamos'),
]
def solo_limpieza(htmltxt):
    """Sustituye verbos de reparación/reforma por limpieza, SOLO en texto visible
    (entre tags), respetando URLs, atributos y la palabra 'restaurantes'."""
    def _txt(seg):
        for pat, rep in _REEMPLAZOS_LIMPIEZA:
            seg = re.sub(pat, rep, seg, flags=re.I)
        return seg
    return re.sub(r'>([^<]+)<', lambda m: '>' + _txt(m.group(1)) + '<', htmltxt)

def convertir(contenido):
    if not contenido:
        return ""
    if "[et_pb_" in contenido:
        html_out = extraer_divi(contenido)
    else:
        html_out = texto_a_parrafos(limpiar_gutenberg(contenido))
    return solo_limpieza(html_out)

# ============================================================================
#  Localización de imágenes (URLs en vivo -> archivos locales subidos)
# ============================================================================
import shutil

def _clave_img(nombre):
    s = os.path.splitext(nombre)[0].lower()
    s = re.sub(r'-\d+x\d+', '', s)            # quitar -1024x576
    s = re.sub(r'-(copia|scaled)', '', s)
    s = re.sub(r'-\d+$', '', s)               # sufijo numérico final
    return re.sub(r'[^a-z0-9]+', '', s)

def cargar_indice_imgs():
    """Devuelve {clave_normalizada: nombre_archivo} de los uploads disponibles."""
    if not os.path.isdir(UPLOADS):
        return {}
    idx = {}
    for f in sorted(os.listdir(UPLOADS)):
        if f.startswith('.'):
            continue
        idx.setdefault(_clave_img(f), f)
    return idx

IDX_IMG = cargar_indice_imgs()
_COPIADAS = set()
LOC = {"ok": set(), "falta": set()}

def localizar_imgs(cuerpo, prefijo):
    """Reescribe los <img src> en vivo a rutas locales cuando hay archivo."""
    patron = re.compile(r'(https://limpiezaincendiosnanonex\.es/wp-content/uploads/([^"\']+))')
    def _sub(m):
        url, resto = m.group(1), m.group(2)
        base = os.path.basename(resto)
        local = IDX_IMG.get(_clave_img(base))
        if not local:
            LOC["falta"].add(base)
            return url  # se queda en vivo
        if local not in _COPIADAS:
            os.makedirs(IMG_DIR, exist_ok=True)
            shutil.copy2(os.path.join(UPLOADS, local), os.path.join(IMG_DIR, local))
            _COPIADAS.add(local)
        LOC["ok"].add(base)
        return f"{prefijo}imagenes/{local}"
    return patron.sub(_sub, cuerpo)

# ============================================================================
#  Plantilla HTML
# ============================================================================
def primer_texto(htmltxt, n=160):
    t = re.sub(r'<[^>]+>', ' ', htmltxt)
    t = html.unescape(re.sub(r'\s+', ' ', t)).strip()
    return (t[:n].rsplit(' ', 1)[0] + '…') if len(t) > n else t

def prefijo_rel(ruta):
    """Prefijo relativo a la raíz según la profundidad de la ruta."""
    d = len([s for s in ruta.split("/") if s])
    return "../" * d

def rel(path, prefijo):
    """Convierte una ruta absoluta '/x/' en relativa según el prefijo."""
    return (prefijo + path.lstrip("/")) or "./"

def _topbar():
    return ('<div class="topbar"><div class="container">'
            '<span>📞 <a href="tel:' + TEL + '">' + TEL_FMT + '</a></span>'
            '<span class="topbar-claim">Operativos 24/7 · Limpieza profesional 365 días</span>'
            '<span class="topbar-hor">🕒 ' + HORARIO + '</span>'
            '</div></div>')

def _cabecera(pf, activo):
    def _enlace(e, r):
        cls = ' class="act"' if r == activo else ''
        return f'<li><a href="{rel(r, pf)}"{cls}>{html.escape(e)}</a></li>'
    items = "".join(_enlace(e, r) for e, r in NAV)
    return f"""{_topbar()}
<header class="header">
  <div class="container">
    <a href="{rel('/', pf)}" class="logo">Nano<span>Nex</span></a>
    <nav class="nav">
      <ul class="nav-list">{items}</ul>
      <a href="tel:{TEL}" class="btn btn-call">{TEL_FMT}</a>
    </nav>
    <button class="hamburger" aria-label="Abrir menú"><span></span><span></span><span></span></button>
  </div>
</header>"""

def _wa_svg(cls):
    return (f'<svg class="{cls}" viewBox="0 0 32 32" aria-hidden="true" width="26" height="26">'
            '<path fill="currentColor" d="M16 .4A15.6 15.6 0 0 0 2.7 24l-2.3 8.4 8.6-2.3A15.6 15.6 0 1 0 16 .4zm0 28.4a12.8 12.8 0 0 1-6.5-1.8l-.5-.3-4.9 1.3 1.3-4.8-.3-.5A12.8 12.8 0 1 1 16 28.8zm7-9.6c-.4-.2-2.3-1.1-2.6-1.3s-.6-.2-.9.2-1 1.3-1.2 1.5-.4.3-.8.1a10.5 10.5 0 0 1-3.1-1.9 11.6 11.6 0 0 1-2.1-2.7c-.2-.4 0-.6.2-.8l.6-.7.4-.7a.7.7 0 0 0 0-.7c0-.2-.9-2.1-1.2-2.9s-.6-.7-.9-.7h-.7a1.4 1.4 0 0 0-1 .5 4.2 4.2 0 0 0-1.3 3.1 7.3 7.3 0 0 0 1.5 3.9 16.7 16.7 0 0 0 6.4 5.7c.9.4 1.6.6 2.1.8a5.1 5.1 0 0 0 2.3.1c.7-.1 2.3-.9 2.6-1.8s.3-1.6.2-1.8-.3-.2-.7-.4z"/></svg>')

def _flotantes_y_barra(pf):
    wa = f"https://wa.me/{WHATSAPP}"
    return f"""<!-- Botones flotantes (escritorio) -->
<div class="float-btns">
  <a href="{wa}" class="float-wa" target="_blank" rel="noopener" aria-label="WhatsApp">{_wa_svg('wa-ic')}</a>
  <a href="tel:{TEL}" class="float-call" aria-label="Llamar">📞</a>
</div>
<!-- Barra inferior (móvil) -->
<div class="mobile-cta-bar">
  <a href="tel:{TEL}" class="btn-mobile-call">📞 Llamar</a>
  <a href="{wa}" class="btn-mobile-wa" target="_blank" rel="noopener">{_wa_svg('wa-ic')} WhatsApp</a>
  <a href="{rel('/contacto/', pf)}" class="btn-mobile-quote">✉️ Presupuesto</a>
</div>"""

def _cookie_banner(pf):
    return ('<div id="cookie-banner" class="cookie-banner" hidden>'
            '<p>Usamos cookies propias y de terceros para mejorar tu experiencia. '
            f'<a href="{rel("/politica-de-cookies/", pf)}">Más información</a>.</p>'
            '<button id="cookie-ok" class="btn btn-primary">Aceptar</button></div>')

def _pie(pf):
    enl = "".join(f'<li><a href="{rel(r, pf)}">{html.escape(e)}</a></li>'
                  for e, r in NAV if r not in ("/",))
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer-col">
      <h3>{MARCA_FULL}</h3>
      <p>Especialistas en {KEYWORD.lower()}: limpieza y descontaminación de viviendas y locales tras un incendio. Más de 30 años de experiencia.</p>
      <p>🕒 {HORARIO}</p>
      <div class="social-links"><a href="#" aria-label="Facebook">F</a><a href="#" aria-label="Instagram">I</a><a href="#" aria-label="Twitter">T</a></div>
    </div>
    <div class="footer-col">
      <h3>Enlaces</h3>
      <ul>{enl}</ul>
    </div>
    <div class="footer-col">
      <h3>Contacto</h3>
      <ul>
        <li><a href="tel:{TEL}">📞 {TEL_FMT}</a></li>
        <li><a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">💬 WhatsApp</a></li>
        <li><a href="mailto:{EMAIL}">✉️ {EMAIL}</a></li>
        <li><a href="{rel('/politica-de-privacidad/', pf)}">Política de privacidad</a></li>
        <li><a href="{rel('/politica-de-cookies/', pf)}">Política de cookies</a></li>
        <li><a href="{rel('/aviso-legal/', pf)}">Aviso legal</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; <span id="currentYear">{datetime.now().year}</span> {MARCA_FULL}. Todos los derechos reservados.</p>
    <p class="grupo">{MARCA_FULL} forma parte del <a href="{GRUPO_URL}" target="_blank" rel="noopener">Grupo Nano Nex</a>.</p>
  </div>
</footer>
{_flotantes_y_barra(pf)}
{_cookie_banner(pf)}"""

def _schema_local(ciudad, canonical):
    loc = ciudad or "tu localidad"
    horario = ",".join(f'"{h}"' for h in OPENING)
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"LocalBusiness","name":"{MARCA_FULL}",
"@id":"{DOMINIO}/#organization","url":"{canonical}","telephone":"+34{TEL}",
"email":"{EMAIL}","priceRange":"€€","areaServed":"{html.escape(loc)}",
"openingHours":[{horario}],
"address":{{"@type":"PostalAddress","addressLocality":"{html.escape(loc)}","addressCountry":"ES"}}}}
</script>"""

def _schema_home(canonical):
    horario = ",".join(f'"{h}"' for h in OPENING)
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[
{{"@type":"Organization","@id":"{DOMINIO}/#organization","name":"{MARCA_FULL}","url":"{DOMINIO}/",
"telephone":"+34{TEL}","email":"{EMAIL}","sameAs":["{GRUPO_URL}"],
"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"127","bestRating":"5"}}}},
{{"@type":"WebSite","@id":"{DOMINIO}/#website","url":"{DOMINIO}/","name":"{MARCA_FULL}","publisher":{{"@id":"{DOMINIO}/#organization"}}}},
{{"@type":"LocalBusiness","name":"{MARCA_FULL}","url":"{DOMINIO}/","telephone":"+34{TEL}","priceRange":"€€","openingHours":[{horario}]}}
]}}
</script>"""

def _schema_breadcrumb(titulo, canonical):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Inicio","item":"{DOMINIO}/"}},
{{"@type":"ListItem","position":2,"name":"{html.escape(titulo)}","item":"{canonical}"}}]}}
</script>"""

def plantilla(titulo, descripcion, canonical, cuerpo, ruta_actual,
              nav_activo=None, schema=None, pf_override=None):
    pf = pf_override if pf_override is not None else prefijo_rel(ruta_actual)
    activo = nav_activo or ruta_actual
    desc = html.escape(descripcion or "")
    og_img = f"{DOMINIO}/assets/img/hero.webp"
    schema_html = schema or ""
    fuentes = "https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&display=swap"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{pf}assets/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{MARCA_FULL}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(titulo)}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_img}">
{schema_html}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{pf}assets/css/style.css">
<link rel="preload" as="style" href="{fuentes}">
<link href="{fuentes}" rel="stylesheet">
<link rel="stylesheet" href="{pf}assets/css/style.css">
<link rel="stylesheet" href="{pf}assets/css/contenido.css">
<noscript><style>.reveal{{opacity:1!important;transform:none!important}}</style></noscript>
</head>
<body>
{_cabecera(pf, activo)}
<main>
{cuerpo}
</main>
{_pie(pf)}
<script src="{pf}assets/js/main.js"></script>
</body>
</html>"""

# ============================================================================
#  Constructores de cuerpo: landing (plantilla-5) y artículo
# ============================================================================
def ciudad_de(titulo):
    """Devuelve la ciudad de una página tipo 'Limpiezas de Incendios <Ciudad>'."""
    m = re.search(r'[Ii]ncendios?\s+(.+)$', titulo or "")
    if not m:
        return None
    c = m.group(1).strip()
    if "nano" in c.lower():
        return None
    return c

def _tarjetas_servicios():
    return "".join(
        f'<div class="servicio-card reveal"><div class="icon">{ic}</div>'
        f'<h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div>'
        for ic, t, d in SERVICIOS)

def _zonas_grid(ciudades, pf):
    return "".join(
        f'<a href="{rel(r, pf)}">{html.escape(ciudad_de(t) or t)}</a>'
        for t, r in ciudades)

def secciones_landing(h1, intro, contenido_real, ciudades, pf, ciudad=None):
    lugar = ciudad or "tu población"
    en_lugar = f"en {lugar}" if ciudad else "en tu zona"
    # Variación de término según la ciudad (evita canibalización de keywords)
    idx = sum(ord(c) for c in (ciudad or "home")) % len(TERMINOS)
    termino, termino_largo = TERMINOS[idx]
    alt_base = f"{KEYWORD} {en_lugar}"
    bloque_real = ""
    if contenido_real and len(re.sub(r'<[^>]+>', '', contenido_real)) > 200:
        bloque_real = f"""
<section class="contenido-wp section-padding">
  <div class="container">
    <article class="reveal">{contenido_real}</article>
  </div>
</section>"""
    return f"""
<section class="hero">
  <div class="hero-overlay"></div>
  <div class="container">
    <span class="badge-urgencia">¡Servicio de Urgencia 24/7!</span>
    <h1>{html.escape(h1)}</h1>
    <p>{html.escape(intro)}</p>
    <div class="hero-ctas">
      <a href="#contacto" class="btn btn-primary">Solicitar Presupuesto Gratuito</a>
      <a href="tel:{TEL}" class="btn btn-secondary">Llamar Ahora</a>
    </div>
    <div class="trust-signals">
      <p>✅ Más de 30 años de experiencia</p>
      <p>✅ Servicio profesional 365 días</p>
      <p>✅ Presupuesto sin compromiso</p>
    </div>
  </div>
</section>

<section class="stats section-padding">
  <div class="container">
    <div class="stat-item"><span class="stat-number" data-counter="30">0</span>+<p>Años de Experiencia</p></div>
    <div class="stat-item"><span class="stat-number" data-counter="500">0</span>+<p>Intervenciones Completadas</p></div>
    <div class="stat-item"><span class="stat-number" data-counter="98">0</span>%<p>Clientes Satisfechos</p></div>
    <div class="stat-item"><span class="stat-number" data-counter="24">0</span>/<span class="stat-number" data-counter="7">0</span><p>Servicio de Urgencia</p></div>
  </div>
</section>

<section id="servicios" class="servicios section-padding">
  <div class="container">
    <h2 class="section-title">Servicios de {KEYWORD} {en_lugar}</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Especialistas en {termino_largo}: limpieza y descontaminación de tu espacio {en_lugar}.</p>
    <div class="servicios-grid">{_tarjetas_servicios()}</div>
  </div>
</section>
{bloque_real}
<section class="before-after section-padding">
  <div class="container">
    <h2 class="section-title">Resultados que Hablan por Sí Solos</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Dejamos tu vivienda o local libre de {termino}, hollín y olores.</p>
    <div class="before-after-content">
      <div class="before-after-image"><img src="{pf}assets/img/resultado.svg" alt="{html.escape(alt_base)}: resultado de la limpieza" loading="lazy"></div>
      <div class="before-after-checklist">
        <h3>Nuestro Compromiso:</h3>
        <ul>
          <li>✅ Eliminación total de hollín y ceniza</li>
          <li>✅ Neutralización completa de olores con ozono</li>
          <li>✅ Limpieza profunda de superficies afectadas</li>
          <li>✅ Desinfección y saneamiento</li>
          <li>✅ Limpieza de objetos de valor</li>
          <li>✅ Entrega de espacios listos para usar</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="proceso" class="proceso section-padding">
  <div class="container">
    <h2 class="section-title">Nuestro Proceso de Limpieza</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Un enfoque metódico para garantizar la máxima eficacia.</p>
    <div class="proceso-grid">
      <div class="proceso-item reveal"><div class="proceso-icon">1</div><h3>Evaluación y Planificación</h3><p>Inspección detallada del alcance y plan de limpieza personalizado.</p></div>
      <div class="proceso-item reveal"><div class="proceso-icon">2</div><h3>Contención y Protección</h3><p>Aislamiento de áreas afectadas para evitar la propagación de contaminantes.</p></div>
      <div class="proceso-item reveal"><div class="proceso-icon">3</div><h3>Limpieza y Desodorización</h3><p>Técnicas avanzadas para eliminar hollín, humo y olores.</p></div>
      <div class="proceso-item reveal"><div class="proceso-icon">4</div><h3>Descontaminación Final</h3><p>Saneamiento y entrega de un espacio limpio y listo para usar.</p></div>
    </div>
    <div class="proceso-image"><img src="{pf}assets/img/proceso.svg" alt="{html.escape(alt_base)}: proceso de limpieza" loading="lazy"></div>
  </div>
</section>

<section id="equipo" class="equipo section-padding">
  <div class="container">
    <h2 class="section-title">Nuestro Equipo de Expertos</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Profesionales cualificados y comprometidos con tu tranquilidad.</p>
    <div class="equipo-content">
      <div class="equipo-image"><img src="{pf}assets/img/equipo.svg" alt="{html.escape(alt_base)}: equipo profesional" loading="lazy"></div>
      <div class="equipo-metrics">
        <div class="metric-item"><span class="metric-number" data-counter="20">0</span>+<p>Especialistas</p></div>
        <div class="metric-item"><span class="metric-number" data-counter="100">0</span>%<p>Formación Continua</p></div>
        <div class="metric-item"><span class="metric-number" data-counter="5">0</span>/5<p>Valoración Media</p></div>
        <div class="metric-item"><span class="metric-number" data-counter="24">0</span>/<span class="metric-number" data-counter="7">0</span><p>Disponibilidad</p></div>
      </div>
    </div>
  </div>
</section>

<section id="testimonios" class="testimonios section-padding">
  <div class="container">
    <h2 class="section-title">Lo que Dicen Nuestros Clientes</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Opiniones de clientes {en_lugar} y alrededores.</p>
    <div class="testimonios-grid">
      <div class="testimonio-card reveal"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Nano Nex salvó mi negocio. La limpieza fue impecable y el olor a humo desapareció por completo."</p><span class="client-name">- María G.</span></div>
      <div class="testimonio-card reveal"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Profesionalidad y eficiencia. Tras el incendio en mi casa dejaron todo limpio y sin olores."</p><span class="client-name">- Juan P.</span></div>
      <div class="testimonio-card reveal"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Desde el primer contacto hasta la finalización, todo fue excelente. Un servicio de primera."</p><span class="client-name">- Ana R.</span></div>
    </div>
  </div>
</section>

<section id="zonas" class="zonas section-padding">
  <div class="container">
    <h2 class="section-title">Otras Zonas de Servicio</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">{KEYWORD} cerca de ti. Estas son otras poblaciones donde actuamos:</p>
    <div class="zonas-grid">{_zonas_grid(ciudades, pf)}</div>
  </div>
</section>

{seccion_contacto(pf, ciudad)}"""

def seccion_contacto(pf, ciudad=None):
    lugar = ciudad or "tu población"
    return f"""<section id="contacto" class="contacto section-padding">
  <div class="container">
    <h2 class="section-title">Nosotros te llamamos</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Déjanos tus datos y te llamamos para darte presupuesto sin compromiso. Disponibles 24/7.</p>
    <div class="contact-content">
      <div class="contact-info">
        <h3>Información de Contacto</h3>
        <p>📞 Teléfono: <a href="tel:{TEL}">{TEL_FMT}</a></p>
        <p>💬 WhatsApp: <a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">{TEL_FMT}</a></p>
        <p>📧 Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>🕒 Horario: {HORARIO}</p>
      </div>
      <div class="contact-form">
        <h3>Te llamamos gratis</h3>
        <p class="form-lead">Rellena estos 3 datos y te llamamos en menos de 24 h.</p>
        <form id="contactForm" action="https://formsubmit.co/{EMAIL}" method="POST">
          <input type="hidden" name="_subject" value="Nueva solicitud · {KEYWORD} ({html.escape(lugar)})">
          <input type="hidden" name="Origen" value="{DOMINIO} · {html.escape(lugar)}">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <input type="text" name="_honey" style="display:none">
          <div class="form-group"><label for="name">Nombre</label><input type="text" id="name" name="Nombre" placeholder="Tu nombre" autocomplete="name" required></div>
          <div class="form-group"><label for="phone">Teléfono</label><input type="tel" id="phone" name="Telefono" placeholder="Ej. 600 123 456" autocomplete="tel" inputmode="tel" required></div>
          <div class="form-group"><label for="city">Población</label><input type="text" id="city" name="Poblacion" placeholder="Tu población" value="{html.escape(ciudad or '')}" autocomplete="address-level2" required></div>
          <button type="submit" class="btn btn-primary">📞 Quiero que me llaméis</button>
          <p class="form-foot">🔒 Sin compromiso. Al enviar aceptas nuestra <a href="{rel('/politica-de-privacidad/', pf)}">política de privacidad</a>.</p>
          <div id="formMessage" class="form-message"></div>
        </form>
      </div>
    </div>
  </div>
</section>"""

def articulo(titulo, cuerpo, fecha=None):
    meta = f'<p class="post-meta">Publicado el {fecha}</p>' if fecha else ''
    return f"""
<section class="page-hero">
  <div class="container"><h1>{html.escape(titulo)}</h1></div>
</section>
<section class="contenido-wp section-padding">
  <div class="container"><article>{meta}{cuerpo}</article></div>
</section>"""

# ============================================================================
#  Copia de assets de la plantilla + CSS complementario para el contenido
# ============================================================================
CONTENIDO_CSS = """/* Estilos para el contenido importado de WordPress y páginas de artículo */
.page-hero{background:var(--color-dark-green);color:var(--color-cream);
  padding:130px 0 50px;text-align:center}
.page-hero h1{font-family:var(--font-playfair);color:#fff;font-size:2.4rem;margin:0 0 10px}
.page-hero p{color:var(--color-cream);max-width:760px;margin:0 auto;opacity:.9}
.contenido-wp{background:var(--color-cream)}
.contenido-wp .container{max-width:1100px}
.contenido-wp article{max-width:880px;margin:0 auto;background:#fff;padding:40px 46px;
  border-radius:14px;box-shadow:0 10px 40px rgba(10,22,40,.08);line-height:1.75;color:#243}
.contenido-wp article h1,.contenido-wp article h2,.contenido-wp article h3{
  font-family:var(--font-playfair);color:var(--color-dark-green);line-height:1.25;margin:1.4em 0 .5em}
.contenido-wp article h2{font-size:1.7rem;border-bottom:2px solid var(--color-gold);padding-bottom:.2em}
.contenido-wp article h3{font-size:1.3rem}
.contenido-wp article p{margin:0 0 1.1em}
.contenido-wp article a{color:var(--color-gold);font-weight:600}
.contenido-wp article ul,.contenido-wp article ol{margin:0 0 1.2em 1.2em}
.contenido-wp article li{margin:.35em 0}
.contenido-wp article img{max-width:100%;height:auto;border-radius:10px;margin:1.2em 0;display:block}
.contenido-wp article .btn{display:inline-block;background:var(--color-gold);color:var(--color-dark-green);
  padding:12px 26px;border-radius:50px;font-weight:700;margin:.4em 0}
.contenido-wp article .btn:hover{background:#b89640}
.post-meta{color:#8a7a55;font-size:.9rem;margin-bottom:1.5em}
/* Rejilla de zonas como enlaces */
.zonas-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px}
.zonas-grid a{display:block;background:var(--color-light-dark-green);color:var(--color-cream);
  padding:16px;border-radius:10px;text-align:center;font-weight:600;transition:.25s;
  border:1px solid rgba(201,168,76,.3)}
.zonas-grid a:hover{background:var(--color-gold);color:var(--color-dark-green)}
/* Rejilla del blog */
.blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:22px;max-width:1100px;margin:0 auto}
.blog-card{display:block;background:#fff;border-radius:12px;padding:24px;text-decoration:none;
  box-shadow:0 8px 30px rgba(10,22,40,.08);transition:.25s;border-top:4px solid var(--color-gold)}
.blog-card:hover{transform:translateY(-5px);box-shadow:0 14px 40px rgba(10,22,40,.15)}
.blog-card .blog-fecha{color:var(--color-gold);font-size:.82rem;font-weight:700;text-transform:uppercase}
.blog-card h3{font-family:var(--font-playfair);color:var(--color-dark-green);margin:.5em 0 0;font-size:1.15rem;line-height:1.35}
/* Topbar */
.topbar{background:var(--color-dark-green);color:var(--color-cream);font-size:.85rem;border-bottom:1px solid rgba(201,168,76,.25)}
.topbar .container{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:7px 20px;flex-wrap:wrap}
.topbar a{color:var(--color-gold);font-weight:700}
.topbar-claim{font-weight:700;color:#fff}
/* Botones flotantes (escritorio) */
.float-btns{position:fixed;right:18px;bottom:22px;z-index:900;display:flex;flex-direction:column;gap:12px}
.float-btns a{width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:1.5rem;box-shadow:0 6px 20px rgba(0,0,0,.3);color:#fff;transition:transform .2s}
.float-btns a:hover{transform:scale(1.08)}
.float-wa{background:#25D366}
.float-call{background:var(--color-gold);color:var(--color-dark-green)!important}
.wa-ic{display:block}
/* Barra inferior móvil */
.mobile-cta-bar{position:fixed;left:0;right:0;bottom:0;z-index:950;display:none;
  background:var(--color-dark-green);border-top:2px solid var(--color-gold)}
.mobile-cta-bar a{flex:1;display:flex;align-items:center;justify-content:center;gap:6px;
  padding:13px 4px;color:#fff;font-weight:700;font-size:.92rem}
.mobile-cta-bar .btn-mobile-wa{background:#25D366}
.mobile-cta-bar .btn-mobile-quote{background:var(--color-gold);color:var(--color-dark-green)}
.mobile-cta-bar .wa-ic{width:20px;height:20px}
/* Grupo Nano Nex */
.footer-bottom .grupo{font-size:.85rem;opacity:.85;margin-top:6px}
.footer-bottom .grupo a{color:var(--color-gold);font-weight:700}
/* Banner cookies */
.cookie-banner{position:fixed;left:14px;right:14px;bottom:14px;z-index:980;background:var(--color-dark-green);
  color:var(--color-cream);padding:14px 18px;border-radius:12px;display:flex;align-items:center;gap:14px;
  box-shadow:0 10px 40px rgba(0,0,0,.35);max-width:780px;margin:0 auto;flex-wrap:wrap;justify-content:center}
.cookie-banner p{margin:0;font-size:.9rem}.cookie-banner a{color:var(--color-gold)}
.cookie-banner .btn{padding:9px 20px;font-size:.9rem}
/* Mejora estética del formulario de contacto */
.contacto{background:linear-gradient(160deg,#0A1628 0%,#13315C 100%)}
.contact-form{border-top:4px solid var(--color-gold);box-shadow:0 18px 50px rgba(0,0,0,.35)}
.contact-info{box-shadow:0 18px 50px rgba(0,0,0,.25)}
.contact-form .form-lead{color:var(--color-cream);opacity:.85;margin:-10px 0 22px;font-size:.95rem}
.form-group{margin-bottom:16px}
.form-group label{font-size:.78rem;letter-spacing:.4px;text-transform:uppercase;opacity:.9;margin-bottom:6px}
.form-group input{padding:14px 16px;border-radius:10px;border:1px solid rgba(201,168,76,.45);
  background:rgba(255,255,255,.06);color:var(--color-cream);transition:border-color .2s,box-shadow .2s,background .2s}
.form-group input::placeholder{color:rgba(253,246,233,.45)}
.form-group input:focus{border-color:var(--color-gold);background:rgba(255,255,255,.1);
  box-shadow:0 0 0 3px rgba(201,168,76,.22)}
.contact-form .btn-primary{border-radius:50px;margin-top:6px;letter-spacing:.3px;
  box-shadow:0 8px 24px rgba(201,168,76,.35)}
.contact-form .form-foot{font-size:.78rem;opacity:.7;text-align:center;margin:14px 0 0}
.contact-form .form-foot a{color:var(--color-gold)}
@media(max-width:768px){
  .page-hero h1{font-size:1.8rem}.contenido-wp article{padding:26px 20px}
  .float-btns{display:none}
  .mobile-cta-bar{display:flex}
  body{padding-bottom:58px}
  .topbar-hor{display:none}
  .topbar .container{justify-content:center;font-size:.8rem}
  /* El banner de cookies no se monta sobre la barra inferior */
  .cookie-banner{bottom:66px;left:8px;right:8px;padding:11px 14px;gap:10px}
  .cookie-banner p{font-size:.82rem}
  .contact-info,.contact-form{padding:26px 22px;min-width:0}
}
"""

def _placeholder_svg(label, sub):
    """Imagen propia (sin logo de terceros) con la identidad Nano Nex."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img" aria-label="{html.escape(label)}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#0A1628"/><stop offset="1" stop-color="#13315C"/></linearGradient></defs>
<rect width="800" height="520" fill="url(#g)"/>
<rect x="18" y="18" width="764" height="484" rx="18" fill="none" stroke="#C9A84C" stroke-width="2" opacity=".6"/>
<circle cx="400" cy="200" r="74" fill="none" stroke="#C9A84C" stroke-width="4"/>
<text x="400" y="226" font-family="Georgia,serif" font-size="62" font-weight="700" text-anchor="middle" fill="#C9A84C">NN</text>
<text x="400" y="330" font-family="Georgia,serif" font-size="40" font-weight="700" text-anchor="middle" fill="#FdF6E9">Nano Nex</text>
<text x="400" y="372" font-family="Arial,sans-serif" font-size="22" text-anchor="middle" fill="#C9A84C" letter-spacing="1">{html.escape(label)}</text>
<text x="400" y="412" font-family="Arial,sans-serif" font-size="16" text-anchor="middle" fill="#FdF6E9" opacity=".75">{html.escape(sub)}</text>
</svg>"""

PLACEHOLDERS = {
    "equipo.svg":    ("Equipo profesional", "Técnicos especializados en limpieza post incendio"),
    "proceso.svg":   ("Proceso de limpieza", "Hollín · humo · desodorización con ozono"),
    "resultado.svg": ("Resultado final", "Espacios limpios y libres de olores"),
}

FAVICON_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<rect width="64" height="64" rx="12" fill="#0A1628"/>'
    '<text x="32" y="44" font-family="Georgia,serif" font-size="34" font-weight="700" '
    'text-anchor="middle" fill="#C9A84C">NN</text></svg>')

MAIN_JS = """document.addEventListener("DOMContentLoaded",()=>{
  // Menú hamburguesa
  const h=document.querySelector(".hamburger"),n=document.querySelector(".nav");
  if(h&&n){h.addEventListener("click",()=>{n.classList.toggle("active");h.classList.toggle("active");});
    document.querySelectorAll(".nav-list a").forEach(l=>l.addEventListener("click",()=>{n.classList.remove("active");h.classList.remove("active");}));}
  // Scroll suave solo para anclas internas (no rompe navegación entre páginas)
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener("click",function(e){const id=this.getAttribute("href");if(id.length>1){const t=document.querySelector(id);if(t){e.preventDefault();t.scrollIntoView({behavior:"smooth"});}}});
  });
  // Año dinámico
  const y=document.getElementById("currentYear");if(y)y.textContent=new Date().getFullYear();
  // Reveal al hacer scroll (umbral 0: aparece en cuanto entra, también en textos largos)
  const reveals=document.querySelectorAll(".reveal");
  const io=new IntersectionObserver((es,o)=>{es.forEach(en=>{if(en.isIntersecting){en.target.classList.add("active");o.unobserve(en.target);}});},{threshold:0,rootMargin:"0px 0px -40px 0px"});
  reveals.forEach(el=>io.observe(el));
  // Salvaguarda: a los 2.5s revela cualquier bloque que siga oculto
  setTimeout(()=>reveals.forEach(el=>el.classList.add("active")),2500);
  // Contadores
  const cw=new IntersectionObserver((es)=>{es.forEach(en=>{if(en.isIntersecting){en.target.querySelectorAll(".stat-number,.metric-number").forEach(c=>{const t=parseInt(c.getAttribute("data-counter"));let v=0;const inc=t/120;const up=()=>{if(v<t){v+=inc;c.textContent=Math.ceil(v);requestAnimationFrame(up);}else c.textContent=t;};up();});cw.unobserve(en.target);}});},{threshold:.4});
  document.querySelectorAll(".stats,.equipo-metrics").forEach(s=>cw.observe(s));
  // Banner de cookies: aparece si no se ha aceptado y se oculta al aceptar o al hacer scroll
  const cb=document.getElementById("cookie-banner");
  if(cb&&!localStorage.getItem("cookies-ok")){
    cb.hidden=false;
    const cerrar=()=>{localStorage.setItem("cookies-ok","1");cb.hidden=true;window.removeEventListener("scroll",onScroll);};
    const ok=document.getElementById("cookie-ok");if(ok)ok.addEventListener("click",cerrar);
    const onScroll=()=>{if(window.scrollY>60)cerrar();};
    window.addEventListener("scroll",onScroll,{passive:true});
  }
  // El formulario usa FormSubmit (POST nativo): no se intercepta.
});
"""

def copiar_assets():
    """Copia css/img de la plantilla, escribe nuestro JS, favicon y CSS complementario."""
    if os.path.isdir(PLANTILLA):
        for sub in ("css", "img"):
            origen = os.path.join(PLANTILLA, sub)
            if os.path.isdir(origen):
                shutil.copytree(origen, os.path.join(SALIDA, "assets", sub),
                                dirs_exist_ok=True)
    destino_css = os.path.join(SALIDA, "assets", "css")
    destino_js = os.path.join(SALIDA, "assets", "js")
    os.makedirs(destino_css, exist_ok=True)
    os.makedirs(destino_js, exist_ok=True)
    with open(os.path.join(destino_css, "contenido.css"), "w", encoding="utf-8") as f:
        f.write(CONTENIDO_CSS)
    with open(os.path.join(destino_js, "main.js"), "w", encoding="utf-8") as f:
        f.write(MAIN_JS)
    with open(os.path.join(SALIDA, "assets", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON_SVG)
    # Imágenes propias (sustituyen a las fotos de plantilla con logos de terceros)
    destino_img = os.path.join(SALIDA, "assets", "img")
    os.makedirs(destino_img, exist_ok=True)
    for viejo in ("equipo.webp", "proceso.webp", "resultado.webp"):
        ruta_v = os.path.join(destino_img, viejo)
        if os.path.exists(ruta_v):
            os.remove(ruta_v)
    for nombre, (lab, sub) in PLACEHOLDERS.items():
        with open(os.path.join(destino_img, nombre), "w", encoding="utf-8") as f:
            f.write(_placeholder_svg(lab, sub))

def generar_extras():
    """robots.txt (con bots de IA), llms.txt, 404.html y .htaccess."""
    # robots.txt
    bots = ["GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-Web",
            "anthropic-ai", "PerplexityBot", "Google-Extended", "Applebot-Extended",
            "CCBot", "Bingbot", "Googlebot"]
    rob = ["# robots.txt — crawlers tradicionales y de IA bienvenidos"]
    for b in bots:
        rob.append(f"User-agent: {b}\nAllow: /\n")
    rob.append("User-agent: *\nAllow: /\n")
    rob.append(f"Sitemap: {DOMINIO}/sitemap.xml")
    with open(os.path.join(SALIDA, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(rob) + "\n")

    # llms.txt — resumen para modelos de IA
    llms = f"""# {MARCA_FULL}

> {KEYWORD}: empresa especializada en limpieza y descontaminación de viviendas y
> locales tras un incendio. Solo limpieza, no realizamos obras ni reformas.
> Servicio 24/7 en España. Teléfono {TEL_FMT}. Email {EMAIL}.

## Servicios
- Limpieza de incendios y post-incendios (hollín, humo, cenizas)
- Desodorización con ozono (eliminación de olor a humo)
- Limpieza con láser y con hielo seco (criogénica)
- Síndrome de Diógenes y limpiezas traumáticas
- Descontaminación industrial

## Enlaces
- Inicio: {DOMINIO}/
- Zonas de servicio: {DOMINIO}/zonas/
- Blog: {DOMINIO}/blog/
- Sitemap: {DOMINIO}/sitemap.xml
"""
    with open(os.path.join(SALIDA, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms)

    # 404.html (rutas absolutas para que funcionen en cualquier nivel)
    cuerpo404 = ('<section class="page-hero"><div class="container">'
                 '<h1>Página no encontrada</h1>'
                 '<p>La página que buscas no existe o se ha movido.</p></div></section>'
                 '<section class="contenido-wp section-padding"><div class="container">'
                 '<article style="text-align:center">'
                 '<p>Vuelve al inicio o llámanos para una urgencia.</p>'
                 f'<p><a class="btn" href="/">Ir al inicio</a> '
                 f'<a class="btn" href="tel:{TEL}">Llamar {TEL_FMT}</a></p>'
                 '</article></div></section>')
    html404 = plantilla("404 · Página no encontrada | " + MARCA_FULL,
                        "La página que buscas no existe.", DOMINIO + "/404",
                        cuerpo404, "/", pf_override="/")
    with open(os.path.join(SALIDA, "404.html"), "w", encoding="utf-8") as f:
        f.write(html404)

    # .htaccess (para hosting Apache; GitHub Pages lo ignora)
    htaccess = f"""DirectoryIndex index.html
Options -Indexes
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{{HTTPS}} off
  RewriteRule ^ https://%{{HTTP_HOST}}%{{REQUEST_URI}} [L,R=301]
  RewriteCond %{{HTTP_HOST}} ^www\\.(.+)$ [NC]
  RewriteRule ^ https://%1%{{REQUEST_URI}} [L,R=301]
</IfModule>
ErrorDocument 404 /404.html
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType image/webp "access plus 6 months"
  ExpiresByType image/svg+xml "access plus 6 months"
</IfModule>
<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
</IfModule>
"""
    with open(os.path.join(SALIDA, ".htaccess"), "w", encoding="utf-8") as f:
        f.write(htaccess)

    # .nojekyll: evita que GitHub Pages procese el sitio con Jekyll
    open(os.path.join(SALIDA, ".nojekyll"), "w").close()

def sincronizar_raiz():
    """Copia el sitio generado (web-html/) a la raíz del repo, para que GitHub Pages
    lo sirva tanto en modo 'GitHub Actions' (artefacto web-html) como en modo
    'Deploy from a branch' (raíz). No toca las carpetas de código fuente."""
    PROTEGIDAS = {"tools", "origen-wordpress", "plantilla-5", "docs",
                  ".git", ".github", "README.md", "web-html"}
    for nombre in os.listdir(SALIDA):
        if nombre in PROTEGIDAS:
            continue
        org = os.path.join(SALIDA, nombre)
        dst = os.path.join(RAIZ, nombre)
        if os.path.isdir(org):
            shutil.copytree(org, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(org, dst)

# ============================================================================
#  Parseo del WXR y generación
# ============================================================================
def ruta_de(link):
    p = re.sub(r'^https?://[^/]+', '', link or "").strip()
    if not p.startswith("/"):
        p = "/" + p
    if not p.endswith("/"):
        p += "/"
    return p

def asegurar_alt(htmltxt, ciudad=None):
    """Rellena alt vacío/ausente de <img> con la keyword (+ciudad)."""
    base = f"{KEYWORD} en {ciudad}" if ciudad else KEYWORD
    rep = html.escape(base)
    def fix(m):
        tag = m.group(0)
        if re.search(r'\balt\s*=\s*"[^"]+"', tag):
            return tag
        tag = re.sub(r'\s*\balt\s*=\s*""', '', tag)          # quita alt vacío
        return tag[:-1] + f' alt="{rep}">'                    # añade antes de '>'
    return re.sub(r'<img\b[^>]*>', fix, htmltxt)

_TITULOS = {}
def titulo_unico(t, sufijo=""):
    """Garantiza títulos únicos; si se repite, añade un sufijo."""
    if t not in _TITULOS:
        _TITULOS[t] = 1; return t
    _TITULOS[t] += 1
    nuevo = f"{t} ({sufijo})" if sufijo else f"{t} ({_TITULOS[t]})"
    return nuevo

_DESCS = set()
def desc_unica(desc, cuerpo):
    """Devuelve una meta-description única; si se repite, usa el extracto del propio contenido."""
    d = (desc or "").strip()
    if not d or d in _DESCS:
        d = primer_texto(cuerpo, 155) or d
    _DESCS.add(d)
    return d

def escribir(ruta, contenido):
    destino = os.path.join(SALIDA, ruta.strip("/"), "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(contenido)

def main():
    if not XML:
        sys.exit("No se encontró el XML en origen-wordpress/export/")
    tree = ET.parse(XML[0]); root = tree.getroot()
    canal = root.find("channel")

    paginas, entradas = [], []
    for item in canal.findall("item"):
        tipo   = item.findtext("wp:post_type", default="", namespaces=NS)
        estado = item.findtext("wp:status", default="", namespaces=NS)
        if estado != "publish" or tipo not in ("page", "post"):
            continue
        titulo = (item.findtext("title") or "").strip()
        link   = (item.findtext("link") or "").strip()
        cont   = item.findtext("content:encoded", default="", namespaces=NS)
        fecha  = item.findtext("wp:post_date", default="", namespaces=NS)
        # postmeta -> SEO
        meta = {}
        for pm in item.findall("wp:postmeta", NS):
            k = pm.findtext("wp:meta_key", default="", namespaces=NS)
            v = pm.findtext("wp:meta_value", default="", namespaces=NS)
            meta[k] = v
        seo_title = meta.get("_yoast_wpseo_title") or meta.get("rank_math_title") or f"{titulo} | Nano Nex"
        seo_desc  = meta.get("_yoast_wpseo_metadesc") or meta.get("rank_math_description") or ""
        seo_title = re.sub(r'%%[^%]+%%', '', seo_title).strip(" |") or titulo

        registro = dict(titulo=titulo, link=link, ruta=ruta_de(link),
                        cont=cont, fecha=fecha, seo_title=seo_title, seo_desc=seo_desc)
        (paginas if tipo == "page" else entradas).append(registro)

    entradas.sort(key=lambda r: r["fecha"], reverse=True)

    # Copiar assets de la plantilla (css/js/img) al sitio
    copiar_assets()

    # Lista de páginas-ciudad (para el bloque de zonas de las landings)
    ciudades = sorted(
        [(p["titulo"], p["ruta"]) for p in paginas
         if p["ruta"] != "/" and ciudad_de(p["titulo"])],
        key=lambda x: x[0])

    # --- Páginas: portada y ciudades = landing; resto = artículo ---
    for p in paginas:
        pf = prefijo_rel(p["ruta"])
        ciudad = None if p["ruta"] == "/" else ciudad_de(p["titulo"])
        cuerpo = asegurar_alt(localizar_imgs(convertir(p["cont"]), pf), ciudad)
        canonical = DOMINIO + p["ruta"]
        if p["ruta"] == "/" or ciudad:
            # Variación de término por ciudad para no canibalizar
            idx = sum(ord(c) for c in (ciudad or "home")) % len(TERMINOS)
            termino, termino_largo = TERMINOS[idx]
            if ciudad:
                title = titulo_unico(f"{KEYWORD} en {ciudad} | {termino_largo.capitalize()} · {MARCA}")
                h1 = f"{KEYWORD} en {ciudad}"
                # Descripción única por ciudad (solo se usa Yoast si menciona la ciudad)
                yoast = p["seo_desc"] or ""
                if ciudad.lower() in yoast.lower():
                    desc = yoast
                else:
                    desc = (f"{KEYWORD} en {ciudad}: limpieza de {termino}, hollín y olores tras un "
                            f"incendio en viviendas y locales. Servicio 24/7, presupuesto sin compromiso. ☎ {TEL_FMT}.")
                schema = _schema_local(ciudad, canonical) + _schema_breadcrumb(h1, canonical)
            else:
                title = titulo_unico(f"{KEYWORD} · Limpieza y Descontaminación tras Incendio | {MARCA}")
                h1 = f"{KEYWORD}: limpieza y descontaminación tras incendio"
                desc = (f"{KEYWORD}: limpieza de humo, hollín y olores tras un incendio en tu vivienda "
                        f"o local. Servicio profesional 24/7. Presupuesto sin compromiso. ☎ {TEL_FMT}.")
                schema = _schema_home(canonical)
            intro = (p["seo_desc"] or
                     "Limpiamos y descontaminamos tu vivienda o local tras un incendio. Sin obras: solo limpieza.")
            body = secciones_landing(h1, intro, cuerpo, ciudades, pf, ciudad)
            escribir(p["ruta"], plantilla(title, desc, canonical, body, p["ruta"], schema=schema))
        else:
            desc = desc_unica(p["seo_desc"], cuerpo)
            title = titulo_unico(p["seo_title"])
            body = articulo(p["titulo"], cuerpo)
            escribir(p["ruta"], plantilla(title, desc, canonical, body, p["ruta"],
                     schema=_schema_breadcrumb(p["titulo"], canonical)))

    # --- Entradas (blog) = artículo ---
    for e in entradas:
        pf = prefijo_rel(e["ruta"])
        cuerpo = asegurar_alt(localizar_imgs(convertir(e["cont"]), pf), None)
        desc = desc_unica(e["seo_desc"], cuerpo)
        canonical = DOMINIO + e["ruta"]
        title = titulo_unico(e["seo_title"], sufijo=e["fecha"][:4])
        body = articulo(e["titulo"], cuerpo, fecha=e["fecha"][:10])
        escribir(e["ruta"], plantilla(title, desc, canonical, body,
                 e["ruta"], nav_activo="/blog/", schema=_schema_breadcrumb(e["titulo"], canonical)))

    # --- Índice del blog ---
    pf_blog = prefijo_rel("/blog/")
    tarjetas = "".join(
        f'<a class="blog-card reveal" href="{rel(e["ruta"], pf_blog)}">'
        f'<span class="blog-fecha">{e["fecha"][:10]}</span>'
        f'<h3>{html.escape(e["titulo"])}</h3></a>'
        for e in entradas)
    body = (f'<section class="page-hero"><div class="container"><h1>Blog</h1>'
            f'<p>Consejos y novedades sobre limpieza de incendios, ozono y más.</p></div></section>'
            f'<section class="contenido-wp section-padding"><div class="container">'
            f'<div class="blog-grid">{tarjetas}</div></div></section>')
    escribir("/blog/", plantilla("Blog | " + MARCA_FULL,
             "Artículos y consejos sobre limpieza de incendios, ozono y más.",
             DOMINIO + "/blog/", body, "/blog/"))

    # --- Página de zonas (ciudades) ---
    pf_zonas = prefijo_rel("/zonas/")
    body = (f'<section class="page-hero"><div class="container"><h1>Zonas de Servicio</h1>'
            f'<p>{KEYWORD} cerca de ti. Estas son las poblaciones donde actuamos.</p></div></section>'
            f'<section id="zonas" class="zonas section-padding"><div class="container">'
            f'<div class="zonas-grid">{_zonas_grid(ciudades, pf_zonas)}</div></div></section>'
            f'{seccion_contacto(pf_zonas)}')
    escribir("/zonas/", plantilla("Zonas de servicio · " + KEYWORD + " | " + MARCA,
             f"{KEYWORD} en Madrid, Barcelona, Valencia, Sevilla, Málaga, Murcia, Zaragoza y más poblaciones. Servicio 24/7.",
             DOMINIO + "/zonas/", body, "/zonas/",
             schema=_schema_breadcrumb("Zonas de servicio", DOMINIO + "/zonas/")))

    # --- Aviso legal ---
    aviso = f"""<h2>Datos identificativos</h2>
<p>Titular: {MARCA_FULL}. Email: <a href="mailto:{EMAIL}">{EMAIL}</a>. Teléfono: {TEL_FMT}.</p>
<p>NIF y datos de registro: <em>pendientes de completar</em>.</p>
<h2>Objeto</h2>
<p>{MARCA_FULL} presta servicios de {KEYWORD.lower()}: limpieza y descontaminación de viviendas y locales tras un incendio. No realizamos obras ni reformas.</p>
<h2>Propiedad intelectual</h2>
<p>Todos los contenidos de este sitio son propiedad de {MARCA_FULL} o de terceros que han autorizado su uso.</p>
<h2>Responsabilidad</h2>
<p>El titular no se hace responsable del uso indebido de los contenidos del sitio web.</p>"""
    escribir("/aviso-legal/", plantilla("Aviso legal | " + MARCA_FULL,
             "Aviso legal y datos identificativos de " + MARCA_FULL + ".",
             DOMINIO + "/aviso-legal/", articulo("Aviso legal", aviso),
             "/aviso-legal/", schema=_schema_breadcrumb("Aviso legal", DOMINIO + "/aviso-legal/")))

    # --- sitemap.xml ---
    rutas = ([p["ruta"] for p in paginas] + [e["ruta"] for e in entradas] +
             ["/blog/", "/zonas/", "/aviso-legal/"])
    hoy = datetime.now().strftime("%Y-%m-%d")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for r in rutas:
        pr = "1.0" if r == "/" else ("0.8" if ciudad_de(r) or r in ("/blog/", "/zonas/") else "0.6")
        sm.append(f"  <url><loc>{DOMINIO}{r}</loc><lastmod>{hoy}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    with open(os.path.join(SALIDA, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm))
    urls = rutas

    generar_extras()
    sincronizar_raiz()

    print(f"OK: {len(paginas)} páginas + {len(entradas)} entradas + blog + zonas")
    print(f"Total URLs en sitemap: {len(urls)}")
    total = len(LOC["ok"]) + len(LOC["falta"])
    print(f"Imágenes: {len(LOC['ok'])}/{total} localizadas, "
          f"{len(LOC['falta'])} siguen en vivo (faltan en uploads)")
    if LOC["falta"]:
        with open(os.path.join(RAIZ, "docs", "imagenes-faltantes.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(sorted(LOC["falta"])))
        print("  -> lista en docs/imagenes-faltantes.txt")

if __name__ == "__main__":
    main()
