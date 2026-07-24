#!/usr/bin/env python3
"""Stage 0 helper — scan the whole volume's OCR layer for structural
headings (TRACTATUS / DISPUTATIO / DUBIUM / ARTICULUS / QUAESTIO) and
emit manifest.seed.json: a candidate unit list with page anchors.

This is a SEED, not the manifest. OCR mangles headings (UNIGUM for
UNICUM, YIII for VIII, § misreads); the Stage 0 agent must verify each
boundary against page images, fix titles, merge false positives, and
write the authoritative manifest.json (schema in CLAUDE.md).

Usage: python3 scripts/seed_manifest.py 01.djvu > manifest.seed.json
"""
import json, re, subprocess, sys

HEAD = re.compile(
    r"\b(TRA[CG]TATUS|DISPUTATIO|DUBIUM|ARTI[CG]ULUS|QU[AE]STIO)\b[\s.]*"
    r"([IVXLY]+|UNI[CG]UM|PRIMU[SM]|SE[CG]UNDU[SM]|TERTIU[SM])?", re.I)


def npages(djvu):
    out = subprocess.run(["djvused", djvu, "-e", "n"],
                         capture_output=True, text=True).stdout
    return int(out.strip())


def page_text(djvu, page):
    return subprocess.run(
        ["djvutxt", djvu, f"--page={page}"],
        capture_output=True, text=True).stdout


def main(djvu):
    hits = []
    for p in range(1, npages(djvu) + 1):
        for line in page_text(djvu, p).splitlines():
            clean = "".join(ch for ch in line if ch.isprintable()).strip()
            m = HEAD.search(clean)
            # heading lines are short; filters running heads & prose refs
            if m and len(clean) < 40:
                hits.append({"scan_page": p, "raw": clean,
                             "kind": m.group(1).upper()})
        if p % 100 == 0:
            print(f"scanned {p} pages", file=sys.stderr)
    json.dump({"note": "SEED ONLY - verify every boundary against images",
               "headings": hits}, sys.stdout, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main(sys.argv[1])
