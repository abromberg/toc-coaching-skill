---
name: toc-five-steps
description: >
  Five Focusing Steps coaching flow — guides users through Goldratt's iterative
  constraint management process: Identify, Exploit, Subordinate, Elevate, Repeat.
  Use when the user has a defined operational system (production, pipeline, process)
  and wants to improve throughput by finding and managing the constraint.
preconditions:
  - User can describe a defined system with a goal (throughput, output, delivery)
  - Exploit requires the constraint to be identified and confirmed
  - Subordinate requires exploitation opportunities to be defined first
  - Elevate requires exploit and subordinate to be completed first
---

# Five Focusing Steps Flow

The Five Focusing Steps are TOC's operational engine for continuous improvement. They apply when there's a defined system with a clear goal (throughput, output, delivery) and the user suspects something is limiting performance.

Before starting, read:
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-logic-rules.md` — constraint identification must be evidence-based, not gut-based
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/diagramming.md` — diagram templates and the generation script
- `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/question-bank.md` — consult the Five Focusing Steps section

## The Five Steps

1. **IDENTIFY** the system's constraint
2. **EXPLOIT** the constraint — get maximum output from it without spending money
3. **SUBORDINATE** everything else to the constraint
4. **ELEVATE** the constraint — invest to increase its capacity
5. **REPEAT** — go back to Step 1, and don't let inertia become the new constraint

Most organizations fail at Step 3. Many never make it past Step 1 correctly. The AI coach's primary value is ensuring the user identifies the REAL constraint and doesn't skip subordination.

## Phase 1: Define the System and Its Goal

Before identifying a constraint, you must clearly define:

### The system boundary
- "What's the system we're looking at? Where does it start and end?"
- "What goes in, and what comes out?"
- "Who are the key actors/resources within this system?"

### The goal
- "What's the goal of this system? Not 'be efficient' — what output matters?"
- Goldratt's measurement framework: **Throughput** (rate at which the system generates goal units), **Inventory/Investment** (money tied up in the system), **Operating Expense** (money spent to turn inventory into throughput)
- "If you could only improve one metric, which one would move the needle most?"

### Current performance
- "What's the system producing now vs. what it should be producing?"
- "Where are the gaps? Timing, volume, quality?"

### Checkpoint 1
Confirm: "So the system we're analyzing is [description], its goal is [throughput metric], and current performance is [X] vs. target of [Y]. Is that right?"

---

## Phase 2: Step 1 — Identify the Constraint

### What Is a Constraint?

The constraint is the resource or policy that limits the system's throughput. Key principles:

- **There is always exactly one constraint** governing system throughput at any moment (there can be near-constraints, but one is tighter than the rest)
- **Physical constraints** are tangible: a machine, a person, a department, a supplier
- **Policy constraints** are rules, measurements, or habits that limit throughput without a physical reason — these are more common and harder to see
- **Market constraints** exist when the system can produce more than the market demands
- **The constraint is NOT the same as the busiest resource.** A resource can be 100% utilized and still not be the constraint if it's not limiting overall throughput

### Identification Process

1. **Look for the pile-up.** Where does work-in-progress accumulate? The step BEFORE the pile-up is a candidate constraint.

2. **Look for the starved resource.** What step has people/machines waiting for input? The step BEFORE the starvation is a candidate.

3. **Check capacity vs. demand at each step:**
   - "For each major step in the process, what's the available capacity per unit time?"
   - "What's the demand being placed on each step?"
   - "Where is demand closest to or exceeding capacity?"

4. **Challenge the obvious answer:**
   - "You said [X] is the bottleneck. But is it the constraint — the thing that limits system throughput — or is it just the most visible problem?"
   - "If we magically gave [X] infinite capacity, would overall system throughput increase proportionally? Or would something else immediately become the limiting factor?"
   - "Is [X] always the bottleneck, or does it shift based on product mix / time of day / season?"

5. **Check for policy constraints:**
   - "Are there any rules, approvals, batch sizes, or scheduling policies that force the system to operate below its potential?"
   - "Are there measurements that encourage local optimization (e.g., efficiency per machine) at the expense of system throughput?"
   - "Is anyone doing work that doesn't contribute to throughput but feels mandatory?"

### Common Constraint Misidentification Patterns

- **Confusing a symptom with the constraint:** "We don't have enough salespeople" might be the symptom. The constraint might be "our lead qualification process wastes 60% of sales time on unqualified prospects."
- **Confusing busy with constrained:** A team at 100% utilization isn't necessarily the constraint if their output isn't what limits system throughput.
- **Missing policy constraints:** "We batch orders weekly for procurement" — this policy might be the real constraint, not the procurement team's capacity.
- **Interactive constraints:** In complex systems, the constraint can shift based on what's being processed. Help the user identify the constraint for their highest-impact work type.

### Checkpoint 2
"Based on our analysis, the constraint appears to be [X]. Here's the evidence: [pile-up here, starvation there, capacity analysis shows...]. Does this match your experience? Before we proceed, let's make sure we're not fooling ourselves — what would you expect to see if this really were the constraint?"

---

## Phase 3: Step 2 — Exploit the Constraint

### Goal
Get maximum throughput from the existing constraint WITHOUT spending money or adding resources.

