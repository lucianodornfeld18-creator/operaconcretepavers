# -*- coding: utf-8 -*-
"""Static site builder for operaconcretepavers.com:  python site/build.py  ->  site/dist/"""
import base64
import csv
import datetime
import hashlib
import html as htmlmod
import importlib
import json
import pathlib
import re
import shutil
import sys
import time

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "content"))
from templates import render_page, SITE_JS  # noqa: E402
from _data import (BASE_URL, DOMAIN, PUBLIC_NAME, BUSINESS, SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, COUNTIES, COUNTY_ORDER, EMAIL,  # noqa: E402
                   REVIEWED, LAUNCH_DATE, PRICES, PRICE_DATE, UNITS, UNIT_ORDER, price_range)

DIST = ROOT / "dist"
SECTIONS = ["core", "services", "areas", "city-services", "blog", "faq", "cost"]


def load_pages():
    pages, seen = [], {}
    import os
    skip = {x.strip() for x in os.environ.get("SKIP", "").split(",") if x.strip()}   # SKIP=c_posts_a,c_posts_b leaves unfinished modules out of a deploy
    mods = sorted(f.stem for f in (ROOT / "content").glob("c_*.py") if f.stem not in skip)
    for name in mods:
        mod = importlib.import_module(name)
        got = mod.get_pages()
        for p in got:
            if p["route"] in seen:
                raise SystemExit(f"[build] DUPLICATE ROUTE {p['route']} in {seen[p['route']]} and {name}")
            if not (p["route"].startswith("/") and p["route"].endswith("/")):
                raise SystemExit(f"[build] BAD ROUTE {p['route']} in {name}")
            seen[p["route"]] = name
            p["_module"] = name
            p.setdefault("_lastmod", p.get("updated", REVIEWED))
            pages.append(p)
        print(f"[build] {name:<28} {len(got):>4} page(s)")
    return pages


def _cols(items):
    return '<ul class="cols">' + "".join(f'<li><a href="{r}">{t}</a></li>' for r, t in items) + "</ul>"


def autolink(pages):
    """Generated link blocks (class="auto", ignored by the similarity check)."""
    cs = {}
    for p in pages:
        if p["kind"] == "cityservice":
            cs.setdefault(p["service"], []).append(p)
    city_pages = {p["city"]: p for p in pages if p["kind"] == "city" and p.get("city")}
    posts = sorted([p for p in pages if p["kind"] == "post"], key=lambda p: p["route"])

    def areas_by_county(filter_fn=lambda s: True, linkfn=None, units=None):
        html = ""
        for co in COUNTY_ORDER:
            if units and COUNTIES[co]["unit"] not in units:
                continue
            items = [(linkfn(s) if linkfn else CITIES[s]["route"], CITIES[s]["name"]) for s in CITY_ORDER if CITIES[s]["county"] == co and filter_fn(s)]
            if items:
                html += f'<h3>{COUNTIES[co]["name"]}</h3>' + _cols(items)
        return html

    for p in pages:
        b = p["body"]
        if p["kind"] == "service" and p.get("service") in cs:
            have = {q["city"]: q["route"] for q in cs[p["service"]]}
            block = f'<section class="auto" id="areas"><h2>{SERVICES[p["service"]]["name"]} by city</h2><p>Each local page covers that town\'s permit office, soil, HOA approvals and weather.</p>' + areas_by_county(lambda s: s in have, lambda s: have[s]) + "</section>"
            b = b.replace("<!--AUTO:service-cities-->", block) if "<!--AUTO:service-cities-->" in b else b + block
        if p["kind"] == "city" and p.get("city"):
            mine = sorted([q for q in pages if q["kind"] == "cityservice" and q["city"] == p["city"]], key=lambda q: SERVICE_ORDER.index(q["service"]))
            if mine:
                block = f'<section class="auto" id="services"><h2>Services in {CITIES[p["city"]]["name"]}</h2>' + _cols([(q["route"], SERVICES[q["service"]]["name"]) for q in mine]) + "</section>"
                b = b.replace("<!--AUTO:city-services-->", block) if "<!--AUTO:city-services-->" in b else b + block
        if p["kind"] == "unit" and p.get("unit"):
            block = '<section class="auto" id="towns"><h2>Towns this crew covers</h2>' + areas_by_county(lambda s: s in city_pages, units=[p["unit"]]) + "</section>"
            b = b.replace("<!--AUTO:unit-cities-->", block) if "<!--AUTO:unit-cities-->" in b else b + block
        if "<!--AUTO:all-areas-->" in b:
            b = b.replace("<!--AUTO:all-areas-->", '<section class="auto">' + areas_by_county(lambda s: s in city_pages) + "</section>")
        if "<!--AUTO:blog-index-->" in b:
            b = b.replace("<!--AUTO:blog-index-->", '<ul class="grid">' + "".join(f'<li class="card"><h3><a href="{q["route"]}">{q["h1"]}</a></h3><p>{q["meta"]}</p></li>' for q in posts) + "</ul>")
        p["body"] = b
    return pages


