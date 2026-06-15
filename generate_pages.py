#!/usr/bin/env python3
"""
Generate 19 landing pages for fire cleaning service in Spanish cities.
"""

import json
import os

# SEO title and description templates for rotation
SEO_TITLES = [
    "Limpieza de incendios en {ciudad} | Urgencias 24/7 | Nano Nex",
    "Servicio urgente limpieza post incendio {ciudad} | Disponibles ahora",
    "{ciudad}: Limpieza incendios emergencia 24/7 | Presupuesto gratis",
    "Limpieza urgente tras incendio {ciudad} | Especialistas Nano Nex",
    "¿Incendio? Limpieza profesional en {ciudad} | 24/7 disponibles",
    "Hollín en {ciudad}? Limpieza profesional post incendio | Garantizado",
    "Olor a humo {ciudad} - Eliminación 100% | Limpieza incendios",
    "Casa quemada {ciudad}? Limpieza y descontaminación completa",
    "Limpieza post incendio {ciudad} | Humo, hollín, olores eliminados",
    "Después de incendio {ciudad} | Limpieza integral profesional",
    "Limpieza incendios {ciudad} | 30 años experiencia | Nano Nex",
    "{ciudad}: Expertos limpieza post incendio - Técnica láser + ozono",
    "Limpieza post incendio {ciudad} | Certificados ITEL | Garantía",
    "Limpiar hollín en {ciudad} | Profesionales especializados",
    "Limpieza incendios {ciudad} | Desde 1994 | Confianza garantizada",
]

SEO_DESCRIPTIONS = [
    "Limpieza profesional tras incendio en {ciudad}. Eliminamos hollín, humo y olores definitivamente. Presupuesto sin compromiso. Llamar ahora.",
    "{ciudad}: Especialistas en limpieza post incendio. Descontaminación completa de viviendas y locales. Garantía de resultado. Disponibles 24/7.",
    "Incendio en {ciudad}? Limpieza urgente profesional. Eliminamos humo y hollín. Informes para seguros. Presupuesto gratis. Llamar 24/7.",
    "Limpieza post incendio en {ciudad} | Técnica láser + ozono. Resultado garantizado. Sin molestias. Presupuesto cerrado. Llamar ahora.",
    "Après incendio {ciudad}? Somos especialistas. Limpieza profunda, eliminación olores, desinfección. Urgencias 24/7. Presupuesto gratis.",
    "Especialistas limpieza incendios {ciudad}. Hollín, humo, olores eliminados. Equipos profesionales. 30 años experiencia. Garantía total.",
    "Limpieza post incendio {ciudad} | Descontaminación técnica. Láser, hielo seco, ozono. Certificados. Informes para seguros. Presupuesto gratis.",
    "{ciudad}: Limpieza exhaustiva tras incendio. Viviendas, locales, naves. Sin reformas, solo limpieza. Llamar 24/7. Disponible hoy.",
    "Hollín y humo en {ciudad}? Limpieza profesional garantizada. Protocolos certificados. Equipos modernos. Presupuesto sin compromiso.",
    "Incendio {ciudad} | Limpieza especializada post siniestro. Eliminamos daño de humo. Informe para seguros. Urgencias 24/7.",
    "{ciudad}: Limpieza de incendios en viviendas. Apartamentos, chalets, estudios. Rápido, limpio, discreto. Presupuesto gratis. Llamar ahora.",
    "Limpieza incendios comercios {ciudad}. Restaurantes, oficinas, tiendas. Reabierto rápido. Presupuesto sin compromiso. 24/7.",
    "{ciudad}: Limpieza post incendio vivienda unifamiliar. Protegemos tus muebles. Presupuesto detallado. Garantía de resultado.",
    "Limpieza urgente incendios {ciudad} | Edifios antiguos especializados. Respeto por detalles. Presupuesto gratis. Llamar 24/7.",
    "Limpieza post incendio {ciudad} | Naves, garajes, almacenes. Áreas grandes sin problema. Presupuesto sin compromiso. Disponibles ya.",
]

