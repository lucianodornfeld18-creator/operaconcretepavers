# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "myakka-city"

WIKI_MYAKKA_CITY_URL = "https://en.wikipedia.org/wiki/Myakka_City,_Florida"
CENSUS_MYAKKA_CITY_URL = "https://censusreporter.org/profiles/06000US1208192290-myakka-city-ccd-manatee-county-fl/"
WIKI_SR70_URL = "https://en.wikipedia.org/wiki/Florida_State_Road_70"
WIKI_PARK_URL = "https://en.wikipedia.org/wiki/Myakka_River_State_Park"
FDOT_RULE_URL = "https://flrules.org/gateway/ruleno.asp?id=14-96.004"
OBSERVER_WELLS_URL = "https://www.yourobserver.com/news/2022/oct/19/manatee-county-continues-to-serve-myakka-residents-who-have-contaminated-water/"
BAYNEWS9_DEBBY_URL = "https://baynews9.com/fl/tampa/news/2024/08/08/water-level-to-rise-in-myakka-city-residents-continue-dealing-with-flooding"
ZONEOMICS_URL = "https://www.zoneomics.com/code/manatee-county-unincorporated-FL/chapter_2"

SRC = [
    "manatee-ldc-1004.2-access-drainage-permit", "manatee-driveway-application", "manatee-driveway-culvert-service",
    "manatee-paver-driveway-inspections", "manatee-no-permit-list", "manatee-phase3", "swfwmd-restrictions",
    "nrcs-myakka-osd", "fl-dos-state-soil", "dep-rule", "fs125572", "fs720-3045",
    ("Wikipedia, Myakka City, Florida", WIKI_MYAKKA_CITY_URL),
    ("Census Reporter, Myakka City CCD, Manatee County FL (ACS 2020-2024 5-yr, B01003/B25035)", CENSUS_MYAKKA_CITY_URL),
    ("Wikipedia, Florida State Road 70", WIKI_SR70_URL),
    ("Wikipedia, Myakka River State Park", WIKI_PARK_URL),
    ("Florida Administrative Code, Rule 14-96.004, Connection Categories and Fees", FDOT_RULE_URL),
    ("Your Observer, Manatee County continues to serve Myakka residents who have contaminated water", OBSERVER_WELLS_URL),
    ("Bay News 9, Water level to rise in the Myakka River as residents deal with flooding", BAYNEWS9_DEBBY_URL),
    ("Zoneomics, Manatee County Unincorporated zoning code summary, Ch. 2", ZONEOMICS_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Who reviews a driveway permit out here, since Myakka City has no town hall?",
        "<p>Myakka City was platted as a town in 1915 but never incorporated, so there's no city clerk's counter to walk a permit into " + ext(WIKI_MYAKKA_CITY_URL, "Wikipedia, Myakka City, Florida") +
        ". Manatee County's Public Works Infrastructure Engineering Division reviews the access and drainage permit for any " + cs("myakka-city", "concrete-driveways", "driveway") +
        " reaching from the property line to the road, a rule written broadly enough to cover a first pour on a new homesite the same way it covers a decades-old ranch "
        "driveway getting widened " + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC §1004.2") + ". Applications for most of the area go through Accela under Building, Public Works, Driveway/Culvert, "
        "with county staff reachable at 311 on weekdays " + src("manatee-driveway-culvert-service", "Manatee driveway/culvert permit service") + ".</p>"
    ),
    sec(
        "Why does a driveway fronting State Road 70 answer to a different office than one on a side road?",
        "<p>State Road 70 runs straight through the middle of Myakka City, narrowing to two lanes east of Lakewood Ranch on its way toward Arcadia " + ext(WIKI_SR70_URL, "Wikipedia, Florida State Road 70") +
        ", and that one road changes who signs off on a new or altered connection. Because SR 70 belongs to the state highway system, a driveway or apron tying into it needs a connection permit under "
        "Florida's own access-management rule, filed on the department's statewide form rather than the county's driveway application " + ext(FDOT_RULE_URL, "FAC Rule 14-96.004") +
        ". A homesite on Singletary Road, Wauchula Road or another county-maintained street stays with Manatee County's access and drainage permit instead " + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC §1004.2") + ", so which "
        "office gets the application often comes down to which road the mailbox sits on.</p>"
    ),
    sec(
        "What does one-acre A-1 zoning change about a driveway or a patio here?",
        "<p>Most of Myakka City sits inside Manatee County's A-1 Suburban Agricultural district, which sets a one-acre minimum lot (43,560 square feet), a 100-foot minimum lot width and a 50-foot front "
        "setback for a single-family home " + ext(ZONEOMICS_URL, "Zoneomics summary of Manatee LDC Ch. 4") + ". A setback that deep pushes the house, and whatever " + svc("concrete-driveways", "driveway") +
        " reaches it, well back from the road compared with a quarter-acre subdivision lot, which is also why a " + svc("paver-patios", "paver patio") + " or a " + svc("artificial-turf", "turf") +
        " lawn here tends to measure in the thousands of square feet rather than the few hundred a townhome lot allows. Manatee's own no-permit list still treats a non-structural concrete or paver patio as exempt from a building permit on "
        "a lot this size, the same as it would on a smaller one " + src("manatee-no-permit-list", "Manatee no-permit list") + ".</p>"
    ),
    sec(
        "What did Hurricane Debby's 2024 flooding show about building on this ground?",
        "<p>Tropical Storm Debby dropped 21.7 inches of rain on Myakka City in early August 2024, the highest total recorded anywhere in Florida during that storm, and the Myakka River's rise closed 14 "
        "miles of Myakka Road and Clay Gully Road while undermining three culverts " + ext(BAYNEWS9_DEBBY_URL, "Bay News 9, Myakka City flooding") + ". One resident told a reporter the only dry ground left on her "
        "property was \"the hill where the septic is,\" a line that captures how close a well and a drain field usually sit on a rural acre out here. Two years earlier, after Hurricane Ian's floodwater mixed "
        "with septic effluent, the county tested 319 private well samples and found coliform or fecal coliform bacteria in just over half of them, prompting free retesting and a bottled-water distribution "
        "point at the community center " + ext(OBSERVER_WELLS_URL, "Your Observer, Manatee County well contamination") + ". Grading a new driveway or patio pad to shed water away from both the wellhead and the septic "
        "mound matters more here than it does on a lot tied to county sewer.</p>"
    ),
    sec(
        "What's actually under a Myakka City slab, and how far is this from the Sarasota unit's base?",
        "<p>The flatwoods soil mapped across most of this part of eastern Manatee is Myakka fine sand, the soil the Legislature named Florida's official state soil in 1989 for covering more than 1.5 million "
        "acres statewide " + src("fl-dos-state-soil", "Florida state soil, Myakka fine sand") + ". Dig a test pit in it during the wet months and groundwater typically shows up less than two feet down before the "
        "ground dries back out later in the year, a pattern the federal soil survey logs as slow runoff on a profile it rates poorly to very poorly drained " + src("nrcs-myakka-osd", "NRCS OSD Myakka") + ". Myakka River State Park, 37,000 acres of wetlands and prairie that straddle the "
        "Sarasota-Manatee line a few miles southwest of here, sits on that same soil pattern " + ext(WIKI_PARK_URL, "Wikipedia, Myakka River State Park") + ". Myakka City itself is about 23 miles from the Sarasota "
        "unit's base, far enough that a same-day visit for a driveway or turf estimate gets scheduled around the drive rather than squeezed in on short notice.</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Does Myakka City have its own permitting office?",
        "No. Myakka City was never incorporated, so Manatee County's Public Works Infrastructure Engineering Division reviews the access and drainage permit for a driveway here, filed through the county's Accela portal rather than a town counter."
    ),
    faq(
        "Why would a Myakka City driveway need an FDOT permit instead of a county one?",
        "Only if the lot fronts State Road 70 itself, since that road belongs to the state highway system. A new or altered connection to it needs a Florida Department of Transportation connection permit; driveways on county-maintained side streets stay with Manatee County."
    ),
    faq(
        "Does a one-acre Myakka City lot need a bigger septic system or a bigger well?",
        "That's a Florida Department of Health question tied to the home's size and soil, not something a concrete or turf contractor sizes, but we do grade a new driveway, patio or turf base to shed water away from an existing wellhead and drain field rather than toward them."
    ),
    faq(
        "Does the current water-shortage order affect a Myakka City lawn?",
        "Yes. Manatee County is under SWFWMD's Modified Phase III shortage order through March 31, 2027, cutting irrigation to one assigned day a week. New sod gets a short daily-watering window first; turf answers to no sprinkler day once it's installed."
    ),
    faq(
        "How do you pick the best contractor for a driveway pour this far out from Sarasota?",
        "Ask directly whether the bid accounts for which office issues the permit on your road, state or county, and whether the crew has graded around a high water table before, rather than comparing a flat per-square-foot number against a closer-in job."
    ),
]

