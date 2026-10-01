# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, a, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "dr-phillips"

WIKI_DP_URL = "https://en.wikipedia.org/wiki/Dr._Phillips,_Florida"
CENSUSREPORTER_DP_URL = "http://censusreporter.org/profiles/16000US1217725-doctor-phillips-fl/"
RESTAURANTROW_URL = "https://www.floridaneighborhoodrealty.com/blog/restaurant-row-dr-phillips/"
PHILLIPSLANDING_URL = "https://www.marketconnectrealty.com/dr-phillips/phillips-landing-homes-for-sale/"
OFW_FACTSHEET_URL = "https://floridadep.gov/sites/default/files/ofw-factsheet.pdf"
POINT2HOMES_DP_URL = "https://www.point2homes.com/US/Neighborhood/FL/Doctor-Phillips-Demographics.html"

SRC = [
    "orange-bldg", "orange-do-i-need-permit", "orange-residential-pavers", "orange-row-directory",
    "orange-code-ch21-art6", "orange-lot-grading", "orange-res-plan-guide", "ocfl-tree-permit",
    "sjrwmd-watering", "dep-rule", "fs125572", "fs720-3045",
    "fl-senate-2011-104", "nrcs-candler-osd", "nrcs-tavares-osd", "nrcs-myakka-osd", "nrcs-smyrna-osd",
    ("Wikipedia, Dr. Phillips, Florida", WIKI_DP_URL),
    ("Census Reporter, Doctor Phillips, FL (ACS 2024 5-yr)", CENSUSREPORTER_DP_URL),
    ("Florida Neighborhood Realty, Restaurant Row in Dr. Phillips", RESTAURANTROW_URL),
    ("MarketConnect Realty, Phillips Landing homes", PHILLIPSLANDING_URL),
    ("FDEP, Outstanding Florida Waters fact sheet", OFW_FACTSHEET_URL),
    ("Point2Homes, Doctor Phillips demographics", POINT2HOMES_DP_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Who actually reviews a Dr. Phillips driveway or paver job?",
        f"<p>Dr. Phillips has no town hall of its own; the census line around it marks an unincorporated pocket of Orange County, so a homeowner calls the county's Division of Building Safety rather than a city office "
        f"({src('orange-bldg', 'Orange County Division of Building Safety')}). The county's own answer to whether a driveway needs paperwork doesn't leave room to guess: pour a slab or set a paver anywhere on the lot and a permit follows, with pavers routed to a lighter zoning review instead of the fuller building review a poured surface gets "
        f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}). {post('orange-county-orlando-driveway-patio-permits', 'Our county-by-county permit guide')} walks through how that compares with Orlando a few miles east.</p>"),
    sec("A citrus baron's old grove lines now hold five familiar neighborhoods",
        f"<p>The name comes from Philip Phillips, a Central Florida citrus grower whose holdings by the early 1920s stretched across nine counties; what's now Dr. Phillips sat on the piece of that land running from Conroy Road south to the Sand Lake chain, a footprint that grew into Bay Hill, Orange Tree, Sand Lake Hills, Clubhouse Estates and Turkey Lake Park "
        f"({ext(WIKI_DP_URL, 'Wikipedia, Dr. Phillips, Florida')}). A {svc('concrete-driveways', 'driveway')} going in on a Sand Lake Hills lot platted in the citrus-era boom is usually meeting decades-old fill, while one a few streets over in a 2000s-built section of Clubhouse Estates sits on a more recent subgrade.</p>"),
    sec("Sand Lake Road built a second identity around the groves",
        f"<p>West Sand Lake Road, running between I-4 and Dr. Phillips Boulevard, carries more than two dozen marquee restaurants today under the name Restaurant Row, a strip that traces back to Christini's Ristorante Italiano opening in 1984 on what was then still mostly citrus land "
        f"({ext(RESTAURANTROW_URL, 'Florida Neighborhood Realty, Restaurant Row in Dr. Phillips')}). The corridor sits inside the same unincorporated stretch of the county as the surrounding homes, so a {svc('concrete-patios', 'patio')} or {svc('stamped-concrete', 'stamped driveway')} going in on a residential street behind it answers to the identical county review as anywhere else in Dr. Phillips, not a separate commercial-district process.</p>"),
    sec("Bay Hill's western edge sits on water the state singles out for protection",
        f"<p>Bay Hill and the gated enclave of Phillips Landing back onto Lake Tibet-Butler, the stretch of the Butler Chain that forms Dr. Phillips' western boundary, with waterfront lots there built mostly between 2003 and 2012 "
        f"({ext(PHILLIPSLANDING_URL, 'MarketConnect Realty, Phillips Landing homes')}). The whole chain carries Florida's Outstanding Florida Water designation, the state's tier for a waterbody with exceptional ecological value, which exists to keep new construction from degrading water quality that's already there "
        f"({ext(OFW_FACTSHEET_URL, 'FDEP, Outstanding Florida Waters fact sheet')}). A {svc('paver-patios', 'lakefront patio')} or {svc('pool-deck-pavers', 'pool deck')} going in along that shoreline is built next to water the state already watches closely, a different starting point than a canal a mile inland.</p>"),
    sec("Sandy ridge on one side, flatwoods on the other, and a county on the state's own claims list",
        f"<p>Dr. Phillips sits in the band of west Orange County where excessively drained Candler and Tavares ridge sand gives way to poorly drained Myakka and Smyrna flatwoods soil that can hold a shallow water table for months "
        f"({src('nrcs-candler-osd', 'Candler soil survey')}; {src('nrcs-myakka-osd', 'Myakka soil survey')}). A 2010 Florida Senate interim report, drawing on state insurance data, counts Orange among just eleven counties that together took in more than 88 percent of Florida's sinkhole insurance claims between 2006 and 2009 "
        f"({src('fl-senate-2011-104', 'state sinkhole-claims report')}); that figure doesn't mean every settling slab here is a sinkhole, but it's a reason a {svc('concrete-pool-decks', 'pool deck')} that's dipped at one corner gets a real look at the soil before anyone reaches for that word.</p>"),
    sec("A grown tree canopy means the permit conversation often starts with roots, not forms",
        f"<p>Unincorporated Orange County regulates any tree 8 inches or more in trunk diameter, and removing one on an occupied single-family lot under 2 acres needs its own tree removal permit unless the work is already tied to an approved building permit for the driveway, pad or septic system "
        f"({src('ocfl-tree-permit', 'Orange County, Tree Removal Permit')}). With a good share of Dr. Phillips built out in the 1980s and 1990s, live oaks planted when those subdivisions went in have had three or four decades to put roots under the original concrete, so a {svc('concrete-repair', 'driveway replacement')} here more often starts with a root-and-permit conversation than a bare lot would.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Is Dr. Phillips its own city with its own permit office?",
        f"No. Dr. Phillips is an unincorporated community in Orange County, so a driveway, patio or pool deck goes through the county's Division of Building Safety rather than a town or city hall "
        f"({src('orange-bldg', 'Orange County Division of Building Safety')})."),
    faq("Does a paver driveway need the same permit as poured concrete in Dr. Phillips?",
        "Not quite. The county requires a permit either way, but a poured slab gets the fuller building review while pavers are routed to a lighter zoning permit instead."),
    faq("How far is Dr. Phillips from downtown Orlando?",
        f"About 9 miles, inside the territory the Orlando-unit crew covers alongside {city('orlando', 'Orlando')}, {city('windermere', 'Windermere')} and the rest of west Orange County."),
    faq("Why does Bay Hill's lake frontage matter for a pool deck or patio project?",
        "Bay Hill and Phillips Landing sit on Lake Tibet-Butler, part of the Butler Chain, which carries the state's Outstanding Florida Water designation. Construction near that shoreline is working next to water the state already protects more closely than an ordinary canal."),
    faq("Does Dr. Phillips' population show up in the latest Census count?",
        f"Yes. Census Reporter's current American Community Survey estimate puts Doctor Phillips CDP at about 12,984 residents, up from 12,328 at the 2020 Census "
        f"({ext(CENSUSREPORTER_DP_URL, 'Census Reporter, Doctor Phillips, FL')}; {ext(WIKI_DP_URL, 'Wikipedia, Dr. Phillips, Florida')})."),
]

