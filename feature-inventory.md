# Resourcify - Complete Feature Inventory

**Source:** Deep crawl of the Resourcify help centers
- English: https://helpcenter.resourcify.com/ (and /en/)
- German: https://www.support.resourcify.com/ (301-redirects to helpcenter.resourcify.com)
- Older `help.resourcify.de` URLs redirect into the same HubSpot KB

Both help centers are a single HubSpot Knowledge Base (multilingual). The platform is a B2B SaaS for industrial / commercial waste & recycling management, with strong DACH-region regulatory focus (German AVV/eANV).

Categories (German label → English label per /en/ site):
1. Administration → Administration
2. Auswertung & Optimierung → Insights
3. Plattform → Platform
4. Zusatzmodule → Additional modules
5. Operations → Operations
6. Technische Hilfe → Technical assistance
7. Accounting & Rechnungswesen → Accounting & Invoicing
8. FAQ → FAQ

---

## 1. Administration

### Article list (full)
Sub-grouped on the index page:

**Abfallarten (Waste types)**
- Was sind Abfallarten — /was-sind-abfallarten
- Wo sehe ich den Materialindex ein — /wo-sehe-ich-den-materialindex-ein

**Anfahrtstellen (Collection / pickup points)**
- Was sind Anfahrtstellen — /was-sind-anfahrtstellen

**Artikel (Articles = container master-data templates)**
- Was ist die Plausibilitätsprüfung — /was-ist-die-plausibilitätspruefung
- Was ist ein Artikel — /was-ist-ein-artikel
- Was ist ein Sammelartikel — /was-ist-ein-sammelartikel
- Wie kopiere ich einen Artikel — /wie-kopiere-ich-einen-artikel

**Benutzer (Users)**
- Wie verwalte ich Benutzer:innen — /wie-verwalte-ich-benutzerinnen
- Wie weise ich Nutzer:innen Standorte zu — /wie-weise-ich-nutzerinnen-standorte-zu
- Benutzer zu Resourcify einladen — /benutzer-zu-resourcify-einladen

**Benutzernachrichten (User messages)**
- Was sind Benutzernachrichten — /was-sind-benutzernachrichten

**Container-Typ**
- Was ist ein Container-Typ — /was-ist-ein-container-typ
- Wo sehe ich den Containerindex ein — /wo-sehe-ich-den-containerindex-ein

**Dienstleister (Service providers)**
- Wer erhält die E-Mail bei Beauftragung eines Containers — /wer-erhaelt-die-e-mail...
- Wie verwalte ich Dienstleister — /wie-verwalte-ich-dienstleister

**Entsorgungswege (Disposal routes)**
- Entsorgungsweg erstellen oder bearbeiten — /entsorgungsweg-erstellen-oder-bearbeiten

**Excel Export**
- Was sind Excel-Exporte — /was-sind-excel-exporte

**Indexpreise (Index prices)**
- Was sind Indexpreise — /was-sind-indexpreise

**Kostenstellen & Profitcenter (Cost / profit centers)**
- Wie verwalte ich Kostenstellen und Profitcenter — /wie-verwalte-ich-kostenstellen-und-profitcenter

**Markierungen (Tags / labels)**
- Was sind Markierungen — /was-sind-markierungen

**Standorte (Locations / sites)**
- Wie kopiere ich einen Standort — /wie-kopiere-ich-einen-standort
- Wie verwalte ich Standorte — /wie-verwalte-ich-standorte

**Vertragskonditionen (Contract conditions)**
- Was sind Vertragskonditionen — /was-sind-vertragskonditionen

**Unternehmen (Company / tenant)**
- Wie hinterlege ich ein neues Unternehmen — /wie-hinterlege-ich-ein-neues-unternehmen
- Wo hinterlege ich die E-Mail für Problemmeldungen — /wo-hinterlege-ich-die-e-mail-fuer-problemmeldungen

### Feature: User & role management
- Two built-in roles: **ADMIN** (whole tenant access) and **USER** (scoped, location-based)
- Multiple-role assignment per user via "+ Weitere Rolle"
- Access scope per role: tenant / company / location / Anfahrtstelle (pickup point)
- Admin sets password directly (min 4 chars) — disabled when SSO is on → SSO is mutually exclusive with local passwords
- Invitation flow ("Benutzer einladen") in addition to direct creation
- No password complexity rules surfaced (4-char minimum is weak — competitive opening)

