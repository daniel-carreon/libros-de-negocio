# Verificación de citas

> Encargo: revisar 1 de cada 10 citas contra su página en la fuente y rehacer las que fallen.
> Hecho el 6 nov 2026 por el coordinador (scripts en el área de trabajo, fuera del repo).

## Método

- **Universo:** 2926 citas ancla en 170 fichas. Muestra: la 1.ª, 11.ª, 21.ª… en orden alfabético de ficha → **293 citas** (1 de cada 10).
- **Contra el archivo original de `biblioteca/`, no contra el texto de trabajo de los lectores:**
  - PDF con capa de texto: `pdftotext -f N -l N` de la página citada.
  - PDF escaneado (Ashby *Mechanisms*, Beer *Diagnosing*, Coase, Wiener *Cybernetics*, Caples, Cialdini *Yes!*, Kennedy *Ultimate Sales Letter*, Drucker *Practice*, Peters, Hopkins *My Life*, Scott): OCR nuevo de esa página con tesseract (con corrección de rotación), tolerando ruido de OCR (similitud ≥ 0.9).
  - EPUB y TXT (sin paginación): el texto completo del archivo original; la cita debe aparecer textual. **No** se verifica que esté en el capítulo indicado, solo en el libro.
- Comparación normalizada (minúsculas, sin acentos ni puntuación, guiones de fin de línea unidos).
- Además, un validador revisa el **100 %** de las citas contra el texto de trabajo: textual completa, 6–25 palabras, página = marca de página del PDF.

## Ronda 1 — falló la muestra y se encontró la causa

- **247 de 293 OK; 46 fallaron.** Casi todas empezaban (o terminaban) con el texto real y luego se desviaban: paráfrasis o recortes por dentro de la frase.
- **Causa:** el validador que usaban los lectores aceptaba una cita si coincidían sus primeras o últimas 6–8 palabras. Era demasiado permisivo.
- **Arreglo, sobre las 2.926 citas, no solo la muestra:** validador estricto (la cita completa, o cada fragmento entre «…», textual). Salieron **594 citas no textuales (20 %)**:
  - **573** se rehicieron automáticamente: el inicio o el final anclaba el lugar exacto del libro, y se sustituyó la cita por el pasaje real de ese lugar (≤ 25 palabras, corte en fin de frase) con la página de ese pasaje. Algunas empiezan a mitad de frase.
  - **21** sin ancla: las rehicieron agentes correctores copiando una frase real del mismo capítulo o página.
- Resultado: 2.926 de 2.926 citas textuales según el validador estricto.

## Ronda 2 — muestra nueva tras el arreglo

- **289 de 293 exactas en su página del original.** Las 4 restantes son legítimas:

  - `brunson-dotcom-secrets` (p. 85): empieza en la p. citada y termina en la siguiente (cita a caballo entre páginas).
  - `greene-48-leyes-del-poder` (p. 456): cita con elisión «…»: cada fragmento está textual en la p. citada.
  - `agrawal-prediction-machines` (p. 236): cita con elisión «…»: cada fragmento está textual en la p. citada.
  - `carnegie-andrew-autobiography-1920` (cap. XXIX): cita con elisión «…»: cada fragmento está textual en el capítulo.

## Antes de la verificación (lo que ya se había corregido)

- Conexiones con slugs inventados (libros que no están en la biblioteca): reemplazadas por obras del catálogo; mínimo 3 por ficha.
- Páginas: algunos lectores anotaron números de línea o el folio impreso en vez de la página del PDF; se normalizó con la correspondencia línea→página y el desfase folio→PDF medido en las citas.
- Citas de más de 25 o menos de 6 palabras: recortadas o cambiadas.

## Límites honestos

- En EPUB/TXT se comprobó que la cita está en el libro, no que esté en el capítulo que dice la ficha.
- En los escaneos, la referencia es el OCR (no un ojo humano sobre la imagen); el OCR de Beer *Diagnosing* tuvo que rehacerse porque las páginas venían giradas 90°.
- La verificación es de **citas**. Las ideas «con palabras propias», los rangos del mapa y los temas no se verificaron contra el libro uno por uno.

## Muestra revisada (ronda 2)

