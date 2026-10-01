# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, compare, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "bradenton"

SRC = [
    "census-pep-v2025",
    "acs-bradenton",
    "bradenton-city",
    "bradenton-lur-4.1-access-sidewalks",
    "bradenton-lur-2.2-zoning-permit",
    "bradenton-lur-3.2-isr",
    "bradenton-lur-5.1-retaining-walls",
    "bradenton-driveway-affidavit",
    "bradenton-impervious-worksheet",
    "bradenton-permitting",
    "manatee-ldc-1004.2-access-drainage-permit",
    "manatee-driveway-culvert-service",
    "manatee-no-permit-list",
    "manatee-phase3",
    "swfwmd-restrictions",
    "fema-coastal-firm",
    "fdot-sdg",
    "nrcs-eaugallie-osd",
    "nrcs-immokalee-osd",
    "nrcs-felda-osd",
    "nrcs-myakka-osd",
    "nrcs-pomello-osd",
    "dep-rule",
    "fs125572",
    "fs720-3045",
    ("City of Bradenton, Floodplain Management Program", "https://cityofbradenton.com/index.asp?SEC=412EC4AA-2923-4330-993A-BE48C0576144&DE=CDCFD067-8988-4FEA-9708-F5E8D69955CD"),
    ("Wikipedia, West Bradenton, Florida", "https://en.wikipedia.org/wiki/West_Bradenton,_Florida"),
    ("Wikipedia, Palma Sola Bay", "https://en.wikipedia.org/wiki/Palma_Sola_Bay"),
]

HUB = page(
    "/bradenton-fl/", "city",
    "Concrete & Paver Contractor in Bradenton, FL",
    "Opera builds concrete driveways, pavers and turf in Bradenton, FL, where Public Works reviews curb cuts under LUR 4.1 and homes date to 1983, as of October 2026.",
    "Concrete, Pavers and Turf Built for Bradenton Homes",
    capsule(
        "Opera's Sarasota unit builds concrete driveways, pavers, pool decks and artificial turf in Bradenton, about 12 miles from the crew's Sarasota base, where the Census Bureau counted 58,014 residents in July 2025 and the median home dates to 1983. "
        "As of October 2026, the city's Public Works director signs off on driveway curb cuts, a zoning permit covers any paved area, and Manatee County has the city on a once-a-week watering schedule."
    ),
    "".join([
        sec(
            "Which office in Bradenton reviews a new driveway or curb cut?",
            "<p>Public Works, through the director's own sign-off under LUR §4.1.4.3: \"Curb cuts in public rights-of-way are subject to the review and approval of the director of public works,\" with a state or county road adding that agency's approval on top "
            + src("bradenton-lur-4.1-access-sidewalks") + ". A home with up to six units gets one driveway per street frontage, a single access point tops out at 24 feet wide, and a circular drive is allowed only at 12 feet per curb cut with at least 25 feet between the two cuts. "
            "Before a crew touches the right-of-way, a signed Driveway/Sidewalk Affidavit & Indemnification Agreement has to be on file with Public Works & Utilities at 1411 9th St W, and the homeowner, not the city, stays on the hook to maintain or relocate the work later if the city asks "
            + src("bradenton-driveway-affidavit") + ". Building, widening or repaving a \"street, driveway, access road, or parking area\" also needs its own zoning permit with a scaled site plan under LUR §2.2.1, a step separate from the right-of-way review "
            + src("bradenton-lur-2.2-zoning-permit") + ". A few blocks west of the city line, homes in the unincorporated West Bradenton community answer to Manatee County's own access and drainage permit instead "
            + ext("https://en.wikipedia.org/wiki/West_Bradenton,_Florida", "West Bradenton, Florida") + "; " + post("manatee-county-driveway-permits", "our Manatee County permit guide") + " covers both sides of that line in detail.</p>"
        ),
        sec(
            "How much of a Bradenton lot can be covered in concrete, pavers or a pool deck?",
            "<p>The city caps impervious surface ratio (ISR) by zoning district, and the definition reaches well past the driveway: \"building footprint, paved drives, paved terraces, impervious decks, swimming pools, and other impervious surfaces\" all draw from the same percentage "
            + src("bradenton-lur-3.2-isr") + ".</p>"
            + table(
                "City of Bradenton maximum impervious surface ratio by district",
                ["Zoning district", "Max. impervious coverage"],
                [["R-1", "50%"], ["R-2", "60%"], ["R-3", "70%"], ["UV", "70%"], ["R-4", "70%"]],
                "Source: Bradenton LUR §3.2, checked October 2026. The city provides an Impervious Coverage Calculation worksheet to total a lot's existing and proposed hard surfaces " + src("bradenton-impervious-worksheet") + "."
            )
            + "<p>A driveway, a " + svc("concrete-patios", "patio") + ", a " + svc("concrete-pool-decks", "pool deck") + " and a paver walkway all pull from that same cap, so a lot already close to its district's limit is worth running through the worksheet before a new project gets designed, not after the forms are ordered.</p>"
        ),
        sec(
            "What does a 1983 median build year mean for a Bradenton project?",
            "<p>The Census Bureau counted 58,014 Bradenton residents on July 1, 2025, and the American Community Survey's five-year estimate puts the median year a home here was built at 1983 "
            + src("census-pep-v2025") + " " + src("acs-bradenton") + ", newer than Sarasota's 1976 median but decades older than Lakewood Ranch's 2014. A lot of original driveways and patio slabs from the early 1980s are now at the point where a crack gets patched for the second or third time, past where "
            + svc("concrete-repair", "resurfacing") + " usually makes more sense than another patch, and a pool cage added a decade or two after the original build often left the surrounding concrete sized for a smaller deck than homeowners want now. The city still markets itself as \"The Friendly City\" "
            + src("bradenton-city") + ", and its housing mix runs from older river-corridor blocks to newer platted subdivisions toward the county line, each aging a little differently.</p>"
        ),
        sec(
            "What do the Manatee River and Palma Sola Bay change for a build near the water?",
            "<p>Bradenton sits on the Manatee River, and the city's own floodplain program names Riverview Boulevard and East Riverside Drive, both along the river, among the stretches it flags for residents checking their flood risk "
            + ext("https://cityofbradenton.com/index.asp?SEC=412EC4AA-2923-4330-993A-BE48C0576144&DE=CDCFD067-8988-4FEA-9708-F5E8D69955CD", "City of Bradenton, Floodplain Management Program") + ". FEMA's coastal maps split that risk two ways nearby: Zone AE assumes roughly a one-in-a-hundred yearly flood chance with modest wave action, while the higher-hazard Zone VE assumes the same odds plus surf capable of damaging a structure during a major storm "
            + src("fema-coastal-firm") + ". Bradenton takes part in the National Flood Insurance Program and offers a flood zone determination by phone at no cost. West of downtown, the unincorporated West Bradenton community runs along Palma Sola Bay, a shallow inlet off Anna Maria Sound "
            + ext("https://en.wikipedia.org/wiki/Palma_Sola_Bay", "Palma Sola Bay") + ", where FDOT's own marine-environment line, any structure within 2,500 feet of water carrying more than 2,000 ppm chloride, describes most of the shoreline "
            + src("fdot-sdg") + ". A " + svc("retaining-walls", "retaining wall") + " or a low " + svc("pool-deck-pavers", "paver pool deck") + " near either the river or the bay is worth checking against the current flood map before forms go up.</p>"
        ),
        sec(
            "How does the current watering order affect sod, turf and new concrete here?",
            "<p>Manatee County confirmed on September 22, 2026 that it keeps following the Southwest Florida Water Management District's Modified Phase III Extreme Water Shortage order through March 31, 2027 "
            + src("manatee-phase3") + ".</p>"
            + table(
                "SWFWMD Modified Phase III watering day by last address digit (checked October 2026)",
                ["Last digit of address", "Watering day"],
                [["0 or 1", "Monday"], ["2 or 3", "Tuesday"], ["4 or 5", "Wednesday"], ["6 or 7", "Thursday"], ["8 or 9", "Friday"]],
                "One day a week, between 12:01 and 4 a.m. or between 8 p.m. and 11:59 p.m. " + src("swfwmd-restrictions")
            )
            + "<p>The county's own notice allows hand-watering and micro-irrigation daily before 8 a.m. or after 6 p.m. even under the order, and sets fines of $100, $250 and $500 for a first, second and third violation "
            + src("manatee-phase3") + ". New sod still gets a grace period, daily water for its first 30 days, a window that overlaps with the hand-watering a freshly poured driveway or patio slab needs while it cures. "
            + svc("artificial-turf") + " sits outside the order entirely once it's installed; the trade-off is worked out in " + compare("artificial-turf-vs-sod", "artificial turf vs sod in Florida") + ".</p>"
        ),
    ]) + "<!--AUTO:city-services-->",
    faqs=[
        faq(
            "Do you work in unincorporated West Bradenton, not just inside the city line?",
            "Yes, the Sarasota unit serves West Bradenton along with the incorporated city. The difference is which office reviews the driveway: a city curb cut goes through the Public Works director under LUR §4.1, while West Bradenton, part of unincorporated Manatee County, uses the county's access and drainage permit instead."
        ),
        faq(
            "Do I need a permit for a straight driveway replacement in Bradenton?",
            "Yes. Building, altering or repaving a driveway needs a zoning permit with a scaled site plan under LUR §2.2.1, and any part of the work in the public right-of-way also needs a signed Driveway/Sidewalk Affidavit on file with Public Works & Utilities."
        ),
        faq(
            "How much of my Bradenton lot can be covered in hardscape?",
            "It depends on the zoning district: the city's impervious surface ratio caps coverage at 50% in R-1, 60% in R-2, and 70% in R-3, UV and R-4, counting the driveway, patio, pool deck and roof together. The city's own worksheet totals the percentage before a permit is filed."
        ),
        faq(
            "Is my Bradenton address in a flood zone near the river or the bay?",
            "Possibly, especially along the Manatee River or in the West Bradenton streets that back onto Palma Sola Bay. FEMA's Zone AE assumes roughly a one-in-a-hundred yearly flood chance with modest waves; the higher-hazard Zone VE assumes the same odds with surf that can damage a low structure."
        ),
        faq(
            "Does artificial turf save water under Bradenton's current restrictions?",
            "It sidesteps them. Manatee County's Modified Phase III order limits irrigation to one day a week in a pre-dawn or late-night window through March 2027, a schedule sod has to live with and turf does not once it's installed and watered in."
        ),
        faq(
            "How do you find the best concrete contractor in Bradenton?",
            "Check the contractor on the state's license-verification tool, confirm the quote accounts for the city's zoning permit or the county's access and drainage permit depending on which side of the line your lot sits, and ask how the bid handles the local water table. "
            + post("how-to-choose-a-concrete-contractor-sarasota", "Our guide to choosing a concrete contractor") + " covers the rest."
        ),
    ],
    sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Bradenton",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/manatee-county-driveway-permits/", "Driveway and patio permits in Bradenton, Lakewood Ranch and Palmetto"),
        ("/sarasota-fl/", "Concrete, pavers and turf in Sarasota"),
        ("/lakewood-ranch-fl/", "Concrete, pavers and turf in Lakewood Ranch"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Bradenton, FL",
)

