# PLAN CRÍTICO 3A + 3B: Limpieza Blog + Expansión Geográfica
**Fecha creación:** 2026-06-14  
**Responsable:** Aitor Mentara Ramírez  
**Estado:** PENDIENTE IMPLEMENTACIÓN  
**Duración estimada:** 4-6 semanas

---

## PARTE 1: CRÍTICO 3A - LIMPIEZA Y REESTRUCTURACIÓN DEL BLOG

### 1.1 ANÁLISIS ACTUAL

#### Situación inicial:
- **Blog en:** `/home/user/limpieza_incendios_nanonex_es/blog.html`
- **Posts totales:** 209 artículos (2017-2025)
- **Duración:** 8 años de contenido acumulado
- **Problema:** ~40-50% de contenido OFF-TOPIC (no relacionado con incendios/hollín)

#### Distribución de categorías:

| Categoría | Cantidad | % | Estatus |
|-----------|----------|---|---------|
| Limpieza (general) | 51 | 24% | MIXTO - Purgar OFF-TOPIC |
| Limpieza de Incendios | 46 | 22% | ON-TOPIC ✓ |
| Limpieza Post-Incendios | 37 | 18% | ON-TOPIC ✓ |
| Prevención de Incendios | 34 | 16% | ON-TOPIC ✓ |
| Empresas de Limpieza | 24 | 11% | MIXTO - Revisar |
| Limpiezas con láser | 20 | 10% | TÉCNICAS (si contexto incendios) |
| Síndrome de Diógenes | 16 | 8% | OFF-TOPIC ✗ |
| Limpiezas Traumáticas | 13 | 6% | REVISAR (potencial ON-TOPIC) |
| Categoría: Limpieza | 10 | 5% | OFF-TOPIC (duplicado) |
| Limpieza Diógenes | 9 | 4% | OFF-TOPIC (duplicado) ✗ |
| Limpieza incendios restaurantes | 3 | 1% | ON-TOPIC ✓ |
| Limpieza con Ozono | 3 | 1% | TÉCNICAS ✓ |
| Ozono | 2 | 1% | TÉCNICAS ✓ |
| Limpieza criogénica | 2 | 1% | OFF-TOPIC ✗ |
| Categoría: Empresas | 1 | <1% | MIXTO |
| Limpieza de Obra | 1 | <1% | OFF-TOPIC ✗ |

#### Clústeres identificados:

**CLÚSTER 1: POST-INCENDIOS (Mantener - 117 posts)**
- Limpieza de Incendios (46)
- Limpieza Post-Incendios (37)
- Prevención de Incendios (34)
- Limpieza incendios restaurantes (3)
- Subtotal: **120 posts core**

**CLÚSTER 2: TÉCNICAS VÁLIDAS (Mantener si contexto incendios - 25 posts)**
- Limpiezas con láser (20)
- Limpieza con Ozono (3)
- Ozono (2)
- Riesgo: Algunos posts de láser pueden ser sobre arte/conservación (OFF-TOPIC)

**CLÚSTER 3: LIMPIEZAS TRAUMÁTICAS (Revisar - 13 posts)**
- Pueden incluir casos de incendios complejos
- Decisión: **Revisar contenido antes de eliminar**

**CLÚSTER 4: EMPRESAS DE LIMPIEZA (Mixto - 24 posts)**
- Algunos son generales (inodoro, ducha, cortina = OFF-TOPIC)
- Algunos son profesionales industriales (ON-TOPIC)
- Decisión: **Revisar y segmentar**

**CLÚSTER 5: OFF-TOPIC CLARO (Eliminar/Redirigir - 45+ posts)**
- Síndrome Diógenes: 25 posts (16 + 9)
- Ducha: 1 post
- Inodoro: 1 post
- Cortina ducha: 1 post
- Mesas comedor: 1 post
- Teclados: 1 post
- Pantallas TV: 1 post
- Suelos: 1 post
- Moscas: 1 post
- Espejos: 1 post
- Alfombras: 1 post
- Tiendas ropa: 1 post
- Criogénica: 2 posts
- Obra: 1 post
- Generales de limpieza: 5 posts
- Subtotal: **45+ posts OFF-TOPIC**

### 1.2 ESTRATEGIA DE LIMPIENZA RECOMENDADA

#### OPCIÓN ELEGIDA: **Opción B - Redirigir con 301**

