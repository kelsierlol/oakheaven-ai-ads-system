# Step 15 — Build A Custom Skill

**Time:** 10 min (plus ~20 min for the interview)
**Goal:** Use the Skill Creator to build a new skill for any repeatable process in your business. Now you can extend the system for anything.

---

## Why This Is The Final Step

Everything you've done so far runs on the 6 built-in skills. But your business has a hundred other repeatable processes — sales call analysis, offer document creation, content idea generation, client onboarding checklists, weekly reports, etc.

The Skill Creator lets you automate any of them, the same way you'd use Creative Strategy or Script Generator. Once you can do this, the system is truly yours.

---

## What A "Skill" Actually Is

A skill is a structured prompt with:
- **A trigger** (when to activate it)
- **Required inputs** (what data it needs)
- **A process** (step-by-step instructions)
- **A quality standard** (how to know the output is good)
- **Constraints** (what it should never do)

Think of it as an SOP that Claude can execute on demand.

---

## Pick A Process To Automate

Good candidates for your first custom skill:

- **Sales call analysis** — Take a Fathom transcript, output: what went well, what could've been better, objection patterns, close probability
- **Offer deck generator** — Take customer details, output a custom offer deck based on their situation
- **Content idea generator** — Take your winning ads, output 10 new content ideas for social
- **Weekly client report** — Take ad data, output a client-facing weekly update
- **Onboarding checklist generator** — For each new client, generate their specific onboarding inputs list

Pick one you do regularly that eats your time.

---

## The Prompt

Paste this into Claude:

```
I want to build a new skill using the Skill Creator
(skills/skill-creator/SKILL.md).

The process I want to automate is: [describe the process in 1-2
sentences]

Before I answer your questions, walk me through your pre-work
requirements (the 8 inputs you want me to gather). I'll come back
with what I have, then you can run the interview.

When you interview me, ask questions ONE AT A TIME. Don't move on
until I've given you a specific answer. If I'm vague, push back.

When you're done, write the skill to skills/[skill-name].md and
show me a summary.
```

---

## How The Interview Works

Claude will ask 7 questions, one at a time:

1. **Goal** — What's the single output this skill produces?
2. **Current Process** — How does this get done today, step by step?
3. **Data Sources** — What inputs does it need, in what format?
4. **Output Standard** — What does a great output look like? Show an example.
5. **Process Challenge** — Claude pushes back on the parts of your process it thinks are wrong or over-complicated
6. **Quality & Constraints** — How do you know the output is good? What must it never do?
7. **Edge Cases** — What are 2-3 ways this could break down?

It's a genuine conversation. Claude is a process skeptic — it'll simplify your thinking as you go.

---

## The Output

Claude writes a production-ready `.md` file to `skills/`. Every time you want to run the process, you just paste a trigger prompt and Claude executes.

---

## Example: Sales Call Analysis Skill

If you built a sales call analysis skill, the workflow after would be:

**You (after any sales call):**
```
Run the sales call analysis skill on this transcript:
[paste transcript]
```

**Claude:**
Reads the skill, follows the process, outputs a structured report with what went well, what didn't, objections raised, probability of close, and specific next-step recommendations.

Every call. Instantly. Saves hours a week.

---

## Rules For Building Good Skills

1. **Start with the output.** If you can't describe the output clearly, you can't automate the process.
2. **Fail loudly.** If the skill hits a failure mode, it should stop and tell you what's missing — not guess.
3. **Human handoffs are fine.** If a step needs a human (like copy-pasting data from a platform Claude can't access), say so directly.
4. **Keep it focused.** One skill = one output. Don't build a mega-skill that does 5 different things.
5. **Pressure-test it.** After building, run it on a real example. Fix what breaks.

---

## How To Build Multiple Skills

Once you've built one, the process gets faster. Skills to consider building over time:

- Sales call analysis
- Client onboarding input generator
- Weekly client report generator
- New angle ideator (from ad data)
- Content idea generator
- Offer deck builder
- VSL script generator (if different from general ad scripts)
- Landing page copy generator
- Email sequence generator
- Cold DM script generator

Build them as you need them. Don't try to build them all at once.

---

## ✅ Checkpoint

- [ ] You've built at least one custom skill
- [ ] The skill is saved to `skills/[skill-name].md`
- [ ] You've tested it on a real example and it works
- [ ] You understand the process for building more skills as needed

---

## 🎉 You're Done

You've just:

- Set up a complete AI ads system for your business
- Populated it with your data
- Run a full creative strategy
- Generated your first 5 ad scripts
- Learned the weekly bottleneck analysis rhythm
- Locked in your KPIs and benchmarks
- Built a custom skill for something uniquely yours

You can now run this exact process for any of your clients. You've been the client. You know what good data looks like, you know what the output feels like, and you can deliver the same experience.

**Next actions:**
1. Start using the weekly Monday bottleneck analysis rhythm
2. Keep feeding new sales calls into the knowledge base as they happen
3. Re-run creative strategy every quarter or whenever your account plateaus
4. Build custom skills as you find new bottlenecks in your workflow
5. Start offering this to your clients (use the onboarding checklist we gave you)

Message me in Slack with feedback, wins, questions. Go make some money.
