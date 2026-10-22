# Matriz de trazabilidad de correcciones

Fecha de cierre: 22/10/2026. Fuentes: informe comentado por el docente, correcciones tomadas en clase, LaTeX vigente y flujo de fondos original.

## Comentarios embebidos del PDF

| ID | Página | Observación del docente | Corrección implementada | Evidencia |
|---|---:|---|---|---|
| PDF-01 | 18 | Las fortalezas eran características o beneficios del producto, no del proyecto. | Se reemplazaron por capacidades internas: integración multidisciplinaria, modularidad, trazabilidad y estrategia de reutilización. | `Evaluacion del proyecto.tex`, Análisis FODA. |
| PDF-02 | 19 | Debilidades demasiado extensas/redundantes. | Se consolidaron en dos debilidades no redundantes: capacidades/infraestructura y desempeño no demostrado. | `Evaluacion del proyecto.tex`, Análisis FODA. |
| PDF-03 | 19 | Cuestionamiento de “mercado no atendido”. | Se eliminó esa afirmación y se declaró que no se sostendrá sin evidencia específica. | `Evaluacion del proyecto.tex`, introducción del FODA. |
| PDF-04 | 20 | La complejidad de uso no corresponde como debilidad. | Se retiró de debilidades y se mantuvo como riesgo de adopción R7. | FODA y matriz de riesgos. |
| PDF-05 | 20 | Integración/calibración es riesgo, no amenaza. | Se eliminó de amenazas y quedó en R1 con mitigación y pruebas. | Riesgo R1 y plan de pruebas. |
| PDF-06 | 20 | Amenazas debían redactarse con mayor claridad. | Se simplificaron a datos, competencia, regulación, adopción y dependencias externas. | FODA, amenazas. |
| PDF-07 | 21 | Revisar ponderación de riesgos. | Se incorporó una rúbrica común 1–10 con bandas y revisión en hitos. | Análisis de riesgos. |
| PDF-08 | 28 | Autonomía prevista para la batería. | Se definieron baterías mínimas de 750/850 mAh, consumos medios máximos de 3,5/4,0 mA, reserva de 20% y autonomía teórica de 7,1 días. | Dimensionamiento preliminar de memoria y energía. |
| PDF-09 | 28 | Explicar cómo se estimaron memoria/tiempo. | Se documentó un registro de 64 bytes cada dos minutos: 45 KiB/día, mínimo 128 KiB y prueba de pérdida BLE por 24 h. | Requerimientos y diseño preliminar. |
| PDF-10 | 29 | Cuestionamiento del 50%. | Se separó la carga de baja serie de la merma; la reserva técnica es 10% sobre partidas identificadas y se aplica una sola vez. | Costos y flujo, filas de supuestos. |
| PDF-11 | 31 | Las 1.340 horas no parecían razonables. | Se reemplazaron por cuatro FTE durante doce meses. | Tabla de dotación y hoja `Plan 12 meses`. |
| PDF-12 | 31 | Conciliar esfuerzo con plan de trabajo. | Capacidad derivada: 7.680 horas brutas; nómina, Gantt y flujo usan la misma dotación. | Planificación y flujo de caja. |
| PDF-13 | 33 | Se inferían solo 4–5 meses de desarrollo. | El cronograma ahora cubre doce meses completos y 26 sprints. | Tabla de Gantt resumido y hoja `Plan 12 meses`. |
| PDF-14 | 33 | Parecía una dedicación menor a 1,5 personas. | Se explicitó la dedicación full-time de cuatro personas y sus roles. | Organización del proyecto y nómina. |
| PDF-15 | 34 | Totalizar el año 1. | La columna Año 1 suma flujos/costos y usa cierre/promedio según el indicador. | `Flujo de caja`, columna O. |
| PDF-16 | 34 | Revisar el flujo en detalle. | Se rehízo el modelo con costos, escenarios, inventario, merma, ventas, soporte, VAN/TIR y controles. | Libro corregido y escaneo sin errores de fórmula. |
| PDF-17 | 37 | Planificar MVP/producto; prototipo solo como entregable intermedio. | Prototipo integrado en mes 7, candidato a MVP en mes 10 y MVP aceptado en mes 12. | Definición, plan de producto y Gantt. |

## Observaciones sustantivas tomadas en clase

| ID | Observación | Corrección implementada | Evidencia |
|---|---|---|---|
| TXT-01 | Un año y cuatro personas full-time. | Doce meses, dos perfiles de ingeniería y dos técnicos/administrativos. | LaTeX y flujo. |
| TXT-02 | Gantt/agilidad para el primer año y tareas de explotación posteriores. | Metodología híbrida, 26 sprints y roadmap de años 2–4. | Hoja `Plan 12 meses` y planificación. |
| TXT-03 | Incluir compras, proveedores, importación, aduana y recepción. | Frente de abastecimiento con responsables, dependencias y costos. | Gantt, inventario técnico y flujo. |
| TXT-04 | Prototipo, batería, electrónica, robustez y pruebas obligatorias. | Hitos de subsistemas, prototipo integrado y pruebas funcionales/técnicas con criterios de cierre. | Gantt y plan de pruebas. |
| TXT-05 | Servicios generales de USD 500 y alquiler de equipamiento. | USD 500/mes de servicios y USD 1.000/mes de laboratorio/equipamiento. | Flujo, filas 14–15. |
| TXT-06 | No forzar TIR/VAN. | VAN negativo informado y TIR “No determinada”; no se alteran supuestos. | Resumen financiero. |
| TXT-07 | Vendedores desde el inicio de ventas y costos comerciales. | Equipo comercial fijo desde año 2, difusión y 8% variable sobre ventas. | Flujo y plan comercial. |
| TXT-08 | Año 1 totalizado. | Sumas mensuales y controles; inventario/caja a cierre. | Columna O y control fila 56. |
| TXT-09 | Ventas vinculadas a especialistas y no excesivamente austeras. | Embudo por clínicas/profesionales, pacientes alcanzables y adopción; 300/800/1.680 kits en base. | Hoja `Plan comercial`. |
| TXT-10 | Costos asociados a cantidades vendidas y pérdidas. | Producción, importación, merma, inventario, comisiones, recambios, logística y soporte dependen del volumen. | Flujo y supuestos. |
| TXT-11 | Consultas legales, médicas y administrativas. | USD 10.000 de consultas médicas, legales y regulatorias; roles administrativos incluidos. | Flujo y recursos. |
| TXT-12 | Insistir en batería, memoria y tiempos. | Cálculos, márgenes y protocolos de prueba explícitos. | Diseño técnico. |

## Controles de cierre

- Cuatro FTE por doce meses concilian con USD 134.400 de nómina y 7.680 horas brutas.
- Año 1 no contiene ventas y totaliza USD 238.982,22 de egresos.
- Capital mínimo: USD 300.920,09; VAN al 20%: USD -233.388,97; TIR: no determinada.
- El escenario base comercial produce 300, 800 y 1.680 kits en años 2–4.
- No se detectaron `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`, `#NUM!`, `#NULL!`, `#SPILL!` ni `#CALC!`.
- Prototipo, candidato a MVP, aceptación funcional/técnica, validación clínica y certificación comercial quedan conceptualmente separados.