**Razones:**
1. Preserva autoridad SEO histórica (backlinks mantienen valor)
2. No rompe indexed URLs (mantiene Google Search Console)
3. Implementación fácil con .htaccess
4. Permite reclasificación futura
5. Mejor que eliminar (Opción A) o dividir en subdominio (Opción C)

**Flujo:**
```
POST OFF-TOPIC → 301 → /servicios-limpieza.html (nueva landing)
                    └─> Contiene enlaces a servicios generales
                        + CTA a servicios incendios
```

#### FASE 1: Identificación y Documentación (1 semana)

**Tareas:**
1. [ ] Crear lista completa de 45+ posts OFF-TOPIC con URLs exactas
2. [ ] Crear mapping `URL_origen → URL_destino` para 301s
3. [ ] Revisar "Limpiezas Traumáticas" (13 posts) - ¿hay contexto incendios?
4. [ ] Revisar "Empresas de Limpieza" (24 posts) - segmentar ON/OFF
5. [ ] Revisar posts de LÁSER (20) - contar cuántos son realmente post-incendios
6. [ ] Generar CSV: `URL_vieja | Categoría_antigua | Decisión | URL_nueva`
7. [ ] Obtener backlinks de Google Search Console para posts a redirigir

**Deliverable:**
- Archivo: `BLOG_CLEANUP_MAPPING.csv` con todas las redirecciones
- Archivo: `URLS_A_REVISAR.txt` con posts ambiguos
- Confirmación: Decisión final sobre 13 posts traumáticos

#### FASE 2: Creación de Infraestructura (3-5 días)

**Tareas:**
1. [ ] Crear landing page: `/servicios-limpieza.html`
   - Título: "Servicios Profesionales de Limpieza General"
   - Contenido: Breve introducción a servicios (sin incendios)
   - CTA: "¿Limpieza post-incendio? Haz clic aquí" → link a `/index.html`
   - Meta tags: No competir con incendios

2. [ ] Crear: `/blog-limpieza-general.html` (alternativa más SEO-friendly)
   - Redirigir posts de limpieza general allá
   - Mantener categoría en blog nuevo

3. [ ] Preparar .htaccess con 301 redirects
   - Formato: `Redirect 301 /blog/2024/11/27/como-limpiar-a-fondo-tu-ducha-en-solo-4-pasos/ https://domain.es/servicios-limpieza.html`

**Deliverable:**
- Archivos HTML listos
- .htaccess actualizado (sin aplicar aún)

#### FASE 3: Reestructuración de blog.html (1 semana)

**Tareas:**
1. [ ] Backup actual: `blog.html.backup`
2. [ ] Remover secciones OFF-TOPIC:
   - Eliminar categoría "Síndrome Diógenes" (25 posts)
   - Eliminar duplicados "Categoría: Limpieza" (10 posts)
   - Eliminar duplicados "Limpieza Diógenes" (9 posts)
   - Limpiar posts individuales OFF-TOPIC de secciones mixtas

3. [ ] Reorganizar categorías:
   - **POST-INCENDIOS** (120 posts)
     - Limpieza de Incendios
     - Limpieza Post-Incendios
     - Prevención de Incendios
     - Limpieza incendios restaurantes
   - **TÉCNICAS AVANZADAS** (25 posts)
     - Limpiezas con láser (validadas)
     - Limpieza con Ozono
   - **CASOS ESPECIALES** (13 posts)
     - Limpiezas Traumáticas

4. [ ] Validar: No quedar con posts duplicados bajo múltiples categorías

5. [ ] Agregar meta description:
   - `"Blog especializado en limpieza post-incendio, técnicas de deshollinado, eliminación de humo y recuperación de espacios tras incendios. Expertos Nano Nex."`

**Deliverable:**
- blog.html actualizado y validado
- Conteo final: 158 posts ON-TOPIC
- Estructura categorías limpia

#### FASE 4: Implementación de Redirects (2-3 días)

**Tareas:**
1. [ ] Subir .htaccess con 301s a servidor
2. [ ] Crear nueva página `/servicios-limpieza.html`
3. [ ] Verificar 301s funcionan (usar redirectchecker.com)
4. [ ] Registrar cambios en Google Search Console:
   - Reportar eliminación de 45 URLs
   - Reportar cambio de dirección en masa si es posible

5. [ ] Monitorear:
   - Google Analytics para traffic redirigido
   - Errores 404 en primeros 7 días
   - Cambios de ranking para términos incendios

**Deliverable:**
- 301s implementados y verificados
- Reporte inicial de redirects en Google SC

#### FASE 5: Optimización Post-Limpieza (1 semana)

