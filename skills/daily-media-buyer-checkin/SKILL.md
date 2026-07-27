---
name: daily-media-buyer-checkin
description: A structured daily workflow for managing and optimizing Meta Ads accounts. Use this skill when the user asks for a "daily review", "daily check-in", "media buying review", or wants to check daily pacing, creative performance, and make routine kill/scale decisions.
---

# Daily Media Buyer Check-in

This skill provides a structured, repeatable daily workflow for media buying on Meta Ads. It is designed to be account-agnostic, meaning it adapts to the specific client's funnel type, target KPIs, and campaign structure.

## Prerequisites & Inputs

Before running the daily check-in, ensure you have the following inputs from the user or the account context:
1. **Funnel Type:** Is this a Lead Gen or Direct Purchase (e.g., app/subscription) account?
2. **Target KPIs:** What is the target Cost Per Result (CPA/CPL/CPP) and ROAS?
3. **Campaign Structure:** What are the core funnel groupings and naming conventions? (e.g., Quiz/Hybrid/VSL for an app account)
4. **Third-Party Attribution Data (Lead Gen accounts):** For lead gen accounts, always request that the user provides Hyros (or equivalent) data for the same date range before proceeding. Meta's in-platform metrics can over- or under-attribute results by up to 30%, making them unreliable as a standalone source of truth for kill/scale decisions. Use Meta data for spend and engagement metrics (CPM, CTR, CPLC). Use third-party data for leads, cost per lead, show rate, close rate, and ROAS.
5. **Winning Ad Assets (for creative analysis):** If the session includes a creative iteration or sequence engineering step, ask the user to share the copy and/or video of the top-performing ad(s) so they can be analysed directly. Do not attempt to infer creative content from metrics alone.

## The Daily Workflow

Execute the following steps in order. Always pull data before making recommendations.

### Step 1: The Bottleneck Early Warning Layer
Before making any kill/scale decisions, run a quick metric health check across the following indicators and flag any that are trending poorly vs. the prior period (e.g., Last 3 Days vs. Prior 3 Days):

| Metric | What a Bad Trend Looks Like | What It Suggests |
|---|---|---|
| **CPM** | Rising sharply (>20% week-on-week) | Auction getting more expensive; creative fatigue or audience saturation |
| **Cost Per Link Click (CPLC)** | Rising | Hook or creative quality declining |
| **Click-to-LPV Rate** | Falling (healthy benchmark: >70–75%) | Page load speed issue, tracking problem, or bad mobile experience |
| **LPV-to-Conversion Rate** | Falling | Landing page or offer problem |
| **ROAS / CPP trend** | Deteriorating over 3–4 day window | Funnel-level issue — warrants full bottleneck analysis |
| **AOV** | Dropping | Product mix or offer change affecting revenue per purchase |

*Action:* If two or more of these are trending badly simultaneously, recommend escalating to a full bottleneck analysis using the dedicated skill rather than trying to fix it through ad-level optimization.

### Step 2: Account Pulse & Funnel Triage
Pull account-level and funnel-level insights for three timeframes: **This Month**, **Last 7 Days**, and **Last 3–4 Days**.
- **Trajectory:** Is the overall CAC improving, flat, or deteriorating? This sets the tone for the session.
- **Funnel-by-Funnel:** Work through each funnel group in sequence. Flag any funnel where the 3–4 day CAC is moving in the wrong direction relative to the 7-day average.

### Step 3: Identify Campaign Structure
Before applying any kill/scale rules, identify the type of campaign the ad sits in:
- **Testing Campaign (ABO):** Each ad set has its own budget. Apply kill rules cautiously. If the ad set as a whole is healthy, do not kill low-spend ads inside it—Meta may be sequencing them.
- **Scaling Campaign (CBO/Advantage+):** Budget is distributed at the campaign level. Do not make ad-level kill decisions based on spend distribution alone. Only kill if an ad has genuinely breached the threshold over a meaningful window (7+ days) with no results.
- **Top-of-Funnel / Awareness:** Do not apply direct CPA kill rules. Evaluate on CPM, CTR, and LPV rate.
- **Warm Audience / Retargeting:** Apply kill rules with a tighter threshold and shorter window, as these audiences fatigue faster.

### Step 4: Ad-Level Kill/Scale Execution
Drill down to the ad level for flagged campaigns and apply the rules mechanically based on the funnel type.

