#!/usr/bin/env python3
"""Obtiene el contenido de un tema del Python roadmap de roadmap.sh.

El contenido oficial vive en el repo de roadmap.sh
(kamranahmedse/developer-roadmap), un archivo Markdown por tema en
src/data/roadmaps/python/content/<slug>@<id>.md. Cada archivo trae la
descripción que escribe roadmap.sh + los "free resources" (links etiquetados
@article@/@video@/@official@/@feed@...).

Uso:
    python3 roadmap_topic.py "Basic syntax"
    python3 roadmap_topic.py basic-syntax

Imprime el Markdown del tema en stdout. Sale con código 2 si no encuentra match.
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
    # nombre = "<slug>@<id>.md" -> comparar contra el slug antes del '@'
    candidates = []
    for f in files:
        name_slug = f["name"].split("@", 1)[0]
        if name_slug == slug:
            return f  # match exacto
        if slug in name_slug or name_slug in slug:
            candidates.append(f)
    if len(candidates) == 1:
        return candidates[0]
    if candidates:
        names = ", ".join(c["name"].split("@", 1)[0] for c in candidates)
        raise SystemExit(f"Tema ambiguo {topic!r} (slug {slug!r}). Candidatos: {names}")
    return None


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Uso: roadmap_topic.py \"<tema>\"")
    topic = sys.argv[1]
    try:
        f = find_topic_file(topic)
    except urllib.error.URLError as e:
        raise SystemExit(f"No se pudo conectar a GitHub API: {e}")
    if f is None:
        raise SystemExit(2)  # sin match
    print(get_text(f["download_url"]))


if __name__ == "__main__":
    main()
