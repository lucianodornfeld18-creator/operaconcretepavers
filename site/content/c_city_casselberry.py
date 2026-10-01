# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "casselberry"

GEN_URL = "https://www.casselberry.org/34/General-Information"
BLDG_URL = "https://www.casselberry.org/668/Building-Division"
ISR_URL = "https://www.zoneomics.com/code/casselberry-FL/chapter_2"
ISR_MUNI_URL = "https://library.municode.com/FL/Casselberry/codes/Code_of_Ordinances?nodeId=PTIIIUNLADERE_CHIIDIGERE"
LAKEKATHRYN_URL = "https://seminole.wateratlas.usf.edu/waterbodies/lakes/7590/lake-kathryn"
LAKECONCORD_URL = "https://seminole.wateratlas.usf.edu/waterbodies/lakes/7528/lake-concord"
CR_POP_URL = "http://censusreporter.org/profiles/16000US1211050-casselberry-fl/"
CR_YEAR_URL = "https://api.censusreporter.org/1.0/data/show/latest?table_ids=B25035&geo_ids=16000US1211050"

SRC = [
    ("City of Casselberry, General Information", GEN_URL),
    ("City of Casselberry, Building Division", BLDG_URL),
    ("Casselberry Zoning Ordinance Ch. II, Table 2-5.4 (via Municode)", ISR_MUNI_URL),
    ("Seminole County Water Atlas, Lake Kathryn", LAKEKATHRYN_URL),
    ("Seminole County Water Atlas, Lake Concord", LAKECONCORD_URL),
    ("Census Reporter, Casselberry, FL", CR_POP_URL),
    ("Census Reporter API, Casselberry median year structure built (B25035)", CR_YEAR_URL),
    "sjrwmd-watering", "dep-rule", "fs125572", "fs720-3045", "nrcs-myakka-osd",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("A $100 driveway permit through the city, not through Seminole County",
        f"<p>Casselberry is its own incorporated city inside Seminole County, so a driveway, slab or paver job here is reviewed by the city's Building Division at 95 Triplet Lake Drive rather than the county's development office; a driveway permit runs a flat $100 "
        f"({ext(BLDG_URL, 'City of Casselberry, Building Division')}). Addresses just outside city limits fall under Seminole County's own driveway construction application instead, a separate process handled out of a different office "
        f"({post('seminole-county-driveway-patio-permits', 'detailed in our Seminole County permit guide')}). Either way, {svc('concrete-driveways', 'a concrete driveway')} or {svc('paver-driveways', 'a paver driveway')} needs that approval before the first truck shows up.</p>"),
    sec("Half the lot, under the city's own coverage table",
        f"<p>Casselberry's zoning code sets impervious-surface-and-open-space ratios by district in Table 2-5.4; the city's single-family zones, R-8, R-9 and R-12.5, cap impervious coverage at 50 percent of the lot with the other half held as open space "
        f"({ext(ISR_MUNI_URL, 'Casselberry Zoning Ordinance Ch. II')}). A house, driveway, {svc('concrete-patios', 'patio')} and pool deck are all counted toward that single ceiling, so a lot that already carries a full footprint has less room than the driveway's own size might suggest.</p>"),
    sec("More than two dozen lakes inside an 8-square-mile city",
        f"<p>Casselberry's own description of itself counts more than two dozen lakes and ponds within roughly 8 square miles, Lake Howell the largest, with the Triplet Chain, Lake Kathryn and Lake Concord among the named waterbodies that give the city its long-running \"City of Lakes\" reputation "
        f"({ext(GEN_URL, 'City of Casselberry, General Information')}). Lake Concord alone covers about 20 acres, and a blockhouse built on its shore in 1849 is one of the area's earliest recorded structures "
        f"({ext(LAKECONCORD_URL, 'Seminole County Water Atlas, Lake Concord')}). That density of shoreline puts a meaningful share of Casselberry lots within reach of the state's water-body setback rules the moment turf or a seawall-adjacent patio comes up.</p>"),
    sec("A city built mostly around 1983, on sandy flatwoods ground",
        f"<p>Casselberry's American Community Survey estimate counts 30,135 residents, with a median year of home construction of 1983 "
        f"({ext(CR_POP_URL, 'Census Reporter, Casselberry, FL')}; {ext(CR_YEAR_URL, 'Census Reporter API, B25035')}). Much of that housing sits on Myakka soil, Florida's official state soil and one of the most common series in the flatwoods belt running through this part of Seminole County, ground the USDA describes as very poorly to poorly drained with slow internal movement of water "
        f"({src('nrcs-myakka-osd', 'NRCS soil survey, Myakka series')}). A four-decade-old slab on soil that drains that slowly is a reasonable candidate for {svc('concrete-repair', 'resurfacing')}, independent of how well the original pour was finished.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Who handles a driveway permit in Casselberry?",
        f"The city's own Building Division, at 95 Triplet Lake Drive, reviews driveway permits inside Casselberry's limits for a flat $100 fee. An address just outside the city line instead goes through Seminole County's separate driveway application "
        f"({ext(BLDG_URL, 'City of Casselberry, Building Division')})."),
    faq("How much of a Casselberry lot can be covered in hard surface?",
        "In the city's single-family zoning districts, R-8, R-9 and R-12.5, the zoning code caps impervious coverage at 50 percent of the lot, with house, driveway, patio and pool deck all counted toward that one limit."),
    faq("Why does Casselberry call itself a city of lakes?",
        "The city's own description counts more than two dozen lakes and ponds across roughly 8 square miles, with Lake Howell as the largest and the Triplet Chain, Lake Kathryn and Lake Concord among its named waterbodies."),
    faq("Does living near a Casselberry lake change what I can build?",
        "A lot that borders a lake or canal falls under the state's setback rules for artificial turf near water, and any patio or wall close to the shoreline is worth checking against those rules before a layout is finalized."),
    faq("How old is the typical driveway in Casselberry?",
        "The city's median home was built in 1983, so a large share of original driveways and patios are now past the 40-year mark, a point where cracking and resurfacing become routine rather than a sign of a bad original pour."),
    faq("What belongs in a solid concrete or paver quote in Casselberry?",
        f"A bid that already accounts for the city's $100 driveway permit, states plainly whether the job stays under the single-family zone's 50 percent coverage cap, and comes from a contractor you've checked through the state's license-verification tool. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our guide to choosing a concrete contractor')} covers the rest of what to look for."),
]

