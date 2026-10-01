# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "winter-garden"

HISTORY_URL = "https://www.cwgdn.com/398/History"
WOT_URL = "https://en.wikipedia.org/wiki/West_Orange_Trail"
APOPKA_URL = "https://www.sjrwmd.com/projects/lake-apopka-project/"

SRC = [
    "wintergarden-faq", "wintergarden-isr-worksheet", "wintergarden-r1a", "wintergarden-row-app", "wintergarden-when-permit",
    "census-pep-v2025", "acs-wintergarden", "ocfl-horizonwest",
    "sjrwmd-watering", "fl-senate-2011-104", "orange-res-plan-guide",
    "nrcs-candler-osd", "nrcs-tavares-osd", "nrcs-astatula-osd", "nrcs-myakka-osd", "nrcs-smyrna-osd",
    "dep-rule", "fs125572",
    ("the city history page", HISTORY_URL),
    ("the trail Wikipedia entry", WOT_URL),
    ("St. Johns River Water Management District, Lake Apopka Project", APOPKA_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Winter Garden skips a separate driveway permit but still runs the math on a worksheet",
        f"<p>The city's Building Division, 300 W. Plant St., 407-877-5136, folds a new or wider driveway, patio or pool deck into the same review as any other improvement: its own guidance states that a permit applies to “every public and private building, structure or appurtenances,” and a worksheet under Code §106-2 has to show the lot isn't over its impervious ceiling before the forms go up "
        f"({src('wintergarden-faq', 'city permit FAQ')}; {src('wintergarden-when-permit', 'city permit guidance')}). That worksheet is required any time a homeowner extends or adds a solid surface, and it tallies more than just the driveway.</p>"
        + table("What Winter Garden's impervious-area worksheet counts",
                ["Surface", "Counted against the lot's limit?"],
                [["Driveways", "Yes"], ["Walkways", "Yes"], ["Porches and lanais", "Yes"], ["A/C pads and pool equipment", "Yes"],
                 ["Pool deck", "Yes"], ["Pavers, any pattern", "Yes — the city's own form says “PAVERS ARE IMPERVIOUS”"]],
                f"Source: {src('wintergarden-isr-worksheet', 'impervious worksheet')}, Code §106-2.")),
    sec("A separate application covers the part of the job that reaches the street",
        f"<p>Once a driveway apron, culvert or sidewalk section crosses into the public right-of-way, the paperwork changes: the Right-of-Way Utilization application goes by e-mail to engineering@cwgdn.com, 24 hours' notice is due before a crew sets foot in the road, and the city applies Orange County's own Right-of-Way Utilization Regulations and Road Construction Specifications “as adopted and modified by the City” "
        f"({src('wintergarden-row-app', 'ROW application form')}). {cs('winter-garden', 'concrete-walkways', 'A sidewalk repair')} that stops short of the curb skips that step; one that touches the curb or the swale doesn't. {post('orange-county-orlando-driveway-patio-permits', 'Our Orange County permit guide')} covers how that compares to the unincorporated county next door.</p>"),
    sec("Filing after the crew has already poured costs three times as much",
        f"<p>Winter Garden's own answer to “when is a permit required” doesn't carve out an exception for a job that's already finished: file the paperwork after the fact and the fee triples "
        f"({src('wintergarden-when-permit', 'city permit guidance')}). The city's Municode chapter on the R-1A district, which covers a wide share of its single-family subdivisions, separately caps overall lot coverage at 35 percent, though that figure isn't confirmed to be calculated the same way as the impervious worksheet above "
        f"({src('wintergarden-r1a', 'R-1A code text')}). Checking both numbers before ordering materials is cheaper than checking them after.</p>"),
    sec("Plant Street still runs down the old railroad bed that built the town",
        f"<p>Winter Garden incorporated as a city in 1908, and its downtown grew up around a depot the Atlantic Coast Line built in 1906 at Plant and Main; when fire twice took out the wooden stores and packinghouses along those streets, the rebuilds went up in brick "
        f"({ext(HISTORY_URL, 'the city history page')}). Orange County later paved that same rail corridor into the West Orange Trail, a 22-mile path built on the old Orange Belt Railway alignment that now runs down the median of Plant Street itself, through the middle of the historic blocks it once served "
        f"({ext(WOT_URL, 'the trail Wikipedia entry')}). A front walkway or an apron a few feet from that median gets measured against the trail corridor as much as against the street.</p>"),
    sec("Horizon West is growing fast right next door, under a different set of rules entirely",
        f"<p>Southwest of the city, the Horizon West Special Planning Area covers roughly 20,704 gross acres of mixed-use villages and a town center, and the county's own page is explicit that the area is unincorporated Orange County, “next to Winter Garden and Windermere,” not inside either town's limits "
        f"({src('ocfl-horizonwest', 'county Horizon West page')}). A new-construction lot on the Winter Garden side of that boundary goes through the city's Building Division; the identical house a few streets over, in a Horizon West village, goes through the county instead, which matters for whoever is scheduling the paver or {svc('concrete-pool-decks', 'pool deck')} inspection.</p>"),
    sec("The lake, the sand and the state's one claims list shape what's under the slab",
        f"<p>Winter Garden grew up on the south shore of Lake Apopka, and the water management district is now working with the city on a dredging project aimed at opening up boater access near the shoreline, part of a restoration that had returned visible native vegetation to about 95 percent of the lake's edge as of a 2024 survey "
        f"({ext(APOPKA_URL, 'SJRWMD lake project page')}). Away from the lake, the ground underneath most west Orange County lots splits between excessively drained ridge sand (Candler, Tavares, Astatula) and wetter flatwoods soil (Myakka, Smyrna) that holds a shallow water table for months at a time "
        f"({src('nrcs-candler-osd', 'Candler soil survey')}; {src('nrcs-myakka-osd', 'Myakka soil survey')}). A 2010 Florida Senate report also puts Orange among the eleven counties that accounted for over 88 percent of the state's sinkhole insurance claims from 2006 to 2009, a figure worth knowing before blaming a crack on the ground moving rather than settling "
        f"({src('fl-senate-2011-104', 'state sinkhole-claims report')}). Under the St. Johns district's normal year-round schedule, which governs Orange County outside any shortage order, odd and even addresses still water on separate days under a twice-a-week calendar "
        f"({src('sjrwmd-watering', 'SJRWMD watering page')}).</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Winter Garden require a permit for a driveway, patio or paver job?",
        "The city's own FAQ says a permit applies to every public and private building, structure or appurtenance, and a separate impervious-area worksheet, required under Code §106-2 whenever a solid surface is added or extended, has to show the lot stays under its limit before the Building Division signs off."),
    faq("Why do pavers count as impervious if water drains between the joints?",
        "The city's own worksheet states it directly: “PAVERS ARE IMPERVIOUS.” The definition in Code §106-2 doesn't distinguish a jointed paver surface from a solid slab, so a paver driveway or patio adds to the same impervious total a poured one would."),
    faq("What happens if the work is finished before a Winter Garden permit is pulled?",
        "The permit fee triples. The city's guidance on when a permit is required doesn't carve out an exception for work that's already complete, so filing before the crew starts is the cheaper path either way."),
    faq("How does a driveway apron get approved when it reaches the street in Winter Garden?",
        "A separate Right-of-Way Utilization application, e-mailed to engineering@cwgdn.com with at least 24 hours' notice before work begins, covers that part of the job. The city applies Orange County's own Right-of-Way Utilization Regulations and Road Construction Specifications to the work."),
    faq("Is Horizon West part of the City of Winter Garden?",
        "No. Horizon West is an unincorporated Orange County planning area next to Winter Garden and Windermere, roughly 20,704 gross acres of villages and a town center, reviewed by the county's own building and zoning offices rather than the city's."),
    faq("How do you pick the best concrete contractor near Winter Garden?",
        f"Verify the contractor's status on the state's license-check tool, ask whether the bid already ran the city's impervious-area worksheet or just assumed the lot has room, and confirm whether the quote covers a Right-of-Way application if the work reaches the street. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor')} covers the rest."),
]

