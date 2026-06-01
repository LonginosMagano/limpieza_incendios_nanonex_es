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

def plantilla(titulo, descripcion, canonical, cuerpo, ruta_actual, nav_activo=None):
    pf = prefijo_rel(ruta_actual)
    activo = nav_activo or ruta_actual
    def _enlace(e, r):
        cls = ' class="act"' if r == activo else ''
        return f'<a href="{rel(r, pf)}"{cls}>{html.escape(e)}</a>'
    nav = "".join(_enlace(e, r) for e, r in NAV)
    desc = html.escape(descripcion or "")
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="es_ES">
<link rel="stylesheet" href="{pf}assets/estilo.css">
</head>
<body>
<header class="cab">
  <div class="cont">
    <a class="logo" href="{rel('/', pf)}">Limpiezas Incendios <b>Nano Nex</b></a>
    <nav>{nav}</nav>
  </div>
</header>
<main class="cont">
{cuerpo}
</main>
<footer class="pie">
  <div class="cont">
    <p>&copy; {datetime.now().year} Limpiezas de Incendios Nano Nex · Limpieza de incendios y post-incendios en toda España.</p>
    <p class="legal">
      <a href="{rel('/politica-de-privacidad/', pf)}">Política de privacidad</a> ·
      <a href="{rel('/politica-de-cookies/', pf)}">Política de cookies</a> ·
      <a href="{rel('/contacto/', pf)}">Contacto</a>
    </p>
  </div>
</footer>
</body>
</html>"""

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

    # --- Páginas ---
    for p in paginas:
        cuerpo = convertir(p["cont"])
        if p["ruta"] == "/":   # portada
            cuerpo = f"<article>{cuerpo}</article>"
        else:
            cuerpo = f"<article><h1>{html.escape(p['titulo'])}</h1>{cuerpo}</article>"
        desc = p["seo_desc"] or primer_texto(cuerpo)
        canonical = DOMINIO + p["ruta"]
        escribir(p["ruta"], plantilla(p["seo_title"], desc, canonical, cuerpo, p["ruta"]))

    # --- Entradas ---
    for e in entradas:
        cuerpo = convertir(e["cont"])
        fecha_txt = e["fecha"][:10]
        cuerpo = (f"<article><h1>{html.escape(e['titulo'])}</h1>"
                  f"<p class='meta'>Publicado el {fecha_txt}</p>{cuerpo}</article>")
        desc = e["seo_desc"] or primer_texto(cuerpo)
        canonical = DOMINIO + e["ruta"]
        escribir(e["ruta"], plantilla(e["seo_title"], desc, canonical, cuerpo,
                                      e["ruta"], nav_activo="/blog/"))

    # --- Índice del blog ---
    pf_blog = prefijo_rel("/blog/")
    lista = "".join(
        f'<li><a href="{rel(e["ruta"], pf_blog)}">{html.escape(e["titulo"])}</a> '
        f'<span class="fecha">{e["fecha"][:10]}</span></li>'
        for e in entradas
    )
    cuerpo = f"<article><h1>Blog</h1><ul class='listado'>{lista}</ul></article>"
    escribir("/blog/", plantilla("Blog | Limpiezas Incendios Nano Nex",
             "Artículos y consejos sobre limpieza de incendios, ozono y más.",
             DOMINIO + "/blog/", cuerpo, "/blog/"))

    # --- Página de zonas (ciudades) ---
    ciudades = [p for p in paginas if "incendios" in p["titulo"].lower()
                and p["ruta"] not in ("/",)]
    pf_zonas = prefijo_rel("/zonas/")
    enl = "".join(f'<li><a href="{rel(p["ruta"], pf_zonas)}">{html.escape(p["titulo"])}</a></li>'
                  for p in sorted(ciudades, key=lambda x: x["titulo"]))
    cuerpo = (f"<article><h1>Zonas donde trabajamos</h1>"
              f"<p>Servicio de limpieza de incendios y post-incendios en toda España.</p>"
              f"<ul class='listado columnas'>{enl}</ul></article>")
    escribir("/zonas/", plantilla("Zonas de servicio | Limpiezas Incendios Nano Nex",
             "Limpieza de incendios en Madrid, Barcelona, Valencia, Sevilla y toda España.",
             DOMINIO + "/zonas/", cuerpo, "/zonas/"))

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

if __name__ == "__main__":
    main()
