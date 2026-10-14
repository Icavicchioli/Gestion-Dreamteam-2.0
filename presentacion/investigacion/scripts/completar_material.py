from pathlib import Path
import json, hashlib, re, html
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[2]
citas = root / 'citas'
out = root / 'investigacion'
catalogo = json.loads((citas / 'catalogo.json').read_text())
loc = {
'S01':'Stanley, Martin y Price; JPL 77-41. §II y tabla 2-1: p. 2-2 / PDF 26. Tabla 3-1: p. 3-6 / PDF 34. CMOS: pp. 6-1–6-3 / PDF 81–83, figura 6-1. Pasivos: p. 7-53 / PDF 151. Circuito óptico de ensayo: figura 7-6, PDF 152. Cristales: p. 8-41 / PDF 202.',
'S02':'Apéndice A, pp. A-1–A-6 / PDF 9–14; tablas A-1, A-2 y A-3. Apéndice E: irradiación y recocido de selección. La tabla A-2 contiene una inconsistencia de exponente, discutida en el dossier.',
'S03':'Potencia: pp. 15–17 / PDF 18–20. AACS: p. 20 / PDF 23. RF: p. 9 / PDF 12. Documento histórico, no inventario del estado de 2026.',
'S04':'James E. Tomayko, NASA SP-2000. Capítulo 6, pp. 178–184 / PDF 183–189. Recuadros 6-1 y 6-2, figura 6-2. Distinguir prototipo TTL de diseño CMOS.',
'S05':'Preguntas sobre computadoras, memoria y velocidad. Conservar discrepancia 8198 frente a 8K; no usar la conversión inconsistente de 80 µs.',
'S06':'Sección History: lanzamientos y encuentros. La página contiene información histórica; no usar sus secciones antiguas como estado actual.',
'S07':'Tabla Instrument Status y aviso del futuro hito de un día luz. Consultada al corte; la tabla de distancias dinámicas no se recuperó como efeméride estática.',
'S08':'F. L. Scarf y D. A. Gurnett, Space Science Reviews 21 (1977), 289–308; reproducción en NASA PDS. §5.C construcción; §5.E radiación; §5.G potencial de antena y equipotencialidad. Figuras del instrumento: ver vínculos en HTML; la copia local del HTML no incluye automáticamente imágenes remotas.',
'S09':'Apartados de daño por Júpiter y calibración con calentadores apagados. Distinguir daño observado de hipótesis de implantación O/S.',
'S10':'Cronología de mayo de 2010, lectura de memoria, bit alterado y verificación. Complementar con actualizaciones fechadas de S34.',
'S11':'Párrafos sobre 3 % de memoria y posible chip; causas propuestas: partícula energética o desgaste. Diagnóstico preliminar del 4 de abril.',
'S12':'Párrafos sobre chip averiado y redistribución de código; recuperación de telemetría de ingeniería en abril de 2024.',
'S13':'Sección Power to the Probes: potencia reservada para protección y menor regulación. Sus previsiones de apagados no sustituyen noticias posteriores.',
'S14':'Apagado LECP de Voyager 1 del 17 de abril de 2026, MAG/PWS y distancia publicada en esa fecha.',
'S15':'Reconfiguración energética de Voyager 2 y continuidad de tres instrumentos; distinguir lo realizado de lo previsto para Voyager 1.',
'S16':'Apagados de 2025 y distancias fechadas. Planes para 2026 revisados posteriormente por S15.',
'S17':'Introducción, composición y origen de rayos cósmicos; contexto general, no dosimetría Voyager.',
'S18':'Diferencia entre tasas y flujos corregidos térmicamente; acceso a datos CRS.',
'S19':'Unidades de intensidad diferencial y notas de corrección; formulario interactivo no reproducido por el HTML local.',
'S20':'Encabezado y última fila del archivo descargado: 2026-10-04 06:00 UTC, 2,369 cuentas/s y ERROR 0,0257. Archivo congelado para que una actualización web no cambie el dato citado.',
'S21':'Kenneth A. LaBel, NASA GSFC. PDF p. 9 LET; pp. 14–24 clasificación y mecanismos; glosario pp. 59–60. Fuente general, no calificación de Voyager.',
'S22':'Design for Radiation Tolerance: ionización, carga atrapada, interfaces y condiciones de evaluación. Guía histórica; no catálogo de tecnologías actuales.',
'S23':'Apéndice de física de efectos radiativos en microelectrónica, complemento de S22.',
'S24':'J. Wyrwas y E. Wilcox, NASA NEPP. PDF pp. 47–50: tendencias con reservas; p. 49: capacitores cerámicos y conductividad inducida.',
'S25':'NASA-HDBK-4002B. §§4.1.2–4.1.5, PDF pp. 30–32: carga interna, dieléctricos y metales flotantes. Tabla 5, pp. 87–88: ejemplos históricos. Guía general posterior, no prueba de cada práctica Voyager.',
'S26':'Volumen 4. §10.2.6.5 p. 10-22 / PDF 72: magnetismo y aislamiento. §8.6.8 pp. 8-23–8-24: cuarzo.',
'S27':'Estudio previo del Grand Tour, no informe de construcción final Voyager. pp. 156–157 / PDF 165–166: pasivos y activos.',
'S28':'Sensitive Volumes: generación de pares en silicio y ponderación por colección. Fuente técnica primaria de Vanderbilt; excepción explícita a NASA/JPL.',
'S29':'Cruces de heliopausa de ambas sondas y cambio de poblaciones observadas.',
'S30':'Descripción CRS: telescopios, aceptación y respuesta. Para interpretar mediciones, no inferir dosis dentro de chips.',
'S31':'Explicación NASA de preparación de naves para radiación; contexto y lectura inicial.',
'S32':'Documentación de Horizons API. Consultada para explorar efemérides; no se obtuvo una solución numérica utilizable y no se cita una distancia calculada con ella.',
'S33':'PGH Rate: umbral del canal y promedios de seis horas, complemento de S20.',
'S34':'Actualizaciones del 17, 20 y 24 de mayo de 2010: identificación 0→1, corrección y regreso de datos científicos.'}

