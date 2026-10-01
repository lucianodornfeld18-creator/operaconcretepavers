# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "anna-maria-island"

WIKI_AMI_URL = "https://en.wikipedia.org/wiki/Anna_Maria_Island"
WIKI_ANNAMARIA_URL = "https://en.wikipedia.org/wiki/Anna_Maria,_Florida"
WIKI_HOLMESBEACH_URL = "https://en.wikipedia.org/wiki/Holmes_Beach,_Florida"
WIKI_BRADENTONBEACH_URL = "https://en.wikipedia.org/wiki/Bradenton_Beach,_Florida"
ANNAMARIA_BUILDING_URL = "https://www.cityofannamaria.com/178/Building-Department"
HOLMESBEACH_BUILDING_URL = "https://www.holmesbeachfl.org/departments/building_department/"
BRADENTONBEACH_BUILDING_URL = "https://www.cityofbradentonbeach.com/158/Building-Planning"
ANNAMARIA_HEIGHT_URL = "https://www.cityofannamaria.com/DocumentCenter/View/860/06132024-Ordinance-No-24-927-Section-107-_Height-Limitation_-To-Article-I-_Creations-and-Powers_"
ISLANDER_SUSPEND_URL = "https://www.islander.org/2025/02/bradenton-beach-suspends-building-official-in-wake-of-2-hurricanes/"
MYSUNCOAST_HELENE_URL = "https://www.mysuncoast.com/2024/09/30/anna-maria-island-residents-dealing-with-hurricanes-destruction/"
ANNA_MARIA_CODE_URL = "https://library.municode.com/fl/anna_maria/codes/code_of_ordinances"
HOLMES_BEACH_CODE_URL = "https://library.municode.com/fl/holmes_beach/codes/code_of_ordinances"
CENSUS_ANNAMARIA_URL = "https://censusreporter.org/profiles/16000US1201475-anna-maria-fl/"
CENSUS_HOLMESBEACH_URL = "https://censusreporter.org/profiles/16000US1232150-holmes-beach-fl/"
CENSUS_BRADENTONBEACH_URL = "https://censusreporter.org/profiles/16000US1207975-bradenton-beach-fl/"

