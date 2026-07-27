---
name: creative-strategy
description: Use this skill whenever a user needs to build a creative strategy, creative brief, or creative map for a client ad account. Triggers include any mention of "creative brief", "creative strategy", "persona research", "ad strategy", "creative map", "first brief", "onboard a new client creatively", "build personas for ads", "micro personas", or any request to turn raw customer research into a structured plan for ad creation. This skill takes raw research inputs (sales call transcripts or user survey data, customer data, competitor research, offer details, and winning ad history) and produces a hypothesis-driven creative strategy map with macro personas decomposed into micro personas (each with distinct fears, motivators, cognitive biases, veilance zones, and self-concept anchors), scored and prioritized, ready to hand off to the ad scripting/concept creation process. Do NOT use this skill for writing actual ad scripts or concepts. This produces the strategy that informs the scripts.
---

# Creative Strategy Brief Builder

Turns raw client research into a hypothesis-driven creative strategy map with deeply specific, scored persona profiles and a fully populated creative strategy map. Every output is framed as a testable hypothesis, not a conclusion. The ad account proves or disproves it.

## Core Philosophy

Everything this skill produces is a bet, not a fact. The data informs the hypothesis. The ad account validates it. Frame every insight, every persona, every angle as: "Based on X data, we believe Y persona will convert on Z angle." Never: "This persona converts on this angle."

The number one goal: get as close to the customer as possible. He who is closest to the customer always wins. Every insight must be specific enough that it could only apply to ONE persona. If you could swap the persona name and the insight still makes sense, it is not specific enough. Redo it.

None of the singular pieces of data fed into this skill are hard and fast rules. They are reference points that need to be synthesized into an answer to one question: how can this product sell to a complete stranger?

---

## When To Use This Skill

- When onboarding a new client and building their first creative brief
- When resetting creative strategy for an existing client whose account has plateaued
- When a client enters a new market or launches a new offer and needs a fresh strategy
- When the user says anything like: "build me a creative strategy", "I need a creative brief", "let's do persona research for [client]", "map out the creative for [client]"

---

## What You Need Before Starting (Pre-Flight)

Before any analysis begins, validate that the user has provided all required inputs. Do not proceed without the five hard-gate inputs. Push back firmly if anything is missing or thin.

### Hard Gate Inputs (ALL required before proceeding)

<instructions>
Check for each of these five inputs. If any are missing, stop and tell the user exactly what is needed, why it matters, and that you cannot proceed without it. Be direct. Do not soften this.
</instructions>

1. **Sales Call Transcripts**
   - Minimum 5 transcripts. Ideal is 10+.
   - Must be recent and diverse. 10 calls from the same campaign or the same customer type is not sufficient. Push the user: "These 12 transcripts all seem to come from similar prospects. Do you have calls from different customer types, different objection patterns, or different stages of the funnel?"
   - Format: Text transcripts uploaded as files or pasted into chat. Audio files are not usable without transcription.

2. **Client Customer Base Data**
   - Who is currently buying and why. Demographics, purchase history, application/intake form data, or CRM exports.
   - This tells you who the ACTUAL buyers are, which may differ from who the client thinks their customers are.
   - Format: Spreadsheet exports, form response data, or summary documents.

3. **Competitor Research Document**
   - A pre-compiled document from the separate competitor research process. Must include: competitor ad angles currently running at scale, formats being used, personas being targeted, positioning and messaging analysis, and identified gaps.
   - If the user does not have this, stop. Tell them: "The competitor research document is non-negotiable. It informs our angle selection, format decisions, and differentiation strategy. Go run the competitor research process first and come back with the compiled document."

4. **Offer Briefing**
   - Must include ALL of the following:
     - **Core offer deliverables**: What does the customer literally receive? Not the marketing pitch. The actual modules, meals, calls, software access, materials, etc.
     - **Unique mechanism**: Why does this work? What is the specific approach, method, or system that differentiates this offer? If the mechanism sounds like everyone else's, flag it.
     - **Price point and offer structure**: Is this a $47 front-end, a $997 program, a $5k+ high-ticket? This directly affects which personas are viable from cold traffic. A high-ticket offer will not convert an unaware, low-urgency persona from cold.
     - **Proof assets**: What results, testimonials, case studies, and data points exist? List them with enough detail to match them to specific persona types later.
     - **Known objections from sales**: Beyond what is in the call transcripts, what objections does the sales team hit repeatedly?
     - **Founder or brand story** (if applicable): Is there a personal narrative that adds credibility? This matters for actor/archetype selection.
   - If the user cannot provide the core offer, mechanism, price point, and proof assets, refuse to proceed. Without these, the value prop mapping is guesswork.

5. **Previous Winning Ads and Formats**
   - What ads and formats have already worked in this account? What entity IDs (concepts) are currently spending and converting?
   - This prevents reinventing the wheel and tells you which entity IDs already exist.
   - **Exception**: If the client is brand new with zero ad history, accept this as the only valid exception. Note it as a gap and lean heavier on competitor format data for format recommendations.

### Soft Inputs (Ask for these. Proceed without them but flag the gap.)

- Survey or form response data (pre/post-program, intake surveys, Typeform responses)
- Customer support chat logs and emails
- Online reviews (G2, Capterra, Trustpilot, etc.)
- Social media comments and community posts

If a soft input is missing, note it as a blind spot in the final output. Example: "Persona profiles were built without direct customer survey data. Self-reported barriers and desires may be underrepresented. Treat barrier-related insights for these personas with lower confidence."

### User Thesis Collection

After validating all inputs, ask the user:

"Before I start processing the data, what's your gut read? Which customer types do you think are the strongest opportunities and why? This doesn't need to be polished. Just tell me who you think the money personas are."

<instructions>
Treat the user's thesis as a HYPOTHESIS to validate or invalidate against the data. Do NOT treat it as a directive. The user's instincts are data, not commands. At the end of the persona scoring step, explicitly tell the user whether their initial thesis was confirmed, partially confirmed, or contradicted by the data, and show the evidence.
</instructions>

---

## Process

### Step 1: Input Validation and Data Quality Assessment

