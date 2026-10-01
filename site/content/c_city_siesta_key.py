# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "siesta-key"

CANAVERAL_URBAN_OSD_URL = "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANAVERAL.html"
SIESTA_ACS_URL = "https://censusreporter.org/profiles/16000US1266000-siesta-key-fl/"
SIESTA_ASSOC_HISTORY_URL = "https://siestakeyassociation.com/about/history/"
SIESTA_ANNEXATION_URL = "https://www.yourobserver.com/news/2022/jan/18/sarasota-city-commissioners-vote-to-extend-a-hand-to-siesta-key/"
SIESTA_BEACH_WIKI_URL = "https://en.wikipedia.org/wiki/Siesta_Beach"
MILTON_ANNIVERSARY_URL = "https://www.mysuncoast.com/2025/10/09/hurricane-milton-made-landfall-near-siesta-key-one-year-ago-first-sarasota-county-landfall-since-1944/"

SRC = [
    "sarasota-county-row-permit", "sarasota-county-98-3-culvert-row-fees", "sarasota-county-124-255-culverts",
    "sarasota-county-124-76-rsf-standards", "sarasota-county-124-283-nonconforming-isr", "sarasota-county-54-723-gbsl",
    "sarasota-county-22-63-retaining-walls", "sarasota-county-building-page", "sarasota-county-online-permitting",
    "fdep-cccl-program", "fdep-cccl-apply", "fdot-sdg", "dep-rule", "fs125572", "swfwmd-restrictions", "usda-wss",
    ("USDA NRCS Official Series Description — Canaveral", CANAVERAL_URBAN_OSD_URL),
    ("Census Reporter, Siesta Key CDP FL (ACS 2020-2024 5-yr, B01003/B25035/B25024)", SIESTA_ACS_URL),
    ("Siesta Key Association — History", SIESTA_ASSOC_HISTORY_URL),
    ("Your Observer — Sarasota city commissioners vote to extend a hand to Siesta Key (Jan. 18, 2022)", SIESTA_ANNEXATION_URL),
    ("Wikipedia — Siesta Beach (Harvard University sand-composition study, TripAdvisor ranking)", SIESTA_BEACH_WIKI_URL),
    ("WWSB/Mysuncoast.com — Hurricane Milton landfall near Siesta Key, one year later (Oct. 9, 2025)", MILTON_ANNIVERSARY_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Which office permits a driveway, culvert or pool deck on Siesta Key?",
        "<p>Mostly Sarasota County's, with one real exception worth knowing about. The county's land development code requires a "
        "\"Right-of-Way Use Permit application\" for \"all work within the County right-of-way,\" and a separate culvert permit "
        "specifically for a \"residential access driveway\" tying into an open drainage swale " +
        src("sarasota-county-row-permit", "Sarasota County Code §124-48") + " " +
        src("sarasota-county-98-3-culvert-row-fees", "Sarasota County Code §98-3") + ". That covers most of the island, but the "
        "northern tip, long referred to as the Bay Island area, was annexed into the City of Sarasota decades ago, and the city "
        "commission voted in January 2022 to explore folding in the rest of the key as well " +
        ext(SIESTA_ANNEXATION_URL, "Your Observer, Sarasota city commissioners vote to extend a hand to Siesta Key") +
        ". A homeowner on that stretch of the island actually answers to the city desk covered on " + city("sarasota", "our "
        "Sarasota page") + ", not the county one described here. Everywhere else, applications run through the county's own "
        "Accela portal " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") + ".</p>"
    ),
    sec(
        "Why do older Siesta Key lots answer to a different coverage cap?",
        "<p>Because a large share of the island was platted long before the county's current zoning existed. In the county's RSF "
        "districts, the standard rule caps the house itself, not the driveway or patio, at 35 percent of the lot " +
        src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ". But a nonconforming RMF lot recorded on "
        "or before November 11, 1975, which describes plenty of the older platting around the island's historic village, instead "
        "carries a 50 percent impervious cap that counts \"roof structures, swimming pools and pool decks, as well as concrete, "
        "asphalt, pavers,\" while excluding grass, shell and other water-permeable surfaces " +
        src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") + ". Figuring out which rule a given "
        "parcel falls under, the 35 percent building-only cap or the older lot's 50 percent impervious total, is one of the first "
        "calls we make before pricing a " + svc("paver-driveways") + " or a pool deck addition here.</p>"
    ),
    sec(
        "What do the Gulf Beach Setback Line and the state's control line add near the water?",
        "<p>Two separate lines, stacked. The county's own Gulf Beach Setback Line bars \"Construction or Excavation\" seaward of "
        "it or waterward of the Barrier Island Pass Hazard Line on Siesta, Casey and Manasota Keys specifically, and a project "
        "inside that zone needs its own coastal setback variance " + src("sarasota-county-54-723-gbsl", "Sarasota County Code "
        "§54-723") + ". On top of that, Florida's Coastal Construction Control Line Program requires a separate DEP permit for "
        "\"construction and excavation activities seaward of the CCCL,\" named specifically for Siesta Key's beaches among others "
        "" + src("fdep-cccl-program", "FDEP's CCCL program") + " " + src("fdep-cccl-apply", "FDEP's CCCL application page") +
        ". A " + svc("concrete-pool-decks") + " or a low retaining wall anywhere near Siesta's Gulf-front dune has to clear both "
        "lines, not just the one that's easier to find.</p>"
    ),
    sec(
        "What does a 'Canaveral-Urban land' soil reading mean for the base under a slab?",
        "<p>It flags ground that's already been reshaped. A soil map check run directly at a point on Siesta Key comes back "
        "\"Canaveral fine sand-Urban land complex,\" the same dune-ridge soil found on Longboat Key but mapped here together with "
        "disturbed, often filled ground from decades of platting and construction " + src("usda-wss") + " " +
        ext(CANAVERAL_URBAN_OSD_URL, "NRCS Official Series Description, Canaveral") + ". The native Canaveral profile drains "
        "quickly and holds a water table only 10 to 40 inches down for part of the year, but the \"Urban land\" half of that "
        "reading means the compaction history under a given lot is less predictable than an undisturbed dune ridge, which is "
        "exactly the kind of detail a pre-pour soil check is meant to catch before a slab goes in.</p>"
    ),
    sec(
        "What does the island's 1976 median build year and condo-heavy housing mix change?",
        "<p>Quite a bit about who actually signs off on a job. The Census Bureau's own survey puts Siesta Key's population at "
        "5,525 as of its latest five-year estimate, with a median year structure built of 1976 " +
        ext(SIESTA_ACS_URL, "Census Reporter, Siesta Key CDP FL") + ", and of the island's roughly 7,767 housing units, only about "
        "four in ten sit in a one- or two-unit building; roughly a quarter are in structures of 50 units or more. That split "
        "traces back to the island's own history: the Siesta Land Company, formed in 1907 by Capt. Louis Roberts, Harry Higel and "
        "E.M. Arbogast, platted the original village, the first bridge to Sarasota opened in 1917 and a second at Stickney Point "
        "followed in 1926 " + ext(SIESTA_ASSOC_HISTORY_URL, "Siesta Key Association, History") + ", well before the condominium "
        "towers that now share the shoreline with those older cottages. A driveway quote near the village usually means an older "
        "single-family lot; a pool-deck quote on the Gulf side more often means a condominium association's common area, which "
        "routes through a different decision-maker than an individual homeowner would.</p>"
    ),
    sec(
        "What did Hurricane Milton change here, and what's finishing up now?",
        "<p>Milton made landfall almost on top of the island on October 9, 2024, a Category 3 storm that the county's own "
        "one-year recap called the first hurricane to hit Sarasota County since 1944 " +
        ext(MILTON_ANNIVERSARY_URL, "Mysuncoast.com, Hurricane Milton landfall near Siesta Key, one year later") + ". The storm "
        "and Hurricane Helene 13 days earlier reopened the historic Midnight Pass between Siesta Key and Casey Key, a channel "
        "that had been filled in since the 1980s, and county crews spent months afterward clearing debris and rebuilding "
        "infrastructure, work that was still ongoing on some projects a year later. Beach sand pushed inland by the storm surge "
        "shifted the practical edge of the Gulf Beach Setback Line on some lots, which is one more reason a current survey, not "
        "an old one, is worth checking before a " + svc("retaining-walls") + " or pool deck goes in near the water. Siesta Key "
        "also sits under the Southwest Florida Water Management District's current irrigation order, same as the rest of the "
        "county " + src("swfwmd-restrictions") + ".</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Is Siesta Key inside the City of Sarasota or Sarasota County?",
        "Mostly the county. Sarasota County's Right-of-Way Use Permit and culvert rules cover most of the island, but the northern Bay Island area has been inside Sarasota's city limits for decades, and the city has since discussed annexing more of the key."
    ),
    faq(
        "Can I build right up to the beach on Siesta Key?",
        "No. The county's own Gulf Beach Setback Line bars construction or excavation seaward of it on Siesta, Casey and Manasota Keys, and Florida's separate Coastal Construction Control Line adds a state DEP permit requirement on top of that county line."
    ),
    faq(
        "Does my Siesta Key lot get a different coverage limit because it's older?",
        "It can. A nonconforming lot recorded on or before November 11, 1975 carries a 50 percent impervious cap that counts pavers, concrete and pool decks, which is a different math than the 35 percent building-only cap that applies to a newer RSF lot."
    ),
    faq(
        "Does a condo building on Siesta Key follow the same driveway rules as a house?",
        "Not usually in practice. With roughly a quarter of the island's housing in buildings of 50 units or more, pool-deck and common-area paving work there typically routes through the condominium association and its own contractor process rather than an individual homeowner permit."
    ),
    faq(
        "Does a retaining wall need engineering here?",
        "Yes, over 4 feet. The county's pool-code amendment requires engineered drawings for any retaining wall taller than that, measured from grade at any point along the wall."
    ),
    faq(
        "Did Hurricane Milton change where the beach setback line sits?",
        "On some lots, yes. Storm surge and sand movement from the October 2024 landfall shifted the practical edge of the Gulf Beach Setback Line in places, which is why we check a current survey rather than an older one before pricing work near the dune."
    ),
]

