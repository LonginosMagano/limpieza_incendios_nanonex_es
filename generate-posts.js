#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { Jimp } = require('jimp');

// Leer posts JSON
const postsData = JSON.parse(fs.readFileSync('/tmp/posts_extracted.json', 'utf8'));

// Función para extraer slug de la URL
function extractSlugFromUrl(url) {
  try {
    const urlObj = new URL(url);
    const pathname = urlObj.pathname.replace(/\/$/, '');
    const parts = pathname.split('/').filter(p => p);
    return {
      slug: parts[parts.length - 1],
      date: {
        year: parts[0],
        month: parts[1],
        day: parts[2]
      }
    };
  } catch (e) {
    return null;
  }
}

// Función para validar URLs y filtrar posts válidos
function filterValidPosts(posts) {
  return posts
    .filter(post => post.status === 'publish' && post.link && post.date)
    .map(post => ({
      ...post,
      urlParts: extractSlugFromUrl(post.link)
    }))
    .filter(post => post.urlParts && post.urlParts.slug)
    .sort((a, b) => new Date(b.date) - new Date(a.date));
}

// Función para generar imagen destacada
async function generateFeaturedImage(title, category, outputPath) {
  try {
    // Crear imagen de 1200x630px
    const width = 1200;
    const height = 630;

    // Colores por categoría (en formato que Jimp entienda: 0xRRGGBBAA)
    const categoryColors = {
      'Limpieza de Incendios': 0xFF6B35FF,
      'Limpieza con Ozono': 0xFFA500FF,
      'Limpieza': 0x0066CCFF,
      'Empresas de Limpieza': 0x33AA00FF,
      'Limpieza Post Incendios': 0xFF8800FF,
    };

    const bgColor = categoryColors[category] || 0xFF6B35FF;

    // Crear imagen con el color especificado
    const img = new Jimp({ width, height, color: bgColor });

    // Crear directorio si no existe
    const dir = path.dirname(outputPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    // Guardar como PNG (WebP no está soportado en todas las versiones)
    const pngPath = outputPath.replace('.webp', '.png');
    await img.write(pngPath);
    return true;
  } catch (error) {
    console.error(`Error generating image for "${title}": ${error.message}`);
    return false;
  }
}

// Función para generar HTML del post
function generatePostHTML(post, featuredImageUrl) {
  const {
    title,
    link,
    date,
    content_length,
    categories = [],
    tags = []
  } = post;

  const pageTitle = `${title} | Nano Nex`;
  const description = title.substring(0, 155);
  const mainCategory = categories[0] || 'Blog';

  // Extraer fecha y año para breadcrumb
  const dateObj = new Date(date);
  const year = dateObj.getFullYear();
  const month = String(dateObj.getMonth() + 1).padStart(2, '0');
  const day = String(dateObj.getDate()).padStart(2, '0');
  const dateFormatted = dateObj.toLocaleDateString('es-ES', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });

  const html = `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${pageTitle}</title>
<meta name="description" content="${description}">
<meta name="robots" content="index, follow">
<meta name="author" content="Nano Nex Madrid">
<meta name="date" content="${dateFormatted}">
<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${description}">
<meta property="og:url" content="${link}">
<meta property="og:image" content="${featuredImageUrl}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="article:published_time" content="${new Date(date).toISOString()}">
<meta property="article:author" content="Nano Nex Madrid">
${categories.map(cat => `<meta property="article:section" content="${cat}">`).join('\n')}
<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${description}">
<meta name="twitter:image" content="${featuredImageUrl}">
<!-- Canonical -->
<link rel="canonical" href="${link}">
<link rel="icon" type="image/png" href="/Favicon trasnparente Rojo Naranja.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Open+Sans:wght@400;600&display=swap" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Open+Sans:wght@400;600&display=swap"></noscript>
<link rel="stylesheet" href="/estilos-landing.css?v=3">
<link rel="preload" as="image" href="${featuredImageUrl}">
<!-- JSON-LD Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "${title}",
  "description": "${description}",
  "image": "${featuredImageUrl}",
  "datePublished": "${new Date(date).toISOString()}",
  "author": {
    "@type": "Organization",
    "name": "Nano Nex Madrid",
    "url": "https://limpiezaincendiosnanonex.es"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Nano Nex Madrid",
    "logo": {
      "@type": "ImageObject",
      "url": "https://limpiezaincendiosnanonex.es/Logo Nano Nex.png"
    }
  }
}
</script>
</head>
<body>
<a href="#main" class="skip-link">Saltar al contenido principal</a>
<div class="topbar"><span class="tb-full">🚨 Operativos 24/7 · Limpieza profesional 365 días</span><span class="tb-short">🚨 Urgencias 24/7 · Los 365 días</span></div>
<header>
    <div class="logo"><a href="/index.html"><img src="/Logo Nano Nex.png" alt="Nano Nex Limpieza de Incendios Madrid" width="680" height="174"></a></div>
    <div class="header-right">
        <nav class="nav-menu" id="navMenu"><a href="/index.html">Inicio</a><a href="/ubicaciones.html">Zonas</a><a href="/blog.html">Blog</a><a href="#contacto">Contacto</a></nav>
        <div class="header-contact"><a href="tel:632107272" class="phone-btn"><svg viewBox="0 0 24 24" width="18" height="18" fill="#fff" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg> <span>632 107 272</span></a></div>
        <button class="menu-toggle" id="menuToggle" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
</header>
<main id="main">
<section class="hero-landing">
    <div class="hero-landing-content">
        <h1>${title}</h1>
        <p>${mainCategory}</p>
    </div>
</section>
<nav class="breadcrumb">
    <a href="/index.html">Inicio</a>
    <span>&rsaquo;</span>
    <a href="/blog.html">Blog</a>
    <span>&rsaquo;</span>
    <span>${title}</span>
</nav>
<article class="blog-article">
    <div class="wrap" style="padding-top:50px;padding-bottom:50px;">
        <div class="article-meta">
            <span class="article-date">${dateFormatted}</span>
            <span class="article-cat">${mainCategory}</span>
        </div>
        <figure class="article-featured">
            <img src="${featuredImageUrl}" alt="${title}" width="1200" height="630">
        </figure>
        <div class="article-content">
            <p><em>Contenido del post: Este es un placeholder. El contenido original será agregado desde el XML de WordPress.</em></p>
            <p>Este artículo forma parte de nuestra serie de guías sobre ${mainCategory.toLowerCase()}.</p>
            ${tags.length > 0 ? `<div class="article-tags"><strong>Tags:</strong> ${tags.map(tag => `<span>${tag}</span>`).join(', ')}</div>` : ''}
        </div>
    </div>
</article>
<section class="form-section" id="contacto">
    <div class="form-card">
        <h2>¿Necesitas ayuda urgente?</h2>
        <p class="lead">📞 Déjanos tus datos y nosotros te llamamos.</p>
        <div id="success-banner">✅ ¡Gracias! Hemos recibido tu aviso. Te llamaremos en breve.</div>
        <form id="my-form" action="https://formspree.io/f/xqarnldw" method="POST">
            <input type="hidden" name="_subject" value="Nueva solicitud (Blog: ${title}) - limpiezaincendiosnanonexmadrid.com.es">
            <input type="hidden" name="Origen" value="Blog - ${title} - limpiezaincendiosnanonexmadrid.com.es">
            <div class="form-group"><label>Nombre <input type="text" name="Nombre" placeholder="Tu nombre" required></label></div>
            <div class="form-group"><label>Teléfono <input type="tel" name="Telefono" placeholder="Tu teléfono" required></label></div>
            <div class="form-group"><label>Población <input type="text" name="Poblacion" placeholder="Tu población o barrio" required></label></div>
            <div class="form-group" style="font-size:0.85rem;"><label><input type="checkbox" required> Acepto la <a href="/privacidad.html" style="color:var(--primary);">política de privacidad</a>.</label></div>
            <button type="submit" id="my-form-button" class="cta-btn" style="width:100%;">ENVIAR AVISO</button>
        </form>
    </div>
</section>
</main>
<footer>
    <div class="footer-content">
        <div class="footer-col"><h4>Nano Nex Madrid</h4><p>Plaza de Castilla, 3, 28046 Madrid</p><p>📞 632 107 272</p><p>info@nanonex.es</p></div>
        <div class="footer-col footer-links"><h4>Información</h4><a href="/index.html">Inicio</a><a href="/ubicaciones.html">Zonas de actuación</a><a href="/blog.html">Blog</a><a href="/aviso-legal.html">Aviso Legal</a><a href="/privacidad.html">Política de Privacidad</a><a href="/cookies.html">Política de Cookies</a></div>
        <div class="footer-col"><h4>Horario</h4><p>L-V: 07:00 - 22:00</p><p>Sáb-Dom: 08:00 - 16:00</p><p><strong>Urgencias 24/7</strong></p></div>
    </div>
    <div class="footer-bottom">&copy; 2020 Nano Nex. Todos los derechos reservados.</div>
    <div class="footer-grupo">Nano Nex Madrid forma parte del <a href="https://nano-nex.es">Grupo Nano Nex</a>.</div>
</footer>
<a href="tel:632107272" class="call-float" aria-label="Llamar al 632 107 272"><svg viewBox="0 0 24 24" width="30" height="30" fill="#fff" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></a>
<a href="https://wa.me/34632107272?text=Hola,%20tengo%20una%20urgencia%20por%20incendio,%20necesito%20ayuda" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Contactar por WhatsApp"><svg viewBox="0 0 32 32" width="36" height="36" fill="#fff" aria-hidden="true"><path d="M16.04 4C9.96 4 5.02 8.94 5.02 15.02c0 1.94.51 3.84 1.48 5.51L4.9 27l6.63-1.74a11 11 0 0 0 4.51.97h.01c6.08 0 11.02-4.94 11.02-11.02C27.07 8.94 22.12 4 16.04 4zm0 20.18h-.01a9.13 9.13 0 0 1-4.65-1.27l-.33-.2-3.93 1.03 1.05-3.83-.22-.35a9.1 9.1 0 0 1-1.4-4.86c0-5.05 4.11-9.16 9.17-9.16 2.45 0 4.75.96 6.48 2.69a9.1 9.1 0 0 1 2.68 6.48c0 5.06-4.11 9.17-9.16 9.17zm5.03-6.86c-.28-.14-1.63-.8-1.88-.9-.25-.09-.43-.14-.61.14-.18.28-.7.9-.86 1.08-.16.18-.32.2-.59.07-.28-.14-1.16-.43-2.21-1.36-.82-.73-1.37-1.62-1.53-1.9-.16-.28-.02-.43.12-.57.13-.13.28-.32.41-.49.14-.16.18-.28.28-.46.09-.18.05-.35-.02-.49-.07-.14-.61-1.48-.84-2.02-.22-.53-.45-.46-.61-.47l-.52-.01c-.18 0-.46.07-.7.35-.25.28-.95.93-.95 2.27 0 1.34.97 2.63 1.11 2.81.14.18 1.91 2.92 4.63 4.09.65.28 1.15.45 1.54.57.65.21 1.24.18 1.7.11.52-.08 1.63-.67 1.86-1.31.23-.65.23-1.2.16-1.31-.07-.12-.25-.19-.53-.33z"/></svg></a>
<script>
if ('scrollRestoration' in history) { history.scrollRestoration = 'manual'; }
window.addEventListener('load', function(){ if(!window.location.hash){ window.scrollTo(0,0); } });
var form = document.getElementById("my-form");
function handleSubmit(e){ e.preventDefault(); var b=document.getElementById("success-banner"); var data=new FormData(e.target);
 fetch(e.target.action,{method:form.method,body:data,headers:{'Accept':'application/json'}}).then(function(r){
   if(r.ok){ b.style.display="block"; form.reset(); setTimeout(function(){b.style.display="none";},5000);} else { alert("Oops! Hubo un problema al enviar el formulario"); }
 }).catch(function(){ alert("Oops! Hubo un problema al enviar el formulario"); });
}
form.addEventListener("submit", handleSubmit);
</script>
<div class="mobile-cta-bar"><a href="tel:632107272" class="mcb-call"><svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg> Llamar</a><a href="https://wa.me/34632107272?text=Hola,%20tengo%20una%20urgencia%20por%20incendio,%20necesito%20ayuda" class="mcb-wa" target="_blank" rel="noopener"><svg viewBox="0 0 32 32" fill="#fff" aria-hidden="true"><path d="M16.04 4C9.96 4 5.02 8.94 5.02 15.02c0 1.94.51 3.84 1.48 5.51L4.9 27l6.63-1.74a11 11 0 0 0 4.51.97h.01c6.08 0 11.02-4.94 11.02-11.02C27.07 8.94 22.12 4 16.04 4zm0 20.18h-.01a9.13 9.13 0 0 1-4.65-1.27l-.33-.2-3.93 1.03 1.05-3.83-.22-.35a9.1 9.1 0 0 1-1.4-4.86c0-5.05 4.11-9.16 9.17-9.16 2.45 0 4.75.96 6.48 2.69a9.1 9.1 0 0 1 2.68 6.48c0 5.06-4.11 9.17-9.16 9.17zm5.03-6.86c-.28-.14-1.63-.8-1.88-.9-.25-.09-.43-.14-.61.14-.18.28-.7.9-.86 1.08-.16.18-.32.2-.59.07-.28-.14-1.16-.43-2.21-1.36-.82-.73-1.37-1.62-1.53-1.9-.16-.28-.02-.43.12-.57.13-.13.28-.32.41-.49.14-.16.18-.28.28-.46.09-.18.05-.35-.02-.49-.07-.14-.61-1.48-.84-2.02-.22-.53-.45-.46-.61-.47l-.52-.01c-.18 0-.46.07-.7.35-.25.28-.95.93-.95 2.27 0 1.34.97 2.63 1.11 2.81.14.18 1.91 2.92 4.63 4.09.65.28 1.15.45 1.54.57.65.21 1.24.18 1.7.11.52-.08 1.63-.67 1.86-1.31.23-.65.23-1.2.16-1.31-.07-.12-.25-.19-.53-.33z"/></svg> WhatsApp</a></div>
<script>(function(){var t=document.getElementById("menuToggle"),n=document.getElementById("navMenu");if(t&&n){t.addEventListener("click",function(){var o=n.classList.toggle("open");t.classList.toggle("open",o);t.setAttribute("aria-expanded",o?"true":"false");});n.querySelectorAll("a").forEach(function(a){a.addEventListener("click",function(){n.classList.remove("open");t.classList.remove("open");t.setAttribute("aria-expanded","false");});});}})();
</script>
</body>
</html>`;

  return html;
}