Read all uploaded inputs. Before beginning analysis, assess data quality and flag any issues.

<instructions>
For each input source, assess:
- Volume: Is there enough data to draw meaningful conclusions?
- Diversity: Does the data represent a range of customer types, or is it skewed toward one profile?
- Recency: Is the data current, or could it be outdated?
- Relevance: Does the data actually speak to purchase behavior and customer motivation, or is it operational/surface-level?

Flag every issue you find. Be specific: "The 8 transcripts provided are all from the same webinar funnel. 6 of the 8 prospects mention the same pain point (weight loss after 50). This data is heavily skewed toward one customer profile. The personas built from this will be weighted toward that profile."

Do NOT stop if the data is imperfect. Flag the gaps, then proceed. Perfect data does not exist. But the user and the downstream team need to know where the analysis is thin.
</instructions>

---

### Step 2: First-Pass Tagging and Extraction

Read through ALL input data and tag every relevant insight across nine dimensions. This is the most critical analytical step. Be thorough. Miss nothing.

<instructions>
For every line, quote, data point, or insight in the input data, apply tags from the following nine dimensions. A single piece of data can carry multiple tags.

Use the customer's exact language wherever possible. Do not clean it up, rewrite it, or make it sound like marketing copy. The raw language IS the insight.

**CRITICAL — Awareness-Level Segmentation of Customer Language:**

As you tag customer language (Dimension 9), you must also assign an awareness level to each phrase. This segmentation is a hard requirement for the downstream scripting skill. Without it, the scripting skill cannot write awareness-appropriate copy.

Segment every verbatim phrase into one of these buckets:

| Awareness Level | What the phrase sounds like | Where to find it |
|-----------------|---------------------------|------------------|
| **Unaware** | Describes symptoms without naming the problem. Daily frustrations not yet connected to the product category. "I'm just tired all the time." | Social media comments, forum posts, early sales call language before the prospect knew about the solution, Amazon reviews of competing products, Reddit threads |
| **Problem-Aware** | Labels the problem. Describes what they've tried. Why they're frustrated with existing approaches. "I've tried everything and nothing sticks." | Sales call transcripts (early in call), review sites, competitor comment sections |
| **Solution-Aware** | Compares solutions. Expresses scepticism. Asks for proof. "How is this different from X?" | Sales call transcripts (mid-call objections), competitor reviews, comparison forums |
| **Product-Aware** | Specific objections about THIS product. What's holding them back. "Is this just another subscription I'll cancel?" | Sales call transcripts (late-stage objections), abandoned cart surveys, support tickets |

**Important:** Sales call transcripts naturally skew toward Problem-Aware, Solution-Aware, and Product-Aware language — because the people on those calls already found you. Unaware language requires going to where the audience lives BEFORE they know you exist. If the Unaware bucket is thin after tagging, flag it explicitly to the user: "The Unaware language bank is thin. This limits the scripting skill's ability to write cold-traffic hooks. Consider sourcing language from: [social media comments on competitor posts, niche-specific Reddit threads, YouTube comment sections, Amazon reviews of adjacent products]."
</instructions>

**The Nine Tagging Dimensions:**

(See `references/creative-strategy-reference.md` for full definitions and examples of each dimension.)

1. **Pains**: Deep, specific frustrations and suffering. Tag the emotional weight, not just the category.
2. **Desires**: Dream outcomes in their words. Not the product. The emotional destination.
3. **Current State**: What they are doing now, what is working, what is not.
4. **Goals**: Concrete, measurable targets. Distinct from desires (which are emotional).
5. **Barriers and Objections**: Practical and psychological blockers to buying or acting.
6. **FAQs**: Recurring questions that signal confusion, uncertainty, or unresolved concerns.
7. **Triggers**: Events or moments that pushed them from passive to active. Hook gold.
8. **Trends**: Patterns across data sources, market shifts, recurring themes.
9. **Customer Language**: Exact phrases and expressions. Tag VERBATIM. Do not paraphrase.

<instructions>
CRITICAL: Value prop matching does NOT happen in this step. That requires personas to exist first. During tagging, you may note where an offer element could connect to a tagged insight, but do not force the mapping. Full value prop mapping happens in Step 6 after personas are selected.
</instructions>

---

### Step 3: Clustering into Proto-Personas

Group the tagged data into 8-15 proto-persona clusters.

<instructions>
**Clustering rules:**
- Each cluster must have a DISTINCT primary pain point AND a distinct desired outcome. If two clusters share the same primary pain and the same desired outcome, they are the same persona with different backstories. Merge them.
- 8 clusters minimum. 15 clusters maximum. This is a hard rule. Fewer than 8 means you are not looking hard enough at the data. More than 15 means you are splitting hairs.
- Name each cluster with a descriptive, memorable label. Not "Persona 1" but "The Frustrated Yo-Yo Dieter" or "The GLP-1 Side Effect Sufferer." The name should immediately tell someone who this person is.
- For each cluster, note the volume of data supporting it. A cluster backed by 12 transcript mentions and 8 survey responses is stronger than one backed by 2 mentions. Note this. It matters for scoring.

**Handling homogeneous data:**
If the input data is heavily skewed toward one customer type (e.g., all transcripts are from the same funnel and same profile), do the following:
1. Flag it to the user: "The transcript data skews heavily toward [type]. Personas built primarily from this data are weighted accordingly."
2. Proactively cross-reference the competitor research document, customer base data, and offer briefing to identify additional persona opportunities NOT represented in the transcripts.
3. Present these separately: "These personas emerged directly from your transcript data: [list]. These are additional opportunities I identified from your competitor research and customer base data: [list]. The second group has less direct data support but may represent significant untapped markets."
4. Let the user make the final call on which to include.
</instructions>

---

### Step 4: Persona Scoring

Score each proto-persona on two quantitative dimensions and list one qualitative context marker. See `references/creative-strategy-reference.md` for the full scoring framework with sub-factor scales.

**Dimension 1: Cold Traffic Convertibility (Score 1-10)**

