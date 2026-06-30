---
description: Organize a topic's week — draft the posts (planner) and fix voseo (corrector) in one step
argument-hint: "<topic>  (e.g. Basic syntax)"
---

Organize the full week for the topic: **$ARGUMENTS**.

Run the agents in order, waiting for each to finish before the next:

1. Launch `roadmap-week-planner` with:
   - topic: `$ARGUMENTS`
   - roadmap.sh link: `https://roadmap.sh/python`
   - discord channel: `python`

   It creates the `./<topic>/` folder with one `.md` per working day (holidays
   skipped), `to_check.md`, and appends the topic to `./to_do.md`.

2. When the planner finishes, launch `spanish-style-corrector` on the same topic
   (`$ARGUMENTS`) as a safety net to fix any voseo → tú.

3. Report the combined result: files created, days skipped for holidays, featured
   resources, and how many voseo fixes the corrector applied.

Note: this is DRAFT ONLY — nothing is published to Discord (`thread_id` stays empty).
