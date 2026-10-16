# Imágenes, fuentes y guía de lectura

La fuente técnica central es el volumen I del informe JPL 77-41. Las figuras extraídas conservan su contenido original. Las imágenes históricas complementan el contexto.

## Correspondencia con el informe

| Diapositiva y capítulo | Pasaje principal |
|---|---|
| 01. Voyager: radiación y decisiones electrónicas | §I, p. 1-1 / PDF 24; portada y ficha bibliográfica. |
| 02. Dos sondas y un recorrido de décadas | H1: historia NASA; H2: comunicado de 05/03/2025. |
| 03. Pioneer cambió las prioridades | §I; §III.A-B; §VI.A, p. 6-1 / PDF 81; §IX.A. |
| 04. El ambiente exterior y el que llega al circuito | §II, pp. 2-1 a 2-4 / PDF 25-28; §III.C, p. 3-6 / PDF 34. |
| 05. Partículas, fotones e ionización | §II; §III.D, pp. 3-7 a 3-8 / PDF 35-36; §VI.B, p. 6-2 / PDF 82. |
| 06. Las magnitudes que necesitamos | Tablas 2-1, 2-2 y 5-3; §III.C-D; §VII.F.3. |
| 07. La respuesta del programa | §III.A; §IV.A.2-3; §IV.B.5; §VI.B; §VII.K. H3 solo para arquitectura. |
| 08. Resistencias, capacitores y conexiones | §VII.H, p. 7-53 / PDF 151. Cálculos porcentuales y modelos RC: explicación didáctica. |
| 09. Diodos y acoplamientos ópticos | §VII.G; §VII.I, pp. 7-54 a 7-61 / PDF 152-159; figura 7-9. |
| 10. Bipolares: ganancia y punto de operación | §VII.B y C, pp. 7-2 a 7-9 / PDF 100-107; figura 7-1; §IX.B. |
| 11. JFET y conmutadores analógicos | §VII.C y E; §VIII.B.1 y D; §IX.C.4. |
| 12. MOS y CMOS: cambios que se superponen | §VI.B, pp. 6-1 a 6-3 / PDF 81-83, figura 6-1; §VII.F.1-2. |
| 13. Hardening de la familia CMOS RCA | §VI.B, pp. 6-1 a 6-2 / PDF 81-82; §VII.F.4; §VIII.E; §IX.C.1. |
| 14. LM108 y LM139: mejoras con contrapartidas | §VI.C.1-3, pp. 6-3 a 6-5 / PDF 83-85; §VII.D.1-2; figura 7-4. |
| 15. Memorias, registros y cuarzo | §VI.B, p. 6-2 / PDF 82; §VII.F, I.2 y J; §VIII.F, p. 8-41 / PDF 202. |
| 16. Screening: elegir las piezas de vuelo | §IV.B, pp. 4-14 a 4-24 / PDF 50-60; §VIII.A, D y E; §IX.B. |
| 17. Blindaje y margen de circuito | §II.D, tabla 2-2; §III.B-C, tabla 3-1; §VI.B. |
| 18. Las decisiones que dejó el programa | §IX, pp. 9-1 a 9-5 / PDF 204-208; casos de §§III, VI, VII y VIII. |

## Fuentes utilizadas

**JPL. [Voyager Electronic Parts Radiation Program, Volume I: Final Report](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf)**

A. G. Stanley, K. E. Martin y W. E. Price. JPL Publication 77-41, 15/09/1977. Fuente técnica central. Copia local en fuentes/.