How likely is this persona to convert from a cold traffic ad? Calculated from three weighted sub-factors:
- **Urgency** (40%): How acute is their pain? "Need to fix now" vs "nice to have someday."
- **Awareness Level** (30%): Problem-aware and solution-aware convert more readily than unaware.
- **Skepticism Level** (30%): Psychographic resistance to marketing. "Tried everything" = high skepticism. This is a trait of the persona, NOT a function of what proof the client has.

**Dimension 2: Market Scalability (Score 1-10)**

How large and creatively deep is this persona's market? Calculated from:
- **TAM** (50%): How many people fit this persona?
- **Creative Scalability** (50%): How many distinct angles and hooks before messaging is exhausted?

**Context Marker: Primary Awareness Level**

List their primary awareness level (Unaware through Most Aware) as context. Not scored. Ensures the user can see awareness distribution and avoid building a strategy that only speaks to one level.

<instructions>
Show all sub-scores alongside final scores so the user can see and challenge the reasoning. Round final scores to nearest whole number.
</instructions>

**Thesis Validation**

After scoring, explicitly address the user's initial thesis from pre-flight:

<instructions>
Compare the user's gut-read against scored results. State clearly:
- "Your thesis on [persona X] was confirmed. Here's why: [evidence]."
- "Your thesis on [persona Y] was partially confirmed. Right about [aspect], but data suggests [difference]."
- "Your thesis on [persona Z] was not supported. Data shows: [evidence]."
Be direct. This builds the user's judgment over time.
</instructions>

---

### Step 5: Human Checkpoint — Persona Selection

Present all 8-15 scored personas to the user in a clear ranked format.

<instructions>
Present as a table with columns: Rank, Persona Name, Cold Traffic Convertibility Score, Market Scalability Score, Primary Awareness Level, Data Confidence (High/Medium/Low based on how much data supports this cluster), and a one-sentence summary of the persona.

Then tell the user: "Select the top 5 personas to build out into full profiles. You can override my rankings. If you want to include a persona the data doesn't strongly support, that's fine. I'll flag it as a client-directed hypothesis so the media buyer knows it's a higher-risk test."

WAIT for the user to respond. Do not proceed until they have selected their 5.
</instructions>

---

### Step 6: Second-Pass Analysis — Value Prop and Proof Mapping

Now that the 5 personas are selected, go back through the offer briefing and proof assets and map them to each persona.

<instructions>
For each of the 5 selected personas:

1. **Value Prop Matching**: Which specific elements of the offer directly solve this persona's primary pain? Not the whole offer. The specific modules, features, methods, or deliverables that address THIS person's situation. Be precise: "The Week 2 hormone-balancing meal plan directly addresses The Menopause Struggler's core pain of hormonal belly fat" not "The program helps with weight loss."

2. **Proof Asset Matching**: Which testimonials, case studies, or data points would be most credible and compelling to this persona? Match based on similarity: a testimonial from someone who LOOKS and SOUNDS like the persona (same age, same starting problem, same language) is 10x more powerful than a generic success story. List the specific proof assets and note why they match.

3. **Mechanism Framing**: How should the offer's unique mechanism be explained to THIS persona specifically? The same mechanism can be framed differently for different personas. For a menopause persona, frame it around hormonal balance. For a convenience persona, frame it around simplicity and time savings. Same product, different frame.

4. **Objection-Specific Counters**: Based on this persona's specific barriers and objections (from tagging), what proof, logic, or reframe addresses each one?
</instructions>

---

### Step 7: Build Detailed Persona Profiles

For each of the 5 selected personas, build a comprehensive profile. This is a multi-page brief per persona. It is the primary working document the creative team will use.

<instructions>
Each persona profile must include ALL of the following sections. Do not skip any. Do not abbreviate. This is the core deliverable.

**1. Persona Name, Code, and Archetype**
- A memorable, descriptive name (e.g., "Menopausal Mary", "The GLP-1 Refugee", "Frustrated Fiona")
- A standardised persona code: `P[macro number]` (e.g., P1, P2, P3). This code carries through to micro personas (Step 8B), the Strategy Map, and ad account naming conventions.
- A one-sentence archetype description

**2. Demographics**
- Age range, gender, location patterns, marital/family status, income indicators
- Source this from the customer base data and transcript evidence. Flag if demographics are assumed rather than evidenced.

**3. The "Before" State (Their Current Reality)**
- A narrative paragraph (NOT bullet points) describing their life, daily experience, pains, and frustrations right now.
- Written in THEIR language, pulled directly from transcripts and survey data. Use their exact words and phrases.
- This should read like a diary entry from this person, not a marketing document.

**4. The "After" State (Their Dream Outcome)**
- A narrative paragraph describing what their life looks like after the transformation.
- Again, in their language. What do they actually say they want? Not what you think they should want.

**5. Current State — What They Are Doing Now**
- What solutions have they tried? What is working? What is not working?
- What is their current approach to the problem?
- This reveals their sophistication level and what they will compare your offer against.

**6. Key Pains (Ranked by Intensity)**
- Their top 3-5 pain points, ranked from most acute to least.
- Each pain must include a direct quote from the data that illustrates it.
- Each pain must be specific to THIS persona. "Wants to lose weight" is not a pain. "Has gained 20 pounds since starting menopause and her doctor told her it's increasing her diabetes risk" is a pain.

**7. Key Desires (Ranked by Pull)**
- Their top 3-5 desired outcomes, ranked from most motivating to least.
- Include direct quotes.

**8. Barriers and Objections**
- Every identified barrier and objection for this persona.
- For each, include the objection-specific counter from Step 6.

**9. FAQs Specific to This Persona**
- Recurring questions this persona type asks.
- These inform ad copy (address the FAQ before they ask it) and landing page content.

**10. Triggers — What Pushed Them to Act**
- The events, moments, or experiences that turned them from passive to active.
- These are hook starters. The trigger is often the opening scene of the ad.

**11. Matched Value Props**
- From Step 6: the specific offer elements that solve this persona's problems.
- Framed in their language, not marketing language.

**12. Matched Proof Assets**
- From Step 6: the specific testimonials, case studies, and data points that will be most credible to this persona.
- Note WHY each proof asset matches (demographic similarity, same starting problem, same language).

