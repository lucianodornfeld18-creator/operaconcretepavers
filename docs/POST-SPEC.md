# Blog posts (internal, never rendered)

Read docs/WRITING-GUIDE.md, docs/AGENT-BRIEF.md and research/facts.md first.

Your module `site/content/c_posts_<x>.py` writes the posts whose module is "c_posts_<x>" in `site/_posts.py` POSTS (slug -> (working H1, module, services, region)). The plan for each post (primary keyword, secondary keywords, intent, why it is distinct from its nearest page) is in `research/blog-plan.csv`; questions the post must answer are the rows in `research/questions.csv` whose owner_page is `/blog/<slug>/`.

```python
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext, price, per, contact, photo
from _photos import for_service

def p_slug():
    return page("/blog/<slug>/", "post", "<title ≤60, keyword first>", "<meta 120–160>", "<H1 = working H1 or close>",
                capsule("…40–70 word direct answer, a number with unit, 'as of October 2026', the place…"),
                body, faqs=[…3–5…], sources=[…], related=[…3–5 (route, label)…], crumbs=[("Blog", "/blog/")],
                published="2026-10-01", service="<first service in the registry entry>", image=<a photo id from for_service(...) or None>, form=False)
```

- 1,200–2,500 words. Structure: answer first (capsule), then H2s phrased as the questions people actually ask, each opening with a 40–70 word direct answer, then detail, tables, steps, a short "say you have…" example where useful. H3s inside long sections.
- Link to the commercial page of the cluster (the service page, via svc()) in the first two paragraphs, and to the cost guide, 1 compare page and 2–4 other posts or services where natural. At least 6 internal links.
- The post must not compete with the service page or cost page: it answers its own intent (see why_it_is_distinct in blog-plan.csv). Don't restate the service page's spec table or the cost page's price tables; link to them.
- Region-specific posts (region = orlando / sarasota) stay in that region; "both" posts cover both and say where rules differ.
- Permit/HOA posts: use research/facts.md parts 3a/3b and 5 exactly, with each jurisdiction's department and link; mark anything the research marks [excerpt]/[snippet] as "confirm with the office"; never guess a rule.
- Hiring and quote posts: criteria only (certificate of insurance from the agent, Sunbiz lookup, written itemized scope, who handles the permit and HOA paperwork, a payment schedule that doesn't run ahead of the work, Notice of Commencement over $2,500), never claims about ourselves; one "best … near me" phrasing as the reader's question. No licence lookups, no F.S. 489.x, no "how to choose a contractor" posts (the six that existed were removed on 2026-10-23 and 301 to the quote-comparison post, /permits/ and /artificial-turf/).
- Don't call price_note(). Never claim track records, insurance, warranty or response times, and never mention licences at all. Never print unverified temperatures.
- One photo via photo(pid, caption) if a relevant one exists (captions describe only what is visible).
