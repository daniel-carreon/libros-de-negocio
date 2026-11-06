---
slug: wiener-cybernetics-1948
titulo: "Cybernetics: or Control and Communication in the Animal and the Machine"
titulo_es: ""
autor: "Norbert Wiener"
anio: 1948
edicion: "Second Edition, The M.I.T. Press, Cambridge, Massachusetts; Copyright © 1948 and 1961; Fourth Printing, 1985; First MIT Press paperback edition, February 1965; ISBN 0-262-23007-0 (hard), 0-262-73009-X (paper); inglés"
estante: 01-cibernetica-sistemas
archivos:
  - biblioteca/01-cibernetica-sistemas/wiener-cybernetics-1948.pdf
paginas: 231
citar_por: "página del PDF"
idioma: en
temas:
  - cibernética: pp. 6–231
  - sistemas: pp. 6–231
  - información: pp. 78–107
  - retroalimentación: pp. 114–130
  - máquinas-de-computación: pp. 135–150
  - organización: pp. 174–185
  - aprendizaje-automático: pp. 188–196
  - control: pp. 6–231
---

# Norbert Wiener — *Cybernetics: or Control and Communication in the Animal and the Machine* (1948)

> Ficha de lectura: mapa para ir al libro, no sustituto. Páginas = número de página **del PDF**
> (el que muestra el visor, no el impreso).

## Tesis en tres líneas

1. La retroalimentación es el mecanismo universal por el cual máquinas y organismos vivos regulan su comportamiento, compensando desviaciones mediante información continua del resultado de sus acciones.
2. La información tiene estructura matemática medible (negativa de entropía), y su transmisión, control y procesamiento forman una disciplina unificada aplicable a ingeniería, biología, psicología y sociedad.
3. Máquinas digitales pueden replicar funciones del sistema nervioso mediante retroalimentación negativa y circuitos de información; las implicaciones sociales incluyen desvalorización del trabajo humano y peligros de sistemas autónomos incontrolables.

## Por capítulo

### Preface to the Second Edition (pp. 24–33)

- La disciplina de cibernética, con énfasis en retroalimentación y control automático, ha pasado de novedad científica a herramienta familiar de ingeniería y biología en trece años.
- Teoría de sistemas no-lineales exige nuevo enfoque matemático: el movimiento browniano como entrada apropiada reemplaza el análisis armónico de sistemas lineales; máquinas de aprendizaje ya no son ficción sino realidad aplicable.
- Riesgos sociales ya anticipados por Wiener (segundo Ludismo: devaluación del cerebro humano) ahora se hacen visibles en industria y sociedad; responsabilidad del científico de comunicar comprensión y confinar esfuerzos a fines no-bélicos.

**Cita ancla** (p. 6): «feedback both in engineering design and in biology has come to be well established»

### Introduction (pp. 38–47)

- Programa nacido de colaboración Wiener–Rosenblueth (1942) estudia "tierra de nadie" entre disciplinas: equipo interdisciplinario (matemáticos, ingenieros, fisiólogos) bajo contexto de guerra (sistemas de control anti-aéreo, máquinas calculadoras rápidas) genera teoría unificada de control y comunicación mediante retroalimentación.
- Círculos viciosos de retroalimentación patológica en neurología (tremor cerebelar cuando retroalimentación excesiva, ataxia cuando insuficiente) sugieren equivalencia entre dinámicas nerviosas y mecánicas; lógica matemática (Turing, Shannon, McCulloch, Pitts) demuestra isomorfismo entre neuronas binarias y circuitos electrónicos.
- Encuentro Princeton 1943–44 y Macy Foundation meetings 1946+ cristalizan cibernética como disciplina integradora incluyendo psicólogos, antropólogos, economistas; trabajo experimental en México (oscilaciones reflejas, clonus como retroalimentación) valida marco teórico; aplicaciones futuras: prótesis con retroalimentación sensorial, fábricas automáticas; peligros: segunda revolución industrial devalúa cerebro humano como la primera devaluó brazo.

**Cita ancla** (p. 27): «the central nervous system no longer appears as a self-contained organ, receiving inputs from the senses and discharging into the muscles»

### Cap. I · Newtonian and Bergsonian Time (pp. 48–61)

