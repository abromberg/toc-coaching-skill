#!/usr/bin/env python3
"""
TOC Diagram Helper — generates properly-aligned box-drawing diagrams.

Usage from Claude Code (via Bash tool):

  python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON'
  {
    "type": "boxes",
    "boxes": [
      {"lines": ["UDE 1: MRR growth", "stalled at 2%"]},
      {"lines": ["UDE 2: Sales cycle", "lengthened to 75d"]},
      {"lines": ["UDE 3: Churn up", "from 3% to 7%"]}
    ],
    "width": 23,
    "style": "normal"
  }
  JSON

  python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON'
  {
    "type": "crt",
    "levels": [
      {"boxes": [["UDE 1: MRR growth", "stalled at 2%"], ["UDE 2: Sales", "cycle lengthened"], ["UDE 3: Churn up", "from 3% to 7%"]]},
      {"boxes": [["New customer", "acquisition slow"], ["Prospects can't", "get clear ROI"], ["Product quality", "declining"]]},
      {"boxes": [["Product position", "keeps shifting"], ["Engineering", "spread too thin"]], "align": "right"},
      {"boxes": [["ROOT CAUSE:", "No stable product", "strategy"]], "style": "emphasis"}
    ],
    "width": 21
  }
  JSON

  python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON'
  {
    "type": "ec",
    "A": ["A: Build sustainable", "SaaS business"],
    "B": ["B: Satisfy board", "growth mandate"],
    "C": ["C: Retain existing", "customers"],
    "D": ["D: Say yes to each", "prospect's feature", "requests"],
    "Dp": ["D': Maintain stable", "focused product", "roadmap"],
    "width": 20
  }
  JSON

  python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON'
  {
    "type": "ec_injection",
    "A": ["A: Build sustainable", "SaaS business"],
    "B": ["B: Satisfy board", "growth mandate"],
    "C": ["C: Retain existing", "customers"],
    "D": ["D: Say yes to each", "prospect's feature", "requests"],
    "Dp": ["D': Maintain stable", "focused product", "roadmap"],
    "injection": ["INJECTION: Reposition", "sales from 'yes' to", "'here's how we solve", "your real problem.'"],
    "broken_arrow": "left",
    "width": 20
  }
  JSON

  python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON'
  {
    "type": "five_steps",
    "steps": [
      {"name": "Inbound", "detail": "Leads", "capacity": "100/wk"},
      {"name": "Qualify", "detail": "Leads", "capacity": "80/wk"},
      {"name": "Buffer", "detail": "", "capacity": ""},
      {"name": "Demo/Trial", "detail": "", "capacity": "30/wk", "constraint": true},
      {"name": "Close", "detail": "Deal", "capacity": "50/wk"}
    ],
    "exploit": "Zero no-shows, pre-qualify every demo",
    "subordinate": "Marketing caps at 30 qualified leads/wk",
    "elevate": "Hire 2nd solutions eng after exploit + subordinate"
  }
  JSON

  python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON'
  {
    "type": "prt",
    "objective": ["OBJECTIVE: Solutions", "eng function launched"],
    "ios": [
      {"name": ["IO 1: Board approves", "strategy shift"], "obstacle": "Board wants logos, not 'approach'"},
      {"name": ["IO 2: Solutions eng", "team hired & trained"], "obstacle": "No one has this skill set today"},
      {"name": ["IO 3: First 3 deals", "closed w/ new model"], "obstacle": "Sales team doesn't trust approach"}
    ],
    "width": 25
  }
  JSON

  python3 ${CLAUDE_PLUGIN_ROOT}/skills/toc-system/shared/toc-diagram.py <<'JSON'
  {
    "type": "scorecard",
    "udes": [
      {"text": "Revenue flat", "status": "resolved", "note": "by injection"},
      {"text": "Sales cycle long", "status": "resolved", "note": "by injection"},
      {"text": "Churn high", "status": "resolved", "note": "by injection"},
      {"text": "Top reps leaving", "status": "partial", "note": "partially addressed"},
      {"text": "Roadmap unstable", "status": "resolved", "note": "by injection"}
    ]
  }
  JSON
"""

import json
import sys


