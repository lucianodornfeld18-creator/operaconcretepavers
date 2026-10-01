# -*- coding: utf-8 -*-
"""Single source of truth for operaconcretepavers.com. Nothing here is invented: facts carry a source id
(see SOURCES, merged from research/sources.json) and the date they were checked.
Phones and e-mail are intentionally blank until the owner supplies them; templates hide every element that needs them."""
import json
import math
import pathlib

DOMAIN = "operaconcretepavers.com"
BASE_URL = "https://" + DOMAIN
PUBLIC_NAME = "Opera Concrete & Pavers"
SHORT_NAME = "Opera"
TAGLINE = "Driveways | Patios | Lifestyles"
EMAIL = ""                       # owner to supply (docs/OWNER-INPUTS.md)
LAUNCH_DATE = "2026-10-01"
REVIEWED = "2026-10-01"          # date the facts on the site were last checked
REVIEWED_HUMAN = "October 2026"
OPERA_ENDPOINT = "https://opera-portal.lucianodornfeld18.workers.dev/api/lead"

# Two units. Phone fields stay empty until the owner sends the numbers; the site then shows them everywhere at once.
UNITS = {
    "orlando": {"name": "Orlando & Central Florida", "short": "Orlando", "route": "/central-florida/", "brand": "opera-orlando",
                "phone_e164": "", "phone_display": "", "base_city": "Orlando", "center": (28.5384, -81.3789),
                "counties": ["orange", "osceola", "seminole", "lake", "polk"]},
    "sarasota": {"name": "Sarasota, Lakewood Ranch & Bradenton", "short": "Sarasota", "route": "/sarasota-manatee/", "brand": "opera-sarasota",
                 "phone_e164": "", "phone_display": "", "base_city": "Sarasota", "center": (27.3364, -82.5307),
                 "counties": ["sarasota", "manatee"]},
}
UNIT_ORDER = ["orlando", "sarasota"]


def unit_phone(unit):
    u = UNITS.get(unit) or {}
    return u.get("phone_e164", ""), u.get("phone_display", "")


def any_phone():
    return any(UNITS[u]["phone_e164"] for u in UNIT_ORDER)


BUSINESS = {
    "blurb": "Opera Concrete & Pavers builds concrete driveways, patios and pool decks, stamped concrete, paver driveways and patios, retaining walls and artificial turf for homes in the Orlando area and in Sarasota, Lakewood Ranch and Bradenton.",
    "service_area_short": "Orlando, Kissimmee, Clermont, Oviedo, Winter Garden, Windermere and Central Florida; Sarasota, Lakewood Ranch, Bradenton, Venice and the Suncoast",
}

