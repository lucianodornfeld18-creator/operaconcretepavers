# -*- coding: utf-8 -*-
"""Blog posts, group l (final group, 2 posts): artificial turf water savings and payback, and a five-material
paver buyer's guide (concrete, clay brick, travertine, porcelain, shellstone). Money/ROI and material-selection
angles that the service, cost and compare pages don't already cover; linked, not repeated."""
from _helpers import page, capsule, sec, table, faq, ul, steps, a, svc, post, compare, src, ext, price, per, photo
from _photos import for_service


def p_artificial_turf_water_savings_florida():
    pids = for_service("artificial-turf", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("How much water does a typical Florida lawn need?",
            "<p>A St. Augustinegrass lawn, the default sod in both service areas, needs about 0.5 to 0.75 inch of water a week once it's established, under University of Florida guidance "
            f"({ext('https://ask.ifas.ufl.edu/publication/AE436', 'UF/IFAS AE436')}). Converted to volume with the standard irrigation math, one inch of water over 1,000 sq ft equals about 623 gallons, so that lawn uses roughly 310 to 470 gallons a week for every 1,000 sq ft it covers. "
            f"{svc('artificial-turf', 'An artificial turf lawn')} built to Florida's 2026 standard uses none of that, since in-ground irrigation on turf is barred outright.</p>"
            + table("Sod water use at the UF/IFAS recommended rate", ["Lawn size", "Gallons a week", "Gallons a year, upper-bound estimate"],
                    [["1,000 sq ft", "310–470", "16,200–24,300"],
                     ["1,500 sq ft", "470–700", "24,300–36,400"],
                     ["2,000 sq ft", "620–935", "32,400–48,600"]],
                    "The yearly figure assumes the full recommended rate is applied every week of the year, which overstates real use; rainfall covers part of that need, especially from late May into mid-October.")
            + "<p>Those are upper-bound numbers, not a bill anyone actually pays, since both service areas also sit under watering-day schedules that cap how often a zone can run in the first place, separate from how much a lawn would ideally drink.</p>"
            + (photo(pid, "A bright green artificial turf lawn fills a front yard beside a covered patio and outdoor seating area.") if pid else "")),
        sec("How much does turf use instead?",
            f"<p>Zero, for the irrigation zone itself. Florida's turf rule, Rule 62-308.100, prohibits watering synthetic turf with an in-ground system, full stop, and a city or county can require the heads inside that zone to be capped below grade "
            f"({src('rule62-308-100-text', 'Rule 62-308.100 text')}). An occasional hose rinse to settle infill or cool the surface on a hot day is allowed, since a hose isn't the in-ground system the rule restricts, but it's nothing close to a weekly watering zone. "
            f"{a('/artificial-turf-cost/', 'Our artificial turf cost guide')} covers the installed price by size; this page is about what happens to the water bill afterward, not the upfront number. "
            f"{compare('artificial-turf-vs-sod', 'Turf vs. sod side by side')} covers the fuller feature comparison if that's the decision still being made.</p>"),
        sec("How much could switching save on a water bill in Greater Orlando?",
            "<p>Say you have a 2,000 sq ft lawn at a 2026-built Oviedo home on OUC water. At the UF/IFAS rate that lawn uses an estimated 32,400 to 48,600 gallons a year if watered at the full recommended amount every week, which lands mostly in OUC's $2.30-per-1,000-gallon tier once an average household's indoor baseline has already filled the cheaper first tiers "
            f"({ext('https://www.ouc.com/wp-content/uploads/2025/08/2025_09-OUC-Electric-Water-Rate-Orlando.pdf', 'OUC residential water rates, effective Oct. 1, 2025')}). That works out to roughly $75 to $110 a year in irrigation charges, before accounting for the rainy-season weeks that need little or no supplemental water at all. A larger lot pushing total household use into OUC's $8.00 or $15.00 tiers would see a bigger number, since those marginal gallons cost far more than the mid tier does.</p>"),
        sec("What does that look like on the Sarasota side?",
            "<p>Say instead you have a 1,800 sq ft lawn at a Bradenton home on Manatee County water. The same UF/IFAS rate puts that lawn at an estimated 29,200 to 43,700 gallons a year, landing mostly in Manatee's $3.89-per-1,000-gallon tier "
            f"({ext('https://www.mymanatee.org/connect/news-and-information/news-and-information/article-detail/utilities-water-division-blog/2026/05/07/rates-for-water-and-sewer---effective-june-1--2026', 'Manatee County water and sewer rates, effective June 1, 2026')}). That's roughly $115 to $170 a year in irrigation charges, somewhat higher than the Orlando example, since Manatee's per-gallon rate runs higher than OUC's mid tier. Sarasota, Manatee and several neighboring counties are also under SWFWMD's Modified Phase III order through March 2027, limiting watering to one day a week, which already trims real-world use below what either of these upper-bound estimates shows.</p>"),
        sec("How long would turf take to pay for itself through water savings alone?",
            f"<p>At current Florida market pricing, installed turf runs {price('artificial-turf')} per {per('artificial-turf')}, typically {price('artificial-turf', True)}. For the 2,000 sq ft Oviedo lawn above, that's roughly $24,000 to $36,000 installed against an estimated $75 to $110 a year saved on water. Divide one by the other and the payback period stretches past two centuries, not the handful of years a homeowner might assume from how often turf gets pitched as a water-saving upgrade. "
            "The Bradenton example pencils out a little faster thanks to Manatee's higher rate, but it still lands well over a century. Municipal water is simply cheap in both service areas relative to what a full turf conversion costs, which is worth knowing before water savings alone is the reason to convert a whole yard.</p>"),
        sec("Does a private well or a separate irrigation meter change this?",
            "<p>Yes, substantially, and it's worth checking before running any of the math above against a specific address. Many Florida subdivisions irrigate from a private well or a dedicated irrigation meter rather than the same metered line that serves the house, "
            f"and a well draws groundwater with no per-gallon municipal charge at all ({ext('https://tampa.gov/water/conservation/water-smart-lawns/dedicated-irrigation-meter-%E2%80%93-yes-or-no', 'City of Tampa, dedicated irrigation meter')}). A home on a well pays essentially nothing per gallon for lawn irrigation today, so switching that specific lawn to turf saves closer to zero dollars on a water bill, whatever it saves in mowing, fertilizer and a sprinkler system's own upkeep. A separate potable irrigation meter changes the math differently: it usually still bills at the same per-gallon rate as the indoor line but skips the sewer charge, since that water never enters the drain. "
            f"{post('rust-and-irrigation-stains-on-concrete-pavers', 'Our post on well and reclaimed water stains')} covers a related side effect of that same well or reclaimed setup, the orange stains it can leave on a driveway.</p>"),
        sec("Is there a rebate for switching from sod to turf?",
            "<p>Not one we can confirm as of October 2026. Some Florida utilities fund Florida-friendly landscaping rebates aimed at reducing turf area and irrigated square footage generally, and whether a specific program pays for synthetic turf specifically, excludes it, or funds only native and drought-tolerant plants varies by utility and changes from year to year. Check directly with the local water provider before counting on a rebate to offset any part of the installed cost.</p>"),
        sec("What actually makes switching worth it, if not the water bill?",
            f"<p>Mowing, edging, fertilizing and pest treatment on a St. Augustine lawn add up to real recurring time and cost that the water-bill math above doesn't capture at all, and those costs keep running whether or not the district is under a watering restriction that week. A lawn that's repeatedly thinned out or died back under the current once-a-week schedule is also a sunk cost worth weighing: resodding the same area every year or two has its own price tag that a converted lawn doesn't carry again. "
            f"{post('artificial-turf-heat-in-florida', 'How hot artificial turf actually gets in Florida sun')} is the other side of that trade worth reading before deciding, since turf's upside on water and labor comes with a real downside on bare feet in July.</p>"),
    ])
    faqs = [faq("Does turf save the same amount of water in the Orlando area as it does around Sarasota?",
                "The water saved per square foot is the same either way, since Florida's turf rule applies statewide and a lawn's irrigation need doesn't change much between the two service areas. What differs is the dollar figure: each utility prices water differently, and SWFWMD's current restrictions on the Sarasota side are tighter than SJRWMD's in most of the Orlando area, which changes how much a sod lawn was actually using before the switch."),
            faq("Do you need to keep an irrigation system if you convert the whole yard to turf?",
                "The zone that served the converted area gets capped below grade or removed, since the state rule bars using it to water turf. If beds, trees or a strip of remaining sod still need water, that part of the system usually stays in place and keeps running on its own zone."),
            faq("Does converting only part of a yard to turf still lower the water bill?",
                "Yes, proportionally. A partial conversion, say a side yard or a strip under a shade tree where sod never grows well anyway, cuts the water that specific area used to need while leaving the rest of the irrigation system and bill unchanged."),
            faq("Does a private well change whether turf is worth it financially?",
                "It changes the water-bill math specifically, since well water carries no per-gallon municipal charge, so the dollar savings from switching shrink toward zero. It doesn't change the time saved on mowing, fertilizing and pest control, which a well doesn't offset."),
            faq("Are turf's water savings spread evenly across the year?",
                "No. Savings skew toward the cooler, drier months, roughly November through May, since a sod lawn often needs little or no supplemental water during the wet season from late May into October. A turf lawn's advantage is largest exactly when watering restrictions bite hardest.")]
    return page("/blog/artificial-turf-water-savings-florida/", "post",
                "Artificial Turf Water Savings in Florida: The Real Math",
                "Artificial turf uses zero in-ground irrigation under Florida turf rule 62-308.100, but at October 2026 water rates the bill payback alone runs into decades.",
                "How Much Water and Money Does Artificial Turf Save in Florida?",
                capsule("Switching a Florida lawn to artificial turf eliminates its irrigation use entirely, since the state's 2026 turf rule bars in-ground watering on turf, but at October 2026 municipal rates of roughly $1 to $4 per 1,000 gallons, a typical lawn's water-bill savings alone rarely clear a few hundred dollars a year in Greater Orlando or Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["rule62-308-100-text", "sjrwmd-watering", "swfwmd-restrictions", "manatee-phase3", "homeguide-artificial-grass", "angi-turf-orlando",
                         ("UF/IFAS AE436, Summary of UF/IFAS Turf and Landscape Irrigation Recommendations", "https://ask.ifas.ufl.edu/publication/AE436"),
                         ("OUC residential water rates, effective Oct. 1, 2025", "https://www.ouc.com/wp-content/uploads/2025/08/2025_09-OUC-Electric-Water-Rate-Orlando.pdf"),
                         ("Manatee County water and sewer rates, effective June 1, 2026", "https://www.mymanatee.org/connect/news-and-information/news-and-information/article-detail/utilities-water-division-blog/2026/05/07/rates-for-water-and-sewer---effective-june-1--2026"),
                         ("City of Tampa, dedicated irrigation meter", "https://tampa.gov/water/conservation/water-smart-lawns/dedicated-irrigation-meter-%E2%80%93-yes-or-no")],
                related=[("/artificial-turf/", "Artificial turf installation"), ("/artificial-turf-cost/", "Artificial turf cost guide"),
                         ("/compare/artificial-turf-vs-sod/", "Artificial turf vs. sod"), ("/blog/how-to-clean-artificial-turf/", "Cleaning and maintaining turf"),
                         ("/blog/artificial-turf-heat-in-florida/", "How hot turf gets in Florida")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf", image=pid, form=False)


def p_best_pavers_for_florida():
    pids = for_service("paver-driveways", 1)
    pid = pids[0] if pids else None
    body = "".join([
        sec("What are the five paver materials Florida homeowners choose from?",
            f"<p>Most Florida paver projects land on one of five materials: concrete, clay brick, travertine, porcelain or shellstone. All five sit on the same compacted aggregate base and bedding sand that any {svc('paver-driveways', 'paver driveway')} or {svc('paver-patios', 'paver patio')} needs; what changes between them is cost, how they feel underfoot in direct sun, how much upkeep they ask for, and how often a specific community's design guidelines name one by name. "
            f"None of the five is simply better across the board, which is why this page compares them side by side instead of picking a winner. {svc('pool-deck-pavers', 'Our pool deck pavers page')} and the cost guides linked below cover installation and pricing for each use once a material is picked.</p>"
            + (photo(pid, "Paver driveways line a sunlit Florida street of Mediterranean-style homes with manicured lawns and palm trees.") if pid else "")),
        sec("Which paver material costs the least installed?",
            "<p>Concrete pavers cost the least per square foot in current Florida pricing, with clay brick, porcelain and travertine climbing from there mostly on material cost rather than labor. Shellstone sits in a wide band of its own, priced by the piece and the finish more than by a single market-wide figure.</p>"
            + table("Paver material cost, installed, Florida market", ["Material", "Installed range", "What it buys"],
                    [["Concrete pavers", "$10–$20/sq ft", "Widest color and shape selection; a cracked or stained unit lifts and resets without disturbing the rest of the field"],
                     ["Clay brick", "$12–$22/sq ft ($25–$50+ for reclaimed or specialty units)", "Color fired through the whole unit, so it never fades the way a pigmented surface can"],
                     ["Shellstone", "roughly $12–$35/sq ft, by one Florida supplier's current pricing", "Porous, fossil-textured surface; thickness options from thin tile to heavy pavers"],
                     ["Porcelain", "$15–$32/sq ft", "The lowest water absorption of the five, which means the least staining risk over time"],
                     ["Travertine", "$13–$45/sq ft overall, $13–$30 on a pool deck specifically", "Natural stone look; the material most often named by name in upscale community design guidelines"]],
                    f"{src('angi-paver-driveway', 'Angi')}; {src('craftpavers-fl-pricing', 'Craft Pavers')}; {src('homeguide-driveway-pavers', 'HomeGuide')}; {src('homeguide-travertine', 'HomeGuide, travertine')}; "
                    f"{ext('https://citadelstone.us/shellstone-pavers-in-florida/', 'Citadel Stone, shellstone pavers')}. Figures are Florida market ranges, not quotes for a specific project.")),
        sec("Which paver stays coolest underfoot in Florida sun?",
            f"<p>Travertine and shellstone generally read cooler to bare feet in direct sun than a dark concrete paver, since both are lighter-colored, more reflective natural stone rather than a manufactured unit with a darker pigment option in the lineup. That's a real factor worth weighing around a pool specifically, but it isn't the whole story: a light-colored concrete paver or a light porcelain finish narrows the gap considerably, and color within a material line often matters as much as which material it is. "
            f"{post('how-hot-do-pool-decks-get-florida', 'Our full comparison of pool deck surface temperatures')} covers the measured side of this question in more depth than fits here.</p>"),
        sec("Which paver needs the least upkeep?",
            f"<p>Porcelain and clay brick ask for the least routine attention, for different reasons. Porcelain's water absorption runs very low by the industry tile standard, so it resists staining without needing a sealer on the schedule a porous stone does; clay brick's color is fired through the entire unit, so there's no surface pigment that needs protecting in the first place. Concrete pavers fall in the middle, since sealing is optional rather than required, and joint sand still tops off over time regardless of sealer. "
            f"Travertine and shellstone are the two that most reward a sealing routine, since both are porous natural stone that can pick up staining from pool chemicals, sunscreen or hard water faster when left bare. {svc('paver-sealing', 'Our paver sealing service')} covers that upkeep across all five materials, not just concrete.</p>"),
        sec("Which material fits a driveway, a patio or a pool deck best?",
            "<p>Load is the deciding factor for a driveway; look and feel underfoot matter more for a patio or pool deck. Concrete and clay brick dominate Florida driveways because both are made in vehicle-rated thicknesses at a lower cost than the alternatives; porcelain and shellstone driveway installs exist but use a thicker, specifically rated unit rather than the thinner tile made for a patio, and cost more per square foot to get there. Around a pool, travertine, shellstone, porcelain and concrete all show up regularly; clay brick is the least common of the five there, mostly on cost and because its fired finish isn't marketed the way the other four are for pool-deck slip resistance specifically.</p>"
            + table("Where each material is typically used", ["Material", "Driveway", "Patio", "Pool deck"],
                    [["Concrete pavers", "Common, vehicle-rated units available", "Common", "Common"],
                     ["Clay brick", "Common where a vehicle-rated unit is specified", "Common", "Uncommon"],
                     ["Shellstone", "Possible, with a thicker rated unit", "Common", "Common"],
                     ["Porcelain", "Possible, with a thicker rated unit", "Common", "Common"],
                     ["Travertine", "Less common; mostly cost-driven", "Common", "Very common"]])),
        sec("What is shellstone, and is it the same thing as Florida coquina?",
            f"<p>No, and the two get mixed up often enough that it's worth untangling. Coquina is the soft, shell-fragment limestone quarried on Anastasia Island near St. Augustine and famously used to build the 17th-century walls of the Castillo de San Marcos; it's a loose or roughly cut stone, not a manufactured paving unit "
            f"({ext('https://www.nps.gov/casa/learn/historyculture/coquina-the-rock-that-saved-st-augustine.htm', 'National Park Service, Castillo de San Marcos')}). Shellstone pavers sold today are a different product: cut, fairly uniform units with a fossil-shell texture, often quarried overseas rather than scooped from a Florida beach, and set in a compacted base exactly like any other paver "
            f"({ext('https://citadelstone.us/shellstone-pavers-in-florida/', 'Citadel Stone, shellstone pavers')}). The name overlaps with Florida's own coquina history, but the material in a shellstone paver and the stone in a 300-year-old fort wall usually aren't from the same place.</p>"),
        sec("How do you decide between the five?",
            "<p>Start with the surface, not the material, since load and exposure narrow the field before budget or looks do.</p>"
            + steps([("Confirm the load.", "A driveway needs a vehicle-rated unit in whichever material is chosen; a patio or walkway doesn't, which opens up thinner, often cheaper options in the same material."),
                     ("Set a budget per square foot.", "Concrete anchors the low end and travertine the high end, with clay brick, shellstone and porcelain filling the range between."),
                     ("Decide how much sealing you want to commit to.", "Porcelain and clay brick ask the least; travertine and shellstone reward a watched resealing schedule the most."),
                     ("Check the HOA's design guidelines before ordering.", "Some communities name a specific material or an approved color list for pool decks and driveways alike, which can settle the decision before cost or looks come into it.")])
            + "<p>Say you have a 1,200 sq ft pool deck going in at a 2026-built Parrish home. Illustrative only: concrete pavers run roughly $14,400 to $36,000 at current Florida pricing, travertine runs $15,600 to $36,000 on a pool deck specifically, porcelain runs $18,000 to $38,400, and shellstone, going by the one Florida supplier's pricing available, runs roughly $14,400 to $42,000. "
            f"At that scale the ranges overlap more than the sticker price alone suggests, which is why look, feel underfoot and upkeep usually settle the choice once a rough budget has already ruled a few options in or out. {post('why-pavers-sink-in-florida', 'Why pavers sink in Florida')} and {post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for a new driveway or pool deck')} cover two questions worth answering before any of the five gets ordered.</p>"),
    ])
    faqs = [faq("Can different paver materials be mixed in the same project?",
                "Yes, and it's a common way to get a premium look without paying premium prices across the whole surface. A frequent pairing is a travertine or shellstone coping band at a pool's edge, where feel underfoot matters most, with a less expensive concrete paver filling the rest of the deck farther from the water."),
            faq("Does the base change depending on which paver material is chosen?",
                "The base depth rules don't change by material: a driveway still needs roughly 6 inches of compacted aggregate on well-drained soil and a patio needs roughly 4, regardless of what sits on top. What changes is the paver's own thickness, since a vehicle-rated unit runs thicker than one made for foot traffic in every material on this list."),
            faq("Which paver material do Florida HOAs approve most often?",
                f"Concrete pavers are accepted almost everywhere, since they're the default in most community design guidelines. Travertine and, less often, shellstone get named specifically in higher-end communities' pool-deck standards; porcelain and clay brick show up less often by name, mainly because many declarations were written before either was widely used locally. {post('hoa-approval-for-pavers-and-concrete', 'Our HOA approval guide')} covers how that review typically works."),
            faq("Is shellstone the same thing as the loose shell driveways seen around St. Augustine?",
                "No. Those are coquina, a soft Florida limestone used loose or in roughly cut blocks, famous as the building stone of the Castillo de San Marcos. Shellstone pavers are a manufactured paving product, cut into fairly uniform units and set in a compacted base, even though both materials get their texture from ancient shell fragments."),
            faq("Can porcelain or shellstone be used on a driveway, not just a patio or pool deck?",
                "Yes, but the unit needs to be rated for vehicle loads, which means a thicker product than the tile made for a patio. It's a less common driveway choice than concrete or clay brick mainly on cost, not because the material can't handle a car's weight when it's specified correctly.")]
    return page("/blog/best-pavers-for-florida/", "post",
                "Best Pavers for Florida: 5 Materials Compared",
                "Concrete, clay brick, travertine, porcelain and shellstone pavers compared for Florida driveways, patios and pool decks, with cost ranges as of October 2026.",
                "What Are the Best Pavers for Florida Homes? Concrete, Clay, Travertine, Porcelain and Shellstone",
                capsule("Florida homeowners choose among five paver materials: concrete, clay brick, travertine, porcelain and shellstone, ranging from about $10 to $45 per square foot installed as of October 2026. Concrete costs least and comes in the most colors; travertine and shellstone stay cooler underfoot in direct sun; porcelain resists staining best. The right one depends on the surface and the budget."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts5", "angi-paver-driveway", "craftpavers-fl-pricing", "homeguide-driveway-pavers", "homeguide-travertine", "fs720-3035",
                         ("Citadel Stone, shellstone pavers in Florida", "https://citadelstone.us/shellstone-pavers-in-florida/"),
                         ("National Park Service, Castillo de San Marcos — coquina", "https://www.nps.gov/casa/learn/historyculture/coquina-the-rock-that-saved-st-augustine.htm")],
                related=[("/paver-driveways/", "Paver driveways"), ("/pool-deck-pavers/", "Pool deck pavers"),
                         ("/compare/travertine-vs-concrete-pavers/", "Travertine vs. concrete pavers"), ("/compare/porcelain-vs-travertine-pavers/", "Porcelain vs. travertine pavers"),
                         ("/blog/how-hot-do-pool-decks-get-florida/", "How hot pool decks get in Florida")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-driveways", image=pid, form=False)


def get_pages():
    return [p_artificial_turf_water_savings_florida(), p_best_pavers_for_florida()]
