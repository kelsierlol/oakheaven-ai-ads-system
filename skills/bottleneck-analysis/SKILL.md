---
name: bottleneck-analysis
description: Expert-level diagnostic workflow for identifying and fixing constraints in Meta Ads accounts. Use when a user reports that an ad account, campaign, or funnel has "died," stopped performing, or experienced a sudden spike in Cost Per Result (CPP/CPA/CPL). Applies to direct purchase, lead gen/call booking, webinar, quiz, and subscription funnel types.
---

# Meta Ads Bottleneck Analysis

This skill runs a systematic, data-driven diagnostic to identify the exact root cause of performance degradation in Meta Ads accounts. The core principle is: **go deep, never stay generic.** A surface-level answer like "creative fatigue" is not acceptable. The analysis must drill through account → campaign → ad set → individual ad until the specific mathematical break point is isolated and proven with data.

---

## Step 0: Initial Setup — Ask Before You Pull

Before touching any data, ask the user for the following if not already provided:

1. **Funnel Type:** Direct Purchase / Low-Ticket, Lead Gen / Call Booking, Webinar, Quiz, Subscription App, or other?
2. **Target KPIs:** What is the target CPP/CPL/CPA and target Front-End ROAS?
3. **Kill/Scale Thresholds:** What are the specific spend thresholds for turning an ad off or scaling it? (e.g., "$150 spend, 0 purchases = kill")
4. **Third-Party Tracking:** Is there a third-party attribution tool in use? (Hyros, ChartMogul, Northbeam, etc.)
5. **Output Mode:** Does the user want a **full comprehensive analysis** (complete deep-dive report for team/client) or a **brief** (just identify the constraint and the fix)?

---

## Step 1: Establish the Baseline vs. Crisis Comparison

Always compare two periods:
- **Crisis period:** The last 2–3 days (when performance dropped)
- **Baseline period:** The 5–7 days immediately prior (when performance was good)

Pull both periods at the **account level** first. Do not start at the ad level.

---

## Step 2: Account-Level Triage

Pull these metrics for both periods and compare:

| Metric | What a Change Tells You |
|---|---|
| Cost Per Result (CPP/CPL) | Is there actually a problem? (>30% change = investigate) |
| Cost Per Link Click (CPLC) | Is the traffic getting more expensive? |
| Page Conversion Rate (CVR) | Is the traffic converting at the same rate post-click? |
| CPM | Is the auction getting more expensive? |
| CTR (Link) | Are people clicking through with intent? |
| CTR (All) | Are people engaging with the content at all? |
| Frequency | Are the same people seeing the ads repeatedly? |
| **CPMr** (CPM × Frequency) | **The leading indicator — is reach shrinking?** |
| Spend | Has total spend changed significantly? |

**The two-metric rule:** Cost Per Result is always a function of **CPLC × CVR**. If CPR spiked, one or both of these changed. Identify which one before going deeper.

**The 30% threshold:** A shift of >30% in any key metric over the comparison period is the trigger for a bottleneck investigation. Even if CPP is flat, a 30% CPM spike warrants investigation — something else must be compensating, and that compensation may not last.

**The "not enough data" rule:** If an ad has spent less than 2–4x the target CPA, nothing has really happened yet. Do not make definitive decisions on low-spend data unless the ad is completely failing (e.g., spent 1x CPA with zero conversions).

---

## Step 3: Funnel-Level Break Point Analysis

Once you know whether the issue is in traffic cost (CPLC) or post-click conversion (CVR), drill into the funnel to find the exact stage where the drop-off occurs.

**For Direct Purchase / Subscription:**
> Impressions → Link Clicks → Landing Page Views (LPV) → Initiate Checkout (IC) → Purchase

**For Lead Gen / Call Booking:**
> Impressions → Link Clicks → LPV → Form Start → Form Submit (Lead) → Call Booked → Show Rate → Close Rate → Cash Collected

**For each stage, calculate the conversion rate between stages for both periods.** The stage where the rate dropped most is the primary break point. Do not assume — calculate it.

---

## Step 4: Drill to Campaign → Ad Set → Ad Level

Once the funnel break point is identified, drill down through the account hierarchy to find *which specific campaigns, ad sets, and ads* are responsible. This is where generic analysis fails. You must get specific.

**At campaign level:** Which campaigns are driving the CPR spike? Are all campaigns affected or just one?

**At ad set level:** Which ad sets have the worst CPR in the crisis period? How has spend allocation shifted between baseline and crisis? Are budget-starved ad sets the issue?

**At ad level:** For the worst-performing ad sets, pull individual ad metrics. Compare each ad's performance between baseline and crisis. Identify:
- Which ads were generating purchases in the baseline but stopped in the crisis?
- Which ads are still working and why?
- Which new ads launched during the crisis period and are absorbing budget without converting?

---

## Step 5: Test the Five Root Cause Hypotheses

For each hypothesis, the check must be done with actual data — not assumed.

**MUST READ for full diagnostic logic:** `references/diagnostic-framework.md`
**MUST READ for metric interpretation:** `references/metric-interrelationships.md`
**MUST READ for funnel-type KPI baselines:** `references/funnel-kpis.md`

### Hypothesis A: Creative Fatigue
- **Check:** Frequency, CTR trend, CPM trend at the *individual ad level*
- **True fatigue signal:** Frequency >2.5 AND CTR dropping AND CPM rising on the same ad
- **Not fatigue:** Frequency <1.5 and CTR flat — do not call it fatigue; look elsewhere
- **Common misdiagnosis:** Launching new ads that also fail is NOT evidence of creative quality issues — it is usually a structural problem (fragmentation, wrong exclusions) that prevents any ad from working

