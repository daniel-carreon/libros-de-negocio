# Índice de libros

Catálogo para leer a ojo. La versión de máquina es `indice.json`; si cambias uno, cambias el otro.

| # | Libro | Autor | Idioma | Formato de lectura | Peso | Origen |
|---|---|---|---|---|---|---|
| 1 | **$100M Ofertas** — cómo hacer ofertas tan buenas que la gente se sienta tonta diciendo que no | Alex Hormozi | ES | PDF | 4.8 MB | `casa/personal/libros/02-marketing-ofertas/hormozi-100m-ofertas-ES.pdf` |
| 2 | **$100M Leads** — cómo lograr que extraños quieran comprarte | Alex Hormozi | EN | HTML (21 MB el PDF de origen) | 533 KB | Markdown del repo `jabjab42/hormozi-books` → pandoc; el PDF original vive en `casa/personal/libros/02-marketing-ofertas/` |
| 3 | **$100M Money Models** — ofertas de atracción, upsell, downsell y continuidad | Alex Hormozi | EN | HTML | 336 KB | Markdown convertido del PDF (`hormozi-markdown/fuentes/`) → pandoc |
| 4 | **La Vía Rápida del Millonario** | MJ DeMarco | ES | HTML | 820 KB | Edición en español del 19 oct (zip `demarco-millionaire-fastlane-ES-libro-y-audio`) → pandoc |

## Procedencia y calidad de cada archivo

**1 · $100M Ofertas (ES).** PDF traducido automáticamente (lleva la marca «Machine Translated by
Google» en la primera página). Se lee bien; los cortes de línea del traductor aparecen de vez en
cuando. Es el único español que existe: el original en inglés está en la biblioteca personal como
markdown (`$100 m offers...md`), no se distribuye.

**2 · $100M Leads (EN).** Markdown del mismo repo público de terceros que Money Models
(`jabjab42/hormozi-books`, commit `46b7158`, bajado el 26 sep 2026) convertido a HTML con pandoc.
Trae las descripciones de imagen que hizo esa IA, con el mismo aviso de cotejo. **El HTML es lo que
se entrega**: el PDF de 21 MB tardaba demasiado en subir a GitHub (HTTP 408 en `git push`) y en el
teléfono se lee peor. El PDF y el EPUB originales siguen en la biblioteca personal como fuente.

**3 · $100M Money Models (EN).** No existe PDF en la biblioteca, solo el markdown que salió del
repo público `jabjab42/hormozi-books` (commit `46b7158`, bajado el 26 sep 2026). Ojo: esa
conversión la hizo una IA desde el PDF y **inventa descripciones de imágenes y rompe algunas
tablas**. Se limpió el bloque de «Icons representing money concepts» del inicio; el resto se
respeta. Para citar textual en video o copy, cotejar contra el PDF original del libro.

**4 · La Vía Rápida del Millonario (ES).** Edición traducida completa (portada, 49 capítulos y
audiolibro) que llegó el 19 oct 2026. Del zip se toma el markdown y de ahí el HTML; el EPUB
también se guarda. El audiolibro (23 GB de mp3) **no** vive aquí: está en `casa/personal/audiolibros/`.

## Portadas

`portadas/<slug>.webp` — 640×357 (16:10), entre 12 y 19 KB. Se generaron el 3 nov 2026 para la
biblioteca de Arbrain y son las mismas que sirve la app desde `arbrain/public/library-covers/`.

## Reglas

- Un libro por carpeta, misma base de nombre que la carpeta.
- El orden de este índice es el orden en que la app los muestra.
- Nada de `.zip` ni audios aquí: solo lo que se lee.
