# Radiación y supervivencia de los componentes electrónicos de Voyager

**Fecha de corte: 14 de octubre de 2026. Nivel: electrónica universitaria.**

Voyager permite estudiar un problema de ingeniería completo: una partícula o un flujo de partículas interactúa con materiales, modifica parámetros eléctricos y puede comprometer una función. La respuesta depende de la resistencia del dispositivo, el margen del circuito y la capacidad del sistema para seguir operando cuando algo falla. El interés está tanto en un dieléctrico o una resistencia como en un procesador.

La explicación mejor respaldada de su longevidad combina componentes evaluados para su ambiente, cambios de diseño y fabricación, blindaje, redundancia y operaciones desde Tierra. Hubo daños y pérdidas de capacidad. En particular, la documentación del CRS registra daño tras Júpiter, mientras que el estado actual distingue instrumentos apagados por energía de otros retirados por degradación. [[S01](04_fuentes.md#s01), [S09](04_fuentes.md#s09), [S07](04_fuentes.md#s07); bibliografía en **04_fuentes.md**]

Se usan tres etiquetas: **documentado** para un resultado explícito de una fuente; **inferido** para una consecuencia física razonada que no constituye una observación del hardware de vuelo; **no resuelto** cuando falta información para atribuir un material, valor o causa a Voyager. Un componente ensayado dentro del programa no equivale automáticamente a un componente instalado en una placa concreta.

## 1 Ambiente y medición

### 1.1 Qué radiación importa

Los rayos cósmicos galácticos son partículas energéticas procedentes de fuera del sistema solar, predominantemente núcleos de hidrógeno y helio, junto con núcleos más pesados y una componente leptónica. Las partículas llegan con un espectro amplio: decir «radiación cósmica» no fija energía, composición ni capacidad de penetración. La aceleración en remanentes de supernovas contribuye a la población galáctica; no todas las energías y poblaciones tienen un único origen. [[S17](04_fuentes.md#s17)]

Para un circuito hay que distinguir cuatro ambientes:

| Ambiente | Qué contiene y cómo varía | Pregunta de ingeniería |
|---|---|---|
| Rayos cósmicos galácticos | Protones, helio, iones pesados y otras partículas; la heliosfera modula sus espectros | ¿Qué carga puede depositar un evento en un volumen sensible? |
| Partículas energéticas solares | Eventos variables de protones, electrones e iones asociados con actividad solar | ¿Qué fluencia y tasa máxima debe soportarse? |
| Cinturones planetarios | Partículas atrapadas y aceleradas en magnetosferas | ¿Qué dosis y carga acumula cada posición durante el sobrevuelo? |
| Fuentes a bordo | Radiación asociada con RTG y calentadores radioisotópicos | ¿Qué exposición local agrega su posición y duración de uso? |

El viento solar, una onda de radio y un ion galáctico de alta energía no son amenazas equivalentes. La electrónica puede sufrir además **carga electrostática** por intercambio y acumulación de partículas; ese problema debe estudiarse junto con la radiación, aunque no se reduzca a TID o a errores de memoria. [[S21](04_fuentes.md#s21), pp. 4–14; [S25](04_fuentes.md#s25), §4.1; [S01](04_fuentes.md#s01), §II]

### 1.2 Magnitudes que no conviene mezclar

| Magnitud | Definición operativa | Unidades habituales | Qué permite calcular |
|---|---|---|---|
| Energía de una partícula | Energía cinética; para núcleos puede expresarse por nucleón | eV, MeV, GeV, MeV/nucleón | Penetración e interacción, junto con especie y material |
| Flujo de partículas | Tasa por área, con convención angular y rango energético especificados | cm⁻² s⁻¹ | Cuántas partículas llegan por unidad de tiempo |
| Intensidad diferencial j(E) | Distribución resuelta en energía y dirección | cm⁻² s⁻¹ sr⁻¹ MeV⁻¹ | Integración del espectro con una respuesta instrumental |
| Fluencia Φ | Flujo integrado en tiempo | cm⁻² | Exposición acumulada a partículas |
| Dosis absorbida D | Energía depositada por masa | Gy = J/kg; rad = 0,01 Gy | Exposición energética del material |
| TID | Parte de la dosis asociada con ionización | rad(Si), rad(SiO₂), Gy(material) | Degradación acumulada por ionización |
| Tasa de dosis | Dosis por tiempo | rad(Si)/s | Dependencia temporal y comparación de ensayos |
| LET | Transferencia de energía por longitud; a menudo normalizada por densidad | keV/µm; MeV·cm²/mg | Densidad de deposición de energía a lo largo de una trayectoria |
| NIEL y DDD | Pérdida no ionizante por masa superficial y daño de desplazamiento integrado | MeV·cm²/g; MeV/g | Comparar daño de red entre especies y energías |
| Tasa de cuentas | Eventos registrados por el instrumento | cuentas/s | Observación instrumental, antes de convertir a intensidad |

Definiciones de dosis y LET: [S21](04_fuentes.md#s21), pp. 9, 15–17, 59–60; [S22](04_fuentes.md#s22), sección TID. Flujo instrumental: [S18](04_fuentes.md#s18)–[S19](04_fuentes.md#s19). El símbolo LET también aparece en Voyager como **Low Energy Telescope**: escribir el nombre completo cuando pueda confundirse con transferencia lineal de energía.

Una intensidad por estereorradián no se convierte en flujo sobre una superficie multiplicando siempre por 4π. Para incidencia sobre una cara plana aparece el factor de proyección cosθ; para un detector se integra su aceptación angular y energética. Un modelo isotrópico y una superficie plana tienen una relación diferente a la fluencia escalar utilizada en transporte.

Las relaciones básicas, con sus convenciones ya fijadas, son:

```text
Φ = ∫ φ(t) dt
D = Edepositada / masa
1 krad = 10 Gy
Rcuentas = ∫ j(E,Ω) Aefectiva(E,Ω) dE dΩ
RSEE ≈ ∫ φ(E) σSEE(E) dE
```

La última ecuación es un modelo simplificado para una especie y una sección eficaz compatible con la definición de flujo. Para iones pesados puede utilizarse un espectro en LET y la respuesta medida del dispositivo, incluyendo geometría. La sección eficaz es una medida de susceptibilidad, no necesariamente el área geométrica del chip. Sin espectro local y respuesta experimental no se obtiene una tasa de fallas seria. [[S21](04_fuentes.md#s21), pp. 17–24; [S28](04_fuentes.md#s28)]

### 1.3 Dónde están y qué atravesaron

**Documentado.** Se lanzaron dos sondas: Voyager 2 el 20 de agosto de 1977 y Voyager 1 el 5 de septiembre de 1977. Al corte de este trabajo tienen, respectivamente, **49 años y 55 días** y **49 años y 39 días**, calculados con fechas civiles. «Casi 50 años» es correcto; «50 años cumplidos» todavía no. [[S06](04_fuentes.md#s06)]

| Sonda | Júpiter | Saturno | Otros sobrevuelos | Cruce de heliopausa |
|---|---|---|---|---|
| Voyager 1 | 5 marzo 1979 | 12 noviembre 1980 | Sin Urano ni Neptuno | 25 agosto 2012 |
| Voyager 2 | 9 julio 1979 | 25 agosto 1981 | Urano: 24 enero 1986; Neptuno: 25 agosto 1989 | 5 noviembre 2018 |

Fechas: [S06](04_fuentes.md#s06) y [S29](04_fuentes.md#s29). Ambas operan en espacio interestelar, fuera de la heliosfera. Esto no significa haber superado todas las regiones gravitacionalmente asociadas con el Sol. Para la presentación interesa el cambio de ambiente de partículas, no una frontera única del «fin del sistema solar».

**Distancias con fecha.** El comunicado del 17 de abril de 2026 sitúa a Voyager 1 a más de 25.000 millones de kilómetros de la Tierra. El del 5 de marzo de 2025 sitúa a Voyager 2 a más de 21.000 millones. Son referencias publicadas en esas fechas, no efemérides exactas del 14 de octubre de 2026. La página de estado consultada anuncia para el 18 de noviembre de 2026 un hito futuro de un día luz para Voyager 1. No debe narrarse como ya ocurrido. [[S14](04_fuentes.md#s14), [S16](04_fuentes.md#s16), [S07](04_fuentes.md#s07)]

El encuentro con Júpiter fue especialmente importante para la calificación. La evaluación previa identificaba a sus electrones como principal amenaza de daño interno; esto describe el ambiente de diseño planetario y no una dosis reconstruida de los 49 años completos. Tras cruzar la heliopausa cambió la población medida: disminuyeron partículas heliosféricas y aumentó la componente galáctica en los canales estudiados. [[S01](04_fuentes.md#s01), §II; [S29](04_fuentes.md#s29)]

### 1.4 Qué nivel de exposición podemos sostener

El informe de diseño de 1977 incluye, para el ambiente externo sin blindaje, un flujo pico de electrones de **2 × 10⁸ cm⁻² s⁻¹ para E > 0,4 MeV** y una fluencia de **4 × 10¹² cm⁻² equivalente a electrones de 3 MeV**. Son parámetros de diseño con umbrales y equivalencias distintos, no dos mediciones que deban dividirse para obtener el tiempo real del sobrevuelo. [[S01](04_fuentes.md#s01), tabla 2-1, p. 2-2, PDF 26]

Para electrónica de ingeniería en el bus, el requisito de blindaje era **30 krad(Si)** y la capacidad de referencia **60 krad(Si)**: margen 2. La memoria CMOS sensible recibió un tratamiento específico para no superar **10 krad(Si)** según el diseño. Ninguno de esos números es la dosis medida actualmente en todos los chips. [[S01](04_fuentes.md#s01), tablas 2-2 y 3-1; §VI.B]

**Medición reciente concreta.** El archivo GSFC descargado el 14 de octubre de 2026 termina en una media de seis horas iniciada el **4 de octubre de 2026 a las 06:00 UTC**: **2,369 cuentas/s**, con columna ERROR de **0,0257 cuentas/s**, en PGH/HET 1 de Voyager 2. El canal responde a núcleos por encima de 70 MeV/nucleón, principalmente protones. No se atribuye un nivel de confianza a ERROR que el encabezado no especifica. [[S20](04_fuentes.md#s20), última fila; [S33](04_fuentes.md#s33)]

Esa tasa acredita una observación de partículas, pero no equivale a 2,369 partículas/cm²/s ni a una dosis del circuito. GSFC advierte que los archivos de tasas no incorporan la corrección térmica aplicada a los productos de flujo tras apagar los calentadores. Por eso el dato sirve como ejemplo instrumental fechado, no para inferir por sí solo una variación física reciente del ambiente o daño acumulado. [[S18](04_fuentes.md#s18)–[S19](04_fuentes.md#s19)]

**No resuelto.** Una dosis absorbida acumulada por componente hasta 2026 requiere espectros, orientación, materiales, geometría de blindaje y transporte de secundarios a lo largo de la misión. La tasa externa del CRS no proporciona esa dosimetría. Tampoco hay una lectura contemporánea del CRS de Voyager 1, apagado para ahorrar energía en febrero de 2025. [[S07](04_fuentes.md#s07)]

## 2 De una partícula a una falla eléctrica

### 2.1 Ionización acumulada

La radiación puede transferir energía a electrones y generar portadores. En un conductor muchos se redistribuyen rápidamente; en un aislante parte de la carga puede quedar atrapada. En estructuras MOS, el óxido y su interfaz con el silicio son críticos: cargas atrapadas y estados de interfaz cambian el potencial que controla el canal. El resultado puede ser deriva de umbral, aumento de fugas, menor movilidad y pérdida de margen de conmutación. [[S22](04_fuentes.md#s22)–[S23](04_fuentes.md#s23)]

Para una carga efectiva positiva por unidad de área Qot, una aproximación electrostática es:

```text
Cox = εox / tox                 [F/cm²]
ΔVT ≈ −Qot / Cox                [V]
```

Es el término de carga efectiva en óxido, no una descripción completa de estados de interfaz ni de la distribución espacial de trampas. La misma dosis puede producir respuestas distintas según proceso, polarización, temperatura, tiempo y recocido. Por eso **TID no es un contador universal de vida útil**.

El recocido durante fabricación y la recuperación parcial de defectos después de irradiar son procesos diferentes. Que una fuente mencione annealing no permite decir que Voyager «se repara calentándose» durante toda la misión.

### 2.2 Desplazamiento atómico

Una colisión puede desplazar un átomo de la red y producir vacancias, intersticiales y complejos de defectos. Estos introducen centros de generación y recombinación: cambia la vida de portadores minoritarios, crecen corrientes oscuras o cae la eficiencia de colección. Son mecanismos relevantes en transistores bipolares, fotodiodos, detectores y emisores ópticos. Electrones suficientemente energéticos también pueden producir desplazamiento; no es un efecto exclusivo de neutrones. [[S21](04_fuentes.md#s21), p. 16]

En un modelo de daño por fluencia equivalente:

```text
1/τfinal ≈ 1/τinicial + K Φeq
```

K depende del material, partícula, energía y condiciones. Esta expresión muestra por qué una menor vida de minoritarios puede afectar ganancia o fotocorriente; no suministra K para Voyager. **Ionización en óxido y desplazamiento de red son mecanismos distintos**, aunque un mismo haz pueda causar ambos.

### 2.3 Eventos de partícula única

La carga depositada y recogida en un nodo puede producir un pulso, alterar un estado o disparar un camino de alta corriente. [[S21](04_fuentes.md#s21), pp. 17–24 y 59]

- **SET:** transitorio en una señal analógica o digital; puede propagarse o ser capturado.
- **SEU:** alteración de un estado almacenado; reescribir puede recuperar el funcionamiento.
- **SEL:** enganche de una estructura parasitaria que mantiene alta corriente; puede requerir corte de alimentación y llegar a destruir el dispositivo.
- **SEB y SEGR:** fenómenos destructivos de burnout o ruptura de óxido en tecnologías susceptibles, especialmente de potencia. No se atribuyen automáticamente a los dispositivos de Voyager.

La energía incidente no es la energía depositada en el nodo: una partícula puede atravesar gran parte del dispositivo. Además, solo una fracción de la carga generada llega al nodo sensible. Una comparación útil es **Qc recogida frente a Qcrit requerida para perturbarlo**, no «energía del rayo frente a tensión del transistor».

### 2.4 Carga electrostática y descargas

Si la llegada de carga supera su evacuación, una superficie, dieléctrico o metal flotante puede acumular potencial. Electrones penetrantes pueden cargar aislantes incluso dentro del recinto conductor. Una descarga posterior inyecta corriente, genera interferencia o daña un camino cercano. [[S25](04_fuentes.md#s25), §§4.1.2–4.1.5, pp. 30–32]

Para un nodo conceptual con capacitancia C y resistencia de descarga R:

```text
C dV/dt = Icarga − V/R
V∞ = Icarga R
τ = RC
Ealmacenada = ½ C V²
```

Esto vincula radiación y plasma con resistencias, dieléctricos, pistas, conectores y carcasas. Una jaula de Faraday útil contra campos electromagnéticos no detiene necesariamente partículas penetrantes. La mitigación requiere estudiar caminos de carga, masas y aislamiento, además de blindaje.

## 3 Componentes de un circuito

![Mapa del circuito y sus componentes](figuras/01_mapa_componentes.png)

**Figura 1.** Mapa conceptual propio. Las flechas representan funciones; no es un esquema eléctrico ni un plano de Voyager. Cada familia se analiza por material, parámetro eléctrico y consecuencia. Las mitigaciones de vuelo verificadas se distinguen de criterios generales.

### 3.1 Resistencias y redes resistivas

**Estructura y efecto.** Una resistencia combina un elemento resistivo, terminaciones y materiales de soporte o encapsulado. La corriente no depende de almacenar un bit ni de una barrera de óxido de compuerta. Interesan la estabilidad de R, el coeficiente térmico, el ruido y el aislamiento respecto a nodos vecinos. Una fuga por el soporte puede importar más que una pequeña variación del elemento resistivo, especialmente en entradas de megaohmios. [[S27](04_fuentes.md#s27), p. 156]

**Consecuencia en circuito.** En un divisor, Vout = Vin·R2/(R1+R2): interesa la deriva relativa de ambas resistencias, no solo la tolerancia aislada. En una entrada de 20 MΩ, una fuga adicional de 10 nA produce un desplazamiento de 0,2 V; este último es un ejemplo ilustrativo, no una medida de Voyager. Una resistencia de polarización también puede evacuar carga ambiental.

**Evidencia y mitigación.** El programa Voyager ensayó resistencias Dale de película metálica sin detectar cambio de R dentro de ±0,01 % a la fluencia informada. Esto no demuestra inmunidad de toda resistencia. El PWS documenta una resistencia de entrada a masa que limita potencial de antena: caso concreto desarrollado en §5.3. [[S01](04_fuentes.md#s01), §VII.H; [S08](04_fuentes.md#s08), §5.G]

**Criterio general.** Seleccionar tecnología y lote, verificar aislamiento, usar márgenes de tensión/potencia y analizar cómo variaciones correlacionadas o independientes afectan el circuito. No se ha identificado una resistencia de protección contra radiación en cada red de Voyager.

### 3.2 Capacitores y sus dieléctricos

**Estructura y efecto.** Dos electrodos separados por un dieléctrico forman una capacitancia; el modelo real incluye ESR, inductancia serie y una resistencia de fuga en paralelo. La ionización puede aumentar la conductividad del aislante mientras se irradia, y la carga atrapada o cambios del material pueden modificar propiedades después. El efecto depende de química, geometría, dosis y tasa. [[S24](04_fuentes.md#s24), p. 49]

**Consecuencia en circuito.** Un capacitor puede conservar aproximadamente C y, aun así, perder capacidad de retener tensión si baja su resistencia de aislamiento. Eso afecta temporizadores, sample-and-hold, acoplamientos y filtros. En desacoplamiento importan también impedancia y corriente de fuga. No toda deriva de ESR o pérdida de electrolito es radiación: envejecimiento, temperatura y sellado constituyen mecanismos propios.

**Evidencia Voyager.** Se ensayaron seis unidades de cada valor de capacitores B11B de teflón de 0,02 y 0,05 µF. Las reducciones medias informadas fueron 5 y 12 pF después de 5 × 10¹² electrones/cm²: **0,025 % y 0,024 %**, respectivamente. Es un resultado de capacitancia, no una medida de todos sus parámetros ni una lista completa de capacitores instalados. [[S01](04_fuentes.md#s01), p. 7-53, PDF 151; cálculo propio]

**Mitigación.** La evaluación de material y componente forma parte de la calificación. En el acoplamiento PWS–PRA hay además tensiones nominales explícitas, vinculadas con el potencial de entrada previsto. Los bancos capacitivos de potencia de Voyager tienen otra función: cubrir transitorios de carga eléctrica. No se debe confundir reserva de energía con protección universal frente a partículas. [[S08](04_fuentes.md#s08), §5.G; [S03](04_fuentes.md#s03), p. 17]

### 3.3 Inductores y transformadores

**Estructura y efecto.** Incluyen conductor bobinado, aislamiento entre espiras, soporte y, frecuentemente, un núcleo magnético. Un inductor no tiene un umbral MOS; las preguntas pertinentes son estabilidad de permeabilidad y pérdidas del núcleo, resistencia del bobinado, aislamiento y soportes. El manual NASA centra el efecto radiativo de esta categoría en algunos aislantes y no atribuye degradación de propiedades magnéticas en su descripción. Por tanto, no corresponde presentar «desmagnetización por rayos cósmicos» como una falla comprobada de Voyager. [[S26](04_fuentes.md#s26), §10.2.6.5, p. 10-22, PDF 72]

**Consecuencia en circuito.** Una alteración de L cambia rizado y frecuencia de un filtro. Una fuga o corto entre espiras altera pérdidas, calentamiento y capacidad de transformar tensión. Un cambio de corriente impuesto por un transistor dañado puede saturar un núcleo sano: hay que distinguir daño directo del componente de la propagación de una falla ajena. Para un modelo lineal, L ≈ μN²A/l y f0 = 1/(2π√LC) muestran qué parámetros intervienen; cerca de saturación ese modelo deja de bastar.

**Mitigación general.** Calificar materiales, aislamiento y bobinado; respetar márgenes térmicos, eléctricos y de flujo magnético. El blindaje se decide con el ambiente local. **No resuelto para Voyager:** composición y tolerancia radiativa de cada núcleo, barniz y transformador. Está documentada la conversión de potencia a 2,4 kHz, pero eso no permite inventar el material de sus magnéticos. [[S03](04_fuentes.md#s03), pp. 16–17]

### 3.4 Diodos y rectificadores

**Estructura y efecto.** Una unión p-n depende de perfiles de dopado, región de agotamiento y tiempos de vida; un Schottky emplea una barrera metal-semiconductor. No todos responden igual. Defectos de red pueden aumentar fugas y modificar conducción o recuperación; efectos de superficie pueden alterar corrientes periféricas. [[S23](04_fuentes.md#s23); [S27](04_fuentes.md#s27), p. 157]

**Consecuencia en circuito.** Más fuga modifica un detector o rectificador de señal; un cambio de tensión directa altera una referencia; variaciones de recuperación pueden incrementar pérdidas de conmutación. En un Zener importa además la estabilidad de tensión y su coeficiente térmico. Que un diodo sirva como protección de transitorios no significa que detenga partículas incidentes.

**Evidencia Voyager.** La caracterización de 1N4148, 1N5711 y otros rectificadores del programa encontró típicamente cambios de fuga menores que 1 nA y cambios de tensión directa de pocos mV bajo el ensayo descrito. Son resultados de esos dispositivos y condiciones, no un umbral universal de daño. [[S01](04_fuentes.md#s01), §VII.G.3, p. 7-53]

**Mitigación general.** Selección y ensayo de lote, margen de tensión inversa y corriente, y verificación funcional del circuito con parámetros degradados. El dossier no asigna esos números de parte a posiciones concretas de vuelo sin una lista de materiales correspondiente.

### 3.5 Transistores bipolares

**Estructura y efecto.** El emisor inyecta portadores que deben atravesar la base y llegar al colector. Una mayor recombinación, causada por defectos de volumen o superficie, reduce la fracción recogida. La consecuencia habitual es pérdida de ganancia de corriente β y aumento de corrientes parásitas. La ionización de pasivaciones también importa; no todo cambio de β es exclusivamente desplazamiento. [[S23](04_fuentes.md#s23); [S27](04_fuentes.md#s27), p. 157]

**Consecuencia en circuito.** Si una etapa exige 10 mA y el diseño presupone β = 100, estima 0,1 mA de base. Con β = 20 necesita 0,5 mA. Si el driver no puede entregarlos, la etapa deja de cumplir. Es un cálculo ilustrativo: en saturación debe analizarse β forzado y las curvas reales. Una etapa analógica puede perder ganancia o cambiar offset sin llegar a un corto ni a un circuito abierto.

**Mitigación Voyager documentada.** El programa combinó análisis de peor caso, selección de unidades y lotes, revisión de ganancia inicial, sustitución y blindaje cuando era necesario. La dispersión entre dispositivos y los casos atípicos importaban tanto como la media. [[S01](04_fuentes.md#s01), §III y §VIII.C]

**Límite moderno.** Algunos bipolares presentan mayor sensibilidad a tasas de dosis bajas. Una equivalencia basada solo en dosis total no debe extenderse de manera automática entre ensayos acelerados y años de exposición; temperatura, polarización y proceso también deben controlarse. [[S21](04_fuentes.md#s21), p. 56; [S22](04_fuentes.md#s22), interpretación de pruebas TID]

### 3.6 JFET, MOSFET y dispositivos de control de potencia

**Estructura y efecto.** El JFET controla el canal mediante una unión polarizada; el MOSFET lo hace a través de una compuerta aislada. El JFET evita el óxido de compuerta como mecanismo principal de control, pero conserva uniones y superficies susceptibles. En MOS son relevantes carga atrapada, estados de interfaz y caminos parásitos. En dispositivos de potencia susceptibles pueden aparecer eventos destructivos, dependientes de estructura y polarización. [[S02](04_fuentes.md#s02), tabla A-1; [S21](04_fuentes.md#s21), p. 59; [S22](04_fuentes.md#s22)]

**Consecuencia en circuito.** Cambios de IDSS o corriente de compuerta alteran una entrada de alta impedancia; deriva de VT modifica conducción y disipación; una fuga puede cargar un nodo que debería estar aislado. En una fuente, la falla del transistor de control puede causar subtensión o sobretensión en muchas cargas.

**Mitigación.** Ensayar con la polarización relevante, revisar parámetros del circuito degradado y limitar solicitaciones. El informe Voyager distingue categorías de prueba y caracteriza JFET, conmutadores analógicos y dispositivos de potencia. **No resuelto:** susceptibilidad SEE y medidas específicas de limitación de corriente para cada transistor de potencia de vuelo. No se atribuye tecnología MOSFET moderna a todas sus fuentes. [[S02](04_fuentes.md#s02), apéndice A; [S01](04_fuentes.md#s01), §§V–VIII]

### 3.7 Amplificadores, comparadores, reguladores y lógica

Un IC combina los mecanismos de sus transistores, resistencias, aislantes e interconexiones. En un amplificador interesa offset, corrientes de entrada, ganancia, ruido y rango de salida. En un comparador, una deriva de referencia puede disparar una protección incorrecta. En lógica, importan umbrales, consumo, retardo y margen de ruido. Un circuito puede dejar de ser útil mucho antes de destruirse físicamente. [[S22](04_fuentes.md#s22)–[S23](04_fuentes.md#s23)]

**Caso de fabricación de Voyager.** RCA modificó el recocido del óxido de la familia CMOS CD4000 de 1100 a 950 °C para mejorar su comportamiento radiativo. Son temperaturas de fabricación, no de funcionamiento de la sonda. El programa también trabajó con circuitos lineales y calificó componentes sensibles. El resultado no vuelve inmune al dispositivo ni autoriza usar una curva de un CD4000 actual como si fuera la del lote de 1977. [[S01](04_fuentes.md#s01), §VI]

**Mitigación de circuito.** Aplicar límites degradados al diseño: retardo máximo, fan-out, referencias, fugas y consumo. En una red analógica, ajustar el margen puede ser más útil que cambiar toda la tecnología. En Voyager, esa evaluación estuvo ligada a selección, rediseño y blindaje, no solo a la etiqueta comercial del IC. [[S01](04_fuentes.md#s01), §III]

### 3.8 Memorias, registros y temporización

Una SRAM conserva estados mediante realimentación y alimentación; una perturbación suficiente puede invertirlos. Una memoria magnética plated-wire representa información mediante magnetización, pero sus circuitos de lectura y escritura siguen siendo electrónicos. «Memoria magnética» no equivale a «computadora inmune». [[S04](04_fuentes.md#s04), pp. 182–184; [S05](04_fuentes.md#s05); inferencia de arquitectura]

Voyager combina tecnologías: CCS y AACS emplean plated-wire; el FDS adoptó memoria CMOS volátil. El suministro de retención del FDS fue una decisión explícita para preservar estado ante problemas del camino de alimentación alterna. La redundancia tampoco era uniforme: la conmutación de FDS descrita requería órdenes desde Tierra, mientras que AACS tenía supervisión de heartbeat. [[S03](04_fuentes.md#s03), p. 20; [S04](04_fuentes.md#s04), recuadros 6-1 y 6-2]

**Mitigación general frente a errores.** Detección, reescritura, reinicio, códigos correctores o redundancia pueden ser adecuados según arquitectura; no se atribuye ECC, scrubbing o votación triple a Voyager sin documentación específica. Un checksum detecta ciertas corrupciones, pero no repara automáticamente el dato. Los casos operacionales comprobados se describen en §6.

### 3.9 Detectores, LED y acoplamientos ópticos

El mismo depósito de energía que perturba un transistor puede ser la señal buscada en un detector. Para detectar se desea recoger carga; para lógica puede ser necesario impedir que esa carga altere un estado. Los defectos cambian colección y corriente oscura, y los materiales ópticos pueden perder transmisión. Una degradación del emisor o receptor reduce la transferencia de una cadena óptica. [[S21](04_fuentes.md#s21), p. 16; [S01](04_fuentes.md#s01), §VII.I]

**Evidencia de vuelo.** Después de Júpiter, detectores L1 de los telescopios LET del CRS mostraron daño modelado como reducción de espesor efectivo. La atribución a implantación de oxígeno y azufre se presenta como hipótesis en la documentación. Voyager 1 fue más afectada; el LET B de Voyager 2 perdió capacidad de entregar datos tras otro daño radiativo del encuentro. Se corrigieron modelos de respuesta para recuperar análisis de otros detectores. Eso recupera utilidad científica; no vuelve físicamente nuevo el sensor. [[S09](04_fuentes.md#s09), apartado de daño en Júpiter]

### 3.10 Pistas, soldaduras y conectores

Una pista metálica no almacena un estado lógico por sí sola. En el circuito completo interesa cómo una descarga o transitorio se acopla a ella y cómo el aislamiento cercano conduce o retiene carga. Un metal flotante puede cargarse aunque sea buen conductor: la conductividad interna no garantiza conexión a una referencia. [[S25](04_fuentes.md#s25), p. 32]

Para una soldadura o contacto, atribuir una apertura a radiación requiere evidencia adicional. Fatiga térmica, vibración, defectos de fabricación y envejecimiento son causas distintas. La evidencia consultada no cuantifica daño radiativo directo de las soldaduras de Voyager ni identifica sus aleaciones o acabado de cada conector. **No resuelto para el hardware de vuelo.**

**Mitigación general.** Controlar continuidad y retorno, evitar conductores involuntariamente flotantes, calificar aislamiento, minimizar acoplamientos y verificar susceptibilidad a descargas. No basta dibujar un blindaje alrededor del IC: el cable puede conducir el transitorio desde otro lugar. La exigencia equipotencial aparece específicamente en el diseño Voyager descrito para PWS. [[S08](04_fuentes.md#s08), §5.G]

### 3.11 Placas, encapsulados, recubrimientos y aislantes

La placa aporta aislamiento y soporte, pero también capacitancias y caminos de fuga. La carga que queda en un dieléctrico puede elevar el campo local; si se supera la resistencia a ruptura aparece una descarga. La radiación también puede aumentar conductividad durante la exposición. Estos efectos pueden competir: más conductividad ayuda a evacuar carga, pero perjudica una función que necesita aislamiento. [[S25](04_fuentes.md#s25), §§4.1.3–4.1.5]

Los materiales y su temperatura importan: no se debe asignar automáticamente FR4, Kapton o una resina particular a todas las placas de Voyager. El artículo del PWS sí identifica montaje con módulos cordwood e híbridos sobre una placa de 0,062 pulgadas y una carcasa de magnesio con acabado dorado. Es un dato de ese instrumento. [[S08](04_fuentes.md#s08), §5.C]

**Mitigación general.** Materiales caracterizados, caminos de evacuación compatibles con la función, geometría y aislamiento adecuados, control de superficies flotantes y pruebas de descarga. El expediente de cada componente decide si blindar, cambiar material o rediseñar el circuito.

### 3.12 Relés y elementos electromecánicos

En un relé se deben considerar bobina, aislamiento, carcasa, contactos y mecanismo. La radiación sobre aislantes y la carga de partes flotantes son relevantes; no hay motivo para asignarle un SEU como si fuera una SRAM. Una orden errónea desde electrónica sí puede cambiar el estado del relé y afectar la alimentación. [[S25](04_fuentes.md#s25), p. 32; [S27](04_fuentes.md#s27), p. 156]

Voyager utilizó relés comandados para distribuir potencia y transferirla entre módulos. **Documentado.** No se han identificado aquí ensayos radiativos ni materiales de cada modelo de relé de vuelo. **No resuelto.** Calificación, margen de bobina/contacto y control de aislamiento son mitigaciones generales; desgaste mecánico y contacto también deben analizarse como envejecimiento. [[S03](04_fuentes.md#s03), p. 16]

### 3.13 Cristales y osciladores

Un resonador de cuarzo convierte energía eléctrica y mecánica por piezoelectricidad. La radiación puede cambiar frecuencia y resistencia equivalente; la respuesta depende del cristal, sus impurezas, preparación y exposición. La circuitería que sostiene la oscilación tiene, además, sus propias sensibilidades. [[S26](04_fuentes.md#s26), §8.6.8, pp. 8-23–8-24]

En Voyager se seleccionaron muestras de barras de cristal para irradiarlas; se fabricaron unidades de vuelo a partir de barras aceptadas. El informe no encontró degradación importante en esos ensayos. Esa evidencia respalda una selección concreta, no un principio de invariabilidad del cuarzo. [[S01](04_fuentes.md#s01), §VIII.F, p. 8-41, PDF 202]

## 4 El hardware real y los planos disponibles

### 4.1 Arquitectura y tensiones verificadas

| Elemento | Dato documentado | Alcance y fuente |
|---|---|---|
| CCS | Dos procesadores de palabra de 18 bits y memorias plated-wire de 4096 palabras | Arquitectura original; [S05](04_fuentes.md#s05) |
| AACS | Computación de actitud y articulación, memoria plated-wire y procesadores redundantes | [S03](04_fuentes.md#s03), p. 20; [S04](04_fuentes.md#s04), recuadro 6-1 |
| FDS | Procesamiento y formato de datos, memoria CMOS volátil de aproximadamente 8K palabras | [S04](04_fuentes.md#s04), pp. 182–184; [S05](04_fuentes.md#s05) |
| Computadora FDS | Alimentación de 10 V descrita en la historia técnica | No confundir con tensión universal de todos los ICs; [S04](04_fuentes.md#s04), recuadro 6-2, p. 184 |
| Potencia del bus | Regulación original a 30 V DC y conversión a onda cuadrada de 2,4 kHz | [S03](04_fuentes.md#s03), pp. 16–17 |
| Retención de memoria | Alimentación adicional desde el bus DC para memoria y registros | [S04](04_fuentes.md#s04), p. 183; no significa aplicar 30 V directamente al chip |
| Reserva transitoria | Bancos de capacitores para sobrecargas breves | [S03](04_fuentes.md#s03), p. 17 |
| PWS | Híbridos y módulos cordwood; placa de 0,062 pulgadas, equivalente a 1,5748 mm | [S08](04_fuentes.md#s08), §5.C; espesor de placa, no geometría del transistor |

La FAQ informa **8198 palabras** por memoria FDS, mientras la historia técnica habla de **8K**. Se conserva esa discrepancia: no se cambia silenciosamente 8198 por 8192. Para el argumento físico basta «aproximadamente 8K palabras de 16 bits». La misma FAQ contiene una relación entre 80 µs e instrucciones/s aritméticamente inconsistente; no se usa para comparar rendimientos. Los subsistemas tienen tiempos distintos. [[S05](04_fuentes.md#s05), preguntas sobre computadoras y velocidad; [S04](04_fuentes.md#s04), pp. 183–184]

### 4.2 Qué puede afirmarse de materiales y fabricación

Hay evidencia de semiconductores de silicio con estructuras de óxido y pasivación, de CMOS RCA CD4000, dispositivos bipolares, JFET y circuitos lineales evaluados en el programa. En los ejemplos pasivos aparecen película metálica y teflón. El estudio de fabricación del óxido es una evidencia más fuerte que inferir robustez a partir del año de lanzamiento. [[S01](04_fuentes.md#s01), §§VI–VIII]

**No resuelto:** longitudes de canal, espesor de óxido, perfiles de dopado, metalización y encapsulado de cada lote de vuelo, distribución exacta de blindaje y lista completa de materiales de ambas sondas. No se asigna un «nodo de fabricación de Voyager»: una nave con dispositivos discretos, híbridos y diferentes familias no tiene una única geometría de semiconductor.

**Inferencia acotada frente a tecnologías modernas.** Mayor capacitancia de nodo o mayor margen de tensión pueden aumentar la carga necesaria para alterar un estado. Eso no prueba una ventaja global de la electrónica antigua: óxidos más gruesos pueden acumular más carga, y las tecnologías modernas incluyen cambios de estructura y endurecimiento. NASA NEPP advierte expresamente que las tendencias de escalado no son reglas universales. [[S24](04_fuentes.md#s24), pp. 47–50]

### 4.3 Qué tipo de planos hay en las fuentes

- **Diagramas de instrumento:** el artículo original del PWS presenta su cadena funcional y detalles de entrada. [S08](04_fuentes.md#s08), figuras 4–7 y §5.
- **Circuitos de ensayo:** [S01](04_fuentes.md#s01), figura 7-6, p. 7-54, muestra una prueba de fuente y detector ópticos con alimentación, resistencias y punto de medida. Es un montaje de ensayo, no una placa de vuelo.
- **Curvas de dispositivo:** [S01](04_fuentes.md#s01), figura 6-1, p. 6-3, compara características MOS antes y después de irradiación.
- **Arquitectura y hardware:** [S03](04_fuentes.md#s03) describe potencia y comunicaciones; [S04](04_fuentes.md#s04), figura 6-2 y recuadro 6-2, muestra y describe el FDS.
- **Procedimientos:** [S02](04_fuentes.md#s02) especifica polarización, dosis, criterios y organización de pruebas.

Se lanzaron **dos Voyager**, pero documentación de un prototipo, modelo de prueba o repuesto no identifica una tercera misión de vuelo. No se encontró un juego completo, revisado y trazable de esquemas eléctricos y listas de materiales de las dos unidades. Los planos parciales encontrados están identificados por su función para evitar presentar un circuito de prueba como circuito de la nave.

## 5 Mitigaciones y ejemplos cuantitativos

### 5.1 Calificar el componente dentro del circuito

La capacidad de un componente se define por el límite que necesita su aplicación: un transistor todavía puede conducir y haber perdido demasiada ganancia para ese diseño. Voyager combinó tolerancias iniciales, temperatura, envejecimiento, alimentación y degradación radiativa en análisis de peor caso. La respuesta incluía sustitución, rediseño, procesos especiales, selección y blindaje. [[S01](04_fuentes.md#s01), §III]

El volumen de procedimientos exige trazabilidad de lote, mediciones eléctricas previas y posteriores y polarización representativa del peor caso. Distingue pruebas de ionización, desplazamiento, combinación y ruido inducido. Esto explica por qué «lo irradiaron y siguió encendiendo» resulta un criterio insuficiente. [[S02](04_fuentes.md#s02), apéndice A, pp. A-1–A-6]

La selección irradiar–recocer, descrita para ciertas familias, pertenece al proceso de aceptación en Tierra. No prueba que todos los componentes de vuelo recibieran el mismo tratamiento ni que la sonda ejecute un ciclo de reparación radiativa en operación. [[S01](04_fuentes.md#s01), §IV.B; [S02](04_fuentes.md#s02), apéndice E]

### 5.2 Blindaje y margen de radiación

Para dosis, el margen de diseño se expresa como:

```text
RDM = capacidad admitida en la aplicación / exposición local prevista
RDM = 60 krad(Si) / 30 krad(Si) = 2
```

El cociente es adimensional. Hay que mantener el mismo material, mecanismo y criterio funcional en numerador y denominador. La referencia general no sustituye el análisis de dispositivos con tolerancias menores. [[S01](04_fuentes.md#s01), pp. 2-3 y 3-5–3-6]

El blindaje reduce parte del espectro y también puede generar secundarios. En electrones interesa el bremsstrahlung; en partículas de alta energía, otros procesos de transporte. La masa, su posición y las trayectorias importan: duplicar el espesor no implica dividir por dos la dosis. El programa calculó ambientes locales y aplicó blindaje específico cuando otras medidas no bastaban. **No se ha establecido aquí un único espesor o material de blindaje válido para toda Voyager.** [[S01](04_fuentes.md#s01), §III.C]

### 5.3 Una resistencia y dos capacitores frente al ambiente

**Caso documentado PWS.** Su diseño de entrada considera una corriente máxima de carga de antena de **4 µA**. Una resistencia de **20 MΩ** a masa limita el potencial DC previsto a:

```text
V = I R = 4 × 10⁻⁶ A × 20 × 10⁶ Ω = 80 V
P = I² R = 0,00032 W = 0,32 mW
```

La fuente especifica la resistencia para 500 V y los capacitores de acoplamiento PWS–PRA para 500 V a 1 kV. La relación nominal 500/80 = 6,25 ilustra el margen de tensión en ese escenario. No es el RDM de dosis ni certifica tolerancia a cualquier descarga. El análisis presupone ausencia de arcos y una nave equipotencial. [[S08](04_fuentes.md#s08), §5.G; potencia y cociente calculados aquí]

La cadena explicativa es completa: **entorno de partículas → corriente de carga → potencial de antena → resistencia de descarga → tensión soportada por aislantes y entrada**. La radiación puede poner en riesgo una entrada a través de carga acumulada sin haber destruido previamente el material resistivo.

### 5.4 Un capacitor que pierde aislamiento

**Ejemplo ilustrativo, ajeno a valores de vuelo.** Supóngase C = 10 nF, tensión inicial 5 V y resistencia de fuga que pasa de 10 GΩ a 1 GΩ:

```text
τinicial = 100 s; τfinal = 10 s
Ifuga inicial = 0,5 nA; Ifuga final = 5 nA
V(1 s), antes = 5 exp(−1/100) = 4,950 V
V(1 s), después = 5 exp(−1/10) = 4,524 V
```

En este modelo de retención aislada, C no cambia y el error crece mucho. En un circuito conectado hay que incluir resistencias externas y la impedancia de la fuente. La utilidad del ejemplo es mostrar que medir solo capacitancia no verifica la función completa. El mecanismo de conductividad inducida está descrito en [S24](04_fuentes.md#s24), p. 49.

### 5.5 De LET a carga en silicio

**Ejemplo ilustrativo.** Se toma LET másico = 10 MeV·cm²/mg, densidad de silicio ≈ 2330 mg/cm³ y longitud atravesada de 1 µm = 10⁻⁴ cm. Se supone LET constante en ese tramo y que la energía calculada es ionizante:

```text
Edepositada ≈ LET × ρ × l = 2,33 MeV
Npares ≈ 2,33 × 10⁶ eV / 3,6 eV = 647.222 pares
Qgenerada ≈ Npares × e = 1,037 × 10⁻¹³ C = 103,7 fC
```

El valor aproximado 3,6 eV por par en silicio y la ponderación por colección se describen en CREME-MC. [[S28](04_fuentes.md#s28)]

Si solo se recoge el 10 %, el nodo recibe aproximadamente 10,4 fC. Un modelo estático Cnodo·ΔV, con **Cnodo supuesto de 10 fF** y **ΔV supuesto de 1 V**, da 10 fC. La proximidad de esos valores muestra plausibilidad física; no predice un error en una memoria Voyager. Qcrit real depende también de realimentación, corriente restauradora, duración y lugar de inyección. Geometría, LET y carga de este ejemplo no son parámetros medidos de sus chips.

### 5.6 Conversión de dosis y verificación de un ensayo

30 krad(Si) = 300 Gy(Si) = 300 J/kg. Que esa energía por masa parezca modesta frente a un proceso térmico no elimina el daño por cargas atrapadas: importa dónde se deposita y qué estados altera.

La tabla A-2 del volumen II contiene exposiciones de 1000 s con tasas de dosis de 30, 30 y 60 rad(Si)/s; las dosis acumuladas son 30, 60 y 120 krad(Si). La última fluencia electrónica aparece impresa como **4,8 × 10¹³**, pero integrar los tres flujos de su tabla da **4,8 × 10¹² cm⁻²**. La tabla A-3 y el texto de A-6 coinciden con este último valor. Se registra como inconsistencia de la fuente, no como corrección invisible del PDF. [[S02](04_fuentes.md#s02), pp. A-5–A-6, PDF 13–14]

## 6 Fallas reales y continuidad de la misión

| Caso | Qué está establecido | Qué no está establecido | Respuesta |
|---|---|---|---|
| Detectores CRS tras Júpiter, 1979 | Daño radiativo y modificación de respuesta | Implantación O/S es una explicación propuesta, no verificación de cada defecto | Recalibración y modificación del análisis; ciertas pérdidas persistieron. [S09](04_fuentes.md#s09) |
| Memoria Voyager 2, 2010 | Un bit pasó de 0 a 1; la modificación se reprodujo en Tierra y se corrigió | La fuente no identifica una partícula causante | Orden de restauración y comprobación de memoria/checksum. [S10](04_fuentes.md#s10) |
| FDS Voyager 1, 2023–2024 | Memoria inutilizable impedía datos legibles; se sospechó y luego aisló un chip averiado | NASA no pudo decidir entre partícula energética y desgaste como causa física | Reubicación de código; telemetría de ingeniería recuperada en abril de 2024. [S11](04_fuentes.md#s11)–[S12](04_fuentes.md#s12) |
| Cambios térmicos CRS | Apagar calentadores modificó respuesta instrumental | El cambio de cuentas no prueba cambio radiativo externo | Nuevas correcciones de flujo y calibración. [S09](04_fuentes.md#s09), [S18](04_fuentes.md#s18) |
| Apagados científicos 2025–2026 | Retiro de cargas para sostener operación con menos potencia | No son prueba de destrucción de esos instrumentos por radiación | Gestión de energía y nuevas configuraciones. [S07](04_fuentes.md#s07), [S14](04_fuentes.md#s14)–[S16](04_fuentes.md#s16) |

El caso de memoria permite separar tres niveles de causalidad: **dato incorrecto**, **componente incapaz de almacenar correctamente** y **causa física del deterioro**. Identificar el segundo no prueba automáticamente el tercero.

**Estado al corte de consulta.** Voyager 1 tiene MAG y PWS activos. Voyager 2 mantiene MAG, PWS y CRS. El comunicado de agosto de 2026 informa una reconfiguración de potencia de Voyager 2 para prolongar esos tres instrumentos; la actuación equivalente sobre Voyager 1 estaba prevista y no se afirma aquí que ya estuviera completada. [[S07](04_fuentes.md#s07), [S15](04_fuentes.md#s15)]

La alimentación procede de RTG. La potencia eléctrica disponible cae con el tiempo y debe distinguirse del daño radiativo de las cargas. Los ajustes actuales de consumo y calefacción tienen consecuencias eléctricas y térmicas: un instrumento que permanece encendido a menor temperatura puede necesitar otra calibración. La estrategia de 2023 también implicó aceptar una regulación menos estricta para recuperar potencia útil. [[S13](04_fuentes.md#s13); [S09](04_fuentes.md#s09)]

### Qué se esperaría en un circuito sin esas medidas

No existe un «caso normal» único. Un diseño no calificado podría superar su límite de fuga, ganancia, tiempo de propagación o aislamiento antes de que la mayoría de sus piezas se destruyan. Una sola referencia que derive puede degradar todo un convertidor; un transistor con poca ganancia puede impedir una conmutación; una descarga en un aislante puede alcanzar una entrada remota.

**Inferencia.** Evaluar cada función con parámetros degradados permite anticipar esos modos de falla. La selección y el blindaje reducen exposición o susceptibilidad; la redundancia y recuperación reducen consecuencias. Ninguna de estas medidas elimina todas las fallas ni constituye, por sí sola, una demostración de vida útil de 50 años.

## 7 Respuesta a la pregunta central

Voyager sigue produciendo ciencia porque una parte suficiente de su sistema conserva capacidad funcional y porque la misión adapta su operación a las pérdidas y restricciones. La resistencia material y eléctrica fue construida mediante ensayos, selección y márgenes; la continuidad de la misión también depende de arquitectura, comunicación y decisiones desde Tierra.

**Documentado:** existen decisiones concretas de endurecimiento y blindaje, ensayos de pasivos y semiconductores, daño de detectores y recuperación operacional. **Inferido:** esa combinación explica mejor la longevidad que una única propiedad como tamaño de transistor o tensión elevada. **No resuelto:** no hay aquí una contabilidad causal que cuantifique cuánto aportó cada medida a los 49 años, ni la dosis de cada pieza al corte de 2026.

El eje para exponer es: **la radiación modifica materiales; los cambios de parámetros afectan circuitos; el diseño limita esos cambios y sus consecuencias; el sistema sigue siendo útil incluso con capacidades reducidas**. Los ejemplos de resistencia de antena, capacitor con fuga, transistor con menor ganancia y detector recalibrado permiten defender esa idea sin concentrar toda la explicación en memorias.
