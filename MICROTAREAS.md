# 🎯 PLAN DE MICROTAREAS - Limpieza Incendios Nano Nex

## CICLO 1: CONTACTO Y CONFIGURACIÓN BÁSICA (Hoy - 2h)

### Microtarea 1.1: Actualizar Teléfono Global
- [ ] Buscar y reemplazar `632 107 272` → `632 107 272` en TODOS los HTML
- [ ] Validar con: `grep -r "632 107 272" .`
- [ ] Verificar WhatsApp wa.me link: `https://wa.me/34632107272`

### Microtarea 1.2: Actualizar Email
- [ ] Buscar y reemplazar `info@nanonex.es` → `info@nanonex.es`
- [ ] Actualizar en FormSubmit _subject
- [ ] Validar: `grep -r "info@nanonex.es" .`

### Microtarea 1.3: Validar FormSubmit
- [ ] Verificar FormSubmit en index.html
- [ ] Campos: Nombre, Teléfono, Población (¿Están todos?)
- [ ] _subject correcto: "Nueva solicitud · Limpieza Post Incendio"
- [ ] Origen debe indicar dominio

### Microtarea 1.4: Topbar Consistente
- [ ] Topbar: "🚨 Urgencias 24/7 · Limpieza profesional 365 días"
- [ ] Horario: "L-V 7:00-22:00 · Sáb-Dom 8:00-16:00"
- [ ] Aplicar a TODAS las landings

### Microtarea 1.5: Favicon
- [ ] Usar `Favicon trasnparente Rojo Naranja.png` en todos los HTML
- [ ] Link rel="icon" correcto

---

## CICLO 2: HUMANIZACIÓN DE TEXTOS (Hoy/Mañana - 6h)

### Microtarea 2.1: Humanizar Home (index.html)
- [ ] H1: Cambiar a estilo Ángel Expósito
  - Actual: Genérico
  - Nuevo: Claro, directo, emocional
- [ ] Párrafo intro: Remover "Empresa especializada"
- [ ] Usar problemas reales: "Después de un incendio tu hogar se convierte en..."
- [ ] Evitar: "limpieza profesional 365 días" (repetido)

### Microtarea 2.2: Humanizar Landings Madrid (7 barrios)
- [ ] madrid-carabanchel.html - Mencionar "Carabanchel, corazón obrero"
- [ ] madrid-chamberi.html - "Histórico Chamberí"
- [ ] madrid-hortaleza.html - "Zona Norte residencial"
- [ ] madrid-retiro.html - "Retiro elegante"
- [ ] madrid-salamanca.html - "Barrio premium"
- [ ] madrid-tetuan.html - "Tetuán multicultural"
- [ ] madrid-vallecas.html - "Vallecas industrial"
- [ ] **Contenido**: 800+ palabras ÚNICAS por barrio (no copiar)

### Microtarea 2.3: Humanizar Artículos Blog (8 textos)
- [ ] como-eliminar-olor-a-humo-en-casa.html
- [ ] como-limpiar-el-hollin-de-paredes-y-techos.html
- [ ] que-hacer-despues-de-un-incendio.html
- [ ] como-reclamar-al-seguro-tras-un-incendio.html
- [ ] el-seguro-cubre-la-limpieza-tras-un-incendio.html
- [ ] documentos-para-reclamar-al-seguro-tras-un-incendio.html
- [ ] peritaje-tras-un-incendio-como-funciona.html
- [ ] cuanto-cuesta-limpiar-una-casa-tras-un-incendio-madrid.html
- **Estilo**: Primera persona, preguntas retóricas, empatía

---

## CICLO 3: OPTIMIZACIÓN SEO - TÍTULOS Y DESCRIPTIONS (Mañana - 4h)

