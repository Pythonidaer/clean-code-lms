# Reading-first LMS content guidelines

Chapter 1 is the preservation-first pilot. Learners read sections and take the chapter quiz at the end. There is no coding editor or per-slide Feynman toggle.

## Slide boundaries

- Give each slide one specific teaching point and an informative title.
- Split at a change in claim, explanation, example, perspective or qualification. Do not slice text solely to satisfy a character count.
- Aim for 60–120 words of self-contained prose. Review slides above 150 words. Shorter slides are appropriate for introductions, quotes and figures; do not add filler to meet a minimum.
- Keep necessary context and supporting examples near the idea they explain. Do not shrink text to fit.
- Preserve source order and substantive qualifications. Source assertions remain the author's perspective, not automatically universal modern guidance.
- Use nested outline groups for genuine subtopics. All groups start closed; explicitly opened groups retain their browser-local state.
- End a chapter with reflection and its quiz. Quiz alternatives should represent plausible misunderstandings; feedback should explain the reasoning.

## Preservation and maintenance

The pilot changes segmentation and titles rather than rewriting the book. Source Markdown and chapter units remain unchanged, including historical examples, anecdotes and footnotes. Some extraction artifacts therefore remain candidates for a separate editorial pass.

Edit `scripts/chapter-one-flow.py` to change Chapter 1 boundaries. Each anchor is an exact source phrase. Assertions reject missing, ambiguous or reordered anchors. `docs/chapter-one-slide-map.json` records source units/pages, subheadings, slide IDs, character ranges within each subheading and word counts. It is generated, not edited by hand.

Run `python3 scripts/build-course.py`, then `node tests/course.test.cjs`. Exact ordered normalized-text comparison verifies preservation, and the Chapter 1 word budget is checked. Run `node tests/browser.test.cjs` with Playwright and Chromium available to check rendering and nested navigation.

## Review locally

1. Run `python3 -m http.server 8000` from the repository root.
2. Open http://localhost:8000 . Expand Chapter 1, then The Total Cost of Owning a Mess.
3. Try the nested perspectives and slide arrows at desktop and mobile widths.
4. Read There Will Be Code and We Are Authors, then take the chapter quiz.
5. Judge whether each title describes its passage, each split feels natural, and essential context remains understandable.

Existing progress in changed Chapter 1 decks resets because the runtime fingerprints lesson content. Other chapters retain their content and IDs. Previous notes on changed decks may not be restored; copy important Chapter 1 notes before testing with the same browser/origin, or use a separate browser profile.
