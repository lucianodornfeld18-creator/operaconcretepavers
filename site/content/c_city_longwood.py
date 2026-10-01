# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "longwood"

ROW_URL = "https://www.longwoodfl.org/612/Right-of-Way-Permit"
MOS_URL = "https://longwoodfl.org/DocumentCenter/View/4399/Manual-of-Standards-for-Subdivisions-PDF-ADA"
ISR_URL = "https://www.longwoodfl.org/DocumentCenter/View/6939/Impervious-calculation-form-PDF-"
HIST_URL = "https://www.longwoodfl.org/322/Historic-District"
HIST_NRHP_URL = "https://en.wikipedia.org/wiki/Longwood_Historic_District_(Longwood,_Florida)"
CR_POP_URL = "http://censusreporter.org/profiles/16000US1241250-longwood-fl/"
CR_YEAR_URL = "https://api.censusreporter.org/1.0/data/show/latest?table_ids=B25035&geo_ids=16000US1241250"

SRC = [
    ("City of Longwood, Right-of-Way Permit", ROW_URL),
    ("City of Longwood, Manual of Standards for City Streets and Stormwater Systems", MOS_URL),
    ("City of Longwood, Impervious Surface Calculation Form", ISR_URL),
    ("City of Longwood, Historic District", HIST_URL),
    ("Wikipedia, Longwood Historic District", HIST_NRHP_URL),
    ("Census Reporter, Longwood, FL", CR_POP_URL),
    ("Census Reporter API, Longwood median year structure built (B25035)", CR_YEAR_URL),
    "sjrwmd-watering", "dep-rule", "fs125572", "fs720-3045", "nrcs-smyrna-osd",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Longwood reviews its own driveways rather than routing them through the county",
        f"<p>Longwood is an incorporated city, so a driveway tying into a city street goes through Longwood's own right-of-way permit rather than Seminole County's driveway application; the fee for a residential driveway permit is $25, filed through the city's online SmartGov portal "
        f"({ext(ROW_URL, 'City of Longwood, Right-of-Way Permit')}). Longwood's Development Code section 2-424 spells out exactly which jobs in the right-of-way need that permit, driveway reconstruction among them, and City Hall's Community Development line, 407-260-3462, takes questions the portal checklist doesn't answer. Homes just outside the city limits still fall to Seminole County's own driveway construction application, a separate office with its own form and fee "
        f"({post('seminole-county-driveway-patio-permits', 'covered in our Seminole County permit guide')}).</p>"),
    sec("A culvert spec and a driveway rule most homeowners never read",
        f"<p>The city's public-works manual bans swaled driveway crossings outright: a driveway over a roadside ditch needs an actual drainage pipe with mitered ends or a concrete headwall, not a graded dip in the swale, and the minimum pipe size for a driveway crossing is 15 inches "
        f"({ext(MOS_URL, 'City of Longwood, Manual of Standards')}). Where a sidewalk crosses that same driveway, the manual doubles the normal 4-inch sidewalk thickness to 6 inches for the width of the crossing, because that strip of concrete also has to carry a vehicle's weight, not just foot traffic. A {svc('concrete-driveways', 'driveway apron')} that skips the culvert and pours a shallow dip instead is the kind of shortcut that shows up as standing water at the first afternoon storm.</p>"),
    sec("The 55 percent ceiling in Longwood's low-density residential zone",
        f"<p>Longwood's own impervious-area worksheet caps the low-density residential district at 55 percent impervious coverage, well above Winter Park's 50 percent citywide figure next door but still a real ceiling once a house, driveway, pool deck and any {svc('paver-patios', 'paver patio')} are added together on one lot "
        f"({ext(ISR_URL, 'City of Longwood, Impervious Surface Calculation Form')}). Other Longwood zoning categories run higher still, up to 80 percent along the US 17-92 corridor, so the number that applies depends on which district a given address sits in before any coverage math gets run.</p>"),
    sec("Thirty-seven buildings and a brick main street from the 1880s",
        f"<p>Longwood's historic district earned a spot on the National Register of Historic Places on October 5, 1990, covering roughly 190 acres and 37 contributing structures around the Longwood Hotel and the 1885 Bradlee-McIntyre House, a Queen Anne-style former winter cottage "
        f"({ext(HIST_NRHP_URL, 'Wikipedia, Longwood Historic District')}). Church Street through the oldest part of that district is still paved in brick rather than asphalt, the kind of surface a replacement {svc('concrete-walkways', 'walkway')} or driveway apron next to it has to read against rather than ignore "
        f"({ext(HIST_URL, 'City of Longwood, Historic District')}).</p>"),
    sec("A city whose typical home predates most of its Orlando-area neighbors",
        f"<p>Longwood's American Community Survey estimate puts the city at 16,337 residents, with a median year of home construction of 1983 "
        f"({ext(CR_POP_URL, 'Census Reporter, Longwood, FL')}; {ext(CR_YEAR_URL, 'Census Reporter API, B25035')}). That predates most of Oviedo's and Winter Garden's housing stock, and it sits on the Smyrna soil series common to this stretch of Seminole County, a poorly drained sand the USDA classifies with a high water table for one to four months in a typical year "
        f"({src('nrcs-smyrna-osd', 'NRCS soil survey, Smyrna series')}). A driveway or patio slab pushing past the four-decade mark on ground like that is due for {svc('concrete-repair', 'resurfacing')} on schedule, not because the original pour was flawed.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Longwood or Seminole County issue my driveway permit?",
        f"If the address sits inside Longwood's city limits, the city's own right-of-way permit applies, filed through its SmartGov portal for a $25 residential fee. Just outside those limits, the request goes to Seminole County's driveway construction application instead "
        f"({ext(ROW_URL, 'City of Longwood, Right-of-Way Permit')})."),
    faq("Why does a driveway culvert in Longwood need a specific pipe size?",
        "The city's manual of standards sets a 15-inch minimum for driveway-crossing culverts and bans a plain graded swale in place of a pipe, because an undersized or missing culvert backs water up against the road shoulder during heavy rain rather than carrying it through."),
    faq("How much of a Longwood lot can concrete or pavers cover?",
        "In the low-density residential district, the city's own worksheet caps total impervious coverage, house, driveway, patio and pool deck together, at 55 percent of the lot. Other zoning categories in Longwood allow a higher percentage, so the district matters before any math gets run."),
    faq("Does the Longwood Historic District affect a driveway or patio replacement?",
        f"The district itself is a National Register listing covering about 190 acres and 37 structures, not a blanket construction ban, but a project near Church Street's brick paving or one of its older structures is worth a call to Community Development before work starts "
        f"({ext(HIST_URL, 'City of Longwood, Historic District')})."),
    faq("Is most of Longwood's concrete original from the 1980s?",
        "The city's median home dates to 1983 per the latest Census estimate, which puts a sizable share of original driveways and patios at or past the point where cracking and resurfacing are expected rather than unusual."),
    faq("What should a Longwood homeowner check before hiring a concrete contractor?",
        f"Make sure the written bid already folds in the city's own right-of-way permit fee rather than adding it as a surprise later, ask directly how the crew prices a culvert crossing if the lot backs onto a drainage ditch, and run the contractor's name through the state's license-verification tool before signing anything. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our guide to choosing a concrete contractor')} covers the rest of what belongs in a solid estimate."),
]