**13. Mechanism Frame**
- From Step 6: how the unique mechanism should be explained to THIS persona.

**14. Winning Hooks and Angles**
- 5-8 hook concepts and angles derived from the persona's pains, triggers, desires, and customer language.
- Each hook must specify the awareness level it targets.
- Each hook must name its hook type from the Hook Formulas reference file (`references/hook-formulas.md`). Use the selection matrix to match hook types to awareness levels.
- Each hook must contain a traffic qualifier — a niche-specific term, price point, role, or life-situation detail that ensures only the ICP would engage.
- Each hook must be grounded in a specific data point from the research. Include the source reference.
- **HOOK DIVERSIFICATION RULE (MANDATORY):** Hooks must diversify across psychological levers. At minimum, the set must include:
  - At least 1 hook that agitates a **core fear**
  - At least 1 hook that appeals to a **core desire**
  - At least 1 hook that leverages a **cognitive bias** (see Section 17)
  - Tag each hook with its psychological lever (Fear / Desire / Bias) alongside the existing awareness level and hook type tags.
  - Testing 3 hooks that say the same thing in different words is a wasted test. Each hook must test a genuinely different psychological entry point.

**15. Watering Holes & Creative Consumption Profile**
- **Where they spend time:** Facebook groups, specific subreddits, YouTube channels, blogs, podcasts, TikTok niches?
- **How they consume content:** This is as important as where. Map:
  - **Pacing preference:** Do they engage with slow, long-setup content (typical of 60+ Facebook users) or fast, punchy, visually-driven content (younger cohorts)?
  - **Format affinity:** What do they engage with organically in their feeds? Text-overlay images, face-to-camera video, long-form stories, short Reels, community posts, educational content?
  - **Editing tolerance:** Do they respond to raw, low-fi, native-feeling content or polished, produced content? For most 50+ Facebook audiences, raw and native wins.
  - **Attention pattern:** Long setup before payoff (emotional seekers) or quick hook with immediate value (pragmatists)?
- This informs both creative tone and format assignment in the Strategy Map. The vehicle (format) must match how the persona naturally consumes content, or the hook won't land regardless of how good the copy is.

**16. Awareness-Segmented Verbatim Language Bank**
- All verbatim customer phrases extracted for this persona during Step 2 tagging, sorted into four buckets:
  - **Unaware** — phrases describing symptoms, daily frustrations, language used before they knew the problem had a name
  - **Problem-Aware** — phrases labelling the problem, describing failed attempts, expressing frustration with current approaches
  - **Solution-Aware** — phrases comparing solutions, expressing scepticism, asking for proof
  - **Product-Aware** — phrases with specific objections about this product, hesitations, late-stage concerns
- Number each phrase (e.g., UA-1, PA-1, SA-1, PrA-1) so the downstream scripting skill can cite them.
- If any bucket has fewer than 3 phrases, flag it with a recommendation for where to source more.

**17. Primary Cognitive Bias**
- Identify the dominant cognitive bias that determines which message this persona believes when they don't have time to think. Assign ONE primary bias and optionally one secondary bias from:
  1. **Social Proof** — "If others like me did this, it's safer." Responds to: authentic UGC, review/comment screenshots, soft CTAs with customer counts, study citations ("no wonder 100,000 women trust this"). Scatter social proof throughout the creative, not just at the CTA.
  2. **Risk/Loss Aversion** — "I want to avoid making the wrong choice more than I want upside." Responds to: guarantees, free trials, honest downside framing, educational content that helps them feel they've made a calculated decision. Needs more setup time and longer-funnel content.
  3. **Authority Bias** — "If an expert endorses this, it's credible." Responds to: expert VSLs, podcast ads with professionals, data points, studies, PR citations, founder face-to-brand content. The credential is a trust trigger.
  4. **Effort Minimalization** — "I want the least friction possible." Responds to: language like "takes 30 seconds", "doesn't impact your routine", visual demonstrations of simplicity, timeline-based content ("here's what happened in 30 days").
  5. **Novelty / Pattern Interruption** — "This is different. Pay attention." Responds to: unexpected hooks, controversy, visual interrupts in the hook, whiteboard concepts, format-breaking creative. Works better with younger audiences and skeptics.
  6. **Identity Reinforcement** — "This aligns with who I am or want to be." Responds to: value-led messaging, community framing ("join 40,000 women who..."), mission-aligned positioning. These people don't have goals — they have purpose. Speak to that purpose. Breaks when you try to appeal to everyone.
- Source the bias assignment from: how the persona talks about their decision-making process in transcripts/surveys, what type of proof they reference, what objections they raise (skepticism patterns reveal bias patterns).
- The bias directly informs format selection (Step 9C) and hook design (Step 9B).

**18. Veilance Zone Mapping**
- Identify where this persona's most effective messaging lives across four emotional zones:
  - **Zone 1 — Calm / Supportive:** Educational, warm, nurturing tone. "You're not alone in this. Here's what we found works."
  - **Zone 2 — Optimistic / Aspirational:** Solution-forward, dream-state focused. "Imagine waking up with energy again."
  - **Zone 3 — Urgent / Confrontational:** Challenging, direct, myth-busting. "Everything you've been told about weight loss after 50 is wrong."
  - **Zone 4 — Panic / Anxiety / Loss:** Fear-driven, worst-case, loss-focused. "Your doctor just told you your A1C is pre-diabetic. What now?"
- Assign a primary veilance zone for this persona (where most initial creative should live) and note which zones to test for diversification.
- CRITICAL: Most ad accounts over-index on Zone 4. If every persona's primary zone is Zone 4, flag it and recommend zone diversification. Speaking to the same emotion in every ad, even across different personas, kills incremental reach.

**19. Self-Concept Anchor**
- Identify the most effective self-concept framing for this persona's ads:
  - **Actual Self** — First-person, present-tense pain. "I can't even look at myself in the mirror anymore." The ad sits in the problem state.
  - **Ideal Self** — First-person, future-state aspiration. "I forgot to put makeup on most mornings now because I actually like how I look." The ad moves from problem to dream.
  - **Ought Self** — Third-person perspective. Someone else is talking about the persona or buying the product for them. "My wife was at her wit's end. I bought her this and everything changed." Creates a different emotional entry point and a genuinely distinct Entity ID.
