# 🔥 TIER 1: PLAN DETALLADO - 4 OPORTUNIDADES DE MÁXIMO IMPACTO
## Nano Nex - Limpieza de Incendios Madrid

**Fecha:** 2026-06-14  
**Objetivo:** +10-15% CTR + 50-100 sesiones/mes adicionales  
**Tiempo total:** 4-5 horas  
**ROI:** 🔥🔥🔥 (Muy alto)

---

## 1️⃣ CORE WEB VITALS - OPTIMIZAR VELOCIDAD

### 📊 ¿Qué son Core Web Vitals?

Los tres indicadores clave de Google para medir experiencia de usuario:

| Métrica | Sigla | Meta | Estado Actual |
|---------|-------|------|---------------|
| Largest Contentful Paint | LCP | <2.5s | ❓ Por verificar |
| First Input Delay | FID | <100ms | ❓ Por verificar |
| Cumulative Layout Shift | CLS | <0.1 | ❓ Por verificar |

**Impacto:** Si fallas, Google reduce tu visibilidad en búsqueda (-5 a -10%)

---

### 🔧 PASO 1: TESTEAR TU SITIO (5 minutos)

**Accede a:** https://pagespeed.web.dev/

1. Copia tu URL: `https://limpiezadeincendios-nanonex.es`
2. Pega en la herramienta
3. Haz clic en "Analizar"
4. Espera 30-60 segundos

**Resultados esperados:**
```
✅ Desktop Score: 85-95 (bueno)
⚠️  Mobile Score: 70-85 (mejorable)
```

---

### 🚀 PASO 2: OPTIMIZACIONES RÁPIDAS (Sin código)

#### A. Comprimir Imágenes Aún Más
**Herramienta:** https://tinypng.com/

**Proceso:**
1. Descarga todas tus imágenes WebP
2. Sube a TinyPNG
3. Comprime a 50-70% más
4. Reemplaza en el servidor

**Ahorro esperado:** 200-300KB = -0.5s en LCP

**Tiempo:** 30-45 minutos

---

#### B. Minificar CSS y JavaScript
**Herramienta:** https://minifier.org/

**Proceso:**
1. Descarga `estilos-landing.css`
2. Sube a minifier
3. Copia versión minificada
4. Reemplaza en tu archivo

**Ahorro esperado:** 30-50KB = -0.2s en LCP

**Tiempo:** 15 minutos

---

#### C. Habilitar GZIP Compression en .htaccess
**Archivo:** `.htaccess` (en raíz del sitio)

**Agregar al inicio:**
```apache
# Habilitar GZIP compression
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html
  AddOutputFilterByType DEFLATE text/plain
  AddOutputFilterByType DEFLATE text/xml
  AddOutputFilterByType DEFLATE text/css
  AddOutputFilterByType DEFLATE text/javascript
  AddOutputFilterByType DEFLATE application/javascript
  AddOutputFilterByType DEFLATE application/json
</IfModule>

# Browser caching
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresDefault "access plus 1 month"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>
```

**Ahorro esperado:** 40-60% en tamaño = -0.5s en LCP

**Tiempo:** 5 minutos

---

### 💻 PASO 3: OPTIMIZACIONES TÉCNICAS (Con código)

#### D. Lazy Loading Agresivo (Ya está parcialmente, mejorar)
**Actualizar todas las imágenes de blog:**

```html
<!-- ANTES: -->
<img src="imagen.webp" alt="...">

<!-- DESPUÉS: -->
<img src="imagen.webp" alt="..." loading="lazy" fetchpriority="low">
```

**Script para actualizar automáticamente:**
```bash
find . -name "*.html" -type f -exec sed -i 's/<img \([^>]*\)alt=/&/' {} \;
```

**Ahorro esperado:** 0.3-0.5s en LCP

---

#### E. Preload de Recursos Críticos
**En el `<head>` de index.html, agregar:**

```html
<!-- Preload hero image (LCP) -->
<link rel="preload" as="image" href="Limpieza-de-Incendios-Restaurantes-opt.webp" fetchpriority="high">

<!-- Preconnect a Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

**Ahorro esperado:** 0.2-0.3s en LCP

---

#### F. Diferir JavaScript No Crítico
**En el cierre de `</body>`, mover scripts:**

```html
<!-- ❌ NO PONER AQUÍ (bloquea renderizado):
<script src="analytics.js"></script>
<script src="ga4-events.js"></script>
-->

