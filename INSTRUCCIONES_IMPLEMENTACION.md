# 📋 INSTRUCCIONES DE IMPLEMENTACIÓN
## Nano Nex Madrid - Limpieza por Incendio

**Versión**: 2.0 SEO-Optimizada
**Fecha**: Mayo 31, 2026
**Dominio**: limpiezaincendiosnanonexmadrid.com.es

---

## 🚀 QUICK START (Primeros 30 minutos)

### PASO 1: Backup del código actual
```bash
# En tu servidor
cp -r public_html public_html.backup.2025-05-31
```

### PASO 2: Archivos a reemplazar/crear
Estos son los archivos listos para usar:

```
✅ index_v2.html        → Renombrar a index.html (reemplazar actual)
✅ .htaccess            → Reemplazar .htaccess actual
✅ robots.txt           → Reemplazar robots.xml
✅ sitemap.xml          → Crear nuevo (o reemplazar)
✅ 404.html             → Crear nuevo
✅ llms.txt             → Crear en raíz
```

### PASO 3: Verificar rutas de imágenes
El index_v2.html usa rutas relativas:
```html
<img src="./Logo Nano Nex.png" ...>
```

Asegúrate de que todas las imágenes del repo estén en la **raíz** (`/public_html/`).

---

## 📁 ESTRUCTURA DE CARPETAS (Recomendada)

```
public_html/
├── index.html                          ← Reemplazar con index_v2.html
├── 404.html                            ← Crear (nuevo)
├── .htaccess                           ← Reemplazar
├── robots.txt                          ← Crear (renombrar robots.xml a robots.txt)
├── sitemap.xml                         ← Crear (nuevo)
├── llms.txt                            ← Crear (nuevo)
├── privacidad.html                     ← Mantener actual
├── cookies.html                        ← Mantener actual
├── aviso-legal.html                    ← Crear si no existe
├── Logo Nano Nex.png                   ← Verificar ruta relativa
├── Favicon trasnparente Rojo Naranja.png ← Verificar favicon
├── [todas las imágenes JPG/PNG]
├── blog/
│   ├── index.html                      ← CREAR (listado de artículos)
│   ├── que-hacer-incendio-casa/
│   │   └── index.html                  ← CREAR
│   ├── eliminar-olor-humo/
│   │   └── index.html                  ← CREAR
│   ├── seguro-limpieza-incendio/
│   │   └── index.html                  ← CREAR
│   ├── 72-horas-criticas/
│   │   └── index.html                  ← CREAR
│   ├── ozono-vs-tradicional/
│   │   └── index.html                  ← CREAR
│   └── prevenir-incendio-hogar/
│       └── index.html                  ← CREAR
├── limpieza-incendios-madrid/
│   └── index.html                      ← CREAR
├── limpieza-incendios-salamanca/
│   └── index.html                      ← CREAR
├── limpieza-incendios-malasana/
│   └── index.html                      ← CREAR
├── limpieza-incendios-retiro/
│   └── index.html                      ← CREAR
├── limpieza-incendios-carabanchel/
│   └── index.html                      ← CREAR
├── limpieza-incendios-vallecas/
│   └── index.html                      ← CREAR
├── limpieza-incendios-hortaleza/
│   └── index.html                      ← CREAR
├── limpieza-incendios-latina/
│   └── index.html                      ← CREAR
├── limpieza-incendios-tetuan/
│   └── index.html                      ← CREAR
├── limpieza-incendios-chamberi/
│   └── index.html                      ← CREAR
├── limpieza-incendios-centro/
│   └── index.html                      ← CREAR
├── limpieza-incendios-alcala-henares/  ← CREAR
├── limpieza-incendios-alcobendas/      ← CREAR
├── limpieza-incendios-alcorcon/        ← CREAR
├── limpieza-incendios-fuenlabrada/     ← CREAR
├── limpieza-incendios-getafe/          ← CREAR
├── limpieza-incendios-leganes/         ← CREAR
├── limpieza-incendios-mostoles/        ← CREAR
├── limpieza-incendios-san-sebastian-reyes/ ← CREAR
├── limpieza-incendios-torrejon-ardoz/  ← CREAR
├── limpieza-incendios-tres-cantos/     ← CREAR
├── limpieza-incendios-colmenar-viejo/  ← CREAR
├── limpieza-incendios-boadilla-monte/  ← CREAR
├── limpieza-incendios-las-rozas/       ← CREAR
├── limpieza-incendios-majadahonda/     ← CREAR
└── limpieza-incendios-pozuelo-alarcon/ ← CREAR
```

