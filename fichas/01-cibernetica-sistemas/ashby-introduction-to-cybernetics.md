---
slug: ashby-introduction-to-cybernetics
titulo: "An Introduction to Cybernetics"
titulo_es: ""
autor: "W. Ross Ashby"
anio: 1956
edicion: "Chapman & Hall, London; Second Impression 1957; Internet Edition (1999)"
estante: 01-cibernetica-sistemas
archivos:
  - biblioteca/01-cibernetica-sistemas/ashby-introduction-to-cybernetics.pdf
paginas: 157
citar_por: "página del PDF"
idioma: en
temas:
  - cibernética: pp. 1–8
  - transformaciones: pp. 9–23
  - máquinas-determinadas: pp. 24–41
  - máquinas-con-entrada: pp. 42–72
  - estabilidad: pp. 73–85
  - sistemas: pp. 86–120
  - variedad: pp. 121–160
  - regulación: pp. 161–272
  - información-y-comunicación: pp. 140–194
---

# W. Ross Ashby — *An Introduction to Cybernetics* (1956)

> Ficha de lectura: mapa para ir al libro, no sustituto. Páginas = número de página **del PDF**
> (el que muestra el visor, no el impreso), salvo que `citar_por` diga capítulo.

## Tesis en tres líneas

1. La cibernética estudia sistemas de control y comunicación mediante el análisis de transformaciones y comportamientos, no materiales específicos: toda máquina determinada puede representarse como una transformación cerrada y única en sus acciones.

2. La regulación biológica y la ingeniería de sistemas se rigen por la Ley de Variedad Requisita: solo la variedad en el regulador puede reducir la variedad del resultado final; la información y el diseño son actos de selección que comprimen posibilidades a un estado único.

3. Los organismos superiores amplifican su capacidad regulatoria en dos etapas: genes crean reguladores innatos que a su vez desarrollan reguladores aprendidos, permitiendo que inteligencia pequeña construya inteligencia grande mediante máquinas intermediarias.

## Por capítulo

### Cap. 1 · What is New (pp. 1–8)

- La cibernética define un nuevo ángulo: estudia comportamientos regulares mediante principios y métodos que no dependen de la materialidad (electrónica, física, biología).
- Ofrece un vocabulario único para sistemas diversos (máquinas, animales, organizaciones) y un marco donde ordenar todas las máquinas posibles.
- Las bases conceptuales son simples: no requieren matemática avanzada ni electrónica para entender los principios fundamentales de control y regulación.

**Cita ancla** (p. 2): «The basic ideas of cybernetics can be treated without reference to electronics, and they are fundamentally simple»

### Cap. 2 · Change (pp. 9–23)

- La transformación es el concepto central: conjunto de operandos y reglas de cambio, especificadas no por causa física sino por el cambio observable de cada elemento.
- Closure: un conjunto es cerrado bajo transformación si todos los resultados (transforms) están ya contenidos en el operandos original; esto caracteriza máquinas determinadas.
- El grafo cinemático visualiza transformaciones: nodos como estados, flechas como cambios; basins son regiones que convergen a un punto o ciclo.

**Cita ancla** (p. 10): «to any physical cause of the change, but by the giving of a set of operands and a statement of what each is changed to»

### Cap. 3 · The Determinate Machine (pp. 24–41)

