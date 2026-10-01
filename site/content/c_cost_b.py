# -*- coding: utf-8 -*-
"""Cost guides: concrete slabs, concrete walkways/sidewalks, concrete repair & resurfacing, paver driveways."""
from _helpers import (page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext,
                       price, per, tel, contact, photo, offer)
from _photos import for_service

CRUMBS = [("Cost guides", "/cost/")]


# ---------------------------------------------------------------- concrete slab cost
def slab_cost():
    K, PK = "concrete-slabs", "concrete-slab"
    pids = for_service(K, 2)
    sizes = [["10 × 10 ft pad", "100", "$400–$1,000", "$600–$800"],
             ["12 × 12 ft pad", "144", "$576–$1,440", "$864–$1,152"],
             ["12 × 16 ft pad", "192", "$768–$1,920", "$1,152–$1,536"],
             ["20 × 20 ft slab", "400", "$1,600–$4,000", "$2,400–$3,200"],
             ["24 × 24 ft garage floor", "576", "$2,304–$5,760", "$3,456–$4,608"],
             ["30 × 30 ft slab", "900", "$3,600–$9,000", "$5,400–$7,200"]]
    body = "".join([
        sec("What does a concrete slab cost in Florida?",
            f"<p>As of October 2026, a concrete slab runs {price(PK)} per {per(PK)} across the Florida market data we track, with most jobs landing nearer {price(PK, True)}. "
            f"That compares with a wider {src('homeguide-concrete-slab', 'national $6–$12 per sq ft')} figure, since published Florida city data tends to sit below the national average on smaller flatwork, and with Orlando-specific pricing of $4 to $8 per square foot averaging $5,476 for a typical project "
            f"({src('angi-slab-orlando', 'Angi Orlando, Apr 2026')}). A slab's price depends far more on its thickness, reinforcement and base than on the square footage alone, which is why two pads of the same size can land at opposite ends of the range.</p>"
            + (photo(pids[0], "Freshly poured concrete slab with cut control joints near a garage.") if pids else "")),
        sec("Concrete slab cost by size", "<p>These totals multiply the Florida market range above across common pad sizes, from a small generator footing to a two-car garage floor. They don't include demolition of anything that was there before, or the cost of a permit where one applies.</p>"
            + table(f"Concrete slab totals by size, {price(PK)} per sq ft", ["Size", "Sq ft", "Market range", "Typical"], sizes,
                    f"Arithmetic on the {price(PK)} and {price(PK, True)} per sq ft figures above. For reference, Angi's Orlando data prices a 10×10 pad at about $610 and a 30×30 slab at about $5,500 ({src('angi-slab-orlando', 'Angi Orlando')}).")),
        sec("Cost by thickness, mix and reinforcement",
            "<p>Thickness and mix design move a slab's price more than almost anything else, since a thicker pour needs more concrete and, often, steel. HomeGuide's national data breaks the per-square-foot cost out by depth, and Angi's Orlando page breaks it out by mix instead; both describe the same underlying driver, how much material and reinforcement goes into the pour.</p>"
            + table("Slab cost by thickness (national) and by mix (Orlando)", ["Spec", "Range", "Typical use"],
                    [["2 in thick", "$4–$6/sq ft", "Below code for most accessory structures; rarely specified alone"],
                     ["4 in thick, standard mix", "$6/sq ft (Orlando)", "Shed, generator pad, patio-adjacent slab"],
                     ["4 in thick, rebar-reinforced", "$7/sq ft (Orlando)", "Garage floor, parking pad, higher point loads"],
                     ["6 in thick", "$8–$10/sq ft", "RV pad, boat trailer parking, equipment pad"],
                     ["High-strength mix", "$8/sq ft (Orlando)", "Heavier equipment or vehicle loads at standard thickness"],
                     ["Fiber-mesh reinforced", "$10/sq ft (Orlando)", "Crack-control alternative to welded wire mesh"],
                     ["8 in thick", "$10–$12/sq ft", "Heavy commercial or industrial-grade loads, uncommon residentially"]],
                    f"{src('homeguide-concrete-slab', 'HomeGuide, concrete slab cost')}; {src('angi-slab-orlando', 'Angi Orlando, concrete slab cost')}.")
            + "<p>Most residential accessory pads, shed floors, generator footings, parking pads, land on the 4-inch, standard or rebar-reinforced lines. Going to 6 inches only makes sense where the pad actually carries truck, RV or boat-trailer weight; paying for it on a pad that will only ever hold a storage shed adds cost without adding anything the shed needs.</p>"),
        sec("What moves a slab quote up or down",
            "<p>Beyond thickness and mix, five factors routinely separate a low bid from a high one on the same footprint.</p>"
            + table("What changes a slab quote", ["Factor", "Why it matters in Florida", "Typical effect"],
                    [["Removing what's there now", "An old pad, a tree stump or a patch of dead sod all need clearing first", "Concrete removal runs $3–$8/sq ft including haul-off; a 10×10 slab removal is $300–$800 (HomeGuide)"],
                     ["Base compaction", "Flatwoods soils hold a seasonal water table within about 18 inches of the surface across much of both service areas; loose fill left uncompacted settles under the slab within a year or two", "Adds labor and time, not usually a separate line item on a small pad"],
                     ["Access for the truck", "A backyard pad with no gate wide enough for a chute means pumping or wheelbarrowing concrete in by hand", "Pump trucks run $150–$600 per pour in Polk County contractor pricing"],
                     ["Minimum job charge", "Forming, mobilizing a crew and ordering a short load cost nearly the same whether the pad is 60 sq ft or 600", "Small pads carry a higher cost per sq ft than a large one at the same spec"],
                     ["Permit filing", "Whether the pad needs a permit, and who files it, changes the paperwork cost even when the concrete itself doesn't change", "See the permit section below"]],
                    f"{src('homeguide-concrete-removal', 'HomeGuide, concrete removal')}; {src('lakeland-readymix', 'Lakeland Concrete Contractors, ready-mix pricing')}.")),
        sec("Ready-mix concrete by the cubic yard",
            f"<p>Most slab quotes are priced per square foot, but the material itself is bought by the cubic yard, and that number is worth knowing when a bid looks unusually high or low. Orlando-area ready-mix runs $120 to $170 per cubic yard for all-purpose mix and $160 to $215 for high-strength, with the slab-specific Angi page citing about $110 per yard "
            f"({src('angi-slab-orlando', 'Angi Orlando')}; {src('angi-driveway-orlando', 'Angi Orlando, driveway')}). Lakeland and Polk County contractor pricing puts a planning average of $145 per yard on top of a $130–$160 range, plus a $5–$15 fuel surcharge, a $50–$150 flat fee on loads under about 5 yards, and $8–$15 per yard for a hot-weather retarder in summer "
            f"({src('lakeland-readymix', 'Lakeland Concrete Contractors')}). A 20×20 ft slab at 4 inches thick needs roughly 5 cubic yards before waste, so a small pad that only needs 1 or 2 yards is almost always hit with a short-load fee, which is part of why a tiny pour costs more per square foot than a full driveway does.</p>"),
        sec("Permits: when a pad needs one, and when it doesn't",
            "<p>Whether a slab needs a permit turns on its use and its size, not a single statewide rule. Florida's structural masonry specialty contractor certificate covers slabs, footers and foundations as a category, but that's a licensing scope, not a permit trigger by itself "
            f"({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). Since July 1, 2026, Florida's HB 803 exempts single-family homeowners and their contractors from a local building permit on non-structural work valued under $7,500, outside a flood-hazard area, which covers plenty of shed, generator and utility pads, though a written exemption request still has to be filed "
            f"({src('orlando-hb803-guide', 'City of Orlando, HB 803 guide')}).</p>"
            + table("Slab permit snapshot, selected jurisdictions (checked October 2026)", ["Jurisdiction", "What applies", "Notes"],
                    [["City of Kissimmee", "Building permit, type \"Slab With/Without Footer\"", "A separate permit track from driveways and sidewalks"],
                     ["City of Orlando", "Engineering permit covering concrete, pavers and asphalt pads", "Same track used for driveways"],
                     ["Manatee County (unincorporated)", "No permit for a non-structural slab", "A slab with footers, or one that carries a structure, still needs one"],
                     ["Statewide, HB 803", "No building permit under $7,500 for non-structural work outside flood zones", "Written exemption request required; doesn't cover a structural addition"]],
                    f"{src('kissimmee-permit-types', 'City of Kissimmee')}; {src('orlando-res-requirements', 'City of Orlando')}; {src('manatee-no-permit-list', 'Manatee County')}; {src('orlando-hb803-guide', 'City of Orlando')}.")
            + f"<p>On a contract over $2,500, Florida's lien law requires a recorded Notice of Commencement before work starts no matter which permit track applies ({src('fs713-13', 'F.S. 713.13')}). A garage addition tied into the house's structure sits outside any of the accessory-pad exemptions above and generally needs the full engineered permit path instead. "
              f"{post('shed-slab-guide-florida', 'Our shed slab guide')} and {post('concrete-pad-for-rv-or-boat-parking', 'RV and boat pad guide')} go deeper into size, thickness and permit questions for those specific pads.</p>"),
        sec("Two worked examples",
            "<p>These are planning illustrations built from the market range above, not jobs we've priced or a promise of what your pad will run.</p>"
            f"<p><strong>Orlando area.</strong> Say you have a 12 × 20 ft carport slab (240 sq ft) going in behind a 1990s {city('clermont', 'Clermont')} home, poured on clear, graded ground with no demolition. At {price(PK)} per sq ft, that's roughly $960 to $2,400, or $1,440 to $1,920 nearer the typical middle, before any permit fee. If the carport ties into the house as a true addition rather than standing alone, the structural review adds cost the accessory-pad estimate above doesn't capture.</p>"
            f"<p><strong>Sarasota area.</strong> Say you have a 10 × 14 ft generator and AC equipment pad (140 sq ft) added after storm season at a {city('bradenton', 'Bradenton')} home, 4 inches thick on open ground. At the same {price(PK)} market range, that's about $560 to $1,400, or $840 to $1,120 nearer the middle. The rate doesn't change because the address is in Manatee County instead of Orange; what can change the number is whether Manatee's non-structural exemption applies to that particular pad.</p>"
            + (photo(pids[1], "Compacted gravel base being prepared for a new concrete pad.") if len(pids) > 1 else "")),
        sec("How to save money without cutting the base",
            "<p>The base and the slab's thickness are the two places a cheap bid usually cuts corners, and they're also the two places that cost the most to fix later once a pad has already settled or cracked. A few other levers move the price without touching either one.</p>"
            + ul(["Order the right mix for the job instead of defaulting to the highest-strength option; a shed floor doesn't need the same mix as a parking pad built for a work truck.",
                  "Schedule a small pad alongside a larger pour already planned on the property, a driveway section or a patio, so the truck's delivery and the minimum-load fee are shared instead of paid twice.",
                  "Keep the finish plain. A broom finish costs less than a stamped or colored one, and a utility pad under a shed or generator rarely benefits from either.",
                  "Confirm whether your project qualifies for the HB 803 permit exemption before a contractor builds a full permit fee into the bid by default.",
                  "Avoid thinning the slab or skipping compaction passes to hit a lower number; a pad that settles in year two costs more to fix than it saved on day one."])),
        sec("What a slab quote should include",
            "<p>A complete bid for a concrete pad spells out more than a single dollar figure per square foot.</p>"
            + ul(["Thickness and mix (standard, rebar-reinforced, high-strength or fiber-mesh) written down, tied to what the pad will actually carry.",
                  "How the base is prepared: what gets removed, what compacted fill goes in, and in how many lifts.",
                  "Whether demolition and haul-off of anything that's there now, an old pad, a stump, is included or billed separately.",
                  "Whether a permit applies to your specific pad, who files it, and whether the fee is part of the quoted price.",
                  "Cure time before the pad can be loaded, especially for a pad going under a heavy generator or a vehicle."])
            + f"<p>{svc('concrete-slabs', 'Our concrete slab page')} covers how we build and base a pad; {compare('resurface-vs-replace-concrete', 'our resurface-or-replace comparison')} is the place to look if the question is fixing an old slab rather than pouring a new one.</p>"),
    ])
    faqs = [faq("How much does a 12x12 concrete slab cost?",
                f"A 144 sq ft pad at the Florida market range of {price(PK)} per sq ft runs roughly $576 to $1,440, or $864 to $1,152 nearer the typical middle, before any demolition or permit fee. Thickness changes that number more than the footprint does: a standard 4-inch pour sits at the lower end, a 6-inch reinforced pad for heavier loads sits toward the top."),
            faq("How much does a yard of concrete cost in Florida?",
                f"Orlando-area ready-mix runs about $120 to $170 per cubic yard for all-purpose mix and $160 to $215 for high-strength ({src('angi-driveway-orlando', 'Angi Orlando')}). Lakeland and Polk County contractor pricing averages around $145 a yard, with added fuel and short-load fees on small orders ({src('lakeland-readymix', 'Lakeland Concrete Contractors')}). A 20×20 ft slab at 4 inches needs roughly 5 yards before waste."),
            faq("Does the price include the base and compaction?",
                "It should, and it's worth asking directly if a bid doesn't spell it out. A complete slab price includes clearing and compacting the subgrade before any concrete is ordered; a quote that skips this step on paper is usually one that skips it on site too, which is where a Florida pad most often fails first."),
            faq("Why do small pads cost more per square foot than a driveway?",
                "Forming, mobilizing a crew and ordering a truck cost close to the same dollar amount whether the pour is 80 square feet or 800. A small generator pad spreads those fixed costs over far less area, so its per-square-foot price runs higher even though the total bill is much smaller than a driveway's."),
            faq("Does removing an old slab add to the cost?",
                "Yes. Concrete removal including haul-off runs $3 to $8 per square foot nationally, and a small 10×10 slab typically comes out for $300 to $800 before the new pour even starts. Reinforced concrete with embedded wire mesh or rebar costs more to break out than plain concrete."),
            faq("Is a permit fee included in a slab quote?",
                "Not automatically, and it depends on the pad. A non-structural accessory pad under $7,500 outside a flood zone may qualify for Florida's HB 803 exemption from a building permit, though a written exemption request is still required; a garage addition tied into the house's structure almost always needs the full permit path. Ask which applies to your project before comparing bids.")]
    return page("/concrete-slab-cost/", "price", "Concrete Slab Cost in Florida (2026)",
                "Florida market ranges for concrete slab installation as of October 2026: size tables, cost by thickness and mix, ready-mix pricing, and what moves a quote.",
                "What a Concrete Slab Costs in Florida",
                capsule(f"As of October 2026, a concrete slab in Greater Orlando or Sarasota–Manatee runs {price(PK)} per square foot installed, with a typical job nearer {price(PK, True)}, based on published Florida and national contractor pricing. A 12×12 shed or equipment pad lands near $864 to $1,152 at that middle range. Thickness, reinforcement and what has to come out first move the price more than the footprint alone."),
                body, faqs=faqs, sources=["homeguide-concrete-slab", "angi-slab-orlando", "angi-driveway-orlando", "homeguide-concrete-removal", "lakeland-readymix",
                                          "fac61g4-15-100", "orlando-hb803-guide", "kissimmee-permit-types", "orlando-res-requirements", "manatee-no-permit-list", "fs713-13"],
                related=[("/concrete-slabs/", "Concrete slab installation"), ("/compare/resurface-vs-replace-concrete/", "Resurface or replace concrete"),
                         ("/blog/shed-slab-guide-florida/", "Shed slabs in Florida"), ("/blog/concrete-pad-for-rv-or-boat-parking/", "RV and boat pads"),
                         ("/cost/", "All cost guides")],
                crumbs=CRUMBS, service=K, form=True, hero_photo=pids[0] if pids else None, offer=offer(PK), eyebrow="Cost guide")


