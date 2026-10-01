# -*- coding: utf-8 -*-
"""HTML shell, inline CSS, JSON-LD and the lead form for operaconcretepavers.com.
Visual language comes from the logo: heavy black geometric caps, a metallic-gold facet and rule, tracked small caps."""
import datetime
import hashlib
import json
import pathlib
import re

from _data import (BASE_URL, PUBLIC_NAME, EMAIL, REVIEWED, LAUNCH_DATE, SERVICES, SERVICE_ORDER, PILLARS, CITIES, CITY_ORDER, COUNTIES,
                   COUNTY_ORDER, SOURCES, BUSINESS, UNITS, UNIT_ORDER, OPERA_ENDPOINT, TAGLINE, unit_phone, any_phone)
from _helpers import esc
from _photos import info as _pinfo, url as _purl, has as _phas, ORDER as PHOTO_ORDER

ROOT = pathlib.Path(__file__).parent
_js = (ROOT / "static" / "site.js").read_bytes()
SITE_JS = "/static/site." + hashlib.sha256(_js).hexdigest()[:10] + ".js"
YEAR = datetime.date.today().year
MARK = '<svg class="mk" viewBox="-10 0 400 300" aria-hidden="true"><path fill="currentColor" d="M200 10 380 278H275L145 88z"/><path fill="#C99A45" d="M130 115 182 190 105 278H0z"/></svg>'

