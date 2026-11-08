# Corrección asistida por IA de la versión 4 del Informe del Proyecto del Grupo 3

**Grupo:** 3 — Sistema Inteligente Multimodal de Detección y Predicción de Glucosa
**Integrantes:** Brischetto, García Vitale, Vigo Abad, Giachetti, Cavicchioli, Monti, Del Rio, Cabrera
**Versión evaluada:** 4 (35 páginas)
**Fecha:** 2026-11-06
**Tipología declarada:** Masivo

> [!NOTE]
> Esta corrección se basa en el PDF y en la planilla enlazada (*Proyecto actualizado 18 meses – flujo de caja agrupado*, descargada por el docente), que se analizó: hoja de supuestos, flujo mensual, tareas y sprints. El modelo se **reprodujo por completo** (VAN, TIR, capital mínimo y recupero coinciden con el informe). Las macros no se ejecutaron. Los resultados de escenarios son **cálculos propios sobre su modelo**, con fines educativos.

---

## Métricas de Avance y Prioridades

- Subsecciones evaluables (lista estándar de 27): **23 con desarrollo real**, **3 parciales** (Precios y receptividad, Financiamiento y estrategias, 4.2.2 Recursos necesarios) y **1 pendiente** (4.1.2 Versiones evolutivas).
- Avance global estimado: **≈ 91 %** (≈ 85 % si no se cuentan las parciales). Es un informe muy trabajado, con cálculos que cierran. Las observaciones apuntan a **medir el objetivo central (el sensado)**, a **respaldar las partidas y plazos más inciertos** y a la **economía de quien paga**.

> [!TIP]
> **Prioridades para V5 (ordenadas por impacto)**
> 1. **Definir criterios de aceptación medibles del sensado** (hoy se fijan "en S1–S6") y **alinear el objetivo y los entregables con los 18 meses** que ejecutan el plan y el flujo.
> 2. **Reubicar requerimientos vs. diseño**, incorporar las **especificaciones** y completar el **AMFE con O, D y NPR**.
> 3. **Respaldar las partidas globales y los plazos más inciertos**: bioquímica, evaluación clínica, trámites y registro. Revisar sueldos y la estructura posterior al mes 18.
> 4. **Definir quién paga y calcular su beneficio y costo total** (USD 800 más recambios). Cuantificar el mercado accesible.
> 5. **Escenarios con un caso pesimista creíble** (retraso regulatorio, retención, ritmo de altas), **detalle del cálculo de VAN y TIR** (un flujo por base de tiempo: mensual para I+D e inversión, anual para el resumen) y justificación de la tasa.
> 6. **Aspectos a cubrir**: reubicar lo que es desarrollo, completar lo que falta y sumar las versiones evolutivas.
> 7. Mostrar en el informe la **BOM** y los datos clave que hoy están solo en las planillas.

---

## 1. Observación General de Estilo

- No se observan textos guía de la plantilla. Muy buena práctica: separan mediciones en sudor de estimaciones de glucosa sanguínea, advierten qué valores no son cotizaciones y citan fuentes.
- La **numeración no coincide con la v2.8**: el Resumen ejecutivo está en la Sec. 2 (en la v2.8 es la Sec. 5) y Definición, Evaluación y Planificación son las Sec. 3, 4 y 5. Verifiquen que trabajan con la última versión del template. La Sec. 2 no se evalúa.
- Hay mucho detalle de diseño: 4.2.2 ocupa seis páginas (carga, memoria, energía, cuentas). Prioricen lo esencial. Las aclaraciones "no es una cotización" se repiten: alcanza con una nota general.
- El informe debe poder leerse sin las planillas. Traigan al texto la BOM, el flujo anual y los escenarios.

---

## 2. Evaluación Sección por Sección

### Secciones 1 y 3 (Introducción, 3.1 a 3.3)
- **Introducción**: clara y de una página (necesidad, destinatario, hitos, advertencias sobre lo no demostrado).
- **3.1 Misión y visión**: bien diferenciadas, con límites explícitos.
- **3.2 Objetivo**:
  - *Inconsistencia*: el objetivo es un **MVP técnico en 12 meses**, pero el plan y el flujo ejecutan **18 meses** (evaluación clínica, registro, lote de 100 kits, preparación comercial) que no figuran como objetivo ni como entregable en 3.3. *Preguntas*: ¿el proyecto termina en el MVP (M12) o en el lanzamiento (M18)? Si es lo segundo, el objetivo y los entregables deben incluir M13 a M18. Si es lo primero, esas tareas pertenecen a una etapa posterior (¿aspectos a cubrir?).
  - *Omisión crítica (Medible)*: "las tolerancias analíticas y los criterios clínicos se fijarán en S1–S6". Hoy no se puede verificar si el MVP cumple: no hay una sola métrica de desempeño del sensado. *Preguntas*: ¿qué error respecto de la referencia aceptarían para cada analito? ¿Qué pasa si en M7 el prototipo no lo alcanza? (Ver Anexo I, punto 1).
  - *Reconocimiento*: el sensado en sudor con cortisol por MIP y la predicción tienen incertidumbre real, y la revisión de aptitud en M7 es una buena práctica. Distingan en el objetivo qué es **por descubrir** (sensado, predicción) y qué es **ingeniería conocida** (electrónica, BLE, aplicación, carga).
