# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, a, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "celebration"

WIKI_CELEBRATION = "https://en.wikipedia.org/wiki/Celebration,_Florida"
ACS_CELEBRATION_URL = "http://censusreporter.org/profiles/16000US1211285-celebration-fl/"
CDD_URL = "https://www.celebrationcdd.org/about-the-cdd"
MAXLIFE_URL = "https://maxliferealty.com/blog/celebration-florida-guide"

SRC = [
    "celebration-arc", "osceola-parking-ord", "osceola-row-info", "osceola-permit-info", "osceola-homeowners",
    "nrcs-smyrna-osd", "nrcs-myakka-osd", "nrcs-basinger-osd",
    "dep-rule", "fs125572", "fs7203045",
    ("Census Reporter, Celebration, FL (ACS 2020-2024 5-yr)", ACS_CELEBRATION_URL),
    ("Celebration Community Development District, About the CDD", CDD_URL),
    ("Wikipedia, Celebration, Florida", WIKI_CELEBRATION),
    ("Max Life Realty, Celebration, FL Community Guide", MAXLIFE_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Celebration isn't incorporated, so Osceola County reviews the driveway, not a city hall",
        "<p>Celebration sits entirely inside unincorporated Osceola County, which means a resident's driveway work answers to the county's Building Office rather than to a town permit counter. County Code §22-50.6 caps an ordinary residential driveway at 24 feet wide, and anything beyond that needs a conditional-use approval before construction starts "
        f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance Ch. 22 Art. II')}). The Building Office sits at 1 Courthouse Square, Suite 1400, 407-742-0200, the same office that reviews a {svc('concrete-driveways', 'driveway')} anywhere else in the unincorporated county.</p>"),
    sec("Two different boards review a Celebration project, and they're not the same thing",
        f"<p>Exterior changes in Celebration don't go to a city council; a private Architectural Review Committee handles that review instead, gathering most months on the third Monday at the Town Hall address on Celebration Avenue, under the community's CROA and CNOA governance "
        f"({src('celebration-arc', 'Celebration, Architectural Review Committee calendar')}). A second, entirely separate body, the Celebration Community Development District, was established under Chapter 190 of the Florida Statutes by Osceola County Ordinance 190.005 effective March 29, 1994, and its five-member Board of Supervisors meets at its own District Office, 313 Campus Street "
        f"({ext(CDD_URL, 'Celebration Community Development District, About the CDD')}). The CDD funds and maintains shared infrastructure; it isn't the office that signs off on a homeowner's new {svc('paver-driveways', 'paver driveway')} or {svc('paver-patios', 'patio')}.</p>"),
    sec("Disney platted Celebration around porches facing the street and garages tucked behind",
        f"<p>The Walt Disney Company began developing the roughly 4,900-acre site in 1994, hiring Robert A.M. Stern and Jaquelin Robertson to lay out a New Urbanism town plan "
        f"({ext(WIKI_CELEBRATION, 'Wikipedia, Celebration, Florida')}). Many of the original neighborhoods were built with front porches close to the sidewalk and garages reached from alleys behind the houses rather than a conventional front-loading driveway "
        f"({ext(MAXLIFE_URL, 'Max Life Realty, Celebration, FL Community Guide')}). That layout changes what “driveway” work usually means on an older Celebration block: a short alley apron and a parking pad, with the street-facing yard built for a walkway or a {svc('paver-patios', 'porch landing')} instead.</p>"),
    sec("Lake Rianhard and Lake Evalyn sit on ground that doesn't drain quickly",
        "<p>Downtown Celebration is built around Lake Rianhard, with Lake Evalyn nearby, both sitting on the same low, flat ground common across much of Osceola County's drainage network. Mapped soil records show Basinger, found on a lot of that low ground, standing in water for six to nine months in an average year wherever it hasn't been raised for a house pad "
        f"({src('nrcs-basinger-osd', 'a federal soil survey')}), and the nearby Smyrna and Myakka flatwoods series aren't much drier, holding moisture within roughly 18 inches of grade part of most years "
        f"({src('nrcs-smyrna-osd', 'NRCS county soil data')}; {src('nrcs-myakka-osd', 'the related Myakka listing')}). A {svc('concrete-slabs', 'slab')} or a {svc('concrete-pool-decks', 'pool deck')} going in near either lake gets a base built for that reality rather than for dry ridge sand.</p>"),
    sec("About 13,667 people live in a community built mostly since the mid-1990s",
        f"<p>Census estimates put Celebration's population at 13,667 and its median year of home construction at 2004 "
        f"({ext(ACS_CELEBRATION_URL, 'Census Reporter, Celebration, FL')}), which makes most of the original housing stock three decades old or less. Celebration is about 17 miles from downtown Orlando, close enough for the same crews serving {city('kissimmee', 'Kissimmee')} to reach it without a special trip.</p>"),
    sec("HB 803's permit exemption still comes with county paperwork attached",
        f"<p>Osceola County applies the state's small-job exemption through an “Owner Disclosure of Exempt Work” form sent to the county's building mailbox rather than skipping documentation outright "
        f"({src('osceola-permit-info', 'Osceola County, Permit Information')}). The county's own homeowner guidance doesn't spell out separate rules for a slab, a set of pavers or a retaining wall beyond that "
        f"({src('osceola-homeowners', 'Osceola County, Homeowners')}); {post('osceola-county-kissimmee-st-cloud-permits', 'the Osceola County permit guide')} walks through what that means in practice.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Celebration have its own building department?",
        "No. Celebration is unincorporated, so Osceola County's Building Office reviews driveway, patio, slab and wall work the same way it does for any other unincorporated address. The Architectural Review Committee and the Community Development District are separate from that county review."),
    faq("What's the difference between Celebration's ARC and its CDD?",
        "The Architectural Review Committee is a private association body that reviews the look of exterior changes, meeting monthly at Town Hall. The Community Development District is a public special district created under state law that funds and maintains shared infrastructure; neither one replaces the county's own permit review."),
    faq("Why do some Celebration homes not have a normal front driveway?",
        "A number of the community's original blocks were designed with garages on rear alleys and front porches facing the street, a New Urbanism layout that puts the paved vehicle access behind the house rather than in front of it."),
    faq("How do I find a good concrete contractor for a Celebration home?",
        f"Check the contractor on the state's license-lookup tool, then ask how the bid handles Osceola County's 24-foot driveway cap and whether the design has already cleared, or needs to clear, Celebration's monthly architectural review. {post('how-to-choose-a-concrete-contractor-orlando', 'A ten-point checklist for vetting a concrete contractor')} has the rest of what to ask."),
    faq("Does the Celebration CDD maintain the lakes near downtown?",
        "The CDD funds and maintains shared community infrastructure under its Chapter 190 charter, which commonly includes stormwater and common-area features, but a specific maintenance assignment for Lake Rianhard or Lake Evalyn is worth confirming directly with the district rather than assuming."),
]

HUB = page("/celebration-fl/", "city", "Concrete, Pavers & Turf Contractor in Celebration, FL",
           "Concrete, pavers and turf in Celebration, FL: Osceola County's driveway cap, the ARC versus the CDD, rear-alley garages and Lake Rianhard soil, October 2026.",
           "Concrete, pavers and artificial turf for Celebration, Florida homes",
           capsule("Celebration isn't a city; it's an unincorporated Osceola County community the Walt Disney Company began developing in 1994. "
                   f"Opera builds driveways, patios, pool decks and turf for its roughly 13,667 residents, and a concrete driveway here runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026, a figure the county's own 24-foot width cap doesn't change."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Celebration",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/osceola-county-kissimmee-st-cloud-permits/", "Osceola County permit basics"),
                    ("/kissimmee-fl/", "Concrete, pavers and turf in Kissimmee"),
                    ("/st-cloud-fl/", "Concrete, pavers and turf in St. Cloud"),
                    ("/paver-driveway-cost/", "Paver driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Celebration, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Celebration, FL – Permits",
    "meta": "Concrete driveway contractors in Celebration, FL: Osceola County's 24-foot cap, the conditional-use path, and the HB 803 disclosure form, Oct. 2026.",
    "h1": "Concrete Driveways for Celebration Homes",
    "lede": capsule(f"{price('concrete-driveway')} per {per('concrete-driveway')} is the Florida range for a concrete driveway in Celebration, as of October 2026. "
                     "Because Celebration sits in unincorporated Osceola County, Code §22-50.6 caps an ordinary residential driveway at 24 feet wide, and a wider one needs a conditional-use approval before the county's Building Office signs off."),
    "sections": [
        ("A 24-foot cap applies no matter how coordinated the streetscape looks",
         "<p>Osceola County Code §22-50.6 sets the ceiling at 24 feet for a residential driveway and requires a driveway permit for new construction or widening "
         f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance Ch. 22 Art. II')}). A three-car layout or a boat-trailer apron that would push past that width needs conditional-use approval first, a county review that runs independently of whatever Celebration's own architectural process separately expects for the driveway's appearance.</p>"),
        ("Small driveway jobs still file paperwork, just not a full permit",
         "<p>For work that falls under the state's HB 803 exemption, Osceola County asks for an “Owner Disclosure of Exempt Work” form routed to the county's building mailbox rather than waiving documentation altogether "
         f"({src('osceola-permit-info', 'Osceola County, Permit Information')}). A full driveway replacement that changes the footprint is a different matter and goes through the standard county driveway permit, filed through the Building Office at 1 Courthouse Square, Suite 1400, 407-742-0200.</p>"),
    ],
    "scenario": ("A Celebration driveway at the county's width cap, worked out in square feet",
                 f"<p>Say a 24 by 20 foot driveway, 480 square feet, gets poured right at the county's maximum width. Apply {price('concrete-driveway')} per {per('concrete-driveway')} to that footage and the slab lands between roughly $2,880 and $7,200 before any conditional-use review is needed, since the width itself stays inside the published cap. "
                 "Planning a third bay or a wider boat-trailer apron on the same lot pushes the design past 24 feet, which means pricing in the time a conditional-use approval adds before the first form goes up.</p>"),
    "faqs": [
        faq("How wide can a driveway be in Celebration?",
            "Up to 24 feet without extra review, under Osceola County Code §22-50.6. Going wider needs a conditional-use approval from the county before construction or widening starts."),
        faq("Who issues a driveway permit in Celebration?",
            "Osceola County's Building Office, at 1 Courthouse Square, Suite 1400, 407-742-0200, since Celebration has no city hall of its own to issue one."),
        faq("Does a small driveway repair still need paperwork under the state's new exemption?",
            "Yes. Osceola County still requires an Owner Disclosure of Exempt Work form for jobs that qualify for the state's threshold, rather than skipping documentation entirely."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Celebration, FL – Rear Alleys",
    "meta": "Paver driveway installers in Celebration, FL: rear-alley garage access on older blocks and the county's right-of-way rules, October 2026.",
    "h1": "Paver Driveways and Alley Aprons in Celebration",
    "lede": capsule(f"As of October 2026, a paver driveway in Celebration runs {price('paver-driveway')} per {per('paver-driveway')} on the Florida market. "
                     "On many of the community's original blocks, the paved vehicle access isn't a front driveway at all; it's a short apron off a rear alley, since the New Urbanism layout put garages behind the house rather than facing the street."),
    "sections": [
        ("Rear-alley garages turn a 'driveway' job into a different shape of project",
         f"<p>A number of Celebration's original neighborhoods were designed with front porches close to the sidewalk and garages reached from alleys running behind the row of houses "
         f"({ext(MAXLIFE_URL, 'Max Life Realty, Celebration, FL Community Guide')}). On a block built that way, a {svc('paver-driveways', 'paver driveway')} project is really a short alley apron and parking pad rather than the long front-yard run a conventional subdivision lot would need, and the materials list shrinks accordingly even though the per-square-foot price stays the same.</p>"),
        ("Right-of-way work in unincorporated Osceola County has its own clock",
         "<p>An alley apron counts as right-of-way work the same as a frontage project would, and the county's guidance puts a tight two-day window on getting any disturbed ground back under grade, plus narrow weekday hours for closing a lane "
         f"({src('osceola-row-info', 'county right-of-way guidance')}). Unlike the driveway ordinance, that right-of-way rule carries no published price tag, so pin the number down with the Building Office at 407-742-0200 before counting on a figure.</p>"),
    ],
    "scenario": ("A rear-alley paver apron, worked out in square feet",
                 f"<p>Say a home on an original Celebration block repaves a 10 by 22 foot alley apron and parking pad, 220 square feet, behind the house. That footage at {price('paver-driveway')} per {per('paver-driveway')} comes to roughly $2,640 to $4,400, well under what a full front-yard paver driveway on a conventional subdivision lot of the same width would run. "
                 "Because the work touches the alley's right-of-way, the 48-hour regrading rule still applies even though the job itself is smaller than a typical driveway.</p>"),
    "faqs": [
        faq("Why don't some Celebration homes have a front driveway?",
            "Many of the community's original blocks were built with garages on rear alleys and front porches facing the street, so the paved vehicle access sits behind the house instead of in front of it."),
        faq("Is an alley apron cheaper than a full front driveway?",
            "Usually, simply because it covers less square footage. The market price per square foot is the same either way; the alley layout just means less area to pave."),
        faq("Does alley work in Celebration need a right-of-way permit?",
            "If it disturbs the county right-of-way behind the house, yes, with ground required to be regraded within 48 hours. Confirming the exact fee is a call to the county's Building Office."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Celebration, FL – ARC Review",
    "meta": "Concrete patio contractors in Celebration, FL: why a patio goes to the ARC, not the CDD, and the community's younger housing stock, October 2026.",
    "h1": "Concrete Patios for Celebration Backyards",
    "lede": capsule(f"A concrete patio in Celebration falls in the {price('concrete-patio')} per {per('concrete-patio')} range, the Florida figure as of October 2026. "
                     "The Architectural Review Committee, not the Community Development District, is the body that reviews a new patio's appearance, on top of whatever Osceola County's own permit process requires for the slab itself."),
    "sections": [
        ("A patio addition answers to the ARC's calendar, not the CDD's",
         f"<p>Celebration's Architectural Review Committee takes up exterior changes on a monthly cycle, typically the third Monday of the month "
         f"({src('celebration-arc', 'the committee calendar')}), and a visible backyard addition like a {svc('concrete-patios', 'patio')} is the kind of change that review covers. The Community Development District, a separate public body that funds shared infrastructure under its own Chapter 190 charter, has no role in reviewing an individual patio's design "
         f"({ext(CDD_URL, 'Celebration Community Development District, About the CDD')}).</p>"),
        ("A community built mostly after 2000 means fewer original patios are failing",
         f"<p>Celebration's median home dates to 2004 "
         f"({ext(ACS_CELEBRATION_URL, 'Census Reporter, Celebration, FL')}), younger than most of the surrounding Orlando-unit cities, so an original patio slab is more often sound than cracked. The more common request is an addition extending an existing lanai or porch landing outward, which still needs to clear the ARC's monthly review before the forms go up.</p>"),
    ],
    "scenario": ("A patio addition timed to an ARC meeting, worked out in square feet",
                 f"<p>Say a Celebration home adds 200 square feet of patio off the back porch, submitted ahead of the ARC's monthly deadline so it clears the third-Monday meeting before work starts. Multiply that footage by {price('concrete-patio')} per {per('concrete-patio')} and the addition lands between roughly $1,200 and $2,600, before any decorative finish is added. "
                 "Missing that month's submission deadline pushes the whole project back roughly four weeks to the next meeting, which is worth building into a start date before material gets ordered.</p>"),
    "faqs": [
        faq("Does a concrete patio in Celebration need ARC approval?",
            "Yes, a visible backyard addition is the kind of exterior change the Architectural Review Committee reviews monthly, on top of whatever Osceola County's own slab permit process requires."),
        faq("Does the Celebration CDD review patio designs?",
            "No. The CDD is a public special district that funds and maintains shared infrastructure under state law; it has no role in reviewing an individual homeowner's patio."),
        faq("Are Celebration's original patios old enough to need replacing?",
            "Often not. With the community's median home dating to 2004, most original patio slabs are younger than those in a lot of surrounding cities, so an addition is more common than a full replacement."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Celebration, FL – Lake Ground",
    "meta": "Paver patio installers in Celebration, FL: Lake Rianhard's low ground, Basinger soil, and the ARC's monthly schedule, October 2026.",
    "h1": "Paver Patios Around Celebration's Lakes",
    "lede": capsule(f"Expect {price('paver-patio')} per {per('paver-patio')} for a paver patio in Celebration, the going Florida range as of October 2026. "
                     "Lots closer to Lake Rianhard or Lake Evalyn sit on ground that drains more slowly than the rest of the community, which matters more for base depth than for the ARC review every patio design already has to clear."),
    "sections": [
        ("Low ground near the downtown lakes needs a deeper paver base",
         f"<p>Soil surveys of this part of Osceola County mark Basinger, common across the low flats and drainage ways, as standing in water six to nine months of an average year before it's built up for a house pad "
         f"({src('nrcs-basinger-osd', 'the Basinger federal soil listing')}). A lot close to Lake Rianhard or Lake Evalyn on ground like that typically needs the extra 2 to 4 inches of compacted aggregate ICPI specs call for on wet soil, beyond what a well-drained lot elsewhere in the community would get.</p>"),
        ("The ARC's monthly cycle is the same for a patio as for a driveway",
         f"<p>A paver patio counts as an exterior change under Celebration's architectural review process, convened roughly once a month with its own filing cutoff ahead of each session "
         f"({src('celebration-arc', 'the committee meeting calendar')}). Timing a paver {svc('paver-patios', 'patio')} project around that cycle, rather than assuming a quick turnaround, keeps a finished design from sitting idle for weeks waiting on the next session.</p>"),
    ],
    "scenario": ("A paver patio near Lake Rianhard, worked out in square feet",
                 f"<p>Say a home close to Lake Rianhard lays 240 square feet of paver patio, with a base built for the wetter ground that close to the water. Scale that footage by {price('paver-patio')} per {per('paver-patio')} and the job comes to roughly $2,400 to $3,840, before the deeper base for wet soil adds to the total. "
                 "Submitting the design ahead of the ARC's monthly deadline keeps the extra base depth from being the only delay in the schedule.</p>"),
    "faqs": [
        faq("Does ground near Lake Rianhard need a different paver base?",
            "Often a deeper one. Basinger and similar low-ground soils near Celebration's downtown lakes can sit ponded for months at a time, which typically calls for 2 to 4 extra inches of compacted aggregate beyond a well-drained lot."),
        faq("How far ahead should a Celebration paver patio be planned?",
            "Around the Architectural Review Committee's monthly cycle, which meets on the third Monday with a submission deadline ahead of that date. Missing the cutoff means waiting roughly four weeks for the next review."),
        faq("Is Lake Evalyn treated differently from Lake Rianhard for drainage purposes?",
            "Not that any published source distinguishes; both sit on the same low, slow-draining ground common to this part of the county, so the same base-depth caution applies near either one."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Celebration, FL",
    "meta": "Concrete pool deck builders in Celebration, FL: the ARC's monthly review and a gap in the county's own pool-deck guidance, October 2026.",
    "h1": "Concrete Pool Decks for Celebration Homes",
    "lede": capsule(f"Celebration homeowners pay {price('concrete-pool-deck')} per {per('concrete-pool-deck')} for a concrete pool deck, the Florida market range as of October 2026. "
                     "Osceola County's own homeowner guidance doesn't spell out a separate rule for a pool deck beyond the standard slab process, which makes a direct call to the Building Office worth making before a design is finalized."),
    "sections": [
        ("The county's published guidance leaves pool decks out",
         f"<p>Osceola County's Homeowners page doesn't address a slab, a set of pavers or a retaining wall specifically, pointing residents instead toward the Building Office for the particulars "
         f"({src('osceola-homeowners', 'Osceola County, Homeowners')}). A {svc('concrete-pool-decks', 'pool deck')} poured alongside new construction typically rides along with the pool's own permit, while a deck added to an existing pool later can be its own filing, a distinction worth confirming at 407-742-0200 before pricing.</p>"),
        ("A visible pool deck still needs the ARC's sign-off",
         f"<p>Celebration's architectural board takes up exterior changes on essentially the same monthly rhythm, a published filing window ahead of each session "
         f"({src('celebration-arc', 'the review committee schedule')}). A pool deck visible from a neighboring lot or the street is the kind of addition that review covers, running alongside, not instead of, whatever county slab process the deck itself needs.</p>"),
    ],
    "scenario": ("A new pool deck cleared through both reviews, worked out in square feet",
                 f"<p>Say a Celebration home pours a 520 square foot pool deck around a new pool shell, with the design submitted to the ARC ahead of its monthly meeting. That footage priced at {price('concrete-pool-deck')} per {per('concrete-pool-deck')} comes to between about $2,600 for a plain broom finish and $7,800 for a cool-touch decorative surface. "
                 "Lining up the ARC submission with the pool permit's own timeline keeps the two reviews from stacking delays on top of each other.</p>"),
    "faqs": [
        faq("Does Osceola County publish a specific rule for pool decks?",
            "Not beyond its standard slab process; the county's homeowner guidance is silent on pool decks specifically, so confirming details directly with the Building Office at 407-742-0200 is worth doing before pricing."),
        faq("Does a pool deck need ARC approval in addition to a county permit?",
            "Yes, a visible pool deck is the kind of exterior change Celebration's Architectural Review Committee reviews monthly, a separate step from the county's own slab permit."),
        faq("Can the ARC review and the county permit happen at the same time?",
            "Often, yes, since they're separate processes. Submitting the ARC application early enough to clear a third-Monday meeting keeps it from becoming the slower of the two reviews."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Celebration, FL",
    "meta": "Pool deck paver installers in Celebration, FL: a community built mostly since 2004 and the flatwoods soil under the base, October 2026.",
    "h1": "Pool Deck Pavers in Celebration: New Builds and Overlays",
    "lede": capsule(f"Pool deck pavers in Celebration price out at {price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026. "
                     "With a median home year of 2004, Celebration's original pool decks are younger on average than those in several surrounding cities, so new installs on recent construction outnumber full overlays on worn-out decks."),
    "sections": [
        ("A younger community means fewer decks have reached overlay age",
         f"<p>Census figures put Celebration's median year of home construction at 2004 "
         f"({ext(ACS_CELEBRATION_URL, 'Census Reporter, Celebration, FL')}), and its population at roughly 13,667 residents. A typical original pool deck here is well short of the three decades that tends to push a worn coating toward a full paver overlay, so {svc('pool-deck-pavers', 'pool deck pavers')} more often go down as a first install than as a replacement.</p>"),
        ("The soil under a new set of pavers doesn't care how old the house is",
         f"<p>Across Osceola County, the Smyrna and Myakka flatwoods series keep moisture inside about a foot and a half of grade for a stretch of most years "
         f"({src('nrcs-smyrna-osd', 'soil-series mapping for Smyrna')}; {src('nrcs-myakka-osd', 'soil-series mapping for Myakka')}). A fresh pool build still needs the base checked against that water table before the pavers go down, the same way an older overlay job would.</p>"),
    ],
    "scenario": ("Pool deck pavers on a recent Celebration build, worked out in square feet",
                 f"<p>Say a home built within the last decade sets 460 square feet of pool deck pavers around a newly installed pool shell. Apply {price('pool-deck-pavers')} per {per('pool-deck-pavers')} to that footage and the job totals roughly $6,440 on the concrete-paver end, climbing to about $13,800 if travertine replaces it. "
                 "Because the construction is recent, the base compaction happens on ground that hasn't had decades to settle, which simplifies the prep compared with relaying pavers over an original, much older deck.</p>"),
    "faqs": [
        faq("Are most pool deck paver jobs in Celebration new installs?",
            "More often than not. With a median home year of 2004, a typical original pool deck here hasn't reached the age where a full overlay is the common fix, so first installs on newer construction are more common."),
        faq("Does a newer Celebration home still need a soil check before paving a pool deck?",
            "It does. Smyrna and Myakka don't care when the house was built; both series can sit damp near the surface on a brand-new lot the same as an old one, so a shovel test decides the base depth, not the build date."),
        faq("Is travertine popular for Celebration pool decks?",
            "It's one option homeowners weigh against concrete pavers, mainly on cost, since travertine sits toward the top of the market range. The ARC's review of the finished look applies either way."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete -----------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Celebration, FL",
    "meta": "Stamped concrete contractors in Celebration, FL: the ARC's review of pattern and color, and a 17-mile drive from Orlando, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Celebration",
    "lede": capsule(f"Stamped concrete in Celebration costs {price('stamped-concrete')} per {per('stamped-concrete')}, Florida's range as of October 2026. "
                     "Because Celebration's streetscapes were platted with a coordinated look in mind, a new stamped pattern or integral color on a visible driveway, alley apron or walk is the kind of change the Architectural Review Committee reviews monthly."),
    "sections": [
        ("A coordinated streetscape means color and pattern go through the ARC too",
         f"<p>Celebration's volunteer review board sits monthly, generally the third Monday, with its own paperwork cutoff set ahead of each session "
         f"({src('celebration-arc', 'a published board schedule')}). A slate or ashlar pattern poured into a front walk or an alley apron is precisely the sort of surface change that board exists to weigh in on, apart from whatever driveway or slab paperwork the county itself requires.</p>"),
        ("Celebration is close enough to Orlando for the same crew, the same week",
         f"<p>Celebration sits about 17 miles from downtown Orlando, roughly the same distance as {city('kissimmee', 'Kissimmee')}, which is close enough that a crew working either town can usually fit a Celebration estimate into the same week without a dedicated trip. That proximity also means Celebration draws on the same stamped patterns and release-agent colors used across the rest of the Orlando unit.</p>"),
    ],
    "scenario": ("A stamped alley apron cleared through ARC review, worked out in square feet",
                 f"<p>Say a Celebration home on an original block stamps 180 square feet of alley apron and front-walk combination in a slate pattern with one integral color, submitted ahead of a third-Monday ARC meeting. That footage at {price('stamped-concrete')} per {per('stamped-concrete')} comes to roughly $2,160 to $2,880, with a second color pushing it higher. "
                 "Because the apron sits in the county right-of-way behind the house, the same 48-hour regrading rule that covers other alley work applies here too.</p>"),
    "faqs": [
        faq("Does Celebration's ARC review stamped-concrete colors?",
            "Yes, a new pattern or integral color on a visible driveway, alley apron or walk is the kind of exterior change its Architectural Review Committee reviews monthly, separate from the county's own permit."),
        faq("How far is Celebration from Opera's Orlando service area?",
            "About 17 miles from downtown Orlando, roughly the same distance as Kissimmee, close enough for the same crew to fit a Celebration job into the same week's schedule."),
        faq("Does a stamped alley apron face the same right-of-way rule as a driveway?",
            "If it sits in the county right-of-way behind the house, yes. Disturbed ground there still needs to be regraded within 48 hours, regardless of whether the surface poured is plain or stamped concrete."),
    ],
    "sources": SRC,
}

# 8. artificial-turf --------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Celebration, FL – Lake Buffer",
    "meta": "Artificial turf installers in Celebration, FL: the 10-foot setback near Lake Rianhard and Lake Evalyn, and HOA limits, October 2026.",
    "h1": "Artificial Turf for Celebration Yards",
    "lede": capsule(f"Artificial turf in Celebration runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "On lots near Lake Rianhard or Lake Evalyn, Florida's turf standard keeps synthetic grass at least 10 feet from the water, and the same state law limits how far Celebration's own architectural guidelines can go in restricting turf elsewhere on the lot."),
    "sections": [
        ("The 10-foot buffer matters most on the downtown lake blocks",
         f"<p>Rule 62-308.100 sets Florida's turf standard: a washed base, natural infill, no in-ground irrigation line buried beneath the turf, and at least 10 feet of clearance from a water body unless a seawall separates the yard from it "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A lot backing onto Lake Rianhard or Lake Evalyn has to measure that buffer before the layout is set, while a lot elsewhere in Celebration, away from the lakes, doesn't carry that particular constraint.</p>"),
        ("State law puts a ceiling on how far Celebration's own rules can reach",
         f"<p>A 2025 law caps how aggressively any local government can restrict residential turf beyond the DEP standard "
         f"({src('fs125572', 'Florida Statutes §125.572')}), and a separate statute keeps most HOA turf rules, the kind the CROA or CNOA might otherwise set for Celebration, from reaching a panel that isn't visible from the street or a neighboring lot "
         f"({src('fs7203045', 'F.S. §720.3045')}). The Architectural Review Committee's monthly process still applies to anything that is visible, the same as it would for a stamped driveway or a new patio.</p>"),
    ],
    "scenario": ("Turf near Lake Rianhard, worked out in square feet",
                 f"<p>Say a home near Lake Rianhard replaces 400 square feet of worn lawn with artificial turf, laid out to clear the water by at least 10 feet. That footage at {price('artificial-turf')} per {per('artificial-turf')} totals roughly $4,000 to $10,000, depending on pile height and infill. "
                 "Submitting the visible portion of that layout to the ARC ahead of its monthly meeting keeps the design step from trailing behind the installation schedule.</p>"),
    "faqs": [
        faq("How close to Lake Rianhard can artificial turf go?",
            "No closer than 10 feet under the state's turf standard, unless a seawall sits between the yard and the water. The rule also requires a washed base, natural infill and no buried irrigation line under the turf."),
        faq("Can Celebration's ARC or CROA ban artificial turf entirely?",
            "Not for turf that isn't visible from the street or an adjacent lot; a separate statute limits that. Turf that is visible still goes through the same monthly architectural review as any other exterior change."),
        faq("Does turf near the lake need the same water-table check as a slab?",
            "No. The 10-foot setback and the DEP installation standard are what govern turf near Lake Rianhard or Lake Evalyn; the water-table questions that matter for a concrete or paver base don't apply once turf and its washed base are down."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
