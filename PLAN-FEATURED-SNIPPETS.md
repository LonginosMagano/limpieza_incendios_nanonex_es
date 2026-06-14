# 🎯 PLAN FEATURED SNIPPETS - Ciclo 6

## OBJETIVO
Optimizar artículos para aparecer en fragmentos destacados de Google.

**Beneficio**: 
- +30% CTR cuando aparece en snippet
- Posición 0 en resultados
- Tráfico cualificado garantizado

---

## ESTRUCTURA PARA FRAGMENTOS DESTACADOS

Google busca responder preguntas directas. Estructura requerida:

### TIPO 1: PÁRRAFO (40-60 palabras)
```html
<div class="respuesta-rapida">
  <strong>Respuesta rápida:</strong>
  <p>
    [Respuesta directa y concisa en 40-60 palabras que 
    responda exactamente la pregunta del H1]
  </p>
</div>
```

**Ejemplo**:
```html
<h1>¿Cómo eliminar olor a humo en casa?</h1>
<div class="respuesta-rapida">
  <strong>Respuesta rápida:</strong>
  <p>El olor a humo penetra a nivel molecular en paredes y textiles. 
  La solución definitiva es ozono profesional que destruye la molécula 
  de humo, no solo la enmascara. Combinado con aireación, se elimina 
  completamente en 3-7 días.</p>
</div>
```

---

### TIPO 2: LISTA NUMERADA (Cómo se hace)
```html
<h2>¿Cómo limpiar hollín de paredes?</h2>

<ol class="snippet-list">
  <li>
    <strong>Paso 1:</strong> 
    [Primera acción concisa]
  </li>
  <li>
    <strong>Paso 2:</strong> 
    [Segunda acción]
  </li>
  <!-- 3-6 pasos total -->
</ol>
```

**Ejemplo**:
```html
<ol class="snippet-list">
  <li><strong>Preparación:</strong> Vacía la habitación, cubre muebles.</li>
  <li><strong>Evaluación:</strong> Determina si es hollín o solo polvo.</li>
  <li><strong>Limpieza:</strong> Con trapo húmedo, nunca en seco (dispersa).</li>
  <li><strong>Tratamiento:</strong> Aplicar limpiador neutro si está muy negro.</li>
  <li><strong>Finalización:</strong> Ventila y deja secar.</li>
  <li><strong>Profesional:</strong> Si cubre >50% paredes, llama a especialistas.</li>
</ol>
```

---

### TIPO 3: TABLA (Comparativas)
```html
<h2>Métodos de limpieza: Ventajas y desventajas</h2>

<table class="comparison-table">
  <thead>
    <tr>
      <th>Método</th>
      <th>Tiempo</th>
      <th>Costo</th>
      <th>Riesgo Daño</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DIY (Trapo húmedo)</td>
      <td>3-5 días</td>
      <td>€</td>
      <td>Medio (si frotás fuerte)</td>
    </tr>
    <tr>
      <td>Profesional (Láser)</td>
      <td>1-2 días</td>
      <td>€€€</td>
      <td>Muy bajo</td>
    </tr>
    <tr>
      <td>Profesional (Ozono)</td>
      <td>3-7 días</td>
      <td>€€</td>
      <td>Muy bajo</td>
    </tr>
  </tbody>
</table>
```

---

### TIPO 4: LISTA CON BULLETS (Qué incluye)
```html
<h2>¿Qué incluye una limpieza post incendio profesional?</h2>

<ul class="snippet-list">
  <li>Evaluación gratuita de daños</li>
  <li>Eliminación de hollín de paredes y techos</li>
  <li>Limpieza de conductos de aire</li>
  <li>Tratamiento con ozono</li>
  <li>Desinfección completa</li>
  <li>Informe detallado para seguros</li>
</ul>
```

---

## ARTÍCULOS PRIORITARIOS (6 total)

### 1. **como-eliminar-olor-a-humo-en-casa.html**
- **Tipo**: PÁRRAFO + TABLA
- **H1**: ¿Cómo eliminar olor a humo en casa?
- **Párrafo rápido**: 50 palabras (CRÍTICO)
- **Tabla**: Métodos vs. Tiempo vs. Costo
- **Keyword**: "olor a humo"

### 2. **que-hacer-despues-de-un-incendio.html**
- **Tipo**: LISTA NUMERADA
- **H1**: ¿Qué hacer después de un incendio?
- **Pasos**: 6-8 pasos ordenados
- **Keyword**: "después de incendio"

