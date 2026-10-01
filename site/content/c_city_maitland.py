# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "maitland"

PERMIT_URL = "https://www.itsmymaitland.com/428/Permitting-Information"
FEES_URL = "https://www.itsmymaitland.com/445/Building-and-Permitting-Fees"
LDC_URL = "https://library.municode.com/fl/maitland/codes/land_development_code?nodeId=PTIILADECO_ART3ZODI"
ART_CENTER_URL = "https://en.wikipedia.org/wiki/Maitland_Art_Center"
LAKEMAITLAND_URL = "https://orange.wateratlas.usf.edu/waterbodies/lakes/140454/lake-sybelia"
CR_POP_URL = "https://censusreporter.org/profiles/16000US1242575-maitland-fl/"
CR_YEAR_URL = "https://api.censusreporter.org/1.0/data/show/latest?table_ids=B25035&geo_ids=16000US1242575"

SRC = [
    ("City of Maitland, Permitting Information", PERMIT_URL),
    ("City of Maitland, Building and Permitting Fees", FEES_URL),
    ("City of Maitland Land Development Code, Art. 3 Zone Districts (via Municode)", LDC_URL),
    ("Wikipedia, Maitland Art Center", ART_CENTER_URL),
    ("Orange County Water Atlas, Lake Sybelia", LAKEMAITLAND_URL),
    ("Census Reporter, Maitland, FL", CR_POP_URL),
    ("Census Reporter API, Maitland median year structure built (B25035)", CR_YEAR_URL),
    "sjrwmd-watering", "dep-rule", "fs125572", "fs720-3045", "usgs-orange-gw",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("A driveway permit through Maitland's own Community Development office",
        f"<p>Maitland reviews driveway, right-of-way and paver work out of its Community Development Department at 1776 Independence Lane rather than through Orange County, with a driveway or sidewalk permit set at $175 and a stand-alone right-of-way permit at $125 "
        f"({ext(FEES_URL, 'City of Maitland, Building and Permitting Fees')}). Pavers placed inside the right-of-way need their own \"Paver Letter\" filed alongside the permit application, on top of the usual checklist, owner-builder affidavit and proof of insurance "
        f"({ext(PERMIT_URL, 'City of Maitland, Permitting Information')}). A Notice of Commencement has to be recorded before the first inspection on any job over $5,000, a threshold the city adopted effective October 1, 2023.</p>"),
    sec("Seventy percent of the lot, the same number across all three single-family zones",
        f"<p>Maitland's Land Development Code sets maximum impervious coverage at 70 percent of the lot in each of its single-family districts, RSF-1, RSF-2 and RSF-3, counting the house, {svc('concrete-driveways', 'driveway')}, pool, deck and {svc('paver-patios', 'patio')} together under one ceiling "
        f"({ext(LDC_URL, 'City of Maitland LDC, Art. 3 Zone Districts')}). A retaining wall permit runs $325 on its own schedule, separate from the driveway and right-of-way fees "
        f"({ext(FEES_URL, 'City of Maitland, Building and Permitting Fees')}).</p>"),
    sec("An artist colony turned museum, built around a sunset on Lake Sybelia",
        f"<p>Jules André Smith founded what's now the Maitland Art Center in 1937 after a 1932 sunset over Lake Sybelia convinced him to settle in Maitland instead of Miami; the Mayan Revival compound's 22 connected buildings earned a spot on the National Register of Historic Places on November 17, 1982, a dozen years after the city bought the dormant property and reopened it as a museum "
        f"({ext(ART_CENTER_URL, 'Wikipedia, Maitland Art Center')}). It sits a short walk from the lake that gave Smith his reason to stay in the first place.</p>"),
    sec("Twenty-one lakes, Lake Maitland largest at 451 acres",
        f"<p>Maitland counts 21 lakes inside its limits, Lake Maitland the biggest at 451 acres, with Lake Sybelia, Lake Minnehaha and Lake Lily among the smaller named waterbodies threaded through town "
        f"({ext(LAKEMAITLAND_URL, 'Orange County Water Atlas, Lake Sybelia')}). That much shoreline per square mile means a meaningful share of {svc('concrete-pool-decks', 'pool decks')}, patios and turf lawns in Maitland sit close enough to open water for the state's waterbody setback rule to apply.</p>"),
    sec("A city whose housing is younger than most of its Seminole County neighbors",
        f"<p>Maitland's American Community Survey estimate counts 19,469 residents, with a median year of home construction of 1996 "
        f"({ext(CR_POP_URL, 'Census Reporter, Maitland, FL')}; {ext(CR_YEAR_URL, 'Census Reporter API, B25035')}), newer housing stock than most of the Orange County towns covered here. Orange County's own groundwater studies describe the water table in this part of the county as tracking the land surface closely, running highest right after the wet season "
        f"({src('usgs-orange-gw', 'USGS, Hydrogeology of Orange County')}), a detail that matters for how a {svc('concrete-slabs', 'slab')} or driveway base drains near one of Maitland's many lakes.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Maitland or Orange County handle my driveway permit?",
        f"Maitland is an incorporated city, so its own Community Development Department reviews driveway, right-of-way and paver permits for $175 and $125 respectively, rather than Orange County's building division "
        f"({ext(FEES_URL, 'City of Maitland, Building and Permitting Fees')})."),
    faq("Do pavers in the Maitland right-of-way need anything beyond the regular permit?",
        "Yes. A paver installation inside the city's right-of-way needs a separate Paver Letter filed with the application, on top of the standard permit checklist and affidavits."),
    faq("How much of a Maitland lot can be covered in hard surface?",
        "All three single-family zoning districts, RSF-1, RSF-2 and RSF-3, cap impervious coverage at 70 percent of the lot, with the house, driveway, pool and patio counted together against that one limit."),
    faq("Why does Maitland have so many lakes close to residential lots?",
        "The city counts 21 lakes within its limits, Lake Maitland the largest at 451 acres, which means a larger-than-typical share of Maitland yards sit close enough to open water for the state's turf setback rule to matter."),
    faq("Is most of Maitland's concrete newer than nearby Winter Park's?",
        "Generally yes. Maitland's median home dates to 1996, roughly two decades newer than Winter Park's 1976 median, so less of the city's original flatwork has reached the point where resurfacing is routine."),
    faq("What should a Maitland homeowner confirm before hiring a contractor?",
        f"Ask whether the written bid already folds in the city's driveway or right-of-way fee, confirm a Paver Letter gets filed wherever the work touches the right-of-way, and look the business up on the state's license-search page before any deposit changes hands. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our concrete-contractor guide')} walks through the rest of a solid bid."),
]

