---
name: toc-frt
description: >
  Future Reality Tree (FRT) coaching flow — validates proposed solutions (injections)
  by tracing their effects forward using sufficiency logic, and systematically
  hunting for Negative Branches (new problems created by the solution). Use when the
  user has a proposed change and wants to check "Will this work? What could go wrong?"
preconditions:
  - User has a proposed solution or injection to validate
  - Ideally has a UDE list to verify the injection resolves them
  - Negative Branch hunting requires at least 3 positive effects traced first
---

# Future Reality Tree (FRT) Flow

The FRT answers: **"Will this change actually produce the results we want, and what new problems might it create?"** It takes an injection (from an EC or any proposed solution) and traces its effects forward through sufficiency logic to verify it resolves the UDEs and to hunt for Negative Branches.

Before starting, read:
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-logic-rules.md` — sufficiency logic and CLR apply in full
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/diagramming.md` — diagram templates and the generation script
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/question-bank.md` — consult the FRT section
- If arriving from an EC: read the handoff state from `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/handoff-protocol.md`

## The FRT's Two Jobs

1. **Positive validation:** Does the injection, when traced forward through causal logic, actually produce Desirable Effects that replace the original UDEs?
2. **Negative Branch identification:** Does the injection ALSO produce new Undesirable Effects — problems that don't exist today but will exist after the change?

Both are essential. Most people do Job 1 (confirmation bias — "see, it works!") and skip Job 2. The coach must push hard on Negative Branch hunting.

## Phase 1: Define the Starting State

### Inputs Required
1. **The injection(s):** What is being proposed? State it clearly and specifically.
2. **The UDE list:** What problems should this injection resolve? (from CRT if available)
3. **Current reality conditions:** What existing conditions will interact with the injection? These are the facts on the ground that don't change just because you implement the injection.

### If arriving from an EC:
The handoff state should contain the injection, the invalidated assumption, the EC structure, and the UDE list. Confirm all of these:
- "The injection we're validating is: [injection]. Is that still your proposal?"
- "And the UDEs we're trying to resolve are: [list]. Any changes?"

### If starting fresh:
Help the user define:
- "What change are you proposing?"
- "What problems do you expect it to solve?"
- "What does the current situation look like — what conditions exist today that will interact with this change?"

### Checkpoint 1
"We're going to trace the effects of [injection] forward and check two things: does it actually resolve your problems, and does it create any new ones. Before we start — what's your gut feeling? How confident are you this will work?"

---

## Phase 2: Positive Trace — Validating the Injection

### Process

Build the FRT forward from the injection using sufficiency logic:

1. **Start with the injection as the base entity.**
   "If [injection] is implemented, what's the first thing that changes?"

2. **For each new entity, apply sufficiency logic:**
   - "If [injection/new condition], then [expected effect]" — is this valid?
   - Does it need AND connectors? "Is the injection alone sufficient, or does it need an existing condition to also be present?"
   - Apply CLR to each connection: Clarity, Causality Existence, Cause Insufficiency, Alternative Cause

3. **Trace up to the Desirable Effects.**
   Each UDE from the original list should have a corresponding Desirable Effect (DE) in the FRT. The DE is often the direct opposite of the UDE:
   - UDE: "Customer churn rate is 7%" → DE: "Customer churn rate decreases to <3%"
   - UDE: "Sales cycle is 75 days" → DE: "Sales cycle returns to ~30 days"

4. **Check coverage:**
   - "Does this FRT reach each of our original UDEs?"
   - "Are there any UDEs that the injection doesn't address? If so, do we need additional injections?"

### The AND Connector Warning

Injections almost never work alone. They need supporting conditions. Be aggressive about asking:
- "What else has to be true for this injection to work?"
- "What existing conditions are you relying on?"
- "What if [assumed supporting condition] isn't actually present?"

Each assumed supporting condition becomes an AND connector in the FRT. If any of these are missing or fragile, the injection's effectiveness is at risk.

### Checkpoint 2
Present the positive trace of the FRT as a text-based tree. Walk through the logic:
"Starting from [injection], this leads to [first effect], which combined with [existing condition] produces [second effect]... ultimately reaching [Desirable Effect replacing UDE X]."

"Does this causal chain feel solid? Where are you least confident?"

---

## Phase 3: Negative Branch Reservation (NBR)

This is the most important phase of the FRT. Skip it and you're just doing confirmation bias with diagrams.

### What Is a Negative Branch?

A Negative Branch is a chain of cause-and-effect that starts from the injection (or one of its positive effects) and leads to a NEW Undesirable Effect — a problem that doesn't exist today but will exist after the change.

```
[Injection] → [Positive Effect] → [Desirable Effect]
                    │
                    └→ [Intermediate Effect] → [NEW UDE! ← Negative Branch]