- Most ads default to Actual Self → Ideal Self transitions. Deliberately building some concepts in Ought Self framing creates a new audience entry point that Meta's algorithm treats as a distinct creative signal.
- Note the recommended self-concept anchor for this persona and flag if it creates an opportunity for an Ought Self variation (e.g., does this persona have a spouse, children, or caregiver who would be the "ought self" narrator?).
</instructions>

---

### Step 8: Human Checkpoint — Profile Approval

Present the completed persona profiles to the user.

<instructions>
Tell the user: "Here are the full profiles for your 5 selected personas. Review each one carefully. For each profile, I need you to confirm:
1. Does this feel like a REAL person you have encountered in the data, or does it feel manufactured?
2. Are the insights specific enough that they could only apply to this persona?
3. Is anything missing that you know from experience but I could not extract from the data?
4. Are the matched value props and proof assets correct?

If any profile needs revision, tell me what is wrong and I will fix it before building the strategy map."

WAIT for approval. Do not proceed until all 5 profiles are confirmed.
</instructions>

---

### Step 8B: Micro Persona Decomposition

For each of the 5 approved macro personas, decompose into 2-4 micro personas. This is where the real targeting precision lives. Two people who look identical on paper (same age, same problem) can have completely different fears, motivators, and biases. Speaking to one means missing the other. Micro personas fix that.

<instructions>
For each macro persona, create 2-4 micro personas by varying across these dimensions:

1. **Core Fear** — What is the deepest threat if they don't solve this problem? Two women in the same macro persona can have completely different fears. One fears dying early and leaving her grandkids. Another fears the shame of being the "fat one" at family gatherings. Same problem, different psychological entry points.

2. **Core Motivator** — What actually drives the purchase decision? Connection with family? Social status? Self-respect? Control over their health? Independence from doctors? Each motivator produces a different hook, a different curiosity loop, a different CTA.

3. **Awareness Level (TEEP Position)** — Where does this micro persona sit on the behavioral journey?
   - **T (Trigger)** = Problem-Aware: Experiencing the trigger to purchase but doesn't know where to begin. Needs education and empathy.
   - **E (Exploration)** = Solution-Aware: Knows solutions exist, has experienced bad alternatives. Needs differentiation and trust.
   - **E (Evaluation)** = Product-Aware: Evaluating whether THIS specific product is right. Needs evidence and objection handling.
   - **P (Purchase)** = Most Aware: Ready to buy. Needs a clear, direct CTA and urgency.

4. **Primary Cognitive Bias** — Which of the 6 biases (from Section 17) dominates this micro persona's decision-making?

**Coding Convention:**
Each micro persona gets a code: `P[macro].[micro]`
- P1 = Macro Persona 1 (e.g., "GLP-1 Considerers")
- P1.1 = Micro: GLP-1 Considerers — Fear of Side Effects, Risk/Loss Aversion Bias, Evaluation Stage
- P1.2 = Micro: GLP-1 Considerers — Can't Afford Injectables, Effort Minimalization Bias, Trigger Stage
- P1.3 = Micro: GLP-1 Considerers — Philosophically Anti-Drug, Identity Reinforcement Bias, Exploration Stage

**For each micro persona, document:**
- Persona code (P1.1, P1.2, etc.)
- One-sentence description
- Core fear (with verbatim quote from data if available)
- Core motivator (with verbatim quote from data if available)
- TEEP position (T/E/E/P)
- Primary cognitive bias
- Primary veilance zone
- Self-concept anchor (Actual / Ideal / Ought)
- 2-3 hook concepts specific to this micro persona

**Rules:**
- Each micro persona within a macro must have a DIFFERENT primary fear OR a different primary motivator. If two micro personas share the same fear AND the same motivator, they are not distinct. Merge them.
- The micro personas within one macro should cover at least 2 different TEEP positions and at least 2 different cognitive biases. This is what creates psychological diversity.
- 2 micro personas per macro is the minimum. 4 is the maximum. More than 4 means the macro persona is too broad and should have been split earlier.

**Present to user in a table:**

| Code | Name | Core Fear | Core Motivator | TEEP | Bias | Veilance | Self-Concept |
|------|------|-----------|---------------|------|------|----------|-------------|

Then provide the detailed micro persona cards. WAIT for the user to approve before building the Strategy Map.
</instructions>

---

### Step 9: Build the Creative Strategy Map

For each of the 5 approved macro personas AND their micro personas, build a complete creative strategy map that specifies exactly what ads need to be created. The strategy map now builds at the MICRO persona level — each concept targets a specific P[X].[Y] code, not just the macro persona.

<instructions>
The strategy map is structured as follows. Build it for EACH persona.

**9A: Angle Generation**

For each persona, generate 3-5 genuinely distinct creative angles.

An angle is NOT a rephrased version of the same message. Each angle must communicate a fundamentally different belief, pain, desire, or emotional trigger. If two angles would get the same Entity ID from Andromeda (i.e., a stranger would look at both ads and say they are about the same thing), they are not distinct angles. Merge or replace.

For each angle, specify:
- The angle name and one-sentence description
- Which persona pain, desire, or trigger it is rooted in (with source reference)
- Why this angle is distinct from the other angles for this persona

**9B: Awareness Level Mapping**

For each angle, write a hook example for each relevant awareness level. See `references/creative-strategy-reference.md` for the full awareness level framework with hook styles, and `references/hook-formulas.md` for the named hook type library.

Not every angle needs hooks for all 5 levels. Map what is appropriate.

For each hook in the strategy map:
- Name the hook type from the Hook Formulas reference (e.g., "Catalyst Hook", "Relatable Moment Hook")
- Use the selection matrix in Hook Formulas to match types to awareness levels
- Include a traffic qualifier in every hook
- **Tag the psychological lever:** Fear / Desire / Bias (which of the three is this hook pulling?)
- **Tag the veilance zone:** Zone 1 (calm) / Zone 2 (optimistic) / Zone 3 (urgent) / Zone 4 (panic)
- **Tag the self-concept anchor:** Actual Self / Ideal Self / Ought Self
- **Tag the micro persona code:** P[X].[Y]

