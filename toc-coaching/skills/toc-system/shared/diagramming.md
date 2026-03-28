# TOC Diagramming Reference

Use diagrams throughout the coaching process to make logic visible. Diagrams are not optional decoration — they are the primary artifact of each thinking process. The user should see their logic taking shape visually as the session progresses.

Generate diagrams at every checkpoint, not just at the end. Partial, in-progress diagrams are valuable because they invite correction.

## How to Generate Diagrams

**Always use the diagram helper script.** Do not hand-draw box-drawing diagrams — character counting errors will break alignment.

Call via Bash:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON'
{ ... }
JSON
```

Wrap the script output in a code fence (triple backticks) when presenting to the user.

## When to Diagram

- After collecting UDEs (numbered list in boxes)
- After every 2-3 new causal connections in a CRT/FRT
- When presenting an Evaporating Cloud structure
- When summarizing a Five Focusing Steps analysis
- When showing PRT obstacle sequences
- Whenever the user seems confused about the structure so far

---

## Diagram Types

### Simple Box Row (`type: "boxes"`)

Use for early-stage UDE lists or any row of labeled boxes.

```json
{
  "type": "boxes",
  "boxes": [
    {"lines": ["UDE 1: MRR growth", "stalled at 2%"]},
    {"lines": ["UDE 2: Sales cycle", "lengthened to 75d"]},
    {"lines": ["UDE 3: Churn up", "from 3% to 7%"]}
  ],
  "width": 21
}
```

### Evaporating Cloud (`type: "ec"`)

Top-down layout: A at top, B/C in middle, D/D' at bottom, CONFLICT line.

```json
{
  "type": "ec",
  "A": ["A: Build sustainable", "SaaS business"],
  "B": ["B: Satisfy board", "growth mandate"],
  "C": ["C: Retain existing", "customers"],
  "D": ["D: Say yes to each", "prospect's feature", "requests"],
  "Dp": ["D': Maintain stable", "focused product", "roadmap"],
  "width": 21
}
```

### EC with Injection (`type: "ec_injection"`)

Same as EC but with a broken arrow and injection box.

```json
{
  "type": "ec_injection",
  "A": ["..."], "B": ["..."], "C": ["..."], "D": ["..."], "Dp": ["..."],
  "injection": ["INJECTION: New idea", "that breaks the", "assumption"],
  "broken_arrow": "left",
  "width": 21
}
```

`broken_arrow`: `"left"` breaks B→D, `"right"` breaks C→D'.

### Five Focusing Steps (`type: "five_steps"`)

Horizontal process flow with constraint highlighted.

```json
{
  "type": "five_steps",
  "steps": [
    {"name": "Inbound", "detail": "Leads", "capacity": "100/wk"},
    {"name": "Buffer", "detail": "", "capacity": ""},
    {"name": "Demo/Trial", "detail": "", "capacity": "30/wk", "constraint": true},
    {"name": "Close", "detail": "Deal", "capacity": "50/wk"}
  ],
  "exploit": "...",
  "subordinate": "...",
  "elevate": "..."
}
```

### Prerequisite Tree (`type: "prt"`)

Bottom-to-top IO chain with obstacles.

```json
{
  "type": "prt",
  "objective": ["OBJECTIVE: Solutions", "eng function launched"],
  "ios": [
    {"name": ["IO 1: Board approves", "strategy shift"], "obstacle": "Board wants logos"},
    {"name": ["IO 2: Team hired", "and trained"], "obstacle": "No skill set today"},
    {"name": ["IO 3: First deals", "closed"], "obstacle": "Sales doesn't trust it"}
  ],
  "width": 25
}
```

### UDE Scorecard (`type: "scorecard"`)

Progress tracking table.

```json
{
  "type": "scorecard",
  "udes": [
    {"text": "Revenue flat", "status": "resolved", "note": "by injection"},
    {"text": "Top reps leaving", "status": "partial", "note": "partially addressed"},
    {"text": "Churn high", "status": "unresolved", "note": "needs work"}
  ]
}
```

Status values: `"resolved"`, `"partial"`, `"unresolved"`.

---

## Style Guide

- **Box width**: Use 21-25 for most diagrams. All boxes in a row should use the same width.
- **Text lines**: Keep under 22 characters per line inside a box. Break into multiple lines if needed.
- **Emphasis boxes** (`╔═╗`): Used automatically for root causes, injections, constraints, and objectives.
- **ALL CAPS labels**: `ROOT CAUSE:`, `INJECTION:`, `CONSTRAINT:`, `OBJECTIVE:` for key entities.

## CRT Diagrams — Progressive Building

CRTs are built incrementally. Use multiple script calls as the tree grows:

1. **After UDE collection**: Use `type: "boxes"` to show UDEs as a row
2. **After first connections**: Use `type: "boxes"` for each level, printing them vertically with `│` and `▲` connectors between levels (hand-draw only the simple single-character connectors between script-generated box rows)
3. **At convergence**: Show the join lines and root cause

For the connectors between box rows (the `│`, `▲`, `└──┬──┘` lines), these are simple enough to hand-draw since they only use single characters at specific columns. The script output tells you exactly which column each box center is at.

## FRT Diagrams

FRTs use the same structure as CRTs (bottom-to-top) but with:
- Injection in emphasis box at the bottom
- Desirable Effects (DEs) replacing UDEs at the top
- Negative branches shown as separate box rows off to the side with dashed connectors

Use `type: "boxes"` with `"style": "emphasis"` for injections and trimming injections.

## Two-Phase Diagram Pattern — MANDATORY

When generating any diagram, ALWAYS follow this two-step process:

**Phase 1 — Generate:** Run the diagram script via Bash. This produces pixel-perfect output.

**Phase 2 — Present:** Take the EXACT script output and include it in a code fence in your response. Never rewrite, simplify, or approximate the diagram.

**CRITICAL rendering rules:**
- ALWAYS write at least one line of plain text BEFORE the code fence. The terminal renderer mangles box-drawing characters that appear as the first line of output. A simple lead-in like "Here's the Cloud:" or "Here's what the tree looks like so far:" is enough.
- ALWAYS wrap diagrams in triple-backtick code fences to preserve alignment.
- Never paste diagram output as raw unquoted text in your response.

**Why this matters:** If you try to compose the diagram and coaching response in one mental step, you will redraw the diagram from memory and get the alignment wrong. By generating first and presenting second, the diagram is always correct. And if box-drawing characters appear as the first line of your response (or without a code fence), the terminal will break the alignment.

Example flow:
1. Call Bash: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON' ... JSON`
2. Receive output (perfectly aligned boxes)
3. In your response, write: coaching text → code fence with exact output → more coaching text / question

**Never start your response with a code fence. Always lead with text.**

## Common Mistakes to Avoid

1. **Hand-drawing box diagrams** — use the script. Character counting errors are inevitable.
2. **Too many levels at once** — build progressively. Show 3-4 entities first, then expand.
3. **Missing code fences** — always wrap diagram output in triple backticks.
4. **Starting response with a diagram** — always write a plain text line first, then the code fence. The terminal breaks box-drawing characters that appear as the first output line.
5. **Pasting diagrams as raw text** — never paste box-drawing output outside a code fence.
6. **Boxes too wide** — keep inner width at 21-25 characters. Wider boxes are harder to read.
