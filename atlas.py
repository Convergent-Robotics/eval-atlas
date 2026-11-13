"""Eval Atlas data tool. The data lives in db/ as JSON files; the website page is built from them.

  python3 atlas.py check            validate every entry and gap against db/vocab.json
  python3 atlas.py stats            counts that the gap texts rely on
  python3 atlas.py new <id>         write a blank entry to db/entries/<id>.json
  python3 atlas.py fmt              rewrite all db files in the house layout
  python3 atlas.py export           check, then embed the data in docs/index.html

db/entries/<id>.json   one evaluation per file
db/gaps/<id>.json      one gap finding per file; "links" maps a name in the body to an entry id or a URL
db/vocab.json          tag labels and scoring rubrics
db/meta.json           "updated" (shown on the page) and "last_sweep" (where the next literature sweep starts)
"""
import json, pathlib, re, sys
from collections import Counter

ROOT = pathlib.Path(__file__).parent
DB = ROOT / "db"
# The public page, plus any extra local copies (e.g. a page embedded in another site) that exist on disk.
PAGES = [ROOT / "docs" / "index.html", ROOT / "site" / "eval-atlas.html"]

FIELDS = ["id", "name", "kind", "url", "arxiv", "code", "venue", "summary", "numbers",
          "domain", "arch", "failure", "harm", "layer", "fidelity", "avail",
          "cx", "dex", "cog", "bottleneck", "xr", "why"]
TAGS = ["domain", "arch", "failure", "harm", "layer", "fidelity"]
SCORES = {"cx": (1, 3), "dex": (0, 3), "cog": (1, 3), "xr": (0, 3)}
GAP_FIELDS = ["id", "order", "title", "body", "map", "links"]


def load(kind):
    return [json.loads(p.read_text()) for p in sorted((DB / kind).glob("*.json"))]

def vocab():
    return json.loads((DB / "vocab.json").read_text())

def meta():
    return json.loads((DB / "meta.json").read_text())

def dump(obj, order):
    """One key per line, values on a single line, so a diff shows exactly which field changed."""
    lines = [f" {json.dumps(k)}: {json.dumps(obj[k], ensure_ascii=False)}" for k in order if k in obj]
    return "{\n" + ",\n".join(lines) + "\n}\n"


def check():
    labels = vocab()["labels"]
    entries, gaps, errs = load("entries"), load("gaps"), []
    ids = {e["id"] for e in entries}
    for p, e in zip(sorted((DB / "entries").glob("*.json")), entries):
        where = p.name
        if p.stem != e.get("id"): errs.append(f"{where}: id {e.get('id')!r} does not match the file name")
        missing = [f for f in FIELDS if f not in e]
        extra = [f for f in e if f not in FIELDS]
        if missing: errs.append(f"{where}: missing {missing}")
        if extra: errs.append(f"{where}: unknown fields {extra}")
        for f in TAGS:
            for v in e.get(f, []):
                if v not in labels[f]: errs.append(f"{where}: {f} {v!r} is not in vocab")
        if e.get("kind") not in labels["kind"]: errs.append(f"{where}: kind {e.get('kind')!r} is not in vocab")
        if e.get("avail") not in labels["avail"]: errs.append(f"{where}: avail {e.get('avail')!r} is not in vocab")
        if e.get("bottleneck") not in ("cognition", "dexterity", "both"): errs.append(f"{where}: bad bottleneck")
        for f, (lo, hi) in SCORES.items():
            if not isinstance(e.get(f), int) or not lo <= e[f] <= hi: errs.append(f"{where}: {f} must be {lo}–{hi}")
        if not str(e.get("url", "")).startswith("http"): errs.append(f"{where}: url missing")
        if not e.get("domain") or not e.get("arch") or not e.get("fidelity"): errs.append(f"{where}: domain, arch and fidelity need a value")
    for g in gaps:
        where = f"gaps/{g.get('id')}.json"
        for n, target in g.get("links", {}).items():
            if n not in g["body"]: errs.append(f"{where}: link name {n!r} does not appear in the body")
            if not target.startswith("http") and target not in ids: errs.append(f"{where}: link {n!r} points at unknown entry {target!r}")
    return entries, gaps, errs


