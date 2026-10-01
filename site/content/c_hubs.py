# -*- coding: utf-8 -*-
"""Cost hub (with calculator) and the permits & HOA hub."""
import json

from _data import SERVICES, SERVICE_ORDER, PRICES, PRICE_DATE
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, post, compare, src, ext, price, per, price_note, contact
from _posts import COST_PAGES, cost_for

CALC_RATES = {
    "concrete-driveway": [PRICES["concrete-driveway"][2], PRICES["concrete-driveway"][3], 4],
    "concrete-driveway-6": [8, 20, 6],
    "stamped-concrete": [PRICES["stamped-concrete"][2], PRICES["stamped-concrete"][3], 4],
    "concrete-patio": [PRICES["concrete-patio"][2], PRICES["concrete-patio"][3], 4],
    "concrete-slab": [PRICES["concrete-slab"][2], PRICES["concrete-slab"][3], 4],
    "paver-driveway": [PRICES["paver-driveway"][2], PRICES["paver-driveway"][3], 0],
    "paver-patio": [PRICES["paver-patio"][2], PRICES["paver-patio"][3], 0],
    "pool-deck-pavers": [PRICES["pool-deck-pavers"][2], PRICES["pool-deck-pavers"][3], 0],
    "artificial-turf": [PRICES["artificial-turf"][2], PRICES["artificial-turf"][3], 0],
    "paver-sealing": [PRICES["paver-sealing"][2], PRICES["paver-sealing"][3], 0],
}
CALC = f"""<form id="calc" class="lead" data-rates='{json.dumps(CALC_RATES)}' aria-describedby="calc-out" style="margin:1.2em 0">
<div class="full"><label for="c-kind">Project</label><select id="c-kind" name="kind">
<option value="concrete-driveway">Concrete driveway, 4 in</option><option value="concrete-driveway-6">Concrete driveway, 6 in (trucks, RV)</option><option value="stamped-concrete">Stamped concrete</option>
<option value="concrete-patio">Concrete patio</option><option value="concrete-slab">Concrete slab or pad</option><option value="paver-driveway">Paver driveway</option><option value="paver-patio">Paver patio</option>
<option value="pool-deck-pavers">Pool deck pavers</option><option value="artificial-turf">Artificial turf</option><option value="paver-sealing">Paver cleaning and sealing</option></select></div>
<div><label for="c-len">Length (ft)</label><input id="c-len" name="len" inputmode="decimal"></div><div><label for="c-wid">Width (ft)</label><input id="c-wid" name="wid" inputmode="decimal"></div>
<div class="full"><label for="c-area">Or total area (sq ft)</label><input id="c-area" name="area" inputmode="decimal"></div>
<div class="full"><button class="btn" type="submit">Estimate the range</button></div>
<p id="calc-out" class="full note" role="status" aria-live="polite">Enter a length and width, or an area.</p></form>"""


