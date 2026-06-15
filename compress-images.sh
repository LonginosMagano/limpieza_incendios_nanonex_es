#!/bin/bash
################################################################################
# SCRIPT DE COMPRESIÓN DE IMÁGENES - NANO NEX
# Optimiza las 3 imágenes críticas para PageSpeed
# Requisitos: cwebp, convert (ImageMagick), ffmpeg O usar TinyPNG online
################################################################################

set -e

REPO="/home/user/limpiezaincendiosnanonexmadrid"
cd "$REPO"

echo "======================================================================"
echo "COMPRESIÓN DE IMÁGENES - NANO NEX LIMPIEZA INCENDIOS"
echo "======================================================================"
echo ""

# Verificar herramientas disponibles
check_tools() {
    echo "🔍 Verificando herramientas disponibles..."
    
    if command -v cwebp &> /dev/null; then
        echo "   ✅ cwebp encontrado"
        HAVE_CWEBP=1
    else
        echo "   ❌ cwebp NO encontrado (requerido)"
        HAVE_CWEBP=0
    fi
    
    if command -v convert &> /dev/null; then
        echo "   ✅ ImageMagick (convert) encontrado"
        HAVE_CONVERT=1
    else
        echo "   ❌ ImageMagick NO encontrado"
        HAVE_CONVERT=0
    fi
    
    if command -v ffmpeg &> /dev/null; then
        echo "   ✅ ffmpeg encontrado"
        HAVE_FFMPEG=1
    else
        echo "   ❌ ffmpeg NO encontrado"
        HAVE_FFMPEG=0
    fi
    
    echo ""
}

# Comprimir imagen WebP
compress_webp() {
    local input="$1"
    local output="$2"
    local quality="${3:-80}"
    
    if [ ! -f "$input" ]; then
        echo "   ❌ Archivo no encontrado: $input"
        return 1
    fi
    
    if [ $HAVE_CWEBP -eq 1 ]; then
        echo "   ⏳ Comprimiendo con cwebp (quality=$quality)..."
        cwebp -q "$quality" "$input" -o "$output"
        local original_size=$(du -h "$input" | cut -f1)
        local new_size=$(du -h "$output" | cut -f1)
        echo "   ✅ $original_size → $new_size"
        return 0
    elif [ $HAVE_FFMPEG -eq 1 ]; then
        echo "   ⏳ Comprimiendo con ffmpeg (quality=$quality)..."
        ffmpeg -i "$input" -q:image "$quality" "$output" -y &>/dev/null
        local original_size=$(du -h "$input" | cut -f1)
        local new_size=$(du -h "$output" | cut -f1)
        echo "   ✅ $original_size → $new_size"
        return 0
    else
        echo "   ❌ No hay herramientas de compresión WebP disponibles"
        return 1
    fi
}

# Convertir PNG a WebP
convert_png_to_webp() {
    local input="$1"
    local output="$2"
    local quality="${3:-85}"
    
    if [ ! -f "$input" ]; then
        echo "   ❌ Archivo no encontrado: $input"
        return 1
    fi
    
    if [ $HAVE_CWEBP -eq 1 ]; then
        echo "   ⏳ Convirtiendo PNG → WebP (quality=$quality)..."
        cwebp -q "$quality" "$input" -o "$output"
        local original_size=$(du -h "$input" | cut -f1)
        local new_size=$(du -h "$output" | cut -f1)
        echo "   ✅ PNG ($original_size) → WebP ($new_size)"
        return 0
    else
        echo "   ❌ cwebp no disponible para conversión PNG"
        return 1
    fi
}

# Redimensionar imagen
resize_image() {
    local input="$1"
    local width="$2"
    local height="$3"
    local output="$4"
    
    if [ ! -f "$input" ]; then
        echo "   ❌ Archivo no encontrado: $input"
        return 1
    fi
    
    if [ $HAVE_CONVERT -eq 1 ]; then
        echo "   ⏳ Redimensionando a ${width}x${height}..."
        convert "$input" -resize "${width}x${height}!" "$output"
        echo "   ✅ Redimensionado: $output"
        return 0
    else
        echo "   ❌ ImageMagick no disponible para redimensionar"
        return 1
    fi
}

