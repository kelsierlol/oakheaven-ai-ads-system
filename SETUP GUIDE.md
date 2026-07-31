# AI Ads System — Setup Guide

Everything you need to get your AI Ads System running. Follow these steps in order.

---

## Phase 1: Install Claude Code

Claude Code is the AI tool that powers your system. It's free to install — you just need an Anthropic account.

### Steps:

1. **Go to** claude.ai/code and follow the download instructions for your operating system (Mac or Windows)
2. **Install** following the on-screen prompts
3. **Open Terminal** (Mac) or Command Prompt (Windows)
4. **Run** `claude` to verify it's installed
5. **Sign in** with your Anthropic account when prompted

If you get stuck, watch the setup video we sent you or ask in the group call.

---

## Phase 2: Clone The Workspace

The workspace is hosted on GitHub. You'll get an invitation email after onboarding — accept it before continuing.

### Steps:

6. **Install Git** if you don't have it (`git --version` to check). On Mac it's usually pre-installed; Windows needs it from git-scm.com/downloads.
7. **Open Terminal** and navigate to your projects folder (Desktop is easiest):
   ```
   cd ~/Desktop
   ```
8. **Clone the workspace:**
   ```
   git clone https://github.com/kelsierlol/oakheaven-ai-ads-system.git oakhaven-ads
   ```
   You can name the folder whatever you like — `ai-ads-system` is just an example.
9. **Navigate into the workspace:**
   ```
   cd oakhaven-ads
   ```
10. **Launch Claude Code** inside the workspace folder:
    ```
    claude
    ```
11. Claude Code will automatically read your CLAUDE.md file and understand your business, your offer, and what skills are available.

**To pull updates later:** `cd` into the workspace folder and run `git pull`. Your data in `context/`, `knowledge-base/`, `outputs/`, and `memory/` is preserved — only the engine (skills, course, references) updates.

---

## Phase 3: Verify Everything Works

Before you start using the system, let's make sure everything loaded correctly.

### Steps:

11. **Ask Claude:** "What skills do you have available?"
    - Claude should list all skills across the four groups:
      - **Creative Engine:** Creative Strategy, Script Generator, Script QC, AI Slop Remover
      - **Naming & Operations:** Naming Code Sheet Generator, Ad Naming Generator
      - **Media Buying:** KPI Tracker, Media Buying SOP Generator, Daily Media Buyer Check-in, Bottleneck Analysis, Lead Quality Report
      - **Utility:** Skill Creator
    - Plus reference files: Hook Formulas, Ad Formats Library, Creative Strategy Reference

12. **Ask Claude:** "Summarise my business context"
    - Claude should accurately describe your offer, ICP, and positioning
    - If anything is wrong, let us know on the next group call or in Slack

13. **Ask Claude:** "What data do you have in my knowledge base?"
    - Claude should confirm it can see your sales call transcripts, winning ads, and research files

If all three checks pass, you're ready to go.

---

## Phase 4: Run Your First Creative Cycle

This is the core workflow you'll use to generate ads.

### Step A: Build Your Creative Strategy

14. **Ask Claude:** "Run a creative strategy for my business"
15. Claude will:
    - Check that all required inputs are in your `knowledge-base/` folder
    - Tell you if anything is missing (and what to add)
    - Walk you through the full process: data tagging → persona clustering → scoring → profiles → micro persona decomposition → strategy map
16. **Review the output** — Claude will pause for your approval at three checkpoints (persona selection, profile approval, micro persona approval) before building the strategy map
17. **Approve or revise** at each checkpoint

### Step B: Lock Your Naming Convention (one-time setup)

18. **Ask Claude:** "Build my Naming Code Sheet from the creative strategy brief"
19. Claude will generate codes for every Issue, Pain, and Motivation, then ask you to confirm each phase
20. Once approved, the Code Sheet is saved to `outputs/Naming Code Sheet.md` — every ad name from now on uses these codes

### Step C: Generate Ad Scripts

