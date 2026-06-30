---
description: Publish today's Discord posts (active topics in to_do.md), creating the threads and saving the thread_id
---

Launch the `daily-discord-publisher` agent to publish **today's** content (Colombia time).

The agent must:
1. Read `./to_do.md` and take only the **unchecked** `[ ]` topics.
2. In each topic folder, find the `.md` whose `date` = today and `thread_id` is empty.
3. Create the Discord thread (name = `title`), post the body inside, ping `@everyone`,
   and write the `thread_id` back into the file.
4. Be idempotent (never re-publish a file that already has a `thread_id`).

Use it through the `daily-discord-publisher` agent (do not replicate its logic here).
When done, report what was published or that there was nothing for today.
