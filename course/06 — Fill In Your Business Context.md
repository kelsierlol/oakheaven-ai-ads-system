# Step 06 — Fill In Your Business Context

**Time:** 15 min
**Goal:** Populate `context/business.md` with your offer, ICP, voice, and positioning.

---

## Why This Matters First

The business context file is the foundation every skill runs off. When Claude writes an ad script, it's drawing from this file. When it builds a persona, it references this. When it diagnoses a funnel, it checks against this.

If this file is vague or generic, everything downstream is vague or generic. If this file is specific and accurate, everything downstream is too.

You have two options for filling it out:

### Option A: Interview Mode (Recommended)

Let Claude interview you. It'll ask you one question at a time, you answer, it writes the file. Takes 15-20 minutes.

### Option B: Write It Yourself

Open `context/business.md` directly and fill in the template. Works if you already have a lot of this documented.

---

## The Prompt (Interview Mode)

Paste this into Claude:

```
I want to fill out my context/business.md using an interview.

Ask me one question at a time about my business. Cover:

1. Offer — what I sell, pricing, what the customer gets
2. Unique mechanism — what makes my approach different
3. ICP — who my ideal customer is (demographics, situation)
4. Avatars / personas — the specific types of people within my ICP
5. Voice & tone — how my brand sounds in marketing
6. Competitive positioning — main competitors and how I'm different
7. Proof assets — testimonials, case studies, results I can reference
8. Known objections — top 3-5 reasons people don't buy on sales calls

Ask me one at a time. Don't move to the next question until I've given
you a specific, detailed answer. If I'm vague, push back and ask me
to be more specific.

When we're done, write the complete file to context/business.md based
on my answers. Show me the draft before saving it.
```

---

## How To Give Good Answers

When Claude asks a question, answer like you would to a smart colleague who knows your industry but not your business.

**Bad:** "I help businesses grow."
**Good:** "I run lead generation for construction trades — roofers, solar, bathrooms — charging $2,500/month retainer, delivering 40-80 qualified leads per month via Facebook ads and lead forms."

**Bad:** "Our customers are business owners."
**Good:** "Our best customers are trade business owners making $70K+/month who have 3-10 staff, are busy running their book but hitting a lead flow ceiling. Not startup tradies — they can't afford us and churn fast."

**Bad:** "Our offer is good value."
**Good:** "We guarantee qualified leads within 14 days or we don't charge. Our unique mechanism is proprietary audience research using YouTube comment data, not just Meta interests — this is why our lead quality is 2x industry average."

---

## If You Don't Know Something

That's fine. Flag it to Claude: "I don't know my exact close rate from Facebook leads — can you note that as a gap?" Claude will flag it in the file and move on. You can fill it in later.

---

## Verify

After Claude writes the file, open `context/business.md` in a text editor. Read it back. Does it actually describe YOUR business, not a generic agency? If it feels like a template, it is — go back and make it specific.

---

## ✅ Checkpoint

- [ ] `context/business.md` is filled in (not a template)
- [ ] Offer, ICP, and voice are all specific — not generic
- [ ] Proof assets and objections are listed
- [ ] Anything you didn't know is flagged as a gap
- [ ] You've read the file back and it describes your business accurately

Move to **Step 07 — Set Up Your Ad Account Context**.
