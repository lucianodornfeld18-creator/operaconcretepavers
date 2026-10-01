# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "nokomis"

CENSUS_NOKOMIS_URL = "http://censusreporter.org/profiles/16000US1248875-nokomis-fl/"
WIKI_NOKOMIS_URL = "https://en.wikipedia.org/wiki/Nokomis,_Florida"
WIKI_CASEYKEY_URL = "https://en.wikipedia.org/wiki/Casey_Key,_Florida"
WIKI_PAVILION_URL = "https://en.wikipedia.org/wiki/Nokomis_Beach_Pavilion"
VSC_BEACH_URL = "https://www.visitsarasota.com/beaches-parks/nokomis-beach"

SRC = [
    "sarasota-county-row-permit", "sarasota-county-98-3-culvert-row-fees", "sarasota-county-124-255-culverts",
    "sarasota-county-124-76-rsf-standards", "sarasota-county-124-283-nonconforming-isr", "sarasota-county-22-63-retaining-walls",
    "sarasota-county-54-723-gbsl", "sarasota-county-online-permitting", "sarasota-county-building-page",
    "fdep-cccl-program", "fdep-cccl-apply", "fema-coastal-firm", "swfwmd-restrictions", "fdot-sdg", "fl-senate-2011-104",
    "nrcs-eaugallie-osd", "nrcs-immokalee-osd", "nrcs-felda-osd", "dep-rule", "fs125572", "fs720-3045",
    ("Census Reporter, Nokomis CDP, FL (ACS 2020-2024 5-yr, B01003/B25035)", CENSUS_NOKOMIS_URL),
    ("Wikipedia, Nokomis, Florida", WIKI_NOKOMIS_URL),
    ("Wikipedia, Casey Key, Florida", WIKI_CASEYKEY_URL),
    ("Wikipedia, Nokomis Beach Pavilion", WIKI_PAVILION_URL),
    ("Visit Sarasota County, Nokomis Beach", VSC_BEACH_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Who reviews a driveway or patio permit in Nokomis: a city hall or the county?",
        "<p>Nokomis has no city hall of its own to call. It's an unincorporated community, so Sarasota County's Building Division takes every application a homeowner here would file, from a fresh "
        + cs("nokomis", "concrete-driveways", "driveway pour") + " to a backyard " + cs("nokomis", "paver-patios", "paver patio") + ". The county's land development code spells out that distinction "
        "plainly: a Right-of-Way Use Permit covers 'all work within the County right-of-way,' full stop, with no carve-out for a town that lacks its own charter " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") +
        ". Applications route through the county's own online system rather than a storefront counter " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") + ", and the county's building page, "
        "reachable only through a cached search summary at the time this was checked, suggests a driveway repaired without touching the culvert may skip that review step entirely " + src("sarasota-county-building-page", "Sarasota County Building") + ", a point worth confirming by phone before assuming it.</p>"
    ),
    sec(
        "What does the county's culvert rule actually require before a driveway gets poured?",
        "<p>Nearly every Nokomis lot still drains to an open roadside ditch rather than a storm sewer, which is why the county treats the pipe under a driveway as its own permit category, separate from "
        "the slab or pavers going on top of it " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ".</p>"
        + table(
            "Sarasota County culvert specs for a residential driveway, §124-255",
            ["Item", "Requirement"],
            [
                ["Pipe length", "20 ft minimum, 24 ft maximum (longer where the ditch runs deeper)"],
                ["Pipe material", "Reinforced or asphalt-coated corrugated metal, or another type the County Engineer approves"],
                ["Grade and size", "Set by the County Engineer before the driveway is formed"],
                ["Drainage easement", "No walkway, driveway or paved surface may sit inside one"],
            ],
            "Source: Sarasota County Code §124-255, checked October 2026 " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + "."
        )
    ),
    sec(
        "Does a bigger patio or pool deck push a Nokomis lot past its coverage limit?",
        "<p>It depends which number the county is measuring. The RSF districts that cover most of Nokomis cap *building* coverage at 35 percent of the lot, a figure that governs the house footprint, not "
        "the driveway or patio beside it " + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ". Older RMF-zoned parcels recorded on or before November 11, 1975, a plat date that catches "
        "plenty of Nokomis's original mid-century lots, answer to a separate ceiling instead: 50 percent impervious coverage, counting 'roof structures, swimming pools and pool decks, as well as concrete, asphalt, "
        "pavers,' while grass, shell and other water-permeable surfaces don't count against it " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") + ". " + svc("concrete-pool-decks", "A concrete pool deck") +
        " addition on one of those older platted lots is worth checking against that 1975 cutoff before the forms go up, since it can decide whether the project needs a variance first.</p>"
    ),
    sec(
        "What does a Casey Key or waterfront address near Nokomis change about the permit?",
        "<p>Casey Key, the narrow barrier island that carries much of Nokomis's Gulf-front mail, sits northwest of the mainland CDP across Blackburn Bay " + ext(WIKI_CASEYKEY_URL, "Wikipedia, Casey Key, Florida") + ", and "
        "the 2024 hurricane season, Helene and Milton both, left visible damage along it that's still shaping rebuild decisions today " + ext(WIKI_CASEYKEY_URL, "Wikipedia, Casey Key, Florida") + ". Any construction or excavation seaward of the county's own Gulf "
        "Beach Setback Line is barred outright absent a coastal setback variance, a county rule that sits on top of, not instead of, Florida DEP's separate Coastal Construction Control Line permit "
        + src("sarasota-county-54-723-gbsl", "Sarasota County Code §54-723") + " " + src("fdep-cccl-program", "FDEP's CCCL program") + ". FEMA's own coastal flood categories split a Key address further still, between the roughly "
        "one-percent-chance Zone AE and the surf-exposed Coastal High Hazard Zone VE " + src("fema-coastal-firm", "FEMA's coastal flood-map guidance") + ", a split worth pulling up by address before " + svc("retaining-walls", "a retaining wall") +
        " or a low deck edge gets its final elevation set.</p>"
    ),
    sec(
        "How do Dona Bay, Shakett Creek and Nokomis Beach fit into the local picture?",
        "<p>The Legacy Trail's roughly 2.5-mile stretch through Nokomis crosses open water at the Shakett Creek bridge, right where that creek empties into Dona Bay on its way to the Gulf "
        + ext(WIKI_NOKOMIS_URL, "Wikipedia, Nokomis, Florida") + ", and that bay-and-creek system is the drainage every swale and culvert permit in town ultimately answers to. Down at the coast, Nokomis Beach carries a "
        "title no other county shoreline can claim: Sarasota County's oldest public beach " + ext(VSC_BEACH_URL, "Visit Sarasota County") + ", with a 1954 pavilion by Sarasota School of Architecture figure Jack West that "
        "earned a spot on the National Register of Historic Places on May 28, 2013 " + ext(WIKI_PAVILION_URL, "Wikipedia, Nokomis Beach Pavilion") + ". None of that history changes a permit application, but it's part of "
        "why so much of the work here is resurfacing and " + svc("paver-sealing", "paver restoration") + " on a mid-century lot rather than a first pour on raw ground: Census figures put Nokomis's median home "
        "construction year at 1978 against a population estimated at 3,452 " + ext(CENSUS_NOKOMIS_URL, "Census Reporter, Nokomis CDP") + ".</p>"
    ),
    sec(
        "What do Nokomis's flatwoods soils mean for a slab, and when does a wall need an engineer?",
        "<p>EauGallie, Immokalee and Felda, the sandy flatwoods series common around Nokomis, all hold a seasonal high water table within about a foot and a half of the surface for part of most "
        "years " + src("nrcs-eaugallie-osd", "NRCS OSD EauGallie") + " " + src("nrcs-immokalee-osd", "NRCS OSD Immokalee") + " " + src("nrcs-felda-osd", "NRCS OSD Felda") + ", a condition the base under "
        "a driveway or patio has to be built up and drained around rather than ignored. Separately, a wall taller than 4 feet, with height taken from grade at whichever point along the run "
        "sits highest, triggers the county's engineered-drawing requirement under its pool-code amendment before a single block gets set " + src("sarasota-county-22-63-retaining-walls", "Sarasota County Code §22-63") + ", a threshold that "
        "comes up often on a canal or bay lot where fill has to be held back from the water. Sarasota County, notably, isn't among the counties the state flagged for the heaviest sinkhole "
        "insurance claims in its own 2010 review " + src("fl-senate-2011-104", "Florida Senate Interim Report 2011-104") + ", so settlement here traces back to that same shallow water table far more often than to karst.</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Does Nokomis have its own building department?",
        "No. Nokomis is an unincorporated Sarasota County community, so the County's Building Division and its online permitting portal review every driveway, patio, pool-deck and wall permit here rather than a city hall counter."
    ),
    faq(
        "Does a Nokomis driveway need a separate culvert permit?",
        "In most cases, yes, since the lot's roadside swale carries a culvert that the county reviews apart from the driveway surface itself, setting the pipe's length, material and grade under its own code."
    ),
    faq(
        "Is my Nokomis or Casey Key lot affected by the Gulf Beach Setback Line?",
        "Only if it sits on or near Casey Key or another county Gulf beach. The county's own setback line bars construction or excavation seaward of it without a variance, on top of whatever Florida DEP's separate coastal control line permit requires."
    ),
    faq(
        "How do you pick the best concrete contractor for a Nokomis address?",
        "Start with the state's license-lookup tool, then ask directly whether the bid accounts for a county culvert permit and the shallow water table in EauGallie or Immokalee soil rather than quoting a flat number used anywhere in Florida. " +
        post("how-to-choose-a-concrete-contractor-sarasota", "Our contractor guide") + " covers the rest."
    ),
    faq(
        "Does the current watering restriction change sod or turf plans in Nokomis?",
        "Yes. Sarasota County sits entirely inside SWFWMD's Modified Phase III shortage order, running through March 31, 2027, which limits irrigation to one assigned day a week. New sod gets a short daily-watering runway first; artificial turf answers to no watering schedule at all once it's down."
    ),
]

