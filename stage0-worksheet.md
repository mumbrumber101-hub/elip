# Stage 0 record — structure verified 2026-07-24

**STATUS: COMPLETE.** All boundaries below were verified against page
images (five parallel verification passes over 180+ extracted pages,
plus two § split-point passes). `manifest.json` is the authoritative
output; this file records the verification evidence and conventions.

## Volume map (scan pages)

| Scan | Content |
|---|---|
| 1–6 | covers, blanks, half-title (7 = series half-title) |
| 7–104 | front matter: title pp., Praeloquium editoris (11+, 1870s editor — NOT translated), Approbationes & monita (15+, historical apparatus — not units by default) |
| 105–109 | **Prooemium & partitio totius Operis** (printed 1–5) — Salmanticenses' own text → unit t00-prooemium-operis |
| 110–113 | Aquinas Quaestio III De simplicitate Dei, arts. I–VIII, small type (skipped) |
| 114 | **Notationes circa omnes articulos q. 3** (printed 10) → unit t00-notationes-q03 |
| 115–194 | **Tractatus I** De principio individuationis (printed 11–90): Disp I (dub 1–5), Disp II (dub 1–3) |
| 195–418 | **Tractatus II** In q. 12, De visione Dei: Disp I–VII, 31 dubia; Aquinas arts. I–XIII interleaved in small type |
| 419–774 | **Tractatus III** In q. 14, De scientia Dei: prooemial dub. unicum (pilot) + Disp I–XII, 45 dubia; Aquinas arts. I–XVI interleaved |
| 775–779 | Index tractatuum, disputationum et dubiorum (printed ~671–675) |
| 780–788 | back matter/covers (788 = marbled board) |

## Fixed facts
- 788 scan pages (djvused verified). Printed page = scan − 104,
  constant for the whole body (checked at 10+ points; index folios
  agree everywhere).
- Body text ends scan 774 (printed 670) with tailpiece after
  Aquinas arts. XIV–XVI.

## Conventions adopted (and why)
1. **Catchwords**: this edition reprints the next page's heading at
   the column foot. Every OCR "duplicate heading" (260/261, 598/599,
   686/687; § I at 284; § V at 178) was a catchword; the real heading
   is always on the later page. Watch for this in Stage 2.
2. **Running heads anticipate**: on disputatio-opening pages the head
   may already read "DUB. I" (703, 755) — heads never used alone to
   place a boundary.
3. **Splits**: dubia ≥10 printed pages split at image-verified §
   boundaries (mid-page § → both parts list the split page;
   column-top § → page belongs to later part). 9-page dubia kept
   single: t01-d02-dub03, t03-d05-dub02.
4. **Aquinas articles** (small type) skipped per runbook; the brief
   large-type "Conclusio" tags attached to them are treated as part
   of the article apparatus (not units). The substantial per-question
   Notationes/Animadversio blocks ARE units (t00-notationes-q03,
   t02-intro-q12).
5. **Pilot id kept**: t03-d01-dub-unicum retained although the print
   has no DISPUTATIO heading there (the dubium hangs off the
   Quaestio XIV prooemium; printed Disp. I begins scan 422 and is
   t03-d01-dub01…). Noted in the unit.

## Discrepancies found (images authoritative)
- Index lists T3-D1 dub 3 at fol. 322; image shows printed 332
  (scan 436). Index typo.
- Index titles T2 Disp V "De aequalitate…"; the disputatio heading
  on scan 354 reads "De qualitate, et inaequalitate visionum in
  beatis." Body reading adopted.
- Seed OCR misses corrected by image passes: T2-D5 dub 1 (scan 354),
  Aquinas art. X (scan 415), T3 Disp VII heading (scan 572), T3-D10
  dub 3 (scan 726), T3-D12 dub 4 (scan 771), and ~12 § headings.

## Counts
- 84 dubia (8 + 31 + 45) + 3 own-text intro units = 87 texts.
- After splits: **121 units** (120 pending, 1 reviewed pilot).
- Translatable body ≈ scan 105–774 minus article blocks ≈ 650
  printed pages.

## For Jon
- Decide whether the Approbationes & monita (scan 15–104) and the
  1870s Praeloquium editoris should ever become units (currently
  excluded; public-domain either way).
- Two 9-page dubia kept unsplit — flag if you prefer stricter ~8.
- include_articles is false everywhere; flip per unit to pull in the
  Aquinas reprints later.
