---
name: kpi-tracker
description: Use this skill for financial modelling, KPI tracking, and performance reporting. Triggers include any mention of "KPI tracking", "financial model", "unit economics", "what should my CPR be", "am I profitable", "break even analysis", "how much can I spend", "ad spend calculator", or any request to model ad performance against business metrics.
---

# KPI Tracker & Financial Modelling

Models your ad performance against your real business economics so you know exactly what a profitable customer acquisition cost looks like, how much you can spend, and whether your current performance is on track.

## When To Use This Skill

- Setting up KPI targets for the first time
- Monthly/quarterly review of whether ad spend is profitable
- Before scaling: "can I afford to spend more?"
- When CPR changes and you need to know if it's still profitable
- When offer pricing or conversion rates change

## What You Need Before Starting

1. **Revenue per customer** — What does one customer pay you? (Include: average order value, subscription value, lifetime value if known)
2. **Fulfilment cost per customer** — What does it cost you to deliver to one customer? (Include: COGS, team time, software, etc.)
3. **Monthly overhead** — Fixed costs that don't change with customer count (rent, salaries, tools, subscriptions)
4. **Current ad spend** — How much you're spending per month on ads
5. **Current conversion metrics** — From `context/ad-account.md`: CPR, ROAS, conversion rate, average CPM, CTR
6. **Sales conversion rate** (if applicable) — If leads book calls, what % close?

## Process

### Step 1: Calculate Unit Economics

```
Revenue per customer:           $[X]
- Fulfilment cost per customer: $[Y]
= Gross profit per customer:    $[X - Y]

Gross margin: [Gross profit / Revenue] × 100 = [Z]%
```

### Step 2: Calculate Maximum Allowable CAC

```
Gross profit per customer:      $[X - Y]
× Target profit margin:         [e.g., 30%]
= Target profit per customer:   $[A]

Maximum allowable CAC:          $[Gross profit - Target profit] = $[B]
```

This is the most you can pay to acquire a customer and still hit your target profit margin. Your CPR should be at or below this number.

If you have a sales team / call funnel:
```
Maximum allowable CAC:          $[B]
÷ Sales close rate:             [e.g., 20%]
= Maximum allowable CPL:        $[B ÷ close rate]
```

### Step 3: Set Performance Benchmarks

Using the maximum allowable CAC/CPL, set benchmarks:

| Metric | Target | How Calculated |
|--------|--------|---------------|
| Max CAC | $[B] | Gross profit × (1 - target margin) |
| Max CPL (if calls) | $[B ÷ close rate] | Max CAC ÷ close rate |
| Target ROAS | [Revenue ÷ Max CAC] | Minimum ROAS to be profitable |
| Break-even ROAS | [Revenue ÷ Gross profit] | ROAS where you make $0 profit |

### Step 4: Model Scenarios

Run three scenarios:

**Conservative (current performance):**
```
Monthly spend:     $[current]
CPR:               $[current]
Customers/month:   [spend ÷ CPR]
Revenue:           [customers × revenue per customer]
Gross profit:      [customers × gross profit per customer]
Ad spend:          -$[current]
Net profit:        [gross profit - ad spend - overhead allocation]
ROAS:              [revenue ÷ spend]
```

**Moderate (10% CPR improvement):**
```
[Same structure with improved CPR]
```

**Aggressive (scale to $X/day):**
```
[Same structure with higher spend, assuming CPR holds]
```

### Step 5: Answer Key Questions

Based on the model, answer:

1. **Am I profitable right now?** — Yes/No + by how much per customer
2. **What's my break-even CPR?** — The CPR where I make $0 profit
3. **How much can I scale before I'm unprofitable?** — Maximum daily/monthly spend at current CPR
4. **If CPR increases by X%, am I still profitable?** — Stress test
5. **What CPR improvement would I need to hit $X profit/month?** — Reverse engineer the target

### Step 6: Update Benchmarks

Save the calculated benchmarks to `context/ad-account.md`:
- Target CPR
- Target ROAS
- Break-even ROAS
- Maximum allowable CAC
- Kill criteria (CPR above which to turn off ads)
- Scale criteria (CPR below which to increase spend)

## Output Format

```
# KPI & FINANCIAL MODEL — [Business Name]

## Unit Economics
Revenue per customer:           $X
Fulfilment cost:                $Y
Gross profit:                   $Z
Gross margin:                   Z%

## Acquisition Targets
Maximum allowable CAC:          $A
Maximum allowable CPL:          $B (if call funnel)
Target ROAS:                    Cx
Break-even ROAS:                Dx

## Scenario Models
[Conservative / Moderate / Aggressive tables]

## Key Answers
1. Profitable: [Yes/No — detail]
2. Break-even CPR: $X
3. Max scale: $X/month at current CPR
4. Stress test: [CPR increase tolerance]
5. Target CPR for $X profit: $Y

## Recommended Benchmarks (for ad-account.md)
[Table of metrics and targets]
```

## Constraints

1. Never assume lifetime value unless the client provides retention data. Use single-transaction revenue by default.
2. Always show the math. Every number must be traceable to an input.
3. Always present break-even alongside target — knowing where you start losing money is as important as knowing the ideal.
4. If any input is missing, flag it and use a conservative assumption. State the assumption clearly.
5. Scenarios must include a stress test (what if CPR goes up 20-30%). Optimistic-only modelling is dangerous.
