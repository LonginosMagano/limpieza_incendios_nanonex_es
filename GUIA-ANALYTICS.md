# 📊 GUÍA DE CONFIGURACIÓN: Monitoreo & Analytics
## Nano Nex - Limpieza de Incendios Madrid

---

## 1️⃣ GOOGLE ANALYTICS 4 (GA4)

### Paso 1: Crear propiedad en Google Analytics
1. Accede a: https://analytics.google.com
2. Haz clic en "Administración" (esquina inferior izquierda)
3. Selecciona "Crear propiedad"
4. Nombre: `Nano Nex - Limpieza Incendios`
5. Zona horaria: `(UTC +01:00) Madrid`
6. Moneda: `EUR`
7. Haz clic en "Crear"

### Paso 2: Obtener ID de medición (G-XXXXXX)
1. En la nueva propiedad, haz clic en "Flujos de datos"
2. Selecciona tu sitio web
3. Copia el ID de medición (formato: G-XXXXXX)

### Paso 3: Agregar script a todas las páginas HTML
Inserta este código en el `<head>` de index.html y las demás páginas principales:

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXX');
</script>
```

**⚠️ IMPORTANTE:** Reemplaza `G-XXXXXX` con tu ID real de medición.

### Paso 4: Configurar eventos personalizados (Opcional pero recomendado)

Agrega este código antes del cierre de `</body>`:

```html
<script>
// Rastrear clics en botones CTA
document.querySelectorAll('.cta-btn').forEach(btn => {
  btn.addEventListener('click', function(e) {
    const text = this.textContent.trim();
    gtag('event', 'cta_click', {
      'button_text': text,
      'page_title': document.title
    });
  });
});

// Rastrear envíos de formulario
document.getElementById('my-form')?.addEventListener('submit', function() {
  gtag('event', 'form_submission', {
    'form_type': 'presupuesto',
    'origin': this.querySelector('input[name="Origen"]').value
  });
});

// Rastrear clics en teléfono
document.querySelectorAll('a[href^="tel:"]').forEach(link => {
  link.addEventListener('click', function() {
    gtag('event', 'phone_click', {
      'phone_number': this.href.replace('tel:', '')
    });
  });
});
</script>
```

---

## 2️⃣ GOOGLE SEARCH CONSOLE (GSC)

### Paso 1: Verificar sitio en GSC
1. Accede a: https://search.google.com/search-console
2. Haz clic en "Añadir propiedad"
3. Selecciona "Prefijo de URL"
4. Escribe: `https://limpiezadeincendios-nanonex.es/`
5. Haz clic en "Continuar"

### Paso 2: Elegir método de verificación
**Método recomendado: Etiqueta META HTML**

1. Google te proporcionará un código como:
   ```html
   <meta name="google-site-verification" content="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" />
   ```

2. Copia este código
3. Pégalo en el `<head>` de index.html (entre `<title>` y otros `<meta>`)
4. Vuelve a GSC y haz clic en "Verificar"

### Paso 3: Enviar Sitemap
1. En GSC, ve a "Sitemaps" (menú izquierdo)
2. En "Nueva entrada de Sitemap", escribe:
   ```
   sitemap.xml
   ```
3. Haz clic en "Enviar"

### Paso 4: Configurar propiedades
1. Ve a "Configuración" (menú izquierdo)
2. Aceptar "Informe de cobertura de índice"
3. Habilitar "Solicitar indexación"

---

## 3️⃣ KEYWORDS A MONITOREAR

### Tier 1 (Palabras clave principales)
- `limpieza de incendios madrid` - Alta intención de compra
- `limpieza post incendio` - Urgencia
- `eliminación de hollín madrid` - Específico
- `limpieza de humo` - Descriptivo

### Tier 2 (Por localidad)
- `limpieza incendios [ciudad]` para cada una de las 11 regionales
- `post incendio [barrio]` para zonas de cobertura

### Tier 3 (Términos secundarios)
- `limpieza comercial madrid`
- `desinfección profesional`
- `eliminación de olores`

### Monitoreo mensual (Google Sheets)
Crear una hoja con:
```
Keyword | GSC Position | GSC Clicks | GSC Impresiones | CTR | Cambio mes anterior
```

