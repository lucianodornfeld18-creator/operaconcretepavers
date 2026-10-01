# -*- coding: utf-8 -*-
"""Merge the research part files (scratchpad part*.md) into research/facts.md and research/sources.json.
Usage: python research/merge_facts.py <dir-with-part-files>"""
import json
import pathlib
import re
import sys

src = pathlib.Path(sys.argv[1])
out = pathlib.Path(__file__).parent
parts = sorted(src.glob("part*.md"))
facts, sources = ["# Research facts — operaconcretepavers.com (as of 2026-10-01)", "",
                  "Internal. Every bullet carries its source. Writers may only state facts that are here or that they research and cite themselves.", ""], {}
for p in parts:
    t = p.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(.*?)```", t, flags=re.S)
    body = re.sub(r"```json\s*.*?```", "", t, flags=re.S).strip()
    facts += [f"<!-- from {p.name} -->", body, ""]
    for b in blocks:
        try:
            d = json.loads(b)
        except Exception as e:
            print("bad json in", p.name, e)
            continue
        for k, v in d.items():
            if isinstance(v, dict):
                v = [v.get("label") or v.get("title") or k, v.get("url")]
            if isinstance(v, str):
                v = [k, v]
            sources.setdefault(k, [v[0], v[1]])
(out / "facts.md").write_text("\n".join(facts), encoding="utf-8")
(out / "sources.json").write_text(json.dumps(sources, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"{len(parts)} parts -> facts.md; {len(sources)} sources")
