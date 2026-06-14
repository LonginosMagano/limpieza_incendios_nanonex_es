/**
 * SEO Rotator - Función para rotar títulos y descriptions únicos
 * Basado en hash(slug) % 15 para evitar duplicados
 */

// PLANTILLAS DE TÍTULOS - 15 Variaciones
const TITLE_TEMPLATES = [
  "Limpieza de incendios en {ciudad} | Urgencias 24/7 | Nano Nex",                    // 0
  "Servicio urgente limpieza post incendio {ciudad} | Disponibles ahora",             // 1
  "{Ciudad}: Limpieza incendios emergencia 24/7 | Presupuesto gratis",               // 2
  "Limpieza urgente tras incendio {ciudad} | Especialistas Nano Nex",                // 3
  "¿Incendio? Limpieza profesional en {ciudad} | 24/7 disponibles",                  // 4
  "Hollín en {ciudad}? Limpieza profesional post incendio | Garantizado",            // 5
  "Olor a humo {ciudad} - Eliminación 100% | Limpieza incendios",                    // 6
  "Casa quemada {ciudad}? Limpieza y descontaminación completa",                     // 7
  "Limpieza post incendio {ciudad} | Humo, hollín, olores eliminados",               // 8
  "Después de incendio {ciudad} | Limpieza integral profesional",                    // 9
  "Limpieza incendios {ciudad} | 30 años experiencia | Nano Nex",                    // 10
  "{Ciudad}: Expertos limpieza post incendio - Técnica láser + ozono",               // 11
  "Limpieza post incendio {ciudad} | Certificados ITEL | Garantía",                 // 12
  "Limpiar hollín en {ciudad} | Profesionales especializados",                       // 13
  "Limpieza incendios {ciudad} | Desde 1994 | Confianza garantizada"                // 14
];

// PLANTILLAS DE META DESCRIPTIONS - 15 Variaciones
const DESCRIPTION_TEMPLATES = [
  "Limpieza profesional tras incendio en {ciudad}. Eliminamos hollín, humo y olores. Presupuesto sin compromiso. Disponibles 24/7.",                           // 0
  "{Ciudad}: Especialistas en limpieza post incendio. Descontaminación completa de viviendas y locales. Garantía de resultado. Disponibles 24/7.",           // 1
  "Incendio en {ciudad}? Limpieza urgente profesional. Eliminamos humo y hollín. Informes para seguros. Presupuesto gratis. Llamar 24/7.",                  // 2
  "Limpieza post incendio en {ciudad} | Técnica láser + ozono. Resultado garantizado. Sin molestias. Presupuesto cerrado. Llamar ahora.",                   // 3
  "Tras incendio en {ciudad}? Somos especialistas. Limpieza profunda, eliminación olores, desinfección. Urgencias 24/7. Presupuesto gratis.",              // 4
  "Especialistas limpieza incendios {ciudad}. Hollín, humo, olores eliminados. Equipos profesionales. 30 años experiencia. Garantía total.",                // 5
  "Limpieza post incendio {ciudad} | Descontaminación técnica. Láser, hielo seco, ozono. Certificados. Informes para seguros. Presupuesto gratis.",       // 6
  "{Ciudad}: Limpieza exhaustiva tras incendio. Viviendas, locales, naves. Sin reformas, solo limpieza. Llamar 24/7. Disponible hoy.",                    // 7
  "Hollín y humo en {ciudad}? Limpieza profesional garantizada. Protocolos certificados. Equipos modernos. Presupuesto sin compromiso.",                    // 8
  "Incendio {ciudad} | Limpieza especializada post siniestro. Eliminamos daño de humo. Informe para seguros. Urgencias 24/7.",                             // 9
  "{Ciudad}: Limpieza de incendios en viviendas. Apartamentos, chalets, estudios. Rápido, limpio, discreto. Presupuesto gratis. Llamar ahora.",           // 10
  "Limpieza incendios comercios {ciudad}. Restaurantes, oficinas, tiendas. Reabierto rápido. Presupuesto sin compromiso. 24/7.",                         // 11
  "{Ciudad}: Limpieza post incendio vivienda unifamiliar. Protegemos tus muebles. Presupuesto detallado. Garantía de resultado.",                        // 12
  "Limpieza urgente incendios {ciudad} | Edificios antiguos especializados. Respeto por detalles. Presupuesto gratis. Llamar 24/7.",                     // 13
  "Limpieza post incendio {ciudad} | Naves, garajes, almacenes. Áreas grandes sin problema. Presupuesto sin compromiso. Disponibles ya."                  // 14
];

