---
name: lead-quality-report
description: Build a Meta Ads Lead Quality Report and interactive rolling dashboard for any lead gen client. Maps ad creative spend to off-platform sales outcomes (calls booked, closes, DQs, no-shows, pipeline) with qualitative lead scoring. Use this skill whenever asked to build a lead quality report, ad-to-sales attribution report, lead-level ROAS analysis, rolling ads dashboard, or when the user wants to see which ads are producing dream clients vs waste. Also triggers on requests like "which ads are bringing in good leads", "show me lead quality by creative", "build the weekly report", "run the lead quality dashboard", "update the dashboard", or any request involving mapping Meta ad data to CRM/sales outcomes.
---

# Meta Ads Lead Quality Report

Maps every dollar of Meta ad spend to real sales outcomes — at the individual lead level — with qualitative scoring derived from closer notes and call summaries. Produces a rolling interactive HTML dashboard with 3/7/14/30 day views.

This skill solves the core media buying problem: Meta doesn't know whether leads were quality, showed up, converted, or what the real ROAS was. This skill bridges that gap by combining Meta spend data with off-platform sales data from Cortana/Hyros and CRM/closer logs.

**What it produces:**
- Interactive HTML dashboard (opens in browser, no server needed)
- Rolling weekly updates that accumulate data over time
- Ad-creative-level ROAS with lead quality scores
- Lead-level detail with SQIBNT qualitative scoring
- Automated pattern detection and recommended actions
- Optional client-facing Google Doc summary

**Reference implementations:**
- the Lead Quality Report (29 Mar – 6 Apr 2026) — lead-level qualitative depth
- Example Client Performance Report (rolling) — aesthetic, analytical structure, ad-level deep dives

---

## Step 0 — Client Setup & Data Collection

Before running the report, confirm the client's setup. Read `references/data-adapters.md` for detailed schemas per source.

### Ask the user:

| Question | Why it matters |
|----------|---------------|
| What attribution tool does the client use? (Cortana / Hyros / manual UTMs) | Determines which data adapter to use |
| What CRM / closer log do they use? (GHL, Airtable, Sheets, etc.) | Determines where qualitative data lives |
| What are the offer tiers and prices? | Needed for revenue validation and tier breakdown |
| What's the reporting period? | Sets the date range for all calculations |
| Is this the first run or an update to an existing dashboard? | First run = build from scratch. Update = merge new data with existing. |

### Collect these files from the user:

**Required:**
1. **Meta Ads Manager CSV** — ad-level export for the period. Used ONLY for spend and click data.
2. **Attribution tool export** — Cortana or Hyros CSV (sales export + calls export + optional aggregated report). This is the source of truth for all conversion data.

**Required for qualitative analysis (Level 3):**
3. **CRM / closer log** — with call outcomes, closer notes, and ideally "why bought / why didn't buy" fields.
4. **Call recording summaries** — AI-generated or manual. If Fathom/Read AI links are available, note them for deep-dive analysis.

**If any required file is missing:** Do not block. Run with what you have, clearly state what's missing and what analysis is limited.

---

## Step 1 — Ingest & Normalise Data

### CRITICAL RULE: Meta Attribution Is Not Truth
Meta over-counts, double-counts, and misattributes. **Never use Meta's reported conversions, leads, or revenue.** Meta is used ONLY for:
- Amount spent per ad/campaign/ad set
- Link clicks, CTR, CPC, impressions, reach, frequency

All conversion data (calls booked, closes, revenue, ROAS) comes from the third-party attribution tool (Cortana/Hyros) or the CRM. If Meta says 10 leads but Cortana says 3, Cortana wins. No exceptions.

### Normalise to canonical lead schema

Every lead record must be normalised to this structure regardless of source:

```
lead_id:           unique identifier (email is the dedup key)
lead_name:         full name
lead_email:        email address
generated_date:    date the lead first booked a call / entered pipeline
close_date:        date the deal closed (null if not closed)
outcome:           Closed/Won | Deposit | Pitched No Close | Disqualified | No-Show | Cancelled | Rescheduled | Remainder Collection
closer:            closer name
setter:            setter name (if available)
funnel_source:     VSL Funnel | Webinar | DM Funnel | Free Community | Organic | Other
offer_tier:        Standard | DIY+DFY | Consulting | Entry | client-specific tiers
cash_collected:    first payment amount (currency)
revenue:           full contract value / expected LTV (currency)
is_fu_call:        boolean — true if this is a follow-up, not the initial sales call
is_recurring:      boolean — true if this is a recurring payment, not a new close
utm_source:        from Cortana/Hyros or UTM parameter
utm_campaign:      from Cortana/Hyros or UTM parameter
utm_content:       the ad creative identifier — the key attribution field
utm_medium:        from Cortana/Hyros or UTM parameter
ad_set_name:       from Cortana/Hyros Origin Source / Last Source field
closer_notes:      free text — what happened on the call
why_bought:        free text — decision driver (closes only)
why_didnt_buy:     free text — blocker (pitched no close / DQ only)
primary_objection: category — Financial | Timing | Trust | Need | Spouse-Partner | Shopping Around | Fear | Not Ready | Other
fathom_url:        link to call recording
call_summary:      AI-generated summary of the call
```

### Dedup rules
1. **Email is the primary dedup key.** One lead = one row, regardless of how many calls they had.
2. **FU calls:** If a lead has multiple call records, the first chronological QUALIFIED call is the initial sales call. All subsequent calls are tagged `is_fu_call = true` and excluded from "calls booked" counts.
3. **Recurring payments:** If a lead has multiple sales records, the first is the new close. Subsequent records with "Recurring" in the info/name field are tagged `is_recurring = true` and excluded from "new close" counts but included in "All Cash" totals.
4. **Cancelled + rebooked:** If a lead cancelled then rebooked, use the rebooked date as generated_date.

### Data adapter selection
Read `references/data-adapters.md` and use the appropriate adapter based on what files the user provides. The adapters handle column mapping for:
- Cortana S3 exports (sales + calls)
- Hyros exports
- Meta Ads Manager CSV
- Airtable SRF table (Airtable model)
- Slack channel parsing
- Generic CSV with manual column mapping

---

## Step 2 — Calculate Funnel Metrics

Calculate for each time window (3d, 7d, 14d, 30d) and for each funnel source and combined:

### Spend & Traffic (from Meta Ads Manager only)
```
Total Ad Spend       = sum of Amount Spent per ad in the period
Link Clicks          = sum of Link Clicks
CTR                  = Link Clicks / Impressions * 100
CPC                  = Ad Spend / Link Clicks
```

### Call Booking (from Cortana/Hyros/CRM — NOT Meta)
```
Calls Booked         = count of leads with generated_date in period (excluding FU calls)
Show Rate            = Calls Held / Calls Booked * 100
   where Calls Held  = leads with outcome in (Closed/Won, Deposit, Pitched No Close, Disqualified)
Cost Per Call Booked = Ad Spend / Calls Booked
```

### Call Quality
```
Qualified Calls      = leads with outcome in (Closed/Won, Deposit, Pitched No Close)
Quality Rate (held)  = Qualified Calls / Calls Held * 100
Quality Rate (booked)= Qualified Calls / Calls Booked * 100
Disqualified         = count of DQ outcomes
```

### Conversion
```
Closes               = count of Closed/Won outcomes (excluding recurring)
Close Rate (qual.)   = Closes / Qualified Calls * 100
Close Rate (held)    = Closes / Calls Held * 100
Cost Per Close       = Ad Spend / Closes
```

### Revenue — THREE DISTINCT NUMBERS
```
New Cash (from this period's leads) = sum of cash_collected where generated_date is in the selected window
All Cash (collected this period)    = sum of cash_collected where close_date OR payment_date is in the selected window
Total Cash (cumulative)             = sum of all cash_collected across all time

New Cash ROAS        = New Cash / Ad Spend for the same period
All Cash ROAS        = All Cash / Ad Spend for the same period
Revenue ROAS         = sum of revenue (contract value) for period's leads / Ad Spend
```

### Sales Cycle
```
Avg Sales Cycle      = mean(close_date - generated_date) across all closes, in days
```
Break down by funnel source and offer tier.

### Payment Plan Completion
```
PP Completion Rate   = Total Cash Collected from PP Clients / Total Contracted Revenue from PP Clients * 100
Expected Remaining   = Total Contracted Revenue from PP Clients - Total Cash Collected from PP Clients
```
Break down by month of close, closer, offer tier.

