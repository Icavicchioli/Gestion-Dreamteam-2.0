# Verificación del modelo financiero

Fecha: 22/10/2026. Archivo verificado: `Flujo-de-caja-agrupado-VAN-TIR-corregido.xlsx`.

## Controles estructurales

- Dotación: 4 FTE × 12 meses × 160 h/mes = 7.680 horas brutas.
- Año 1 sin ventas ni demostradores.
- Ventas base: 300/800/1.680 kits; demostradores: 7/15/24.
- Canales base: 18/35/56 médicos y 7/15/24 clínicas.
- Costo directo por kit: USD 102,46; logística e importación: USD 69,06.
- Preserie del año 1: costo directo USD 87,20 y logística/importación USD 64,03 por kit bruto, sin duplicar la mano de obra cubierta por los cuatro FTE.
- Carga de importación: `CIF × 45%`; no se usa un multiplicador general `1,50`.
- Presupuesto y capital mínimo base: USD 228.303,06.
- VAN base al 20%: USD 103.250,74; TIR anual base: 36,83%.
- La hoja `Cambios realizados` documenta de forma compacta los ajustes y remite a la evidencia dentro del libro.

## Pruebas de escenarios y supuestos

| Prueba | Ventas A2/A3/A4 | Capital mínimo USD | VAN USD | TIR | Errores de fórmula |
|---|---:|---:|---:|---:|---:|
| Conservador | 72/193/400 | 277.731,19 | -223.190,04 | No determinada | 0 |
| Base | 300/800/1.680 | 228.303,06 | 103.250,74 | 36,83% | 0 |
| Expansivo | 800/2.633/6.000 | 228.303,06 | 1.130.368,76 | 125,54% | 0 |
| Ventas nulas | 0/0/0 | 646.278,06 | -439.521,40 | No determinada | 0 |
| Demora: año 2 sin ventas | 0/800/1.680 | 312.303,06 | 1.561,25 | 20,24% | 0 |
| Merma del 20% | 300/800/1.680 | 230.403,44 | -12.611,36 | 17,68% | 0 |
| Cargo proveedor + USD 25/kit | 300/800/1.680 | 231.080,83 | 58.364,08 | 29,84% | 0 |
| Retención mensual del 85% | 300/800/1.680 | 228.303,06 | -18.477,62 | 16,48% | 0 |

La prueba se ejecutó en memoria y luego se restauró el escenario base. El escaneo final no encontró `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`, `#NUM!`, `#NULL!`, `#SPILL!` ni `#CALC!`.