---

## 🔧 PASOS DETALLADOS DE IMPLEMENTACIÓN

### 1️⃣ REEMPLAZAR INDEX.HTML

1. Descarga `index_v2.html` de `/home/claude/`
2. Renómbralo a `index.html`
3. Sube a `public_html/index.html` (reemplaza el actual)
4. **Verifica en el navegador**: https://limpiezaincendiosnanonexmadrid.com.es/

**Checklist post-upload**:
- [ ] Logo visible y centrado
- [ ] Topbar roja con "Operativos 24/7"
- [ ] Botones flotantes (llamada + WhatsApp) en esquina derecha
- [ ] Formulario funciona
- [ ] Links internos funcionan
- [ ] Imágenes cargan correctamente

---

### 2️⃣ CREAR/REEMPLAZAR .HTACCESS

1. Descarga `.htaccess` de `/home/claude/`
2. Sube a `public_html/.htaccess` (reemplaza el actual)
3. **Verifica**:
   - HTTP → HTTPS redirect funciona
   - www → sin-www redirect funciona
   - Error 404 funciona

```bash
# Test en terminal
curl -I https://www.limpiezaincendiosnanonexmadrid.com.es
# Debe mostrar: HTTP/2 301 (redirect)
```

---

### 3️⃣ CREAR ROBOTS.TXT

1. Descarga `robots.txt` de `/home/claude/`
2. Sube a `public_html/robots.txt` (renombra o reemplaza `robots.xml`)
3. **Verifica**:
   - https://limpiezaincendiosnanonexmadrid.com.es/robots.txt (visible)
   - Contiene referencia a sitemap

---

### 4️⃣ CREAR SITEMAP.XML

1. Descarga `sitemap.xml` de `/home/claude/`
2. Sube a `public_html/sitemap.xml`
3. **Verifica**:
   - https://limpiezaincendiosnanonexmadrid.com.es/sitemap.xml (válido XML)
   - Contiene 40+ URLs

---

### 5️⃣ CREAR 404.HTML

1. Descarga `404.html` de `/home/claude/`
2. Sube a `public_html/404.html`
3. **Verifica** probando URL inexistente:
   - https://limpiezaincendiosnanonexmadrid.com.es/test-404/
   - Debe mostrar página profesional de error

---

### 6️⃣ CREAR LLMs.TXT

1. Descarga `llms.txt` de `/home/claude/`
2. Sube a `public_html/llms.txt`
3. **Verifica**:
   - https://limpiezaincendiosnanonexmadrid.com.es/llms.txt (accesible)

---

### 7️⃣ CREAR LANDINGS DE BARRIOS (10 PÁGINAS)

**PARA CADA BARRIO:**

```
Barrio: Salamanca
Slug: salamanca
URL: /limpieza-incendios-salamanca/
Keywords: limpieza por incendio Salamanca, hollín Salamanca
Contenido: 900-1000 palabras únicas
```

**Estructura base** (copiar y personalizar):

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Limpieza por Incendio en Salamanca, Madrid | Nano Nex</title>
    <meta name="description" content="Limpieza por incendio en Salamanca, Madrid. Especialistas en eliminación de hollín. Servicio urgente 24h. Tu seguro lo cubre.">
    <link rel="canonical" href="https://limpiezaincendiosnanonexmadrid.com.es/limpieza-incendios-salamanca/">
    
    <!-- SCHEMA LocalBusiness -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Nano Nex - Limpieza por Incendio Salamanca",
      "areaServed": "Salamanca, Madrid",
      "url": "https://limpiezaincendiosnanonexmadrid.com.es/limpieza-incendios-salamanca/",
      "telephone": "+34911086565"
    }
    </script>