- Contraste fundamental: astronomía (reversible, determinista, pocos cuerpos) vs. meteorología (irreversible, estadística, muchas partículas); tiempo newtoniano es matemáticamente simétrico (ecuaciones invariantes bajo t → −t) pero tiempo real es flecha unidireccional (termodinámica clásica, vida, evolución).
- Incluso sistemas gravitacionales (George Darwin) exhiben procesos disipativos y fricción a largo plazo; máquinas modernas (termostatos, control anti-aéreo, computadoras) operan en tiempo bergsonian: dependencia del pasado, imposibilidad de conocimiento inicial completo, roles estadísticos; son "sensitive automata" acopladas al mundo mediante retroalimentación, no máquinas newtonianas sino estadísticas.
- Historia de técnica refleja evolución filosófica: era de relojes (Huyghens–Newton) → era de máquinas de vapor (Rumford–Carnot) → era actual de comunicación y control (servomecanismos).

**Cita ancla** (p. 50): «no such thing as a cloud, defined as an object with a quasi-permanent identity»

### Cap. II · Groups and Statistical Mechanics (pp. 63–77)

- Gibbs (1900) desarrolla mecánica estadística; Lebesgue proporciona fundamento matemático; hipótesis ergódica (Gibbs) y cuasi-ergódica (Plancherel) permiten equivalencia entre promedios temporales y de fase; entropía = logaritmo de medida de probabilidad de región; sistemas aislados tienden a máxima entropía.
- Maxwell demon pensado como violador de segunda ley; resolución: información tiene precio en entropía; enzimas y organismos = "metastable Maxwell demons" que disminuyen entropía localmente gracias a fuentes externas de energía; vivos son sistemas que funcionan contra tendencia entrópica mientras se mantiene ley global.
- Invariantes de grupo (caracteres = funciones que se transforman multiplicativamente); medida de fase = medida en espacio fásico invariante bajo transformaciones conservativas; teorema ergódico de Birkhoff–Koopman–von Neumann (ca. 1930) es base matemática rigurosa.

**Cita ancla** (p. 77): «Certainly the enzyme and the living organism are alike metastable: the stable state of an enzyme is to be deconditioned»

### Cap. III · Time Series, Information, and Communication (pp. 78–107)

- Información = medida de elección / negativa de entropía; decisión entre dos alternativas equiprobables = 1 bit; cantidad de información = −log₂(error); información de fuentes independientes es aditiva; relación con termodinámica: transmisión requiere que mensajes varíen estadísticamente.
- Series de tiempo en equilibrio estadístico: promedio temporal = promedio de fase (teorema ergódico); conociendo pasado completo se pueden computar parámetros estadísticos y predecir futuro con error conocido; movimiento browniano (partícula impulsada por choques aleatorios) es base para expansiones; probabilidad de ocupar posiciones en tiempos dados por distribución gaussiana.
- Predicción óptima minimiza error cuadrático medio; solución en dominio de frecuencias depende de ancho de banda y nivel de ruido; analogía con filtros de onda que separan mensaje de ruido optimizando criterio estadístico; transmisión de información proporcional a log(potencia mensaje/potencia ruido) sobre ancho de banda.

**Cita ancla** (p. 77): «The demon can only act on information»

### Cap. IV · Feedback and Oscillation (pp. 114–130)

- Patologías neurológicas como fallos de retroalimentación: tabes dorsalis (pérdida de propiocepción = imposibilidad de coordinar sin retroalimentación visual); tremor cerebelar = oscilación descontrolada por retroalimentación excesiva; cerebelum proporciona retroalimentación para acomodar respuesta muscular; retroalimentación insuficiente causa ataxia, excesiva causa oscilación.
- Teoría matemática de sistemas lineales: operador lineal invariante en tiempo g(t) = ∫₀^∞ a(τ)f(t−τ)dτ (solo pasado, no futuro); funciones e^(st) son eigenfunctions; representación en frecuencia A(s) = ∫₀^∞ a(τ)e^(−sτ)dτ (transformada Laplace); A(s) es función holomorfa bounded en semiplano Re(s) > 0.
- Sistema de retroalimentación: Y = X − λ·AY produce Y = X/(1 + λA); estabilidad crítica: si −1/λ es interior point de curva A(iy), sistema oscila inestablemente; si exterior, estable; diferenciador A(s) = s admite retroalimentación arbitraria; integrador A(s) = 1/s no; cascada triple no puede compensarse con única retroalimentación; ejemplo naval (gyrocompass): requiere dos retroalimentaciones, no una.

**Cita ancla** (p. 116): «a badly designed thermostat may send the temperature of the house into violent oscillations not unlike the motions of the man suffering from cerebellar tremor»

