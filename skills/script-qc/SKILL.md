---
name: script-qc
description: Use this skill whenever a user wants to QC, review, check, audit, or get feedback on ad scripts, ad copy, storyboards, or creative scripts before sending to a client or launching. Triggers include any mention of "QC this copy", "review these scripts", "check these ads", "audit this copy", "is this ready to send", "feedback on these scripts", or any request to evaluate ad script quality. This skill analyzes ad copy against direct response frameworks and the client's creative strategy brief, then produces a structured feedback report identifying what's wrong and what needs to change. It does NOT rewrite copy — it only gives feedback. Do not use this skill for writing or generating ad scripts. Use the Ad Script & Storyboard Generator for that.
---

# Ad Script QC

Analyze ad script copy against direct response frameworks and the client's creative strategy brief. Produce a structured feedback report that tells the copywriter exactly what's wrong and what needs to change — without rewriting a single word.

## When To Use This Skill

- User asks to QC, review, check, or audit ad scripts or ad copy
- User asks "is this ready to send to the client"
- User asks for feedback on storyboards or creative scripts
- User pastes ad scripts and asks what needs to be fixed
- User wants to evaluate a batch of scripts before launch

Do NOT use this skill when:
- User wants to write or generate new ad scripts (use the Ad Script & Storyboard Generator)
- User wants copy rewritten or edited (this skill only gives feedback)
- User is building a creative strategy brief (use the Creative Strategy Brief Builder)

## What You Need Before Starting

1. **Ad Scripts / Storyboards** — The actual copy being reviewed. Pasted directly by the user. Any format accepted (storyboard tables, raw scripts, numbered concepts, etc.)
2. **Creative Strategy Brief** — The completed brief for this client, containing persona profiles, creative strategy map, winning ads, offer details, and customer language tags. Pasted directly by the user.

Both inputs should be provided before running. If either is missing, follow the escalation process in Step 1 below.

## Process

### Step 1: Input Validation

Check what the user has provided.

**If ad scripts are provided but no creative strategy brief:**
- Ask for the brief: "To run a full QC, I need the Creative Strategy Brief for this client. It contains the persona profiles, angles, awareness levels, winning ads, and customer language I check the scripts against. Can you paste it in?"
- If the user does not provide the brief after being asked, switch to **Reduced QC Mode**. In this mode, you can run these checks WITHOUT the brief: Hook Quality (Check 2), AI-isms Detection (Check 4), Body Structure Alignment (Check 5 — can assess awareness-level structure if metadata is present), Open Loop & Hold Rate (Check 6), Value Equation Coverage (Check 7), Traffic Qualification (Check 8), CTA Quality (Check 9), and Recordability (Check 10). You CANNOT run: Specificity (Check 1 — needs brief for persona-specific detail), Avatar Alignment (Check 3), Format Diversity (Check 11), Angle Diversity (Check 12), or Awareness Distribution (Check 13) without the brief. Tell the user: "Running reduced QC without the brief. I can check hooks, AI patterns, body structure, open loops, value equation, traffic qualification, CTAs, and recordability. I can't evaluate persona alignment, specificity against the brief, or batch-level diversity without the strategy brief."

**If scripts are missing metadata** (no persona assignment, no angle label, no awareness level, no concept ID):
- Flag it: "These scripts don't have persona, angle, or awareness level metadata attached. Can you add that so I can check alignment against the brief?"
- If the user proceeds without metadata, do what you can — but note in the report that alignment checks were limited.

**If the brief is incomplete** (missing personas, or missing winning ads, or missing customer language tags):
- Flag exactly what is missing: "The brief is missing [winning ads / customer language tags / persona profiles]. This limits what I can check. Do you want me to proceed with what's available?"
- If the user says proceed, work with what you have and note the limitations in the report.

### Step 2: Brief Ingestion (Full QC Mode Only)

