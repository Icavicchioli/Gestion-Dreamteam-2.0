# Homologaciones: a qué organismos acudir y qué pedirles

**Proyecto:** drones para monitoreo y detección de plagas en soja, maíz y sorgo.  
**Fecha de consulta:** 9 de septiembre de 2026.  
**Alcance:** imágenes RGB/multiespectrales, análisis y asesoramiento agronómico; posibles sensores terrestres con LoRa. Sin pulverización ni intervención sobre fauna, conforme a las especificaciones del repositorio.

## Respuesta para el grupo

**Agenda práctica:** ver [Trámites, correos y webs oficiales](Homologaciones_contactos_y_tramites.md), con canales de contacto, procedimientos de registro y laboratorios para consultar ensayos.

No hay que buscar un único organismo que certifique todo el servicio. Hay tres frentes principales: **ANAC para la operación del dron, ENACOM para los equipos de comunicaciones y un ingeniero agrónomo habilitado por el colegio profesional de la jurisdicción para respaldar el diagnóstico y las recomendaciones**. Para demostrar que el análisis de imágenes funciona, corresponde preparar ensayos con un agrónomo y consultar a INTA o una universidad sobre colaboración técnica. Esa validación no equivale a una homologación estatal.

## Organismos e interlocutores

| Frente | A quién acudir | Qué pedir o comprobar | Cuándo aplica / resultado esperado |
|---|---|---|---|
| Operación del dron | **ANAC**, especialmente el Registro Nacional de Aeronaves y el área competente en RPA/RPAS | Encuadre de la operación; registro del equipo; requisitos del piloto y del explotador según categoría. Presentar peso, tipo de dron, ubicación, altura y modalidad de vuelo. | Para el servicio base, verificar que la misión cumple la categoría Abierta. Obtener la constancia registral exigible. No asumir que todo vuelo comercial requiere licencia o CETA. [1][2] |
| Uso del espacio aéreo | **EANA**, área de afectación/reserva de espacio aéreo, y autoridad del aeródromo cuando corresponda | Revisar restricciones y tramitar autorización/coordinación si la operación afecta espacio aéreo controlado u otro caso que la requiera. | Depende del lugar y misión; no es una homologación del dron ni un permiso universal para cada lote rural. Canal publicado: **reacentral@eana.com.ar**. [3] |
| Radios y comunicaciones | **ENACOM**; primero, proveedor/importador del equipo | Comprobar inscripción y conformidad aplicable en **RAMATEL**, identificando marca, modelo y configuración de radios del dron, control, video, módulos LoRa y gateway. Consultar banda, potencia y antenas permitidas. | Antes de comprar o integrar. Si el equipo ya cuenta con conformidad aplicable, reunir evidencia; si es propio, modificado o sin documentación, consultar el procedimiento y los ensayos correspondientes. [4][5] |
| Responsabilidad agronómica | **Colegio/consejo profesional de la provincia donde se presta el servicio** y agrónomo matriculado | Verificar matrícula y alcance profesional; acordar quién valida diagnósticos, recomendaciones e informes y qué formalidades corresponden. | Necesario para organizar el componente profesional del servicio. En Buenos Aires: **CIAFBA**; en Córdoba: **CIAPC**; Santa Fe: **CIASFE**; Entre Ríos: **COPAER**. Verificar la habilitación territorial concreta. [6] |
| Validación de imágenes y algoritmo | **INTA**, estación experimental o equipo especializado; alternativamente, una facultad de agronomía o laboratorio competente | Consultar disponibilidad para diseñar ensayos, realizar muestreos de campo y contrastar resultados del sistema con observaciones independientes. | Colaboración técnica propuesta, sujeta a aceptación y presupuesto. Pedir un informe de desempeño con alcance y limitaciones; no presentarlo como aprobación regulatoria. INTA publica servicios de ensayos, diagnóstico y consultoría. [7] |
| Diagnósticos con reconocimiento oficial | **SENASA**, área de sanidad vegetal y, para ensayos oficiales, Dirección General de Laboratorios y Control Técnico / REDLAB | Consultar el circuito específico si se pretende emitir resultados oficiales o intervenir en un programa sanitario. Para muestras oficiales, verificar laboratorio y rubro autorizados. | Condicional. La REDLAB regula ensayos sobre muestras oficiales; no permite concluir que todo software de monitoreo deba inscribirse como laboratorio. [8] |
| Datos personales | **AAIP** | Revisar obligaciones del responsable, inscripción de bases alcanzadas, información a titulares y tratamiento/transferencia de datos personales. | Si imágenes, ubicaciones u otros registros permiten identificar personas. No es una homologación de la cámara ni del algoritmo. [9] |
| Condiciones territoriales | **Autoridad agropecuaria provincial y municipio/comuna del lote** | Consultar requisitos locales concretos del servicio y de las recomendaciones. Si se incorpora prescripción de fitosanitarios, verificar receta y registros exigibles. | La provincia y el municipio todavía deben definirse. No corresponde trasladar automáticamente registros de pulverizadores al servicio de observación. |

