# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "longboat-key"

CANAVERAL_OSD_URL = "https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CANAVERAL.html"
LBK_ACS_URL = "https://censusreporter.org/profiles/16000US1241150-longboat-key-fl/"
BAYISLES_DECL_URL = "https://www.bayisles.com/wp-content/uploads/Declaration-of-Restrictions-4-16-1976.pdf"
LBK_WAIVER_URL = "https://www.longboatkey.org/235/Post-Hurricane-Helene-Milton-Building-Pe"
LBK_WAIVER_EXT_URL = "https://www.mysuncoast.com/2025/10/15/one-last-extension-waived-storm-related-rebuilding-permits-longboat-key/"

SRC = [
    "lbk-code-57.03-row-permit", "lbk-streets-row", "lbk-code-158.100-drive-width", "lbk-code-150.30-minor-work",
    "lbk-code-158.144-impermeable", "lbk-code-158.030-open-space-cccl", "lbk-code-158.062-r3sf",
    "lbk-code-158.118-retaining-wall", "lbk-code-158.102-walls", "lbk-code-100.04-cccl-lighting", "lbk-building-division",
    "census-pep-v2025", "fdot-sdg", "fema-coastal-firm", "fdep-cccl-program", "fdep-cccl-apply", "dep-rule", "fs125572",
    "swfwmd-restrictions", "usda-wss",
    ("USDA NRCS Official Series Description — Canaveral", CANAVERAL_OSD_URL),
    ("Census Reporter, Longboat Key FL (ACS 2020-2024 5-yr, B25035/B01003)", LBK_ACS_URL),
    ("Bay Isles Association, Inc. — Declaration of Maintenance Covenants and Restrictions on the Commons, recorded April 16, 1976", BAYISLES_DECL_URL),
    ("Town of Longboat Key — Post-Hurricane Helene & Milton Building Permitting Information", LBK_WAIVER_URL),
    ("WWSB/Mysuncoast.com — final extension of Longboat Key's storm-related permit-fee waiver (Oct. 15, 2025)", LBK_WAIVER_EXT_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Which office issues a driveway, patio or pool deck permit on Longboat Key?",
        "<p>The Town itself, no matter which county line a given lot falls on. Longboat Key's own code makes it unlawful to "
        "\"construct, install, remove, relocate, or perform other work activities on utilities or installations within, on, under, "
        "or above rights-of-way without first having obtained a rights-of-way use permit,\" and work has to start within 90 days of "
        "issue " + src("lbk-code-57.03-row-permit", "Town of Longboat Key Code §57.03") + ". Planning, Zoning & Building, at 501 Bay "
        "Isles Rd, has processed every application through the Accela online portal since April 22, 2025 " +
        src("lbk-building-division", "Longboat Key Building Division") + ". That single desk matters here because the Town itself "
        "straddles two counties: of the 7,359 residents the Census Bureau counted on the island on July 1, 2025, roughly 4,634 live "
        "on the Sarasota County side and 2,725 on the Manatee County side, yet both sides apply through the same building division, "
        "not a county one " + src("census-pep-v2025", "Census Bureau PEP, Vintage 2025") + ". Gulf of Mexico Drive, the island's only "
        "through street, is State Road 789 and belongs to the Florida Department of Transportation, so a driveway connection to it "
        "is an FDOT matter the Town's own Public Works office routes forward rather than approving outright " +
        src("lbk-streets-row", "Longboat Key Streets & Rights-of-Way") + ". " + svc("concrete-driveways") + " and " +
        svc("paver-driveways") + " both start with that same apron question before anything else gets priced.</p>"
    ),
    sec(
        "Why can 'minor work directly on grade' still need a zoning sign-off?",
        "<p>Because the Town's code treats it as a borderline case, not a blanket exemption. Section 150.30(D)(11) lists \"driveways, "
        "decks and patios directly on grade\" as minor work, but the same clause requires that it \"meet specific zoning criteria and "
        "must be approved by zoning department as an exception,\" and minor work can still pull in a full permit once it's part of a "
        "larger remodel " + src("lbk-code-150.30-minor-work", "Longboat Key Code §150.30") + ". The driveway's own width is set on a "
        "separate table: a one-way drive from a parking space to the street tops out at 12 feet, and a two-way drive at 24 feet " +
        src("lbk-code-158.100-drive-width", "Longboat Key Code §158.100") + ". On a lot where the floor sits below the current base "
        "flood elevation, or where the structure is already flagged as FEMA-noncompliant, that same zoning exception can also require "
        "a FEMA tracking permit before anyone pours.</p>"
    ),
    sec(
        "How much of a Longboat Key lot has to stay open, and what counts against that?",
        "<p>At least half of it. The code requires every residential lot to preserve \"a minimum of 50 percent of the gross land "
        "areas\" as open space, and a driveway, paved or not, along with any pool, is written out of that open-space count " +
        src("lbk-code-158.030-open-space-cccl", "Longboat Key Code §158.030") + ". \"Impermeable surface\" is defined broadly on top "
        "of that: structures, pools, driveways, walks and parking areas all count, while permeable wood decks, trellises, thin "
        "walls and clay or grass courts do not " + src("lbk-code-158.144-impermeable", "Longboat Key Code §158.144") + ". The house "
        "itself answers to a separate cap: a single-family lot in the R-3SF district tops out at 25 percent building coverage, rising "
        "to 30 percent in R-4SF and R-6SF " + src("lbk-code-158.062-r3sf", "Longboat Key Code §158.062") + ". A licensed design "
        "professional has to verify that open-space math on the site plan, which is worth raising before a " + svc("paver-driveways") +
        " or a wider pool deck gets drawn up.</p>"
    ),
    sec(
        "What does the one-to-four slope rule mean for a retaining wall here?",
        "<p>It sets both when a wall is allowed and how tall it's permitted to get. Longboat Key caps the grade change between a "
        "property line and a structure at one foot of rise for every four feet of run, and a retaining wall \"may only be constructed "
        "for the purpose of achieving the required one-to-four slope over a minimum distance of four feet unless the wall meets the "
        "required setback,\" and even then it \"cannot exceed eight feet in height\" " +
        src("lbk-code-158.118-retaining-wall", "Longboat Key Code §158.118") + ". Stack a fence on top and the code measures the "
        "combined height from the lower grade, not from the wall's own footing " + src("lbk-code-158.102-walls", "Longboat Key Code "
        "§158.102") + ". Anywhere this overlaps Florida's Coastal Construction Control Line, the site plan has to flag the state "
        "permit separately, and new development seaward of that line also pulls in the Town's sea-turtle lighting review under "
        "Chapter 100 " + src("lbk-code-158.030-open-space-cccl") + " " + src("lbk-code-100.04-cccl-lighting", "Longboat Key Code "
        "§100.04") + ".</p>"
    ),
    sec(
        "What does the island's dune sand and its 1976 communities change about a build?",
        "<p>Longboat Key doesn't sit on the flatwoods soil most of the Sarasota unit does. A soil map check run directly at the "
        "island's own coordinates comes back Canaveral fine sand, a somewhat poorly to moderately well drained dune soil with very "
        "rapid permeability and a seasonal water table only 10 to 40 inches down, and only for two to six months of the year " +
        src("usda-wss") + " " + ext(CANAVERAL_OSD_URL, "NRCS Official Series Description, Canaveral") + ". That drains faster and "
        "holds less water against a base course than the Myakka or EauGallie flatwoods soil common on the mainland. The housing "
        "above it runs older than much of the unit too, with a median year built of 1980 " + ext(LBK_ACS_URL, "Census Reporter, "
        "Longboat Key FL") + ". In Bay Isles, one of the island's larger deed-restricted communities, a declaration recorded in "
        "April 1976 reserves architectural and construction approval for each neighborhood or condominium association inside it, "
        "with the master Bay Isles Association, Inc. stepping in only if that smaller association doesn't act " +
        ext(BAYISLES_DECL_URL, "Bay Isles Association, Inc., Declaration of Maintenance Covenants and Restrictions") + ". No "
        "published rule there names a specific driveway material or paver color, so the first call on a Bay Isles job is to the "
        "right sub-association, not the master one.</p>"
    ),
    sec(
        "What did two hurricanes change here, and what's back to normal now?",
        "<p>Hurricanes Helene and Milton hit the island in quick succession in the fall of 2024, and the Town answered by waiving "
        "storm-related building permit fees outright, a policy the Town Commission stretched one more time as what its planning "
        "director called \"the final extension,\" through December 31, 2025 " + src("lbk-building-division") + " " +
        ext(LBK_WAIVER_EXT_URL, "Mysuncoast.com, final extension of Longboat Key's permit-fee waiver") + ". As of October 2026 that "
        "waiver has lapsed, so a driveway, pool deck or paver job that still traces back to 2024's storm damage now pays the same "
        "permit fee as any other project. The island sits inside the Southwest Florida Water Management District's area-wide "
        "shortage order too, which currently limits irrigation to one day a week by street address, a schedule new sod gets a short "
        "grace period from and " + svc("artificial-turf") + " skips once it's installed and rinsed in " +
        src("swfwmd-restrictions") + ".</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Does the county line through Longboat Key change which office issues a driveway permit?",
        "No. The Town's Planning, Zoning & Building office issues the rights-of-way use permit and reviews the zoning exception for on-grade work no matter which side of the Sarasota-Manatee county line a lot sits on. The county line affects things like property taxes and voting precincts, not who signs off on a driveway or a patio."
    ),
    faq(
        "Can I pour a patio or replace a driveway on grade without a Town permit?",
        "Not automatically. Section 150.30(D)(11) calls driveways, decks and patios directly on grade minor work, but it still has to meet specific zoning criteria and clear a zoning department exception, and the same scope can pull in a full permit, or a FEMA tracking permit, once it's part of a larger project or sits below base flood elevation."
    ),
    faq(
        "How much of my Longboat Key lot has to stay open?",
        "At least 50 percent of the gross land area under the Town's own open-space rule. A driveway, paved or not, and a pool don't count toward that figure, and a licensed design professional has to verify the calculation on the site plan before a permit moves forward."
    ),
    faq(
        "Is there a height limit on a retaining wall here?",
        "Yes. A Longboat Key retaining wall is allowed only to achieve the code's required one-to-four slope over at least four feet, and it can't exceed eight feet regardless of how much grade it's holding back. Add a fence on top and the combined height is measured from the lower grade."
    ),
    faq(
        "Does Bay Isles have its own rule for driveways or pavers?",
        "No specific driveway or paver rule turned up in its recorded documents. Bay Isles' 1976 declaration delegates architectural and construction approval to whichever neighborhood or condominium association covers that part of the community, with the master association stepping in only if that smaller one fails to act."
    ),
    faq(
        "How do you pick the best concrete contractor on Longboat Key?",
        "Start with the state's DBPR license lookup, then ask how the bid handles Section 150.30's zoning exception for on-grade work and the FDOT review that applies if the apron touches Gulf of Mexico Drive. A contractor who can't walk through that process probably hasn't worked on the island before."
    ),
]

