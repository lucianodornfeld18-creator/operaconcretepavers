# -*- coding: utf-8 -*-
"""Authoring helpers. Content modules import from here and return page dicts via page()."""
import html as _html
import re

from _photos import info as _pinfo, url as _purl, has as _phas
from _data import (BASE_URL, PUBLIC_NAME, REVIEWED, SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, COUNTIES, SOURCES, PRICES, PRICE_DATE,
                   PRICE_LABEL, UNITS, price_range, price_unit, city_service_route, nearest, TIER_SERVICES, unit_phone)


def esc(s):
    return _html.escape(str(s), quote=True)


# ---------------------------------------------------------------- links
def a(route, text, title=None):
    """Internal link. Routes are checked after the build; a link to a page not built yet renders as plain text."""
    t = f' title="{esc(title)}"' if title else ""
    return f'<a href="{route}"{t}>{text}</a>'


def svc(key, text=None):
    return a(SERVICES[key]["route"], text or SERVICES[key]["name"].lower())


def city(slug, text=None):
    return a(CITIES[slug]["route"], text or CITIES[slug]["name"])


def cs(city_slug, service, text=None):
    return a(city_service_route(city_slug, service), text or f"{SERVICES[service]['name'].lower()} in {CITIES[city_slug]['name']}")


def post(slug, text):
    return a(f"/blog/{slug}/", text)


def compare(slug, text):
    return a(f"/compare/{slug}/", text)


def ext(url, text):
    return f'<a href="{esc(url)}" rel="noopener">{text}</a>'


def src(sid, text=None):
    label, url = SOURCES[sid]
    return ext(url, text or label)


def contact(text="request a free estimate"):
    return a("/contact/", text)


def tel(unit, text=None):
    """Phone link for a unit; until the owner adds the number it falls back to the estimate form."""
    e164, disp = unit_phone(unit)
    if not e164:
        return a("/contact/", text or "send us the project details")
    return f'<a class="tel" href="tel:{e164}">{text or disp}</a>'


# ---------------------------------------------------------------- blocks
def capsule(html):
    """40-70 word direct answer that must stand alone if quoted."""
    return f'<p class="capsule">{html}</p>'


def sec(h2, html, sid=None):
    i = f' id="{sid}"' if sid else ""
    return f'<section{i}><h2>{h2}</h2>\n{html}\n</section>'


def table(caption, headers, rows, note=None):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    trs = []
    for r in rows:
        tds = "".join((f'<th scope="row">{c}</th>' if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r))
        trs.append(f"<tr>{tds}</tr>")
    n = f'<p class="tnote">{note}</p>' if note else ""
    return f'<div class="tw" role="region" aria-label="{esc(re.sub("<[^>]+>", "", caption))}" tabindex="0"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>{n}'


def steps(items):
    return "<ol class=\"steps\">" + "".join(f"<li><strong>{t}</strong> {d}</li>" for t, d in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def faq(q, a_html):
    return (q, a_html)


def note(html):
    return f'<p class="note">{html}</p>'


def price(key, typical=False):
    return price_range(key, typical)


def per(key):
    return price_unit(key)


def price_note():
    return f"{PRICE_LABEL}, {PRICE_DATE}, compiled from published contractor pricing and national cost guides. A written quote follows a site visit."


def offer(key):
    lo, hi, _, _, unit, _ = PRICES[key]
    return (lo, hi, unit)


def cta(text="Get a free estimate", sub=None):
    s = f"<p>{sub}</p>" if sub else ""
    return f'<aside class="cta"><div>{s}<p class="cta-row"><a class="btn" href="#quote">{text}</a> <span>Free on-site estimates in Greater Orlando and Sarasota–Manatee.</span></p></div></aside>'


# ---------------------------------------------------------------- page constructor
def page(route, kind, title, meta, h1, lede, body, faqs=None, sources=None, related=None, crumbs=None, **kw):
    """kind: home | pillar | service | cityservice | city | unit | price | permit | post | faq | compare | tool | page | about | contact | plain
    lede: capsule html under the H1. faqs: list of faq(). sources: list of SOURCES ids or (label, url). related: list of (route, label).
    crumbs: list of (label, route) after Home. Extra keys: noindex, service, city, unit, form (bool), form2 (bool), image/hero_photo,
    schema (list of dicts), published, howto=(name, [(step, text)]), offer=(lo, hi, unit), wide (bool), eyebrow, hero_extra."""
    p = {"route": route, "kind": kind, "title": title, "meta": meta, "h1": h1, "lede": lede, "body": body,
         "faqs": faqs or [], "sources": sources or [], "related": related or [], "crumbs": crumbs or []}
    p.update(kw)
    return p


# ---------------------------------------------------------------- photos
PH_SIZES = "(max-width:860px) calc(100vw - 40px), 780px"


def photo(pid, caption=None, sizes=None, eager=False):
    if not _phas(pid):
        return ""
    d = _pinfo(pid)
    srcset = ", ".join(f"{_purl(pid, w)} {w}w" for w in d["widths"])
    mid = d["widths"][min(1, len(d["widths"]) - 1)]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return (f'<figure class="ph"><img src="{_purl(pid, mid)}" srcset="{srcset}" sizes="{sizes or PH_SIZES}" width="{d["w"]}" height="{d["h"]}" '
            f'alt="{esc(d["alt"])}" {load} decoding="async">{cap}</figure>')


def thumb(pid):
    if not _phas(pid):
        return ""
    d = _pinfo(pid)
    srcset = ", ".join(f"{_purl(pid, w, thumb=True)} {w}w" for w in d["thumbs"])
    return (f'<div class="ph"><img src="{_purl(pid, 480, thumb=True)}" srcset="{srcset}" sizes="(max-width:600px) calc(100vw - 40px), 380px" '
            f'width="480" height="360" alt="{esc(d["alt"])}" loading="lazy" decoding="async"></div>')
