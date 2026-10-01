# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "windermere"

WIKI_WINDERMERE = "https://en.wikipedia.org/wiki/Windermere,_Florida"
WIKI_ISLEWORTH = "https://en.wikipedia.org/wiki/Isleworth,_Florida"
WIKI_LAKE_DOWN = "https://en.wikipedia.org/wiki/Lake_Down"
WIKI_OFW_LIST = "https://en.wikipedia.org/wiki/List_of_Outstanding_Florida_Waters"
OFW_FACTSHEET = "https://floridadep.gov/sites/default/files/ofw-factsheet.pdf"
CLICKORLANDO_DIRTROAD = "https://www.clickorlando.com/news/local/2025/07/22/can-a-dirt-road-be-stormwater-resilient-windermere-project-aims-to-try/"
ORANGEOBSERVER_DIRTROAD = "https://www.orangeobserver.com/article/forecast-the-cost-of-keeping-windermeres-roads-dirty"

SRC = [
    "windermere-pdcs", "windermere-row-app", "windermere-isr",
    "census-pep-v2025", "acs-windermere",
    "orange-bldg", "orange-do-i-need-permit", "orange-residential-pavers", "orange-res-plan-guide", "orange-lot-grading",
    "ocfl-horizonwest", "sjrwmd-watering", "dep-rule", "fs125572",
    "fl-senate-2011-104", "fgs-sinkhole-faq",
    ("Wikipedia, Windermere, Florida", WIKI_WINDERMERE),
    ("Wikipedia, Isleworth, Florida", WIKI_ISLEWORTH),
    ("Wikipedia, Lake Down", WIKI_LAKE_DOWN),
    ("Wikipedia, List of Outstanding Florida Waters", WIKI_OFW_LIST),
    ("FDEP, Outstanding Florida Waters fact sheet", OFW_FACTSHEET),
    ("ClickOrlando, a Windermere dirt-road stormwater pilot", CLICKORLANDO_DIRTROAD),
    ("Orange Observer, the cost of keeping Windermere's roads dirty", ORANGEOBSERVER_DIRTROAD),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Who reviews a new driveway or apron in Windermere, the town or the county?",
        "<p>Inside the town line, that desk belongs to PDCS LLC, the outside firm the Town of Windermere hires to run building and permitting out of Town Hall on Main Street " +
        src("windermere-pdcs", "PDCS, Windermere") + ". A new or rebuilt driveway goes through the town's own Right-of-Way Use Application, which splits the money into a $75 application fee, a $50 first inspection and a second $50 "
        "if a reinspection is needed, and Public Works wants a day's notice before a crew pours " + src("windermere-row-app", "Windermere ROW Use Application") + ". The same form fixes the apron itself at 6 inches of "
        "3,000 psi fiber-mesh concrete with a saw-cut edge at the road, 5-foot flares on each side, and keeps a new driveway at least 5 feet off a side property line and 40 feet from an intersection " +
        src("windermere-row-app") + ". " + cs("windermere", "concrete-driveways", "A concrete driveway") + " and " + cs("windermere", "paver-driveways", "a paver driveway") + " both start at that same desk before "
        "either one is drawn up.</p><p>Not every Windermere address answers to PDCS, though. " + ext(WIKI_ISLEWORTH, "Isleworth") + " runs along the south shore of Lake Down, inside the Butler Chain, yet it stayed "
        "unincorporated Orange County rather than joining the town, a split a 2007 annexation fight over its tax base made public. A driveway there goes through the county's own Division of Building Safety instead " +
        src("orange-bldg", "Orange County Division of Building Safety") + ", and the same county desk also covers newer, unincorporated subdivisions along the town's edge toward Horizon West " +
        src("ocfl-horizonwest", "Orange County, Horizon West") + ".</p>"
    ),
    sec(
        "What does Windermere's 0.45 impervious surface cap actually cover?",
        "<p>The town's own land development code caps impervious surface ratio at 0.45 for residential lots, and the definition is written broadly: 'buildings, accessory structures, swimming pools, patios, decks, "
        "driveways, parking areas' " + src("windermere-isr", "Windermere LDC, impervious surface") + ". That single number covers nearly everything a homeowner might add to a yard, so a pool deck, a " +
        svc("paver-patios", "paver patio") + " and a widened driveway are all drawing from the same 45 percent of the lot rather than separate allowances. Step outside the town line into unincorporated "
        "Orange County and the math changes shape: the county's residential-paver permit instead asks that private open space on the lot run at least 40 percent, a different figure measured the opposite way, "
        "reviewed with a $38 permit fee plus a $38 engineering-review fee rather than PDCS's own form " + src("orange-residential-pavers", "Orange County, Residential Pavers") + ".</p>"
    ),
    sec(
        "Why are so many of Windermere's own streets still sand or brick?",
        "<p>Outside Main Street and Sixth Avenue, which carry an estimated 17,000 to 18,000 cars a day through town, most of Windermere's residential grid stayed unpaved by the town's own choice rather than by "
        "accident " + ext(WIKI_WINDERMERE, "Wikipedia, Windermere, Florida") + ". Town Council has looked at paving some of those streets and decided instead to keep rebuilding them to a proper crown 'as long as it "
        "makes fiscal sense,' a sand-street maintenance program the town itself estimates at $200,000 a year, against $2 million to $4 million to bring every dirt street up to grade at once " +
        ext(ORANGEOBSERVER_DIRTROAD, "Orange Observer, Windermere's dirt-road costs") + ". Bessie and Butler streets are mid-way through a $1.4 million pilot that pitches water to the sides instead of down the "
        "crown, adding swales and a rain garden so runoff stops carving out the road the way a flat, worn surface does " + ext(CLICKORLANDO_DIRTROAD, "ClickOrlando, Windermere's dirt-road pilot") + ". " +
        cs("windermere", "concrete-walkways", "A walkway") + " tying into one of those streets answers to whichever drainage design is in place on that block, not a single townwide standard.</p>"
    ),
    sec(
        "What does sitting on the Butler Chain of Lakes change for a lakefront build?",
        "<p>Windermere occupies the isthmus between Lake Down and Lake Butler " + ext(WIKI_WINDERMERE, "Wikipedia, Windermere, Florida") + ", and Lake Down itself, the 885-acre headwater lake of the Butler Chain, runs along the town's western "
        "shore " + ext(WIKI_LAKE_DOWN, "Wikipedia, Lake Down") + ". The whole chain carries Florida's Outstanding Florida Water designation, the state's own protection tier for a waterbody with exceptional "
        "ecological or recreational value, which exists specifically to stop new work from lowering the water quality already there " + ext(OFW_FACTSHEET, "FDEP, Outstanding Florida Waters fact sheet") + "; " +
        src("fs125572") + ". A " + svc("concrete-pool-decks", "pool deck") + " or " + svc("retaining-walls", "retaining wall") + " cut into a lake bank on the Butler Chain is working next to water the state "
        "already flags for extra scrutiny, not an ordinary drainage ditch.</p>"
    ),
    sec(
        "How old is the typical Windermere home, and is the ground under it sinkhole-prone?",
        "<p>Windermere's median home dates to 1989, and the town grew only from 3,159 residents in the 2020 base count to an estimated 3,344 by July 2025, a modest gain next to the growth rates some of the "
        "unit's newer cities post " + src("acs-windermere", "Census Reporter, Windermere FL") + "; " + src("census-pep-v2025", "Census Bureau PEP, Vintage 2025") + ". Orange County does sit among the eleven "
        "counties the Florida Senate flagged for the heaviest statewide sinkhole claims in its 2010 review " + src("fl-senate-2011-104", "Florida Senate Interim Report 2011-104") + ", though the state's own "
        "geological survey draws a line between a sudden cover-collapse sinkhole and the slower, far more common cover-subsidence kind " + src("fgs-sinkhole-faq", "FDEP/FGS Sinkhole FAQ") + "; a dip near a "
        "35-year-old Windermere driveway is a candidate for " + svc("concrete-repair", "resurfacing or repair") + " well before it's a candidate for either one.</p>"
    ),
    sec(
        "Does the state's current watering order reach Windermere?",
        "<p>No, not the emergency version. SJRWMD's own restrictions page keeps all of Orange County on the district's normal, year-round twice-a-week schedule, separate from the Phase III emergency order that "
        "limits Lake County to a single day " + src("sjrwmd-watering", "SJRWMD Watering Restrictions") + ". Near any of the Butler Chain's lakes or canals, " + svc("artificial-turf", "artificial turf") +
        " still answers to the state's own standard either way: installed turf has to sit at least 10 feet back from the water unless a seawall forms the bank, with no buried irrigation line running "
        "underneath it " + src("dep-rule", "Florida Administrative Code, Rule 62-308.100") + ".</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Does the Town of Windermere or Orange County review my project?",
        "It depends on the exact address. Inside the town's own boundary, PDCS LLC runs permitting for the Town of Windermere. Several well-known Windermere-addressed communities, Isleworth among them, sit in unincorporated Orange County instead and go through the county's Division of Building Safety."
    ),
    faq(
        "What is Windermere's maximum impervious surface ratio?",
        "0.45 of the lot, under the town's land development code. The definition covers buildings, accessory structures, swimming pools, patios, decks, driveways and parking areas together, not just the house footprint."
    ),
    faq(
        "Are Windermere's residential streets paved?",
        "Many are not. Main Street and Sixth Avenue carry the town's through traffic and are paved, but most other residential streets remain sand or brick by the town's own maintenance choice, with a current pilot project adding swales to two of them."
    ),
    faq(
        "How close to the Butler Chain of Lakes can artificial turf go in Windermere?",
        "At least 10 feet back from the water under the state's synthetic-turf rule, unless the edge is a seawall rather than open shoreline. The chain's Outstanding Florida Water status adds extra scrutiny to any work that could affect runoff into the lakes."
    ),
    faq(
        "How do you pick the best concrete contractor in Windermere?",
        "Verify the contractor on the state's license-check tool, confirm whether PDCS or Orange County actually reviews the address, and ask whether the bid already accounts for the town's Right-of-Way apron spec. " +
        post("how-to-choose-a-concrete-contractor-orlando", "Ten criteria for choosing a concrete contractor") + " covers the rest."
    ),
]