HUB = page(
    "/longboat-key-fl/", "city",
    "Concrete, Pavers & Turf Contractor on Longboat Key, FL",
    "Concrete, pavers and turf on Longboat Key, FL: the Town's §57.03 right-of-way permit, the 50% open-space rule and FDOT on Gulf of Mexico Drive, Oct. 2026.",
    "Concrete, Pavers and Artificial Turf for Longboat Key Homes",
    capsule(
        "Opera's Sarasota unit builds concrete, pavers and turf on Longboat Key, the incorporated town that spans Sarasota and Manatee "
        "counties, where the Town itself, not either county, permits driveways and on-grade patios under its own zoning code. As of "
        "October 2026, Gulf of Mexico Drive answers to FDOT, and the island's Canaveral dune sand drains faster than the mainland's "
        "flatwoods soil."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Longboat Key",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/saltwater-pools-and-coastal-salt-air-hardscape/", "Salt air and coastal hardscape"),
        ("/siesta-key-fl/", "Concrete, pavers and turf on Siesta Key"),
        ("/sarasota-fl/", "Concrete, pavers and turf in Sarasota"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf on Longboat Key, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways on Longboat Key, FL – Width & FDOT",
    "meta": "Concrete driveways on Longboat Key, FL cap width at 12 or 24 feet under §158.100; market range is " + price("concrete-driveway") + " per " + per("concrete-driveway") + ", October 2026.",
    "h1": "Pouring a Concrete Driveway on Longboat Key",
    "lede": capsule(
        "A new or replacement concrete driveway on Longboat Key runs " + price("concrete-driveway") + " per " + per("concrete-driveway") +
        " as of October 2026. The Town, not Sarasota or Manatee County, issues the permit, and the apron's own width tops out at "
        "12 feet for a one-way drive or 24 feet for a two-way one under the Town's zoning code."
    ),
    "sections": [
        (
            "Why the width tops out at 12 or 24 feet",
            "<p>Longboat Key's own zoning table sets the limit directly: a drive running one way from a parking space to the street "
            "is capped at 12 feet, and a two-way drive at 24 feet " + src("lbk-code-158.100-drive-width", "Longboat Key Code §158.100") +
            ". That number is the same whether the surface is poured concrete or " + svc("paver-driveways", "pavers") + ", and a "
            "homeowner who wants a wider motor court for a boat trailer or a second vehicle bay usually needs a variance rather than "
            "a bigger apron pour. We measure the existing cut against that table before quoting a widening job, since the Town's "
            "zoning exception review, covered next, assumes the width already fits.</p>"
        ),
        (
            "Why the apron still needs Town sign-off even as 'minor work'",
            "<p>Section 150.30(D)(11) lists a driveway directly on grade as minor work, but the same clause requires it to \"meet "
            "specific zoning criteria and must be approved by zoning department as an exception,\" not simply pass through unreviewed "
            "" + src("lbk-code-150.30-minor-work", "Longboat Key Code §150.30") + ". Any part of the apron in the right-of-way needs "
            "its own permit under Section 57.03 before work starts " + src("lbk-code-57.03-row-permit") + ", and if the driveway ties "
            "into Gulf of Mexico Drive, the island's only through street, that connection is an FDOT matter the Town routes forward "
            "rather than approving on its own " + src("lbk-streets-row") + ".</p>"
        ),
    ],
    "scenario": (
        "Say you have a 16 × 36 ft driveway, 576 sq ft, tying into Gulf of Mexico Drive on a mid-key lot",
        "<p>Say you have a 16 × 36 ft driveway, 576 sq ft, tying into Gulf of Mexico Drive on a mid-key lot. At the market range of " +
        price("concrete-driveway") + " per sq ft, that runs $3,456 to $8,640, narrowing to roughly $4,608 to $6,912 in the typical " +
        price("concrete-driveway", typical=True) + " band. Because the apron meets a state road, the FDOT connection question gets "
        "answered before the Town's own zoning exception is even relevant, and the 24-foot two-way width cap is checked against the "
        "existing cut rather than assumed. A straight repour inside the same footprint moves faster than any plan that widens the "
        "opening.</p>"
    ),
    "faqs": [
        faq(
            "How wide can a two-car driveway be on Longboat Key?",
            "Twenty-four feet for a two-way drive, or 12 feet for a one-way drive from a parking space to the street, under Section 158.100. A wider motor court than that usually needs a variance, not a bigger pour."
        ),
        faq(
            "Does a straight driveway replacement need a Town permit?",
            "The part in the right-of-way does, under Section 57.03, and the driveway as a whole still needs the Section 150.30 zoning exception that applies to any on-grade minor work."
        ),
        faq(
            "Does my driveway need FDOT approval?",
            "Only if it connects to Gulf of Mexico Drive, which is State Road 789 and belongs to FDOT. A driveway opening onto any other Longboat Key street answers to the Town alone."
        ),
    ],
    "sources": SRC,
}

# 2. paver-driveways -----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways on Longboat Key, FL – Open-Space Math",
    "meta": "Paver driveways on Longboat Key, FL still count as impermeable surface against the 50% open-space rule; range " + price("paver-driveway") + " per " + per("paver-driveway") + ", Oct. 2026.",
    "h1": "Paver Driveway Installation on Longboat Key",
    "lede": capsule(
        "A paver driveway on Longboat Key runs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026. "
        "The Town's own definition of impermeable surface names driveways outright, so a paver apron counts the same as a poured one "
        "against the 50 percent open-space minimum every residential lot has to keep."
    ),
    "sections": [
        (
            "Why pavers don't get treated as pervious here",
            "<p>Longboat Key's code defines impermeable surface to include \"structures, pools, driveways, walks, and parking areas,\" "
            "and specifically excludes only permeable wood decks, trellises, thin walls and grass or clay courts " +
            src("lbk-code-158.144-impermeable", "Longboat Key Code §158.144") + ". A brick or concrete paver driveway falls on the "
            "impermeable side of that line regardless of how much water moves through the joints, which matters on a lot already "
            "carrying a pool and a pool deck toward the same open-space figure.</p>"
        ),
        (
            "Why the 50 percent open-space floor limits how wide a motor court can get",
            "<p>Every residential lot has to preserve \"a minimum of 50 percent of the gross land areas\" as open space, with driveways "
            "and pools written out of that count entirely " + src("lbk-code-158.030-open-space-cccl", "Longboat Key Code §158.030") +
            ". A licensed design professional has to verify that math on the site plan, and the house itself answers to a separate "
            "building-coverage cap, 25 percent in R-3SF and up to 30 percent in R-4SF and R-6SF " +
            src("lbk-code-158.062-r3sf", "Longboat Key Code §158.062") + ". On a tight lot, widening a two-car paver driveway to three "
            "cars is a calculation worth running before pavers are ordered, not after.</p>"
        ),
    ],
    "scenario": (
        "Say you have an 18 × 34 ft paver driveway, 612 sq ft, on an R-3SF lot that already carries a pool",
        "<p>Say you have an 18 × 34 ft paver driveway, 612 sq ft, on an R-3SF lot that already carries a pool. At the market range of " +
        price("paver-driveway") + " per sq ft, that runs $6,120 to $18,360, narrowing to roughly $7,344 to $12,240 in the typical " +
        price("paver-driveway", typical=True) + " band depending on the paver and base depth. Because the lot already has a pool and "
        "pool deck working against the same 50 percent open-space floor, the driveway's footprint gets added to that running total "
        "before the paver order goes in, not after the base is already excavated.</p>"
    ),
    "faqs": [
        faq(
            "Do pavers count differently than concrete for Longboat Key's open-space rule?",
            "No. The Town's definition of impermeable surface names driveways directly, with no exception for pavers over a poured slab, so both count the same way against the 50 percent open-space minimum."
        ),
        faq(
            "Who checks the open-space math before a paver driveway is approved?",
            "A licensed design professional has to verify the calculation on the site plan. We run that number against the existing pool, house footprint and any patio before pricing a wider driveway."
        ),
        faq(
            "Can I widen my paver driveway on Longboat Key?",
            "Only if the lot's open-space total has room for it once the pool, house and any patio are already counted. A width beyond the Section 158.100 cap also needs a variance regardless of the open-space math."
        ),
    ],
    "sources": SRC,
}

