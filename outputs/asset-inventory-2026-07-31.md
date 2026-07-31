# Asset Inventory (Pre-Flight Checklist) — Oakhaven Media
**Date:** 2026-07-31
**Per:** `course/04 — Asset Inventory (Pre-Flight Checklist).md`
**Purpose:** This is the gate the Master Setup Prompt checks at guided-setup Phase 5. Scored honestly, not optimistically.

---

## Scorecard

| # | Category | Score | Hard gate? |
|---|----------|-------|-----------|
| 1 | Voice of Customer Data | 🔴 **RED** | **YES** |
| 2 | Business Fundamentals | 🔴 **RED** | **YES** |
| 3 | Ad Account Data | ⚪ N/A | Only if running ads — they aren't |
| 4 | Market Intelligence | 🟢 **GREEN** (upgraded 2026-07-31) | Yes |
| 5 | Performance History | ⚪ N/A | Only if running ads |
| 6 | Tracking Infrastructure | 🔴 RED | Recommended |
| 7 | Creative Production Assets | 🟡 YELLOW | Optional |
| 8 | Team & Capacity | 🔴 **RED** | **YES** |

## VERDICT: NOT READY — do not proceed past Phase 5

Three hard-gate REDs (1, 2, 8). Per guided-setup Phase 5: *"Any RED in categories 1, 2, or 8 — STOP. Do not proceed."*
Do **not** run Creative Strategy, Script Generator, or KPI Tracker yet. Close the gaps first.

---

## 1. Voice of Customer — 🔴 RED

**Rule:** RED = fewer than 5 sales call transcripts. Oakhaven has **zero**.

| Asset | Have | Notes |
|---|---|---|
| Sales call transcripts | 0 / 5 min | No calls recorded. No CRM. |
| Survey data | 0 | No customer base to survey |
| Support logs | 0 | Same |
| Online reviews (own) | 0 | Same |
| Online reviews (competitors) | Not yet pulled | Queued in `voice-of-customer.md` Tier 2 |
| Community posts / ad comments | ~10 verbatims | Already extracted from the client dump |

**UPDATE 2026-07-31 (later):** bank now at **~115 verified across all four awareness bands** — Reddit scraper
(35, permalinked), EditCrew (~30), Boomin Brands (~20), VidChops (~20), Editors Connection coach quotes (3),
client dump (11). Index: `research/voice-of-customer.md`.

Score stays 🔴 by the letter of the rule — RED means fewer than 5 sales calls, and there are none. But the
substitute now clears the Script Generator's verbatim-bank gate and is serviceable for scripting.
What it still cannot give you: why someone says no at Oakhaven's price. Sales calls only.

**Mitigation in place:** `knowledge-base/research/voice-of-customer.md` — competitor-sourced VOC with a harvest queue.
Step 04 explicitly sanctions this for the *reviews/community* line item: *"No reviews or community data: go to competitor ad comment sections. Scrape 100+ comments. This is where Unaware-level language hides."*

**But it does not clear the gate.** Step 04's remedy for missing sales calls is unambiguous: *"Start recording today. Use Fathom. Come back when you have 5+."* Competitor VOC substitutes for the *soft* inputs, not the hard one. Treat it as damage control, not a pass.

**To reach YELLOW:** 5 sales call transcripts, or 5–8 recorded ICP interviews as the interim proxy.
**To reach GREEN:** 10+ calls plus two other VOC sources (competitor ad comments + Trustpilot/G2 negatives would do it).

## 2. Business Fundamentals — 🔴 RED

**Rule:** RED = can't answer 3+ of the 6 items specifically. Three fail.

| Item | Status |
|---|---|
| Offer details | ⚠️ **Partial** — deliverables clear, **price and structure unknown**. Inferred $1,250–$2,500/mo from the VSL's "one-fourth of $5–10k payroll" anchor. An inference is not an answer. |
| Unique mechanism | ✅ Strong — Content Immersion System, three named phases, clearly articulated |
| ICP definition | ✅ Documented (coaches / business owners / creators) |
| Proof assets | ❌ **Zero.** Requirement is minimum 5 with specific numbers. Oakhaven has founder credibility claims and no case studies, no before/afters, no named clients, no stats. |
| Known objections | ❌ Inferred from competitor VOC. No sales team, so no observed objections. |
| Founder/brand story | ⚠️ Narrative exists and is good; founder is unnamed and years-operating is an unfilled `[X years]` in the VSL |