CSS = """
@font-face{font-family:Montserrat;src:url(/static/fonts/montserrat-latin.woff2) format("woff2");font-weight:500 900;font-style:normal;font-display:swap}
:root{--ink:#111111;--ink2:#1E1E1E;--text:#2A2A2A;--mute:#5C5852;--line:#E4DED3;--bg:#FFFFFF;--soft:#F6F3EE;--gold:#B88A3B;--gold-l:#C99A45;--gold-d:#8A6420;--gold-t:#E9D6AE;--r:6px;--w:1200px;
--head:Montserrat,"Arial Black",Arial,sans-serif;--body:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--body);font-size:1.0625rem;line-height:1.68}
img,svg{max-width:100%;height:auto}a{color:var(--gold-d);text-underline-offset:3px}a:hover{color:var(--ink)}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px;border-radius:3px}
h1,h2,h3{font-family:var(--head);color:var(--ink);line-height:1.12;margin:0 0 .5em;letter-spacing:-.01em}
h1{font-weight:900;font-size:clamp(2rem,4.6vw,3.3rem);text-transform:none}
h2{font-weight:800;font-size:clamp(1.45rem,3vw,2.05rem);margin-top:1.8em}
h2:after{content:"";display:block;width:56px;height:3px;background:var(--gold);margin-top:.45em}
.ctr h2:after,.band h2:after{margin-left:auto;margin-right:auto}
h3{font-weight:700;font-size:1.22rem;margin-top:1.4em}
p{margin:0 0 1.05em}ul,ol{margin:0 0 1.1em;padding-left:1.3em}li{margin:.3em 0}
.wrap{max-width:var(--w);margin:0 auto;padding:0 20px}.narrow{max-width:820px}
.skip{position:absolute;left:-999px;top:0;background:var(--ink);color:#fff;padding:10px 14px;z-index:9}.skip:focus{left:8px;top:8px}
.top{background:var(--ink);color:#D9D3C7;font-size:.86rem;letter-spacing:.04em}.top .wrap{display:flex;justify-content:space-between;gap:10px 18px;flex-wrap:wrap;padding-top:7px;padding-bottom:7px}.top a{color:#fff;font-weight:600;text-decoration:none}.top b{color:var(--gold-l);font-weight:600}
header.site{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:14px;min-height:76px;flex-wrap:wrap}
.brand{display:block;line-height:0}.brand img{height:60px;width:auto}
#navb{display:none;background:none;border:2px solid var(--ink);border-radius:var(--r);padding:9px 13px;min-height:44px;font:700 .9rem var(--head);color:var(--ink);cursor:pointer;letter-spacing:.06em;text-transform:uppercase}
nav.main ul{list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:0;margin:0;padding:0}nav.main a{display:block;padding:12px 10px;text-decoration:none;color:var(--ink);font:700 .8rem var(--head);letter-spacing:.08em;text-transform:uppercase;border-bottom:2px solid transparent}nav.main a:hover,nav.main a[aria-current]{border-bottom-color:var(--gold);color:var(--ink)}
nav.main a.btn{margin-left:8px;border:0;padding:12px 18px}
.btn{display:inline-block;background:var(--gold);color:var(--ink);text-decoration:none;font:800 .9rem var(--head);letter-spacing:.08em;text-transform:uppercase;padding:15px 24px;border-radius:var(--r);border:0;min-height:48px;line-height:1.3;cursor:pointer}.btn:hover{background:var(--gold-l);color:var(--ink)}
.btn.dark{background:var(--ink);color:#fff}.btn.dark:hover{background:#333;color:#fff}
.btn.ghost{background:transparent;color:#fff;box-shadow:inset 0 0 0 2px rgba(255,255,255,.75)}.btn.ghost:hover{background:#fff;color:var(--ink)}
.crumbs{font-size:.84rem;padding:14px 0 0}.crumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:4px 8px;margin:0;padding:0}.crumbs li+li:before{content:"/";margin-right:8px;opacity:.5}.crumbs a{color:inherit}
.eyebrow{font:800 .78rem var(--head);letter-spacing:.22em;text-transform:uppercase;color:var(--gold-d);margin:0 0 .9em}
.capsule{font-size:1.14rem;line-height:1.62;color:var(--ink);border-left:4px solid var(--gold);padding:2px 0 2px 16px;margin:0 0 1.1em}
.by{font-size:.88rem;color:var(--mute);margin:.4em 0 0}
/* dark hero with the form on the right (home, services, cities, city x service) */
.hero-x{position:relative;background:var(--ink);color:#EDE8DF;overflow:hidden}
.hero-x .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.45}
.hero-x:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(17,17,17,.92) 0,rgba(17,17,17,.78) 52%,rgba(17,17,17,.55) 100%)}
.hero-x .wrap{position:relative;z-index:1}
.hero-x .crumbs{color:#CFC8BB}
.hx{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:start;padding:40px 0 48px}
.hero-x h1{color:#fff}.hero-x .eyebrow{color:var(--gold-l)}.hero-x .capsule{color:#F3EEE6;border-left-color:var(--gold-l)}.hero-x .capsule a,.hero-x a{color:#F2DDB0}
.hero-x .by{color:#CFC8BB}
.rule{display:flex;align-items:center;gap:14px;margin:0 0 1em;font:700 .74rem var(--head);letter-spacing:.3em;text-transform:uppercase;color:#E9E2D5}.rule:before{content:"";flex:0 0 46px;height:2px;background:var(--gold-l)}
.ticks{list-style:none;padding:0;margin:1.2em 0 0;display:grid;grid-template-columns:1fr 1fr;gap:8px 18px;font-size:.98rem}.ticks li{margin:0;padding-left:26px;position:relative}.ticks li:before{content:"";position:absolute;left:0;top:.42em;width:14px;height:9px;border-left:3px solid var(--gold-l);border-bottom:3px solid var(--gold-l);transform:rotate(-45deg)}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:1.2em 0 .2em}
/* light hero (posts, faq, pages) */
.hero-l{background:var(--soft);border-bottom:1px solid var(--line);padding:0 0 30px}.hero-l .in{padding-top:26px}
main section{margin:0 0 .6em}
.band{background:var(--soft);padding:24px 0 34px;margin:2em 0}.band.dk{background:var(--ink);color:#E6E0D6}.band.dk h2,.band.dk h3{color:#fff}.band.dk a{color:#F2DDB0}
.ctr{text-align:center}
.grid{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));margin:1.2em 0;padding:0;list-style:none}
.card{background:#fff;border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:var(--r);padding:20px 20px 14px;margin:0}.card h3{margin:0 0 .4em;font-size:1.12rem}.card p{margin:0 0 .6em;font-size:.97rem}.card a{font-weight:700}
.card .ph{margin:-20px -20px 14px;line-height:0}.card .ph img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:var(--r) var(--r) 0 0}
.tw{overflow-x:auto;margin:1.1em 0 .4em;border:1px solid var(--line);border-radius:var(--r);background:#fff}
table{border-collapse:collapse;width:100%;font-size:.96rem}caption{caption-side:top;text-align:left;font:700 .95rem var(--head);color:var(--ink);padding:12px 14px 8px}
th,td{padding:10px 14px;text-align:left;vertical-align:top;border-top:1px solid var(--line)}thead th{background:var(--ink);color:#fff;font:700 .8rem var(--head);letter-spacing:.05em;text-transform:uppercase;border-top:0}tbody th{font-weight:600;color:var(--ink)}tbody tr:nth-child(even){background:#FBF9F5}
.tnote,.note{font-size:.92rem;color:var(--mute)}.note{background:var(--soft);border-left:3px solid var(--gold);padding:12px 16px}
.steps{padding-left:1.4em}.steps li{margin:.65em 0}.steps li::marker{font-weight:800;color:var(--gold-d)}
.faq h3{font-family:var(--body);font-weight:700;font-size:1.07rem;margin:1.3em 0 .3em;color:var(--ink);letter-spacing:0}
.cols{columns:3 210px;column-gap:28px;padding:0;list-style:none}.cols li{break-inside:avoid;margin:.25em 0}
.cta{background:var(--ink);color:#E6E0D6;border-radius:var(--r);padding:26px 28px;margin:2em 0;border-left:6px solid var(--gold)}.cta p{margin:0 0 .7em}.cta a{color:#F2DDB0}.cta-row{display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center;margin:0}.cta .btn{color:var(--ink)}
.src{font-size:.9rem;color:var(--mute);border-top:1px solid var(--line);margin-top:2em;padding-top:1em}.src ul{padding-left:1.1em}.src h2{font-family:var(--body);font-size:1rem;font-weight:700;margin:0 0 .4em}.src h2:after{display:none}
.rel{background:var(--soft);border-radius:var(--r);padding:16px 22px;margin:2em 0}.rel h2{font-size:1.15rem;margin:0 0 .5em}.rel h2:after{display:none}.rel ul{margin:0}
/* lead form */
.fcard{background:#fff;color:var(--text);border-radius:var(--r);border-top:5px solid var(--gold);box-shadow:0 18px 50px rgba(0,0,0,.35);padding:22px 22px 18px}
.fcard a{color:var(--gold-d)}.fcard h2{font-size:1.32rem;margin:0 0 .25em}.fcard h2:after{display:none}.fcard .sub{font-size:.92rem;color:var(--mute);margin:0 0 .9em}
form.lead{display:grid;gap:11px;grid-template-columns:1fr 1fr;margin:0}
form.lead .full{grid-column:1/-1}label{display:block;font-weight:700;font-size:.82rem;color:var(--ink);margin-bottom:3px;letter-spacing:.01em}label i{color:#A33A1F;font-style:normal}
input,select,textarea{width:100%;font:inherit;font-size:1rem;padding:10px 12px;border:1.5px solid #9C968C;border-radius:var(--r);background:#fff;color:var(--ink);min-height:46px}textarea{min-height:84px;resize:vertical}
input:focus,select:focus,textarea:focus{border-color:var(--gold-d);outline:2px solid var(--gold-t)}
form.lead .btn{width:100%}.fine{font-size:.78rem;color:var(--mute);margin:2px 0 0;line-height:1.45}.hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}.ferr{color:#8A1F11;font-weight:600;margin:0}
.sect-form{background:var(--soft);padding:10px 0 34px;margin-top:2.4em}.sect-form .fcard{max-width:760px;box-shadow:0 8px 30px rgba(0,0,0,.08)}
/* photos */
figure.ph{margin:1.5em 0}figure.ph img{display:block;width:100%;height:auto;border-radius:var(--r);background:var(--soft)}figure.ph figcaption{font-size:.86rem;color:var(--mute);margin:.5em 0 0}
.split{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:center}
.stat{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:2px;background:var(--line);border-radius:var(--r);overflow:hidden;margin:1.4em 0}.stat div{background:#fff;padding:18px}.stat b{display:block;font:900 1.6rem var(--head);color:var(--ink)}.stat span{font-size:.9rem;color:var(--mute)}
.units{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:1.2em 0}.unit{background:var(--ink);color:#E6E0D6;border-radius:var(--r);padding:22px;position:relative;overflow:hidden}.unit h3{color:#fff;margin:0 0 .3em}.unit a{color:#F2DDB0}.unit .mk{position:absolute;right:-18px;bottom:-10px;width:130px;color:#2a2a2a}
footer.site{background:var(--ink);color:#CFC8BB;margin-top:0;padding:46px 0 26px;font-size:.93rem}footer.site a{color:#EDE8DF;text-decoration:none}footer.site a:hover{color:var(--gold-l)}
footer.site h2{font:800 .76rem var(--head);letter-spacing:.2em;text-transform:uppercase;color:var(--gold-l);margin:0 0 .8em}footer.site h2:after{display:none}
.fg{display:grid;gap:28px;grid-template-columns:1.3fr 1fr 1fr 1fr}footer.site ul{list-style:none;padding:0;margin:0}footer.site li{margin:.1em 0}footer.site li a{display:inline-block;padding:4px 0}
.flogo img{height:62px;width:auto;margin-bottom:12px}
.legal{border-top:1px solid #333;margin-top:30px;padding-top:16px;font-size:.84rem;color:#9D978C}
.mk{display:inline-block;width:38px;height:auto;vertical-align:middle;color:var(--ink)}
@media (max-width:1060px){#navb{display:block}nav.main{flex-basis:100%;display:none}nav.main.open{display:block}nav.main ul{flex-direction:column;align-items:stretch;padding-bottom:14px}nav.main a.btn{margin:8px 0 0;text-align:center}}
@media (max-width:900px){.hx{grid-template-columns:1fr;gap:26px;padding:28px 0 34px}.fg{grid-template-columns:1fr 1fr}.split,.units{grid-template-columns:1fr}.brand img{height:44px}header.site .wrap{min-height:64px}.top .wrap{justify-content:center}.top .ar{display:none}}
@media (max-width:560px){.rule{letter-spacing:.16em;font-size:.68rem}form.lead{grid-template-columns:1fr}.ticks{grid-template-columns:1fr}.fg{grid-template-columns:1fr}.fcard{padding:18px 16px 14px}h2{margin-top:1.5em}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{header.site,footer.site,.top,.cta,.fcard,.sect-form{display:none}.hero-x{background:none;color:#000}.hero-x h1{color:#000}}
"""
CSS = re.sub(r"\n+", "", CSS.strip())

