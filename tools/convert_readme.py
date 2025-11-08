import io
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
OUT = ROOT / 'README_preview.html'

md_text = README.read_text(encoding='utf-8')
html = markdown.markdown(md_text, extensions=['fenced_code', 'tables', 'codehilite'])
full = (
    '<!doctype html><meta charset="utf-8"><title>README preview</title>'
    '<style>body{font-family:Segoe UI,Arial,Helvetica,sans-serif;margin:24px;max-width:980px}pre{background:#f6f8fa;padding:12px;border-radius:6px;overflow:auto}</style>'
    + html
)
OUT.write_text(full, encoding='utf-8')
print('WROTE:', OUT)