SRC = [
    "fdep-cccl-program", "fdep-cccl-apply", "fema-coastal-firm", "fema-msc", "fdot-sdg", "swfwmd-restrictions",
    "dep-rule", "fs125572", "fs720-3045",
    ("Wikipedia, Anna Maria Island", WIKI_AMI_URL),
    ("Wikipedia, Anna Maria, Florida", WIKI_ANNAMARIA_URL),
    ("Wikipedia, Holmes Beach, Florida", WIKI_HOLMESBEACH_URL),
    ("Wikipedia, Bradenton Beach, Florida", WIKI_BRADENTONBEACH_URL),
    ("City of Anna Maria, Building Department", ANNAMARIA_BUILDING_URL),
    ("Holmes Beach, Building Department", HOLMESBEACH_BUILDING_URL),
    ("City of Bradenton Beach, Building & Planning", BRADENTONBEACH_BUILDING_URL),
    ("City of Anna Maria, Ordinance No. 24-927 (height limitation)", ANNAMARIA_HEIGHT_URL),
    ("The Anna Maria Islander, Bradenton Beach suspends building official in wake of 2 hurricanes", ISLANDER_SUSPEND_URL),
    ("My Suncoast, Anna Maria Island residents dealing with the hurricanes' destruction", MYSUNCOAST_HELENE_URL),
    ("Anna Maria Code of Ordinances", ANNA_MARIA_CODE_URL),
    ("Holmes Beach Code of Ordinances", HOLMES_BEACH_CODE_URL),
    ("Census Reporter, Anna Maria, FL (ACS 2020-2024 5-yr)", CENSUS_ANNAMARIA_URL),
    ("Census Reporter, Holmes Beach, FL (ACS 2020-2024 5-yr)", CENSUS_HOLMESBEACH_URL),
    ("Census Reporter, Bradenton Beach, FL (ACS 2020-2024 5-yr)", CENSUS_BRADENTONBEACH_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Anna Maria Island has three cities. Which one issues the permit for my project?",
        "<p>Unlike most of the towns we serve, Anna Maria Island isn't one place with one building department; it's three separate incorporated cities packed onto an eight-mile barrier island, each "
        "running its own code and its own counter " + ext(WIKI_AMI_URL, "Wikipedia, Anna Maria Island") + ". The City of Anna Maria covers the island's north end, Holmes Beach the middle, and Bradenton Beach "
        "the south end toward the Longboat Pass bridge, and a " + cs("anna-maria-island", "concrete-driveways", "driveway") + " or " + cs("anna-maria-island", "paver-patios", "patio") + " permit goes to "
        "whichever city's address the project sits in: Anna Maria's Building Department at 941-708-6132 " + ext(ANNAMARIA_BUILDING_URL, "City of Anna Maria, Building Department") + ", Holmes Beach's at "
        "941-708-5833 " + ext(HOLMESBEACH_BUILDING_URL, "Holmes Beach, Building Department") + ", or Bradenton Beach's Building & Planning Department at 941-778-1005 " + ext(BRADENTONBEACH_BUILDING_URL, "City of Bradenton Beach, Building & Planning") + ".</p>"
    ),
    sec(
        "Why do three cities on the same island have three different height limits?",
        "<p>Each city guards its own skyline separately. Anna Maria caps new construction at two habitable floors and 37 feet above the crown of the adjoining road under an ordinance the commission "
        "adopted in 2024 " + ext(ANNAMARIA_HEIGHT_URL, "City of Anna Maria, Ordinance No. 24-927") + "; Holmes Beach's limit runs to 36 feet, and Bradenton Beach's to 29, the lowest of "
        "the three " + ext(WIKI_HOLMESBEACH_URL, "Wikipedia, Holmes Beach, Florida") + " " + ext(WIKI_BRADENTONBEACH_URL, "Wikipedia, Bradenton Beach, Florida") + ". None of that touches a driveway or a patio "
        "directly, but it's a reminder that a rule confirmed in one of the three cities doesn't automatically carry across a city line a few blocks away.</p>"
    ),
    sec(
        "What did the 2024 hurricanes change about building on this island?",
        "<p>Hurricane Helene's storm surge in late September 2024 flooded essentially every ground-floor home on the island, by the Holmes Beach Police Department's own count, and Hurricane Milton followed "
        "less than two weeks later with sustained winds near 120 mph " + ext(MYSUNCOAST_HELENE_URL, "My Suncoast, Anna Maria Island residents dealing with the hurricanes' destruction") + ". Bradenton Beach's building "
        "official was suspended in the aftermath over how FEMA substantial-damage determinations and permit records were being handled " + ext(ISLANDER_SUSPEND_URL, "The Anna Maria Islander, Bradenton Beach building official") +
        ", and two of the island's three piers were destroyed outright. Two years later, a driveway, patio or pool-deck project on this island is as likely to be part of a storm rebuild, with an "
        "elevation certificate already on file, as it is a standalone upgrade.</p>"
    ),
    sec(
        "How much has the island's population changed since those storms?",
        "<p>All three cities counted fewer residents at the 2020 census than a decade earlier, and the slide hasn't reversed since: Anna Maria's latest five-year estimate puts it near 765 people, "
        "Bradenton Beach near 733, and Holmes Beach, the largest of the three, near 3,047 " + ext(CENSUS_ANNAMARIA_URL, "Census Reporter, Anna Maria") + " " + ext(CENSUS_BRADENTONBEACH_URL, "Census Reporter, Bradenton Beach") +
        " " + ext(CENSUS_HOLMESBEACH_URL, "Census Reporter, Holmes Beach") + ". A fair share of that shift is second homes changing hands or sitting mid-repair rather than people leaving outright, which is part of "
        "why a hardscape crew on this island spends as much time matching a rebuild's elevation as pricing a fresh pour.</p>"
    ),
    sec(
        "How exposed is a slab or a patio here to salt air, and how far is the island from our base?",
        "<p>FDOT draws its own marine-environment line at 2,500 feet from any chloride-heavy water, a chemistry threshold rather than a distance anyone eyeballs " + src("fdot-sdg", "FDOT Structures Design Guidelines") +
        ", and there isn't a lot on this island that falls outside it, bordered as it is by the Gulf on one side and Anna Maria Sound and Tampa Bay on the other " + ext(WIKI_AMI_URL, "Wikipedia, Anna Maria Island") +
        ". That exposure shortens how long a sealer or joint sand holds up compared with an inland job. Anna Maria Island sits about 16 miles from the Sarasota unit's base, the shortest drive of "
        "any town in this part of our service area.</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Is there one building department for all of Anna Maria Island?",
        "No. The island holds three separate incorporated cities, Anna Maria, Holmes Beach and Bradenton Beach, and each runs its own building department and its own code. A permit goes to whichever city the address falls in."
    ),
    faq(
        "Does every project on the island need a FEMA elevation certificate?",
        "Not every project, but a growing share do. After Hurricane Helene's surge flooded nearly every ground-floor home on the island, FEMA substantial-damage and elevation-certificate questions now come up on many rebuild projects, particularly in Bradenton Beach."
    ),
    faq(
        "Does Florida's coastal construction line reach Anna Maria Island?",
        "Yes, for anything seaward of it. Florida DEP's Coastal Construction Control Line program regulates construction and excavation activity along the island's Gulf-front beaches, on top of whatever each city's own code requires."
    ),
    faq(
        "Why would a contractor ask which of the three cities a project is in before quoting it?",
        "Because the permit process, the height limit and even how a storm-damage determination gets handled differ by city on this island. A quote that doesn't account for that is guessing rather than pricing the actual job."
    ),
    faq(
        "Does the regional water-shortage order apply on Anna Maria Island?",
        "Yes, in every one of the three cities alike. SWFWMD's Modified Phase III order has sprinklers across the whole district down to a single assigned day a week into the spring of 2027, and the island doesn't get a city-by-city exception."
    ),
]

