# The Bottleneck Diagnostic Framework

## Table of Contents
1. [Core Principles](#1-core-principles)
2. [The Five Root Cause Hypotheses — Full Diagnostic Logic](#2-the-five-root-cause-hypotheses)
3. [The "Perfect Storm" Prioritisation Logic](#3-the-perfect-storm-prioritisation-logic)
4. [Common Misdiagnoses](#4-common-misdiagnoses)
5. [Real-World Case Studies](#5-real-world-case-studies)

---

## 1. Core Principles

**Top-Down Always.** Start at the account level. Move to campaign. Then ad set. Then individual ad. Never jump straight to the ad level unless explicitly instructed by the user. The account-level view tells you the *size* of the problem. The ad-level view tells you the *cause*.

**No Conclusion First.** Pull the data. Identify the mathematical break point. Then form a thesis. Do not decide "it's creative fatigue" before looking at frequency, CTR trend, and CPM data.

**The 30% Threshold.** A shift of >30% in any key metric (CPP, CPM, CVR, CPMr) over the comparison period triggers an investigation. Even a 30% CPM spike with flat CPP warrants investigation — something else is compensating, and that may not last.

**The "Not Enough Data" Rule.** An ad that has spent less than 2–4x the target CPA has not generated meaningful signal. Do not kill it unless it has spent 1x CPA with zero conversions (hard kill threshold). Spending $400 on a funnel with a $400 target CPL and getting 0 calls = kill. Spending $200 on the same funnel = wait.

**Triangulate Before Concluding.** Never commit to a single-cause diagnosis. You need at least two independent data points pointing to the same narrative before acting.

---

## 2. The Five Root Cause Hypotheses

### Hypothesis A: Creative Fatigue

**What it is:** The same people have seen the same ad too many times. They are ignoring it. CTR drops, CPM rises as the algorithm has to work harder to find anyone who will engage.

**How to confirm it:**
- Pull frequency, CTR (link), and CPM at the *individual ad level* for both baseline and crisis periods
- True fatigue = Frequency >2.5 AND CTR dropping AND CPM rising on the same ad, same period
- The three signals must occur together. One alone is not fatigue.

**How to rule it out:**
- Frequency <1.5 + CTR flat = NOT fatigue. Do not call it fatigue. Look at Hypotheses B, C, or D.
- CTR dropping + Frequency low = wrong audience or weak hook, not fatigue

**The common misdiagnosis:** Launching new ads that also fail is not evidence of bad creative. It is usually a structural problem (fragmentation, wrong exclusions, CBO allocation failure) that prevents any ad from working regardless of quality.

**Fix:** Pause the fatigued ad. Do not duplicate it — the audience has seen it. Launch a new concept or a meaningfully different angle.

---

### Hypothesis B: Audience Exhaustion

**What it is:** The algorithm has served the ad to all the high-intent buyers in the audience pool. It is now serving to lower-intent users who click (because the ad is still relevant to them) but do not buy (because they were never going to).

**How to distinguish from fatigue:**
- Fatigue = CTR *drops* (people stop clicking because they have seen it)
- Exhaustion = CTR *flat* but LPV→IC or LPV→Purchase rate *collapses* (people still click but don't buy)

**How to confirm it:**
- Pull LPV→IC conversion rate for old proven ads vs. new ads in the same audience for both periods
- If old ads show flat CTR but collapsing post-click conversion, and new ads in the same audience are converting cheaply, the audience pool for the old ads is exhausted
- Check spend allocation: if 30+ ad sets are running against the same broad audience simultaneously, they are collectively strip-mining the high-intent buyers and forcing the algorithm to serve lower-intent users to pace budget

**Fix:** Pause the exhausted ad set and let the audience replenish (typically 2–4 weeks). Consolidate the number of active ad sets targeting the same audience. Shift budget to the new ads that are still hitting unconsumed audience segments.

---

### Hypothesis C: CBO Budget Allocation Failure

**What it is:** In a CBO (Campaign Budget Optimisation) campaign, the algorithm has redistributed budget away from proven winning ad sets and toward new, unproven ad sets that are not converting. The winning ads did not fatigue — they were starved of budget.

**How to confirm it:**
- Pull ad-level spend for the baseline and crisis periods for the CBO campaign
- If a proven ad received $400+ in the baseline with strong CPP, and received <$20 in the crisis, it was budget-starved
- Check the CTR and CPM of the starved ad in the crisis period. If both are flat or improving, the creative is fine — the algorithm just stopped spending on it
- Identify which ad sets absorbed the budget in the crisis period. Are they new? Are they converting?

**The specific failure mode:** CBO algorithms will often shift budget toward newly launched ad sets (especially warm/MOFU ad sets) because they appear novel to the algorithm. These new ad sets may have zero purchase history, so the algorithm is essentially guessing — and often guessing wrong.

**Fix:** Either set minimum spend floors on the proven cold ad sets, or separate warm/MOFU ad sets into their own campaign so the CBO cannot cannibalize the cold budget.

---

### Hypothesis D: Placement Shift (Advantage+)

**What it is:** Meta's Advantage+ Placements has shifted budget toward lower-converting placements (Audience Network, Instagram, Messenger) and away from higher-converting placements (Facebook Feed).

**How to confirm it:**
- Pull placement breakdown for both baseline and crisis periods
- Calculate CPP per placement for both periods
- A 5% platform shift is not conclusive on its own — check whether the shift correlates with specific fatiguing ads or a structural change in the campaign

**Specific signals:**
- Suspiciously low CPC → check Audience Network. Calculate true CPC by removing Audience Network clicks: (Total Spend) / (Total Clicks - Audience Network Clicks)
- CPP spike with flat CTR → check if budget shifted to Instagram or Audience Network
- Instagram CPP 3–4x higher than Facebook CPP → Instagram is burning budget

**Fix:** Manually exclude Audience Network in placement settings. Consider excluding Instagram if CPP is consistently 2x+ higher than Facebook. Do not exclude blindly — confirm with data first.

---

### Hypothesis E: External / Attribution Change

**What it is:** A change outside the account (Meta algorithm update, iOS privacy change, attribution model change) is causing Meta's reported metrics to look worse than actual performance.

**How to confirm it:**
- Check third-party attribution (Hyros, ChartMogul, Northbeam). If Meta CPP spikes but third-party CAC is flat, it is a measurement artefact
- Check the ratio of CTR(All) to Link CTR. If CTR(All) is 3–5x higher than Link CTR, a large share of "conversions" were previously being attributed via non-link engagement actions (saves, shares, likes) — these are most exposed to attribution changes
- Check Twitter/X: search "meta change" or "meta attribution" and look for posts with high engagement and comments from multiple advertisers corroborating the same issue

**The April 2026 Meta Attribution Change:**
- Non-link interactions (saves, shares, likes) moved from click-through attribution to engage-through attribution with a 1-day window (down from 7 days)
- Video engaged view threshold dropped from 10 seconds to 5 seconds
- Accounts with high engagement-to-click ratios are most exposed (their conversions previously attributed via 7-day save/share window are now uncounted)
- Fix: Enable 1-day engage-through attribution in ad set settings. Do not make irreversible budget decisions until 3–5 days of data under the new model has accumulated

**Fix:** Enable engage-through attribution. Rely on third-party attribution for true CAC during the transition. Update benchmarks before making scaling decisions.

---

## 3. The "Perfect Storm" Prioritisation Logic

When multiple constraints are confirmed simultaneously, prioritise fixes in this order:

1. **Stop the bleeding first** — Pause any campaign or ad set burning significant budget with zero conversions. This is immediate and recovers spend today.
2. **Fix measurement before making further decisions** — If attribution is broken, every subsequent decision is based on corrupted data. Fix it before scaling or killing anything.
3. **Restore algorithm signal quality** — Consolidate ad sets to reduce fragmentation. The algorithm needs dense purchase signal to optimise. Fragmentation prevents this.
4. **Refresh fatigued creative** — Medium-term fix. Pause fatigued ads, launch new concepts.
5. **Structural fixes** — CPMr reduction (exclusions, upper funnel campaigns). Long-term health.

---

## 4. Common Misdiagnoses

**"Our creative is fatigued."**
The most common misdiagnosis. Advertisers launch new ads, none of them work, and conclude the creative team is underperforming. In reality, the new ads are being served to the same saturated audience because the account's exclusions, consolidation, and objective mix have not changed. New creative cannot fix a structural problem.

**"The algorithm is broken."**
When reach drops and performance deteriorates, advertisers assume Meta has changed something or penalised their account. In many cases, the algorithm is working exactly as instructed — it is finding the same high-intent users it always found, because nothing in the account structure has changed.

**"We need to increase budget."**
Scaling spend into a saturated account accelerates the problem. More budget served to the same narrow audience drives frequency higher and CPMr higher faster.

**"Instagram is the problem."**
A 5% shift in platform mix is not the cause of a 50% CPP spike. Check whether the platform shift is correlated with specific fatiguing ads rather than a structural change.

**"It's a landing page issue."**
Before blaming the landing page, confirm that the traffic quality has not changed. If CTR is flat and frequency is low, the same quality of people are arriving at the page. If the page was converting before and is not now, check for tech issues (page speed, payment processor, mobile optimisation) before rewriting copy.

---

## 5. Real-World Case Studies

### Case Study 1: The CBO Scaling Campaign Collapse (the account, March 2026)
**Symptom:** CBO scaling campaign went from $75–$89 CPP in the hot period to $693 CPP in the crisis period.
**Initial hypothesis:** Creative fatigue.
**What the data showed:** The winning ads (Kathy Disappear Reel: CTR 18.2% → 19.7%; Dolly Parton Scrambled Eggs: CTR flat) showed zero fatigue signals. The CBO had reallocated 90%+ of budget to newly launched warm MOFU ad sets that generated zero purchases.
**Root cause:** CBO Budget Allocation Failure (Hypothesis C). The winning cold ads were starved of budget.
**Fix:** Separate warm MOFU ad sets into their own campaign. Set minimum spend floors on proven cold ad sets.

### Case Study 2: The Attribution Cliff (the account, March 2026)
**Symptom:** Meta reported CPP spiked 30–50%. ChartMogul showed decent subscriber numbers.
**Root cause:** Meta's April 2026 attribution change reclassified non-link engagement conversions from 7-day click-through to 1-day engage-through. The account had a CTR(All)-to-Link-CTR ratio of 3.5x, meaning 71% of "clicks" were non-link engagement actions. A large share of previously attributed conversions disappeared from Meta's reporting.
**Fix:** Enable 1-day engage-through attribution. Use ChartMogul as source of truth during transition.

### Case Study 3: The B2B Spam Click Problem
**Symptom:** $734 spent, 0 conversions, $2.04 CPC (suspiciously low for enterprise B2B).
**Initial hypothesis:** Landing page issue.
**What the data showed:** Placement breakdown was relatively even — not Audience Network. Firmographic tool confirmed clicks were from the right job titles (heads of sales, enterprise).
**Root cause:** The landing page was the bottleneck. High-quality traffic was arriving but not converting due to a combination of poor mobile optimisation, no clear CTA above the fold, and insufficient proof (no testimonials, no case studies).
**Fix:** Mobile optimisation, CTA above fold, proof injection (testimonials, results screenshots).

### Case Study 4: The Perfect Storm (the account, November)
**Symptoms:** ROAS dropped from 0.84x to 0.62x over 9 days.
**Root causes (multiple simultaneous):**
1. AOV dropped 10% (offer/pricing issue)
2. Click-to-LPV rate collapsed (tech/tracking issue)
3. Winning ads fatigued (creative issue)
4. New ads launched during tech issue period got "one-shotted" with corrupted data
**Fix priority:** (1) Fix tech/tracking first, (2) restore AOV, (3) relaunch new ads with clean data.
