# Step 07 — Set Up Your Ad Account Context

**Time:** 10 min
**Goal:** Fill in `context/ad-account.md` with your current spend, benchmarks, and testing criteria.

---

## Why This Matters

Every time you run a bottleneck analysis, the skill references this file to compare your performance against your targets. Without this file, Claude doesn't know what "good" looks like for your account — it has to guess.

Your ad account context includes:
- Current monthly spend
- Target CPR, ROAS, CPM, CTR, etc.
- Kill criteria (when to turn off an ad)
- Scale criteria (when to increase budget)
- Attribution window
- Account history notes

---

## The Prompt

Paste this into Claude:

```
Interview me about my ad account so we can fill in context/ad-account.md.

Ask me one question at a time. Cover:

1. Platform(s) — Meta, Google, etc.
2. Current monthly spend — rough number is fine
3. Current CPR (cost per result / cost per lead)
4. Target CPR — what you're aiming for
5. Current ROAS — if tracked
6. Target ROAS — what you need for break-even and profit
7. Conversion event — what counts as a result (lead, call booked, sale)
8. Attribution window — 1-day click, 7-day click, etc.
9. Kill criteria — when do you turn off an ad?
10. Scale criteria — when do you increase spend on an ad?
11. Account history — what's worked and what hasn't

If I don't know a number, flag it as a gap and move on. Don't let me
skip kill/scale criteria — those matter.

When done, write the file to context/ad-account.md. Show me the draft
first.
```

---

## If You Don't Know Your Numbers

This is common. Most people running ads don't know their ROAS. That's a problem we'll fix in Step 12 (KPIs).

For now, give Claude what you do know. For what you don't:
- "I don't know my ROAS — flag it as a gap"
- "I don't have kill criteria yet — help me set some reasonable defaults based on my retainer size"

Claude will fill in what you know and flag the gaps. You'll fill the gaps after Step 12.

---

## One Thing To Watch For

**Kill criteria and scale criteria are where most people get stuck.** They run ads and never turn anything off, or they kill winners too fast. Good defaults:

- **Kill:** CPR is 2x your target after at least $X spend (where $X = 5-10% of your typical retainer value)
- **Scale:** CPR is below target for 3+ consecutive days with stable volume

If you don't have better numbers, use these.

---

## ✅ Checkpoint

- [ ] `context/ad-account.md` is filled in
- [ ] Monthly spend, CPR target, and ROAS target are set
- [ ] Kill and scale criteria are defined
- [ ] Gaps are flagged where you don't know a number
- [ ] File reads accurately for your account

Move to **Step 08 — Load Your Sales Calls**.
