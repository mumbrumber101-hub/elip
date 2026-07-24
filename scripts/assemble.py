#!/usr/bin/env python3
"""Stage 5 — assemble reviewed English units into one XeLaTeX document.

Walks manifest.json in order, collects units/<id>/english.md for every
unit with status "reviewed" (use --any to include earlier statuses for
draft builds), converts each with pandoc, and wraps the result in
templates/main.tex. Then compiles with xelatex (two passes for TOC).

Usage:
  python3 scripts/assemble.py                 # reviewed units only
  python3 scripts/assemble.py --any --draft   # everything translated so far

Requires: pandoc, texlive-xetex, texlive-fonts-extra (EB Garamond).
"""
import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def md_to_tex(md_path):
    r = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "latex", "--wrap=none",
         "--top-level-division=section", str(md_path)],
        capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"pandoc failed on {md_path}:\n{r.stderr}")
    return r.stdout


def main(only_reviewed, draft):
    manifest = json.loads((ROOT / "manifest.json").read_text())
    body, skipped = [], []
    for u in manifest["units"]:
        ok = (u["status"] == "reviewed") if only_reviewed else \
             (u["status"] in ("translated", "reviewed"))
        md = ROOT / "units" / u["id"] / "english.md"
        if ok and md.exists():
            body.append("% ==== unit: " + u["id"] + " ====\n" + md_to_tex(md))
        else:
            skipped.append(u["id"])
    if skipped:
        print(f"skipped {len(skipped)} units: {', '.join(skipped[:8])}"
              + (" ..." if len(skipped) > 8 else ""), file=sys.stderr)

    template = (ROOT / "templates" / "main.tex").read_text()
    stamp = "DRAFT — unreviewed units included" if draft else ""
    tex = template.replace("%%BODY%%", "\n\n".join(body)) \
                  .replace("%%DRAFTSTAMP%%", stamp)
    out = ROOT / "final"
    out.mkdir(exist_ok=True)
    (out / "salmanticenses-t1.tex").write_text(tex)
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode",
                            "salmanticenses-t1.tex"], cwd=out,
                           capture_output=True, text=True)
    pdf = out / "salmanticenses-t1.pdf"
    print(f"wrote {pdf}" if pdf.exists()
          else "xelatex failed - see final/salmanticenses-t1.log")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--any", action="store_true",
                    help="include translated-but-unreviewed units")
    ap.add_argument("--draft", action="store_true",
                    help="stamp the build as a draft")
    a = ap.parse_args()
    main(only_reviewed=not a.any, draft=a.draft)