Read the entire Creative Strategy Brief and extract:
- **Persona Profiles**: Names, pains (ranked), desires (ranked), before/after states, barriers, objections, triggers, customer language tags, matched proof assets
- **Awareness-Segmented Verbatim Language Bank**: For each persona, the numbered verbatim phrases sorted by awareness level (Unaware / Problem-Aware / Solution-Aware / Product-Aware). Use these to verify Customer Language alignment in scripts.
- **Creative Strategy Map**: Which persona/angle/awareness level/format combinations were assigned, including named hook types from the Hook Formulas library
- **Winning Ads**: Previous winning scripts or references — note their tone, pacing, structure, hook style, CTA approach
- **Offer Details**: Core deliverables, unique mechanism, price point, proof assets
- **Customer Language**: Verbatim phrases, metaphors, expressions from research (should be segmented by awareness level per the brief builder's output)

Hold all of this as your evaluation baseline. Every piece of feedback you give must be traceable back to something in the brief or the reference frameworks below.

### Step 3: Per-Script Analysis

For each script in the batch, run these four checks in order. Rate each check as **PASS**, **NEEDS WORK**, or **FAIL**.

---

**CHECK 1: Specificity**

<instructions>
Read the script and mentally remove all metadata (persona name, angle label, concept ID). Then ask:

- Does the copy clearly speak to ONE specific type of person, or could it be for anyone?
- Are the pains, desires, and triggers mentioned specific to the assigned persona, or are they generic?
- Are there concrete details (numbers, timelines, scenarios, named outcomes) or is it vague?
- If you swapped the persona name, would the script still make sense? If yes, it fails.

What to look for:
- Generic phrases like "grow your business", "take it to the next level", "achieve your goals" — these are specificity failures
- Claims without numbers or proof anchors
- Pain points that could apply to any persona in the brief, not just the assigned one
- Language that sounds like it was written for a category, not a person

Rate:
- PASS: The script is clearly written for one specific persona. You could not swap it to another persona without rewriting.
- NEEDS WORK: Some sections are specific but others fall back to generic language. Fixable with targeted edits.
- FAIL: The script could be for anyone. No specificity to the assigned persona.

For NEEDS WORK or FAIL: Identify the exact lines or sections that are generic and explain what specific detail from the persona profile should replace them.
</instructions>

---

**CHECK 2: Hook Quality**

<instructions>
Evaluate each hook in the script (there should be multiple variations — typically 3). Assess each hook independently.

Check each hook against these criteria:
1. **Scroll-stopping power**: Would this make the target persona stop scrolling at 11pm? Is it jarring, interesting, or emotionally charged enough to interrupt?
2. **Audience qualification**: Does the hook contain a word or phrase that lets the ideal customer know this is for them? A hook that appeals to "anyone" is a weak hook.
3. **Awareness level match**: Does the hook style match the assigned awareness level?
   - Unaware: Leads with a symptom or relatable moment, NOT a problem label
   - Problem-Aware: Calls out the problem, empathizes, hints at a solution
   - Solution-Aware: Leads with why other approaches fail, introduces the unique mechanism
   - Product-Aware: Leads with proof, addresses specific hesitations
   - Most Aware: Direct offer, testimonial, urgency
4. **Friend test**: Would this persona say this to their friend? If it sounds like a Facebook ad, it fails.
5. **Genuine distinction**: Are the hook variations actually different from each other? Three variations of the same idea in different words is NOT three hooks. Each hook should use a different entry point — a different pain, trigger, or emotional angle.
6. **Open loop potential**: Does the hook create curiosity or an unresolved question that pulls the viewer into the body?
7. **Proof in the hook**: Where possible, does the hook include specific proof (numbers, names, results) for instant credibility?

Rate:
- PASS: Hooks are specific, awareness-level appropriate, distinct from each other, and would genuinely stop the scroll for the target persona.
- NEEDS WORK: Some hooks are strong but others are weak, or the hooks are too similar to each other, or the awareness level is mismatched.
- FAIL: Hooks are generic, sound like marketing copy, don't qualify the audience, or all use the same entry point.

For NEEDS WORK or FAIL: Identify which specific hooks are weak and why. Reference the specific hook quality criteria that are not being met. Do NOT rewrite the hooks — just explain what's wrong.
</instructions>

---

**CHECK 3: Avatar Alignment (Full QC Mode Only)**

<instructions>
This check requires the Creative Strategy Brief. Skip this check in Reduced QC Mode.

Compare the script against the assigned persona profile from the brief:

1. **Pain/desire match**: Are the pains and desires referenced in the script actually from the assigned persona's profile? Or has the writer used pains from a different persona or made up pains not in the research?
2. **Customer language**: Is the script using language that matches the customer language tags from the persona profile? Or has the writer paraphrased the customer's words into marketing language?
3. **Proof asset match**: If the script references testimonials, case studies, or results — do those match the proof assets assigned to this persona in the brief? Are any testimonials or proof points fabricated (not found in the brief)?
4. **Trigger alignment**: Does the script tap into the triggers identified for this persona, or is it using generic motivational prompts?
5. **Before/after state**: Does the script accurately represent the persona's before state (current situation) and after state (desired outcome) as defined in the brief?

Rate:
- PASS: Script clearly maps to the assigned persona. Pains, language, proof, and triggers all trace back to the brief.
- NEEDS WORK: Script is broadly aligned but uses some language or pain points not from the persona profile, or misses key elements.
- FAIL: Script does not match the assigned persona. Wrong pains, wrong language, fabricated proof, or could easily belong to a different persona.

For NEEDS WORK or FAIL: Identify exactly where the script deviates from the persona profile. Quote the specific section of the script and reference the specific element from the brief it should be aligned to. If proof or testimonials appear fabricated, flag them explicitly: "This testimonial/case study does not appear in the brief. Confirm it exists or replace with [INSERT TESTIMONIAL — persona match criteria: X]."
</instructions>

---

**CHECK 4: AI-isms Detection**

<instructions>
Scan the entire script for the following 13 AI language patterns. Flag every instance found, regardless of context. The writer decides whether to keep or remove — your job is to make sure they see it.

**Pattern 1: The Reframe Flip**
"It's not X, it's Y" / "This isn't just X — it's Y" / "Stop X. Start Y."
Clean binary contrasts that real people rarely use.

**Pattern 2: The Rhetorical Reveal**
"The reason? It's X." / "The secret? X." / "The truth? X."
Question-then-answer cadence. The single biggest AI tell in DR copy.

**Pattern 3: The Pseudo-Intimate Opener**
"Here's the thing:" / "Let me be honest:" / "Can I be real with you?"
Stalling before the actual point while pretending to earn trust.

**Pattern 4: The Forced Reflection**
"Think about it." / "Sound familiar?" / "Let that sink in."
Dropped after claims like mic drops nobody asked for.

**Pattern 5: The Dramatic Fragment List**
"No gimmicks. No fluff. Just results." / "Simple. Proven. Effective."
Three-word fragments in a row. Dead giveaway.

**Pattern 6: The Upgrade Reframe**
"This isn't a course — it's a transformation." / "We don't sell X — we deliver Y."
Same skeleton as the flip but dressed up as positioning.

**Pattern 7: The Bonus Reveal**
"And the best part?" / "But here's where it gets interesting:" / "Oh, and did I mention?"
Manufactured transition signals.

**Pattern 8: The Welcome Mat**
"Welcome to [concept]." / "Say goodbye to X and hello to Y." / "It's time to [desired outcome]."
Sound like taglines on a brochure, not conversation.

**Pattern 9: The Inclusive Qualifier**
"Whether you're a [X] or a [Y]..."
Trying to broaden the audience but sounds templated.

**Pattern 10: The Self-Answering Question Chain**
"What if you could [outcome]? What if [benefit]? What if [bigger benefit]?"
Stacking hypotheticals without ever making a real claim.

**Pattern 11: The Empathy Mirror**
"You've tried everything. You're exhausted. You just want something that works."
The "I see you" sequence listing three pain points in parallel structure. Real empathy doesn't come in triplets.

**Pattern 12: The CTA Cushion**
"Ready to [desired outcome]?" / "You deserve [X]."
These close out AI copy almost every single time.

**Pattern 13: The Authority Pivot**
"In fact, ..." / "Actually, ..." / "You see, ..."
Correcting a belief the reader never expressed just so the copy can look smart.

For each instance found, report:
- Which pattern it matches
- The exact text from the script
- Where in the script it appears (hook, lead, body, CTA)

Note: Flagging an AI-ism does not automatically mean FAIL. This is an awareness flag. The writer decides whether the usage is intentional or lazy. But every instance must be surfaced.

Rate:
- PASS: Zero or 1 minor instances found. Script reads naturally.
- NEEDS WORK: 2-4 instances found. Script has AI fingerprints but is mostly natural.
- FAIL: 5+ instances found, or the AI patterns dominate the tone of the script. Script sounds like it was generated, not written.
</instructions>

---

---

**CHECK 5: Body Structure Alignment**

<instructions>
This check evaluates whether the script's body structure matches the awareness level and format.

Reference the body structure tools from the Ad Script & Storyboard Generator:
- Tool A (Full DR Framework) — best for long-form, cold traffic, complex offers
- Tool B (Education-First) — best for Unaware audiences, mechanisms that need explanation
- Tool C (Story-Style) — best for UGC/founder ads, Problem-Aware audiences
- Tool D (Proof-Stack) — best for Product-Aware/Most Aware, testimonial formats
- Tool E (Short-Form Punch) — best for under 30 seconds, Reels/TikTok

Check:
1. Does the script's body structure match what the awareness level requires?
   - Unaware scripts must educate before pitching. If the product/solution appears in the first 40% of the ad, it's structurally wrong for Unaware.
   - Problem-Aware scripts should spend significant time on failed solutions before introducing the mechanism.
   - Product-Aware scripts should lead with proof and objection handling, not education.
2. Does the script reveal the solution too early? For Unaware and Problem-Aware audiences, the solution should appear no earlier than the halfway point. The hook must NOT reveal the solution.
3. Are features translated into benefits? For Unaware and Problem-Aware audiences, feature names should not appear in the copy. Only plain-language benefit descriptions.
4. **Awareness Curve:** Does awareness increase gradually through the script, or does it staircase? Check for hard bridges — sudden jumps from education to pitch and back. Each hard bridge is a retention cliff in the data. The ideal ad starts at zero product awareness and creeps up smoothly to the CTA. A staircase pattern (education → hard pitch → education → hard pitch) is a structural failure.
5. **Copy-to-Creative Awareness Mismatch** (applies to statics and any ad where visual and copy are distinct): Do the visual/static and the primary text assume the same awareness level? A Product-Aware image (branded product shot, assumes recognition) paired with Problem-Aware copy (educating on the category) is a mismatch — neither audience is properly served. If visual direction is specified in the storyboard, check it matches the copy's awareness level.

Rate:
- PASS: Body structure matches the awareness level. Solution reveal is appropriately timed. Features are translated. Awareness progresses smoothly. Visual and copy are congruent.
- NEEDS WORK: Structure is close but solution appears too early, some features are untranslated, or a minor awareness staircase exists that's fixable with restructuring.
- FAIL: Pitch-first structure on an Unaware/Problem-Aware ad, feature-heavy copy with no benefit translation for cold traffic, severe staircase pattern, or visual/copy awareness mismatch.

For NEEDS WORK or FAIL: Identify the specific structural problem — including where any staircase bridges occur and whether the visual and copy awareness levels are mismatched — and which awareness-level body structure would be more appropriate.
</instructions>

---

**CHECK 6: Open Loop & Hold Rate**

<instructions>
Check whether the script uses open loops to sustain attention through the body.

1. Does the hook or lead plant an unresolved question that forces the viewer to keep watching?
2. Is the loop sustained through the body (not resolved too early)?
3. Does the CTA close the primary loop?
4. Does the hook avoid revealing the solution? If the audience knows what's being sold within the first 3 seconds, there's no reason to keep watching.

Rate:
- PASS: Clear open loop planted early, sustained through body, resolved at CTA. Solution not revealed in hook.
- NEEDS WORK: Some tension exists but the loop resolves too early, or the hook gives away too much.
- FAIL: No open loop. Script is a linear pitch with no unresolved question sustaining attention. Or the hook reveals the solution immediately.

For NEEDS WORK or FAIL: Identify where the loop breaks or where the solution is revealed too early.
</instructions>

---

**CHECK 7: Value Equation Coverage**

<instructions>
Check whether the ad body addresses all four levers of the value equation:

1. **Dream Outcome** — Is the result specific and vivid? "Get in shape" fails. "Drop 20 pounds, fit into your college jeans" passes.
2. **Perceived Likelihood** — Is there proof this actually works? Mechanism explanation, specific testimonials, numbers. Vague claims fail.
3. **Time Delay** — Does the script address how quickly they'll see results? Milestones and early wins reduce perceived time delay.
4. **Effort & Sacrifice** — Does the script address how easy this is to implement? "You just read the hooks on camera" passes. No mention of effort fails.

Not every ad format needs all four at equal depth (a 30-second Reel won't have space for all four). But for ads over 45 seconds targeting Problem-Aware or colder audiences, all four should be present.

Rate:
- PASS: All four levers present and specific.
- NEEDS WORK: 2-3 levers present. Missing lever(s) identified.
- FAIL: Only dream outcome present. No proof, no timeline, no effort reduction.

For NEEDS WORK or FAIL: Identify which lever(s) are missing and where in the body they should appear.
</instructions>

---

**CHECK 8: Traffic Qualification**

<instructions>
Check whether each hook contains a qualifying term or phrase that ensures only the ICP would keep watching.

A hook about "YouTube" attracts vloggers, gamers, educators, and everyone else. A hook about "faceless YouTube channels running on a $30/video editing budget" attracts only the ICP. The qualifier tells Meta's pixel who is engaging, which improves delivery over time.

For each hook, identify:
- The qualifying term/phrase (or its absence)
- Whether a stranger outside the target persona would also think this hook is for them

Rate:
- PASS: Every hook contains a clear qualifier. Non-ICP viewers would self-select out.
- NEEDS WORK: Some hooks are qualified, others are too broad.
- FAIL: Hooks are generic enough to attract anyone. No qualifying language.

For NEEDS WORK or FAIL: Identify which hooks lack qualifiers and suggest what type of qualifier would work (niche term, price point, role, life-situation detail).
</instructions>

---

**CHECK 9: CTA Quality**

<instructions>
Evaluate the CTA against the loop-closing formula: [Action verb] + [Vehicle/format] + [Specific deliverable].

Check:
1. Does the CTA close the open loop from the hook? The resolution of the hook's unresolved question should be the action the CTA asks for.
2. Does the CTA promise a specific deliverable, or just ask for a click? "Click the link below" fails. "Click the link to book a free audit where we'll show you the exact 3-video sequence" passes.
3. Is the CTA strength appropriate for the awareness level? Unaware = soft (learn more, download report). Problem-Aware = diagnostic (book an audit). Solution-Aware = demonstration. Product-Aware = trial/offer. Most Aware = direct purchase with urgency.

Rate:
- PASS: CTA closes the loop, promises a specific deliverable, and matches the awareness level.
- NEEDS WORK: CTA is decent but generic, or doesn't close the loop from the hook.
- FAIL: CTA is a throwaway "click the link" with no specific deliverable and no loop closure.

For NEEDS WORK or FAIL: Explain what's missing and reference the CTA formula.
</instructions>

---

**CHECK 10: Recordability**

<instructions>
Check whether the script is practically recordable by talent.

1. Is the word count within range for the assigned format? (Reference the Ad Formats Library if available. General guides: UGC selfie 120-200 words, Talking Head 180-300 words, B-Roll 60-120 words, Short-form 50-100 words.)
2. Is the maximum sentence length under 15 words for recorded formats (UGC, Talking Head, Testimonial)? Long, complex sentences cause stumbling during recording.
3. Could the talent read this in one take without a teleprompter? If there are tongue-twisters, jargon, or multi-clause sentences, flag them.

Rate:
- PASS: Word count is in range, sentences are short and readable, no recordability issues.
- NEEDS WORK: Slightly over on word count or a few sentences are too long. Easy fixes.
- FAIL: Significantly over word count, or sentences are consistently too long/complex for the assigned format.
</instructions>

---

### Step 4: Batch-Level Analysis

After completing per-script checks, step back and evaluate the full batch together.

---

**CHECK 11: Format Diversity (Full QC Mode Only)**

<instructions>
This check requires the Creative Strategy Brief. Skip this check in Reduced QC Mode.

Look at the formats assigned across all scripts in the batch. Compare against the format assignments in the creative strategy map.

Ask:
- Are multiple ad formats represented (e.g., talking head, UGC, VSL, listicle, story-based, screen recording, mashup)?
- Or do all scripts default to the same format?
- Does the format mix match what was specified in the strategy map?

If all scripts use the same format and the strategy map assigned multiple formats, flag it.
If the strategy map is not available but all scripts are the same format, note it as a potential concern.
</instructions>

---

**CHECK 12: Angle Diversity (Full QC Mode Only)**

<instructions>
This check requires the Creative Strategy Brief. Skip this check in Reduced QC Mode.

Look at the angles used across all scripts in the batch.

Ask:
- Are the scripts attacking different angles, or are multiple scripts essentially saying the same thing with different words?
- Would a stranger looking at all these ads say any two are "about the same thing"?
- Does the angle mix match what was specified in the strategy map?

If two or more scripts overlap significantly in their angle (same pain point, same entry point, same emotional territory), flag the overlap and identify which scripts are redundant.
</instructions>

---

**CHECK 13: Awareness Distribution**

<instructions>
Count how many scripts in the batch target each awareness level. Present as a table:

| Awareness Level | # Scripts | % of Batch | Benchmark |
|-----------------|-----------|------------|-----------|
| Unaware         |           |            | }~80%     |
| Problem-Aware   |           |            | }         |
| Solution-Aware  |           |            | ~10%      |
| Product-Aware   |           |            | }~10%     |
| Most Aware      |           |            | }         |

