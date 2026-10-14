# Guion de selección para una exposición de 20 minutos

No es una presentación terminada. Es la selección del dossier para desarrollar después las diapositivas. Las fuentes y reservas de cada afirmación están en [el dossier](01_dossier.md) y [la matriz](02_matriz_evidencias.md).

**Pregunta conductora:** ¿cómo cambia una partícula el funcionamiento de un circuito y qué hizo Voyager para seguir siendo útil durante casi 50 años?

| Tiempo | Bloque | Contenido que debe quedar claro |
|---|---|---|
| 0:00–1:00 | Introducción y objetivo | Dos sondas lanzadas en 1977; casi 50 años, capacidades reducidas. Objetivo: unir material, componente, circuito y sistema. |
| 1:00–4:00 | I. Ambiente | Galáctico, solar y cinturones; Júpiter frente a espacio interestelar. Distinguir energía, flujo, fluencia, dosis y LET. Una cuenta instrumental no es una dosis del chip. |
| 4:00–6:00 | II. Física | TID: carga/defectos acumulados; desplazamiento: red y minoritarios; SEE: carga recogida de un evento. Añadir carga electrostática y descarga para entender aislantes e interconexiones. |
| 6:00–15:00 | II. Recorrido por componentes | Usar el mapa como índice visual y profundizar en los ejemplos de abajo. Cada explicación: interacción → parámetro → función → mitigación y límite. |
| 15:00–18:00 | III. Ingeniería Voyager | Ensayos por lote y polarización, peor caso, proceso CMOS, blindaje localizado, redundancia y respuesta desde Tierra. RDM 60/30 = 2 como ejemplo de diseño. |
| 18:00–20:00 | III. Aplicación y conclusión | Detectores dañados frente a chip de causa incierta; energía y temperatura como problemas distintos. Resistencia del componente más recuperación del sistema. |

Total: **20:00**. Ensayar a 18:30 deja 90 segundos de margen dentro de ese máximo. Si las preguntas cuentan dentro del tiempo, recortar ejemplos; no acelerar todo el relato.

## Recorrido del mapa: nueve minutos

| Tiempo disponible | Familias | Ejemplo y frase que organiza la explicación |
|---|---|---|
| 2:00 | Resistencias y capacitores | PWS: 4 µA × 20 MΩ = 80 V; la resistencia evacúa carga. El capacitor puede conservar C y perder aislamiento. Ensayo B11B: variación de C pequeña, sin generalizar a todas sus propiedades. |
| 1:00 | Inductores y transformadores | Separar núcleo, bobinado y aislante. El aislamiento puede importar más que la idea intuitiva de “desmagnetización”. Composición de magnéticos de vuelo no resuelta. |
| 1:30 | Diodos y bipolares | Defectos → recombinación/fuga; menor β → más corriente de base para la misma carga. La función puede fallar antes que el componente quede abierto. |
| 1:30 | FET, IC y memoria | Óxido/interfaz → umbral; evento → carga recogida. Cambio del proceso RCA y blindaje CMOS documentados. Un SEU no describe toda la radiación. |
| 1:30 | Placa, pistas, conectores, soldaduras y relés | Dieléctrico o metal flotante → potencial → descarga acoplada. Separar esto de fatiga de soldaduras o desgaste de contactos. No inventar materiales Voyager. |
| 1:30 | Detectores, óptica y cuarzo | La carga es señal en un detector y perturbación en otro circuito. Daño CRS real; recalibración recupera utilidad. Cuarzo: selección de barras mediante irradiación. |

No hace falta leer trece fichas de texto. El mapa permite señalar cada familia; cuatro casos sostienen el argumento en profundidad: **resistencia de antena, aislamiento del capacitor, ganancia del transistor y respuesta del detector**. Las demás fichas quedan disponibles para preguntas.

## Figuras que conviene seleccionar después

1. Mapa propio de componentes como índice del recorrido, claramente rotulado “conceptual”.
2. Curvas MOS de [S01](04_fuentes.md#s01), figura 6-1: identificar ejes, polarización y condición de irradiación antes de explicar el desplazamiento. No atribuir geometría que no indica.
3. Tabla de pasivos de [S01](04_fuentes.md#s01), p. 7-53: extraer los dos cambios de C y explicar que un ensayo de C no mide toda la función.
4. Entrada PWS: redibujar únicamente conexiones que el artículo permite establecer; citar §5.G. El cálculo de 80 V ya funciona sin un plano completo.

Para la futura diapositiva del mapa, usar seis grupos con nombres breves. Las cadenas causales y reservas se explican oralmente; no trasladar esta matriz completa a la pantalla. Respetar las consignas de tipografía, cantidad de texto, contraste y explicación de figuras transcritas en [00_consignas](00_consignas.md).

## Apertura y cierre sugeridos

**Apertura:** “Voyager no demuestra que la radiación sea inofensiva. Nos permite ver cómo se diseña un circuito para que cambios inevitables en sus componentes no terminen de inmediato la misión. Vamos a recorrer desde una resistencia hasta la memoria.”

**Cierre:** “La partícula interactúa con materiales; el cambio de material altera un parámetro; el circuito tiene un margen; y el sistema puede recuperarse de algunas pérdidas. Voyager reúne esas cuatro escalas. Sigue haciendo ciencia con menos capacidades, y no podemos atribuir cada avería a radiación.”

## Material de reserva, fuera del recorrido principal

Derivación LET→carga; DDD y NIEL; integración angular del flujo; discrepancia de fluencia en tabla A-2; números exactos de palabras FDS; arquitectura de heartbeat; límites de blindaje por secundarios. Son útiles para preguntas técnicas, pero juntos exceden veinte minutos.
