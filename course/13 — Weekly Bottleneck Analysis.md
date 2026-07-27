# Step 13 — Weekly Bottleneck Analysis

**Time:** 15 min every Monday
**Goal:** Run the highest-leverage skill in the system. Diagnose exactly where your funnel is breaking and what to fix this week.

---

## Why This Is The Most Important Weekly Habit

Most ads get launched and ignored until something visibly breaks. By then, you've burned budget, lost momentum, and are reacting instead of steering.

Bottleneck Analysis inverts this. Every Monday, you look at last week's data in a structured way, identify the primary bottleneck, and act on it. You stop getting surprised. You start compounding.

---

## What You Need

Before running the skill, pull this data from Meta Ads Manager for the last 7 days:

- **Spend**
- **Impressions**
- **CPM**
- **CPC**
- **CTR (Link)**
- **Hook Rate** (3-sec views / impressions)
- **Hold Rate** (ThruPlay / 3-sec views)
- **Leads / Conversions**
- **Cost per Result (CPR)**
- **ROAS** (if tracked)

Break it down by campaign and by ad where possible. Export to CSV if easier.

---

## The Prompt

Paste this into Claude every Monday:

```
Run a bottleneck analysis on my ad data for the past 7 days.

Data:
[paste your numbers here — campaign-level and ad-level breakdown,
plus any sales data showing which leads closed]

Follow the Bottleneck Analysis skill (skills/bottleneck-analysis/SKILL.md).

Structure the output:
1. Executive summary — what's the primary bottleneck, biggest action item
2. Funnel diagnosis — stage by stage, numbers vs benchmarks
3. Campaign breakdown — status per ad (SCALE / WATCH / TEST / KILL /
   CREATIVE FATIGUE)
4. Recommendations — prioritized action list (Fix Now / Test This Week /
   Monitor / Strategic)
5. Creative gap analysis — what should the next batch of ads focus on?

Reference my benchmarks in context/ad-account.md. Don't just say
"CPR is high" — tell me WHICH stage of the funnel is causing it and
WHY.

Save the report to outputs/bottleneck-analysis-[date].md.
```

---

## The Funnel Stages (What Claude Diagnoses)

| Stage | Metric | If Below Target → |
|-------|--------|-------------------|
| 1. Impressions | CPM | Audience too narrow, creative fatigue, or platform competition |
| 2. Hook | Hook rate | Your hooks aren't stopping the scroll. Replace them. |
| 3. Hold | Hold rate | Body of ad loses them. Restructure. |
| 4. Click | CTR | CTA is weak OR offer isn't compelling as presented |
| 5. Landing | Landing page CR | Not an ad problem — fix the landing page |
| 6. Output | CPR / ROAS | Consequence of one of the above — not the cause |

**The rule:** the FIRST stage significantly off-target is your primary bottleneck. Fix that before touching anything downstream.

---

## The Status Categories

Every active ad gets one of these labels:

- **SCALE** — Below CPR target for 3+ days, stable/improving. Increase budget.
- **WATCH** — Within 20% of CPR target. Keep running, monitor daily.
- **TEST** — New ad, insufficient data. Don't touch yet.
- **KILL** — Above CPR target by >2x after sufficient spend. Turn off.
- **CREATIVE FATIGUE** — Was performing, now declining over 5+ days. Needs new creative.

---

## How To Use The Output

Claude will give you a prioritized action list. Work through it in order:

### Priority 1 — Fix Now
These are things that could cost you money this week. Do them today.

**Examples:**
- Kill ads that are 3x over CPR target
- Increase budget on clear winners
- Fix tracking that's broken

### Priority 2 — Test This Week
New creative to launch based on gaps identified.

**Example:** "We have no Unaware-level creative. Generate 2 Unaware-targeted scripts this week."

Feed this back into the Script Generator (Step 09).

### Priority 3 — Monitor
Things to watch but not act on yet. Usually new ads that need more data.

### Priority 4 — Strategic
Bigger changes for the next creative cycle — new angles, new personas, landing page changes.

---

## The Feedback Loop

This is the magic. Every bottleneck analysis feeds back into:

- **Creative Strategy** — "Persona 3 is underperforming. Re-evaluate."
- **Script Generator** — "We need more Unaware cold traffic scripts."
- **KPIs** — "Our CPR benchmark was too aggressive. Adjust target."

The system gets smarter every week.

---

## What To Do With The Report

Save it. Share it with your team. Actually take the actions.

Most people will read a great bottleneck analysis, nod along, and do nothing. Don't be that person. The analysis is worthless unless you act.

---

## ✅ Checkpoint

- [ ] You know what data to pull from Meta every Monday
- [ ] You've run your first bottleneck analysis
- [ ] You have a prioritized action list
- [ ] You've actioned Priority 1 items
- [ ] Report saved to `outputs/bottleneck-analysis-[date].md`

Move to **Step 14 — Lock In Your KPIs**.
