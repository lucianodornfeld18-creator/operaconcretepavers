# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "south-venice"

WIKI_SOUTHVENICE_URL = "https://en.wikipedia.org/wiki/South_Venice,_Florida"
CENSUS_SOUTHVENICE_URL = "https://censusreporter.org/profiles/16000US1268100-south-venice-fl/"
SVB_HISTORY_URL = "https://southvenicebeach.org/about-us/history-of-south-venice-beach/"
SVB_FERRY_URL = "https://southvenicebeach.org/beach-ferry/"
MYSUNCOAST_ALLIGATOR_URL = "https://www.mysuncoast.com/2026/10/01/sarasota-county-launches-25-million-alligator-creek-restoration-project/"
YOURSUN_SEPTIC_URL = "https://www.yoursun.com/venice/news/countys-plan-to-eliminate-septic-tanks-on-hold/article_1c8f35ec-74b0-11ed-8507-6bd5c5445bc2.html"

SRC = [
    "sarasota-county-row-permit", "sarasota-county-98-3-culvert-row-fees", "sarasota-county-124-255-culverts",
    "sarasota-county-124-76-rsf-standards", "sarasota-county-124-283-nonconforming-isr", "sarasota-county-22-63-retaining-walls",
    "sarasota-county-online-permitting", "sarasota-county-building-page", "swfwmd-restrictions",
    "nrcs-eaugallie-osd", "nrcs-felda-osd", "dep-rule", "fs125572", "fs720-3045",
    ("Wikipedia, South Venice, Florida", WIKI_SOUTHVENICE_URL),
    ("Census Reporter, South Venice, FL (ACS 2020-2024 5-yr, B01003/B25035)", CENSUS_SOUTHVENICE_URL),
    ("South Venice Beach, History of South Venice Beach", SVB_HISTORY_URL),
    ("South Venice Beach, Beach Ferry", SVB_FERRY_URL),
    ("My Suncoast, Sarasota County launches $25 million Alligator Creek restoration project", MYSUNCOAST_ALLIGATOR_URL),
    ("Your Sun, County's plan to eliminate septic tanks on hold", YOURSUN_SEPTIC_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Who reviews a driveway or patio permit in South Venice, since there's no town hall here either?",
        "<p>South Venice has never been its own city; it's an unincorporated Sarasota County community, so a " + cs("south-venice", "concrete-driveways", "driveway") + " or " + cs("south-venice", "paver-patios", "patio") +
        " permit here goes to the county's Building Division rather than a local counter. Sarasota County's own code requires a Right-of-Way Use Permit for any work placed in the county right-of-way, no "
        "exception carved out for a long-platted subdivision like this one " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ", and the filing happens through the county's online system rather "
        "than a walk-in office " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") + ".</p>"
    ),
    sec(
        "Why does South Venice have so many canal lots, and what does that mean for a culvert permit?",
        "<p>Brothers Warren and Arthur Smadbeck bought roughly 3,000 acres here in the early 1950s and platted it into 19,587 lots as the South Venice subdivision, selling the first model home for "
        "$6,900 " + ext(SVB_HISTORY_URL, "South Venice Beach, History of South Venice Beach") + ". A large share of those lots back onto one of the community's many canals, which is why the county's culvert "
        "rule, a 20-foot minimum and 24-foot maximum pipe with grade and size set by the County Engineer before the driveway forms go up, shows up on so many South Venice applications " +
        src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ".</p>"
    ),
    sec(
        "What's the story behind South Venice's private beach ferry, and why does it matter for seawalls here?",
        "<p>Until 1965, footbridges carried South Venice residents across to the Gulf side at Manasota Key; that year, the Army Corps of Engineers dredged Lemon Bay into part of the Intracoastal "
        "Waterway, removed the footbridges, and funded a replacement ferry and dock instead " + ext(SVB_HISTORY_URL, "South Venice Beach, History of South Venice Beach") + ". The South Venice Civic Association has "
        "run that ferry ever since, and the same community sits on canals lined with private seawalls that predate most of today's stormwater rules " + ext(SVB_FERRY_URL, "South Venice Beach, Beach Ferry") +
        ". A retaining wall over 4 feet high anywhere in the county, canal lot or not, still needs an engineer's drawing before it goes in " + src("sarasota-county-22-63-retaining-walls", "Sarasota County Code §22-63") + ".</p>"
    ),
    sec(
        "Why does South Venice keep coming up in the county's septic-to-sewer conversations?",
        "<p>Sarasota County has spent more than two decades converting septic systems to sewer in the Phillippi Creek basin, eliminating roughly 9,932 of them, but it's put a broader replacement program "
        "for the roughly 15,000 septic systems identified in South County, South Venice included, on hold until upgraded treatment plants come online " + ext(YOURSUN_SEPTIC_URL, "Your Sun, County's plan to eliminate septic tanks on hold") +
        ". Until that changes, a drain field on an older South Venice lot is something a new driveway, patio or turf layout still has to be graded around rather than over.</p>"
    ),
    sec(
        "What's happening with Alligator Creek, and how far is South Venice from our base?",
        "<p>Alligator Creek, a roughly 4-mile stream that drains this part of South County into Lemon Bay, is the subject of a $25 million county restoration project breaking ground this fall to reshape "
        "about 2.3 miles of what's now a straightened canal back into a more natural channel " + ext(MYSUNCOAST_ALLIGATOR_URL, "My Suncoast, Alligator Creek restoration project") + ". South Venice sits about 21 "
        "miles from the Sarasota unit's base, a drive we schedule alongside other South County stops like Venice and Nokomis rather than on its own.</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Does South Venice have its own building department?",
        "No. South Venice is an unincorporated Sarasota County community, so the County's Building Division reviews every driveway, patio and turf permit here through its online portal rather than a local counter."
    ),
    faq(
        "Does a South Venice driveway on a canal lot need a culvert permit?",
        "In most cases, yes, since the roadside swale on a typical South Venice lot carries a culvert the county reviews separately from the driveway surface, setting the pipe's length and grade under its own code before the pour."
    ),
    faq(
        "Is South Venice's canal network connected to the Gulf?",
        "Yes, through Lemon Bay and the Intracoastal Waterway. That connection is also why the community still runs a private beach ferry to Manasota Key, a holdover from when footbridges served the same purpose before the waterway was dredged in 1965."
    ),
    faq(
        "Will South Venice get county sewer service soon?",
        "Not on a fixed timeline. The county has put a broader septic-to-sewer program for South County, including South Venice, on hold until its treatment plants finish upgrading, so most homes here still run on private septic for now."
    ),
    faq(
        "Does the current watering restriction affect a South Venice lawn?",
        "Yes. South Venice sits inside SWFWMD's Modified Phase III shortage order, in effect through March 31, 2027, which holds irrigation to one assigned day a week. A turf lawn isn't bound by that schedule once it's installed."
    ),
]

