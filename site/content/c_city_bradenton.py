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
    "fcc-bradenton-normals",
    "nrmca-cip12",
    "nrmca-cip6",
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
        "Bradenton sits about 12 miles north of the Sarasota unit's base, and the crew pours concrete, sets pavers and installs artificial turf across the city, where the Census Bureau counted 58,014 residents in July 2025 and the median home dates to 1983. "
        "As of October 2026, the Public Works director signs off on driveway curb cuts, a separate zoning permit covers any paved area, and Manatee County keeps the city on a once-a-week watering schedule under its current shortage order."
    ),
    "".join([
        sec(
            "Which office in Bradenton reviews a new driveway or curb cut?",
            "<p>Public Works, through the director's own sign-off under LUR §4.1.4.3: \"Curb cuts in public rights-of-way are subject to the review and approval of the director of public works,\" with a state or county road adding that agency's approval on top "
            + src("bradenton-lur-4.1-access-sidewalks") + ". The same section sets a residential driveway's maximum width at the curb, how far apart two curb cuts on one lot have to sit, and what a circular drive is allowed to do; "
            + post("manatee-county-driveway-permits", "our Manatee County permit guide") + " lays out those numbers in full, along with how Palmetto and the unincorporated county differ. Before a crew reaches the right-of-way, a signed Driveway/Sidewalk Affidavit & Indemnification Agreement has to be on file with Public Works & Utilities at 1411 9th St W, putting the ongoing upkeep and any later relocation cost on the homeowner "
            + src("bradenton-driveway-affidavit") + ". Paving, widening or altering a \"street, driveway, access road, or parking area\" needs its own zoning permit with a scaled site plan under LUR §2.2.1 "
            + src("bradenton-lur-2.2-zoning-permit") + ", a different step from the curb-cut review above it. A few blocks west of downtown, homes in the unincorporated West Bradenton community go through Manatee County's own access and drainage permit instead "
            + ext("https://en.wikipedia.org/wiki/West_Bradenton,_Florida", "West Bradenton, Florida") + ".</p>"
        ),
        sec(
            "What is Bradenton's impervious surface ratio, and what counts toward it?",
            "<p>LUR §3.2 sets a maximum impervious surface ratio (ISR) by zoning district, and the term covers more ground than most homeowners expect: \"building footprint, paved drives, paved terraces, impervious decks, swimming pools, and other impervious surfaces\" are all totaled against the same number "
            + src("bradenton-lur-3.2-isr") + ".</p>"
            + table(
                "City of Bradenton maximum impervious surface ratio by district",
                ["Zoning district", "Max. impervious coverage"],
                [["R-1", "50%"], ["R-2", "60%"], ["R-3", "70%"], ["UV", "70%"], ["R-4", "70%"]],
                "Source: Bradenton LUR §3.2, checked October 2026. The city provides an Impervious Coverage Calculation worksheet to total a lot's existing and proposed hard surfaces " + src("bradenton-impervious-worksheet") + "."
            )
            + "<p>Add up the roof, the driveway, any " + svc("concrete-patios", "patio") + " or " + svc("concrete-pool-decks", "pool deck") + " and a paver walkway, and that's the figure the worksheet checks against the district cap, which is why we run it before a design is finalized rather than after materials are ordered.</p>"
        ),
        sec(
            "What does a 1983 median build year mean for a Bradenton project?",
            "<p>The Census Bureau counted 58,014 Bradenton residents on July 1, 2025 " + src("census-pep-v2025", "Census Bureau, Vintage 2025 population estimates") + ", and the American Community Survey's five-year estimate puts the median year a home here was built at 1983 "
            + src("acs-bradenton", "Census Reporter, Bradenton FL") + ", newer than Sarasota's 1976 median but decades older than Lakewood Ranch's 2014. A lot of original driveways and patio slabs from the early 1980s are now at the point where a crack gets patched for the second or third time, past where "
            + svc("concrete-repair", "resurfacing") + " usually makes more sense than another patch, and a pool cage added a decade or two after the original build often left the surrounding concrete sized for a smaller deck than homeowners want now. The city still markets itself as \"The Friendly City\" "
            + src("bradenton-city") + ", and its housing mix runs from older river-corridor blocks to newer platted subdivisions toward the county line, each aging a little differently.</p>"
        ),
        sec(
            "What do the Manatee River and Palma Sola Bay change for a build near the water?",
            "<p>Bradenton sits on the Manatee River, and the city's own floodplain program names Riverview Boulevard and East Riverside Drive, both along the river, among the stretches it flags for residents checking their flood risk "
            + ext("https://cityofbradenton.com/index.asp?SEC=412EC4AA-2923-4330-993A-BE48C0576144&DE=CDCFD067-8988-4FEA-9708-F5E8D69955CD", "City of Bradenton, Floodplain Management Program") + ". FEMA sorts the ground nearby into two main designations: Zone AE, carrying roughly a 1% chance of flooding in a given year with limited wave action, and the Coastal High Hazard Zone VE, where the odds are the same but breaking waves can be strong enough to damage a structure in a major storm "
            + src("fema-coastal-firm", "FEMA flood zone designations") + ". Bradenton takes part in the National Flood Insurance Program and offers a flood zone determination by phone at no cost. West of downtown, the unincorporated West Bradenton community runs along Palma Sola Bay, a shallow inlet off Anna Maria Sound "
            + ext("https://en.wikipedia.org/wiki/Palma_Sola_Bay", "Palma Sola Bay") + ", shoreline that falls inside the band FDOT's structures manual reserves for a marine environment, salt water carrying 2,000 ppm chloride or more within 2,500 feet "
            + src("fdot-sdg") + ". A " + svc("retaining-walls", "retaining wall") + " or a low " + svc("pool-deck-pavers", "paver pool deck") + " near either the river or the bay is worth checking against the current flood map before forms go up.</p>"
        ),
        sec(
            "How does the current watering order affect sod, turf and new concrete here?",
            "<p>Manatee County confirmed on September 22, 2026 that it keeps following the Southwest Florida Water Management District's Modified Phase III Extreme Water Shortage order, which runs through March 31, 2027 and limits irrigation to a single assigned day each week, tied to the last digit of the address, inside a pre-dawn or late-evening window "
            + src("manatee-phase3") + " " + src("swfwmd-restrictions") + ". What sets the county's own notice apart from a generic district summary is the fine schedule and the hand-watering carve-out: $100 for a first violation, $250 for a second and $500 for a third, while hand-watering and micro-irrigation stay allowed every day before 8 a.m. or after 6 p.m. regardless of the assigned day "
            + src("manatee-phase3") + ". That daily hand-watering allowance is worth knowing on a job site, since it covers the kind of watering-in a freshly laid patch of sod or a curing concrete slab needs, something the once-a-week limit alone wouldn't permit. "
            + svc("artificial-turf") + " never has to wait for its assigned day, since the order governs irrigation, not a lawn that doesn't need any; the water-savings math against sod is worked out in " + compare("artificial-turf-vs-sod", "our turf-versus-sod comparison") + ".</p>"
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
            "Possibly, especially along the Manatee River or in the West Bradenton streets that back onto Palma Sola Bay. FEMA's Zone AE carries roughly a 1% yearly flood chance with limited waves; the Coastal High Hazard Zone VE carries the same odds plus surf strong enough to damage a low structure."
        ),
        faq(
            "Does artificial turf save water under Bradenton's current restrictions?",
            "It sidesteps them entirely. Sod has to live with the county's once-a-week, pre-dawn-or-late-evening window through March 2027; turf is done needing any of that once it's installed and watered in during the setup period."
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
            "As of October 2026, a new or replacement concrete driveway in Bradenton runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", before the portion in the right-of-way, which the Public Works director reviews separately. "
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
            "<p>Say you have a 20 x 24 ft two-car driveway, 480 sq ft, original to a 1983 Bradenton home with diagonal cracking near the garage. Figure " + price("concrete-driveway") + " per sq ft for a full tear-out and repour: $2,880 to $7,200 across that full range, tightening to about $3,840 to $5,760 inside the typical " + price("concrete-driveway", typical=True) + " band. That covers the private slab only; the apron at the street needs its own Public Works review under LUR §4.1, and the Driveway/Sidewalk Affidavit has to be signed before the old apron comes out. If the lot sits a few blocks west in the unincorporated West Bradenton community instead, the same job goes through Manatee County's access and drainage permit rather than the city's zoning review.</p>"
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
            "Expect to pay " + price("paver-driveway") + " per " + per("paver-driveway") + " for a paver driveway in Bradenton, a market range current as of October 2026 that holds whether the job is new work or a tear-out. "
            "The finished square footage still has to clear the city's impervious surface ratio, and on a lot near Palma Sola Bay, salt air shapes which base and edge-restraint hardware holds up best."
        ),
        "sections": [
            (
                "Pavers don't get a pass on the impervious cap",
                "<p>Bradenton's LUR §3.2 defines impervious surface broadly enough to catch a paver driveway the same way it catches poured concrete: \"building footprint, paved drives, paved terraces, impervious decks, swimming pools, and other impervious surfaces\" "
                + src("bradenton-lur-3.2-isr") + ". The district caps run from 50% in R-1 up to 70% in R-3, UV and R-4, and the city's own worksheet totals a lot's existing coverage against the proposed addition " + src("bradenton-impervious-worksheet") + ". Going from two bays to three on a tight R-1 lot is the kind of change that can tip a parcel over its cap, so the worksheet is worth running before the paver order goes in, not after, since LUR §2.2.1's zoning permit asks for the same figure " + src("bradenton-lur-2.2-zoning-permit") + ".</p>"
            ),
            (
                "Building a paver base on wet flatwoods ground",
                "<p>Myakka and Pomello, two soils found across Manatee County, sit at opposite ends of the drainage spectrum: Myakka holds a seasonal high water table less than a foot and a half deep for part of most years, while Pomello drains somewhat better, with water typically a foot and a half to four feet down "
                + src("nrcs-myakka-osd") + " " + src("nrcs-pomello-osd") + ". ICPI's paver spec calls for at least 6 inches of compacted base on well-drained ground, 2 to 4 inches more where the soil runs wet or weak, which on a Myakka lot is closer to the rule than the exception. On a lot bordering Palma Sola Bay, we also favor edge restraints and fastener hardware rated for salt exposure, since FDOT's structures manual puts anything within 2,500 feet of salt water carrying 2,000 ppm chloride or more in its marine-environment category " + src("fdot-sdg") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have an 18 x 40 ft two-car paver driveway, 720 sq ft, on a West Bradenton lot a few blocks from Palma Sola Bay",
            "<p>Say you have an 18 x 40 ft two-car paver driveway, 720 sq ft, on a West Bradenton lot a few blocks from Palma Sola Bay. Figure " + price("paver-driveway") + " per sq ft: $7,200 to $21,600 across the full range, tightening to about $8,640 to $14,400 inside the typical " + price("paver-driveway", typical=True) + " band depending on paver type and base depth. Because the lot sits in unincorporated West Bradenton rather than inside the city line, the access and drainage permit comes from Manatee County rather than the city's zoning office, and because the bay is close by, the edge restraint spec steps up a grade from what an inland Bradenton lot would need.</p>"
        ),
        "faqs": [
            faq(
                "Do pavers count the same as concrete for Bradenton's impervious limit?",
                "Yes. LUR §3.2 defines impervious surface broadly enough to include paved drives regardless of material, so a paver driveway draws from the same percentage cap as a poured one would on the same lot."
            ),
            faq(
                "Does a paver driveway near Palma Sola Bay need different hardware?",
                "It's worth it. FDOT's own structures guide puts anything within 2,500 feet of salt water carrying 2,000 ppm chloride or more in its marine-environment category, which describes much of the shoreline along the bay, so we spec edge restraints and fasteners rated for salt exposure on those lots."
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
            "As of October 2026, a concrete patio in Bradenton runs " + price("concrete-patio") + " per " + per("concrete-patio") + ". Unlike unincorporated Manatee County, which exempts a non-structural patio outright, "
            "the city counts a patio toward its impervious surface cap and folds it into the same zoning permit as a driveway."
        ),
        "sections": [
            (
                "Why the city treats a patio differently from the county",
                "<p>Out in unincorporated Manatee County, the current \"What Does Not Require a Permit\" list, updated June 16, 2026, lets a homeowner pour a non-structural concrete or paver patio without pulling anything first "
                + src("manatee-no-permit-list") + ". Inside the Bradenton city line, that exemption doesn't carry over: there is no published flatwork exemption, so a patio counts toward impervious surface ratio and falls under the same zoning permit rule LUR §2.2.1 applies to any paved area " + src("bradenton-lur-2.2-zoning-permit") + " " + src("bradenton-lur-3.2-isr") + ". A homeowner who moved from Parrish or Myakka City and remembers a patio going in without a permit there is describing the county's rule, not the city's.</p>"
            ),
            (
                "Fitting a patio into the ISR worksheet",
                "<p>Because \"impervious decks\" and \"paved terraces\" are both named in the city's own definition " + src("bradenton-lur-3.2-isr") + ", a patio addition has to be totaled against whatever the lot's driveway, roof and any " + svc("pool-deck-pavers", "pool deck") + " already use, with the Impervious Coverage Calculation worksheet doing that math " + src("bradenton-impervious-worksheet") + ". On a 1983-era lot where the original patio was sized for a smaller pool cage than what's there now, that worksheet step often decides how large a replacement patio can get before the design has to shrink or a different district's cap comes into play.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 14 x 16 ft patio extension, 224 sq ft, off a screened pool cage added a decade after the home's 1983 construction",
            "<p>Say you have a 14 x 16 ft patio extension, 224 sq ft, off a screened pool cage added a decade after the home's 1983 construction. Figure " + price("concrete-patio") + " per sq ft: $1,344 to $2,912 across the full range, tightening to about $1,568 to $2,240 inside the typical " + price("concrete-patio", typical=True) + " band for a broom-finished slab. Before the pour, the new square footage gets added to the lot's existing driveway and pool deck coverage against the district's ISR cap, and the zoning permit required under LUR §2.2.1 covers that addition even though the same scope would likely be exempt a few miles away in unincorporated Manatee County.</p>"
        ),
        "faqs": [
            faq(
                "Does a small concrete patio need a permit in Bradenton?",
                "Yes. Unlike unincorporated Manatee County, which exempts a non-structural patio, Bradenton has no published flatwork exemption, so a patio counts toward the lot's impervious surface ratio and needs the same zoning permit LUR §2.2.1 requires for any paved area."
            ),
            faq(
                "Will a new patio push my Bradenton lot over its coverage limit?",
                "On a lot that's already got a driveway and a pool deck eating into the allowance, yes. Running the city's Impervious Coverage Calculation worksheet against the district's cap before a patio is designed, not after, is how we catch that early."
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
            "As of October 2026, a paver patio in Bradenton costs " + price("paver-patio") + " per " + per("paver-patio") + ". The edge restraint holding the border in place usually decides whether a patio keeps its line over the years, "
            "and that detail carries more weight on a West Bradenton lot near Palma Sola Bay than it does on a dry inland yard."
        ),
        "sections": [
            (
                "The edge restraint matters as much as the paver itself",
                "<p>ICPI's own technical spec requires an edge restraint along the entire perimeter of a paver patio and anywhere the pavement material changes, with plastic or aluminum restraints suited to either a flexible or a rigid base and steel reserved for rigid bases only; the spikes that hold a restraint in place anchor into the compacted aggregate base, not the native soil underneath. Planting-bed edging isn't rated to do that job, a detail worth knowing since a patio built around a garden bed sometimes inherits the wrong hardware by default. None of that changes how the finished square footage gets counted: a paver patio still draws from the lot's impervious surface ratio under LUR §3.2 the same as poured concrete would " + src("bradenton-lur-3.2-isr") + ".</p>"
            ),
            (
                "What a lot near Palma Sola Bay changes about the build",
                "<p>West Bradenton's shoreline along Palma Sola Bay " + ext("https://en.wikipedia.org/wiki/Palma_Sola_Bay", "Palma Sola Bay") + " sits close enough to open water that FDOT's structures manual would classify the ground there as a marine environment, the category it reserves for anything within 2,500 feet of salt water carrying 2,000 ppm chloride or more " + src("fdot-sdg") + ". The base and bedding sand go in the same way regardless, but a metal edge restraint or an unsealed joint shows wear faster on a lot that close to the bay, which is why we weigh hardware and a resealing schedule differently there than we would a few miles inland.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 16 x 20 ft paver patio, 320 sq ft, on a West Bradenton lot within a few blocks of Palma Sola Bay",
            "<p>Say you have a 16 x 20 ft paver patio, 320 sq ft, on a West Bradenton lot within a few blocks of Palma Sola Bay. Figure " + price("paver-patio") + " per sq ft: $3,200 to $5,440 across the full range, tightening to about $3,840 to $5,120 inside the typical " + price("paver-patio", typical=True) + " band depending on the paver and pattern. Because the lot sits in unincorporated West Bradenton, the access and drainage review runs through Manatee County rather than the city, and because the bay is close by, the edge restraint and joint sand go in rated for salt exposure rather than the standard inland spec.</p>"
        ),
        "faqs": [
            faq(
                "Does a paver patio need the same edge restraint as a driveway in Bradenton?",
                "Yes, the perimeter needs a restraint spiked into the compacted base either way; a patio built around a garden bed can't rely on planting-bed edging to do that job, since it isn't rated to hold pavers in line."
            ),
            faq(
                "Does being near Palma Sola Bay change how a paver patio is built?",
                "It doesn't change the base, but salt exposure within FDOT's marine-environment threshold wears down a metal edge restraint or an unsealed joint faster than it would inland, so we spec hardware and a resealing schedule accordingly."
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
            "As of October 2026, a concrete pool deck in Bradenton runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ". Riverfront lots near the Manatee River "
            "and some West Bradenton streets along Palma Sola Bay carry a FEMA flood designation, a factor that sets the elevation and the slope at the slab's edge more than the deck's finish does."
        ),
        "sections": [
            (
                "A pool deck counts toward the lot's impervious cap by name",
                "<p>Bradenton's LUR §3.2 lists \"swimming pools\" and \"impervious decks\" separately in its definition of impervious surface, so a pool deck draws from the same percentage cap as the driveway and roof, not a different allowance " + src("bradenton-lur-3.2-isr") + ". The district caps run from 50% in R-1 to 70% in R-3, UV and R-4, and the city's worksheet totals the lot's existing coverage against a proposed deck before the permit is filed " + src("bradenton-impervious-worksheet") + ". On a lot that already carries a full driveway and a " + svc("paver-patios", "paver patio") + ", that math is worth running before the pool contractor finalizes a deck size, not after.</p>"
            ),
            (
                "Flood zones along the river and the bay",
                "<p>Two FEMA designations cover most of the ground near the water here: Zone AE, where the yearly odds of flooding run around 1% and wave action stays modest, and Zone VE, the Coastal High Hazard category, where those same odds come paired with breaking surf that can take out a low structure in a major storm " + src("fema-coastal-firm", "FEMA flood zone designations") + ". The city's own floodplain program flags Riverview Boulevard and East Riverside Drive, both along the Manatee River, as streets worth a closer look " + ext("https://cityofbradenton.com/index.asp?SEC=412EC4AA-2923-4330-993A-BE48C0576144&DE=CDCFD067-8988-4FEA-9708-F5E8D69955CD", "City of Bradenton, Floodplain Management Program") + ", and a call to the city gets a deck's finished elevation checked against the current map at no charge before forms go up.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 700 sq ft screened-cage pool deck on a lot close enough to the Manatee River for the flood map to matter",
            "<p>Say you have a 700 sq ft screened-cage pool deck on a lot close enough to the Manatee River for the flood map to matter. Figure " + price("concrete-pool-deck") + " per sq ft: $3,500 to $10,500 across the full range, tightening to about $4,900 to $8,400 inside the typical " + price("concrete-pool-deck", typical=True) + " band, the exact finish depending on whether it's a plain broom texture or a cool-touch spray coating. Because the lot's flood designation sets the minimum elevation at the coping, the slab's slope and the fill underneath get planned around that number first, and the finished square footage still gets added to the lot's existing coverage against the district's ISR cap before the permit is filed.</p>"
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
                "No, but it changes how fill and drainage at the slab's edge get handled, since Zone VE pairs the same flood odds as Zone AE with breaking surf strong enough to take out a low structure, a tougher standard than the more common AE designation."
            ),
        ],
        "sources": SRC,
    },
    "pool-deck-pavers": {
        "title": "Pool Deck Pavers in Bradenton, FL – Salt Air",
        "meta": "Pool deck pavers near Palma Sola Bay in Bradenton, FL face FDOT's marine-environment salt criterion; market range is " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ", Oct. 2026.",
        "h1": "Travertine and Paver Pool Decks in Bradenton",
        "lede": capsule(
            "As of October 2026, pool deck pavers or travertine in Bradenton run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ". On lots along Palma Sola Bay in West Bradenton, "
            "salt air off the water shapes the sealer and hardware choice more than it does on an inland driveway or patio."
        ),
        "sections": [
            (
                "Why a bayfront deck needs different hardware",
                "<p>A paver or travertine pool deck going in close to Palma Sola Bay, a shallow inlet off Anna Maria Sound in West Bradenton " + ext("https://en.wikipedia.org/wiki/Palma_Sola_Bay", "Palma Sola Bay") + ", sits inside the zone FDOT's structures manual reserves for salt water carrying 2,000 ppm chloride or more within 2,500 feet " + src("fdot-sdg", "FDOT marine-environment classification") + ". That level of salt exposure wears joint sand and an unsealed surface down faster than an inland deck sees, which is why we size the resealing schedule to how close the bay actually sits rather than applying one interval to every Bradenton address.</p>"
            ),
            (
                "Counting the deck against the lot's coverage cap",
                "<p>Whether the deck is on the mainland or along the bay, it still draws from the same impervious surface ratio the city applies to a driveway or patio, since \"swimming pools\" and \"impervious decks\" are both named in LUR §3.2's definition " + src("bradenton-lur-3.2-isr") + ". On a West Bradenton lot, that review runs through Manatee County's own process rather than the city's, since the community sits in unincorporated territory, though the underlying math, totaling the deck against the roof and driveway, works the same way either side of the line.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 750 sq ft travertine pool deck overlay on a West Bradenton lot a few hundred feet from Palma Sola Bay",
            "<p>Say you have a 750 sq ft travertine pool deck overlay on a West Bradenton lot a few hundred feet from Palma Sola Bay. Figure " + price("pool-deck-pavers") + " per sq ft: $9,000 to $22,500 across the full range, tightening to about $10,500 to $16,500 inside the typical " + price("pool-deck-pavers", typical=True) + " band depending on the stone and pattern. Because the lot sits well inside FDOT's marine-environment threshold, we spec a sealer and edge restraint rated for salt exposure rather than the standard inland hardware, and plan the resealing interval shorter than we would for a deck a mile or two from open water.</p>"
        ),
        "faqs": [
            faq(
                "Does salt air near Palma Sola Bay change how a pool deck paver job is built?",
                "It doesn't change the base, but it does change the sealer and edge-restraint hardware we spec, and how often resealing comes up, since FDOT's structures manual puts this stretch of shoreline in its marine-environment category."
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
            "As of October 2026, stamped concrete in Bradenton costs " + price("stamped-concrete") + " per " + per("stamped-concrete") + ". Getting the color and texture right before the surface sets up matters as much here as the pattern itself, "
            "especially during a rainy-season stretch wetter than the regional airport average, and the finished slab still counts toward the city's impervious cap like any other hardscape."
        ),
        "sections": [
            (
                "Why timing the pour matters as much as the pattern",
                "<p>The Bradenton weather co-op station reads wetter than the Sarasota-Bradenton airport gauge most of the unit relies on, 56.28 inches of rain a year with August alone averaging above 10 inches " + src("fcc-bradenton-normals") + ", which shortens the dry window a stamping crew gets between afternoon storms. Integral color and a release agent both need a workable surface to texture correctly, and NRMCA's hot-weather guidance calls for curing to start the moment finishing is done and to continue at least 3 days, with a white-pigmented curing compound reflecting some of the heat a darker stamped color would otherwise hold " + src("nrmca-cip12") + ". On a muggy August afternoon with a storm building over the bay, that schedule decides when a crew starts far more than the pattern choice does.</p>"
            ),
            (
                "A stamped slab still counts toward the impervious cap",
                "<p>A stamped finish doesn't change how the city counts the slab: it still draws from the same impervious surface ratio LUR §3.2 applies to any driveway, patio or deck, from 50% in R-1 up to 70% in R-3, UV and R-4 " + src("bradenton-lur-3.2-isr") + ". On a lot that already carries a full driveway and a pool deck, running the city's worksheet before finalizing a stamped walkway's footprint avoids a redesign after the forms are set " + src("bradenton-impervious-worksheet") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have a 350 sq ft stamped-concrete entry walk and front patio, poured during a wet August week",
            "<p>Say you have a 350 sq ft stamped-concrete entry walk and front patio, poured during a wet August week. Figure " + price("stamped-concrete") + " per sq ft: $2,800 to $6,650 across the full range, tightening to about $4,200 to $5,600 inside the typical " + price("stamped-concrete", typical=True) + " band, the spread tied mostly to how many colors and stamps the pattern calls for. Because afternoon storms are common that time of year, the pour gets scheduled for an early start with curing compound ready to go the moment the texture is stamped, rather than planned around a single set start time regardless of the forecast.</p>"
        ),
        "faqs": [
            faq(
                "Does Bradenton's rain affect a stamped-concrete pour?",
                "It can. The local weather co-op station reads wetter than the regional airport average, and an afternoon storm rolling in before the stamp texture sets or the curing compound goes down can affect the finish, so crews favor early starts during the rainy season."
            ),
            faq(
                "How soon does a stamped driveway need to start curing after it's poured?",
                "As soon as finishing is done, per NRMCA's hot-weather guidance, and it should stay moist or covered for at least 3 days. A white-pigmented curing compound also reflects some of the heat a dark stamped color would otherwise absorb."
            ),
            faq(
                "Does stamped concrete cost more than plain concrete in Bradenton?",
                "Yes, roughly: " + price("stamped-concrete") + " per sq ft for stamped work against " + price("concrete-driveway") + " for a plain pour, a gap that comes from the integral color, release agent and extra labor to texture the surface, not from any difference in permitting or ISR treatment."
            ),
        ],
        "sources": SRC,
    },
    "concrete-walkways": {
        "title": "Concrete Walkways in Bradenton, FL – Sidewalk Spec",
        "meta": "Concrete walkways in Bradenton, FL match the city's 4-inch, 5-foot residential sidewalk spec under LUR 4.1; market range is " + price("concrete-walkway") + " per " + per("concrete-walkway") + ".",
        "h1": "Concrete Sidewalks and Walkways in Bradenton",
        "lede": capsule(
            "As of October 2026, a concrete walkway or sidewalk section in Bradenton runs " + price("concrete-walkway") + " per " + per("concrete-walkway") + ". The city sets a specific spec for residential sidewalks, "
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
            "<p>Say you have a 4 x 40 ft front walkway, about 160 sq ft, connecting the driveway to the entry and crossing the public sidewalk strip. Figure " + price("concrete-walkway") + " per sq ft: $1,120 to $2,720 across the full range, tightening to about $1,280 to $1,920 inside the typical " + price("concrete-walkway", typical=True) + " band for a broom-finished walk. Where the walk crosses the sidewalk strip, it has to be poured to the city's 4-inch, 5-foot residential spec and covered by the same affidavit a driveway apron needs; the private portion closer to the house doesn't carry that width requirement, though it still counts toward the lot's impervious total.</p>"
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
            "As of October 2026, a concrete slab in Bradenton for a shed, an AC pad or boat and RV parking costs " + price("concrete-slab") + " per " + per("concrete-slab") + ". "
            "Which soil series sits under a given pad, more than the slab's finished size, is usually what decides how much fill the job needs."
        ),
        "sections": [
            (
                "Felda and Myakka ground call for their own fill plan",
                "<p>Felda and Myakka, two soils mapped across Manatee County, both sit on the wet end of the local range: Felda carries a seasonal high water table within about a foot of the surface for two to six months of a typical year, and Myakka, Florida's own official state soil, stays within a foot and a half of the surface for one to four months "
                + src("nrcs-felda-osd") + " " + src("nrcs-myakka-osd") + ". The code's fill table draws the line at 24 inches for clean sand or gravel and a tighter 8 inches for ordinary earth before an engineer has to approve anything deeper, with a 4-inch compacted base required underneath regardless. A boat or RV pad set on the low side of a Felda or Myakka lot can run into that ceiling faster than a pad on drier ground would, which is why we flag it at the site visit instead of after the fill truck has already shown up.</p>"
            ),
            (
                "A pad still counts toward the lot's coverage, and the permit covers it",
                "<p>LUR §2.2.1 names \"parking areas\" directly among the work requiring a zoning permit " + src("bradenton-lur-2.2-zoning-permit") + ", and the slab itself still draws from the lot's impervious surface ratio under LUR §3.2, whether it's a shed pad, an AC slab or a parking area for a boat or RV " + src("bradenton-lur-3.2-isr") + ". Swapping an older carport slab for one sized to a modern condenser unit or a trailer that never fit the original footprint counts as an enlargement, not a like-for-like repour, so the worksheet gets run on the new footprint before inspection turns up a lot that's already past its cap " + src("bradenton-impervious-worksheet") + ".</p>"
            ),
        ],
        "scenario": (
            "Say you have a 12 x 30 ft parking pad, 360 sq ft, for a boat trailer on the low corner of a Myakka-soil lot",
            "<p>Say you have a 12 x 30 ft parking pad, 360 sq ft, for a boat trailer on the low corner of a Myakka-soil lot. Figure " + price("concrete-slab") + " per sq ft: $1,440 to $3,600 across the full range, tightening to about $2,160 to $2,880 inside the typical " + price("concrete-slab", typical=True) + " band for a standard 4-inch pour over a compacted aggregate base. Myakka's own drainage profile means that corner holds water part of the year, so the fill depth gets planned against the code's 24-inch ceiling before anything is trucked in, and the pad's finished size still gets tallied into the property's running coverage total before the permit application goes in.</p>"
        ),
        "faqs": [
            faq(
                "Does a boat or RV pad in Bradenton need extra fill because of the soil?",
                "Often, on a lot with Felda or Myakka soil, both of which hold a seasonal high water table within a foot or so of the surface for part of the year. The fill depth gets planned against the code's ceiling rather than guessed at before the pad is priced."
            ),
            faq(
                "Does a shed or AC pad need a zoning permit in Bradenton?",
                "Yes. LUR §2.2.1 names parking areas directly among the work requiring a zoning permit, and the general rule extends to other paved or impervious pads as well, with the finished slab counting toward the lot's ISR."
            ),
            faq(
                "Does a bigger AC condenser pad need more than a straight repour?",
                "Sometimes. A newer condenser can be larger than the carport slab it's replacing was built for, so a resized pad counts as an enlargement against the lot's impervious total, not just a like-for-like repour, which is worth confirming before the worksheet math is finalized."
            ),
        ],
        "sources": SRC,
    },
    "concrete-repair": {
        "title": "Concrete Repair in Bradenton, FL – 1983-Era Slabs",
        "meta": "Concrete repair in Bradenton, FL often means a driveway original to the 1983 median build year; market range is " + price("concrete-repair") + " per " + per("concrete-repair") + ", October 2026.",
        "h1": "Concrete Driveway and Slab Repair in Bradenton",
        "lede": capsule(
            "As of October 2026, concrete repair and resurfacing in Bradenton runs " + price("concrete-repair") + " per " + per("concrete-repair") + ". The joint layout usually tells the story faster than the crack itself does: "
            "a crack that follows an undersized joint pattern is a different repair than one that traces a line of corroding rebar on a lot close to the water."
        ),
        "sections": [
            (
                "Reading the joint layout before pricing the fix",
                "<p>Bradenton's median build year, 1983, trails Sarasota's 1976 figure by about seven years " + src("acs-bradenton") + ", so a driveway here has generally had somewhat fewer seasons of heat cycling and rainy-season saturation on its control joints. NRMCA's joint spacing guidance runs 24 to 36 times a slab's thickness, roughly every 8 to 12 feet on a standard 4-inch driveway " + src("nrmca-cip6") + ", and a slab poured with joints a few feet wider than that spec tends to crack at the midpoint of each panel rather than along the cut line. That pattern, cracking mid-panel versus along a joint, is one of the first things we check on an older Bradenton driveway before pricing an overlay against a tear-out.</p>"
            ),
            (
                "When corroding rebar, not the joint spacing, is the real cause",
                "<p>On a lot close to the Manatee River or to Palma Sola Bay in West Bradenton, FDOT's structures manual would classify the ground as a marine environment, the category it applies within 2,500 feet of salt water carrying 2,000 ppm chloride or more " + src("fdot-sdg") + ", and that salt exposure corrodes embedded rebar or wire mesh faster than it would further inland. Corrosion-driven cracking tends to show up as spalling, a patch of surface popping loose over the reinforcement, rather than the clean mid-panel crack a plain age or joint issue produces, and the two call for different fixes once a site visit sorts out which one is at work.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 500 sq ft driveway with surface cracking and some spalling near one edge, close enough to open water for salt to be a factor",
            "<p>Say you have a 500 sq ft driveway with surface cracking and some spalling near one edge, close enough to open water for salt to be a factor. Figure " + price("concrete-repair") + " per sq ft for resurfacing: $1,500 to $5,000 across the full range, tightening to about $2,000 to $3,500 inside the typical " + price("concrete-repair", typical=True) + " band, well under a full tear-out and repour priced at the " + price("concrete-driveway") + " per sq ft new-concrete range. Because the spalling sits near the edge rather than mid-panel, the reinforcement underneath gets checked for corrosion before resurfacing is quoted, since an overlay poured over actively rusting rebar tends to crack open again within a season or two.</p>"
        ),
        "faqs": [
            faq(
                "How do I know if my Bradenton driveway crack is normal wear or something worse?",
                "Check where it runs. A crack along or near a control joint, especially on a wider-than-spec joint layout, is usually ordinary wear; a crack with surface spalling over it, especially on a lot close to the river or the bay, points toward corroding reinforcement underneath instead."
            ),
            faq(
                "Does living near the Manatee River or Palma Sola Bay change how a driveway cracks?",
                "It can. Salt exposure inside FDOT's marine-environment threshold corrodes embedded rebar or wire mesh faster than it would further inland, which tends to show up as spalling over the reinforcement rather than a clean mid-panel crack."
            ),
            faq(
                "Can resurfacing fix a driveway with corroding rebar underneath?",
                "Not for long. An overlay poured over actively corroding reinforcement tends to crack open again within a season or two, so that diagnosis usually points toward a tear-out and repour instead of a resurfacing quote."
            ),
        ],
        "sources": SRC,
    },
    "paver-sealing": {
        "title": "Paver Sealing in Bradenton, FL – Maintenance Rule",
        "meta": "Paver sealing in Bradenton, FL counts as maintenance under LUR 2.2, skipping the zoning permit; market range is " + price("paver-sealing") + " per " + per("paver-sealing") + ".",
        "h1": "Paver Sealing and Restoration in Bradenton",
        "lede": capsule(
            "As of October 2026, cleaning, re-sanding and sealing pavers in Bradenton costs " + price("paver-sealing") + " per " + per("paver-sealing") + ". It's maintenance, not construction, under the city's own zoning code, "
            "though how soon it needs doing again depends heavily on whether the address sits near open water."
        ),
        "sections": [
            (
                "Why sealing skips the zoning permit, in the code's own words",
                "<p>LUR §2.2.1 requires a zoning permit before building or altering a paved area, but it carves out an exception in the same sentence: the permit is required \"except for recurring maintenance, regardless of cost\" " + src("bradenton-lur-2.2-zoning-permit") + ". A pressure-wash, a fresh load of polymeric sand and a coat of sealer over an existing driveway or patio stay inside that carve-out, since nothing about the footprint or the material changes. Where that carve-out stops applying is a job that turns into a releveling project partway through: once pavers start coming out of the base to be reset rather than just rinsed off, the scope has drifted from upkeep toward reconstruction.</p>"
            ),
            (
                "Reading the salt exposure before quoting an interval",
                "<p>A paver surface near the Manatee River or Palma Sola Bay in West Bradenton sits inside the band FDOT's structures manual reserves for a marine environment, water carrying 2,000 ppm chloride or more within 2,500 feet " + src("fdot-sdg") + ". Joint sand washes out faster under that kind of salt exposure, and staining on an unsealed surface shows up sooner too, which is why the first question on a Bradenton reseal quote is how close the address sits to open water, not just how many years it's been since the last sealing.</p>"
            ),
        ],
        "scenario": (
            "Say you have a 450 sq ft combined driveway and walkway, unsealed for 6 years, on a West Bradenton lot a few blocks from Palma Sola Bay",
            "<p>Say you have a 450 sq ft combined driveway and walkway, unsealed for 6 years, on a West Bradenton lot a few blocks from Palma Sola Bay. Figure " + price("paver-sealing") + " per sq ft for a clean, re-sand and seal: $675 to $1,463 across the full range, tightening to about $788 to $1,238 inside the typical " + price("paver-sealing", typical=True) + " band depending on how much releveling the joints need first. The job counts as maintenance under LUR §2.2.1's recurring-maintenance exception, so no separate zoning permit applies, but a sealer rated for salt exposure is the upgrade worth paying for on a lot this close to the bay.</p>"
        ),
        "faqs": [
            faq(
                "Does paver sealing need a zoning permit in Bradenton?",
                "No. LUR §2.2.1 requires a zoning permit for paving work, but it exempts recurring maintenance regardless of cost, and cleaning, re-sanding and sealing an existing paver surface falls under that maintenance exception."
            ),
            faq(
                "How often should pavers near Palma Sola Bay be resealed?",
                "On a shorter cycle than an inland Bradenton address needs, as a rule of thumb, since the salt exposure inside FDOT's marine-environment threshold speeds up joint-sand washout and surface staining alike."
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
        "meta": "Retaining walls in Bradenton, FL cannot sit in drainage or utility easements under LUR 5.1; market range is " + price("retaining-wall") + " per " + per("retaining-wall") + ".",
        "h1": "Retaining Walls for Bradenton Yards",
        "lede": capsule(
            "As of October 2026, a retaining wall in Bradenton runs " + price("retaining-wall") + " per " + per("retaining-wall") + ". The city's code bars a retaining wall "
            "from sitting inside a drainage or utility easement, a rule worth checking before a wall is designed near the river or a sloped lot line."
        ),
        "sections": [
            (
                "What Bradenton's code says, and what it doesn't",
                "<p>LUR §5.1 states that in residential districts, \"retaining walls and solid walls cannot be located in drainage and utility easements,\" and that a wall's height is measured \"from the outside, lower grade inclusive of any fence or wall\" built on top of it " + src("bradenton-lur-5.1-retaining-walls") + ". No separate engineering threshold by height was published in the sections reviewed, which makes a direct call to the Building and Permitting Division at (941) 932-9414 worth making before finalizing a wall's design " + src("bradenton-permitting") + ". The wall still counts toward the lot's impervious surface ratio under LUR §3.2 if it's part of a larger hardscape addition " + src("bradenton-lur-3.2-isr") + ".</p>"
            ),
            (
                "Grading near the Manatee River or a sloped lot line",
                "<p>A retaining wall built to manage a grade change near the river or along a canal has to account for the easement rule first, since a drainage easement often runs along the low side of a riverfront lot precisely where a wall would otherwise go. On a lot close enough to the water for FEMA's Zone AE or VE to apply " + src("fema-coastal-firm", "FEMA flood zone designations") + ", the wall's drainage behind it also has to account for a higher water table than an inland Bradenton yard would need to plan around, which is part of why we check the flood map and the easement plat together before pricing the job.</p>"
            ),
        ],
        "scenario": (
            "Say you have a sloped side yard that needs a 25 linear ft segmental block wall, 3 feet tall, 75 sq ft of wall face, near a drainage easement",
            "<p>Say you have a sloped side yard that needs a 25 linear ft segmental block wall, 3 feet tall, 75 sq ft of wall face, near a drainage easement. Figure " + price("retaining-wall") + " per sq ft of wall face: $1,125 to $3,000 across the full range, tightening to about $1,500 to $2,625 inside the typical " + price("retaining-wall", typical=True) + " band before drainage behind the wall is added in. Because part of the property's lower grade falls inside a platted drainage easement, the wall's alignment gets shifted off that easement before a design is finalized, since LUR §5.1 bars a retaining or solid wall from sitting inside one regardless of height.</p>"
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
            "As of October 2026, artificial turf in Bradenton runs " + price("artificial-turf") + " per " + per("artificial-turf") + ". On a lot near the Manatee River or Palma Sola Bay, "
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
            "<p>Say you have a 600 sq ft backyard turf installation on a West Bradenton lot about 30 feet from the edge of Palma Sola Bay. Figure " + price("artificial-turf") + " per sq ft: $6,000 to $15,000 across the full range, tightening to about $7,200 to $10,800 inside the typical " + price("artificial-turf", typical=True) + " band depending on pile height and backing. Because the yard sits well clear of the state's 10-foot water-body setback, that rule doesn't limit the layout, but the washed-base and natural-infill requirements still apply, and no in-ground irrigation can run under the finished turf.</p>"
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
