# Matriz de trazabilidad de correcciones

Fecha de cierre: 22/10/2026. Fuentes: informe comentado por el docente, correcciones tomadas en clase, LaTeX vigente y flujo de fondos original.

## Comentarios embebidos del PDF

| ID | Página | Observación del docente | Corrección implementada | Evidencia |
|---|---:|---|---|---|
| PDF-01 | 18 | Las fortalezas eran características o beneficios del producto, no del proyecto. | Se reemplazaron por capacidades internas del proyecto: dotación full-time con roles definidos, integración multidisciplinaria, gestión trazable y modelo operativo-financiero conectado. Se eliminaron modularidad y reutilización de la lista de fortalezas. | `Evaluacion del proyecto.tex`, Análisis FODA. |
| PDF-02 | 19 | Debilidades demasiado extensas/redundantes. | Se consolidaron en dos debilidades no redundantes: capacidades/infraestructura y desempeño no demostrado. | `Evaluacion del proyecto.tex`, Análisis FODA. |
| PDF-03 | 19 | Cuestionamiento de “mercado no atendido”. | Se eliminó esa afirmación y se declaró que no se sostendrá sin evidencia específica. | `Evaluacion del proyecto.tex`, introducción del FODA. |
| PDF-04 | 20 | La complejidad de uso no corresponde como debilidad. | Se retiró de debilidades y se mantuvo como riesgo de adopción R7. | FODA y matriz de riesgos. |
| PDF-05 | 20 | Integración/calibración es riesgo, no amenaza. | Se eliminó de amenazas y quedó en R1 con mitigación y pruebas. | Riesgo R1 y plan de pruebas. |
| PDF-06 | 20 | Amenazas debían redactarse con mayor claridad. | Se simplificaron a datos, competencia, regulación, adopción y dependencias externas. | FODA, amenazas. |
| PDF-07 | 21 | Revisar ponderación de riesgos. | Se incorporó una rúbrica común 1–10 con bandas y revisión en hitos. | Análisis de riesgos. |
| PDF-08 | 28 | Autonomía prevista para la batería. | Se definieron baterías mínimas de 750/850 mAh, consumos medios máximos de 3,5/4,0 mA, reserva de 20% y autonomía teórica de 7,1 días. | Dimensionamiento preliminar de memoria y energía. |
| PDF-09 | 28 | Explicar cómo se estimó “armado final, programación y prueba”. | Se desagregaron tareas: lector 10+4+8+3 = 25 min y USD 6,08; pulsera 8+4+6+3 = 21 min y USD 5,10; parche 20 h/100 unidades = USD 4,08. Se identificaron como estimaciones internas, no cotizaciones. En la preserie del año 1 se excluyen del costo porque ya están cubiertas por los cuatro FTE; desde el año 2 integran el costo variable. | `Evaluacion del proyecto.tex`, costos de lector/pulsera/parche; `Flujo de caja`, bloques “Costos unitarios trazables” y “Preserie año 1 sin doble mano de obra”. |
| PDF-10 | 29 | Cuestionamiento del 50%. | Se eliminó el multiplicador general 1,50. Quedaron separados costo directo, mano de obra, merma por unidades brutas, importación `CIF × 45%`, logística y reserva técnica del 10% solo sobre partidas de desarrollo/ensayo. | `Evaluacion del proyecto.tex`; fórmulas de costos unitarios y recambios en `Flujo de caja`. |
| PDF-11 | 31 | Las 1.340 horas no parecían razonables. | Se reemplazaron por cuatro FTE durante doce meses. | Tabla de dotación y hoja `Plan 12 meses`. |
| PDF-12 | 31 | Conciliar esfuerzo con plan de trabajo. | Capacidad derivada: 7.680 horas brutas; nómina, Gantt y flujo usan la misma dotación. | Planificación y flujo de caja. |
| PDF-13 | 33 | Se inferían solo 4–5 meses de desarrollo. | El cronograma ahora cubre doce meses completos y 26 sprints. | Tabla de Gantt resumido y hoja `Plan 12 meses`. |
| PDF-14 | 33 | Parecía una dedicación menor a 1,5 personas. | Se explicitó la dedicación full-time de cuatro personas y sus roles. | Organización del proyecto y nómina. |
| PDF-15 | 34 | Totalizar el año 1. | La columna Año 1 suma flujos/costos y usa cierre/promedio según el indicador. | `Flujo de caja`, columna O. |
| PDF-16 | 34 | Revisar el flujo en detalle. | Se rehízo el modelo con costos, escenarios, inventario, merma, ventas, soporte, VAN/TIR y controles. La preserie quedó separada del costo de explotación para impedir el doble pago de la mano de obra incluida en los cuatro FTE. | Libro corregido, bloque de preserie y escaneo sin errores de fórmula. |
| PDF-17 | 37 | Planificar MVP/producto; prototipo solo como entregable intermedio. | Prototipo integrado en mes 7, candidato a MVP en mes 10 y MVP aceptado en mes 12. | Definición, plan de producto y Gantt. |

