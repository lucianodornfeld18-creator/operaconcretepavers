# -*- coding: utf-8 -*-
"""Cost guides: concrete driveway, concrete patio, stamped concrete, pool deck (module c_cost_a of COST_PAGES)."""
from _data import SERVICES, PRICE_DATE
from _helpers import page, capsule, sec, table, faq, ul, a, svc, post, compare, src, price, per, offer
from _photos import for_service


def driveway_cost():
    K = "concrete-driveways"
    pk = SERVICES[K]["price"]
    pids = for_service(K, 1)
    body = "".join([
        sec("How much does a concrete driveway cost in Florida?",
            f"<p>A new concrete driveway runs {price(pk)} per square foot installed in Florida as of {PRICE_DATE}, with most jobs landing nearer {price(pk, True)} ({src('homeguide-concrete-driveway', 'HomeGuide, 2025')}). "
            f"Angi's Orlando data puts the average project at $6,490, with a reported range of $2,738 to $14,703 and a per-square-foot spread of $5 to $21 once demolition, thickness and reinforcement are factored in ({src('angi-driveway-orlando', 'Angi Orlando, May 2026')}). "
            "That per-square-foot number is a starting point for a conversation, not a quote. What a specific driveway costs depends on how much of the old surface comes out, how deep the base goes, and whether the apron needs engineering review before a crew can pour.</p>"
            "<h3>Price by finish, from plain gray to decorative</h3>"
            f"<p>HomeGuide breaks concrete driveways into four tiers by finish: standard plain gray at $6 to $10 per square foot, basic (single-color stain, a stenciled border, broom or exposed-aggregate texture) at $10 to $15, mid-range stamped work with two or three colors at $15 to $20, and high-end multi-color stamped work at $20 to $25 or more ({src('homeguide-concrete-driveway', 'HomeGuide')}). "
            f"A separate stamped-specific guide lists stamped driveways anywhere from $8 to $26 per square foot and stained driveways at $8 to $25 ({src('homeguide-stamped', 'HomeGuide, Dec 2025')}). If a pattern and color system is the goal rather than a plain slab, {a('/stamped-concrete-cost/', 'our stamped concrete cost guide')} spells out tier-by-tier pricing in more depth than fits here.</p>"),
        sec("What does it cost to replace a 2-car driveway?",
            "<p>Replacing a 400 to 576 square foot two-car driveway typically runs $3,200 to $9,100 before demolition, and $800 to $4,600 more once the old slab comes out and gets hauled off. "
            f"Angi's Orlando cost calculator shows a 20x20 ft (400 sq ft) driveway at $3,240 to $7,200 and a 24x24 ft (576 sq ft) driveway at $4,800 to $8,720, using the same standard sizes HomeGuide uses nationally ({src('angi-driveway-orlando', 'Angi Orlando, May 2026')}; {src('homeguide-concrete-driveway', 'HomeGuide')}). "
            "Demolition and disposal of the old driveway is usually priced as its own line rather than folded into the per-square-foot rate, because the cost depends on how thick the old slab is and whether it has reinforcing steel inside it.</p>"
            + table("Concrete driveway totals by size, before demolition", ["Driveway size", "Area", f"Market range at {price(pk)}/sq ft"],
                    [["One-car (10 × 20 ft)", "200 sq ft", "$1,200–$3,000"],
                     ["One-car, deep (12 × 24 ft)", "288 sq ft", "$1,730–$4,320"],
                     ["Two-car (20 × 20 ft)", "400 sq ft", "$2,400–$6,000"],
                     ["Two-car, deep (24 × 24 ft)", "576 sq ft", "$3,460–$8,640"],
                     ["Three-car (24 × 36 ft)", "864 sq ft", "$5,180–$12,960"]],
                    f"Arithmetic on the published Florida market range of {price(pk)} per square foot, {PRICE_DATE}. Sizes are the standard bands HomeGuide and Angi use; demolition, a thicker 6-inch section, rebar or a stamped finish add to every row.")
            + "<p>Those figures assume a bare lot with no old slab to remove. Add $2 to $6 per square foot nationally for tearing out an existing driveway, or $5 to $8 in Orlando's published figures; a 400-square-foot removal in that range runs roughly $2,000 to $3,200 on top of the new-pour total "
            f"({src('homeguide-concrete-driveway', 'HomeGuide')}; {src('angi-driveway-orlando', 'Angi Orlando')}).</p>"),
        sec("Is a concrete driveway cheaper in Orlando or Sarasota?",
            "<p>Published data puts Orlando and the Tampa Bay area within a few dollars of each other, and we use Tampa as the closest published comparison for the Sarasota–Manatee side because Angi has not built a Sarasota-specific driveway page. "
            f"Angi's two city pages both cite average projects near $6,450 to $6,490, though Tampa's quoted per-square-foot range runs a little higher at $8 to $20 against Orlando's $5 to $21 ({src('angi-driveway-orlando', 'Angi Orlando, May 2026')}; {src('angi-driveway-tampa', 'Angi Tampa, May 2026')}). A 2018-era Sarasota ZIP-code estimator shows $5.18 per square foot, but that figure is too old to compare directly to current pricing.</p>"
            + table("Orlando vs. Tampa published totals, by driveway size", ["Driveway size", "Orlando total", "Tampa total (nearest published metro to Sarasota)"],
                    [["One-car (10 × 20 ft, 200 sq ft)", "$1,620–$3,040", "$1,600–$2,200"],
                     ["Two-car (20 × 20 ft, 400 sq ft)", "$3,240–$7,200", "$3,200–$4,400"],
                     ["Three-car (24 × 36 ft, 864 sq ft)", "$7,000–$12,600", "$6,900–$9,500"]],
                    "Angi's own city-level figures, May 2026; Tampa stands in for the Suncoast because Angi publishes no Sarasota driveway page.")
            + "<p>We price projects by scope, not by ZIP code. What actually separates a Windermere bid from a Lakewood Ranch bid isn't the city line; it's how much base the sandy or flatwoods subgrade needs, whether the apron falls under a city engineering permit, and how far a truck has to reach around a pool cage or a tight side yard.</p>"),
        sec("What moves a driveway quote up or down",
            "<p>Per-square-foot numbers hide the line items that separate one bid from another on the same lot. These are the ones that come up most in Florida specifically:</p>"
            + table("Driveway cost drivers", ["Factor", "What it does to the price", "Florida detail"],
                    [["Demolition", "Adds $2–$8 per sq ft depending on thickness and reinforcement", "Orlando figures run $5–$8/sq ft; Tampa's published figure is $2.90–$5"],
                     ["Thickness", "4 in. runs $6–$15; a 5–6 in. section for RVs or boat trailers runs $8–$20", "Some jurisdictions require a thicker apron section where the drive crosses the right-of-way, regardless of the rest of the slab"],
                     ["Subgrade and base", "Soft or sandy soil needs more compacted fill before the pour", "Tampa's cost guide adds $1–$2/sq ft specifically for compacting fill over Florida's sandy subgrade"],
                     ["Access", "A truck that can't reach the forms means a pump or buggies", "Narrow side-yard access or a locked gate around a pool cage is common on Florida lots built close together"],
                     ["Permits", "A right-of-way or engineering permit for the apron", "National figures cite $50–$200; several cities we build in require a specific 6-inch apron section even when the rest of the drive is 4 inches"],
                     ["Finish and color", "Broom is the floor; stamped and multi-color runs the top of the range", "Stamped driveways run $8–$26/sq ft against $6–$15 for plain broom concrete"]],
                    "Ranges drawn from the Florida and national sources cited on this page.")),
        sec("Two driveway budgets, worked through",
            "<p>Say you have a 1990s ranch off Kirkman Road with a cracked 400-square-foot two-car driveway that needs to come out. At the published Orlando range, demolition runs roughly $2,000 to $3,200, and the new 4-inch pour runs $2,400 to $6,000, putting the whole job somewhere around $4,400 to $9,200 before a decorative finish, with the final number landing closer to the low end for a plain broom finish and closer to the top for exposed aggregate or a stamped border.</p>"
            "<p>Say instead you have a bare 1-acre lot near Parrish with no existing driveway and plan a 288-square-foot single-car drive connecting to a culvert at the road. Skipping demolition entirely, the new-pour range is $1,730 to $4,320, and a culvert or access permit at the county level typically adds a few hundred dollars on top. "
            "In both cases, a written quote that itemizes demolition, base, thickness and finish separately is the only way to see where the money is actually going.</p>"),
        sec("Cutting the price without cutting the base",
            "<p>The base is the one place a Florida driveway should never get thinner just to hit a number, because a shallow or uncompacted base is what shows up as a sunken edge or a hairline crack a year or two later. There are still real ways to bring a bid down:</p>"
            + ul(["Choose a plain broom finish over a stamped or multi-color pattern. The finish, not the structure underneath, is where tiers $6–$10, $10–$15 and $15–$20+ diverge.",
                  "Keep the layout rectangular. Curves, radiuses and extra forming edges add labor time that a straight run doesn't need.",
                  "Pour the driveway and an adjoining walkway or pad in the same mobilization. One truck, one crew day and one set of forms split across two jobs costs less than two separate visits.",
                  "Ask whether the existing base is sound enough to reuse under a resurfacing overlay instead of a full tear-out, when the slab itself is cracked but the subgrade underneath hasn't settled.",
                  "Schedule outside the rainy season's busiest stretch. A crew juggling fewer rain delays in the dry months often has more flexibility on timing, which can matter more to the final price than it seems."])),
        sec("What a driveway quote should spell out",
            "<p>A square-foot number by itself doesn't tell you much. Ask every bidder for the same list of specifics so the totals are comparing the same job:</p>"
            + ul(["Slab thickness and concrete strength (4 in. at 3,000–4,000 psi is standard; 5–6 in. for RVs and trailers)",
                  "Reinforcement: fiber mesh, wire mesh or rebar, and whether it's included or an add-on",
                  "Base depth and what gets compacted before the pour, not just that a base exists",
                  "Demolition and haul-off as a separate, itemized line if an old driveway is coming out",
                  "Who applies for the right-of-way or engineering permit, and whether the fee is in the price",
                  f"Whether sealing is included; it's typically $1 to $3 per square foot extra in national data when it's added on, separate from the base concrete price. Florida's lien law requires a recorded Notice of Commencement on any project over $2,500 ({src('fs713-13', 'F.S. 713.13')}), and a contractor who collects more than a 10% deposit has specific permitting and start-date obligations under {src('fs489-126', 'F.S. 489.126')}"])),
        sec("Related reading",
            f"<p>For the install itself, see {svc('concrete-driveways', 'our concrete driveways page')}, which covers thickness, control joints and the step-by-step process. If a slab versus pavers is still an open question, {compare('pavers-vs-concrete-driveway', 'our pavers vs. concrete driveway comparison')} and {compare('concrete-driveway-finishes', 'broom vs. exposed aggregate vs. stamped')} go through the trade-offs. "
            f"A driveway that's holding up but showing cracks might not need a full replacement; {compare('resurface-vs-replace-concrete', 'resurface or replace a concrete driveway')} and {post('concrete-driveway-cracks-florida', 'which cracks are normal in Florida')} cover that decision. "
            f"{post('driveway-apron-and-right-of-way-florida', 'Who owns the driveway apron')} is worth a read before the first bid if the lot backs onto a public street, and the {a('/cost/', 'full cost guide hub')} lists market ranges for every service we build.</p>"),
    ])
    faqs = [
        faq("Does a concrete driveway quote usually include the permit fee?",
            "It should list the fee as a separate line, or state plainly that it's included. National cost data puts driveway or right-of-way permit fees at $50 to $200, and several of the cities we work in require a specific thicker apron section where the drive crosses the public right-of-way, which the permit office checks at inspection."),
        faq("How much more does a stamped or colored driveway cost than plain gray?",
            "Roughly double. HomeGuide's tiers run $6 to $10 per square foot for standard plain gray concrete up to $20 to $25 or more for high-end, multi-color stamped work, with basic color or texture and mid-range stamped patterns in between. The jump comes from labor time and materials, not the base concrete itself."),
        faq("Is a per-square-foot price enough to compare two driveway bids?",
            "Not on its own. Two bids at the same per-square-foot number can describe different jobs if one includes demolition, a thicker 6-inch section or rebar and the other doesn't. Ask each contractor to itemize thickness, reinforcement, base depth and who pulls the permit before comparing totals."),
        faq("How much does demolition add to a driveway replacement in Florida?",
            "National data puts removal of an old driveway at $2 to $6 per square foot, and Orlando's published figures run a bit higher at $5 to $8 per square foot including haul-off. For a typical 400-square-foot two-car driveway, that's roughly $800 to $3,200 added to the new-pour price."),
        faq("Why do some quotes price concrete by the cubic yard and others by the square foot?",
            "Both describe the same job. The square-foot price covers forming, pouring, finishing and joint work for the whole slab; the cubic-yard figure is just the raw ready-mix delivery cost, which Angi lists at roughly $120 to $170 a yard in Orlando. A 400-square-foot, 4-inch driveway needs about 5 yards of concrete, a small share of the total project cost."),
        faq("Does a wider driveway cost proportionally more per square foot?",
            "Mostly yes, since material and base costs scale with area, but very small jobs can carry a higher effective rate because mobilization, forming and minimum crew time get spread over less square footage. A single-car extension poured on its own often prices closer to the top of the range than the same square footage poured as part of a larger driveway.")]
    return page("/concrete-driveway-cost/", "price", "Concrete Driveway Cost in Florida (2026)",
                f"Concrete driveway cost in Florida as of {PRICE_DATE}: {price(pk)} per sq ft, size tables for 1- to 3-car driveways, and Orlando vs. Tampa pricing.",
                "What a New Concrete Driveway Costs in Florida",
                capsule(f"As of {PRICE_DATE}, a new concrete driveway in Florida runs {price(pk)} per square foot installed, with most jobs landing nearer {price(pk, True)} ({src('homeguide-concrete-driveway', 'HomeGuide')}). "
                        "A 400 square foot two-car driveway works out to roughly $2,400 to $6,000 before demolition, which typically adds $800 to $3,200 more on a replacement."),
                body, faqs=faqs,
                sources=["homeguide-concrete-driveway", "homeguide-stamped", "angi-driveway-orlando", "angi-driveway-tampa", "promatcher-driveways-sarasota", "fs713-13", "fs489-126"],
                crumbs=[("Cost guides", "/cost/")], crumb="Concrete driveway cost", service=K, form=True,
                hero_photo=pids[0] if pids else None, offer=offer(pk), eyebrow="Cost guide")


