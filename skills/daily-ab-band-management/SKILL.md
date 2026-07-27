---
name: daily-ab-band-management
description: The surgical daily workflow for managing ABO testing campaigns using budget bands. Takes your daily Ads Manager export and tells you exactly which ad sets to kill, which to promote up a band, which to drop down a band, and which to leave alone. Use this every morning once your campaign structure is built via the ads-setup-engine skill. Supplements (does not replace) the broader Daily Media Buyer Check-in skill. Triggers on "run my daily bands", "daily band management", "what moves today", "daily ads review", or similar.
---

# Daily A/B Band Management

Your daily 3-minute ritual. Takes your Ads Manager export + the band structure from `outputs/campaign-structure.md` and produces a kill/promote/drop action list for the day.

This is surgical — it only does band management on ABO testing campaigns. For broader funnel diagnosis, audience issues, creative fatigue signals beyond budget bands, or weekly rhythm analysis, use the Daily Media Buyer Check-in or Bottleneck Analysis skills instead.

---

## Prerequisites

1. `outputs/campaign-structure.md` exists (run `ads-setup-engine` first)
2. You have your 3-day rolling Ads Manager export ready
3. You know what changes you made yesterday (for the Date Last Edited check)

If `campaign-structure.md` doesn't exist:

> "Run the `ads-setup-engine` skill first. Without your custom bands, I can't tell you what moves to make."

---

## Inputs

Ask the user:

> "Paste your Ads Manager export. I need these columns for each ad set:
> - Ad Set Name
> - Budget (Daily)
> - Amount Spent (3-day lookback)
> - Results
> - Cost Per Result
> - Date Last Edited
>
> You can paste as CSV or copy/paste the table directly. If you don't have 'Date Last Edited' in your columns, add it to your Performance Analytics view before running this."

Wait for the paste.

---

## Process

### Step 1: Read Your Band Structure

Load `outputs/campaign-structure.md` and extract:
- Target CPR
- Account average CPR
- All 8 band dollar amounts
- Kill rules
- Scale rules

### Step 2: Classify Every Ad Set

For each ad set in the export, determine its current state:

| State | Condition |
|-------|-----------|
| **Testing — No Results** | Impressions > 0, Results = 0 |
| **Testing — 1 Result** | Results = 1 |
| **Scaling** | Results ≥ 2 |
| **Cold** | No impressions (ignore for now) |

Then classify its performance vs account average CPR into Tier A/B/C/D/E:

- Tier A: CPR ≤ 60% of account avg (top performer)
- Tier B: CPR 60-100% of account avg (above average)
- Tier C: CPR 100-140% of account avg (at average)
- Tier D: CPR 140-170% of account avg (below average)
- Tier E: CPR > 170% of account avg OR spend > 2× target CPR with ≤ 1 result (fail)

### Step 3: Check "Date Last Edited"

For any ad set edited today already, lock it. Do not suggest another move for it.

> **Rule: One band change per ad set per day, maximum.**

### Step 4: Apply Kill / Drop / Promote Rules

For each ad set (skipping today-locked ones):

**KILL immediately if:**
- No Results AND spend ≥ 1× target CPR in 3-day window
- 1 Result AND spend ≥ 2× target CPR in 3-day window
- At Band 1 ($50/day) with zero improvement for 14+ days (check Date Last Edited history)

**DROP one band if:**
- 2+ Results AND CPR in Tier E
- CPR degraded 2 bands in a single day's data (override the "one-change" rule for clear breaks)

**PROMOTE one band if:**
- Performance is at the next band's threshold for 3+ consecutive days
- Ad set has earned the upgrade per the scale rules

**PROMOTE to Band 8 directly if:**
- 2+ Results AND Tier A (top performer) for 3+ consecutive days
- Currently below Band 8

**HOLD (no change) if:**
- Just launched (< 3 days live) — give Meta time to optimize
- Within normal variance of current band
- Edited today already
- At Band 8 cap

### Step 5: Output The Daily Action List

Structure the output like this:

```markdown
# Daily Band Management — [Date]

**Lookback:** 3-day rolling
**Current Account Avg CPR:** $[X] | **Target CPR:** $[Y]
**Ad Sets Reviewed:** [N] | **Locked (edited today):** [N]

---

## 🔴 KILL (N ad sets)

Turn these off now. Reason listed for each.

- `[Ad Set Name]` — $[spend] spent, [results] results, CPR $[X]. Reason: [killed rule]
- `[Ad Set Name]` — ...

## 🔽 DROP ONE BAND (N ad sets)

Reduce budget to the next lower band. Don't kill yet.

- `[Ad Set Name]` — currently Band [X] at $[current], drop to Band [X-1] at $[new]. Reason: [why]

## 🔼 PROMOTE ONE BAND (N ad sets)

Raise budget to next band.

- `[Ad Set Name]` — currently Band [X] at $[current], promote to Band [X+1] at $[new]. Reason: [why]

## 🚀 PROMOTE TO BAND 8 (N ad sets)

Top performer — send straight to scaling tier.

- `[Ad Set Name]` — CPR $[X] (Tier A) for [N] days. Promote from Band [X] to Band 8 at $[new].

## ⏸ HOLD — NO CHANGE (N ad sets)

No action needed today.

- `[Ad Set Name]` — [reason: launched <3 days / edited today / within variance / at Band 8 cap]

---

## Summary

- Ad sets killed: [N]
- Band changes made: [N up, N down]
- Total daily spend before changes: $[X]
- Estimated daily spend after changes: $[Y]
- Flags: [anything unusual — all ad sets fatiguing, big shift in account average, etc.]

## Notes

[Any patterns worth watching — e.g., "All P1 personas underperforming this week. Consider a creative refresh for persona 1 before next week."]

[If any action list is empty, say so — "No kills today. Everything is within band tolerance."]
```

### Step 6: Timer Challenge

End the output with:

> "This list should take you under 3 minutes to apply in Ads Manager. Timer starts when you open Meta."

---

## Edge Cases

**If the export has fewer than 5 ad sets:**
> "Your campaign is too small for meaningful band management. Focus on launching more concepts before optimizing. Come back when you have 10+ ad sets running."

**If no ad sets have results:**
> "No results in the 3-day window. Either the campaign is fresh (< 48 hours) or there's a delivery problem. Check: are your ads active? Is your pixel firing? Is your audience too narrow?"

**If account average CPR has shifted 20%+ from what's in `campaign-structure.md`:**
> "Your account average CPR has shifted significantly. The bands may be stale. I recommend re-running the `ads-setup-engine` skill to recalibrate. I'll still produce today's moves using the current bands, but flag this."

**If more than 30% of ad sets are in Tier E (failing):**
> "30%+ of your ad sets are failing. This isn't a budget management problem — it's a creative or audience problem. Don't just kill ads today. Run the Bottleneck Analysis skill this week to find the root cause."

---

## Constraints

1. **Never suggest multi-band moves.** One band at a time per ad set per day, except for the explicit "drop 2 bands in a day" exception.
2. **Never override 'Date Last Edited' locks.** If they moved an ad today, don't recommend touching it again.
3. **Never kill an ad set that's spent less than 1× target CPR.** Let it cook.
4. **Never suggest a band change without a specific reason from the rules.** No vibes-based promotions.
5. **Always flag patterns.** If 5 ad sets are being killed and all are from one persona, call it out — that's a creative issue, not a budget issue.
6. **Keep the output fast to read.** The point is 3-minute daily execution. Don't bury actions in paragraphs.
