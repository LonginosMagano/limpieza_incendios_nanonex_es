# PLAN CRÍTICO 3A + 3B: Limpieza Blog & Expansión Geográfica
**Nano Nex Madrid - Limpieza Post Incendio**

---

## EJECUTIVO

Este plan aborda dos críticos del negocio:
1. **CRÍTICO 3A:** Blog contiene 50% de contenido OFF-TOPIC (100/201 posts) que diluy autoridad SEO
2. **CRÍTICO 3B:** Expansión geográfica a 11 nuevas ciudades para capturar 570-840 búsquedas/mes

**Impacto combinado:** +2-5 clientes nuevos/mes + enfoque especializado en post-incendio

---

# PARTE 1: ANÁLISIS DE BLOG (CRÍTICO 3A)

## 1.1 Resumen de hallazgos

```
Total posts en blog.html: 201 posts únicos
Publicados: 2017-2025 (8 años de contenido)
```

### Distribución por clúster

| Clúster | Cantidad | % | Acción |
|---------|----------|-----|--------|
| **1. Post-Incendio** (MANTENER) | 81 | 40.3% | Conservar |
| **5. Técnicas Especiales** (MANTENER) | 20 | 9.9% | Conservar |
| **4. Ciudades/Geografía** (MANTENER) | 0 | 0% | Crear con nueva expansión |
| **3. Limpieza General** (ELIMINAR) | 100 | 49.8% | Redirect 301 |
| **2. Seguros** (MANTENER - no encontrados)* | 0 | 0% | Crear si falta |
| **TOTAL RELEVANTE** | 101 | 50.2% | |
| **TOTAL OFF-TOPIC** | 100 | 49.8% | |

*Nota: Algunos posts sobre incendios incluyen info asegurador, pero no hay categoría dedicada a "seguros" como clúster puro.

## 1.2 Clúster 1: Post-Incendio (81 posts - MANTENER)

**Ejemplos:**
- "8 Estrategias Para la Limpieza de Paredes Después de un Incendio"
- "Guía Completa para la Limpieza de Incendios"
- "10 pasos para eliminar olores persistentes tras un incendio en bares"
- "Limpieza Post Incendio: El Humo"
- "Pasos para limpiar las paredes dañadas por Humo"
- "Limpieza de Incendios en restaurantes"
- "Fuego y humo: la operación de limpieza Post incendios"

**Estrategia:** Mantener todos. Reorganizar por subcategorías internas.

---

## 1.3 Clúster 5: Técnicas Especiales (20 posts - MANTENER)

**Ejemplos:**
- "Limpieza de Teclados Portátiles: ¿Es Necesario Usar Aire Comprimido?"
- "Limpiezas con láser: consejos y usos"
- "Limpieza con Ozono" (múltiples)
- "Limpieza criogénica"

**Estrategia:** Mantener. Son diferenciadores técnicos (ozono, láser, HEPA).

---

## 1.4 Clúster 3: Limpieza General - OFF-TOPIC (100 posts - ELIMINAR)

### Categorías de OFF-TOPIC encontradas:

**Limpieza del hogar genérica (35 posts):**
- Cómo limpiar a fondo tu ducha en 4 pasos
- Limpiar un Inodoro de Forma Profesional
- Las 5 claves para desinfección de mesas del comedor
- CÓMO LIMPIAR TU CORTINA DE DUCHA
- 4 TAREAS DOMÉSTICAS QUE QUEMAN CALORÍAS
- Cómo deshacerse de las moscas de la fruta
- Cómo limpiar tus espejos sin dejar marcas
- Con qué frecuencia debe fregar sus Suelos
- 7 consejos para organizar tu cocina
- Limpieza de teclados portátiles

**Limpieza industrial genérica (30 posts):**
- Limpieza Industrial: Los Retos Más Comunes
- Limpieza de Oficinas: Consejos Efectivos
- Limpieza de Garajes
- Limpieza de Hospitales
- Limpieza profunda de oficinas
- Mantenimiento de tiendas
- Limpieza de fábricas

**Limpiezas de acumulación / Síndrome de Diógenes (28 posts):**
- "Limpieza de Síndrome de Diógenes (16)"
- "Limpieza Diógenes (9)"
- Limpieza de acumulación (múltiples)

**Otros (7 posts):**
- Desinfección genérica (COVID)
- Limpieza de alfombras
- Limpieza de chimeneas (genérica, no post-incendio)

### Problema estratégico

**Dilución de autoridad temática:** Google ve el sitio como "limpieza genérica" en lugar de especialista en "post-incendio".

**Impacto:**
- Cannibalización de búsquedas (posts genéricos vs posts post-incendio compiten por mismo crawl budget)
- Baja intención de conversión (usuario que llega por "limpiar ducha" no contrata limpieza post-incendio)
- Señal débil de E-E-A-T (Google no ve especialización)

---

## 1.5 Recomendación: Opción B - Redirects 301

### Estrategia elegida

Redirigir los **100 posts OFF-TOPIC** a una **nueva landing genérica** (`/limpieza-general.html` o `/servicios.html`) con **301 permanentes**.

### Ventajas

