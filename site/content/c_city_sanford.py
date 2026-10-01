# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "sanford"

CENSUS_SANFORD_URL = "https://censusreporter.org/profiles/16000US1263650-sanford-fl/"
SANFORD_WIKI_URL = "https://en.wikipedia.org/wiki/Sanford,_Florida"
SCHEDULE_S_URL = "https://sanfordfl.gov/wp-content/uploads/2023/09/Schedule-S-Historic-Preservation-District.pdf"
WATER_ATLAS_URL = "https://seminole.wateratlas.usf.edu/library/learn-more/learnmore.aspx?toolsection=lm_soils"

SRC = [
    "census-pep-v2025", "sanford-building", "sanford-schedule-n", "sanford-fees", "sanford-schedule-f",
    "seminole-driveway-app", "seminole-hb803", "sjrwmd-watering", "fl-dos-state-soil", "fl-senate-2011-104",
    "dep-rule", "fs125572", "fema-msc",
    (f"Census Reporter, Sanford FL (ACS 2020-2024 5-yr, B01003/B25035)", CENSUS_SANFORD_URL),
    ("Wikipedia, Sanford, Florida", SANFORD_WIKI_URL),
    ("City of Sanford, LDR Schedule S, Historic Preservation District (Ord. 2023-4729/4730)", SCHEDULE_S_URL),
    (f"Seminole County Water Atlas, Learn More: Soils", WATER_ATLAS_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Does a Sanford driveway or paver job go through Citizenserve the same way?",
        f"<p>Yes. The city's Building Division reviews every driveway, patio and paver application through its Citizenserve portal, and its Land Development Regulations draw a clear line at the property boundary: \"A City permit is required for all proposals to access City right-of-way,\" while a Seminole County permit covers the same work where a lot fronts a county road and an FDOT permit applies on a state road "
        f"({src('sanford-building', 'City of Sanford, Building Division')}; {src('sanford-schedule-n', 'City of Sanford, LDR Schedule N')}). A single-family residential driveway permit carries a published $250 fee under the city's Article VII fee schedule, separate from whatever a contractor charges for the work itself "
        f"({src('sanford-fees', 'City of Sanford, LDR Article VII Fees')}). {svc('concrete-driveways')} and {svc('paver-driveways')} cover what we build across every Sanford neighborhood; this hub covers what the city, the county and a handful of local facts change about how that work gets approved and laid out.</p>"),
    sec("What does Schedule F cap on a Sanford lot, and does it count pavers or turf?",
        f"<p>Sanford's impervious surface rule, Schedule F Section 5.0, spells out what counts toward the limit in plain language: \"concrete, pavers, asphalt, compacted gravel or mulch, and artificial turf\" are all impervious surface for calculation purposes, and every application has to include an ISR worksheet showing the math "
        f"({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}). The cap itself is 50 percent of the lot in the city's SR-1AA, SR-1A, SR-1, MR-2 and MR-3 districts, the zoning that covers most single-family subdivisions, while land under a planned development order can run up to 60 percent. A {cs('sanford', 'paver-driveways', 'paver driveway')} expansion or a new {svc('artificial-turf', 'turf lawn')} both move that same needle, which is why the worksheet gets filled out before either one is ordered, not after.</p>"),
    sec("What changes inside one of Sanford's four historic districts?",
        f"<p>Sanford's Schedule S covers four local historic districts, the Downtown Commercial, Sanford Residential, Sanford Avenue and Georgetown Residential districts, two of which also carry National Register status "
        f"({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')}; {ext(SANFORD_WIKI_URL, 'Wikipedia, Sanford, Florida')}). Inside those boundaries the design guidelines get specific: \"Driveways visible from the right of way may be surfaced with poured concrete, pavers, gravel or natural mulch, and must be confined by appropriate curbing,\" and new curb cuts aren't permitted on a lot that already has alley access, a rule meant to keep front-loaded garages off the street-facing side "
        f"({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')}). Garden walls in those same districts have to be brick or stucco matching the house, at least 8 inches wide with a capped top, and chain link or vinyl fencing is prohibited outright. A Certificate of Appropriateness from the Historic Preservation Board covers that review, separate from the building permit itself.</p>"),
    sec("How does sitting on Lake Monroe change where a Sanford project drains?",
        f"<p>Sanford grew up on the southern shore of Lake Monroe, at the head of navigation on the St. Johns River, a location that earned it the old nickname \"Historic Waterfront Gateway City\" "
        f"({ext(SANFORD_WIKI_URL, 'Wikipedia, Sanford, Florida')}). The nearly five-mile Riverwalk that now runs along that shoreline grew out of a 1995 sidewalk concept, with its first mile-plus segment finished in 2004 and a second phase reaching Mangoustine Avenue in 2018, part of a broader downtown streetscaping push that put brick pavers and wider sidewalks along the historic core the same year "
        f"({ext(SANFORD_WIKI_URL, 'Wikipedia, Sanford, Florida')}). A lot near that shoreline doesn't carry a single citywide flood designation; FEMA's own map center looks up the zone for a specific address rather than Sanford as a whole, which matters most for a {svc('concrete-pool-decks', 'pool deck')} or {svc('concrete-patios', 'patio')} pad elevation near the water "
        f"({src('fema-msc', 'FEMA Flood Map Service Center')}).</p>"),
    sec("What does a median 1994 build year and a growing population mean for a Sanford yard?",
        f"<p>Seminole County's latest count put Sanford at 67,483 residents as of July 1, 2025, up from 66,377 the year before and from a 2020 base of 61,184, among the faster-growing of the nine incorporated cities in the Orlando unit's territory "
        f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}). The housing stock itself skews a little older than that growth curve suggests: the median Sanford home dates to 1994, with an ACS five-year population estimate of 63,730 "
        f"({ext(CENSUS_SANFORD_URL, 'Census Reporter, Sanford FL')}). A driveway or patio original to a mid-1990s subdivision has had three decades of Florida summers on it, while a lot platted in the last few years inside a newer development starts from a clean slab and a current ISR worksheet instead of an older one that may never have been filed.</p>"),
    sec("Does Sanford's ground hold water the same way the rest of Seminole County's does?",
        f"<p>Sanford sits on the same band of flatwoods ground that covers most of Seminole County, where Myakka fine sand, the soil Florida named its official state symbol in 1989, is the dominant series "
        f"({src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}; {ext(WATER_ATLAS_URL, 'Seminole County Water Atlas, Learn More: Soils')}). That kind of ground can sit with a shallow water table for stretches of a typical rainy season, something a crew checks before pricing a {svc('concrete-slabs', 'slab')} or a {svc('paver-patios', 'paver patio')} rather than assuming every lot drains the way the sandier ridges west of Orlando do. Shallow limestone underlies parts of the county too, the geology behind Florida's sinkhole activity statewide, but the Florida Senate's own tally of where sinkhole insurance claims actually landed between 2006 and 2009 left Seminole off the list of eleven counties that produced most of them "
        f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). Irrigation in Sanford follows St. Johns River Water Management District's address-based calendar year-round: odd-numbered and no-number homes water Wednesdays and Saturdays, even-numbered homes water Thursdays and Sundays, and sprinklers stay off between 10 a.m. and 4 p.m. regardless of the day "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}).</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Sanford or Seminole County review my driveway permit?",
        f"It depends on which road the driveway fronts. Sanford's Building Division reviews anything touching city right-of-way through its Citizenserve portal, a Seminole County permit applies on a county road, and an FDOT permit applies on a state road "
        f"({src('sanford-schedule-n', 'City of Sanford, LDR Schedule N')}; {src('seminole-driveway-app', 'Seminole County, Residential Driveway Construction Application')})."),
    faq("Does artificial turf count toward Sanford's impervious surface limit?",
        f"Yes. Schedule F names \"artificial turf\" directly alongside concrete, pavers, asphalt, compacted gravel and mulch as impervious surface for ISR purposes, so a turf lawn uses up the same 50 percent lot allowance a driveway or patio would "
        f"({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')})."),
    faq("Can I pour a plain concrete driveway inside one of Sanford's historic districts?",
        f"Yes, poured concrete is one of the surfaces the historic district guidelines allow for a driveway visible from the right of way, alongside pavers, gravel and natural mulch, as long as it's confined by curbing and doesn't add a new curb cut on a lot with alley access "
        f"({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')})."),
    faq("What are Sanford's current watering days for new sod or landscaping?",
        f"St. Johns River Water Management District splits addresses into two groups year-round, odd and no-number households on Wednesday and Saturday, even-numbered households on Thursday and Sunday, with no watering allowed from 10 a.m. to 4 p.m. "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). A newly sodded yard gets 30 days of unrestricted watering first, then 30 more every other day before it drops onto that regular schedule."),
    faq("How do I pick the best concrete contractor for a Sanford project?",
        f"Start by confirming the address actually falls inside city limits rather than unincorporated Seminole County, since that single fact decides which permit desk reviews the job before any quote gets finalized. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our broader guide to vetting a contractor')} covers licensing checks and what else belongs in a written estimate."),
    faq("Does a garden wall in a Sanford historic district have to match the house?",
        f"Yes. The design guidelines call for brick or stucco garden walls matching the principal building, at least 8 inches wide with a capped top, and they prohibit chain link or vinyl fencing anywhere inside the historic districts "
        f"({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')})."),
]