HUB = page(
    "/nokomis-fl/", "city",
    "Concrete, Paver & Turf Contractor in Nokomis, FL",
    "Concrete, pavers and turf for unincorporated Nokomis, FL: Sarasota County's culvert and ROW permits, Casey Key's setback line and flatwoods soil, October 2026.",
    "Concrete Driveways, Pavers and Turf Serving Nokomis",
    capsule(
        "Nokomis is an unincorporated Sarasota County community of about 3,452 residents stretched along Dona Bay, with Casey Key as its Gulf-front address. As of October 2026, the county's Building "
        "Division, not a city hall, reviews any driveway, patio or pool-deck project here, and a culvert crossing the roadside swale needs its own right-of-way permit before the apron gets poured."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Nokomis",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/sarasota-county-driveway-patio-permits/", "Driveway and patio permits in Sarasota, Venice and North Port"),
        ("/osprey-fl/", "Concrete, pavers and turf in Osprey"),
        ("/venice-fl/", "Concrete, pavers and turf in Venice"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Nokomis, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Nokomis, FL – Culvert Permit",
    "meta": "Concrete driveway installers in Nokomis, FL: Sarasota County's §124-255 culvert rule and 20-24 ft pipe length, market range " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
    "h1": "Pouring a Concrete Driveway in Unincorporated Nokomis",
    "lede": capsule(
        "A concrete driveway in Nokomis costs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026. With no city hall of its own, Nokomis routes every driveway "
        "application to Sarasota County's Building Division, and where the drive crosses the roadside swale, a culvert permit comes first, set apart from the slab itself."
    ),
    "sections": [
        (
            "Why the swale, not the slab, gets reviewed first",
            "<p>Sarasota County treats the pipe under a Nokomis driveway as its own permit category: the culvert has to run 20 feet at minimum and no more than 24 feet unless the ditch runs "
            "deeper, built from reinforced or asphalt-coated corrugated metal or another material the County Engineer signs off on " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") +
            ". The county sets the pipe's grade and size before forms for the slab ever go up, and a driveway, walkway or other paved surface is barred outright from sitting inside a drainage "
            "easement on the same lot " + src("sarasota-county-124-255-culverts") + ".</p>"
        ),
        (
            "Where the application actually goes",
            "<p>There's no Nokomis building counter to walk into; the county's own online system is the only filing route, the same portal that handles a Right-of-Way Use Permit for any other work "
            "placed in the county right-of-way " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") + " " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ". A straight "
            "driveway repair that leaves the culvert untouched may clear that review faster, a distinction the county's own building guidance draws, though we confirm it by phone on each job rather than assume it " +
            src("sarasota-county-building-page", "Sarasota County Building") + ".</p>"
        ),
    ],
    "scenario": (
        "Replacing a two-car driveway on an older Nokomis lot, worked out in square feet",
        "<p>Picture a 22 by 24 foot driveway, 528 square feet, on a lot platted back in the 1970s where the original culvert pipe has started to collapse under the swale. At " +
        price("concrete-driveway") + " per " + per("concrete-driveway") + ", the pour itself runs $3,168 to $7,920, tightening to roughly $4,224 to $6,336 inside the typical " + price("concrete-driveway", typical=True) +
        " band. Because the old pipe needs replacing anyway, the project picks up a fresh culvert permit alongside the driveway permit, with the County Engineer setting the new pipe's grade before "
        "either one gets poured.</p>"
    ),
    "faqs": [
        faq(
            "How long does a residential culvert pipe have to be in Nokomis?",
            "Sarasota County's code sets a 20-foot minimum and a 24-foot maximum, with more length allowed only where the roadside ditch itself runs deeper than the standard section."
        ),
        faq(
            "Can a driveway sit inside a drainage easement in Nokomis?",
            "No. County code bars any paved surface, walkway included, from being located inside a drainage easement, regardless of how the rest of the driveway is laid out."
        ),
        faq(
            "Does every Nokomis driveway repair need a new culvert permit?",
            "Not necessarily. A repair that doesn't disturb the culvert pipe itself may not trigger that review, though confirming with the county's Building Division before starting avoids a stop-work surprise."
        ),
    ],
    "sources": SRC,
}

# 2. paver-driveways -----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Nokomis, FL – County ROW Rules",
    "meta": "Paver driveway installers in Nokomis, FL: the same culvert and right-of-way review the county applies to a concrete pour; range " + price("paver-driveway") + " per " + per("paver-driveway") + ".",
    "h1": "Paver Driveway Installation Near Nokomis",
    "lede": capsule(
        "A paver driveway near Nokomis runs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026. The surface material doesn't change which county office reviews "
        "the job: a Right-of-Way Use Permit and, where the swale is crossed, a culvert permit both apply the same way they would to a poured slab."
    ),
    "sections": [
        (
            "The county doesn't distinguish pavers from concrete at the permit desk",
            "<p>Sarasota County's rule covering work in its rights-of-way names 'all work,' with no separate track for a paver surface over a poured one " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") +
            ". That means a paver driveway crossing the roadside swale still needs its own culvert permit, pipe length and grade set the same way under §124-255 " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") +
            ", before the base for the pavers goes down.</p>"
        ),
        (
            "Where pavers help on an older, tighter lot",
            "<p>On a Nokomis parcel platted before November 11, 1975, the county's nonconforming-lot rule caps impervious coverage, driveway pavers included, at 50 percent, while it specifically excludes grass, "
            "shell or another water-permeable surface from that count " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") + ". A homeowner widening " + svc("paver-driveways", "a paver driveway") +
            " toward that ceiling sometimes trims a planting strip to shell or another pervious material instead of adding solid pavers across the entire apron.</p>"
        ),
    ],
    "scenario": (
        "Relaying a driveway in pavers on a bay-side Nokomis lot, worked out in square feet",
        "<p>Take a 20 by 26 foot paver driveway, 520 square feet, planned for a lot close enough to Dona Bay that the original slab's culvert crossing is being rebuilt at the same time. "
        "At " + price("paver-driveway") + " per " + per("paver-driveway") + ", that puts the job between $5,200 and $15,600, landing near $6,240 to $10,400 inside the typical " + price("paver-driveway", typical=True) +
        " range once the paver grade is chosen. The culvert work underneath gets its own line-and-grade sign-off from the County Engineer before the base for the pavers is compacted on top.</p>"
    ),
    "faqs": [
        faq(
            "Does a paver driveway skip the county's culvert permit in Nokomis?",
            "No. The permit covers the pipe under the swale crossing regardless of what surface material sits above it, so pavers go through the same §124-255 review a poured driveway would."
        ),
        faq(
            "Can shell count toward a lot's coverage limit instead of pavers?",
            "On an older, nonconforming lot under the county's 1975 cutoff, yes; shell and other water-permeable surfaces are specifically excluded from the 50 percent impervious-coverage count that catches solid pavers."
        ),
        faq(
            "Is there a separate right-of-way rule for pavers versus concrete in Nokomis?",
            "No. The county's Right-of-Way Use Permit requirement names all work in the right-of-way without singling out a surface material, so pavers and concrete both answer to the same review."
        ),
    ],
    "sources": SRC,
}