HUB = page(
    "/south-venice-fl/", "city",
    "Concrete, Paver & Turf Contractor in South Venice, FL",
    "Concrete, pavers and turf for unincorporated South Venice, FL: Sarasota County's culvert permit on a 1952 canal subdivision, October 2026.",
    "Concrete Driveways, Pavers and Turf for South Venice Canal Lots",
    capsule(
        "South Venice is an unincorporated Sarasota County community platted in 1952 into nearly 20,000 lots, many backing onto one of its canals. As of October 2026, the county's Building "
        "Division reviews every driveway, patio and turf permit here, a roadside culvert often needs its own sign-off, and much of South County's unconverted septic still sits under South Venice lots."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="South Venice",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/sarasota-county-driveway-patio-permits/", "Driveway and patio permits in Sarasota, Venice and North Port"),
        ("/venice-fl/", "Concrete, pavers and turf in Venice"),
        ("/nokomis-fl/", "Concrete, pavers and turf in Nokomis"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-patio-cost/", "Paver patio cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in South Venice, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in South Venice, FL – Canal Lots",
    "meta": "Concrete driveway installers in South Venice, FL: Sarasota County's culvert rule on a 1952-platted canal subdivision; range " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
    "h1": "Concrete Driveways on South Venice's Canal Lots",
    "lede": capsule(
        "A concrete driveway in South Venice costs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026. This subdivision was platted around a dense canal "
        "network back in 1952, and that same roadside swale is usually why a culvert permit from Sarasota County gets filed before the driveway permit rather than alongside it."
    ),
    "sections": [
        (
            "A 1950s canal subdivision meets a modern culvert rule",
            "<p>The Smadbeck brothers platted South Venice into 19,587 lots in 1952, decades before the county wrote its current culvert code " + ext(SVB_HISTORY_URL, "South Venice Beach, History of South Venice Beach") +
            ", so today's permit review still has to fit a drainage rule onto a street grid that predates it. Sarasota County's own code sets the culvert at 20 to 24 feet, built from reinforced or "
            "asphalt-coated corrugated pipe, with grade and size dictated by the County Engineer before the slab forms go up " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ".</p>"
        ),
        (
            "Filing the application on a community this size",
            "<p>There's no South Venice counter to walk a permit into; the county's online portal handles every Right-of-Way Use Permit application the same way it would for a driveway anywhere else in "
            "unincorporated Sarasota County " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") + " " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ". A straight "
            "resurfacing job that leaves the culvert alone sometimes clears faster, a distinction the county's building guidance draws, though confirming it by phone before assuming it avoids a stop-work surprise "
            + src("sarasota-county-building-page", "Sarasota County Building") + ".</p>"
        ),
    ],
    "scenario": (
        "Replacing a driveway on a South Venice canal lot, worked out in square feet",
        "<p>Picture an 18 by 44 foot driveway, 792 square feet, on a lot backing onto one of the community's canals, where the original 1950s culvert pipe has partly collapsed under decades of "
        "settling. At " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", the pour comes to $4,752 to $11,880, tightening toward roughly $6,336 to $9,504 inside the typical " +
        price("concrete-driveway", typical=True) + " band. Because the old pipe needs replacing anyway, the county's line-and-grade sign-off happens before either the culvert or the new slab goes in.</p>"
    ),
    "faqs": [
        faq(
            "Why do so many South Venice driveway jobs involve a culvert permit?",
            "Because the subdivision was platted in the early 1950s around an extensive canal and swale system, and nearly every lot's driveway crosses a roadside ditch that the county now reviews separately under its current culvert code."
        ),
        faq(
            "How long does a residential culvert pipe have to be in South Venice?",
            "Sarasota County's code sets a 20-foot minimum and a 24-foot maximum, with additional length allowed only where that particular ditch happens to run deeper than the standard section."
        ),
        faq(
            "Does a driveway resurfacing job in South Venice always need a new culvert permit?",
            "Not always. A resurfacing job that doesn't disturb the existing culvert pipe may clear review faster, though the county's Building Division confirms that case by case rather than guaranteeing it upfront."
        ),
    ],
    "sources": SRC,
}

# 2. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in South Venice, FL – Seawalls & Setbacks",
    "meta": "Paver patio installers in South Venice, FL: coverage limits on a canal lot and the county's retaining-wall rule; market range " + price("paver-patio") + " per " + per("paver-patio") + ".",
    "h1": "Paver Patios on South Venice Canal Lots",
    "lede": capsule(
        "A paver patio in South Venice runs " + price("paver-patio") + " per " + per("paver-patio") + " this October 2026. A canal lot here often pairs a straightforward patio with an older seawall, "
        "and the county's coverage limit that applies depends on exactly when the lot was platted."
    ),
    "sections": [
        (
            "Why the 50 percent rule, not the newer 35 percent one, usually governs here",
            "<p>The Smadbecks' 1952 plat predates Sarasota County's 35 percent RSF building-coverage standard by decades, so most South Venice parcels default instead to the county's older nonconforming "
            "rule, a 50 percent ceiling on impervious surface that counts a paver patio or pool deck directly and leaves grass and shell out of the tally " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") +
            ". A homeowner on one of the community's rarer, re-platted parcels is the exception who instead answers to that newer rule, which caps the house footprint rather than the paving beside "
            "it " + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ".</p>"
        ),
        (
            "A moving drainage picture on the creek that carries this area's runoff",
            "<p>Sarasota County is about to reshape 2.3 miles of Alligator Creek, the stream carrying much of South County's stormwater into Lemon Bay, under a $25 million restoration project breaking "
            "ground this fall " + ext(MYSUNCOAST_ALLIGATOR_URL, "My Suncoast, Alligator Creek restoration project") + ". That work won't touch most South Venice canals directly, but it's a reminder that the "
            "drainage pattern a patio gets graded against isn't fixed here the way it might be in a newer subdivision. Separately, any canal-side wall built or rebuilt past 4 feet in height still needs "
            "an engineer's drawing, whatever the age of the seawall next to it " + src("sarasota-county-22-63-retaining-walls", "Sarasota County Code §22-63") + ".</p>"
        ),
    ],
    "scenario": (
        "A patio built out to a canal-side seawall, worked out in square feet",
        "<p>Consider a 280 square foot paver patio planned between the back of the house and an existing seawall on one of South Venice's original 1952 canal lots. At " + price("paver-patio") +
        " per " + per("paver-patio") + ", the job runs $2,800 to $4,760, narrowing to about $3,360 to $4,480 inside the typical " + price("paver-patio", typical=True) + " band. Before pricing "
        "it, the driveway and any dock or deck already on the lot get added up against the parcel's 50 percent impervious ceiling, since whatever room is left over sets the real limit on the new patio's size.</p>"
    ),
    "faqs": [
        faq(
            "Why does the 1950s platting date matter for my South Venice patio?",
            "Because it predates the county's newer 35 percent building-coverage rule, most lots here fall under an older nonconforming standard instead: a 50 percent ceiling on paving, pool decks and the house combined, which leaves grass and shell out of the count."
        ),
        faq(
            "Does a patio built out to a seawall need an engineer's drawing?",
            "Only if the wall itself is being built or replaced above 4 feet in height, measured from its lowest adjacent grade. A patio surface tying into an existing, undisturbed seawall doesn't trigger that requirement on its own."
        ),
        faq(
            "Will the Alligator Creek project change drainage rules for a South Venice patio?",
            "Not directly for most lots, since the restoration work targets the creek corridor itself rather than the community's residential canals, but it signals that this area's stormwater routing is still being actively reworked rather than fixed in place."
        ),
    ],
    "sources": SRC,
}

# 3. artificial-turf --------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in South Venice, FL – Canal Buffer",
    "meta": "Artificial turf installers in South Venice, FL: the state's water-buffer rule on a canal-heavy subdivision; market range " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
    "h1": "Artificial Turf for South Venice Canal Lots",
    "lede": capsule(
        "A South Venice turf lawn costs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of this October. With canals running behind so many lots in this subdivision, the "
        "state's water-setback rule for turf is one of the first things we check before sketching out a layout."
    ),
    "sections": [
        (
            "Measuring from the seawall, not the fence line",
            "<p>DEP Rule 62-308.100 keeps a synthetic lawn at least 10 feet from open water unless a seawall already sets the property line, and requires a washed-rock base with natural infill "
            "wherever the turf does go in " + src("dep-rule", "DEP Rule 62-308.100") + ". On a canal lot platted back in the 1950s, that buffer gets measured off the actual bulkhead rather than a fence that "
            "may sit a few feet closer to or farther from the water than the property line itself, and the rule leaves no room for a local variance to loosen it " + src("fs125572", "F.S. 125.572") + ".</p>"
        ),
        (
            "An older lawn against a tighter watering schedule",
            "<p>South Venice sits inside SWFWMD's Modified Phase III shortage order, which has cut sprinkler use to a single assigned day a week through March 31, 2027 " + src("swfwmd-restrictions", "SWFWMD district restrictions") +
            ". On a lot whose sod has thinned out after decades of mowing and the occasional drought, that one weekly slot rarely brings a struggling lawn back on its own, which is a common reason turf "
            "comes up here instead of a fresh re-sod attempt. A turf panel installed where it can't be seen from the street or an adjoining lot also carries the HOA protection F.S. 720.3045 grants as of "
            "2026 " + src("fs720-3045", "F.S. 720.3045") + ".</p>"
        ),
    ],
    "scenario": (
        "Swapping a canal-lot lawn for turf behind an existing seawall, worked out in square feet",
        "<p>A homeowner on a South Venice canal lot wants 340 square feet of backyard converted to turf, backed by a seawall that's lined the canal edge since the 1960s. At " +
        price("artificial-turf") + " per " + per("artificial-turf") + ", the full range runs $3,400 to $8,500, landing closer to $4,080–$6,120 inside the usual " + price("artificial-turf", typical=True) +
        " window once backing and pile height are chosen. A wall built that long ago already marks the property line on paper, so the state's 10-foot buffer drops out of the math entirely, and the "
        "turf can run the full depth of the yard without a setback cut into it.</p>"
    ),
    "faqs": [
        faq(
            "Does a South Venice canal lot need special clearance for turf?",
            "No more than the statewide rule already requires everywhere: a 10-foot gap from the water, run from whatever bulkhead lines the canal. A property whose seawall already sits on the boundary line skips that gap requirement entirely."
        ),
        faq(
            "Why does turf come up so often for older South Venice lawns?",
            "A lawn that's been mowed and watered on this same canal-lot grid for seven decades often thins out faster than the district's one-day-a-week limit lets it recover, and at that point turf stops being a cosmetic swap and becomes the lower-maintenance fix."
        ),
        faq(
            "Does the South Venice Civic Association have its own turf rule?",
            "We haven't found a published architectural-review document from the association covering turf specifically, so a South Venice turf project generally answers to the county and state rules covered above; a homeowner in a separately deed-restricted pocket of the subdivision should still check that community's own documents."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
