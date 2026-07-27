---
name: media-buying-sop-generator
description: Takes client offer economics and funnel data, reverse-engineers KPIs, and produces a complete per-client Media Buying SOP with specific budget brackets, kill/scale rules, daily review protocol, and weekly cadence that a media buyer can follow without interpretation.
---

# Client KPI & Media Buying SOP Generator

Build a per-client Media Buying SOP. The output is an operational playbook that any media buyer can follow daily without needing to interpret or calculate anything — every threshold, bracket, and action is pre-computed from the client's economics.

## Before You Start

1. Read `context/business.md` — pull any existing KPI data, offer details, or funnel structure from there
2. Read `context/ad-account.md` — pull current spend, performance benchmarks, and campaign structure
3. If historical ad data is available, use it to validate assumptions rather than relying on industry benchmarks
4. The full KPI/kill-scale framework, daily optimisation protocol, and creative testing structure are all embedded in this skill — no external SOPs required

## Inputs Required

Collect ALL of the following before generating. If any are missing, ask for them. Don't guess — wrong inputs produce wrong kill thresholds, which costs real money.

### Core Economics
| Input | What to ask | Example |
|-------|-------------|---------|
| **Client name** | | Example Client |
| **Funnel type** | Call / Webinar / Low-ticket / Subscription-App | Call funnel |
| **Offer price (headline)** | What's the sticker price? | $6,000 |
| **Average sale price (actual)** | After discounts, payment plans, downsells — what's the real average? | $4,200 |
| **LTV (estimated)** | Total revenue per customer over their lifetime | $6,500 |
| **Gross margin %** | Revenue after COGS (not after opex) | 80% |
| **Operational cost per customer** | Fulfillment, support, platform, commissions | $500 |
| **Monthly ad budget** | Starting monthly spend | $50,000 |
| **Daily spend target** | Monthly ÷ 30 (or client-specified) | $1,700 |
| **Desired ROAS (gross)** | What does the client want to see? | 4.0x |

### Funnel Conversion Rates
**For call funnels:**
| Input | Source | Example |
|-------|--------|---------|
| **Cost per booked call (estimated or historical)** | From prior ads or industry benchmark | $200 |
| **Show rate** | % of booked calls that actually happen | 50% |
| **Quality rate** | % of held calls that are qualified | 80% |
| **Close rate** | % of quality calls that close | 30% |
| **Cash collected rate** | % of total sale collected upfront | 50% |

**For webinar funnels:**
| Input | Source | Example |
|-------|--------|---------|
| **Cost per registration (estimated)** | | $5 |
| **Show rate** | Registration → attendance | 25% |
| **Close rate** | Attendee → purchase | 8% |

**For low-ticket funnels:**
| Input | Source | Example |
|-------|--------|---------|
| **Cost per landing page view** | | $0.40 |
| **LPV → purchase conversion rate** | | 4% |
| **OTO/upsell take rate** | | 15% |
| **OTO price** | | $297 |

**For subscription/app funnels:**
| Input | Source | Example |
|-------|--------|---------|
| **Monthly price** | | $47 |
| **Average retention (months)** | | 18 |
| **Churn rate (monthly)** | | 5% |

### Campaign Context
| Input | Example |
|-------|---------|
| **Number of active creatives** | ~45 |
| **Number of proven winners** | 8 |
| **Creative production capacity (concepts/week)** | 5 (realistic, sustainable cadence — not aspirational) |
| **Campaign structure** | ABO testing + CBO scaling / ABO only |
| **Ads per ad set** | 1 (ABO isolation) or 3 (concept grouping — the default) |
| **Pixel conditioning method** | Typeform redirect / Calendly routing / CAPI from CRM / None |
| **Tracking platform** | Hyros / Cortana / Meta only |
| **Currency** | USD / AUD / EUR |

---

## Calculation Engine

### Step 1 — Reverse-Engineer Target CAC

```
Max CAC = (LTV × Gross Margin) - Operational Cost Per Customer
```

