# Stage 3 — Translation agent

You are translating one unit of the *Cursus theologicus
Salmanticensis* from the corrected Latin in `units/<id>/latin.md` into
scholarly English.

## Inputs you must load first
1. `glossary.md` — locked renderings. These BIND you. If a technical
   term is absent from the glossary, choose a rendering consistent
   with its principles, use it consistently within the unit, and list
   it under "Glossary candidates" in your completion summary so it can
   be adjudicated and added.
2. `calibration/pilot-english.md` — the register exemplar. Match it.
3. The final two paragraphs of the PRECEDING unit's `english.md`
   (if it exists) — for continuity of register and running references.

## Translation policy
- Complete rendering: every sentence, every connective particle (nam,
  etenim, quare, propterea, quandoquidem, nihilominus). Omission is
  the cardinal failure. Never summarize, never compress.
- Latin periods may be divided for English readability, but never
  across an argumentative joint (licet/nihilominus,
  antecedent/consequent, probatur structure).
- *Ratio* is rendered contextually per the glossary; supply the Latin
  in parentheses when load-bearing.
- Retain ad extra, esse, and other glossary-flagged Latin terms in
  italics.
- Structural labels: DUBIUM stays "Dubium" ("Sole Dubium" for
  unicum); § headings translated.
- Margin apparatus: keep the bracketed labels `[First.]`,
  `[To the second.]`, `[Rejoinder.]`, `[Solution.]` and bold printed
  paragraph numbers, mirroring the Latin file one-for-one.
- Scripture and Aquinas quotations in italics; identify Scripture
  sources in a bracketed note ONLY when certain; otherwise flag for
  review.
- No modernizing paraphrase of scholastic machinery; the reader wants
  the machinery. No em-dash decoration beyond what clarity requires;
  CMS 16 conventions; ". . ." spaced ellipses.

## Output
Write `units/<id>/english.md` mirroring the Latin file's structure
exactly (same headings, same paragraph breaks, same bracket labels).
Header block carries the same locators plus a one-line translator's
note only if the unit forced a nonobvious rendering decision.

Completion summary must list: (a) glossary candidates, (b) passages
flagged for review with reasons, (c) any place you divided a Latin
period, with the joint checked.
