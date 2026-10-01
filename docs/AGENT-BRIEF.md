# Brief for content writers (internal, never rendered)

Project root: `C:\Users\luana\SSD-Antigo-Lucia\Projetos\operaconcretepavers`. Static site generator in Python; content is Python modules that return page dicts. Site: operaconcretepavers.com — Opera Concrete & Pavers, two crews (Orlando unit, Sarasota unit).

## Read first, in this order

1. `docs/WRITING-GUIDE.md` — voice, the never-invent rule, keyword and "best/near me" rules, banned phrases. **Binding.**
2. `research/facts.md` — the verified facts with sources (prices, Florida law and licensing, permits, soils, climate, specs). Source ids for `src("id")` / `sources=[...]` are the keys of `research/sources.json`. Facts marked UNVERIFIED there may not be stated.
3. `site/_helpers.py` — the only helpers you may use to build HTML and links.
4. `site/_data.py` — services (keys, routes), cities (slugs, counties, tiers, unit), `site/_prices.json` (market ranges: use `price("key")`, `per("key")`).
5. `site/_posts.py` — every blog, compare, cost and FAQ URL that exists or is being written in parallel. **Link only to routes in `_data.py` or `_posts.py`** (plus `/`, `/concrete/`, `/pavers/`, `/cost/`, `/service-areas/`, `/central-florida/`, `/sarasota-manatee/`, `/blog/`, `/compare/`, `/permits/`, `/about/`, `/contact/`, `/process/`). Other writers are producing those pages right now, so linking to them is fine.
6. `research/questions.csv` and `research/keywords.csv` — each question/keyword has ONE owner page (column `owner_page`). Answer the questions your page owns; do not answer questions owned by another page beyond one linking sentence.

## Rules of the road

- Write only the file(s) you were assigned, in `site/content/` (or `site/bank/`). Do **not** edit `_data.py`, `_helpers.py`, `_posts.py`, `templates.py`, `build.py`, anything in `qa/`, or another writer's module. Do **not** run `python site/build.py` (other writers are working at the same time and the build wipes `dist/`).
- Check your work from the project root with `python qa/check_module.py <your_module>` (pages) or `python qa/check_bank.py <your_bank>` (banks), and `python qa/cross_check.py <your_module>` for pages once `site/dist` exists. Iterate until every line says `OK`. Word-count floors are real: add substance (a table, a worked example, an exception, a local fact), never padding.
- Research on the web whenever you state something local, legal, regulatory or a price that isn't already in `research/facts.md`. Cite it inline with `ext(url, "label")` and/or add `(label, url)` to `sources=[...]`. Prefer primary sources. If you can't verify it, leave it out.
- Python: write the file with the Write tool (not a shell heredoc). Use double-quoted Python strings around text containing apostrophes, or triple quotes. f-strings: escape braces. Use `–` for ranges. No emojis.
- Every page: unique title (≤ 60 chars if possible, 65 max), meta 120–160 chars, H1 different from the title, a 40–70 word capsule as `lede`, at least 6 internal links in running text, a `sources` list when you cite anything.
- No sentence of 8+ words may appear on two pages. Don't reuse your own paragraphs across pages.
- Never mention other contractors' sites or brands named in the writing guide's "never mention" list.

## Report back (your final message)

Files written; pages and word counts (paste the final check output); sources you added; anything you could not verify and therefore left out; any route you linked to that is not in `_data.py`/`_posts.py`.
