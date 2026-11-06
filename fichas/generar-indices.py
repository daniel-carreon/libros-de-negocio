#!/usr/bin/env python3
"""Regenera fichas/INDICE.md (obra → ficha) y fichas/TEMAS.md (tema → obras → páginas)
desde el frontmatter de cada ficha. Uso: python3 fichas/generar-indices.py"""
import glob, os, re, collections

RAIZ = os.path.dirname(os.path.abspath(__file__))
ALIAS = {'economia': 'economía', 'escalabilidad': 'escalar', 'feedback': 'retroalimentación',
         'creencias': 'creencia', 'marketing': 'publicidad', 'disruption': 'innovación',
         'automatización': 'tecnología', 'aprendizaje-automático': 'ia', 'emprendimiento': 'startups'}

def frontmatter(path):
    s = open(path).read()
    fm = s.split('\n---', 1)[0]
    def campo(k):
        m = re.search(rf'^{k}:\s*(.*)$', fm, re.M)
        return m.group(1).strip().strip('"') if m else ''
    archivos = [re.sub(r'\s+#.*', '', l.strip()[1:].strip()) for l in
                re.search(r'archivos:\n((?:\s+-.*\n?)+)', fm).group(1).strip().split('\n')]
    temas = []
    m = re.search(r'temas:\n((?:\s+-.*\n?)+)', fm)
    for l in (m.group(1).strip().split('\n') if m else []):
        t, _, r = l.strip()[1:].strip().partition(':')
        t = t.strip().strip('"').lower(); t = ALIAS.get(t, t)
        temas.append((t, r.strip().strip('"')))
    aviso = re.search(r'^> Aviso:\s*(.+)$', s, re.M)
    return dict(slug=campo('slug'), titulo=campo('titulo'), autor=campo('autor'), anio=campo('anio'),
                estante=campo('estante'), paginas=campo('paginas'), idioma=campo('idioma'),
                archivos=archivos, temas=temas, aviso=aviso.group(1) if aviso else '',
                ruta=os.path.relpath(path, RAIZ))

fichas = [frontmatter(p) for p in sorted(glob.glob(os.path.join(RAIZ, '*', '*.md')))]

SIN_FICHA = [
    ('biblioteca/02-marketing-ofertas/carnegie-how-to-win-friends.pdf', 'copia idéntica de *How to Stop Worrying* (1948) con nombre equivocado → ver `08-mente-psicologia/carnegie-how-to-stop-worrying.md`'),
    ('biblioteca/04-operaciones-liderazgo/deming-out-of-the-crisis.pdf', 'copia idéntica de Micklewright, *Out of Another Crisis* (2010) → ver `04-operaciones-liderazgo/micklewright-out-of-another-crisis.md`; el Deming bueno es la edición en español: `04-operaciones-liderazgo/deming-out-of-the-crisis.md`'),
    ('biblioteca/04-operaciones-liderazgo/sloan-my-years-with-general-motors.pdf', 'copia idéntica de McDonald, *A Ghost\'s Memoir* (2002) → ver `11-biografias/mcdonald-a-ghosts-memoir.md`; el Sloan bueno es el epub: `04-operaciones-liderazgo/sloan-my-years-with-general-motors.md`'),
    ('biblioteca/04-operaciones-liderazgo/drucker-the-effective-executive.pdf', 'copia idéntica de *HBR\'s 10 Must Reads On Leadership* (2011) → ver `04-operaciones-liderazgo/hbr-on-leadership.md`; el Drucker bueno es el de 1967: `04-operaciones-liderazgo/drucker-the-effective-executive.md`'),
    ('biblioteca/03-negocio-startups/hoffman-blitzscaling.pdf', 'no es el libro: resumen de terceros de 3 páginas. *Blitzscaling* no está en la biblioteca'),
    ('biblioteca/iman-17-books-transcript.txt', 'transcripción de un video, no un libro'),
    ('biblioteca/01-cibernetica-sistemas/INDICE-CORPUS.md · biblioteca/INDICE.md', 'índices de la biblioteca, no obras'),
]

