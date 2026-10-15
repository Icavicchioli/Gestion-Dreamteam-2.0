"""Markdown local a PDF de estudio. No usa servicios externos ni modifica fuentes."""
from pathlib import Path
import html, json, re, os, shutil, unicodedata, sys
from urllib.parse import quote
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, PageBreak, Image, LongTable, TableStyle, KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
from pypdf import PdfReader

ROOT=Path.cwd()
OUT=ROOT/'cosas que tengo que leer'
OUT.mkdir(exist_ok=True)
BUILD=ROOT/'.build_slides/v4'
for name,file in [('Arial','Arial.ttf'),('Arial-Bold','Arial Bold.ttf'),('Arial-Italic','Arial Italic.ttf'),('Arial-BoldItalic','Arial Bold Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/System/Library/Fonts/Supplemental/'+file))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial-Italic',boldItalic='Arial-BoldItalic')
pdfmetrics.registerFont(TTFont('ArialUnicode','/System/Library/Fonts/Supplemental/Arial Unicode.ttf'))
pdfmetrics.registerFontFamily('ArialUnicode',normal='ArialUnicode',bold='ArialUnicode',italic='ArialUnicode',boldItalic='ArialUnicode')
def glyphs(s):
    return re.sub('[⁻₂⁸⁶⁴⁹]',lambda m:'<font name="ArialUnicode">'+m[0]+'</font>',s)
INK=colors.HexColor('#172B3A'); BLUE=colors.HexColor('#126FA1')
ST={
 'body':ParagraphStyle('body',fontName='Arial',fontSize=10.5,leading=14.5,textColor=INK,spaceAfter=8,splitLongWords=1),
 'h1':ParagraphStyle('h1',fontName='Arial-Bold',fontSize=22,leading=27,textColor=INK,spaceAfter=16,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='Arial-Bold',fontSize=15,leading=19,textColor=BLUE,spaceBefore=14,spaceAfter=9,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='Arial-Bold',fontSize=12,leading=16,textColor=INK,spaceBefore=12,spaceAfter=7,keepWithNext=True),
 'h4':ParagraphStyle('h4',fontName='Arial-Bold',fontSize=11,leading=15,textColor=INK,spaceBefore=9,spaceAfter=6,keepWithNext=True),
 'table':ParagraphStyle('table',fontName='Arial',fontSize=9.5,leading=12.5,textColor=INK,spaceAfter=0,splitLongWords=1),
 'th':ParagraphStyle('th',fontName='Arial-Bold',fontSize=9.5,leading=12.5,textColor=colors.white,spaceAfter=0),
 'code':ParagraphStyle('code',fontName='Arial',fontSize=10,leading=15,textColor=INK,backColor=colors.HexColor('#F1F5F8'),borderPadding=8,spaceAfter=10),
 'caption':ParagraphStyle('caption',fontName='Arial-Italic',fontSize=9.5,leading=12.5,textColor=INK,spaceAfter=12),
 'bullet':ParagraphStyle('bullet',fontName='Arial',fontSize=10.5,leading=14.5,textColor=INK,leftIndent=13,firstLineIndent=0,bulletIndent=0,spaceAfter=6),
}
for style in ST.values():
    style.allowWidows=0
    style.allowOrphans=0
    style.bulletFontName='Arial'
MAP={
 'investigacion/01_dossier.md':'01_Dossier.pdf',
 'entregables/v4/notas_orales.md':'02_Guion_para_exponer.pdf',
 'investigacion/04_fuentes.md':'04_Fuentes_y_figuras.pdf',
 'investigacion/02_matriz_evidencias.md':'05_Matriz_de_evidencias.pdf',
 'investigacion/00_consignas.md':'06_Consignas_y_validacion.pdf',
 'investigacion/05_validacion.md':'06_Consignas_y_validacion.pdf',
 'investigacion/07_auditoria_consignas.md':'06_Consignas_y_validacion.pdf',
 'investigacion/06_revision_historica.md':'07_Revision_historica.pdf',
 'entregables/v4/00_empeza_por_aca.md':'00_Empeza_por_aca.pdf',
}
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')