### Feature: Multi-tenant / company model
- Tenant = "Mandant"; companies, locations and Anfahrtstellen form a 3-level hierarchy
- Cost centers and profit centers are first-class objects linked to companies/locations/Anfahrtstellen; cannot be deleted while referenced (referential integrity enforced)
- "Markierungen" (tags) provide cross-cutting custom classification

### Feature: Master data — Artikel ("article" = container template)
- A container template is an `(Abfallart, Container-Typ, size)` tuple
- Naming convention `A<AVV><type><size>`, e.g. `A150102ABS10` (article / waste-code 150102 / type ABS / 10 m³)
- "Sammelartikel" supports multi-waste containers
- Article has plausibility-check range (min/max kg) for auto-review of returned weights
- Every article must be linked to a contract condition (lead-time / cut-off rules)

### Feature: Plausibility check (waste weight auto-review)
- Per article: configurable from-to weight range
- If `Zurückgemeldet` weight falls in range → status auto-promoted to `Geprüft` and flagged "automatically reviewed"
- Otherwise: problem ticket auto-raised, requires manual review
- *Signal:* simple rule engine, no ML — easy to leapfrog with model-based anomaly detection

### Feature: AVV/waste-type catalogue
- Built-in catalogue of German AVV codes (Abfallverzeichnisverordnung)
- Editable colour per fraction (used across dashboards)
- Hazardous-waste flag derived from AVV (codes with asterisk)
- Material-index lookup ("Materialindex") and Container-index for reference data

### Feature: Index prices
- Manually maintained monthly index values (admin updates)
- Linked into container "Vertragspreise" — referenced, not duplicated
- Cannot be deleted, only archived (audit trail preserved)
- *Signal:* no automated price-feed integration (EUWID, plasticker, EEX, etc.) — automation gap

### Feature: Contract conditions
- Govern lead-time windows for ordering and for service-provider confirmation
- Drive which "Wunschtermin" dates are selectable on a new order
- Referential integrity: cannot delete if still attached to any article

### Feature: Excel export catalogue
- One central "Administration > Excel-Exporte" hub stores all asynchronously-generated exports
- Exports available for every admin object: waste types, articles, users, container types, service providers, disposal routes, index prices, cost/profit centers, tags, locations, contract conditions, companies, Anfahrtstellen, user messages
- Format `.xlsx`; reports (Abfallreport, Kostenreport) download to device instead of being archived
- *Signal:* heavy reliance on Excel as universal export → backend likely uses Apache POI / EPPlus / SheetJS; no CSV/Parquet/Power-BI-direct API surfaced

### Feature: Service-provider directory
- Provider object has child collections: Standorte (provider sites), Kontakte (contacts), Dokumente (certificates/contracts)
- "Wer erhält die Email bei Beauftragung" — per-provider email-routing rule
- Soft-delete only (cannot be removed once orders exist) → strong audit posture
- Documents tab acts as a per-provider DMS

### Feature: User messages / broadcast notifications
- Admin-created in-app banner messages, shown post-login on Home dashboard
- Audience scoping by company / location
- *No* email, SMS, push, scheduling, or template surface mentioned

### Feature: Problem-report routing
- Admin configures the email address to which "Problemmeldungen" are routed
- Each company can have its own escalation address

---

## 2. Auswertung & Optimierung (Insights)