✓ Preserva autoridad de dominio (enlaces externos siguen fluyendo)  
✓ Preserva "link juice" interno  
✓ Reduce crawl budget desperdiciado  
✓ Mejora UX (usuarios redirigidos a contenido relevante)  
✓ Mantiene historial en Google Search Console  
✓ No perderá posicionamiento para búsquedas genéricas (se redirigen)  

### Implementación

**Paso 1:** Crear página `/limpieza-general.html`
- Hero: "Servicios de limpieza profesional diversa"
- Contenido: breve descripción de servicios (garajes, limpieza industrial, etc.)
- CTA: "¿Limpieza post-incendio? Contacta aquí"
- Meta: robots `index, follow` pero sin canonical a post-incendio

**Paso 2:** Agregar a `.htaccess`

```apache
# Redirect OFF-TOPIC posts to general cleaning page
RedirectMatch 301 ^/blog/2024/11/27/como-limpiar-a-fondo-tu-ducha-en-solo-4-pasos/$ /limpieza-general.html
RedirectMatch 301 ^/blog/2018/06/20/limpiar-un-inodoro-de-forma-profesional/$ /limpieza-general.html
RedirectMatch 301 ^/blog/2024/12/25/las-5-claves-para-una-correcta-desinfeccion-de-las-mesas-del-comedor/$ /limpieza-general.html
RedirectMatch 301 ^/blog/2018/06/19/como-limpiar-tu-cortina-de-ducha/$ /limpieza-general.html
[... 96 más ...]
```

**Paso 3:** Actualizar `sitemap.xml`
- Remover URLs de los 100 posts (o marcarlos como `<changefreq>never</changefreq>`)
- Agregar `/limpieza-general.html`

**Paso 4:** Notificar en Google Search Console
- Subir nuevo sitemap
- Verificar que 301s se procesan correctamente

---

## 1.6 Reestructura del Blog

### Estructura propuesta

```
Blog de Nano Nex
├─ Limpieza Post-Incendio (81 posts)
│  ├─ Hollín y humo (30 posts)
│  ├─ Técnicas de limpieza (20 posts)
│  ├─ Restauración de espacios (15 posts)
│  ├─ Incendios comerciales (16 posts)
│
├─ Técnicas Especiales (20 posts)
│  ├─ Ozono (3 posts)
│  ├─ Láser (7 posts)
│  ├─ Criogénico (2 posts)
│  ├─ HEPA (8 posts)
│
├─ Prevención (0 posts - crear si necesario)
│  └─ Cómo prevenir incendios (nuevo)
│
└─ Limpieza General [REDIRIGIDA] (100 posts → /limpieza-general.html)
```

### Implementación

Actualizar `blog.html`:
- Renombrar secciones por subcategoría
- Quitar "Limpieza (51)" → renombramiento confuso
- Agregar sección "Limpieza Post-Incendio" con los 81 posts core

---

## 1.7 Impacto estimado

| Métrica | Antes | Después |
|---------|-------|---------|
| Posts relevantes | 101/201 (50%) | 101/201 (50%) |
| Posts indexados | 201 | 1 (limpieza-general) |
| Crawl budget usado | Disperso | Concentrado en core |
| E-E-A-T señal | Débil | Fuerte |
| Tasa de conversión esperada | 1-2% | 2-4% (más calidad) |

---

# PARTE 2: EXPANSIÓN GEOGRÁFICA (CRÍTICO 3B)

## 2.1 Análisis de cobertura actual

### Landings existentes (48 archivos HTML)

```
MADRID (11 landings)
├─ Centro: 8 landings (Retiro, Chamberi, Salamanca, Tetuan, Vallecas, Hortaleza, Carabanchel, + hollin-madrid)
└─ Periférica: 3 landings (Alcalá, Getafe, Tres Cantos, + otros: Alcobendas, Alcorcón, Colmenar, Fuenlabrada, Leganés, Móstoles, Torrejón)

BARCELONA (6 landings)
├─ Distritos: Eixample, Gracia, Horta, Montjuic, Sarria, + región

VALENCIA (4 landings)
├─ Distritos: Campanar, Centro, Rascanya, + región

OTRAS (27 landings)
├─ Andalucía: Málaga, Córdoba, Granada, Sevilla, Jaén, Almería, Huelva, Cádiz, etc.
├─ Aragón: Zaragoza
├─ Cataluña: Bilbao (error - es Euskadi)
├─ Islas: Palma de Mallorca
└─ Especiales: Laboratorios (1 landing)

TOTAL: ~48 landings post-incendio
```

### Gaps identificados

| Región | Cobertura | Gap | Oportunidad |
|--------|-----------|-----|------------|
| Madrid | 11/1 + periférica | Excelente | Saturado |
| Barcelona | 6 landings | Buena | Municipios vecinos (Sabadell, Tarrasa) |
| Valencia | 4 landings | Parcial | Alicante (+ Elche, Torrevieja) + Castellón |
| Andalucía | 8+ landings | Parcial | Jaén (gap), Huelva (gap) |
| Castilla-La Mancha | 0 landings | **CRÍTICO** | Toledo, Cuenca, Ciudad Real, Albacete |
| Castilla y León | 0 landings | **CRÍTICO** | Valladolid, Burgos, Salamanca, León |
| Aragón | 1 landing (Zaragoza) | Parcial | Huesca, Teruel |
| Región Murcia | 1 landing (Murcia) | Parcial | Cartagena, Lorca |
| C. Valenciana | 1 región + Valencia | Parcial | **ALTO VALOR:** Alicante, Castellón |