L = ['# Índice de fichas de lectura', '',
     '> Una ficha por obra: mapa para ir al libro, no sustituto. Cada ficha trae tesis, ideas por capítulo,',
     '> una cita ancla textual con su página (página **del PDF**, la del visor; en EPUB/TXT, capítulo),',
     '> un mapa «si buscas X → pp. Y–Z», conexiones y para qué le sirve a Daniel.',
     '> Generado por `fichas/generar-indices.py` desde el frontmatter; no editar a mano.', '',
     '**Para un agente:** busca por tema en `TEMAS.md`; por autor o título aquí; dentro de las fichas con',
     '`rg -n "<concepto>" fichas/` (las fichas son markdown con frontmatter YAML: `slug`, `autor`, `anio`,',
     '`archivos`, `paginas`, `temas`). Para ir al libro, abre el archivo de `archivos:` en la página citada.', '',
     f'**{len(fichas)} fichas** · {sum(len(re.findall(r"Cita ancla", open(os.path.join(RAIZ, f["ruta"])).read())) for f in fichas)} citas ancla · verificación en `VERIFICACION.md`.', '']
por_estante = collections.defaultdict(list)
for f in fichas: por_estante[f['estante']].append(f)
for e in sorted(por_estante):
    L += [f'## {e}', '', '| Obra | Año | Ficha | Archivo(s) en la biblioteca |', '|---|---|---|---|']
    for f in sorted(por_estante[e], key=lambda x: x['autor']):
        nota = ' ⚠️' if f['aviso'] else ''
        arch = '<br>'.join(f'`{a.split(" (")[0]}`' for a in f['archivos'])
        L.append(f"| {f['autor']} — *{f['titulo']}*{nota} | {f['anio']} | [{f['slug']}]({f['ruta']}) | {arch} |")
    L.append('')
L += ['## Avisos (archivo con nombre o contenido distinto al esperado)', '']
for f in fichas:
    if f['aviso']: L.append(f"- **{f['slug']}** — {f['aviso']}")
L += ['', '## Archivos sin ficha (y por qué)', '']
for a, why in SIN_FICHA: L.append(f'- `{a}` — {why}')
L.append('')
open(os.path.join(RAIZ, 'INDICE.md'), 'w').write('\n'.join(L))

temas = collections.defaultdict(list)
for f in fichas:
    for t, r in f['temas']: temas[t].append((f, r))
T = ['# Temas → obras → páginas', '',
     '> Para encontrar rápido dónde trata la biblioteca un tema. Rango = páginas del PDF (o capítulos en',
     '> EPUB/TXT) según el frontmatter `temas:` de cada ficha; el detalle fino está en el «Mapa: si buscas…»',
     '> de cada ficha. Generado por `fichas/generar-indices.py`.', '']
grandes = sorted([t for t in temas if len(temas[t]) >= 3], key=lambda t: (-len(temas[t]), t))
T.append('**Temas:** ' + ' · '.join(f'[{t}](#{t}) ({len(temas[t])})' for t in grandes))
T.append('')
for t in grandes:
    T += [f'## {t}', '']
    for f, r in sorted(temas[t], key=lambda x: x[0]['autor']):
        T.append(f"- {f['autor']}, *{f['titulo']}* ({f['anio']}) — {r} → [{f['slug']}]({f['ruta']})")
    T.append('')
T += ['## Otros temas (menos de 3 obras)', '']
for t in sorted(t for t in temas if len(temas[t]) < 3):
    T.append(f'- **{t}**: ' + '; '.join(f"[{f['slug']}]({f['ruta']}) {r}" for f, r in temas[t]))
T.append('')
open(os.path.join(RAIZ, 'TEMAS.md'), 'w').write('\n'.join(T))
print(len(fichas), 'fichas ·', len(grandes), 'temas principales ·', len(temas), 'temas en total')