21. **Ask Claude:** "Write 5 ad scripts from this brief"
22. Claude will produce storyboards with:
    - 3 hook variations per concept
    - Visual direction and editing instructions
    - Full QC checks run automatically before presenting
23. **Review each script** — Claude will ask for feedback
24. **Revise if needed** — Claude will fix and re-QC

### Step D: Quality Control

25. **If you've written scripts yourself**, ask Claude: "QC these scripts"
26. Claude will run 13 per-script checks + 3 batch-level checks covering: specificity, hook quality, avatar alignment, AI language detection, body structure, awareness curve integrity, open loops, value equation, traffic qualification, CTA quality, recordability, format diversity, angle diversity, and awareness distribution
27. **Review the QC report** — it tells you exactly what's wrong and what to fix (without rewriting for you)

### Step E: Name and Launch

28. **Ask Claude:** "Generate ad names for these concepts"
29. Claude uses your Naming Code Sheet to produce snake_case ad names ready to paste into Meta

---

## Phase 5: Set Up Your Media Buying Playbook

The creative engine produces ads. The media buying engine runs them.

### Step A: Lock Your KPIs

30. **Ask Claude:** "Run the KPI Tracker for my business"
31. Provide: revenue per customer, fulfilment cost, monthly overhead, current ad spend, current conversion metrics, sales close rate (if applicable)
32. Claude will reverse-engineer your max CAC, target ROAS, break-even ROAS, and run three scenarios (conservative / moderate / aggressive)

### Step B: Generate Your Media Buying SOP

33. **Ask Claude:** "Build my Media Buying SOP using the KPIs from the tracker"
34. Claude will produce a complete operational playbook with: budget brackets, kill/scale rules, daily review protocol, weekly cadence, ramping schedule, and a quick-reference cheat sheet
35. The SOP is saved to `outputs/Media Buying SOP.md` — your media buyer follows it daily without needing to interpret anything

---

## Phase 6: Ongoing Use

### Your Weekly Rhythm

| Day | What to do |
|-----|-----------|
| Monday | Daily Media Buyer Check-in (with weekly mining filter). Run Bottleneck Analysis if performance has dropped |
| Tuesday-Thursday | Daily Media Buyer Check-in (3-min). Generate new creative as needed (run strategy → scripts → QC → naming) |
| Friday | Daily Media Buyer Check-in. Run Lead Quality Report on last week's data. Update `context/ad-account.md` with new benchmarks if needed |

### When To Run Each Skill

| Situation | Skill to use |
|-----------|-------------|
| Starting a new creative cycle | Creative Strategy |
| Need new ad scripts | Script Generator |
| Before sending scripts to production | Script QC |
| QC any non-script copy (emails, posts, landing pages) | AI Slop Remover |
| Onboarding a new client / setting up naming | Naming Code Sheet Generator |
| Naming a batch of new ads | Ad Naming Generator |
| Setting up KPIs for a new account | KPI Tracker |
| Building the per-account media buying playbook | Media Buying SOP Generator |
| Daily ad account review | Daily Media Buyer Check-in |
| Account suddenly stopped performing | Bottleneck Analysis |
| Weekly attribution + lead quality review | Lead Quality Report |
| Want to automate a new process | Skill Creator |

### Keeping Your System Updated

Your system gets smarter as you feed it more data. Keep these updated:

- **`knowledge-base/sales-calls/`** — Add new transcripts as you have them. More data = better personas
- **`knowledge-base/winning-ads/`** — When a new ad wins, add the script text here
- **`context/ad-account.md`** — Update benchmarks as your account matures
- **`context/business.md`** — Update if your offer, pricing, or ICP changes
- **`outputs/Naming Code Sheet.md`** — Add new codes as you discover new personas/angles (run Naming Code Sheet Generator to add cleanly)

---

## Your Workspace Structure

