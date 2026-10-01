# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, a, svc, city, cs, post, compare, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "winter-park"

CR_POP_URL = "https://censusreporter.org/profiles/16000US1278300-winter-park-fl/"
CR_YEAR_URL = "https://api.censusreporter.org/1.0/data/show/latest?table_ids=B25035&geo_ids=16000US1278300"
BRICK_URL = "https://cityofwinterpark.org/docs/departments/public-works-transportation/streets/BrickingPolicy.pdf"

SRC = [
    "winterpark-do-i-need-permit", "winterpark-58-65", "winterpark-driveway-permit", "winterpark-coverage-worksheet",
    "winterpark-row-faq", "winterpark-tree-ord", "winterpark-tree-permit", "sjrwmd-watering",
    "fs720-3045", "fs125572", "dep-rule",
    ("Census Reporter, Winter Park, FL (ACS 2024 5-yr)", CR_POP_URL),
    ("Census Reporter API, Winter Park median year structure built (B25035)", CR_YEAR_URL),
    ("City of Winter Park, Street Brick Policy", BRICK_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Winter Park runs its own permit counter",
        "<p>Winter Park is an incorporated city, so a drive or patio here goes through the city's own Building and Permitting Services office at 401 S. Park Avenue rather than Orange County's building division. "
        f"A building or miscellaneous permit covers “deck (wood, concrete, or other hard surfaces)… driveway… walls (including a retaining wall),” and work poured before that permit clears costs triple the normal fee "
        f"({src('winterpark-do-i-need-permit', 'City of Winter Park, Do I Need a Permit')}). Anything touching the curb, the sidewalk or the driveway approach itself is a second, separate application filed through the Engineering Division at 407-450-0815, apart from the office that reviews the lot "
        f"({src('winterpark-row-faq', 'City of Winter Park, Right of Way FAQ')}). {svc('concrete-driveways', 'A concrete driveway')} or {svc('retaining-walls', 'a retaining wall')} here can need both applications before a crew shows up.</p>"),
    sec("The §58-65 math: half the lot, half the front yard",
        f"<p>Winter Park's single-family code section 58-65 sets two separate limits at once: “buildings, accessory structures, patios, decks, drives and other impervious surfaces shall not cover more than 50 percent of the total land area of the lot,” and inside the front yard specifically, “at least 50 percent of the front yard area must consist of pervious surfaces with landscaping material” "
        f"({src('winterpark-58-65', 'City of Winter Park, Sec. 58-65 R-1A districts')}). A hard-surface or stone driveway in the front yard tops out at that same 50 percent ceiling, and the ordinance is blunt about one shortcut: “mulch drives are prohibited.” Stormwater from a new driveway has to stay on the property rather than sheet onto the street, and the worksheet homeowners fill out to check their math counts artificial turf as part of the impervious total, not as landscaping "
        f"({src('winterpark-driveway-permit', 'City of Winter Park, Driveway Permit Requirements')}).</p>"),
    sec("Thirty inches of trunk: Winter Park's own landmark-oak threshold",
        f"<p>Ordinance 3320-24, adopted October 17, 2024, protects “any tree measuring at least six inches DBH” the way most Central Florida tree codes do, but it also carves out a second, higher tier: a “landmark tree” is any live oak or bald cypress “in fair to excellent condition measuring thirty inches DBH or greater” "
        f"({src('winterpark-tree-ord', 'City of Winter Park Ordinance 3320-24')}). Any permit application tied to site work has to include a plan showing the proposed “sidewalks, pool decks, patios, fences, walls, driveways” against the trunks already on the lot, and a residential removal permit, where one is needed, runs $35 "
        f"({src('winterpark-tree-permit', 'City of Winter Park, Tree Removal Permit Application')}). On the older, oak-canopied streets common here, that landmark tier changes how a {svc('concrete-patios', 'patio')} or {svc('paver-patios', 'paver walkway')} gets laid out long before the first form goes up.</p>"),
    sec("A city built decades before its Orlando-area neighbors",
        f"<p>Winter Park's ACS five-year estimate puts the city at roughly 30,274 residents inside Orange County "
        f"({ext(CR_POP_URL, 'Census Reporter, Winter Park, FL')}), with a median year of home construction of 1976, the oldest housing stock of any Orlando-unit town in this coverage "
        f"({ext(CR_YEAR_URL, 'Census Reporter API, B25035')}). That half-century-plus age shows up as narrow original aprons poured to an older standard, root heave from mature canopy trees, and driveways that were never built to the current 50 percent lot math because the lot predates the current code. "
        f"{svc('concrete-repair', 'Concrete repair and resurfacing')} on a slab that old is routine work, not a sign anything went wrong structurally.</p>"),
    sec("Where brick pavement still carries traffic",
        f"<p>A chunk of Winter Park's street network was never asphalted over: the city's own streets policy counts close to 19 of its roughly 100-plus miles of public roadway as brick, material the policy credits with a working life of 40 to 50 years against roughly a third of that span for an asphalt resurfacing "
        f"({ext(BRICK_URL, 'City of Winter Park, Street Brick Policy')}). None of that changes the driveway-apron spec itself, but it does shape what a homeowner wants the apron to look like where it meets a brick segment, and it's the reason {svc('paver-driveways', 'a paver driveway')} in brick or brick-toned units comes up here more than in a town without an inch of brick pavement. The transition where a concrete or paver apron meets a brick lane is a detail worth a site visit rather than a phone estimate.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Winter Park require a permit for a new driveway?",
        f"Yes. The city treats a driveway, a hard-surface deck or a wall as a building or miscellaneous permit, filed with Building and Permitting Services, and work started first costs triple the standard fee. A separate right-of-way permit covers the curb and sidewalk portion where the driveway meets the street "
        f"({src('winterpark-do-i-need-permit', 'City of Winter Park, Do I Need a Permit')})."),
    faq("How much of my Winter Park lot can be covered in concrete or pavers?",
        "Code section 58-65 caps total impervious coverage at 50 percent of the lot, and at least half of the front yard specifically has to stay pervious and landscaped. Artificial turf counts toward that impervious total on the city's own worksheet, so it doesn't get treated as a landscaping credit."),
    faq("What size tree is protected in Winter Park?",
        "Any tree 6 inches or more in diameter at breast height is a protected tree under Ordinance 3320-24, and a live oak or bald cypress in fair to excellent condition at 30 inches or more earns a second tier, landmark status, with its own added protection."),
    faq("Do you install brick-look pavers that suit historic Winter Park homes?",
        f"Yes. Concrete pavers cast in a brick-toned color and a running-bond or herringbone pattern read close to the city's own brick streets without the per-unit cost of real clay brick, and a clay-brick border or edge course is an option where the budget allows it. "
        f"{compare('clay-brick-vs-concrete-pavers', 'Clay brick vs. concrete pavers')} walks through the cost and upkeep difference between the two."),
    faq("Why are so many Winter Park driveways older than the ones in newer Orlando-area suburbs?",
        "The city's median home was built in 1976, decades before towns like Clermont or Winter Garden saw most of their construction, so a larger share of the original concrete here is well past the point where cracking and resurfacing are routine rather than unusual."),
    faq("How do you pick the best concrete contractor for a Winter Park home?",
        f"Confirm the quote accounts for both the lot permit and the separate right-of-way application where the work touches the street, ask how the bid handles a protected or landmark tree on the property, and check the contractor on the state's license-verification tool before signing anything. "
        f"{post('hoa-approval-for-pavers-and-concrete', 'Getting HOA or ARC approval for pavers and concrete')} covers community-level review on top of the city's own process."),
]