HUB = page(
    "/anna-maria-island-fl/", "city",
    "Concrete, Paver & Turf Contractor on Anna Maria Island, FL",
    "Concrete, pavers and turf for Anna Maria Island, FL: three cities, three building departments and post-hurricane rebuilding, October 2026.",
    "Driveways, Patios and Turf Across the Island's Three Cities",
    capsule(
        "Anna Maria Island is three separate cities on one eight-mile barrier island: Anna Maria, Holmes Beach and Bradenton Beach, each with its own building department. As of October 2026, "
        "the island is still working through rebuilding from the 2024 hurricanes, and a driveway, patio or turf project here answers to whichever city's permit counter the address falls under."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Anna Maria Island",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/longboat-key-fl/", "Concrete, pavers and turf on Longboat Key"),
        ("/bradenton-fl/", "Concrete, pavers and turf in Bradenton"),
        ("/blog/manatee-county-driveway-permits/", "Driveway and patio permits in Manatee County"),
        ("/paver-patio-cost/", "Paver patio cost guide"),
        ("/artificial-turf-cost/", "Artificial turf cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf on Anna Maria Island, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways on Anna Maria Island, FL",
    "meta": "Concrete driveway installers on Anna Maria Island, FL: three cities' permit counters and Holmes Beach's width and setback rules; range " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
    "h1": "Concrete Driveways Across Anna Maria Island's Three Cities",
    "lede": capsule(
        "A concrete driveway on Anna Maria Island runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026. Anna Maria, Holmes Beach and Bradenton Beach each "
        "review a driveway permit through their own department, and Holmes Beach's code sets specific width and setback numbers the other two cities don't publish the same way."
    ),
    "sections": [
        (
            "Holmes Beach's own numbers for a narrow island lot",
            "<p>Holmes Beach caps the combined width of a driveway on a lot under 75 feet wide at half the lot's own width, measured where the drive meets the right-of-way, and keeps any driveway at "
            "least 10 feet from a street-line intersection or 6 feet along the right-of-way line, 6 feet from a side property line and 10 feet from the next driveway over " + ext(HOLMES_BEACH_CODE_URL, "Holmes Beach Code, zoning supplemental standards") +
            ". Those numbers matter on an island where plenty of lots are narrower than a mainland subdivision lot to begin with.</p>"
        ),
        (
            "Anna Maria and Bradenton Beach confirm case by case",
            "<p>Anna Maria's own code addresses driveway pavers placed in the right-of-way directly, under a permit the Building Department issues with Public Works sign-off, but a straightforward on-lot "
            "driveway question there, like one in Bradenton Beach, gets confirmed with that city's own department rather than assumed from a neighboring city's rule " + ext(ANNAMARIA_BUILDING_URL, "City of Anna Maria, Building Department") +
            " " + ext(BRADENTONBEACH_BUILDING_URL, "City of Bradenton Beach, Building & Planning") + ". Since Bradenton Beach sits entirely within a FEMA flood zone, a driveway tied into a storm rebuild there often "
            "comes with an elevation certificate already on file, which the permit review references directly.</p>"
        ),
    ],
    "scenario": (
        "Rebuilding a driveway after storm damage on a narrow Holmes Beach lot, worked out in square feet",
        "<p>Picture a 60-foot-wide Holmes Beach lot with an 18 by 40 foot driveway, 720 square feet, that cracked and settled after 2024's storm surge undermined the base beneath it. At " +
        price("concrete-driveway") + " per " + per("concrete-driveway") + ", the new pour runs $4,320 to $10,800, tightening to roughly $5,760 to $8,640 inside the typical " + price("concrete-driveway", typical=True) +
        " band. Because the lot is under 75 feet wide, the new driveway's width still has to clear half the lot's own width at the right-of-way line, the same limit that applied before the storm.</p>"
    ),
    "faqs": [
        faq(
            "Which city issues my driveway permit on Anna Maria Island?",
            "Whichever of the three incorporated cities the address sits in: Anna Maria, Holmes Beach or Bradenton Beach. Each runs a separate building department, so the permit never goes to a county office or to one of the other two cities."
        ),
        faq(
            "Does Holmes Beach limit how wide a driveway can be?",
            "On a lot under 75 feet wide, yes. The combined driveway width at the right-of-way line is capped at half the lot's own width, on top of separate setback distances from intersections, property lines and neighboring driveways."
        ),
        faq(
            "Does a driveway rebuild in Bradenton Beach need flood paperwork?",
            "Often, yes, since the city sits entirely within a FEMA-mapped flood zone. A rebuild tied to storm damage commonly references an elevation certificate or a substantial-damage determination already on file with the city."
        ),
    ],
    "sources": SRC,
}

# 2. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios on Anna Maria Island, FL",
    "meta": "Paver patio installers on Anna Maria Island, FL: Anna Maria's right-of-way paver rule and the island's salt-air exposure; market range " + price("paver-patio") + " per " + per("paver-patio") + ".",
    "h1": "Paver Patios on Anna Maria Island",
    "lede": capsule(
        "A paver patio on Anna Maria Island runs " + price("paver-patio") + " per " + per("paver-patio") + " this October. Nearly every lot on the island sits close enough to open saltwater that "
        "it matters more here than almost anywhere else we work, and Anna Maria's own code adds a specific rule for pavers that stray into the right-of-way."
    ),
    "sections": [
        (
            "Anna Maria's rule for a paver apron that reaches the right-of-way",
            "<p>Anna Maria's code lets a homeowner put a pervious brick paver system in the right-of-way with Building Department and Public Works sign-off, provided the pavers don't extend past the "
            "driveway's own border or 24 feet of width, whichever is less, and the owner records a non-exclusive maintenance agreement obligating perpetual upkeep " + ext(ANNA_MARIA_CODE_URL, "Anna Maria Code §114-421") +
            ". The city keeps the right to pull up or trim any paver system that turns into a hazard or blocks utility work, with no reimbursement owed for the loss " + ext(ANNA_MARIA_CODE_URL, "Anna Maria Code §114-421") + ".</p>"
        ),
        (
            "Why joint sand and sealer wear faster on this island than inland",
            "<p>FDOT's bridge engineers draw their marine-environment boundary at 2,500 feet from any chloride-heavy waterway " + src("fdot-sdg", "FDOT Structures Design Guidelines") + ", and on an island this narrow, "
            "bounded by the Gulf on one side and Anna Maria Sound or Tampa Bay on the other, that line sweeps in essentially every address " + ext(WIKI_AMI_URL, "Wikipedia, Anna Maria Island") + ". The paver base "
            "spec underneath doesn't change, but a sealer coat or polymeric joint sand that would last several seasons three miles inland needs a shorter recoat interval here.</p>"
        ),
    ],
    "scenario": (
        "A paver patio replacing a storm-damaged pool deck in Holmes Beach, worked out in square feet",
        "<p>Say a Holmes Beach cottage needs its 400 square foot paver patio replaced after 2024's flooding undermined the old base, on a lot close enough to Anna Maria Sound to sit well inside "
        "FDOT's marine-exposure line. At " + price("paver-patio") + " per " + per("paver-patio") + ", the job runs $4,000 to $6,800, narrowing to about $4,800 to $6,400 inside the typical " +
        price("paver-patio", typical=True) + " band once the paver grade and sealer spec are chosen. The old base gets excavated rather than reused, since storm-driven saturation is exactly the condition "
        "that undermines a compacted base from beneath.</p>"
    ),
    "faqs": [
        faq(
            "Can I put pavers in the right-of-way in front of my Anna Maria home?",
            "With a permit, yes, as long as the pavers stay within the driveway's own border or 24 feet of width, whichever is smaller, and the owner records a maintenance agreement committing to upkeep the paver system going forward."
        ),
        faq(
            "Can the city remove pavers I've installed in the right-of-way?",
            "Yes. Anna Maria's code reserves the right to trim or remove a paver system in the right-of-way if it becomes a hazard or blocks utility access, and it doesn't owe the owner reimbursement for that loss."
        ),
        faq(
            "Does a paver patio need resealing more often on this island?",
            "Often, yes. FDOT's own marine-chloride boundary covers nearly the whole island, and a sealer coat or polymeric joint sand under that much airborne salt typically needs attention on a shorter cycle than the same patio would a few miles inland."
        ),
    ],
    "sources": SRC,
}