// Función principal
async function main() {
  console.log('📝 Iniciando generación de posts...');

  // Filtrar y ordenar posts válidos
  const validPosts = filterValidPosts(postsData);
  console.log(`✓ Posts válidos encontrados: ${validPosts.length} de ${postsData.length}`);

  // Tomar los 10 más recientes para la prueba
  const testPosts = validPosts.slice(0, 10);
  console.log(`✓ Generando ${testPosts.length} posts de prueba\n`);

  const baseDir = '/home/user/limpieza_incendios_nanonex_es';
  const blogDir = path.join(baseDir, 'blog');
  const imagesDir = path.join(baseDir, 'blog-images');

  // Crear directorios base si no existen
  if (!fs.existsSync(imagesDir)) {
    fs.mkdirSync(imagesDir, { recursive: true });
  }

  let successCount = 0;
  let errorCount = 0;

  for (const post of testPosts) {
    const { slug, date } = post.urlParts;
    const year = date.year;
    const month = date.month;
    const day = date.day;

    // Rutas
    const postDir = path.join(blogDir, year, month, day, slug);
    const htmlPath = path.join(postDir, 'index.html');
    const imagePath = path.join(imagesDir, `${year}-${month}-${day}-${slug}.webp`);
    const imageUrl = `/blog-images/${year}-${month}-${day}-${slug}.webp`;

    try {
      // Crear estructura de carpetas
      if (!fs.existsSync(postDir)) {
        fs.mkdirSync(postDir, { recursive: true });
      }

      // Generar imagen
      const actualImagePath = imagePath.replace('.webp', '.png');
      const actualImageUrl = imageUrl.replace('.webp', '.png');

      const imageSuccess = await generateFeaturedImage(
        post.title,
        post.categories[0] || 'Blog',
        actualImagePath
      );

      if (!imageSuccess) {
        console.warn(`⚠ No se pudo generar imagen para: ${post.title}`);
      }

      // Generar HTML
      const html = generatePostHTML(post, actualImageUrl);
      fs.writeFileSync(htmlPath, html, 'utf8');

      console.log(`✓ ${year}/${month}/${day}/${slug}`);
      successCount++;
    } catch (error) {
      console.error(`✗ Error procesando ${post.title}: ${error.message}`);
      errorCount++;
    }
  }

  console.log(`\n📊 Resumen:`);
  console.log(`✓ Posts generados: ${successCount}`);
  console.log(`✗ Errores: ${errorCount}`);
  console.log(`📁 Ubicación: ${blogDir}`);
  console.log(`🖼 Imágenes: ${imagesDir}`);
}

main().catch(console.error);