/**
 * Calcula un hash simple a partir de un string
 * @param {string} str - El string a hashear (slug)
 * @returns {number} - Hash numérico
 */
function hashSlug(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash += str.charCodeAt(i);
  }
  return hash;
}

/**
 * Obtiene la plantilla de título rotativa basada en el slug
 * @param {string} slug - El slug de la página (ej: 'madrid-carabanchel')
 * @param {string} ciudad - El nombre de la ciudad a insertar
 * @returns {string} - El título formateado
 */
function getRotatingTitle(slug, ciudad) {
  const hash = hashSlug(slug);
  const index = hash % TITLE_TEMPLATES.length;
  const template = TITLE_TEMPLATES[index];

  // Reemplazar placeholders
  return template
    .replace(/{ciudad}/g, ciudad.toLowerCase())
    .replace(/{Ciudad}/g, ciudad.charAt(0).toUpperCase() + ciudad.slice(1).toLowerCase());
}

/**
 * Obtiene la plantilla de description rotativa basada en el slug
 * @param {string} slug - El slug de la página (ej: 'madrid-carabanchel')
 * @param {string} ciudad - El nombre de la ciudad a insertar
 * @returns {string} - La description formateada
 */
function getRotatingDescription(slug, ciudad) {
  const hash = hashSlug(slug);
  const index = hash % DESCRIPTION_TEMPLATES.length;
  const template = DESCRIPTION_TEMPLATES[index];

  // Reemplazar placeholders
  return template
    .replace(/{ciudad}/g, ciudad.toLowerCase())
    .replace(/{Ciudad}/g, ciudad.charAt(0).toUpperCase() + ciudad.slice(1).toLowerCase());
}

/**
 * Pruebas de rotación
 */
function testRotation() {
  const testCases = [
    { slug: 'madrid-carabanchel', ciudad: 'Carabanchel' },
    { slug: 'madrid-chamberi', ciudad: 'Chamberí' },
    { slug: 'madrid-hortaleza', ciudad: 'Hortaleza' },
    { slug: 'madrid-retiro', ciudad: 'Retiro' },
    { slug: 'madrid-salamanca', ciudad: 'Salamanca' },
    { slug: 'alcala-de-henares', ciudad: 'Alcalá de Henares' },
    { slug: 'alcobendas', ciudad: 'Alcobendas' },
    { slug: 'alcorcon', ciudad: 'Alcorcón' },
    { slug: 'getafe', ciudad: 'Getafe' },
    { slug: 'leganes', ciudad: 'Leganés' },
    { slug: 'mostoles', ciudad: 'Móstoles' },
    { slug: 'tres-cantos', ciudad: 'Tres Cantos' }
  ];

  console.log('=== PRUEBAS DE ROTACIÓN SEO ===\n');
  testCases.forEach(test => {
    const hash = hashSlug(test.slug);
    const titleIndex = hash % TITLE_TEMPLATES.length;
    const descIndex = hash % DESCRIPTION_TEMPLATES.length;

    console.log(`Slug: ${test.slug}`);
    console.log(`Hash: ${hash} -> Índice Title: ${titleIndex}, Description: ${descIndex}`);
    console.log(`Título: ${getRotatingTitle(test.slug, test.ciudad)}`);
    console.log(`Description: ${getRotatingDescription(test.slug, test.ciudad)}`);
    console.log('---\n');
  });
}

// Exportar para uso en Node.js o navegador
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    hashSlug,
    getRotatingTitle,
    getRotatingDescription,
    testRotation,
    TITLE_TEMPLATES,
    DESCRIPTION_TEMPLATES
  };
}

// Ejecutar pruebas si se llama directamente
if (require.main === module) {
  testRotation();
}