---

## 2.2 Plan de 11 landings nuevas

### TIER 1: Alto valor (5 landings)

Enfoque en capitales provinciales con población 100K+, actividad comercial alta.

| # | Ciudad | Provincia | CCAA | Población | Contexto | Municipios vecinos |
|---|--------|-----------|------|-----------|----------|-------------------|
| 1 | **Valladolid** | Valladolid | Castilla y León | 305K | Industria alimentaria, fabricación, inviernos duros | Tordesillas, Peñafiel, Medina del Campo |
| 2 | **Burgos** | Burgos | Castilla y León | 178K | Medieval, patrimonio, humedad norte | Aranda de Duero, Briviesca |
| 3 | **Toledo** | Toledo | Castilla-La Mancha | 84K | Turismo UNESCO, ciudad histórica densa | Talavera de la Reina, Orgaz |
| 4 | **Murcia** | Murcia | Región Murcia | 468K | Calor, clima continentalizado, agricultura | Cartagena, Lorca, Cieza |
| 5 | **Jaén** | Jaén | Andalucía | 114K | Olivicultura, rural, industria agraria | Linares, Andújar, Baeza |

**Volume estimado:** 380-510 búsquedas/mes

---

### TIER 2: Valor medio (4 landings)

Capitales provinciales con población 35-150K, valor comercial menor pero mercado desatendido.

| # | Ciudad | Provincia | CCAA | Población | Contexto | Municipios vecinos |
|---|--------|-----------|------|-----------|----------|-------------------|
| 6 | **Huesca** | Huesca | Aragón | 52K | Montaña, Pirineo, turismo | Jaca, Barbastro |
| 7 | **Teruel** | Teruel | Aragón | 35K | Rural extremo, despoblación | Alcañiz, Calamocha |
| 8 | **Salamanca** | Salamanca | Castilla y León | 143K | Universitaria, patrimonio histórico | Ciudad Rodrigo, Guijuelo |
| 9 | **Cuenca** | Cuenca | Castilla-La Mancha | 54K | Casas colgadas, turismo, rural | Requena, Tarancón |

**Volume estimado:** 80-160 búsquedas/mes

---

### TIER 3: Mantenimiento (2 landings)

Expandir cobertura en comunidades ya presentes (Valencia).

| # | Ciudad | Provincia | CCAA | Población | Contexto | Municipios vecinos |
|---|--------|-----------|------|-----------|----------|-------------------|
| 10 | **Alicante** | Alicante | C. Valenciana | 330K | Costa Blanca, humedad marina, turismo | Elche, Torrevieja, Orihuela |
| 11 | **Castellón** | Castellón | C. Valenciana | 174K | Cerámica, Costa Dorada, industria | Oropesa del Mar, Vinarós |

**Volume estimado:** 110-170 búsquedas/mes

---

## 2.3 Copy templates personalizados

### Template base (estándar)

```html
<!-- Hero personalizado por ciudad -->
<section class="hero-landing" style="background-image: ...">
    <h1>[Ciudad]: Expertos limpieza post incendio - [Contexto local]</h1>
    <p>[Párrafo contextual 80-120 palabras]</p>
    <a href="#contacto" class="cta-btn">Pide presupuesto gratis</a>
</section>

<!-- Reutilizable: Todo excepto H1, párrafo contexto y municipios -->
```

### VALLADOLID (Tier 1) - Ejemplo completo

**Hero H1:**
```
Limpieza de incendios en Valladolid: Cuando la industria se detiene
```

**Párrafo contexto:**
```
Valladolid es fábrica. Plantas alimentarias, metalurgia, transformación industrial. Pero también es ciudad de abuelos, de barrios residenciales donde viven familias que nunca pensaron en un incendio. Los incendios en Valladolid tienen carácter: humo denso de combustión industrial o doméstica, hollín que se adhiere en la sequedad del clima central castellano, corrosión rápida de acero. Un incendio aquí paraliza negocios y vidas. La limpieza debe ser rápida y técnica.

En Valladolid, la industria alimentaria genera humo específico con residuos grasientos. La fabricación libera partículas metálicas. El clima seco del interior de Castilla hace que el hollín se enquiste sin la humedad que lo humedecería. Además, Valladolid tiene inviernos duros: el humo se adhiere a ventanas frías, se cristaliza en grietas. Por eso la limpieza debe comenzar en 24 horas.
```

**FAQ personalizada:**
1. ¿Cuánto cuesta limpiar un incendio en una vivienda de Valladolid?
   - Respuesta: 900-2.500€ según tamaño (reutilizable)
   
2. ¿Limpiáis naves industriales en Valladolid?
   - Respuesta: Sí, Nano Nex trabaja con plantas alimentarias y transformación industrial
   
