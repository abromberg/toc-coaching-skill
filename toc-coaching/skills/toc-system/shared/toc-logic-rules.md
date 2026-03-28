# TOC Logic Rules & Validation Standards

This reference defines the logical foundations used across all TOC Thinking Process flows. Every tree and cloud built in this system must be validated against these rules.

## Two Types of Logic in TOC

### Sufficiency Logic (used in CRT, FRT, Transition Tree)
- Read as: "If A, then B" — A is **sufficient** to cause B
- The arrow means: the existence of A alone is enough to produce B
- When multiple causes are needed together, use an elliptical AND connector: "If A AND B, then C" — neither A nor B alone is sufficient, but together they are
- Magnitudinal AND: A and B independently contribute to C, and between them produce enough effect

### Necessity Logic (used in Evaporating Cloud, Prerequisite Tree)
- Read as: "In order to have A, we must have B" — B is **necessary** for A
- The arrow means: without B, A cannot exist
- This is NOT the same as "B causes A" — it means B is a prerequisite condition

Confusing these two logic types is one of the most common errors. The AI coach must identify which logic type is active in the current flow and enforce it consistently.

## Categories of Legitimate Reservation (CLR)

The CLR are the formal rules for validating any cause-effect or necessity relationship in a TOC logic tree. They are grouped into three levels of increasing depth. When reviewing user-constructed logic, apply them in order.

### Level I: Clarity

**1. Clarity Reservation**
- Does the entity (statement in a box) mean what the builder intends?
- Is the language precise enough that two people would interpret it the same way?
- Are there hidden ambiguities, jargon, or vague qualifiers ("sometimes," "usually," "a lot")?
- Test: Can you restate it and get the builder to agree that your restatement captures their meaning?

Red flags to challenge:
- "We have a communication problem" → What specifically is not being communicated, to whom, causing what observable effect?
- "Morale is low" → What behaviors are you observing that you're labeling as low morale?
- "The process is broken" → Which step, what happens, what should happen instead?

### Level II: Existence

**2. Entity Existence**
- Does the stated entity actually exist in reality?
- Is there observable evidence for it, or is it an assumption being stated as fact?
- Test: Can the builder point to specific, concrete evidence that this condition is real?
- Common failure: Stating a belief or fear as if it were an observed reality

**3. Causality Existence**
- Does the causal relationship actually exist between the stated cause and effect?
- Just because A and B both exist doesn't mean A causes B
- Test: If we removed cause A, would effect B actually diminish or disappear?
- Test: Can you describe the mechanism by which A produces B?
- Common failure: Confusing correlation, co-occurrence, or sequence with causation

### Level III: Sufficiency and Rigor

**4. Cause Insufficiency**
- Is the stated cause, by itself, really enough to produce the stated effect?
- Or does it require additional conditions (AND connectors) that haven't been stated?
- Test: Can you think of a situation where the cause exists but the effect does NOT occur? If yes, what additional condition is needed?
- Common failure: Stating a contributing factor as if it were the complete cause

**5. Additional Cause (Alternative Cause)**
- Could something entirely different also cause the same effect?
- If so, the tree may be pointing at the wrong root cause
- Test: If we completely eliminated the stated cause, could the effect still occur due to something else?
- This does not invalidate the stated cause — it means the tree is potentially incomplete
- Common failure: Fixating on one cause when multiple independent causes produce the same UDE

**6. Cause-Effect Reversal**
- Is the arrow pointing the wrong way? Could B actually be causing A?
- Test: Which came first? Which can exist without the other?
- Test: If we intervened to change A, would B change? If we intervened to change B, would A change?
- Common failure: "We have high turnover because morale is low" — is it possible that morale is low because people see colleagues leaving?

**7. Predicted Effect Existence**
- If the stated cause-effect relationship is real, what OTHER effects should also be observable?
- This is the most powerful validation tool: a real cause should produce multiple verifiable effects
- Test: "If A really does cause B, then we should also see C. Do we see C?"
- Goldratt called this "Effect-Cause-Effect" — the core validation mechanism
- Common failure: A causal claim that only explains one effect when a real root cause should explain many

**8. Tautology (Circular Logic)**
- Is the effect just a restatement of the cause in different words?
- Test: Remove the cause — does the effect still say something independent?
- Example of tautology: "Because customers are dissatisfied (cause) → We get negative feedback (effect)" — these are the same thing stated differently
- Common failure: Feeling productive building the tree while actually going in circles

## Applying CLR in Practice

When reviewing a user's logic, do NOT dump all eight categories at once. Instead:

1. Start with Clarity — most trees fail here before anything else
2. Check Entity Existence for any statement that feels like an assumption
3. Check Causality Existence for every arrow
4. Apply Level III reservations selectively where the logic feels thin

The goal is not to be pedantic. The goal is to ensure the user's tree represents reality as accurately as possible, because every decision built on this tree depends on it being right.

## Sufficiency Logic Validation Checklist (for CRT and FRT)

For every "If... Then..." connection, verify:
- [ ] The cause is clearly stated (Clarity)
- [ ] The cause actually exists in reality (Entity Existence)
- [ ] There is a real causal mechanism, not just correlation (Causality Existence)
- [ ] The cause alone is sufficient, or necessary AND connectors are included (Cause Insufficiency)
- [ ] Alternative causes have been considered (Additional Cause)
- [ ] The arrow direction is correct (Cause-Effect Reversal)
- [ ] Other predicted effects of this cause are observable (Predicted Effect Existence)
- [ ] The connection is not circular (Tautology)

## Necessity Logic Validation Checklist (for EC and PRT)

For every "In order to... we must..." connection, verify:
- [ ] Both entities are clearly stated (Clarity)
- [ ] The objective/need actually exists and matters (Entity Existence)
- [ ] The stated prerequisite is truly necessary, not merely helpful (Necessity Existence)
- [ ] The stated prerequisite is not a disguised want or solution (check for hidden assumptions)

## Key Principle: Intellectual Honesty

Goldratt's thinking processes only work when participants are willing to follow the logic wherever it leads — even when it points to uncomfortable truths about their own decisions, policies, or assumptions. The AI coach should model this by being willing to challenge the user respectfully but directly, and by never accepting a causal claim just because the user states it confidently.

As Elliot Temple has emphasized in his analysis of TOC: the rigor of the thinking processes is what separates them from generic brainstorming. Weakening the logic rules to be "nice" defeats the entire purpose. The coach should be kind in tone but relentless in logic.
