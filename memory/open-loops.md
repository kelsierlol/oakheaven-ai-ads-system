# Open Loops

*Tasks and items that need follow-up from previous sessions. Review at start of every session.*

<!-- Format:
- [DATE] — [Task description] — [Status: pending/in-progress/blocked]
-->

## Client: Oakhaven Media (video editing subscription) — onboarded 2026-07-31

Context files are populated from the client's raw research dump. `knowledge-base/` is scaffolded.

**🟡 PRE-FLIGHT STATUS: PROCEED WITH FLAGS — interim mode, deliberate.** Asset Inventory run 2026-07-31 →
`outputs/asset-inventory-2026-07-31.md`. Three hard-gate REDs remain: Voice of Customer (0 sales calls),
Business Fundamentals (no price, no proof), Team & Capacity (unknown).

**[2026-08-01] DECISION — the sales-call gate is waived for Phase 1.** Guided-setup Phase 5 would normally
block Creative Strategy, Script Generator and KPI Tracker here. The client has chosen to start now on
competitor-sourced VOC rather than wait for his own calls, and to re-run properly once calls exist. This is
an accepted trade, not an oversight.

**What this means when you run those skills:**

- **Run them.** Do not stop and cite the missing sales calls as a blocker. The substitute is declared:
  `knowledge-base/research/voice-of-customer.md`, ~115 verified verbatims across all four awareness bands.
- **Flag everything built on it.** Every persona, angle and script is a lower-confidence hypothesis until
  real calls land. Say so in the output — don't present them as settled conclusions.
- **The still-hard blocks stay hard.** Price is genuinely unknown, so no script may state or imply a price,
  and KPI Tracker cannot model unit economics until Q1–Q7 of the questionnaire are answered. No case study
  or named result exists, so proof stays as `[INSERT PROOF]` tags. Do not invent either.

**Phase 2 trigger:** 5 transcripts in `knowledge-base/sales-calls/` → re-run Creative Strategy on the
client's own data, demote `voice-of-customer.md` to secondary market context, remove the confidence flags.

The gap-closing sprint is at the bottom of the inventory file. Items 3–5 (competitor swipe, VOC harvest,
review pulls) are complete; 1, 2, 6 and 7 are on the client.

*Equivalent of guided-setup Phases 1–4 is complete* (filing verified, business/ad-account/glossary written
from documents rather than a live interview). Phase 5 is where this stops.

### Blockers — ask the client

- [2026-07-31] — **Price point and offer structure.** Not in the dump. VSL implies $1,250–$2,500/mo from the "one-fourth of $5–10k payroll" anchor, unconfirmed. Blocks KPI Tracker, CAC math, and the entire Media Buying SOP. — **blocked**
- [2026-07-31] — **Conversion event.** Call-booking and direct "order now" both appear as CTAs. Which one is the tracked result? Changes the whole KPI model. — **blocked**
- [2026-07-31] — **Deliverable specifics.** Videos per month, formats covered (reels / long-form / ads / podcast), revision policy, guarantee (14-day money-back vs. unlimited-revisions-on-first-project — the VSL lists both as options). — **blocked**
- [2026-07-31] — **Founder name, team size, years operating.** VSL has an unfilled `[X years]`. — **blocked**
- [2026-07-31] — **Landing page URL, tracking (Pixel/CAPI), CRM/booking tool, geo, monthly budget.** Blocks Ads Setup Engine. — **blocked**
- [2026-07-31] — **Naming decisions:** "Content Immersion System" vs. "Method"; "project manager" vs. "creative manager". Pick one of each and lock it. — **pending**

### Do these first

- [2026-07-31] — **Produce the side-by-side proof asset**: generic edit vs. Oakhaven edit of the same segment. The entire offer is a visual claim being made in a visual medium with no visual evidence. The VSL script itself marks this as the most powerful proof element and it doesn't exist. — **pending**
- [2026-07-31] — ~~Run competitor-swipe~~ — **DONE.** 18 live ads ripped with timestamped transcripts → `research/competitors/`. Category 4 now GREEN. Sophistication question **answered: yes**. — **complete**
- [2026-07-31] — ~~Resolve the VidChops conflict~~ — **DONE, and it's worse than thought.** EditCrew and Boomin Brands are each running Oakhaven's VSL v1 beat for beat (in-house-cost anchor, dedicated PM ×3 people, unlimited revisions, fixed price, 14-day guarantee, book-a-call). **VSL v1 is retired.** Mechanism lane confirmed empty across all 18 ads. See `research/competitors/ad-teardown.md`. — **complete**
- [2026-07-31] — **Oakhaven's offer needs a quantified promise.** Boomin runs "20 Videos. 14 Days. Or you don't pay" + scarcity. Oakhaven's "book a call, get a free edit" has no number in it. Fix once price + volume land from the questionnaire. — **pending**
- [2026-07-31] — **Study EditCrew's scaled winner** before writing hooks: `video-bottlenecks-killing-your-growth`, 5 simultaneous live variants, growth-framed not time-framed. The only validated concept in the market. — **pending**
- [2026-07-31] — **Pull ad comments manually.** The Meta Ad Library does not expose comments; they live on the live FB/IG posts. This is the highest-signal remaining VOC source. — **pending**

### Research gaps

- [2026-07-31] — **No sales calls.** Still true and still the only fix for Product-Aware objection data. Record and transcribe every call from call #1; re-run Creative Strategy at 5. — **pending**
- [2026-07-31] — ~~VOC harvest~~ — **DONE.** Bank at **~115 verified**, all four awareness bands. Five sources: client dump (11), Reddit scraper (35), EditCrew (~30), Boomin Brands (~20), VidChops (~20), Editors Connection coach quotes (3). Clears the Script Generator gate. Index: `research/voice-of-customer.md`. — **complete**
- [2026-07-31] — ~~Pull VidChops + Boomin customer stories~~ — **DONE.** All four competitors ripped. — **complete**
- [2026-07-31] — **COACH PREMIUM ANGLE — decision needed.** Coaches *do* buy (5 in competitor case studies), but every one is sold on time and money saved, never on charging more. Three of the client's seven angles claim they buy to raise prices. Zero supporting language anywhere, including 4 dry Reddit searches. **Resolve via ICP interviews before funding those angles.** — **blocking creative strategy scope**
- [2026-07-31] — **Agencies pay the most and aren't being pursued.** EditCrew (8/13) and Boomin (4/6) buyers are agencies. The client saw EditCrew's agency ad and passed. Worth revisiting. — **pending**
- [2026-07-31] — **Unaware bank is thinner than it counts.** 12 tagged, ~4 on-target for editing pain; the rest is adjacent creator burnout. Sample skews r/PartneredYoutube and 80% non-buyer. — **pending**
- [2026-07-31] — **No customer base data.** No CRM, no buyers. Personas in `context/business.md` are hypotheses only. — **blocked**

### Next actions once unblocked

1. competitor-swipe → `knowledge-base/research/competitor-analysis.md`
2. VOC harvest → expand `voice-of-customer.md`
3. Creative Strategy (flagging low confidence on persona scoring)
4. KPI Tracker (needs price) → Naming Code Sheet → Script Generator → Script QC
5. Ads Setup Engine → Media Buying SOP Generator
