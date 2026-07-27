---
name: ai-slop-remover
description: Use this skill whenever a user wants to QC, review, check, audit, or get feedback on ANY piece of written copy before publishing, sending, or delivering. Triggers include any mention of "QC this", "review this copy", "check this", "audit this", "is this ready to send", "does this sound like AI", "de-slop this", "clean this up", or any request to evaluate copy quality. Works on any format: emails, landing pages, LinkedIn posts, sales pages, webinar scripts, proposals, cold DMs, lead magnets, Slack messages, newsletters, website copy, whatever. This skill analyzes copy against direct response frameworks and produces a structured feedback report identifying what's wrong and what needs to change. It does NOT rewrite copy. It only gives feedback.
---

# AI Slop Remover

Analyze any piece of written copy for AI patterns, weak structure, and lazy writing. Produce a structured feedback report that tells the writer exactly what's wrong and what needs to change, without rewriting a single word.

## When To Use This Skill

- User asks to QC, review, check, or audit any written copy
- User asks "does this sound like AI" or "is this ready to send"
- User pastes copy and asks what needs to be fixed
- User wants feedback on any written deliverable before it goes out
- User asks to "de-slop" or "clean up" a piece of copy

Do NOT use this skill when:
- User wants copy rewritten or edited (this skill only gives feedback)
- User wants new copy generated from scratch
- User is reviewing ad scripts specifically with a creative strategy brief (use AdQC for that)

## What You Need Before Starting

1. **The Copy** — whatever's being reviewed. Pasted directly by the user. Any format accepted.
2. **Context (optional but improves accuracy)** — who the audience is, what the piece is for, where it's being published, what action it's trying to drive. If provided, enables deeper checks. If not provided, run every check you can without it.

## Process

### Step 1: Input Validation & Format Detection

Read the copy and identify:
- **Format**: What type of copy is this? (email, landing page, LinkedIn post, sales page, cold DM, proposal, lead magnet, newsletter, website section, webinar script, Slack message, other)
- **Approximate length**: Word count and whether this is short-form (<200 words), mid-form (200-800 words), or long-form (800+ words)
- **Apparent purpose**: What is this copy trying to do? (sell, educate, nurture, convert, introduce, persuade, announce)
- **Apparent audience**: Who is this written for, based on the content? (Note: if the user provided context, use that instead of guessing)

If the copy is extremely short (under 50 words), note that some checks will be limited. Still run every check that applies.

### Step 2: Context Ingestion

If the user provided audience, purpose, or platform context, hold it as your evaluation baseline.

If no context was provided, state: "Running without audience/purpose context. I'll evaluate against general copy quality frameworks. Providing context (who this is for, where it's going, what action you want) would make the feedback sharper."

Then proceed. Do not ask twice. Do not block on missing context.

### Step 3: Per-Piece Analysis

Run these 8 checks in order. Rate each as **PASS**, **NEEDS WORK**, or **FAIL**.

---

**CHECK 1: AI-isms Detection**

<instructions>
This is the centerpiece. Scan the entire piece for the following 13 AI language patterns. Flag every instance found, regardless of context. The writer decides whether to keep or remove. Your job is to make sure they see it.

**Pattern 1: The Reframe Flip**
"It's not X, it's Y" / "This isn't just X, it's Y" / "Stop X. Start Y."
Clean binary contrasts that real people rarely use in natural writing.

**Pattern 2: The Rhetorical Reveal**
"The reason? It's X." / "The secret? X." / "The truth? X."
Question-then-answer cadence. The single biggest AI tell in written copy.

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
"This isn't a course, it's a transformation." / "We don't sell X, we deliver Y."
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

**Additionally, flag these general AI tells that appear across all copy types:**

**Pattern 14: The Buzzword Stack**
"Leverage", "streamline", "optimize", "cutting-edge", "game-changer", "next-level", "revolutionary", "seamless", "robust", "holistic"
Corporate filler words that say nothing specific. One is fine in context. Three or more in a piece means the copy is padding, not communicating.

**Pattern 15: The Throat-Clear Opener**
"In today's [anything]..." / "In the world of [anything]..." / "When it comes to [anything]..."
Opening with a panoramic zoom-out that delays the actual point. Real writing starts where the topic starts.

**Pattern 16: The Diplomatic Hedge**
"It's important to note that..." / "It's worth mentioning..." / "It should be noted..."
Filler phrases that add zero information. If it's important, just say the thing.

**Pattern 17: The Listicle Connector**
"Furthermore," / "Additionally," / "Moreover,"
Mechanical transition words that no human uses in natural writing. Real transitions come from the logic of the argument, not from conjunctions bolted between paragraphs.