**Tareas:**
1. [ ] Audit de URLs internas que linkeaban a posts eliminados
   - Buscar: `blog/2024/11/27/` en archivos HTML
   - Reemplazar por nuevas URLs ON-TOPIC

2. [ ] Verificar sitemap.xml:
   - Remover URLs redirigidas
   - Actualizar `sitemap.xml` con 158 URLs finales

3. [ ] Crear contenido "bridge" si es necesario:
   - 1-2 artículos que mencionen "limpiezas generales" como adyacentes
   - Ejemplo: "Limpieza residencial vs post-incendio"

4. [ ] Monitorear performance:
   - Día 1-7: Búsqueda de errores
   - Día 8-30: Cambios de ranking
   - Día 30+: Tráfico consolidado

**Deliverable:**
- Reporte inicial de impacto
- URLs internas corregidas
- Sitemap actualizado

---

## PARTE 2: CRÍTICO 3B - EXPANSIÓN GEOGRÁFICA

### 2.1 ANÁLISIS DE COBERTURA ACTUAL

#### Landings existentes por región:

**MADRID (19 landings) ✓ COMPLETA**
- madrid.html (región)
- madrid-carabanchel.html
- madrid-chamberi.html
- madrid-hortaleza.html
- madrid-retiro.html
- madrid-salamanca.html
- madrid-tetuan.html
- madrid-vallecas.html
- Municipios: Alcalá (2), Alcobendas, Alcorcón, Fuenlabrada, Getafe, Leganés, Móstoles, Torrejón, Tres Cantos, San Sebastián, Colmenar

**BARCELONA (6 landings) ✓ COMPLETA**
- barcelona.html (región)
- barcelona-eixample.html
- barcelona-gracia.html
- barcelona-horta.html
- barcelona-montjuic.html
- barcelona-sarria.html

**VALENCIA (4 landings) ⚠️ PARCIAL**
- valencia.html
- valencia-campanar.html
- valencia-centro.html
- valencia-rascanya.html

**OTRAS CIUDADES (aisladas)**
- Bilbao (1)
- Malaga (1)
- Sevilla (1)
- Granada (1)
- Córdoba (1)
- Zaragoza (1)
- Palma (1)
- Alicante (1)
- Murcia (1)

#### PROBLEMA IDENTIFICADO:
- Solo 3 comunidades autónomas con cobertura mínima
- Falta estrategia de crecimiento geográfico
- Municipios principales sin landing

### 2.2 ESTRATEGIA DE EXPANSIÓN

#### OBJETIVO:
Crear 8 comunidades autónomas con cobertura ciudad + municipios principales
- **Meta:** 40-50 landings nuevas
- **Timeline:** 3-4 semanas
- **Esfuerzo:** 2-3 horas/landing

#### COMUNIDADES PRIORIZADAS:

##### TIER 1 - ALTO VALOR (5 landings nuevas)

**1. CASTILLA Y LEÓN**
- Principal: **Valladolid** (~ 300k habitantes)
- Secundarios: Burgos, León, Salamanca
- Estimado de búsquedas anuales: 8-12k
- Landing: `limpieza-de-incendios-valladolid.html`

**2. CASTILLA-LA MANCHA**
- Principal: **Toledo** (~ 85k, pero capital histórica)
- Secundarios: Cuenca, Ciudad Real, Albacete
- Alternativa: Guadalajara (225k)
- Estimado de búsquedas: 5-8k
- Landing: `limpieza-de-incendios-toledo.html`

**3. REGIÓN DE MURCIA**
- Principal: **Murcia** (capital región, 440k)
- Secundario: Cartagena (215k)
- Estimado de búsquedas: 8-12k
- Landing: `limpieza-de-incendios-murcia.html`

**4. ANDALUCÍA - EXTENSIÓN**
- Principal: **Jaén** (capital provincia, 115k)
- Ya existen: Sevilla, Málaga, Córdoba, Granada
- Estimado: 4-6k búsquedas
- Landing: `limpieza-de-incendios-jaen.html`

**5. ARAGÓN - EXTENSIÓN**
- Secundarios: **Huesca**, **Teruel**
- Ya existe: Zaragoza
- Estimado: 3-5k búsquedas
- Landings: `limpieza-de-incendios-huesca.html` + Teruel

##### TIER 2 - VALOR MEDIO (4 landings nuevas)

**6. CASTILLA Y LEÓN - EXTENSIÓN**
- **Salamanca** (160k) - turismo + estudiantes
- Landing: `limpieza-de-incendios-salamanca.html`

