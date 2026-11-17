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
@font-face{font-family:"Playfair Display";src:url(/static/fonts/playfair-latin.woff2) format("woff2");font-weight:500 800;font-style:normal;font-display:swap}
@font-face{font-family:"Playfair Display";src:url(/static/fonts/playfair-italic-latin.woff2) format("woff2");font-weight:500 700;font-style:italic;font-display:swap}
:root{--ink:#0B0B0B;--ink2:#161513;--ink3:#24211C;--text:#26241F;--mute:#5E5950;--line:#E7E0D2;--bg:#FFFFFF;--soft:#F8F5EF;--gold:#C29B4E;--gold-l:#E2C27F;--gold-d:#8A6420;--gold-t:#EFE0BD;--r:4px;--w:1200px;
--gold-g:linear-gradient(135deg,#F3DD9F 0%,#D9B567 34%,#BE8F3F 68%,#9E742B 100%);--gold-h:linear-gradient(90deg,rgba(194,155,78,0),#C29B4E 18%,#F0D898 50%,#C29B4E 82%,rgba(194,155,78,0));
--serif:"Playfair Display",Georgia,"Times New Roman",serif;--head:Montserrat,"Arial Black",Arial,sans-serif;--body:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--body);font-size:1.0625rem;line-height:1.7}
img,svg{max-width:100%;height:auto}a{color:var(--gold-d);text-underline-offset:3px;text-decoration-thickness:1px}a:hover{color:var(--ink)}
::selection{background:#E9D6A6;color:#0B0B0B}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px;border-radius:3px}
h1,h2,h3{font-family:var(--serif);color:var(--ink);line-height:1.14;margin:0 0 .5em;letter-spacing:-.005em}
h1{font-weight:700;font-size:clamp(2.1rem,4.7vw,3.45rem)}h1 em,h2 em{font-style:italic;color:var(--gold-d)}
h2{font-weight:700;font-size:clamp(1.5rem,3vw,2.15rem);margin-top:1.8em}
h2:after{content:"";display:block;width:64px;height:2px;background:var(--gold-g);margin-top:.5em}
.ctr h2:after,.band h2:after{margin-left:auto;margin-right:auto}
h3{font-family:var(--head);font-weight:700;font-size:1.14rem;margin-top:1.4em;letter-spacing:0}
p{margin:0 0 1.05em}ul,ol{margin:0 0 1.1em;padding-left:1.3em}li{margin:.3em 0}
.wrap{max-width:var(--w);margin:0 auto;padding:0 20px}.narrow{max-width:820px}
.skip{position:absolute;left:-999px;top:0;background:var(--ink);color:#fff;padding:10px 14px;z-index:9}.skip:focus{left:8px;top:8px}
.top{background:#000;color:#BDB5A6;font-size:.84rem;letter-spacing:.05em;border-bottom:1px solid #1d1b18}.top .wrap{display:flex;justify-content:space-between;gap:8px 18px;flex-wrap:wrap;padding-top:8px;padding-bottom:8px}.top a{color:var(--gold-l);font-weight:600;text-decoration:none;white-space:nowrap}.top a:hover{color:#fff}.top b{color:var(--gold);font-weight:600}.top .ph{color:#E9E2D4}.top .sep{font-style:normal;color:#5d574d;margin:0 10px}
header.site{background:#0B0B0B;position:sticky;top:0;z-index:5;box-shadow:0 1px 0 rgba(194,155,78,.5),0 10px 30px rgba(0,0,0,.18)}header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:14px;min-height:80px;flex-wrap:wrap}
.brand{display:block;line-height:0}.brand img{height:58px;width:auto}
#navb{display:none;background:none;border:1px solid var(--gold);border-radius:var(--r);padding:9px 14px;min-height:44px;font:700 .82rem var(--head);color:#F3EBDD;cursor:pointer;letter-spacing:.14em;text-transform:uppercase}
nav.main ul{list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:0;margin:0;padding:0}nav.main a{display:block;padding:12px 10px;text-decoration:none;color:#EDE6D8;font:600 .76rem var(--head);letter-spacing:.14em;text-transform:uppercase;border-bottom:1px solid transparent}nav.main a:hover,nav.main a[aria-current]{border-bottom-color:var(--gold);color:var(--gold-l)}
nav.main a.btn{margin-left:10px;border:0;padding:12px 20px;color:#0B0B0B}nav.main a.btn:hover{color:#0B0B0B}
.btn{display:inline-block;background:var(--gold-g);color:#0B0B0B;text-decoration:none;font:800 .84rem var(--head);letter-spacing:.14em;text-transform:uppercase;padding:15px 26px;border-radius:var(--r);border:0;min-height:48px;line-height:1.3;cursor:pointer;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),0 8px 22px rgba(158,116,43,.28);transition:filter .15s,box-shadow .15s}.btn:hover{filter:brightness(1.07) saturate(1.05);color:#0B0B0B;box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 10px 26px rgba(158,116,43,.38)}
.btn.dark{background:#0B0B0B;color:var(--gold-l);box-shadow:inset 0 0 0 1px var(--gold)}.btn.dark:hover{background:#1a1916;color:#F3DD9F}
.btn.ghost{background:transparent;color:var(--gold-l);box-shadow:inset 0 0 0 1px var(--gold)}.btn.ghost:hover{background:rgba(194,155,78,.12);color:#F3DD9F}
.crumbs{font-size:.84rem;padding:14px 0 0}.crumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:4px 8px;margin:0;padding:0}.crumbs li+li:before{content:"/";margin-right:8px;opacity:.5}.crumbs a{color:inherit}
.eyebrow{font:700 .74rem var(--head);letter-spacing:.26em;text-transform:uppercase;color:var(--gold-d);margin:0 0 1em}
.capsule{font-size:1.13rem;line-height:1.66;color:var(--ink);border-left:2px solid var(--gold);padding:2px 0 2px 18px;margin:0 0 1.1em}
.by{font-size:.86rem;color:var(--mute);margin:.4em 0 0;letter-spacing:.01em}
/* dark hero with the form on the right (home, services, cities, city x service) */
.hero-x{position:relative;background:#0B0B0B;color:#EDE8DF;overflow:hidden}
.hero-x .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.42;filter:saturate(.85)}
.hero-x:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,8,8,.95) 0,rgba(8,8,8,.82) 50%,rgba(8,8,8,.55) 100%),radial-gradient(900px 420px at 0 100%,rgba(194,155,78,.16),transparent 70%)}
.hero-x:before{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--gold-h);z-index:2}
.hero-x .wrap{position:relative;z-index:1}
.hero-x .crumbs{color:#C9C1B2}
.hx{display:grid;grid-template-columns:1.1fr .9fr;gap:44px;align-items:start;padding:44px 0 54px}
.hero-x h1{color:#fff}.hero-x h1 em{color:var(--gold-l)}.hero-x .eyebrow{color:var(--gold-l)}.hero-x .capsule{color:#F1ECE3;border-left-color:var(--gold)}.hero-x .capsule a,.hero-x a{color:#F0D898}
.hero-x .by{color:#BDB5A6}
.rule{display:flex;align-items:center;gap:14px;margin:0 0 1.1em;font:600 .72rem var(--head);letter-spacing:.34em;text-transform:uppercase;color:var(--gold-l)}.rule:before{content:"";flex:0 0 52px;height:1px;background:var(--gold-g)}
.ticks{list-style:none;padding:0;margin:1.3em 0 0;display:grid;grid-template-columns:1fr 1fr;gap:9px 18px;font-size:.97rem}.ticks li{margin:0;padding-left:26px;position:relative}.ticks li:before{content:"";position:absolute;left:2px;top:.5em;width:9px;height:9px;background:var(--gold-g);transform:rotate(45deg)}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:1.3em 0 .2em}
.hcall{display:flex;flex-wrap:wrap;gap:12px 28px;margin:1.4em 0 0;padding:14px 0 0;border-top:1px solid rgba(194,155,78,.28);font-size:.92rem;color:#CFC7B8}.hero-x .hcall a{color:#F3DD9F;font:700 1.06rem var(--head);letter-spacing:.04em;text-decoration:none;white-space:nowrap}.hcall span{display:block;font:600 .64rem var(--head);letter-spacing:.24em;text-transform:uppercase;color:#A39A8B}
/* light hero (posts, faq, pages) */
.hero-l{background:var(--soft);border-bottom:1px solid var(--line);padding:0 0 32px;position:relative}.hero-l:after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:var(--gold-h)}.hero-l .in{padding-top:28px}
main section{margin:0 0 .6em}
.band{background:var(--soft);padding:26px 0 36px;margin:2em 0}.band.dk{background:radial-gradient(1000px 380px at 88% 0,rgba(194,155,78,.14),transparent 62%),#0B0B0B;color:#E6E0D6}.band.dk h2,.band.dk h3{color:#fff}.band.dk a{color:#F0D898}
.ctr{text-align:center}
.grid{display:grid;gap:20px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));margin:1.2em 0;padding:0;list-style:none}
.card{background:linear-gradient(#fff,#fff) padding-box,var(--gold-g) border-box;border:1px solid var(--line);border-top:3px solid transparent;border-radius:var(--r);padding:20px 20px 14px;margin:0;transition:box-shadow .2s}.card:hover{box-shadow:0 14px 34px rgba(11,11,11,.09)}.card h3{margin:0 0 .4em;font-family:var(--serif);font-size:1.2rem}.card p{margin:0 0 .6em;font-size:.97rem}.card a{font-weight:700;color:var(--ink);text-decoration:none}.card a:hover{color:var(--gold-d)}
.card .ph{margin:-20px -20px 14px;line-height:0}.card .ph img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:2px 2px 0 0}
.tw{overflow-x:auto;margin:1.1em 0 .4em;border:1px solid var(--line);border-radius:var(--r);background:#fff}
table{border-collapse:collapse;width:100%;font-size:.96rem}caption{caption-side:top;text-align:left;font:700 .95rem var(--head);color:var(--ink);padding:12px 14px 8px}
th,td{padding:10px 14px;text-align:left;vertical-align:top;border-top:1px solid var(--line)}thead th{background:#0B0B0B;color:var(--gold-l);font:700 .76rem var(--head);letter-spacing:.1em;text-transform:uppercase;border-top:0}tbody th{font-weight:600;color:var(--ink)}tbody tr:nth-child(even){background:#FBF9F4}
.tnote,.note{font-size:.92rem;color:var(--mute)}.note{background:var(--soft);border-left:2px solid var(--gold);padding:12px 16px}
.steps{padding-left:1.4em}.steps li{margin:.65em 0}.steps li::marker{font-weight:800;color:var(--gold-d)}
.faq h3{font-family:var(--serif);font-weight:700;font-size:1.16rem;margin:1.4em 0 .35em;color:var(--ink);padding-left:14px;border-left:2px solid var(--gold)}
.cols{columns:3 210px;column-gap:28px;padding:0;list-style:none}.cols li{break-inside:avoid;margin:.25em 0}
.cta{background:radial-gradient(700px 260px at 100% 0,rgba(194,155,78,.18),transparent 65%),#0B0B0B;color:#E6E0D6;border-radius:var(--r);padding:28px 30px;margin:2em 0;border:1px solid #2a261f;border-left:3px solid var(--gold)}.cta p{margin:0 0 .7em}.cta a{color:#F0D898}.cta-row{display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center;margin:0}.cta .btn{color:#0B0B0B}
.src{font-size:.9rem;color:var(--mute);border-top:1px solid var(--line);margin-top:2em;padding-top:1em}.src ul{padding-left:1.1em}.src h2{font-family:var(--body);font-size:1rem;font-weight:700;margin:0 0 .4em}.src h2:after{display:none}
.rel{background:var(--soft);border-radius:var(--r);padding:16px 22px;margin:2em 0;border:1px solid var(--line)}.rel h2{font-size:1.2rem;margin:0 0 .5em}.rel h2:after{display:none}.rel ul{margin:0}
/* lead form */
.fcard{background:#fff;color:var(--text);border-radius:var(--r);box-shadow:0 26px 64px rgba(0,0,0,.5),0 0 0 1px rgba(194,155,78,.35);padding:26px 24px 18px;position:relative}.fcard:before{content:"";position:absolute;left:0;right:0;top:0;height:4px;background:var(--gold-g);border-radius:var(--r) var(--r) 0 0}
.fcard a{color:var(--gold-d)}.fcard h2{font-size:1.45rem;margin:0 0 .25em}.fcard h2:after{display:none}.fcard .sub{font-size:.92rem;color:var(--mute);margin:0 0 .9em}
form.lead{display:grid;gap:11px;grid-template-columns:1fr 1fr;margin:0}
form.lead .full{grid-column:1/-1}label{display:block;font-weight:700;font-size:.8rem;color:var(--ink);margin-bottom:3px;letter-spacing:.02em}label i{color:#A33A1F;font-style:normal}
input,select,textarea{width:100%;font:inherit;font-size:1rem;padding:10px 12px;border:1px solid #A7A094;border-radius:var(--r);background:#FDFCF9;color:var(--ink);min-height:46px}textarea{min-height:84px;resize:vertical}
input:focus,select:focus,textarea:focus{border-color:var(--gold-d);outline:2px solid var(--gold-t);background:#fff}
form.lead .btn{width:100%}.fine{font-size:.78rem;color:var(--mute);margin:2px 0 0;line-height:1.45}.hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}.ferr{color:#8A1F11;font-weight:600;margin:0}
.sect-form{background:radial-gradient(900px 340px at 50% 0,rgba(194,155,78,.16),transparent 65%),#0B0B0B;padding:16px 0 44px;margin-top:2.4em}.sect-form h2{color:#fff}.sect-form .fcard{max-width:760px;margin:0 auto}
/* photos */
figure.ph{margin:1.5em 0}figure.ph img{display:block;width:100%;height:auto;border-radius:var(--r);background:var(--soft)}figure.ph figcaption{font-size:.86rem;color:var(--mute);margin:.5em 0 0}
.split{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:center}
.stat{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:1px;background:var(--line);border-radius:var(--r);overflow:hidden;margin:1.4em 0;border:1px solid var(--line)}.stat div{background:#fff;padding:18px}.stat b{display:block;font:700 1.7rem var(--serif);color:var(--ink)}.stat span{font-size:.9rem;color:var(--mute)}
.units{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:1.2em 0}.unit{background:radial-gradient(500px 200px at 100% 0,rgba(194,155,78,.16),transparent 70%),#0B0B0B;color:#E6E0D6;border-radius:var(--r);padding:24px;position:relative;overflow:hidden;border:1px solid #2a261f;border-top:2px solid var(--gold)}.unit h3{color:#fff;margin:0 0 .3em;font-family:var(--serif);font-size:1.3rem}.unit a{color:#F0D898}.unit .mk{position:absolute;right:-18px;bottom:-10px;width:130px;color:#1d1b18}
.nap{list-style:none;padding:0;margin:1em 0;border:1px solid var(--line);border-radius:var(--r);background:#fff}.nap li{display:grid;grid-template-columns:150px 1fr;gap:12px;margin:0;padding:10px 16px;border-top:1px solid var(--line)}.nap li:first-child{border-top:0}.nap b{font:700 .74rem var(--head);letter-spacing:.14em;text-transform:uppercase;color:var(--gold-d);padding-top:.25em}
footer.site{background:#0B0B0B;color:#BDB5A6;margin-top:0;padding:48px 0 26px;font-size:.93rem;position:relative}footer.site:before{content:"";position:absolute;left:0;right:0;top:0;height:1px;background:var(--gold-h)}footer.site a{color:#EDE8DF;text-decoration:none}footer.site a:hover{color:var(--gold-l)}
footer.site h2{font:700 .72rem var(--head);letter-spacing:.24em;text-transform:uppercase;color:var(--gold-l);margin:0 0 .9em}footer.site h2:after{display:none}
.fg{display:grid;gap:28px;grid-template-columns:1.3fr 1fr 1fr 1fr}footer.site ul{list-style:none;padding:0;margin:0}footer.site li{margin:.1em 0}footer.site li a{display:inline-block;padding:4px 0}
.funit{margin:0 0 1em;padding:0 0 0 12px;border-left:1px solid var(--gold)}.funit small{display:block;color:#958D80;font-size:.82rem}footer.site .funit .tel{color:var(--gold-l);font-weight:700;letter-spacing:.03em}
.flogo img{height:62px;width:auto;margin-bottom:12px}
.legal{border-top:1px solid #26231e;margin-top:30px;padding-top:16px;font-size:.84rem;color:#8F887C}
.mk{display:inline-block;width:38px;height:auto;vertical-align:middle;color:var(--ink)}
@media (max-width:1060px){#navb{display:block}nav.main{flex-basis:100%;display:none}nav.main.open{display:block}nav.main ul{flex-direction:column;align-items:stretch;padding-bottom:14px}nav.main a{border-bottom:1px solid #1e1c18}nav.main a.btn{margin:10px 0 0;text-align:center}}
@media (max-width:900px){.hx{grid-template-columns:1fr;gap:26px;padding:30px 0 36px}.fg{grid-template-columns:1fr 1fr}.split,.units{grid-template-columns:1fr}.brand img{height:44px}header.site .wrap{min-height:64px}.top .wrap{justify-content:center}.top .ar{display:none}.nap li{grid-template-columns:1fr;gap:2px}}
@media (max-width:560px){.top .wrap>span:last-child{display:flex;flex-direction:column;align-items:center;gap:1px}.top .sep{display:none}.rule{letter-spacing:.2em;font-size:.66rem}form.lead{grid-template-columns:1fr}.ticks{grid-template-columns:1fr}.fg{grid-template-columns:1fr}.fcard{padding:22px 16px 14px}h2{margin-top:1.5em}.top{font-size:.8rem}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn,.card{transition:none}}
@media print{header.site,footer.site,.top,.cta,.fcard,.sect-form{display:none}.hero-x{background:none;color:#000}.hero-x h1{color:#000}}
"""
CSS = re.sub(r"\n+", "", CSS.strip())

NAV = [("/concrete/", "Concrete"), ("/pavers/", "Pavers"), ("/artificial-turf/", "Turf"), ("/cost/", "Cost"), ("/service-areas/", "Areas"),
       ("/faq/", "FAQ"), ("/blog/", "Blog"), ("/about/", "About")]
LOGO_H = '<img src="/static/img/logo-light-128.webp" width="374" height="128" alt="Opera Concrete &amp; Pavers — driveways, patios, lifestyles" fetchpriority="high">'
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
    towns = [s for s in CITY_ORDER if CITIES[s]["unit"] == u and CITIES[s]["tier"] <= 2]
    n = {"@type": "HomeAndConstructionBusiness", "@id": f"{BASE_URL}{U['route']}#unit", "name": f"{PUBLIC_NAME} – {U['base_city']}",
         "alternateName": f"{PUBLIC_NAME} — {U['name']}", "url": BASE_URL + U["route"], "logo": BASE_URL + "/static/img/logo-512.png",
         "image": BASE_URL + "/static/img/og.jpg",
         "description": f"{PUBLIC_NAME} crew based in {U['base_city']}, Florida: pavers, paver sealing and restoration, concrete and artificial turf for homes in {U['name']}.",
         "address": {"@type": "PostalAddress", "addressLocality": U["base_city"], "addressRegion": "FL", "addressCountry": "US"},
         "areaServed": [{"@type": "City", "name": CITIES[s]["name"] + ", Florida"} for s in towns] +
                       [{"@type": "AdministrativeArea", "name": COUNTIES[c]["name"] + ", Florida"} for c in U["counties"]],
         "knowsAbout": ["Paver installation", "Paver sealing", "Paver restoration", "Paver driveways", "Pool deck pavers", "Concrete driveways", "Stamped concrete", "Artificial turf"],
         "parentOrganization": {"@id": BASE_URL + "/#business"}}
    if tel:
        n["telephone"] = tel
        n["contactPoint"] = {"@type": "ContactPoint", "telephone": tel, "contactType": "sales", "areaServed": "US-FL"}
    if U.get("same_as"):
        n["sameAs"] = U["same_as"]
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
                           "Paver sealing", "Paver restoration", "Segmental retaining walls", "Artificial turf installation", "Florida hot-weather concreting"]
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
    phones = '<i class="sep">·</i>'.join(f'<span class="tp"><span class="ph">{esc(UNITS[u]["short"])}</span> <a href="tel:{UNITS[u]["phone_e164"]}">{UNITS[u]["phone_display"]}</a></span>' for u in UNIT_ORDER if UNITS[u]["phone_e164"])
    right = phones or '<a href="/contact/">Free on-site estimates · <b>Orlando &amp; Sarasota crews</b></a>'
    return f'<div class="top"><div class="wrap"><span class="ar">Kissimmee · Orlando · Clermont · Windermere &nbsp;<b>|</b>&nbsp; Sarasota · Lakewood Ranch · Bradenton</span><span>{right}</span></div></div>'


def _hcall(p):
    """Phone strip under the hero copy: the page's own crew, or both crews on pages that serve both areas."""
    unit = page_unit(p)
    us = [unit] if unit else UNIT_ORDER
    items = [f'<p style="margin:0"><span>{esc(UNITS[u]["name"])}</span><a href="tel:{UNITS[u]["phone_e164"]}">{UNITS[u]["phone_display"]}</a></p>' for u in us if UNITS[u]["phone_e164"]]
    return f'<div class="hcall">{"".join(items)}</div>' if items else ""


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
        t = f'<br><a class="tel" href="tel:{U["phone_e164"]}">{U["phone_display"]}</a>' if U["phone_e164"] else ""
        units += f'<p class="funit"><a href="{U["route"]}"><strong>{esc(U["name"])}</strong></a><small>Based in {esc(U["base_city"])}, FL · crews come to you</small>{t}</p>'
    mail = f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>' if EMAIL else ""
    t1 = "".join(f'<li><a href="{CITIES[s]["route"]}">{esc(CITIES[s]["name"])}</a></li>' for s in CITY_ORDER if CITIES[s]["tier"] == 1)
    return f"""<footer class="site"><div class="wrap"><div class="fg">
<div><a class="flogo" href="/">{LOGO_F}</a><p>Pavers, paver sealing and restoration, concrete and artificial turf for Florida homes. Two crews: one based in Kissimmee for Greater Orlando, one based in Sarasota for Sarasota and Manatee counties.</p>{units}{mail}</div>
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
            left = f'<p class="rule">{esc(TAGLINE)}</p><h1>{p["h1"]}</h1>{p["lede"]}{p.get("hero_extra", "")}{_hcall(p)}'
        else:
            left = f'{eb}<h1>{p["h1"]}</h1>{p["lede"]}{by}{p.get("hero_extra", "")}{_hcall(p)}'
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
<link rel="preload" href="/static/fonts/playfair-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/static/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>{_preload(p)}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{esc(PUBLIC_NAME)}"><meta property="og:title" content="{esc(p["title"])}"><meta property="og:description" content="{esc(p["meta"])}"><meta property="og:url" content="{url}"><meta property="og:image" content="{_og_abs(p)}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_US"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="icon" href="/static/img/icon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/static/img/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#0B0B0B">
<link rel="alternate" type="application/rss+xml" title="{esc(PUBLIC_NAME)} blog" href="/feed.xml">
<style>{CSS}</style><noscript><style>nav.main{{display:block}}#navb{{display:none}}</style></noscript>
<script type="application/ld+json">{jsonld(p)}</script>
<script src="{SITE_JS}" defer></script>
</head><body>
{_header(p)}
{main}
{_footer()}
</body></html>"""