Example: ($6,500 × 0.80) - $500 = **$4,700 max CAC**

This is the absolute ceiling. The operational target should be significantly lower to allow for scaling headroom.

### Step 2 — Calculate CPQC (Call Funnels)

The primary KPI for call funnels is **Cost Per Quality Call (CPQC)**, not ROAS. ROAS depends on the sales team. CPQC is within media buying control.

```
CPQC = Cost Per Booked Call ÷ (Show Rate × Quality Rate)
```

Example: $200 ÷ (0.50 × 0.80) = $200 ÷ 0.40 = **$500 CPQC**

This becomes the **max ad set spend before kill decision**. If an ad set spends $500 with zero quality calls, it gets turned off.

### Step 3 — Calculate Kill and Scale Thresholds

**Kill thresholds (these go into the SOP):**

| Checkpoint | ROAS-based kill | Spend-based kill (no results) |
|------------|----------------|-------------------------------|
| Immediate | ROAS < 0.5 | Ad: spend > CPQC with 0 results → off |
| 3-day | ROAS < 0.5 → pause | Ad set: spend > 2× CPL benchmark with 0 results → off |
| 7-day | ROAS < 0.7 → pause and diagnose | |
| 14-day | ROAS < breakeven → pause permanently | |

**Scale thresholds:**

| Condition | Action |
|-----------|--------|
| ROAS > 1.5 for 7+ days | Scale 15-20% (one tier up in bracket system) |
| ROAS 1.0-1.5, stable | Hold or scale max 10% |
| CPL < target × 0.85 | Scale 20-30% |

### Step 4 — Calculate Budget Brackets

Budget brackets are calibrated to the client's daily spend target, CPL benchmark, and creative testing volume.

**Formula for bracket tiers:**

| Tier | Condition | Budget formula |
|------|-----------|---------------|
| 1 — New | 0 results, any spend | Starting test budget (usually $20-100/day depending on account size) |
| 2 — First Signal | 1 result, any CPL | 0.375× CPL benchmark (e.g. $75 at $200 CPL) |
| 3 — Proving | 2+ results, CPL > 1.75× benchmark | 0.75× CPL benchmark |
| 4 — Above Benchmark | 2+ results, CPL between 1× and 1.75× benchmark | 1.5× CPL benchmark |
| 5 — At Benchmark | CPL ≤ benchmark | 2× CPL benchmark |
| 6 — Strong | Consistent CPL well under benchmark | 6× CPL benchmark |
| 7 — Top Performer | Best in account | 10× CPL benchmark |
| 8 — Maximum Cap | Hard ceiling | 15× CPL benchmark (capped at 10% of daily target) |

**Kill threshold for no-results ads:**
```
Kill spend = 2× CPL benchmark
```
At $200 CPL → kill at $400 spent with 0 results.
At starting budget of $20/day, that's ~20 days of testing. At $100/day, that's ~4 days.

**Color coding thresholds:**
```
Green: CPL ≤ benchmark
Yellow: CPL > benchmark but < 1.75× benchmark  
Red: CPL > 1.75× benchmark
Blue: Top performers, CPL well under benchmark
```

### Step 5 — Calculate Testing Budget Allocation

```
Testing budget = 30% of daily spend target
Creatives per week = testing budget ÷ starting budget per creative ÷ 7 days
```

Example: $1,700/day × 0.30 = $510/day testing budget. At $20/creative/day = 25 creatives in testing at once. At $100/creative/day = 5 concepts in testing at once.

### Step 5.5 — Size The Testing Volume (How Many Ad Sets To Run)

This is the most-missed step. Correct ad set count depends on BOTH daily spend AND creative production capacity — bounded by the lower of the two.

```
Spend-based cap = Daily Spend ÷ $50  (at the $50/day starting budget per ad set)
Creative-based cap = Creative Production (concepts/week) × 2

Target ad set count = MIN(Spend-based cap, Creative-based cap)
```

