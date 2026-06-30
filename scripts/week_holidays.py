#!/usr/bin/env python3
"""One week (Monday-Sunday) calendar with Colombia's national holidays.

Uses the public API at https://calendariosnacionales.com (no auth). Given a
reference date, it computes the week that contains it (Mon-Sun) and marks which
days are national holidays.

Usage:
    python3 week_holidays.py [YYYY-MM-DD]

If no date is given, today is used. Holiday names come from the API and stay in
Spanish (they are the official Colombian holiday names).
"""
import datetime
import json
import sys
import urllib.error
import urllib.request

API = "https://calendariosnacionales.com/co/v1/{year}/nacionales.json"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def fetch_year(year):
    """Download the national holidays for a year. Returns {iso_date: name}."""
    url = API.format(year=year)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (week-holidays-cli)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Error {e.code} fetching {url} "
                         f"(year out of range? The API covers 2025-2027).")
    except urllib.error.URLError as e:
        raise SystemExit(f"Could not reach the API: {e.reason}")
    return {h["date"]: h["name"] for h in data.get("holidays", [])}


def week_range(ref):
    """Return the list of 7 dates (Monday to Sunday) that contain ref."""
    monday = ref - datetime.timedelta(days=ref.weekday())  # weekday(): Mon=0
    return [monday + datetime.timedelta(days=i) for i in range(7)]


def holidays_for_week(week):
    """Map iso_date -> holiday name, covering a possible year boundary."""
    years = {week[0].year, week[-1].year}
    hmap = {}
    for y in sorted(years):
        for iso, name in fetch_year(y).items():
            hmap.setdefault(iso, name)
    return hmap


def main():
    if len(sys.argv) > 1:
        try:
            ref = datetime.date.fromisoformat(sys.argv[1])
        except ValueError:
            raise SystemExit(f"Invalid date: {sys.argv[1]!r}. Expected format YYYY-MM-DD.")
    else:
        ref = datetime.date.today()

    week = week_range(ref)
    hmap = holidays_for_week(week)

    holidays = []
    print(f"Week of {week[0].isoformat()} to {week[-1].isoformat()}\n")
    for i, d in enumerate(week):
        iso = d.isoformat()
        name = hmap.get(iso)
        mark = f"🎉 HOLIDAY — {name}" if name else ""
        print(f"  {DAYS[i]:10} {iso}  {mark}")
        if name:
            holidays.append((iso, DAYS[i], name))

    print()
    if holidays:
        print(f"Holidays this week: {len(holidays)}")
        for iso, day, name in holidays:
            print(f"  - {day} {iso}: {name}")
    else:
        print("No national holidays this week.")


if __name__ == "__main__":
    main()