LOCAL = {
    "concrete-driveways": {
        "title": "Concrete Driveways in Bradenton, FL – ROW Rules",
        "meta": "Concrete driveways in Bradenton, FL need a Public Works curb cut review and a zoning permit under LUR 2.2; market range is " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", October 2026.",
        "h1": "Concrete Driveway Installation in Bradenton",
        "lede": capsule(
            "A new or replacement concrete driveway in Bradenton runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026, before the portion in the right-of-way, which the Public Works director reviews separately. "
            "Many driveways here date to the city's 1983 median build year, old enough that a straight repour is as common as a first installation."
        ),
        "sections": [
            (
                "Two city approvals for one driveway",
                "<p>A Bradenton driveway touches two separate reviews before a crew pours anything. The curb cut itself needs the Public Works director's sign-off under LUR §4.1.4.3, capped at 24 feet wide for a single access point, with a circular drive limited to 12 feet per cut and at least 25 feet between two cuts on the same lot "
                + src("bradenton-lur-4.1-access-sidewalks") + ". The driveway as a whole also needs a zoning permit with a scaled site plan under LUR §2.2.1, since the code names \"driveway, access road, or parking area\" directly among the work that requires one "
                + src("bradenton-lur-2.2-zoning-permit") + ". Before the crew reaches the right-of-way, a signed Driveway/Sidewalk Affidavit has to be on file with Public Works & Utilities, putting the ongoing maintenance obligation on the homeowner rather than the city "
                + src("bradenton-driveway-affidavit") + ".</p>"
            ),
            (
                "Why the subgrade gets checked before the slab thickness does",
                "<p>Bradenton lots commonly sit on EauGallie or Felda soil, both poorly drained, with EauGallie holding a seasonal high water table within a foot and a half of the surface for part of the year and Felda running wetter still, within about a foot for two to six months "
                + src("nrcs-eaugallie-osd") + " " + src("nrcs-felda-osd") + ". Florida's residential code limits clean fill under a slab to 24 inches of sand or gravel and 8 inches of earth without an engineer's sign-off, with at least 4 inches of compacted base under the slab itself. On a driveway sized for a loaded trailer or a dual-axle work truck, we plan the section around that wet subgrade rather than assume a dry-ridge base will carry the same load the same way.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 20 x 24 ft two-car driveway, 480 sq ft, original to a 1983 Bradenton home with diagonal cracking near the garage",
            "<p>Say you have a 20 x 24 ft two-car driveway, 480 sq ft, original to a 1983 Bradenton home with diagonal cracking near the garage. At the market range of " + price("concrete-driveway") + " per sq ft, a full tear-out and repour runs $2,880 to $7,200, narrowing to roughly $3,840 to $5,760 in the typical " + price("concrete-driveway", typical=True) + " band. That figure covers the private slab only; the apron at the street needs its own Public Works review under LUR §4.1, and the Driveway/Sidewalk Affidavit has to be signed before the old apron comes out. If the lot sits a few blocks west in the unincorporated West Bradenton community instead, the same job goes through Manatee County's access and drainage permit rather than the city's zoning review.</p>"
        ),
        "faqs": [
            faq(
                "Does a straight driveway replacement in Bradenton need a city permit?",
                "Yes, two of them in most cases: a zoning permit under LUR §2.2.1 for the driveway itself, and the Public Works director's review of the curb cut where it meets the street, plus a signed Driveway/Sidewalk Affidavit for any work in the right-of-way."
            ),
            faq(
                "How wide can a Bradenton driveway be at the street?",
                "A single access point is capped at 24 feet wide under LUR §4.1.4.3. A circular drive is allowed at up to 12 feet per curb cut, with at least 25 feet required between the two cuts on the same lot."
            ),
            faq(
                "Why does Bradenton's soil matter for a driveway base?",
                "EauGallie and Felda, two common soils under Bradenton driveways, both run poorly drained with a seasonal high water table within a foot or two of the surface for part of the year, which changes how much base a heavily loaded driveway needs compared with a dry-ridge lot."
            ),
        ],
        "sources": SRC,
    },
    "paver-driveways": {
        "title": "Paver Driveways in Bradenton, FL – ISR Math",
        "meta": "Paver driveways in Bradenton, FL count toward the city's impervious surface ratio under LUR 3.2; market range is " + price("paver-driveway") + " per " + per("paver-driveway") + ", Oct. 2026.",
        "h1": "Paver Driveway Installation in Bradenton",
        "lede": capsule(
            "A paver driveway in Bradenton runs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026, and every square foot counts toward the city's impervious surface ratio the same as poured concrete would. "
            "On a lot near Palma Sola Bay, salt air also shapes which base and edge-restraint hardware holds up best."
        ),
        "sections": [
            (
                "Pavers don't get a pass on the impervious cap",
                "<p>Bradenton's LUR §3.2 defines impervious surface broadly enough to catch a paver driveway the same way it catches poured concrete: \"building footprint, paved drives, paved terraces, impervious decks, swimming pools, and other impervious surfaces\" "
                + src("bradenton-lur-3.2-isr") + ". The district caps run from 50% in R-1 up to 70% in R-3, UV and R-4, and the city's own worksheet totals a lot's existing coverage against the proposed addition " + src("bradenton-impervious-worksheet") + ". A homeowner widening a two-car driveway to three cars on a tight R-1 lot should run that math before ordering pavers, since the zoning permit required under LUR §2.2.1 will ask for the same figure " + src("bradenton-lur-2.2-zoning-permit") + ".</p>"
            ),
            (
                "Building a paver base on wet flatwoods ground",
                "<p>Myakka and Pomello, two soils found across Manatee County, sit at opposite ends of the drainage spectrum: Myakka holds a seasonal high water table less than a foot and a half deep for part of most years, while Pomello drains somewhat better, with water typically a foot and a half to four feet down "
                + src("nrcs-myakka-osd") + " " + src("nrcs-pomello-osd") + ". ICPI's paver spec calls for at least 6 inches of compacted base on well-drained ground, 2 to 4 inches more where the soil runs wet or weak, which on a Myakka lot is closer to the rule than the exception. On a lot bordering Palma Sola Bay, we also favor edge restraints and fastener hardware rated for salt exposure, since FDOT treats anything within 2,500 feet of water above 2,000 ppm chloride as a marine environment " + src("fdot-sdg") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have an 18 x 40 ft two-car paver driveway, 720 sq ft, on a West Bradenton lot a few blocks from Palma Sola Bay",
            "<p>Say you have an 18 x 40 ft two-car paver driveway, 720 sq ft, on a West Bradenton lot a few blocks from Palma Sola Bay. At the market range of " + price("paver-driveway") + " per sq ft, that runs $7,200 to $21,600, narrowing to roughly $8,640 to $14,400 in the typical " + price("paver-driveway", typical=True) + " band depending on paver type and base depth. Because the lot sits in unincorporated West Bradenton rather than inside the city line, the access and drainage permit comes from Manatee County rather than the city's zoning office, and because the bay is close by, the edge restraint spec steps up a grade from what an inland Bradenton lot would need.</p>"
        ),
        "faqs": [
            faq(
                "Do pavers count the same as concrete for Bradenton's impervious limit?",
                "Yes. LUR §3.2 defines impervious surface broadly enough to include paved drives regardless of material, so a paver driveway draws from the same percentage cap as a poured one would on the same lot."
            ),
            faq(
                "Does a paver driveway near Palma Sola Bay need different hardware?",
                "It's worth it. FDOT treats any structure within 2,500 feet of water above 2,000 ppm chloride as a marine environment, which describes much of the shoreline along the bay, so we spec edge restraints and fasteners rated for salt exposure on those lots."
            ),
            faq(
                "Is the paver driveway permit different in West Bradenton than inside the city?",
                "Yes. West Bradenton is unincorporated Manatee County, so the driveway goes through the county's access and drainage permit rather than the city's zoning permit and Public Works curb cut review that apply inside the Bradenton city line."
            ),
        ],
        "sources": SRC,
    },
    "concrete-patios": {
        "title": "Concrete Patios in Bradenton, FL – ISR & Permits",
        "meta": "Concrete patios in Bradenton, FL count toward LUR 3.2 coverage and need a zoning permit, unlike unincorporated Manatee County; range " + price("concrete-patio") + " per " + per("concrete-patio") + ".",
        "h1": "Concrete Patio Installation in Bradenton",
        "lede": capsule(
            "A concrete patio in Bradenton runs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. Unlike unincorporated Manatee County, which exempts a non-structural patio outright, "
            "the city counts a patio toward its impervious surface cap and folds it into the same zoning permit as a driveway."
        ),
        "sections": [
            (
                "Why the city treats a patio differently from the county",
                "<p>In unincorporated Manatee County, the current \"What Does Not Require a Permit\" list puts a non-structural concrete or paver patio in the no-permit column "
                + src("manatee-no-permit-list") + ". Inside the Bradenton city line, that exemption doesn't carry over: there is no published flatwork exemption, so a patio counts toward impervious surface ratio and falls under the same zoning permit rule LUR §2.2.1 applies to any paved area " + src("bradenton-lur-2.2-zoning-permit") + " " + src("bradenton-lur-3.2-isr") + ". A homeowner who moved from Parrish or Myakka City and remembers a patio going in without a permit there is describing the county's rule, not the city's.</p>"
            ),
            (
                "Fitting a patio into the ISR worksheet",
                "<p>Because \"impervious decks\" and \"paved terraces\" are both named in the city's own definition " + src("bradenton-lur-3.2-isr") + ", a patio addition has to be totaled against whatever the lot's driveway, roof and any " + svc("pool-deck-pavers", "pool deck") + " already use, with the Impervious Coverage Calculation worksheet doing that math " + src("bradenton-impervious-worksheet") + ". On a 1983-era lot where the original patio was sized for a smaller pool cage than what's there now, that worksheet step often decides how large a replacement patio can get before the design has to shrink or a different district's cap comes into play.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 14 x 16 ft patio extension, 224 sq ft, off a screened pool cage added a decade after the home's 1983 construction",
            "<p>Say you have a 14 x 16 ft patio extension, 224 sq ft, off a screened pool cage added a decade after the home's 1983 construction. At the market range of " + price("concrete-patio") + " per sq ft, that runs $1,344 to $2,912, or roughly $1,568 to $2,240 in the typical " + price("concrete-patio", typical=True) + " band for a broom-finished slab. Before the pour, the new square footage gets added to the lot's existing driveway and pool deck coverage against the district's ISR cap, and the zoning permit required under LUR §2.2.1 covers that addition even though the same scope would likely be exempt a few miles away in unincorporated Manatee County.</p>"
        ),
        "faqs": [
            faq(
                "Does a small concrete patio need a permit in Bradenton?",
                "Yes. Unlike unincorporated Manatee County, which exempts a non-structural patio, Bradenton has no published flatwork exemption, so a patio counts toward the lot's impervious surface ratio and needs the same zoning permit LUR §2.2.1 requires for any paved area."
            ),
            faq(
                "Will a new patio push my Bradenton lot over its coverage limit?",
                "It can, especially on a lot that already carries a full driveway and pool deck. The city's Impervious Coverage Calculation worksheet totals the existing hardscape against the district's cap before a patio design is finalized."
            ),
            faq(
                "Is a patio treated differently in West Bradenton than inside the city?",
                "Yes. West Bradenton is unincorporated Manatee County, where a non-structural patio is currently exempt from a building permit outright, a looser rule than the city's zoning-permit-and-ISR approach inside the Bradenton line."
            ),
        ],
        "sources": SRC,
    },
    "paver-patios": {
        "title": "Paver Patios in Bradenton, FL – 1980s Pool Cages",
        "meta": "Paver patios in Bradenton, FL often extend a 1980s pool cage and count toward LUR 3.2 coverage; market range is " + price("paver-patio") + " per " + per("paver-patio") + ", Oct. 2026.",
        "h1": "Paver Patios and Walkways in Bradenton",
        "lede": capsule(
            "A paver patio in Bradenton runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. With a median home here built in 1983, "
            "a lot of patio work is an addition to a pool cage that came later, tied into an edge that was never meant to carry pavers."
        ),
        "sections": [
            (
                "Extending a patio past a 1980s-era pool cage",
                "<p>Bradenton's median year structure built is 1983 " + src("acs-bradenton") + ", and plenty of those homes added a screened pool cage sometime after the original construction, with a concrete patio poured to the cage's footprint at the time. A paver patio extension past that original edge usually means tying a new edge restraint into the existing slab rather than pouring fresh concrete under the screen frame, and the added footprint still counts toward the lot's impervious surface ratio under LUR §3.2, the same as any other hardscape on the property " + src("bradenton-lur-3.2-isr") + ". " + svc("concrete-patios", "Plain concrete") + " covers the alternative version of the same addition.</p>"
            ),
            (
                "What proximity to the Manatee River or Palma Sola Bay changes",
                "<p>Homes along Riverview Boulevard or East Riverside Drive, both of which the city's floodplain program flags for flood risk along the Manatee River " + ext("https://cityofbradenton.com/index.asp?SEC=412EC4AA-2923-4330-993A-BE48C0576144&DE=CDCFD067-8988-4FEA-9708-F5E8D69955CD", "City of Bradenton, Floodplain Management Program") + ", and lots in West Bradenton along Palma Sola Bay, sit close enough to open water that FDOT's marine-environment line, within 2,500 feet of water above 2,000 ppm chloride, applies to most of them " + src("fdot-sdg") + ". That doesn't change how the paver base gets built, but it does change how soon a sealer or a metal edge restraint starts showing wear, which is why we weigh hardware choices differently on a patio that close to the water.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 16 x 20 ft paver patio extension, 320 sq ft, off a screened lanai along East Riverside Drive near the Manatee River",
            "<p>Say you have a 16 x 20 ft paver patio extension, 320 sq ft, off a screened lanai along East Riverside Drive near the Manatee River. At the market range of " + price("paver-patio") + " per sq ft, that runs $3,200 to $5,440, or roughly $3,840 to $5,120 in the typical " + price("paver-patio", typical=True) + " band depending on the paver and pattern. Because the street sits among the ones the city's floodplain program flags along the river, we check the current flood map before setting the finished grade, and the new patio's footprint still gets added to the home's existing impervious total before the zoning permit is filed.</p>"
        ),
        "faqs": [
            faq(
                "Can a paver patio be added to an existing 1980s pool cage in Bradenton?",
                "Usually, by tying a new edge restraint into the original slab at the cage's footprint rather than pouring under the existing screen frame. The added square footage still has to be counted against the lot's impervious surface ratio."
            ),
            faq(
                "Does being near the Manatee River change how a paver patio is built?",
                "It doesn't change the base, but a lot along a street like Riverview Boulevard or East Riverside Drive is worth checking against the current flood map first, and salt exposure near the water can mean upgrading the edge restraint and fastener hardware."
            ),
            faq(
                "Do I need a permit for a paver patio addition in Bradenton?",
                "Yes, inside the city line. Bradenton has no published exemption for patio flatwork, so the addition counts toward impervious surface ratio and needs the same zoning permit a driveway or parking area would."
            ),
        ],
        "sources": SRC,
    },
    "concrete-pool-decks": {
        "title": "Concrete Pool Decks in Bradenton, FL – Flood Zones",
        "meta": "Concrete pool decks in Bradenton, FL count toward LUR 3.2 coverage and sit near FEMA Zone AE or VE on riverfront lots; range " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ".",
        "h1": "Concrete Pool Deck Installation in Bradenton",
        "lede": capsule(
            "A concrete pool deck in Bradenton runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. Riverfront lots near the Manatee River "
            "and some West Bradenton streets along Palma Sola Bay sit in a FEMA flood zone, which changes how fill and drainage get handled at the slab's edge."
        ),
        "sections": [
            (
                "A pool deck counts toward the lot's impervious cap by name",
                "<p>Bradenton's LUR §3.2 lists \"swimming pools\" and \"impervious decks\" separately in its definition of impervious surface, so a pool deck draws from the same percentage cap as the driveway and roof, not a different allowance " + src("bradenton-lur-3.2-isr") + ". The district caps run from 50% in R-1 to 70% in R-3, UV and R-4, and the city's worksheet totals the lot's existing coverage against a proposed deck before the permit is filed " + src("bradenton-impervious-worksheet") + ". On a lot that already carries a full driveway and a " + svc("paver-patios", "paver patio") + ", that math is worth running before the pool contractor finalizes a deck size, not after.</p>"
            ),
            (
                "Flood zones along the river and the bay",
                "<p>FEMA's coastal maps sort nearby lots into two main categories: Zone AE, a roughly one-in-a-hundred yearly flood chance with modest wave action, and the higher-hazard Zone VE, the same odds but with surf capable of damaging a low structure during a major storm " + src("fema-coastal-firm") + ". The city's own floodplain program names Riverview Boulevard and East Riverside Drive, both along the Manatee River, among the areas it flags for residents checking their risk " + ext("https://cityofbradenton.com/index.asp?SEC=412EC4AA-2923-4330-993A-BE48C0576144&DE=CDCFD067-8988-4FEA-9708-F5E8D69955CD", "City of Bradenton, Floodplain Management Program") + ", and the city offers a no-cost flood zone determination by phone before a deck's finished elevation gets set.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 700 sq ft pool deck around a screened cage on a lot a few blocks off the Manatee River",
            "<p>Say you have a 700 sq ft pool deck around a screened cage on a lot a few blocks off the Manatee River. At the market range of " + price("concrete-pool-deck") + " per sq ft, that runs $3,500 to $10,500, narrowing to roughly $4,900 to $8,400 in the typical " + price("concrete-pool-deck", typical=True) + " band for a broom or spray-textured finish with slope to a drain. Because the street sits close enough to the river to warrant a flood map check, the deck's edge and any fill under it get built with the current flood zone in mind, and the finished square footage gets added to the lot's existing coverage against the district's ISR cap before the permit is filed.</p>"
        ),
        "faqs": [
            faq(
                "Is my Bradenton pool deck lot in a flood zone?",
                "Possibly, especially near the Manatee River or in West Bradenton streets along Palma Sola Bay. The city's floodplain program names Riverview Boulevard and East Riverside Drive among the areas it flags, and the city offers a free flood zone determination by phone."
            ),
            faq(
                "Does a pool deck count toward Bradenton's impervious surface limit?",
                "Yes. The city's LUR §3.2 names swimming pools and impervious decks directly in its coverage definition, so a pool deck draws from the same percentage cap as the driveway and roof on the same lot."
            ),
            faq(
                "Does FEMA's Zone VE ban a pool deck near the water?",
                "No, but it changes how fill and drainage at the slab's edge get handled, since Zone VE assumes surf capable of damaging a low structure during a major storm, a higher bar than the more common Zone AE designation."
            ),
        ],
        "sources": SRC,
    },
    "pool-deck-pavers": {
        "title": "Pool Deck Pavers in Bradenton, FL – Salt Air",
        "meta": "Pool deck pavers near Palma Sola Bay in Bradenton, FL face FDOT's marine-environment salt criterion; market range is " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ", Oct. 2026.",
        "h1": "Travertine and Paver Pool Decks in Bradenton",
        "lede": capsule(
            "Pool deck pavers or travertine in Bradenton run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. On lots along Palma Sola Bay in West Bradenton, "
            "salt air off the water shapes the sealer and hardware choice more than it does on an inland driveway or patio."
        ),
        "sections": [
            (
                "Why a bayfront deck needs different hardware",
                "<p>FDOT draws its own marine-environment line at 2,500 feet from water above 2,000 ppm chloride, and a paver or travertine pool deck that close to Palma Sola Bay, a shallow inlet off Anna Maria Sound in West Bradenton " + ext("https://en.wikipedia.org/wiki/Palma_Sola_Bay", "Palma Sola Bay") + ", sits in that same salt-heavy air " + src("fdot-sdg") + ". Salt accelerates how fast joint sand washes out and how quickly an unsealed surface shows staining, which is why we check how close a lot sits to the bay before recommending a resealing interval rather than quoting the same schedule for every Bradenton address.</p>"
            ),
            (
                "Counting the deck against the lot's coverage cap",
                "<p>Whether the deck is on the mainland or along the bay, it still draws from the same impervious surface ratio the city applies to a driveway or patio, since \"swimming pools\" and \"impervious decks\" are both named in LUR §3.2's definition " + src("bradenton-lur-3.2-isr") + ". On a West Bradenton lot, that review runs through Manatee County's own process rather than the city's, since the community sits in unincorporated territory, though the underlying math, totaling the deck against the roof and driveway, works the same way either side of the line.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 750 sq ft travertine pool deck overlay on a West Bradenton lot a few hundred feet from Palma Sola Bay",
            "<p>Say you have a 750 sq ft travertine pool deck overlay on a West Bradenton lot a few hundred feet from Palma Sola Bay. At the market range of " + price("pool-deck-pavers") + " per sq ft, that runs $9,000 to $22,500, or roughly $10,500 to $16,500 in the typical " + price("pool-deck-pavers", typical=True) + " band depending on the stone and pattern. Because the lot sits well inside FDOT's 2,500-foot marine-environment line, we spec a sealer and edge restraint rated for salt exposure rather than the standard inland hardware, and plan the resealing interval shorter than we would for a deck a mile or two from open water.</p>"
        ),
        "faqs": [
            faq(
                "Does salt air near Palma Sola Bay change how a pool deck paver job is built?",
                "It doesn't change the base, but it does change the sealer and edge-restraint hardware we spec, and how often resealing comes up, since FDOT treats anything within 2,500 feet of water above 2,000 ppm chloride as a marine environment."
            ),
            faq(
                "Is a pool deck paver permit different in West Bradenton than inside the city?",
                "Yes, since West Bradenton is unincorporated Manatee County, the review runs through the county rather than the City of Bradenton's zoning office, though both apply a similar impervious-coverage calculation to the finished deck."
            ),
            faq(
                "How often does a bayfront paver pool deck need resealing in Bradenton?",
                "More often than an inland one, as a rule of thumb, since salt accelerates joint-sand washout and surface staining. We check a lot's distance from Palma Sola Bay or the Manatee River before setting a resealing interval rather than using one schedule for every address."
            ),
        ],
        "sources": SRC,
    },
    "stamped-concrete": {
        "title": "Stamped Concrete in Bradenton, FL – Riverfront Lots",
        "meta": "Stamped concrete in Bradenton, FL works around the city's ISR cap on riverfront lots near Riverview Boulevard; market range is " + price("stamped-concrete") + " per " + per("stamped-concrete") + ".",
        "h1": "Stamped Concrete Driveways and Patios in Bradenton",
        "lede": capsule(
            "Stamped concrete in Bradenton runs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October 2026. On older blocks near the Manatee River, "
            "a stamped walk or entry patio is as often a replacement for a cracked 1980s original as it is a first installation."
        ),
        "sections": [
            (
                "Why pattern choice reads differently on an older river-corridor lot",
                "<p>Streets like Riverview Boulevard and East Riverside Drive, both along the Manatee River and both named in the city's own floodplain program " + ext("https://cityofbradenton.com/index.asp?SEC=412EC4AA-2923-4330-993A-BE48C0576144&DE=CDCFD067-8988-4FEA-9708-F5E8D69955CD", "City of Bradenton, Floodplain Management Program") + ", carry older housing stock than the subdivisions built closer to the 1983 citywide median " + src("acs-bradenton") + ". A slate or ashlar stamped pattern in a muted integral color tends to suit a riverfront lot like that in a way a bright stamped cobble pattern sized for a newer subdivision driveway does not, a styling call homeowners along the older corridors make more often than elsewhere in the city.</p>"
            ),
            (
                "Fitting a stamped slab into the impervious coverage math",
                "<p>A stamped finish doesn't change how the city counts the slab: it still draws from the same impervious surface ratio LUR §3.2 applies to any driveway, patio or deck, from 50% in R-1 up to 70% in R-3, UV and R-4 " + src("bradenton-lur-3.2-isr") + ". On a riverfront lot that already carries a full driveway and a dock easement to account for, running the city's worksheet before finalizing a stamped walkway's footprint avoids a redesign after the forms are set " + src("bradenton-impervious-worksheet") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have a 350 sq ft stamped-concrete entry walk and front patio on a lot along Riverview Boulevard",
            "<p>Say you have a 350 sq ft stamped-concrete entry walk and front patio on a lot along Riverview Boulevard. At the market range of " + price("stamped-concrete") + " per sq ft, that runs $2,800 to $6,650, or roughly $4,200 to $5,600 in the typical " + price("stamped-concrete", typical=True) + " band depending on the pattern and number of colors. Because the street sits among the ones the city's floodplain program flags along the Manatee River, the finished grade is checked against the current flood map before forms go in, and a slate or ashlar pattern in a single integral color is the choice we steer toward on an older river-corridor lot like this one.</p>"
        ),
        "faqs": [
            faq(
                "Does stamped concrete need to match older Bradenton riverfront homes?",
                "There's no code requirement tied to the pattern, but a muted slate or ashlar pattern tends to suit an older river-corridor lot better than a bright multi-color cobble pattern sized for a newer subdivision, so it's the default we suggest along streets like Riverview Boulevard."
            ),
            faq(
                "Does a stamped driveway near the Manatee River need a flood check?",
                "Worth doing. The city's floodplain program names Riverview Boulevard and East Riverside Drive among the streets it flags for flood risk, so we check the current flood map before setting a stamped slab's finished grade on those blocks."
            ),
            faq(
                "Does stamped concrete cost more than plain concrete in Bradenton?",
                "The market range here is " + price("stamped-concrete") + " per sq ft versus " + price("concrete-driveway") + " for plain concrete, reflecting the integral color, release agent and stamping labor; the permit and ISR math are the same either way."
            ),
        ],
        "sources": SRC,
    },
    "concrete-walkways": {
        "title": "Concrete Walkways in Bradenton, FL – Sidewalk Spec",
        "meta": "Concrete walkways in Bradenton, FL match the city's 4-inch, 5-foot residential sidewalk spec under LUR 4.1; market range is " + price("concrete-walkway") + " per " + per("concrete-walkway") + ".",
        "h1": "Concrete Sidewalks and Walkways in Bradenton",
        "lede": capsule(
            "A concrete walkway or sidewalk section in Bradenton runs " + price("concrete-walkway") + " per " + per("concrete-walkway") + " as of October 2026. The city sets a specific spec for residential sidewalks, "
            "4 inches thick and 5 feet wide, that a front-walk replacement crossing that strip has to match."
        ),
        "sections": [
            (
                "The city's own sidewalk thickness and width",
                "<p>LUR §4.1 is specific about residential sidewalks: \"Sidewalks shall be concrete and shall be a minimum of four inches thick and five feet wide in residential areas\" "
                + src("bradenton-lur-4.1-access-sidewalks") + ". A front walkway that crosses that strip between the property line and the street has to meet the same spec, and because the work sits in the public right-of-way, it falls under the same Driveway/Sidewalk Affidavit a driveway apron needs, putting the ongoing maintenance obligation on the homeowner " + src("bradenton-driveway-affidavit") + ". A side-yard path that stays entirely on private ground doesn't carry that same width requirement, which is why we confirm where a walkway crosses the sidewalk strip before pricing it.</p>"
            ),
            (
                "A walkway still counts toward the lot's impervious total",
                "<p>Even a narrow front walk draws from the same impervious surface ratio the city applies to the driveway and patio, since LUR §3.2 reaches \"other impervious surfaces\" beyond the named categories " + src("bradenton-lur-3.2-isr") + ". On a lot already close to its district's cap, a wider front walk or a new side path is worth checking against the worksheet before the forms go in, the same step a driveway widening would need " + src("bradenton-impervious-worksheet") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have a 4 x 40 ft front walkway, about 160 sq ft, connecting the driveway to the entry and crossing the public sidewalk strip",
            "<p>Say you have a 4 x 40 ft front walkway, about 160 sq ft, connecting the driveway to the entry and crossing the public sidewalk strip. At the market range of " + price("concrete-walkway") + " per sq ft, that runs $1,120 to $2,720, or roughly $1,280 to $1,920 in the typical " + price("concrete-walkway", typical=True) + " band for a broom-finished walk. Where the walk crosses the sidewalk strip, it has to be poured to the city's 4-inch, 5-foot residential spec and covered by the same affidavit a driveway apron needs; the private portion closer to the house doesn't carry that width requirement, though it still counts toward the lot's impervious total.</p>"
        ),
        "faqs": [
            faq(
                "What thickness and width does a Bradenton sidewalk need?",
                "LUR §4.1 sets residential sidewalks at a minimum of 4 inches thick and 5 feet wide. A front walkway crossing that public strip has to meet the same spec, even where the rest of the walkway on private ground is narrower."
            ),
            faq(
                "Does a front walkway need the same affidavit as a driveway in Bradenton?",
                "The portion crossing the public right-of-way does. The Driveway/Sidewalk Affidavit covers both, putting the ongoing maintenance and relocation obligation on the homeowner for whatever sits in the public strip."
            ),
            faq(
                "Does a new walkway count toward Bradenton's impervious surface limit?",
                "Yes. LUR §3.2's definition reaches beyond the driveway and patio to other impervious surfaces generally, so a new or widened front walk gets added to the lot's existing coverage against its district's cap."
            ),
        ],
        "sources": SRC,
    },
    "concrete-slabs": {
        "title": "Concrete Slabs in Bradenton, FL – Fill & ISR",
        "meta": "Concrete slabs in Bradenton, FL need fill sized to flatwoods soil and count toward LUR 3.2 coverage; market range is " + price("concrete-slab") + " per " + per("concrete-slab") + ", Oct. 2026.",
        "h1": "Concrete Slabs for Sheds, AC Pads and Parking",
        "lede": capsule(
            "A concrete slab in Bradenton, for a shed, an AC pad or RV parking, runs " + price("concrete-slab") + " per " + per("concrete-slab") + " as of October 2026. Flatwoods soil "
            "and a shallow seasonal water table shape how much fill a pad needs, and the finished slab still draws from the lot's impervious cap."
        ),
        "sections": [
            (
                "Fill limits on EauGallie and Immokalee soil",
                "<p>Many Bradenton lots sit on EauGallie or Immokalee fine sand, both poorly drained flatwoods series with a seasonal high water table that climbs within 6 to 18 inches of the surface for part of the year "
                + src("nrcs-eaugallie-osd") + " " + src("nrcs-immokalee-osd") + ". Florida's residential code caps clean sand or gravel fill under a slab at 24 inches and earth fill at 8 inches unless an engineer signs off on something deeper, with at least 4 inches of compacted base under the slab itself. A shed or AC pad set on a low spot of the lot sometimes needs more fill than that code limit allows without engineering, worth flagging before a site visit turns into a surprise on pour day.</p>"
            ),
            (
                "A pad still counts toward the lot's coverage, and the permit covers it",
                "<p>LUR §2.2.1 names \"parking areas\" directly among the work requiring a zoning permit " + src("bradenton-lur-2.2-zoning-permit") + ", and the slab itself still draws from the lot's impervious surface ratio under LUR §3.2, whether it's a shed pad, an AC slab or a parking area for a boat or RV " + src("bradenton-lur-3.2-isr") + ". On a lot where the original 1983-era carport slab was sized for smaller equipment than today's condenser units or trailers, adding or enlarging a " + svc("concrete-slabs", "pad") + " is as much a resizing project as a repour, and the worksheet math should happen before the new footprint is finalized " + src("bradenton-impervious-worksheet") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have a 10 x 12 ft slab, 120 sq ft, for a shed on the side yard of a 1983-built lot with soft, sandy ground",
            "<p>Say you have a 10 x 12 ft slab, 120 sq ft, for a shed on the side yard of a 1983-built lot with soft, sandy ground. At the market range of " + price("concrete-slab") + " per sq ft, that runs $480 to $1,200, or roughly $720 to $960 in the typical " + price("concrete-slab", typical=True) + " band for a 4-inch slab with a compacted base. Because the side yard sits on EauGallie fine sand with a shallow seasonal water table, the fill under the slab gets checked against the code's 24-inch clean-fill limit before anything is brought in, and the pad's footprint gets added to the lot's existing impervious total before the zoning permit is filed.</p>"
        ),
        "faqs": [
            faq(
                "Does a shed slab in Bradenton need extra fill because of the soil?",
                "Often, since EauGallie and Immokalee, two common soils here, hold a seasonal water table within 6 to 18 inches of the surface for part of the year. Florida's residential code caps clean fill at 24 inches without an engineer's sign-off, which we check against before ordering fill."
            ),
            faq(
                "Does a shed or AC pad need a zoning permit in Bradenton?",
                "Yes. LUR §2.2.1 names parking areas directly among the work requiring a zoning permit, and the general rule extends to other paved or impervious pads as well, with the finished slab counting toward the lot's ISR."
            ),
            faq(
                "Can I replace an old AC pad with a bigger one in Bradenton?",
                "Yes, and it's common on homes from the 1983 median build year, since newer equipment is often larger than the original unit. The new slab's footprint counts toward the lot's impervious coverage cap the same as any other hardscape."
            ),
        ],
        "sources": SRC,
    },
    "concrete-repair": {
        "title": "Concrete Repair in Bradenton, FL – 1983-Era Slabs",
        "meta": "Concrete repair in Bradenton, FL often means a driveway original to the 1983 median build year; market range is " + price("concrete-repair") + " per " + per("concrete-repair") + ", October 2026.",
        "h1": "Concrete Driveway and Slab Repair in Bradenton",
        "lede": capsule(
            "Concrete repair and resurfacing in Bradenton runs " + price("concrete-repair") + " per " + per("concrete-repair") + " as of October 2026. With a median home built in 1983, "
            "a lot of what we see is an original driveway cracking near its joints, sometimes faster on a lot close enough to the river or the bay for salt air to be a factor."
        ),
        "sections": [
            (
                "Why so much of Bradenton's driveway stock is overdue",
                "<p>The median year a Bradenton home was built is 1983 " + src("acs-bradenton") + ", which puts a lot of original driveways and walks at more than four decades of Florida heat cycling and rainy-season saturation, well past the point where patching the same crack twice makes sense over a resurfacing overlay or a tear-out. Resurfacing restores the surface without the cost of a full replacement when the underlying slab hasn't lost structural integrity; " + svc("concrete-repair") + " covers both paths, and a site visit is what tells us which one a given slab needs.</p>"
            ),
            (
                "When salt air, not just age, drives the cracking",
                "<p>On a lot close to the Manatee River or to Palma Sola Bay in West Bradenton, FDOT's marine-environment line, within 2,500 feet of water above 2,000 ppm chloride, often applies " + src("fdot-sdg") + ", and salt exposure corrodes any embedded rebar or wire mesh faster than it would on an inland driveway, which can show up as spalling along a crack rather than a clean break. Before pricing a repair on one of these lots, we check whether the damage pattern points to ordinary age or to salt working on the reinforcement underneath, since the two call for different fixes.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 500 sq ft driveway, original to a 1983 Bradenton home, with surface cracking and some spalling near one edge",
            "<p>Say you have a 500 sq ft driveway, original to a 1983 Bradenton home, with surface cracking and some spalling near one edge. At the market range of " + price("concrete-repair") + " per sq ft for resurfacing, that runs $1,500 to $5,000, or roughly $2,000 to $3,500 in the typical " + price("concrete-repair", typical=True) + " band, against a full tear-out and repour at the higher " + price("concrete-driveway") + " per sq ft range for new concrete. If the home sits close enough to the river or the bay for salt air to be a factor, the spalling pattern gets checked against the embedded reinforcement before deciding between resurfacing and replacement, since salt-driven corrosion under a resurfaced overlay tends to resurface within a season or two.</p>"
        ),
        "faqs": [
            faq(
                "Is my Bradenton driveway's age the reason it's cracking?",
                "It's a common factor. The median home here was built in 1983, and a driveway from that era has had roughly four decades of Florida heat and rainy-season cycling to work on its joints, longer than most concrete is expected to go without attention."
            ),
            faq(
                "Does living near the Manatee River or Palma Sola Bay change how a driveway cracks?",
                "It can. Salt air within FDOT's 2,500-foot marine-environment line corrodes embedded rebar or wire mesh faster than it would inland, which tends to show up as spalling along a crack rather than a clean structural break."
            ),
            faq(
                "Is resurfacing or full replacement cheaper for an old Bradenton driveway?",
                "Resurfacing, at " + price("concrete-repair") + " per sq ft, costs less than a full tear-out and repour at " + price("concrete-driveway") + " per sq ft, but only holds up if the underlying slab and its reinforcement haven't lost structural integrity, which a site visit determines."
            ),
        ],
        "sources": SRC,
    },
    "paver-sealing": {
        "title": "Paver Sealing in Bradenton, FL – Maintenance Rule",
        "meta": "Paver sealing in Bradenton, FL counts as maintenance under LUR 2.2, skipping the zoning permit; market range is " + price("paver-sealing") + " per " + per("paver-sealing") + ".",
        "h1": "Paver Sealing and Restoration in Bradenton",
        "lede": capsule(
            "Cleaning, re-sanding and sealing pavers in Bradenton runs " + price("paver-sealing") + " per " + per("paver-sealing") + " as of October 2026. The city's zoning permit rule carries its own maintenance exception, "
            "and a lot near Palma Sola Bay or the Manatee River needs that sealer sooner than an inland address."
        ),
        "sections": [
            (
                "Why sealing skips the zoning permit, in the code's own words",
                "<p>LUR §2.2.1 requires a zoning permit before building or altering a paved area, but it carves out an exception in the same sentence: the permit is required \"except for recurring maintenance, regardless of cost\" " + src("bradenton-lur-2.2-zoning-permit") + ". Cleaning, re-sanding with polymeric sand and sealing an existing paver driveway or patio falls squarely into that maintenance category, not new construction, which is why a reseal job doesn't trigger the same review a new driveway or an expanded patio would. That line gets tested on a project that starts as a reseal and grows into a releveling job, where pavers have to come up and be reset rather than just cleaned.</p>"
            ),
            (
                "Why bayfront and riverfront lots need sealer sooner",
                "<p>FDOT draws its own marine-environment line at 2,500 feet from water above 2,000 ppm chloride for bridge design, and a paver surface that close to the Manatee River or Palma Sola Bay in West Bradenton sits in the same salt-heavy air " + src("fdot-sdg") + ". Salt accelerates how fast joint sand washes out and how quickly an unsealed paver surface shows staining, which is why we check how close a lot sits to open water before recommending a resealing interval rather than quoting the same schedule for every Bradenton address.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 450 sq ft combined driveway and walkway, 6 years unsealed, on a West Bradenton lot a few blocks from Palma Sola Bay",
            "<p>Say you have a 450 sq ft combined driveway and walkway, 6 years unsealed, on a West Bradenton lot a few blocks from Palma Sola Bay. At the market range of " + price("paver-sealing") + " per sq ft, a clean, re-sand and seal runs $675 to $1,463, or roughly $788 to $1,238 in the typical " + price("paver-sealing", typical=True) + " band depending on how much releveling the joints need first. Because the job is maintenance on an existing surface rather than new construction, it falls under LUR §2.2.1's recurring-maintenance exception and doesn't need a separate zoning permit, though a sealer rated for salt exposure is worth the upgrade on a lot this close to the bay.</p>"
        ),
        "faqs": [
            faq(
                "Does paver sealing need a zoning permit in Bradenton?",
                "No. LUR §2.2.1 requires a zoning permit for paving work, but it exempts recurring maintenance regardless of cost, and cleaning, re-sanding and sealing an existing paver surface falls under that maintenance exception."
            ),
            faq(
                "How often should pavers near Palma Sola Bay be resealed?",
                "More often than an inland Bradenton address, as a rule of thumb, since salt air within FDOT's 2,500-foot marine-environment line speeds up joint-sand washout and surface staining. We check a lot's distance from the bay or the river before setting an interval."
            ),
            faq(
                "What turns a sealing job into one that needs a permit in Bradenton?",
                "If pavers in a driveway or walkway have to come up and be reset rather than just cleaned and re-sanded, the scope can cross from maintenance into reconstruction, which is worth flagging before a reseal quote grows mid-job."
            ),
        ],
        "sources": SRC,
    },
    "retaining-walls": {
        "title": "Retaining Walls in Bradenton, FL – Easement Rule",
        "meta": "Retaining walls in Bradenton, FL cannot sit in drainage or utility easements under LUR 5.1; market range is " + price("retaining-wall") + " per " + per("retaining-wall") + " of wall face.",
        "h1": "Retaining Walls for Bradenton Yards",
        "lede": capsule(
            "A retaining wall in Bradenton runs " + price("retaining-wall") + " per " + per("retaining-wall") + " of wall face as of October 2026. The city's code bars a retaining wall "
            "from sitting inside a drainage or utility easement, a rule worth checking before a wall is designed near the river or a sloped lot line."
        ),
        "sections": [
            (
                "What Bradenton's code says, and what it doesn't",
                "<p>LUR §5.1 states that in residential districts, \"retaining walls and solid walls cannot be located in drainage and utility easements,\" and that a wall's height is measured \"from the outside, lower grade inclusive of any fence or wall\" built on top of it " + src("bradenton-lur-5.1-retaining-walls") + ". No separate engineering threshold by height was published in the sections reviewed, which makes a direct call to the Building and Permitting Division at (941) 932-9414 worth making before finalizing a wall's design " + src("bradenton-permitting") + ". The wall still counts toward the lot's impervious surface ratio under LUR §3.2 if it's part of a larger hardscape addition " + src("bradenton-lur-3.2-isr") + ".</p>"
            ),
            (
                "Grading near the Manatee River or a sloped lot line",
                "<p>A retaining wall built to manage a grade change near the river or along a canal has to account for the easement rule first, since a drainage easement often runs along the low side of a riverfront lot precisely where a wall would otherwise go. On a lot close enough to the water for FEMA's Zone AE or VE to apply " + src("fema-coastal-firm") + ", the wall's drainage behind it also has to account for a higher water table than an inland Bradenton yard would need to plan around, which is part of why we check the flood map and the easement plat together before pricing the job.</p>"
            ),
        ],
        "scenario": (
            "Say you have a sloped side yard that needs a 25 linear ft segmental block wall, 3 feet tall, 75 sq ft of wall face, near a drainage easement",
            "<p>Say you have a sloped side yard that needs a 25 linear ft segmental block wall, 3 feet tall, 75 sq ft of wall face, near a drainage easement. At the market range of " + price("retaining-wall") + " per sq ft of wall face, that runs $1,125 to $3,000, or roughly $1,500 to $2,625 in the typical " + price("retaining-wall", typical=True) + " band before drainage behind the wall is added in. Because part of the property's lower grade falls inside a platted drainage easement, the wall's alignment gets shifted off that easement before a design is finalized, since LUR §5.1 bars a retaining or solid wall from sitting inside one regardless of height.</p>"
        ),
        "faqs": [
            faq(
                "Can a retaining wall sit in a drainage easement in Bradenton?",
                "No. LUR §5.1 bars retaining walls and solid walls from drainage and utility easements in residential districts, so the wall's alignment has to stay clear of any easement shown on the property's plat."
            ),
            faq(
                "What height retaining wall needs engineering in Bradenton?",
                "The sections of Bradenton's code reviewed don't publish a specific height threshold for engineered drawings, unlike some neighboring jurisdictions. Call the Building and Permitting Division at (941) 932-9414 to confirm what a specific wall height requires before finalizing a design."
            ),
            faq(
                "Does a retaining wall near the Manatee River need extra drainage planning?",
                "Often, yes. A wall close enough to the river for FEMA's flood zones to apply typically faces a higher water table behind it than an inland lot would, which changes how the drainage behind the wall gets built."
            ),
        ],
        "sources": SRC,
    },
    "artificial-turf": {
        "title": "Artificial Turf in Bradenton, FL – DEP Setback",
        "meta": "Artificial turf in Bradenton, FL follows DEP Rule 62-308.100's 10-foot water setback near Palma Sola Bay and the river; market range is " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
        "h1": "Artificial Turf for Bradenton Yards",
        "lede": capsule(
            "Artificial turf in Bradenton runs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October 2026. On a lot near the Manatee River or Palma Sola Bay, "
            "the state's turf rule sets a 10-foot setback from the water that has to be planned into the layout from the start."
        ),
        "sections": [
            (
                "The statewide turf rule, and what Bradenton's own code leaves open",
                "<p>Florida's DEP Rule 62-308.100, effective May 19, 2026, requires natural infill and a washed base, bars in-ground irrigation under the turf, and keeps synthetic turf at least 10 feet from a water body unless the yard backs onto a seawall " + src("dep-rule", "DEP Rule 62-308.100") + ", while F.S. 125.572 limits how far local governments can go in regulating residential turf beyond that " + src("fs125572", "F.S. 125.572") + ". Bradenton's own LUR §3.2 lists \"other impervious surfaces\" in its coverage definition but doesn't name artificial turf specifically among the examples given " + src("bradenton-lur-3.2-isr") + ", so whether a particular yard's turf area counts toward the ISR cap is worth confirming with the Building and Permitting Division before installation rather than assuming either answer.</p>"
            ),
            (
                "The 10-foot setback near the river or the bay",
                "<p>A backyard close to the Manatee River or to Palma Sola Bay in West Bradenton has to keep turf at least 10 feet back from the water's edge unless a seawall runs along the property line, under the state's own rule " + src("dep-rule", "DEP Rule 62-308.100") + ". As of 2026, F.S. 720.3045 separately protects turf that isn't visible from a lot's frontage or a neighboring parcel from most community restrictions " + src("fs720-3045") + ", which matters less inside Bradenton itself, since the city has no citywide HOA layer, but applies directly to any deed-restricted community nearby.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 600 sq ft backyard turf installation on a West Bradenton lot about 30 feet from the edge of Palma Sola Bay",
            "<p>Say you have a 600 sq ft backyard turf installation on a West Bradenton lot about 30 feet from the edge of Palma Sola Bay. At the market range of " + price("artificial-turf") + " per sq ft, that lands between $6,000 and $15,000, or roughly $7,200 to $10,800 in the typical " + price("artificial-turf", typical=True) + " band depending on pile height and backing. Because the yard sits well clear of the state's 10-foot water-body setback, that rule doesn't limit the layout, but the washed-base and natural-infill requirements still apply, and no in-ground irrigation can run under the finished turf.</p>"
        ),
        "faqs": [
            faq(
                "How close to Palma Sola Bay or the Manatee River can artificial turf be installed?",
                "No closer than 10 feet from the water's edge under Florida's DEP Rule 62-308.100, unless the yard backs onto a seawall, in which case that setback doesn't apply."
            ),
            faq(
                "Does artificial turf count toward Bradenton's impervious surface limit?",
                "Unclear from the published code. LUR §3.2 doesn't name turf specifically among its impervious-surface examples, so we confirm with the Building and Permitting Division before assuming either answer on a given lot."
            ),
            faq(
                "Can an irrigation system run under artificial turf in Bradenton?",
                "No. The state's 2026 turf rule bars in-ground irrigation beneath synthetic turf statewide, along with requiring natural infill and a washed base, regardless of which city or county the lot sits in."
            ),
        ],
        "sources": SRC,
    },
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
