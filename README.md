# Mailroom

A small command-line tool for one newsletter, **Kettlebird Tea's Steep Club**.
It counts subscribers, checks an issue before it goes out, and sends it to a
practice mail server on this computer. No real email is ever sent.

Built step by step with Claude Code, following the Mailroom Lab in
Part III of *The AI Agent Factory*:
https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/

## Setup

Needs [uv](https://docs.astral.sh/uv/). uv installs Python 3.14 for you.

```powershell
uv sync
uv run python --version
```

## Layout

| Path | What it is |
| --- | --- |
| `AGENTS.md` | The project's rules. One more per step. |
| `CLAUDE.md` | One line, `@AGENTS.md`, so Claude Code reads the rules. |
| `notes/predictions.md` | My predictions, written before each run. |
| `lab/mailroom-lab.md` | The lab's 27 steps. |
| `lab/prompts-playbook.md` | Upgraded prompts for every step, to compare with mine. |
| `lab/practice-files/` | Made-up data, copied in when a step asks. |