**Why "Creative Production × 2"?** You don't want 1:1 refresh rate — you want a 2:1 ratio between what's live and what's in your pipeline. As ads fatigue or get killed, you have replacements ready. Without this buffer, you hit creative starvation within 3-4 weeks.

**Reference points (spend-based cap alone):**

| Daily Spend | Max Ad Sets (by spend) |
|-------------|------------------------|
| $100/day | 2 |
| $200/day | 4 |
| $500/day | 10 |
| $1,000/day | 20 |
| $2,000/day | 40 |
| $5,000/day | 100 |

**Reference points (creative cap alone):**

| Concepts Produced/Week | Max Ad Sets (by creative) |
|------------------------|---------------------------|
| 1 | 2 |
| 2-3 | 4-6 |
| 5 (the standard) | 10 |
| 10 | 20 |
| 20+ | 40+ |

**Ramping logic** (also needs to go in the SOP):
- Week 1: Launch ~30% of target ad set count
- Week 2: Add another ~30% based on week 1 signals
- Week 3-4: Fill to capacity as creative pipeline matures
- Ongoing: Replace killed ad sets at creative production rate

**Flag mismatches loudly:**
- High spend, low creative → account will plateau within 4 weeks. Recommend capping spend OR investing in creative pipeline.
- Low spend, high creative → budget starvation per ad set. Recommend consolidating to fewer ad sets at higher budgets.
- Client wants high scale without creative pipeline investment → this is the #1 agency failure mode. Must be addressed before SOP finalises.

**Output into SOP as:**

```
## Testing Volume Plan
- Starting ad set count (week 1): [N]
- Scale-to ad set count (week 4): [N]
- Creative production target: [X] concepts/week = [3X] ads with hook variations
- Expected kill rate (first 7 days of new tests): ~30%
- Sustainable scale requires replacement of ~[N] ad sets/week
```

### Step 6 — Build Scenario Models (High-Ticket Call Funnels)

For call funnels, build three scenarios using the CPQC math:

| Scenario | Show Rate | Quality Rate | Close Rate | CPQC | Deals/Month | Gross Revenue | ROAS |
|----------|-----------|-------------|------------|------|-------------|---------------|------|
| **Best case** | Input + 10% | Input + 10% | Input + 5% | Calculate | Calculate | Calculate | Calculate |
| **Base case** | Input | Input | Input | Calculate | Calculate | Calculate | Calculate |
| **Worst case** | Input - 15% | Input - 15% | Input - 10% | Calculate | Calculate | Calculate | Calculate |

Present all three to the client so expectations are set. Media buyer operates to the base case.

---

## Output: Per-Client Media Buying SOP

Generate the following document. Every number must be pre-calculated — no formulas, no "insert here," no placeholders. The media buyer should be able to print this and follow it.

**Save to:** `outputs/Media Buying SOP.md`

### Output Template

````markdown
# [CLIENT NAME] — Media Buying SOP

**Generated:** [DATE]
**Funnel type:** [Call / Webinar / Low-ticket / Subscription]
**Monthly ad budget:** [AMOUNT]
**Daily spend target:** [AMOUNT]
**Tracking platform:** [Hyros / Cortana / Meta]
**Currency:** [USD/AUD/EUR]

---

## Section 1: Funnel Economics & Benchmarks

### How This Funnel Works
[1-3 sentences describing the specific funnel flow for this client. E.g. "Ad → Landing page with VSL → Typeform qualifier → Calendly booking → Thank you page. Typeform routes unqualified leads to a disqualification page (no pixel fire). Only qualified scheduled calls fire the conversion event."]

### Key Metrics

