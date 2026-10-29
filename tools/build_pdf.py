#!/usr/bin/env python
"""Wandelt Lernkarten (Markdown) in A4-PDFs um: Markdown -> HTML -> Chromium (via Playwright).

Aufruf (aus dem Repo-Root, in der Conda-Umgebung „codeclub“):
    conda activate codeclub
    python tools/build_pdf.py            # alle Lerneinheiten
    python tools/build_pdf.py 1 4        # nur Einheit 1 und 4
"""

import base64
import re
import sys
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Scratch"
OUT = ROOT / "pdf"
CSS = (Path(__file__).parent / "style.css").read_text(encoding="utf-8")
LOGO = ROOT / "medien" / "logo_196x196.png"
CHROMIUM = "/snap/bin/chromium"
UNITS_TOTAL = 8
MARGIN_LEFT = "18mm"
MARGIN_RIGHT = "12mm"
HEADER_TOP = "5mm"  # Mindestabstand zum oberen Rand fürs Drucken
LOGO_SIZE = "14mm"
FOOTER_PIC_HEIGHT = "10mm"
# Ein Bild pro Einheit, mittig in der Fußzeile jeder Seite
FOOTER_PICS = {
    "1": "scratch.png",
    "2": "diver.png",
    "3": "taco.png",
    "4": "arduino.png",
    "5": "repeat.png",
    "6": "bat.png",
    "7": "rocket.png",
    "8": "unicorn.png",
}

PAGE = """<!doctype html>
<html lang="de"><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>
{body}
</body></html>
"""


def to_html(md_text: str) -> str:
    html = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])

    def checklist(m: re.Match) -> str:
        items = re.findall(r"<li>(.*?)</li>", m.group(0), flags=re.S)
        if items and all(i.startswith("[ ]") for i in items):
            return re.sub(r"<li>\[ \]\s*", "<li>", m.group(0)).replace("<ul>", '<ul class="checklist">', 1)
        return m.group(0)

    # In ```diff-Blöcken neue (+) und entfernte (-) Zeilen hervorheben
    def diff_block(m: re.Match) -> str:
        cls = {"+": "add", "-": "del"}
        lines = [
            f'<span class="ln {cls.get(line[:1], "ctx")}">{line or " "}</span>'
            for line in m.group(2).rstrip("\n").split("\n")
        ]
        return m.group(1) + "".join(lines) + m.group(3)

    html = re.sub(r'(<pre><code class="language-diff">)(.*?)(</code></pre>)', diff_block, html, flags=re.S)
    return re.sub(r"<ul>.*?</ul>", checklist, html, flags=re.S)


def header_html() -> str:
    logo = base64.b64encode(LOGO.read_bytes()).decode()
    return (
        # Chromium rückt den Header-Bereich selbst ein; absolute Position macht den Abstand zum Blattrand eindeutig
        f'<div style="position:absolute; top:{HEADER_TOP}; left:0; width:100%; box-sizing:border-box;'
        f" padding:0 {MARGIN_RIGHT} 0 {MARGIN_LEFT};"
        " font-size:10pt; color:#62061f; display:flex; justify-content:space-between; align-items:center;"
        " font-family:'DejaVu Sans', sans-serif; font-weight:bold;\">"
        "<span>Code Club Wagh&auml;usel</span>"
        f'<img src="data:image/png;base64,{logo}" style="width:{LOGO_SIZE}; height:{LOGO_SIZE};">'
        "</div>"
    )


def footer_html(unit: str) -> str:
    pic = ""
    if unit in FOOTER_PICS:
        data = base64.b64encode((ROOT / "medien" / FOOTER_PICS[unit]).read_bytes()).decode()
        pic = f'<img src="data:image/png;base64,{data}" style="height:{FOOTER_PIC_HEIGHT};">'
    return (
        f'<div style="width:100%; box-sizing:border-box; padding:0 {MARGIN_RIGHT} 0 {MARGIN_LEFT};'
        " font-size:8pt; color:#555; display:flex; justify-content:space-between; align-items:center;"
        " font-family:'DejaVu Sans', sans-serif;\">"
        # Beide Textspalten gleich breit, damit das Bild genau in der Mitte steht
        f'<span style="flex:1;">Lerneinheit {unit} von {UNITS_TOTAL}</span>'
        f"{pic}"
        '<span style="flex:1; text-align:right;">Seite <span class="pageNumber"></span> von <span class="totalPages"></span></span>'
        "</div>"
    )


def build(page, md_file: Path) -> Path:
    md_text = md_file.read_text(encoding="utf-8")
    title = md_text.splitlines()[0].lstrip("# ").strip()
    unit = re.search(r"lerneinheit_(\d+)", md_file.stem).group(1)
    OUT.mkdir(exist_ok=True)
    pdf = OUT / md_file.with_suffix(".pdf").name
    page.set_content(PAGE.format(title=title, css=CSS, body=to_html(md_text)))
    page.pdf(
        path=str(pdf),
        format="A4",
        display_header_footer=True,
        header_template=header_html(),
        footer_template=footer_html(unit),
        margin={
            "top": "22mm",
            "bottom": "20mm",
            "left": MARGIN_LEFT,
            "right": MARGIN_RIGHT,
        },
    )
    return pdf


def main() -> None:
    nums = sys.argv[1:]
    files = [SRC / f"lerneinheit_{n}.md" for n in nums] if nums else sorted(SRC.glob("lerneinheit_[0-9]*.md"))
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROMIUM)
        page = browser.new_page()
        for f in files:
            print(f"{f.name} -> {build(page, f)}")
        browser.close()


if __name__ == "__main__":
    main()