HUB = page("/dr-phillips-fl/", "city", "Concrete, Pavers & Turf Contractor in Dr. Phillips, FL",
           "Concrete, pavers and turf in Dr. Phillips, FL: unincorporated Orange County permits, the Butler Chain's protected water and Restaurant Row, October 2026.",
           "Concrete, Pavers and Artificial Turf for Dr. Phillips Homes",
           capsule(f"Opera pours concrete and lays pavers and artificial turf for Dr. Phillips, an unincorporated Orange County community of roughly 12,984 residents as of the latest estimate, about 9 miles southwest of downtown Orlando. "
                   f"A new driveway runs {price('concrete-driveway')} per {per('concrete-driveway')} this October 2026, reviewed by the county's Division of Building Safety rather than a city office, since Dr. Phillips sits outside Orlando's municipal line."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Dr. Phillips",
           related=[("/central-florida/", "The Orlando-unit coverage area"),
                    ("/orlando-fl/", "Concrete, pavers and turf in Orlando"),
                    ("/windermere-fl/", "Concrete, pavers and turf in Windermere"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Orlando and Orange County permits"),
                    ("/blog/hoa-approval-for-pavers-and-concrete/", "Getting HOA approval for pavers and concrete"),
                    ("/paver-driveway-cost/", "Paver driveway cost guide")],
           eyebrow="Concrete · Pavers · Turf in Dr. Phillips, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Dr. Phillips, FL – Permits",
    "meta": "Concrete driveway installers in Dr. Phillips, FL: Orange County's lot grading rules, the 6-inch ROW spec and live-oak roots, October 2026.",
    "h1": "Pouring a Concrete Driveway in Dr. Phillips",
    "lede": capsule(f"A concrete driveway in Dr. Phillips runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026, the same Florida market range used across the Orlando unit. "
                     "Because the community sits in unincorporated Orange County, the driveway is reviewed under the county's own lot-grading standard rather than a city building code, and on an established street that often means working around a mature oak canopy as much as around the house itself."),
    "sections": [
        ("The county spells out the apron, not just the permit requirement",
         f"<p>Orange County's Residential Lot Grading Policy sets the apron itself at a minimum 6 inches of 3,000 psi concrete where the driveway crosses the right-of-way, keeps the driveway at least 3 feet off the property line, and caps most lots under 100 feet of frontage at a single driveway "
         f"({src('orange-lot-grading', 'Orange County, Residential Lot Grading Policy 2023')}). Where a lot drains to a roadside ditch instead of a curb, the same policy calls for a culvert built with at least a 15-inch reinforced concrete pipe, mitered at both ends, which is worth confirming before a new driveway layout is finalized on an older Dr. Phillips street that still drains that way.</p>"),
        ("Decades of oak canopy change the order of operations",
         f"<p>Trees 8 inches or more in diameter are regulated countywide, and removing one from an occupied single-family lot under 2 acres needs its own tree removal permit, unless the removal is already covered by an approved building permit for the driveway, pad or septic field "
         f"({src('ocfl-tree-permit', 'Orange County, Tree Removal Permit')}). On streets built out in the 1980s and 1990s, where live oaks planted with the original subdivision have had decades to spread, a {svc('concrete-driveways', 'driveway replacement')} often starts with a look at which roots cross the slab before the pour itself is scheduled.</p>"),
    ],
    "scenario": ("Replacing a cracked original driveway under an oak canopy, worked out in square feet",
                 f"<p>Picture a Clubhouse Estates home built in the late 1980s, its original 16 by 24 foot driveway, 384 square feet, heaved along one edge by a live oak planted the same year the house went up. At {price('concrete-driveway')} per {per('concrete-driveway')}, replacing that slab lands between roughly $2,300 and $5,760, before the cost of a root cut or an arborist's opinion on the tree itself. A frontage under 100 feet keeps the job to a single driveway under the county's own grading policy, so the new layout has to work inside that same footprint rather than adding a second curb cut.</p>"),
    "faqs": [
        faq("Does Orange County require a specific driveway thickness where it meets the street in Dr. Phillips?",
            "Yes. The county's lot grading policy sets the apron at a minimum 6 inches of 3,000 psi concrete across the right-of-way, separate from whatever thickness is used for the rest of the driveway on private property."),
        faq("Can a tree be removed in Dr. Phillips to make room for a new driveway?",
            "Often, yes, without a separate tree removal permit, if the removal is already covered by an approved building permit for that driveway, pad or septic field. A tree removed outside that scope, on an occupied lot under 2 acres, needs its own permit."),
        faq("Is more than one driveway allowed on a Dr. Phillips lot?",
            "Generally not if the lot has under 100 feet of frontage. The county's grading policy caps those lots at a single driveway, which shapes how a widened or second-access layout can be designed."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Dr. Phillips, FL – Zoning Permit",
    "meta": "Paver driveway installers in Dr. Phillips, FL: the county's $38 zoning permit, the 40% open-space rule, and gated Bay Hill lots, October 2026.",
    "h1": "Paver Driveways in Dr. Phillips",
    "lede": capsule(f"A paver driveway in Dr. Phillips runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026. "
                     "Unincorporated Orange County reviews a paver driveway through its own residential paver permit, a lighter zoning process than the building review a poured slab goes through, with a site plan and a set fee rather than an engineering submittal."),
    "sections": [
        ("A $38 permit plus a $38 review fee, not a building application",
         f"<p>The county's residential paver permit asks for a dimensioned site plan showing the paver layout, property lines and easements, charges a $38 permit fee plus a $38 Development Engineering review fee, and turns the review around in about 4 business days "
         f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}). The same zoning code sets residential private open space at a 40 percent minimum for the lot "
         f"({src('orange-residential-pavers')}), which a {svc('paver-driveways', 'paver driveway')} widening has to leave room for alongside the house, pool cage and any existing patio.</p>"),
        ("Gated streets in Bay Hill still answer to the same county desk",
         f"<p>Bay Hill's guard-gated frontage on Lake Tibet-Butler doesn't change which office reviews a paver driveway; the gate controls who drives in, not who signs off on the permit, and the county's Division of Building Safety reviews work there the same way it reviews a non-gated street elsewhere in Dr. Phillips "
         f"({src('orange-bldg', 'Orange County Division of Building Safety')}). Where a driveway section reaches the right-of-way at the street, a separate Right-of-Way Utilization permit from Development Engineering Permitting applies on top of the paver review itself "
         f"({src('orange-row-directory', 'Orange County, ROW Utilization Permit directory')}).</p>"),
    ],
    "scenario": ("Widening a paver driveway inside the open-space limit, worked out in square feet",
                 f"<p>Say a Sand Lake Hills home adds a 6-foot-wide parking apron beside an existing 480 square foot paver driveway, 150 square feet more, bringing the total to 630 square feet. At {price('paver-driveway')} per {per('paver-driveway')}, that addition alone runs roughly $1,800 to $4,500, and because the county's open-space rule holds the lot to a 40 percent minimum of unpaved area, that addition gets checked against the pool deck and existing patio before the layout is final, not assumed to fit.</p>"),
    "faqs": [
        faq("What does Orange County charge for a residential paver permit in Dr. Phillips?",
            "A $38 permit fee plus a $38 Development Engineering review fee, with review typically taking about 4 business days once the site plan is submitted."),
        faq("Does a gated Bay Hill street skip the county's paver permit?",
            "No. The gate controls access to the street; the county's Division of Building Safety still reviews the permit for a paver driveway there the same way it would on a non-gated Dr. Phillips street."),
        faq("What open-space rule applies to a wider paver driveway in Dr. Phillips?",
            "Unincorporated Orange County's zoning code sets residential private open space at a 40 percent minimum for the lot, which a driveway widening has to leave room for alongside the house, pool enclosure and any patio."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Dr. Phillips, FL – Near Sand Lake Rd",
    "meta": "Concrete patio contractors in Dr. Phillips, FL: building behind the Restaurant Row corridor and the county's permit for a patio addition, October 2026.",
    "h1": "Building a Concrete Patio in Dr. Phillips",
    "lede": capsule(f"A concrete patio in Dr. Phillips runs {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "The residential streets a few blocks off Restaurant Row's restaurant strip sit on land that was mostly citrus grove before the 1980s and 1990s, so a patio addition here usually means extending a screened lanai's original slab rather than pouring on undisturbed ground."),
    "sections": [
        ("A patio addition still goes through the county's own permit, not a commercial review",
         f"<p>West Sand Lake Road's Restaurant Row sits inside the same unincorporated stretch of Orange County as the homes behind it, so a residential {svc('concrete-patios', 'patio addition')} there answers to the county's Division of Building Safety like any other Dr. Phillips address, regardless of how close it sits to the restaurant corridor "
         f"({src('orange-bldg', 'Orange County Division of Building Safety')}). The county's general rule is explicit that pouring new concrete anywhere on a residential lot triggers a permit, addition or not "
         f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}).</p>"),
        ("Grove-era lots often start with a smaller original pour",
         f"<p>Much of Dr. Phillips was still citrus grove before Philip Phillips' holdings gave way to Bay Hill, Orange Tree, Sand Lake Hills, Clubhouse Estates and Turkey Lake Park in the decades after "
         f"({ext(WIKI_DP_URL, 'Wikipedia, Dr. Phillips, Florida')}), and homes from that first wave of building typically shipped with a modest screened lanai pad rather than a full outdoor living space. Extending that original slab means matching its control-joint spacing before the new pour ties in, so the seam doesn't become the first place the patio cracks.</p>"),
    ],
    "scenario": ("Extending a 1990s lanai slab, worked out in square feet",
                 f"<p>Take a Sand Lake Hills lanai pad original to the house, 12 by 10 feet, 120 square feet, getting extended by 180 square feet toward the back fence for an outdoor dining area. At {price('concrete-patio')} per {per('concrete-patio')}, that 180 square foot addition runs roughly $1,080 to $2,340, with the existing slab's joint layout checked first so the new pour reads as one surface rather than two mismatched ones.</p>"),
    "faqs": [
        faq("Does a patio near Restaurant Row need a different permit than one elsewhere in Dr. Phillips?",
            "No. The homes behind Sand Lake Road's restaurant strip are reviewed by the same county Division of Building Safety as any other unincorporated Dr. Phillips address; proximity to the commercial corridor doesn't change the process."),
        faq("Why do so many Dr. Phillips patio jobs start as an extension rather than new construction?",
            "A large share of the community's older sections were built in the 1980s and 1990s with a basic screened lanai slab included, so adding on to that original pour is a more common first project than starting from bare ground."),
        faq("Is a permit required for a small patio extension in Dr. Phillips?",
            "Yes. Orange County's own guidance states that pouring new concrete anywhere on a residential lot requires a permit, regardless of the addition's size."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Dr. Phillips, FL",
    "meta": "Paver patio installers in Dr. Phillips, FL: building near the Butler Chain's protected water on Lake Tibet-Butler, October 2026.",
    "h1": "Paver Patios and Walkways Near the Butler Chain",
    "lede": capsule(f"A paver patio in Dr. Phillips runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "Where a lot in Bay Hill or Phillips Landing backs onto Lake Tibet-Butler, the shoreline isn't an ordinary retention pond; it's part of the Butler Chain, a water body the state has flagged for extra protection."),
    "sections": [
        ("An Outstanding Florida Water designation sets the backdrop for lakefront grading",
         f"<p>The Butler Chain, which forms Dr. Phillips' western edge along Bay Hill and Phillips Landing, carries Florida's Outstanding Florida Water designation, a classification the state applies specifically to keep new development from lowering water quality that's already considered exceptional "
         f"({ext(OFW_FACTSHEET_URL, 'FDEP, Outstanding Florida Waters fact sheet')}). A {svc('paver-patios', 'paver patio')} graded toward that shoreline needs its slope planned to carry runoff into the yard's existing drainage path rather than straight at the water, a detail that matters less on a patio a half-mile from any lake.</p>"),
        ("Phillips Landing's build-out years shape what a patio ties into",
         f"<p>Phillips Landing's waterfront homes were built mostly between 2003 and 2012 "
         f"({ext(PHILLIPSLANDING_URL, 'MarketConnect Realty, Phillips Landing homes')}), newer construction than much of the rest of Dr. Phillips, so a paver patio project there is more often tying into a deck or pool cage from that same build era than matching decades of prior settling. The county's standard permit for the work still applies regardless of the home's age "
         f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}).</p>"),
    ],
    "scenario": ("A lakefront paver patio graded away from Lake Tibet-Butler, worked out in square feet",
                 f"<p>Say a Phillips Landing home adds a 340 square foot paver patio between the pool cage and the seawall, with the grade set to shed water toward a side yard swale instead of the lake itself. At {price('paver-patio')} per {per('paver-patio')}, that patio runs roughly $4,080 to $5,440, with the drainage plan reviewed before the base goes in given the shoreline's protected status.</p>"),
    "faqs": [
        faq("Does a lakefront patio in Bay Hill need extra review because of the Butler Chain?",
            "The county's standard permit still applies, but because the Butler Chain carries the state's Outstanding Florida Water designation, the grading plan is worth checking carefully so runoff is directed away from the shoreline rather than into it."),
        faq("Are Phillips Landing homes newer than the rest of Dr. Phillips?",
            "Many of the waterfront lots there were built between 2003 and 2012, which is newer than a lot of the community's earlier 1980s and 1990s sections, so patio work there more often ties into a deck or pool cage from that later build era."),
        faq("Does being near a lake change the paver patio permit itself in Dr. Phillips?",
            "Not the permit category. The same county review applies lakefront or not; what changes is how carefully the grading and drainage plan accounts for the nearby shoreline."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Dr. Phillips, FL",
    "meta": "Concrete pool deck builders in Dr. Phillips, FL: why a dip in an older deck usually isn't a sinkhole, and the soil underneath it, October 2026.",
    "h1": "Concrete Pool Decks for Dr. Phillips Homes",
    "lede": capsule(f"A concrete pool deck in Dr. Phillips runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} as of October 2026. "
                     "Orange County sits on a state list of counties with the heaviest run of sinkhole insurance claims, which makes an honest look at a settling deck worth doing, even though ordinary fill settlement explains most of what actually shows up."),
    "sections": [
        ("A state claims list, read carefully",
         f"<p>A 2010 Florida Senate interim report, citing state Office of Insurance Regulation data, found that just eleven Florida counties accounted for more than 88 percent of sinkhole insurance claims paid between 2006 and 2009, and Orange is on that list "
         f"({src('fl-senate-2011-104', 'state sinkhole-claims report')}). That figure describes insurance claims countywide, not a Dr. Phillips-specific rate, and a dipped corner on an older {svc('concrete-pool-decks', 'pool deck')} is still far more often ordinary settlement over compacted fill than a sinkhole, but it's a fact worth knowing before assuming either explanation without a look at the pattern of the cracking.</p>"),
        ("The ground under the deck shifts character across the community",
         f"<p>West Orange County's soil runs from excessively drained Candler and Tavares sand on the ridge side to poorly drained Myakka and Smyrna flatwoods soil holding a shallow water table for months at a stretch "
         f"({src('nrcs-candler-osd', 'Candler soil survey')}; {src('nrcs-smyrna-osd', 'Smyrna soil survey')}), and Dr. Phillips sits in the transition band between the two. Laying out a deck's compacted base starts from whichever side of that line a given lot falls on, since a pour over the flatwoods soil generally wants a deeper base than the same deck would need over fast-draining sand a few streets away.</p>"),
    ],
    "scenario": ("Replacing a dipped pool deck section, worked out in square feet",
                 f"<p>Picture a 1990s-era pool on a Clubhouse Estates lot where a 200 square foot section of deck near one corner has settled about half an inch below the rest. Repouring that section after confirming it's ordinary fill settlement, not a void underneath, runs roughly $1,000 to $3,000 at the {price('concrete-pool-deck')} per {per('concrete-pool-deck')} range, with a plain broom finish at the lower end and a decorative cool-touch texture pushing it higher.</p>"),
    "faqs": [
        faq("Does Orange County's place on the sinkhole-claims list mean a Dr. Phillips pool deck is at risk?",
            "Not specifically. The county's position on the state's 2006-2009 claims list describes insurance activity across all of Orange County, not a Dr. Phillips rate, and most dipped deck sections trace to ordinary fill settlement rather than a sinkhole."),
        faq("Is the soil the same under every Dr. Phillips pool deck?",
            "No. The community sits where excessively drained ridge sand on one side gives way to wetter flatwoods soil on the other, so the base depth that works for one deck doesn't necessarily carry over to a lot a few streets away."),
        faq("What should be checked before repouring a settled section of pool deck?",
            "Confirming whether the dip traces to compacted fill settling normally or to a void underneath changes the fix. A site visit before the forms go up is what settles that question rather than guessing from the surface crack alone."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Dr. Phillips, FL",
    "meta": "Pool deck pavers in Dr. Phillips, FL: matching a paver choice to the neighborhood's build era, from Sand Lake Hills to Phillips Landing, October 2026.",
    "h1": "Pool Deck Pavers for Dr. Phillips Backyards",
    "lede": capsule(f"Pool deck pavers in Dr. Phillips fall in the {price('pool-deck-pavers')} {per('pool-deck-pavers')} range as of October 2026. "
                     "Which part of the community a pool sits in changes what the deck is actually being matched to: an older grove-era section like Sand Lake Hills, or a newer waterfront build like Phillips Landing."),
    "sections": [
        ("Older sections mean matching a deck to an existing pool cage and lanai",
         f"<p>Dr. Phillips grew out of land Philip Phillips once farmed as citrus groves, and its earlier-built neighborhoods, Bay Hill, Orange Tree, Sand Lake Hills, Clubhouse Estates and Turkey Lake Park among them, came up through the 1980s and 1990s "
         f"({ext(WIKI_DP_URL, 'Wikipedia, Dr. Phillips, Florida')}). A {svc('pool-deck-pavers', 'paver pool deck')} going over an older Kool Deck or broom-finish original in one of those sections has to work around whatever pool cage footers and plumbing penetrations the original build left behind, a different starting point than a deck poured alongside a brand-new pool shell.</p>"),
        ("Newer waterfront construction starts from a cleaner slate",
         f"<p>Phillips Landing's homes, most built between 2003 and 2012 along Lake Tibet-Butler "
         f"({ext(PHILLIPSLANDING_URL, 'MarketConnect Realty, Phillips Landing homes')}), more often pair a paver deck with a pool installed in the same build cycle, so the deck and the pool shell are typically going in together rather than one being added decades after the other. The county's permit process treats either case the same way, whether the deck is new or an overlay on an older one "
         f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}).</p>"),
    ],
    "scenario": ("A paver overlay on an aging Kool Deck surface, worked out in square feet",
                 f"<p>Say a Sand Lake Hills pool from the early 1990s has a worn, chalky Kool Deck surface across 600 square feet that's due for a full replacement rather than another resurfacing pass. Switching to pavers at the {price('pool-deck-pavers')} per {per('pool-deck-pavers')} range runs roughly $7,200 to $18,000, with the pool cage's existing footers surveyed first so the new base doesn't conflict with them.</p>"),
    "faqs": [
        faq("Does an older Dr. Phillips pool deck need extra work before pavers go over it?",
            "Often, yes. A deck original to a 1980s or 1990s pool typically has cage footers and plumbing penetrations that need mapping before the new base and pavers are installed, which a brand-new build doesn't have to account for."),
        faq("Are Phillips Landing pool decks usually new installs?",
            "More often than in older sections, yes, since many of those homes and their pools were built in the same 2003 to 2012 window, so the deck and the pool shell typically go in together rather than one being added much later."),
        faq("Does the county review a paver overlay differently than a brand-new pool deck?",
            "No. The same permit process applies either way, whether the paver deck is new construction or installed over an existing concrete surface."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Dr. Phillips, FL",
    "meta": "Stamped concrete contractors in Dr. Phillips, FL: matching a pattern to a golf-course or lakefront entry, and the county's permit, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Dr. Phillips",
    "lede": capsule(f"Stamped concrete in Dr. Phillips falls in the {price('stamped-concrete')} {per('stamped-concrete')} range as of October 2026, set by the pattern and the number of colors used. "
                     "With no historic district here and no single HOA covering the whole community, the finish a homeowner picks is mostly a question of matching the surrounding streetscape, whether that's a golf-course frontage in Bay Hill or a citrus-era ranch house in Sand Lake Hills."),
    "sections": [
        ("No citywide design board, just the county's standard review",
         f"<p>Dr. Phillips has no historic preservation district and no single architectural review board covering the entire community, so a stamped pattern or integral color doesn't trigger the kind of Certificate of Appropriateness review a designated historic street elsewhere in Orange County would require. The county's Division of Building Safety still reviews the slab itself under its usual permit, regardless of finish "
         f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}).</p>"),
        ("A pattern choice usually tracks the neighborhood it's going into",
         f"<p>A stamped ashlar-slate or cobble pattern in muted earth tones tends to read as a natural fit on a Bay Hill golf-course lot, where the surrounding landscaping and course frontage lean traditional, while a cleaner running-bond pattern suits the more straightforward ranch-style streets of Sand Lake Hills and Clubhouse Estates built in the 1980s and 1990s "
         f"({ext(WIKI_DP_URL, 'Wikipedia, Dr. Phillips, Florida')}). Neither choice changes the {svc('stamped-concrete', 'underlying slab spec')} or the permit category; it's a matter of what looks right on the street, not a code requirement.</p>"),
    ],
    "scenario": ("Upgrading a plain driveway to a stamped pattern, worked out in square feet",
                 f"<p>Picture a Clubhouse Estates driveway, 360 square feet, resurfaced in a stamped running-bond pattern with a single integral color to match the brick accents already on the house. At the {price('stamped-concrete')} per {per('stamped-concrete')} range, that project runs roughly $4,320 to $6,840, with a second color or a more detailed release agent pushing the number toward the top.</p>"),
    "faqs": [
        faq("Does Dr. Phillips have a design review board that controls stamped concrete patterns?",
            "No single board covers the whole community. There's no historic district here, so a stamped pattern or color choice doesn't trigger the kind of design review a designated historic street would require elsewhere in the county."),
        faq("Does a stamped driveway cost more to permit than plain concrete in Dr. Phillips?",
            "No. The county's Division of Building Safety reviews the slab the same way regardless of the finish; a stamped pattern changes the look and the price of the work, not the permit category."),
        faq("What stamped pattern fits a Bay Hill golf-course lot best?",
            "An ashlar-slate or cobble pattern in muted, earth-toned colors tends to suit the traditional landscaping common on Bay Hill's course-fronting streets, though it's a style choice rather than a requirement."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Dr. Phillips, FL – Water Setback",
    "meta": "Artificial turf installers in Dr. Phillips, FL: the state's water-body setback near the Butler and Sand Lake chains, October 2026.",
    "h1": "Artificial Turf for Dr. Phillips Yards",
    "lede": capsule(f"Artificial turf in Dr. Phillips runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "Between the Butler Chain along Bay Hill's western edge and the Sand Lake chain running through the community's center, more Dr. Phillips lots sit within reach of open water than a typical inland Orlando neighborhood, which puts the state's turf setback in play more often here."),
    "sections": [
        ("Two lake chains mean the setback comes up on more than just waterfront lots",
         f"<p>Florida's rule for synthetic turf keeps it at least 10 feet back from a pond, lake or canal, unless a seawall forms that edge, and requires a washed-stone base with natural infill rather than buried irrigation underneath "
         f"({src('dep-rule', 'the DEP turf rule')}). With the Butler Chain forming Dr. Phillips' western boundary near Bay Hill and the Sand Lake chain cutting through its center "
         f"({ext(WIKI_DP_URL, 'Wikipedia, Dr. Phillips, Florida')}), a meaningfully larger share of lots here back onto open water than in a community built around a single retention pond, so that 10-foot line gets checked against the actual shoreline before a {svc('artificial-turf', 'turf')} layout is drawn.</p>"),
        ("An HOA still gets the final say on visible turf, where one exists",
         f"<p>As of 2026, state law limits a homeowners association to restricting artificial turf only where it's actually visible from the street frontage or an adjoining lot "
         f"({src('fs720-3045', 'F.S. 720.3045')}), and a separate 2025 law caps how far local governments can go in regulating residential turf beyond the state's own DEP standard "
         f"({src('fs125572', 'F.S. 125.572')}). Gated communities such as Bay Hill and Phillips Landing run their own architectural review for an exterior change like a new lawn, so that approval runs alongside, not instead of, the state rule and the county's water-body setback.</p>"),
    ],
    "scenario": ("Backyard turf set back from a Sand Lake chain shoreline, worked out in square feet",
                 f"<p>Say a Sand Lake Point home replaces 400 square feet of struggling St. Augustine sod with turf, with the lawn's edge pulled back 10 feet from the water rather than run to the property line. At {price('artificial-turf')} per {per('artificial-turf')}, that comes to roughly $4,000 to $10,000 depending on pile height and backing, with the setback measured from the actual shoreline before the layout is ordered.</p>"),
    "faqs": [
        faq("How close to the water can artificial turf go in Dr. Phillips?",
            "At least 10 feet back from a pond, lake or canal under the state's rule, measured from the water's edge itself rather than from a fence line, unless a seawall forms that edge."),
        faq("Does Dr. Phillips have more lakefront lots than a typical Orlando neighborhood?",
            "Proportionally, yes. Between the Butler Chain along its western edge and the Sand Lake chain running through its center, a larger share of lots here sit within reach of open water than in a community built around a single pond."),
        faq("Can a Bay Hill or Phillips Landing HOA still block artificial turf?",
            "It can review a visible turf installation under its own architectural standards, but as of 2026 state law limits that review to turf actually visible from the street or an adjoining property, on top of the state's own DEP installation rule."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
