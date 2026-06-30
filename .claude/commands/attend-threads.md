---
description: Attend Discord threads with new activity — the scanner finds unanswered questions/exercises and the tutor replies in each thread
---

Attend the open threads of the active topics. Orchestrate the handoff between two agents:

1. Launch `thread-scanner`. It reads `./to_do.md` (unchecked topics), finds the published
   threads (`thread_id` not empty) with **unanswered student activity**, and returns, for
   each thread that needs attention, its transcript and metadata
   (`topic`, `channel_id`, `thread_id`, `bot_id`, `last_bot_message_id`).

2. For EACH thread the scanner reports as "needs attention", launch one `discord-tutor`
   (one per thread), passing it that data and the transcript. The tutor replies with ONE
   consolidated message in Colombian Spanish (tuteo), grounded in the topic's roadmap.sh
   content.
   - You may launch several `discord-tutor` agents in parallel (one per thread) since
     they are independent.

3. If the scanner finds no thread with new activity, do not launch any tutor.

When done, report: how many threads had activity, which ones the tutor replied to, and
whether there was any warning (e.g. the bot is missing the MESSAGE CONTENT intent).