HUB = page("/sanford-fl/", "city", "Concrete, Pavers & Turf Contractor in Sanford, FL",
           "Opera pours concrete, sets pavers and installs turf in Sanford, FL, where Schedule F counts turf toward the city's 50% impervious cap, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Sanford Homes",
           capsule(f"As of October 2026, Opera builds concrete driveways, pavers and artificial turf across Sanford, a Seminole County city on Lake Monroe with about 67,483 residents, roughly {str(__import__('_data').CITIES['sanford']['miles'])} miles from the Orlando unit's base. "
                   f"A new concrete driveway here runs {price('concrete-driveway')} per {per('concrete-driveway')} in the Florida market, and the city's own Schedule F counts a paver surface or an artificial turf lawn the same way it counts concrete toward the lot's 50 percent impervious-surface cap."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Sanford",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/seminole-county-driveway-patio-permits/", "Driveway and patio permits in Seminole County"),
                    ("/oviedo-fl/", "Concrete, pavers and turf in Oviedo"),
                    ("/lake-mary-fl/", "Concrete, pavers and turf in Lake Mary"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Sanford, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Sanford, FL – Schedule N",
    "meta": "Concrete driveway contractors in Sanford, FL: the city's $250 right-of-way fee and Schedule N's 10-foot driveway spacing rule, October 2026.",
    "h1": "Pouring a Concrete Driveway in Sanford",
    "lede": capsule(f"A new concrete driveway in Sanford costs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "The city's LDR Schedule N sets the layout rules for anything touching the right-of-way: a $250 permit fee, at least 10 feet of separation from the neighbor's driveway, and an apron poured at 3,000 psi minimum."),
    "sections": [
        ("Schedule N sets the spacing before the forms go up",
         f"<p>Three numbers from Sanford's Land Development Regulations drive most driveway layouts: a 10-foot minimum gap from the neighbor's driveway, a 35-foot clearance from the street's parallel pavement on a standard lot (smaller on a tight corner parcel), and 3,000 psi concrete for the apron itself "
         f"({src('sanford-schedule-n', 'City of Sanford, LDR Schedule N')}). A driveway that also crosses an existing sidewalk pours that section 6 inches thick rather than the usual 4, since Schedule N treats a vehicular crossing differently from a plain walking surface. Getting any one of those figures wrong on the plan is what usually sends an application back for revision before it reaches the Citizenserve inspection queue.</p>"),
        ("The $250 fee covers the city; a county road means a different office entirely",
         f"<p>Sanford's own Article VII fee schedule lists the single-family residential driveway permit flat at $250, filed through the Building Division once the layout clears Schedule N "
         f"({src('sanford-fees', 'City of Sanford, LDR Article VII Fees')}). A lot that technically fronts a Seminole County-maintained road instead of a city street skips that fee and the Citizenserve queue entirely, routing instead through the county's own Residential Driveway Construction Application, with its own 18-foot width cap and 18-inch minimum culvert "
         f"({src('seminole-driveway-app', 'Seminole County, Residential Driveway Construction Application')}). Confirming which office actually owns the road before ordering concrete avoids paying one fee and then being told to file with the other.</p>"),
    ],
    "scenario": ("Replacing an apron on a street the city maintains, worked out in square feet",
                 f"<p>Take a 22 by 24 ft two-car driveway, 528 sq ft, on a Sanford street inside the city's own right-of-way. At {price('concrete-driveway')} per {per('concrete-driveway')}, the job falls between roughly $3,168 and $7,920 before any demolition of the old slab is added in. "
                 "Add the $250 city permit fee on top, and check the plan against Schedule N's 10-foot spacing from the neighbor's driveway before the forms go in, since a layout that's too tight to the property line is the single change order that shows up most often on a Sanford job once the survey comes back.</p>"),
    "faqs": [
        faq("How much is a Sanford driveway permit?",
            f"$250 for a single-family residential driveway, published in the city's LDR Article VII fee schedule and filed through the Citizenserve portal ({src('sanford-fees', 'City of Sanford, LDR Article VII Fees')})."),
        faq("How far apart do Sanford driveways have to be?",
            f"At least 10 feet from an adjacent driveway, with an additional rule requiring at least 35 feet from the street's parallel pavement, both reduced proportionally on a smaller corner lot ({src('sanford-schedule-n', 'City of Sanford, LDR Schedule N')})."),
        faq("What happens if my driveway fronts a county road instead of a city street?",
            f"The application moves to Seminole County's Development Review Division instead of Sanford's Building Division, using the county's own width and culvert rules rather than Schedule N ({src('seminole-driveway-app', 'Seminole County')})."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Sanford, FL – ISR Math",
    "meta": "Paver driveway installers in Sanford, FL: how Schedule F's 50% impervious cap figures a paver expansion, October 2026.",
    "h1": "Paver Driveways and Sanford's Impervious Surface Limit",
    "lede": capsule(f"Expect {price('paver-driveway')} per {per('paver-driveway')} for a paver driveway in Sanford as of October 2026. "
                     "Schedule F counts the paver surface as impervious the same way it counts plain concrete, so a wider driveway or an added parking pad has to fit inside the lot's 50 percent cap in most residential zoning, not just the building footprint."),
    "sections": [
        ("Schedule F's worksheet decides how much driveway a lot can carry",
         f"<p>Sanford's impervious surface rule caps most single-family zoning districts, SR-1AA, SR-1A, SR-1, MR-2 and MR-3, at 50 percent of the lot, and every building application has to include an ISR calculation showing the math behind it "
         f"({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}). A homeowner widening a two-car driveway into a three-car paver apron on a lot that's already close to that ceiling can find the expansion capped by the ISR number long before the layout runs into a setback line. Land under a planned development order gets more room, up to 60 percent, which is worth checking against the specific subdivision's zoning before assuming the standard figure applies.</p>"),
        ("The right-of-way portion still routes through Schedule N separately",
         f"<p>Where the paver driveway crosses from private ground into the city right-of-way, that section falls under the same Schedule N spacing rules as a concrete apron, 10 feet from the neighbor's driveway and 35 feet from the street's parallel pavement "
         f"({src('sanford-schedule-n', 'City of Sanford, LDR Schedule N')}). Pairing the ISR worksheet for the private portion with the Schedule N layout for the public-facing section up front keeps {cs('sanford', 'concrete-driveways', 'a driveway job')} from stalling at the counter over paperwork that was filed separately instead of together.</p>"),
    ],
    "scenario": ("Sizing a paver expansion against the ISR ceiling",
                 f"<p>Picture a 1994-era Sanford home on a 7,500 sq ft SR-1 lot already carrying 3,200 sq ft of impervious surface between the house, an existing driveway and a rear patio, about 43 percent of the parcel. Adding a 450 sq ft paver widening to fit a boat trailer would push the total to roughly 49 percent, just inside the city's 50 percent cap. "
                 f"Pricing that addition at {price('paver-driveway')} per {per('paver-driveway')} comes to somewhere between $4,500 and $13,500 depending on the paver chosen, numbers worth having in hand before the ISR worksheet goes in alongside the permit application.</p>"),
    "faqs": [
        faq("Do pavers count toward Sanford's 50 percent impervious surface limit?",
            f"Yes. Schedule F names pavers directly as impervious surface for ISR purposes, the same as poured concrete, asphalt, compacted gravel or mulch, and artificial turf ({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')})."),
        faq("Which Sanford zoning districts use the 50 percent impervious cap?",
            f"SR-1AA, SR-1A, SR-1, MR-2 and MR-3, which cover most single-family and some multi-family residential land; property under a planned development order can run up to 60 percent instead ({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')})."),
        faq("Does a paver driveway need a separate right-of-way review in Sanford?",
            f"Only the section crossing into the right-of-way, which follows Schedule N's spacing rules; the private portion is covered by the ISR worksheet filed with the building permit ({src('sanford-schedule-n', 'City of Sanford, LDR Schedule N')})."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Sanford, FL – Flatwoods Ground",
    "meta": "Concrete patio contractors in Sanford, FL: drainage on Seminole County's flatwoods soil and the city's 1994 median build year, October 2026.",
    "h1": "Building a Concrete Patio in Sanford",
    "lede": capsule(f"A concrete patio in Sanford runs {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "With the city's typical home dating to 1994, plenty of original backyard pads are approaching three decades on flatwoods ground that holds water close to the surface for part of a typical year."),
    "sections": [
        ("A pad from the city's median build year has seen three decades of this climate",
         f"<p>Sanford's median year of home construction is 1994 "
         f"({ext(CENSUS_SANFORD_URL, 'Census Reporter, Sanford FL')}), which puts a meaningful share of the city's original backyard slabs well past the point where hairline cracking and a chalky surface are just ordinary wear. Whether a replacement stays inside the existing footprint or expands it changes the paperwork: an expansion feeds into the same ISR worksheet Schedule F requires for any added impervious surface "
         f"({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}).</p>"),
        ("A shallow water table decides the pitch more than the mix design",
         f"<p>The flatwoods soil under most of Seminole County, dominated by Myakka fine sand, can run with a seasonal high water table well within 18 inches of grade "
         f"({ext(WATER_ATLAS_URL, 'Seminole County Water Atlas, Learn More: Soils')}). On ground like that a patio slab needs a pitch that actively carries rain toward an existing swale, drain or low corner of the yard instead of relying on the soil to soak it away the way a sandier ridge lot west of Orlando might. A crew confirms that with a level and a shovel on site, since two lots on the same Sanford street can drain differently depending on how much fill went in when the subdivision was graded.</p>"),
    ],
    "scenario": ("A backyard patio addition on an older Sanford lot",
                 f"<p>Say a home built around the city's 1994 median adds a 15 by 20 ft patio off the back door, 300 sq ft, replacing a bare, compacted strip of yard. At {price('concrete-patio')} per {per('concrete-patio')}, that project runs roughly $1,800 to $3,900 before any decorative finish is added. "
                 "Because the addition is new impervious surface rather than a like-for-like replacement, the ISR worksheet gets updated alongside the permit, and the crew checks where the existing yard already sheds water before cutting into ground that's held a water table close to the surface for most of the lot's history.</p>"),
    "faqs": [
        faq("Does a concrete patio need an ISR worksheet in Sanford?",
            f"If it adds new impervious surface beyond an existing footprint, yes. Schedule F requires an impervious surface calculation on every application, and a patio counts the same way a driveway or paver area does ({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')})."),
        faq("Is a 1990s Sanford patio likely to need resurfacing rather than a repair?",
            "Often, yes. With the city's median home dating to 1994, a lot of original backyard slabs are old enough that hairline cracking and surface wear point toward resurfacing or replacement rather than a simple patch."),
        faq("Why does Sanford's soil matter for how a patio is pitched?",
            "Flatwoods ground common across Seminole County, including Myakka fine sand, holds a water table close to the surface part of the year, which shapes how a slab is sloped to shed rain more than it changes the mix design itself."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Sanford, FL – Historic Districts",
    "meta": "Paver patio installers in Sanford, FL: what Schedule S allows for paving inside the city's four historic districts, October 2026.",
    "h1": "Paver Patios and Walkways in Sanford",
    "lede": capsule(f"A paver patio in Sanford falls between {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "Inside the city's four historic districts, the design guidelines name pavers, poured concrete, gravel and natural mulch as acceptable surfacing, and a Certificate of Appropriateness covers that review separately from a standard building permit."),
    "sections": [
        ("Pavers are named on Schedule S's own list of allowed surfaces",
         f"<p>Sanford's four local historic districts, Downtown Commercial, Sanford Residential, Sanford Avenue and Georgetown Residential, fall under Schedule S, which states that a driveway or walkway visible from the right of way \"may be surfaced with poured concrete, pavers, gravel or natural mulch, and must be confined by appropriate curbing\" "
         f"({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')}; {ext(SANFORD_WIKI_URL, 'Wikipedia, Sanford, Florida')}). A patio tucked behind the house, out of view from the street, has more flexibility, but any new curb cut is off the table on a lot that already has alley access, part of the district's effort to keep front-loaded garages off its older streets.</p>"),
        ("The review runs through the Historic Preservation Board, not the standard counter",
         f"<p>Work inside one of the four districts gets a Certificate of Appropriateness from the city's Historic Preservation Board before construction starts, a step layered on top of whatever building or ISR review Schedule F already requires for the added surface "
         f"({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}). {cs('sanford', 'stamped-concrete', 'A decorative stamped surface')} goes through that same COA process, since the board reviews visual character rather than exempting a finish just because it isn't plain gray.</p>"),
    ],
    "scenario": ("A rear patio behind a Sanford Residential Historic District home",
                 f"<p>Consider a 1920s home in the Sanford Residential Historic District adding a 280 sq ft paver patio entirely behind the house, out of view from the street. At {price('paver-patio')} per {per('paver-patio')}, that lands around $2,800 to $4,760 depending on the paver and pattern chosen. "
                 "Because the patio isn't visible from the right of way, the surfacing choice has more latitude than a front driveway would, though the Certificate of Appropriateness and the ISR worksheet still both apply before pavers go down.</p>"),
    "faqs": [
        faq("Are pavers allowed on a driveway inside a Sanford historic district?",
            f"Yes, named directly alongside poured concrete, gravel and natural mulch on the city's own list of acceptable driveway surfaces for the historic districts, as long as the surface is confined by curbing ({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')})."),
        faq("Does a rear patio need the same historic district review as a front driveway?",
            "Both need a Certificate of Appropriateness from the Historic Preservation Board, but the surfacing rules are stricter for anything visible from the right of way than for a patio tucked behind the house."),
        faq("Can I add a new curb cut for a driveway in one of Sanford's historic districts?",
            f"Not if the lot already has alley access; the guidelines specifically disallow new curb cuts in that case to discourage front-loaded garages ({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')})."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Sanford, FL – Lake Monroe",
    "meta": "Concrete pool deck builders in Sanford, FL: checking a lot's flood zone near Lake Monroe before setting the deck elevation, October 2026.",
    "h1": "Concrete Pool Decks for Sanford Homes",
    "lede": capsule(f"As of October 2026, a concrete pool deck in Sanford runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} in the Florida market. "
                     "Sanford sits on the southern shore of Lake Monroe at the head of the St. Johns River's navigable stretch, and a lot close to that shoreline has its own flood zone to check before the deck's elevation gets set."),
    "sections": [
        ("A lakefront location changes the grading question, not the deck spec",
         f"<p>Sanford's old nickname, \"Historic Waterfront Gateway City,\" comes from its position at the head of navigation on the St. Johns River, where Lake Monroe gave steamers from Jacksonville a place to turn around "
         f"({ext(SANFORD_WIKI_URL, 'Wikipedia, Sanford, Florida')}). A pool deck going in near that shoreline isn't governed by a single citywide flood rule; FEMA's Flood Map Service Center looks up the designation by address, and that number decides the deck's finished elevation more than any other single factor on a lakefront lot "
         f"({src('fema-msc', 'FEMA Flood Map Service Center')}).</p>"),
        ("Inland lots work from the same impervious surface math as everywhere else",
         f"<p>Away from the water, a pool deck addition runs into the same Schedule F impervious surface accounting that governs a driveway or patio, with most residential zoning capped at 50 percent of the lot "
         f"({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}). {cs('sanford', 'pool-deck-pavers', 'A paver pool deck')} counts the same way a poured slab does for that calculation, so the choice between the two comes down to budget and look rather than which one uses up less of the ISR allowance.</p>"),
    ],
    "scenario": ("Setting a deck elevation on an inland Sanford lot",
                 f"<p>Take a home a few blocks inland from Lake Monroe pouring a 600 sq ft deck around a new pool shell. Figuring {price('concrete-pool-deck')} per {per('concrete-pool-deck')} puts that job between roughly $3,000 for a plain broom finish and $9,000 for a decorative cool-touch surface. "
                 "Because the lot sits outside the immediate shoreline, the grading question is a standard one, carrying water away from the house and the pool equipment pad, rather than the flood-elevation check a lot backing directly onto the lake would need first.</p>"),
    "faqs": [
        faq("Does every Sanford lot near Lake Monroe carry a flood zone?",
            f"Not automatically. Flood zones are assigned by address through FEMA's own Flood Map Service Center rather than as a single designation for the whole city, so a specific lot needs its own lookup before a pool deck's elevation is finalized ({src('fema-msc', 'FEMA Flood Map Service Center')})."),
        faq("Does a pool deck count toward Sanford's impervious surface limit?",
            f"Yes, the same way a driveway or patio does under Schedule F, with most residential zoning districts capped at 50 percent of the lot ({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')})."),
        faq("Why is Sanford called the Historic Waterfront Gateway City?",
            f"Sanford sits at the head of navigation on the St. Johns River, on the southern shore of Lake Monroe, where steamboats from Jacksonville historically had to stop because the river narrows upstream ({ext(SANFORD_WIKI_URL, 'Wikipedia, Sanford, Florida')})."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Sanford, FL – Pool Cages & Walls",
    "meta": "Pool deck paver installers in Sanford, FL: the city's 4-foot front wall limit and when a pool enclosure needs Building Official sign-off, October 2026.",
    "h1": "Pool Deck Pavers and Enclosure Walls in Sanford",
    "lede": capsule(f"Pool deck pavers in Sanford run {price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026, whether set fresh or over an existing slab. "
                     "A pool project often brings a wall or screen enclosure into the same job, and Sanford's own rule limits a front-yard wall to 4 feet while anything over 6 feet needs the Building Official's sign-off."),
    "sections": [
        ("A pool job's wall or fence work follows a separate height rule",
         f"<p>Sanford's Schedule F requires a building permit for any fence or wall allowed in the applicable zoning district, caps front-yard walls at 4 feet, and sends anything taller than 6 feet to the Building Official for approval before it's built "
         f"({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}). A pool cage or a low screening wall around the equipment pad usually clears that threshold without issue, but a taller privacy wall paired with the deck project is worth checking against that 6-foot line before it's drawn into the plans.</p>"),
        ("Inside a historic district, the wall material gets specified too",
         f"<p>On a lot inside one of Sanford's four historic districts, a garden or screening wall near the pool has its own material rule on top of the height limit: brick or stucco matching the house, at least 8 inches wide with a capped top, and chain link or vinyl fencing is off the table entirely "
         f"({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')}). {cs('sanford', 'concrete-pool-decks', 'A poured pool deck')} on the same historic lot gets reviewed through that same Certificate of Appropriateness process rather than a standard counter permit.</p>"),
    ],
    "scenario": ("Pairing a paver deck with a low screening wall",
                 f"<p>Picture a 550 sq ft paver deck going in around a new pool, with a 3.5-foot stucco screening wall along one side to shield the equipment pad from the neighbor's view. Pricing the deck at {price('pool-deck-pavers')} per {per('pool-deck-pavers')} comes to roughly $6,600 for a standard concrete paver and closer to $16,500 if travertine is chosen. "
                 "Since the wall stays under the city's 6-foot threshold, it clears Schedule F without the extra Building Official review a taller privacy wall would trigger, keeping the deck and the wall on the same permit timeline.</p>"),
    "faqs": [
        faq("How tall can a wall be next to a Sanford pool deck without extra review?",
            f"Up to 6 feet under Schedule F; anything taller needs the Building Official's approval, and a front-yard wall specifically is capped at 4 feet regardless of location ({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')})."),
        faq("What material does a screening wall need in a Sanford historic district?",
            f"Brick or stucco matching the principal building, at least 8 inches wide with a capped top; chain link and vinyl fencing are prohibited in all four historic districts ({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')})."),
        faq("Can pavers go over an existing Sanford pool deck instead of a full tear-out?",
            "Usually, as an overlay, reviewed the same way new construction is. How far the original slab has already cracked or settled decides whether an overlay holds up or a tear-out is the safer call."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Sanford, FL – Historic Brick Look",
    "meta": "Stamped concrete contractors in Sanford, FL: matching the city's brick-paved downtown streetscape with a decorative driveway or walkway, October 2026.",
    "h1": "Stamped Concrete Driveways and Walkways in Sanford",
    "lede": capsule(f"Stamped concrete work in Sanford falls between {price('stamped-concrete')} per {per('stamped-concrete')} as of October 2026, depending on pattern complexity and color count. "
                     "Downtown Sanford's own 2004 streetscaping project set brick pavers and wider sidewalks along its historic core, a look homeowners near that district often try to echo in a stamped driveway or front walk."),
    "sections": [
        ("A 2004 streetscaping project set the visual tone downtown",
         f"<p>A downtown streetscaping initiative launched in 2004 put brick pavers, wider sidewalks and restored infrastructure along Sanford's historic commercial core, part of an effort to draw new business and visitors to a district already known for its older brick storefronts "
         f"({ext(SANFORD_WIKI_URL, 'Wikipedia, Sanford, Florida')}). A brick-pattern stamped driveway or front walk near that core reads as an extension of that same streetscape, while a lot farther from downtown has more room for a contemporary slate or flagstone pattern instead.</p>"),
        ("Inside the historic districts, the finish doesn't change which review applies",
         f"<p>A stamped surface counts the same as plain gray concrete under Schedule S's list of allowed driveway materials, poured concrete, pavers, gravel or natural mulch confined by curbing, so the color or pattern doesn't exempt the work from a Certificate of Appropriateness "
         f"({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')}). {svc('stamped-concrete', 'Stamped work')} outside the four districts skips that extra board review and goes through the standard Schedule F and Schedule N process instead.</p>"),
    ],
    "scenario": ("Pricing a brick-pattern entry near downtown",
                 f"<p>A home a few blocks from Sanford's historic core is replacing a 200 sq ft driveway apron and front walk with a brick-pattern stamped finish and a rust-toned integral color. At {price('stamped-concrete')} per {per('stamped-concrete')}, that comes to roughly $1,600 at the plain end and up to $3,800 for a more detailed multi-color layout. "
                 "If the lot sits inside one of the four historic districts, the Certificate of Appropriateness and the curb-cut rule both apply exactly as they would to a plain gray pour; outside those boundaries, only the standard permit review applies.</p>"),
    "faqs": [
        faq("Does a brick-pattern stamped driveway need special approval near downtown Sanford?",
            f"Only if the lot sits inside one of the four historic districts, where any driveway surface, stamped or plain, goes through a Certificate of Appropriateness along with the standard Schedule F review ({ext(SCHEDULE_S_URL, 'City of Sanford, LDR Schedule S')})."),
        faq("What inspired the brick look in downtown Sanford?",
            f"A 2004 streetscaping project added brick pavers, wider sidewalks and restored infrastructure to the city's historic commercial core, part of a push to attract new business to the district ({ext(SANFORD_WIKI_URL, 'Wikipedia, Sanford, Florida')})."),
        faq("Is stamped concrete allowed in Sanford's historic districts?",
            "The guidelines don't exclude a decorative finish; poured concrete is on the list of acceptable driveway materials regardless of whether it's plain or stamped, as long as it's confined by curbing."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Sanford, FL – Counts as ISR",
    "meta": "Artificial turf installers in Sanford, FL: why Schedule F counts turf toward the 50% impervious cap and what the state rule requires, October 2026.",
    "h1": "Artificial Turf for Sanford Yards",
    "lede": capsule(f"Budget {price('artificial-turf')} per {per('artificial-turf')} for artificial turf in Sanford, a Florida market range holding as of October 2026. "
                     "What sets Sanford apart from many nearby cities is that Schedule F names \"artificial turf\" directly as impervious surface, so a new lawn counts toward the same 50 percent lot cap a driveway or patio does."),
    "sections": [
        ("Sanford counts turf toward ISR by name, which not every city does",
         f"<p>Schedule F's impervious surface definition lists \"concrete, pavers, asphalt, compacted gravel or mulch, and artificial turf\" together, and every application needs a worksheet showing the calculation "
         f"({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}). That means a homeowner replacing a struggling lawn with turf on a lot that's already close to the 50 percent ceiling can find the project capped by ISR math rather than by the state's own turf rule, a wrinkle worth checking before ordering material.</p>"),
        ("The state's base, infill and setback rules apply on top of that local math",
         f"<p>Florida's turf rule took effect May 19, 2026 and sets its own requirements regardless of what a city's ISR worksheet says: a washed, permeable base, infill that stays on the property rather than washing off, anchored seams, and a water-body setback of 10 feet unless a seawall already separates the lawn from the water "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}; {src('fs125572', 'Florida Statutes §125.572')}). Measuring that setback matters most on a lot backing toward Lake Monroe or one of Sanford's smaller lakes, where the turf layout has to clear the water-body line and still fit inside whatever ISR room is left on the lot.</p>"),
    ],
    "scenario": ("Checking ISR before swapping a dying lawn for turf",
                 f"<p>Consider a Sanford home on an SR-1 lot already at 46 percent impervious surface between the house, driveway and a rear patio, replacing 350 sq ft of thinning St. Augustine with turf. Figuring {price('artificial-turf')} per {per('artificial-turf')} puts the project somewhere between $3,500 and $8,750, swinging with pile height and backing. "
                 "Adding that turf pushes the lot to about 49 percent, just inside Sanford's 50 percent cap, a margin thin enough that the ISR worksheet gets checked before the old sod comes out rather than after.</p>"),
    "faqs": [
        faq("Does artificial turf count toward Sanford's impervious surface limit?",
            f"Yes, named directly in Schedule F alongside concrete and pavers, so it uses up the same 50 percent lot allowance in most residential zoning districts ({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')})."),
        faq("How far must turf stay from Lake Monroe or a Sanford pond?",
            f"The statewide rule sets a 10-foot minimum gap between turf and any natural or man-made water body, dropping only where a seawall or comparable barrier already sits between the lawn and the water ({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')})."),
        faq("Does turf need to follow Sanford's watering schedule?",
            "No. St. Johns River Water Management District's address-day calendar governs sprinklers irrigating grass, and a turf lawn with a compacted base underneath doesn't need watering once it's installed."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