def hash_slug(slug):
    """Generate hash from slug string"""
    return sum(ord(c) for c in slug)

def get_seo_index(slug, total=15):
    """Get SEO template index based on slug hash"""
    h = hash_slug(slug)
    return h % total

def generate_problem_section(city_name, is_neighborhood=False):
    """Generate unique problem section based on city"""
    problems = {
        "Barcelona": "En Barcelona, los incendios tienen característica especial: los pisos están pegados unos a otros, los conductos de aire son compartidos, las escaleras son chimenea. Cuando el fuego golpea, el humo no respeta puertas: sube, sube, y mancha a los vecinos de arriba y abajo. Además, muchos edificios de Eixample y Gràcia tienen estructuras originales de hace ciento treinta años: no están diseñados para ventilación moderna.",
        "Eixample": "En Eixample, los bloques de finales del XIX tienen luz interior compartida: patio pequeño que actúa como chimenea. Un incendio en un piso bajo se ve reflejado en hollín en el séptimo piso. Las instalaciones son viejas, improvisadas en reformas sucesivas, sin aislamiento. El humo penetra profundo.",
        "Gràcia": "Gràcia es pueblo dentro de ciudad: casas conectadas, escaleras estrechas, patios mínimos. Un incendio aquí es drama comunitario que afecta a toda la manzana. Los edificios respiran entre sí, los olores se comparten, los daños son múltiples.",
        "Sarrià": "Sarrià tiene casas más dispersas, terrazas, jardines. Pero eso significa que el humo, cuando llega, penetra profundo en espacios amplios. Las casas de Sarrià tienen más materiales naturales: madera, plantas, textiles que absorben hollín.",
        "Montjuïc": "En Montjuïc viven chalets con valor, casas de época, materiales valiosos. El incendio aquí no es solo sucio: es destructivo para patrimonio. Los pisos largos acumulan hollín en rincones que cuesta limpiar sin dañar.",
        "Horta": "Horta es densidad: bloques altos, ascensores compartidos, escaleras donde sube el humo de forma desordenada. Los apartamentos son pequeños pero múltiples: un incendio afecta a diez viviendas mínimo.",
        "Valencia": "En Valencia, los pisos modernos están sellados: aire acondicionado centralizado que redistribuye humo por toda la vivienda. Los materiales son económicos, porosos: absorben hollín con facilidad. Además, la densidad es extrema: edificios de dos filas que comparten sistemas.",
        "Centro": "El Centro de Valencia es mezcla: edificios históricos con instalaciones nuevas improvisadas. Un incendio aquí es caos de técnicas mixtas: estructura antigua con mecánica moderna. El daño es impredecible.",
        "Rascaña": "Rascaña es bloques de viviendas típicos de los años 70-80: hormigón, poco aislamiento, conductos compartidos. El humo se distribuye igual entre arriba y abajo. Muchas viviendas simultáneamente afectadas.",
        "Campanar": "Campanar mantiene parcelas con construcciones variadas: desde casas bajas antiguas hasta bloques nuevos. Cada tipo requiere técnica diferente. El humo viaja distinto en casa de época que en apartamento moderno.",
        "Sevilla": "En Sevilla, los incendios afectan a patrimonio: azulejos mudejar, maderas centenarias, patios históricos. El hollín del fuego se incrusta en poro arquitectónico. El daño es no solo suciedad: es amenaza a herencia cultural.",
        "Málaga": "En Málaga, la humedad marina acelera el proceso de corrosión del hollín. La sal del aire hace que el residuo sea más pegajoso, más difícil de eliminar. Además, hay mucho turismo: un incendio en apartamento de playa es pérdida económica inmediata.",
        "Alicante": "Alicante es heterogeneidad: desde apartamentos de lujo junto al mar hasta viviendas obreras con densidad extrema. El mismo incendio requiere técnicas diferentes según ubicación. Además, la cercanía del mar complica la limpieza por sales.",
        "Murcia": "Murcia es ciudad sin prisa. Los incendios aquí tienen velocidad lenta pero daño profundo: el calor del interior mantiene el humo activo durante días, los olores persisten, el hollín se enquista.",
        "Zaragoza": "Zaragoza es ciudad de transición: edificios antiguos del Casco Viejo conviven con bloques residenciales sin carácter. Cada tipo de construcción tiene problemas diferentes. El humo de un piso bajo viaja diferente que en otro.",
        "Granada": "Granada está en ladera: los incendios aquí tienen geografía compleja. El humo sube diferente, los pisos están en niveles diferentes, la dispersión es tridimensional. La limpieza requiere entender esa topografía.",
        "Córdoba": "Córdoba es patrimonio puro: casas patio que son obras de arte, azulejos mudejar que son historia. Un incendio es amenaza directa a eso. El hollín mancha piezas arqueológicas vivas.",
        "Bilbao": "Bilbao tiene humedad del Nervión: hace que el humo sea más pegajoso, los olores más persistentes. Además, la ciudad tiene capas de tiempo: edificios del Casco Viejo conviven con arquitectura moderna. Cada zona requiere técnica diferente.",
        "Palma": "En Palma, el aislamiento de la isla hace que no haya emergencias rápidas: si se quema un apartamento, no viene especialista profesional de aquí a mañana. La humedad marina es intensa. El daño se multiplica por falta de intervención urgente.",
    }
    return problems.get(city_name, f"En {city_name}, los incendios crean situaciones donde el humo y hollín penetran profundamente en estructuras variadas.")