---

## Step 3 — SQIBNT Lead Quality Scoring

Read `references/sqibnt-scoring-guide.md` for the full scoring rubric with calibration examples.

For every lead that has closer notes or call summaries, score on 6 dimensions (1-5 each):

| Dimension | What it measures |
|-----------|-----------------|
| **S — Sellable** | Was the lead reachable, receptive, and engageable? |
| **Q — Qualified** | Does the lead match the ICP? Right industry/role/situation? |
| **I — Intent** | Genuine interest in solving their problem? Research-first or impulse? |
| **B — Budget** | Can they afford the offer? Financial DQ signals? |
| **N — Need** | Real, urgent problem the offer solves? |
| **T — Timing** | Ready to act now, or "someday"? |

**Composite LQS** = average of all 6 scores.

**Classification:**
| LQS | Class | Colour |
|-----|-------|--------|
| 4.0-5.0 | Dream Lead | Green |
| 3.0-3.9 | Qualified | Blue |
| 2.0-2.9 | Marginal | Amber |
| 1.0-1.9 | Bad Lead | Red |

### Roll up to ad creative level
For each ad creative (utm_content value), calculate:
- **Avg LQS (period)** — average LQS of leads generated by this ad within the selected time window
- Lead count, close count, DQ count, no-show count, pipeline count
- Revenue, cash collected
- Distribution: % Dream, % Qualified, % Marginal, % Bad

### Extract from notes (if available)
For each lead, also extract:
- **Why bought / Why didn't buy** — the actual decision driver or blocker
- **Primary objection** — categorised
- **Recurring objection patterns** — across multiple leads from the same ad

---

## Step 4 — Build the Dashboard

Generate an interactive HTML file. Read `references/dashboard-template.html` for the base template if it exists. Otherwise, build from the specification below.

The dashboard is a single self-contained HTML file with embedded CSS and JavaScript. Data is stored as a JSON object embedded in a `<script>` tag. No external dependencies, no server needed.

### Layout Sections

**1. Header Bar**
- Client name, report period, last updated timestamp
- Time window toggles: [3D] [7D] [14D] [30D] — clicking recalculates all metrics

