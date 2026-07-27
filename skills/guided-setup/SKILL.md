---
name: guided-setup
description: Interactive, end-to-end FOUNDATIONS setup. Runs a phase-based walkthrough that fills in context files, loads data, runs creative strategy, generates scripts, and locks in KPIs. This is Phase 1 of client onboarding — produces the foundation. Phase 2 (strategic 30/60/90 plan) is handled by the ads-plan-generator skill, and Phase 3 (operational Media Buying SOP) by the media-buying-sop-generator skill. Use this skill when the user says "guided setup", "run the setup", "walk me through setup", "onboard me", "get me started", or pastes the master onboarding prompt. Resumes from memory/open-loops.md if a previous run was interrupted.
---

# Guided Setup — Foundations

Runs the FOUNDATIONS onboarding inside Claude. Takes a brand new workspace from zero to a fully loaded system with personas, scripts, and locked-in KPIs.

**This skill produces the foundation.** Strategic plan is handled by the `ads-plan-generator` skill after this completes; the operational Media Buying SOP is handled by the `media-buying-sop-generator` skill.

## Core Principles

1. **One question at a time.** Do not present lists of questions. Wait for the full response before moving to the next.
2. **Save progress every phase.** Write a snapshot to `memory/open-loops.md` at the end of each phase. If the session is interrupted, resume by reading this file first.
3. **Explicit checkpoints.** At the end of each phase, stop and confirm before proceeding. Never race through.
4. **Never skip hard gates.** If the user can't provide required data (5+ sales calls, etc.), pause the flow, tell them exactly what to go get, and offer to resume when ready.
5. **Challenge vague answers.** If the user gives a generic response, push back. Specificity is the whole point.
6. **Write files, don't just talk.** Every phase produces an artifact.

---

## Phase 0: Resume Check

Read `memory/open-loops.md`. If a previous guided setup is logged with a checkpoint, skip to that phase and tell the user:

> "I can see we got to [Phase X]. Resuming from there. If you'd rather restart from the top, say 'restart setup'."

If no previous session, continue to Phase 1.

---

## Phase 1: Filing System Verification (2 min)

Check every file:
- `CLAUDE.md` at root
- `context/business.md`, `ad-account.md`, `glossary.md`
- `skills/` folder with all 16 skills + 3 reference docs (hook-formulas, ad-formats-library, creative-strategy-reference) + reference folders (bottleneck-analysis-references, daily-checkin-references, lead-quality-report)
- `knowledge-base/sales-calls/`, `winning-ads/`, `research/`
- `outputs/` and `memory/open-loops.md`

Report what's present, what's missing. If anything is missing, stop.

If complete:

> "Filing system verified. I'll walk you through the full foundations setup. You can pause any time by saying 'pause'."

Save checkpoint:
```
## Guided Setup — Foundations — In Progress
Phase 1 complete (filing verified). Next: Phase 2 (business context).
```

---

## Phase 2: Business Context Interview (15 min)

> "Phase 2. Your business context. 8 questions, one at a time. Be specific — vague answers produce vague ads."

Ask ONE AT A TIME:

**Q1 — Offer:** "What exactly do you sell? Include what the customer gets, pricing, and how they pay."

**Q2 — Unique Mechanism:** "What makes your approach different from every competitor? The how, not the what."

**Q3 — ICP:** "Describe your ideal customer. Demographics, situation, what triggered them to look for a solution."

**Q4 — Personas:** "Within your ICP, are there distinct persona types? Who are the 2-4 different kinds of customer you serve?"

**Q5 — Voice & Tone:** "How does your brand sound? Casual, professional, funny, direct? Give me an example of writing you like."

**Q6 — Competitive Positioning:** "Top 3 competitors and how you're different from each."

**Q7 — Proof Assets:** "Your best 5 proof points — testimonials, case studies, revenue numbers."

**Q8 — Known Objections:** "Top 3-5 reasons people don't buy on sales calls."

Push back on vague answers. Write `context/business.md`. Show the draft. Iterate until approved. Save checkpoint.

---

## Phase 3: Ad Account Context Interview (10 min)

> "Phase 3. Your ad account. 11 questions. If you don't know a number, say so — we'll fix it in the KPI phase."

Ask ONE AT A TIME:

