---
name: ads-plan-and-sops
description: Generates a strategic 30/60/90 day ads plan tailored to the user's account, KPIs, creative strategy, and growth targets. Use after the foundations setup is complete (Guided Setup). For the operational Media Buying SOP (budget brackets, kill/scale rules, daily review protocol), run the media-buying-sop-generator skill separately. Triggers on "build my ads plan", "30/60/90 plan", "ads plan", "what's my strategy", or "where am I going next quarter".
---

# Ads Plan Generator (30/60/90 Day Plan)

Produces one artifact:

- `outputs/ads-plan.md` — A strategic 30/60/90 day plan tailored to the user's account, KPIs, creative strategy, and growth targets

For the operational Media Buying SOP (budget brackets, kill/scale rules, daily review protocol, weekly cadence — the playbook a media buyer follows daily), run the **media-buying-sop-generator** skill separately. The two skills are designed to work together: this one sets direction, that one sets execution.

This skill runs AFTER the foundations are in place. It assumes context files are filled, creative strategy brief exists, KPIs are locked in, and at least one batch of scripts has been generated.

---

## Prerequisites

Before starting, verify ALL of these exist. If any are missing, tell the user to complete the foundations setup first (run Guided Setup).

- [ ] `context/business.md` — filled in (not a template)
- [ ] `context/ad-account.md` — filled in with locked-in KPI benchmarks
- [ ] `outputs/creative-strategy-*.md` — at least one creative strategy brief
- [ ] `outputs/ad-scripts-*.md` — at least one script batch

If anything is missing:

> "I can't build your plan and SOPs yet — foundations aren't complete. Run the Guided Setup first to produce [missing items]. Then come back."

---

## Phase 1: Strategic Context (5 min)

Read:
1. `context/business.md`
2. `context/ad-account.md`
3. The most recent `outputs/creative-strategy-*.md`
4. The most recent `outputs/ad-scripts-*.md`

Confirm you've understood the account by summarizing back:

> "Here's what I have:
>
> - Business: [1-line summary of offer + ICP]
> - Current performance: [monthly spend, CPR, ROAS]
> - Target: [target CPR, ROAS, break-even]
> - Creative strategy: [N personas, primary angles, awareness mix]
> - Scripts ready: [N scripts, formats]
>
> Is this accurate? If anything is wrong, tell me now before we build the plan."

Wait for confirmation.

---

## Phase 2: Growth Target Interview (10 min)

Ask one question at a time:

### Q1 — Revenue Target (90 days)
"Where do you want this account to be 90 days from now? Give me a specific revenue/result number."

### Q2 — Spend Willingness
"What's the most you're willing to spend per month in the next 90 days if results are proven? Not your current spend — the ceiling."

### Q3 — Biggest Risk
"What's the single biggest risk to hitting that target? Creative fatigue, offer mismatch, ad account stability, cash flow, something else?"

### Q4 — Constraints
"What are the hard constraints on what you CAN'T do? (e.g., can't change pricing, can't add new formats, can't hire more people, etc.)"

### Q5 — Funnel Type
"Are you running a Lead Gen funnel (leads → setter → closer), Direct Purchase funnel (ad → landing page → buy), or both? If both, what's the split?"

### Q6 — Team Capacity
"Who's doing what? Script writing, editing, uploading, reporting — are these all you, or do you have help? How many hours per week can actually be invested?"

### Q7 — Current Bottleneck
"If you had to point at ONE thing that's limiting growth right now, what would it be?"

Save answers in working memory for plan generation.

---

## Phase 3: Generate The 30/60/90 Day Plan (10 min processing)

Write `outputs/ads-plan.md` using this structure:

```markdown
# Ads Plan — [Client Name or "Your Business"]
**Generated:** [Date]
**Target:** [From Q1]
**Spend Ceiling:** [From Q2]
**Funnel Type:** [From Q5]

## Current State
- Monthly spend: [from ad-account.md]
- Current CPR: [X] (target [Y])
- Current ROAS: [X] (break-even [Y])
- Creative diversity: [N personas, N angles, N formats active]
- Biggest bottleneck: [from Q7]

## 30-Day Goals
[Tactical — fix the current bottleneck, get baseline data solid]

**Targets:**
- Spend: [$X]
- CPR: [$X — conservative improvement from current]
- Creative output: [N concepts tested]

**Priority actions:**
1. [Fix top bottleneck — specific actions from Q7]
2. [Baseline creative testing system — ensure naming conventions are applied]
3. [Address top risk from Q3]

**Creative testing priorities:**
- Test [persona X] with [format Y] via [angle Z] — hypothesis: [specific bet]
- Test [persona A] with [format B] via [angle C] — hypothesis: [specific bet]
[List 3-5 specific tests drawn from the strategy map]

**Success criteria:**
- At least [N] winning concepts identified (CPR below target)
- Hit rate baseline established
- Bottleneck analysis cadence in place

## 60-Day Goals
[Scale proven winners, diversify into new personas/formats]

**Targets:**
- Spend: [$X — ramped from 30-day baseline if winners exist]
- CPR: [target — further improvement]
- Creative output: [N new concepts + N refreshes of winners]

**Priority actions:**
1. [Scale winners from 30-day tests with specific budget increase rhythm]
2. [Launch new persona tests — specifically P[X] micro personas not yet tested]
3. [Introduce new format diversity — specifically [format] if not present]

**Creative testing priorities:**
- [Specific tests focused on filling gaps identified in 30-day data]

**Success criteria:**
- Scaled campaigns holding CPR under target at higher spend
- New persona coverage expanded
- First refreshes of fatigued winners launched

## 90-Day Goals
[Lock in scale, build redundancy, prepare for next quarter]

**Targets:**
- Spend: [$X — toward ceiling from Q2]
- CPR: [$X — at or below target]
- Hit rate: [known and tracked]

**Priority actions:**
1. [Scale toward spend ceiling]
2. [Build creative refresh pipeline — no single ad carries the account]
3. [Address cross-account diversity — veilance zones, cognitive biases, self-concept anchors]

**Success criteria:**
- Account hitting 90-day revenue target
- No single ad responsible for >40% of results (creative redundancy)
- Clear view of what the NEXT quarter's strategy should be (fresh research, new angles)

## Risk Mitigation
[From Q3 + Q4 answers]
- [Risk 1]: [Specific mitigation action]
- [Risk 2]: [Specific mitigation action]

## What Success Looks Like At Day 90
[Narrative paragraph: given their inputs, what does the account look like at day 90 if everything goes right?]

## What Would Make This Plan Fail
[Be honest. List 2-3 specific failure modes based on their answers and the account state.]
```

Show the plan to the user. Ask:

> "Read this back. Does it match your ambition and your constraints? If anything feels off — too aggressive, too conservative, missing a specific risk — tell me now."

Iterate based on feedback. Save to `outputs/ads-plan.md` when approved.

---

## Phase 4: Hand-off To Media Buying SOP Generator (1 min)

The 30/60/90 plan tells the account where it's going. The operational playbook tells the media buyer how to get there.

Tell the user:

> "Your strategic plan is locked. The next step is the operational playbook your media buyer follows daily — budget brackets, kill/scale rules, daily review protocol, weekly cadence. That's a separate skill: **media-buying-sop-generator**.
>
> Run it now, or come back to it later. Either way, the SOP it produces will reference the targets in this plan, so they stay in sync.
>
> Want me to run it now?"

If yes, hand off to `skills/media-buying-sop-generator/SKILL.md`. If no, save checkpoint and end.

---

<!-- Below this point is reference material kept for transparency. The full media buying SOP is generated by the media-buying-sop-generator skill. The structure below is what that skill produces — included here so the plan's context shows what comes next. -->

### What The Media Buying SOP Will Cover