def resolve_link(url,source):
    if re.match(r'^(https?://|mailto:)',url):return url
    if url.startswith('#'):return url
    pathname,sep,fragment=url.partition('#')
    target=(source.parent/pathname).resolve()
    try: rel=target.relative_to(ROOT).as_posix()
    except ValueError: rel=''
    if rel in MAP:return MAP[rel]+('#'+fragment if sep else '')
    # Los originales permanecen en el repositorio, fuera de la carpeta de PDFs.
    return quote(os.path.relpath(target,OUT),safe='/')+('#'+fragment if sep else '')

def inline(s,source):
    saved=[]
    def hold(v):
        key=f'ZZTOKEN{len(saved)}ZZ';saved.append(v);return key
    def mdlink(m):
        label=html.escape(m.group(1)); dest=html.escape(resolve_link(m.group(2),source),quote=True)
        return hold(f'<link href="{dest}" color="#126FA1">{label}</link>')
    s=re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)',mdlink,s)
    s=re.sub(r'https?://[^\s<>]+',lambda m:hold('<link href="'+html.escape(m.group(0),quote=True)+'" color="#126FA1">'+html.escape(m.group(0))+'</link>'),s)
    s=html.escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
    s=re.sub(r'`([^`]+)`',r'<font color="#126FA1">\1</font>',s)
    for i,v in enumerate(saved):s=s.replace(f'ZZTOKEN{i}ZZ',v)
    return glyphs(s)

