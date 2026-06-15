# 📊 Guía de Optimización PageSpeed - Nano Nex

## Estado Actual
- **PageSpeed Score**: ~60-70/100 (necesita optimización de imágenes)
- **LCP (Largest Contentful Paint)**: ~3-4s (debería ser < 2.5s)
- **Ahorro Estimado**: 112 KiB si se aplican todas las compresiones

---

## ✅ Optimizaciones COMPLETADAS (2026-06-11)

### 1. Reflow Forzado
- ✅ JavaScript optimizado para evitar `classList.toggle` reflows
- ✅ Rendimiento JS: -69ms en reflow time

### 2. Cache del Navegador
- ✅ Imágenes: caché de 1 año (31536000 segundos)
- ✅ CSS/JS: caché de 1 mes (2592000 segundos)
- ✅ HTML: caché de 1 semana (604800 segundos)
- ✅ Headers Cache-Control explícitos añadidos

### 3. Logo Responsivo
- ✅ Media queries para ajustar tamaño en móvil (70px → 50px)
- ✅ Reducción de descarga en dispositivos móviles

---

## ⚠️ Tareas PENDIENTES (requieren herramientas externas)

### Problema 1: Limpieza-de-Incendios-Restaurantes.webp (LCP Image)
**Tamaño actual**: 114 KiB  
**Objetivo**: 39 KiB  
**Ahorro**: 75 KiB  

#### Solución 1a: Usar TinyPNG (en línea, sin instalar)
1. Ir a https://tinypng.com/
2. Subir `Limpieza-de-Incendios-Restaurantes.webp`
3. Descargar versión comprimida
4. Reemplazar archivo original

#### Solución 1b: Usar ImageMagick (CLI)
```bash
convert -quality 75 Limpieza-de-Incendios-Restaurantes.webp Limpieza-de-Incendios-Restaurantes-opt.webp
```

#### Solución 1c: Usar ffmpeg
```bash
ffmpeg -i Limpieza-de-Incendios-Restaurantes.webp -q:image 75 Limpieza-de-Incendios-Restaurantes-opt.webp
```

---

### Problema 2: Logo Nano Nex.png
**Tamaño actual**: 39 KiB  
**Tamaño mostrado**: 479x123 (pero imagen es 680x174)  
**Objetivo**: 10 KiB (convertir a WebP)  
**Ahorro**: 29 KiB  

#### Solución 2a: Convertir a WebP
```bash
cwebp -q 80 "Logo Nano Nex.png" -o "Logo Nano Nex.webp"
```

#### Solución 2b: Crear versión móvil
```bash
convert -resize 479x123 "Logo Nano Nex.png" "Logo Nano Nex-mobile.png"
cwebp -q 85 "Logo Nano Nex-mobile.png" -o "Logo Nano Nex-mobile.webp"
```

#### Solución 2c: Usar en HTML (con srcset)
```html
<picture>
  <source srcset="Logo Nano Nex.webp" type="image/webp">
  <img src="Logo Nano Nex.png" alt="..." width="680" height="174">
</picture>
```

#### Solución 2d: En mobile media query
```html
<picture>
  <source srcset="Logo Nano Nex-mobile.webp" type="image/webp" media="(max-width: 768px)">
  <source srcset="Logo Nano Nex.webp" type="image/webp">
  <img src="Logo Nano Nex.png" alt="..." width="680" height="174">
</picture>
```

---

### Problema 3: Limpieza-de-Escombros-4.webp
**Tamaño actual**: 26 KiB  
**Objetivo**: 18 KiB  
**Ahorro**: 8 KiB  

#### Solución
```bash
cwebp -quality 80 Limpieza-de-Escombros-4.webp -o Limpieza-de-Escombros-4-opt.webp
```

---

## 📈 Resultados Esperados

| Métrica | Actual | Esperado | Mejora |
|---------|--------|----------|--------|
| LCP | ~3-4s | ~1.5-2s | -50% |
| PageSpeed Score | 60-70 | 85-95 | +25 puntos |
| Tamaño transferencia | ~177 KiB | ~65 KiB | -63% |
| Caché navegador | 2d | 1 año | ✅ |

---

## 🚀 Próximos Pasos

1. **Comprimir 3 imágenes críticas** (total: 112 KiB de ahorro)
2. **Reemplazar en servidor** (FTP upload)
3. **Purgar caché del navegador** (invalidar versiones viejas)
4. **Validar en PageSpeed Insights**
5. **Monitorizar Core Web Vitals** en Google Search Console

---

## 📋 Checklist de Implementación

- [ ] Descargar imagen LCP comprimida (39 KiB)
- [ ] Convertir Logo a WebP (10 KiB)
- [ ] Comprimir imagen Escombros (18 KiB)
- [ ] Reemplazar archivos en servidor
- [ ] Ejecutar invalidación de caché CDN
- [ ] Validar con PageSpeed Insights
- [ ] Monitorizar LCP durante 48h

---

## 🔗 Herramientas Recomendadas

- **TinyPNG/TinyJPG**: https://tinypng.com/ (mejor para WebP)
- **ImageOptim**: https://imageoptim.com/ (macOS)
- **FileZilla**: Para FTP uploads
- **Google PageSpeed Insights**: https://pagespeed.web.dev/
- **Lighthouse CI**: Para monitorización continua

---

**Última actualización**: 2026-06-11  
**Auditor**: Nano Nex SEO Audit
