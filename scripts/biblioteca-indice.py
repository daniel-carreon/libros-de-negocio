#!/usr/bin/env python3
"""Genera BIBLIOTECA.md a partir de los archivos de biblioteca/.

Uso:  python3 scripts/biblioteca-indice.py

Camina los 13 estantes y escribe la tabla completa (estante, archivo, formato,
peso) más el resumen. La descripción de cada estante vive en DESCRIPCIONES; si
agregas un estante, agrégalo ahí. No inventa títulos: el nombre del archivo es
la fuente.
"""

from __future__ import annotations

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BIBLIOTECA = RAIZ / "biblioteca"
SALIDA = RAIZ / "BIBLIOTECA.md"

DESCRIPCIONES = {
    "01-cibernetica-sistemas": "El corpus completo: Beer, Wiener, Ashby, Medina, Davies, Pickering.",
    "02-marketing-ofertas": "Hormozi (incluye la colección Markdown con 12 playbooks), Brunson, Cialdini, Belfort, Ogilvy, Fladlien (extracto).",
    "03-negocio-startups": "Thiel, Hoffman, Kaufman, Masterson, Martell, Ferriss.",
    "04-operaciones-liderazgo": "Womack, Wooden, Maxwell, Lencioni (extracto), Grove, Sinek x4.",
    "05-riqueza-inversion": "DeMarco, Housel, Dalio, Robbins. El zip de libro+audio queda fuera de git: 477 MB.",
    "06-productividad-foco": "Newport (Deep Work, Slow Productivity).",
    "07-cuerpo-longevidad": "Attia, Walker, Lembke, Huberman (guía de 12 págs).",
    "08-mente-psicologia": "Kahneman, Greene, Holiday, Allen, Pritchett, García Calvo, Zeland, Goggins.",
    "09-estrategia-clasicos": "Sun Tzu, dos ediciones.",
    "10-ficcion-sistemas": "Heinlein.",
    "11-biografias": "Elon Musk, en inglés y en español.",
    "12-epistemologia-frontera": "Deutsch, Kurzweil.",
    "13-historia-del-negocio": "Dominio público en EE. UU. (1532 a 1928): Maquiavelo, Smith, Franklin, Babbage, Barnum, Conwell, Le Bon, Veblen, Pacioli, Sheldon, Scott, Taylor, Esenwein y Carnagey, A. Carnegie, Ford x2, Lippmann, Hopkins x2, Lefèvre, Bernays x2. Legal de publicar.",
}

LIBRO = re.compile(r"\.(pdf|epub|mobi|azw3|djvu)$", re.I)
LECTURA = re.compile(r"\.(md|txt|html)$", re.I)


def peso(bytes_: int) -> str:
    if bytes_ >= 1024 * 1024:
        return f"{bytes_ / 1024 / 1024:.1f} MB"
    return f"{max(1, round(bytes_ / 1024))} KB"


def filas(estante: Path) -> list[tuple[str, str, int]]:
    out = []
    for f in sorted(estante.rglob("*")):
        if not f.is_file() or f.name == ".DS_Store":
            continue
        rel = f.relative_to(estante).as_posix()
        if LIBRO.search(f.suffix):
            fmt = f.suffix.lstrip(".").upper()
        elif LECTURA.search(f.suffix):
            fmt = f.suffix.lstrip(".").upper()
        else:
            fmt = f.suffix.lstrip(".").upper() or "—"
        out.append((rel, fmt, f.stat().st_size))
    return out


def main() -> None:
    estantes = sorted(p for p in BIBLIOTECA.iterdir() if p.is_dir() and not p.name.startswith("."))
    lineas = [
        "# Biblioteca completa",
        "",
        "> Generado por `scripts/biblioteca-indice.py` desde los archivos de `biblioteca/`.",
        "> No editar a mano: se regenera. El comentario de cada libro vive en `biblioteca/INDICE.md`.",
        "",
    ]

    total_libros = 0
    total_bytes = 0
    for estante in estantes:
        fs = filas(estante)
        libros = [f for f in fs if LIBRO.search(f[0])]
        total_libros += len(libros)
        total_bytes += sum(f[2] for f in fs)
        desc = DESCRIPCIONES.get(estante.name, "")
        lineas += [f"## {estante.name}", ""]
        if desc:
            lineas += [f"_{desc}_", ""]
        lineas += [f"{len(libros)} libros · {peso(sum(f[2] for f in fs))}", ""]
        lineas += ["| Archivo | Formato | Peso |", "|---|---|---|"]
        for rel, fmt, size in fs:
            lineas.append(f"| `{rel}` | {fmt} | {peso(size)} |")
        lineas.append("")

    lineas += [
        "## Resumen",
        "",
        f"- **{total_libros} libros** en {len(estantes)} estantes.",
        f"- **{peso(total_bytes)}** en total (sin el zip de libro+audio de 477 MB).",
        "- Los archivos que Arbrain entrega en la app son otros: `entregados/`.",
        "",
    ]
    SALIDA.write_text("\n".join(lineas), encoding="utf-8")
    print(f"{SALIDA.relative_to(RAIZ)}: {total_libros} libros, {peso(total_bytes)}")


if __name__ == "__main__":
    main()
