from pathlib import Path
import json,re
import pypdfium2 as pdf
root=Path.cwd(); out=root/'.build_slides/assets'
cat=json.loads((root/'citas/catalogo.json').read_text()); by={x['id']:x for x in cat}
# Render only the figure region from original PDF pages. Fractions use top-left coordinates.
for name,sid,page,box in [('mos','S01',83,(.30,.105,.77,.70)),('bjt','S01',101,(.22,.115,.84,.54)),('set','S35',4,(.19,.14,.81,.47))]:
 doc=pdf.PdfDocument(root/'citas'/by[sid]['archivo']);p=doc[page-1];w,h=p.get_size();l,t,r,b=box
 p.render(scale=3,crop=(w*l,h*(1-b),w*(1-r),h*t)).to_pil().save(out/f'{name}.png')
guion=(root/'investigacion/03_sintesis_20min.md').read_text();notes=[]
for i in range(1,12):
 block=re.search(r'## '+str(i)+r' .*?(?=\n## |\Z)',guion,re.S).group()
 oral=block.split('**Notas orales:**')[1].split('**Transición')[0].strip()
 ids=list(dict.fromkeys(re.findall(r'\bS\d{2}\b',block)))
 refs='\n'.join(f"{sid} — {by[sid]['titulo']}\n{by[sid]['url']}" for sid in ids)
 notes.append(oral+'\n\nFUENTES Y LOCALIZADORES\n'+block.split('**Fuentes:**')[1].strip()+'\n'+refs)
(root/'.build_slides/notes.json').write_text(json.dumps(notes,ensure_ascii=False))
