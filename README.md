# Clean Code LMS

Course URL: https://pythonidaer.github.io/clean-code-lms/

A source-complete learning course for the **supplied 67-page Clean Code excerpt**, using the JSON and GraphQL LMS course model. It contains **8 modules, 21 guided lesson decks, 9 source-reference decks, 196 slides, 6 module quizzes with 23 questions, and an independent 12-question final assessment**.

## Curriculum

1. Orientation, publication details, navigation and scope
2. Care, maintenance, 5S, honest quality and design as repair
3. Knowledge, deliberate practice and heuristics in context
4. Precise requirements, messy-code economics, rewrite risk and responsibility
5. Code sense and the Stroustrup, Booch, Thomas, Feathers, Jeffries and Cunningham perspectives
6. Schools of thought, authorship, reader effort, the Boy Scout Rule and follow-up principles
7. Original JavaScript refactoring clinic and an evidence-based code review capstone
8. Every extracted source page in original order, including contents, credits, bibliography, index, footnotes and publisher offers

Guided lessons include objectives, source PDF page ranges, practice and worked checks. JavaScript examples and assessments were authored for the course; they are not missing book listings. Work on exercises in your own environment. The LMS does not execute arbitrary lesson code.

## Source scope

The uploaded PDF contains front matter, the foreword, the introduction, Chapter 1 (printed pages 1–15), and the full book index (printed pages 413–431). **It does not contain the later chapters named in the contents and index.** Index page numbers refer to the full book's printed pages, not this excerpt's PDF page numbers.

`docs/clean-code-extracted.txt` is the complete text previously extracted from the user-supplied PDF, preserving original order, headings and indentation. `source-manifest.json` maps each of the 67 pages to its lesson and slide, with exact text hashes, plus the guided topic coverage. The generated source-reference decks reproduce every page's text once. Text extraction does not reproduce illustrations or recover text embedded only in an image. Historical claims, opinions and cover-essay speculation are identified as such in guided lessons.

Original copyright and attribution notices remain in the source. See `THIRD_PARTY_NOTICES.md`. The source is not relabeled with the reference documentation's license.

## Theme

Solid navy, deep blue, pale light, lilac and ice blue colors were extracted from the supplied image. Primary/secondary text and links meet 4.5:1 contrast against the specified backgrounds; essential borders/focus meet 3:1. `docs/theme.md` records colors and validation scope. This does not claim blanket WCAG conformance.

## Use and maintain

No install or build step is needed to use the static course. Run `python3 -m http.server 8000`, then open http://localhost:8000 . Markdown rendering is packaged locally. All lessons and quizzes are open by default. Passing is 80%, retakes are allowed, and progress, notes, settings and reports are browser-local.

The outline collapses on all devices. Small screens have a menu for Course, Reporting and Settings. Copy entire course includes source text, exercises, quiz choices, correct answers and explanations, even if sections are collapsed or assessments are locked. Personal progress and notes are excluded; a manual-copy fallback appears if clipboard permission is unavailable.

To update authored material, edit `scripts/build-course.py`; to update the source, replace `docs/clean-code-extracted.txt` with a complete page-labeled extraction. Run `python3 scripts/build-course.py` to regenerate the course, embedded HTML and source manifest together. Keep IDs stable. The distinct Clean Code course ID isolates progress from the old Design foundations sample.

## Validation

Run `node tests/course.test.cjs` for exact 67-page coverage, source hashes, runtime readiness, course/HTML parity, fence integrity, assessment correctness, independent final prompts, palette contrast and behavior checks for the original lookup clinic.

With Playwright and Chromium installed, run `node tests/browser.test.cjs` for rendering, every source-page text, Markdown safety, responsive layouts, outline/menu, focus/contrast, notes, completion, reload persistence, quiz grading, reports, final gating and complete copy/manual fallback. Optional `CHROMIUM_EXECUTABLE` overrides the browser path; `LMS_SCREENSHOT_DIR` writes QA screenshots outside the repository.

There is no authentication, shared backend, verified certificate or exam-secure grading. Correct answers are delivered to the browser. Browser-local results are personal study feedback.
