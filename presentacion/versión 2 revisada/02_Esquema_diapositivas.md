# Esquema de las 18 diapositivas

Ignacio Cavicchioli · Versión 2 revisada · 16/10/2026

Duración prevista: 18 minutos, más 2 de margen. La duración real requiere ensayo oral. El texto de pantalla es independiente del apoyo oral. Las fechas y distancias se conservan con su referencia temporal.

## 01. Casi 50 años de electrónica en el espacio

**Tiempo previsto:** 0:25

### Texto para mostrar

Voyager lleva casi cinco décadas funcionando lejos de la Tierra. Vamos a recorrer las decisiones electrónicas que ayudaron a sostener esa misión.

### Texto adicional y datos del recurso visual

Ignacio Cavicchioli

1977–2026

### Apoyo oral

Voyager 1 y Voyager 2 se lanzaron en 1977. Durante estos minutos vamos a seguir su recorrido, identificar la radiación que encontraron y ver cómo afecta a los componentes. La pregunta es qué decisiones de diseño permitieron seguir trabajando pese a la degradación y los problemas que aparecieron.

### Imagen o recurso visual

`imagenes/01_voyager.jpg`. Identificar la antena y el cuerpo central. La imagen presenta la nave; no muestra sus circuitos internos.

### Fuentes y precisiones

S01, §I y §III; S22-S23, física general.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S07.** Where Are Voyager 1 and 2 Now. [consulta 2026-10-14](https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/)

