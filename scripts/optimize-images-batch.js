#!/usr/bin/env node

const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const inputDirs = ['./imagenes', './assets/img', '.'];
const supportedFormats = ['.jpg', '.jpeg', '.png', '.webp'];

async function optimizeImage(inputPath) {
  try {
    const ext = path.extname(inputPath).toLowerCase();
    if (!supportedFormats.includes(ext)) return null;

    const dir = path.dirname(inputPath);
    const name = path.basename(inputPath, ext);
    const outputPath = path.join(dir, `${name}-opt.webp`);

    const metadata = await sharp(inputPath).metadata();
    const isSmall = metadata.width < 500 && metadata.height < 500;

    await sharp(inputPath)
      .resize(isSmall ? 600 : 2000, isSmall ? 600 : 2000, {
        fit: 'inside',
        withoutEnlargement: true
      })
      .webp({ quality: isSmall ? 85 : 80 })
      .toFile(outputPath);

    const originalSize = fs.statSync(inputPath).size;
    const optimizedSize = fs.statSync(outputPath).size;
    const savings = ((1 - optimizedSize / originalSize) * 100).toFixed(1);

    return {
      original: inputPath,
      optimized: outputPath,
      originalSize: (originalSize / 1024).toFixed(1),
      optimizedSize: (optimizedSize / 1024).toFixed(1),
      savings: savings
    };
  } catch (err) {
    console.error(`❌ Error: ${inputPath} - ${err.message}`);
    return null;
  }
}

async function processDirectory(dir) {
  if (!fs.existsSync(dir)) return [];

  const files = fs.readdirSync(dir);
  const results = [];

  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isFile()) {
      const result = await optimizeImage(filePath);
      if (result) results.push(result);
    }
  }

  return results;
}

async function main() {
  console.log('🖼️  Iniciando optimización de imágenes con Sharp...\n');

  let totalResults = [];
  let totalSavings = 0;

  for (const dir of inputDirs) {
    if (fs.existsSync(dir)) {
      console.log(`📁 Procesando: ${dir}`);
      const results = await processDirectory(dir);
      totalResults = totalResults.concat(results);
    }
  }

  if (totalResults.length === 0) {
    console.log('ℹ️  No hay imágenes para optimizar.');
    return;
  }

  console.log('\n✅ RESULTADOS DE OPTIMIZACIÓN:\n');
  console.log('Original → Optimized | Tamaño Original | Tamaño Optimizado | Ahorro');
  console.log('-'.repeat(80));

  totalResults.forEach(r => {
    console.log(
      `${path.basename(r.original).padEnd(20)} | ${r.originalSize.padEnd(14)} KB | ${r.optimizedSize.padEnd(16)} KB | ${r.savings}%`
    );
    totalSavings += parseFloat(r.savings);
  });

  const avgSavings = (totalSavings / totalResults.length).toFixed(1);
  console.log('-'.repeat(80));
  console.log(`\n📊 Resumen: ${totalResults.length} imágenes optimizadas`);
  console.log(`💾 Ahorro promedio: ${avgSavings}%\n`);
  console.log('🎉 Optimización completada.\n');
}

main().catch(console.error);