# ---------------------------------------------------------------- services
# key -> name, nav label, route, pillar, short description, primary keyword, price key, noun
SERVICES = {
    "concrete-driveways": {"name": "Concrete Driveways", "route": "/concrete-driveways/", "pillar": "concrete", "kw": "concrete driveway installation",
                           "short": "New, widened and replacement driveways, poured to a thickness and joint plan that fits Florida soil.", "price": "concrete-driveway", "noun": "a concrete driveway"},
    "concrete-patios": {"name": "Concrete Patios", "route": "/concrete-patios/", "pillar": "concrete", "kw": "concrete patio contractor",
                        "short": "Back patios, lanai extensions and outdoor-kitchen pads, broom, stamped or decorative.", "price": "concrete-patio", "noun": "a concrete patio"},
    "concrete-pool-decks": {"name": "Concrete Pool Decks", "route": "/concrete-pool-decks/", "pillar": "concrete", "kw": "concrete pool deck",
                            "short": "Pool decks with cool-to-the-touch textures, proper slope to drains and expansion joints at the coping.", "price": "concrete-pool-deck", "noun": "a concrete pool deck"},
    "stamped-concrete": {"name": "Stamped Concrete", "route": "/stamped-concrete/", "pillar": "concrete", "kw": "stamped concrete",
                         "short": "Slate, ashlar, wood-plank and cobble patterns with integral color, release and sealer.", "price": "stamped-concrete", "noun": "stamped concrete"},
    "concrete-walkways": {"name": "Sidewalks & Walkways", "route": "/concrete-walkways/", "pillar": "concrete", "kw": "concrete walkway",
                          "short": "Front walks, side-yard paths and sidewalk repairs, including right-of-way sections.", "price": "concrete-walkway", "noun": "a concrete walkway"},
    "concrete-slabs": {"name": "Concrete Slabs", "route": "/concrete-slabs/", "pillar": "concrete", "kw": "concrete slab installation",
                       "short": "Pads for sheds, carports, AC units, RV and boat parking, and garage or addition slabs.", "price": "concrete-slab", "noun": "a concrete slab"},
    "concrete-repair": {"name": "Concrete Repair & Resurfacing", "route": "/concrete-repair/", "pillar": "concrete", "kw": "concrete repair",
                        "short": "Crack repair, resurfacing overlays, slab leveling and tear-out-and-replace when repair won't hold.", "price": "concrete-repair", "noun": "concrete repair"},
    "paver-driveways": {"name": "Paver Driveways", "route": "/paver-driveways/", "pillar": "pavers", "kw": "paver driveway installation",
                        "short": "Driveways in vehicle-rated pavers over a compacted aggregate base, with edge restraint that holds.", "price": "paver-driveway", "noun": "a paver driveway"},
    "paver-patios": {"name": "Paver Patios & Walkways", "route": "/paver-patios/", "pillar": "pavers", "kw": "paver patio installation",
                     "short": "Patios, walkways, fire-pit areas and lanai extensions in concrete pavers or travertine.", "price": "paver-patio", "noun": "a paver patio"},
    "pool-deck-pavers": {"name": "Pool Deck Pavers", "route": "/pool-deck-pavers/", "pillar": "pavers", "kw": "pool deck pavers",
                         "short": "Pool decks in travertine, shell stone and concrete pavers, including overlays on an old deck.", "price": "pool-deck-pavers", "noun": "a paver pool deck"},
    "paver-sealing": {"name": "Paver Sealing & Restoration", "route": "/paver-sealing/", "pillar": "pavers", "kw": "paver sealing",
                      "short": "Cleaning, re-sanding with polymeric sand, sealing and releveling sunken or shifted pavers.", "price": "paver-sealing", "noun": "paver sealing"},
    "retaining-walls": {"name": "Retaining Walls", "route": "/retaining-walls/", "pillar": "pavers", "kw": "retaining wall contractor",
                        "short": "Segmental block walls, raised planters and seat walls, with drainage behind the wall.", "price": "retaining-wall", "noun": "a retaining wall"},
    "artificial-turf": {"name": "Artificial Turf", "route": "/artificial-turf/", "pillar": "turf", "kw": "artificial turf installation",
                        "short": "Lawns, pet areas, putting greens and turf between pavers, built on a washed-rock base.", "price": "artificial-turf", "noun": "artificial turf"},
}
SERVICE_ORDER = ["concrete-driveways", "paver-driveways", "concrete-patios", "paver-patios", "concrete-pool-decks", "pool-deck-pavers",
                 "stamped-concrete", "concrete-walkways", "concrete-slabs", "concrete-repair", "paver-sealing", "retaining-walls", "artificial-turf"]
PILLARS = {
    "concrete": {"name": "Concrete", "route": "/concrete/", "h": "Concrete services"},
    "pavers": {"name": "Pavers", "route": "/pavers/", "h": "Paver services"},
    "turf": {"name": "Artificial Turf", "route": "/artificial-turf/", "h": "Artificial turf"},
}
TIER_SERVICES = {
    1: SERVICE_ORDER,
    2: ["concrete-driveways", "paver-driveways", "concrete-patios", "paver-patios", "concrete-pool-decks", "pool-deck-pavers", "stamped-concrete", "artificial-turf"],
    3: ["concrete-driveways", "paver-patios", "artificial-turf"],
}

# ---------------------------------------------------------------- prices (market ranges, not quotes)
# key -> (low, high, typical_low, typical_high, unit, source ids). Filled from research/facts.md.
PRICES = {}
PRICE_DATE = "October 2026"
PRICE_LABEL = "Florida market range"
_pf = pathlib.Path(__file__).parent / "_prices.json"
if _pf.exists():
    PRICES = {k: tuple(v) for k, v in json.loads(_pf.read_text(encoding="utf-8")).items()}