## Observaciones sustantivas tomadas en clase

| ID | Observación | Corrección implementada | Evidencia |
|---|---|---|---|
| TXT-01 | Un año y cuatro personas full-time. | Doce meses, dos perfiles de ingeniería y dos técnicos/administrativos. | LaTeX y flujo. |
| TXT-02 | Gantt/agilidad para el primer año y tareas de explotación posteriores. | Metodología híbrida y 26 sprints en el año 1; Kanban comercial/operativo y metas trimestrales en los años 2–4. | Hoja `Plan 12 meses` y planificación. |
| TXT-03 | Incluir compras, proveedores, importación, aduana y recepción. | Frente de abastecimiento con responsables, dependencias y costos. | Gantt, inventario técnico y flujo. |
| TXT-04 | Prototipo, batería, electrónica, robustez y pruebas obligatorias. | Hitos de subsistemas, prototipo integrado y pruebas funcionales/técnicas con criterios de cierre. | Gantt y plan de pruebas. |
| TXT-05 | Servicios generales de USD 500 y alquiler de equipamiento. | USD 500/mes de servicios y USD 1.000/mes de laboratorio/equipamiento. | Flujo, filas 14–15. |
| TXT-06 | No forzar TIR/VAN. | Se informan las salidas recalculadas sin aumentar ventas: base VAN USD 103.250,74/TIR 36,83%; conservador VAN USD -223.190,04/TIR no determinada. | Resumen financiero y verificación de escenarios. |
| TXT-07 | Vendedores desde el inicio de ventas y costos comerciales. | Equipo comercial fijo desde año 2, difusión y 8% variable sobre ventas. | Flujo y plan comercial. |
| TXT-08 | Año 1 totalizado. | Sumas mensuales y controles; inventario/caja a cierre. | Columna O y control fila 56. |
| TXT-09 | Ventas vinculadas a especialistas y no excesivamente austeras. | Se conservaron 300/800/1.680 kits y se dividió el canal en 18/35/56 médicos y 7/15/24 clínicas, con prospectos y conversión del 20%. | Hoja `Plan comercial` e informe. |
| TXT-10 | Costos asociados a cantidades vendidas y pérdidas. | Producción, importación, merma, inventario, comisiones, recambios, demostradores, onboarding, logística y soporte dependen del volumen y del escenario. | Flujo y supuestos. |
| TXT-11 | Consultas legales, médicas y administrativas. | Se desagregaron USD 10.000: médicas 3.000, legales 2.500, regulatorias 3.500 y contables/impositivas 1.000; bioquímica permanece separada en USD 12.000. | Flujo y recursos. |
| TXT-12 | Insistir en batería, memoria y tiempos. | Cálculos, márgenes y protocolos de prueba explícitos. | Diseño técnico. |

## Controles de cierre

- La auditoría final encontró evidencia para los 17 comentarios embebidos del PDF y las 12 observaciones sustantivas del TXT.
- Cuatro FTE por doce meses concilian con USD 134.400 de nómina y 7.680 horas brutas.
- Año 1 no contiene ventas ni demostradores y totaliza USD 228.303,06 de egresos.
- La preserie usa USD 87,20 de costo directo y USD 64,03 de logística/importación por kit bruto; no vuelve a pagar la mano de obra cubierta por los cuatro FTE.
- Capital mínimo base: USD 228.303,06; VAN al 20%: USD 103.250,74; TIR anual: 36,83%.
- El escenario base comercial produce 300, 800 y 1.680 kits en años 2–4.
- Los demostradores 7/15/24 y el onboarding USD 3.450/7.125/11.400 responden al escenario y están conectados a producción/costos.
- La hoja `Cambios realizados` resume en forma compacta los ajustes, resultados y ubicación de la evidencia; `Flujo de caja` permanece como fuente financiera autoritativa.
- No se detectaron `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`, `#NUM!`, `#NULL!`, `#SPILL!` ni `#CALC!`.
- Se probaron escenarios conservador/base/expansivo, ventas nulas, demora del lanzamiento, merma del 20%, mayor costo y retención del 85%; los resultados están en `Verificacion-modelo-financiero.md`.
- Prototipo, candidato a MVP, aceptación funcional/técnica, validación clínica y certificación comercial quedan conceptualmente separados.
- El informe se regeneró desde LaTeX sin errores de compilación ni referencias indefinidas; las 24 consignas originales de la plantilla se conservaron visibles.
