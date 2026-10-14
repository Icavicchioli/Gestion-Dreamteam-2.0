from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
root=Path.cwd();images=root/'.build_slides/v2/renders';out=root/'entregables/v2/Voyager_radiacion_v2.pdf'
files=[images/f'{n:02d}.png' for n in range(1,17)]
assert all(p.exists() for p in files), 'Faltan diapositivas finales'
assert (root/'entregables/v2/Voyager_radiacion_v2.pptx').exists(), 'Falta PPTX validado'
c=canvas.Canvas(str(out),pagesize=(960,540));c.setTitle('Radiación y electrónica de Voyager');c.setAuthor('Ignacio Cavicchioli')
for n,p in enumerate(files,1):
 c.bookmarkPage(f'slide{n}');c.addOutlineEntry(f'Diapositiva {n}',f'slide{n}',0)
 c.drawImage(ImageReader(str(p)),0,0,960,540);c.showPage()
c.save();assert len(PdfReader(out).pages)==16;print(out)