HUB = page(
    "/siesta-key-fl/", "city",
    "Concrete, Pavers & Turf Contractor on Siesta Key, FL",
    "Concrete, pavers and turf on Siesta Key, FL: Sarasota County's §124-48 ROW permit, the Gulf Beach Setback Line and a 1976 median build year, October 2026.",
    "Concrete, Pavers and Artificial Turf for Siesta Key Homes",
    capsule(
        "Opera's Sarasota unit builds concrete, pavers and turf on Siesta Key, the barrier island where most permits run through "
        "unincorporated Sarasota County rather than a city hall, except for a northern strip annexed into Sarasota decades ago. As "
        "of October 2026, the county's Gulf Beach Setback Line and Florida's Coastal Construction Control Line both apply near the "
        "dune, and the island's median home was built in 1976."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Siesta Key",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/sarasota-county-driveway-patio-permits/", "Driveway and patio permits in Sarasota, Venice and North Port"),
        ("/longboat-key-fl/", "Concrete, pavers and turf on Longboat Key"),
        ("/venice-fl/", "Concrete, pavers and turf in Venice"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf on Siesta Key, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways on Siesta Key, FL – County Permits",
    "meta": "Concrete driveways on Siesta Key, FL need Sarasota County's §124-48 ROW permit and a culvert permit on open swales; market range is " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
    "h1": "Pouring a Concrete Driveway on Siesta Key",
    "lede": capsule(
        "A new or replacement concrete driveway on Siesta Key runs " + price("concrete-driveway") + " per " + per("concrete-driveway") +
        " as of October 2026. Sarasota County, not a city hall, reviews the right-of-way work on most of the island, and a "
        "driveway tying into an open drainage swale needs its own culvert permit on top of that."
    ),
    "sections": [
        (
            "Why a driveway apron here often means a culvert permit too",
            "<p>The county's code requires \"a Right-of-Way Use Permit application\" for all work in the right-of-way " +
            src("sarasota-county-row-permit", "Sarasota County Code §124-48") + ", and goes further for a driveway that crosses "
            "an open ditch: \"a culvert permit, a sub-class of the ROW Use Permit, shall be required for residential access "
            "driveways\" along roads with open drainage " + src("sarasota-county-124-255-culverts", "Sarasota County Code "
            "§124-255") + ". The pipe itself has to run 20 to 24 feet unless the ditch runs deeper, and the County Engineer sets "
            "the line and grade, not the contractor, which is why we survey the swale before quoting a driveway that touches "
            "one.</p>"
        ),
        (
            "Where no paved surface is allowed, period",
            "<p>The same culvert section is blunt about drainage easements: \"No walkways or driveways or other paved surfaces "
            "shall be located in the easement\" that carries a lot's stormwater " + src("sarasota-county-124-255-culverts") +
            ". On an older Siesta Key lot where the drainage easement runs close to the street, that rule can push a driveway's "
            "actual buildable width narrower than the county's culvert spacing alone would suggest, so we check the plat before "
            "pricing a wider apron, not after the forms are already staked.</p>"
        ),
    ],
    "scenario": (
        "Picture a 16 × 34 ft driveway, 544 sq ft, crossing an open swale on an older part of the island",
        "<p>Picture a 16 × 34 ft driveway, 544 sq ft, crossing an open swale on an older part of the island. Pricing it at " +
        price("concrete-driveway") + " per sq ft puts the job between $3,264 and $8,160, settling closer to $4,352 to $6,528 "
        "inside the typical " + price("concrete-driveway", typical=True) + " band. Before that number firms up, the County "
        "Engineer sets the culvert's line and grade across the swale, and the final width gets checked against any drainage "
        "easement on the plat, since paving inside one isn't allowed regardless of how the rest of the driveway is laid out.</p>"
    ),
    "faqs": [
        faq(
            "Does my Siesta Key driveway need a culvert permit?",
            "If it crosses an open drainage swale, yes, under Sarasota County Code §124-255, in addition to the general §124-48 right-of-way use permit that covers any work in the county's right-of-way."
        ),
        faq(
            "Can I pave over a drainage easement on my lot?",
            "No. The county's code is explicit that no walkways, driveways or other paved surfaces may sit inside a drainage easement, which can narrow a driveway's realistic width on an older platted lot."
        ),
        faq(
            "Who sets the culvert pipe's grade on Siesta Key?",
            "The County Engineer, not the contractor. Driveway culverts run 20 to 24 feet unless the ditch is deeper, and the pipe material has to be one the County Engineer approves."
        ),
    ],
    "sources": SRC,
}

# 2. paver-driveways -----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways on Siesta Key, FL – Old Lot Coverage",
    "meta": "Paver driveways on Siesta Key, FL count toward a 50% impervious cap on pre-1975 lots, unlike the county's 35% building-only rule; range " + price("paver-driveway") + " per " + per("paver-driveway") + ".",
    "h1": "Paver Driveway Installation on Siesta Key",
    "lede": capsule(
        "A paver driveway on Siesta Key runs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026. "
        "Which coverage rule applies depends on when the lot was platted: a newer lot's cap touches only the house, while an "
        "older lot's cap counts the driveway's pavers directly."
    ),
    "sections": [
        (
            "The 35 percent rule doesn't touch a driveway at all",
            "<p>In the county's RSF districts, the standard development rule caps building coverage, the house itself, at 35 "
            "percent of the lot " + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ". A paver "
            "driveway on a lot governed by that rule simply isn't part of the math, which means widening a two-car paver "
            "driveway to three cars on a standard RSF lot doesn't push the parcel toward that particular ceiling.</p>"
        ),
        (
            "Why a pre-1975 lot is a different conversation entirely",
            "<p>A nonconforming RMF lot of record from on or before November 11, 1975, common around Siesta Key's older platting, "
            "instead carries a 50 percent impervious cap that explicitly counts \"concrete, asphalt, pavers\" alongside the roof "
            "and any pool deck, while excluding grass, shell or other surfaces water can pass through " +
            src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") + ". On one of these older lots, a "
            "paver driveway's square footage gets added to the running total before the job is priced, since that total, not "
            "just the house, is what the 50 percent line is measuring.</p>"
        ),
    ],
    "scenario": (
        "Picture an 18 × 32 ft paver driveway, 576 sq ft, on a lot platted before 1975 and already carrying a pool deck",
        "<p>Picture an 18 × 32 ft paver driveway, 576 sq ft, on a lot platted before 1975 and already carrying a pool deck. "
        "Pricing it at " + price("paver-driveway") + " per sq ft comes out between $5,760 and $17,280, tightening toward $6,912 "
        "to $11,520 inside the typical " + price("paver-driveway", typical=True) + " band depending on the paver chosen. Because "
        "this lot falls under the nonconforming 50 percent impervious cap rather than the newer 35 percent building-only rule, "
        "the driveway's full footprint gets added to whatever the house, pool and pool deck already total before the design is "
        "finalized.</p>"
    ),
    "faqs": [
        faq(
            "Does a paver driveway count toward my Siesta Key lot's coverage limit?",
            "It depends on the lot. Under the county's standard 35 percent rule, only the house counts; on a nonconforming lot recorded before November 11, 1975, pavers count directly toward a separate 50 percent impervious cap."
        ),
        faq(
            "How do I know if my Siesta Key lot is nonconforming?",
            "A lot recorded on or before November 11, 1975 typically qualifies, which is common on the older platted sections of the island. We check the plat date before pricing a wider driveway."
        ),
        faq(
            "Can I widen a paver driveway on an older Siesta Key lot?",
            "Only after checking the running impervious total against the 50 percent cap, since the house, pool, pool deck and driveway all count together on a nonconforming lot."
        ),
    ],
    "sources": SRC,
}

