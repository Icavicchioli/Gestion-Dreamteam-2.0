from pathlib import Path
import re, html, json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, KeepTogether
from reportlab.pdfgen import canvas
from PIL import Image as PILImage

ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'versión 3 basada en JPL 77-41';BUILD=Path(__file__).parent
for name,file in [('Arial','Arial.ttf'),('Arial-Bold','Arial Bold.ttf'),('Arial-Italic','Arial Italic.ttf'),('Arial-BoldItalic','Arial Bold Italic.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/System/Library/Fonts/Supplemental/'+file))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial-Italic',boldItalic='Arial-BoldItalic')
INK=colors.HexColor('#172B3A');BLUE=colors.HexColor('#126F87');GRAY=colors.HexColor('#49616E')
styles={
 'body':ParagraphStyle('body',fontName='Arial',fontSize=10.5,leading=15.4,textColor=INK,spaceAfter=9,allowWidows=0,allowOrphans=0),
 'title':ParagraphStyle('title',fontName='Arial-Bold',fontSize=28,leading=34,textColor=INK,spaceAfter=24),
 'h2':ParagraphStyle('h2',fontName='Arial-Bold',fontSize=21,leading=27,textColor=INK,spaceBefore=24,spaceAfter=17,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='Arial-Bold',fontSize=13,leading=18,textColor=BLUE,spaceBefore=12,spaceAfter=7,keepWithNext=True),
 'caption':ParagraphStyle('caption',fontName='Arial-Italic',fontSize=9,leading=12,textColor=GRAY,spaceAfter=10),
 'cell':ParagraphStyle('cell',fontName='Arial',fontSize=9.1,leading=12,textColor=INK),
 'headcell':ParagraphStyle('headcell',fontName='Arial-Bold',fontSize=9.1,leading=12,textColor=colors.white),
}
def inline(t):
 t=html.escape(t)
 t=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',lambda m:f'<link href="{m[2]}" color="#126F87">{m[1]}</link>',t)
 t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
 t=re.sub(r'\*([^*]+)\*',r'<i>\1</i>',t)
 t=re.sub(r'`([^`]+)`',r'\1',t)
 return t
def footer(c,doc):
 c.saveState();c.setFont('Arial',8.5);c.setFillColor(GRAY)
 c.drawString(52,29,'Voyager · Versión 3 · JPL 77-41 · 16/10/2026')
 c.drawRightString(A4[0]-52,29,str(doc.page));c.restoreState()
class StudyDoc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and f.style.name=='h2' and re.match(r'^\d\d\.',f.getPlainText()):
   label=f.getPlainText();key='chapter-'+label[:2]
   self.canv.bookmarkPage(key);self.canv.addOutlineEntry(label,key,level=0,closed=False)
def make_dossier():
 raw=(OUT/'01_Dossier.md').read_text();lines=raw.splitlines();story=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('# '):story.append(Paragraph(inline(line[2:]),styles['title']));i+=1;continue
  if line.startswith('## '):
   title=line[3:]
   if title.startswith('01.'):story.append(PageBreak())
   story.append(Paragraph(inline(title),styles['h2']));i+=1;continue
  if line.startswith('### '):story.append(Paragraph(inline(line[4:]),styles['h3']));i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    r=[c.strip() for c in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r'[-: ]+',c) for c in r):rows.append(r)
    i+=1
   widths=[(A4[0]-104)/len(rows[0])]*len(rows[0])
   if len(rows[0])==3:widths=[133,164,A4[0]-104-297]
   t=Table([[Paragraph(inline(c),styles['headcell' if n==0 else 'cell']) for c in row]for n,row in enumerate(rows)],colWidths=widths,repeatRows=1,hAlign='LEFT')
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,0),(-1,-1),.35,colors.HexColor('#D7E2E6'))]))
   story.extend([KeepTogether([t]),Spacer(1,12)]);continue
  if line.startswith('!['):
   m=re.match(r'!\[(.*?)\]\((.*?)\)',line);p=OUT/m[2]
   im=PILImage.open(p);w,h=im.size;k=min((A4[0]-130)/w,205/h)
   fig=Image(str(p),width=w*k,height=h*k)
   cap='';j=i+1
   while j<len(lines) and not lines[j].strip():j+=1
   if j<len(lines) and lines[j].strip().startswith('*Figura'):
    cap=lines[j].strip().strip('*');i=j
   story.append(KeepTogether([Spacer(1,8),fig,Spacer(1,8),Paragraph(inline(cap),styles['caption'])]));i+=1;continue
  para=[line];i+=1
  while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','![')):
   para.append(lines[i].strip());i+=1
  if re.match(r'^\d+\. ',line):
   for t in para:story.append(Paragraph(inline(t),styles['body']))
  else:story.append(Paragraph(inline(' '.join(para)),styles['body']))
 doc=StudyDoc(str(OUT/'01_Dossier.pdf'),pagesize=A4,rightMargin=52,leftMargin=52,topMargin=48,bottomMargin=48,title='Voyager: radiación, componentes y decisiones de diseño',author='Ignacio Cavicchioli')
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
 print('Dossier PDF generado')

def make_slides():
 c=canvas.Canvas(str(OUT/'03_Presentacion.pdf'),pagesize=(960,540))
 c.setTitle('Voyager: radiación y electrónica');c.setAuthor('Ignacio Cavicchioli')
 for n in range(1,19):
  p=BUILD/'renders'/f'{n:02}.png';assert p.exists(),p
  c.drawImage(str(p),0,0,960,540);c.showPage()
 c.save();print('Presentación PDF generada desde las vistas del PowerPoint')
if __name__=='__main__':
 import sys
 if len(sys.argv)==1 or sys.argv[1]=='dossier':make_dossier()
 if len(sys.argv)==1 or sys.argv[1]=='slides':make_slides()