**Q1 — Platform:** Meta, Google, both?
**Q2 — Current monthly spend**
**Q3 — Current CPR**
**Q4 — Target CPR**
**Q5 — Current ROAS**
**Q6 — Target ROAS**
**Q7 — Conversion event** — lead / call booked / sale?
**Q8 — Attribution window** — 1DC, 7DC, etc.
**Q9 — Kill criteria** — current rule for turning off ads
**Q10 — Scale criteria** — rule for increasing budget
**Q11 — Account history** — 2-3 sentences on what's worked, failed, current status

Write `context/ad-account.md`. Iterate. Save checkpoint.

---

## Phase 4: Glossary (5 min)

> "Short one. Your shorthand — product names, internal terms, acronyms."

Ask: product/offer terms, customer terms, any business abbreviations.

Write `context/glossary.md`. Save checkpoint.

---

## Phase 5: Data Loading & Readiness Checkpoint (10 min + their upload time)

**This is the most important phase. It is a HARD CHECKPOINT — do not proceed to Phase 6 until readiness is verified.**

Before asking the user to upload anything, run this check:

> "Phase 5 is where most setups fail. The quality of everything downstream depends on what you load here. Before we continue, I need to verify you have the assets to run this workspace at the level it's designed for.
>
> Have you completed the Asset Inventory (Pre-Flight Checklist) from Step 04 of the course? If not, stop. Go do it now — it takes 30 minutes and saves 20+ hours of bad outputs.
>
> If you have — what did you score on each of the 8 categories? Tell me R/Y/G for each:
>
> 1. Voice of Customer Data
> 2. Business Fundamentals
> 3. Ad Account Data
> 4. Market Intelligence
> 5. Performance History
> 6. Tracking Infrastructure
> 7. Creative Production Assets
> 8. Team & Capacity"

Based on the user's answer, apply these rules:

- **Any RED in categories 1, 2, or 8** — STOP. Do not proceed. Tell them:
  > "I can't run a reliable setup without [category]. Fix the gap first, then come back. Say 'resume guided setup' when you're ready."

- **Any RED in categories 3, 4, 5, or 6** — Flag loudly but allow to continue:
  > "You're RED on [category]. We can proceed, but I'll flag this as a known weakness and outputs may be thinner in [specific area]. Acknowledged?"

- **All YELLOW or GREEN** — Proceed:
  > "Good. Let's load the data."

Once readiness is confirmed, walk through each upload:

### 5.1 Sales Calls
> "Export your diverse sales call transcripts to `knowledge-base/sales-calls/`. Mix of wins AND losses. Minimum 5 — but based on your readiness score, aim for 20. Tell me when done."

After they confirm, read the folder. Count files. Assess diversity by filename pattern. If fewer than 5, do not proceed:

> "I see [N] files. The creative strategy skill needs at least 5 diverse transcripts to produce reliable personas. Go get more. Say 'resume' when you have at least 5."

### 5.2 Winning Ads
> "Drop text of your best performers into `knowledge-base/winning-ads/`. Script text only, not links. If you're a new account with no winners, create `NEW-ACCOUNT.md` with a note — the system will lean on competitor references instead."

Verify folder. If Performance History was rated GREEN, expect 3-5 files. If YELLOW, accept 1-2. If RED, verify the NEW-ACCOUNT.md note is there.

### 5.3 Proof
> "Testimonials, case studies, results → `knowledge-base/research/proof/`. Text form — not screenshots."

Verify at least one file exists. If empty AND they said they have proof, push back:

> "You said you have proof assets. Nothing's in the folder. Go drop them in before we continue."

### 5.4 Competitors
> "facebook.com/ads/library. Top 3-5 competitors. For each, document angles, formats, hooks, offer, positioning → `knowledge-base/research/competitors/`."

Verify at least 3 competitor files. If fewer:

> "Creative strategy is much weaker without competitor context. Spend 45 min and do 3 more before we proceed."

### Final Readiness Gate

After all four sub-phases, run a final check:

```
READINESS GATE

Sales calls: [N] files ✓/✗
Winning ads: [N] files or NEW-ACCOUNT note ✓/✗
Proof: [N] files ✓/✗
Competitors: [N] files ✓/✗

Business context: filled ✓/✗
Ad account context: filled ✓/✗
Glossary: filled ✓/✗

Result: READY / NOT READY
```

