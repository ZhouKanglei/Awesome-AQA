#!/usr/bin/env python3
import re
from pathlib import Path
import json
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
BIB = DATA_DIR / "aqa.bib"
SURVEY_BIB = DATA_DIR / "survey.bib"
README = ROOT / "README.md"
CCF_JSON = DATA_DIR / "ccf2026.json"
CCF_CACHE = {}


def parse_bib(path: Path):
    entries, cur = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("@") and not line.lower().startswith("@string"):
            if cur:
                entries.append(cur)
            m = re.match(r"@\w+\{([^,]+),", line)
            cur = {"key": m.group(1) if m else ""}
            continue
        if cur is None:
            continue
        if line.strip().startswith("}"):
            entries.append(cur)
            cur = None
            continue
        m = re.match(r"\s*(\w+)\s*=\s*(\{.*\}|\".*\"|[^,]+),?\s*", line)
        if m:
            k, v = m.groups()
            v = v.strip()
            if v.startswith("{") and v.endswith("}"):
                v = v[1:-1]
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            cur[k.lower()] = v
    # keep entries with title/year
    entries = [e for e in entries if e.get("title") and e.get("year")]
    return entries


def badge(venue, year):
    venue_disp = venue or "--"
    year_disp = year or "--"
    if venue_disp.startswith("arXiv preprint arXiv:"):
        venue_disp = "arXiv"
    base = normalize_abbr(venue_disp)
    level = ccf_level(base)
    color_map = {"A": "e74c3c", "B": "f1c40f", "C": "2ecc71", "Z": "4682B4"}
    color = color_map[level]
    return f"![](https://img.shields.io/badge/{quote(venue_disp + ' ' + year_disp)}-{color})"


def ccf_level(venue_disp: str) -> str:
    base = normalize_abbr(venue_disp)
    return CCF_CACHE.get(base, "Z")