# 3. artificial-turf --------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf on Anna Maria Island, FL",
    "meta": "Artificial turf installers on Anna Maria Island, FL: the state's 10-foot water-buffer rule on canal and bay-front lots; market range " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
    "h1": "Artificial Turf for Anna Maria Island Yards",
    "lede": capsule(
        "Expect " + price("artificial-turf") + " per " + per("artificial-turf") + " for turf on Anna Maria Island this October 2026. Between canal lots on the bay side and tight lots near the Gulf, "
        "a water-setback check belongs on nearly every layout here before the first measurement is final."
    ),
    "sections": [
        (
            "The 10-foot line that touches almost every yard on a narrow island",
            "<p>DEP Rule 62-308.100 keeps turf at least 10 feet back from open water, measured to a seawall where one exists or to the natural shoreline where it doesn't, and pairs that buffer with a "
            "washed-rock base, natural infill and a ban on in-ground irrigation beneath the turf " + src("dep-rule", "DEP Rule 62-308.100") + ". On an island this narrow, with canal frontage common on the bay "
            "side and Gulf frontage on the other, that measurement comes up on far more yards here than on a typical mainland subdivision lot, and none of the three cities can write a looser local rule "
            "around it " + src("fs125572", "F.S. 125.572") + ".</p>"
        ),
        (
            "Why a small lot with no room for a lawn still has room for a smaller rule check",
            "<p>Island lots tend to run small, which often means the realistic turf footprint is a side strip, a dog run beside a cottage, or the ground around a raised pool deck rather than a "
            "broad front lawn. Florida's current shortage order still caps irrigation at one assigned day a week for whatever sod survives nearby " + src("swfwmd-restrictions", "SWFWMD district restrictions") +
            ", and once turf replaces that strip, it draws nothing from a sprinkler system at all, a detail that matters on a lot where water pressure and the irrigation main are already stretched thin "
            "across the island's older infrastructure.</p>"
        ),
    ],
    "scenario": (
        "Converting a narrow side yard to turf on a Bradenton Beach canal lot, worked out in square feet",
        "<p>A Bradenton Beach cottage has a side yard running 6 feet wide by 30 feet long, 180 square feet, backing onto a canal where a seawall already lines the property edge. At " +
        price("artificial-turf") + " per " + per("artificial-turf") + ", the strip runs $1,800 to $4,500, settling closer to $2,160–$3,240 inside the usual " + price("artificial-turf", typical=True) +
        " window once backing and pile height are picked. Because the seawall itself forms the property line, the state's 10-foot buffer condition doesn't apply, and the layout runs the full length "
        "of the yard without a setback cut into it.</p>"
    ),
    "faqs": [
        faq(
            "Does a canal-front lot on Anna Maria Island need extra clearance for turf?",
            "Just the standard statewide one: a 10-foot gap back from the water, measured to the seawall where the lot has one. Where a seawall already sets the property line, that distance requirement drops away entirely."
        ),
        faq(
            "Is turf worth it on a small island lot with limited yard space?",
            "Many owners find a small, well-placed turf panel, a side strip or a pet run, more useful than a patchy lawn that's hard to water evenly on a tight lot, especially under the district's current one-day-a-week irrigation limit."
        ),
        faq(
            "Does which of the three cities I'm in change the turf rule itself?",
            "No. DEP's turf rule and the state law limiting local turf restrictions apply the same way in Anna Maria, Holmes Beach and Bradenton Beach; only the building permit process, where one applies, differs by city."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