HUB = page(
    "/myakka-city-fl/", "city",
    "Concrete, Pavers & Turf Contractor in Myakka City, FL",
    "Concrete, pavers and turf for unincorporated Myakka City, FL: Manatee County's access permit, State Road 70's separate FDOT rule and flatwoods soil, October 2026.",
    "Driveways, Patios and Turf for Myakka City Acreage",
    capsule(
        "Myakka City is a rural, unincorporated crossroads in southeastern Manatee County, platted in 1915 and still zoned mostly one acre per lot. As of October 2026, Manatee County's Public Works "
        "division reviews every driveway and patio permit here, a State Road 70 address answers to FDOT instead, and the area's flatwoods soil and shallow water table shape how a slab or a turf base gets built."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Myakka City",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/manatee-county-driveway-permits/", "Driveway and patio permits in Manatee County"),
        ("/parrish-fl/", "Concrete, pavers and turf in Parrish"),
        ("/lakewood-ranch-fl/", "Concrete, pavers and turf in Lakewood Ranch"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/artificial-turf-cost/", "Artificial turf cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Myakka City, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Myakka City, FL – Permit Split",
    "meta": "Concrete driveway installers near Myakka City, FL: Manatee County's access permit versus FDOT's rule on State Road 70; market range " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
    "h1": "Pouring a Concrete Driveway on Myakka City Acreage",
    "lede": capsule(
        "As of October 2026, a concrete driveway near Myakka City prices out at " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", and the permit office depends on which "
        "road the lot touches: Manatee County's access and drainage permit covers most side streets, while a lot fronting State Road 70 answers to a separate FDOT rule instead."
    ),
    "sections": [
        (
            "Two permits for the same kind of pour, split by which road the lot touches",
            "<p>Manatee County LDC §1004.2.A requires an access and drainage permit before any part of a driveway between the property line and the road pavement is built, improved or widened, language that "
            "reaches a brand-new pour on a one-acre homesite the same way it reaches an older ranch driveway getting a second lane " + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC §1004.2") +
            ". That rule governs county-maintained roads; a driveway connecting straight onto State Road 70, which runs through the heart of Myakka City on its way toward Arcadia " + ext(WIKI_SR70_URL, "Wikipedia, Florida State Road 70") +
            ", instead needs a state connection permit under Florida's access-management rule, filed on the department's own statewide application form " + ext(FDOT_RULE_URL, "FAC Rule 14-96.004") + ".</p>"
        ),
        (
            "The county's own spec sheet for a residential pour",
            "<p>Where the county permit applies, its application sets a residential driveway at 12 feet minimum and 24 feet maximum in width, 6 inches thick from the edge of pavement to the right-of-way "
            "line, with an expansion joint between the new concrete and the existing curb " + src("manatee-driveway-application", "Manatee Driveway & Culvert Application") + ". Culvert and swale grades under the drive are "
            "set by county staff before the pour, not guessed at on site " + src("manatee-driveway-culvert-service", "Manatee driveway/culvert permit service") + ", a step that matters more here than on a drained ridge lot given how "
            "slowly this area's flatwoods soil moves water away from a driveway base.</p>"
        ),
    ],
    "scenario": (
        "Replacing a washed-out driveway apron after a summer storm, worked out in square feet",
        "<p>Picture a 14 by 60 foot gravel-and-concrete driveway, 840 square feet, running from a county road back to a homesite set 50 feet off the right-of-way under the area's one-acre zoning "
        + ext(ZONEOMICS_URL, "Zoneomics summary of Manatee LDC Ch. 4") + ", where the existing culvert collapsed after a wet summer. At " + price("concrete-driveway") + " per " + per("concrete-driveway") +
        ", the pour alone runs $5,040 to $12,600, tightening to roughly $6,720 to $10,080 inside the typical " + price("concrete-driveway", typical=True) + " band. Because the culvert failed, the job "
        "picks up the county's access and drainage permit alongside a culvert line-and-grade sign-off before either one gets built.</p>"
    ),
    "faqs": [
        faq(
            "Which office issues the driveway permit near Myakka City?",
            "Manatee County's Public Works Infrastructure Engineering Division handles any driveway on a county-maintained road. A driveway connecting directly to State Road 70 instead needs a Florida Department of Transportation connection permit."
        ),
        faq(
            "How wide can a residential driveway be in unincorporated Manatee County?",
            "The county's own application sets a 12-foot minimum and a 24-foot maximum width, measured at the edge of the road pavement, with the culvert's grade and size set by county staff before the pour."
        ),
        faq(
            "Does a one-acre lot's 50-foot setback change how long the driveway run is?",
            "Often, yes. A-1 zoning's 50-foot front setback pushes a typical Myakka City home well back from the road compared with a quarter-acre subdivision lot, which usually means a longer driveway run from the right-of-way to the garage."
        ),
    ],
    "sources": SRC,
}

# 2. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Myakka City, FL – Acreage Lots",
    "meta": "Paver patio installers near Myakka City, FL: building on one-acre A-1 lots and flatwoods soil; market range " + price("paver-patio") + " per " + per("paver-patio") + ", October 2026.",
    "h1": "Paver Patios on Myakka City's Acreage Lots",
    "lede": capsule(
        "A paver patio near Myakka City runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. Room is rarely the issue on a one-acre A-1 lot; the shallow water "
        "table under this area's flatwoods soil is what decides how thick the compacted base under the pavers needs to be."
    ),
    "sections": [
        (
            "Why a non-structural patio skips the permit counter entirely here",
            "<p>Manatee County's current no-permit list puts a non-structural concrete or paver patio outside the building-permit requirement, the same whether the lot is a quarter acre in a subdivision "
            "or a full acre out past Wauchula Road " + src("manatee-no-permit-list", "Manatee no-permit list") + ". That exemption doesn't reach a patio tied into a pool deck or one with footings, which still answer "
            "to the county's standard review, but a straightforward slab-on-grade " + svc("paver-patios", "paver patio") + " off the back of a ranch home generally doesn't need one.</p>"
        ),
        (
            "Myakka fine sand's water table sets the base depth, not the lot size",
            "<p>Myakka fine sand, the soil series the state legislature named Florida's official state soil for covering more than 1.5 million acres of flatwoods " + src("fl-dos-state-soil", "Florida state soil, Myakka fine sand") +
            ", is also one of the most common series mapped across this part of eastern Manatee County. The federal soil survey rates it poorly to very poorly drained, and on the low end of a yard "
            "groundwater can climb to knee height on a shovel for a few months most years " + src("nrcs-myakka-osd", "NRCS OSD Myakka") + ", the condition that pushes a base builder to add aggregate thickness no "
            "matter how much open ground surrounds the patio on a one-acre lot.</p>"
        ),
    ],
    "scenario": (
        "A paver patio off a ranch home's lanai, worked out in square feet",
        "<p>Say a homeowner on a one-acre Myakka City parcel wants a 22 by 16 foot paver patio, 352 square feet, added off an existing lanai, on ground that stays damp near a low corner of the yard "
        "most summers. At " + price("paver-patio") + " per " + per("paver-patio") + ", the project runs $3,520 to $5,984, narrowing to about $4,224 to $5,632 inside the typical " + price("paver-patio", typical=True) +
        " band once the extra base depth for the wet corner is priced in. Because the patio sits on grade with no footings, it stays off Manatee County's building-permit list, though the county's access permit "
        "rule still applies if any part of the work touches the driveway or the road frontage.</p>"
    ),
    "faqs": [
        faq(
            "Does a Myakka City patio need a Manatee County permit?",
            "A non-structural concrete or paver patio on grade, without footings, is currently on the county's no-permit list. A patio tied into a pool deck or built with footings still goes through the standard review."
        ),
        faq(
            "Why does the base under a Myakka City patio sometimes run thicker than normal?",
            "Myakka fine sand, the dominant soil series across much of this area, holds a seasonal high water table within about a foot and a half of the surface for part of most years, which calls for extra compacted aggregate under the pavers on the wetter stretches of a lot."
        ),
        faq(
            "Does a bigger acreage lot mean a bigger patio by default?",
            "Not necessarily. A one-acre A-1 lot has the room for a larger patio than a subdivision lot would, but most homeowners here size the patio to the house and the lanai rather than to the full acreage around it."
        ),
    ],
    "sources": SRC,
}