HUB = page("/casselberry-fl/", "city", "Concrete, Pavers & Turf Contractor in Casselberry, FL",
           "Concrete, pavers and turf in Casselberry, FL: the city's $100 driveway permit, a 50% coverage cap, and more than two dozen lakes, October 2026.",
           "Concrete, Pavers and Artificial Turf for Casselberry Homes",
           capsule(f"Opera builds concrete driveways, paver patios and artificial turf lawns across Casselberry, a Seminole County city of 30,135 residents known for the more than two dozen lakes inside its roughly 8 square miles. "
                   f"This October, a concrete driveway here costs {price('concrete-driveway')} per {per('concrete-driveway')}, and the city's own Building Division reviews the permit rather than Seminole County's office."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Casselberry",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/winter-springs-fl/", "Concrete, pavers and turf in Winter Springs"),
                    ("/longwood-fl/", "Concrete, pavers and turf in Longwood"),
                    ("/blog/seminole-county-driveway-patio-permits/", "Seminole County driveway and patio permits"),
                    ("/compare/concrete-vs-pavers/", "Concrete vs. pavers")],
           eyebrow="Concrete · Pavers · Turf in Casselberry, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Casselberry, FL – Permits",
    "meta": "Concrete driveway contractors in Casselberry, FL: the city's $100 flat permit fee, and the 50% single-family coverage cap, October 2026.",
    "h1": "Pouring a Concrete Driveway in Casselberry",
    "lede": capsule(f"Market pricing for a Casselberry concrete driveway runs {price('concrete-driveway')} per {per('concrete-driveway')}, current as of October 2026. "
                     "On top of that, the city charges a flat $100 for a driveway permit through its own Building Division, separate from whatever Seminole County charges just outside the city line."),
    "sections": [
        ("One flat fee, filed with the city rather than the county",
         f"<p>Inside Casselberry, a driveway permit is a flat $100 through the Building Division at 95 Triplet Lake Drive, open Monday through Thursday "
         f"({ext(BLDG_URL, 'City of Casselberry, Building Division')}). That single fee covers the driveway itself; it doesn't by itself clear a separate right-of-way sign-off if the apron ties into a city-maintained street, so it's worth confirming with staff whether a given lot needs both before the quote is finalized.</p>"),
        ("A 50 percent ceiling that counts everything hard on the lot",
         f"<p>Casselberry's single-family zones, R-8, R-9 and R-12.5, limit impervious coverage to 50 percent of the lot under the city's zoning table, with the driveway weighed against the same number as the house, any patio and the pool deck "
         f"({ext(ISR_MUNI_URL, 'Casselberry Zoning Ordinance Ch. II')}). On an older, smaller Casselberry lot, that ceiling can be the deciding factor on whether a two-car driveway is possible at full width or has to narrow somewhere along its run.</p>"),
    ],
    "scenario": ("A two-car driveway on a tight 1980s Casselberry lot, worked out in square feet",
                 f"<p>Say a Casselberry home from around the city's 1983 median construction year wants to go from a single 10 by 20 foot driveway, 200 square feet, to a full two-car width at 20 by 20 feet, 400 square feet. At {price('concrete-driveway')} per {per('concrete-driveway')}, that upgrade runs roughly $2,400 to $6,000 before the $100 permit fee, and because the house itself already sits close to the lot's 50 percent coverage line on a smaller older parcel, the extra 200 square feet is worth checking against the zoning table before the wider layout gets poured.</p>"),
    "faqs": [
        faq("What does a Casselberry driveway permit cost?",
            "A flat $100 through the city's Building Division, separate from any right-of-way sign-off that may apply where the apron meets a city street."),
        faq("Does a two-car driveway in Casselberry always fit under the coverage cap?",
            "Not automatically. The single-family zoning districts cap total impervious coverage at 50 percent of the lot, counting the house, driveway, patio and pool deck together, so a wider driveway on a smaller or older lot can run into that ceiling."),
        faq("Is the Casselberry driveway permit different from Seminole County's?",
            "Yes. Inside city limits, Casselberry's own Building Division reviews the permit. Just outside the city line, the same work falls under Seminole County's separate driveway construction application."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Casselberry, FL",
    "meta": "Paver patio installers in Casselberry, FL: the single-family 50% coverage cap, and building near one of the city's two dozen lakes, October 2026.",
    "h1": "Paver Patios and Walkways for a Casselberry Yard",
    "lede": capsule(f"A paver patio or walkway in Casselberry runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "The same 50 percent impervious cap that governs a driveway applies to a patio, and a sizable share of Casselberry lots sit close enough to one of the city's two dozen lakes for shoreline rules to matter."),
    "sections": [
        ("A patio is weighed against the identical lot-wide ceiling",
         f"<p>Casselberry's zoning table doesn't set a separate allowance for a patio; it's part of the same single-family coverage limit, 50 percent of the lot, that also includes the house, driveway and pool deck "
         f"({ext(ISR_MUNI_URL, 'Casselberry Zoning Ordinance Ch. II')}). Adding a {svc('paver-patios', 'paver patio')} on a lot that already has a full driveway and house footprint is sometimes the project that pushes the total closest to that number, which is why we run the math against the lot before sizing the layout.</p>"),
        ("Lakefront lots carry their own setback considerations",
         f"<p>With more than two dozen lakes packed into roughly 8 square miles, a larger-than-usual share of Casselberry addresses sit within reach of a shoreline, including smaller named lakes like Lake Kathryn at about 74 acres "
         f"({ext(LAKEKATHRYN_URL, 'Seminole County Water Atlas, Lake Kathryn')}). A paver patio or walkway going in close to open water doesn't trigger the same build rule as artificial turf, but a lakefront layout is still worth walking before a final design is drawn, since grading toward the shoreline affects drainage differently than grading toward a street.</p>"),
    ],
    "scenario": ("A lakeside patio near the coverage ceiling, worked out in square feet",
                 f"<p>Picture a Casselberry home near one of the city's smaller lakes adding a 15 by 18 foot paver patio, 270 square feet, off the back of the house, on a lot that already carries a full driveway and a modest addition. At {price('paver-patio')} per {per('paver-patio')}, that patio runs roughly $2,700 to $4,320, and on a lot already close to the single-family district's 50 percent ceiling, that square footage is checked against the zoning table before the final layout is cut.</p>"),
    "faqs": [
        faq("Does a Casselberry patio count toward the same limit as the driveway?",
            "Yes. The city's single-family zoning caps total impervious coverage, house, driveway, patio and pool deck together, at 50 percent of the lot, so a new patio is weighed against whatever coverage the property already has."),
        faq("Do lakefront lots in Casselberry have extra patio rules?",
            "A patio itself isn't subject to a special lakefront setback the way artificial turf near open water is, but grading and drainage near a shoreline lot are still worth reviewing on site before a final layout is set."),
        faq("How many lakes does Casselberry actually have?",
            "The city's own description counts more than two dozen lakes and ponds across about 8 square miles, with Lake Howell the largest and the Triplet Chain, Lake Kathryn and Lake Concord among the named waterbodies."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Casselberry, FL – Lake Rules",
    "meta": "Artificial turf installers in Casselberry, FL: the state's 10-foot lake setback, and why it matters in a city with two dozen-plus lakes, October 2026.",
    "h1": "Artificial Turf for Casselberry Yards",
    "lede": capsule(f"Artificial turf in Casselberry falls in the {price('artificial-turf')} {per('artificial-turf')} market range as of October 2026. "
                     "The state's turf-construction rule sets a 10-foot setback from most water bodies, a detail that matters more here than in a landlocked town, given how many Casselberry lots touch a lake."),
    "sections": [
        ("Why the water-body setback carries extra weight in a city of lakes",
         f"<p>Florida's Rule 62-308.100 keeps new turf at least 10 feet from a pond, lake or canal unless a seawall sits between the two, on top of requiring a washed base, natural infill and no buried irrigation line underneath "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). With more than two dozen named lakes inside roughly 8 square miles, that setback is a live measurement question on a meaningfully larger share of Casselberry yards than it would be in a town with one or two ponds "
         f"({ext(GEN_URL, 'City of Casselberry, General Information')}).</p>"),
        ("What state law does and doesn't let an HOA restrict",
         f"<p>F.S. 125.572 limits how far a local government can go in regulating residential turf once it meets the state's construction rule, and separately, F.S. 720.3045 keeps most homeowners' associations from blocking turf that isn't actually visible from the street or a neighboring lot, unless the association's own documents say otherwise "
         f"({src('fs125572', 'F.S. 125.572')}; {src('fs720-3045', 'F.S. 720.3045')}). Turf itself also drops off the twice-weekly SJRWMD irrigation calendar that governs sod across the rest of a Casselberry property "
         f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}).</p>"),
    ],
    "scenario": ("Turf going in near the edge of a Casselberry lake lot, worked out in square feet",
                 f"<p>Take a Casselberry backyard that slopes down toward one of the city's smaller lakes, where 450 square feet of lawn close to the shoreline keeps drowning out during the wet season. At {price('artificial-turf')} per {per('artificial-turf')}, that area runs roughly $4,500 to $8,100 to convert to turf, with the installer pulling the setback line 10 feet back from the water's edge before laying out the washed base, which on a narrow lakefront lot can trim the usable turf footprint more than the square-footage math alone would suggest.</p>"),
    "faqs": [
        faq("Does Casselberry's lake density change the turf setback rule?",
            "The 10-foot setback from a pond, lake or canal is set by state rule, not by the city, but because Casselberry has more than two dozen named lakes in a small area, the rule applies to a larger share of yards here than in most nearby towns."),
        faq("Can turf go right up to a Casselberry lake's edge if there's a seawall?",
            "The state rule's setback is waived specifically where a seawall separates the turf from the water, so a seawalled lot can generally run turf closer to the shoreline than an unwalled one."),
        faq("Does artificial turf near a Casselberry lake still need the SJRWMD watering schedule?",
            "No. Once a lawn is turf rather than irrigated sod, there's no sprinkler zone left for the district's twice-weekly schedule to apply to, regardless of how close the lot sits to the water."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