# 3. concrete-patios -------------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios on Longboat Key, FL – Zoning Exception",
    "meta": "Concrete patios on Longboat Key, FL need a zoning department exception under §150.30 even on grade; market range is " + price("concrete-patio") + " per " + per("concrete-patio") + ".",
    "h1": "Building a Concrete Patio on Longboat Key",
    "lede": capsule(
        "A concrete patio on Longboat Key runs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. "
        "The Town's own minor-work rule still requires a zoning department exception for a patio directly on grade, and a lot below "
        "the current base flood elevation can add a FEMA tracking permit on top of that."
    ),
    "sections": [
        (
            "Why a patio on grade still goes through zoning, not around it",
            "<p>Section 150.30(D)(11) lists \"driveways, decks and patios directly on grade\" as minor work, but the same sentence "
            "requires the project to \"meet specific zoning criteria and must be approved by zoning department as an exception\" " +
            src("lbk-code-150.30-minor-work") + ". That's a different answer than the flat permit exemption some nearby counties "
            "publish for an on-grade slab, and it's why we file the zoning exception request before pouring rather than treat a "
            "lanai extension as automatically exempt.</p>"
        ),
        (
            "When the same patio pulls in a FEMA tracking permit too",
            "<p>FEMA splits the island's flood risk into Zone AE, where a one-in-a-hundred-year flood is expected but wave action "
            "stays modest, and the Coastal High Hazard Zone VE, where that same storm's surf can take out an unreinforced edge " +
            src("fema-coastal-firm", "FEMA's coastal flood-map guidance") + ". If the existing structure is already flagged as "
            "non-compliant with the base flood elevation, or the new patio slab sits below it, the Section 150.30 zoning exception "
            "comes bundled with a FEMA tracking permit rather than standing on its own, which is worth confirming with the Building "
            "Division before the forms go up.</p>"
        ),
    ],
    "scenario": (
        "Say you have a 14 × 20 ft lanai patio extension, 280 sq ft, behind an existing screened cage",
        "<p>Say you have a 14 × 20 ft lanai patio extension, 280 sq ft, behind an existing screened cage. At the market range of " +
        price("concrete-patio") + " per sq ft, that runs $1,680 to $3,640, or roughly $1,960 to $2,800 in the typical " +
        price("concrete-patio", typical=True) + " band for a broom finish sized to the existing screen frame. Before the forms go "
        "up, the zoning department exception under Section 150.30 gets filed, and if the home's elevation certificate shows the "
        "slab would sit below base flood elevation, a FEMA tracking permit goes in alongside it rather than after the fact.</p>"
    ),
    "faqs": [
        faq(
            "Does a small concrete patio on Longboat Key need a permit?",
            "It needs a zoning department exception under Section 150.30, even though the code calls an on-grade patio minor work. That's a review, not a blanket exemption."
        ),
        faq(
            "Why would my patio need a FEMA permit too?",
            "If the existing structure is flagged as non-compliant with the base flood elevation, or the new slab sits below it, the zoning exception comes with a separate FEMA tracking permit."
        ),
        faq(
            "Is Zone VE different from Zone AE for a Longboat Key patio?",
            "Zone VE assumes the same flood odds as Zone AE but with surf strong enough to damage an unreinforced edge, which changes how a low patio wall or edge detail near the water gets built, not just whether a permit is needed."
        ),
    ],
    "sources": SRC,
}

