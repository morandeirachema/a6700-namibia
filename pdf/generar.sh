#!/usr/bin/env bash
# Regenera los PDF de las cuatro hojas de campo desde su Markdown.
# Uso: ./pdf/generar.sh [nombre]   (sin argumento, las cuatro)
# Requiere: pandoc y google-chrome (o chromium).
set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="$(command -v google-chrome || command -v chromium || true)"
[ -z "$CHROME" ] && { echo "Falta google-chrome/chromium"; exit 1; }

declare -A HOJAS=(
  [chuleta]="a6700/chuleta.md"
  [verificacion-in-situ]="a6700/verificacion-in-situ.md"
  [lista-de-tomas]="plan/lista-de-tomas.md"
  [chuleta-video]="tecnica/chuleta-video.md"
  [cuaderno-de-composicion]="plan/cuaderno-de-composicion.md"
)

hacer() {
  local nombre="$1" fuente="${HOJAS[$1]}"
  local tmp; tmp="$(mktemp -d)"
  local css=(--css=pdf/estilo.css)
  case "$nombre" in
    chuleta|chuleta-video) css+=(--css=pdf/compacto.css) ;;   # deben caber en una cara
  esac
  pandoc "$fuente" --standalone --embed-resources \
         "${css[@]}" --metadata title="" \
         -o "$tmp/$nombre.html"
  "$CHROME" --headless --disable-gpu --no-sandbox \
            --no-pdf-header-footer --print-to-pdf-no-header \
            --print-to-pdf="$PWD/pdf/$nombre.pdf" \
            "file://$tmp/$nombre.html" >/dev/null 2>&1
  rm -rf "$tmp"
  echo "  pdf/$nombre.pdf  ($(du -h "pdf/$nombre.pdf" | cut -f1))"
}

if [ $# -gt 0 ]; then hacer "$1"; else for n in "${!HOJAS[@]}"; do hacer "$n"; done; fi
