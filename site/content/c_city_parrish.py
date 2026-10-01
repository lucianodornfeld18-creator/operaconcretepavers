# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, svc, city, cs, post, compare, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "parrish"

SRC = [
    "manatee-ldc-1004.2-access-drainage-permit",
    "manatee-driveway-culvert-service",
    "manatee-driveway-application",
    "manatee-paver-driveway-inspections",
    "manatee-no-permit-list",
    "manatee-ldc-511.16-pool-decks",
    "manatee-phase3",
    "swfwmd-restrictions",
    "fema-msc",
    "nrcs-myakka-osd",
    "nrcs-eaugallie-osd",
    "nrcs-felda-osd",
    "dep-rule",
    "fs125572",
    "fs720-3045",
    ("Census Reporter, Parrish CCD, Manatee County FL (ACS 2020-2024 5-yr, B01003/B25035)", "https://censusreporter.org/profiles/06000US1208192652-parrish-ccd-manatee-county-fl/"),
    ("Wikipedia, Fort Hamer Bridge", "https://en.wikipedia.org/wiki/Fort_Hamer_Bridge"),
    ("USGS Water Data, Gamble Creek at County Road 675 near Parrish FL (Station 02300017)", "https://waterdata.usgs.gov/monitoring-location/USGS-02300017/"),
    ("USF Water Atlas, Gamble Creek", "https://manatee.wateratlas.usf.edu/waterbodies/rivers/21004/gamble-creek"),
    ("Your Observer, Big projects to keep an eye on in Parrish", "https://www.yourobserver.com/news/2025/feb/18/big-projects-parrish/"),
]