| Metric | Current | Target | Notes |
|--------|---------|--------|-------|
| **Cost Per [Primary Event]** | [current if known] | $[TARGET] | Primary daily decision metric |
| **Show Rate** | [current if known] | [TARGET]% | [Booked → held calls] |
| **Quality Rate** | [current if known] | [TARGET]% | [Held → qualified calls] |
| **Cost Per Quality Call** | [current if known] | $[CPQC] | Max ad set spend before kill |
| **Close Rate** | [current if known] | [TARGET]% | [Quality → closed] |
| **Cost Per Acquisition** | [current if known] | $[TARGET CAC] | Spend ÷ closes |
| **Cash Collected ROAS** | [current if known] | [TARGET]x | Cash upfront ÷ spend |
| **Gross ROAS** | [current if known] | [TARGET]x | Total revenue ÷ spend |
| **Monthly Spend Target** | — | $[AMOUNT] | ~$[DAILY]/day |
| **Est. Clients/Month at Target** | — | ~[NUMBER] | At $[CAC] CPA |

### The $[CPL BENCHMARK] CPL Benchmark
[1-2 sentences explaining why this number was chosen and what margin of safety it provides. E.g. "The $200 target is conservative by design. Even if show rate dips to 45% or close rate drops to 25%, the economics remain profitable."]

---

## Section 2: Campaign Structure

### Two-Campaign Setup

| Campaign | Audience | Exclusions | Budget Type |
|----------|----------|------------|-------------|
| Campaign 1 — Cold | Broad / interest targeting | All warm audiences + [conversion event] last 30 days | ABO |
| Campaign 2 — Warm | Website visitors, IG/FB engagers | [conversion event] last 30 days | ABO |

### Ad Set Rules
- [Ads per ad set: 1 or 3 depending on client structure]
- ABO (Ad Set Budget Optimization) — [or CBO if specified]
- Each ad set gets its own budget based on its own performance
- [Any client-specific structural notes]

---

## Section 3: Ads Manager Setup

### Custom Column View
Create a saved column view with these columns:

| Column | Purpose |
|--------|---------|
| Budget | See and adjust daily budget per ad set |
| Amount Spent | Track delivery against budget |
| Results | Number of [conversion events] |
| Cost Per Result | Primary decision metric |
| Date Last Edited | Prevents double-editing same day |

### Saved Filters (Ad Set Level)

| Filter Name | Logic | Purpose |
|-------------|-------|---------|
| Had Delivery | Impressions ≥ 1 | Base — excludes paused/undelivered |
| No Results | Results = 0 | Ads spending with zero conversions |
| One Result | Results = 1 | Minimal proof — monitor closely |
| Scale | Results ≥ 2 | Proven ads — scale candidates |

### Color Coding (Cost Per Result Column)

| Color | Condition | Action |
|-------|-----------|--------|
| 🔴 Red | CPL > $[1.75× BENCHMARK] | Immediate decrease candidate |
| 🟡 Yellow | CPL $[BENCHMARK] – $[1.75× BENCHMARK] | Watch — do not increase |
| 🟢 Green | CPL ≤ $[BENCHMARK] | Performing — scale with caution |
| 🔵 Blue | CPL well under $[BENCHMARK] | Priority — push up bracket |

---

## Section 4: Budget Brackets

### Account-Specific Tiers
Calibrated for: $[DAILY]/day target, $[CPL BENCHMARK] CPL benchmark, $[STARTING BUDGET] starting budget, ~[N] active creatives.

| Tier | Condition | Daily Budget |
|------|-----------|-------------|
| 1 — New | 0 results, any spend | $[STARTING] |
| 2 — First Signal | 1 result, any CPL | $[TIER 2] |
| 3 — Proving | 2+ results, CPL > $[RED THRESHOLD] | $[TIER 3] |
| 4 — Above Benchmark | 2+ results, CPL $[BENCHMARK]–$[RED THRESHOLD] | $[TIER 4] |
| 5 — At Benchmark | CPL ≤ $[BENCHMARK] | $[TIER 5] |
| 6 — Strong | Consistent CPL well under $[BENCHMARK] | $[TIER 6] |
| 7 — Top Performer | Best in account | $[TIER 7] |
| 8 — Maximum Cap | Hard ceiling | $[TIER 8] |

### Kill Threshold — No Results
Turn off any ad set that has spent $[2× BENCHMARK] with zero results. At $[STARTING]/day starting budget, this allows ~[N] days of testing.