| # | Ficha | Ubicación | Método | Resultado |
|---|---|---|---|---|
| 1 | ashby-design-for-a-brain | p. 15 | pdftotext de la página | OK · en p. 15 (exacta) |
| 2 | ashby-introduction-to-cybernetics | p. 2 | pdftotext de la página | OK · en p. 2 (exacta) |
| 3 | ashby-introduction-to-cybernetics | p. 110 | pdftotext de la página | OK · en p. 110 (exacta) |
| 4 | ashby-mechanisms-of-intelligence | p. 150 | ocr nuevo de la página | OK · en p. 150 (exacta) |
| 5 | beer-brain-of-the-firm | p. 52 | pdftotext de la página | OK · en p. 52 (exacta) |
| 6 | beer-brain-of-the-firm | p. 179 | pdftotext de la página | OK · en p. 179 (exacta) |
| 7 | beer-designing-freedom | p. 30 | pdftotext de la página | OK · en p. 30 (exacta) |
| 8 | beer-diagnosing-the-system | p. 70 | ocr nuevo de la página | OK · en p. 70 (exacta) |
| 9 | davies-the-unaccountability-machine | p. 6 | pdftotext de la página | OK · en p. 6 (exacta) |
| 10 | hayek-the-use-of-knowledge-in-society | p. 11 | pdftotext de la página | OK · en p. 11 (exacta) |
| 11 | medina-cybernetic-revolutionaries | p. 175 | pdftotext de la página | OK · en p. 175 (exacta) |
| 12 | pickering-the-cybernetic-brain | p. 412 | pdftotext de la página | OK · en p. 412 (exacta) |
| 13 | schumpeter-capitalism-socialism-democracy | p. 102 | pdftotext de la página | OK · en p. 102 (exacta) |
| 14 | schumpeter-capitalism-socialism-democracy | p. 185 | pdftotext de la página | OK · en p. 185 (exacta) |
| 15 | schumpeter-capitalism-socialism-democracy | p. 328 | pdftotext de la página | OK · en p. 328 (exacta) |
| 16 | wiener-cybernetics-1948 | p. 77 | ocr nuevo de la página | OK · en p. 77 (exacta) |
| 17 | wiener-human-use-of-human-beings | p. 40 | pdftotext de la página | OK · en p. 40 (exacta) |
| 18 | wiener-human-use-of-human-beings | p. 218 | pdftotext de la página | OK · en p. 218 (exacta) |
| 19 | abraham-getting-everything-you-can | p. 66 | pdftotext de la página | OK · en p. 66 (exacta) |
| 20 | abraham-getting-everything-you-can | p. 134 | pdftotext de la página | OK · en p. 134 (exacta) |
| 21 | belfort-way-of-the-wolf | p. 98 | pdftotext de la página | OK · en p. 98 (exacta) |
| 22 | bettger-how-i-raised-myself | cap. 5 | texto completo del epub (cita por capítulo) | OK · exacta |
| 23 | bettger-how-i-raised-myself | cap. 15 | texto completo del epub (cita por capítulo) | OK · exacta |
| 24 | bettger-how-i-raised-myself | cap. 25 | texto completo del epub (cita por capítulo) | OK · exacta |
| 25 | bettger-how-i-raised-myself | cap. 35 | texto completo del epub (cita por capítulo) | OK · exacta |
| 26 | brunson-dotcom-secrets | p. 85 | pdftotext de la página | justificada · empieza en la p. citada y termina en la siguiente (cita a caballo entre páginas) |
| 27 | brunson-secretos-de-experto | p. 46 | pdftotext de la página | OK · en p. 46 (exacta) |
| 28 | brunson-secretos-de-experto | p. 155 | pdftotext de la página | OK · en p. 155 (exacta) |
| 29 | brunson-traffic-secrets | p. 32 | pdftotext de la página | OK · en p. 32 (exacta) |
| 30 | brunson-traffic-secrets | p. 209 | pdftotext de la página | OK · en p. 209 (exacta) |
| 31 | brunson-traffic-secrets | p. 349 | pdftotext de la página | OK · en p. 349 (exacta) |
| 32 | caples-tested-advertising-methods | p. 58 | ocr nuevo de la página | OK · en p. 58 (exacta) |
| 33 | carnegie-how-to-win-friends | p. 5 | pdftotext de la página | OK · en p. 5 (exacta) |
| 34 | cialdini-influencia | p. 103 | pdftotext de la página | OK · en p. 103 (exacta) |
| 35 | cialdini-presuasion | p. 99 | pdftotext de la página | OK · en p. 99 (exacta) |
| 36 | cialdini-presuasion | p. 267 | pdftotext de la página | OK · en p. 267 (exacta) |
| 37 | cialdini-yes-50-ways | p. 59 | ocr nuevo de la página | OK · en p. 59 (exacta) |
| 38 | cialdini-yes-50-ways | p. 96 | ocr nuevo de la página | OK · en p. 96 (exacta) |
| 39 | cialdini-yes-50-ways | p. 137 | ocr nuevo de la página | OK · en p. 137 (exacta) |
| 40 | cialdini-yes-50-ways | p. 180 | ocr nuevo de la página | OK · en p. 180 (exacta) |
| 41 | cialdini-yes-50-ways | p. 224 | ocr nuevo de la página | OK · en p. 224 (exacta) |
| 42 | dunford-obviously-awesome | cap. 8 | texto completo del epub (cita por capítulo) | OK · exacta |
| 43 | fladlien-one-to-many | cap. 3 | texto completo del epub (cita por capítulo) | OK · exacta |
| 44 | halbert-the-boron-letters | p. 23 | pdftotext de la página | OK · en p. 23 (exacta) |
| 45 | halbert-the-boron-letters | p. 84 | pdftotext de la página | OK · en p. 84 (exacta) |
| 46 | halbert-the-boron-letters | p. 143 | pdftotext de la página | OK · en p. 143 (exacta) |
| 47 | holmes-the-ultimate-sales-machine | p. 139 | pdftotext de la página | OK · en p. 139 (exacta) |
| 48 | hormozi-100m-leads | p. 51 | pdftotext de la página | OK · en p. 51 (exacta) |
| 49 | hormozi-100m-leads | p. 226 | pdftotext de la página | OK · en p. 226 (exacta) |
| 50 | hormozi-100m-money-models | p. 17 | pdftotext de la página | OK · en p. 17 (exacta) |
| 51 | hormozi-100m-money-models | p. 103 | pdftotext de la página | OK · en p. 103 (exacta) |
| 52 | hormozi-100m-offers | p. 42 | pdftotext de la página | OK · en p. 42 (exacta) |
| 53 | hormozi-100m-offers | p. 154 | pdftotext de la página | OK · en p. 154 (exacta) |
| 54 | hormozi-playbook-branding | cap. 6 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 55 | hormozi-playbook-closing | cap. 2 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 56 | hormozi-playbook-fast-cash | cap. 2 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 57 | hormozi-playbook-goated-ads | cap. 6 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 58 | hormozi-playbook-hooks | cap. 8 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 59 | hormozi-playbook-lead-nurture | cap. 8 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 60 | hormozi-playbook-marketing-machine | Cap. 2 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 61 | hormozi-playbook-price-raise | Cap. 6 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 62 | hormozi-playbook-retention | cap. 3 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 63 | keenan-gap-selling | cap. 10 | texto completo del epub (cita por capítulo) | OK · exacta |
| 64 | keenan-gap-selling | cap. 20 | texto completo del epub (cita por capítulo) | OK · exacta |
| 65 | kennedy-magnetic-marketing | p. 140 | pdftotext de la página | OK · en p. 140 (exacta) |
| 66 | kennedy-no-bs-direct-marketing | p. 92 | pdftotext de la página | OK · en p. 92 (exacta) |
| 67 | kennedy-no-bs-direct-marketing | p. 181 | pdftotext de la página | OK · en p. 181 (exacta) |
| 68 | kennedy-the-ultimate-sales-letter | p. 45 | ocr nuevo de la página | OK · en p. 45 (exacta) |
| 69 | marshall-8020-sales-and-marketing | p. 37 | pdftotext de la página | OK · en p. 37 (exacta) |
| 70 | marshall-8020-sales-and-marketing | p. 100 | pdftotext de la página | OK · en p. 100 (exacta) |
| 71 | marshall-8020-sales-and-marketing | p. 177 | pdftotext de la página | OK · en p. 177 (exacta) |
| 72 | ogilvy-confesiones-de-un-publicitario | p. 116 | pdftotext de la página | OK · en p. 116 (exacta) |
| 73 | rackham-spin-selling | p. 6 | pdftotext de la página | OK · en p. 6 (exacta) |
| 74 | reeves-reality-in-advertising | p. 8 | pdftotext de la página | OK · en p. 8 (exacta) |
| 75 | reeves-reality-in-advertising | p. 27 | pdftotext de la página | OK · en p. 27 (exacta) |
| 76 | reeves-reality-in-advertising | p. 47 | pdftotext de la página | OK · en p. 47 (exacta) |
| 77 | reeves-reality-in-advertising | p. 71 | pdftotext de la página | OK · en p. 71 (exacta) |
| 78 | ries-trout-positioning | p. 56 | pdftotext de la página | OK · en p. 56 (exacta) |
| 79 | ries-trout-positioning | p. 187 | pdftotext de la página | OK · en p. 187 (exacta) |
| 80 | roberge-the-sales-acceleration-formula | p. 47 | pdftotext de la página | OK · en p. 47 (exacta) |
| 81 | roberge-the-sales-acceleration-formula | p. 163 | pdftotext de la página | OK · en p. 163 (exacta) |
| 82 | ross-predictable-revenue | cap. 10 | texto completo del epub (cita por capítulo) | OK · exacta |
| 83 | schwartz-breakthrough-advertising | p. 92 | pdftotext de la página | OK · en p. 92 (exacta) |
| 84 | suby-sell-like-crazy | p. 12 | pdftotext de la página | OK · en p. 12 (exacta) |
| 85 | suby-sell-like-crazy | p. 249 | pdftotext de la página | OK · en p. 249 (exacta) |
| 86 | sugarman-the-adweek-copywriting-handbook | p. 142 | pdftotext de la página | OK · en p. 142 (exacta) |
| 87 | walker-launch | p. 24 | pdftotext de la página | OK · en p. 24 (exacta) |
| 88 | walker-launch | p. 184 | pdftotext de la página | OK · en p. 184 (exacta) |
| 89 | anderson-the-bezos-letters | p. 51 | pdftotext de la página | OK · en p. 51 (exacta) |
| 90 | anderson-the-bezos-letters | p. 149 | pdftotext de la página | OK · en p. 149 (exacta) |
| 91 | baker-the-business-of-expertise | cap. 3 | texto completo del epub (cita por capítulo) | OK · exacta |
| 92 | baker-the-business-of-expertise | cap. 13 | texto completo del epub (cita por capítulo) | OK · exacta |
| 93 | blank-the-four-steps-to-the-epiphany | p. 543 | pdftotext de la página | OK · en p. 543 (exacta) |
| 94 | chen-the-cold-start-problem | cap. 6 | texto completo del epub (cita por capítulo) | OK · exacta |
| 95 | chen-the-cold-start-problem | cap. 16 | texto completo del epub (cita por capítulo) | OK · exacta |
| 96 | chen-the-cold-start-problem | cap. 26 | texto completo del epub (cita por capítulo) | OK · exacta |
| 97 | collins-good-to-great | p. 3 | pdftotext de la página | OK · en p. 3 (exacta) |
| 98 | enns-pricing-creativity | cap. 2 | texto completo del epub (cita por capítulo) | OK · exacta |
| 99 | enns-pricing-creativity | cap. 15 | texto completo del epub (cita por capítulo) | OK · exacta |
| 100 | enns-win-without-pitching | p. 34 | pdftotext de la página | OK · en p. 34 (exacta) |
| 101 | ferriss-semana-laboral-4-horas | p. 32 | pdftotext de la página | OK · en p. 32 (exacta) |
| 102 | ferriss-semana-laboral-4-horas | p. 215 | pdftotext de la página | OK · en p. 215 (exacta) |
| 103 | fitzpatrick-the-mom-test | Cap. 4 | texto completo del epub (cita por capítulo) | OK · exacta |
| 104 | gerber-the-e-myth-revisited | p. 55 | pdftotext de la página | OK · en p. 55 (exacta) |
| 105 | gerber-the-e-myth-revisited | p. 168 | pdftotext de la página | OK · en p. 168 (exacta) |
| 106 | kaufman-mba-personal | p. 102 | pdftotext de la página | OK · en p. 102 (exacta) |
| 107 | martell-buy-back-your-time | p. 8 | pdftotext de la página | OK · en p. 8 (ocr≈0.93) |
| 108 | martell-buy-back-your-time | p. 202 | pdftotext de la página | OK · en p. 202 (exacta) |
| 109 | masterson-listos-fuego-apunten | p. 46 | pdftotext de la página | OK · en p. 46 (exacta) |
| 110 | masterson-listos-fuego-apunten | p. 220 | pdftotext de la página | OK · en p. 220 (exacta) |
| 111 | masterson-listos-fuego-apunten | p. 353 | pdftotext de la página | OK · en p. 353 (exacta) |
| 112 | moore-crossing-the-chasm | p. 217 | pdftotext de la página | OK · en p. 217 (exacta) |
| 113 | osterwalder-business-model-generation | cap. 7 | texto completo del epub (cita por capítulo) | OK · exacta |
| 114 | osterwalder-business-model-generation | cap. 17 | texto completo del epub (cita por capítulo) | OK · exacta |
| 115 | ries-the-lean-startup | p. 97 | pdftotext de la página | OK · en p. 97 (exacta) |
| 116 | thiel-zero-to-one | p. 9 | pdftotext de la página | OK · en p. 9 (exacta) |
| 117 | thiel-zero-to-one | p. 105 | pdftotext de la página | OK · en p. 105 (exacta) |
| 118 | weiss-million-dollar-consulting | p. 135 | pdftotext de la página | OK · en p. 135 (exacta) |
| 119 | weiss-million-dollar-consulting | p. 356 | pdftotext de la página | OK · en p. 356 (exacta) |
| 120 | catmull-creativity-inc | p. 78 | pdftotext de la página | OK · en p. 78 (exacta) |
| 121 | deming-out-of-the-crisis | p. 40 | pdftotext de la página | OK · en p. 40 (exacta) |
| 122 | deming-out-of-the-crisis | p. 280 | pdftotext de la página | OK · en p. 280 (exacta) |
| 123 | drucker-the-effective-executive | p. 85 | pdftotext de la página | OK · en p. 85 (exacta) |
| 124 | drucker-the-practice-of-management | p. 55 | ocr nuevo de la página | OK · en p. 55 (exacta) |
| 125 | drucker-the-practice-of-management | p. 180 | ocr nuevo de la página | OK · en p. 180 (exacta) |
| 126 | drucker-the-practice-of-management | p. 299 | ocr nuevo de la página | OK · en p. 299 (exacta) |
| 127 | goldratt-la-meta | p. 33 | pdftotext de la página | OK · en p. 33 (exacta) |
| 128 | goldratt-la-meta | p. 73 | pdftotext de la página | OK · en p. 73 (exacta) |
| 129 | goldratt-la-meta | p. 130 | pdftotext de la página | OK · en p. 130 (exacta) |
| 130 | goldratt-la-meta | p. 175 | pdftotext de la página | OK · en p. 175 (exacta) |
| 131 | grove-high-output-management | p. 92 | pdftotext de la página | OK · en p. 92 (exacta) |
| 132 | grove-only-the-paranoid-survive | Cap. 1 | texto completo del epub (cita por capítulo) | OK · exacta |
| 133 | hastings-no-rules-rules | p. 8 | pdftotext de la página | OK · en p. 8 (exacta) |
| 134 | hastings-no-rules-rules | p. 212 | pdftotext de la página | OK · en p. 212 (exacta) |
| 135 | hbr-on-leadership | p. 152 | pdftotext de la página | OK · en p. 152 (exacta) |
| 136 | horowitz-the-hard-thing-about-hard-things | cap. 7 | texto completo del epub (cita por capítulo) | OK · exacta |
| 137 | lencioni-the-motive | Two Motives | texto completo del epub (cita por capítulo) | OK · exacta |
| 138 | maxwell-5-levels-of-leadership | p. 363 | pdftotext de la página | OK · en p. 363 (exacta) |
| 139 | micklewright-out-of-another-crisis | p. 130 | pdftotext de la página | OK · en p. 130 (exacta) |
| 140 | micklewright-out-of-another-crisis | p. 168 | pdftotext de la página | OK · en p. 168 (exacta) |
| 141 | micklewright-out-of-another-crisis | p. 209 | pdftotext de la página | OK · en p. 209 (exacta) |
| 142 | ohno-toyota-production-system | cap. 2 | texto completo del epub (cita por capítulo) | OK · exacta |
| 143 | peters-in-search-of-excellence | p. 149 | ocr nuevo de la página | OK · en p. 149 (exacta) |
| 144 | sinek-find-your-why | p. 32 | pdftotext de la página | OK · en p. 32 (exacta) |
| 145 | sinek-leaders-eat-last | p. 50 | pdftotext de la página | OK · en p. 50 (exacta) |
| 146 | sinek-leaders-eat-last | p. 148 | pdftotext de la página | OK · en p. 148 (exacta) |
| 147 | sinek-leaders-eat-last | p. 249 | pdftotext de la página | OK · en p. 249 (exacta) |
| 148 | sinek-start-with-why | p. 140 | pdftotext de la página | OK · en p. 140 (exacta) |
| 149 | sinek-the-infinite-game | p. 35 | pdftotext de la página | OK · en p. 35 (exacta) |
| 150 | sinek-the-infinite-game | p. 173 | pdftotext de la página | OK · en p. 173 (exacta) |
| 151 | sloan-my-years-with-general-motors | Cap. 8 | texto completo del epub (cita por capítulo) | OK · exacta |
| 152 | sloan-my-years-with-general-motors | Cap. 18 | texto completo del epub (cita por capítulo) | OK · exacta |
| 153 | voss-never-split-the-difference | cap. 4 | texto completo del epub (cita por capítulo) | OK · exacta |
| 154 | womack-lean-thinking | p. 47 | pdftotext de la página | OK · en p. 47 (exacta) |
| 155 | womack-lean-thinking | p. 365 | pdftotext de la página | OK · en p. 365 (exacta) |
| 156 | wooden-on-leadership | p. 98 | pdftotext de la página | OK · en p. 98 (exacta) |
| 157 | wooden-on-leadership | p. 98 | pdftotext de la página | OK · en p. 98 (exacta) |
| 158 | buffett-the-essays-of-warren-buffett | p. 64 | pdftotext de la página | OK · en p. 64 (exacta) |
| 159 | buffett-the-essays-of-warren-buffett | p. 125 | pdftotext de la página | OK · en p. 125 (exacta) |
| 160 | buffett-the-essays-of-warren-buffett | p. 173 | pdftotext de la página | OK · en p. 173 (exacta) |
| 161 | dalio-nuevo-orden-mundial | p. 184 | pdftotext de la página | OK · en p. 184 (exacta) |
| 162 | dalio-principios | p. 9 | pdftotext de la página | OK · en p. 9 (exacta) |
| 163 | dalio-principios | p. 194 | pdftotext de la página | OK · en p. 194 (exacta) |
| 164 | dalio-principios | p. 422 | pdftotext de la página | OK · en p. 422 (exacta) |
| 165 | demarco-millionaire-fastlane | Preface | texto completo del epub (cita por capítulo) | OK · exacta |
| 166 | demarco-millionaire-fastlane | Cap. 10 | texto completo del epub (cita por capítulo) | OK · exacta |
| 167 | demarco-millionaire-fastlane | Cap. 20 | texto completo del epub (cita por capítulo) | OK · exacta |
| 168 | demarco-millionaire-fastlane | Cap. 31 | texto completo del epub (cita por capítulo) | OK · exacta |
| 169 | demarco-millionaire-fastlane | Cap. 41 | texto completo del epub (cita por capítulo) | OK · exacta |
| 170 | graham-the-intelligent-investor | p. 92 | pdftotext de la página | OK · en p. 92 (exacta) |
| 171 | graham-the-intelligent-investor | p. 351 | pdftotext de la página | OK · en p. 351 (exacta) |
| 172 | hill-grow-rich-with-peace-of-mind | p. 44 | pdftotext de la página | OK · en p. 44 (exacta) |
| 173 | hill-grow-rich-with-peace-of-mind | p. 171 | pdftotext de la página | OK · en p. 171 (exacta) |
| 174 | hill-think-and-grow-rich | p. 144 | pdftotext de la página | OK · en p. 144 (exacta) |
| 175 | hill-think-and-grow-rich | p. 420 | pdftotext de la página | OK · en p. 420 (exacta) |
| 176 | housel-psicologia-del-dinero | p. 82 | pdftotext de la página | OK · en p. 82 (exacta) |
| 177 | housel-psicologia-del-dinero | p. 175 | pdftotext de la página | OK · en p. 175 (exacta) |
| 178 | naval-the-almanack | p. 72 | pdftotext de la página | OK · en p. 72 (exacta) |
| 179 | naval-the-almanack | p. 112 | pdftotext de la página | OK · en p. 112 (exacta) |
| 180 | robbins-money-master-the-game | p. 173 | pdftotext de la página | OK · en p. 173 (exacta) |
| 181 | newport-deep-work | p. 65 | pdftotext de la página | OK · en p. 65 (exacta) |
| 182 | newport-slow-productivity | p. 131 | pdftotext de la página | OK · en p. 131 (exacta) |
| 183 | attia-outlive | p. 205 | pdftotext de la página | OK · en p. 205 (exacta) |
| 184 | huberman-daily-blueprint | p. 5 | pdftotext de la página | OK · en p. 5 (exacta) |
| 185 | lembke-dopamine-nation | p. 94 | pdftotext de la página | OK · en p. 94 (exacta) |
| 186 | walker-why-we-sleep | p. 92 | pdftotext de la página | OK · en p. 92 (exacta) |
| 187 | walker-why-we-sleep | p. 286 | pdftotext de la página | OK · en p. 286 (exacta) |
| 188 | carnegie-how-to-stop-worrying | p. 28 | pdftotext de la página | OK · en p. 28 (exacta) |
| 189 | carnegie-how-to-stop-worrying | p. 81 | pdftotext de la página | OK · en p. 81 (exacta) |
| 190 | carnegie-how-to-stop-worrying | p. 131 | pdftotext de la página | OK · en p. 131 (exacta) |
| 191 | garcia-calvo-la-voz-de-tu-alma | p. 34 | pdftotext de la página | OK · en p. 34 (exacta) |
| 192 | garcia-calvo-la-voz-de-tu-alma | p. 122 | pdftotext de la página | OK · en p. 122 (exacta) |
| 193 | goggins-no-me-puedes-lastimar | p. 74 | pdftotext de la página | OK · en p. 74 (exacta) |
| 194 | greene-maestria | p. 14 | pdftotext de la página | OK · en p. 14 (exacta) |
| 195 | holiday-el-ego-es-el-enemigo | p. 43 | pdftotext de la página | OK · en p. 43 (exacta) |
| 196 | holiday-el-ego-es-el-enemigo | p. 98 | pdftotext de la página | OK · en p. 98 (exacta) |
| 197 | holiday-el-ego-es-el-enemigo | p. 156 | pdftotext de la página | OK · en p. 156 (exacta) |
| 198 | kahneman-pensar-rapido-pensar-despacio | p. 95 | pdftotext de la página | OK · en p. 95 (exacta) |
| 199 | kahneman-pensar-rapido-pensar-despacio | p. 189 | pdftotext de la página | OK · en p. 189 (exacta) |
| 200 | kahneman-pensar-rapido-pensar-despacio | p. 301 | pdftotext de la página | OK · en p. 301 (exacta) |
| 201 | pritchett-tu-al-cuadrado | p. 6 | pdftotext de la página | OK · en p. 6 (exacta) |
| 202 | pritchett-tu-al-cuadrado | p. 30 | pdftotext de la página | OK · en p. 30 (exacta) |
| 203 | ray-la-ciencia-del-exito | p. 82 | pdftotext de la página | OK · en p. 82 (exacta) |
| 204 | zeland-reality-transurfing | p. 76 | pdftotext de la página | OK · en p. 76 (exacta) |
| 205 | christensen-the-innovators-dilemma | p. 113 | pdftotext de la página | OK · en p. 113 (exacta) |
| 206 | greene-48-leyes-del-poder | p. 63 | pdftotext de la página | OK · en p. 63 (exacta) |
| 207 | greene-48-leyes-del-poder | p. 145 | pdftotext de la página | OK · en p. 145 (exacta) |
| 208 | greene-48-leyes-del-poder | p. 231 | pdftotext de la página | OK · en p. 231 (exacta) |
| 209 | greene-48-leyes-del-poder | p. 353 | pdftotext de la página | OK · en p. 353 (exacta) |
| 210 | greene-48-leyes-del-poder | p. 456 | pdftotext de la página | justificada · cita con elisión «…»: cada fragmento está textual en la p. citada |
| 211 | helmer-7-powers | cap. 5 | texto completo del epub (cita por capítulo) | OK · exacta |
| 212 | maquiavelo-del-arte-de-la-guerra | p. 83 | pdftotext de la página | OK · en p. 83 (exacta) |
| 213 | parker-platform-revolution | p. 99 | pdftotext de la página | OK · en p. 99 (exacta) |
| 214 | porter-competitive-strategy | p. 142 | pdftotext de la página | OK · en p. 142 (exacta) |
| 215 | porter-competitive-strategy | p. 383 | pdftotext de la página | OK · en p. 383 (exacta) |
| 216 | rumelt-good-strategy-bad-strategy | p. 50 | pdftotext de la página | OK · en p. 50 (exacta) |
| 217 | rumelt-good-strategy-bad-strategy | p. 99 | pdftotext de la página | OK · en p. 99 (exacta) |
| 218 | heinlein-stranger-in-a-strange-land | p. 80 | pdftotext de la página | OK · en p. 80 (exacta) |
| 219 | heinlein-stranger-in-a-strange-land | p. 182 | pdftotext de la página | OK · en p. 182 (exacta) |
| 220 | heinlein-stranger-in-a-strange-land | p. 292 | pdftotext de la página | OK · en p. 292 (exacta) |
| 221 | chernow-titan | p. 25 | pdftotext de la página | OK · en p. 25 (exacta) |
| 222 | chernow-titan | p. 270 | pdftotext de la página | OK · en p. 270 (exacta) |
| 223 | chernow-titan | p. 557 | pdftotext de la página | OK · en p. 557 (exacta) |
| 224 | chernow-titan | p. 844 | pdftotext de la página | OK · en p. 844 (exacta) |
| 225 | isaacson-elon-musk | p. 154 | pdftotext de la página | OK · en p. 154 (exacta) |
| 226 | isaacson-steve-jobs | p. 38 | pdftotext de la página | OK · en p. 38 (exacta) |
| 227 | isaacson-steve-jobs | p. 92 | pdftotext de la página | OK · en p. 92 (exacta) |
| 228 | isaacson-steve-jobs | p. 169 | pdftotext de la página | OK · en p. 169 (exacta) |
| 229 | isaacson-steve-jobs | p. 243 | pdftotext de la página | OK · en p. 243 (exacta) |
| 230 | isaacson-steve-jobs | p. 313 | pdftotext de la página | OK · en p. 313 (exacta) |
| 231 | knight-shoe-dog | p. 244 | pdftotext de la página | OK · en p. 244 (exacta) |
| 232 | kroc-grinding-it-out | p. 110 | pdftotext de la página | OK · en p. 110 (exacta) |
| 233 | kroc-grinding-it-out | p. 221 | pdftotext de la página | OK · en p. 221 (exacta) |
| 234 | mcdonald-a-ghosts-memoir | p. 208 | pdftotext de la página | OK · en p. 208 (exacta) |
| 235 | stone-the-everything-store | p. 344 | pdftotext de la página | OK · en p. 344 (exacta) |
| 236 | walton-made-in-america | p. 31 | pdftotext de la página | OK · en p. 31 (exacta) |
| 237 | walton-made-in-america | p. 142 | pdftotext de la página | OK · en p. 142 (exacta) |
| 238 | agrawal-power-and-prediction | cap. 8 | texto completo del epub (cita por capítulo) | OK · exacta |
| 239 | agrawal-power-and-prediction | cap. 18 | texto completo del epub (cita por capítulo) | OK · exacta |
| 240 | agrawal-prediction-machines | p. 113 | pdftotext de la página | OK · en p. 113 (exacta) |
| 241 | agrawal-prediction-machines | p. 236 | pdftotext de la página | justificada · cita con elisión «…»: cada fragmento está textual en la p. citada |
| 242 | brynjolfsson-the-second-machine-age | cap. 10 | texto completo del epub (cita por capítulo) | OK · exacta |
| 243 | carreon-como-se-construye-una-mente | cap. 5 | texto completo del epub (cita por capítulo) | OK · exacta |
| 244 | carreon-como-se-construye-una-mente | cap. 15 | texto completo del epub (cita por capítulo) | OK · exacta |
| 245 | carreon-como-se-construye-una-mente | cap. 25 | texto completo del epub (cita por capítulo) | OK · exacta |
| 246 | deutsch-beginning-of-infinity | p. 180 | pdftotext de la página | OK · en p. 180 (exacta) |
| 247 | deutsch-beginning-of-infinity | p. 474 | pdftotext de la página | OK · en p. 474 (exacta) |
| 248 | mollick-co-intelligence | cap. 9 | texto completo del epub (cita por capítulo) | OK · exacta |
| 249 | babbage-economy-of-machinery-1832 | cap. 8 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 250 | babbage-economy-of-machinery-1832 | cap. 18 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 251 | babbage-economy-of-machinery-1832 | cap. 28 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 252 | barnum-the-art-of-money-getting-1880 | cap. 3 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 253 | barnum-the-art-of-money-getting-1880 | cap. 13 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 254 | bernays-crystallizing-public-opinion-1923 | cap. 3 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 255 | bernays-crystallizing-public-opinion-1923 | cap. 13 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 256 | bernays-propaganda-1928 | p. 139 | pdftotext de la página | OK · en p. 139 (exacta) |
| 257 | carnegie-andrew-autobiography-1920 | cap. X | texto completo del archivo (cita por capítulo) | OK · exacta |
| 258 | carnegie-andrew-autobiography-1920 | cap. XX | texto completo del archivo (cita por capítulo) | OK · exacta |
| 259 | carnegie-andrew-autobiography-1920 | cap. XXIX | texto completo del archivo (cita por capítulo) | justificada · cita con elisión «…»: cada fragmento está textual en el capítulo |
| 260 | conwell-acres-of-diamonds-1890 | cap. 3 Bio | texto completo del archivo (cita por capítulo) | OK · exacta |
| 261 | esenwein-carnagey-art-of-public-speaking-1915 | cap. 2 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 262 | esenwein-carnagey-art-of-public-speaking-1915 | cap. 12 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 263 | esenwein-carnagey-art-of-public-speaking-1915 | cap. 22 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 264 | esenwein-carnagey-art-of-public-speaking-1915 | Apéndices | texto completo del archivo (cita por capítulo) | OK · exacta |
| 265 | ford-my-life-and-work-1922 | cap. IX | texto completo del archivo (cita por capítulo) | OK · exacta |
| 266 | ford-my-life-and-work-1922 | cap. XIX | texto completo del archivo (cita por capítulo) | OK · exacta |
| 267 | ford-today-and-tomorrow-1926 | p. 121 | pdftotext de la página | OK · en p. 121 (exacta) |
| 268 | ford-today-and-tomorrow-1926 | p. 235 | pdftotext de la página | OK · en p. 235 (exacta) |
| 269 | franklin-autobiography-1791 | cap. VI | texto completo del archivo (cita por capítulo) | OK · exacta |
| 270 | franklin-autobiography-1791 | cap. XVI | texto completo del archivo (cita por capítulo) | OK · exacta |
| 271 | hopkins-my-life-in-advertising-1927 | p. 94 | ocr nuevo de la página | OK · en p. 94 (exacta) |
| 272 | hopkins-my-life-in-advertising-1927 | p. 204 | ocr nuevo de la página | OK · en p. 204 (exacta) |
| 273 | hopkins-scientific-advertising-1923 | p. 51 | pdftotext de la página | OK · en p. 51 (exacta) |
| 274 | hopkins-scientific-advertising-1923 | p. 105 | pdftotext de la página | OK · en p. 105 (exacta) |
| 275 | le-bon-the-crowd-1895 | cap. 3 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 276 | lefevre-reminiscences-1923 | cap. 8 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 277 | lefevre-reminiscences-1923 | cap. 18 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 278 | lippmann-public-opinion-1922 | cap. 4 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 279 | lippmann-public-opinion-1922 | cap. 14 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 280 | lippmann-public-opinion-1922 | cap. 24 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 281 | machiavelli-the-prince-1532 | cap. 6 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 282 | machiavelli-the-prince-1532 | cap. 16 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 283 | machiavelli-the-prince-1532 | cap. 26 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 284 | pacioli-geijsbeek-double-entry-1914 | p. 91 | pdftotext de la página | OK · en p. 91 (exacta) |
| 285 | scott-the-psychology-of-advertising-1908 | p. 120 | ocr nuevo de la página | OK · en p. 120 (exacta) |
| 286 | sheldon-science-of-salesmanship-1906 | p. 61 | pdftotext de la página | OK · en p. 61 (exacta) |
| 287 | sheldon-science-of-salesmanship-1906 | p. 412 | pdftotext de la página | OK · en p. 412 (exacta) |
| 288 | smith-the-wealth-of-nations-1776 | cap. 8 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 289 | smith-the-wealth-of-nations-1776 | lib. II, cap. 3 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 290 | smith-the-wealth-of-nations-1776 | lib. IV, cap. 4 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 291 | smith-the-wealth-of-nations-1776 | lib. V, cap. 2 | texto completo del archivo (cita por capítulo) | OK · exacta |
| 292 | taylor-principles-of-scientific-management-1911 | cap. 2, «Transition» | texto completo del archivo (cita por capítulo) | OK · exacta |
| 293 | veblen-the-theory-of-the-leisure-class-1899 | cap. 9 | texto completo del archivo (cita por capítulo) | OK · exacta |
