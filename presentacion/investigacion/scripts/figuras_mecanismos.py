"""Esquemas pedagógicos propios, sin geometrías ni valores de vuelo."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
out=Path(__file__).resolve().parents[1]/'figuras'
font=lambda n:ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',n)
ink='#173449';blue='#16788b';red='#b14b35'
im=Image.new('RGB',(1800,1100),'white');d=ImageDraw.Draw(im)
def t(x,y,s,n=27,c=ink):d.text((x,y),s,font=font(n),fill=c)
def arrow(a,b,c=blue):
 d.line([a,b],fill=c,width=5);ang=math.atan2(b[1]-a[1],b[0]-a[0]);l=17
 d.polygon([b,(b[0]-l*math.cos(ang-.5),b[1]-l*math.sin(ang-.5)),(b[0]-l*math.cos(ang+.5),b[1]-l*math.sin(ang+.5))],fill=c)
t(60,35,'Tres mecanismos, tres preguntas distintas',49)
t(60,105,'Esquemas conceptuales propios • sin escala • no representan dispositivos de vuelo',27)
for x in [50,635,1220]:d.rounded_rectangle((x,185,x+530,960),radius=16,outline='#bccdd7',width=2)
t(75,210,'Unión: recoge carga',33)
d.rectangle((85,330,235,530),fill='#d7eaf0');d.rectangle((235,330,365,530),fill='#eee5d6');d.rectangle((365,330,545,530),fill='#d7eaf0')
t(125,350,'p',35);t(440,350,'n',35);t(242,545,'Campo',24)
arrow((350,400),(250,400));t(245,610,'electrón (-)',25);t(165,662,'hueco (+)',25)
arrow((260,650),(425,650));arrow((330,695),(165,695))
t(80,750,'La ionización genera un par.',25);t(80,795,'El campo separa portadores.',25);t(80,840,'Puede aparecer corriente espuria.',25)
t(660,210,'MOS: cambia el campo',33)
d.rectangle((690,335,1100,390),fill='#abc2ce');t(790,345,'Compuerta',28)
d.rectangle((690,405,1100,500),fill='#f4e3bf');t(718,420,'Óxido: carga atrapada',26)
for x in [740,850,960,1055]:t(x,463,'+',28,red)
d.rectangle((665,515,1135,675),fill='#d7eaf0');t(760,595,'Semiconductor',28)
for x in [765,895,1025]:arrow((x,510),(x,568))
t(665,750,'La carga altera la electrostática.',25);t(665,795,'Cambia la tensión de control.',25);t(665,840,'También importan las interfaces.',25)
t(1245,210,'Capacitor: pierde carga',33)
# Circuito equivalente, dos ramas entre nodos.
d.line([(1280,360),(1700,360),(1700,430)],fill=ink,width=4)
d.line([(1280,360),(1280,470)],fill=ink,width=4)
d.line([(1245,470),(1315,470)],fill=ink,width=6);d.line([(1245,495),(1315,495)],fill=ink,width=6)
d.line([(1280,495),(1280,635),(1700,635),(1700,535)],fill=ink,width=4)
d.rectangle((1675,430,1725,535),outline=ink,width=4)
t(1325,465,'C',30);t(1515,465,'R de fuga',26)
t(1250,750,'Más conducción en el aislante.',25);t(1250,795,'Menor resistencia de fuga.',25);t(1250,840,'C puede cambiar muy poco.',25)
t(60,1005,'Fuentes de los mecanismos: NASA/JPL S21–S25 y S35. Interpretación en el dossier §3.',25)
im.save(out/'02_mecanismos_conceptuales.png')

im=Image.new('RGB',(1800,1000),'white');d=ImageDraw.Draw(im)
t(60,35,'El pulso termina; el estado puede permanecer',48)
t(60,105,'Ejemplo conceptual • no reconstruye una falla de Voyager',28)
names=['Amplificador','Comparador','Registro','Carga']
for i,name in enumerate(names):
 x=80+i*440;d.rounded_rectangle((x,205,x+310,310),radius=12,fill='#e7f0f4',outline=ink,width=2);t(x+25,239,name,32)
 if i<3:arrow((x+315,255),(x+425,255))
t(85,365,'Un pulso supera el umbral y es aceptado por el receptor: condición supuesta.',28)
for y,label in [(600,'Perturbación'),(815,'Estado registrado')]:
 d.line([(335,y),(1690,y)],fill='#a9b8c2',width=2);t(60,y-75,label,27);arrow((335,y+20),(335,y-150),ink);arrow((335,y),(1705,y),ink)
d.line([(340,600),(660,600),(670,485),(770,485),(780,600),(1670,600)],fill=blue,width=5)
d.line([(340,815),(690,815),(690,700),(1670,700)],fill=red,width=5)
t(820,495,'El circuito analógico se recupera',28,blue)
t(820,735,'El registro necesita otra acción',28,red)
t(1570,845,'Tiempo',26)
t(60,920,'Si el pulso no cumple amplitud y tiempo requeridos, el registro puede no cambiar. Fuentes: S22 y S35.',25)
im.save(out/'03_pulso_y_estado.png')
print('Dos esquemas conceptuales generados.')
