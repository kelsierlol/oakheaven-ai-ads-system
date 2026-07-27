---
name: ad-naming-generator
description: Generates ad names and Naming Code Sheets per client using the snake_case naming convention. Takes a creative brief or concept list as input, outputs properly formatted ad names ready to paste into Meta.
---

# Ad Naming Generator

Generate ad names or a Naming Code Sheet for a client account.

## Before You Start

1. The naming system is documented in this skill file (see "Universal Code Reference" below). Follow it exactly.
2. Check if the client already has a Naming Code Sheet at `outputs/Naming Code Sheet.md`
   - If yes: use the existing codes. Do not invent new ones unless the brief introduces a genuinely new persona/pain/motivation.
   - If no: you'll need to generate one first (see Mode A below).

## Two Modes

### Mode A: Generate a Naming Code Sheet for a New Client

**Input needed:** The client's Creative Strategy Brief, or at minimum: their offer, ICP, key personas, known pain points, and desired outcomes.

**Process:**

1. Read the Creative Strategy Brief (check `knowledge-base/` and `outputs/` for the brief)
2. Extract every distinct persona / problem category → these become **Issues**
3. For each Issue, extract 3–5 specific pain points → these become **Pains**
4. For each Issue, extract 3–5 desired outcomes → these become **Motivations**
5. Assign codes following these rules:
   - 2–5 characters, UPPERCASE
   - Memorable and unambiguous — someone should be able to guess what the code means
   - No overlap with existing universal codes (Creative Type, Format, Hook, Tag)
   - No overlap with other client-specific codes in the same sheet
6. Present the full Code Sheet for sign-off before saving

**Output format:**

```markdown
# [CLIENT] — Naming Code Sheet
**Last updated:** [DATE]
**Maintained by:** your media buyer
**Location:** This is the single source of truth for all ad naming codes.

---

## Issues (Personas)
| Code | Full Name | Description |
|------|-----------|-------------|

## Pains (by Issue)
| Issue | Code | Pain Point |
|-------|------|------------|

## Motivations (by Issue)
| Issue | Code | Motivation |
|-------|------|------------|

## Universal Codes
Creative Type, Format, Hook, and Tag codes are standardised across all accounts.
See the "Universal Code Reference" section below for the full list.

---

## Deprecated Codes
| Old Code | Replaced By | Date | Reason |
|----------|------------|------|--------|
```

**Save to:** `outputs/Naming Code Sheet.md` — only after the account owner approves.

---

### Mode B: Generate Ad Names from a Concept List

**Input needed:** A list of concepts to name. For each concept, you need to know (or infer from context):
- What Issue (persona) it targets
- What Pain it leads with (if specific)
- What Motivation it appeals to (if specific)
- What Creative Type it is (UGC, FOUND, STATIC, etc.)
- What Format (VID, IMG, REEL, CARO)
- What Hook strategy the opening uses
- A short description of the actual creative (becomes the concept slug)
- What Tag applies (NC for new, HO for hook variation, etc.)
- Age bracket (if the creative is age-specific)

**Process:**

1. Load the client's Naming Code Sheet from `outputs/Naming Code Sheet.md`
2. For each concept in the list:
   a. Match to the correct Issue code
   b. Match to Pain and Motivation codes (if applicable — if broad, use shortened format)
   c. Identify Creative Type, Format, and Hook from the description
   d. Generate the concept slug: lowercase, hyphenated, max 5 words, descriptive enough to picture the ad
   e. Apply the correct Tag
   f. Assemble using the snake_case format:
      - Full: `[AGE]_[ISSUE]_[PAIN]_[MOTIVATION]_[CREATIVE_TYPE]_[FORMAT]_[HOOK]_[CONCEPT]_[TAG]`
      - Shortened: `[ISSUE]_[CREATIVE_TYPE]_[FORMAT]_[HOOK]_[CONCEPT]_[TAG]`
3. If any concept requires a code that doesn't exist in the Code Sheet, flag it:
   > "This concept introduces a new [Issue/Pain/Motivation] not in the Code Sheet: [description]. Proposed code: `[CODE]`. Add to Code Sheet?"
4. Present all names in a table for review

**Output format:**

| # | Concept Description | Ad Name | Notes |
|---|--------------------|---------| ------|
| 1 | Kathy's testimonial about inflammation, story hook, video | `55-70_BP_ARTHRITIS_GRANDKIDS_TESTI_VID_STORY_kathy-inflammation_NC` | |
| 2 | Selfie video about outdated flows, pattern interrupt hook | `OUTFLOW_SELFIE_VID_PATTERN_still-using-2020-flows_NC` | |
| 3 | Hook variation of the Mark Cuban ad (hook 2) | `OUTFLOW_FOUND_VID_PROOF_mark-cuban-case-h2_HO` | Hook var of existing winner |

**If generating hook variations of an existing ad:**
- Keep everything the same except the concept slug (append the hook identifier) and the Tag (`HO`)
- Example: original is `OUTFLOW_FOUND_VID_CALLOUT_mark-cuban-case_NC` → hook variation is `OUTFLOW_FOUND_VID_PROOF_mark-cuban-case-h2_HO`

---

## Universal Code Reference (Do Not Modify Per Client)

### Creative Type
| Code | Meaning |
|------|---------|
| `UGC` | User-generated content style |
| `TESTI` | Testimonial |
| `FOUND` | Founder-to-camera |
| `STATIC` | Static image + body copy |
| `PARTN` | Partnership / whitelist ad |
| `COMP` | Compilation (multiple clips) |
| `SCREEN` | Screen recording / walkthrough |
| `NOTE` | Notepad-style ad |
| `SELFIE` | Selfie-style video |
| `ANIM` | Animation / motion graphics |

### Format
| Code | Meaning |
|------|---------|
| `VID` | Video (edited) |
| `IMG` | Single image |
| `REEL` | Reel (organic style) |
| `CARO` | Carousel |

### Hook
| Code | Meaning |
|------|---------|
| `FEAR` | Fear-based / loss aversion |
| `DESIRE` | Outcome / aspiration |
| `QUESTION` | Direct question |
| `AUTHORITY` | Credibility / expert framing |
| `STORY` | Narrative / testimonial opening |
| `PATTERN` | Pattern interrupt / contrarian |
| `APOLOGY` | Apology / switcheroo |
| `PROOF` | Data / results led |
| `CALLOUT` | Direct callout of ICP |

### Tag
| Code | Meaning |
|------|---------|
| `NC` | New Concept |
| `WC` | Winning Concept |
| `HO` | Hook Variation |
| `WCO` | Winning Combination |
| `IT` | Iteration |
| `DUP` | Duplicate |
| `REV` | Revived |

---

## Rules

1. **Never invent a code.** If the concept needs a code that's not in the client's Code Sheet, flag it for addition. Don't improvise.
2. **snake_case format only.** Underscore between variables. Hyphens within multi-word concept slugs. No spaces ever.
3. **Concept slugs must be descriptive.** `mark-cuban-case` is good. `ad1` is not. Someone should be able to picture the ad from the slug alone.
4. **Use shortened format when Age, Pain, or Motivation aren't specifically targeted in the creative.** Don't pad the name with variables that aren't actually being tested.
5. **One concept = one Issue.** If an ad targets two personas, it's probably too broad. Flag it.
6. **Present names for review before they go live.** the account owner confirms before anything gets uploaded to Meta.
7. **UTMs must include `{{ad.name}}`** in the `utm_content` parameter so the naming convention flows into attribution data.