NAV = [("/concrete/", "Concrete"), ("/pavers/", "Pavers"), ("/artificial-turf/", "Turf"), ("/cost/", "Cost"), ("/service-areas/", "Areas"),
       ("/faq/", "FAQ"), ("/blog/", "Blog"), ("/about/", "About")]
LOGO_H = '<img src="/static/img/logo-header-128.webp" width="374" height="128" alt="Opera Concrete &amp; Pavers — driveways, patios, lifestyles" fetchpriority="high">'
LOGO_F = '<img src="/static/img/logo-light-128.webp" width="374" height="128" alt="Opera Concrete &amp; Pavers" loading="lazy">'


def _date_h(iso):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%B %d, %Y").replace(" 0", " ")


def page_unit(p):
    if p.get("unit"):
        return p["unit"]
    if p.get("city"):
        return CITIES[p["city"]]["unit"]
    return None


# ---------------------------------------------------------------- photos
HERO_SIZES = "100vw"


def _page_photo(p):
    pid = p.get("image") or p.get("hero_photo")
    return pid if pid and _phas(pid) else None


def _og_abs(p):
    pid = _page_photo(p)
    return BASE_URL + (_purl(pid, kind="og") if pid else "/static/img/og.jpg")


def image_node(pid):
    d = _pinfo(pid)
    n = {"@type": "ImageObject", "@id": f"{BASE_URL}{_purl(pid)}#image", "contentUrl": BASE_URL + _purl(pid), "url": BASE_URL + _purl(pid),
         "name": d["name"], "description": d["alt"], "width": d["w"], "height": d["h"], "encodingFormat": "image/webp"}
    if not d.get("stock"):
        n.update({"creator": {"@id": BASE_URL + "/#business"}, "creditText": PUBLIC_NAME, "copyrightNotice": f"© {YEAR} {PUBLIC_NAME}"})
    return n