# 4. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios on Longboat Key, FL – Dune Sand Base",
    "meta": "Paver patios on Longboat Key, FL sit on fast-draining Canaveral dune sand, not flatwoods soil; market range is " + price("paver-patio") + " per " + per("paver-patio") + ", Oct. 2026.",
    "h1": "Paver Patios and Walkways on Longboat Key",
    "lede": capsule(
        "A paver patio on Longboat Key runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. The "
        "island's own dune sand drains differently than the mainland's flatwoods soil, and with a median home built in 1980, a lot "
        "of patio work here is a replacement, not a first installation."
    ),
    "sections": [
        (
            "What Canaveral dune sand means for the base under a patio",
            "<p>A soil map check run at the island's coordinates returns Canaveral fine sand, a somewhat poorly to moderately well "
            "drained dune soil with very rapid permeability and a seasonal high water table only 10 to 40 inches down, and only for "
            "two to six months most years " + src("usda-wss") + " " + ext(CANAVERAL_OSD_URL, "NRCS OSD, Canaveral") + ". That's a "
            "faster-draining profile than the Myakka or EauGallie flatwoods soil the unit's mainland towns sit on, which changes "
            "how quickly bedding sand can lose moisture during a hot afternoon pour rather than how much fill the base needs.</p>"
        ),
        (
            "Why a 1980-median lot usually means a redo, not a first patio",
            "<p>Longboat Key's median year structure built is 1980, older than most of the Sarasota unit's mainland towns " +
            ext(LBK_ACS_URL, "Census Reporter, Longboat Key FL") + ". A paver patio job here is commonly tied into an existing "
            "1980s-era concrete slab rather than built from scratch, which means matching a new edge restraint to whatever base is "
            "already compacted under the old pour. " + svc("concrete-patios", "A plain concrete") + " version of the same addition "
            "faces the identical Section 150.30 zoning review either way.</p>"
        ),
    ],
    "scenario": (
        "Say you have a 20 × 18 ft paver patio, 360 sq ft, replacing an older patio behind a 1980s-era home",
        "<p>Say you have a 20 × 18 ft paver patio, 360 sq ft, replacing an older patio behind a 1980s-era home. At the market range "
        "of " + price("paver-patio") + " per sq ft, that runs $3,600 to $6,120, narrowing to roughly $4,320 to $5,760 in the typical "
        "" + price("paver-patio", typical=True) + " band depending on paver size and pattern. Because the lot's base is Canaveral "
        "dune sand rather than flatwoods soil, bedding sand gets watched for moisture loss during the pour window more than the "
        "fill depth does, and tying the new paver edge into the old 1980s slab footprint without a visible seam is usually the "
        "trickier part of the job.</p>"
    ),
    "faqs": [
        faq(
            "Is the soil on Longboat Key different from Sarasota's mainland?",
            "Yes. The island's own soil-map reading comes back Canaveral fine sand, a dune soil with very rapid permeability and a shallow water table for only two to six months a year, unlike the poorly drained flatwoods soil common on the mainland."
        ),
        faq(
            "Why is so much patio work on Longboat Key a replacement?",
            "The island's median home was built in 1980, so a lot of what we see is a paver patio tied into an existing concrete slab from that era rather than a brand-new installation."
        ),
        faq(
            "Does a paver patio need the same zoning review as concrete here?",
            "Yes. Section 150.30's zoning department exception for on-grade minor work applies the same way regardless of whether the finished surface is poured concrete or pavers."
        ),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks on Longboat Key, FL – CCCL & Lighting",
    "meta": "Concrete pool decks on Longboat Key, FL near the Gulf add a CCCL permit and a sea-turtle lighting review; range " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ", Oct. 2026.",
    "h1": "Concrete Pool Deck Installation on Longboat Key",
    "lede": capsule(
        "A concrete pool deck on Longboat Key runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of "
        "October 2026. A deck on a Gulf-front lot can cross Florida's Coastal Construction Control Line, which brings in a state "
        "permit and the Town's own sea-turtle lighting review before the concrete gets priced."
    ),
    "sections": [
        (
            "What the Coastal Construction Control Line adds to a Gulf-front deck",
            "<p>Longboat Key's own site-plan rule flags the overlap directly, requiring a project to note any \"FDEP Coastal "
            "Construction Control Line permit\" it needs on top of the Town's own sign-off " +
            src("lbk-code-158.030-open-space-cccl") + ". The CCCL program exists to keep a private pool deck or patio from "
            "undercutting a dune or blocking public beach access, and DEP's own application process runs on its own schedule, "
            "separate from when the Town clears the zoning exception " + src("fdep-cccl-program", "FDEP's CCCL program") + " " +
            src("fdep-cccl-apply", "FDEP's CCCL application page") + ".</p>"
        ),
        (
            "Why deck lighting answers to a sea-turtle rule, not just the slab",
            "<p>New development seaward of the control line also pulls in Chapter 100's sea-turtle lighting review, which looks "
            "specifically at fixtures visible from the beach, pool-area sconces and deck lights included " +
            src("lbk-code-100.04-cccl-lighting", "Longboat Key Code §100.04") + ". A deck light aimed out toward the Gulf, or an "
            "uncovered pool-equipment light, is the kind of detail that can hold up a final inspection longer than the concrete "
            "pour itself, so we plan fixture placement against that rule before the deck's layout is finished.</p>"
        ),
    ],
    "scenario": (
        "Say you have a 28 × 30 ft pool deck, 840 sq ft, around a cage on a lot close enough to the Gulf to cross the control line",
        "<p>Say you have a 28 × 30 ft pool deck, 840 sq ft, around a cage on a lot close enough to the Gulf to cross the control "
        "line. At the market range of " + price("concrete-pool-deck") + " per sq ft, that runs $4,200 to $12,600, narrowing to "
        "roughly $5,880 to $10,080 in the typical " + price("concrete-pool-deck", typical=True) + " band for a textured, "
        "slip-resistant finish pitched to a drain. Because part of the deck sits seaward of the CCCL, the state permit question "
        "gets answered before the Town's zoning exception is even relevant, and any deck or equipment lighting fixture gets "
        "checked against the sea-turtle rule rather than finalized by habit.</p>"
    ),
    "faqs": [
        faq(
            "Does my Longboat Key pool deck need a state permit as well as a Town one?",
            "If it crosses Florida's Coastal Construction Control Line, yes, a DEP permit is required, and the Town's own site-plan rule requires that permit to be noted before its own sign-off is relevant."
        ),
        faq(
            "Does pool deck lighting need special approval near the Gulf?",
            "New development seaward of the control line pulls in the Town's sea-turtle lighting review under Chapter 100, which looks at fixtures visible from the beach, including pool and deck lights."
        ),
        faq(
            "Is my Longboat Key lot in a flood zone that affects the deck?",
            "Possibly. On FEMA's coastal maps, Zone AE carries a lighter wave hazard than the Coastal High Hazard Zone VE, where surf is strong enough to damage an unreinforced deck edge during a major storm; the dividing line can split a single block."
        ),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ----------------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers on Longboat Key, FL – Bay Isles Review",
    "meta": "Pool deck pavers on Longboat Key, FL in Bay Isles answer to the sub-association's own sign-off; market range is " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ".",
    "h1": "Travertine and Paver Pool Decks on Longboat Key",
    "lede": capsule(
        "Pool deck pavers or travertine on Longboat Key run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as "
        "of October 2026. In Bay Isles, the deck design answers to the neighborhood or condominium association first, and salt air "
        "off either shore shortens how long a sealer or edge restraint holds up."
    ),
    "sections": [
        (
            "Why a Bay Isles pool deck starts with the sub-association, not the Town",
            "<p>Bay Isles' own governing document, recorded in April 1976, hands architectural and construction approval to "
            "whichever neighborhood or condominium association covers that section of the community, not to one island-wide board "
            "" + ext(BAYISLES_DECL_URL, "Bay Isles Association, Inc., Declaration of Maintenance Covenants and Restrictions") +
            ". The master Bay Isles Association only takes over that approval if the smaller association fails to exercise it, "
            "which is why pricing a travertine overlay there starts with identifying the right sub-association rather than "
            "assuming one island-wide process covers every section.</p>"
        ),
        (
            "What salt air off either shore does to joints and sealer",
            "<p>For bridge design, FDOT draws its marine-environment line at 2,500 feet from a chloride level above 2,000 parts per "
            "million " + src("fdot-sdg") + ", a threshold that, on a key this narrow, puts both the Gulf shore and the bay shore of "
            "most lots inside the same salt-heavy air. The structural concrete under a travertine or paver deck doesn't need "
            "anything different for that, but an unsealed joint or a bare metal edge restraint shows the salt faster here than it "
            "would a few miles inland, which is why " + svc("paver-sealing", "resealing") + " a Bay Isles deck tends to land on a "
            "shorter cycle than the same job well off the water.</p>"
        ),
    ],
    "scenario": (
        "Say you have a 700 sq ft travertine pool deck overlay on an older deck inside Bay Isles",
        "<p>Say you have a 700 sq ft travertine pool deck overlay on an older deck inside Bay Isles. At the market range of " +
        price("pool-deck-pavers") + " per sq ft, that comes out between $8,400 and $21,000, tightening toward $9,800 to $15,400 "
        "inside the typical " + price("pool-deck-pavers", typical=True) + " band once the stone and pattern are picked. Before the "
        "overlay is priced, the homeowner's neighborhood or condominium association gets identified so the right body reviews the "
        "exterior change, and the deck's finished look still has to clear the Town's own site-plan rules on top of whatever the "
        "association decides.</p>"
    ),
    "faqs": [
        faq(
            "Who approves a pool deck change inside Bay Isles?",
            "The neighborhood or condominium association covering that part of the community, under Bay Isles' 1976 declaration. The master Bay Isles Association only steps in if that smaller association doesn't act."
        ),
        faq(
            "Why does salt air matter more here than a few miles inland?",
            "FDOT's own marine-environment threshold, water above 2,000 parts per million chloride within 2,500 feet, covers nearly the whole island on one shore or the other, which is why sealer and edge-restraint choices differ here."
        ),
        faq(
            "Does a Bay Isles pool deck still need a Town permit?",
            "Yes. The sub-association's architectural approval runs alongside the Town's own review, not instead of it, and either process can still trigger the state CCCL permit on a Gulf-front parcel."
        ),
    ],
    "sources": SRC,
}

# 7. stamped-concrete -------------------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete on Longboat Key, FL – Storm Rebuilds",
    "meta": "Stamped concrete on Longboat Key, FL often traces to 2024's storm damage; market range is " + price("stamped-concrete") + " per " + per("stamped-concrete") + ", as of October 2026.",
    "h1": "Stamped Concrete Driveways and Patios on Longboat Key",
    "lede": capsule(
        "Stamped concrete on Longboat Key runs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October "
        "2026. A good share of the stamped work here still traces back to Hurricanes Helene and Milton in 2024, even though the "
        "Town's storm-related permit-fee waiver has already expired."
    ),
    "sections": [
        (
            "Why so much stamped concrete here traces back to 2024's storms",
            "<p>The Town waived storm-related building permit fees outright after Hurricanes Helene and Milton, a policy its "
            "planning director called \"the final extension\" when the Commission stretched it through December 31, 2025 " +
            src("lbk-building-division") + " " + ext(LBK_WAIVER_EXT_URL, "Mysuncoast.com, Longboat Key's final permit-fee waiver "
            "extension") + ". As of October 2026 that waiver has lapsed, so a stamped driveway or pool-deck apron replaced today "
            "pays the standard permit fee even if the original cracking or saltwater intrusion dates back to the 2024 storms, a "
            "distinction worth knowing before budgeting the permit line on a rebuild.</p>"
        ),
        (
            "Why color choice carries more weight on a lot facing open water",
            "<p>A dark integral color absorbs more heat off direct sun than a light one does, and on a lot facing the Gulf or the "
            "bay, that same dark surface also reflects glare back up off the water for a few extra hours a day compared with an "
            "inland yard shaded by neighboring roofs and canopy. We talk homeowners here toward a lighter tan or buff base color "
            "with a simple, shallow-relief pattern more often than the deeper, high-contrast stamps that read well on a shaded "
            "mainland lot, since a busy pattern under that much reflected light can look washed out by midafternoon rather than "
            "sharper.</p>"
        ),
    ],
    "scenario": (
        "Say a 450 sq ft stamped-concrete entry walk and pool-deck apron needs rebuilding after storm damage",
        "<p>Say a 450 sq ft stamped-concrete entry walk and pool-deck apron needs rebuilding after storm damage. Pricing it at " +
        price("stamped-concrete") + " per sq ft puts the job between $3,600 and $8,550, settling closer to $5,400 to $7,200 inside "
        "the typical " + price("stamped-concrete", typical=True) + " band once the pattern and color count are set. Since the "
        "Town's fee waiver expired at the close of 2025, this permit gets filed at the standard rate rather than the waived one "
        "that covered the original 2024 storm damage, and a lighter buff tone with a shallow, single-pattern stamp is what we'd "
        "steer toward given how much open water the lot faces.</p>"
    ),
    "faqs": [
        faq(
            "Is Longboat Key still waiving permit fees for storm-damaged concrete?",
            "No. The Town Commission extended the waiver one last time through December 31, 2025, and as of October 2026 it has expired, so a storm-related rebuild now pays the standard permit fee."
        ),
        faq(
            "What color works best for stamped concrete facing open water?",
            "A lighter tan or buff tone with a shallow, simple pattern tends to hold up visually better against reflected glare off the Gulf or the bay than a dark, high-contrast stamp, which can look washed out in that much direct light."
        ),
        faq(
            "Does stamped concrete cost more than plain concrete here?",
            "The market range runs " + price("stamped-concrete") + " per sq ft here against " + price("concrete-driveway") + " for a plain pour, a gap that comes from the integral pigment, release agent and stamping time rather than anything about the permit or FDOT review underneath."
        ),
    ],
    "sources": SRC,
}

