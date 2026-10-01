# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, svc, city, cs, post, compare, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "ellenton"

SRC = [
    "manatee-ldc-1004.2-access-drainage-permit",
    "manatee-driveway-culvert-service",
    "manatee-driveway-application",
    "manatee-paver-driveway-inspections",
    "manatee-no-permit-list",
    "manatee-ldc-511.16-pool-decks",
    "manatee-ldc-403.10-watershed",
    "manatee-phase3",
    "swfwmd-restrictions",
    "fema-coastal-firm",
    "fdot-sdg",
    "nrcs-myakka-osd",
    "nrcs-pomello-osd",
    "nrcs-eaugallie-osd",
    "dep-rule",
    "fs125572",
    "fs720-3045",
    "fcc-bradenton-normals",
    ("Census Reporter, Ellenton FL (ACS 2020-2024 5-yr, B01003/B25035)", "http://censusreporter.org/profiles/16000US1220375-ellenton-fl/"),
    ("Wikipedia, Ellenton, Florida", "https://en.wikipedia.org/wiki/Ellenton,_Florida"),
    ("Florida State Parks, Gamble Plantation Historic State Park", "https://www.floridastateparks.org/parks-and-trails/judah-p-benjamin-confederate-memorial-gamble-plantation-historic-state-park/gamble"),
]