def generate_faq_section(city_name):
    """Generate FAQ section"""
    return f"""<div class="faq-item"><h3>¿Cuánto tarda la limpieza post incendio en {city_name}?</h3><p>Depende del tamaño. Una habitación, 1 día. Una vivienda media (70-90m²), 2-3 días. Nos desplazamos en menos de 24 horas para valorar. La urgencia es prioridad.</p></div><div class="faq-item"><h3>¿El seguro paga la limpieza post incendio?</h3><p>Generalmente sí. Revisamos tu póliza, documentamos todo con fotografías, emitimos informe. Tú nos pagas o el seguro lo hace directamente. Sin sorpresas.</p></div><div class="faq-item"><h3>¿Hacéis también reformas o pinturas después?</h3><p>No. Nos centramos exclusivamente en limpieza y descontaminación. Somos especialistas en eso, no en obras. Después de nosotros, la casa está lista para reforma si hace falta, o para vivir si el daño es solo suciedad.</p></div>"""

def generate_html(city_data, neighborhood=None, all_cities=None):
    """Generate HTML for a city or neighborhood"""

    if neighborhood:
        name = neighborhood['name']
        city_name = city_data['name']
        h1 = neighborhood['h1']
        intro = neighborhood['intro']
        slug = neighborhood['id']
        filename = neighborhood['filename']
    else:
        name = city_data['name']
        city_name = name
        h1 = city_data['h1']
        intro = city_data['intro']
        slug = city_data['id']
        filename = city_data['filename']

    # Get SEO templates
    seo_idx = get_seo_index(slug)
    title = SEO_TITLES[seo_idx].format(ciudad=name)
    description = SEO_DESCRIPTIONS[seo_idx].format(ciudad=name)

    # Build JSON-LD schemas
    localbiz_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": f"Nano Nex - Limpieza de Incendios en {name}",
        "image": "https://limpiezaincendiosnanonexmadrid.com.es/Logo Nano Nex.png",
        "url": f"https://limpiezaincendiosnanonexmadrid.com.es/{filename}",
        "telephone": "632107272",
        "email": "info@nanonex.es",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": city_name,
            "addressCountry": "ES"
        },
        "areaServed": name,
        "priceRange": "$$",
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "07:00",
                "closes": "22:00"
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Saturday", "Sunday"],
                "opens": "08:00",
                "closes": "16:00"
            }
        ]
    })

    breadcrumb_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://limpiezaincendiosnanonexmadrid.com.es/"},
            {"@type": "ListItem", "position": 2, "name": "Zonas", "item": "https://limpiezaincendiosnanonexmadrid.com.es/ubicaciones.html"},
            {"@type": "ListItem", "position": 3, "name": name, "item": f"https://limpiezaincendiosnanonexmadrid.com.es/{filename}"}
        ]
    })

    faq_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"¿Cuánto cuesta una limpieza post incendio en {name}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "El presupuesto depende de la superficie afectada y el nivel de hollín. Una habitación cuesta desde 350€. Una vivienda media (70-90m²) entre 900€ y 2.500€. Hacemos presupuesto gratuito sin compromiso."
                }
            }
        ]
    })

    # Build breadcrumb
    if neighborhood:
        breadcrumb = f'<a href="index.html">Inicio</a><span>&rsaquo;</span><a href="ubicaciones.html">Zonas</a><span>&rsaquo;</span><a href="limpieza-de-incendios-{city_data["id"]}.html">{city_name}</a><span>&rsaquo;</span>{name}'
    else:
        breadcrumb = f'<a href="index.html">Inicio</a><span>&rsaquo;</span><a href="ubicaciones.html">Zonas</a><span>&rsaquo;</span>{name}'

    # Build neighborhoods section
    neighborhoods_section = ""
    if not neighborhood and city_data.get('neighborhoods'):
        neighborhoods_section = f'<section class="otros-barrios"><h3>También cubrimos otros barrios de {city_name}</h3><div class="links-grid">'
        for nb in city_data['neighborhoods']:
            neighborhoods_section += f'<a href="{nb["filename"]}" class="link-btn">{nb["name"]} →</a>'
        neighborhoods_section += '</div></section>'

    # Build sidebar neighborhood links (exclude current neighborhood)
    barrios_html = ""
    if city_data.get('neighborhoods'):
        barrios_html = f'<div class="side-box"><h3>Barrios de {city_name}</h3><div class="side-links">'
        count = 0
        for nb in city_data['neighborhoods']:
            if nb['filename'] != filename:  # Don't link to self
                if count < 4:
                    barrios_html += f'<a href="{nb["filename"]}">{nb["name"]}</a>'
                    count += 1
        barrios_html += '</div></div>'

    # Build linked cities (validate they exist in our config)
    linked_cities_html = ""
    if city_data.get('linkedCities') and all_cities:
        linked_cities_html = '<div class="side-box"><h3>Otras ciudades donde actuamos</h3><div class="side-links">'
        for linked_city_id in city_data['linkedCities']:
            # Check if the linked city exists in config
            if any(c['id'] == linked_city_id for c in all_cities):
                linked_city_name = linked_city_id.replace("-", " ").title()
                linked_cities_html += f'<a href="limpieza-de-incendios-{linked_city_id}.html">{linked_city_name}</a>'
        linked_cities_html += '</div></div>'

    # Get content
    problem_text = generate_problem_section(name, neighborhood is not None)
    faq_section = generate_faq_section(name)

    # Build HTML
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://limpiezaincendiosnanonexmadrid.com.es/{filename}">
<link rel="icon" type="image/png" href="Favicon trasnparente Rojo Naranja.png">
<link rel="apple-touch-icon" href="Favicon trasnparente Rojo Naranja.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="Limpieza de Incendios en {name} | Nano Nex Post Incendio">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://limpiezaincendiosnanonexmadrid.com.es/{filename}">
<meta property="og:image" content="https://limpiezaincendiosnanonexmadrid.com.es/LimpiezadeGarajes.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<script type="application/ld+json">{localbiz_schema}</script>
<script type="application/ld+json">{breadcrumb_schema}</script>
<script type="application/ld+json">{faq_schema}</script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Open+Sans:wght@400;600&display=swap" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Open+Sans:wght@400;600&display=swap"></noscript>
<link rel="stylesheet" href="estilos-landing.css?v=3">
</head>
<body>
<div class="topbar"><span class="tb-full">🚨 Operativos 24/7 · Limpieza profesional 365 días</span><span class="tb-short">🚨 Urgencias 24/7 · Los 365 días</span></div>
<header>
    <div class="logo"><a href="index.html"><img src="Logo Nano Nex.png" alt="Nano Nex Limpieza de Incendios Madrid" width="680" height="174"></a></div>
    <div class="header-right">
        <nav class="nav-menu" id="navMenu"><a href="index.html">Inicio</a><a href="ubicaciones.html">Zonas</a><a href="blog.html">Blog</a><a href="#contacto">Contacto</a></nav>
        <div class="header-contact"><a href="tel:632107272" class="phone-btn"><svg viewBox="0 0 24 24" width="18" height="18" fill="#fff" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg> <span>632 107 272</span></a></div>
        <button class="menu-toggle" id="menuToggle" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
