---
name: ads-setup-engine
description: Builds the user's custom Meta ABO testing campaign structure — interviews them about their account, calculates personalised budget bands based on their CPR and target daily budget, applies the modifications (start at $50/day, 3 hook variations per ad set), and outputs a complete campaign structure document plus a live tracking sheet template. Triggers on "set up my ads", "campaign structure", "build my ABO structure", "calculate my budget bands", "ads setup", or "what's my campaign structure".
---

# Ads Setup Engine

Builds a custom Meta ABO testing campaign structure for lead gen accounts. The strategy is fixed — ABO testing with 3 hook variations per ad set, manual budget band management, kill/scale based on bands. What's NOT fixed is the specific dollar amounts of each band — those are calculated based on the user's account.

**This skill is lead gen only.** Direct purchase / e-com accounts use a different structure (CBO or Advantage+). Flag this upfront and refuse to run for e-com.

---

## The Strategy (Non-Negotiable)

1. **One campaign type: ABO Testing** — ad set budget optimization, not CBO
2. **One ad set per concept** — each concept from the creative strategy becomes its own ad set
3. **3 ads per ad set** — the 3 hook variations from the Script Generator are launched together inside the ad set
4. **Starting budget: $50/day per ad set** (standard — some start at $10/day, this system jumps straight to $50)
5. **Budget bands govern kill/scale** — not gut feel, not CBO delegation to Meta
6. **One band change per ad set per day** — tracked via "date last edited" column
7. **Weekly + Daily cadence** — weekly for long-lookback decisions, daily 3-day rolling for reactive adjustments

---

## What You Need Before Starting

1. `context/ad-account.md` filled in (from Guided Setup Phase 3 + KPI Tracker lock-in)
2. At least one creative strategy brief at `outputs/creative-strategy-*.md`
3. User has access to their Meta Business Manager (for implementation)

If either of the first two is missing, stop and tell the user to complete foundations setup first.

---

## Phase 1: Funnel Gate (1 min)

First question, before anything else:

> "Before we build your campaign structure — what are you running? Lead generation (people book a call / fill a form / apply) or direct purchase (people buy a product on the landing page)?"

If they say **direct purchase / e-com / shop / Shopify / checkout**:

> "This skill is for lead gen accounts only. The strategy we use — manual ABO testing with budget bands — works best when you have slow feedback loops and expensive conversions. For direct purchase, Meta's Advantage+ or broad CBO with the pixel firing at checkout usually beats manual management. I can't build this for you. Pause here and run a different campaign strategy."

Stop. Do not proceed.

If they say **lead gen**, continue to Phase 2.

---

## Phase 2: Account Interview (10 min)

Ask ONE question at a time. Push back on vague answers.

### Q1 — Target Monthly Spend
"What's your target monthly Meta ad spend over the next 90 days? Give me a specific number."

*Convert to daily: monthly ÷ 30. Use this as the working "target daily budget" for all band calculations.*

### Q2 — Current CPR (Cost Per Result)
"What's your current or most recent cost per result? A result means a qualified booked call for lead gen. Rough number is fine."

*If they don't know, pull from `context/ad-account.md`. If still unknown, push back:*

> "I can't build the bands without this. Run your last 30 days of data through the KPI Tracker skill first to establish this baseline. Come back when you know."

### Q3 — Target CPR
"What CPR are you aiming for? This should come from your KPI Tracker output — it's the maximum allowable cost per result that keeps you profitable."

*Pull from `context/ad-account.md` if they don't remember. If target is lower than current, note the gap — they need to close it through creative, not budget tricks.*

### Q4 — Account Average CPR
"What's your account-wide average CPR? Not your best ads, not your worst — the average across everything that spent money in the last 30 days."

*This becomes the centreline of the bands. Most ads sit here; winners are below, losers above.*

### Q5 — Concept Volume
"How many concepts are you launching right now from your creative strategy brief? (A concept = one persona + angle + format combination.) Each concept becomes one ad set."