```
[Your Business Name] AI Ads System/
├── CLAUDE.md                  ← Master instructions (don't edit unless asked)
├── SETUP GUIDE.md             ← This file
├── ONBOARDING — Client Inputs Checklist.md  ← What you provided during onboarding
├── context/
│   ├── business.md            ← Your offer, ICP, personas, voice
│   ├── ad-account.md          ← Your account structure and benchmarks
│   └── glossary.md            ← Your terms and shorthand
├── skills/
│   ├── creative-strategy.md            ← Builds persona profiles + strategy map
│   ├── script-generator.md             ← Turns briefs into production scripts
│   ├── script-qc.md                    ← Reviews scripts against 13 + 3 quality checks
│   ├── ai-slop-remover.md              ← QCs any written copy
│   ├── naming-code-sheet-generator.md  ← Builds the locked code sheet
│   ├── ad-naming-generator.md          ← Generates Meta-ready ad names
│   ├── kpi-tracker.md                  ← Unit economics + scenario modelling
│   ├── media-buying-sop-generator.md   ← Per-client media buying playbook
│   ├── daily-media-buyer-checkin.md    ← Daily review workflow
│   ├── bottleneck-analysis.md          ← Diagnostic for performance drops
│   ├── bottleneck-analysis-references/ ← Diagnostic framework, KPIs, metric interrelationships
│   ├── lead-quality-report/            ← Folder skill: SQIBNT scoring + dashboard
│   ├── skill-creator.md                ← Builds new automation skills
│   ├── hook-formulas.md                ← Reference: 10 proven hook types
│   ├── ad-formats-library.md           ← Reference: format specs
│   └── creative-strategy-reference.md  ← Reference: awareness framework
├── knowledge-base/
│   ├── sales-calls/           ← Your transcripts
│   ├── winning-ads/           ← Your best-performing ad scripts
│   └── research/              ← ICP research, competitor analysis, surveys
├── outputs/                   ← Where finished briefs, scripts, SOPs, reports go
└── memory/
    └── open-loops.md          ← Unfinished tasks between sessions
```

---

## Troubleshooting

**Claude doesn't seem to know my business:**
→ Make sure you're inside the workspace folder when you launch Claude Code. Run `pwd` in terminal to check your current directory.

**Claude says a skill is missing:**
→ Check that all files are in the `skills/` folder. If a file is missing, run `git pull` to fetch the latest. If still missing, re-clone the repo.

**Claude says inputs are missing when running Creative Strategy:**
→ The skill has hard gates. It needs: sales call transcripts (5+), customer data, competitor research, offer details, and winning ads. Check your `knowledge-base/` folder.

**Scripts sound too much like AI:**
→ The QC skill catches this. Run Script QC and it will flag every AI-ism pattern. Then revise.

**My CPP/CPL spiked overnight:**
→ Run Bottleneck Analysis. It will diagnose the root cause across the five hypotheses (creative fatigue, audience exhaustion, CBO budget allocation, placement shift, attribution change) and tell you exactly what to fix first.

**Lead Quality Report won't run:**
→ It needs your Meta Ads Manager CSV + your attribution tool export (Hyros / Cortana / etc) + ideally your CRM closer notes. Without the attribution export, you can only run Level 1 (basic ROAS attribution).

**Need help?**
→ Ask in the weekly group call or message us in Slack (1-1 clients) or Skool (group clients)

---

## Quick Commands

Copy and paste these into Claude Code to get started:

**Creative engine:**
- `"What skills do you have available?"` — Check the system
- `"Summarise my business context"` — Verify your data loaded
- `"Run a creative strategy for my business"` — Start a new creative cycle
- `"Build my Naming Code Sheet from the creative strategy"` — Lock naming
- `"Write 5 ad scripts from this brief"` — Generate scripts
- `"QC these scripts"` — Quality check scripts
- `"Generate ad names for these concepts"` — Produce Meta-ready names
- `"De-slop this copy"` — QC any non-script copy

**Media buying:**
- `"Run the KPI Tracker"` — Lock your unit economics
- `"Build my Media Buying SOP"` — Generate the playbook
- `"Run my daily media buyer check-in"` — Daily review
- `"Run a bottleneck analysis"` — Diagnose performance drops
- `"Build my Lead Quality Report"` — Weekly attribution + lead scoring

**Utility:**
- `"I want to build a new skill"` — Create a custom automation