HUB = page(
    "/windermere-fl/", "city",
    "Concrete, Pavers & Turf Contractor in Windermere, FL",
    "Concrete, pavers and turf in Windermere, FL: PDCS's $75 Right-of-Way permit, the town's 0.45 impervious cap and the Butler Chain of Lakes, October 2026.",
    "Concrete, Pavers and Artificial Turf for Windermere Homes",
    capsule(
        "Windermere sits about 10 miles southwest of Orlando on the Butler Chain of Lakes, a town the Census Bureau put at 3,344 residents in its July 2025 estimate. As of October 2026, PDCS LLC reviews "
        "driveway and apron work for the town itself under a $75 Right-of-Way Use Application, a new concrete driveway runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", and the "
        "town's own impervious cap tops out at 0.45 of the lot."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Windermere",
    related=[
        ("/central-florida/", "The Orlando unit's full coverage area"),
        ("/blog/orange-county-orlando-driveway-patio-permits/", "Driveway and patio permits in Orlando and Orange County"),
        ("/orlando-fl/", "Concrete, pavers and turf in Orlando"),
        ("/kissimmee-fl/", "Concrete, pavers and turf in Kissimmee"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Windermere, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Windermere, FL – ROW Permit",
    "meta": "Concrete driveway installers in Windermere, FL: PDCS's $75/$50 Right-of-Way fees and the town's apron and flare spec, as of October 2026.",
    "h1": "Pouring or Replacing a Concrete Driveway in Windermere",
    "lede": capsule(
        "A new or replacement concrete driveway in Windermere runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026. Before the apron is formed, the town's own "
        "Right-of-Way Use Application sets the fee, the inspection schedule and the exact spec the apron has to meet, a separate process from the private slab review PDCS also handles."
    ),
    "sections": [
        (
            "The $75 application and $50 inspection cover only the right-of-way piece",
            "<p>Windermere's Right-of-Way Use Application, run by the town's contracted building office, PDCS LLC, charges $75 to apply, $50 for the first inspection and another $50 if a reinspection is needed, "
            "and Public Works asks for a day's notice before the pour so an inspector can be on site for both the pre-pour and the final look " + src("windermere-row-app", "Windermere ROW Use Application") + ". "
            "That fee covers the portion of the driveway sitting in the public strip; the rest of the slab, on private ground, is reviewed separately. A homeowner swapping a cracked apron for a new one still "
            "files the application even when nothing about the private driveway itself is changing.</p>"
        ),
        (
            "The apron spec is specific about thickness, flares and setbacks",
            "<p>The same application fixes the apron at 6 inches of 3,000 psi concrete with fiber mesh, saw-cut cleanly at the edge of the road, with 5-foot flares on each side " +
            src("windermere-row-app") + ". No new driveway can sit within 5 feet of a side property line or within 40 feet of an intersection, and where a culvert is called for, it has to run at least 15 inches "
            "across with mitered ends " + src("windermere-row-app") + ". On a lot where the existing apron predates that spec, matching it exactly, rather than copying the old dimensions, is what gets the "
            "reinspection fee avoided the first time around.</p>"
        ),
    ],
    "scenario": (
        "A driveway rebuild with flares, worked out in square feet",
        "<p>Say a Windermere driveway measures 24 by 40 feet, 960 square feet, and the apron where it meets the road adds two 5-foot flares at roughly 25 square feet each for 1,010 square feet total. At " +
        price("concrete-driveway") + " per " + per("concrete-driveway") + ", that full scope runs $6,060 to $15,150, narrowing to about $8,080 to $12,120 in the typical " + price("concrete-driveway", typical=True) +
        " band. The private portion and the right-of-way apron are priced together here, but only the apron crossing into the public strip needs the $75 Right-of-Way Use Application and its follow-up inspection.</p>"
    ),
    "faqs": [
        faq(
            "What does Windermere charge for a driveway permit?",
            "$75 to apply for the Right-of-Way Use Application, plus $50 for the first inspection and another $50 if a reinspection is needed. That covers the portion of the driveway in the public right-of-way."
        ),
        faq(
            "How close to the property line can a Windermere driveway sit?",
            "At least 5 feet from a side property line and at least 40 feet from an intersection, under the town's own Right-of-Way Use Application standard."
        ),
        faq(
            "Does a straight apron replacement in Windermere need the same review as a new driveway?",
            "Yes. Replacing an existing apron still goes through the Right-of-Way Use Application and its pre-pour and final inspections, even when the private portion of the driveway isn't being touched."
        ),
    ],
    "sources": SRC,
}

# 2. paver-driveways -----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Windermere, FL – Apron Specs",
    "meta": "Paver driveway installers in Windermere, FL: the town's ASTM C902 and ribbon-curb apron spec where pavers meet a paved street, Oct. 2026.",
    "h1": "Paver Driveway Installation in Windermere",
    "lede": capsule(
        "A paver driveway in Windermere runs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026. Where the driveway meets a paved street, the town's own Right-of-Way "
        "spec calls for either an ASTM C902 paver apron inside a ribbon curb or a short concrete transition, a detail that changes depending on which of Windermere's streets a given lot actually fronts."
    ),
    "sections": [
        (
            "Pavers get their own apron standard, separate from poured concrete",
            "<p>Windermere's Right-of-Way Use Application spells out two paths for a paver apron: the pavers themselves meeting ASTM C902 inside a 1-foot-wide, 6-inch-thick ribbon curb, or, where there's no "
            "sidewalk, built to FDOT Section 526 instead " + src("windermere-row-app", "Windermere ROW Use Application") + ". Where that paver driveway ties into a paved road, the strip from the edge of "
            "pavement to the property line still has to be 6 inches of concrete rather than pavers all the way to the street " + src("windermere-row-app") + ". " +
            cs("windermere", "concrete-driveways", "A plain concrete driveway") + " skips that second material transition entirely.</p>"
        ),
        (
            "Most of Windermere's own streets aren't the paved kind that spec assumes",
            "<p>Main Street and Sixth Avenue carry Windermere's through traffic and are paved, but most of the town's residential grid stayed sand or brick by the town's own choice " +
            ext(WIKI_WINDERMERE, "Wikipedia, Windermere, Florida") + ". A paver driveway fronting one of those unpaved side streets isn't tying into the same curb-and-pavement edge the Right-of-Way "
            "application describes, so PDCS is worth a call before the apron design is finalized on a lot that doesn't front Main Street or Sixth Avenue. The private portion of the driveway, back from the "
            "street edge, follows the same base and bedding-sand work regardless of which street it meets.</p>"
        ),
    ],
    "scenario": (
        "A paver driveway meeting a paved street, worked out in square feet",
        "<p>Say a 22 by 42 foot paver driveway, 924 square feet, fronts a paved stretch near Main Street, where the apron has to carry that 6-inch concrete transition for roughly the first 15 feet back from "
        "the road. Pricing the full driveway at " + price("paver-driveway") + " per " + per("paver-driveway") + " puts the job between $9,240 and $27,720, tightening to about $11,080 to $18,480 in the typical "
        + price("paver-driveway", typical=True) + " band. The concrete transition strip adds a second material and a second inspection point to the job that a driveway fronting one of Windermere's sand "
        "streets wouldn't necessarily carry.</p>"
    ),
    "faqs": [
        faq(
            "Do Windermere's paver driveways need a concrete strip at the street?",
            "Only where the driveway meets a paved road. The town's spec then calls for 6 inches of concrete from the edge of pavement to the property line, with the pavers themselves built to ASTM C902 inside a ribbon curb, or to FDOT Section 526 where there's no sidewalk."
        ),
        faq(
            "Does a paver driveway need a different review than concrete in Windermere?",
            "No, both go through the same Right-of-Way Use Application for the portion crossing into the public strip, with the paver apron following its own material spec rather than the concrete one."
        ),
        faq(
            "Are all of Windermere's streets paved?",
            "No. Main Street and Sixth Avenue are paved through routes, but most residential streets in town stayed sand or brick, which changes what a driveway apron is actually tying into at the road edge."
        ),
    ],
    "sources": SRC,
}

# 3. concrete-patios -------------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Windermere, FL – Impervious Cap",
    "meta": "Concrete patio contractors in Windermere, FL: why a patio counts fully against the town's 0.45 impervious surface ratio, October 2026.",
    "h1": "Building a Concrete Patio in Windermere",
    "lede": capsule(
        "A concrete patio in Windermere runs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. The town's land development code names patios directly inside its 0.45 "
        "impervious surface ratio, so a backyard addition is measured against the same lot-wide cap as the driveway and the pool deck, not against a separate allowance of its own."
    ),
    "sections": [
        (
            "A patio is named outright in the 0.45 cap, not folded in by inference",
            "<p>Windermere's code defines impervious surface as including 'buildings, accessory structures, swimming pools, patios, decks, driveways, parking areas,' with the residential maximum set at 0.45 "
            "of the lot " + src("windermere-isr", "Windermere LDC, impervious surface") + ". A patio addition behind a house that already carries a full footprint and a screened lanai can run into that "
            "ceiling faster than the square footage alone suggests, since every other paved feature on the same lot is drawing from the identical 45 percent. Checking a current survey against that figure "
            "before the forms go up is the step that avoids a design that has to shrink mid-project.</p>"
        ),
        (
            "A low lot near the lakes changes which way the slab has to pitch",
            "<p>A backyard running down toward Lake Down or Lake Butler rarely stays flat all the way to the water, so a patio there needs its slope checked against the yard's real grade rather than "
            "assumed level. " + svc("concrete-pool-decks", "A concrete pool deck") + " on the same lot works through an identical grading question, since both features are shedding storm runoff toward "
            "the same low ground near the shoreline either way.</p>"
        ),
    ],
    "scenario": (
        "A lanai patio addition, worked out in square feet",
        "<p>Say a Windermere household extends a screened lanai with a 14 by 25 foot slab, 350 square feet, on a lot where the house and the existing driveway already sit close to the town's 0.45 "
        "impervious ceiling. Multiplying that footage by " + price("concrete-patio") + " per " + per("concrete-patio") + " puts the addition between $2,100 and $4,550, settling nearer $2,450 to $3,500 inside the typical "
        + price("concrete-patio", typical=True) + " band for a broom finish. Before the forms go up, that 350 square feet gets weighed against the lot's current impervious total instead of priced in "
        "isolation, since every other paved feature on the property is drawing from that identical 45 percent.</p>"
    ),
    "faqs": [
        faq(
            "Does a concrete patio count against Windermere's impervious surface limit?",
            "Yes. The town's code names patios directly inside its definition of impervious surface, capped at 0.45 of the lot, alongside the driveway, pool deck and any other paved feature on the property."
        ),
        faq(
            "Does a patio in Windermere need its own permit from PDCS?",
            "Private-property patio work is reviewed through the town's building office, PDCS, separately from the Right-of-Way Use Application that covers driveway aprons in the public strip."
        ),
        faq(
            "Why does a patio near Lake Down or Lake Butler need extra grading?",
            "Because the lot isn't flat all the way to the shoreline. A patio near either lake has its pitch checked against the actual grade down to the water so runoff clears the house rather than pooling against it."
        ),
    ],
    "sources": SRC,
}

# 4. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Windermere, FL – Town vs. County",
    "meta": "Paver patio installers in Windermere, FL: the town's 0.45 cap versus Orange County's 40% open-space rule for unincorporated lots, Oct. 2026.",
    "h1": "Paver Patios and Walkways in Windermere",
    "lede": capsule(
        "A paver patio in Windermere runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. Which rulebook applies depends on the exact address: the town's own 0.45 impervious "
        "cap inside the line, or Orange County's separate open-space standard on the many Windermere-addressed lots, Isleworth among them, that actually sit in the unincorporated county."
    ),
    "sections": [
        (
            "Two different numbers, measured two different ways",
            "<p>Inside the town, a paver patio counts toward Windermere's 0.45 impervious surface ratio, the same cap that covers the driveway and the pool deck " +
            src("windermere-isr", "Windermere LDC, impervious surface") + ". Step into unincorporated Orange County and the county's own residential-paver permit instead requires at least 40 percent of the "
            "lot to stay as private open space, reviewed with a $38 permit fee and a $38 Development Engineering review fee rather than PDCS's Right-of-Way form " +
            src("orange-residential-pavers", "Orange County, Residential Pavers") + ". Those two figures aren't simply inverses of each other, so a patio sized against one rule can still need rechecking "
            "under the other.</p>"
        ),
        (
            "Isleworth is the clearest example of that split",
            "<p>" + ext(WIKI_ISLEWORTH, "Isleworth") + " markets itself as part of Windermere and sits along Lake Down's south shore, yet it remains unincorporated Orange County rather than inside the "
            "town's own boundary, a distinction a 2007 annexation dispute over its tax base put on the public record. A paver patio there goes through the county's process, not PDCS, even though the "
            "mailing address reads Windermere. " + svc("paver-driveways", "A paver driveway") + " on the same kind of lot faces that identical jurisdiction question first.</p>"
        ),
    ],
    "scenario": (
        "A paver patio on an unincorporated Windermere-area lot, worked out in square feet",
        "<p>Say a 300 square foot paver patio is going in behind a home on a Windermere-addressed lot that actually sits in unincorporated Orange County, reviewed under the county's $38-plus-$38 "
        "residential-paver fee rather than the town's application. At " + price("paver-patio") + " per " + per("paver-patio") + ", the patio itself runs $3,000 to $5,100, or about $3,600 to $4,800 in the "
        "typical " + price("paver-patio", typical=True) + " band. Confirming which side of the town line the parcel sits on, before the application is filed, is the step that decides whether the 40 "
        "percent open-space rule or the town's 0.45 cap actually governs the design.</p>"
    ),
    "faqs": [
        faq(
            "Is Isleworth inside the Town of Windermere?",
            "No. Isleworth carries a Windermere mailing address and sits along Lake Down, but it remains unincorporated Orange County, a status a 2007 annexation dispute over its tax base made public. Permitting there runs through the county, not the town's PDCS office."
        ),
        faq(
            "What open-space rule applies to a paver patio outside the Windermere town line?",
            "Orange County's own residential-paver permit requires at least 40 percent of the lot to stay as private open space, reviewed with a $38 permit fee plus a $38 engineering-review fee."
        ),
        faq(
            "Does a paver patio inside Windermere follow the same cap as a driveway?",
            "Yes. Both count toward the town's single 0.45 impervious surface ratio, which covers patios, decks, pools, driveways and parking areas together rather than giving each one its own allowance."
        ),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Windermere, FL – Lake Lots",
    "meta": "Concrete pool deck builders in Windermere, FL: grading toward Lake Down and Lake Butler, and the town's 0.45 impervious rule, Oct. 2026.",
    "h1": "Concrete Pool Deck Installation in Windermere",
    "lede": capsule(
        "A concrete pool deck in Windermere runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. The town's code names swimming pools directly inside its "
        "0.45 impervious surface cap, and on a lot near the Butler Chain, the deck's slope away from the house matters as much as that square-footage math."
    ),
    "sections": [
        (
            "Swimming pools are named outright in the town's 0.45 cap",
            "<p>Windermere's impervious surface definition lists 'swimming pools' alongside patios, decks and driveways under the same 0.45 lot-wide maximum " +
            src("windermere-isr", "Windermere LDC, impervious surface") + ". A pool deck addition on a lot that already carries a full house footprint and a wide driveway is drawing from that same 45 "
            "percent, so the deck's finished size is worth checking against a current survey rather than a dated one from when the house was built.</p>"
        ),
        (
            "A lot near Lake Down or Lake Butler needs its own grading logic",
            "<p>Lake Down, the Butler Chain's 885-acre headwater lake, runs along Windermere's western shore, with Lake Butler forming the opposite edge of the same narrow stretch of town " +
            ext(WIKI_LAKE_DOWN, "Wikipedia, Lake Down") + ". On a deck close to either shoreline, the pour has to shed water away from the house and toward the yard's actual low point rather than toward "
            "the lake bank itself, since that bank is part of a chain carrying Florida's Outstanding Florida Water protection " + ext(OFW_FACTSHEET, "FDEP, Outstanding Florida Waters fact sheet") + ". " +
            svc("retaining-walls", "A retaining wall") + " holding back fill at the same bank answers to that same water-quality concern.</p>"
        ),
    ],
    "scenario": (
        "A pool deck near Lake Down, worked out in square feet",
        "<p>Say a 550 square foot pool deck goes in around a screened cage on a lot close enough to Lake Down that the backyard slopes gently toward the shoreline. Pricing that at " +
        price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " puts the job between $2,750 and $8,250, or about $3,850 to $6,600 in the typical " + price("concrete-pool-deck", typical=True) +
        " band for a textured, slip-resistant surface. Because the lot already slopes toward the lake, the deck's own pitch gets set to carry runoff into the yard's drainage rather than straight down the "
        "bank, and the 550 square feet still counts against the same 0.45 impervious cap the house and driveway already draw from.</p>"
    ),
    "faqs": [
        faq(
            "Does a pool deck count against Windermere's impervious surface limit?",
            "Yes. The town's code names swimming pools directly inside its 0.45 impervious surface ratio, the same lot-wide cap that covers the driveway, patios and decks."
        ),
        faq(
            "Does a pool deck near Lake Down need extra review?",
            "The deck itself goes through the same PDCS permitting as any other pool deck in town, but its grading has to account for the slope toward the shoreline on a lot near Lake Down or Lake Butler, part of a chain the state protects as an Outstanding Florida Water."
        ),
        faq(
            "Is there a separate state permit for a pool deck near the Butler Chain of Lakes?",
            "Not simply for being near the lakes. The Outstanding Florida Water designation limits activities that would lower water quality in the chain itself, which matters more for work at the water's edge, like a seawall or retaining wall, than for a deck set back from the bank."
        ),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ----------------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Windermere, FL – Butler Chain",
    "meta": "Pool deck paver and travertine installers in Windermere, FL: building near a lake the state protects as an Outstanding Florida Water, Oct. 2026.",
    "h1": "Travertine and Paver Pool Decks in Windermere",
    "lede": capsule(
        "Pool deck pavers or travertine in Windermere run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. A lakefront deck overlay on the Butler Chain is built "
        "next to water Florida protects as an Outstanding Florida Water, which raises the stakes on keeping runoff and bedding sand out of the lake during the job, not just on the finished look."
    ),
    "sections": [
        (
            "Building next to an Outstanding Florida Water changes the job site, not the material",
            "<p>The Butler Chain of Lakes, the connected lake system Windermere sits among, on the isthmus between Lake Down and Lake Butler " + ext(WIKI_WINDERMERE, "Wikipedia, Windermere, Florida") + ", carries Florida's Outstanding Florida Water "
            "designation, a protection tier meant to stop new work from lowering a waterbody's existing quality " + ext(OFW_FACTSHEET, "FDEP, Outstanding Florida Waters fact sheet") + ". A travertine or "
            "paver overlay on a deck close to that shoreline still uses the same base, bedding sand and edge restraint as any other job, but keeping bedding sand, demolition debris and wash water out of "
            "the lake during construction matters more here than on a yard a few streets back from the water.</p>"
        ),
        (
            "The deck's own footprint still answers to the town's 0.45 cap",
            "<p>Windermere's impervious surface rule covers 'swimming pools' and the paved area around them inside its single 0.45 ceiling " + src("windermere-isr", "Windermere LDC, impervious surface") +
            ", so overlaying an old concrete deck in travertine without changing its footprint doesn't add new impervious area, but widening it toward the lake does. " +
            svc("concrete-pool-decks", "A poured concrete deck") + " on the same lot faces an identical footprint question, regardless of which surface finish gets picked.</p>"
        ),
    ],
    "scenario": (
        "A travertine overlay near the Butler Chain, worked out in square feet",
        "<p>Say a 680 square foot concrete pool deck near Lake Down is ready for a travertine overlay, with the yard sloping gently toward the shoreline about 40 feet from the pool cage. Pricing the "
        "overlay at " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " runs $8,160 to $20,400, tightening to roughly $9,520 to $14,960 in the typical " +
        price("pool-deck-pavers", typical=True) + " range once the stone and pattern are picked. Because the lot sits inside the Butler Chain's protected boundary, the crew plans where wash water and "
        "old demolition material go before the first paver comes up, rather than routing it toward the lake by default.</p>"
    ),
    "faqs": [
        faq(
            "Does building near the Butler Chain of Lakes require a special state permit for a pool deck overlay?",
            "Not simply for the overlay itself. The Outstanding Florida Water designation targets activities that would lower the chain's water quality, which matters most for work happening at or past the water's edge rather than a deck resurfacing set back from the shoreline."
        ),
        faq(
            "Why does job-site runoff matter more on a Butler Chain lot?",
            "Because the lakes carry Florida's highest water-quality protection tier. Keeping bedding sand, wash water and demolition debris from washing toward the shoreline during the job matters more here than it would on a yard well back from any lake."
        ),
        faq(
            "Does overlaying an existing pool deck in travertine change its impervious footprint in Windermere?",
            "Not if the deck's edges stay where they are. Widening the deck toward the lake while overlaying it does add new area against the town's 0.45 impervious cap, even though the overlay material itself doesn't."
        ),
    ],
    "sources": SRC,
}

# 7. stamped-concrete -------------------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Windermere, FL – Main Street",
    "meta": "Stamped concrete contractors in Windermere, FL: pattern choices near the town's brick Main Street versus its sand side streets, Oct. 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Windermere",
    "lede": capsule(
        "Stamped concrete in Windermere runs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October 2026. Homes close to the town's brick-and-paved Main Street tend toward a "
        "quieter slate or ashlar pattern that reads at home next to that corridor, while houses on one of Windermere's sand side streets have more room to pick a bolder stamp."
    ),
    "sections": [
        (
            "Main Street's character shapes the pattern choice, not the permit",
            "<p>Main Street and Sixth Avenue are the paved, through-traffic corridors of a town where most other residential streets stayed sand or brick by the town's own maintenance decision " +
            ext(WIKI_WINDERMERE, "Wikipedia, Windermere, Florida") + ". A stamped driveway or walkway fronting that corridor sits against a more formal streetscape than one a block over on a quiet sand "
            "lane, which is less about any written rule and more about what actually looks settled next to the surrounding frontage. Nothing in the town's own code ties a specific pattern to any street, "
            "though, so the choice stays the homeowner's.</p>"
        ),
        (
            "The same 0.45 cap and Right-of-Way review apply regardless of the finish",
            "<p>A stamped driveway crossing into the public right-of-way still needs the same Right-of-Way Use Application as a plain pour " + src("windermere-row-app", "Windermere ROW Use Application") +
            ", and a stamped finish counts toward the town's 0.45 impervious surface ratio the same way a broom finish does " + src("windermere-isr", "Windermere LDC, impervious surface") + ". " +
            cs("windermere", "concrete-driveways", "A plain gray driveway") + " on the same lot goes through that exact same paperwork, which means the stamping itself changes the invoice, not the review path.</p>"
        ),
    ],
    "scenario": (
        "An entry walk sized against a brick-street frontage",
        "<p>Say a homeowner near Main Street wants 310 square feet of stamped concrete across a front walk and small entry pad, swapped out for a plain slab that no longer matches the block. Multiplying "
        "that by " + price("stamped-concrete") + " per " + per("stamped-concrete") + " works out to $2,480 up to $5,890, landing closer to $3,720 through $4,960 within the typical " +
        price("stamped-concrete", typical=True) + " range once a pattern is picked. Most homeowners this close to the brick corridor end up choosing a single, restrained color over a busier multi-tone "
        "stamp, simply because the louder option tends to pull the eye away from the street rather than sit comfortably beside it.</p>"
    ),
    "faqs": [
        faq(
            "Does Windermere have a rule about stamped-concrete patterns near Main Street?",
            "No specific rule was found tying a pattern to a particular street. The standard Right-of-Way Use Application and the town's 0.45 impervious cap apply the same way regardless of the finish chosen."
        ),
        faq(
            "What stamp pattern fits a lot close to Windermere's brick corridor?",
            "There's no requirement either way, but a restrained, single-color texture like slate tends to sit more comfortably next to a brick-and-paver streetscape than a bright, multi-tone cobble pattern built for a wide subdivision frontage."
        ),
        faq(
            "What drives the price difference between stamped and plain concrete in Windermere?",
            "The extra labor for stamping a pattern into the slab while it's still workable, plus an integral color and release agent, which together move the job above a flat gray pour even though the permitting steps underneath stay identical."
        ),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Walkways & Sidewalks in Windermere, FL – Sand Streets",
    "meta": "Concrete walkway and sidewalk contractors in Windermere, FL: tying a walkway into a sand street versus a paved one, as of October 2026.",
    "h1": "Concrete Sidewalks and Walkways in Windermere",
    "lede": capsule(
        "A concrete walkway or sidewalk section in Windermere runs " + price("concrete-walkway") + " per " + per("concrete-walkway") + " as of October 2026. Most of the town's residential streets are "
        "sand or brick rather than paved, so a walkway's edge treatment and drainage depend on which kind of street the lot actually fronts."
    ),
    "sections": [
        (
            "A walkway along a sand street answers to a different drainage picture",
            "<p>Outside the paved Main Street and Sixth Avenue corridors, most of Windermere's residential grid stayed unpaved by the town's own choice " + ext(WIKI_WINDERMERE, "Wikipedia, Windermere, Florida") + ", and a current pilot on "
            "Bessie and Butler streets is adding swales and a rain garden so stormwater sheets to the sides of the road instead of washing out the crown " +
            ext(CLICKORLANDO_DIRTROAD, "ClickOrlando, Windermere's dirt-road pilot") + ". A front walkway tying into one of those improved sections has to clear the new swale rather than the flat, worn "
            "edge an older sand street would have had, while a walkway along an untouched sand street still faces the kind of edge washout the town's own maintenance program is trying to fix.</p>"
        ),
        (
            "Only the piece that touches the street needs the town's sign-off",
            "<p>Most of a front walk, the stretch from the porch to the driveway, is private work that PDCS reviews separately from anything happening at the curb. The short run at the far end, "
            "wherever it actually meets the road, answers to the same Right-of-Way Use Application the town built for driveway aprons " + src("windermere-row-app", "Windermere ROW Use Application") +
            ". " + cs("windermere", "concrete-driveways", "A driveway apron") + " goes through that identical review for its own road-facing edge, whether the street it meets is Main Street's pavement "
            "or one of the town's sand lanes.</p>"
        ),
    ],
    "scenario": (
        "A front walkway replacement along a sand street, worked out in square feet",
        "<p>Say a 5 by 30 foot front walkway, 150 square feet, connects the driveway to the entry on a lot fronting one of Windermere's unpaved residential streets, crossing the sidewalk strip near the "
        "road. At " + price("concrete-walkway") + " per " + per("concrete-walkway") + ", that runs $1,050 to $2,550, or about $1,200 to $1,800 in the typical " + price("concrete-walkway", typical=True) +
        " band for a broom-finished walk. Where the walkway meets the sand street's edge, the crew checks whether that block has already been regraded to the town's newer crown-and-swale design or still "
        "carries the older flat profile before setting the final grade.</p>"
    ),
    "faqs": [
        faq(
            "Do Windermere's sand streets change how a front walkway is built?",
            "They can change the grading at the street edge. A block already rebuilt under the town's swale-and-crown drainage pilot sheds water differently than an older, flat sand street, so the walkway's edge is set against whichever profile that block actually has."
        ),
        faq(
            "Does a walkway crossing a Windermere sidewalk strip need a permit?",
            "Yes, the portion crossing into the public right-of-way goes through the same Right-of-Way Use Application the town requires for a driveway apron."
        ),
        faq(
            "Why is Windermere investing in drainage on Bessie and Butler streets?",
            "A roughly $1.4 million pilot project there is adding swales and a rain garden so stormwater runs to the sides of the road rather than down the crown, which has been causing washout on those unpaved streets."
        ),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Windermere, FL – Sheds & Pads",
    "meta": "Concrete slab contractors in Windermere, FL: PDCS review inside town versus Orange County's permit near Horizon West, October 2026.",
    "h1": "Concrete Slabs for Sheds, AC Pads and Parking in Windermere",
    "lede": capsule(
        "A shed pad, an AC slab or an RV parking strip in Windermere falls between " + price("concrete-slab") + " per " + per("concrete-slab") + " as of October 2026. Which office signs off on it "
        "depends on the exact parcel: PDCS checks it against the town's 0.45 impervious cap inside Windermere, while a lot on the unincorporated side toward Horizon West answers to Orange County instead."
    ),
    "sections": [
        (
            "A utility pad draws from the same 45 percent as everything else",
            "<p>Windermere's definition of impervious surface doesn't stop at driveways and patios; it names 'accessory structures' and 'parking areas' outright " +
            src("windermere-isr", "Windermere LDC, impervious surface") + ", which pulls a shed pad, an AC slab or an RV parking strip into the identical 0.45 ceiling. A homeowner adding one of these to "
            "a lot that already carries a full house footprint is spending from the same allowance the driveway and the pool deck already draw on, so pricing the pad against a current survey, rather than "
            "an old one, is what keeps the design from needing to shrink mid-project.</p>"
        ),
        (
            "Toward Horizon West, the same kind of slab answers to the county instead",
            "<p>Horizon West, the unincorporated special planning area bordering Windermere, sits under Orange County's own permitting rather than the town's " +
            src("ocfl-horizonwest", "Orange County, Horizon West") + ". The county's own guidance is direct about the underlying requirement: 'anytime you are pouring concrete or placing pavers, a permit "
            "is required' " + src("orange-do-i-need-permit", "Orange County, Do I Need a Permit") + ". A shed or parking pad on a lot that close to the Windermere line is worth a quick check on which "
            "jurisdiction's line it actually falls on before the forms are ordered.</p>"
        ),
    ],
    "scenario": (
        "A parking pad near the Horizon West boundary, worked out in square feet",
        "<p>Say a homeowner needs a 9 by 15 foot slab, 135 square feet, for a boat trailer tucked beside the garage on a lot sitting right where Windermere's edge meets unincorporated Horizon West. The "
        + price("concrete-slab") + " per " + per("concrete-slab") + " figure puts that pad at $540 to $1,350, narrowing to about $810 to $1,080 within the typical " + price("concrete-slab", typical=True) +
        " range for a 4-inch reinforced pour. A few feet one direction, the pad counts toward PDCS's 0.45 cap; a few feet the other, it instead answers to Orange County's general requirement that any "
        "poured concrete on the lot gets its own permit.</p>"
    ),
    "faqs": [
        faq(
            "Does a shed slab count toward Windermere's impervious surface limit?",
            "Yes, inside the town. The code's definition reaches accessory structures and parking areas by name, so a shed, AC or parking pad draws from the identical 0.45 ceiling as the driveway and the pool deck."
        ),
        faq(
            "Is a slab permitted differently near Horizon West than inside Windermere?",
            "Yes. Horizon West is unincorporated Orange County, so the county's own general permit requirement for pouring concrete or placing pavers applies there instead of the town's PDCS review."
        ),
        faq(
            "How do I find out which side of the Windermere line my lot is on?",
            "PDCS, the town's contracted building office, or Orange County's Division of Building Safety can both confirm jurisdiction from the address, which is worth doing before a slab is priced on a lot near the town's edge."
        ),
    ],
    "sources": SRC,
}

# 10. concrete-repair -----------------------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair in Windermere, FL – 1989-Era Slabs",
    "meta": "Concrete repair and resurfacing in Windermere, FL: why 1989-median driveways crack, and the county's spot on the state's sinkhole list, Oct. 2026.",
    "h1": "Concrete Driveway and Slab Repair in Windermere",
    "lede": capsule(
        "Concrete repair and resurfacing in Windermere runs " + price("concrete-repair") + " per " + per("concrete-repair") + " as of October 2026. The town's median home dates to 1989, and population "
        "growth has stayed modest since 2020, so most cracking here traces to decades of ordinary wear on older slabs rather than fresh settlement on freshly filled lots."
    ),
    "sections": [
        (
            "A driveway from Windermere's median build year is pushing 35 years old",
            "<p>Windermere's median year structure built is 1989 " + src("acs-windermere", "Census Reporter, Windermere FL") + ", and the town grew only from 3,159 residents in the 2020 base count to an "
            "estimated 3,344 by July 2025 " + src("census-pep-v2025", "Census Bureau PEP, Vintage 2025") + ", a slower pace than several newer cities in the same unit. Thirty-five summers of expansion and "
            "contraction is a lot for one slab to absorb, and once a joint or crack has already been patched once, a second patch rarely lasts as long as simply resurfacing the whole panel would.</p>"
        ),
        (
            "Orange County is on the state's sinkhole-claims list, but settlement is still the usual culprit",
            "<p>Orange County is one of the eleven counties the Florida Senate flagged for the heaviest statewide sinkhole insurance claims in a 2010 review " +
            src("fl-senate-2011-104", "Florida Senate Interim Report 2011-104") + ", a different finding than some neighboring counties that didn't make that list. Florida's own geological survey still "
            "draws a clear line between a sudden cover-collapse sinkhole and the slower, far more common cover-subsidence kind " + src("fgs-sinkhole-faq", "FDEP/FGS Sinkhole FAQ") + ", and a dip near a "
            "35-year-old Windermere driveway reads far more like ordinary fill settlement than either category of sinkhole.</p>"
        ),
    ],
    "scenario": (
        "Patching a driveway built around the town's median year",
        "<p>Say a two-car driveway measuring 460 square feet, poured sometime close to 1989 when the town's typical home went up, has gone chalky and picked up a scatter of narrow surface cracks across "
        "both panels. Pricing a resurfacing overlay at " + price("concrete-repair") + " per " + per("concrete-repair") + " comes out to $1,380 through $4,600, settling closer to $1,840 and $3,220 inside "
        "the typical " + price("concrete-repair", typical=True) + " band, a fraction of what tearing out and re-pouring the whole slab at the higher " + price("concrete-driveway") + " per sq ft figure "
        "would cost. Which path actually makes sense turns on what the base underneath looks like once a panel or two gets opened up, not on the driveway's age by itself.</p>"
    ),
    "faqs": [
        faq(
            "Should I worry about cracking in an older Windermere driveway?",
            "Usually not right away. With the town's median home dating to 1989, scattered surface cracking and worn control joints are what three and a half decades of Florida sun and rain normally leave behind, not necessarily a sign the slab has failed."
        ),
        faq(
            "Is Orange County a sinkhole-prone area?",
            "It's among the eleven counties the Florida Senate flagged for the heaviest sinkhole insurance claims statewide in a 2010 review. Even so, the far more common explanation for a sunken slab is ordinary settlement, not either kind of sinkhole the state's geological survey tracks."
        ),
        faq(
            "Is resurfacing cheaper than full replacement for an older Windermere driveway?",
            "Per square foot, yes, but only when the subgrade under the existing slab is still sound. Once the base itself has shifted, resurfacing tends to crack again within a season or two, so opening up a panel to look is worth more than guessing from the home's age."
        ),
    ],
    "sources": SRC,
}

# 11. paver-sealing --------------------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing in Windermere, FL – Sand Street Dust",
    "meta": "Paver sealing and restoration in Windermere, FL: why proximity to the town's sand streets and lakes changes the cleaning cycle, Oct. 2026.",
    "h1": "Paver Sealing and Restoration in Windermere",
    "lede": capsule(
        "Cleaning, re-sanding and sealing pavers in Windermere runs " + price("paver-sealing") + " per " + per("paver-sealing") + " as of October 2026. A paver surface close to one of the town's unpaved "
        "sand streets collects more grit between cleanings than one set back from the road, which is a bigger factor here than it is in most of the unit's fully paved towns."
    ),
    "sections": [
        (
            "Sand streets kick up more grit than a paved road does",
            "<p>Most of Windermere's residential grid stayed sand or brick rather than paved " + ext(WIKI_WINDERMERE, "Wikipedia, Windermere, Florida") + ", and loose sand tracked by tires and foot "
            "traffic settles into paver joints faster near one of those streets than it would on a lot fronting a fully paved road elsewhere in the unit. That grit works its way between the joint sand "
            "and the sealer coat the same way wind-blown dust would anywhere else, just in heavier amounts on a lot close to an unpaved frontage, which is a reason to plan the cleaning cycle around the "
            "street itself and not just the paver's age.</p>"
        ),
        (
            "Proximity to the Butler Chain adds a second reason to keep wash water contained",
            "<p>The Butler Chain of Lakes carries Florida's Outstanding Florida Water designation " + ext(OFW_FACTSHEET, "FDEP, Outstanding Florida Waters fact sheet") + ", and on a lakefront or canal-side "
            "lot, the pressure-washing step ahead of sealing is run so wash water and old sealer residue don't drain straight toward the shoreline. " + svc("pool-deck-pavers", "A paver pool deck") +
            " near the same water faces that identical containment question during its own cleaning.</p>"
        ),
    ],
    "scenario": (
        "Resealing a paver patio near a sand street, worked out in square feet",
        "<p>Say a 400 square foot paver patio, set a short walk from one of Windermere's unpaved side streets, is due for a wash, a polymeric-sand refresh and a fresh seal coat. That footprint priced at " +
        price("paver-sealing") + " per " + per("paver-sealing") + " runs $600 to $1,300, or about $700 to $1,100 in the typical " + price("paver-sealing", typical=True) + " band, with any heavier grit "
        "buildup near the street edge pushing the cleaning time toward the higher end. Because the lot sits close to a sand street, the joints along that side tend to need a more thorough sweep before "
        "the new sand goes in than the joints on the patio's lake-facing side would.</p>"
    ),
    "faqs": [
        faq(
            "Do Windermere's sand streets affect how often pavers need resealing?",
            "They can affect how dirty the joints get between cleanings rather than the sealing interval itself. A paver surface close to one of the town's unpaved streets tends to collect more tracked-in sand and grit than one set back from the road."
        ),
        faq(
            "Does resealing pavers near the Butler Chain of Lakes need special precautions?",
            "The pavers themselves are cleaned and sealed the same way, but on a lakefront or canal-side lot, wash water and old sealer residue are kept from draining straight toward the shoreline, given the chain's Outstanding Florida Water protection."
        ),
        faq(
            "Is a permit required to reseal existing pavers in Windermere?",
            "No. Cleaning, re-sanding or sealing pavers that are already down isn't the kind of new construction the town's Right-of-Way or building review is built to cover."
        ),
    ],
    "sources": SRC,
}

# 12. retaining-walls -----------------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Windermere, FL – County's 24-In Rule",
    "meta": "Retaining wall contractors in Windermere, FL: no town-published height threshold, versus Orange County's 24-inch engineering trigger, Oct. 2026.",
    "h1": "Retaining Walls for Windermere Yards",
    "lede": capsule(
        "Retaining wall construction in Windermere runs between " + price("retaining-wall") + " per " + per("retaining-wall") + " as of October 2026. The town itself publishes no specific height threshold "
        "for when a wall needs engineered plans, unlike the unincorporated parts of Orange County nearby, where a wall over 24 inches resisting lateral loads needs a sealed design."
    ),
    "sections": [
        (
            "Windermere itself leaves the wall threshold unanswered",
            "<p>No town-published rule sets a specific height at which a retaining wall in Windermere needs engineered drawings, so PDCS, at 407-277-9795, is the call to confirm what a given wall actually "
            "needs before a design is finalized " + src("windermere-pdcs", "PDCS, Windermere") + ". That's a real gap compared with some of the unit's other cities, which publish an exact number, and it "
            "means a wall that would clearly need engineering under a neighboring jurisdiction's rule still has to be checked directly with the town rather than assumed.</p>"
        ),
        (
            "Orange County's own threshold is explicit, for the unincorporated lots nearby",
            "<p>For lots in unincorporated Orange County, Horizon West and the areas around Isleworth among them, signed and sealed engineering is required for a retaining wall that holds back more than 48 "
            "inches of unbalanced fill without support at the top, or one over 24 inches that resists lateral loads in addition to the soil itself " +
            src("orange-res-plan-guide", "Orange County, A Guide for Residential Plan Approval") + ". " + svc("concrete-pool-decks", "A pool deck") + " built up against that same kind of wall, on a sloped "
            "lot near one of the lakes, is planned around whichever threshold actually applies to that parcel.</p>"
        ),
    ],
    "scenario": (
        "A low seat wall near the Windermere line, worked out in square feet",
        "<p>Say a terraced planting bed at the edge of a patio needs a block wall running 35 feet long and standing 2 feet tall, 70 square feet of wall face once multiplied out. Applying " +
        price("retaining-wall") + " per " + per("retaining-wall") + " to that area puts the job in the range of $1,050 to $2,800, or roughly $1,400 to $2,450 in the typical " +
        price("retaining-wall", typical=True) + " band, before drainage behind the wall is figured in. At 2 feet, that wall stays under Orange County's 24-inch lateral-load threshold on an unincorporated "
        "lot, though confirming the same project's requirements with PDCS is still the step inside the Windermere town line.</p>"
    ),
    "faqs": [
        faq(
            "Does Windermere publish a height limit for when a retaining wall needs an engineer?",
            "No specific threshold was found on the town's own permitting material. PDCS, the town's contracted building office, is the office to confirm what a given wall height and load actually requires."
        ),
        faq(
            "What height triggers engineered plans for a retaining wall near Horizon West?",
            "In unincorporated Orange County, a wall retaining more than 48 inches of unbalanced fill without support at the top, or one over 24 inches resisting lateral loads beyond the soil itself, needs signed and sealed engineering."
        ),
        faq(
            "Does a low wall near Lake Down or Lake Butler need extra review?",
            "Any wall holding fill at the water's edge on the Butler Chain is built with the lakes' Outstanding Florida Water protection in mind, keeping disturbed soil and wash water from reaching the shoreline during construction, separate from whatever height threshold applies to the wall itself."
        ),
    ],
    "sources": SRC,
}