HUB = page("/maitland-fl/", "city", "Concrete, Pavers & Turf Contractor in Maitland, FL",
           "Concrete, pavers and turf in Maitland, FL: a $175 driveway permit, 70% lot coverage cap, and 21 lakes including 451-acre Lake Maitland, October 2026.",
           "Concrete, Pavers and Artificial Turf for Maitland Homes",
           capsule(f"Opera pours concrete and lays pavers and artificial turf for Maitland, an Orange County city of 19,469 residents built around 21 lakes, Lake Maitland the largest at 451 acres. "
                   f"Pricing a Maitland concrete driveway this October lands in the {price('concrete-driveway')} per {per('concrete-driveway')} range, reviewed through the city's own $175 driveway permit rather than the county's."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Maitland",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/winter-park-fl/", "Concrete, pavers and turf in Winter Park"),
                    ("/orlando-fl/", "Concrete, pavers and turf in Orlando"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Orlando and Orange County permits"),
                    ("/compare/concrete-vs-pavers/", "Concrete vs. pavers")],
           eyebrow="Concrete · Pavers · Turf in Maitland, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Maitland, FL – Permits",
    "meta": "Concrete driveway contractors in Maitland, FL: the city's $175 permit, the 70% coverage cap, and the Notice of Commencement rule, October 2026.",
    "h1": "Pouring a Concrete Driveway in Maitland",
    "lede": capsule(f"A concrete driveway in Maitland runs {price('concrete-driveway')} per {per('concrete-driveway')}, the market range as of this October. "
                     "The city's own $175 driveway/sidewalk permit applies before the first form goes up, and a job over $5,000 needs a recorded Notice of Commencement ahead of the first inspection."),
    "sections": [
        ("A $175 city permit, plus the paperwork that comes with it",
         f"<p>Maitland's fee schedule lists a driveway or sidewalk permit at $175, filed through Community Development rather than Orange County's building division "
         f"({ext(FEES_URL, 'City of Maitland, Building and Permitting Fees')}). The application packet calls for the signed permit checklist, a Limited Power of Attorney form, an Owner/Builder Affidavit if applicable, and a Waiver of Limitations Affidavit, and any job over $5,000 needs a Notice of Commencement recorded before the first inspection "
         f"({ext(PERMIT_URL, 'City of Maitland, Permitting Information')}).</p>"),
        ("Seventy percent of the lot, driveway and all",
         f"<p>Maitland's RSF-1, RSF-2 and RSF-3 single-family districts share the same 70 percent impervious-coverage ceiling, with the driveway counted alongside the house, pool and any patio toward that one number "
         f"({ext(LDC_URL, 'City of Maitland LDC, Art. 3 Zone Districts')}). That's a noticeably higher cap than Winter Park's 50 percent next door, which gives a wider driveway more room on a comparably sized Maitland lot before the math gets tight.</p>"),
    ],
    "scenario": ("Widening a driveway on a 1990s-era Maitland lot, worked out in square feet",
                 f"<p>Say a Maitland home built close to the city's 1996 median construction year widens its original 10 by 20 foot driveway, 200 square feet, to a 20 by 24 foot two-car layout, 480 square feet. At {price('concrete-driveway')} per {per('concrete-driveway')}, that upgrade runs roughly $2,880 to $7,200 before the $175 permit fee, and because the contract value clears $5,000, a Notice of Commencement has to be recorded before the city's first inspection of the job.</p>"),
    "faqs": [
        faq("What does a Maitland driveway permit cost?",
            "The city's fee schedule lists a driveway/sidewalk permit at $175, filed with the Community Development Department rather than Orange County's office."),
        faq("When does a Maitland driveway job need a Notice of Commencement?",
            "Any job valued over $5,000 needs a recorded Notice of Commencement before the city's first inspection, a threshold Maitland adopted effective October 1, 2023."),
        faq("How much wider can a Maitland driveway be before hitting the coverage cap?",
            "All three single-family zoning districts allow up to 70 percent total impervious coverage, counting the driveway along with the house, pool and patio, a higher ceiling than several neighboring Orange County cities."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Maitland, FL",
    "meta": "Paver patio installers in Maitland, FL: the Paver Letter required in the right-of-way, and building near one of the city's 21 lakes, October 2026.",
    "h1": "Paver Patios and Walkways for a Maitland Home",
    "lede": capsule(f"A paver patio or walkway in Maitland runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "A patio on private property fits inside the same 70 percent coverage math as the rest of the lot, while a front walkway that steps into the right-of-way needs its own Paver Letter on file first."),
    "sections": [
        ("The right-of-way portion of a walkway carries its own paperwork",
         f"<p>Where a paver walkway extends from the porch into the strip the city maintains near the street, Maitland requires a Paver Letter submitted with the permit application, separate from the standard driveway or right-of-way review "
         f"({ext(PERMIT_URL, 'City of Maitland, Permitting Information')}). A patio that stays entirely on private property doesn't trigger that extra document, but the front few feet of a long walkway often do.</p>"),
        ("Seventy percent of the lot covers the patio too",
         f"<p>Maitland's single-family zoning code counts a {svc('paver-patios', 'paver patio')} toward the same 70 percent impervious ceiling that applies to the driveway, pool and house "
         f"({ext(LDC_URL, 'City of Maitland LDC, Art. 3 Zone Districts')}). On a lakefront lot near Lake Sybelia or one of Maitland's other 20 named lakes, that math is worth running before a patio is extended toward the water, since shoreline setbacks add another layer on top of the coverage limit.</p>"),
    ],
    "scenario": ("A paver walkway and patio combination near a Maitland lake, worked out in square feet",
                 f"<p>Consider a Maitland home near one of the city's smaller lakes relaying a 3-foot-wide, 25-foot front walkway, 75 square feet, that crosses into the right-of-way strip, plus a 200 square foot paver patio off the back porch. At {price('paver-patio')} per {per('paver-patio')} for the combined 275 square feet, that runs roughly $2,750 to $4,400, with the front walkway's Paver Letter filed before the crew starts on the right-of-way section.</p>"),
    "faqs": [
        faq("Does every Maitland paver walkway need a Paver Letter?",
            "Only the portion that extends into the city's right-of-way strip near the street. A walkway or patio that stays fully on private property doesn't trigger that requirement."),
        faq("Does a patio count toward Maitland's 70 percent coverage cap?",
            "Yes, a patio is weighed against the same lot-wide impervious ceiling as the driveway, pool and house in all three of the city's single-family zoning districts."),
        faq("Are there extra rules for a patio near one of Maitland's lakes?",
            "The coverage cap applies the same way regardless of lot location, but a patio extended toward open water is also worth checking against the state's shoreline setback rules that govern features like artificial turf."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Maitland, FL – Lake Setbacks",
    "meta": "Artificial turf installers in Maitland, FL: the state's 10-foot lake setback, relevant across the city's 21 named lakes, October 2026.",
    "h1": "Artificial Turf for Maitland Yards",
    "lede": capsule(f"Artificial turf in Maitland falls in the {price('artificial-turf')} {per('artificial-turf')} market range as of October 2026. "
                     "With 21 lakes inside the city, Lake Maitland alone covering 451 acres, the state's water-body setback for new turf is a routine site-plan question here rather than an edge case."),
    "sections": [
        ("A setback rule that touches more lots than usual",
         f"<p>Florida's Rule 62-308.100 keeps new artificial turf at least 10 feet from a pond, lake or canal unless the water is separated by a seawall, alongside requiring a washed base, natural infill and no in-ground irrigation beneath the turf itself "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). In a city built around 21 named lakes "
         f"({ext(LAKEMAITLAND_URL, 'Orange County Water Atlas, Lake Sybelia')}), that measurement comes up on a larger share of backyard turf jobs than it would in a town with only one or two ponds.</p>"),
        ("What the law leaves to the HOA, and what it takes away",
         f"<p>F.S. 125.572 caps how far a city can push its own turf restrictions once an install meets the state construction rule, while F.S. 720.3045 keeps most homeowners' associations from blocking turf that isn't visible from the street or a neighboring lot unless their own documents already address it "
         f"({src('fs125572', 'F.S. 125.572')}; {src('fs720-3045', 'F.S. 720.3045')}). A turf lawn also comes off the SJRWMD watering calendar that governs sod across the rest of Orange County "
         f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}).</p>"),
    ],
    "scenario": ("Turf along a Maitland lake lot, worked out in square feet",
                 f"<p>Picture a Maitland backyard that runs down toward one of the city's smaller lakes, where 600 square feet of lawn near the water struggles under partial shade from the shoreline tree line. At {price('artificial-turf')} per {per('artificial-turf')}, converting that area to turf runs roughly $6,000 to $10,800, with the installer measuring 10 feet back from the water's edge before the washed base goes in, a step that can reshape the usable footprint on a narrow lakefront yard more than the square footage alone suggests.</p>"),
    "faqs": [
        faq("How many of Maitland's lakes does the turf setback rule apply to?",
            "All of them. The state's 10-foot setback from a pond, lake or canal applies to any water body a turf installation sits near, which in Maitland's case touches a larger-than-typical share of residential lots given the city's 21 named lakes."),
        faq("Does a seawall change the Maitland turf setback?",
            "Yes. Where a seawall separates the yard from the water, the state's rule waives the 10-foot setback that would otherwise apply."),
        faq("Does turf near a Maitland lake still follow the SJRWMD watering schedule?",
            "No. A turf lawn has no irrigation zone for the district's twice-weekly schedule to govern once it's installed, regardless of how close the lot sits to the water."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