### 3. **como-limpiar-el-hollin-de-paredes-y-techos.html**
- **Tipo**: LISTA NUMERADA + TABLA
- **H1**: ¿Cómo limpiar hollín de paredes?
- **Pasos**: 5-6 pasos detallados
- **Tabla**: DIY vs. Profesional
- **Keyword**: "limpiar hollín"

### 4. **el-seguro-cubre-la-limpieza-tras-un-incendio.html**
- **Tipo**: PÁRRAFO + BULLETS
- **H1**: ¿El seguro cubre la limpieza después de un incendio?
- **Párrafo rápido**: Sí/No respuesta clara
- **Bullets**: Qué está cubierto
- **Keyword**: "seguro incendio limpieza"

### 5. **como-reclamar-al-seguro-tras-un-incendio.html**
- **Tipo**: LISTA NUMERADA
- **H1**: ¿Cómo reclamar al seguro tras un incendio?
- **Pasos**: 6-7 pasos legales
- **Keyword**: "reclamar seguro incendio"

### 6. **documentos-para-reclamar-al-seguro-tras-un-incendio.html**
- **Tipo**: LISTA CON BULLETS
- **H1**: ¿Qué documentos necesito para reclamar al seguro?
- **Bullets**: Listado de documentos requeridos
- **Keyword**: "documentos seguro incendio"

---

## SCHEMA JSON-LD

Agregar a artículos "Cómo se hace":

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "¿Cómo limpiar hollín de paredes?",
  "description": "Guía paso a paso para limpiar hollín de paredes tras un incendio",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Paso 1: Preparación",
      "text": "Vacía la habitación y cubre muebles con plástico.",
      "image": "imagen-paso1.webp"
    },
    {
      "@type": "HowToStep",
      "name": "Paso 2: Evaluación",
      "text": "Determina si es hollín fino o capa gruesa.",
      "image": "imagen-paso2.webp"
    }
    // ... más pasos
  ]
}
</script>
```

---

## CHECKLIST DE SNIPPETS

Para cada artículo:
- [ ] ¿Tiene "Respuesta rápida" (40-60 palabras)?
- [ ] ¿La respuesta es DIRECTA a la pregunta?
- [ ] ¿Tiene estructura (tabla/lista/pasos)?
- [ ] ¿Máximo 6 items por lista?
- [ ] ¿Máximo 6 columnas en tabla?
- [ ] ¿Tiene schema JSON-LD correcto?
- [ ] ¿Los <strong> resaltan palabras clave?
- [ ] ¿El HTML es válido?

---

## EJEMPLO COMPLETO

**Archivo**: como-limpiar-el-hollin-de-paredes-y-techos.html

```html
<h1>¿Cómo limpiar hollín de paredes y techos?</h1>

<!-- RESPUESTA RÁPIDA -->
<div class="respuesta-rapida">
  <strong>Respuesta rápida:</strong>
  <p>El hollín requiere limpieza delicada con trapo húmedo, 
  nunca en seco. Para áreas grandes o paredes valiosas, 
  profesionales usan láser o vapor. Importante: el hollín 
  es tóxico, así que protégete o llama a especialistas.</p>
</div>

<!-- PASOS -->
<h2>Pasos para limpiar hollín</h2>
<ol class="snippet-list">
  <li><strong>Preparación:</strong> Vacía la habitación...</li>
  <li><strong>Evaluación:</strong> Determina la densidad...</li>
  <!-- más pasos -->
</ol>

<!-- TABLA COMPARATIVA -->
<h2>Métodos: DIY vs. Profesional</h2>
<table class="comparison-table">
  <!-- tabla -->
</table>

<!-- SCHEMA HowTo -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "¿Cómo limpiar hollín de paredes y techos?",
  "step": [...]
}
</script>
```

---

## VALIDACIÓN EN GOOGLE

Para verificar si aparece en snippets:
```
site:limpiezaincendiosnanonex.es "¿Cómo limpiar hollín"
```

También:
- Busca la pregunta en Google
- Mira si aparece en posición 0
- Verifica que el texto coincida con el snippet

---

## PALABRAS CLAVE SNIPPET-READY

Artículos que DEBEN tener snippet:
- "¿Cómo..." (How-to)
- "¿Qué..." (Definition)
- "¿Cuál es..." (Comparison)
- "¿Dónde..." (Location)
- "¿Cuánto..." (Price)

Nuestros artículos cubren:
- ✅ ¿Cómo limpiar hollín? → Lista numerada
- ✅ ¿Qué hacer después incendio? → Pasos
- ✅ ¿El seguro cubre? → Sí/No
- ✅ ¿Cómo reclamar? → Pasos
- ✅ ¿Qué documentos? → Lista

---

Este plan se ejecutará en Ciclo 6.
