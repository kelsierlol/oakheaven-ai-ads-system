# Step 02 — Install Claude Code & Git

**Time:** 10 min
**Goal:** Get Claude Code and Git running on your computer.

---

## Why Claude Code (Not Claude.ai or Cowork)

- **Reads your files directly** — no more copying and pasting into a chat window
- **Runs skills automatically** — when you ask for a creative strategy, Claude knows exactly which file to reference
- **Works with your filing system** — everything stays organized in folders you can version and back up
- **Can write files back to your computer** — outputs go directly into `/outputs` where you expect them

If you're using Cowork, Claude.ai, or Manus, this is the next level.

---

## Install Claude Code

### Mac

1. Go to **claude.ai/code**
2. Download the Mac installer
3. Open the `.dmg` file
4. Drag Claude Code to Applications
5. Open Claude Code from Applications
6. Sign in with your Anthropic account (Pro plan required — you already have it if you've been using Claude)

### Windows

1. Go to **claude.ai/code**
2. Download the Windows installer
3. Run the `.exe` file
4. Follow the installation prompts
5. Launch Claude Code from the Start menu
6. Sign in with your Anthropic account

---

## Install Git

You'll use Git to clone the workspace from GitHub and pull updates over time. Most Macs ship with it pre-installed; Windows usually doesn't.

### Mac

In Terminal, type:

```
git --version
```

- If it returns a version (e.g., `git version 2.x.x`), you're done.
- If it prompts you to install the developer tools, click "Install" and wait — that gets you Git.

### Windows

1. Go to **git-scm.com/downloads**
2. Download "Git for Windows"
3. Run the installer (default settings are fine)
4. Open Command Prompt or PowerShell
5. Type `git --version` to verify

---

## Open Your Terminal

You'll be using Terminal (Mac) or Command Prompt / PowerShell (Windows) for both Git and Claude Code.

### Mac

- Press `Cmd + Space` → type "Terminal" → hit Enter
- Or: Applications → Utilities → Terminal

### Windows

- Press `Windows key` → type "Terminal" → hit Enter
- Or use PowerShell (works the same)

---

## Verify Both Installations

In your terminal, type:

```
claude --version
git --version
```

If both return version numbers, you're good. If either returns "command not found", reinstall following the steps above.

---

## ✅ Checkpoint

- [ ] Claude Code installed
- [ ] Signed in with your Anthropic account (Pro plan active)
- [ ] Git installed (`git --version` returns a number)
- [ ] Terminal or Command Prompt open
- [ ] `claude --version` returns a version number

Move to **Step 03 — Load Your Workspace**.