def cost_hub():
    rows = []
    for k in SERVICE_ORDER:
        S = SERVICES[k]
        pk = S["price"]
        r = cost_for(k)
        rows.append([a(r, S["name"]) if r else a(S["route"], S["name"]), price(pk), per(pk), price(pk, True)])
    sizes = [["One-car (10 × 20 ft)", "200", f"${200 * PRICES['concrete-driveway'][0]:,}–${200 * PRICES['concrete-driveway'][1]:,}", f"${200 * PRICES['paver-driveway'][0]:,}–${200 * PRICES['paver-driveway'][1]:,}"],
             ["Two-car (20 × 20 ft)", "400", f"${400 * PRICES['concrete-driveway'][0]:,}–${400 * PRICES['concrete-driveway'][1]:,}", f"${400 * PRICES['paver-driveway'][0]:,}–${400 * PRICES['paver-driveway'][1]:,}"],
             ["Two-car (24 × 24 ft)", "576", f"${576 * PRICES['concrete-driveway'][0]:,}–${576 * PRICES['concrete-driveway'][1]:,}", f"${576 * PRICES['paver-driveway'][0]:,}–${576 * PRICES['paver-driveway'][1]:,}"],
             ["Three-car (24 × 36 ft)", "864", f"${864 * PRICES['concrete-driveway'][0]:,}–${864 * PRICES['concrete-driveway'][1]:,}", f"${864 * PRICES['paver-driveway'][0]:,}–${864 * PRICES['paver-driveway'][1]:,}"]]
    body = "".join([
        sec("Florida price ranges for every service we offer",
            f"<p>The table below lists the installed market range for each service as of {PRICE_DATE}, compiled from Angi's Orlando and Tampa city pages, HomeGuide's national guides and published Florida contractor pricing. Each service name links to its own cost guide with worked examples and the factors that move the price.</p>"
            + table(f"Installed cost by service, Florida, {PRICE_DATE}", ["Service", "Market range", "Unit", "Typical middle"], rows, price_note())),
        sec("What does a new driveway cost by size?",
            f"<p>Standard driveway sizes come from HomeGuide and Angi: a one-car driveway is about 200 to 288 square feet, a two-car 400 to 576 and a three-car 864 to 900 ({src('homeguide-concrete-driveway', 'HomeGuide')}). Multiplying by the market ranges gives the spread below. Angi's Orlando page puts the average concrete driveway project at $6,490, inside the two-car band ({src('angi-driveway-orlando', 'Angi Orlando, May 2026')}).</p>"
            + table("Driveway totals by size, before demolition", ["Driveway", "Sq ft", f"Concrete at {price('concrete-driveway')}", f"Pavers at {price('paver-driveway')}"], sizes,
                    "Arithmetic on the published ranges. Removing an old driveway typically adds $3–$8 per sq ft nationally and $5–$8 in Angi's Orlando data.")
            + f"<p>For the full breakdown, see the {a('/concrete-driveway-cost/', 'concrete driveway cost guide')} and the {a('/paver-driveway-cost/', 'paver driveway cost guide')}.</p>"),
        sec("Quick calculator", "<p>Pick a project, enter the size, and the calculator multiplies it by the typical middle of the Florida range. For concrete it also estimates the volume in cubic yards. It's a planning number, not a quote.</p>" + CALC),
        sec("What moves the price up or down?",
            "<p>Per-square-foot ranges hide the things that actually change a bid. These are the line items that most often separate a low quote from a high one:</p>"
            + table("Common cost drivers", ["Factor", "Why it matters", "Typical effect"],
                    [["Demolition and haul-off", "Old concrete or pavers removed and disposed of", "$3–$8 per sq ft (national); $5–$8 Orlando"],
                     ["Thickness and reinforcement", "6 in for heavy vehicles; rebar adds strength at joints", "4 in $6–$15, 6 in $8–$20 per sq ft; rebar +$1–$3"],
                     ["Base and fill", "Soft flatwoods soil needs more compacted base", "Angi Tampa lists +$1–$2 per sq ft for subbase on sandy soil"],
                     ["Finish", "Broom vs. exposed aggregate vs. stamped and colored", "Stamped $8–$19 vs. plain $6–$10 per sq ft"],
                     ["Access", "Pump truck or wheelbarrows when a truck can't reach", "Pump trucks $150–$600 per pour in Polk County data"],
                     ["Permits", "Right-of-way and zoning permits for aprons and pavers", "$50–$200 in national data; local fees vary"]],
                    "Ranges from HomeGuide, Angi and published Florida sources listed on this page.")
            + f"<p>Ready-mix concrete itself is a small share of the price: Angi lists $120 to $170 per cubic yard for all-purpose concrete in Orlando, and a 400-square-foot, 4-inch driveway needs about 5 yards ({src('angi-driveway-orlando', 'Angi Orlando')}). Labor, base work, forming, finishing, the pump or buggy if the truck can't reach, and the cleanup make up most of the rest, which is why a crew's method shows up in the price more than the concrete does.</p>"),
        sec("Pool deck options compared by cost",
            f"<p>Pool decks have the widest spread of any project because the choices run from a coating on the old slab to a full travertine rebuild. National and Central Florida data line up like this ({src('homeguide-pool-deck', 'HomeGuide pool deck')}, {src('poolmechanic-pooldeck-cfl', 'Central Florida resurfacing data')}):</p>"
            + table("Pool deck surfaces, installed cost per sq ft", ["Option", "Range", "What you get"],
                    [["Acrylic or Kool Deck-style coating on existing concrete", "$3–$6", "New textured surface; the old slab stays"],
                     ["Spray deck or micro-topping overlay", "$4–$8", "Thicker decorative overlay; hides small cracks"],
                     ["New poured concrete deck", "$5–$15", "Fresh slab; finish and texture are your choice"],
                     ["Stamped concrete deck", "$8–$19", "Pattern and color; needs resealing"],
                     ["Concrete pavers", "$8–$17", "Individual units; easy spot repairs"],
                     ["Travertine pavers", "$13–$30", "Natural stone; stays comfortable underfoot"]],
                    "Ranges from HomeGuide (Dec 2025 and Apr 2026) and a Central Florida pool-deck guide (Jul 2026); removal of an old deck adds about $5 per sq ft.")
            + f"<p>The {a('/pool-deck-cost/', 'pool deck cost guide')} works through an 800 and a 1,200 square-foot deck for each option.</p>"),
        sec("Repair and upkeep costs",
            "<p>Not every budget conversation is about something new. These are the common repair and maintenance jobs and what published data says they cost:</p>"
            + table("Repair and maintenance, market ranges", ["Job", "Range", "Source"],
                    [["Concrete crack filling", "$0.50–$5 per linear ft", "Angi Orlando, Jun 2026"],
                     ["Driveway resurfacing", "$3–$5 per sq ft national; $5–$10 Orlando", "HomeGuide; Angi Orlando"],
                     ["Mudjacking a sunken slab", "$3–$8 per sq ft; about $500 minimum", "Angi Orlando, May 2026"],
                     ["Polyurethane foam lifting", "$8–$25 per sq ft", "HomeGuide, Nov 2025"],
                     ["Paver cleaning, re-sanding and sealing", f"{price('paver-sealing')} per sq ft", "HomeGuide; Central Florida data"],
                     ["Paver releveling", "$6–$12 per sq ft for larger areas", "HomeGuide driveway repair"]])
            + f"<p>See {a('/concrete-repair-cost/', 'concrete repair costs')} and {a('/paver-sealing-cost/', 'paver sealing costs')} for detail, or {compare('resurface-vs-replace-concrete', 'resurface vs. replace')} for the decision itself.</p>"),
        sec("Patios: concrete, stamped or pavers?",
            f"<p>For a 20 × 20 ft patio (400 sq ft), the market ranges work out to roughly $2,400–$5,200 for broom-finish concrete, $3,200–$7,600 for stamped concrete and $4,000–$6,800 for concrete pavers. "
            "Concrete is the budget choice; stamped concrete buys a pattern for less than pavers but needs resealing and can't be spot-repaired invisibly; pavers cost the most up front and are the easiest to repair or extend later. "
            f"The {a('/concrete-patio-cost/', 'concrete patio')}, {a('/stamped-concrete-cost/', 'stamped concrete')} and {a('/paver-patio-cost/', 'paver patio')} guides cover each in detail.</p>"),
        sec("Artificial turf vs. sod over time",
            f"<p>Turf costs far more on day one: {price('artificial-turf')} per square foot installed against a dollar or two for sod. The return comes from water, mowing and replacement sod over the following years, and in 2026 that math changed for many homeowners because Sarasota, Manatee and Lake counties spent the year under emergency once-a-week watering orders. "
            f"The {a('/artificial-turf-cost/', 'artificial turf cost guide')} and {compare('artificial-turf-vs-sod', 'turf vs. sod comparison')} run the numbers.</p>"),
        sec("Is pricing different in Orlando and Sarasota?",
            "<p>Published data shows the two metros close together. Angi's 2026 pages put the average concrete driveway at $6,490 in Orlando and $6,458 in Tampa, the nearest metro Angi publishes for the Sarasota side; its Tampa page cites $8 to $20 per square foot against $5 to $21 in Orlando. "
            f"We don't price by ZIP code. What changes between a Lakewood Ranch driveway and a Kissimmee one is the soil, the HOA's material rules and the permit desk, not the rate ({src('angi-driveway-tampa', 'Angi Tampa')}).</p>"),
        sec("Budgeting a bigger outdoor project",
            "<p>Driveway, pool deck, patio and turf rarely get built in the same year, and they don't have to. The order matters more than the timing: anything that needs heavy equipment or a concrete truck to cross the yard goes first, then the hardscape closest to the house, then turf and planting last so nothing drives over finished work. "
            "A paver patio can be laid with a border that a later extension ties into without a visible seam, and a driveway can be poured with a sleeve under it for future irrigation or lighting wire, which costs little now and saves cutting concrete later. "
            f"The guide to {post('how-to-budget-a-backyard-hardscape-project-in-phases', 'budgeting a backyard project in phases')} lays out a three-year plan, and {post('does-a-new-driveway-add-home-value', 'whether a new driveway adds home value')} covers resale.</p>"),
        sec("Every cost guide", ul([a(r, f"{SERVICES[s]['name']} cost") for r, (kw, mod, s) in COST_PAGES.items()])
            + f"<p>Comparisons help with the bigger decisions: {compare('pavers-vs-concrete-driveway', 'pavers vs. concrete driveway')}, {compare('stamped-concrete-vs-pavers', 'stamped concrete vs. pavers')} and {compare('artificial-turf-vs-sod', 'artificial turf vs. sod')}.</p>"),
    ])
    faqs = [faq("Why do quotes for the same driveway vary so much?", "Because they often describe different jobs. One bid may include demolition, a thicker slab, rebar, a compacted base and permits; another may not. Compare the line items, not the totals, and ask each contractor for base depth, thickness, joint spacing and who pulls the permit."),
            faq("Is a deposit normal for concrete or paver work in Florida?", "Yes, and Florida law sets guardrails: under F.S. 489.126, a contractor who takes more than 10% up front must apply for permits within 30 days and start work within 90 days after the permits are issued, unless the contract says otherwise."),
            faq("How much concrete does a two-car driveway need?", "A 20 × 20 ft driveway at 4 inches thick is about 4.9 cubic yards before waste; most crews order 5 to 5.5 yards. At 6 inches the same driveway needs about 7.4 yards. The calculator on this page does the math for any size."),
            faq("Are permit fees included in the price?", "They should be listed. Right-of-way and zoning permit fees in our area range from about $40 to $250 depending on the city, plus inspection fees in some places. Our estimates say who applies and whether the fee is included, so you can compare bids on equal terms."),
            faq("Does the paver price include the base?", "A complete paver price includes excavation, compacted aggregate base, bedding sand, edge restraint, cutting, compaction and joint sand. If a bid quotes pavers per square foot without listing the base depth, ask; the base is where cheap paver jobs save money and where they fail."),
            faq("Why is artificial turf priced so differently from one quote to the next?", "Product weight and pile height, base depth, infill type, demolition of the old lawn and edging all vary. In Florida, the 2026 state rule requires a washed rock base and natural infill on residential lawns, which removes some of the cheapest shortcuts."),
            faq("Do prices include sealing?", "Not always. Sealing new concrete is optional and often listed separately at $1 to $3 per square foot in national data. Pavers are usually sealed after efflorescence has had time to appear, so sealing may be a separate visit.")]
    return page("/cost/", "price", "Concrete, Paver & Turf Costs in Florida (2026)", "2026 Florida price ranges for concrete driveways, pavers, pool decks, stamped concrete, walls and turf, with driveway totals by size and a calculator.",
                "What concrete, pavers and turf cost in Florida",
                capsule(f"As of {PRICE_DATE}, Florida market data puts installed concrete driveways at {price('concrete-driveway')} per square foot, paver driveways at {price('paver-driveway')}, paver patios at {price('paver-patio')} and artificial turf at {price('artificial-turf')}. A typical 400 sq ft two-car concrete driveway lands between about $2,400 and $6,000 before demolition."),
                body, faqs=faqs, crumb="Cost guides", form=True, wide=False,
                sources=["angi-driveway-orlando", "angi-driveway-tampa", "homeguide-concrete-driveway", "homeguide-driveway-pavers", "homeguide-paver-patio", "homeguide-artificial-grass", "homeguide-stamped", "homeguide-concrete-removal", "lakeland-readymix", "fs489-126"])


