# Metric Interrelationships & Diagnostic Combinations

## Table of Contents
1. [The Metric Stack — What to Pull and Why](#1-the-metric-stack)
2. [CPMr — The Leading Indicator of Account Health](#2-cpmr)
3. [CTR vs CTR(All) — Engagement vs. Intent](#3-ctr-vs-ctrall)
4. [CPM Diagnostic Combinations](#4-cpm-diagnostic-combinations)
5. [Frequency — When to Worry, When to Ignore](#5-frequency)
6. [Hook Rate & Hold Rate — Video Ad Diagnostics](#6-hook-rate--hold-rate)
7. [CPC + CVR — The Trust Gap](#7-cpc--cvr)
8. [The Harvest vs. Plant Audit](#8-harvest-vs-plant-audit)

---

## 1. The Metric Stack

When pulling data for a bottleneck analysis, always pull these metrics in this order. Each layer narrows the diagnosis.

| Layer | Metrics to Pull | What It Tells You |
|---|---|---|
| Account / Campaign | Spend, CPP/CPL, ROAS, CPM, Frequency, CPMr | Is the account healthy or broken at the top level? |
| Funnel | Clicks, LPV, IC/Form Start, Purchase/Submit | Where exactly is the drop-off? |
| Ad Set | Spend allocation %, CPP per ad set, Reach, Frequency | Is budget going to the right places? |
| Ad | CTR, CTR(All), CPM, Frequency, Hook Rate, Hold Rate, LPV→IC rate | Which specific ads are working and which are dead? |

---

## 2. CPMr — The Leading Indicator of Account Health

**CPMr = CPM × Frequency** (Cost Per 1,000 Unique Accounts Reached)

CPMr is the most important metric in the account for diagnosing long-term structural health. It moves *before* ROAS and CPA deteriorate. By the time CPP spikes, CPMr has usually been climbing for weeks.

### Why CPMr Matters More Than CPM Alone
CPM tells you how expensive it is to buy 1,000 impressions. CPMr tells you how expensive it is to reach 1,000 *different people*. An account can have a flat CPM but a rising CPMr if frequency is climbing — meaning you are paying the same per impression but showing ads to the same people over and over.

### CPMr Benchmarks

| Signal | Interpretation | Action |
|---|---|---|
| CPMr flat or declining | Reaching new people efficiently | Maintain structure, scale with confidence |
| CPMr rising 10–20% over 30 days | Early warning — frequency or CPM creeping | Review exclusions, check ad set count |
| CPMr rising >30% over 30 days | Active audience saturation | Full playbook: exclusions, consolidation, creative refresh, upper funnel |
| CPMr high but ROAS strong | Harvest loop — over-indexed on warm audiences | Introduce Plant Intent creative, audit reach per ad |
| Frequency >3.0 over 7 days | Exclusions insufficient for current spend | Escalate exclusions to website visitors + social engagers |

### The "Slow Death" Trajectory
> Month 1: CPMr $55 → Month 3: CPMr $75 → Month 6: CPMr $110 → Month 9: CPMr $150

New visitor % drops. Frequency climbs. Growth stalls. ROAS looks fine because the algorithm is harvesting warm audiences — until the warm pool is exhausted and CPP collapses suddenly.

### How to Reduce CPMr (in order of impact)
1. **Increase exclusions** — Add recent purchasers, email list, website visitors (30–60 days), social engagers (30–60 days)
2. **Consolidate ad sets** — Fewer ad sets = less auction overlap = lower frequency
3. **Diversify creative** — Different concepts reach different audience segments, reducing CPM
4. **Launch Partnership Ads** — Creator/whitelist ads reach new audience pools at lower CPM
5. **Invest in upper funnel campaigns** — Awareness/Video View campaigns reach cold audiences the Purchase algorithm ignores

---

## 3. CTR vs CTR(All) — Engagement vs. Intent

**CTR(All)** includes all clicks: link clicks, likes, comments, shares, saves, profile taps, "see more" expansions.
**CTR (Link Click)** includes only clicks that take the user to the destination URL.

### The Ratio Rule
You generally want to see **CTR(All) running 2.5–5x higher than Link CTR**. This gap tells you people are consuming the content — clicking "see more," engaging, sharing — which signals they are in the education/permission-seeking phase. This gap is data for your next ad brief.

### Diagnostic Combinations

| CTR(All) | Link CTR | Interpretation |
|---|---|---|
| High | High | Strong ad — people engage AND click through with intent |
| High | Low | Curiosity traffic — people engage but don't convert. Ad creates interest but not enough belief/proof to click. |
| Low | Low | Weak hook or wrong audience — people are not stopping to engage at all |
| Low | High | Unusual — direct-response ad with minimal social engagement. Check if CPP is good; if yes, leave it alone |

### The "Curiosity Traffic" Problem
An ad with 50%+ hook rate, 12% CTR, and under 10 seconds on the landing page is generating pure curiosity clicks with no purchase intent. The ad is creating interest but not installing enough belief. The fix is more proof in the ad (testimonials, results, case studies), not a new landing page.

---

## 4. CPM Diagnostic Combinations

CPM alone means nothing. Always pair it with CTR and Frequency to get the full picture.

| CPM | CTR | Frequency | Interpretation |
|---|---|---|---|
| High | Low | Low | Bad messaging OR algorithm doesn't know who to show it to. Test new creative angles. |
| High | Low | High | Classic creative fatigue — same people seeing the same ad and ignoring it |
| High | High | Low | Competitive niche — expensive but effective. Check ROAS before touching anything |
| Rising | Dropping (over time) | Rising | Hitting the same segment repeatedly — burnout. Check frequency, refresh creative |
| Rising | Flat | Flat | CPM inflation from auction competition — may be seasonal or platform-wide |
| Low | High | Low | Healthy account — cheap reach, strong engagement |
| Suspiciously low | Any | Any | Check placement breakdown for Audience Network spam clicks |

---

## 5. Frequency — When to Worry, When to Ignore

Frequency is not inherently bad. Context determines whether it is a problem.

### Cold Audiences
Let cold frequency run to **2.5–3.0** before refreshing creative. Today it takes 5–10 touch points before someone truly understands what you are selling. Those touch points do not all have to be your ads — they happen through organic content, word of mouth, and general environment exposure.

### Retargeting Audiences
Retargeting frequency can go to **7+**. It is a repetition game. The goal is to stay top of mind until the person is ready to buy.

### Seasonal Exception (BFCM)
During Black Friday / Cyber Monday, higher frequency is intentional and desirable. Consumers are in active buying mode and comparing offers. Elevated frequency keeps the brand visible. Looser exclusions are acceptable during this period.

### Frequency as a Diagnostic Tool
- Frequency rising + CTR dropping + CPM rising = **Creative fatigue** (same people, ignoring the ad)
- Frequency rising + CTR flat + CPM flat = **Structural fragmentation** (too many ad sets, not enough exclusions)
- Frequency low (< 1.5) + CPP spiking = **NOT a fatigue issue** — look elsewhere (audience exhaustion, placement shift, attribution)

---

## 6. Hook Rate & Hold Rate — Video Ad Diagnostics

### Hook Rate (3-Second View Rate)
The percentage of people who watch at least 3 seconds of a video ad. Measures whether the opening stops the scroll.

- A high hook rate with poor CPP = the ad is stopping people but not converting them. The problem is in the body of the ad or on the landing page, not the hook.

### Hold Rate (15-Second View Rate)
The percentage of people who watch at least 15 seconds. Measures whether the content sustains attention past the hook.

- Track average play time and where people drop off. A sharp drop-off at a specific timestamp points to a weak argument, a confusing transition, or a boring section.

### The Full Video Diagnostic Sequence
1. Hook Rate (3s) — Is the opening stopping the scroll?
2. Hold Rate (15s) — Is the content sustaining attention?
3. Average Play Time — How far through the ad are people getting?
4. CTR(All) — Are people engaging with the content?
5. Link CTR — Are people clicking through with intent?
6. LPV → IC Rate — Are the people who click actually buying?

---

## 7. CPC + CVR — The Trust Gap

**Low CPC + Poor CVR = Curiosity without belief.**

The ad created enough interest to generate a cheap click, but did not install enough trust or proof to convert the visitor. This is the most common misdiagnosis in direct-response accounts — advertisers blame the landing page when the real problem is the ad did not do enough selling before the click.

### The Ad-to-Page Congruency Check
The conversion rate is a function of the ad AND the page in combination, not just the page. Ask:
- Is the message in the winning ad reflected on the landing page? If the ad focuses on a specific pain point but the landing page is generic, there is a disconnect.
- High-intent/direct ads ("Buy this thing") → Higher CPC, Higher CVR
- High-curiosity/indirect ads ("Watch this training") → Lower CPC, Lower CVR

Both can produce strong Cost Per Result, but they require different landing page experiences.

---

## 8. The Harvest vs. Plant Audit

When ROAS looks strong but CPMr is rising, run this audit to check if the account is in a Harvest loop.

**Step 1:** Pull the top 10 ads by spend over the last 30 days.
**Step 2:** Add CPMr and Reach columns.
**Step 3:** Sort by ROAS (highest to lowest).

**Red flag:** If your highest-ROAS ads also have the highest CPMr and the lowest Reach, the algorithm is harvesting warm audiences and claiming credit for conversions that were already going to happen. The account looks healthy but is slowly consuming its own audience pool.

**The fix:** Introduce Plant Intent creative — ads designed to reach cold, unaware audiences who have never heard of the brand. These will have lower ROAS but higher Reach and lower CPMr. They feed next month's warm audience pool.