**S09.** Voyager CRS Instrument Problems. [actualización indicada 2025-11-19](https://voyager.gsfc.nasa.gov/instrument_problems.html)

**S22.** JPL ASIC Guide Design for Radiation Tolerance. [sin fecha estable](https://parts.jpl.nasa.gov/asic/Sect.3.4.html)

**S23.** JPL ASIC Guide Appendix Three. [sin fecha estable](https://parts.jpl.nasa.gov/asic/Appendix.3.html)

## 02. Dos sondas, dos recorridos

**Tiempo previsto:** 1:10

### Texto para mostrar

Voyager 2 partió el 20 de agosto de 1977 y Voyager 1, el 5 de septiembre. Ambas visitaron Júpiter y Saturno; Voyager 2 continuó hacia Urano y Neptuno.

### Texto adicional y datos del recurso visual

Más de 25.000 millones de km: V1.
Más de 21.000 millones de km: V2.

Distancias a la Tierra · NASA, 05/03/2025

Proyecto aprobado en 1972; lanzamientos en 1977.

### Apoyo oral

El proyecto aprobado en 1972 llegó a los lanzamientos unos cinco años después, aunque había estudios anteriores. Voyager 2 salió primero, pero Voyager 1 llegó antes a Júpiter. El diseño inicial se centró en Júpiter y Saturno, con posibilidad de extender el viaje. Las distancias de referencia publicadas por NASA en marzo de 2025 superaban 25.000 millones de kilómetros para V1 y 21.000 millones para V2. Son distancias a la Tierra de esa fecha, no kilómetros recorridos ni posiciones exactas de hoy. Al 16 de octubre de 2026 faltan 308 días para los 50 años de V2 y 324 para los de V1.

### Imagen o recurso visual

`imagenes/02_trayectorias.png`. Seguir V1 hasta Saturno y V2 hasta Neptuno. El dibujo no representa distancias actuales.

### Fuentes y precisiones

S06, tabla de encuentros; S16, comunicado del 05/03/2025; S37, historia e imagen de trayectorias.

**S06.** Voyager Fact Sheet. [contenido histórico sin fecha única](https://science.nasa.gov/mission/voyager/fact-sheet/)

**S16.** NASA Turns Off 2 Voyager Science Instruments. [2025-03-05](https://science.nasa.gov/blogs/voyager/2025/03/05/nasa-turns-off-2-voyager-science-instruments-to-extend-mission/)

**S29.** The Voyage to Interstellar Space. [2019-03-27](https://www.nasa.gov/solar-system/the-voyage-to-interstellar-space/)

**S37.** 45 Years Ago: Voyager 1 Begins its Epic Journey to the Outer Planets and Beyond. [2022-09-07](https://www.nasa.gov/history/45-years-ago-voyager-1-begins-its-epic-journey-to-the-outer-planets-and-beyond/)

## 03. El recorrido define el ambiente

**Tiempo previsto:** 0:45

### Texto para mostrar

Durante el crucero, los encuentros planetarios y la etapa interestelar cambian las condiciones de exposición. El diseño debe responder a esos ambientes y a lo que cada componente puede tolerar.

### Texto adicional y datos del recurso visual

Interplanetario → magnetósferas → interestelar

### Apoyo oral

Vamos a distinguir tres situaciones: viajar entre planetas, atravesar una magnetósfera y explorar más allá de la heliopausa. No son compartimentos sin mezcla. En Júpiter se agregan poblaciones atrapadas muy intensas. Después de la heliopausa cambia el balance entre partículas solares y galácticas. También existen impactos, problemas térmicos y limitaciones de energía, pero el alcance de esta charla es electrónico.

### Imagen o recurso visual

`imagenes/03_heliosfera.jpg`. La frontera señalada corresponde al plasma y los campos heliosféricos, no al límite de la gravedad solar.

### Fuentes y precisiones

S01, §II; S25, §4; S29, transición a espacio interestelar.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S25.** NASA HDBK 4002B Mitigating In Space Charging Effects. [2022-06-07](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/2022-06-07-NASA-HDBK-4002B-Approved.pdf)

**S29.** The Voyage to Interstellar Space. [2019-03-27](https://www.nasa.gov/solar-system/the-voyage-to-interstellar-space/)

## 04. Las fuentes de radiación

**Tiempo previsto:** 0:55

### Texto para mostrar

Las partículas solares y los rayos cósmicos atraviesan el medio interplanetario. Cerca de los planetas se suman partículas atrapadas; los RTG aportan una fuente local durante toda la misión.

### Texto adicional y datos del recurso visual

| Fuente | Población relevante |
| --- | --- |
| Sol | Plasma y partículas energéticas |
| Galaxia | Protones, núcleos y electrones |
| Magnetósferas | Poblaciones atrapadas |
| RTG y calentadores | Neutrones y gamma externos |

### Apoyo oral

La fuente nos dice de dónde viene la radiación, pero todavía no qué partícula llega al circuito. Las cuatro fuentes se superponen. En Júpiter son decisivos los electrones atrapados; lejos de la heliosfera aumenta la importancia de la población galáctica. Los RTG agregan neutrones y fotones considerados en el diseño, aunque su combustible libera principalmente partículas alfa que quedan detenidas localmente.

### Imagen o recurso visual

`imagenes/04_jupiter.png`. Imagen de contexto de los cinturones jovianos. Las cuatro fuentes se explican en el texto y la tabla del dossier.

### Fuentes y precisiones

S01, §II y tabla 2-1; S17, composición galáctica; S38, RTG; S39, partículas solares.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S17.** Cosmic Rays Introduction NASA GSFC. [sin fecha estable](https://imagine.gsfc.nasa.gov/science/toolbox/cosmic_rays1_orig.html)

**S29.** The Voyage to Interstellar Space. [2019-03-27](https://www.nasa.gov/solar-system/the-voyage-to-interstellar-space/)

**S38.** NASA Voyager Spacecraft: RTG and subsystems. [consulta 16/10/2026](https://science.nasa.gov/mission/voyager/spacecraft/)

**S39.** NASA Space Radiation: What is space radiation?. [consulta 16/10/2026](https://srag.jsc.nasa.gov/SpaceRadiation/What/What.cfm)

## 05. Partículas, fotones e ionización

**Tiempo previsto:** 1:10

### Texto para mostrar

La radiación puede transportar energía mediante partículas o fotones. Al interactuar con un material puede generar cargas móviles, modificar enlaces o desplazar átomos de la red.

### Texto adicional y datos del recurso visual

| Radiación | Qué es |
| --- | --- |
| Protones y otros núcleos | Partículas con carga positiva |
| Electrones / beta | Electrones; beta también positrones |
| Alfa | Núcleos de helio-4 |
| Rayos X / gamma | Fotones sin carga |
| Neutrones | Partículas sin carga |

### Apoyo oral

Un protón es un núcleo de hidrógeno y una alfa es un núcleo de helio. Beta designa electrones o positrones emitidos en ciertos decaimientos; no vamos a llamar beta a cualquier electrón espacial. Gamma y rayos X son fotones, sin carga eléctrica. Los neutrones tampoco tienen carga, pero pueden transferir energía a núcleos y producir secundarios. Lo que altera el circuito es cómo se deposita esa energía y qué portadores o defectos quedan.

### Imagen o recurso visual

Tabla editable de especies, carga y forma de interacción; no hace falta una imagen decorativa.

### Fuentes y precisiones

S21, pp. 9 y 15-17; S23, física de interacción; S28, energía por par; S40, interacción de partículas y fotones.

**S17.** Cosmic Rays Introduction NASA GSFC. [sin fecha estable](https://imagine.gsfc.nasa.gov/science/toolbox/cosmic_rays1_orig.html)

**S21.** Radiation Effects on Electronics 101 Kenneth LaBel. [2004-04-21](https://nepp.nasa.gov/DocUploads/392333B0-7A48-4A04-A3A72B0B1DD73343/Rad_Effects_101_WebEx.pdf)

**S23.** JPL ASIC Guide Appendix Three. [sin fecha estable](https://parts.jpl.nasa.gov/asic/Appendix.3.html)

**S28.** CREME MC Sensitive Volumes Vanderbilt. [sin fecha estable](https://creme.isde.vanderbilt.edu/CREME-MC/help/sensitive-volumes)

**S40.** NASA THREE: Interactions of Radiation with Matter. [consulta 16/10/2026](https://three.jsc.nasa.gov/Encyclopedia/Article/4)

## 06. Tipo, energía, flujo y dosis

**Tiempo previsto:** 1:15

### Texto para mostrar

La energía ayuda a entender cómo interactúa la radiación y cuánto puede penetrar. El flujo cuenta lo que llega; la dosis mide la energía que el material absorbe por unidad de masa.

### Texto adicional y datos del recurso visual

| Característica | Qué expresa |
| --- | --- |
| Tipo | Especie de partícula o fotón |
| Energía | Energía incidente: eV, keV, MeV |
| Flujo | Partículas por área y tiempo |
| Dosis | Energía absorbida por masa |

Flujo acumulado en el tiempo = fluencia.

### Apoyo oral

Nos quedamos con cuatro características: tipo, energía, flujo y dosis. El flujo se expresa por área y tiempo. Si lo acumulamos obtenemos fluencia, que todavía no es dosis: falta saber cuánto se deposita y en qué masa. Una partícula muy energética puede atravesar el equipo y dejar solo parte de su energía. El blindaje cambia el espectro y también puede generar radiación secundaria. Para comparar dosis hay que indicar el material, por ejemplo silicio.

### Imagen o recurso visual

Tabla editable: tipo / energía / flujo / dosis; una aclaración breve distingue fluencia.

### Fuentes y precisiones

S21, pp. 9, 15-17 y 59-60; S28, pares en silicio; S40, transporte de radiación.

**S21.** Radiation Effects on Electronics 101 Kenneth LaBel. [2004-04-21](https://nepp.nasa.gov/DocUploads/392333B0-7A48-4A04-A3A72B0B1DD73343/Rad_Effects_101_WebEx.pdf)

**S28.** CREME MC Sensitive Volumes Vanderbilt. [sin fecha estable](https://creme.isde.vanderbilt.edu/CREME-MC/help/sensitive-volumes)

**S32.** JPL Horizons API Documentation. [2025-06](https://ssd-api.jpl.nasa.gov/doc/horizons.html)

**S40.** NASA THREE: Interactions of Radiation with Matter. [consulta 16/10/2026](https://three.jsc.nasa.gov/Encyclopedia/Article/4)

## 07. Qué contiene Voyager

**Tiempo previsto:** 0:35

### Texto para mostrar

Voyager combina fuentes de energía, estructura, instrumentos y circuitos electrónicos. Nos vamos a concentrar en estos circuitos y en los materiales que permiten que funcionen.

### Texto adicional y datos del recurso visual

Conductores, dieléctricos y semiconductores

### Apoyo oral

El RTG convierte calor en electricidad. La estructura sostiene el equipo y también forma parte del material que la radiación atraviesa. Hay metales, aislantes, cables e instrumentos. Vamos a concentrarnos en electrónica, pero incluir sus dieléctricos e interconexiones: un problema puede empezar en un aislante y terminar alterando una entrada.

### Imagen o recurso visual

`imagenes/07_instrumentos.jpg`. Localizar RTG, antena, cuerpo central e instrumentos. No confundir instrumento con computadora.

### Fuentes y precisiones

S03, pp. 15-20; S08, §5.C; S25, §4; S38, descripción RTG.

**S03.** Voyager Backgrounder. [1981](https://ntrs.nasa.gov/api/citations/19810023559/downloads/19810023559.pdf)

**S08.** A Plasma Wave Investigation for the Voyager Mission. [1977](https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/pwsinst.htm)

**S25.** NASA HDBK 4002B Mitigating In Space Charging Effects. [2022-06-07](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/2022-06-07-NASA-HDBK-4002B-Approved.pdf)

**S38.** NASA Voyager Spacecraft: RTG and subsystems. [consulta 16/10/2026](https://science.nasa.gov/mission/voyager/spacecraft/)

## 08. Computadoras, memoria y almacenamiento

**Tiempo previsto:** 0:55

### Texto para mostrar

Voyager distribuye el control y los datos entre CCS, AACS y FDS. Combina memorias magnéticas y CMOS con un grabador de cinta para almacenar información científica.

### Texto adicional y datos del recurso visual

CCS: comandos · AACS: orientación · FDS: datos

### Apoyo oral

CCS maneja comandos; AACS, orientación y articulación; FDS organiza datos. En la arquitectura original hay pares de procesadores, pero su redundancia no funciona igual en todos los casos. CCS y AACS usan memoria plated-wire y el FDS adoptó procesador y memoria CMOS. El prototipo FDS usó TTL: no hay que trasladar ese dato a todas las computadoras de vuelo. La cinta sirve para almacenar datos, no reemplaza todas las memorias.

### Imagen o recurso visual

`imagenes/08_fds.png`. Fotografía de S04, figura 6-2. No identifica la instalación de ese número de serie en V1 o V2.

### Fuentes y precisiones

S04, fig. 6-2 p. 181 y pp. 182-184; S03, pp. 16-20; S01, §VI.B; S41, grabador.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S03.** Voyager Backgrounder. [1981](https://ntrs.nasa.gov/api/citations/19810023559/downloads/19810023559.pdf)

**S04.** Computers in Spaceflight The NASA Experience. [1988](https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf)

**S05.** Voyager Frequently Asked Questions. [sin fecha estable](https://science.nasa.gov/mission/voyager/frequently-asked-questions/)

**S41.** NASA Images of Voyager: digital tape recorder. [consulta 16/10/2026](https://science.nasa.gov/gallery/images-of-voyager/)

## 09. Resistencias: valor y aislamiento

**Tiempo previsto:** 0:45

### Texto para mostrar

Una resistencia puede conservar su valor y aun así participar en una lectura incorrecta. Si aparece una corriente de fuga, una entrada de alta resistencia la convierte en una tensión apreciable.

### Texto adicional y datos del recurso visual

Entrada de antena del PWS

4 µA × 20 MΩ = 80 V

Resistencia especificada para 500 V.

Caso de carga de antena; S08, §5.G.

### Apoyo oral

El programa ensayó redes Dale de película metálica y no detectó cambios de resistencia dentro del error informado. Eso no vuelve inmune a todo el circuito: el soporte o los aislantes pueden conducir más y la resistencia convierte esa corriente en tensión. Un ejemplo real es la entrada de antena del PWS, donde una resistencia a masa limita el potencial de carga.

### Imagen o recurso visual

Ejemplo editable: 4 µA × 20 MΩ = 80 V. La copia del ensayo de pasivos está en imagen 09 para consulta.

### Fuentes y precisiones

S01, §VII.H.2 p. 7-53 / PDF 151; S08, §5.G; S25, §4.1.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S08.** A Plasma Wave Investigation for the Voyager Mission. [1977](https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/pwsinst.htm)

**S24.** Radiation Effects and Analysis Lessons Wyrwas Wilcox. [2022-06](https://nepp.nasa.gov/docs/etw/2022/16-JUN-THU/1600-Wyrwas-20220002512.pdf)

**S25.** NASA HDBK 4002B Mitigating In Space Charging Effects. [2022-06-07](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/2022-06-07-NASA-HDBK-4002B-Approved.pdf)

## 10. Capacitores: conservar el aislamiento

**Tiempo previsto:** 0:55

### Texto para mostrar

La radiación puede aumentar la conductividad del dieléctrico y hacer que el capacitor pierda carga más rápido. Por eso, comprobar su capacitancia no alcanza: también importa que conserve el aislamiento.

### Texto adicional y datos del recurso visual

| Mismo capacitor: 10 nF | Antes | Con mayor fuga |
| --- | --- | --- |
| Resistencia de fuga | 10 GΩ | 1 GΩ |
| Constante de tiempo | 100 s | 10 s |

Ejemplo general: C no cambia, la retención sí.

### Apoyo oral

Un capacitor real se puede pensar como una capacitancia con un camino de fuga en paralelo. La radiación puede modificar ese camino sin cambiar mucho C. Voyager ensayó capacitores B11B de teflón con variaciones pequeñas de capacitancia. El resultado es específico: no prueba que todos sus capacitores fueran de teflón ni que la fuga fuera siempre despreciable.

### Imagen o recurso visual

Modelo editable de C y fuga; ejemplo de constantes de tiempo. Imagen 09 conserva el ensayo original.

### Fuentes y precisiones

S01, §VII.H.1 p. 7-53 / PDF 151; S08, §5.G; S24, PDF 49.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S03.** Voyager Backgrounder. [1981](https://ntrs.nasa.gov/api/citations/19810023559/downloads/19810023559.pdf)

**S08.** A Plasma Wave Investigation for the Voyager Mission. [1977](https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/pwsinst.htm)

**S24.** Radiation Effects and Analysis Lessons Wyrwas Wilcox. [2022-06](https://nepp.nasa.gov/docs/etw/2022/16-JUN-THU/1600-Wyrwas-20220002512.pdf)

**S25.** NASA HDBK 4002B Mitigating In Space Charging Effects. [2022-06-07](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/2022-06-07-NASA-HDBK-4002B-Approved.pdf)

## 11. Bobinados, relés e interconexiones

**Tiempo previsto:** 0:50

### Texto para mostrar

En bobinas, relés y conexiones importa tanto el aislamiento como la señal de mando. Un componente sano puede ejecutar una orden equivocada o conducir una descarga hacia otro circuito.

### Texto adicional y datos del recurso visual

Mando → bobina → contactos → carga

Inductores y transformadores: conductor, núcleo y aislante.
Pistas, soldaduras y conectores: camino de la corriente.
Placas y encapsulados: aislamiento y carga retenida.

### Apoyo oral

En un inductor distinguimos cobre, aislante y núcleo; no hay que atribuirles el mismo mecanismo. Para Voyager no identificamos el barniz o el núcleo de cada magnético. Sí hay distribución de potencia con relés. Si la radiación altera un registro de mando, un relé sano puede obedecerlo. Las pistas, conectores y encapsulados también participan: una descarga puede viajar por ellos sin que el cobre se haya degradado.

### Imagen o recurso visual

Diagrama funcional editable: mando → bobina → contactos → carga. No representa un plano de vuelo.

### Fuentes y precisiones

S03, pp. 16-17; S08, §§5.C y 5.G; S25, §4.1; S26, §10.2.6.5.

**S03.** Voyager Backgrounder. [1981](https://ntrs.nasa.gov/api/citations/19810023559/downloads/19810023559.pdf)

**S08.** A Plasma Wave Investigation for the Voyager Mission. [1977](https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/pwsinst.htm)

**S25.** NASA HDBK 4002B Mitigating In Space Charging Effects. [2022-06-07](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/2022-06-07-NASA-HDBK-4002B-Approved.pdf)

**S26.** MIL HDBK 978B NASA Parts Application Handbook Volume 4. [1988-03-01](https://nepp.nasa.gov/files/21544/MIL-HDBK-978B_vol4.pdf)

## 12. Diodos y optoelectrónica

**Tiempo previsto:** 0:55

### Texto para mostrar

Una unión puede recoger carga generada por radiación y producir una corriente inesperada. En un detector esa carga puede ser la señal buscada; en otro circuito puede convertirse en un error.

### Texto adicional y datos del recurso visual

LED, fotodiodos y acoplamientos ópticos

### Apoyo oral

La región de agotamiento de una unión tiene un campo que separa portadores. Si la radiación genera pares allí o cerca, parte de esa carga llega a los terminales. Puede haber un pulso sin daño permanente; con defectos acumulados, puede aumentar la fuga. En un LED, mayor recombinación no radiativa puede reducir luz. En una pareja emisor-receptor interesa la respuesta de toda la cadena.

### Imagen o recurso visual

`imagenes/12_union.png`. Figura de principio, ajena al hardware Voyager. Identificar región de agotamiento y colección de portadores.

### Fuentes y precisiones

S01, §§VII.G.3 y VII.I, PDF 151-152; S09, daño en Júpiter; S35, §2.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S09.** Voyager CRS Instrument Problems. [actualización indicada 2025-11-19](https://voyager.gsfc.nasa.gov/instrument_problems.html)

**S21.** Radiation Effects on Electronics 101 Kenneth LaBel. [2004-04-21](https://nepp.nasa.gov/DocUploads/392333B0-7A48-4A04-A3A72B0B1DD73343/Rad_Effects_101_WebEx.pdf)

**S23.** JPL ASIC Guide Appendix Three. [sin fecha estable](https://parts.jpl.nasa.gov/asic/Appendix.3.html)

**S35.** Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices. [2005-10-24](https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf)

## 13. TBJ: recombinación y ganancia

**Tiempo previsto:** 1:40

### Texto para mostrar

Los defectos pueden aumentar la recombinación y reducir la ganancia de un transistor bipolar. El circuito necesita conservar margen suficiente para amplificar o conmutar aun con esos parámetros degradados.

### Texto adicional y datos del recurso visual

A I_C fija: menor β requiere más I_B.

### Apoyo oral

En un NPN, el emisor inyecta electrones en una base delgada. Muchos llegan al colector y una parte se recombina. Si aparecen centros de recombinación, puede aumentar la corriente de base necesaria para sostener la corriente de colector. Por ejemplo, 10 mA con beta 100 necesitan 0,1 mA de base; con beta 50 necesitan 0,2 mA en el modelo activo. Eso no significa que cualquier corriente se reduzca siempre: hay que decir qué se mantiene fijo. El programa ensayó familias y fabricantes y diseñó con límites degradados. Además, una partícula puede provocar un pulso en una unión aunque no deje una pérdida permanente de ganancia.

### Imagen o recurso visual

`imagenes/13_tbj.png`. Sección general, no geometría de una pieza de vuelo. Explicar inyección, difusión, colección y recombinación.

### Fuentes y precisiones

S01, §VII.B, figura 7-1 y §III; S36, §3.2 PDF 24-26; S35, §§2 y 4.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S02.** Voyager Electronic Parts Radiation Program Volume II. [1978-12-15](https://ntrs.nasa.gov/api/citations/19790006102/downloads/19790006102.pdf)

**S23.** JPL ASIC Guide Appendix Three. [sin fecha estable](https://parts.jpl.nasa.gov/asic/Appendix.3.html)

**S35.** Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices. [2005-10-24](https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf)

**S36.** Hydrogen Contamination and Its Correlation with Enhanced Low-Dose-Rate Sensitivity. [2012-12](https://nepp.nasa.gov/files/25742/12_162_JPL_Adell_Hydrogen%20Contamination%20rec%201%207%2014.pdf)

## 14. JFET, MOSFET y CMOS

**Tiempo previsto:** 1:50

### Texto para mostrar

En un MOSFET, la carga atrapada en el óxido modifica el campo que controla el canal. Por eso puede cambiar el umbral y aumentar la fuga, incluso antes de que el transistor deje de funcionar.

### Texto adicional y datos del recurso visual

CMOS RCA: recocido de 1100 a 950 °C.

### Apoyo oral

El JFET controla un canal mediante una juntura; el MOSFET lo hace a través de un aislante. En el óxido, la ionización genera pares: una parte se recombina y otra deja carga atrapada o estados de interfaz. Eso cambia el campo y la tensión necesaria para lograr una condición de canal. No todos los efectos tienen el mismo signo ni siempre reducen la corriente. CMOS combina transistores n y p, de modo que sus cambios afectan márgenes y consumo. En Voyager hay una decisión de fabricación muy concreta: modificar el recocido del óxido de 1100 a 950 °C en la familia CMOS RCA. Son temperaturas de fabricación, no de operación de la sonda.

### Imagen o recurso visual

`imagenes/14_mos.png`. Identificar compuerta, óxido, canal y uniones. El dibujo ilustra conducción con V_G = 0 por carga positiva: es un caso posible, no una respuesta universal. No corresponde a una geometría Voyager.

### Fuentes y precisiones

S01, §VI.B PDF 81-83 y §VII.C; S22, TID e Interface Traps; S23, estructuras y física.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S02.** Voyager Electronic Parts Radiation Program Volume II. [1978-12-15](https://ntrs.nasa.gov/api/citations/19790006102/downloads/19790006102.pdf)

**S22.** JPL ASIC Guide Design for Radiation Tolerance. [sin fecha estable](https://parts.jpl.nasa.gov/asic/Sect.3.4.html)

**S23.** JPL ASIC Guide Appendix Three. [sin fecha estable](https://parts.jpl.nasa.gov/asic/Appendix.3.html)

## 15. Memorias y registros: un estado equivocado

**Tiempo previsto:** 1:20

### Texto para mostrar

Un pulso breve puede cambiar un estado que la memoria conserva después. Recuperar ese dato exige una acción adecuada; la desaparición del pulso no garantiza que el sistema vuelva al estado correcto.

### Texto adicional y datos del recurso visual

Carga recogida → pulso → estado alterado

El pulso desaparece. El dato puede quedar equivocado.

Ejemplo conceptual; no identifica una celda de Voyager.

### Apoyo oral

En una celda CMOS, la realimentación sostiene uno de dos estados. La carga de una partícula puede llevarla al otro, o un registro puede capturar un pulso que viene de otra etapa. El pulso termina, pero el bit equivocado queda. Reescribir puede corregirlo si no hubo daño; reiniciar no recupera automáticamente toda la información. Voyager tiene redundancia y alimentación de retención documentadas, pero esas medidas resuelven problemas diferentes. En 2010 se corrigió un bit de Voyager 2; la nota no prueba que lo causara un rayo cósmico.

### Imagen o recurso visual

Secuencia editable: carga recogida → pulso → captura → estado persistente. Ejemplo general, no simulación de una celda Voyager.

### Fuentes y precisiones

S04, pp. 182-184; S22, SEU/SET; S34, actualización 17/05/2010; S11, diagnóstico 04/04/2024.

**S04.** Computers in Spaceflight The NASA Experience. [1988](https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf)

**S10.** Voyager 2 FDS reset May 2010. [2010](https://voyager.gsfc.nasa.gov/Library/V2_FDS_reset.pdf)

**S11.** Engineers Pinpoint Cause of Voyager 1 Issue. [2024-04-04](https://science.nasa.gov/blogs/voyager/2024/04/04/engineers-pinpoint-cause-of-voyager-1-issue-are-working-on-solution/)

**S22.** JPL ASIC Guide Design for Radiation Tolerance. [sin fecha estable](https://parts.jpl.nasa.gov/asic/Sect.3.4.html)

**S34.** Engineers Diagnosing Voyager 2 Data System Update. [2010-05](https://www.jpl.nasa.gov/news/engineers-diagnosing-voyager-2-data-system-update/)

**S35.** Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices. [2005-10-24](https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf)

## 16. Amplificadores y referencias de tiempo

**Tiempo previsto:** 0:55

### Texto para mostrar

Una perturbación puede alterar una medida o una referencia de tiempo sin destruir el equipo. En amplificadores y osciladores importa conservar precisión, estabilidad y capacidad de recuperación.

### Texto adicional y datos del recurso visual

Amplificadores

Offset, ganancia y transitorios
pueden alterar una medida.

Cuarzo y osciladores

Frecuencia, pérdidas y electrónica
de reloj afectan el tiempo.

Voyager seleccionó barras de cuarzo mediante ensayos.

### Apoyo oral

Un amplificador puede transformar una corriente inducida en un pulso de salida y hasta saturarse brevemente. La dosis acumulada también puede cambiar offset, ganancia o consumo. En el cuarzo interesa la frecuencia y las pérdidas, pero el reloj además tiene electrónica susceptible a pulsos. Voyager seleccionó barras de cuarzo a partir de ensayos: es una medida concreta de aceptación de materiales.

### Imagen o recurso visual

Comparación editable entre precisión de amplitud y estabilidad temporal. La imagen 16 contiene transitorios generales NASA para estudio.

### Fuentes y precisiones

S01, §III y §VIII.F PDF 202; S26, §8.6.8; S35, PDF 4 y §§2.4/4.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S26.** MIL HDBK 978B NASA Parts Application Handbook Volume 4. [1988-03-01](https://nepp.nasa.gov/files/21544/MIL-HDBK-978B_vol4.pdf)

**S35.** Testing and Hardness Assurance Guidelines for Single Event Transients in Linear Devices. [2005-10-24](https://nepp.nasa.gov/docuploads/FE7A50F8-E974-462D-8642C727C445125F/SET_Linear05.pdf)

## 17. Exposición prevista y margen de diseño

**Tiempo previsto:** 0:55

### Texto para mostrar

El blindaje reduce parte de la exposición, pero no elimina todos los efectos. Voyager combinó esa protección con ensayos y márgenes para conservar la función de los circuitos.

### Texto adicional y datos del recurso visual

60 krad(Si) / 30 krad(Si) = 2

Capacidad de referencia / exposición local prevista

Ejemplo histórico de diseño, no dosis acumulada actual.

### Apoyo oral

Un ejemplo del programa usa una exposición local de referencia de 30 krad en silicio y una capacidad de 60: el margen es dos. No son dosis medidas hoy en todas las placas. Los componentes más sensibles tuvieron condiciones particulares; la memoria CMOS requería atención específica. Además, el blindaje puede generar secundarios. Se decide junto con selección, fabricación y diseño, no como una pared que resuelve todo.

### Imagen o recurso visual

Comparación editable: 30 krad(Si) previstos / 60 krad(Si) de capacidad de referencia = margen 2.

### Fuentes y precisiones

S01, tablas 2-1/2-2/3-1, §III.C y §VI.B; S02, apéndice A.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S02.** Voyager Electronic Parts Radiation Program Volume II. [1978-12-15](https://ntrs.nasa.gov/api/citations/19790006102/downloads/19790006102.pdf)

**S18.** Voyager CRS Data. [actualización indicada 2025-11-19](https://voyager.gsfc.nasa.gov/data.html)

**S19.** Voyager CRS Flux Time History. [consulta 2026-10-14](https://voyager.gsfc.nasa.gov/flux.html)

## 18. Las decisiones que siguen dando resultado

**Tiempo previsto:** 0:45

### Texto para mostrar

La misión siguió adelante porque sus circuitos se evaluaron para un ambiente concreto y conservaron margen para funcionar. La selección, el blindaje y la capacidad de recuperación actuaron juntos durante décadas.

### Texto adicional y datos del recurso visual

Ensayos, márgenes y recuperación de funciones

### Apoyo oral

Podemos volver a la pregunta inicial con ejemplos concretos: comprobar los pasivos, seleccionar cristales, modificar el proceso CMOS y calcular márgenes en el circuito. A eso se sumaron blindaje, redundancia y operaciones desde Tierra. Voyager también sufrió degradación y perdió capacidades. Lo valioso es haber conservado funciones útiles durante décadas. Entender qué puede cambiar en un componente permite diseñar para que ese cambio no termine inmediatamente con la misión.

### Imagen o recurso visual

`imagenes/18_integracion.jpg`. Fotografía de pruebas de 1977. Volver a decisiones tomadas antes del lanzamiento, sin atribuir inmunidad total.

### Fuentes y precisiones

Síntesis de S01-S02; S08, §5.G; S04, pp. 182-184; S09, degradación; S16, operación.

**S01.** Voyager Electronic Parts Radiation Program Volume I. [1977-09-15](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)

**S02.** Voyager Electronic Parts Radiation Program Volume II. [1978-12-15](https://ntrs.nasa.gov/api/citations/19790006102/downloads/19790006102.pdf)

**S04.** Computers in Spaceflight The NASA Experience. [1988](https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf)

**S08.** A Plasma Wave Investigation for the Voyager Mission. [1977](https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/pwsinst.htm)

**S09.** Voyager CRS Instrument Problems. [actualización indicada 2025-11-19](https://voyager.gsfc.nasa.gov/instrument_problems.html)

**S16.** NASA Turns Off 2 Voyager Science Instruments. [2025-03-05](https://science.nasa.gov/blogs/voyager/2025/03/05/nasa-turns-off-2-voyager-science-instruments-to-extend-mission/)
