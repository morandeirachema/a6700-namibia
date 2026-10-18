#!/usr/bin/env bash
# Regenera los PDF de las seis hojas de campo desde su Markdown.
# Uso: ./pdf/generar.sh [nombre]   (sin argumento, las seis)
# Requiere: pandoc y Google Chrome (o Chromium), en Linux o en macOS.
set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="$(command -v google-chrome || command -v chromium || true)"
if [ -z "$CHROME" ]; then
  for app in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
             "/Applications/Chromium.app/Contents/MacOS/Chromium"; do
    [ -x "$app" ] && { CHROME="$app"; break; }
  done
fi
[ -z "$CHROME" ] && { echo "Falta Google Chrome/Chromium"; exit 1; }
command -v pandoc >/dev/null || { echo "Falta pandoc"; exit 1; }

NOMBRES="chuleta verificacion-in-situ lista-de-tomas chuleta-video cuaderno-de-composicion hojas-por-parada"

# Sin arrays asociativos: el bash 3.2 de macOS no los tiene
fuente() {
  case "$1" in
    chuleta)                 echo "a6700/chuleta.md" ;;
    verificacion-in-situ)    echo "a6700/verificacion-in-situ.md" ;;
    lista-de-tomas)          echo "plan/lista-de-tomas.md" ;;
    chuleta-video)           echo "tecnica/chuleta-video.md" ;;
    cuaderno-de-composicion) echo "plan/cuaderno-de-composicion.md" ;;
    hojas-por-parada)        echo "plan/hojas-por-parada.md" ;;
    *) echo "Hoja desconocida: $1 (son: $NOMBRES)" >&2; exit 1 ;;
  esac
}

hacer() {
  local nombre="$1" fuente; fuente="$(fuente "$1")"
  local tmp; tmp="$(mktemp -d)"
  local css=(--css=pdf/estilo.css)
  case "$nombre" in
    chuleta|chuleta-video) css+=(--css=pdf/compacto.css) ;;      # deben caber en una cara
    hojas-por-parada)      css+=(--css=pdf/una-por-pagina.css) ;; # una parada por cara
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

if [ $# -gt 0 ]; then hacer "$1"; else for n in $NOMBRES; do hacer "$n"; done; fi
