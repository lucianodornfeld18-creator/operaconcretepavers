# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "montverde"

ORDINANCE_URL = "https://mcclibraryfunctions.azurewebsites.us/api/ordinanceDownload/14606/1185385/pdf"
BUILDING_URL = "https://mymontverde.com/building-department/"
WIKI_URL = "https://en.wikipedia.org/wiki/Montverde,_Florida"
CENSUS_URL = "http://censusreporter.org/profiles/16000US1246525-montverde-fl/"
BELLACOLLINA_URL = "https://www.bellacollina.com/golf-course"
POINT2_URL = "https://www.point2homes.com/US/Neighborhood/FL/Montverde-Demographics.html"

SRC = [
    ("Town of Montverde, Ordinance 2022-18, Land Development Code §4-84", ORDINANCE_URL),
    ("Town of Montverde, Building & Permitting Department", BUILDING_URL),
    ("Wikipedia, Montverde, Florida", WIKI_URL),
    ("Census Reporter, Montverde, FL", CENSUS_URL),
    ("Bella Collina Golf Club, Course Overview", BELLACOLLINA_URL),
    ("Point2Homes, Montverde, FL Demographics", POINT2_URL),
    "nrcs-candler-osd", "nrcs-tavares-osd",
    "sjrwmd-watering", "dep-rule", "fs125572",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("A driveway apron in Montverde has its own section of town code, not a generic permit note",
        f"<p>Section 4-84 of the Land Development Code, amended by Ordinance 2022-18, states plainly that no driveway or driveway apron may be built in Montverde without both a Zoning Clearance and a Building Permit from the Town "
        f"({ext(ORDINANCE_URL, 'Town of Montverde, Ordinance 2022-18')}). The apron itself has a published shape: at least 10 feet wide parallel to the road and 5 feet deep, built in asphalt or concrete to a standard that meets or exceeds the public roadway it ties into, and the driveway run from that apron to the property line has to be concrete, or cement concrete pavement rated 3,000 to 3,500 psi "
        f"({ext(ORDINANCE_URL, 'Town of Montverde, Ordinance 2022-18')}). The Building Department, 17404 Sixth Street, 407-469-2681, is the office that reviews a {cs('montverde', 'concrete-driveways', 'new driveway')} or an apron rebuild against that section before work starts "
        f"({ext(BUILDING_URL, 'Town of Montverde, Building Department')}).</p>"),
    sec("A town barely over two thousand people, growing by more than a third since 2020",
        f"<p>Montverde's 2020 census count was 1,655; Census Reporter's current estimate puts the town at 2,249, a jump of better than a third in a handful of years "
        f"({ext(WIKI_URL, 'Wikipedia, Montverde, Florida')}; {ext(CENSUS_URL, 'Census Reporter, Montverde, FL')}). Real-estate demographic trackers put the town's typical home construction year around 2000 "
        f"({ext(POINT2_URL, 'Point2Homes, Montverde, FL Demographics')}), which leaves a mix on the ground: original early-2000s slabs old enough for {svc('concrete-repair', 'repair or resurfacing')} to start coming up, next to the newer lots behind that growth figure.</p>"),
    sec("Hills, a private lake and a 50-foot drop on one golf hole explain the grading",
        f"<p>Montverde sits on hills that climb 50 to 100 feet above Lake Apopka, with an average town elevation of 89 feet and a high point of 115 feet "
        f"({ext(WIKI_URL, 'Wikipedia, Montverde, Florida')}). Bella Collina, a 1,900-acre gated community built into those hills above Lake Apopka and the private, spring-fed Lake Siena, carries a Nick Faldo-designed course where the first hole alone drops more than 50 feet in elevation, unusual terrain for a part of Florida that's normally flat "
        f"({ext(BELLACOLLINA_URL, 'Bella Collina Golf Club, course overview')}). A lot anywhere in town that drops sharply from the street is why {svc('retaining-walls', 'a retaining wall')} shows up on far more Montverde quotes than it would on level ground elsewhere in the Orlando unit.</p>"),
    sec("The same ridge sand under Clermont and Groveland runs under Montverde too",
        f"<p>Montverde's hills sit on the excessively drained Candler and Tavares soils common across this stretch of Lake County's sand-ridge country, both series with a water table that sits well below where a driveway or patio base ever reaches "
        f"({src('nrcs-candler-osd', 'NRCS, Candler series')}; {src('nrcs-tavares-osd', 'NRCS, Tavares series')}). That combination of loose, fast-draining sand and real elevation change means a compacted base here is doing double duty, holding a stable grade in sand that drains almost too well while still carrying the slope.</p>"),
    sec("Montverde Academy anchors the south shore of Lake Apopka",
        f"<p>Montverde Academy, a private boarding and day school on the town's Lake Apopka shoreline, is the single institution most outsiders associate with the town's name "
        f"({ext(WIKI_URL, 'Wikipedia, Montverde, Florida')}). Homes clustered near the Academy and along the lake shore tend to be older than the hillside developments further from the water, which is part of why a {svc('concrete-patios', 'patio')} or walkway job near the lake more often means working around an established yard than grading a bare lot.</p>"),
    sec("One watering day a week applies here the same as the rest of Lake County",
        f"<p>SJRWMD's Phase III Extreme Water Shortage order holds every Lake County address, Montverde included, to a single watering day: Saturday for odd-numbered addresses, Sunday for even-numbered, Tuesday for nonresidential irrigation, and never between 8 a.m. and 6 p.m. "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). On a hillside lot where runoff moves faster than it would on flat ground, new sod trying to establish under that single soak struggles more than it would elsewhere, a reason {svc('artificial-turf', 'artificial turf')} comes up for the steepest section of a Montverde yard.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Montverde require a permit for a new driveway?",
        "Yes, both a Zoning Clearance and a Building Permit, under Section 4-84 of the Land Development Code. The apron connecting to the road has its own published width and depth, and the driveway itself has to be concrete or cement concrete pavement built to a stated strength."),
    faq("What's the minimum apron width for a Montverde driveway?",
        "At least 10 feet wide measured parallel to the road and 5 feet deep, built in asphalt or concrete that meets or exceeds the standard of the public roadway it connects to."),
    faq("Why does Montverde have so many retaining walls compared to flatter towns nearby?",
        "The town sits on hills 50 to 100 feet above Lake Apopka, with developments like Bella Collina built into grades steep enough that one golf hole there drops more than 50 feet. A lot that falls off sharply from the street needs something to hold the grade at a driveway or patio edge."),
    faq("How old is the typical home in Montverde?",
        "Real estate demographic data puts the town's typical construction year around 2000, though homes near the older lakefront and the Montverde Academy campus tend to run older than the hillside subdivisions that have grown up more recently."),
    faq("How do you choose the right concrete contractor for a Montverde project?",
        f"Confirm the bid accounts for both the Zoning Clearance and the Building Permit Section 4-84 requires, not just one of the two, and ask how the crew plans to handle grading on a sloped lot before it's priced. See {post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor')} for the broader checklist."),
]