**7. CASTILLA-LA MANCHA - EXTENSIÓN**
- **Cuenca** (50k, turismo)
- Landing: `limpieza-de-incendios-cuenca.html`

**8. ANDALUCÍA - EXPANSIÓN COMPLETA**
- **Almería** - costa, turismo
- **Huelva** - frontera Portugal
- **Cádiz** - turismo

**9. VALENCIA - COMPLETAR**
- Ya existe: Valencia, Alicante (parcial)
- Agregar: **Castellón** (180k)
- Landing: `limpieza-de-incendios-castellon.html`

#### RESUMEN CUANTITATIVO:

| Región | Estatus | Landings nuevas | Municipios |
|--------|---------|-----------------|-----------|
| Madrid | ✓ Completa | 0 | 19 |
| Barcelona | ✓ Completa | 0 | 6 |
| Valencia | ⚠️ Ampliar | +1 (Castellón) | 4→5 |
| Castilla y León | ✗ Nueva | +3-4 | Valladolid, Burgos, León, Salamanca |
| Castilla-La Mancha | ✗ Nueva | +2-3 | Toledo, Cuenca, Ciudad Real |
| Murcia | ✗ Nueva | +1 | Murcia (+ Cartagena opcional) |
| Andalucía | ⚠️ Ampliar | +1-2 | Jaén (+ Almería, Huelva, Cádiz) |
| Aragón | ⚠️ Ampliar | +2 | Huesca, Teruel |
| **TOTAL** | | **11-13 nuevas** | **45-50 landings total** |

### 2.3 PLANTILLA ESTÁNDAR PARA LANDINGS

Usar template basado en landings existentes (Alcalá de Henares, Getafe, Madrid):

```html
<!-- ESTRUCTURA BÁSICA LANDING -->
<h1>Limpieza de Incendios en [Ciudad], [Provincia]</h1>
<meta name="description" content="Servicio profesional de limpieza post-incendio en [Ciudad]. Eliminación de hollín, humo y desodorización. Nano Nex disponible 24/7.">

<!-- SECCIONES RECOMENDADAS -->
1. Hero + Descripción local (100 palabras)
2. Servicios específicos (hollín, humo, humedades)
3. Zona de cobertura (barrios principales)
4. Galería antes/después
5. Datos de contacto local + teléfono
6. CTA a presupuesto
7. Testimonios
8. FAQ local
9. Interlinking a otras ciudades/blog
10. Schema markup (LocalBusiness + ServiceArea)
```

#### Variaciones por ciudad:

| Tamaño | Contenido | Ejemplos |
|--------|-----------|----------|
| **+300k hab.** | Completo: 5-6 barrios + datos únicos | Valladolid, Burgos |
| **100-300k** | Estándar: 3-4 barrios + referencias | Toledo, Salamanca, Murcia |
| **50-100k** | Compacto: 2-3 zonas principales | Cuenca, Huesca, Teruel |

### 2.4 PLAN DE IMPLEMENTACIÓN - EXPANSIÓN GEOGRÁFICA

#### FASE 1: Preparación (3-5 días)

**Tareas:**
1. [ ] Auditar landings existentes (Madrid + Barcelona) para template
   - Identificar elementos SEO comunes
   - Copiar estructura HTML
   - Documentar palabras clave por ciudad

2. [ ] Recopilar datos locales:
   - Población, barrios principales
   - Códigos postales
   - Referencias locales (referencias, noticias)
   - Competencia local

3. [ ] Crear documento: `CIUDADES_CONFIG.json` (ya existe, actualizar)
   ```json
   {
     "valladolid": {
       "provincia": "Valladolid",
       "comunidad": "Castilla y León",
       "poblacion": "301000",
       "barrios": ["Centro", "Parquesol", "Pilarica", "Delicias"],
       "kw_primaria": "limpieza incendios valladolid",
       "vol_mensual": 720,
       "url": "limpieza-de-incendios-valladolid.html"
     }
   }
   ```

4. [ ] Generar estructura de interlinking
   - Madrid → Valencia → Murcia → ... → Valladolid
   - Crear mapa: qué ciudades linkan a cuáles

5. [ ] Preparar imágenes:
   - Reutilizar "antes/después" del portfolio existente
   - Generar 1 imagen local si es posible (o usar genéricas)

**Deliverable:**
- CIUDADES_CONFIG.json actualizado con 11-13 ciudades nuevas
- Template HTML final
- Documento de interlinking
- 11-13 pares de imágenes listos