**Note:** the mechanism is the strongest asset in this whole file. Step 04 flags "can't articulate unique mechanism" as a bigger problem than ads — Oakhaven doesn't have that problem. The gap is purely evidentiary: a strong claim with nothing behind it.

**Fix first:** the **side-by-side** — generic edit vs. Oakhaven edit of the same footage. The offer is a visual claim in a visual medium with no visual evidence. One asset closes the largest hole here.

## 3. Ad Account Data — ⚪ N/A
Brand new account, zero spend. Step 04 says skip to Category 4. Revisit after ~7 days of spend.

## 4. Market Intelligence — 🟢 GREEN *(upgraded 2026-07-31)*

| Item | Status |
|---|---|
| Top 3–5 competitors identified | ✅ Five: EditCrew, Boomin Brands, The Editors Connection, VidChops, Podcast Monkey |
| Competitor ad examples | ✅ **18 live ads ripped** with video + timestamped transcripts → `research/competitors/swipes/` |
| Angles / formats / hooks documented | ✅ `research/competitors/ad-teardown.md` |
| Pricing / offer structure | ✅ `research/competitors/market-pricing-and-positioning.md` — $495 to $2,450 ladder |
| Differentiation per competitor | ✅ Resolved, and the answer is brutal — see below |

**Sophistication question: ANSWERED — yes.** Every table-stakes claim confirmed spending on video with timestamps.

**The finding that matters:** Oakhaven's VSL v1 is, beat for beat, an ad EditCrew and Boomin Brands are running
right now — in-house-cost anchor, dedicated PM (they field three people), unlimited revisions, fixed price,
14-day guarantee, book-a-call CTA. VSL v1 is retired. VSL v2 (mechanism) is the only viable direction, and the
mechanism lane is confirmed empty across all 18 ads.

**Remaining gap:** ad comments. The Ad Library doesn't expose them — they live on the live FB/IG posts and need
a manual pull. That's a Category 1 item, not Category 4.

## 5. Performance History — ⚪ N/A
No ads have ever run. Handled via the system's stated new-account exception —
`knowledge-base/winning-ads/NEW-ACCOUNT.md` is in place. Format recommendations lean on competitor data instead.

## 6. Tracking Infrastructure — 🔴 RED
Unknown across the board: Pixel, CAPI, landing page, booking tool, CRM, attribution platform.
Also unresolved: **the conversion event itself** — the funnel has both "book a 15-min call" and "order now" as CTAs.
Blocks Ads Setup Engine and makes the Lead Quality Report unrunnable.

## 7. Creative Production Assets — 🟡 YELLOW
Five drafted-but-unrun scripts (1 TOF, 2 BOF, 2 VSLs) and full landing copy — genuinely useful raw material.
Missing: the side-by-side, the onboarding/brief screen recording, any client-result footage. All three are
marked as `[insert here]` placeholders in the client's own VSL script.

## 8. Team & Capacity — 🔴 RED
Nothing known. Unanswered: who films and appears on camera, creative production capacity per week
(a direct input to the testing structure), who runs the ad account, monthly budget, who handles inbound calls.
Guided-setup treats this as a hard gate for a reason — the testing cadence is built from it.

---

## Gap-closing sprint — do these in this order

| # | Action | Unblocks | Effort |
|---|---|---|---|
| 1 | **Get the price and offer structure** from the client, in writing | Cat 2, KPI Tracker, Media Buying SOP | 1 message |
| 2 | **Get team/capacity + budget answers** | Cat 8, testing structure | 1 message |
| 3 | **Run competitor-swipe** on the 6 ad IDs; answer the sophistication question | Cat 4 → GREEN | 2–3 hrs |
| 4 | **Scrape competitor ad comments** into `voice-of-customer.md` | Cat 1 (partial) | 2 hrs, free |
| 5 | **Pull Trustpilot/G2 reviews** — negatives first, 50/30/20 split | Cat 1 (partial) | 2 hrs |
| 6 | **Produce the side-by-side proof asset** | Cat 2, and the entire mechanism claim | 1 day |
| 7 | **Start recording every sales call** (Fathom free tier). Re-gate at 5. | Cat 1 → YELLOW | ongoing |
| 8 | **Run 5–8 ICP interviews** if calls are weeks away | Cat 1 interim proxy | 1 week |

Items 1–5 are achievable this week and move the workspace from NOT READY to
"proceed with flagged weaknesses." Item 7 is the only thing that makes it properly GREEN.