- **3.3 Entregables**: buen formato por componente. Los criterios del parche ("calibración, interferencias, estabilidad y adhesión") no tienen valores. Faltan entregables para lo que ejecuta M13 a M18 (informe de evaluación clínica, expediente de registro, lote inicial, documentación).

### 4.1 Tipo de proyecto
- Justificado como *Masivo*. *Preguntas*: con USD 800 más USD 100 mensuales de recambios, ¿es realmente un producto para el público masivo? Con el desempeño aún no demostrado, ¿hay una parte de Innovación / Investigación que cambie los aspectos a cubrir?

### 4.2.1 Requerimientos técnicos y funcionales
- Muy buena la separación entre mediciones en sudor, asociaciones y predicciones, y los requisitos de incertidumbre.
- *Error conceptual*: la tabla "Requerimientos técnicos" mezcla requerimientos con **decisiones de diseño y componentes** (papel plegado tipo origami, MIP, potenciostato, baterías de 750 y 850 mAh, "calibración adaptativa"; el requerimiento 1 incluye "el pH como referencia de calibración"). Reubiquen al diseño o a las especificaciones y dejen en el requerimiento el *qué*.
- *Omisiones críticas (preguntas)*: ¿qué rango, exactitud, tiempo de respuesta y retardo entre sudor y sangre necesita cada medición? ¿Qué cantidad mínima de sudor? ¿Qué normativa aplica a un dispositivo en contacto con la piel durante siete días, con batería de litio (seguridad eléctrica, biocompatibilidad, gestión de riesgos)? ¿Qué requisitos de privacidad tiene un dato de salud? La actualización remota de firmware aparece en soporte (4.2.4) pero no como requerimiento.

### 4.2.2 Uso de los dispositivos y 4.2.3 Diseño preliminar
- *Cálculos verificados* (coinciden): presupuesto de energía (3,57 y 4,05 mA; 171 y 170 h; 162 y 158 h con el enlace directo), memoria (64 B × 720 = 45 KiB por día; 128 KiB ≈ 2,8 días) y tiempos ideales de carga (3,0 y 3,4 h). Está bien aclarado que t = C/I no predice la carga real.
- *Inconsistencias y preguntas técnicas*:
  1. **No hay sección de especificaciones** derivadas del diseño (el *cómo* cuantitativo). Las de energía y memoria están dispersas en 4.2.2 y las del sensado no existen.
  2. **Parche de papel con lectura cada 2 minutos durante 7 días**: ¿las reacciones colorimétricas son reversibles o se consumen? ¿Cómo se renueva el sudor y cuánto sudor hace falta en reposo? ¿Qué pasa con la estabilidad de los reactivos sobre la piel durante una semana? Respáldenlo con **fuentes de la literatura**. Este es el riesgo técnico central (R1).
  3. **Dos lectores por kit**: el segundo cuesta USD 61,38 (55,30 + 6,08), **≈ 31,5 % del costo directo** de USD 194,57. Se justifica por evitar el hueco de ≈ 3 h de recarga semanal. Como el parche se recambia cada 7 días y el lector se desacopla en ese momento, ¿la recarga no podría coincidir con el recambio? ¿Qué problema resuelve el segundo lector y cuánto cuesta (con logística)?
  4. **Autonomía**: 3,5 mA para tres AS7341, el AD5941, la iluminación y el BLE cada 2 minutos es una hipótesis que reconocen. Contrástenla con las hojas de datos y el ciclo de trabajo.
  5. **BOM**: los conjuntos de USD 28,40 y USD 7,05 no muestran precio por componente. Incluyan la BOM (componente, cantidad, USD).
  6. **Cuenta y activación del kit (4.2.2.4)**: el acceso a la aplicación se limita a compradores mediante número de serie, código de activación o prueba de posesión por BLE, con transferencia de propiedad y desvinculación entre cuentas. Esto **agrega complejidad** (flujos de alta y recuperación, servicio de autenticación, registro de activaciones, tareas "A" del plan) a un producto Masivo, cuya puesta en marcha debe ser simple. *Preguntas*: ¿qué problema resuelve? Dentro del alcance, la aplicación sin los dispositivos no tiene uso: el hardware ya funciona como "licencia". **Evalúen un vínculo fácil, como el de un auricular Bluetooth** (emparejamiento BLE cifrado, sin códigos), y distingan dos cosas: (a) *emparejar* los dispositivos con el teléfono, que debe ser sencillo; (b) *atar la unidad a una cuenta*, que solo se justifica con una razón concreta (privacidad de datos de salud, trazabilidad por unidad o lote ante un retiro, reventa). La privacidad se resuelve con emparejamiento cifrado y la trazabilidad puede lograrse registrando el número de serie en el alta, sin impedir el uso. Comparen el costo de lo que hoy diseñan con el beneficio que aporta.