# 3. artificial-turf --------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Myakka City, FL – Well & Septic Lots",
    "meta": "Artificial turf installers near Myakka City, FL: DEP's no-irrigation rule on well-and-septic acreage lots; market range " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
    "h1": "Artificial Turf for Myakka City's Acreage Lots",
    "lede": capsule(
        "A Myakka City turf lawn runs " + price("artificial-turf") + " per " + per("artificial-turf") + ", current as of this October. Out here, where an acre typically runs its own well and "
        "septic system instead of county water and sewer, the state's ban on watering turf with in-ground irrigation happens to match what a well owner wants anyway: less draw on the same aquifer."
    ),
    "sections": [
        (
            "A rule written for sprinklers fits a well-water lot especially well",
            "<p>DEP Rule 62-308.100, effective May 19, 2026, bars using in-ground irrigation to water a synthetic turf area at all, on top of requiring a washed-rock base and natural infill " + src("dep-rule", "DEP Rule 62-308.100") +
            ". On county water that mostly changes a utility bill; on a private well, it means one less fixture drawing against the same aquifer that feeds the kitchen tap. After flooding mixed septic "
            "effluent into dozens of area wells following Hurricane Ian, Manatee County spent weeks distributing bottled water and testing samples for coliform bacteria " + ext(OBSERVER_WELLS_URL, "Your Observer, Manatee County well contamination") +
            ", a history that makes a lower-draw yard more than a line item for some homeowners out here.</p>"
        ),
        (
            "Capping a sprinkler zone instead of just switching it off",
            "<p>The state rule requires any sprinkler head that used to cover a lawn going to turf be capped below grade, not just shut off at the controller, since a pressurized line left live under turf "
            "eventually finds a seam or a low spot " + src("dep-rule", "DEP Rule 62-308.100") + ". On a lot where that same well also runs the house, capping the zone cleanly matters more than it would on a "
            "municipal connection, and Manatee County's own Modified Phase III order already limits that well-fed sprinkler system to one watering day a week through March 31, 2027 " + src("manatee-phase3", "Manatee Phase III restrictions") + ".</p>"
        ),
    ],
    "scenario": (
        "Converting a well-watered lawn to turf on a one-acre lot, worked out in square feet",
        "<p>A homeowner on a one-acre Myakka City lot is tired of running the home well dry keeping 2,400 square feet of front lawn green under the county's one-day watering window, and wants the "
        "front yard converted to turf while keeping the back acre in pasture grass for a couple of horses. At " + price("artificial-turf") + " per " + per("artificial-turf") + ", the front-yard "
        "conversion runs $24,000 to $60,000, with most comparable jobs landing in the typical " + price("artificial-turf", typical=True) + " band, near $28,800 to $43,200, once backing weight and pile "
        "height are chosen. The old zone's sprinkler heads get capped below grade before the washed-rock base goes in, and the well's draw drops the moment the old lawn stops needing water at all.</p>"
    ),
    "faqs": [
        faq(
            "Does turf make sense on a well-and-septic lot in Myakka City?",
            "Many homeowners here find it does, since the state's turf rule already bars in-ground irrigation on turf, which cuts one more fixture off a private well that may also be the only water source on the property."
        ),
        faq(
            "What happens to the old sprinkler zone under a new turf lawn?",
            "State rule requires capping the line below grade rather than leaving it live and switched off, since a buried, pressurized head eventually works its way up through a seam or a low spot in the turf."
        ),
        faq(
            "Does the county's water-shortage order affect a turf decision here?",
            "Indirectly. Manatee County's Modified Phase III order limits well-fed sprinkler systems to one watering day a week through March 31, 2027, which is often the reason a struggling lawn gets replaced rather than nursed along."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
