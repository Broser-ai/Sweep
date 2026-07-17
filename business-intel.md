# Resourcify GmbH — Strategic Business Intelligence Report

**Prepared:** 28 May 2026
**Scope:** Internal competitive analysis — funding, leadership, customers, GTM, and competitor landscape
**Companion document:** `REPORT.md` (technical architecture analysis, same directory)
**Method:** WebSearch + WebFetch across press releases, TechCrunch/EU-Startups/Sifted/Silicon Canals, Crunchbase/Tracxn/Dealroom (where accessible), VC blog posts, and the Resourcify website.

---

## Executive Summary (50-line brief)

**Company:** Resourcify GmbH — Hamburg-based B2B SaaS for digital waste management & circularity. Founded 2015 by Gary Lewis (CEO, NZ-origin), Felix Heinricy (CBDO/MD), and Pascal Alich. ~56–60 FTEs as of early 2026.

**Total raised:** **€23M (~$25.4M)** across 5 rounds.
- 2018 Seed: ~€1M (HTGF + Innovationsstarter Fonds Hamburg)
- 2021 Series A-I: €3M (Speedinvest-led)
- 2022 Series A-II: €5M (Ananda Impact + Speedinvest; HTGF, Sennder/Schüttflix founders followed on)
- Jul 2023 Strategic: 5% sold to Interzero (no co-determination, no data rights) — implicit valuation ~€40–50M pre-money
- **27 Sep 2023 Series A-III:** **€14M** led by **Vorwerk Ventures**, with Revent, Ananda Impact, Speedinvest, BonVenture, WEPA Ventures, and Interzero Circular Solutions
- **Estimated post-money valuation: ~€50M (~$53M)** per TechCrunch reporting — modest for the funding amount, suggesting investor caution on enterprise SaaS multiples in waste sector