**Lead Gen Accounts:**
- **Kill:** Spend ≥ 1x target CPA with 0 results.
- **Watch/Flag:** Spend ≥ 2x target CPA with 1 result. *Prompt user:* "Check Hyros for this lead's show rate and close rate before deciding."
- **Scale:** Performing at or below target CPA with volume. Increase budget 10–20%, wait 2–3 days before next increase.

**Direct Purchase / App Accounts (subscription/membership):**
- **Kill:** Spend ≥ 1.2x target CPA with 0 results.
- **Kill:** Spend ≥ 1.8x target CPA with 1 result (unless ROAS is strong due to high AOV—flag if ambiguous).
- **Scale:** Performing at or below target CPA with volume. Increase budget 10–20%.
- **Promote:** Extract standout winners from testing to a dedicated scaling campaign (do not duplicate inside the same campaign to avoid fragmentation).

### Step 5: Critical Thinking & Creative Iteration
Look beyond the basic kill/scale thresholds for hidden opportunities in the data:
- **High Hook Rate (>35%):** If an ad stops the scroll but fails to convert, test the winning hook with a new ad body.
- **Sequence Engineering:** Ask the user to share the copy and/or video of the top-performing ad and the landing page URL. Analyse both directly — think through every question or concern a first-time viewer would have after seeing that ad (e.g., "What was she eating?", "Any side effects?", "Was she still going out at weekends?"). Prescribe specific new ads that answer each question directly (e.g., full day of eating, comment reply videos, candid lifestyle content) and let Meta sequence them naturally.
- **Awareness Stage Iteration:** Take a winning ad, use AI to classify its current awareness stage (Unaware / Problem Aware / Solution Aware / Product Aware / Most Aware), then prescribe how to adapt it to appeal to a higher or lower awareness stage to reach a new audience segment.
- **Angle & Avatar Coverage:** Check whether the account is over-indexed on one persona, pain point, or angle. Flag any underrepresented persona that has historically performed well but is not currently receiving spend.

### Step 6: Weekly Mining / Revive (Run Weekly, Not Daily)
Once a week, filter the account for ads that are currently paused/off and have not been active for 14+ days.
- Sort by all-time purchases/results descending.
- Flag any ad that spent >$1,000–$2,000 at below the target CPA.
- Output a shortlist of "revive candidates" to be re-launched in a new testing campaign, turned back on at a test budget, or used as creative references.

### Step 7: Experimental Campaign Sweep
Filter for any campaigns outside the named funnel structure. Review these separately, as they are often the silent drivers of a high overall account CAC.

## Output Format: The Daily Report

Deliver the findings using the following structured format:

---

# 📅 Daily Media Buyer Check-in: [Account Name]
**Date:** [Current Date] | **Lookback Window:** Last 3-4 Days vs Last 7 Days

### 🚨 1. Bottleneck Early Warning
*   [Metric] is trending [Up/Down]. [Brief interpretation].

### 📊 2. Account Pulse & Trajectory
*   **Trajectory:** [Improving / Flat / Deteriorating]
*   **Efficiency:** [CPP/CPL] at $[X] | ROAS at [X]x
*   **Target KPI Status:** [Meeting / Missing by X%]

### 🎯 3. Kill / Scale Decisions (Action Required)
*   🔴 **KILL:** `[Ad Name]` - Spent $[X] (>[Threshold]) with 0 results.
*   🟡 **WATCH/FLAG:** `[Ad Name]` - [Reason based on funnel rules].
*   🟢 **SCALE:** `[Ad Name]` - Driving volume at $[X] CPP (well below target).

### 🧠 4. Critical Thinking & Iteration Opportunities
*   **Hook Rate Signal:** [Note any ad with >35% hook rate that is failing to convert — suggest new body test].
*   **Sequence Engineering:** [If winning ad assets were provided, list the specific audience questions to address with new creative].
*   **Awareness Stage:** [Note the winning ad's current stage and suggest how to move it up].
*   **Persona Coverage:** [Flag any underrepresented angle or avatar].

### ⛏️ 5. Weekly Revive Candidates (If Applicable)
*   [List of high-performing inactive ads].

---
*Ready to execute these changes? Let me know and I can apply the kills/scales directly or provide the specific ad IDs.*
