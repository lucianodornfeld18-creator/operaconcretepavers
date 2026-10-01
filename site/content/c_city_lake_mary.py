# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "lake-mary"

CENSUS_LM_URL = "https://censusreporter.org/profiles/16000US1238425-lake-mary-fl/"
LM_WIKI_URL = "https://en.wikipedia.org/wiki/Lake_Mary,_Florida"
HEATHROW_WIKI_URL = "https://en.wikipedia.org/wiki/Heathrow,_Florida"
LM_BUILDING_URL = "https://www.lakemaryfl.com/157/Building"
LM_HB803_URL = "https://www.lakemaryfl.com/1747"
LM_FEE_URL = "https://www.lakemaryfl.com/239/Application-Fee-Schedule"
LM_ISR_FAQ_URL = "https://www.lakemaryfl.com/FAQ.aspx?QID=134"
LM_POOL_FAQ_URL = "https://www.lakemaryfl.com/faq.aspx?TID=22"
LM_ARBOR_CODE_URL = "https://codelibrary.amlegal.com/codes/lakemary/latest/lakemary_fl/0-0-0-31263"

SRC = [
    "census-pep-v2025", "seminole-driveway-app", "seminole-hb803", "sjrwmd-watering", "fl-dos-state-soil",
    "dep-rule", "fs125572",
    (f"Census Reporter, Lake Mary FL (ACS 2020-2024 5-yr, B01003/B25035)", CENSUS_LM_URL),
    ("Wikipedia, Lake Mary, Florida", LM_WIKI_URL),
    ("Wikipedia, Heathrow, Florida", HEATHROW_WIKI_URL),
    ("City of Lake Mary, Building Division", LM_BUILDING_URL),
    ("City of Lake Mary, Permit Exemption (HB 803)", LM_HB803_URL),
    ("City of Lake Mary, Application Fee Schedule", LM_FEE_URL),
    ("City of Lake Mary, FAQ: What is the impervious surface ratio (ISR)?", LM_ISR_FAQ_URL),
    ("City of Lake Mary, Planning & Zoning FAQs", LM_POOL_FAQ_URL),
    ("City of Lake Mary Code of Ordinances §157.12, Arbor Permit Required", LM_ARBOR_CODE_URL),
    (f"Seminole County Water Atlas, Learn More: Soils", "https://seminole.wateratlas.usf.edu/library/learn-more/learnmore.aspx?toolsection=lm_soils"),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Who signs off on a driveway or paver job inside Lake Mary?",
        f"<p>The city's own Building Division, at 911 Wallace Court, reviews driveway, patio and paver work through its online permit portal, separate from the Seminole County office that handles the unincorporated pockets around the city "
        f"({ext(LM_BUILDING_URL, 'City of Lake Mary, Building Division')}). Site work including a driveway or a paver surface runs through the city's Site Construction Permit, billed at 1.25 percent of the contract price with a $250 minimum, a different formula than the flat fees some nearby cities publish "
        f"({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')}). {svc('concrete-driveways')} and {svc('paver-driveways')} cover what we build on either side of that line; this hub covers what changes depending on which office actually reviews the lot.</p>"),
    sec("Does Florida's 2026 small-project exemption let me skip a Lake Mary permit?",
        f"<p>Not for most of what falls under this kind of work. The city's own exemption page lists what never qualifies for HB 803's relief from a building permit: \"electrical, plumbing, mechanical, or gas work,\" anything structural, \"any project valued at $7,500 or more,\" and any work on a property in a designated flood zone "
        f"({ext(LM_HB803_URL, 'City of Lake Mary, Permit Exemption (HB 803)')}). A driveway, paver patio or pool deck job that stays under that dollar threshold and touches none of those carve-outs can qualify, but a job that crosses $7,500 in contract value, common once a {svc('paver-driveways', 'paver driveway')} gets past a few hundred square feet, goes through the standard Site Construction Permit instead.</p>"),
    sec("How does Lake Mary calculate impervious surface on a lot?",
        f"<p>Rather than one flat percentage, the city ties its impervious surface ratio to the property's Future Land Use designation: most categories, office, commercial, industrial and several others, cap out at 65 percent, the Downtown Development District and its overlays allow up to 90 percent, and a High Intensity Planned Development sits at 65 percent with a 35 percent minimum open-space requirement layered on top "
        f"({ext(LM_ISR_FAQ_URL, 'City of Lake Mary, FAQ: What is the impervious surface ratio (ISR)?')}). A {cs('lake-mary', 'paver-driveways', 'paver driveway')} or an expanded {svc('concrete-patios', 'patio')} both add to that same running total, which is why the city asks for the calculation on the permit application rather than leaving it to be checked after the fact.</p>"),
    sec("What's different about a lot with a Heathrow mailing address?",
        f"<p>Heathrow, the roughly 2,200-home gated, master-planned community founded in 1985 on former celery farmland by food entrepreneur Jeno Paulucci, carries a Lake Mary mailing address and ZIP code but is actually an unincorporated census-designated place in Seminole County, not part of the city itself "
        f"({ext(HEATHROW_WIKI_URL, 'Wikipedia, Heathrow, Florida')}). A paver driveway or pool deck project at a Heathrow address goes through Seminole County's own permit process rather than Lake Mary's Building Division, on top of whatever architectural approval the community's own association requires; confirming the jurisdiction before assuming a Lake Mary mailing address means the city reviews the job is worth the extra call.</p>"),
    sec("What does a built-out, slow-growth city mean for a Lake Mary project?",
        f"<p>Seminole County's latest count puts Lake Mary at 16,789 residents as of July 1, 2025, essentially flat against the 16,833 counted as the 2020 base and the 16,812 recorded the year before, a sign of a city that filled in most of its available land decades ago rather than one still adding new subdivisions "
        f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}). The typical Lake Mary home dates to 1997, with an ACS five-year population estimate of 16,860 "
        f"({ext(CENSUS_LM_URL, 'Census Reporter, Lake Mary FL')}). That build-out pattern traces back to the late 1980s and 1990s, when office, retail and industrial construction along the Interstate 4 corridor turned a small citrus-and-rail settlement named for Mary Sundell, wife of the Reverend J. F. Sundell, into a residential suburb and employment hub, now home to the American Automobile Association's national headquarters, Deloitte and Dixon Ticonderoga "
        f"({ext(LM_WIKI_URL, 'Wikipedia, Lake Mary, Florida')}). A driveway or patio original to that late-1990s wave of construction is old enough that a resurfacing conversation is more common now than it was a decade ago.</p>"),
        sec("Does Lake Mary's soil and tree rule work the same way as the rest of Seminole County?",
        f"<p>Myakka fine sand dominates the ground under Lake Mary just as it does most of Seminole County, a poorly drained flatwoods series that carries a shallow water table for stretches of a typical year "
        f"({ext('https://seminole.wateratlas.usf.edu/library/learn-more/learnmore.aspx?toolsection=lm_soils', 'Seminole County Water Atlas, Learn More: Soils')}). Florida's legislature made that soil the state's official symbol back in 1989, a detail that matters less than what it means on site: drainage, far more than the mix design, decides how a slab or base gets graded here. Trees get their own layer of review separate from any of that. Lake Mary's landscaping and arbor code requires a permit before cutting down, removing or moving a living tree taller than 15 feet, a $30 charge for a residential property "
        f"({ext(LM_ARBOR_CODE_URL, 'City of Lake Mary Code of Ordinances §157.12, Arbor Permit Required')}; {ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')}), a step worth budgeting for before a driveway or pool deck layout calls for clearing one to make room.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Is my Lake Mary address actually inside city limits for permit purposes?",
        f"Not always. A Lake Mary mailing address can still sit in a surrounding unincorporated pocket of Seminole County, Heathrow among them, where the county's Development Review Division handles the review instead of the city's own Building Division "
        f"({ext(LM_BUILDING_URL, 'City of Lake Mary, Building Division')}; {src('seminole-driveway-app', 'Seminole County, Residential Driveway Construction Application')})."),
    faq("How much does a Lake Mary site construction permit cost?",
        f"1.25 percent of the contract price, with a $250 minimum, covering driveway, paving and similar site work filed through the city's Building Division "
        f"({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')})."),
    faq("Does Florida's 2026 exemption cover a Lake Mary driveway under $7,500?",
        f"It can, as long as the work isn't structural, electrical, plumbing, mechanical or gas, and the lot isn't in a designated flood zone; crossing the $7,500 threshold removes the exemption regardless "
        f"({ext(LM_HB803_URL, 'City of Lake Mary, Permit Exemption (HB 803)')})."),
    faq("Is Heathrow part of the City of Lake Mary?",
        f"No. Heathrow carries a Lake Mary mailing address but is an unincorporated community in Seminole County, so county permitting and the community's own association, not the city's Building Division, review exterior work there "
        f"({ext(HEATHROW_WIKI_URL, 'Wikipedia, Heathrow, Florida')})."),
    faq("When is a Lake Mary homeowner allowed to irrigate a fresh lawn?",
        f"The district's year-round calendar assigns a watering day by the last digit of the address, odd and no-number households on Wednesday and Saturday, even-numbered ones on Thursday and Sunday, and blocks irrigation entirely from 10 a.m. to 4 p.m. "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). A brand-new lawn is exempt from that calendar for its first 30 days, then moves to an every-other-day schedule for another 30 before settling onto the regular two-day rotation."),
    faq("How do I find the best concrete contractor for a Lake Mary project?",
        f"Confirm a bid already accounts for which office reviews the job, since a Heathrow-area address changes that answer, and check the contractor against the state's license-lookup tool before signing anything. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our broader guide to vetting a contractor')} covers what else belongs in a written estimate."),
]

