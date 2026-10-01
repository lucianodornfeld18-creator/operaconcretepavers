# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, compare, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "sarasota"

SRC = [
    "city-sarasota-code-29.5-7-curb-cut-driveway",
    "city-sarasota-code-29.5-8-erosion",
    "city-sarasota-engineering-row",
    "city-sarasota-bp-guidelines",
    "city-sarasota-zoning-vi-203-impervious",
    "city-sarasota-zoning-vi-907-isod",
    "city-sarasota-permit-portal",
    "sarasota-tree",
    "sarasota-city-phase3",
    "acs-sarasota",
    "census-pep-v2025",
    "fdot-sdg",
    "fema-coastal-firm",
    "fdep-cccl-program",
    "fdep-cccl-apply",
    "swfwmd-restrictions",
    "dep-rule",
    "fs125572",
    "nrcs-eaugallie-osd",
    "nrcs-immokalee-osd",
    ("Laurel Park Historic District, National Register of Historic Places (listed March 11, 2008)", "https://en.wikipedia.org/wiki/Laurel_Park_Historic_District"),
    ("City of Sarasota tree protection ordinance — root-pruning, barricades and arborist inspection (Div. 3.1)", "https://sarasota.granicus.com/MetaViewer.php?view_id=102&clip_id=10075&meta_id=595968"),
]