3. ¿Cuánto tardan en llegar a Valladolid desde Madrid?
   - Respuesta: Menos de 24 horas para valoración, operamos en la provincia
   
4. ¿Qué pasa con el hollín industrial pesado?
   - Respuesta: Técnica específica con HEPA + químicos en seco

**Municipios a linkear:**
- `/limpieza-de-incendios-tordesillas.html` (futura)
- `/limpieza-de-incendios-penafiel.html` (futura)
- `/limpieza-de-incendios-medina-del-campo.html` (futura)

---

### MURCIA (Tier 1) - Ejemplo

**Hero H1:**
```
Limpieza de incendios en Murcia: Huerta de ceniza
```

**Párrafo contexto:**
```
Murcia es tierra y agua, huerta ancestral donde la ciudad creció sin control. Viviendas antiguas en el casco histórico, urbanizaciones nuevas en las afueras, edificios de comercio en el centro. Los incendios aquí tienen ritmo lento pero destructivo: el calor del interior mantiene el humo vivo durante días, el polvo se enquista, los olores persisten. La limpieza en Murcia es cuestión de profesionales que entienda esa inercia térmica.
```

---

## 2.4 Checklist técnico de implementación

```markdown
### URLS y Estructura
[ ] URL pattern: /limpieza-de-incendios-[ciudad].html
[ ] Validar que 11 ciudades NO existen en lista_48 actual
    (Comprobar: limpieza-de-incendios-valladolid.html, limpieza-de-incendios-burgos.html, etc.)
[ ] Canonical URL única por ciudad
[ ] Redirecciones 301 desde variantes (ej: de limpieza-incendios-valladolid.html → limpieza-de-incendios-valladolid.html)

### Meta Tags (por landing)
[ ] Title: "[Ciudad]: Expertos limpieza post incendio - Técnica láser + ozono"
    Ejemplo: "Valladolid: Expertos limpieza post incendio - Técnica láser + ozono"
[ ] Meta description: "Limpieza incendios [Ciudad]. [Sector local]. Presupuesto sin compromiso. 24/7."
    Ejemplo: "Limpieza incendios Valladolid. Plantas, viviendas, comercios. Presupuesto gratis. 24/7."
[ ] og:title personalizado
[ ] og:description personalizado
[ ] og:image: reutilizar LimpiezadeGarajes.webp O generar específica por región
[ ] twitter:card summary_large_image
[ ] Canonical: https://limpiezaincendiosnanonexmadrid.com.es/limpieza-de-incendios-[ciudad].html

### JSON-LD / Schema.org
[ ] LocalBusiness schema:
    - name: "Nano Nex - Limpieza de Incendios en [Ciudad]"
    - addressLocality: "[Ciudad]"
    - areaServed: "[Ciudad] y alrededores"
    - telephone: "632107272"
    - email: "info@nanonex.es"
    
[ ] BreadcrumbList:
    - Inicio > Zonas > [Ciudad]
    
[ ] FAQPage schema con 4 preguntas:
    - 3 preguntas genéricas (reutilizar)
    - 1 pregunta ciudad-específica (personalizada)

### Contenido (por landing)
[ ] H1 personalizado (hero)
[ ] Párrafo contexto: 80-120 palabras con industria/clima/turismo local
[ ] Imagen: reutilizar LimpiezadeGarajes.webp (o generar nueva)
[ ] Sección "Por qué la limpieza es urgente en [Ciudad]" - adaptada
[ ] 6 pasos proceso estándar (NO cambiar, reutilizar de Málaga)
[ ] Tabla precios orientativos (adaptar si necesario por región, pero usar estándar)
[ ] FAQ: 4 preguntas (3 estándar + 1 ciudad)
[ ] Sección "Errores frecuentes" - adaptar contexto local
[ ] "Qué incluye/qué no" (reutilizar textual)
[ ] Sidebar: Links a 3 municipios vecinos (futuros landings)

### Links Internos
[ ] Links a municipios vecinos: /limpieza-de-incendios-[municipio].html
    (Marcar como "próximamente" si aún no existen)
[ ] Link a región principal (si existe): /limpieza-de-incendios-[provincia].html
[ ] Link a /ubicaciones.html (catálogo de ciudades)
[ ] Link a blog: /blog.html
[ ] Link a home: /index.html
[ ] SIN ENLACES ROTOS: validar con tools antes de commit

### Breadcrumb (estructura HTML)
[ ] <nav class="breadcrumb">
    Inicio > Zonas > [Ciudad]
    </nav>

### Testing
[ ] HTML válido (sin errores de sintaxis)
[ ] Responsive: mobile (320px), tablet (768px), desktop (1024px+)
[ ] Meta tags rendering OK (inspeccionar <head>)
[ ] Forms: campo "Origen" = "[Ciudad]" (cambiar de Málaga)
[ ] Velocidad: < 3s en 4G (lighthouse)
[ ] Accesibilidad: WCAG AA (contraste, alt text, keyboard nav)
[ ] Links: validar no 404 (incluir links internos futuros con disclaimer)

### Preparación de assets
[ ] Imagen por landing (si es específica): guardar en raíz
    Nombrado: LimpiezadeIncendios-[Ciudad].webp
    O reutilizar: LimpiezadeGarajes.webp
[ ] Validar peso imagen < 300KB (optimizar con tinypng.com o similar)

### Pre-publicación (antes de commit)
[ ] Crear archivo HTML limpio (copiar de template, no copy-paste del anterior)
[ ] Buscar y reemplazar: [CIUDAD] → Valladolid (verificar todas las instancias)
[ ] Validar que NO hay referencias a otras ciudades
[ ] Screenshot mobile + desktop (validación visual)
```

