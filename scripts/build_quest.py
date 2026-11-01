#!/usr/bin/env python3
"""Build quest/data.js from the Markdown questions in this repository.

Every <details><summary>question</summary> answer </details> block becomes a card.
Exercise tables (rows linking to exercise and solution files) become quests.

Usage: python3 scripts/build_quest.py
"""

import hashlib
import json
import os
import posixpath
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "quest", "data.js")
REPO_URL = "https://github.com/Va1halla/devops-exercises/blob/master/"
SKIP_DIRS = {"perl"}

# Display names for topic folders (the first heading of a README is not always the name).
TITLES = {
    "ansible": "Ansible", "argo": "Argo", "aws": "AWS", "azure": "Azure",
    "chaos_engineering": "Chaos Engineering", "cicd": "CI/CD", "circleci": "CircleCI",
    "cloud": "Облака", "containers": "Контейнеры", "databases": "Базы данных",
    "datadog": "Datadog", "devops": "DevOps", "dns": "DNS", "gcp": "Google Cloud",
    "git": "Git", "go": "Go", "grafana": "Grafana", "kafka": "Kafka",
    "kubernetes": "Kubernetes", "linux": "Linux", "observability": "Наблюдаемость",
    "openshift": "OpenShift", "python": "Python", "security": "Безопасность",
    "shell": "Shell", "soft_skills": "Soft Skills", "software_development": "Разработка ПО",
    "sre": "SRE", "system_design": "System Design", "terraform": "Terraform", "zuul": "Zuul",
    "sql": "SQL", "os": "Операционные системы", "node": "Node.js",
}

# Sections of the main README that are not question topics.
README_SKIP = {
    "приложения для devops", "дополнительные проекты devops и sre", "благодарности",
    "лицензия",
}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
SUMMARY_RE = re.compile(r"<summary>(.*?)</summary>", re.S)
SRC_RE = re.compile(r'(src=")([^"]+)(")')
MD_LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\))")
TAG_RE = re.compile(r"<[^>]+>")