# 8. artificial-turf -------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf on Longboat Key, FL – Watering Order",
    "meta": "Artificial turf on Longboat Key, FL skips the current once-a-week watering order and must clear a 10-ft waterbody setback; range " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
    "h1": "Artificial Turf Installation on Longboat Key",
    "lede": capsule(
        "Artificial turf on Longboat Key runs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October 2026. "
        "The island answers to the same one-day-a-week watering order as the rest of Sarasota and Manatee counties, and Florida's "
        "newer turf rule adds its own 10-foot setback from the water on a canal-front lot."
    ),
    "sections": [
        (
            "Why turf skips the current watering schedule",
            "<p>Longboat Key sits inside the Southwest Florida Water Management District's area-wide shortage order, which "
            "currently limits irrigation to one day a week, assigned by street address, in an overnight or late-night window " +
            src("swfwmd-restrictions") + ". New sod gets a short grace period before it drops onto that same one-day calendar, "
            "and a finished turf lawn simply has nothing left to schedule against the order, a fact that carries extra weight on "
            "the island's smaller lots where every square foot of lawn is visible from the street or a neighbor's window.</p>"
        ),
        (
            "What the state's turf rule requires near the water",
            "<p>Florida's installation standard, effective since May 19, 2026, sets the specifics directly: natural infill, a "
            "washed base, no in-ground irrigation run to the turf itself, and a 10-foot setback from any waterbody unless a "
            "seawall separates the lawn from the water " + src("dep-rule", "DEP Rule 62-308.100") + " " +
            src("fs125572", "F.S. §125.572") + ". On a canal-front Longboat Key lot, that setback is usually what decides where "
            "the turf panel ends and the existing shoreline planting begins, and the same rule keeps new turf outside a "
            "protected tree's drip line unless an arborist signs off on it.</p>"
        ),
    ],
    "scenario": (
        "Say you have a 320 sq ft side-yard turf strip on a canal-front lot",
        "<p>Say you have a 320 sq ft side-yard turf strip on a canal-front lot. At the market range of " + price("artificial-turf") +
        " per sq ft, that runs $3,200 to $8,000, or roughly $3,840 to $5,760 in the typical " + price("artificial-turf", typical=True) +
        " band for a washed-rock base and natural infill. Because the yard backs onto a canal, the turf panel's edge gets set 10 "
        "feet back from the waterline unless a seawall already separates the yard from the water, and no irrigation line gets run "
        "to the turf area itself, since the state rule treats that as a separate violation from the setback.</p>"
    ),
    "faqs": [
        faq(
            "Does artificial turf help with Longboat Key's current watering restrictions?",
            "It sidesteps them entirely. The island is under SWFWMD's one-day-a-week watering order, which turf never has to follow once it's installed, unlike new sod, which gets only a short grace period before the same schedule applies."
        ),
        faq(
            "How close to the water can I install turf on a Longboat Key canal lot?",
            "Florida's turf rule requires at least a 10-foot setback from any waterbody, unless a seawall separates the lawn from the water, on top of whatever setback the Town's own zoning code requires."
        ),
        faq(
            "Can I run sprinklers to a new turf area here?",
            "No. The state's turf installation standard bars in-ground irrigation run to the turf itself, which is separate from the waterbody setback and from any watering-day restriction that still applies to the rest of the yard."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