**Pattern 18: The False Excitement**
Excessive exclamation marks, "Exciting news!", "We're thrilled to announce!", "This is huge!"
Telling the reader to be excited instead of writing something that makes them excited.

For each instance found, report:
- Which pattern it matches
- The exact text from the copy
- Where in the piece it appears (opening, body, close, headline, subhead, CTA)

Rate:
- PASS: 0-1 minor instances. Copy reads like a human wrote it.
- NEEDS WORK: 2-5 instances. AI fingerprints present but mostly natural.
- FAIL: 6+ instances, or the AI patterns dominate the tone. Copy sounds generated, not written.
</instructions>

---

**CHECK 2: Specificity**

<instructions>
Read the copy and ask:

- Does this speak to ONE specific type of person, or could it be for anyone?
- Are the pains, desires, and situations mentioned concrete and specific, or generic?
- Are there real details (numbers, timelines, scenarios, named outcomes) or is it vague?
- If you changed the audience label, would the copy still work? If yes, it's not specific enough.

What to look for:
- Generic phrases like "grow your business", "take it to the next level", "achieve your goals", "unlock your potential"
- Claims without numbers or proof
- Pain points so broad they could apply to anyone
- Language that sounds like it was written for a category, not a person

Rate:
- PASS: The copy is clearly written for a specific audience. You could not swap the audience without rewriting.
- NEEDS WORK: Some sections are specific but others fall back to generic language. Fixable with targeted edits.
- FAIL: The copy could be for anyone. No specificity to a real audience.

For NEEDS WORK or FAIL: Identify the exact lines or sections that are generic and explain what kind of specific detail should replace them.
</instructions>

---

**CHECK 3: Hook Quality**

<instructions>
Evaluate the opening of the piece. The "hook" varies by format:
- Email: subject line + first 1-2 sentences
- LinkedIn post: first 2-3 lines (above the fold)
- Landing page: headline + subheadline
- Sales page: headline + lead section
- Cold DM: entire first message
- Newsletter: subject line + opening paragraph
- Any other format: the first thing the reader sees

Check against these criteria:

1. **Attention**: Would the target reader stop and read this, or scroll past? Is it interesting, specific, or emotionally charged enough to interrupt whatever they were doing?
2. **Qualification**: Does the opening contain a word or phrase that lets the right reader know this is for them? An opening that appeals to "anyone" is weak.
3. **Earned continuation**: Does the opening earn the next sentence? Is there a reason to keep reading, or has it already said everything?
4. **Friend test**: Would a real person say this to a colleague or friend? If it sounds like marketing copy, it fails.
5. **Proof or specificity**: Where possible, does the opening include something concrete (a number, a name, a result, a scenario) for instant credibility?

Rate:
- PASS: Opening is specific, earns the next line, qualifies the reader, and sounds human.
- NEEDS WORK: Opening has some strength but is too broad, too generic, or gives everything away upfront.
- FAIL: Opening is forgettable, sounds like marketing, doesn't qualify anyone, or gives no reason to keep reading.

For NEEDS WORK or FAIL: Explain which criteria are not being met. Do NOT rewrite the hook.
</instructions>

---

**CHECK 4: Structure & Flow**

<instructions>
Evaluate whether the piece is structured for its format and purpose.

For persuasive/sales copy (landing pages, sales pages, emails selling something, webinar pitches):
1. Does the piece move through awareness levels appropriately? (Problem first, then solution, then offer, not the reverse)
2. Is the solution/product/offer revealed too early? For cold audiences, the solution should not appear in the first third.
3. Are features translated into benefits? Feature names without benefit translation are lazy.
4. Does awareness increase gradually, or does it staircase? (Education then hard pitch then education then hard pitch is a structural failure)

For nurture/relationship copy (newsletters, LinkedIn posts, thought leadership):
1. Does the piece have a clear through-line, or does it meander?
2. Is there a single core idea, or is it trying to say 5 things at once?
3. Does it build to something (an insight, a takeaway, a shift in thinking)?

For transactional/operational copy (cold DMs, proposals, announcements):
1. Is the purpose clear within the first 2 sentences?
2. Is it scannable? Can someone get the point in 10 seconds?
3. Is there unnecessary preamble before the actual ask or information?

Rate:
- PASS: Structure matches the format and purpose. Information flows logically. Reader is led, not lost.
- NEEDS WORK: Structure is close but has pacing issues, reveals too early, meanders in the middle, or tries to do too much.
- FAIL: No clear structure. Information is dumped, not sequenced. Reader has no reason to keep going after the first paragraph.

For NEEDS WORK or FAIL: Identify the specific structural problem and where it occurs.
</instructions>

---

**CHECK 5: Open Loop & Hold Rate**

<instructions>
Check whether the copy creates and sustains reasons to keep reading.

