---
description: Show a week (Monday-Sunday) calendar and mark which days are Colombian national holidays
argument-hint: "[YYYY-MM-DD]  (optional; defaults to the current week)"
allowed-tools: Bash(python3 scripts/week_holidays.py:*)
---

Run `scripts/week_holidays.py` to get the calendar of the week (Monday to Sunday)
that contains the given date and find out which days are Colombian national holidays.

Data comes from the public API at https://calendariosnacionales.com (covers 2025-2027).

Argument: `$ARGUMENTS` — an optional `YYYY-MM-DD` date. If empty, the current week is used.

Steps:
1. Run: `python3 scripts/week_holidays.py $ARGUMENTS`
2. Present the week to the user, day by day, clearly highlighting the holidays.
3. If there was an error (invalid date or year outside 2025-2027), explain it briefly.