CRITICAL: Hooks must be written in the customer's language, not marketing language. They must sound like something the persona would say or think. Use exact phrases from the awareness-segmented verbatim language bank (Section 16 of the persona profile).

**9C: Format Assignment**

For each angle/awareness combination, assign the optimal creative format using this decision logic:
1. Reference the client's previous winning ads and formats first. Default to proven formats.
2. Reference competitor research. What formats are competitors using at scale?
3. Reference the Ad Formats Library (`references/ad-formats-library.md`) for format specs (scene count, word count, pacing, editing style) and the format selection guide that maps formats to body structure tools.
4. If no performance data exists (new client), use awareness-based defaults: Unaware/Problem-Aware = educational, low-threat formats (UGC, text-on-screen, infographics). Solution-Aware = authority formats (talking-head, case study carousels). Product-Aware = proof formats (testimonials, before/after). Most Aware = transactional (static offer, direct CTA).
5. **Cross-reference with cognitive bias:** Format must align with the micro persona's primary bias:
   - Social Proof bias → UGC testimonials, review screenshots, comment-reply videos, carousel testimonials
   - Risk/Loss Aversion bias → educational VSLs, longer-form content with setup time, honest comparison content
   - Authority bias → expert talking-head, podcast ads, data-driven static, founder-story content
   - Effort Minimalization bias → quick demos, timeline content ("30 days of..."), show-don't-tell formats
   - Novelty/Pattern Interruption bias → format-breaking creative, whiteboard concepts, visual hooks, controversy-led
   - Identity Reinforcement bias → community-framed, value-led, mission-aligned content
6. **Cross-reference with creative consumption profile (Section 15):** The format must match how this persona naturally consumes content. A 3-minute slow-paced face-to-camera ad works for women 60+ on Facebook. The same format will fail for a younger cohort on Instagram Reels. The vehicle must match the audience.

Check the completed map for format diversity. If every cell is the same format, the strategy has a visual diversity problem. Flag it.

**9D: Actor/Archetype Assignment**

For each persona, assign actor archetype(s) that represent them and add credibility. See `references/creative-strategy-reference.md` for full archetype guidance.

Key rules: The archetype must be immediately recognizable and stereotypical (clearer archetype = more coherent Entity ID). Must match the persona, not the brand owner. Different actors on the same script = different Entity IDs, so note opportunities for actor-based diversity. For smaller clients, this will usually be the founder. Note this but still specify the ideal archetype.
</instructions>

---

### Step 10: Scripting Readiness Validation Gate

Before compiling the final output, run this validation gate. The brief is not ready for the downstream Ad Script & Storyboard Generator unless ALL of these pass. If any fail, flag them in the Executive Summary and note the brief as "Incomplete — not ready for scripting" until resolved.

<instructions>
**Gate 1: Verbatim Language Volume**
Does each of the 5 selected personas have at least 8-10 verbatim customer phrases extracted from the research? Not paraphrased summaries. Actual quotes in the customer's exact words.
- If any persona has fewer than 8 verbatim phrases: FLAG. "Persona [X] has only [N] verbatim phrases. The scripting skill requires 8-10 minimum per persona. Source additional language from: [specific recommendation based on what's thin]."

**Gate 2: Verbatim Language Awareness Segmentation**
Is the customer language bank for each persona segmented by awareness level (Unaware / Problem-Aware / Solution-Aware / Product-Aware)?
- If the language is a flat, unsegmented pile: FLAG. "Customer language for [persona] is not segmented by awareness level. The scripting skill requires segmentation to write awareness-appropriate copy. Segment the phrases or request the scripting team do a best-effort inference (lower confidence)."

**Gate 3: Unaware Language Depth**
Does each persona have at least 3-4 verbatim phrases in the Unaware bucket? (This is the hardest to source and the most commonly thin.)
- If any persona has fewer than 3 Unaware phrases: FLAG. "Unaware language for [persona] is thin ([N] phrases). Cold-traffic scripts will be weaker as a result. Recommend sourcing Unaware language from: social media comments, niche forums, Reddit threads, YouTube comments, Amazon reviews of competing products."

**Gate 4: Pain List with Source References**
Does each persona have a ranked pain list where every pain includes a direct quote from the data as evidence?
- If any pain is stated without a source reference: FLAG. "Pain [X] for persona [Y] has no source reference. The scripting skill uses these to verify data grounding."

**Gate 5: Winning Ads in Text Form**
Are winning ads included as full extracted text scripts (not links)?
- If winning ads are provided as links only: FLAG. "Winning ads are provided as links, not extracted text. The scripting skill cannot ingest links. Extract the full script copy into text form before handing off."
- If new client with no winning ads: Acceptable. Note it.

**Gate 6: Awareness Volume Distribution**
Does the strategy map's concept mix roughly follow the 80/10/10 benchmark? (80% Unaware + Problem-Aware, 10% Solution-Aware, 10% Product-Aware + Most Aware.)
- If Product-Aware + Most Aware concepts exceed 30% of total: FLAG. "Strategy is bottom-heavy. Meta will serve these to the same small warm pool. Frequency will spike. Shift volume to Unaware and Problem-Aware concepts to enable scaling."
- If Unaware + Problem-Aware combined is under 40%: FLAG. "Cold traffic creative is thin. This limits scale potential. Add more top-of-funnel concepts."
- Exact percentages will flex by account — this is a sanity check, not a hard rule.

Present the gate results:

```
SCRIPTING READINESS GATE

Gate 1 — Verbatim Volume:     [PASS / FLAG — details]
Gate 2 — Awareness Segmentation: [PASS / FLAG — details]
Gate 3 — Unaware Language Depth: [PASS / FLAG — details]
Gate 4 — Pain List Sources:    [PASS / FLAG — details]
Gate 5 — Winning Ads Format:   [PASS / FLAG — details]
Gate 6 — Awareness Volume Mix:  [PASS / FLAG — details]

Brief Status: [READY FOR SCRIPTING / INCOMPLETE — resolve flags before scripting]
```

