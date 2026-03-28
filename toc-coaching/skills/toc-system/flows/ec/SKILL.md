---
name: toc-ec
description: >
  Evaporating Cloud (EC) coaching flow — guides users through conflict resolution
  by surfacing and challenging hidden assumptions. Use when the user faces a dilemma
  where two needs appear incompatible, or when a CRT has revealed a core conflict
  maintaining the root cause. This is the "What to change to?" tool.
preconditions:
  - User can articulate a conflict or dilemma (two needs that seem incompatible)
  - Phase 2 requires a validated five-box cloud (Objective, Need A, Need B, Want A, Want B)
  - Phase 3 requires at least 3 assumptions surfaced per arrow on B→D and C→D'
---

# Evaporating Cloud (EC) Flow

The Evaporating Cloud (also called the Conflict Resolution Diagram) answers: **"What to change to?"** by exposing the hidden assumptions that make a conflict seem irresolvable, then finding an injection that invalidates one of those assumptions — dissolving the conflict rather than compromising.

Before starting, read:
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-logic-rules.md` — the EC uses necessity logic, not sufficiency logic
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/diagramming.md` — diagram templates and the generation script
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/question-bank.md` — consult the EC section
- If arriving from a CRT: read the handoff state from `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/handoff-protocol.md`

## The EC Structure

Every Evaporating Cloud has exactly five elements:

```
     ┌── [B: Need A] ──── [D: Want/Prerequisite A]
     │                              │