################################################################################
# IMAGEN 1: Limpieza-de-Incendios-Restaurantes.webp (LCP)
################################################################################

echo "📊 IMAGEN 1: Limpieza-de-Incendios-Restaurantes.webp"
echo "   Tamaño actual: 113.8 KiB"
echo "   Objetivo: 39.5 KiB"
echo "   Ahorro estimado: 74.3 KiB"
echo ""

if compress_webp "Limpieza-de-Incendios-Restaurantes.webp" "Limpieza-de-Incendios-Restaurantes-opt.webp" 75; then
    echo "   💾 Optimización completa"
    echo "   📝 PRÓXIMO PASO: Reemplazar archivo original"
    echo "   mv Limpieza-de-Incendios-Restaurantes-opt.webp Limpieza-de-Incendios-Restaurantes.webp"
else
    echo "   ⚠️ Usar TinyPNG: https://tinypng.com/"
fi
echo ""

################################################################################
# IMAGEN 2: Logo Nano Nex.png
################################################################################

echo "📊 IMAGEN 2: Logo Nano Nex.png"
echo "   Tamaño actual: 38.7 KiB"
echo "   Objetivos:"
echo "   - Convertir a WebP: 38.7 → ~10 KiB (ahorro 28.7 KiB)"
echo "   - Versión móvil (342x88): ~3-5 KiB"
echo "   Ahorro total: ~30-35 KiB"
echo ""

if convert_png_to_webp "Logo Nano Nex.png" "Logo-Nano-Nex.webp" 85; then
    echo "   ✅ WebP creado"
    
    if resize_image "Logo Nano Nex.png" 342 88 "Logo-Nano-Nex-mobile.png"; then
        if convert_png_to_webp "Logo-Nano-Nex-mobile.png" "Logo-Nano-Nex-mobile.webp" 85; then
            echo "   ✅ Versión móvil WebP creada"
        fi
    fi
else
    echo "   ⚠️ Usar TinyPNG: https://tinypng.com/"
fi
echo ""

################################################################################
# IMAGEN 3: Limpieza-de-Escombros-4.webp
################################################################################

echo "📊 IMAGEN 3: Limpieza-de-Escombros-4.webp"
echo "   Tamaño actual: 25.4 KiB"
echo "   Objetivo: 7.9 KiB"
echo "   Ahorro estimado: 17.5 KiB"
echo ""

if compress_webp "Limpieza-de-Escombros-4.webp" "Limpieza-de-Escombros-4-opt.webp" 80; then
    echo "   💾 Optimización completa"
    echo "   📝 PRÓXIMO PASO: Reemplazar archivo original"
    echo "   mv Limpieza-de-Escombros-4-opt.webp Limpieza-de-Escombros-4.webp"
else
    echo "   ⚠️ Usar TinyPNG: https://tinypng.com/"
fi
echo ""

################################################################################
# RESUMEN
################################################################################

echo "======================================================================"
echo "📈 RESUMEN DE COMPRESIÓN"
echo "======================================================================"
echo ""
echo "Archivos optimizados generados:"
ls -lh *-opt.webp *-mobile.webp 2>/dev/null || echo "   (Pendiente: ejecutar localmente)"
echo ""
echo "Ahorro total estimado: 81+ KiB"
echo "PageSpeed Score estimado: +30-35 puntos"
echo "LCP mejorado: ~50%"
echo ""
echo "PRÓXIMOS PASOS:"
echo "1. Reemplazar archivos originales con versiones optimizadas"
echo "2. Actualizar index.html con picture elements para srcset"
echo "3. Hacer git commit y push"
echo "4. Validar en PageSpeed Insights (24h después)"
echo ""
echo "======================================================================"