### The One-Tier Rule
Always move ONE tier at a time — up or down. Never jump multiple tiers in a single day. Meta's distribution engine cannot handle violent budget changes.

### Testing Budget Allocation

| Metric | Value |
|--------|-------|
| New creatives per week | ~[N] |
| Starting budget per creative | $[STARTING]/day |
| Daily testing spend | ~$[AMOUNT]/day |
| As % of daily target | ~[N]% |

### Testing Volume Plan

| Metric | Value |
|--------|-------|
| Starting ad set count (week 1) | [N] (30% of target) |
| Scale-to ad set count (week 4) | [N] (full capacity) |
| Spend-based cap | [N] ad sets |
| Creative-based cap | [N] ad sets |
| Binding constraint | [Spend / Creative] |
| Creative production target | [X] concepts/week ([3X] ads with hooks) |
| Expected kill rate (first 7 days) | ~30% |
| Sustainable refresh rate | ~[N] ad sets/week |

### Ramping Schedule

| Week | Action | Running Ad Sets |
|------|--------|-----------------|
| 1 | Launch starting batch | [N] |
| 2 | Add next batch based on week 1 signals | [N] |
| 3-4 | Fill to capacity as creative pipeline matures | [N] |
| Ongoing | Replace killed ad sets at creative production rate | [N] |

---

## Section 5: Daily Review Protocol

### Three Lookback Periods

| Period | Frequency | Purpose |
|--------|-----------|---------|
| All Time | Weekly (Monday) | Full account health — kill chronic underperformers |
| Last 7 Days | Weekly (Monday) | Week-long trends — upgrade proven, cut dead weight |
| Last 3 Days (Rolling) | Daily | Fast feedback — increase winners, decrease over-KPI |

### Weekly Review (Monday) — ~15 min

**All Time + Last 7 Days, run through each:**

1. **No Results filter** — Sort by spend descending. Turn off anything over $[KILL THRESHOLD] with 0 results. Leave under $[KILL THRESHOLD].
2. **One Result filter** — Turn off over $[KILL THRESHOLD] with only 1 result. Upgrade any $[STARTING] ad that got its first result → $[TIER 2].
3. **Scale filter** — Find high performers with low budgets. Upgrade by one tier. Only turn off Scale ads if CPL consistently over $[RED THRESHOLD].

### Daily Review (Tue–Fri) — ~3 min

Last 3 days rolling. Filter sequence:

| # | Action | Rule |
|---|--------|------|
| 1 | Open Scale filter | Look at color coding first |
| 2 | Decrease over-KPI ads (red/yellow over $[RED THRESHOLD]) | One tier down |
| 3 | Increase underweighted winners (blue/green) | One tier up |
| 4 | Open One Result filter | Check for budget adjustments |
| 5 | Decrease any over-KPI | One tier down max |
| 6 | Skip No Results filter | Weekly review catches these |
| 7 | Check Date Last Edited | Never touch same ad twice in one day |

---

## Section 6: Creative Pipeline

| Metric | Target |
|--------|--------|
| New creatives per month | ~[N] |
| New creatives per week | ~[N] |
| Starting daily budget per creative | $[STARTING] |
| Weekly testing spend (new only) | ~$[AMOUNT]/day |
| Kill threshold (no results) | $[KILL THRESHOLD] spent |
| Expected days to kill decision | ~[N] days |

### New Creative Launch Checklist
- [ ] Assign to correct campaign (cold vs warm)
- [ ] [1 ad per ad set / 3 hooks per ad set — per client structure]
- [ ] Set starting budget to $[STARTING]/day
- [ ] Confirm conversion event is set to [EVENT NAME]
- [ ] Confirm warm audience exclusions applied
- [ ] Confirm [conversion event] exclusion (last 30 days) applied
- [ ] Ad named per snake_case naming convention (see `skills/ad-naming-generator/SKILL.md`)
- [ ] UTMs include `{{ad.name}}` in utm_content
- [ ] Note launch date — determines when kill threshold applies

