# Esquema curado y notas orales para veinte minutos

**Fecha de corte: 14/10/2026.** Guion para una clase de electrónica cuyos integrantes pueden no haber cursado física de dispositivos. No es un archivo de diapositivas. El [dossier](01_dossier.md) conserva la profundización; aquí se selecciona lo que puede explicarse con claridad en voz alta.

La pregunta conductora es **cómo la radiación altera señales y componentes, y cómo Voyager limita esos efectos y sus consecuencias**. Una perturbación no necesita destruir una pieza para afectar la función.

## Orden y presupuesto de tiempo

| Nº | Bloque | Tema | Duración | Acumulado |
|---|---|---|---|---|
| 1 | Apertura | Pregunta y objetivo | 0:45 | 0:45 |
| 2 | I Ambiente | Partículas, origen y energía | 1:15 | 2:00 |
| 3 | I Ambiente | Trayectoria y exposición Voyager | 1:30 | 3:30 |
| 4 | II Componentes | Hardware y tres tipos de resultado | 1:15 | 4:45 |
| 5 | II Componentes | Resistencias y capacitores | 2:15 | 7:00 |
| 6 | II Componentes | Diodos y BJT | 2:30 | 9:30 |
| 7 | II Componentes | MOS, analógico y lógica | 2:30 | 12:00 |
| 8 | II Componentes | Magnéticos, placas e interconexiones | 1:30 | 13:30 |
| 9 | II Componentes | Detectores, óptica y cuarzo | 1:00 | 14:30 |
| 10 | III Ingeniería | Del pulso a una orden | 1:15 | 15:45 |
| 11 | III Ingeniería | Mitigaciones, evidencia y conclusión | 1:45 | 17:30 |
| — | Cierre | Mostrar bibliografía y señalar material de respaldo | 0:30 | 18:00 |

Se corrige la suma del plan recibido: sus once intervalos daban 18:45. Esta selección deja **18:00 de recorrido y 2:00 de margen**. La bibliografía puede mostrarse como lámina de consulta posterior, sin agregar explicación técnica. Si las preguntas cuentan dentro de veinte minutos, consumir ese margen y responder lo restante con el dossier.

Las notas siguientes son el relato seleccionado, no texto para copiar a la pantalla. Los tiempos incluyen señalar dibujos, explicar ejes y hacer pausas. La velocidad real debe comprobarse en un ensayo oral; un conteo de palabras solo aproxima su viabilidad.

## 1 Una misión útil puede tener efectos y fallas

**Mensaje central:** seguir funcionando no significa inmunidad.

**En pantalla:** «Dos sondas, casi cincuenta años» / «Señales falsas, degradación y recuperación» / «Del material al sistema».

**Visual previsto:** nombres Voyager 1 y 2, fechas de lanzamiento y una cadena partícula → componente → circuito → misión. No cargar la apertura con cifras de instrumentos.

**Notas orales:**

«Queremos explicar cómo la radiación afecta la electrónica de Voyager, incluyendo las partes que no son computadoras. Al 14 de octubre de 2026 ambas sondas tienen 49 años. Que continúen siendo útiles no significa que todas sus piezas funcionen como al comienzo. La radiación puede provocar una señal falsa por un instante, dejar un estado equivocado o degradar un componente. Vamos a recorrer esos efectos y ver qué decisiones de ingeniería ayudan a limitar sus consecuencias.»

**Transición:** «Primero debemos separar las distintas radiaciones que encontraron».

