# FDR AuditWala (FDRGuard) 🛡️
### Intelligent Security Deposit & FDR Lifecycle Management Platform
*Smart India Hackathon 2026 — Problem Statement: "Streamline of security deposit / FDR portal" (AICTE Context — PS ID: SIH26265)*

> **One-line identity:**
> *"This is not an FDR database. It is an AI-powered FDR lifecycle intelligence and decision-support platform."*

**Live Production Deployment:** [https://web-beta-snowy-47.vercel.app](https://web-beta-snowy-47.vercel.app)  
**GitHub Repository:** [https://github.com/Starmann1/FDR-AuditWala](https://github.com/Starmann1/FDR-AuditWala)  
**Full System Specification:** [docs/ARCHITECTURE_SPECIFICATION.md](docs/ARCHITECTURE_SPECIFICATION.md)

---

## 🏛️ Core Principles & Separation of Duties

| Component | Strict Role | Guardrail / Invariant |
|---|---|---|
| **AI** | Suggests, detects anomalies, explains | Never invents rules, never silently modifies records, never initiates transfers |
| **Rules Engine** | Decides deterministic compliance | Hard regulatory checks evaluated strictly without probabilistic hallucination |
| **Verification** | Checks authoritative bank gateways | Fail-safe: `SOURCE_UNAVAILABLE` is a connectivity state, never flagged as fraud |
| **Case Officer** | Conducts inspection & recommends | Can submit recommendations; direct approval/rejection is blocked (403 Forbidden) |
| **Approving Authority** | Makes consequential decisions | Holds sole statutory power to issue final approval or rejection with mandatory justification |
| **Audit Ledger** | Records immutable history | Append-only, SHA-256 hash-chained cryptographic ledger capturing all actions |
| **Improvement Loop** | Learns only from validated feedback | Zero uncontrolled self-learning; changes require versioned rule deployment |

**Core Loop:** `DOCUMENT → VERIFY → UNDERSTAND → SCORE → PRIORITIZE → REVIEW → ACT → AUDIT → IMPROVE`

---

## 👥 Seeded Demo Personas & Credentials

All demo accounts use password: **`Demo@12345`**

| Role Clearance | Persona / Official | Email | Core Responsibilities |
|---|---|---|---|
| **CASE_OFFICER** | Rajesh Sharma | `rajesh.sharma@demo.fdrguard.test` | Queue triage, Digital Twin comparison, inspection recommendations |
| **APPROVING_AUTHORITY** | Prof. K. Rajagopal | `approving.authority@demo.fdrguard.test` | Member Secretary, final statutory deposit adjudication |
| **APPLICANT** | Dr. Arvind Patel | `registrar.inst2@demo.fdrguard.test` | Registrar (Sardar Patel Academy), tenant-isolated intake & deposit tracking |
| **FINANCE_OFFICER** | Shri M. K. Verma | `finance.officer@demo.fdrguard.test` | Custody accounting, bank reconciliation, maturity calendar |
| **AUDITOR** | Smt. Meenakshi Sundaram | `auditor@demo.fdrguard.test` | Vigilance cell, read-only audit chain integrity verification |
| **SYSTEM_ADMIN** | Smt. Priya Sundaram | `admin@demo.fdrguard.test` | Portal infrastructure, demo account management, lockout reset |
| **POLICY_ADMIN** | Dr. H. C. Nagaraj | `policy.admin@demo.fdrguard.test` | Approval Process Handbook (APH) Council, publishes regulatory rule packs |
| **MANAGEMENT** | Dr. Anil Sahasrabudhe | `management@demo.fdrguard.test` | Executive Council portfolio analytics, risk distribution, macro exposure |

---

## 🚀 Quick Start & Verification

### 1. Run Web Application
```bash
cd apps/web
npm install --legacy-peer-deps
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

### 2. Run Automated Verification Suite (21 Unit Tests)
```bash
python scripts/run_unit_tests.py
```
Validates:
* Tenant boundary isolation (cross-institution leakage blocked).
* Separation of duties (Case Officer blocked from issuing final approvals).
* System Admin blocked from altering regulatory decisions.
* Optimistic concurrency (stale `record_version` returns HTTP 409).
* Fail-safe source semantics (`SOURCE_UNAVAILABLE` is not treated as fraud).
* Digital Twin claims vs facts invariant (unresolved conflicts preserved side-by-side).
* AICTE regulatory rules (tenure >= 60 months, lien endorsement, amount slabs).

---

## 🧪 5 Scripted Benchmark Scenarios

1. **Clean Normal FDR** (`FDR-SBI-2024-81729`) → ₹35 Lakhs, State Bank of India. 100% Core Banking Match → **LOW RISK / VERIFIED**.
2. **Amount Mismatch** (`FDR-PNB-2024-9981`) → ₹50 Lakhs claimed in PDF vs ₹45 Lakhs recorded in PNB CBS (₹5 Lakh deficit) → **CRITICAL RISK / HUMAN REVIEW**.
3. **Approaching Maturity** (`FDR-BOB-2019-44120`) → Bank of Baroda deposit maturing within 18 days → **RENEWAL REQUIRED**.
4. **Suspicious Scan** (`FDR-HDFC-2024-55190`) → Photoshop metadata tags, resolution mismatch on seal stamp → **REVIEW RECOMMENDED / HIGH CONCERN**.
5. **Release / Refund Authorization** (`FDR-CAN-2016-10291`) → 8-year mandatory security deposit lock-in completed with continuous A++ accreditation → **RELEASE ELIGIBLE**.

---

## 🌐 Production REST API v1 Suite

All API v1 routes require authenticated session token via cookie or `Authorization: Bearer <token>`:

* `GET /api/v1/cases` — List cases with scope/tenant filtering.
* `GET /api/v1/cases/:id/explainability` — Returns versioned trace (pipeline, model confidence, extraction claims, verification status, rule evaluations, and findings).
* `POST /api/v1/cases/:id/review` — Submits recommendations or statutory decisions with mandatory justification, optimistic locking, and audit ledger persistence.
* `GET /api/v1/fdrs` — Portfolio list with lifecycle status and tenant filtering.
* `GET /api/v1/maturity/alerts?window=45` — Automated 45-day pre-expiry renewal sentinel.

---

## 📁 Repository Structure

```text
fdr-auditwala/
├── apps/
│   ├── web/                     # Next.js 14 App Router, Tailwind CSS, Lucide UI
│   │   ├── app/                 # Routes: /reviewer, /institution, /admin, /management, /api/v1
│   │   ├── components/          # Reusable UI widgets: StatusBadge, RiskScoreGauge, Navbar
│   │   └── lib/                 # FSM, rulesEngine, riskEngine, mockBank, auditLedger, store
│   └── api/                     # FastAPI backend reference service
├── rules/                       # Versioned regulatory rule packs (YAML)
├── tests/                       # Unit, integration, and guidebook compliance suites
├── scripts/                     # run_unit_tests.py, test runners
├── vercel.json                  # Next.js Vercel production deployment spec
└── README.md                    # System documentation
```
