# Lernmaterial – Code Club Waghäusel

Dieses Repository enthält frei nutzbares Lernmaterial für den Code Club Waghäusel. Alle Materialien sind auf Deutsch.

## Inhalt

### Scratch

Im Ordner [`Scratch/`](Scratch/) liegt ein Curriculum für Scratch 3.0 aus Lernkarten:

- **Zielgruppe:** Kinder ab ca. 11 Jahren, auch ohne Vorkenntnisse
- **Umfang:** 8 Lerneinheiten
- **Sozialform:** Einzelarbeit mit Betreuung durch Mentorinnen und Mentoren
- **Plattform:** [scratch.mit.edu](https://scratch.mit.edu) oder Scratch Desktop (offline)

Die Einheiten bauen aufeinander auf. Eine Übersicht mit Konzepten und Lernzielen steht in [`Scratch/lerneinheiten.md`](Scratch/lerneinheiten.md). Die einzelnen Lernkarten heißen `lerneinheit_1.md` bis `lerneinheit_8.md`.

## Wie wird mit den Lernkarten gearbeitet?

- Die Kinder arbeiten die Lernkarte selbstständig am Computer durch.
- Die Lernkarten enthalten sogenannte Mentorenmomente, in denen die Kinder und Jugendlichen Ihre Erkenntnisse mit den Mentorinnen und Mentoren besprechen.
- Mentorinnen und Mentoren zeigen nicht einfach die Lösung auf, sondern versuchen die Kinder und Jugendlichen durch Fragen und Hinweise darin zu unterstützen, selbst auf die Lösung zukommen.

## PDFs erzeugen

Die Lernkarten lassen sich als A4-PDFs (Hochformat) ausgeben. Voraussetzung sind Miniconda (oder Anaconda) und Chromium (Snap-Installation unter `/snap/bin/chromium`).

```
conda create -n codeclub python
conda activate codeclub
pip install -r tools/requirements.txt
python tools/build_pdf.py        # alle Einheiten
python tools/build_pdf.py 1 4    # nur Einheit 1 und 4
```

Die PDFs landen im Ordner `pdf/`. Das Aussehen wird in `tools/style.css` festgelegt, Logo, Kopf- und Fußzeile in `tools/build_pdf.py`.

## Mitmachen

Verbesserungsvorschläge und Korrekturen sind willkommen, zum Beispiel über Issues oder Pull Requests.

## Lizenz

Dieses Repository steht unter der [GNU General Public License v3.0](LICENSE). Kurz gesagt:

- Du darfst das Material frei nutzen, kopieren und weitergeben.
- Du darfst es verändern und anpassen.
- Veränderte Versionen musst du unter derselben Lizenz (GPL-3.0) veröffentlichen.
- Es gibt keine Gewährleistung.

Den vollständigen Lizenztext findest du in der Datei [LICENSE](LICENSE).
