# Oakhaven Media — AI Ads System

Your ad workspace. Claude reads your business context and runs the skills that turn research into scripts, campaigns and daily media buying decisions.

## Start here

```
claude
```

Run that inside this folder. Claude loads your context automatically. Then ask for what you want in plain English — no commands to memorise.

## The two things you do

**1. Drop files in.** Everything the system learns comes from these folders:

| Put this here | Folder |
|---|---|
| Sales call transcripts | `knowledge-base/sales-calls/` |
| Testimonials, case studies, results | `knowledge-base/research/proof/` |
| Scripts of ads that performed | `knowledge-base/winning-ads/` |
| Anything else — surveys, reviews, notes | `knowledge-base/research/` |

Text files. Claude reads them next session.

**2. Ask for the work.**

| Say this | You get |
|---|---|
| "Run a creative strategy" | Scored personas, micro-personas, the strategy map |
| "Write 5 ad scripts from this brief" | Storyboards with 3 hook variations each, QC'd |
| "QC these scripts" | 13 per-script + 3 batch checks against direct response standards |
| "Run the KPI Tracker" | Max CAC, break-even ROAS, target CPR |
| "Build my Media Buying SOP" | Budget brackets, kill/scale rules, daily protocol |
| "Run my daily check-in" | Today's moves on the account |
| "Run a bottleneck analysis" | Why performance dropped, ranked by cause |

Finished work lands in `outputs/`.

## What's already done

Competitor research is complete — 18 live competitor ads ripped and transcribed, pricing across the market, and ~115 verified customer quotes from competitor case studies and forums. All in `knowledge-base/research/`.

Read `outputs/asset-inventory-2026-07-31.md` first. It's a scorecard of what the system has and what it's missing, and it says exactly what to send to unblock the rest.

## What's still needed from you

In priority order:

1. **Your price and package structure** — blocks the KPI model and half the copy
2. **Sales call recordings** — start recording from your next call. Fathom's free tier does it automatically. At 5 transcripts the personas get rebuilt properly.
3. **One side-by-side video** — a generic edit next to your team's edit of the same footage
4. **Team capacity and monthly budget** — sets the testing structure

Full list with reasoning: `outputs/client-gap-questionnaire.md`

## Folders

```
context/          Your offer, ICP, personas, voice, positioning
knowledge-base/   What you upload — calls, proof, winning ads, research
outputs/          Finished briefs, scripts, SOPs, reports
memory/           What's open between sessions
skills/           The 16 skills Claude runs
course/           15-chapter operator course, if you want the theory
```

## Updating

`git pull` brings engine updates. Your data in `context/`, `knowledge-base/`, `outputs/` and `memory/` is untouched.

Stuck? Check `SETUP GUIDE.md` or ask on the next call.