def cmd_check():
    entries, gaps, errs = check()
    for e in errs: print(e)
    print(f"{len(entries)} entries, {len(gaps)} gaps: " + ("OK" if not errs else f"{len(errs)} problems"))
    return not errs


def cmd_stats():
    E, _, _ = check()
    c = lambda f: dict(Counter(v for e in E for v in e[f]).most_common())
    print("entries:", len(E))
    print("real hardware:", sum("real" in e["fidelity"] for e in E))
    print("dex>=2 and cog>=2:", sum(e["dex"] >= 2 and e["cog"] >= 2 for e in E),
          "of which capability suites:", sum(e["dex"] >= 2 and e["cog"] >= 2 and e["kind"] == "capability" for e in E))
    print("xr>=2:", [e["id"] for e in E if e["xr"] >= 2])
    print("xr=3:", [e["id"] for e in E if e["xr"] == 3])
    for f in ("kind", "harm", "failure", "arch", "layer", "fidelity", "domain"):
        print(f + ":", c(f) if f != "kind" else dict(Counter(e["kind"] for e in E)))


def cmd_new(id):
    p = DB / "entries" / f"{id}.json"
    if p.exists(): sys.exit(f"{p} already exists")
    blank = dict(id=id, name="", kind="benchmark", url="", arxiv="", code="", venue="", summary="", numbers="",
                 domain=[], arch=[], failure=[], harm=[], layer=[], fidelity=[], avail="paper",
                 cx=1, dex=0, cog=1, bottleneck="cognition", xr=0, why=dict(cx="", dex="", cog="", xr=""))
    p.write_text(dump(blank, FIELDS))
    print("wrote", p.relative_to(ROOT))


def cmd_fmt():
    for p in (DB / "entries").glob("*.json"): p.write_text(dump(json.loads(p.read_text()), FIELDS))
    for p in (DB / "gaps").glob("*.json"): p.write_text(dump(json.loads(p.read_text()), GAP_FIELDS))


def cmd_export():
    entries, gaps, errs = check()
    if errs:
        for e in errs: print(e)
        sys.exit("not exported: fix the problems above")
    url = {e["id"]: e["url"] for e in entries}
    out_gaps = [{**g, "links": {n: t if t.startswith("http") else url[t] for n, t in g.get("links", {}).items()}} for g in gaps]
    m = meta()
    blob = json.dumps({"asof": m["updated"], "vocab": vocab(), "benchmarks": entries, "gaps": out_gaps},
                      ensure_ascii=False, separators=(",", ":"))
    blob = blob.replace("</", "<\\/")  # keep the payload from closing the script tag
    for page in [p for p in PAGES if p.exists()]:
        html, n = re.subn(r'(<script id="atlas-data" type="application/json">).*?(</script>)',
                          lambda mm: mm.group(1) + blob + mm.group(2), page.read_text(), count=1, flags=re.S)
        if n != 1: sys.exit(f"atlas-data script tag not found in {page.relative_to(ROOT)}")
        page.write_text(html)
        print(f"{len(entries)} entries, {len(gaps)} gaps, updated {m['updated']} -> {page.relative_to(ROOT)}")


if __name__ == "__main__":
    cmds = {"check": cmd_check, "stats": cmd_stats, "fmt": cmd_fmt, "export": cmd_export}
    a = sys.argv[1:]
    if a[:1] == ["new"] and len(a) == 2: cmd_new(a[1])
    elif len(a) == 1 and a[0] in cmds:
        ok = cmds[a[0]]()
        if ok is False: sys.exit(1)
    else: sys.exit(__doc__)
