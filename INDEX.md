# Resourcify Knowledge Base — Indeks

Komplet teknisk og forretningsmæssig viden om Resourcify, struktureret per emne. Brug denne mappe som opslagsværk når der bygges, planlægges, eller pitches.

**Sidst opdateret:** 28. maj 2026
**Kilder:** Bundle-dekompilering (3.6 MB JS), help-center crawl, marketing-crawl, CT-logs, jobopslag, presseresearch

---

## 📁 Struktur

```
knowledge-base/
├── 01-tech-stack/
│   ├── frontend.md              React 19 + Vite + libraries
│   ├── backend.md               Java/Spring Boot signaturer
│   ├── auth-identity.md         Auth0 EU + SSO providers
│   ├── observability.md         Rollbar, Hotjar, Segment, Userpilot, etc.
│   ├── infrastructure.md        GCP, Cloudflare, CDN-strategi
│   └── third-party-services.md  Komplet liste af eksterne services
│
├── 02-architecture/
│   ├── multi-tenancy.md         Shared SaaS + Dedicated white-label
│   ├── domain-topology.md       Komplet DNS-kort fra CT-logs
│   └── deployment-environments.md Production/staging/dev/preview/PR
│
├── 03-api/
│   ├── graphql-operations.md    Alle 60+ GraphQL operations
│   ├── graphql-entities.md      19 entity fragments + felter
│   ├── rest-endpoints.md        REST APIs (config, m2m)
│   └── m2m-clients.md           Machine-to-machine integration
│
├── 04-features/
│   ├── master-data.md           Container, location, waste-type management
│   ├── operations-flow.md       Service orders, scheduling, providers
│   ├── insights-ai.md           12 AI-optimerings-anbefalinger
│   ├── compliance-csrd-eanv.md  CSRD, EANV, EPR, MDR
│   ├── reporting-kpis.md        Dashboards + KPI-bibliotek
│   ├── co2-engine.md            GHG Scope 3 Cat. 5 implementation
│   └── easydrop-ocr.md          PDF → struktureret data pipeline
│
├── 05-data-model/
│   ├── entity-fragments.md      19 GraphQL fragments
│   ├── enums.md                 Container-typer, materials, disposal paths
│   └── state-machines.md        9-state order machine
│
├── 06-business/
│   ├── funding-history.md       €23M raised, runder, investorer
│   ├── customers.md             80+ kunder (CT logs + presse)
│   ├── pricing-gtm.md           Pricing model, sales motion, ACV
│   └── competitors.md           11 konkurrenter med profiler
│
└── 07-wedges/
    └── exploitable-weaknesses.md Konkrete svagheder vi kan angribe
```

---

## 🎯 Quick References

### Sammenfattet Tech-Stack

| Lag | Resourcify | Vores anbefaling |
|-----|------------|------------------|
| Frontend framework | React 19.2.4 + Vite | Samme |
| GraphQL klient | urql eller graphql-request (codegen) | TanStack Query + graphql-codegen |
| State | Redux Toolkit + Immer | TanStack Query + Zustand |
| Forms/validation | Zod (260) + Yup (16 legacy) | Zod + React Hook Form |
| UI components | Radix + shadcn + cmdk + vaul + sonner | Samme |
| Charts | Recharts + D3 | Samme |
| Rich text | Slate | Tiptap (modernere) |
| PDF | jsPDF | Samme |
| Excel | xlsx (SheetJS) | Samme |
| i18n | i18next | Samme |
| Backend | Java + Spring Boot + Spring GraphQL | TypeScript + Hono + GraphQL Yoga (anbefales for hastighed) |
| Database | PostgreSQL (multi-tenant) | Samme + RLS for shared, schema-per-tenant for enterprise |
| Auth | Auth0 EU + Google/Microsoft/OIDC SSO | Samme + MFA + WebAuthn baseline |
| Cloud | GCP europe-west | Samme (Frankfurt for GDPR) |
| Observability | Rollbar + Hotjar + Segment → Amplitude + Userpilot + Crisp + Grafana + Looker + SonarQube | Sentry + PostHog + Grafana + Userpilot + Crisp (færre værktøjer, samme dækning) |
| CDN/Asset | Cloudinary | Samme |
| OCR / IDP | Eget system "EasyDrop" | Google Document AI + Claude Vision fallback |
| Compliance | NSUITE for EANV | Samme + Cloud QES via D-TRUST |

### Topscore Findings

1. **Hele GraphQL-API'et er kortlagt** — 60+ operations, 19 entities — se `03-api/graphql-operations.md`
2. **12 AI-optimerings-features** — komplet liste med beskrivelser — se `04-features/insights-ai.md`
3. **80+ enterprise-kunder** identificeret via CT-logs — se `06-business/customers.md`
4. **Komplet funding-historik** — €23M total, korrigeret fra €15M påstand — se `06-business/funding-history.md`
5. **10 konkrete svagheder** at angribe — se `07-wedges/exploitable-weaknesses.md`

---

## 🗂️ Hvordan bruges denne KB

| Du vil... | Læs... |
|-----------|--------|
| Vælge teknologi til et lag | `01-tech-stack/<lag>.md` |
| Forstå deres data-model | `05-data-model/entity-fragments.md` |
| Liste hvilke features vi skal bygge | `04-features/` (alle) |
| Pitche til en investor | `06-business/` + `07-wedges/` |
| Bygge en konkret integration | `03-api/graphql-operations.md` |
| Beslutte vores GTM-strategi | `06-business/pricing-gtm.md` + `06-business/competitors.md` |
| Hyre engineering-team | `01-tech-stack/` (alle) |

---

## 🔗 Relaterede dokumenter (i parent-mappen)

- `../REPORT.md` — Original arkitektur-rapport (v1)
- `../ULTIMATE-REPORT.md` — Master-rapport (v2, 41 KB)
- `../marketing-crawl.md` — 28 sider marketing crawl
- `../feature-inventory.md` — Komplet feature-katalog
- `../business-intel.md` — Business intelligence + konkurrenter
- `../drejebog/Resourcify-Drejebog.md` — Pitch-ready drejebog (md + docx + pdf)
- `../raw/` — Råfiler (JS bundle, i18n JSON, network logs)
- `../screenshots/` — UI screenshots
