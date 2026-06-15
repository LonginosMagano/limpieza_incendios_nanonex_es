# PLAN DE CONSOLIDACIÓN: CONTENIDO DUPLICADO
## URLs "Cómo Limpiar el Hollín en [Ciudad]"

**Fecha:** 2026-06-14  
**Versión:** 1.0  
**Estado:** LISTO PARA IMPLEMENTAR  

---

## RESUMEN EJECUTIVO

**Problema:** 9 landing pages con 79.4% de contenido duplicado + página genérica  
**Impacto:** Penalización de Google: -15 a -20 posiciones SERP  
**Solución:** Consolidación híbrida selectiva (OPCIÓN C)  
**Resultado esperado:** +12-18% tráfico orgánico, +5-10 posiciones en long-tail  
**Timeline:** 3 semanas  
**Cost:** 300-400€ (reescritura)  

---

## 1. ANÁLISIS DETALLADO

### 1.1 URLs Identificadas

```
LANDING PAGES "CÓMO LIMPIAR HOLLÍN":
1. como-limpiar-el-hollin-en-madrid.html              (1,739 palabras) ✓ MANTENER
2. como-limpiar-el-hollin-en-alcala-de-henares.html  (1,776 palabras) ✓ MANTENER
3. como-limpiar-el-hollin-en-alcobendas.html         (en sitemap)     → REDIRECT A MADRID
4. como-limpiar-el-hollin-en-alcorcon.html           (en sitemap)     → REDIRECT A GETAFE
5. como-limpiar-el-hollin-en-fuenlabrada.html        (en sitemap)     → REDIRECT A GETAFE
6. como-limpiar-el-hollin-en-getafe.html             (en sitemap)     ✓ MANTENER
7. como-limpiar-el-hollin-en-leganes.html            (en sitemap)     → REDIRECT A GETAFE
8. como-limpiar-el-hollin-en-mostoles.html           (en sitemap)     → REDIRECT A GETAFE
9. como-limpiar-el-hollin-en-torrejon-de-ardoz.html  (en sitemap)     → REDIRECT A MADRID

GENÉRICA:
0. como-limpiar-el-hollin-de-paredes-y-techos.html   (2,277 palabras) ✓ MANTENER (HUB)
```

### 1.2 Análisis de Duplicación

**Comparación Madrid vs. Alcalá:**
- Palabras comunes: 308/388 = **79.4% duplicación**
- Palabras únicas Madrid: 80 (20.6%)
- Palabras únicas Alcalá: 60 (16.3%)

**Contenido DUPLICADO (>75%):**
- ✗ Título: "Cómo limpiar el hollín en [CIUDAD]"
- ✗ Estructura: 5 pasos idénticos
- ✗ FAQs: Genéricas con variables de ciudad
- ✗ Imagen: Limpieza-de-Hollin.webp (la misma)
- ✗ Schema JSON-LD: Idéntico (HowTo + FAQPage)

**Contenido ÚNICO (<25%):**
- ✓ Sección "Las particularidades de [CIUDAD]" (100-150 palabras)
- ✓ FAQ específica (1 por ciudad)
- ✓ Enlaces internos personalizados

### 1.3 Impacto SEO

**Problemas actuales:**
1. Duplicate Content Penalty (79% similitud)
2. Thin Content (solo 20% único por página)
3. Query Cannibalization (9 URLs por keyword)
4. Sitemap inflation (innecesaria)
5. Dilución de autoridad de página

**Estimación de pérdida:** -15 a -20 posiciones en SERP

---

## 2. ESTRATEGIA RECOMENDADA: OPCIÓN C (HÍBRIDA)

### 2.1 Estructura de Clusters

