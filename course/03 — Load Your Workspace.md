# Step 03 — Load Your Workspace

**Time:** 10 min
**Goal:** Clone the AI Ads System workspace from GitHub and verify it.

---

## Clone The Workspace

You should have received a GitHub invitation email giving you access to the `sophron-skills` repository. Accept it before continuing.

In your terminal, navigate to where you keep project folders (Desktop is easiest):

**Mac:**
```
cd ~/Desktop
```

**Windows:**
```
cd %USERPROFILE%\Desktop
```

Then clone the workspace:

```
git clone https://github.com/leoxmoore/sophron-skills.git ai-ads-system
```

(`ai-ads-system` becomes the folder name — change it if you prefer something else.)

If git asks you to authenticate, follow the prompts. On Mac it'll usually open a browser. On Windows it may prompt for username + a personal access token (use a PAT, not your password — instructions in the GitHub docs).

You should now have a folder called `ai-ads-system` with these contents:

```
ai-ads-system/
├── README.md
├── CLAUDE.md
├── SETUP GUIDE.md
├── ONBOARDING — Client Inputs Checklist.md
├── context/
├── skills/
├── knowledge-base/
├── outputs/
├── memory/
└── course/                ← this course (also bundled in the repo)
```

---

## Navigate Into Your Workspace

```
cd ai-ads-system
```

Verify you're in the right place by running:

```
pwd
```

(Mac) or

```
cd
```

(Windows) — this should print the path ending in `ai-ads-system`.

---

## Launch Claude Code

Inside the workspace folder, type:

```
claude
```

Claude Code will start. It will automatically read the `CLAUDE.md` file and know your setup.

---

## Run The Setup Prompt

Open `course/SETUP PROMPT.md`. Copy the prompt inside the code block. Paste it into Claude.

Claude will:
- Verify every file is in place
- Tell you which skills are available
- Confirm whether your context files are templates or already filled in
- Point you to Step 04

---

## Pulling Updates Later

When new versions of the engine ship, you'll get a notification (group call, Slack, Skool). To update your workspace:

```
cd ~/Desktop/ai-ads-system
git pull
```

This pulls the latest skills and reference files. Your own data in `context/`, `knowledge-base/`, `outputs/`, and `memory/` won't be touched — those folders are yours to fill in.

**Rule:** Never edit files in `skills/` or `course/` yourself. Those are owned by the repo, and your edits will conflict on the next pull. If you want to customize a skill, build a new one with the Skill Creator instead.

---

## ✅ Checkpoint

- [ ] Repository cloned to your Desktop (or chosen project folder)
- [ ] Terminal is inside the workspace folder (`pwd` confirms it)
- [ ] Claude Code is running
- [ ] Setup Prompt has been pasted and Claude confirmed everything is in place

Move to **Step 04 — Asset Inventory (Pre-Flight Checklist)**.
