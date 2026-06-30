#!/usr/bin/env python3
"""Fetch the content of a topic from roadmap.sh's Python roadmap.

The official content lives in roadmap.sh's repo (kamranahmedse/developer-roadmap),
one Markdown file per topic at src/data/roadmaps/python/content/<slug>@<id>.md.
Each file holds the description roadmap.sh writes + the "free resources" (links
tagged @article@/@video@/@official@/@feed@...).

Usage:
    python3 roadmap_topic.py "Basic syntax"
    python3 roadmap_topic.py basic-syntax

Prints the topic's Markdown to stdout. Exits with code 2 if no match is found.
"""
import json
import re
import sys
import urllib.error
import urllib.request

CONTENT_API = (
    "https://api.github.com/repos/kamranahmedse/developer-roadmap/"
    "contents/src/data/roadmaps/python/content"
)
UA = {"User-Agent": "Mozilla/5.0 (roadmap-topic-cli)"}


def slugify(text):
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def get_text(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8")


def find_topic_file(topic):
    slug = slugify(topic)
    listing = get_json(CONTENT_API)
    files = [x for x in listing if x.get("type") == "file" and x["name"].endswith(".md")]
    # name = "<slug>@<id>.md" -> compare against the slug before the '@'
    candidates = []
    for f in files:
        name_slug = f["name"].split("@", 1)[0]
        if name_slug == slug:
            return f  # exact match
        if slug in name_slug or name_slug in slug:
            candidates.append(f)
    if len(candidates) == 1:
        return candidates[0]
    if candidates:
        names = ", ".join(c["name"].split("@", 1)[0] for c in candidates)
        raise SystemExit(f"Ambiguous topic {topic!r} (slug {slug!r}). Candidates: {names}")
    return None


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: roadmap_topic.py \"<topic>\"")
    topic = sys.argv[1]
    try:
        f = find_topic_file(topic)
    except urllib.error.URLError as e:
        raise SystemExit(f"Could not reach the GitHub API: {e}")
    if f is None:
        raise SystemExit(2)  # no match
    print(get_text(f["download_url"]))


if __name__ == "__main__":
    main()
