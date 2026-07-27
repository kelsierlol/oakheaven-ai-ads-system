# Your AI Ads System

This is your workspace. It contains 16 skills that take your ad account from raw customer research to launched, QC'd ads — and the media buying playbook to run them. It also includes a 15-chapter operator course that walks you through onboarding from zero.

---

## Two ways to use this

### Option 1 — Install as a Claude Code plugin (skills only, no workspace)

If you just want the 16 skills available inside an existing Claude Code or Cowork project, install via the marketplace:

```
/plugin marketplace add leoxmoore/sophron-skills
/plugin install sophron-skills@sophron
```

After install, the skills appear under the `sophron-skills` namespace and trigger automatically based on your prompts. This option does **not** include the operator course or the workspace folders (`context/`, `knowledge-base/`, `outputs/`, `memory/`) — those only come with Option 2.

### Option 2 — Clone the full workspace (skills + course + folders)

This is the original full experience: skills, the 15-chapter operator course, and the pre-structured folders for client context, research, and outputs.

1. Open **course/README.md** and follow the fast path (Steps 01–05). It walks you through installing Claude Code + Git, cloning the workspace, gathering your inputs, and running your first creative cycle. About 3–4 hours end to end.
2. Have **ONBOARDING — Client Inputs Checklist.md** open while you gather the inputs the system needs.
3. Once you're set up, open Claude Code in this folder and start with: *"What skills do you have available?"*

If you'd rather read the workspace setup separately first, see **SETUP GUIDE.md**.

---

## What's in here

**Onboarding & setup**
A guided onboarding flow that interviews you, fills your context files, walks you through loading your data, runs the creative strategy, generates your first scripts, locks in your KPIs, and builds your custom campaign structure with personalised budget bands. Pause and resume any time.

**Creative engine — research → scripts → QC**
Turn sales call transcripts and customer data into deeply specific persona profiles. Write production-ready ad scripts with 3 hook variations each. Quality-check every script before launch. Plus a generic copy QC for any non-script writing.

**Naming & operations**
Lock the naming convention for your account once. Generate Meta-ready ad names from any concept list in seconds.

**Media buying**
Reverse-engineer your target CAC from your real unit economics. Get a daily review playbook your media buyer can follow without interpretation. Surgical daily band management for ABO testing campaigns. Diagnose performance drops with a five-hypothesis framework. Map every dollar of ad spend to real sales outcomes with lead-level scoring.

**Utility**
A skill creator for automating any new repeatable process you find yourself doing twice.

---

## Workspace layout

```
├── README.md                                ← This file
├── CLAUDE.md                                ← How the system thinks (don't edit)
├── SETUP GUIDE.md                           ← First-time setup walkthrough
├── ONBOARDING — Client Inputs Checklist.md  ← What to gather
├── context/                                 ← Your business + account context
├── skills/                                  ← The 16 skills + reference docs
├── course/                                  ← AI Ads Operator Course (15 chapters)
├── knowledge-base/                          ← Your transcripts, winning ads, research
├── outputs/                                 ← Where finished work lands
└── memory/                                  ← Tracks unfinished work across sessions
```

---

## What you need

- **Claude Code** installed (claude.com/claude-code — free with an Anthropic account)
- **Git** installed (`git --version` to check; install from git-scm.com if missing)
- **Your data** — sales call transcripts, customer data, competitor research, offer details, ad account access. Full list in the ONBOARDING checklist.

That's it. No API keys. No integrations to set up.

---

## Pulling updates

When new versions of the engine ship, update with:

```
cd ~/Desktop/your-workspace-folder
git pull
```

Your data in `context/`, `knowledge-base/`, `outputs/`, and `memory/` is yours and never gets touched. Only the engine (skills, course, references) updates.

**Don't edit files in `skills/` or `course/` yourself** — those are owned by the repo, and edits will conflict on the next pull. To customise the system, build a new skill with the Skill Creator instead.

---

## Need help?

Group calls run weekly. Drop questions in Slack/Skool any time between.
