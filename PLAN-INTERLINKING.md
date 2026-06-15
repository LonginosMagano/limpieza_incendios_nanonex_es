# 🔗 PLAN DE INTERLINKING - Ciclo 5

## OBJETIVO
Crear red de enlaces internos entre:
- Barrios de Madrid
- Ciudades principales
- Provincias
- Artículos relevantes

**Resultado**: Mayor SEO, mejor crawl budget, más pageviews internos.

---

## ESTRUCTURA DE INTERLINKING

### A. ENLACES DENTRO DE MADRID (7 barrios)

En cada barrio, agregar sección "También cubrimos":
```html
<section class="otros-barrios">
  <h3>También cubrimos otros barrios de Madrid</h3>
  <div class="links-grid">
    <a href="limpieza-de-incendios-madrid-retiro.html" class="link-btn">Retiro</a>
    <a href="limpieza-de-incendios-madrid-salamanca.html" class="link-btn">Salamanca</a>
    <!-- Más barrios -->
  </div>
</section>
```

**Distribución (cada barrio enlaza a 4-5 otros):**
- Carabanchel → Vallecas, Tetuán, Retiro, Salamanca
- Chamberí → Salamanca, Retiro, Hortaleza, Carabanchel
- Hortaleza → Chamberí, Tetuán, Salamanca, Carabanchel
- Retiro → Salamanca, Chamberí, Carabanchel, Vallecas
- Salamanca → Retiro, Chamberí, Hortaleza, Carabanchel
- Tetuán → Chamberí, Hortaleza, Carabanchel, Vallecas
- Vallecas → Carabanchel, Tetuán, Retiro, Salamanca

**Estilo CSS**: Cards terracota (#FF6B35) con flecha →

---

### B. ENLACES DESDE MADRID A CIUDADES CERCANAS

En madrid-main (o index de Madrid), agregar:
```html
<section class="municipios-cercanos">
  <h3>Limpieza de incendios en la región madrileña</h3>
  <div class="links-grid">
    <a href="limpieza-de-incendios-alcala-de-henares.html">Alcalá de Henares</a>
    <a href="limpieza-de-incendios-alcobendas.html">Alcobendas</a>
    <!-- 13 municipios más -->
  </div>
</section>
```

**Municipios Madrid (15 total)**:
1. Alcalá de Henares
2. Alcobendas
3. Alcorcón
4. Colmenar Viejo
5. Getafe
6. Leganés
7. Móstoles
8. Fuenlabrada
9. Torrejón de Ardoz
10. San Sebastián de los Reyes
11. Tres Cantos
12. Coslada
13. Rivas-Vaciamadrid
14. Pozuelo de Alarcón
15. Las Rozas

---

### C. ENLACES ENTRE CIUDADES DE OTRAS PROVINCIAS

Crear secciones "Otras ciudades donde actuamos":

**Barcelona (Cataluña)**:
- Links a: Valencia, Zaragoza, Tarragona, Lleida

**Valencia (C. Valenciana)**:
- Links a: Barcelona, Murcia, Albacete, Cuenca

**Sevilla (Andalucía)**:
- Links a: Córdoba, Málaga, Granada, Cádiz

**Málaga (Andalucía)**:
- Links a: Sevilla, Granada, Córdoba, Jaén

**Murcia (Región de Murcia)**:
- Links a: Almería, Valencia, Cuenca, Albacete

**Zaragoza (Aragón)**:
- Links a: Barcelona, Lleida, Teruel, Madrid

---

### D. SIDEBAR CON INTERLINKING CONTEXTUAL

En cada página:

```html
<aside class="sidebar">
  <!-- Sección 1: Barrios (si es Madrid) -->
  <div class="sidebar-block">
    <h4>Otros barrios de Madrid</h4>
    <ul>
      <li><a href="madrid-retiro.html">Retiro</a></li>
      <li><a href="madrid-salamanca.html">Salamanca</a></li>
      <!-- Max 4-5 links -->
    </ul>
  </div>

  <!-- Sección 2: Ciudades cercanas (por provincia) -->
  <div class="sidebar-block">
    <h4>Otras ciudades de la región</h4>
    <ul>
      <li><a href="limpieza-incendios-barcelona.html">Barcelona</a></li>
      <li><a href="limpieza-incendios-toledo.html">Toledo</a></li>
    </ul>
  </div>

  <!-- Sección 3: Artículos relacionados -->
  <div class="sidebar-block">
    <h4>Guías útiles</h4>
    <ul>
      <li><a href="que-hacer-despues-de-un-incendio.html">Qué hacer después de un incendio</a></li>
      <li><a href="como-eliminar-olor-a-humo.html">Cómo eliminar olor a humo</a></li>
    </ul>
  </div>
</aside>
```

---

### E. ENLACES CONTEXTUALES EN TEXTOS

Dentro del contenido, enlazar:
- Primera mención de palabra clave → página del servicio
- Referencia a ciudad cercana → landing de esa ciudad
- "Qué hacer después" → artículo de blog
- Mencionada garantía → página de garantías (si existe)

**EJEMPLO**:
```html
<p>
  Aquí en Carabanchel el <a href="limpieza-de-incendios-madrid-retiro.html">Retiro</a>
  es nuestro vecino, y en ambos barrios sabemos que...
</p>
```

---

## ESTRUCTURA DE TABLA DE INTERLINKING

| Página | Enlaces Salientes | Enlaces Internos | Tipo |
|--------|------------------|------------------|------|
| Madrid-Carabanchel | 4 barrios | Sidebar | Barrio |
| Madrid-Retiro | 4 barrios + 5 ciudades | Sidebar | Barrio |
| Barcelona | 4 ciudades | Sidebar | Ciudad |
| Valencia | 3 ciudades | Sidebar | Ciudad |
| Blog: Qué hacer | 3 servicios | Inline | Artículo |

---

## VALIDACIÓN DE INTERLINKING

Checklist por página:
- [ ] ¿Tiene enlaces a barrios/ciudades cercanas?
- [ ] ¿Los enlaces son contextuales (no random)?
- [ ] ¿Máximo 5-6 enlaces por sección?
- [ ] ¿Todos los links funcionan (href correcto)?
- [ ] ¿El anchor text es descriptivo?
- [ ] ¿No hay enlaces rotos (404)?

---

## DISTRIBUCIÓN DE LINK JUICE

**Prioridad baja-media** (no critique):
- "Otros barrios" = 10% del page authority

**Prioridad media** (distribuir mejor):
- Artículos blog = 30% link juice

**Prioridad alta** (proteger)**:
- Home + Ciudades principales = 60% link juice

---

## PRÓXIMAS FASES

### Fase 2: Crear páginas faltantes
- Barcelona + 5 barrios (Eixample, Gràcia, Sarrià, Montjuïc, Horta)
- Valencia + 3 barrios
- Sevilla, Málaga
- Otras ciudades provincias

### Fase 3: Breadcrumbs estructurados
```html
Home > Madrid > Carabanchel > Limpieza Post Incendio
```

### Fase 4: Mapa de sitio dinámico
- `/sitemap.html` visible para usuarios
- `/sitemap.xml` para buscadores

---

## HERRAMIENTA: VALIDAR ENLACES

Script para encontrar enlaces rotos:
```bash
# Verificar que archivos existen
grep -rho 'href="[^"]*\.html"' . | sed 's/href="//g' | sed 's/"//g' | sort -u | while read file; do
  if [ ! -f "$file" ]; then
    echo "❌ Enlace roto: $file"
  fi
done
```

---

Este plan ejecutará Ciclo 5 de forma ordenada y medible.
