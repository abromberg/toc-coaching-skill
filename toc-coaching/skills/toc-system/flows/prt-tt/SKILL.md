---
name: toc-prt-tt
description: >
  Prerequisite Tree (PRT) and Transition Tree (TT) coaching flow — guides users
  through implementation planning by identifying obstacles, sequencing intermediate
  objectives, and building detailed action plans. Use when the user has a validated
  solution and needs to figure out how to actually make it happen. This is the
  "How to cause the change?" tool.
preconditions:
  - User has a validated solution or injection to implement
  - TT phase requires PRT obstacles and IOs to be sequenced first
  - Each TT step requires the previous IO to be clearly defined
---

# Prerequisite Tree (PRT) + Transition Tree (TT) Flow

These two tools answer: **"How to cause the change?"** The PRT identifies obstacles and sequences intermediate objectives. The TT builds the detailed action plan for each step. Together, they turn an injection into reality.

Before starting, read:
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-logic-rules.md` — the PRT uses necessity logic; the TT uses sufficiency logic
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/diagramming.md` — diagram templates and the generation script
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/question-bank.md` — consult the PRT/TT section
- If arriving from an FRT: read the handoff state from `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/handoff-protocol.md`

## When to Use Each Tool

**PRT only:** When the injection is complex and has many obstacles, but the individual steps to overcome each obstacle are straightforward.

**TT only:** When the path is clear but the detailed action sequence needs to be worked out carefully (e.g., politically sensitive changes where each step's framing matters).

**PRT then TT:** When both are needed — PRT to map the obstacle landscape and sequence, TT to detail the critical-path steps.

Most real implementations benefit from at least a PRT.

---

## Part 1: Prerequisite Tree (PRT)

### Purpose
The PRT identifies every obstacle standing between the current state and the implemented injection, then determines the intermediate objectives (IOs) needed to overcome each obstacle, and sequences them.

### Logic Type
The PRT uses **necessity logic**: "In order to achieve [IO or injection], we must first overcome [obstacle]." This is different from the sufficiency logic used in CRT/FRT.

### Phase 1: Define the Objective

The PRT's objective is the injection (or set of injections) from the FRT, stated clearly:
- "What specifically do we need to have in place? What does 'done' look like?"
- "Is this a single objective or multiple objectives? If multiple, which one do we tackle first?"

### Phase 2: Identify Obstacles

This is a brainstorming phase. For the target objective, systematically identify everything that stands in the way:

1. **Ask broadly first:**
   - "What stands between where you are now and this being fully implemented?"
   - "What could prevent this from working?"
   - "What's the hardest part about making this real?"

2. **Probe specific categories:**
   - **People obstacles:** "Who would resist this? Why? Whose cooperation is essential but not guaranteed?"
   - **Resource obstacles:** "What resources (money, time, people, tools) don't you have yet?"
   - **Knowledge obstacles:** "What do you not yet know how to do? What information is missing?"
   - **Policy obstacles:** "What existing rules, contracts, or processes conflict with this change?"
   - **Sequencing obstacles:** "What must happen before something else can happen?"
   - **External obstacles:** "What depends on parties outside your control (customers, vendors, regulators)?"

3. **Challenge each obstacle:**
   - "Is this a real obstacle, or is it a fear? What evidence do you have?"
   - "Is this obstacle permanent, or is it only an obstacle under current conditions?"
   - "Could this obstacle be bypassed entirely rather than overcome?"

### Phase 3: Define Intermediate Objectives

For each real obstacle, define what needs to be true for the obstacle to be overcome:
- "What condition, once achieved, means this obstacle no longer blocks us?"
- State each IO as a positive condition, not a negation: "Sales team trained on new approach" not "Sales team no longer untrained"

### Phase 4: Sequence the IOs

Determine dependencies:
- "Which IOs must be completed before others can start?"
- "Which IOs are independent and can happen in parallel?"
- "What's the critical path — the longest chain of dependent IOs?"

### Checkpoint 1
Present the PRT as a sequence:

```
[INJECTION: Create solutions engineering function]
                    ↑
         ┌──────────┴──────────┐
         │                     │
[IO: Sales team trained   [IO: Solutions engineering
 on consultative selling]  team hired and onboarded]
         ↑                     ↑
         │              ┌──────┴──────┐
         │              │             │
[IO: New sales     [IO: Job       [IO: Playbook of
 playbook created]  descriptions   common enterprise
                    & hiring       configurations
                    pipeline       documented]
                    established]        ↑
                                       │
                              [IO: Top 20 enterprise
                               use cases catalogued]