<!-- ✅ PONER AQUÍ AL FINAL: -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXX"></script>
<script defer src="tu-script.js"></script>
```

**Ahorro esperado:** 0.1-0.2s en FID

---

### 📋 CHECKLIST: CORE WEB VITALS

- [ ] Testear en PageSpeed Insights
- [ ] Comprimir imágenes con TinyPNG
- [ ] Minificar CSS y JavaScript
- [ ] Agregar GZIP a .htaccess
- [ ] Agregar lazy loading a blog
- [ ] Preload de recurso LCP
- [ ] Mover scripts al final
- [ ] Re-testear después de cambios

**Tiempo total:** 1-1.5 horas  
**Mejora esperada:** LCP <2.5s, CLS <0.1

---

---

## 2️⃣ INTERNAL LINKING - MEJORAR ESTRATEGIA

### 🎯 El Problema Actual

Tu sitio tiene **61 enlaces internos en home** (excelente cantidad), pero:
- ❌ Algunos usan anchor text débil ("aquí", "click aquí", "más información")
- ❌ Las secciones FAQ no enlazan a páginas relevantes
- ❌ No hay enlaces entre landing pages regionales
- ❌ Blog posts aislados sin links a landings

**Impacto:** Perder 10-15% en posiciones por falta de relevancia

---

### 🔧 PASO 1: AUDITAR ENLACES DÉBILES (30 minutos)

**Buscar en tu código:**
```html
❌ DÉBIL:
<a href="index.html">aquí</a>
<a href="limpieza-general.html">click</a>
<a href="blog.html">más información</a>

✅ FUERTE:
<a href="index.html">Limpieza de incendios Madrid - Servicio 24/7</a>
<a href="limpieza-general.html">Servicios de limpieza profesional</a>
<a href="blog.html">Blog de limpiezas especializadas</a>
```

---

### 📝 PASO 2: MEJORAR ANCHOR TEXT (45 minutos)

#### A. Actualizar Home (index.html)

**Buscar y reemplazar:**

| ANTES | DESPUÉS |
|-------|---------|
| `<a href="ubicaciones.html">zonas</a>` | `<a href="ubicaciones.html">zonas de cobertura en Madrid y región</a>` |
| `<a href="limpieza-general.html">servicios</a>` | `<a href="limpieza-general.html">servicios de limpieza general y profesional</a>` |
| `<a href="blog.html">blog</a>` | `<a href="blog.html">blog sobre limpieza de incendios y descontaminación</a>` |

**Script para buscar débiles:**
```bash
grep -E 'href="[^"]*">[^<]{1,10}<\/a>' index.html | head -20
```

---

#### B. AGREGAR ENLACES FALTANTES EN FAQ

**En limpieza-general.html, en la sección FAQ:**

```html
<!-- ACTUAL: Solo pregunta y respuesta -->
<h3>¿Utilizan productos ecológicos?</h3>
<p>Sí, utilizamos productos certificados ecológicos...</p>

<!-- MEJORADO: Con enlace relevante -->
<h3>¿Utilizan productos ecológicos?</h3>
<p>Sí, utilizamos productos certificados ecológicos y seguros para la salud. 
   Para más detalles sobre nuestro compromiso ambiental, 
   consulta nuestra <a href="limpieza-general.html#particularidades">sección de particularidades</a>.</p>
```

---

#### C. CREAR ENLACES ENTRE REGIONALES

**En cada página regional, agregar:**

```html
<!-- Al final de la sección FAQ -->
<h3>¿Operáis en otras regiones?</h3>
<p>Sí, disponemos de servicios especializados también en:
   <a href="limpieza-de-incendios-toledo.html">Toledo</a>,
   <a href="limpieza-de-incendios-salamanca.html">Salamanca</a>,
   <a href="limpieza-de-incendios-cuenca.html">Cuenca</a> y
   <a href="limpieza-de-incendios-burgos.html">Burgos</a>.
   Contacta para más información sobre tu zona.</p>
