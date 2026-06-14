# ÍNDICE: PLAN CRÍTICO 3A + 3B
**Nano Nex Madrid - Limpieza Post Incendio**

## 📋 Documentación generada (2026-06-14)

Este plan aborda dos críticos simultáneamente:
- **3A:** Limpiar blog (50% OFF-TOPIC) → 301 redirects
- **3B:** Expandir a 11 nuevas ciudades → 570-840 búsquedas/mes

**Impacto estimado:** +4-7 clientes nuevos/mes + mejora 2-3x en autoridad temática

---

## 📄 ARCHIVOS DEL PLAN

### 1. RESUMEN_EJECUTIVO_FINAL.md ⭐ **COMIENZA AQUÍ**
**Descripción:** Documento ejecutivo de 1-2 páginas  
**Contenido:**
- Resumen de hallazgos (blog + expansión)
- Timelines integrados
- Recursos necesarios
- Impacto proyectado
- Checklist de implementación

**Audiencia:** Directivos, stakeholders  
**Tiempo de lectura:** 5-10 min

---

### 2. PLAN_CRITICO_3A_3B.md ⭐ **DOCUMENTO COMPLETO**
**Descripción:** Plan detallado de 40+ páginas  
**Contenido:**

**PARTE 1: ANÁLISIS DE BLOG (3A)**
- 1.1 Resumen de hallazgos (201 posts, 50% OFF-TOPIC)
- 1.2 Clúster 1: Post-Incendio (81 posts - MANTENER)
- 1.3 Clúster 5: Técnicas Especiales (20 posts - MANTENER)
- 1.4 Clúster 3: Limpieza General (100 posts - ELIMINAR)
- 1.5 Recomendación: Opción B (Redirects 301)
- 1.6 Reestructura del Blog
- 1.7 Impacto estimado

**PARTE 2: EXPANSIÓN GEOGRÁFICA (3B)**
- 2.1 Análisis de cobertura actual (48 landings)
- 2.2 Plan de 11 landings nuevas (Tier 1-3)
- 2.3 Copy templates personalizados (Valladolid, Murcia ejemplos)
- 2.4 Checklist técnico de implementación
- 2.5 Timeline estimado (Gantt simplificado)
- 2.6 Estimación de impacto SEO
- 2.7 Mapeo de ciudades + municipios vecinos

**PARTE 3: PLAN DE IMPLEMENTACIÓN**
- 3.1 Timeline consolidado (Fases 3A + 3B)
- 3.2 Recursos necesarios
- 3.3 Checklist ordenada (semana por semana)
- 3.4 Archivo: Lista de 100 posts OFF-TOPIC
- 3.5 Validación pre-deploy
- 3.6 Monitorización post-launch

**PART 4: ENTREGA FINAL**
- 4.1 Archivos generados
- 4.2 Resumen ejecutivo
- 4.3 Siguientes pasos

**Audiencia:** Project managers, developers, copywriters  
**Tiempo de lectura:** 30-45 min

---

### 3. OFF_TOPIC_POSTS_REDIRECT_LIST.txt
**Descripción:** Lista completa de 100 posts OFF-TOPIC  
**Contenido:**
- **Categoría 1:** Limpieza del hogar (35 posts)
  - Ducha, inodoro, mesas, cortinas, TV, espejos, ventanas, suelos, etc.
  
- **Categoría 2:** Limpieza industrial/comercial genérica (30 posts)
  - Oficinas, garajes, hospitales, fábricas, tiendas, etc.
  
- **Categoría 3:** Síndrome de Diógenes / Acumulación (28 posts)
  - Limpiezas de desorden, casos extremos
  
- **Categoría 4:** Otros (7 posts)

**Formato:**
- URL exact (con fechas)
- Destino: `/limpieza-general.html`
- Instrucciones para .htaccess

**Audiencia:** Developers, SEO specialists  
**Tiempo de lectura:** 10 min

---

