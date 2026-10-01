# -*- coding: utf-8 -*-
"""Cost guides: paver patio, paver sealing, retaining wall, artificial turf (module c_cost_c of COST_PAGES)."""
from _data import PRICE_DATE
from _helpers import page, capsule, sec, table, faq, ul, a, svc, city, post, compare, src, ext, price, per, offer
from _photos import for_service


def paver_patio_cost():
    K = "paver-patios"
    pk = "paver-patio"
    pids = for_service(K, 1)
    body = "".join([
        sec("How much does a paver patio cost in Florida?",
            f"<p>An installed paver patio or walkway in concrete pavers runs {price(pk)} per square foot in Florida and national market data as of {PRICE_DATE}, with most jobs landing nearer {price(pk, True)} "
            f"({src('homeguide-paver-patio', 'HomeGuide')}). Travertine runs well above that, from $13 to $45 per square foot depending on the cut and finish ({src('homeguide-travertine', 'HomeGuide, travertine')}). "
            "Those per-square-foot numbers are a planning figure, not a bid. What a specific patio costs depends on how much old concrete, sod or landscaping has to come out first, how far a wheelbarrow or skid steer has to travel to reach the work, and whether the layout is a plain rectangle or a shape with a lot of cut borders around a fire pit or pool cage post.</p>"),
        sec("How much does a 400 sq ft paver patio cost?",
            "<p>A 400 square foot patio in concrete pavers runs roughly $4,000 to $6,800 at current Florida market rates, in line with HomeGuide's own worked example for a 20 by 20 ft patio at $3,800 to $6,800. Smaller seating areas and larger full-backyard patios scale from there.</p>"
            + table("Paver patio totals by size, concrete pavers", ["Patio size", "Area", f"Market range at {price(pk)}/sq ft"],
                    [["Small seating area (10 × 10 ft)", "100 sq ft", "$1,000–$1,700"],
                     ["Standard patio (12 × 12 ft)", "144 sq ft", "$1,440–$2,450"],
                     ["Lanai extension (16 × 20 ft)", "320 sq ft", "$3,200–$5,440"],
                     ["Full backyard patio (20 × 20 ft)", "400 sq ft", "$4,000–$6,800"],
                     ["Large entertaining patio (24 × 25 ft)", "600 sq ft", "$6,000–$10,200"]],
                    f"Arithmetic on the published Florida range of {price(pk)} per square foot, {PRICE_DATE}; close to HomeGuide's own 12 × 12 ($1,400–$2,500) and 20 × 20 ($3,800–$6,800) examples ({src('homeguide-paver-patio', 'HomeGuide')}). None of these rows include a fire pit, seat wall or travertine upgrade.</p>")),
        sec("How much do pavers cost per square foot installed?",
            "<p>Installed pavers run $10 to $30 per square foot nationally across every material, with concrete pavers, the material most patios in both service areas use, narrower at $8 to $15 "
            f"({src('homeguide-pavers-sqft', 'HomeGuide, pavers per sq ft')}). The paver unit itself is a small share of that: material averages $2 to $4 per square foot, with labor, base and bedding sand making up the rest. A separate HomeGuide guide prices a dedicated paver walkway considerably higher, $15 to $40 per square foot, with a 200 square foot walkway running $3,000 to $8,000 "
            f"({src('homeguide-paver-walkway', 'HomeGuide, paver walkway')}). That spread between a walkway and an open patio isn't a typo in either guide; a narrow 3- or 4-foot-wide walk needs the same base, edge restraint and compaction equipment as a wide patio but spreads that fixed cost over far less square footage, and a walkway usually has more linear feet of cut border per square foot than an open field does. A front walkway tied into a larger patio, rather than priced as its own standalone job, usually lands closer to the patio rate than the walkway-only figure above.</p>"),
        sec("Paver patio cost by material",
            "<p>Concrete pavers and travertine solve the same layout problem at very different price points, and the gap between them is almost entirely the material cost, not the labor to set it in place.</p>"
            + table("Paver patio material cost, a 250 sq ft seating area", ["Material", "Range per sq ft", "Installed total"],
                    [["Concrete pavers", price(pk), "$2,500–$4,250"],
                     ["Travertine", "$13–$45", "$3,250–$11,250"]],
                    f"{src('homeguide-paver-patio', 'HomeGuide, paver patios')}; {src('homeguide-travertine', 'HomeGuide, travertine')}. Clay brick and porcelain sit between the two in published Florida pricing, though patio-specific data for either material is thinner than for concrete or travertine.")),
        sec("Is paver patio pricing different in Orlando and Sarasota–Manatee?",
            "<p>No Florida-specific cost guide breaks out paver patio pricing by metro the way Angi does for concrete driveways; every patio figure in current published data, from HomeGuide's per-square-foot ranges to its sized examples, is national rather than tied to Orlando or Tampa. A Lakewood Ranch patio and a Kissimmee patio start from the same per-square-foot range. What actually separates the two bids is the soil under each lot, whichever jurisdiction's permit desk reviews the plan, and how much of the old yard needs to come out, not which service area the address sits in.</p>"),
        sec("What moves a paver patio quote up or down",
            "<p>A flat per-square-foot number hides the line items that decide where a specific bid lands inside that range.</p>"
            + table("Paver patio cost drivers", ["Factor", "What it does to the price", "Florida detail"],
                    [["Removing an old slab or patio", "Adds to the job before the new base goes in", f"Concrete removal runs $3–$8/sq ft nationally including disposal ({src('homeguide-concrete-removal', 'HomeGuide')})"],
                     ["Base depth", "A standard 4 in. base over well-drained soil costs less than 6–8 in. over wet flatwoods ground", "Set by soil condition, not by square footage alone"],
                     ["Access", "A patio reached only through a gated side yard or under a screen enclosure track takes longer to build", "Common on Florida lots with a pool cage or a fenced backyard"],
                     ["Permits", "A zoning or engineering review adds a line item", f"Orange County charges about $38 for the permit plus $38 for engineering review on a paver patio ({src('orange-residential-pavers', 'Orange County')})"],
                     ["Fire pit or seat wall", "A denser base detail and extra edge restraint under the add-on", "Priced separately from the open paver field"]],
                    "Ranges drawn from the Florida and national sources cited on this page; not every factor applies to every lot.")),
        sec("Two paver patio budgets, worked through",
            f"<p>Say you have a cracked 300 square foot concrete slab behind a 1980s ranch in {city('winter-garden')} that you want to pull out and replace with a concrete-paver patio. Removal runs roughly $900 to $2,400, and the new paver field at {price(pk)} per square foot runs $3,000 to $5,100, putting the full job in the neighborhood of $3,900 to $7,500 before a fire pit or seat wall, with the final number landing lower for a plain rectangular layout and higher for one with a lot of cut borders around an existing pool cage post.</p>"
            f"<p>Say instead you have a bare, newly sodded backyard on a 2010s lot in {city('lakewood-ranch')} and want a 250 square foot travertine patio off the lanai, with no demolition involved. At $13 to $45 per square foot, that runs roughly $3,250 to $11,250 for the paver field alone, a wide spread that mostly tracks the specific travertine cut and pattern chosen rather than the base work underneath it, which follows the same compaction spec regardless of material.</p>"),
        sec("Cutting the price without cutting the base",
            "<p>The compacted base under a paver patio is the one place a bid shouldn't get thinner just to hit a number; a shallow or under-compacted base is what shows up as a sunken joint or a rocking unit within a season or two. There are still real ways to bring a patio quote down:</p>"
            + ul(["Choose concrete pavers over travertine or porcelain. The material, not the base work, is most of the gap between them.",
                  "Keep the footprint a simple rectangle. A curved edge or a layout cut around several existing trees or a pool cage adds labor time a straight run doesn't need.",
                  "Pour or lay a patio and a connecting walkway in the same mobilization rather than as two separate visits, splitting one crew day and one set of base equipment across both.",
                  "Ask whether an existing concrete slab is sound enough to serve as part of the compacted sub-base for pavers set on top, where grade allows, instead of a full tear-out.",
                  "Schedule outside the rainy season's busiest stretch, when a crew juggling fewer storm delays often has more room to work with on timing."])),
        sec("What a paver patio quote should spell out",
            "<p>A square-foot number alone doesn't say much. Ask every bidder for the same list so the totals describe the same job:</p>"
            + ul(["Compacted base depth, written down, not just that a base exists",
                  "Paver thickness and the specific material, brand or color, not just 'pavers'",
                  "Edge restraint as its own line item; it's invisible once the job is finished and easy to leave off a cheap bid",
                  "Whether removal and haul-off of an existing slab, sod or landscaping is included or billed separately",
                  f"Who applies for any required permit, and whether the fee is in the price; a contract over $2,500 also triggers Florida's Notice of Commencement paperwork, recorded with the county clerk before anyone breaks ground ({src('fs713-13', 'F.S. 713.13')})"])),
        sec("Related reading",
            f"<p>For the full build spec, see {svc('paver-patios', 'our paver patios and walkways page')}, which covers base depth, drainage slope and the step-by-step install. If concrete is still on the table, {compare('stamped-concrete-vs-pavers', 'our stamped concrete vs. pavers comparison')} and {compare('travertine-vs-concrete-pavers', 'travertine vs. concrete pavers')} go through the trade-offs. "
              f"{post('paver-patio-ideas-florida', 'Paver patio ideas for Florida backyards')} and {post('extend-patio-under-screen-enclosure', 'extending a patio under a screen enclosure')} are worth a look before the first bid, and {post('how-to-compare-concrete-and-paver-quotes', 'how to compare quotes line by line')} covers what to ask for in writing. The {a('/cost/', 'cost guide hub')} rounds up current pricing for every other service we quote.</p>"),
    ])
    faqs = [
        faq("How much does a 400 sq ft paver patio cost?",
            f"At current Florida market rates of {price(pk)} per square foot, a 400 square foot patio in concrete pavers runs roughly $4,000 to $6,800, close to HomeGuide's own worked example of $3,800 to $6,800 for a 20 by 20 ft patio. A travertine patio the same size costs considerably more; the material, not the base work, drives that gap."),
        faq("How much do pavers cost per square foot installed?",
            "Nationally, installed pavers of any material run $10 to $30 per square foot, with concrete pavers, the most common patio material in both service areas, narrower at $8 to $15. A separate guide prices paver walkways higher, $15 to $40 per square foot, because a narrow walk carries the same fixed base and edge-restraint cost as a wide patio over far less area."),
        faq("Are paver walkways priced the same as paver patios per square foot?",
            "Not usually. A connecting walkway 3 to 4 feet wide needs the same compacted base, bedding sand and edge restraint as an open patio, but spreads that cost over much less square footage, which is why dedicated walkway pricing runs well above open-patio pricing per square foot. A walkway built as part of a larger patio project, rather than priced on its own, typically comes in closer to the patio rate."),
        faq("Is travertine much more expensive than concrete pavers for a patio?",
            "Yes, usually two to three times the material cost. Concrete pavers run about $10 to $17 per square foot installed; travertine runs $13 to $45 depending on the cut, pattern and finish. The base, bedding sand and edge restraint underneath cost about the same regardless of which material goes on top."),
        faq("Does a paver patio quote usually include the base and edge restraint?",
            "It should, but not every bid itemizes them the same way. A complete price covers excavation, compacted aggregate base, bedding sand, edge restraint and joint sand along with the pavers themselves. If a quote lists only a per-square-foot paver price with no base depth stated, ask; the base is where a cheap bid usually cuts a corner that doesn't show up until a season or two later."),
        faq("Why do two paver patio quotes for the same size come back so different?",
            "They're often describing different scopes. One bid may include demolition of an existing slab, a 6-inch base on soft ground, edge restraint and permit fees; another may assume a bare, well-drained lot and skip one or more of those lines. Comparing the line items, not just the bottom-line total, is the only reliable way to tell whether two numbers describe the same job."),
        faq("Does adding a fire pit or seat wall raise the per-square-foot price?",
            "It raises the total more than it raises the rate on the open paver field around it. A fire pit needs a denser base detail under the ring itself and its own edge restraint, and a seat wall adds a short run of block and footing, both priced as separate line items rather than folded into the patio's per-square-foot number.")]
    return page("/paver-patio-cost/", "price", "Paver Patio Cost in Florida (2026)",
                f"Florida paver patio cost as of {PRICE_DATE}: {price(pk)} per sq ft installed in concrete pavers, size tables, travertine pricing, and what moves a patio quote.",
                "What a Paver Patio or Walkway Costs in Florida",
                capsule(f"As of {PRICE_DATE}, a paver patio or walkway in Florida runs {price(pk)} per square foot installed in concrete pavers, more in travertine. A 400 square foot patio lands near $4,000 to $6,800 before a fire pit, lighting or a seat wall. We quote paver patios, walkways and lanai extensions by scope across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["homeguide-paver-patio", "homeguide-travertine", "homeguide-pavers-sqft", "homeguide-paver-walkway", "homeguide-concrete-removal",
                         "orange-residential-pavers", "fs713-13"],
                crumbs=[("Cost guides", "/cost/")], crumb="Paver patio cost", service=K, form=True,
                hero_photo=pids[0] if pids else None, offer=offer(pk), eyebrow="Cost guide")


