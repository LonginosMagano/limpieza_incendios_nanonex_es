# Nano Nex — Limpieza de Incendios Madrid

Sitio web corporativo de **Limpieza Incendios Nano Nex S.L.**, empresa especializada
en limpieza y descontaminación tras incendios en Madrid y la Comunidad de Madrid.
*(Solo limpieza y descontaminación; no se realizan reformas ni restauración.)*

- **Web en producción:** https://limpiezaincendiosnanonexmadrid.com.es
- **Tecnología:** HTML/CSS/JS estático (sin framework ni build)
- **Hosting:** DreamHost — despliegue automático por SFTP en cada push a `master`

---

## 📁 Estructura del sitio (43 páginas HTML)

| Tipo | Páginas |
|------|---------|
| **Home** | `index.html` |
| **Landings de municipios** (8) | Alcalá de Henares, Getafe, Leganés, Alcorcón, Móstoles, Fuenlabrada, Torrejón de Ardoz, Alcobendas |
| **Landings Zona Norte** (3) | San Sebastián de los Reyes, Tres Cantos, Colmenar Viejo |
| **Landings de barrios de Madrid** (7) | Salamanca, Chamberí, Retiro, Carabanchel, Vallecas, Hortaleza, Tetuán |
| **Hub de zonas** | `ubicaciones.html` |
| **Blog — índice** | `blog.html` |
| **Blog — artículos generales** (6) | Qué hacer tras un incendio · Eliminar olor a humo · Limpiar hollín · ¿Cubre el seguro? · Cómo reclamar · Cuánto cuesta |
| **Blog — cluster seguros** (3) | Si el seguro no cubre · Documentos para reclamar · Peritaje |
| **Blog — "Cómo limpiar el hollín en [ciudad]"** (9) | Madrid, Getafe, Alcalá, Alcorcón, Leganés, Móstoles, Fuenlabrada, Torrejón, Alcobendas |
| **Legales** (3) | Aviso legal · Privacidad · Cookies |
| **Error** | `404.html` |

Todas las landings y artículos tienen **contenido único** (sin texto duplicado).

---

## 🔍 SEO y optimización para IA

- **Titles y meta descriptions únicos** en todas las páginas.
- **Schemas (JSON-LD):** `LocalBusiness`, `Organization`, `Service`, `WebSite`,
  `FAQPage`, `HowTo`, `BlogPosting`, `BreadcrumbList`, `Review`, `AggregateRating`, `speakable`.
- **Fragmentos destacados:** estructura "Respuesta rápida" + pasos numerados +
  tablas + FAQ en landings y artículos.
- **Búsqueda por IA:** `robots.txt` con permisos explícitos para GPTBot, ClaudeBot,
  PerplexityBot, Google-Extended, CCBot, OAI-SearchBot… + `llms.txt`.
- **HTML estático** → contenido legible sin ejecutar JavaScript (ventaja para crawlers de IA).
- **Datos reales:** rating 4.9/10 y reseñas reales de Google con schema `Review`;
  `sameAs` apuntando a la ficha de Google Business Profile.
- `sitemap.xml` (42 URLs) + canonicals en todas las páginas.

## ⚡ Rendimiento

- Imágenes en **WebP**; logo optimizado (228 KB → 38 KB). Total imágenes ~1,7 MB.
- Google Fonts en **carga asíncrona** (no bloquea el render).
- **Preload + fetchpriority** de la imagen LCP del hero.
- `width`/`height` en todas las imágenes (evita CLS).

## ♿ Accesibilidad

- Formularios con `<label>` asociados · Landmark `<main>` en todas las páginas ·
  Contraste WCAG AA.

---

## 🚀 Despliegue (automático)

Cada push a `master` ejecuta `.github/workflows/deploy-dreamhost.yml`, que sube el
sitio a DreamHost por **SFTP** (puerto 22) con `lftp mirror` (`--delete` → espejo
exacto del repo; incluye `.htaccess` y dotfiles).

**Secrets de GitHub:** `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`,
`FTP_REMOTE_PATH` (la ruta debe ser **absoluta**, empezar por `/`).

### Cómo editar el sitio
1. Modifica los `.html` o `estilos-landing.css`.
2. `git add -A && git commit -m "..." && git push`.
3. El workflow despliega solo en 1-2 minutos.

> Las landings y el blog comparten estilos en `estilos-landing.css` (enlazado con
> `?v=N` para cache-busting: **sube ese número al cambiar el CSS**).
> La home (`index.html`) tiene su CSS inline propio.

---

## 📇 Datos de la empresa

- **Razón social:** Limpieza Incendios Nano Nex S.L. · **CIF:** B-10541001
- **Dirección:** Plaza de Castilla, 3, 28046 Madrid
- **Teléfono:** 911 086 565 · **WhatsApp:** +34 632 107 272 · **Email:** info@nanonex.es
- **Horario:** L-V 07:00-22:00 · Sáb-Dom 08:00-16:00 · Urgencias 24/7
- **Google Business Profile:** https://share.google/XCuzrBolYpBIBzzAR
- **Formulario de contacto:** Formspree → `info@nanonex.es`

---

## ✅ Pendiente (tareas externas al código)

- [ ] Alta del dominio en **Google Search Console** y envío de `sitemap.xml`.
- [ ] En el **GBP**, comprobar que el campo "sitio web" apunta al dominio.
- [ ] Borrar en DreamHost la carpeta duplicada de un deploy antiguo fallido
      (`/home/<usuario>/home/<usuario>/...`), por SFTP/panel.

## 🗂️ Recursos sin usar (reservados)

~15 imágenes de "antes/después" en el repo sin enlazar, reservadas para una futura
galería o nuevos artículos del blog.