def permits_hub():
    body = "".join([
        sec("What changed on July 1, 2026",
            f"<p>Florida's HB 803 requires local governments to exempt single-family owners and their contractors from <em>building</em> permits for work valued under $7,500, with exceptions for electrical, plumbing, mechanical, gas, structural and flood-zone work. "
            f"It does not exempt engineering, zoning or right-of-way permits. Orlando's own guide says land-development and civil permits \"are not included in the exemption\" ({src('orlando-hb803-guide', 'City of Orlando HB 803 guide')}). For driveways and pavers, those are exactly the permits that apply.</p>"),
        sec("Do you need a permit for a driveway, patio or pavers?",
            "<p>Usually for a driveway, sometimes for a patio, and it depends on the city for pavers. Any work on the apron between your property line and the street is in the public right-of-way, and every jurisdiction we checked requires a permit for it. On-grade patios and pavers on private property range from no permit at all to a zoning or engineering permit.</p>"
            + table("Permit snapshot by jurisdiction (checked October 2026)", ["Jurisdiction", "Driveway / apron", "Patio or pavers on your lot", "Notes"],
                    [[f"{ext('https://www.orlando.gov/Building-Development/Permits-Inspections/Other-Permits/Apply-for-an-Engineering-Permit', 'City of Orlando')}", "Engineering permit; apron 6 in, 3,000 psi", "Engineering permit for pavers or concrete", "Turf also needs an engineering permit"],
                     [f"{ext('https://www.orangecountyfl.net/PermitsLicenses/DoINeedaPermit.aspx', 'Orange County')}", "Right-of-way permit", "Permit for concrete; pavers need a zoning permit only", "Engineered retaining walls over code thresholds"],
                     ["City of Kissimmee", "Driveway/Sidewalk Construction permit", "Slab permit type exists; pavers not listed", "Engineering 407-518-2278"],
                     ["City of Winter Park", "Driveway permit", "Permit for hard-surface decks and walls", "50% impervious limit; half the front yard pervious"],
                     ["City of Sanford", "Driveway permit, $250 fee", "Not published", "50% impervious limit"],
                     ["City of Clermont", "Driveway zoning approval", "Concrete patio permit type on grade", "Retaining walls always permitted; engineered over 3 ft"],
                     ["City of St. Cloud", "Public Works right-of-way permit", "Pavers handled by Public Works", "Right-of-way basic fee $110"],
                     ["City of Sarasota", "City engineer permit", "No flatwork exemption published", "Impervious 60–75% by zone; 70% on coastal islands"],
                     ["Sarasota County", "Right-of-Way Use Permit and culvert permit", "Check with the county", "Engineered drawings for walls over 4 ft"],
                     ["Manatee County", "Access and drainage (driveway/culvert) permit; 6 in to the right-of-way line", "Non-structural patio: no permit", "Masonry walls need a permit"],
                     ["City of Bradenton", "Public Works approval and affidavit", "Zoning permit for paved areas", "Impervious 50–70% by zone"]],
                    "Summaries of each jurisdiction's published rules; always confirm with the permit office before work starts.")),
        sec("Impervious surface limits: the rule that stops patio expansions",
            "<p>Several cities cap how much of a lot can be covered by roofs, driveways, patios and pool decks. Winter Park allows 50% of the lot and requires half the front yard to stay pervious; Sanford caps most single-family zones at 50% and counts artificial turf as impervious; Bradenton allows 50% in R-1 and up to 70% in denser zones; the City of Sarasota sets 60% to 75% by zone. "
            f"Winter Garden makes you file an impervious-area worksheet for any added hard surface ({src('wintergarden-isr-worksheet', 'Winter Garden worksheet')}). Before you design a bigger patio, it's worth knowing how close your lot already is.</p>"),
        sec("HOA and architectural review", f"<p>Master-planned communities add their own approval. Lakewood Ranch routes modification requests through Town Hall; Celebration's architectural review committee meets monthly; Baldwin Park's guidelines even dictate the first 7 feet of an alley driveway. "
            f"A 2026 change to Florida law means an HOA can no longer require you to get a building permit before it reviews your application ({src('fs720-3035', 'F.S. 720.3035')}). For artificial turf, F.S. 720.3045 limits HOA control only over turf that can't be seen from the street or neighbors ({src('fs720-3045', 'F.S. 720.3045')}). "
            f"More in {post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for pavers or a driveway')} and {post('lakewood-ranch-arc-approval-hardscape', 'Lakewood Ranch approvals')}.</p>"),
        sec("County-by-county guides", ul([post("orange-county-orlando-driveway-patio-permits", "Orlando and Orange County"), post("osceola-county-kissimmee-st-cloud-permits", "Kissimmee, St. Cloud and Osceola County"),
                                           post("seminole-county-driveway-patio-permits", "Seminole County"), post("lake-and-polk-county-driveway-permits", "Lake and Polk counties"),
                                           post("sarasota-county-driveway-patio-permits", "Sarasota, Venice and North Port"), post("manatee-county-driveway-permits", "Bradenton, Lakewood Ranch, Parrish and Palmetto"),
                                           post("driveway-apron-and-right-of-way-florida", "Who owns the driveway apron"), post("florida-hoa-artificial-turf-law", "Florida HOA rules on artificial turf")])),
        sec("Who pulls the permit?", f"<p>On the projects we build, we apply for the permits the city or county requires and list them on the estimate. Florida's lien law adds one more document on projects over $2,500: the Notice of Commencement, recorded before work starts ({src('fs713-13', 'F.S. 713.13')}). If a contractor asks you to pull an owner-builder permit for work they are doing, ask why. {contact('Ask us about your address')}.</p>"),
    ])
    faqs = [faq("Can I replace my driveway with pavers without a permit?", "Rarely in our area. The apron in the right-of-way almost always needs a permit, and cities such as Orlando and Orange County require an engineering or zoning permit for pavers on the lot too. Manatee County exempts non-structural patios but not driveway connections to the road."),
            faq("Does the HB 803 exemption cover my new patio?", "It covers building permits for single-family work under $7,500, not zoning, engineering or right-of-way permits. A patio that needs a zoning permit for impervious coverage still needs it after July 1, 2026."),
            faq("What happens if work is done without a required permit?", "Cities can stop the work, require an after-the-fact permit and inspection, and charge more for it; Winter Garden, for example, charges triple for after-the-fact permits. It can also complicate a home sale if the buyer's inspector finds unpermitted work.")]
    return page("/permits/", "permit", "Driveway, Patio & Paver Permits in Central & SW Florida", "Do you need a permit for a driveway, patio, pavers or retaining wall? Rules for Orlando, Orange, Seminole, Lake, Sarasota and Manatee, checked October 2026.",
                "Permits and HOA approvals for concrete and pavers",
                capsule("As of October 2026, nearly every city and county in Greater Orlando and Sarasota–Manatee requires a right-of-way or engineering permit for a driveway apron, and many require a zoning permit for pavers. Florida's HB 803 exempts small single-family jobs under $7,500 from building permits only, not from zoning or right-of-way review."),
                body, faqs=faqs, crumb="Permits & HOA", form=False,
                sources=["orlando-hb803-guide", "orlando-engineering-permit", "orlando-esm", "orange-do-i-need-permit", "orange-residential-pavers", "kissimmee-driveway-sidewalk", "winterpark-58-65", "sanford-schedule-f", "sanford-fees",
                         "clermont-permit-types", "stcloud-pw-fees", "city-sarasota-engineering-row", "city-sarasota-zoning-vi-203-impervious", "sarasota-county-row-permit", "sarasota-county-22-63-retaining-walls",
                         "manatee-driveway-application", "manatee-no-permit-list", "bradenton-lur-4.1-access-sidewalks", "bradenton-lur-3.2-isr", "wintergarden-isr-worksheet", "wintergarden-faq", "fs720-3035", "fs720-3045", "fs713-13"])


def get_pages():
    return [cost_hub(), permits_hub()]