HUB = page("/lake-mary-fl/", "city", "Concrete, Pavers & Turf Contractor in Lake Mary, FL",
           "Opera builds concrete driveways, pavers and turf in Lake Mary, FL, where site permits run 1.25% of contract value, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Lake Mary Homes",
           capsule(f"Opera pours concrete, sets pavers and installs turf for homeowners in Lake Mary, a built-out Seminole County city of about 16,789 residents on the Interstate 4 corridor, {str(__import__('_data').CITIES['lake-mary']['miles'])} miles from the Orlando unit's base. "
                   f"Pricing for a new concrete driveway sits in the {price('concrete-driveway')} per {per('concrete-driveway')} range as of October 2026, and the city reviews most driveway and paver work through a Site Construction Permit billed at 1.25 percent of the contract price."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Lake Mary",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/seminole-county-driveway-patio-permits/", "Driveway and patio permits in Seminole County"),
                    ("/sanford-fl/", "Concrete, pavers and turf in Sanford"),
                    ("/oviedo-fl/", "Concrete, pavers and turf in Oviedo"),
                    ("/paver-driveway-cost/", "Paver driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Lake Mary, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Lake Mary, FL – Permit Cost",
    "meta": "Concrete driveway contractors in Lake Mary, FL: how the city's 1.25% site permit fee is figured, and when HB 803 applies, October 2026.",
    "h1": "Pouring a Concrete Driveway in Lake Mary",
    "lede": capsule(f"Budget {price('concrete-driveway')} per {per('concrete-driveway')} for a new concrete driveway in Lake Mary as of October 2026. "
                     "The city's own Site Construction Permit prices the review itself as a percentage of the job, 1.25 percent of the contract with a $250 floor, rather than the flat per-driveway fee some nearby cities charge."),
    "sections": [
        ("A percentage-based fee means the permit cost scales with the job",
         f"<p>Lake Mary's Application Fee Schedule lists site construction work, the category that covers a driveway, at 1.25 percent of the contract price with a $250 minimum "
         f"({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')}). On a modest resurfacing job that $250 floor is what actually applies; on a larger paver or decorative driveway running well into five figures, the fee climbs with it rather than staying flat. A breakdown of estimated construction cost has to accompany the application before the city calculates the number.</p>"),
        ("HB 803's exemption rarely reaches a driveway once the dollar figure adds up",
         f"<p>Florida's 2026 small-project law frees some residential work from a building permit below $7,500, but Lake Mary's own exemption page keeps structural work, utility trades and any flood-zone property off that list entirely "
         f"({ext(LM_HB803_URL, 'City of Lake Mary, Permit Exemption (HB 803)')}). A full driveway replacement on an average Lake Mary lot tends to land above that $7,500 line once demolition and base work are counted, which routes most driveway jobs back to the standard Site Construction Permit regardless of how the work itself is classified.</p>"),
    ],
    "scenario": ("Pricing a driveway against the city's percentage fee",
                 f"<p>Take a 500 sq ft two-car driveway replacement with a $9,500 contract value. At {price('concrete-driveway')} per {per('concrete-driveway')}, that square footage lands within the expected range, and because the contract clears $7,500, the project needs the standard Site Construction Permit rather than qualifying for HB 803's exemption. "
                 "The permit fee itself works out to roughly $119 under the 1.25 percent formula, below the $250 floor, so the floor is what the city actually charges on a job this size.</p>"),
    "faqs": [
        faq("How is a Lake Mary driveway permit fee calculated?",
            f"As 1.25 percent of the contract price, with a $250 minimum, filed through the city's Building Division as a Site Construction Permit ({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')})."),
        faq("Does HB 803 let me skip a Lake Mary driveway permit?",
            f"Only on work under $7,500 that isn't structural, electrical, plumbing, mechanical, gas work, or on a flood-zone lot; most full driveway jobs cross that dollar threshold once base and demolition are priced in ({ext(LM_HB803_URL, 'City of Lake Mary, Permit Exemption (HB 803)')})."),
        faq("What has to be submitted with a Lake Mary driveway application?",
            "A breakdown of estimated construction costs, since the permit fee itself is calculated as a percentage of that figure rather than charged as a flat rate."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Lake Mary, FL – ISR by Zone",
    "meta": "Paver driveway installers in Lake Mary, FL: how the city's impervious surface ratio varies by Future Land Use designation, October 2026.",
    "h1": "Paver Driveways and Lake Mary's Impervious Surface Rules",
    "lede": capsule(f"A paver driveway in Lake Mary runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026. "
                     "Unlike a city that sets one flat impervious surface cap, Lake Mary ties its limit to each property's Future Land Use designation, which decides how much room is left for a driveway expansion before the lot maxes out."),
    "sections": [
        ("The impervious cap moves with the land-use designation, not a single citywide number",
         f"<p>Lake Mary's own zoning FAQ breaks the impervious surface ratio down by Future Land Use category: most designations, office, commercial, industrial and public or semi-public land among them, top out at 65 percent, the Downtown Development District and its related overlays allow up to 90 percent, and a High Intensity Planned Development is capped at 65 percent alongside a required 35 percent of open space "
         f"({ext(LM_ISR_FAQ_URL, 'City of Lake Mary, FAQ: What is the impervious surface ratio (ISR)?')}). A homeowner widening a driveway into pavers checks the specific designation attached to the parcel rather than assuming a single citywide percentage applies the way it might in a neighboring city.</p>"),
        ("The same Site Construction Permit and percentage fee apply either way",
         f"<p>Whether the surface ends up poured concrete or pavers, the application still runs through the city's Site Construction Permit at 1.25 percent of the contract price, $250 minimum "
         f"({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')}). {cs('lake-mary', 'concrete-driveways', 'A plain concrete driveway')} and a paver one are reviewed on the same fee schedule, so the choice between materials comes down to budget and look rather than a difference in what the city charges to review the plan.</p>"),
    ],
    "scenario": ("Sizing a paver driveway against a lot's ISR room",
                 f"<p>Consider a Lake Mary home on a residential parcel where the house, existing driveway and a side patio already use a meaningful share of the lot's impervious allowance, and the owner wants to widen a 350 sq ft driveway into a 550 sq ft paver apron, adding 200 sq ft. Pricing the full 550 sq ft at {price('paver-driveway')} per {per('paver-driveway')} comes to somewhere between $5,500 and $16,500 depending on the paver chosen. "
                 "Before ordering material, the city's own ISR figure for that specific land-use designation gets checked against the lot's existing coverage, since the ceiling differs by designation rather than following one flat rule.</p>"),
    "faqs": [
        faq("Does Lake Mary use one impervious surface limit for every property?",
            f"No. The city ties the cap to each lot's Future Land Use designation, ranging from 65 percent in most categories up to 90 percent in the Downtown Development District and its overlays ({ext(LM_ISR_FAQ_URL, 'City of Lake Mary, FAQ: What is the impervious surface ratio (ISR)?')})."),
        faq("Does a paver driveway cost more to permit than a concrete one in Lake Mary?",
            "No. Both go through the same Site Construction Permit at 1.25 percent of the contract price, so the fee tracks the job's dollar value rather than the surface material chosen."),
        faq("What is a High Intensity Planned Development's impervious limit in Lake Mary?",
            f"65 percent, the same ceiling as most standard designations, but paired with a required minimum of 35 percent open space on the property ({ext(LM_ISR_FAQ_URL, 'City of Lake Mary, FAQ: What is the impervious surface ratio (ISR)?')})."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Lake Mary, FL – 1997 Homes",
    "meta": "Concrete patio contractors in Lake Mary, FL: drainage on flatwoods soil and why the city's 1997 median build year matters, October 2026.",
    "h1": "Building a Concrete Patio in Lake Mary",
    "lede": capsule(f"A concrete patio in Lake Mary falls between {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "With the typical home here dating to 1997 and the city largely built out since, original backyard slabs from that late-1990s wave of construction are common enough that a resurfacing decision comes up almost as often as a new pour."),
    "sections": [
        ("A city that stopped expanding leaves a lot of same-era concrete behind",
         f"<p>Lake Mary's population has barely moved in five years, 16,789 counted in 2025 against a 2020 base of 16,833 "
         f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}), a pattern that lines up with a median home build year of 1997 "
         f"({ext(CENSUS_LM_URL, 'Census Reporter, Lake Mary FL')}). That combination means most of the city's original backyard patios share roughly the same age, nearly three decades of Florida heat, rain and UV exposure, rather than a mix of brand-new and original slabs the way a still-growing city would show.</p>"),
        ("Flatwoods ground shapes the grading before the forms go in",
         f"<p>Myakka fine sand, the series that covers most of Seminole County including Lake Mary, drains slowly enough that standing water after a storm is more a function of the native soil than poor workmanship "
         f"({src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}). Skipping that reality when a patio is pitched leaves water pooling against the slab instead of running toward a swale or low corner of the yard, which is why a crew walks the lot with a level before deciding the finished grade rather than copying the pitch of a neighboring driveway.</p>"),
    ],
    "scenario": ("Replacing a patio that matches the city's building-era average",
                 f"<p>Picture a home built close to Lake Mary's 1997 median adding a 260 sq ft patio extension off an existing lanai, replacing a bare strip of compacted yard. At {price('concrete-patio')} per {per('concrete-patio')}, the job runs somewhere between $1,560 and $3,380 before any decorative finish is added. "
                 "Because the extension is new impervious surface, it feeds into the ISR figure tied to that lot's Future Land Use designation, and the grading gets checked against the yard's existing drainage pattern before the forms go in.</p>"),
    "faqs": [
        faq("Is a 1990s Lake Mary patio more likely to need replacement than repair?",
            "Often, yes. With the typical home dating to 1997 and the city largely built out since, a meaningful share of original backyard slabs are old enough that resurfacing or a full tear-out comes up more than a simple patch."),
        faq("Does a concrete patio addition affect Lake Mary's impervious surface limit?",
            "Yes, if it adds new surface beyond what already exists, since the added square footage counts toward whatever ISR ceiling applies to that lot's Future Land Use designation."),
        faq("Why does Lake Mary's soil matter for patio drainage?",
            f"Myakka fine sand, the series under most of the city, drains slowly enough that a patio's pitch does more work keeping water off the slab than the concrete mix itself does ({src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')})."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Lake Mary, FL – Heathrow Address",
    "meta": "Paver patio installers in Lake Mary, FL and the nearby Heathrow area: why a Lake Mary ZIP code doesn't always mean a city permit, October 2026.",
    "h1": "Paver Patios in Lake Mary and the Heathrow Area",
    "lede": capsule(f"A paver patio in Lake Mary or the surrounding Heathrow area runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "A Lake Mary mailing address doesn't always mean a Lake Mary permit review: the roughly 2,200-home Heathrow community carries that ZIP code while sitting outside city limits in unincorporated Seminole County."),
    "sections": [
        ("Heathrow's address is Lake Mary's; its permit desk is the county's",
         f"<p>Heathrow was founded in 1985 on former celery-farming land and has grown into a gated, master-planned community of roughly 2,200 homes across 3.16 square miles, with the American Automobile Association's national headquarters among its office tenants "
         f"({ext(HEATHROW_WIKI_URL, 'Wikipedia, Heathrow, Florida')}). Despite the Lake Mary mailing address, Heathrow is an unincorporated census-designated place, so a paver patio there is reviewed by Seminole County's Development Review Division rather than the Lake Mary Building Division "
         f"({ext(LM_BUILDING_URL, 'City of Lake Mary, Building Division')}). No published architectural rule specific to patio pavers for a Heathrow sub-association was confirmed for this guide, so a homeowner there checks both the county's permit requirement and the community's own design review before ordering material.</p>"),
        ("Inside Lake Mary proper, the same Site Construction Permit applies",
         f"<p>A patio built on a lot actually inside the Lake Mary city limits goes through the same 1.25 percent Site Construction Permit fee, $250 minimum, that covers a driveway or pool deck "
         f"({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')}). {cs('lake-mary', 'concrete-patios', 'A poured concrete patio')} on the same lot files under that identical fee structure, so the material choice doesn't change which office reviews it or how the fee is figured.</p>"),
    ],
    "scenario": ("Checking jurisdiction before pricing a patio near Heathrow",
                 f"<p>Say a homeowner with a Lake Mary, FL mailing address wants a 320 sq ft paver patio added off the back of the house. If the parcel sits inside Heathrow's unincorporated boundary, Seminole County reviews the permit rather than the city, and the community's own architectural process runs alongside it. "
                 f"Pricing the patio itself at {price('paver-patio')} per {per('paver-patio')} comes to roughly $3,200 to $5,440 either way; what changes with the address is which office stamps the permit, not the cost of the work itself.</p>"),
    "faqs": [
        faq("Is Heathrow inside the City of Lake Mary?",
            f"No. Heathrow carries a Lake Mary mailing address and ZIP code but is an unincorporated community in Seminole County, founded in 1985 on former celery land ({ext(HEATHROW_WIKI_URL, 'Wikipedia, Heathrow, Florida')})."),
        faq("Who reviews a paver patio permit for a Heathrow address?",
            f"Seminole County's Development Review Division, not Lake Mary's Building Division, since Heathrow sits outside the city's incorporated boundary ({ext(LM_BUILDING_URL, 'City of Lake Mary, Building Division')})."),
        faq("Does Heathrow have its own paver or driveway design rules beyond the county permit?",
            "Likely, through the community's own master association, but no specific published paver or driveway guideline was confirmed for this guide; check directly with the Heathrow Master Association before finalizing a design."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Lake Mary, FL – Setbacks",
    "meta": "Concrete pool deck builders in Lake Mary, FL: the city's 10-foot pool and 3-foot enclosure setback from the rear lot line, October 2026.",
    "h1": "Concrete Pool Decks for Lake Mary Homes",
    "lede": capsule(f"As of October 2026, a concrete pool deck in Lake Mary runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} in the Florida market. "
                     "The city's own zoning rule sets how close a pool and its screen enclosure can sit to the rear lot line, a number that shapes the deck's footprint on a standard residential lot."),
    "sections": [
        ("A 10-foot and 3-foot setback frame the deck before the pool shell goes in",
         f"<p>Lake Mary's Planning & Zoning guidance allows a swimming pool to sit as close as 10 feet to the rear lot line in regular residential zoning districts, with the surrounding screen enclosure allowed to 3 feet from that same line "
         f"({ext(LM_POOL_FAQ_URL, 'City of Lake Mary, Planning & Zoning FAQs')}). That gap between the two numbers is where most of a pool deck's usable footprint actually sits, since the enclosure can push closer to the property line than the water itself.</p>"),
        ("The deck's added surface still counts toward the lot's ISR figure",
         f"<p>A new pool deck is new impervious surface, counted the same way a driveway or patio addition is against whatever Future Land Use designation governs that lot's impervious ceiling "
         f"({ext(LM_ISR_FAQ_URL, 'City of Lake Mary, FAQ: What is the impervious surface ratio (ISR)?')}). {cs('lake-mary', 'pool-deck-pavers', 'A paver pool deck')} adds to that same total, so the setback and the ISR number both get checked before the deck's final dimensions are drawn.</p>"),
    ],
    "scenario": ("Laying out a deck against the rear setback",
                 f"<p>Take a standard Lake Mary lot adding a new pool with a screen cage set 3 feet off the rear line and the water itself held to the 10-foot pool setback, leaving a 620 sq ft deck between the house and the cage. Figuring {price('concrete-pool-deck')} per {per('concrete-pool-deck')} puts that job between roughly $3,100 for a plain broom finish and $9,300 for a decorative cool-touch surface. "
                 "Running the enclosure to the 3-foot line rather than further back is what lets the deck and pool fit the lot without pushing into the required rear yard space.</p>"),
    "faqs": [
        faq("How close to the rear lot line can a Lake Mary pool sit?",
            f"As close as 10 feet in regular residential zoning districts, with the screen enclosure around it allowed to 3 feet from that same line ({ext(LM_POOL_FAQ_URL, 'City of Lake Mary, Planning & Zoning FAQs')})."),
        faq("Does a Lake Mary pool deck count toward the lot's impervious surface limit?",
            "Yes, the same as any other new paved surface, counted against whatever ISR ceiling applies under the lot's Future Land Use designation."),
        faq("Can pavers go over an existing Lake Mary pool deck instead of a full tear-out?",
            "Often, as an overlay, following the same Site Construction Permit process as new construction; how far the original slab has cracked or settled decides whether an overlay holds up long-term."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Lake Mary, FL – Tree Rule",
    "meta": "Pool deck paver installers in Lake Mary, FL: when removing a tree over 15 feet for a pool project needs its own arbor permit, October 2026.",
    "h1": "Pool Deck Pavers and Lake Mary's Arbor Permit",
    "lede": capsule(f"Pool deck pavers in Lake Mary fall in the {price('pool-deck-pavers')} per {per('pool-deck-pavers')} range as of October 2026, whether laid fresh or over an existing slab. "
                     "A pool deck large enough to require removing a mature tree brings the city's arbor permit into the project alongside the Site Construction Permit covering the pavers themselves."),
    "sections": [
        ("A tree over 15 feet needs its own permit before it comes down",
         f"<p>Lake Mary's landscaping and arbor code requires a permit before cutting down, removing or moving a living tree taller than 15 feet anywhere in the city, with a $30 fee for a residential arbor permit "
         f"({ext(LM_ARBOR_CODE_URL, 'City of Lake Mary Code of Ordinances §157.12, Arbor Permit Required')}; {ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')}). A pool deck footprint that calls for clearing a tree to make room runs that arbor application alongside the Site Construction Permit covering the deck itself, since the two are reviewed as separate steps.</p>"),
        ("The paver deck permit tracks the same percentage fee as every other site job",
         f"<p>Whether the deck is a first installation or an overlay set over an existing slab, it goes through the same Site Construction Permit at 1.25 percent of the contract price, $250 minimum "
         f"({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')}). {cs('lake-mary', 'concrete-pool-decks', 'A poured pool deck')} on the same lot files on that identical fee basis, so the choice between a paver surface and plain concrete doesn't change the permit cost itself.</p>"),
    ],
    "scenario": ("Clearing a tree to fit a paver deck",
                 f"<p>Picture a backyard pool project where a 580 sq ft paver deck layout requires removing one 20-foot oak that sits directly where the screen enclosure needs to go. The arbor permit for that single tree costs $30, filed separately from the deck's own Site Construction Permit. "
                 f"Pricing the deck at {price('pool-deck-pavers')} per {per('pool-deck-pavers')} runs from roughly $6,960 for a standard concrete paver up to $17,400 if travertine is chosen instead, with the tree removal and its permit handled as a distinct line item before the base goes in.</p>"),
    "faqs": [
        faq("Does removing a tree for a Lake Mary pool deck need its own permit?",
            f"Yes, if the tree is taller than 15 feet, the city's arbor code requires a permit before it's cut down, removed or moved, with a $30 fee for a residential property ({ext(LM_ARBOR_CODE_URL, 'City of Lake Mary Code of Ordinances §157.12')})."),
        faq("Is the arbor permit separate from the pool deck's building permit in Lake Mary?",
            "Yes, the two are filed and reviewed as distinct applications, the arbor permit covering the tree and the Site Construction Permit covering the deck itself."),
        faq("Does a paver pool deck cost more to permit than a poured concrete one in Lake Mary?",
            "No. Both fall under the same 1.25 percent Site Construction Permit fee, so the review cost tracks the contract value rather than the surface material."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Lake Mary, FL – I-4 Corridor",
    "meta": "Stamped concrete contractors in Lake Mary, FL: matching a decorative driveway to the city's 1980s-90s office-corridor housing stock, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Lake Mary",
    "lede": capsule(f"Stamped concrete work in Lake Mary falls between {price('stamped-concrete')} per {per('stamped-concrete')} as of October 2026. "
                     "Unlike Sanford or Oviedo, Lake Mary has no old downtown core; most of its housing stock grew up alongside the office parks that filled in along Interstate 4 during the late 1980s and 1990s, which shapes what a decorative driveway is usually matched against."),
    "sections": [
        ("A suburb that grew with the I-4 office corridor, not an old town center",
         f"<p>Lake Mary incorporated in 1973 from what had been a citrus and agricultural settlement along the rail line between Sanford and Orlando, then filled in fast during the 1980s and 1990s as office, retail and industrial development spread along Interstate 4 "
         f"({ext(LM_WIKI_URL, 'Wikipedia, Lake Mary, Florida')}). That history means a stamped driveway here is usually paired against a 1980s or 1990s suburban facade rather than the brick storefronts and older bungalows found in a city with a historic downtown core, so a clean slate or ashlar-cut pattern tends to read better than an ornate brick pattern built to match century-old architecture.</p>"),
        ("The decorative finish doesn't change the permit or its fee",
         f"<p>A stamped surface is reviewed the same way a plain broom-finish driveway is, through the Site Construction Permit at 1.25 percent of the contract price "
         f"({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')}). {svc('stamped-concrete', 'Stamped concrete')} does typically carry a higher contract value than plain gray concrete for the same square footage, which can move the permit fee above the $250 minimum where a smaller plain job would land right at that floor.</p>"),
    ],
    "scenario": ("Pricing a stamped entry against a 1990s-era home",
                 f"<p>A home built close to Lake Mary's 1997 median is replacing a 230 sq ft driveway apron and front walk with an ashlar-slate stamped pattern in a warm gray tone. At {price('stamped-concrete')} per {per('stamped-concrete')}, that comes to roughly $1,840 at the plain end and up to $4,370 for a more detailed layout. "
                 "Because the contract value for the decorative work runs higher than a plain pour of the same size, the 1.25 percent Site Construction Permit fee lands above the city's $250 floor rather than at it.</p>"),
    "faqs": [
        faq("Does Lake Mary have a historic district that affects stamped concrete choices?",
            "No. The city grew mainly during the 1980s and 1990s alongside its Interstate 4 office corridor rather than around an older downtown core, so there's no historic-district design review to match a pattern against the way a city like Sanford has."),
        faq("Does a stamped driveway cost more to permit in Lake Mary than plain concrete?",
            f"The fee formula is the same, 1.25 percent of the contract price, but a higher contract value for decorative work can push the fee above the city's $250 minimum where a plain job of the same size would land at the floor ({ext(LM_FEE_URL, 'City of Lake Mary, Application Fee Schedule')})."),
        faq("What pattern suits a typical 1990s Lake Mary home?",
            "A cleaner ashlar or slate-style pattern tends to match the city's mostly 1980s-90s suburban architecture better than an ornate brick pattern built for an older downtown setting."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Lake Mary, FL – Flood Zone Rule",
    "meta": "Artificial turf installers in Lake Mary, FL: why turf on a flood-zone lot skips the city's HB 803 exemption, October 2026.",
    "h1": "Artificial Turf for Lake Mary Yards",
    "lede": capsule(f"Artificial turf in Lake Mary runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026 in the Florida market. "
                     "Lake Mary's own HB 803 exemption page excludes any flood-zone property outright, so a turf project on a lot carrying that designation needs the standard permit regardless of its dollar value."),
    "sections": [
        ("A flood-zone lot loses the small-project exemption no matter the price",
         f"<p>Lake Mary's exemption page for Florida's 2026 small-project law lists \"any work in a designated flood zone\" among the categories that never qualify, alongside structural and utility-trade work "
         f"({ext(LM_HB803_URL, 'City of Lake Mary, Permit Exemption (HB 803)')}). A turf lawn under $7,500 on most lots could otherwise qualify for that exemption, but a property in a mapped flood zone goes through the standard Site Construction Permit regardless of the project's size or cost.</p>"),
        ("The lake the city is named for puts the state's water-body rule to work often",
         f"<p>Florida's synthetic turf rule took effect May 19, 2026 and doesn't bend for local permit rules: the base has to drain, the infill has to stay put rather than washing off the property, seams get anchored against wind and rain, and turf can't go within 10 feet of a natural or man-made water body short of a seawall standing between the two "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}; {src('fs125572', 'Florida Statutes §125.572')}). Between Lake Mary itself and the smaller retention ponds built into so many of the city's subdivisions, that 10-foot line comes up on more backyards here than it would in a town with fewer water features tucked into its neighborhoods.</p>"),
    ],
    "scenario": ("Checking flood-zone status before assuming turf is exempt",
                 f"<p>Say a homeowner near one of Lake Mary's neighborhood ponds wants to replace 300 sq ft of thinning grass with turf, a project estimated at $3,000, well under HB 803's $7,500 threshold. If the lot's FEMA designation puts it in a mapped flood zone, the city's own exemption rule removes that path regardless of the low price tag, and the standard Site Construction Permit applies instead. "
                 f"Pricing the turf itself at {price('artificial-turf')} per {per('artificial-turf')} comes to roughly $3,000 to $7,500 for that square footage, with the 10-foot water-body setback checked against the pond's edge before the layout is finalized.</p>"),
    "faqs": [
        faq("Does Florida's 2026 exemption cover turf on every Lake Mary lot?",
            f"No. The city's exemption page removes any property in a designated flood zone from eligibility regardless of the project's dollar value, on top of the usual $7,500 ceiling ({ext(LM_HB803_URL, 'City of Lake Mary, Permit Exemption (HB 803)')})."),
        faq("How far must turf stay from a pond in a Lake Mary neighborhood?",
            f"The state's rule draws that line at 10 feet from a natural or man-made water body, closing only where a seawall or equivalent barrier already stands between the turf and the water ({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')})."),
        faq("Do turf lawns in Lake Mary get assigned a sprinkler day?",
            "No. The district's irrigation calendar exists for sprinkler heads watering grass; a finished turf panel sitting on a compacted base has no root zone for that calendar to govern."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
