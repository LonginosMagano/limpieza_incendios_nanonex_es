const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const imageDirs = ['imagenes', 'assets/img'];
const supportedFormats = ['.jpg', '.jpeg', '.png', '.webp'];

async function optimizeImages() {
  for (const dir of imageDirs) {
    const fullPath = path.join(__dirname, '..', dir);

    if (!fs.existsSync(fullPath)) {
      console.log(`Directorio no encontrado: ${fullPath}`);
      continue;
    }

    const files = fs.readdirSync(fullPath);

    for (const file of files) {
      const ext = path.extname(file).toLowerCase();
      if (!supportedFormats.includes(ext)) continue;

      const inputPath = path.join(fullPath, file);
      const outputPath = path.join(fullPath, `optimized-${file}`);

      try {
        await sharp(inputPath)
          .resize(2000, 2000, {
            fit: 'inside',
            withoutEnlargement: true
          })
          .webp({ quality: 80 })
          .toFile(outputPath.replace(/\.[^.]+$/, '.webp'));

        console.log(`✅ Optimizada: ${file}`);
      } catch (error) {
        console.error(`❌ Error optimizando ${file}: ${error.message}`);
      }
    }
  }
}

optimizeImages().catch(console.error);