1. Does the opening plant an unresolved question, tension, or curiosity gap?
2. Is that tension sustained through the body (not resolved too early)?
3. Does the close resolve the primary loop?
4. For longer pieces: are there secondary loops that maintain momentum through the middle?

This applies differently by format:
- Short-form (<200 words): One loop is sufficient. The opening should create it, the close should resolve it.
- Mid-form (200-800 words): Primary loop from opening plus at least one mid-piece tension point.
- Long-form (800+ words): Multiple nested loops. If the reader can stop at any paragraph and feel "done," the loops are broken.

Rate:
- PASS: Clear tension created early, sustained through body, resolved at close.
- NEEDS WORK: Some tension exists but resolves too early, or the middle sags.
- FAIL: No open loop. The piece is a linear information dump with no unresolved question pulling the reader forward.

For NEEDS WORK or FAIL: Identify where the tension breaks or where the piece becomes skippable.
</instructions>

---

**CHECK 6: Value Equation Coverage**

<instructions>
Check whether the copy addresses the four levers of the value equation where relevant. This check applies most strongly to persuasive copy (sales pages, landing pages, emails with an offer, proposals). For pure content or relationship copy, note which levers are present but don't penalize for missing ones that aren't relevant.

1. **Dream Outcome** — Is the result specific and vivid? "Get better results" fails. "Cut your client onboarding from 3 weeks to 3 days" passes.
2. **Perceived Likelihood** — Is there proof this actually works? Mechanism explanation, specific results, social proof. Vague claims fail.
3. **Time Delay** — Does the copy address how quickly they'll see results? Milestones and early wins reduce perceived time delay.
4. **Effort & Sacrifice** — Does the copy address how easy this is to implement or adopt? If effort is never mentioned, the reader fills in the worst case.

Rate:
- PASS: All relevant levers present and specific.
- NEEDS WORK: 2-3 levers present. Missing lever(s) identified.
- FAIL: Only dream outcome present (or not even that). No proof, no timeline, no effort reduction.
- N/A: Copy type doesn't require value equation coverage (pure content, announcements, etc.)

For NEEDS WORK or FAIL: Identify which lever(s) are missing and where in the piece they should appear.
</instructions>

---

**CHECK 7: Audience Qualification**

<instructions>
Check whether the copy attracts the right people and repels the wrong ones.

A piece about "growing your business" attracts every freelancer, agency owner, SaaS founder, and life coach on the internet. A piece about "cutting CAC below $40 for DTC brands doing $50K-$200K/month" attracts only the target.

Check:
- Does the copy contain qualifying language that self-selects the right audience?
- Would someone outside the target audience also think this was written for them?
- Is there a niche term, price point, role, scenario, or life-situation detail that narrows the field?

This check is especially important for:
- LinkedIn posts (where algorithmic distribution sends copy to broad audiences)
- Cold outreach (where irrelevant messages damage sender reputation)
- Top-of-funnel content (where broad copy wastes ad spend or attention)

Rate:
- PASS: Copy contains clear qualifying language. Non-target readers would self-select out.
- NEEDS WORK: Some qualifying language present but the copy is still too broad in places.
- FAIL: Copy is generic enough to attract anyone. No qualifying language.

For NEEDS WORK or FAIL: Identify which sections lack qualifiers and suggest what type of qualifier would work.
</instructions>

---

**CHECK 8: CTA Quality**

<instructions>
Evaluate the call to action (or call to next-step, depending on the copy type).

Not every piece of copy has a traditional CTA. Adjust expectations by format:
- Sales/landing pages: Hard CTA expected. Should follow [Action verb] + [Vehicle] + [Specific deliverable].
- Emails: CTA or clear next step expected.
- LinkedIn posts: Soft CTA acceptable (comment prompt, DM invitation, link). But it should still be specific.
- Newsletters: CTA optional, but if present, should be specific.
- Cold DMs: Ask must be low-friction and specific.
- Proposals: Next step must be crystal clear.

Check:
1. Does the CTA close the loop from the opening? The resolution of whatever tension the opening created should connect to the action being asked for.
2. Does the CTA promise a specific deliverable or outcome, or just ask for a click/reply?
3. Is the CTA strength appropriate for the relationship stage? (Cold = soft ask. Warm = diagnostic/demo. Hot = direct purchase/commitment.)

Rate:
- PASS: CTA closes the loop, promises something specific, and matches the relationship stage.
- NEEDS WORK: CTA is present but generic, doesn't close the loop, or is mismatched to the stage.
- FAIL: CTA is a throwaway ("click here", "let me know", "check it out") with no specificity and no loop closure.
- N/A: Copy type doesn't require a CTA (pure content pieces, internal comms, etc.)