---

## 2.5 Timeline estimado (Gantt simplificado)

```
SEMANA 1 (Fase 3B.1) - TIER 1 Primera mitad
├─ Research + copy: Valladolid, Burgos (2 horas)
├─ Desarrollo: Valladolid (1.5h), Burgos (1.5h)
├─ Testing: Ambas (1h)
└─ Total: 6h

SEMANA 2 (Fase 3B.2) - TIER 1 Segunda mitad
├─ Research + copy: Toledo, Murcia, Jaén (2.5h)
├─ Desarrollo: Toledo (1.5h), Murcia (1.5h), Jaén (1.5h)
├─ Testing: Todas (1h)
└─ Total: 7.5h

SEMANA 3 (Fase 3B.3) - TIER 2 Primera mitad
├─ Research + copy: Huesca, Teruel, Salamanca (2h)
├─ Desarrollo: 3 landings (4.5h)
├─ QA general: Links internos, schema (1h)
└─ Total: 7.5h

SEMANA 4 (Fase 3B.4) - TIER 2 + TIER 3 + Integración
├─ Research + copy: Cuenca, Alicante, Castellón (2h)
├─ Desarrollo: 3 landings (4.5h)
├─ Actualizar /ubicaciones.html (1h)
├─ Actualizar sitemap.xml (0.5h)
├─ Testing final + validación (1.5h)
├─ Deploy (0.5h)
└─ Total: 10h

PROYECTO TOTAL: ~31 horas desarrollo
PARALLELIZABLE: Research + copy (independiente) + maquetación (independiente)

CRÍTICO PATH:
1. Research + copy (2-2.5h/ciudad) = máx 2.5h/semana
2. Desarrollo HTML (1.5h/ciudad) = máx 4.5h/semana
3. Testing + integración (último)
```

---

## 2.6 Estimación de impacto SEO

### Keywords por Tier

**TIER 1 (5 landings, ~380-510 búsquedas/mes):**
- Valladolid: "limpieza incendios valladolid", "hollín valladolid", "plantas alimentarias incendio"
- Burgos: "limpieza incendios burgos", "humo piedra antigua"
- Toledo: "limpieza incendios toledo", "turismo patrimonio"
- Murcia: "limpieza incendios murcia" (ya rankea, refuerzo)
- Jaén: "limpieza incendios jaén", "olivarera"

**TIER 2 (4 landings, ~80-160 búsquedas/mes):**
- Huesca, Teruel, Salamanca, Cuenca: 20-40 búsquedas/mes c/u

**TIER 3 (2 landings, ~110-170 búsquedas/mes):**
- Alicante: 80-120 búsquedas/mes
- Castellón: 30-50 búsquedas/mes

**VOLUMEN TOTAL NUEVO: ~570-840 búsquedas/mes potenciales**

### Posicionamiento esperado

```
Timeline de ranking:
- 2-3 semanas: Indexación inicial (Google crawl)
- 6-8 semanas: Posicionamiento inicial (posición 7-10 en SERP)
- 3-4 meses: Posicionamiento consolidado (top 3 con suerte)
- 6+ meses: Autoridad completa + municipios vecinos

CTR Promedio (si top 3): 20-30% de las búsquedas
Conversión esperada (form submission): 2-3% de clics

LEADS NUEVO/MES ESTIMADO:
- Tier 1: (450 búsquedas × 25% CTR × 2.5% conversión) = 2.8 leads/mes
- Tier 2: (120 búsquedas × 20% CTR × 2% conversión) = 0.5 leads/mes
- Tier 3: (140 búsquedas × 25% CTR × 2.5% conversión) = 0.9 leads/mes
- TOTAL: ~4.2 leads/mes (conservador; puede ser 5-7 con buena ejecución)

VALOR COMERCIAL:
- Lead = contacto potencial
- Conversión lead → cliente: 20-30% (según follow-up)
- Cliente promedio: 1.5-3K€ (según tipo servicio)
- Valor/mes esperado: 4-6 clientes × 2K€ = 8-12K€/mes (6+ meses post-launch)
- ROI: ~8-12K€ / 1K€ (coste desarrollo) = 8-12x
```

### Factores de éxito SEO

✅ **HACER:**
- Contexto local personalizado (copy original, no genérico)
- Schema.org correcto por ciudad (LocalBusiness + Breadcrumb + FAQ)
- Links internos ciudad-municipios (topical clustering)
- URLs semánticamente claras y consistentes
- Publicación secuencial (no spam de indexación)
- Interlinking back desde blog hacia nuevas landings

