#!/usr/bin/env python3
"""Stage 1 — mechanical extraction from the DjVu.

For each requested page, produces in <outdir>/<page>/:
  page.png        full page render, 300 dpi
  colL.png        left-column crop (with left margin)
  colR.png        right-column crop (with right margin)
  zones.txt       column-sorted, margin-peeled OCR text (see below)

zones.txt separates the embedded OCR layer into four x-zones using
djvused word coordinates: LEFT-MARGIN | LEFT-COLUMN | RIGHT-COLUMN |
RIGHT-MARGIN. Margin words are printed with their y-position so the
transcription agent can align labels/numbers to body paragraphs.
This is the key trick discovered in the pilot: the plain `djvutxt`
stream interleaves marginalia into body text; coordinates peel them.

Usage:
  python3 scripts/extract.py 01.djvu --pages 419-435
  python3 scripts/extract.py 01.djvu --pages 420,421,422 --outdir extracted

Requires: djvulibre-bin (djvused, ddjvu), Pillow.
"""
import argparse, re, subprocess, sys
from pathlib import Path
from PIL import Image

# x-zone boundaries as fractions of page width; tuned on the Palme
# edition of the Cursus theologicus. Adjust if a volume differs.
LMARGIN_LT, GUTTER, RMARGIN_GT = 0.13, 0.505, 0.875


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"command failed: {' '.join(cmd)}\n{r.stderr}")
    return r.stdout


def page_size(djvu, page):
    out = run(["djvused", str(djvu), "-e", f"select {page}; size"])
    m = re.search(r"width=(\d+)\s+height=(\d+)", out)
    return int(m.group(1)), int(m.group(2))


def words_with_coords(djvu, page):
    """Parse djvused print-txt s-expression into (x1,y1,x2,y2,text)."""
    out = run(["djvused", str(djvu), "-e", f"select {page}; print-txt"])
    words = []
    for m in re.finditer(r'\(word (\d+) (\d+) (\d+) (\d+) "((?:[^"\\]|\\.)*)"', out):
        x1, y1, x2, y2 = (int(m.group(i)) for i in range(1, 5))
        raw = m.group(5)
        # djvused escapes non-ASCII as octal; decode defensively
        try:
            text = raw.encode("latin-1", "replace").decode("unicode_escape")
            text = text.encode("latin-1", "replace").decode("utf-8", "replace")
        except Exception:
            text = raw
        words.append((x1, y1, x2, y2, text))
    return words


def group_lines(words, y_tol=18):
    """Group words into lines by y proximity, sort top-to-bottom.
    djvused y-origin is bottom-left, so 'top' = max y."""
    lines = []
    for w in sorted(words, key=lambda t: (-t[3], t[0])):
        for line in lines:
            if abs(line[0] - w[3]) <= y_tol:
                line[1].append(w)
                break
        else:
            lines.append([w[3], [w]])
    out = []
    for ytop, ws in sorted(lines, key=lambda l: -l[0]):
        ws.sort(key=lambda t: t[0])
        out.append((ytop, " ".join(t[4] for t in ws)))
    return out


def extract_page(djvu, page, outdir, dpi=300):
    pdir = outdir / f"{page:03d}"
    pdir.mkdir(parents=True, exist_ok=True)

    # 1. render
    pgm = pdir / "page.pgm"
    run(["ddjvu", "-format=pgm", f"-page={page}", f"-scale={dpi}",
         str(djvu), str(pgm)])
    im = Image.open(pgm)
    im.save(pdir / "page.png")
    W, H = im.size
    im.crop((0, 0, int(W * 0.56), H)).save(pdir / "colL.png")
    im.crop((int(W * 0.46), 0, W, H)).save(pdir / "colR.png")
    pgm.unlink()

    # 2. coordinate-sorted OCR zones
    nw, nh = page_size(djvu, page)  # native coordinate space
    zones = {"LEFT-MARGIN": [], "LEFT-COLUMN": [],
             "RIGHT-COLUMN": [], "RIGHT-MARGIN": []}
    for w in words_with_coords(djvu, page):
        cx = (w[0] + w[2]) / 2 / nw
        if cx < LMARGIN_LT:
            zones["LEFT-MARGIN"].append(w)
        elif cx < GUTTER:
            zones["LEFT-COLUMN"].append(w)
        elif cx < RMARGIN_GT:
            zones["RIGHT-COLUMN"].append(w)
        else:
            zones["RIGHT-MARGIN"].append(w)

    with open(pdir / "zones.txt", "w", encoding="utf-8") as f:
        f.write(f"# page {page} | native {nw}x{nh} | render {W}x{H}\n")
        for zone in ("LEFT-MARGIN", "LEFT-COLUMN",
                     "RIGHT-COLUMN", "RIGHT-MARGIN"):
            f.write(f"\n== {zone} ==\n")
            marg = "MARGIN" in zone
            for ytop, text in group_lines(zones[zone]):
                if marg:
                    f.write(f"[y={ytop / nh:.3f}] {text}\n")
                else:
                    f.write(text + "\n")
    print(f"page {page}: ok")


def parse_pages(spec):
    pages = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            pages.extend(range(int(a), int(b) + 1))
        else:
            pages.append(int(part))
    return pages


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("djvu")
    ap.add_argument("--pages", required=True,
                    help="e.g. 419-435 or 420,421,422")
    ap.add_argument("--outdir", default="extracted")
    args = ap.parse_args()
    outdir = Path(args.outdir)
    for p in parse_pages(args.pages):
        extract_page(Path(args.djvu), p, outdir)