```

### Hunting Process

For each entity in the positive FRT, systematically ask:

1. **"What else could this cause?"** — beyond the positive effect you want, what other effects might occur?
2. **"Who would be negatively affected by this change?"** — think about all stakeholders, not just the user
3. **"What's the worst-case scenario?"** — if this goes wrong, how does it go wrong?
4. **"What would a skeptic or opponent of this change predict?"** — they often see the negative branches the proponent is blind to
5. **"Does this injection create a NEW constraint somewhere?"** — solving one bottleneck often reveals or creates another
6. **"Could this injection make any of our OTHER UDEs worse?"** — even while fixing the target UDE

### Common Negative Branch Patterns

- **Capacity shift:** Fixing one constraint overloads the next step in the process
- **Cultural resistance:** The change requires behavior changes that people resist, leading to workarounds that undermine the injection
- **Customer impact:** Changes to internal processes have unintended effects on customer experience
- **Talent flight:** Changes that reduce autonomy or change roles cause valued people to leave
- **Measurement dysfunction:** New metrics or processes create gaming behavior
- **Timing mismatch:** The injection takes time to work, but the negative effects are immediate — creating a valley of despair where things get worse before they get better

### Checkpoint 3
For each identified Negative Branch:
- "Is this a real risk, or are we being overly paranoid?"
- "How serious would this new UDE be compared to the current ones?"
- "Is the Negative Branch worse than the current reality? Sometimes the cure's side effects are milder than the disease."

---

## Phase 4: Trimming Negative Branches

### Goal
For each real Negative Branch, find a way to prevent or mitigate it WITHOUT undermining the original injection.

### Process

For each Negative Branch:

1. **Identify where to intervene.** Look at the causal chain that leads to the new UDE. Where can you insert a secondary injection that blocks the negative effect?

2. **Generate a trimming injection:**
   - "What would prevent [intermediate effect] from leading to [negative UDE]?"
   - "Can we add a condition that blocks this branch while preserving the positive effects?"
   - "Is there a timing, sequencing, or communication change that would prevent this?"

3. **Validate the trim:**
   - "Does this trimming injection actually prevent the Negative Branch?"
   - "Does it undermine the original injection or any of its positive effects?"
   - "Does the trimming injection itself create NEW Negative Branches?" (recurse carefully — don't go more than one level deep unless necessary)

4. **Check feasibility:**
   - "Is this trimming injection realistic and achievable?"
   - "Does it require additional resources or changes beyond what was planned?"
   - "Does the combination of original injection + all trimming injections still make sense as a whole?"

### When You Can't Trim a Branch

If a Negative Branch can't be trimmed:
- Reassess whether the original injection is the right one — maybe a different assumption in the EC needs to be challenged
- Consider whether the Negative Branch is actually acceptable (less bad than current state)
- Consider whether the whole approach needs rethinking — this is a valid outcome. Not every injection works.

---

## Phase 5: Complete FRT Presentation

### Checkpoint 4 (Final)

Present the full FRT:

1. **The injection(s):** Primary + all trimming injections
2. **The positive causal chain:** Injection → intermediate effects → Desirable Effects
3. **All AND connectors:** Supporting conditions required
4. **Negative Branches identified:** Each one with its trimming injection
5. **UDE coverage scorecard:** Which original UDEs are resolved, which aren't
6. **Remaining risks:** Anything unresolved

### Final Questions
- "Overall, does this FRT give you confidence that the injection will work?"
- "Are there any Negative Branches we missed?"
- "What's the biggest remaining risk?"
- "Are you ready to plan implementation, or does the injection need revision?"

### Transition Decision
- If ready to implement → recommend **PRT/TT** for implementation planning
- If the injection needs revision → return to **EC** with new information
- If new UDEs were discovered → return to **CRT** to incorporate them
- If a new constraint was identified → consider **Five Focusing Steps**

Prepare handoff state per `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/handoff-protocol.md`.