- Una máquina determinada es aquella cuyo siguiente estado está completamente determinado por su estado actual; el comportamiento, no la materia, define la máquina.
- El vector agrupa componentes de sistemas complejos; la representación canónica (ecuaciones x' = f(x₁,...,xₙ)) permite especificar cualquier máquina discreta o continua.
- El sistema debe definirse correctamente: el mundo tiene infinitas variables, pero solo las relevantes importan; determinacy requiere un conjunto cerrado de variables bajo transformación.

**Cita ancla** (p. 18): «make unique the state it next moves to»

### Cap. 4 · The Machine with Input (pp. 42–72)

- Un transductor (máquina con entrada) tiene comportamiento que varía con parámetros externos que cambian; coupling une máquinas para que salida de una afecte entrada de otra.
- Feedback ocurre cuando partes se afectan mutuamente circularmente; feedback negativo tiende a mantener equilibrio, pero puede coexistir con feedback positivo.
- Variables muestran independencia o dominancia según si el cambio de una afecta la transición de otra; reducibilidad existe si subsistemas son funcionalmente independientes.

**Cita ancla** (p. 31): «When this circularity of action exists between the parts of a dynamic system, feedback may be said to be present»

### Cap. 5 · Stability (pp. 73–85)

- Equilibrio es un estado que la transformación no cambia (T(a) = a); estabilidad bajo perturbación significa que tras desplazamiento, el sistema vuelve al equilibrio límite.
- El homeostat (dispositivo de Ashby) usa poder de veto: ningún estado global es equilibrio a menos que sea aceptable para todas las partes; esto permite ultrastabilidad.
- Estabilidad es concepto compuesto: requiere especificación completa del equilibrio, la perturbación y sus límites; feedback negativo mantiene equilibrio pero puede coexistir con estabilidad en sistemas complejos.

**Cita ancla** (p. 44): «the state of equilibrium a in the system with transformation T is stable under displacement D if and only if n lim T D (»

### Cap. 6 · The Black Box (pp. 86–120)

- Problema central: dado un sistema sellado (black box) con entrada y salida observables, ¿qué puede deducirse del interior? Solo se tiene el protocolo de pares (entrada, salida) en tiempo discreto.
- Isomorfismo: dos máquinas son isomórficas si una transformación uno-a-uno convierte una en la otra; pueden tener patrones idénticos pero substancias completamente diferentes.
- Homomorfismo: una máquina compleja puede simplificarse agrupando estados si resultado sigue determinado; simplificación es homomorfismo (transformación muchos-a-uno).

**Cita ancla** (p. 54): «Machines can thus show the profoundest similarities in behaviour while being, from other points of view, utterly dissimilar»

### Cap. 7 · Quantity of Variety (pp. 121–139)

- Variedad es el número de elementos distinguibles en un conjunto (o logaritmo base 2 en bits); comunicación y ciencia requieren conjuntos de posibilidades.
- Constraint (restricción) es la relación entre conjuntos donde la variedad bajo una condición es menor que bajo otra; cada ley de la naturaleza implica constraint.
- Los grados de libertad miden independencia: si fewer combinaciones que máximo posible, existe restricción; máquinas determinadas son constraints caracterizadas por su protocolo codificado compactamente.

**Cita ancla** (p. 71): «Science looks for laws; it is therefore much concerned with looking for constraints»

### Cap. 8 · Transmission of Variety (pp. 140–160)

- Codificación: los mensajes se transforman en formas codificadas; si la transformación es uno-a-uno, la variedad se preserva; si pierde distinciones, no se puede recuperar completamente el original.
- Un inversor siempre puede construirse para recuperar mensajes originales si la transformación es determinista, independientemente de la materialidad.
- Ley fundamental: la variedad en U (resultado) no puede aumentar más en un paso que la variedad presente en T (transductor); con suficiente tiempo, cualquier transductor puede transmitir cualquier cantidad de variedad.

**Cita ancla** (p. 82): «the U's cannot gain in variety at one step by more than the variety present in the T's»

### Cap. 9 · Incessant Transmission (pp. 161–194)

- Transformaciones estocásticas permiten transmisión indefinida: cada operando puede ir a múltiples estados posibles con probabilidades constantes; matriz de transición especifica el comportamiento.
- Cadenas de Markov: secuencias donde probabilidades de transición son constantes; en equilibrio alcanzan densidades poblacionales constantes aunque individuos sigan moviéndose.
- Entropía de Shannon mide variedad en cadenas Markov; redundancia existe cuando vectores pueden codificarse con menos componentes; ruido es entrada no deseada; teorema fundamental: mensajes pueden transmitirse sin error sobre canales ruidosos si se aumenta capacidad.

**Cita ancla** (p. 100): «"Noise" is thus purely relative to some given recipient, who must say which information he wants to ignore»

### Cap. 10 · Regulation in Biological Systems (pp. 195–201)

- Regulación biológica es esencial para supervivencia: organismos actuales son resultado de 2 mil millones de años de selección natural que favorece mecanismos de defensa.
- Supervivencia significa mantener variables esenciales dentro de límites aceptables (η); regulación interpone mecanismo R entre disturbios D y variables esenciales E para bloquear transmisión de variedad.
- Bloqueo puede ser pasivo (cáscara de tortuga) o activo (habilidad del esgrimidor); buena regulación actúa como barrera contra información sobre disturbios.

**Cita ancla** (p. 106): «an essential function of F as a regulator is that it shall block the transmission of variety from disturbance to essential variable»

### Cap. 11 · Requisite Variety (pp. 202–218)

- Regulación como juego: D (disturbios) vs. R (regulador) con E (resultado); R gana si obtiene resultados aceptables para cualquier movimiento de D.
- **Ley de Variedad Requisita**: solo la variedad en R puede forzar que la variedad en E decrezca; variedad destruye variedad; es la ley fundamental de regulación que no depende de propiedades físicas.
- Si V_R es fija, la variedad en E se reduce solo si se aumenta V_R logarítmicamente (V_O ≥ V_D − V_R); los organismos toman información (variedad) del ambiente para bloquear variedad mayor que llegue al patrón genético.

**Cita ancla** (p. 110): «only variety in R can force down the variety due to D; variety can destroy variety»

### Cap. 12 · The Error-Controlled Regulator (pp. 219–243)

- Regulador error-controlado recibe información no del disturbio D sino del error en E; nunca puede ser perfecto porque su éxito bloquea el canal de información que necesita.
- Máquinas Markovianas tienen transiciones probabilísticas; búsqueda y anclaje (hunt and stick) es el proceso donde sistema alcanza equilibrio mediante tentativa.
- Regulación Markoviana es más fácil de construir que determinista, aunque menos eficiente; reguladores deterministas son servomecanismos con retroalimentación negativa; potencia amplificadora usa fuente generosa controlada por entrada pequeña.

**Cita ancla** (p. 120): «the more successful R is in keeping E constant, the more does R block the channel by which it is receiving its necessary information»

### Cap. 13 · Regulating the Very Large System (pp. 244–264)

- El tamaño no causa dificultad; la verdadera causa es la variedad en disturbios; Ley de Variedad Requisita pone límites absolutos a regulación posible.
- Disturbios repetitivos muestran restricción (constraint); descubrirlas es crucial para regulación efectiva; diseño de regulador es acto de comunicación: variedades se reducen a una máquina final.
- Selección puede ocurrir en etapas discretas reduciendo variedad gradualmente; si máquina es reducible (subsistemas independientes), selección rápida por dicotomía es posible.

**Cita ancla** (p. 134): «Thus the act of “designing” or “making” a machine is essentially an act of communication»

### Cap. 14 · Amplifying Regulation (pp. 265–272)

- Amplificador toma entrada pequeña y emite salida grande usando fuente abundante; proceso ocurre por suplementación, no por violación de conservación de energía.
- Amplificación de regulación en dos etapas: patrón genético hace R1 que a su vez hace R2 más potente; genes determinan reguladores embrionarios cuya acción desarrolla mecanismo regulatorio superior.
- Inteligencia es principalmente selección apropiada de posibilidades; si poder de selección se amplifica, poder intelectual se amplifica como potencia física; ahora es posible hacerlo sintéticamente, conscientemente, deliberadamente.

**Cita ancla** (p. 145): «the gene-patterns do it every time they form a brain that grows up to be something better than the gene-pattern could have specified in detail»

## Mapa: si buscas…

| Si buscas | Ve a |
|---|---|
| Definición de cibernética y su ángulo nuevo | pp. 1–8 |
| Transformaciones y closure | pp. 9–23 |
| Máquinas determinadas y representación canónica | pp. 24–41 |
| Transductores, coupling y feedback | pp. 42–72 |
| Equilibrio y estabilidad ante perturbación | pp. 73–85 |
| Black box, isomorfismo y homomorfismo | pp. 86–120 |
| Variedad, constraint y grados de libertad | pp. 121–139 |
| Transmisión de variedad por máquinas | pp. 140–160 |
| Cadenas de Markov, entropía y ruido | pp. 161–194 |
| Regulación biológica y bloqueo de variedad | pp. 195–201 |
| Ley de Variedad Requisita (teorema central) | pp. 202–218 |
| Reguladores error-controlados y Markovianos | pp. 219–243 |
| Regulación en sistemas muy grandes | pp. 244–264 |
| Amplificación de regulación en dos etapas | pp. 265–272 |

## Conexiones con la biblioteca

- **ashby-design-for-a-brain** — Complemento profundo: aplica los principios de Cybernetics al diseño de máquinas autorreguladoras; Ashby lo cita como intimately related.
- **wiener-cybernetics-1948** — Obra matriz: Wiener acuña el término "cibernética" que Ashby usa como punto de partida; esta introducción hace su teoría accesible.
- **beer-brain-of-the-firm** — Aplicación: Beer lleva la Ley de Variedad Requisita de Ashby a la organización de empresas como sistemas reguladores.
- **coase-the-nature-of-the-firm** — Puente conceptual: Coase ve firmas como estructuras de comunicación; Ashby proporciona la teoría de comunicación y variedad para entender eso.
- **wiener-human-use-of-human-beings** — Contexto social: Wiener explora implicaciones sociales de cibernética; Ashby da fundamento matemático y conceptual.

## Para Daniel

La Ley de Variedad Requisita (cap. 11) es el motor del diagnóstico RACE: cuando el consultor abre línea de comunicación con el dueño de negocio, está ganando información (variedad) para reducir el espacio de problemas. Ashby enseña que solo esa variedad informativa puede comprimir el desorden del negocio a tres acciones claras en 24h. En el Acompañamiento, la amplificación de regulación en dos etapas (cap. 14) describe cómo el consultor pequeño (R1) crea sistemas de IA y procesos (R2) que escalan su capacidad: genes del negocio (sistema del consultor) hacen reguladores innatos (procesos) que desarrollan reguladores aprendidos (máquinas de IA). El canal de Levy saca episodios sobre transformaciones determinadas y feedback para que consultores entiendan cómo sus sistemas deben comportarse regularmente sin depender de su presencia.
