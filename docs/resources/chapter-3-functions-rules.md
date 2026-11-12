# Chapter 3 — Functions

Companion to the [Chapter 3 study notes](chapter-3-notes.md). Use these draft rules when reviewing or refining functions.

Make a function's purpose, inputs, result and effects easy to understand. These rules develop Chapter 1's readability and responsibility principles and Chapter 2's naming guidance; use those overlaps as context rather than duplicate findings.

## CC3-1 — Give each function one coherent purpose

Make the function's name and steps describe the same task.

Why: A reader should be able to explain the operation without discovering unrelated work hidden inside it.

Check: Describe the purpose in one brief sentence, then compare each step with that purpose. Internal sections can signal separate responsibilities, but a multi-step task can still be coherent.

## CC3-2 — Keep functions small enough to understand

Use length and nesting as signals to investigate; improve readability rather than enforce an arbitrary line limit.

Why: Shorter code can reduce reading effort, but excessive fragmentation can make the reader jump between helpers.

Check: Read the function with its helpers. Can its control flow and purpose be followed without excessive nesting or navigation? Do not split code solely to reach a number.

## CC3-3 — Keep a consistent level of detail

Let higher-level steps call helpers that explain lower-level implementation details.

Why: Mixing the overall task with storage, formatting or other mechanism details makes the sequence harder to follow.

Check: Describe the function as “To accomplish this, do these steps.” Check that sibling steps express a comparable level of detail. The Stepdown Rule is a readability technique, not a mandatory source-file ordering.

## CC3-4 — Extract meaningful concepts

Give a helper a meaningful responsibility and name; extraction should improve understanding.

Why: Moving lines into a function does not automatically create a useful abstraction.

Check: Explain the idea the helper introduces and read the caller again. Keep details inline when extraction would merely restate the implementation or increase indirection.

## CC3-5 — Use descriptive, consistent names

Make function names communicate the action and make argument roles predictable. Apply the naming guidance in [Chapter 2](chapter-2-notes.md).

Why: Readers use names to anticipate behavior and connect related operations.

Check: Compare the name with the actual work and its effects. Reuse established vocabulary for equivalent concepts; improve names safely rather than add length without meaning.

## CC3-6 — Keep inputs understandable

Reduce unnecessary arguments and group values when they represent a real concept. Keep dependencies explicit.

Why: Readers must understand each argument's role, ordering and valid combinations.

Check: Review call sites for ambiguous positional values. Use a named concept or options object when helpful; do not hide dependencies in globals or mutable state just to reduce the count.

## CC3-7 — Review flags that select different operations

Separate clearly different actions when that makes their interface easier to understand.

Why: A boolean at a call site can hide which operation will run.

Check: Explain what true and false select. Consider separate named operations or an explicit option when they clarify intent. Boolean inputs and existing flags are not automatically defects.

## CC3-8 — Make effects and ordering visible

Communicate what state changes and whether another operation must happen first.

Why: Hidden mutation and ordering requirements force callers to discover unwritten contracts.

Check: Check changes to inputs, owning objects, shared state and external systems. Make required setup or sequencing visible in the interface or contract; do not assume a reassuring name makes an effect obvious.

## CC3-9 — Keep questions free of surprising changes

Distinguish reading information from changing state. Make intentional combinations explicit.

Why: A call used as a condition can appear to be a harmless check while changing the system.

Check: Inspect predicates and queries for unexpected mutation. An action may intentionally return a result or status; preserve useful contracts and make its effects clear rather than applying command–query separation mechanically.

## CC3-10 — Keep failure handling clear

Follow the language and project's error-handling conventions and preserve useful failure information.

Why: Normal work and recovery become harder to follow when failures are obscured or repeatedly checked without structure.

Check: Can a caller identify the failure and respond appropriately? Choose exceptions, returned results or established project mechanisms deliberately. Extract handling when it clarifies responsibility; do not mandate Java exception patterns or swallow errors to simplify the happy path.

## CC3-11 — Consolidate repeated knowledge

Share logic that must change together without forcing unrelated cases into one abstraction.

Why: Repeated rules can drift; superficially similar code may represent different concepts.

Check: Identify the shared reason to change before consolidating. Check callers and resulting conditionals for evidence that the abstraction is combining unrelated responsibilities.

## CC3-12 — Refine with behavior checks

Improve names and structure incrementally, preserving intended behavior and checking affected contracts.

Why: Readable functions usually emerge through revision, and structural changes can alter observable behavior.

Check: Use appropriate existing tests and focused checks for the change. Inspect callers, effects, ordering and failure paths. Choose early returns, multiple returns or other control flow for clarity rather than imposing a single-exit rule.

## Qualifications

Function size, argument counts and return counts are prompts for judgment. Do not automatically introduce inheritance, factories, polymorphism, exceptions or zero-argument functions because a historical Java example uses them. A growing or repeated switch is a reason to examine responsibilities and alternatives, not an automatic instruction to replace it.

Open questions and speculative ideas remain in the LMS Resources. These rules are working guidance for an appropriately scoped review or change.
