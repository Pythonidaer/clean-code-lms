# Clean Code LMS

Live course: https://pythonidaer.github.io/clean-code-lms/

A chapter-based course: **14 core chapters, one optional advanced chapter, 131 source-subsection decks, 172 total decks, 605 slides, 15 chapter quizzes with 75 questions, and an independent 20-question core final.**

## Curriculum

- Core: Chapters 1–12, 14 Successive Refinement, and 17 Smells and Heuristics.
- Advanced optional: Chapter 13 Concurrency. It does not supply core final questions or block the final completion gate.
- Deferred: Chapters 15 JUnit Internals and 16 Refactoring SerialDate. Their Markdown files are ready, but not loaded into the LMS.
- Separate index: PDF pages 444–462 are in docs/index.md and are not loaded, copied or assessed by the LMS.

## Documentation and scope

docs/chapters contains all 17 chapter Markdown files. docs/table-of-contents.md retains PDF 8–19 as the structural reference. docs/preparation-checklist.md records chapter roles and work. source-manifest.json records hashes, source ranges, all heading matches and subsection mappings.

Actual Chapter 1 starts on PDF 32. Chapter source is extracted from **32–345**. Introduction and cover material at 26–31 are excluded, along with publication pages 1–7, foreword 20–25 and pages 346–443. No appendices, epilogue, index lessons or publication trivia enter the curriculum. Bibliographies remain in chapter Markdown where within scope, but are not taught or assessed.

The chapter and subsection explanations and code provide the lessons. Running headers, blank notices, chapter-opening artwork and portraits are omitted. Seven explanatory figures are retained. Source code is fenced as text because the book contains multiple languages and historical APIs. Long listings are labeled ordered continuations, not standalone runnable programs. Extraction is a transcription, not a verified compilation.

Goals, practice, worked checks and assessments are authored separately. They test programming concepts and decisions rather than dedication, publisher or acknowledgment facts. Historical Java-specific recommendations remain separate from general design ideas; the course does not present every author recommendation as a universal rule for modern JavaScript.

## Use and maintain

No install or build is needed to use the static site. Run python3 -m http.server 8000 and open http://localhost:8000 . Markdown rendering and teaching figures are packaged locally.

All content is open by default. Passing is 80%; retakes are enabled. Notes, progress, settings and reports are browser-local. Copy entire course includes the loaded lessons, code, choices, answers and explanations, excluding personal notes, the index and deferred chapters. A manual fallback supports blocked clipboard permissions. The course ID separates this curriculum from previous placeholders and the rejected excerpt.

1. Source preparation: run scripts/extract-chapters.py with the absolute PDF path in an environment containing PyMuPDF and Poppler. The PDF is not committed.
2. Edit authored goals and assessments in scripts/study-material.py.
3. Run python3 scripts/build-course.py to synchronize course.json, embedded index.html, mappings and stats. This step uses only the standard library.

Preserve the owner's scope. Do not automatically restore deferred content or add index lessons.

## Verification

node tests/course.test.cjs checks every included source subsection, prose block, code line and figure; source hashes and heading matches; scope exclusions; optional flags; schema/readiness; embedded parity; assessments; answer distribution and palette contrast.

With Playwright installed, node tests/browser.test.cjs checks every rendered slide, figures, safe Markdown, 390/768/1440px layouts, code layouts, menu/outline, notes/completion persistence, grading/reports, optional advanced gates, complete copying and manual fallback. GitHub Actions runs these checks plus deterministic generation. QA screenshots are workflow artifacts.

There is no authentication, shared backend, verified certificate or secure grading. Answers are delivered to the client; results are personal study feedback.

## Chapter 1 reading-flow pilot

Chapter 1 preserves every source passage while replacing 23 long slides with 75 shorter slides (maximum 144 words), explicit teaching-point titles and nested source subtopics. The chapter quiz remains at the end. See docs/content-guidelines.md for local review steps and docs/chapter-one-slide-map.json for source coverage. Source Markdown is unchanged. Changed Chapter 1 lessons start fresh progress; existing notes on retained lesson IDs are preserved when prose changes.

Teaching prose is cleaned separately from archived source: footnote markers and reference-only footnotes are removed, explanatory notes remain plain prose, and interrupted lowercase continuations are rejoined. Code and genuine numbered lists are unchanged. docs/source-cleanup-audit.json records the citation cleanup.