HUB = page("/winter-garden-fl/", "city", "Concrete, Pavers & Turf Contractor in Winter Garden, FL",
           "Concrete, pavers and turf in Winter Garden, FL: the city's impervious-area worksheet, its Right-of-Way process and the 35% R-1A cap, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Winter Garden, Florida Homes",
           capsule("Opera pours concrete and sets pavers and artificial turf for homes in Winter Garden, an Orange County city of about 48,063 residents as of mid-2025, roughly 13 miles west of Orlando. "
                   f"Plan on {price('concrete-driveway')} per {per('concrete-driveway')} for a new concrete driveway, the Florida market range for October 2026, and expect the city's own worksheet to count every square foot of it, pavers included, against the lot's impervious limit."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Winter Garden",
           related=[("/central-florida/", "The Orlando-unit coverage area"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Driveway and patio permits in Orlando and Orange County"),
                    ("/orlando-fl/", "Concrete, pavers and turf in Orlando"),
                    ("/clermont-fl/", "Concrete, pavers and turf in Clermont"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Winter Garden, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Winter Garden, FL – Permits",
    "meta": "Concrete driveway installers in Winter Garden, FL: the city's impervious worksheet, the 35% R-1A cap and the Right-of-Way process, Oct. 2026.",
    "h1": "Pouring a Concrete Driveway in Winter Garden",
    "lede": capsule(f"A new or replacement concrete driveway in Winter Garden runs {price('concrete-driveway')} per {per('concrete-driveway')}, the Florida market range tracked this October 2026. "
                     "The city doesn't treat it as a special permit category, but it does run the square footage through an impervious-area worksheet, and in the R-1A district, which covers much of the city's single-family housing, that total feeds into a separate 35-percent lot-coverage cap."),
    "sections": [
        ("One worksheet decides whether the lot has room for a wider driveway",
         f"<p>Winter Garden's Building Division, 300 W. Plant St., 407-877-5136, requires the impervious-area worksheet under Code §106-2 any time a homeowner extends or adds a solid surface, and a driveway is the first line item it checks "
         f"({src('wintergarden-faq', 'city permit FAQ')}; {src('wintergarden-isr-worksheet', 'impervious worksheet')}). The city's own FAQ states that a permit applies to every public and private structure, so a driveway replacement goes through the Building Division rather than being waved through as routine maintenance "
         f"({src('wintergarden-when-permit', 'city permit guidance')}).</p>"),
        ("The R-1A district folds the driveway into a 35-percent coverage number",
         f"<p>Most of Winter Garden's single-family subdivisions sit in the R-1A zoning district, where the Municode chapter caps overall lot coverage at 35 percent; the city's own documentation doesn't confirm that this figure is measured the same way as the impervious worksheet, so both numbers are worth checking against a current survey before a design is final "
         f"({src('wintergarden-r1a', 'R-1A code text')}). Filing the paperwork after the pour, rather than before, triples the permit fee {svc('concrete-driveways', 'on a driveway')} or any other improvement "
         f"({src('wintergarden-when-permit', 'city permit guidance')}).</p>"),
    ],
    "scenario": ("Rebuilding a driveway to fit a second vehicle, worked out in square feet",
                 f"<p>An 18-by-24-foot driveway rebuild, 432 square feet, covers one car with room to park a second alongside it. Multiplying that footage by the {price('concrete-driveway')} per {per('concrete-driveway')} range puts the pour at roughly $2,600 to $6,500, before any demolition of the old slab is added in. "
                 "Running that 432 square feet through the city's worksheet first, against whatever the house, walkway and existing patio already use, is what decides whether the lot still clears its R-1A coverage number once the new driveway is in.</p>"),
    "faqs": [
        faq("Does a concrete driveway need a permit in Winter Garden?",
            "Yes. The city's own guidance says a permit applies to every public and private building, structure or appurtenance, and a driveway replacement or widening goes through the Building Division along with an impervious-area worksheet under Code §106-2."),
        faq("What is Winter Garden's lot-coverage limit for a driveway?",
            "In the R-1A district, which covers much of the city's single-family housing, total lot coverage caps out at 35 percent. The city's records don't confirm whether that figure is calculated the same way as the separate impervious-area worksheet, so both are worth checking."),
        faq("What happens if a Winter Garden driveway is poured before the permit is filed?",
            "The permit fee triples. The city's own answer to when a permit is required doesn't make an exception for work that's already finished, so filing beforehand costs less either way."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Winter Garden, FL – Worksheet",
    "meta": "Paver driveway installers in Winter Garden, FL: the worksheet that calls pavers impervious, and the ridge sand under much of the city, Oct. 2026.",
    "h1": "Paver Driveways in and Around Winter Garden",
    "lede": capsule(f"Figure {price('paver-driveway')} per {per('paver-driveway')} heading into the last quarter of 2026 for a paver driveway in Winter Garden, the going Florida range. "
                     "Pavers don't get a lighter review here: the city's own worksheet treats a jointed surface the same as a poured one, and a good share of the ground under the area's older subdivisions is fast-draining ridge sand rather than the wetter flatwoods soil found in other pockets of the unit."),
    "sections": [
        ("The worksheet is blunt about what a jointed surface counts as",
         f"<p>Winter Garden's impervious-area worksheet spells it out without qualification: “NOTE: PAVERS ARE IMPERVIOUS,” under the definition in Code §106-2 "
         f"({src('wintergarden-isr-worksheet', 'impervious worksheet')}). That line surprises homeowners who assume a paver surface drains and therefore doesn't count toward a lot's limit the way a solid slab would; the worksheet doesn't distinguish between the two, so {svc('paver-driveways', 'a paver driveway')} and a poured one use up the same allowance square foot for square foot.</p>"),
        ("Ridge sand under much of the city drains fast and compacts differently than flatwoods ground",
         f"<p>Candler, Tavares and Astatula soils, all excessively to moderately well drained with a water table well below the surface, are common across much of west Orange County, a contrast with the poorly drained Myakka and Smyrna flatwoods soil that holds water closer to grade elsewhere in the Orlando unit "
         f"({src('nrcs-candler-osd', 'Candler soil survey')}; {src('nrcs-tavares-osd', 'Tavares soil survey')}). On that kind of ground, the compacted aggregate base under a paver driveway is usually managing loose, fast-draining sand rather than a shallow water table, which changes where the crew spends its compaction effort.</p>"),
    ],
    "scenario": ("A paver driveway resized against the worksheet, worked out in square feet",
                 f"<p>A 20-by-24-foot paver driveway comes to 480 square feet, and against the {price('paver-driveway')} per {per('paver-driveway')} range, that prices between roughly $4,800 and $14,400 depending on the paver and base depth chosen. "
                 "Because the worksheet counts every one of those 480 square feet as impervious regardless of the joint pattern, the lot's remaining allowance gets checked against that full number, not against a lower figure some homeowners assume applies to a surface that lets water through at the seams.</p>"),
    "faqs": [
        faq("Do pavers count less than poured concrete on Winter Garden's impervious worksheet?",
            "No. The worksheet states plainly that pavers are impervious, under the Code §106-2 definition, so a paver driveway uses up the same square footage of a lot's impervious allowance as a solid concrete one would."),
        faq("What soil is typically under a paver driveway in Winter Garden?",
            "Much of west Orange County sits on excessively drained Candler, Tavares or Astatula sand, different from the wetter flatwoods soil common elsewhere in the Orlando unit. That sand drains fast but still needs real compaction to hold a stable base under vehicle loads."),
        faq("Does a paver driveway in Winter Garden need the same permit as a poured one?",
            "Yes, the city's review doesn't split driveways by material. Both go through the Building Division and the same impervious-area worksheet before the work is approved."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Winter Garden, FL – Add-Ons",
    "meta": "Concrete patio contractors in Winter Garden, FL: fitting a new patio into the city's impervious worksheet on an already-built lot, Oct. 2026.",
    "h1": "Building a Concrete Patio in Winter Garden",
    "lede": capsule(f"Expect {price('concrete-patio')} per {per('concrete-patio')} for a concrete patio in Winter Garden, the Florida range current for this October. "
                     "Because a patio is almost always added onto a lot where the house, driveway and walkways are already built, the city's worksheet has less room left to work with than it would on a brand-new build, which is the main thing that decides how big the slab can go."),
    "sections": [
        ("Porches and lanais are named on the same worksheet as the patio itself",
         f"<p>Winter Garden's impervious-area worksheet lists porches and lanais as their own line item alongside driveways, walkways and pool decks, and a new concrete patio off the back of the house has to be added to whatever those existing surfaces already total "
         f"({src('wintergarden-isr-worksheet', 'impervious worksheet')}). On a lot built out close to that limit already, {svc('concrete-patios', 'a patio addition')} sometimes has to shrink from the size a homeowner first pictures, which is worth finding out from a worksheet calculation before a design is drawn.</p>"),
        ("A backyard that slopes toward Lake Apopka changes which way the pour sheds water",
         f"<p>Winter Garden grew up along the south shore of Lake Apopka, and the water management district is now working with the city on a project to improve boat access near the shoreline, part of a restoration that has brought native vegetation back to about 95 percent of the lake's edge as of a 2024 survey "
         f"({ext(APOPKA_URL, 'SJRWMD lake project page')}). A lakefront patio's pitch gets set to carry rain away from the house and toward the yard's natural low point rather than straight at the shoreline, a grading question that doesn't come up on a lot a mile or two from the water.</p>"),
    ],
    "scenario": ("A patio addition checked against the existing worksheet total, in square feet",
                 f"<p>A 14-by-18-foot patio off the back door comes to 252 square feet, and at the {price('concrete-patio')} per {per('concrete-patio')} range, that pour lands between roughly $1,500 and $3,275 before a decorative finish changes the number. "
                 "On a lot where the driveway, walkway and an existing lanai already use a chunk of the worksheet's limit, that 252 square feet gets added to the running total first, which sometimes trims the patio's footprint before the forms ever go up.</p>"),
    "faqs": [
        faq("Does adding a concrete patio in Winter Garden require a new impervious calculation?",
            "Yes. The worksheet treats porches, lanais and patios as their own line item, and a new patio has to be added to whatever the driveway, walkway and any existing lanai already total before the city signs off."),
        faq("Does a Winter Garden patio near Lake Apopka need different grading?",
            "A lot that slopes toward the lake gets its patio pitched to carry water toward the yard's own low point instead of straight at the shoreline, a grading check that doesn't apply the same way a mile or two inland."),
        faq("Can a Winter Garden patio be denied for exceeding the impervious limit?",
            "A design that would push the lot's total past its worksheet limit doesn't clear review as drawn. Checking the running total against the worksheet before the forms are ordered avoids a redesign later."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Winter Garden, FL – Permit Order",
    "meta": "Paver patio installers in Winter Garden, FL: why filing the permit after the pavers are down triples the fee, plus the city's 2004 housing stock, Oct. 2026.",
    "h1": "Paver Patios and Walkways for Winter Garden Homes",
    "lede": capsule(f"{price('paver-patio')} per {per('paver-patio')} is the current Florida range this October 2026 for a paver patio in Winter Garden. "
                     "With the city's median home dated to 2004, a lot of paver-patio work here is an extension tied into an existing slab rather than a first install, and filing the city's paperwork before the pavers go down, not after, is what keeps the permit fee at its normal rate."),
    "sections": [
        ("Finishing the job first and filing second is the costliest order to do it in",
         f"<p>Winter Garden's own guidance on permits doesn't soften for a patio that seems like routine backyard work: once the pavers are already down and the paperwork is filed after the fact, the fee triples "
         f"({src('wintergarden-when-permit', 'city permit guidance')}). Calling the Building Division, 407-877-5136, before a crew is scheduled, rather than after the job wraps, is the difference between the normal fee and three times it.</p>"),
        ("A 2004 median build year means a lot of the existing slabs are extension-ready",
         f"<p>Winter Garden's population reached an estimated 48,063 by mid-2025, and the typical home in the city dates to 2004, newer than much of the rest of the Orlando unit's older housing stock "
         f"({src('census-pep-v2025', 'latest Census population count')}; {src('acs-wintergarden', 'Census Reporter local profile')}). A slab that age is usually still sound, which is why {cs('winter-garden', 'paver-patios', 'paver-patio work')} here more often means tying a new edge into that original pour and extending it toward a shaded corner of the yard than tearing out a cracked, decades-old base.</p>"),
    ],
    "scenario": ("A lanai-edge extension, worked out in square feet",
                 f"<p>A 16-by-20-foot paver extension off an existing lanai comes to 320 square feet, and running that against the {price('paver-patio')} per {per('paver-patio')} range prices the job between about $3,200 and $5,440, depending on the paver pattern and base depth. "
                 "Filing for the permit before the first paver goes down, rather than treating the extension as routine backyard work to be squared away later, keeps that job at the ordinary fee instead of the tripled one the city charges after the fact.</p>"),
    "faqs": [
        faq("Does a small paver patio extension in Winter Garden still need a permit filed first?",
            "Yes. The city's guidance applies the same after-the-fact tripled fee to any improvement filed late, regardless of size, so calling the Building Division before scheduling the crew is worth the few extra days it takes."),
        faq("Are most Winter Garden paver patios new installs or extensions?",
            "More often extensions. With a median home built in 2004, a lot of existing concrete patio slabs are still sound enough that paver work means tying new pavers into that original pour rather than tearing it out."),
        faq("Does a paver patio in Winter Garden count differently than a concrete one on the city's worksheet?",
            "No. The impervious-area worksheet counts porches, lanais and patios as a single line item regardless of material, so a paver extension and a poured one add the same square footage to the lot's running total."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Winter Garden, FL",
    "meta": "Concrete pool deck builders in Winter Garden, FL: the city's growth, its 2004 median build year and the 35% R-1A coverage cap, Oct. 2026.",
    "h1": "Concrete Pool Decks for Winter Garden's Newer Homes",
    "lede": capsule(f"A concrete pool deck in Winter Garden falls between {price('concrete-pool-deck')} per {per('concrete-pool-deck')} under current October 2026 Florida pricing. "
                     "The city's population climbed to about 48,063 by mid-2025 on a wave of newer construction, and a deck that size has to clear the R-1A district's 35-percent lot-coverage number alongside the house, driveway and any existing patio."),
    "sections": [
        ("A newer, fast-growing city means more decks going in around a freshly set pool",
         f"<p>Winter Garden's population rose from a 2020 base of 47,399 to roughly 48,063 by July 2025, and the typical home in the city dates to 2004 "
         f"({src('census-pep-v2025', 'latest Census population count')}; {src('acs-wintergarden', 'Census Reporter local profile')}). That pace of building means a share of the pool decks going in around the city get poured the same week the pool shell itself is set, one choice made at the start of the job instead of a later call to fix a surface that has already gone dull or cracked.</p>"),
        ("The deck's square footage has to fit inside the same 35-percent ceiling as everything else",
         f"<p>In the R-1A zoning district, which covers much of Winter Garden's single-family housing, total lot coverage caps out at 35 percent, and a pool deck is one more surface that gets totaled against that figure alongside the house, driveway and walkways "
         f"({src('wintergarden-r1a', 'R-1A code text')}). On a lot where the driveway was already poured wide and a lanai extension is planned too, checking the running total before the deck is sized avoids redesigning it after the pool shell is already set.</p>"),
    ],
    "scenario": ("A new pool deck sized against the lot's remaining allowance, in square feet",
                 f"<p>A newly built pool on a Winter Garden lot calling for a 500-square-foot deck around the shell prices out between roughly $2,500 and $7,500 once the {price('concrete-pool-deck')} per {per('concrete-pool-deck')} range is applied, moving toward the higher end for a cool-touch decorative finish. "
                 "Before the forms go up, that 500 square feet gets checked against whatever the driveway and any patio already use of the R-1A district's 35-percent ceiling, since a deck sized to the pool contractor's shell alone can still push the lot over that number.</p>"),
    "faqs": [
        faq("Are most Winter Garden pool decks new installs or replacements?",
            "More often new installs, since the city's population and housing stock have grown quickly and the median home dates to 2004. A newly poured deck alongside a newly set pool shell is more common here than resurfacing an old one."),
        faq("Does a concrete pool deck in Winter Garden count toward the city's lot-coverage limit?",
            "Yes. In the R-1A district, a pool deck is totaled against the same 35-percent lot-coverage figure as the house, driveway and walkways, so its square footage is checked against whatever those surfaces already use."),
        faq("What's the price range for a concrete pool deck in Winter Garden?",
            f"Figure {price('concrete-pool-deck')} per {per('concrete-pool-deck')} heading into the last part of 2026; a plain broom finish sits toward the bottom of that span, and a cool-touch decorative texture or a replacement job with demolition included pushes it toward the top."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Winter Garden, FL – Horizon West",
    "meta": "Pool deck paver installers near Winter Garden, FL: Horizon West's different permitting office and the worksheet's pool-deck line item, Oct. 2026.",
    "h1": "Travertine and Paver Pool Decks Near Winter Garden",
    "lede": capsule(f"Winter Garden pool decks finished in travertine or pavers price between {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, tracking current Florida contractor rates for this fall. "
                     "A lot just inside the city limits and one a few streets over in the fast-growing, unincorporated Horizon West area can look identical, but they answer to different permitting offices for the same deck."),
    "sections": [
        ("The same new pool deck can mean two different offices depending on the address",
         f"<p>Horizon West, the roughly 20,704-acre planning area southwest of the city, is unincorporated Orange County rather than part of Winter Garden, even though the county's own description places it right “next to Winter Garden and Windermere” "
         f"({src('ocfl-horizonwest', 'county Horizon West page')}). A travertine or paver pool deck going in on the Winter Garden side goes through the city's Building Division; the same deck on a new-construction lot in a Horizon West village is reviewed by the county instead, a distinction worth confirming before a permit application is filed.</p>"),
        ("Winter Garden's own worksheet names the pool deck and the equipment pad beside it separately",
         f"<p>Inside the city, the impervious-area worksheet lists “A/C pads and pool equipment” as one line and “pool deck” as another, so a travertine deck and the small concrete pad for the pool pump and filter both get tallied, not just the larger surface "
         f"({src('wintergarden-isr-worksheet', 'impervious worksheet')}). Leaving the equipment pad off that math is a common way a worksheet total comes in short of what the finished job actually covers.</p>"),
    ],
    "scenario": ("A new paver pool deck plus its equipment pad, worked out in square feet",
                 f"<p>A newly built pool on a 450-square-foot paver deck, plus a 15-square-foot pad for the pump and filter nearby, totals 465 square feet once both line items are added together. Applying the {price('pool-deck-pavers')} per {per('pool-deck-pavers')} range to the 450-square-foot deck alone prices that portion between roughly $5,400 and $13,500, with the equipment pad priced separately as a small slab. "
                 "Whether that lot sits inside Winter Garden or a few streets south in Horizon West changes which office reviews the paperwork, not the arithmetic itself.</p>"),
    "faqs": [
        faq("Does a Horizon West pool deck near Winter Garden use the city's permit process?",
            "No. Horizon West is unincorporated Orange County, not part of Winter Garden, so a pool deck there goes through the county's building and zoning offices rather than the city's Building Division, even though the area borders the city directly."),
        faq("Does the pool equipment pad count separately from the deck on Winter Garden's worksheet?",
            "Yes. The worksheet lists A/C pads and pool equipment as their own line item, distinct from the pool deck itself, so both the larger paver surface and the smaller equipment pad get added to the lot's impervious total."),
        faq("Is travertine or a concrete paver more common on new Winter Garden pool decks?",
            "Both show up on new builds. The choice comes down to budget and how cool the surface needs to stay underfoot, not a city rule, since the permitting and worksheet process treats either material the same way."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Winter Garden, FL – Downtown",
    "meta": "Stamped concrete contractors in Winter Garden, FL: a brick-look pattern that echoes Plant Street, and the Right-of-Way rule for a decorative apron, Oct. 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Winter Garden",
    "lede": capsule(f"Budget {price('stamped-concrete')} per {per('stamped-concrete')} for stamped concrete in Winter Garden, with the final number inside that current Florida range depending on the pattern and color count chosen. "
                     "A running-bond or herringbone brick stamp echoes the rebuilt brick storefronts along the historic downtown, and when the stamped surface reaches the right-of-way, it still has to meet the same engineering spec a plain apron would."),
    "sections": [
        ("A brick pattern has a real local reference point a few blocks from most lots",
         f"<p>Winter Garden's downtown stores were twice rebuilt in brick after fire destroyed the original wooden buildings along Plant and Main Streets, and that commercial core was listed on the National Register of Historic Places in 1996 "
         f"({ext(HISTORY_URL, 'the city history page')}). A stamped running-bond or herringbone brick pattern on a driveway or walkway picks up that same look without the upkeep of actual brick pavers, which is a reasonable starting point for a homeowner choosing a pattern rather than picking blind from a sample board.</p>"),
        ("The Right-of-Way rule doesn't bend for a decorative finish",
         f"<p>Where a stamped apron crosses into the street right-of-way, the same application that covers a plain concrete apron applies, e-mailed to engineering@cwgdn.com with 24 hours' notice before work starts, built to Orange County's own Road Construction Specifications as the city has adopted them "
         f"({src('wintergarden-row-app', 'ROW application form')}). A deep stamp pattern or an integral color doesn't change that engineering standard, only the look of the finished surface.</p>"),
    ],
    "scenario": ("A stamped apron section, worked out in square feet",
                 f"<p>A running-bond brick-pattern stamp across a 300-square-foot driveway apron, with a single integral color, falls between roughly $2,400 and $5,700 once the {price('stamped-concrete')} per {per('stamped-concrete')} range is applied, with a second color or a more detailed release agent pushing it toward the top. "
                 "Because that section reaches the right-of-way, the Right-of-Way Utilization application still has to go in before the pour, the decorative finish doesn't exempt it from that step.</p>"),
    "faqs": [
        faq("Why do some Winter Garden driveways use a brick-pattern stamp?",
            "The city's own downtown core was rebuilt in brick after fire took out the original wooden storefronts, and that look carries into a running-bond or herringbone stamp some homeowners choose for a driveway or walkway, without the maintenance of real brick pavers."),
        faq("Does a stamped driveway apron skip Winter Garden's Right-of-Way process?",
            "No. Any apron that reaches the street right-of-way goes through the same Right-of-Way Utilization application, regardless of whether the surface is plain gray concrete or a stamped, colored finish."),
        faq("Does Winter Garden's impervious worksheet treat stamped concrete differently than plain concrete?",
            "No, the worksheet counts square footage, not finish, so a stamped driveway or patio adds the same number to the lot's impervious total that a plain pour of the same size would."),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Sidewalks & Walkways in Winter Garden, FL",
    "meta": "Concrete walkway contractors in Winter Garden, FL: the city's Right-of-Way application and the West Orange Trail's Plant Street median, Oct. 2026.",
    "h1": "Concrete Sidewalks and Walkways in Winter Garden",
    "lede": capsule(f"A concrete walkway in Winter Garden runs {price('concrete-walkway')} per {per('concrete-walkway')} as of October 2026. "
                     "A front walk built entirely on private property is one project; a walk that crosses into the public right-of-way, including anywhere near the West Orange Trail corridor that runs down the middle of Plant Street, is a different one with its own application."),
    "sections": [
        ("A walkway reaching the right-of-way needs its own application, with notice given first",
         f"<p>Winter Garden's Right-of-Way Utilization application, e-mailed to engineering@cwgdn.com, applies to any sidewalk or walkway section that reaches the street, the swale or the area under a public sidewalk, and the city requires 24 hours' notice before work starts there "
         f"({src('wintergarden-row-app', 'ROW application form')}). {cs('winter-garden', 'concrete-walkways', 'A walkway repair')} that stays entirely on private ground, between the driveway and the front door, doesn't trigger that same application the way a sidewalk section in the right-of-way does.</p>"),
        ("Downtown, that right-of-way runs down the middle of the old rail bed",
         f"<p>Orange County paved the former Orange Belt Railway corridor into the 22-mile West Orange Trail, and through downtown Winter Garden that trail “runs through downtown Winter Garden in the median of Plant Street where the railroad used to run” "
         f"({ext(WOT_URL, 'the trail Wikipedia entry')}). A walkway project a few blocks from that corridor, where the trail itself occupies what used to be the rail line down the center of the street, gets checked against both the city's ordinary sidewalk rules and the trail easement before work starts.</p>"),
    ],
    "scenario": ("A front walkway replacement, worked out in square feet",
                 f"<p>A 4-foot-wide, 50-foot-long front walkway, 200 square feet, runs between roughly $1,400 and $3,400 once the {price('concrete-walkway')} per {per('concrete-walkway')} range is applied to that footage. "
                 "On a lot set back from the street, that full 200 square feet usually sits on private property and skips the Right-of-Way application; on a corner lot where the walk ties into the public sidewalk, part of that same job falls under the city's right-of-way process instead.</p>"),
    "faqs": [
        faq("Does every concrete walkway in Winter Garden need a Right-of-Way application?",
            "Only the part that reaches the public right-of-way, meaning the street, the swale or the area under a public sidewalk. A front walk that stays entirely on private property between the driveway and the door typically doesn't trigger that application."),
        faq("Does the West Orange Trail affect sidewalk work in downtown Winter Garden?",
            "It can, since the trail occupies the old rail corridor in the median of Plant Street. A walkway project near that stretch gets checked against the trail easement in addition to the city's ordinary sidewalk and right-of-way rules."),
        faq("How much notice does Winter Garden require before right-of-way walkway work begins?",
            "At least 24 hours, under the city's Right-of-Way Utilization application, which is submitted by e-mail to the engineering department before a crew starts work in the street or swale."),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Winter Garden, FL – Sheds & Pads",
    "meta": "Concrete slab contractors in Winter Garden, FL: how a shed or parking pad counts toward the 35% R-1A cap, and the sand underneath it, Oct. 2026.",
    "h1": "Concrete Slabs for Sheds, Pads and Parking in Winter Garden",
    "lede": capsule(f"Florida contractor figures published this October put a Winter Garden concrete slab at {price('concrete-slab')} per {per('concrete-slab')}. "
                     "A shed, AC or parking pad is a small addition next to a house and driveway that may already sit close to the R-1A district's 35-percent coverage ceiling, and the sand underneath it varies enough across the city to change how deep the base needs to go."),
    "sections": [
        ("A small pad can be the square footage that tips a lot over its limit",
         f"<p>In the R-1A district, which covers much of Winter Garden's single-family housing, the Municode chapter sets overall lot coverage at 35 percent, and a shed pad, AC pad or parking slab, however small, is one more surface added to that running total alongside the house and driveway "
         f"({src('wintergarden-r1a', 'R-1A code text')}). On an older lot where the driveway was poured wide and a lanai was already added, even a modest utility pad is worth checking against the worksheet before it's poured, not assumed to be too small to matter.</p>"),
        ("Ridge sand and flatwoods ground can sit within a few lots of each other",
         f"<p>West Orange County's soil runs from excessively drained Candler and Tavares ridge sand to poorly drained Myakka and Smyrna flatwoods soil that holds a shallow water table for months at a time, and the two can show up within a short distance of each other depending on where a lot sits relative to Lake Apopka and the surrounding terrain "
         f"({src('nrcs-candler-osd', 'Candler soil survey')}; {src('nrcs-myakka-osd', 'Myakka soil survey')}). A shed or parking pad on the wetter soil typically needs a few more inches of compacted base than the identical pad would on ridge sand.</p>"),
    ],
    "scenario": ("A shed pad checked against the R-1A limit, worked out in square feet",
                 f"<p>A 10-by-12-foot shed pad, 120 square feet, prices between about $480 and $1,200 once the {price('concrete-slab')} per {per('concrete-slab')} range is applied, depending on the mix and reinforcement chosen. "
                 "On a lot where the driveway and an existing patio already use a meaningful share of the R-1A district's 35-percent ceiling, that 120 square feet is worth running through the worksheet before the forms go up, since even a shed-sized pad can be the piece that pushes a tight lot over its limit.</p>"),
    "faqs": [
        faq("Does a shed pad count toward Winter Garden's 35-percent lot-coverage limit?",
            "Yes. Any solid surface, including a small shed, AC or parking pad, is added to the running total that the R-1A district caps at 35 percent of the lot, alongside the house and driveway."),
        faq("Does the soil under a Winter Garden slab change by neighborhood?",
            "It can. West Orange County includes both excessively drained ridge sand and poorly drained flatwoods soil, and which one sits under a particular lot depends partly on its position relative to Lake Apopka and the surrounding terrain."),
        faq("Is a permit needed for a small utility pad in Winter Garden?",
            "The city's general guidance applies a permit requirement to every structure, so confirming with the Building Division before pouring even a small pad avoids assuming an exemption that the city's published rules don't actually spell out."),
    ],
    "sources": SRC,
}

# 10. concrete-repair ----------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair & Resurfacing in Winter Garden, FL",
    "meta": "Concrete repair contractors in Winter Garden, FL: why cracking in a 2004-era city often isn't a sinkhole, even with Orange on the claims list, Oct. 2026.",
    "h1": "Concrete Repair and Resurfacing in Winter Garden",
    "lede": capsule(f"Late-2026 Florida contractor figures put concrete repair and resurfacing in Winter Garden at {price('concrete-repair')} per {per('concrete-repair')}. "
                     "With a median home built in 2004, most cracking here traces to ordinary joint wear or fill settlement rather than the sudden ground collapse behind Orange County's place on the state's own sinkhole-claims roster."),
    "sections": [
        ("A relatively young housing stock still produces its first generation of cracks",
         f"<p>Winter Garden's typical home dates to 2004, and the city's population has kept climbing, from a 2020 base of 47,399 to about 48,063 by mid-2025 "
         f"({src('acs-wintergarden', 'Census Reporter local profile')}; {src('census-pep-v2025', 'latest Census population count')}). Slabs poured in that era are now old enough that ordinary joint and shrinkage cracking is starting to show up, well before the kind of age-related deterioration that shows up on a much older driveway elsewhere in the Orlando unit.</p>"),
        ("Orange County does make the state's own high-claims list, which changes how a crack gets read",
         f"<p>Office of Insurance Regulation figures cited in a 2010 Florida Senate interim report tie more than 88 percent of the sinkhole claims Florida insurers paid between 2006 and 2009 to just eleven counties, and Orange is on that roster "
         f"({src('fl-senate-2011-104', 'state sinkhole-claims report')}). That doesn't make every crack in a Winter Garden driveway a sinkhole; a diagonal crack over fill that was placed when the lot was graded is still the more common explanation, but it's part of why {svc('concrete-repair', 'a repair estimate')} here sometimes includes a closer look at the pattern of the cracking before assuming it's routine.</p>"),
    ],
    "scenario": ("Resurfacing a cracked driveway section, worked out in square feet",
                 f"<p>A 300-square-foot section of a 2006-era driveway, showing a straight crack along one wheel path, can run anywhere from about $900 up to $3,000 to resurface, applying the {price('concrete-repair')} per {per('concrete-repair')} range; a plain broom finish sits toward the lower end, and a decorative overlay pushes it higher. "
                 "Checking whether that crack follows an old control joint or cuts across the slab at an angle is part of deciding whether the subgrade needs attention first or the surface repair can go on as is.</p>"),
    "faqs": [
        faq("Is cracking in a newer Winter Garden driveway usually a sinkhole?",
            "Not usually. Orange County does rank among the counties a 2010 state Senate report tied to the heaviest run of Florida sinkhole claims, but ordinary joint cracking or fill settlement explains most cracks in a driveway built since the early 2000s far more often."),
        faq("Why would a Winter Garden driveway from the 2000s already need repair?",
            "A median home built in 2004 means a meaningful share of the city's original driveways are now old enough for ordinary joint and shrinkage cracking to appear, the normal first stage of wear rather than a sign of a bigger structural problem."),
        faq("Does resurfacing a Winter Garden driveway need a permit?",
            "Work that stays within the existing footprint is typically reviewed more lightly than a new driveway, but confirming the scope with the Building Division before assuming a lighter review avoids filing after the fact and tripling the fee."),
    ],
    "sources": SRC,
}

# 11. paver-sealing -------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing & Restoration in Winter Garden, FL",
    "meta": "Paver sealing in Winter Garden, FL: the normal twice-a-week SJRWMD watering calendar and cleaning pavers near Lake Apopka, Oct. 2026.",
    "h1": "Paver Sealing and Restoration Near Lake Apopka",
    "lede": capsule(f"A wash, re-sand and seal on Winter Garden pavers lands somewhere in {price('paver-sealing')} per {per('paver-sealing')}, the Florida figure this month. "
                     "Unlike several counties farther north, Orange isn't under a one-day-a-week watering order right now, and that distinction matters less for a sealing job than homeowners expect, since a hose-fed washer was never on the sprinkler calendar to begin with."),
    "sections": [
        ("Orange County's sprinkler calendar and a pressure washer run on two different clocks",
         f"<p>Odd and no-number addresses in the St. Johns district water Wednesday and Saturday under its year-round schedule, even addresses Thursday and Sunday, and the district states outright that the whole county follows that ordinary calendar rather than the stricter once-a-week order some neighboring districts are enforcing "
         f"({src('sjrwmd-watering', 'SJRWMD watering page')}). None of that touches a crew cleaning a paver surface by hand with a pressure washer ahead of sealing, since the watering restriction applies to sprinkler zones, not a hose run off an outdoor spigot.</p>"),
        ("Proximity to Lake Apopka can leave a surface damp a little longer after a storm",
         f"<p>Winter Garden grew up along the lake's south shore, and a patio or walkway within a block or two of that water tends to stay humid a bit past the point an inland yard would already be dry, giving algae and mildew a slight head start before the next {svc('paver-sealing', 'cleaning')}. "
         f"That's a reason to inspect a lakefront surface on a shorter cycle, not a rule that changes the sealing chemistry or the process itself.</p>"),
    ],
    "scenario": ("A patio cleaning and reseal job, sized in square feet",
                 f"<p>Take a 480-square-foot paver walkway and patio combination overdue for its wash, sand refresh and sealer: at the {price('paver-sealing')} per {per('paver-sealing')} range, that comes to somewhere between $720 and $1,560, with a few sunken pavers needing releveling adding to the total. "
                 "The crew picks the work date off the forecast rather than off any irrigation calendar, since getting a dry, clean surface before the sealer goes on is the only scheduling constraint that actually applies to this job.</p>"),
    "faqs": [
        faq("Does Orange County's sprinkler schedule limit when pavers can be pressure-washed?",
            "No. A hose-fed pressure washer isn't an irrigation zone, so cleaning pavers ahead of sealing can happen on any day the crew and the weather cooperate, regardless of which day the address is assigned to water the lawn."),
        faq("Is Winter Garden under the same strict watering limits as counties farther south?",
            "No. Orange follows the St. Johns district's ordinary twice-a-week schedule rather than the once-a-week shortage order several counties to the south and west are currently enforcing."),
        faq("Should pavers near Lake Apopka be sealed on a shorter cycle?",
            "A lot close to the shoreline often stays damp a bit longer after rain, which can speed up algae growth between cleanings. Checking that surface more often than one set back from the water is a reasonable precaution rather than a required schedule."),
    ],
    "sources": SRC,
}

# 12. retaining-walls -----------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Winter Garden, FL – Call First",
    "meta": "Retaining wall contractors in Winter Garden, FL: the city's unpublished height threshold and the statewide 48-inch engineering trigger, Oct. 2026.",
    "h1": "Retaining Walls for Winter Garden's Graded Lots",
    "lede": capsule(f"Florida contractors are quoting {price('retaining-wall')} per {per('retaining-wall')} for wall work in Winter Garden this fall. "
                     "The city hasn't put a height number on its own permit pages for when a retaining wall needs a sealed engineering drawing, so a call to the Building Division before a design on a graded lot near the lake, or near a newer subdivision in Horizon West, goes final is worth the few minutes it takes."),
    "sections": [
        ("Winter Garden's general FAQ covers every structure, but a wall-specific number is missing",
         f"<p>The city's own answer to when a permit is required states that one applies to “every public and private building, structure or appurtenances,” without naming a retaining-wall height that triggers a different level of review, a gap worth closing with a call to the Building Division, 407-877-5136, before a wall design is finalized "
         f"({src('wintergarden-when-permit', 'city permit guidance')}). Florida's own residential code sets a statewide trigger regardless of which city enforces it: a wall holding back more than 48 inches of unbalanced fill, or one over 24 inches that resists lateral loads beyond soil alone, needs a sealed engineering design, a threshold Orange County's own residential plan-approval guide spells out "
         f"({src('orange-res-plan-guide', 'the county plan-approval guide')}).</p>"),
        ("Grading near the lake and in the growth areas nearby is what drives the demand",
         f"<p>Winter Garden sits on the south shore of Lake Apopka, where a lot that drops toward the shoreline needs something to hold the grade at the edge of a patio or pool deck, and the fast-growing Horizon West area just southwest of the city is seeing new subdivisions graded and filled on a scale that creates the same need on a freshly built lot "
         f"({ext(APOPKA_URL, 'SJRWMD lake project page')}; {src('ocfl-horizonwest', 'county Horizon West page')}). A {svc('retaining-walls', 'retaining wall')} on either kind of lot is doing the same job, holding fill in place rather than letting it slump toward the lower side of the yard.</p>"),
    ],
    "scenario": ("Sizing a low block wall along a graded bed",
                 f"<p>A 30-foot run of block, 3 feet tall, holding a terraced planting bed at the edge of a patio, works out to 90 square feet of wall face. Multiplying that by the {price('retaining-wall')} per {per('retaining-wall')} range gives a job cost somewhere around $1,350 to $3,600, not counting the drainage gravel and pipe that go in behind the blocks. "
                 "That 3-foot height sits right at the state's unbalanced-fill threshold, so the design stays out of the sealed-engineering category; add even a foot more to hold back a steeper slope and the same wall would need a stamped drawing no matter which office reviews the permit.</p>"),
    "faqs": [
        faq("Does Winter Garden publish a height limit for when a retaining wall needs an engineer?",
            "Not on its own permit pages. The city's general guidance says a permit applies to every structure but doesn't name a wall-specific height. Florida's residential code sets a statewide 48-inch unbalanced-fill trigger for sealed engineering, which the Building Division would apply regardless."),
        faq("Why are retaining walls common near Lake Apopka in Winter Garden?",
            "A lot that slopes toward the shoreline needs something to hold the grade at the edge of a patio, driveway or pool deck, the same reason a wall shows up often in the fast-growing, newly graded subdivisions just southwest of the city in the Horizon West area."),
        faq("Does a low retaining wall in Winter Garden still need a permit?",
            "The city's own guidance doesn't carve out an exemption by height, so confirming with the Building Division before building even a short wall is worth the call, especially since filing after the work is done triples the fee."),
    ],
    "sources": SRC,
}

# 13. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Winter Garden, FL – Lake Setback",
    "meta": "Artificial turf installers in Winter Garden, FL: the state's 10-foot lake setback and the normal twice-weekly watering calendar, Oct. 2026.",
    "h1": "Artificial Turf for Winter Garden Yards",
    "lede": capsule(f"Turf installers are pricing Winter Garden jobs at {price('artificial-turf')} per {per('artificial-turf')} this fall. "
                     "A yard that touches Lake Apopka or one of the area's ponds and canals has a state-set buffer to measure before the layout is drawn, and once the base goes in, the sprinkler calendar that governs the rest of the county simply stops applying to that section of the yard."),
    "sections": [
        ("A shoreline buffer, not a fence line, sets where the turf can start",
         f"<p>Florida's rule for synthetic turf keeps it back 10 feet from a pond, lake or canal unless a seawall forms that edge, and bans buried irrigation underneath, specifying a washed stone base and a natural infill instead "
         f"({src('dep-rule', 'the DEP turf rule')}). Measuring that 10 feet from the actual water's edge, rather than from wherever the backyard fence happens to sit, is what decides the real usable footprint on a lot along Lake Apopka's south shore, where the shoreline and the property line rarely line up exactly.</p>"),
        ("A sodded lawn still answers to the sprinkler calendar; installed turf stops answering to it",
         f"<p>Outside any shortage order, the St. Johns district still limits every Orange County address to two sprinkler days a week and blocks watering between 10 a.m. and 4 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD watering page')}). New sod has to establish on exactly those two days; once {svc('artificial-turf', 'turf')} is down and the infill is swept in, that calendar no longer has anything to govern on that patch of the yard, which is the appeal for a strip that's struggled to hold grass under the normal schedule.</p>"),
    ],
    "scenario": ("Working the lake buffer into a turf layout",
                 f"<p>Picture a 540-square-foot run of backyard that ends at Lake Apopka's edge: pulling the layout back the required 10 feet from the water trims off roughly 60 square feet, leaving about 480 square feet to actually turf. At the {price('artificial-turf')} per {per('artificial-turf')} range, that comes to somewhere between $4,800 and $12,000 once pile height and backing are chosen. "
                 "Surveying the shoreline first, instead of assuming the fence marks the edge, is what sets the real number before a roll of turf is ordered.</p>"),
    "faqs": [
        faq("How far back from Lake Apopka does artificial turf have to stay?",
            "At least 10 feet from the water's edge itself, not from a fence or a property line, under the state's synthetic-turf rule. That buffer only goes away where a seawall, rather than open shoreline, forms the edge of the water."),
        faq("Once turf is installed, does it still need to follow Orange County's watering days?",
            "No. The sprinkler calendar governs irrigated sod and landscaping; a turf section with its base and infill already down has nothing left for that schedule to regulate."),
        faq("Can a homeowners association near Winter Garden still say no to artificial turf?",
            "An HOA's own design standards aren't touched by the state law that limits city and county turf restrictions, so checking the specific community's rules before buying materials is still worth doing."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
