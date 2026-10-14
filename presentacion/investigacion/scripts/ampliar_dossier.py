"""Integra explicaciones por familia y una guía de lectura en el dossier existente."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'01_dossier.md'
s=p.read_text()
if '## Guía de lectura y resultados posibles' in s:
    raise SystemExit('La ampliación ya está integrada; no se duplica.')
s=s.replace('# Radiación y supervivencia de los componentes electrónicos de Voyager','# Efectos de la radiación sobre los componentes y circuitos de Voyager',1)
intro='''
## Guía de lectura y resultados posibles

La radiación puede perturbar un circuito sin romper ninguna pieza. Una corriente fugaz puede parecer una señal válida y dejar una orden ejecutada; una fuga sostenida puede desplazar una lectura; una degradación de ganancia puede agotar el margen del diseño. Por eso estudiamos **comportamiento**, no solamente supervivencia material.

| Resultado | Qué persiste | Ejemplo conceptual |
|---|---|---|
| Perturbación transitoria | El pulso desaparece; puede no quedar daño ni estado alterado | Corriente recogida en una unión que produce una lectura espuria |
| Estado alterado recuperable | Permanece el dato o estado después del pulso | Un registro cambia o un mando activa una carga; hace falta una acción de recuperación |
| Degradación o daño | Cambian parámetros o se pierde una función | Ganancia reducida, fuga elevada, aislamiento perforado |

Estas categorías describen el resultado, no tres tipos exclusivos de radiación. Un solo evento puede ser inocuo, provocar un estado persistente o causar daño. Una degradación acumulada también puede recuperarse parcialmente por procesos de recocido; «acumulada» no significa necesariamente irreversible. El latchup tampoco es simplemente un pulso: puede mantenerse hasta retirar alimentación y producir daño si no se limita. [S21, S22, S35]

**Ruta para leer hoy.** Leer §§1–2 para el ambiente y los mecanismos; recorrer §3 con sus apartados «Cómo explicarlo en clase»; terminar con hardware, mitigaciones y casos reales (§§4–7). Los apartados «Profundización opcional» explican regiones y ecuaciones que no son necesarias para exponer. El guion curado está en [03_sintesis_20min.md](03_sintesis_20min.md).

**Vocabulario mínimo.** Un portador es una carga móvil: electrón o hueco, este último una ausencia de electrón que se comporta como carga positiva. Generar un par no crea carga neta: crea dos portadores de signo opuesto. Un campo puede separarlos y producir corriente. Una trampa es un estado localizado que puede capturar y liberar un portador; un centro de recombinación puede facilitar la eliminación sucesiva de un electrón y un hueco. No toda trampa actúa igual ni toda captura es recombinación. Un estado de interfaz está asociado a la frontera entre materiales. La región de agotamiento de una unión tiene pocos portadores móviles y un campo que favorece la colección de carga. [S21–23, S36]

**Espurio no equivale a ruido continuo.** Aquí llamamos espuria a una señal que el circuito entrega o interpreta sin que corresponda al estímulo buscado. Un pulso aislado es un transitorio; el ruido se describe estadísticamente y también puede producir cruces falsos de umbral. Una sucesión de eventos puede aumentar el fondo de un detector. Para atribuir cualquiera de ellos a radiación hace falta evidencia; una interferencia o fluctuación térmica no se vuelve radiativa por parecerse a un pulso. [S35, §§2–4; interpretación funcional]

'''
s=s.replace('## 1 Ambiente y medición',intro+'## 1 Ambiente y medición',1)

parts={
'3.1':'''#### De la corriente del material al error de medida

La resistencia cumple aproximadamente V = IR en su régimen de trabajo. Cambiar la resistividad del elemento o crear un camino conductor por su soporte son efectos diferentes: el segundo puede desviar corriente entre terminales o hacia otro nodo aunque el elemento resistivo conserve su valor. En un aislante, portadores generados por ionización pueden aumentar la conductividad durante la exposición; carga atrapada puede modificar campos y tiempos de recuperación. No se presume un cambio importante en una película metálica solo porque otro material aislante sea sensible. [S24, p. 49; S25, §4.1; S27, p. 156]

**Efecto de circuito y duración.** En una entrada de alta impedancia, una pequeña corriente inducida produce una tensión espuria. Para una perturbación lenta respecto del tiempo RC, ΔV ≈ Iespuria·R; para un impulso muy breve interesa la carga que llega y la capacitancia del nodo. El transitorio puede desaparecer al cesar la corriente y descargarse el nodo, mientras una deriva permanente de R exige otro análisis. La resistencia no necesita sufrir daño directo para participar en un error: convierte una corriente ajena en tensión.

**Mitigación y límite.** Reducir impedancia puede reducir la tensión causada por una fuga, pero también cargar el sensor y consumir más. Calificar aislamiento y tecnología, y evaluar tolerancias del divisor, son criterios generales. El caso PWS de 20 MΩ documenta una función concreta de evacuación de carga; no demuestra que todas las resistencias fueran protectoras ni que esa red suprima cualquier pulso. [S08, §5.G]

**Cómo explicarlo en clase.** «En una resistencia debemos mirar tanto su valor como el aislamiento que la rodea. Si aparece una corriente no deseada en una entrada de alta resistencia, puede producir una tensión que se confunda con señal. La pieza puede seguir sana; el circuito igual puede medir mal».

''',
'3.2':'''#### El dieléctrico durante y después de irradiar

En un capacitor ideal, los electrodos almacenan cargas opuestas y el dieléctrico impide una corriente DC entre ellos. En el material real, la ionización puede generar portadores que se mueven bajo el campo entre electrodos. Esto eleva la conductividad y reduce la resistencia de aislamiento durante la exposición. Captura, liberación y recombinación determinan cuánto dura la respuesta; no debe suponerse recuperación instantánea. Los cambios residuales dependen de composición, defectos y exposición. La carga atrapada puede modificar el campo interno sin que eso se traduzca en una variación única o universal de C. [S24, p. 49; S25, §§4.1.3–4.1.5]

**Circuito y recuperación.** Representar C en paralelo con Rfuga permite separar almacenamiento y pérdida. Una fuga transitoria puede descargar un capacitor de temporización: aunque el aislamiento se recupere, el temporizador ya pudo dispararse antes de lo debido. Hay que volver a cargarlo o restablecer la función. En un capacitor de desacoplamiento, el efecto depende además de la impedancia de la fuente, ESR e inductancia del montaje. No toda exposición equivale a un corto y no toda alteración del dieléctrico es permanente.

**Profundización opcional.** En geometría plana C ≈ εA/d, mientras que Rfuga ≈ d/(σA) para conducción uniforme. Un aumento de σ no exige un cambio proporcional de ε; por eso C puede permanecer casi igual mientras la retención empeora. En este modelo RC = ε/σ. Materiales heterogéneos, dependencia del campo, absorción dieléctrica y caminos superficiales requieren un modelo más completo. Estas relaciones ilustran el mecanismo, no parametrizan los B11B de vuelo.

**Mitigación y límite.** Seleccionar y medir el dieléctrico bajo condiciones relevantes; comprobar aislamiento además de C y ESR. Un capacitor añadido como filtro puede reducir ciertos pulsos, pero modifica ancho de banda y respuesta, y puede sufrir sus propios efectos. El ensayo B11B demuestra estabilidad de C bajo sus condiciones, no inmunidad funcional completa. [S01, p. 7-53]

**Cómo explicarlo en clase.** «La radiación puede hacer que el aislante conduzca más mientras está expuesto. El capacitor entonces pierde carga más rápido: puede alterar una medida o un tiempo sin quedar destruido y sin cambiar mucho su capacitancia».

''',
'3.3':'''#### Separar el magnético de la perturbación que lo atraviesa

El campo magnético almacena energía y el núcleo modifica la relación entre corriente y flujo. La radiación no implica por sí sola un impulso de corriente en el bobinado. Hay que identificar el material afectado: una corriente inducida en aislamiento o una descarga puede perturbar la red, mientras una orden espuria en el transistor de mando puede aplicar volt-segundos indebidos a un transformador sano. El segundo caso es propagación desde la electrónica, no desmagnetización directa. [S26, §10.2.6.5; S25, §4.1; inferencia de circuito]

Una perturbación breve puede disiparse con la dinámica de la red; una perforación de aislamiento o un sobrecalentamiento pueden dejar daño. La energía ½LI² y la relación v = L·di/dt, dentro del régimen lineal, ayudan a entender que cortar corriente o excitar el bobinado genera tensiones. No permiten calcular un transitorio radiativo sin conocer su fuente y circuito. El control de aislamiento y márgenes se fundamenta aquí en el manual NASA de componentes, no en materiales de magnéticos Voyager identificados.

**Cómo explicarlo en clase.** «En bobinas y transformadores miramos especialmente el aislamiento y lo que les aplica el circuito de mando. Un transistor que entrega un pulso incorrecto puede alterar un transformador que está perfectamente sano. No tenemos evidencia para decir que los rayos cósmicos desmagnetizaron los núcleos de Voyager».

''',
'3.4':'''#### Cómo una unión produce una corriente espuria

Una unión p-n dispone de una región con campo eléctrico. Si la radiación genera pares electrón–hueco dentro de ella o cerca, parte de esos portadores se separa y llega a los terminales. En la zona de campo predomina el transporte por deriva; carga generada cerca puede llegar por difusión antes de recombinarse. Aparece una corriente adicional aunque la tensión aplicada no haya cambiado. El pulso termina al recogerse o recombinarse el exceso de portadores; no requiere crear defectos permanentes. La polarización, geometría y trayectoria determinan cuánto se recoge. [S21–23; S35, §2]

En una entrada de medida esa corriente puede parecer señal. En un diodo de protección o rectificación, la consecuencia depende de impedancias y polarización: no se presupone la misma sensibilidad que en un detector. Tras el pulso el diodo puede recuperar su comportamiento, pero un circuito posterior pudo memorizar una lectura equivocada.

**Profundización opcional.** Los defectos de red pueden introducir niveles dentro de la banda prohibida. Bajo polarización inversa, centros de generación pueden aumentar corriente de fuga; en otras condiciones favorecen recombinación y cambian el transporte. Generación y recombinación dependen de ocupación y concentraciones, no de una «pérdida de electrones» universal. Un Schottky no se explica enteramente con el mismo modelo p-n. La carga transitoria Qrec = ∫iespuria(t)dt se distingue del incremento residual de fuga. [S21, p. 16; S23]

**Caso y mitigación.** El programa ensayó, entre otros, 1N4148 y 1N5711; su evaluación de parámetros posirradiación no caracteriza por sí sola los pulsos durante irradiación. Para estos últimos se requiere conocer la respuesta temporal y la aplicación. Selección y márgenes reducen susceptibilidad; filtrado o validación temporal son opciones generales cuyo uso en Voyager requiere evidencia específica. [S01, p. 7-53; S35]

**Cómo explicarlo en clase.** «La radiación puede generar cargas que el campo de la unión separa. Durante un instante circula una corriente que el circuito no esperaba. Si además quedan defectos, también puede aumentar la fuga después: el pulso y el deterioro son dos efectos diferentes».

''',
'3.5':'''#### Balance de corrientes y dos caminos de degradación

En un NPN en región activa, la unión base–emisor polarizada en directa permite inyectar electrones desde el emisor a la base. La base es suficientemente delgada para que una fracción elevada alcance la región de campo base–colector y sea recogida. Otra fracción se recombina; además existe inyección de huecos hacia el emisor. La corriente del terminal de base sostiene esos procesos. Para magnitudes de corriente estacionarias, IE = IC + IB y β = IC/IB. Esa igualdad conserva carga, pero no explica por sí sola cuánto vale cada corriente.

**Desplazamiento.** Los defectos en el volumen pueden introducir niveles que facilitan la captura sucesiva de un electrón y un hueco. El centro puede volver a participar: no es un recipiente que se llena una sola vez. Una menor vida de minoritarios reduce la probabilidad de atravesar la base sin recombinarse. **Ionización.** Carga y estados de interfaz en óxidos superficiales alteran campos y recombinación, especialmente cerca de la unión emisor–base; pueden aumentar IB aun cuando IC cambie poco a un mismo VBE. No atribuir todo aumento de IB a defectos en el volumen. [S36, figuras 26–27; S01, §VII.B]

**Condición de comparación.** A IC fijada, un β menor implica más IB. A IB fijada, puede disminuir la corriente de colector en región activa. A VBE fijada, observar por separado curvas de IC e IB permite identificar de dónde proviene el cambio de β. En saturación, IC ≈ βIB no basta: la carga y las tensiones disponibles fijan el funcionamiento. Ejemplo ilustrativo: sostener IC = 10 mA con β = 100 requiere IB = 0,1 mA; con β = 50 requiere 0,2 mA en el modelo activo. No son parámetros medidos de Voyager.

**El transistor también entrega espurios.** La carga generada y recogida en sus uniones puede producir corrientes momentáneas y ser amplificada por el circuito. Un amplificador puede saturarse brevemente y tardar en recuperar su punto de trabajo. El exceso de señal puede desaparecer sin degradación de β; si dispara un comparador o se muestrea, la consecuencia puede persistir. [S35, §§2 y 4; explicación de circuito]

**Profundización opcional.** La longitud de difusión Ln = √(Dnτn) relaciona difusión y vida de electrones minoritarios en la base p. Una reducción de τn puede reducir el transporte útil, dependiendo del ancho y perfil de base. No inferir anchos de base Voyager con esta fórmula. La recombinación superficial y en regiones de agotamiento requiere considerar concentración de portadores y estados de interfaz, además de τ del volumen. [S36]

**Gráfico para estudiar.** S01, figura 7-1, representa cambio de 1/hFE frente a IC bajo el ensayo indicado. Un mayor incremento de la ganancia inversa significa más degradación; no es un gráfico del valor absoluto de β. Permite explicar dependencia con corriente y proceso. La figura 7-2 compara condiciones del 2N2907A. Los 2N2222 de distintos fabricantes no se comportaron igual: el nombre comercial no fija la tolerancia. Estos son resultados de ensayo del programa, sin asignación a una placa concreta. [S01, pp. 7-2–7-3]

**Cómo explicarlo en clase.** «Parte de la corriente de control se relaciona con recombinación. La radiación puede crear condiciones que aumenten esa recombinación, y el transistor necesita más corriente de control para sostener la salida. También puede generar un pulso momentáneo sin dañarlo. Diseñar con margen de ganancia y evitar que un pulso se interprete como orden resuelven problemas distintos».

''',
'3.6':'''#### Control electrostático, carga atrapada y carga recogida

En un MOSFET, el potencial de compuerta establece un campo a través del óxido que modifica la población de portadores del canal. El aislante permite ejercer ese control sin una corriente DC ideal entre compuerta y canal. La ionización puede generar pares en el óxido: una parte se recombina; la restante se transporta bajo el campo y puede atraparse. Esa carga también contribuye al campo que ve el semiconductor, modificando el voltaje de compuerta necesario para una misma condición de canal. Los estados de interfaz intercambian carga con el semiconductor y alteran su respuesta; no son idénticos a una carga fija dentro del óxido. [S22–23]

**Profundización opcional.** Con convención de tensión de compuerta, el término de carga positiva efectiva en óxido produce ΔVT ≈ −Qot/Cox. En un NMOS puede reducir el umbral positivo; en un PMOS puede volver más negativo el umbral. El signo y ocupación de estados de interfaz y otros efectos cambian el resultado neto; no afirmar que NMOS y PMOS siempre se vuelven más fáciles de encender. La dispersión de portadores por defectos puede afectar movilidad, y los estados de interfaz empeorar la transición subumbral. Tiempo, polarización y temperatura condicionan recuperación y compensación de efectos. [S22, TID e Interface Traps]

**Transitorio distinto.** Una partícula también puede generar carga en el silicio, que se recoge en una unión de drenador y perturba un nodo. No hace falta esperar a que cambie el umbral. El tamaño y duración del pulso dependen de colección, capacitancia y corriente restauradora. En un JFET, la compuerta controla mediante una unión: explicar corrientes de unión y cambios de canal, sin atribuirle el óxido de compuerta de un MOS. [S21–23]

**Potencia: límite de evidencia.** El informe muestra montajes para ensayar transistores de potencia (figuras 5-15 y 5-16), pero eso no identifica aquí cada modelo instalado ni su función. No se ha demostrado presencia de MOSFET de potencia en las unidades de vuelo con esta documentación. SEB/SEGR se mantienen como mecanismos generales de dispositivos susceptibles, fuera de la explicación principal de Voyager. Un fallo del mando puede perturbar la alimentación sin daño directo del elemento de potencia. [S01, §V; S21]

**Cómo explicarlo en clase.** «La compuerta controla el transistor con un campo eléctrico. Si queda carga atrapada en el aislante, ese campo cambia y también cambia la tensión necesaria para encenderlo. Por otro camino, la carga recogida en una unión puede producir un pulso breve aunque el transistor no haya quedado deteriorado».

''',
'3.7':'''#### De un nodo interno a una salida falsa

Un amplificador tiene nodos con pequeñas capacitancias y corrientes que fijan su punto de trabajo. Una corriente inducida en una unión puede cargar uno de esos nodos; las etapas siguientes amplifican o transforman la perturbación. La salida puede producir un SET, es decir, un transitorio de evento único. Su forma depende del dispositivo, ganancia configurada, alimentación, entrada y carga; un ensayo con una sola configuración no cubre todas las aplicaciones. Comparadores, referencias y reguladores pueden transmitir consecuencias diferentes a partir de una perturbación interna. [S35, §§2.4 y 4]

En un comparador, un pulso puede cruzar el umbral y generar un cambio lógico. En un ADC, una perturbación capturada durante la conversión puede dejar una muestra errónea aunque la señal analógica se recupere. En lógica combinacional el pulso puede atenuarse o propagarse; solo ciertas amplitudes, duraciones y coincidencias temporales alteran el estado posterior. No todo SET produce SEU. [S22, Single-Event Transients; S35]

**Mitigación general.** Elegir componentes caracterizados en condiciones pertinentes; filtrar cuando la señal útil lo permita, validar duración, introducir histéresis o contrastar medidas. Cada opción tiene límites: un pulso grande puede superar histéresis; una señal falsa suficientemente larga supera un filtro; filtros pueden retrasar protecciones legítimas. No se atribuyen estas técnicas a una placa Voyager concreta por recomendarlas aquí.

**Cómo explicarlo en clase.** «El circuito puede amplificar una carga que no venía del sensor. Sale entonces un pulso falso. Aunque desaparezca, otro bloque puede haberlo tomado como una medida o una orden. Debemos estudiar el circuito receptor, no solo comprobar si el integrado sobrevivió».

''',
'3.8':'''#### El pulso termina, el estado puede permanecer

En una memoria estática, la realimentación mantiene uno de dos estados. Si una perturbación desplaza suficientemente un nodo y la dinámica cruza hacia el otro estado estable, la celda termina conservando el dato equivocado. La carga transitoria ya desapareció, pero la realimentación sostiene el nuevo estado. Reescribir puede corregirlo si no hay daño. Una señal espuria capturada por un registro también puede cambiar estado sin impacto directo en la celda. [S22, SEU y SET]

La consecuencia depende del dato: una muestra incorrecta puede descartarse; un parámetro o una instrucción alterada puede afectar muchas operaciones. Reiniciar no garantiza recuperar datos originales y requiere un estado seguro conocido. La alimentación de retención evita cierta pérdida por interrupción de suministro, pero no bloquea por sí misma la colección de carga radiativa. [S04, p. 183; distinción funcional]

**Cómo explicarlo en clase.** «La memoria conserva estados. Un pulso breve puede hacerla conservar el estado equivocado después de que el pulso terminó. Eso puede recuperarse escribiendo de nuevo, pero no significa que cualquier error se arregle solo o reiniciando».

''',
'3.9':'''#### Cuándo la carga es señal y cuándo es espuria

Un detector de silicio aprovecha generación y colección de portadores para medir partículas. Una trayectoria que deposita energía produce un pulso útil si corresponde al canal y a la medición buscada. En un sensor óptico, una partícula ionizante puede generar carga sin el fotón que se quería medir: aparece un evento espurio. La misma interacción tiene distinto significado según la función. Su amplitud depende de energía depositada y colección, no simplemente de la energía incidente. [S21; S30; explicación funcional]

Con defectos acumulados puede aumentar corriente oscura y disminuir colección. En emisores, recombinación no radiativa puede reducir la luz emitida; en una cadena óptica importa la transferencia completa, no solo si el LED enciende. El montaje S01, figura 7-6, permite distinguir fuente y receptor en el ensayo. La recuperación de un pulso es distinta de recalibrar una respuesta degradada: recalibrar no elimina defectos. [S01, §VII.I; S09]

**Cómo explicarlo en clase.** «Un detector usa la carga producida por radiación como señal. En otro sensor, esa carga puede ser una lectura falsa. A lo largo del tiempo también puede cambiar la eficiencia del detector; corregir su calibración recupera utilidad, pero no lo vuelve nuevo».

''',
'3.10':'''#### La pista conduce la perturbación, aunque no sea su origen

La carga depositada o acumulada en otro material puede descargarse hacia un conductor. Corrientes rápidas generan diferencias de potencial en impedancias compartidas y pueden acoplarse capacitivamente o magnéticamente a otras líneas. Así una descarga puede llegar a una entrada remota por cable, pista o referencia común. La pista no tiene que cambiar su resistividad ni sufrir un defecto permanente para transportar un espurio. [S25, §4; explicación de interconexión]

La carga acumulada se disipa y el pulso puede terminar, pero una entrada puede quedar dañada o un receptor interpretar una orden. Separar esa consecuencia de la fatiga de una soldadura. Continuidad de retornos, equipotencialidad y control del acoplamiento son criterios generales; el PWS documenta su requisito equipotencial, sin identificar aquí todo el cableado de vuelo. [S08, §5.G]

**Cómo explicarlo en clase.** «El problema puede empezar en un aislante y viajar por una pista hasta otro circuito. El cobre puede estar sano y, sin embargo, transportar una señal falsa o una descarga. Importa el recorrido completo de la corriente».

''',
'3.11':'''#### Acumulación, conducción y descarga no son lo mismo

En un aislante penetrado por electrones, la carga que queda retenida puede crear campo interno. Si llega más carga de la que sale, ese campo aumenta; una trayectoria de descarga puede aparecer cuando las condiciones locales superan la capacidad del aislamiento. La tensión y energía disponibles dependen de geometría y caminos de fuga. Al mismo tiempo, radiación puede elevar conductividad y facilitar evacuación: el balance debe evaluarse, no decidirse por el nombre «aislante». [S25, §§4.1.3–4.1.5]

Un aumento temporal de conducción puede afectar una entrada de alta impedancia sin producir descarga. Una descarga puede ser un evento aislado de interferencia o dejar daño. El espesor de placa PWS documentado no identifica su resina ni permite calcular una tensión de ruptura. Los mecanismos generales se apoyan en NASA-HDBK-4002B, posterior a Voyager y no prueba de que cada recomendación se aplicó en 1977.

**Cómo explicarlo en clase.** «La placa también contiene aislantes. Pueden acumular carga o conducir más durante la exposición. Eso puede causar fugas y, si el campo crece lo suficiente, una descarga. No hace falta que falle un chip para alterar una señal».

''',
'3.12':'''#### Una orden espuria puede cambiar una carga real

La electrónica de mando energiza la bobina y el mecanismo mueve contactos. Un pulso muy breve no necesariamente lo acciona: importan corriente, duración, dinámica mecánica y circuito de excitación. Si la perturbación altera antes un registro de mando, la orden puede durar lo suficiente para cambiar el relé. Ese es un efecto indirecto, distinto de deteriorar su aislamiento. [S03, p. 16; S25, p. 32; inferencia funcional]

La recuperación dependerá de que el relé sea mantenido o biestable y del estado que conserve el controlador; no se asigna aquí una de esas arquitecturas a todos los relés Voyager. Validar órdenes y calificar el aislamiento son medidas diferentes. Una maniobra falsa puede afectar la misión aunque contactos y bobina sigan sanos.

**Cómo explicarlo en clase.** «Un relé no cambia un bit como una memoria, pero puede recibir una orden equivocada de ella. Si el mando dura lo suficiente, conecta o desconecta una carga real. Hay que distinguir el relé dañado del relé sano que obedece una orden falsa».

''',
'3.13':'''#### Resonador y electrónica del oscilador

El cuarzo es un resonador piezoeléctrico; su respuesta se representa cerca de una resonancia mediante una rama equivalente mecánica-eléctrica. Cambios en defectos y propiedades efectivas pueden modificar frecuencia y pérdidas, con dependencia del material y preparación. No se deriva aquí una magnitud universal de cambio a partir de dosis. El manual NASA describe sensibilidad del cristal y el informe Voyager documenta selección de barras. [S26, §8.6.8; S01, §VIII.F]

Un pulso en la electrónica que mantiene o conforma la oscilación también puede perturbar el reloj sin alterar permanentemente el cuarzo. Es una consecuencia posible del circuito, no una observación de Voyager establecida por el ensayo de barras. Distinguir deriva de frecuencia, fase momentánea y pulso lógico extra evita atribuir toda falla temporal al cristal. [S35; inferencia de circuito]

**Cómo explicarlo en clase.** «El cristal fija una referencia de tiempo y puede cambiar su respuesta según material y exposición. Pero el reloj también tiene electrónica: un pulso espurio allí no significa que el cuarzo haya cambiado permanentemente de frecuencia».

'''}
import re
for key,add in parts.items():
    pat=r'(### '+re.escape(key)+r' .*?)(?=\n### |\n## |\Z)'
    match=re.search(pat,s,re.S)
    assert match,key
    s=s[:match.end()]+ '\n'+add+s[match.end():]
hardware='''### 4.4 Identificación de tecnología y alcance del inventario

**No era «todo TTL salvo una memoria».** Tomayko distingue el prototipo FDS con memoria plated-wire y 150 IC TTL de baja potencia de la evolución hacia procesador y memorias CMOS. El informe de radiación afirma uso de numerosos CMOS correspondientes a 28 funciones lógicas. Esto no identifica automáticamente la familia de cada circuito de CCS/AACS ni permite llamar «microprocesador monolítico» a cada computadora. [S04, pp. 182–183; S01, §VI.B]

| Ejemplo | Evidencia disponible | Qué no se atribuye |
|---|---|---|
| CMOS RCA CD4000 | Uso de funciones lógicas y proceso modificado en el programa | Geometría única o inmunidad de todo CMOS |
| 2N2222 / 2N2907A | Curvas y ensayos del programa por fabricante/polarización | Placa y función de vuelo sin esquema identificado |
| 1N4148 / 1N5711 | Evaluación de diodos, p. 7-53 | Un rectificador de potencia concreto de la nave |
| Capacitores B11B de teflón | Ensayo de valores 0,02 y 0,05 µF | Inventario de todos los capacitores instalados |
| Redes Dale de película metálica | Ensayo de estabilidad resistiva | Ausencia de toda fuga o perturbación durante exposición |
| Transistores de potencia | Fotografías de montajes de ensayo en §V | Identificación de MOSFET de potencia o modelo/BOM de vuelo |

Los ensayos de componentes y la arquitectura de la nave se complementan, pero no sustituyen un esquema revisado y su lista de materiales. En la exposición se nombrarán componentes concretos con esta etiqueta de alcance.

'''
s=s.replace('## 5 Mitigaciones y ejemplos cuantitativos',hardware+'## 5 Mitigaciones y ejemplos cuantitativos',1)
chain='''### 5.7 Ejemplo de un espurio que deja una consecuencia

**Circuito conceptual, no plano ni evento de Voyager:** sensor → amplificador → comparador → registro de mando → carga. Una partícula genera carga en una unión del amplificador; aparece un pulso de salida. Si ese pulso cruza el umbral y satisface las condiciones temporales del receptor, el registro cambia. El amplificador vuelve a su punto normal, pero el registro sigue ordenando activar la carga. [S35, §§2 y 4; aplicación conceptual]

Tres tiempos son distintos: duración de la corriente inducida, recuperación del circuito analógico y permanencia del estado registrado. Un pulso demasiado pequeño, demasiado corto o fuera de la ventana de captura puede no producir esa consecuencia. No todo evento alcanza el final de la cadena.

**Ejemplo numérico ilustrativo.** Un nodo con C = 10 pF que recoge Q = 1 pC rápidamente respecto de su descarga experimenta aproximadamente ΔV = Q/C = 0,1 V. Con una resistencia equivalente de 100 kΩ, RC = 1 µs. Sin amplificación ni realimentación, el incremento decae aproximadamente como 0,1·exp(−t/1 µs) V. Si el nodo estaba 50 mV por debajo del umbral, lo supera durante unos 0,693 µs en ese modelo. Eso solo producirá una captura si el receptor responde en ese intervalo. No son carga, umbral ni tiempos de un dispositivo Voyager.

| Medida general | Qué interrumpe | Límite |
|---|---|---|
| Componente con menor sensibilidad o blindaje adecuado | Generación del efecto o exposición relevante | No elimina todos los eventos ni todo el espectro |
| Filtrado y control de impedancia | Amplitud/duración del pulso que llega al receptor | Puede alterar señal útil; pulsos lentos o grandes pueden atravesarlo |
| Histéresis o validación temporal | Interpretación de la señal como una orden | Debe definirse según señal legítima y peor perturbación |
| Comprobación de datos/estado | Detecta ciertas consecuencias | No detecta todos los errores ni corrige sin información adicional |
| Reescritura, reconfiguración o reinicio seguro | Recupera función tras estado erróneo | No repara daño físico y puede perder información |
| Márgenes y análisis con parámetros degradados | Evita que deriva acumulada invalide la función | No reemplaza el análisis temporal |

Esta tabla explica funciones de ingeniería, no una lista de técnicas confirmadas en Voyager. Las medidas de misión documentadas permanecen vinculadas a sus fuentes en §§4–6.

'''
s=s.replace('## 6 Fallas reales y continuidad de la misión',chain+'## 6 Fallas reales y continuidad de la misión',1)
s=s.replace('El eje para exponer es: **la radiación modifica materiales;', 'El eje para exponer es: **la radiación genera y desplaza carga, y puede modificar materiales;')
s += '\nUn componente puede sobrevivir y aun así entregar una señal incorrecta. La continuidad funcional exige estudiar tanto los parámetros degradados como los pulsos que se generan, propagan, capturan o rechazan.\n'
# Referencias nuevas, conservando las ya enlazadas.
s=re.sub(r'(?<![\w/])(S\d{2})(?![\w]|\]\()',lambda m:f'[{m[1]}](04_fuentes.md#{m[1].lower()})',s)
p.write_text(s)
print('Dossier ampliado: 13 familias, hardware y ejemplo de espurio.')
