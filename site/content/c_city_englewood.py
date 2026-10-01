# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "englewood"

WIKI_ENGLEWOOD_URL = "https://en.wikipedia.org/wiki/Englewood,_Florida"
WIKI_SR776_URL = "https://en.wikipedia.org/wiki/Florida_State_Road_776"
WIKI_MANASOTA_URL = "https://en.wikipedia.org/wiki/Manasota_Key,_Florida"
CENSUS_ENGLEWOOD_URL = "https://censusreporter.org/profiles/16000US1220825-englewood-fl/"
SCGOV_CRA_URL = "https://www.scgov.net/government/planning-and-development-services/englewood-cra"
SARMAG_DEARBORN_URL = "https://www.sarasotamagazine.com/news-and-profiles/2015/06/a-look-back-at-englewoods-historic-dearborn-street"
YOURSUN_BLINDPASS_URL = "https://www.yoursun.com/englewood/news/blind-pass-beach-reopens/article_a1e30dbe-fabd-11ef-b312-c73ae603eb6e.html"

SRC = [
    "sarasota-county-row-permit", "sarasota-county-98-3-culvert-row-fees", "sarasota-county-124-255-culverts",
    "sarasota-county-124-76-rsf-standards", "sarasota-county-124-283-nonconforming-isr", "sarasota-county-54-723-gbsl",
    "sarasota-county-online-permitting", "sarasota-county-building-page", "fdep-cccl-program", "fdep-cccl-apply",
    "fema-coastal-firm", "swfwmd-restrictions", "nrcs-immokalee-osd", "nrcs-felda-osd", "dep-rule", "fs125572", "fs720-3045",
    ("Wikipedia, Englewood, Florida", WIKI_ENGLEWOOD_URL),
    ("Wikipedia, Florida State Road 776", WIKI_SR776_URL),
    ("Wikipedia, Manasota Key, Florida", WIKI_MANASOTA_URL),
    ("Census Reporter, Englewood CDP, FL (ACS 2020-2024 5-yr, B01003/B25035)", CENSUS_ENGLEWOOD_URL),
    ("Sarasota County, Englewood Community Redevelopment Area", SCGOV_CRA_URL),
    ("Sarasota Magazine, A Look Back at Englewood's Historic Dearborn Street", SARMAG_DEARBORN_URL),
    ("Your Sun, Blind Pass Beach reopens", YOURSUN_BLINDPASS_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Which county actually reviews a driveway or patio permit in Englewood?",
        "<p>Englewood isn't a city at all; it's one unincorporated community that happens to straddle a county line, and the line runs roughly south of Dearborn Street and north of McCall Road, "
        "zig-zagging rather than following a single straight road " + ext(WIKI_SR776_URL, "Wikipedia, Florida State Road 776") + ". A homeowner north of that line, including the Dearborn Street corridor, files a "
        "driveway or " + cs("englewood", "paver-patios", "patio") + " permit with Sarasota County's Building Division; a few blocks south, the same project goes to Charlotte County instead. We work the "
        "Sarasota County side, so the permit path below covers that half of town; confirming which county a specific parcel sits in, before assuming either office, is the first call worth making " +
        src("sarasota-county-building-page", "Sarasota County Building") + ".</p>"
    ),
    sec(
        "What does Sarasota County's culvert rule require on this side of Englewood?",
        "<p>Sarasota County folds culvert work into the same umbrella permit it requires for any job that touches its right-of-way " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") +
        ". A driveway crossing the roadside swale needs a culvert built between 20 and 24 feet long, from reinforced or asphalt-coated corrugated pipe, with County Engineer staff dictating the grade and size "
        "before anyone forms up the slab " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ". None of it happens over a counter; this side of Englewood files every application through the "
        "county's own online portal instead " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") + ".</p>"
    ),
    sec(
        "What's behind Dearborn Street, and why does it matter for a home built decades ago?",
        "<p>Dearborn Street was Englewood's original commercial spine, platted in 1896 by three brothers from Englewood, Chicago, who gave the new settlement their hometown's name " + ext(WIKI_ENGLEWOOD_URL, "Wikipedia, Englewood, Florida") +
        "; it went on to host the area's first newspaper, bank, drugstore and garage before anything else in town did " + ext(SARMAG_DEARBORN_URL, "Sarasota Magazine, Englewood's Historic Dearborn Street") + ". Sarasota County's own "
        "Englewood Community Redevelopment Area, which covers only the Sarasota County half of the community, now funds sidewalks and streetscape work around that corridor " + ext(SCGOV_CRA_URL, "Sarasota County, Englewood CRA") +
        ". The Census Bureau's current five-year estimate puts Englewood's median home at 1982, a build date old enough that a driveway " + svc("concrete-repair", "resurfacing") + " job is at least as common here as a "
        "first pour on raw ground " + ext(CENSUS_ENGLEWOOD_URL, "Census Reporter, Englewood CDP") + ".</p>"
    ),
    sec(
        "Does Englewood's stretch of Manasota Key change anything about a coastal project?",
        "<p>Manasota Key runs about 11 miles as a barrier island, and while most of it, Englewood Beach included, sits in Charlotte County, the key continues north into Sarasota County, with Blind Pass "
        "Beach marking the county's southernmost stretch of Gulf shoreline " + ext(WIKI_MANASOTA_URL, "Wikipedia, Manasota Key, Florida") + " " + ext(YOURSUN_BLINDPASS_URL, "Your Sun, Blind Pass Beach") + ". A pool deck or "
        "patio on that northern, Sarasota County sliver of the key falls under two coastal lines rather than one: the county's own Gulf Beach Setback Line, which allows no construction or excavation past it "
        "without a variance, and Florida DEP's Coastal Construction Control Line permit, a separate state-level review that applies on its own terms " + src("sarasota-county-54-723-gbsl", "Sarasota County Code §54-723") +
        " " + src("fdep-cccl-program", "FDEP's CCCL program") + ".</p>"
    ),
    sec(
        "How big is Englewood, and how far is the Sarasota County side from our base?",
        "<p>The Census Bureau's single Englewood CDP, which the figures treat as one place even though it crosses the county line, puts the area's population at roughly 20,091 as of the latest five-year "
        "estimate, up from 14,863 counted in 2010 " + ext(CENSUS_ENGLEWOOD_URL, "Census Reporter, Englewood CDP") + ". The Sarasota County side we work sits about 28 miles from the Sarasota unit's base, the longest "
        "drive of any town in this part of our service area, which is why we schedule an Englewood estimate alongside other South County stops rather than as a standalone trip.</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Is Englewood its own city with a building department?",
        "No. Englewood is unincorporated on both sides of the Sarasota-Charlotte county line, so there's no city hall. The Sarasota County side files permits with the county's Building Division; the Charlotte County side is outside the area we work."
    ),
    faq(
        "How do I know which county my Englewood address falls in?",
        "The line runs roughly south of Dearborn Street and north of McCall Road but zig-zags rather than following one straight road, so a parcel search or a call to the county building line is more reliable than guessing from the street name."
    ),
    faq(
        "Does a Sarasota County driveway in Englewood need a culvert permit?",
        "Usually, yes. Most lots on this side of town still drain to an open roadside ditch, so county staff review the pipe underneath on its own, apart from whatever surface sits above it, and dictate its material, length and grade."
    ),
    faq(
        "Is any part of Englewood subject to Florida's coastal construction line?",
        "Only the Sarasota County stretch of Manasota Key, north of Blind Pass. Most of the key, including Englewood Beach, sits in Charlotte County; the Sarasota County sliver still answers to the county's own Gulf Beach Setback Line on top of the state's CCCL permit."
    ),
    faq(
        "Does the current watering restriction change sod or turf plans in Englewood?",
        "Yes. SWFWMD's current shortage order holds the Sarasota County side to one irrigation day a week through the spring of 2027, a restriction a lawn stops needing entirely once it's replaced with turf instead of sod."
    ),
]

