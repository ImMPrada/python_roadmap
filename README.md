# Python Roadmap → Discord Learning Bot

An agent-driven system that turns [roadmap.sh/python](https://roadmap.sh/python)
topics into a week of bite-sized Discord content (examples, curiosities, and daily
exercises), publishes it day by day, and tutors the community in the threads.

- **Development-facing things are in English** (scripts, commands, agents, tracking files).
- **What gets published to Discord is in Colombian Spanish** (tuteo), with technical
  programming terms kept in English. That's product, not code.

---

## How it works (lifecycle of a topic)

```
            /organize-week "Basic syntax"
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 roadmap-week-planner   →   spanish-style-corrector
 (drafts the week)          (voseo → tú safety net)
        │
        ▼
 ./basic_syntax/*.md  (one file per working day, thread_id empty)
 ./basic_syntax/to_check.md
 ./to_do.md  (- [ ] Basic syntax)
        │
        ▼   every morning ~5:00 AM COT   ── /publish-today
 daily-discord-publisher
 (creates the thread, posts the body, pings @everyone, fills thread_id)
        │
        ▼   every ~2–3 h               ── /attend-threads
 thread-scanner  →  discord-tutor
 (find unanswered student activity)   (one consolidated reply per thread)
        │
        ▼   daily                       ── /review-checklists
 to-check-reviewer
 (checks off days past their "review by" date; closes the topic in to_do.md
  once all its days are done)
```

A topic stays **active** while it has an unchecked `- [ ]` entry in `to_do.md`.
The publisher, scanner, and reviewer only look at active topics.

---

## Setup

1. **Discord bot token** — stored in `.claude/settings.local.json` (gitignored):
   ```json
   {
     "env": {
       "DISCORD_BOT_TOKEN": "...",
       "DISCORD_GUILD_ID": "..."
     }
   }
   ```
   Use `.claude/settings.local.json.example` as a template. **Never commit the real token.**

2. **Privileged intent for tutoring** — the tutor must read members' messages. Enable
   the **MESSAGE CONTENT** intent in the Discord Developer Portal
   (*Bot → Privileged Gateway Intents*). Without it, student messages come back empty
   and `thread-scanner` will warn you.

3. **Python** — the scripts use only the standard library (Python 3). No dependencies.

4. **Bot permissions** in the target channel: View Channels, Read Message History,
   Send Messages, Send Messages in Threads, Create Public Threads.

---

## Commands

| Command | What it does | Cadence |
|---------|--------------|---------|
| `/organize-week <topic>` | Draft a full week for a topic, then fix any voseo. DRAFT ONLY. | On demand (e.g. Sunday night) |
| `/publish-today` | Publish today's posts for active topics (creates threads, fills `thread_id`). | Daily ~5:00 AM COT |
| `/attend-threads` | Find threads with unanswered student activity and have the tutor reply. | Every ~2–3 h |
| `/review-checklists` | Check off expired `to_check.md` days; close finished topics in `to_do.md`. | Daily |
| `/week-holidays [YYYY-MM-DD]` | Show a Mon–Sun calendar with Colombian national holidays. | As needed |

To run any of these automatically while a session is alive, wrap them with `/loop`
(e.g. `/loop /publish-today`). For something that survives a closed session, use a
cloud routine via `/schedule`.

### Week selection rule (`/organize-week`)
- Requested **Mon/Tue** → the **current** week.
- Requested **Wed–Sun** → the **next** week (upcoming Monday–Sunday).

National holidays in the target week are **skipped** — no file is created for that day.

---

## Agents

| Agent | Role | Writes to Discord? |
|-------|------|--------------------|
| `roadmap-week-planner` | Drafts the week's `.md` files from the roadmap.sh topic content. | No |
| `spanish-style-corrector` | Rewrites any voseo paisa into tú; preserves code & meaning. | No |
| `daily-discord-publisher` | Posts today's content, pings `@everyone`, writes back `thread_id`. | **Yes** |
| `thread-scanner` | Read-only; finds threads with unanswered student activity. | No |
| `discord-tutor` | One consolidated, grounded reply per thread (ES-CO, tuteo). | **Yes** |
| `to-check-reviewer` | Date-driven; checks off review days and closes topics. | No |

The orchestrator chains them; the commands above are the entry points. The publisher
is idempotent (a file with a non-empty `thread_id` is never re-posted), and the tutor
only addresses messages posted after the bot's last reply.

---

## Scripts

- **`scripts/week_holidays.py [YYYY-MM-DD]`** — prints the Mon–Sun week containing the
  date and marks national holidays (`🎉 HOLIDAY`). Data from
  `calendariosnacionales.com` (covers 2025–2027). Holiday names stay in Spanish (they
  are official names).
- **`scripts/roadmap_topic.py "<topic>"`** — prints a roadmap.sh Python topic's
  Markdown (description + free resources), fetched from the official
  `kamranahmedse/developer-roadmap` repo. Exits with code 2 if the topic isn't found.

---

## File layout

```
.
├── README.md
├── to_do.md                     # master topic list:  - [ ] / - [x]
├── <topic_snake_case>/          # e.g. basic_syntax/
│   ├── monday.md … sunday.md    # one per working day (holidays skipped)
│   └── to_check.md              # per-day review checklist
├── scripts/
│   ├── week_holidays.py
│   └── roadmap_topic.py
└── .claude/
    ├── agents/                  # the 6 agents above
    ├── commands/                # the 5 commands above
    └── settings.local.json      # DISCORD_BOT_TOKEN (gitignored)
```

### Daily post format (`<weekday>.md`)
Frontmatter keys are English; the body and `title` are Colombian Spanish.

```markdown
---
title: "🐍 Short attractive hook — becomes the Discord thread name"
date: 2026-06-30
thread_id: ""            # empty until published
channel: "python"
---

Body in Colombian Spanish (tuteo), technical terms in English,
with ```python``` code blocks, examples, a curiosity, or an exercise.
```

### `to_check.md`
```markdown
# To check — Basic syntax

- [ ] tuesday — published 2026-06-30 · review by 2026-07-08
```
`review by` = the post date + 8 days.

### `to_do.md`
```markdown
# Topics

- [ ] Basic syntax
```

---

## Conventions

- **Discord content:** Colombian Spanish, address the reader with **tú** (never voseo,
  never "usted"); keep technical terms in English (`string`, `loop`, `f-string`,
  `indentation`, …). `spanish-style-corrector` enforces this.
- **Everything else** (names, comments, instructions, tracking files): English.
- **Holidays:** skipped at planning time, so the rest of the pipeline never has to
  special-case them.
- **Time zone:** "today" is always computed in `America/Bogota`.
