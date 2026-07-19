# How to import your AWS cloud emissions into Sweep - Sweep


**Description:** Automatically import AWS cloud emissions into Sweep to consolidate Scope 1, 2 and 3 data for faster, audit-ready carbon reporting.


## Content


Home
Insights
Blog
How to import your AWS cloud emissions into Sweep
Category
Blog
Last updated
May 29, 2026
Cloud infrastructure is one of the fastest-growing components of corporate Scope 3 emissions, and one of the hardest to measure accurately. For most organizations, getting clean, auditable cloud emissions data has required manual exports, spreadsheet manipulation, and significant back-and-forth with IT teams, before the numbers even reach a sustainability platform.
That changes today.
Sweep has built a complete cloud emissions measurement solution based on the
AWS Sustainability service
, the standalone emissions reporting service launched by Amazon Web Servicess. As an
AWS ISV-Accelerate partner fully deployed on AWS
, Sweep is uniquely positioned to connect directly to AWS emissions data. The integration enables enterprise customers to automatically consolidate their AWS cloud emissions data directly within Sweep, alongside Scope 1, 2 and 3 data from across their full operations, under a single methodology, traceable to source, and ready for external audit.
This connector fits naturally into our data ecosystem and delivers data quality that goes beyond what we expected. Sweep allows us to centralise not just the impact of our cloud infrastructure, but all the operational data that underpins our non-financial reporting.
Federica Del Fiume
ESG Manager, Quonto
Why cloud emissions are a critical gap and why now
Cloud infrastructure remains a major challenge in carbon reporting, particularly for companies with large AWS footprints. Sweep and Capgemini found that 61% of sustainability leaders spend more than four hours a week consolidating emissions data.
That burden is growing as CSRD, UK SRS, ISSB and California’s SB 253 expand Scope 3 reporting requirements.
AWS Sustainability gives companies programmatic access to Scope 1, 2 and 3 emissions data by service, region and account. Sweep’s connector automatically integrates that data into a company’s carbon baseline, eliminating manual exports and spreadsheets.
What you get: emissions data broken down by service, region, and account
The AWS Sustainability Console provides carbon emissions data across:
Scope 1:
direct emissions from AWS operations
Scope 2 (location-based and market-based):
indirect emissions from energy consumption, with or without renewable energy certificates (RECs) or Power Purchase Agreements (PPAs)
Scope 3:
upstream and downstream value chain emissions
All of this flows into Sweep broken down by AWS service (e.g. EC2, S3), region, and account, giving you the granularity needed to identify your cloud emissions hotspots and track progress over time.
How the integration works
Sweep automatically imports emissions data from AWS Sustainability using Amazon S3, with support for AWS emission factor versioning and near real-time processing. The integration is compatible with existing AWS infrastructure, including Redshift and Athena, as well as platforms like Snowflake and Microsoft SQL Server.
Setup overview
To configure the integration, you will need:
Access to your AWS management account
Permission to create S3 buckets, IAM users and BCM Data Exports
Terraform installed (recommended for infrastructure-as-code setup)
The setup process includes:
Creating an S3 bucket to store AWS carbon emissions exports
Configuring a BCM Data Export to send emissions data to that bucket
Creating a read-only IAM user for Sweep
Connecting the export to Sweep through the AWS connector
Applying a transformation rule to map AWS emissions data into Sweep’s data model
The integration supports Scope 1, 2 and 3 emissions data by service, region and account. Sweep recommends using location-based emissions values (LBM) by default, though market-based values (MBM) are also supported.
Important notes
AWS emissions data is usually published after the reporting month ends
AWS exports include account IDs, not account names
Filtering imports by account is not currently supported at connector level
The AWS Sustainability Console connector replaces the legacy AWS Cloud Carbon Footprint (CCF) connector
Ready to connect?
The AWS connector is available to all Sweep customers today. If you are already a customer, log in and follow the link to our help desk:
help.sweep.net
.
If you are not yet a Sweep customer and want to see how the platform can help you consolidate and report on your full carbon footprint
book a demo here
.
Contents
Why cloud emissions are a critical gap and why now
How the integration works
Ready to connect?
More stories
Reports
Verdantix on Sweep: The new standard for AI in sustainability
Reports
2026 Verdantix Green Quadrant: Sweep turns ESG data into strategic advantage
Carbon accounting
ESG management
Reports
IDC Names Sweep a Leader in Sustainability Software: get the report
ESG management