class Doc(BaseDocTemplate):
    def __init__(self,file,title,wide=False):
        self.title_text=title; self.wide=wide
        pagesize=landscape(A4) if wide else A4
        super().__init__(str(file),pagesize=pagesize,leftMargin=38,rightMargin=38,topMargin=48,bottomMargin=43,title=title,author='Ignacio Cavicchioli')
        frame=Frame(self.leftMargin,self.bottomMargin,self.width,self.height,id='main',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates(PageTemplate(id='body',frames=[frame],onPage=self.page_frame))
    def page_frame(self,c,doc):
        c.saveState();c.setFont('Arial',8.5);c.setFillColor(INK)
        c.drawString(self.leftMargin,self.pagesize[1]-29,self.title_text)
        c.drawString(self.leftMargin,23,'Voyager | corte documental: 14/10/2026')
        c.drawRightString(self.pagesize[0]-self.rightMargin,23,str(doc.page))
        c.restoreState()
    def afterFlowable(self,f):
        if hasattr(f,'toc_level'):
            self.canv.bookmarkPage(f.anchor)
            self.canv.addOutlineEntry(f.getPlainText(),f.anchor,min(f.toc_level,1),False)
            self.notify('TOCEntry',(f.toc_level,f.getPlainText(),self.page,f.anchor))

def blocks(source,width,with_toc=False):
    lines=source.read_text().splitlines(); story=[]; i=0; image_count=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        anchor=re.fullmatch(r'<a id="([^"]+)"></a>',line)
        if anchor:
            story.append(Paragraph(f'<a name="{anchor.group(1)}"/>',ST['body']));i+=1;continue
        h=re.match(r'^(#{1,4})\s+(.+)',line)
        if h:
            level=len(h[1]);txt=h[2];key=slug(txt)
            para=Paragraph(f'<a name="{key}"/>'+inline(txt,source),ST['h'+str(level)])
            if level in (2,3):para.toc_level=level-2;para.anchor=source.stem+'-'+key
            story.append(para);i+=1
            if level==1 and with_toc:
                story.append(Paragraph('Índice',ST['h2']))
                toc=TableOfContents()
                toc.levelStyles=[ParagraphStyle('toc0',fontName='Arial-Bold',fontSize=10.5,leading=14,spaceBefore=6,textColor=INK),ParagraphStyle('toc1',fontName='Arial',fontSize=10,leading=13,leftIndent=13,textColor=INK)]
                story.extend([toc,PageBreak()])
            continue
        img=re.fullmatch(r'!\[([^]]*)\]\(([^)]+)\)',line)
        if img:
            file=(source.parent/img[2]).resolve();assert file.exists(),file
            with PILImage.open(file) as p:iw,ih=p.size
            scale=min(width/iw,570/ih)
            im=Image(str(file),width=iw*scale,height=ih*scale)
            im.hAlign='CENTER'
            caption=Paragraph(inline(img[1],source),ST['caption'])
            im.keepWithNext=True
            story.extend([im,caption])
            image_count+=1;i+=1;continue
        if line.startswith('```'):
            raw=[];i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'):
                raw.append(lines[i]);i+=1
            i+=1
            # Ecuaciones Unicode conservadas como texto seleccionable, con saltos explícitos.
            story.append(Paragraph(glyphs('<br/>'.join(html.escape(x) for x in raw)),ST['code']));continue
        if line.startswith('|') and i+1<len(lines) and re.match(r'^\s*\|[-: |]+\|\s*$',lines[i+1]):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=lines[i].strip()
                if not re.match(r'^\|[-: |]+\|$',row):rows.append([x.strip() for x in row.strip('|').split('|')])
                i+=1
            n=len(rows[0]);assert all(len(r)==n for r in rows),(source,rows)
            weights=[1/n]*n
            if n==3 and rows[0][1]=='Estado':weights=[.28,.13,.59]
            elif n==3 and rows[0][2]=='Estado':weights=[.28,.45,.27]
            elif n==3:weights=[.25,.38,.37]
            elif n==2:weights=[.29,.71]
            table=LongTable([[Paragraph(inline(c,source),ST['th' if r==0 else 'table']) for c in row] for r,row in enumerate(rows)],colWidths=[width*w for w in weights],repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F2F6F8')]),('LINEBELOW',(0,0),(-1,0),.6,BLUE)]))
            story.extend([KeepTogether([table]) if len(rows)<=5 else table,Spacer(1,12)]);continue
        bullet=re.match(r'^(?:[-*]|\d+\.)\s+(.+)',line)
        if bullet:
            story.append(Paragraph(inline(bullet[1],source),ST['bullet'],bulletText='•'));i+=1;continue
        if line.startswith('> '):line=line[2:]
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#{1,4} |\||!\[|```|<a |[-*] |\d+\. )',lines[i].strip()):
            para.append(lines[i].strip());i+=1
        story.append(Paragraph(inline(' '.join(para),source),ST['body']))
    return story,image_count

JOBS=[
 ('00_Empeza_por_aca.pdf','Guía de lectura',['entregables/v4/00_empeza_por_aca.md'],False,False),
 ('01_Dossier.pdf','Dossier: radiación y electrónica de Voyager',['investigacion/01_dossier.md'],False,True),
 ('02_Guion_para_exponer.pdf','Guion para exponer',['entregables/v4/notas_orales.md'],False,False),
 ('04_Fuentes_y_figuras.pdf','Fuentes, figuras y procedencia',['investigacion/04_fuentes.md','citas/presentacion_v3/README.md'],False,False),
 ('05_Matriz_de_evidencias.pdf','Matriz de evidencias',['investigacion/02_matriz_evidencias.md'],True,False),
 ('06_Consignas_y_validacion.pdf','Consignas, auditoría y validación',['investigacion/07_auditoria_consignas.md','investigacion/00_consignas.md','investigacion/05_validacion.md'],False,False),
 ('07_Revision_historica.pdf','Revisión histórica y de fuentes',['investigacion/06_revision_historica.md'],False,False),
]
manifest=[]
previous=json.loads((BUILD/'manifest_pdf.json').read_text()) if (BUILD/'manifest_pdf.json').exists() else []
for filename,title,sources,wide,toc in JOBS:
    if sys.argv[1:] and filename not in sys.argv[1:]:
        manifest.extend(x for x in previous if x['archivo']==filename)
        continue
    doc=Doc(OUT/filename,title,wide);story=[];images=0
    for j,src in enumerate(sources):
        if j:story.append(PageBreak())
        flow,n=blocks(ROOT/src,doc.width,toc);story.extend(flow);images+=n
    doc.multiBuild(story)
    reader=PdfReader(OUT/filename)
    manifest.append({'archivo':filename,'paginas':len(reader.pages),'imagenes_fuente':images,'fuentes':sources})
    print(filename,len(reader.pages),'páginas;',images,'imágenes',flush=True)
slides=ROOT/'entregables/v4/Voyager_radiacion.pdf'
ppt=ROOT/'entregables/v4/Voyager_radiacion_final.pptx'
if slides.exists():shutil.copy2(slides,OUT/'03_Presentacion.pdf')
if ppt.exists():shutil.copy2(ppt,OUT/'03_Presentacion_editable.pptx')
(BUILD/'manifest_pdf.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