def _fmt(x):
    return f"{x:,.0f}" if x >= 100 or float(x).is_integer() else f"{x:.2f}"


def price_range(key, typical=False):
    lo, hi, tlo, thi, unit, _ = PRICES[key]
    a, b = (tlo, thi) if typical else (lo, hi)
    return f"${_fmt(a)}–${_fmt(b)}"


def price_unit(key):
    return PRICES[key][4]


# ---------------------------------------------------------------- sources (ids -> (label, url)); research/sources.json is merged in
SOURCES = {
    "hb683": ("Florida Senate — CS/CS/CS/HB 683 (2025), Construction Regulations", "https://www.flsenate.gov/Session/Bill/2025/683"),
    "fs125572": ("Florida Statutes §125.572 — synthetic turf on single-family lots", "https://www.flsenate.gov/Laws/Statutes/2025/0125.572"),
    "dep-rule": ("Florida Administrative Code — Rule 62-308.100, Synthetic Turf (effective May 19, 2026)", "https://flrules.org/gateway/RuleNo.asp?id=62-308.100"),
    "fs7203045": ("Florida Statutes §720.3045 — items not visible from the frontage or an adjacent parcel", "https://www.flsenate.gov/Laws/Statutes/2025/720.3045"),
    "dbpr": ("Florida DBPR — verify a license", "https://www.myfloridalicense.com/wl11.asp"),
    "noaa-normals": ("NOAA NCEI — U.S. Climate Normals 1991–2020", "https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals"),
    "usda-wss": ("USDA NRCS — Web Soil Survey", "https://websoilsurvey.nrcs.usda.gov/app/"),
}
_sf = pathlib.Path(__file__).resolve().parent.parent / "research" / "sources.json"
if _sf.exists():
    for k, v in json.loads(_sf.read_text(encoding="utf-8")).items():
        SOURCES.setdefault(k, tuple(v))

# ---------------------------------------------------------------- counties and cities
COUNTIES = {
    "orange": {"name": "Orange County", "unit": "orlando"},
    "osceola": {"name": "Osceola County", "unit": "orlando"},
    "seminole": {"name": "Seminole County", "unit": "orlando"},
    "lake": {"name": "Lake County", "unit": "orlando"},
    "polk": {"name": "Polk County", "unit": "orlando"},
    "sarasota": {"name": "Sarasota County", "unit": "sarasota"},
    "manatee": {"name": "Manatee County", "unit": "sarasota"},
}
COUNTY_ORDER = ["orange", "osceola", "seminole", "lake", "polk", "sarasota", "manatee"]