### 4. HTACCESS_REDIRECTS_EXAMPLE.txt
**Descripción:** Template técnico para configuración .htaccess  
**Contenido:**
- **Template base:** `RedirectMatch 301 ^/blog/YYYY/MM/DD/slug/$ /limpieza-general.html`
- **20 ejemplos** de redirects reales
- **Notas técnicas:**
  - Diferencia RedirectMatch vs Redirect
  - Orden en .htaccess (antes de RewriteRule)
  - Barra final (trailing slash)
  - Estado HTTP 301 vs 302
  
- **Validación:**
  - Comandos `curl -I` para verificar
  - Herramientas online (redirect-checker.org)
  - Google Search Console monitoring
  
- **Checklist de implementación:**
  - Pre-deployment (backup, staging)
  - Post-deployment (primeras 48h monitoring)

**Audiencia:** Developers, DevOps  
**Tiempo de lectura:** 15 min

---

### 5. CIUDADES_EXPANSION_MAESTRO.csv
**Descripción:** Tabla maestra de 11 ciudades  
**Contenido por fila (11 ciudades):**

| Campo | Ejemplo (Valladolid) |
|-------|----------------------|
| Prioridad | 1 |
| Tier | 1 |
| Semana | 2 |
| Ciudad | Valladolid |
| Provincia | Valladolid |
| CCAA | Castilla y León |
| Población | 305,000 |
| Estado_Actual | NUEVA |
| Context_Hook | "Cuando la industria se detiene" |
| Industrias_Principales | Alimentaria, fabricación, transformación |
| Clima_Caracteristicas | Inviernos duros, sequedad interior |
| Municipios_Vecinos | Tordesillas, Peñafiel, Medina del Campo |
| URL_Archivo | limpieza-de-incendios-valladolid.html |
| Meta_Title | "Valladolid: Expertos limpieza post incendio..." |
| Meta_Description | "Limpieza incendios Valladolid. Plantas..." |
| Copy_Hero_Short | Frase gancho de hero |
| Search_Volume_Estimado | 140-180/mes |
| Status_Implementacion | PENDING |

**Filas incluidas (11 ciudades):**
1. Valladolid (Tier 1) - Semana 2
2. Burgos (Tier 1) - Semana 2
3. Toledo (Tier 1) - Semana 3
4. Murcia (Tier 1) - Semana 3
5. Jaén (Tier 1) - Semana 3
6. Huesca (Tier 2) - Semana 4
7. Teruel (Tier 2) - Semana 4
8. Salamanca (Tier 2) - Semana 5
9. Cuenca (Tier 2) - Semana 5
10. Alicante (Tier 3) - Semana 5
11. Castellón (Tier 3) - Semana 5

**Secciones adicionales:**
- Notas meta (interpretación de columnas)
- Timeline resumen
- Validación pre-launch
- Municipios candidatos para Fase 3C (futura)

**Audiencia:** Project managers, copywriters, developers  
**Uso:** Reference durante desarrollo + status tracking

---

## 🗂️ ESTRUCTURA DE LECTURA RECOMENDADA

### Para Directivos / Stakeholders
1. ⭐ RESUMEN_EJECUTIVO_FINAL.md (5 min)
2. PLAN_CRITICO_3A_3B.md - Parte 3, sección 3.1-3.2 (10 min)

### Para Project Managers
1. ⭐ RESUMEN_EJECUTIVO_FINAL.md
2. PLAN_CRITICO_3A_3B.md - Completo (30-45 min)
3. CIUDADES_EXPANSION_MAESTRO.csv - Para tracking

### Para Copywriters
1. PLAN_CRITICO_3A_3B.md - Parte 2, sección 2.3 (15 min)
2. CIUDADES_EXPANSION_MAESTRO.csv - Datos contexto local
3. OFF_TOPIC_POSTS_REDIRECT_LIST.txt - Validar posts a descartar

### Para Developers
1. HTACCESS_REDIRECTS_EXAMPLE.txt (15 min)
2. OFF_TOPIC_POSTS_REDIRECT_LIST.txt (10 min)
3. PLAN_CRITICO_3A_3B.md - Parte 3, sección 3.3 Checklist

