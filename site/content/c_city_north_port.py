# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, svc, city, cs, post, compare, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "north-port"

SRC = [
    "north-port-row-permit-application",
    "north-port-uldc-a.1.1.1-culvert",
    "north-port-uldc-4.4.1-driveway",
    "north-port-uldc-3.2.3-isr",
    "north-port-uldc-3.6.13-pervious-pavers",
    "north-port-uldc-6.5.15.3-floodway",
    "north-port-permitting",
    "north-port-public-works",
    "swfwmd-restrictions",
    "fema-msc",
    "nrcs-myakka-osd",
    "nrcs-immokalee-osd",
    "nrcs-eaugallie-osd",
    "dep-rule",
    "fs125572",
    "fs720-3045",
    ("Census Bureau PEP, City and Town Population Totals, Vintage 2025 (North Port city, FL)", "https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025.csv"),
    ("Census Reporter, North Port, FL (ACS 2020-2024 5-yr, B25035)", "https://censusreporter.org/profiles/16000US1249675-north-port-fl/"),
    ("Wikipedia, North Port, Florida", "https://en.wikipedia.org/wiki/North_Port,_Florida"),
    ("City of North Port, Stormwater Management", "https://www.northportfl.gov/City-Services-and-Safety/Public-Works/Stormwater-Management"),
    ("Wikipedia, Myakkahatchee Creek Environmental Park", "https://en.wikipedia.org/wiki/Myakkahatchee_Creek_Environmental_Park"),
    ("Wikipedia, Warm Mineral Springs, Florida", "https://en.wikipedia.org/wiki/Warm_Mineral_Springs,_Florida"),
]

