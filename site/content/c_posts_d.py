# -*- coding: utf-8 -*-
"""Blog posts, module c_posts_d: artificial turf in Florida rain/flooding/hurricanes, and county-by-county
driveway/patio/paver permit guides for Orange, Osceola, Seminole, and Lake/Polk counties (Orlando unit) plus
Sarasota County (Sarasota unit). See research/blog-plan.csv for the plan and research/questions.csv for the
owned questions. Manatee County and the generic HOA/ARC posts belong to a different module."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, cs, post, compare, src, ext, photo


def artificial_turf_rain_and_storms():
    body = "".join([
        sec("Does Artificial Turf Hold Up to Florida Rain, Flooding and Hurricanes?",
            "<p>Yes, when it is built on a drainage-first base: a permeable backing, a washed and compacted stone sub-base, and a slope that carries water off the panel rather than letting it pool. Florida's 2026 turf rule makes most of that mandatory rather than optional, and the practical risk in a storm is less about the turf itself and more about what sits underneath it and around its edges.</p>"
            f"<p>{svc('artificial-turf')} covers how we build lawns, pet areas and putting greens for this climate; this post focuses specifically on how turf behaves in heavy rain, standing water and named storms, which a general installation page does not cover in depth.</p>"
            + (photo("turf-pavers-pool", "Bright green artificial turf bordered by large concrete pavers in a backyard that slopes gently toward a drain.") or "")),
        sec("What Goes Under Turf That Keeps It From Flooding?",
            f"<p>Florida's synthetic turf rule, DEP Rule 62-308.100, took effect May 19, 2026 and sets the base and drainage standard statewide: the subgrade must be \"composed of natural materials, such as crushed rock, or crushed concrete,\" washed before installation \"to prevent fines from binding,\" with the turf and its backing kept permeable over a pervious subgrade ({src('rule62-308-100-text', 'Rule 62-308.100')}). A local government may set a stricter permeability number, up to a ceiling of 10 inches of water per hour through every layer, but it cannot go below the state floor. The rule also requires the site to be graded for positive drainage and bars soil compaction tight enough to choke that percolation.</p>"
            "<p>That base is what separates turf that sheds a downpour from turf that holds it. A crushed, washed aggregate base drains between the stones; a base built from unwashed fill or ordinary dirt clogs with fines and starts to seal the way a driveway sub-base is meant to, which is the opposite of what turf needs underneath it.</p>"),
        sec("Can Turf Flood During a Hurricane or a Heavy Summer Storm?",
            f"<p>A yard can flood regardless of its surface, and turf does not drain floodwater away any faster than grass does once the ground underneath is already saturated. What the state rule controls is whether turf makes that worse. It bars installing turf \"within a swale, ditch, stormwater pond, or a stormwater pond's littoral zone,\" and it says turf \"must not increase runoff volume or rates\" onto a neighbor's property or alter a permitted stormwater system ({src('rule62-308-100-text', 'Rule 62-308.100')}). Orlando's airport gauge averages 51.45 inches of rain a year and Sarasota-Bradenton's averages 49.05, with June through September each running well over 6 inches a month at both stations ({src('ncei-annual-prcp', 'NOAA NCEI 1991-2020 normals')}). NWS Melbourne puts the median start of wet season at May 27 for Central Florida, and NWS Tampa Bay runs it roughly mid-May to mid-October for the Suncoast ({src('nws-mlb-wetdry', 'NWS Melbourne')}; {src('nws-tbw-tstm-climo', 'NWS Tampa Bay')}). A base and grading plan sized for that rainfall, not just an average year, is what keeps a turf lawn from becoming the low spot in a yard.</p>"),
        sec("Will Turf Seams Lift or the Infill Wash Away in a Storm?",
            f"<p>Both are real risks if the install skipped the state's anchoring and infill rules, not an inherent flaw in the material. The DEP rule requires installers to \"anchor all edges and seams against wind and flooding\" and to install infill so that it does not wash off the property during heavy rain ({src('rule62-308-100-text', 'Rule 62-308.100')}). Infill itself is limited statewide to clean silica sand, rock, shell or coated silica sand, and it has to stay on site rather than migrate into a storm drain or a neighbor's yard. A seam that was glued and nailed properly along the base, with infill swept in at the right depth, is what keeps a panel from curling at the edge when water runs across it during a downpour.</p>"),
        sec("Low-Lying Lots and Coastal Flood Zones: What Changes?",
            f"<p>Nothing about how turf itself is built changes, but where it goes and what else is required around it does. FEMA Zone AE carries at least a 1 percent annual chance of flooding with wave heights under 3 feet, and Zone VE is the higher-hazard coastal zone where wave action can cause serious damage in a base flood event ({src('fema-coastal-firm', 'FEMA coastal flood zone features')}). Coastal Sarasota and Manatee properties near the Gulf are more likely to carry one of those designations than inland Orlando-area lots; the state's water-body setback rule, a minimum 10 feet from a natural or man-made waterbody unless a seawall or similar barrier is already there, applies in both regions the same way ({src('rule62-308-100-text', 'Rule 62-308.100')}). A property's actual flood zone is looked up by address at FEMA's own map center rather than guessed ({src('fema-msc', 'FEMA Flood Map Service Center')}).</p>"),
        sec("What Should I Check on Turf After a Big Storm?",
            "<p>A quick walk-through after heavy rain or a named storm catches most problems before they get worse.</p>"
            + ul(["Look for standing water that has not drained within a few hours of the rain stopping, which usually points to a clogged or undersized base rather than the turf itself.",
                  "Check seams and the perimeter edge for lifting, curling or nail heads working loose, especially where water ran fastest across the yard.",
                  "Look for infill that has visibly washed into a low corner, a drain or the street, leaving a bare or thin patch on the turf.",
                  "Walk the base edge for erosion where turf meets a planting bed, a driveway or a fence line, since that is where a washout usually starts.",
                  "Rinse off any silt or debris left behind once standing water clears, before it dries into the fibers."])),
        sec("How Does Turf Compare to Grass or Pavers in a Flood-Prone Yard?",
            f"<p>Turf does not rot, develop mud or need resodding the way a flooded lawn of St. Augustine or bahia grass often does, which is one reason homeowners in low-lying parts of both service areas ask about it. It also does not absorb water the way living soil and root systems do, so a yard that is mostly turf relies entirely on its base and grading to move water, unlike a planted yard that still has some soil infiltration working for it. {compare('artificial-turf-vs-sod', 'Turf vs. sod')} covers that trade-off in more detail, and a paver patio or permeable paver driveway handles a heavy downpour differently again; {post('permeable-pavers-and-drainage-florida', 'our permeable pavers post')} covers how those surfaces manage stormwater instead.</p>"),
        sec("A Quick Example",
            f"<p>Say you have a low corner of a backyard in a 2000s {city('kissimmee')} subdivision that stays soggy under sod for days after a summer storm. Turf installed there without addressing that drainage problem first just moves the same standing-water complaint onto a new surface. Grading the base to carry water toward an existing swale or drain, and keeping the panel out of that swale itself under the state rule, is what actually fixes it; the turf choice on top is secondary to that base work. {svc('artificial-turf')} and the {a('/artificial-turf-cost/', 'artificial turf cost guide')} cover what that base work adds to a project.</p>"),
        sec("Related Reading",
            ul([svc("artificial-turf"), post("artificial-turf-installation-process", "how artificial turf is installed in Florida"),
                post("permeable-pavers-and-drainage-florida", "permeable pavers and yard drainage"),
                post("pavers-and-concrete-in-hurricanes", "how pavers and concrete hold up to Florida hurricanes"),
                post("artificial-turf-heat-in-florida", "how hot artificial turf gets in Florida")])),
    ])
    faqs = [
        faq("Does artificial turf flood the way a grass yard does?",
            f"It can pool water on the surface if the base and grading underneath are not built for Florida rainfall, the same as any hard surface would. Florida's 2026 turf rule requires a permeable, washed-stone base and positive drainage specifically to prevent that ({src('rule62-308-100-text', 'Rule 62-308.100')}), so a properly built turf area should shed a downpour rather than hold it."),
        faq("What is DEP Rule 62-308.100 and does it apply to my yard?",
            f"It is Florida's statewide minimum standard for synthetic turf on single-family lots of 1 acre or less, effective May 19, 2026, covering infill, base, permeability, stormwater and setbacks from water ({src('rule62-308-100-text', 'Rule 62-308.100')}; {src('fs125-572', 'F.S. 125.572')}). It applies the same way across Greater Orlando and Sarasota-Manatee; a local government can set a stricter permeability number but not a looser one."),
        faq("Can turf be installed next to a drainage swale or pond?",
            f"No. The state rule specifically bars installing turf \"within a swale, ditch, stormwater pond, or a stormwater pond's littoral zone\" ({src('rule62-308-100-text', 'Rule 62-308.100')}), and sets a 10-foot minimum setback from a natural or man-made waterbody unless a seawall or similar barrier already separates the two."),
        faq("Will heavy rain wash the sand infill out of my turf?",
            f"Not if it was installed to the state standard, which requires infill to stay on the property rather than wash off during rain ({src('rule62-308-100-text', 'Rule 62-308.100')}). A wash-out pattern after a storm usually means the base slope or edge restraint needs attention rather than the infill product itself."),
        faq("Does a hurricane put more stress on turf than ordinary rain?",
            "Wind is the bigger factor in a named storm, since it can work at loose seams or edges before rain even becomes an issue, which is why the state rule specifically calls for anchoring edges and seams against both wind and flooding. A well-anchored installation handles a tropical system's rain volume the same way it handles a normal summer downpour."),
    ]
    return page("/blog/artificial-turf-in-florida-rain-and-storms/", "post",
                "Artificial Turf Flooding and Rain in Florida: What to Know",
                "Florida's 2026 turf rule requires a permeable base and anchored seams, as of October 2026. How artificial turf handles rain, flooding and hurricanes.",
                "Does Artificial Turf Hold Up to Florida Rain, Flooding and Storms?",
                capsule("Artificial turf handles Florida rain and storms well when it is built on a permeable, washed-stone base with positive drainage and properly anchored seams, all required under the state's 2026 synthetic turf rule. The real flood risk comes from a clogged or undersized base, not the turf material itself. As of October 2026, that rule sets the same drainage and anchoring standard in Greater Orlando and Sarasota-Manatee."),
                body, faqs=faqs,
                sources=["rule62-308-100-text", "flrules62-308-100", "fs125-572", "ncei-annual-prcp", "nws-mlb-wetdry", "nws-tbw-tstm-climo", "fema-coastal-firm", "fema-msc"],
                related=[("/artificial-turf/", "artificial turf installation"), ("/artificial-turf-cost/", "artificial turf cost guide"),
                         ("/blog/permeable-pavers-and-drainage-florida/", "permeable pavers and yard drainage"),
                         ("/blog/pavers-and-concrete-in-hurricanes/", "pavers and concrete in hurricanes"),
                         ("/compare/artificial-turf-vs-sod/", "artificial turf vs. sod")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf", image="turf-pavers-pool", form=False)


def orange_county_permits():
    body = "".join([
        sec("Do You Need a Permit for a Driveway, Patio or Pavers in Orange County?",
            f"<p>In almost every case, yes, though the type of permit depends on exactly where the work sits. The City of Orlando requires an Engineering Permit for a driveway, patio slab or pavers, and unincorporated Orange County requires either a zoning permit for pavers or a right-of-way permit for driveway work, depending on the job ({src('orlando-engineering-permit', 'City of Orlando')}; {src('orange-do-i-need-permit', 'Orange County')}). Private-property patios and pavers skip a <em>building</em> permit in a few jurisdictions but almost never skip a zoning or right-of-way review entirely.</p>"
            f"<p>{svc('concrete-driveways')} and {svc('paver-driveways')} cover what we build; this post covers who has to approve it first, city by city across Orange County.</p>"
            + (photo("concrete-driveway-joints", "A broom-finish concrete driveway with cut control joints leads to a garage, the kind of apron work that crosses into a city right-of-way permit.") or "")),
        sec("What Does the City of Orlando Require?",
            f"<p>Orlando treats driveway, paver and patio work as an engineering matter rather than a building one. \"If you are installing/removing pavers, asphalt, concrete or expanding your driveway, an engineering permit application is required,\" and any work in the street, under the sidewalk or in the grassy strip next to it also needs a separate Right-of-Way Permit, reviewed within about 10 business days ({src('orlando-engineering-permit', 'City of Orlando, Engineering Permit')}; {src('orlando-row-permit', 'City of Orlando, Right-of-Way Permit')}). The city's Engineering Standards Manual sets single-family driveways at 7 to 18 feet wide at the throat, at least 3 feet from the property line, with the apron itself built at least 6 inches thick in 3,000 psi concrete and a break joint at the property line ({src('orlando-esm', 'Orlando Engineering Standards Manual')}). A 2022 parking code update also caps the impervious surface ratio of the required front or street-side yard at 0.40 for any driveway, parking or turnaround area ({src('orlando-ord-2022-45', 'Ordinance 2022-45')}). A submittal typically needs a survey with dimensions, an ISR worksheet, and a recorded Notice of Commencement once the job passes $5,000 ({src('orlando-res-requirements', 'Orlando Residential Permitting Requirements')}).</p>"),
        sec("What Does Unincorporated Orange County Require?",
            f"<p>The county's own FAQ is direct about it: \"Yes, anytime you are pouring concrete or placing pavers, a permit is required. Pavers require a Zoning permit only\" ({src('orange-do-i-need-permit', 'Orange County')}). A residential paver permit needs a dimensioned site plan showing the paver location, property lines and any easement, plus an Easement Acknowledgement form if the pavers sit in one; the permit fee runs $38 plus a $38 Development Engineering review fee, with review taking about 4 business days ({src('orange-residential-pavers', 'Orange County, Residential Pavers')}). A driveway in the county right-of-way instead goes through a Right-of-Way Utilization permit, and the county's Residential Lot Grading Policy sets a minimum 6-inch, 3,000 psi driveway with non-steel reinforcement through the right-of-way section, at least 3 feet from the property line, with one driveway per lot under 100 feet of frontage ({src('orange-lot-grading', 'Orange County Lot Grading Policy')}). Retaining walls need signed, sealed engineering once they retain more than 48 inches of unbalanced fill, or more than 24 inches if the wall also resists lateral loads beyond soil ({src('orange-res-plan-guide', 'Orange County Residential Plan Approval Guide')}).</p>"),
        sec("Winter Garden, Ocoee and Other Orange County Cities",
            f"<p>Incorporated cities inside Orange County run their own permit desks, separate from both Orlando and the county. {city('winter-garden')} requires an Impervious Area Calculation Worksheet whenever a project adds or extends a driveway, walkway, pool deck or similar surface, and its own form states plainly, \"PAVERS ARE IMPERVIOUS,\" so they count the same as concrete toward the lot's limit ({src('wintergarden-isr-worksheet', 'Winter Garden Impervious Area Worksheet')}). {city('ocoee')} answers its own FAQ the same direct way Orange County does: a concrete slab, patio, driveway or paver installation needs a permit, with a site plan and work description required and extra structural detail possible depending on scope (City of Ocoee, Building FAQ, {ext('https://www.ocoee.org/FAQ.aspx?QID=181', 'ocoee.org/FAQ.aspx?QID=181')}). Other Orange County cities and towns, {city('apopka')}, {city('maitland')} and {city('belle-isle')} among them, run separate building departments again; call ahead rather than assume a rule that applies in Orlando or Winter Garden carries over.</p>"
            + table("Orange County permit snapshot",
                    ["Jurisdiction", "Driveway", "Patio / pavers", "Contact"],
                    [["City of Orlando", "Engineering Permit + ROW permit", "Engineering Permit", "407-246-2271"],
                     ["Unincorporated Orange County", "ROW Utilization permit", "Zoning permit, $76 total fee", "407-836-5550"],
                     ["Winter Garden", "City permit; ISR worksheet required", "ISR worksheet; pavers count as impervious", "407-656-4111 ext. 5136"],
                     ["Ocoee", "Permit required, site plan", "Permit required, site plan", "407-905-3100"]],
                    "Fees and review times change; confirm the current figure with each office before you budget a project.")),
        sec("Does Florida's New HB 803 Exemption Let Me Skip a Permit?",
            f"<p>Not for most driveway, paver or patio work. Since July 1, 2026, Florida law exempts single-family homeowners from a <em>building</em> permit for qualifying non-structural work under $7,500, but it carves out flood-hazard-area properties and anything structural, and Orlando's own guide is explicit that \"applicable land development, planning, civil-related permits are not included in the exemption\" ({src('orlando-hb803-guide', 'City of Orlando HB 803 Guide')}). Because driveway and paver work in Orange County almost always routes through an engineering, zoning or right-of-way permit rather than a straight building permit, HB 803 rarely removes the approval step; it mostly affects small non-structural indoor work.</p>"),
        sec("Do You Need a Notice of Commencement Too?",
            f"<p>Yes, once the contract price passes $2,500. Florida law requires an owner to record a Notice of Commencement before work starts on any improvement over that threshold, and the permitting authority requires a copy on file before the first inspection once the contract exceeds $5,000 ({src('fs713-13', 'F.S. 713.13')}; {src('fs713-135', 'F.S. 713.135')}). Skipping it risks paying twice if a subcontractor or supplier later files a lien; most Orange County and Orlando permit cards print that warning directly on the application.</p>"),
        sec("A Quick Example",
            f"<p>Say you have a 1990s ranch home in unincorporated Orange County near {city('horizon-west')} and want to replace a cracked driveway with pavers in the same footprint. The paver work itself needs the county's $76 zoning permit with a site plan, and if the apron crosses into the county right-of-way, a separate Right-of-Way Utilization permit covers that section. A home a few miles away inside Orlando's city limits for the same project instead needs a single Engineering Permit that covers both the private driveway and the right-of-way apron together. {a('/permits/', 'Our permit guide')} links to every jurisdiction we cover.</p>"),
        sec("Related Reading",
            ul([svc("concrete-driveways"), svc("paver-driveways"),
                post("osceola-county-kissimmee-st-cloud-permits", "driveway permits in Kissimmee and Osceola County"),
                post("hoa-approval-for-pavers-and-concrete", "getting HOA approval for pavers or a driveway"),
                a("/faq/cost-and-permits/", "the cost and permits FAQ")])),
    ])
    faqs = [
        faq("Does Orlando require a separate permit for the part of my driveway in the right-of-way?",
            f"Often yes. The Engineering Permit covers the driveway and paver work itself, but any part of the job in the street, under the sidewalk or in the grassy strip next to it needs its own Right-of-Way Permit, which may be bundled with the larger permit depending on scope ({src('orlando-row-permit', 'City of Orlando')})."),
        faq("How much does an Orange County paver permit cost?",
            f"As published, $38 for the permit itself plus a $38 Development Engineering review fee, or $76 total before any code-violation surcharge ({src('orange-residential-pavers', 'Orange County')}). Confirm the current fee with the Zoning Division before budgeting, since fee schedules change."),
        faq("What's the front-yard impervious surface limit in Orlando?",
            f"Orlando's 2022 parking code update caps the impervious surface ratio of a required front or street-side yard at 0.40 for any driveway, parking or turnaround configuration, with driveways themselves limited to 7 to 18 feet wide at the property line ({src('orlando-ord-2022-45', 'Ordinance 2022-45')})."),
        faq("Who do I call for a right-of-way permit in unincorporated Orange County?",
            f"Development Engineering Permitting at 407-836-7920 handles Right-of-Way Utilization permits; the Plan Review Section at 407-836-7974 handles related plan review ({src('orange-plan-review', 'Orange County Plan Review')})."),
        faq("Does Winter Garden count a paver patio toward my lot's impervious limit?",
            f"Yes. The city's own worksheet states plainly that pavers are impervious for calculation purposes, counted the same as a concrete driveway, pool deck or walkway toward the lot's overall limit ({src('wintergarden-isr-worksheet', 'Winter Garden')})."),
    ]
    return page("/blog/orange-county-orlando-driveway-patio-permits/", "post",
                "Driveway and Paver Permits in Orlando and Orange County",
                "Orlando requires an Engineering Permit for driveways and pavers; Orange County requires a zoning or ROW permit. City-by-city rules as of October 2026.",
                "Do You Need a Permit for a Driveway, Patio or Pavers in Orlando and Orange County?",
                capsule("Orlando requires an Engineering Permit for a driveway, patio slab or pavers, plus a separate Right-of-Way Permit for work touching the street. Unincorporated Orange County requires a zoning permit for pavers and a right-of-way permit for driveway work. Winter Garden and Ocoee run their own permit desks with their own rules. As of October 2026, almost none of this is exempt under Florida's HB 803 building-permit carve-out."),
                body, faqs=faqs,
                sources=["orlando-hb803-guide", "orlando-engineering-permit", "orlando-row-permit", "orlando-esm", "orlando-ord-2022-45",
                         "orlando-res-requirements", "orange-do-i-need-permit", "orange-residential-pavers", "orange-plan-review",
                         "orange-lot-grading", "orange-res-plan-guide", "wintergarden-isr-worksheet", "fs713-13", "fs713-135",
                         ("City of Ocoee, Building FAQ: concrete slab, patio, driveway and paver permits", "https://www.ocoee.org/FAQ.aspx?QID=181"),
                         ("City of Ocoee, Building Division", "https://www.ocoee.org/163/Building-Division")],
                related=[("/concrete-driveways/", "concrete driveways"), ("/paver-driveways/", "paver driveways"),
                         ("/blog/osceola-county-kissimmee-st-cloud-permits/", "permits in Osceola County"),
                         ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA approval for pavers and concrete"),
                         ("/faq/cost-and-permits/", "cost and permits FAQ")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways", image="concrete-driveway-joints", form=False)


def osceola_county_permits():
    body = "".join([
        sec("Do You Need a Permit for a Driveway or Patio in Osceola County?",
            f"<p>Yes in nearly every case, but which office you apply to depends on whether the address is inside Kissimmee, inside St. Cloud, or in unincorporated Osceola County. Kissimmee and unincorporated Osceola County both require a driveway permit before construction or widening, and St. Cloud requires Public Works approval for any work touching its right-of-way even though it exempts some paver work on private property from a building permit ({src('kissimmee-driveway-sidewalk', 'City of Kissimmee')}; {src('osceola-parking-ord', 'Osceola County Code §22-50.6')}; {src('stcloud-permit-info', 'City of St. Cloud')}).</p>"
            f"<p>{svc('concrete-driveways')} and {svc('paver-patios')} cover the work itself; this post covers who signs off on it first.</p>"
            + (photo("paver-driveway-herringbone", "A herringbone-pattern paver driveway and walkway lead to a garage, the kind of job that needs a driveway permit in Kissimmee and Osceola County.") or "")),
        sec("City of Kissimmee: Driveway, Sidewalk and Slab Permits",
            f"<p>Kissimmee's Engineering Division handles driveway and sidewalk work through its EnerGov portal under \"Driveway / Sidewalk Construction,\" and staff tell applicants which documents they need once the application is open; routing takes at least 2 business days, and the city notes that some adjacent rights-of-way actually belong to FDOT or Osceola County rather than the city ({src('kissimmee-driveway-sidewalk', 'City of Kissimmee')}). Right-of-way work is a separate permit with fees starting at a $25 minimum, $150 for an open cut on a paved street, $25 for an unpaved street, and $50 for bore-and-jack work ({src('kissimmee-row-permit', 'City of Kissimmee, Right-of-Way Permits')}). On the building side, the permit-type list includes \"Slab With/Without Footer\" for a patio or pad; pavers and retaining walls don't have their own listed category, so call Permitting at 407-518-2379 to confirm how a specific paver or wall job gets classified ({src('kissimmee-permit-types', 'City of Kissimmee, Types of Permits')}).</p>"),
        sec("Unincorporated Osceola County: Driveway Width and Right-of-Way Rules",
            f"<p>County code sets a hard limit on driveway width: \"Residential driveways shall not exceed twenty-four (24) feet in width unless approved by conditional use,\" and any new driveway or widening needs a county driveway permit before work starts ({src('osceola-parking-ord', 'Osceola County Code §22-50.6')}). The county's right-of-way permitting page is written mostly with utility work in mind, with disturbed areas required to be regraded within 48 hours and lane closures limited to set weekday windows, but it publishes no flat fee for a residential driveway permit, so confirm the current cost directly with the Building Office at 407-742-0200 ({src('osceola-row-info', 'Osceola County Right-of-Way Permit Information')}). The county applies the 2026 HB 803 small-project exemption through its own \"Owner Disclosure of Exempt Work\" form rather than an automatic waiver ({src('osceola-permit-info', 'Osceola County Permit Information')}). Osceola's own homeowners page doesn't spell out patio, paver or retaining-wall permit rules beyond the driveway code above, so confirm those directly with the Building Office before scheduling work ({src('osceola-homeowners', 'Osceola County Homeowners')}).</p>"),
        sec("City of St. Cloud: What's Exempt and What Isn't",
            f"<p>St. Cloud's own \"No Permit Required\" list names \"Pavers (Driveways/Sidewalks - Please see Public Works Department)\" alongside resealing an existing on-site driveway, while its \"Permit Required\" list separately names a \"Concrete Pad,\" a \"Subdivision or Retaining Wall,\" and any swimming pool or spa work ({src('stcloud-permit-info', 'City of St. Cloud, Permit Information')}). The exemption for pavers is conditional, not absolute: any work inside the public right-of-way still routes through Public Works and Engineering, with published right-of-way fees of a $110 base permit, $30 per curb cut, $100 per driveway inspection and $60 for sidewalk work ({src('stcloud-pw-fees', 'City of St. Cloud, Public Works Fees')}). A retaining wall needs a permit, though the city hasn't published a height threshold that triggers engineered drawings, so confirm that number directly with City Hall at 407-957-7300.</p>"),
        sec("Celebration and Other Osceola Communities",
            f"<p>{city('celebration')} and {city('poinciana')} sit inside unincorporated Osceola County for county-level driveway and paver permits, but a planned community can layer its own architectural review on top. Celebration's Architectural Review Committee meets on the third Monday of each month on a monthly application deadline; one cycle's posted example listed an April application due by early May at 5:30 p.m. ({src('celebration-arc', 'Celebration, Architectural Review Committee')}). The county permit covers the driveway or paver work itself; the community's own ARC review is a separate step that happens alongside it, and the exact submittal packet for Celebration's ARC wasn't published where this research could confirm it, so ask the community association directly before submitting.</p>"
            + table("Osceola County permit snapshot",
                    ["Jurisdiction", "Driveway", "Patio / pavers", "Contact"],
                    [["City of Kissimmee", "Engineering Division permit", "Slab permit (patio); pavers not separately listed", "407-518-2278"],
                     ["Unincorporated Osceola County", "County driveway permit, 24 ft max width", "Confirm with Building Office", "407-742-0200"],
                     ["City of St. Cloud", "ROW permit, $110 base + fees", "Exempt on private property; ROW work still permitted", "407-957-7300"]],
                    "Fees and categories change; confirm current figures before you budget a project.")),
        sec("Does the Notice of Commencement Rule Apply Here Too?",
            f"<p>It does, the same as anywhere else in Florida. Once a driveway, patio or paver contract passes $2,500, the owner records a Notice of Commencement before work starts, and once it passes $5,000 the permitting office needs a copy on file before the first inspection ({src('fs713-13', 'F.S. 713.13')}; {src('fs713-135', 'F.S. 713.135')}). Kissimmee, St. Cloud and Osceola County all print the standard statutory warning about paying twice on their permit applications.</p>"),
        sec("A Quick Example",
            f"<p>Say you have a 1,200 square foot driveway and walkway paver job in a 1990s {city('kissimmee')} subdivision near {a('/kissimmee-fl/', 'Lake Tohopekaliga')}. The driveway portion needs Kissimmee's Engineering Division permit, and if any part of it extends into the right-of-way strip near the street, that's a second permit with its own fee. The same job three miles away in unincorporated Osceola County instead goes through the county's driveway permit process, with the 24-foot width cap applying regardless of how wide the garage is behind it.</p>"),
        sec("Related Reading",
            ul([svc("paver-driveways"), svc("concrete-driveways"),
                post("orange-county-orlando-driveway-patio-permits", "driveway permits in Orlando and Orange County"),
                post("hoa-approval-for-pavers-and-concrete", "HOA and ARC approval for pavers"),
                a("/faq/cost-and-permits/", "the cost and permits FAQ")])),
    ])
    faqs = [
        faq("Does St. Cloud really not require a permit for a paver driveway?",
            f"Pavers on private property are on the city's own no-permit list, but anything touching the public right-of-way, the apron, a curb cut or the sidewalk strip, still needs Public Works and Engineering approval with its own fee schedule ({src('stcloud-permit-info', 'City of St. Cloud')}; {src('stcloud-pw-fees', 'St. Cloud Public Works Fees')})."),
        faq("How wide can a residential driveway be in unincorporated Osceola County?",
            f"Code caps it at 24 feet unless the county approves a conditional use for something wider ({src('osceola-parking-ord', 'Osceola County Code §22-50.6')})."),
        faq("Does St. Cloud require a permit for a retaining wall?",
            "Yes, though the city hasn't published a specific height that triggers engineered, signed-and-sealed drawings; confirm that threshold directly with City Hall before finalizing a wall design."),
        faq("Where do I apply for a Kissimmee right-of-way permit?",
            f"Through the Engineering Division; fees start at a $25 minimum and scale up based on the type of work, with open cuts on paved streets running $150 ({src('kissimmee-row-permit', 'City of Kissimmee')})."),
        faq("Does Celebration have its own approval process beyond the county permit?",
            f"Yes. Celebration's Architectural Review Committee reviews exterior changes separately from Osceola County's permit, meeting on the third Monday of each month on a monthly deadline ({src('celebration-arc', 'Celebration ARC')}); check with the community association for the current submittal packet."),
    ]
    return page("/blog/osceola-county-kissimmee-st-cloud-permits/", "post",
                "Driveway Permits in Kissimmee, St. Cloud and Osceola County",
                "Kissimmee needs an Engineering Division permit, Osceola County caps driveways at 24 feet, and St. Cloud exempts private pavers. October 2026 guide.",
                "Driveway and Patio Permits in Kissimmee, St. Cloud and Osceola County",
                capsule("Kissimmee and unincorporated Osceola County both require a driveway permit before construction or widening, with the county capping residential driveways at 24 feet wide. St. Cloud exempts pavers on private property from a building permit but still requires Public Works approval for anything touching the right-of-way. As of October 2026, Celebration layers its own ARC review on top of the county permit."),
                body, faqs=faqs,
                sources=["kissimmee-driveway-sidewalk", "kissimmee-row-permit", "kissimmee-permit-types", "osceola-row-info",
                         "osceola-parking-ord", "osceola-permit-info", "osceola-homeowners", "stcloud-permit-info", "stcloud-pw-fees",
                         "celebration-arc", "fs713-13", "fs713-135"],
                related=[("/paver-driveways/", "paver driveways"), ("/concrete-driveways/", "concrete driveways"),
                         ("/blog/orange-county-orlando-driveway-patio-permits/", "permits in Orlando and Orange County"),
                         ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA and ARC approval for pavers"),
                         ("/faq/cost-and-permits/", "cost and permits FAQ")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways", image="paver-driveway-herringbone", form=False)


def seminole_county_permits():
    body = "".join([
        sec("Do You Need a Permit for a Driveway or Patio in Seminole County?",
            f"<p>Yes, in every Seminole County jurisdiction checked for this guide, Sanford, Lake Mary, Oviedo, Winter Springs and unincorporated Seminole County all require some form of permit for a driveway, and most require one for a patio or pavers on private property too, even where a straight building permit is waived ({src('seminole-driveway-app', 'Seminole County')}; {src('sanford-schedule-n', 'City of Sanford')}; {src('oviedo-building-services', 'City of Oviedo')}).</p>"
            f"<p>{svc('concrete-driveways')} and {svc('paver-driveways')} cover what we build across all four cities and the unincorporated county; this post covers who approves it first.</p>"
            + (photo("concrete-driveway-modern", "A wide broom-finish concrete driveway leads to a modern house with a dark garage door, the kind of apron work that triggers a right-of-way permit in Seminole County.") or "")),
        sec("Unincorporated Seminole County",
            f"<p>The county's Residential Driveway Construction Application spells out the spec in detail: a minimum 6 inches of non-steel reinforced concrete through the right-of-way section, 3,000 psi minimum, with fiber reinforcement allowed, a maximum width of 18 feet plus 3-foot flares on each side for 24 feet total at the roadway, and the driveway set at least 5 feet from the property line ({src('seminole-driveway-app', 'Seminole County')}). Pavers are allowed in the right-of-way portion of the driveway but not across the crosswalk or sidewalk section, and the county won't replace paver sections it has to disturb for utility work. Plan for about 3 business days of review; the published form leaves the fee blank, though an older county document cited a $45 fee. Call the Development Review Division at 407-665-7371 to confirm the current number before budgeting.</p>"),
        sec("City of Sanford",
            f"<p>Sanford's LDR Schedule N requires a city permit for any proposal to access the city right-of-way, with a Seminole County permit needed instead for county roads and an FDOT permit for state roads. Single-family driveways must sit at least 10 feet from an adjacent driveway and at least 35 feet from the street's parallel pavement, reduced proportionally on smaller corner lots, with aprons built to 3,000 psi concrete ({src('sanford-schedule-n', 'City of Sanford, LDR Schedule N')}). The published fee for a single-family residential driveway permit is $250 ({src('sanford-fees', 'City of Sanford, LDR Article VII Fees')}). Sanford's impervious surface rule caps most residential zoning districts at 50 percent of the lot, counting \"concrete, pavers, asphalt, compacted gravel or mulch, and artificial turf\" the same way ({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}).</p>"),
        sec("City of Oviedo",
            f"<p>Oviedo applies the 2026 HB 803 exemption to some interior and structural work, but its own guidance lists \"Pavers/driveways/sidewalks on private property\" and \"Non-structural 4-inch concrete slabs on grade\" as projects that still need a planning and zoning permit through the Planning Department, with a separate Engineering right-of-way permit required for anything in the street-side strip ({src('oviedo-building-services', 'City of Oviedo')}). A Right-of-Way Type I application runs $79 plus a $25 technology fee and needs a sealed boundary survey, an MOT plan and a certificate of insurance ({src('oviedo-row-type1', 'City of Oviedo, ROW Type I Application')}). The slab and paver permit package asks for a notarized application, the contractor's license, insurance naming the city, and two site plans showing distances to the property line ({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}). A retaining wall needs signed, sealed engineered drawings with wind design data regardless of height ({src('oviedo-permit-guidelines', 'City of Oviedo, Permit Guidelines')}).</p>"),
        sec("Lake Mary and Winter Springs",
            f"<p>{city('lake-mary')}'s Building Division requires a permit for residential paver work, applied for through the city's online portal with a current survey and site plan showing the proposed paver footprint and its impervious-surface impact; its HB 803 exemption page lists only electrical, plumbing, mechanical, gas, structural work, flood-zone properties and projects at or above $7,500 as the items that never qualify for the exemption, without confirming whether ordinary driveway or paver work does (City of Lake Mary, Building Division, {ext('https://www.lakemaryfl.com/157/Building', 'lakemaryfl.com/157')}; City of Lake Mary, Permit Exemption, {ext('https://www.lakemaryfl.com/1747', 'lakemaryfl.com/1747')}). Confirm exemption eligibility for a specific project with the Building Department at 407-585-1361 before skipping an application. {city('winter-springs')}'s Community Development Department issues building permits and reviews right-of-way work the same way most Central Florida cities do; the exact material and width rules for residential driveways weren't confirmed on a fetched city page for this guide, so check the current driveway and parking standards with the department at 407-327-5963 before finalizing a design.</p>"
            + table("Seminole County permit snapshot",
                    ["Jurisdiction", "Driveway", "Patio / pavers", "Contact"],
                    [["Unincorporated Seminole County", "County ROW driveway permit", "Confirm with Development Review", "407-665-7371"],
                     ["City of Sanford", "City ROW permit, $250 fee", "Falls under ISR calculation", "407-688-5150"],
                     ["City of Oviedo", "P&Z permit even on private property", "Slab/paver permit package required", "407-971-5755"],
                     ["City of Lake Mary", "Building Division permit", "Paver permit with site plan", "407-585-1361"],
                     ["City of Winter Springs", "City permit; confirm current rule", "City permit; confirm current rule", "407-327-5963"]],
                    "Fees and categories change; confirm current figures before you budget a project.")),
        sec("Do You Need a Notice of Commencement in Seminole County Too?",
            f"<p>The same statewide rule applies here as anywhere else in Florida: a Notice of Commencement gets recorded once a driveway, patio or paver contract passes $2,500, and a copy has to be on file with the permitting office before the first inspection once the contract passes $5,000 ({src('fs713-13', 'F.S. 713.13')}; {src('fs713-135', 'F.S. 713.135')}). Lake Mary's own permit guidance flags this specifically for paver work; the other Seminole County jurisdictions apply the same statutory threshold even where it isn't spelled out on their own forms.</p>"),
        sec("A Quick Example",
            f"<p>Say you have a driveway apron replacement in a 1990s subdivision in {city('oviedo')}. Because the work is on private property but still a driveway, it needs Oviedo's planning and zoning permit rather than skipping review the way some HB 803 exempt projects do, and if the apron crosses into the road right-of-way, a separate Right-of-Way Type I application covers that section at $79 plus the tech fee. A homeowner three miles away in unincorporated Seminole County instead files the county's own driveway application, with its own width and setback numbers applying instead of Oviedo's.</p>"),
        sec("Related Reading",
            ul([svc("concrete-driveways"), svc("paver-driveways"),
                post("orange-county-orlando-driveway-patio-permits", "driveway permits in Orlando and Orange County"),
                post("lake-and-polk-county-driveway-permits", "driveway permits in Lake and Polk counties"),
                a("/faq/cost-and-permits/", "the cost and permits FAQ")])),
    ])
    faqs = [
        faq("Does unincorporated Seminole County allow pavers in the right-of-way?",
            f"Yes, on the driveway portion, but not across the sidewalk or crosswalk section, and the county won't replace pavers it has to remove for utility work ({src('seminole-driveway-app', 'Seminole County')})."),
        faq("How far must a Sanford driveway sit from the neighbor's driveway?",
            f"At least 10 feet, with an additional requirement of at least 35 feet from the street's parallel pavement, reduced proportionally on smaller corner lots under the city's LDR Schedule N ({src('sanford-schedule-n', 'City of Sanford')})."),
        faq("Does Oviedo require a contractor's license copy for a paver permit?",
            f"Its slab and paver permit package asks for the contractor's license along with a notarized application and proof of insurance naming the city ({src('oviedo-slab-paver', 'City of Oviedo')})."),
        faq("Do I need a Notice of Commencement for a driveway project in Seminole County?",
            f"Yes, once the contract passes $2,500 under Florida's statewide lien law, the same threshold that applies everywhere else in the state ({src('fs713-13', 'F.S. 713.13')})."),
        faq("Who do I call to confirm Lake Mary or Winter Springs permit rules?",
            "Lake Mary's Building Department at 407-585-1361 or Winter Springs's Community Development Department at 407-327-5963; both cities' specific driveway material and width rules are best confirmed directly before finalizing a design."),
    ]
    return page("/blog/seminole-county-driveway-patio-permits/", "post",
                "Driveway and Patio Permits in Seminole County, Florida",
                "Sanford, Lake Mary, Oviedo and Winter Springs each run separate permit desks from unincorporated Seminole County. Rules as of October 2026.",
                "Driveway and Patio Permits in Seminole County (Sanford, Lake Mary, Oviedo, Winter Springs)",
                capsule("Every Seminole County jurisdiction requires a permit for driveway work, and most require one for a patio or pavers too, even where a straight building permit is waived. Unincorporated Seminole County, Sanford, Oviedo, Lake Mary and Winter Springs each run a separate permit desk with its own width, setback and fee rules. As of October 2026, confirming the current rule with the specific city or county office matters more than assuming one jurisdiction's answer applies to the next."),
                body, faqs=faqs,
                sources=["seminole-driveway-app", "seminole-driveway-app-old", "seminole-hb803", "sanford-building", "sanford-schedule-n",
                         "sanford-fees", "sanford-schedule-f", "oviedo-building-services", "oviedo-row-type1", "oviedo-slab-paver",
                         "oviedo-permit-guidelines", "fs713-13", "fs713-135",
                         ("City of Lake Mary, Building Division", "https://www.lakemaryfl.com/157/Building"),
                         ("City of Lake Mary, Permit Exemption (HB 803)", "https://www.lakemaryfl.com/1747"),
                         ("City of Winter Springs, Building & Permits", "https://www.winterspringsfl.org/cd/page/building-permits")],
                related=[("/concrete-driveways/", "concrete driveways"), ("/paver-driveways/", "paver driveways"),
                         ("/blog/orange-county-orlando-driveway-patio-permits/", "permits in Orlando and Orange County"),
                         ("/blog/lake-and-polk-county-driveway-permits/", "permits in Lake and Polk counties"),
                         ("/faq/cost-and-permits/", "cost and permits FAQ")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways", image="concrete-driveway-modern", form=False)


def lake_polk_permits():
    body = "".join([
        sec("Do You Need a Permit for a Driveway or Patio in Lake or Polk County?",
            f"<p>Almost always, though the exact answer shifts from city to city more in this corner of Central Florida than anywhere else we build. {city('clermont')} waives a building permit for a private driveway but still requires zoning approval, unincorporated Lake County exempts some driveways and sidewalks from a building permit under the state code while still requiring a separate driveway permit for right-of-way work, and {city('minneola')}, {city('groveland')} and {city('davenport')} each run their own building departments with their own rules ({src('clermont-permit-checklists', 'City of Clermont')}; {src('lake-exempt', 'Lake County')}).</p>"
            f"<p>{svc('concrete-driveways')} and {svc('retaining-walls')} cover what we build across this stretch of Lake and Polk counties; this post covers who signs off on it first.</p>"
            + (photo("retaining-wall-crib", "A modular concrete crib-style retaining wall built into a grassy slope, the kind of grade change common in the rolling terrain around Clermont and Minneola.") or "")),
        sec("Unincorporated Lake County",
            f"<p>Lake County's own exemption list, drawn from the state building code, waives a permit for \"sidewalks and driveways not more than 30 inches above adjacent grade,\" but adds that \"zoning and flood requirements shall be met as required\" regardless ({src('lake-exempt', 'Lake County, Residential Work Exempt from Permits')}). That building-permit exemption is separate from the county's driveway apron permit, which is required in the right-of-way of any county-maintained road: the apron runs 10 to 24 feet wide at the property line, needs either an 8-foot radius or 8-by-4-foot flares up to 32 feet at the road edge, and any required culvert matches the neighborhood's existing culverts or runs at least 15 inches in diameter ({src('lake-driveway-apron', 'Lake County, Driveway Apron Permit')}). The county's transportation design standards separately cap most lots at one driveway per 100 feet of frontage, with a 10-foot minimum driveway width ({src('lake-ldr-appendix-a', 'Lake County LDR Appendix A')}).</p>"),
        sec("City of Clermont",
            f"<p>Clermont's own FAQ states that \"a building permit is not required\" for a driveway or sidewalk on private property, \"however, a zoning approval is required,\" with a $45 fee and no inspection needed for that private-property work ({src('clermont-permit-checklists', 'City of Clermont, Permit Checklists')}). An apron built in the city right-of-way is a different application: also $45, but this one does need a city driveway inspection once the apron is built \"per City Standards.\" On the building side, the city's own permit-type list includes \"Concrete/Driveway/Patio-Concrete only on grade (no footers)\" as its own category ({src('clermont-permit-types', 'City of Clermont, Permit Type Descriptions')}). Retaining walls under 3 feet need a permit but not engineered plans; above 3 feet, engineered plans are required. Clermont's R-1 zoning caps total impervious coverage at 55 percent, with the house plus driveway and walkways limited to 45 percent ({src('clermont-r1-isr', 'City of Clermont, Municode Ch. 125')}), a tighter number worth checking early on a hilly Lake County lot where driveway grading already eats into the budget.</p>"),
        sec("Minneola and Groveland",
            f"<p>{city('minneola')}'s Building Department, at 800 N. US Highway 27, states that a permit is required to \"construct, enlarge, alter, repair, move, demolish or change the occupancy of a building or structure\"; the department's general scope covers paver and concrete work the way most Lake County cities treat it, and the office is the right call to confirm exactly how a specific driveway or patio project gets classified before applying (City of Minneola, Building Department, {ext('https://www.minneola.us/building-department', 'minneola.us/building-department')}). {city('groveland')}'s Building Division requires site plans for residential permits that show \"the location of driveways, walks, patios, pavers, and any other impervious items on the lot,\" with paver or concrete slab questions routed to the division directly by phone or through its eTrakit portal (City of Groveland, Building Division, {ext('https://www.groveland-fl.gov/130/Building-Division', 'groveland-fl.gov/130')}). Neither city publishes a plain-language exemption list the way Clermont does for private-property flatwork, so call ahead rather than assume Clermont's rule carries over.</p>"),
        sec("Davenport and Unincorporated Polk County",
            f"<p>{city('davenport')}'s Building Department requires a site plan showing setbacks from the property line for \"sheds, pavers, slabs,\" alongside a signed, notarized permit application (City of Davenport, Building, {ext('https://www.mydavenport.org/index.asp?SEC=54C1C62E-BE5B-43DE-AF31-EF135278CEAD', 'mydavenport.org')}). Unincorporated Polk County's Building Division, which covers areas outside Davenport, Lakeland, Winter Haven and the county's other incorporated cities, publishes a narrower exemption: its building FAQ lists concrete slabs for support of a structure, elevated slabs, sidewalks, and portions of driveways in the right-of-way or within minimum setbacks among the items that don't require a building permit, while still requiring that all slabs meet building code and land development code drainage requirements (Polk County, Building FAQ, {ext('https://www.polkfl.gov/services/building/faqs/', 'polkfl.gov/services/building/faqs')}). Confirm the current exemption wording with the Polk County Building Division at 863-534-6080 before assuming a specific slab or driveway section qualifies.</p>"
            + table("Lake and Polk County permit snapshot",
                    ["Jurisdiction", "Driveway", "Patio / pavers / slab", "Contact"],
                    [["Unincorporated Lake County", "County apron permit in ROW", "Exempt under 30 in. height if zoning/flood rules met", "352-253-6019"],
                     ["City of Clermont", "Zoning approval, $45; ROW apron, $45", "Own permit category; retaining wall rule by height", "352-394-4081"],
                     ["City of Minneola", "City permit required", "Confirm with Building Department", "352-394-3598"],
                     ["City of Groveland", "City permit required", "Site plan showing all impervious items", "352-429-2141"],
                     ["City of Davenport", "City permit, site plan with setbacks", "Site plan with setbacks required", "863-419-3300"],
                     ["Unincorporated Polk County", "Confirm with Building Division", "Some slab/ROW portions exempt; drainage rules still apply", "863-534-6080"]],
                    "Fees, categories and exemptions change; confirm current rules with each office before you budget a project.")),
        sec("Why Retaining Walls Come Up So Often in This Area",
            f"<p>Lake County's terrain is hillier than most of Central Florida; Sugarloaf Mountain near Clermont rises about 312 feet above sea level, part of the Lake Wales Ridge chain of ancient sand hills running south through the county ({src('wiki-sugarloaf', 'Sugarloaf Mountain, Florida')}). That rolling grade is why a Clermont or Minneola driveway or backyard project is more likely to need a retaining or seat wall than a flatter lot in Orlando or Kissimmee, and why Clermont's own permit rule draws a clear line at 3 feet for when engineered drawings kick in. {svc('retaining-walls')} covers how we build those walls with drainage behind them; {post('retaining-wall-ideas-florida-yards', 'our retaining wall ideas post')} covers design options for a sloped Lake County yard.</p>"),
        sec("Do You Need a Notice of Commencement in Lake or Polk County Too?",
            f"<p>Yes, on the same statewide terms as anywhere else: a Notice of Commencement gets recorded once a driveway, patio, paver or wall contract passes $2,500, and the permitting office needs a copy on file before the first inspection once the job passes $5,000 ({src('fs713-13', 'F.S. 713.13')}; {src('fs713-135', 'F.S. 713.135')}). Clermont, Minneola, Groveland and Davenport all handle permit cards the same way most Florida cities do, with that warning printed directly on the application.</p>"),
        sec("A Quick Example",
            f"<p>Say you have a sloped half-acre lot in {city('minneola')} where a new paver driveway needs a retaining wall along one side to hold the grade. The driveway and paver permit goes through Minneola's Building Department, and the wall itself needs its own review, likely with engineered drawings once it passes a few feet in height, the same way Clermont's rule works a few miles away. Budgeting the wall and the driveway as two separate approvals, rather than assuming one permit covers both, avoids a schedule surprise partway through the job.</p>"),
        sec("Related Reading",
            ul([svc("retaining-walls"), svc("concrete-driveways"),
                post("seminole-county-driveway-patio-permits", "driveway permits in Seminole County"),
                post("retaining-wall-ideas-florida-yards", "retaining wall and seat wall ideas"),
                a("/faq/cost-and-permits/", "the cost and permits FAQ")])),
    ])
    faqs = [
        faq("Does Clermont require a permit for a concrete patio?",
            f"Clermont lists \"Concrete/Driveway/Patio-Concrete only on grade (no footers)\" as its own permit category, which is different from its private-property driveway exemption; confirm which one applies to a specific patio design with the Building Services office ({src('clermont-permit-types', 'City of Clermont')})."),
        faq("How tall can a retaining wall be in Clermont before it needs engineering?",
            f"Walls under 3 feet need a permit but not engineered plans; walls over 3 feet need engineered drawings ({src('clermont-permit-types', 'City of Clermont')})."),
        faq("Does unincorporated Lake County exempt driveways from permits?",
            f"Only in a narrow sense: a building permit is waived for sidewalks and driveways under 30 inches above grade, but zoning and flood rules still apply, and a separate apron permit is still required for any work in the county right-of-way ({src('lake-exempt', 'Lake County')})."),
        faq("Do Minneola and Groveland require a permit for pavers?",
            "Both cities require permits for paver and concrete work; neither publishes the kind of plain private-property exemption Clermont does, so confirm the specific requirement with each building department before starting."),
        faq("Does unincorporated Polk County exempt driveway and slab work?",
            "Polk County's own building FAQ exempts some slab and driveway-in-the-right-of-way scenarios from a building permit, but drainage requirements still apply, and the office recommends confirming any specific project against the current rule before assuming it qualifies."),
    ]
    return page("/blog/lake-and-polk-county-driveway-permits/", "post",
                "Driveway Permits in Clermont, Minneola and Lake County",
                "Lake County exempts low driveways but still requires an apron permit; Clermont, Minneola, Groveland and Davenport each run their own rules.",
                "Driveway and Patio Permits in Clermont, Minneola, Groveland and Davenport (Lake and Polk Counties)",
                capsule("Unincorporated Lake County waives a building permit for driveways under 30 inches of grade but still requires a separate apron permit for right-of-way work. Clermont waives a building permit for a private driveway but requires zoning approval, while Minneola, Groveland, Davenport and unincorporated Polk County each run their own rules. As of October 2026, Lake County's hilly terrain also makes a retaining wall permit come up more often here than in flatter parts of Central Florida."),
                body, faqs=faqs,
                sources=["lake-exempt", "lake-driveway-apron", "lake-ldr-appendix-a", "lake-row-permit", "lake-building-services",
                         "clermont-faq", "clermont-permit-checklists", "clermont-forms", "clermont-permit-types", "clermont-r1-isr",
                         "wiki-sugarloaf", "fs713-13", "fs713-135",
                         ("City of Minneola, Building Department", "https://www.minneola.us/building-department"),
                         ("City of Groveland, Building Division", "https://www.groveland-fl.gov/130/Building-Division"),
                         ("City of Davenport, Building Department", "https://www.mydavenport.org/index.asp?SEC=54C1C62E-BE5B-43DE-AF31-EF135278CEAD"),
                         ("Polk County, Building FAQ", "https://www.polkfl.gov/services/building/faqs/")],
                related=[("/retaining-walls/", "retaining walls"), ("/concrete-driveways/", "concrete driveways"),
                         ("/blog/seminole-county-driveway-patio-permits/", "permits in Seminole County"),
                         ("/blog/retaining-wall-ideas-florida-yards/", "retaining wall and seat wall ideas"),
                         ("/faq/cost-and-permits/", "cost and permits FAQ")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways", image="retaining-wall-crib", form=False)


def sarasota_county_permits():
    body = "".join([
        sec("Do You Need a Permit for a Driveway or Patio in Sarasota County?",
            f"<p>Yes for any driveway or apron work, in every jurisdiction covered here. The City of Sarasota, Sarasota County, Venice and North Port each require a right-of-way permit for driveway or apron work, and each applies its own rule, sometimes an exemption, sometimes not, for a patio or paver surface built entirely on private property ({src('city-sarasota-code-29.5-7-curb-cut-driveway', 'City of Sarasota')}; {src('sarasota-county-row-permit', 'Sarasota County')}; {src('venice-ldr-9.1-row-definition', 'City of Venice')}; {src('north-port-row-permit-application', 'City of North Port')}).</p>"
            f"<p>{svc('concrete-driveways')} and {svc('paver-patios')} cover what we build across the Suncoast; this post covers who approves it first.</p>"
            + (photo("interlocking-pavers", "A close-up, top-down view of gray interlocking concrete pavers, the kind of driveway surface that needs a right-of-way permit anywhere it crosses into a Sarasota County street frontage.") or "")),
        sec("City of Sarasota",
            f"<p>City code makes a curb cut or driveway construction unlawful without first getting a permit from the city engineer, built to the Engineering Design Criteria Manual ({src('city-sarasota-code-29.5-7-curb-cut-driveway', 'City of Sarasota Code §29.5-7')}). Any grading, filling or altering of natural topography needs a separate erosion and siltation control permit, though the code exempts \"minor land disturbing activities, such as garden work or individual home landscaping\" ({src('city-sarasota-code-29.5-8-erosion', 'City of Sarasota Code §29.5-8')}). The city's own building-permit guidelines don't name a specific exemption for a patio, pool deck or paver surface on private property, so the guidance is direct: \"When in doubt... call the City Building Division\" at 941-263-6494 ({src('city-sarasota-bp-guidelines', 'City of Sarasota, Building Permit Requirement Guidelines')}). Zoning sets maximum impervious coverage by district, from 60 percent in RSF-E up to 75 percent in RSF-2 through RSF-4, with the city's Coastal Islands Overlay, covering Lido, St. Armands, Bird Key and similar neighborhoods, capping coverage at 70 percent regardless of the underlying zone ({src('city-sarasota-zoning-vi-203-impervious', 'City of Sarasota Zoning Code §VI-203')}; {src('city-sarasota-zoning-vi-907-isod', 'City of Sarasota Zoning Code §VI-907')}).</p>"),
        sec("Sarasota County, Including Siesta Key",
            f"<p>County code requires a Right-of-Way Use Permit for all work in the county right-of-way, with driveway culverts handled as their own sub-permit: culvert pipe goes in before home construction when possible, runs 20 to 24 feet in length, and must meet size and grade standards set by the County Engineer ({src('sarasota-county-row-permit', 'Sarasota County Code §124-48')}; {src('sarasota-county-124-255-culverts', 'Sarasota County Code §124-255')}). Patio, pool deck and paver permit specifics weren't confirmed directly from a fetched county Building Division page for this guide; search summaries suggest driveway repair without culvert work and some on-grade patios may be permit-exempt, but confirm that directly with Planning & Development Services at 941-861-5000 before assuming either way ({src('sarasota-county-building-page', 'Sarasota County Building')}). Retaining walls over 4 feet need engineered drawings ({src('sarasota-county-22-63-retaining-walls', 'Sarasota County Code §22-63')}). {city('siesta-key')} and the county's other coastal barrier islands carry an extra layer: the county's own Gulf Beach Setback Line bars construction or excavation seaward of that line, on top of any FDEP Coastal Construction Control Line permit the state requires for the same stretch of beach ({src('sarasota-county-54-723-gbsl', 'Sarasota County Code §54-723')}; {src('fdep-cccl-program', 'FDEP CCCL Program')}).</p>"),
        sec("City of Venice",
            f"<p>Venice requires a right-of-way use authorization from its Engineering Department before any construction in the city right-of-way, and the city specifically allows a License Agreement for cases like pavers installed over existing concrete under its own paver installation guidelines ({src('venice-engineering-permits', 'City of Venice, Engineering')}). Driveway openings are capped by frontage: one opening per street for lots under 80 feet, two for lots between 80 and 200 feet, with one more allowed per extra 100 feet beyond that ({src('venice-ldr-3.1-general-standards', 'Venice LDR §3.1')}). An older, third-party-hosted copy of the city's building permit guidelines lists decks and patios built directly on grade without footings as not requiring a permit; confirm that is still current with the Building Division at 941-882-7547 before skipping a step ({src('venice-bp-guidelines-3rdparty', 'Venice Building Permit Guidelines')}). Retaining walls need a zoning permit, with height counted toward any fence built on top of the wall, though the city hasn't published a numeric threshold for when engineering kicks in ({src('venice-ldr-3.8-walls', 'Venice LDR §3.8')}).</p>"),
        sec("City of North Port",
            f"<p>North Port's Right-of-Way Use Permit application lists \"Culvert/Driveway/Sidewalk/Concrete Slab\" as a single work category, with the applicant required to restore the roadway, right-of-way and swales before Public Works signs off ({src('north-port-row-permit-application', 'City of North Port, ROW Use Permit')}). City code requires a one- or two-family home to connect to the right-of-way with a driveway of \"concrete, brick paver, or other material approved by the Public Works Department,\" with front-load garage driveways at least 18 feet long and at least 10 feet wide at the property line ({src('north-port-uldc-4.4.1-driveway', 'North Port ULDC §4.4.1')}). On impervious surface limits, North Port's code allows \"impervious surface areas\" to be offset with pervious pavers or other permeable material, an option worth asking about on a tight lot near the ISR cap ({src('north-port-uldc-3.6.13-pervious-pavers', 'North Port ULDC §3.6.13')}). No city-published exemption was found for a patio, pool deck or paver surface built entirely on private property; the Building Department applies the 2026 HB 803 exemption through a written request rather than an automatic waiver ({src('north-port-permitting', 'North Port Permitting')}).</p>"
            + table("Sarasota County permit snapshot",
                    ["Jurisdiction", "Driveway", "Patio / pavers", "Contact"],
                    [["City of Sarasota", "City engineer permit, ROW", "No published exemption; confirm with Building", "941-263-6494"],
                     ["Sarasota County", "ROW Use Permit; culvert sub-permit", "Confirm with Planning & Development Services", "941-861-5000"],
                     ["City of Venice", "ROW use authorization; openings capped by frontage", "On-grade decks/patios may be exempt; confirm current rule", "941-882-7547"],
                     ["City of North Port", "ROW Use Permit (driveway/culvert/slab)", "No published exemption; confirm with Building Department", "941-429-7044"]],
                    "Fees, categories and exemptions change; confirm current rules with each office before you budget a project.")),
        sec("Coastal Setbacks: One More Layer on Barrier Island Lots",
            f"<p>A Gulf-front or near-Gulf lot on {city('siesta-key')} or {city('longboat-key')} can need both the city or county's ordinary driveway and patio review and a state coastal permit on top of it. FDEP's Coastal Construction Control Line program regulates structures and activities seaward of the CCCL line specifically because that work can affect beach erosion, dune stability or public beach access, and it issues that permit separately from any local building or right-of-way approval ({src('fdep-cccl-program', 'FDEP CCCL Program')}). The exact field-permit categories for minor hardscape like a patio or paver walkway weren't confirmed in this research, so a barrier-island project worth checking with FDEP directly at 850-245-2094 before finalizing design, alongside whatever the city or county requires.</p>"),
        sec("Do You Need a Notice of Commencement on the Suncoast Too?",
            f"<p>The same statewide rule applies here as in Orlando-area counties: a Notice of Commencement gets recorded once a driveway, patio or paver contract passes $2,500, and a copy has to be on file with the permitting office before the first inspection once the contract passes $5,000 ({src('fs713-13', 'F.S. 713.13')}; {src('fs713-135', 'F.S. 713.135')}). Sarasota, Venice and North Port all route permit applications through online portals that flag this requirement directly.</p>"),
        sec("A Quick Example",
            f"<p>Say you have a paver driveway and front walkway project on a {city('venice')} lot with 90 feet of frontage. The property qualifies for up to two driveway openings under the city's frontage rule, and any apron work in the right-of-way needs the Engineering Department's authorization regardless of how many openings the lot uses. A similar project a few miles away in unincorporated {city('sarasota')}-side Sarasota County instead routes through the county's Right-of-Way Use Permit, with its own culvert rules applying if the lot has an open drainage ditch out front.</p>"),
        sec("Related Reading",
            ul([svc("concrete-driveways"), svc("paver-patios"),
                post("lakewood-ranch-arc-approval-hardscape", "Lakewood Ranch ARC approval for hardscape"),
                post("saltwater-pools-and-coastal-salt-air-hardscape", "protecting hardscape from coastal salt air"),
                a("/faq/cost-and-permits/", "the cost and permits FAQ")])),
    ])
    faqs = [
        faq("Does the City of Sarasota require a permit for a patio or pavers?",
            f"The city hasn't published a specific exemption for a patio, pool deck or paver surface built entirely on private property, so the Building Division's own guidance is to call and confirm before assuming either way ({src('city-sarasota-bp-guidelines', 'City of Sarasota')})."),
        faq("What is the Gulf Beach Setback Line and does it affect my patio?",
            f"It's Sarasota County's own line barring construction or excavation seaward of it on Gulf-fronting beaches, applying on top of any state FDEP Coastal Construction Control Line permit for the same property ({src('sarasota-county-54-723-gbsl', 'Sarasota County Code §54-723')}). It matters most for a patio, deck or walkway planned close to the beach on an island like Siesta Key."),
        faq("How many driveways can a Venice home have?",
            f"It depends on frontage: one opening per street for lots under 80 feet, two for lots between 80 and 200 feet, and one additional opening per extra 100 feet of frontage beyond that ({src('venice-ldr-3.1-general-standards', 'Venice LDR §3.1')})."),
        faq("Does North Port allow pervious pavers to offset impervious surface limits?",
            f"Yes. City code allows impervious surface area to be offset with pervious pavers or other permeable material, as long as the owner keeps that material functioning as a pervious surface going forward ({src('north-port-uldc-3.6.13-pervious-pavers', 'North Port ULDC §3.6.13')})."),
        faq("Do I need both a county permit and an FDEP CCCL permit on Siesta Key?",
            f"On a lot seaward of the Coastal Construction Control Line, often yes; the state CCCL permit is separate from whatever driveway, patio or ROW permit Sarasota County itself requires for the same project ({src('fdep-cccl-program', 'FDEP CCCL Program')})."),
    ]
    return page("/blog/sarasota-county-driveway-patio-permits/", "post",
                "Driveway and Patio Permits in Sarasota, Venice, North Port",
                "Sarasota, Venice and North Port each require a right-of-way permit for driveway work, with different patio rules. Suncoast guide, October 2026.",
                "Driveway and Patio Permits in Sarasota, Venice and North Port",
                capsule("The City of Sarasota, Sarasota County, Venice and North Port all require a right-of-way permit for driveway or apron work, while patio and paver rules on private property differ by jurisdiction and are worth confirming directly. Barrier-island lots on Siesta Key and similar coastal areas can need a state FDEP coastal permit on top of the local one. As of October 2026, each office's current fee and exemption list is the one to check before scheduling work."),
                body, faqs=faqs,
                sources=["city-sarasota-code-29.5-7-curb-cut-driveway", "city-sarasota-code-29.5-8-erosion", "city-sarasota-engineering-row",
                         "city-sarasota-bp-guidelines", "city-sarasota-zoning-vi-203-impervious", "city-sarasota-zoning-vi-907-isod",
                         "sarasota-county-row-permit", "sarasota-county-124-255-culverts", "sarasota-county-22-63-retaining-walls",
                         "sarasota-county-54-723-gbsl", "sarasota-county-building-page", "venice-ldr-9.1-row-definition",
                         "venice-ldr-3.1-general-standards", "venice-ldr-3.8-walls", "venice-engineering-permits",
                         "venice-bp-guidelines-3rdparty", "north-port-row-permit-application", "north-port-uldc-4.4.1-driveway",
                         "north-port-uldc-3.6.13-pervious-pavers", "north-port-permitting", "fdep-cccl-program", "fdep-cccl-apply",
                         "fs713-13", "fs713-135"],
                related=[("/concrete-driveways/", "concrete driveways"), ("/paver-patios/", "paver patios and walkways"),
                         ("/blog/lakewood-ranch-arc-approval-hardscape/", "Lakewood Ranch ARC approval"),
                         ("/blog/saltwater-pools-and-coastal-salt-air-hardscape/", "protecting hardscape from salt air"),
                         ("/faq/cost-and-permits/", "cost and permits FAQ")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways", image="interlocking-pavers", form=False)


def get_pages():
    return [artificial_turf_rain_and_storms(), orange_county_permits(), osceola_county_permits(),
            seminole_county_permits(), lake_polk_permits(), sarasota_county_permits()]
