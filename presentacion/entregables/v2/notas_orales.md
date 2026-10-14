# Radiación y electrónica de Voyager

Ignacio Cavicchioli. Corte: 14/10/2026.
12 diapositivas principales: 18 minutos; 4 respaldos fuera del tiempo.

## 1. Radiación y electrónica de Voyager

Tiempo: 0:45

«Queremos explicar cómo la radiación afecta la electrónica de Voyager, incluyendo las partes que no son computadoras. Al 14 de octubre de 2026 ambas sondas tienen 49 años. Que continúen siendo útiles no significa que todas sus piezas funcionen como al comienzo. La radiación puede provocar una señal falsa por un instante, dejar un estado equivocado o degradar un componente. Vamos a recorrer esos efectos y ver qué decisiones de ingeniería ayudan a limitar sus consecuencias.»

FUENTES Y LOCALIZADORES
[S06](04_fuentes.md#s06), [S07](04_fuentes.md#s07), [S21](04_fuentes.md#s21); dossier §§1 y 6.
S06 — Voyager Fact Sheet
https://science.nasa.gov/mission/voyager/fact-sheet/
S07 — Where Are Voyager 1 and 2 Now
https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/
S21 — Radiation Effects on Electronics 101 Kenneth LaBel
https://nepp.nasa.gov/DocUploads/392333B0-7A48-4A04-A3A72B0B1DD73343/Rad_Effects_101_WebEx.pdf

LECTURA DE LA FIGURA
La ilustración de S37 localiza el bus, los instrumentos y los RTG. Es un esquema de la nave, no una placa electrónica. Al corte 14/10/2026 ambas sondas superan los 49 años. Introducir la pregunta: continuar produciendo ciencia admite degradación, capacidades reducidas y recuperación.
S37: 45 Years Ago: Voyager 1 Begins its Epic Journey to the Outer Planets and Beyond
https://www.nasa.gov/history/45-years-ago-voyager-1-begins-its-epic-journey-to-the-outer-planets-and-beyond/

## 2. Tres ambientes, distintas partículas

Tiempo: 1:15

«Los rayos cósmicos galácticos incluyen principalmente núcleos, como protones y helio, y llegan desde fuera del sistema solar. El Sol también produce episodios de partículas energéticas. Además, las magnetosferas planetarias pueden atrapar partículas, como ocurre en Júpiter. La energía ayuda a determinar cómo penetra e interactúa una partícula; el flujo indica cuántas llegan por área y tiempo. La dosis mide energía depositada por masa en un material. Por eso no podemos tomar una cantidad de partículas y llamarla directamente dosis del chip: necesitamos saber qué deposita energía y dónde.»

FUENTES Y LOCALIZADORES
[S01](04_fuentes.md#s01) §II; [S17](04_fuentes.md#s17); [S21](04_fuentes.md#s21) pp. 4–17.
S01 — Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf
S17 — Cosmic Rays Introduction NASA GSFC
https://imagine.gsfc.nasa.gov/science/toolbox/cosmic_rays1_orig.html
S21 — Radiation Effects on Electronics 101 Kenneth LaBel
https://nepp.nasa.gov/DocUploads/392333B0-7A48-4A04-A3A72B0B1DD73343/Rad_Effects_101_WebEx.pdf

LECTURA DE LA FIGURA
Los puntos representan partículas sin escala de tamaño o energía. No se conectan los tres ambientes: no son etapas. El flujo cuenta partículas por área y tiempo; la dosis depende de energía depositada y masa del material. Los cinturones incluyen electrones y protones; la primera etiqueta solo caracteriza la población galáctica de modo abreviado.

## 3. Del espacio al interior del equipo

Tiempo: 1:30

«Ambas sondas pasaron por Júpiter y Saturno; Voyager 2 continuó a Urano y Neptuno. Hoy están fuera de la heliosfera. Para el diseño, los electrones de Júpiter eran una amenaza importante. Los informes establecieron exposiciones y requisitos de protección según la ubicación del equipo. Tenemos mediciones recientes de partículas de Voyager 2, pero son datos de un instrumento con una respuesta propia. Entre ese ambiente y un chip hay materiales, blindaje y geometría. Los requisitos de diseño no son una medición de la dosis acumulada durante toda la misión.»

FUENTES Y LOCALIZADORES
[S01](04_fuentes.md#s01) tablas 2-1/3-1; [S06](04_fuentes.md#s06), [S18](04_fuentes.md#s18), [S19](04_fuentes.md#s19), [S20](04_fuentes.md#s20), [S29](04_fuentes.md#s29), [S33](04_fuentes.md#s33). Distancias exactas fuera de la pantalla; fechas en dossier §1.3.
S01 — Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf
S06 — Voyager Fact Sheet
https://science.nasa.gov/mission/voyager/fact-sheet/
S18 — Voyager CRS Data
https://voyager.gsfc.nasa.gov/data.html
S19 — Voyager CRS Flux Time History
https://voyager.gsfc.nasa.gov/flux.html
S20 — Voyager 2 PGH Rate six hour averages
https://voyager.gsfc.nasa.gov/_recent/data/v2_3m_ipgh.txt
S29 — The Voyage to Interstellar Space
https://www.nasa.gov/solar-system/the-voyage-to-interstellar-space/
S33 — Voyager 2 PGH Rate documentation
https://voyager.gsfc.nasa.gov/v2pgh.html

LECTURA DE LA FIGURA
Imágenes históricas NASA S37. La ilustración de heliosfera representa ambas sondas fuera, no distancias actuales. Sección inferior conceptual: material y geometría modifican el espectro y la deposición. Las flechas no cuantifican un factor de atenuación. Los 30 krad de diseño del bus en S01 no son dosis medida acumulada durante 49 años.
S37: 45 Years Ago: Voyager 1 Begins its Epic Journey to the Outer Planets and Beyond
https://www.nasa.gov/history/45-years-ago-voyager-1-begins-its-epic-journey-to-the-outer-planets-and-beyond/

## 4. Un circuito, distintas consecuencias

Tiempo: 1:15

«La nave combina alimentación, sensores, procesamiento y comunicaciones. En ellos encontramos resistencias, capacitores, dispositivos magnéticos, diodos, transistores, circuitos integrados y conexiones. La documentación describe un procesador y memorias CMOS en el sistema de datos, además de otras funciones lógicas CMOS. Para cada componente preguntaremos qué cambia. Puede aparecer un pulso que termina solo; ese pulso puede dejar un dato u orden incorrectos; o pueden cambiar parámetros y quedar daño. Son resultados diferentes y no una secuencia inevitable.»

FUENTES Y LOCALIZADORES
[S01](04_fuentes.md#s01) §VI.B; [S03](04_fuentes.md#s03), [S04](04_fuentes.md#s04); [S21](04_fuentes.md#s21), [S22](04_fuentes.md#s22). Alcance de identificación: dossier §4.4.
S01 — Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf
S03 — Voyager Backgrounder
https://ntrs.nasa.gov/api/citations/19810023559/downloads/19810023559.pdf
S04 — Computers in Spaceflight The NASA Experience
https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf
S21 — Radiation Effects on Electronics 101 Kenneth LaBel
https://nepp.nasa.gov/DocUploads/392333B0-7A48-4A04-A3A72B0B1DD73343/Rad_Effects_101_WebEx.pdf
S22 — JPL ASIC Guide Design for Radiation Tolerance
https://parts.jpl.nasa.gov/asic/Sect.3.4.html

LECTURA DE LA FIGURA
Esquema funcional didáctico, no plano Voyager. Se omiten polarización, realimentación y conexiones detalladas de alimentación. El sensor produce señal; R/C acondicionan; amplificador y comparador forman una señal lógica; un registro puede conservar un estado y el transistor manda una carga inductiva. Las etiquetas pulso, estado y parámetro señalan resultados posibles, no etapas obligatorias.

## 5. Aislamiento, fuga y carga almacenada

Tiempo: 2:15

«En una resistencia importa su valor, pero también el aislamiento que la rodea. Una corriente no deseada puede crear una tensión considerable en una entrada de alta resistencia. En el instrumento PWS se consideró una corriente de carga de antena de cuatro microamperios y una resistencia de veinte megaohmios a masa: el producto da ochenta voltios. Esa resistencia ayuda a evacuar carga. Es un caso documentado, no una afirmación sobre cada resistencia de la nave.

En el capacitor, los electrodos almacenan cargas opuestas y el dieléctrico limita la corriente entre ellos. La radiación puede generar portadores en ese aislante y hacer que conduzca más durante la exposición. Entonces crece la fuga. El capacitor puede perder carga y alterar un tiempo, incluso si después se recupera el aislamiento. El disparo puede adelantarse o retrasarse según cómo funcione ese temporizador. Si solo medimos capacitancia, podemos pasar por alto ese problema.

El programa Voyager ensayó capacitores de teflón con cambios pequeños de capacitancia. Eso es evidencia favorable para ese parámetro y esas condiciones; no demuestra ausencia de todos los efectos. La mitigación exige elegir material, verificar aislamiento y comprobar que el circuito funcione con los parámetros previstos. Un capacitor usado como filtro tampoco elimina cualquier perturbación.»

FUENTES Y LOCALIZADORES
[S01](04_fuentes.md#s01) p. 7-53; [S08](04_fuentes.md#s08) §5.G; [S24](04_fuentes.md#s24) p. 49. Dossier §§3.1–3.2 y 5.3–5.4.
S01 — Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf
S08 — A Plasma Wave Investigation for the Voyager Mission
https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/pwsinst.htm
S24 — Radiation Effects and Analysis Lessons Wyrwas Wilcox
https://nepp.nasa.gov/docs/etw/2022/16-JUN-THU/1600-Wyrwas-20220002512.pdf

LECTURA DE LA FIGURA
Izquierda: caso PWS documentado, corriente de carga de antena de 4 µA y resistencia de 20 MΩ, 80 V. No dibuja un capacitor instalado en el PWS. Derecha: capacitor aislado inicialmente cargado; traza gris representa idealización sin fuga, azul descarga por fuga resistiva. Mismos ejes conceptuales, sin valores medidos. La radiación puede aumentar conductividad durante irradiación y alterar la descarga. Mitigación: aislamiento, material y margen; los ensayos B11B documentan capacitancia, no inmunidad a todo efecto.

## 6. La carga altera señal y ganancia

Tiempo: 2:30

«En una unión existe un campo eléctrico. Si la radiación genera cargas positivas y negativas cerca de esa zona, el campo puede separarlas y producir una corriente que no estaba prevista. En un diodo conectado a una entrada, esa corriente puede parecer una señal. Cuando se recoge o recombina la carga extra, el pulso termina; no es necesario que el diodo quede dañado.

El transistor bipolar suma otra cuestión: su ganancia. En funcionamiento normal, muchos portadores inyectados desde el emisor llegan al colector y otros se recombinan. La radiación puede crear defectos que facilitan la recombinación, o alterar superficies que aumentan la corriente de base. Para sostener una misma corriente de salida puede necesitarse más corriente de control. Si el circuito no tiene ese margen, cambia su funcionamiento.

Por ejemplo, en un modelo sencillo de región activa, diez miliamperios de salida requieren una décima de miliamperio de base con ganancia cien. Si la ganancia cae a cincuenta, requieren el doble. Son valores ilustrativos. El programa Voyager midió degradación en modelos como 2N2222 y 2N2907A, y encontró diferencias entre fabricantes. Esto justifica ensayar y seleccionar, no confiar solo en el nombre del transistor.

Un bipolar también puede entregar un pulso espurio sin haber perdido ganancia permanentemente. Por eso hay que evaluar tanto el parámetro degradado como lo que el circuito hace ante un pulso.»

FUENTES Y LOCALIZADORES
[S01](04_fuentes.md#s01) §VII.B, figuras 7-1/7-2; [S21](04_fuentes.md#s21); [S35](04_fuentes.md#s35), [S36](04_fuentes.md#s36). Dossier §§3.4–3.5. No explicar diagramas de bandas durante el relato principal.
S01 — Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf
S21 — Radiation Effects on Electronics 101 Kenneth LaBel
https://nepp.nasa.gov/DocUploads/392333B0-7A48-4A04-A3A72B0B1DD73343/Rad_Effects_101_WebEx.pdf
S35 — Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices
https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf
S36 — Hydrogen Contamination and Its Correlation with Enhanced Low-Dose-Rate Sensitivity
https://nepp.nasa.gov/files/25742/12_162_JPL_Adell_Hydrogen%20Contamination%20rec%201%207%2014.pdf

LECTURA DE LA FIGURA
Izquierda: unión p–n, con separación de cargas dentro o cerca de la zona de colección. Flechas de cargas positivas hacia p y electrones hacia n; el campo tiene sentido n hacia p. No se dibuja una escala espacial ni una polarización de vuelo. Derecha: comparación cualitativa NPN con igual geometría: E emisor, B base, C colector. Las cruces representan recombinación adicional, no una fracción medida. Para sostener IC puede requerirse más IB. El modelo no distingue visualmente recombinación superficial y volumétrica: explicarlas verbalmente según el dossier. El dato cuantitativo ilustrativo queda en notas.

## 7. La carga atrapada modifica el control

Tiempo: 2:30

«En un transistor MOS, la compuerta controla la conducción mediante un campo eléctrico a través de un aislante. La radiación puede generar carga en ese óxido. Parte se recombina o sale, pero otra puede quedar atrapada. Esa carga también genera campo: cambia la tensión de compuerta necesaria para obtener la misma conducción. Los defectos en la interfaz aportan otros cambios, por lo que no todos los dispositivos responden igual.

En este gráfico del programa Voyager vemos corriente frente a tensión de compuerta antes y después de irradiar. La característica NMOS se desplaza: para una misma corriente cambia la tensión de compuerta. Para el circuito eso puede significar menos margen de encendido y apagado o más consumo. El programa modificó un paso de fabricación de la familia CMOS RCA para mejorar su comportamiento. No significa que el dispositivo se hiciera inmune.

Por otro camino, la carga generada en el semiconductor puede perturbar un nodo por un instante. Un amplificador puede entregar un pulso falso; un comparador puede cambiar su salida; una memoria puede conservar el estado equivocado después de que el pulso desapareció. No todo pulso llega a alterar un estado: importa su amplitud, duración y cuándo lo recibe el siguiente bloque. El filtrado o la comprobación de estados pueden ayudar en una aplicación, pero deben verificarse y no reparan por sí solos un dispositivo dañado.»

FUENTES Y LOCALIZADORES
[S01](04_fuentes.md#s01) §VI.B y figura 6-1; [S22](04_fuentes.md#s22), [S23](04_fuentes.md#s23); [S35](04_fuentes.md#s35). Mitigaciones generales identificadas como tales.
S01 — Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf
S22 — JPL ASIC Guide Design for Radiation Tolerance
https://parts.jpl.nasa.gov/asic/Sect.3.4.html
S23 — JPL ASIC Guide Appendix Three
https://parts.jpl.nasa.gov/asic/Appendix.3.html
S35 — Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices
https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf

LECTURA DE LA FIGURA
Sección de compuerta, óxido y semiconductor sin escala. Los signos positivos representan carga atrapada ilustrativa, no una densidad medida; los estados de interfaz también importan. Gráfica S01 fig. 6-1 conserva los dos dispositivos porque comparten ejes. Señalar las curvas NMOS de 0 y 150 krad. ID es corriente de drenador en escala logarítmica y VG tensión de compuerta. No leer umbral exacto del escaneo. Voyager documenta cambios del proceso CMOS RCA. Un transitorio en el semiconductor es otro mecanismo, desarrollado en el circuito compartido.

## 8. Una descarga puede entrar en la señal

Tiempo: 1:30

«Las placas y los bobinados tienen materiales aislantes. Pueden acumular carga o conducir más; según las condiciones, una descarga puede inyectar un pulso en una conexión. La pista puede estar sana y conducir ese pulso hasta otra entrada. Importan los retornos y la conexión entre partes, además de proteger cada chip.

En un transformador debemos separar el núcleo, el bobinado y su aislamiento. También puede pasar que el transistor de mando entregue un pulso incorrecto a un magnético sano. Algo similar ocurre con un relé: si recibe una orden equivocada suficientemente larga, puede conectar una carga aunque no esté dañado.

Esta explicación general se basa en manuales NASA. Cuando no conocemos el material o modelo de vuelo lo dejamos explícito; tampoco confundimos una soldadura fatigada con daño por radiación.»

FUENTES Y LOCALIZADORES
[S25](04_fuentes.md#s25) §4.1; [S26](04_fuentes.md#s26) §10.2.6.5; [S03](04_fuentes.md#s03) p. 16; [S08](04_fuentes.md#s08) §5.G.
S25 — NASA HDBK 4002B Mitigating In Space Charging Effects
https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/2022-06-07-NASA-HDBK-4002B-Approved.pdf
S26 — MIL HDBK 978B NASA Parts Application Handbook Volume 4
https://nepp.nasa.gov/files/21544/MIL-HDBK-978B_vol4.pdf
S03 — Voyager Backgrounder
https://ntrs.nasa.gov/api/citations/19810023559/downloads/19810023559.pdf
S08 — A Plasma Wave Investigation for the Voyager Mission
https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/pwsinst.htm

LECTURA DE LA FIGURA
Izquierda: aislante y pista conceptual. La descarga solo ocurre bajo condiciones suficientes; las flechas no implican que toda carga produzca ruptura. Derecha: bobina de mando y contactos de un relé, no circuito completo ni modelo instalado. Una orden espuria suficientemente larga puede accionar un relé sano. Un pulso corto puede no hacerlo. Conectar verbalmente aislamiento, retornos y validación del mando como criterios generales; S03 documenta relés de potencia Voyager, sin identificar todos sus materiales.

## 9. La carga y la función del sensor

Tiempo: 1:00

«En un detector de partículas, recoger la carga producida por radiación es la función. En un sensor óptico esa misma interacción puede parecer una luz que no llegó. Con exposición también puede cambiar la eficiencia del detector. En Voyager se documentaron daños después de Júpiter y ajustes de respuesta: recalibrar puede recuperar utilidad científica, pero no elimina los defectos. La cadena óptica también depende de emisor y receptor. Para cuarzo hay evidencia de selección mediante irradiación de muestras de barras. No atribuimos todo error de reloj al cristal: su electrónica también puede sufrir espurios.»

FUENTES Y LOCALIZADORES
[S09](04_fuentes.md#s09); [S01](04_fuentes.md#s01) §§VII.I y VIII.F; [S26](04_fuentes.md#s26) §8.6.8; [S30](04_fuentes.md#s30).
S09 — Voyager CRS Instrument Problems
https://voyager.gsfc.nasa.gov/instrument_problems.html
S01 — Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf
S26 — MIL HDBK 978B NASA Parts Application Handbook Volume 4
https://nepp.nasa.gov/files/21544/MIL-HDBK-978B_vol4.pdf
S30 — Voyager 1 and 2 Cosmic Ray Subsystem PDS
https://pds.nasa.gov/data/vg1-j-pls-5-summ-ele-mom-96.0sec-v1.1/vg_1501/document/crs/crsdata.htm

LECTURA DE LA FIGURA
Las dos figuras muestran la misma interacción con significado funcional distinto. No representan la geometría de detectores Voyager. La calibración puede compensar cambios de respuesta sin reparar defectos. Cuarzo: símbolo de resonador piezoeléctrico conectado funcionalmente a la referencia de reloj; no oscilador completo. S01 documenta selección de barras mediante irradiación. La electrónica del oscilador puede introducir espurios aunque el resonador no cambie permanentemente.

## 10. Un pulso breve, una orden persistente

Tiempo: 1:15

«Imaginemos que aparece un pulso falso en un amplificador. Si supera el umbral del comparador y el receptor lo acepta, un registro cambia y ordena activar una carga. El amplificador se recupera, pero el registro sigue dando la orden. No se rompió necesariamente ninguna pieza. Si el pulso era demasiado corto, pequeño o llegó fuera del momento de captura, esa consecuencia puede no ocurrir.

Un filtro puede reducir ciertas perturbaciones; validar la duración puede rechazar otras; comprobar o restablecer el estado ayuda después. Pero filtrar también puede retrasar una señal legítima. Son decisiones de circuito que hay que verificar, no soluciones universales. Este ejemplo explica el mecanismo y no reconstruye una falla concreta de Voyager.»

FUENTES Y LOCALIZADORES
[S35](04_fuentes.md#s35) §§2 y 4; [S22](04_fuentes.md#s22) SET. Modelo propio, dossier §5.7.
S35 — Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices
https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf
S22 — JPL ASIC Guide Design for Radiation Tolerance
https://parts.jpl.nasa.gov/asic/Sect.3.4.html

LECTURA DE LA FIGURA
Mismo esquema conceptual de la diapositiva 4. Las trazas comparten escala temporal conceptual, sin valores numéricos. La salida analógica vuelve al nivel inicial; el registro conserva el cambio si el comparador y la captura aceptan el pulso. No se afirma que todo pulso quede registrado ni que el esquema reproduzca una avería Voyager. Filtrado y validación pueden limitar propagación; recuperación de estado actúa después.

## 11. La protección actúa en varios niveles

Tiempo: 1:45

«Los informes de Voyager muestran ensayos de componentes, análisis de peor caso, selección, cambios de fabricación y blindaje específico. La arquitectura y el trabajo desde Tierra permitieron recuperar funciones. Cada medida trata un problema: reducir exposición no es lo mismo que tolerar una ganancia menor o corregir un estado erróneo.

La evidencia también obliga a separar causas. Hay daño radiativo documentado en detectores tras Júpiter. En 2010 se corrigió un bit alterado, pero eso no identifica por sí solo una partícula causante. En 2024 se recuperó telemetría reubicando código tras una falla de memoria, cuya causa física no quedó resuelta entre las posibilidades publicadas. Además, apagar instrumentos para ahorrar energía no demuestra que esos instrumentos hayan sido destruidos por radiación.

La conclusión es que la radiación puede alterar señales y parámetros. El diseño debe limitar ambas cosas y sus consecuencias. Voyager continúa produciendo ciencia con capacidades reducidas: eso muestra resistencia y recuperación del sistema, no ausencia de efectos.»

FUENTES Y LOCALIZADORES
[S01](04_fuentes.md#s01), [S02](04_fuentes.md#s02), [S03](04_fuentes.md#s03), [S04](04_fuentes.md#s04), [S07](04_fuentes.md#s07), [S09](04_fuentes.md#s09), [S10](04_fuentes.md#s10), [S11](04_fuentes.md#s11), [S12](04_fuentes.md#s12), [S13](04_fuentes.md#s13), [S14](04_fuentes.md#s14), [S15](04_fuentes.md#s15), [S16](04_fuentes.md#s16). Presentar estado de instrumentos solo con fecha de corte si surge la pregunta.
S01 — Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf
S02 — Voyager Electronic Parts Radiation Program Volume II
https://ntrs.nasa.gov/api/citations/19790006102/downloads/19790006102.pdf
S03 — Voyager Backgrounder
https://ntrs.nasa.gov/api/citations/19810023559/downloads/19810023559.pdf
S04 — Computers in Spaceflight The NASA Experience
https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf
S07 — Where Are Voyager 1 and 2 Now
https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/
S09 — Voyager CRS Instrument Problems
https://voyager.gsfc.nasa.gov/instrument_problems.html
S10 — Voyager 2 FDS reset May 2010
https://voyager.gsfc.nasa.gov/Library/V2_FDS_reset.pdf
S11 — Engineers Pinpoint Cause of Voyager 1 Issue
https://science.nasa.gov/blogs/voyager/2024/04/04/engineers-pinpoint-cause-of-voyager-1-issue-are-working-on-solution/
S12 — Voyager 1 Resumes Sending Engineering Updates
https://www.jpl.nasa.gov/news/nasas-voyager-1-resumes-sending-engineering-updates-to-earth/
S13 — Voyager Will Do More Science With New Power Strategy
https://www.jpl.nasa.gov/news/nasas-voyager-will-do-more-science-with-new-power-strategy/
S14 — NASA Shuts Off Instrument on Voyager 1
https://science.nasa.gov/blogs/voyager/2026/04/17/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/
S15 — NASA Engineers Help Prolong Voyager 2 Science Mission
https://science.nasa.gov/blogs/voyager/2026/08/04/nasa-engineers-help-prolong-voyager-2s-science-mission/
S16 — NASA Turns Off 2 Voyager Science Instruments
https://science.nasa.gov/blogs/voyager/2025/03/05/nasa-turns-off-2-voyager-science-instruments-to-extend-mission/

LECTURA DE LA FIGURA
El contorno representa conceptualmente protección alrededor del equipo, no distribución real de blindaje. S01 documenta blindaje específico, ensayos, selección y cambios de proceso. S04 documenta arquitectura redundante. En 2010 se corrigió un bit; no identifica por sí solo radiación. En 2024 se reubicó código ante falla de memoria con causa física no resuelta. Energía y temperatura también limitan. No atribuir a radiación apagados de ahorro energético.

## 12. Fuentes para seguir la explicación

Tiempo: 0:30

Documentos principales para respaldar mecanismos, hardware y mitigación. Los informes de 2005, 2012 y 2022 no prueban por sí mismos prácticas Voyager.

S01: Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf

S02: Voyager Electronic Parts Radiation Program Volume II
https://ntrs.nasa.gov/api/citations/19790006102/downloads/19790006102.pdf

S04: Computers in Spaceflight The NASA Experience
https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf

S08: A Plasma Wave Investigation for the Voyager Mission
https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/pwsinst.htm

S09: Voyager CRS Instrument Problems
https://voyager.gsfc.nasa.gov/instrument_problems.html

S21: Radiation Effects on Electronics 101 Kenneth LaBel
https://nepp.nasa.gov/DocUploads/392333B0-7A48-4A04-A3A72B0B1DD73343/Rad_Effects_101_WebEx.pdf

S25: NASA HDBK 4002B Mitigating In Space Charging Effects
https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/2022-06-07-NASA-HDBK-4002B-Approved.pdf

S35: Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices
https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf

S36: Hydrogen Contamination and Its Correlation with Enhanced Low-Dose-Rate Sensitivity
https://nepp.nasa.gov/files/25742/12_162_JPL_Adell_Hydrogen%20Contamination%20rec%201%207%2014.pdf

## 13. Respaldo: la ganancia depende del ensayo

Tiempo: respaldo

S01 fig. 7-1, p. 7-3, PDF 101. Incremento de ganancia inversa frente a corriente de colector. Fluencia 5 × 10¹² electrones/cm². Comparar las curvas de fabricantes del 2N2222; no afirmar que el modelo comercial fija susceptibilidad ni que cada curva corresponde a una pieza instalada.
S01: Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf

## 14. Respaldo: un transitorio medido

Tiempo: respaldo

S35 p. 4, fig. 1. Ejemplo de circuito lineal, no Voyager. Condiciones: LET 9 MeV·cm²/mg, Vcc ±15 V, V+ 5 V. Eje temporal en segundos, marcas de microsegundos. La salida vuelve al nivel inicial. El receptor podría haber capturado un cambio.
S35: Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices
https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf

## 15. Respaldo: las computadoras de Voyager

Tiempo: respaldo

Los pares representan redundancia de arquitectura; no implica duplicación idéntica de todas las funciones y estados en cualquier fecha. S04 pp. 182–184 describe prototipos TTL y evolución del FDS a CMOS. S01 §VI.B documenta 28 funciones CMOS usadas. No asignar TTL a todas las computadoras.
S01: Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf

S03: Voyager Backgrounder
https://ntrs.nasa.gov/api/citations/19810023559/downloads/19810023559.pdf

S04: Computers in Spaceflight The NASA Experience
https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf

S05: Voyager Frequently Asked Questions
https://science.nasa.gov/mission/voyager/frequently-asked-questions/

## 16. Respaldo: qué demuestran los ensayos

Tiempo: respaldo

S01 p. 7-53 PDF 151. Resistencias Dale CDP16, CDP18, LDP16 y SDP16. Capacitores: seis muestras de cada valor, no inventario instalado. La evidencia corresponde a esos parámetros y condiciones. Capacitancia estable no demuestra ausencia de fuga transitoria. La fluencia de esta lámina no se confunde con dosis absorbida. La errata de S02 tabla A-2 se explica en el dossier.
S01: Voyager Electronic Parts Radiation Program Volume I
https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf

S02: Voyager Electronic Parts Radiation Program Volume II
https://ntrs.nasa.gov/api/citations/19790006102/downloads/19790006102.pdf