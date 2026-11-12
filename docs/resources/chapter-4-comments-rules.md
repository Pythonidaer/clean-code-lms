# Chapter 4 — Comments

Start by making the code clear. Keep comments that explain reasoning, constraints, or consequences the reader would otherwise miss, and check them when the code changes.

## CC4-1 — Express intent in code first

Improve the name, helper, or structure when it can communicate the same idea.

Why: Readers can follow the code directly and have one fewer explanation to keep in sync.

Check: Read the code without the comment. If a clearer name or structure tells the same story, improve the code and remove the redundant comment.

## CC4-2 — Explain what the reader would otherwise miss

Use comments for rationale, external constraints, warnings, or surprising consequences. Clarify obscure library behavior when you cannot make the call itself clearer.

Why: The implementation may show what happens without revealing why it must happen that way.

Check: Name the fact the comment adds and verify it. For example, explain why retries reuse the request ID instead of simply labeling the retry.

## CC4-3 — Keep comments close, specific, and accurate

Place comments near the code they describe and review them when behavior changes. Put systemwide guidance in shared documentation.

Why: A vague or stale comment can send the next reader in the wrong direction.

Check: Identify exactly what code the comment applies to. Check its claims against the implementation, relevant tests, or the source of an external constraint.

## CC4-4 — Document what callers need

Describe public API expectations, effects, and failure behavior where they matter. Preserve required legal notices and follow repository documentation conventions.

Why: Callers need to understand the contract before using an operation.

Check: Check what someone can learn from the signature and what they still need to know. Add missing contract details; avoid boilerplate that repeats the signature.

## CC4-5 — Make TODOs actionable

Say what work remains and, when useful, why it is deferred. Link to a tracked issue when one exists.

Why: A useful TODO gives the next reader a task they can recognize and act on.

Check: Can another developer tell what needs to change? Review stale TODOs and remove them when the work is complete or no longer relevant.

## CC4-6 — Remove comments that add maintenance without meaning

Fix or remove stale and misleading explanations. Remove redundant headers, change journals, informal bylines, and dead commented-out code. Keep section markers when they materially help navigation.

Why: Noise makes useful comments easier to overlook. Version control already records ordinary change history and deleted code.

Check: Name what a reader would lose if the comment disappeared. Preserve required notices, tool directives, and intentional documentation.