### Article list (full)
- Was ist der Abfallreport — /was-ist-der-abfallreport
- Wie werden geschätzte Abfall- und Materialmengen berechnet — /wie-werden-geschaetzte-abfall-und-materialmengen-berechnet
- Wie werden CO2-Werte berechnet — /wie-werden-co2-werte-berechnet
- Grafische Darstellung der Entsorgungswege — /grafische-darstellung-der-entsorgungswege
- Was ist das Insights Dashboard — /was-ist-das-insights-dashboard
- Wie funktionieren Drill-downs — /wie-funktionieren-drill-downs
- Benchmarking von Standorten — /benchmarking-von-standorten
- Was ist die Materialanalyse — /was-ist-die-materialanalyse
- Was ist die Getrenntsammlungsquote — /was-ist-die-getrenntsammlungsquote
- Was ist der Kostenreport — /was-ist-der-kostenreport
- Was ist die Recyclingquote und wie wird sie berechnet — /was-ist-die-recyclingquote...
- Was ist die Rückmeldequote — /was-ist-die-rueckmeldequote
- Was ist das Standort Dashboard — /was-ist-das-standort-dashboard
- Was ist das Operations Dashboard — /was-ist-das-operations-dashboard

### Feature: Abfallreport (Waste Report)
Three tabs:
1. **Gesamt** — interactive table; columns: location, Anfahrtstelle, material, AVV, material category, disposal provider, quantity, # orders; column-menu customization; sort on any column; Excel download
2. **Jahresübersicht** — multi-year trend per material (tonnes only); chart + downloadable table; filter year / location / material; colour scheme inherited from waste-type admin
3. **Getrenntsammlungsquote** — separated vs mixed commercial waste, % and mass; share of orders included in calc; period + location filter; view-only (no export)

Quantities sourced from automatic provider reports or manual admin entry; mixed billing units (tonnes vs containers) summed separately; weight aggregation handles t/kg unification.

### Feature: Insights Dashboard
- Central hub for recycling, CO₂ and cost KPIs across all locations
- Filter panel: time period, locations, disposal providers, material categories, individual materials
- Interactive charts with click-to-drill
- KPIs: recycling rate, recovery/utilization rate, total emissions, saved emissions
- Disposal-method breakdown: recycling, incineration-with-energy-recovery (R1), incineration, landfill
- Volumes: total waste with drill-down by material/location/provider
- Costs: total, average vs period avg, cost per tonne (by disposal method)
- Location ranking by recycling rate / CO₂ efficiency / cost

### Feature: CO₂ calculation engine
- Formula: `Σ (mass of waste component × emission factor of disposal method)`
- Material × method matrix; methods = landfill, incineration, recycling, composting
- Emission factor sources: ADEME (FR), Genesis (DE), UK gov data, Ecoinvent (commercial), expert research
- Standards alignment: **GHG Protocol Scope 3 Category 5** ("Waste Generated in Operations")
- Avoided-emissions for recycling acknowledged but excluded to prevent double-counting
- Methodology described as "Näherungswerte" pending certification
- *Signal:* no ISO 14064 / 14067 stamp yet; not yet 3rd-party verified — competitor differentiator

### Feature: Estimated weight calculation
- Method 1 — historical avg from same container type+size
- Method 2 — material density × container volume × 70% assumed fill level
- Report filterable by weight-determination method: reported / historic-est / density-est / converted / missing
- *Signal:* explicit data-lineage field per row — strong audit pattern

### Feature: Material analysis
- Boxplot of cost (€) and CO₂ (t) per material, both absolute and per-tonne
- Filter: time, region, location, material
- Highlights variance, outliers, optimization candidates
- Excel export

### Feature: Location benchmarking
- Multi-site side-by-side
- Regional aggregation
- Top/bottom performer surfacing
- Metrics: cost efficiency, recycling rate, CO₂, disposal cost

### Feature: KPI library (named/standardised)
- **Recyclingquote** (recycling quota)
- **Getrenntsammlungsquote** (separate-collection quota) — explicit AVV inclusion/exclusion list (≈60 codes in numerator + 5 mixed/residual in denominator), excludes hazardous (asterisked AVV) and unverified orders
- **Rückmeldequote** (report-back rate)
- **Pünktliche Abholquote** (on-time pickup rate)
- **Problemquote** (problem rate)
- **Auftragsausführungsquote** (order execution rate, ex-cancellations)

### Feature: Operations dashboard (real-time)
- Trend chart of completed/requested pickups + punctuality (last weeks)
- Monthly status breakdown (processing/cancelled/reviewed/problem)
- Filters: period, location, provider, material

### Feature: Standort dashboard
- Per-location overview for location users
- Cost & revenue per fraction, quantities per fraction
- Period-over-period comparison (% or absolute)
- Excludes orders not yet verified ("zurückgemeldet & geprüft" only)