❌ **EVITAR:**
- Copy paste entre landings (penalización Panda)
- URLs ambiguas ("limpieza-incendios-madrid-madrid.html")
- Missing meta descriptions o títulos
- Imágenes sin optimizar / alt text vacío
- Links rotos (validar antes de commit)
- Canonicals incorrectos (evitar duplicate content)

---

# PARTE 3: PLAN DE IMPLEMENTACIÓN INTEGRADO

## 3.1 Timeline consolidado (Fases 3A + 3B)

```
SEMANA 1-2: Fase 3A (Limpieza Blog)
├─ Día 1-2: Análisis final + validación de posts
├─ Día 3-4: Crear página /limpieza-general.html
├─ Día 5: Generar lista de 100 redirects 301 para .htaccess
├─ Día 6: Actualizar blog.html con nuevas categorías
└─ Día 7: Test + validación en staging

SEMANA 2-3: Fase 3B - TIER 1 (5 landings)
├─ Semana 2: Valladolid, Burgos (4 horas dev)
├─ Semana 3 Inicio: Toledo, Murcia, Jaén (6 horas dev)
└─ Testing: 2-3 horas

SEMANA 4-5: Fase 3B - TIER 2 (4 landings)
├─ Semana 4: Huesca, Teruel, Salamanca (4.5 horas dev)
├─ Semana 5: Cuenca + TIER 3 (3 horas dev)
└─ QA general: 2 horas

SEMANA 6: Integración + Deploy
├─ Actualizar /ubicaciones.html
├─ Actualizar sitemap.xml
├─ Test de 301 redirects (Fase 3A)
├─ Google Search Console: submit sitemap
└─ Monitorización post-launch

TOTAL: 6 semanas
Parallelizable: Fases 3A y 3B pueden correr en paralelo (semana 1-2 ambas)
```

---

## 3.2 Recursos necesarios

| Recurso | Cantidad | Coste | Notas |
|---------|----------|-------|-------|
| **Copywriting especializado** | 11 horas | 500-750€ | Personalizacion por ciudad |
| **Desarrollo HTML/técnico** | 17 horas | 400-600€ | Templating + testing |
| **Research local** | 3 horas | 0€ | Wikipedia, fuentes públicas |
| **Imágenes** | 11 assets | 0€ | Reutilizar LimpiezadeGarajes.webp |
| **SEO + Schema.org** | 2 horas | 0€ | Template estándar |
| **Testing + QA** | 4 horas | 0€ | Manual |
| **TOTAL INTERNO** | ~37 horas | - | ~1-2 semanas tiempo dedicado |
| **TOTAL EXTERNAL (si outsource)** | - | 1.5-2K€ | Copy + desarrollo |

---

## 3.3 Checklist de implementación ordenada

### FASE 3A: Limpieza Blog (Días 1-7)

```markdown
### Pre-Implementación
[ ] Crear backup de blog.html
[ ] Crear backup de .htaccess
[ ] Validar que los 100 posts OFF-TOPIC están documentados con URLs exactas

### Desarrollo
[ ] Crear /limpieza-general.html (nueva página genérica)
    - Hero: "Servicios de limpieza profesional diversa"
    - Contenido: breve descripción (garajes, industrial, etc.)
    - CTA a post-incendio
    
[ ] Generar lista de 100 redirects 301 para .htaccess
    RedirectMatch 301 ^/blog/YYYY/MM/DD/slug/$ /limpieza-general.html
    
[ ] Actualizar blog.html:
    - Renombrar secciones por subcategoría
    - Cambiar "Limpieza (51)" → subcategorías más específicas
    - Agregar "(REDIRIGIDO)" a sección de limpieza genérica
    
[ ] Actualizar sitemap.xml:
    - Agregar /limpieza-general.html
    - Remover o marcar 100 posts como <changefreq>never</changefreq>

### Testing
[ ] Validar 301 redirects en local (/limpieza-general.html)
[ ] Validar que blog.html renderiza OK
[ ] Comprobar que no hay enlaces rotos internos
[ ] Screenshot antes/después de cambios

### Publicación
[ ] Upload .htaccess con los 100 redirects
[ ] Upload blog.html actualizado
[ ] Upload sitemap.xml actualizado
[ ] Upload /limpieza-general.html
[ ] Notificar en Google Search Console (submit sitemap)

### Post-Publicación
[ ] Monitorizar errores 4xx en GSC (primeras 24h)
[ ] Verificar que algunos redirects funcionen (test manualmente 5-10)
[ ] Revisar crawl stats en GSC (debería estabilizar)
```

---

### FASE 3B: Expansión Geográfica (Semanas 2-6)

#### SEMANA 1 (Tier 1 Parte 1)

