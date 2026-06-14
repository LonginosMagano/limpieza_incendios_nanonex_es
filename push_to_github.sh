#!/bin/bash

# ============================================================================
# SCRIPT PARA HACER PUSH AUTOMÁTICO AL REPOSITORIO GITHUB
# Nano Nex Madrid - Limpieza por Incendio SEO v2.0
# ============================================================================

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         PUSH AUTOMÁTICO - NANO NEX MADRID                    ║"
echo "║        Limpieza por Incendio SEO v2.0                        ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# 1. CLONAR REPOSITORIO (si no existe)
if [ ! -d "limpiezaincendiosnanonexmadrid" ]; then
    echo "📥 Clonando repositorio..."
    git clone https://github.com/LonginosMagano/limpiezaincendiosnanonexmadrid.git
    cd limpiezaincendiosnanonexmadrid
else
    echo "✅ Repositorio ya existe. Accediendo..."
    cd limpiezaincendiosnanonexmadrid
    git pull origin master
fi

# 2. CONFIGURAR GIT
echo ""
echo "⚙️  Configurando git..."
git config user.email "info@nano-nex.es"
git config user.name "Nano Nex Team"

# 3. COPIAR ARCHIVOS (Asegúrate de que existan en /outputs/)
echo ""
echo "📂 Copiando archivos generados..."

if [ -f "../00_COMIENZA_AQUI.md" ]; then
    cp ../00_COMIENZA_AQUI.md .
    echo "✓ 00_COMIENZA_AQUI.md"
fi

if [ -f "../PLAN_ESTRATEGICO_NANO_NEX_MADRID.md" ]; then
    cp ../PLAN_ESTRATEGICO_NANO_NEX_MADRID.md .
    echo "✓ PLAN_ESTRATEGICO_NANO_NEX_MADRID.md"
fi

if [ -f "../INSTRUCCIONES_IMPLEMENTACION.md" ]; then
    cp ../INSTRUCCIONES_IMPLEMENTACION.md .
    echo "✓ INSTRUCCIONES_IMPLEMENTACION.md"
fi

if [ -f "../RESUMEN_EJECUTIVO.md" ]; then
    cp ../RESUMEN_EJECUTIVO.md .
    echo "✓ RESUMEN_EJECUTIVO.md"
fi

if [ -f "../GBP_INFO.md" ]; then
    cp ../GBP_INFO.md .
    echo "✓ GBP_INFO.md"
fi

if [ -f "../index_v2.html" ]; then
    cp ../index_v2.html .
    echo "✓ index_v2.html"
fi

if [ -f "../.htaccess" ]; then
    cp ../.htaccess .
    echo "✓ .htaccess"
fi

if [ -f "../robots.txt" ]; then
    cp ../robots.txt .
    echo "✓ robots.txt"
fi

if [ -f "../sitemap.xml" ]; then
    cp ../sitemap.xml .
    echo "✓ sitemap.xml"
fi

if [ -f "../404.html" ]; then
    cp ../404.html .
    echo "✓ 404.html"
fi

if [ -f "../llms.txt" ]; then
    cp ../llms.txt .
    echo "✓ llms.txt"
fi

if [ -f "../TEMPLATE_BARRIO_SALAMANCA.html" ]; then
    cp ../TEMPLATE_BARRIO_SALAMANCA.html .
    echo "✓ TEMPLATE_BARRIO_SALAMANCA.html"
fi

if [ -f "../TEMPLATE_MUNICIPIO_GETAFE.html" ]; then
    cp ../TEMPLATE_MUNICIPIO_GETAFE.html .
    echo "✓ TEMPLATE_MUNICIPIO_GETAFE.html"
fi

# 4. VER STATUS
echo ""
echo "📊 Estado del repositorio:"
git status

# 5. ADD Y COMMIT
echo ""
echo "📝 Haciendo commit..."
git add -A
git commit -m "feat: SEO v2.0 - Homepage + técnica + documentación + plantillas

✅ Archivos técnicos:
   - index_v2.html: Homepage optimizada (Schema + Open Graph + botones)
   - .htaccess: HTTPS + caché + gzip + seguridad
   - robots.txt: Optimizado para Google + IA bots
   - sitemap.xml: 40+ URLs (homepage + futuros landings + blog)
   - 404.html: Página error profesional
   - llms.txt: Metadata para indexación IA

📚 Documentación:
   - 00_COMIENZA_AQUI.md: Quick start (30 min)
   - PLAN_ESTRATEGICO_NANO_NEX_MADRID.md: Estrategia 4 fases
   - INSTRUCCIONES_IMPLEMENTACION.md: Paso a paso
   - RESUMEN_EJECUTIVO.md: Qué se entregó vs qué falta
   - GBP_INFO.md: Optimización Google Business Profile

🎨 Plantillas HTML reutilizables:
   - TEMPLATE_BARRIO_SALAMANCA.html: Landing barrio (copiar 10x)
   - TEMPLATE_MUNICIPIO_GETAFE.html: Landing municipio (copiar 15x)

📊 Impacto esperado:
   - 100+ keywords posicionadas (6 meses)
   - +200-300% tráfico orgánico
   - 15-20 conversiones/semana

⏱️ Timeline:
   - FASE 1 (Core técnico): 12 horas
   - FASE 2-3 (Landings + Blog): 48 horas
   - Total: ~60 horas (1.5 semanas)

🔥 Estado: Listo para implementación"

# 6. PUSH
echo ""
echo "🚀 Haciendo push al repositorio..."
echo ""
echo "⚠️  IMPORTANTE: Se te pedirá autenticación."
echo "Usa tu Personal Access Token de GitHub como contraseña."
echo ""
echo "📖 Si no tienes token, crea uno en:"
echo "   https://github.com/settings/tokens"
echo ""

git push origin master

if [ $? -eq 0 ]; then
    echo ""
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║          ✅ PUSH COMPLETADO CON ÉXITO                        ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "✅ Repositorio actualizado:"
    echo "   https://github.com/LonginosMagano/limpiezaincendiosnanonexmadrid"
    echo ""
    echo "📋 Próximos pasos:"
    echo "   1. Revisa el repositorio en GitHub"
    echo "   2. Lee: 00_COMIENZA_AQUI.md"
    echo "   3. Implementa FASE 1 (Core técnico)"
    echo "   4. Crea 3 landings prioritarias"
    echo ""
else
    echo ""
    echo "❌ Error en el push. Verifica:"
    echo "   - Tu Personal Access Token (credenciales GitHub)"
    echo "   - Conexión a internet"
    echo "   - Permisos de escritura en el repositorio"
    echo ""
    echo "💡 Prueba manual:"
    echo "   git push origin master"
    echo ""
fi