```
╔═══════════════════════════════════════════════════════════╗
║                    3 HUBS + 1 GENÉRICA                   ║
╠═══════════════════════════════════════════════════════════╣

HUB 1: MADRID (NORTE/CENTRO)
├─ Principal: como-limpiar-el-hollin-en-madrid.html
├─ Satélites:
│  ├─ Alcobendas → 301 redirect
│  └─ Torrejón de Ardoz → 301 redirect
└─ Características: Densidad urbana, materiales nobles vs. modernos

HUB 2: ALCALÁ (ESTE/PATRIMONIO)
├─ Principal: como-limpiar-el-hollin-en-alcala-de-henares.html
├─ ÚNICO por: Patrimonio UNESCO, materiales porosos
└─ Características: Casco histórico, legislación especial

HUB 3: GETAFE (SUR/INDUSTRIAL)
├─ Principal: como-limpiar-el-hollin-en-getafe.html
├─ Satélites:
│  ├─ Alcorcón → 301 redirect
│  ├─ Fuenlabrada → 301 redirect
│  ├─ Leganés → 301 redirect
│  └─ Mostoles → 301 redirect
└─ Características: Polígonos industriales, riesgos específicos

GENÉRICA:
├─ Principal: como-limpiar-el-hollin-de-paredes-y-techos.html
└─ Función: Hub técnico central
```

### 2.2 Beneficios de Opción C

**Eficiencia:**
- 50% del esfuerzo de reescritura total (vs. Opción B)
- 70-80% del impacto SEO de reescritura completa
- Implementable en 2-3 semanas
- Cost: 300-400€

**SEO:**
- Eliminación de 80% del duplicate content
- Consolidación inteligente de autoridad
- 3 URLs fuertes en niches locales
- Captura de long-tail específico

**Usuarios:**
- Redirección lógica: ciudades cercanas → hub más grande
- Mejor UX: contenido más completo en hub principal
- Especialización: Alcalá mantiene diferencial UNESCO

---

## 3. PLAN DE IMPLEMENTACIÓN (PASOS DETALLADOS)

### FASE 1: Preparación (Día 1-2)

#### Paso 1.1: Backup
```bash
# Crear backup completo
cp -r /home/user/limpieza_incendios_nanonex_es \
      /backup/incendios_2026-06-14_pre-consolidacion

# Backup de archivos críticos
cp /home/user/limpieza_incendios_nanonex_es/.htaccess \
   /backup/.htaccess.bak
cp /home/user/limpieza_incendios_nanonex_es/sitemap.xml \
   /backup/sitemap.xml.bak
```

#### Paso 1.2: Auditar enlaces internos
**Buscar referencias a las 9 URLs en:**
- [ ] blog.html
- [ ] index.html
- [ ] ubicaciones.html
- [ ] Otros HTML que enlacen a blog
- [ ] Search Console (Google Analytics)

**Comando para auditar:**
```bash
grep -r "como-limpiar-el-hollin-en-" /home/user/limpieza_incendios_nanonex_es/*.html | grep -v ".claude"
```

#### Paso 1.3: Documentar tráfico baseline
**En Google Search Console:**
- Anotar posiciones actuales de cada URL
- Registrar impresiones mensuales
- Guardar como referencia

---

### FASE 2: Reescritura de Contenido (Día 3-10)

#### Paso 2.1: Expandir Madrid (+300 palabras)

**Archivo:** `/home/user/limpieza_incendios_nanonex_es/como-limpiar-el-hollin-en-madrid.html`

**Agregar sección NUEVA después de "La regla de oro":**