[A: Objective]                   CONFLICT
     │                              │
     └── [C: Need B] ──── [D': Want/Prerequisite B]
```

- **A (Objective):** The common goal that both sides of the conflict are trying to achieve
- **B (Need A):** A necessary condition for achieving the Objective
- **C (Need B):** Another necessary condition for achieving the Objective
- **D (Want A):** What we think we must do or have in order to satisfy Need A
- **D' (Want B):** What we think we must do or have in order to satisfy Need B
- **Conflict:** D and D' appear to be mutually exclusive — you can't have both

The arrows use **necessity logic**: "In order to have A, we must have B." Each arrow has hidden assumptions behind it explaining WHY the necessity relationship holds.

The cloud "evaporates" when you find that one of those assumptions is invalid — meaning the perceived necessity doesn't actually hold, and the conflict dissolves.

## What Makes a Good EC

A good EC:
- Has a genuine Objective that both parties care about (not a fake compromise goal)
- States Needs, not solutions — "maintain customer trust" not "keep our current SLA"
- Identifies the real conflict at the Want/Prerequisite level, not at the Need level (Needs rarely actually conflict)
- Surfaces 3-5 assumptions per arrow (especially the B→D, C→D', and D↔D' arrows)
- Produces an injection that invalidates a real assumption — not a compromise, not wishful thinking
- Results in both Needs being fully satisfied (win-win, not trade-off)

A bad EC:
- States the conflict as "we need more resources" (that's not a conflict, that's a wish)
- Has vague Needs that are really restated Wants
- Produces a "compromise" injection that partially sacrifices one Need
- Doesn't actually surface the assumptions — just jumps to a solution
- Has an Objective so abstract it doesn't constrain anything ("succeed")

## Phase 1: Identifying the Conflict

### If arriving from a CRT:
The handoff state should contain a root cause and a preliminary conflict framing. Start by validating that framing:
- "The CRT suggested the core conflict is between [Need A] and [Need B]. Does that feel right?"
- "Let me make sure I understand both sides. Walk me through why [Need A] matters."
- "And why does [Need B] matter?"
- "What's the common goal — the thing you're ultimately trying to achieve that requires both?"

### If starting fresh:
Help the user articulate the conflict:
1. "What are the two things you feel pulled between?"
2. Separate the wants from the needs. Users almost always start by stating wants (actions, solutions, positions). Push to underlying needs:
   - "You said you need to [Want]. But WHY do you need to do that? What underlying need does it serve?"
   - "If there were a completely different way to satisfy that need, would you care about [Want] specifically?"
3. Find the Objective:
   - "What's the bigger thing that both of these needs are trying to achieve?"
   - "If you could fully satisfy both needs, what would be the outcome?"

### Common Mistakes to Catch

- **Stating the conflict at the Need level.** If B and C seem to genuinely conflict, one of them is probably a disguised Want. Needs are usually both legitimate — the conflict lives in HOW we think we must satisfy them.
- **"We don't have enough money/time/people."** This is not a conflict — it's a resource wish. Push deeper: what are the two competing demands ON those resources? That's where the conflict lives.
- **One-sided framing.** The user often feels one side is "right" and the other is "wrong." The EC requires treating both sides as legitimate. Ask: "Why would a reasonable person believe [the side you disagree with]?"
- **Objective too vague.** "Be successful" or "grow the business" — push for specificity tied to the actual situation: "Grow the SaaS business profitably while retaining existing customers."

### Checkpoint 1

Present the five-box cloud in text form:
```
     ┌── B: [Need A] ────── D: [Want A]
     │                            │
A: [Objective]                 CONFLICT
     │                            │
     └── C: [Need B] ────── D': [Want B]
```

Read each arrow using necessity logic:
- "In order to [A], we must [B]."
- "In order to [B], we must [D]."
- "In order to [A], we must [C]."
- "In order to [C], we must [D']."
- "But [D] and [D'] conflict because..."

Ask: "Does this accurately capture your situation? Does each 'must' feel real?"

---

## Phase 2: Surfacing Assumptions

This is where the real work happens. Every arrow in the cloud is held up by hidden assumptions. The injection will come from invalidating one of these assumptions.

### Process

For each of the five arrows (A→B, A→C, B→D, C→D', D↔D'), ask:

1. "Why must this be true? What assumption makes this connection hold?"
2. "Is there another assumption behind that one?"
3. "Under what conditions might this assumption be false?"
4. "Is this assumption based on evidence, or is it inherited wisdom / 'how we've always done it'?"

### Arrow Priority

Not all arrows are equally productive for finding injections:

- **B→D and C→D' arrows** (Need→Want): These are the most fertile ground. The assumption here is usually "the only way to satisfy this need is through this specific action/condition." That's almost never actually true.
- **D↔D' conflict arrow**: The assumption here is that the two wants are truly incompatible. Sometimes they're not — or they're only incompatible under specific conditions that can be changed.
- **A→B and A→C arrows** (Objective→Need): These are usually the most solid and hardest to challenge, but occasionally a breakthrough comes from questioning whether a stated need is truly necessary for the objective.

### Recording Assumptions

For each arrow, build a numbered list of assumptions. Aim for 3-5 per arrow, especially for B→D, C→D', and D↔D'.

```
Arrow B→D: "In order to [Need A], we must [Want A]"
Assumptions:
  1. [Want A] is the only way to achieve [Need A]
  2. [Specific condition] that makes alternatives infeasible
  3. [Belief about customers/market/resources] that constrains options
  4. [Historical precedent] that may no longer apply
```

### Checkpoint 2

Present all assumptions organized by arrow. Then ask:
- "Which of these assumptions do you feel least confident about?"
- "Which ones are based on real evidence vs. inherited beliefs?"
- "If you could magically make one of these assumptions false, which one would change the game?"

---

## Phase 3: Finding the Injection

### Goal
Identify one or more assumptions that can be invalidated, and construct an injection — a new idea, action, or condition — that makes the assumption false, thereby dissolving the conflict.

### Process

1. **Start with the weakest assumption** (the one the user identified as most questionable).

2. **Ask:** "If this assumption were false — if [assumption] didn't hold — what would be possible?"

3. **Let the user generate the injection first.** Don't suggest solutions. Ask:
   - "What new idea, action, or condition would make this assumption no longer true?"
   - "Is there something you could DO that would change the conditions so this assumption doesn't apply?"
   - "What would someone who doesn't share this assumption do in your situation?"

4. **If the user is stuck,** try:
   - "What if we changed the time scale? Does this assumption hold if we think about it over [shorter/longer] time?"
   - "What if we changed who does it? Does this assumption hold if a different person/team/partner were involved?"
   - "What would your most creative competitor do here?"

5. **Validate the injection:**
   - "If we implemented [injection], would [Need A] still be satisfied?"
   - "Would [Need B] still be satisfied?"
   - "Is this truly a win-win, or is one side giving something up?"
   - "Is this injection actionable — something you could actually do — or is it wishful thinking?"

### Injection Quality Test

A good injection:
- Makes a specific assumption false (you can point to which one)
- Allows BOTH needs to be fully satisfied — it's not a compromise
- Is actionable and concrete — not "have better communication" but "implement a weekly cross-functional review where engineering presents the constraint impact of each feature request"
- Doesn't create obvious new conflicts (though this is what the FRT is for)
- Feels like a genuine insight — users often say "why didn't I see that before?"

A bad injection:
- Is just "get more resources" in disguise
- Sacrifices one need for the other (that's compromise, not resolution)
- Is vague and hand-wavy
- Only works if other people change their behavior without any structural reason to do so
- Is something the user already tried and it didn't work

### Checkpoint 3 (Final)

Present the complete EC with:
1. The five-box cloud diagram
2. All assumptions mapped to each arrow
3. The invalidated assumption highlighted
4. The injection and how it dissolves the conflict

Ask:
- "Does this feel like a genuine breakthrough, or does it feel forced?"
- "Who needs to be convinced of this for it to work?"
- "What's your biggest worry about this injection?"

### Transition Decision

After the EC is validated:
- If the injection needs forward validation → recommend **Future Reality Tree** to check for unintended consequences (prepare handoff per `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/handoff-protocol.md`)
- If the injection is straightforward and the user wants to implement → recommend **PRT/TT**
- If the user is uncertain about the injection → revisit assumptions or try invalidating a different assumption
