# Step 14 — Lock In Your KPIs

**Time:** 15 min
**Goal:** Calculate your unit economics. Know exactly what you can afford to pay for a customer, your break-even ROAS, and how much you can scale before you're unprofitable.

---

## Why This Matters

Without these numbers, you're flying blind. You don't know if your current CPR is good or bad. You don't know when to scale. You don't know when you're about to run into a wall.

Most agencies and info businesses don't do this. It's why they plateau.

---

## What You'll Calculate

| Metric | What It Tells You |
|--------|-------------------|
| Gross profit per customer | Revenue minus what it costs to deliver |
| Max allowable CAC | The most you can pay to acquire a customer and still hit target margin |
| Max allowable CPL | Max CAC ÷ sales close rate (if you have a call funnel) |
| Target ROAS | Revenue ÷ Max CAC |
| Break-even ROAS | Revenue ÷ Gross profit (the ROAS where you make $0) |

These become the benchmarks in your `context/ad-account.md`.

---

## What You Need Before Running

Pull these numbers:

- **Revenue per customer** — average order value, subscription value, or LTV (if tracked)
- **Fulfilment cost per customer** — COGS, team time, software costs, etc.
- **Monthly overhead** — fixed costs that don't change with customer count
- **Current ad spend**
- **Current conversion metrics** — CPR, close rate if applicable

Rough numbers are fine. Round to the nearest 10%.

---

## The Prompt

Paste this into Claude:

```
Run the KPI Tracker skill (skills/kpi-tracker/SKILL.md).

Interview me about my unit economics. Cover:
1. Revenue per customer (average, or LTV if tracked)
2. Fulfilment cost per customer
3. Monthly overhead
4. Current ad spend
5. Current CPR and ROAS
6. Sales close rate (if call funnel)
7. Target profit margin (default 30% if I'm not sure)

Calculate:
- Gross profit per customer
- Max allowable CAC
- Max allowable CPL
- Target ROAS
- Break-even ROAS

Run 3 scenarios:
- Conservative (current performance)
- Moderate (10% CPR improvement)
- Aggressive (scale spend 2x at current CPR)

Include a stress test — what if CPR goes up 20%?

Answer:
1. Am I profitable right now?
2. What's my break-even CPR?
3. How much can I scale before I'm unprofitable?
4. If CPR increases by X%, am I still profitable?
5. What CPR improvement would I need to hit $X profit/month?

Save the benchmarks to context/ad-account.md (max CAC, target ROAS,
break-even ROAS, kill criteria, scale criteria).
```

---

## What To Do With The Output

### If You're Unprofitable

Don't panic. The model shows you the exact lever to move. Usually it's one of:

- **CPR is too high** → Need better creative (back to Script Generator)
- **Close rate is too low** → Need better sales process or better leads
- **Revenue per customer is too low** → Need higher-ticket offer or upsell
- **Overhead is too high** → Cut costs before scaling

Pick the biggest lever. Work on it.

### If You're Profitable

Now you know how much you can scale. The model tells you your headroom. Use it.

**Rule:** Don't scale past your maximum allowable CAC. It feels good short-term but kills margin. If you want to scale past that number, you need to first:
- Raise your prices, or
- Lower your delivery cost, or
- Improve your CPR

---

## The Stress Test Matters Most

Your CPR will go up. It always does. New platforms change, competitors enter, audiences fatigue.

The question isn't "am I profitable today?" — it's "do I still make money if my CPR goes up 20-30%?"

If your answer is no, you're one bad week away from unprofitable. Fix the underlying economics before scaling.

---

## Save The Benchmarks

Claude will write the final numbers to `context/ad-account.md`. These become the reference point for every future bottleneck analysis.

When Claude runs a bottleneck analysis, it'll compare your actual CPR to your target CPR from this file. Without these benchmarks, the analysis is generic. With them, it's dialed in.

---

## ✅ Checkpoint

- [ ] KPI Tracker skill ran end-to-end
- [ ] Gross profit per customer calculated
- [ ] Max allowable CAC and CPL calculated
- [ ] Break-even ROAS calculated
- [ ] 3 scenarios modeled (conservative, moderate, aggressive)
- [ ] Stress test complete (CPR +20%)
- [ ] Benchmarks saved to `context/ad-account.md`
- [ ] You know if you're profitable and how much headroom you have

Move to **Step 15 — Build A Custom Skill**.