# ---------------------------------------------------------------- concrete walkway / sidewalk cost
def walkway_cost():
    K, PK = "concrete-walkways", "concrete-walkway"
    pids = for_service(K, 2)
    widths = [["3 ft wide", "$21–$51 per linear ft"], ["4 ft wide", "$28–$68 per linear ft"], ["5 ft wide", "$35–$85 per linear ft"]]
    sizes = [["Short entry walk, 3 × 15 ft", "45", "$315–$765", "$360–$540"],
             ["Standard front walk, 4 × 25 ft", "100", "$700–$1,700", "$800–$1,200"],
             ["Side-yard path, 4 × 40 ft", "160", "$1,120–$2,720", "$1,280–$1,920"],
             ["Right-of-way crossing, 5 × 20 ft", "100", "$700–$1,700", "$800–$1,200"]]
    body = "".join([
        sec("What does a concrete sidewalk or walkway cost per square foot?",
            f"<p>As of October 2026, a concrete walkway or sidewalk runs {price(PK)} per {per(PK)} installed, with a typical job nearer {price(PK, True)}, drawn from published national cost-guide data "
            f"({src('homeguide-sidewalk', 'HomeGuide, concrete sidewalk')}). Priced per linear foot at a standard 4-foot width, that works out to $28 to $68 a running foot, the same figure HomeGuide publishes directly for a 4-foot sidewalk, which lines up with multiplying the per-square-foot range by the width. A short front walk costs less in total than a long side-yard run, but both price out at the same rate per square foot; what separates a cheap walk from an expensive one is usually what came before it, not how far it runs.</p>"
            + (photo(pids[0], "Concrete paver stepping-stone path crossing a lawn toward a house entrance.") if pids else "")),
        sec("Cost per linear foot by width", "<p>Narrower paths used for a side-yard trash run price lower per linear foot than a wider entry walk or right-of-way crossing, simply because less concrete goes into each foot of length.</p>"
            + table(f"Concrete walkway cost per linear foot, at {price(PK)} per sq ft", ["Width", "Cost per linear ft"], widths,
                    f"Width multiplied by the {price(PK)} per sq ft market range. {src('homeguide-sidewalk', 'HomeGuide')} publishes the 4-foot figure directly.")),
        sec("Concrete walkway cost by size",
            "<p>These totals apply the same per-square-foot range across a few common layouts, from a short entry walk to a full right-of-way sidewalk crossing. They assume clear ground with nothing to tear out first.</p>"
            + table(f"Walkway totals by layout, {price(PK)} per sq ft", ["Layout", "Sq ft", "Market range", "Typical"], sizes,
                    f"Arithmetic on the {price(PK)} and {price(PK, True)} per sq ft figures. HomeGuide's own 200 sq ft example prices at $1,400 to $3,400, in line with this range ({src('homeguide-sidewalk', 'HomeGuide')}).")),
        sec("Removing an old walk before pouring a new one",
            f"<p>A new walk poured on clear ground is one project; tearing out a cracked or sunken one first is another, priced as its own line item. HomeGuide's national data puts full remove-and-replace work at $10 to $25 or more per square foot, well above the $7–$17 figure for a straightforward new pour, and a small repair that doesn't replace the whole run runs $3 to $8 per square foot instead "
            f"({src('homeguide-sidewalk', 'HomeGuide')}). A 100 sq ft section that has to come out before the new concrete goes in adds roughly $1,000 to $2,500 at the remove-and-replace rate, on top of whatever the new pour itself costs.</p>"),
        sec("Stamped, colored and paver alternatives",
            "<p>A plain broom finish sits at the lower half of the walkway range; stamping or coloring the surface, usually done to carry a pattern through from an adjoining patio, pushes the price toward the top of it and beyond.</p>"
            + table("Walkway finish options", ["Finish", "Range per sq ft", "Notes"],
                    [["Broom finish", "$7–$12", "Standard, slip-resistant texture; the baseline most front walks use"],
                     ["Exposed aggregate or colored", "$10–$15", "Matches a driveway or patio finish poured in the same color"],
                     ["Stamped concrete", "$10–$21", "Carries a pattern through from an adjoining stamped patio or driveway"]],
                    f"{src('homeguide-sidewalk', 'HomeGuide, concrete sidewalk')}.")
            + f"<p>Paver walkways are a different product entirely, not concrete at all, and run $15 to $40 per square foot installed, higher than any concrete finish but repairable one unit at a time ({src('homeguide-paver-walkway', 'HomeGuide, paver walkway')}). {a('/paver-patio-cost/', 'Our paver patio cost guide')} covers that option and its own size table in full.</p>"),
        sec("What moves a walkway quote, beyond width and length",
            "<p>A walkway's price swings on a handful of site conditions more than on the layout itself.</p>"
            + ul([f"<strong>Demolition.</strong> An old, cracked walk has to be cut out and hauled off before the new pour, pushing the job from the new-pour range into the $10–$25+ remove-and-replace range.",
                  "<strong>A crossing section.</strong> Several cities in our service area specify a thicker section where a sidewalk passes in front of a driveway apron, so one part of the same walk can be built to a different spec than the rest of it.",
                  "<strong>Base work.</strong> A narrow path still needs a compacted subgrade underneath; the labor to do that right doesn't shrink proportionally just because the walk is 4 feet wide instead of 20.",
                  "<strong>Access.</strong> A side-yard path behind a narrow gate or fence line sometimes rules out a concrete buggy, which means wheelbarrowing material in by hand and a longer day for the same square footage.",
                  "<strong>Whether the section sits in the right-of-way.</strong> A private front walk and a public sidewalk crossing can be billed and permitted separately even when they're poured on the same visit."])),
        sec("Permits for a private walk versus a right-of-way sidewalk",
            "<p>Where a walkway sits relative to the property line decides whether, and from whom, a permit is needed, and that answer changes by city.</p>"
            + table("Walkway permit snapshot, selected jurisdictions (checked October 2026)", ["Jurisdiction", "Private walk", "Right-of-way sidewalk"],
                    [["City of Clermont", "No building permit, zoning sign-off only", "Separate application and inspection for the apron and sidewalk crossing"],
                     ["City of Sarasota", "No published exemption; the Building Division is the point of contact", "Same"],
                     ["Sarasota County (unincorporated)", "Varies by scope", "Right-of-Way Use Permit required; no walkway may sit inside a drainage easement"]],
                    f"{src('clermont-permit-checklists', 'City of Clermont')}; {src('city-sarasota-bp-guidelines', 'City of Sarasota')}; {src('sarasota-county-row-permit', 'Sarasota County')}; {src('sarasota-county-124-255-culverts', 'Sarasota County Code §124-255')}.")
            + f"<p>On any contract over $2,500, the lien-law Notice of Commencement applies regardless of which permit track the walk falls under ({src('fs713-13', 'F.S. 713.13')}); a small repair under that threshold is exempt from most of the same paperwork, though not from a city's permit requirement where one exists ({src('fs713-02', 'F.S. 713.02')}). {a('/permits/', 'Our permits and HOA hub')} has the full jurisdiction table.</p>"),
        sec("Two worked examples",
            "<p>Both are planning illustrations, not a price for a specific job.</p>"
            f"<p><strong>Orlando area.</strong> Say you have a 4 × 30 ft front walk (120 sq ft) replacing a cracked original walk at a 1970s {city('winter-garden', 'Winter Garden')} home. At the remove-and-replace rate of $10 to $25 per square foot, that's roughly $1,200 to $3,000 for the full job, well above what the same walk would cost poured fresh on open ground.</p>"
            f"<p><strong>Sarasota area.</strong> Say you have a 5 × 40 ft side path (200 sq ft) connecting a {city('lakewood-ranch', 'Lakewood Ranch')} driveway to a side gate, poured on open ground with nothing to remove. At the new-pour range of {price(PK)}, that's about $1,400 to $3,400, in line with HomeGuide's own 200 sq ft figure. The rate is the same one used in the Orlando example; what changed the total was demolition, not the county.</p>"
            + (photo(pids[1], "A narrow concrete side-yard path running along a fence line.") if len(pids) > 1 else "")),
        sec("How to save money without cutting the base",
            "<p>A few choices trim a walkway's cost without touching the compaction or thickness that keep it from cracking.</p>"
            + ul(["Hold the width to what the path actually needs; 3 feet is enough for a side-yard trash run, while a shared entry walk benefits from the extra foot.",
                  "Skip stamping or color on a utility path that no one sees from the street; save the decorative finish for the front entry walk alone.",
                  "If only a section has failed, ask about cutting out and replacing that panel instead of a full remove-and-replace of the whole run; see our concrete repair cost guide for that comparison.",
                  "Schedule the walk alongside another pour already planned on the property so the crew's mobilization cost is shared.",
                  "Don't thin the subgrade compaction to save a day on a long run; a walk poured over loose fill is the one most likely to call us back within a season."])),
        sec("What a walkway quote should include",
            "<p>A complete bid for a walkway or sidewalk crossing spells out more than a single per-square-foot number.</p>"
            + ul(["Width and thickness, including any thicker crossing section where the walk meets a driveway apron.",
                  "Whether removing and hauling off an old walk is included, and at what rate, versus pouring on clear ground.",
                  "Who applies for a right-of-way permit if any part of the path falls outside the property line.",
                  "Joint spacing, since a narrow walk needs tighter joints than a driveway to avoid random cracking between cuts.",
                  "Whether the finish matches an existing patio or driveway, and whether that match is guaranteed on day one versus over time."])
            + f"<p>{svc('concrete-walkways', 'Our concrete walkway page')} covers the full build sequence and Florida soil considerations; {post('front-walkway-ideas-curb-appeal', 'front walkway ideas')} and {post('tree-roots-under-driveway-florida', 'tree roots under a walkway')} go further into design and a common cause of damage.</p>"),
    ])
    faqs = [faq("How much does a concrete sidewalk or walkway cost per square foot?",
                f"As of October 2026, {price(PK)} per square foot installed, typically {price(PK, True)}, which works out to $28 to $68 per linear foot at a standard 4-foot width. Removing an old walk first pushes the job into a higher, $10 to $25-plus per square foot remove-and-replace range instead."),
            faq("Does a right-of-way sidewalk cost more than a walk on private property?",
                "Not necessarily per square foot, but it often carries a separate permit and sometimes a thicker spec where it crosses a driveway apron, both of which add to the total even when the concrete itself is priced the same way. Ask whether your bid treats the private and right-of-way portions as one job or two."),
            faq("Is demolition of an old walkway included in the price?",
                "Only if the bid says so. A quote for a new walk poured on clear ground and a quote that also removes a cracked existing one describe two different scopes at two different per-square-foot rates; compare bids on the same scope before comparing the totals."),
            faq("How does a paver walkway compare in price to concrete?",
                "Pavers run higher, about $15 to $40 per square foot installed against $7 to $17 for concrete, but they can be lifted and reset one unit at a time if a section settles. Our paver patio cost guide covers paver walkway pricing and sizing in full."),
            faq("Do narrow walkways cost more per square foot than a wide driveway?",
                "Width itself doesn't change the per-square-foot rate, but forming and finishing a narrow strip takes close to the same labor as a wider one of the same length, so a small path can feel expensive relative to its total square footage even at the same published rate."),
            faq("Does a stamped or colored walkway cost extra?",
                "Yes. A stamped walkway runs $10 to $21 per square foot against $7 to $12 for a plain broom finish, mostly because of the extra labor to stamp, color and seal the surface rather than the concrete itself costing more.")]
    return page("/concrete-walkway-cost/", "price", "Concrete Sidewalk & Walkway Cost (2026)",
                "Florida and national market ranges for concrete walkway and sidewalk cost per square foot and per linear foot, as of October 2026, with size tables and permit notes.",
                "What a Concrete Walkway or Sidewalk Costs",
                capsule(f"As of October 2026, a concrete walkway or sidewalk runs {price(PK)} per square foot installed, or $28 to $68 per linear foot at a standard 4-foot width, based on published national cost-guide data. A 100 sq ft front walk lands near $700 to $1,700. Removing an old, cracked walk first, rather than pouring on clear ground, is what most often pushes a job toward the top of the range."),
                body, faqs=faqs, sources=["homeguide-sidewalk", "homeguide-paver-walkway", "clermont-permit-checklists", "city-sarasota-bp-guidelines",
                                          "sarasota-county-row-permit", "sarasota-county-124-255-culverts", "fs713-13", "fs713-02"],
                related=[("/concrete-walkways/", "Concrete walkway installation"), ("/concrete-repair-cost/", "Concrete repair cost"),
                         ("/paver-patio-cost/", "Paver patio and walkway cost"), ("/blog/front-walkway-ideas-curb-appeal/", "Front walkway ideas"),
                         ("/permits/", "Permits and HOA hub")],
                crumbs=CRUMBS, service=K, form=True, hero_photo=pids[0] if pids else None, offer=offer(PK), eyebrow="Cost guide")