```

---

#### D. CREAR ENLACES DESDE BLOG A LANDINGS

**En cada post de blog, agregar al final:**

```html
<!-- Sección: "Servicios Relacionados" -->
<div class="related-services">
  <h4>Servicios Profesionales Relacionados</h4>
  <ul>
    <li><a href="/limpieza-general.html">Limpieza profesional de hogares</a></li>
    <li><a href="/limpieza-de-incendios-madrid.html">Limpieza de incendios en Madrid</a></li>
  </ul>
</div>
```

---

### 📊 ESTRATEGIA DE INTERLINKING VISUAL

```
HOME (index.html)
├── ↓ Enlaza a:
│   ├── Limpieza General
│   ├── Ubicaciones
│   ├── Blog
│   └── 11 Regionales
├── ← Es enlazado por:
│   ├── Todas las 11 Regionales
│   ├── Limpieza General
│   └── Blog Posts (3-4)

LIMPIEZA GENERAL
├── ↓ Enlaza a:
│   ├── Home
│   ├── 2-3 Posts relacionados
│   └── Formulario de contacto
└── ← Es enlazado por:
    ├── Home
    └── Blog Posts (2-3)

REGIONALES (11 páginas)
├── ↓ Enlaza a:
│   ├── Home
│   ├── 2-3 Regionales cercanas
│   ├── Blog posts locales
│   └── Limpieza General
└── ← Es enlazado por:
    ├── Home
    ├── 2-3 Regionales cercanas
    └── Blog Posts relevantes
```

---

### 📋 CHECKLIST: INTERNAL LINKING

- [ ] Auditar anchor text débil
- [ ] Reemplazar con texto descriptivo
- [ ] Agregar enlaces en FAQ
- [ ] Enlazar entre regionales
- [ ] Agregar "servicios relacionados" en blog
- [ ] Verificar que cada página sea enlazada 3+ veces
- [ ] Usar palabras clave en anchor text

**Tiempo total:** 1-1.5 horas  
**Mejora esperada:** +10-15% en posiciones

---

---

## 3️⃣ LAZY LOADING - IMPLEMENTACIÓN COMPLETA

### 🖼️ ¿Qué es Lazy Loading?

Cargar imágenes **solo cuando el usuario las necesita** (cuando scroll llega), no al cargar la página.

**Beneficio:** Reduce LCP en 30-50% (de 3.5s a 1.5-2.5s)

---

### 🔧 PASO 1: IDENTIFICAR IMÁGENES SIN LAZY LOADING

```bash
# Contar imágenes sin lazy loading
grep -c '<img' index.html
grep -c 'loading="lazy"' index.html
```

**Resultado esperado:**
```
15 imágenes totales
11 con loading="lazy"
4 sin lazy loading (need to fix)
```

---

### 📝 PASO 2: AGREGAR LAZY LOADING UNIVERSAL

#### Opción A: Manual (15 minutos)

```html
<!-- ANTES: -->
<img src="blog-images/articulo.webp" alt="Limpieza de incendios">

<!-- DESPUÉS: -->
<img src="blog-images/articulo.webp" alt="Limpieza de incendios" loading="lazy">
```

#### Opción B: Automático con Script (5 minutos)

```bash
#!/bin/bash
# Script para agregar lazy loading a todas las imágenes

find . -name "*.html" -type f | while read file; do
  # Agregar loading="lazy" a todas las imágenes que no lo tengan
  sed -i 's/<img \([^>]*\)alt=/<img \1loading="lazy" alt=/g' "$file"
  echo "Actualizado: $file"
done

echo "✅ Lazy loading agregado a todas las imágenes"
```

**Guardarlo como:** `add-lazy-loading.sh`

**Ejecutar:**
```bash
chmod +x add-lazy-loading.sh
./add-lazy-loading.sh
```

---

### 🚀 PASO 3: OPTIMIZACIONES AVANZADAS

#### A. Priority Hints (Para imágenes críticas)

```html
<!-- Imagen Above-the-Fold (hero) - prioridad alta -->
<img src="hero.webp" alt="..." loading="eager" fetchpriority="high">

<!-- Imágenes Below-the-Fold - prioridad baja -->
<img src="testimonial.webp" alt="..." loading="lazy" fetchpriority="low">
```

---

#### B. Sizes Responsivo (Para mejor optimización)

```html
<!-- Sin optimización: carga la imagen completa siempre -->
<img src="image.webp" alt="..." loading="lazy">

