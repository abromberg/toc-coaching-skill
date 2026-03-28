---
name: toc-crt
description: >
  Current Reality Tree (CRT) coaching flow — guides users through root cause analysis
  using Goldratt's sufficiency logic. Use when the user has multiple symptoms or
  undesirable effects and needs to find the 1-2 root causes driving most of them.
  This is the "What to change?" tool.
preconditions:
  - User has described a problem or situation with observable symptoms
  - Phase 2 requires at least 3 UDEs surfaced and confirmed
  - Phase 3 requires at least 3-4 causal connections built and validated
---

# Current Reality Tree (CRT) Flow

The CRT is the diagnostic tool of the Thinking Processes. It answers: **"What to change?"** by tracing observable Undesirable Effects (UDEs) back to their root causes through chains of sufficiency logic.

Before starting, read:
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-logic-rules.md` — you will need the CLR rules throughout this flow
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/diagramming.md` — diagram templates and the generation script
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/question-bank.md` — consult the CRT section for Socratic prompts

## What Makes a Good CRT

A good CRT:
- Starts from 5-10 real, observable, specific UDEs
- Uses strict sufficiency logic: "If A, then B" means A alone is enough to produce B
- Achieves convergence: many UDEs trace back through different causal paths to 1-2 root causes
- Identifies root causes that are actionable — not "the economy is bad" but "our pricing policy assumes cost-plus in a market that has shifted to value-based"
- Passes CLR validation at every connection

A bad CRT:
- Lists vague complaints instead of specific UDEs
- Confuses correlation with causation
- Has many root causes (suggests the tree isn't deep enough — keep digging)
- Has causes that are actually effects stated in different words (tautology)
- Skips the AND connectors — most real causes need co-conditions

## Phase 1: Surfacing Undesirable Effects (UDEs)

### Goal
Collect 3-5 UDEs from the user to start — you can surface more as you build connections. Don't wait for a complete list before producing a diagram.

### Process

Start by asking the user to describe what's going wrong. Use questions from the question bank's CRT Phase 1 section. Your job in this phase is to:

1. **Collect raw complaints and frustrations.** Let the user vent. Don't organize yet.

2. **Refine each one into a proper UDE.** A proper UDE is:
   - Observable (a camera could record it, or it shows up in data)
   - Stated as a condition, not an action ("Customer complaints are increasing" not "Customers complain")
   - Not a cause or a solution in disguise
   - Not vague ("morale is low" → push for: "Three senior engineers have requested transfers in the past quarter")

3. **Challenge and sharpen.** For each candidate UDE, ask:
   - "Is that a fact you can point to, or is it your interpretation of a fact?"
   - "Would the people involved agree this is happening, or is this your perception?"
   - "Is this the UDE itself, or is it actually a cause of some deeper UDE?"
   - "Is this really undesirable — for whom? From whose perspective?"

4. **Don't over-collect.** Once you have 3-5 solid UDEs, move to diagramming and connection-building. More UDEs will surface naturally as you trace causes. Asking "what else?" five times before showing any work kills momentum.

### Checkpoint 1

Once you have 3-5 refined UDEs, generate a diagram showing them as labeled boxes and present them back:
- "Here's what I have. Does this list accurately capture the situation?"
- "Is anything missing? Anything that shouldn't be here?"
- "If you had to rank these by impact, which 3 are most painful?"

Generate an ASCII diagram showing the UDEs as labeled boxes — this is the first visual artifact. It gives the user something concrete to react to.

Get explicit confirmation before proceeding.

### Common Pitfalls in This Phase

- **Solution-stating**: "We need a new CRM system" is not a UDE. Ask: "What's the problem that makes you think you need a new CRM?"
- **Blame-stating**: "Marketing doesn't communicate with sales" — push past blame to effect: "What happens as a result? What observable bad thing occurs?"
- **Vagueness**: "Efficiency is low" — compared to what? Measured how? Push for specifics.
- **Cause-stating**: "We don't have enough capacity" might be a cause, not a UDE. The UDE is the effect: "We're missing 30% of delivery deadlines."

---

## Phase 2: Building Causal Connections

### Goal
Connect UDEs through cause-effect chains using sufficiency logic, working downward toward root causes.

### Process

1. **Start with the most impactful UDE.** Ask: "What do you think causes this?"

2. **For each proposed cause, apply the Sufficiency Logic Check:**
   - "If [cause], then [effect]" — does this read correctly?
   - "Is [cause] by itself sufficient to produce [effect]? Or does it need something else to be true at the same time?" (If yes → add an AND connector)
   - "If [cause] went away, would [effect] disappear?" (Tests causality existence)
   - "Could something else entirely produce [effect]?" (Tests for alternative causes)
   - "If [cause] is real, what ELSE should we see happening?" (Predicted effect existence — the most powerful validation)

3. **Apply CLR at every arrow.** Don't wait until the tree is "done." Challenge each connection as it's built. Reference `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-logic-rules.md` for the full CLR framework. Focus especially on:
   - **Clarity**: Is this statement precise?
   - **Causality Existence**: Is there a real mechanism, or just co-occurrence?
   - **Cause Insufficiency**: Does this need AND connectors?
   - **Cause-Effect Reversal**: Is the arrow pointing the right way?

4. **Look for connections between branches.** As you build downward from multiple UDEs, actively look for convergence: "This cause you identified for UDE #3 — could it also be contributing to UDE #7?"

5. **Use the Effect-Cause-Effect method.** This is Goldratt's core validation technique:
   - Start with an observed Effect (a UDE)
   - Hypothesize a Cause
   - Predict another Effect that should also exist if the Cause is real
   - Check: does that predicted Effect actually exist?
   - If yes, confidence in the causal claim increases significantly
   - If no, the hypothesized Cause is probably wrong

### Building AND Connections

In reality, most effects require multiple co-conditions. Use AND (elliptical) connectors when:
- A cause exists but the effect doesn't always occur → something else must also be present
- The user says "well, it depends on..." → that dependency is an AND condition
- The cause seems too small to explain the magnitude of the effect → additional factors are needed

Notation for the text-based tree:
```
[Effect]
    ↑