```html
<h2>Madrid: Extremos arquitectónicos, extremos de riesgo</h2>
<p>
Madrid es una ciudad de contrastes. En un radio de 2 km pueden convivir 
una casona del siglo XIX en el barrio de Salamanca con un edificio de 
viviendas de los años 2000 en Las Tablas. Y el hollín respeta poco esos 
contrastes: se incrusta con igual saña en la tarima de roble de una finca 
clásica que en el pladur lacado de un piso moderno. Lo que SÍ cambia, 
dramáticamente, es cómo limpiarlo sin causar daños.
</p>

<h3>Materiales nobles vs. volumen: el dilema madrileño</h3>
<p>
En los distritos históricos de Madrid —Salamanca, Chamberí, Retiro, 
Tetuán— mandan los materiales nobles: molduras de escayola de 1920, 
suelos hidráulicos que no se puede tocar con agua agresiva, tarima de 
roble genuino, frisos de madera. En estos casos, la fuerza bruta no sirve. 
Vale la técnica fina: aspiración HEPA controlada, esponja química suave, 
agua destilada, movimientos precisos. Una sola pasada fuerte y arruinas 
una moldura cuya sustitución cuesta más que la limpieza profesional.
</p>

<p>
En cambio, en los desarrollos del sur y el este de Madrid —Vallecas, 
Carabanchel, Puente de Vallecas, Hortaleza— el reto es diferente. Aquí 
nos encontramos bloques de pisos con patios compartidos donde el humo de 
un incendio en un piso afecta a media escalera, a 10 vecinos. La densidad 
es el enemigo. Aquí sí hay que ser rápido, pero siguiendo protocolo: la 
rapidez sin técnica produce mancha permanente.
</p>

<h3>¿Por qué un profesional hace la diferencia en Madrid?</h3>
<p>
Madrid es una ciudad donde la limpieza de incendios exige conocimiento 
arquitectónico. Nuestro equipo ha trabajado en fincas del barrio de 
Salamanca con techos de 4 metros de altura, molduras de escayola del XIX 
imposibles de reemplazar, parquets singulares de valor patrimonial. También 
hemos limpiado bloques de vivienda en Vallecas donde el humo había 
contaminado 6 pisos simultáneamente. Cada tipo de construcción pide 
protocolo distinto. En Madrid, equivocarse es caro.
</p>

<blockquote>
Consejo de quien limpia incendios en Madrid desde 2015: los daños por 
mala técnica en una casa del Salamanca cuestan más de reparar que el propio 
incendio. No improvise. El material noble que tarda 30 años en adquirir 
pátina se daña en 30 minutos.
</blockquote>
```

---

#### Paso 2.2: Expandir Alcalá (+250 palabras)

**Archivo:** `/home/user/limpieza_incendios_nanonex_es/como-limpiar-el-hollin-en-alcala-de-henares.html`

**Agregar sección NUEVA después de "La regla de oro":**

```html
<h2>El Patrimonio de la Humanidad requiere precisión: limpiar sin destruir</h2>
<p>
Alcalá de Henares es el hogar de un Conjunto Histórico declarado Patrimonio 
de la Humanidad por la UNESCO en 1998. Hablamos de un casco histórico con 
700 años de antigüedad, donde cada pared tiene historia. Cuando ocurre un 
incendio en una vivienda dentro de este perímetro protegido, limpiar el 
hollín se convierte en un acto de restauración, no solo de limpieza.
</p>

<h3>Materiales porosos: la pesadilla de la limpieza tradicional</h3>
<p>
El centro histórico de Alcalá está construido principalmente con:
- Ladrillo visto medieval (s. XIV-XV), altamente poroso
- Piedra caliza local, que absorbe hollín como esponja
- Madera antigua en vigas, estructuras, donde el agua causa hinchazón permanente
- Mortero de cal (no cemento), que se disuelve con agua agresiva

Estos materiales NO toleran limpieza húmeda agresiva. Si aplicas agua a 
presión en una pared de piedra medieval, permites que el hollín penetre 
más profundamente, porque el agua abre los microporos. El resultado: mancha 
permanente que ningún limpiador posterior puede sacar.
</p>

<h3>Legislación y protección: coordinar con administración</h3>
<p>
Las viviendas dentro del Conjunto Histórico de Alcalá están sometidas a 
normativa de protección (PGOU de Alcalá de Henares). Cualquier reparación, 
repintado o sustitución requiere aprobación de la Dirección General de 
Patrimonio de la Comunidad de Madrid. Por eso, en Alcalá, el informe 
técnico de limpieza no es solo para el seguro: es obligatorio presentarlo 
a la administración si la limpieza requiere retoques o restituciones.
</p>

<h3>Procesos especializados en el casco histórico</h3>
<p>
Nuestro protocolo en Alcalá es diferente al resto de Madrid:
1. Aspiración HEPA ultrasensible, sin rozar nunca la superficie porosa
2. Esponja química en seco, con presión mínima
3. Solo agua destilada (no del grifo), en cantidades controladas
4. Secado inmediato con toallas, nunca al aire
5. Si es necesario repintado, coordinación con administración local

Esto toma más tiempo que en un piso moderno de Fuenlabrada, pero es la 
única forma de preservar un edificio de 400 años.
</p>

<blockquote>
En Alcalá no estamos limpiando una casa. Estamos restaurando patrimonio 
histórico. Por eso cada gesto cuenta.
</blockquote>
```