HUB = page(
    "/ellenton-fl/", "city",
    "Concrete & Paver Contractor in Ellenton, FL",
    "Opera pours concrete and sets pavers in Ellenton, FL, unincorporated Manatee County, where LDC Sec. 1004.2 covers the apron and a plain patio skips a permit.",
    "Concrete, Pavers and Turf for Ellenton Homes",
    capsule(
        "Ellenton has no city hall of its own; it's an unincorporated pocket of Manatee County on the tidal Manatee River, about 13 miles from the Sarasota unit's base, where the crew builds driveways, patios, pool decks and turf. "
        "As of October 2026, every permit question here, the apron at the street, a patio, a pool deck, runs through the county's Land Development Code rather than a municipal building office, since Ellenton was never incorporated."
    ),
    "".join([
        sec(
            "Which county office signs off on an Ellenton driveway?",
            "<p>Manatee County LDC Sec. 1004.2.A puts it plainly: no part of a driveway reaching from the property line to the edge of the road pavement \"shall be constructed, improved, or enlarged without an access and drainage permit,\" and the same rule covers a sidewalk, culvert, swale or handicap ramp inside the right-of-way "
            + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC Sec. 1004.2") + ". Routine driveway upkeep is specifically exempt from that permit "
            + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC Sec. 1004.2") + ". The Driveway/Culvert permit itself runs through Public Works' Infrastructure Engineering Division, filed in Accela under Building, Public Works, Driveway/Culvert, with 311 fielding questions Monday through Friday "
            + src("manatee-driveway-culvert-service", "Manatee driveway/culvert permit service") + ", and residential applications land at Building & Development Services, 1112 Manatee Ave W "
            + src("manatee-driveway-application", "Manatee driveway and culvert application") + ". " + post("manatee-county-driveway-permits", "Our Manatee County permit guide") + " walks through how that compares to Palmetto and Bradenton next door.</p>"
        ),
        sec(
            "What numbers does the county's own driveway application set?",
            "<p>The application spells out the build in specific terms rather than leaving it general:</p>"
            + table(
                "Manatee County residential driveway and apron specifications",
                ["Item", "Requirement"],
                [
                    ["Width", "12 ft minimum, 24 ft maximum"],
                    ["Thickness in the ROW", "6 in., from the edge of pavement to the right-of-way line"],
                    ["Curb-to-drive joint", "Expansion joint required"],
                    ["Catch basin clearance", "At least 3 ft"],
                    ["Shell aprons", "Not allowed next to a paved road"],
                ],
                "Source: Manatee County Driveway and Culvert Application, checked October 2026 " + src("manatee-driveway-application", "Manatee driveway and culvert application") + "."
            )
            + "<p>County crews also set the culvert and swale grades, and the existing Type \"F\" curb gets removed for the width of the new drive " + src("manatee-driveway-application", "Manatee driveway and culvert application") + ".</p>"
        ),
        sec(
            "Does a patio or a deck in Ellenton need a permit?",
            "<p>Manatee County keeps a standing reference for exactly this question, and a plain concrete or paver patio, nothing structural tied into it, lands on the side that skips a permit "
            + src("manatee-no-permit-list", "Manatee no-permit list") + ". Pour footers under that same slab, or add a pool, and the project crosses onto the side that needs one; a detached deck stays exempt only under 30 inches high and 120 sq ft, while an attached deck of any size always needs a permit "
            + src("manatee-no-permit-list", "Manatee no-permit list") + ". Development Services sorts out the borderline cases at 941-748-4501 ext. 3800. Separately, a pool deck or screen cage has its own distance rule to clear under LDC Sec. 511.16, a 5-foot minimum off the lot line or the shoreline that the code doesn't treat as encroaching on the yard " + src("manatee-ldc-511.16-pool-decks", "Manatee LDC Sec. 511.16") + ".</p>"
        ),
        sec(
            "Is there a hardscape coverage limit in unincorporated Ellenton?",
            "<p>The county's Land Development Code doesn't set a general single-family impervious surface ratio the way Bradenton's city code does. Where a cap does appear is inside overlay districts, Watershed Protection and Coastal among them, where an application has to state the maximum percentage of impervious surface the project proposes "
            + src("manatee-ldc-403.10-watershed", "Manatee LDC Sec. 403.10") + ". Most Ellenton lots sit outside those overlays, so a driveway, patio and pool deck on the same parcel typically aren't totaled against a single countywide percentage the way they would be across the river in Bradenton.</p>"
        ),
        sec(
            "What does Ellenton's history tell you about a project here?",
            "<p>The community takes its name from Ellen, the daughter of Major George and Mary Patten, who bought land here and named it for her around 1870 "
            + ext("https://en.wikipedia.org/wiki/Ellenton,_Florida", "Ellenton, Florida") + ". Its oldest surviving structure predates that naming by decades: the Gamble Plantation house, built between 1845 and 1850 and now a state historic site at 3708 Patten Avenue, is described by the state park service as the only plantation house still standing in South Florida " + ext("https://www.floridastateparks.org/parks-and-trails/judah-p-benjamin-confederate-memorial-gamble-plantation-historic-state-park/gamble", "Florida State Parks, Gamble Plantation") + ". Census Reporter's latest five-year estimate puts Ellenton's population at about 5,133 and the median year a home here was built at 1988, newer housing stock on average than either Palmetto or Bradenton across the river " + ext("http://censusreporter.org/profiles/16000US1220375-ellenton-fl/", "Census Reporter, Ellenton FL") + ". Interstate 75 forms the community's eastern edge at Exit 224, with US 301 running through its center toward Palmetto and Bradenton " + ext("https://en.wikipedia.org/wiki/Ellenton,_Florida", "Ellenton, Florida") + ".</p>"
        ),
        sec(
            "How much of Ellenton is actually water, and what does that mean for a build?",
            "<p>The Census Bureau's own geography for the Ellenton CDP runs about 4.47 square miles, roughly a quarter of it open water, with an average elevation near 13 feet above sea level "
            + ext("https://en.wikipedia.org/wiki/Ellenton,_Florida", "Ellenton, Florida") + ", figures that track with its position along the tidal reach of the Manatee River. FEMA's Zone AE carries roughly a 1% yearly flood chance with limited wave action, and the Coastal High Hazard Zone VE adds breaking-wave force to those same odds "
            + src("fema-coastal-firm", "FEMA flood zone designations") + "; a parcel-level check at the Flood Map Service Center is worth running before a pool deck or a retaining wall near the river gets its elevation set. A September 22, 2026 county notice extends the district's Modified Phase III water-shortage order through the end of March 2027, holding every address, Ellenton included, to a single assigned sprinkler day, though hand-watering and micro-irrigation stay allowed every morning before 8 or every evening after 6 regardless of that assignment " + src("manatee-phase3", "Manatee Modified Phase III order") + " " + src("swfwmd-restrictions", "SWFWMD district restrictions") + ".</p>"
        ),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq(
            "Does Ellenton have its own building department?",
            "No. Ellenton has never incorporated, so every permit question, from a driveway apron to a pool deck, goes through Manatee County's Development Services and Public Works departments rather than a city office."
        ),
        faq(
            "What width does an Ellenton driveway apron have to be?",
            "The county's application sets a 12-foot minimum and a 24-foot maximum, with the portion inside the right-of-way poured 6 inches thick from the edge of pavement to the right-of-way line."
        ),
        faq(
            "Can I pour a patio in Ellenton without a permit?",
            "A non-structural concrete or paver patio is currently on the county's no-permit list. A slab poured with footers, a pool, or an attached deck of any size still needs one filed first."
        ),
        faq(
            "Is my Ellenton address in a flood zone?",
            "Given how much of the CDP sits along the tidal Manatee River and how low the average elevation runs, it's worth checking. FEMA's Flood Map Service Center at msc.fema.gov returns the specific AE or VE designation for a parcel."
        ),
        faq(
            "How do you pick the best concrete contractor for an Ellenton project?",
            "Confirm the contractor on the state's license-verification tool, ask whether the quote accounts for the county's access and drainage permit rather than a city process, and check how the base plan handles Ellenton's low-lying, flatwoods soil. " + post("how-to-choose-a-concrete-contractor-sarasota", "Our contractor guide") + " covers the rest."
        ),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Ellenton",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/manatee-county-driveway-permits/", "Driveway and patio permits in Bradenton, Lakewood Ranch, Parrish and Palmetto"),
        ("/palmetto-fl/", "Concrete, pavers and turf in Palmetto"),
        ("/bradenton-fl/", "Concrete, pavers and turf in Bradenton"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Ellenton, FL",
)

LOCAL = {
    "concrete-driveways": {
        "title": "Concrete Driveways in Ellenton, FL – LDC 1004.2",
        "meta": "Concrete driveways in Ellenton, FL need a Manatee County access and drainage permit under LDC 1004.2; market range is " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
        "h1": "Concrete Driveway Installation in Ellenton",
        "lede": capsule(
            "A new or replacement concrete driveway in Ellenton runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026. "
            "Because the community is unincorporated, the permit for the portion reaching the street comes from Manatee County's own access and drainage process, not a city office."
        ),
        "sections": [
            (
                "Filing through the county, not a city hall",
                "<p>LDC Sec. 1004.2.A requires an access and drainage permit before any driveway, defined broadly enough to include \"a sidewalk, culvert, drainage or stormwater structure, swale, driveway apron, roadway shoulder or handicap ramp,\" gets built, widened or improved in the right-of-way "
                + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC Sec. 1004.2") + ". The application itself sets the build: 12 feet minimum and 24 feet maximum in width, 6 inches of thickness from the edge of pavement to the right-of-way line, an expansion joint where the drive meets the curb, and at least 3 feet of clearance from any catch basin " + src("manatee-driveway-application", "Manatee driveway and culvert application") + ". Shell driveway aprons aren't allowed next to a paved road under the same application " + src("manatee-driveway-application", "Manatee driveway and culvert application") + ".</p>"
            ),
            (
                "Planning the subgrade for Ellenton's flatwoods ground",
                "<p>Myakka, Florida's own state soil and one of the most common series mapped across Manatee County, holds a seasonal high water table less than 18 inches down for one to four months in most years "
                + src("nrcs-myakka-osd", "NRCS Myakka soil series") + ". Florida's residential code caps clean sand or gravel fill at 24 inches and ordinary earth at 8 inches before an engineer has to sign off, with a 4-inch compacted base required underneath regardless. On a low-lying Ellenton lot, that water table, more than the finished driveway's size, is usually what sets how deep the fill plan has to run.</p>"
            ),
        ],
        "scenario": (
            "Say a 20 x 30 ft driveway reaching from an Ellenton garage out to the county right-of-way comes to 600 sq ft",
            "<p>Say a 20 x 30 ft driveway reaching from an Ellenton garage out to the county right-of-way comes to 600 sq ft. At " + price("concrete-driveway") + " per sq ft, that spans $3,600 to $9,000 across the full range, tightening to roughly $4,800 to $7,200 inside the typical " + price("concrete-driveway", typical=True) + " band. The section crossing the right-of-way has to match the county's 6-inch thickness spec and clear the 3-foot catch basin setback before the access and drainage permit closes out, requirements a driveway built entirely on private ground further back on the lot wouldn't have to meet.</p>"
        ),
        "faqs": [
            faq(
                "Who issues my driveway permit in Ellenton?",
                "Manatee County's Public Works Infrastructure Engineering Division, through an access and drainage permit filed in Accela under Building, Public Works, Driveway/Culvert. Ellenton has no city office of its own to handle it."
            ),
            faq(
                "How thick does an Ellenton driveway need to be at the road?",
                "6 inches, measured from the edge of the road pavement to the right-of-way line, per the county's own driveway and culvert application, with the rest of the slab typically following standard residential thickness."
            ),
            faq(
                "Does Ellenton's soil change how deep a driveway's base goes?",
                "Often. Myakka, a common soil across the area, keeps groundwater within about 18 inches of the surface for part of most years, which affects how much fill a driveway built for heavier loads needs before the slab goes down."
            ),
        ],
        "sources": SRC,
    },
    "paver-driveways": {
        "title": "Paver Driveways in Ellenton, FL – Inspection Spec",
        "meta": "Paver driveways in Ellenton, FL follow Manatee County's own inspection spec for grade cut and width; market range is " + price("paver-driveway") + " per " + per("paver-driveway") + ", Oct. 2026.",
        "h1": "Paver Driveway Installation in Ellenton",
        "lede": capsule(
            "A paver driveway in Ellenton costs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026. "
            "The county publishes an inspection sheet specific to paver driveways, separate from its general driveway application, that sets the grade cut and the width a crew has to build to."
        ),
        "sections": [
            (
                "What the county's paver inspection sheet actually checks",
                "<p>Manatee County's own inspection guidance for paver driveways calls for a 6-inch grade cut, so the compacted sub-base plus the paver together equal 6 inches at finished grade "
                + src("manatee-paver-driveway-inspections", "Manatee paver driveway inspections") + ". Width runs 12 to 24 feet the same as a poured driveway, except a street-facing three-car garage is allowed up to 30 feet, with flares adding 3 feet on each side at the roadway over an 8-foot run " + src("manatee-paver-driveway-inspections", "Manatee paver driveway inspections") + ". Where a concrete sidewalk section crosses the paver drive, its spec matches the residential standard elsewhere in the county, a 4-inch, 5-foot-wide broom-finished strip spanning the full lot frontage with saw cuts spaced every 10 feet " + src("manatee-paver-driveway-inspections", "Manatee paver driveway inspections") + ".</p>"
            ),
            (
                "Building the base over Pomello or EauGallie ground",
                "<p>Pomello soil, mapped across parts of Manatee County, drains somewhat better than the area's wettest flatwoods, with groundwater typically 18 to 48 inches down, while EauGallie runs wetter, inside 18 inches for one to four months most years "
                + src("nrcs-pomello-osd", "NRCS Pomello soil series") + " " + src("nrcs-eaugallie-osd", "NRCS EauGallie soil series") + ". ICPI calls for roughly 6 inches of compacted aggregate on the better-drained end of that range and 2 to 4 more inches on the wetter end, a distinction worth confirming with a soil check before the base is ordered rather than assumed from the lot next door.</p>"
            ),
        ],
        "scenario": (
            "Say a 28 x 22 ft paver apron for a street-facing three-car garage in Ellenton comes to 616 sq ft",
            "<p>Say a 28 x 22 ft paver apron for a street-facing three-car garage in Ellenton comes to 616 sq ft. At " + price("paver-driveway") + " per sq ft, figure $6,160 to $18,480 across the full range, narrowing to about $7,392 to $12,320 inside the typical " + price("paver-driveway", typical=True) + " band. Because the garage faces the street directly, the county's inspection sheet allows the apron up to 30 feet wide rather than the standard 24-foot cap, with an 8-foot flare on each side where the drive meets the road, and the grade still gets cut so the compacted base plus paver together land at 6 inches.</p>"
        ),
        "faqs": [
            faq(
                "Can an Ellenton paver driveway be wider than 24 feet?",
                "Yes, up to 30 feet, but only for a street-facing three-car garage under the county's paver driveway inspection sheet; a standard one- or two-car driveway still falls inside the 12-to-24-foot range."
            ),
            faq(
                "What is the grade-cut rule for a paver driveway in Ellenton?",
                "The county's inspection guidance calls for a 6-inch grade cut, meaning the compacted sub-base and the paver together have to total 6 inches at finished grade, the same overall depth as a poured concrete apron."
            ),
            faq(
                "Does a sidewalk crossing a paver driveway need its own spec in Ellenton?",
                "Yes. The crossing matches the county's standard residential walk, 4 inches thick and 5 feet wide, carried the full lot frontage with a broom finish and saw cuts every 10 feet."
            ),
        ],
        "sources": SRC,
    },
    "concrete-patios": {
        "title": "Concrete Patios in Ellenton, FL – No-Permit List",
        "meta": "Non-structural concrete patios in Ellenton, FL skip a county permit, unlike a slab with footers; market range is " + price("concrete-patio") + " per " + per("concrete-patio") + ", Oct. 2026.",
        "h1": "Concrete Patio Installation in Ellenton",
        "lede": capsule(
            "A concrete patio in Ellenton runs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. "
            "Where the slab lands on the county's permit list depends on a detail easy to miss: whether it's freestanding and non-structural, or poured with footers against an existing wall."
        ),
        "sections": [
            (
                "The line between exempt and permitted, in the county's own words",
                "<p>Manatee County's current no-permit list names a \"non-structural concrete/paver patio\" directly as work that skips a building permit "
                + src("manatee-no-permit-list", "Manatee no-permit list") + ", while a \"concrete slab with footers\" sits on the opposite side of the same list and does need one " + src("manatee-no-permit-list", "Manatee no-permit list") + ". A simple broom-finished pad poured on grade, detached from the house's foundation, usually falls in the first category; a patio tied structurally into an addition or a new footer along the house wall falls in the second, and a call to Development Services at 941-748-4501 ext. 3800 settles which applies before the forms go up.</p>"
            ),
            (
                "Decks share the same lot, different rule",
                "<p>A detached deck under 30 inches high and under 120 sq ft is exempt the same way a non-structural patio is, but every attached deck needs a permit regardless of height or size "
                + src("manatee-no-permit-list", "Manatee no-permit list") + ", a distinction that matters on a lot where a patio and a small deck are being planned together. The patio's own drainage plan still has to account for Felda or similar wet-flatwoods soil underneath, common enough across the area that a perimeter swale is worth sketching before the slope is poured rather than adjusted after.</p>"
            ),
        ],
        "scenario": (
            "Say a 12 x 20 ft concrete patio, 240 sq ft, is poured against the house with a footer tying into a planned screen enclosure",
            "<p>Say a 12 x 20 ft concrete patio, 240 sq ft, is poured against the house with a footer tying into a planned screen enclosure. At " + price("concrete-patio") + " per sq ft, that comes to $1,440 to $3,120 across the full range, narrowing to about $1,680 to $2,400 inside the typical " + price("concrete-patio", typical=True) + " band for a broom finish. Because the footer ties the slab structurally to the screen enclosure, it falls outside the county's non-structural exemption and needs a permit filed before the pour, a step a simple freestanding patio of the same size could have skipped entirely.</p>"
        ),
        "faqs": [
            faq(
                "Does every concrete patio need a permit in Ellenton?",
                "No. A freestanding, non-structural patio is on the county's current no-permit list. A slab poured with footers, especially one tied into a screen enclosure or addition, falls outside that exemption and needs a permit."
            ),
            faq(
                "Is a small deck next to an Ellenton patio exempt too?",
                "Only if it's detached, under 30 inches high and under 120 sq ft. An attached deck of any size needs a permit, a different standard than the patio exemption right next to it."
            ),
            faq(
                "Who do I call to confirm whether my Ellenton patio needs a permit?",
                "Manatee County Development Services, at 941-748-4501 ext. 3800, is the quickest way to settle a borderline case before pricing or scheduling the pour."
            ),
        ],
        "sources": SRC,
    },
    "paver-patios": {
        "title": "Paver Patios in Ellenton, FL – Newer Lots",
        "meta": "Paver patios in Ellenton, FL often sit on housing built around 1988, newer than neighboring Palmetto or Bradenton; market range is " + price("paver-patio") + " per " + per("paver-patio") + ".",
        "h1": "Paver Patios and Walkways in Ellenton",
        "lede": capsule(
            "A paver patio in Ellenton costs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. "
            "Housing here skews newer than its river neighbors, which usually means fewer original-era obstacles to work around and more room to plan a patio from a clean slate."
        ),
        "sections": [
            (
                "Newer housing stock, simpler starting point",
                "<p>Census Reporter's current five-year estimate puts the median year an Ellenton home was built at 1988, roughly five years newer than the figure for both Palmetto and Bradenton across the river "
                + ext("http://censusreporter.org/profiles/16000US1220375-ellenton-fl/", "Census Reporter, Ellenton FL") + ". A patio project on that newer stock more often starts from a lot graded to modern drainage standards than from decades of settling and prior additions, which tends to simplify how a new paver surface ties into the existing slab or screen frame. Even on these newer lots, the county's no-permit list still applies the same way it does on an older parcel: a non-structural patio skips a permit, a structural one doesn't " + src("manatee-no-permit-list", "Manatee no-permit list") + ".</p>"
            ),
            (
                "A different kind of history next door",
                "<p>Not every Ellenton property dates to the 1980s. The Gamble Plantation house, built between 1845 and 1850 and now a state historic site on Patten Avenue, predates the surrounding subdivisions by well over a century "
                + ext("https://www.floridastateparks.org/parks-and-trails/judah-p-benjamin-confederate-memorial-gamble-plantation-historic-state-park/gamble", "Florida State Parks, Gamble Plantation") + ". A paver walkway or patio project near that older core of the community sometimes means working around mature landscaping and grade changes that a newer platted lot further out wouldn't have.</p>"
            ),
        ],
        "scenario": (
            "Say a 16 x 24 ft paver patio off a 1990s-built Ellenton home's lanai comes to 384 sq ft",
            "<p>Say a 16 x 24 ft paver patio off a 1990s-built Ellenton home's lanai comes to 384 sq ft. At " + price("paver-patio") + " per sq ft, that runs $3,840 to $6,528 across the full range, tightening to about $4,608 to $6,144 inside the typical " + price("paver-patio", typical=True) + " band depending on the paver chosen. Because the lot's grading dates to a newer build than much of the surrounding county, the drainage plan starts from a fairly clean baseline, and the non-structural patio addition stays on the county's no-permit list as long as it isn't tied into a new footer along the house.</p>"
        ),
        "faqs": [
            faq(
                "Is Ellenton's housing newer than Palmetto's or Bradenton's?",
                "On average, yes. Census Reporter's current estimate puts the median build year at 1988 in Ellenton against 1983 in both Palmetto and Bradenton, a gap that often means simpler, more standard-graded lots to build a patio on."
            ),
            faq(
                "Does a paver patio near the Gamble Plantation need special review?",
                "The state historic site itself is a separate property with its own protections; a nearby residential paver patio follows the same county permit rules as any other Ellenton address, not a historic-district process."
            ),
            faq(
                "Does a newer Ellenton lot still need a permit for a structural patio?",
                "Yes. The county's distinction between a non-structural patio and one poured with footers applies the same way regardless of when the surrounding subdivision was built."
            ),
        ],
        "sources": SRC,
    },
    "concrete-pool-decks": {
        "title": "Concrete Pool Decks in Ellenton, FL – 5-Ft Setback",
        "meta": "Concrete pool decks in Ellenton, FL must clear Manatee LDC 511.16's 5-foot setback from the lot line or shoreline; market range is " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ".",
        "h1": "Concrete Pool Deck Installation in Ellenton",
        "lede": capsule(
            "A concrete pool deck in Ellenton runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. "
            "County code sets a minimum 5-foot setback from the lot line or the shoreline for the deck itself, a line worth surveying before the forms go up on a tidal-river lot."
        ),
        "sections": [
            (
                "What LDC 511.16 actually requires",
                "<p>Manatee County's LDC sets a single setback for a pool, screen cage or an on-grade deck in a side or rear yard: 5 feet, measured from either the lot line or the shoreline, whichever applies, and the code treats none of those features as a yard encroachment at that distance "
                + src("manatee-ldc-511.16-pool-decks", "Manatee LDC Sec. 511.16") + ". On a lot backing up to the tidal Manatee River, that shoreline measurement runs from the water's edge rather than from a rear property line set back from it, which changes the usable footprint on a narrower waterfront parcel more than it would on an inland lot.</p>"
            ),
            (
                "Planning for a low, water-heavy CDP",
                "<p>Roughly a quarter of Ellenton's land area is open water, and the community sits at an average elevation near 13 feet "
                + ext("https://en.wikipedia.org/wiki/Ellenton,_Florida", "Ellenton, Florida") + ", figures that track with its position along the tidal Manatee River. FEMA's Zone AE and the higher-risk Coastal Zone VE both apply near the water here " + src("fema-coastal-firm", "FEMA flood zone designations") + ", and checking a specific parcel's designation before setting a deck's finished elevation is worth the call to the Flood Map Service Center, especially on a lot close enough to the river for the setback and the flood line to interact.</p>"
            ),
        ],
        "scenario": (
            "Say a 560 sq ft pool deck on an Ellenton lot backs up to the tidal Manatee River",
            "<p>Say a 560 sq ft pool deck on an Ellenton lot backs up to the tidal Manatee River. At " + price("concrete-pool-deck") + " per sq ft, figure $2,800 to $8,400 across the full range, tightening to about $3,920 to $6,720 inside the typical " + price("concrete-pool-deck", typical=True) + " band, the range depending on a plain broom finish versus a cool-touch textured coating. Because the rear property line sits along the river, the deck's edge has to clear LDC 511.16's 5-foot shoreline setback, and the parcel's flood zone gets checked before the slab's elevation is finalized, both steps ahead of what an inland Ellenton lot further from the water would need.</p>"
        ),
        "faqs": [
            faq(
                "How close can a pool deck sit to the water in Ellenton?",
                "No closer than 5 feet from the shoreline under LDC Sec. 511.16, the same minimum that applies from any side or rear lot line. The county's code specifically doesn't treat a pool deck at that distance as a yard encroachment."
            ),
            faq(
                "Is my Ellenton pool deck lot in a flood zone?",
                "Given how much of the CDP sits along the tidal Manatee River, it's worth checking directly. FEMA's Flood Map Service Center returns the AE or VE designation for a specific address before a deck's elevation is set."
            ),
            faq(
                "Does the 5-foot pool deck setback count against my buildable area?",
                "No. LDC 511.16 specifically states that a pool, screen enclosure, deck or patio built within that setback isn't considered a yard encroachment, unlike most other structures held to the same line."
            ),
        ],
        "sources": SRC,
    },
    "pool-deck-pavers": {
        "title": "Pool Deck Pavers in Ellenton, FL – River Salt",
        "meta": "Pool deck pavers near the tidal Manatee River in Ellenton, FL fall inside FDOT's marine-environment classification; market range is " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ".",
        "h1": "Travertine and Paver Pool Decks in Ellenton",
        "lede": capsule(
            "Pool deck pavers or travertine in Ellenton run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. "
            "The tidal stretch of the Manatee River that borders the community carries enough salt to shift how a deck's hardware and sealing schedule get specified."
        ),
        "sections": [
            (
                "Why a tidal river changes the hardware list",
                "<p>FDOT's structures manual classifies anything within 2,500 feet of water carrying 2,000 ppm chloride or more as a marine environment "
                + src("fdot-sdg", "FDOT marine-environment classification") + ", a threshold the tidal reach of the Manatee River meets along much of Ellenton's southern edge. Joint sand and an unsealed travertine surface both give out faster under that kind of exposure, which is why a deck going in close to the river gets a different sealer and edge-restraint spec than one a half-mile inland on higher ground would.</p>"
            ),
            (
                "The 5-foot setback still governs where the deck can go",
                "<p>Regardless of material, a pool deck on a riverfront Ellenton lot still has to clear LDC Sec. 511.16's 5-foot minimum setback from the shoreline "
                + src("manatee-ldc-511.16-pool-decks", "Manatee LDC Sec. 511.16") + ", and the compacted aggregate base underneath still gets sized for whatever soil sits beneath it, commonly Pomello or EauGallie across this part of the county, both of which call for extra base depth on the wetter end of their drainage range " + src("nrcs-pomello-osd", "NRCS Pomello soil series") + " " + src("nrcs-eaugallie-osd", "NRCS EauGallie soil series") + ".</p>"
            ),
        ],
        "scenario": (
            "Say a 620 sq ft travertine pool deck overlay goes in on an Ellenton lot a few hundred feet from the tidal river",
            "<p>Say a 620 sq ft travertine pool deck overlay goes in on an Ellenton lot a few hundred feet from the tidal river. At " + price("pool-deck-pavers") + " per sq ft, that spans $7,440 to $18,600 across the full range, tightening to about $8,680 to $13,640 inside the typical " + price("pool-deck-pavers", typical=True) + " band depending on stone grade and pattern. That distance puts the lot inside FDOT's chloride threshold, so the deck gets a salt-rated sealer and restraint hardware from the outset, and its footprint is still measured against the 5-foot shoreline setback before a single paver is laid.</p>"
        ),
        "faqs": [
            faq(
                "Does the Manatee River's salt content affect pool deck pavers in Ellenton?",
                "On a lot within FDOT's marine-environment threshold, roughly 2,500 feet of the tidal river, yes. Joint sand washes out and an unsealed surface stains faster there than it would further from the water."
            ),
            faq(
                "How close to the river can a paver pool deck be built in Ellenton?",
                "The same 5-foot minimum that applies to any pool deck under LDC Sec. 511.16, regardless of whether the finished surface is paver, travertine or poured concrete."
            ),
            faq(
                "Does the base under a riverfront pool deck need extra depth?",
                "Often, on Pomello or EauGallie soil common in the area, especially on the wetter end of either series' drainage range, which calls for a thicker compacted aggregate base than a well-drained inland lot needs."
            ),
        ],
        "sources": SRC,
    },
    "stamped-concrete": {
        "title": "Stamped Concrete in Ellenton, FL – I-75 Corridor",
        "meta": "Stamped concrete in Ellenton, FL near the I-75 Exit 224 corridor skips a county permit if non-structural; market range is " + price("stamped-concrete") + " per " + per("stamped-concrete") + ", Oct. 2026.",
        "h1": "Stamped Concrete Driveways and Patios in Ellenton",
        "lede": capsule(
            "Stamped concrete in Ellenton costs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October 2026. "
            "Growth along the I-75 Exit 224 corridor has brought newer subdivisions into the mix alongside the community's older plantation-era core, and the permit question comes down to the same structural-versus-non-structural line as plain concrete."
        ),
        "sections": [
            (
                "A newer corridor, the same county rule",
                "<p>Interstate 75 forms Ellenton's eastern boundary at Exit 224, and U.S. 301 carries traffic through the community's center toward Palmetto and Bradenton "
                + ext("https://en.wikipedia.org/wiki/Ellenton,_Florida", "Ellenton, Florida") + ", a corridor that has drawn newer residential development alongside older river-area parcels. A stamped pattern doesn't move a patio or driveway off the county's no-permit list if the underlying work is non-structural " + src("manatee-no-permit-list", "Manatee no-permit list") + ", and a stamped apron reaching into the right-of-way still needs the same access and drainage permit a plain one would " + src("manatee-ldc-1004.2-access-drainage-permit", "Manatee LDC Sec. 1004.2") + ".</p>"
            ),
            (
                "Timing the pour for color consistency",
                "<p>The Bradenton weather co-op station, the closest long-running rain gauge to Ellenton, averages 56.28 inches of rain a year, with August alone typically bringing more than 10 inches "
                + src("fcc-bradenton-normals", "FL Climate Center Bradenton normals") + ". A stamped surface holds its integral color most evenly when the release agent and texture go down on a dry, workable slab, so crews here plan around that wetter stretch of the calendar by starting early in the morning rather than risking a pattern set half under a clear sky and half under a passing shower.</p>"
            ),
        ],
        "scenario": (
            "Say a 280 sq ft stamped-concrete front entry and walkway goes in on a newer lot near the Exit 224 corridor",
            "<p>Say a 280 sq ft stamped-concrete front entry and walkway goes in on a newer lot near the Exit 224 corridor. At " + price("stamped-concrete") + " per sq ft, that comes to $2,240 to $5,320 across the full range, tightening to about $3,360 to $4,480 inside the typical " + price("stamped-concrete", typical=True) + " band depending on color and pattern complexity. Set back from the road on private ground, the walkway stays on the county's non-structural no-permit list, and the pour gets scheduled for an early start to keep the stamped texture's color consistent through a single dry window rather than split across a day interrupted by rain.</p>"
        ),
        "faqs": [
            faq(
                "Does stamped concrete need a permit in Ellenton?",
                "The same rule applies as plain concrete: a non-structural patio or walkway stays on the county's no-permit list, while a structural slab with footers, or any work in the right-of-way, needs a permit regardless of the finish."
            ),
            faq(
                "Has growth near I-75 Exit 224 changed how Ellenton permits are handled?",
                "No. Newer subdivisions along the corridor still follow the same Manatee County Land Development Code as the community's older river-area parcels; there's no separate process tied to the newer growth."
            ),
            faq(
                "Why does timing matter for a stamped-concrete pour in Ellenton?",
                "A stamped pattern holds its integral color most evenly when it's textured on a dry, workable surface, so crews favor early starts during the area's wetter months to avoid a pour interrupted partway through by rain."
            ),
        ],
        "sources": SRC,
    },
    "artificial-turf": {
        "title": "Artificial Turf in Ellenton, FL – Tidal Setback",
        "meta": "Artificial turf near the tidal Manatee River in Ellenton, FL follows the state's 10-foot water buffer; market range is " + price("artificial-turf") + " per " + per("artificial-turf") + ", Oct. 2026.",
        "h1": "Artificial Turf for Ellenton Yards",
        "lede": capsule(
            "Artificial turf in Ellenton runs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October 2026. "
            "On a lot backing up to the tidal Manatee River, which touches roughly a quarter of the community's total land area, the state's water buffer shapes the layout more than it would on an inland yard."
        ),
        "sections": [
            (
                "Reading the state rule against a water-heavy CDP",
                "<p>Florida Administrative Code Rule 62-308.100, in force since May 19, 2026, sets four conditions for residential synthetic turf statewide: a natural infill rather than crumb rubber, a washed-rock base, no irrigation line run beneath the surface, and a minimum 10-foot gap from the edge of a water body unless a seawall sits on that property line "
                + src("dep-rule", "DEP Rule 62-308.100") + ". With water covering an estimated quarter of Ellenton's land area " + ext("https://en.wikipedia.org/wiki/Ellenton,_Florida", "Ellenton, Florida") + ", that last condition reaches more yards here than it would in a community further from the river. F.S. 125.572 keeps local government from tightening that statewide floor any further on a single-family lot " + src("fs125572", "F.S. 125.572") + ".</p>"
            ),
            (
                "Skipping the county's weekly sprinkler schedule",
                "<p>Manatee County's current order holds the area to SWFWMD's Modified Phase III restrictions through March 31, 2027, one sprinkler day a week inside a pre-dawn or evening window "
                + src("manatee-phase3", "Manatee Modified Phase III order") + " " + src("swfwmd-restrictions", "SWFWMD district restrictions") + ". A turf lawn is done needing that schedule once it's installed and watered in, a swap weighed in more depth in " + compare("artificial-turf-vs-sod", "our turf-versus-sod comparison") + ". A section of turf a neighbor or the street can't see is also shielded from most HOA restrictions by F.S. 720.3045, current as of 2026 " + src("fs720-3045", "F.S. 720.3045") + ".</p>"
            ),
        ],
        "scenario": (
            "Say a 700 sq ft backyard turf project sits roughly 25 ft back from the tidal Manatee River on an Ellenton lot",
            "<p>Say a 700 sq ft backyard turf project sits roughly 25 ft back from the tidal Manatee River on an Ellenton lot. At " + price("artificial-turf") + " per sq ft, that spans $7,000 to $17,500 across the full range, tightening to about $8,400 to $12,600 inside the typical " + price("artificial-turf", typical=True) + " band depending on pile height and backing. At 25 feet, the layout clears the state's 10-foot water buffer with margin, though the washed-base and natural-infill specs still apply the same way they would on a yard nowhere near the river, and no irrigation line can run underneath the finished turf.</p>"
        ),
        "faqs": [
            faq(
                "How far from the Manatee River does turf have to sit in Ellenton?",
                "At least 10 feet from the water's edge under Florida's turf rule, unless the property line there is a seawall, which removes the buffer requirement entirely."
            ),
            faq(
                "Does turf avoid Manatee County's current watering order?",
                "Yes. The county's order governs sprinkler irrigation on a weekly schedule through March 2027; a turf lawn stops needing watering altogether once it's installed, so the order no longer applies to it."
            ),
            faq(
                "Why does Ellenton's water coverage matter for turf layout?",
                "With open water making up a sizeable share of the community's land area along the tidal river, more Ellenton yards run into the state's 10-foot water-body setback than would be typical in an inland town."
            ),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