# slug: (name, county, tier, lat, lon, kind)   kind: city | town | cdp | community | neighborhood | island
_C = {
    # Orlando unit
    "orlando": ("Orlando", "orange", 1, 28.5384, -81.3789, "city"),
    "kissimmee": ("Kissimmee", "osceola", 1, 28.2920, -81.4076, "city"),
    "clermont": ("Clermont", "lake", 1, 28.5494, -81.7729, "city"),
    "oviedo": ("Oviedo", "seminole", 1, 28.6700, -81.2081, "city"),
    "winter-garden": ("Winter Garden", "orange", 1, 28.5653, -81.5862, "city"),
    "windermere": ("Windermere", "orange", 1, 28.4956, -81.5348, "town"),
    "st-cloud": ("St. Cloud", "osceola", 2, 28.2489, -81.2812, "city"),
    "winter-park": ("Winter Park", "orange", 2, 28.6000, -81.3392, "city"),
    "lake-nona": ("Lake Nona", "orange", 2, 28.3772, -81.2473, "neighborhood"),
    "dr-phillips": ("Dr. Phillips", "orange", 2, 28.4494, -81.4923, "community"),
    "apopka": ("Apopka", "orange", 2, 28.6934, -81.5322, "city"),
    "sanford": ("Sanford", "seminole", 2, 28.8029, -81.2695, "city"),
    "lake-mary": ("Lake Mary", "seminole", 2, 28.7589, -81.3178, "city"),
    "winter-springs": ("Winter Springs", "seminole", 2, 28.6989, -81.3081, "city"),
    "celebration": ("Celebration", "osceola", 2, 28.3253, -81.5331, "community"),
    "davenport": ("Davenport", "polk", 2, 28.1614, -81.6017, "city"),
    "minneola": ("Minneola", "lake", 2, 28.5744, -81.7462, "city"),
    "horizon-west": ("Horizon West", "orange", 2, 28.4336, -81.6226, "community"),
    "ocoee": ("Ocoee", "orange", 2, 28.5692, -81.5440, "city"),
    "altamonte-springs": ("Altamonte Springs", "seminole", 2, 28.6611, -81.3656, "city"),
    "longwood": ("Longwood", "seminole", 3, 28.7031, -81.3384, "city"),
    "casselberry": ("Casselberry", "seminole", 3, 28.6778, -81.3279, "city"),
    "maitland": ("Maitland", "orange", 3, 28.6278, -81.3631, "city"),
    "groveland": ("Groveland", "lake", 3, 28.5581, -81.8512, "city"),
    "hunters-creek": ("Hunters Creek", "orange", 3, 28.3606, -81.4223, "community"),
    "championsgate": ("ChampionsGate", "osceola", 3, 28.2611, -81.6201, "community"),
    "poinciana": ("Poinciana", "osceola", 3, 28.1403, -81.4584, "community"),
    "avalon-park": ("Avalon Park", "orange", 3, 28.5130, -81.1530, "community"),
    "montverde": ("Montverde", "lake", 3, 28.6003, -81.6740, "town"),
    "belle-isle": ("Belle Isle", "orange", 3, 28.4583, -81.3592, "city"),
    # Sarasota unit
    "sarasota": ("Sarasota", "sarasota", 1, 27.3364, -82.5307, "city"),
    "lakewood-ranch": ("Lakewood Ranch", "manatee", 1, 27.4200, -82.4065, "community"),
    "bradenton": ("Bradenton", "manatee", 1, 27.4989, -82.5748, "city"),
    "venice": ("Venice", "sarasota", 1, 27.0998, -82.4543, "city"),
    "palmetto": ("Palmetto", "manatee", 2, 27.5214, -82.5723, "city"),
    "parrish": ("Parrish", "manatee", 2, 27.5870, -82.4248, "community"),
    "north-port": ("North Port", "sarasota", 2, 27.0442, -82.2359, "city"),
    "nokomis": ("Nokomis", "sarasota", 2, 27.1192, -82.4443, "community"),
    "osprey": ("Osprey", "sarasota", 2, 27.1961, -82.4904, "community"),
    "ellenton": ("Ellenton", "manatee", 2, 27.5217, -82.5276, "community"),
    "longboat-key": ("Longboat Key", "sarasota", 2, 27.4125, -82.6590, "town"),
    "siesta-key": ("Siesta Key", "sarasota", 2, 27.2678, -82.5465, "island"),
    "myakka-city": ("Myakka City", "manatee", 3, 27.3473, -82.1612, "community"),
    "englewood": ("Englewood", "sarasota", 3, 26.9620, -82.3526, "community"),
    "anna-maria-island": ("Anna Maria Island", "manatee", 3, 27.5000, -82.7151, "island"),
    "south-venice": ("South Venice", "sarasota", 3, 27.0531, -82.4243, "community"),
}


def _miles(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 3958.8 * 2 * math.asin(math.sqrt(h))


CITIES = {}
for slug, (name, co, tier, lat, lon, kind) in _C.items():
    unit = COUNTIES[co]["unit"]
    CITIES[slug] = {"name": name, "county": co, "county_name": COUNTIES[co]["name"], "tier": tier, "lat": lat, "lon": lon, "kind": kind,
                    "unit": unit, "route": f"/{slug}-fl/", "miles": round(_miles(UNITS[unit]["center"], (lat, lon)))}
CITY_ORDER = list(_C)


def city_service_route(city_slug, service):
    return f"/{city_slug}-fl{SERVICES[service]['route']}"


def nearest(slug, n=6, same_unit=True):
    c = CITIES[slug]
    others = [s for s in CITY_ORDER if s != slug and (not same_unit or CITIES[s]["unit"] == c["unit"])]
    return sorted(others, key=lambda s: _miles((c["lat"], c["lon"]), (CITIES[s]["lat"], CITIES[s]["lon"])))[:n]