### Feature: Disposal-route visualisation
- Annual waste-stream overview (waste origin → disposal route)
- Total + per-stream tonnes; click to drill into orders per stream
- Visualisation itself non-exportable; underlying orders Excel-exportable
- *Signal:* sounds like a custom proportional/flow chart, not a full Sankey

### Feature: Kostenreport (Cost report)
- Companion to Abfallreport on cost dimensions; interactive table with sort/column-customize/Excel export

---

## 3. Plattform (Platform)

### Article list (full)
**Containerverwaltung:**
- Wie verlängere ich die Container-Gültigkeit — /wie-verlängere-ich-die-container-gültigkeit
- Wie manage ich einen Entsorgerwechsel — /wie-manage-ich-einen-entsorgerwechsel-in-der-containerverwaltung
- Wie hinterlege ich zusätzliche Auftragsinformationen — /wie-hinterlege-ich-zusätzliche-auftragsinformationen
- Wie füge ich einen neuen Container hinzu — /wie-füge-ich-einen-neuen-container-hinzu
- Was ist die Containerverwaltung — /was-ist-die-containerverwaltung
- Wie hinterlege ich Informationen zu Entsorgungswegen — /wie-hinterlege-ich-informationen-zu-entsorgungswegen
- Wie verwalte ich die Preise für einen Container — /wie-verwalte-ich-die-preise-für-einen-container
- Wie verwalte ich einzelne Container — /wie-verwalte-ich-einzelne-container
- Wie verwalte ich mehrere Container auf einmal — /wie-verwalte-ich-mehrere-container-auf-einmal

**Dienstleister:**
- Was sind Dienstleister — /was-sind-dienstleister
- Wie hinterlege ich abweichende Dienstleister für einen Container — /wie-hinterlege-ich-abweichende-dienstleister-für-einen-container-right

### Feature: Container registry (Containerverwaltung)
- Admin-only module (not visible to USER role)
- Per-container fields: validity dates, contract prices, disposal-route info, additional order info, hazardous-waste flag, external contract number, alternative disposal provider
- Excel export of containers
- Filter chips at top + extensible "+Filter" with at least: gefährlicher Abfall, externe Vertragsnummer, abweichender Entsorger
- Container has lifecycle: create → extend validity → swap provider → retire

### Feature: Bulk container management
- Export → edit → import round-trip for mass changes
- Bulk fields documented: contract prices + general container details
- Bulk-create supported (large-batch onboarding)
- *Signal:* explicit Excel-driven bulk pattern (likely no spreadsheet-grid UI)

### Feature: Pricing engine
- Per-container contract prices link to global Index prices
- Mietpreise (rental fees) auto-generated under defined conditions (see Technische Hilfe)
- Tagespreis (spot/day price) for one-off ad-hoc orders
- Pauschalpreis (flat price) for fixed-cost orders
- Multi-currency status not surfaced; appears EUR-only

### Feature: Provider switch ("Entsorgerwechsel")
- Dedicated workflow when changing the provider on an existing container — preserves history while migrating future orders

### Feature: Alternative provider per container
- Per-container override of the default provider; enables backup/secondary routing

---

## 4. Zusatzmodule (Add-on modules)

### Article list (full)
**eANV:**
- Wie lade ich eine Deklarationsanalyse hoch — /wie-lade-ich-eine-deklarationsanalyse-hoch
- Wie funktioniert das Modul zur Elektronischen Nachweisführung (eANV) — /wie-funktioniert-das-modul...
- Wie kann ich einen Begleitschein signieren — /wie-kann-ich-einen-begleitschein-signieren
- Was zeigt mir die eANV-Übersicht — /was-zeigt-mir-die-eanv-übersicht
- Wie sehe ich das Abfallregister ein — /wie-sehe-ich-das-abfallregister-ein
- Was sind gefährliche Abfälle — /was-sind-gefährliche-abfälle
- Wie verwalte ich Begleitscheine — /wie-verwalte-ich-begleitscheine
- Wie verwalte ich Entsorgungsnachweise — /wie-verwalte-ich-entsorgungsnachweise
- Wie kann ich eine Deklarationsanalyse beauftragen — /wie-kann-ich-eine-deklarationsanalyse-beauftragen

