from pathlib import Path
import json, shutil, hashlib
from PIL import Image
B=Path(__file__).resolve().parent
ROOT=B.parents[1]; OUT=ROOT/'versión 3 basada en JPL 77-41'
assets=json.loads((B/'imagenes.json').read_text())
# Extract unchanged figure regions from rendered source pages, preserving axes and labels.
crops={83:(410,180,1035,1265),101:(300,200,1125,975),112:(275,205,1080,925),155:(275,205,1190,855),201:(295,195,970,1260)}
for a in assets:
 if 'page' in a:
  p=a['page']; im=Image.open(B/'originales'/f'p{p}.png')
  if p in crops:im=im.crop(crops[p]);a['scope']+=' Recorte de figura conservando ejes, rótulos y pie original.'
  im.save(OUT/'imagenes'/a['name'])
 a['sha256']=hashlib.sha256((OUT/'imagenes'/a['name']).read_bytes()).hexdigest()
(B/'imagenes.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2))
slides=json.loads((B/'contenido.json').read_text());sources=json.loads((B/'fuentes.json').read_text())
idx=['# Imágenes, fuentes y guía de lectura\n\nLa fuente técnica central es el volumen I del informe JPL 77-41. Las figuras extraídas conservan su contenido original. Las imágenes históricas complementan el contexto.\n\n## Correspondencia con el informe\n\n| Diapositiva y capítulo | Pasaje principal |\n|---|---|\n']
for s in slides:idx.append(f"| {s['n']:02}. {s['title']} | {s['loc']} |\n")
idx.append('\n## Fuentes utilizadas\n\n')
for r in sources:idx.append(f"**{r['id']}. [{r['titulo']}]({r['url']})**\n\n{r['detalle']}\n\n")
idx.append('El informe central se incluye en `fuentes/JPL_77-41_Volumen_I.pdf`. Su SHA-256 es `'+hashlib.sha256((OUT/'fuentes/JPL_77-41_Volumen_I.pdf').read_bytes()).hexdigest()+'`.\n\n## Catálogo de imágenes\n\n')
for a in assets:
 idx.append(f"### {a['name']}\n\nDiapositivas: {a['slides']}.\n\nProcedencia: {a['credit']}. [Fuente]({a['url']}).\n\nArchivo de origen: `{a['origin']}`.\n\nAlcance: {a['scope']}\n\nSHA-256 de la copia: `{a['sha256']}`.\n\n")
idx.append('''## Recursos que no es necesario inventar

El esquema y el PowerPoint usan texto y tablas editables para los conceptos que no necesitan fotografía. Para agregar una foto de placa, buscar «Voyager Flight Data Subsystem JPL 360-751AC»; se incluye `contexto_fds.png` procedente de la historia NASA y debe conservar su identificación. No identifica por sí sola el número de serie que voló.

La ilustración `contexto_heliosfera.jpg` queda como recurso opcional para la historia. Su frontera no debe rotularse como fin de la gravedad solar. Para los inductores o capacitores de vuelo no se encontró en este volumen una fotografía y lista de materiales que permita identificar todas las piezas; los circuitos de ensayo se rotulan como tales.

## Cómo seguir el documento original

Las páginas 25-28 del PDF definen el ambiente. Las 29-36 explican las decisiones y el margen. Las 50-60 desarrollan screening. Las 81-85 presentan hardening CMOS y lineal; las tablas posteriores completan esa sección. Los resultados por familia comienzan en la 99. El screening por familia comienza en la 162. Las conclusiones están en 204-208.

El capítulo V describe instalaciones, dosimetría y procedimientos; se conserva solo el contexto necesario para interpretar resultados. Las tablas extensas quedan en el original: el dossier selecciona casos y conserva condiciones, sin convertir promedios o ensayos de un lote en garantías universales.
''')
(OUT/'04_Imagenes_y_fuentes.md').write_text(''.join(idx))
old=B.parent/'revisada2'
pdf=(old/'pdf.py').read_text().replace("OUT=ROOT/'versión 2 revisada'","OUT=ROOT/'versión 3 basada en JPL 77-41'").replace('Versión 2 revisada','Versión 3 · JPL 77-41')
(B/'pdf.py').write_text(pdf)
js=(old/'generar.mjs').read_text().replace('.build_slides/revisada2','.build_slides/revisada3').replace('versión 2 revisada','versión 3 basada en JPL 77-41').replace('[4,5,6,10]','[4,6,8,11]')
(B/'generar.mjs').write_text(js)
link=B/'node_modules'
if not link.exists():link.symlink_to('/Users/i.e.cavicchioli/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules')
print('Figuras y referencias preparadas:',len(assets))