### Para SEO Specialists
1. PLAN_CRITICO_3A_3B.md - Parte 1 (análisis blog) + Parte 2 (expansión)
2. CIUDADES_EXPANSION_MAESTRO.csv - Volume estimado
3. RESUMEN_EJECUTIVO_FINAL.md - Impacto proyectado

---

## 📊 DATOS CLAVE

### Blog Analysis (Crítico 3A)
- **Total posts:** 201 únicos (2017-2025)
- **OFF-TOPIC:** 100 posts (49.8%)
- **Relevante:** 101 posts (50.2%)
- **Solución:** 301 redirects a `/limpieza-general.html`
- **Timeline:** 2 semanas

### Geographic Expansion (Crítico 3B)
- **Landings nuevas:** 11 ciudades
- **Tier 1 (5):** Valladolid, Burgos, Toledo, Murcia, Jaén
- **Tier 2 (4):** Huesca, Teruel, Salamanca, Cuenca
- **Tier 3 (2):** Alicante, Castellón
- **Search volume:** 570-840 búsquedas/mes
- **Leads esperados:** 4-7 leads/mes (6+ meses)
- **Valor/mes:** 8-14K€ potencial
- **Timeline:** 4 semanas desarrollo

### Combined Impact
- **Horas totales:** 37-45h
- **Coste (si outsource):** 900-1.350€
- **Timeline total:** 6 semanas
- **ROI estimado:** 8-14x

---

## ✅ IMPLEMENTACIÓN RÁPIDA

### Si tiene prisa (versión comprimida)

**Día 1:** Leer RESUMEN_EJECUTIVO_FINAL.md (5 min)  
**Día 2:** Crear `/limpieza-general.html` (1h)  
**Día 3:** Generar 100 redirects 301 (1h)  
**Día 4:** Test en staging (1h)  
**Día 5:** Deploy Fase 3A (30 min)  
**Semana 2-6:** Crear 11 landings Fase 3B (19h distribuidas)

**Total crítico path:** 6 semanas

---

## 🔍 VALIDACIÓN ANTES DE EMPEZAR

Antes de implementar, verificar:

### Fase 3A
- [ ] Confirmar que 100 posts OFF-TOPIC están bien identificados
- [ ] Verificar que no hay posts con valor oculto (ej: "limpieza de incendios" + "ducha")
- [ ] Validar que `/limpieza-general.html` no exista ya

### Fase 3B
- [ ] Confirmar que ninguna de las 11 ciudades tiene landing existente
- [ ] Validar municipios vecinos (no crear landings < 50K población sin valor)
- [ ] Verificar acentos en ciudades (Jaén, Córdoba, etc.)

---

## 📞 PRÓXIMOS PASOS

1. **Aprobación:** Revisar RESUMEN_EJECUTIVO_FINAL.md
2. **Asignación:** Designar copywriter + developer
3. **Staging:** Crear ambiente de prueba
4. **Semana 1:** Ejecutar Fase 3A
5. **Semana 2-6:** Ejecutar Fase 3B
6. **Semana 7+:** Monitorizar en Google Search Console

---

## 📝 NOTAS TÉCNICAS

- **Todos los redirects son 301 permanentes** (preservan SEO)
- **Fase 3A y 3B se pueden paralelizar** (pero recomienda hacer 3A primero)
- **Validar en staging antes de producción**
- **Monitorizar primeras 48h post-deploy**
- **Esperar 6-8 semanas para posicionamiento inicial**
- **Esperar 3-4 meses para posicionamiento consolidado (top 3)**

---

## 🎯 OBJETIVO FINAL

Convertir Nano Nex de "empresa de limpieza genérica" a "especialista SEO en limpieza POST-INCENDIO" con cobertura geográfica nacional (11 nuevas ciudades).

**Resultado esperado:** 8-14K€/mes de valor potencial (6+ meses post-launch)

---

**Documento actualizado:** 2026-06-14  
**Versión:** 1.0 Completa  
**Estado:** ✅ Listo para implementación

Para dudas o preguntas, referir al documento detallado PLAN_CRITICO_3A_3B.md