HUB = page(
    "/englewood-fl/", "city",
    "Concrete, Paver & Turf Contractor in Englewood, FL",
    "Concrete, pavers and turf for the Sarasota County side of Englewood, FL: the county-line permit split and Manasota Key's setback line, October 2026.",
    "Concrete, Pavers and Turf on Englewood's Sarasota County Side",
    capsule(
        "Englewood is an unincorporated community split by the Sarasota-Charlotte county line near historic Dearborn Street. As of October 2026, we work the Sarasota County side, where the county's "
        "Building Division reviews every driveway, patio and turf permit, a roadside culvert often needs its own sign-off, and the area's 1982 median home means resurfacing comes up as often as a first pour."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Englewood",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/sarasota-county-driveway-patio-permits/", "Driveway and patio permits in Sarasota, Venice and North Port"),
        ("/nokomis-fl/", "Concrete, pavers and turf in Nokomis"),
        ("/venice-fl/", "Concrete, pavers and turf in Venice"),
        ("/paver-patio-cost/", "Paver patio cost guide"),
        ("/artificial-turf-cost/", "Artificial turf cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Englewood, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Englewood, FL – County Line",
    "meta": "Concrete driveway installers in Englewood, FL (Sarasota County side): the §124-255 culvert rule and the county-line permit split; range " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
    "h1": "Concrete Driveways on the Sarasota County Side of Englewood",
    "lede": capsule(
        "A concrete driveway in Englewood runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", current this October. On the Sarasota County side of the community, Sarasota "
        "County's Building Division reviews the permit, and where the drive crosses the roadside swale, a separate culvert permit comes first."
    ),
    "sections": [
        (
            "Confirming the county before confirming the permit",
            "<p>Because the Sarasota-Charlotte line runs irregularly through Englewood, roughly south of Dearborn Street and north of McCall Road " + ext(WIKI_SR776_URL, "Wikipedia, Florida State Road 776") +
            ", two driveways a few streets apart can answer to two different building departments. On the Sarasota County side, a Right-of-Way Use Permit covers any work in the county right-of-way, "
            "with no carve-out for how close the parcel sits to the county line " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ", and that's the permit this page walks through.</p>"
        ),
        (
            "The culvert spec that comes before the slab",
            "<p>Sarasota County treats the pipe under a driveway as its own category: a 20-foot minimum and 24-foot maximum culvert, reinforced or asphalt-coated corrugated pipe, with grade and size "
            "set by the County Engineer ahead of the pour " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ". The same section keeps a drainage easement clear of any paved surface at all, "
            "driveway or walkway " + src("sarasota-county-124-255-culverts") + ", a rule that comes up often on an older Dearborn Street-area lot where the original swale has silted in over four or five decades.</p>"
        ),
    ],
    "scenario": (
        "Replacing a cracked mid-century driveway on the Sarasota County side, worked out in square feet",
        "<p>Take a 20 by 50 foot driveway, 1,000 square feet, on a lot near Dearborn Street dating to the 1970s, where the slab has settled unevenly and the old culvert pipe has partly collapsed. At " +
        price("concrete-driveway") + " per " + per("concrete-driveway") + ", the pour runs $6,000 to $15,000, tightening to roughly $8,000 to $12,000 inside the typical " + price("concrete-driveway", typical=True) +
        " band. Because the culvert needs replacing anyway, the county's line-and-grade review happens before either the pipe or the new slab goes in, not after.</p>"
    ),
    "faqs": [
        faq(
            "How do I find out which county reviews my Englewood driveway permit?",
            "Search the parcel on the county property appraiser's site or call the Sarasota County Building Division directly, since the county line zig-zags near Dearborn Street and McCall Road rather than following one street."
        ),
        faq(
            "Is there a size limit on the culvert pipe itself?",
            "County staff size it to the ditch, generally landing somewhere between 20 and 24 feet long, and they'll call for a longer run only where that particular swale happens to run deeper than the standard cross-section."
        ),
        faq(
            "Why does the county care so much about where exactly a driveway sits relative to the swale?",
            "Because the swale is doing the drainage work for the whole street, not just one lot; a paved surface built into that easement blocks water the next storm needs somewhere to go, which is why the county won't permit one there."
        ),
    ],
    "sources": SRC,
}

# 2. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Englewood, FL – Coverage & Setback",
    "meta": "Paver patio installers in Englewood, FL (Sarasota side): the 35% building cap vs. the 50% nonconforming rule; range " + price("paver-patio") + " per " + per("paver-patio") + ".",
    "h1": "Paver Patios on Englewood's Sarasota County Side",
    "lede": capsule(
        "Englewood paver patios price out around " + price("paver-patio") + " per " + per("paver-patio") + " this October 2026, and the coverage rule that applies turns on when the lot was platted, with a patio "
        "near Englewood's stretch of Manasota Key carries an extra setback line most of the rest of the Sarasota County side never has to check."
    ),
    "sections": [
        (
            "Two coverage ceilings, one depending on a 1975 cutoff",
            "<p>Sarasota County's RSF zoning, which covers most residential lots on this side of Englewood, caps building coverage, the house footprint itself, at 35 percent, a number that doesn't touch "
            "a patio beside it " + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ". An older lot recorded on or before November 11, 1975 instead falls under the county's nonconforming "
            "RMF rule, a 50 percent impervious ceiling that counts pavers, pool decks and concrete directly while excluding grass and shell " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") +
            ". Many of the platted lots north of Dearborn Street date well before that cutoff, which makes checking the plat date worth doing before sizing a patio.</p>"
        ),
        (
            "Why the Manasota Key sliver needs an extra check",
            "<p>A patio or pool deck on the Sarasota County stretch of Manasota Key, north of Blind Pass, answers to the county's own Gulf Beach Setback Line on top of the standard coverage rule, barring "
            "construction seaward of it without a variance " + src("sarasota-county-54-723-gbsl", "Sarasota County Code §54-723") + ". FEMA's coastal flood categories split that stretch further, between the one-percent-chance "
            "Zone AE and the surf-exposed Zone VE " + src("fema-coastal-firm", "FEMA's coastal flood-map guidance") + ", a distinction worth pulling up by address before a " + svc("concrete-pool-decks", "pool deck") +
            " or patio's finished elevation gets set.</p>"
        ),
    ],
    "scenario": (
        "A patio addition on a pre-1975 Dearborn-area lot, worked out in square feet",
        "<p>Consider a 320 square foot paver patio planned off the back of a home near Dearborn Street, on a lot platted in the early 1960s, old enough to fall under the county's nonconforming 50 percent "
        "impervious rule rather than the newer 35 percent building-only cap. At " + price("paver-patio") + " per " + per("paver-patio") + ", the job runs $3,200 to $5,440, narrowing to about $3,840 to "
        "$5,120 inside the typical " + price("paver-patio", typical=True) + " band. Before pricing it, the lot's existing pool deck and driveway square footage get tallied against that 50 percent ceiling, "
        "since the new patio has to fit inside what's left of it.</p>"
    ),
    "faqs": [
        faq(
            "Which coverage rule applies to my Englewood patio, 35% or 50%?",
            "It depends on the plat date. A lot recorded on or before November 11, 1975 falls under Sarasota County's 50 percent impervious-coverage rule; a newer RSF lot instead caps building coverage, not paving, at 35 percent."
        ),
        faq(
            "Does every patio near Englewood's Manasota Key stretch need a state coastal permit?",
            "Only one seaward of Florida's Coastal Construction Control Line, which mainly affects the key's Gulf side north of Blind Pass. A patio set well back from the beach on that stretch usually clears the county's setback line without needing the state permit."
        ),
        faq(
            "Does grass or shell count against my lot's coverage limit in Englewood?",
            "No, under the county's nonconforming-lot rule. Grass, shell and other water-permeable surfaces are specifically excluded from the 50 percent impervious-coverage calculation that catches pavers, concrete and asphalt."
        ),
    ],
    "sources": SRC,
}