HUB = page(
    "/parrish-fl/", "city",
    "Concrete & Paver Contractor in Parrish, FL",
    "Opera pours concrete and sets pavers for Parrish, FL homes, where Manatee County's access and drainage permit covers the apron, even on a new build.",
    "Concrete, Pavers and Turf for Parrish Homes",
    capsule(
        "Parrish sits about 18 miles north of the Sarasota unit's base along the Manatee River, unincorporated ground that's still filling in lot by lot with new subdivisions. "
        "As of October 2026, Opera builds driveways, patios, pool decks and turf for that growing mix of brand-new and established homes, with Manatee County standing in for a city hall on every permit question."
    ),
    "".join([
        sec(
            "Who reviews a driveway or apron in Parrish, since there's no city office?",
            "<p>Parrish was never incorporated, so a county office, not a town hall, decides whether a driveway apron can be poured or widened. Manatee County LDC Sec. 1004.2.A bars any part of a driveway reaching from the property line to the roadway pavement from being \"constructed, improved, or enlarged without an access and drainage permit\" "
            + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC Sec. 1004.2") + ", language broad enough to cover a builder pouring the first driveway on a new lot and a longtime owner adding a parking pad years later under the same rule. Public Works' Infrastructure Engineering Division handles the review, with the application filed in Accela under Building, Public Works, Driveway/Culvert and county staff at 311 fielding scheduling questions on weekdays " + src("manatee-driveway-culvert-service", "Manatee driveway/culvert permit service") + ". " + post("manatee-county-driveway-permits", "Our Manatee County permit guide") + " walks through how the same process plays out in Ellenton and Palmetto.</p>"
        ),
        sec(
            "Does a brand-new Parrish driveway skip the county's permit?",
            "<p>No. Even on a lot where the builder poured the original driveway as part of the home's construction, the county's access and drainage permit rule doesn't carve out an exception for new construction, and a homeowner who later wants a wider apron, a second parking pad or a paver overlay still has to file for the same Driveway/Culvert permit a decades-old lot would need "
            + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC Sec. 1004.2") + ". Residential applications and the county's own spec sheet for width, thickness and curb treatment go through Building & Development Services at 1112 Manatee Ave W " + src("manatee-driveway-application", "Manatee driveway and culvert application") + ", while a non-structural patio stays off that list entirely under the county's current no-permit guidance " + src("manatee-no-permit-list", "Manatee no-permit list") + ".</p>"
        ),
        sec(
            "What's driving all the new construction around Parrish?",
            "<p>Fort Hamer Bridge, a 2,318-foot span that opened October 18, 2017, carries Fort Hamer Road across the Manatee River to link Parrish directly with the Lakewood Ranch side of East County " + ext("https://en.wikipedia.org/wiki/Fort_Hamer_Bridge", "Wikipedia, Fort Hamer Bridge") + ", shortening what used to be a longer drive around to US 301 or I-75. That new crossing sits near two of the area's largest active subdivisions: North River Ranch, approved for roughly 5,000 to 6,000 homes on 2,600 acres near Fort Hamer Road and Moccasin Wallow Road, and Seaire, planned for about 3,000 homes east of I-75 on Moccasin Wallow Road, where the first residents moved in during late 2024 " + ext("https://www.yourobserver.com/news/2025/feb/18/big-projects-parrish/", "Your Observer, Big projects to keep an eye on in Parrish") + ". Both are still building out lot by lot, which is why so much of the driveway, patio and pool-deck work here is a first installation rather than a replacement.</p>"
        ),
        sec(
            "What does Gamble Creek mean for drainage on a Parrish lot?",
            "<p>Gamble Creek, a tributary that empties into the Manatee River, runs through the middle of the Parrish area; the U.S. Geological Survey's own gauge near County Road 675 lists a 14-square-mile drainage basin feeding that stretch of the creek "
            + ext("https://waterdata.usgs.gov/monitoring-location/USGS-02300017/", "USGS, Gamble Creek near Parrish") + ", and the creek itself runs about 22.4 miles before reaching the river " + ext("https://manatee.wateratlas.usf.edu/waterbodies/rivers/21004/gamble-creek", "USF Water Atlas, Gamble Creek") + ". Florida's own state soil, Myakka fine sand, is one of the series most often mapped across this stretch of Manatee County, and it sits saturated to within roughly a foot and a half of grade for a stretch of most years " + src("nrcs-myakka-osd", "NRCS Myakka soil series") + ", a fact that drives the base depth on a lot near that drainage network no matter how recently the subdivision around it was platted.</p>"
        ),
        sec(
            "Does a pool deck or patio need its own setback in Parrish?",
            "<p>Manatee County's code sets a single distance for a pool, screen cage or an on-grade deck built in a side or rear yard: 5 feet from the lot line or the shoreline, whichever applies, and that same section says none of those features count as a yard encroachment at that distance "
            + src("manatee-ldc-511.16-pool-decks", "Manatee LDC Sec. 511.16") + ". On a new-construction lot backing to a retention pond or a conservation buffer, a common layout inside Parrish's larger master-planned subdivisions, that setback still runs from the actual rear lot line rather than from the pond's edge, so a survey is worth pulling before a deck extension gets staked out.</p>"
        ),
        sec(
            "How new is the typical Parrish home, and what does the growth look like on paper?",
            "<p>The Census Bureau's current five-year estimate for the Parrish CCD area puts the population at 43,855 and the median year a home here was built at 2011, newer than every other Manatee community in this unit "
            + ext("https://censusreporter.org/profiles/06000US1208192652-parrish-ccd-manatee-county-fl/", "Census Reporter, Parrish CCD") + ". That skew toward recent construction is why so much of the hardscape work coming out of Parrish right now is a first pour or a builder-grade upgrade rather than a tear-out of failing 1990s concrete, a pattern this page's FAQ below gets into directly.</p>"
        ),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq(
            "Does Parrish have its own building department?",
            "No, there isn't a Parrish town hall to call. A brand-new driveway on a North River Ranch lot and a pool deck addition on a decades-old parcel both get reviewed by the same two county offices, Development Services and Public Works, since the community has never incorporated."
        ),
        faq(
            "Do you serve new-construction homes in Parrish and North Port?",
            "Yes. In Parrish, that often means extending a builder's driveway apron, adding a pool deck or lanai extension behind a home that closed with only the standard package, or swapping a slab for pavers before the landscaping goes in, all of which still route through Manatee County's access and drainage permit the same as an older lot would. North Port's new-construction work runs through a different, city-issued process, covered on " + city("north-port", "our North Port page") + "."
        ),
        faq(
            "Does Gamble Creek's drainage basin affect where I can build in Parrish?",
            "It can on lots close to the creek or the Manatee River, where the water table tends to sit closer to the surface. The USGS gauge near County Road 675 tracks a 14-square-mile basin feeding that stretch, a detail that shapes how deep a driveway or pool deck's compacted base needs to run rather than whether the permit itself is required."
        ),
        faq(
            "Is a patio exempt from a permit on a new Parrish lot the same as an older one?",
            "Yes. The county's no-permit list treats a non-structural concrete or paver patio the same way regardless of when the subdivision around it was built; a slab poured with footers or tied into a pool still needs a permit filed first."
        ),
        faq(
            "How do you pick the best concrete contractor for a Parrish project?",
            "Start with the state's license-lookup tool, then ask two Parrish-specific questions: has this crew filed Manatee County's access and drainage permit before, and does the proposal spell out a base thickness sized for Myakka or similar wet flatwoods ground rather than a one-size answer. " + post("how-to-choose-a-concrete-contractor-sarasota", "Our contractor guide") + " covers the rest."
        ),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Parrish",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/manatee-county-driveway-permits/", "Driveway and patio permits in Bradenton, Lakewood Ranch, Parrish and Palmetto"),
        ("/lakewood-ranch-fl/", "Concrete, pavers and turf in Lakewood Ranch"),
        ("/ellenton-fl/", "Concrete, pavers and turf in Ellenton"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Parrish, FL",
)

LOCAL = {
    "concrete-driveways": {
        "title": "Concrete Driveways in Parrish, FL – New Construction",
        "meta": "Concrete driveways in Parrish, FL, new or added-to, need a Manatee County access and drainage permit; market range is " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
        "h1": "Concrete Driveway Installation in Parrish",
        "lede": capsule(
            "Pricing out a new or widened driveway in Parrish, expect " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", the same market range as of October 2026 whether the lot sits inside a subdivision still under construction or on an older platted parcel. "
            "Either way, Manatee County's access and drainage permit has to close out before the old concrete comes up or the new pour goes down."
        ),
        "sections": [
            (
                "A first driveway and a later one follow the same rule",
                "<p>LDC Sec. 1004.2.A doesn't distinguish between a builder's original driveway and an owner's later change; both fall under the county's access and drainage permit before any part of the apron can be built, improved or enlarged "
                + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC Sec. 1004.2") + ". Inside a large, still-building subdivision like North River Ranch, that means a homeowner who wants a wider pad for a second vehicle files the same Driveway/Culvert application in Accela that the original builder used, routed through Public Works' Infrastructure Engineering Division " + src("manatee-driveway-culvert-service", "Manatee driveway/culvert permit service") + ".</p>"
            ),
            (
                "Reading the ground near Gamble Creek before the base goes in",
                "<p>Quite a few Parrish lots sit inside the roughly 14-square-mile basin that feeds Gamble Creek near the USGS gauge at County Road 675 "
                + ext("https://waterdata.usgs.gov/monitoring-location/USGS-02300017/", "USGS, Gamble Creek near Parrish") + ", ground mapped to Myakka fine sand, a series NRCS lists as saturated close to the surface for a stretch of most years " + src("nrcs-myakka-osd", "NRCS Myakka soil series") + ". The Florida Building Code limits how much sand or gravel fill can go under a slab (24 inches) and ordinary earth fill (8 inches) without engineering sign-off, on top of a 4-inch compacted base that's required either way; a driveway sized for a boat trailer rather than a sedan is where that creek-fed water table ends up mattering, more than the project's square footage ever does.</p>"
            ),
        ],
        "scenario": (
            "Say a new three-car-garage driveway inside a Parrish subdivision like North River Ranch measures 24 x 40 ft, 960 sq ft total",
            "<p>Say a new three-car-garage driveway inside a Parrish subdivision like North River Ranch measures 24 x 40 ft, 960 sq ft total. At " + price("concrete-driveway") + " per sq ft, that spans $5,760 to $14,400 across the full range, tightening to roughly $7,680 to $11,520 inside the typical " + price("concrete-driveway", typical=True) + " band. The access and drainage permit still has to be filed and closed out before the pour, the same step a builder would have taken on the lot next door, and the base gets checked against the local water table rather than assumed safe just because the subdivision itself is new.</p>"
        ),
        "faqs": [
            faq(
                "Does a brand-new Parrish home still need a driveway permit?",
                "Yes. Manatee County's access and drainage permit covers a builder's first driveway on a new lot the same way it covers a change made years later; there's no new-construction exemption in the county's rule."
            ),
            faq(
                "Who handles the driveway permit for a Parrish address?",
                "Manatee County's Public Works Infrastructure Engineering Division, filed in Accela under Building, Public Works, Driveway/Culvert, since Parrish has no city building department of its own."
            ),
            faq(
                "Does Parrish's soil change how deep a driveway base goes?",
                "Often, especially inside the Gamble Creek drainage basin. Myakka, the dominant soil there, sits saturated to within a foot and a half of grade for part of most years, which is the number that drives the fill plan on a driveway built for heavier loads, not the lot's size."
            ),
        ],
        "sources": SRC,
    },
    "paver-driveways": {
        "title": "Paver Driveways in Parrish, FL – Motor Courts",
        "meta": "Paver driveways in Parrish, FL follow Manatee County's paver inspection spec on new and existing lots; market range is " + price("paver-driveway") + " per " + per("paver-driveway") + ".",
        "h1": "Paver Driveway Installation in Parrish",
        "lede": capsule(
            "Budget " + price("paver-driveway") + " per " + per("paver-driveway") + " for a paver driveway in Parrish as of October 2026, the figure holding steady whether it's the builder's first install on a new lot or a motor-court upgrade on an established one. "
            "Three-car-garage floor plans are common enough in the area's newer subdivisions that the county's widest-allowed apron comes up often, not just as a rare exception."
        ),
        "sections": [
            (
                "Reading the county's paver spec on a newer floor plan",
                "<p>North River Ranch and Seaire both sell plenty of three-car-garage layouts, and the county's own paver driveway guidance lets that style of home build out to 30 feet of apron width at the street, wider than the standard 12-to-24-foot range it sets for everything else, as long as the compacted sub-base and the paver together still land at a 6-inch grade cut "
                + src("manatee-paver-driveway-inspections", "Manatee paver driveway inspections") + ". A crew pricing a new-build job checks the garage configuration against that spec before assuming the standard width applies.</p>"
            ),
            (
                "Compacting over wetter ground near the creek",
                "<p>EauGallie soil, mapped across parts of the Parrish area, keeps a water table within about 18 inches of the surface for one to four months most years, while Felda runs wetter still, staying within roughly a foot of grade for two to six months "
                + src("nrcs-eaugallie-osd", "NRCS EauGallie soil series") + " " + src("nrcs-felda-osd", "NRCS Felda soil series") + ". ICPI calls for 2 to 4 extra inches of compacted aggregate on ground that wet compared with a free-draining lot, a distinction worth confirming before the base order goes in on a new paver drive rather than guessed from the model home next door.</p>"
            ),
        ],
        "scenario": (
            "Say a circular paver motor court on a Parrish new-build lot adds 20 x 45 ft of surface, 900 sq ft",
            "<p>Say a circular paver motor court on a Parrish new-build lot adds 20 x 45 ft of surface, 900 sq ft. At " + price("paver-driveway") + " per sq ft, figure $9,000 to $27,000 across the full range, narrowing to about $10,800 to $18,000 inside the typical " + price("paver-driveway", typical=True) + " band depending on paver thickness and pattern. Because the addition sits past the garage apron the builder originally poured, it still needs its own access and drainage permit filed before work starts, and the grade cut gets checked the same way a standalone driveway's would, whether the base soil underneath leans toward Myakka, EauGallie or Felda.</p>"
        ),
        "faqs": [
            faq(
                "How wide can a three-car-garage paver driveway be in Parrish?",
                "The county's paver driveway spec allows up to 30 feet of width at the street for that garage configuration specifically, well past the 12-to-24-foot range that governs a one- or two-car driveway."
            ),
            faq(
                "Does a paver motor-court addition need its own permit in Parrish?",
                "Yes. Adding motor-court paving past a builder's original apron is still an enlargement under the county's access and drainage permit rule, filed the same way a brand-new driveway application would be."
            ),
            faq(
                "Why does base depth vary so much across Parrish paver jobs?",
                "The soil underneath varies. EauGallie and Felda both hold groundwater within about 18 inches of the surface for part of the year, calling for 2 to 4 inches more compacted base than a better-drained lot would need."
            ),
        ],
        "sources": SRC,
    },
    "concrete-patios": {
        "title": "Concrete Patios in Parrish, FL – No-Permit List",
        "meta": "Non-structural concrete patios in Parrish, FL skip a Manatee County permit on new and older lots alike; market range is " + price("concrete-patio") + " per " + per("concrete-patio") + ".",
        "h1": "Concrete Patio Installation in Parrish",
        "lede": capsule(
            "A concrete patio in Parrish runs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. "
            "A simple slab added behind a brand-new home follows the county's same non-structural exemption as a patio poured on a parcel that predates the newer subdivisions around it."
        ),
        "sections": [
            (
                "Reading the county's no-permit list on a new lot",
                "<p>Manatee County's current no-permit guidance names a \"non-structural concrete/paver patio\" directly as work that skips a building permit, while a \"concrete slab with footers\" sits on the opposite side of the list and does need one "
                + src("manatee-no-permit-list", "Manatee no-permit list") + ". That split doesn't care whether the home behind the patio closed last year or thirty years ago; a freestanding slab poured on grade, not tied structurally into the house, is the detail that matters, and Development Services at 941-748-4501 ext. 3800 sorts out a borderline case either way.</p>"
            ),
            (
                "Grading a patio around a new subdivision's stormwater layout",
                "<p>Many of Parrish's newer master-planned sections, including North River Ranch and Seaire, are built around retention ponds and conservation buffers as part of the overall stormwater design, so a patio addition on one of those lots often has a rear-yard grading plan already set by the original site plan rather than a blank slate. Felda soil, common in low spots across the area, keeps a water table within about a foot of grade for part of the year " + src("nrcs-felda-osd", "NRCS Felda soil series") + ", which still shapes slope and perimeter drainage even on a lot built within the last few years.</p>"
            ),
        ],
        "scenario": (
            "Say a 14 x 20 ft lanai patio addition behind a recently built Parrish home comes to 280 sq ft",
            "<p>Say a 14 x 20 ft lanai patio addition behind a recently built Parrish home comes to 280 sq ft. At " + price("concrete-patio") + " per sq ft, that comes to $1,680 to $3,640 across the full range, narrowing to about $1,960 to $2,800 inside the typical " + price("concrete-patio", typical=True) + " band for a broom finish. Because the slab is freestanding and poured on grade, it lands on the county's no-permit list the same way an identical patio would on a decades-older lot, though the rear-yard grading still gets checked against whatever retention pond or buffer the subdivision's original site plan set up.</p>"
        ),
        "faqs": [
            faq(
                "Does a patio on a new Parrish home need a permit?",
                "Not if it's a freestanding, non-structural slab poured on grade; the county's no-permit list treats that the same way regardless of how recently the home was built. A slab with footers, or one tied into the house, needs a permit."
            ),
            faq(
                "Does a new subdivision's retention pond affect where I can put a patio?",
                "It can shape the rear-yard grading and slope, since many newer Parrish sections route stormwater to ponds and buffers as part of the original site plan, even though it doesn't change whether the patio itself needs a permit."
            ),
            faq(
                "Who do I call to confirm a patio permit question in Parrish?",
                "Manatee County Development Services, at 941-748-4501 ext. 3800, settles a borderline case before pricing or scheduling the pour."
            ),
        ],
        "sources": SRC,
    },
    "paver-patios": {
        "title": "Paver Patios in Parrish, FL – 2011 Median Build Year",
        "meta": "Paver patios in Parrish, FL sit on housing built around 2011 on average, the newest stock in the Manatee unit; market range is " + price("paver-patio") + " per " + per("paver-patio") + ".",
        "h1": "Paver Patios and Walkways in Parrish",
        "lede": capsule(
            "Paver patio pricing in Parrish lands at " + price("paver-patio") + " per " + per("paver-patio") + ", a market range that held through October 2026. "
            "Most of the lots behind that number are recent builds, so a paver patio job here usually starts from a modern footprint rather than untangling decades of prior additions."
        ),
        "sections": [
            (
                "Building on a newer lot's clean grading",
                "<p>Census Reporter's current five-year estimate puts the median year a Parrish-area home was built at 2011, newer than Palmetto, Bradenton or Ellenton across the river "
                + ext("https://censusreporter.org/profiles/06000US1208192652-parrish-ccd-manatee-county-fl/", "Census Reporter, Parrish CCD") + ". A paver patio project on that recent a build usually ties into a lanai or pool cage threshold set during original construction rather than an older addition poured a decade after the house went up, which tends to simplify how the new surface's elevation is matched.</p>"
            ),
            (
                "Fort Hamer Bridge and why that matters for scheduling",
                "<p>Fort Hamer Bridge's 2017 opening gave Parrish a direct link across the Manatee River to the Lakewood Ranch side of East County " + ext("https://en.wikipedia.org/wiki/Fort_Hamer_Bridge", "Wikipedia, Fort Hamer Bridge") + ", shortening material and crew travel time for jobs on the Fort Hamer Road corridor compared with routing around through US 301. That shorter run is less about the permit itself, which still follows the same county access and drainage rule for any portion touching the right-of-way, and more about keeping a multi-day paver job on schedule.</p>"
            ),
        ],
        "scenario": (
            "Say an 18 x 24 ft paver patio backing up to a retention pond on a Parrish lot comes to 432 sq ft",
            "<p>Say an 18 x 24 ft paver patio backing up to a retention pond on a Parrish lot comes to 432 sq ft. At " + price("paver-patio") + " per sq ft, that runs $4,320 to $7,344 across the full range, tightening to about $5,184 to $6,912 inside the typical " + price("paver-patio", typical=True) + " band, with the spread mostly tracking paver grade. Since the lot's grading dates to the 2010s or later, the slope running toward the pond usually follows the plan the subdivision's engineer already set, sparing the crew a fresh drainage study that an older, re-graded Manatee County lot might need first.</p>"
        ),
        "faqs": [
            faq(
                "Is Parrish's housing newer than nearby Manatee communities?",
                "It runs newer on paper: the ACS five-year figure for the Parrish area lands at 2011, well ahead of Palmetto, Bradenton or Ellenton, so a paver patio crew here is usually working around fewer original-era quirks than those other towns present."
            ),
            faq(
                "Does a paver patio near a retention pond need special review in Parrish?",
                "The pond itself is usually part of the subdivision's original stormwater design rather than a separate review trigger; the patio still follows the same county no-permit rule for non-structural work, with the setback measured from the actual rear lot line."
            ),
            faq(
                "Does the Fort Hamer Bridge affect paver patio pricing in Parrish?",
                "No, prices don't change by location within the market area. The bridge mainly affects how quickly a crew and materials can reach a Fort Hamer Road corridor job from the East County side."
            ),
        ],
        "sources": SRC,
    },
    "concrete-pool-decks": {
        "title": "Concrete Pool Decks in Parrish, FL – 5-Ft Setback",
        "meta": "Concrete pool decks in Parrish, FL clear Manatee LDC 511.16's 5-foot setback whether the lot is new or established; market range is " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ".",
        "h1": "Concrete Pool Deck Installation in Parrish",
        "lede": capsule(
            "Figure " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " for a concrete pool deck in Parrish, the market range as of October 2026. "
            "Stretching a deck past the cage a builder installed is one of the most common add-ons here, and the county measures its own setback the same way whether that cage is five years old or thirty."
        ),
        "sections": [
            (
                "Why a builder's pool cage isn't the last word on deck size",
                "<p>Manatee County's code doesn't treat a pool, a screen enclosure or an on-grade deck as encroaching on a side or rear yard as long as the edge stays 5 feet clear of the lot line or the shoreline "
                + src("manatee-ldc-511.16-pool-decks", "Manatee LDC Sec. 511.16") + ". That 5-foot figure is measured from the surveyed property line itself, so on a Parrish lot backing to a retention pond or a conservation buffer, the pond's edge doesn't move the number closer, a detail worth confirming with a survey before an owner assumes the deck can stretch all the way to the water view.</p>"
            ),
            (
                "Checking the subgrade, not just the setback",
                "<p>EauGallie and Felda, both mapped across parts of the Parrish area, carry a water table inside roughly 18 inches of grade for one to four months most years "
                + src("nrcs-eaugallie-osd", "NRCS EauGallie soil series") + " " + src("nrcs-felda-osd", "NRCS Felda soil series") + ", which is the kind of ground that catches an owner off guard on a lot where the house itself is only a few years old but the backyard still sits on unimproved native soil past the original slab's footprint.</p>"
            ),
        ],
        "scenario": (
            "Say a Parrish homeowner extends a builder-installed screen cage by 600 sq ft of new pool deck",
            "<p>Say a Parrish homeowner extends a builder-installed screen cage by 600 sq ft of new pool deck. At " + price("concrete-pool-deck") + " per sq ft, that spans $3,000 to $9,000 across the full range, tightening to roughly $4,200 to $7,200 inside the typical " + price("concrete-pool-deck", typical=True) + " band, with a cool-touch textured coating pushing toward the top of that band over a plain broom finish. A survey confirms the extension's new edge still clears the 5-foot line before the forms go up, and the crew tests the native soil past the original slab rather than assuming it compacts the same as the engineered pad the builder graded under the house.</p>"
        ),
        "faqs": [
            faq(
                "Can I extend a builder-installed pool deck in Parrish right up to a retention pond?",
                "No. The required 5-foot clearance runs from the surveyed rear property line, not from the pond's edge, so a deck extension still has to stop short of the line even on a lot that backs to open water."
            ),
            faq(
                "Does extending an existing pool deck in Parrish need a new permit?",
                "Yes. Enlarging a deck already attached to a builder-installed cage still goes through the same county review as a standalone pool deck project."
            ),
            faq(
                "Why would a newer Parrish home still have drainage issues in the backyard?",
                "Because the engineered pad under the house and driveway doesn't necessarily extend into the rest of the yard. EauGallie and Felda soil, both common in the area, can hold water close to the surface on that untouched native ground even behind a recently built house."
            ),
        ],
        "sources": SRC,
    },
    "pool-deck-pavers": {
        "title": "Pool Deck Pavers in Parrish, FL – Overlay Option",
        "meta": "Pool deck pavers in Parrish, FL often go in as a paver overlay on a builder's original concrete deck; market range is " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ".",
        "h1": "Travertine and Paver Pool Decks in Parrish",
        "lede": capsule(
            "Pool deck pavers or travertine in Parrish run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. "
            "Because so many pools here came with the house as a builder package, a paver or travertine overlay on the existing broom-finished deck is a common upgrade rather than a first installation."
        ),
        "sections": [
            (
                "Overlaying rather than starting from bare ground",
                "<p>With the median Parrish-area home dated to around 2011 " + ext("https://censusreporter.org/profiles/06000US1208192652-parrish-ccd-manatee-county-fl/", "Census Reporter, Parrish CCD") + ", a large share of the pools in the community's newer subdivisions came with a standard broom-finished concrete deck already in place. A paver or travertine overlay on top of that existing slab is a non-structural resurfacing job on the county's own terms the way a fresh patio pour is, which keeps the permit question the same as it would be for any other non-structural hardscape " + src("manatee-no-permit-list", "Manatee no-permit list") + ".</p>"
            ),
            (
                "The base underneath still matters",
                "<p>EauGallie soil, mapped across parts of the Parrish area, keeps a water table within about 18 inches of grade for one to four months most years "
                + src("nrcs-eaugallie-osd", "NRCS EauGallie soil series") + ", which is worth checking before an overlay goes down, since an uneven or soft base underneath an existing deck can undercut a new paver surface even when the project itself is cosmetic rather than structural.</p>"
            ),
        ],
        "scenario": (
            "Say a 500 sq ft travertine overlay goes over an existing builder-installed pool deck on a Parrish lot",
            "<p>Say a 500 sq ft travertine overlay goes over an existing builder-installed pool deck on a Parrish lot. At " + price("pool-deck-pavers") + " per sq ft, figure $6,000 to $15,000 across the full range, narrowing to about $7,000 to $11,000 inside the typical " + price("pool-deck-pavers", typical=True) + " band depending on stone grade and pattern. Before the overlay goes down, the crew checks the existing slab's grade and drainage toward the pool, since a builder's original deck was designed for a broom finish, not necessarily for the slightly different thickness and joint pattern a stone overlay adds.</p>"
        ),
        "faqs": [
            faq(
                "Can pavers go over an existing concrete pool deck in Parrish?",
                "Yes, as an overlay, which is common here given how many pools came with the house as a builder package. The existing slab's grade and drainage toward the pool get checked first."
            ),
            faq(
                "Does a pool deck overlay need a Manatee County permit?",
                "A non-structural resurfacing job generally doesn't, under the same no-permit guidance that covers a non-structural patio, though a borderline case is worth confirming with Development Services first."
            ),
            faq(
                "Does the soil under a Parrish pool deck affect an overlay?",
                "It can. EauGallie soil, common in the area, holds a seasonal high water table that can soften the base under an older deck, which is worth checking before adding a stone surface on top."
            ),
        ],
        "sources": SRC,
    },
    "stamped-concrete": {
        "title": "Stamped Concrete in Parrish, FL – Entry Accents",
        "meta": "Stamped concrete in Parrish, FL dresses up entries and walkways in both new and established subdivisions; market range is " + price("stamped-concrete") + " per " + per("stamped-concrete") + ".",
        "h1": "Stamped Concrete Driveways and Patios in Parrish",
        "lede": capsule(
            "Expect to pay " + price("stamped-concrete") + " per " + per("stamped-concrete") + " for stamped concrete in Parrish, a figure that hasn't moved as of October 2026. "
            "Once the sod and landscaping go in behind a new build, an entry walk or porch accent in a pattern is a frequent next step, and it answers to the same permit rules as a plain slab."
        ),
        "sections": [
            (
                "A decorative finish doesn't change the permit path",
                "<p>Stamping and coloring a slab doesn't move the work out from under the county's access and drainage permit if any part of it touches the right-of-way at the street, and it doesn't add a permit requirement to a freestanding walk that stays on the no-permit list either "
                + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC Sec. 1004.2") + " " + src("manatee-no-permit-list", "Manatee no-permit list") + ". A homeowner finishing out a new-build front yard with a stamped walk follows the exact same rule a decades-older Parrish lot getting the same upgrade would.</p>"
            ),
            (
                "Matching a palette the builder already set",
                "<p>Many of Parrish's newer subdivisions sell homes with a defined exterior color scheme chosen at closing, so a stamped accent added afterward often has to work with trim and roof colors already fixed rather than a totally open palette. That's a design conversation between homeowner and crew rather than a published code requirement, and it's worth settling before integral color or a release agent gets ordered.</p>"
            ),
        ],
        "scenario": (
            "Say a 320 sq ft stamped entry walk and small porch extension goes in on a newer Parrish lot",
            "<p>Say a 320 sq ft stamped entry walk and small porch extension goes in on a newer Parrish lot. The job runs $2,560 to $6,080 at " + price("stamped-concrete") + " per sq ft across the full range, settling closer to $3,840 to $5,120 once the typical " + price("stamped-concrete", typical=True) + " band is applied. Set back on private ground away from the street, the walk never touches the county's permit requirements at all, leaving the only real planning step as matching the integral color to whatever exterior scheme the builder already fixed on the house.</p>"
        ),
        "faqs": [
            faq(
                "Does a stamped pattern change which Manatee County permit applies in Parrish?",
                "No, the finish is cosmetic as far as the county is concerned. A stamped apron crossing the right-of-way still needs the access and drainage permit, and a stamped walk set back on private ground stays on the no-permit list the same as a plain one would."
            ),
            faq(
                "Do Parrish's HOAs set an approved color list for stamped concrete?",
                "None is published for this to cite directly; the practical move is matching a stamped addition to whatever exterior scheme the builder already fixed at closing rather than assuming an open palette."
            ),
            faq(
                "Why does stamped concrete cost more than a plain driveway pour in Parrish?",
                "The integral color, release agent and hand-texturing add labor a broom finish skips, which is why stamped work runs " + price("stamped-concrete") + " per sq ft against " + price("concrete-driveway") + " for a plain slab; neither figure changes based on county permitting."
            ),
        ],
        "sources": SRC,
    },
    "artificial-turf": {
        "title": "Artificial Turf in Parrish, FL – New-Build Yards",
        "meta": "Artificial turf in Parrish, FL skips the county's weekly watering order on new and established lots alike; market range is " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
        "h1": "Artificial Turf for Parrish Yards",
        "lede": capsule(
            "Turf installers in Parrish are quoting " + price("artificial-turf") + " per " + per("artificial-turf") + " this October, a range that applies equally to a bare new-build lot and a yard that's carried sod for years. "
            "The appeal on the newer side of town is simple: turf never has to wait out the county's once-a-week sprinkler limit the way fresh sod does."
        ),
        "sections": [
            (
                "Four things to settle before the order goes in, regardless of the lot's age",
                "<p>Since May 19, 2026, Florida Administrative Code Rule 62-308.100 has governed every residential turf install in the state, and it comes down to the infill (a natural product, never crumb rubber), what sits underneath it (washed rock, not raw fill), what can't run beneath it (an irrigation line) and how far it has to sit from open water (10 feet, unless a seawall forms that boundary) "
                + src("dep-rule", "DEP Rule 62-308.100") + ". A dog run tucked against a side fence with nothing but more yard beyond it skips that last condition outright; a lawn that backs onto one of Parrish's ponds or canals doesn't. Local ordinances can't push past this statewide floor on a single-family lot under F.S. 125.572 " + src("fs125572", "F.S. 125.572") + ".</p>"
            ),
            (
                "Why timing matters more for sod than for turf",
                "<p>Through March 31, 2027, Manatee County has every address, new or old, on a single assigned sprinkler day under SWFWMD's Modified Phase III order, running from just after midnight to 4 a.m. or from 8 p.m. to midnight "
                + src("manatee-phase3", "Manatee Modified Phase III order") + " " + src("swfwmd-restrictions", "SWFWMD district restrictions") + ". A pallet of fresh sod trying to root under that single weekly window is a genuinely different proposition than turf, which needs no watering day at all once it's down, a gap " + compare("artificial-turf-vs-sod", "our turf-versus-sod comparison") + " walks through in more detail. A patch screened from the street by a fence or hedge also picks up cover from most HOA restrictions under 2026's F.S. 720.3045 " + src("fs720-3045", "F.S. 720.3045") + ".</p>"
            ),
        ],
        "scenario": (
            "Say a 750 sq ft stretch of side yard and backyard behind a new Parrish build gets turf instead of sod",
            "<p>Say a 750 sq ft stretch of side yard and backyard behind a new Parrish build gets turf instead of sod, with no canal or pond touching the property. Pricing runs $7,500 to $18,750 at " + price("artificial-turf") + " per sq ft across the full range, or $9,000 to $13,500 inside the typical " + price("artificial-turf", typical=True) + " band once pile height and backing are chosen. Nothing about the lot triggers the 10-foot water-buffer condition here, but the washed-rock base and natural infill rule still apply exactly as they would three streets over on a lot that does touch water.</p>"
        ),
        "faqs": [
            faq(
                "Why would a new Parrish homeowner choose turf over sod right after closing?",
                "Mostly timing. Fresh sod has to establish under the county's single weekly sprinkler window through March 2027, while turf is finished the day it's installed and never needs a watering slot at all."
            ),
            faq(
                "Does a Parrish yard with no canal or pond still have to meet the state's turf setback?",
                "No. The 10-foot buffer in Rule 62-308.100 only kicks in near open water; a landlocked yard has nothing to measure against."
            ),
            faq(
                "Can crumb rubber be used as turf infill in Parrish?",
                "No. The state rule in effect since May 2026 calls for a natural infill material statewide, ruling out crumb rubber or similar synthetic products on any residential lot regardless of location."
            ),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