def normalize_abbr(text: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", (text or "--").upper())


def project_icon(url):
    if not url:
        return ""
    m = re.match(r"https?://github\.com/([^/]+)/([^/#]+)", url)
    if m:
        owner, repo = m.groups()
        shield = (
            f"https://img.shields.io/github/stars/{owner}/{repo}.svg?"
            "style=social&label=&logo=github"
        )
        return f"[![]({shield})]({url})"
    return f"[🌐]({url})"


def resource_icons(entry):
    project = (entry.get("project") or "").strip()
    code = (entry.get("code") or "").strip()
    urls = [url for url in (project, code) if url]
    return "<br>".join(project_icon(url) for url in dict.fromkeys(urls))


def title_link(entry):
    url = (
        entry.get("pdf")
        or entry.get("url")
        or entry.get("project")
        or entry.get("abstract")
    )
    title = entry.get("title", "--")
    parts = []
    domain = (entry.get("domain") or "").strip()
    if domain:
        parts.append(domain)
    tags_clean = clean_tags(entry.get("tags", ""))
    if tags_clean:
        parts.append(tags_clean)
    suffix = f" ({'; '.join(parts)})" if parts else ""
    linked = f"[{title}]({url})" if url else title
    return f"{linked}{suffix}"


def new_dataset_cell(entry):
    tags = entry.get("tags", "")
    items = []
    modality_raw = entry.get("modality", "").strip()
    # Split modalities on separators to handle multiple entries
    modality_list = re.split(r"[;,]", modality_raw) if modality_raw else []
    modality_list = [m.strip() for m in modality_list if m.strip()]
    for part in [t.strip() for t in tags.split(",")]:
        if "(new)" in part:
            name = part.replace("(new)", "").strip()
            if name:
                # If multiple new datasets, try to pair sequentially with modality entries
                mod = modality_list.pop(0) if modality_list else modality_raw
                if mod:
                    items.append(f"{name}<br><span style='font-size:90%;color:gray'>{mod}</span>")
                else:
                    items.append(name)
    return "<br>".join(items)


def clean_tags(tags: str) -> str:
    cleaned = []
    for t in [p.strip() for p in tags.split(",") if p.strip()]:
        if "(new)" in t or t.lower() == "dataset":
            continue
        cleaned.append(t.replace("(new)", "").strip())
    return ", ".join(cleaned)


def main():
    entries = parse_bib(BIB)
    surveys = parse_bib(SURVEY_BIB) if SURVEY_BIB.exists() else []
    # sort per year: CCF level (A→B→C→others), then venue alphabetically, then title
    level_priority = {"A": 0, "B": 1, "C": 2, "Z": 3}
    entries.sort(
        key=lambda e: (
            -int(re.sub(r"[^0-9]", "", e.get("year", "0")) or 0),
            level_priority.get(
                ccf_level(e.get("journal") or e.get("booktitle") or "--"), 3
            ),
            (e.get("journal") or e.get("booktitle") or "").upper(),
            e.get("title", ""),
        )
    )
    pinned = {"zhou2024acomprehensivesu"}
    surveys.sort(
        key=lambda e: (
            0 if e.get("key", "").lower() in pinned else 1,
            -int(re.sub(r"[^0-9]", "", e.get("year", "0")) or 0),
            (e.get("journal") or e.get("booktitle") or "").upper(),
            e.get("title", ""),
        )
    )
    header = """# Awesome Action Quality Assessment (AQA)

## Recommended: Survey / Project entry points
- 🔍 **Project page (keyword-friendly search):** <https://zhoukanglei.github.io/AQA-Survey> — quickly search and filter all papers/notes.
- 📘 **Bibliography bundle:** this repo ships the latest reference list; use the project page for fast discovery.

[![](imgs/project.png)](https://zhoukanglei.github.io/AQA-Survey)

<details>
<summary><b>Notes / Contributions / Community</b> (click to expand)</summary>

| Item | Details | Link / Image |
|---|---|---|
| Contribute | Open an issue or submit full Pull requests to add or correct papers/links. | [Issue tracker](https://github.com/ZhouKanglei/Awesome-AQA/issues) · [Pull requests](https://github.com/ZhouKanglei/Awesome-AQA/pulls) |
| WeChat group | Join via QR; if the main one expires, use the personal link. | [Main QR](imgs/aqa-wechat-group.jpg) · [Personal QR](imgs/ZKL.png) |
| Updates | Project page and issues carry the latest notes and announcements. | [Project page](https://zhoukanglei.github.io/AQA-Survey) · [Issue tracker](https://github.com/ZhouKanglei/Awesome-AQA/issues) |

</details>

## Survey list

| Venue / Year | Title | Project / Code |
|---|---|---|
"""
    survey_rows = [
        f"| {badge(s.get('journal') or s.get('booktitle') or '--', s.get('year','--'))} | {title_link(s)} | {resource_icons(s)} |"
        for s in surveys
    ]

    header_refs = """

## Reference list (sorted by year → venue → title)
Auto-compiled from the bundled bibliography. If you spot a mistake, please open an issue.

| Venue / Year | Title | Project / Code | New Dataset (modality) |
|---|---|---|---|
"""
    rows = [
        f"| {badge(e.get('journal') or e.get('booktitle') or '--', e.get('year','--'))} | {title_link(e)} | {resource_icons(e)} | {new_dataset_cell(e)} |"
        for e in entries
    ]
    footer = f"\n\nTotal entries: {len(rows)}\n"
    README.write_text(
        header + "\n".join(survey_rows) + header_refs + "\n".join(rows) + footer,
        encoding="utf-8",
    )
    print(f"Written {len(rows)} entries to {README}")


if __name__ == "__main__":
    # load CCF ranks once
    CCF_CACHE = {}
    if CCF_JSON.exists():
        data = json.loads(CCF_JSON.read_text(encoding="utf-8"))
        CCF_CACHE = {
            normalize_abbr(entry["abbr"]): entry["rank"] for entry in data.get("list", [])
        }
    main()
