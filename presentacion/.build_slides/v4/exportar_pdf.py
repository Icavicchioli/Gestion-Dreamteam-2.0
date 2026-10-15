"""Exportación PDF con Arial embebida, usando el mismo contenido y geometría."""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

root=Path.cwd()
data=json.loads((root/'.build_slides/v4/contenido.json').read_text())
out=root/'entregables/v4/Voyager_radiacion.pdf'
assert (out.parent/'Voyager_radiacion_final.pptx').exists()
pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
c=canvas.Canvas(str(out),pagesize=(960,540))
c.setTitle('Radiación y electrónica de Voyager')
c.setAuthor('Ignacio Cavicchioli')
ink='#172B3A';blue='#126FA1';muted='#172B3A'
def text(t,x,y,size=36,color=ink,bold=False):
    font='Arial-Bold' if bold else 'Arial'
    c.setFont(font,size*.75);c.setFillColor(color)
    for j,line in enumerate(t.split('\n')):
        c.drawString(x*.75,540-(y+size*.91+j*size*1.2)*.75,line)
def image(f,x,y,w,h):
    im=Image.open(root/f);iw,ih=im.size;k=min(w/iw,h/ih);dw,dh=iw*k,ih*k
    c.drawImage(str(root/f),(x+(w-dw)/2)*.75,540-(y+(h-dh)/2+dh)*.75,dw*.75,dh*.75,mask='auto')
def bullets(items,y):
    for j,line in enumerate(items):
        text('•',74,y+j*65.5,32)
        text(line,94,y+j*65.5,32)
captions={3:['SOHO, julio de 1996'],4:['Cinturones observados por Cassini'],5:['Ilustración NASA de la heliosfera'],6:['Voyager 2 en pruebas','Marzo de 1977'],7:['Hardware FDS, fotografía JPL'],11:['Fotodiodo: ejemplo equivalente'],12:['Sección de BJT NPN, JPL'],13:['Sección NMOS, ejemplo JPL']}
for i,d in enumerate(data,1):
    text(f'{i:02}',1165,656,32,blue)
    if d.get('layout')=='cover':
        text(d['title'],64,56,54,bold=True)
        text('Ignacio Cavicchioli',64,268,36,blue)
        text('Objetivo: explicar efectos',64,390)
        text('y mitigaciones.',64,442)
        image(d['image'],660,250,555,330)
    else:
        text(d['title'],64,48,46,bold=True)
        if d.get('layout')=='figure':
            text(d['intro'][0],64,142,34)
            image(d['image'],360,207,720,395)
            if i==20:
                text('Δ(1/hFE)',64,325,32,blue);text('IC en mA',64,395,32,blue)
            if i==21:
                text('ID en µA',64,325,32,blue);text('VG en V',64,395,32,blue);text('Antes / 150 krad',930,325,32,blue)
            if i==22:
                text('Salida en V',64,325,32,blue);text('Tiempo en s',64,395,32,blue)
            text(d['caption'],64,608,32,muted)
        else:
            for j,t in enumerate(d['intro']):text(t,64,155+j*53)
            bullets(d['bullets'],330 if d.get('image') else 340)
            if d.get('image'):
                image(d['image'],658,300,557,280)
                for j,t in enumerate([d['caption']]):text(t,658,587+j*38,32,muted)
    c.showPage()
c.save()
print(out)
