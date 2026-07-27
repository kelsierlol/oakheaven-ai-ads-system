# Step 11 — Generate Your First Scripts

**Time:** 15 min (plus ~20 min of Claude processing)
**Goal:** Turn your Creative Strategy brief into 5 production-ready ad storyboards.

---

## What This Skill Does

The Script Generator takes your strategy brief and produces:

1. **5 storyboards** (one per persona/angle combination)
2. **3 hook variations per storyboard** — each a different hook type, different entry point
3. **Lead + body structure + CTA** for each script
4. **Visual direction + editing instructions** per scene
5. **B-roll shot list** when applicable
6. **QC report** attached to every script (13 checks)

Every script that comes out has been quality-checked. Nothing failing QC gets presented to you.

---

## The Prompt

Paste this into Claude:

```
Write 5 ad scripts from my creative strategy brief.

Instructions:
- Reference the brief in outputs/creative-strategy-[date].md
- Reference the winning ads in knowledge-base/winning-ads/ for tone,
  pacing, and structural patterns
- Use Hook Formulas (skills/script-generator/references/hook-formulas.md) for hook types
- Use Ad Formats Library (skills/script-generator/references/ad-formats-library.md) for format specs
- Run Script QC on every script before presenting — I don't want to see
  anything that fails QC
- Include a mix of awareness levels — at least 2 for cold traffic
  (Unaware or Problem-Aware)
- Include format diversity — don't make all 5 the same format
- 3 hook variations per script, each a genuinely different hook type

Pick the 5 strongest persona/angle/format combinations from the strategy
map. Tell me which 5 you chose and why before writing.

Format outputs as full storyboards (scene | script | visual | editing)
and save the batch to outputs/ad-scripts-[date].md.
```

---

## What To Expect

### Stage 1: Selection
Claude picks 5 persona/angle/format combos from your strategy map and tells you why.

**What to do:** Approve the selection or override. If you want different combos, say so now.

### Stage 2: Script Writing
Claude writes each storyboard. For each script, you'll see:

- Concept Brief (persona, angle, awareness level, format, lead type)
- 3 Hook Variations (each with hook type, entry point, qualifier)
- Lead
- Full body with scenes
- CTA
- B-Roll shot list
- Value equation coverage check

### Stage 3: QC Report
For each script, you get a QC report with 13 checks. Anything failing gets fixed before it's shown to you.

### Stage 4: Batch Review
After all 5 scripts, Claude gives you:

- Format diversity check
- Angle diversity check
- Awareness distribution table
- Cross-script redundancy flag

---

## How To Read The Output

For each storyboard, check:

1. **Does the hook actually sound like the persona?** Read it aloud. Would that person say this to a friend? If not, it's too polished.

2. **Are the 3 hooks genuinely different?** Not three versions of the same idea in different words. Each hook should hit a different pain, trigger, or emotional angle.

3. **Does the body deliver on the hook's promise?** If the hook opens a loop about "why X didn't work," the body better explain why. If it drifts to a different angle, it fails.

4. **Is the CTA specific?** "Click the link below" fails. "Click the link to book a 10-minute strategy call where we'll map your top 3 lead gen gaps" passes.

5. **Is the script recordable?** Sentences under 15 words for UGC formats. Could someone say this in one take?

---

## Revisions

If a script isn't right, tell Claude specifically what's wrong:

**Good feedback:**
- "Hook B sounds like a Facebook ad. Make it feel like a voice note to a friend."
- "The body drifts into a different persona's pain point. Stay on P2.1's core fear."
- "CTA doesn't close the loop from the hook. Rewrite so the action resolves the question."

**Bad feedback:**
- "I don't like it." (No info — Claude can't fix this.)
- "Make it better." (Claude doesn't know what "better" means to you.)

---

## Save The Output

Claude will write everything to `outputs/ad-scripts-[date].md` automatically. Your storyboards live here — this is what your video editor or production team gets.

---

## ✅ Checkpoint

- [ ] 5 storyboards produced
- [ ] Each script has 3 hook variations
- [ ] All scripts passed QC
- [ ] Format and angle diversity is present (not all the same)
- [ ] At least 2 scripts target cold traffic (Unaware or Problem-Aware)
- [ ] Output saved to `outputs/ad-scripts-[date].md`

Move to **Step 12 — Read The QC Report & Iterate**.