### Hypothesis B: Audience Exhaustion
- **Check:** LPV→IC conversion rate trend for old proven ads vs. new ads in the same audience
- **Signal:** Old ads show flat CTR (people still click) but collapsing LPV→IC rate (people land but don't buy) — the algorithm has strip-mined the high-intent buyers and is now serving ads to lower-intent users
- **Distinguishing from fatigue:** Fatigue = CTR drops (people stop clicking). Exhaustion = CTR flat but post-click conversion collapses

### Hypothesis C: CBO Budget Allocation Failure
- **Check:** Ad-level spend allocation between baseline and crisis in any CBO campaign
- **Signal:** Proven winning ads received significant spend in baseline but near-zero in crisis; budget shifted to new/unproven ad sets that are not converting
- **Key insight:** The winning ads did not fatigue — they were starved of budget by the CBO algorithm. Check their CTR and CPM; if both are flat, the creative is fine

### Hypothesis D: Placement Shift (Advantage+)
- **Check:** Placement breakdown (Facebook vs. Instagram vs. Audience Network vs. Messenger) for both periods
- **Signals:**
  - Suspiciously low CPC → check for Audience Network spam (calculate true CPC excluding Audience Network clicks)
  - CPP spike with flat CTR → check if budget shifted to lower-converting platform (e.g., Instagram)
  - Note: A 5% platform shift is not conclusive on its own — check whether the shift correlates with specific fatiguing ads rather than a structural change

### Hypothesis E: External / Attribution Change
- **Check:** Ratio of link clicks vs. non-link engagement actions (saves, shares, likes, comments). Check third-party attribution tool. Check Twitter/X for Meta platform update news (search "meta change" and look for corroborated posts with high engagement and comments saying "happening to me too")
- **Signal:** Meta CPP spikes but third-party CAC is flat → measurement artefact, not real performance decline
- **Meta attribution change (April 2026):** Non-link interactions (saves, shares, likes) moved from click-through to engage-through attribution with a 1-day window. Accounts with high engagement-to-click ratios (>2.5x CTR(All) vs Link CTR) are most exposed. Enable 1-day engage-through attribution in ad set settings to restore visibility

---

## Step 6: The "Perfect Storm" — Multiple Simultaneous Failures

When multiple things break at the same time, do not try to identify a single root cause. List all confirmed constraints and prioritise them by mathematical impact on revenue/CAC.

**Prioritisation logic:** Which constraint, if fixed today, would have the largest immediate impact on Cost Per Result? Fix that first.

Example priority order:
1. Kill campaigns burning budget with zero conversions (immediate spend waste)
2. Restore attribution visibility (fixes measurement before making further decisions)
3. Consolidate ad sets (reduces fragmentation and restores algorithm signal quality)
4. Refresh creative for fatigued ads (medium-term)
5. Introduce upper funnel campaigns to reduce CPMr (structural, long-term)

---

## Step 7: Triangulate Before Concluding

Never commit to a conclusion based on a single data point. You need at least two independent data points pointing to the same narrative.

- Meta CPP spike + third-party CAC flat = attribution issue (not real performance decline)
- Meta CPP spike + third-party CAC also spiked = real performance decline
- High frequency + CTR dropping + CPM rising = creative fatigue confirmed
- High frequency + CTR flat + CPM flat = structural fragmentation (not fatigue)

---

## Output Format

Ask the user which mode they want before writing the output:

**Mode 1 — Brief:** 2–3 sentences identifying the constraint and the single most important action to take.

**Mode 2 — Full Comprehensive Analysis:** Use this exact structure:

---

# Bottleneck Analysis: [Account / Campaign Name]
**Period Analysed:** [Baseline dates] vs. [Crisis dates]

## 1. Executive Summary
[One paragraph. State the root cause clearly. Is it a traffic issue, a post-click issue, a structural issue, or a measurement issue? What is the single most important thing the reader needs to know?]

## 2. Funnel Breakdown — Baseline vs. Crisis

| Metric | Baseline | Crisis | Change | Verdict |
|---|---|---|---|---|
| Total Spend | | | | |
| Cost Per Result (CPP/CPL) | | | | |
| Cost Per Link Click | | | | |
| Page CVR | | | | |
| CPM | | | | |
| CPMr | | | | |
| Frequency | | | | |
| [Funnel stage rates] | | | | |

## 3. Root Cause Diagnosis
[Explain which hypothesis was proven correct and provide the specific data that proves it. Be explicit: "Ad X spent $450 in the baseline with 6 purchases ($75 CPP). In the crisis period it received $15 of spend and 0 purchases — not because it fatigued (CTR was 19.7%, up from 18.2%) but because the CBO algorithm reallocated budget to unproven warm ad sets."]

## 4. Winners vs. Dead Weight
[Identify the specific ads still working and explain what they have in common. Identify the specific ads that collapsed and explain the mechanism. This section must name individual ads with their metrics — not generic statements.]

## 5. Prioritised Action Plan
[Numbered list ordered by urgency and mathematical impact. Each item must be specific and actionable — not "refresh creative" but "pause ad X and ad Y immediately; they have spent $450 combined in the crisis period with zero purchases."]

---

## Key Principles to Never Violate

1. **Never stay at the surface.** "Creative fatigue" is not a conclusion — it is a hypothesis. Prove it with frequency, CTR trend, and CPM data at the individual ad level.
2. **Never make a conclusion before looking at the data.** Pull the numbers first, identify the mathematical break point, then form a thesis.
3. **Never act on a single data point.** Triangulate before committing to a diagnosis.
4. **Never confuse measurement change with performance change.** Always check third-party attribution when Meta numbers spike.
5. **Never kill an ad that is not fatigued.** If frequency is low and CTR is flat, the ad is not the problem.
