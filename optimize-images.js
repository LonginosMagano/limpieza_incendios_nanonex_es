#!/usr/bin/env node

const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const projectRoot = '/home/user/limpieza_incendios_nanonex_es';

// Configuration
const QUALITY = 80;
const WEBP_QUALITY = 75;
const EXCLUDE_DIRS = ['node_modules', '.git', '.claude'];

let stats = {
  processed: 0,
  skipped: 0,
  errors: 0,
  originalSize: 0,
  compressedSize: 0,
  webpFiles: 0,
};

async function findImages(dir) {
  const images = [];
  const files = fs.readdirSync(dir);

  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      if (!EXCLUDE_DIRS.includes(file) && !file.startsWith('.')) {
        images.push(...await findImages(filePath));
      }
    } else if (/\.(jpg|jpeg|png)$/i.test(file)) {
      // Skip if already has -opt in name
      if (!file.includes('-opt')) {
        images.push(filePath);
      }
    }
  }

  return images;
}

async function optimizeImage(imagePath) {
  try {
    const ext = path.extname(imagePath).toLowerCase();
    const dir = path.dirname(imagePath);
    const basename = path.basename(imagePath, ext);
    const optimizedPath = path.join(dir, `${basename}-opt${ext}`);
    const webpPath = path.join(dir, `${basename}-opt.webp`);

    // Get original size
    const originalStat = fs.statSync(imagePath);
    const originalSize = originalStat.size;

    // Optimize original format
    const sharpInstance = sharp(imagePath);
    const metadata = await sharpInstance.metadata();

    let compressed;
    if (ext === '.png') {
      compressed = await sharpInstance
        .png({ quality: QUALITY, progressive: true })
        .toFile(optimizedPath);
    } else {
      compressed = await sharpInstance
        .jpeg({ quality: QUALITY, progressive: true })
        .toFile(optimizedPath);
    }

    // Generate WebP
    await sharp(imagePath)
      .webp({ quality: WEBP_QUALITY })
      .toFile(webpPath);

    const compressedSize = compressed.size;
    const savings = ((1 - compressedSize / originalSize) * 100).toFixed(1);

    stats.processed++;
    stats.originalSize += originalSize;
    stats.compressedSize += compressedSize;
    stats.webpFiles++;

    console.log(`✓ ${path.basename(imagePath)}`);
    console.log(`  → ${basename}-opt${ext} (${savings}% savings)`);
    console.log(`  → ${basename}-opt.webp (${(compressed.size / 1024).toFixed(1)}KB)`);

    return true;
  } catch (error) {
    stats.errors++;
    console.error(`✗ Error processing ${imagePath}: ${error.message}`);
    return false;
  }
}

async function updateHtmlReferences() {
  console.log('\n📝 Updating HTML references...');

  const htmlFiles = [];

  function findHtmlFiles(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
      const filePath = path.join(dir, file);
      const stat = fs.statSync(filePath);
      if (stat.isDirectory()) {
        if (!EXCLUDE_DIRS.includes(file) && !file.startsWith('.')) {
          findHtmlFiles(filePath);
        }
      } else if (file.endsWith('.html')) {
        htmlFiles.push(filePath);
      }
    }
  }

  findHtmlFiles(projectRoot);

  let updated = 0;
  for (const htmlFile of htmlFiles) {
    let content = fs.readFileSync(htmlFile, 'utf8');
    const originalContent = content;

    // For images without -opt, add -opt to src attributes
    content = content.replace(
      /src=['"](.*?)\.(jpg|jpeg|png)(['"'])/gi,
      (match, path, ext, quote) => {
        // Skip if already has -opt
        if (path.includes('-opt')) return match;
        return `src="${path}-opt.${ext}${quote}`;
      }
    );

    // Add picture tag support for WebP where applicable
    content = content.replace(
      /<img\s+src=['"](.*?)-opt\.(jpg|jpeg|png)['"][^>]*alt=['"](.*?)['"]/gi,
      (match, imagePath, ext, alt) => {
        const webpPath = `${imagePath}-opt.webp`;
        const srcAttr = `${imagePath}-opt.${ext}`;
        return `<picture>
    <source srcset="${webpPath}" type="image/webp">
    <img src="${srcAttr}" alt="${alt}`;
      }
    );

    // Close picture tags
    if (content.includes('<picture>')) {
      content = content.replace(/<img\s+src="[^"]*-opt\.(jpg|jpeg|png)"([^>]*)>/gi, (match) => {
        if (!match.includes('</picture>')) {
          return match.replace(/>/,  '>\n  </picture>');
        }
        return match;
      });
    }

    if (content !== originalContent) {
      fs.writeFileSync(htmlFile, content, 'utf8');
      updated++;
    }
  }

  console.log(`Updated ${updated} HTML files`);
}

async function main() {
  console.log('🖼️  Image Optimization Script\n');
  console.log(`Scanning for images in: ${projectRoot}\n`);

  const images = await findImages(projectRoot);
  console.log(`Found ${images.length} images to optimize\n`);

  for (const imagePath of images) {
    await optimizeImage(imagePath);
  }

  // Update HTML references
  await updateHtmlReferences();

  // Print summary
  console.log('\n' + '='.repeat(50));
  console.log('📊 Optimization Summary');
  console.log('='.repeat(50));
  console.log(`✓ Processed: ${stats.processed}`);
  console.log(`✗ Errors: ${stats.errors}`);
  console.log(`📦 WebP files generated: ${stats.webpFiles}`);
  console.log(`\n📉 Size Reduction:`);
  console.log(`  Original: ${(stats.originalSize / 1024 / 1024).toFixed(2)}MB`);
  console.log(`  Compressed: ${(stats.compressedSize / 1024 / 1024).toFixed(2)}MB`);
  console.log(`  Saved: ${((1 - stats.compressedSize / stats.originalSize) * 100).toFixed(1)}%`);
  console.log('='.repeat(50));
}

main().catch(console.error);
