# MASTER SETUP PROMPT

This is the single prompt that sets up your entire AI Ads System inside Claude. After you've installed Claude Code and navigated into the workspace folder (Steps 01–03), paste this prompt and Claude handles everything else.

You won't need to read the other steps. Claude will interview you, ask for the files it needs you to upload, run the skills, and produce every artifact. Just follow along.

---

## Before You Paste This

Make sure you've completed **Step 04 — Asset Inventory (Pre-Flight Checklist)** in the course. If you haven't, stop here and go do that first. The Master Setup Prompt will ask you to confirm your readiness scores before letting you proceed past Phase 5.

If you skip the pre-flight and score RED on critical assets, Claude will stop the setup and send you back to gather what's missing. Save yourself the round-trip.

---

## Paste This Into Claude

```
Run the Guided Setup skill (skills/guided-setup/SKILL.md) for my workspace.

I want you to take me from zero to a fully operational AI ads system
in this one session. Walk me through every phase:

1. Verify the filing system
2. Interview me to fill context/business.md (my offer, ICP, personas,
   voice, positioning, proof, objections)
3. Interview me to fill context/ad-account.md (spend, benchmarks,
   kill/scale criteria)
4. Fill context/glossary.md (my product terms, shorthand)
5. Walk me through loading my data:
   - Ask me to upload 20 sales call transcripts to
     knowledge-base/sales-calls/
   - Ask me to upload winning ad scripts to knowledge-base/winning-ads/
   - Ask me to upload testimonials/case studies to
     knowledge-base/research/proof/
   - Ask me to research and document my top 3-5 competitors in
     knowledge-base/research/competitors/
   - Verify each folder before moving on
6. Run the full Creative Strategy skill (personas, scoring, micro
   personas, strategy map). Pause at every human checkpoint.
7. Run the Script Generator skill to produce 5 QC'd storyboards
   (3 hook variations each) from the brief
8. Run the KPI Tracker skill to calculate my unit economics and
   lock in benchmarks
9. Explain my ongoing operations rhythm (daily check-in, weekly
   bottleneck analysis, quarterly strategy refresh)
10. Offer to build a custom skill for me via the Skill Creator

Rules:
- Ask me ONE question at a time. Never give me a list of questions.
  Wait for my answer before moving to the next.
- Push back if my answers are vague. Specificity is the whole point.
- Save progress to memory/open-loops.md at the end of every phase so
  I can pause and resume.
- Never skip the hard gates. If I don't have 5+ sales calls, pause
  the setup and tell me to go get them.
- Never write context files with generic filler. Only write what I
  specifically tell you.
- If I say "pause" at any point, save where we are and stop.
- If I say "resume guided setup" in a future session, read
  memory/open-loops.md and pick up where we left off.

Start with Phase 0: read memory/open-loops.md to check if we've done
this before. If not, start Phase 1 (filing system verification).

Go.
```

---

## What To Expect

Claude will walk you through ~10 phases. Total time: 2–3 hours, but you can pause and resume any time.

You'll produce:
- Filled-in business context, ad account context, and glossary
- A populated knowledge base (sales calls, winning ads, proof, competitors)
- A full Creative Strategy Brief with personas, scoring, and strategy map
- 5 production-ready ad storyboards with QC reports
- Locked-in KPIs and benchmarks
- Optionally: a custom skill for any other process in your business

---

## Pausing & Resuming

- Say **"pause"** any time to stop. Claude saves your progress.
- Say **"resume guided setup"** when you come back. Claude reads your progress and picks up where you left off.

---

## If Something Breaks

- **"Filing system check failed"** — Run `git pull` in your workspace folder to make sure you have the latest. If files are still missing, re-clone the repo. Make sure you're in the right folder (`pwd` should end in your workspace folder name).
- **"Not enough sales calls"** — Go get more. This is a hard gate for a reason. Come back when you have 5+.
- **"Claude is giving generic answers"** — Push back. Tell Claude to be specific to your business. If your inputs were vague, go back and fix them.
- **Anything else** — Message in the community channel with a screenshot.

---

## Once Setup Is Complete

You'll have everything you need. Your daily rhythm:
- **Every morning (2 min):** Daily Media Buyer Check-in
- **Monday (15 min):** Full Bottleneck Analysis
- **Quarterly:** Refresh Creative Strategy with new data

And anytime you want: new scripts, QC on copy you've written, custom skills for new processes.

That's it. Go paste the prompt.