def soften_links(html, routes, missing):
    """Links to pages that are not written yet render as plain text, so no deploy ever ships a broken internal link."""
    def fix(m):
        href = m.group(1)
        path = href.split("#")[0].split("?")[0]
        if not path or path in routes or path.startswith("/static/") or re.search(r"\.(xml|txt|ico|png|svg|webmanifest|js|webp)$", path):
            return m.group(0)
        missing[path] = missing.get(path, 0) + 1
        return m.group(3)
    html = re.sub(r'<li>\s*<a href="(/[^"]*)"([^>]*)>(.*?)</a>\s*</li>', lambda m: m.group(0) if (m.group(1).split("#")[0] in routes) else (missing.__setitem__(m.group(1), missing.get(m.group(1), 0) + 1) or ""), html, flags=re.S)
    return re.sub(r'<a href="(/[^"]*)"([^>]*)>(.*?)</a>', fix, html, flags=re.S)


def visible_text(html):
    m = re.search(r"<main.*?</main>", html, flags=re.S)
    t = m.group(0) if m else html
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<form.*?</form>|<nav.*?</nav>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return htmlmod.unescape(re.sub(r"\s+", " ", t)).strip()


def email_off(html):
    """Wrap mailto links and bare addresses in <!--email_off--> so Cloudflare's obfuscation skips them (scripts untouched)."""
    from _data import EMAIL
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"

    html = re.sub(r"<script\b.*?</script>", hold, html, flags=re.S)
    html = re.sub(r'<a href="mailto:[^"]+"[^>]*>.*?</a>', lambda m: "<!--email_off-->" + m.group(0) + "<!--/email_off-->", html, flags=re.S)
    html = re.sub(r"<!--email_off-->.*?<!--/email_off-->", hold, html, flags=re.S)
    if EMAIL:
        html = html.replace(EMAIL, "<!--email_off-->" + EMAIL + "<!--/email_off-->")
    return re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], html)


def section_of(p):
    k = p["kind"]
    return {"service": "services", "pillar": "services", "city": "areas", "unit": "areas", "cityservice": "city-services", "post": "blog", "compare": "blog", "faq": "faq", "price": "cost", "tool": "cost"}.get(k, "core")


def page_images(html):
    """Largest published variant of every project photo used on the page, for the image sitemap extension."""
    best = {}
    for stem, w in re.findall(r'(/static/img/photos/[a-z0-9-]+?)-(\d+)\.webp', html):
        best[stem] = max(best.get(stem, 0), int(w))
    return "".join(f"<image:image><image:loc>{BASE_URL}{stem}-{w}.webp</image:loc></image:image>" for stem, w in sorted(best.items()))


def write_sitemaps(pages, rendered):
    buckets = {s: [] for s in SECTIONS}
    for p in pages:
        if p.get("noindex") or p["route"] in ("/404/",):
            continue
        buckets[section_of(p)].append(p)
    idx = []
    for s, ps in buckets.items():
        if not ps:
            continue
        urls = "\n".join(f"  <url><loc>{BASE_URL}{p['route']}</loc><lastmod>{p['_lastmod']}</lastmod>{page_images(rendered.get(p['route'], ''))}</url>" for p in ps)
        (DIST / f"sitemap-{s}.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n{urls}\n</urlset>\n', encoding="utf-8")
        idx.append(f"  <sitemap><loc>{BASE_URL}/sitemap-{s}.xml</loc><lastmod>{max(p['_lastmod'] for p in ps)}</lastmod></sitemap>")
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(idx) + "\n</sitemapindex>\n", encoding="utf-8")