### Microtarea 3.1: Crear 15 Plantillas de Titles
```
1. "Limpieza de incendios en {ciudad} | Nano Nex - 24/7"
2. "Especialistas limpieza post incendio {ciudad} | Elimina hollín"
3. "Servicio urgente limpieza incendios {ciudad} | Nano Nex"
4. "{Ciudad}: Limpieza profesional tras incendio | Garantizado"
5. "Limpieza hollín y humo {ciudad} | Nano Nex emergencias 24/7"
... (15 total)
```
- [ ] Generar script de rotación (hash slug % 15)
- [ ] Incluir keyword + ciudad en title

### Microtarea 3.2: Crear 15 Plantillas de Meta Descriptions
```
1. "Limpieza profesional tras incendio en {ciudad}. Eliminamos hollín, humo y olores. Urgencias 24/7. ✓ Presupuesto sin compromiso."
2. "{Ciudad}: Especialistas en limpieza post incendio. Descontaminación de viviendas y locales. Garantía de resultado. Llamar ahora."
... (15 total)
```
- [ ] Máximo 160 caracteres
- [ ] Incluir keyword principal

### Microtarea 3.3: H1 con Keywords Principales
- [ ] Home: "Limpieza Post Incendio: Recupera tu hogar en [Madrid/Barcelona/etc.]"
- [ ] Landings: "[Limpieza de incendios en {Ciudad}] | Expertos Post Incendio"
- [ ] Artículos: Pregunta directa (ej: "¿Cómo eliminar olor a humo en casa?")

---

## CICLO 4: IMÁGENES CON SHARP (Mañana - 3h)

### Microtarea 4.1: Script Batch Optimization
- [ ] Crear `scripts/optimize-images.js` (ya existe, mejorar)
- [ ] Inputs: /imagenes/, /assets/img/
- [ ] Outputs: WebP 80% quality, max 2000px ancho
- [ ] Rename: original → `-opt.webp`

### Microtarea 4.2: Alt Text con Keywords
- [ ] Patrón: "{servicio} en {ciudad} - {descripción}"
  - ✅ "Limpieza de hollín en Madrid - antes y después de intervención"
  - ❌ "imagen.jpg"
- [ ] Validar todas las `<img>` tienen alt

### Microtarea 4.3: Procesar Todas las Imágenes
- [ ] `npm run optimize-images`
- [ ] Verificar output
- [ ] Actualizar referencias HTML a `-opt.webp`

---

## CICLO 5: INTERLINKING BÁSICO (Pasado mañana - 5h)

### Microtarea 5.1: Crear "También cubrimos" en cada landing Madrid
Ejemplo en madrid-carabanchel.html:
```html
<div class="otras-ciudades">
  <h3>También cubrimos</h3>
  <a href="limpieza-de-incendios-madrid-retiro.html">Retiro</a>
  <a href="limpieza-de-incendios-madrid-salamanca.html">Salamanca</a>
  <a href="limpieza-de-incendios-alcala-de-henares.html">Alcalá de Henares</a>
  ...
</div>
```
- [ ] Aplicar a los 7 barrios de Madrid

### Microtarea 5.2: Crear Sección "Provincias Cercanas"
En landing Madrid:
```html
<div class="provincias-cercanas">
  <h3>Limpieza de incendios en la región</h3>
  <a href="limpieza-incendios-barcelona/">Barcelona</a>
  <a href="limpieza-incendios-toledo/">Toledo</a>
  ...
</div>
```
- [ ] Madrid → Barcelona, Toledo, Segovia, Cuenca
- [ ] Cada provincia → municipios dentro

### Microtarea 5.3: Validar Enlaces Rotos
- [ ] `grep -r 'href="' . | grep -v "http" > enlaces_locales.txt`
- [ ] Verificar que archivos existen
- [ ] Arreglar / crear páginas faltantes

---

## CICLO 6: FRAGMENTOS DESTACADOS BÁSICO (En paralelo)