**SSO:**
- Was ist Single Sign-On (SSO) — /was-ist-single-sign-on-sso

**QR-Code:**
- Wie generiere ich QR-Codes für Container — /wie-generiere-ich-qr-codes-für-container

### Feature: eANV module (electronic waste manifest for DE)
- Implemented as **partner integration with NSUITE** (Resourcify does *not* connect to ZKS-Abfall directly)
- NSUITE handles OSCI communication to ZKS, implements BMU/BMUB interfaces
- Bidirectional sync, refresh **every minute**
- Document types: Begleitschein, Entsorgungsnachweis, Übernahmeschein
- Functions: user/tenant/register admin, qualified e-signature with viewer, automatic document distribution to all transport parties, semantic + syntactic validation on receipt, mailbox-based document assignment
- Automated **Abfallregister** maintenance (reportable + non-reportable waste), customizable filters/views, register-excerpt generation, selective distribution
- Disposal-certificate usage monitor with configurable thresholds (% used or time-remaining) — warning at 70 %
- Hazardous-goods transport docs (PDF / image) attachable to orders
- Declaration analysis (Deklarationsanalyse): upload and order workflow
- *Signal:* the cert-utilization gauge is a unique compliance feature; OSCI/ZKS is outsourced — Resourcify is a UX wrapper here

### Feature: e-Signature for Begleitscheine
- Native Windows-side app **"NSUITE-Signatur"** (download on first use)
- Requires hardware **signature card + card reader** (eIDAS-style)
- Card-based, not cloud-based — suggests Qualified Electronic Signature (QES), eIDAS-aligned but not explicitly labelled
- *Signal:* no remote/cloud signing, no mobile signing — friction point

### Feature: SSO (add-on)
- Activation-only via Customer Success (not self-serve)
- No public detail on protocol (SAML vs OIDC), IdPs, SCIM, JIT
- Mutually exclusive with local password (per User mgmt article)

### Feature: QR-codes for containers
- Generate PDF sheet of QR codes from Containerverwaltung selection
- Limit: 10 codes per generation batch
- Workflow: print → affix to physical container → mobile scan to open order flow
- *Signal:* camera + barcode/QR library on mobile (likely ZXing or platform-native AVFoundation / ML Kit)
- Add-on, gated by CSM

---

## 5. Operations

### Article list (full)
**Auftragsabwicklung (Order processing):**
- Was ist EasyDrop AI — /was-ist-easydrop-ai
- Was ist die "Eingehende E-Mails"-Übersicht — /was-ist-die-eingehende-e-mails-übersicht
- Wie berechne ich einen Pauschalpreis — /wie-berechne-ich-einen-pauschalpreis
- Wie bereite ich Aufträge für die Rechnungsprüfung vor — /wie-bereite-ich-auftraege-fuer-die-rechnungspruefung-vor
- Wie kann ich den Auftragsstatus manuell ändern — /wie-kann-ich-den-auftragsstatus-manuell-aendern
- Wie storniere ich einen Auftrag — /wie-storniere-ich-einen-auftrag
- Wie führe ich eine Umdeklarierung durch — /wie-fuehre-ich-eine-umdeklarierung-durch

**Auftragserteilung (Order placement):**
- Was ist ein Tagespreis — /was-ist-ein-tagespreis
- Intervallplan selbst- oder fremdverwaltet — /intervallplan-selbstverwaltet-oder-fremdverwaltet
- Was ist die Standortübersicht — /was-ist-die-standortuebersicht
- Wie bearbeite ich den Intervallplan eines Containers — /wie-bearbeite-ich-den-intervallplan-eines-containers
- Wie beauftrage ich einen Container in der Standortübersicht — /wie-beauftrage-ich-einen-container
- Wie beauftrage ich Mehrmengen bei Intervall-Aufträgen — /wie-beauftrage-ich-mehrmengen-bei-intervall-auftraegen
- Wie erfasse ich einen Auftrag für einen Container nach — /wie-erfasse-ich-einen-auftrag-fuer-einen-container-nach
- Wie erzeuge ich Mietpreise — /wie-erzeuge-ich-mietpreise
- Wie beauftrage ich den Abzug eines Containers — /wie-beauftrage-ich-den-abzug-eines-containers
- Wie beauftrage ich einen Container über die Containerverwaltung — /wie-beauftrage-ich-einen-container-ueber-die-containerverwaltung

