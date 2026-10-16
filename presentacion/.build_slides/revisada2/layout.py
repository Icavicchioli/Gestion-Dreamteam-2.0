from pathlib import Path
import json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

B=Path(__file__).parent
pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
D=json.loads((B/'contenido.json').read_text())
INK='#172B3A'; BLUE='#126F87'; GRAY='#49616E'; WHITE='#FFFFFF'
def wrap(s,w,size,bold=False):
    lines=[]
    for para in s.split('\n'):
        line=''
        for word in para.split():
            test=(line+' '+word).strip()
            if pdfmetrics.stringWidth(test,'Arial-Bold' if bold else 'Arial',size*.75)>w*.75 and line:
                lines.append(line);line=word
            else:line=test
        lines.append(line)
    return '\n'.join(lines)
def text(ops,s,x,y,w,size=34,bold=False,color=INK,h=None):
    t=wrap(s,w,size,bold)
    height=h or (len(t.splitlines())*size*1.22+6)
    ops.append(dict(kind='text',text=t,x=x,y=y,w=w,h=height,size=size,bold=bold,color=color))
    return y+height
def picture(ops,f,x,y,w,h):ops.append(dict(kind='image',file=f,x=x,y=y,w=w,h=h))
def table(ops,rows,x,y,w,h,widths,size=31):
    ops.append(dict(kind='table',rows=rows,x=x,y=y,w=w,h=h,widths=widths,size=size))

