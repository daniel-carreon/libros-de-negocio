# libros-de-negocio

La biblioteca de negocio de Arbrain. Dos capas de libros y una de decisiones:

- **`biblioteca/`** — tus 13 estantes, 75 libros, lo que lees y trabajas.
- **`entregados/`** — los cuatro libros completos que viajan dentro de la app del alumno.
- **Censo** — qué existe, qué falta, en qué orden se compra y de dónde viene cada teoría.

| Ruta | Qué es |
|---|---|
| `biblioteca/<estante>/` | Los 13 estantes por campo, un archivo por libro. Es la biblioteca personal, ahora versionada y pública. |
| `biblioteca/INDICE.md` | El índice maestro original: qué hay en cada estante, qué falta y qué está descartado, con la razón. |
| `BIBLIOTECA.md` | La tabla completa, generada desde los archivos: estante, archivo, formato y peso. |
| `entregados/libros/<slug>/` | Los cuatro libros que sirve la app, completos. |
| `entregados/portadas/<slug>.webp` | Portada 640×357 (16:10), la que pinta la biblioteca de la app. |
| `entregados/indice.json` | **Manifiesto.** La app lo lee de `/libros/indice.json`. Única fuente de verdad de lo entregado. |
| `entregados/INDICE.md` | El catálogo entregado para leer a ojo: procedencia, formato y calidad de cada archivo. |
| `CENSO.md` | El censo por etapa del embudo: 69 fichas con estado, edición en español y procedencia. |
| `COMPRA.md` | La lista de compra en el orden de Daniel: *Ya · Expansión · Este mes · Después*. |
| `HISTORIA.md` | Cómo se vende, de 1494 a 2021: qué agregó cada autor y qué pieza de hoy heredó. |
| `LICENCIAS.md` | Qué es de quién y qué implica que el repo sea público. |
| `scripts/biblioteca-indice.py` | Regenera `BIBLIOTECA.md` desde `biblioteca/`. |

## Cómo se regenera el índice

```bash
python3 scripts/biblioteca-indice.py
```

Camina `biblioteca/`, cuenta y pesa; no inventa títulos: el nombre del archivo es la fuente.
La descripción de cada estante vive en el script (`DESCRIPCIONES`), para que agregar un estante
sea una línea y no una tabla escrita a mano.

## Cómo lo consume Arbrain

1. `arbrain/public/libros/` **es una copia** de `entregados/libros/` y `entregados/indice.json`
   (más las portadas, que ya viven en `arbrain/public/library-covers/`).
2. `LibraryOverlay.tsx` pide `/libros/indice.json` y pinta una tarjeta por libro; al abrir,
   el archivo se sirve same-origin en un iframe (`pdf` y `html`).
3. El empaquetado (`arbrain/empaquetado/generador`, allowlist) incluye `arbrain/public/libros/**`
   y esas cuatro portadas, así que llegan a la copia del alumno.

**Regla:** el manifiesto y los archivos se editan **aquí** y se copian a Arbrain. Al revés se
pierden: `arbrain/public/libros/` se regenera.

## Cómo agregar un libro a la biblioteca

1. Déjalo en su estante (`biblioteca/<estante>/`) con el nombre `autor-titulo` en minúsculas.
2. Corre `python3 scripts/biblioteca-indice.py` y commitea el índice regenerado.
3. Si falta el estante, agrégalo en `DESCRIPCIONES` del script y en `biblioteca/INDICE.md`.

## Cómo agregar un libro **entregado** (el que ve el alumno)

1. Elige el slug (`autor-titulo`, sin acentos).
2. Crea `entregados/libros/<slug>/` y mete el archivo, con el mismo nombre que la carpeta.
3. Genera la portada webp 640×357 en `entregados/portadas/<slug>.webp`.
4. Agrega su entrada en `entregados/indice.json` **y** en `entregados/INDICE.md` (mismo orden);
   pásalo a ✅ en `CENSO.md` y bájalo de `COMPRA.md`.
5. Copia a `arbrain/public/libros/`, portada a `arbrain/public/library-covers/`, y corre
   `npx tsc --noEmit` + `npm test` en `arbrain/` antes de publicar versión.

## Formatos

- `pdf` — el original. Fiel, pero pesa y no se deja estilar.
- `html` — un solo archivo autocontenido (CSS e imágenes embebidas), generado del original
  con `pandoc --embed-resources --standalone --toc`. Es el que mejor se lee en el teléfono.
- `epub` — respaldo del original; la app lo abre con `EpubReader`.

Para generar el HTML de los entregados el comando exacto es:

```bash
pandoc <fuente>.md|.epub -f markdown-tex_math_dollars -t html5 -s --toc --toc-depth=2 \
  --css=lector.css --embed-resources --standalone -o entregados/libros/<slug>/<slug>.html
```

`lector.css` es el estilo de lectura (papel claro/oscuro, serif, 40rem) y se embebe en el HTML.

**Qué se entrega, formato por libro:** Ofertas va en PDF (es el único español y pesa 4.8 MB);
Leads, Money Models y La Vía Rápida van en HTML. De Leads se guarda además el PDF de 21 MB en la
biblioteca, pero **no viaja**: a GitHub le costaba subirlo y en el teléfono se lee peor.

## Tamaño

~430 MB: 422 MB de biblioteca (75 libros) y 7 MB de entregados. El zip de *La Vía Rápida* con su
audiolibro (477 MB) queda fuera por `.gitignore`; el libro ya está en HTML. Todo archivo pesa
menos de 100 MB, así que no hace falta LFS. Si la biblioteca crece arriba de ~1 GB, se evalúa.

## Origen

Estos archivos vivían en `~/Developer/artificial-brain/casa/personal/libros/` (repo privado
`business-os-personal`) y no eran clonables sin acceso a esa máquina. Aquí están completos desde el
4 nov 2026, con un índice que se regenera solo.