**Fuentes:** [S06](04_fuentes.md#s06)–07, [S21](04_fuentes.md#s21); dossier §§1 y 6.

## 2 Qué llega al circuito

**Mensaje central:** la radiación es una población de partículas con diferentes energías, no una intensidad única.

**En pantalla:** «Partículas galácticas» / «Eventos solares» / «Cinturones planetarios» / «Energía y cantidad importan».

**Visual previsto:** tres orígenes y partículas esquemáticas; no usar tamaños de dibujos como escala de energía.

**Notas orales:**

«Los rayos cósmicos galácticos incluyen principalmente núcleos, como protones y helio, y llegan desde fuera del sistema solar. El Sol también produce episodios de partículas energéticas. Además, las magnetosferas planetarias pueden atrapar partículas, como ocurre en Júpiter. No son ambientes equivalentes. La energía ayuda a determinar cómo penetra e interactúa una partícula; el flujo indica cuántas llegan por área y tiempo. La fluencia acumula esa llegada durante un intervalo. La dosis mide energía depositada por masa en un material. Por eso no podemos tomar una cantidad de partículas y llamarla directamente dosis del chip: necesitamos saber qué deposita energía y dónde.»

**Transición:** «Voyager pasó por más de uno de estos ambientes».

**Fuentes:** [S01](04_fuentes.md#s01) §II; [S17](04_fuentes.md#s17); [S21](04_fuentes.md#s21) pp. 4–17.

## 3 Lo que atravesó Voyager y lo que mide

**Mensaje central:** distinguir el ambiente del sobrevuelo de Júpiter del actual, y el detector del componente protegido.

**En pantalla:** «Júpiter: ambiente de diseño exigente» / «Hoy: espacio interestelar» / «Medir partículas no mide cada chip».

**Visual previsto:** cronología común hasta Saturno, separación de trayectorias y heliopausas; recuadro detector externo → blindaje → electrónica. Evitar una barra que compare dosis sin datos compatibles.

**Notas orales:**

«Ambas sondas pasaron por Júpiter y Saturno; Voyager 2 continuó a Urano y Neptuno. Hoy están fuera de la heliosfera. Para el diseño, los electrones de Júpiter eran una amenaza importante. Los informes establecieron exposiciones y requisitos de protección según la ubicación del equipo. Eso es diferente de afirmar cuánto recibió cada componente durante 49 años. Tenemos mediciones recientes de partículas de Voyager 2, pero son datos de un instrumento con una respuesta propia. Entre ese ambiente y un chip hay materiales, blindaje y geometría. Por eso vamos a usar los números de diseño como tales, sin presentarlos como una dosis actual medida de toda la nave.»

**Transición:** «Ahora veamos qué hay detrás de ese blindaje».

**Fuentes:** [S01](04_fuentes.md#s01) tablas 2-1/3-1; [S06](04_fuentes.md#s06), [S18](04_fuentes.md#s18)–20, [S29](04_fuentes.md#s29), [S33](04_fuentes.md#s33). Distancias exactas fuera de la pantalla; fechas en dossier §1.3.

## 4 El mapa del circuito y tres resultados

**Mensaje central:** toda la cadena electrónica importa, y no todo efecto es permanente.

**En pantalla:** seis grupos del mapa; una franja «Pulso → estado alterado → daño» con la aclaración «resultados posibles, no etapas obligatorias».

**Visual previsto:** mapa de familias, resaltando sucesivamente pasivos, semiconductores y conexiones. No presentarlo como plano de vuelo.

**Notas orales:**

«La nave combina alimentación, sensores, procesamiento y comunicaciones. En ellos encontramos resistencias, capacitores, dispositivos magnéticos, diodos, transistores, circuitos integrados y conexiones. No era simplemente toda TTL con una memoria CMOS: la documentación describe la evolución del FDS hacia procesador y memorias CMOS, además de numerosas funciones lógicas CMOS. Para cada componente preguntaremos qué cambia. Puede aparecer un pulso que termina solo; ese pulso puede dejar un dato u orden incorrectos; o pueden cambiar parámetros y quedar daño. Son resultados diferentes y no una secuencia inevitable.»

**Transición:** «Empezamos por dos componentes que parecen simples».

**Fuentes:** [S01](04_fuentes.md#s01) §VI.B; [S03](04_fuentes.md#s03)–04; [S21](04_fuentes.md#s21)–22. Alcance de identificación: dossier §4.4.

## 5 Resistencias y capacitores también participan

**Mensaje central:** estabilidad de valor y calidad del aislamiento son problemas distintos.

**En pantalla:** «Resistencia: valor e aislamiento» / «Capacitor: capacitancia y fuga» / «Una perturbación puede alterar tiempos» / «Voyager: ensayos y márgenes».

**Visual previsto:** resistencia a masa del ejemplo PWS y capacitor con una resistencia de fuga en paralelo. Aclarar que el segundo es modelo conceptual, no circuito Voyager.

**Notas orales:**

«En una resistencia importa su valor, pero también el aislamiento que la rodea. Una corriente no deseada puede crear una tensión considerable en una entrada de alta resistencia. En el instrumento PWS se consideró una corriente de carga de antena de cuatro microamperios y una resistencia de veinte megaohmios a masa: el producto da ochenta voltios. Esa resistencia ayuda a evacuar carga. Es un caso documentado, no una afirmación sobre cada resistencia de la nave.

En el capacitor, los electrodos almacenan cargas opuestas y el dieléctrico limita la corriente entre ellos. La radiación puede generar portadores en ese aislante y hacer que conduzca más durante la exposición. Entonces crece la fuga. El capacitor puede perder carga y disparar un temporizador antes de tiempo, incluso si después se recupera el aislamiento. Si solo medimos capacitancia, podemos pasar por alto ese problema.

El programa Voyager ensayó capacitores de teflón con cambios pequeños de capacitancia. Eso es evidencia favorable para ese parámetro y esas condiciones; no demuestra ausencia de todos los efectos. La mitigación exige elegir material, verificar aislamiento y comprobar que el circuito funcione con los parámetros previstos. Un capacitor usado como filtro tampoco elimina cualquier perturbación.»

**Transición:** «En los semiconductores, la carga generada puede convertirse directamente en una corriente de señal».

**Fuentes:** [S01](04_fuentes.md#s01) p. 7-53; [S08](04_fuentes.md#s08) §5.G; [S24](04_fuentes.md#s24) p. 49. Dossier §§3.1–3.2 y 5.3–5.4.

## 6 Diodos y BJT: pulso y ganancia

**Mensaje central:** colección de carga y recombinación explican efectos diferentes.

**En pantalla:** «Carga generada → corriente espuria» / «Más recombinación → menor ganancia» / «El circuito necesita margen».

**Visual previsto:** dibujo conceptual de una unión que separa cargas y una relación β = IC/IB. La figura 7-1 original queda como respaldo: su eje Δ(1/hFE) necesita más explicación que el tiempo disponible. Mostrarla solo si en ensayo oral resulta clara.

**Notas orales:**

«En una unión existe un campo eléctrico. Si la radiación genera cargas positivas y negativas cerca de esa zona, el campo puede separarlas y producir una corriente que no estaba prevista. En un diodo conectado a una entrada, esa corriente puede parecer una señal. Cuando se recoge o recombina la carga extra, el pulso termina; no es necesario que el diodo quede dañado.

El transistor bipolar suma otra cuestión: su ganancia. En funcionamiento normal, muchos portadores inyectados desde el emisor llegan al colector y otros se recombinan. La radiación puede crear defectos que facilitan la recombinación, o alterar superficies que aumentan la corriente de base. Para sostener una misma corriente de salida puede necesitarse más corriente de control. Si el circuito no tiene ese margen, cambia su funcionamiento.

Por ejemplo, en un modelo sencillo de región activa, diez miliamperios de salida requieren una décima de miliamperio de base con ganancia cien. Si la ganancia cae a cincuenta, requieren el doble. Son valores ilustrativos. El programa Voyager midió degradación en modelos como 2N2222 y 2N2907A, y encontró diferencias entre fabricantes. Esto justifica ensayar y seleccionar, no confiar solo en el nombre del transistor.

Un bipolar también puede entregar un pulso espurio sin haber perdido ganancia permanentemente. Por eso hay que evaluar tanto el parámetro degradado como lo que el circuito hace ante un pulso.»

**Transición:** «En MOS, el aislante de compuerta agrega otro mecanismo».

**Fuentes:** [S01](04_fuentes.md#s01) §VII.B, figuras 7-1/7-2; [S21](04_fuentes.md#s21); [S35](04_fuentes.md#s35)–36. Dossier §§3.4–3.5. No explicar diagramas de bandas durante el relato principal.

## 7 MOS y circuitos: el campo cambia o aparece un pulso

**Mensaje central:** carga atrapada y carga transitoria no son el mismo efecto.

**En pantalla:** «Carga atrapada: cambia el control» / «Carga recogida: aparece un pulso» / «Pulso capturado: cambia un estado».

**Visual previsto:** corte conceptual compuerta–óxido–semiconductor y curva MOS original [S01](04_fuentes.md#s01) figura 6-1. Señalar solo eje de tensión, eje de corriente y desplazamiento; indicar escala logarítmica. No extraer números finos del escaneo.

**Notas orales:**

«En un transistor MOS, la compuerta controla la conducción mediante un campo eléctrico a través de un aislante. La radiación puede generar carga en ese óxido. Parte se recombina o sale, pero otra puede quedar atrapada. Esa carga también genera campo: cambia la tensión de compuerta necesaria para obtener la misma conducción. Los defectos en la interfaz aportan otros cambios, por lo que no todos los dispositivos responden igual.

En este gráfico del programa Voyager vemos corriente frente a tensión de compuerta antes y después de irradiar. Las curvas se desplazan. Para el circuito eso puede significar menos margen de encendido y apagado o más consumo. El programa modificó un paso de fabricación de la familia CMOS RCA para mejorar su comportamiento. No significa que el dispositivo se hiciera inmune.

Por otro camino, la carga generada en el semiconductor puede perturbar un nodo por un instante. Un amplificador puede entregar un pulso falso; un comparador puede cambiar su salida; una memoria puede conservar el estado equivocado después de que el pulso desapareció. No todo pulso llega a alterar un estado: importa su amplitud, duración y cuándo lo recibe el siguiente bloque. El filtrado o la comprobación de estados pueden ayudar en una aplicación, pero deben verificarse y no reparan por sí solos un dispositivo dañado.»

**Transición:** «La perturbación tampoco se queda obligatoriamente dentro del integrado».

**Fuentes:** [S01](04_fuentes.md#s01) §VI.B y figura 6-1; [S22](04_fuentes.md#s22)–23; [S35](04_fuentes.md#s35). Mitigaciones generales identificadas como tales.

## 8 Aislantes y conexiones: por dónde viaja el efecto

**Mensaje central:** un conductor sano puede transmitir una perturbación originada en otro lugar.

**En pantalla:** «Aislante: carga y fugas» / «Descarga: pulso hacia otras líneas» / «Bobina y relé: revisar el mando».

**Visual previsto:** aislante con carga, trayectoria de descarga y línea receptora; bobinado señalado por su aislamiento. Figura conceptual, no materiales identificados de Voyager.

**Notas orales:**

«Las placas y los bobinados tienen materiales aislantes. Pueden acumular carga o conducir más; según las condiciones, una descarga puede inyectar un pulso en una conexión. La pista puede estar sana y conducir ese pulso hasta otra entrada. Importan los retornos y la conexión entre partes, además de proteger cada chip.

En un transformador debemos separar el núcleo, el bobinado y su aislamiento. No tenemos evidencia para atribuir una desmagnetización radiativa a los núcleos de Voyager. También puede pasar que el transistor de mando entregue un pulso incorrecto a un magnético sano. Algo similar ocurre con un relé: si recibe una orden equivocada suficientemente larga, puede conectar una carga aunque no esté dañado.

Esta explicación general se basa en manuales NASA. Cuando no conocemos el material o modelo de vuelo lo dejamos explícito; tampoco confundimos una soldadura fatigada con daño por radiación.»

**Transición:** «En los sensores, la misma carga puede ser precisamente lo que buscamos medir».

**Fuentes:** [S25](04_fuentes.md#s25) §4.1; [S26](04_fuentes.md#s26) §10.2.6.5; [S03](04_fuentes.md#s03) p. 16; [S08](04_fuentes.md#s08) §5.G.

## 9 Señal útil y respuesta del sensor

**Mensaje central:** el significado de una carga depende de qué mide el circuito.

**En pantalla:** «Detectar carga puede ser la función» / «Recalibrar no repara el material» / «Cuarzo: selección mediante ensayos».

**Visual previsto:** detector de partículas frente a sensor óptico y etiqueta de cuarzo como referencia temporal.

**Notas orales:**

«En un detector de partículas, recoger la carga producida por radiación es la función. En un sensor óptico esa misma interacción puede parecer una luz que no llegó. Con exposición también puede cambiar la eficiencia del detector. En Voyager se documentaron daños después de Júpiter y ajustes de respuesta: recalibrar puede recuperar utilidad científica, pero no elimina los defectos. La cadena óptica también depende de emisor y receptor. Para cuarzo hay evidencia de selección mediante irradiación de muestras de barras. No atribuimos todo error de reloj al cristal: su electrónica también puede sufrir espurios.»

**Transición:** «Sigamos ahora un pulso hasta su consecuencia».

**Fuentes:** [S09](04_fuentes.md#s09); [S01](04_fuentes.md#s01) §§VII.I y VIII.F; [S26](04_fuentes.md#s26) §8.6.8; [S30](04_fuentes.md#s30).

## 10 Un pulso termina, una orden puede quedar

**Mensaje central:** supervivencia del componente y funcionamiento correcto del sistema son distintos.

**En pantalla:** «Amplificador → comparador → registro → carga» / «El pulso termina; el estado permanece» / «Ejemplo conceptual, no evento Voyager».

**Visual previsto:** cadena y dos trazas: pulso breve frente a estado sostenido. Usar el esquema del dossier, sin valores de vuelo inventados.

**Notas orales:**

«Imaginemos que aparece un pulso falso en un amplificador. Si supera el umbral del comparador y el receptor lo acepta, un registro cambia y ordena activar una carga. El amplificador se recupera, pero el registro sigue dando la orden. No se rompió necesariamente ninguna pieza. Si el pulso era demasiado corto, pequeño o llegó fuera del momento de captura, esa consecuencia puede no ocurrir.

Un filtro puede reducir ciertas perturbaciones; validar la duración puede rechazar otras; comprobar o restablecer el estado ayuda después. Pero filtrar también puede retrasar una señal legítima. Son decisiones de circuito que hay que verificar, no soluciones universales. Este ejemplo explica el mecanismo y no reconstruye una falla concreta de Voyager.»

**Transición:** «La ingeniería combina medidas que actúan en distintos puntos de esta cadena».

**Fuentes:** [S35](04_fuentes.md#s35) §§2 y 4; [S22](04_fuentes.md#s22) SET. Modelo propio, dossier §5.7.

## 11 Qué explica la continuidad de Voyager

**Mensaje central:** limitar efectos y recuperar funciones permite seguir siendo útil con pérdidas.

**En pantalla:** «Ensayos, selección y márgenes» / «Proceso y blindaje específicos» / «Redundancia y recuperación operacional» / «Energía y temperatura también importan».

**Visual previsto:** cuatro medidas asociadas a exposición, componente, circuito y sistema. Dos ejemplos: daño CRS documentado y recuperación de memoria sin causa radiativa probada.

**Notas orales:**

«Los informes de Voyager muestran ensayos de componentes, análisis de peor caso, selección, cambios de fabricación y blindaje específico. La arquitectura y el trabajo desde Tierra permitieron recuperar funciones. Cada medida trata un problema: reducir exposición no es lo mismo que tolerar una ganancia menor o corregir un estado erróneo.

La evidencia también obliga a separar causas. Hay daño radiativo documentado en detectores tras Júpiter. En 2010 se corrigió un bit alterado, pero eso no identifica por sí solo una partícula causante. En 2024 se recuperó telemetría reubicando código tras una falla de memoria, cuya causa física no quedó resuelta entre las posibilidades publicadas. Además, apagar instrumentos para ahorrar energía no demuestra que esos instrumentos hayan sido destruidos por radiación.

La conclusión es que la radiación puede alterar señales y parámetros. El diseño debe limitar ambas cosas y sus consecuencias. Voyager continúa produciendo ciencia con capacidades reducidas: eso muestra resistencia y recuperación del sistema, no ausencia de efectos.»

**Transición al respaldo:** «Las fuentes originales y las explicaciones más profundas quedan disponibles en el dossier».

**Fuentes:** [S01](04_fuentes.md#s01)–04, [S07](04_fuentes.md#s07), [S09](04_fuentes.md#s09)–16. Presentar estado de instrumentos solo con fecha de corte si surge la pregunta.

## Material de respaldo y límites de la selección

Mostrar bibliografía abreviada: [S01](04_fuentes.md#s01)/S02 para calificación Voyager; [S04](04_fuentes.md#s04) para hardware; [S21](04_fuentes.md#s21)/S22 para mecanismos; [S25](04_fuentes.md#s25)/S26 para materiales; [S35](04_fuentes.md#s35)/S36 para transitorios y bipolares. El índice completo está en [04_fuentes.md](04_fuentes.md) y las copias en [citas](../citas/README.md).

Reservar para preguntas: balance detallado de corrientes, regiones y estados de interfaz, LET→carga, tabla de ensayos y su discrepancia, arquitecturas CCS/AACS/FDS, susceptibilidad por lote y límites de filtrado. El dossier explica todo ello sin obligar a exponerlo.

**Criterio de diseño posterior:** texto breve y figuras explicadas, respetando [las consignas](00_consignas.md). No colocar las notas orales en la diapositiva. No usar una figura de transistor de potencia moderno como si identificara hardware Voyager. El mapa sirve de índice; no sustituye esquemas explicativos de cada mecanismo.
