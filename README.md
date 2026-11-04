# libros-de-negocio

La biblioteca de negocio de Arbrain, en dos capas: **los libros que se entregan** dentro de la app
del alumno, y **el censo** de lo que hay, lo que falta y en qué orden se compra.

> **Por qué este repo aparte.** Convivían tres cosas distintas en un solo lugar: la biblioteca
> personal de Daniel (`casa/personal/`, con sus 60+ PDFs), los libros que se **distribuyen** con
> Arbrain y el código de Arbrain. Mezclarlos rompía dos cosas: el repo de código cargaba con
> binarios de decenas de MB en cada clon, y la biblioteca personal —que no viaja a nadie— quedaba
> a un `git add` de distancia de publicarse. Aquí viven solo los libros que se entregan y el censo
> de la biblioteca; `casa/personal/` sigue siendo la biblioteca privada, sin cambios.

## Las dos capas

| Capa | Qué es | Archivos |
|---|---|---|
| **Entregados** | Los libros completos que viajan dentro de la app, sus portadas y el manifiesto que la app lee | `libros/<slug>/`, `portadas/<slug>.webp`, `indice.json`, `INDICE.md` |
| **Censo** | Lo que existe, lo que falta, con enlaces y ediciones en español; el orden de compra; y la línea histórica de la venta | `CENSO.md`, `COMPRA.md`, `HISTORIA.md` |

Regla de oro entre las dos: **lo que está en el censo no tiene que estar en la app**. El censo es
el mapa de la biblioteca entera; `libros/` es lo que se entrega hoy.

## Qué hay

| Archivo | Qué es |
|---|---|
| `CENSO.md` | El censo por etapa del embudo (alcance, nutrición, conversión, onboarding, entrega, expansión y transversales): 69 fichas con estado, edición en español y procedencia. |
| `COMPRA.md` | La lista de compra en el orden de Daniel: *Ya · Expansión · Este mes · Después*. Donde difiere del censo, manda el suyo. |
| `HISTORIA.md` | Cómo se vende, de 1494 a 2021: qué agregó cada autor y qué pieza de hoy heredó. |
| `INDICE.md` | El catálogo de los entregados, para leer a ojo: procedencia, formato y calidad de cada archivo. |
| `indice.json` | **Manifiesto.** La app lo lee de `/libros/indice.json`. Es la única fuente de verdad del catálogo entregado. |
| `LICENCIAS.md` | Qué es de quién y qué se puede hacer con esto. |

## Cómo lo consume Arbrain

1. `arbrain/public/libros/` **es una copia** de `libros/` y `indice.json` de este repo
   (más las portadas, que ya viven en `arbrain/public/library-covers/`).
2. `LibraryOverlay.tsx` pide `/libros/indice.json` y pinta una tarjeta por libro; al abrir,
   el archivo se sirve same-origin en un iframe (`pdf` y `html`).
3. El empaquetado (`arbrain/empaquetado/generador`, allowlist) incluye `arbrain/public/libros/**`
   y esas cuatro portadas, así que llegan a la copia del alumno.

**Regla:** el manifiesto y los archivos se editan **aquí** y se copian a Arbrain. Al revés se
pierden: `arbrain/public/libros/` se regenera.

## Cómo agregar un libro

1. Elige el slug (`autor-titulo` en minúsculas, sin acentos).
2. Crea `libros/<slug>/` y mete el archivo, con el mismo nombre que la carpeta.
3. Genera la portada webp 640×357 y guárdala como `portadas/<slug>.webp`.
4. Agrega su entrada en `indice.json` **y** en `INDICE.md` (mismo orden); pásalo a ✅ en `CENSO.md`
   y bájalo de `COMPRA.md`.
5. Copia a `arbrain/public/libros/`, portada a `arbrain/public/library-covers/`, y corre
   `npx tsc --noEmit` + `npm test` en `arbrain/` antes de publicar versión.

## Formatos

- `pdf` — el original. Fiel, pero pesa y no se deja estilar.
- `html` — un solo archivo autocontenido (CSS e imágenes embebidas), generado del original
  con `pandoc --embed-resources --standalone --toc`. Es el que mejor se lee en el teléfono.
- `epub` — se queda como respaldo del original; la app lo abre con `EpubReader`.

Para generar el HTML de este repo el comando exacto es:

```bash
pandoc <fuente>.md|.epub -f markdown-tex_math_dollars -t html5 -s --toc --toc-depth=2 \
  --css=lector.css --embed-resources --standalone -o libros/<slug>/<slug>.html
```

`lector.css` es el estilo de lectura (papel claro/oscuro, serif, 40rem) y se embebe en el HTML.

**Qué se entrega, formato por libro:** Ofertas va en PDF (es el único español y pesa 4.8 MB);
Leads, Money Models y La Vía Rápida van en HTML. De Leads el repo guarda además el PDF de 21 MB
como original, pero **no viaja**: a GitHub le costaba subirlo y en el teléfono se lee peor.

## Tamaño

~47 MB en total. `hormozi-100m-leads.pdf` (21 MB) y `hormozi-100m-ofertas-ES.pdf` (4.8 MB)
son el 55 %. No hay LFS a propósito: son cuatro archivos que cambian poco y LFS complica el
build de la app; si el catálogo crece arriba de ~200 MB, se evalúa.