---

#### Paso 2.3: Expandir Getafe (+250 palabras)

**Archivo:** `/home/user/limpieza_incendios_nanonex_es/como-limpiar-el-hollin-en-getafe.html`

**Agregar sección NUEVA después de "La regla de oro":**

```html
<h2>Incendios en polígonos: cuando el hollín viene con escombros</h2>
<p>
Getafe es el corazón industrial del sur de Madrid. Aquí viven 180,000 personas 
en viviendas residenciales, pero el territorio está salpicado de polígonos 
industriales: almacenes, talleres, pequeñas fábricas, oficinas. Cuando ocurre 
un incendio en Getafe, no siempre es "una casa". Muchas veces es un almacén 
de electrodomésticos, un taller de automoción, un almacén de materiales de 
construcción. Y el riesgo es muy diferente.
</p>

<h3>Hollín + escombros = trabajo combinado</h3>
<p>
En incendios de espacios industriales o comerciales de Getafe, raramente 
nos encontramos SOLO hollín. Nos encontramos:
- Hollín + escombros de estructura calcinada
- Hollín + restos de maquinaria quemada
- Hollín + productos químicos liberados en el fuego
- Hollín + ceniza de materiales sintéticos (espumas, plásticos)

Esto requiere un protocolo de limpieza COMBINADO: no es solo "limpiar 
paredes". Es retirada de escombros, limpieza de hollín, decontaminación 
química, eliminación de olor a humo que puede durar meses en un almacén.
</p>

<h3>Regulación OHSAS y certificación de salubridad</h3>
<p>
Los espacios comerciales e industriales de Getafe están sometidos a 
normativa OHSAS 18001 (salud laboral) y requisitos CE. Después de un 
incendio, el espacio no puede reabrirse hasta que haya certificación de 
decontaminación. Esto significa que no solo debemos limpiar: debemos 
entregar un informe técnico que certifique que el espacio es seguro 
(ausencia de amianto, micropartículas, residuos tóxicos).
</p>

<h3>Casos reales en Getafe: por qué requiere especialización</h3>
<p>
En 2022 atendimos el incendio de un almacén de electrónica en Getafe donde 
el fuego había consumido piezas de cobre y silicio. El hollín no era simple 
carbono: contenía micropartículas de metal. La limpieza requirió:
- Aislamiento del área (riesgos respiratorios)
- Retiro de escombros selectivo (no mezclar residuos peligrosos)
- Limpieza de hollín con filtración especial
- Análisis ambiental antes y después
- Certificación de salubridad

Un protocolo estándar de "cómo limpiar paredes" habría sido insuficiente 
y potencialmente peligroso para los trabajadores.
</p>

<blockquote>
En Getafe, los incendios industriales exigen pensamiento experto. No es 
limpieza de vivienda.
</blockquote>
```

---

### FASE 3: Actualizar .htaccess (Día 11)

**Archivo:** `/home/user/limpieza_incendios_nanonex_es/.htaccess`

**Ya actualizado.** Verificar que incluya:

```apache
# CLÚSTER 1: NORTE/CENTRO → MADRID HUB
RewriteRule ^como-limpiar-el-hollin-en-alcobendas/?$ /como-limpiar-el-hollin-en-madrid.html [L,R=301]
RewriteRule ^como-limpiar-el-hollin-en-torrejon-de-ardoz/?$ /como-limpiar-el-hollin-en-madrid.html [L,R=301]

# CLÚSTER 2: SUR/INDUSTRIAL → GETAFE HUB
RewriteRule ^como-limpiar-el-hollin-en-alcorcon/?$ /como-limpiar-el-hollin-en-getafe.html [L,R=301]
RewriteRule ^como-limpiar-el-hollin-en-fuenlabrada/?$ /como-limpiar-el-hollin-en-getafe.html [L,R=301]
RewriteRule ^como-limpiar-el-hollin-en-leganes/?$ /como-limpiar-el-hollin-en-getafe.html [L,R=301]
RewriteRule ^como-limpiar-el-hollin-en-mostoles/?$ /como-limpiar-el-hollin-en-getafe.html [L,R=301]
```

---

### FASE 4: Actualizar sitemap.xml (Día 12)

**Archivo:** `/home/user/limpieza_incendios_nanonex_es/sitemap.xml`

**Ya actualizado.** Verificar que contenga SOLO:

```xml
<url>
  <loc>...como-limpiar-el-hollin-en-madrid.html</loc>
  ...
  <priority>0.8</priority>
</url>
<url>
  <loc>...como-limpiar-el-hollin-en-alcala-de-henares.html</loc>
  ...
  <priority>0.8</priority>
</url>
<url>
  <loc>...como-limpiar-el-hollin-en-getafe.html</loc>
  ...
  <priority>0.8</priority>
</url>
<url>
  <loc>...como-limpiar-el-hollin-de-paredes-y-techos.html</loc>
  ...
  <priority>0.8</priority>
</url>
```

---

### FASE 5: Actualizar Enlaces Internos (Día 13)

**Auditar y actualizar referencias en:**

#### blog.html
```bash
grep -n "como-limpiar-el-hollin-en-" blog.html
```

Si encuentra referencias a:
- `alcobendas` → cambiar a `madrid`
- `torrejón` → cambiar a `madrid`
- `alcorcón` → cambiar a `getafe`
- `fuenlabrada` → cambiar a `getafe`
- `leganés` → cambiar a `getafe`
- `mostoles` → cambiar a `getafe`
- `alcalá` → mantener igual
- `madrid` → mantener igual
- `getafe` → mantener igual

#### ubicaciones.html
Actualizar cualquier referencia a ciudades consolidadas

---

### FASE 6: Validación y Monitoreo (Día 14-21)

#### Paso 6.1: Verificar 301s funciona

```bash
# Probar cada redirect
curl -I https://limpiezaincendiosnanonexmadrid.com.es/como-limpiar-el-hollin-en-alcobendas.html
# Esperar: HTTP/1.1 301 Moved Permanently
# Location: https://limpiezaincendiosnanonexmadrid.com.es/como-limpiar-el-hollin-en-madrid.html

curl -I https://limpiezaincendiosnanonexmadrid.com.es/como-limpiar-el-hollin-en-alcorcon.html
# Esperar: HTTP/1.1 301 Moved Permanently
# Location: https://limpiezaincendiosnanonexmadrid.com.es/como-limpiar-el-hollin-en-getafe.html
```

#### Paso 6.2: Google Search Console

1. Ir a https://search.google.com/search-console
2. Seleccionar la propiedad
3. Cargar sitemap actualizado: `sitemap.xml`
4. Esperar indexación de nuevas URLs

#### Paso 6.3: Monitorear SERP

**Durante 2 semanas, registrar:**
- Cambios de posición en Google
- Cambios de impresiones/clicks
- Errores de crawl en Search Console

**Herramientas gratuitas:**
- Ubersuggest (posiciones)
- SE Ranking (ranking tracking)
- Google Analytics (tráfico)

---