- **AMFE (4.2.3.1)**:
  - *Error conceptual / omisión crítica*: la tabla tiene solo **Severidad cualitativa (Media / Alta)**. Falta **O, D y NPR** (Decisión #4). Las fallas que incluyen son aplicables y bien mitigadas (luz ambiente, degradación del reactivo, plegado, pérdida de BLE, alternancia de lectores, LED).
  - *Fallas importantes posiblemente omitidas (preguntas)*: ¿qué ocurre con **poco o nulo sudor** o piel contaminada? ¿Y con una **reacción cutánea** al adhesivo o los reactivos tras siete días? ¿Y con un mal **acople lector–parche**? ¿Y con el calentamiento de la batería junto a la piel? ¿Y con una actualización remota fallida? ¿Y con la exposición de datos de salud? ¿Y con activaciones involuntarias del gesto?

### 4.2.4 Aspectos a cubrir
- *A reubicar*: **Pruebas** y **Servicios especializados** (laboratorio de química para seleccionar y adaptar reactivos) son parte del **desarrollo** y ya están en el plan. Lo mismo vale para las cotizaciones vigentes de "Compras". Revisen qué queda para después del MVP.
- *Posibles aspectos no contemplados (preguntas)*: ¿garantía, reposición y devoluciones? ¿Distribución, almacenamiento y vida útil del parche? ¿Manual de uso, etiquetado e instrucciones para el usuario? ¿Protección de datos personales de salud? ¿Vigilancia posterior a la venta? ¿Facturación y cobro de los recambios? ¿Seguro de responsabilidad de producto? ¿Residuos de baterías y parches?

### 4.3.1 FODA
- Cumple el criterio: está orientado a la **capacidad de ejecución** (equipo, recursos, entorno). Buenas debilidades (experiencia limitada en biosensores y regulación, desempeño no demostrado).
- *Observaciones*: F3 y F4 (sistema de gestión, modelo operativo y financiero) son herramientas de gestión, no capacidades técnicas del equipo. F2 afirma capacidad de integrar, mientras D1 reconoce falta de experiencia en biosensores. *Pregunta*: ¿quién diseña y valida el parche si el equipo no tiene un perfil de química o bioingeniería y el laboratorio es un técnico con una partida externa de USD 12.000? Las oportunidades son genéricas.

### 4.3.2 Riesgos de ejecución
- Muy buena: escalas definidas, responsables, umbral y residuales. **Los 12 productos S×O son correctos** (54, 48, 48, 35, 30, 24, 35, 40 y sus residuales) y la conclusión de cuáles quedan sobre el umbral coincide.
- *Amenazas del FODA sin riesgo asociado*: **proveedores e importación** (PCB en China, aduana, plazos) no figuran en R1 a R8.
- *Riesgos críticos posiblemente omitidos (preguntas)*: ¿qué pasa si falta una de las cuatro personas, cada una con un rol único? ¿Y si la evaluación clínica requiere más participantes que los diez kits previstos? Definan qué hacen si R1 se concreta en M7 (plan B).

### 4.4.1 Mercado y público objetivo
- Bien: parten de la población con diabetes (IDF, ≈ 4,3 millones; ≈ 4 millones con tipo 2) y no de la facturación mundial de CGM, y reconocen que no es un relevamiento. *[Verificar la cifra y su cita en la fuente]*.
- *Omisión*: el mercado accesible no está cuantificado (uso de CGM, teléfono compatible, cobertura, disposición a pagar). El adquirente puede ser el paciente, una obra social o una clínica: **¿cuál es el comprador principal sobre el que se calcula el precio y el flujo?** Revisen este punto en clase con el docente (Anexo I, punto 3).

### 4.4.2 Competidores y sustitutos
- Razonable (CGM, SmartGuide, Levels, mySugr) pero **sin precios** de ninguna alternativa. El sustituto más obvio, el **glucómetro capilar con tiras**, no figura. Una búsqueda estándar debería mostrar si existe algún producto de sensado en sudor o no invasivo *[verificar]*. Comparen el costo total del usuario (CGM más este complemento).

### 4.4.3.1 y 4.4.3.2 Costos
- *Cálculos verificados*:
  - La Tabla 5 suma USD 194,57.
  - Lector USD 55,30; pulsera USD 33,65; parche USD 11,33.
  - CIF USD 172,15 y logística USD 105,97, con desembolso de USD 275,12 y 300,54 por kit.
  - Lote de 112 kits: USD 18.944,80 + 11.868,36 + 300 = USD 31.113,16 (311,13 por kit).
  - Nómina USD 11.200 por mes × 18 = USD 201.600.
  - El **capital mínimo de USD 368.813,16 se reconstruye** con las partidas más la reserva del 10 % (USD 9.100).
- *Errores u omisiones críticas*:
  - Las partidas más inciertas son **globales y sin cotización**, como ya reconocen: bioquímica USD 12.000 (adaptar reactivos, MIP, desempeño en sudor), QA externo USD 8.000, evaluación clínica USD 30.000 y ensayos y trámites USD 10.000. Los servicios externos suman ≈ USD 70.000 (≈ 19 % del capital) frente a la nómina (≈ 55 %), pese a que el sensado es el corazón del producto.
  - Los ingenieros se presupuestan a ARS 3.500.000 brutos, **por debajo del promedio sectorial que ustedes citan** (ARS 3.738.000). Los perfiles de embebidos con BLE o de biosensores no suelen ubicarse debajo de ese promedio *[verificar]*. Verifiquen también el factor laboral (1,40) y el tipo de cambio (ARS 1.500/USD).
  - La dotación termina en M18. ¿Quién mantiene firmware, aplicación, nube, soporte, calidad y vigilancia posterior desde M19, y a qué costo de mercado?
  - USD 500 mensuales fijos de herramientas y nube durante 48 meses, mientras los clientes activos crecen hasta ≈ 1.280 (ver Anexo I, punto 4). ¿Escala el costo con usuarios (cuentas, correos, nube)?
  - No hay impuestos (IVA, ingresos brutos, ganancias) y la carga del 45 % sobre CIF es una simplificación *[verificar]*. ¿Qué rol y qué costo tienen los 8 integrantes si el equipo presupuestado es de 4?
- *Preguntas*: ¿qué respalda cada partida global? ¿Qué cotización o consulta a laboratorios o centros de investigación clínica pueden pedir?

### 4.4.3 Precios y receptividad *(parcial)*
- USD 800 por kit y USD 25 por recambio (cuatro por mes): **cubre el costo directo con margen** (≈ 62 % en el kit) y reconocen que es un supuesto a validar.
- *Error conceptual / omisión*: no se calcula el **beneficio para quien paga**. El primer año cuesta ≈ USD 1.950 (≈ ARS 2,9 millones a su propio tipo de cambio, cerca de un sueldo bruto mensual de sus ingenieros) y luego USD 1.200 por año, **además** del CGM. *Preguntas*: ¿qué gana o ahorra el paciente, la obra social o la clínica por ese costo? ¿Qué retención mensual del 95 % (≈ 46 % de bajas por año) respalda la fuente? (Anexo I, punto 2).

### 4.4.3.4 y 4.4.3.5 Flujo de fondos, VAN y TIR
- *Cálculos verificados*: las sumas y los acumulados de la Tabla 7 son correctos (−233.200 → −311.484,63 → −131.541,74 → +421.258,92). Los **ingresos de los años 2 a 4 se reproducen exactamente** con kits × USD 800 más USD 100 mensuales por cliente activo (retención 95 %). El capital mínimo concuerda con la Tabla 7. La etapa de inversión (18 meses) coincide con el plan.
- *VAN y TIR*: recalculé con los flujos anuales de la Tabla 7 al 20 % y obtuve **VAN ≈ 122.000 (fin de año), ≈ 146.400 (inversión del año 1 en t = 0, criterio esperable del curso) y ≈ 133.700 (mitad de período), con TIR ≈ 40,8 %**. El informe indica **119.928,98 y 37,36 %** con flujos mensuales: el orden de magnitud es consistente y la diferencia se explica por la convención de tiempo. **Detallen el cálculo** (flujo por período, factor de descuento, valor presente y convención) según la Decisión #14.
- *Observación crítica*: el **año 4 aporta más que todo el VAN** (su valor presente es ≈ 2,2 veces el VAN) y depende de 840 kits en M43 a M48 (el ritmo pasa de 300 a 800 y a 1.680 kits por año). El VAN se anula con una caída de ≈ 33 % de los flujos netos de los años 3 y 4 (cota simple). *Preguntas*: ¿qué capacidad de captación (aliados, clínicas, médicos) sostiene ese ritmo? ¿Qué pasa con un retraso regulatorio, si el horizonte es fijo (48 meses) y no hay valor terminal?
- *Base de tiempo del flujo (recomendación)*: el VAN y la TIR se calculan con un **flujo mensual de 48 meses**, pero el informe muestra la **Tabla 7 anual**, y sus resultados no se pueden reproducir desde esa tabla (por eso mi recálculo anual da otro VAN, según la convención). Mezclar bases de tiempo confunde al lector. Presenten **un flujo por base de tiempo, con su propio cálculo y la conciliación entre ambos**: (1) **mensual** para la etapa de I+D e inversión (M1 a M18) y el arranque comercial, donde los desembolsos son discretos (nómina, lotes, ensayos, trámites) y definen el capital mínimo; (2) **anual** para el resumen de los años 1 a 4, con el VAN y la TIR calculados sobre esa misma tabla y la convención de tiempo explícita. *Base trimestral en la planilla*: la hoja "Flujo agrupado" presenta **M1 a M18 mensual, M19 a M48 en trimestres (T7 a T16) y resúmenes anuales**, tres bases en una misma tabla. Son sumas de la hoja mensual (el VAN y la TIR salen del flujo mensual), así que el trimestre no agrega información al cálculo. *Preguntas para el grupo*: ¿qué sentido tiene la base trimestral para M19 a M48 y por qué la eligieron? ¿Hay estacionalidad, pagos o renovaciones trimestrales, o un dato que se conozca con esa precisión, que mejore la predicción frente al año? Las ventas de los años 2 a 4 no se conocen con precisión de trimestre, de modo que desagregarlas da **falsa precisión**; si no hay una razón, simplifiquen a mensual + anual.
- *Planilla*: reproduje el modelo mensual (**VAN 119.928,98; TIR 37,4 %; capital mínimo USD 368.813; recupero en M41**) y coincide con el informe. Las ventas salen de *aliados × pacientes × adopción* (30 a 35 % de los pacientes alcanzables) y los ingresos recurrentes de USD 100 por cliente y mes con retención del 95 %.
- *Escenarios*: el informe muestra solo el **base**, pero la planilla trae un escenario **"Conservador" (72 / 193 / 400 kits por año contra 300 / 800 / 1.680)** que no aparece en el texto. Al correrlo, el VAN da **negativo** (entre ≈ −280.000 y −340.000 según se escalen las demos y la incorporación) y el capital mínimo sube a ≈ USD 420.000. Es una información clave que el informe omite: **tráiganla al texto** y expliquen qué decisión tomarían con ese resultado (Anexo I, punto 4).
- *Estructura posterior a M18 (planilla)*: la nómina vale **cero desde M19**; el soporte (40 h cada 100 clientes) y el equipo comercial sí están, pero no hay ingenieros para firmware, aplicación, QA ni vigilancia posterior. Con solo la mitad de la dotación (≈ USD 5.600 por mes) el VAN cae de ≈ 120.000 a ≈ 18.000.
- *Costos de la BOM*: todas las partidas de la BOM y las globales son **asignaciones internas sin cotización**. La nube y las herramientas son fijas (USD 500 por mes) mientras los clientes activos llegan a ≈ 1.280.
- La **tasa del 20 %** no está justificada. Muestren el VAN con otras tasas.
- *Financiamiento (parcial)*: informan el capital mínimo (USD 368.813,16), sin estrategia. Alcanza con comentar brevemente cómo piensan cubrirlo.

### 5. Planificación del proyecto
- Metodología por sprints con 199 tareas, 6 épicas, 12 features y 42 historias: válida para el curso. *Cálculos verificados*: las horas por tramo suman 8.856,40; la capacidad es 11.520 y queda una reserva de 2.663,60 (≈ 23 %). El sprint S14 suma 245 h (67 + 69 + 49 + 60). El plan coincide con los 18 meses del flujo.
- **5.1 Equipo**: cuatro puestos con un solo responsable por rol y horas estimadas "a partir de su experiencia en trabajos prácticos". *Horas por frente (planilla de tareas, 8.856 h)*: Transversal 2.304 h (26 %), Aplicación 1.875 h (21 %), **Parche 1.812 h (20,5 %)**, Lector 1.487 h (17 %) y Pulsera 1.378 h (16 %). Por rol: software 2.428 h, embebidos 2.437 h, QA 1.836 h y laboratorio 2.155 h. El frente parche (39 tareas, ≈ 100 h por mes parejas) lo ejecuta en un **75 % el técnico de laboratorio** (1.358 h), un único puesto que además aporta a las tareas transversales. El mes más cargado de un integrante llega a ≈ 159 h sobre 160 disponibles: **sin holgura individual**, aunque la reserva global sea del 23 %. *Preguntas*: ¿cómo se cubre una ausencia del único responsable de laboratorio o de QA? ¿Las horas de ensayo dependen de la disponibilidad de instrumental externo?
- **5.2 a 5.4**: secuencia clara. En el texto no se ven las **dependencias externas** (fabricación y envío de PCB, laboratorio, comité de ética, ANMAT), aunque la planilla las marca en **95 tareas** (por ejemplo, "ventana M8–12 estimada; no plazo garantizado"). Súbanlas al calendario del informe y señalen el **camino crítico**: ¿qué tarea retrasa a todas las demás si el proveedor tarda 4 semanas más?
- **5.5 Plazos regulatorios**: aprobaciones en M8 a M12, evaluación en M13 a M15 y registro en M16 a M18. Ustedes citan 90 días hábiles (≈ 4 meses) solo para la presentación de investigación. ¿Qué respalda tres meses para evaluar y tres para registrar? *[Verificar normativa y plazos con asesores]*. Revisen si la evaluación clínica y el registro son parte del proyecto o aspectos a cubrir, y qué ocurre con el flujo si se demoran (Anexo I, punto 5).
- **4.1.2 Versiones evolutivas**: pendiente. Aclaren qué incluye la versión comercial y qué las versiones posteriores (por ejemplo, las funciones predictivas "sujetas a resultados") y sus costos en el flujo.

---

## 3. Secciones Pendientes

- **4.1.2 Versiones evolutivas**: sin desarrollo.
- **Parciales**: 4.2.2 Recursos necesarios (no hay inventario por categorías: infraestructura, equipamiento de laboratorio, licencias, servicios), Precios y receptividad, y Financiamiento (estrategias).
- **Especificaciones técnicas**: no existe una sección propia (ver 4.2.2).
- **No evaluadas** (Decisión #8): Sec. 2 (Resumen ejecutivo) y seguimiento.

---

## Anexo I: Criterios de aceptación, economía del comprador, mercado, VAN y escenarios, y plazos regulatorios

> [!NOTE]
> Este anexo tiene propósito **educativo**. Los cálculos usan **datos del propio informe**. Los valores externos o rangos están marcados *[verificar]* y deben obtenerse de fuentes citables antes de usarlos.

### 1. Del "que funcione" a un criterio de aceptación medible

El objetivo del proyecto es entregar un MVP que **cumple especificaciones**. Que "funciona" no se declara: se demuestra con una **medición contra una referencia**, bajo condiciones definidas y con un umbral de aceptación fijado **antes** del ensayo. Hoy el informe difiere esos criterios a S1–S6, y entonces el hito de M12 no tiene una condición que lo apruebe o lo rechace.

Para cada salida (glucosa, lactato, cortisol, pH, frecuencia cardíaca, predicciones) conviene completar una ficha como esta:

| Salida | Referencia | Métrica de exactitud | Umbral de aceptación (hipótesis inicial) | Condiciones y muestra | Fuente que lo respalda |
|---|---|---|---|---|---|
| (por completar) | ¿contra qué se compara? | ¿qué error y qué relación se mide? | ¿cuánto aceptan? | ¿cuántas personas, cuántas horas, qué actividad? | literatura / norma |

En glucosa se suelen usar métricas de exactitud contra una referencia y análisis de cuadrícula de errores *[verificar cuáles y con qué valores en la literatura]*. En sudor hay además un **retardo** entre el valor en sudor y el valor en sangre, y una **cantidad mínima de sudor** para medir: ambos son parte del requerimiento, no detalles del ensayo.

**Cómo se trata la parte innovadora.** Sensar cortisol con un MIP en un parche de papel o predecir a 1–8 horas son incertidumbres reales: el objetivo puede incluir **determinar con un criterio explícito si se alcanza** un desempeño dado. Lo que no puede quedar abierto es el criterio. La electrónica, el BLE, la carga y la aplicación son ingeniería conocida: deben cumplirse, no "evaluarse".

*Qué debería hacer el grupo*: fijar ahora, aunque se ajusten en S1–S6, las hipótesis de aceptación por salida y por qué se eligen; separar en el objetivo lo **por descubrir** de lo **conocido**; y definir qué decisión se toma si la revisión de M7 no alcanza el umbral (por ejemplo, qué analitos se conservan o qué función se posterga). Esa decisión debe verse en el plan y en el flujo.

### 2. ¿Quién paga y cuánto le conviene?

Con los números del informe, el costo para el usuario es USD 800 por el kit más USD 25 por cada uno de los cuatro recambios mensuales (se descuentan dos pagos en el mes de alta):

- **Primer año**: 800 + 100 × 12 − 50 = **USD 1.950**. A su propio tipo de cambio (ARS 1.500/USD) son ≈ ARS 2,9 millones, cerca de un sueldo bruto mensual de los ingenieros de su equipo (ARS 3,5 millones).
- **Años siguientes**: USD 1.200 por año (≈ ARS 1,8 millones).
- Todo **además del CGM**, que el usuario ya usa o considera usar. El costo total de propiedad es la suma de ambos *[relevar el precio de CGM en Argentina con fuente]*.

El producto tiene tres posibles pagadores (el paciente, la obra social o prepaga, y la clínica) y cada uno compra por una razón distinta:

- *Paciente*: ¿qué decisión cotidiana mejora, qué consulta o medición evita, y es eso lo que paga como particular?
- *Obra social o prepaga*: ¿qué costo evita (descompensaciones, consultas, internaciones) y con qué evidencia, que además todavía no existe?
- *Clínica*: ¿qué ingreso o fidelización le aporta ofrecer el servicio en un programa de seguimiento?

*Qué debería hacer el grupo*: elegir un **comprador principal** para el precio y el flujo, calcular su beneficio y compararlo con el costo total, y validar con entrevistas. No hace falta abrir otros modelos si el análisis no los vuelve claramente convenientes.

**La retención es la hipótesis más sensible.** Con 95 % mensual, ≈ 46 % de los usuarios se va en un año y la vida media es de unos 20 meses. Reproduje el modelo de ingresos del informe (kits vendidos × USD 800 más USD 100 mensuales por cliente activo): **los recambios son ≈ 49,5 % de los ingresos del año 4** y los clientes activos en M48 son ≈ 1.280 de los 1.940 kits vendidos. ¿Qué fuente respalda 95 %? ¿Cuántos usuarios de dispositivos vestibles o de sensores adhesivos los abandonan por molestias, irritación o por costo? *[Relevar con fuentes]*.

### 3. Dimensionar el mercado accesible (de abajo hacia arriba)

El informe parte bien de la población con diabetes. Para llegar al mercado que el producto puede alcanzar, conviene recorrer un embudo y justificar cada paso con una fuente:

1. Personas con diabetes en Argentina (≈ 4,3 millones adultos según la IDF; ≈ 4 millones con tipo 2, extrapolando el 90–95 %). *[Verificar]*
2. De ellas, las que **usan o usarían un CGM** (acceso y cobertura de CGM en el país) *[relevar]*.
3. De esas, las que tienen **teléfono compatible** y capacidad de usar la aplicación.
4. De esas, las que podrían **pagar** USD 1.950 el primer año (o cuya cobertura lo financiaría).
5. De esas, las que **alcanzan** a través de clínicas, médicos y aliados en el período.

Los 1.940 kits vendidos en 30 meses son ≈ 0,05 % del paso 1, un número pequeño que **no dice nada** hasta compararlo con el paso 4 o 5. Más importante es la **capacidad de captación**: el plan pasa de ≈ 25 a ≈ 67 y a ≈ 140 altas por mes. ¿Cuántos aliados clínicos se necesitan para sostener 140 altas mensuales? ¿Cuántos pacientes aporta cada uno y con qué ciclo de venta (demostraciones, acuerdos, capacitación)? ¿Qué costo comercial implica y dónde está en el flujo?

### 4. Anatomía del VAN y escenarios

**Convenciones de tiempo** (flujos anuales de la Tabla 7, tasa del 20 %):

| Convención | VAN (USD) | TIR |
|---|---|---|
| Años 1 a 4 al final de cada año (t = 1…4) | ≈ 122.000 | ≈ 40,8 % |
| **Criterio esperable del curso**: inversión del año 1 en t = 0; años 2 a 4 en t = 1…3 | ≈ 146.400 | ≈ 40,8 % |
| Mitad de cada período | ≈ 133.700 | ≈ 40,8 % |
| **Informe (flujos mensuales)** | **119.928,98** | **37,36 %** |

Los valores son coherentes y la diferencia se explica por la convención de tiempo. Por eso se pide el **detalle del cálculo**: tabla con cada período, flujo, factor de descuento y valor presente; la tasa mensual equivalente (con 20 % anual efectivo, ≈ 1,53 % mensual) y el momento del flujo dentro del mes.

**De dónde viene el valor.** Con la convención de fin de año, los valores presentes por año son aproximadamente −194.300 (año 1), −54.400 (año 2), +104.100 (año 3) y +266.600 (año 4): el **año 4 vale ≈ 2,2 veces el VAN** y compensa todo lo anterior. Es un año con tasa de altas máxima (840 kits en M43 a M48), recambios al 49,5 % del ingreso y **sin valor terminal** posterior. Una caída de ≈ 33 % en los flujos netos de los años 3 y 4 lleva el VAN a cero (cota simple: una parte de los egresos varía con las ventas, por lo que el efecto real depende de su modelo).

**Un escenario pesimista creíble** mueve las variables que realmente se mueven:

- **Retraso regulatorio**: ventas desde M25 o M31 en lugar de M19, con la dotación y los costos fijos corriendo.
- **Ritmo de altas** menor (por ejemplo, la mitad), por captación o ciclo de venta.
- **Retención** menor que 95 %.
- **Desvío** en las partidas globales (bioquímica, evaluación clínica, trámites).
- **Precio** menor si la disposición a pagar no alcanza.

**Qué da el propio modelo del grupo** (reproducido de la planilla; cada fila cambia **una sola** variable respecto del base):

| Caso | VAN (USD) | TIR | Capital mínimo (USD) | Recupero |
|---|---|---|---|---|
| **Base** | 119.929 | 37,4 % | 368.813 | M41 |
| Retención 90 % (en vez de 95 %) | ≈ 75.700 | ≈ 31 % | 368.813 | M42 |
| Retención 85 % | ≈ 47.400 | ≈ 27 % | 368.813 | M43 |
| Ventas −25 % | ≈ −31.600 | ≈ 15 % | 368.813 | M45 |
| Ventas −50 % | ≈ −182.000 | ≈ −14 % | 368.813 | no recupera |
| Precio del kit USD 600 (en vez de 800) | ≈ −80.300 | ≈ 7 % | 368.813 | M47 |
| Lanzamiento con 6 meses de demora (M25) | ≈ −101.600 | ≈ 3 % | ≈ 387.000 | M48 |
| Lanzamiento con 12 meses de demora (M31) | ≈ −209.300 | ≈ −20 % | ≈ 402.000 | no recupera |
| Mitad de la dotación después de M18 | ≈ 18.100 | ≈ 23 % | 368.813 | M44 |
| Escenario "Conservador" de la planilla (72 / 193 / 400 kits) | negativo (≈ −280.000 a −340.000) | muy negativa | ≈ 420.000 | no recupera |

Lectura: el proyecto es **muy sensible a las ventas, al precio y al plazo regulatorio**, y poco a la retención. Con un 25 % menos de ventas ya no crea valor. Un retraso regulatorio de solo 6 meses, con el equipo completo corriendo, lo vuelve negativo (el horizonte fijo de 48 meses y la falta de valor terminal amplifican ese efecto). Estas cifras son del modelo del grupo, no una predicción: sirven para ordenar qué variable pesa más y qué evidencia (aliados, disposición a pagar, plazos de ANMAT) conviene reunir primero.

Para cada caso muestren VAN, TIR, capital mínimo y mes de recupero, en una tabla en el informe (hoy el escenario "Conservador" está solo en la planilla y no se comenta). Una tabla tipo "tornado" ordena qué variable pesa más.

**La tasa del 20 %.** Representa lo que exigiría quien aporta capital a un proyecto con este riesgo (técnico, regulatorio y comercial). Justifíquenla por componentes (rendimiento sin riesgo, riesgo país, prima por riesgo de etapa) y muestren el VAN con otras tasas. Recuerden que el flujo es **antes de impuestos** (ganancias, IVA e ingresos brutos) y que, con utilidades en los años 3 y 4, el impuesto no es un detalle.

### 5. Plazos y costos regulatorios: lo que más mueve la caja

Por su propia estructura, cada mes de demora con el equipo completo cuesta ≈ **USD 13.700** (nómina 11.200 + infraestructura 2.000 + herramientas 500). Doce meses de retraso son ≈ **USD 164.400**, cerca de **45 % del capital mínimo** de USD 368.813, sin contar las ventas que se desplazan y las que quedan fuera del horizonte de 48 meses.

El plan asigna tres meses a la evaluación clínica (M13 a M15) y tres al registro (M16 a M18), después de aprobaciones de investigación en M8 a M12. Ustedes mismos citan 90 días hábiles para la presentación de investigación. Para respaldar los plazos y las partidas (USD 30.000 de evaluación y USD 10.000 de trámites):

- Consulten a asesores regulatorios, a comités de ética y a centros que realicen estudios similares, y **citen** los plazos y costos obtenidos *[verificar con fuentes y normativa vigente]*.
- Armen la secuencia con dependencias (qué evidencia exige cada trámite, qué se presenta cuándo) y señalen el **camino crítico**.
- Definan si la evaluación clínica y el registro son parte del proyecto o aspectos a cubrir después del MVP; esa decisión cambia el objetivo, los entregables y el flujo.
- Incorporen la demora como una variable de sus escenarios.

Una partida global se respalda con **cantidad × tarifa**: horas por perfil, número de participantes, número de visitas, ensayos por laboratorio. Para bioquímica, por ejemplo, ¿cuántas formulaciones, ciclos de prueba y horas de laboratorio y asesoramiento requiere cada analito?

### 6. Qué debería hacer el grupo en V5

1. Fijar criterios de aceptación medibles del sensado, separar lo por descubrir de lo conocido, y alinear objetivo y entregables con los 18 meses (o separar la etapa posterior al MVP).
2. Reubicar los componentes de la tabla de requerimientos, incluir las especificaciones y completar el AMFE con O, D y NPR y las fallas faltantes.
3. Respaldar con cotizaciones o consultas las partidas de bioquímica, evaluación clínica y trámites, y revisar sueldos, factor laboral y la estructura posterior a M18.
4. Elegir el comprador principal, calcular su beneficio frente al costo total y cuantificar el mercado accesible con fuentes.
5. Detallar el cálculo de VAN y TIR, justificar la tasa y presentar en el informe un escenario pesimista con retraso regulatorio, retención y ritmo de altas.
6. Revisar los aspectos a cubrir, agregar riesgos de proveedores y personas clave, y completar 4.1.2 y 4.2.2.
7. Traer al informe la BOM, el flujo anual, el escenario "Conservador" y el calendario con dependencias externas que hoy están solo en las planillas.