# ---------------------------------------------------------------- concrete repair / resurfacing cost
def repair_cost():
    K, PK = "concrete-repair", "concrete-repair"
    pids = for_service(K, 2)
    sizes = [["One-car section, 200 sq ft", "$600–$2,000", "$800–$1,400"],
             ["Two-car driveway, 400 sq ft", "$1,200–$4,000", "$1,600–$2,800"],
             ["Three-car driveway, 864 sq ft", "$2,592–$8,640", "$3,456–$6,048"],
             ["Patio, 300 sq ft", "$900–$3,000", "$1,200–$2,100"]]
    body = "".join([
        sec("How much does it cost to repair a cracked concrete driveway?",
            f"<p>As of October 2026, concrete repair and resurfacing together run {price(PK)} per {per(PK)} in current Florida market data, typically {price(PK, True)}. A single stable crack filled with sealant runs far less, $0.50 to $5 per linear foot, while a full cut-out-and-replace of a damaged section runs more, $10 to $15 per square foot in Orlando-area data, since it includes demolition and a full new pour rather than a surface treatment "
            f"({src('angi-driveway-repair-orlando', 'Angi Orlando, driveway repair')}). The right number for your driveway depends on which of those four or five different repairs it actually needs, which is why repair pricing spreads so much wider than installation pricing for the same material.</p>"
            + (photo(pids[0], "A crew finishing a resurfaced section of concrete driveway.") if pids else "")),
        sec("Cost by repair method", "<p>\"Concrete repair\" covers several distinct jobs, each priced its own way rather than by square foot alone.</p>"
            + table("Repair and resurfacing cost by method", ["Method", "Range", "When it fits"],
                    [["Crack sealing", "$0.50–$5 per linear ft", "A stable, narrow crack that isn't tied to a settled area"],
                     ["Pothole patch", "$105–$410 each", "Isolated surface damage, usually a spalled or chipped spot"],
                     ["Mudjacking (slab lifting)", "$3–$9/sq ft, $500 typical minimum", "A sunken panel over a void, on stable soil"],
                     ["Polyurethane foam leveling", "$8–$25/sq ft", "A sunken panel on soft or saturated ground, where added weight is a concern"],
                     ["Resurfacing overlay, plain", "$3–$7/sq ft", "Cosmetic wear on a structurally sound slab"],
                     ["Resurfacing overlay, stamped or decorative", "$6–$20/sq ft", "Cosmetic wear plus a pattern or color change"],
                     ["Cut-out and replace a panel", "$10–$15/sq ft (Orlando); $6–$14 national", "A panel too cracked or damaged for any surface fix to hold"]],
                    f"{src('angi-driveway-repair-orlando', 'Angi Orlando')}; {src('homeguide-driveway-repair', 'HomeGuide, driveway repair')}; {src('homeguide-mudjacking', 'HomeGuide, mudjacking')}; {src('homeguide-polyjacking', 'HomeGuide, polyjacking')}; {src('homeguide-concrete-resurfacing', 'HomeGuide, concrete resurfacing')}.")),
        sec("Resurfacing cost by size",
            f"<p>When resurfacing, rather than a point repair, is the right call, these totals apply the {price(PK)} market range across common driveway and patio sizes.</p>"
            + table(f"Resurfacing totals by size, {price(PK)} per sq ft", ["Area", "Market range", "Typical"],
                    [[r[0], r[1], r[2]] for r in sizes],
                    f"Arithmetic on the {price(PK)} and {price(PK, True)} per sq ft figures. Orlando-specific data runs higher for resurfacing alone, $5 to $10 per sq ft against $3 to $5 nationally, which is already reflected in the wider market range above ({src('angi-driveway-repair-orlando', 'Angi Orlando')}).")),
        sec("How much does concrete leveling cost?",
            f"<p>Leveling, raising a sunken panel back toward grade rather than replacing it, runs $3 to $12 per square foot or $700 to $5,000 for a typical job depending on method and size "
            f"({src('homeguide-concrete-leveling', 'HomeGuide, concrete leveling')}). Mudjacking, pumping a cement-based slurry under the slab, is the cheaper of the two common methods at $3 to $9 per square foot with a roughly $500 minimum; Orlando data shows mudjacking jobs scaling from about $500 to $650 for 50 square feet up to $2,400 to $3,500 for 800 square feet "
            f"({src('angi-mudjacking-orlando', 'Angi Orlando, mudjacking')}). Polyurethane foam injection costs more per square foot, $8 to $25, but adds far less weight to already-soft ground, which matters more on flatwoods soils with a shallow seasonal water table than it does on well-drained ridge sand.</p>"
            "<p>Neither method is the right fit for a crack that's still actively moving or a panel that's cracked through rather than simply sunken; a crew should diagnose which situation you have before recommending either one, since quoting a leveling price before confirming there's an intact panel to lift is a guess dressed up as a number.</p>"),
        sec("What moves a repair quote, and why the diagnosis matters more than the method",
            "<p>A repair bid can swing widely for reasons that have little to do with the size of the visible crack.</p>"
            + ul(["<strong>What's actually underneath.</strong> A void under the slab from a washed-out base, common on flatwoods soils with a shallow seasonal water table, calls for lifting; a root pushing up from below calls for grinding or cutting, a different fix entirely.",
                  "<strong>How many panels are affected.</strong> One cracked joint is a small job; a driveway with three settled panels and a network of hairline cracks is closer to a full resurfacing or replacement scope.",
                  "<strong>Access for equipment.</strong> Mudjacking and foam rigs need room to park and run hose to the work area; a backyard patio reached only through a narrow side gate adds labor time a street-facing driveway doesn't.",
                  "<strong>Whether the cause gets fixed, not just the symptom.</strong> Resurfacing over an active void looks finished on day one and often cracks again within a wet season, which turns a one-time repair cost into two.",
                  "<strong>Permits, on a full section replacement.</strong> A cut-out-and-replace job large enough to resemble new construction can trigger the same permit review a new driveway would, where a crack fill or a leveling job typically doesn't."])),
        sec("Permits and HOA notice for repair work",
            "<p>A repair that stays within a slab's existing footprint, crack sealing, leveling by injection, or a resurfacing overlay, usually doesn't trigger the same permit review a new driveway does, though a large cut-out-and-replace of a right-of-way apron can fall back under the ordinary flatwork permit for that jurisdiction. Manatee County's published list of work that needs no permit covers routine, non-structural repair, while Orange County and the City of Orlando route larger section replacements through the same engineering permit used for new concrete "
            f"({src('manatee-no-permit-list', 'Manatee County')}; {src('orange-do-i-need-permit', 'Orange County')}). On a contract over $2,500, the lien-law Notice of Commencement still applies regardless of whether the repair itself needs a building permit "
            f"({src('fs713-13', 'F.S. 713.13')}). An HOA with architectural control over a driveway's appearance can generally require notice before color-matched resurfacing, even where the repair needs no government permit at all; {post('hoa-approval-for-pavers-and-concrete', 'our HOA approval guide')} covers that process.</p>"),
        sec("Two worked examples",
            "<p>Both are planning illustrations built from the ranges above, not a bid for an actual driveway.</p>"
            f"<p><strong>Orlando area.</strong> Say you have a 20 × 20 ft two-car driveway (400 sq ft) in a 1990s {city('kissimmee', 'Kissimmee')} subdivision, with hairline cracks along two joints and one settled corner about 100 square feet in size. Sealing roughly 30 linear feet of crack runs about $15 to $150; lifting the settled corner by mudjacking, going by Orlando's own 100 sq ft pricing band, runs about $650 to $950. Combined, the job lands in roughly the $700 to $1,100 range, well below what resurfacing or replacing the whole driveway would cost.</p>"
            f"<p><strong>Sarasota area.</strong> Say you have a 24 × 24 ft driveway (576 sq ft) in a {city('bradenton', 'Bradenton')} neighborhood that's cosmetically worn, faded and lightly spalled in a few spots, but structurally sound with no sunken panels. Resurfacing the full surface at the {price(PK, True)} typical range runs about $2,304 to $4,032, a fraction of what a full tear-out and replacement at $10 to $15 per square foot would cost.</p>"
            + (photo(pids[1], "Close-up of a saw cutting a control joint into fresh concrete.") if len(pids) > 1 else "")),
        sec("How to save money without cutting the base",
            "<p>The one shortcut that never pays off in a repair is skipping the diagnosis to get to a price faster.</p>"
            + ul(["Get the cause identified before picking a method; a resurfacing quote written before anyone checks for a void underneath is a guess with a number attached.",
                  "Seal a stable crack while it's still small and linear-foot priced, rather than waiting until it widens into a panel that needs cutting out.",
                  "Bundle a few small repairs into one site visit instead of calling separately for each one, since most repair jobs carry a minimum charge that's paid once per visit, not once per crack.",
                  "Choose mudjacking over foam injection where the soil underneath is stable enough for it; it's the less expensive of the two leveling methods per square foot.",
                  "Don't choose resurfacing over replacement just because it's cheaper upfront if the slab underneath is still actively settling; that's the scenario most likely to need the work redone."])),
        sec("What a repair quote should include",
            "<p>A complete repair bid names the method and the reason for it, not just a number.</p>"
            + ul(["A stated diagnosis: void, root, cracked panel or cosmetic wear, before a method is recommended.",
                  "The specific method, crack sealing, mudjacking, foam leveling, overlay or cut-out-and-replace, not just a total price.",
                  "Square footage or linear footage for each affected area, not one number for the whole driveway if only part of it needs work.",
                  "For a replaced panel, the thickness, strength and dowel detail tying it into the surrounding slab.",
                  "Whether the quote addresses the underlying cause, drainage, a root, an unfinished base, or only the visible symptom."])
            + f"<p>{svc('concrete-repair', 'Our concrete repair page')} walks through the full diagnostic sequence; {compare('resurface-vs-replace-concrete', 'our resurface-or-replace comparison')} and {post('concrete-driveway-cracks-florida', 'which driveway cracks are normal in Florida')} go further into the decision itself.</p>"),
    ])
    faqs = [faq("How much does it cost to repair a cracked concrete driveway?",
                f"It depends on the repair. Crack sealing runs $0.50 to $5 per linear foot, mudjacking a sunken panel runs $3 to $9 per square foot with a roughly $500 minimum, and a full cut-out-and-replace runs $10 to $15 per square foot in Orlando-area data. Across all repair and resurfacing work, the market range is {price(PK)} per square foot."),
            faq("How much does concrete leveling cost?",
                "Leveling a sunken panel runs $3 to $12 per square foot, or roughly $700 to $5,000 for a typical job. Mudjacking, the cement-slurry method, is the less expensive option at $3 to $9 per square foot; polyurethane foam injection costs more, $8 to $25 per square foot, but adds far less weight to soft or saturated ground."),
            faq("Is mudjacking cheaper than polyurethane foam leveling?",
                "Per square foot, yes, mudjacking typically runs less. The right choice depends on the soil underneath more than the price, though: foam is usually the better fit on soft or saturated ground, since its added weight is a small fraction of what a mudjacking slurry adds to the same area."),
            faq("Does resurfacing cost less than replacing a driveway?",
                "Usually, yes, by a wide margin, since resurfacing covers only the surface at $3 to $7 per square foot against $10 to $15 for a full cut-out-and-replace. Resurfacing only holds up over the long run on a slab that's structurally sound underneath; applied over an active void, it tends to crack again within a wet season or two."),
            faq("Is there a minimum charge for a small repair?",
                "Most repair methods carry one. Mudjacking jobs commonly carry a minimum around $500 regardless of area, and polyurethane foam jobs carry a similar $300 to $700 minimum. That's part of why bundling a few small repairs into one visit, rather than calling separately for each, tends to cost less overall."),
            faq("Does patio repair cost the same as driveway repair?",
                "Roughly, since both are priced by method rather than by which slab they're on. National data for patio repair by material runs $5 to $20 per square foot for concrete, in the same band as driveway repair; what differs more is access, since a backyard patio reached through a gate sometimes costs more in labor time than a street-facing driveway.")]
    return page("/concrete-repair-cost/", "price", "Concrete Repair & Resurfacing Cost (2026)",
                "Florida market ranges for concrete driveway repair cost as of October 2026: crack sealing, mudjacking, foam leveling, resurfacing and panel replacement compared.",
                "What Concrete Repair and Resurfacing Cost",
                capsule(f"As of October 2026, concrete repair and resurfacing run {price(PK)} per square foot in Florida market data, typically {price(PK, True)}. Crack sealing alone runs $0.50 to $5 per linear foot; mudjacking a sunken panel runs $3 to $9 per square foot. A full cut-out-and-replace of a damaged section costs more, $10 to $15 per square foot in Orlando data, since it includes demolition and a new pour."),
                body, faqs=faqs, sources=["angi-driveway-repair-orlando", "homeguide-driveway-repair", "homeguide-mudjacking", "angi-mudjacking-orlando",
                                          "homeguide-polyjacking", "homeguide-concrete-resurfacing", "homeguide-concrete-leveling", "manatee-no-permit-list",
                                          "orange-do-i-need-permit", "fs713-13"],
                related=[("/concrete-repair/", "Concrete repair & resurfacing"), ("/compare/resurface-vs-replace-concrete/", "Resurface or replace concrete"),
                         ("/blog/concrete-driveway-cracks-florida/", "Which driveway cracks are normal"), ("/blog/sinkholes-and-settlement-central-florida/", "Sinkholes vs. normal settlement"),
                         ("/cost/", "All cost guides")],
                crumbs=CRUMBS, service=K, form=True, hero_photo=pids[0] if pids else None, offer=offer(PK), eyebrow="Cost guide")