def _hero_bg(p):
    pid = _page_photo(p)
    if not pid:
        return ""
    d = _pinfo(pid)
    srcset = ", ".join(f"{_purl(pid, w)} {w}w" for w in d["widths"])
    return f'<img class="bg" src="{_purl(pid, d["widths"][min(1, len(d["widths"]) - 1)])}" srcset="{srcset}" sizes="100vw" width="{d["w"]}" height="{d["h"]}" alt="" fetchpriority="high" decoding="async">'


def _preload(p):
    pid = _page_photo(p)
    if not pid or p["kind"] not in ("home", "service", "city", "cityservice", "pillar", "unit"):
        return ""
    d = _pinfo(pid)
    srcset = ", ".join(f"{_purl(pid, w)} {w}w" for w in d["widths"])
    return f'\n<link rel="preload" as="image" imagesrcset="{srcset}" imagesizes="100vw" fetchpriority="high">'


# ---------------------------------------------------------------- schema
def _unit_dept(u):
    U = UNITS[u]
    tel, _ = unit_phone(u)
    n = {"@type": "HomeAndConstructionBusiness", "@id": f"{BASE_URL}{U['route']}#unit", "name": f"{PUBLIC_NAME} — {U['name']}", "url": BASE_URL + U["route"],
         "address": {"@type": "PostalAddress", "addressLocality": U["base_city"], "addressRegion": "FL", "addressCountry": "US"},
         "areaServed": [{"@type": "AdministrativeArea", "name": COUNTIES[c]["name"] + ", Florida"} for c in U["counties"]],
         "parentOrganization": {"@id": BASE_URL + "/#business"}}
    if tel:
        n["telephone"] = tel
    return n