def clean_heading(text):
    text = TAG_RE.sub("", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return text.strip()


def resolve(link, md_path):
    """Make a link from md_path usable from the quest page."""
    if re.match(r"^[a-z]+:", link) or link.startswith("#") or link.startswith("//"):
        return link
    anchor = ""
    if "#" in link:
        link, anchor = link.split("#", 1)
        anchor = "#" + anchor
    base = posixpath.dirname(os.path.relpath(md_path, ROOT).replace(os.sep, "/"))
    target = posixpath.normpath(posixpath.join(base, link))
    if target.startswith(".."):
        return link + anchor
    if re.search(r"\.(png|jpe?g|gif|svg|webp)$", target, re.I):
        return "../" + target
    return REPO_URL + target + anchor


def fix_links(text, md_path):
    text = SRC_RE.sub(lambda m: m.group(1) + resolve(m.group(2), md_path) + m.group(3), text)
    return MD_LINK_RE.sub(
        lambda m: m.group(1) + resolve(m.group(2), md_path) + m.group(3), text)


def clean_answer(body):
    body = body.strip()
    body = re.sub(r"^<br>\s*", "", body)
    body = re.sub(r"^<b>", "", body).strip()
    body = re.sub(r"</b>\s*$", "", body).strip()
    return body


def parse_file(md_path, topic_of):
    """Yield (topic, section, question, answer) for each <details> block."""
    with open(md_path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    section = ""
    topic = None
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence:
            m = HEADING_RE.match(line)
            if m:
                level, title = len(m.group(1)), clean_heading(m.group(2))
                new_topic = topic_of(level, title)
                if new_topic is not None:
                    topic, section = new_topic, ""
                elif level >= 2:
                    section = title
            elif line.strip().startswith("<details>") and topic:
                block = []
                depth = 0
                j = i
                while j < len(lines):
                    block.append(lines[j])
                    depth += lines[j].count("<details>") - lines[j].count("</details>")
                    if depth <= 0:
                        break
                    j += 1
                text = "\n".join(block)
                sm = SUMMARY_RE.search(text)
                if sm:
                    question = sm.group(1).strip()
                    answer = text[sm.end():]
                    answer = re.sub(r"</details>\s*$", "", answer.strip())
                    yield topic, section, question, clean_answer(answer)
                i = j
        i += 1


def parse_exercises(md_path):
    """Yield (name, exercise_url, solution_url) from exercise tables."""
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("|"):
                continue
            links = re.findall(r"\[([^\]]+)\]\(([^)\s]+\.md[^)\s]*)\)", line)
            if not links:
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            name = clean_heading(cells[0]) if cells else links[0][0]
            ex = resolve(links[0][1], md_path)
            sol = resolve(links[1][1], md_path) if len(links) > 1 else ""
            yield name, ex, sol


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w]+", "-", text)
    return text.strip("-") or "topic"


def main():
    topics = {}
    order = []

    def topic_entry(tid, title, icon, source):
        if tid not in topics:
            topics[tid] = {"id": tid, "title": title, "icon": icon, "source": source,
                           "cards": [], "quests": []}
            order.append(tid)
        return topics[tid]

    def add_cards(md_path, topic_of):
        for tid, section, question, answer in parse_file(md_path, topic_of):
            topics[tid]["cards"].append({
                "s": section,
                "q": fix_links(question, md_path),
                "a": fix_links(answer, md_path),
            })

    # 1. Topic folders.
    tdir = os.path.join(ROOT, "topics")
    for name in sorted(os.listdir(tdir)):
        path = os.path.join(tdir, name)
        if name in SKIP_DIRS or not os.path.isdir(path):
            continue
        readme = os.path.join(path, "README.md")
        title = TITLES.get(name, name.replace("_", " ").title())
        if name not in TITLES and os.path.exists(readme):
            with open(readme, encoding="utf-8") as f:
                for line in f:
                    m = HEADING_RE.match(line)
                    if m and len(m.group(1)) == 1 and "{" not in line:
                        title = clean_heading(m.group(2))
                        break
        topic_entry(name, title, "", "topics/" + name)
        for dirpath, _, files in os.walk(path):
            for fn in sorted(files):
                if not fn.endswith(".md"):
                    continue
                md = os.path.join(dirpath, fn)
                add_cards(md, lambda level, t, n=name: n)
                if fn == "README.md":
                    for q in parse_exercises(md):
                        topics[name]["quests"].append(
                            {"n": q[0], "e": q[1], "s": q[2]})

    # 2. Inline sections of the main README.
    readme = os.path.join(ROOT, "README.md")

    def readme_topic(level, title):
        if level != 2:
            return None
        if title.lower() in README_SKIP:
            return "__skip__"
        # A README section about a topic that also has a folder joins that topic.
        for t in topics.values():
            if t.get("title", "").lower() == title.lower():
                return t["id"]
        tid = "readme-" + slugify(title)
        topic_entry(tid, title, "", "README.md")
        return tid

    topics["__skip__"] = {"id": "__skip__", "cards": [], "quests": []}
    add_cards(readme, readme_topic)
    del topics["__skip__"]

    # Icons from the topics table of the main README.
    with open(readme, encoding="utf-8") as f:
        head = f.read().split("<!-- ALL-TOPICS-LIST:END -->")[0]
    for href, src in re.findall(r'<a href="([^"]+)"><img src="([^"]+)"', head):
        m = re.match(r"topics/([^/]+)/", href)
        tid = m.group(1) if m else None
        if href.startswith("#"):
            for t in topics.values():
                if t["source"] == "README.md" and slugify(t["title"]) == slugify(
                        href[1:].replace("-", " ")):
                    tid = t["id"]
        if tid in topics and not topics[tid]["icon"]:
            topics[tid]["icon"] = "../" + src

    result = [topics[t] for t in order if topics[t]["cards"] or topics[t]["quests"]]
    for t in result:
        seen = set()
        for c in t["cards"]:
            # Stable id: progress survives reordering and edits elsewhere in the file.
            h = hashlib.sha1((t["id"] + "|" + c["q"]).encode("utf-8")).hexdigest()[:10]
            while h in seen:
                h += "x"
            seen.add(h)
            c["id"] = h
    total = sum(len(t["cards"]) for t in result)
    quests = sum(len(t["quests"]) for t in result)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// Generated by scripts/build_quest.py. Do not edit by hand.\n")
        f.write("window.QUEST_DATA = ")
        json.dump({"topics": result}, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    print("topics: %d, cards: %d, quests: %d -> %s" % (len(result), total, quests, OUT))


if __name__ == "__main__":
    main()
