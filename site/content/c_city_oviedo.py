# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "oviedo"

WATER_ATLAS_URL = "https://seminole.wateratlas.usf.edu/library/learn-more/learnmore.aspx?toolsection=lm_soils"
ECON_WIKI_URL = "https://en.wikipedia.org/wiki/Econlockhatchee_River"
OVIEDO_WIKI_URL = "https://en.wikipedia.org/wiki/Oviedo,_Florida"

SRC = [
    "census-pep-v2025", "acs-oviedo",
    "oviedo-building-services", "oviedo-row-type1", "oviedo-slab-paver", "oviedo-permit-guidelines",
    "seminole-driveway-app", "seminole-hb803",
    "sjrwmd-watering", "fl-dos-state-soil", "fl-senate-2011-104", "dep-rule", "fs125572", "oviedo-otp",
    (f"Seminole County Water Atlas, Learn More: Soils", WATER_ATLAS_URL),
    ("Wikipedia, Econlockhatchee River", ECON_WIKI_URL),
    ("Wikipedia, Oviedo, Florida", OVIEDO_WIKI_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Does Oviedo's 2026 permit exemption cover a new driveway or paver patio?",
        "<p>House Bill 803 took effect July 1, 2026 and frees a homeowner, or the contractor working for one, from a building permit on residential work valued under $7,500. Oviedo's Building Services department confirms that exemption applies here, then publishes its own list of “Non-Structural residential work that would still require a planning and zoning permit through the Planning Department,” and two lines on that list matter most to anyone pouring or paving: "
        f"“Pavers/driveways/sidewalks on private property” and “Non-structural 4\" concrete slabs on grade” "
        f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). In plain terms, the 2026 exemption doesn't reach {cs('oviedo', 'paver-driveways', 'a paver driveway')} or {cs('oviedo', 'concrete-patios', 'a patio slab')} inside the city limits; a planning and zoning permit still applies. Call Building Services at 407-971-5755 or buildingpermits@cityofoviedo.net before ordering material, since the city's own guidance is specific about what it exempts and what it doesn't.</p>"),
    sec("What does a right-of-way permit for the apron cost in Oviedo?",
        f"<p>Any part of a driveway, walk or paver apron that crosses the right-of-way, the strip between a homeowner's property line and the street, needs its own Right-of-Way Type I application through the Development Review Division at 400 Alexandria Blvd., 407-971-5796. The current form, revised October 2023, carries an application fee of $79.00 plus a $25.00 technology fee, $104.00 total, and the city asks for a sealed boundary survey, a maintenance-of-traffic plan and a certificate of insurance alongside it "
        f"({src('oviedo-row-type1', 'City of Oviedo, Right-of-Way Type I Application')}). That review runs separately from, and on top of, whatever permit covers the rest of {svc('concrete-driveways', 'the driveway')} on private ground.</p>"),
    sec("Outside the city, Seminole County caps a driveway at 18 feet plus flares",
        f"<p>A fair amount of ground with an Oviedo mailing address actually sits in unincorporated Seminole County, where a different office, the Development Review Division, reviews the Residential Driveway Construction Application (Plandesk@seminolecountyfl.gov, 407-665-7371, with inspections called in 24 to 48 hours ahead at 407-665-7409). The form's own numbers are specific "
        f"({src('seminole-driveway-app', 'Seminole County, Residential Driveway Construction Application')}):</p>"
        + table("Seminole County residential driveway specifications (unincorporated area)",
                ["Item", "County requirement"],
                [["Driveway width", "18 ft maximum, with 3 ft flares (24 ft total at the roadway)"],
                 ["Driveway material in the ROW", "6 in of non-steel or fiber-reinforced concrete, 3,000 psi minimum"],
                 ["Culvert diameter", "18 in minimum, or per an engineer's specification"],
                 ["Setback from property line", "5 ft minimum"],
                 ["Clearance from a neighbor's flare", "6 ft minimum"]],
                "Source: Seminole County Residential Driveway Construction Application, checked October 2026. Pavers may go in the right-of-way, but the county keeps them out of any crosswalk or sidewalk portion and won't take responsibility for replacing them if it ever has to dig there.")
        + f"<p>The county's own 2026 rundown of HB 803's new exemptions lists fences, pergolas, floating docks, non-bearing interior walls, cabinets and sheds of 200 sq ft or less, and it doesn't mention driveways, pavers, slabs or retaining walls at all "
        f"({src('seminole-hb803', 'Seminole County, New State Legislation Affecting Permits')}), so a {cs('oviedo', 'retaining-walls', 'retaining wall')} or a parking pad on an unincorporated lot still goes through standard review; call the Building Division at 407-665-7050 to confirm scope before pricing the job.</p>"),
    sec("How do the Econlockhatchee River and Lake Jesup change where water goes on a lot?",
        f"<p>Oviedo grew up on the shore of Lake Jesup, where homesteaders settled in 1875, and the city is still bordered by that lake to the north and by the Econlockhatchee River, a 54.5-mile blackwater tributary of the St. Johns River, running through its eastern side, with the Little Econlockhatchee River crossing the south "
        f"({ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}; {ext(ECON_WIKI_URL, 'Wikipedia, Econlockhatchee River')}). Neither the city's permit guidance nor Seminole County's driveway application publishes a stand-alone setback from either waterway for a {svc('concrete-pool-decks', 'pool deck')} or a {svc('retaining-walls', 'retaining wall')}; the grading question on a lot that slopes toward the river corridor or the lake is about where the fill goes and how the pad or wall sheds water, which a site visit settles before forms go up, not a published number to look up.</p>"),
    sec("What does a median 1997 build year mean for an Oviedo project?",
        f"<p>Seminole County counted Oviedo's population at 41,317 residents on July 1, 2025 "
        f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}), and the city's typical home dates to 1997 "
        f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), newer than a lot of Central Florida's older suburbs but old enough that an original driveway or patio slab is approaching three decades of Florida summers. Much of that growth traces back to the University of Central Florida, chartered in 1963 a short drive west, and the Central Florida Research Park that followed in 1978, which pulled rooftops out past the old Lake Jesup settlement and its historic downtown, where free-roaming chickens were once a local fixture "
        f"({ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}). More recently, the city's own Oviedo on the Park development has added newer construction around Center Lake Park, “the crown jewel of the city's new Oviedo on the Park development area” "
        f"({src('oviedo-otp', 'City of Oviedo, Oviedo on the Park')}), so a two-year-old {svc('concrete-pool-decks', 'pool deck')} there and a 1997-era original a few miles away aren't rare to find on the same street map.</p>"),
    sec("Does Oviedo's soil hold water the way the rest of Seminole County's flatwoods does?",
        f"<p>Seminole County's own water-quality education program names Myakka fine sand as “typical” of the flatwoods ground found across the county, and the state legislature designated Myakka fine sand Florida's official state soil in 1989, found on more than 1.5 million acres statewide "
        f"({ext(WATER_ATLAS_URL, 'Seminole County Water Atlas, Learn More: Soils')}; {src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}). Flatwoods ground like that holds a water table close to the surface for part of a typical year, which is the reason a crew checks a yard with a shovel before pricing {svc('concrete-slabs', 'a slab')} or a {svc('paver-patios', 'paver patio')}, rather than assuming every Seminole County lot drains the way a ridge-sand lot farther west does.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Who reviews a new driveway, Oviedo's Building Services or Seminole County?",
        "Check the address against the city boundary first, since the Oviedo limits and the surrounding unincorporated county can carry the same mailing address. Building Services handles anything inside that line, including the right-of-way apron; outside it, the county's Development Review Division takes the whole application instead."),
    faq("What are Oviedo's current watering days for new sod or landscaping?",
        f"The district splits addresses into two groups year-round: odd and no-number households get Wednesday and Saturday, even-numbered households get Thursday and Sunday, and the clock blocks any watering from 10 a.m. to 4 p.m. regardless of which day applies "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). A freshly sodded or seeded yard gets 30 days of unrestricted daily watering, then 30 more on an every-other-day cadence before it drops onto that normal two-day calendar."),
    faq("Does the 2026 permit exemption mean I can pour a patio slab in Oviedo without a permit?",
        "No. Oviedo's own carve-out list keeps a planning and zoning permit on non-structural 4-inch slabs on grade and on pavers, driveways and sidewalks on private property, even though the same work might clear the state's new $7,500 exemption threshold for a building permit elsewhere."),
    faq("Is there a published setback from the Econlockhatchee River or Lake Jesup for a pool deck or wall?",
        "Not one we found in either the city's or the county's permit guidance. A lot that slopes toward the river corridor or the lake gets its grading and fill checked on site, since the general rule is to keep water moving away from the house and off a neighbor's yard, not a specific foot count published for either waterway."),
    faq("How do I pick the best concrete contractor for a job in Oviedo?",
        f"Look the contractor up on the state's license-verification tool first, then make sure the quote already accounts for whichever office actually reviews your lot, Building Services or the county's Development Review Division, rather than guessing. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our guide to choosing a concrete contractor')} walks through the rest of what to check."),
    faq("Does a retaining wall in Oviedo need an engineer's drawings?",
        f"Yes, the city's wall permit guideline requires “signed and sealed engineered drawings” with wind design data for a freestanding or retaining wall, and it doesn't state a height below which that requirement drops away "
        f"({src('oviedo-permit-guidelines', 'City of Oviedo, Permit Guidelines')})."),
]