*Pull from `outputs/creative-strategy-*.md` if uncertain — count the rows in the strategy map.*

### Q6 — Creative Production Cadence
"How many new concepts can you realistically produce per week going forward? Scripts, recorded, edited, uploaded. Be honest."

*This determines how aggressive the kill rules can be. If they can only produce 2/week, we can't kill 10 ads a week or the account goes dark.*

### Q7 — Risk Tolerance
"On a scale of 1-5: how aggressive do you want the scaling rules to be?
- 1 = Conservative (small budget increases, longer windows before acting)
- 3 = Balanced (default — recommended for most)
- 5 = Aggressive (fast increases, fast kills — only if creative pipeline is deep)"

*Default to 3 if they're unsure.*

### Q8 — Optimization Event
"What conversion event are you optimizing the pixel on? Book call / application submitted / lead form complete / other?"

*If they don't know, tell them:*

> "Set this up before launching. The optimization event is what Meta chases — wrong event = wasted spend. Use the event closest to a qualified lead (usually 'Lead' or 'Schedule' or a custom 'Qualified Booking')."

---

## Phase 3: Band Calculation (5 min processing)

Now calculate the 8 bands.

### The Logic

Reference bands (for $35K/day target spend):
- New ad with 0 results: $10/day
- 1 result (CPR > $850): $10
- 1 result (CPR $700-850): $50
- 1 result (CPR $500-700): $100
- 2+ results (CPR > account avg): $500
- 2+ results (CPR < account avg): $1,000
- Top performers: $2,000
- Max: $3,000

**standard modifications:**
- Starting band = $50/day (not $10) — matches our concept = 3 hooks launched together
- Second result band scales from $50 to $100 (not $10 to $50)
- All subsequent bands scale proportionally to the user's target daily budget

### The Calculation

Compute based on user inputs:

**Target daily budget** = monthly_spend / 30 (from Q1)
**Account average CPR** = user's answer (from Q4)
**CPR tiers:**
- Tier A = Top performers: CPR ≤ 60% of account average
- Tier B = Above average: CPR 60-100% of account average
- Tier C = At average: CPR 100-140% of account average
- Tier D = Below average: CPR 140-170% of account average
- Tier E = Fail: CPR > 170% of account average OR ≥ 2× target CPR

**Apply risk multiplier (from Q7):**
- Risk 1: multiply top-tier bands by 0.5x
- Risk 3: 1.0x (baseline)
- Risk 5: 1.5x

**Calculate the 8 bands:**

| # | Condition | Band Formula |
|---|-----------|--------------|
| 1 | New ad, 0 results, spend < 1× target CPR | $50/day (flat starting point) |
| 2 | 1 result, Tier D (below average) | $50/day |
| 3 | 1 result, Tier C (at average) | $100/day |
| 4 | 1 result, Tier B (above average) | min(target_daily_budget × 0.02, $500) × risk_multiplier |
| 5 | 2+ results, Tier C | min(target_daily_budget × 0.015, $250) × risk_multiplier |
| 6 | 2+ results, Tier B | min(target_daily_budget × 0.03, $750) × risk_multiplier |
| 7 | 2+ results, Tier A | min(target_daily_budget × 0.06, $1,500) × risk_multiplier |
| 8 | Top 1-2 ads in account | min(target_daily_budget × 0.10, $3,000) × risk_multiplier |

Round all band amounts to nearest $50 for clean operations.

**Kill rules:**
- 0 results AND spend ≥ 1× target CPR → Kill immediately
- 1 result AND spend ≥ 2× target CPR → Kill
- 2+ results AND CPR in Tier E → Drop one band, don't kill yet
- Any ad sitting at $50/day for 14+ days with no improvement → Kill (creative fatigue)

**Promote-to-scale rules:**
- 2+ results AND CPR in Tier A for 3+ consecutive days → Promote to Band 8
- Any ad at Band 8 for 7+ days with stable performance → Leave alone (no further increases — this is the cap)

---

## Phase 4: Generate Campaign Structure Doc

Write the complete structure to `outputs/campaign-structure.md`:

```markdown
# Campaign Structure — [Account Name or "Your Account"]
**Generated:** [Date]
**Strategy:** Manual ABO Testing + Band Management (standard)
**Funnel Type:** Lead Gen
**Target Monthly Spend:** $[from Q1]
**Target Daily Budget:** $[calculated]
**Account Average CPR:** $[from Q4]
**Target CPR:** $[from Q3]
**Risk Profile:** [1-5 from Q7]

## 1. Campaign Architecture

You will run ONE primary campaign:

**"[Account Code] — Testing — [MonthYear]"**

Type: Ad Set Budget Optimization (ABO)
Optimization event: [From Q8]
Attribution window: [From context/ad-account.md — typically 7DC 1DV for lead gen]

### Why ABO, Not CBO
You're running lead gen. Feedback loops are slow, signals are sparse, and Meta's algorithm isn't getting enough conversion data to allocate correctly. CBO will over-spend on the ad that gets cheap leads — not the ad that gets GOOD leads. ABO puts you in control of distribution so you can manually promote ads based on real results (show rate, close rate, CAC — not just cost per lead).

## 2. Ad Set Structure

**One ad set per concept.** A concept = persona + angle + format combination from your creative strategy brief.

**3 ads per ad set.** These are the 3 hook variations produced by the Script Generator (one concept, three different hooks — same body, same CTA, different opening).

**Starting budget: $50/day per ad set.**

Example ad set names (applying the naming convention from your SOP):
- `P1.2_UGC-Selfie_Ozempic-Refugee_6mo-Setup`
- `P2.1_Talking-Head_Menopause-Struggler_Free-Audit`

## 3. Your Custom Budget Bands

| Band | Condition | Daily Budget |
|------|-----------|--------------|
| 1 | New ad set, 0 results, under spend threshold | $50 |
| 2 | 1 result, CPR below average (Tier D) | $50 |
| 3 | 1 result, CPR at average (Tier C) | $100 |
| 4 | 1 result, CPR above average (Tier B) | $[calculated] |
| 5 | 2+ results, CPR at average (Tier C) | $[calculated] |
| 6 | 2+ results, CPR above average (Tier B) | $[calculated] |
| 7 | 2+ results, CPR top tier (Tier A) | $[calculated] |
| 8 | Top 1-2 ads in the account | $[calculated, capped at daily_budget × 0.10] |

## 4. Kill Rules

**Kill immediately if:**
- 0 results AND spend ≥ $[target CPR] (1× target CPR)
- 1 result AND spend ≥ $[2× target CPR]
- Any ad set at $50/day for 14+ days with no improvement

**Drop one band (don't kill yet) if:**
- 2+ results AND CPR in Tier E (>170% of account average)
- Performance degrades 2 bands in a single day

## 5. Scale Rules

**Promote up one band if:**
- Performance is at the next tier for 3+ consecutive days (3-day rolling lookback)
- Weekly review (7-day lookback) shows the ad has earned the upgrade

**Promote straight to Band 8 if:**
- 2+ results AND Tier A (top performer) for 3+ consecutive days

## 6. Management Cadence

### Daily (3 minutes, every morning)
1. Open Ads Manager → your Testing campaign
2. Filter: 3-day rolling lookback
3. Run through 4 filter views: No results / 1 result / Scale / Had delivery
4. Apply band rules mechanically — one band change per ad per day MAX
5. Use the "Date Last Edited" column to avoid double-moves

### Weekly (30 minutes, every Monday)
1. All-time lookback: kill anything over $1,000 total spend with 0 results
2. 7-day lookback: apply band rules more aggressively (promote proven winners, cut fatigued ones)
3. Pull the Daily A/B Band Management skill for a deeper diagnosis if anything looks off

## 7. Custom Filters To Set Up In Ads Manager

Create these 4 saved filter views today:

1. **Had Delivery** — Impressions > 0 (3-day lookback)
2. **No Results** — Results = 0
3. **1 Result** — Results = 1
4. **Scale** — Results ≥ 2

## 8. Custom Columns To Set Up

Name this column set "Performance Analytics":

- Ad Set Name
- Budget (Daily)
- Amount Spent
- Results (your optimization event)
- Cost Per Result
- Date Last Edited

Set this as your default column view in Ads Manager.

## 9. Conditional Formatting (Color Coding)

In Ads Manager, apply conditional formatting to the "Cost Per Result" column:
- **Green:** CPR ≤ 60% of account average (Tier A)
- **Yellow:** CPR 60-100% of account average (Tier B)
- **Orange:** CPR 100-140% of average (Tier C)
- **Red:** CPR > 140% of average or 0 results with high spend

This makes the daily 3-minute review viable.

## 10. Monthly Review & Recalibration

At the end of every month:
1. Recalculate account average CPR
2. If it's shifted by more than 20% from the value used to build these bands, re-run this skill
3. Re-examine risk tolerance — if your creative pipeline has scaled, raise risk profile; if it's shrunk, lower it
```

