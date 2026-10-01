# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, svc, city, cs, post, compare, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "palmetto"

SRC = [
    "palmetto-code-25-2-row-permit",
    "palmetto-row-permit-form",
    "palmetto-building-department",
    "palmetto-code-10-46-retaining-wall-permit",
    "palmetto-code-29-207-stormwater-fee",
    "manatee-phase3",
    "swfwmd-restrictions",
    "fema-coastal-firm",
    "fdot-sdg",
    "nrcs-immokalee-osd",
    "nrcs-eaugallie-osd",
    "nrcs-felda-osd",
    "dep-rule",
    "fs125572",
    "fs720-3045",
    "nws-tbw-tstm-climo",
    ("Census Reporter, Palmetto FL (ACS 2020-2024 5-yr, B01003/B25035)", "http://censusreporter.org/profiles/16000US1254250-palmetto-fl/"),
    ("Wikipedia, Palmetto, Florida", "https://en.wikipedia.org/wiki/Palmetto,_Florida"),
    ("Wikipedia, Snead Island", "https://en.wikipedia.org/wiki/Snead_Island"),
]

HUB = page(
    "/palmetto-fl/", "city",
    "Concrete & Paver Contractor in Palmetto, FL",
    "Opera pours concrete and sets pavers in Palmetto, FL, where Public Works permits driveway work in the street under Code Sec. 25-2 and homes date to 1983.",
    "Concrete, Pavers and Turf for Palmetto Homes",
    capsule(
        "Palmetto sits on the north bank of the Manatee River, across from Bradenton and about 13 miles from the Sarasota unit's base, where the crew pours driveways, patios, pool decks and turf. "
        "As of October 2026, the city's own code reaches only the work that happens in the street or along the shoreline; a residential patio or slab off that strip has no published city rule at all, so a call to the Building Department settles it."
    ),
    "".join([
        sec(
            "Who signs off on a Palmetto driveway apron, and who doesn't?",
            "<p>City Code Sec. 25-2(a) makes it unlawful for a contractor to \"place or construct... culverts, driveways, curbs, or sidewalks within any public street, alley or other public right-of-way\" without first applying for a written permit from the Department of Public Works "
            + src("palmetto-code-25-2-row-permit", "Palmetto Code Sec. 25-2") + ". The city's own Right-of-Way Use Application spells out the mechanics: notify Public Works at least 48 hours before work starts, begin within 60 days of the permit being issued, finish within 30 days, and restore the disturbed section to city standards before the final inspection closes it out "
            + src("palmetto-row-permit-form", "Palmetto Right-of-Way Use Permit") + ". That rule governs the apron at the street. The Building Department's own page is silent on a patio, a slab or a stretch of driveway back from the curb, saying only that \"if you are not sure whether or not a permit is required, call the Building Department at (941) 721-2166\" "
            + src("palmetto-building-department", "Palmetto Building Department") + ", which is the opposite of how Manatee County's unincorporated side handles the same question, as " + post("manatee-county-driveway-permits", "our Manatee County permit guide") + " covers in full.</p>"
        ),
        sec(
            "Why does a Palmetto retaining wall need a permit at any height?",
            "<p>Sec. 10-46 of the city code names the work directly: a permit is required before anyone builds, changes or tears down \"any seawall, retaining wall or bulkhead,\" and nothing in that section carves out a height below which the rule stops applying "
            + src("palmetto-code-10-46-retaining-wall-permit", "Palmetto Code Sec. 10-46") + ". The fee that goes with it, set by Sec. 10-47, runs $10 plus $0.10 per linear foot "
            + src("palmetto-code-10-46-retaining-wall-permit", "Palmetto Code Sec. 10-47 fee") + ". A low segmental-block garden wall that would skip a permit in plenty of other Florida towns still needs one filed here, a detail worth knowing before a grading plan near the river gets finalized.</p>"
        ),
        sec(
            "Does adding a patio or pool deck raise a Palmetto utility bill?",
            "<p>The city hasn't published a residential impervious surface ratio the way neighboring Bradenton has; the only rule tied to hardscape coverage found in the code is a stormwater utility fee under Sec. 29-207, calculated from how much impervious area sits on a parcel "
            + src("palmetto-code-29-207-stormwater-fee", "Palmetto Code Sec. 29-207") + ". That means a new " + svc("concrete-pool-decks", "pool deck") + " or a widened " + svc("paver-patios", "paver patio") + " in Palmetto won't bump against a coverage cap on the building permit the way the same addition would across the river, though it can shift the recurring fee line on the city utility bill.</p>"
        ),
        sec(
            "What does Palmetto's age and growth mean for a project here?",
            "<p>Local histories put Palmetto's founding at 1868, when Samuel Sparks Lamb surveyed and platted the original town site, with the settlement incorporating as a city in 1897 "
            + ext("https://en.wikipedia.org/wiki/Palmetto,_Florida", "Palmetto, Florida") + ". Census Reporter's current five-year estimate counts about 13,588 residents, and the same dataset puts the median year a Palmetto home was built at 1983, the same decade as homes across the bridge in Bradenton "
            + ext("http://censusreporter.org/profiles/16000US1254250-palmetto-fl/", "Census Reporter, Palmetto FL") + ". That stock contrasts with Riviera Dunes, a waterfront community built starting in 1998 on a reclaimed 214-acre dolomite mine site along the river, where lots, setbacks and drainage all run newer than the downtown grid " + ext("https://en.wikipedia.org/wiki/Palmetto,_Florida", "Palmetto, Florida") + ".</p>"
        ),
        sec(
            "How close does the Manatee River and Terra Ceia Bay sit to a Palmetto yard?",
            "<p>Palmetto's downtown faces the Manatee River directly across from Bradenton, and Snead Island, just west of the city, sits between Terra Ceia Bay to the north and Tampa Bay to the west "
            + ext("https://en.wikipedia.org/wiki/Snead_Island", "Snead Island") + ". FEMA's Zone AE carries roughly a 1% yearly flood chance with modest wave heights, while the Coastal High Hazard Zone VE adds breaking-wave force strong enough to damage a low structure "
            + src("fema-coastal-firm", "FEMA flood zone designations") + ", and a lot inside FDOT's marine-environment band, within 2,500 feet of water carrying 2,000 ppm chloride or more, calls for salt-rated hardware on a " + svc("pool-deck-pavers", "paver pool deck") + " or a " + svc("retaining-walls", "retaining wall") + " " + src("fdot-sdg", "FDOT marine-environment classification") + ". Inland, Immokalee soil, poorly drained with a water table 6 to 18 inches down for one to four months most years, is common enough under a Palmetto lot to shape how much base a driveway needs " + src("nrcs-immokalee-osd", "NRCS Immokalee soil series") + ".</p>"
        ),
        sec(
            "What water restriction applies to a Palmetto lawn or a new slab's curing?",
            "<p>Manatee County confirmed on September 22, 2026 that it's keeping Southwest Florida Water Management District's Modified Phase III order in place through March 31, 2027, limiting sprinkler irrigation to one assigned day a week before 8 a.m. or after 6 p.m., with hand-watering and micro-irrigation allowed daily inside that same window regardless of the schedule "
            + src("manatee-phase3", "Manatee Modified Phase III order") + " " + src("swfwmd-restrictions", "SWFWMD district restrictions") + ". That daily hand-watering carve-out matters on a job site, since it covers watering in fresh sod or keeping a new slab's curing compound moist without waiting for an assigned day. " + svc("artificial-turf", "Artificial turf") + " sidesteps the schedule entirely, a tradeoff compared in " + compare("artificial-turf-vs-sod", "our turf-versus-sod comparison") + ".</p>"
        ),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq(
            "Does Palmetto or Manatee County issue my driveway permit?",
            "The City of Palmetto does, since the address sits inside an incorporated city. Code Sec. 25-2 puts any driveway, curb or sidewalk work in the public right-of-way under a Public Works permit, a different office than the county permit a nearby unincorporated address would use."
        ),
        faq(
            "Is a low retaining wall exempt from a permit in Palmetto?",
            "No. Sec. 10-46 covers any seawall, retaining wall or bulkhead regardless of height, with no published threshold below which the requirement drops away, so even a short garden wall needs an application filed first."
        ),
        faq(
            "Does a pool deck addition cap out at a coverage limit in Palmetto?",
            "Not that the published code sets. Instead, Sec. 29-207 ties a stormwater utility fee to the parcel's impervious area, so a larger deck or patio can shift a recurring charge rather than trip a hard percentage cap on the building permit."
        ),
        faq(
            "Is my Palmetto address near enough to the water for FEMA's flood zones to matter?",
            "Possibly, especially downtown along the Manatee River or near Snead Island to the west. FEMA's Zone AE and the higher-risk Coastal Zone VE both apply close to the water; the Flood Map Service Center at msc.fema.gov shows a specific parcel's designation."
        ),
        faq(
            "How do you find the best concrete contractor in Palmetto?",
            "Verify the contractor on the state's license-lookup tool, ask whether the bid accounts for the city's right-of-way permit on any work touching the street, and confirm how the crew plans the base over Immokalee or similar flatwoods soil. " + post("how-to-choose-a-concrete-contractor-sarasota", "Our contractor guide") + " goes through the rest."
        ),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Palmetto",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/manatee-county-driveway-permits/", "Driveway and patio permits in Bradenton, Lakewood Ranch, Parrish and Palmetto"),
        ("/bradenton-fl/", "Concrete, pavers and turf in Bradenton"),
        ("/lakewood-ranch-fl/", "Concrete, pavers and turf in Lakewood Ranch"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Palmetto, FL",
)

LOCAL = {
    "concrete-driveways": {
        "title": "Concrete Driveways in Palmetto, FL – ROW Permit",
        "meta": "Concrete driveways in Palmetto, FL need a Public Works right-of-way permit under Code Sec. 25-2; market range is " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", Oct. 2026.",
        "h1": "Concrete Driveway Installation in Palmetto",
        "lede": capsule(
            "A new or replacement concrete driveway in Palmetto runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", a range that held through October 2026. "
            "The apron where it meets the street is the only part the city regulates directly, under a right-of-way permit that has to be filed before the old concrete comes out."
        ),
        "sections": [
            (
                "One permit for the street, none published for the rest",
                "<p>Pulling out and repouring a Palmetto driveway apron is covered by Code Sec. 25-2, which bars a contractor from working in the right-of-way \"unless application shall first be made to and a written permit obtained from the department of public works\" "
                + src("palmetto-code-25-2-row-permit", "Palmetto Code Sec. 25-2") + ". The Right-of-Way Use Permit itself sets the clock: 48 hours' notice before the crew shows up, a start within 60 days of approval, and the job wrapped within 30 days, with Public Works doing the final look before it's closed "
                + src("palmetto-row-permit-form", "Palmetto Right-of-Way Use Permit") + ". The driveway section between the sidewalk and the garage sits outside that rule, and the Building Department's page doesn't publish a separate threshold for it, so we confirm scope with a phone call rather than assume the private portion is exempt " + src("palmetto-building-department", "Palmetto Building Department") + ".</p>"
            ),
            (
                "Planning the base for Palmetto's flatwoods subgrade",
                "<p>Immokalee fine sand, mapped widely across the city, is poorly drained, carrying a seasonal high water table 6 to 18 inches down for one to four months most years and 18 to 42 inches down for longer stretches "
                + src("nrcs-immokalee-osd", "NRCS Immokalee soil series") + ". Florida's residential code allows up to 24 inches of clean sand or gravel fill, or 8 inches of ordinary earth, before an engineer has to sign off, with a 4-inch compacted base required under the slab regardless. On a driveway built for a work truck or a boat trailer rather than a sedan, that wet subgrade is the detail that decides how deep the base goes, not the finished square footage.</p>"
            ),
        ],
        "scenario": (
            "Say a 22 x 24 ft two-car driveway in an older downtown Palmetto neighborhood needs a full tear-out, 528 sq ft total",
            "<p>Say a 22 x 24 ft two-car driveway in an older downtown Palmetto neighborhood needs a full tear-out, 528 sq ft total. At " + price("concrete-driveway") + " per sq ft, that spans $3,168 to $7,920 across the full range, narrowing to roughly $4,224 to $6,336 inside the typical " + price("concrete-driveway", typical=True) + " band. The private slab is priced the same whether or not the apron gets touched, but once the apron at the street is part of the job, the right-of-way permit has to be filed and the 48-hour notice given before the old concrete comes out, something a driveway set back entirely on private ground skips.</p>"
        ),
        "faqs": [
            faq(
                "Do I need a city permit to replace my Palmetto driveway?",
                "The apron in the right-of-way does, under Code Sec. 25-2, with Public Works requiring 48 hours' notice before work starts. The city's published rules are silent on the private section of the driveway, so we call the Building Department to confirm scope before pricing a job."
            ),
            faq(
                "How fast does a Palmetto right-of-way permit have to move once it's issued?",
                "The permit requires work to start within 60 days of issuance and finish within 30 days once it begins, with a final Public Works inspection closing it out and the restored section matching city standards."
            ),
            faq(
                "Does Palmetto's soil affect how deep a driveway base goes?",
                "Often, yes. Immokalee soil, common under Palmetto lots, holds a seasonal high water table within 18 inches of the surface for part of the year, which changes the fill and base plan for a driveway built to carry heavier loads."
            ),
        ],
        "sources": SRC,
    },
    "paver-driveways": {
        "title": "Paver Driveways in Palmetto, FL – Riviera Dunes",
        "meta": "Paver driveways in Palmetto, FL still need a Public Works ROW permit where the apron meets the street; market range is " + price("paver-driveway") + " per " + per("paver-driveway") + ", Oct. 2026.",
        "h1": "Paver Driveway Installation in Palmetto",
        "lede": capsule(
            "Palmetto homeowners pricing a paver driveway see " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026, whether the lot sits downtown or along the newer waterfront at Riviera Dunes. "
            "The permit rule stays the same either way: anything touching the street needs the city's right-of-way approval first."
        ),
        "sections": [
            (
                "Newer ground at Riviera Dunes, older ground downtown",
                "<p>Riviera Dunes, a waterfront community that began development in 1998 on a reclaimed 214-acre dolomite mine along the Manatee River, sits on a very different footprint than Palmetto's older downtown grid "
                + ext("https://en.wikipedia.org/wiki/Palmetto,_Florida", "Palmetto, Florida") + ". A wider motor-court paver driveway common on a newer Riviera Dunes lot still answers to the same Sec. 25-2 right-of-way rule at the street as a narrower apron on an older downtown block " + src("palmetto-code-25-2-row-permit", "Palmetto Code Sec. 25-2") + ", and the city's own form sets the same 48-hour notice and 30-day completion window for either one " + src("palmetto-row-permit-form", "Palmetto Right-of-Way Use Permit") + ".</p>"
            ),
            (
                "Compacting a paver base over wet ground",
                "<p>ICPI calls for about 6 inches of compacted aggregate on ground that drains freely, with 2 to 4 more inches added where the subgrade stays wet. Two soils common around Manatee County fall into that second group: EauGallie keeps groundwater inside 18 inches of grade for one to four months most years, and Felda does the same for two to six months "
                + src("nrcs-eaugallie-osd", "NRCS EauGallie soil series") + " " + src("nrcs-felda-osd", "NRCS Felda soil series") + ". Pouring the standard 6-inch base on either one is how a paver driveway ends up rutting under a parked car within a season or two.</p>"
            ),
        ],
        "scenario": (
            "Say a 16 x 38 ft paver driveway with a side motor court on a Riviera Dunes lot comes to 608 sq ft",
            "<p>Say a 16 x 38 ft paver driveway with a side motor court on a Riviera Dunes lot comes to 608 sq ft. At " + price("paver-driveway") + " per sq ft, figure $6,080 to $18,240 across the full range, tightening to about $7,296 to $12,160 inside the typical " + price("paver-driveway", typical=True) + " band depending on paver thickness and pattern. Because the lot sits on reclaimed, newer-graded ground rather than the original downtown fill, the base compaction gets checked against the softer spots a mine-site reclamation can leave behind, and the apron at the street still needs the same right-of-way filing a downtown Palmetto driveway would.</p>"
        ),
        "faqs": [
            faq(
                "Does a paver driveway at Riviera Dunes need a different permit than one downtown?",
                "No. Both answer to the same Code Sec. 25-2 right-of-way permit for the portion touching the street, regardless of which part of Palmetto the lot sits in."
            ),
            faq(
                "Does a paver driveway need extra base depth on Palmetto's wetter lots?",
                "On EauGallie or Felda ground, yes, typically 2 to 4 more inches of compacted base than a free-draining lot needs, since groundwater on both soils sits inside 18 inches of grade for part of a typical year."
            ),
            faq(
                "How wide can a paver driveway be in Palmetto?",
                "The published city code doesn't set a maximum width for a residential apron the way some neighboring jurisdictions do; the Right-of-Way Use Permit application and a call to Public Works confirm what a specific lot and street can support."
            ),
        ],
        "sources": SRC,
    },
    "concrete-patios": {
        "title": "Concrete Patios in Palmetto, FL – No City Rule",
        "meta": "Concrete patios in Palmetto, FL have no published city permit rule, unlike driveway work in the ROW; market range is " + price("concrete-patio") + " per " + per("concrete-patio") + ".",
        "h1": "Concrete Patio Installation in Palmetto",
        "lede": capsule(
            "As of October 2026, a concrete patio in Palmetto costs " + price("concrete-patio") + " per " + per("concrete-patio") + ". "
            "The city's code covers driveways and walls in detail but says nothing specific about a patio, which makes a phone call to the Building Department the fastest way to confirm what a given project needs."
        ),
        "sections": [
            (
                "What the Building Department actually says about a patio",
                "<p>Palmetto's Building Department page lists building, electrical, plumbing and mechanical work, fences and \"other minor construction projects such as storage sheds\" as needing a permit, without naming a patio slab one way or the other "
                + src("palmetto-building-department", "Palmetto Building Department") + ". The page's own advice is to call (941) 721-2166 when it isn't clear, which is the opposite of a published patio exemption and worth more trust than guessing, since a wrong assumption on a permit question can mean tearing out finished work.</p>"
            ),
            (
                "Fitting a patio into the flatwoods drainage picture",
                "<p>Felda soil, mapped on plenty of Palmetto lots, keeps groundwater within roughly a foot of grade for two to six months out of a typical year, a timeline that drives how a patio's slope and perimeter drain get laid out rather than how deep the base itself runs "
                + src("nrcs-felda-osd", "NRCS Felda soil series") + ". Palmetto's stormwater utility fee under Sec. 29-207 is based on a parcel's impervious area " + src("palmetto-code-29-207-stormwater-fee", "Palmetto Code Sec. 29-207") + ", so a sizeable patio addition is worth checking against that fee schedule even though it won't run into a hard coverage cap the way it might in a neighboring city.</p>"
            ),
        ],
        "scenario": (
            "Say a 15 x 18 ft back patio addition off an older Palmetto home's lanai comes to 270 sq ft",
            "<p>Say a 15 x 18 ft back patio addition off an older Palmetto home's lanai comes to 270 sq ft. At " + price("concrete-patio") + " per sq ft, figure $1,620 to $3,510 across the full range, tightening to roughly $1,890 to $2,700 inside the typical " + price("concrete-patio", typical=True) + " band for a broom finish. Before pricing it, a call to the Building Department confirms whether this particular scope needs a permit, since the published code doesn't spell out an answer for a patio the way it does for driveway work in the right-of-way, and the added square footage gets factored into the stormwater fee calculation either way.</p>"
        ),
        "faqs": [
            faq(
                "Does a concrete patio need a permit in Palmetto?",
                "The published code doesn't say directly. The Building Department's own page recommends calling (941) 721-2166 to confirm, since patios aren't named among the listed permit categories the way building and fence work is."
            ),
            faq(
                "Will a new patio affect my Palmetto utility bill?",
                "Possibly. The city's stormwater fee under Sec. 29-207 is calculated from a parcel's impervious area, so adding a patio can shift that recurring charge even without triggering a separate coverage cap on the building permit."
            ),
            faq(
                "Why does a Palmetto patio need extra drainage planning on some lots?",
                "On Felda soil, common across parts of the city, the seasonal high water table sits within about a foot of the surface for part of the year, which changes how the slope and perimeter drainage around a patio get designed."
            ),
        ],
        "sources": SRC,
    },
    "paver-patios": {
        "title": "Paver Patios in Palmetto, FL – Historic Lots",
        "meta": "Paver patios on Palmetto, FL's older 1983-median lots pair with a city still silent on patio permits; market range is " + price("paver-patio") + " per " + per("paver-patio") + ".",
        "h1": "Paver Patios and Walkways in Palmetto",
        "lede": capsule(
            "A paver patio in Palmetto runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. "
            "On the older lots near the Palmetto Historic District downtown, the original hardscape often predates the pool cage or lanai it now sits beside, which changes how a replacement patio has to tie in."
        ),
        "sections": [
            (
                "Working around an older home's existing footprint",
                "<p>Census Reporter's current estimate puts the median year a Palmetto home was built at 1983 "
                + ext("http://censusreporter.org/profiles/16000US1254250-palmetto-fl/", "Census Reporter, Palmetto FL") + ", a generation before many pool cages and lanai additions went in, which means a paver patio project here often has to tie into a slab or a screen frame added years after the original build rather than a clean, uniform footprint. The Palmetto Historic District downtown preserves blocks from that same era " + ext("https://en.wikipedia.org/wiki/Palmetto,_Florida", "Palmetto, Florida") + ", and matching a new paver patio's elevation to an older house's existing threshold is a common fit issue on those lots.</p>"
            ),
            (
                "Edge restraint and joint sand near the river",
                "<p>A paver patio close to the Manatee River downtown, or near Snead Island where Terra Ceia Bay and Tampa Bay both reach the shoreline just west of the city " + ext("https://en.wikipedia.org/wiki/Snead_Island", "Snead Island") + ", falls inside FDOT's own definition of a marine environment, anything within 2,500 feet of water that salty " + src("fdot-sdg", "FDOT marine-environment classification") + ". A standard edge restraint and an unsealed joint give out faster under that kind of exposure than they would a mile or two inland, so hardware choice carries more weight on a riverfront Palmetto lot than on one set back a few blocks.</p>"
            ),
        ],
        "scenario": (
            "Say an 18 x 22 ft paver patio replacing an original slab beside a 1980s-era pool cage comes to 396 sq ft",
            "<p>Say an 18 x 22 ft paver patio replacing an original slab beside a 1980s-era pool cage comes to 396 sq ft. At " + price("paver-patio") + " per sq ft, that runs $3,960 to $6,732 across the full range, narrowing to about $4,752 to $6,336 inside the typical " + price("paver-patio", typical=True) + " band depending on the paver and pattern chosen. Tying the new surface into the existing screen frame's threshold height takes more planning than a blank-slate patio would, and if the lot sits close enough to the river for FDOT's marine-environment threshold to apply, the edge restraint and joint sand get specified for salt exposure rather than the standard inland hardware.</p>"
        ),
        "faqs": [
            faq(
                "Why does a Palmetto paver patio sometimes need to match an older slab's height?",
                "Many Palmetto homes date to around 1983, often a decade or more before a pool cage or lanai got added, so a replacement patio commonly has to tie into a screen frame's existing threshold rather than start from an open footprint."
            ),
            faq(
                "Does a paver patio near the Manatee River need different hardware in Palmetto?",
                "On a lot close to the river or near Snead Island to the west, yes. FDOT's structures guide classifies that stretch as a marine environment, which speeds up joint-sand washout and edge-restraint wear without salt-rated hardware."
            ),
            faq(
                "Is the Palmetto Historic District relevant to a paver patio project?",
                "It describes the character of the surrounding blocks rather than regulating paver material directly; the city's published code doesn't name a historic-district review process specific to patio hardscape."
            ),
        ],
        "sources": SRC,
    },
    "concrete-pool-decks": {
        "title": "Concrete Pool Decks in Palmetto, FL – River Flood Zones",
        "meta": "Concrete pool decks near the Manatee River in Palmetto, FL sit close to FEMA Zone AE or VE; market range is " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ", Oct. 2026.",
        "h1": "Concrete Pool Deck Installation in Palmetto",
        "lede": capsule(
            "A concrete pool deck in Palmetto runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. "
            "A lot close to the Manatee River or the shoreline near Snead Island to the west carries a FEMA flood designation that sets the deck's minimum elevation well before the finish is chosen."
        ),
        "sections": [
            (
                "Flood zones along Palmetto's riverfront",
                "<p>FEMA's Zone AE carries roughly a 1% yearly chance of flooding with limited wave action, while the Coastal High Hazard Zone VE pairs those same odds with breaking surf strong enough to damage a low structure in a major storm "
                + src("fema-coastal-firm", "FEMA flood zone designations") + ". Palmetto's downtown faces the Manatee River directly, and Snead Island, bordered by Terra Ceia Bay on one side and Tampa Bay on the other, sits just west of the city line "
                + ext("https://en.wikipedia.org/wiki/Snead_Island", "Snead Island") + ". A free parcel lookup at FEMA's Flood Map Service Center is the fastest way to confirm which zone, if any, a specific Palmetto address falls into before a deck's finished elevation is set.</p>"
            ),
            (
                "Counting the deck toward the stormwater fee, not a coverage cap",
                "<p>Unlike Bradenton's published impervious surface ratio, Palmetto's code doesn't set a residential coverage percentage; the hardscape math that does apply runs through the stormwater utility fee under Sec. 29-207, based on how much impervious area the lot carries "
                + src("palmetto-code-29-207-stormwater-fee", "Palmetto Code Sec. 29-207") + ". A larger pool deck addition is worth weighing against that fee line even without a hard cap forcing a design change, especially alongside an existing driveway and patio on the same parcel.</p>"
            ),
        ],
        "scenario": (
            "Say a 640 sq ft screened-cage pool deck on a Palmetto lot sits close enough to the river for the flood map to matter",
            "<p>Say a 640 sq ft screened-cage pool deck on a Palmetto lot sits close enough to the river for the flood map to matter. At " + price("concrete-pool-deck") + " per sq ft, that spans $3,200 to $9,600 across the full range, tightening to roughly $4,480 to $7,680 inside the typical " + price("concrete-pool-deck", typical=True) + " band, the difference largely tied to a plain broom finish versus a cool-touch textured coating. Because the parcel's flood zone sets a minimum elevation at the coping, the fill and slope under the deck get planned around that number first, and the added square footage still factors into the lot's stormwater fee once the permit is filed.</p>"
        ),
        "faqs": [
            faq(
                "Is my Palmetto pool deck lot in a flood zone?",
                "Possibly, especially facing the Manatee River downtown or near Snead Island to the west. FEMA's Flood Map Service Center at msc.fema.gov returns the specific zone designation, AE or the higher-risk VE, for a given parcel."
            ),
            faq(
                "Does a pool deck push my Palmetto lot over a coverage limit?",
                "The city hasn't published a residential impervious surface cap the way Bradenton has. A larger deck does factor into the Sec. 29-207 stormwater fee, which is based on a parcel's total impervious area, but it isn't capped at a fixed percentage."
            ),
            faq(
                "Does FEMA's Zone VE rule out a pool deck near the water in Palmetto?",
                "No, but it raises the standard for fill and drainage planning, since Zone VE adds breaking-wave force to the same roughly 1% yearly flood odds Zone AE carries, which changes how the slab's elevation and edge get engineered."
            ),
        ],
        "sources": SRC,
    },
    "pool-deck-pavers": {
        "title": "Pool Deck Pavers in Palmetto, FL – Salt Exposure",
        "meta": "Pool deck pavers near the Manatee River in Palmetto, FL face FDOT's marine-environment salt criterion; market range is " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ", Oct. 2026.",
        "h1": "Travertine and Paver Pool Decks in Palmetto",
        "lede": capsule(
            "Pool deck pavers or travertine in Palmetto run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. "
            "The closer a lot sits to the Manatee River or the Tampa Bay side near Snead Island, the more the sealer and edge-restraint choice matters compared with an inland Palmetto yard."
        ),
        "sections": [
            (
                "Reading the marine-environment line before specifying hardware",
                "<p>FDOT's structures manual draws its marine-environment classification at 2,500 feet from water carrying 2,000 ppm chloride or more "
                + src("fdot-sdg", "FDOT marine-environment classification") + ", a threshold that reaches much of downtown Palmetto along the Manatee River and the shoreline near Snead Island to the west, where Terra Ceia Bay and Tampa Bay both meet the land " + ext("https://en.wikipedia.org/wiki/Snead_Island", "Snead Island") + ". Inside that band, joint sand washes out faster and an unsealed travertine surface stains sooner, which is why we size the resealing interval to a lot's actual distance from open water rather than using one schedule citywide.</p>"
            ),
            (
                "Pool deck pavers still answer to the stormwater fee",
                "<p>A travertine or paver pool deck adds to the same impervious-area total the city's stormwater utility fee under Sec. 29-207 draws from, whether the lot sits downtown or a few blocks inland "
                + src("palmetto-code-29-207-stormwater-fee", "Palmetto Code Sec. 29-207") + ". The deck still needs its slope and the aggregate base planned for Immokalee or similar poorly drained soil underneath, since salt exposure changes the surface hardware, not the compaction the base itself needs " + src("nrcs-immokalee-osd", "NRCS Immokalee soil series") + ".</p>"
            ),
        ],
        "scenario": (
            "Say a 500 sq ft travertine pool deck overlay on a Palmetto lot a few hundred feet from the Manatee River",
            "<p>Say a 500 sq ft travertine pool deck overlay on a Palmetto lot a few hundred feet from the Manatee River. At " + price("pool-deck-pavers") + " per sq ft, figure $6,000 to $15,000 across the full range, tightening to about $7,000 to $11,000 inside the typical " + price("pool-deck-pavers", typical=True) + " band, the spread tied to stone grade and pattern. Because the lot sits well inside FDOT's marine-environment threshold, the sealer and edge restraint get specified for salt exposure, with a shorter resealing interval planned from the start rather than added after the first signs of staining show up.</p>"
        ),
        "faqs": [
            faq(
                "Does salt air from the Manatee River affect pool deck pavers in Palmetto?",
                "On a lot within FDOT's marine-environment threshold, roughly 2,500 feet of water carrying meaningful salt content, yes. Joint sand and an unsealed surface wear faster there than on an inland Palmetto yard, which is why we spec hardware by distance from the water."
            ),
            faq(
                "How often should a Palmetto pool deck near the river be resealed?",
                "More often than an inland deck, as a rule of thumb, since salt exposure speeds up joint-sand washout and surface staining. We check a lot's distance from the river or Snead Island before setting a specific interval."
            ),
            faq(
                "Does the type of soil under a Palmetto pool deck matter?",
                "Yes. Immokalee soil, common across the city, is poorly drained with a seasonal high water table, which affects how the compacted aggregate base under the deck is planned regardless of whether the surface is travertine or standard pavers."
            ),
        ],
        "sources": SRC,
    },
    "stamped-concrete": {
        "title": "Stamped Concrete in Palmetto, FL – ROW Apron",
        "meta": "Stamped concrete in Palmetto, FL crossing the right-of-way still needs a Sec. 25-2 permit; market range is " + price("stamped-concrete") + " per " + per("stamped-concrete") + ", Oct. 2026.",
        "h1": "Stamped Concrete Driveways and Patios in Palmetto",
        "lede": capsule(
            "Stamped concrete in Palmetto costs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October 2026, the same range whether the pattern goes on an entry walk downtown or a Riviera Dunes patio. "
            "A stamped apron crossing the right-of-way still falls under the same city permit a plain concrete driveway needs."
        ),
        "sections": [
            (
                "A decorative finish doesn't change which permit applies",
                "<p>Swapping a broom finish for an ashlar or cobble stamp pattern doesn't move the work out from under Sec. 25-2 if any part of it crosses the right-of-way at the street; Public Works still reviews that section the same way it would a plain pour "
                + src("palmetto-code-25-2-row-permit", "Palmetto Code Sec. 25-2") + ". Off that strip, the city's published rules stay quiet on flatwork generally, so a stamped patio addition gets the same call-ahead treatment to the Building Department that a plain one would " + src("palmetto-building-department", "Palmetto Building Department") + ".</p>"
            ),
            (
                "Working inside the region's late-spring-to-fall storm window",
                "<p>NWS Tampa Bay marks the regional rainy season from roughly May 15 through October 15 "
                + src("nws-tbw-tstm-climo", "NWS Tampa Bay rainy-season dates") + ", a stretch when an unplanned afternoon downpour can catch a crew mid-texture. Keeping the surface workable long enough to set an even stamp pattern during that window is less about the forecast for the week and more about starting early in the day, before heat and humidity speed up how fast the slab firms underneath the tools.</p>"
            ),
        ],
        "scenario": (
            "Say a 300 sq ft stamped-concrete entry walk and small front porch addition, downtown on an older Palmetto lot",
            "<p>Say a 300 sq ft stamped-concrete entry walk and small front porch addition, downtown on an older Palmetto lot. At " + price("stamped-concrete") + " per sq ft, that comes to $2,400 to $5,700 across the full range, narrowing to about $3,600 to $4,800 inside the typical " + price("stamped-concrete", typical=True) + " band depending on color count and the stamp pattern chosen. None of the walk crosses the right-of-way in this layout, so Sec. 25-2's permit doesn't apply, though the crew still schedules the pour for an early morning start during the rainy season rather than risk the texture setting unevenly under an afternoon sky that's turned.</p>"
        ),
        "faqs": [
            faq(
                "Does a stamped driveway apron in Palmetto need the same permit as a plain one?",
                "Yes. The decorative finish doesn't change the Sec. 25-2 requirement for any portion of the work that touches the public right-of-way at the street; Public Works reviews a stamped apron the same way it reviews a broom-finished one."
            ),
            faq(
                "When is the riskiest time of year to pour stamped concrete in Palmetto?",
                "Roughly mid-May through mid-October, the regional rainy season NWS Tampa Bay tracks for this part of the state, when an afternoon storm arriving before the texture is set can mar a stamped pattern."
            ),
            faq(
                "Does stamped concrete cost more than a plain driveway in Palmetto?",
                "Yes, generally: " + price("stamped-concrete") + " per sq ft for stamped work against " + price("concrete-driveway") + " for plain concrete, a gap tied to the integral color and texturing labor rather than to any difference in city permitting."
            ),
        ],
        "sources": SRC,
    },
    "artificial-turf": {
        "title": "Artificial Turf in Palmetto, FL – Canal Lots",
        "meta": "Artificial turf on canal-front Riviera Dunes lots in Palmetto, FL follows the state's 10-foot water buffer; market range is " + price("artificial-turf") + " per " + per("artificial-turf") + ", Oct. 2026.",
        "h1": "Artificial Turf for Palmetto Yards",
        "lede": capsule(
            "Artificial turf in Palmetto runs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October 2026, whether the yard sits downtown or along a Riviera Dunes canal. "
            "A canal-front or riverfront lot has one extra layout rule to plan around before the turf order goes in."
        ),
        "sections": [
            (
                "Four things the state rule covers",
                "<p>Rule 62-308.100 of the Florida Administrative Code took effect May 19, 2026 and governs residential synthetic turf statewide " + src("dep-rule", "DEP Rule 62-308.100") + ":</p>"
                + ul([
                    "Infill has to be a natural material, not crumb rubber or a similar synthetic.",
                    "The base underneath has to be washed rock rather than unwashed fill.",
                    "No irrigation line can run beneath the finished turf.",
                    "The turf has to sit at least 10 feet back from a water body's edge, unless the property line there is a seawall.",
                ])
                + "<p>A Riviera Dunes canal lot or a yard that runs down to the Manatee River has to account for that last point specifically; a yard with no water frontage never encounters it. Separately, F.S. 125.572 caps how far a city or county can tighten residential turf rules beyond this statewide floor " + src("fs125572", "F.S. 125.572") + ".</p>"
            ),
            (
                "A lawn that ignores the county's weekly watering order",
                "<p>Lawns across the county are still rationed to a single pre-dawn or evening watering slot each week under the district's Modified Phase III order, a restriction Manatee confirmed stays in force through the end of March 2027 "
                + src("manatee-phase3", "Manatee Modified Phase III order") + " " + src("swfwmd-restrictions", "SWFWMD district restrictions") + ". Turf never has to wait its turn in that rotation; once it's watered in during installation, the weekly clock simply stops applying, a comparison worked out further in " + compare("artificial-turf-vs-sod", "our turf-versus-sod comparison") + ". A turf patch tucked behind a fence or a hedge, out of sight from the street and from neighboring yards, also gets protection from most deed restrictions under F.S. 720.3045 as of 2026 " + src("fs720-3045", "F.S. 720.3045") + ".</p>"
            ),
        ],
        "scenario": (
            "Say an 850 sq ft backyard turf project sits behind a Riviera Dunes home roughly 40 ft from a canal's edge",
            "<p>Say an 850 sq ft backyard turf project sits behind a Riviera Dunes home roughly 40 ft from a canal's edge. At " + price("artificial-turf") + " per sq ft, that spans $8,500 to $21,250 across the full range, tightening to about $10,200 to $15,300 inside the typical " + price("artificial-turf", typical=True) + " band depending on pile height and backing. Forty feet clears the state's water-buffer line with room to spare, so the layout doesn't bump against it, though the washed-base and natural-infill specs still apply the same as they would on a yard nowhere near the canal.</p>"
        ),
        "faqs": [
            faq(
                "How far back from a Riviera Dunes canal does artificial turf have to sit?",
                "At least 10 feet from the water's edge under the state turf rule, unless a seawall runs along that property line, in which case the buffer doesn't apply."
            ),
            faq(
                "Does a turf lawn still need to follow Manatee County's watering order?",
                "No, not after it's installed. The county's current order governs sprinkler irrigation on a weekly schedule through March 2027, and turf stops needing any watering at all once it's down."
            ),
            faq(
                "What kind of infill does Florida's turf rule require?",
                "A natural material rather than a synthetic one like crumb rubber, paired with a washed-rock base underneath and no irrigation line run beneath the finished surface, statewide as of the rule's 2026 effective date."
            ),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