HUB = page("/oviedo-fl/", "city", "Concrete, Pavers & Turf Contractor in Oviedo, FL",
           "Opera builds concrete driveways, pavers and turf in Oviedo, FL, where a planning permit still covers pavers under the city's 2026 exemption list, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Oviedo Homes",
           capsule(f"As of October 2026, Opera pours concrete, sets pavers and installs artificial turf across Oviedo, a Seminole County city of about 41,317 residents sitting roughly {str(__import__('_data').CITIES['oviedo']['miles'])} miles from the Orlando unit's base. "
                   f"A new concrete driveway here falls in the {price('concrete-driveway')} per {per('concrete-driveway')} Florida market range, though a paver driveway or a patio slab still needs the city's own planning and zoning permit despite House Bill 803's 2026 exemption for smaller remodeling jobs."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Oviedo",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/seminole-county-driveway-patio-permits/", "Driveway and patio permits in Seminole County"),
                    ("/winter-springs-fl/", "Concrete, pavers and turf in Winter Springs"),
                    ("/lake-mary-fl/", "Concrete, pavers and turf in Lake Mary"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Oviedo, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Oviedo, FL – Permits",
    "meta": "Concrete driveway contractors in Oviedo, FL: the city's $104 right-of-way fee versus Seminole County's 18-foot width cap, as of October 2026.",
    "h1": "Pouring or Replacing a Concrete Driveway in Oviedo",
    "lede": capsule(f"A new or replacement concrete driveway in Oviedo runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "Inside the city, the private portion is reviewed separately from the apron crossing into the right-of-way, which carries its own $104 application fee; in unincorporated Seminole County, the whole driveway instead goes through a single county application capped at 18 feet wide."),
    "sections": [
        ("Inside Oviedo, the apron gets its own $104 right-of-way review",
         f"<p>Where a driveway meets the street, that section falls under the city's Right-of-Way Type I application, filed with the Development Review Division at 400 Alexandria Blvd., 407-971-5796. The current form, revised October 2023, totals $104.00, a $79.00 application fee plus a $25.00 technology fee, and the city also wants a sealed boundary survey, a maintenance-of-traffic plan and proof of insurance before it signs off "
         f"({src('oviedo-row-type1', 'City of Oviedo, Right-of-Way Type I Application')}). The rest of the slab on private ground is a separate planning and zoning permit, since Oviedo's own 2026 exemption list keeps driveways on private property out of the building-permit exemption HB 803 otherwise created "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}).</p>"),
        ("Outside the city, one county application sets the width at 18 feet",
         f"<p>A lot carrying an Oviedo address can still sit in unincorporated Seminole County, where the Residential Driveway Construction Application caps a driveway at 18 feet wide, 24 feet counting the 3-foot flares on each side, and requires 6 inches of non-steel or fiber-reinforced concrete at 3,000 psi inside the right-of-way "
         f"({src('seminole-driveway-app', 'Seminole County, Residential Driveway Construction Application')}). That review runs through the county's Development Review Division (Plandesk@seminolecountyfl.gov, 407-665-7371) rather than the city desk, and a driveway planned wider than 18 feet on an unincorporated lot is worth confirming against that cap before {cs('oviedo', 'paver-driveways', 'a paver driveway')} or a wide concrete apron gets designed.</p>"),
    ],
    "scenario": ("A two-car driveway crossing the right-of-way, worked out in square feet",
                 f"<p>Picture a 24 by 22 ft two-car driveway, 528 sq ft, replacing an original slab on a lot inside the Oviedo city limits. At {price('concrete-driveway')} per {per('concrete-driveway')}, the private portion lands between roughly $3,168 and $7,920 before demolition is added. "
                 "A 9 by 5 ft section of that same driveway, 45 sq ft, sits in the right-of-way where it meets the street, and that piece adds the separate $104 Right-of-Way Type I fee on top of the per-square-foot driveway cost, along with the survey and traffic-control plan the city asks for before approving it. On an otherwise identical lot in unincorporated Seminole County, that same width clears the county's 18-foot cap without a conditional review.</p>"),
    "faqs": [
        faq("Does Oviedo charge a separate fee for the part of my driveway that meets the street?",
            "Yes. The Right-of-Way Type I application covers that section, $79.00 plus a $25.00 technology fee, $104.00 total, filed with the Development Review Division along with a sealed survey, a traffic-control plan and proof of insurance."),
        faq("How wide can a driveway be in unincorporated Seminole County?",
            "The county's Residential Driveway Construction Application caps an ordinary driveway at 18 feet wide, 24 feet including the 3-foot flares on each side, reviewed by the Development Review Division rather than the city."),
        faq("Does Oviedo's 2026 permit exemption cover a new driveway?",
            "No. The city's own list of work that still needs a planning and zoning permit names “pavers/driveways/sidewalks on private property” directly, so HB 803's $7,500 building-permit exemption doesn't reach a driveway inside the city limits."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Oviedo, FL – 2026 Exemption",
    "meta": "Paver driveway installers in Oviedo, FL: why HB 803's 2026 exemption still leaves pavers on the city's planning-permit list, October 2026.",
    "h1": "Paver Driveways in Oviedo: What the 2026 Exemption Doesn't Cover",
    "lede": capsule(f"As of October 2026, expect {price('paver-driveway')} per {per('paver-driveway')} for a paver driveway in Oviedo, close to double the plain-concrete figure once material and base labor are counted. "
                     "The state's 2026 small-job exemption from a building permit doesn't change the review either: Oviedo's own guidance keeps pavers on private property squarely on its planning and zoning permit list."),
    "sections": [
        ("Pavers sit at the top of the city's non-exempt list, by name",
         f"<p>Oviedo's Building Services department publishes a list titled “Non-Structural residential work that would still require a planning and zoning permit through the Planning Department” to go alongside HB 803's new $7,500 exemption, and the very first line reads “Pavers/driveways/sidewalks on private property,” with a note that Engineering Department right-of-way permits are required separately for anything in the right of way "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). Call Building Services at 407-971-5755 before ordering pallets, since the exemption homeowners may have heard about from the new law simply doesn't apply to {svc('paver-driveways', 'a paver driveway')} inside the city.</p>"),
        ("The slab-and-paver package wants two site plans, not a stack of paperwork",
         f"<p>Once the permit applies, Oviedo's own paver permit guidelines, last revised January 2021, ask for a notarized building permit application, the contractor's license, general liability and workers' compensation insurance naming the city, and two site plans showing the distance from the paved area to the property line "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}). That packet covers a driveway the same way it covers a {svc('paver-patios', 'patio')} or a {svc('pool-deck-pavers', 'pool deck')}, so gathering the insurance documents and site plan ahead of ordering material keeps the application from stalling at the counter.</p>"),
    ],
    "scenario": ("A paver driveway sized to Seminole County's maximum width, worked out in square feet",
                 f"<p>Consider an 18 by 32 ft paver driveway, 576 sq ft, on an unincorporated Seminole County lot sized to the county's own 18-foot maximum width. At {price('paver-driveway')} per {per('paver-driveway')}, that job lands between roughly $5,760 and $17,280 depending on the paver and base depth. "
                 "Inside the Oviedo city limits, the same square footage still needs the planning and zoning permit the 2026 exemption list leaves in place, plus the slab-and-paver package's two site plans measuring distance to the property line, before the pallets show up on site.</p>"),
    "faqs": [
        faq("Does Florida's 2026 small-project exemption cover a paver driveway in Oviedo?",
            "No. The city's non-exempt list names pavers and driveways on private property directly, so the new $7,500 building-permit exemption that took effect July 1, 2026 doesn't reach that work inside the city limits."),
        faq("What documents does Oviedo's paver permit package require?",
            "A notarized building permit application, the contractor's license, general liability and workers' compensation insurance naming the city, and two site plans showing the distance from the paved area to the property line."),
        faq("Does a paver driveway need a different review than a concrete one in Oviedo?",
            "The underlying slab-and-paver permit package is the same either way. Where the two differ is on the exemption list itself, which calls out pavers, driveways and sidewalks together as work still requiring a planning and zoning permit."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Oviedo, FL – 4-In Slabs",
    "meta": "Concrete patio contractors in Oviedo, FL: why a non-structural 4-inch patio slab still needs a city permit, and flatwoods drainage, October 2026.",
    "h1": "Building a Concrete Patio in Oviedo",
    "lede": capsule(f"As of October 2026, a concrete patio in Oviedo falls between {price('concrete-patio')} per {per('concrete-patio')}. "
                     "Oviedo's own carve-out list keeps a standard 4-inch patio slab on grade on its planning and zoning permit roster, and the flatwoods ground under much of Seminole County holds water close enough to the surface to shape how that slab gets pitched."),
    "sections": [
        ("A non-structural 4-inch slab is still on Oviedo's permit list by name",
         f"<p>Oviedo's carve-out list for HB 803's 2026 exemption spells out “Non-structural 4\" concrete slabs on grade” as work that still needs a planning and zoning permit, sitting alongside pavers and driveways on the same list "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). A typical patio pour is exactly that, a 4-inch slab on grade rather than a footed foundation, so the exemption homeowners may expect from the new law doesn't apply here. The paperwork behind that review covers a patio the same application the city uses for {svc('concrete-slabs', 'a slab')}, a notarized permit form plus proof of the contractor's license and insurance, checked against how far the work sits from the lot line "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("Flatwoods ground sets the slope before the forms go up",
         f"<p>Seminole County's own water-quality program names Myakka fine sand, Florida's official state soil since 1989, as typical of the flatwoods ground found across the county "
         f"({ext(WATER_ATLAS_URL, 'Seminole County Water Atlas, Learn More: Soils')}; {src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}). Ground like that can hold a water table close to the surface for part of a typical year, so a patio's pitch has to carry rainwater away from the house rather than let it pond against the slab, a detail worth checking on site rather than assuming a flat, dry backyard.</p>"),
    ],
    "scenario": ("A backyard patio addition on flatwoods ground, worked out in square feet",
                 f"<p>Say a home adds a 16 by 18 ft patio off the back of the house, 288 sq ft, replacing a bare patch of St. Augustine between the lanai and the yard. Pricing that at {price('concrete-patio')} per {per('concrete-patio')} works out to roughly $1,728 to $3,744 before a broom or stamped finish changes the number. "
                 "Because the slab counts as non-structural 4-inch flatwork, it still needs Oviedo's planning and zoning permit even under the 2026 exemption, and because the lot sits on the kind of flatwoods soil common across the county, the crew checks where the yard already sheds water before the forms go in, rather than after.</p>"),
    "faqs": [
        faq("Is a concrete patio exempt from a permit in Oviedo under the 2026 law?",
            "No. The city's own list names “Non-structural 4\" concrete slabs on grade” as work that still needs a planning and zoning permit, which covers a typical backyard patio pour."),
        faq("Does Oviedo's soil affect how a patio drains?",
            "It can. Flatwoods ground common across Seminole County, including Myakka fine sand, Florida's official state soil, can hold a water table close to the surface for part of the year, which shapes a patio's slope more than it changes the mix design."),
        faq("What permit application covers a patio slab in Oviedo?",
            "The city's slab-and-paver package, the same one used for a driveway or pool deck: proof of licensing and insurance on file with the city, a notarized form, and a pair of site plans pinning down where the slab sits relative to the lot line."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Oviedo, FL – Econlockhatchee Lots",
    "meta": "Paver patio installers in Oviedo, FL on lots near the Econlockhatchee River and Lake Jesup, about 14 miles from Orlando, October 2026.",
    "h1": "Paver Patios and Walkways Around an Oviedo Home",
    "lede": capsule(f"A paver patio in Oviedo runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     f"The city sits about {str(__import__('_data').CITIES['oviedo']['miles'])} miles from the Orlando unit's base, bordered by Lake Jesup and the Econlockhatchee River, and a backyard that slopes toward either waterway needs its grading worked out before a paver base goes down."),
    "sections": [
        ("A lot near the Econlockhatchee or Lake Jesup drains differently than an inland yard",
         f"<p>The Econlockhatchee River, a 54.5-mile blackwater tributary of the St. Johns River, runs along Oviedo's eastern side, with the Little Econlockhatchee crossing the south, and the city itself grew up on the shore of Lake Jesup to the north "
         f"({ext(ECON_WIKI_URL, 'Wikipedia, Econlockhatchee River')}; {ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}). Neither the city's paver guidelines nor Seminole County's driveway application publishes a setback from either waterway for a patio, but a yard that slopes toward the river corridor or the lake has less room to shed rainwater than a flat inland lot, which is the kind of thing a crew checks with a level before cutting into the base.</p>"),
        ("A patio or walkway still goes through the same two-site-plan package",
         f"<p>Insurance naming the city, a notarized application and proof of the contractor's license round out Oviedo's slab-and-paver packet, along with two site plans locating the paved area against the property boundary "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}); that's the same packet whether the patio sits on a dry inland lot or one backing up to the Econ corridor. {cs('oviedo', 'concrete-patios', 'A poured concrete patio')} on the same lot goes through that identical review.</p>"),
    ],
    "scenario": ("A paver patio on a lot backing toward the Econlockhatchee corridor, worked out in square feet",
                 f"<p>Take a home on the east side of Oviedo, a 20 by 15 ft paver patio, 300 sq ft, added off the back of the house on a lot that slopes gently toward the Econlockhatchee floodplain. Figuring {price('paver-patio')} per {per('paver-patio')} puts that job around $3,000 to $5,100 depending on the paver and pattern chosen. "
                 "Before the base goes in, the crew checks where the existing yard already carries water toward the river corridor, since a patio poured flat against a lot that's already working with less fall than an inland yard can push water back toward the house instead of away from it.</p>"),
    "faqs": [
        faq("Is there a setback from the Econlockhatchee River for a paver patio in Oviedo?",
            "Not one published in the city's own paver guidelines or the county's driveway application. The practical question is grading: a yard sloping toward the river corridor has less natural fall to shed water than an inland lot, which gets checked on site before the base is cut."),
        faq("How far is Oviedo from the Orlando unit's base?",
            f"About {str(__import__('_data').CITIES['oviedo']['miles'])} miles. Oviedo sits in Seminole County, bordered by Lake Jesup to the north and the Econlockhatchee River along its eastern side."),
        faq("Does a paver patio need the same permit package as a driveway in Oviedo?",
            "Yes. The city's slab-and-paver guidelines use the same notarized application, insurance requirements and two-site-plan package for a patio, a driveway or a pool deck."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Oviedo, FL – 1997 Homes",
    "meta": "Concrete pool deck builders in Oviedo, FL: original 1997-era decks versus newer Oviedo on the Park construction, October 2026.",
    "h1": "Concrete Pool Decks for Oviedo Homes",
    "lede": capsule(f"As of October 2026, a concrete pool deck in Oviedo runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} in the Florida market. "
                     "The city's typical home dates to 1997, old enough that plenty of original decks are nearing three decades of wear, while newer construction around Oviedo on the Park is still pouring first decks rather than resurfacing anything."),
    "sections": [
        ("A deck from the city's median build year is old enough to need a closer look",
         f"<p>Oviedo's median year of home construction is 1997 "
         f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), old enough that a share of the city's original pool decks are showing the hairline cracking and worn cool-deck coating that call for a resurfacing decision rather than another spot patch. Notarized paperwork, proof of licensing and insurance, and two site plans pinpointing the deck's distance from the property line cover a replacement or an overlay the same way they cover new construction "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("Newer pools cluster around Oviedo on the Park",
         f"<p>The city's Oviedo on the Park development has added newer housing around Center Lake Park, described on the city's own site as “the crown jewel of the city's new Oviedo on the Park development area” "
         f"({src('oviedo-otp', 'City of Oviedo, Oviedo on the Park')}). A pool going in on a lot built in the last few years there is a first installation rather than a resurfacing job, and the deck's finished elevation gets set against current grading rather than whatever settling an older, 1997-era yard has already gone through.</p>"),
    ],
    "scenario": ("A new pool deck on recently developed ground, worked out in square feet",
                 f"<p>Picture a newer home near Oviedo on the Park pouring a 650 sq ft deck around a freshly set pool shell. Figuring {price('concrete-pool-deck')} per {per('concrete-pool-deck')} puts that job between roughly $3,250 for a plain broom finish and $9,750 for a cool-touch decorative surface. "
                 "A deck going in around an original 1997-era pool instead typically starts with a resurfacing conversation first, since the existing slab's cracking pattern decides whether an overlay holds up or a tear-out and repour makes more sense before the new finish goes on.</p>"),
    "faqs": [
        faq("Should I expect to resurface rather than replace an original Oviedo pool deck?",
            "Often, yes. With the city's median home dating to 1997, a lot of original decks are old enough for hairline cracking and a worn coating without being structurally compromised, which usually points toward resurfacing rather than a full tear-out."),
        faq("Is a pool deck permit different for a newer Oviedo on the Park home?",
            "No, the slab-and-paver permit package is the same whether the deck is a first installation or a resurfacing job, built around two site plans showing distance to the property line."),
        faq("What finish holds up best on an older Oviedo pool deck?",
            "A slip-resistant, cool-touch broom or textured finish wears better than a smooth trowel finish once the original coating is past its useful life, which is one reason resurfacing jobs on older decks often switch finishes rather than matching the original."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Oviedo, FL – Overlays",
    "meta": "Pool deck paver overlays in Oviedo, FL: resurfacing 1990s decks and the city's two-site-plan permit package, October 2026.",
    "h1": "Pool Deck Pavers in Oviedo: New Decks and Overlays",
    "lede": capsule(f"As of October 2026, pool deck pavers in Oviedo fall in the {price('pool-deck-pavers')} per {per('pool-deck-pavers')} range, whether they go down fresh or get set over an existing slab. "
                     "With the city's typical home dating to 1997, a share of the original cool-deck surfaces around Oviedo's older neighborhoods are old enough for a paver overlay instead of another patch."),
    "sections": [
        ("An original cool-deck surface from the late 1990s is a common overlay candidate",
         f"<p>Oviedo's median year of home construction is 1997 "
         f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), which puts a meaningful share of the city's original pool decks in the range where a worn coating and hairline cracking make a paver overlay worth pricing against a full tear-out. The city's own slab-and-paver guidelines, last revised January 2021, don't shorten the paperwork for an overlay either; it's the same notarized-application, licensed-and-insured, two-site-plan packet Oviedo uses for a first installation "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("Lots near Lake Jesup add a grading check before the pavers go down",
         f"<p>Oviedo grew up along Lake Jesup, and some of its older lakefront streets sit close enough to the water that the yard's slope matters more than it would a few blocks inland "
         f"({ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}). On a lot like that, the overlay's finished height has to account for whatever grading the original deck already set, since pavers laid directly over an existing slab inherit that slab's drainage pattern rather than starting from a clean grade.</p>"),
    ],
    "scenario": ("Weighing an overlay against a full tear-out",
                 f"<p>A 1990s-era home near Oviedo's older core has a 500 sq ft pool deck with a cracked, discolored cool-deck coating, and the owner is deciding between a paver overlay and starting over. Overlay pricing at {price('pool-deck-pavers')} per {per('pool-deck-pavers')} lands around $6,000 for a standard concrete paver and closer to $15,000 if travertine is chosen instead. "
                 "Going the tear-out route costs more up front once demolition is added, but it's the safer call if the original slab's cracking runs deep enough that an overlay would just telegraph the same lines through the new surface within a year or two.</p>"),
    "faqs": [
        faq("Can pavers go over an existing Oviedo pool deck without a full tear-out?",
            "Usually, as an overlay, reviewed under the same slab-and-paver permit package the city uses for new construction. How much the existing slab has already cracked or settled decides whether an overlay is the right call."),
        faq("Does a lakefront lot near Lake Jesup need special grading for pool deck pavers?",
            "No separate permit, but the slope matters more. An overlay set over an existing slab inherits that slab's drainage pattern, so the finished height gets checked against the yard's existing grade before pavers go down."),
        faq("Are older Oviedo pool decks more likely to need an overlay than new ones?",
            "Generally, yes. With the city's median home dating to 1997, a meaningful share of original pool decks are old enough that a worn coating and hairline cracking make an overlay worth pricing against a tear-out."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Oviedo, FL – Downtown Charm",
    "meta": "Stamped concrete contractors in Oviedo, FL: why a decorative slab still needs the city's planning permit, near the historic downtown, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Oviedo",
    "lede": capsule(f"As of October 2026, stamped concrete work in Oviedo falls between {price('stamped-concrete')} per {per('stamped-concrete')}, swinging with the pattern complexity and how many colors go into it. "
                     "The finish itself doesn't change which permit applies: Oviedo's 2026 exemption list keeps a decorative driveway or patio slab on its planning-permit roster right alongside a plain gray pour."),
    "sections": [
        ("A decorative finish doesn't move a slab off the city's permit list",
         f"<p>Oviedo's carve-out list for HB 803's 2026 exemption names “Pavers/driveways/sidewalks on private property” and “Non-structural 4\" concrete slabs on grade” without carving out an exception for color or pattern "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). A slate-pattern stamped driveway or an integral-color front walk still goes through the city's planning and zoning review, filing the identical notarized form, contractor's-license proof and insurance, plus two site plans locating the work against the lot line, that a plain broom-finish pour would need "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("Oviedo's historic downtown sets a different visual bar than its newer subdivisions",
         f"<p>Oviedo's historic downtown, once known for the chickens that roamed its streets, still carries older houses and storefronts along the Florida Trail and Cross Seminole Trail crossing "
         f"({ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}), a different visual context than the newer construction spreading out from Oviedo on the Park. A {svc('stamped-concrete', 'stamped walkway')} or driveway near the older core is more often matched to a historic-looking brick or slate pattern, while newer subdivisions further out see more uniform, contemporary colors.</p>"),
    ],
    "scenario": ("Pricing a slate-pattern entry and apron",
                 f"<p>A home near Oviedo's older core is swapping a 240 sq ft driveway apron and front walk for a slate-pattern stamped finish with an integral color. At {price('stamped-concrete')} per {per('stamped-concrete')}, that comes out to roughly $1,920 at the plain end and up to $4,560 for a more elaborate multi-color layout. "
                 "The permitting doesn't track the price up or down: because the work is still private-property flatwork, the city's planning and zoning review applies exactly as it would to an unadorned gray pour, and the section of apron meeting the street still needs its own right-of-way sign-off.</p>"),
    "faqs": [
        faq("Does stamped concrete need a different permit than plain concrete in Oviedo?",
            "No. The city's 2026 exemption carve-out list covers driveway and patio slabs generally, without an exception for a decorative finish, so a stamped pattern goes through the same planning and zoning review a plain pour would."),
        faq("Do homes near Oviedo's historic downtown favor a particular stamped pattern?",
            "There's no published rule requiring it, but a brick or slate-style pattern tends to read better against the older houses and storefronts downtown than it would in a newer subdivision, where more uniform colors are common."),
        faq("Does a stamped driveway apron still need the city's right-of-way permit?",
            "Yes, if any part of it crosses into the right-of-way. That review runs separately from the planning and zoning permit covering the private portion of the slab."),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Sidewalks & Walkways in Oviedo, FL",
    "meta": "Concrete walkway contractors in Oviedo, FL: the city's permit list for sidewalks on private property versus the right-of-way review, October 2026.",
    "h1": "Concrete Sidewalks and Walkways in Oviedo",
    "lede": capsule(f"A concrete walkway in Oviedo runs {price('concrete-walkway')} per {per('concrete-walkway')} as of October 2026. "
                     "The city groups sidewalks on private property with driveways and pavers on its 2026 exemption carve-out list, while a walkway section crossing into the right-of-way needs its own separate review."),
    "sections": [
        ("Private-property walkways share a line item with driveways and pavers",
         f"<p>Oviedo's non-exempt list reads “Pavers/driveways/sidewalks on private property” as a single line, so a front walk connecting the driveway to the entry doesn't clear HB 803's 2026 exemption any more than a driveway does "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). The same note on that list flags that Engineering Department right-of-way permits apply separately to “driveway/sidewalk work in the right of way,” a distinction worth checking before assuming a front-walk project is a single application.</p>"),
        ("The right-of-way section has its own $104 fee and paperwork",
         f"<p>Wherever a walkway crosses from the property line into the public right-of-way, Oviedo's Right-of-Way Type I application applies: $79.00 plus a $25.00 technology fee, with a sealed boundary survey, a maintenance-of-traffic plan and a certificate of insurance required alongside it "
         f"({src('oviedo-row-type1', 'City of Oviedo, Right-of-Way Type I Application')}). A path that stays entirely on private ground, connecting a side door to a patio rather than to the street, skips that particular review even though it still needs the planning permit covering private flatwork.</p>"),
    ],
    "scenario": ("A front walkway crossing the right-of-way, worked out in square feet",
                 f"<p>Consider a 4 by 35 ft front walkway, 140 sq ft, replacing a cracked original path from the driveway to the front door. At {price('concrete-walkway')} per {per('concrete-walkway')}, that lands between roughly $980 and $2,380. "
                 "Where that walk crosses the sidewalk strip near the street, the $104 Right-of-Way Type I fee and its paperwork apply on top of the planning permit covering the rest of the path; a side-yard walkway that never leaves private ground only needs the latter.</p>"),
    "faqs": [
        faq("Does a front walkway in Oviedo need a permit separate from the driveway?",
            "The city lists sidewalks, driveways and pavers on private property together on its 2026 exemption carve-out, so the planning review is similar either way. Where the walk crosses into the right-of-way, it adds a separate Right-of-Way Type I application."),
        faq("What does Oviedo's right-of-way permit cost for a sidewalk section?",
            "$104.00 total, a $79.00 application fee plus a $25.00 technology fee, along with a sealed boundary survey, a maintenance-of-traffic plan and proof of insurance."),
        faq("Does a side-yard walkway that stays on private property need the right-of-way permit?",
            "No, only the planning and zoning permit that covers private-property flatwork generally. The right-of-way review applies specifically to the section that crosses from the property line into the public strip."),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Oviedo, FL – Shed Pads",
    "meta": "Concrete slab contractors in Oviedo, FL: the city's 4-inch slab permit line and Seminole County's shed-size exemption, October 2026.",
    "h1": "Concrete Slabs for Sheds, Pads and Parking in Oviedo",
    "lede": capsule(f"As of October 2026, a concrete slab for a shed, an AC pad or boat and RV parking in Oviedo runs {price('concrete-slab')} per {per('concrete-slab')}. "
                     "Oviedo folds all of that under its non-structural 4-inch slab line, still subject to the city's planning and zoning permit, while unincorporated Seminole County's 2026 exemption list leaves slabs off entirely, covering only a shed structure itself once it's over 200 square feet."),
    "sections": [
        ("A 4-inch pad is on the city's permit list by name, regardless of use",
         f"<p>Oviedo's carve-out for HB 803's 2026 exemption names “Non-structural 4\" concrete slabs on grade” directly, a category that covers a shed pad, an AC pad or a small parking slab the same way it covers a patio "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). Getting that permit means filing a notarized application, proof of license and insurance naming the city, and two site plans marking the pad's distance to the property line "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("The county's shed exemption and the slab under it are two different questions",
         f"<p>In unincorporated Seminole County, the 2026 list of HB 803 exemptions names sheds of 200 sq ft or less among the non-structural work that no longer needs a building permit, alongside fences, pergolas and floating docks, but the same list doesn't mention driveways, pavers, slabs or retaining walls "
         f"({src('seminole-hb803', 'Seminole County, New State Legislation Affecting Permits')}). That gap means a small shed itself may be exempt while the concrete pad underneath it is worth a call to the county's Building Division at 407-665-7050 before assuming the same exemption covers both.</p>"),
    ],
    "scenario": ("Pricing an AC pad against a boat-trailer slab",
                 f"<p>Picture two small jobs on the same Oviedo lot: an 8 by 10 ft AC condenser pad, 80 sq ft, and a separate 12 by 20 ft parking slab for a boat trailer, 240 sq ft. Figuring {price('concrete-slab')} per {per('concrete-slab')}, the condenser pad runs somewhere around $320 to $800, and the parking slab runs roughly $960 to $2,400. "
                 "Both fall under the same non-structural 4-inch slab line on the city's planning permit, so neither one skips the paperwork just for being small. A few miles out in unincorporated Seminole County, that same parking slab still goes through standard county review, since the Building Division's own list of newly exempt work doesn't name slabs, pavers or walls at all.</p>"),
    "faqs": [
        faq("Does a shed slab need a permit in Oviedo under the 2026 exemption?",
            "Yes. The city's carve-out list keeps “Non-structural 4\" concrete slabs on grade” on its planning-permit roster, which covers a shed pad the same way it covers a patio or AC pad."),
        faq("Is a small shed exempt from a permit in unincorporated Seminole County?",
            "Sheds of 200 sq ft or less are on the county's 2026 list of exempt non-structural work. The concrete pad underneath isn't named on that same list, so confirming with the Building Division before pouring is worth the call."),
        faq("What paperwork slows down an Oviedo slab permit the most?",
            "Missing insurance documentation, typically. The city wants a notarized form, proof of licensing, and liability and workers' comp coverage naming Oviedo directly, plus two site plans marking the pad against the lot line, before the application moves."),
    ],
    "sources": SRC,
}

# 10. concrete-repair ----------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair & Resurfacing in Oviedo, FL",
    "meta": "Concrete repair and resurfacing in Oviedo, FL: cracking in 1997-era driveways and why Seminole isn't on the state's top sinkhole-claims list, October 2026.",
    "h1": "Concrete Repair and Resurfacing in Oviedo",
    "lede": capsule(f"As of October 2026, concrete repair and resurfacing in Oviedo runs {price('concrete-repair')} per {per('concrete-repair')} in the Florida market. "
                     "The city added more than 1,200 residents between the 2020 census and mid-2025, so freshly poured work now sits beside driveways and walkways dating back to the 1997 median build year, old enough that a resurfacing decision is coming due."),
    "sections": [
        ("A driveway from Oviedo's median build year has had nearly three decades of Florida weather",
         f"<p>Oviedo's typical home dates to 1997 "
         f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), old enough that a meaningful share of the city's original driveways and walkways show hairline cracking, a widened control joint or a chalky finish as ordinary wear rather than a warning sign. Whether a resurfacing job needs the full planning permit turns on whether it stays inside the existing footprint; Building Services at 407-971-5755 confirms the scope before material is ordered.</p>"),
        ("Seminole sits on shaky limestone ground, but not on the state's worst-claims list",
         f"<p>Florida Geological Survey staff describe the state's sinkhole-prone terrain as shallow limestone sitting under a mix of sand and clay, a description that reaches into parts of Seminole County along with Orange, Lake, Marion, Citrus, Sumter and Volusia. Yet when the Florida Senate tallied where the claims actually land, Broward, Miami-Dade, Citrus, Alachua, Orange, Polk, Marion, Pinellas, Hillsborough, Pasco and Hernando accounted for over 88 percent of the sinkhole insurance claims filed statewide between 2006 and 2009, and Seminole's name is missing from that group entirely "
         f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). On an Oviedo driveway, a dip or crack is far more often the flatwoods water table working against loose fill than the sudden ground loss that list is built around.</p>"),
    ],
    "scenario": ("A worn driveway heading toward a resurfacing decision",
                 f"<p>Consider a 420 sq ft two-car driveway, original to a home built around the city's 1997 median, now showing a network of hairline cracks along its control joints. Resurfacing it at {price('concrete-repair')} per {per('concrete-repair')} comes out somewhere between $1,260 and $4,200, cheaper for a plain broom finish and pricier once a decorative overlay is added. "
                 "Choosing a full tear-out and repour instead moves the job into driveway-pricing territory and reopens both the city's planning permit and, if the apron is involved, its separate right-of-way review.</p>"),
    "faqs": [
        faq("Is cracking in a 1997-era Oviedo driveway something to worry about?",
            "Usually not. Given the city's median home dates to 1997, a fine web of surface cracks and worn control joints on flatwork that age tends to be ordinary wear rather than a structural problem. A sudden, deep dip is the kind of thing worth a second look, a gradual hairline crack typically isn't."),
        faq("Does Seminole County see sinkhole activity the way some nearby counties do?",
            "Less than the counties the state's own claims data points to. Seminole shares the shallow-limestone geology found across parts of Central Florida, but it falls outside the eleven counties, led by Hernando, Pasco and Hillsborough, that generated most of the sinkhole insurance claims filed from 2006 through 2009."),
        faq("Does a smaller resurfacing job skip Oviedo's permit process?",
            "Sometimes, if it stays inside the slab's existing footprint; expanding the paved area pulls in the same planning review a new driveway needs. Calling Building Services before assuming a job is exempt avoids a surprise mid-project."),
    ],
    "sources": SRC,
}

# 11. paver-sealing -------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing & Restoration in Oviedo, FL",
    "meta": "Paver sealing and restoration in Oviedo, FL: why SJRWMD's watering schedule doesn't govern a pre-seal pressure wash, October 2026.",
    "h1": "Paver Sealing and Restoration in Oviedo",
    "lede": capsule(f"As of October 2026, cleaning, re-sanding and sealing pavers in Oviedo costs {price('paver-sealing')} per {per('paver-sealing')} in the Florida market. "
                     "A hose-fed pressure washer isn't the same category of water use as lawn irrigation under St. Johns River Water Management District's rules, so scrubbing pavers ahead of a seal doesn't have to wait for a particular address day."),
    "sections": [
        ("A pressure washer isn't bound by the district's address-day calendar",
         f"<p>St. Johns River Water Management District assigns sprinkler zones to specific days by address, odd and no-number addresses on Wednesday and Saturday, even addresses on Thursday and Sunday during Daylight Saving Time, with a 10 a.m. to 4 p.m. blackout window in between "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). That calendar is written around sprinkler heads watering grass; a crew blasting algae and grime off a paver surface with a hose-fed washer isn't the activity the rule describes, so the clean-and-re-sand prep ahead of sealing gets scheduled around the forecast and the job list instead of an assigned day.</p>"),
        ("A deck from the city's median build year is a common first-seal candidate",
         f"<p>With Oviedo's typical home dating to 1997 "
         f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), a lot of the original paver walkways and patios around the city are old enough that the first sealing application, or the first in years, is overdue rather than routine maintenance. Re-sanding with polymeric sand before sealing holds joints in place better on a surface that's gone that long without attention than a quick rinse and reseal would.</p>"),
    ],
    "scenario": ("A first-time seal on a long-neglected walkway",
                 f"<p>Say a 340 sq ft front walkway and entry patio, never sealed since it went down years ago, gets a full clean, a polymeric re-sand and its first coat of sealer. Pricing that at {price('paver-sealing')} per {per('paver-sealing')} comes out to roughly $510 to $1,105, with leveling a few sunken pavers near the entry pushing the total toward the higher end. "
                 "None of that prep waits on an address-based watering day, since the district's rule doesn't reach a pressure washer; the job books around whatever the forecast and the crew's calendar allow.</p>"),
    "faqs": [
        faq("Does an Oviedo address-day watering restriction limit when pavers can be pressure-washed?",
            "No. The district's schedule covers sprinklers irrigating grass, not a hose running through a pressure washer, so the pre-seal rinse and re-sand can happen whenever the crew and the forecast line up."),
        faq("Does a permit cover cleaning and sealing pavers that are already down in Oviedo?",
            "No. The city's slab-and-paver permit guidelines are built around new construction or replacing a paved area, not maintenance on a surface that's already in place."),
        faq("Why do so many Oviedo paver surfaces need their first sealing now?",
            "Oviedo's median home construction year, 1997, puts plenty of the original paver walkways and patios around the city past the point where a first or long-overdue sealing, not routine upkeep, is what the surface actually needs."),
    ],
    "sources": SRC,
}

# 12. retaining-walls -----------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Oviedo, FL – Engineering",
    "meta": "Retaining wall contractors in Oviedo, FL: the city's signed-and-sealed engineering requirement near the Econlockhatchee floodplain, October 2026.",
    "h1": "Retaining Walls for Oviedo Yards",
    "lede": capsule(f"As of October 2026, a retaining wall in Oviedo falls in the {price('retaining-wall')} per {per('retaining-wall')} Florida market range. "
                     "The city's own wall permit guideline requires signed and sealed engineered drawings for any freestanding or retaining wall, with no height written in below which that requirement drops away."),
    "sections": [
        ("Oviedo requires sealed engineering on a wall regardless of height",
         f"<p>Oviedo's permit guidelines for freestanding and retaining walls call for “signed and sealed engineered drawings” including wind design data, and the document doesn't name a height below which a homeowner could skip that step "
         f"({src('oviedo-permit-guidelines', 'City of Oviedo, Permit Guidelines')}). That's a stricter default than some nearby jurisdictions that simply don't publish a threshold at all; in Oviedo, the engineering requirement is the starting point, confirmed with Building Services at 407-971-5755 before a wall's design is finalized.</p>"),
        ("A yard sloping toward the Econlockhatchee or Lake Jesup usually has more fill to hold",
         f"<p>Oviedo sits along the Econlockhatchee River, a 54.5-mile blackwater tributary of the St. Johns River, with Lake Jesup bordering the city to the north "
         f"({ext(ECON_WIKI_URL, 'Wikipedia, Econlockhatchee River')}; {ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}). A lot that loses more elevation toward either waterway over its depth has more ground to hold back than a level inland yard does, a factor the sealed engineering on the wall's drawings works out before anything is built.</p>"),
    ],
    "scenario": ("Holding back a grade change near the floodplain",
                 f"<p>A yard on Oviedo's east side needs a 30 linear ft segmental block wall, 3 ft tall, 90 sq ft of wall face, to hold a grade that drops toward the Econlockhatchee floodplain. Pricing it at {price('retaining-wall')} per {per('retaining-wall')} works out to roughly $1,350 to $3,600 before drainage behind the wall is figured in. "
                 "Since the city's own guideline calls for signed and sealed engineered drawings regardless of the wall's height, that design step, wind data included, happens well before construction, not as an afterthought once block is already on site.</p>"),
    "faqs": [
        faq("Does a 2-foot retaining wall in Oviedo still need an engineer's drawings?",
            "Yes. The city's permit guideline applies signed and sealed engineered drawings, with wind design data, to any freestanding or retaining wall, and it doesn't carve out a lower height where that requirement stops applying."),
        faq("Why would a wall near the Econlockhatchee floodplain cost more than one on a flat lot?",
            "Mainly the fill and the drainage behind it. A lot that drops more sharply toward the river corridor or Lake Jesup is retaining more soil over the same wall length, and the engineered drawings have to size the wall and its drainage for that extra load."),
        faq("Who reviews a retaining wall permit in Oviedo?",
            "Building Services, reachable at 407-971-5755, using the city's own permit guidelines for freestanding and retaining walls rather than the slab-and-paver package used for driveways and patios."),
    ],
    "sources": SRC,
}

# 13. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Oviedo, FL – Water Rules",
    "meta": "Artificial turf installers in Oviedo, FL: the statewide water-body setback near Lake Jesup and SJRWMD's watering schedule, October 2026.",
    "h1": "Artificial Turf for Oviedo Yards",
    "lede": capsule(f"As of October 2026, artificial turf in Oviedo runs {price('artificial-turf')} per {per('artificial-turf')} in the Florida market. "
                     "A finished turf lawn doesn't appear anywhere in St. Johns River Water Management District's address-day watering calendar, since nothing underneath it needs irrigating, and on a lot backing up to Lake Jesup or the Econlockhatchee River, state rule keeps the turf itself 10 feet back from the water unless a seawall sits in between."),
    "sections": [
        ("A turf lawn has nothing for the district's watering calendar to govern",
         f"<p>Every address in Oviedo falls under St. Johns River Water Management District's split irrigation calendar, the odd-even, Wednesday-Saturday-versus-Thursday-Sunday rule covered on {cs('oviedo', 'paver-sealing', 'our paver-sealing page')} "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). Once turf replaces a struggling patch of St. Augustine, that calendar simply has nothing left to govern on that part of the yard, since a compacted, washed-rock base underneath turf doesn't take water the way sod's root zone does. That matters most on a flatwoods lot where grass has been fighting both a shallow water table and shade from mature trees.</p>"),
        ("The state's water-body buffer reaches lots along Lake Jesup and the Econ",
         f"<p>Florida's turf rule, effective May 19, 2026, keeps synthetic grass at least 10 feet from a natural or man-made water body unless a seawall or similar barrier sits between the lawn and the water, and it also requires natural infill, a washed subgrade and no in-ground irrigation line run underneath "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A companion 2025 law limits how much further a city or county can push its own turf restrictions past that state floor "
         f"({src('fs125572', 'Florida Statutes §125.572')}). Oviedo's own border along Lake Jesup and the Econlockhatchee River puts a fair number of backyards close enough to open water that the 10-foot line is worth measuring before the turf layout is finalized.</p>"),
    ],
    "scenario": ("Replacing a shaded, struggling lawn with turf",
                 f"<p>A side yard shaded by oak canopy has never held St. Augustine well, and the owner swaps 400 sq ft of bare, thinning grass for turf, keeping clear of a drainage swale at the back of the lot. At {price('artificial-turf')} per {per('artificial-turf')}, that job runs roughly $4,000 for a basic pile up to $10,000 for a thicker, more realistic build. "
                 "None of that square footage sits within 10 feet of open water, so the seawall exception never enters the conversation; a yard closer to Lake Jesup or the Econ corridor would need that distance checked first.</p>"),
    "faqs": [
        faq("Does turf in Oviedo need to follow an assigned watering day?",
            "No. The district's schedule assigns irrigation days by address for sprinklers watering grass, and turf doesn't need watering once its base is compacted, so it falls outside that calendar entirely."),
        faq("How far must artificial turf stay from Lake Jesup or the Econlockhatchee River?",
            "At least 10 feet under the statewide turf rule, unless a seawall or similar barrier separates the lawn from the water. The same rule bars in-ground irrigation under the turf and calls for natural infill over a washed base."),
        faq("Can an HOA in Oviedo require something stricter than the state's turf rule?",
            "A local government can't go far past the state's baseline standard under the 2025 law, but an HOA's own architectural guidelines are a separate layer worth checking, since they aren't bound by that same state cap the way a city or county ordinance is."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