Show the user the output. Ask:

> "Here's your campaign structure. Read it back. Does this match your reality — your spend, your bandwidth, your team capacity? If the bands feel too aggressive or too conservative, say so and I'll recalculate."

Iterate on band numbers if needed. Save when approved.

---

## Phase 5: Tracker Sheet Template (3 min)

Generate a simple tracking sheet template and save to `outputs/ad-set-tracker.md`:

```markdown
# Ad Set Tracker — [Account Name]

Copy this into a Google Sheet or Airtable. Update weekly (or daily if you prefer).

| Ad Set Name | Concept ID | Launched | Current Budget | Current Band | Total Spend | Total Results | CPR | Status | Date Last Edited | Notes |
|-------------|-----------|----------|----------------|--------------|-------------|---------------|-----|--------|-----------------|-------|
| P1.2_UGC-Selfie_Ozempic-Refugee_6mo-Setup | B0001 | [date] | $50 | Band 1 | | | | Testing | | |
| ... | | | | | | | | | | |

Status options: Testing / Scaling / Paused-Fatigue / Paused-Kill / Won
```

Tell the user:

> "Drop this into a Google Sheet. Keep it updated weekly. This + the Ads Manager view + the Daily A/B Band Management skill = your complete ops stack."

---

## Phase 6: Wrap & Hand-off

Save to `memory/open-loops.md`:

```
## Ads Setup Engine — Complete
Date: [date]
Artifacts:
- outputs/campaign-structure.md (custom bands, kill/scale rules, cadence)
- outputs/ad-set-tracker.md (tracker template)

Next actions:
- Build the Testing campaign in Meta using this structure
- Apply naming convention to every ad set + ad
- Set up the 4 custom filters in Ads Manager
- Set up the "Performance Analytics" custom column set
- Apply conditional formatting
- Launch first 3-5 ad sets at $50/day
- Start using the Daily A/B Band Management skill from Day 1
```

Tell the user:

> "Your campaign structure is built. Next: go into Meta Ads Manager, build the campaign using this spec, launch your first 3-5 concepts. From tomorrow onward, your daily 3-minute ritual is the **Daily A/B Band Management** skill — paste your export, get your band moves, apply them.
>
> Weekly on Monday, run the full **Bottleneck Analysis** skill for deeper patterns.
>
> If you want me to walk you through the Meta Ads Manager setup step-by-step, say 'walk me through the build'."

If they want the walkthrough, provide it. Otherwise, wrap.

---

## Constraints

1. **Lead gen only.** Direct purchase accounts get refused at Phase 1.
2. **Never invent band numbers.** All calculations must trace back to user inputs.
3. **Starting budget is always $50/day per ad set.** Non-negotiable — this is the standard modification.
4. **3 ads per ad set.** Always. Hook variations from the Script Generator.
5. **Push back on vague answers.** If they say "I don't know my CPR", stop and send them to the KPI Tracker.
6. **Round to clean numbers.** $50, $100, $250, $500 — never $437 or $1,186.