### Microtarea 6.1: Estructura "Respuesta Rápida"
En artículos, agregar al inicio:
```html
<div class="respuesta-rapida">
  <strong>Respuesta rápida:</strong> 
  [40-60 palabras respondiendo el título de forma concisa]
</div>
```
- [ ] Aplicar a 8 artículos blog principales

### Microtarea 6.2: Tablas Comparativas
Ejemplo en "Cómo limpiar hollín":
```html
<table>
  <tr><th>Método</th><th>Tiempo</th><th>Costo</th></tr>
  <tr><td>DIY</td><td>3-5 días</td><td>€</td></tr>
  <tr><td>Profesional</td><td>1-2 días</td><td>€€€</td></tr>
</table>
```
- [ ] Agregar a artículos "Cómo..." y "Cuánto cuesta"

---

## CICLO 7: PÁGINAS FALTANTES (Próxima semana)

### Microtarea 7.1: Página "Ubicaciones por Provincia"
Crear `/provincias/` con:
- [ ] Madrid
- [ ] Barcelona (Cataluña)
- [ ] Valencia (C. Valenciana)
- [ ] Sevilla (Andalucía)
- [ ] Murcia (Región de Murcia)
- [ ] Zaragoza (Aragón)
- [ ] Toledo (Castilla-La Mancha)
- [ ] Segovia (Castilla y León)

Cada provincia: links a municipios con landing

### Microtarea 7.2: Landings Nuevas - Ciudades Grandes
- [ ] Barcelona (+ 5 barrios)
- [ ] Valencia (+ 3 barrios)
- [ ] Sevilla
- [ ] Málaga
- [ ] Alicante
- [ ] Murcia
- [ ] Zaragoza
- [ ] Granada

**Contenido**: 800+ palabras únicas, particularidades locales

### Microtarea 7.3: Galería Antes/Después
- [ ] Crear `/galeria/`
- [ ] Clasificar fotos: Vivienda, Local, Industrial, Restaurante
- [ ] Agregar captions con ciudad + servicio
- [ ] Schema ImageGallery

---

## CICLO 8: METADATOS AVANZADOS (Próxima semana)

### Microtarea 8.1: Crear llms.txt
Archivo `/llms.txt` con:
```
# Nano Nex - Limpieza de Incendios

## Sobre nosotros
Especialistas en limpieza post incendio desde 1994...

## Servicios
- Limpieza de hollín
- Eliminación de olores
- Descontaminación
...

## Contacto
- Teléfono: 632 107 272
- Email: info@nanonex.es
- WhatsApp: wa.me/34632107272
```

### Microtarea 8.2: Mejorar robots.txt
```
User-agent: *
Allow: /
Disallow: /admin/
Sitemap: https://tu-dominio/sitemap.xml

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

### Microtarea 8.3: Crear Sitemap XML Dinámico
- [ ] Script que genere sitemap con todas las URLs
- [ ] Incluir: home, landings, artículos, provincias
- [ ] Actualizar robots.txt

---

## 📊 RESUMEN DE MICROTAREAS

| Ciclo | Tareas | Tiempo | Estado |
|-------|--------|--------|--------|
| 1: Contacto | 5 tareas | 2h | [ ] |
| 2: Humanización | 3 tareas | 6h | [ ] |
| 3: SEO Títulos | 3 tareas | 4h | [ ] |
| 4: Imágenes | 3 tareas | 3h | [ ] |
| 5: Interlinking | 3 tareas | 5h | [ ] |
| 6: Snippets | 2 tareas | 3h | [ ] |
| 7: Nuevas Páginas | 3 tareas | 8h | [ ] |
| 8: Metadatos | 3 tareas | 4h | [ ] |

**Total estimado**: 35 horas de trabajo

---

## 🚀 RECOMENDACIÓN

**Empezar hoy por Ciclo 1 (2h) + Ciclo 4 (3h) = 5h rápidas**
Luego Ciclo 2 y 3 en paralelo

¿Comenzamos por Ciclo 1 ahora?
