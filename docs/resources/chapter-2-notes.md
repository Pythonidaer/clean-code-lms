# Chapter 2 — My clean-code notes

## Names should remove guessing

A good name should help me understand what something represents, why it exists, and how it is used. Meaning, role, and units make this concrete: `daysSinceModification` tells me what is measured and in which unit; `source` and `destination` explain two different roles. Short code can still hide its purpose. Names like `gameBoard`, `flaggedCells`, and `isFlagged` make the concepts explicit without making the underlying logic more complicated. I want names that are easy to read, pronounce, search for, and discuss with another developer.

## Consistency should follow meaning

Use the same vocabulary for the same concept, and different names when the concepts actually differ. Adding `Info`, `Data`, a number, or an arbitrary prefix does not automatically explain a difference. Context should help me understand the name, not bury it: `address.state` is clearer than an isolated `state`, while repeating the product name everywhere adds little. Use familiar technical terms for technical mechanisms and domain terms for the problem being solved. The goal is enough precision to remove guessing, without unnecessary decoding or clutter. Improve names as understanding grows, using refactoring tools and checking affected behavior and contracts.

## Draft rules for future reviews and skills

1. Name the concept, purpose, or role; include units when they matter.
2. Use consistent vocabulary for equivalent concepts and distinguish genuinely different ones.
3. Avoid names that imply the wrong behavior, data, or representation.
4. Prefer pronounceable, searchable names; consider how widely each name is used.
5. Replace arbitrary abbreviations, numbering, and noise words with meaningful distinctions.
6. Give names useful surrounding context without repeating irrelevant product or type labels.
7. Use nouns for entities, verbs for actions, and clear questions for boolean checks.
8. Choose established technical or domain vocabulary that the intended readers understand.
9. Rename through the affected references and verify behavior; check public contracts before changing exposed names.

These are review heuristics. Java-specific prefixes, factories, and accessor conventions are not automatic rules for JavaScript, TypeScript, or React. A comment can still explain reasoning or constraints that a name cannot.

## Vocabulary — meaning and context

- **Meaning:** what a value or operation represents, such as elapsed time.
- **Role:** its job in an operation, such as source versus destination.
- **Units:** the scale of a quantity, such as seconds versus milliseconds.
- **Useful context:** surrounding names or structure that clarify an otherwise ambiguous name.
- **Problem domain:** the subject and rules the software serves. In this LMS: lessons, quizzes, and learning progress.
- **Solution domain:** technical concepts used to implement the solution, such as a map, cache, or queue.

The same codebase uses both domains: `lesson` names what the application deals with; `Map` describes one way to store and look up lessons.

## Vocabulary — data and implementation

- **Underlying representation:** how information is stored or arranged, such as lesson records in an array or a map.
- **Implementation details:** the particular steps and mechanisms used to make something work.
- **Business logic:** rules about required application behavior, such as when a quiz counts as passed.
- **Collection:** a group of values or objects.
- **Index/subscript:** a position or key used to access an element.
- **Status:** a value describing a condition, such as flagged or completed.
- **Predicate:** a check that answers true or false, such as `isFlagged`.
- **Job queue:** pending tasks held for processing.

A caller may need a useful operation without needing to know its internal representation. Clear naming helps communicate that boundary.

## Questions to explore

**Naming decisions:** How do I choose a shared vocabulary for a real repository? When do two similar operations deserve different names? How do I identify meaningless differences?

**Application to my stack:** How do TypeScript types affect the need for type prefixes? When are factories, interfaces, accessors, or mutators useful in JavaScript/TypeScript? How does domain vocabulary apply to React components and application code?

**Concepts to practice:** Can I identify problem-domain names, solution-domain names, implementation details, and business rules in one small module?

## Ideas to revisit

- Grow a focused CS glossary from terms I actually encounter: collections, status, indexes, predicates, queues, maps, algorithms, and design patterns. Add accessors and mutators, and explore the Visitor pattern when relevant.
- Build a shared vocabulary with examples and genuine distinctions rather than a list of preferred synonyms.
- Turn the draft rules into a review sequence: identify the concept, choose a name, check what readers could infer incorrectly, then verify the change.
- Combine overlapping rules with Chapter 1 later, preserving each rule’s reason and when it applies.
