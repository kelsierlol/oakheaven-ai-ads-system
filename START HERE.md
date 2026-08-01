# Start Here

This folder is your ads system. Claude reads your business out of it and does the work — research into
personas, personas into scripts, scripts into campaigns, campaigns into daily decisions.

## Opening it

```
git clone https://github.com/kelsierlol/oakheaven-ai-ads-system.git oakhaven-ads
cd oakhaven-ads
claude
```

If you'd rather use the Claude Code desktop app, open it and add the `oakhaven-ads` folder. Either way, the
only thing that matters is that Claude is pointed at this folder — that's what loads your business context.

Full install walkthrough, including getting Claude Code on your machine: `SETUP GUIDE.md`, Phases 1 and 2.
The rest of that guide is already done.

---

## Read this before you start

The system is running in an interim mode right now, on purpose. Here's the honest version.

Everything the system currently knows about your customers came from **your competitors** — 18 of their live
ads ripped and transcribed, plus about 115 verbatim customer quotes from their testimonials, reviews and
forum threads. It's real language from real people in your market. It is not from *your* buyers.

That's a deliberate trade. It means you can start now instead of waiting a month. It also means the personas
and angles the system produces this week are **educated bets, not conclusions**, and Claude will label them
that way in its output. Don't read them as settled.

The fix is sales calls. Once five of them are recorded and dropped into `knowledge-base/sales-calls/`,
the system rebuilds the strategy on your actual buyers and the confidence flags come off.

So: two phases.

---

## Phase 1 — this week

**1. Answer Part 1 of `outputs/client-gap-questionnaire.md`.**
Sixteen questions, most are one-liners. Price, what a package includes, which action you actually want the
ads to drive, what you're using for booking and tracking, budget, your name and how long you've been running.
Where you don't know a number, write "don't know" — a wrong number is worse than a blank one.

This is the highest-leverage thing you can do. It unblocks the pricing model, the media buying plan, the
campaign structure, and the value argument in every single script.

**2. Start recording your sales calls today.**
Fathom's free tier does it automatically. This is the only item that gets the system fully out of interim
mode, and it runs on its own once it's set up — so start it now, not after everything else.

**3. Make the side-by-side video.**
One piece of footage. A generic edit of it, next to your team's edit. Same segment, same audio.

Your whole offer is a claim about something visual, being made in a visual medium, and right now there's
nothing visual proving it. Your own VSL script marks the spot for this and calls it your most powerful proof
element. Three of the draft ad scripts are waiting on it.

**4. Then ask Claude for the work.** In plain English:

| Say this | You get |
|---|---|
| "Read the asset inventory and tell me where we stand" | A scorecard of what the system has and what's missing |
| "Run the KPI Tracker" | Max cost per customer, break-even ROAS, target cost per booked call |
| "Run a creative strategy" | Scored personas and the angle map — flagged as hypotheses until calls land |
| "Write 5 ad scripts from that" | Storyboards, 3 hook variations each, quality-checked |
| "Build my media buying SOP" | Budget rules, when to kill an ad, when to scale it |

Finished work lands in `outputs/`.

---

## Phase 2 — once you have 5 recorded calls

Drop the transcripts into `knowledge-base/sales-calls/` and say:

> "I've added 5 sales calls. Re-run the creative strategy on my own customer data."

The system swaps the borrowed research for yours, rebuilds the personas properly, and the low-confidence
flags come off. Scripts written after that point are grounded in what your actual buyers said, including
the objections that come up at your actual price — which is the one thing competitor research can never
tell you.

---

## Where things live

| Folder | What's in it |
|---|---|
| `context/` | Your offer, customers, voice, positioning. Claude reads this every session. |
| `knowledge-base/` | The research. Drop sales calls, testimonials and winning ads in here. |
| `outputs/` | Finished work — briefs, scripts, reports, SOPs. |
| `memory/open-loops.md` | Running list of what's unfinished and what's still needed from you. |

## One thing that's already settled

Worth knowing before you look at any creative: the original VSL — the one built around the in-house-payroll
cost comparison, a dedicated project manager, unlimited revisions, fixed price and the 14-day guarantee — is
being run almost word for word by two of your competitors right now, with bigger teams behind it. It's in
`knowledge-base/research/competitors/ad-teardown.md` with timestamps.

So that direction is retired. What's left is the thing none of the 18 competitor ads claim: that your editors
understand what you *mean*, not just what you said. That lane is empty and it's the one the system is
building everything around.