# 3. artificial-turf --------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Englewood, FL – Older Lawns",
    "meta": "Artificial turf installers in Englewood, FL (Sarasota side): the state water-buffer rule and SWFWMD's Phase III order; market range " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
    "h1": "Artificial Turf for Englewood Yards",
    "lede": capsule(
        "Turf installation in Englewood prices out at " + price("artificial-turf") + " per " + per("artificial-turf") + " this October. With a median age near 69 on the Sarasota County side, plenty "
        "of homeowners here are trading a lawn that needs mowing and watering for one that needs neither, within the limits of the state's new turf rule."
    ),
    "sections": [
        (
            "A rule that reaches canal lots and lots near Lemon Bay alike",
            "<p>DEP Rule 62-308.100, effective May 19, 2026, sets a 10-foot minimum buffer between turf and open water, unless a seawall already forms the property line, on top of requiring a washed-rock "
            "base and natural infill " + src("dep-rule", "DEP Rule 62-308.100") + ". Englewood backs onto Lemon Bay and a number of residential canals feeding it, so measuring that gap from the actual seawall "
            "or shoreline, rather than from the fence line, is worth doing before a layout gets finalized, since this is a statewide floor and no city or county ordinance can push it any tighter " + src("fs125572", "F.S. 125.572") + ".</p>"
        ),
        (
            "Why an older, retiree-heavy community leans toward lower-upkeep turf",
            "<p>The Census Bureau's current estimate puts Englewood's median age at 68.5, well above the metro average " + ext(CENSUS_ENGLEWOOD_URL, "Census Reporter, Englewood CDP") + ", and the district's own "
            "shortage order has every sprinkler system on this side of the county down to a single assigned day a week into 2027 " + src("swfwmd-restrictions", "SWFWMD district restrictions") + ". Skipping both the mower "
            "and the sprinkler zone tends to draw more interest here than in a younger subdivision down the road, and once turf replaces a lawn, F.S. 720.3045's 2026 protection still only covers a panel "
            "an HOA genuinely can't see from the street or a neighboring lot " + src("fs720-3045", "F.S. 720.3045") + ".</p>"
        ),
    ],
    "scenario": (
        "Converting a canal-lot lawn near Dearborn Street, worked out in square feet",
        "<p>A retired homeowner on a canal lot a few blocks from Dearborn Street has watched the front lawn thin out to bare patches under the district's one-day-a-week limit, and wants 380 square "
        "feet converted to turf, with the layout measured 14 feet back from the seawall that lines the canal. At " + price("artificial-turf") + " per " + per("artificial-turf") + ", the full price range "
        "runs $3,800 to $9,500, settling closer to $4,560–$6,840 inside the usual " + price("artificial-turf", typical=True) + " window once pile height and backing are chosen. Fourteen feet clears the "
        "state's 10-foot floor without a variance, and the washed-rock base goes in exactly as it would three streets inland.</p>"
    ),
    "faqs": [
        faq(
            "Does a canal lot in Englewood need extra clearance for turf?",
            "Only the standard statewide one: at least 10 feet between the turf and the water's edge, unless a seawall already forms the property line, in which case that buffer condition doesn't apply."
        ),
        faq(
            "Why does turf come up so often in conversations with older Englewood homeowners?",
            "Two things line up here: the district's shortage order has cut sprinklers to a single day a week, and the area's median age sits near 69, so a lawn demanding more hands-on upkeep than it used to get is often the deciding factor."
        ),
        faq(
            "Does an HOA in Englewood still get a say over turf?",
            "The state law preempting local government turf restrictions doesn't reach HOA architectural review, so a community's own approval process can still apply; F.S. 720.3045 only protects turf that isn't visible from the frontage or an adjacent parcel."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
