---
description: Review the active topics' to_check.md files and check off expired days; close a topic in to_do.md when nothing is left to review
---

Launch the `to-check-reviewer` agent to update **today's** review checklists (Colombia time).

The agent must:
1. Read `./to_do.md` and take only the **unchecked** `[ ]` topics.
2. In each `./<topic>/to_check.md`, check off `[x]` the days whose `review by` date has
   already arrived or passed (`today >= deadline`).
3. When **all** of a topic's days are checked off, check that topic off in `./to_do.md`.

Use it through the `to-check-reviewer` agent (do not replicate its logic here).
When done, report what was checked off and which topics were closed, or that there was
nothing to do.