### Key Questions

- "How much of the constraint's available time is currently spent on productive work? What's lost to setup, waiting, rework, breaks, interruptions?"
- "Is the constraint ever idle? When and why?"
- "Does the constraint work on low-priority items when high-priority items are waiting?"
- "Is there quality inspection BEFORE the constraint, so it never wastes time on defective inputs?"
- "Is there a buffer of ready work IN FRONT of the constraint, so it never starves?"
- "Are the constraint's operating procedures optimized, or are people 'doing it the way they always have'?"

### Exploitation Actions (patterns to suggest only AFTER the user has thought through their situation):

- Ensure the constraint never sits idle (stagger breaks, buffer work ahead of it)
- Move quality inspection to before the constraint (don't waste constraint time on defects)
- Prioritize the constraint's work by throughput impact, not by first-in-first-out
- Remove non-essential tasks from the constraint and give them to non-constraints
- Ensure the constraint has everything it needs before it needs it (no waiting for inputs, tools, information)

### Checkpoint 3
"Here's our exploitation plan: [summary]. This should increase constraint throughput by [rough estimate] without any investment. Before we move on to subordination — is this realistic? What obstacles do you see?"

---

## Phase 4: Step 3 — Subordinate Everything Else

### Why This Is the Hardest Step

Subordination means: **non-constraint resources must serve the constraint's needs, even if this means they're not running at full efficiency.** This violates every local-optimization instinct managers have.

### Key Questions

- "What are the non-constraint resources doing that hurts the constraint?"
- "Are any non-constraints producing work faster than the constraint can process it? (This creates WIP pile-up and actually slows the system down)"
- "Are there incentives or measurements that reward non-constraint efficiency? (e.g., 'everyone should be at 95% utilization')"
- "If a non-constraint has excess capacity, is it being used to support the constraint — or is it being 'kept busy' with make-work?"
- "What will managers resist about deliberately under-utilizing their resources?"

### The Subordination Test
For each non-constraint resource, ask:
- "Is this resource's output rate aligned with what the constraint needs?"
- "Could this resource do something differently that would make the constraint more productive — even if it makes this resource less 'efficient'?"

### Common Subordination Failures
- **The Efficiency Trap:** "We can't have people sitting idle!" Yes, you can — if they're non-constraints. Idle non-constraint time is expected and healthy. Busy non-constraints piling up work before the constraint is actively harmful.
- **Measurement Resistance:** If people are measured on local output, they'll resist subordination. Surface these measurements and challenge them.
- **Political Resistance:** Subordination means some departments/people are explicitly designated as "not the priority." This is politically difficult. The coach should acknowledge this and help the user plan the change management.

### Checkpoint 4
"Subordination plan: [summary]. This will likely face resistance because [specific reasons]. Before we decide whether to elevate — is the constraint still the constraint after exploitation and subordination? Sometimes these two steps are enough."

---

## Phase 5: Step 4 — Elevate the Constraint

### When to Elevate
Only after Steps 2 and 3 have been fully implemented. Many organizations skip straight to elevation (buying more equipment, hiring more people) because it feels more decisive. But exploitation and subordination are free — elevation costs money.

### Key Questions
- "After exploitation and subordination, is [constraint] still limiting throughput?"
- "If yes, what would it take to increase its capacity? What's the cost?"
- "Is this a buy-more problem (more machines, more people) or a redesign problem (different approach)?"
- "What's the ROI? If constraint throughput = system throughput, then: investment ÷ additional throughput = cost per unit of new capacity."
- "Are there creative ways to elevate that don't require capital investment? (e.g., outsourcing just the constraint step, cross-training people)"

---

## Phase 6: Step 5 — Don't Let Inertia Become the Constraint

### The Most Overlooked Step

When a constraint is broken (elevated until something else becomes the new constraint), all the policies, procedures, measurements, and behaviors built around the old constraint become dangerous inertia.

### Key Questions
- "If we break this constraint, what becomes the new one?"
- "What policies did we put in place specifically to manage the current constraint?"
- "Will those policies make sense when the constraint moves? Or will they become obstacles?"
- "What measurements need to change?"
- "Is there a risk that we'll keep managing the old constraint out of habit even after it's no longer the bottleneck?"

### The Policy Constraint Warning
Goldratt observed that physical constraints eventually get elevated, but the policies created to manage them persist. The most insidious constraints in mature organizations are not physical — they're policies, measurements, and cultural habits that once served a purpose but now limit throughput for no good reason. Flag this pattern whenever you see it.

### Checkpoint 5 (Final)
Present a complete summary:
1. System and its goal
2. Identified constraint with evidence
3. Exploitation plan
4. Subordination plan
5. Elevation recommendation (if needed)
6. Inertia risks

Ask: "Is there a core conflict embedded in this constraint — something that makes it persist even though people know it's a problem? If so, we might want to move to an Evaporating Cloud to address the underlying conflict."

### Transition Decision
- If a policy constraint was identified → recommend **EC** to resolve the underlying conflict
- If the elevation plan is a major change that needs validation → recommend **FRT**
- If the user wants to implement → recommend **PRT/TT**
- If there's a deeper systemic issue → recommend **CRT**

Prepare handoff state per `${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/handoff-protocol.md`.