HUB = page("/winter-park-fl/", "city", "Concrete, Pavers & Turf Contractor in Winter Park, FL",
           "Concrete, pavers and turf in Winter Park, FL: the city's 50% impervious-coverage cap, 30-inch landmark oaks, and 19 miles of brick streets, October 2026.",
           "Concrete, Pavers and Artificial Turf for Winter Park Homes",
           capsule("Opera pours concrete and lays pavers and artificial turf for Winter Park, an Orange County city of roughly 30,274 residents where the typical home dates to 1976, the oldest housing stock among the Orlando-unit towns covered here. "
                   f"As of October 2026, a concrete driveway runs {price('concrete-driveway')} per {per('concrete-driveway')}, and city code caps total lot coverage from concrete, pavers and turf at 50 percent."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Winter Park",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/orlando-fl/", "Concrete, pavers and turf in Orlando"),
                    ("/winter-garden-fl/", "Concrete, pavers and turf in Winter Garden"),
                    ("/oviedo-fl/", "Concrete, pavers and turf in Oviedo"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Orlando and Orange County permits"),
                    ("/compare/clay-brick-vs-concrete-pavers/", "Clay brick vs. concrete pavers")],
           eyebrow="Concrete · Pavers · Turf in Winter Park, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Winter Park, FL – Permits",
    "meta": "Concrete driveway installers in Winter Park, FL: the city permit, the 2-ft setback, and why stormwater has to stay on the lot, October 2026.",
    "h1": "Pouring a Concrete Driveway in Winter Park",
    "lede": capsule(f"A concrete driveway in Winter Park runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "The city reviews it as a building or miscellaneous permit, not a zoning sign-off, and the application has to show the slab keeping its own stormwater on the property rather than sheeting toward the street."),
    "sections": [
        ("A building permit, filed before the first form goes up",
         f"<p>Winter Park's permitting guide lists “driveway” directly among the hard-surface work that needs a building or miscellaneous permit, and it warns that pouring first and applying later triples the fee "
         f"({src('winterpark-do-i-need-permit', 'City of Winter Park, Do I Need a Permit')}). The driveway worksheet that goes with the application calls for 2-foot minimum side and rear setbacks, confirmation that runoff from the new slab stays on site, and an inspection call placed 24 hours ahead of the pour "
         f"({src('winterpark-driveway-permit', 'City of Winter Park, Driveway Permit Requirements')}). A new curb or sidewalk section where the apron meets the street is reviewed separately by the Engineering Division "
         f"({src('winterpark-row-faq', 'City of Winter Park, Right of Way FAQ')}).</p>"),
        ("The §58-65 ceiling applies to the whole lot, not just the driveway",
         f"<p>Section 58-65 caps impervious coverage, buildings, patios, decks and drives together, at 50 percent of the entire lot, on top of the separate rule that at least half of the front yard specifically stays pervious and landscaped "
         f"({src('winterpark-58-65', 'City of Winter Park, Sec. 58-65 R-1A districts')}). That whole-lot framing is broader than a cap written around the front yard alone, so a wide new driveway on a lot that already carries a pool deck or an expanded patio can run into the ceiling faster than the driveway's own footprint would suggest. We run that math on the survey before quoting a width.</p>"),
    ],
    "scenario": ("A replacement driveway on a 1970s Winter Park lot, worked out in square feet",
                 f"<p>Say a home built in 1976, the city's own median construction year, replaces a cracked 10 by 20 foot driveway, 200 square feet, with a straight repour at the same footprint. At {price('concrete-driveway')} per {per('concrete-driveway')}, that lands between roughly $1,200 and $3,000 before the permit fee or any apron work in the right-of-way is added. "
                 "A wider 24 by 24 foot two-car layout, 576 square feet, scales the same per-square-foot range to roughly $3,456 to $8,640, and on a lot already close to the 50 percent coverage ceiling, that extra width is worth checking against the worksheet before the design is finalized.</p>"),
    "faqs": [
        faq("Does a straight driveway repour in Winter Park still need a permit?",
            "Yes, the city's guide lists driveway work as a permit item regardless of whether the new slab is wider than the old one, and starting the pour first triples the fee once the permit is filed after the fact."),
        faq("What setback does a Winter Park driveway need from the side property line?",
            "The driveway worksheet sets a 2-foot minimum side and rear setback. A separate right-of-way application covers the portion of the apron that meets the curb or sidewalk."),
        faq("Does the whole lot count toward Winter Park's impervious coverage limit, or just the front yard?",
            "Both. Section 58-65 caps the entire lot at 50 percent impervious coverage across buildings, patios, decks and drives together, and layers a second requirement that at least half of the front yard specifically stays pervious."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Winter Park, FL – Brick Match",
    "meta": "Paver driveway installers in Winter Park, FL: the 50% coverage cap, why mulch drives are banned, and matching a brick-street apron, October 2026.",
    "h1": "Paver Driveways for a Winter Park Lot",
    "lede": capsule(f"A paver driveway in Winter Park runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026. "
                     "Pavers count toward the same 50 percent lot-coverage ceiling as poured concrete, and on streets the city still paves in brick, the apron's color and pattern are as much a design question as a permitting one."),
    "sections": [
        ("Pavers are impervious for coverage math, same as concrete",
         f"<p>Winter Park's code draws no distinction between a paver driveway and a poured one under the 50 percent impervious-coverage ceiling in section 58-65: “buildings, accessory structures, patios, decks, drives and other impervious surfaces” are counted together, and front-yard hard surfaces, “concrete, asphalt, brick, pavers” by name, max out at that same 50 percent inside the front yard "
         f"({src('winterpark-58-65', 'City of Winter Park, Sec. 58-65 R-1A districts')}). The one material the ordinance rules out entirely is a mulch drive, which it calls prohibited outright "
         f"({src('winterpark-58-65', 'Sec. 58-65')}). A dimensioned site plan still goes to Building and Permitting Services before pavers go down "
         f"({src('winterpark-driveway-permit', 'City of Winter Park, Driveway Permit Requirements')}).</p>"),
        ("Matching an apron to a brick street, where one still exists",
         f"<p>Not every Winter Park block runs on asphalt. The city still maintains close to 19 of its roughly 100-plus miles of public road in brick, a surface its own streets policy expects to outlast an asphalt resurfacing by a wide margin "
         f"({ext(BRICK_URL, 'City of Winter Park, Street Brick Policy')}). That's separate pavement from a private driveway, but on a lot that fronts one of those segments, a brick-toned paver or a real clay-brick border carries the street's look onto the apron instead of breaking it with plain gray concrete. {cs('winter-park', 'stamped-concrete', 'A stamped, brick-pattern driveway')} is the lower-cost alternative when real pavers don't fit the budget.</p>"),
    ],
    "scenario": ("A two-car paver driveway near a brick street, worked out in square feet",
                 f"<p>Say a home on one of Winter Park's brick-fronted blocks relays a 24 by 24 foot driveway, 576 square feet, in a brick-toned concrete paver to echo the street. At {price('paver-driveway')} per {per('paver-driveway')}, that lands between roughly $6,912 and $17,280 depending on the paver and base thickness, with the homeowner's coverage worksheet rechecked afterward to confirm the lot stays under the 50 percent ceiling once the new paver footprint is added in.</p>"),
    "faqs": [
        faq("Do pavers count differently than concrete toward Winter Park's coverage limit?",
            "No. The city's ordinance groups brick, pavers, concrete and asphalt together under the same 50 percent lot and front-yard caps, so switching materials doesn't buy extra square footage."),
        faq("Can I use mulch or gravel instead of pavers for part of a Winter Park driveway?",
            "Gravel is allowed within the same coverage limits, but mulch drives are explicitly prohibited by the city's own ordinance, not just discouraged."),
        faq("Does a paver driveway in Winter Park need the same right-of-way permit as concrete?",
            "Yes, where the apron crosses into the curb or sidewalk strip, pavers go through the same right-of-way review Engineering applies to a poured concrete apron, separate from the building permit that covers the rest of the driveway."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Winter Park, FL – Coverage & Trees",
    "meta": "Concrete patio contractors in Winter Park, FL: why patios count in the citywide 50% cap, and planning around a landmark live oak, October 2026.",
    "h1": "Building a Concrete Patio in Winter Park",
    "lede": capsule(f"A concrete patio in Winter Park runs {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "Unlike a coverage rule written only around the front yard, Winter Park's ordinance names patios directly inside a single citywide 50 percent impervious cap, so a backyard addition still gets checked against the whole lot's math."),
    "sections": [
        ("Patios are named, not implied, in the coverage ordinance",
         f"<p>Section 58-65 lists “patios” by name alongside buildings, decks and drives as part of the lot's impervious total, capped at 50 percent of the whole parcel "
         f"({src('winterpark-58-65', 'City of Winter Park, Sec. 58-65 R-1A districts')}). That's a different scope than a rule aimed only at the front setback: a backyard patio behind an older Winter Park home still counts against the same citywide ceiling as the driveway out front, so the two additions compete for the same square footage rather than being judged separately. The permit itself still runs through Building and Permitting Services before the forms go up "
         f"({src('winterpark-do-i-need-permit', 'City of Winter Park, Do I Need a Permit')}).</p>"),
        ("A landmark oak changes where the slab can go",
         f"<p>Any application tied to site work has to include a plan showing the proposed patio against the trees already on the lot "
         f"({src('winterpark-tree-ord', 'City of Winter Park Ordinance 3320-24')}). A live oak or bald cypress 30 inches or more in diameter, in fair to excellent condition, earns landmark status under the city's 2024 tree ordinance, a tier above the six-inch threshold that protects an ordinary tree "
         f"({src('winterpark-tree-ord', 'Ordinance 3320-24')}). On a lot with a specimen like that near the back of the house, the patio footprint and the contractor's equipment path both work around the canopy's root zone before a shovel goes in.</p>"),
    ],
    "scenario": ("A backyard patio under a protected canopy, worked out in square feet",
                 f"<p>Say a 1970s-era Winter Park home adds a 16 by 12 foot back patio, 192 square feet, off the kitchen, on a lot shaded by a live oak measuring close to 30 inches across. At {price('concrete-patio')} per {per('concrete-patio')}, that lands between roughly $1,152 and $2,496 before any adjustment for working around the root zone. "
                 "If the oak measures at or above 30 inches once it's checked on site, the landmark designation adds a step to the permit plan, and the patio's shape sometimes shifts a few feet to keep the pour clear of the root flare.</p>"),
    "faqs": [
        faq("Does a backyard patio count toward Winter Park's 50 percent coverage limit?",
            "Yes. Section 58-65 names patios directly as part of the citywide impervious total, capped at half the lot, so a backyard addition is weighed against the same ceiling as the driveway and any other hard surface already on the property."),
        faq("What happens if a live oak is near where I want a new patio?",
            "Any permit tied to site work needs a plan showing the patio relative to the trees on the lot. A live oak 30 inches or more in diameter, in fair to excellent condition, is a landmark tree under the city's 2024 ordinance, which adds protection beyond the standard six-inch threshold."),
        faq("Is a patio permit separate from a driveway permit in Winter Park?",
            "They're the same permit category, a building or miscellaneous permit reviewed by Building and Permitting Services, though each addition is submitted with its own site plan and counted separately in the lot's coverage math."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Winter Park, FL",
    "meta": "Paver patio and walkway installers in Winter Park, FL: the right-of-way rule for planters and walls, and the landmark-tree site plan, October 2026.",
    "h1": "Paver Patios and Walkways Around a Winter Park Home",
    "lede": capsule(f"A paver patio or walkway in Winter Park runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "A front walk that steps into the right-of-way needs its own permit, separate from the patio itself, and the city's rule reaches further than driveways: planters, walls and landscaping in that strip are all covered."),
    "sections": [
        ("The right-of-way rule covers more than pavement",
         f"<p>Winter Park's right-of-way FAQ states plainly that “a city right of way permit is required for work or activities in the right of way including… installation of planters, retaining walls, mailbox… landscaping,” with Public Works at 407-599-3233 and Engineering at 407-450-0815 handling separate pieces of that review "
         f"({src('winterpark-row-faq', 'City of Winter Park, Right of Way FAQ')}). A front paver walkway that crosses from the porch to the sidewalk often touches that strip even when the rest of the patio sits well inside the property line, which is why we flag the walkway's endpoint on the site plan before pricing the job.</p>"),
        ("The same tree site plan applies to a walkway as to a slab",
         f"<p>The 2024 tree ordinance's site-plan requirement names “pool decks, patios, fences, walls, driveways” and, separately, sidewalks among the features a permit application has to map against protected trees "
         f"({src('winterpark-tree-ord', 'City of Winter Park Ordinance 3320-24')}). A paver patio or walkway routed around a mature oak's canopy, rather than straight through its drip line, is a common reason the finished layout curves where a drawing board version would have run straight. {svc('paver-sealing', 'Paver sealing')} later on doesn't reopen that review; only new or relocated pavers do.</p>"),
    ],
    "scenario": ("A front walkway and back patio combination, worked out in square feet",
                 f"<p>Say a Winter Park home relays a 4-foot-wide, 30-foot front walkway, 120 square feet, plus a 200 square foot paver patio off the back porch, 320 square feet combined. At {price('paver-patio')} per {per('paver-patio')}, that lands between roughly $3,840 and $5,120, with the front walkway's last few feet checked against the right-of-way rule since it crosses into the planting strip near the sidewalk.</p>"),
    "faqs": [
        faq("Does a front paver walkway need a right-of-way permit in Winter Park?",
            "If it extends into the strip between the sidewalk and the street, yes, the same permit that covers planters, retaining walls and mailboxes in that area. A walkway that stays entirely on private property doesn't trigger that separate review."),
        faq("Do paver patios need the same tree site plan as a driveway in Winter Park?",
            "Yes. The 2024 tree ordinance's site-plan requirement applies to patios, walkways and driveways alike whenever the permit is tied to site work, so a mature oak's location shapes the layout the same way regardless of which hardscape feature is being added."),
        faq("Can a paver walkway be rerouted around a protected tree instead of removed?",
            "Usually, yes, and it's the preferred option. Curving a walkway or patio edge around a canopy's root zone avoids triggering a tree removal or encroachment review altogether, which is simpler and often cheaper than the alternative."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Winter Park, FL",
    "meta": "Concrete pool deck builders in Winter Park, FL: why decks are named in the 50% coverage cap, and resurfacing an older deck, October 2026.",
    "h1": "Concrete Pool Decks for Winter Park Homes",
    "lede": capsule(f"A concrete pool deck in Winter Park runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} as of October 2026. "
                     "Section 58-65 names decks directly alongside driveways and patios in the city's 50 percent lot-coverage math, and on a home built around the city's 1976 median, the existing deck is often as old as the pool itself."),
    "sections": [
        ("A pool deck counts the same as a driveway in the coverage math",
         f"<p>The ordinance's own list, “buildings, accessory structures, patios, decks, drives and other impervious surfaces,” puts a pool deck in the identical 50 percent citywide bucket as everything else hard on the lot "
         f"({src('winterpark-58-65', 'City of Winter Park, Sec. 58-65 R-1A districts')}). On a property that already carries a full driveway and a side patio, enlarging an existing pool deck is sometimes the addition that pushes the lot closest to that ceiling, which is worth checking on the worksheet before a design gets finalized rather than after.</p>"),
        ("Original decks on 1970s-era Winter Park pools",
         f"<p>With the city's median home dating to 1976 "
         f"({ext(CR_YEAR_URL, 'Census Reporter API, B25035')}), a large share of its in-ground pools are old enough that the original deck has gone through at least one resurfacing already, and some are due for a second. A straight resurface or a decorative overlay still has to clear the same building-permit review as a new deck "
         f"({src('winterpark-do-i-need-permit', 'City of Winter Park, Do I Need a Permit')}), and on a lot already close to the coverage ceiling, a resurfacing over the existing footprint avoids adding new square footage the way a widened deck would.</p>"),
    ],
    "scenario": ("Resurfacing a 1970s-era Winter Park pool deck, worked out in square feet",
                 f"<p>Say a pool built not long after the home's 1976 construction date carries an original 500 square foot broom-finish deck now showing surface cracking. At {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, a resurfacing at the low end of that range lands around $2,500, while a full decorative refinish runs toward $7,500. "
                 "Staying inside the existing 500 square foot footprint means the job doesn't add to the lot's impervious total, which matters more on an older Winter Park lot than on a newer one with more coverage headroom to spare.</p>"),
    "faqs": [
        faq("Does a pool deck count toward Winter Park's impervious coverage cap?",
            "Yes, decks are named directly in section 58-65's list of impervious surfaces, capped at 50 percent of the whole lot along with the driveway, patio and any accessory structures."),
        faq("Is resurfacing an old pool deck cheaper than adding new square footage?",
            "Usually, and it also avoids adding to the lot's coverage total the way widening the deck would. A resurfacing or decorative overlay still goes through the same building-permit review as new construction."),
        faq("How old are most pool decks in Winter Park?",
            "With the city's median home built in 1976, a substantial share of its pools and original decks are now approaching or past 50 years old, old enough that a second resurfacing is common rather than unusual."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Winter Park, FL",
    "meta": "Pool deck paver overlays in Winter Park, FL: working around a landmark live oak, and the 50% coverage ceiling, October 2026.",
    "h1": "Pool Deck Pavers for Winter Park Backyards",
    "lede": capsule(f"As of October 2026, laying pavers around a Winter Park pool, fresh or as an overlay on an older deck, falls in the {price('pool-deck-pavers')} {per('pool-deck-pavers')} market range. "
                     "On the city's older, canopy-shaded lots, a landmark-sized live oak near the cage usually drives the layout more than the price does."),
    "sections": [
        ("An overlay keeps the footprint, and the coverage math, unchanged",
         f"<p>Laying pavers over an existing concrete pool deck, rather than tearing it out, keeps the hard-surface footprint the same, which matters directly under section 58-65's citywide 50 percent impervious cap "
         f"({src('winterpark-58-65', 'City of Winter Park, Sec. 58-65 R-1A districts')}). The overlay still goes through the same building-permit review the city applies to any hard-surface deck "
         f"({src('winterpark-do-i-need-permit', 'City of Winter Park, Do I Need a Permit')}), so skipping the permit because the slab underneath is already there isn't an option the city recognizes.</p>"),
        ("A landmark oak near the pool cage changes the paver layout",
         f"<p>A live oak measuring 30 inches or more in diameter, in fair to excellent condition, is a landmark tree under the city's 2024 ordinance, a step up from the ordinary six-inch protected threshold "
         f"({src('winterpark-tree-ord', 'City of Winter Park Ordinance 3320-24')}). Where one of those sits close enough to a pool cage to shade the deck, which is common on Winter Park's older, mature-canopy lots, the paver pattern and the equipment path for the install both route around its root zone, and the permit's required site plan has to show that relationship before the job is approved.</p>"),
    ],
    "scenario": ("A travertine overlay near a protected oak, worked out in square feet",
                 f"<p>Picture a 450 square foot original cool-deck patio on an older Winter Park lot, with a landmark-sized live oak shading roughly a third of it. Resetting that area in travertine instead of a plain resurfacing, at {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, puts the job somewhere around $5,400 to $13,500 before the site plan accounts for whatever extra care the root zone needs during the install.</p>"),
    "faqs": [
        faq("Can pavers go over an existing Winter Park pool deck without changing the coverage math?",
            "Yes, an overlay on the existing footprint doesn't add new impervious square footage, which helps on a lot already close to the city's 50 percent coverage ceiling, though the overlay still needs its own building permit."),
        faq("Does a shade tree near the pool deck need special handling in Winter Park?",
            "If it measures 30 inches or more in diameter and is a live oak or bald cypress in fair to excellent condition, it's a landmark tree under the 2024 ordinance, and the permit's site plan has to show the deck work relative to its root zone."),
        faq("Is an overlay cheaper than tearing out and replacing a pool deck in Winter Park?",
            "Generally yes, since it skips demolition and disposal costs, though an overlay only makes sense if the slab underneath hasn't settled or cracked badly enough to need a full tear-out first."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Winter Park, FL – Overlays",
    "meta": "Stamped concrete contractors in Winter Park, FL: why an overlay on existing concrete still needs a permit, and the triple-fee rule, October 2026.",
    "h1": "Stamped Concrete for Winter Park Driveways and Patios",
    "lede": capsule(f"A stamped-concrete pattern on a Winter Park driveway or patio falls between {price('stamped-concrete')} {per('stamped-concrete')} this October, the exact figure set by the pattern and the colors chosen. "
                     "Because the work often goes on top of a slab that already exists, homeowners sometimes treat it as routine maintenance; the city's own guide treats it as permit work, triple-fee penalty included, the same as new construction."),
    "sections": [
        ("An overlay on existing concrete is still permit work",
         f"<p>Winter Park's permitting guide doesn't carve out an exception for resurfacing or stamping an existing slab; the same list that covers “driveway… deck (wood, concrete, or other hard surfaces)” applies whether the concrete is new or already there, and the city charges triple the normal fee for work started before the permit is filed "
         f"({src('winterpark-do-i-need-permit', 'City of Winter Park, Do I Need a Permit')}). A stamped pattern laid over a 1970s-era driveway without that step on file is the kind of after-the-fact penalty worth avoiding with one phone call before the crew mobilizes.</p>"),
        ("Pattern and color don't change the coverage math",
         f"<p>Section 58-65 treats a stamped driveway the same as a plain one for coverage purposes: the whole-lot 50 percent cap and the front-yard pervious requirement apply to the footprint, not the finish "
         f"({src('winterpark-58-65', 'City of Winter Park, Sec. 58-65 R-1A districts')}). A brick-pattern stamp near one of the city's own brick streets is a popular way to echo that look at a lower cost than real pavers, without adding any square footage beyond what a plain pour would have used.</p>"),
    ],
    "scenario": ("A brick-pattern stamped driveway overlay, worked out in square feet",
                 f"<p>Picture a 350 square foot original driveway near a brick-street block getting a stamped overlay, running-bond pattern, integral rust color. Figuring {price('stamped-concrete')} per {per('stamped-concrete')} for that square footage puts the job in the neighborhood of $4,200 to $6,650, with the number of colors and the release agent used swinging the final bid up or down, and the permit filed before the crew ever mobilizes.</p>"),
    "faqs": [
        faq("Does resurfacing an old driveway with a stamped overlay need a permit in Winter Park?",
            "Yes, the city's permitting guide covers driveways and hard-surface decks whether the concrete is new or already in place, and it triples the fee for anyone who starts the work before the permit is filed."),
        faq("Does a stamped pattern count differently than plain concrete toward the coverage cap?",
            "No. Section 58-65's 50 percent lot and front-yard limits are based on the footprint, not the finish, so a decorative stamp or integral color doesn't change how much of the lot the driveway or patio is allowed to cover."),
        faq("Can a stamped driveway match Winter Park's brick streets?",
            "A brick-pattern stamp with an integral rust or red-brown color is a common way to echo the look of the city's brick streets for less than the cost of real clay brick or brick-toned pavers."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Winter Park, FL – Permits",
    "meta": "Artificial turf installers in Winter Park, FL: why turf counts in the 50% coverage cap, and the SJRWMD watering schedule it replaces, October 2026.",
    "h1": "Artificial Turf for Winter Park Yards",
    "lede": capsule(f"Artificial turf in Winter Park runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "The city's own driveway-permit worksheet counts turf as impervious coverage rather than landscaping, the opposite of how a homeowner might expect a grass replacement to be scored."),
    "sections": [
        ("Turf is impervious on the city's own worksheet, not a landscaping credit",
         f"<p>The coverage worksheet that accompanies a Winter Park driveway or hardscape permit lists “artificial turf” among the surfaces counted toward the 50 percent impervious cap, the same bucket as a driveway or a deck "
         f"({src('winterpark-driveway-permit', 'City of Winter Park, Driveway Permit Requirements')}). That reaches further than the statewide synthetic-turf rule, which sets a washed base, natural infill and a 10-foot setback from most water bodies without addressing how a city counts turf toward a local coverage limit "
         f"({src('dep-rule', 'DEP Rule 62-308.100')}). A 2025 state law otherwise limits how far a city or an HOA can restrict residential turf "
         f"({src('fs125572', 'F.S. 125.572')}).</p>"),
        ("Turf sidesteps the watering calendar that governs sod",
         f"<p>Orange County, Winter Park included, follows the St. Johns River Water Management District's year-round irrigation schedule, odd-numbered and no-address homes on Wednesday and Saturday, even addresses on Thursday and Sunday "
         f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}). None of that applies once a lawn is turf rather than St. Augustine, since there's no irrigation zone left to schedule, though it doesn't change the fact that turf still counts toward the lot's coverage ceiling the way a sprinkler-fed lawn never did. If an HOA's governing documents don't name turf specifically, state law limits what it can restrict to turf visible from the street or an adjoining lot "
         f"({src('fs720-3045', 'F.S. 720.3045')}).</p>"),
    ],
    "scenario": ("Replacing a struggling lawn with turf near the coverage ceiling, worked out in square feet",
                 f"<p>Say a Winter Park backyard swaps 600 square feet of thinning St. Augustine for artificial turf, on a lot that already carries a driveway, a patio and a pool deck adding up close to the 50 percent impervious mark. At {price('artificial-turf')} per {per('artificial-turf')}, that turf lands between roughly $6,000 and $15,000 depending on pile height and backing, and because the worksheet counts turf as impervious rather than pervious, the homeowner's existing coverage total has to be rechecked before the installation is finalized rather than assumed to have room to spare.</p>"),
    "faqs": [
        faq("Does artificial turf count toward Winter Park's impervious coverage limit?",
            "Yes. The city's own driveway-permit worksheet lists turf among the impervious surfaces counted toward the 50 percent cap, so it doesn't free up coverage the way removing a lawn might seem to."),
        faq("Do SJRWMD watering restrictions apply to artificial turf?",
            "No, the twice-a-week irrigation schedule governs sprinkler-fed sod and landscaping, not a surface with no irrigation zone attached to it, though turf still has to clear the city's own coverage math separately."),
        faq("Can a Winter Park HOA block artificial turf even where the city allows it?",
            "Only within limits. As of 2026, state law restricts an HOA to turf that's actually visible from the frontage or an adjoining property, unless its own governing documents already name turf in more detail."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