---

## Section 7: Scenario Models

[For call funnels — present the three scenarios calculated in Step 6]

| Scenario | Show Rate | Quality Rate | Close Rate | CPQC | Deals/Mo | Gross Rev | Cash ROAS | Gross ROAS |
|----------|-----------|-------------|------------|------|----------|-----------|-----------|------------|
| **Best** | | | | | | | | |
| **Base** | | | | | | | | |
| **Worst** | | | | | | | | |

---

## Section 8: Quick Reference Cheat Sheet

| Decision | Rule |
|----------|------|
| Ad set spent $[KILL THRESHOLD]+ with 0 results | Turn off |
| Ad set spent $[KILL THRESHOLD]+ with 1 result | Turn off |
| Ad got 1 result — was at $[STARTING] | Upgrade to $[TIER 2] |
| Ad is red (CPL > $[RED THRESHOLD]) | Decrease one tier |
| Ad is green (CPL ≤ $[BENCHMARK]) | Increase one tier |
| Ad is blue (top performer) | Increase one tier |
| Ad was already edited today | Do not touch — check tomorrow |
| Ad at $[TIER 8] (max cap) | Hold — do not increase |
| Ad at max starts fatiguing | Decrease one tier, let stabilize |
| Tempted to jump multiple tiers | Don't — one tier at a time, always |

---

## Section 9: Weekly Checklist

| Day | Time | Tasks |
|-----|------|-------|
| **Monday** | ~15 min | All-Time review (3 filters) → 7-Day review (3 filters) → 3-Day daily review → Launch new creatives (~[N]) |
| **Tuesday** | ~3 min | 3-day rolling: Scale filter → One Result filter. One tier moves only. |
| **Wednesday** | ~3 min | Same as Tuesday. Mid-week creative check: early signals on Monday's batch. |
| **Thursday** | ~3 min | Same as Tuesday. Confirm next week's creatives are in production. |
| **Friday** | ~5 min | 3-day review + end-of-week prep: confirm next batch ready, flag creatives approaching kill threshold, identify winners for Monday upgrade. |
| **Sat/Sun** | 0 min | Hands off. Weekend data feeds Monday's 3-day window. |

**Total time per week: ~29 minutes.**

---

**References:**
- `skills/daily-media-buyer-checkin/SKILL.md` — daily review workflow this SOP feeds into
- `skills/bottleneck-analysis/SKILL.md` — diagnostic when performance drops
- `skills/ad-naming-generator/SKILL.md` — naming convention applied to every ad
- `outputs/Naming Code Sheet.md` — the locked code sheet for this account
````

---

## Rules

1. **Every number must be pre-calculated.** No "insert X here." No formulas the media buyer needs to solve. The SOP is the answer, not the question.
2. **Budget brackets must be calibrated to the specific client.** Don't use generic tiers — calculate from their CPL benchmark, daily spend target, and creative volume.
3. **Kill thresholds must be tied to funnel economics.** The kill spend = 2× CPL benchmark is the default, but adjust if the client has unusual economics (very high ticket, very long sales cycle, etc.).
4. **If historical data exists, use it.** Prior performance beats industry benchmarks. If the client already knows their show rate is 65%, don't default to 50%.
5. **Present scenario models for sign-off before finalising.** The targets must be confirmed by the account owner before the SOP is locked.
6. **The SOP goes in the outputs folder.** Save to `outputs/Media Buying SOP.md`. Update `context/business.md` to reference it.
7. **CPQC is the primary KPI for call funnels, not ROAS.** ROAS depends on the sales team. CPQC is within media buying control. The media buyer optimises to CPQC. Sales performance is tracked separately and used to inform — not to kill ads.
8. **Cash collected ROAS must be tracked alongside gross ROAS.** If cash collected ROAS drops while CPQC is fine, that's a sales problem, not a media buying problem. The SOP should make this distinction explicit.
9. **Don't save without confirmation.** Present the draft in chat first, get sign-off, then save.