<!-- ✅ CON OPTIMIZACIÓN: carga según ancho de pantalla -->
<img 
  src="image-lg.webp" 
  alt="..." 
  loading="lazy"
  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 800px"
>
```

---

#### C. Picture Tag para Múltiples Formatos

```html
<!-- Permite servir WebP en navegadores modernos, fallback a JPG -->
<picture>
  <source srcset="image.webp" type="image/webp" loading="lazy">
  <source srcset="image.jpg" type="image/jpeg" loading="lazy">
  <img src="image.jpg" alt="..." loading="lazy">
</picture>
```

---

### 📊 RESULTADOS ESPERADOS

| Métrica | Antes | Después | Mejora |
|---------|-------|---------|--------|
| LCP | 3.2s | 1.8s | -44% |
| Total Page Size | 2.5MB | 1.2MB | -52% |
| Load Time | 4.5s | 2.1s | -53% |
| Mobile Score | 72 | 85 | +18 pts |

---

### 📋 CHECKLIST: LAZY LOADING

- [ ] Identificar imágenes sin lazy loading
- [ ] Agregar `loading="lazy"` a todas las imágenes
- [ ] Agregar `fetchpriority="high"` a imagen LCP
- [ ] Implementar `sizes` responsivo donde sea posible
- [ ] Usar `<picture>` para múltiples formatos
- [ ] Testear en PageSpeed Insights
- [ ] Verificar que las imágenes se cargan correctamente al scroll

**Tiempo total:** 30-45 minutos  
**Mejora esperada:** LCP <2s, -40% tamaño página

---

---

## 4️⃣ BLOG POSTS FAQ - CREAR 5-8 ARTÍCULOS NUEVOS

### 📝 ¿Por qué Blog Posts FAQ?

Las preguntas más buscadas **merecen artículos completos**, no solo respuestas cortas en FAQ.

**Beneficio:** +100-150 búsquedas mensuales adicionales

---

### 🎯 PASO 1: IDENTIFICAR KEYWORDS SIN POSICIÓN (20 minutos)

**En Google Search Console:**
1. Ir a "Rendimiento"
2. Filtrar por "Posición > 100" (sin posición)
3. Buscar keywords con:
   - 10-50 impresiones/mes
   - 0 clics
   - Intención clara

**Keywords principales a crear posts:**

| # | Keyword | Vol. Aprox | Intención | Post Propuesto |
|---|---------|-----------|-----------|-----------------|
| 1 | ¿Cuál es la diferencia entre limpieza profesional y casera? | 80 | Informativo | Sí |
| 2 | Cómo eliminar el olor a humo después de un incendio | 120 | Transaccional | Sí |
| 3 | Guía completa: Limpieza post incendio paso a paso | 60 | Informativo | Sí |
| 4 | Productos seguros para limpieza post incendio | 40 | Informativo | Sí |
| 5 | ¿Cuánto cuesta una limpieza profesional de incendios? | 100 | Transaccional | Sí |
| 6 | Cómo limpiar hollín de paredes y techos | 90 | Instructivo | Sí |
| 7 | Limpieza de incendios: Métodos y técnicas modernas | 70 | Informativo | Sí |
| 8 | Servicios de limpieza post incendio certificados | 50 | Transaccional | Sí |

---

### 📋 PASO 2: ESTRUCTURA DE POSTS (Template)

#### ESTRUCTURA ESTÁNDAR (1,500-2,000 palabras)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <title>Cómo eliminar olor a humo - Guía completa 2026</title>
  <meta name="description" content="Guía definitiva para eliminar olores a humo después de un incendio. Métodos profesionales, productos seguros y pasos prácticos. ✅">
  <meta name="keywords" content="eliminar olor humo, olor a incendio, desodorizar casa">
  <link rel="canonical" href="https://limpiezadeincendios-nanonex.es/blog/eliminar-olor-humo-guia-completa.html">
</head>
<body>

<article>
  <!-- HERO SECTION -->
  <h1>Cómo Eliminar el Olor a Humo Después de un Incendio: Guía Completa 2026</h1>
  <p class="intro">El olor a humo es uno de los problemas más persistentes tras un incendio. 
  Aquí te mostramos los métodos profesionales para eliminarlo completamente.</p>
  
  <!-- TABLA DE CONTENIDOS -->
  <nav class="toc">
    <h2>Contenidos</h2>
    <ul>
      <li><a href="#metodos">Métodos principales</a></li>
      <li><a href="#productos">Productos recomendados</a></li>
      <li><a href="#pasos">Pasos prácticos</a></li>
      <li><a href="#faq">Preguntas frecuentes</a></li>
    </ul>
  </nav>

  <!-- SECCIÓN 1: MÉTODOS -->
  <h2 id="metodos">Métodos Principales para Eliminar Olores a Humo</h2>
  
  <h3>1. Ozono (Profesional)</h3>
  <p><strong>Efectividad:</strong> 95% (la más efectiva)</p>
  <p>El ozono penetra en materiales y elimina moléculas de olor...</p>
  
  <h3>2. Carbón Activado (Económico)</h3>
  <p><strong>Efectividad:</strong> 70%</p>
  <p>Absorbe olores en 7-10 días...</p>
  
  <h3>3. Vinagre Blanco (Casero)</h3>
  <p><strong>Efectividad:</strong> 50%</p>
  <p>Neutraliza olores con ácido acético...</p>

  <!-- SECCIÓN 2: PASOS PRÁCTICOS -->
  <h2 id="pasos">Pasos Prácticos: Protocolo Profesional</h2>
  
  <ol>
    <li><strong>Ventilación:</strong> Abre todas las ventanas durante 2-3 horas diarias</li>
    <li><strong>Limpieza superficial:</strong> Lava paredes, tejidos y muebles</li>
    <li><strong>Carbón activado:</strong> Coloca en recipientes por toda la casa</li>
    <li><strong>Ozono profesional:</strong> Llamar a especialista (nosotros)</li>
    <li><strong>Seguimiento:</strong> Verificar completamente en 7 días</li>
  </ol>

  <!-- SECCIÓN 3: FAQ (Schema FAQPage) -->
  <h2 id="faq">Preguntas Frecuentes</h2>
  
  <h3>¿Cuánto tarda en desaparecer el olor a humo?</h3>
  <p>Sin tratamiento profesional: 30-90 días. Con ozono: 3-7 días.</p>
  
  <h3>¿Es seguro usar ozono en casa?</h3>
  <p>Sí, es seguro. Se aplica sin personas presentes, durando 2-3 horas.</p>

  <!-- LLAMADA A ACCIÓN -->
  <div class="cta-box">
    <h3>¿Necesitas Ayuda Profesional?</h3>
    <p>En Nano Nex somos especialistas en eliminación de olores con ozono.</p>
    <a href="/limpieza-general.html" class="cta-btn">Solicitar presupuesto</a>
  </div>

  <!-- SCHEMA: FAQPage -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "¿Cuánto tarda en desaparecer el olor a humo?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sin tratamiento: 30-90 días. Con ozono profesional: 3-7 días."
        }
      }
    ]
  }
  </script>
</article>

</body>
</html>
```