def patio_cost():
    K = "concrete-patios"
    pk = SERVICES[K]["price"]
    pids = for_service(K, 1)
    body = "".join([
        sec("How much does a concrete patio cost in Florida?",
            f"<p>A new concrete patio runs {price(pk)} per square foot installed as of {PRICE_DATE}, with a typical job closer to {price(pk, True)} ({src('homeguide-concrete-patio', 'HomeGuide, Jul 2025')}). "
            f"Angi's Orlando figures for concrete slab work show patios landing at $4 to $7 per square foot depending on finish, with a 450-square-foot patio running about $2,700 ({src('angi-slab-orlando', 'Angi Orlando, Apr 2026')}). "
            "Plain broom-finish concrete sits at the bottom of the range; stained, stamped or exposed-aggregate finishes push a patio well past it, which is why the finish question matters as much as the square footage.</p>"),
        sec("How much does a 12x12 concrete patio cost?",
            "<p>A 12 × 12 ft patio (144 square feet) in plain concrete runs roughly $860 to $1,870 at Florida market rates. Smaller patios like a 10 × 10 ft pad (100 sq ft) and larger ones like a 12 × 20 ft extension (240 sq ft) scale the same way, before a stamped or stained finish adds more.</p>"
            + table("Concrete patio totals by size, plain broom finish", ["Patio size", "Area", f"Market range at {price(pk)}/sq ft"],
                    [["Small pad (10 × 10 ft)", "100 sq ft", "$600–$1,300"],
                     ["Seating area (12 × 12 ft)", "144 sq ft", "$860–$1,870"],
                     ["Lanai extension (12 × 20 ft)", "240 sq ft", "$1,440–$3,120"],
                     ["Full back patio (20 × 20 ft)", "400 sq ft", "$2,400–$5,200"]],
                    f"Arithmetic on the Florida market range of {price(pk)} per square foot, {PRICE_DATE}. A stained or stamped finish adds to every row; see the finish table below.")),
        sec("Is a concrete patio cheaper than a paver patio?",
            "<p>Yes, for a comparable plain-to-mid finish, concrete usually prices lower up front than pavers. "
            f"Florida market data runs {price(pk)} per square foot for concrete against {price('paver-patio')} for a paver patio, which means a 400-square-foot patio in plain concrete lands well under the low end of a paver quote for the same footprint. "
            f"That's a price-only answer; pavers make up some of the gap with easier spot repairs and no resealing schedule tied to a single continuous slab. The full decision, including upkeep and how each surface takes a Florida summer, is in {compare('stamped-concrete-vs-pavers', 'our stamped concrete vs. pavers comparison')}.</p>"),
        sec("Cost by finish: broom, exposed aggregate, stained or stamped",
            f"<p>HomeGuide's patio-specific data lines finishes up this way ({src('homeguide-concrete-patio', 'HomeGuide')}; {src('homeguide-exposed-aggregate', 'HomeGuide, 2023')}):</p>"
            + table("Concrete patio cost by finish, per sq ft installed", ["Finish", "Range", "Notes"],
                    [["Plain broom", "$4–$12", "Lowest cost; textured for slip resistance"],
                     ["Exposed aggregate", "$7–$18", "About $2–$3 more than plain concrete; stone shows through the surface"],
                     ["Stained", "$8–$25", "Color applied to existing or new concrete; wide range by complexity"],
                     ["Stamped", "$9–$30", f"Pattern and texture; see {svc('stamped-concrete', 'our stamped concrete cost guide')} for tiers"],
                     ["Epoxy-coated new slab", "$7–$22", "Coating applied over a fresh pour, common on garage-adjacent pads"]],
                    "National ranges from HomeGuide's patio and exposed-aggregate cost guides.")),
        sec("What moves a patio quote up or down",
            "<p>Beyond the per-square-foot finish tier, these items separate one patio bid from another:</p>"
            + table("Patio cost drivers", ["Factor", "What it does to the price", "Florida detail"],
                    [["Access under a screen enclosure", "Limits truck and pump reach; buggies or wheelbarrows take longer", "Common on Florida lots where the patio sits inside a pool cage or lanai"],
                     ["Demolition of an old patio or pad", "$3–$8 per sq ft nationally, including disposal", "Reinforced slabs cost $1–$3/sq ft more to break up"],
                     ["Base and drainage slope", "Compacted fill where the subgrade is soft, and grading away from the house", "Flatwoods soils common in both service areas hold water near the surface part of the year"],
                     ["Finish complexity", "Broom is the floor; stamped, multi-color and exposed aggregate run the top", "Stamped patio tiers run $8–$30 depending on color count"],
                     ["Permits and impervious limits", "Some cities cap how much of a lot can be hard surface", "Several cities in both service areas require a zoning or impervious-surface review before a patio addition goes in"]],
                    "Ranges from HomeGuide and Angi; permit specifics vary by city, see the permits hub below.")),
        sec("Two patio budgets, worked through",
            "<p>Say you have a 14 × 20 ft lanai extension (280 sq ft) planned off a Winter Garden kitchen, poured in plain broom concrete with no demolition involved. At Florida market rates, that lands around $1,680 to $3,640 before a zoning check on the lot's impervious coverage, which several Orange County-area cities require once a hard surface is added.</p>"
            "<p>Say instead you have a cracked 200-square-foot patio slab off a Venice lanai that needs to come out before a 240-square-foot replacement goes in, this time with a light exposed-aggregate finish. Demolition on the old pad runs roughly $600 to $1,600, and the new exposed-aggregate pour at $7 to $18 per square foot adds another $1,680 to $4,320, putting the full job in the $2,280 to $5,920 range depending on access and the exact aggregate finish chosen.</p>"),
        sec("Saving money without thinning the base",
            "<p>The base and the control-joint layout are not places to trim on a Florida patio; a thin or poorly compacted base is what shows up as a sunken corner later. Real savings live elsewhere:</p>"
            + ul(["Pick broom or a light stain instead of stamped or exposed aggregate. The finish tier, not the slab underneath, drives most of the spread between $4 and $30 per square foot.",
                  "Keep the shape simple. A rectangular patio needs less forming labor than one with curved edges or multiple levels.",
                  "Pour the patio in the same visit as a nearby walkway or pad if both are on the project list, splitting one mobilization across two smaller jobs.",
                  "Ask whether a cracked but otherwise sound slab can be resurfaced with an overlay instead of torn out and replaced; overlays run well under full demolition and repour pricing.",
                  "Confirm the impervious-surface limit for the lot before finalizing the size. A patio sized to stay under a city's coverage cap avoids a redesign mid-project."])),
        sec("Does a patio addition need a permit, and does that change the price?",
            "<p>Sometimes, and when it does the permit fee is a small add-on next to the concrete itself, usually well under a few hundred dollars. What actually matters is whether the lot has room left under its impervious-surface cap, because a patio that pushes a lot over the limit can mean a redesign, not just a fee.</p>"
            f"<p>Several cities on both sides of the state cap how much of a residential lot can be covered by roofs, driveways, patios and pool decks before it counts against stormwater rules. The City of Sarasota sets that cap at 60% to 75% of the lot depending on zoning district ({src('city-sarasota-zoning-vi-203-impervious', 'City of Sarasota Zoning Code')}), and the City of Winter Garden requires an impervious-area worksheet filed with any permit that adds hard surface, regardless of size ({src('wintergarden-isr-worksheet', 'Winter Garden worksheet')}).</p>"
            "<p>None of this changes the per-square-foot concrete price; it changes whether the patio you're pricing is the size you'll actually be allowed to build. Checking the lot's remaining impervious allowance before finalizing a layout avoids paying for a design that a permit reviewer later shrinks.</p>"),
        sec("Is a concrete patio priced differently in Orlando than in Sarasota?",
            "<p>Not by much, based on the published data available. Angi's Orlando figures for patio-adjacent slab work show $4 to $7 per square foot depending on finish, inside the broader Florida range this page uses throughout. No Sarasota-specific patio guide from a major cost-data publisher turned up in research for this page, so the closest comparison is the same statewide range rather than a second city figure.</p>"
            "<p>What tends to separate a Lakewood Ranch patio bid from a Clermont one isn't the county line. It's usually the subgrade under the slab, how tight the access is through a pool cage or side yard, and whether the city requires an impervious-surface review before the permit gets issued.</p>"),
        sec("What a patio quote should include",
            "<p>A patio bid worth comparing spells out:</p>"
            + ul(["Finish and whether color, texture or an exposed-aggregate mix is included in the base price",
                  "Thickness (4 in. is standard for patios, matching the code floor plus margin for foot traffic)",
                  "Base prep: what gets removed, what gets compacted, and the slope direction for drainage away from the house",
                  "Demolition as its own line item if an old patio or pad is being replaced",
                  "Whether a zoning or impervious-surface permit applies to the lot, and who's responsible for pulling it",
                  "Control joint layout, since joints placed well are what keep a patio from cracking in a random, visible line across the slab"])),
        sec("Related reading",
            f"<p>See {svc('concrete-patios', 'our concrete patios page')} for the install process and finish options, or {svc('stamped-concrete', 'stamped concrete')} if a pattern is part of the plan. "
            f"{compare('stamped-concrete-vs-pavers', 'Stamped concrete vs. pavers')} covers the full decision between surfaces, and {post('concrete-patio-ideas-florida', 'concrete patio ideas for Florida homes')} and {post('extend-patio-under-screen-enclosure', 'extending a patio under a pool screen enclosure')} go further into layout and design. "
            f"The {a('/cost/', 'cost guide hub')} lists every service's market range side by side.</p>"),
    ])
    faqs = [
        faq("How much does a 12x12 concrete patio cost?",
            "A 144-square-foot patio in plain broom concrete runs roughly $860 to $1,870 at current Florida market rates. A stained or exposed-aggregate finish on the same footprint typically adds a few hundred dollars more, and a stamped pattern can roughly double the total."),
        faq("Is a concrete patio cheaper than a paver patio?",
            "Yes, for most comparable finishes. Florida market data puts plain-to-mid concrete at roughly half the per-square-foot rate of a paver patio. Pavers cost more up front but can be spot-repaired without a visible patch, which is the trade-off the full comparison covers."),
        faq("Does extending an existing patio cost the same as pouring a new one?",
            "Roughly, if the extension is poured in plain concrete and ties cleanly into the existing slab's grade. Tying a new pour to an old one well enough that it doesn't crack along the seam takes a bit more planning than an isolated pad, which can show up as a small line-item difference rather than a change in the per-square-foot rate."),
        faq("Does a concrete patio under a pool cage cost more to install?",
            "Often slightly, because a truck or pump may not reach through a screen enclosure, which means wheelbarrows or a longer pump hose and more labor time. It's worth asking a bidder directly how they plan to get concrete to a patio inside a cage before comparing quotes."),
        faq("What's the price difference between a 10x10 and a 20x20 concrete patio?",
            "At Florida market rates, a 10 × 10 ft pad (100 sq ft) runs about $600 to $1,300, while a 20 × 20 ft patio (400 sq ft) runs about $2,400 to $5,200, four times the area at roughly the same per-square-foot rate. Larger patios sometimes land slightly lower per square foot once mobilization costs spread across more concrete.")]
    return page("/concrete-patio-cost/", "price", "Concrete Patio Cost in Florida (2026)",
                f"Concrete patio cost in Florida as of {PRICE_DATE}: {price(pk)} per sq ft, a size table from 10x10 to 20x20 ft, and concrete vs. paver patio pricing.",
                "Pricing a New Concrete Patio in Orlando and Sarasota–Manatee",
                capsule(f"As of {PRICE_DATE}, a new concrete patio in Florida runs {price(pk)} per square foot installed, closer to {price(pk, True)} for most jobs ({src('homeguide-concrete-patio', 'HomeGuide')}). "
                        "A 12 × 12 ft patio in plain broom concrete runs roughly $860 to $1,870; a 20 × 20 ft patio runs $2,400 to $5,200, before a stained or stamped finish."),
                body, faqs=faqs,
                sources=["homeguide-concrete-patio", "homeguide-exposed-aggregate", "angi-slab-orlando", "city-sarasota-zoning-vi-203-impervious", "wintergarden-isr-worksheet"],
                crumbs=[("Cost guides", "/cost/")], crumb="Concrete patio cost", service=K, form=True,
                hero_photo=pids[0] if pids else None, offer=offer(pk), eyebrow="Cost guide")


