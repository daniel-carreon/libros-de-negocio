#!/usr/bin/env bash
# Sube la biblioteca en tandas, para que un push que falle no arrastre todo.
# La conexión del Studio sube a ~80 KB/s y un pack de 400 MB en un solo request
# se cae con HTTP 408; con postBuffer chico y HTTP/1.1 va en trozos y aguanta.
#
# Uso:  bash scripts/subir-biblioteca.sh
# Log:  ~/libros-subida.log

set -u
cd "$(dirname "$0")/.." || exit 1

LOG="$HOME/libros-subida.log"
GIT=(git -c user.name="Daniel Carreón" -c user.email="daniel@saasfactory.so")

di() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG"; }

empujar() {
  local intento
  for intento in 1 2 3 4 5 6; do
    if git -c http.postBuffer=1048576 -c http.version=HTTP/1.1 push origin main >>"$LOG" 2>&1; then
      di "push ok (intento $intento)"
      return 0
    fi
    di "push falló (intento $intento), reintento en 30 s"
    sleep 30
  done
  return 1
}

tanda() {
  local titulo="$1"; shift
  local rutas=("$@") pendientes=()
  local r
  for r in "${rutas[@]}"; do
    [ -e "$r" ] && pendientes+=("$r")
  done
  [ ${#pendientes[@]} -eq 0 ] && { di "tanda «$titulo»: nada nuevo"; return 0; }

  di "tanda «$titulo»: ${#pendientes[@]} rutas"
  git add -A "${pendientes[@]}" || return 1
  if git diff --cached --quiet; then
    di "tanda «$titulo»: sin cambios, se salta"
    return 0
  fi
  "${GIT[@]}" commit -q -m "$titulo

Co-Authored-By: Claude Code <noreply@anthropic.com>" || return 1
  di "commit hecho; subiendo…"
  empujar || { di "TANDA «$titulo» FALLÓ"; return 1; }
}

di "=== subida de la biblioteca ==="

tanda "Estructura: entregados/ y biblioteca/, con índice que se regenera" \
  README.md LICENCIAS.md COMPRA.md CENSO.md HISTORIA.md BIBLIOTECA.md \
  .gitignore .gitattributes scripts entregados biblioteca/INDICE.md 2>/dev/null

tanda "Biblioteca: pequeños (productividad, estrategia, ficción)" \
  biblioteca/06-productividad-foco biblioteca/09-estrategia-clasicos \
  biblioteca/10-ficcion-sistemas biblioteca/iman-17-books-transcript.txt

tanda "Biblioteca: cibernética y sistemas" biblioteca/01-cibernetica-sistemas
tanda "Biblioteca: marketing y ofertas" biblioteca/02-marketing-ofertas
tanda "Biblioteca: mente, operaciones y startups" \
  biblioteca/08-mente-psicologia biblioteca/04-operaciones-liderazgo biblioteca/03-negocio-startups
tanda "Biblioteca: riqueza y cuerpo" biblioteca/05-riqueza-inversion biblioteca/07-cuerpo-longevidad
tanda "Biblioteca: biografías y frontera" \
  biblioteca/11-biografias biblioteca/12-epistemologia-frontera
tanda "Biblioteca: historia del negocio (dominio público)" biblioteca/13-historia-del-negocio

di "=== fin: $(git log --oneline -1) ==="