# 3. concrete-patios -------------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios on Siesta Key, FL – Cottage or Condo",
    "meta": "Concrete patios on Siesta Key, FL: older single-family cottages near the Village permit differently than a condo's common area; range " + price("concrete-patio") + " per " + per("concrete-patio") + ".",
    "h1": "Building a Concrete Patio on Siesta Key",
    "lede": capsule(
        "A concrete patio on Siesta Key runs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. "
        "With roughly a quarter of the island's housing stock in buildings of 50 units or more, a lot of patio work here is a "
        "condominium's common area, not an individual homeowner's backyard."
    ),
    "sections": [
        (
            "Why 'who orders the patio' matters as much as the design",
            "<p>Of Siesta Key's roughly 7,767 housing units, only about four in ten sit in a one- or two-unit structure, while "
            "around a quarter are in buildings of 50 units or more " + ext(SIESTA_ACS_URL, "Census Reporter, Siesta Key CDP FL") +
            ". A patio addition behind a single-family cottage goes through the homeowner directly, the way it would on the "
            "mainland. A patio or walkway resurfacing job at a 50-unit condominium instead routes through the association's "
            "board and its own contractor-approval process, which usually takes longer to schedule than a straightforward "
            "residential job even when the concrete work itself is simpler.</p>"
        ),
        (
            "What the county's permit exemption notes leave unclear",
            "<p>The county's own guidance on patios without footings is thinner than what some cities publish: an on-grade "
            "residential patio without footings may be exempt, but the exact scope wasn't confirmed on the county's own site when "
            "we checked " + src("sarasota-county-building-page", "Sarasota County Building") + ". Rather than guess, we confirm "
            "the scope with the county's Building Division before pricing a patio as permit-free, the same way we would for " +
            svc("concrete-pool-decks", "a pool deck") + " addition on the same lot.</p>"
        ),
    ],
    "scenario": (
        "Picture a 16 × 18 ft patio extension, 288 sq ft, off the back of a single-family cottage near the Village",
        "<p>Picture a 16 × 18 ft patio extension, 288 sq ft, off the back of a single-family cottage near the Village. At " +
        price("concrete-patio") + " per sq ft, that project runs $1,728 to $3,744, or about $2,016 to $2,880 inside the typical "
        "" + price("concrete-patio", typical=True) + " band for a broom finish matched to the existing slab. Because this is a "
        "single-family lot, the homeowner signs off directly rather than waiting on a condominium board, though we still confirm "
        "the permit-exemption scope with the county before pouring, since the island's own guidance on footings-free patios "
        "leaves some of that scope unconfirmed.</p>"
    ),
    "faqs": [
        faq(
            "Does a condo need a different process than a house for patio work on Siesta Key?",
            "In practice, yes. A single-family homeowner can request and approve the work directly, while a condominium association's common-area patio or walkway usually has to clear the board and its own contractor-approval process first."
        ),
        faq(
            "Is a small concrete patio exempt from a permit on Siesta Key?",
            "The county's own published guidance suggests an on-grade patio without footings may not need one, but the exact scope wasn't confirmed on the county's site, so we check with the Building Division before pricing it as exempt."
        ),
        faq(
            "Why is so much of Siesta Key's housing in large buildings?",
            "About a quarter of the island's roughly 7,767 housing units sit in buildings of 50 units or more, a mix that grew up alongside the older single-family cottages near the historic village over the past several decades."
        ),
    ],
    "sources": SRC,
}