def box(lines, width=None, style='normal'):
    """Generate a properly aligned text box. Returns list of strings."""
    min_width = max(len(l) for l in lines) + 2  # 1 char padding each side
    if width is None:
        width = min_width
    else:
        width = max(width, min_width)
    chars = {
        'normal': ('┌', '┐', '└', '┘', '─', '│'),
        'emphasis': ('╔', '╗', '╚', '╝', '═', '║'),
    }
    tl, tr, bl, br, h, v = chars[style]
    out = []
    out.append(f"{tl}{h * width}{tr}")
    for l in lines:
        out.append(f"{v}{(' ' + l).ljust(width)}{v}")
    out.append(f"{bl}{h * width}{br}")
    return out


def box_width(box_lines):
    """Get the display width of a rendered box."""
    return len(box_lines[0])


def box_center(box_lines):
    """Get the center column index of a rendered box."""
    return len(box_lines[0]) // 2


def side_by_side(box_groups, gap=2):
    """Render multiple boxes side by side. Returns list of strings."""
    max_h = max(len(b) for b in box_groups)
    for b in box_groups:
        w = len(b[0])
        while len(b) < max_h:
            b.append(' ' * w)
    spacer = ' ' * gap
    result = []
    for row in zip(*box_groups):
        result.append(spacer.join(row))
    return result


def place_boxes(boxes, positions, total_width):
    """Place boxes at specific column positions. Returns list of strings."""
    max_h = max(len(b) for b in boxes)
    for b in boxes:
        w = len(b[0])
        while len(b) < max_h:
            b.append(' ' * w)
    result = []
    for row_idx in range(max_h):
        line = [' '] * total_width
        for bi, b in enumerate(boxes):
            pos = positions[bi]
            for j, ch in enumerate(b[row_idx]):
                if pos + j < total_width:
                    line[pos + j] = ch
        result.append(''.join(line).rstrip())
    return result


def make_line(total_width, chars_at_positions):
    """Make a line with specific characters at specific positions."""
    line = [' '] * total_width
    for pos, ch in chars_at_positions:
        if 0 <= pos < total_width:
            line[pos] = ch
    return ''.join(line).rstrip()


def render_boxes(data):
    """Render a simple row of boxes."""
    w = data.get('width', 23)
    style = data.get('style', 'normal')
    boxes = [box(b['lines'], w, b.get('style', style)) for b in data['boxes']]
    for line in side_by_side(boxes, gap=2):
        print(line)


