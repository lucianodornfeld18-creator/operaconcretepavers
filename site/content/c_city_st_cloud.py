# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, a, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "st-cloud"

TOHO_URL = "https://www.tohowater.com/residents-business/watering-days-and-times"
STCLOUD_MERGER_URL = "https://www.tohowater.com/sites/default/files/2022-10/10.4.22%20St.%20Cloud.pdf"
WIKI_STCLOUD = "https://en.wikipedia.org/wiki/St._Cloud,_Florida"
ACS_STCLOUD_URL = "http://censusreporter.org/profiles/16000US1262625-st-cloud-fl/"

SRC = [
    "stcloud-permit-info", "stcloud-pw-fees",
    "census-pep-v2025",
    ("Census Reporter, St. Cloud, FL (ACS 2020-2024 5-yr, B25035)", ACS_STCLOUD_URL),
    "nrcs-smyrna-osd", "nrcs-myakka-osd", "nrcs-basinger-osd",
    "osceola-parking-ord", "dep-rule", "fs125572", "fs7203045",
    ("Toho Water Authority, Watering Days and Times", TOHO_URL),
    ("Toho Water Authority, St. Cloud Utility Integration News Release", STCLOUD_MERGER_URL),
    ("Wikipedia, St. Cloud, Florida", WIKI_STCLOUD),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("St. Cloud's Building Division waves pavers through, but Public Works still has a say",
        "<p>St. Cloud draws its own line between what needs a building permit and what doesn't: pavers used for a driveway or sidewalk sit on the Building Division's “No Permit Required” list, while a concrete pad, a subdivision or retaining wall, and a pool or spa all stay on the “Permit Required” side "
        f"({src('stcloud-permit-info', 'City of St. Cloud, Permit Information')}). That no-permit line comes printed with a catch: any part of the job that reaches into the right-of-way still needs Public Works and Engineering approval before the pallets get delivered. City Hall is at 1300 9th St., 407-957-7300, and that's also where a {svc('concrete-driveways', 'concrete driveway')} replacement starts once the footprint changes.</p>"),
    sec("Public Works prices the apron by the piece, not as one flat fee",
        "<p>Where St. Cloud does charge for driveway or sidewalk work, it itemizes rather than quoting a single number: a $110 basic fee applies per permit, a curb cut runs $30, a driveway inspection is $100, and a sidewalk inspection is $60 "
        f"({src('stcloud-pw-fees', 'City of St. Cloud, Public Works Fees')}). Replacing a worn apron at the street and reworking the rest of a {svc('paver-driveways', 'paver driveway')} in the same visit can mean paying more than one of those line items at once, so scoping the full job up front usually saves a second trip to Public Works.</p>"),
    sec("St. Cloud's water utility merged with Toho in 2022, and old accounts kept a separate clock",
        "<p>St. Cloud ran its own water utility for most of the city's history, until Toho Water Authority and the city's Environmental Utilities Department combined into one operation on October 1, 2022 "
        f"({ext(STCLOUD_MERGER_URL, 'Toho Water Authority, St. Cloud utility integration')}). Toho's watering-days page still carries a separate schedule for those legacy accounts: a St. Cloud address ending in 0 through 8 waters on a tiered rotation across three day-pairs, in windows as narrow as two and a half hours between midnight and 7:30 a.m., not the simple odd-and-even, Wednesday-and-Saturday pattern Toho uses for the rest of its territory "
        f"({ext(TOHO_URL, 'Toho Water Authority, Watering Days and Times')}). New {svc('artificial-turf', 'artificial turf')} skips the question entirely, since nothing underneath it needs that schedule.</p>"),
    sec("The city grew up on a lake clear enough to see seven feet down",
        "<p>St. Cloud sits on the southern shore of East Lake Tohopekaliga, a lake Wikipedia's sourced entry describes as exceptionally clear, with visibility reaching 7 to 9 feet in open stretches "
        f"({ext(WIKI_STCLOUD, 'Wikipedia, St. Cloud, Florida')}). A yard sloping toward that shoreline, a connected canal or Lakefront Park's own waterline has less room to shed storm water than a lot set back from the water, a detail a crew checks with a level before forming a {svc('concrete-patios', 'patio')} or a {svc('concrete-pool-decks', 'pool deck')} rather than after. {svc('retaining-walls', 'A retaining wall')} on ground like that usually ends up holding back more fill than one on flat inland lots.</p>"),
    sec("Flatwoods soil under St. Cloud holds water close to the surface for part of the year",
        "<p>Two flatwoods series, Smyrna and Myakka, cover most of the ground under Osceola County's yards, and both keep a seasonal high water table less than a foot and a half down for a stretch of most years "
        f"({src('nrcs-smyrna-osd', 'the Smyrna soil record')}; {src('nrcs-myakka-osd', 'federal survey data on Myakka')}). Basinger sits lower still, naturally ponded six to nine months out of a typical year wherever a house pad hasn't raised and compacted it "
        f"({src('nrcs-basinger-osd', 'NRCS Basinger notes')}). That's ground a crew tests with a shovel and a compaction gauge before pricing a {svc('concrete-slabs', 'slab')} or laying the base under {svc('paver-patios', 'a paver patio')}, since the wrong depth on wet ground tends to show up as settling a year or two later rather than right away.</p>"),
    sec("Celebration, a short drive northwest, runs under a different set of rules entirely",
        f"<p>{city('celebration', 'Celebration')}, the planned community a short drive from St. Cloud, isn't a city at all; it sits in unincorporated Osceola County, where exterior work answers to the county's own driveway ordinance and, separately, to Celebration's private architectural review process rather than to the St. Cloud permit counter described above "
        f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance Ch. 22 Art. II')}). Inside St. Cloud itself, no stand-alone driveway-width rule has been published the way the county has one; {post('osceola-county-kissimmee-st-cloud-permits', 'the Osceola County permit guide')} covers both sides of that line in more detail.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does St. Cloud require a permit for a paver driveway?",
        "No, not from the Building Division; pavers for a driveway or sidewalk sit on the city's own no-permit list. Any part of the job that crosses into the right-of-way still needs Public Works and Engineering approval, and that review carries its own fees, a $110 basic charge plus $30 per curb cut."),
    faq("Who do I call about a concrete pad or retaining wall in St. Cloud?",
        "Both stay on the city's permit-required list, filed through the Building Division at City Hall, 1300 9th St., 407-957-7300. Confirming the exact scope before pricing the job is worth the call, since the category also covers a subdivision wall."),
    faq("Did St. Cloud's watering schedule change when Toho Water Authority took over?",
        f"The city's utility and Toho combined into one operation on October 1, 2022, and Toho still runs a separate tiered schedule for the older St. Cloud accounts rather than folding them into its standard odd-and-even pattern. {svc('artificial-turf', 'Artificial turf')} follows neither schedule, since it doesn't need watering once the base is set."),
    faq("How do I find the best concrete contractor near St. Cloud?",
        f"Start with the state's license-lookup tool, then ask directly whether the quote accounts for St. Cloud's own permit list versus Osceola County's rules, since plenty of St. Cloud-area addresses sit close enough to the county line to confuse the two. {post('how-to-choose-a-concrete-contractor-orlando', 'Ten more criteria worth checking')} round out the vetting."),
    faq("What's different about permitting in St. Cloud versus Celebration?",
        "St. Cloud is an incorporated city with its own Building Division and Public Works fee schedule. Celebration is an unincorporated Osceola County community, so a driveway or paver job there goes through the county's Building Office and, separately, Celebration's architectural review, two reviews a St. Cloud homeowner never has to coordinate."),
]