</head>
<body>
    <!-- Incluir header/footer iguales al index -->
    <h1>Limpieza por incendio en Salamanca, Madrid</h1>
    
    <!-- Contenido único para Salamanca -->
    <p>
        El barrio de Salamanca es conocido por sus...
        [Descripción contextual, arquitectura, riesgos específicos]
    </p>
    
    <!-- Testimonial local -->
    <h2>Cliente en Salamanca</h2>
    <p>"Vivía en la calle Serrano..."</p>
    
    <!-- Interlinking -->
    <h3>También cubrimos barrios cercanos:</h3>
    <ul>
        <li><a href="/limpieza-incendios-chamberi/">Chamberí</a></li>
        <li><a href="/limpieza-incendios-madrid/">Madrid Capital</a></li>
    </ul>
    
    <!-- Municipios cercanos -->
    <h3>Disponible en municipios cercanos:</h3>
    <ul>
        <li><a href="/limpieza-incendios-getafe/">Getafe</a></li>
        <li><a href="/limpieza-incendios-leganés/">Leganés</a></li>
    </ul>
</body>
</html>
```

**Barrios a crear (10 páginas)**:
- [ ] Salamanca
- [ ] Malasaña
- [ ] Retiro
- [ ] Carabanchel
- [ ] Vallecas
- [ ] Hortaleza
- [ ] Latina
- [ ] Tetuán
- [ ] Chamberí
- [ ] Centro

---

### 8️⃣ CREAR LANDINGS DE MUNICIPIOS (15 PÁGINAS)

**Misma estructura que barrios, pero con datos municipales**:

```
Municipio: Getafe
Slug: getafe
URL: /limpieza-incendios-getafe/
Keywords: limpieza por incendio Getafe, hollín Getafe
Contenido: 1000-1200 palabras únicas
```

**Municipios a crear (15 páginas)**:
- [ ] Alcalá de Henares
- [ ] Alcobendas
- [ ] Alcorcón
- [ ] Fuenlabrada
- [ ] Getafe
- [ ] Leganés
- [ ] Móstoles
- [ ] San Sebastián de los Reyes
- [ ] Torrejón de Ardoz
- [ ] Tres Cantos
- [ ] Colmenar Viejo
- [ ] Boadilla del Monte
- [ ] Las Rozas
- [ ] Majadahonda
- [ ] Pozuelo de Alarcón

---

### 9️⃣ CREAR BLOG (6 ARTÍCULOS)

**Estructura de cada artículo**:

```html
<h1>¿Qué hacer después de un incendio en casa?</h1>

<p class="respuesta-rapida">
  <strong>Respuesta rápida:</strong> 
  Lo primero es asegurar que no hay peligro, evaluar daños con profesionales, 
  contactar con tu seguro y contratar limpieza técnica antes de 72 horas 
  para evitar oxidación del hollín.
</p>

<h2>1. Los primeros pasos tras un incendio</h2>
<p>...</p>

<h2>2. Contactar con el seguro de hogar</h2>
<p>...</p>

<h2>3. Contratar limpieza profesional urgente</h2>
<p>...</p>

<h2>La gente también pregunta</h2>
<div class="faq">
  <h3>¿Quién paga la limpieza?</h3>
  <p>...</p>
</div>

<h2>¿Necesitas ayuda urgente?</h2>
<a href="tel:911086565">632 107 272</a>
```

**Artículos a crear (6 páginas)**:
- [ ] que-hacer-incendio-casa
- [ ] eliminar-olor-humo
- [ ] seguro-limpieza-incendio
- [ ] 72-horas-criticas
- [ ] ozono-vs-tradicional
- [ ] prevenir-incendio-hogar

---

## 📊 VERIFICACIÓN POST-IMPLEMENTACIÓN

### Google Search Console

```
1. Subir nuevo sitemap.xml
   → https://search.google.com/search-console
   → Sitemaps → Añadir
   → https://limpiezaincendiosnanonexmadrid.com.es/sitemap.xml

2. Solicitar indexación de URLs
   → Homepage primero
   → Luego barrios/municipios principales (Getafe, Alcobendas)
   → Blog después

3. Monitorear errores
   → Errores de rastreo
   → Problemas de cobertura
```

### Validadores Online

- [ ] **HTML Validator**: https://validator.w3.org/
- [ ] **XML Sitemap**: https://www.xml-sitemaps.com/validate-xml-sitemap.html
- [ ] **Robots.txt**: https://www.robotstester.com/
- [ ] **Schema Markup**: https://schema.org/validate

### Mobile & Performance

- [ ] **Google Mobile-Friendly Test**: https://search.google.com/test/mobile-friendly
- [ ] **PageSpeed Insights**: https://pagespeed.web.dev/
- [ ] **Lighthouse**: Chrome DevTools → Lighthouse

---

## 🔐 CAMBIOS CRÍTICOS EN FORMSPREE → FORMSUBMIT

El nuevo index.html usa **FormSubmit** en lugar de Formspree:

```html
<!-- VIEJO (Formspree) -->
<form action="https://formspree.io/f/xqarnldw" method="POST">