HUB = page("/montverde-fl/", "city", "Concrete, Pavers & Turf Contractor in Montverde, FL",
           "Concrete, pavers and turf in Montverde, FL: the town's driveway apron code, its hillside lots near Bella Collina, and the Lake County watering order, Oct. 2026.",
           "Concrete, Pavers and Artificial Turf for Montverde, Florida Homes",
           capsule(f"Montverde is a small, hilly Lake County town of about 2,249 residents on the south shore of Lake Apopka, roughly 18 miles from Orlando, where grades of 50 feet or more aren't unusual. "
                   f"Opera builds concrete driveways, paver patios and artificial turf here; a new concrete driveway runs {price('concrete-driveway')} per {per('concrete-driveway')}, October 2026 Florida pricing, reviewed under the town's own apron and driveway code."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Montverde",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/lake-and-polk-county-driveway-permits/", "Driveway and patio permits in Lake and Polk counties"),
                    ("/groveland-fl/", "Concrete, pavers and turf in Groveland"),
                    ("/clermont-fl/", "Concrete, pavers and turf in Clermont"),
                    ("/retaining-wall-cost/", "Retaining wall cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Montverde, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Montverde, FL – §4-84",
    "meta": "Concrete driveway installers in Montverde, FL: the town's apron width rule and the 3,000-3,500 psi concrete standard under LDC §4-84, Oct. 2026.",
    "h1": "Concrete Driveways for Montverde's Hillside Lots",
    "lede": capsule(f"A new concrete driveway in Montverde is priced at {price('concrete-driveway')} per {per('concrete-driveway')}, October 2026 Florida figures. "
                     "Section 4-84 of the town's Land Development Code spells out both the apron's dimensions and the concrete strength the driveway itself has to meet, a level of detail most nearby towns leave to a general permit checklist."),
    "sections": [
        ("Two approvals, one published spec sheet",
         f"<p>Montverde requires a Zoning Clearance and a Building Permit for any driveway or apron, and the code doesn't stop at requiring the paperwork: the apron has to run at least 10 feet wide parallel to the road and 5 feet deep, built to match or exceed the abutting roadway, while the driveway from there to the property line has to be poured in concrete, or cement concrete pavement at 3,000 to 3,500 psi "
         f"({ext(ORDINANCE_URL, 'Town of Montverde, Ordinance 2022-18')}). The Building Department, 407-469-2681, reviews that submission before a crew breaks ground on a {cs('montverde', 'concrete-driveways', 'new Montverde driveway')} "
         f"({ext(BUILDING_URL, 'Town of Montverde, Building Department')}).</p>"),
        ("A sloped lot means the forms follow the grade, not a flat template",
         f"<p>With the town's hills running 50 to 100 feet above Lake Apopka, a Montverde driveway often has to step down or curve to follow a grade that a flatter inland lot would never present "
         f"({ext(WIKI_URL, 'Wikipedia, Montverde, Florida')}). That grading sits on top of the excessively drained Candler sand common under the town's hill country, soil that compacts well once it's properly worked but drains fast enough that standing water during the pour is rarely the issue it is on flatwoods ground elsewhere in the Orlando unit "
         f"({src('nrcs-candler-osd', 'NRCS, Candler series')}).</p>"),
    ],
    "scenario": ("A sloped driveway rebuild, worked out in square feet",
                 f"<p>A Montverde homeowner replacing a cracked 12 by 40 foot driveway that drops nearly 6 feet from the street to the garage is looking at 480 square feet of new concrete. Scaled to the {price('concrete-driveway')} per {per('concrete-driveway')} range, that comes to somewhere between $2,880 and $7,200, with the grade itself adding to the forming and finishing time versus a flat pour of the same size. "
                 "Because the apron at the road still has to hit the code's 10-foot width and 5-foot depth regardless of what the rest of the driveway does, that section gets built to spec first before the sloped run behind it is poured.</p>"),
    "faqs": [
        faq("Does a Montverde driveway need two separate approvals?",
            "Yes. Section 4-84 requires both a Zoning Clearance and a Building Permit for any driveway or driveway apron, not just one or the other."),
        faq("What concrete strength does Montverde require for a driveway?",
            "The town's code calls for concrete, or cement concrete pavement rated at 3,000 to 3,500 psi, for the stretch of driveway running from the road apron to the property line."),
        faq("Why do Montverde driveways often need extra grading work?",
            "Much of the town sits on hills 50 to 100 feet above Lake Apopka, so a driveway frequently has to step down or curve with the slope rather than running flat the way it would on level ground elsewhere in the Orlando unit."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Montverde, FL – Hillside Grading",
    "meta": "Paver patio installers in Montverde, FL: building on grades near Bella Collina and Lake Apopka, plus the town's permit office, Oct. 2026.",
    "h1": "Paver Patios for Montverde Hillside Homes",
    "lede": capsule(f"{price('paver-patio')} per {per('paver-patio')} is the current Florida range for a paver patio in Montverde this October 2026. "
                     "With much of the town built into hills above Lake Apopka, where a patio's base steps or terraces down a grade matters as much as the paver pattern chosen, and that work still runs through the town's Building Department."),
    "sections": [
        ("A terrace cut into a slope is a different build than a patio on a flat pad",
         f"<p>Bella Collina, the 1,900-acre gated community built into Montverde's hills above Lake Apopka and the private Lake Siena, sits on terrain steep enough that the golf course's first hole alone drops more than 50 feet "
         f"({ext(BELLACOLLINA_URL, 'Bella Collina Golf Club, course overview')}). A {svc('paver-patios', 'paver patio')} on a comparably graded lot elsewhere in town often needs a retaining edge or a stepped base rather than a single flat compacted pad, since the ground itself rarely sits level the way a Lake Apopka shoreline lot or a flatter inland town's lot would.</p>"),
        ("Lake-shore lots near Montverde Academy skew older than the hillside subdivisions",
         f"<p>Montverde Academy's campus runs along the town's Lake Apopka shoreline, and the homes clustered near it tend to predate the newer hillside developments that have driven the town's recent growth "
         f"({ext(WIKI_URL, 'Wikipedia, Montverde, Florida')}). A patio addition on one of those older lakefront lots is more often tied into an existing slab or screened lanai than built from scratch, which changes how the paver base ties into what's already there.</p>"),
    ],
    "scenario": ("A terraced hillside patio, worked out in square feet",
                 f"<p>A 14 by 20 foot paver patio on a Montverde lot that drops about 3 feet from the house to the yard's edge works out to 280 square feet, with a low retaining course needed to hold the lower terrace level. That footage against the {price('paver-patio')} per {per('paver-patio')} range comes to roughly $2,800 to $4,760, before the retaining course itself is priced separately. "
                 "Because the grade is doing more work than the paver pattern on a lot like this, the base gets stepped to the slope before the first course is set rather than forced flat against the hillside.</p>"),
    "faqs": [
        faq("Do Montverde patios need extra grading compared to flatter Orlando-area towns?",
            "Often, yes. With the town's hills running 50 to 100 feet above Lake Apopka, a patio base more commonly steps or terraces down a slope than it would on the flatter lots common elsewhere in the Orlando unit."),
        faq("Are lakefront patios near Montverde Academy built differently than hillside ones?",
            "They tend to tie into an older existing slab or lanai rather than start from a bare graded lot, since homes near the lake and the Academy generally predate the town's newer hillside subdivisions."),
        faq("Does a patio in Montverde need the same permit as a driveway?",
            "The town's Building Department reviews both, though the published code detail in Section 4-84 is written specifically for driveways and aprons; confirming a patio's exact requirements with that office before work starts is worth the call."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Montverde, FL – Sloped Yards",
    "meta": "Artificial turf installers in Montverde, FL: why sod struggles on hillside lots under the one-day watering order, plus the state's 10-foot lake setback, Oct. 2026.",
    "h1": "Artificial Turf for Montverde's Sloped Yards",
    "lede": capsule(f"Turf installation in Montverde runs {price('artificial-turf')} per {per('artificial-turf')}, current Florida figures for this fall. "
                     "Lake County's current order allows only one watering day a week, and on a hillside lot where water already runs off faster than it would on flat ground, that single soak leaves new sod with even less to work with."),
    "sections": [
        ("Slope plus one watering day makes for a hard combination",
         f"<p>Under SJRWMD's Phase III Extreme Water Shortage order, Montverde addresses water once a week, odd-numbered on Saturday and even-numbered on Sunday, with nothing allowed between 8 a.m. and 6 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). On a lot that drops toward Lake Apopka or one of the hills near Bella Collina, rainfall and irrigation alike run downhill before much of it soaks in, which is why new sod on a graded Montverde lot can struggle to establish even by the standard of a single-watering-day schedule, and why {svc('artificial-turf', 'artificial turf')} gets asked about for the steepest section of a yard specifically.</p>"),
        ("The 10-foot lake buffer matters more here than in a landlocked town",
         f"<p>Florida's statewide synthetic-turf rule sets a minimum 10-foot gap between installed turf and the edge of a pond, lake or canal, dropped only where a seawall takes the place of open shoreline, and it calls for a washed base with natural infill rather than buried irrigation underneath "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). With Lake Apopka forming Montverde's northern edge, more properties here sit within reach of that buffer than in towns without a comparable shoreline, and a 2025 statute limits how far local government can tighten residential turf rules beyond the state standard "
         f"({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
    ],
    "scenario": ("Turf on a graded slope above Lake Apopka, worked out in square feet",
                 f"<p>A side yard on a Montverde lot that slopes toward the lake, measuring 18 by 30 feet, covers 540 square feet once the required shoreline buffer is subtracted from the original footprint. At the {price('artificial-turf')} per {per('artificial-turf')} range, that comes to roughly $5,400 to $13,500 depending on the pile height and backing. "
                 "Because the slope sheds water fast, the base underneath gets extra attention to drainage during installation so runoff doesn't undercut the turf's edge after a heavy storm.</p>"),
    "faqs": [
        faq("Does Montverde's hilly terrain make artificial turf a better fit than sod?",
            "On the steepest sections of a yard, often yes, since runoff on a slope leaves less time for a single weekly watering to soak in than it would on flat ground, making new sod harder to establish there."),
        faq("How close to Lake Apopka can artificial turf be installed in Montverde?",
            "At least 10 feet back from the shoreline under the state's synthetic-turf rule, unless the edge is a seawall. No irrigation can be buried under the turf itself either way."),
        faq("Does Montverde's own code add turf rules on top of the state standard?",
            "The published Section 4-84 language covers driveways and aprons specifically; for turf, the 2025 state statute and the DEP rule are the primary framework, and confirming any town-specific add-on is worth a call to the Building Department."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