# 4. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios on Siesta Key, FL – Disturbed Dune Base",
    "meta": "Paver patios on Siesta Key, FL sit on a 'Canaveral-Urban land' soil reading, signaling fill under much of the island; range " + price("paver-patio") + " per " + per("paver-patio") + ".",
    "h1": "Paver Patios and Walkways on Siesta Key",
    "lede": capsule(
        "A paver patio on Siesta Key runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. A soil "
        "map check at the island comes back a 'Canaveral-Urban land' reading, meaning the dune sand under a given lot has often "
        "been disturbed or filled, not left as it was originally deposited."
    ),
    "sections": [
        (
            "What 'Urban land' means next to the soil series name",
            "<p>The reading at a Siesta Key coordinate comes back \"Canaveral fine sand-Urban land complex, 0 to 5 percent "
            "slopes,\" pairing the island's natural dune soil with ground the survey itself flags as altered " + src("usda-wss") +
            " " + ext(CANAVERAL_URBAN_OSD_URL, "NRCS Official Series Description, Canaveral") + ". The native Canaveral profile "
            "drains quickly, but decades of platting, fill and construction mean the compacted layer under a given Siesta Key lot "
            "is less predictable than that profile alone would suggest, which is why we probe the actual base before setting a "
            "paver patio's bedding depth rather than assuming the textbook soil answer.</p>"
        ),
        (
            "Working around what's already buried",
            "<p>On an older lot near the Village, a new paver patio excavation sometimes turns up remnants of a prior slab, old "
            "shell fill or utility lines from a build predating current record-keeping. None of that changes the bedding-sand "
            "spec itself, but it does change how much of the layout gets confirmed by probing before the crew commits to a final "
            "elevation, especially on a patio that ties into " + svc("concrete-patios", "an existing concrete") + " surface rather "
            "than starting on open ground.</p>"
        ),
    ],
    "scenario": (
        "Picture a 20 × 16 ft paver patio, 320 sq ft, replacing an older slab near Siesta Key Village",
        "<p>Picture a 20 × 16 ft paver patio, 320 sq ft, replacing an older slab near Siesta Key Village. At " +
        price("paver-patio") + " per sq ft, the job comes to $3,200 to $5,440; picking a paver and pattern within the typical " +
        price("paver-patio", typical=True) + " range tightens that to about $3,840 to $5,120. Because the soil reading "
        "here flags disturbed ground alongside the natural dune sand, a test probe ahead of excavation is what decides the final "
        "base depth, not the series name alone, and any leftover shell fill or old slab fragments get cleared before the new "
        "bedding sand goes down.</p>"
    ),
    "faqs": [
        faq(
            "Is Siesta Key's soil different from Longboat Key's?",
            "They share the same Canaveral dune sand series, but the Siesta Key reading comes back paired with 'Urban land,' flagging ground that's been disturbed or filled by decades of construction, which Longboat Key's own reading at the coordinates we checked didn't show."
        ),
        faq(
            "Will excavation for a paver patio hit old fill or debris here?",
            "It can, especially near the older platted sections of the island. We probe the base before setting a final bedding depth rather than relying on the soil series name alone."
        ),
        faq(
            "Does disturbed soil mean a deeper paver base is required?",
            "Not automatically, but it does mean the compacted layer under a given lot is harder to predict than an undisturbed dune, so we check it directly rather than assume the textbook depth applies."
        ),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks on Siesta Key, FL – Setback Lines",
    "meta": "Concrete pool decks on Siesta Key, FL near the Gulf face the county's Gulf Beach Setback Line plus the state CCCL permit; range " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ".",
    "h1": "Concrete Pool Deck Installation on Siesta Key",
    "lede": capsule(
        "A concrete pool deck on Siesta Key runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of "
        "October 2026. A deck close to the Gulf has to clear two separate lines: the county's own Gulf Beach Setback Line and "
        "Florida's statewide Coastal Construction Control Line."
    ),
    "sections": [
        (
            "Two lines, not one, near the dune",
            "<p>Sarasota County's own Gulf Beach Setback Line bars \"Construction or Excavation\" seaward of it or waterward of "
            "the Barrier Island Pass Hazard Line specifically on Siesta, Casey and Manasota Keys, and a project inside that zone "
            "needs its own coastal setback variance from the county " + src("sarasota-county-54-723-gbsl", "Sarasota County Code "
            "§54-723") + ". That county line sits in addition to, not instead of, the state's Coastal Construction Control Line "
            "permit, which DEP requires for \"construction and excavation activities seaward of the CCCL\" " +
            src("fdep-cccl-program", "FDEP's CCCL program") + ". A deck that clears one line but not the other still can't be "
            "built, so both get checked before a design is drawn.</p>"
        ),
        (
            "What storm-shifted sand changed about where that line sits",
            "<p>Hurricane Milton's October 2024 landfall near the island, and the surge from Hurricane Helene 13 days before it, "
            "pushed enough sand around on some stretches of beach that the practical edge of the setback line has moved on "
            "certain lots since the last survey most homeowners have on file " +
            ext(MILTON_ANNIVERSARY_URL, "Mysuncoast.com, Hurricane Milton landfall near Siesta Key") + ". We pull a current survey "
            "rather than rely on an older plat before pricing a deck addition anywhere near the dune, since the setback line "
            "itself, not just the sand on top of it, can have shifted.</p>"
        ),
    ],
    "scenario": (
        "Picture a 24 × 28 ft pool deck, 672 sq ft, on a Gulf-front lot close enough to the dune to raise the setback question",
        "<p>Picture a 24 × 28 ft pool deck, 672 sq ft, on a Gulf-front lot close enough to the dune to raise the setback "
        "question. Pricing it at " + price("concrete-pool-deck") + " per sq ft lands between $3,360 and $10,080, settling near "
        "$4,704 to $8,064 inside the typical " + price("concrete-pool-deck", typical=True) + " band for a textured, "
        "slip-resistant surface pitched to a drain. Before that figure firms up, a current survey confirms where the Gulf Beach "
        "Setback Line and the state's control line actually fall on this particular parcel, since storm-driven sand movement "
        "since 2024 means an older survey may no longer match the ground as it sits today.</p>"
    ),
    "faqs": [
        faq(
            "Does my Siesta Key pool deck need a county permit, a state permit, or both?",
            "Possibly both. The county's Gulf Beach Setback Line requires its own variance for work seaward of it, and Florida's separate Coastal Construction Control Line adds a DEP permit requirement on top, independent of each other."
        ),
        faq(
            "Did Hurricane Milton move the beach setback line on Siesta Key?",
            "On some lots, the storm surge and sand movement from the October 2024 landfall shifted where the practical edge of the setback sits, which is why we check a current survey rather than an older one before designing a deck near the dune."
        ),
        faq(
            "What's the Barrier Island Pass Hazard Line?",
            "A second boundary the county names alongside the Gulf Beach Setback Line, specific to Siesta, Casey and Manasota Keys, and construction or excavation waterward of either one needs a coastal setback variance."
        ),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ----------------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers on Siesta Key, FL – Retaining Walls",
    "meta": "Pool deck pavers on Siesta Key, FL near a low retaining wall over 4 ft need engineered drawings under §22-63; range " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ".",
    "h1": "Travertine and Paver Pool Decks on Siesta Key",
    "lede": capsule(
        "Pool deck pavers or travertine on Siesta Key run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") +
        " as of October 2026. A deck that steps down toward a canal or a seawall often needs a low retaining wall alongside it, "
        "and the county requires engineered drawings once that wall passes 4 feet."
    ),
    "sections": [
        (
            "Why a deck's retaining wall can trigger engineering the deck itself doesn't",
            "<p>Sarasota County's pool-code amendment requires engineered drawings for \"all retaining walls greater than four "
            "feet in height,\" measured from grade at any point along the wall " +
            src("sarasota-county-22-63-retaining-walls", "Sarasota County Code §22-63") + ". A travertine or paver deck stepping "
            "down toward a seawall or a lower canal-side yard frequently needs a short retaining wall to hold the grade change, "
            "and that wall, not the deck surface itself, is usually what decides whether an engineer gets involved before the "
            "permit is filed.</p>"
        ),
        (
            "What the salt load off the Gulf and the bay does to the finish",
            "<p>Bridge engineers classify a structure as sitting in a corrosive marine environment once it's within 2,500 feet of "
            "water testing above 2,000 parts per million chloride " + src("fdot-sdg") + ", and a barrier island this narrow "
            "rarely has a lot that clears that distance from either the Gulf or the bay side. The paver base underneath a "
            "travertine deck doesn't need anything different for that reading, but the polymeric joint sand and any unprotected "
            "metal edge restraint give out sooner than the same materials would a few miles up the mainland, so " +
            svc("paver-sealing", "resealing") + " a Siesta Key deck is usually budgeted on a tighter schedule from day one.</p>"
        ),
    ],
    "scenario": (
        "Picture a 600 sq ft travertine pool deck stepping down 5 feet to a canal-side seawall",
        "<p>Picture a 600 sq ft travertine pool deck stepping down 5 feet to a canal-side seawall. Pricing the overlay at " +
        price("pool-deck-pavers") + " per sq ft puts the job between $7,200 and $18,000, tightening toward $8,400 to $13,200 "
        "inside the typical " + price("pool-deck-pavers", typical=True) + " band once the stone and pattern are set. Because the "
        "grade change to the seawall clears 4 feet, the retaining wall supporting that step needs engineered drawings before the "
        "county signs off, even though the deck surface above it doesn't carry the same requirement on its own.</p>"
    ),
    "faqs": [
        faq(
            "Does my Siesta Key pool deck need engineering for a retaining wall?",
            "If any part of a retaining wall supporting the deck exceeds 4 feet in height, yes, under the county's pool-code amendment, measured from grade at the tallest point along the wall."
        ),
        faq(
            "Why does salt matter more for a Siesta Key pool deck than one inland?",
            "Bridge engineers treat anything within 2,500 feet of water that tests above 2,000 parts per million chloride as a corrosive marine environment, a reading that applies to most waterfront lots on an island this narrow and that shortens how long joint sand and metal hardware hold up before resealing."
        ),
        faq(
            "Is travertine a good choice for a canal-side Siesta Key deck?",
            "It's a common choice, though no verified temperature or reflectance figure exists for it against a concrete paver deck, so we price the stone on its look and upkeep rather than quoting a specific coolness claim."
        ),
    ],
    "sources": SRC,
}

