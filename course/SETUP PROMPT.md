# SETUP PROMPT — Paste This Into Claude Code

Once you've installed Claude Code + Git and cloned the workspace (Steps 02–03), open Claude Code inside the workspace folder and paste this prompt:

---

```
I've just cloned my AI Ads System workspace from GitHub. Before we start,
I need you to do three things:

1. Read my CLAUDE.md so you know what skills and context files are
   available.

2. Verify the full filing system is in place. Run this checklist:
   - Is CLAUDE.md present at root?
   - Is the context/ folder present with business.md, ad-account.md,
     glossary.md?
   - Is the skills/ folder present with all skill files (you should see
     creative-strategy, script-generator, script-qc, ai-slop-remover,
     ad-naming-generator, naming-code-sheet-generator, kpi-tracker,
     media-buying-sop-generator, daily-media-buyer-checkin,
     bottleneck-analysis, lead-quality-report, ads-setup-engine,
     ads-plan-and-sops, daily-ab-band-management, guided-setup,
     master-setup-prompt, skill-creator) plus reference files
     (hook-formulas, ad-formats-library, creative-strategy-reference)?
   - Is the knowledge-base/ folder present with sales-calls/,
     winning-ads/, research/ subfolders?
   - Is the outputs/ folder present?
   - Is the memory/open-loops.md file present?
   - Is the course/ folder present?

   Report back: which files are present, which are missing. If anything is
   missing, tell me exactly what to do (e.g., re-clone, run `git pull`).

3. Confirm course/ has the 15 numbered chapter files plus README and
   MASTER SETUP PROMPT.

Once everything is verified, tell me:

- Which skills are loaded and ready to use
- Whether my context files are templates (empty) or already filled in
- Whether my knowledge-base is populated
- Point me to Step 01 of the course (course/01 — The Mental Model.md)

Do not proceed with any work until I explicitly tell you I'm ready to
start the course. Just confirm the setup is good.
```

---

## If Something Is Missing

If Claude reports missing files, check:

1. **Did the clone complete?** Run `ls -la` in your workspace folder — you should see CLAUDE.md, README.md, the skills/ folder, and others.
2. **Are you inside the correct folder in Terminal?** Run `pwd` — should end with the folder name you gave the clone (e.g., `ai-ads-system`).
3. **Did you run `git pull` recently?** If updates have shipped, `cd` into the workspace folder and run `git pull` to fetch them.
4. **Re-clone if all else fails.** Delete the folder and `git clone` again.

If you're still stuck, fire a message in Slack with a screenshot of your terminal.

---

## What To Do After This Prompt Works

Claude will confirm everything is in place and point you to **Step 01 — The Mental Model**.

Open that file. Read it. Then move to Step 02.

Every step tells you exactly what to do and gives you the prompt to paste. You don't need to think about what to ask Claude — just follow the steps.