def business_node(full=False):
    n = {"@type": "HomeAndConstructionBusiness", "@id": BASE_URL + "/#business", "name": PUBLIC_NAME, "url": BASE_URL + "/", "slogan": TAGLINE,
         "logo": BASE_URL + "/static/img/logo-512.png", "image": BASE_URL + "/static/img/og.jpg",
         "department": [{"@id": f"{BASE_URL}{UNITS[u]['route']}#unit"} for u in UNIT_ORDER]}
    if EMAIL:
        n["email"] = EMAIL
    if full:
        n["description"] = BUSINESS["blurb"]
        n["areaServed"] = [{"@type": "City", "name": CITIES[s]["name"] + ", Florida"} for s in CITY_ORDER if CITIES[s]["tier"] == 1] + \
                          [{"@type": "AdministrativeArea", "name": COUNTIES[c]["name"] + ", Florida"} for c in COUNTY_ORDER]
        n["knowsAbout"] = ["Concrete driveways", "Stamped concrete", "Concrete pool decks", "Paver driveways", "Paver patios", "Travertine pool decks",
                           "Paver sealing", "Segmental retaining walls", "Artificial turf installation", "Florida hot-weather concreting"]
        n["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": "Concrete, paver and turf services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": SERVICES[k]["name"], "url": BASE_URL + SERVICES[k]["route"]}} for k in SERVICE_ORDER]}
    return n


def jsonld(p):
    url = BASE_URL + p["route"]
    g = [business_node(full=(p["kind"] == "home"))]
    if p["kind"] in ("home", "unit", "about", "contact"):
        g += [_unit_dept(u) for u in UNIT_ORDER]
    if p["kind"] == "home":
        g.append({"@type": "WebSite", "@id": BASE_URL + "/#website", "url": BASE_URL + "/", "name": PUBLIC_NAME, "publisher": {"@id": BASE_URL + "/#business"}, "inLanguage": "en-US"})
    wp = {"@type": p.get("wp_type") or "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["meta"], "inLanguage": "en-US",
          "isPartOf": {"@id": BASE_URL + "/#website"}, "about": {"@id": BASE_URL + "/#business"}, "dateModified": p.get("_lastmod", REVIEWED),
          "datePublished": p.get("published", LAUNCH_DATE)}
    if p.get("speakable", p["kind"] in ("service", "cityservice", "city", "post", "price", "faq")):
        wp["speakable"] = {"@type": "SpeakableSpecification", "cssSelector": [".capsule", "h1"]}
    pid = _page_photo(p)
    if pid:
        wp["primaryImageOfPage"] = image_node(pid)
    g.append(wp)
    crumbs = [("Home", "/")] + list(p.get("crumbs") or [])
    if p["route"] != "/":
        crumbs.append((p.get("crumb") or p["h1"], p["route"]))
        g.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": re.sub("<[^>]+>", "", n), "item": BASE_URL + r} for i, (n, r) in enumerate(crumbs)]})
    if p["kind"] in ("service", "cityservice") and p.get("service"):
        s = SERVICES[p["service"]]
        unit = page_unit(p)
        node = {"@type": "Service", "@id": url + "#service", "name": re.sub("<[^>]+>", "", p["h1"]), "serviceType": s["name"], "url": url,
                "provider": {"@id": f"{BASE_URL}{UNITS[unit]['route']}#unit"} if unit else {"@id": BASE_URL + "/#business"}, "description": p["meta"]}
        if p.get("city"):
            c = CITIES[p["city"]]
            node["areaServed"] = {"@type": "City" if c["kind"] in ("city", "town") else "Place", "name": f"{c['name']}, Florida",
                                  "containedInPlace": {"@type": "AdministrativeArea", "name": c["county_name"] + ", Florida"}}
        else:
            node["areaServed"] = [{"@type": "AdministrativeArea", "name": COUNTIES[c]["name"] + ", Florida"} for c in COUNTY_ORDER]
        if p.get("offer"):
            lo, hi, unit_lbl = p["offer"]
            node["offers"] = {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": lo, "highPrice": hi,
                              "description": f"Florida market range per {unit_lbl}, {REVIEWED[:7]}; a written quote follows a site visit."}
        g.append(node)
    if p["kind"] == "post":
        g.append({"@type": "BlogPosting", "@id": url + "#article", "headline": re.sub("<[^>]+>", "", p["h1"]), "description": p["meta"], "url": url,
                  "mainEntityOfPage": {"@id": url + "#webpage"}, "datePublished": p.get("published", LAUNCH_DATE), "dateModified": p.get("_lastmod", REVIEWED),
                  "inLanguage": "en-US", "author": {"@id": BASE_URL + "/#business"}, "publisher": {"@id": BASE_URL + "/#business"}, "image": _og_abs(p)})
    if p.get("howto"):
        name, steps_ = p["howto"]
        g.append({"@type": "HowTo", "@id": url + "#howto", "name": name, "step": [{"@type": "HowToStep", "position": i + 1, "name": t, "text": re.sub("<[^>]+>", "", d)} for i, (t, d) in enumerate(steps_)]})
    if p.get("faqs") and not p.get("faq_schema_off"):
        g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\s+", " ", re.sub("<[^>]+>", "", ans)).strip()}} for q, ans in p["faqs"]]})
    for extra in p.get("schema") or []:
        g.append(extra)
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":"))