def stamped_cost():
    K = "stamped-concrete"
    pk = SERVICES[K]["price"]
    pids = for_service(K, 1)
    body = "".join([
        sec("How much does stamped concrete cost per square foot in Florida?",
            f"<p>Stamped concrete runs {price(pk)} per square foot installed in Florida as of {PRICE_DATE}, with most jobs falling nearer {price(pk, True)} ({src('homeguide-stamped', 'HomeGuide, Dec 2025')}). "
            "That range covers both patios and driveways; HomeGuide's own numbers show a 20 × 20 ft stamped patio at $3,200 to $7,600 and a stamped driveway running $12 to $18 per square foot once the heavier driveway-grade mix and traffic-rated finish are factored in. "
            f"A Homewyse national figure quotes a much higher $26.27 to $31.94 per square foot starting point; it's an outlier against every other guide checked for this page and shouldn't be treated as the Florida market number ({src('homewyse-stamped', 'Homewyse, Sep 2026')}).</p>"),
        sec("Why does stamped concrete cost more than plain concrete?",
            "<p>Stamped concrete costs more because of labor timing, not materials. A crew has a narrow window after the slab is poured and floated to press a pattern mold into the surface, dust or liquid-release the color, and clean the texture lines, all before the concrete sets up too firm to take an impression. "
            "That window compresses a normally forgiving finishing step into something closer to a race against the clock, and it takes a crew that's done it before to get clean lines on a hot Florida afternoon. "
            "Color and sealer add their own cost: integral color mixed into the batch, a release agent or antiquing stain worked into the texture, and a sealer coat that both locks the color in and protects the surface, compared to a broom finish that needs none of those steps.</p>"),
        sec("Cost by pattern and color complexity",
            f"<p>HomeGuide splits stamped work into three tiers by color and pattern complexity ({src('homeguide-stamped', 'HomeGuide')}):</p>"
            + table("Stamped concrete cost by tier, per sq ft installed", ["Tier", "Range", "What's included"],
                    [["Basic", "$8–$13", "One pattern, a single uniform color"],
                     ["Mid-range", "$13–$19", "Two or more colors, a custom border or accent band"],
                     ["High-end", "$19–$26+", "Multi-color layering, antiquing and complex patterns"],
                     ["Stamped overlay on existing concrete", "$7–$15", "Applied over a sound old slab instead of a full tear-out and repour"],
                     ["Stamped walkway", "$10–$21", "Narrower footprint; the same pattern and color options apply"]],
                    "National ranges from HomeGuide's stamped concrete cost guide, December 2025.")),
        sec("Stamped concrete totals by size",
            "<p>Sizing a stamped patio or driveway works the same arithmetic as plain concrete, just against a higher per-square-foot range.</p>"
            + table("Stamped concrete totals by size", ["Project size", "Area", f"Market range at {price(pk)}/sq ft"],
                    [["Small accent pad (10 × 10 ft)", "100 sq ft", "$800–$1,900"],
                     ["Seating area (12 × 12 ft)", "144 sq ft", "$1,150–$2,740"],
                     ["Patio extension (16 × 20 ft)", "320 sq ft", "$2,560–$6,080"],
                     ["Full back patio (20 × 20 ft)", "400 sq ft", "$3,200–$7,600"]],
                    f"Arithmetic on the Florida market range of {price(pk)} per square foot, {PRICE_DATE}; HomeGuide independently cites the same $3,200–$7,600 figure for a 20 × 20 ft stamped patio.")),
        sec("What moves a stamped concrete quote",
            "<p>Beyond the base per-square-foot tier, a handful of specifics push a stamped job up or down:</p>"
            + table("Stamped concrete cost drivers", ["Factor", "What it does to the price", "Florida detail"],
                    [["Pattern complexity", "A multi-stamp layout with hand-tooled joint lines takes longer than a single repeating mold", "Ashlar slate and wood-plank patterns need more hand-detailing at borders than a uniform cobble pattern"],
                     ["Color system", "Integral color alone costs less than integral plus an antiquing release", "Release powder residue needs to be pressure-washed off before sealing, adding a labor step"],
                     ["Sealer", "A film-forming sealer with slip-resistant grit costs more than a basic penetrating sealer", "Pool-deck and patio sealers in Florida typically need a slip additive; driveway sealers may not"],
                     ["Base and thickness", "Same spec as plain concrete; never a place to cut corners on a stamped job", "4 in. for patios, 4–6 in. for driveways, same control-joint spacing as plain concrete"],
                     ["Weather window", "A hot, dry afternoon shortens the stamping window before the surface firms up", "Crews often schedule stamped pours for early morning starts in warmer months to buy more working time"]],
                    "Drivers compiled from HomeGuide's stamped and concrete-patio cost guides.")),
        sec("Does stamped concrete need a different base than plain concrete?",
            f"<p>No, and this is where a low stamped bid most often cuts a corner that doesn't show up until the first rainy season. The base, thickness and control-joint spacing for a stamped slab follow the same rules as a plain one: 4 inches for a patio, 4 to 6 inches for a driveway, and joints cut every 8 to 12 feet at a quarter of the slab's depth regardless of what the surface looks like once it's finished ({src('nrmca-cip6', 'NRMCA CIP 6')}).</p>"
            "<p>Where stamped work does add a step is in sequencing. The crew has to finish the base, pour and float the slab, then stamp it before the concrete sets, all while the Florida sun works against the clock on a hot afternoon. That's a labor and timing cost, not a structural one, and it's the reason a bid that's unusually cheap on stamped work is worth asking about rather than simply accepting.</p>"),
        sec("Is stamped concrete pricing different in Orlando than in Sarasota?",
            f"<p>Published guides don't show a meaningful split between the two sides of the state. HomeGuide's stamped concrete tiers are national rather than city-specific, and the Florida driveway and patio pages that do break out Orlando and Tampa figures separately land inside the same {price(pk)} per square foot band once a stamped finish is applied ({src('homeguide-stamped', 'HomeGuide')}; {src('angi-driveway-orlando', 'Angi Orlando')}). "
            "A Lakewood Ranch pool deck and a Winter Garden patio in the same stamped tier should price within the same range; what actually shifts a number is pattern complexity, color count and how much of the surface gets stamped versus left plain, not the county the project sits in.</p>"),
        sec("Two stamped concrete budgets, worked through",
            "<p>Say you have a 240-square-foot section of an Oviedo patio planned for a single-pattern, single-color stamp along the back entry, with the rest of the patio left plain broom. The stamped section at a basic tier runs roughly $1,920 to $3,120, far less than stamping the entire 400-square-foot patio would.</p>"
            "<p>Say instead you have a 400-square-foot pool deck area near Bradenton where the whole surface is stamped in a two-color ashlar pattern with an antiquing release. At the mid-range tier that's roughly $5,200 to $7,600, and a slip-resistant sealer coat is worth budgeting as a separate line since pool-deck sealers carry different grit requirements than a driveway sealer.</p>"),
        sec("Keeping the price down without skipping the base",
            "<p>Stamped work has more places to trim cost than plain concrete does, because so much of the price lives in the decorative layer rather than the structure underneath:</p>"
            + ul(["Stamp only the visible, high-traffic zone, such as an entry walk or pool-deck border, and leave the rest of the area plain broom.",
                  "Choose a single-color, single-pattern basic tier instead of a layered multi-color design; the mold itself costs the same either way.",
                  "Ask about a stamped overlay if the goal is a new look on a slab that's structurally sound, rather than a full demolition and repour.",
                  "Pick a pattern with fewer hand-tooled border details, since straight-line joints take less finishing time than curved or radial layouts.",
                  "Never shrink the base depth or thickness to offset a decorative upgrade; that's the one line that has to stay the same as a plain concrete job regardless of finish."])),
        sec("What a stamped concrete quote should spell out",
            "<p>Because so much of the price is in the decorative process, ask for these specifics in writing before comparing bids:</p>"
            + ul(["Pattern name or mold, and which tier (basic, mid-range, high-end) it falls under",
                  "Color method: integral color alone, or integral plus a release powder or antiquing stain",
                  "Sealer type, number of coats, and whether a slip-resistant additive is included for a pool deck or patio",
                  "Slab thickness and base depth, which should match a plain concrete job of the same use",
                  f"Resealing timeline and cost, since stamped finishes need periodic resealing to keep the color from fading; see {post('stamped-concrete-maintenance-florida', 'stamped concrete maintenance in Florida')}"])),
        sec("Related reading",
            f"<p>{svc('stamped-concrete', 'Our stamped concrete page')} covers pattern options and the install process in full. If pavers are also on the table, {compare('stamped-concrete-vs-pavers', 'stamped concrete vs. pavers')} runs the cost and upkeep comparison side by side. "
            f"For a plain-finish baseline, see {svc('concrete-driveways', 'concrete driveways')} or {svc('concrete-patios', 'concrete patios')}; for a pool setting specifically, {svc('concrete-pool-decks', 'concrete pool decks')} and the {a('/pool-deck-cost/', 'pool deck cost guide')} cover the surface-by-surface pricing. "
            f"{post('stamped-concrete-patterns-and-colors', 'Stamped concrete patterns and colors that work in Florida')} is worth a look before settling on a mold.</p>"),
    ])
    faqs = [
        faq("How much does stamped concrete cost per square foot in Florida?",
            f"Stamped concrete runs {price(pk)} per square foot installed, with most jobs closer to {price(pk, True)}. The low end covers a single-pattern, single-color basic job; the high end covers multi-color, hand-tooled work, and a stamped driveway typically prices a bit higher than a stamped patio of the same tier."),
        faq("Why does stamped concrete cost more than plain concrete?",
            "The texturing has to happen in a narrow window right after the slab is poured, while it's still soft enough to take a mold impression but firm enough to hold the pattern. That compressed labor window, plus integral color, a release agent and a sealer coat, is what separates stamped pricing from plain broom concrete, not the base concrete itself."),
        faq("Does a stamped pool deck cost more than a stamped patio?",
            "Often a bit more, because pool-deck sealers typically need a slip-resistant additive that a patio sealer may not, and pool-deck slabs need slope built in toward drains. The stamping and coloring work itself is priced the same way regardless of setting."),
        faq("How often does stamped concrete need resealing, and does that show up in the quote?",
            "A sealer coat is usually included in the initial install price, but resealing on a schedule afterward is ongoing upkeep, not a one-time cost. Ask whether the first reseal is included or priced separately, since that's a common point of confusion between a new-install quote and a maintenance quote."),
        faq("Is stamped concrete cheaper than pavers for the same patio?",
            "Usually yes for a comparable pattern and finish, since stamped concrete pours as one continuous slab rather than individual set units. Pavers cost more up front but don't need resealing on the same schedule and can be lifted and reset for a spot repair, which the full comparison walks through."),
        faq("Can plain concrete be stamped later as an overlay?",
            "Sometimes, if the existing slab is structurally sound with no major cracking or settlement. A stamped overlay runs $7 to $15 per square foot, below the cost of demolishing and repouring, but it's a thinner decorative layer bonded to the old surface rather than a full-depth new slab.")]
    return page("/stamped-concrete-cost/", "price", "Stamped Concrete Cost in Florida (2026)",
                f"Stamped concrete cost in Florida as of {PRICE_DATE}: {price(pk)} per sq ft, basic-to-high-end tier pricing, and why stamped costs more than plain concrete.",
                "What Stamped Concrete Costs Over Plain Concrete in Florida",
                capsule(f"As of {PRICE_DATE}, stamped concrete in Florida runs {price(pk)} per square foot installed, closer to {price(pk, True)} for most jobs ({src('homeguide-stamped', 'HomeGuide')}). "
                        "A basic single-color pattern starts around $8 per square foot; multi-color, hand-tooled work runs $19 or more, roughly double the cost of plain broom concrete."),
                body, faqs=faqs,
                sources=["homeguide-stamped", "homeguide-concrete-patio", "homewyse-stamped", "nrmca-cip6", "angi-driveway-orlando"],
                crumbs=[("Cost guides", "/cost/")], crumb="Stamped concrete cost", service=K, form=True,
                hero_photo=pids[0] if pids else None, offer=offer(pk), eyebrow="Cost guide")


