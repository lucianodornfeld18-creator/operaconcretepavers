# -*- coding: utf-8 -*-
"""Business cards for the two Google Business Profiles (Kissimmee and Sarasota).

python -X utf8 brand/make_cards.py  ->  brand/business-cards/
  card-<unit>.pdf          print file, 2 pages (front, back), 3.75 x 2.25 in = 3.5 x 2 in trim + 0.125 in bleed each side
  card-<unit>-front.png    preview at 600 dpi-ish (2x), back likewise
Everything on the card comes from site/_data.py so the name, phone and website match the site and the GBP exactly."""
import base64
import pathlib
import sys

import segno
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))
from _data import UNITS, PUBLIC_NAME, BASE_URL, DOMAIN, COUNTIES  # noqa: E402

OUT = ROOT / "brand" / "business-cards"
OUT.mkdir(exist_ok=True)
FONTS = ROOT / "site" / "static" / "fonts"
LOGO = base64.b64encode((ROOT / "brand" / "opera-logo-light.png").read_bytes()).decode()

CARDS = {
    "kissimmee": {"unit": "orlando", "title": "Kissimmee &amp; Greater Orlando", "serving": "Kissimmee · Orlando · Clermont · Windermere · Winter Garden · Oviedo",
                  "campaign": "kissimmee"},
    "sarasota": {"unit": "sarasota", "title": "Sarasota, Lakewood Ranch &amp; Bradenton", "serving": "Sarasota · Lakewood Ranch · Bradenton · Venice · Siesta Key · Parrish",
                 "campaign": "sarasota"},
}

CSS = f"""
@font-face{{font-family:Montserrat;src:url({(FONTS / 'montserrat-latin.woff2').as_uri()}) format("woff2");font-weight:500 900}}
@font-face{{font-family:Playfair;src:url({(FONTS / 'playfair-latin.woff2').as_uri()}) format("woff2");font-weight:500 800}}
@font-face{{font-family:Playfair;src:url({(FONTS / 'playfair-italic-latin.woff2').as_uri()}) format("woff2");font-weight:500 700;font-style:italic}}
@page{{size:3.75in 2.25in;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:3.75in;height:2.25in;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.side{{width:3.75in;height:2.25in;position:relative;overflow:hidden;page-break-after:always}}
.safe{{position:absolute;inset:.25in}}
.front{{background:radial-gradient(2.6in 1.4in at 50% 115%,rgba(194,155,78,.22),transparent 70%),radial-gradient(2in 1in at 50% -20%,rgba(194,155,78,.10),transparent 70%),#0A0A0A}}
.front .safe{{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.front img{{width:2.45in;height:auto;display:block}}
.front .line{{width:1.1in;height:.6pt;margin:.13in 0 .08in;background:linear-gradient(90deg,transparent,#C29B4E 20%,#F0D898 50%,#C29B4E 80%,transparent)}}
.front .svc{{font:600 5.6pt Montserrat,sans-serif;letter-spacing:.24em;text-transform:uppercase;color:#D9BE83}}
.back{{background:#FBF8F2;color:#141210}}
.back:before{{content:"";position:absolute;left:0;right:0;top:0;height:.19in;background:#0A0A0A}}
.back:after{{content:"";position:absolute;left:0;right:0;top:.19in;height:1.3pt;background:linear-gradient(90deg,#9E742B,#F3DD9F 45%,#BE8F3F 75%,#9E742B)}}
.back .safe{{top:.33in;display:grid;grid-template-columns:1fr .78in;column-gap:.14in}}
.brand{{font:800 6pt Montserrat,sans-serif;letter-spacing:.22em;text-transform:uppercase;color:#8A6420}}
h1{{font:700 11.4pt/1.08 Playfair,Georgia,serif;margin:.03in 0 .05in;color:#0A0A0A}}
.what{{font:500 5.7pt/1.4 Montserrat,sans-serif;color:#3a352d;letter-spacing:.02em}}
.what b{{color:#0A0A0A;font-weight:700}}
.tel{{font:800 13.5pt Montserrat,sans-serif;letter-spacing:.01em;color:#0A0A0A;margin:.07in 0 .015in}}
.web{{font:600 6.6pt Montserrat,sans-serif;color:#8A6420;letter-spacing:.03em}}
.foot{{position:absolute;left:0;right:0;bottom:-.03in;font:500 4.9pt/1.35 Montserrat,sans-serif;color:#5E5950;letter-spacing:.02em}}
.foot b{{color:#0A0A0A;font-weight:700}}
.qr{{align-self:start;text-align:center}}
.qr svg{{width:.82in;height:.82in;display:block}}
.qr span{{display:block;font:600 4.3pt Montserrat,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8A6420;margin-top:.03in}}
"""


def qr_svg(url):
    q = segno.make(url, error="m")
    return q.svg_inline(border=2, dark="#0A0A0A", light="#FBF8F2", omitsize=True)


def html(key):
    c = CARDS[key]
    U = UNITS[c["unit"]]
    url = f"{BASE_URL}{U['route']}?utm_source=card&utm_campaign={c['campaign']}"
    names = [COUNTIES[x]["name"].replace(" County", "") for x in U["counties"]]
    counties = (" &amp; ".join(names) + " counties") if len(names) == 2 else " · ".join(names)
    front = f"""<div class="side front"><div class="safe"><img src="data:image/png;base64,{LOGO}" alt="">
<div class="line"></div><p class="svc">Pavers · Sealing · Restoration · Concrete</p></div></div>"""
    back = f"""<div class="side back"><div class="safe"><div>
<p class="brand">{PUBLIC_NAME.replace('&', '&amp;')}</p>
<h1>{c['title']}</h1>
<p class="what"><b>Pavers</b> · Paver Sealing &amp; Restoration<br>Concrete Driveways &amp; Pool Decks · Artificial Turf</p>
<p class="tel">{U['phone_display']}</p>
<p class="web">{DOMAIN}</p>
</div>
<div class="qr">{qr_svg(url)}<span>Free estimate</span></div>
<p class="foot"><b>Based in {U['base_city']}, FL</b> · we come to you · {counties}<br>{c['serving']}</p>
</div></div>"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{front}{back}</body></html>", url


def main():
    with sync_playwright() as p:
        b = p.chromium.launch()
        for key in CARDS:
            doc, url = html(key)
            src = OUT / f"card-{key}.html"
            src.write_text(doc, encoding="utf-8")
            pg = b.new_page()
            pg.goto(src.as_uri())
            pg.wait_for_timeout(300)
            pg.pdf(path=str(OUT / f"card-{key}.pdf"), width="3.75in", height="2.25in", print_background=True, prefer_css_page_size=True)
            pv = b.new_page(viewport={"width": 360, "height": 216}, device_scale_factor=5)
            pv.goto(src.as_uri())
            pv.wait_for_timeout(300)
            for i, side in enumerate(("front", "back")):
                pv.locator(".side").nth(i).screenshot(path=str(OUT / f"card-{key}-{side}.png"))
            print(key, "->", url)
        b.close()


if __name__ == "__main__":
    main()