## Links


  [Get the report](https://www.sweep.net/reports/2026-idc-marketscape)
  [Get the report](https://www.sweep.net/reports/2026-verdantix-green-quadrant-sweep-turns-esg-data-into-strategic-advantage)
  [Read the report](/the-state-of-business-sustainability-2026)
  [Carbon management](/carbon-management)
  [Supplier Emissions](/supply-chain-emissions)
  [Sustainability Reporting](/sustainability-reporting)
  [Decarbonization Strategy](/decarbonization-strategy)
  [California SB 253](/sb-253)
  [CSRD](/csrd)
  [ISSB](/issb)
  [UK SRS](/landing/uk-srs)
  [CDP](/cdp)
  [Platform](/platform)
  [AI](/platform/ai)
  [Customers](/customers)
  [Reports](/reports)
  [Events](/events)
  [Newsroom](/newsroom)
  [Blog](/blog)
  [Ultimate guide to ESG software in 2026](/guides/2026-decarbonization-strategy-guide-3)
  [SB 253 and SB 261 – Is your company on the list?](/blog/sb-253-and-sb-261-is-your-company-on-the-list)
  [ESG regulations: how to get ready for 2026](/guides/2026-decarbonization-strategy-guide-3)
  [Guides](/guides)
  [Guide to improving your CDP score](/guides/how-to-improve-your-cdp-score)
  [California SB 253: From Data to Disclosure](/guides/california-sb-253-guide)
  [What the first CSRD reporters learned — and how you can apply it](/guides/what-the-first-csrd-reporters-learned-and-how-you-can-apply-it)
  [Tools](/tools)
  [SB 253 Navigator](https://www.sweep.net/tools/sb-253-navigator/)
  [UK Sustainability Laws Compass](https://www.sweep.net/tools/uk-sustainability-laws-compass/)
  [The CSRD Materiality Builder](https://www.sweep.net/tools/csrd-materiality-builder/)
  [CSRD Roadmap tool](/tools/csrd-roadmap-tool)
  [About us](/about)
  [Partners](/partners)
  [Why us?](/why-us)
  [Careers](https://sweep.teamtailor.com/)
  [English](/blog/how-to-import-your-aws-cloud-emissions-into-sweep/)
  [French](/fr/blog/comment-importer-vos-emissions-cloud-aws-dans-sweep/)
  [Login](https://app.sweep.net/auth/sign-in)
  [Book a demo](/demo)
  [Home](/)
  [Blog](/blog)
  [AWS ISV-Accelerate partner fully deployed on AWS](https://www.sweep.net/blog/sweep-is-fully-deployed-on-aws-heres-why-it-matters-2)
  [help.sweep.net](https://help.sweep.net/en/aws-sustainability-console.html)
  [book a demo here](https://www.sweep.net/demo)
  [Why cloud emissions are a critical gap and why now](#why-cloud-emissions-are-a-critical-gap-and-why-now)
  [How the integration works](#how-the-integration-works)
  [Ready to connect?](#ready-to-connect)
  [ReportsVerdantix on Sweep: The new standard for AI in sustainability](/reports/verdantix-on-sweep-the-new-standard-for-ai-in-sustainability/)
  [Reports2026 Verdantix Green Quadrant: Sweep turns ESG data into strategic advantageCarbon accountingESG management](/reports/2026-verdantix-green-quadrant-sweep-turns-esg-data-into-strategic-advantage/)
  [ReportsIDC Names Sweep a Leader in Sustainability Software: get the reportESG management](/reports/sweep-named-a-leader-in-idc-marketscape-2025/)
  [Carbon management](/carbon-management)
  [Supplier Emissions](/supply-chain-emissions)
  [Sustainability Reporting](/sustainability-reporting)
  [Decarbonization Strategy](/decarbonization-strategy)
  [Enterprise](/enterprise)
  [Midmarket](/midmarket)
  [Financial institutions](/financial-institutions)
  [Sweep Starter](https://www2.sweep.net/starter-package)
  [Platform](/platform)
  [AI](https://www.sweep.net/platform/ai)
  [Blog](/blog)
  [Events](/events)
  [Newsroom](/newsroom)
  [for Compliance](/sustainability-works-for-compliance)
  [for Market Advantage](/sustainability-works-for-market-advantage)
  [for Growth](/sustainability-works-for-growth)
  [for Cost Savings](/sustainability-works-for-cost-savings)
  [for Risk Reduction](/sustainability-works-for-risk-reduction)
  [California SB 253](/sb-253 )
  [CSRD](/csrd )
  [ISSB](/issb )
  [UK SRS](/uk-srs)
  [CDP](/cdp)
  [Consumer goods](/industry/consumer-goods)
  [Retail](/industry/retail)
  [Media & Telecoms](/industry/media-telecoms)
  [Energy, utilities, oil & gas](/industry/energy-oil-and-gas)
  [Grocery](/industry/grocery)
  [Manufacturing](/industry/manufacturing)
  [Professional services](/industry/services)
  [Healthcare](/industry/healthcare)
  [About us](/about)
  [Customers](/customers)
  [Partners](/partners)
  [Press](https://sweepnet.notion.site/Sweep-media-kit-2025-170f1c3c643c802c8d98d8a5833dc107)
  [Contact](/contact)
  [Careers](https://sweep.teamtailor.com/)
  [Legal](/company/terms)
  [Linkedin](https://www.linkedin.com/company/sweeptheplanet/about/)
  [YouTube](https://www.youtube.com/@SweepThePlanet)
  [Instagram](https://www.instagram.com/sweeptheplanet/)
  [System](https://status.sweep.net/)
  [Security](https://trust.sweep.net/)
  [Sweep vs Workiva](/workiva-vs-sweep)
  [Sweep vs Watershed](/watershed-vs-sweep)
  [Sweep vs Greenly](/greenly-vs-sweep)
  [Sweep vs Persefoni](/persefoni-vs-sweep)
  [Sweep vs Salesforce Net Zero Cloud](/netzerocloud-vs-sweep)
  [Sweep vs Normative](/normative-vs-sweep)


## Images


  ![Sweep AWS](/_astro/LP_header1_1n1Qj.webp)
  ![Federica Del Fume](/_astro/Screenshot20260529at13.19.14_Z1LmUv7.webp)
  ![Verdantix Report 2025](/_astro/homepage_spotlight1_25gFBi.webp)
  ![Verdantix Green Quadrant 2026](/_astro/sweep_verdantix_mar26header01_F61EB.webp)
  ![Cover IDC 2025](/_astro/LP_1_1BpLzX.webp)
  ![](/_astro/Group_1rOUQL.svg)
  ![](/_astro/Frame_ZrUz7Q.svg)
  ![](/_astro/csr_WHITE1_Z1Jryw.svg)
  ![](/_astro/LFT_2025white_ZXsvVq.webp)