# Validación, discrepancias y límites

Fecha: 14 de octubre de 2026. Se revisaron unidades, cálculos, trazabilidad y correspondencia con las consignas. Esto es una investigación documental; no sustituye una revisión de los expedientes completos de vuelo.

## Cobertura de prompt.txt

| Consigna | Respuesta | Estado |
|---|---|---|
| Qué es la radiación cósmica y cómo se mide | Dossier §§1.1–1.2: origen, poblaciones, energía, flujo, fluencia, dosis, LET y cuentas | Respondida |
| Dónde está Voyager y a qué está expuesta | §§1.3–1.4: ambas trayectorias, espacio interestelar, distancias fechadas y medición reciente CRS | Respondida con límite: no hay efeméride exacta ni dosis por chip al corte |
| Electrónica, tensiones, materiales, fabricación y geometrías | §§3–4: familias, arquitectura, 30 V del bus, 10 V FDS, materiales y proceso documentados | Parcial: geometrías, dopados y materiales de cada lote pendientes |
| Efectos sobre semiconductores de la época | §§2 y 3.4–3.9; ensayos y proceso de fabricación Voyager | Respondida sin asignar un único proceso a toda la nave |
| Qué se esperaría en un caso normal | §6: pérdida de margen funcional, casos ilustrativos y límites de predicción | Respondida como inferencia; no hay plazo universal de falla |
| Qué hizo Voyager para mitigarlos | §5 y matriz: selección, ensayo, proceso, peor caso, blindaje, arquitectura y operaciones | Respondida con alcance por evidencia |
| Capacitores, pistas, dieléctricos, resistencias, inductores, diodos, etc. | Trece familias en §3 y mapa conceptual | Respondida; donde falta evidencia de vuelo se indica |
| Ver planos y cuántas Voyager hubo | §4.3: dos sondas, diagramas parciales y circuitos de ensayo identificados | Parcial: no se encontró juego completo de planos/BOM de vuelo |
| Explicar por qué sigue funcionando tras 50 años | §§6–7: casi 50 años, capacidades parciales y causas de falla diferenciadas | Respondida; no se cuantifica aporte causal de cada mitigación |
| Consignas de las imágenes | 00_consignas y selección de introducción, objetivos, conceptos, aplicación y conclusión | Transcritas; diseño final se aplicará al crear diapositivas |

## Cálculos revisados

| Cálculo | Resultado | Alcance |
|---|---|---|
| Edad V1: 05/09/1977 → 14/10/2026 | 49 años y 39 días | Fechas civiles, no precisión de hora de lanzamiento |
| Edad V2: 20/08/1977 → 14/10/2026 | 49 años y 55 días | Mismo criterio |
| 30.000 rad × 0,01 Gy/rad | 300 Gy = 300 J/kg | Mantener material Si al comparar dosis |
| RDM: 60/30 | 2, adimensional | Diseño documentado, no dosis acumulada medida |
| 5 pF / 0,02 µF × 100 | 0,025 % | Resultado relativo de capacitancia ensayada |
| 12 pF / 0,05 µF × 100 | 0,024 % | No certifica fuga, ESR ni toda la vida útil |
| 4 µA × 20 MΩ | 80 V | Escenario PWS documentado |
| (4 µA)² × 20 MΩ | 0,32 mW | Cálculo derivado del escenario |
| 500 V / 80 V | 6,25 | Cociente de tensiones, no margen de dosis |
| 10 nF × 10 GΩ; 10 nF × 1 GΩ | 100 s; 10 s | Modelo ilustrativo de fuga |
| 5 exp(−1/100); 5 exp(−1/10) | 4,950 V; 4,524 V | Retención aislada durante 1 s |
| 10 MeV·cm²/mg × 2330 mg/cm³ × 10⁻⁴ cm | 2,33 MeV | LET supuesto constante; ejemplo, no geometría Voyager |
| 2,33 MeV / 3,6 eV × carga elemental | 103,7 fC generados | Recogidos al 10 %: 10,37 fC |
| 10 fF × 1 V | 10 fC | Modelo estático ilustrativo, no Qcrit de vuelo |
| (1,2 + 1,2 + 2,4) × 10⁹ × 1000 | 4,8 × 10¹² cm⁻² | Comprobación de la tabla A-2 |
| (30 + 30 + 60) rad/s × 1000 s | 120 krad | Dosis acumulada del ensayo |

## Discrepancias conservadas

