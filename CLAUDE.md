# Salmanticenses Translation Pipeline — Runbook

Goal: a complete, reviewed English translation of the *Cursus
theologicus Salmanticensis*, Tome I (788-page DjVu scan, Palmé
edition), assembled into a typeset PDF. The pipeline is
manifest-driven and resumable: every unit's state lives on disk, so
any session can pick up exactly where the last one stopped.

## Setup (once)
1. Place the scan at repo root as `01.djvu` (it is NOT in this kit —
   Jon supplies it).
2. `sudo apt-get install -y djvulibre-bin pandoc texlive-xetex texlive-fonts-extra`
3. `pip install pillow`
4. Verify: `djvused 01.djvu -e n` → should print 788.

## Pipeline state
`manifest.json` at repo root is the single source of truth. Schema:

```json
{
  "volume": "tome-1",
  "units": [
    {
      "id": "t03-d01-dub-unicum",
      "tractatus": "III De scientia Dei",
      "disputatio": "I (prooemialis)",
      "dubium": "unicum",
      "title": "Utrum ea quae D. Thom. in Prooemio hujus quaestionis docet, sint vera",
      "scan_pages": [419, 422],
      "printed_pages": "315-318",
      "include_articles": false,
      "status": "reviewed",
      "notes": "pilot unit; done in chat 2026-07-24"
    }
  ]
}
```

Statuses: `pending → extracted → transcribed → translated → reviewed`.
A Stage 4 substantive fault resets a unit to `transcribed` and leaves
`review-findings.md` in its directory.

## Stage 0 — build the manifest (first session)
1. `python3 scripts/seed_manifest.py 01.djvu > manifest.seed.json`
   (takes a few minutes; scans all 788 pages).
2. From the seed, reconstruct the volume structure: tractatus →
   disputatio → dubium with scan-page ranges. Verify EVERY boundary
   against page images (`scripts/extract.py` on the boundary page,
   then view the PNG) — OCR mangles headings (UNIGUM, YIII, TRAGT).
   Also render the volume's index pages (front or back matter) and
   cross-check against them.
3. Unit granularity: one unit per dubium. Split a dubium longer than
   ~8 printed pages at a § boundary into `-a`, `-b` parts. Never split
   inside a §.
4. The pilot unit above is already done: copy
   `calibration/pilot-latin.md` and `calibration/pilot-english.md`
   into `units/t03-d01-dub-unicum/` as `latin.md` / `english.md`, and
   enter it with status `reviewed`.
5. Write `manifest.json`. Report the unit count and total page count
   to Jon before proceeding.

## Stages 1–4 — the unit loop
For each pending unit (process in manifest order; batches of ~10–20
units per session are comfortable):

1. **Extract**: `python3 scripts/extract.py 01.djvu --pages A-B`
   → status `extracted`.
2. **Transcribe**: run a subagent with `prompts/stage2-transcription.md`
   plus the unit's extracted files → `units/<id>/latin.md`, status
   `transcribed`. The subagent must actually VIEW the column images;
   transcription from OCR alone is forbidden.
3. **Translate**: run a subagent with `prompts/stage3-translation.md`,
   `glossary.md`, the unit Latin, and the tail of the previous unit's
   English → `units/<id>/english.md`, status `translated`. Collect its
   glossary candidates into `glossary-candidates.md` at root.
4. **Review**: run a DIFFERENT subagent with
   `prompts/stage4-review.md` → status `reviewed` (or reset per its
   verdict).

Concurrency: units are independent; up to ~5 parallel unit-loops are
fine. Keep the manifest write atomic (read-modify-write one unit at a
time). If a session is interrupted mid-unit, the status field says
what to redo; redo the whole stage, never resume a half-written file.

## Working rules
- Images are the textual authority; OCR is a draft. When in doubt,
  crop tighter and view at 2x (see `calibration/` for the standard).
- Margin apparatus comes pre-peeled in `zones.txt` via word
  coordinates; align labels to paragraphs by y-position.
- Aquinas's reprinted articles (small type) are skipped by default;
  the translation covers the Salmanticenses' own text. Jon may flip
  `include_articles` per unit later.
- The glossary binds every translation. New technical terms go to
  `glossary-candidates.md`, never into ad-hoc circulation.
- Public-domain source; no copyright constraints.
- Periodically (every ~25 units) surface to Jon: unit count done,
  glossary candidates awaiting ruling, any structural surprises.

## Stage 5 — assembly
Draft builds any time: `python3 scripts/assemble.py --any --draft`.
Final build (reviewed units only): `python3 scripts/assemble.py`.
Output: `final/salmanticenses-t1.pdf`. Template:
`templates/main.tex` (XeLaTeX, EB Garamond, teal-slate #264653
headings, CMS 16: spaced ellipses ". . .", no AI-tic prose anywhere
in front matter).

## What Jon reviews
- Glossary rulings: `glossary.md` ⚑ items + `glossary-candidates.md`.
- Spot-checks: sample ~5% of units per tractatus; `review-log.md`
  lists each unit's audit result to guide sampling.