OBSTACLES OVERCOME:
- Sales team doesn't know how to sell without promising features → Training + playbook
- No solutions engineers exist yet → Hiring pipeline
- No institutional knowledge of configuration patterns → Use case catalog + playbook
```

Ask: "Does this sequence make sense? Are there obstacles we missed? Are any IOs in the wrong order?"

---

## Part 2: Transition Tree (TT)

### Purpose
The TT details the specific actions for critical-path IOs, including: what the current reality is before each action, what action is taken, what the expected new reality is after the action, and why the action should produce that result.

### Logic Type
The TT uses **sufficiency logic** with a four-element structure for each step:

1. **Current Reality (CR):** What exists right now, before this action
2. **Need:** Why this action is necessary (the objective it serves)
3. **Action:** The specific thing someone does
4. **Expected Effect:** What should be true after the action succeeds

Read as: "Given [Current Reality] and [Need], if we take [Action], then [Expected Effect]."

### When to Build a Full TT

Build a TT for:
- Steps that are politically sensitive (getting buy-in from resistant stakeholders)
- Steps where the action isn't obvious and the "how" matters
- Steps where failure would be costly or hard to reverse
- The first 2-3 steps of the implementation (to build momentum)

Don't build a TT for:
- Routine or well-understood tasks (just list them)
- Steps where the user already has a clear plan

### Phase 5: Build the TT for Critical Steps

For each critical-path IO from the PRT:

1. **Define current reality:**
   - "Before this step, what's the situation? What exists and what doesn't?"
   - "Who knows what? What has been communicated?"

2. **Define the need:**
   - "Why is this step necessary? What does it accomplish for the overall plan?"

3. **Define the specific action:**
   - "What exactly does someone DO? Not a goal, not an aspiration — a concrete action."
   - "Who does it? When? With what resources?"
   - "What's the very first physical action on Monday morning?"

4. **Define the expected effect:**
   - "After this action, what's changed? What's the new state of reality?"
   - "How will you know it worked? What evidence would confirm success?"

5. **Validate the logic:**
   - "Given [CR] and [Need], if [Action], then [Expected Effect]" — does this hold?
   - "Is the action sufficient to produce the expected effect, or does it need supporting conditions?"
   - "What could go wrong between the action and the expected effect?"

### Example TT Step:

```
Step 1: Get CEO alignment on the new approach

Current Reality: CEO currently says yes to enterprise feature requests under
                 board pressure. No alternative approach has been presented.

Need: CEO buy-in is prerequisite for every other change. Without it, sales
      will continue the old pattern regardless of any new processes.

Action: Present the CRT/EC analysis to CEO in a 1-hour working session.
        Walk through the causal chain showing how saying "yes" to features
        is the root cause of churn and growth stall. Present the injection
        (solutions engineering) and the FRT showing expected results.
        Use the board's own growth mandate as the framing.

Expected Effect: CEO understands the systemic problem, agrees to pilot the
                 new approach for 90 days, and commits to a moratorium on
                 new custom feature promises during the pilot.

Validation: If this works, we should see: CEO stops making feature
            commitments in prospect meetings within 1 week. CEO
            communicates the pilot to the sales team within 2 weeks.
```

### Checkpoint 2 (Final)
Present the complete implementation plan:

1. **PRT overview:** All obstacles, IOs, and sequencing
2. **TT detail:** For critical-path steps
3. **Timeline:** Rough sequence with dependencies
4. **First actions:** The very first 1-2 things to do this week
5. **Success criteria:** How will you know each step worked?
6. **Risk mitigation:** For each major risk, what's the contingency?

Ask:
- "Does this plan feel achievable? What's the biggest risk?"
- "Who needs to see this plan? How will you present it?"
- "What's the very first action — can you commit to doing it this week?"

---

## Handling Backtracking

Implementation planning often reveals that the injection needs refinement:

- If an obstacle is truly insurmountable → return to **EC** to find a different injection
- If the implementation plan reveals new UDEs → return to **FRT** to check for Negative Branches
- If the user realizes the original problem was misdiagnosed → return to **CRT**

This is normal and healthy. Goldratt said "ideas are not yet solutions" — the full thinking process includes iteration.

---

## Tone for This Flow

The PRT/TT phase is where abstract thinking meets concrete reality. Users often feel overwhelmed here. The coach should:

- **Break it into small pieces.** Don't present a 20-step plan all at once.
- **Focus on "what's the very next thing."** Action orientation reduces anxiety.
- **Acknowledge the difficulty.** "This is the hard part — turning insight into action. Let's take it one step at a time."
- **Celebrate progress.** When an obstacle is overcome or an action is completed, note it. Momentum matters.
- **Stay grounded.** If the plan is getting too complex, challenge: "Do we really need all of this? What's the minimum viable implementation that tests the injection?"
