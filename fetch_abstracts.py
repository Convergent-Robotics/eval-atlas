"""Fetch arXiv abstracts by id into sources/abstracts.md (appends, skips ids already present)."""
import sys, re, subprocess, xml.etree.ElementTree as ET, pathlib
ns = {'a': 'http://www.w3.org/2005/Atom'}
out = pathlib.Path(__file__).parent / 'sources' / 'abstracts.md'
have = set(re.findall(r'^## (\S+)', out.read_text(), re.M)) if out.exists() else set()
ids = [i for i in sys.argv[1].split(',') if i not in have]
if not ids: sys.exit()
xml = subprocess.run(['curl', '-sSL', '-m', '120', f'https://export.arxiv.org/api/query?id_list={",".join(ids)}&max_results={len(ids)}'],
                     capture_output=True, text=True).stdout
with out.open('a') as f:
    for e in ET.fromstring(xml).findall('a:entry', ns):
        i = re.sub(r'v\d+$', '', e.find('a:id', ns).text.split('/')[-1])
        t = ' '.join(e.find('a:title', ns).text.split())
        au = [a.text for a in e.findall('a:author/a:name', ns)]
        s = ' '.join(e.find('a:summary', ns).text.split())
        rec = f"## {i} | {t} | {au[0] if au else ''} et al. | {e.find('a:published', ns).text[:10]}\n{s}\n\n"
        f.write(rec); print(rec)