# 3. concrete-patios -------------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Nokomis, FL – Coverage Limits",
    "meta": "Concrete patio contractors in Nokomis, FL: the county's 35% building cap versus the 50% impervious limit on pre-1975 lots; market range " + price("concrete-patio") + " per " + per("concrete-patio") + ".",
    "h1": "Building a Concrete Patio in Nokomis",
    "lede": capsule(
        "A concrete patio near Nokomis costs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. Which coverage limit the county applies depends on when the "
        "lot was platted, so a 1970s subdivision parcel and a newer one down the street can face two different ceilings on the same size addition."
    ),
    "sections": [
        (
            "Two different coverage numbers, depending on the plat date",
            "<p>Sarasota County's RSF districts, which cover most of Nokomis, cap the house itself at 35 percent building coverage, a rule aimed at the structure rather than the patio beside it " +
            src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ". A lot recorded on or before November 11, 1975 under the older RMF designation instead faces a 50 percent impervious "
            "ceiling that explicitly counts pool decks and paved patios, concrete included, while leaving grass and shell out of the tally " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") +
            ". Checking the plat date before pricing a patio addition is the difference between a routine permit and a variance application.</p>"
        ),
        (
            "The permit question the county's own page leaves open",
            "<p>A search summary of the county's building page suggests an on-grade patio without footings may not need a standalone permit, though the page itself returned an access error when checked "
            "directly, so that point gets confirmed with the Building Division rather than assumed from a secondary source " + src("sarasota-county-building-page", "Sarasota County Building") + ". " + svc("concrete-pool-decks", "A pool deck") +
            " addition on the same lot follows that identical confirm-first approach.</p>"
        ),
    ],
    "scenario": (
        "A lanai-adjacent patio on a pre-1975 Nokomis lot, worked out in square feet",
        "<p>Consider a 16 by 18 foot patio, 288 square feet, added off a screened lanai on a lot platted in the 1960s, old enough to fall under the county's nonconforming RMF coverage rule "
        "rather than the newer RSF standard. At " + price("concrete-patio") + " per " + per("concrete-patio") + ", the job runs $1,728 to $3,744, or about $2,016 to $2,880 inside the typical " +
        price("concrete-patio", typical=True) + " range for a broom finish. Before pricing it, the lot's existing impervious total against that 50 percent ceiling gets checked, since the pool and deck "
        "already on the property count toward it the same way the new patio would.</p>"
    ),
    "faqs": [
        faq(
            "Which coverage rule applies to my Nokomis patio, 35% or 50%?",
            "It depends on the plat date. Lots recorded on or before November 11, 1975 fall under the county's 50 percent impervious-coverage rule for nonconforming RMF parcels; newer RSF lots instead cap building coverage, not paving, at 35 percent."
        ),
        faq(
            "Does a Nokomis patio on grade need a building permit?",
            "A secondary summary of county guidance suggests an on-grade patio without footings may be exempt, but since the county's own page couldn't be confirmed directly, we check with the Building Division before pricing a job as permit-free."
        ),
        faq(
            "Does grass or shell count against my lot's coverage limit?",
            "No, under the county's nonconforming-lot rule. Grass, shell and other surfaces that let water penetrate are specifically excluded from the 50 percent impervious-coverage calculation that catches concrete, pavers and asphalt."
        ),
    ],
    "sources": SRC,
}

