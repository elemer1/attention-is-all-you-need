"""Copy site/data/*.json into the <script type="application/json"> blocks of site/index.html,
so the page works as a single file. Run after ablations.py / export_attention.py."""
import re
from pathlib import Path

site = Path(__file__).resolve().parent.parent / "site"
page = site / "index.html"
html = page.read_text(encoding="utf-8")
for name in ("ablations", "attention"):
    data = (site / "data" / f"{name}.json").read_text(encoding="utf-8").replace("</", "<\\/")
    pat = re.compile(rf'(<script id="data-{name}" type="application/json">)(.*?)(</script>)', re.S)
    assert pat.search(html), f"missing data-{name} block"
    html = pat.sub(lambda m: m.group(1) + data + m.group(3), html)
page.write_text(html, encoding="utf-8")
print("inlined into", page)
