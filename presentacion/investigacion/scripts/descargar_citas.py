"""Descarga exclusivamente las fuentes públicas enumeradas en citas/catalogo.json.

No accede a credenciales ni modifica los originales de trabajo del usuario.
Los PDF ya descargados se conservan. Las copias web llevan fecha de consulta.
"""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import json
import urllib.request
import subprocess
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / 'citas'

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.lines = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'):
            self.hidden += 1
        if tag in ('p', 'div', 'h1', 'h2', 'h3', 'li', 'tr', 'br'):
            self.lines.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript'):
            self.hidden = max(0, self.hidden - 1)
        if tag in ('p', 'div', 'h1', 'h2', 'h3', 'li', 'tr'):
            self.lines.append('\n')
    def handle_data(self, data):
        if not self.hidden:
            self.lines.append(data)

def main():
    records = json.loads((DEST / 'catalogo.json').read_text())
    for item in records:
        path = DEST / item['archivo']
        if item.get('estado', '').startswith('copia_textual_web'):
            print(item['id'], 'copia de lectura conservada', path.name)
            continue
        try:
            if not path.exists():
                req = urllib.request.Request(item['url'], headers={'User-Agent': 'VoyagerResearch/1.0'})
                try:
                    with urllib.request.urlopen(req, timeout=50) as response:
                        data = response.read()
                        item['url_final'] = response.url
                except urllib.error.URLError:
                    # curl usa el almacén de confianza del sistema; mantiene TLS verificado.
                    data = subprocess.check_output(['/usr/bin/curl', '--fail', '--location', '--silent', '--show-error', '--max-time', '50', item['url']])
                path.write_bytes(data)
            data = path.read_bytes()
            item['sha256'] = hashlib.sha256(data).hexdigest()
            item['bytes'] = len(data)
            item['consulta'] = '2026-10-14'
            if path.suffix == '.pdf':
                reader = PdfReader(path)
                text = '\n'.join(f'\n--- PAGINA PDF {i+1} ---\n'+p.extract_text() for i,p in enumerate(reader.pages))
                path.with_suffix('.txt').write_text(text)
                item['paginas_pdf'] = len(reader.pages)
            elif path.suffix == '.html':
                parser = TextExtractor()
                parser.feed(data.decode('utf-8', errors='replace'))
                lines = [x.strip() for x in ''.join(parser.lines).splitlines() if x.strip()]
                path.with_suffix('.txt').write_text('\n'.join(lines))
            item['estado'] = 'descargado'
            item.pop('error', None)
            print(item['id'], item['estado'], path.name, flush=True)
        except Exception as error:
            item['estado'] = 'pendiente_descarga'
            item['error'] = str(error)
            print(item['id'], item['estado'], str(error)[:180], flush=True)
        (DEST / 'catalogo.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')

if __name__ == '__main__':
    main()
