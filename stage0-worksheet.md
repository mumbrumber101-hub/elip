# Stage 0 worksheet — structure reconstruction

**STATUS: text-layer analysis done; image verification IN PROGRESS.**
`01.djvu` verified present (788 pages). Running-head sweep of the OCR
layer confirms the skeleton below; image verification of every
boundary is underway. Confirmed so far from the text layer:

- Printed page = scan page − 104, constant across the body (checked
  at scan 117, 121, 199, 305, 423, 703, 757).
- Tome I contains Tractatus I–III (editor's preface, scan 13):
  Tract. II De visione Dei, Tract. III De scientia Dei; Tract. I
  title reads (OCR) "De principio individuationis substantiae
  materialis, et accidentium ejus" — confirm on images of 13/114/115.
- Front matter: title pages ~7–9, Praeloquium editoris 11+,
  Approbationes & monita 15+, general prooemium ~105–109.
- Missed headings found by loose re-sweep: T2-D4 Dub III p335
  ("DUBTUM"), T3-D1 Dub II p425, T3-D10 Dub V p736 / VI p738,
  T3-D12 Dub IV p771; T3-D10 Dub III begins ~p726 (running heads
  flip DUB.II→DUB.III between 725 and 727).
- Running heads confirm T3 Disp VII exists (p577 head) though its
  heading page (~572–573) needs image confirmation; T2-D5 Dub I
  still unlocated (354–355) — image check.

## Gross layout (provisional)

| Scan pages | Content |
|---|---|
| 1–109 | Front matter + (?) start of volume — **no headings detected**; suspicious gap, must be inspected |
| 110–113 | ARTICULUS I–VII block (Aquinas reprint, small type) |
| 114–194 | TRACTATUS heading (number unreadable) — Disp I–II |
| 195–413 | TRACTATUS heading — Disp I–VII (matches index's Tract. II) |
| 414–418 | ARTICULUS IX–XIII block |
| 419–772 | TRACTATUS III *De scientia Dei* (pilot unit confirms 419) — prooemial disp. + Disp I–XII |
| 773–774 | ARTICULUS XIV–XVI block |
| 775–778 | Volume index |
| 779–788 | Back matter (?) — no headings detected |

## Detected dubium boundaries (scan pages)

### Tractatus at 114/115 (identity unresolved — index says Tract. I has only Disp. I, but body shows two disputations here)
- Disp I (115): Dub I 115, II 126, III 138, IV 153, V 156
- Disp II (168): Dub I ~169 (heading missed; inferred from "…dubium hoc sigillatim excitamus"), II 174, III 186

### Tractatus at 195 (likely Tract. II)
- Disp I (197): Dub I 197, II 203, III 207, IV 214, V 218
- Disp II (223): Dub I 223, II 229, III 244, IV 256, V 260 **and** 261 (duplicate — check which is the heading), VI 268, VII 270, VIII 280, IX 284, X 292
- Disp III (306): Dub I 306, II 310
- Disp IV (323): Dub I 324, II 330, III ~335 (heading missed), IV 339, V 346
- Disp V (354): **Dub I heading missing** (~354), II 356, III 362
- Disp VI (371): Dub unicum 371
- Disp VII (383): Dub I 383, II 385, III 393, IV 398, V 404

### Tractatus III De scientia Dei (419)
- Disp prooemialis: Dub unicum 420 — **pilot unit, done (419–422)**
- Disp I (422): Dub I 422, **II missing** (between 422 and 436), III 436, IV 443
- Disp II (454): Dub I 454, II 472
- Disp III (491): Dub I 491 ("DUBIUM T"), II 496
- Disp IV (507): Dub I 507, II 518
- Disp V (535): Dub I 535, II 537, III 546
- Disp VI (564): Dub I 564, II 565
- Disp VII: **heading missing** (~571–573, after Articulus XIII): Dub I 573, II 574, III 581, IV 588, V 598 **and** 599 (duplicate), VI 604
- Disp VIII (628): Dub I 628, II 640, III 652, IV 671
- Disp IX (678): Dub I 678, II 680, III 686/687 (duplicate), IV 690, V 695
- Disp X (703): Dub I 704, II 714, **III missing**, IV 732, **V–VI missing**, VII 742 ("DUBIUM VI l"), VIII 752
- Disp XI (755): Dub I 756, II 761
- Disp XII (766): Dub I 766, II 766, III 770

## Index cross-check (OCR of scan 775–778)
- Tract. I: Disp I only ← conflicts with two disputations found at 115/168
- Tract. II: Disp I–V, VII listed (VI likely OCR-missed; body has VI at 371)
- Tract. III: Disp I–III, V–VIII, XI listed (IV, IX, X, XII likely OCR-missed; body has all)

## Must-verify list (image checks required, in addition to every boundary)
1. Pages 1–109: locate Tract. I start, any disputatio/dubium structure, front-matter extent.
2. Identity of the tractatus at 114/115 vs the index's Tract. I/II division.
3. Duplicate DUBIUM V at 260/261, 598/599; DUBIUM III at 686/687 — pick true headings.
4. Missing headings: T2-D4 Dub III (~335), T2-D5 Dub I (~354), T3-D1 Dub II (422–436), T3-D7 heading (~571–573), T3-D10 Dub III/V/VI (714–742).
5. False positives: TRACTATUS at 584 and DISPUTATIO/DUBIUM hits that are running text (e.g. 420, 455, 491–492, 643, 680, 684) — confirm and discard.
6. Pages 779–788: identify back matter.
7. Printed-page ↔ scan-page offset (pilot gives scan 419–422 = printed 315–318, i.e. offset ~104; confirm it is constant).

## Provisional counts (if the seed is roughly right)
~66 dubia detected + ~7 known-missing ⇒ ~73 dubia before length-based
`-a`/`-b` splits; final unit count will exceed this once long dubia
(e.g. T3-D2 Dub II spans 472–491, ~19 scan pages) are split at §
boundaries.