**Volume distribution benchmark:** ~80% of creative volume should target Unaware + Problem-Aware, ~10% Solution-Aware, ~10% Product-Aware + Most Aware. This is a starting benchmark — flex by account. But significant deviation should be flagged.

If Unaware + Problem-Aware combined is under 40% of total scripts, flag it: "Cold traffic creative is thin. The largest and cheapest audiences are Unaware and Problem-Aware. Consider adding more cold-traffic scripts to the batch before launch."

If Product-Aware + Most Aware exceeds 30% of total scripts, flag it: "Strategy is bottom-heavy. Post-Andromeda, Meta serves Product-Aware ads to a small warm pool — frequency will spike. Shift volume to Unaware and Problem-Aware to enable scale."

If all scripts target the same awareness level, flag it as a diversity issue regardless of which level it is.
</instructions>

---

### Step 5: Compile the QC Report

Structure the report exactly as follows:

<example>
# AD SCRIPT QC REPORT

**Client:** [Name from brief, or "Not provided"]
**Scripts Reviewed:** [Number]
**QC Mode:** [Full QC / Reduced QC (no brief)]
**Brief Completeness:** [Complete / Missing: list what's missing]

---

## PER-SCRIPT FEEDBACK

### [Concept ID or Script Label]
**Persona:** [Name] | **Angle:** [Name] | **Awareness Level:** [Level]

| Check | Rating | Summary |
|-------|--------|---------|
| Specificity | PASS / NEEDS WORK / FAIL | [1 sentence summary] |
| Hook Quality | PASS / NEEDS WORK / FAIL | [1 sentence summary] |
| Avatar Alignment | PASS / NEEDS WORK / FAIL / SKIPPED | [1 sentence summary] |
| AI-isms | PASS / NEEDS WORK / FAIL | [X instances found] |
| Body Structure | PASS / NEEDS WORK / FAIL | [1 sentence summary] |
| Open Loop | PASS / NEEDS WORK / FAIL | [1 sentence summary] |
| Value Equation | PASS / NEEDS WORK / FAIL | [Levers present / missing] |
| Traffic Qualification | PASS / NEEDS WORK / FAIL | [1 sentence summary] |
| CTA Quality | PASS / NEEDS WORK / FAIL | [1 sentence summary] |
| Recordability | PASS / NEEDS WORK / FAIL | [Word count + max sentence length] |

**Detailed Feedback:**

**Specificity:**
[If NEEDS WORK or FAIL: specific lines that are generic, what should replace them, referenced back to the brief or frameworks]

**Hook Quality:**
[If NEEDS WORK or FAIL: which hooks are weak, why, which criteria they fail against]

**Avatar Alignment:**
[If NEEDS WORK or FAIL: where the script deviates from the persona profile, specific references to the brief]

**AI-isms Found:**
[List each instance: pattern name, exact text, location in script]

**Body Structure (includes Awareness Curve + Copy-to-Creative Mismatch):**
[If NEEDS WORK or FAIL: which awareness-level body structure should be used, where the solution appears too early, which features need benefit translation. Also flag: any staircase bridges (hard jumps between awareness levels), the product reveal timing vs. the awareness level benchmark, and whether visual and copy are at the same awareness level.]

**Open Loop:**
[If NEEDS WORK or FAIL: where the loop breaks, where the solution is revealed too early, whether the CTA closes the loop]

**Value Equation:**
[If NEEDS WORK or FAIL: which of the 4 levers are missing (dream outcome, perceived likelihood, time delay, effort & sacrifice)]

**Traffic Qualification:**
[If NEEDS WORK or FAIL: which hooks lack qualifiers, what type of qualifier to add]

**CTA Quality:**
[If NEEDS WORK or FAIL: what's missing from the CTA formula, whether it closes the loop]

**Recordability:**
[If NEEDS WORK or FAIL: word count vs target, longest sentence length, specific sentences that are too complex]

---

[Repeat for each script]

---

## BATCH-LEVEL ASSESSMENT

### Format Diversity
[Assessment of format mix across all scripts. Flag if all scripts use the same format.]

### Angle Diversity
[Assessment of angle mix. Flag any overlapping scripts and explain where they overlap.]

### Awareness Distribution
[Table showing scripts per awareness level. Flag if cold traffic creative is under 40%.]

### Cross-Script Redundancy
[Flag any two scripts that a stranger would say are "about the same thing."]

---

## SUMMARY

**Scripts ready to send:** [List concept IDs that passed all checks]
**Scripts needing revision:** [List concept IDs with NEEDS WORK ratings and the primary issue for each]
**Scripts requiring significant rework:** [List concept IDs with FAIL ratings and the primary issue for each]
</example>

## Quality Standards

The QC report passes its own quality check when:
- Every piece of feedback is specific, actionable, and traceable to a framework or principle from the reference material or the creative strategy brief
- No feedback is vague opinion (e.g., "this could be better" without saying how or why)
- No issues are fabricated — if a script is strong, the report says so
- AI-ism flags include the exact text and pattern name, not just "there are some AI patterns"
- The report clearly distinguishes between per-script issues and batch-level issues
- Limitations are noted when operating in Reduced QC Mode or with an incomplete brief

## Known Failure Modes & How To Handle Them

| Failure Mode | What It Looks Like | What To Do |
|---|---|---|
| No brief provided | User pastes scripts but no creative strategy brief | Ask for the brief. If they proceed without it, switch to Reduced QC Mode and note limitations. |
| Incomplete brief | Brief is missing personas, winning ads, or customer language | Flag exactly what's missing. Proceed if prompted. Note in report which checks were limited. |
| Scripts missing metadata | No concept IDs, persona labels, angle labels, or awareness levels on scripts | Ask the user to add metadata. If they proceed without it, do what you can and note that alignment checks were limited. |
| Fabricated proof in scripts | Script references testimonials or case studies not found in the brief | Flag explicitly: "This testimonial/case study does not appear in the brief. Confirm it exists or use a placeholder tag." |
| Non-standard script format | Scripts don't follow the storyboard table format — raw copy, no scene labels | Work with whatever format is provided. Evaluate the copy as-is. Note in the report if the format made certain checks harder to evaluate. |
| Single script submitted | Only one script, making batch-level checks impossible | Run per-script checks normally. Note that batch-level diversity checks require multiple scripts. |

## Constraints

- **Never rewrite or change copy.** This skill produces analysis and feedback only. If the user asks for rewrites, tell them to use the Ad Script & Storyboard Generator or revise manually based on the feedback.
- **Never fabricate issues.** If a script is strong, say so. Do not invent problems to justify the QC process.
- **Never make broad inferences about testimonials.** If a testimonial in the script does not appear in the brief, flag it as unverified. Do not assume it's fabricated — ask the user to confirm.
- **Never comment on visual direction or editing instructions.** This skill reviews written copy only. Ignore the Visual and Editing Instructions columns in storyboard tables.
- **Every piece of feedback must be traceable.** Reference the specific framework, checklist item, or brief element that supports the feedback. No gut-feel opinions.
- **Flag every AI-ism instance.** Even if the usage might be intentional. The writer decides whether to keep it — your job is to surface it.
- **Do not apply the ad copy training document as a rigid checklist.** Not every ad format will include every element listed in the training material. Evaluate based on what the specific format and awareness level requires, not a universal checklist.

## Output Format

A structured QC report following the exact template in Step 5 above. Delivered as text in the conversation. The report has three sections:

1. **Per-Script Feedback** — Individual ratings and detailed feedback for each script
2. **Batch-Level Assessment** — Format diversity, angle diversity, and redundancy checks across all scripts
3. **Summary** — Quick list of which scripts are ready, which need revision, and which need rework

## Reference Frameworks

This skill evaluates copy against the following frameworks. These are embedded in the training material and should be used as evaluation lenses, not rigid checklists:

- **Eugene Schwartz's 5 Awareness Levels** — for evaluating hook style and messaging strategy alignment
- **Hormozi's Value Equation** — Dream Outcome, Perceived Likelihood, Time Delay, Effort & Sacrifice — for evaluating whether the ad body addresses all four levers where appropriate
- **Great Leads (Masterson)** — Offer, Promise, Problem-Solution, Big Secret, Proclamation, Story — for evaluating lead type alignment
- **Hook Quality Criteria** — Scroll-stopping power, audience qualification, boldness, proof inclusion, uniqueness, specificity, curiosity creation
- **Open Loop Mechanics** — Whether hooks and leads create unresolved questions that sustain attention through the body
- **CTA Framework** — Action + Vehicle + Specific Deliverable formula, loop closure, awareness-level appropriate CTA strength
- **CPO Framework** — Circumstances, Problem, Outcome integration in ad bodies
- **Ad Body Checklist** — Proof and believability, open loop tension management, emotional amplification, clarity and flow
- **13 AI-ism Patterns** — The specific language patterns catalogued in Check 4 above

## Reference Files

Consult these files when available for more specific evaluation criteria:

- **Hook Formulas** (`references/hook-formulas.md`) — 10 named hook types with selection matrix by awareness level. Use to verify hook type is named and appropriate for the awareness level.
- **Ad Formats Library** (`references/ad-formats-library.md`) — Per-format specs (scene count, word count, pacing). Use to verify recordability and format compliance.
- **Body Structure Tools** (defined in `skills/script-generator/SKILL.md`, Phase 2 Step 5) — 5 named body structure tools (A through E) mapped to awareness levels. Use to verify body structure alignment.