```markdown
### Lunes-Martes: Research + Copy
[ ] Valladolid:
    - Research: población, industrias, contexto
    - Copy H1: "Limpieza de incendios en Valladolid: Cuando la industria se detiene"
    - Copy contexto: 120 palabras personalizadas
    - FAQ: 4 preguntas (1 específica)
    - Municipios: Tordesillas, Peñafiel, Medina del Campo
    
[ ] Burgos: (idem)

### Miércoles-Jueves: Desarrollo
[ ] Copiar limpieza-de-incendios-malaga.html → limpieza-de-incendios-valladolid.html
[ ] Buscar/Reemplazar:
    - "Málaga" → "Valladolid"
    - "Málaga" → "Valladolid"
    - Copy contexto estándar → Copy Valladolid personalizado
    - Links municipios → [Tordesillas, Peñafiel, Medina]
    - Origen en form: "Valladolid"
[ ] Validar HTML (no errores de sintaxis)
[ ] Idem para Burgos

### Viernes: Testing
[ ] Responsive design (mobile, tablet, desktop)
[ ] Meta tags visibles
[ ] Forms funcional (Origin = "Valladolid")
[ ] Links internos: no 404
[ ] Screenshot visual mobile + desktop

### Sábado: Publicación
[ ] Upload limpieza-de-incendios-valladolid.html
[ ] Upload limpieza-de-incendios-burgos.html
[ ] Actualizar /ubicaciones.html: agregar links a Valladolid y Burgos
[ ] Actualizar sitemap.xml (agregar 2 URLs)
```

#### SEMANA 2 (Tier 1 Parte 2 + QA)

```markdown
### Lunes-Miércoles: Research + Copy + Desarrollo
[ ] Toledo: Copy personalizado + HTML
[ ] Murcia: Copy personalizado + HTML (nota: puede que exista, validar primero)
[ ] Jaén: Copy personalizado + HTML

### Jueves-Viernes: Testing
[ ] Las 3 landings: responsive, meta, forms, links
[ ] Verificar que URLs en sitemap_anterior no rompieron

### Sábado: Publicación
[ ] Upload 3 landings (Toledo, Murcia, Jaén)
[ ] Actualizar /ubicaciones.html
[ ] Actualizar sitemap.xml (+3 URLs)
[ ] Google Search Console: submit sitemap
```

#### SEMANA 3 (Tier 2 Parte 1 + QA)

```markdown
### Lunes-Miércoles: Research + Copy + Desarrollo
[ ] Huesca: Copy + HTML
[ ] Teruel: Copy + HTML
[ ] Salamanca: Copy + HTML

### Jueves: Testing + QA general
[ ] Las 3 landings: testing completo
[ ] Validar que 8 landings anteriores no tuvieron regresión (links rotos, etc.)
[ ] Comprobar que sitemap.xml está correcto

### Viernes-Sábado: Publicación
[ ] Upload 3 landings
[ ] Actualizar /ubicaciones.html
[ ] Actualizar sitemap.xml
```

#### SEMANA 4 (Tier 2 Parte 2 + Tier 3 + Integración Final)

```markdown
### Lunes-Martes: Research + Copy + Desarrollo
[ ] Cuenca: Copy + HTML
[ ] Alicante: Copy + HTML (expandir Valencia)
[ ] Castellón: Copy + HTML (expandir Valencia)

### Miércoles: Testing
[ ] 3 landings: testing completo
[ ] Validación general de las 11 nuevas

### Jueves-Viernes: Integración
[ ] Actualizar /ubicaciones.html (versión final con las 11 nuevas)
    - Agrupar por región
    - Links coherentes
[ ] Actualizar sitemap.xml (versión final)
[ ] Validar no hay duplicate content
[ ] Comprobar que canonicals son correctos

### Sábado: Publicación Final
[ ] Upload 3 landings (Cuenca, Alicante, Castellón)
[ ] Upload /ubicaciones.html (versión final)
[ ] Upload sitemap.xml (versión final)
[ ] Google Search Console: submit sitemap
[ ] Google Search Console: request indexing para las 11 nuevas

### Post-Publicación (Semana 5+)
[ ] Monitorizar crawl errors (primeras 48h)
[ ] Revisar impressions en GSC (después de 1-2 semanas)
[ ] Revisar ranking inicial (posición 5-15 esperada)
[ ] Ajustar copy si hay bajo CTR
```

---

## 3.4 Archivo: Lista de 100 posts OFF-TOPIC (resumen)

```
LIMPIEZA DEL HOGAR (35 posts)
[1] blog/2024/11/27/como-limpiar-a-fondo-tu-ducha-en-solo-4-pasos/
[2] blog/2018/06/20/limpiar-un-inodoro-de-forma-profesional/
[3] blog/2024/12/25/las-5-claves-para-una-correcta-desinfeccion-de-las-mesas-del-comedor/
[4] blog/2018/06/19/como-limpiar-tu-cortina-de-ducha/
[5] blog/2024/10/08/como-eliminar-manchas-y-huellas-en-pantallas-de-tv/
... [30 más]

LIMPIEZA INDUSTRIAL GENÉRICA (30 posts)
[36] blog/2024/09/26/limpieza-industrial-los-retos-mas-comunes-y-como-superarlos/
[37] blog/2024/10/16/7-formas-de-desinfectar-oficinas-despues-de-una-limpieza-de-acumulacion/
[38] blog/2024/09/19/limpieza-oficinas-2/
... [27 más]

SÍNDROME DE DIÓGENES / ACUMULACIÓN (28 posts)
[67] blog/2022/12/28/limpieza-de-incendios-10-consejos/ [NOTA: este puede ser recuperable]
... [27 más]

OTROS (7 posts)
... [7 posts varios]

TOTAL: 100 posts para redirect a /limpieza-general.html
```