**Auftragsverwaltung (Order admin):**
- Was kann die Auftragsverwaltung — /was-kann-die-auftragsverwaltung
- Wie sehe ich Reklamationen von Entsorgern ein — /wie-sehe-ich-reklamationen-von-entsorgern-ein
- Wie verwalte ich Problemmeldungen zu einem Auftrag — /wie-verwalte-ich-problemmeldungen-zu-einem-auftrag
- Wie verwalte ich die Auftragsdetails — /wie-verwalte-ich-die-auftragsdetails

**Rechnungs- und Gutschriftsabwicklung (Invoicing):**
- Wie leite ich die geprüften Rechnungen an meine Finanzbuchhaltung weiter — /wie-leite-ich-die-gepruften-rechnungen...

### Feature: Order types (4)
- **Gestellung** — place new container
- **Leerung** — empty in place
- **Tausch** — swap full ↔ empty
- **Abholung / Abzug** — pick up & remove (Abzug = explicit removal that updates placement status)

### Feature: Order state machine (9 states)
`Beauftragt → Bestätigt → Ausgeführt → Zurückgemeldet → Geprüft → Bereit zur Abrechnung → In Abrechnung → Abgerechnet`; orphan branch: `Storniert` (only valid from `Beauftragt`). Status changes locked after `Abgerechnet`.

### Feature: Standortübersicht (Site overview — primary operator UI)
- Two operating modes per container:
  - **Auf Abruf** — manual create via green "+" when full
  - **Intervall** — auto-create per schedule, fires **6 days before** next planned pickup
- Mehrmengen handling on top of interval orders
- Nachträgliche Erfassung — back-date / reconstruct missed orders
- Mietpreis (rental) generation conditional on usage rules

### Feature: Interval plan modes
- **Selbstverwaltet** — order email goes to provider, provider feedback expected, customer steers
- **Fremdverwaltet** — *no* email to provider; provider runs its own tours; no per-order feedback (assumes standard weights / bulk pickup)

### Feature: Order placement channels (provider notification)
- Auto-generated **email** to the provider (default channel) — covers appointment confirmation, execution confirmation, and quantity/weight return
- **ERP integration** option — direct Resourcify ↔ provider ERP interface (alt to email)
- *Signal:* dual-channel architecture; specific protocol (EDI? REST? Soap?) not disclosed — likely a custom REST integration with major DE entsorger ERPs

### Feature: Incoming-emails inbox
- Stores every email received by the platform (execution confirmations, invoices, provider responses)
- Searchable + filterable
- Per-email attachment column with quick-view
- "Verlinkter Auftrag" column = order-number link to jump to the order
- *Signal:* an actual inbound mail-domain / mailbox per tenant or per location; the address is shown in-app (per Accounting article)

### Feature: EasyDrop AI (document → data extraction)
- Drag-and-drop or upload PDF of delivery note / weighing slip
- One PDF per order; multiple pages allowed
- AI extracts weight + quantity → auto-populates "Mengen & Gewichte"
- Auto-status → `Geprüft`
- Auto-match orders or manual search if ambiguous
- PDF archived under order Dokumente tab
- Feedback collection in-app (training-loop hint)
- Activated by support, lives between Administration and language menu
- *Signal:* IDP/OCR + LLM pipeline (likely Document AI / Azure Document Intelligence / custom layout-aware extraction); no email-ingest mode mentioned

### Feature: Order admin (Auftragsverwaltung)
- Provider-side complaint review ("Reklamationen von Entsorgern")
- Per-order problem ticket management
- Manual status overrides
- Cancellations
- Umdeklarierung — reclassify the waste type post-pickup (a common operational reality)