# 13. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Windermere, FL – Lake Setback",
    "meta": "Artificial turf installers in Windermere, FL: the state's 10-foot Butler Chain setback and Orange County's normal watering schedule, Oct. 2026.",
    "h1": "Artificial Turf for Windermere Yards",
    "lede": capsule(
        "Artificial turf installation in Windermere is priced between " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October 2026. Orange County still runs on SJRWMD's normal "
        "twice-a-week watering schedule rather than Lake County's emergency order, and near the Butler Chain of Lakes, the state's turf rule keeps installed turf at least 10 feet from the water."
    ),
    "sections": [
        (
            "Orange County's watering calendar is the normal one, not the emergency order",
            "<p>SJRWMD's current restrictions page keeps all of Orange County on the district's standard, year-round schedule rather than the Phase III emergency order limiting Lake County to a single "
            "watering day a week " + src("sjrwmd-watering", "SJRWMD Watering Restrictions") + ". That gives new sod in Windermere more recovery time between waterings than sod planted under the stricter "
            "neighboring order would get, which narrows, but doesn't close, the maintenance gap " + svc("artificial-turf", "artificial turf") + " closes entirely once it's installed and rinsed in.</p>"
        ),
        (
            "Florida's own turf rule won't let it touch the water's edge",
            "<p>The state's rule for synthetic turf keeps the installed surface 10 feet off a lake, pond or canal bank, a distance that only drops away where a seawall has replaced the open shoreline " +
            src("dep-rule", "Florida Administrative Code, Rule 62-308.100") + ". Underneath, no irrigation line runs beneath the turf itself, and the infill goes down over a washed-stone base instead of "
            "whatever soil was there before " + src("dep-rule") + ". On a lot fronting Lake Down, Lake Butler or any other link in the chain " + ext(WIKI_WINDERMERE, "Wikipedia, Windermere, Florida") +
            ", that 10-foot line is paced off from the water itself, not from wherever a fence happens to sit. Statewide, a 2025 law caps how aggressively a city or county can regulate residential turf "
            "beyond that " + src("fs125572", "Florida Statutes §125.572") + ", though a homeowners association can still set its own look-and-feel standard on top of it.</p>"
        ),
    ],
    "scenario": (
        "Turf on a lot near the Butler Chain, worked out in square feet",
        "<p>Say a backyard running down toward one of the Butler Chain's lakes measures 540 square feet inside the fence, and pulling the turf layout back 10 feet from the water's edge trims that to "
        "roughly 470 square feet of actual installed area. Figured against " + price("artificial-turf") + " per " + per("artificial-turf") + ", the job prices out to $4,700 up to $11,750, tightening "
        "toward $5,640 and $8,460 within the typical " + price("artificial-turf", typical=True) + " range depending on pile height and backing. With the lot sloping toward open water, the crew works out "
        "the buffer line first and the grading second, rather than cutting the base to the fence line and adjusting afterward.</p>"
    ),
    "faqs": [
        faq(
            "Is Windermere under the state's emergency watering order?",
            "No. Orange County, Windermere included, stays on SJRWMD's normal twice-a-week schedule, separate from the Phase III emergency order that limits Lake County to a single watering day a week."
        ),
        faq(
            "How close to the Butler Chain of Lakes can artificial turf be installed?",
            "The state keeps installed turf 10 feet off the bank of any lake, pond or canal, counted from the shoreline itself rather than a fence line. A seawall is the one condition that drops the distance away entirely."
        ),
        faq(
            "Can a homeowners association in the Windermere area set its own turf rules?",
            "Yes, within limits. A 2025 state law caps how far a city or county government can go in regulating residential turf, but that cap doesn't reach private community design standards, so checking with the specific association still matters."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