**2. Executive Summary Cards**
Row of metric cards:
- New Cash (from this period's leads) + delta arrow
- All Cash (collected this period)
- Total Cash (cumulative)
- Closes (count)
- Bad/DQ Leads (count)
- Active Pipeline (count)
- Avg Sales Cycle (days)
- PP Completion Rate (%)
- New Cash ROAS
- All Cash ROAS

**3. Ad Creative Performance Table**
Sortable, filterable. One row per ad creative:

| Ad Creative | Spend | Leads | Closes | New Cash | All Cash | ROAS | Avg LQS | Dream% | Bad% | Show Rate | Action |

- Avg LQS cells colour-coded (green/blue/amber/red)
- Action column: auto-recommendation based on KPI framework thresholds:
  - ROAS >1.5 + LQS >3.5 → **SCALE** (green)
  - ROAS 1.0-1.5 → **MONITOR** (blue)
  - ROAS 0.7-1.0 → **WATCH** (amber)
  - ROAS <0.7 OR LQS <2.0 → **KILL** (red)
  - <$200 spend → **EARLY DATA** (grey)
- Click any row → expands to show lead-level detail

**4. Lead Detail (expandable per ad)**
When ad row is clicked, shows every lead attributed to that ad:

| Lead | Generated | Closed | Outcome | Closer | S | Q | I | B | N | T | LQS | Notes |

- Outcome as colour-coded pills
- SQIBNT scores individually coloured
- Notes truncated with expand toggle
- "Why bought / didn't buy" shown if available

**5. Campaign Attribution**
Roll-up by campaign:
- Volume, close rate, avg LQS, revenue, ROAS
- Stacked bar showing Dream/Qualified/Marginal/Bad distribution per campaign

**6. Closer Performance**
Per closer:
- Leads handled, close rate, avg deal size, avg LQS of leads received
- Distinguishes lead quality from closing ability

**7. Pattern Detection (auto-generated)**
Analyse the dataset and surface:
- Which creatives produce the most DQs?
- Which funnel source has the cleanest close rate?
- Most common DQ/no-buy reason?
- GC/engagement signals predicting no-shows?
- Creatives driving pipeline but not closes (timing stalls)?
- Objection clusters by ad creative?
- New cash vs expected cash gap (PP collection issues)?

**8. Recommended Actions**
Auto-generated action items with owner tags:
- "KILL [creative] — avg LQS 2.1, 5 DQs, 1 close" → Media Buyer
- "Add financial pre-qualifier — 4 post-call financial DQs" → Setter SOP
- "SCALE [source] — 100% close rate, avg LQS 4.3" → Media Buyer

**9. Source Summary Table (Appendix)**
One row per source/campaign: closes, pipeline, bad/DQ, notes.

### Design System

```css
/* Colour palette */
--dark-blue:    #1F3864;    /* headers, section bars */
--mid-blue:     #2E75B6;    /* dividers, totals */
--accent:       #EBF3FB;    /* label cells */
--light-grey:   #F2F2F2;    /* alternating rows */
--white:        #FFFFFF;
--green:        #1E7E34;    /* strong performance, Dream leads */
--blue:         #2E75B6;    /* Qualified leads */
--amber:        #B8860B;    /* watch items, Marginal leads */
--red:          #C0392B;    /* poor performance, Bad leads */
--text-dark:    #2C3E50;    /* primary text */
--text-mid:     #7F8C8D;    /* secondary text */

/* Typography */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
/* Headers: 600 weight, dark-blue */
/* Body: 400 weight, text-dark */
/* Metric cards: large numbers, bold */
```

### Rolling Update
When updating an existing dashboard:
1. Read the existing HTML file
2. Extract the embedded JSON data
3. Merge new leads (dedup by email)
4. Recalculate all metrics for all time windows
5. Regenerate the HTML
6. Save to `outputs/[client-name]-lead-quality-dashboard.html`

---

## Step 5 — Quality Checks

### Number Audit
- All combined metrics = sum of individual funnels
- All rates = numerator / denominator, rounded to 1 decimal
- New Cash ROAS uses only cash from leads generated in the period
- All Cash ROAS uses all cash collected in the period
- Close counts exclude recurring payments and FU calls
- Lead counts exclude FU calls

### Attribution Integrity
- Never use Meta's reported conversions. Cortana/Hyros is truth.
- Leads with no utm_content go to "Unattributed" bucket — not assigned to any ad.
- Organic/no-UTM closes noted separately, not mixed with paid ad attribution.
- Recurring payments clearly separated from new closes.

### Language Audit
- No em dashes in prose (use comma, full stop, or colon)
- No "genuinely", "straightforward", "it's worth noting"
- Specific numbers, names, dates — never vague summaries

---

## Step 6 — Present to User

1. Show the dashboard in browser: `open outputs/[client-name]-lead-quality-dashboard.html`
2. Present key findings in chat — top 3-5 insights from the pattern detection
3. Present recommended actions with owner tags
4. Ask if the user wants a Google Doc summary for client sharing

---

## Failure Modes

| Failure | What happens | Fix |
|---------|-------------|-----|
| No attribution tool data | Can't calculate ROAS by creative | Request Cortana/Hyros export |
| No closer notes | SQIBNT scoring not possible | Run at Level 1 (ROAS only), flag gap |
| Missing UTM content on leads | Leads go to "Unattributed" bucket | Report % unattributed, suggest fixing at source |
| FU calls not tagged | Call counts inflated | Apply dedup by email + date, flag leads with multiple calls |
| Recurring payments mixed with new closes | Close count and revenue inflated | Filter by "Recurring" flag or first-sale-per-email logic |
| Meta and Cortana spend don't match | Confusing discrepancy | Use Meta for spend, Cortana for conversions. Note the discrepancy. |
| Junk/spam leads in data | Skews metrics | Filter obvious junk (profanity in name, fake emails), note in report |

---

## Constraints

- This skill reads data files the user provides. It does not connect to Meta Ads Manager, Cortana, or Hyros APIs directly.
- SQIBNT scoring requires closer notes or call summaries. Without them, the skill runs at Level 1 (ROAS attribution only) or Level 2 (funnel metrics) — still useful, just not qualitative.
- The dashboard is a static HTML file. It does not auto-refresh. Each weekly update requires running the skill again.
- Payment plan completion tracking requires historical payment data, not just the initial close record. If this data isn't available, flag it and skip the PP section.
