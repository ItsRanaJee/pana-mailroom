# Mailroom: project rules

These rules apply to every session in this folder. Follow them in order of the
sections below. If two rules seem to disagree, stop and ask me.

## Scope of these rules

- This file is the only source of rules for Mailroom. CLAUDE.md files in parent
  folders (n8n workflows, WordPress posting, affiliate links) do **not** apply
  here. Ignore them in this project.

## What Mailroom is

- Mailroom is a command-line tool for one newsletter: **Kettlebird Tea's Steep
  Club**, a monthly tea-box club for home tea drinkers.
- It reads the subscribers, checks an issue before it goes out, and sends it
  to a **practice** mail server on this computer. It never sends real email.

## Tools

- Python 3.14 (pinned in `.python-version`). Use **uv for everything**:
  `uv run`, `uv add`, `uv add --dev`, `uv sync`. Never call `pip`, `python`
  or `pip install` directly, and never edit `uv.lock` by hand.
- Add a dependency only when a step needs it, and tell me its name first.
- Open text files with an explicit `encoding="utf-8"`. This machine is Windows.

## Safety

- Never use a real person's email address. Use `@example.com` for made-up
  people, and `@resend.dev` (for example `delivered@resend.dev`) for practice
  sends.
- No secrets in code, tests, commits or chat. Keys come from the environment.
- Never run `git push --force`, `git reset --hard`, or delete branches or
  files I did not ask you to delete.

## Dates

- Never read today's date inside the logic. Pass the run date in. Only the
  command line may read today's date.

## Git

- Commit and push after every step, with a message that names the step,
  for example `Step 1: count subscribers by group`.
- Before committing, show me `git status` and the files you are about to add.
  Never commit `.env`, `outbox/`, or `.venv/`.

## How I learn

- I am new to Python. I am working through Part III of *The AI Agent Factory*:
  https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/
- **I have completed up to lesson 13.10.** I update this number as I learn.
  When I say "I have now completed up to X", change only this number.
- Write code only with what I have learned up to that lesson. If something
  new would really help, stop and tell me its name in one line. I decide.
- When the code uses something I have not seen before, show me that piece
  first and ask me to predict what it does. Stay quiet while I guess. Then run
  it, and explain a line only when I ask.
- I write my predictions in `notes/predictions.md` before each run. Never edit
  that file, and never show me an answer before I have written my prediction.
- Keep each change small: one step, one idea. If a request would need more than
  one new idea, stop and tell me how you would split it.

## Behaviors

<!-- One rule is added here per step of the lab. Newest at the bottom. -->

- Behaviors first: I give the expected answers, you write them as checks, show
  them failing, then write the code.
- When something breaks, show me the full error before changing anything.
