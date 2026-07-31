# Creative Strategy Brief — Oakhaven Media (WIP)
**Generated:** 2026-07-31 · **Version:** 0.1 — *Steps 1–4 complete, paused at Step 5 checkpoint*
**Status:** ⛔ NOT READY FOR SCRIPTING. Awaiting persona selection.

---

## Pre-Flight Gate

| # | Hard-gate input | Status |
|---|---|---|
| 1 | Sales call transcripts (min 5) | ❌ **ZERO.** Declared substitute per `CLAUDE.md`: `voice-of-customer.md` (~115 competitor-sourced verbatims). Every persona below is a **lower-confidence hypothesis**. |
| 2 | Customer base data | ❌ **NONE.** No CRM, no buyers, no intake data. Demographics are inferred from competitor buyers, not Oakhaven's. |
| 3 | Competitor research doc | ✅ **STRONG.** 18 live ads with timestamped transcripts + a full pricing ladder. |
| 4 | Offer briefing | ⚠️ **PARTIAL.** Deliverables and mechanism known. **Price unknown. Proof assets: zero.** |
| 5 | Previous winning ads | ⚠️ **VALID EXCEPTION** — brand-new account, zero history. Leaning on competitor format data per skill rule. |

**Two hard gates are failed, not substituted.** Gate 1 has a declared stand-in. Gate 2 has nothing.
Proceeding under the CLAUDE.md exception with everything flagged. This is a market-derived strategy,
not a customer-derived one.

---

## Step 1 — Data Quality Assessment

**Volume:** Adequate. ~115 verbatims across 5 sources.

**Diversity:** Poor in a specific and consequential way. The corpus splits into two populations that
do not overlap:

| Source | n | Population | Awareness | Bias |
|---|---|---|---|---|
| Reddit (Arctic Shift archive) | 35 | 80% **non-buyer**, self-editing | Unaware → Solution | Skews r/PartneredYoutube — hobbyist creators, not the $1k+/mo ICP |
| Competitor testimonials (4 sites) | ~73 | 100% **buyer**, post-purchase | Problem → Product | Curated marketing pages. 100% positive by construction. |
| Client dump | 11 | Mixed | Problem, Solution | Provenance unaudited |

**The gap this creates:** nobody in the corpus is a *cold prospect at Oakhaven's price point*.
The Reddit population largely can't afford $1k+/mo. The testimonial population already bought and
is being quoted by the seller. There is **zero data on price resistance**.

**Recency:** Good. Reddit quotes are Feb 2026, competitor ads are live-now.

**Relevance:** The Unaware bucket is thinner than the count suggests — 12 tagged, ~4 genuinely
on-target for *editing* pain. The rest is adjacent creator burnout. 4 dry searches on
coach-premium language returned nothing.

---

## Steps 2–3 — Tagging & Clustering

12 proto-persona clusters. Grouped by **evidence origin**, because the three groups carry
materially different confidence.

### Group A — Reddit-derived (cold, non-buyer, unprompted)
Highest trust in the language, lowest trust in the budget.

### Group B — Competitor-testimonial-derived (warm, buyer, curated)
Highest trust in the budget, lowest trust in the framing — these are seller-selected quotes.

### Group C — Client-directed (no supporting evidence)
Included because the client planned angles around it. Scored honestly.

---

## Step 4 — Persona Scorecard

CTC = (Urgency×0.4) + (Awareness×0.3) + (Skepticism_inv×0.3)
MS = (TAM×0.5) + (Creative Scalability×0.5)

| # | Persona | Grp | Urg | Awr | Skp⁻¹ | **CTC** | TAM | CS | **MS** | Awareness | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | The Midnight CapCut Owner | A | 7 | 6 | 6 | **6** | 9 | 8 | **9** | Problem | Medium |
| 2 | The Burned Re-Hirer | A/B | 8 | 8 | 3 | **7** | 6 | 9 | **8** | Solution | High |
| 3 | The Ground-Down Grinder | A | 9 | 3 | 5 | **6** | 9 | 9 | **9** | Unaware | Medium |
| 4 | The Agency Capacity Ceiling | B | 8 | 8 | 4 | **7** | 6 | 8 | **7** | Solution | High |
| 5 | The Freelancer-Roulette Survivor | B | 8 | 8 | 4 | **7** | 6 | 7 | **7** | Solution | High |
| 6 | The Coach (time & cost framed) | B | 6 | 6 | 5 | **6** | 8 | 7 | **8** | Problem | Medium |
| 7 | The Blocked Creator | A | 6 | 7 | 6 | **6** | 7 | 6 | **7** | Solution | Medium |
| 8 | The Vision Keeper | A | 5 | 7 | 2 | **5** | 7 | 8 | **8** | Solution | High |
| 9 | The Feast/Famine Production Co. | B | 8 | 7 | 4 | **7** | 4 | 6 | **5** | Solution | Medium |
| 10 | The Production-Gap Solo Operator | A | 6 | 4 | 6 | **5** | 7 | 7 | **7** | Unaware | Medium |
| 11 | The ROI Gatekeeper | A | 3 | 6 | 3 | **4** | 9 | 4 | **7** | Solution | Medium |
| 12 | The Premium-Positioning Coach | C | 3 | 3 | 5 | **4** | 6 | 5 | **6** | Unaware | **NONE** |