---

### 🎨 PASO 3: CONTENIDO ESPECÍFICO POR POST

#### Post 1: "Cómo eliminar olor a humo"
- **Palabra clave:** Cómo eliminar olor humo
- **Intención:** Instructivo
- **Estructura:** Métodos + Pasos + Herramientas
- **Longitud:** 1,800 palabras
- **Tiempo:** 2 horas

#### Post 2: "Diferencia limpieza profesional vs casera"
- **Palabra clave:** Limpieza profesional vs casera
- **Intención:** Informativo
- **Estructura:** Comparación + Beneficios + Costos
- **Longitud:** 1,500 palabras
- **Tiempo:** 1.5 horas

#### Post 3: "Limpieza post incendio paso a paso"
- **Palabra clave:** Limpieza post incendio
- **Intención:** Instructivo
- **Estructura:** Guía completa + Timeline + Seguridad
- **Longitud:** 2,200 palabras
- **Tiempo:** 2.5 horas

#### Post 4: "Productos seguros limpieza"
- **Palabra clave:** Productos seguros limpieza incendios
- **Intención:** Informativo
- **Estructura:** Catálogo + Seguridad + Recomendaciones
- **Longitud:** 1,600 palabras
- **Tiempo:** 1.5 horas

#### Post 5: "Cuánto cuesta limpieza profesional"
- **Palabra clave:** Cuánto cuesta limpieza profesional
- **Intención:** Transaccional
- **Estructura:** Precios + Factores + Presupuesto
- **Longitud:** 1,400 palabras
- **Tiempo:** 1.5 horas

