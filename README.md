# limpieza_incendios_nanonex_es

Conversión del sitio WordPress **Limpiezas de Incendios Nano Nex**
(`limpiezaincendiosnanonex.es`, hecho con Divi) a una **web HTML estática**
optimizada para SEO.

## Estructura del repositorio

```
origen-wordpress/
└── export/      Export XML (WXR) original de WordPress  [fuente]
tools/
└── generar_sitio.py   Generador: XML -> HTML estático
web-html/        Web HTML estática generada  [resultado]
├── index.html           portada
├── <permalinks>/        páginas y entradas (misma URL que el original)
├── blog/                índice del blog
├── zonas/               índice de páginas por ciudad
├── assets/estilo.css    estilos
├── sitemap.xml
└── robots.txt
docs/            Documentación
```

## Qué hace el generador

`tools/generar_sitio.py` lee el XML y:

- Extrae el contenido limpio de los **módulos Divi** (`et_pb_text`, `et_pb_image`,
  `et_pb_blurb`, botones, CTA, formularios…) y de las entradas Gutenberg.
- Conserva los **permalinks** originales (no se pierde SEO).
- Mantiene los **meta-tags SEO de Yoast/RankMath** (`<title>` y meta description).
- Genera `sitemap.xml` y `robots.txt`.

Resultado: **28 páginas + 209 entradas** de blog + índices.

## Regenerar la web

```bash
python3 tools/generar_sitio.py
```

## Previsualizar en local

```bash
cd web-html
python3 -m http.server 8000
# abre http://localhost:8000 en el navegador
```

## Imágenes (pendiente)

El XML solo **enlaza** las imágenes; ahora mismo el HTML apunta a las URLs
en vivo de `limpiezaincendiosnanonex.es` (la web se ve completa). Para
hacerla 100 % autónoma hay que **localizar** las imágenes:

1. Subir la carpeta `wp-content/uploads` a `origen-wordpress/uploads/`, **o**
2. Permitir el dominio en la política de red del entorno para descargarlas.

Una vez disponibles, se añade un paso al generador para reescribir los `src`
a rutas locales (`/wp-content/uploads/...`).