HUB = page(
    "/north-port-fl/", "city",
    "Concrete & Paver Contractor in North Port, FL",
    "Opera pours concrete and sets pavers in North Port, FL, a city built on a 1950s canal-and-swale grid where a culvert permit comes before most driveway work.",
    "Concrete, Pavers and Turf for North Port Homes",
    capsule(
        "North Port sits about 27 miles south of the Sarasota unit's base, a city built almost entirely on a single mid-century subdivision that's still filling in with new construction today. "
        "As of October 2026, nearly every lot here fronts a roadside swale crossed by a culvert, which is why the city's own Public Works office, not just a building permit, signs off on most driveway, patio and pool-deck projects before the first shovel goes in."
    ),
    "".join([
        sec(
            "Why does North Port treat a driveway as a drainage project first?",
            "<p>City code requires a Public Works permit before anyone installs \"culvert pipe or other structures within City-maintained rights-of-way or easements,\" with staff setting the line and grade and inspecting on 24-hour notice "
            + src("north-port-uldc-a.1.1.1-culvert", "North Port ULDC App. A.1.1.1") + ". That's a separate hurdle from the driveway surface itself: the city's Right-of-Way Use Permit application lists \"Culvert/Driveway/Sidewalk/Concrete Slab\" together as one work category, and the applicant has to restore the roadway, right-of-way and swale before Public Works signs off " + src("north-port-row-permit-application", "North Port ROW Use Permit application") + ". Neighborhood Development Services at 4970 City Hall Blvd, (941) 429-7044, is the office that reviews it.</p>"
        ),
        sec(
            "What size and material does a North Port driveway have to be?",
            "<p>City code requires a one- or two-family home to connect to the street with a driveway built of \"concrete, brick paver, or other material approved by the Public Works Department,\" and the apron specifically has to be an impervious material such as concrete, asphalt or brick pavers "
            + src("north-port-uldc-4.4.1-driveway", "North Port ULDC Sec. 4.4.1") + ".</p>"
            + table(
                "North Port residential driveway dimensions, ULDC Sec. 4.4.1.E",
                ["Garage orientation", "Minimum requirement"],
                [
                    ["Front-load garage", "At least 18 ft long and 10 ft wide at the property line"],
                    ["Side-load garage", "At least 30 ft wide in front of the garage, narrowing to 10 ft at the property line"],
                    ["Collector road or larger (from July 1, 2027)", "Circular or hammerhead drive required"],
                ],
                "Source: North Port ULDC Sec. 4.4.1, checked October 2026 " + src("north-port-uldc-4.4.1-driveway", "North Port ULDC Sec. 4.4.1") + "."
            )
        ),
        sec(
            "Does a new patio or pool deck count against a lot's coverage limit?",
            "<p>The city caps impervious surface area by zoning district under ULDC Sec. 3.2.3, though the specific per-district percentages aren't published in a format this page can quote directly; notably, that overall cap and the related open-space rule don't apply to General Development Corporation-platted lots inside the Port Charlotte Subdivision, the original 1950s grid most of North Port still sits on "
            + src("north-port-uldc-3.2.3-isr", "North Port ULDC Sec. 3.2.3") + ". Owners on a tight lot can offset impervious area with pervious pavers or another permeable surface instead of paying down the percentage another way, as long as the material is kept functioning as a pervious surface going forward " + src("north-port-uldc-3.6.13-pervious-pavers", "North Port ULDC Sec. 3.6.13") + ". No separate exemption for a patio, pool deck or paver surface on private ground has been published; the Building Department instead applies 2026's statewide $7,500 exemption through a written request rather than an automatic waiver " + src("north-port-permitting", "North Port Permitting") + ".</p>"
        ),
        sec(
            "How did North Port end up with a swale in front of almost every house?",
            "<p>Mackle Brothers' General Development Corporation platted more than 114,000 lots across what became North Port and Port Charlotte between 1954 and 1971, digging the canal network that still drains the city today "
            + ext("https://en.wikipedia.org/wiki/North_Port,_Florida", "Wikipedia, North Port, Florida") + ". North Port's own Public Works department now maintains 64 water control structures citywide, with 23 of the gated ones serviced daily, and rehabilitates roughly 30 miles of roadside swale every year " + ext("https://www.northportfl.gov/City-Services-and-Safety/Public-Works/Stormwater-Management", "City of North Port, Stormwater Management") + ". Water collected in that system flows toward Myakkahatchee Creek and the Cocoplum waterway, which the city also draws on for its own drinking-water supply, inside the roughly 196-square-mile Big Slough Watershed " + ext("https://www.northportfl.gov/City-Services-and-Safety/Public-Works/Stormwater-Management", "City of North Port, Stormwater Management") + ".</p>"
        ),
        sec(
            "What happens to retaining walls and fill near a regulated floodway?",
            "<p>Inside a mapped floodway, North Port's code holds retaining walls, sidewalks and driveways that place fill to the same floodway limits as any other structure, though no specific height threshold is published for a retaining wall on its own "
            + src("north-port-uldc-6.5.15.3-floodway", "North Port ULDC Sec. 6.5.15.3") + ". Myakkahatchee Creek, a tributary that the city's stormwater system routes toward on its way to Charlotte Harbor, runs through a wooded 168-acre park north of I-75 that Sarasota County operates " + ext("https://en.wikipedia.org/wiki/Myakkahatchee_Creek_Environmental_Park", "Wikipedia, Myakkahatchee Creek Environmental Park") + ", and a parcel near that corridor is worth a flood-zone check at FEMA's Flood Map Service Center before a wall or deck's elevation gets finalized " + src("fema-msc", "FEMA Flood Map Service Center") + ".</p>"
        ),
        sec(
            "How fast is North Port actually growing, and how old is the typical house?",
            "<p>The Census Bureau's own population estimates put North Port at 75,009 residents in the 2020 base count and 96,551 by July 2025, close to 29 percent growth in five years "
            + ext("https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025.csv", "Census PEP Vintage 2025, North Port") + ", while the city's current ACS five-year estimate puts the median year a home here was built at 2005 " + ext("https://censusreporter.org/profiles/16000US1249675-north-port-fl/", "Census Reporter, North Port") + ". That combination, a city old enough to have decades of established, GDC-era slabs cracking on schedule and growing fast enough to add a steady stream of brand-new ones, is why both repair and first-install work stay busy here at once.</p>"
        ),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq(
            "Does North Port issue its own permits, or does Sarasota County handle it?",
            "North Port issues its own. The city incorporated in 1959 and has run its own Neighborhood Development Services and Public Works review ever since, a different path than an unincorporated Sarasota County address a few miles away would use."
        ),
        faq(
            "Does a brand-new North Port home ever need a driveway or patio permit later on?",
            "Yes. A builder's original driveway and culvert crossing come with the home's construction permit, but any later change, a widened apron, a second parking pad, a patio addition, still goes back through the same Public Works and Building Department review an older GDC-platted lot would use, including the culvert permit if the swale crossing is touched."
        ),
        faq(
            "Why does a culvert permit come up so often for North Port driveways?",
            "Because almost every residential lot in the city fronts a roadside swale, part of the drainage grid General Development Corporation dug in the 1950s and 60s, and a driveway crossing that swale needs its own Public Works-reviewed culvert, separate from the surface material question."
        ),
        faq(
            "Do older, General Development-platted lots in North Port follow different rules than newer ones?",
            "On impervious surface and open space, yes in one respect: the city's overall coverage and open-space standards specifically don't apply to lots platted by General Development Corporation inside the Port Charlotte Subdivision, which covers most of the older part of the city."
        ),
        faq(
            "How do you find the best concrete contractor in North Port?",
            "Run the license-lookup tool first, then ask a North Port-specific question most generic bids skip: has this crew pulled a city culvert permit before, not just a driveway permit, and does the proposal name a base depth for the specific soil under that lot rather than a flat number used everywhere. " + post("how-to-choose-a-concrete-contractor-sarasota", "Our contractor guide") + " covers the rest."
        ),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="North Port",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/sarasota-county-driveway-patio-permits/", "Driveway and patio permits in Sarasota, Venice and North Port"),
        ("/venice-fl/", "Concrete, pavers and turf in Venice"),
        ("/sarasota-fl/", "Concrete, pavers and turf in Sarasota"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in North Port, FL",
)

LOCAL = {
    "concrete-driveways": {
        "title": "Concrete Driveways in North Port, FL – Culvert Permit",
        "meta": "Concrete driveways in North Port, FL cross a city swale, so a Public Works culvert permit comes first; market range is " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
        "h1": "Concrete Driveway Installation in North Port",
        "lede": capsule(
            "A new or replacement concrete driveway in North Port runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026. "
            "Because nearly every lot fronts a drainage swale, the city reviews the culvert crossing that swale separately from the driveway surface itself."
        ),
        "sections": [
            (
                "Two city reviews, not one",
                "<p>ULDC Appendix A.1.1.1 bars anyone from installing \"culvert pipe or other structures within City-maintained rights-of-way or easements\" without a Public Works permit, with the city setting the line and grade and inspecting on 24 hours' notice "
                + src("north-port-uldc-a.1.1.1-culvert", "North Port ULDC App. A.1.1.1") + ". The driveway surface itself then has to be built of \"concrete, brick paver, or other material approved by the Public Works Department\" under Sec. 4.4.1, with the apron specifically required to be an impervious material " + src("north-port-uldc-4.4.1-driveway", "North Port ULDC Sec. 4.4.1") + ".</p>"
            ),
            (
                "Sizing a front-load or side-load driveway",
                "<p>A front-load garage needs a driveway at least 18 feet long and 10 feet wide at the property line, while a side-load garage has to open up to at least 30 feet wide in front of the garage before narrowing back to 10 feet at the property line "
                + src("north-port-uldc-4.4.1-driveway", "North Port ULDC Sec. 4.4.1") + ". Starting July 1, 2027, a home fronting a collector road or larger has to use a circular or hammerhead drive instead of a straight shot to the garage, a rule worth planning around now on any lot that fits that description.</p>"
            ),
        ],
        "scenario": (
            "Say a front-load-garage driveway on a North Port canal lot measures 20 x 40 ft, 800 sq ft, crossing the standard roadside swale",
            "<p>Say a front-load-garage driveway on a North Port canal lot measures 20 x 40 ft, 800 sq ft, crossing the standard roadside swale. At " + price("concrete-driveway") + " per sq ft, that spans $4,800 to $12,000 across the full range, tightening to roughly $6,400 to $9,600 inside the typical " + price("concrete-driveway", typical=True) + " band. Before the forms go up, the culvert crossing the swale gets its own Public Works line-and-grade check, a step a driveway in a jurisdiction without this city's canal-grid history wouldn't need at all.</p>"
        ),
        "faqs": [
            faq(
                "Does every North Port driveway need a culvert permit?",
                "Most do, since almost every residential lot fronts a city-maintained swale that the driveway has to cross. The culvert permit is reviewed separately from the driveway surface material itself."
            ),
            faq(
                "How wide does a side-load garage driveway have to be in North Port?",
                "At least 30 feet wide directly in front of the garage, narrowing to a minimum of 10 feet at the property line, wider at the garage end than the 18-foot length required for a front-load layout."
            ),
            faq(
                "Will North Port require circular driveways on busier streets?",
                "Starting July 1, 2027, yes, for homes fronting a collector road or larger, which have to use a circular or hammerhead configuration rather than a straight driveway to the garage."
            ),
        ],
        "sources": SRC,
    },
    "paver-driveways": {
        "title": "Paver Driveways in North Port, FL – Impervious Apron",
        "meta": "Paver driveways in North Port, FL qualify as the city's required impervious apron material; market range is " + price("paver-driveway") + " per " + per("paver-driveway") + ", Oct. 2026.",
        "h1": "Paver Driveway Installation in North Port",
        "lede": capsule(
            "A paver driveway in North Port costs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026. "
            "The city names brick pavers directly as an approved apron material, though a paver surface still has to clear the same culvert and width rules a poured driveway would."
        ),
        "sections": [
            (
                "Pavers are a named option, not a workaround",
                "<p>North Port's code lists \"concrete, brick paver, or other material approved by the Public Works Department\" as the acceptable driveway surfaces for a one- or two-family home, and separately requires the apron section at the right-of-way to be an impervious material such as concrete, asphalt or brick pavers "
                + src("north-port-uldc-4.4.1-driveway", "North Port ULDC Sec. 4.4.1") + ". Choosing pavers doesn't change the culvert review where the driveway crosses the swale, since that permit is about the drainage structure underneath, not the surface on top " + src("north-port-uldc-a.1.1.1-culvert", "North Port ULDC App. A.1.1.1") + ".</p>"
            ),
            (
                "Where the pervious-paver offset actually helps",
                "<p>On a lot pressed against the city's impervious surface cap, swapping a section of standard pavers for a pervious paver system lets that area offset the overall coverage calculation, as long as the material is kept functioning as a pervious surface rather than sealed over later "
                + src("north-port-uldc-3.6.13-pervious-pavers", "North Port ULDC Sec. 3.6.13") + ". That offset doesn't apply to General Development-platted lots inside the Port Charlotte Subdivision, since the city's overall coverage rule already exempts those parcels outright " + src("north-port-uldc-3.2.3-isr", "North Port ULDC Sec. 3.2.3") + ".</p>"
            ),
        ],
        "scenario": (
            "Say a side-load garage paver driveway in North Port opens to 30 ft at the garage and narrows to 10 ft at the street, averaging out to 650 sq ft",
            "<p>Say a side-load garage paver driveway in North Port opens to 30 ft at the garage and narrows to 10 ft at the street, averaging out to 650 sq ft. At " + price("paver-driveway") + " per sq ft, figure $6,500 to $19,500 across the full range, narrowing to about $7,800 to $13,000 inside the typical " + price("paver-driveway", typical=True) + " band. The trapezoid shape follows the city's own side-load dimension rule rather than the installer's preference, and the culvert crossing at the street still gets its own Public Works inspection regardless of the paver pattern chosen above it.</p>"
        ),
        "faqs": [
            faq(
                "Are brick pavers an approved driveway surface in North Port?",
                "Yes, named directly in the city's own code alongside concrete and asphalt as an acceptable material for both the driveway itself and the apron section in the right-of-way."
            ),
            faq(
                "Can pervious pavers help on a North Port lot near its coverage limit?",
                "Yes, as long as the pervious section is kept functioning as a permeable surface afterward; it offsets the impervious surface calculation under the city's own code, though General Development-platted lots are already exempt from that overall cap."
            ),
            faq(
                "Does a paver driveway skip North Port's culvert permit?",
                "No. The culvert permit covers the drainage structure under the swale crossing, a separate review from whatever surface material, paver or poured concrete, sits on top of the driveway."
            ),
        ],
        "sources": SRC,
    },
    "concrete-patios": {
        "title": "Concrete Patios in North Port, FL – $7,500 Exemption",
        "meta": "Concrete patios in North Port, FL under $7,500 can use the state's written-request exemption; market range is " + price("concrete-patio") + " per " + per("concrete-patio") + ", Oct. 2026.",
        "h1": "Concrete Patio Installation in North Port",
        "lede": capsule(
            "Patio pricing in North Port sits at " + price("concrete-patio") + " per " + per("concrete-patio") + " this October. "
            "No city form waives a patio permit outright; a smaller job instead relies on the state's 2026 written-request exemption for work priced under $7,500."
        ),
        "sections": [
            (
                "No published patio exemption, but a statewide one to ask for",
                "<p>North Port's Permitting page doesn't list a specific carve-out for a patio, pool deck or paver surface on private property; instead, the city applies 2026's statewide exemption for single-family work valued under $7,500 through a written request filed with the Building Department "
                + src("north-port-permitting", "North Port Permitting") + ". That exemption only covers the building permit itself; it doesn't excuse electrical, plumbing, mechanical or structural components, and a project inside a flood-hazard area is excluded outright regardless of its price.</p>"
            ),
            (
                "Whether the patio counts against the lot's coverage",
                "<p>Where a patio does land is on the city's impervious surface ledger under Sec. 3.2.3, which sets a maximum percentage by zoning district, though that overall cap and the matching open-space standard don't reach General Development-platted lots inside the Port Charlotte Subdivision "
                + src("north-port-uldc-3.2.3-isr", "North Port ULDC Sec. 3.2.3") + ". A homeowner on one of those older platted lots can generally add a patio without the same percentage math a newer, non-GDC subdivision lot would face.</p>"
            ),
        ],
        "scenario": (
            "Say a 15 x 20 ft concrete patio addition on an older North Port GDC-platted lot works out to 300 sq ft",
            "<p>Say a 15 x 20 ft concrete patio addition on an older North Port GDC-platted lot works out to 300 sq ft. A broom finish at " + price("concrete-patio") + " per sq ft puts the job somewhere between $1,800 and $3,900, with most quotes landing near " + price("concrete-patio", typical=True) + " per sq ft once the typical range is applied, or $2,100 to $3,000 total. The owner still files the written exemption request with the Building Department before the pour rather than assuming the dollar figure alone waives the step, and because the lot sits in the original Port Charlotte Subdivision, the addition doesn't run into the city's general impervious surface cap either.</p>"
        ),
        "faqs": [
            faq(
                "Does North Port automatically exempt small patios from a permit?",
                "Not automatically. The city applies the state's 2026 exemption for single-family work under $7,500 through a written request to the Building Department rather than waiving the requirement outright."
            ),
            faq(
                "Does a patio count toward North Port's impervious surface cap?",
                "On most lots, yes, under the city's per-district maximum in Sec. 3.2.3. Lots platted by General Development Corporation inside the Port Charlotte Subdivision are specifically excluded from that overall cap."
            ),
            faq(
                "What work isn't covered by North Port's $7,500 exemption?",
                "Electrical, plumbing, mechanical and structural components are excluded regardless of the project's price, and any work inside a flood-hazard area doesn't qualify for the exemption at all."
            ),
        ],
        "sources": SRC,
    },
    "paver-patios": {
        "title": "Paver Patios in North Port, FL – Pervious Offset",
        "meta": "Paver patios in North Port, FL can use pervious pavers to offset impervious surface limits under ULDC 3.6.13; market range is " + price("paver-patio") + " per " + per("paver-patio") + ".",
        "h1": "Paver Patios and Walkways in North Port",
        "lede": capsule(
            "A paver patio in North Port costs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. "
            "With the city's median home dated to 2005, plenty of patio work here is a resurfacing of an original slab rather than a first installation on open ground."
        ),
        "sections": [
            (
                "Working on a house that's past its first two decades",
                "<p>Census Reporter's current five-year estimate puts the median year a North Port home was built at 2005 "
                + ext("https://censusreporter.org/profiles/16000US1249675-north-port-fl/", "Census Reporter, North Port") + ", old enough that a fair share of original concrete patios around the city are due for a paver overlay or a full replacement rather than a brand-new install. A homeowner keeping the project under the state's $7,500 written-request threshold still files that request with the Building Department before the surface swap, since no separate patio exemption is published here " + src("north-port-permitting", "North Port Permitting") + ".</p>"
            ),
            (
                "Letting a pervious section do double duty",
                "<p>City code lets a pervious paver installation or other permeable surface offset impervious surface area elsewhere on the lot, provided the owner keeps it functioning as pervious going forward "
                + src("north-port-uldc-3.6.13-pervious-pavers", "North Port ULDC Sec. 3.6.13") + ", an option worth raising on a lot outside the Port Charlotte Subdivision's GDC exemption where the coverage percentage is actually running tight.</p>"
            ),
        ],
        "scenario": (
            "Say a 350 sq ft paver patio replaces an original 2000s-era concrete slab on a North Port lot outside the GDC exemption",
            "<p>Say a 350 sq ft paver patio replaces an original 2000s-era concrete slab on a North Port lot outside the GDC exemption. The full " + price("paver-patio") + " per sq ft range puts the job at $3,500 to $5,950, though most quotes here land in the $4,200-to-$5,600 neighborhood once the " + price("paver-patio", typical=True) + " typical band and paver grade are factored in. Swapping in a pervious section for part of the new layout trims the lot's impervious surface tally under Sec. 3.6.13, a detail that matters here specifically because this parcel doesn't carry the older GDC-platted exemption a Port Charlotte Subdivision lot would.</p>"
        ),
        "faqs": [
            faq(
                "Is most paver patio work in North Port a first install or a replacement?",
                "A fair amount is a replacement or overlay, given the city's median home dates to 2005; original concrete patios from that era are reaching the point where resurfacing in pavers is a common next step."
            ),
            faq(
                "How does the pervious paver offset work for a North Port patio?",
                "Installing pervious pavers or another permeable surface lets that square footage offset impervious surface area elsewhere on the lot, as long as the material stays functionally pervious rather than getting sealed over later."
            ),
            faq(
                "Do all North Port lots qualify for the GDC impervious surface exemption?",
                "No, only lots platted by General Development Corporation inside the Port Charlotte Subdivision. A patio on a lot outside that original plat still has to work within the standard per-district coverage cap."
            ),
        ],
        "sources": SRC,
    },
    "concrete-pool-decks": {
        "title": "Concrete Pool Decks in North Port, FL – Floodway Rule",
        "meta": "Concrete pool decks near a regulated floodway in North Port, FL follow ULDC 6.5.15.3's fill limits; market range is " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ".",
        "h1": "Concrete Pool Deck Installation in North Port",
        "lede": capsule(
            "A concrete pool deck in North Port runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. "
            "Near a regulated floodway, the deck's fill has to respect the same limits the city applies to any structure placed in that corridor."
        ),
        "sections": [
            (
                "What a mapped floodway adds to the project",
                "<p>City code holds a retaining wall, sidewalk or driveway that places fill inside a regulated floodway to the floodway's own development limits, a standard that extends to a pool deck's fill and grading the same way "
                + src("north-port-uldc-6.5.15.3-floodway", "North Port ULDC Sec. 6.5.15.3") + ". No separate height threshold is published for when that rule starts applying, so a parcel's exact floodway boundary is worth confirming before a deck's elevation is finalized rather than assumed from a neighboring lot.</p>"
            ),
            (
                "Checking the flood zone near Myakkahatchee Creek",
                "<p>Myakkahatchee Creek runs through North Port on its way toward Charlotte Harbor, passing a 168-acre county-operated park north of I-75 along the way "
                + ext("https://en.wikipedia.org/wiki/Myakkahatchee_Creek_Environmental_Park", "Wikipedia, Myakkahatchee Creek Environmental Park") + ", and a lot anywhere near that corridor or one of the city's many drainage canals is worth checking at FEMA's Flood Map Service Center before a pool deck's finished elevation gets set " + src("fema-msc", "FEMA Flood Map Service Center") + ".</p>"
            ),
        ],
        "scenario": (
            "Say a 540 sq ft pool deck goes in on a North Port lot near a mapped floodway along the Myakkahatchee Creek corridor",
            "<p>Say a 540 sq ft pool deck goes in on a North Port lot near a mapped floodway along the Myakkahatchee Creek corridor. At " + price("concrete-pool-deck") + " per sq ft, that spans $2,700 to $8,100 across the full range, tightening to roughly $3,780 to $6,480 inside the typical " + price("concrete-pool-deck", typical=True) + " band, the spread tied to finish choice. Because the lot sits near the floodway, the fill brought in under the deck is checked against the city's floodway development limits before the pour, a step a deck well outside that corridor wouldn't trigger.</p>"
        ),
        "faqs": [
            faq(
                "Does every North Port pool deck need a floodway review?",
                "No, only one near a mapped regulated floodway, commonly along a creek or major canal corridor. The city's rule on fill placement applies specifically inside that boundary, not citywide."
            ),
            faq(
                "How do I know if my North Port lot sits in a flood zone?",
                "FEMA's Flood Map Service Center returns the specific zone designation for an address, which is worth checking before a pool deck's elevation is finalized on any lot near a creek, canal or the Myakkahatchee corridor."
            ),
            faq(
                "Is there a height limit on floodway retaining walls in North Port?",
                "None is published specifically for retaining walls; the floodway development limits apply to the fill and structure generally, so a parcel's exact boundary is confirmed case by case rather than against a fixed height number."
            ),
        ],
        "sources": SRC,
    },
    "pool-deck-pavers": {
        "title": "Pool Deck Pavers in North Port, FL – Canal Lots",
        "meta": "Pool deck pavers on North Port, FL canal lots tie into the city's swale-and-culvert drainage grid; market range is " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ".",
        "h1": "Travertine and Paver Pool Decks in North Port",
        "lede": capsule(
            "Pool deck pavers or travertine in North Port run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. "
            "On a canal-front lot tied into the city's drainage grid, where the deck's runoff ends up matters as much as which stone sits on top."
        ),
        "sections": [
            (
                "Why North Port's drainage system shapes deck grading",
                "<p>The city's own stormwater system, 64 water control structures and about 30 miles of roadside swale rehabbed every year, routes runoff toward Myakkahatchee Creek and the Cocoplum waterway, the same path the city draws its drinking water from "
                + ext("https://www.northportfl.gov/City-Services-and-Safety/Public-Works/Stormwater-Management", "City of North Port, Stormwater Management") + ". A pool deck overlay on a canal lot gets graded to keep runoff moving toward that system rather than pooling against the house, a detail that matters more here than in a city without this scale of engineered drainage.</p>"
            ),
            (
                "The soil underneath still sets the base",
                "<p>Myakka and Immokalee, both common across North Port, hold a seasonal high water table within about 18 inches of grade for part of most years "
                + src("nrcs-myakka-osd", "NRCS Myakka soil series") + " " + src("nrcs-immokalee-osd", "NRCS Immokalee soil series") + ", which affects how much compacted aggregate a travertine or paver overlay needs underneath regardless of how well the citywide canal system drains the rest of the lot.</p>"
            ),
        ],
        "scenario": (
            "Say a 480 sq ft paver overlay goes over an older pool deck on a North Port canal-front lot",
            "<p>Say a 480 sq ft paver overlay goes over an older pool deck on a North Port canal-front lot. At " + price("pool-deck-pavers") + " per sq ft, figure $5,760 to $14,400 across the full range, narrowing to about $6,720 to $10,560 inside the typical " + price("pool-deck-pavers", typical=True) + " band depending on stone grade and pattern. Grading the new surface to shed water toward the canal side rather than the house takes priority over the paver pattern itself, and the base underneath still gets sized for Myakka or Immokalee soil the same way it would three blocks inland.</p>"
        ),
        "faqs": [
            faq(
                "Does a canal lot in North Port need special drainage planning for a pool deck overlay?",
                "Generally yes. Grading the new surface to move runoff toward the canal and the broader city drainage system, rather than pooling it near the house, is a bigger factor than on a non-canal lot."
            ),
            faq(
                "Does North Port's water supply connection affect pool deck work?",
                "Not directly for the construction itself, but it's a reason the city takes swale and canal maintenance seriously citywide, since the same system that drains yards also feeds the utility's drinking-water source."
            ),
            faq(
                "What soil is typically under a North Port pool deck?",
                "Myakka or Immokalee are both common across the city, and either one holds a seasonal high water table that affects how deep the compacted base under an overlay needs to run."
            ),
        ],
        "sources": SRC,
    },
    "stamped-concrete": {
        "title": "Stamped Concrete in North Port, FL – Circular Drives",
        "meta": "Stamped concrete circular driveways in North Port, FL get ahead of the 2027 collector-road rule; market range is " + price("stamped-concrete") + " per " + per("stamped-concrete") + ".",
        "h1": "Stamped Concrete Driveways and Patios in North Port",
        "lede": capsule(
            "Stamped concrete in North Port costs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October 2026. "
            "A stamped circular drive is worth planning early on a collector-road lot, since the city's own code will require that layout there starting July 1, 2027."
        ),
        "sections": [
            (
                "Getting ahead of the 2027 collector-road rule",
                "<p>Homes fronting a collector road or larger will have to use a circular or hammerhead driveway rather than a straight shot to the garage once that part of ULDC Sec. 4.4.1.E takes effect "
                + src("north-port-uldc-4.4.1-driveway", "North Port ULDC Sec. 4.4.1") + ". A homeowner replacing an aging driveway on that kind of lot now has a reason to design the circular layout in stamped concrete from the start rather than retrofitting a straight apron into a loop later.</p>"
            ),
            (
                "Keeping a stamped pour clear of the canal network's grading",
                "<p>Because so much of North Port drains through a citywide grid of swales and canals rather than storm sewers, a stamped driveway or walkway still has to respect the lot's existing grade toward that system; stamping doesn't change the culvert or right-of-way review that applies to any driveway crossing a swale "
                + src("north-port-uldc-a.1.1.1-culvert", "North Port ULDC App. A.1.1.1") + ".</p>"
            ),
        ],
        "scenario": (
            "Say a North Port homeowner builds a 280 sq ft stamped circular driveway loop ahead of the 2027 collector-road rule",
            "<p>Say a North Port homeowner builds a 280 sq ft stamped circular driveway loop ahead of the 2027 collector-road rule. Pricing it out at " + price("stamped-concrete") + " per sq ft puts the full range at $2,240 to $5,320, with most jobs settling near " + price("stamped-concrete", typical=True) + " per sq ft, or roughly $3,360 to $4,480 total, once color count and pattern are picked. Building the loop now means the homeowner isn't retrofitting a straight driveway into a circular one once the 2027 rule takes effect, and the culvert crossing where the loop meets the street still gets the same Public Works review a straight driveway would.</p>"
        ),
        "faqs": [
            faq(
                "When does North Port require a circular driveway on collector roads?",
                "Starting July 1, 2027, for homes fronting a collector road or larger, which have to use a circular or hammerhead configuration under the city's own driveway code."
            ),
            faq(
                "Does stamping a driveway change its culvert review in North Port?",
                "No. The decorative finish doesn't affect the Public Works review of the culvert where the driveway crosses a roadside swale; that permit covers the drainage structure, not the surface pattern."
            ),
            faq(
                "Is stamped concrete worth it on an older North Port driveway before 2027?",
                "It can be, especially on a collector-road lot that will eventually need a circular layout anyway; building that shape now in a stamped pattern avoids a second retrofit project later."
            ),
        ],
        "sources": SRC,
    },
    "artificial-turf": {
        "title": "Artificial Turf in North Port, FL – Canal Setback",
        "meta": "Artificial turf on North Port, FL canal lots follows the state's 10-foot water buffer; market range is " + price("artificial-turf") + " per " + per("artificial-turf") + ", Oct. 2026.",
        "h1": "Artificial Turf for North Port Yards",
        "lede": capsule(
            "Artificial turf in North Port runs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October 2026. "
            "With canals and drainage waterways touching so many lots across the city, the state's water-buffer condition comes up more often here than in a town with fewer lots backing to open water."
        ),
        "sections": [
            (
                "Reading the turf rule against a city built on canals",
                "<p>Florida's Rule 62-308.100, in effect since May 19, 2026, requires a natural infill, a washed-rock base, no irrigation line beneath the surface and at least 10 feet of clearance from a water body's edge unless a seawall sits on that line "
                + src("dep-rule", "DEP Rule 62-308.100") + ". General Development Corporation's canal grid put more North Port lots within reach of open water than a typical inland subdivision would have, so that buffer condition is worth checking on any backyard before the layout is finalized. F.S. 125.572 keeps the city from setting a tighter standard than the state's on a single-family lot " + src("fs125572", "F.S. 125.572") + ".</p>"
            ),
            (
                "Turf and the district's current watering limit",
                "<p>Sarasota County, North Port included, is one of the counties SWFWMD's Modified Phase III order holds to a single assigned sprinkler day a week through March 31, 2027, inside a pre-dawn or late-evening window "
                + src("swfwmd-restrictions", "SWFWMD district restrictions") + ". A sod lawn has to work within that one weekly slot to establish; a turf lawn needs no slot at all once it's down, a comparison explored further in " + compare("artificial-turf-vs-sod", "our turf-versus-sod comparison") + ". Turf out of view from the street also picks up cover from most HOA rules under F.S. 720.3045 as of 2026 " + src("fs720-3045", "F.S. 720.3045") + ".</p>"
            ),
        ],
        "scenario": (
            "Say a North Port backyard backing to one of the city's drainage canals gets 680 sq ft of turf, 12 ft from the water's edge",
            "<p>Say a North Port backyard backing to one of the city's drainage canals gets 680 sq ft of turf, 12 ft from the water's edge. Pile height and backing choice move the job between " + price("artificial-turf") + " per sq ft on the wide end, roughly $6,800 to $17,000 total, and the typical " + price("artificial-turf", typical=True) + " band most quotes fall into, closer to $8,160 to $12,240. Twelve feet clears the state's 10-foot buffer with margin to spare, and the washed-rock base and natural-infill specs apply the same way they would on a lot with no canal frontage at all.</p>"
        ),
        "faqs": [
            faq(
                "Do most North Port yards have to account for the turf water-buffer rule?",
                "More than a typical city, since the General Development-era canal grid put a large share of residential lots within reach of open water. A yard with no canal, pond or creek frontage still skips the condition entirely."
            ),
            faq(
                "Does turf avoid Sarasota County's current watering restriction in North Port?",
                "Yes. The county's one-day-a-week order under SWFWMD's Modified Phase III restrictions governs sprinkler irrigation through March 2027; turf needs no scheduled watering day once it's installed."
            ),
            faq(
                "How close to a North Port canal can artificial turf be installed?",
                "The statewide floor sets that line at 10 feet back from open water, measured from the actual edge, and that distance drops away entirely on a lot where a seawall forms the property boundary instead."
            ),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