### Feature: Invoice preparation (Rechnungsprüfung readiness)
- "Schattenpositionen" (shadow positions): system-generated billing positions derived from returned weights and contract prices
- Shadow positions are what later get matched against the supplier invoice
- Manual verification of reported quantities/weights gated before invoice check

### Feature: Pricing flavors at order level
- Tagespreis (day price)
- Pauschalpreis (flat / lump-sum) with built-in calculation helper
- Mietpreis (rental price) auto-generated under specific conditions
- Index-linked contract prices

### Feature: Internal communication / file attachments
- "Zusätzliche Auftragsinformationen" per order
- Documents tab per order
- Comments on problem reports

---

## 6. Technische Hilfe (Technical assistance)

### Article list (full)
- Link zur Resourcify Software lässt sich nicht öffnen — /link-zur-resourcify-software-lässt-sich-nicht-öffnen
- Wie benutze ich den Chat Bot — /wie-benutze-ich-den-chat-bot
- Was ist das Resourcify Support Center — /was-ist-das-resourcify-support-center
- Löschung von Cache und Cookies — /löschung-von-cache-und-cookies
- Unter welchen Bedingungen werden Mietpreisaufträge erzeugt — /unter-welchen-bedingungen-werden-mietpreise-erzeugt
- Welche Filter kann ich in der Containerverwaltung benutzen — /welche-filter-kann-ich-in-der-containerverwaltung-benutzen
- Wie erstelle ich eine Support-Anfrage zu einem Auftrag — /wie-erstelle-ich-eine-support-anfrage-zu-einem-auftrag
- Wie erstelle ich eine Support-Anfrage zu einem Container — /wie-erstelle-ich-eine-support-anfrage-zu-einem-container
- Wie kann ich einen Standort löschen — /wie-kann-ich-einen-standort-löschen
- Wie kopiere ich einen Container — /wie-kopiere-ich-einen-container
- Wie nutze ich die interaktiven Tabellen zum Abfallreport und Kostenreport richtig — /wie-nutze-ich-die-interaktiven-tabellen...

### Feature: In-app chatbot
- Embedded chat-bot for first-line support (HubSpot Service Hub likely — confirms HubSpot stack)

### Feature: Support center / context-aware tickets
- Per-order and per-container "Open ticket from this object" deep-link to support center → tickets carry object IDs automatically

### Feature: Interactive table component
- Re-used across Abfallreport, Kostenreport, Containerverwaltung
- Column customisation, sorting, multi-filter
- *Signal:* a shared table widget (probably AG-Grid / TanStack Table)

### Feature: Browser support guidance
- Cache/cookies article + login link troubleshooting — confirms web-only SPA, no install footprint

---

## 7. Accounting & Rechnungswesen

### Article list (full)
- Was ist die Rechnungsübersicht — /was-ist-die-rechnungsübersicht
- Wie verwalte ich Rechnungen und Gutschriften — /wie-verwalte-ich-rechnungen-und-gutschriften
- Wie prüfe ich Rechnungen und Gutschriften — /wie-prufe-ich-rechnungen-und-gutschriften (Einzelposten line-item check)
- Schritt-für-Schritt-Anleitung zur Rechnungsprüfung mit PDF und Excel-Datei — /schritt-fur-schritt-anleitung-zur-rechnungsprufung-mit-pdf-und-excel-datei
- Automatisierter Abgleichprozess von Rechnungsdaten in der Resourcify Plattform — /automatisierter-abgleichprozess-von-rechnungsdaten-in-der-resourcify-plattform

### Feature: Invoice & credit-note overview
- Two tabs: Incoming Invoices, main Rechnungsübersicht
- Upload paths:
  1. Web upload (PDF) per location
  2. **Mailbox upload** to the address shown in-app (provider can send directly)
- Archive flow (Archived state)
- ZIP-batch download for forwarding to FiBu (manual handoff — no DATEV/SAP connector documented)
- Individual PDF download

### Feature: Invoice review — two modes
1. **Einzelposten** (line-item, manual matching)
2. **Sammelrechnung** (collective invoice) with **PDF + Excel** dual-document workflow