for s in D:
 n=s['n'];o=[];s['ops']=o
 if n==1:
  text(o,s['title'],64,58,1120,56,True)
  text(o,'Ignacio Cavicchioli',64,235,620,34,False,BLUE)
  text(o,s['screen'],64,330,585,34)
  picture(o,s['image'],720,230,485,365)
  text(o,'1977–2026',64,579,500,32,False,BLUE)
 else:
  text(o,s['title'],64,48,1150,43,True,h=108)
  if n in [3,7,8,12,13,14,18]:
   text(o,s['screen'],64,176,575,34)
   picture(o,s['image'],704,170,510,365)
   text(o,s['caption'],704,551,510,25,False,GRAY)
   extras={3:'Interplanetario → magnetósferas → interestelar',7:'Conductores, dieléctricos y semiconductores',8:'CCS: comandos · AACS: orientación · FDS: datos',12:'LED, fotodiodos y acoplamientos ópticos',13:'A I_C fija: menor β requiere más I_B.',14:'CMOS RCA: recocido de 1100 a 950 °C.',18:'Ensayos, márgenes y recuperación de funciones'}
   text(o,extras[n],64,590,1130,31,False,BLUE)
  elif n==2:
   text(o,s['screen'],64,165,620,32)
   text(o,'Más de 25.000 millones de km: V1.\nMás de 21.000 millones de km: V2.',64,390,630,31,True,BLUE)
   text(o,'Distancias a la Tierra · NASA, 05/03/2025',64,498,630,27,False,GRAY)
   text(o,'Proyecto aprobado en 1972; lanzamientos en 1977.',64,565,1130,31)
   picture(o,s['image'],730,162,470,380)
  elif n==4:
   text(o,s['screen'],64,160,1140,33)
   table(o,[['Fuente','Población relevante'],['Sol','Plasma y partículas energéticas'],['Galaxia','Protones, núcleos y electrones'],['Magnetósferas','Poblaciones atrapadas'],['RTG y calentadores','Neutrones y gamma externos']],64,319,1140,300,[390,750],32)
  elif n==5:
   text(o,s['screen'],64,160,1140,33)
   table(o,[['Radiación','Qué es'],['Protones y otros núcleos','Partículas con carga positiva'],['Electrones / beta','Electrones; beta también positrones'],['Alfa','Núcleos de helio-4'],['Rayos X / gamma','Fotones sin carga'],['Neutrones','Partículas sin carga']],64,288,1140,342,[390,750],30)
  elif n==6:
   text(o,s['screen'],64,160,1140,33)
   table(o,[['Característica','Qué expresa'],['Tipo','Especie de partícula o fotón'],['Energía','Energía incidente: eV, keV, MeV'],['Flujo','Partículas por área y tiempo'],['Dosis','Energía absorbida por masa']],64,310,1140,270,[390,750],31)
   text(o,'Flujo acumulado en el tiempo = fluencia.',64,605,1130,29,False,BLUE)
  elif n==9:
   text(o,s['screen'],64,160,1140,36)
   text(o,'Entrada de antena del PWS',64,355,1140,34,True,BLUE)
   text(o,'4 µA × 20 MΩ = 80 V',64,427,1140,57,True)
   text(o,'Resistencia especificada para 500 V.',64,526,1140,34)
   text(o,'Caso de carga de antena; S08, §5.G.',64,594,1140,26,False,GRAY)
  elif n==10:
   text(o,s['screen'],64,160,1140,36)
   table(o,[['Mismo capacitor: 10 nF','Antes','Con mayor fuga'],['Resistencia de fuga','10 GΩ','1 GΩ'],['Constante de tiempo','100 s','10 s']],64,361,1140,205,[620,250,270],31)
   text(o,'Ejemplo general: C no cambia, la retención sí.',64,597,1140,30,False,BLUE)
  elif n==11:
   text(o,s['screen'],64,160,1140,34)
   text(o,'Mando → bobina → contactos → carga',64,340,1140,42,True,BLUE)
   text(o,'Inductores y transformadores: conductor, núcleo y aislante.\nPistas, soldaduras y conectores: camino de la corriente.\nPlacas y encapsulados: aislamiento y carga retenida.',64,435,1140,30)
  elif n==15:
   text(o,s['screen'],64,160,1140,35)
   text(o,'Carga recogida → pulso → estado alterado',64,355,1140,42,True,BLUE)
   text(o,'El pulso desaparece. El dato puede quedar equivocado.',64,458,1140,34)
   text(o,'Ejemplo conceptual; no identifica una celda de Voyager.',64,585,1140,26,False,GRAY)
  elif n==16:
   text(o,s['screen'],64,160,1140,35)
   text(o,'Amplificadores',64,354,520,36,True,BLUE)
   text(o,'Offset, ganancia y transitorios pueden alterar una medida.',64,419,520,33)
   text(o,'Cuarzo y osciladores',690,354,520,36,True,BLUE)
   text(o,'Frecuencia, pérdidas y electrónica de reloj afectan el tiempo.',690,419,520,33)
   text(o,'Voyager seleccionó barras de cuarzo mediante ensayos.',64,597,1140,30)
  elif n==17:
   text(o,s['screen'],64,160,1140,35)
   text(o,'60 krad(Si) / 30 krad(Si) = 2',64,353,1140,54,True,BLUE)
   text(o,'Capacidad de referencia / exposición local prevista',64,453,1140,33)
   text(o,'Ejemplo histórico de diseño, no dosis acumulada actual.',64,555,1140,30,False,GRAY)
 text(o,f'{n:02d}',1160,657,55,29,False,BLUE)
 for op in o:
  if op['y']+op['h']>710:raise ValueError((n,op))
(B/'layout.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
outline=B.parents[1]/'versión 2 revisada/02_Esquema_diapositivas.md'
content=outline.read_text()
for d in D:
    extra=[]
    for op in d['ops']:
        if op['kind']=='table':
            rows=op['rows'];extra.append('| '+' | '.join(rows[0])+' |\n| '+' | '.join(['---']*len(rows[0]))+' |\n'+'\n'.join('| '+' | '.join(row)+' |' for row in rows[1:]))
        elif op['kind']=='text':
            t=' '.join(op['text'].split());omit=[' '.join(d['title'].split()),' '.join(d['screen'].split()),d['caption'],f"{d['n']:02d}"]
            if t not in omit:extra.append(op['text'])
    if extra:
        start=content.index(f"## {d['n']:02d}. ")
        pos=content.index('### Apoyo oral',start)
        content=content[:pos]+'### Texto adicional y datos del recurso visual\n\n'+'\n\n'.join(extra)+'\n\n'+content[pos:]
outline.write_text(content)
print('Layout:',len(D),'slides')