#### FASE 2: Redacción de contenido (2-3 semanas)

**Tareas:**
1. [ ] Redactar 11-13 landings nuevas
   - 1-2 horas/landing (usando template)
   - Personalizaciones:
     - Nombre ciudad + provincia
     - Barrios locales
     - Datos de población
     - Referencias locales
     - Schema markup con LocalBusiness

2. [ ] Revisar calidad:
   - Únicos, no copy-paste excesivo
   - SEO keywords naturales
   - Enlaces internos coherentes
   - Meta descriptions únicos

3. [ ] Crear FAQ local para cada ciudad:
   - 3-5 preguntas específicas por región
   - Ejemplo: "¿Qué barrios de Valladolid cubre Nano Nex?"

4. [ ] Interlinking:
   - Agregar a landings Madrid/Barcelona referencias a nuevas ciudades
   - Crear índice: `/ciudades.html` o `/zonas.html` (si no existe)

**Deliverable:**
- 11-13 archivos .html listos
- Archivos SEO-optimizados (meta tags, keywords)
- Interlinking configuration document

#### FASE 3: Implementación técnica (1 semana)

**Tareas:**
1. [ ] Upload de archivos HTML al servidor
   ```
   /limpieza-de-incendios-valladolid.html
   /limpieza-de-incendios-burgos.html
   /limpieza-de-incendios-toledo.html
   /limpieza-de-incendios-murcia.html
   /limpieza-de-incendios-huesca.html
   /limpieza-de-incendios-teruel.html
   /limpieza-de-incendios-salamanca.html
   /limpieza-de-incendios-cuenca.html
   /limpieza-de-incendios-jaen.html
   /limpieza-de-incendios-castellon.html
   + 1-3 adicionales según decisión
   ```

2. [ ] Actualizar sitemap.xml
   - Agregar URLs nuevas
   - Versionar: `sitemap_v2.xml`

3. [ ] Actualizar ubicaciones.html (si existe)
   - Agregar links a nuevas ciudades
   - Mantener jerarquía: España → Región → Ciudad

4. [ ] Actualizar index.html
   - Agregar sección "Nuevas ciudades"
   - Crear grid/lista de ciudades con links

5. [ ] Crear redirects (si URLs cambian):
   - No necesario si son nuevas, pero agregar si migran

6. [ ] Validar:
   - Todos los HTML validan (W3C)
   - No hay broken links
   - Schema markup valida (schema.org)
   - Mobile responsive

**Deliverable:**
- Archivos en servidor
- sitemap.xml actualizado
- Validaciones completas

#### FASE 4: SEO + Google Search Console (3-5 días)

**Tareas:**
1. [ ] Agregar URLs a Google Search Console
   - Forzar crawl si es posible
   - Monitorear descubrimiento en primeros 7 días

2. [ ] Crear "discovery page" si es necesario:
   - `/nuevas-ciudades-2026.html`
   - Listar 11-13 ciudades nuevas
   - CTA a servicios

3. [ ] Preparar Google Business Profile para ciudades grandes
   - Valladolid, Burgos, Toledo, Murcia

4. [ ] Agregue ciudades a robots.txt si hay exclusiones

5. [ ] Monitorear:
   - Indexación (esperar 1-2 semanas)
   - Primeros clicks/impresiones
   - Posición media

**Deliverable:**
- Reporte de indexación
- Posicionamiento inicial (baseline)
- Plan de link building si es necesario

#### FASE 5: Validación de resultados (1-2 semanas)

**Tareas:**
1. [ ] Medir tráfico inicial
   - Esperar ~7 días para datos
   - Comparar conversiones incendios vs tráfico

2. [ ] Ajustar contenido si no rankea
   - Mejorar estructura de encabezados
   - Agregar más palabras clave long-tail
   - Aumentar interlinking

3. [ ] Crear backlinks si es necesario
   - Directorios locales (Yellow Pages España, etc.)
   - Citas de negocio local
   - Guest posts en blogs locales

4. [ ] Documentar lecciones aprendidas
   - Qué ciudades rankean rápido
   - Qué palabras clave funcionan mejor
   - Patrones de conversión

**Deliverable:**
- Reporte de performance
- Backlink plan
- Documento de lecciones aprendidas

---

## 3. TIMELINE CONSOLIDADO