def render_crt(data):
    """Render a Current Reality Tree."""
    w = data.get('width', 21)
    levels = data['levels']
    all_lines = [l for level in levels for b in level['boxes'] for l in b]
    if all_lines:
        w = max(w, max(len(l) for l in all_lines) + 2)
    gap = 2

    for li, level in enumerate(levels):
        style = level.get('style', 'normal')
        boxes = [box(b, w, style) for b in level['boxes']]
        bw = w + 2

        if level.get('align') == 'right':
            # Right-align: position boxes to align with the rightmost boxes of the previous level
            prev_count = len(levels[li-1]['boxes']) if li > 0 else len(boxes)
            total_w = prev_count * bw + (prev_count - 1) * gap
            n = len(boxes)
            actual_w = n * bw + (n - 1) * gap
            offset = total_w - actual_w
            for line in side_by_side(boxes, gap):
                print(' ' * offset + line)
        elif level.get('align') == 'center' or len(boxes) == 1:
            # Center single boxes
            first_level_count = len(levels[0]['boxes'])
            total_w = first_level_count * bw + (first_level_count - 1) * gap
            for b_line in boxes[0]:
                pad = (total_w - len(b_line)) // 2
                print(' ' * pad + b_line)
        else:
            for line in side_by_side(boxes, gap):
                print(line)

        # Draw connectors to next level
        if li < len(levels) - 1:
            n = len(boxes)
            next_n = len(levels[li+1]['boxes'])
            total_w = max(n, len(levels[0]['boxes'])) * bw + (max(n, len(levels[0]['boxes'])) - 1) * gap

            # Get center columns for current level's boxes
            if level.get('align') == 'right':
                prev_count = len(levels[li-1]['boxes']) if li > 0 else n
                prev_total_w = prev_count * bw + (prev_count - 1) * gap
                offset = prev_total_w - (n * bw + (n - 1) * gap)
                centers = [offset + i * (bw + gap) + bw // 2 for i in range(n)]
            else:
                centers = [i * (bw + gap) + bw // 2 for i in range(n)]

            # Vertical lines down
            print(make_line(total_w, [(c, '│') for c in centers]))
            print(make_line(total_w, [(c, '▲') for c in centers]))

            # If next level has fewer boxes, draw join lines
            if next_n < n:
                next_level = levels[li+1]
                if next_level.get('align') == 'right':
                    # Right-aligned: connect rightmost centers
                    right_centers = centers[-next_n:]
                    # Just show connectors for the ones that continue
                elif next_n == 1:
                    # Single box: join all to center
                    left = min(centers)
                    right = max(centers)
                    mid = (left + right) // 2
                    join = [' '] * total_w
                    for i in range(left, right + 1):
                        join[i] = '─'
                    join[left] = '└'
                    join[right] = '┘'
                    join[mid] = '┬'
                    print(''.join(join).rstrip())
                    print(make_line(total_w, [(mid, '│')]))
                    print(make_line(total_w, [(mid, '▲')]))


def render_ec(data):
    """Render an Evaporating Cloud (top-down layout)."""
    w = data.get('width', 20)
    all_lines = data['A'] + data['B'] + data['C'] + data['D'] + data['Dp']
    w = max(w, max(len(l) for l in all_lines) + 2)
    bw = w + 2
    gap = 4
    pair_width = 2 * bw + gap
    total_w = pair_width + 8  # some margin

    bA = box(data['A'], w)
    bB = box(data['B'], w)
    bC = box(data['C'], w)
    bD = box(data['D'], w)
    bDp = box(data['Dp'], w)

    mid = total_w // 2
    left_start = (total_w - pair_width) // 2
    right_start = left_start + bw + gap
    left_col = left_start + bw // 2
    right_col = right_start + bw // 2

    # A box centered
    a_pad = (total_w - len(bA[0])) // 2
    for l in bA:
        print(' ' * a_pad + l)

    # Connector from A
    print(make_line(total_w, [(mid, '│')]))

    # Split line
    split = [' '] * total_w
    for i in range(left_col, right_col + 1):
        split[i] = '─'
    split[left_col] = '┌'
    split[right_col] = '┐'
    split[mid] = '┴'
    print(''.join(split).rstrip())

    print(make_line(total_w, [(left_col, '│'), (right_col, '│')]))
    print(make_line(total_w, [(left_col, '▼'), (right_col, '▼')]))

    # B and C
    for l in place_boxes([bB, bC], [left_start, right_start], total_w):
        print(l)

    print(make_line(total_w, [(left_col, '│'), (right_col, '│')]))
    print(make_line(total_w, [(left_col, '▼'), (right_col, '▼')]))

    # D and D'
    for l in place_boxes([bD, bDp], [left_start, right_start], total_w):
        print(l)

    # CONFLICT line
    print(make_line(total_w, [(left_col, '│'), (right_col, '│')]))
    conflict_line = [' '] * total_w
    for i in range(left_col, right_col + 1):
        conflict_line[i] = '─'
    conflict_line[left_col] = '└'
    conflict_line[right_col] = '┘'
    label = " CONFLICT "
    cm = (left_col + right_col) // 2 - len(label) // 2
    for j, ch in enumerate(label):
        conflict_line[cm + j] = ch
    print(''.join(conflict_line).rstrip())


def render_ec_injection(data):
    """Render an EC with injection."""
    w = data.get('width', 20)
    all_lines = data['A'] + data['B'] + data['C'] + data['D'] + data['Dp']
    w = max(w, max(len(l) for l in all_lines) + 2)
    bw = w + 2
    gap = 4
    pair_width = 2 * bw + gap
    total_w = pair_width + 8

    bA = box(data['A'], w)
    bB = box(data['B'], w)
    bC = box(data['C'], w)
    bD = box(data['D'], w)
    bDp = box(data['Dp'], w)

    mid = total_w // 2
    left_start = (total_w - pair_width) // 2
    right_start = left_start + bw + gap
    left_col = left_start + bw // 2
    right_col = right_start + bw // 2

    broken = data.get('broken_arrow', 'left')

    # A box centered
    a_pad = (total_w - len(bA[0])) // 2
    for l in bA:
        print(' ' * a_pad + l)

    print(make_line(total_w, [(mid, '│')]))

    split = [' '] * total_w
    for i in range(left_col, right_col + 1):
        split[i] = '─'
    split[left_col] = '┌'
    split[right_col] = '┐'
    split[mid] = '┴'
    print(''.join(split).rstrip())

    print(make_line(total_w, [(left_col, '│'), (right_col, '│')]))
    print(make_line(total_w, [(left_col, '▼'), (right_col, '▼')]))

    for l in place_boxes([bB, bC], [left_start, right_start], total_w):
        print(l)

    print(make_line(total_w, [(left_col, '│'), (right_col, '│')]))

    if broken == 'left':
        print(make_line(total_w, [(left_col, 'X'), (right_col, '▼')]))
    else:
        print(make_line(total_w, [(left_col, '▼'), (right_col, 'X')]))

    for l in place_boxes([bD, bDp], [left_start, right_start], total_w):
        print(l)

    # Injection box
    if 'injection' in data:
        print()
        inj = box(data['injection'], None, 'emphasis')
        inj_pad = (total_w - len(inj[0])) // 2
        for l in inj:
            print(' ' * max(0, inj_pad) + l)


def render_five_steps(data):
    """Render a Five Focusing Steps process diagram."""
    steps = data['steps']
    w = 12

    boxes = []
    for s in steps:
        style = 'emphasis' if s.get('constraint') else 'normal'
        label = 'CONSTRAINT' if s.get('constraint') else s['name']
        lines = [label]
        if s.get('detail'):
            lines.append(s['detail'])
        elif s.get('constraint'):
            lines.append(s['name'])
        else:
            lines.append('')
        lines.append(s.get('capacity', ''))
        boxes.append(box(lines, w, style))

    arrow = '───►'
    for row_idx in range(len(boxes[0])):
        parts = []
        for bi, b in enumerate(boxes):
            parts.append(b[row_idx])
            if bi < len(boxes) - 1:
                if row_idx == 2:
                    parts.append(arrow)
                else:
                    parts.append(' ' * len(arrow))
        print(''.join(parts))

    print()
    if data.get('exploit'):
        print(f"EXPLOIT:      {data['exploit']}")
    if data.get('subordinate'):
        print(f"SUBORDINATE:  {data['subordinate']}")
    if data.get('elevate'):
        print(f"ELEVATE:      {data['elevate']}")


def render_prt(data):
    """Render a Prerequisite Tree."""
    w = data.get('width', 25)
    bw = w + 2
    indent = 12
    mid = indent + bw // 2

    # Objective
    obj = box(data['objective'], w, 'emphasis')
    for r in obj:
        print(' ' * indent + r)

    # IOs in reverse order (bottom to top, but we print top to bottom)
    ios = list(reversed(data['ios']))
    for io in ios:
        print(make_line(80, [(mid, '│')]))
        print(make_line(80, [(mid, '▲')]))

        io_box = box(io['name'], w)
        obs_text = f"◄╌╌╌ Obstacle: {io['obstacle']}"
        for i, r in enumerate(io_box):
            if i == 1:  # first content line
                print(' ' * indent + r + '  ' + obs_text)
            else:
                print(' ' * indent + r)


def render_scorecard(data):
    """Render a UDE scorecard."""
    print("UDE Status:")
    for i, ude in enumerate(data['udes'], 1):
        status = ude['status']
        if status == 'resolved':
            marker = '[x]'
        elif status == 'partial':
            marker = '[~]'
        else:
            marker = '[ ]'
        text = f"UDE {i}: {ude['text']}"
        note = ude.get('note', '')
        print(f"  {marker} {text:<40s} -- {note}")

    resolved = sum(1 for u in data['udes'] if u['status'] == 'resolved')
    partial = sum(1 for u in data['udes'] if u['status'] == 'partial')
    total = len(data['udes'])
    print()
    print(f"  Score: {resolved}/{total} resolved, {partial} partial")


def main():
    raw = sys.stdin.read().strip()
    data = json.loads(raw)
    diagram_type = data['type']

    renderers = {
        'boxes': render_boxes,
        'crt': render_crt,
        'ec': render_ec,
        'ec_injection': render_ec_injection,
        'five_steps': render_five_steps,
        'prt': render_prt,
        'scorecard': render_scorecard,
    }

    renderer = renderers.get(diagram_type)
    if renderer:
        print()  # blank line so box-drawing chars aren't on first line of output
        renderer(data)
    else:
        print(f"Unknown diagram type: {diagram_type}", file=sys.stderr)
        print(f"Available types: {', '.join(renderers.keys())}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