# ---------------------------------------------------------------- lead form (posts natively to the Opera portal, which 303s to /thank-you/)
def lead_form(p, fid="quote", title=None):
    unit = page_unit(p)
    svc_opts = "".join(f'<option{" selected" if p.get("service") == k else ""}>{esc(SERVICES[k]["name"])}</option>' for k in SERVICE_ORDER)
    if unit:
        where = f'<input type="hidden" name="brand" value="{UNITS[unit]["brand"]}">'
    else:
        opts = "".join(f'<option value="{UNITS[u]["brand"]}">{esc(UNITS[u]["name"])}</option>' for u in UNIT_ORDER)
        where = f'<div class="full"><label for="{fid}-unit">Project location <i>*</i></label><select id="{fid}-unit" name="brand" required><option value="">Choose your area…</option>{opts}</select></div>'
    city_val = esc(CITIES[p["city"]]["name"] + ", FL") if p.get("city") else ""
    tel, disp = unit_phone(unit) if unit else ("", "")
    alt = f' Prefer to talk? Call <a href="tel:{tel}">{disp}</a>.' if tel else ""
    h = esc(title or p.get("form_title") or "Get a free estimate")
    return f"""<div class="fcard" id="{fid}"><h2>{h}</h2><p class="sub">Tell us about the project and we'll call to set up a free site visit.{alt}</p>
<form class="lead" method="post" action="{OPERA_ENDPOINT}">
<input type="hidden" name="redirect" value="{BASE_URL}/thank-you/"><input type="hidden" name="page" value="{BASE_URL}{p['route']}"><input type="hidden" name="channel" value="form">
<input type="hidden" name="utm_source" value=""><input type="hidden" name="utm_medium" value=""><input type="hidden" name="utm_campaign" value=""><input type="hidden" name="utm_term" value=""><input type="hidden" name="utm_content" value=""><input type="hidden" name="gclid" value=""><input type="hidden" name="fbclid" value="">
{where}
<div><label for="{fid}-name">Full name <i>*</i></label><input id="{fid}-name" name="name" autocomplete="name" required maxlength="120"></div>
<div><label for="{fid}-phone">Phone <i>*</i></label><input id="{fid}-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required maxlength="40"></div>
<div><label for="{fid}-email">Email</label><input id="{fid}-email" name="email" type="email" autocomplete="email" maxlength="160"></div>
<div><label for="{fid}-addr">City or ZIP <i>*</i></label><input id="{fid}-addr" name="address" autocomplete="postal-code" required maxlength="120" value="{city_val}"></div>
<div class="full"><label for="{fid}-svc">Service needed <i>*</i></label><select id="{fid}-svc" name="job_type" required><option value="">Choose a service…</option>{svc_opts}<option>Something else</option></select></div>
<div class="full"><label for="{fid}-msg">Project details</label><textarea id="{fid}-msg" name="message" maxlength="3000" placeholder="Size, current surface, HOA approval, timing…"></textarea></div>
<div class="hp" aria-hidden="true"><label for="{fid}-hp">Leave empty</label><input id="{fid}-hp" name="company_website" tabindex="-1" autocomplete="off"></div>
<div class="full"><button class="btn" type="submit">Request my free estimate</button><p class="fine">By sending this form you agree that {esc(PUBLIC_NAME)} may contact you by phone, text or email about your project. Message and data rates may apply. See our <a href="/privacy/">privacy policy</a>.</p></div>
</form></div>"""