For NEEDS WORK or FAIL: Explain what's missing.
</instructions>

---

### Step 4: Compile the Report

Structure the report exactly as follows:

```
# COPY QC REPORT: AI SLOP REMOVER

**Format:** [Detected format]
**Length:** [Word count] ([short/mid/long]-form)
**Purpose:** [Detected or stated purpose]
**Audience:** [Stated by user, or "Not provided — evaluated against general frameworks"]

---

## RATINGS SUMMARY

| Check | Rating | Summary |
|-------|--------|---------|
| AI-isms | PASS / NEEDS WORK / FAIL | [X instances found] |
| Specificity | PASS / NEEDS WORK / FAIL | [1 sentence] |
| Hook Quality | PASS / NEEDS WORK / FAIL | [1 sentence] |
| Structure & Flow | PASS / NEEDS WORK / FAIL | [1 sentence] |
| Open Loop | PASS / NEEDS WORK / FAIL | [1 sentence] |
| Value Equation | PASS / NEEDS WORK / FAIL / N/A | [Levers present / missing] |
| Audience Qualification | PASS / NEEDS WORK / FAIL | [1 sentence] |
| CTA Quality | PASS / NEEDS WORK / FAIL / N/A | [1 sentence] |

---

## DETAILED FEEDBACK

### AI-isms Found
[List each instance: pattern name, exact text from copy, location in piece]
[If PASS: "Clean. No significant AI patterns detected."]

### Specificity
[If NEEDS WORK or FAIL: exact lines that are generic, what kind of specific detail should replace them]
[If PASS: brief note on what's working]

### Hook Quality
[If NEEDS WORK or FAIL: which criteria aren't met, what's weak about the opening]
[If PASS: brief note on what's working]

### Structure & Flow
[If NEEDS WORK or FAIL: where the structure breaks, what should change]
[If PASS: brief note on what's working]

### Open Loop & Hold Rate
[If NEEDS WORK or FAIL: where tension breaks, where the piece becomes skippable]
[If PASS: brief note on what's working]

### Value Equation
[If NEEDS WORK or FAIL: which levers are missing, where they should appear]
[If PASS or N/A: brief note]

### Audience Qualification
[If NEEDS WORK or FAIL: which sections lack qualifiers, what type to add]
[If PASS: brief note on what's working]

### CTA Quality
[If NEEDS WORK or FAIL: what's missing, how to fix]
[If PASS or N/A: brief note]

---

## VERDICT

**[READY TO SEND / NEEDS REVISION / NEEDS REWORK]**

[2-3 sentence summary: what's the single biggest issue, what's the priority fix, and is this fundamentally sound or structurally broken]
```

## Quality Standards

The QC report passes its own quality check when:
- Every piece of feedback is specific, actionable, and traceable to a framework or principle from the checks above
- No feedback is vague opinion (e.g., "this could be stronger" without saying how or why)
- No issues are fabricated. If the copy is strong, the report says so. Do not invent problems to justify the process.
- AI-ism flags include the exact text and pattern name, not just "there are some AI patterns"
- The report distinguishes between critical issues (structural, audience) and surface issues (word choice, minor AI patterns)

## Constraints

- **Never rewrite or change copy.** This skill produces analysis and feedback only. If the user asks for rewrites, tell them to revise based on the feedback or use a writing skill.
- **Never fabricate issues.** If a piece is strong, say so. A PASS is a valid outcome.
- **Every piece of feedback must be traceable.** Reference the specific check, pattern, or framework that supports the feedback. No gut-feel opinions.
- **Flag every AI-ism instance.** Even if the usage might be intentional. The writer decides whether to keep it. Your job is to surface it.
- **Adjust expectations by format.** A 50-word cold DM doesn't need all 4 value equation levers. A LinkedIn post doesn't need a hard CTA. Evaluate based on what the specific format requires, not a universal checklist.
- **Don't over-penalize short copy.** Under 100 words, some checks will naturally have less to evaluate. Rate based on what's there, not what's missing because of length.

## Reference Frameworks

This skill evaluates copy against the following frameworks, used as evaluation lenses, not rigid checklists:

- **13+5 AI Language Patterns** — the specific patterns catalogued in Check 1
- **Eugene Schwartz's 5 Awareness Levels** — for evaluating structure and information sequencing
- **Hormozi's Value Equation** — Dream Outcome, Perceived Likelihood, Time Delay, Effort & Sacrifice
- **Hook Quality Criteria** — attention, qualification, earned continuation, friend test, proof/specificity
- **Open Loop Mechanics** — whether openings create unresolved questions that sustain attention
- **CTA Framework** — Action + Vehicle + Specific Deliverable, loop closure, stage-appropriate ask strength
