# limpieza_incendios_nanonex_es

Proyecto para **convertir un sitio WordPress en una web HTML estática**,
optimizada para SEO.

## Estrategia

1. **Extraer el contenido** del WordPress original (textos, datos y fotos).
2. **Generar una web estática** con un generador de sitios (Eleventy/Hugo),
   que produce HTML puro: carga rápida, control de meta-tags, `sitemap.xml`,
   `robots.txt` y URLs limpias → ideal para SEO.

## Qué subir y dónde

```
origen-wordpress/
├── export/      ← aquí el Export XML (WXR) de WordPress  → contenido + SEO
└── uploads/     ← aquí la carpeta wp-content/uploads      → fotos/imágenes

web-html/        ← aquí se construirá la web HTML final
docs/            ← documentación y notas del proyecto
```

### 1. Export XML (WXR) — el contenido

En tu WordPress: **Escritorio → Herramientas → Exportar → Todo el contenido**.
Descarga el `.xml` y colócalo en `origen-wordpress/export/`.

Contiene: títulos, textos, páginas, entradas, categorías, etiquetas, fechas,
autores y los **metadatos SEO** (títulos y meta descriptions de Yoast/RankMath).

### 2. Carpeta uploads — las fotos

El XML solo **enlaza** las imágenes por URL, no las incluye. Copia la carpeta
`wp-content/uploads` (por FTP o desde tu backup) a `origen-wordpress/uploads/`.

## Cómo subir los archivos

```bash
# copia tus archivos en las carpetas indicadas, luego:
git add .
git commit -m "Añadir datos del WordPress (export + uploads)"
git push
```

> ⚠️ Si los `uploads` pesan mucho (cientos de MB), avísame: conviene usar
> Git LFS o subirlos por lotes.

## Siguientes pasos (una vez subido el contenido)

- Parsear el XML y convertir las entradas/páginas a Markdown/HTML.
- Montar el generador estático en `web-html/` con plantillas y SEO.
- Mantener los **permalinks** originales y generar `sitemap.xml` + `robots.txt`.
