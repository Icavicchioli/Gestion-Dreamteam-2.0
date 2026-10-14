# Presentación de Voyager: tercera versión

18 diapositivas principales para 18 minutos, más bibliografía y cuatro respaldos: 23 diapositivas. Autor: Ignacio Cavicchioli. Corte histórico: 14/10/2026.

## Entrega final

- `Voyager_radiacion_final.pptx`: presentación con texto editable, figuras y notas completas.
- `Voyager_radiacion.pdf`: versión para lectura y proyección, con Arial incrustada y texto seleccionable.
- `notas_orales.md`: guion, texto proyectado, explicación de figuras y referencias con localizadores.

## Fuentes y reproducción

El contenido y el generador están en `.build_slides/v3/contenido.json` y `.build_slides/v3/generar.mjs`. El PDF se genera con `exportar_pdf.py` en esa carpeta. Los borradores se conservan aparte; la conversión preliminar de LibreOffice se descartó como entrega porque sustituyó Arial.

Las nuevas fuentes y su procedencia están en `citas/presentacion_v3/`. Los informes anteriores permanecen en `citas/`. Las referencias completas por diapositiva están en las notas.

## Validación

- Las 23 diapositivas y las 23 páginas finales del PDF fueron inspeccionadas visualmente.
- El PPTX final pasó los controles de estructura, geometría, familia Arial e importación por Artifact Tool. Recibo: `.build_slides/v3/validacion_final.json`.
- El PDF utiliza Arial y Arial Bold en todos sus caracteres; tamaño mínimo del texto: 24 puntos. Los rótulos originales dentro de figuras son parte de las imágenes.
- El guion principal contiene 1.878 palabras, con tiempo para explicar las figuras dentro de los 18 minutos asignados.
- Se distinguen hardware de vuelo, ensayos del programa y ejemplos equivalentes.
- No se ha verificado la importación a Google Slides ni la duración mediante ensayo oral.