# 4. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Nokomis, FL – Flatwoods Soil Base",
    "meta": "Paver patio installers near Nokomis, FL: building the base over EauGallie and Immokalee flatwoods soil; market range " + price("paver-patio") + " per " + per("paver-patio") + ", Oct. 2026.",
    "h1": "Paver Patios and Walkways Near Nokomis",
    "lede": capsule(
        "A paver patio near Nokomis runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. Most lots here sit on sandy flatwoods soil that stays damp near grade for "
        "a stretch of the year, a condition that decides how thick the compacted aggregate under the pavers needs to be before any joint sand goes down."
    ),
    "sections": [
        (
            "Why the base runs deeper here than on a ridge lot",
            "<p>EauGallie and Immokalee, two of the sandy flatwoods series common around Nokomis, both stay saturated close to grade for a stretch of most years, the kind of ground ICPI flags as "
            "needing a thicker build-up " + src("nrcs-eaugallie-osd", "NRCS OSD EauGallie") + " " + src("nrcs-immokalee-osd", "NRCS OSD Immokalee") + ". Its own guidance adds 2 to 4 extra inches of aggregate "
            "on soils that stay wet or weak, stacked on top of the roughly 4-inch minimum it sets for a patio subgrade that drains well on its own, a spec that applies directly here.</p>"
        ),
        (
            "A path to the water still answers to the county's easement rule",
            "<p>A paver walkway staying entirely on private ground skips the right-of-way review, but one crossing toward a canal, bay frontage or the street falls under the same permit a driveway "
            "apron needs " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ", and no paved path may sit inside a drainage easement regardless of where it leads " +
            src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ". " + svc("concrete-walkways", "A concrete version") + " of the same path answers to the identical easement check.</p>"
        ),
    ],
    "scenario": (
        "A paver patio over EauGallie soil on a shaded Nokomis lot, worked out in square feet",
        "<p>Say a 260 square foot paver patio goes in off the back of a 1970s Nokomis home sitting on EauGallie fine sand, close enough to the water table that the base gets built up an "
        "extra few inches past the standard spec. At " + price("paver-patio") + " per " + per("paver-patio") + ", the job comes to $2,600 and $4,420, narrowing to roughly $3,120 to $4,160 inside the "
        "typical " + price("paver-patio", typical=True) + " band. The thicker base adds modestly to the labor time but not materially to the paver cost itself, since the extra depth is aggregate, not stone.</p>"
    ),
    "faqs": [
        faq(
            "Does a Nokomis paver patio need a deeper base than normal?",
            "Often, yes, on EauGallie or Immokalee soil, since both hold a seasonal high water table close to the surface, and industry guidance calls for 2 to 4 inches of extra compacted base on wet or weak ground."
        ),
        faq(
            "Can a paver path run across a Nokomis drainage easement?",
            "No. County code bars any paved surface, a walkway included, from being placed inside a drainage easement, no matter where the path is headed."
        ),
        faq(
            "Does a paver patio need the same permit as a driveway in Nokomis?",
            "Only the portion crossing into the county right-of-way does. A patio or walkway that stays fully on private ground doesn't trigger the Right-of-Way Use Permit a driveway apron requires."
        ),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Nokomis, FL – Flood Zones",
    "meta": "Concrete pool deck builders in Nokomis, FL: FEMA Zone AE/VE near Casey Key and the nonconforming-lot coverage rule; range " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ".",
    "h1": "Concrete Pool Deck Installation in Nokomis",
    "lede": capsule(
        "A concrete pool deck in Nokomis runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. Lots on Casey Key or along Dona Bay carry a FEMA flood "
        "designation that an inland Nokomis address doesn't, and the deck itself can count toward a tighter coverage limit on an older, nonconforming parcel."
    ),
    "sections": [
        (
            "Checking the flood category before the deck's elevation is set",
            "<p>A Casey Key or bay-front lot falls into one of two FEMA coastal categories: Zone AE, with roughly a one-percent annual flood chance and modest wave action, or the Coastal High Hazard "
            "Zone VE, where storm surf can punch through an unprotected deck edge " + src("fema-coastal-firm", "FEMA's coastal flood-map guidance") + ". A deck reaching toward Casey Key's Gulf side also runs into "
            "the county's own Gulf Beach Setback Line, a construction bar that sits on top of Florida DEP's separate CCCL permit rather than replacing it " + src("sarasota-county-54-723-gbsl", "Sarasota County Code §54-723") +
            " " + src("fdep-cccl-apply", "FDEP's CCCL application page") + ".</p>"
        ),
        (
            "Why the deck's footprint matters more on an older lot",
            "<p>On a Nokomis parcel platted on or before November 11, 1975, the county's own nonconforming rule names pool decks directly among the paved surfaces that count toward a 50 percent "
            "impervious ceiling " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") + ", a sharper limit than the 35 percent *building*-only cap that governs newer RSF lots "
            + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ". " + svc("pool-deck-pavers", "A paver overlay") + " on that same older lot counts the same way toward the total.</p>"
        ),
    ],
    "scenario": (
        "A pool deck pour on a Dona Bay lot, worked out in square feet",
        "<p>Imagine a 620 square foot pool deck around a screened cage on a lot close enough to Dona Bay to land inside FEMA's Zone AE on the current flood map. Pricing it at " +
        price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " comes to $3,100 and $9,300, tightening toward $4,340 to $7,440 inside the typical " + price("concrete-pool-deck", typical=True) +
        " range for a slip-resistant texture pitched to the yard drain. Because the lot sits in a mapped flood zone, the deck's finished height gets set against the base-flood elevation rather than "
        "an inland guess, and if the parcel predates 1975, the new square footage also gets checked against the nonconforming coverage ceiling.</p>"
    ),
    "faqs": [
        faq(
            "Is my Nokomis or Casey Key pool deck lot in a flood zone?",
            "Possibly, especially on Casey Key or along Dona Bay. FEMA's map viewer shows whether an address falls into Zone AE or the higher-hazard Zone VE, and the line can split a single street."
        ),
        faq(
            "Does a Nokomis pool deck need a state permit as well as a county one?",
            "Only if it reaches seaward of Florida's Coastal Construction Control Line, which mainly affects Casey Key's Gulf side. Most bay-front and inland Nokomis lots don't cross that line."
        ),
        faq(
            "Does a pool deck count toward my Nokomis lot's coverage limit?",
            "On a lot platted on or before November 11, 1975, yes, directly, under the county's 50 percent impervious-coverage rule. Newer RSF lots instead cap building coverage, which a deck doesn't touch."
        ),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ----------------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Nokomis, FL – Salt Air",
    "meta": "Pool deck pavers and travertine near Nokomis, FL: FDOT's marine-environment chloride threshold off Casey Key and Dona Bay; range " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ".",
    "h1": "Travertine and Paver Pool Decks Near Nokomis",
    "lede": capsule(
        "Travertine or paver pool decks near Nokomis price out at " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " this October. How far a backyard sits from Casey Key's "
        "shoreline or Dona Bay matters more to how soon a sealed surface shows salt staining than which stone gets chosen."
    ),
    "sections": [
        (
            "How close is close enough for salt to matter",
            "<p>Bridge engineers at FDOT draw their own marine-environment line at 2,500 feet from any chloride-heavy waterway, a chemistry test rather than a distance anyone eyeballs from the yard "
            + src("fdot-sdg") + ", and that line sweeps in essentially every lot on Casey Key plus a good share of those backing to Dona Bay or Roberts Bay on the mainland side of Nokomis. That "
            "exposure doesn't change the paver base spec underneath, but it shortens how long joint sand and a sealer coat hold up against an inland overlay built the same way.</p>"
        ),
        (
            "Two separate lines can both run through a Casey Key backyard",
            "<p>Sarasota County's own Gulf Beach Setback Line prohibits construction or excavation seaward of it, or waterward of the Barrier Island Pass Hazard Line, anywhere on Casey Key, independent "
            "of whatever Florida's own coastal program requires " + src("sarasota-county-54-723-gbsl", "Sarasota County Code §54-723") + ". A homeowner stretching a travertine overlay toward the Gulf can "
            "find the county line and the state's own control line falling in two different spots on the same lot, which is why pinning down both before quoting a square-foot number matters more "
            "here than it would a mile inland " + src("fdep-cccl-apply", "FDEP's CCCL application page") + ". " + svc("concrete-pool-decks", "A plain concrete deck") + " expansion on the same parcel runs "
            "into both lines identically.</p>"
        ),
    ],
    "scenario": (
        "Resurfacing a Casey Key deck in travertine where two setback lines cross the yard",
        "<p>A Casey Key cottage has a tired 540 square foot broom-finish deck ringing its cage, and the owner wants travertine instead, except a corner of that deck sits past the county's own "
        "Gulf Beach Setback Line. Pricing the resurface at " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " puts the job at $6,480 to $16,200, narrowing to about $7,560 to "
        "$11,880 inside the typical " + price("pool-deck-pavers", typical=True) + " band once stone and pattern are chosen. The corner past the setback line either gets redesigned around that "
        "boundary or goes through a county variance first, and either way, the sealer spec on the rest of the deck still answers to how close the whole lot sits to open saltwater.</p>"
    ),
    "faqs": [
        faq(
            "Why does a Casey Key pool deck need a tighter sealing schedule?",
            "Nearly the entire key falls inside FDOT's own marine-chloride boundary, water above 2,000 parts per million within 2,500 feet, and that level of salt exposure wears through joint sand and a sealer coat faster than an inland Nokomis yard sees."
        ),
        faq(
            "Can the Gulf Beach Setback Line cut through the middle of a Casey Key deck?",
            "On a narrow lot, yes. The county's own line and Florida's separate coastal control line don't always fall in the same spot, so a deck redesign or overlay near the Gulf side gets both checked against the actual survey before pricing."
        ),
        faq(
            "Is a travertine deck worth the added cost this close to the water on Casey Key?",
            "Plenty of owners near the Gulf pick it for the lighter surface and look, though no verified temperature figure separates it from a concrete paver deck, so the choice tends to come down to upkeep and appearance rather than a specific degree claim."
        ),
    ],
    "sources": SRC,
}

# 7. stamped-concrete -------------------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Nokomis, FL – 1970s Lots",
    "meta": "Stamped concrete contractors in Nokomis, FL: pattern choices on the area's mid-century platted lots; market range " + price("stamped-concrete") + " per " + per("stamped-concrete") + ", Oct. 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Nokomis",
    "lede": capsule(
        "Stamped concrete in Nokomis runs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October 2026. With the area's median home dated to 1978, stamped work here "
        "is as often a resurfacing choice over a tired original slab as it is a feature on a brand-new pour."
    ),
    "sections": [
        (
            "Why a 1978-median town leans toward overlay work",
            "<p>Census figures put Nokomis's median year of construction at 1978 against a current population near 3,452 " + ext(CENSUS_NOKOMIS_URL, "Census Reporter, Nokomis CDP") + ", meaning a sizeable share "
            "of the area's original driveways and entry walks are approaching fifty years old. A stamped overlay over a sound but worn slab is a common way to refresh that kind of driveway without "
            "a full tear-out, provided the base beneath hasn't failed structurally.</p>"
        ),
        (
            "Stamped work doesn't change the culvert or easement review",
            "<p>A stamped driveway crossing into the county right-of-way still needs the same Right-of-Way Use Permit a plain pour requires " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") +
            ", and where a swale crossing is part of the job, the culvert permit under §124-255 applies regardless of the finish chosen on top " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") +
            ". " + svc("concrete-driveways", "A plain concrete driveway") + " on the same lot answers to that identical pair of reviews.</p>"
        ),
    ],
    "scenario": (
        "A stamped entry walk replacing a cracked 1970s path, worked out in square feet",
        "<p>Here's a 220 square foot stamped-concrete entry walk and small landing replacing a cracked original path on a Nokomis lot dating to the mid-1970s. At " + price("stamped-concrete") +
        " per " + per("stamped-concrete") + ", that project prices between $1,760 and $4,180, settling closer to $2,640 to $3,520 inside the typical " + price("stamped-concrete", typical=True) +
        " range once the pattern and color count are chosen. A muted ashlar or slate pattern tends to suit the scale of a mid-century home here better than a bright multi-tone cobble built for "
        "a newer subdivision facade.</p>"
    ),
    "faqs": [
        faq(
            "Is stamped concrete common on older Nokomis driveways?",
            "It's a frequent resurfacing choice, given how much of the area's housing dates to the late 1970s, where an overlay refreshes a worn but structurally sound original slab without a full replacement."
        ),
        faq(
            "Does a stamped driveway skip Nokomis's culvert permit?",
            "No. The culvert review covers the drainage pipe under a swale crossing regardless of the finish on top, so a stamped driveway follows the same §124-255 process a plain pour would."
        ),
        faq(
            "What stamped pattern suits a mid-century Nokomis home?",
            "A single-color slate or ashlar pattern tends to read more in scale with a 1970s-era house than a busy, multi-tone cobble pattern built for a larger, newer subdivision facade."
        ),
    ],
    "sources": SRC,
}