def paver_sealing_cost():
    K = "paver-sealing"
    pk = "paver-sealing"
    pids = for_service(K, 1)
    body = "".join([
        sec("How much does it cost to seal pavers?",
            f"<p>Cleaning, re-sanding and sealing an existing paver surface in Florida runs {price(pk)} per square foot as of {PRICE_DATE}, with most jobs landing nearer {price(pk, True)}, including pressure washing and re-sanding as part of the visit "
            f"({src('homeguide-seal-pavers', 'HomeGuide')}). A Central Florida contractor's own 2026 pricing lines up closely: $1.50 to $3.00 per square foot, with most homeowners paying $750 to $2,500 for a 500 to 1,000 square foot surface "
            f"({src('castle-paver-sealing-cfl', 'Castle Clean & Seal, Central Florida')}). Pressure washing alone, without re-sanding or a sealer coat, costs far less, $0.35 to $0.80 per square foot ({src('homeguide-seal-pavers', 'HomeGuide')}). What a specific job costs depends on how much joint sand has washed out, whether any pavers have sunk and need releveling first, and which sealer finish is specified.</p>"),
        sec("Is sealing pavers worth the money?",
            "<p>For most driveways, patios and pool decks, yes, measured against what it costs to let the surface go instead. The paver industry's own construction standard treats sealing as optional, not a requirement for the pavers to perform structurally, but it locks compacted joint sand in place and slows staining and UV fading. "
            f"Skipping it doesn't cost nothing; a joint that loses its sand is what lets a paver rock loose and eventually sink, and fixing that runs far more than a sealing visit would have. Paver releveling and repair, priced by scope rather than a flat sealing rate, costs $7 to $30 per square foot nationally, and replacing a few individual sunken stones runs $8 to $20 per square foot "
            f"({src('angi-patio-repair', 'Angi')}). Against a $1.50 to $3.25 per square foot sealing visit every few years, catching a joint before it fails is the cheaper path more often than not.</p>"),
        sec("Paver sealing cost by scope",
            "<p>\"Sealing\" covers a few different jobs depending on what the surface actually needs.</p>"
            + table("Paver cleaning and sealing, by scope", ["Scope", "Range per sq ft", "Note"],
                    [["Pressure washing only", "$0.35–$0.80", "No re-sanding or sealer coat"],
                     ["Clean, re-sand and seal (standard visit)", price(pk), "Our combined-service range"],
                     ["Releveling a sunken or rocking section", "$6–$12 for large areas; $8–$20 per stone", "Priced on top of the cleaning and sealing visit, not instead of it"]],
                    f"{src('homeguide-seal-pavers', 'HomeGuide, sealing and pressure washing')}; releveling figures from {src('homeguide-driveway-repair', 'HomeGuide, driveway repair')} and {src('angi-patio-repair', 'Angi')}.")),
        sec("Paver sealing cost by surface size",
            f"<p>Central Florida pricing scales roughly in proportion to area, with driveways, pool decks and patios each carrying a slightly different rate depending on exposure and access ({src('castle-paver-sealing-cfl', 'Castle Clean & Seal')}).</p>"
            + table("Paver sealing cost by surface, Central Florida contractor data", ["Surface", "Typical range per sq ft", "Example total"],
                    [["Driveway", "$1.50–$2.50", "$900–$3,000 for 600 sq ft"],
                     ["Pool deck", "$1.75–$3.00", "$1,400–$2,400 for 800 sq ft"],
                     ["Patio", "$1.50–$2.95 (sized job)", "$450–$2,000"]],
                    f"{src('castle-paver-sealing-cfl', 'Castle Clean & Seal, Central Florida, 2026')}.")),
        sec("Does sealing cost differ around Orlando and Sarasota–Manatee?",
            "<p>The Central Florida contractor pricing above is the only Florida-specific regional data found for paver sealing, and it covers the counties in our Orlando unit. A South Florida contractor quotes a noticeably lower starting rate, $0.75 to $1.50 per square foot, but that figure comes from a market well outside our Sarasota–Manatee service area and shouldn't be read as a Suncoast price "
            f"({src('craftpavers-fl-pricing', 'Craft Pavers')}). No published cost guide breaks out sealing pricing for Sarasota or Manatee specifically. We quote cleaning, re-sanding and sealing the same way on both coasts, priced by the surface's condition and size rather than by which county it's in.</p>"),
        sec("What moves a sealing quote up or down",
            "<p>A per-square-foot range hides the details that separate a quick visit from a longer one.</p>"
            + table("Paver sealing cost drivers", ["Factor", "Why it matters", "Typical effect"],
                     [["Algae, moss or heavy staining", "More passes with the pressure washer before sand or sealer go down", "Pushes a job toward the top of the range"],
                      ["Sand type", "Polymeric sand costs more material than dry sand", "Higher upfront cost, fewer repeat visits for washout"],
                      ["Surface type", "Pool decks see chlorine, splash and sun exposure patios don't", "Pool decks run $1.75–$3.00/sq ft against $1.50–$2.50 for driveways in Central FL data"],
                      ["Releveling", "A sunken or rocking paver needs the base rebuilt before anything else happens", "Adds $6–$20 per sq ft or per stone on top of the base sealing price"],
                      ["Minimum job fee", "Small areas don't scale down proportionally", f"A South Florida contractor sets a $1,000 minimum regardless of square footage ({src('craftpavers-fl-pricing', 'Craft Pavers')})"]],
                     "Ranges drawn from the Florida sources cited on this page.")),
        sec("Two sealing budgets, worked through",
            f"<p>Say you have a 600 square foot paver driveway and walkway in a 2000s subdivision near {city('kissimmee')} that hasn't been resealed in about five years and has a few joints losing sand near the garage apron. At the Central Florida driveway rate, that runs roughly $900 to $1,500 for cleaning, re-sanding and sealing, with no releveling needed if the apron is still flat.</p>"
            f"<p>Say instead you have an 800 square foot pool deck in a 1990s community near {city('bradenton')} with chlorine staining and two or three pavers that have sunk slightly near the skimmer. The sealing itself runs roughly $1,400 to $2,400 at the pool-deck rate, plus a separate releveling charge for the sunken units, likely $50 to $150 for a small handful of individual stones rather than a full-field rebuild. In both cases, a quote that itemizes the releveling separately from the clean-and-seal price is easier to compare against a competing bid than one lump total.</p>"),
        sec("Getting more sealing life for the money",
            "<p>The surface itself, not a calendar date, should set when the next visit happens, but there are ways to keep each visit's cost down:</p>"
            + ul(["Bundle a driveway, patio and walkway into one visit rather than scheduling them separately; one mobilization and one minimum fee cover all three.",
                  "Schedule for a dry stretch rather than racing a forecast; sealing a surface that's still damp underneath often means redoing the work.",
                  "Keep up light routine sweeping and the occasional rinse between visits, since windblown grit and standing algae are what push a job toward the top of the condition-based range.",
                  "Flag a sunken or rocking paver as soon as it's noticed rather than waiting; a small, early releveling costs a fraction of rebuilding a larger failed section later.",
                  "Ask whether dry sand, which costs less upfront, is enough for a shaded, low-traffic area where polymeric sand's washout resistance matters less."])),
        sec("What a paver sealing quote should spell out",
            "<p>A per-square-foot number by itself doesn't say whether a quote covers cleaning alone or the full clean, re-sand and seal visit. Ask every bidder for the same specifics so two quotes describe the same job:</p>"
            + ul(["The order of operations in writing: releveling first if needed, then cleaning, then sand, then sealer, never sealer applied before the surface is fully dry",
                  "Sand type named specifically, dry or polymeric, not a generic line item that just says 're-sand'",
                  "Sealer finish, wet-look or natural, with a sample on a small test area before the whole surface is committed",
                  "Square footage measured on site, not estimated from a driveway's listed width alone",
                  "Whether a minimum job fee applies, and what square footage it covers"])),
        sec("Related reading",
            f"<p>For the full service scope, see {svc('paver-sealing', 'our paver sealing and restoration page')}, which covers the order of steps and why releveling comes first. {compare('polymeric-sand-vs-joint-sand', 'Polymeric sand vs. regular joint sand')} and {compare('wet-look-vs-natural-paver-sealer', 'wet-look vs. natural-finish sealer')} go through the material choices. "
              f"{post('why-pavers-sink-in-florida', 'Why pavers sink in Florida')} and {post('mold-and-algae-on-pavers-florida', 'stopping mold and algae on pavers')} cover the causes behind the two most common calls, and {post('ants-and-weeds-in-paver-joints', 'ants and weeds between pavers')} rounds out the maintenance picture. The {a('/cost/', 'cost guide hub')} has current pricing for every other service we offer.</p>"),
    ])
    faqs = [
        faq("How much does it cost to seal pavers?",
            f"Cleaning, re-sanding and sealing an existing paver surface in Florida runs {price(pk)} per square foot, with most jobs landing nearer {price(pk, True)}. Central Florida contractor pricing for 2026 lines up closely, with most homeowners paying $750 to $2,500 for a 500 to 1,000 square foot surface."),
        faq("Is sealing pavers worth the money?",
            "Usually, measured against the cost of letting a loose joint turn into a sunken paver. Sealing itself is optional under the paver industry's own spec, but it locks joint sand in place and slows staining and fading. Paver releveling and repair run $7 to $30 per square foot once a surface has actually failed, well above the $1.50 to $3.25 per square foot a routine sealing visit costs."),
        faq("Does pressure washing alone cost less than a full clean-and-seal?",
            "Yes, considerably. Pressure washing by itself, with no re-sanding or sealer coat, runs $0.35 to $0.80 per square foot nationally, against $1.50 to $3.25 for the combined service. Washing alone strips algae and grime but does nothing for joint sand that's already washed out or a sealer coat that's worn through."),
        faq("How much more does releveling sunken pavers add to a sealing visit?",
            "Releveling a larger sunken area runs roughly $6 to $12 per square foot, and swapping individual stones runs $8 to $20 per unit, added on top of the base cleaning and sealing price rather than replacing it. A small handful of sunken pavers near a drain or a pool skimmer typically costs far less to fix than letting the problem spread across a wider section."),
        faq("Is there a minimum job fee for paver sealing in Florida?",
            "Often, yes. A South Florida contractor publishes a $1,000 minimum regardless of square footage, and Central Florida pricing shows the same pattern, with small jobs under 500 square feet running toward the higher end of the per-square-foot range. Bundling a driveway, patio and walkway into one visit spreads a minimum fee across more square footage."),
        faq("Does a pool deck cost more to seal than a driveway?",
            "Slightly, yes, in published Central Florida pricing: roughly $1.75 to $3.00 per square foot for a pool deck against $1.50 to $2.50 for a driveway. Chlorine, splash and more frequent water contact wear a sealer coat faster near the water, which is the main reason the rate runs a little higher there."),
        faq("Why do two Florida paver sealing quotes for the same job differ so much?",
            "They often describe different scopes. One bid may include releveling a few sunken pavers, polymeric sand and a wet-look sealer; another may quote a basic clean-and-seal with dry sand and skip any sunken units entirely. Asking each bidder to list sand type, sealer type and whether releveling is included is the only reliable way to compare totals.")]
    return page("/paver-sealing-cost/", "price", "Paver Sealing Cost in Florida (2026)",
                f"Florida paver sealing cost as of {PRICE_DATE}: {price(pk)} per sq ft for cleaning, re-sanding and sealing, plus Central Florida pricing and releveling costs.",
                "What It Costs to Clean, Re-Sand and Seal Pavers in Florida",
                capsule(f"As of {PRICE_DATE}, cleaning, re-sanding and sealing an existing paver surface in Florida runs {price(pk)} per square foot, with most jobs landing nearer {price(pk, True)}. An 800 square foot driveway or patio falls between about $1,200 and $2,600 before any releveling. We quote the combined service by scope across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["homeguide-seal-pavers", "castle-paver-sealing-cfl", "angi-patio-repair", "homeguide-driveway-repair", "craftpavers-fl-pricing"],
                crumbs=[("Cost guides", "/cost/")], crumb="Paver sealing cost", service=K, form=True,
                hero_photo=pids[0] if pids else None, offer=offer(pk), eyebrow="Cost guide")


def retaining_wall_cost():
    K = "retaining-walls"
    pk = "retaining-wall"
    pids = for_service(K, 1)
    body = "".join([
        sec("How much does a retaining wall cost per linear foot?",
            f"<p>A segmental block retaining wall runs {price(pk)} per square foot of wall face in Florida and national market data as of {PRICE_DATE}, with most jobs landing nearer {price(pk, True)} "
            f"({src('homeguide-retaining-wall', 'HomeGuide')}). Priced by length instead, a 10 linear foot section 2 feet tall runs about $700 to $1,300 installed, or roughly $70 to $130 per linear foot; the same 10 feet at 4 feet tall runs about $1,400 to $2,600, or $140 to $260 per linear foot "
            f"({src('homeguide-retaining-wall', 'HomeGuide')}). Height, not length, is what pushes the per-foot number up: every extra foot adds a buried course below grade, more fill behind the face to hold back, and, once a local height trigger is crossed, a stamped engineering set on top of the build. Most jobs also carry a project minimum of $1,500 to $3,000, so a short run still costs more per foot than a longer one on the same lot.</p>"),
        sec("Retaining wall cost by height",
            "<p>Published Florida and national data gives two solid reference points; the jump between them shows how much height alone changes the number.</p>"
            + table("Retaining wall cost, 10 linear ft section, installed", ["Height", "Total, 10 linear ft", "Per linear ft"],
                    [["2 ft", "$700–$1,300", "$70–$130"],
                     ["4 ft", "$1,400–$2,600", "$140–$260"]],
                    f"{src('homeguide-retaining-wall', 'HomeGuide')}. A wall taller than 4 ft climbs faster still once engineering is required; engineering review alone adds $500 to $2,000 or more on top of the build ({src('homeguide-retaining-wall', 'HomeGuide')}).")),
        sec("Retaining wall cost by type and material",
            "<p>Two separate choices stack on top of each other here: how the wall is built, and what it's faced with. A homeowner picking between a dry-stacked block system and a poured concrete wall is really comparing both at once, which is part of why published ranges for the two overlap as much as they diverge.</p>"
            + table("Retaining wall pricing by build method, per sq ft of wall face", ["Build method", "Range"],
                    [["Segmental (dry-stacked interlocking block)", "$15–$35"],
                     ["Gravity (weight alone holds the slope)", "$20–$50"],
                     ["Cantilevered (poured footing and stem)", "$40–$80"]],
                    f"{src('homeguide-retaining-wall', 'HomeGuide')}. Segmental systems cover most of the residential work we quote in both counties; cantilevered construction is reserved for taller or engineered walls.")
            + table("Retaining wall facing material, per sq ft", ["Facing material", "Range"],
                    [["Concrete block", "$15–$40"],
                     ["Poured concrete", "$20–$45"],
                     ["Brick", "$30–$60"]],
                    f"{src('homeguide-retaining-wall', 'HomeGuide')}; brick runs the highest material cost of the three. A different HomeGuide page prices poured concrete walls by linear foot instead, $45 to $270, a figure that probably bundles in taller or more heavily engineered projects than the per-square-foot numbers above assume ({src('homeguide-sidewalk', 'HomeGuide, concrete sidewalk')}).")),
        sec("How much does engineering add to the price?",
            "<p>Once a wall crosses the height a given jurisdiction treats as structural, engineered drawings become part of the cost, not an optional upgrade. That threshold isn't one statewide number; unincorporated Orange County applies Florida's residential code figures of 24 inches or 48 inches of unsupported fill, Clermont's line is 3 feet, and Sarasota County requires engineering above 4 feet "
            f"({src('orange-res-plan-guide', 'Orange County')}; {src('clermont-permit-types', 'City of Clermont')}; {src('sarasota-county-22-63-retaining-walls', 'Sarasota County')}). The permit itself can carry its own fee regardless of height; the City of Palmetto charges $10 plus $0.10 per linear foot for any retaining wall, engineered or not "
            f"({src('palmetto-code-10-46-retaining-wall-permit', 'City of Palmetto')}). {svc('retaining-walls', 'Our retaining walls page')} has the full jurisdiction-by-jurisdiction table; the short version for budgeting is that a wall sitting just under a local threshold can cost noticeably less than the same wall built a foot taller.</p>"),
        sec("Seat walls cost less than a full retaining wall",
            "<p>A seat wall is priced in roughly the same per-square-foot range as a retaining wall's facing material, since it uses the same block, but the total almost always comes in lower. A seat wall skips the engineered gravel backfill, perforated drain pipe and buried base course a true retaining wall needs to resist soil pressure, and it's typically built to an 18- to 24-inch sitting height rather than the 3- to 6-foot range a slope-holding wall often needs, so there's simply less wall to build and less behind it to drain.</p>"),
        sec("What else moves a retaining wall quote",
            "<p>Beyond height and type, a few Florida-specific factors show up in most bids.</p>"
            + table("Retaining wall cost drivers", ["Factor", "Why it matters", "Florida detail"],
                    [["Removing an old or failing wall", "Demolition and haul-off before the new wall starts", "No wall-specific Florida figure is published; general concrete removal runs $3–$8/sq ft including disposal"],
                     ["Drainage", "Gravel backfill and a perforated pipe are part of a working wall, not an upgrade", "Flatwoods soils common to both service areas hold a seasonal high water table within about 18 in. of the surface for part of most years"],
                     ["Access", "A wall built against a tight side yard or a steep slope limits equipment", "Common on the hillier lots in Clermont and Minneola and on narrow coastal lots in Sarasota–Manatee"],
                     ["Permit fees", "Required almost everywhere a wall is built, independent of height", f"Palmetto: $10 plus $0.10 per linear ft; other jurisdictions set their own fee schedule ({src('palmetto-code-10-46-retaining-wall-permit', 'City of Palmetto')})"]],
                    "Ranges drawn from the Florida and national sources cited on this page.")),
        sec("Two retaining wall budgets, worked through",
            f"<p>Say you have a 30 linear foot grade change between the house pad and the backyard on a sloped lot near {city('clermont')}, with about 3 feet of elevation to hold back. At the 4-foot reference pricing above, a wall that size runs roughly $4,200 to $7,800 installed, plus whatever the local engineering review adds if the final design comes in at or above the city's 3-foot threshold.</p>"
            f"<p>Say instead you have a 20 linear foot seat wall planned around a new paver patio and fire pit on a flat lot near {city('lakewood-ranch')}, built to an 18-inch sitting height with no slope behind it to hold back. Without the engineered drainage column or deep base a true retaining wall needs, that runs well under the 4-foot reference pricing, closer to the lower segmental-block range applied to a shorter, lighter structure.</p>"),
        sec("Reducing the cost without skipping drainage",
            "<p>Drainage behind the wall is the one line item that shouldn't come out of a bid to save money; a wall with nowhere for water to go is a wall that bulges or leans within a few rainy seasons. There are still real ways to bring the price down:</p>"
            + ul(["Where the grade allows it, terrace a tall slope into two shorter walls with a planted step between them instead of one tall engineered wall; each short wall can land under a jurisdiction's engineering threshold on its own.",
                  "Choose segmental block over a cantilevered design where the height and soil allow it; cantilevered construction costs more per square foot across every published range.",
                  "Keep the wall's run straight rather than curved; corners and curves add cutting and fitting time a straight line doesn't need.",
                  "Bundle a wall into the same mobilization as a patio or driveway project on the same lot, sharing one crew visit and one set of excavation equipment.",
                  "Get the drainage detail in writing rather than assuming it's included; a quote that's missing it isn't actually cheaper, it's incomplete."])),
        sec("What a retaining wall quote should spell out",
            "<p>Ask every bidder for the same specifics so the numbers describe the same wall:</p>"
            + ul(["Height measured from the lowest finished grade to the top of the wall, not an approximate figure",
                  "Drainage detail: aggregate type, pipe size and where the outlet daylights",
                  "Whether engineered drawings are required for this specific height and jurisdiction, and whether that cost is included or billed separately",
                  "Linear footage and square footage of wall face both stated, since quotes price by either basis",
                  f"Who applies for the permit, and whether the fee shown is in the total; past $2,500, Florida's lien statute calls for a Notice of Commencement filed with the county before anyone breaks ground ({src('fs713-13', 'F.S. 713.13')})"])),
        sec("Related reading",
            f"<p>For the full build spec and the complete jurisdiction-by-jurisdiction engineering table, see {svc('retaining-walls', 'our retaining walls page')}. If the project is still at the idea stage, {post('retaining-wall-ideas-florida-yards', 'our roundup of wall and seat-wall designs')} is worth a look, and {post('how-to-budget-a-backyard-hardscape-project-in-phases', 'this guide to phasing a bigger yard project')} covers sequencing a wall alongside a patio or driveway. The {a('/cost/', 'cost guide hub')} covers current pricing for the rest of what we build.</p>"),
    ])
    faqs = [
        faq("How much does a retaining wall cost per linear foot?",
            "A 10 linear foot section 2 feet tall runs about $70 to $130 per linear foot installed; the same length at 4 feet tall runs about $140 to $260 per linear foot. Most jobs also carry a $1,500 to $3,000 project minimum, so a short run costs more per foot than a longer one built on the same lot."),
        faq("Does a taller wall cost more per square foot, or just more overall?",
            "Both. Each added foot of height needs a deeper buried course and a wider band of backfill, so the rate per square foot of wall face climbs along with the total, and crossing a jurisdiction's engineering trigger adds a flat design fee on top of that. A 4-foot wall runs roughly double the per-linear-foot price of a 2-foot wall of the same length."),
        faq("How much does engineering add to a retaining wall quote?",
            "Published data puts engineering review for a taller wall at $500 to $2,000 or more, on top of the build itself. The height that triggers it varies by jurisdiction: Orange County applies Florida's residential code figures of 24 or 48 inches depending on the load, Clermont's threshold is 3 feet, and Sarasota County's is 4 feet."),
        faq("Is a seat wall cheaper than a full retaining wall?",
            "Yes, usually by a wide margin. A seat wall uses the same block pricing per square foot but skips the engineered gravel backfill and drain pipe a true retaining wall needs, and it's typically built to an 18- to 24-inch sitting height rather than several feet of slope-holding height, so there's less wall and less behind it to build."),
        faq("Do retaining wall quotes usually price by linear foot or square foot of wall face?",
            "Both appear in published data, and bidders don't always use the same basis. A linear-foot price only makes sense alongside a stated height, since a 10-foot run at 2 feet tall and the same run at 4 feet tall are very different jobs. Asking for both the linear footage and the square footage of wall face keeps two quotes comparable."),
        faq("Does drainage cost extra, or is it included in the per-square-foot price?",
            "Published per-square-foot ranges for retaining walls generally assume a properly drained wall, since gravel backfill and a perforated pipe are standard construction, not an add-on. A quote that's unusually low for its height and length is worth asking about directly; skipping drainage to hit a number is a common way a cheap bid gets there."),
        faq("Why do retaining wall quotes for the same length vary so much?",
            "Height, soil and access usually explain more of the gap than the contractor's margin does. A 20-foot wall on a gentle, well-drained slope with easy equipment access prices very differently from the same 20 feet on steep, wet ground reached only through a narrow side yard. Confirming height, drainage detail and access assumptions is the fastest way to see why two numbers differ.")]
    return page("/retaining-wall-cost/", "price", "Retaining Wall Cost in Florida (2026)",
                f"Florida retaining wall cost as of {PRICE_DATE}: {price(pk)} per sq ft of wall face, pricing by height and linear foot, and when engineering adds to the bill.",
                "What a Retaining Wall Costs in Florida",
                capsule(f"As of {PRICE_DATE}, a segmental block retaining wall in Florida runs {price(pk)} per square foot of wall face, or roughly $700 to $2,600 for a 10 linear foot section between 2 and 4 feet tall. Height, not length, drives most of the jump, since a taller wall needs a deeper base and, past certain heights set by each jurisdiction, engineered drawings. We build retaining walls, planters and seat walls across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["homeguide-retaining-wall", "homeguide-sidewalk", "orange-res-plan-guide", "clermont-permit-types",
                         "sarasota-county-22-63-retaining-walls", "palmetto-code-10-46-retaining-wall-permit", "fs713-13"],
                crumbs=[("Cost guides", "/cost/")], crumb="Retaining wall cost", service=K, form=True,
                hero_photo=pids[0] if pids else None, offer=offer(pk), eyebrow="Cost guide")


def artificial_turf_cost():
    K = "artificial-turf"
    pk = "artificial-turf"
    pids = for_service(K, 1)
    body = "".join([
        sec("How much does artificial turf cost in Florida?",
            f"<p>Installed artificial turf in Florida runs {price(pk)} per square foot as of {PRICE_DATE}, with most lawns landing nearer {price(pk, True)} "
            f"({src('homeguide-artificial-grass', 'HomeGuide')}; {src('angi-turf-national', 'Angi')}). Angi's Orlando-specific data puts the average project at $4,758, with a typical range of $2,811 to $6,950 covering excavation, base material and turf together "
            f"({src('angi-turf-orlando', 'Angi, Orlando')}). That's a planning figure, not a quote. What a specific lawn costs depends on how much old sod and irrigation has to come out, how much the yard has to be regraded for drainage, and which backing and infill the project needs.</p>"),
        sec("Artificial turf cost by lawn size",
            f"<p>A straightforward lawn conversion scales close to linear with area, though a very small job can carry a higher effective rate because excavation equipment and crew time don't shrink proportionally with square footage.</p>"
            + table("Artificial turf totals by lawn size", ["Area", f"Market range at {price(pk)}/sq ft"],
                    [["250 sq ft (small side or pet yard)", "$2,500–$6,250"],
                     ["500 sq ft (typical backyard section)", "$5,000–$12,500"],
                     ["750 sq ft", "$7,500–$18,750"],
                     ["1,000 sq ft (full backyard)", "$10,000–$25,000"]],
                    f"Arithmetic on the published Florida and national range of {price(pk)} per square foot, {PRICE_DATE}. Angi's Orlando data puts a roughly 500 sq ft project at $2,811–$6,950 all-in, toward the lower half of this arithmetic range once local labor and material figures are used directly ({src('angi-turf-orlando', 'Angi, Orlando')}).")),
        sec("What drives the price: material, backing and base, not just size",
            "<p>The per-square-foot headline number hides several line items that move independently of lawn size.</p>"
            + table("Artificial turf cost components", ["Component", "Range", "Note"],
                    [["Turf material", "$2–$8 per sq ft", "Nylon runs $5–$8 and polyethylene $5–$10 in Orlando-area pricing"],
                     ["Compacted base", "$1.20–$2.25 per sq ft", "Washed rock, required under Florida's 2026 turf rule"],
                     ["Old lawn or sod removal", "$155–$610 for a typical yard in Orlando; $1–$2.75/sq ft in Tampa", "Varies with how much sod and root mass has to come out"],
                     ["Drainage system, if added", "$1,000–$4,000+", "Beyond the base grading every installation needs"]],
                    f"{src('angi-turf-orlando', 'Angi, Orlando')}; {src('angi-turf-tampa', 'Angi, Tampa')}; {src('angi-turf-national', 'Angi, national')}; {src('homeguide-artificial-grass', 'HomeGuide')}.")),
        sec("How much does a backyard putting green cost?",
            "<p>A backyard putting green costs more per square foot than a lawn panel, commonly $15 to $40 depending on size, since a small green carries more shaping, screeding and edge work per square foot than an open lawn "
            f"({src('homeguide-putting-green', 'HomeGuide, putting greens')}). Angi's size bands run from $25 to $40 per square foot for a green under 400 square feet down to $15 to $25 for one over 2,000, with a typical project averaging about $4,300 "
            f"({src('angi-putting-green', 'Angi, putting greens')}). Each cup and flagstick adds roughly $150. DIY kits run far less, $5 to $20 per square foot, but skip the precisely screeded base a true putting surface needs to roll true.</p>"),
        sec("Does turf cost more in Orlando or Tampa/Sarasota?",
            f"<p>Published averages show a real gap: Orlando's typical project averages $4,758 against Tampa's $7,246 ({src('angi-turf-orlando', 'Angi, Orlando')}; {src('angi-turf-tampa', 'Angi, Tampa')}). We use Tampa as the closest published comparison for the Sarasota–Manatee side, since no Angi or HomeGuide page breaks out Sarasota turf pricing specifically. That difference more likely reflects the mix of project sizes each page's data draws from than a real cost gap between the two coasts; a 500 square foot pet run and a 2,000 square foot full-yard conversion average very differently even at the same per-square-foot rate. We quote by yard size and scope, not by which coast the address sits on.</p>"),
        sec("What Florida's 2026 turf rule adds to (and removes from) a quote",
            f"<p>DEP Rule 62-308.100, effective May 19, 2026, sets a material floor every residential turf quote in Florida has to meet: a washed crushed-rock or crushed-concrete base, with the fines removed so water keeps moving through it, and infill limited to clean sand, rock, shell or coated silica sand, with rubber crumb allowed only inside a playground footprint "
            f"({src('rule62-308-100-text', 'DEP Rule 62-308.100')}). That standard removes some of the cheapest shortcuts a bid used to be able to take, limerock or road base with fines compacted underneath, or loose rubber infill swept in to save a material cost, which is worth knowing before comparing an unusually low bid against the ranges on this page. {svc('artificial-turf', 'Our artificial turf page')} has the complete rule, including the water setback and tree drip-line requirements that can affect where turf is installed on a given lot.</p>"),
        sec("Are there rebates for replacing grass with artificial turf in Florida?",
            "<p>No, not in the programs we could verify. Several utilities and water districts covering both service areas run Florida-Friendly Landscaping rebates that pay homeowners to replace irrigated turf grass, but each one we checked defines the replacement as living, drought-tolerant plants verified by an extension service or conservation staff, not a synthetic surface. "
            f"Manatee County's Landscape Retrofit rebate, for example, pays 50 percent of documented costs up to $1,500 for replacing grass with Florida-Friendly landscaping, and requires an approved planting plan and an in-person evaluation before and after the work "
            f"({ext('https://www.mymanatee.org/services-and-amenities/service-listing/service-details/apply-for-outdoor-water-conservation-rebate-programs', 'Manatee County, Outdoor Water Conservation Rebate Programs')}). Orlando Utilities Commission's Florida-Friendly Landscape and Irrigation Rebate works the same way, paying up to $200 toward qualifying Florida-Friendly plants and microirrigation, with the plant list itself excluding anything that isn't a living plant "
            f"({ext('https://www.ouc.com/solutions-programs/savings/rebates/landscape-irrigation/', 'Orlando Utilities Commission, Florida-Friendly Landscape and Irrigation Rebate')}). We don't build a rebate into a turf estimate, and a homeowner weighing turf against a water-saving plant conversion should check directly with their own utility before counting on one.</p>"),
        sec("Two turf budgets, worked through",
            f"<p>Say you have a fenced 300 square foot side yard near {city('windermere')} you want to convert to a pet run, with the old St. Augustine sod coming out and a more open-backed turf going in for drainage. Removal and excavation on a yard that size typically fall in the $150 to $400 range, and the turf and base work at the standard rate run roughly $3,000 to $7,500, putting the full job somewhere around $3,200 to $7,900.</p>"
            f"<p>Say instead you want a 500 square foot backyard putting green on a flat lot near {city('lakewood-ranch')}, with a few cups and a fringe area around the edge. At the small-green rate of $25 to $40 per square foot, the green itself runs roughly $12,500 to $20,000, plus a few hundred dollars for the cups and flagsticks, well above what the same square footage would cost as a standard lawn panel.</p>"),
        sec("Getting turf cost down without cutting the base",
            "<p>The washed-rock base under turf isn't optional under Florida's 2026 rule, and it shouldn't be the place a bid saves money even where it is. There are still real ways to bring the price down:</p>"
            + ul(["Keep the layout simple. A lawn shape with a lot of curves around beds, a pool deck edge or a tree canopy needs more cutting and seaming than an open rectangle.",
                  "Reuse existing irrigation heads for the beds and sod that still need them instead of pulling the whole system; the rule only requires heads inside the turf footprint to be capped, not the entire yard re-plumbed.",
                  "Skip a pet-specific open-backed system where there are no pets using the area regularly; standard backing costs less and drains adequately for ordinary foot traffic.",
                  "Bundle a turf accent strip into the same mobilization as a paver patio or walkway project, sharing one crew visit and one base delivery.",
                  "Ask whether a narrow side yard needs hand excavation or whether equipment can reach it; access, not turf material, is often what separates a mid-range bid from a high one on a tight lot."])),
        sec("What a turf quote should spell out",
            "<p>Ask every bidder for the same specifics so two quotes describe the same job:</p>"
            + ul(["Base material named specifically as washed crushed rock or crushed concrete, not just 'compacted base'",
                  "Infill material named: clean sand, rock, shell or coated silica sand, with no rubber crumb outside a playground footprint",
                  "Whether the project sits within 10 feet of a pond, canal or other waterbody, or inside a tree's drip line, and how the quote addresses either one",
                  "The irrigation plan in writing: which heads get capped and where, since in-ground systems can't water turf directly",
                  "Whether removal and haul-off of the old sod or landscaping is included in the price shown"])),
        sec("Related reading",
            f"<p>For the full material standard and installation steps, see {svc('artificial-turf', 'our artificial turf page')}. {compare('artificial-turf-vs-sod', 'Our turf vs. sod comparison')} runs the water-savings math in more depth, and {post('backyard-putting-green-florida', 'planning a backyard putting green')} and {post('artificial-turf-for-dogs-florida', 'turf for dogs')} go further on those two specific uses. The {a('/cost/', 'cost guide hub')} rounds up pricing for concrete, pavers and everything in between.</p>"),
    ])
    faqs = [
        faq("How much does artificial turf cost in Florida?",
            f"Installed turf runs {price(pk)} per square foot, with most lawns landing nearer {price(pk, True)}. Angi's Orlando-specific data puts a typical project at $2,811 to $6,950 all-in, covering excavation, base and turf material together."),
        faq("How much does a backyard putting green cost?",
            "More per square foot than a standard lawn: commonly $15 to $40, with smaller greens under 400 square feet running toward $25 to $40 and larger ones over 2,000 square feet closer to $15 to $25. A typical project averages around $4,300, and each cup and flagstick adds roughly $150 more."),
        faq("Are there rebates for replacing grass with artificial turf in Florida?",
            "Not that we could verify. Florida-Friendly Landscaping rebates, including Manatee County's Landscape Retrofit program and Orlando Utilities Commission's landscape and irrigation rebate, pay for replacing turf grass with living, drought-tolerant plants verified by an inspection, not a synthetic surface. We don't build a rebate into a turf estimate, and checking directly with your own utility is the reliable way to confirm current terms."),
        faq("Why is Orlando's average turf project cheaper than Tampa's?",
            "Published averages, $4,758 for Orlando against $7,246 for Tampa, likely reflect a different mix of project sizes in each dataset more than a real cost gap between the coasts. A small pet run and a full backyard conversion average very differently even priced at the same per-square-foot rate, which is why we quote by yard size and scope rather than by metro."),
        faq("Does pet turf cost more than a standard lawn?",
            "It can, mainly because of backing and drainage rather than the turf fiber itself. A pet area typically uses a more open, perforated backing for faster drainage and a steeper base slope, both of which add labor over a standard lawn panel. We don't have a verified Florida-specific per-square-foot figure for pet turf alone to quote here."),
        faq("Does putting green pricing include the cups and flagsticks?",
            "Not always; published pricing often lists them separately. Each hole and flagstick adds roughly $150 on top of the per-square-foot green price, which covers the turf, the precisely screeded base and the fringe area around the cups."),
        faq("Does turf over an existing pool deck or patio cost less than a full yard?",
            "It can, since there's no excavation or new base to build, just a drainage layer or pad between the hard surface and the turf. The washed-rock base rule for a ground-level lawn doesn't apply the same way on top of an existing slab, which is one reason turf set over a deck or patio sometimes runs toward the lower end of published ranges.")]
    return page("/artificial-turf-cost/", "price", "Artificial Turf Cost in Florida (2026)",
                f"Florida artificial turf cost as of {PRICE_DATE}: {price(pk)} per sq ft installed, Orlando and Tampa averages, putting green pricing, and the rebate question answered.",
                "What Artificial Turf Costs in Florida",
                capsule(f"As of {PRICE_DATE}, installed artificial turf in Florida runs {price(pk)} per square foot, with a typical Orlando project averaging $4,758 and a typical Tampa-area project averaging $7,246. A backyard putting green costs more, commonly $15 to $40 per square foot on a small green. Florida's 2026 turf rule requires a washed-rock base and natural infill in every quote. We install turf across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["homeguide-artificial-grass", "angi-turf-national", "angi-turf-orlando", "angi-turf-tampa", "homeguide-putting-green",
                         "angi-putting-green", "rule62-308-100-text",
                         ("Manatee County, Outdoor Water Conservation Rebate Programs", "https://www.mymanatee.org/services-and-amenities/service-listing/service-details/apply-for-outdoor-water-conservation-rebate-programs"),
                         ("Orlando Utilities Commission, Florida-Friendly Landscape and Irrigation Rebate", "https://www.ouc.com/solutions-programs/savings/rebates/landscape-irrigation/")],
                crumbs=[("Cost guides", "/cost/")], crumb="Artificial turf cost", service=K, form=True,
                hero_photo=pids[0] if pids else None, offer=offer(pk), eyebrow="Cost guide")


def get_pages():
    return [paver_patio_cost(), paver_sealing_cost(), retaining_wall_cost(), artificial_turf_cost()]