def write_robots():
    bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "Applebot", "DuckDuckBot", "GPTBot", "Google-Extended", "Applebot-Extended", "CCBot"]
    body = "User-agent: *\nAllow: /\nDisallow: /thank-you/\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {BASE_URL}/sitemap.xml\n"
    (DIST / "robots.txt").write_text(body, encoding="utf-8")


def write_llms(pages, rendered):
    by_kind = {}
    for p in pages:
        if not p.get("noindex"):
            by_kind.setdefault(p["kind"], []).append(p)

    def block(title, ps):
        return [f"## {title}", ""] + [f"- [{re.sub('<[^>]+>', '', p['h1'])}]({BASE_URL}{p['route']}): {p['meta']}" for p in ps] + [""]
    units = []
    for u in UNIT_ORDER:
        U = UNITS[u]
        units.append(f"- {U['name']} crew: {BASE_URL}{U['route']}" + (f" (phone {U['phone_display']})" if U["phone_display"] else ""))
    facts = [f"- {SERVICES[k]['name']}: {price_range(SERVICES[k]['price'])} per {PRICES[SERVICES[k]['price']][4]} ({PRICE_DATE} Florida market range, not a quote)" for k in SERVICE_ORDER if SERVICES[k]["price"] in PRICES]
    lines = [f"# {PUBLIC_NAME}", "", f"> {BUSINESS['blurb']}", "", f"- Website: {BASE_URL}"] + ([f"- Email: {EMAIL}"] if EMAIL else []) + units + \
            [f"- Service area: {BUSINESS['service_area_short']}.", f"- Facts last reviewed: {REVIEWED}", "", "## Price ranges published on this site (sources on each page)", ""] + facts + [""]
    lines += block("Services", by_kind.get("pillar", []) + by_kind.get("service", []))
    lines += block("Cost guides", by_kind.get("price", []) + by_kind.get("tool", []))
    lines += block("Permits and HOA rules", by_kind.get("permit", []))
    lines += block("Service areas", by_kind.get("unit", []) + by_kind.get("city", []))
    lines += block("Comparisons", by_kind.get("compare", []))
    lines += block("FAQ", by_kind.get("faq", []))
    lines += block("Articles", by_kind.get("post", []))
    (DIST / "llms.txt").write_text("\n".join(lines), encoding="utf-8")
    full = [f"# {PUBLIC_NAME} — full text", ""]
    for p in pages:
        if p.get("noindex") or p["kind"] == "cityservice":
            continue
        full += [f"## {p['title']}", f"URL: {BASE_URL}{p['route']}", f"Updated: {p['_lastmod']}", "", visible_text(rendered[p["route"]]), ""]
    (DIST / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")


def write_feed(pages):
    posts = sorted([p for p in pages if p["kind"] == "post"], key=lambda p: p.get("published", LAUNCH_DATE), reverse=True)
    items = "".join(f"<item><title>{htmlmod.escape(p['h1'])}</title><link>{BASE_URL}{p['route']}</link><guid>{BASE_URL}{p['route']}</guid><pubDate>{datetime.datetime.fromisoformat(p.get('published', LAUNCH_DATE)).strftime('%a, %d %b %Y 12:00:00 +0000')}</pubDate><description>{htmlmod.escape(p['meta'])}</description></item>" for p in posts)
    (DIST / "feed.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{PUBLIC_NAME} blog</title><link>{BASE_URL}/blog/</link><description>Straight answers about concrete, pavers and artificial turf in Florida.</description><language>en-us</language>{items}</channel></rss>', encoding="utf-8")


def indexnow_key():
    f = ROOT / "indexnow-key.txt"
    if not f.exists():
        f.write_text(hashlib.sha256((DOMAIN + str(time.time())).encode()).hexdigest()[:32], encoding="utf-8")
    key = f.read_text(encoding="utf-8").strip()
    (DIST / f"{key}.txt").write_text(key, encoding="utf-8")
    return key


def inline_script_hashes():
    hashes = set()
    for f in DIST.rglob("*.html"):
        for m in re.finditer(r"<script(?P<a>[^>]*)>(?P<b>.*?)</script>", f.read_text(encoding="utf-8"), flags=re.S):
            if "src=" in m.group("a") or "ld+json" in m.group("a") or not m.group("b").strip():
                continue
            hashes.add("'sha256-" + base64.b64encode(hashlib.sha256(m.group("b").encode()).digest()).decode() + "'")
    return sorted(hashes)


def write_headers():
    csp = "; ".join([
        "default-src 'self'", "script-src 'self' " + " ".join(inline_script_hashes() + ["https://static.cloudflareinsights.com"]), "style-src 'self' 'unsafe-inline'",
        "img-src 'self' data:", "font-src 'self'", "connect-src 'self' https://cloudflareinsights.com https://opera-portal.lucianodornfeld18.workers.dev",
        "form-action 'self' https://opera-portal.lucianodornfeld18.workers.dev https://operaconcretepavers.com", "base-uri 'self'", "object-src 'none'", "frame-ancestors 'self'", "upgrade-insecure-requests"])
    (DIST / "_headers").write_text(f"""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  Cross-Origin-Opener-Policy: same-origin
  Content-Security-Policy: {csp}

https://:project.pages.dev/*
  X-Robots-Tag: noindex, nofollow

https://:branch.:project.pages.dev/*
  X-Robots-Tag: noindex, nofollow

/static/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/static/img/*
  Cache-Control: public, max-age=31536000, immutable
/static/site.*.js
  Cache-Control: public, max-age=31536000, immutable
/sitemap*.xml
  Cache-Control: public, max-age=3600
/llms*.txt
  Cache-Control: public, max-age=3600
""", encoding="utf-8")
    (DIST / "_redirects").write_text("/index.html / 301\n/home / 301\n/pricing/ /cost/ 301\n/services/ /concrete/ 301\n/turf/ /artificial-turf/ 301\n/thanks/ /thank-you/ 301\n", encoding="utf-8")


def write_static():
    dst = DIST / "static"
    shutil.copytree(ROOT / "static", dst)
    shutil.move(str(dst / "site.js"), str(DIST / SITE_JS.lstrip("/")))
    for name in ("favicon.ico",):
        if (ROOT / "static" / "img" / name).exists():
            shutil.copy(ROOT / "static" / "img" / name, DIST / name)
    (DIST / "site.webmanifest").write_text(json.dumps({"name": PUBLIC_NAME, "short_name": "Opera", "start_url": "/", "display": "browser", "background_color": "#FFFFFF", "theme_color": "#111111",
                                                       "icons": [{"src": "/static/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/static/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}), encoding="utf-8")


def write_reports(pages, rendered):
    out = ROOT.parent / "research"
    out.mkdir(exist_ok=True)
    with open(out / "titles-metas.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["route", "kind", "title", "title_len", "h1", "meta", "meta_len", "words", "html_kb", "noindex"])
        for p in pages:
            h = rendered[p["route"]]
            w.writerow([p["route"], p["kind"], p["title"], len(p["title"]), re.sub("<[^>]+>", "", p["h1"]), p["meta"], len(p["meta"]), len(visible_text(h).split()), round(len(h.encode()) / 1024, 1), bool(p.get("noindex"))])


def main():
    t0 = time.time()
    if DIST.exists():
        for _ in range(5):
            try:
                shutil.rmtree(DIST)
                break
            except PermissionError:
                time.sleep(0.5)
    DIST.mkdir(parents=True)
    pages = autolink(load_pages())
    rendered, missing = {}, {}
    routes = {p["route"] for p in pages}
    for p in pages:
        out = DIST if p["route"] == "/" else DIST / p["route"].strip("/")
        out.mkdir(parents=True, exist_ok=True)
        html = email_off(soften_links(render_page(p), routes, missing))
        for dup, one in (("installed installed", "installed"), ("of wall face of wall face", "of wall face"), ("(clean, re-sand, seal) (clean, re-sand, seal)", "(clean, re-sand, seal)")):
            html = html.replace(dup, one)
        (out / "index.html").write_text(html, encoding="utf-8")
        rendered[p["route"]] = html
    if (DIST / "404" / "index.html").exists():
        shutil.copy(DIST / "404" / "index.html", DIST / "404.html")
    write_static()
    write_robots()
    write_sitemaps(pages, rendered)
    write_llms(pages, rendered)
    write_feed(pages)
    key = indexnow_key()
    write_headers()
    write_reports(pages, rendered)
    kinds = {}
    for p in pages:
        kinds[p["kind"]] = kinds.get(p["kind"], 0) + 1
    print(f"\n[build] {len(pages)} pages in {time.time() - t0:.1f}s -> {DIST}\n[build] by kind: {kinds}\n[build] IndexNow key {key}")


if __name__ == "__main__":
    main()