## Las tres preguntas del chat

### 1. ¿Quién certifica las imágenes para el diagnóstico?

En las fuentes consultadas **no se identificó un trámite general de homologación estatal de imágenes o algoritmos para el monitoreo agronómico privado descrito**. Esto es una conclusión acotada al alcance del proyecto, no una certificación de ausencia de requisitos para cualquier uso futuro.

La propuesta concreta es incorporar un agrónomo habilitado y consultar a INTA o una universidad para validar el método. El colegio controla la habilitación profesional; el agrónomo interpreta y respalda el diagnóstico; la institución técnica puede colaborar en los ensayos. Ninguno de esos roles debe confundirse con un sello de aprobación universal del software.

Los ensayos deberían comparar las alertas con muestreos en campo, separar resultados por cultivo/plaga y medir falsas alarmas, detecciones omitidas y condiciones de uso. Las efectividades y resoluciones propuestas en el repositorio son hipótesis de diseño hasta que se demuestren. Detectar estrés o daño visible no demuestra por sí solo cuál es la plaga causante.

Si se quiere emitir un diagnóstico **oficial**, el interlocutor pasa a ser SENASA para definir el circuito aplicable. Su autorización REDLAB corresponde al laboratorio y rubro de ensayo, no automáticamente al servicio completo de drones. [7][8]

### 2. ¿Quién homologa las comunicaciones para no generar interferencias?

**ENACOM**, mediante el régimen de conformidad e inscripción aplicable a los equipos de telecomunicaciones. El primer paso práctico es pedir al proveedor la documentación y contrastarla con los registros oficiales. RAMATEL es un registro, no otro organismo. [4][5]

Hay que revisar el sistema real: transmisor del dron, control, video y sensores/gateway si se incorporan. Si cambiamos antenas, potencia, módulo o configuración regional, debemos consultar si la conformidad existente sigue cubriendo el equipo integrado. La documentación de un componente no permite dar por aprobado cualquier montaje final.

La conformidad regulatoria tampoco demuestra por sí sola la confiabilidad del enlace en el campo. Como verificación técnica del proyecto, corresponde ensayar alcance, coexistencia, pérdida de mensajes y contingencias. La banda LoRa propuesta en el repo debe verificarse junto con los parámetros técnicos y modelo elegidos antes de cerrar la compra.

### 3. ¿Quién autoriza o certifica el vuelo?

**ANAC** define el régimen aeronáutico y los requisitos de registro, piloto, explotador y operación. Su información publicada distingue categorías: en Abierta no exige licencia de piloto a distancia ni CETA; otras operaciones pueden activar requisitos adicionales. Por eso no conviene presupuestar una certificación aeronáutica genérica sin definir primero equipo y misión. [1][2]

**EANA** interviene en la coordinación y autorización del espacio aéreo cuando corresponda. Para consultar, preparar coordenadas del lote, fechas, altura, equipo y responsable. La página de EANA describe el procedimiento y los canales por región de vuelo. [3]

El documento normativo previo del repo señala diferencias entre textos y guías aeronáuticas, especialmente para vuelos rurales fuera del alcance visual. Este relevamiento no resuelve esas diferencias: para el piloto inicial se mantiene la decisión del proyecto de operar dentro del alcance visual; cualquier ampliación requiere revisar las RAAC vigentes y consultar el caso concreto a ANAC.

## Consultas listas para adaptar

**ANAC:** “Estamos desarrollando un servicio de monitoreo agrícola por imágenes, sin aplicación de productos. Utilizaremos [modelo/tipo], de [peso máximo de despegue], en [ubicación], a [altura], dentro del alcance visual y con rutas automáticas supervisadas. ¿Qué categoría y requisitos de registro, piloto, explotador y documentación corresponden? ¿Qué cambia si ampliamos el alcance de vuelo?”

**Proveedor / ENACOM:** “Necesitamos verificar la conformidad en Argentina de [marca y modelo del dron/control/radio/gateway]. ¿Pueden indicar número RAMATEL, documentación aplicable, bandas, potencia y antenas admitidas? Integraremos [módulo y antena]; ¿la documentación cubre esta configuración o requiere evaluación adicional?”