```markdown
# Media Buying SOP — [Client Name or "Your Business"]
**Generated:** [Date]
**Funnel Type:** [From Q5]
**Account Stage:** [Testing / Early Scale / Scale / Optimization — infer from spend level]

## 1. Campaign Structure

### Testing Campaigns (ABO)
- Budget per ad set: [$X/day — based on current CPR and spend tolerance]
- Ad sets per campaign: [3-5, recommended]
- Ads per ad set: [3 concepts testing 3 hook variations each = 9 ads/adset]
- Audience targeting: [broad / interest-based / lookalike — based on account stage and platform recommendations]

### Scaling Campaigns (CBO / Advantage+)
- Budget: [$X/day — started at 2x what the winner was spending in testing]
- Audience: [broad or stacked LALs depending on account maturity]
- Concept limit: [6-8 winners max — avoid fragmentation]

### Retargeting (if applicable)
- Budget: [10-15% of total spend typical]
- Window: [7-30 day based on sales cycle]

## 2. Naming Convention

**Required format for all ads:**
`[Persona Code]_[Format]_[Angle]_[Offer]_[Version]`

Example: `P1.2_UGC-Selfie_Ozempic-Refugee_6mo-Setup_v1`

**Persona Codes:** [List their P1, P2, etc. from the strategy brief]
**Formats:** [UGC-Selfie / Talking-Head / B-Roll / Static / Carousel / Testimonial — list based on strategy map]
**Angles:** [List named angles from strategy brief]
**Offers:** [List their offer variants]
**Version:** v1, v2, v3 as iterations are produced

**Why this matters:** Without this structure, the Bottleneck Analysis skill can't attribute results to the right variables. Kill/scale decisions become guesses.

## 3. Testing Framework

### Creative Production Cadence
- **New concepts per week:** [N — based on Q6 team capacity]
- **Concepts per batch:** [5 — matches Script Generator default]
- **Hook variations per concept:** [3 — always]

### Hit Rate Math
Based on current data, expect a [X]% hit rate (winners ÷ total tests).

To produce [Y] winning concepts per month, you need to test [Y ÷ X × 100] concepts per month.

### Test Duration
- **Minimum spend before decision:** [$X — equivalent to 2x your target CPR]
- **Minimum time:** [3 days]
- **Signal thresholds:** Use the KPI benchmarks in `context/ad-account.md`

## 4. Kill / Scale / Watch Rules

### Kill
[Pull from context/ad-account.md — the criteria set during foundations]

### Scale
[Pull from context/ad-account.md]

### Watch (don't touch)
- New ads under the spend threshold
- Ads within 20% of target CPR
- Ads showing unusual early signals (high hook rate, low CTR — data is still ambiguous)

### Promote (testing → scaling)
When a concept in a testing campaign beats target CPR for 3+ days with volume:
1. Duplicate the concept into the Scaling Campaign
2. Start at 2x the testing budget
3. Do NOT touch the testing campaign version — let it run

## 5. Daily Rhythm

### Morning (5-10 min)
1. Open Meta Ads Manager
2. Pull yesterday + last-3-days metrics
3. Run the **Daily Media Buyer Check-in** skill
4. Execute kill/scale decisions from the report

### Midday (optional — only if spend >$500/day)
- Quick pulse check: CPM spiking? Any ad running away with budget?

### Evening (5 min)
- Log any deals closed to your tracking sheet
- Note any observations for tomorrow

## 6. Weekly Rhythm

### Monday (30 min)
1. Run **Bottleneck Analysis** skill on last 7 days of data
2. Update `context/ad-account.md` with any changed benchmarks
3. Brief this week's creative priorities based on bottleneck output

### Wednesday (60-90 min)
1. Script new batch using **Script Generator** (5 scripts per batch)
2. Run **Script QC** on the batch
3. Hand to production/editor

### Friday (15 min)
1. Weekly review — did we hit creative production target?
2. Log winners and losers to the creative tracker
3. Plan Monday's priorities

## 7. Monthly Rhythm

- **Week 1:** Run Bottleneck Analysis, update plan if off-track
- **Week 2:** Creative refresh — bring back high-performing paused ads, retest
- **Week 3:** Persona expansion — test a new micro persona not yet covered
- **Week 4:** Format experimentation — test an underrepresented format

## 8. Reporting Template

Track these weekly in a sheet (or use Cortana if ad spend justifies it):

| Metric | Target | This Week | Last Week | Trend |
|--------|--------|-----------|-----------|-------|
| Spend | | | | |
| Impressions | | | | |
| CPM | | | | |
| Hook Rate | | | | |
| Hold Rate | | | | |
| CTR (Link) | | | | |
| Leads / Purchases | | | | |
| CPR | | | | |
| ROAS | | | | |
| Winners produced | | | | |

## 9. When To Escalate

Escalate to a full re-strategy (re-run Creative Strategy, re-run KPIs) when:
- Account CPR is 2x target for 7+ days and Bottleneck Analysis hasn't surfaced a fix
- A full batch of new scripts fails to produce a winner after $X spent
- The business fundamentally changes (new offer, new pricing, new ICP)
- Quarter ends and you want a fresh creative strategy cycle

## 10. Non-Negotiables

1. Every ad is named with the convention — no exceptions
2. Daily check-in runs every single morning the account is live
3. Monday bottleneck analysis is locked on the calendar
4. Winners get promoted to scaling, not just left in testing
5. No new creative cycle starts without updated voice-of-customer data (new sales calls added to knowledge-base/)
6. Any scaling decision above [2x current daily spend] requires a full bottleneck analysis first
```

Show the SOP to the user. Ask:

> "Read through it. Does the campaign structure match how you (or your team) actually operate? Does the cadence fit your bandwidth? Anything unrealistic or missing?"

End of reference. Continue to Phase 5.

---

## Phase 5: Sync & Summarize (2 min)

Write a summary entry to `memory/open-loops.md`:

```
## Ads Plan Generator — Complete
Date: [date]
Artifact:
- outputs/ads-plan.md (30/60/90 day plan)

Next action:
- Run media-buying-sop-generator to produce the operational playbook
- Then: apply naming convention to active ads, execute Week 1 priorities, start daily check-in rhythm
```

Tell the user:

> "Done. You now have your **Ads Plan** (`outputs/ads-plan.md`) — 30/60/90 day targets and priority actions.
>
> Next: run **media-buying-sop-generator** to produce the operational playbook your media buyer follows daily. That SOP turns the targets in your plan into specific budget brackets, kill/scale rules, and a daily review protocol.
>
> If anything in the plan doesn't match your reality in 2-4 weeks, we revise. The plan is a hypothesis — the account tells us what's right."

---

## Constraints

1. **Never produce a generic plan.** Every target, every priority, every test must reference something specific from the user's data — their current CPR, their personas from the brief, their bottleneck from Q7.
2. **Never skip Phase 2.** The growth target interview is what makes the plan theirs vs. a template.
3. **Never write SOPs the user can't execute.** If they said they have 5 hours/week in Q6, don't prescribe a 20-hour/week cadence. Match it to reality.
4. **Flag tension openly.** If their revenue target (Q1) is incompatible with their spend ceiling (Q2) or their capacity (Q6), say so directly before generating the plan. Don't hide the math.
5. **Pull real numbers.** Campaign budgets, test thresholds, kill criteria — all pulled from `context/ad-account.md`, never invented.
