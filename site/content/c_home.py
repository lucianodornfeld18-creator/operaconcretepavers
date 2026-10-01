# -*- coding: utf-8 -*-
"""Home page."""
from _data import SERVICES, SERVICE_ORDER, PRICES, UNITS
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, cs, post, compare, src, ext, price, per, price_note, contact, thumb
from _photos import for_service
from _posts import cost_for

H1 = "Concrete driveways, pavers and patios built for Florida ground"


def _cards(pillar):
    out = []
    for k in SERVICE_ORDER:
        S = SERVICES[k]
        if (S["pillar"] == pillar) or (pillar == "pavers" and S["pillar"] == "turf"):
            pid = (for_service(k, 1) or [None])[0]
            img = thumb(pid) if pid else ""
            cost = cost_for(k)
            cl = f' · <a href="{cost}">cost guide</a>' if cost else ""
            out.append(f'<li class="card">{img}<h3><a href="{S["route"]}">{S["name"]}</a></h3><p>{S["short"]}</p><p><small>Market range {price(S["price"])} per {per(S["price"])}{cl}</small></p></li>')
    return '<ul class="grid">' + "".join(out) + "</ul>"


def get_pages():
    rows = [[a(SERVICES[k]["route"], SERVICES[k]["name"]), f"{price(SERVICES[k]['price'])}", per(SERVICES[k]["price"]), f"{price(SERVICES[k]['price'], True)}"] for k in SERVICE_ORDER]
    body = "".join([
        sec("Concrete work we pour", "<p>Concrete is still the most common driveway surface in Florida subdivisions, and most of what goes wrong with it starts below the surface. "
            f"We pour new and replacement {svc('concrete-driveways', 'concrete driveways')}, back patios and lanai extensions, {svc('concrete-pool-decks', 'pool decks')}, "
            f"decorative {svc('stamped-concrete')}, front walks and right-of-way sidewalk sections, pads for sheds, RVs and AC units, and the {svc('concrete-repair', 'repair and resurfacing')} that keeps an older slab in service. "
            f"The {a('/concrete/', 'concrete services overview')} explains how we choose thickness, reinforcement and joint spacing for each.</p>" + _cards("concrete")),
        sec("Pavers, retaining walls and artificial turf", f"<p>Interlocking pavers flex where a slab cracks, and a single damaged unit can be lifted and reset. We lay {svc('paver-driveways', 'paver driveways')}, "
            f"patios and walkways, travertine and concrete-paver pool decks, segmental block walls, and {svc('artificial-turf', 'artificial turf')} for yards where sod keeps failing. "
            f"Old pavers that have sunk, stained or lost their joint sand usually need {svc('paver-sealing', 'cleaning, releveling and sealing')} rather than replacement. See the {a('/pavers/', 'paver services overview')} for base depths and materials.</p>" + _cards("pavers")),
        sec("Two crews: Greater Orlando and Sarasota–Manatee",
            "<p>We run the business as two service units so the people who quote a job are the people who know that county's permit desk and that soil. "
            "The Orlando unit covers Orange, Osceola, Seminole and Lake counties and Davenport on the Polk County side. The Sarasota unit covers Sarasota and Manatee counties, from Palmetto and Parrish down to Venice and Englewood.</p>"
            f'<div class="units"><div class="unit"><h3>{UNITS["orlando"]["name"]}</h3><p>Orlando, {city("kissimmee")}, {city("clermont")}, {city("oviedo")}, {city("winter-garden")}, {city("windermere")}, {city("st-cloud")}, {city("winter-park")} and nearby towns.</p><p><a href="/central-florida/">The Orlando unit</a></p></div>'
            f'<div class="unit"><h3>{UNITS["sarasota"]["name"]}</h3><p>{city("sarasota")}, {city("lakewood-ranch")}, {city("bradenton")}, {city("venice")}, {city("parrish")}, {city("north-port")} and the barrier islands.</p><p><a href="/sarasota-manatee/">The Sarasota unit</a></p></div></div>'),
        sec("What does concrete or paver work cost in Florida in 2026?",
            f"<p>As of October 2026, published Florida and national cost data put an installed concrete driveway at about {price('concrete-driveway')} per square foot, a paver driveway at {price('paver-driveway')}, a paver patio at {price('paver-patio')} and artificial turf at {price('artificial-turf')}. "
            f"Angi's Orlando data, updated May 2026, puts the average concrete driveway project near $6,490 ({src('angi-driveway-orlando', 'Angi, Orlando')}). Prices don't change by ZIP code; demolition, access, base work, permits and HOA requirements do.</p>"
            + table("Florida market ranges by service, October 2026", ["Service", "Market range", "Unit", "Typical middle"], rows, price_note())
            + f"<p>The {a('/cost/', 'cost guides')} break each of these down by size, finish and site conditions, with worked examples for a one-, two- and three-car driveway.</p>"),
        sec("Why Florida concrete cracks, and what we do about it",
            "<p>Central and Southwest Florida are hard on flatwork for three reasons, and none of them is the concrete itself.</p>"
            f"<h3>Water sits close to the surface</h3><p>Much of both regions is flatwoods soil: Myakka, the official state soil, plus Smyrna, Immokalee and EauGallie. USDA soil descriptions put the water table within roughly 0 to 18 inches of the surface for part of the year ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}). A subgrade that is soft in August and firm in April moves, so we compact it in lifts and grade the finished surface away from the house.</p>"
            f"<h3>Heat dries the top before the slab cures</h3><p>ACI guidance treats 95 °F concrete and an evaporation rate above 0.2 lb per square foot per hour as the danger zone for plastic shrinkage cracking ({src('aci-faq-maxtemp', 'ACI')}). On a July afternoon in Orlando, both are easy to hit. That's why our pours start early and the slab gets a curing compound or wet cure, not a hose rinse at lunch.</p>"
            f"<h3>Rain comes on a schedule</h3><p>Orlando averages 51.45 inches of rain a year and Sarasota–Bradenton about 49 inches, most of it in the late-May to mid-October wet season ({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}). A paver base left open before a 3 p.m. storm, or a pour that gets rained on before it sets, is a problem we plan around rather than fix later. The post on {post('pouring-concrete-in-florida-rainy-season', 'pouring in the rainy season')} goes into how.</p>"
            "<p>Control joints matter as much as any of that. NRMCA's rule of thumb is joints at 24 to 36 times the slab thickness, so a 4-inch driveway gets a joint every 8 to 12 feet, cut a quarter of the way through "
            f"({src('nrmca-cip6', 'NRMCA CIP 6')}). A crack that follows a joint is the slab doing its job; a crack that wanders across a panel usually traces back to the base, the timing of the cut or the cure.</p>"),
        sec("Concrete or pavers: which one should you choose?",
            f"<p>For most Florida driveways the decision comes down to budget, HOA rules and how you feel about cracks. Concrete costs less up front, typically {price('concrete-driveway', True)} per square foot against {price('paver-driveway', True)} for pavers, and it's one continuous surface that's easy to keep clean. "
            "Pavers cost more, but a sunken corner or a stained section can be lifted out and relaid, and nobody notices a repair. Some HOAs in newer master-planned communities specify pavers or a decorative finish on driveways; older neighborhoods often have plain concrete aprons that the city or county controls.</p>"
            + table("Concrete vs. pavers at a glance", ["Factor", "Poured concrete", "Interlocking pavers"],
                    [["Installed cost (Florida range)", f"{price('concrete-driveway')} / sq ft", f"{price('paver-driveway')} / sq ft"],
                     ["Cracking", "Expected at joints; random cracks point to base or curing problems", "Joints flex; units don't crack in normal use"],
                     ["Repair", "Patch shows; full panels replaced for a clean look", "Lift and relay the affected area"],
                     ["Ready to drive on", "Only after the slab has cured and gained strength", "Once compacted and joint-sanded"],
                     ["Upkeep", "Clean; optional sealer", "Joint sand top-ups; sealing on a schedule you choose"]],
                    "General comparison; the comparison page covers lifespan, resale and storm behavior.")
            + f"<p>The full side-by-side is on our {compare('pavers-vs-concrete-driveway', 'pavers vs. concrete driveway comparison')}, and pool decks get their own in {compare('pavers-vs-concrete-pool-deck', 'pavers vs. concrete for a pool deck')}.</p>"),
        sec("How a project runs with us",
            "<p>Every job follows the same order, whether it's a 200-square-foot walkway or a full driveway and pool-deck rebuild.</p>"
            + steps([("Site visit and measure.", "We look at the subgrade, the slope, the trees, where the water goes in a storm and what the HOA or city requires."),
                     ("Written scope and price.", "Thickness, reinforcement, joint plan, base depth, finish, demolition and haul-off, permit responsibility and the cleanup are written down."),
                     ("Approvals.", "HOA or ARC packet and any permit the city or county requires, including right-of-way permits for driveway aprons."),
                     ("Demolition and base.", "Old surface removed, roots and organic soil dug out, base placed and compacted in lifts."),
                     ("Pour or lay.", "Concrete placed, finished, jointed and cured; or pavers laid, cut, compacted and sanded; or turf seamed and infilled."),
                     ("Walkthrough.", "We go over curing, when to drive on it, and how to care for the surface.")])
            + f"<p>The {a('/process/', 'project process page')} explains each step, and the post on {post('prepare-your-yard-for-hardscape-installation', 'preparing your home for installation day')} covers sprinklers, pets, vehicles and gates.</p>"),
        sec("How do you choose the best concrete contractor near you?",
            "<p>Whether you search for the best concrete contractor near me or paver installers near me, the shortlist should be judged on paperwork and method, not on photos alone. Five checks catch most problems:</p>"
            + ul([f"Look the business up on the {src('dbpr-search', 'DBPR license search')} and ask which license, if any, covers the work. Florida law exempts driveway installation from licensing requirements but treats structural slabs and walls differently ({src('fs489-117', 'F.S. 489.117')}).",
                  f"Ask who pulls the permit. Cities like Orlando require an engineering permit for driveway and paver work even after the 2026 change that exempted small single-family building permits.",
                  f"On jobs over $2,500, expect the Notice of Commencement process under Florida's lien law ({src('fs713-13', 'F.S. 713.13')}).",
                  "Get the base depth, thickness, reinforcement and joint plan in writing. A price without them can't be compared.",
                  "Ask how the crew handles heat and rain on pour day."])
            + f"<p>Two guides go deeper: {post('how-to-choose-a-concrete-contractor-orlando', 'choosing a concrete contractor in Orlando')} and {post('how-to-compare-concrete-and-paver-quotes', 'comparing concrete and paver quotes line by line')}.</p>"),
        sec("Permits, HOAs and the driveway apron",
            "<p>The section of driveway between the sidewalk and the street usually sits in the public right-of-way, so the city or county sets its thickness and width even when the rest of the driveway is yours. "
            "Orlando, for example, specifies a 6-inch, 3,000 psi apron and sidewalk crossing. Master-planned communities add a second layer: architectural review committees that approve material, color and pattern before work starts. "
            f"Since 2026, Florida law bars an HOA from requiring a building permit before it reviews your application ({src('fs720-3035', 'F.S. 720.3035')}), so the two approvals can run side by side.</p>"
            f"<p>County-by-county guides: {post('orange-county-orlando-driveway-patio-permits', 'Orange County and Orlando')}, {post('osceola-county-kissimmee-st-cloud-permits', 'Osceola County')}, {post('seminole-county-driveway-patio-permits', 'Seminole County')}, "
            f"{post('lake-and-polk-county-driveway-permits', 'Lake and Polk')}, {post('sarasota-county-driveway-patio-permits', 'Sarasota County')} and {post('manatee-county-driveway-permits', 'Manatee County')}. HOA steps are in {post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for pavers or a new driveway')}.</p>"),
        sec("Artificial turf, built to the 2026 state standard",
            "<p>Florida's synthetic turf rule, Rule 62-308.100, took effect on May 19, 2026 for single-family lots of one acre or less. It requires natural infill on lawns, a washed crushed-rock or crushed-concrete base, no in-ground irrigation watering the turf, turf kept out of swales and stormwater ponds, a 10-foot setback from water bodies unless there's a seawall, and no turf inside a tree's drip line without a certified arborist's sign-off "
            f"({src('flrules62-308-100', 'Florida Administrative Code')}). We build to that standard on every lawn. An HOA can still regulate turf that's visible from the street ({src('fs720-3045', 'F.S. 720.3045')}).</p>"
            f"<p>Where turf meets hardscape, the two trades work best as one job: a paver border holds turf edges better than nails in sand. More in {svc('artificial-turf', 'our artificial turf service')} and {compare('artificial-turf-vs-sod', 'turf vs. sod in Florida')}.</p>"),
        sec("Pool decks: heat underfoot, drains and the coping",
            f"<p>A pool deck is the one slab people walk on barefoot in August, so surface choice matters more than color. Light-colored travertine and shell stone stay noticeably cooler than dark concrete pavers, and a spray-applied texture such as Kool Deck is the usual way to cool a poured concrete deck ({src('epa-cool-pavements', 'EPA, cool pavements')}). "
            f"Resurfacing an existing concrete deck runs about $3 to $12 per square foot in national data, while a new travertine deck sits near the top of the paver range ({src('homeguide-pool-deck-resurfacing', 'HomeGuide')}).</p>"
            "<p>Two details decide whether a deck lasts: slope and the joint at the coping. The deck has to shed water toward drains or the lawn, never toward the pool or the house, and the joint between deck and coping needs a flexible sealant so the two can move separately. "
            f"Compare the options in {compare('cool-deck-vs-pavers-vs-travertine', 'Cool Deck vs. pavers vs. travertine')}, or read {post('how-hot-do-pool-decks-get-florida', 'how hot pool decks get in Florida')} before you pick a material. Our {svc('pool-deck-pavers', 'pool deck pavers')} and {svc('concrete-pool-decks', 'concrete pool deck')} pages cover the build.</p>"),
        sec("Repair, resurface or replace?",
            "<p>Not every cracked driveway needs to come out. Hairline shrinkage cracks and cracks along control joints are cosmetic; a resurfacing overlay or a sealed crack is often enough. "
            f"Sections that have sunk, heaved over a root or broken into loose pieces usually need the panel cut out and repoured. National cost data puts resurfacing at about $3 to $7 per square foot against $6 to $15 for a new driveway ({src('homeguide-concrete-resurfacing', 'HomeGuide, resurfacing')}).</p>"
            + table("Common driveway problems and the usual fix", ["What you see", "Likely cause", "Usual fix"],
                    [["Hairline cracks across the surface", "Plastic shrinkage while curing", "Clean and seal; resurface if widespread"],
                     ["Crack along a sawcut joint", "The joint working as designed", "Nothing, or seal the joint"],
                     ["One panel lower than the next", "Soft or washed-out subgrade", "Lift the slab or cut out and repour"],
                     ["Raised, broken section near a tree", "Root growth under the slab", "Remove the section, root barrier, repour"],
                     ["Pavers sunk in the tire paths", "Thin or poorly compacted base", "Lift, rebuild the base, relay"]], "Field guide, not a diagnosis; a site visit settles it.")
            + f"<p>Our {svc('concrete-repair', 'concrete repair service')} covers crack repair, overlays and slab replacement. For a deeper look at crack types, read {post('concrete-driveway-cracks-florida', 'which driveway cracks are normal in Florida')}, and for the cost math see {compare('resurface-vs-replace-concrete', 'resurface or replace a concrete driveway')}.</p>"),
        sec("What our written estimate includes",
            "<p>A number on a business card can't be compared with anything. Our estimates list the items below so you can lay two bids side by side.</p>"
            + table("Line items on an Opera estimate", ["Item", "What it tells you"],
                    [["Area and layout", "Square footage, shape, and any steps, curves or borders"],
                     ["Demolition and disposal", "Whether the old surface is removed and hauled away"],
                     ["Base", "Material and compacted depth under concrete or pavers"],
                     ["Concrete spec", "Thickness, strength, reinforcement and joint spacing"],
                     ["Paver or turf spec", "Product type, thickness, pattern, edge restraint, joint sand or infill"],
                     ["Finish and sealer", "Broom, stamped, exposed aggregate, color; sealer if included"],
                     ["Permits and HOA", "Who applies, and what each approval covers"],
                     ["Cleanup and walkthrough", "Site cleanup and care instructions at handover"]])
            + f"<p>Ready to compare? {contact('Send us your project')} and we'll set up the site visit.</p>"),
        sec("Guides worth reading before you sign",
            "<p>A few of our articles answer the questions that come up on almost every site visit:</p>"
            + ul([post("why-pavers-sink-in-florida", "Why pavers sink in Florida, and how the fix works"),
                  post("should-you-seal-a-concrete-driveway-florida", "Whether a concrete driveway in Florida needs sealing"),
                  post("does-a-new-driveway-add-home-value", "Whether a new driveway, patio or pool deck adds home value"),
                  post("best-time-of-year-for-hardscape-projects-florida", "Which months suit pavers, concrete or turf work"),
                  post("florida-contractor-license-check-concrete-pavers", "How to check a concrete or paver contractor's license in Florida")])),
        sec("Where we work", "<p>These are the towns with their own local pages, grouped by county. If yours isn't listed, send the address with your request and we'll tell you which crew covers it.</p><!--AUTO:all-areas-->"),
    ])
    faqs = [
        faq("Do you work in both Orlando and Sarasota?", "Yes. Opera Concrete & Pavers runs two service units. The Orlando unit covers Orange, Osceola, Seminole and Lake counties plus northeast Polk; the Sarasota unit covers Sarasota and Manatee counties. Pick your area on the estimate form and the right crew gets the request."),
        faq("Are estimates free?", "Yes. We measure on site, look at drainage, trees, access and the existing surface, and then send a written scope and price. There is no charge for the visit or the estimate in either service area."),
        faq("Can one contractor handle concrete, pavers and turf on the same project?", "Yes, and it often saves a step. A typical backyard project pairs a paver patio or pool deck with turf, and the paver edge doubles as the turf border. Scheduling one crew avoids a second excavation and keeps the grading consistent."),
        faq("Do you remove the old driveway or patio?", "Yes. Demolition, haul-off and disposal are part of most replacement jobs and are listed as a separate line in the estimate. Removal typically adds $3 to $8 per square foot in national cost data, depending on thickness and reinforcement."),
        faq("Will my HOA need to approve the work?", "In most master-planned communities, yes: driveways, pavers, pool decks and visible turf usually need architectural review approval before work starts. We supply the material specs, colors and site sketch that the application asks for."),
        faq("What areas do you serve outside the main cities?", "The service-area pages list every town with its own page, from Montverde and Groveland to Myakka City and Anna Maria Island. If your town isn't listed, include the address on the form and we'll confirm coverage."),
    ]
    return [page("/", "home", "Concrete & Paver Contractor | Orlando & Sarasota, FL", "Concrete driveways, pavers, pool decks, stamped concrete and turf in Greater Orlando and Sarasota–Manatee. Free on-site estimates and 2026 Florida price ranges.",
                 H1,
                 capsule(f"Opera Concrete & Pavers pours concrete driveways, patios and pool decks and installs pavers, retaining walls and artificial turf in Greater Orlando and in Sarasota, Lakewood Ranch and Bradenton. As of October 2026, Florida market data puts installed concrete driveways at {price('concrete-driveway')} per sq ft and paver driveways at {price('paver-driveway')}; every price we give follows a site visit."),
                 body, faqs=faqs, faq_title="Questions homeowners ask first", wide=True, hero_photo="home-hero",
                 hero_extra='<ul class="ticks"><li>Concrete driveways &amp; patios</li><li>Pavers &amp; travertine</li><li>Pool decks</li><li>Artificial turf</li></ul>',
                 sources=["angi-driveway-orlando", "homeguide-driveway-pavers", "homeguide-paver-patio", "homeguide-artificial-grass", "nrcs-myakka-osd", "aci-faq-maxtemp", "ncei-annual-prcp", "nrmca-cip6", "dbpr-search", "fs489-117", "fs713-13", "fs720-3035", "flrules62-308-100", "fs720-3045"])]
