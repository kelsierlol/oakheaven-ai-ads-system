# Funnel KPIs, Baselines & Spend Allocation

## Table of Contents
1. [The "Metrics Are Relative" Principle](#1-the-metrics-are-relative-principle)
2. [Baseline Expectations by Funnel Type](#2-baseline-expectations-by-funnel-type)
3. [Lead Gen Funnel — Full Metric Stack](#3-lead-gen-funnel--full-metric-stack)
4. [Spend Allocation Diagnostics](#4-spend-allocation-diagnostics)
5. [Triangulation Rule](#5-triangulation-rule)

---

## 1. The "Metrics Are Relative" Principle

A metric that looks good in isolation can be a primary indicator of a problem. Always evaluate metrics against the specific funnel type, audience, and offer before concluding whether a number is healthy or a red flag.

**Example:** A $2 CPC might seem excellent, but for a high-end B2B audience targeting enterprise decision-makers, it is suspiciously low. High-intent B2B buyers are expensive to reach. A $2 CPC almost certainly means the ad is being served to the wrong audience (Audience Network spam, wrong demographics) rather than genuine buyers.

**Example:** A 50%+ hook rate with 12% CTR sounds like a winning ad. But if average time on landing page is under 10 seconds, the ad is generating curiosity clicks with no purchase intent. The ad is creating interest but not installing enough belief.

---

## 2. Baseline Expectations by Funnel Type

### B2B Cold Funnel (High-End / Enterprise)
- **Target audience:** Directors of Sales, VPs, C-suite, enterprise decision-makers
- **Expected CPC:** $1.00 – $3.00
- **Red flag:** CPC below $1.00 → immediately check placement breakdown for Audience Network spam
- **Key diagnostic:** Zero conversions + low CPC = traffic quality issue, not landing page issue. Verify with firmographic data (e.g., Rb2b) before touching the page.

### Webinar Funnel (Biz Op / Make Money Online)
- **Target audience:** People looking to start a business, side hustle, make money online
- **Expected CPC:** $2.00 – $8.00
- **Expected Registration CVR:** 20–40%

### Webinar Funnel (Coaching / Consulting)
- **Target audience:** Existing business owners, professionals seeking coaching
- **Expected CPC:** $5.00 – $10.00
- **Expected Registration CVR:** 15–30%

### Direct Purchase / Low-Ticket Offer (LTO)
- **Target audience:** B2C buyers ($20–$100 products)
- **Front-End ROAS target:** 0.8x – 1.0x (goal is customer acquisition for backend upsell, not immediate profit)
- **CPA benchmark:** Should be roughly equal to or slightly above AOV
- **Key diagnostic:** If Front-End ROAS is 0.9x but zero backend upsells or calls are booking, the bottleneck is post-purchase, not the ads

### Subscription App / Low-Ticket Subscription
- **Target audience:** B2C, typically broad interest targeting
- **Front-End ROAS target:** 0.7x – 1.0x
- **Key metrics:** CPP, LTV/CAC ratio, subscriber retention rate
- **Key diagnostic:** CPP is the primary metric. LPV→IC and IC→Purchase rates are the funnel stages to monitor for drop-off.

### Lead Gen / Call Booking (High-Ticket)
- **Target audience:** Qualified prospects for high-ticket offers ($3,000+)
- **See Section 3 for full metric stack**

---

## 3. Lead Gen Funnel — Full Metric Stack

For lead gen accounts, the analysis must extend beyond Meta's dashboard into sales data. The full funnel is:

| Stage | Metric | What "Bad" Looks Like |
|---|---|---|
| Ad → Click | CPC | Too high = bad creative or wrong audience |
| Click → LPV | Click-to-LPV Rate | <80% = page speed or tracking issue |
| LPV → Form Start | Page CVR | Low = weak headline, no proof above fold, bad mobile |
| Form Start → Form Submit | Form Completion Rate | Low = too many fields, confusing questions, tech issue |
| Form Submit → Call Booked | Booking Rate | Low = weak confirmation page, no urgency |
| Call Booked → Show | Show Rate | Low = wrong audience, weak pre-call sequence, low intent |
| Show → Close | Close Rate | Low = sales team issue, wrong ICP, objection handling |
| Close → Cash Collected | Cash Collected % | Low = payment plan issues, payment processor friction |

**When the bottleneck is in sales (not ads):**
If show rate is low, ask: Is the confirmation page clear? Is the pre-call email/SMS sequence strong? Are the leads the right ICP?
If close rate is low, ask: Are calls being recorded? What are the common objections? Is the offer framed correctly? Is the sales team trained?

**Important:** If leads are quality (right ICP, financially qualified) but close rate is 0%, this is a sales process issue — not an ads issue. Keep the ads running and fix the sales process.

---

## 4. Spend Allocation Diagnostics

Spend allocation analysis is a critical part of any bottleneck investigation. Even if the creative is strong, poor spend allocation can kill performance.

### Signs of Bad Spend Allocation

**Too many ad sets (fragmentation):**
- 20+ active ad sets on a $5,000–$10,000/day budget means each ad set gets ~$250–$500/day
- At a $150 CPP, that is 1–3 purchases per ad set per day — far below the 50 purchases/week threshold needed to exit the learning phase
- The algorithm stays in learning phase permanently, paying a "learning tax" on every result

**CBO budget concentration on wrong ad sets:**
- The CBO algorithm will often concentrate budget on the newest ad sets or the ones with the most recent engagement signal, even if they have no purchase history
- Check: which ad sets received the most spend in the crisis period? Are they proven converters or new launches?

**Scaling campaign cannibalising testing campaign:**
- If a scaling campaign and a testing campaign are targeting the same broad audience simultaneously, they compete in the same auctions, driving up CPM for both
- The scaling campaign (with higher budget) will usually win, starving the testing campaign of spend

### Healthy Spend Allocation Benchmarks
- **Testing campaign:** 8–12 active ad sets maximum. Each ad set should receive enough daily budget to generate 4–6 purchases per day (i.e., daily budget per ad set = 4–6 × target CPP)
- **Scaling campaign:** 3–5 proven winners maximum. Budget concentrated on the top performers.
- **Warm/retargeting campaigns:** Separate campaign, separate budget. Do not mix cold and warm ad sets in the same CBO.

---

## 5. Triangulation Rule

Never make a definitive conclusion based on a single data point. Always use multiple data points to corroborate the same narrative.

**Two data points minimum.** In some cases you will only have access to one data source — acknowledge this limitation and note what additional data would confirm or refute the hypothesis.

**Examples of triangulation:**
- Meta CPP spike + third-party CAC flat → attribution issue (not real performance decline)
- Meta CPP spike + third-party CAC also spiked → real performance decline
- High frequency + CTR dropping + CPM rising → creative fatigue confirmed
- High frequency + CTR flat + CPM flat → structural fragmentation (not fatigue)
- Low CPC + zero conversions + Audience Network = 80% of clicks → traffic quality issue confirmed
- Low CPC + zero conversions + Audience Network = 20% of clicks → landing page or offer issue
