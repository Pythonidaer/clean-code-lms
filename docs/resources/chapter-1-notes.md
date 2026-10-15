# Chapter 1 — My clean-code notes

## What clean code should communicate

Clean code should help the next person understand what the code does, why it exists, and how to change it. Meaningful names, straightforward logic, focused functions and modules, clear boundaries, and deliberate error handling make that easier. Readability and changeability are related, but they are not identical: code can look simple while still being difficult to modify safely. Tests provide evidence that a change preserves the behavior we depend on.

## Why maintaining it matters

Messy code makes us spend more time reconstructing context before we can make a change. That is the “wading” I want to avoid. If each change adds more confusion, the effort can build into a productivity spiral. I want to develop my code-sense by understanding the existing design, recognizing specific problems, and practicing small improvements. The Boy Scout Rule gives me a practical starting point: leave the area I touched a little clearer. Reading provides techniques; practice develops judgment. I should understand each recommendation’s purpose and tradeoffs rather than treat this book as the final authority.

## The six perspectives

- **Bjarne Stroustrup:** focused logic, efficiency, minimal dependencies, and attention to failure handling.
- **Grady Booch:** clear design intent, direct flow, and abstractions that explain the problem.
- **Dave Thomas:** code other people can read and enhance, supported by tests and a clear API.
- **Michael Feathers:** care shows up in simplicity, order, and attention to details.
- **Ron Jeffries:** passing tests, reduced duplication, expressed intent, and fewer unnecessary entities—in that priority order.
- **Ward Cunningham:** predictable routines and modules that prepare the reader for what comes next.

These perspectives overlap. I can use them as questions when reviewing code, rather than six competing definitions to memorize.

## Draft rules for future reviews and skills

1. Understand the behavior and design intent before changing the code.
2. Choose names that explain meaning, purpose, and relevant units.
3. Keep functions and modules focused; separate responsibilities when that clarifies the design.
4. Remove duplication when it represents the same underlying idea.
5. Introduce an abstraction when it clarifies a real need or useful boundary.
6. Handle failures deliberately and make dependencies clear.
7. Make small, behavior-preserving improvements and check the affected behavior.
8. Explain the observed problem, its consequence, and the reason for the proposed change.
9. Communicate maintenance risks during requirements and schedule discussions.
10. Evaluate recommendations in context; avoid treating shortness, test presence, or a named principle as proof of quality.

These are draft review heuristics, not automatic pass/fail rules.

## Why easier reading makes the next change easier

Before changing code, I need to understand its behavior and surrounding assumptions. Clear names and predictable structure reduce the guessing needed to find the relevant logic, understand its callers, and identify what the change could affect. That makes it easier to choose a small change and check its consequences.

The goal is to reduce avoidable effort, not to hit a reading-to-writing ratio below 10:1. Reading is necessary work; the chapter’s ratio illustrates why readability matters. Likewise, developers should communicate risks and protect quality, but organizational failures are not automatically one developer’s fault.

## A small Boy Scout improvement in React and TypeScript

A React component receives this typed value:

```tsx
// Before
const d: number = 3;
return <span>{d} days since your last visit</span>;
```

Clarify what the value represents:

```tsx
// After
const daysSinceLastVisit: number = 3;
return <span>{daysSinceLastVisit} days since your last visit</span>;
```

The displayed result stays the same. The name now communicates meaning and units. Update every reference and check the affected rendering. The same naming improvement applies in JavaScript; TypeScript also states that the value is a number.

## Questions to explore — core concepts

- How do higher levels of language abstraction work? What is a domain-specific language?
- What are design intent, a module, a greenfield project, and code decay?
- What makes an abstraction “crisp” or useful rather than unnecessary?
- How do meaningful names, duplication, and Extract Method help express an idea?
- What are unit tests, acceptance tests, and test-driven development?
- What is a composite condition? How can its intent become clearer?
- What are heuristics, and how do I practice deciding when they apply?

These are open learning questions, not gaps to hide in the summary.

## Questions to explore — principles and background

**Design principles:** What do SRP, OCP, DIP, and object-oriented design mean? Where do they apply in JavaScript, TypeScript, and React?

**Historical context:** What are OTI, Eclipse, Fit, Extreme Programming, literate programming, and the Object Mentor school? These can remain secondary to understanding the code-quality ideas.

**Working with AI:** Can I inspect an editing session or change history in Cursor? How can I use that to understand LLM-generated code and the reasoning behind changes?

## Ideas to revisit

- Create a Hangman-style learning activity for identifying code issues, possibly by selecting functions or conditions. Clarify what the player would learn before choosing the game mechanics.
- Use these draft rules as a repeatable review: identify the code’s purpose, observe a specific problem, propose one improvement, explain the tradeoff, and verify behavior.
- Build code-sense through small examples and comparisons. Revisit these notes after later chapters and revise the rules with what I learn.