# 8. artificial-turf --------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Nokomis, FL – Water Buffer Rule",
    "meta": "Artificial turf installers in Nokomis, FL: the state's 10-foot water-buffer rule near Dona Bay and canal lots; market range " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
    "h1": "Artificial Turf for Nokomis Yards",
    "lede": capsule(
        "Turf installers quote " + price("artificial-turf") + " per " + per("artificial-turf") + " for a Nokomis yard this October. A homeowner tired of re-sodding a lawn backing to Dona Bay or a "
        "residential canal still has to clear the state's water-setback line before the layout gets drawn, a step an inland subdivision lot never has to think about."
    ),
    "sections": [
        (
            "The buffer distance that bay and canal lots can't skip",
            "<p>DEP Rule 62-308.100 took effect May 19, 2026, and it conditions any synthetic lawn on a washed-rock base, natural infill, no irrigation line running underneath, and a minimum 10 "
            "feet of open space back from a waterbody's edge, unless the property line is a seawall " + src("dep-rule", "DEP Rule 62-308.100") + ". A shoreline lot along Dona Bay, Roberts Bay or one "
            "of the canal spurs threading through Nokomis is exactly where measuring that gap on the actual survey, rather than guessing from the fence line, keeps the install from needing a redesign "
            "midway through. The rule sets a statewide floor that no local ordinance may tighten on a single-family lot " + src("fs125572", "F.S. 125.572") + ".</p>"
        ),
        (
            "A thirsty 1978-median lawn versus a turf lawn under Phase III",
            "<p>Sarasota County is locked into SWFWMD's Modified Phase III shortage order through March 31, 2027, cutting sprinkler use to one assigned day a week during an overnight or late-night "
            "window only " + src("swfwmd-restrictions", "SWFWMD district restrictions") + ". On a Nokomis lot whose sod dates back decades, that single weekly slot is rarely enough to keep bare or "
            "thinning patches from spreading further, which is part of why turf comes up so often on an older lawn here rather than a fresh re-sod attempt. Once installed, turf answers to no sprinkler "
            "day at all, and a yard shielded from street view carries the HOA protection F.S. 720.3045 extends as of 2026 " + src("fs720-3045", "F.S. 720.3045") + ".</p>"
        ),
    ],
    "scenario": (
        "Swapping a failing bay-front lawn for turf, worked out in square feet",
        "<p>A homeowner on a Dona Bay canal spur is down to patchy, half-dead sod after a summer on the county's one-day watering window, and wants 460 square feet of front and side yard "
        "converted instead, measured out to sit a full 18 feet back from the seawall line. At " + price("artificial-turf") + " per sq ft, the full range runs $4,600 to $11,500, with most "
        "comparable jobs landing in the typical " + price("artificial-turf", typical=True) + " band, near $5,520 to $8,280, once backing weight and pile height are picked. Eighteen feet clears "
        "the state's 10-foot floor comfortably, so the layout goes forward without a variance, and the washed-rock base underneath gets specified exactly as it would three streets inland.</p>"
    ),
    "faqs": [
        faq(
            "Why do so many Nokomis turf quotes mention a water-setback check?",
            "Because a large share of residential lots here front Dona Bay, Roberts Bay or a canal spur, and the state's own turf rule requires at least 10 feet of clearance from open water before the layout can be finalized."
        ),
        faq(
            "Is turf a common fix for a struggling older Nokomis lawn?",
            "Often, yes. With sprinkler use capped at one day a week under the county's current shortage order, a lawn that's already thinning rarely recovers on that schedule, which pushes plenty of homeowners toward turf instead of a fresh re-sod."
        ),
        faq(
            "What happens if a planned turf layout falls inside the 10-foot buffer?",
            "The layout gets pulled back from the water's edge to clear that distance, unless a seawall already forms the property line there, in which case the buffer condition doesn't apply at all."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