# ---------------------------------------------------------------- paver driveway cost
def paver_driveway_cost():
    K, PK = "paver-driveways", "paver-driveway"
    pids = for_service(K, 2)
    sizes = [["1-car, 10 × 20 ft", "200", "$2,000–$6,000", "$2,400–$4,000"],
             ["1-car, 12 × 24 ft", "288", "$2,880–$8,640", "$3,456–$5,760"],
             ["2-car, 20 × 20 ft", "400", "$4,000–$12,000", "$4,800–$8,000"],
             ["2-car, 24 × 24 ft", "576", "$5,760–$17,280", "$6,912–$11,520"],
             ["3-car, 24 × 36 ft", "864", "$8,640–$25,920", "$10,368–$17,280"]]
    materials = [["Concrete pavers", "$10–$18", "$5,760–$10,368"], ["Brick", "$12–$22", "$6,912–$12,672"],
                 ["Permeable pavers", "$15–$25", "$8,640–$14,400"], ["Porcelain", "$15–$30", "$8,640–$17,280"],
                 ["Natural stone", "$20–$35", "$11,520–$20,160"]]
    body = "".join([
        sec("How much does a paver driveway cost in Florida?",
            f"<p>As of October 2026, installed paver driveways run {price(PK)} per {per(PK)} in current Florida market data, typically {price(PK, True)}, across the material options contractors offer locally "
            f"({src('homeguide-driveway-pavers', 'HomeGuide')}; {src('angi-paver-driveway', 'Angi')}). A South Florida paver contractor's own published pricing lands in a similar $12 to $32 per square foot band depending on material "
            f"({src('craftpavers-fl-pricing', 'Craft Pavers')}). The material you choose moves the price more than anything else on the job, concrete pavers sit at the lower end, natural stone at the top, and whether an old driveway has to come out first is the other big swing factor.</p>"
            + (photo(pids[0], "A row of paver driveways along a palm-lined Florida street.") if pids else "")),
        sec("Paver driveway cost by size", "<p>These totals apply the full market range across common driveway footprints, from a single-car driveway to a three-car layout, on clear ground with no old driveway to remove.</p>"
            + table(f"Paver driveway totals by size, {price(PK)} per sq ft", ["Driveway", "Sq ft", "Market range", "Typical"], sizes,
                    f"Arithmetic on the {price(PK)} and {price(PK, True)} per sq ft figures. HomeGuide's own 2-car 24×24 ft example prices at $5,700 to $17,200, in line with this range ({src('homeguide-driveway-pavers', 'HomeGuide')}).")),
        sec("Cost by material, for a two-car driveway",
            "<p>The unit itself, not the base underneath it, is what separates a budget paver driveway from an expensive one. These totals apply Angi's published per-material rates to a 576 sq ft, two-car footprint.</p>"
            + table("Material cost for a 576 sq ft two-car paver driveway", ["Material", "Per sq ft", "Total"], materials,
                    f"{src('angi-paver-driveway', 'Angi, paver driveway cost')}; labor runs $5–$15 per sq ft on top of material cost across all five options, so the base-and-labor share of the job narrows the spread between the cheapest and most expensive material shown here.")),
        sec("Why removing old concrete first changes the number",
            f"<p>Replacing an existing concrete driveway with pavers, rather than installing on bare or landscaped ground, runs $12 to $35 per square foot including demolition, noticeably higher than new pavers on clear ground "
            f"({src('homeguide-driveway-pavers', 'HomeGuide')}). On a 400 sq ft driveway, that's the difference between roughly $4,800 and $14,000 with demolition against $4,000 to $12,000 without it. Breaking out and hauling off the old slab, then building the full paver base underneath where the concrete used to sit, is close to two jobs stacked into one, which is why a like-for-like swap from concrete to pavers rarely lands at the bottom of either range.</p>"
            f"<p>Haul-off adds a second cost on top of the breaking-out labor: dump fees for concrete debris run roughly $90 to $160 per ton nationally, and an average driveway's worth of old slab weighs several tons once it's broken up ({src('homeguide-concrete-removal', 'HomeGuide, concrete removal')}), which is part of why a contractor who quotes demolition as a flat line item rather than a per-ton pass-through is usually easier to compare against another bid. Reinforced concrete, with embedded wire mesh, costs more to break out than plain unreinforced slab, since the mesh has to be cut free rather than simply fractured and lifted.</p>"),
        sec("What else moves a paver driveway quote",
            "<p>Beyond material and demolition, a few other factors routinely separate bids on paper-identical driveways.</p>"
            + ul(["<strong>Paver thickness.</strong> 60 mm units are standard for a car driveway; 80 mm, priced somewhat higher, is specified for an RV, boat trailer or regular work-truck traffic.",
                  "<strong>Base depth.</strong> A wet, poorly drained flatwoods lot needs 2 to 4 inches more compacted aggregate than a free-draining ridge-sand lot, more material and more compaction passes for the same footprint.",
                  "<strong>Pattern and cutting.</strong> A running-bond layout wastes less material and labor than a herringbone or a layout with a custom border, both of which need more units cut to fit.",
                  "<strong>Edge restraint.</strong> It's invisible once the job is done, which is also why it's the line item most often left off a cheap bid; without it along the full perimeter, the field spreads under tire loads within a season or two.",
                  "<strong>Permit and right-of-way work.</strong> The apron almost always sits in a right-of-way the city or county controls, and it can carry its own spec and fee separate from the rest of the driveway."])),
        sec("Are paver driveways more expensive than concrete?",
            f"<p>By published price alone, yes. Paver driveways run {price(PK)} per square foot against roughly $6 to $20 for concrete, including stamped finishes, in the same Florida and national data. That's a price-only comparison, though, not the full picture: pavers can be lifted and reset one unit at a time if a section settles or stains, where a concrete repair usually means cutting out and replacing a whole panel. "
            f"{compare('pavers-vs-concrete-driveway', 'Our pavers vs. concrete driveway comparison')} works through lifespan, repair cost over time and resale together, which matters more to most homeowners than the installed price alone.</p>"),
        sec("Permits for a paver driveway",
            f"<p>Florida law exempts driveway installation from needing a state or local contractor license, but it never exempts the permit itself ({src('fs489-117', 'F.S. 489.117')}). Orange County charges a flat $38 zoning review fee plus a $38 engineering review for a paver driveway, a small line item next to the driveway's own cost "
            f"({src('orange-residential-pavers', 'Orange County')}). Manatee and Sarasota counties each route the work through their own access, drainage or right-of-way permit instead "
            f"({src('manatee-paver-driveway-inspections', 'Manatee County')}; {src('sarasota-county-row-permit', 'Sarasota County')}). On a contract over $2,500, the lien-law Notice of Commencement applies no matter which permit track covers the driveway itself "
            f"({src('fs713-13', 'F.S. 713.13')}). {post('driveway-widening-and-extensions-florida', 'Our driveway widening guide')} and {a('/permits/', 'the permits and HOA hub')} cover county-by-county detail beyond what fits here.</p>"),
        sec("Two worked examples",
            "<p>Both are planning illustrations, not a quote for an actual driveway.</p>"
            f"<p><strong>Orlando area.</strong> Say you have a 24 × 24 ft two-car driveway (576 sq ft) in a {city('horizon-west', 'Horizon West')} subdivision, and you're replacing a cracked original concrete driveway with concrete pavers. At the $12 to $35 per square foot remove-and-replace range, that's roughly $6,912 to $20,160 for the full job, demolition included.</p>"
            f"<p><strong>Sarasota area.</strong> Say you have a 12 × 24 ft one-car driveway (288 sq ft) on a new-build lot in {city('parrish', 'Parrish')} with no existing driveway to remove. At the {price(PK)} new-install range, that's about $2,880 to $8,640, or $3,456 to $5,760 nearer the typical middle. The per-square-foot rate is the same one used in the Orlando example; what changed the total was demolition, not the county line.</p>"
            + (photo(pids[1], "A herringbone-pattern paver driveway and walkway leading to a garage.") if len(pids) > 1 else "")),
        sec("How to save money without cutting the base",
            "<p>Base depth and compaction are the one place a paver driveway should never be cut thin to save money; a few other choices bring the price down without touching either.</p>"
            + ul(["Choose concrete pavers over brick, porcelain or natural stone; the material itself, not the base underneath it, is the biggest swing in the price range.",
                  "Keep the layout to a simple running bond rather than a herringbone pattern or a contrasting border, which cuts the amount of custom cutting a crew has to do.",
                  "Specify 60 mm pavers unless the driveway will regularly carry an RV, boat trailer or work truck; 80 mm costs more and isn't needed for ordinary car traffic.",
                  "If the existing concrete is sound, ask whether it makes sense structurally to leave it in place as a base layer rather than demolishing it, a question worth raising before assuming full removal.",
                  "Get a firm figure for edge restraint and demolition as separate line items before comparing two bids on the installed-pavers number alone."])),
        sec("What a paver driveway quote should include",
            "<p>A complete paver driveway bid names the material and the build spec, not only an installed total.</p>"
            + ul(["Material by name, concrete pavers, brick, permeable, porcelain or natural stone, not just a price per square foot.",
                  "Paver thickness, 60 mm or 80 mm, matched to how the driveway will be used.",
                  "Base depth and the compaction standard it's built to, in writing.",
                  "Edge restraint as its own line item along the full perimeter.",
                  "Demolition and haul-off of any existing driveway, itemized separately from the new installation.",
                  "Who applies for the permit, and whether the apron's right-of-way work is included in the same bid."])
            + f"<p>{svc('paver-driveways', 'Our paver driveway page')} covers the full ICPI base spec and build sequence; {post('paver-installation-process-florida', 'how pavers are installed in Florida')} and {post('paver-driveway-ideas-florida', 'paver driveway ideas')} go further into process and design.</p>"),
    ])
    faqs = [faq("How much does a paver driveway cost in Florida?",
                f"As of October 2026, {price(PK)} per square foot installed, typically {price(PK, True)}, depending mostly on material. A 576 sq ft, two-car driveway in concrete pavers runs roughly $5,760 to $10,368; in natural stone, the same footprint runs $11,520 to $20,160."),
            faq("Are paver driveways more expensive than concrete?",
                f"By the published per-square-foot price, yes: {price(PK)} for pavers against roughly $6 to $20 for concrete including stamped finishes. That's a price-only answer; our pavers vs. concrete comparison covers lifespan and repair cost over time, which changes the picture for many homeowners."),
            faq("Does removing an old concrete driveway before installing pavers cost extra?",
                "Yes. A full concrete-to-paver conversion, demolition included, runs $12 to $35 per square foot, higher than the $10 to $30 range for new pavers installed on clear ground, since it combines demolition and base rebuilding with the paver installation itself."),
            faq("Why do natural stone and porcelain pavers cost more than concrete pavers?",
                "Material cost, mainly. Natural stone and porcelain run $20 to $35 and $15 to $30 per square foot respectively against $10 to $18 for concrete pavers, largely because each unit is quarried or manufactured rather than cast in standard molds, and some, like natural stone, vary in thickness and need more careful setting."),
            faq("Is labor a big share of a paver driveway's price?",
                "A meaningful one. Published data puts labor at $5 to $15 per square foot on top of material cost across all paver types, which is why the gap between the cheapest and most expensive material narrows once labor and base work are added to the total."),
            faq("Do 80 mm pavers cost more than 60 mm?",
                "Yes, somewhat, both in the unit itself and because a vehicle-rated base built for RV or boat-trailer loads typically goes deeper than the standard car-driveway spec. We specify 80 mm only where the extra load calls for it, not as a default upgrade.")]
    return page("/paver-driveway-cost/", "price", "Paver Driveway Cost in Florida (2026)",
                "Florida market ranges for paver driveway cost as of October 2026: size tables, material comparison for a two-car driveway, and permits by county.",
                "What a Paver Driveway Costs in Florida",
                capsule(f"As of October 2026, a paver driveway in Greater Orlando or Sarasota–Manatee runs {price(PK)} per square foot installed, typically {price(PK, True)}, based on published Florida and national contractor pricing. A 576 sq ft two-car driveway in concrete pavers runs roughly $5,760 to $10,368; natural stone runs about double that. Material and whether an old driveway has to come out first move the price more than size alone."),
                body, faqs=faqs, sources=["homeguide-driveway-pavers", "angi-paver-driveway", "craftpavers-fl-pricing", "homeguide-concrete-removal", "fs489-117", "orange-residential-pavers",
                                          "manatee-paver-driveway-inspections", "sarasota-county-row-permit", "fs713-13"],
                related=[("/paver-driveways/", "Paver driveway installation"), ("/compare/pavers-vs-concrete-driveway/", "Pavers vs. concrete driveway"),
                         ("/blog/paver-installation-process-florida/", "How pavers are installed"), ("/blog/paver-driveway-ideas-florida/", "Paver driveway ideas"),
                         ("/cost/", "All cost guides")],
                crumbs=CRUMBS, service=K, form=True, hero_photo=pids[0] if pids else None, offer=offer(PK), eyebrow="Cost guide")


def get_pages():
    return [slab_cost(), walkway_cost(), repair_cost(), paver_driveway_cost()]