**H1. [45 Years Ago: Voyager 1 Begins its Epic Journey to the Outer Planets and Beyond](https://www.nasa.gov/history/45-years-ago-voyager-1-begins-its-epic-journey-to-the-outer-planets-and-beyond/)**

NASA, 07/09/2022. Solo historia, encuentros e ilustraciones.

**H2. [NASA Turns Off 2 Voyager Science Instruments to Extend Mission](https://science.nasa.gov/blogs/voyager/2025/03/05/nasa-turns-off-2-voyager-science-instruments-to-extend-mission/)**

NASA, 05/03/2025. Solo distancias fechadas y contexto posterior.

**H3. [Computers in Spaceflight: The NASA Experience](https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf)**

James E. Tomayko, NASA, 1988, pp. 181-184. Complemento puntual para ubicar computadoras y almacenamiento; no aporta los casos de radiación.

El informe central se incluye en `fuentes/JPL_77-41_Volumen_I.pdf`. Su SHA-256 es `c5b5bff0cdcdbd7057172e0cbff3cec8d21e04403d22ed130f90d9a790a5934e`.

## Catálogo de imágenes

### 01_voyager.jpg

Diapositivas: 1.

Procedencia: NASA/JPL, spacecraft-profile-3. [Fuente](https://science.nasa.gov/image-detail/spacecraft-profile-3/).

Archivo de origen: `citas/presentacion_v3/portada.jpg`.

Alcance: Vista general de la nave; imagen de contexto.

SHA-256 de la copia: `be5ecfb387c32cb921e5ae485a329dd16f790114491f50ea8b642f68f8541581`.

### 02_trayectorias.png

Diapositivas: 2.

Procedencia: NASA, historia de Voyager 1 (S37). [Fuente](https://www.nasa.gov/wp-content/uploads/2022/09/voyager_1_6_trajectories_lightened.png).

Archivo de origen: `investigacion/imagenes_diapos/02_trayectorias.png`.

Alcance: Trayectorias históricas, no posiciones actuales.

SHA-256 de la copia: `331de2e25ce29c632b11b3e470a5b7d4b9cdd1d765dc551a85e4ccc5fb7eed32`.

### 03_jupiter.png

Diapositivas: 3.

Procedencia: Recorte ya existente de imagen NASA/JPL/Cassini. [Fuente](https://science.nasa.gov/photojournal/inner-radiation-belts-of-jupiter/).

Archivo de origen: `.build_slides/v3/assets/jupiter_detalle.png`.

Alcance: Contexto de cinturones jovianos. URL específica en catálogo original de imágenes v3.

SHA-256 de la copia: `2173b309dd514d04327604f71c4556fd4d27656231958b4fa28f5fead14a0b53`.

### 07_instrumentos.jpg

Diapositivas: 7.

Procedencia: NASA, historia de Voyager 1 (S37). [Fuente](https://www.nasa.gov/wp-content/uploads/2022/09/voyager_1_5_instruments.jpg).

Archivo de origen: `investigacion/imagenes_diapos/01_instrumentos.jpg`.

Alcance: Vista rotulada de instrumentos.

SHA-256 de la copia: `710f6f6cfe2665315060e56931d477ded36cc23624938f355c976c4a309326c6`.

### 18_integracion.jpg

Diapositivas: 18.

Procedencia: NASA/JPL, integración Voyager 2, marzo de 1977. [Fuente](https://science.nasa.gov/image-detail/pia21736/).

Archivo de origen: `citas/presentacion_v3/integracion.jpg`.

Alcance: Procedencia exacta en catálogo original de imágenes v3.

SHA-256 de la copia: `f964b0eb404e9b32104b302cbd7edb99abcc3b51e7a0a598bc6972f97c798f9a`.

### contexto_heliosfera.jpg

Diapositivas: 2; complemento.

Procedencia: NASA, historia de Voyager 1 (S37). [Fuente](https://www.nasa.gov/wp-content/uploads/2022/09/voyager_1_14_interstellar_mission.jpg).

Archivo de origen: `investigacion/imagenes_diapos/03_heliosfera.jpg`.

Alcance: Ilustración conceptual de la heliosfera.

SHA-256 de la copia: `b0b293c80283e9bcc9635b672bd09a1e95576c8c64a965a4664ee90b6154410e`.

### contexto_fds.png

Diapositivas: 7; complemento.

Procedencia: S04, fig. 6-2 p. 181; JPL foto 360-751AC. [Fuente](https://ntrs.nasa.gov/api/citations/19880069935/downloads/19880069935_Optimized.pdf).

Archivo de origen: `.build_slides/v3/assets/fds.png`.

Alcance: Hardware FDS. No identifica el vuelo del número de serie mostrado.

SHA-256 de la copia: `e81d1e7dbc71813e45484afd96c229e918f8be447e7eb5f91c3b27393cb5a1a3`.

### 08_pasivos_original.png

Diapositivas: 8; estudio.

Procedencia: S01, p. 7-53 / PDF 151. [Fuente](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf).

Archivo de origen: `investigacion/figuras/voyager_radiacion_vol1_1977_p151.png`.

Alcance: Página original de resultados de pasivos y diodos; no proyectar como texto pequeño.

SHA-256 de la copia: `7f1df84c72957c21caa12d96389e746b08d561f51d9eafda7f2bc2576c72c8be`.

### 09_circuito_optico.png

Diapositivas: 9.

Procedencia: JPL 77-41, vol. I, 7-9, PDF 155. [Fuente](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf).

Archivo de origen: `citas/voyager_radiacion_vol1_1977.pdf, PDF 155`.

Alcance: Circuito de ensayo, no placa de vuelo. Recorte de figura conservando ejes, rótulos y pie original.

SHA-256 de la copia: `3f05b5e32ff7732465e91a4377fc34fd54b57d98922df685f4fd5a7ca38ab33b`.

### 10_curvas_bipolares.png

Diapositivas: 10.

Procedencia: JPL 77-41, vol. I, 7-1, PDF 101. [Fuente](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf).

Archivo de origen: `citas/voyager_radiacion_vol1_1977.pdf, PDF 101`.

Alcance: Curvas históricas por tipo y fabricante. Recorte de figura conservando ejes, rótulos y pie original.

SHA-256 de la copia: `2c7fb1ead37130d35a06b57d86d3e13926f294620a822adfc6491975d56d0847`.

### 12_curvas_mos.png

Diapositivas: 12.

Procedencia: JPL 77-41, vol. I, 6-1, PDF 83. [Fuente](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf).

Archivo de origen: `citas/voyager_radiacion_vol1_1977.pdf, PDF 83`.

Alcance: Curvas medidas; umbral depende del criterio de corriente. Recorte de figura conservando ejes, rótulos y pie original.

SHA-256 de la copia: `cf2e5880cf861caf9010de6feb1d8fdee218891c3c6be1e4f25b3078fc6c0a4f`.

### 14_lm108.png

Diapositivas: 14.

Procedencia: JPL 77-41, vol. I, 7-4, PDF 112. [Fuente](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf).

Archivo de origen: `citas/voyager_radiacion_vol1_1977.pdf, PDF 112`.

Alcance: Comparación LM108 estándar/endurecido y circuito empleado. Recorte de figura conservando ejes, rótulos y pie original.

SHA-256 de la copia: `b4a79c4a22899ff284d91294a77ecb43b93e9154d5c9f83edc588406c77bb058`.

### 16_lotes_cmos.png

Diapositivas: 16.

Procedencia: JPL 77-41, vol. I, 8-21, PDF 201. [Fuente](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf).

Archivo de origen: `citas/voyager_radiacion_vol1_1977.pdf, PDF 201`.

Alcance: Comparación de lotes CD4053B. Recorte de figura conservando ejes, rótulos y pie original.

SHA-256 de la copia: `1d4fd7d491250a3cb6ac31ee2eee46b1912829cd8a7ff3fadb6f30b569b5f9b6`.

### 17_margen_original.png

Diapositivas: 17; estudio.

Procedencia: JPL 77-41, vol. I, tabla 3-1, PDF 34. [Fuente](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf).

Archivo de origen: `citas/voyager_radiacion_vol1_1977.pdf, PDF 34`.

Alcance: Requisito de blindaje del bus, no dosis actual.

SHA-256 de la copia: `69933d2dca08769ef22dab2d82d8bfc54aa40b61ab7bedff07ad7eff8f338be7`.

### fuente_portada.png

Diapositivas: 1; estudio.

Procedencia: JPL 77-41, vol. I, portada, PDF 1. [Fuente](https://ntrs.nasa.gov/api/citations/19780007219/downloads/19780007219.pdf).

Archivo de origen: `citas/voyager_radiacion_vol1_1977.pdf, PDF 1`.

Alcance: Portada del documento base.

SHA-256 de la copia: `effc678412f6d9a9be737d0b1f2ddc62a09a124d5f0644f5e8a519405d0ca4b0`.

## Recursos que no es necesario inventar

El esquema y el PowerPoint usan texto y tablas editables para los conceptos que no necesitan fotografía. Para agregar una foto de placa, buscar «Voyager Flight Data Subsystem JPL 360-751AC»; se incluye `contexto_fds.png` procedente de la historia NASA y debe conservar su identificación. No identifica por sí sola el número de serie que voló.

La ilustración `contexto_heliosfera.jpg` queda como recurso opcional para la historia. Su frontera no debe rotularse como fin de la gravedad solar. Para los inductores o capacitores de vuelo no se encontró en este volumen una fotografía y lista de materiales que permita identificar todas las piezas; los circuitos de ensayo se rotulan como tales.

## Cómo seguir el documento original

Las páginas 25-28 del PDF definen el ambiente. Las 29-36 explican las decisiones y el margen. Las 50-60 desarrollan screening. Las 81-85 presentan hardening CMOS y lineal; las tablas posteriores completan esa sección. Los resultados por familia comienzan en la 99. El screening por familia comienza en la 162. Las conclusiones están en 204-208.

El capítulo V describe instalaciones, dosimetría y procedimientos; se conserva solo el contexto necesario para interpretar resultados. Las tablas extensas quedan en el original: el dossier selecciona casos y conserva condiciones, sin convertir promedios o ensayos de un lote en garantías universales.