def pool_deck_cost():
    K = "concrete-pool-decks"
    pk = SERVICES[K]["price"]
    pids = for_service(K, 1)
    body = "".join([
        sec("How much does a pool deck cost in Florida?",
            f"<p>Pool deck pricing spreads wider than almost any other project here because the choices run from a coating sprayed over an existing slab to a full travertine rebuild. HomeGuide's material-by-material breakdown puts poured concrete at $5 to $15 per square foot, stamped concrete at $8 to $19, concrete pavers at $10 to $17 and natural stone at $16 to $35 "
            f"({src('homeguide-pool-deck', 'HomeGuide, Dec 2025')}). A Central Florida pool-resurfacing contractor's own published pricing lines up close to that for the lower tiers: acrylic or Kool Deck-style coatings at $3 to $6 per square foot and a spray-deck overlay at $4 to $8 ({src('poolmechanic-pooldeck-cfl', 'Pool Mechanic, Jul 2026')}). "
            "As of October 2026, the plain poured-concrete option sits at the lower end of that spread, with travertine and natural stone at the top.</p>"),
        sec("Pool deck surfaces compared, by size",
            "<p>Because a deck can be resurfaced, overlaid or fully rebuilt in several materials, the size table below runs the common 800 and 1,200 square-foot bands a Pool Mechanic guide for Central Florida uses, next to the arithmetic for a new poured-concrete, stamped or paver deck built to the Florida market ranges on this site.</p>"
            + table("Pool deck cost by material, 800 and 1,200 sq ft deck", ["Material", "Per sq ft", "800 sq ft total", "1,200 sq ft total"],
                    [["Acrylic / Kool Deck-style coating", "$3–$6", "$2,400–$7,200", "not published for this size"],
                     ["Spray deck / micro-topping overlay", "$4–$8", "$3,200–$9,600", "not published for this size"],
                     ["New poured concrete deck", "$5–$15", "$4,000–$12,000", "$6,000–$18,000"],
                     ["Stamped concrete deck", "$8–$19", "$6,400–$15,200", "$9,600–$22,800"],
                     ["Concrete pavers", "$10–$17", "$8,000–$13,600", "$12,000–$20,400"],
                     ["Travertine pavers", "$13–$30", "$10,400–$24,000", "$15,600–$36,000"]],
                    f"Coating and spray-deck totals from a Central Florida contractor's published 800–1,200 sq ft bands ({src('poolmechanic-pooldeck-cfl', 'Pool Mechanic')}); the other four rows are arithmetic on the Florida market ranges, {PRICE_DATE}. Removing an old deck adds roughly $5 per square foot on top of any row.")),
        sec("How much does a travertine pool deck cost?",
            f"<p>A travertine pool deck runs $13 to $30 per square foot installed, with most 400 to 1,000 square foot decks totaling $5,200 to $30,000 depending on size and stone grade ({src('homeguide-travertine', 'HomeGuide, Apr 2026')}). "
            f"A Florida contractor's own pricing puts a 1,000 square foot travertine pool deck at roughly $22,000 to $28,000, inside that national band but on the higher side, reflecting the cost of imported stone and more detailed cutting around curves and the pool coping ({src('craftpavers-fl-pricing', 'Craft Pavers, Jul 2026')}). "
            "Bullnose coping, the rounded edge piece that caps the pool's edge, typically runs $20 to $40 per linear foot on top of the deck price, and sealing travertine afterward adds $1 to $3 per square foot.</p>"),
        sec("How much does it cost to resurface a pool deck in Florida?",
            "<p>Resurfacing an old deck instead of tearing it out costs a fraction of a new pour, with the price scaling to how decorative the finish is. "
            f"HomeGuide's national resurfacing tiers run basic at $3 to $6 per square foot, decorative at $6 to $12, and a stamped resurfacing overlay at $7 to $20 ({src('homeguide-pool-deck-resurfacing', 'HomeGuide, Jul 2025')}). "
            "A Central Florida contractor quotes similar numbers for the region specifically: acrylic and Kool Deck-style coatings at $3 to $6 per square foot, and a thicker spray-deck or micro-topping overlay at $4 to $8, with an 800 to 1,200 square foot deck landing around $2,400 to $7,200 for the acrylic option and $3,200 to $9,600 for the spray-deck option.</p>"),
        sec("How much does it cost to put pavers over an existing pool deck?",
            f"<p>Installing pavers over an existing pool deck runs close to a new paver install, roughly {price('pool-deck-pavers')} per square foot, without the cost of fully demolishing the old slab first. "
            f"HomeGuide's broader paver-patio data puts pavers specifically laid around a pool at $12 to $25 per square foot, or $5,000 to $20,000 total depending on the deck's size ({src('homeguide-paver-patio', 'HomeGuide, Sep 2024')}), and a Central Florida pool-resurfacing contractor quotes concrete pavers over an existing slab at $8 to $15 per square foot installed ({src('poolmechanic-pooldeck-cfl', 'Pool Mechanic')}). "
            "The main thing an overlay-style paver install skips is the roughly $5 per square foot that full removal of the old deck would otherwise add, since the old slab stays in place as the base.</p>"),
        sec("What moves a pool deck quote",
            "<p>Beyond the base material choice, these line items separate bids on the same deck:</p>"
            + table("Pool deck cost drivers", ["Factor", "What it does to the price", "Florida detail"],
                    [["Removal of the old deck", "Adds roughly $5/sq ft when the existing surface comes out instead of being resurfaced or overlaid", "Resurfacing or a paver overlay skips this cost by building on top of the old slab"],
                     ["Coping and edge detail", "Bullnose or specialty coping runs $20–$40 per linear foot on top of the field", "Pool coping has to meet the pool's edge cleanly, which is cut and fitted work, not a straight run"],
                     ["Slope and drainage", "A deck has to pitch away from the pool toward drains or the yard, which takes more careful grading than a flat patio", "Standing water on a Florida pool deck after a summer storm is usually a sign the slope was never set correctly"],
                     ["Access through a screen enclosure", "A pool cage narrows how equipment reaches the work area", "Many Florida pools sit inside a screened enclosure, which limits truck and pump access to buggies or hand tools"],
                     ["Material", "The widest swing on this page: $3/sq ft coating to $30/sq ft travertine", "Travertine and shell stone stay noticeably cooler underfoot than dark concrete or pavers in direct sun, a common reason coastal Sarasota and Manatee homeowners choose stone despite the higher price"]],
                    "Drivers compiled from HomeGuide, Pool Mechanic and the Florida building facts cited on this page.")),
        sec("Two pool deck budgets, worked through",
            "<p>Say you have an 800-square-foot Kool Deck-style deck near Lake Nona that's faded and chalky but structurally sound, with no cracks that need section replacement. Resurfacing with a fresh acrylic coating runs roughly $2,400 to $4,800, far less than tearing the deck out and starting over.</p>"
            "<p>Say instead you have a 1,000-square-foot original pool deck on a coastal Sarasota or Manatee lot where salt air has been rough on the existing surface, and the plan is a full switch to travertine. At published Florida contractor pricing, that's roughly $22,000 to $28,000 for the field, plus bullnose coping around the pool's edge at $20 to $40 per linear foot and a sealer coat after installation.</p>"),
        sec("Saving money without cutting the base or the slope",
            "<p>A pool deck's base and its slope toward the drains are not the places to economize; a flat or under-built deck holds water and that water finds its way into cracks faster than a dry deck ever would. Real savings sit elsewhere:</p>"
            + ul(["Resurface or overlay a sound old deck instead of a full tear-out when the slab underneath is structurally fine; the savings over full replacement runs into thousands of dollars.",
                  "Limit a pricier material like travertine or stamped concrete to the areas closest to the pool and entry points, and use plain concrete or a basic coating on the back stretch few people walk.",
                  "Ask whether a localized section repair is possible for a single cracked or stained area rather than resurfacing the entire deck.",
                  "Choose a standard bullnose coping profile over a custom cut shape, since specialty coping adds cost per linear foot on top of the field price.",
                  "Pair the deck project with any other hardscape work planned for the same year, since sharing a mobilization across two jobs trims the setup cost on both."])),
        sec("What a pool deck quote should include",
            "<p>Pool decks have more moving parts than a driveway or patio quote, so ask for these specifics before comparing bids:</p>"
            + ul(["Whether the job is a full tear-out and new pour, a resurfacing overlay, or pavers laid over the existing slab",
                  "Slope direction and how it's verified before the final surface goes down",
                  "Coping material, profile and linear footage, priced separately from the field",
                  "Expansion joint placement at the coping, which keeps the deck from binding against the pool shell as temperatures change",
                  "Sealer type and whether a slip-resistant additive is included, since a wet pool deck needs more traction than a dry patio"])),
        sec("Related reading",
            f"<p>{svc('concrete-pool-decks', 'Our concrete pool decks page')} and {svc('pool-deck-pavers', 'pool deck pavers page')} cover the install process for each surface. For the decision between materials, {compare('pavers-vs-concrete-pool-deck', 'pavers vs. concrete for a pool deck')}, {compare('cool-deck-vs-pavers-vs-travertine', 'Kool Deck vs. pavers vs. travertine')} and {compare('travertine-vs-concrete-pavers', 'travertine vs. concrete pavers')} go through comfort, upkeep and lifespan side by side. "
            f"{post('pool-deck-ideas-florida', 'Pool deck ideas for Florida homes')} and {post('saltwater-pools-and-coastal-salt-air-hardscape', 'protecting a deck near saltwater and salt air')} round out the planning, and the {a('/cost/', 'cost guide hub')} has every other service's market range in one place.</p>"),
    ])
    faqs = [
        faq("How much does a travertine pool deck cost?",
            "Travertine pool decks run $13 to $30 per square foot installed, and a 1,000-square-foot deck in published Florida contractor pricing runs roughly $22,000 to $28,000. Bullnose coping around the pool's edge adds $20 to $40 per linear foot on top of that field price."),
        faq("How much does it cost to resurface a pool deck in Florida?",
            "A basic acrylic or Kool Deck-style resurfacing runs $3 to $6 per square foot, and a decorative or spray-deck overlay runs $4 to $12. An 800-square-foot deck lands around $2,400 to $7,200 for the basic option, well under the cost of a full tear-out and new pour."),
        faq("How much does it cost to put pavers over an existing pool deck?",
            "Pavers installed over an existing deck run roughly $8 to $17 per square foot depending on the material, close to a new paver install but without the roughly $5-per-square-foot cost of fully removing the old slab first, since the old deck stays in place as the base."),
        faq("Does removing an old pool deck add much to the price?",
            "Yes, roughly $5 per square foot on top of whatever new surface goes in. That's one reason resurfacing or a paver overlay, both of which build on the existing slab, run well under the cost of a full tear-out and new pour for a deck that's still structurally sound."),
        faq("Is a concrete pool deck cheaper than a paver pool deck?",
            "Usually, yes. A new poured concrete deck runs $5 to $15 per square foot against $10 to $17 for concrete pavers and well more for travertine. Pavers and stone cost more up front but offer easier spot repairs and, for natural stone, a cooler surface underfoot in direct sun."),
        faq("Does bullnose coping cost extra on top of the deck price?",
            "Yes, coping is priced separately from the field. Bullnose or specialty coping profiles run $20 to $40 per linear foot around the pool's edge, on top of whatever the deck surface itself costs per square foot.")]
    return page("/pool-deck-cost/", "price", "Pool Deck Cost in Florida: Concrete, Pavers & Travertine",
                f"Pool deck cost in Florida as of {PRICE_DATE}: Kool Deck resurfacing $3-$6/sq ft, new concrete $5-$15, pavers $10-$17, travertine $13-$30 per sq ft.",
                "What a Pool Deck Costs in Florida, Material by Material",
                capsule(f"As of {PRICE_DATE}, Florida pool deck pricing runs from about $3 per square foot for an acrylic or Kool Deck-style resurfacing coat up to $30 per square foot for travertine pavers ({src('homeguide-pool-deck', 'HomeGuide')}). "
                        "A new 800 square foot poured-concrete deck runs roughly $4,000 to $12,000; a travertine deck of the same size runs $10,400 to $24,000."),
                body, faqs=faqs,
                sources=["homeguide-pool-deck", "homeguide-pool-deck-resurfacing", "homeguide-travertine", "homeguide-paver-patio", "poolmechanic-pooldeck-cfl", "craftpavers-fl-pricing"],
                crumbs=[("Cost guides", "/cost/")], crumb="Pool deck cost", service=K, form=True,
                hero_photo=pids[0] if pids else None, offer=offer(pk), eyebrow="Cost guide")


def get_pages():
    return [driveway_cost(), patio_cost(), stamped_cost(), pool_deck_cost()]