</header>
<main>

<section class="hero-landing" style="background-image: linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.72)), url('LimpiezadeGarajes.webp');">
    <div class="hero-landing-content">
        <h1>{h1}</h1>
        <p>{intro}</p>
        <a href="#contacto" class="cta-btn">Pide presupuesto gratis</a>
    </div>
</section>

<nav class="breadcrumb" aria-label="Migas de pan">
    {breadcrumb}
</nav>

<div class="wrap">
<div class="layout">
<div class="content">
    <div class="quick-answer"><strong>Respuesta rápida:</strong> Una limpieza post incendio en {name} cuesta entre 600 y 3.500 € según superficie y hollín. Nano Nex llega en menos de 24 horas, retira humo y hollín, desodoriza con ozono y entrega informe para el seguro. Solo limpiamos.</div>

    <p>Conocemos {name}. Sabemos qué significa un incendio aquí, en esta ciudad, en estos barrios. Sabemos que la gente tiene prisa y no puede esperar semanas. Por eso llegamos rápido, limpiamos a fondo, dejamos todo como era — y lo hacemos sin molestar a los vecinos ni el entorno.</p>

    <p>{problem_text}</p>

    <img src="LimpiezadeGarajes.webp" loading="lazy" class="landing-img" alt="Limpieza de incendios y hollín en {name}" width="600" height="748">

    <h2>Por qué la limpieza tras un incendio en {name} es urgente</h2>
    <p>El hollín no es solo suciedad: es un residuo graso y ácido que, con el paso de los días, corroe metales, amarillea plásticos y se incrusta en superficies porosas. Cuanto antes se actúe, más enseres se recuperan y menor es el coste final. Por eso en {name} nos desplazamos en menos de 24 horas para valorar los daños y frenar su avance.</p>
    <ul class="bullets">
        <li>Eliminación de hollín en paredes, techos y mobiliario</li>
        <li>Neutralización del olor a humo con ozono (no lo enmascaramos)</li>
        <li>Limpieza técnica de cocinas, campanas y conductos</li>
        <li>Vaciado, desescombro y gestión de residuos del siniestro</li>
        <li>Informe técnico con fotografías para tu aseguradora</li>
    </ul>

    <h2>Cómo trabajamos: nuestro proceso paso a paso</h2>
    <ol>
        <li><strong>Valoración en 24 h.</strong> Visitamos {name}, evaluamos el alcance del hollín y damos un presupuesto cerrado.</li>
        <li><strong>Protección y ventilación.</strong> Aislamos zonas no afectadas y ventilamos de forma controlada para evitar que el humo siga extendiéndose.</li>
        <li><strong>Retirada de residuos.</strong> Vaciamos y desescombramos lo no recuperable y gestionamos los residuos.</li>
        <li><strong>Limpieza técnica del hollín.</strong> Aplicamos aspiración HEPA y esponjas químicas en seco antes de la limpieza húmeda, según el material.</li>
        <li><strong>Desodorización con ozono.</strong> Eliminamos el olor a humo de raíz en estancias, armarios y textiles.</li>
        <li><strong>Informe para el seguro.</strong> Entregamos documentación fotográfica de todo el trabajo.</li>
    </ol>

    <h2>Precios orientativos de limpieza post incendio en {name}</h2>
    <table>
        <tr><th>Tipo de intervención</th><th>Plazo estimado</th><th>Precio orientativo</th></tr>
        <tr><td>Habitación / estancia afectada</td><td>1 día</td><td>desde 350 €</td></tr>
        <tr><td>Vivienda media (70-90 m²)</td><td>2-3 días</td><td>900 € - 2.500 €</td></tr>
        <tr><td>Vivienda grande / chalet</td><td>3-5 días</td><td>2.500 € - 6.000 €</td></tr>
        <tr><td>Local, cocina o nave</td><td>según superficie</td><td>presupuesto a medida</td></tr>
    </table>
    <p style="font-size:0.9rem;color:#777;">*Precios orientativos. El presupuesto final depende de la superficie, el nivel de hollín y los materiales. La valoración es gratuita.</p>

    <h2>Qué incluye y qué no</h2>
    <p><strong>Sí hacemos:</strong></p>
    <ul class="bullets">
        <li>Limpieza y descontaminación de hollín, humo y olores</li>
        <li>Tratamiento de mobiliario, textiles y enseres recuperables</li>
        <li>Limpieza de zonas comunes afectadas</li>
    </ul>
    <p><strong>No hacemos:</strong> obras, reformas, pintura ni restauración estructural. Nos centramos exclusivamente en la limpieza y descontaminación, que es donde somos especialistas.</p>

    <h2>La gente también pregunta sobre la limpieza de incendios en {name}</h2>
    {faq_section}

    <h2>Errores frecuentes al limpiar tras un incendio en {name}</h2>
    <p>El error más común en {name} es intentar limpiar por cuenta propia. El hollín es tóxico: respirarlo sin protección es peligro para la salud. Además, las técnicas caseras no funcionan: esparcen el humo, manchan más, y los olores persisten. Lo mejor es llamar a profesionales desde el primer momento. Nosotros atendemos urgencias 24/7.</p>