# 7. stamped-concrete -------------------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete on Siesta Key, FL – Village Lots",
    "meta": "Stamped concrete on Siesta Key, FL: older cottage lots near the Village read differently than a newer Gulf-front build; market range is " + price("stamped-concrete") + " per " + per("stamped-concrete") + ".",
    "h1": "Stamped Concrete Driveways and Patios on Siesta Key",
    "lede": capsule(
        "Stamped concrete on Siesta Key runs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October "
        "2026. The island's own history, platted as Siesta Village in 1907, left a cluster of narrow older cottage lots that "
        "call for a different pattern scale than a newer Gulf-front build does."
    ),
    "sections": [
        (
            "How a 1907 village plat changed what fits on a narrow lot",
            "<p>The Siesta Land Company platted the original village in 1907, and the first bridge connecting the key to "
            "Sarasota opened a decade later, in 1917 " + ext(SIESTA_ASSOC_HISTORY_URL, "Siesta Key Association, History") + ". "
            "Lots laid out on that original village grid tend to run narrower than anything platted since, which leaves less "
            "room between a driveway or entry walk and the house itself. A large-format stamped pattern sized for a modern "
            "Gulf-front lot can look oversized at that scale, so we size the joint layout and pattern repeat down to match the "
            "narrower frontage rather than reusing a layout drawn for a bigger property.</p>"
        ),
        (
            "Matching a 1976-median home without overdoing the texture",
            "<p>The island's median year structure built sits at 1976 " + ext(SIESTA_ACS_URL, "Census Reporter, Siesta Key CDP "
            "FL") + ", a generation of single-story, low-roofline homes where a heavily textured, deep-relief stamp can compete "
            "visually with the house's own flat planes rather than complementing them. A shallower, more subtle texture in a "
            "single color tends to sit better against that kind of roofline than a deep ashlar or cobble relief would, which is "
            "the direction we steer most quotes on an original 1976-era Siesta Key home.</p>"
        ),
    ],
    "scenario": (
        "Picture a 380 sq ft stamped-concrete driveway apron and entry walk on a narrow lot near the original village grid",
        "<p>Picture a 380 sq ft stamped-concrete driveway apron and entry walk on a narrow lot near the original village grid. "
        "At " + price("stamped-concrete") + " per sq ft, pricing comes to $3,040 to $7,220, settling closer to $4,560 to $6,080 "
        "inside the typical " + price("stamped-concrete", typical=True) + " band depending on the pattern scale chosen. Given "
        "the lot's narrow village-era frontage, we'd size the pattern repeat down from what a wider Gulf-front lot could carry, "
        "and keep the texture shallow enough that it reads as a finish on the slab rather than competing with the low, flat "
        "roofline of the 1976-era house it fronts.</p>"
    ),
    "faqs": [
        faq(
            "Does a narrow village-grid lot need a different stamped pattern?",
            "Usually a smaller-scale pattern, since Siesta Key's original 1907 village plat left narrower lots than later subdivisions, and a large-format stamp sized for a wider property can look out of proportion there."
        ),
        faq(
            "What texture suits a 1976-era Siesta Key home?",
            "A shallower, more subtle stamped texture in a single color tends to sit better against that generation's low, flat rooflines than a deep ashlar or cobble relief, which can visually compete with the house rather than complement it."
        ),
        faq(
            "Is stamped concrete pricier than a plain driveway on Siesta Key?",
            "Yes, the market range here runs " + price("stamped-concrete") + " per sq ft against " + price("concrete-driveway") + " for plain concrete, a gap driven by the integral pigment, release agent and stamping labor rather than anything about the permit process."
        ),
    ],
    "sources": SRC,
}

