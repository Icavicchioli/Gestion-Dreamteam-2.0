"""Descarga cinco imágenes públicas NASA/PDS y conserva su procedencia."""
from pathlib import Path
import subprocess, json, hashlib

ROOT = Path(__file__).resolve().parents[2]
p = ROOT / 'investigacion/imagenes_diapos'
p.mkdir(exist_ok=True)
base = 'https://www.nasa.gov/wp-content/uploads/2022/09/'
items = [
    ('01_instrumentos.jpg', base+'voyager_1_5_instruments.jpg'),
    ('02_trayectorias.png', base+'voyager_1_6_trajectories_lightened.png'),
    ('03_heliosfera.jpg', base+'voyager_1_14_interstellar_mission.jpg'),
    ('04_lanzamiento.jpg', base+'voyager_1_4_launch.jpg'),
    ('05_pws_bloques.gif', 'https://pds.nasa.gov/data/vg1-j-spice-6-spk-v2.0/vg_1501/document/pws/fig7.gif'),
]
records = []
for name, url in items:
    subprocess.run(['curl', '-fLsS', '--max-time', '45', url, '-o', str(p/name)], check=True)
    records.append(dict(archivo=name, url=url, consulta='2026-10-14', sha256=hashlib.sha256((p/name).read_bytes()).hexdigest()))
(p/'catalogo.json').write_text(json.dumps(records, indent=2)+'\n')
u = 'https://www.nasa.gov/history/45-years-ago-voyager-1-begins-its-epic-journey-to-the-outer-planets-and-beyond/'
f = ROOT/'citas/S37_historia_imagenes_2022.html'
subprocess.run(['curl', '-fLsS', '--max-time', '45', u, '-o', str(f)], check=True)
c = ROOT/'citas/catalogo.json'
r = [x for x in json.loads(c.read_text()) if x['id'] != 'S37']
r.append(dict(id='S37', titulo='45 Years Ago: Voyager 1 Begins its Epic Journey to the Outer Planets and Beyond', fecha='2022-09-07', url=u, archivo=f.name, consulta='2026-10-14', sha256=hashlib.sha256(f.read_bytes()).hexdigest(), bytes=f.stat().st_size, estado='descargado'))
c.write_text(json.dumps(r, ensure_ascii=False, indent=2)+'\n')
print('Descargadas cinco imágenes y página de procedencia.')
