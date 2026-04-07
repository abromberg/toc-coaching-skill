# TOC Coaching System

A [Theory of Constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) coaching system that walks you through Goldratt's Thinking Processes to solve problems.

Distributed as a **Claude Code plugin**. See the [blog post](https://andybromberg.com/theory-of-constraints-skill) for background and motivation.

## Install

```bash
claude plugin marketplace add abromberg/toc-coaching-skill
claude plugin install toc-coaching@toc-marketplace
```

## Usage

Type `/toc-coaching` and describe your problem. The skill also auto-triggers on TOC-relevant situations.

If you know which tool you want, just say so: "I want to do a CRT" or "Let's build an Evaporating Cloud," but generally, you can just type `/toc-coaching` with your problem and it will find the right tool for the job.

<img width="1773" height="1210" alt="Xnapper-2026-04-07-15 05 20" src="https://github.com/user-attachments/assets/0c39f1d2-38b9-4c6c-b459-5df5d45eb892" />

## The Thinking Process Tools

| Tool | Question it answers | When to use |
|------|-------------------|-------------|
| Current Reality Tree (CRT) | What to change? | Multiple symptoms, unknown root cause |
| Evaporating Cloud (EC) | What to change to? | Two needs that seem to conflict |
| Five Focusing Steps | Where's the constraint? | Operational system, throughput improvement |
| Future Reality Tree (FRT) | Will this work? | Validating a proposed solution |
| Prerequisite + Transition Tree | How to cause the change? | Implementation planning |

## How a Session Works

1. You describe your problem (via `/toc-coaching` or just talking)
2. The router asks a few diagnostic questions to figure out which tool fits
3. It loads the right flow and walks you through each phase — asking questions, challenging logic, building the tree or cloud incrementally
4. At every checkpoint you see a diagram of your progress
5. At the end you get the complete diagram and a recommendation for what's next
6. If continuing to another flow, state transfers automatically

<details>
<summary>What's inside</summary>

```
toc-coaching/                          <- the plugin
├── .claude-plugin/
│   └── plugin.json                    <- plugin manifest
├── skills/toc-system/
    ├── SKILL.md                       <- Master router (auto-invoked)
    ├── flows/
    │   ├── crt/SKILL.md               <- Current Reality Tree
    │   ├── ec/SKILL.md                <- Evaporating Cloud
    │   ├── five-steps/SKILL.md        <- Five Focusing Steps
    │   ├── frt/SKILL.md               <- Future Reality Tree
    │   └── prt-tt/SKILL.md            <- Prerequisite + Transition Tree
    └── shared/
        ├── jonah-voice.md             <- Coaching voice guide
        ├── toc-logic-rules.md         <- CLR rules & logic validation
        ├── question-bank.md           <- Socratic questions by flow
        ├── diagramming.md             <- ASCII diagram templates
        ├── handoff-protocol.md        <- State transfer between flows
        └── toc-diagram.py             <- Diagram generation script so Claude doesn't screw up the box offsets :)
```

</details>