# ---------------------------------------------------------------- shell
def _topbar():
    phones = " · ".join(f'{UNITS[u]["short"]} <a href="tel:{UNITS[u]["phone_e164"]}">{UNITS[u]["phone_display"]}</a>' for u in UNIT_ORDER if UNITS[u]["phone_e164"])
    right = phones or '<a href="/contact/">Free on-site estimates · <b>Orlando &amp; Sarasota crews</b></a>'
    return f'<div class="top"><div class="wrap"><span class="ar">Orlando · Kissimmee · Clermont · Oviedo &nbsp;<b>|</b>&nbsp; Sarasota · Lakewood Ranch · Bradenton</span><span>{right}</span></div></div>'


def _header(p):
    nav = "".join(f'<li><a href="{r}"{" aria-current=\"page\"" if p["route"] == r else ""}>{t}</a></li>' for r, t in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
{_topbar()}
<header class="site"><div class="wrap"><a class="brand" href="/" aria-label="{esc(PUBLIC_NAME)} home">{LOGO_H}</a>
<button id="navb" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="main" id="nav" aria-label="Main"><ul>{nav}<li><a class="btn" href="/contact/">Free estimate</a></li></ul></nav></div></header>"""


def _footer():
    con = "".join(f'<li><a href="{SERVICES[k]["route"]}">{esc(SERVICES[k]["name"])}</a></li>' for k in SERVICE_ORDER if SERVICES[k]["pillar"] == "concrete")
    pav = "".join(f'<li><a href="{SERVICES[k]["route"]}">{esc(SERVICES[k]["name"])}</a></li>' for k in SERVICE_ORDER if SERVICES[k]["pillar"] != "concrete")
    units = ""
    for u in UNIT_ORDER:
        U = UNITS[u]
        t = f'<br><a href="tel:{U["phone_e164"]}">{U["phone_display"]}</a>' if U["phone_e164"] else ""
        units += f'<p><a href="{U["route"]}"><strong>{esc(U["name"])}</strong></a>{t}</p>'
    mail = f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>' if EMAIL else ""
    t1 = "".join(f'<li><a href="{CITIES[s]["route"]}">{esc(CITIES[s]["name"])}</a></li>' for s in CITY_ORDER if CITIES[s]["tier"] == 1)
    return f"""<footer class="site"><div class="wrap"><div class="fg">
<div><a class="flogo" href="/">{LOGO_F}</a><p>Concrete, pavers and artificial turf for Florida homes. Two crews: one for Greater Orlando, one for Sarasota and Manatee counties.</p>{units}{mail}</div>
<div><h2>Concrete</h2><ul>{con}</ul></div>
<div><h2>Pavers &amp; turf</h2><ul>{pav}</ul><h2 style="margin-top:1.4em">Resources</h2><ul><li><a href="/cost/">Cost guides</a></li><li><a href="/permits/">Permits &amp; HOA rules</a></li><li><a href="/compare/">Comparisons</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/blog/">Blog</a></li></ul></div>
<div><h2>Main areas</h2><ul>{t1}<li><a href="/service-areas/">All service areas</a></li></ul></div>
</div><p class="legal">© {YEAR} {esc(PUBLIC_NAME)} · <a href="/about/">About</a> · <a href="/contact/">Contact</a> · <a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/accessibility/">Accessibility</a> · <a href="/sitemap.xml">Sitemap</a></p></div></footer>"""


FORM_KINDS = ("home", "service", "city", "cityservice", "pillar", "unit", "price")


def render_page(p):
    url = BASE_URL + p["route"]
    robots = "noindex,follow" if p.get("noindex") else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    items = [("Home", "/")] + list(p.get("crumbs") or [])
    crumbs_html = ""
    if p["route"] != "/" and p["kind"] != "plain":
        lis = "".join(f'<li><a href="{r}">{n}</a></li>' for n, r in items) + f'<li aria-current="page">{p.get("crumb") or p["h1"]}</li>'
        crumbs_html = f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'
    faq_html = ""
    if p.get("faqs"):
        faq_html = '<section class="faq" id="faq"><h2>' + esc(p.get("faq_title") or "Frequently asked questions") + "</h2>" + "".join(
            f"<h3>{esc(q)}</h3><p>{ans}</p>" if not ans.lstrip().startswith("<p") else f"<h3>{esc(q)}</h3>{ans}" for q, ans in p["faqs"]) + "</section>"
    rel_html = ""
    if p.get("related"):
        rel_html = '<aside class="rel"><h2>' + esc(p.get("related_title") or "Related pages") + "</h2><ul>" + "".join(f'<li><a href="{r}">{t}</a></li>' for r, t in p["related"]) + "</ul></aside>"
    src_html = ""
    if p.get("sources"):
        lis = []
        for s in p["sources"]:
            if isinstance(s, str):
                if s not in SOURCES:
                    continue
                lab, u = SOURCES[s]
            else:
                lab, u = s
            lis.append(f'<li><a href="{esc(u)}" rel="noopener">{esc(lab)}</a></li>')
        src_html = '<div class="src"><h2>Sources</h2><ul>' + "".join(dict.fromkeys(lis)) + "</ul></div>"
    by = ""
    if p["kind"] not in ("home", "plain", "page", "index", "unit", "pillar"):
        by = f'<p class="by">By the {esc(PUBLIC_NAME)} estimating team · Updated {_date_h(p.get("_lastmod", REVIEWED))}</p>'
    show_form = p.get("form", p["kind"] in FORM_KINDS)
    eb = f'<p class="eyebrow">{esc(p["eyebrow"])}</p>' if p.get("eyebrow") else ""
    if show_form:
        if p["kind"] == "home":
            left = f'<p class="rule">{esc(TAGLINE)}</p><h1>{p["h1"]}</h1>{p["lede"]}{p.get("hero_extra", "")}'
        else:
            left = f'{eb}<h1>{p["h1"]}</h1>{p["lede"]}{by}{p.get("hero_extra", "")}'
        hero = f'<div class="hero-x">{_hero_bg(p)}<div class="wrap">{crumbs_html}<div class="hx"><div>{left}</div>{lead_form(p)}</div></div></div>'
        tail_form = f'<div class="sect-form"><div class="wrap"><h2 class="ctr">{esc(p.get("form2_title") or "Ready for a price on your project?")}</h2>{lead_form(p, fid="quote2", title="Request a free estimate")}</div></div>' if p.get("form2", True) else ""
    else:
        hero = f'<div class="hero-l"><div class="wrap narrow">{crumbs_html}<div class="in">{eb}<h1>{p["h1"]}</h1>{p["lede"]}{by}</div></div></div>'
        tail_form = ""
    wide = "" if p.get("wide") else " narrow"
    main = f'<main id="main">{hero}<div class="wrap{wide}">{p["body"]}{faq_html}{rel_html}{src_html}</div>{tail_form}</main>'
    og_type = "article" if p["kind"] == "post" else "website"
    return f"""<!doctype html>
<html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(p["title"])}</title><meta name="description" content="{esc(p["meta"])}"><meta name="robots" content="{robots}"><link rel="canonical" href="{url}">
<link rel="preload" href="/static/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>{_preload(p)}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{esc(PUBLIC_NAME)}"><meta property="og:title" content="{esc(p["title"])}"><meta property="og:description" content="{esc(p["meta"])}"><meta property="og:url" content="{url}"><meta property="og:image" content="{_og_abs(p)}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_US"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="icon" href="/static/img/icon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/static/img/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#111111">
<link rel="alternate" type="application/rss+xml" title="{esc(PUBLIC_NAME)} blog" href="/feed.xml">
<style>{CSS}</style><noscript><style>nav.main{{display:block}}#navb{{display:none}}</style></noscript>
<script type="application/ld+json">{jsonld(p)}</script>
<script src="{SITE_JS}" defer></script>
</head><body>
{_header(p)}
{main}
{_footer()}
</body></html>"""
