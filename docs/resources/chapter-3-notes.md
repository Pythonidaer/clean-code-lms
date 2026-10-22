# Chapter 3 — My clean-code notes

## Functions should make their purpose clear

A function should make its purpose easy to understand. Its name tells me what it does, and its steps should deliver on that promise without mixing the overall task with low-level details. Small, focused functions help, but the goal is readability rather than a particular line count. Extracting a helper is useful when it gives a meaningful idea a name and makes the surrounding code easier to follow.

## Clear inputs, effects, and revisions

I should understand what goes into a function, what comes back, and what changes. Unclear argument roles, hidden side effects, and unexpected ordering requirements create extra work. Clear functions usually emerge through revision: write a working draft, then improve names, separate responsibilities, and remove meaningful duplication while checking that behavior stays correct. Together, the functions should explain how the system works.

## Draft rules — purpose and structure

1. Give each function one coherent purpose. Its name and steps should describe the same task.
2. Keep functions small enough to understand. Use length and nesting as signals to investigate, rather than enforcing arbitrary limits.
3. Keep each function at a consistent level of detail. Let higher-level steps call helpers that explain the implementation.
4. Extract meaningful concepts. A helper should improve understanding rather than merely move lines elsewhere.
5. Use descriptive, consistent names. Make actions and argument roles predictable across related functions.

## Draft rules — inputs and effects

6. Keep inputs understandable. Reduce unnecessary arguments and group values when they represent a real concept. Avoid hiding dependencies just to reduce the count.
7. Review flags that select different operations. Separate clearly different actions when that makes the interface easier to understand.
8. Make effects and ordering visible. Callers should understand what changes and whether another operation must happen first.
9. Keep questions free of surprising changes. Distinguish reading information from changing state; make intentional combinations explicit.

## Draft rules — failures and refinement

10. Keep failure handling clear. Follow the language and project's error-handling conventions, and preserve useful failure information.
11. Consolidate repeated knowledge. Share logic that must change together without forcing unrelated cases into one abstraction.
12. Refine with behavior checks. Improve structure incrementally, using appropriate tests to protect the behavior being changed.

These are review heuristics. The chapter's Java examples do not make inheritance, factories, exceptions, zero arguments, or a single return mandatory in JavaScript or TypeScript. Choose structures that make responsibilities and behavior clear.

## Questions — abstraction and design

**Abstraction levels and the Stepdown Rule:** How do I distinguish the overall task, its major steps, and implementation details? Practice rewriting a function as “To accomplish this, do these steps.”

**Polymorphism, SRP, and OCP:** What do they mean, and when would they improve a growing or repeated switch? Compare Java examples with TypeScript alternatives.

**Temporal coupling:** When must operations happen in a particular order, and how can the interface make that requirement explicit?

## Questions — applying this to my stack

How do exceptions compare with returned results in JavaScript and TypeScript? When is input mutation intentional, and how should it be communicated? How does command–query separation apply when an action returns a useful result?

How do I judge argument counts, function length, and multiple returns by clarity rather than treating them as automatic restrictions?

## Ideas to revisit

- Compare one function before and after refinement: purpose, abstraction levels, names, inputs, effects, failure handling, and duplication.
- Practice tracing a top-down sequence from the main task into its implementation helpers.
- Combine overlapping rules with Chapters 1 and 2 later, preserving each rule's reason and limits before turning them into a shared review workflow or skill.