HUB = page(
    "/sarasota-fl/", "city",
    "Concrete & Paver Contractor in Sarasota, FL",
    "Opera builds concrete driveways, pavers and turf in Sarasota, FL, where the city permits curb cuts under Sec. 29.5-7 and homes date to 1976, as of October 2026.",
    "Concrete, Pavers and Turf for Sarasota Homes",
    capsule(
        "Opera's Sarasota unit builds concrete driveways, pavers, pool decks and artificial turf in the city of Sarasota, where the Census Bureau counted 58,458 residents in July 2025 and the median home was built in 1976, the oldest housing stock in the unit. "
        "As of October 2026, a city engineer permits driveway curb cuts, impervious coverage is capped by zone, and the Southwest Florida Water Management District has the city on a once-a-week watering schedule."
    ),
    "".join([
        sec(
            "Which office in Sarasota permits a new driveway or curb cut?",
            "<p>The city engineer, not the county. Sec. 29.5-7 of the city code makes it unlawful to cut a street curb or build a driveway in the public right-of-way without a permit from the city engineer, and the work has to follow the city's own Engineering Design Criteria Manual " + src("city-sarasota-code-29.5-7-curb-cut-driveway", "Sec. 29.5-7, curb cuts and driveways") + ". The Engineering Division of Public Works handles that permit and the broader right-of-way, which it defines to include streets, alleys, parkways, sidewalks and drainage facilities, from 1575 2nd St, Monday through Friday 7:30 a.m. to 4:30 p.m., (941) 263-6793 or ROWerosion@sarasotafl.gov " + src("city-sarasota-engineering-row") + ". Applications go in through the city's online permitting portal " + src("city-sarasota-permit-portal", "ftgportal.sarasotafl.gov") + ". A " + svc("concrete-driveways") + " or " + svc("paver-driveways") + " replacement that stays inside the property line is a different question, covered next, and anyone grading or filling a lot before either one needs a separate erosion and siltation control permit under Sec. 29.5-8 unless the work is minor landscaping " + src("city-sarasota-code-29.5-8-erosion") + ".</p>"
        ),
        sec(
            "How much of a Sarasota lot can be paved before it hits the impervious cap?",
            "<p>Table VI-203 of the city's zoning code sets a maximum impervious coverage for every single-family lot, and a driveway, patio, pool deck or paver walkway all count toward it alongside the roof. The applicant has to state the percentage on the permit, and the zoning director can ask for a PE-sealed impervious surface plan on a tight lot " + src("city-sarasota-zoning-vi-203-impervious") + ".</p>" +
            table(
                "City of Sarasota maximum impervious coverage by zoning district (Table VI-203)",
                ["Zoning district", "Max. impervious coverage"],
                [
                    ["RSF-E", "60%"],
                    ["RSF-1", "70%"],
                    ["RSF-2, RSF-3, RSF-4", "75%"],
                    ["RSM-9", "75%"],
                    ["RTD-9 (attached)", "75%"],
                ],
                "Source: City of Sarasota Zoning Code §VI-203, checked October 2026. Confirm your parcel's zoning before planning a large driveway, pool deck or turf area."
            ) +
            "<p>Lido Key, St. Armands Key and Bird Key sit inside the city limits but answer to a second layer: the Coastal Islands Overlay District caps impervious coverage at 70% there, regardless of what the base zone would otherwise allow " + src("city-sarasota-zoning-vi-907-isod") + ".</p>"
        ),
        sec(
            "What does a median 1976 build year mean for a Sarasota project?",
            "<p>Sarasota's housing stock is the oldest of the ten towns the Sarasota unit serves, with a median year built of 1976 against a 2024 American Community Survey population of 56,970 " + src("acs-sarasota") + ", while the Census Bureau's own count put the city at 58,458 residents on July 1, 2025, up from 54,850 at the 2020 base " + src("census-pep-v2025") + ". A lot of driveways and slabs poured in the 1970s and 1980s are due for " + svc("concrete-repair") + " or a full tear-out, and older in-town grids such as the Laurel Park Historic District, listed on the National Register in 2008 with roughly 250 contributing buildings from 1920 to 1957, carry narrower lots and more mature canopy than the newer subdivisions east of the city " + ext("https://en.wikipedia.org/wiki/Laurel_Park_Historic_District", "Laurel Park Historic District") + ". That canopy matters: a city permit has to be pulled before anything thicker than 4.5 inches in diameter is cut down or moved, a live oak or sand live oak 24 inches across or wider counts as a Grand Tree, and root pruning near either has to be finished and inspected by the city arborist before a building permit can move to its own inspections " + src("sarasota-tree") + ".</p>"
        ),
        sec(
            "What do the barrier islands and flood zones change for a build?",
            "<p>Lido Key, St. Armands Key and Bird Key add a state layer on top of the city's own rules: any work seaward of Florida's Coastal Construction Control Line needs its own DEP sign-off first " + src("fdep-cccl-program") + ", applied for through the agency's own process " + src("fdep-cccl-apply") + ". FEMA's coastal maps split the risk two ways: Zone AE assumes roughly a one-in-a-hundred yearly chance of flooding with modest wave action, while the Coastal High Hazard Zone VE assumes those same odds plus surf big enough to tear into framing during a major storm " + src("fema-coastal-firm") + ". For bridge design, FDOT calls anything within 2,500 feet of water above 2,000 ppm chloride a marine environment, a fair stand-in for how salty the air gets off Sarasota Bay and the barrier islands " + src("fdot-sdg") + ". None of the city sources reviewed set a height threshold that automatically triggers engineering on a " + svc("retaining-walls") + ", so a wall holding back fill near the water is worth a call to the Building Division before design starts.</p>"
        ),
        sec(
            "How does the current watering order change sod, turf and new concrete here?",
            "<p>The Southwest Florida Water Management District put Sarasota under a Modified Phase III shortage order that began April 3, 2026 and runs through the end of March 2027, a timeline the city confirmed on its own news page in September 2026 " + src("sarasota-city-phase3") + ". The table below shows the one watering day each address gets " + src("swfwmd-restrictions") + ".</p>" +
            table(
                "SWFWMD Modified Phase III watering day by street address (checked October 2026)",
                ["Last digit of address", "Watering day"],
                [["0 or 1", "Monday"], ["2 or 3", "Tuesday"], ["4 or 5", "Wednesday"], ["6 or 7", "Thursday"], ["8 or 9", "Friday"]],
                "One day a week only, between 12:01 and 4 a.m. or between 8 p.m. and 11:59 p.m."
            ) +
            "<p>New sod still gets a short grace period, daily water for the first 30 days and three days a week for the next 30, a window that overlaps with the hand-watering a freshly poured driveway or patio slab needs for curing, so the two are worth planning together. " + svc("artificial-turf") + " sits outside the order entirely once it's installed, which is part of why it comes up so often against sod on tight lots; see how much that saves in " + compare("artificial-turf-vs-sod", "artificial turf vs sod in Florida") + ".</p>"
        ),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq(
            "Do you work on Longboat Key, Siesta Key and Anna Maria Island?",
            "Yes, the Sarasota unit covers the barrier islands along with the mainland city. Island jobs add Florida's Coastal Construction Control Line permit, FEMA's VE and AE flood zones, and the salt-air conditions FDOT treats as a marine environment within 2,500 feet of the water, on top of whichever town or county desk issues the local permit."
        ),
        faq(
            "Do I need a permit for a patio or pool deck on my own lot in Sarasota?",
            "The city's Building Permit Requirement Guidelines only list gas, mechanical and plumbing work as exempt, and don't name patios, slabs or pavers either way; the guideline itself says to call the Building Division at (941) 263-6494 when it's unclear, which we treat as the answer rather than guess."
        ),
        faq(
            "How much of my Sarasota lot can be covered in concrete, pavers or a pool deck?",
            "It depends on the zoning district: Table VI-203 caps impervious coverage at 60% in RSF-E, 70% in RSF-1, and 75% in RSF-2 through RSF-4, RSM-9 and attached RTD-9 lots, with a separate 70% cap on Lido Key, St. Armands Key and Bird Key regardless of the base zone."
        ),
        faq(
            "Will removing a tree for a new driveway need a city permit?",
            "Any tree over 4.5 inches in diameter needs a removal or relocation permit, and a live oak or sand live oak 24 inches in diameter or larger counts as a Grand Tree with stricter protection. Root pruning near a protected tree has to be finished and signed off by the city arborist before building-permit inspections can proceed."
        ),
        faq(
            "Is my address in a flood zone that affects a pool deck or retaining wall?",
            "Possibly, especially near the bay or on a barrier island. Zone AE on FEMA's maps assumes roughly a one-in-a-hundred yearly flood chance with modest waves; the higher-hazard Zone VE assumes the same odds with surf capable of tearing into a low deck or an unengineered wall."
        ),
        faq(
            "Does artificial turf save water under Sarasota's current restrictions?",
            "It sidesteps them. SWFWMD's Modified Phase III order limits irrigation to one day a week in a pre-dawn or late-night window through March 2027, a schedule sod has to live with and turf does not, once the installation itself is finished and watered in."
        ),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Sarasota",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/sarasota-county-driveway-patio-permits/", "Driveway and patio permits in Sarasota, Venice and North Port"),
        ("/lakewood-ranch-fl/", "Concrete, pavers and turf in Lakewood Ranch"),
        ("/bradenton-fl/", "Concrete, pavers and turf in Bradenton"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Sarasota, FL",
)

LOCAL = {
    "concrete-driveways": {
        "title": "Concrete Driveways in Sarasota, FL – Permit Guide",
        "meta": "Concrete driveways in Sarasota, FL need a city engineer permit for the curb cut under Sec. 29.5-7; market range is " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", as of October 2026.",
        "h1": "Concrete Driveway Installation in Sarasota",
        "lede": capsule(
            "A new or replacement concrete driveway in Sarasota runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026, before the part that touches the right-of-way, which the city engineer permits separately under Sec. 29.5-7. "
            "Lots here sit on EauGallie or Immokalee flatwoods soil, with a seasonal water table within 18 inches of the surface, which shapes how the base and swale get built."
        ),
        "sections": [
            (
                "Why the apron is a separate permit from the rest of the slab",
                "<p>Sec. 29.5-7 draws a hard line at the property edge: it is unlawful to cut a curb or build a driveway in the public right-of-way without a permit from the city engineer, built to the Engineering Design Criteria Manual, with a fee the city sets under a separate ordinance " + src("city-sarasota-code-29.5-7-curb-cut-driveway", "City of Sarasota Code §29.5-7") + ". The Engineering Division that issues it covers the right-of-way broadly, streets, alleys, parkways, sidewalks and drainage, out of 1575 2nd St, (941) 263-6793 or ROWerosion@sarasotafl.gov, Monday through Friday 7:30 to 4:30 " + src("city-sarasota-engineering-row") + ". Applications go in online through the city's permitting portal " + src("city-sarasota-permit-portal", "ftgportal.sarasotafl.gov") + ". The slab between the sidewalk and the garage is a separate question; the city's own Building Permit Requirement Guidelines don't name driveways on the exempt list, so when the scope is unclear we call the Building Division at (941) 263-6494 before pricing the job " + src("city-sarasota-bp-guidelines") + ".</p>"
            ),
            (
                "What flatwoods soil does to the base under the slab",
                "<p>Most Sarasota lots sit on EauGallie or Immokalee fine sand, both poorly drained flatwoods soils with a seasonal high water table within about 6 to 18 inches of the surface for part of the year " + src("nrcs-eaugallie-osd") + " " + src("nrcs-immokalee-osd") + ". Florida's residential code limits clean sand or gravel fill under a slab to 24 inches and earth fill to 8 inches unless an engineer approves otherwise, and calls for at least 4 inches of compacted base beneath it. On a driveway headed for a boat trailer or a dual-axle work truck, we go beyond the 3½-inch code minimum and thicken the section rather than lean on the base alone to carry the extra load, since a wet subgrade gives a slab less to work with than a well-drained ridge lot would.</p>"
            ),
        ],
        "scenario": (
            "Say you have an 18 × 50 ft driveway, 900 sq ft, in one of Sarasota's 1970s-built subdivisions where the original slab has settled unevenly near the street",
            "<p>Say you have an 18 × 50 ft driveway, 900 sq ft, in one of Sarasota's 1970s-built subdivisions where the original slab has settled unevenly near the street. At the market range of " + price("concrete-driveway") + " per sq ft, a full tear-out and repour lands between $5,400 and $13,500, and within the typical " + price("concrete-driveway", typical=True) + " band that narrows to roughly $7,200 to $10,800. That figure covers only the private portion; the apron in the right-of-way needs its own Sec. 29.5-7 permit from the city engineer, and if the old slab's edge sits closer to a live oak than the city's root-pruning barricade distance, the arborist inspection has to clear before the pour can be scheduled. A written quote follows a site visit, since the swale grade and the condition of the existing base change the number.</p>"
        ),
        "faqs": [
            faq(
                "Does a straight driveway replacement in Sarasota need a city permit?",
                "The portion in the right-of-way does, under Sec. 29.5-7, issued by the city engineer through the Engineering Division. The private portion between the sidewalk and the garage falls into a gap the city's own guidelines don't name directly, so we confirm with the Building Division before starting."
            ),
            faq(
                "Why does the water table in Sarasota matter for a driveway base?",
                "EauGallie and Immokalee, the two soils most common under Sarasota driveways, run poorly drained with a shallow seasonal high water table for part of the year. A wet subgrade compacts differently than dry ridge sand, which is one reason we don't treat every lot's base the same way."
            ),
            faq(
                "Can I widen my driveway past the current apron in Sarasota?",
                "Widening crosses back into right-of-way territory, so it needs the same Sec. 29.5-7 permit as a new driveway, plus a check against the lot's impervious coverage cap under Table VI-203 before the city engineer signs off."
            ),
        ],
        "sources": SRC,
    },
    "paver-driveways": {
        "title": "Paver Driveways in Sarasota, FL – Impervious Caps",
        "meta": "Paver driveways in Sarasota, FL count toward the city's Table VI-203 impervious cap; market range is " + price("paver-driveway") + " per " + per("paver-driveway") + ", as of October 2026.",
        "h1": "Paver Driveway Installation in Sarasota",
        "lede": capsule(
            "A paver driveway in Sarasota runs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026, and every square foot of it counts toward the city's per-zone impervious coverage cap under Table VI-203. "
            "In older in-town neighborhoods such as Laurel Park, a driveway this size also sits close enough to protected live oaks that root pruning has to clear with the city arborist first."
        ),
        "sections": [
            (
                "Why pavers still count against the impervious limit",
                "<p>A driveway in brick pavers does not get treated as pervious under City of Sarasota zoning just because water can move through the joints. Table VI-203 sets the maximum impervious coverage by zoning district, from 60% in RSF-E up to 75% in RSF-2 through RSF-4, and the permit applicant has to state the percentage, with the director able to require a PE-sealed impervious surface plan on a lot that is already close to the line " + src("city-sarasota-zoning-vi-203-impervious") + ". On Lido Key, St. Armands Key and Bird Key, a second layer applies: the Coastal Islands Overlay District caps coverage at 70% no matter what the base zone would otherwise allow " + src("city-sarasota-zoning-vi-907-isod") + ". Anyone widening a two-car driveway to three cars on a tight island lot should run that math before ordering pavers, not after.</p>"
            ),
            (
                "Working around protected live oaks on older lots",
                "<p>Sarasota's in-town grids, Laurel Park among them, were platted between 1920 and 1957 and carry more mature canopy than the subdivisions built decades later " + ext("https://en.wikipedia.org/wiki/Laurel_Park_Historic_District", "Laurel Park Historic District") + ". A city permit has to be pulled before anything thicker than 4.5 inches in diameter comes down or gets moved, and a live oak or sand live oak 24 inches across or wider counts as a Grand Tree, with its own 20-foot barricade distance and a root-pruning inspection the city arborist has to sign off on before building-permit inspections can move forward " + src("sarasota-tree") + ". Excavating a 6-inch paver base close to a live oak's root flare without that sign-off is the kind of delay that is cheaper to avoid than to fix.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 16 × 40 ft two-car paver driveway, 640 sq ft, going in on a Laurel Park lot with a mature live oak near the property line",
            "<p>Say you have a 16 × 40 ft two-car paver driveway, 640 sq ft, going in on a Laurel Park lot with a mature live oak near the property line. At the market range of " + price("paver-driveway") + " per sq ft, that runs $6,400 to $19,200, narrowing to roughly $7,680 to $12,800 in the typical " + price("paver-driveway", typical=True) + " band depending on paver type and whether an old slab has to come out first. Before the aggregate base goes in, the root zone near that oak gets measured against the city's barricade distance, and if excavation reaches into the protected root area, the arborist inspection has to clear before the Sec. 29.5-7 right-of-way apron can be scheduled. The driveway's footprint also gets checked against the lot's Table VI-203 cap alongside the existing roof and any patio already on the property.</p>"
        ),
        "faqs": [
            faq(
                "Do pavers count differently than concrete for Sarasota's impervious limit?",
                "No. Table VI-203 treats a paver driveway the same as a poured one for impervious coverage purposes in the text reviewed; the permit still requires the applicant to state the percentage covered against the zone's cap."
            ),
            faq(
                "What if my new paver driveway is close to a live oak?",
                "The city treats any tree over 4.5 inches in diameter as protected, with stricter rules for a Grand Tree 24 inches or larger. Root pruning near the tree has to be inspected by the city arborist before building-permit inspections proceed."
            ),
            faq(
                "Is the permit different for a paver driveway on Lido Key or St. Armands?",
                "The underlying city permits are the same, but the Coastal Islands Overlay District adds its own 70% impervious coverage cap on those parcels, regardless of what the base zoning district would otherwise allow."
            ),
        ],
        "sources": SRC,
    },
    "concrete-patios": {
        "title": "Concrete Patios in Sarasota, FL – Permit Rules",
        "meta": "Concrete patios in Sarasota, FL fall outside the city's published permit exemptions; market range is " + price("concrete-patio") + " per " + per("concrete-patio") + ", as of October 2026.",
        "h1": "Concrete Patio Installation in Sarasota",
        "lede": capsule(
            "A concrete patio in Sarasota runs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. The city's own permit guidelines don't name patios one way or the other, "
            "so confirming with the Building Division before pouring is part of the job, not an afterthought."
        ),
        "sections": [
            (
                "Why a patio slab can trigger a grading permit before it triggers a building one",
                "<p>Sec. 29.5-8 of the city code requires an erosion and siltation control permit from the city engineer before cutting, filling, grading or altering the natural topography of a lot, with an exemption for minor land-disturbing activities such as garden work, individual home landscaping and routine repairs " + src("city-sarasota-code-29.5-8-erosion") + ". A small patio addition that doesn't change the lot's grade usually stays inside that exemption; a larger lanai extension that reworks drainage toward a neighbor's fence line is the kind of project where that line gets tested. Separately, the city's Building Permit Requirement Guidelines list only gas, mechanical and plumbing work as exempt under FBC 105.2, and say nothing about patios or slabs either way, closing with: \"When in doubt... call the City Building Division at (941) 263-6494\" " + src("city-sarasota-bp-guidelines") + ".</p>"
            ),
            (
                "What counts against the lot's coverage once the patio is in",
                "<p>Whatever the permit question resolves to, the finished patio still counts toward the lot's impervious coverage under Table VI-203, the same cap that applies to the driveway and the roof, running from 60% in RSF-E up to 75% in the densest single-family zones " + src("city-sarasota-zoning-vi-203-impervious") + ". On a lot that already carries a full driveway and a pool deck, we run that math before design rather than after, since a patio that pushes a parcel over its zone's limit is a redesign, not a change order. A " + svc("paver-patios") + " alternative changes the look and the joint maintenance, not the coverage math.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 20 × 16 ft lanai extension, 320 sq ft, off the back of a screened pool cage on a standard RSF-3 lot",
            "<p>Say you have a 20 × 16 ft lanai extension, 320 sq ft, off the back of a screened pool cage on a standard RSF-3 lot. At the market range of " + price("concrete-patio") + " per sq ft, that runs $1,920 to $4,160, or roughly $2,240 to $3,200 in the typical " + price("concrete-patio", typical=True) + " band for a broom-finished slab with a control-joint layout sized to the panel. Because the addition sits flush with the existing grade and doesn't reroute drainage, it is the kind of scope that usually clears Sec. 29.5-8's minor-landscaping exemption, but we still confirm the building-permit question with the city before pouring, since the guidelines leave patios unaddressed either way. Adding the new square footage to the lot's existing coverage total against the RSF-3 cap is part of that same call.</p>"
        ),
        "faqs": [
            faq(
                "Does a small concrete patio in Sarasota need a building permit?",
                "The city's own guidelines don't say either way; they list only gas, mechanical and plumbing exemptions and tell homeowners to call the Building Division at (941) 263-6494 when it's unclear, which is what we do before pricing a patio job."
            ),
            faq(
                "Does regrading my backyard for a patio need a separate permit?",
                "If the work alters the lot's natural topography beyond routine landscaping, Sec. 29.5-8 requires an erosion and siltation control permit from the city engineer. Minor grading tied to ordinary home maintenance is exempt."
            ),
            faq(
                "Will a new patio push my lot over Sarasota's impervious limit?",
                "It can, especially on a lot that already carries a full driveway and pool deck. Table VI-203 caps coverage by zone, so we add the planned patio to the existing total before finalizing the design."
            ),
        ],
        "sources": SRC,
    },
    "paver-patios": {
        "title": "Paver Patios in Sarasota, FL – Older-Home Guide",
        "meta": "Paver patios in Sarasota, FL fit homes built around 1976 and salt-air lots near the bay; market range is " + price("paver-patio") + " per " + per("paver-patio") + ", October 2026.",
        "h1": "Paver Patios and Walkways in Sarasota",
        "lede": capsule(
            "A paver patio in Sarasota runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. With a median home here built in 1976, a lot of patio work is an addition "
            "to a pool cage that came later, not a first installation, and bay-side lots add salt air most ridge towns don't deal with."
        ),
        "sections": [
            (
                "Adding a paver patio to a 1970s pool cage",
                "<p>Sarasota's median year structure built is 1976, the oldest in the Sarasota unit's service area, against a 2024 ACS population estimate of 56,970 " + src("acs-sarasota") + ". Plenty of those homes added a screened pool cage sometime after the original build, with a concrete patio sized to the cage footprint at the time. A paver patio extension past that original edge usually means tying a new edge restraint into the old slab rather than pouring fresh concrete under the existing screen frame, and matching the paver's joint pattern to whatever walkway already runs from the lanai to the yard. " + svc("concrete-patios") + " covers the plain-concrete version of the same addition.</p>"
            ),
            (
                "What salt air near the bay changes about a patio build",
                "<p>Bridges within 2,500 feet of water above 2,000 ppm chloride fall under FDOT's own marine-environment classification, and a lot backing onto Sarasota Bay or a canal off it sits well inside that same salt-air band " + src("fdot-sdg") + ". That doesn't change how the base or bedding sand gets built, but it does change how soon a sealer, a metal edge restraint or an unprotected fastener on a nearby fence starts showing it. " + svc("paver-sealing") + " and the unit's piece on " + post("saltwater-pools-and-coastal-salt-air-hardscape", "salt air and coastal hardscape") + " cover the upkeep side in more depth.</p>"
            ),
        ],
        "scenario": (
            "Say you have an 18 × 22 ft paver patio and connecting walkway, 396 sq ft, extending a screened lanai on a bayside lot",
            "<p>Say you have an 18 × 22 ft paver patio and connecting walkway, 396 sq ft, extending a screened lanai on a bayside lot. At the market range of " + price("paver-patio") + " per sq ft, that runs $3,960 to $6,732, or roughly $4,752 to $6,336 in the typical " + price("paver-patio", typical=True) + " band depending on paver size and pattern. Because the lot backs onto open water, we favor an edge restraint and fastener hardware rated for a salt-air environment over the standard spec, and plan the joint-sand choice with resealing in mind rather than treating it as a one-time install. Tying the new paver edge into the existing 1970s pool-cage slab without a visible seam is usually the trickiest part of the layout, not the base work itself.</p>"
        ),
        "faqs": [
            faq(
                "Can a paver patio be added to an existing 1970s pool cage in Sarasota?",
                "Usually, by tying a new edge restraint into the old slab at the cage's footprint rather than pouring under the existing screen frame. The main constraint is matching the new joint pattern to whatever walkway already runs from the lanai."
            ),
            faq(
                "Does salt air near Sarasota Bay change how a paver patio is built?",
                "It doesn't change the base or bedding sand, but it does affect how fast a sealer or metal edge restraint shows wear on a lot within a couple thousand feet of open water, so we spec hardware accordingly on bayside jobs."
            ),
            faq(
                "Do I need a permit for a paver patio addition in Sarasota?",
                "The city's guidelines don't name patios or pavers directly; if the scope is a straightforward addition at grade, we confirm with the Building Division before starting rather than assume either answer."
            ),
        ],
        "sources": SRC,
    },
    "concrete-pool-decks": {
        "title": "Concrete Pool Decks in Sarasota, FL – Flood Zones",
        "meta": "Concrete pool decks in Sarasota, FL sit in FEMA Zone AE or VE on many lots; market range is " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ", October 2026.",
        "h1": "Concrete Pool Deck Installation in Sarasota",
        "lede": capsule(
            "A concrete pool deck in Sarasota runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. Many lots near the bay or the barrier islands "
            "sit in a FEMA flood zone, and a live oak canopy over the cage is common enough on 1976-era homes to plan around."
        ),
        "sections": [
            (
                "What FEMA's flood zones mean for a deck near the water",
                "<p>FEMA's coastal maps sort Sarasota's waterfront lots into two main categories: Zone AE, a roughly one-in-a-hundred yearly flood chance with modest wave action, and the Coastal High Hazard Zone VE, the same odds but with surf capable of punching through a wall during a major storm " + src("fema-coastal-firm") + ". Neither zone bans a pool deck outright, but both change how fill and drainage get handled at the slab's edge, and the dividing line between them is worth a look on FEMA's own map viewer early, since it can split a single street in two. A deck planned without that look is the kind of redesign that costs more once concrete is already on order.</p>"
            ),
            (
                "Working a deck slab around an older live oak canopy",
                "<p>Sarasota's median home dates to 1976, old enough that the live oak over a lot's pool cage is often original to the property, not a recent planting. The city treats any tree over 4.5 inches in diameter as protected, with a 24-inch-or-larger live oak qualifying as a Grand Tree and root pruning near it requiring the city arborist's sign-off before building-permit inspections proceed " + src("sarasota-tree") + ". On a deck pour that wraps close to a trunk like that, we plan the expansion joint at the coping and the slab's edge with the protected root zone in mind, not just the pool equipment layout.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 30 × 30 ft pool deck, 900 sq ft, around a screened cage on a lot a few blocks off the bay",
            "<p>Say you have a 30 × 30 ft pool deck, 900 sq ft, around a screened cage on a lot a few blocks off the bay. At the market range of " + price("concrete-pool-deck") + " per sq ft, that runs $4,500 to $13,500, narrowing to roughly $6,300 to $10,800 in the typical " + price("concrete-pool-deck", typical=True) + " band for a broom or spray-textured finish with slope to a drain. Because the parcel is close enough to open water to fall in FEMA's Zone AE on the current flood map, the deck's edge and any fill under it get built with that base-flood context in mind rather than treated as an inland pour. If a mature oak shades part of the cage, the deck's control-joint layout is planned around its protected root zone before the forms go in.</p>"
        ),
        "faqs": [
            faq(
                "Is my Sarasota pool deck lot in a flood zone?",
                "Possibly; waterfront and barrier-island lots here commonly fall in Zone AE or the higher-hazard Zone VE. FEMA's own map viewer shows the exact line for a given parcel, and it can change from one side of a street to the other."
            ),
            faq(
                "Does a live oak over the pool cage affect the deck design?",
                "It can. Any tree over 4.5 inches in diameter is protected, and a 24-inch-or-larger live oak counts as a Grand Tree with its own root-pruning and arborist sign-off requirements before building-permit inspections proceed."
            ),
            faq(
                "Does the pool deck count toward my Sarasota lot's impervious limit?",
                "Yes. It counts alongside the roof, driveway and any patio against the zone's cap under Table VI-203, which runs from 60% to 75% depending on the district."
            ),
        ],
        "sources": SRC,
    },
    "pool-deck-pavers": {
        "title": "Pool Deck Pavers in Sarasota, FL – Barrier Islands",
        "meta": "Pool deck pavers in Sarasota, FL face the Coastal Islands Overlay's 70% cap on Lido and St. Armands; range " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ", Oct. 2026.",
        "h1": "Travertine and Paver Pool Decks in Sarasota",
        "lede": capsule(
            "Pool deck pavers or travertine in Sarasota run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. On Lido Key, St. Armands Key and Bird Key, "
            "the deck's footprint answers to a 70% impervious cap that applies on top of the state's coastal construction permit."
        ),
        "sections": [
            (
                "The 70% cap on Lido, St. Armands and Bird Key",
                "<p>Those three islands sit inside the Sarasota city limits but carry an extra layer of zoning: the Coastal Islands Overlay District caps impervious coverage at 70% of the lot, regardless of what the base zoning district would otherwise allow " + src("city-sarasota-zoning-vi-907-isod") + ". A travertine or paver pool deck on one of these parcels gets measured against that 70% alongside the house footprint, the driveway and any patio, which is a tighter number than the 75% many mainland RSF-2 through RSF-4 lots work with " + src("city-sarasota-zoning-vi-203-impervious") + ". On a lot that is already near the line, widening a deck by even a few feet of paver coverage is worth running past the zoning counter before it is designed.</p>"
            ),
            (
                "Building seaward of the Coastal Construction Control Line",
                "<p>Island lots close to the Gulf add a state permit on top of the city's: any construction or excavation seaward of Florida's Coastal Construction Control Line needs its own DEP sign-off " + src("fdep-cccl-program") + ", applied for through the agency's own process " + src("fdep-cccl-apply") + ". A pool deck addition that extends toward the beach side of a Lido Key or Longboat-adjacent lot is the kind of project where that line, not just the city's setback, decides how far the deck can reach. Salt exposure is part of the same equation: FDOT's marine-environment criterion covers any structure within 2,500 feet of water above 2,000 ppm chloride, which describes most of these parcels outright " + src("fdot-sdg") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have an 850 sq ft travertine pool deck overlay on an older concrete deck on a Lido Key lot",
            "<p>Say you have an 850 sq ft travertine pool deck overlay on an older concrete deck on a Lido Key lot. At the market range of " + price("pool-deck-pavers") + " per sq ft, that runs $10,200 to $25,500, or roughly $11,900 to $18,700 in the typical " + price("pool-deck-pavers", typical=True) + " band depending on the stone and pattern. Before the overlay is priced, the existing impervious coverage on the parcel gets checked against the Coastal Islands Overlay's 70% cap, since the old deck plus the house and driveway may already be close to it, and if the project extends the deck's footprint seaward of the control line, the DEP permit question gets answered before the city's own sign-off is even relevant.</p>"
        ),
        "faqs": [
            faq(
                "Is the impervious limit different for a pool deck on Lido Key?",
                "Yes. The Coastal Islands Overlay District caps Lido Key, St. Armands Key and Bird Key parcels at 70% impervious coverage, which applies instead of the base zoning district's usual 60-75% range used on the mainland."
            ),
            faq(
                "Does a pool deck on the Gulf side need a state permit too?",
                "If it's seaward of Florida's Coastal Construction Control Line, yes, a DEP permit is required before any city sign-off is relevant. Check the parcel's position relative to the line before finalizing a deck layout near the beach."
            ),
            faq(
                "Why does salt air matter more for a paver pool deck here than inland?",
                "FDOT's own criterion treats any structure within 2,500 feet of water above 2,000 ppm chloride as a marine environment, which covers most island and bayfront pool decks, and it's a reason we weigh sealer and joint-sand choices differently on those lots."
            ),
        ],
        "sources": SRC,
    },
    "stamped-concrete": {
        "title": "Stamped Concrete in Sarasota, FL – In-Town Lots",
        "meta": "Stamped concrete in Sarasota, FL works around live oaks on older in-town lots like Laurel Park; market range is " + price("stamped-concrete") + " per " + per("stamped-concrete") + ", Oct. 2026.",
        "h1": "Stamped Concrete Driveways and Patios in Sarasota",
        "lede": capsule(
            "Stamped concrete in Sarasota runs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October 2026. Older in-town neighborhoods, Laurel Park among them, "
            "pair narrower lots with mature live oak canopy, which shapes both the pattern choice and the permit path."
        ),
        "sections": [
            (
                "Why pattern choice reads differently on a 1920s-1950s lot",
                "<p>Laurel Park, listed on the National Register of Historic Places in March 2008, covers roughly 50 acres just south of downtown and contains about 250 contributing buildings built between 1920 and 1957 " + ext("https://en.wikipedia.org/wiki/Laurel_Park_Historic_District", "Laurel Park Historic District") + ". A slate or ashlar stamped pattern in a muted integral color tends to read as period-appropriate on a lot like that in a way a bright stamped cobble pattern sized for a 1990s subdivision driveway does not; it's a styling call homeowners here make more often than in the unit's newer towns. The release agent and sealer choice matter just as much on a narrow in-town lot, since there is less room between the driveway edge and the house to correct a color that reads wrong in afternoon shade.</p>"
            ),
            (
                "Building a stamped slab close to a protected live oak",
                "<p>Older in-town lots carry more mature canopy, and Sarasota's own tree rule applies regardless of the decorative finish on the slab: any tree over 4.5 inches in diameter needs a permit to remove or relocate, a live oak or sand live oak 24 inches or larger is a Grand Tree, and root pruning near either has to be finished and inspected by the city arborist before building-permit inspections can proceed, with barricades set at least 20 feet from a Grand Tree's trunk " + src("sarasota-tree") + ". A stamped driveway extension that crowds a live oak's root flare is worth flagging to the arborist before the forms go in, not after excavation has already disturbed the root zone.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 400 sq ft stamped-concrete front walk and entry patio on a Laurel Park-era lot with a large live oak near the walk",
            "<p>Say you have a 400 sq ft stamped-concrete front walk and entry patio on a Laurel Park-era lot with a large live oak near the walk. At the market range of " + price("stamped-concrete") + " per sq ft, that runs $3,200 to $7,600, or roughly $4,800 to $6,400 in the typical " + price("stamped-concrete", typical=True) + " band depending on the pattern and number of colors. Before excavation starts, the oak's root zone is measured against the city's protected-tree barricade distance, and if the new walk's edge sits inside it, the arborist inspection has to clear before the forms go in. A slate or ashlar pattern in a single integral color is the choice we steer toward on a lot this close to a historic grid, over a brighter multi-color cobble pattern that reads newer than the house around it.</p>"
        ),
        "faqs": [
            faq(
                "Does a stamped-concrete pattern need to match Laurel Park's historic look?",
                "There's no code requirement tied to the stamp pattern itself, but a muted slate or ashlar pattern tends to suit a 1920s-1950s house better than a bright multi-color cobble pattern sized for a newer subdivision, so it's the default we suggest on older in-town lots."
            ),
            faq(
                "Can I pour stamped concrete close to a live oak in Sarasota?",
                "Only after the root zone is checked. Any tree over 4.5 inches in diameter is protected, and a Grand Tree 24 inches or larger requires root pruning to be finished and inspected by the city arborist before building-permit inspections proceed."
            ),
            faq(
                "Does stamped concrete cost more than plain concrete in Sarasota?",
                "The market range here is " + price("stamped-concrete") + " per sq ft versus " + price("concrete-driveway") + " for plain concrete, reflecting the integral color, release agent and stamping labor; the subgrade and permit questions are the same either way."
            ),
        ],
        "sources": SRC,
    },
    "concrete-walkways": {
        "title": "Concrete Walkways in Sarasota, FL – ROW Rules",
        "meta": "Concrete walkways in Sarasota, FL fall under the same Engineering Division that manages sidewalks and drainage; market range is " + price("concrete-walkway") + " per " + per("concrete-walkway") + ".",
        "h1": "Concrete Sidewalks and Walkways in Sarasota",
        "lede": capsule(
            "A concrete walkway or sidewalk section in Sarasota runs " + price("concrete-walkway") + " per " + per("concrete-walkway") + " as of October 2026. Any part of it in the public right-of-way "
            "answers to the same Engineering Division that handles driveway curb cuts and drainage, not a separate desk."
        ),
        "sections": [
            (
                "Who reviews a walkway that touches the sidewalk strip",
                "<p>The city's Engineering Division, part of Public Works, defines the right-of-way it regulates broadly: streets, alleys, parkways, sidewalks and drainage facilities all fall under the same permit desk at 1575 2nd St, (941) 263-6793 or ROWerosion@sarasotafl.gov " + src("city-sarasota-engineering-row") + ". A front walkway that crosses the sidewalk strip between the property line and the street is treated the same way a driveway apron is, under the city engineer's permit authority established by Sec. 29.5-7 for cutting or building in that strip " + src("city-sarasota-code-29.5-7-curb-cut-driveway") + ". A side-yard path that stays entirely on private ground, by contrast, is the kind of small-footprint work the Building Permit Requirement Guidelines are least clear about, which is why we confirm scope with the Building Division before pricing a walkway that's partly public, partly private.</p>"
            ),
            (
                "Routing a path around a protected tree's root zone",
                "<p>A straight walkway from the driveway to the front door is one of the more common places a Sarasota job runs into a protected tree, since the shortest line between two points often crosses a live oak's drip line on an older lot. The city requires a permit before removing or relocating any tree over 4.5 inches in diameter and sets a 20-foot barricade distance around a Grand Tree, a live oak 24 inches in diameter or larger among them " + src("sarasota-tree") + ". We route a walkway's curve around that root zone rather than ask for a removal permit on a tree that size, both because the permit itself is not guaranteed and because a mature oak's shade is part of what makes an in-town Sarasota lot worth the detour.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 4 × 38 ft front walkway, about 150 sq ft, connecting the driveway to the entry on a lot with an oak near the front corner",
            "<p>Say you have a 4 × 38 ft front walkway, about 150 sq ft, connecting the driveway to the entry on a lot with an oak near the front corner. At the market range of " + price("concrete-walkway") + " per sq ft, that runs $1,050 to $2,550, or roughly $1,200 to $1,800 in the typical " + price("concrete-walkway", typical=True) + " band for a broom-finished walk with a control joint about every 4 feet. Where the walk crosses the sidewalk strip near the street, it falls under the same Sec. 29.5-7 permit as a driveway apron; where it curves around the oak at the front corner, we keep the route outside the tree's protected root zone rather than request a removal permit for a tree that size.</p>"
        ),
        "faqs": [
            faq(
                "Does a front walkway need the same permit as a driveway in Sarasota?",
                "The portion that crosses the public sidewalk strip does, under the city engineer's Sec. 29.5-7 authority, handled by the same Engineering Division that manages sidewalks and drainage generally. A path that stays fully on private ground is a different, less clearly defined case."
            ),
            faq(
                "Can I remove a tree in the way of a new walkway?",
                "Any tree over 4.5 inches in diameter needs a city permit to remove or relocate, and a Grand Tree, a 24-inch-or-larger live oak among them, is harder to clear. We usually route the walkway around the tree instead."
            ),
            faq(
                "What finish holds up best on a Sarasota sidewalk section?",
                "A broom finish with joints spaced to the slab thickness is standard for sidewalk work here, matching what the city's own sidewalk specifications call for on public-facing concrete."
            ),
        ],
        "sources": SRC,
    },
    "concrete-slabs": {
        "title": "Concrete Slabs in Sarasota, FL – Pads & Fill",
        "meta": "Concrete slabs in Sarasota, FL need fill sized to flatwoods soil and FBC limits; market range is " + price("concrete-slab") + " per " + per("concrete-slab") + ", as of October 2026.",
        "h1": "Concrete Slabs for Sheds, AC Pads and Parking",
        "lede": capsule(
            "A concrete slab in Sarasota, for a shed, an AC pad or RV parking, runs " + price("concrete-slab") + " per " + per("concrete-slab") + " as of October 2026. Flatwoods soil "
            "and a shallow seasonal water table shape how much fill a pad needs before the concrete ever goes down."
        ),
        "sections": [
            (
                "Fill limits on EauGallie and Immokalee soil",
                "<p>Most Sarasota lots sit on EauGallie or Immokalee fine sand, poorly drained flatwoods series with a seasonal high water table within roughly 6 to 18 inches of the surface for part of the year " + src("nrcs-eaugallie-osd") + " " + src("nrcs-immokalee-osd") + ". Florida's residential code caps clean sand or gravel fill under a slab at 24 inches and earth fill at 8 inches unless an engineer signs off on something deeper, and requires at least 4 inches of compacted base under the slab itself. An AC pad or shed slab on a low spot of the lot sometimes needs more fill than that code limit allows without an engineer's approval, which is a conversation worth having before a site visit turns into a surprise on pour day.</p>"
            ),
            (
                "Why original 1970s slabs are usually too small now",
                "<p>Sarasota's median home was built in 1976, and a lot of the original AC pads, carports and utility slabs from that era were sized for equipment that has since gotten larger, a modern heat pump condenser or a boat trailer that didn't fit the household budget decades ago. Adding or replacing a " + svc("concrete-slabs") + " for a current RV, boat or AC unit is as much a resizing project as a repour, and the new slab's footprint gets checked against the lot's impervious coverage cap under Table VI-203 the same as a driveway or patio would " + src("city-sarasota-zoning-vi-203-impervious") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have a 10 × 12 ft slab, 120 sq ft, for a shed on the side yard of a 1970s-built lot with soft, sandy ground",
            "<p>Say you have a 10 × 12 ft slab, 120 sq ft, for a shed on the side yard of a 1970s-built lot with soft, sandy ground. At the market range of " + price("concrete-slab") + " per sq ft, that runs $480 to $1,200, or roughly $720 to $960 in the typical " + price("concrete-slab", typical=True) + " band for a 4-inch slab with a compacted base. Because the side yard sits on EauGallie fine sand with a shallow seasonal water table, the fill under the slab gets checked against the code's 24-inch clean-fill limit before anything is brought in, and the pad's footprint gets added to the lot's existing impervious total rather than priced as if the rest of the lot is empty.</p>"
        ),
        "faqs": [
            faq(
                "Does a shed slab in Sarasota need extra fill because of the soil?",
                "Often, since EauGallie and Immokalee, the common soils here, hold a seasonal water table within 6 to 18 inches of the surface. Florida's residential code caps clean fill at 24 inches without an engineer's sign-off, which we check against before ordering fill."
            ),
            faq(
                "Can I replace an old AC pad with a bigger one in Sarasota?",
                "Yes, and it's common on homes from the 1976 median build year, since newer equipment is often larger than the original unit. The new slab's footprint counts toward the lot's impervious coverage cap the same as any other hardscape."
            ),
            faq(
                "What thickness slab does an RV or boat pad need here?",
                "Residential flatwork is typically 4 inches at 3,000 to 4,000 psi; a pad that will carry a loaded trailer or RV regularly is usually built thicker than that minimum, which we size to the actual load rather than the code floor."
            ),
        ],
        "sources": SRC,
    },
    "concrete-repair": {
        "title": "Concrete Repair in Sarasota, FL – 1976-Era Slabs",
        "meta": "Concrete repair in Sarasota, FL often means a driveway original to a 1976-median-year home; market range is " + price("concrete-repair") + " per " + per("concrete-repair") + ", Oct. 2026.",
        "h1": "Concrete Driveway and Slab Repair in Sarasota",
        "lede": capsule(
            "Concrete repair and resurfacing in Sarasota runs " + price("concrete-repair") + " per " + per("concrete-repair") + " as of October 2026. With a median home built in 1976, "
            "the oldest housing stock in the Sarasota unit, a lot of what we see is an original driveway cracking near its joints or a live oak's root pushing up a slab edge."
        ),
        "sections": [
            (
                "Why so much of Sarasota's driveway stock is overdue",
                "<p>The median year structure was built in Sarasota is 1976, older than any of the other nine towns the Sarasota unit serves, against a 2024 ACS population estimate of 56,970 " + src("acs-sarasota") + ". A driveway poured in the 1970s or 1980s has had five decades of Florida heat cycling and rainy-season saturation to work on its joints and surface, well past the point where patching the same crack twice makes sense over a resurfacing overlay or a tear-out. Resurfacing restores the surface without the cost of a full replacement when the underlying slab hasn't lost structural integrity; " + svc("concrete-repair") + " covers both paths, and a site visit is what tells us which one a given slab needs.</p>"
            ),
            (
                "When a live oak root, not age, is the real cause",
                "<p>Older in-town Sarasota lots carry more mature live oak canopy than the newer subdivisions, and a root growing under a driveway edge lifts and cracks a slab in a pattern that looks a lot like ordinary settlement until someone traces it back to the tree. Before any repair crosses into a protected root zone, the city's rule applies regardless of whether the work is a repair or new construction: root pruning near a tree over 4.5 inches in diameter, or a 24-inch-or-larger Grand Tree, has to be finished and inspected by the city arborist before building-permit inspections proceed " + src("sarasota-tree") + ". We flag that distinction early, since a root-caused crack calls for a different fix than a joint that simply failed on its own.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 20 × 30 ft driveway, 600 sq ft, original to a 1970s Sarasota home, with diagonal cracking near one corner and a nearby oak",
            "<p>Say you have a 20 × 30 ft driveway, 600 sq ft, original to a 1970s Sarasota home, with diagonal cracking near one corner and a nearby oak. At the market range of " + price("concrete-repair") + " per sq ft for resurfacing, that runs $1,800 to $6,000, or roughly $2,400 to $4,200 in the typical " + price("concrete-repair", typical=True) + " band, against a full tear-out and repour at the higher " + price("concrete-driveway") + " per sq ft range for new concrete. Because the cracking sits near where a live oak's canopy shades the corner, the first step is tracing whether a root is the cause before deciding between resurfacing and replacement, since a root-driven crack under a resurfaced overlay will reopen the same way within a season or two.</p>"
        ),
        "faqs": [
            faq(
                "Is my Sarasota driveway's age the reason it's cracking?",
                "It's a common factor. The median home here was built in 1976, and a driveway from that era has had roughly five decades of Florida heat and rainy-season cycling to work on its joints, which is longer than most concrete is expected to go without attention."
            ),
            faq(
                "How do I tell if a tree root is lifting my driveway?",
                "A root-caused crack usually runs parallel to a nearby tree and follows the root's path rather than the slab's control joints. We trace it back before pricing a fix, since a repair over an active root tends to fail again."
            ),
            faq(
                "Is resurfacing or full replacement cheaper for an old Sarasota driveway?",
                "Resurfacing, at " + price("concrete-repair") + " per sq ft, costs less than a full tear-out and repour at " + price("concrete-driveway") + " per sq ft, but only holds up if the underlying slab hasn't lost structural integrity, which a site visit determines."
            ),
        ],
        "sources": SRC,
    },
    "paver-sealing": {
        "title": "Paver Sealing in Sarasota, FL – Salt-Air Upkeep",
        "meta": "Paver sealing in Sarasota, FL runs faster near salt air off the bay and Gulf; market range is " + price("paver-sealing") + " per " + per("paver-sealing") + ", as of October 2026.",
        "h1": "Paver Sealing and Restoration in Sarasota",
        "lede": capsule(
            "Cleaning, re-sanding and sealing pavers in Sarasota runs " + price("paver-sealing") + " per " + per("paver-sealing") + " as of October 2026. Lots within a couple thousand feet of "
            "Sarasota Bay or the Gulf sit in what FDOT classifies as a marine environment, which is part of why sealing comes up sooner there than on an inland lot."
        ),
        "sections": [
            (
                "Why bayfront and island lots need sealer sooner",
                "<p>FDOT draws its own marine-environment line at 2,500 feet from water above 2,000 ppm chloride for bridge design, and a paver surface that close to Sarasota Bay, a bayfront canal, or any of the barrier islands sits in the same salt-heavy air " + src("fdot-sdg") + ". Salt accelerates how fast joint sand washes out and how quickly an unsealed paver surface shows staining, which is why we check how close a lot sits to open water before recommending a resealing interval rather than quoting the same schedule for every address in the unit.</p>"
            ),
            (
                "Maintenance work versus a right-of-way permit",
                "<p>Cleaning, re-sanding with polymeric sand and sealing an existing paver driveway or patio is maintenance, not new construction, and does not trigger the Sec. 29.5-7 permit that a city engineer requires for cutting a curb or building a driveway in the right-of-way " + src("city-sarasota-code-29.5-7-curb-cut-driveway") + ". That line matters on a project that starts as a reseal and grows into a releveling job: if pavers in the right-of-way apron have to come up and be reset rather than just cleaned, the work crosses back into permit territory, which is worth flagging before the scope expands mid-job.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 500 sq ft combined driveway and patio, 7 years unsealed, on a lot a few blocks from Sarasota Bay",
            "<p>Say you have a 500 sq ft combined driveway and patio, 7 years unsealed, on a lot a few blocks from Sarasota Bay. At the market range of " + price("paver-sealing") + " per sq ft for cleaning, re-sanding and sealing, that runs $750 to $1,625, or roughly $875 to $1,375 in the typical " + price("paver-sealing", typical=True) + " band depending on the sealer type and how much joint sand has to be replaced. Given the lot's proximity to open water, a salt-tolerant sealer formulation and a closer eye on the joint sand than an inland job would need are both part of the quote. If any pavers near the street have sunk enough to need releveling rather than just cleaning, that section gets priced separately from the straightforward reseal.</p>"
        ),
        "faqs": [
            faq(
                "Does living near Sarasota Bay mean my pavers need sealing more often?",
                "It can. FDOT treats structures within 2,500 feet of water above 2,000 ppm chloride as a marine environment, and that level of salt exposure tends to wash out joint sand and show staining faster than an inland lot sees."
            ),
            faq(
                "Does resealing an existing paver driveway need a city permit in Sarasota?",
                "No. Cleaning, re-sanding and sealing is maintenance, not the right-of-way construction that Sec. 29.5-7 covers. A full releveling that pulls up pavers in the apron is a different scope and can cross back into permit territory."
            ),
            faq(
                "How often should pavers be resealed in Sarasota?",
                "There's no fixed national interval; an acrylic sealer generally needs recoating after a few years of wear and weather, sooner on a salt-exposed lot near the bay or Gulf than on one farther inland."
            ),
        ],
        "sources": SRC,
    },
    "retaining-walls": {
        "title": "Retaining Walls in Sarasota, FL – Ask Before Height",
        "meta": "Retaining walls in Sarasota, FL have no published city height threshold for engineering; market range is " + price("retaining-wall") + " per " + per("retaining-wall") + ", Oct. 2026.",
        "h1": "Retaining Walls and Seat Walls in Sarasota",
        "lede": capsule(
            "A retaining wall in Sarasota runs " + price("retaining-wall") + " per " + per("retaining-wall") + " of wall face as of October 2026. Unlike Sarasota County's unincorporated areas, "
            "which require engineered drawings above 4 feet, the city sources reviewed set no comparable height threshold, so a call to the Building Division is the first step."
        ),
        "sections": [
            (
                "No published height trigger inside the city limits",
                "<p>Sarasota County's own pool-code amendment requires engineered drawings for any retaining wall over 4 feet tall measured from grade, a rule that applies in the unincorporated county, including Siesta Key and the Sarasota side of Lakewood Ranch. Within the city of Sarasota itself, no equivalent height threshold turned up in the code sections reviewed; the honest answer is to ask the Building Division directly at (941) 263-6494 before assuming a wall under some number is automatically exempt from engineering. A wall holding back fill for a raised planter reads very differently from one retaining a graded slope toward a neighbor's yard, and the office makes that call case by case.</p>"
            ),
            (
                "Fill, flood zones and where the wall sits",
                "<p>A retaining wall on a lot near Sarasota Bay or one of the barrier islands often does double duty, holding fill in place on a parcel that also falls under FEMA's Zone AE or the higher-hazard Zone VE " + src("fema-coastal-firm") + ". Where the wall sits relative to Florida's Coastal Construction Control Line matters too; any construction or excavation seaward of that line needs its own DEP permit before a local one is relevant " + src("fdep-cccl-program") + ". A seat wall framing a paver patio on a mainland lot away from the water is a much simpler case, but we still check the fill depth against Florida's code limits for sand and earth fill under any adjoining slab before pricing the combined project.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 30 ft long, 2 ft tall seat wall, about 60 sq ft of wall face, framing a raised paver patio on a sloped backyard",
            "<p>Say you have a 30 ft long, 2 ft tall seat wall, about 60 sq ft of wall face, framing a raised paver patio on a sloped backyard. At the market range of " + price("retaining-wall") + " per sq ft of wall face, that runs $900 to $2,400, or roughly $1,200 to $2,100 in the typical " + price("retaining-wall", typical=True) + " band for segmental block with drainage behind it. At 2 feet, the wall sits well under the county's 4-foot engineering trigger that would apply on an unincorporated lot nearby, but since the city hasn't published a comparable threshold of its own, we confirm the scope with the Building Division before design rather than assume the county's number carries over.</p>"
        ),
        "faqs": [
            faq(
                "At what height does a Sarasota retaining wall need an engineer?",
                "No height threshold turned up in the city code sections reviewed, unlike the unincorporated county's 4-foot rule. We call the Building Division at (941) 263-6494 to confirm before assuming a wall is exempt from engineering."
            ),
            faq(
                "Does a retaining wall near Sarasota Bay need a state permit?",
                "If it sits seaward of Florida's Coastal Construction Control Line, yes, a DEP permit is required regardless of the wall's height, on top of whatever the city's own review calls for."
            ),
            faq(
                "Can a retaining wall help with drainage on a flatwoods lot?",
                "It can manage grade changes and hold fill in place, but it isn't a substitute for proper swale and drain planning on a lot with a shallow seasonal water table; we treat the two as separate parts of the design."
            ),
        ],
        "sources": SRC,
    },
    "artificial-turf": {
        "title": "Artificial Turf in Sarasota, FL – DEP Rule & Water",
        "meta": "Artificial turf in Sarasota, FL follows DEP Rule 62-308.100 and sidesteps SWFWMD's Phase III order; market range is " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
        "h1": "Artificial Turf Installation in Sarasota",
        "lede": capsule(
            "Artificial turf in Sarasota runs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October 2026. It sits outside the city's current once-a-week watering order once installed, "
            "and the state's own turf rule steers installation around protected tree root zones the same way the city's arborist process already does."
        ),
        "sections": [
            (
                "How the state turf rule and the city's tree rule line up",
                "<p>Florida Administrative Code Rule 62-308.100, effective May 19, 2026, sets the statewide installation standard for synthetic turf: natural infill, a washed base, a 10-foot setback from any waterbody without a seawall, no in-ground irrigation beneath it, and turf kept clear of a tree's canopy edge unless a licensed arborist approves a closer install " + src("dep-rule") + ". That last piece lines up with a rule Sarasota already runs on its own: root pruning near a protected tree has to be finished and inspected by the city arborist before building-permit inspections proceed, and a Grand Tree, a live oak 24 inches across or wider, carries its own 20-foot barricade distance " + src("sarasota-tree") + ". On a lot with mature canopy, one arborist visit tends to cover both requirements rather than two separate approvals.</p>"
            ),
            (
                "Watering restrictions turf doesn't have to live with",
                "<p>Lawn irrigation in Sarasota is down to one watering day a week, assigned by address, under SWFWMD's Modified Phase III shortage order, a schedule the city confirmed runs through March 2027 " + src("swfwmd-restrictions") + " " + src("sarasota-city-phase3") + ". A sod lawn has to live inside that calendar until it lifts; turf, once installed and rinsed in, needs no irrigation afterward at all. The law's protection for turf against an HOA has a limit, too: under F.S. §720.3045, it only shields turf hidden from the street and from neighboring lots, nothing visible from either, so a front-yard install in a deed-restricted community is worth checking against the association's own rules first.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 400 sq ft side yard, currently struggling sod under a live oak canopy, going to artificial turf for a dog run",
            "<p>Say you have a 400 sq ft side yard, currently struggling sod under a live oak canopy, going to artificial turf for a dog run. At the market range of " + price("artificial-turf") + " per sq ft, that runs $4,000 to $10,000, or roughly $4,800 to $7,200 in the typical " + price("artificial-turf", typical=True) + " band for a washed-rock base and pet-rated infill. Because the yard sits under the oak's drip line, DEP Rule 62-308.100 calls for an arborist's sign-off before installation, the same inspection the city's own root-pruning rule would require if the project disturbed the tree's roots instead. Once installed, the turf comes off SWFWMD's once-a-week watering schedule entirely, which is most of the appeal on a shaded side yard where sod was already struggling under the canopy.</p>"
        ),
        "faqs": [
            faq(
                "Does artificial turf under a live oak in Sarasota need special approval?",
                "Yes. State Rule 62-308.100 keeps turf off a tree's canopy edge unless a licensed arborist signs off on a closer layout, which lines up with the city's own root-pruning and arborist-inspection rule for work near protected trees."
            ),
            faq(
                "Can my Sarasota HOA ban artificial turf in the front yard?",
                "Only partly. F.S. §720.3045 shields turf an HOA can't see from the street or from a neighboring lot; anything visible from either still depends on that association's own design rules."
            ),
            faq(
                "Does turf help with Sarasota's current watering restrictions?",
                "Once installed, yes. SWFWMD's current shortage order holds sod to one watering day a week into 2027, and turf, once it's watered in during installation, is free of that calendar for good."
            ),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