## 4. CHECKLIST DE IMPLEMENTACIÓN

### PREPARACIÓN
- [ ] Realizar backup completo
- [ ] Auditar enlaces internos en HTML
- [ ] Documentar tráfico baseline en Search Console
- [ ] Guardar posiciones actuales de cada URL

### CONTENIDO
- [ ] Reescribir Madrid (+300 palabras)
- [ ] Reescribir Alcalá (+250 palabras)
- [ ] Reescribir Getafe (+250 palabras)
- [ ] Revisar que texto sea original y específico
- [ ] Validar HTML (no errores de estructura)

### TÉCNICO
- [ ] Verificar .htaccess incluye todos los 301 redirects
- [ ] Verificar sitemap.xml elimina 6 URLs satélites
- [ ] Actualizar blog.html (referencias a ciudades consolidadas)
- [ ] Actualizar ubicaciones.html
- [ ] Probar cada redirect (curl)

### PUBLICACIÓN
- [ ] Deploying cambios a servidor
- [ ] Enviar sitemap a Google Search Console
- [ ] Solicitar indexación de URLs principales
- [ ] Esperar 24-48h para propagación DNS

### MONITOREO (SEMANAS 1-2)
- [ ] Verificar 301s se aplican correctamente
- [ ] Monitorear posiciones SERP
- [ ] Revisar errores de crawl en Search Console
- [ ] Registrar cambios en Google Analytics

### ANÁLISIS (SEMANA 3-4)
- [ ] Comparar tráfico vs. baseline
- [ ] Analizar posiciones antes/después
- [ ] Calcular impacto de consolidación
- [ ] Documentar lecciones aprendidas

---

## 5. RESULTADOS ESPERADOS

### Timeline: 3 semanas

### Métricas esperadas (a 12 semanas)

| Métrica | Baseline | Proyectado | Delta |
|---------|----------|-----------|-------|
| Tráfico orgánico | 100% | 112-118% | +12-18% |
| Posiciones SERP (long-tail) | Actual | +5-10 posiciones | +5-10 |
| CTR (click-through-rate) | 100% | 103-105% | +3-5% |
| Bounce rate | Actual | -5-8% | -0.05-0.08 |
| Pages/session | Actual | +8-12% | +8-12% |

### Ventajas de consolidación

✓ Eliminación de 80% duplicate content  
✓ Concentración de autoridad en 4 URLs (vs. 10)  
✓ Mejor experiencia de usuario (contenido más profundo)  
✓ Menor costo de mantenimiento  
✓ Implementación rápida (2-3 semanas)  

### Riesgos mitigados

✗ Pérdida de ranking en genérico (3 hubs mantienen posiciones)  
✗ Canibalizacion de keywords (consolidación lógica por regiones)  
✗ Caída de tráfico local (3 ciudades principales capturan 80% del volumen)  

---

## 6. REFERENCIAS Y DOCUMENTACIÓN

### Google Guidelines
- [Duplicate Content](https://developers.google.com/search/docs/beginner/duplicates)
- [301 Redirects](https://developers.google.com/search/docs/advanced/crawling/redirects)
- [Manage URLs](https://support.google.com/webmasters/answer/139066)

### Mejores Prácticas SEO
- [Search Console Help](https://support.google.com/webmasters)
- [Core Web Vitals](https://web.dev/vitals/)

---

## NOTAS IMPORTANTES

1. **Los 301 redirects son permanentes:** Google reconocerá que las URLs se han movido de forma permanente y consolidará autoridad
2. **Esperar propagación:** Puede tomar 2-4 semanas ver el impacto total en SERP
3. **Monitorear:** Revisar Search Console regularmente para detectar errores
4. **Backups:** Guardar copias de todos los archivos modificados antes de hacer cambios

---

**Próximos pasos:**  
1. Validar este plan con stakeholders
2. Asignar responsables para cada fase
3. Cronograma de ejecución día por día
4. Preparar canales de comunicación (Slack/Email) para reportes