---

## 3.5 Validación pre-deploy

### Checklist final

```markdown
### Fase 3A Validación
[ ] /limpieza-general.html: accesible y sin 404
[ ] .htaccess: 100 redirects 301 válidos (test 10 URLs aleatorias)
[ ] blog.html: renderiza OK, no enlaces rotos
[ ] sitemap.xml: syntax correcto, sin duplicados
[ ] robots.txt: permite acceso a /limpieza-general.html

### Fase 3B Validación (11 landings)
[ ] Todas las 11 URLs son accesibles
[ ] No hay duplicate content (comprobar meta canonicals)
[ ] Meta descriptions todas personalizadas (no idénticas)
[ ] O:image válida (ruta correcta, imagen existe)
[ ] Schema.org válido (usar schema.org/validator)
[ ] Forms funcional (test envío en staging)
[ ] Links internos: validar que municipios vecinos no rompan (marcar futuros con disclaimer)
[ ] Responsive: mobile, tablet, desktop
[ ] Speed: < 3s en 4G (lighthouse)

### Integración General
[ ] /ubicaciones.html: todas las 11 nuevas tienen link
[ ] sitemap.xml: contiene las 11 nuevas URL
[ ] No hay cannibalization: comprobar que keywords no compiten
[ ] Interlinking: nuevo contenido linkea a blog donde relevante

### SEO Pre-Launch
[ ] Google Search Console: verificar propiedad del sitio
[ ] Bing Webmaster Tools: idem
[ ] robots.txt: permite robots
[ ] sitemap.xml: bien formado, submittable
```

---

## 3.6 Monitorización post-launch

### KPIs a trackear (Semanas 1-8)

```markdown
### Google Search Console
[ ] Impressions por ciudad (esperado: ramp-up gradual)
[ ] Click-through rate (CTR) - target: > 15% si en top 5
[ ] Average position (esperado: 7-15 inicialmente, mejora a 3-5 en 8 semanas)
[ ] Crawl stats (debería normalizarse)
[ ] Indexation: validar que 11 nuevas se indexan (no en "Excluded")

### Google Analytics 4
[ ] Users nuevos por landing (track por ciudad)
[ ] Time on page (target: > 2 minutos)
[ ] Conversion rate (formulario) - target: 2-4%
[ ] Bounce rate (target: < 50%)

### Conversiones
[ ] Form submissions por ciudad
[ ] Lead quality (validar que leads son reales, geografía correcta)
[ ] Sales closed (seguimiento manual si posible)

### Acción correctiva si underperformance
- Bajo CTR: revisar meta description / title tag, reescribir si necesario
- Bajo ranking: revisar interlinking, agregar blog posts relacionadas, mejorar copy
- Bajo conversion: revisar form, CTA visibility, copy persuasión
```

---

# ENTREGA FINAL

## 4.1 Archivos generados

Disponibles para implementación:

1. **PLAN_CRITICO_3A_3B.md** (este archivo)
   - Análisis blog + posts a redirigir
   - Plan expansión geográfica (11 landings)
   - Timeline + checklist implementación

2. **Plantilla estándar para nuevo landing:**
   - Basado en `/limpieza-de-incendios-malaga.html`
   - Parámetros a personalizar por ciudad (H1, contexto, municipios, etc.)

3. **Copy templates (2 ciudades ejemplo):**
   - Valladolid (Tier 1)
   - Murcia (Tier 1)

4. **Checklist técnico detallado:**
   - URLs, meta tags, schema.org, links, testing

5. **Timeline Gantt (6 semanas):**
   - Fases 3A + 3B integradas
   - Hitos críticos
   - Paralelización

---

## 4.2 Resumen ejecutivo de impacto

| Métrica | Fase 3A | Fase 3B | Total |
|---------|---------|---------|--------|
| **Posts relevantes** | 101/201 (50%) | — | 101/201 (50%) |
| **Landings nuevas** | — | 11 ciudades | 11 |
| **Keywords nuevas** | — | 570-840/mes | 570-840/mes |
| **Horas trabajo** | 7-10h | 30-35h | 37-45h |
| **Leads nuevos/mes** | +1-2 | +3-5 | +4-7 |
| **Valor/mes estimado** | +2-4K€ | +6-15K€ | +8-19K€ |
| **Timeline** | 2 semanas | 4 semanas | 6 semanas |

---

## 4.3 Siguientes pasos

1. **Aprobación de este plan** ✓ Entregado
2. **Semana 1:** Ejecutar Fase 3A (blog cleanup)
3. **Semana 2-4:** Ejecutar Fase 3B Tier 1 (5 landings principales)
4. **Semana 5-6:** Ejecutar Fase 3B Tier 2+3 (6 landings complementarias)
5. **Semana 7+:** Monitorizar posicionamiento + optimizaciones
6. **Mes 3+:** Evaluar ROI, decidir expansión a municipios vecinos (fase futura)

---

**Documento generado:** 2026-06-14  
**Versión:** 1.0  
**Estado:** Listo para implementación
