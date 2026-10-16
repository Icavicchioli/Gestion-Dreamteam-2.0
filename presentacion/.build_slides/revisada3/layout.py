from pathlib import Path
import json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
B=Path(__file__).parent;OUT=B.parents[1]/'versión 3 basada en JPL 77-41'
for n,f in [('Arial','Arial.ttf'),('Arial-Bold','Arial Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,'/System/Library/Fonts/Supplemental/'+f))
D=json.loads((B/'contenido.json').read_text()); INK='#172B3A';BLUE='#126F87';GRAY='#49616E'
def wrap(s,w,size,bold=False):
 lines=[]
 for para in s.split('\n'):
  line=''
  for word in para.split():
   q=(line+' '+word).strip()
   if line and pdfmetrics.stringWidth(q,'Arial-Bold' if bold else 'Arial',size)>w:
    lines.append(line);line=word
   else:line=q
  lines.append(line)
 return '\n'.join(lines)
def text(o,s,x,y,w,size=32,bold=False,color=INK):
 t=wrap(s,w,size,bold);h=len(t.splitlines())*size*1.23+6
 o.append(dict(kind='text',text=t,x=x,y=y,w=w,h=h,size=size,bold=bold,color=color));return y+h
def pic(o,f,x,y,w,h):o.append(dict(kind='image',file=f,x=x,y=y,w=w,h=h))
def table(o,rows,y,h,widths,size=28):o.append(dict(kind='table',rows=rows,x=64,y=y,w=1152,h=h,widths=widths,size=size))
foot={1:'Informe JPL 77-41, volumen I · 1977',2:'NASA · Historia 2022 y comunicado del 05/03/2025',3:'JPL · §VI.A, p. 6-1 / PDF 81',4:'JPL · §II, pp. 2-1 a 2-4 / PDF 25-28',5:'JPL · §II y §III.D',6:'JPL · Tablas 2-1, 2-2 y 5-3',7:'JPL · §III.A y §IV · Arquitectura: NASA/Tomayko',8:'JPL · §VII.H, p. 7-53 / PDF 151',9:'JPL · §VII.I, pp. 7-55 y 7-57 / PDF 153 y 155',10:'JPL · §VII.B-C, pp. 7-2 a 7-9 / PDF 100-107',11:'JPL · §VII.E, §VIII.B y §IX.C.4',12:'JPL · §VI.B, pp. 6-1 a 6-3 / PDF 81-83',13:'JPL · §VI.B, §VII.F y §VIII.E',14:'JPL · §VI.C y §VII.D · Figura 7-4',15:'JPL · §VI.B, §VII.I-J y §VIII.F',16:'JPL · §IV.B y §VIII · Figura 8-21',17:'JPL · Tablas 2-2 y 3-1; §III.B-C',18:'JPL · §IX, pp. 9-1 a 9-5 / PDF 204-208'}
tabletexts={}
for s in D:
 n=s['n'];o=[];s['ops']=o
 if n==1:
  text(o,s['title'],64,65,1160,55,True)
  text(o,'Ignacio Cavicchioli',64,253,650,34,False,BLUE)
  text(o,s['screen'],64,329,600,34)
  pic(o,s['image'],720,230,475,375)
 elif n==2:
  text(o,s['title'],64,48,1148,44,True)
  text(o,s['screen'],64,157,590,32)
  pic(o,s['image'],709,150,495,370)
  text(o,'V1: >25.000 millones de km\nV2: >21.000 millones de km',64,435,595,29,False,BLUE)
  text(o,'A la Tierra · NASA, 05/03/2025',64,536,610,25,False,GRAY)
  text(o,'49 años desde los lanzamientos, al 16/10/2026.',64,590,1145,29)
 elif n in [3,7,9,10,12,14,16,18]:
  text(o,s['title'],64,48,1152,44,True)
  text(o,s['screen'],64,166,565,33)
  pic(o,s['image'],688,156,526,390)
  # Short captions on projection; full original captions remain in notes and dossier.
  short={3:'Cinturones jovianos · NASA/JPL',7:'Instrumentos de Voyager · NASA',9:'Figura 7-9 · Circuito de ensayo',10:'Figura 7-1 · Δ(1/β) frente a I_C',12:'Figura 6-1 · I_D frente a V_G',14:'Figura 7-4 · LM108 estándar y endurecido',16:'Figura 8-21 · Lotes CD4053B',18:'Integración de Voyager 2 · NASA/JPL'}
  text(o,short[n],688,558,526,25,False,GRAY)
  text(o,s['extra'],64,600,1148,27,False,BLUE)
 elif n==4:
  text(o,s['title'],64,48,1152,43,True)
  text(o,s['screen'],64,168,1152,32)
  table(o,[['Situación','Poblaciones del modelo'],['Crucero','Solar y cósmica galáctica'],['Cinturones terrestres y jovianos','Electrones y protones atrapados'],['Fuentes a bordo','Neutrones y gamma de RTG/RHU']],340,246,[550,602],29)
  text(o,s['extra'],64,610,1152,26,False,BLUE)
 elif n==5:
  text(o,s['title'],64,48,1152,44,True)
  text(o,s['screen'],64,167,1152,35)
  text(o,'Electrones y protones tienen carga.\nNeutrones y fotones transfieren energía sin carga eléctrica.',64,352,1152,35,True,BLUE)
  text(o,s['extra'],64,550,1152,31)
 elif n==6:
  text(o,s['title'],64,48,1152,44,True)
  text(o,s['screen'],64,164,1152,31)
  table(o,[['Magnitud','Qué expresa'],['Tipo y energía','Agente y energía incidente: eV, keV, MeV'],['Flujo / fluencia','Por área y tiempo / acumulado por área'],['Dosis','Energía absorbida por masa: Gy o rad(Si)']],327,240,[375,777],28)
  text(o,s['extra'],64,601,1152,27,False,BLUE)
 elif n==8:
  text(o,s['title'],64,48,1152,44,True)
  text(o,s['screen'],64,164,1152,32)
  table(o,[['Pieza ensayada','Exposición','Resultado'],['Dale: película metálica','10¹³ e/cm²','ΔR dentro de ±0,01 %'],['B11B: 0,02 µF','5 × 10¹² e/cm²','C disminuyó 5 pF en promedio'],['B11B: 0,05 µF','5 × 10¹² e/cm²','C disminuyó 12 pF en promedio']],337,248,[410,310,432],27)
  text(o,'Inductores y conexiones: el informe no da una caracterización equivalente.',64,610,1152,26,False,BLUE)
 elif n==11:
  text(o,s['title'],64,48,1152,44,True)
  text(o,s['screen'],64,166,1152,32)
  table(o,[['Conmutador','Elemento de paso','Controlador'],['DG129 / DG133 / DG141','JFET de canal n','Bipolar'],['DG181','JFET de canal n','Bipolar y MOS']],345,202,[475,340,337],28)
  text(o,s['extra'],64,601,1152,29,False,BLUE)
 elif n==13:
  text(o,s['title'],64,48,1152,44,True)
  text(o,s['screen'],64,166,1152,35)
  text(o,'1100 °C → 950 °C',64,390,1152,64,True,BLUE)
  text(o,'Recocido del óxido durante la fabricación',64,490,1152,34)
  text(o,'Después: verificar fugas, consumo, retardo y variación entre lotes.',64,592,1152,29)
 elif n==15:
  text(o,s['title'],64,48,1152,44,True)
  text(o,s['screen'],64,166,1152,35)
  text(o,'Memoria CMOS',64,367,530,36,True,BLUE)
  text(o,'Blindaje para limitar la dosis a 10 krad(Si).',64,429,530,34)
  text(o,'Cristales de cuarzo',690,367,520,36,True,BLUE)
  text(o,'Muestras de las barras antes de fabricar piezas de vuelo.',690,429,520,34)
  text(o,'Registros MOS: también aparecen en la lectura del detector UVS.',64,598,1152,28)
 elif n==17:
  text(o,s['title'],64,48,1152,44,True)
  text(o,s['screen'],64,166,1152,35)
  text(o,'60 krad(Si) / 30 krad(Si) = 2',64,390,1152,54,True,BLUE)
  text(o,'Capacidad en la aplicación / exposición local prevista',64,492,1152,33)
  text(o,'Ejemplo del bus de ingeniería; no representa su dosis actual.',64,593,1152,29)
 text(o,foot[n],64,668,1050,19,False,GRAY)
 text(o,f'{n:02}',1160,662,56,28,False,BLUE)
 for op in o:
  if op['y']+op['h']>710:raise ValueError((n,op))
 # Reconstruct visible text so outline includes all editable content and data.
 visible=[]
 for op in o:
  if op['kind']=='table':
   rows=op['rows'];visible.append('| '+' | '.join(rows[0])+' |\n| '+' | '.join(['---']*len(rows[0]))+' |\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows[1:]))
  elif op['kind']=='text' and op['y']<660:
   q=' '.join(op['text'].split())
   if q not in [' '.join(s['title'].split()),' '.join(s['screen'].split())]:visible.append(op['text'])
 s['visible_extra']='\n\n'.join(visible)
(B/'layout.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
f=OUT/'02_Esquema_diapositivas.md';t=f.read_text()
for s in D:
 start=t.index(f"## {s['n']:02}. ")
 a=t.index('### Datos o texto de apoyo visibles',start);b=t.index('### Apoyo oral',a)
 t=t[:a]+'### Datos o texto de apoyo visibles\n\n'+s['visible_extra']+'\n\n'+t[b:]
f.write_text(t)
print('Layout listo:',len(D))
