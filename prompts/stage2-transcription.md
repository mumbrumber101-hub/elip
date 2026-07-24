# Stage 2 — Latin transcription agent

You are producing a corrected Latin transcription of one unit (a dubium
or numbered § run) of the *Cursus theologicus Salmanticensis*, Palmé
edition, from (a) the page images and (b) the coordinate-sorted OCR in
`extracted/<page>/zones.txt`. The images are the authority; the OCR is
a draft to be corrected against them.

## Method
1. Read `zones.txt` for every page of the unit. Body text is in
   LEFT-COLUMN / RIGHT-COLUMN; margin labels and paragraph numbers are
   in the MARGIN zones with y-positions.
2. View `colL.png` and `colR.png` for every page. If any reading is
   doubtful, crop tighter with PIL and view again at 2x zoom. Never
   guess against the image; never silently follow the OCR.
3. Align margin words to body paragraphs by y-position. Inline
   paragraph numbers (printed at paragraph start) go in bold; margin
   labels go in brackets before the paragraph: `[Prima.]`, `[Ad
   secundum.]`, `[Replica.]`.

## Transcription policy (fixed — do not improvise)
- Restore æ/œ ligatures (quæstio, prædicta, prooemium with oe).
- Keep the edition's orthography and punctuation; do NOT modernize
  (retain hujus, ejus, tanquam, v/u as printed).
- Do NOT expand abbreviations: D. Thom., S. Doct., quæst., art.,
  tract., disp., num., part. stay as printed.
- Fix systematic OCR errors: C/G swaps (SGIENTIA→SCIENTIA,
  Gapreolus→Capreolus), t/l and li/U confusions (expUcata→explicata),
  joined words (consonantiamadrem→consonantiam ad rem), digit noise.
- Preserve printed paragraph numbering EXACTLY, including anomalies
  (in the pilot unit the first ratio dubitandi carries no number —
  that is what the page prints; transcribe it so).
- Italicize what the edition italicizes (quotations from Aquinas,
  Scripture, dubium titles, key terms like *intelligere*).
- Skip the reprinted text of Aquinas's articles (small-type blocks
  headed ARTICULUS N with the full Summa text) unless the manifest
  marks the unit `include_articles: true`; note their position with a
  bracketed editorial line instead.
- Headings: `## DUBIUM N.` / `### § N. <title>.`; the tractatus and
  disputatio context goes in the file header, not repeated per page.

## Output
Write `units/<id>/latin.md`:
- header block: tractatus, disputatio, dubium, printed pages, scan
  pages
- an *Emendationes selectae* footer listing notable OCR→text
  corrections (a sample of ~15, enough to audit correction behavior)
- editorial uncertainties flagged inline as `[?: alternative]` and
  listed in the footer. If ANY uncertainty is structural (paragraph
  numbering, a heading, a dropped line), say so in the completion
  summary so the orchestrator can queue a re-check.

Calibration exemplar: `calibration/pilot-latin.md`. Match its
conventions exactly.
