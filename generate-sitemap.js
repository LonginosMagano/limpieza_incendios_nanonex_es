#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const projectRoot = '/home/user/limpieza_incendios_nanonex_es';
const baseUrl = 'https://limpiezadeincendios-nanonex.es';
const changefreq = {
  'index.html': 'daily',
  'blog.html': 'weekly',
  'blog': 'monthly',
  'ubicaciones.html': 'weekly',
  'default': 'monthly',
};

const pages = [];

function getChangefreq(filePath) {
  if (filePath.includes('/blog/')) return changefreq.blog;
  const basename = path.basename(filePath);
  return changefreq[basename] || changefreq.default;
}

function getLastModified(filePath) {
  const stat = fs.statSync(filePath);
  return stat.mtime.toISOString().split('T')[0];
}

function getPriority(filePath) {
  if (filePath === 'index.html') return '1.0';
  if (filePath.includes('/blog/')) return '0.6';
  if (filePath.includes('ubicaciones')) return '0.9';
  if (filePath.endsWith('.html') && !filePath.includes('/blog/')) return '0.8';
  return '0.7';
}

function scanDirectory(dir, relativePath = '') {
  const files = fs.readdirSync(dir);

  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    const rel = relativePath ? `${relativePath}/${file}` : file;

    if (stat.isDirectory()) {
      if (!['node_modules', '.git', '.claude'].includes(file)) {
        scanDirectory(filePath, rel);
      }
    } else if (file === 'index.html' || (file.endsWith('.html') && !file.startsWith('.'))) {
      const url = rel.replace(/\\index\.html$/, '').replace(/\\/g, '/');
      const urlPath = url === 'index.html' ? '' : url;

      pages.push({
        url: urlPath,
        loc: `${baseUrl}${urlPath ? '/' + urlPath : '/'}`,
        lastmod: getLastModified(filePath),
        changefreq: getChangefreq(filePath),
        priority: getPriority(filePath),
      });
    }
  }
}

function generateSitemap() {
  scanDirectory(projectRoot);

  // Sort and deduplicate
  const uniquePages = Array.from(new Map(pages.map(p => [p.loc, p])).values());
  uniquePages.sort((a, b) => b.priority - a.priority);

  let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';

  for (const page of uniquePages) {
    xml += '  <url>\n';
    xml += `    <loc>${page.loc}</loc>\n`;
    xml += `    <lastmod>${page.lastmod}</lastmod>\n`;
    xml += `    <changefreq>${page.changefreq}</changefreq>\n`;
    xml += `    <priority>${page.priority}</priority>\n`;
    xml += '  </url>\n';
  }

  xml += '</urlset>';

  fs.writeFileSync(path.join(projectRoot, 'sitemap.xml'), xml, 'utf8');

  console.log('✓ Sitemap generado exitosamente');
  console.log(`  URLs totales: ${uniquePages.length}`);
  console.log(`  Prioridad alta (0.8-1.0): ${uniquePages.filter(p => p.priority >= 0.8).length}`);
  console.log(`  Prioridad media (0.6-0.7): ${uniquePages.filter(p => p.priority >= 0.6 && p.priority < 0.8).length}`);
  console.log(`  Prioridad baja (<0.6): ${uniquePages.filter(p => p.priority < 0.6).length}`);

  return uniquePages.length;
}

generateSitemap();