**Colegio profesional:** “El servicio generará mapas de indicios de plagas e informes agronómicos en [provincia]. ¿Qué matrícula, intervención profesional, firma y registros corresponden para validar diagnósticos y recomendaciones? Si se recomiendan productos y dosis, ¿qué requisitos adicionales aplican?”

**INTA / universidad:** “Buscamos validar detección de [plaga/daño] en [cultivo] mediante imágenes [sensor y resolución]. ¿Tienen un equipo que pueda colaborar en un protocolo con muestreo de campo independiente y evaluación de errores? Solicitamos alcance, disponibilidad, presupuesto y tipo de informe entregable.”

**SENASA, si se busca reconocimiento oficial:** “Nuestro sistema realiza monitoreo por imágenes y genera alertas, sin ensayos sobre muestras oficiales. Si quisiéramos que sus resultados se utilicen en [programa/trámite concreto], ¿qué validación, laboratorio autorizado o procedimiento exigirían?”

## Orden de trabajo propuesto

1. **Definir provincia, municipio, lote piloto, dron y radios.** Sin esos datos no se pueden cerrar requisitos ni costos.
2. **Consultar al proveedor y verificar RAMATEL antes de comprar.** Responsable propuesto: equipo de electrónica/comunicaciones.
3. **Encuadrar la misión ante ANAC y revisar el espacio aéreo.** Responsable propuesto: quien se encargue de la operación de vuelo.
4. **Incorporar un agrónomo con habilitación territorial.** Consultar al colegio las formalidades del servicio.
5. **Solicitar colaboración/presupuesto a INTA o universidad y ejecutar una validación de campo.** El equipo desarrolla el procesamiento; el diagnóstico de referencia necesita conocimiento agronómico.
6. **Cerrar los requisitos condicionales:** EANA según ubicación, AAIP según los datos tratados y provincia/municipio según actividad. SENASA si se busca un uso oficial o se amplía el alcance sanitario.

**Evidencia que debería quedar en la carpeta del proyecto:** encuadre y registro aeronáutico aplicables, autorizaciones de espacio aéreo cuando correspondan, documentación de radios, matrícula del agrónomo, protocolo e informe de validación y respuestas a consultas locales. Este documento es un relevamiento; no se realizaron contactos, trámites ni certificaciones.

## Fuentes y puntos de entrada oficiales

- **[1]** [ANAC — marco para operación de drones](https://www.argentina.gob.ar/anac/nuevo-marco-normativo-para-la-operacion-de-drones). Para el encuadre definitivo, contrastar con [RAAC vigentes](https://www.argentina.gob.ar/anac/regulaciones-argentinas-de-aviacion-civil-raac).
- **[2]** [ANAC — implementación del autorregistro](https://www.argentina.gob.ar/node/483764).
- **[3]** [EANA — servicios / afectación de espacio aéreo](https://www.eana.com.ar/servicios).
- **[4]** [ENACOM — consulta de equipos homologados](https://www.enacom.gob.ar/buscador/equipos%2Bhomologados/pagina) y [datos abiertos, equipos RAMATEL](https://enacom.gob.ar/datosabiertos).
- **[5]** [ENACOM — Resolución 57/2026](https://www.enacom.gob.ar/multimedia/normativas/2026/res57.pdf). Verificar el procedimiento vigente al seleccionar el equipo.
- **[6]** [CIAFBA — matrícula](https://ciafba.org/matricula) y [preguntas frecuentes y colegios de otras provincias](https://ciafba.org/preguntas-frecuentes).
- **[7]** [INTA — servicios de diagnóstico, ensayos y consultoría](https://www.argentina.gob.ar/inta/servicios-) y [buscador de diagnóstico de patógenos vegetales](https://www.argentina.gob.ar/inta/buscador-diagnosticos-patogenos-vegetales). El buscador de patógenos no cubre necesariamente todos los insectos o daños del proyecto.
- **[8]** [SENASA — REDLAB](https://www.argentina.gob.ar/senasa/laboratorios/rednacional-de-laboratorios) y [Resolución 1446/2024, arts. 1, 3 y 6](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-1446-2024-407180/texto).
- **[9]** [AAIP — obligaciones de responsables de bases de datos](https://www.argentina.gob.ar/aaip/datospersonales/responsables/obligaciones).

**Base interna:** `Especificaciones_marco_normativo_revisadas.md`, `../parte 1/Marco_normativo_drones_agro_Argentina.md` y `../parte 1/preguntas 3 sep 2026.txt`. Se tomó el alcance de esos archivos; las fuentes anteriores permiten distinguir autoridades, validadores técnicos y obligaciones condicionales sin repetir todo el marco legal.