- **[S02](04_fuentes.md#s02), tabla A-2:** imprime 4,8 × 10¹³ en la última fluencia; suma de flujos, tabla A-3 y texto A-6 corresponden a 4,8 × 10¹². Se cotejó visualmente el original. No confundir error del documento con OCR.
- **FAQ frente a historia técnica:** [S05](04_fuentes.md#s05) informa 8198 palabras FDS y [S04](04_fuentes.md#s04) aproximadamente 8K. No se sustituyó silenciosamente una cifra. La conversión de 80 µs a instrucciones/s de la FAQ también resulta inconsistente; no se utiliza.
- **Previsiones frente a estado:** los apagados previstos en [S13](04_fuentes.md#s13)/S16 no son automáticamente hechos ocurridos. Se priorizan [S07](04_fuentes.md#s07) y el comunicado de agosto de 2026 para el estado consignado.
- **Duración inicial:** algunas notas describen cuatro años hasta Saturno y la ficha histórica resume cinco años. No se usa ese redondeo como límite garantizado de resistencia de componentes ni como vida útil diseñada de toda pieza.
- **Posición:** cifras fechadas de distancia terrestre no se presentan como distancia heliocéntrica ni como efeméride exacta del día de consulta.
- **Causalidad:** el bit alterado de 2010 y el chip averiado de 2024 no prueban por sí solos una partícula causante. El daño documentado del CRS sí aporta evidencia radiativa, con reservas sobre el mecanismo propuesto.

## Comprobaciones de material

Se conservaron 36 registros con archivo local: 33 descargas originales y tres copias de texto recuperado por la herramienta web. Estas tres páginas JPL devolvieron HTTP 403 en la descarga directa; no se presentan como HTML original. El catálogo registra esa diferencia y las huellas SHA-256. Las copias HTML no incluyen todos sus recursos remotos.

Se revisaron visualmente el mapa propio y las páginas técnicas empleadas para curvas MOS, prueba óptica, pasivos y la inconsistencia de fluencia. Los escaneos históricos tienen calidad limitada; las transcripciones automáticas son auxiliares. Las figuras son material de investigación, no diapositivas listas para proyectar.

## Preguntas que permanecen abiertas

Faltan el conjunto completo de esquemas y listas de materiales por unidad, tecnologías y geometrías por lote de vuelo, dosis acumulada por ubicación hasta 2026 y ensayos específicos de varios magnéticos, relés, soldaduras y recubrimientos. También faltan diagnósticos concluyentes de causa física para ciertas averías. Estas limitaciones están explícitas en el dossier y no impiden explicar los mecanismos generales ni las mitigaciones efectivamente documentadas.

## Revisión de profundidad y efectos transitorios

La ampliación distingue perturbación transitoria, estado persistente recuperable y degradación/daño, sin hacerlas equivalentes a mecanismos físicos. Incluye trece explicaciones «Cómo explicarlo en clase», además de regiones y ecuaciones opcionales. El balance del BJT indica las condiciones mantenidas; la explicación MOS distingue el término de óxido de los estados de interfaz y diferencia NMOS/PMOS. Se evita atribuir pares electrón–hueco como única explicación de todo componente.

Se verificó en [S04](04_fuentes.md#s04), p. 182, la evolución del prototipo TTL hacia procesador y memorias CMOS; [S01](04_fuentes.md#s01) §VI.B identifica 28 funciones CMOS usadas. No se asigna una tecnología universal a todas las computadoras ni se confirma MOSFET de potencia de vuelo. El esquema de amplificador–comparador–registro–carga es conceptual.

Nuevos cálculos comprobables: 10 mA/100 = 0,1 mA; 10 mA/50 = 0,2 mA (región activa). 1 pC/10 pF = 0,1 V; 100 kΩ × 10 pF = 1 µs; tiempo sobre un umbral 50 mV por encima del punto inicial: 1 µs × ln(0,1/0,05) ≈ 0,693 µs. El pulso es supuesto instantáneo respecto de RC, sin realimentación ni carga adicional; la captura no está garantizada.

El plan recibido sumaba 18:45, no 18:00. El esquema curado deja 17:30 de contenido y 0:30 para bibliografía/respaldo: 18:00 más 2:00 de margen. La comprobación automática de palabras es orientativa; la duración final requiere ensayo oral con pausas y figuras. No se afirma haber realizado ese ensayo.

Se añadieron [S35](04_fuentes.md#s35) (NASA/GSFC, 24/10/2005) y [S36](04_fuentes.md#s36) (JPL Publication 12-20, diciembre de 2012 según portada), descargados con texto extraído. Total actualizado: **36 fuentes, 33 originales descargados y tres copias de lectura web**. Las dos fuentes nuevas son generales, no hardware específico de Voyager.

Comprobación final: 36 archivos catalogados con SHA-256 coincidente, sin enlaces locales rotos, trece explicaciones para clase. Las notas orales revisadas suman aproximadamente 1478 palabras: 11.8 minutos a 125 palabras/minuto. El presupuesto restante contempla señalar figuras, pausas, transiciones y bibliografía. Es una estimación, no un ensayo cronometrado. Se revisaron visualmente las figuras nuevas; se corrigieron símbolos que la fuente tipográfica no representaba.


## Revisión editorial y física del 14 de octubre

Se integraron las explicaciones añadidas con las fichas iniciales, eliminando aproximadamente mil palabras de repeticiones antes de añadir ayudas de lectura. Se preservaron las trece familias, resultados de ensayos, explicaciones para clase y referencias. Se unificó el ejemplo de ganancia BJT a 100→50, sin mezclarlo con otro ejemplo 100→20.

Se corrigió la temporización capacitiva: una fuga puede adelantar, retrasar o impedir un cruce según topología y sentido del umbral. Se retiró la expresión que identificaba los B11B ensayados como necesariamente de vuelo. Se añadió la distinción entre mecanismo posible y frecuencia de ocurrencia en el ambiente real. El guion utiliza resultados separados por barras, evitando flechas que parecían indicar evolución obligatoria de pulso a daño.

Verificación posterior: enlaces locales y anclas de fuentes válidos; integridad SHA-256 de los 36 archivos conservada; trece familias y trece explicaciones para clase. No se agregaron fuentes ni se alteraron originales descargados.