HUB = page("/st-cloud-fl/", "city", "Concrete, Pavers & Turf Contractor in St. Cloud, FL",
           "Concrete, pavers and turf in St. Cloud, FL: the city's no-permit paver list, Public Works' itemized fees, East Lake Tohopekaliga and Osceola soil, October 2026.",
           "Concrete, pavers and artificial turf for St. Cloud, Florida homes",
           capsule("St. Cloud's roughly 74,960 residents live on the southern shore of East Lake Tohopekaliga in Osceola County, and Opera builds their driveways, patios, pool decks and turf. "
                   f"Expect to pay {price('concrete-driveway')} per {per('concrete-driveway')} for a new concrete driveway here, as of October 2026. The city's own Building Division treats pavers differently from a concrete pad or a retaining wall, which still needs a permit."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="St. Cloud",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/osceola-county-kissimmee-st-cloud-permits/", "Osceola County permit basics"),
                    ("/celebration-fl/", "Concrete, pavers and turf in Celebration"),
                    ("/kissimmee-fl/", "Concrete, pavers and turf in Kissimmee"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in St. Cloud, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in St. Cloud, FL – Permits",
    "meta": "Concrete driveway contractors in St. Cloud, FL: Public Works' $110 base fee, $30 curb cuts and the city's no-permit list, as of October 2026.",
    "h1": "Concrete Driveways for St. Cloud Homes",
    "lede": capsule(f"A new or replacement concrete driveway in St. Cloud costs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "The city's Building Division doesn't treat the driveway surface itself as a permit item, but Public Works still charges a $110 basic fee plus $30 for every curb cut where the new apron meets the street."),
    "sections": [
        ("Public Works prices the apron by the piece",
         "<p>St. Cloud splits a driveway job into separate line items rather than one flat permit fee: a $110 basic fee applies per permit, a curb cut is $30, a driveway inspection runs $100, and a sidewalk inspection is $60 "
         f"({src('stcloud-pw-fees', 'City of St. Cloud, Public Works Fees')}). Those charges sit with Public Works, a different office than the Building Division that handles the “Residential Other” and pool-and-spa permits, so a quote that only budgets for one office's fees can come up short once the other one weighs in. City Hall is at 1300 9th St., 407-957-7300, the number to call before ordering concrete for a driveway that touches the right-of-way at all.</p>"),
        ("The Building Division's own list draws a line most homeowners don't expect",
         "<p>St. Cloud's permit page separates “No Permit Required” items from “Permit Required” ones, and a driveway reseal on an existing on-site surface falls on the easy side of that line, with a note that anything reaching into the right-of-way still needs Public Works and Engineering sign-off first "
         f"({src('stcloud-permit-info', 'City of St. Cloud, Permit Information')}). A full tear-out and repour, by contrast, changes the footprint and the apron at the same time, the kind of scope that pulls in both offices rather than one. Confirming which category a specific job falls into before the first yard of concrete is ordered avoids a stop-work call mid-pour.</p>"),
    ],
    "scenario": ("A St. Cloud driveway replacement, worked out with both fees stacked",
                 f"<p>Say a 20 by 22 foot driveway, 440 square feet, gets torn out and repoured along with a new apron at the curb. At {price('concrete-driveway')} per {per('concrete-driveway')}, the slab itself runs roughly $2,640 to $6,600 before Public Works' fees are added. "
                 "The apron work alone adds the $110 basic fee, the $30 curb cut and the $100 driveway inspection, about $240 total, on top of whatever the Building Division charges for the rest of the pour. Repouring only the section back from the street skips that $240, though the two sections of concrete then meet at a new joint instead of one continuous pour.</p>"),
    "faqs": [
        faq("Does St. Cloud charge a flat fee for a driveway permit?",
            "No. Public Works itemizes the charges instead: a $110 basic fee, $30 per curb cut, $100 for a driveway inspection and $60 for a sidewalk inspection. A job touching more than one of those categories pays more than one line item."),
        faq("Is a concrete driveway on the city's no-permit list?",
            "A reseal of an existing on-site surface is. A full replacement that changes the apron at the street is different, since that work reaches into the right-of-way and needs Public Works and Engineering approval before it starts."),
        faq("Which office do I call first for a St. Cloud driveway job?",
            "Public Works and Engineering, reachable through City Hall at 407-957-7300, is the office that reviews anything touching the curb or the right-of-way. The Building Division handles the separate permit list for pads, walls and pools."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in St. Cloud, FL – No-Permit List",
    "meta": "Paver driveway installers in St. Cloud, FL: why pavers sit on the city's no-permit list, but curb work still needs Public Works, October 2026.",
    "h1": "Paver Driveways: What St. Cloud's Permit List Covers",
    "lede": capsule(f"A paver driveway in St. Cloud runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026. "
                     "The city's own permit page names pavers specifically on its “No Permit Required” list, right alongside a note to check with Public Works, the office that still reviews any part of the job reaching into the right-of-way."),
    "sections": [
        ("Pavers get their own line on the no-permit list, with an asterisk",
         "<p>St. Cloud's permit page lists “Pavers (Driveways/Sidewalks – Please see Public Works Department)” under items that don't need a Building Division permit "
         f"({src('stcloud-permit-info', 'City of St. Cloud, Permit Information')}). That's narrower than it first looks: the same page directs homeowners to check with Public Works before work starts, since the no-permit line covers only the Building Division's side of the review, not Public Works' separate right-of-way approval for the part of the driveway that meets the street. A concrete driveway in the same spot goes through that identical Public Works step, even though it isn't named on the same list line.</p>"),
        ("New subdivisions are doing a lot of the paving these days",
         "<p>St. Cloud's population grew from an estimated 59,090 in 2020 to 74,960 by July 2025, a gain of nearly 27 percent "
         f"({src('census-pep-v2025', 'Census Bureau PEP, City and Town Population Totals, Vintage 2025')}). A fair share of that growth shows up as brand-new subdivisions on the city's edges, where a paver driveway often goes in on freshly graded ground rather than over an older, settled lot, which changes the base-compaction question more than the permit question. New construction still faces the same curb-cut review Public Works applies on an older street.</p>"),
    ],
    "scenario": ("A new-construction paver driveway, worked out in square feet",
                 f"<p>Say a new home on a freshly platted St. Cloud lot lays a 24 by 21 foot paver driveway, 504 square feet, with an apron tying into a brand-new curb. Multiply that footage by {price('paver-driveway')} per {per('paver-driveway')} and the driveway alone lands between roughly $6,048 and $10,080, before Public Works' curb-cut and driveway-inspection fees are added. "
                 "Because the subdivision's curb and swale are new rather than retrofit, the apron detail usually matches a standard already on file with Public Works, which can make that part of the review faster than it would be on an older street with a nonstandard curb.</p>"),
    "faqs": [
        faq("Do I need a permit for a paver driveway in St. Cloud?",
            "Not from the Building Division; pavers for a driveway or sidewalk are named on the city's no-permit list. Public Works still reviews the part of the job that reaches the street, worth confirming before material is ordered."),
        faq("Does a paver driveway face a different curb-cut fee than concrete?",
            "No. Public Works' fee schedule applies by the type of work at the curb, not the surface material, so a paver apron and a concrete apron of the same size pay the same curb-cut and inspection charges."),
        faq("Why are so many St. Cloud paver driveways on new construction?",
            "The city's population grew by close to 27 percent between 2020 and mid-2025, and a lot of that growth landed in newer subdivisions, where paver driveways often go in on freshly graded lots rather than over an already-settled one."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in St. Cloud, FL – Permits",
    "meta": "Concrete patio contractors in St. Cloud, FL: the 'Residential Other – Concrete Pad' permit and the city's newer housing stock, October 2026.",
    "h1": "Concrete Patios for St. Cloud Backyards",
    "lede": capsule(f"A concrete patio in St. Cloud is priced at {price('concrete-patio')} per {per('concrete-patio')} as of October 2026, Florida's going range for the work. "
                     "The city's Building Division files a patio slab under “Residential Other – Concrete Pad,” a category that does need a permit, unlike the pavers exemption that covers a driveway or sidewalk."),
    "sections": [
        ("A patio pour sits on the permit-required side of the city's list",
         "<p>St. Cloud's permit page groups a concrete pad, a subdivision or retaining wall, and a pool or spa together as items that do need a Building Division permit, separate from the “No Permit Required” category that covers a paver driveway reseal "
         f"({src('stcloud-permit-info', 'City of St. Cloud, Permit Information')}). A backyard patio addition typically falls under that pad category, since it adds new impervious area rather than resurfacing something already there. Confirming the scope with the Building Division before pricing avoids finding out mid-job that a survey or site plan was expected too.</p>"),
        ("St. Cloud's housing runs newer than several nearby Orlando-unit towns",
         "<p>The median St. Cloud home dates to 2003, per five-year Census estimates "
         f"({ext(ACS_STCLOUD_URL, 'Census Reporter, St. Cloud, FL')}), noticeably newer than the 1992 median seen across several cities closer to Orlando. That younger stock means fewer original 1980s or 1990s patios are due for replacement here; the more common job is an addition, extending an existing lanai or slab outward rather than tearing one out. A stamped or decorative finish on that kind of addition has to tie its control joints into whatever pattern the original pour already used.</p>"),
    ],
    "scenario": ("A patio addition on a newer St. Cloud lot, worked out in square feet",
                 f"<p>Say a home built around the city's 2003 median year adds a 15 by 14 foot patio off the back of the house, 210 square feet, extending an existing lanai pad. That footage, run through {price('concrete-patio')} per {per('concrete-patio')}, comes to about $1,260 to $2,730 before a decorative finish changes the number. "
                 "Because the original slab is closer to two decades old than four, the new pour usually ties into a subgrade that hasn't shifted much, which keeps the transition joint between old and new concrete simpler than it would be on an older lot.</p>"),
    "faqs": [
        faq("Does a concrete patio need a permit in St. Cloud?",
            "Yes. The Building Division files a patio under the “Residential Other – Concrete Pad” category, one of the items on its permit-required list, unlike the paver exemption that covers a driveway or sidewalk resurfacing."),
        faq("Are St. Cloud's original patios old enough to need replacing?",
            "Often not yet. With the city's median home dating to 2003, a lot of the original patio slabs are closer to two decades old than four, so an addition extending the existing pad is more common than a full tear-out and repour."),
        faq("Does extending an existing patio require a new survey?",
            "The Building Division reviews new impervious area the same way it reviews a fresh pad, so a site plan showing the addition relative to the property line is typically part of that review, worth confirming before pricing."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in St. Cloud, FL – Lake Lots",
    "meta": "Paver patio installers in St. Cloud, FL: grading on lakefront and canal lots, and the flatwoods soil under local yards, October 2026.",
    "h1": "Paver Patios and Walkways Around a St. Cloud Home",
    "lede": capsule(f"A paver patio in St. Cloud runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "On the lots closest to East Lake Tohopekaliga or one of the canals feeding it, the base under a new patio has to account for ground that drains more slowly than an inland yard, a grading question rather than a permit one."),
    "sections": [
        ("A lakefront or canal lot drains differently than one set back from the water",
         "<p>A share of St. Cloud's residential lots back onto East Lake Tohopekaliga or a connecting canal, ground that carries less natural fall toward the street than an inland lot has to work with. Before the base for a paver patio goes down on a lot like that, the crew checks where the lot already sheds storm water, since pavers set flat against ground that already drains slowly can pond against the house rather than carrying it away.</p>"),
        ("Low, poorly drained ground sits under a share of the county's lakeside lots",
         "<p>Mapped soil records for the county's low flats and drainage ways show Basinger naturally ponded six to nine months most years on ground nobody has graded and built up yet "
         f"({src('nrcs-basinger-osd', 'a federal survey of Basinger')}). A paver base on ground like that often needs the extra 2 to 4 inches of aggregate wet or weak soil calls for, beyond the standard depth a drier, inland lot would get. Smyrna and Myakka, the two more common flatwoods series across the county, aren't much better, staying damp within roughly 18 inches of grade for part of most years "
         f"({src('nrcs-smyrna-osd', 'the Smyrna federal soil record')}; {src('nrcs-myakka-osd', 'the Myakka series record')}).</p>"),
    ],
    "scenario": ("A canal-adjacent paver patio, worked out in square feet",
                 f"<p>Say a home backing onto a canal that feeds East Lake Tohopekaliga adds 300 square feet of paver patio between the lanai and the yard's edge. At {price('paver-patio')} per {per('paver-patio')}, that footage works out to roughly $3,000 to $4,800, before the base depth is adjusted for wet ground. "
                 "If a shovel test during layout finds standing water within 18 inches of grade, the crew adds the extra aggregate the wetter soil calls for rather than building to the depth a dry, inland yard would get, which raises the base cost before the pavers themselves are set.</p>"),
    "faqs": [
        faq("Does a paver patio near East Lake Tohopekaliga need special grading?",
            "Not a separate permit, but the slope matters more than it would inland. A lot backing onto the lake or a connected canal has less natural fall to shed storm water, so the patio's pitch gets checked against the yard's existing drainage before the base is built."),
        faq("Why does St. Cloud's soil sometimes need a thicker paver base?",
            "Basinger and similar flatwoods soils common in the county can sit ponded or hold water close to the surface for months at a time. Where a shovel test finds that, the base typically needs 2 to 4 extra inches of compacted aggregate beyond what a well-drained lot requires."),
        faq("Do walkways face the same soil check as a full patio?",
            "A narrower walkway disturbs less ground, but the underlying soil question is the same. On a lot already known to hold water close to the surface, the base depth matters more than the finished square footage."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in St. Cloud, FL",
    "meta": "Concrete pool deck builders in St. Cloud, FL: the city's pool-and-spa permit category and new-construction growth, October 2026.",
    "h1": "Concrete Pool Decks for St. Cloud Homes",
    "lede": capsule(f"A concrete pool deck in St. Cloud costs {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, a Florida market range as of October 2026. "
                     "The Building Division reviews a pool deck under its “Swimming Pool and Spa” permit category, and with new subdivisions filling in across the city, a good share of that work is a deck poured around a brand-new pool rather than a resurfacing job."),
    "sections": [
        ("“Swimming Pool and Spa” is its own line on the permit list",
         "<p>St. Cloud's permit-required list keeps pools and spas in a category of their own, separate from the “Residential Other – Concrete Pad” line that covers a patio or walkway "
         f"({src('stcloud-permit-info', 'City of St. Cloud, Permit Information')}). A pool deck poured at the same time as the shell typically goes through that review as part of the larger pool package rather than as a stand-alone slab permit, while a deck replacement on an existing pool without new construction can file separately. Either way, the Building Division at City Hall, 407-957-7300, confirms which path applies.</p>"),
        ("New-construction pools are a bigger share of the work than in an older city",
         "<p>The city's July 2025 population estimate, 74,960, is roughly 15,900 higher than its 2020 base of 59,090 "
         f"({src('census-pep-v2025', 'Census Bureau PEP, City and Town Population Totals, Vintage 2025')}), growth that's landed largely in new subdivisions rather than infill on older streets. A pool deck poured alongside a brand-new pool shell follows a straightforward grading plan tied to the subdivision's own stormwater design, while a deck going in around an older pool has to work with whatever drainage pattern the original construction left behind.</p>"),
    ],
    "scenario": ("A new-construction pool deck, worked out in square feet",
                 f"<p>Say a new home pours a 650 square foot pool deck around a freshly set pool shell, on a lot graded as part of a new subdivision's stormwater plan. Run that footage through {price('concrete-pool-deck')} per {per('concrete-pool-deck')} and the deck lands between about $3,250 for a plain broom finish and $9,750 for a cool-touch decorative surface. "
                 "Because the subdivision's drainage was engineered before the first house went up, the deck's slope usually just follows the lot's existing grading plan rather than requiring a separate drainage study the way a retrofit on an older street sometimes does.</p>"),
    "faqs": [
        faq("What permit covers a new pool deck in St. Cloud?",
            "The Building Division's “Swimming Pool and Spa” category, usually reviewed as part of the larger pool permit when the deck is poured alongside new construction. A deck added later to an existing pool can be a separate filing; confirm which applies with the Building Division."),
        faq("Are most St. Cloud pool decks new construction or replacements?",
            "A larger share than in some nearby cities is new construction, with the city's population up by roughly 15,900 since 2020, much of it in new subdivisions where the pool and deck go in together."),
        faq("Does a new-construction pool deck need its own drainage plan?",
            "Usually not a separate one. New subdivisions typically have their stormwater grading engineered before homes are built, so the deck's slope follows that existing plan rather than needing an independent drainage study."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in St. Cloud, FL",
    "meta": "Pool deck paver installers in St. Cloud, FL: new pools in fresh subdivisions and flatwoods soil under the base, October 2026.",
    "h1": "Pool Deck Pavers in St. Cloud: New Builds and Overlays",
    "lede": capsule(f"Pool deck pavers in St. Cloud run {price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026, whether set fresh around a new pool or relaid over an older deck. "
                     "With the city's median home dating to 2003, most original pool decks around St. Cloud are still within their first two or three decades, which tilts the local mix toward first installs over full overlays."),
    "sections": [
        ("A younger housing stock means fewer decks are due for a full overlay",
         "<p>St. Cloud's median year of home construction is 2003 "
         f"({ext(ACS_STCLOUD_URL, 'Census Reporter, St. Cloud, FL')}), well short of the 30-plus years that tends to push an older coating toward a full paver overlay. Pool deck pavers going in now more often sit on a first-time pool build than on a worn-out original surface, the reverse of the pattern in some of the area's older cities.</p>"),
        ("The base under those pavers still answers to the same flatwoods soil",
         "<p>Dominant across Osceola County, the Smyrna and Myakka soil series keep their water table inside about 18 inches of grade for a few months most years "
         f"({src('nrcs-smyrna-osd', 'NRCS soil survey records')}; {src('nrcs-myakka-osd', 'the Myakka series data')}). A brand-new pool doesn't change that math; the aggregate base under a fresh set of pavers has to account for how close the water sits, the same way it would on an overlay job over an older deck.</p>"),
    ],
    "scenario": ("Pool deck pavers on a new build, worked out in square feet",
                 f"<p>Say a new-construction home sets 580 square feet of pool deck pavers around a freshly installed pool shell. That footage at {price('pool-deck-pavers')} per {per('pool-deck-pavers')} comes to around $8,120 on the concrete-paver end and up near $17,400 if travertine is chosen instead. "
                 "Because the pool and the deck go in together, base compaction happens on freshly graded soil rather than over whatever settling an older slab left behind, the main way this job differs from relaying pavers over a worn deck on an established lot.</p>"),
    "faqs": [
        faq("Are pool deck pavers usually new installs or overlays in St. Cloud?",
            "More often new installs. The city's median home dates to 2003, young enough that most original pool decks haven't reached the point where an overlay is the common fix, unlike in some of the area's older cities."),
        faq("Does new-construction soil need the same base prep as an overlay?",
            "Yes. The flatwoods soils common across the county can hold water close to the surface regardless of whether the lot is brand-new or decades old, so the aggregate base depth depends on the soil test, not the age of construction."),
        faq("Is travertine a common choice for new St. Cloud pool decks?",
            "It's one of several options homeowners weigh against concrete pavers, mainly on cost; travertine runs toward the higher end of the market range. The soil and base work underneath doesn't change based on which surface material sits on top."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete -----------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in St. Cloud, FL",
    "meta": "Stamped concrete contractors in St. Cloud, FL: the 'Subdivision or Retaining Wall' permit line and a 21-mile drive from Orlando, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in St. Cloud",
    "lede": capsule(f"A stamped-concrete project in St. Cloud runs {price('stamped-concrete')} per {per('stamped-concrete')} as of October 2026, shifting with the stamp pattern and how many integral colors go into the mix. "
                     "The city groups “Subdivision or Retaining Wall” work on its permit-required list, the category a decorative entry wall or a stamped border tied into a subdivision monument sign typically falls under."),
    "sections": [
        ("One permit line covers both a retaining wall and subdivision-entry work",
         "<p>St. Cloud's Building Division lists “Subdivision or Retaining Wall” as one item on its permit-required side, grouped with the concrete-pad and pool-and-spa categories rather than broken out separately "
         f"({src('stcloud-permit-info', 'City of St. Cloud, Permit Information')}). A stamped driveway or walk on an individual home lot usually doesn't trigger that particular line unless it ties into a retaining wall or a subdivision's own entry feature, worth confirming with the Building Division before a design with a decorative wall component gets finalized.</p>"),
        ("St. Cloud sits about 21 miles from Opera's Orlando base",
         f"<p>St. Cloud is roughly 21 miles from central Orlando, close enough that a crew already working a job in {city('kissimmee', 'Kissimmee')} or {city('orlando', 'Orlando')} the same week can typically fit in a St. Cloud estimate without a dedicated trip. That distance also means St. Cloud draws on the same material suppliers and release-agent colors available across the rest of the Orlando unit, rather than a separate regional supply chain.</p>"),
    ],
    "scenario": ("A stamped driveway-and-walk combination, worked out in square feet",
                 f"<p>Say a St. Cloud home replaces a plain 300 square foot driveway-and-front-walk combination with a slate-pattern stamped finish and one integral color. At {price('stamped-concrete')} per {per('stamped-concrete')}, that 300 square feet prices out between roughly $3,600 and $4,800, with a second color or a hand-applied release agent pushing it toward the higher end. "
                 "If the design adds a short decorative wall at the walk's edge, that piece is what's worth checking against the city's “Subdivision or Retaining Wall” permit line, even though the stamped slab itself doesn't trigger that review on its own.</p>"),
    "faqs": [
        faq("Does a stamped-concrete driveway need a permit in St. Cloud?",
            "On its own, usually not beyond whatever applies to a standard driveway or patio. Adding a retaining or decorative wall as part of the design is what pulls in the city's “Subdivision or Retaining Wall” permit category."),
        faq("How far is St. Cloud from Opera's Orlando service area?",
            "About 21 miles from central Orlando, close enough that a crew already working in Kissimmee or elsewhere in the Orlando unit the same week can usually fit in a St. Cloud job without a dedicated trip."),
        faq("Do St. Cloud stamped-concrete jobs use different colors than the rest of Central Florida?",
            "No. The market range and the available patterns and release-agent colors are the same across the Orlando unit; St. Cloud isn't on a separate supply chain."),
    ],
    "sources": SRC,
}

# 8. artificial-turf --------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in St. Cloud, FL – Lake Rules",
    "meta": "Artificial turf installers in St. Cloud, FL: the state's 10-foot water-body rule near East Lake Tohopekaliga and the watering exemption, Oct. 2026.",
    "h1": "Artificial Turf for St. Cloud Yards",
    "lede": capsule(f"Installing artificial turf in St. Cloud costs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "Florida's DEP standard holds synthetic grass back at least 10 feet from a water body unless a seawall sits between the yard and the lake or canal, and since nothing under the turf needs irrigation, it never has to answer to Toho Water Authority's watering clock at all."),
    "sections": [
        ("One state rule sets the floor; nobody can write a looser one",
         "<p>Rule 62-308.100, Florida's DEP standard for synthetic turf, took effect in May 2026 and spells out what an installation needs: a washed aggregate base, natural infill rather than crumb rubber, no in-ground irrigation line buried underneath, and that 10-foot gap from any water body unless a seawall stands between the lawn and the water "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). Lawmakers capped local add-ons the same cycle, so neither St. Cloud nor Osceola County can stack a stricter turf rule on top of that state floor "
         f"({src('fs125572', 'Florida Statutes §125.572')}), and {src('fs7203045', 'F.S. §720.3045')} keeps most HOA turf restrictions from reaching a panel nobody can actually see from the street or the next lot over. For a yard touching East Lake Tohopekaliga or a canal, the 10-foot gap is the number to measure first.</p>"),
        ("An installed lawn never has to check St. Cloud's watering calendar",
         "<p>St. Cloud's older utility accounts still run on a tiered Toho Water Authority schedule tied to the last digit of the address, in windows as narrow as two and a half hours "
         f"({ext(TOHO_URL, 'Toho Water Authority, Watering Days and Times')}). Turf has no stake in any of that math, because the ground beneath it never needs a drop once the compacted base goes in. An owner running a rental or a second home from out of state gets to skip tracking which of St. Cloud's nine or ten windows applies to that address.</p>"),
    ],
    "scenario": ("Backyard turf on a lot near a canal, worked out in square feet",
                 f"<p>Say a St. Cloud home near a canal feeding East Lake Tohopekaliga swaps out 550 square feet of struggling lawn for artificial turf, keeping the full layout a safe 10 feet back from the waterline. Multiply that footage by {price('artificial-turf')} per {per('artificial-turf')} and the job lands between roughly $5,500 and $13,750, depending on pile height and infill. "
                 "Staying outside that buffer means the seawall exception never has to be invoked; a layout planned any closer to the canal would need that condition confirmed before the first roll goes down.</p>"),
    "faqs": [
        faq("How close to East Lake Tohopekaliga can artificial turf go?",
            "The state standard draws the line at 10 feet from the water, with an exception for lots where a seawall separates the yard from the lake or canal. The same rule calls for a washed base, natural infill and no in-ground irrigation line under the turf."),
        faq("Does artificial turf follow St. Cloud's watering schedule?",
            "No, neither the citywide Toho pattern nor the older tiered schedule still used for legacy St. Cloud accounts applies to turf. Both govern irrigated grass, and an installed turf system has nothing left to irrigate."),
        faq("Can an HOA in St. Cloud ban artificial turf outright?",
            "Not outright. State law sets a ceiling on how far a local government's own turf rules can reach, and a separate statute keeps most HOA restrictions from applying to a turf panel nobody can see from the frontage or an adjacent lot. A specific community's design guidelines are still worth checking first."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
