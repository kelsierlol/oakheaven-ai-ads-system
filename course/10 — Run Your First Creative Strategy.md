# Step 10 — Run Your First Creative Strategy

**Time:** 20 min (plus ~30 min of Claude processing)
**Goal:** Generate your full creative strategy — personas, scoring, micro personas, and strategy map.

---

## What This Skill Does

The Creative Strategy skill takes all your data and produces:

1. **8-15 proto-personas** clustered from your data
2. **Scoring** on cold traffic convertibility and market scalability
3. **Your top 5 personas** selected (you approve)
4. **Detailed persona profiles** (before/after state, pains, desires, triggers, language bank)
5. **Micro personas** — 2-4 per macro persona, each with a distinct fear/motivator/bias
6. **Strategy map** — specific angles, hooks, formats, and actors per persona

This is the brief every script will eventually reference. It's the most important output of the entire system.

---

## The Prompt

Paste this into Claude:

```
I want to run a full creative strategy for my business.

1. Read my business context from context/business.md
2. Read all sales call transcripts in knowledge-base/sales-calls/
3. Read all files in knowledge-base/research/
4. Read my winning ads in knowledge-base/winning-ads/
5. Run the Creative Strategy skill (skills/creative-strategy/SKILL.md)

Before you start, give me a quick read on the data you have:
- How many transcripts, how diverse
- How much proof
- How many competitors researched

Then walk me through the full process. Don't skip any steps. Do pause
at each human checkpoint (persona selection, persona profile approval,
micro persona approval, strategy map).

Frame everything as hypothesis, not conclusion. These are bets. The
ad account will validate or invalidate them.

Before you begin the tagging phase, ask me for my thesis — which customer
types do I think are the strongest opportunities and why? Treat that as
a hypothesis to validate against the data.
```

---

## What To Expect

Claude will work through this in stages. At each stage, it pauses for your approval:

### Stage 1: Data Validation
Claude reads everything and flags gaps. Example: "Transcript data skews heavily toward [type]. Persona scoring will weight accordingly."

### Stage 2: Tagging
Claude tags every quote, insight, and data point across 9 dimensions (pains, desires, triggers, language, etc.). This takes 5-10 min of processing.

### Stage 3: Proto-Personas
You'll see 8-15 clusters. Each has a name, a primary pain, a desired outcome, and volume of supporting data.

### Stage 4: Scoring
Each persona scored on:
- Cold Traffic Convertibility (1-10)
- Market Scalability (1-10)

### Stage 5: Persona Selection
You pick 5. Claude suggests based on scores, but you can override.

**What to do here:** Trust the scores but don't blindly follow. If a persona feels wrong to you based on experience, flag it. If you want to include a low-scored one as a bet, do it — just know it's a hypothesis.

### Stage 6: Detailed Persona Profiles
Full profile for each of the 5. Before state, after state, pains (ranked), desires (ranked), triggers, matched value props, matched proof assets, hooks, language bank, cognitive biases, veilance zones, self-concept anchors.

### Stage 7: Micro Personas
Each macro persona gets split into 2-4 micros (e.g., P1.1, P1.2, P1.3). Different fears, motivators, awareness levels.

### Stage 8: Strategy Map
For each micro persona: specific angles, awareness-level hooks, format assignments, actor archetypes.

---

## How To Challenge The AI

If something feels off, push back. Claude should defend or revise.

**Good challenges:**
- "Persona 3 feels too similar to Persona 1. What's actually different between them?"
- "You scored this persona high on convertibility, but I've tried this market and it doesn't convert. What's your reasoning?"
- "This micro persona's core fear doesn't match what I hear on calls. Can you re-check the data?"

Claude will either defend with evidence or revise. Both are good.

---

## How Long This Takes

Plan for 30-45 minutes total. You'll be answering questions and approving at each stage, so don't rush it. Have a coffee.

---

## Save The Output

When the strategy map is complete, Claude will write it to `outputs/creative-strategy-[date].md` automatically. You can reference this brief for every script you write.

---

## ✅ Checkpoint

- [ ] Creative Strategy skill ran end-to-end
- [ ] 5 macro personas approved
- [ ] Micro personas approved
- [ ] Strategy map complete
- [ ] Full brief saved to `outputs/creative-strategy-[date].md`
- [ ] Scripting Readiness Gate passed (Claude confirms brief is ready for Script Generator)

Move to **Step 11 — Generate Your First Scripts**.
