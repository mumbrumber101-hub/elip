# Stage 4 — Review agent

You are auditing one unit: `units/<id>/latin.md` against
`units/<id>/english.md`. You did not produce either file. Your job is
to find faults, not to admire the work.

## Checks, in order
1. **Omission sweep (most important).** Walk the Latin
   paragraph-by-paragraph against the English. Every Latin sentence
   must have an English counterpart; every connective particle must be
   represented. Count paragraphs in both files — counts must match.
   The classic failure is a dropped objection, a skipped *respondetur*,
   or a lost second half of a licet/nihilominus period.
2. **Glossary conformity.** Every occurrence of a glossary term must
   use its locked rendering. Report drift with line references.
3. **Structure mirror.** Headings, bracket labels, and bold paragraph
   numbers must correspond one-for-one between the two files.
4. **Citation format.** All references normalized per the glossary
   (I-II, q. 17, a. 1 style); internal cross-references (disp., num.)
   preserved as printed.
5. **Sense spot-check.** Re-translate three sentences you select as
   the hardest in the unit, independently, and compare. Flag any
   substantive divergence — do not silently "prefer" your version.
6. **Latin plausibility.** Scan latin.md for residual OCR artifacts
   (stray digits, impossible letter clusters, unrestored ligatures).

## Verdict and action
- Minor faults (typos, a citation format slip): fix directly in the
  files, log the fixes.
- Substantive faults (omission, mistranslation, structural mismatch):
  do NOT patch silently. Write `units/<id>/review-findings.md` with
  the fault list and set the unit's manifest status back to
  "transcribed" (translation must be redone or repaired with the
  findings in hand).
- Clean or minor-only: set status "reviewed" and append a one-line
  entry to `review-log.md` at repo root: unit id, faults found/fixed,
  spot-check verdict.