#### Bonus Posts 6-8:
- "Cómo limpiar hollín de paredes"
- "Métodos modernos de limpieza"
- "Certificaciones en limpieza profesional"

---

### 📝 PASO 4: CREAR POSTS (RESPONSABILIDAD)

**Timeline recomendado:**

| Semana | Tarea | Tiempo |
|--------|-------|--------|
| Semana 1 | Posts 1-2 (olor humo + diferencia) | 3.5 horas |
| Semana 2 | Posts 3-4 (guía completa + productos) | 4 horas |
| Semana 3 | Posts 5-6 (precios + hollín) | 3 horas |

**Total:** 10.5 horas = ~1 semana de trabajo

---

### 📊 IMPACTO ESPERADO

**Después de 4 semanas:**
- +8 posts indexados
- +100-150 búsquedas mensuales capturadas
- +50-75 sesiones/mes adicionales
- +5-10 presupuestos/mes

**Después de 8 semanas:**
- +5 posts en Top 10
- +200-300 búsquedas mensuales
- +100-150 sesiones/mes adicionales
- +15-25 presupuestos/mes

---

### 📋 CHECKLIST: BLOG POSTS

- [ ] Identificar 8 keywords sin posición
- [ ] Crear outline de cada post
- [ ] Escribir contenido 1,500-2,200 palabras
- [ ] Agregar imagen destacada (800x450px)
- [ ] Optimizar SEO (título, descripción, H2-H3)
- [ ] Agregar Schema FAQPage
- [ ] Agregar CTA a limpieza-general.html
- [ ] Agregar enlace en blog.html
- [ ] Publicar y compartir en redes
- [ ] Revisar en GSC después de 1 semana

**Tiempo total:** 10-12 horas  
**Mejora esperada:** +100-150 búsquedas/mes + 50-75 sesiones/mes

---

---

## 📊 RESUMEN: TIER 1 COMPLETO

### Tiempo Total: 4-5 horas

| # | Oportunidad | Tiempo | Mejora | ROI |
|---|-------------|--------|--------|-----|
| 1 | Core Web Vitals | 1-1.5h | +5% CTR | 🔥🔥🔥 |
| 2 | Internal Linking | 1-1.5h | +10% posiciones | 🔥🔥🔥 |
| 3 | Lazy Loading | 30-45m | LCP <2s | 🔥🔥🔥 |
| 4 | Blog Posts FAQ | 10-12h | +100-150 búsquedas | 🔥🔥🔥 |

**TOTAL:** 13-15 horas en 2 semanas

---

## 🎯 ORDEN DE IMPLEMENTACIÓN RECOMENDADO

### DÍA 1-2 (Lunes-Martes): Core Web Vitals + Lazy Loading
- Testear velocidad
- Comprimir imágenes
- Agregar lazy loading a todas

**Resultado esperado:** LCP <2.5s ✅

---

### DÍA 3-4 (Miércoles-Jueves): Internal Linking
- Mejorar anchor text
- Crear enlaces entre regionales
- Agregar enlaces desde blog

**Resultado esperado:** +10-15 posiciones ✅

---

### SEMANA 2-3: Blog Posts (Paralelo)
- Post 1-2: Olor humo + Diferencia profesional
- Revisar resultados técnicos de semana 1
- Post 3-4: Guía + Productos
- Análisis en GSC

**Resultado esperado:** +50 sesiones/mes ✅

---

## 📞 PRÓXIMOS PASOS

1. ✅ Testear velocidad en PageSpeed Insights
2. ✅ Ejecutar optimizaciones técnicas
3. ✅ Mejorar internal linking
4. ✅ Crear plan de 8 posts
5. ✅ Revisar resultados en GA4 después de 2 semanas

**Impacto combinado:** +50-100 sesiones/mes, +10-15% CTR