HUB = page("/longwood-fl/", "city", "Concrete, Pavers & Turf Contractor in Longwood, FL",
           "Concrete, pavers and turf in Longwood, FL: the city's own $25 right-of-way permit, a 15-inch culvert rule, and the 55% LDR coverage cap, October 2026.",
           "Concrete, Pavers and Artificial Turf for Longwood Homes",
           capsule(f"Opera pours concrete and lays pavers and artificial turf in Longwood, where the going market range for a {price('concrete-driveway')} per {per('concrete-driveway')} concrete driveway applies the same as everywhere else in Greater Orlando, October 2026. "
                   "What's local is the paperwork: this Seminole County city of 16,337 residents reviews driveway work through its own right-of-way permit rather than the county's, and its median home was built in 1983."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Longwood",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/winter-springs-fl/", "Concrete, pavers and turf in Winter Springs"),
                    ("/altamonte-springs-fl/", "Concrete, pavers and turf in Altamonte Springs"),
                    ("/blog/seminole-county-driveway-patio-permits/", "Seminole County driveway and patio permits"),
                    ("/compare/concrete-vs-pavers/", "Concrete vs. pavers")],
           eyebrow="Concrete · Pavers · Turf in Longwood, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Longwood, FL – Permits",
    "meta": "Concrete driveway installers in Longwood, FL: the city's $25 right-of-way permit, a 15-inch culvert rule, and the 55% coverage cap, October 2026.",
    "h1": "Pouring a Concrete Driveway in Longwood",
    "lede": capsule(f"Pricing a concrete driveway in Longwood this October lands in the {price('concrete-driveway')} per {per('concrete-driveway')} market range. "
                     "What changes from one Seminole County address to the next is the review process: inside Longwood's limits, the city's own right-of-way permit applies, and a driveway crossing a roadside ditch needs an actual culvert pipe, not a graded dip."),
    "sections": [
        ("A city permit, not a county one, and a real culvert underneath",
         f"<p>Longwood's right-of-way permit covers driveway reconstruction directly, for a $25 residential fee filed through the city's online portal, separate from the driveway application Seminole County runs for unincorporated addresses "
         f"({ext(ROW_URL, 'City of Longwood, Right-of-Way Permit')}). Where the lot backs onto a roadside swale, the city's manual of standards requires a minimum 15-inch culvert pipe with mitered ends or a concrete headwall under the new slab; a swaled crossing with no pipe at all isn't an option the manual allows "
         f"({ext(MOS_URL, 'City of Longwood, Manual of Standards')}).</p>"),
        ("Fifty-five percent of the lot, driveway included",
         f"<p>In Longwood's low-density residential district, the city's impervious-area worksheet treats a driveway as part of a single 55 percent ceiling that also covers the house, any patio and the pool deck "
         f"({ext(ISR_URL, 'City of Longwood, Impervious Surface Calculation Form')}). A lot that already carries a full house footprint and a side patio can run into that number faster on a widened driveway than the driveway's own square footage would suggest on its own, which is worth checking against the worksheet before a width gets finalized.</p>"),
    ],
    "scenario": ("Replacing a 1980s driveway with a culvert crossing, worked out in square feet",
                 f"<p>Take a Longwood home built around the city's 1983 median construction year, where the original 10 by 22 foot driveway, 220 square feet, has cracked at the swale crossing. At {price('concrete-driveway')} per {per('concrete-driveway')}, a straight repour at that footprint runs roughly $1,320 to $3,300 before the permit fee, and because the lot backs onto a drainage ditch, the bid also has to cover a new 15-inch culvert pipe under the slab rather than reusing whatever shallow dip was there originally. Widening that same driveway to 24 feet for a second vehicle adds real square footage against the district's 55 percent ceiling, not just against the driveway's own budget.</p>"),
    "faqs": [
        faq("Is a Longwood driveway permit the same application as Seminole County's?",
            "No. Inside Longwood's city limits, the driveway goes through the city's own right-of-way permit for $25. Just outside the city limits, the same work falls to Seminole County's separate driveway construction application."),
        faq("What happens if a Longwood driveway crosses a roadside ditch?",
            "The city's manual of standards requires a minimum 15-inch culvert pipe with mitered ends or a concrete headwall under that section of driveway. A graded swale dip with no pipe isn't an accepted substitute."),
        faq("Does a driveway count toward Longwood's 55 percent coverage limit?",
            "Yes, in the low-density residential district the driveway is part of the same impervious-area total as the house, patio and pool deck, capped at 55 percent of the lot under the city's worksheet."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Longwood, FL",
    "meta": "Paver patio and walkway installers in Longwood, FL: the citywide coverage math, and a 6-inch sidewalk rule where a walk meets a driveway, October 2026.",
    "h1": "Paver Patios and Walkways for a Longwood Yard",
    "lede": capsule(f"A paver patio or walkway in Longwood runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "The same 55 percent impervious ceiling that governs a driveway in the city's low-density zone applies to a backyard patio, and a front walkway that meets a driveway apron follows its own thickness rule."),
    "sections": [
        ("A patio competes with the driveway for the same coverage headroom",
         f"<p>Longwood's impervious-area worksheet doesn't carve out a separate allowance for a patio; house, driveway, patio and pool deck are added together against the same 55 percent ceiling in the low-density district "
         f"({ext(ISR_URL, 'City of Longwood, Impervious Surface Calculation Form')}). On a lot that already has a wide driveway and a full-footprint house, adding a sizable {svc('paver-patios', 'paver patio')} out back is sometimes the addition that pushes the total closest to that limit, a math problem worth running before the layout is drawn rather than after.</p>"),
        ("Where a walkway crosses a driveway, the concrete underneath gets thicker",
         f"<p>Longwood's public-works manual sets ordinary sidewalks at a minimum 4 inches of portland cement concrete, 5 feet wide, but doubles that to 6 inches wherever the walk crosses a driveway, since that section also has to bear vehicle loads "
         f"({ext(MOS_URL, 'City of Longwood, Manual of Standards')}). A front paver walkway that ties into the driveway apron inherits that same reinforced-base expectation at the crossing point, even though the rest of the walk sits on a lighter base.</p>"),
    ],
    "scenario": ("A backyard patio and front walkway on one lot, worked out in square feet",
                 f"<p>Picture a Longwood home adding a 14 by 16 foot paver patio off the back door, 224 square feet, plus relaying a 3-foot-wide, 30-foot front walkway, 90 square feet, where it crosses the driveway apron. At {price('paver-patio')} per {per('paver-patio')} for the combined 314 square feet, that lands between roughly $3,140 and $5,024, with the walkway's crossing section built to the thicker driveway-grade base rather than the lighter spec used for the rest of the path.</p>"),
    "faqs": [
        faq("Does a backyard paver patio count toward Longwood's impervious limit?",
            "Yes. The city's worksheet totals the house, driveway, patio and pool deck together against the same 55 percent ceiling in the low-density residential district, so a new patio is weighed against whatever coverage the lot already carries."),
        faq("Why would a front walkway in Longwood need a thicker base in one spot?",
            "Where a walkway crosses a driveway, the city's manual of standards requires 6 inches of concrete instead of the normal 4-inch sidewalk thickness, since that section has to carry vehicle weight as well as foot traffic."),
        faq("Is a separate permit needed for a patio that doesn't touch the right-of-way?",
            "A patio entirely on private property doesn't trigger the right-of-way permit that covers driveway work, though it's still counted in the lot's overall impervious-coverage math and worth confirming with Community Development on a borderline lot."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Longwood, FL – Rules",
    "meta": "Artificial turf installers in Longwood, FL: the state's washed-base and water-setback rule, and the SJRWMD schedule turf sidesteps, October 2026.",
    "h1": "Artificial Turf for Longwood Lawns",
    "lede": capsule(f"Artificial turf in Longwood runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "The state's 2026 turf rule sets the build standard statewide, and on a 1983-median lot here, turf swaps out a sprinkler schedule that's been running on the same twice-a-week calendar for years."),
    "sections": [
        ("No city-specific turf ordinance, but a statewide build spec that still applies",
         f"<p>No Longwood ordinance addressing artificial turf was found, so the construction standard that governs an install here is the state's: Rule 62-308.100, effective May 19, 2026, calls for a washed base under the turf, natural infill rather than crumb rubber, no buried irrigation line beneath it, and keeping new turf 10 feet back from a pond or canal unless a seawall separates the two "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). F.S. 125.572, passed the year before that rule took effect, caps how aggressively a local government specifically can regulate residential turf beyond what the rule already requires "
         f"({src('fs125572', 'F.S. 125.572')}).</p>"),
        ("Turf drops off the irrigation calendar entirely",
         f"<p>Longwood, like the rest of Seminole County inside the St. Johns River Water Management District, runs a year-round lawn-watering calendar split by address, odd numbers and no-number homes on one pair of days, even numbers on another, with no watering allowed between 10 a.m. and 4 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}). A turf lawn has no irrigation zone left to schedule once it's installed, though if a homeowners' association's own documents don't already name turf, state law still limits what it can restrict to turf that's actually visible from the street or an adjoining lot "
         f"({src('fs720-3045', 'F.S. 720.3045')}).</p>"),
    ],
    "scenario": ("Swapping a front lawn for turf on an older Longwood lot, worked out in square feet",
                 f"<p>Consider a Longwood yard built around the city's 1983 median home age, where 500 square feet of St. Augustine along the front has thinned out under live oak shade. At {price('artificial-turf')} per {per('artificial-turf')}, turf for that area runs roughly $5,000 to $12,500 depending on pile height and backing, and because the state rule requires a washed base rather than whatever sand sits under the existing lawn, the install includes removing and replacing that base rather than laying turf directly over the old grade.</p>"),
    "faqs": [
        faq("Does Longwood have its own artificial turf ordinance?",
            "No city-specific rule was found; the construction standard that applies is the state's Rule 62-308.100, covering the base, infill and water-body setback the same way statewide."),
        faq("Does turf in Longwood still need to follow the SJRWMD watering schedule?",
            "No. The twice-a-week schedule governs irrigated sod and landscaping; a turf lawn has no sprinkler zone to schedule once it's in, though the lot's overall landscaping may still mix turf and irrigated beds under the same property."),
        faq("Can a Longwood HOA refuse turf that meets the state standard?",
            "Only to a point. Unless the association's own governing documents specifically address turf, state law limits what it can restrict to turf visible from the street frontage or an adjoining property."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