<!-- NUEVO (FormSubmit) -->
<form action="https://formsubmit.co/info@nanonex.es" method="POST">
    <input type="hidden" name="_subject" value="Presupuesto Limpieza - limpiezaincendiosnanonexmadrid.com.es">
```

**Ventajas de FormSubmit**:
- ✅ Gratuito sin límites
- ✅ GDPR compliant
- ✅ Sin JavaScript necesario
- ✅ Captcha integrado

**Verificación**:
1. Prueba el formulario en homepage
2. Verifica email en info@nanonex.es
3. Confirma que aparezca el campo "Origen: limpiezaincendiosnanonexmadrid.com.es"

---

## 📈 TIMELINE RECOMENDADO

| Semana | Tarea | Duración |
|--------|-------|----------|
| **1** | Reemplazar index + .htaccess + robots | 2h |
| **1** | Crear 404.html + llms.txt + sitemap | 1h |
| **1-2** | Crear 10 landings barrios | 15h |
| **2** | Crear 15 landings municipios | 20h |
| **2-3** | Crear 6 artículos blog | 25h |
| **3** | Testing + optimizaciones | 8h |
| **3** | Envío a Google Search Console | 1h |
| **Total** | | **~72 horas (≈9 días)**|

---

## ⚠️ CHECKLIST CRÍTICO ANTES DE PUBLICAR

- [ ] Index.html reemplazado y funciona
- [ ] Todas las imágenes cargan correctamente
- [ ] Links internos funcionan (sin errores 404)
- [ ] Formulario envía correos a info@nanonex.es
- [ ] Botones flotantes (llamada + WhatsApp) visibles en móvil
- [ ] Cookie banner aparece (delay 2seg)
- [ ] HTTPS forzado funciona
- [ ] .htaccess gzip comprime assets
- [ ] Favicon visible
- [ ] Logo no rompe en subdirectorios
- [ ] Meta descriptions únicas en cada página
- [ ] H1 con keyword principal
- [ ] Schema markup válido (https://schema.org/validate)
- [ ] Sitemap.xml válido
- [ ] Robots.txt accesible
- [ ] 404.html funciona
- [ ] llms.txt visible
- [ ] Google Search Console conectada
- [ ] Sitemap enviado a GSC
- [ ] URL principal indexada

---

## 🆘 TROUBLESHOOTING COMÚN

### Las imágenes no cargan
**Solución**: Verifica que todas las imágenes estén en `/public_html/` (raíz).
```bash
ls -la public_html/*.png
ls -la public_html/*.jpg
```

### El formulario no envía correos
**Solución**: Cambia `info@nanonex.es` en form action a un email verificado.
```html
<form action="https://formsubmit.co/TU_EMAIL_VERIFICADO@email.com">
```

### .htaccess no funciona (Error 500)
**Solución**: El servidor no tiene `mod_rewrite` habilitado.
Contacta a tu hosting: "Necesito mod_rewrite y mod_deflate habilitados".

### Logo roto en subdirectorios
**Solución**: Usar rutas relativas (`./Logo`) en lugar de absolutas (`/Logo`).
✅ Ya incluido en index_v2.html

### Error 404 no personalizado
**Solución**: Asegúrate de que el .htaccess contiene:
```apache
ErrorDocument 404 /404.html
```

---

## 📞 CONTACTO PARA AYUDA

Si tienes dudas durante la implementación:

- **Email**: info@nanonex.es
- **Teléfono**: 632 107 272
- **Horario**: L-V 07:00-22:00, Sáb-Dom 08:00-16:00

---

## 📚 REFERENCIAS Y RECURSOS

- **Google Search Console**: https://search.google.com/search-console
- **Schema.org Validator**: https://schema.org/validate
- **SEO Best Practices**: https://developers.google.com/search
- **Mobile Testing**: https://search.google.com/test/mobile-friendly

---

**Documento generado**: Mayo 31, 2026
**Versión**: 2.0
**Estado**: Listo para implementación