</div>
<aside class="sidebar">
    <div class="side-box cta-box">
        <h3>¿Urgencia por incendio?</h3>
        <p>Atendemos 24/7 en {name}. Presupuesto gratuito e informe para el seguro.</p>
        <a href="tel:632107272" class="cta-btn">Llamar 632 107 272</a>
    </div>
    <div class="side-box"><h3>Guía útil</h3><div class="side-links"><a href="como-limpiar-el-hollin-en-madrid.html">Cómo limpiar el hollín</a><a href="blog.html">Ver todo el blog</a></div></div>

    {barrios_html}

    {linked_cities_html}

    <div class="side-box">
        <h3>Más información</h3>
        <div class="side-links"><a href="ubicaciones.html">Todas las zonas de actuación</a><a href="index.html">Servicios de limpieza de incendios</a></div>
    </div>
</aside>
</div>
</div>

<section class="form-section" id="contacto">
    <div class="form-card">
        <h2>Solicita presupuesto sin compromiso</h2>
        <p class="lead">📞 Déjanos tus datos y nosotros te llamamos.</p>
        <div id="success-banner">✅ ¡Gracias! Hemos recibido tu aviso. Te llamaremos en breve.</div>
        <form id="my-form" action="https://formspree.io/f/xqarnldw" method="POST">
            <input type="hidden" name="_subject" value="Nueva solicitud ({name}) - limpiezaincendiosnanonexmadrid.com.es">
            <input type="hidden" name="Origen" value="{name} - limpiezaincendiosnanonexmadrid.com.es">
            <div class="form-group"><label>Nombre <input type="text" name="Nombre" placeholder="Tu nombre" required></label></div>
            <div class="form-group"><label>Teléfono <input type="tel" name="Telefono" placeholder="Tu teléfono" required></label></div>
            <div class="form-group"><label>Población <input type="text" name="Poblacion" placeholder="Tu población o barrio" required></label></div>
            <div class="form-group" style="font-size:0.85rem;"><label><input type="checkbox" required> Acepto la <a href="privacidad.html" style="color:var(--primary);">política de privacidad</a>.</label></div>
            <button type="submit" id="my-form-button" class="cta-btn" style="width:100%;">ENVIAR AVISO</button>
        </form>
    </div>