# 8. artificial-turf -------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf on Siesta Key, FL – Setback & Watering",
    "meta": "Artificial turf on Siesta Key, FL needs a 10-ft waterbody setback and skips the current SWFWMD watering order; range " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
    "h1": "Artificial Turf Installation on Siesta Key",
    "lede": capsule(
        "Artificial turf on Siesta Key runs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October "
        "2026. The state's own turf standard sets a 10-foot setback from the water that matters on a canal or bayfront lot, and "
        "the island's current watering order gives turf one less thing to schedule around."
    ),
    "sections": [
        (
            "Why the waterbody setback matters more here than inland",
            "<p>DEP's own installation rule, effective May 19, 2026, pairs the turf material spec, natural infill over a washed "
            "base, with a hard line near open water: nothing closer than 10 feet to a waterbody unless a seawall stands between "
            "the lawn and the water " + src("dep-rule", "DEP Rule 62-308.100") + " " + src("fs125572", "F.S. §125.572") + ". "
            "Siesta Key is mostly shoreline, canal frontage on one side of the island or the next, Roberts Bay on another, so "
            "that 10-foot line decides the turf's actual footprint on far more lots here than it would on an inland Orlando-area "
            "yard where the nearest open water might be a retention pond nobody built next to on purpose.</p>"
        ),
        (
            "What the current watering order leaves out of turf's upkeep",
            "<p>Sarasota County sits inside the Southwest Florida Water Management District's current shortage order, which "
            "limits irrigation countywide to one scheduled day a week in an overnight window " + src("swfwmd-restrictions") +
            ". New sod still has to live inside that calendar after a short initial grace period, but a finished turf lawn drops "
            "irrigation from its upkeep list entirely, a detail that carries real weight on a storm-recovery yard where the sod "
            "was already replaced once after the 2024 hurricanes and homeowners would rather not do it again.</p>"
        ),
    ],
    "scenario": (
        "Picture a 280 sq ft turf strip replacing storm-damaged sod along a canal-front side yard",
        "<p>Picture a 280 sq ft turf strip replacing storm-damaged sod along a canal-front side yard. Pricing it at " +
        price("artificial-turf") + " per sq ft runs $2,800 to $7,000, and a job that lands inside the typical " +
        price("artificial-turf", typical=True) + " range settles closer to $3,360 to $5,040. The canal frontage is what drives "
        "the layout here: the turf stops 10 feet short of the waterline unless an existing seawall already stands between the "
        "yard and the water, and the irrigation line that used to feed the old sod gets capped rather than extended into the "
        "new turf footprint.</p>"
    ),
    "faqs": [
        faq(
            "How close to the water can I install turf on a Siesta Key canal lot?",
            "At least 10 feet back from the waterline, under Florida's statewide turf rule, unless a seawall already separates the lawn from the water. That's in addition to whatever setback the county's own zoning code requires."
        ),
        faq(
            "Does turf help with the current water-shortage order on Siesta Key?",
            "Yes. The island is under SWFWMD's countywide order limiting irrigation to one day a week, a schedule new sod still has to follow after a short grace period, while a finished turf lawn has nothing left to irrigate."
        ),
        faq(
            "Can I run a sprinkler zone to a new turf area?",
            "No. The state's turf standard bars in-ground irrigation run to the turf itself, a separate requirement from the waterbody setback and from any watering-day restriction on the rest of the yard."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
