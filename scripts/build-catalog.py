#!/usr/bin/env python3
"""build-catalog.py — generate docs/catalog.html, a searchable catalogue of every agent.

Reads divisions.json for the division list, each agent .md file's frontmatter
(name, description, emoji, vibe) and body, and the team bundles in
strategy/teams/*.txt. Writes one self-contained HTML page (no server, no build
step) that you can open straight from disk or host anywhere.

Usage:
  python3 scripts/build-catalog.py                 # writes docs/catalog.html
  python3 scripts/build-catalog.py --fragment OUT  # page body only (for hosts that add <html>/<head>)

Re-run after adding or editing agents.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_frontmatter(text):
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return {}, text
    meta, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            meta[key] = "" if val in (">", "|", ">-", "|-") else val
        elif key and line.startswith((" ", "\t")):
            meta[key] = (meta[key] + " " + line.strip()).strip()
    for k, v in meta.items():
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            meta[k] = v[1:-1]
    return meta, text[m.end():]


def load_teams():
    teams = []
    tdir = os.path.join(ROOT, "strategy", "teams")
    if not os.path.isdir(tdir):
        return teams
    for fn in sorted(os.listdir(tdir)):
        if not fn.endswith(".txt"):
            continue
        lines = open(os.path.join(tdir, fn), encoding="utf-8").read().splitlines()
        comments = [l[1:].strip() for l in lines if l.startswith("#")]
        slugs = [l.strip() for l in lines if l.strip() and not l.startswith("#")]
        teams.append({
            "id": fn[:-4],
            "title": comments[0] if comments else fn[:-4],
            "summary": comments[1] if len(comments) > 1 else "",
            "file": "strategy/teams/" + fn,
            "agents": slugs,
        })
    return teams


def load_agents(divisions):
    agents = []
    for div in divisions:
        ddir = os.path.join(ROOT, div)
        for dirpath, _, files in os.walk(ddir):
            for fn in sorted(files):
                if not fn.endswith(".md"):
                    continue
                path = os.path.join(dirpath, fn)
                text = open(path, encoding="utf-8").read()
                meta, body = parse_frontmatter(text)
                if not meta.get("name"):
                    continue
                agents.append({
                    "slug": fn[:-3],
                    "name": meta.get("name", ""),
                    "description": meta.get("description", ""),
                    "emoji": meta.get("emoji", ""),
                    "vibe": meta.get("vibe", ""),
                    "division": div,
                    "path": os.path.relpath(path, ROOT),
                    "body": body.strip(),
                })
    agents.sort(key=lambda a: (a["division"], a["name"].lower()))
    return agents


def main():
    fragment_out = None
    if len(sys.argv) == 3 and sys.argv[1] == "--fragment":
        fragment_out = sys.argv[2]
    elif len(sys.argv) != 1:
        print(__doc__)
        sys.exit(2)

    divisions = json.load(open(os.path.join(ROOT, "divisions.json"), encoding="utf-8"))["divisions"]
    agents = load_agents(divisions)
    teams = load_teams()
    known = {a["slug"] for a in agents}
    for t in teams:
        missing = [s for s in t["agents"] if s not in known]
        if missing:
            print(f"ERROR team {t['id']} lists unknown agents: {', '.join(missing)}", file=sys.stderr)
            sys.exit(1)

    data = {
        "divisions": {k: {"label": v["label"], "color": v.get("color", "#888")} for k, v in divisions.items()},
        "agents": agents,
        "teams": teams,
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = open(os.path.join(ROOT, "scripts", "catalog-template.html"), encoding="utf-8").read()
    page = template.replace("/*__DATA__*/null", payload)

    if fragment_out:
        out = fragment_out
        html = page
    else:
        out = os.path.join(ROOT, "docs", "catalog.html")
        html = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
                "</head>\n<body>\n" + page + "\n</body>\n</html>\n")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)
    print(f"Wrote {os.path.relpath(out, ROOT) if out.startswith(ROOT) else out}: "
          f"{len(agents)} agents, {len(divisions)} divisions, {len(teams)} teams")


if __name__ == "__main__":
    main()