---

## 4️⃣ DASHBOARD DE KPIs

### Métricas principales (revisar mensualmente)
1. **Tráfico orgánico total**
   - Meta: 500+ sesiones/mes en 3 meses

2. **Posición media en búsqueda (GSC)**
   - Meta: Top 10 para palabras principales

3. **Impresiones en búsqueda (GSC)**
   - Meta: 5,000+ impresiones/mes

4. **Click-through rate (CTR)**
   - Meta: >3% para palabras principales

5. **Sesiones por fuente**
   - Orgánico vs. Directo vs. Social

6. **Conversiones (formularios + llamadas)**
   - Presupuestos solicitados
   - Llamadas desde GA

7. **Tasa de rebote (Bounce Rate)**
   - Meta: <50% para landing pages

8. **Páginas por sesión**
   - Meta: >2 páginas por sesión

### Objetivos de GA4 recomendados
- Envío de formulario
- Clic en teléfono
- Clic en WhatsApp
- Duración de sesión >30s

---

## 5️⃣ ALERTAS Y MONITOREO

### Alertas automáticas en GSC
1. Ve a "Configuración"
2. Configura alertas para:
   - Errores de rastreo (crítico)
   - Nuevos problemas de seguridad
   - Cambios en la cobertura del índice

### Monitoreo semanal manual
- Revisar tráfico en GA4
- Verificar posiciones en GSC
- Revisar errores en consola

### Monitoreo mensual detallado
- Crear reporte de keywords
- Analizar comportamiento de usuarios
- Revisar conversiones
- Ajustar estrategia

---

## 6️⃣ HERRAMIENTAS COMPLEMENTARIAS (Opcionales)

### Rastreo de posiciones (Rank Tracker)
- **Opción gratuita:** Rank Ranger (5 keywords)
- **Opción premium:** SEMrush, Ahrefs

### Análisis de competencia
- Busca competidores en Google
- Revisa sus keywords en SEMrush
- Analiza su estructura de enlaces

### Auditoría técnica
- ScreamingFrog (análisis de errores 404, redirects)
- Google PageSpeed Insights (Core Web Vitals)

---

## 7️⃣ CALENDARIO DE ACCIONES

### Semana 1
- ✅ Instalar GA4 y verificar en GSC
- ✅ Crear lista de keywords a monitorear
- ✅ Configurar objetivos en GA4

### Semana 2-4
- ✅ Recopilar datos iniciales
- ✅ Crear dashboard en Google Sheets
- ✅ Primera revisión de posiciones

### Mes 2-3
- ✅ Analizar tendencias
- ✅ Optimizar keywords con bajo CTR
- ✅ Crear más contenido para keywords relevantes

### Mes 4+
- ✅ Ajustar estrategia basado en datos
- ✅ Expandir a nuevas palabras clave
- ✅ Optimizar conversiones

---

## 📈 MÉTRICAS DE ÉXITO (3 MESES)

| Métrica | Objetivo | Realista |
|---------|----------|----------|
| Sesiones orgánicas | 500+ | ✅ |
| Posición promedio (Top 10) | 15+ keywords | ✅ |
| Impresiones búsqueda | 5,000+/mes | ✅ |
| CTR promedio | >2.5% | ✅ |
| Presupuestos solicitados | 5+ /mes | ✅ |
| Llamadas telefónicas | 10+ /mes | ✅ |

---

## ⚠️ NOTAS IMPORTANTES

1. **Privacidad:** Avisa a usuarios sobre GA4 en tu política de privacidad
2. **GDPR:** En EU, obtén consentimiento para cookies antes de GA4
3. **Tiempo:** Los datos toman 48h en aparecer en GA4
4. **Verificación GSC:** Puede tomar 24-48h verificar el sitio

---

## 📞 CONTACTO Y SOPORTE

Para preguntas sobre implementación:
1. Documentación de GA4: https://support.google.com/analytics
2. Ayuda de GSC: https://support.google.com/webmasters
3. Comunidad: https://www.reddit.com/r/SEO/

---

**Última actualización:** 2026-06-14
**Estado:** Listo para implementación