### SEMANA 1-2: FASE 3A (Blog Cleanup)
- **Lunes 1:** Identificación y documentación posts OFF-TOPIC
- **Viernes 1:** Mapping completado
- **Lunes 2:** .htaccess y landings creadas
- **Viernes 2:** blog.html reestructurado

### SEMANA 3: TRANSICIÓN
- **Lunes 3:** Implementar 301 redirects
- **Martes-Viernes 3:** Testing y optimizaciones

### SEMANA 3-4: FASE 3B (Geografía) COMIENZA EN PARALELO
- **Día 1:** Preparación y recopilación de datos
- **Día 2-5:** Primeras 3-4 landings redactadas

### SEMANA 5-6: EXPANSIÓN CONTINÚA
- **Día 1-10:** Redacción de 11-13 landings
- **Día 11-14:** Upload y validación técnica

### SEMANA 7: FINALIZACIÓN
- **Día 1-3:** Google SC + SEO
- **Día 4-7:** Monitoreo inicial

**Total:** 6-7 semanas (4-6 si trabajo paralelo es efectivo)

---

## 4. EQUIPO Y RESPONSABILIDADES

| Tarea | Owner | Duración |
|-------|-------|----------|
| Identificación posts OFF-TOPIC | Aitor | 2-3 días |
| Redacción landing pages | Aitor | 2-3 sem |
| Validación SEO | Aitor | 3-5 días |
| Upload/implementación técnica | DevOps/Aitor | 3-5 días |
| Google SC + monitoreo | Aitor | Continuo |
| Revisión de Limpiezas Traumáticas | Aitor (manual) | 1 día |

---

## 5. MÉTRICAS DE ÉXITO

### PARTE 1 (Blog Cleanup):
- ✓ 45+ posts redirigidos correctamente (0 errores 404)
- ✓ No pérdida de ranking en términos principales incendios
- ✓ Blog con 158 posts ON-TOPIC
- ✓ Estructura categorías clara

### PARTE 2 (Expansión):
- ✓ 11-13 landings nuevas creadas
- ✓ Todas indexadas en Google en 14 días
- ✓ Primeras posiciones (top 10) en ciudades para "limpieza incendios [ciudad]"
- ✓ +2-3 leads/mes desde nuevas ciudades

---

## 6. RIESGOS Y MITIGACIÓN

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|--------|-----------|
| Pérdida de ranking (incendios) post-limpieza | Media | Alto | 301s bien configurados, no eliminar |
| Posts con contexto ambiguo | Alta | Bajo | Revisar caso a caso, errar del lado de mantener |
| Google penalizar redirects masivos | Baja | Alto | Máx 50 URLs, redirigir a página temática, no al home |
| Landings nuevas no rankean | Media | Medio | Backlinks, interlinking fuerte, mejor contenido |
| Duplicate content (entre ciudades) | Alta | Medio | Usar variables de ciudad, no copiar exacto |

---

## 7. DOCUMENTACIÓN REQUERIDA

### Archivos a crear:
1. `BLOG_CLEANUP_MAPPING.csv` - Todas las redirecciones 301
2. `URLS_A_REVISAR.txt` - Posts ambiguos
3. `.htaccess.new` - Configuración redirects (sin aplicar hasta validación)
4. `CIUDADES_CONFIG.json` - Configuración expandida
5. `INTERLINKING_MAP.txt` - Mapa de enlaces entre ciudades
6. `TEMPLATE_LANDING.html` - Template estándar para ciudades

### Archivos a actualizar:
1. `blog.html` - Removidos posts OFF-TOPIC
2. `sitemap.xml` - Agregadas 11-13 URLs nuevas
3. `ubicaciones.html` - Agregadas nuevas ciudades
4. `index.html` - Referencias a nuevas ciudades
5. `.htaccess` - Redirecciones 301

---

## 8. PRÓXIMOS PASOS

1. **APROBACIÓN:** Revisar este plan con stakeholder
2. **START:** Lunes próximo comienza Fase 3A
3. **CHECKPOINT:** Día 7 - blog.html reestructurado
4. **GO-LIVE:** Semana 2 - Implementar 301s
5. **EXPANSION-START:** Semana 3 - Comienza Fase 3B en paralelo
6. **COMPLETION:** Semana 6-7 - Todas las ciudades online

---

**Nota importante:** Este plan es flexible. Si necesita ajustes en prioridades (ej: enfocarse SOLO en blog primero), indicar y se adapta el timeline.

**Última actualización:** 2026-06-14  
**Próxima revisión recomendada:** Después de Fase 1 completa (día 7)
