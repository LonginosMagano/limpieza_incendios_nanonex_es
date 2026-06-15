# 🎯 PLANTILLAS SEO - 15 Títulos y 15 Descriptions

## TÍTULOS - 15 Variaciones

### Grupo 1: Urgencia + Servicio
```
1. "Limpieza de incendios en {ciudad} | Urgencias 24/7 | Nano Nex"
2. "Servicio urgente limpieza post incendio {ciudad} | Disponibles ahora"
3. "{Ciudad}: Limpieza incendios emergencia 24/7 | Presupuesto gratis"
4. "Limpieza urgente tras incendio {ciudad} | Especialistas Nano Nex"
5. "¿Incendio? Limpieza profesional en {ciudad} | 24/7 disponibles"
```

### Grupo 2: Problema + Solución
```
6. "Hollín en {ciudad}? Limpieza profesional post incendio | Garantizado"
7. "Olor a humo {ciudad} - Eliminación 100% | Limpieza incendios"
8. "Casa quemada {ciudad}? Limpieza y descontaminación completa"
9. "Limpieza post incendio {ciudad} | Humo, hollín, olores eliminados"
10. "Después de incendio {ciudad} | Limpieza integral profesional"
```

### Grupo 3: Diferencial
```
11. "Limpieza incendios {ciudad} | 30 años experiencia | Nano Nex"
12. "{Ciudad}: Expertos limpieza post incendio - Técnica láser + ozono"
13. "Limpieza post incendio {ciudad} | Certificados ITEL | Garantía"
14. "Limpiar hollín en {ciudad} | Profesionales especializados"
15. "Limpieza incendios {ciudad} | Desde 1994 | Confianza garantizada"
```

---

## META DESCRIPTIONS - 15 Variaciones

### Grupo 1: Emocional + CTA
```
1. "Limpieza profesional tras incendio en {ciudad}. Eliminamos hollín, humo y olores definitivamente. ✓ Presupuesto sin compromiso. Llamar ahora."

2. "{Ciudad}: Especialistas en limpieza post incendio. Descontaminación completa de viviendas y locales. Garantía de resultado. Disponibles 24/7."

3. "Incendio en {ciudad}? Limpieza urgente profesional. Eliminamos humo y hollín. Informes para seguros. Presupuesto gratis. Llamar 24/7."

4. "Limpieza post incendio en {ciudad} | Técnica láser + ozono. Resultado garantizado. Sin molestias. Presupuesto cerrado. Llamar ahora."

5. "Après incendio {ciudad}? Somos especialistas. Limpieza profunda, eliminación olores, desinfección. Urgencias 24/7. Presupuesto gratis."
```

### Grupo 2: Técnico + Confianza
```
6. "Especialistas limpieza incendios {ciudad}. Hollín, humo, olores eliminados. Equipos profesionales. 30 años experiencia. Garantía total."

7. "Limpieza post incendio {ciudad} | Descontaminación técnica. Láser, hielo seco, ozono. Certificados. Informes para seguros. Presupuesto gratis."

8. "{Ciudad}: Limpieza exhaustiva tras incendio. Viviendas, locales, naves. Sin reformas, solo limpieza. Llamar 24/7. Disponible hoy."

9. "Hollín y humo en {ciudad}? Limpieza profesional garantizada. Protocolos certificados. Equipos modernos. Presupuesto sin compromiso."

10. "Incendio {ciudad} | Limpieza especializada post siniestro. Eliminamos daño de humo. Informe para seguros. Urgencias 24/7."
```

### Grupo 3: Particularizado por Zona
```
11. "{Ciudad}: Limpieza de incendios en viviendas. Apartamentos, chalets, estudios. Rápido, limpio, discreto. Presupuesto gratis. Llamar ahora."

12. "Limpieza incendios comercios {ciudad}. Restaurantes, oficinas, tiendas. Reabierto rápido. Presupuesto sin compromiso. 24/7."

13. "{Ciudad}: Limpieza post incendio vivienda unifamiliar. Protegemos tus muebles. Presupuesto detallado. Garantía de resultado."

14. "Limpieza urgente incendios {ciudad} | Edifios antiguos especializados. Respeto por detalles. Presupuesto gratis. Llamar 24/7."

15. "Limpieza post incendio {ciudad} | Naves, garajes, almacenes. Áreas grandes sin problema. Presupuesto sin compromiso. Disponibles ya."
```

---

## ESTRUCTURA DE ROTACIÓN (JavaScript)

```javascript
// Hashear slug y seleccionar plantilla
function getRotatingTitle(slug) {
  const templates = [
    // 15 templates aquí
  ];
  
  // hash del slug % 15 = índice
  const hash = slug.split('').reduce((h, c) => h + c.charCodeAt(0), 0);
  const index = hash % templates.length;
  return templates[index];
}

// Usar en landing:
const title = getRotatingTitle('madrid-carabanchel');
// Resultado: varía cada carga o según slug
```

---

## KEYWORDS PRINCIPALES

### Por Tipo de Landing

**Ciudades (Madrid, Barcelona, etc.):**
- Primary: "Limpieza de incendios en {ciudad}"
- Secondary: "Limpieza post incendio {ciudad}"
- Long-tail: "¿Dónde limpian después de incendio en {ciudad}?"

**Barrios (Carabanchel, Salamanca, etc.):**
- Primary: "Limpieza de incendios en {barrio}, {ciudad}"
- Secondary: "Hollín {barrio}"
- LSI: "Olor a humo {barrio}"

**Artículos (Blog):**
- Primary: Pregunta directa ("¿Cómo eliminar olor a humo?")
- Secondary: Long-tail ("Cómo limpiar hollín después incendio")
- LSI: Variantes ("Eliminar olor humo casa", "Limpiar hollín paredes")

---

## CHECKLIST SEO

Para cada página:
- [ ] Title: Keyword + {ciudad} + CTA
- [ ] Description: 150-160 caracteres, keyword al inicio
- [ ] H1: Keyword principal visible
- [ ] H2/H3: Subkeywords relacionadas
- [ ] No repetir entre páginas (usar rotación)
- [ ] URL slug legible (no números)
- [ ] Canonical tag correcto
- [ ] Schema LocalBusiness con ciudad

---

## EJEMPLO COMPLETO

**URL:** /limpieza-de-incendios-madrid-carabanchel.html

**Title (Plantilla 6):**
```
Limpieza incendios Carabanchel Madrid | 30 años experiencia | Nano Nex
```

**Meta Description (Plantilla 11):**
```
Carabanchel Madrid: Limpieza de incendios en viviendas. Apartamentos, chalets. 
Rápido, limpio, discreto. Presupuesto gratis. Llamar 24/7 disponibles.
```

**H1:**
```
Limpieza de Incendios en Carabanchel: Tu barrio, tu solución
```

**H2s:**
```
- Limpieza de hollín en viviendas de Carabanchel
- Eliminación de olor a humo sin molestas
- Presupuesto rápido sin compromiso
```

---

Este documento será usado en Ciclo 3 para generar los 15 títulos y descriptions únicos.