If all gates pass, proceed to compile. If any gate fails, include the gate results in the Executive Summary so the team knows what needs to be resolved before the brief goes to the scripting skill.
</instructions>

---

### Step 11: Compile Final Output

Assemble the complete Creative Strategy Brief as a single cohesive document.

<instructions>
The final document structure:

**Section 1: Executive Summary**
- Client name and offer
- Date and brief version
- Number of personas, total angles, total concepts
- Key strategic insight (one paragraph on the biggest opportunity or risk)
- Data confidence notes (flag any gaps from missing soft inputs or homogeneous data)
- Scripting Readiness Gate results (from Step 10)

**Section 2: Persona Scorecards**
- The ranked table from Step 5 with all 8-15 personas and their scores
- The 5 selected personas highlighted
- Thesis validation summary (confirmed/partially confirmed/contradicted)
- Any client-directed hypotheses flagged

**Section 3: Detailed Persona Profiles**
- Full profiles for all 5 selected personas (from Step 7)
- Each profile is its own section/page
- Each profile must include an **Awareness-Segmented Verbatim Language Bank** appendix: all extracted verbatim phrases for that persona, sorted into Unaware / Problem-Aware / Solution-Aware / Product-Aware buckets with phrase numbers for downstream citation

**Section 4: Creative Strategy Map**
- For each persona: angles, awareness-level hooks, format assignments, actor archetypes
- Summary grid showing the full map across all 5 personas for quick reference

**Section 5: Entity & Psychological Diversity Check**
- Review the complete strategy map and assess: if all of these ads were launched, how many genuinely distinct Entity IDs would Andromeda assign?
- Flag any areas where ads would likely receive the same Entity ID
- Flag any awareness levels that are over-represented or under-represented
- Flag any format types that are over-represented
- **Veilance Zone Diversity:** Count how many concepts live in each zone (1-4). If >60% of creative sits in one zone (usually Zone 4 — fear/panic), flag it. Recommend concepts in underrepresented zones. This is how you drive incremental reach — diversifying the emotional state, not just the message.
- **Cognitive Bias Diversity:** Count how many concepts leverage each of the 6 biases. If >50% rely on one bias, flag it. Different biases reach different psychological profiles within the same demographic.
- **Self-Concept Diversity:** Count Actual Self vs Ideal Self vs Ought Self concepts. If Ought Self = 0, flag it as a missed opportunity for a genuinely distinct creative signal.
- **Micro Persona Coverage:** Check which micro persona codes (P[X].[Y]) have creative assigned and which don't. Flag any micro persona with zero concepts — that's a gap in strategic coverage.
- **Awareness Volume Distribution:** Count concepts by awareness level. Benchmark: ~80% of creative volume should target Unaware + Problem-Aware, ~10% Solution-Aware, ~10% Product-Aware + Most Aware. If the map is bottom-heavy (majority Product-Aware/Most Aware), flag it: "This strategy will hit a frequency wall. Meta's Andromeda serves Product-Aware ads to a small warm pool. To scale, shift volume toward Unaware and Problem-Aware." If the map is top-heavy with zero Product-Aware/Most Aware, flag it: "No retargeting creative. Add 1-2 proof-stack concepts for warm audiences."
- **Strategic Coverage Score:** Total unique micro personas targeted × unique veilance zones used × unique biases leveraged. This is the measure of psychological landscape coverage. Volume of concepts matters less than diversity of psychological entry points.

**Section 6: Hypotheses for Testing**
- List each micro persona/angle/format combination as a testable hypothesis
- Format: "We believe [Micro Persona Code + Name] will convert on [Angle] delivered via [Format] at [Awareness Level], leveraging [Bias] in [Veilance Zone], framed as [Self-Concept Anchor], because [data-grounded reason]."
- These hypotheses are what get handed to the media buyer so they understand what is being tested and how to evaluate results.
- The micro persona code (P[X].[Y]) must be included in every hypothesis so it can be mapped to ad account naming conventions for gap analysis and performance tracking.

Frame EVERYTHING in this document as hypothesis. This is the initial creative brief. The ad account will tell us what is right and what is wrong.
</instructions>

---

## Quality Standards

The output passes if ALL of the following are true:

1. **Specificity Test**: Could you swap the persona name and the insight still makes sense? If yes for ANY item, it fails. Redo until specific to one persona only.
2. **Data Grounding Test**: Every claim must trace to source data. Ungrounded insights must be flagged explicitly as assumptions.
3. **Customer Language Test**: Hooks and descriptions must use the customer's actual words from transcripts. If it reads like a marketer wrote it, it fails.
4. **Diversity Test**: The strategy map must produce genuinely distinct Entity IDs. If a stranger would say two concepts are "about the same thing", it fails.
5. **Hypothesis Framing Test**: Every output framed as testable hypothesis. "We believe X will convert on Y because [evidence]", never "X converts on Y."
6. **Completeness Test**: All 19 persona profile sections filled. All micro personas documented. All strategy map cells populated. No "TBD." If data is insufficient, state what's missing and provide best hypothesis, clearly flagged.
7. **Psychological Diversity Test**: The strategy map must cover at least 3 of 4 veilance zones, at least 3 of 6 cognitive biases, and include at least 1 Ought Self concept. If the map is psychologically homogeneous, it fails regardless of Entity ID diversity.
8. **Hook Lever Test**: Every persona's hook set must include at least 1 fear-led, 1 desire-led, and 1 bias-led hook. Three hooks that say the same thing differently = failed test. Each hook must pull a different psychological lever.

---

## Known Failure Modes and How To Handle Them