If NOT READY, stop and tell them exactly what's missing. If READY, proceed to Phase 6 and save checkpoint.

---

## Phase 6: Creative Strategy (45 min)

> "The big one. Produces personas, scoring, micro personas, strategy map. 30-45 min with human checkpoints.
>
> First: what's your gut read? Which customer types do you think are the strongest opportunities and why?"

Treat thesis as hypothesis. Run the Creative Strategy skill (`skills/creative-strategy/SKILL.md`) end-to-end. Hit every checkpoint. Let user approve personas and micro personas before the strategy map.

Save to `outputs/creative-strategy-[date].md`. Save checkpoint.

---

## Phase 7: Script Generation (20 min)

> "Now we turn the strategy into ads. 5 storyboards, 3 hook variations each, QC'd."

Run Script Generator (`skills/script-generator/SKILL.md`). Pick 5 strongest combos. Run Script QC on every script. Save to `outputs/ad-scripts-[date].md`.

Walk through each script briefly. Accept revisions. Re-QC as needed. Save checkpoint.

---

## Phase 8: KPI Lock-in (15 min)

> "Now we lock in your unit economics."

Run KPI Tracker (`skills/kpi-tracker/SKILL.md`). Calculate max allowable CAC, break-even ROAS, target CPR. Run conservative/moderate/aggressive scenarios with 20% stress test.

Save benchmarks to `context/ad-account.md` (overwriting Phase 3 targets with calculated ones).

Save checkpoint.

---

## Phase 9: Foundations Wrap + Hand-off (5 min)

Write final foundations summary to `memory/open-loops.md`:

```
## Guided Setup — Foundations — COMPLETE
Date: [date]
Artifacts produced:
- context/business.md (filled)
- context/ad-account.md (filled, benchmarks locked)
- context/glossary.md (filled)
- knowledge-base/ populated ([N] sales calls, [N] winning ads, [N] competitors, proof assets)
- outputs/creative-strategy-[date].md
- outputs/ad-scripts-[date].md

Next:
- Run Ads Plan Generator (skills/ads-plan-and-sops/SKILL.md) to produce the 30/60/90 day plan
- Then run Media Buying SOP Generator (skills/media-buying-sop-generator/SKILL.md) to produce the operational playbook
```

Tell the user:

> "Foundations complete. You have:
>
> - Filled-in context files (business, ad account, glossary)
> - A fully populated knowledge base
> - A complete Creative Strategy Brief with personas, scoring, strategy map
> - 5 QC'd ad scripts ready to record
> - Locked-in KPIs and benchmarks
>
> **Next steps:** I'll now build your strategic 30/60/90 day plan, then your operational Media Buying SOP. Two separate skills, run in sequence.
>
> Total time: ~40-50 minutes. Ready to continue, or do you want to pause here?
>
> If yes: I'll run the ads-plan-generator skill now, then offer the media-buying-sop-generator after.
> If pause: Say 'resume plan' when you come back."

If the user confirms, trigger the `ads-plan-generator` skill (file: `skills/ads-plan-and-sops/SKILL.md`) automatically and run it end-to-end. At the end of that skill it will prompt the user to also run `media-buying-sop-generator` — let that flow naturally.

If the user pauses, save checkpoint:
```
## Guided Setup — Foundations Complete, Plan Pending
User paused before ads-plan-generator phase.
Next: When user says "resume plan" or similar, trigger skills/ads-plan-and-sops/SKILL.md.
```

---

## Handling Interruptions

At any phase, if the user says "pause", "stop", "let's come back later":

1. Write current phase + sub-phase to `memory/open-loops.md`
2. Tell the user: "Saved at [phase X]. Say 'resume guided setup' when you're back."

Phase 0 (Resume Check) catches this on re-entry.

---

## Constraints

1. Never skip hard gates (5+ sales calls minimum).
2. Never write context files with generic filler.
3. Never race. One phase at a time, checkpoint between each.
4. Always one question at a time in interviews.
5. Always save progress after each phase.
6. This skill produces FOUNDATIONS only. For the strategic plan, hand off to `ads-plan-generator`. For the operational Media Buying SOP, hand off to `media-buying-sop-generator`.