### Cap. V · Computing Machines and the Nervous System (pp. 135–150)

- Máquinas analógicas (Bush differential analyzer) vs. digitales; sistema binario es óptimo: registro de información minimiza cuando base N → ∞; máquinas digitales ideales requieren instrucciones que cubran todas contingencias.
- Neurona como relay con dos estados (firing/repose); "all-or-none principle"; sinapsis: número de fibers varía de pocos a cientos; umbral de disparo cuando suficientes sinapsis activan en fusion interval; sinapsis inhibitorias que elevan threshold o previenen firing.
- Memoria corto-plazo para operaciones en curso (circuitos de delay con regeneración); memoria largo-plazo permanente (punched cards, magnetic tape, phosphorescent, fotografía); quantum degeneracy en storage (ferromagnetism, high dielectric constant); posible mecanismo: cambios en thresholds de neuronas o permeabilidad de sinapsis.

**Cita ancla** (p. 142): «Photography is indeed ideal for the permanence and detail»

### Cap. VI · Gestalt and Universals (pp. 152–162)

- Eye-muscle feedbacks (centering, focusing, converging) centra objetos en posición estándar; retina concentra información visual: fovea ~1:1 ratio, periphery ~10:1; reconocimiento de drawing depende de accommodation en receptores constantes, mejor en boundaries.
- Telegraph-type repeater phenomena (compression de contrasts, deblurring); transformaciones perspectiva forman grupo matemático; group scanning método mecánico: scanning periódico sobre group-space cubre región como television scanning; medida de grupo = probabilidad density invariante.
- Posible mecanización lectura para ciegos: photoelectric cells + código auditivo (notas musicales); McCulloch device: conectores entre capas visuales; grupo-scanning assembly estructura anatómica fija con sincronismo widespread; alpha rhythm ~0.1 segundos = orden magnitud para comparación directa de formas.

**Cita ancla** (p. 154): «bring any object that attracts our attention into a standard position»

### Cap. VII · Cybernetics and Psychopathology (pp. 163–173)