---

## Cluster evidence

**1. The Midnight CapCut Owner** — SMB owner self-editing after hours.
> "Mine's definitely the weekly social content grind — coming up with fresh posts that don't look like they were made by 5 different people is exhausting when you're already running the actual business" — r/smallbusiness, UNAWARE
> "editing everything myself in CapCut at like 11pm after the baby was asleep" — client dump
Pain: editing consumes revenue hours. Outcome: the hours back.

**2. The Burned Re-Hirer** — paid already, got generic work.
> "The content was so generic and in some cases had typos" · "their graphics are quite… well boring, basic images, nothing custom made"
Pain: paid and still had to fix it. Outcome: one team that doesn't need managing. Highest skepticism after #8.

**3. The Ground-Down Grinder** — high effort, no return, close to quitting. Highest-engagement quote in the entire corpus (score 36).
> "I work WAY more hours and spend more money to produce videos than I ever did at my 'real job' — and i was a web developer"
> "I got tired of putting a lot of effort into my content and only got around 30 videos max… it really, really mentally fucked me up"
Pain: effort/return mismatch. Outcome: the work paying off. **Blames the algorithm, not editing** — hence Awareness 3.
Strategic note: this is the frame behind EditCrew's scaled winner (`video-bottlenecks-killing-your-growth`, 5 live variants) — the only validated concept in the market.

**4. The Agency Capacity Ceiling** — agency owner, editors are the growth blocker.
> "I have had every bottleneck you can think of when it comes to having to manage editors, correct typos" — Alec Minkoff
> "our biggest barrier to growing was finding really solid, reliable quality editors" — Nathan Jones
> "If I'm hiring a freelance editor, **I'm the project manager**" — Ryan Stober
Pain: capacity ceiling on client revenue. Outcome: scale without hiring. **Highest-paying segment in the market — 8/13 EditCrew buyers, 4/6 Boomin buyers. The client chose not to pursue it.**

**5. The Freelancer-Roulette Survivor** — loses the training investment every cycle.
> "It takes a week or two, sometimes longer, just to get a freelancer onboarded… they've already learned your stuff and learned your styles, but they're gone." — Adriel Hampton
Distinct from #2: burned on *continuity*, not on quality. Brand Download answers this directly.

**6. The Coach (time & cost framed)** — content is the acquisition channel.
> "I can create without worrying about editing." — Chad Morgan
> "They're an extension of my team, not just an editor." — Shana Yurko
5 coaches evidenced across TEC + VidChops. **Every one sold on time and cost. None on premium positioning.**

**7. The Blocked Creator** — ideas ready, editing is the wall.
> "I can record videos all day, but once it comes to editing, that's where I stop… I have the ideas written down and everything"
Lowest budget confidence of Group A for a $1k+/mo offer from cold.

**8. The Vision Keeper** — identity-level resistance to delegating.
> "you feel like you're the only one who understands how to edit properly the way you want it"
> "In many ways then I feel like its their video and not mine lol"
> "They all end up changing the edits to match their workflow"
> "He doesn't know your audience… You can't expect someone else to tell you that"
Pain: delegation costs authorship. Outcome: hand off without losing the voice.
**The hardest objection and the one the Content Immersion System was built to answer. Nobody in 18 competitor ads addresses it.**

**9. The Feast/Famine Production Co.** — cyclical capacity, can't justify a full-time hire.
> "The big project comes in and then I'm just gone for a month" — Andrew Cardy
> "in the ups, you're doing production… then you come back to the office and you're doing editing for a week, a month" — Christopher Dorsano

**10. The Production-Gap Solo Operator** — can't match team-produced competitors.
> "Multiple camera angles, animations, graphics, footage… if they uploading videos like that every week then that is a team, not one person"
> "Editing very detailed videos as one person. Wanting to go for a near Netflix production quality"

**11. The ROI Gatekeeper** — can't justify the spend yet.
> "Did you earn enough from them to justify hiring an editor?"
> "No thanks. Would rather build my editing skills than hire someone whos likely going to ask for way too much money"
Large TAM, shallow creative well, price-resistant. Volume without convertibility.

**12. The Premium-Positioning Coach** — ⚠️ **CLIENT-DIRECTED, ZERO EVIDENCE.**
4 dry searches returned nothing ("I want to be seen as premium but my marketing doesn't look premium", "I look like just another coach online", "high ticket clients judge you on how professional your content looks", "my personal brand doesn't match the quality of my offer").
5 coaches found in competitor case studies, none sold on this. **Three of the client's seven planned angles depend on this persona.** Scoring it honestly rather than deleting it — the client's call.

---

## Next: Step 5 human checkpoint — awaiting selection of 5 personas + user thesis.