### Feature: Automated invoice-matching algorithm (5 stages)
1. Location matching via assigned cost center; material via AVV + **RMID**
2. Container validation by location + material + service date; optional **RCID**
3. Order match: PO number primary; container as secondary key
4. Line-item assignment by service type, provider, billing unit + all relevant numeric fields
5. Multi-match resolution: scoring algorithm picks "höchste Übereinstimmungsrate"
- No documented tolerance thresholds (qualitative)
- No documented OCR step — works off provider-supplied Excel that mirrors the PDF
- *Signal:* RMID / RCID are internal stable IDs (Resourcify Material ID / Resourcify Container ID) → enables clean B2B data contract with Entsorger ERPs

### Feature: No native ERP / accounting connectors
- Hand-off to FiBu = ZIP-of-PDFs
- *Big competitive gap:* DATEV-Export-DTVF, SAP iDoc/RE-FX, Microsoft Dynamics, Lexware, ELO, etc. are absent

---

## 8. FAQ

### Article list (full)
- Was bedeuten die verschiedenen Auftragstypen — /was-bedeuten-die-verschiedenen-auftragstypen
- Wie kann ich mein Passwort ändern — /wie-kann-ich-mein-passwort-ändern
- Welchen Standort kann ich einsehen — /welchen-standort-kann-ich-einsehen
- Welches Problem kann ich melden — /welches-problem-kann-ich-melden
- Wie hinterlege ich ein Standardgewicht in der Software — /wie-hinterlege-ich-ein-standardgewicht
- Wo kann ich mich in die Software einloggen — /wo-kann-ich-mich-in-die-software-einloggen
- Was ist das Elektronische Abfallnachweisverfahren (eANV) — /was-ist-das-elektronische-abfallnachweisverfahren-eanv
- Was bedeutet der jeweilige Auftragsstatus — /was-bedeutet-der-jeweilige-auftragsstatus

### Feature: Standard weights
- Per-container or per-article default weight, used when no real weighing is available
- Drives auto-generation of estimates and unlocks Fremdverwaltet workflows

### Feature: Login URL
- Confirmed single web app (https URL surfaced in FAQ); no native app surfaced
- Old `help.resourcify.de/knowledge-base/einloggen/` redirects to the FAQ login page → DNS-level migration of legacy help URLs intact

### Feature: Problem reporting catalogue
- Whitelisted problem types per object (container, order, location); each has its own routing email

### Feature: Per-user location visibility
- Determines which sites a USER sees based on role assignments + scope dropdown

---

## Cross-cutting technology signals (consolidated)

| Signal | Likely implication |
|---|---|
| All exports are Excel `.xlsx`; report exports download client-side, admin object exports archived server-side | Apache POI / EPPlus / SheetJS; async export pipeline (queue + storage) |
| Drill-down KPIs across Insights | OLAP-style aggregation; likely Postgres + materialized views or a column-store (ClickHouse/BigQuery/Snowflake) |
| Real-time Operations dashboard | Read-replica or event-stream into dashboard service |
| QR-code PDF batches of ≤10 | Server-side PDF generation (likely Puppeteer / wkhtmltopdf / PDFKit); QR via standard library |
| Camera-based QR scan, no native app surfaced | Web-based scanning (BarcodeDetector API / ZXing-JS) inside PWA or wrapper |
| EasyDrop AI extracts weight/qty from PDF, returns extracted fields with order auto-match | Document AI (Google / Azure / AWS Textract) + LLM post-processing; feedback loop hints at supervised retraining |
| Automated invoice matching (RMID/RCID, multi-stage scoring) | Custom rules engine + score-based matcher; no ML stated |
| eANV done via NSUITE | Outsourced OSCI/ZKS connectivity — Resourcify is the UX skin |
| Card-reader e-signature (NSUITE-Signatur exe) | eIDAS QES via local hardware; no cloud-signing |
| HubSpot KB + in-app chatbot | HubSpot Service Hub backbone for support; CRM/marketing alignment |
| ERP integration with selected disposal providers | Custom point-to-point integrations (no public Resourcify API surfaced in KB) |
| ZIP-of-PDFs to handoff to FiBu | No native accounting connectors |
| User mgmt: min 4-char password, no MFA mentioned | Weak auth posture unless SSO is on |
| In-app messages only via dashboard banner | No notification center / email/push templating engine |

