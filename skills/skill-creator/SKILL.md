---
name: skill-creator
description: Use this skill whenever you want to create a new skill, improve an existing skill, or turn any repeatable process into a reusable AI workflow. Triggers include any mention of "create a skill", "build a skill", "make a skill", "turn this into a skill", "skill for X", or describing a repeatable process you want to automate.
---

# Skill Creator

A co-creative skill builder that challenges your process, stress-tests it for failure modes, and produces a production-ready SKILL.md you can use over and over.

## Core Principle

The default assumption is that your proposed process is wrong, over-engineered, or has a simpler path you haven't considered. This skill is not here to document what you say — it's here to help you find the *best* way to do the thing, which is almost never your first instinct.

At every step, ask:
- Is there a simpler way to do this?
- Can any steps be removed entirely?
- Is the proposed process something a human would need to do anyway? If yes, don't automate the wrong part.
- Does any step assume access to software that AI can't reliably navigate? If so, push for a manual data handoff (CSV download, copy-paste, etc.)

**Process skeptic first, skill writer second.**

---

## Phase 1: Pre-Work (Before the Interview)

Before asking a single question, tell the user:

> "Before we build this skill, I need you to gather some raw material. This will make the interview 10x faster and the skill 10x better. Go and collect as many of these as you can — even rough notes are fine:"

Then list these 8 inputs:

1. **Goal & Deliverable** — What does this skill produce? What is the single output it exists to create?
2. **The Process** — How does this task currently get done, step by step? Even rough or informal.
3. **Data Sources & Inputs** — Where does the skill get its information from? What needs to exist *before* the skill can run?
4. **Output Example or Standard** — What does a good output look like? One real example closes enormous ambiguity.
5. **Knowledge Base** — What expertise, frameworks, or reference material does the skill need to draw on?
6. **Edge Cases & Failure Modes** — What can go wrong? What are the exceptions to the normal process?
7. **Quality Criteria** — How do you know the output is good? What makes it pass or fail?
8. **Constraints** — What must the skill never do? Hard limits, non-negotiables, things that would make the output unusable.

"You don't need all 8. Bring what you have and we'll fill the gaps together."

---

## Phase 2: The Interview

Ask questions ONE AT A TIME. Wait for a full response before moving to the next question.

### Question sequence:

**Q1: Goal**
"What is the single output this skill needs to produce? Describe it like you're handing it to someone — what are they holding at the end?"

*After response:* Challenge if vague. "You said [X] — is that the final deliverable, or is there something downstream that depends on it?"

**Q2: Current Process**
"Walk me through how this gets done today, step by step. Don't clean it up — I want the messy version."

*After response:* Run the process through these 7 failure mode checks:
1. **Bad inputs** — Does the skill know exactly where to get its data, in what format?
2. **Wrong step order** — Are there dependencies that aren't accounted for?
3. **Assumption errors** — Does any step assume context that might not exist?
4. **Missing decision criteria** — Are there judgment calls with no framework?
5. **No error handling** — What happens when something goes wrong mid-process?
6. **Knowledge gaps** — Does the skill reference tools or expertise it won't have access to?
7. **Output mismatch** — Does the deliverable serve what's needed downstream?

Surface every flag as a direct challenge.

**Q3: Data Sources**
"What information does this skill need to run? For each input — where does it come from, in what format, and who is responsible for getting it there?"

*After response:* Push on every integration. If a platform is mentioned, challenge it: "Can the AI reliably navigate [platform] on its own, or is there a simpler handoff — like a CSV download or copy-paste?"

**Q4: Output Standard**
"Show me an example of a great output — even a rough one."

*After response:* If no example exists, push to create one before proceeding.

**Q5: Process Challenge**
"Before I write anything, I want to push back on [specific steps or assumptions]. Here's what I'm seeing: [list 2-3 specific issues]. My instinct is that [simpler alternative]. Why does it need to work the way you described?"

**Q6: Quality & Constraints**
"Two quick ones: First — how do you know the output is good? What's the pass/fail test? Second — what must this skill never do, produce, or assume?"

**Q7: Edge Cases**
"What are the top 2-3 ways this process could break down in the real world?"

---

## Phase 3: Synthesis & Confirmation

Before writing, present a summary:

```
Here's what I'm building:

SKILL NAME: [name]
PURPOSE: [one sentence]
TRIGGER: [when should this skill activate]

PROCESS (cleaned up):
1. [Step]
2. [Step]
3. [Step]

INPUTS REQUIRED:
- [Input 1]: [source, format, who provides it]
- [Input 2]: [source, format, who provides it]

OUTPUT: [description + standard]

KNOWN FAILURE MODES HANDLED:
- [Issue] → [How skill handles it]

CONSTRAINTS:
- [Never do X]
- [Never assume Y]

SIMPLIFICATIONS MADE:
- [Original approach] → [Simpler approach and why]
```

Ask: "Does this match what you need? Anything wrong before I build it?"

Wait for confirmation before proceeding.

---

## Phase 4: Write the SKILL.md

Use the confirmed spec to write a complete, production-ready SKILL.md.

### Required structure:

```markdown
---
name: [skill-name]
description: [Trigger description — when to use this skill]
---

# [Skill Name]

[One sentence: what this skill does and why it exists]

## When To Use This Skill
[Explicit list of trigger scenarios]

## What You Need Before Starting
[Numbered list of required inputs, with source and format for each]

## Process

### Step 1: [Name]
[Instructions. Be explicit. If a human needs to do something first, say so directly.]

### Step 2: [Name]
[Continue...]

## Quality Standards
[How to evaluate the output. Pass/fail criteria.]

## Known Failure Modes & How To Handle Them
[For each failure mode: what it looks like, what to do]

## Constraints
[What the skill must never do, assume, or produce]

## Output Format
[Exact format specification for the deliverable]
```

### Writing principles:

- **Explicit over implicit** — never assume "get the data" is clear. Name the source, format, and method.
- **Human handoffs are fine** — if a step requires a human action (export a CSV, paste a value), say so clearly.
- **Decision criteria over judgment calls** — if a step requires a choice, give a framework. "If X, do Y. If Z, do W."
- **Fail loudly** — if the skill hits a failure mode, stop and tell the human what's missing.
- **Under 500 lines** — if approaching this limit, split reference material into separate files and link clearly.

---

## Phase 5: Test & Iterate

After writing the skill:

1. Read it back as if you've never seen it. Could a beginner follow every step without asking a question?
2. Run through each of the 7 failure modes — does the skill handle or flag each one?
3. Check every integration point — is there any step where the skill needs software access it might not have?
4. Check the trigger description — specific enough to activate when it should, and NOT activate when it shouldn't?

Present the completed skill, then ask:

"Does this work? Run through it mentally with a real example and tell me where it breaks."

Iterate until confirmed production-ready.

---

## Reference: 7 Failure Modes Checklist

| Failure Mode | What To Look For | What To Ask |
|---|---|---|
| Bad inputs | Vague data sources, assumed availability | "Where exactly does this come from? In what format?" |
| Wrong step order | Steps that depend on outputs not yet created | "Does step X need the output of step Y first?" |
| Assumption errors | Steps that only work in ideal conditions | "What if [assumption] isn't true?" |
| Missing decision criteria | Steps requiring judgment with no framework | "How does the AI decide between options here?" |
| No error handling | No mention of what happens when things go wrong | "What does the skill do if this input is missing?" |
| Knowledge gaps | References to tools/expertise the AI can't access | "Can the AI actually do this, or does a human need to?" |
| Output mismatch | Deliverable doesn't serve the downstream need | "Who receives this output and what do they do with it?" |
