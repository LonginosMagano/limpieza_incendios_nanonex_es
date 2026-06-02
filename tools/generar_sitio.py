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
EMAIL      = "info@nano-nex.es"

# Servicios reales de Nano Nex (icono, título, descripción)
SERVICIOS = [
    ("🔥", "Limpieza de Incendios y Post-Incendios",
     "Recuperación integral de viviendas y locales tras un incendio: hollín, cenizas y daños."),
    ("💨", "Desodorización con Ozono",
     "Eliminamos por completo el olor a humo con tratamiento profesional de ozono."),
    ("✨", "Limpieza con Láser",
     "Tecnología láser para limpiar superficies delicadas sin dañar el material original."),
    ("❄️", "Limpieza con Hielo Seco",
     "Limpieza criogénica que elimina residuos sin abrasivos ni agua, ideal para maquinaria."),
    ("🏠", "Síndrome de Diógenes y Acumulación",
     "Limpieza y saneamiento de espacios con acumulación extrema, con total discreción."),
    ("🏭", "Limpiezas Traumáticas e Industriales",
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

def convertir(contenido):
    if not contenido:
        return ""
    if "[et_pb_" in contenido:
        return extraer_divi(contenido)
    return texto_a_parrafos(limpiar_gutenberg(contenido))

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

def _cabecera(pf, activo):
    def _enlace(e, r):
        cls = ' class="act"' if r == activo else ''
        return f'<li><a href="{rel(r, pf)}"{cls}>{html.escape(e)}</a></li>'
    items = "".join(_enlace(e, r) for e, r in NAV)
    return f"""<header class="header">
  <div class="container">
    <a href="{rel('/', pf)}" class="logo">Nano<span>Nex</span></a>
    <nav class="nav">
      <ul class="nav-list">{items}</ul>
      <a href="tel:{TEL}" class="btn btn-call">{TEL_FMT}</a>
    </nav>
    <button class="hamburger" aria-label="Abrir menú"><span></span><span></span><span></span></button>
  </div>
</header>"""

def _pie(pf):
    enl = "".join(f'<li><a href="{rel(r, pf)}">{html.escape(e)}</a></li>'
                  for e, r in NAV if r not in ("/",))
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer-col">
      <h3>{MARCA_FULL}</h3>
      <p>Especialistas en limpieza y restauración tras incendios en toda España. Más de 30 años de experiencia.</p>
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
        <li><a href="mailto:{EMAIL}">✉️ {EMAIL}</a></li>
        <li><a href="{rel('/politica-de-privacidad/', pf)}">Política de privacidad</a></li>
        <li><a href="{rel('/politica-de-cookies/', pf)}">Política de cookies</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; <span id="currentYear">{datetime.now().year}</span> {MARCA_FULL}. Todos los derechos reservados.</p>
  </div>
</footer>
<div class="mobile-cta-bar">
  <a href="tel:{TEL}" class="btn-mobile-call">📞 Llamar</a>
  <a href="{rel('/contacto/', pf)}" class="btn-mobile-quote">✉️ Presupuesto</a>
</div>"""

def _schema_local(ciudad, canonical):
    loc = ciudad or "España"
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"LocalBusiness","name":"{MARCA_FULL}",
"@id":"{DOMINIO}/#organization","url":"{canonical}","telephone":"+34{TEL}",
"email":"{EMAIL}","areaServed":"{loc}","priceRange":"€€",
"address":{{"@type":"PostalAddress","addressLocality":"{loc}","addressCountry":"ES"}}}}
</script>"""

def plantilla(titulo, descripcion, canonical, cuerpo, ruta_actual,
              nav_activo=None, schema=None):
    pf = prefijo_rel(ruta_actual)
    activo = nav_activo or ruta_actual
    desc = html.escape(descripcion or "")
    og_img = f"{DOMINIO}/assets/img/hero.webp"
    schema_html = schema or ""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
{schema_html}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pf}assets/css/style.css">
<link rel="stylesheet" href="{pf}assets/css/contenido.css">
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
    lugar = ciudad or "toda España"
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
      <p>✅ Equipos de última generación</p>
      <p>✅ Satisfacción garantizada</p>
    </div>
  </div>
</section>

<section class="stats section-padding">
  <div class="container">
    <div class="stat-item"><span class="stat-number" data-counter="30">0</span>+<p>Años de Experiencia</p></div>
    <div class="stat-item"><span class="stat-number" data-counter="500">0</span>+<p>Proyectos Completados</p></div>
    <div class="stat-item"><span class="stat-number" data-counter="98">0</span>%<p>Clientes Satisfechos</p></div>
    <div class="stat-item"><span class="stat-number" data-counter="24">0</span>/<span class="stat-number" data-counter="7">0</span><p>Servicio de Urgencia</p></div>
  </div>
</section>

<section id="servicios" class="servicios section-padding">
  <div class="container">
    <h2 class="section-title">Nuestros Servicios de Limpieza</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Soluciones integrales para la recuperación de tu espacio en {html.escape(lugar)}.</p>
    <div class="servicios-grid">{_tarjetas_servicios()}</div>
  </div>
</section>
{bloque_real}
<section class="before-after section-padding">
  <div class="container">
    <h2 class="section-title">Resultados que Hablan por Sí Solos</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Transformamos espacios devastados en ambientes renovados.</p>
    <div class="before-after-content">
      <div class="before-after-image"><img src="{pf}assets/img/resultado.webp" alt="Resultado de limpieza por incendio" loading="lazy"></div>
      <div class="before-after-checklist">
        <h3>Nuestro Compromiso:</h3>
        <ul>
          <li>✅ Eliminación total de hollín y ceniza</li>
          <li>✅ Neutralización completa de olores con ozono</li>
          <li>✅ Restauración de superficies dañadas</li>
          <li>✅ Desinfección y saneamiento</li>
          <li>✅ Recuperación de objetos de valor</li>
          <li>✅ Entrega de espacios listos para usar</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="proceso" class="proceso section-padding">
  <div class="container">
    <h2 class="section-title">Nuestro Proceso de Restauración</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Un enfoque metódico para garantizar la máxima eficacia.</p>
    <div class="proceso-grid">
      <div class="proceso-item reveal"><div class="proceso-icon">1</div><h3>Evaluación y Planificación</h3><p>Inspección detallada de los daños y plan de acción personalizado.</p></div>
      <div class="proceso-item reveal"><div class="proceso-icon">2</div><h3>Contención y Protección</h3><p>Aislamiento de áreas afectadas para evitar la propagación de contaminantes.</p></div>
      <div class="proceso-item reveal"><div class="proceso-icon">3</div><h3>Limpieza y Desodorización</h3><p>Técnicas avanzadas para eliminar hollín, humo y olores.</p></div>
      <div class="proceso-item reveal"><div class="proceso-icon">4</div><h3>Restauración Final</h3><p>Reparación de superficies y entrega de un espacio renovado.</p></div>
    </div>
    <div class="proceso-image"><img src="{pf}assets/img/proceso.webp" alt="Proceso de limpieza por incendio" loading="lazy"></div>
  </div>
</section>

<section id="equipo" class="equipo section-padding">
  <div class="container">
    <h2 class="section-title">Nuestro Equipo de Expertos</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Profesionales cualificados y comprometidos con tu tranquilidad.</p>
    <div class="equipo-content">
      <div class="equipo-image"><img src="{pf}assets/img/equipo.webp" alt="Equipo de Nano Nex" loading="lazy"></div>
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
    <p class="section-subtitle">Historias de éxito y satisfacción en {html.escape(lugar)}.</p>
    <div class="testimonios-grid">
      <div class="testimonio-card reveal"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Nano Nex salvó mi negocio. La limpieza fue impecable y el olor a humo desapareció por completo."</p><span class="client-name">- María G.</span></div>
      <div class="testimonio-card reveal"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Profesionalidad y eficiencia. Tras el incendio en mi casa hicieron un trabajo increíble."</p><span class="client-name">- Juan P.</span></div>
      <div class="testimonio-card reveal"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Desde el primer contacto hasta la finalización, todo fue excelente. Un servicio de primera."</p><span class="client-name">- Ana R.</span></div>
    </div>
  </div>
</section>

<section id="zonas" class="zonas section-padding">
  <div class="container">
    <h2 class="section-title">Nuestras Zonas de Servicio</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Atendemos urgencias en toda España.</p>
    <div class="zonas-grid">{_zonas_grid(ciudades, pf)}</div>
  </div>
</section>

{seccion_contacto(pf, ciudad)}"""

def seccion_contacto(pf, ciudad=None):
    return f"""<section id="contacto" class="contacto section-padding">
  <div class="container">
    <h2 class="section-title">Contacto y Presupuesto Gratuito</h2>
    <div class="ornament"></div>
    <p class="section-subtitle">Estamos disponibles 24/7 para atender tu emergencia.</p>
    <div class="contact-content">
      <div class="contact-info">
        <h3>Información de Contacto</h3>
        <p>📞 Teléfono: <a href="tel:{TEL}">{TEL_FMT}</a></p>
        <p>📧 Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>🌍 Cobertura: {html.escape(ciudad or 'Toda España')}</p>
        <p>⏰ Servicio de urgencias 24 horas, 7 días</p>
      </div>
      <div class="contact-form">
        <h3>Solicita tu Presupuesto</h3>
        <form id="contactForm">
          <div class="form-group"><label for="name">Nombre:</label><input type="text" id="name" name="name" required></div>
          <div class="form-group"><label for="phone">Teléfono:</label><input type="tel" id="phone" name="phone" required></div>
          <div class="form-group"><label for="city">Población:</label><input type="text" id="city" name="city" required></div>
          <div class="form-group"><label for="description">Descripción del Incidente:</label><textarea id="description" name="description" rows="5" required></textarea></div>
          <button type="submit" class="btn btn-primary">Enviar Solicitud</button>
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
@media(max-width:768px){.page-hero h1{font-size:1.8rem}.contenido-wp article{padding:26px 20px}}
"""

def copiar_assets():
    """Copia css/js/img de la plantilla y escribe el CSS complementario."""
    if os.path.isdir(PLANTILLA):
        for sub in ("css", "js", "img"):
            origen = os.path.join(PLANTILLA, sub)
            if os.path.isdir(origen):
                shutil.copytree(origen, os.path.join(SALIDA, "assets", sub),
                                dirs_exist_ok=True)
    destino_css = os.path.join(SALIDA, "assets", "css")
    os.makedirs(destino_css, exist_ok=True)
    with open(os.path.join(destino_css, "contenido.css"), "w", encoding="utf-8") as f:
        f.write(CONTENIDO_CSS)

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
        cuerpo = localizar_imgs(convertir(p["cont"]), pf)
        desc = p["seo_desc"] or primer_texto(cuerpo)
        canonical = DOMINIO + p["ruta"]
        ciudad = None if p["ruta"] == "/" else ciudad_de(p["titulo"])
        if p["ruta"] == "/" or ciudad:
            h1 = (f"Limpieza Profesional por Incendio en {ciudad}" if ciudad
                  else "Limpieza Profesional por Incendio en toda España")
            intro = desc or "Recupera tu hogar o negocio tras un incendio con expertos."
            body = secciones_landing(h1, intro, cuerpo, ciudades, pf, ciudad)
            escribir(p["ruta"], plantilla(p["seo_title"], desc, canonical, body,
                     p["ruta"], schema=_schema_local(ciudad, canonical)))
        else:
            body = articulo(p["titulo"], cuerpo)
            escribir(p["ruta"], plantilla(p["seo_title"], desc, canonical, body, p["ruta"]))

    # --- Entradas (blog) = artículo ---
    for e in entradas:
        pf = prefijo_rel(e["ruta"])
        cuerpo = localizar_imgs(convertir(e["cont"]), pf)
        desc = e["seo_desc"] or primer_texto(cuerpo)
        canonical = DOMINIO + e["ruta"]
        body = articulo(e["titulo"], cuerpo, fecha=e["fecha"][:10])
        escribir(e["ruta"], plantilla(e["seo_title"], desc, canonical, body,
                 e["ruta"], nav_activo="/blog/"))

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
            f'<p>Limpieza de incendios y post-incendios en toda España.</p></div></section>'
            f'<section id="zonas" class="zonas section-padding"><div class="container">'
            f'<div class="zonas-grid">{_zonas_grid(ciudades, pf_zonas)}</div></div></section>'
            f'{seccion_contacto(pf_zonas)}')
    escribir("/zonas/", plantilla("Zonas de servicio | " + MARCA_FULL,
             "Limpieza de incendios en Madrid, Barcelona, Valencia, Sevilla y toda España.",
             DOMINIO + "/zonas/", body, "/zonas/"))

    # --- sitemap.xml ---
    urls = ([DOMINIO + p["ruta"] for p in paginas] +
            [DOMINIO + e["ruta"] for e in entradas] +
            [DOMINIO + "/blog/", DOMINIO + "/zonas/"])
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{u}</loc></url>")
    sm.append("</urlset>")
    with open(os.path.join(SALIDA, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm))

    # --- robots.txt ---
    with open(os.path.join(SALIDA, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMINIO}/sitemap.xml\n")

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