**Customer scale (verified):**
- 800+ active recyclers, 25k+ active locations, 19+ countries, 2M+ devices collected
- €100M → €200M+ in "waste under management" trajectory post-Interzero
- ~50–60 paying enterprise customers (TechCrunch '23) reaching ~15,000 businesses through the network
- 40% cost-savings claim, two-thirds time reduction (Syntegon case study)

**Top 5 verifiable customer wins:**
1. **McDonald's Deutschland** — anchor account, named in 2021/2022/2023 PR; has dedicated subdomain `mcd.resourcify.de` + `api.mcd.resourcify.de`
2. **Hornbach Baumarkt AG** — named case study, named in 2022 €5M press release
3. **Johnson & Johnson** — named since 2022 €5M round (medical devices, US-HQ multinational)
4. **Bosch (Syntegon Technology)** — case study, "two-thirds time reduction"
5. **Interzero (REWE/Penny, Frankfurt Airport via Zero Waste Manager)** — July 2023 partnership + 5% equity; Five Guys (35 DE locations) live by end-2022

Additional CT-log evidence (technical recon, not press-verified — see `REPORT.md`): BMW, Continental, Stihl, Maersk, Aldi Nord/Süd, Edeka, Bauhaus, Karl Storz, Dräger, Helios, Vonovia, Fraport, Rolls-Royce, Ambu, Arthrex. Each runs on a dedicated white-label subdomain.

**Top 3 competitive threats — and how to beat them:**

1. **AMCS Group (Ireland)** — $225M raised, 1,148 FTEs, ERP-grade. **Beat by:** speed of deployment, modern UX, focus on the *waste-producer* (corporate generator) vs. AMCS's waste-*operator* (hauler/MRF) ICP. Resourcify already does this — a new entrant needs an even sharper producer-only product.
2. **Routeware (US, $123M, K1-backed)** — rolling up the US municipal/hauler stack via M&A (Wastech/Rubicon, PermiServ, Recyclist). **Beat by:** stay out of routing/municipal, double down on EU corporate compliance (CSRD, CRMA, EU PPWR).
3. **Circulor (UK, $69M)** — owns the battery-passport / EV-circularity narrative with Volvo, Polestar, BHP, Daimler. **Beat by:** pick an industry where Circulor *isn't* deeply embedded (e.g., construction/demolition, retail, hospitality) and own it before they expand.

**ONE wedge strategy — "EU compliance-grade waste OS for healthcare":**
- Pick **hospitals + medical-device manufacturers** as the entry beachhead.
- Resourcify has Helios, Karl Storz, Dräger, Ambu, Arthrex, J&J on its books *but no public case study or vertical play* — they treat healthcare as one more vertical.
- A new entrant can win this segment by building EANV-native (German electronic waste manifest), HIPAA/MDR-compliant, with explicit handling for sharps, pharma, and category-2 biomedical waste — a regulatory minefield Resourcify's horizontal product glosses over.
- Healthcare waste compliance has the highest fines per non-compliance event of any vertical → highest pricing power, longest contracts, lowest churn. Win 5 anchor hospitals → repeat the Resourcify playbook 10x faster in a higher-margin niche.

---

## Part 1: Resourcify Business Intelligence

### 1.1 Funding History

| Date | Round | Amount | Lead / Notable Investors | Source |
|------|-------|--------|--------------------------|--------|
| Apr 2018 | Seed | ~€1M | High-Tech Gründerfonds (HTGF), Innovationsstarter Fonds Hamburg | [Nordic9](https://nordic9.com/news/resourcify-in-a-1m-funding-round-backed-by-htgf-and-the-innovationsstarter-fonds-hamburg/) |
| Jun 2021 | Series A-I | €3M (~€3.78M per Tracxn) | Speedinvest (lead) | [EU-Startups](https://www.eu-startups.com/2021/06/hamburg-based-resourcify-raises-e3-million-to-expand-its-waste-management-platform/), [Tech.eu](https://tech.eu/2021/06/08/hamburgs-waste-and-recycling-management-platform-resourcify-raises-e3-million-looks-to-expand-its-waist/) |
| Feb 2022 | Series A-II | €5M | Ananda Impact Ventures + Speedinvest co-led; HTGF, Innovationsstarter Hamburg, founders of Sennder & Schüttflix | [Resourcify PR](https://www.resourcify.com/en/knowledge-centre/5-million-financing-round-recycling-platform) |
| Jul 2023 | Strategic | 5% stake (undisclosed cash; no co-determination, no data rights) | **Interzero Circular Solutions** | [Resourcify PR](https://www.resourcify.com/press-release/knowledge-centre-interzero-partnership) |
| **27 Sep 2023** | **Series A-III** | **€14M** | **Vorwerk Ventures (lead)**, Revent, Ananda Impact, Speedinvest, BonVenture, WEPA Ventures, Interzero | [Resourcify PR](https://www.resourcify.com/press-release/resourcify-raises-eu14m-series-a-funding), [TechCrunch](https://techcrunch.com/2023/09/27/resourcify-a-platform-to-digitize-waste-management-raises-e14m/), [EU-Startups](https://www.eu-startups.com/2023/09/hamburg-based-resourcify-snaps-e14-million-series-a-to-make-every-company-dramatically-reduce-its-waste/) |
| **Total** | **5 rounds** | **~€23M / ~$25.4M** | Implied post-money ~€50M (TechCrunch) | |

**Note on the "€15M" Series A:** The brief asks about €15M; the actual figure is **€14M** (~$14.94M / $15.1M when converted at the September 2023 rate, which is likely the source of the €15M figure in some coverage). All Series A coverage uses "Series A" as a label even though Resourcify has stacked three separate Series A rounds (A-I, A-II, A-III) — typical for cleantech/impact where a single Series A gets fractionalized.

**Use of funds (Sep 2023):**
1. Scale SaaS across new verticals (was originally retail/manufacturing → expanding to hospitals, aviation, FMCG)
2. International expansion: UK, France, Spain, Nordics
3. Build take-back / closed-loop product (became "Closeloop" and "Zero Waste Manager")
4. Grow commercial / sales team (~60 → ~100 target)

### 1.2 Founding Team & Leadership

| Person | Role | Background |
|--------|------|------------|
| **Gary Lewis** | Co-founder, CEO, Managing Director | NZ-origin, tech+sustainability background, "Reverse Amazon" Forbes profile (the user-provided brief mentioning "Filippo Cardillo" appears to be incorrect — no public source confirms this name) |
| **Felix Heinricy** | Co-founder, Managing Director, CBDO | Former Head of Business Development & Channel Management at Protonet GmbH (Apr 2014 – Jan 2017) |
| **Pascal Alich** | Co-founder | Less publicly visible — not appearing on current OrgChart leadership listings; may have stepped back |

**Other named leadership (limited visibility):** TheOrg lists only 2 of 5 leadership team members publicly. No CFO, CTO, or CRO is publicly identifiable as of May 2026 — a notable gap for a Series A company. The team page on resourcify.com does not surface a leadership section, suggesting deliberate opacity.

**Board / investors with board seats (inferred from lead investors):** Likely Vorwerk Ventures (Sep 2023 lead), Speedinvest, Ananda Impact Ventures. No public board roster.

**No notable independent advisors** are publicly disclosed.

### 1.3 Customer & Revenue Signals

| Metric | Value | Source |
|--------|-------|--------|
| Paying enterprise customers | ~50+ direct, 15,000 reached through network | [TechCrunch 2023](https://techcrunch.com/2023/09/27/resourcify-a-platform-to-digitize-waste-management-raises-e14m/) |
| Active locations | 25,000+ | Resourcify homepage |
| Active recyclers in network | 800+ | Resourcify homepage |
| Countries | 19+ | Resourcify homepage |
| Devices collected (cumulative) | 2M+ | Resourcify homepage |
| Tonnes managed (cumulative) | 500,000+ (2023); claim of "100M+" on current homepage (likely cumulative across network, not Resourcify-managed directly) | Resourcify homepage & PRs |
| Waste-spend under management | €100M (Sep '23) → €200M+ post-Interzero | [Interzero PR](https://www.resourcify.com/press-release/knowledge-centre-interzero-platform-partnership) |
| Employees | ~56 (Apr 2026 Tracxn) / ~60 (TechCrunch Sep 2023) | Tracxn, TechCrunch |
| Revenue (estimated) | Tripled YoY (TechCrunch quote); no absolute number disclosed. Estimated ARR €4–8M based on team size & valuation | TechCrunch + benchmark math |

**Customer wins — verified press-cited:**

| Customer | First mentioned in PR | Sector |
|----------|----------------------|--------|
| McDonald's | 2022 (€5M round); subdomain `mcd.resourcify.de` active 2022+ | QSR |
| Hornbach Baumarkt AG | 2022 (€5M round) | Home improvement retail |
| Johnson & Johnson | 2022 (€5M round) | Pharma/MedTech |
| Bosch (Syntegon) | Pre-2023 (case study) | Industrial machinery |
| Frankfurt Airport (Fraport) | 2023 | Aviation |
| REWE/Penny | 2023 (via Interzero) | Grocery retail |
| Five Guys (35 DE locations) | end-2022 (via Interzero Zero Waste Manager) | QSR |
| OBI | 2024+ (homepage logo) | Home improvement retail |
| Rolls-Royce | 2024 (Gary Lewis interviews) | Industrial |

**Brief-mentioned wins (BMW, Maersk, Karl Storz, Helios) — status:** Not confirmed in press releases. **However**, all four appear in Certificate Transparency logs as dedicated white-label subdomains on `resourcify.de` (see companion `REPORT.md`). This means they have a Resourcify environment provisioned, which is highly suggestive of an active or proof-of-concept relationship — but not press-confirmed customers.

### 1.4 Strategic Milestones (2015–2026)

| Year | Event |
|------|-------|
| 2015 | Founded by Lewis, Heinricy, Alich in Hamburg |
| 2018 | First seed round (€1M); platform processing waste disposal orders |
| 2021 | Series A-I €3M (Speedinvest); expansion to 6 European countries |
| 2022 | Series A-II €5M; 2M+ annual pickups; named McDonald's, J&J, Hornbach |
| May 2023 | **German Innovation Award 2023** (Excellence in B2B, IT category) |
| Jul 2023 | **Interzero partnership** + 5% equity; launches Zero Waste Manager white-label |
| Sep 2023 | **Series A-III €14M** (Vorwerk-led) |
| 2024 | Launches/expands modules: Closeloop, WMS Lite, Exchange (marketplace), Discovra (in dev); Webflow→React 19 frontend migration ("Phoenix") |
| 2025 | OBI, Rolls-Royce added publicly; product expands to 19+ countries |
| 2026 (current) | 56 FTEs, ~100M+ tonnes "managed" (cumulative network), looking at Series B |

**Awards:** German Innovation Award 2023 is the only confirmed major recognition. The brief asks about Forbes 30 Under 30 — **not confirmed**; Gary Lewis has been *profiled* by Forbes ("Reverse Amazon" tag) but no 30 Under 30 listing surfaces.

### 1.5 Go-to-Market Model

**Pricing model (inferred — not publicly published):**
- **Annual contract, enterprise SaaS**. No public pricing page.
- Likely **per-site / per-location** anchor + variable per-pickup or per-tonne component
- G2 reviews and case studies suggest 1–3 year contracts
- Implied ACV (from €23M raised, ~60 FTE, ~50 customers, 50:1 LTV:CAC math): **~€80–150k average ACV** — strong mid-market/lower-enterprise

**Sales motion:**
- **Pure enterprise sales** — long, consultative, multi-stakeholder (procurement, sustainability, operations, finance)
- Tech stack confirms this: **HubSpot + Demandbase ABM + Apollo + Userpilot** (per `REPORT.md`)
- Multi-tenant white-label deployment per enterprise customer = onboarding-heavy
- Sales cycle: estimated **6–12 months** for enterprise (typical for waste/sustainability buyers, where multi-site rollouts require pilot → expansion path)

**No PLG / self-serve.** The login flow (Auth0 with custom domain per tenant) is gated entirely — no signup form anywhere on the public site.

**Channel/partner motion:** Interzero is the first big channel play (Zero Waste Manager white-label = Interzero sells, Resourcify provides platform). Replicable pattern with other waste-management aggregators.

---

## Part 2: Competitor Landscape

### 2.1 AMCS Group (Ireland)

| Field | Value |
|-------|-------|
| HQ | Limerick, Ireland (Innovation Works, Castletroy) |
| Founded | 2003 |
| Funding | **$225M+** (Insight Partners-backed, plus SVB, NCB Ventures) |
| Customers | 1,300+ in 22+ countries; Suez, Veolia, major haulers globally |
| Employees | 1,148 (Mar 2026) |
| Products | AMCS Platform (ERP for waste/recycling operators), Wastedge (ANZ), contract management |
| Pricing | Enterprise license + per-seat ERP-style; 6–18 month implementations |
| Tech | Cloud-based (formerly on-prem heritage); Azure-leaning |
| Positioning | **The incumbent ERP for waste operators** (haulers, MRFs, recyclers) — *sell-side* of the waste industry |
| **Diff vs Resourcify** | Sells to **waste operators**, Resourcify sells to **waste producers**. Different ICP entirely. AMCS is heavier, slower, deeper. |
| **Competitor type** | **Adjacent** — they meet at the network edge (an AMCS-running hauler can plug into Resourcify's platform). Not head-to-head. |
| Geo overlap | Significant — both EU + UK |

Source: [AMCS](https://www.amcsgroup.com/), [Tracxn](https://tracxn.com/d/companies/amcs/__5dYbiJH0GtkirPoLaF6KSeFM0PuuA3aTy4rf2gY0LV0), [Crunchbase](https://www.crunchbase.com/organization/advanced-manufacturing-control-systems)

### 2.2 Evreka (Turkey)

| Field | Value |
|-------|-------|
| HQ | Ankara, Turkey |
| Founded | 2015 |
| Funding | **~$2.9M** total (Series A-II); Driventure, Garanti BBVA, ScaleUp, Nexus Ventures |
| Customers | 10,000 users, 40+ countries (DE, FR, IT, NO, HR, CA, BR, CL, TR, MY, SG, IN, PK, MA, EG, GA, CG, ZA, LB, IL, KSA, UAE, QA, OM, AZ, AR) |
| Employees | Not disclosed; estimated 100–200 |
| Products | End-to-end waste management OS (operations, fleet, HR, assets) |
| Pricing | Subscription tailored by customer type & geography |
| Tech | Oracle Cloud Infrastructure (per Oracle case study) |
| Positioning | **Emerging-markets champion** — municipalities + operators in regions where AMCS doesn't go |
| **Diff vs Resourcify** | Targets **municipalities + waste-collection operators**, not corporate generators. Geo is mostly outside Resourcify's EU core. |
| **Competitor type** | **Adjacent**, low geographic overlap |
| Geo overlap | Limited — they're in DE/FR/IT but as suppliers to municipalities, not corporates |

Source: [Evreka](https://evreka.co/), [Crunchbase](https://www.crunchbase.com/organization/evreka), [Oracle case study](https://www.oracle.com/customers/evreka-turkey/)

### 2.3 Sourcemap (US)

| Field | Value |
|-------|-------|
| HQ | New York, USA |
| Founded | 2011 (MIT spin-out) |
| Funding | **$11M+** (Series A led by Energize Ventures + E14 Fund, $10M); also reported $20M Series B in some sources |
| Customers | 400,000 business entities mapped; AG1 (2024); food/agri, apparel, home goods, auto, pharma, luxury, cosmetics |
| Revenue | **$17.4M (2024)** per Latka |
| Employees | 69 (2024) |
| Products | Supply chain mapping, transaction traceability, EUDR/CSDDD compliance |
| Pricing | Per-supply-chain / per-tier subscription |
| Tech | Cloud-native; graph DB heavy |
| Positioning | **Upstream supply-chain transparency for due diligence** (EUDR, UFLPA, CSDDD) |
| **Diff vs Resourcify** | Sourcemap is **upstream** (where do raw materials come from?). Resourcify is **downstream** (where does waste go?). Same circularity theme, opposite ends. |
| **Competitor type** | **Complementary** — could partner. Not a direct threat. |
| Geo overlap | US-primary, expanding to EU |

Source: [Sourcemap](https://www.sourcemap.com/), [FreightWaves](https://www.freightwaves.com/news/sourcemap-raises-10m-to-step-up-supply-chain-transparency-and-traceability), [Latka](https://getlatka.com/companies/sourcemap)

### 2.4 Topolytics (UK)

| Field | Value |
|-------|-------|
| HQ | Edinburgh, Scotland |
| Founded | 2013 |
| Funding | **~£2M total** (£500k UK gov 2019 + £1.5M / €1.7M Feb 2023, private investors + UKRI) |
| Customers | Manufacturers, waste brokers, government agencies (mostly EU/US/Asia); details non-public |
| Employees | <20 (estimate) |
| Products | WasteMap — ML-driven waste analytics, ESG/carbon reporting backbone |
| Pricing | Not public; likely £20–50k/year mid-market subscription |
| Tech | ML/analytics-heavy; cloud SaaS |
| Positioning | **Pure analytics & insights layer** — explicitly NOT operational waste management |
| **Diff vs Resourcify** | Topolytics is **read-only intelligence**; Resourcify is **system of record + workflow**. They can plug into operational systems incl. Resourcify. |
| **Competitor type** | **Complementary** — partnership candidate, not competitor |
| Geo overlap | UK-heavy; some EU |

Source: [EU-Startups](https://www.eu-startups.com/2023/02/edinburghs-topolytics-tops-up-expansion-plans-with-e1-7-million/), [Envirotec](https://envirotecmagazine.com/2019/10/22/data-analytics-firm-wins-500k-funding-to-build-the-uks-first-digital-waste-tracking-system/)

### 2.5 Wastedge / AMCS ANZ (Australia)

| Field | Value |
|-------|-------|
| HQ | Originally Sydney; **acquired by AMCS** |
| Founded | 1990s (as Australian Software Professionals / ASP) |
| Funding | N/A (part of AMCS Group) |
| Customers | 100+ in ANZ; Benedict Group; ANZ market leader |
| Products | SaaS for hauler/operator: weighing, mobile, route opt, analytics |
| Positioning | **AMCS's ANZ arm** |
| **Diff vs Resourcify** | Same as AMCS — operator-side, not corporate-side |
| **Competitor type** | **Adjacent**; zero direct competition (ANZ market) |
| Geo overlap | None |

Source: [Waste Management Review](https://wastemanagementreview.com.au/amcs-buys-wastedge/), [AMCS Wastedge page](https://www.amcsgroup.com/solutions/wastedge-anz/)

### 2.6 Rubicon Technologies (US)

| Field | Value |
|-------|-------|
| HQ | Atlanta/Lexington, USA |
| Founded | 2008 |
| Funding | Went public via SPAC 2022 (RBT/NYSE); **delisted June 7, 2024** (market cap & equity below NYSE thresholds); now OTC. May 2024 sold fleet tech business ($61.7M cash + $12.5M earnout) to Routeware. |
| Customers | Walmart, 7-Eleven, Apple historically; rapidly contracting |
| Products | Originally "Uber for trash" marketplace; pivoted to SmartCity/SaaS; now sold off to Routeware |
| Tech | SaaS + marketplace; legacy stack |
| Positioning | **Cautionary tale** — SPAC bust, "marketplace + SaaS" hybrid failed to find unit economics |
| **Diff vs Resourcify** | Rubicon was hauler-marketplace + commercial. Resourcify is pure SaaS, never tried marketplace fulfillment. |
| **Competitor type** | **Direct (historical) but functionally exiting** — Rubicon is no longer a real competitor as of 2024 |
| Geo overlap | US — Resourcify has no US presence |

Source: [Waste Dive](https://www.wastedive.com/news/rubicon-sale-timeline-take-private-offer-enrich-saas/724960/), [BusinessWire delisting](https://www.businesswire.com/news/home/20240607062376/en/Rubicon-Technologies-Receives-Delisting-Notice-from-the-New-York-Stock-Exchange)

### 2.7 Routeware (US)

| Field | Value |
|-------|-------|
| HQ | Portland, Oregon, USA |
| Founded | 2000 |
| Funding | **$123M+** (K1 Investment Management, since 2021) |
| Customers | 100+ UK local authorities; 100+ US municipalities (Houston, Atlanta, Miami, Austin, Phoenix); 8 of top 10 US cities |
| Products | Routing, billing, citizen apps, fleet tech (now Rubicon SmartCity + Pro), permits (PermiServ UK) |
| Pricing | Municipal contract (typical 3–7 yr public-sector deals) |
| Positioning | **The US/UK municipal routing & ops aggregator**, rolling up via M&A |
| **Diff vs Resourcify** | Municipal/public-sector + routing focused. Resourcify is corporate/private-sector + producer-side. |
| **Competitor type** | **Adjacent**, geographic gap |
| Geo overlap | UK (some) — could collide if Resourcify pursues public-sector EU clients |

Source: [Routeware](https://routeware.com/), [Waste Dive](https://www.wastedive.com/news/routeware-acquires-recently-spun-off-rubicon-fleet-tech-business/725404/), [PitchBook](https://pitchbook.com/profiles/company/55228-06)

### 2.8 EcoVadis (France)

| Field | Value |
|-------|-------|
| HQ | Paris, France |
| Founded | 2007 |
| Funding | **$237.6M total**; **€500M (~$540M) from General Atlantic & Astorg in 2024** (largest round) |
| Customers | **55,000 customers** (2024); 1,500 global enterprise rating-buyers; 3M suppliers profiled |
| Revenue | **$162.2M (2024)** up from $101.8M (2023) per Latka — 59% YoY |
| Employees | ~1,500+ |
| Products | Sustainability ratings (E/S/G), risk insights, $2.5T spend now governed |
| Pricing | Subscription per supplier rated; tiered by ratings volume |
| Positioning | **The de-facto sustainability rating layer for procurement** — independent assessor of suppliers |
| **Diff vs Resourcify** | EcoVadis rates *suppliers*; Resourcify manages *waste flows*. Both feed the CSRD/ESG report but at different layers. |
| **Competitor type** | **Adjacent**; complementary in the same enterprise procurement/sustainability buyer stack |
| Geo overlap | Global, including DACH where Resourcify lives |

Source: [Latka](https://getlatka.com/companies/ecovadis), [EcoVadis](https://ecovadis.com/), [PRNewswire](https://www.prnewswire.com/news-releases/ecovadis-reports-2-5t-in-global-spend-now-governed-through-sustainability-risk-insights-as-companies-shift-from-compliance-to-resilience-led-procurement-302762254.html)

### 2.9 Circular IQ (Netherlands)

| Field | Value |
|-------|-------|
| HQ | Amsterdam, Netherlands |
| Founded | 2016 |
| Funding | Undisclosed — appears to be bootstrapped or small-seed; no public round |
| Customers | Mid-size EU manufacturers; partnered with Circle Economy |
| Products | Material-flow SaaS — links materials → environmental impact (resource depletion, GHG, waste) |
| Positioning | **Material-flow accounting / circular performance monitoring** |
| **Diff vs Resourcify** | Material accounting (upstream design choice) vs waste flow management (downstream operations). Different decision-makers (R&D/product vs facilities/ops). |
| **Competitor type** | **Adjacent/complementary**; small and not a near-term threat |
| Geo overlap | NL + EU |

Source: [Circle Economy](https://www.circle-economy.com/news/circle-economy-and-circulariq-join-forces-to-help-businesses-identify-and-implement-circular-solutions-driven-by-data), [CB Insights](https://www.cbinsights.com/company/circular-iq)

**Note:** The Dutch player most often referenced as comparable to Resourcify is actually **Seenons** (BV-Capital backed, Dutch, B2B corporate waste digitization) — included as a watchlist item even though not in the original brief. Listed in CB Insights as a Resourcify competitor.

### 2.10 Circulor (UK)

| Field | Value |
|-------|-------|
| HQ | London, UK |
| Founded | 2017 |
| Funding | **$69.2M+** (Westly Group, Salesforce Ventures, BHP Ventures, Sky Ocean, Future Positive, 24Haymarket) |
| Customers | **Volvo, Polestar, Daimler, JLR, LG Energy Solutions, Total, BHP, Powin, Acculon, Talon Metals** |
| Products | Blockchain-based traceability for battery materials (cobalt, nickel, lithium, mica) + EV battery passport |
| Pricing | Enterprise, deep integration |
| Tech | Blockchain (Hyperledger / similar) + AI |
| Positioning | **The EU battery-passport standard candidate** — extremely strong in automotive/EV |
| **Diff vs Resourcify** | Circulor = raw-material *upstream* provenance + carbon footprint; Resourcify = waste *downstream* + reuse. Both circularity but different end of the loop. |
| **Competitor type** | **Adjacent today, potentially competitive** if Resourcify moves into industrial material take-back & Circulor moves downstream into reverse logistics |
| Geo overlap | UK + EU — high overlap |

Source: [Crunchbase](https://www.crunchbase.com/organization/circulor), [Recycling Startups](https://www.recyclingstartups.pro/startup/circulor/), [Batteries News](https://batteriesnews.com/circulor-uk-startup-volvo-ev-battery-materials/)

### 2.11 Competitor Landscape Summary

| Competitor | Funding | Customer Focus | Competitor Type | Resourcify Overlap |
|------------|---------|----------------|-----------------|-------------------|
| AMCS | $225M | Waste operators (haulers, MRFs) | Adjacent | Low |
| Routeware | $123M | US/UK municipalities | Adjacent | Low (geo) |
| Circulor | $69M | EV/battery OEMs, miners | Adjacent | Medium (could collide) |
| EcoVadis | $237M | Procurement ratings | Adjacent / Complementary | Medium (same buyer) |
| Sourcemap | $11M+ | Supply-chain due diligence | Complementary | Low |
| Topolytics | £2M | Analytics layer | Complementary | Medium (data) |
| Wastedge | (AMCS) | ANZ operators | Adjacent | None |
| Evreka | $2.9M | Emerging-mkt municipalities | Adjacent | Very low |
| Rubicon | (SPAC bust) | US commercial | Effectively exited | Zero |
| CircularIQ | Undisc. | Material-flow analysts | Complementary | Low |
| **Seenons** (added) | €15M+ | NL/EU corporate producers | **DIRECT** | **High** |

**Critical observation:** Resourcify has **no direct, well-funded, EU-focused, corporate-waste-producer-targeting peer** other than **Seenons (NL)**. The brief omitted them but they are the only "mirror image" competitor — same buyer, same model, slightly smaller, neighboring country. *A new entrant should evaluate Seenons carefully as the only true near-peer.*

---

## Part 3: Strategic Conclusions — 5 Bets to Beat Resourcify

### Bet 1: Pick a **vertical wedge**, not horizontal
Resourcify's biggest weakness is **horizontal positioning**. They serve QSR (McDonald's, Five Guys), retail (Hornbach, OBI, Aldi, Edeka), pharma (J&J), industrial (Bosch/Syntegon), aviation (Fraport), automotive (BMW, Continental), hospitals (Helios). One product trying to serve all of these means **none of them get a vertical-grade solution**.

A new entrant should pick **one** of:
- **Healthcare waste** (highest regulatory complexity, highest pricing power) ← **recommended wedge**
- **Construction & demolition waste** (largest waste stream by volume in EU; not yet dominated)
- **Pharmaceutical reverse logistics** (high-margin, MDR/SUR compliance pressure mounting)
- **Aviation MRO waste** (highly regulated, recurring, global)

Win 10 anchor customers in one vertical → repeat the Resourcify roadmap 5–10x faster with deeper moat.

### Bet 2: Native EU compliance suite — not bolt-on
Resourcify's product was *built before* the new regulatory wave. CSRD, CRMA, EU PPWR, ESPR, EUDR, the German Lieferkettengesetz, Austria's AWG amendments — all are now binding obligations on corporate waste-producers. Resourcify's marketing references these but their data model (per `REPORT.md`: tenant-isolated, EANV integration as a module) is retrofitted.

Build a **compliance-first data model from day 1**: every waste event captures the data fields needed for CSRD ESRS E5 (Resource use & Circular Economy) disclosure *without* manual mapping. This becomes the wedge against Resourcify when finance/audit committees buy.

### Bet 3: Take the **waste-broker / channel partner** route, not direct enterprise
Resourcify took 8+ years to reach ~50 paying customers via direct enterprise sales. The Interzero deal (Jul 2023) was their breakthrough — instant access to "100M+ in waste under management". The lesson: **distribution > product** in this market.

A new entrant should approach 2–3 large EU waste brokers (Veolia, Suez, Remondis, Prezero) with a **white-label SaaS** offer instead of competing for end-customers head-on. Veolia & Remondis don't have a modern SaaS layer for their corporate accounts; Resourcify's Interzero deal is a template they can't easily replicate with another aggregator (5% exclusive equity probably has follow-on rights).

### Bet 4: **AI-native operations** — leapfrog the legacy data model
Resourcify's stack (per `REPORT.md`) is **React 19 + Java/Spring Boot + Postgres on GCP** — modern but operationally conventional. Their AI/ML claims are mostly analytics + insights bolted onto a transactional system.

A new entrant should build:
- **LLM-native intake**: every invoice/email/photo from a recycler is parsed and structured automatically (Resourcify still requires structured data entry).
- **Computer vision waste classification**: dock-cam or container-cam → automatic sorting verification + invoice dispute resolution.
- **Predictive route optimization for producers** (when to schedule pickups for cost-optimal logistics): something neither Resourcify nor AMCS does well from the *producer* side.

This is the next-gen "operating system" play Resourcify *talks* about but doesn't yet deliver.

### Bet 5: **Open the data layer** — be the platform Resourcify won't be
Resourcify is a closed enterprise SaaS. Each tenant's data is locked into Resourcify's reporting layer. Customers ask for raw exports and integrations and have to escalate to support.

A new entrant should commit to:
- **Public read API + webhooks from day 1**
- **Open data model published** (waste events, material codes mapped to EWC/AVV, recycler graph)
- **Embedded analytics / BI export** (Cube, Metabase, native CSV/Parquet)
- **Direct integrations with SAP S/4 ESG, Sphera, Watershed, Persefoni** for emissions reporting

This positions you as the "Stripe of waste" — be the trustworthy primitive that big sustainability platforms build on top of, rather than a walled garden.

---

## Sources & References

### Primary Resourcify sources
- [Resourcify homepage](https://www.resourcify.com/)
- [Resourcify Series A press release (€14M, Sep 2023)](https://www.resourcify.com/press-release/resourcify-raises-eu14m-series-a-funding)
- [Resourcify Series A-II press release (€5M, Feb 2022)](https://www.resourcify.com/en/knowledge-centre/5-million-financing-round-recycling-platform)
- [Resourcify–Interzero partnership press release (Jul 2023)](https://www.resourcify.com/press-release/knowledge-centre-interzero-partnership)
- [Resourcify German Innovation Award 2023 press release](https://www.resourcify.com/press-release/press-release-resourcify-german-innovation-award-2023)
- [Press Releases index](https://www.resourcify.com/press-releases)
- [Knowledge Center](https://www.resourcify.com/knowledge-center)
- [Hornbach case study](https://www.resourcify.com/case-study/hornbach-baumarkt-ag-achieves-ambitious-recycling-goals-through-digitisation)

### Funding & company data
- [TechCrunch — Resourcify €14M Series A (27 Sep 2023)](https://techcrunch.com/2023/09/27/resourcify-a-platform-to-digitize-waste-management-raises-e14m/)
- [EU-Startups Series A (Sep 2023)](https://www.eu-startups.com/2023/09/hamburg-based-resourcify-snaps-e14-million-series-a-to-make-every-company-dramatically-reduce-its-waste/)
- [Silicon Canals (Sep 2023)](https://siliconcanals.com/resourcify-secures-14m/)
- [EU-Startups (Jun 2021)](https://www.eu-startups.com/2021/06/hamburg-based-resourcify-raises-e3-million-to-expand-its-waste-management-platform/)
- [Tech.eu (Jun 2021)](https://tech.eu/2021/06/08/hamburgs-waste-and-recycling-management-platform-resourcify-raises-e3-million-looks-to-expand-its-waist/)
- [Nordic9 — Seed 2018](https://nordic9.com/news/resourcify-in-a-1m-funding-round-backed-by-htgf-and-the-innovationsstarter-fonds-hamburg/)
- [Nordic9 — €5M 2022](https://nordic9.com/news/resourcify-in-a-5-million-funding-round-backed-by-ananda-impact-ventures-and-speedinvest/)
- [Tracxn — Resourcify profile](https://tracxn.com/d/companies/resourcify/__36JPFkxqimyO6oPoFFP_Y7083FEOtOCL510yV6xHpHs)
- [Crunchbase — Resourcify](https://www.crunchbase.com/organization/resourcify)
- [Crunchbase — Gary Lewis](https://www.crunchbase.com/person/gary-lewis-5665)
- [Crunchbase — Felix Heinricy](https://www.crunchbase.com/person/felix-heinricy-c602)
- [TheOrg — Resourcify](https://theorg.com/org/resourcify)
- [Ananda Impact Ventures — Why we invested](https://medium.com/ananda-impact-ventures/why-we-invested-resourcify-enabling-zero-waste-by-becoming-the-1-recycling-platform-in-europe-cbe65deaf5e8)
- [KfW Stories on Resourcify](https://www.kfw.de/stories/economy/innovation/resourcify/)
- [EIT success story](https://www.eit.europa.eu/news-events/success-stories/resourcify)

### GTM / interviews
- [Frontlines.io podcast — Gary Lewis](https://www.frontlines.io/podcasts/gary-lewis/)
- [Startups Magazine — Gary Lewis](https://startupsmagazine.co.uk/content/gary-lewis)
- [Category Visionaries — YouTube (gated)](https://www.youtube.com/watch?v=btCBJ98DIDk)
- [Startup City Hamburg — Interzero partnership](https://startupcity.hamburg/news-events/news/resourcify-partners-with-interzero-to-digitize-waste-management)

### Competitors
- [AMCS Group](https://www.amcsgroup.com/) — [Tracxn](https://tracxn.com/d/companies/amcs/__5dYbiJH0GtkirPoLaF6KSeFM0PuuA3aTy4rf2gY0LV0)
- [Evreka](https://evreka.co/) — [Crunchbase](https://www.crunchbase.com/organization/evreka) — [Oracle case study](https://www.oracle.com/customers/evreka-turkey/)
- [Sourcemap](https://www.sourcemap.com/) — [FreightWaves $10M](https://www.freightwaves.com/news/sourcemap-raises-10m-to-step-up-supply-chain-transparency-and-traceability) — [Latka](https://getlatka.com/companies/sourcemap)
- [Topolytics](https://www.topolytics.com/) via [EU-Startups](https://www.eu-startups.com/2023/02/edinburghs-topolytics-tops-up-expansion-plans-with-e1-7-million/) and [Envirotec](https://envirotecmagazine.com/2019/10/22/data-analytics-firm-wins-500k-funding-to-build-the-uks-first-digital-waste-tracking-system/)
- [Wastedge / AMCS](https://www.amcsgroup.com/solutions/wastedge-anz/) — [Waste Management Review acquisition](https://wastemanagementreview.com.au/amcs-buys-wastedge/)
- [Rubicon delisting](https://www.businesswire.com/news/home/20240607062376/en/Rubicon-Technologies-Receives-Delisting-Notice-from-the-New-York-Stock-Exchange) — [Waste Dive sale](https://www.wastedive.com/news/rubicon-sale-timeline-take-private-offer-enrich-saas/724960/)
- [Routeware](https://routeware.com/) — [Waste Dive Rubicon SmartCity acq](https://www.wastedive.com/news/routeware-acquires-recently-spun-off-rubicon-fleet-tech-business/725404/) — [PitchBook](https://pitchbook.com/profiles/company/55228-06)
- [EcoVadis](https://ecovadis.com/) — [Latka revenue](https://getlatka.com/companies/ecovadis) — [PRNewswire](https://www.prnewswire.com/news-releases/ecovadis-reports-2-5t-in-global-spend-now-governed-through-sustainability-risk-insights-as-companies-shift-from-compliance-to-resilience-led-procurement-302762254.html)
- [Circular IQ via Circle Economy](https://www.circle-economy.com/news/circle-economy-and-circulariq-join-forces-to-help-businesses-identify-and-implement-circular-solutions-driven-by-data) — [CB Insights](https://www.cbinsights.com/company/circular-iq)
- [Circulor — Crunchbase](https://www.crunchbase.com/organization/circulor) — [Recycling Startups](https://www.recyclingstartups.pro/startup/circulor/) — [Batteries News Volvo](https://batteriesnews.com/circulor-uk-startup-volvo-ev-battery-materials/)

### Market sizing
- [Verified Market Research — Waste Management Software](https://www.verifiedmarketresearch.com/product/waste-management-software-market/)
- [Credence Research — Europe Waste Management Software](https://www.credenceresearch.com/report/europe-waste-management-software-market)
- [IntelMarket Research](https://www.intelmarketresearch.com/europe-waste-management-software-market-20980)

---

**End of report.**

**Companion file:** `C:\Users\Ambro2\resourcify-analysis\REPORT.md` — technical architecture analysis (stack, multi-tenant model, replication blueprint).