- Cerebro vs. máquina de computación: necesaria triple o doble check para reliability; internuncial pool = canales alternativos para mensajes entre niveles nerviosos; funcional vs. organic: ambos pueden tener base física en memoria circulante o sinapsis thresholds.
- Procesos patológicos circulares: worry maligno en neurosis de ansiedad expande ocupando neuronas; shock treatment vs. lobotomía prefrontal: ambos interrumpen círculos viciosos con trade-offs; psychoanalysis: acceso multi-level a información almacenada con "affective tone".
- Traffic problem: cada forma de organización tiene upper limit de tamaño (D'Arcy Thompson: insects, animals, trees, skyscrapers); probabilidad de suceso total = (p)^N cuando N stages; sistemas multi-stage fallan catastróficamente cerca de punto crítico; humano tiende a operar eficientemente muy cerca del edge de overload.

**Cita ancla** (p. 170): «complicated type of behavior efficiently very close to the edge of an overload»

### Cap. VIII · Information, Language, and Society (pp. 174–185)

- Organización jerárquica: células → Leviatán Hobbes → organismos; comunicación social: hormigas (química limitada), abejas (danza), humanos (lenguaje); información racial vs. individual depende de si resulta en recognizable activity; community information ≠ individual information.
- Mercado no homeostático: game theory von Neumann muestra indeterminacy coalition instability; brilliant huckster espera ruina, rewards van a quien rompe acuerdo; knaves explotan fools; pequeñas comunidades homeostáticas por contact directo, customs tienen value homeostático.
- Ciencias sociales vs. naturales: observer influye en phenomenon; traduttore traditore; chess-playing machine: von Neumann optimal vs. crude decent play con depth 2–3 moves; medios comunicación (press, radio, phone, schools, church) constreñidos por triple constriction.

**Cita ancla** (p. 177): «There is a well-known tendency of libraries to become clogged by»

### Cap. IX · On Learning and Self-Reproducing Machines (pp. 188–196)

- Aprendizaje vs. auto-reproducción: ontogénico (individual) vs. phylogénico (racial); ambos modos de adaptación; game theory von Neumann: work backwards desde final; win > draw > lose valuations; Napoleon, Nelson: conocimiento de capacidad del opponent crítico más que estrategia perfecta.
- Chess books empíricos: principios de práctica, weightings sobre piezas/mobilidad/command; máquina de chess rígida sin aprendizaje; con aprendizaje absorbe policy de opponents; checkmate requiere fases distintas (opening/middle/endgame), valuations por stages; first-order vs. second-order programming: inmediato vs. statistical long-past.
- Mongoose vs. cobra: feints + timing; learning machine vs. reflexive snake; torero vs. toro: pattern timing + coordinación; atomic weapons peligrosos combinados con máquinas de aprendizaje; no se pueden apagar si no se conoce punto de peligro; máquinas literal-minded como Sorcerer's Apprentice genie.

**Cita ancla** (p. 195): «can defeat the man who has programmed it»

### Cap. X · Brain Waves and Self-Organizing Systems (pp. 200–222)

- Historia electrofisiología: Volta/Galvani → string galvanometer → vacuum tube amplifier → cathode-ray oscillograph; análisis armónico: autocorrelation fundamental; magnetic tape frequency-modulation (Rosenblith/Brazier) permite repeated reading sin degradation; playback heads para delay adjustable.
- Spectrum brain wave: integrated spectrum F(ω), mostly ~10 cycles; heterodyning method mueve análisis a centro frequency; poder spectrum sharp drop ~9.05 cycles/sec; peak width ~tercio cycle; gating needed en computing/control: mensajes almacenados se deben liberar simultáneamente, combined mientras están en máquina.
- Non-linear mechanism necesario: linear produce solo same frequency; non-linear sum/difference frequencies; oscillators ~10 cps atraen frecuencias formando clumps; after-discharge muestra power ~10 cycles; electrical alternators con governors: parallel busbars → frequency attraction (virtual governor), series → repulsion; self-organizing systems = non-linear frequency attraction.

**Cita ancla** (p. 207): «neighborhood of zero frequency which greatly cut down the work»

## Mapa: si buscas…

| Si buscas | Ve a |
|---|---|
| Retroalimentación negativa y estabilidad de sistemas | pp. 114–130 |
| Definición y medida de información | pp. 78–107 |
| Equivalencia entre máquinas digitales y sistema nervioso | pp. 135–150 |
| Patologías neurológicas como fallos de control | pp. 163–173 |
| Organización jerárquica y comunicación social | pp. 174–185 |
| Teoría de máquinas de aprendizaje | pp. 188–196 |
| Oscillaciones cerebrales y sistemas auto-organizadores | pp. 200–222 |
| Tiempo irreversible y máquinas estadísticas | pp. 48–61 |
| Maxwell demon, entropía, vida como sistema neguentrópico | pp. 63–77 |
| Predicción óptima de series de tiempo | pp. 78–107 |
| Group scanning y reconocimiento visual Gestalt | pp. 152–162 |
| Peligros sociales de máquinas autónomas | pp. 24–33, 174–185 |

## Conexiones con la biblioteca

- **ashby-introduction-to-cybernetics** — Ashby formaliza matemáticamente los principios cibernéticos de Wiener aplicados a regulación y diseño de sistemas complejos.
- **wiener-human-use-of-human-beings** — Wiener profundiza en las implicaciones sociales y éticas de la cibernética que apenas menciona en Cybernetics.
- **beer-brain-of-the-firm** — Beer aplica directamente la retroalimentación y la teoría cibernética de Wiener a la estructura organizacional de empresas.
- **ashby-design-for-a-brain** — Ashby desarrolla los principios de cibernética para el diseño de sistemas adaptativos y auto-reguladores.
- **pickering-the-cybernetic-brain** — Análisis histórico de cómo la cibernética de Wiener transformó el entendimiento del cerebro como máquina de información y control.
- **medina-cybernetic-revolutionaries** — Contexto histórico de Macy Conferences y desarrollo de cibernética en diálogo con antropología y psicología.

## Para Daniel

Este libro es la **fuente conceptual fundacional** para diagnosticar cualquier sistema de negocio mediante ciclos de retroalimentación: toda estrategia de un consultor (pricing, lead generation, conversión, retención) opera con feedback loops deficientes. En el diagnóstico RACE, la pregunta "¿qué métrica estás midiendo y reaccionando?" sale directamente de aquí—máquinas, empresas y equipos humanos fallan cuando no tienen retroalimentación clara o cuando sobre-reaccionan (tremor). El aprendizaje automático de máquinas que Wiener describe predice por qué los sistemas de un consultor que no "aprenden" de los datos cliente colapsan en escala.