</section>

{neighborhoods_section}

</main>
<footer>
    <div class="footer-content">
        <div class="footer-col"><h4>Nano Nex Madrid</h4><p>Plaza de Castilla, 3, 28046 Madrid</p><p>📞 632 107 272</p><p>info@nanonex.es</p></div>
        <div class="footer-col footer-links"><h4>Información</h4><a href="index.html">Inicio</a><a href="ubicaciones.html">Zonas de actuación</a><a href="blog.html">Blog</a><a href="aviso-legal.html">Aviso Legal</a><a href="privacidad.html">Política de Privacidad</a><a href="cookies.html">Política de Cookies</a></div>
        <div class="footer-col"><h4>Horario</h4><p>L-V: 07:00 - 22:00</p><p>Sáb-Dom: 08:00 - 16:00</p><p><strong>Urgencias 24/7</strong></p></div>
    </div>
    <div class="footer-bottom">&copy; 2020 Nano Nex. Todos los derechos reservados.</div>
    <div class="footer-grupo">Nano Nex Madrid forma parte del <a href="https://nano-nex.es">Grupo Nano Nex</a>.</div>
</footer>
<a href="tel:632107272" class="call-float" aria-label="Llamar al 632 107 272"><svg viewBox="0 0 24 24" width="30" height="30" fill="#fff" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></a>
<a href="https://wa.me/34632107272?text=Hola,%20tengo%20una%20urgencia%20por%20incendio,%20necesito%20ayuda" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Contactar por WhatsApp"><svg viewBox="0 0 32 32" width="36" height="36" fill="#fff" aria-hidden="true"><path d="M16.04 4C9.96 4 5.02 8.94 5.02 15.02c0 1.94.51 3.84 1.48 5.51L4.9 27l6.63-1.74a11 11 0 0 0 4.51.97h.01c6.08 0 11.02-4.94 11.02-11.02C27.07 8.94 22.12 4 16.04 4zm0 20.18h-.01a9.13 9.13 0 0 1-4.65-1.27l-.33-.2-3.93 1.03 1.05-3.83-.22-.35a9.1 9.1 0 0 1-1.4-4.86c0-5.05 4.11-9.16 9.17-9.16 2.45 0 4.75.96 6.48 2.69a9.1 9.1 0 0 1 2.68 6.48c0 5.06-4.11 9.17-9.16 9.17zm5.03-6.86c-.28-.14-1.63-.8-1.88-.9-.25-.09-.43-.14-.61.14-.18.28-.7.9-.86 1.08-.16.18-.32.2-.59.07-.28-.14-1.16-.43-2.21-1.36-.82-.73-1.37-1.62-1.53-1.9-.16-.28-.02-.43.12-.57.13-.13.28-.32.41-.49.14-.16.18-.28.28-.46.09-.18.05-.35-.02-.49-.07-.14-.61-1.48-.84-2.02-.22-.53-.45-.46-.61-.47l-.52-.01c-.18 0-.46.07-.7.35-.25.28-.95.93-.95 2.27 0 1.34.97 2.63 1.11 2.81.14.18 1.91 2.92 4.63 4.09.65.28 1.15.45 1.54.57.65.21 1.24.18 1.7.11.52-.08 1.63-.67 1.86-1.31.23-.65.23-1.2.16-1.31-.07-.12-.25-.19-.53-.33z"/></svg></a>
<script>
if ('scrollRestoration' in history) {{ history.scrollRestoration = 'manual'; }}
window.addEventListener('load', function(){{ if(!window.location.hash){{ window.scrollTo(0,0); }} }});
var form = document.getElementById("my-form");
function handleSubmit(e){{ e.preventDefault(); var b=document.getElementById("success-banner"); var data=new FormData(e.target);
 fetch(e.target.action,{{method:form.method,body:data,headers:{{'Accept':'application/json'}}}}).then(function(r){{
   if(r.ok){{ b.style.display="block"; form.reset(); setTimeout(function(){{b.style.display="none";}},5000);}} else {{ alert("Oops! Hubo un problema al enviar el formulario"); }}
 }}).catch(function(){{ alert("Oops! Hubo un problema al enviar el formulario"); }});
}}
form.addEventListener("submit", handleSubmit);
</script>
<div class="mobile-cta-bar"><a href="tel:632107272" class="mcb-call"><svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg> Llamar</a><a href="https://wa.me/34632107272?text=Hola,%20tengo%20una%20urgencia%20por%20incendio,%20necesito%20ayuda" class="mcb-wa" target="_blank" rel="noopener"><svg viewBox="0 0 32 32" fill="#fff" aria-hidden="true"><path d="M16.04 4C9.96 4 5.02 8.94 5.02 15.02c0 1.94.51 3.84 1.48 5.51L4.9 27l6.63-1.74a11 11 0 0 0 4.51.97h.01c6.08 0 11.02-4.94 11.02-11.02C27.07 8.94 22.12 4 16.04 4zm0 20.18h-.01a9.13 9.13 0 0 1-4.65-1.27l-.33-.2-3.93 1.03 1.05-3.83-.22-.35a9.1 9.1 0 0 1-1.4-4.86c0-5.05 4.11-9.16 9.17-9.16 2.45 0 4.75.96 6.48 2.69a9.1 9.1 0 0 1 2.68 6.48c0 5.06-4.11 9.17-9.16 9.17zm5.03-6.86c-.28-.14-1.63-.8-1.88-.9-.25-.09-.43-.14-.61.14-.18.28-.7.9-.86 1.08-.16.18-.32.2-.59.07-.28-.14-1.16-.43-2.21-1.36-.82-.73-1.37-1.62-1.53-1.9-.16-.28-.02-.43.12-.57.13-.13.28-.32.41-.49.14-.16.18-.28.28-.46.09-.18.05-.35-.02-.49-.07-.14-.61-1.48-.84-2.02-.22-.53-.45-.46-.61-.47l-.52-.01c-.18 0-.46.07-.7.35-.25.28-.95.93-.95 2.27 0 1.34.97 2.63 1.11 2.81.14.18 1.91 2.92 4.63 4.09.65.28 1.15.45 1.54.57.65.21 1.24.18 1.7.11.52-.08 1.63-.67 1.86-1.31.23-.65.23-1.2.16-1.31-.07-.12-.25-.19-.53-.33z"/></svg> WhatsApp</a></div>
<script>(function(){{var t=document.getElementById("menuToggle"),n=document.getElementById("navMenu");if(t&&n){{t.addEventListener("click",function(){{var o=n.classList.toggle("open");t.classList.toggle("open",o);t.setAttribute("aria-expanded",o?"true":"false");}});n.querySelectorAll("a").forEach(function(a){{a.addEventListener("click",function(){{n.classList.remove("open");t.classList.remove("open");t.setAttribute("aria-expanded","false");}});}});}}}})();
</script>
</body>
</html>"""

    return html_content

def main():
    """Main generation function"""
    # Load city data
    with open('CIUDADES_CONFIG.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    base_path = '/home/user/limpieza_incendios_nanonex_es/'
    generated_count = 0

    for city in data['cities']:
        # Generate city page
        html = generate_html(city, all_cities=data['cities'])
        filepath = os.path.join(base_path, city['filename'])
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Created {city['filename']}")
        generated_count += 1

        # Generate neighborhood pages
        for neighborhood in city.get('neighborhoods', []):
            html = generate_html(city, neighborhood, all_cities=data['cities'])
            filepath = os.path.join(base_path, neighborhood['filename'])
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"✓ Created {neighborhood['filename']}")
            generated_count += 1

    print(f"\n✅ Generated {generated_count} pages total!")
    return generated_count

if __name__ == '__main__':
    main()
