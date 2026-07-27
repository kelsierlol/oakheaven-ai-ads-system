---
name: naming-code-sheet-generator
description: Use this skill when onboarding a new client or resetting creative strategy to generate the standardised Naming Code Sheet for that client's ad account. Triggers include any mention of "naming codes", "code sheet", "naming convention setup", "set up naming for [client]", "build the codes for [client]", or when a new Creative Strategy Brief has been completed and the client needs their naming locked before ads launch. This skill takes the Creative Strategy Brief (personas, angles, pain points, motivations) and produces a locked, standardised Naming Code Sheet that your team uses to name every ad in the account. Do NOT use this skill to name individual ads — it produces the code reference that informs the naming.
---

# Naming Code Sheet Generator

Takes a client's Creative Strategy Brief and produces a standardised Naming Code Sheet — the single source of truth for every code used in that client's ad names.

## Core Principle

Every code must be:
- **Short:** 2-5 characters, all uppercase
- **Unique:** No two codes can look the same when scanning quickly in Ads Manager
- **Permanent:** Once locked, a code cannot be renamed — only deprecated and replaced
- **Specific:** A code must map to exactly one concept. If it could mean two things, split it into two codes.

---

## When To Use This Skill

- When onboarding a new client and their Creative Strategy Brief is complete
- When resetting creative strategy for an existing client and new personas/angles have emerged
- When a client enters a new market and needs additional codes added to their existing sheet
- When the user says anything like: "set up naming for [client]", "build the code sheet", "we need naming codes before we launch"

---

## What You Need Before Starting

### Required Input
1. **Creative Strategy Brief** — The completed output from the Creative Strategy Brief Builder skill. Must include:
   - Persona profiles (macro and/or micro personas with ranked pains and desires)
   - Angles mapped per persona
   - Voice-of-customer language
   - Offer details

### Optional But Valuable
2. **Existing ad account data** — If the client has historical ads, the names of currently running ads help identify what's already in use and what legacy patterns exist
3. **Client Brain File** — Additional context on ICP, past performance, specific terminology the client uses

---

## How This Skill Works

### Phase 1: Brief Ingestion

Read the entire Creative Strategy Brief. Extract and confirm:
- How many distinct personas exist
- What the core problem categories are (these become Issues)
- What specific pain points are ranked for each persona
- What motivations/desired outcomes are ranked for each persona

Output a summary:
```
BRIEF INGESTION COMPLETE
Client: [Name]
Personas identified: [List with one-line description each]
Distinct problem categories: [List]
Total pain points extracted: [X across Y personas]
Total motivations extracted: [X across Y personas]
Ready to generate codes.
```

### Phase 2: Issue Code Generation

For each distinct problem category / persona, propose a code.

Rules for Issue codes:
- 2-5 uppercase characters
- Must be immediately recognisable — someone scanning Ads Manager should know what it means without checking the sheet
- Avoid codes that are substrings of other codes (e.g., don't use `IN` if you also have `INF`)
- Avoid codes that look like common Meta column names or metrics
- If the client's industry has standard abbreviations, use them (e.g., `BP` for blood pressure, `GLP` for GLP-1)

Present the proposed codes in a table:
```
| Code | Issue / Persona | Description |
|------|----------------|-------------|
```

Ask the user to confirm or adjust before proceeding.

### Phase 3: Pain Code Generation

For each Issue, propose codes for the top 3-5 pain points from the brief's persona profiles.

Rules for Pain codes:
- Short, descriptive, uppercase
- Must be unique ACROSS ALL issues (not just within one issue) — because the ad name doesn't always repeat the Issue code nearby when filtering
- Derived from the actual voice-of-customer language where possible
- If the brief ranks pains, start with the top-ranked ones

Present:
```
| Issue | Code | Pain Point | Source (from brief) |
|-------|------|------------|-------------------|
```

Ask the user to confirm or adjust.

### Phase 4: Motivation Code Generation

For each Issue, propose codes for the top 3-5 motivations/desired outcomes.

Same rules as Pain codes — unique across all issues, derived from customer language.

Present:
```
| Issue | Code | Motivation | Source (from brief) |
|-------|------|-----------|-------------------|
```

Ask the user to confirm or adjust.

### Phase 5: Collision Check

Before finalising, run a collision check across ALL proposed codes:
- No two codes are identical
- No code is a substring of another code (e.g., `FAT` inside `FATIGUE` — both could match on a "contains" filter)
- No code matches a common Ads Manager filter term or metric abbreviation
- All codes are 2-5 characters

If collisions are found, propose alternatives and ask the user to choose.

### Phase 6: Output the Naming Code Sheet

Generate the complete Code Sheet in the standard template format:

```markdown
# [CLIENT] — Naming Code Sheet
**Last updated:** [DATE]
**Maintained by:** [your team]
**Location:** This is the single source of truth for all ad naming codes.
**Reference Skill:** `skills/ad-naming-generator/SKILL.md`

---

## Issues (Personas)
| Code | Full Name | Description |
|------|-----------|-------------|
[Generated rows]

## Pains (by Issue)
| Issue | Code | Pain Point |
|-------|------|------------|
[Generated rows]

## Motivations (by Issue)
| Issue | Code | Motivation |
|-------|------|------------|
[Generated rows]

## Universal Codes (do not modify per client)
Creative Type, Format, Hook, and Tag codes are standardised across all accounts unless the client defines their own (e.g., some clients have client-specific creative type, hook, and tag codes).
See `skills/ad-naming-generator/SKILL.md` for the full universal code reference.

---

## Ad Name Format

Fields separated by underscores (`_`). Hyphens within codes are part of the code name, not separators.

### Full Format
[ISSUE]_[AGE]_[PAIN]_[MOTIVATION]_[CREATIVE TYPE]_[HOOK]_[CONCEPT]_[TAG]

### Shortened Format (broad / no specific age-pain-motivation targeting)
[ISSUE]_[CREATIVE TYPE]_[HOOK]_[CONCEPT]_[TAG]

Note: Some clients (some accounts) merge Creative Type and Format into a single field. Check the client's specific convention doc if one exists.

---

## Example Ad Names for [CLIENT]
[3-5 example ad names using the codes above, mixing full and shortened formats]

---

## Deprecated Codes
| Old Code | Replaced By | Date | Reason |
|----------|------------|------|--------|
| (none yet) | | | |
```

### Phase 7: Save Location

Tell the user:
```
Code Sheet ready. Save to: outputs/Naming Code Sheet.md

This file is now the single source of truth. All ad naming for [CLIENT] references this file.
Your team maintains it and checks it before every creative round. New codes go through the
add-code workflow in the Naming Conventions SOP before being used in any ad name.
```

---

## Hard Rules for This Skill

1. **Never generate codes without the Creative Strategy Brief.** The brief is the source material. Without it, codes will be generic and useless.
2. **Never skip the collision check.** A single substring collision (e.g., `IN` matching inside `INF`) will corrupt every "contains" filter in Ads Manager.
3. **Always get user confirmation at each phase.** Do not auto-generate the full sheet without checkpoints. The codes need to make sense to the people using them daily.
4. **Never reuse codes across Issues without explicit intent.** Each code should map to exactly one meaning across the entire Code Sheet.
5. **Keep it tight.** Start with 3-5 pains and 3-5 motivations per Issue. The sheet grows over time as new angles are tested. Better to start lean and add than to start bloated with codes nobody uses.