for s in catalogo:
    if s['id'] in ['S12','S13','S34']:
        p = citas / (s['id']+'_lectura_web.txt')
        s.setdefault('archivo_original_solicitado', s['archivo'])
        s['archivo'] = p.name
        s['estado'] = 'copia_textual_web; HTML original rechazó descarga HTTP 403'
        s['consulta'] = '2026-10-14'
        s['sha256'] = hashlib.sha256(p.read_bytes()).hexdigest()
        s['bytes'] = p.stat().st_size
        s.pop('error', None)
(citas/'catalogo.json').write_text(json.dumps(catalogo,ensure_ascii=False,indent=2)+'\n')

bib = ['# Fuentes y figuras\n','Consulta: 14 de octubre de 2026. Las páginas PDF se cuentan desde 1 e incluyen portada; se indica además la página impresa cuando difiere. El catálogo conserva URL, fecha de consulta, tamaño y SHA-256.\n','Se priorizan documentos originales NASA/JPL/GSFC, NTRS, PDS y NEPP. S28 es la excepción técnica de Vanderbilt. Los manuales generales explican física; no demuestran instalación ni práctica de vuelo. S32 es material consultado auxiliar.\n']
idx = ['# Copias de las fuentes consultadas\n','**34 registros:** 31 originales descargados (PDF, HTML o datos TXT) y 3 copias de lectura web de páginas JPL cuya descarga directa devolvió HTTP 403. Estas últimas no son el HTML original.\n','Para empezar: **S01** (ensayos de componentes), **S02** (procedimientos), **S08** (PWS), **S21** (física) y **S09** (daño real). Los números de página y secciones están en [la bibliografía](../investigacion/04_fuentes.md).\n','Los HTML son copias del documento, no sitios completos sin conexión: imágenes, estilos o elementos interactivos pueden depender del sitio original. Los TXT extraídos de PDF contienen errores de OCR posibles; consultar el PDF para números y símbolos.\n','| ID | Fuente | Archivo local | Texto |\n|---|---|---|---|']
for s in catalogo:
    p=citas/s['archivo']
    txt=p.with_suffix('.txt')
    textlink=f'[Texto]({txt.name})' if txt.exists() else '—'
    idx.append(f"| {s['id']} | {s['titulo']} | [Abrir]({p.name}) | {textlink} |")
    bib.extend([f"\n<a id=\"{s['id'].lower()}\"></a>\n\n## {s['id']} — {s['titulo']}\n",f"Fecha: {s['fecha']}. [Original en línea]({s['url']}) · [Copia local](../citas/{p.name}). Estado: {s['estado']}.\n",loc[s['id']]+'\n'])
bib.append('''
## Figuras incluidas y procedencia

- **Mapa de componentes:** elaboración propia, síntesis de S01, S21, S24–S27 y el dossier. No reproduce un plano de vuelo. PNG y SVG en `figuras/`.
- **S01, PDF 26:** tabla 2-1, ambiente previo al vuelo. Sirve para discutir umbrales y equivalencias, no para asignar dosis actual.
- **S01, PDF 34:** tabla 3-1, requisitos de blindaje por localización. Relacionar con margen de diseño.
- **S01, PDF 83:** figura 6-1, curvas MOS antes y después de irradiación. Observar desplazamiento bajo las condiciones indicadas en el original.
- **S01, PDF 151:** resultados de diodos, capacitores y redes resistivas. Los valores son del ensayo descrito, no una garantía universal.
- **S01, PDF 152:** figura 7-6, montaje de ensayo óptico. Identifica alimentación y resistencias de un banco de prueba; no es una placa Voyager.
- **S02, PDF 13:** tabla A-2, secuencia de irradiación. El exponente de fluencia final discrepa del cálculo y de A-3.

Las páginas son reproducciones renderizadas de los PDF NASA/JPL, sin reconstruir ni alterar curvas o cifras. Las imágenes remotas enlazadas por otros HTML no se incluyen salvo indicación expresa.

![Curvas MOS originales, figura 6-1](figuras/voyager_radiacion_vol1_1977_p083.png)

**Figura de respaldo A.** S01, p. 6-3. Leer condiciones y ejes en la página: un corrimiento de característica modifica el margen eléctrico del circuito.

![Resultados de componentes pasivos y diodos](figuras/voyager_radiacion_vol1_1977_p151.png)

**Figura de respaldo B.** S01, p. 7-53. Permite verificar los valores de capacitancia usados en el cálculo y las familias de resistencias ensayadas.

![Circuito óptico de ensayo](figuras/voyager_radiacion_vol1_1977_p152.png)

**Figura de respaldo C.** S01, p. 7-54. Ejemplo real de prueba que integra componentes discretos; no presentarlo como esquema de vuelo.
''')
(out/'04_fuentes.md').write_text('\n'.join(bib))
(citas/'README.md').write_text('\n'.join(idx)+'\n\n[Catálogo con fechas y huellas de integridad](catalogo.json).\n')

