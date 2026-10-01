# -*- coding: utf-8 -*-
"""City x service page assembler.

A city module (content/c_city_<slug>.py) supplies hand-written local material per service; the bank
(bank/b_<service_with_underscores>.py) supplies technical blocks in several variants. Variants are assigned with a
linear code so two cities rarely share a block on the same service: 8 variants -> GF(8), any two cities share at most
ONE of the five blocks; 5 variants -> degree-2 polynomial over GF(5), at most TWO."""
import importlib
import pathlib
import sys

from _data import CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER, TIER_SERVICES, city_service_route, nearest
from _helpers import page, sec, offer
from _photos import for_service
from _posts import posts_for

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT / "bank"))
BLOCKS = ["base", "build", "process", "risks", "care"]
SKELETONS = [
    ["L0", "base", "L1", "build", "SC", "process", "risks", "care"],
    ["SC", "L0", "build", "L1", "base", "risks", "process", "care"],
    ["L0", "L1", "base", "process", "SC", "build", "risks", "care"],
    ["L0", "build", "SC", "L1", "risks", "base", "process", "care"],
]
_T1 = [s for s in CITY_ORDER if CITIES[s]["tier"] == 1]
_REST = [s for s in CITY_ORDER if CITIES[s]["tier"] > 1]


def has_module(slug):
    return (ROOT / "content" / f"c_city_{slug.replace('-', '_')}.py").exists()


def exists(city_slug, service):
    return has_module(city_slug) and service in TIER_SERVICES[CITIES[city_slug]["tier"]]


def _gf8_mul(x, y):
    r = 0
    for _ in range(3):
        if y & 1:
            r ^= x
        y >>= 1
        x <<= 1
        if x & 8:
            x ^= 0b1011
    return r & 7


def _variant(city_slug, j, n):
    order = _T1 + _REST
    i = order.index(city_slug)
    if n == 8:
        a, b = divmod(i % 64, 8)
        return a ^ _gf8_mul(b, j)
    if n == 5:
        a, b, c = i % 5, (i // 5) % 5, (i // 25) % 5
        return (a + b * j + c * j * j) % 5
    return (i * (j + 2) + j) % n


def _bank(service):
    try:
        return importlib.import_module("b_" + service.replace("-", "_")).BLOCKS
    except ModuleNotFoundError:
        return {}


def cityservice_pages(city_slug, local):
    """local: {service: {"title","meta","h1","lede","sections":[(h2,html),(h2,html)],"scenario":(h2,html),"faqs":[...],"sources":[...]}}"""
    c = CITIES[city_slug]
    out = []
    for service in TIER_SERVICES[c["tier"]]:
        if service not in local:
            continue
        L = local[service]
        bank = _bank(service)
        sk = SKELETONS[((_T1 + _REST).index(city_slug) + SERVICE_ORDER.index(service)) % 4]
        parts = []
        for token in sk:
            if token.startswith("L"):
                k = int(token[1])
                if k < len(L["sections"]):
                    parts.append(sec(*L["sections"][k]))
            elif token == "SC":
                if L.get("scenario"):
                    parts.append(sec(*L["scenario"]))
            elif token in bank and bank[token]:
                vs = bank[token]
                h2, html = vs[_variant(city_slug, BLOCKS.index(token), len(vs))]
                poss = c["name"] + ("'" if c["name"].endswith("s") else "'s")
                rep = lambda t: t.replace("{city}'s", poss).replace("{city}", c["name"]).replace("{county}", c["county_name"])  # noqa: E731
                parts.append('<section class="bank"><h2>' + rep(h2) + "</h2>\n" + rep(html) + "\n</section>")
        near = [n for n in nearest(city_slug, 8) if exists(n, service)][:3]
        other = [s for s in TIER_SERVICES[c["tier"]] if s != service and s in local]
        idx = SERVICE_ORDER.index(service)
        other = other[idx % len(other):] + other[:idx % len(other)] if other else []
        S = SERVICES[service]
        related = [(S["route"], f"{S['name']}: how we build them"), (c["route"], f"Concrete, pavers and turf in {c['name']}")]
        related += [(city_service_route(n, service), f"{S['name']} in {CITIES[n]['name']}") for n in near]
        related += [(city_service_route(city_slug, o), f"{SERVICES[o]['name']} in {c['name']}") for o in other[:3]]
        related += posts_for(service, 2)
        pids = for_service(service, 3)
        hero = pids[(_T1 + _REST).index(city_slug) % len(pids)] if pids else None
        out.append(page(city_service_route(city_slug, service), "cityservice", L["title"], L["meta"], L["h1"], L["lede"], "\n".join(parts),
                        faqs=L.get("faqs"), sources=L.get("sources"), related=related, related_title=f"More for {c['name']} homeowners",
                        crumbs=[(c["name"], c["route"])], crumb=S["name"], service=service, city=city_slug, hero_photo=hero,
                        offer=offer(S["price"]) if S["price"] in __import__("_data").PRICES else None,
                        eyebrow=f"{S['name']} · {c['name']}, FL"))
    return out