[Cause A]  AND  [Cause B]
```

Both A and B must be present for the Effect to occur. Neither alone is sufficient.

### Checkpoint 2

After connecting 3-4 UDEs with causal chains, pause:
- Generate an updated ASCII CRT diagram showing connections built so far — the user should see branches forming and beginning to converge
- "Here's what we've built so far. Let me walk through the logic..."
- Read each connection aloud: "If [cause], then [effect]. And if [cause] is real, we should also see [predicted effect]."
- "Does this match your reality? Where does it feel wrong?"
- "Do you see any connections between these branches that we haven't drawn yet?"

---

## Phase 3: Finding Root Causes and Convergence

### Goal
Trace causal chains to their deepest point until you find 1-2 root causes that explain the majority (70%+) of UDEs.

### Process

1. **Keep asking "What causes that?"** for each entity at the bottom of your current tree. Don't stop at the first plausible-sounding root cause.

2. **Test for convergence.** The hallmark of a good CRT is that branches converge:
   ```
   [UDE 1]   [UDE 2]   [UDE 3]   [UDE 4]
      ↑         ↑         ↑         ↑
   [Cause A] [Cause B] [Cause C] [Cause D]
      ↑         ↑         ↑         ↑
       ↑        ↑         ↑        ↑
        └───┬───┘         └───┬───┘
            ↑                 ↑
      [Deeper Cause X]  [Deeper Cause Y]
            ↑                 ↑
             └───────┬───────┘
                     ↑
              [ROOT CAUSE]
   ```
   If most branches converge to the same point, you've likely found something real.

3. **Challenge the root cause.** When the user thinks they've found it:
   - "If this is truly the root cause, can you trace a path from it to each of our UDEs?"
   - "What percentage of our UDEs does this explain? If it's less than 70%, we may need to dig deeper or find a second root cause."
   - "Is this root cause something that can be changed? If not, we need to keep looking — a root cause that can't be addressed isn't useful."
   - "Is this a policy, a resource limitation, a measurement, or a structural issue?"
   - "How long has this root cause existed? What created it? (This is not strictly necessary for the CRT, but often reveals important context)"

4. **Distinguish root causes from core conflicts.** If the root cause is a policy or behavior that persists despite being harmful, there's usually an underlying conflict maintaining it. This is the bridge to the Evaporating Cloud. Flag it: "It sounds like this policy exists because people are trying to protect [Need A], but it's causing these problems because it conflicts with [Need B]. Do you see that conflict?"

### Root Cause Quality Criteria

A good root cause:
- Explains 70%+ of the UDEs through traceable causal paths
- Is specific and clear (passes Clarity CLR)
- Is a condition that actually exists (passes Entity Existence CLR)
- Is actionable — changing it is within someone's control
- Is not itself a UDE — it's the thing that CAUSES the UDEs
- Often sounds uncomfortable or politically sensitive — if it's easy and obvious, you probably haven't gone deep enough

### Checkpoint 3 (Final)

Present the complete CRT:
1. Full ASCII diagram showing all UDEs, intermediate causes, AND connectors, and root cause(s) — root cause in a `*` emphasis box
2. Walk through each major causal path: "Starting from [root cause], this leads to [intermediate cause], which produces [UDE]"
3. Explicitly verify: "Does this root cause explain UDEs 1, 2, 3, 5, 7, and 8? That's 6 out of 9 — we might want to check whether UDEs 4 and 9 have a different root cause."
4. Ask: "On a scale of 1-10, how confident are you that this is the actual root cause?"

### Transition Decision

After the CRT is validated:
- If there's a clear conflict maintaining the root cause → recommend **Evaporating Cloud** (read `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/handoff-protocol.md` for CRT → EC handoff format)
- If the root cause is a physical constraint in a process → recommend **Five Focusing Steps**
- If the user already has an idea for a solution → recommend **Future Reality Tree** to validate it
- If the user wants to sit with it → that's fine too. The CRT is valuable on its own.

Prepare the handoff state as specified in `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/handoff-protocol.md` and present it to the user for confirmation before transitioning.
