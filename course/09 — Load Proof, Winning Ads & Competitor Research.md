# Step 09 — Load Proof, Winning Ads & Competitor Research

**Time:** 15 min
**Goal:** Populate `knowledge-base/winning-ads/` and `knowledge-base/research/` with the rest of the critical inputs.

---

## The Three Data Sets

### 1. Winning Ads (`knowledge-base/winning-ads/`)

Text of your best-performing ads. Not links. Not screenshots. **The actual script/copy.**

Why: the Script Generator skill mirrors the tone, pacing, and structure of your winners when writing new scripts. Without these, it has no reference for what sounds like YOU.

**What to include:**
- Top 3-5 performers by conversion (not clicks)
- Include the hook, lead, body, and CTA — the full script
- If it's a video, transcribe the script word-for-word

**File naming:**
```
[Winner #1] — [Performance metric] — [Date range].txt
```

Example:
```
Winner 1 — $42 CPL over 3 months — Jan-Mar 2026.txt
Winner 2 — 30x ROAS single campaign — Feb 2026.txt
```

---

### 2. Proof Assets (`knowledge-base/research/proof/`)

Testimonials, case studies, results, screenshots, revenue numbers. These get matched to specific personas later — the system uses them as credibility anchors in ads.

**What to include:**
- Text testimonials (copy the full text, not just a quote)
- Case studies (what they had before, what you did, what they got)
- Results screenshots (describe what's in them — Claude can't read images directly yet)
- Revenue numbers for specific clients
- Before/after data

**Organize:**
```
knowledge-base/
  research/
    proof/
      testimonials.md        ← All testimonials in one file
      case-studies.md        ← All case studies in one file
      results-screenshots.md ← Description of screenshot contents
```

---

### 3. Competitor Research (`knowledge-base/research/competitors/`)

What your competitors are running. This informs differentiation — if everyone's running "Get 100 leads in 30 days," that's what you DON'T want to say.

**How to get it:**

1. Go to **facebook.com/ads/library**
2. Search your top 3-5 competitors
3. Filter by "Meta ads" and current active
4. For each competitor, document:
   - Which angles they're using (problem-awareness, promise, proof-based, etc.)
   - Which formats (UGC, talking head, carousel, VSL)
   - Which hooks they lead with
   - What their offer is

**Organize:**
```
knowledge-base/
  research/
    competitors/
      competitor-1-[name].md
      competitor-2-[name].md
      competitor-3-[name].md
```

Each file should have: angles, formats, hooks, offer, positioning.

---

## The Prompt

Once all three datasets are loaded, paste this into Claude:

```
Confirm what's in my knowledge-base/. List:
- How many sales call transcripts in sales-calls/
- What's in winning-ads/
- What's in research/proof/
- What's in research/competitors/

Tell me if anything is thin or missing. Flag specifically:
- If I have fewer than 5 sales calls → not enough
- If I have no winning ads → ok for new accounts, but note it
- If I have fewer than 3 competitors researched → flag
- If I have no proof assets → flag, this weakens every persona match

Don't proceed with any analysis yet. Just verify the data is ready.
```

---

## A Note On "New Accounts"

If you're running a brand new ad account with no winners yet, that's fine. Put a note in `winning-ads/NEW-ACCOUNT.md` that says:

```
New account. No winning ads yet. System should lean heavier on
competitor references and format library for structural decisions.
```

Claude will work with this. But you'll want to start collecting winners as soon as ads start converting.

---

## ✅ Checkpoint

- [ ] 3-5 winning ad scripts (text form) in `knowledge-base/winning-ads/`
- [ ] Proof assets (testimonials, cases, results) in `knowledge-base/research/proof/`
- [ ] 3-5 competitors researched with angles/formats/hooks in `knowledge-base/research/competitors/`
- [ ] Claude confirmed everything is loaded and ready

Move to **Step 10 — Run Your First Creative Strategy**.