# Diagrama propio: vector y raster generados a partir del mismo contenido.
W,H=1800,1200
im=Image.new('RGB',(W,H),'#f4f6f8'); d=ImageDraw.Draw(im)
fontpath='/System/Library/Fonts/Supplemental/Arial.ttf'
font=lambda n:ImageFont.truetype(fontpath,n)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="1800" height="1200" fill="#f4f6f8"/>']
def text(x,y,t,n=27,color='#152f46'):
    d.text((x,y),t,font=font(n),fill=color)
    svg.append(f'<text x="{x}" y="{y+n}" font-family="Arial, sans-serif" font-size="{n}" fill="{color}">{html.escape(t)}</text>')
text(65,40,'Radiación: del material al circuito',52)
text(65,112,'Mapa conceptual • no es un esquema de vuelo de Voyager',28)
text(65,175,'Ambiente → interacción física → parámetro eléctrico → función del circuito',32)
cards=[
('R / C','Resistencias y capacitores',['R, aislamiento, C y fugas','Polarización, filtros, retención','Voyager: ensayos de pasivos','PWS: descarga de antena'], 'S01 p. 7-53; S08 §5.G'),
('L / T','Inductores y transformadores',['Bobinado, núcleo y aislantes','Pérdidas, aislamiento, rizado','Calificar materiales y márgenes','Materiales Voyager: no resueltos'],'S26 §10.2.6.5; S03'),
('D / Q','Diodos y transistores',['Unión, red y óxido de control','Fuga, ganancia y umbral','Selección y margen eléctrico','Voyager: ensayos y proceso CMOS'],'S01 §§VI–VII; S21–23'),
('IC','Analógico, lógica y memoria',['Offset, tiempos y estado lógico','TID, desplazamiento y SEE','Blindaje y respuesta del sistema','Voyager: retención / recuperación'],'S01; S04; S10–12'),
('PCB','Placa e interconexiones',['Pistas, soldaduras, relés, contactos','Carga, aislamiento y descargas','Retornos y equipotencialidad','Distinguir radiación de fatiga'],'S25 §§4.1.3–5; S08 §5.G'),
('SENS','Detectores, óptica y cuarzo',['Colección, emisión y frecuencia','Respuesta, señal y temporización','Calibración y selección de lotes','Voyager: daño CRS / ensayo cuarzo'],'S09; S01 §VIII.F; S26')]
for i,(tag,title,lines,source) in enumerate(cards):
    x=65+(i%3)*565; y=255+(i//3)*390
    d.rounded_rectangle((x,y,x+540,y+355),radius=16,fill='white',outline='#bfd0dc',width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="540" height="355" rx="16" fill="white" stroke="#bfd0dc" stroke-width="2"/>')
    text(x+24,y+20,tag,36,'#126c81'); text(x+24,y+78,title,29)
    for k,line in enumerate(lines):text(x+24,y+132+k*40,line,25)
    text(x+24,y+307,source,21,'#526676')
text(65,1065,'La mitigación documentada en Voyager se distingue del criterio general.',29)
text(65,1120,'Fuentes completas y límites: dossier y matriz de evidencias • 14/10/2026',25)
svg.append('</svg>')
(out/'figuras/01_mapa_componentes.svg').write_text('\n'.join(svg))
im.save(out/'figuras/01_mapa_componentes.png')

# Enlaces navegables en referencias del dossier y matriz, sin alterar números.
for name in ['01_dossier.md','02_matriz_evidencias.md','03_sintesis_20min.md']:
    p=out/name
    s=p.read_text()
    s=re.sub(r'(?<![\w/])(S\d{2})(?![\w]|\]\()',lambda m:f'[{m[1]}](04_fuentes.md#{m[1].lower()})',s)
    p.write_text(s)
print('Bibliografía, índice de citas, referencias y mapa generados.')