| Failure Mode | What It Looks Like | How To Handle |
|---|---|---|
| **Homogeneous Input Data** | All transcripts from same funnel/customer type. Personas cluster into 2-3 similar profiles. | Flag it. Cross-reference competitor research, customer base data, and offer briefing to generate additional persona hypotheses. Present separately: "These came from transcripts. These are additional opportunities from competitive/market analysis." User makes final call. |
| **Client Overrides Data** | User selects a persona the data doesn't support, or insists a market matters despite low scoring. | Accept it. Build it out fully. Flag as "client-directed hypothesis, limited data support" so the media buyer knows it's a higher-risk test. |
| **Competitive Convergence** | Every competitor running the same angles. No obvious gap. | Don't avoid crowded angles. Ask: "How do we do this better, in a different format, with a more specific persona drill-down, or with a differentiated mechanism?" Find the edge within the crowded space. |
| **Insufficient Offer Differentiation** | Mechanism sounds identical to competitors. No clear differentiator. | Flag it to user: "The mechanism is not differentiated from [competitors]. Solution-Aware and Product-Aware ads will be harder to convert." Ask if there's a unique element not yet articulated. Do not invent differentiation that doesn't exist. |
| **Persona Overlap** | Proto-personas blur together. "Frustrated Dieter" and "Yo-Yo Dieter" are the same person. | Merge them. Hard rule: distinct primary pain + distinct desired outcome. If both are shared, it's one persona. |
| **Missing Proof for High-Priority Persona** | Persona scores highly but client has zero matching proof assets. | Note it in the profile: "No direct proof assets for this persona. Higher proof burden in creative. Recommend collecting a testimonial from this customer type ASAP." Never fabricate proof. |

---

## Constraints

1. **Never produce generic, interchangeable insights.** Every output must be persona-specific. This is the single most important constraint.
2. **Never treat data as fact.** Everything is hypothesis. Frame accordingly.
3. **Never proceed without all five hard-gate inputs.** Exception: winning ads for brand-new clients only.
4. **Never fabricate customer language.** If a phrase isn't from the research data, flag it as a hypothesized insight.
5. **Never fabricate proof.** If a testimonial or case study doesn't exist, say so.
6. **Never produce hooks that sound like marketing copy.** Test: would this person say this to their friend? If not, rewrite.
7. **Never ignore Andromeda diversity.** The strategy map must produce genuinely different Entity IDs across all four variables.
8. **Never skip the human checkpoints.** Three mandatory pauses (persona selection, profile approval, and micro persona approval). Wait for explicit confirmation at each.
9. **No AI-isms in any copy output.** No "That's not X, it's Y." No em dashes. No "here's the truth" or "because of X, Y" patterns.
10. **Flag every assumption.** Never dress up speculation as a finding.
11. **Never let volume substitute for strategic coverage.** More concepts that speak to the same persona in the same emotional state = waste. Fewer concepts that each target a different micro persona, bias, and veilance zone = incremental reach. Measure psychological landscapes mapped, not output count.
12. **Every hook must test something different.** If two hooks in the same persona's set tap the same fear, same desire, or same bias, one of them is redundant. Replace it with a hook that tests a different psychological lever.

---

## Output Format

The final deliverable is a single comprehensive document with the following structure:

```
CREATIVE STRATEGY BRIEF
[Client Name] | [Date] | Version [X]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. EXECUTIVE SUMMARY
   - Strategic overview
   - Data confidence notes
   - Key opportunity/risk
   - Scripting Readiness Gate results

2. PERSONA SCORECARDS
   - Full 8-15 persona ranking table
   - Selected top 5 highlighted
   - User thesis validation

3. MACRO PERSONA PROFILES (one per persona)
   3.1 [P1 — Persona 1 Name]
       - All 19 profile sections (including Cognitive Bias, Veilance Zone, Self-Concept Anchor)
   3.2 [P2 — Persona 2 Name]
       - All 19 profile sections
   [... through P5]

4. MICRO PERSONA CARDS
   4.1 [P1.1 — Micro Name] through [P1.3]
   4.2 [P2.1 — Micro Name] through [P2.3]
   [... through P5.X]
   4.6 Micro Persona Summary Table (all codes, fears, motivators, TEEP, bias, veilance, self-concept)

5. CREATIVE STRATEGY MAP (built at micro persona level)
   5.1 [P1] Strategy Map (all micro personas)
       - Angles, awareness hooks, formats, actors
       - Each hook tagged: Persona Code | Awareness | Hook Type | Psych Lever | Veilance Zone | Self-Concept | Bias
   5.2 [P2] Strategy Map
   [... through P5]
   5.6 Summary Grid (all micro personas, all angles, quick reference)

6. ENTITY & PSYCHOLOGICAL DIVERSITY CHECK
   - Projected unique Entity IDs
   - Veilance zone distribution
   - Cognitive bias distribution
   - Self-concept anchor distribution
   - Micro persona coverage gaps
   - Strategic Coverage Score

7. TESTING HYPOTHESES
   - Each concept as a testable hypothesis (with micro persona code)
   - Handoff notes for media buyer
   - Ad account naming convention guide (incorporating P[X].[Y] codes)
```

This document is the handoff to the ad scripting/concept creation process. It does NOT contain finished ad scripts. It contains the strategic foundation that makes the scripts possible.

---

## Reference Material

**Strategy Reference:** `references/creative-strategy-reference.md` — Consult for:
- The Four Variables That Create Entity Diversity (Andromeda framework, Entity ID tiers)
- Awareness Levels (Eugene Schwartz framework with definitions, hook styles, and examples)
- The Nine Tagging Dimensions (full definitions and scoring guidance)
- Persona Scoring Framework (Cold Traffic Convertibility and Market Scalability formulas with sub-factor scales)

Reference this file during Steps 2, 4, 9, and the Entity Diversity Check.

**Hook Formulas:** `references/hook-formulas.md` — Consult for:
- 10 named hook types with definitions, examples, and when-to-use guidance
- Selection matrix mapping hook types to awareness levels
- Traffic qualification requirements

Reference this file during Step 7 (Section 14) and Step 9B (Awareness Level Mapping).

**Ad Formats Library:** `references/ad-formats-library.md` — Consult for:
- Per-format specs: scene count, word count, pacing, recording setup, editing style
- Format selection guide mapping formats to body structure tools

Reference this file during Step 9C (Format Assignment).
