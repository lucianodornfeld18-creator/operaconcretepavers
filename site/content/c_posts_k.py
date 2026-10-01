# -*- coding: utf-8 -*-
"""Blog posts, group k: hiring and money mechanics once a homeowner already knows which service they want.
Covers choosing an artificial turf installer, checking a concrete or paver contractor's license, what a
warranty should and shouldn't cover, comparing quotes line by line, whether a driveway or patio adds home
value, and how to budget a multi-service backyard project in phases. The hiring and warranty posts are
criteria lists only: what to check on any business before signing, never a claim about Opera's own
license, insurance, warranty terms or track record."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext, price, per, contact, photo
from _photos import for_service


def p_how_to_choose_an_artificial_turf_installer():
    pids = for_service("artificial-turf", 1)
    pid = pids[0] if pids else None
    body = "".join([
        sec("How Do You Choose an Artificial Turf Installer in Florida?",
            f"<p>Picking an {svc('artificial-turf', 'artificial turf')} installer in Florida comes down to three checks that matter "
            "more than color samples or a photo gallery: whether the base and infill plan matches the state's 2026 turf standard, "
            "whether there's a written workmanship warranty separate from the manufacturer's warranty on the turf itself, and who's "
            "responsible for any local permit. Two lawns can look identical on install day and perform very differently a year later, "
            "depending entirely on what's buried underneath and what the joints were filled with.</p>"),
        sec("What Should You Ask the Best Artificial Turf Installer Near You?",
            "<p>A search for the best artificial turf installer near me mostly returns businesses sorted by ad spend, which says "
            "little about what's going under a specific lawn. The table below separates the turf-specific questions tied to "
            "Florida's state rule from the general contractor paperwork that applies to any hardscape job.</p>"
            + table("Ten checks before hiring an artificial turf installer in Florida", ["Check", "Why it matters"],
                    [["Subgrade and base material, in writing", "State rule requires washed natural material such as crushed rock or crushed concrete, not unwashed fill"],
                     ["Infill type specified", "Only clean silica sand, rock, shell or coated silica sand is allowed outside a playground footprint"],
                     ["In-ground irrigation plan for the footprint", "State rule bars watering turf with an in-ground irrigation system"],
                     ["Setback from ponds, canals or other water", "10 ft minimum from the water line unless a seawall or bulkhead already exists"],
                     ["Tree drip line clearance", "Turf can't go inside a drip line without a certified arborist's sign-off"],
                     ["Local building or zoning permit handling", "Turf often counts as added impervious coverage; the office that reviews it varies by city"],
                     ["DBPR license status, if the installer holds one", "No statute names turf installation as a licensed trade the way it does a driveway"],
                     ["Manufacturer warranty terms on the turf itself", "Usually covers material defects and UV fading, separate from the installation"],
                     ["Written workmanship warranty on seams and infill", "Covers installation defects such as a lifting seam or unevenly settled infill"],
                     ["General liability insurance certificate", "Confirms coverage is current rather than taken on a verbal claim"]],
                    f"{src('rule62-308-100-text', 'DEP Rule 62-308.100')} sets the base, infill, setback and drip-line standards referenced here.")),
        sec("Does an Artificial Turf Installer Need a License in Florida?",
            "<p>Not in the clearly named way a driveway does. Florida's licensing statute carves \"driveway or tennis court "
            f"installation\" out of state and local licensing requirements by name, but turf installation isn't listed alongside it "
            f"({src('fs489-117', 'F.S. 489.117')}). Turf work also doesn't fall under the state's structural masonry specialty "
            f"category, since there's no slab, footer or wall involved ({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). "
            f"That leaves the question open rather than settled. Running a business name through the {src('dbpr-search', 'DBPR license search')} "
            "shows whether it holds any state certificate at all, and a call to the local building department clarifies whether a "
            f"permit, rather than a license, is what actually governs the job in a given city. {post('florida-contractor-license-check-concrete-pavers', 'Our guide to checking a Florida contractor license')} "
            "covers that search in more depth than fits here.</p>"
            + (photo(pid, "A backyard with bright green artificial turf bordered by large gray concrete pavers near a pool.") if pid else "")),
        sec("What Does Florida's 2026 Turf Standard Require, and How Does It Shape the Questions You Ask?",
            f"<p>DEP Rule 62-308.100, effective May 19, 2026, sets minimum install standards for synthetic turf on single-family lots "
            f"of an acre or less, and it's the baseline an installer's answers should match ({src('rule62-308-100-text', 'Rule 62-308.100')}). "
            "The subgrade has to be washed natural material, crushed rock or crushed concrete, rather than unwashed fill that still "
            "carries fine particles capable of clogging drainage underneath. Infill is limited to clean silica sand, rock, shell or a "
            "coated silica sand; rubber or other synthetic infill is allowed only inside the footprint of playground equipment. The "
            "turf and its backing have to stay permeable over a pervious subgrade, graded so water moves off the lot instead of "
            "pooling, and installation can't go inside a stormwater swale, pond or a pond's littoral zone. Two setback numbers are "
            "worth asking about directly: at least 10 ft from a natural or man-made water body unless a seawall or bulkhead already "
            "serves as a barrier, and no turf inside a tree's drip line without a certified arborist's sign-off. Edges and seams get "
            "anchored against wind and flooding. None of this creates a new state-issued permit on its own, the rule says so "
            f"directly, which is why the local building department, not DEP, is who to ask about paperwork. {post('florida-hoa-artificial-turf-law', 'Our guide to Florida turf law and HOAs')} "
            f"covers how the rule interacts with deed restrictions, and {post('artificial-turf-installation-process', 'our turf installation process guide')} "
            "walks through how a compliant base and infill actually get built on site.</p>"),
        sec("What Should a Written Turf Warranty Cover?",
            "<p>Two separate documents, not one. A manufacturer warranty covers the turf product itself, fiber UV resistance and "
            "color retention most commonly, and industry buyer guides describe residential turf manufacturer warranties running "
            f"roughly 8 to 15 years depending on the product line ({ext('https://ideal-turf.com/artificial-turf-warranties/', 'Ideal Turf, Artificial Turf Warranties')}). "
            "An installer's own workmanship warranty is a shorter, separate document covering the installation itself: whether a "
            "seam bonds and holds, whether infill distributes evenly, whether the base was prepared the way it was described, "
            f"commonly a 1 to 3 year window according to the same buyer guide. {post('concrete-and-paver-warranty-what-it-should-cover', 'Our guide to what a concrete or paver warranty should cover')} "
            "walks through the same manufacturer-versus-workmanship split for hard surfaces, and the logic for asking for both "
            "documents in writing carries over directly to turf.</p>"),
        sec("What Permit Questions Should You Ask Before Turf Goes In?",
            "<p>Permit handling for artificial turf varies more by city than concrete or paver work tends to, since some "
            "jurisdictions treat a synthetic lawn as ordinary landscaping and others treat it as added impervious coverage subject "
            "to the same review as a patio. The city of Orlando, for example, routes turf through the same engineering permit used "
            "for pavers and concrete because the city counts it as impervious surface, with its own water-body buffer that runs "
            f"wider than the state rule's 10 ft minimum ({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). "
            "Asking an installer directly which office handles the paperwork in a specific city, rather than assuming turf is exempt "
            f"because nothing gets poured or mortared, is the safer approach. {post('prepare-your-yard-for-hardscape-installation', 'Our guide to preparing a yard for installation')} "
            "covers what else typically needs to happen before a crew arrives, beyond the permit question itself.</p>"),
        sec("Say You're Comparing Turf Installers for a Pet Area in Apopka",
            f"<p>A homeowner in {city('apopka')} comparing three quotes for a 600 sq ft pet turf area checks each one against the "
            "same three things regardless of price: a stated subgrade and infill spec that matches the state's washed-material and "
            "clean-infill rule, a written workmanship warranty kept separate from whatever the turf manufacturer offers, and "
            "confirmation of which office handles the local permit. A quote that stays silent on infill type or base material is the "
            "one worth a follow-up call before it's the one that gets accepted.</p>"),
    ])
    faqs = [faq("Does artificial turf need a permit in Florida?",
                "Often, yes, though the state's own 2026 turf standard doesn't create a new permit by itself. Many cities route a turf install through the same building or engineering permit used for pavers or concrete, since the finished lawn counts as impervious surface, so checking with the local building department before signing is worth doing rather than assuming turf is exempt."),
            faq("Does an artificial turf installer need a state license in Florida?",
                "Not in a clearly named way. State law exempts driveway installation from licensing requirements by name, but turf isn't listed the same way, and turf work doesn't fall under the structural masonry category either since there's no slab or footer involved. Running the business through the DBPR license search shows what, if anything, it holds, and a county or city building department call settles the permit side."),
            faq("What should a turf warranty cover?",
                "Two separate documents: a manufacturer warranty on the turf material itself, commonly 8 to 15 years against defects and significant UV fading, and a shorter installer workmanship warranty, often 1 to 3 years, covering seam bonding, infill distribution and base preparation. Asking for both in writing, rather than assuming one covers the other, avoids confusion if a seam lifts a year or two in."),
            faq("What base material does Florida's 2026 turf rule require?",
                "A washed natural subgrade material such as crushed rock or crushed concrete, not unwashed fill that still carries fine particles capable of clogging drainage underneath it. The rule also limits infill to clean silica sand, rock, shell or coated silica sand, with rubber or other synthetic infill allowed only inside a playground's footprint."),
            faq("How close to a pond or canal can artificial turf go?",
                "At least 10 feet from the water line under the state's 2026 standard, unless a seawall or bulkhead already serves as a physical barrier. The same rule keeps turf out of a stormwater swale, pond or a pond's littoral zone, and a city's own buffer can run wider than the state minimum.")]
    related = [("/artificial-turf/", "Artificial turf"), ("/blog/florida-hoa-artificial-turf-law/", "Can an HOA ban artificial turf"),
               ("/blog/artificial-turf-installation-process/", "How artificial turf is installed"),
               ("/blog/florida-contractor-license-check-concrete-pavers/", "Checking a Florida contractor's license"),
               ("/artificial-turf-cost/", "Artificial turf cost")]
    return page("/blog/how-to-choose-an-artificial-turf-installer/", "post",
                "Choosing an Artificial Turf Installer in Florida",
                "How to choose an artificial turf installer in Florida: base and infill spec, workmanship warranty and permit checks, as of October 2026.",
                "How to Choose an Artificial Turf Installer in Florida",
                capsule("Choosing an artificial turf installer in Florida means checking three things before pattern or price: "
                        "whether the base and infill plan match the state's 2026 turf standard, a written workmanship warranty "
                        "separate from the turf's own manufacturer warranty, and who handles any local permit. As of October 2026, "
                        "DEP Rule 62-308.100 sets minimum install standards statewide for lots up to one acre."),
                body, faqs=faqs,
                sources=["rule62-308-100-text", "fs489-117", "fac61g4-15-100", "dbpr-search", "orlando-res-requirements",
                         ("Ideal Turf, Artificial Turf Warranties: What to Look For (updated Apr. 2, 2025)", "https://ideal-turf.com/artificial-turf-warranties/")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf",
                image=pid, form=False)


def p_florida_contractor_license_check_concrete_pavers():
    pids = for_service("concrete-driveways", 3)
    pid = pids[2] if len(pids) > 2 else (pids[0] if pids else None)
    body = "".join([
        sec("Does a Concrete or Paver Contractor Need a License in Florida?",
            f"<p>It depends on the scope. {svc('concrete-driveways', 'Driveway')} installation on its own is carved out of state "
            "and local licensing requirements by name, so a driveway-only business can legally operate without a state license, "
            "though a permit can still be required. Structural concrete tied to a foundation, footer, slab or wall falls under a "
            "separate state specialty certificate, and pavers and patios aren't named in the driveway exemption at all, which makes "
            "them a judgment call the statute leaves open rather than a clean yes or no.</p>"),
        sec("How Do You Look Up a Contractor's License on DBPR?",
            f"<p>The {src('dbpr-search', 'DBPR license search')} at myfloridalicense.com takes a business or individual name and "
            "returns license status, type and any discipline history on file. Two terms show up in that listing worth knowing "
            "apart: a \"certified\" contractor holds a state certificate of competency and can legally work anywhere in Florida, "
            "while a \"registered\" contractor is registered off a local competency license and can only work in the specific "
            f"jurisdictions where that local license applies ({src('fs489-105', 'F.S. 489.105')}; {src('fs489-117', 'F.S. 489.117')}). "
            "A business that's \"registered\" in one county has no automatic standing to pull a permit or advertise in another, "
            "which matters for anyone comparing bids from businesses based outside their own county.</p>"
            + (photo(pid, "A clean broom-finish concrete driveway with control joints leads up to a white garage door.") if pid else "")),
        sec("Which Jobs Are Exempt From Needing a License by Name, and Which Aren't?",
            f"<p>F.S. 489.117(4)(a)1 lists specific job scopes a local government can't require a state or local license for, and "
            f"\"driveway or tennis court installation\" is on that list by name, alongside \"decorative stone, tile, marble, "
            f"granite, or terrazzo installation\" ({src('fs489-117', 'F.S. 489.117')}). The statute doesn't abolish the permit "
            "itself, only the license requirement for that specific scope. Structural concrete work sits on the other side of the "
            "line: a 2024 rule created the \"structural masonry specialty contractor\" certificate, covering the forming, placing "
            "and finishing of concrete and masonry in foundations, slabs, footers, curbs, walls, columns and beams "
            f"({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). Pavers and patios fall in between, since neither is "
            "named in the driveway exemption and neither is clearly a foundation or footer, so whether a specific job "
            "\"substantially corresponds\" to the structural masonry scope is something the statute leaves to interpretation "
            f"rather than settling outright. Pool decks sit in a similar gap: the pool contractor categories cover the pool "
            f"structure itself, not the surrounding deck, by the statute's own text ({src('fs489-105', 'F.S. 489.105')}).</p>"
            + table("Which Florida license category, if any, usually applies", ["Job", "License status"],
                    [["Driveway installation, stand-alone", "Named exemption; no state or local license can be required for this scope"],
                     ["Decorative stone, tile, marble or terrazzo", "Also named in the same exemption"],
                     ["Foundation, footer, structural slab or wall", "Structural masonry specialty contractor certificate"],
                     ["Paver patio or paver driveway", "Not named either way; confirm with DBPR and the county"],
                     ["Pool deck (not the pool structure itself)", "No statute clearly assigns this to one category"]],
                    "General guidance, not legal advice; a specific scope can combine more than one category.")),
        sec("What Happened to County-Level \"Concrete\" Licenses After 2025?",
            f"<p>A lot changed here in a short window. A 2021 law, codified at {src('fs163-211', 'F.S. 163.211')}, preempted "
            "occupational licensing to the state but let pre-2021 local licenses keep operating on a sunset clock that moved twice "
            "before landing on July 1, 2025. Past that date, DBPR's own guidance says a local government may only keep licensing "
            "specialty categories that substantially correspond to a state CILB category, or ones the statute expressly allows "
            f"({src('dbpr-hot', 'DBPR CILB Hot Topics')}). Miami-Dade, outside our service area but a useful example, lists "
            "\"Concrete Finishing,\" \"Concrete Forming and Placing\" and \"Masonry Floor\" among the local categories it "
            f"preempted as a result ({src('md-preempt', 'Miami-Dade Contractor License Category Preemption')}). Closer to home, "
            "Manatee County's own pages still describe local licenses covering \"Mason, Masonry and Concrete\" categories, with "
            f"state-certified contractors able to register locally as well ({src('manatee-lic', 'Manatee County Contractor Licensing')}). "
            f"Orange County's building safety page lists no separate concrete license category at all ({src('orange-bldg', 'Orange County Division of Building Safety')}). "
            "Osceola, Seminole, Lake and Sarasota counties' current local categories weren't confirmed from a page we could fetch "
            "directly, so a direct call to that county's contractor licensing office is the reliable way to settle it rather than "
            "assuming either way.</p>"),
        sec("How Do You Check Insurance and Workers' Comp, Not Just the License?",
            f"<p>A license search alone doesn't show current insurance coverage. Before a state certificate or registration issues "
            "or renews, an applicant has to file an affidavit confirming workers' compensation, public liability and property "
            f"damage insurance in board-set amounts ({src('fs489-115', 'F.S. 489.115')}). Rule 61G4-15.003 makes it a violation to "
            "stop carrying that coverage, but proof is checked through random board audits rather than posted publicly, so asking "
            f"a contractor directly for a current certificate of insurance is more reliable than assuming the license listing "
            f"covers it ({src('fac61g4-15-003', 'Fla. Admin. Code R. 61G4-15.003')}). Workers' compensation itself follows its own "
            "rule in construction: any employer with at least one employee is covered, up to three corporate officers who each own "
            f"10 percent or more of the business can file for an exemption, and an independent contractor on a construction job "
            f"generally counts as an employee for this purpose ({src('fs440-02', 'F.S. 440.02')}).</p>"),
        sec("What Happens If You Hire a Contractor Who Isn't Licensed for Work That Required One?",
            f"<p>Three consequences, and they mostly protect the homeowner rather than the contractor. An unlicensed contractor "
            f"can't enforce its own contract in court, though doing work in a scope that genuinely doesn't require a license (like "
            f"a stand-alone driveway) doesn't make someone \"unlicensed\" to begin with ({src('fs489-128', 'F.S. 489.128')}). An "
            f"unlicensed contractor also has no lien rights against the property, which cuts both ways for a homeowner weighing "
            f"risk ({src('fs713-02', 'F.S. 713.02')}). And the state's Homeowners' Construction Recovery Fund, which can "
            f"reimburse a homeowner for certain losses, only pays out for violations committed by a licensed contractor, so hiring "
            f"around licensing for a scope that needed one forfeits that backstop entirely ({src('fs489-1425', 'F.S. 489.1425')}). "
            f"Separately, state law requires a contractor's registration or certification number to appear on every bid, proposal "
            f"or advertisement it issues, in any medium ({src('fs489-119', 'F.S. 489.119')}); a written bid that's missing a "
            f"license number where one should appear, or an unlicensed business that claims to be licensed or insured, is grounds "
            f"for a local fine under the same statute.</p>"),
        sec("Say You're Checking Two Bids for a Patio Extension in St. Cloud",
            f"<p>A homeowner in {city('st-cloud')} comparing two concrete patio bids runs both business names through the "
            "DBPR license search first, noting whether either holds a certified (statewide) or registered (local-only) status, "
            "then calls Osceola County's building office directly since its current local licensing categories weren't something "
            "we could confirm from a published page. Both bids get asked for a current certificate of insurance rather than a "
            "verbal assurance, and both get checked for a printed license number, since a bid that's silent on that point either "
            f"doesn't need one for its scope or is skipping a requirement it should be meeting. {a('/concrete-patio-cost/', 'Our concrete patio cost guide')} "
            "covers where Florida market pricing lands for an extension that size.</p>"),
    ])
    faqs = [faq("Does a concrete contractor need a license in Florida?",
                "It depends on scope. Driveway installation on its own is exempt from state and local licensing requirements by name, while structural concrete tied to a foundation, footer or wall falls under the state's structural masonry specialty certificate. Running the business name through the DBPR license search, and asking directly which category applies to a specific job, settles it faster than guessing."),
            faq("How do I check a contractor's license in Florida?",
                "Use the DBPR license search at myfloridalicense.com, which returns the business's license status, type and any discipline history. A \"certified\" license is statewide; a \"registered\" license only covers the specific local jurisdictions it was issued for, which matters when comparing out-of-county bids."),
            faq("Does a paver contractor need a license in Florida?",
                "Pavers and patios aren't named in the state's driveway licensing exemption, and whether a given paver job falls under the structural masonry category is a judgment call the statute leaves open. Checking DBPR directly and asking the contractor which category, if any, covers the scope is the reliable approach rather than assuming either answer."),
            faq("What's the difference between a certified and a registered contractor?",
                "A certified contractor holds a state certificate of competency and can legally work anywhere in Florida. A registered contractor's standing comes from a local competency license and only covers the specific jurisdictions where that local license was issued, so a registered contractor from one county has no automatic standing in another."),
            faq("What happens if I hire an unlicensed contractor for work that needed a license?",
                "Three things, mostly protective of the homeowner: the contractor can't enforce its contract in court, it has no lien rights against the property, and the state's Homeowners' Construction Recovery Fund only reimburses losses caused by a licensed contractor, so that backstop isn't available. Checking DBPR before signing avoids finding this out after a dispute starts.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/paver-driveways/", "Paver driveways"),
               ("/blog/how-to-choose-a-concrete-contractor-orlando/", "How to choose a concrete contractor in Orlando"),
               ("/blog/how-to-choose-a-paver-contractor-sarasota/", "How to choose a paver contractor in Sarasota"),
               ("/blog/concrete-and-paver-warranty-what-it-should-cover/", "What a concrete or paver warranty should cover")]
    return page("/blog/florida-contractor-license-check-concrete-pavers/", "post",
                "Checking a Concrete or Paver Contractor's License",
                "Does a concrete or paver contractor need a license in Florida? How to check DBPR, county rules and insurance, as of October 2026.",
                "Does a Concrete or Paver Contractor Need a License in Florida? How to Check",
                capsule("A Florida concrete or paver contractor needs a license only for certain scopes: driveway installation is "
                        "exempt by name, while structural concrete tied to a foundation or wall needs the state's structural "
                        "masonry certificate. As of October 2026, the DBPR license search and a call to the county confirm what "
                        "applies to a specific job and whether local licenses still exist after 2025's statewide changes."),
                body, faqs=faqs,
                sources=["fs489-117", "fs489-105", "fac61g4-15-100", "dbpr-search", "fs163-211", "dbpr-hot", "md-preempt",
                         "manatee-lic", "orange-bldg", "fs489-115", "fac61g4-15-003", "fs440-02", "fs489-128", "fs713-02",
                         "fs489-1425", "fs489-119"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image=pid, form=False)


def p_concrete_and_paver_warranty_what_it_should_cover():
    pids = for_service("paver-driveways", 3)
    pid = pids[2] if len(pids) > 2 else (pids[0] if pids else None)
    body = "".join([
        sec("What Should a Concrete or Paver Warranty Actually Cover?",
            f"<p>A written warranty on {svc('concrete-driveways', 'concrete')} or {svc('paver-driveways', 'paver')} work should "
            "cover installation defects, not the material itself and not ordinary wear. That usually means settling or sinking "
            "traced back to the base, edge separation on a paver field, and cracking in concrete beyond a stated width threshold. "
            "What it typically excludes matters just as much: tree root damage, storm and flood events, heavy vehicle loads the job "
            "wasn't built for, and skipped maintenance like sealing. Getting both halves, what's in and what's out, spelled out in "
            "writing is the point; a warranty that only promises to \"stand behind the work\" without defining either side isn't "
            "worth much if a dispute comes up later.</p>"),
        sec("What's the Difference Between a Manufacturer Warranty and a Workmanship Warranty?",
            f"<p>Two different documents cover two different risks. A manufacturer warranty, where one exists, covers defects in "
            "the paver units themselves, color consistency, strength, freeze-thaw performance in climates that see it, and it "
            "comes from the paver maker, not the installer. A workmanship warranty is the installer's own promise about how the "
            "job was built: base depth, compaction, edge restraint, joint spacing. Industry buyer guides describe a roughly 2 to 3 "
            "year workmanship warranty as standard practice among ICPI-certified paver installers, covering settlement, edge "
            f"failure and jointing failure specifically ({ext('https://hmndp.org/hardscape-contractor-vetting/', 'HMNDP Landscaping, hardscape contractor vetting guide')}). "
            "Poured concrete generally has no separate \"manufacturer\" to warranty the slab itself, so the installer's own "
            "workmanship warranty is the only document covering the work, which makes its wording worth reading closely rather "
            "than assuming it matches a paver job's split.</p>"
            + (photo(pid, "Close-up top-down view of gray interlocking zigzag-shaped concrete pavers fitted tightly together.") if pid else "")),
        sec("What Does a Paver Warranty Usually Cover, and for How Long?",
            f"<p>Settling and sinking tied to the compacted base, rather than to the paver units themselves, sits at the center of "
            "most paver workmanship warranties, since a base that was built short of spec is the installer's responsibility to "
            "correct. Edge or joint separation, where the restraint holding the field's perimeter fails and pavers start to "
            "spread, is the other common item. Asking what happens if a section needs to come up and be re-leveled, rather than "
            f"just whether it's \"covered,\" clarifies whether the fix is a quick re-level or a bigger tear-out. {post('why-pavers-sink-in-florida', 'Our guide to why pavers sink in Florida')} "
            "covers the underlying causes a warranty like this is meant to address.</p>"),
        sec("What Does a Concrete Warranty Usually Cover?",
            "<p>Cracking beyond a stated width, rather than cracking in general, is the more honest way a concrete warranty is "
            "usually written, since a slab is engineered to crack at its control joints by design. An example seen on one "
            "contractor's published warranty page sets the line at cracks exceeding a quarter inch in width within the first year "
            f"as the threshold for a covered repair, with ordinary hairline shrinkage cracking excluded ({ext('https://www.mattinglyconcrete.com/warranty-information/', 'Mattingly Concrete, 1-Year Limited Warranty')}). "
            "Standing water that persists on the surface well past a rain event is another common item, since a slab that wasn't "
            f"sloped correctly for drainage is a workmanship question, not a maintenance one. {post('concrete-driveway-cracks-florida', 'Our guide to why concrete driveways crack')} "
            "walks through which cracks are considered normal versus which ones point to an underlying problem.</p>"),
        sec("What Do Written Warranties Typically Exclude?",
            "<p>Acts of nature sit at the top of nearly every warranty's exclusion list: storms, flooding, and earth movement the "
            "installer had no control over. Damage traced to tree roots growing into a base after the fact is another common "
            f"exclusion, since it's a site condition that developed after the work was finished rather than a flaw in how it was "
            f"built ({post('tree-roots-under-driveway-florida', 'our guide to tree roots under a driveway')} covers that specific "
            "problem). Heavy or commercial vehicle loads the job wasn't designed for, surface wear like spalling or color fading, "
            "and skipped maintenance, a sealer that was never reapplied on the schedule the contract specified, round out the "
            "common list. A warranty that names these exclusions explicitly is easier to work with than one that stays vague, "
            "since vague language tends to get interpreted against whoever wrote it when a dispute actually happens.</p>"),
        sec("Does Florida Law Offer Any Protection Beyond a Contractor's Own Warranty?",
            f"<p>Yes, but it depends on licensing status. The state's Homeowners' Construction Recovery Fund can reimburse a "
            "homeowner for certain losses caused by specified violations, but only when the contractor responsible held a valid "
            f"license for the scope of work at the time ({src('fs489-1425', 'F.S. 489.1425')}). That's a separate backstop from "
            "the contractor's own written warranty, not a substitute for one, and it only exists at all if the business was "
            f"licensed for a scope that required a license in the first place. {post('florida-contractor-license-check-concrete-pavers', 'Our guide to checking a Florida contractor license')} "
            "covers how to confirm that status before signing.</p>"),
        sec("What Should Be in Writing Before You Sign?",
            "<p>A duration, in years or months rather than \"a reasonable time.\" A crack-width or settlement threshold that "
            "triggers a covered repair, rather than a promise to \"stand behind the work.\" A list of what's excluded, named "
            "directly instead of left to be argued about later. Whether the warranty transfers to a new owner if the home sells "
            "within the coverage window, since that detail affects resale conversations years down the line. And who's actually "
            "responsible if part of the job was subcontracted, the general contractor named on the bid or the subcontractor who "
            f"physically did the work. {post('how-to-compare-concrete-and-paver-quotes', 'Our guide to comparing concrete and paver quotes')} "
            "covers how warranty language fits alongside the rest of a written bid.</p>"),
        sec("Say You're Comparing Warranty Language on Two Paver Patio Bids in Parrish",
            f"<p>A homeowner in {city('parrish')} reading two paver patio bids side by side notices that one spells out a 2 year "
            "workmanship warranty covering settlement and edge separation, with tree root damage and storm events named as "
            "exclusions, while the other simply states the work is \"guaranteed\" with no duration or scope attached. The second "
            "bid isn't necessarily a worse job, but the vague language means there's nothing to point to if a section settles 18 "
            "months in, which is reason enough to ask for the same specificity the first bid already provides before signing "
            "either one.</p>"),
    ])
    faqs = [faq("How long should a paver workmanship warranty last?",
                "Industry buyer guides describe roughly 2 to 3 years as standard practice among ICPI-certified installers, covering settlement, edge failure and joint separation specifically. Shorter or longer terms both exist in practice; the more important question is whether the warranty names a specific duration and specific covered items rather than a vague promise."),
            faq("Does a concrete warranty cover all cracking?",
                "Usually not, and it shouldn't, since a slab is designed to crack at its control joints. Written warranties more often set a width threshold, such as cracks exceeding a quarter inch within the first year, as the trigger for a covered repair, with ordinary hairline shrinkage cracking excluded from coverage."),
            faq("Is a paver warranty the same as the manufacturer's warranty?",
                "No. A manufacturer warranty, where one exists, covers defects in the paver units themselves. A separate workmanship warranty from the installer covers how the job was built: base depth, compaction and edge restraint. Asking for both documents in writing avoids assuming one covers what the other doesn't."),
            faq("What does the Florida Homeowners' Construction Recovery Fund cover?",
                "It can reimburse a homeowner for certain losses caused by specified violations, but only when the responsible contractor held a valid license for that scope of work. It's a backstop separate from a contractor's own written warranty, not a replacement for getting warranty terms in writing."),
            faq("Do warranties cover damage from tree roots?",
                "Typically not. Tree root damage that develops after installation is a common exclusion in both concrete and paver warranties, since it's treated as a site condition rather than a flaw in the original work. A root barrier installed up front is a prevention question, not a warranty one.")]
    related = [("/paver-driveways/", "Paver driveways"), ("/concrete-driveways/", "Concrete driveways"),
               ("/paver-patios/", "Paver patios & walkways"),
               ("/blog/florida-contractor-license-check-concrete-pavers/", "Checking a Florida contractor's license"),
               ("/blog/how-to-compare-concrete-and-paver-quotes/", "Comparing concrete and paver quotes")]
    return page("/blog/concrete-and-paver-warranty-what-it-should-cover/", "post",
                "Reading a Concrete or Paver Warranty",
                "What a concrete or paver warranty should and shouldn't cover: manufacturer vs. workmanship terms, exclusions and Florida law, October 2026.",
                "What a Concrete or Paver Warranty Should (and Shouldn't) Cover",
                capsule("A concrete or paver warranty should spell out a duration, a specific defect it covers, such as settling "
                        "beyond a stated threshold or cracking past a stated width, and named exclusions like tree roots and storm "
                        "damage. As of October 2026, a separate manufacturer warranty on paver units and Florida's Homeowners' "
                        "Construction Recovery Fund offer additional, narrower protection alongside it."),
                body, faqs=faqs,
                sources=["fs489-1425",
                         ("HMNDP Landscaping, hardscape contractor vetting guide (Jun. 16, 2026)", "https://hmndp.org/hardscape-contractor-vetting/"),
                         ("Mattingly Concrete, 1-Year Limited Warranty", "https://www.mattinglyconcrete.com/warranty-information/")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image=pid, form=False)


def p_how_to_compare_concrete_and_paver_quotes():
    body = "".join([
        sec("Why Do Estimates for the Same Driveway or Patio Vary So Much?",
            f"<p>Two bids for what looks like the same {svc('concrete-driveways', 'concrete')} or {svc('paver-patios', 'paver')} "
            "job usually differ because they're not actually describing the same job: base depth, demolition scope, reinforcement "
            "and permit handling all swing the number without changing the square footage on paper. A quote several thousand "
            "dollars lower than the rest is far more often a thinner base or a missing haul-off fee than it is a better deal, which "
            "is why comparing bids by the line item, not just the bottom line, matters more than it seems like it should.</p>"),
        sec("What Line Items Should Every Concrete or Paver Quote Include?",
            "<p>A number without the specification behind it can't be compared to anything. The table below lists what a complete "
            "quote spells out, whether it's concrete or pavers, so two bids can actually be checked against each other rather than "
            "judged on price alone.</p>"
            + table("What belongs in a written concrete or paver quote", ["Line item", "What to look for"],
                    [["Area and layout", "Exact dimensions and square footage, not a round estimate"],
                     ["Demolition and haul-off", "Named as its own line, not folded silently into the total"],
                     ["Base depth and compaction target", "A specific number in inches and a percentage, not \"compacted base\" alone"],
                     ["Slab thickness and reinforcement, or paver thickness", "4 in. standard vs. 6 in. for vehicle loads; 60 mm vs. 80 mm pavers"],
                     ["Control joint spacing (concrete) or edge restraint (pavers)", "Governs where a slab cracks or whether a paver field holds its line"],
                     ["Finish", "Broom, stamped, exposed aggregate, or paver pattern and color"],
                     ["Sealing", "Named as included or priced separately, not assumed either way"],
                     ["Permit handling", "States who applies for it and who pays the fee"],
                     ["Deposit amount and payment schedule", "Tied to completed stages rather than one large sum up front"],
                     ["Warranty terms", "A duration and named coverage, not just \"guaranteed\""]],
                    "General comparison checklist; not every item applies to every job size.")),
        sec("How Do You Compare Two Quotes for the Same Square Footage?",
            f"<p>Say a 400 sq ft concrete driveway gets two bids. Quote A comes in around " + price("concrete-driveway", typical=True) +
            f" per {per('concrete-driveway')}, specifies a 4 in. slab on a 4 in. compacted base, and lists haul-off of the old "
            "driveway as a separate $1,200 line. Quote B comes in noticeably lower, closer to the bottom of the full " +
            price("concrete-driveway") + f" per {per('concrete-driveway')} range, but the written scope just says \"remove and "
            "replace\" with no base depth given and no mention of where the old concrete goes. On paper, B looks like the better "
            "number; once the base spec and haul-off are priced into A's total and B's missing details are asked about directly, "
            "the gap usually narrows or disappears. The dollar figures here are illustrative, not a quote either homeowner "
            "actually received; the method, pricing the same scope before comparing totals, is what carries over to a real bid.</p>"),
        sec("What Base and Thickness Numbers Need to Match Before You Compare Price?",
            f"<p>Square footage alone isn't enough to put two numbers side by side. A driveway quote built on a thinner base or "
            "lighter reinforcement than its competitor will always look cheaper per square foot and will usually perform worse "
            "over time, so normalizing both bids to the same base depth, same slab thickness or paver class, and same finish "
            "before comparing dollar figures is the step that actually makes the comparison honest. For pavers specifically, "
            f"60 mm units suit a patio while 80 mm units are built for driveway loads; pricing two bids against different paver "
            f"thicknesses isn't really comparing the same job at all.</p>"),
        sec("What Permit and Paperwork Details Belong in Every Quote?",
            f"<p>A quote should state plainly who's applying for any required permit and who's paying the fee, since that's not a "
            "detail to discover after signing. Florida law also requires a contractor's license number to appear on every bid, "
            f"proposal or advertisement it issues, so a written quote that should carry a license number and doesn't is worth a "
            f"direct question ({src('fs489-119', 'F.S. 489.119')}). On the money side, a deposit above 10 percent of the contract "
            "price puts the contractor on a 30-day clock to apply for permits and a 90-day clock to start work once they issue, "
            f"under the same statewide rule regardless of which trade is doing the work ({src('fs489-126', 'F.S. 489.126')}), and "
            "a job over $2,500 also calls for a recorded Notice of Commencement, signed by the property owner, before the first "
            f"day of work ({src('fs713-13', 'F.S. 713.13')}). A bid that mentions none of this isn't automatically a problem, but it's worth "
            "raising directly rather than assuming it was simply left off the page.</p>"),
        sec("What Counts as a Red Flag in a Quote?",
            "<p>A handful of patterns show up often enough to be worth naming directly: a cash-only arrangement with nothing in "
            "writing, a deposit near half the contract price with no stage-based schedule behind it, a base description that says "
            "\"compacted\" without a depth number attached, and a total that's missing demolition or haul-off as its own line. "
            "None of these guarantees a bad outcome by itself, but together they're the pattern behind most disputes that end up "
            "in a dollar-for-dollar argument partway through a job rather than settled in writing before it started.</p>"),
        sec("Say You're Comparing Three Paver Patio Bids in Winter Park",
            f"<p>A homeowner in {city('winter-park')} collecting three bids for a paver patio lines up base depth, edge restraint "
            "spec and finish first, before looking at the total on any of them. One bid specifies 6 in. of compacted aggregate "
            "under the pavers and a spiked edge restraint along the full perimeter; a second lists \"standard base\" with no "
            "number; the third is priced closest to the middle but includes polymeric sand for the joints where the other two "
            f"don't say either way. Calling the second bidder to get a real base number, and confirming whether joint sand is "
            f"included on the other two, turns three numbers that aren't really comparable into a fair comparison. {a('/paver-patio-cost/', 'Our paver patio cost guide')} "
            "covers where Florida market pricing typically lands for a patio that size.</p>"),
    ])
    faqs = [faq("Why do estimates for the same driveway vary so much?",
                "Because the bids usually aren't describing the same job underneath the same number. Base depth, demolition and haul-off, reinforcement, permit handling and deposit structure all move the price independently of square footage, so a lower bid is far more often a thinner spec than a better deal. Comparing the line items, not just the total, is what explains the gap."),
            faq("Is the lowest quote usually the best deal?",
                "Not reliably. The lowest number on a page often turns out to specify a thinner base, skip the haul-off fee, or leave reinforcement and joint sand unmentioned, none of which shows up until the written scopes are compared side by side. A fair price for a thinner job isn't the same thing as a good price for the job actually wanted."),
            faq("Should every quote include a written base depth?",
                "Yes. A base depth and compaction target in writing, not just the word \"compacted\" on its own, is one of the few numbers that reliably explains why two bids for the same square footage land at different prices. A contractor unwilling to put a number on it is worth a direct follow-up question before signing."),
            faq("What permit information should appear on a quote?",
                "Who's applying for any required permit and who's paying the fee, stated plainly rather than left for later. Florida law also requires a license number on every bid or advertisement where one applies, so its absence on a bid that should carry one is worth asking about directly."),
            faq("What's a red flag in a concrete or paver quote?",
                "A cash-only arrangement with nothing in writing, a deposit near half the contract price with no stage-based schedule, a base description with no depth number attached, and a total missing demolition or haul-off as its own line. None proves a bad outcome alone, but together they're the pattern behind most disputes.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/paver-driveways/", "Paver driveways"),
               ("/paver-patios/", "Paver patios & walkways"),
               ("/blog/florida-contractor-license-check-concrete-pavers/", "Checking a Florida contractor's license"),
               ("/blog/concrete-and-paver-warranty-what-it-should-cover/", "What a concrete or paver warranty should cover")]
    return page("/blog/how-to-compare-concrete-and-paver-quotes/", "post",
                "Comparing Concrete and Paver Contractor Quotes",
                "How to compare concrete and paver quotes line by line: base depth, permits, deposits and red flags, as of October 2026.",
                "How to Compare Concrete and Paver Quotes Line by Line",
                capsule("Comparing concrete or paver quotes means checking the line items behind the total: base depth, "
                        "demolition and haul-off, reinforcement or paver thickness, joint spacing and permit handling. As of "
                        "October 2026, a quote missing a written base depth or a required license number is worth a direct "
                        "question before a lower price gets mistaken for a better deal."),
                body, faqs=faqs,
                sources=["fs489-119", "fs489-126", "fs713-13"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image=None, form=False)


def p_does_a_new_driveway_add_home_value():
    pids = for_service("paver-driveways", 1)
    pid = pids[0] if pids else None
    body = "".join([
        sec("Does a New Driveway, Patio or Pool Deck Add Home Value?",
            f"<p>Nationally, the best-documented figure is for patios, not driveways: a 2023 REALTORS® survey estimated "
            "homeowners recover about 95 percent of the cost of a new paver patio at resale. No comparably rigorous national study "
            "was found isolating a driveway or a pool deck on its own; appraisers and buyers clearly weigh both, condition and "
            "curb appeal show up repeatedly in survey data, but no single recovered-percentage figure exists for either the way it "
            "does for a patio.</p>"),
        sec("What Does the Most Reliable National Data Say About Patios?",
            "<p>The National Association of REALTORS® and the National Association of Landscape Professionals published a "
            "joint 2023 report specifically on outdoor remodeling projects, and the patio project it priced is worth noting "
            "because it's built the same way our paver patios are: an 18 by 16 ft paver patio, dry-set over a compacted gravel and "
            f"sand base. Landscape professionals estimated the national cost at $10,500; REALTORS® estimated $10,000 "
            f"recovered at resale, 95 percent of the cost, with a Joy Score of 9.9 out of 10 among owners who'd completed the "
            f"project ({ext('https://cms.nar.realtor/sites/default/files/documents/2023-03-remodeling-impact-outdoor-features-03-17-2023.pdf', 'NAR/NALP, 2023 Remodeling Impact Report: Outdoor Features')}). "
            "The same report surveyed REALTORS® directly on curb appeal: 92 percent said they'd recommended a seller improve "
            "curb appeal before listing, and 97 percent called it important to attracting a buyer. A comparable project in the "
            "same report, installing a pool rather than resurfacing an existing pool deck, recovered only about 56 percent, which "
            "is a reminder that \"outdoor project\" covers a wide range of outcomes and a pool addition isn't the same thing as a "
            "deck replacement.</p>"
            + table("Selected projects, 2023 NAR/NALP Remodeling Impact Report", ["Project", "National cost estimate", "Percent recovered at resale"],
                    [["New patio (paver, 18x16 ft)", "$10,500", "95%"],
                     ["Outdoor kitchen", "not itemized in the summary table", "100%"],
                     ["New wood deck", "not itemized in the summary table", "89%"],
                     ["Overall landscape upgrade", "not itemized in the summary table", "100%"],
                     ["In-ground pool addition", "not itemized in the summary table", "56%"]],
                    "National figures, not Florida-specific; no comparable line item exists in this report for a driveway or a pool-deck resurface.")),
        sec("Does a Driveway Specifically Add Value, and How Do Appraisers Treat It?",
            f"<p>Appraisers do factor a driveway into the overall condition picture, even without a published recovered-percentage "
            "figure to point to the way the patio data above gives one. One national home-buying company's published guide to "
            "appraisal factors lists driveway condition and type among the exterior items appraisers note, stating plainly that "
            f"\"paved driveways are valued higher than gravel\" and that \"cracks and deterioration are noted\" "
            f"({ext('https://www.opendoor.com/articles/items-that-increase-your-home-appraisal-value-what-appraisers-actually-look-for', 'Opendoor, items that increase home appraisal value')}). "
            "That lines up with what the same NAR survey found about curb appeal generally: 98 percent of REALTORS® said curb "
            "appeal matters to a potential buyer, with 63 percent calling it very important. A cracked or visibly patched "
            "driveway is the kind of thing that factors into that impression even without its own dollar figure attached to it. "
            f"{post('concrete-driveway-cracks-florida', 'Our guide to driveway cracks')} covers which cracks are cosmetic versus "
            "which point to a bigger problem worth addressing before a home goes on the market.</p>"),
        sec("What About a Pool Deck Specifically?",
            "<p>No national study was found that isolates a pool deck resurface or replacement from the pool itself, so there's no "
            "reliable recovered-percentage figure to cite here the way the patio data above provides one. What does show up "
            "consistently in buyer behavior, even without a dollar figure attached, is that a cracked, spalling or badly stained "
            "deck surrounding a pool reads as deferred maintenance to a buyer touring the home, in a way that colors the "
            f"impression of the pool itself. {post('should-you-seal-a-concrete-driveway-florida', 'Our guide to sealing concrete')} "
            "and " + post('how-hot-do-pool-decks-get-florida', 'our guide comparing pool deck surfaces') + " cover the condition "
            "and comfort side of that question, which is a separate thing from resale value but tends to move together with it in "
            "practice.</p>"),
        sec("Does the Material, Pavers or Concrete, Change the Resale Picture?",
            "<p>No study comparing paver and concrete resale outcomes directly was found, for a driveway, patio or pool deck. "
            "The one solid data point available, the NAR/NALP patio figure above, happens to describe a paver patio specifically, "
            "which is worth knowing if the question is which material that particular survey was measuring, but it isn't evidence "
            "that pavers outperform concrete at resale generally. Absent a comparative study, condition, consistency with the "
            f"rest of the home's finishes, and the quality of the installation itself are the factors buyers and appraisers "
            "actually respond to, regardless of which material is underfoot.</p>"),
        sec("Say You're Weighing a Driveway Replacement Before Listing a Home in Sanford",
            f"<p>A homeowner in {city('sanford')} planning to list within the year weighs a cracked, patched driveway against the "
            "cost of replacing it, knowing there's no single study to point to that says exactly how many dollars a new driveway "
            "adds at closing. What's better documented is the softer side of the decision: a driveway in visibly poor condition "
            "gets noted by an appraiser and registers with a buyer walking up to the front door before they've seen anything else "
            f"about the house. {a('/concrete-driveway-cost/', 'Our concrete driveway cost guide')} and "
            f"{a('/paver-driveway-cost/', 'our paver driveway cost guide')} cover where Florida market pricing lands for a "
            "driveway replacement of a given size.</p>"),
    ])
    faqs = [faq("Do pavers add value to a home?",
                "The best national data available, a 2023 REALTORS® and landscape professionals survey, measured a paver patio specifically and found about 95 percent of its cost recovered at resale. No comparable study measures a paver driveway on its own, so while condition and curb appeal clearly matter to appraisers and buyers, there's no single recovered-percentage figure to cite for a driveway the way the patio data provides."),
            faq("Does a new driveway increase home value?",
                "There's no single national study isolating a driveway's resale value the way one exists for patios, but appraisers do note driveway condition and type directly, with paved driveways valued higher than gravel and cracks or deterioration factored into the overall impression. Replacing a visibly cracked driveway before listing is more about curb appeal and appraiser notes than a documented dollar return."),
            faq("Does a new patio pay for itself at resale?",
                "National data from a 2023 REALTORS® survey put the recovered value at about 95 percent of a paver patio's cost, among the higher-recovery outdoor projects measured in that report. That's a national figure, not a Florida-specific one, and actual recovery depends on the home's price point and local market."),
            faq("Is a paver driveway worth more at resale than a concrete driveway?",
                "No study comparing the two materials' resale outcomes directly was found. Condition, consistency with the rest of the home's finishes and installation quality appear to matter more to buyers and appraisers than which material was used, based on the available survey data on curb appeal generally."),
            faq("Does resurfacing a pool deck add resale value?",
                "No national study was found that isolates pool deck condition from the pool itself in resale terms. What's documented is that buyers and appraisers respond to visible condition and curb appeal broadly, so a deteriorated deck surrounding an otherwise well-kept pool is the kind of detail that shapes a buyer's overall impression even without its own dollar figure attached.")]
    related = [("/paver-driveways/", "Paver driveways"), ("/concrete-driveways/", "Concrete driveways"),
               ("/pool-deck-pavers/", "Pool deck pavers"),
               ("/blog/concrete-driveway-cracks-florida/", "Why concrete driveways crack"),
               ("/concrete-driveway-cost/", "Concrete driveway cost")]
    return page("/blog/does-a-new-driveway-add-home-value/", "post",
                "Do Driveways and Patios Add Home Value?",
                "Does a new driveway, patio or pool deck add home value in Florida? What the 2023 NAR/NALP data actually shows, October 2026.",
                "Does a New Driveway, Patio or Pool Deck Add Home Value in Florida?",
                capsule("A 2023 national REALTORS® and landscape professionals survey found about 95 percent of a new paver "
                        "patio's cost recovered at resale, the best-documented figure available. As of October 2026, no "
                        "comparable study isolates a driveway or pool deck specifically, though appraisers note driveway "
                        "condition directly and curb appeal matters to most buyers surveyed."),
                body, faqs=faqs,
                sources=[("NAR/NALP, 2023 Remodeling Impact Report: Outdoor Features", "https://cms.nar.realtor/sites/default/files/documents/2023-03-remodeling-impact-outdoor-features-03-17-2023.pdf"),
                         ("Opendoor, items that increase home appraisal value (updated Mar. 11, 2026)", "https://www.opendoor.com/articles/items-that-increase-your-home-appraisal-value-what-appraisers-actually-look-for")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-driveways",
                image=pid, form=False)


def p_how_to_budget_a_backyard_hardscape_project_in_phases():
    pids = for_service("retaining-walls", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("How Do You Budget a Backyard Hardscape Project in Phases?",
            f"<p>Phasing a backyard that will eventually include {svc('retaining-walls', 'a retaining wall')}, "
            f"{svc('paver-patios', 'a paver patio')} and {svc('artificial-turf', 'turf')} works best when the structural and "
            "grading work goes first, the patio or walkway goes second, and turf or planting goes last, even if the whole project "
            "is spread across two or three budget cycles. Building in that order avoids the common mistake of finishing a patio "
            "early, then discovering a later retaining wall needs to disturb the grade right next to it.</p>"),
        sec("What Should Be Designed Before Phase One Even Starts?",
            f"<p>A full-yard concept plan, even a rough one, before the first shovel goes in anywhere. Submitting that whole "
            "concept for any required HOA or architectural review up front, rather than resubmitting piece by piece as each phase "
            "gets built, saves a round of paperwork later, and a 2026 change to Florida law means an association can't hold a "
            "building permit over a homeowner's head as a condition of even starting that review, so the design and the permit "
            f"process can move together rather than one waiting on the other ({src('fs720-3035', 'F.S. 720.3035')}). "
            f"{post('hoa-approval-for-pavers-and-concrete', 'Our guide to HOA approval for pavers and concrete')} covers what a "
            "typical architectural review packet asks for.</p>"
            + (photo(pid, "A modular concrete crib-style retaining wall with gravel fill, built into a grassy slope.") if pid else "")),
        sec("Which Comes First: A Retaining Wall, a Patio or Turf?",
            "<p>Structural and drainage work first, because it changes the grade everything else sits on. A retaining wall moves "
            "soil and often redirects water, so building it after a patio is already poured risks undermining or flooding "
            "the finished surface. Hardscape, a patio or walkway, comes second, since it needs a stable, already-graded base to "
            "sit on. Turf comes last by default, not because it's less important, but because it has no multi-day cure to protect "
            "and its washed-rock base is quick to tie into finished hardscape edges once everything around it is already in "
            "place.</p>"
            + table("A typical phase order and budget band", ["Phase", "Typical driver", "Florida market range"],
                    [["1. Retaining wall and grading", "Changes the grade; often needed before anything else can be built level",
                      price("retaining-wall") + " per " + per("retaining-wall")],
                     ["2. Paver patio or walkway", "Needs a stable, already-graded surface to sit on",
                      price("paver-patio") + " per " + per("paver-patio")],
                     ["3. Artificial turf", "No multi-day cure; ties into finished hardscape edges last",
                      price("artificial-turf") + " per " + per("artificial-turf")]],
                    "Florida market ranges, October 2026; a site visit prices a specific yard's conditions.")),
        sec("How Do You Avoid Rework Between Phases?",
            f"<p>Sleeving conduit for future lighting or an irrigation line under a patio before it's poured, even if that wiring "
            "won't go in until phase two or three, is far cheaper than cutting into finished pavers or a slab later to add it. "
            "Matching the compaction and base depth between adjoining phases keeps the transition from settling unevenly where one "
            "section meets the next, which otherwise shows up as a visible dip at the seam a year or two in. Keeping the same "
            "contractor, or at least sharing the first phase's as-built drawings with whoever does the next one, also avoids a "
            "second crew guessing at what's buried where the first phase left off.</p>"),
        sec("How Do Permits and Deposits Work Across Multiple Phases?",
            f"<p>Each phase is generally its own contract, which means Florida's lien-law thresholds apply separately to each one "
            "rather than to the project as a whole. A Notice of Commencement has to be recorded before work starts on any single "
            f"phase priced over $2,500, even if an earlier phase already had its own ({src('fs713-13', 'F.S. 713.13')}). The same "
            "logic applies to deposits: a deposit over 10 percent of a given phase's contract price starts that phase's own "
            f"30-day permit-filing clock, independent of what happened on the phase before it ({src('fs489-126', 'F.S. 489.126')}). "
            "Treating each phase as its own contract, with its own paperwork, is more accurate than assuming one set of "
            "documents from the first phase covers everything that follows.</p>"),
        sec("Say You're Phasing a Backyard in Davenport: Wall, Patio, Then Turf Over Three Years",
            f"<p>A homeowner in {city('davenport')} with a sloped backyard budgets a segmental retaining wall for year one, since "
            "the slope has to be addressed before anything else can sit level behind it, then a paver patio for year two once the "
            "graded area behind the wall has settled, and artificial turf for the remaining lawn in year three. Each phase gets "
            "priced and contracted separately, with its own deposit and, where the price passes $2,500, its own Notice of "
            "Commencement, and the original full-yard concept plan from year one keeps the patio's edge and the eventual turf "
            f"border lining up rather than being designed in isolation three years apart. {a('/retaining-wall-cost/', 'Our retaining wall cost guide')} "
            "covers where Florida market pricing lands for a wall sized to a given slope.</p>"),
    ])
    faqs = [faq("Should you design the whole backyard before building the first phase?",
                "A rough full-yard concept plan before phase one starts is worth the extra step, even if only a fraction of it gets built right away. It keeps a later phase from conflicting with grading or edges already finished, and submitting the whole concept for any HOA review up front can save a round of paperwork compared to resubmitting piece by piece."),
            faq("Does a retaining wall need to go in before a patio?",
                "Generally yes, when both are part of the same yard. A retaining wall changes the grade and often redirects water, so building it after a patio is already poured risks undermining or flooding the finished surface. Structural and grading work typically comes first for that reason."),
            faq("Can artificial turf be added years after a patio is finished?",
                "Yes, and it's often the easiest phase to add later, since turf has no multi-day cure to protect and its base ties into existing hardscape edges without disturbing what's already built. Matching the original edge line and grade from the design plan keeps the later phase looking intentional rather than added on."),
            faq("Does each phase of a multi-year project need its own Notice of Commencement?",
                "Yes, if each phase is contracted separately and priced over $2,500. Florida's lien-law threshold applies per contract, not per overall project, so a phase built two years after the first one still needs its own Notice of Commencement recorded before work starts."),
            faq("What's typically the most expensive phase of a backyard hardscape project?",
                "It depends on scope, but a retaining wall usually carries the highest per-square-foot cost of the three, since it's priced by wall face rather than footprint and often includes engineering on taller sections. A patio or turf phase covering more area can still cost more in total even at a lower per-square-foot rate.")]
    related = [("/paver-patios/", "Paver patios & walkways"), ("/artificial-turf/", "Artificial turf"),
               ("/retaining-walls/", "Retaining walls"),
               ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA approval for pavers and concrete"),
               ("/retaining-wall-cost/", "Retaining wall cost")]
    return page("/blog/how-to-budget-a-backyard-hardscape-project-in-phases/", "post",
                "Budgeting a Backyard Project in Phases",
                "How to budget a backyard hardscape project in phases: what order to build a wall, patio and turf, as of October 2026.",
                "How to Budget a Backyard Hardscape Project in Phases",
                capsule("Budgeting a backyard hardscape project in phases works best when structural work, a retaining wall or "
                        "grading, goes first, a patio or walkway goes second, and turf goes last, since turf has no cure to "
                        "protect and ties into finished edges easily. As of October 2026, each phase priced over $2,500 needs "
                        "its own Notice of Commencement under Florida law."),
                body, faqs=faqs,
                sources=["fs720-3035", "fs713-13", "fs489-126"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-patios",
                image=pid, form=False)


def get_pages():
    return [p_how_to_choose_an_artificial_turf_installer(), p_florida_contractor_license_check_concrete_pavers(),
            p_concrete_and_paver_warranty_what_it_should_cover(), p_how_to_compare_concrete_and_paver_quotes(),
            p_does_a_new_driveway_add_home_value(), p_how_to_budget_a_backyard_hardscape_project_in_phases()]
