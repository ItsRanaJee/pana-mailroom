# Mailroom Lab: upgraded prompts

The upgraded version of every prompt in [mailroom-lab.md](mailroom-lab.md),
written for **this** project: Python 3.14, uv, Windows, and the practice files
in [practice-files/](practice-files/).

## How to use this file

1. **Write your own prompt first.** The lab's method (PRIMM-AI+) only works if
   you predict and write before you look. Open the prompt here *after*, to
   compare, the way the lab's "Show a sample prompt" works.
2. **🟨 marks your decisions.** Every 🟨 value is an answer you are meant to
   decide yourself. The value shown matches the generated practice files, so
   it is a correct answer, but replace it if yours differs and you can argue why.
3. **🟥 Break-it prompts are pasted exactly.** They are kept word for word from
   the lab, because they break something on purpose and the step depends on it.
4. **Check prompts run in a fresh session** (`/exit`, then `claude`, then paste).

### What "upgraded" means here

Each Make prompt follows the same shape, so Claude has less room to guess:

| Part | What it does |
| --- | --- |
| **Level** | Your lesson number, so Claude only uses what you have learned. |
| **Goal** | One sentence: the behavior, seen from the command line. |
| **Cases first** | Your expected answers, written as tests that fail before any code. Edge cases are included. |
| **Constraints** | What must not happen, such as no `today()` in the logic, or no request in tests. |
| **Done when** | Commands that prove it, which Claude runs and pastes. |
| **Rule** | The line AGENTS.md gains, under *Behaviors*. |

Each Check prompt also gets the same stricter footer:

- read-only: scratch files go in a temp folder **outside** the project and are deleted after
- every row of the table shows the **command it ran** and the **real output**, not a summary
- if something fails: show the full error and stop, with no fixing

Under each step, **Why upgraded** lists what the new version catches that the
original could miss.

> **Windows note.** Python on this machine prints through code page 1252 when
> output is piped, so `print("👍🏽")` crashes with `UnicodeEncodeError`.
> Step 7 deals with it. Until then, avoid emoji in printed output.

---

## Step 0 · The base *(already done for you)*

This is the prompt that set up the project you have now. Read it to compare
with what you would have written.

```
Set up a Python project called mailroom in this folder with uv, pinned to Python 3.14 (the latest stable release).
Write AGENTS.md with these rules, and a CLAUDE.md whose only line is @AGENTS.md:
- Scope: this file is the only source of rules here. CLAUDE.md files in parent folders do not apply.
- Mailroom is a command-line tool for one newsletter, Kettlebird Tea's Steep Club. It reads the subscribers, checks an issue, and sends it to a practice mail server. It never sends real email.
- Use uv for everything. Never pip. Add a dependency only when a step needs it, and name it first. Open text files with encoding="utf-8".
- Never use a real person's email address. Use @example.com, and @resend.dev for practice sends. No secrets in code or commits.
- Commit and push after every step, with the step in the message. Show me git status before committing. Never force-push.
Add a section "How I learn":
- I am new to Python. I have completed up to 13.7 of https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/ and I update this number as I learn.
- Write only with what I have learned. If something new would really help, stop and name it in one line. I decide.
- When the code uses something new, show me that piece first and ask me to predict it. Stay quiet while I guess. Then run it, and explain a line only when I ask.
- I write predictions in notes/predictions.md before each run. Never edit that file.
- One step, one idea. If a request needs two new ideas, stop and tell me how to split it.
Add an empty "Behaviors" section for the rules each step adds.
Extend .gitignore with .env, outbox/ and tool caches. Create notes/predictions.md.
Then make the first commit and push to a new public GitHub repository called pana-mailroom.
Done when: uv run python --version prints 3.14, git log shows one commit, and gh repo view shows the repository as public.
```

**Why upgraded:** a Python version pinned to the latest stable, not "3.12 or newer"
· parent-folder CLAUDE.md files (your n8n and WordPress rules) are switched off
here · no pip · secrets and force-push are ruled out from the first minute
· "show git status first" stops a stray `.env` from being committed.

**Check** *(fresh session)*

```
Check my base project. Read-only: don't change, create or commit any project files.
1. Without opening any file, list the rules you follow here and name the file each came from. Say whether any rules from a parent folder apply.
2. Run uv run python --version, git log --oneline, git remote -v and git status.
3. Run gh repo view --json url,visibility.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why the rules live in a file, and why we push from the first step.
```

---

# Part A · Read and check (Chapter 13)

## Step 1 · Count your subscribers *(13.8)*

**Before:** copy `lab/practice-files/subscribers.csv` to `data/subscribers.csv`.

```
I have now completed up to 13.8. Update How I learn in AGENTS.md.

Goal: uv run mailroom.py subscribers prints the total number of subscribers in data/subscribers.csv, then one line per group, groups in alphabetical order.
Cases first. Write my expected answers as assert lines in checks.py that call functions in mailroom.py, run it, and show me it failing before you write the code:
- total: 🟨 24
- per group: 🟨 cafe-partners 8, gift-buyers 8, monthly-box 8
- a file with only the header row: total 0
Constraints:
- Read the CSV with the csv module, by column name, opening it with encoding="utf-8" and newline="".
- Functions take the file path as an argument. Nothing is fixed to data/subscribers.csv except the default in the command.
- A blank line at the end of the file must not count as a subscriber.
Done when: python checks.py failed first, now passes, and uv run mailroom.py subscribers prints the numbers above.
Add to AGENTS.md under Behaviors: behaviors first. I give the expected answers, you write them as checks, show them failing, then write the code.
Commit and push.
```

**Why upgraded:** an empty-file case catches an off-by-one on the header ·
`newline=""` is what the csv docs ask for · group order is fixed, so output
can be compared · the path is passed in, so the 6-row check works.

**Modify:** "Add a line for how many gave consent. 🟨 Expected: 24. Check first."

**Check** *(fresh session)*

```
Test my subscriber count. Read-only: don't change any project files. Scratch files go in a temp folder outside the project, deleted after.
1. Run uv run python checks.py and uv run mailroom.py subscribers.
2. Count the rows and the groups in data/subscribers.csv yourself with a one-off command that does not import Mailroom's code. Do the numbers agree?
3. Make a copy with only 6 rows outside the project, and run the count on it. Does it say 6?
4. Make a copy that ends with two blank lines. Does the total stay 24?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why I wrote the expected numbers before the code.
```

---

## Step 2 · Who is new, and when do we send? *(13.9)*

```
I have now completed up to 13.9. Update How I learn in AGENTS.md.

Goal: two commands.
- subscribers --since-days N prints how many joined in the last N days.
- next-send prints the date of the next send: the first Monday of the month after the run date.
Both take an optional --run-date YYYY-MM-DD. Without it, the command line uses today's date.
Cases first, as checks that fail before the code:
- run date 2026-11-20, 30 days: 🟨 7. The window includes both ends: 🟨 2026-10-21 counts, 2026-10-20 does not, and 2026-11-20 counts.
- next send for 2026-11-20: 🟨 2026-12-07
- next send for 2026-12-07 (already a first Monday): 🟨 2027-01-04
- next send for 2026-12-31 (crosses the year): 🟨 2027-01-04
Constraints:
- Turn joined_on into a date with date.fromisoformat before comparing. Never compare dates as text.
- Only the command-line code may read today's date. Every other function takes the run date as an argument.
Done when: the checks failed first, now pass, and both commands print the dates above with --run-date.
Add to AGENTS.md under Behaviors: never read today's date inside the logic. Pass the run date in.
Commit and push.
```

**Why upgraded:** both edges of the window are named (the original named one) ·
a year-crossing case catches `month + 1 = 13` · "already a first Monday" was
in the original, but now it is explicit why it is a case · text comparison is
ruled out.

**Modify:** "Add --since 2026-10-01, an exact start date instead of a number of days. 🟨 Expected for run date 2026-11-20: ___. Check first."

**Check** *(fresh session)*

```
Test the dates in Mailroom. Read-only: don't change any project files.
1. Run uv run python checks.py.
2. With Python's datetime only, not Mailroom's code, work out the first Monday of the next month for 2026-11-20, 2026-12-07 and 2026-12-31. Compare with uv run mailroom.py next-send --run-date for each.
3. Count who joined from 2026-10-21 to 2026-11-20 inclusive with a one-off command, and compare with Mailroom.
4. Search the code for every call to date.today, datetime.now or datetime.today. How many places, and in which function?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why the run date is passed in.
```

---

## Step 3 · The 30th of February *(13.10)*

🟥 **Break it** (paste exactly)

```
In data/subscribers.csv, change Jonas Berg's joined_on to 2026-02-30, as if someone retyped it by hand.
Then run uv run mailroom.py subscribers --since-days 30 --run-date 2026-11-20.
Don't fix or explain anything. Show me the full error, exactly as printed.
```

Read it yourself, bottom up, before the next prompt.

**Then, after you have read it**

```
Explain the error in three lines: what happened, which function in mailroom.py raised it, and why.
Then fix the data, not the code: restore data/subscribers.csv from git with git restore, and show me git diff is empty for that file. Run the checks again.
Don't change any .py file in this step.
Add to AGENTS.md under Behaviors: when something breaks, show me the full error before changing anything.
Commit and push.
```

**Why upgraded:** names the exact git command, so Claude cannot "fix" the date
by guessing one · proves the restore with an empty diff · forbids code changes,
which the original only implied.

**Check** *(fresh session)*

```
Check my fix. Read-only: don't change any project files.
1. With a one-off command, check every joined_on in data/subscribers.csv: is each one a real calendar date? List any that are not.
2. Run uv run python checks.py and uv run mailroom.py subscribers.
3. Run git status and git log -1 --stat. Is the data the same as git had, and is the new rule committed?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about where to start reading a Python error.
```

---

## Step 4 · Real tests *(13.11)*

**Prediction to write first:** how many tests after the move? 🟨 one per assert-behavior in checks.py.

```
I have now completed up to 13.11. Update How I learn in AGENTS.md.

Goal: move checks.py into pytest, without changing a single expected answer.
- Add pytest as a dev dependency with uv add --dev pytest.
- Put the tests in tests/test_mailroom.py. One test per behavior, named test_<what it proves>, for example test_window_includes_first_day.
- Make the tests use a small CSV they write themselves in pytest's tmp_path where a test needs a special file (the header-only file). Leave the real data file for the tests about it.
- Before deleting checks.py, show me a table: old assert | new test name | same expected answer (yes or no).
Then delete checks.py, run uv run pytest -v, and paste the output.
Update AGENTS.md: the checks are now tests in tests/, run with uv run pytest.
Commit and push.
```

**Why upgraded:** the mapping table proves nothing was lost or changed ·
`tmp_path` stops tests from editing real data · the naming pattern is given, so
the test list reads like a spec · pytest goes in **dev** dependencies only.

**Check** *(fresh session)*

```
Check the tests. Read-only: don't change any project files.
1. Run uv run pytest -v.
2. Compare the tests with git show HEAD~1:checks.py. Is every old assert still tested, with the same expected answer? List any that are missing or changed.
3. Is pytest a dev dependency in pyproject.toml, not a main one?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why one test per behavior.
```

---

## Step 5 · Is this subject line OK? *(13.11)*

**Before:** copy `lab/practice-files/issue-01.md` to `issues/issue-01.md` and
`lab/practice-files/email-rules.md` to `docs/email-rules.md`. Ask Claude to commit them.

```
I have now completed up to 13.11. Update How I learn in AGENTS.md.

Goal: check_subject(issue_text) returns a list of problems. An empty list means the subject is fine. It follows rule 1 in docs/email-rules.md.
Tests first. My cases, each with its answer:
- 🟨 "The Steep Club opens Monday": no problems
- 🟨 "Your Steep Club box ships on Monday with new teas." (exactly 50 characters): no problems
- 🟨 "Your Steep Club box ships on Monday with fresh teas" (51 characters): one problem, too long
- 🟨 an empty subject: one problem, empty
- 🟨 a subject of only spaces: one problem, empty
- 🟨 no Subject line at all: one problem, missing
- 🟨 issues/issue-01.md: no problems
In each test, assert the length of my string first (for example assert len(subject) == 50), so a typo in the test itself is caught.
Each problem is a short sentence a person can act on, and the too-long one says the actual length, for example "Subject is 51 characters; the limit is 50."
Keep 50 in one named constant, SUBJECT_MAX = 50, used everywhere.
Show the tests failing first. Then make them pass, and never change my answers. If you think one is wrong, stop and tell me.
Add to AGENTS.md under Behaviors: I decide the test cases and their answers. Never change an expected answer to make a test pass.
Commit and push.
```

**Why upgraded:** asserting the string's length catches a miscounted test case
(the most common bug in this step) · the real issue is a case too · one
constant, not two copies of 50 · problems say *how far* off, which a person can fix.

**Check** *(fresh session)*

```
Test my tests. Read-only: don't change any project files.
1. Run uv run pytest -v.
2. Read git log -p for the subject tests. Did any expected answer change after check_subject was first written?
3. Copy the project to a temp folder outside it. In the copy, make check_subject always return an empty list, run the tests there, and count the failures. Then delete the copy.
4. Search for the number 50 in the code. How many places hold it?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about who owns the expected answers, and what green does not prove.
```

---

## Step 6 · The rest of the rules *(13.11)*

```
I have now completed up to 13.11.

Goal: check the other four rules in docs/email-rules.md, then add a check command for a whole issue.
Tests first, my cases:
- 🟨 issues/issue-01.md: no problems
- 🟨 a preview of 91 characters: one problem (limit 90)
- 🟨 a preview of exactly 90 characters: no problems
- 🟨 no Preview line: one problem
- 🟨 no {{first_name}} in the body: one problem
- 🟨 two links: one problem. A link starting http:// still counts.
- 🟨 no links at all: one problem
- 🟨 {{unsubscribe_url}} alone is not a link
- 🟨 no footer and no greeting: two problems, both listed
Then add uv run mailroom.py check <issue file>:
- prints every problem on its own line and exits 1
- or prints OK and exits 0
- a file that does not exist prints one plain sentence and exits 2
Keep each limit in a named constant next to SUBJECT_MAX.
Before writing code, list in one short block every assumption you are making that docs/email-rules.md does not state. I will decide each one.
```

**Why upgraded:** boundary cases (90 exactly, no links, no Preview) · the
"assumptions first" line turns the lab's Investigate question into a gate,
*before* the code bakes them in · exit code 2 for a missing file now, so
step 13 builds on it instead of changing it.

**Modify:** "Show the line number beside each problem. Check first."

**Check** *(fresh session)*

```
Test the issue checks. Read-only: don't change any project files. Scratch files go in a temp folder outside the project, deleted after.
1. Run uv run pytest -v, and uv run mailroom.py check issues/issue-01.md. Show the exit code.
2. Make three broken copies of the issue: a 91-character preview, two links, no footer. Run the check on each. Does each get exactly its own problem, and exit 1?
3. Run the check on a file that does not exist. Show the output and the exit code.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what the check assumed that the rules file does not say.
```

---

## Step 7 · How long is an emoji? *(13.12)*

**Ask first**

```
I have now completed up to 13.12. Update How I learn in AGENTS.md.
How long is the subject "👍🏽 Thanks for joining"? Give your answer, then prove it in Python with len() and by listing each character's code point. Tell me the ways our check could count length, and what each one would say for this subject. Don't change any files.
```

**Then your decision**

```
Decision: 🟨 count length as what Python's len() counts.
Add a test with "👍🏽 Thanks for joining" that proves it: assert its len() is 21, and that check_subject gives no problems.
Add a second test with a 49-character subject plus one 👍🏽, which is 51 by len(), and must get one problem.
Also: this is Windows, and printing an emoji through a pipe crashes with UnicodeEncodeError. Make the command line set its output to UTF-8 at the start, so check can print any subject. Show me it working with uv run mailroom.py check on a copy of the issue whose subject has the emoji, piped through more.
Add to AGENTS.md under Behaviors: subject and preview length count what Python's len() counts.
Commit and push.
```

**Why upgraded:** the original test would pass even if length were never
checked. The second test fails unless the emoji is counted as 2 · the
Windows crash is real on this machine (`cp1252` cannot encode 👍🏽), so it is
fixed here, where emoji first appear.

**Check** *(fresh session)*

```
Check the emoji decision. Read-only: don't change any project files.
1. Read AGENTS.md: what does a character mean in this project?
2. Run uv run pytest -v. Which test proves the code follows that decision? Would it still pass if the length check were deleted?
3. Run the check on a temp copy of the issue whose subject starts with 👍🏽, piped through more. Does it print without crashing?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why the emoji question was mine to decide.
```

---

# Part B · Shape the code (Chapter 14)

## Step 8 · One file per job *(14.1)*

```
I have now completed up to 14.1. Update How I learn in AGENTS.md.

Goal: turn Mailroom into a package under src/mailroom, with the same behavior.
- Modules, one job each: subscribers.py (reading subscribers), dates.py (run dates and send dates), issue.py (reading an issue), rules.py (the checks), cli.py (the commands).
- Add [project.scripts] mailroom = "mailroom.cli:main" and a build backend, so uv run mailroom works.
- Delete mailroom.py and the unused main.py.
Before moving anything, save the output and exit code of every command (subscribers, --since-days, next-send, check on the good issue and a broken copy) to a temp folder outside the project. After the move, run them again as uv run mailroom and show me both side by side. They must be identical.
Move code only: no behavior changes. In the tests, only the import lines may change. Show me git diff --stat for tests/ to prove it.
Add to AGENTS.md under Behaviors: one module per job. Only cli.py prints or reads today's date.
Commit and push.
```

**Why upgraded:** a before-and-after snapshot of every command proves "no
behavior change" instead of claiming it · module names are given, so you can
predict where each function lands · the rule now covers *today's date* too,
which also belongs only in cli.py.

**Modify:** "Is dates.py really one job? Decide, and say why."

**Check** *(fresh session)*

```
Check the package. Read-only: don't change any project files.
1. Run uv run pytest -v and every mailroom command.
2. Check out the commit before the move into a temporary git worktree outside the project. Run the same commands there as uv run mailroom.py, and compare output and exit codes. Then remove the worktree.
3. Search for print( and for date.today or datetime.now outside cli.py.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why each module has one job.
```

---

## Step 9 · A date that was really text *(14.2)*

🟥 **Break it** (paste exactly)

```
Add a test that calls the 30-day function with the run date as the text "2026-11-20". Run it, and show me exactly what happens.
```

**Then**

```
I have now completed up to 14.2. Update How I learn in AGENTS.md.
Add pyright as a dev dependency, and set it to strict mode in pyproject.toml under [tool.pyright], with pythonVersion = "3.14" and include = ["src", "tests"].
Add type hints to every function and every parameter, including tests. Run uv run pyright and show me everything it finds, before fixing anything.
Fix the call, not the hint: the test that passed text becomes a test that passes a date. Never use Any, cast, or # type: ignore to make pyright quiet. If one seems needed, stop and tell me why.
Done when: uv run pyright reports 0 errors and uv run pytest passes.
Add to AGENTS.md under Behaviors: every function has type hints, and pyright in strict mode must be clean. No Any, cast or type: ignore.
Commit and push.
```

**Why upgraded:** strict mode is what the book uses, and basic mode lets
untyped functions through · the "show before fixing" line keeps the lesson
visible · the three ways to silence pyright are named and ruled out.

**Check** *(fresh session)*

```
Check the types. Read-only: don't change any project files.
1. Run uv run pyright and uv run pytest.
2. Is pyright in strict mode in pyproject.toml?
3. Search for Any, cast(, and type: ignore. Find any function without full type hints.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what a type checker catches and what it cannot.
```

---

## Step 10 · A subscriber is a thing *(14.3)*

```
I have now completed up to 14.3. Update How I learn in AGENTS.md.

Goal: rows and issue text stop travelling around raw.
- Subscriber is a frozen dataclass with email, first_name, last_name, group and joined_on (a date).
- Issue is a class made from the issue file's text, with subject, preview, body, links (a property) and personalize(first_name) -> str.
- Use them everywhere. Only the code that reads the CSV touches column names in quotes.
Tests first:
- 🟨 issues/issue-01.md has exactly one link, https://kettlebird.example/steep-club
- 🟨 personalize("Ayesha") puts Ayesha where {{first_name}} was, and leaves {{unsubscribe_url}} and {{company_address}} as they are
- 🟨 the first subscriber is Ayesha Khan, ayesha.khan@example.com, joined_on is a date and not text
- 🟨 personalize does not change the Issue it was called on
All earlier tests still pass with the same answers, and pyright stays clean.
Add to AGENTS.md under Behaviors: pass Subscriber and Issue objects around, never raw rows or raw text.
Commit and push.
```

**Why upgraded:** `frozen=True` stops code from changing a subscriber by
accident · a test that `personalize` returns a new text and leaves the Issue
alone catches a common mutation bug · `joined_on` is checked as a real date.

**Check** *(fresh session)*

```
Check the classes. Read-only: don't change any project files.
1. Run uv run pytest and uv run pyright.
2. Search for row["...] style access outside the code that reads the CSV.
3. In uv run python, make one Subscriber and one Issue from the files, print both, call personalize("Ayesha") and print the first five lines, then print the Issue's subject again to show it did not change.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what a class gives us that a dictionary does not.
```

---

## Step 11 · Marketing sent a messy file *(14.4)*

**Before:** copy `lab/practice-files/new-signups.csv` to `data/new-signups.csv`.

```
I have now completed up to 14.4. Update How I learn in AGENTS.md.

Goal: Subscriber becomes a Pydantic model that checks each field's shape, and mailroom import <file> reports each row.
- Add pydantic with its email extra: uv add "pydantic[email]".
- The model: email is an EmailStr. group is one of exactly three values, 🟨 monthly-box, gift-buyers, cafe-partners, as a Literal. joined_on is a date. consent is text that is not empty after trimming spaces.
- mailroom import <file> prints one line per row: the row number as it appears in the file (header is row 1), the email, and accepted or rejected with the reason in plain words, not Pydantic's raw error dump.
Tests first, from my predictions for data/new-signups.csv:
- 🟨 accepted: Maria, Sara, Tom, Ines
- 🟨 rejected: Omar (email), Lena (group), Kofi (date), Hana (consent). Assert the field that failed, not just "rejected".
All earlier tests and pyright stay clean.
Add to AGENTS.md under Behaviors: data from outside goes through the model before any code uses it.
Commit and push.
```

**Why upgraded:** the email extra is named, because `EmailStr` fails at import
without it · each rejection test asserts *which field* failed, so a row
rejected for the wrong reason fails the test · row numbers match what you see
in a spreadsheet.

**Modify:** "Should 'Gift Buyers' be turned into gift-buyers before the check? 🟨 Decide, and say why in one line."

**Check** *(fresh session)*

```
Test the import. Read-only: don't change any project files.
1. Run uv run mailroom import data/new-signups.csv. Which rows are accepted?
2. For each rejected row, open the raw line in the CSV. Is the reason printed the real problem with that row?
3. Run uv run pytest and uv run pyright.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what the model checks.
```

---

## Step 12 · What the model let through *(14.5)*

```
I have now completed up to 14.5. Update How I learn in AGENTS.md.

Two accepted rows are still wrong for us:
- Sara is not at an allowed domain. Allowed domains: 🟨 example.com only for subscribers. Compare the domain exactly and ignoring case: x@EXAMPLE.com is allowed, x@notexample.com and x@example.com.evil.io are not.
- Tom joined after the run date.
Add our own rules for both, as functions outside the model, tests first, including the three domain cases above. import takes --run-date like the other commands.
Before writing code, tell me in two lines why the run-date rule cannot live inside the model.
Done when: 🟨 only Maria and Ines are accepted with --run-date 2026-11-20, and pytest and pyright are clean.
Add to AGENTS.md under Behaviors: the model checks the shape. Our own rules check the meaning.
Commit and push.
```

**Why upgraded:** "ends with example.com" is the classic hole, so
`notexample.com` and `example.com.evil.io` are cases · case-insensitive domain
matching is decided, not left to chance.

**Check** *(fresh session)*

```
Test our own rules. Read-only: don't change any project files. Scratch files go in a temp folder outside the project, deleted after.
1. Run uv run mailroom import data/new-signups.csv --run-date 2026-11-20. Which rows are accepted now?
2. Import a temp copy with three extra rows: someone@example.org, someone@notexample.com and SOMEONE@EXAMPLE.COM. Which are accepted?
3. Run uv run pytest and uv run pyright.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about the difference between a field's shape and its meaning.
```

---

## Step 13 · One bad row, 999 good ones *(14.6)*

```
I have now completed up to 14.6. Update How I learn in AGENTS.md.

Goal: bad data becomes a report, not a crash.
My sorting:
- 🟨 stop everything, exit 2, one plain sentence, no traceback: the file does not exist, the file is missing a required column, the file is empty or not UTF-8
- 🟨 report and carry on, exit 1 if any: a bad date in a row, a disallowed domain, an unknown group, a joined_on after the run date, an issue that breaks a rule
Reading subscribers returns two things: the good Subscriber objects and a list of problems. Each problem has the row number, the field and a plain message.
Commands print every problem, then a one-line summary such as "2 accepted, 6 rejected", and exit 1 if there is any problem, else 0.
Tests first:
- 🟨 data/new-signups.csv with run date 2026-11-20: 2 good subscribers, 6 problems, each with its row and field
- 🟨 a missing file: exit 2, one sentence, and the word Traceback does not appear in the output
- 🟨 a file whose joined_on column is named joined: exit 2, naming the missing column
- 🟨 data/subscribers.csv: 24 good, 0 problems, exit 0
Only catch the exceptions you expect, by name. No bare except, and no except Exception.
Add to AGENTS.md under Behaviors: report every problem with its row and field. No traceback for a user's mistake. Exit 0 for OK, 1 for problems in the data, 2 for a problem that stops the run.
Commit and push.
```

**Why upgraded:** the three exit codes are written into AGENTS.md as a
contract, because hooks (step 25) and CI (step 21) read them · "no Traceback"
is tested, not just asked for · bare `except` is ruled out · the
renamed-column case from step 3's Modify becomes a test.

**Modify:** "Add --strict, which stops at the first problem with exit 1. Test first."

**Check** *(fresh session)*

```
Test the errors. Read-only: don't change any project files.
1. Run uv run mailroom import data/new-signups.csv --run-date 2026-11-20, then show the exit code.
2. Run it on a file that does not exist, and show the output and exit code.
3. Search the code for every except. For each one, say what it catches, and flag any bare except, except Exception, or except that hides the error with pass.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about which errors should stop a program.
```

---

# Part C · Talk to a service (Chapter 14)

Start the practice mail server in a second terminal before step 15, and leave it running:

```powershell
npx emulate@0.12.3 start --service resend
```

## Step 14 · See the send before it happens *(14.7)*

```
I have now completed up to 14.7. Update How I learn in AGENTS.md.

Goal: mailroom send <issue> --dry-run --run-date 2026-12-07 writes the send plan to outbox/plan.json and sends nothing.
- It runs the issue check first. If the check finds a problem, it prints the problems, writes no plan, and exits 1.
- It reads subscribers through the model and our rules. Rejected rows are reported and left out of the plan.
- The plan is a JSON object: run_date as an ISO text "2026-12-07", issue as the file path, and emails, a list with one entry per subscriber: to, subject, text.
- Every placeholder is filled: {{first_name}}, 🟨 {{company_address}} = 12 Leaf Lane, Portland, OR 97201, 🟨 {{unsubscribe_url}} = https://kettlebird.example/unsubscribe. Keep those two values in one settings place, not inside the send code.
- After filling, if any {{ is left in the text, stop with exit 2 and name the placeholder.
- Write the file with encoding="utf-8", indent=2 and ensure_ascii=False.
- outbox/ is already in .gitignore. Confirm it.
Tests first, using tmp_path for the outbox:
- 🟨 24 entries, the first to ayesha.khan@example.com with a text containing "Hi Ayesha,"
- 🟨 an issue that fails the check writes no plan
- 🟨 an issue with an unknown placeholder {{coupon}} stops with exit 2
Add to AGENTS.md under Behaviors: look before you send. Every send can be dry-run, and no placeholder is ever sent unfilled.
Commit and push.
```

**Why upgraded:** an unfilled-placeholder guard, because "Hi {{first_name}}"
reaching a reader is the most visible mistake a newsletter can make · company
details live in one place · `ensure_ascii=False` keeps emoji readable in the
file · tests never write to the real outbox/.

**Modify:** "Edit one subject in plan.json to 60 characters. Add --from-plan, which reads the plan back through a Pydantic model and runs the rules again. 🟨 Expected: your edit is caught with exit 1."
**Rule it adds:** JSON read from a file is outside data: it goes through a model too.

**Check** *(fresh session)*

```
Test the dry run. Read-only: don't change any project files except outbox/, which is not tracked.
1. Run uv run mailroom send issues/issue-01.md --dry-run --run-date 2026-12-07, and check outbox/plan.json with uv run python -m json.tool.
2. Count its entries with a one-off command, and compare with the number of subscribers.
3. Search the plan for any {{ left unfilled.
4. Run git status. Is outbox/ untracked and ignored?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why JSON from a file needs checking again.
```

---

## Step 15 · Send one email *(14.7)*

**Before:** the practice server is running and shows `http://localhost:4000`.

```
I have now completed up to 14.7.

Goal: send one email to the practice server with httpx, and read it back.
- uv add httpx. POST {RESEND_API_URL}/emails with JSON: from onboarding@resend.dev, to (a list), subject, text. The key goes in the header Authorization: Bearer <key>.
- Read RESEND_API_URL and RESEND_API_KEY from the environment in cli.py only, defaulting to 🟨 http://localhost:4000 and re_practice. Pass them into the send code as arguments.
- Set an explicit timeout of 🟨 10 seconds on the client.
Two guards, both checked before any request is built:
- Host guard: parse the URL and allow only the hosts localhost, 127.0.0.1 and ::1, over http. Tests: http://localhost:4000 and http://127.0.0.1:4000 allowed. https://api.resend.com, http://localhost.evil.io and http://evil.io/?localhost refused.
- Recipient guard: allow only addresses whose domain is exactly example.com or resend.dev, ignoring case. Tests: delivered@resend.dev and DELIVERED@Resend.Dev allowed. sara.ali@gmail.com, x@notresend.dev and x@resend.dev.evil.io refused. Put this rule in one function; step 25 reuses it.
Add mailroom send-one <issue> --to delivered@resend.dev: prints the status code and the id, then GETs /emails/{id} and prints its status.
Tests must never touch the network: use httpx.MockTransport, and add a test that proves a refused recipient makes zero requests.
Never print the key, not even in an error.
Add to AGENTS.md under Behaviors: the key and the address come from the environment, read only in cli.py. Sending works only against localhost, and only to @example.com and @resend.dev.
Commit and push.
```

**Why upgraded:** a substring check like `"localhost" in url` lets
`localhost.evil.io` through, so the guard parses the host and the tests prove
it · the same hole in the recipient check is closed · "zero requests" is
tested, not trusted · an explicit timeout · the key is never printed.

**Check** *(fresh session)*

```
Test sending. Read-only: don't change any project files. The practice server is running on http://localhost:4000.
1. Run uv run mailroom send-one issues/issue-01.md --to delivered@resend.dev, then list the server's emails with curl -s http://localhost:4000/emails. Is it there?
2. Try --to sara.ali@gmail.com. Is it refused, with a plain message?
3. Run it with RESEND_API_URL=https://api.resend.com, then with RESEND_API_URL=http://localhost.evil.io. Is each refused before any request?
4. Search the output of all the runs above for re_practice. Is the key ever printed?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about where the key comes from, and why.
```

---

## Step 16 · When the server says no *(14.7)*

🟥 **Break it** (paste exactly)

```
Show me the status code and body the server sends for: a request without a subject, and GET /emails/does-not-exist. Then I will stop the server: show me what happens then.
```

Stop the server with Ctrl+C, then tell Claude "I stopped the server. Show me what happens now." Start it again before the next prompt.

**Then**

```
Handle each failure on purpose, tests first, all with httpx.MockTransport:
- 🟨 422: show the server's message field, exit 1, never retried
- 🟨 404 on GET: say the email id is unknown, exit 1
- 🟨 401 or 403: say the key was refused, and never print the key, exit 2
- 🟨 no connection: say the practice server is not running, show the exact command to start it (npx emulate@0.12.3 start --service resend), exit 2
- 🟨 timeout: say the server did not answer in time, exit 2
- 🟨 any other status: show the status code and the first 200 characters of the body, exit 1
Every test also asserts how many requests were made, so "never retried" is proven.
Add to AGENTS.md under Behaviors: handle each status on purpose. Never retry a 4xx.
Commit and push.
```

**Why upgraded:** 401/403, timeouts and unknown statuses are handled now, not
discovered later · the request count turns "never retried" into a test.

**Check** *(fresh session)*

```
Test the failures. Read-only: don't change any project files. The practice server is running.
1. Make Mailroom send without a subject, and fetch an unknown id. What does each print, and what exit code?
2. Point RESEND_API_URL at http://localhost:4999, where nothing runs. What does it print, and what exit code?
3. Search the output for "Traceback". Is there any?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about which failures are worth retrying.
```

---

## Step 17 · Twenty-four at once, five at a time *(14.8)*

**Prediction:** 🟨 24 × 0.3 s ≈ 7.2 s one by one · 5 waves of up to 5 ≈ 1.5 s at five at a time.

```
I have now completed up to 14.8. Update How I learn in AGENTS.md.

Goal: send the whole plan.
- mailroom send <issue> --run-date 2026-12-07 --latency 0.3 builds the plan as the dry run does, sends it one by one, waits the latency before each request, and prints the total time.
- Then add --at-once N: the same send with asyncio and httpx.AsyncClient, with an asyncio.Semaphore of N, results kept in the plan's order. --at-once must be between 1 and 🟨 10, else exit 2.
- One email failing does not stop the others. At the end, print how many were sent and how many failed, and exit 1 if any failed.
Tests first, with httpx.MockTransport and no real waiting:
- 🟨 results come back in the plan's order even when later requests finish first
- 🟨 never more than N requests are in flight at once: count them in the mock
- 🟨 one failing email out of 24: 23 sent, 1 failed, exit 1
Don't test wall-clock time in pytest. I check timing by hand.
Add to AGENTS.md under Behaviors: send with a limit on how many at once, keep the plan's order, and one failure never stops the rest.
Commit and push.
```

**Why upgraded:** timing tests are flaky, so the tests count concurrency
instead · `--at-once` has a ceiling, so a typo like `--at-once 1000` cannot
flood the server · one bad address no longer stops a whole send.

**Check** *(fresh session)*

```
Test sending at once. Read-only: don't change any project files. The practice server is running; restart it first so its list is empty.
1. Time the send one by one and with --at-once 5, both with --latency 0.3. Show both times.
2. List the server's emails with curl -s http://localhost:4000/emails. Did each subscriber get exactly one email per send? Count by recipient.
3. Try --at-once 0 and --at-once 500. Are both refused with exit 2?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why async helps when waiting, and why we limit it.
```

---

## Step 18 · The vendor's own library *(14.9)*

**Read the SDK**

```
I have now completed up to 14.9. Update How I learn in AGENTS.md.
Add the official resend package. Point it at the practice server with RESEND_API_URL and write the same single send with it, in a separate function. Show me the httpx version and the SDK version side by side.
Then, in the installed package's own source under .venv, show me with file paths and line numbers: where it builds the request, where an error status becomes an exception, its default timeout, and whether it retries. Quote the lines. If something is not there, say so and show where you looked.
Don't change the send command yet.
```

**Then**

```
Decision: Mailroom keeps 🟨 the httpx version, because ___. Remove the SDK and write the reason in AGENTS.md.
Add our own retry, tests first, with httpx.MockTransport and the waits replaced by a fake sleep:
- retry only after no connection, a timeout, a 429 or a 5xx. Never a 4xx other than 429.
- at most 3 tries in total, waiting 🟨 0.5, then 1 second. If a 429 has a Retry-After header, wait that long instead, capped at 🟨 10 seconds.
- each email has an Idempotency-Key header made from the issue file name and the recipient, the same on every try, for example a SHA-256 hash of "issue-01.md|ayesha.khan@example.com".
Tests: 🟨 a 503 then a 200 sends once and succeeds · a 422 is tried exactly once · three 503s give up after 3 tries · the key is the same on every try · two different recipients get different keys.
Prove it against the server: the same key twice gives one email, and the same key with another subject gets a 409.
Add to AGENTS.md under Behaviors: retry only what can succeed later, at most 3 tries, and every send has an idempotency key.
Commit and push.
```

**Why upgraded:** source lines are quoted, so "the SDK never retries" is
proven · `Retry-After` is honoured and capped · a fake sleep keeps tests fast ·
the key is made the same way every time, so a retry tomorrow does not send twice.

**Check** *(fresh session)*

```
Test the retries. Read-only: don't change any project files. The practice server is running.
1. Run uv run pytest and uv run pyright.
2. Read the retry code. List exactly which answers are retried. Is any 4xx other than 429?
3. Send one email twice with the same idempotency key, then list the server's emails. How many arrived? Send it once more with the same key and another subject. What status comes back?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what the SDK does for us, and what it leaves to us.
```

---

# Part D · Ship like a team (Chapter 15)

From here, nothing goes straight to main.

## Step 19 · Your first pull request *(15.1, 15.3)*

**Prediction:** 🟨 the files the report command will touch: ___

```
I have now completed up to 15.1. Update How I learn in AGENTS.md.

Goal: mailroom report, on a new branch called feature/report.
- The send also writes outbox/sent.json: one entry per email with id, recipient, group and status (sent or failed, with the reason).
- mailroom report reads outbox/sent.json through a Pydantic model and prints how many each group got, and every failure.
Tests first: 🟨 after a send to all 24, the report says 8 per group and no failures. 🟨 A sent.json with one failure lists it and exits 1. 🟨 A missing sent.json says "Nothing has been sent yet" and exits 2.
Run uv run pytest and uv run pyright. Then push the branch and open a pull request with gh pr create. The description has three headings: What changed, Why, How I tested it, with the real commands and their output.
Don't merge.
Add to AGENTS.md under Behaviors: every change goes on a branch and arrives as a pull request. Never commit to main. This replaces "commit and push after every step": now commit and push to the branch.
```

**Why upgraded:** the new rule says it *replaces* the old push-to-main rule,
so AGENTS.md doesn't hold two rules that disagree · the branch name is given ·
sent.json is read through a model, following step 14's rule.

**Then:** read *Files changed* on GitHub yourself. When you are happy: "Merge it with a merge commit, delete the branch, and pull main."

**Check** *(fresh session)*

```
Check my pull request. Read-only: don't change any files.
1. Run gh pr list --state all.
2. Read the report pull request with gh pr view. Does the description say what, why and how it was tested, with real output?
3. Run git log --oneline --graph -8 on main. Did the change come in through the merge? Is any commit on main that did not come from a pull request?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why changes go through pull requests.
```

---

## Step 20 · Evidence, not "done" *(15.4, 15.5)*

```
I have now completed up to 15.4. Update How I learn in AGENTS.md.

On a new branch, two changes:
1. Add .github/pull_request_template.md with these headings: What changed, Why, Evidence (the real output of uv run pytest, uv run pyright and uv run mailroom check on every issue, each in its own code block with the command on the first line), Risk (what could go wrong, and who it would affect).
2. A new rule, tests first: 🟨 the preview must not repeat the subject. Decide with me first: does "repeat" mean equal, equal ignoring case and spaces, or the preview starting with the subject? 🟨 ___
Run every command fresh, after the last change, and paste the real output, not a summary. If any command fails, stop and show me; don't open the pull request.
Open the pull request with the template filled in. Don't merge.
Add to AGENTS.md under Behaviors: a pull request shows its evidence: real output, run after the last change.
```

**Why upgraded:** "repeat" is ambiguous, so it becomes your decision · evidence
must be run *after the last change*, since output from before a fix proves nothing
· the Risk section asks who would be affected.

**Check** *(fresh session)*

```
Review my latest pull request. Read-only: don't change any files.
1. Read it with gh pr view and gh pr diff.
2. Check its branch out into a temporary git worktree outside the project, run uv sync, uv run pytest, uv run pyright and uv run mailroom check on every issue there, and compare with the evidence pasted. Do they match? Then remove the worktree.
3. Was the evidence run on the pull request's last commit? Compare the commit time with when the description was written, if you can tell.
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about the difference between evidence and a claim.
```

---

## Step 21 · Checks that block *(15.8)*

```
I have now completed up to 15.8. Update How I learn in AGENTS.md.

On a new branch, add .github/workflows/checks.yml, a GitHub Actions workflow named checks that runs on every pull request and on every push to main:
- ubuntu-latest, with the official astral-sh/setup-uv action pinned to its latest major version, reading Python from .python-version
- uv sync --locked, so a stale uv.lock fails the run
- uv run pytest, uv run pyright, and uv run mailroom check on every file in issues/, failing if any issue fails
- permissions: contents: read only. A timeout of 🟨 10 minutes.
Open it as a pull request. Wait for the run with gh pr checks --watch. When it passes, merge it.
Then protect main with gh api: require a pull request before merging, require the checks job to pass and the branch to be up to date, and apply the rules to admins too. Show me the protection that GitHub reports back.
Add to AGENTS.md under Behaviors: the checks must pass before a merge.
```

**Why upgraded:** `--locked` catches a lockfile someone forgot to update · the
workflow runs on main too, so main is never silently red · least-privilege
permissions · a timeout stops a hung run · "admins too" means you can't skip
it by accident.

🟥 **Break it** (paste exactly)

```
On a new branch, change only the issue's subject to "Your first Steep Club box ships Monday, and it is lovely". Don't run anything yourself. Push, open a pull request, and tell me what the checks say and whether GitHub allows the merge.
```

**Check** *(fresh session)*

```
Check the protection. Read-only: don't change any files.
1. Run gh api repos/{owner}/{repo}/branches/main/protection and say in plain words what it requires, including whether it applies to admins.
2. Find the pull request with the 56-character subject. Did its check fail? Quote the line in the log that says why.
3. Run gh run list --branch main --limit 3. Is main green?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why a check that blocks beats evidence pasted by hand.
```

---

## Step 22 · A reviewer that reads your rules *(15.6, 15.7)*

```
I have now completed up to 15.6. Update How I learn in AGENTS.md.

On a new branch, write REVIEW.md: what a reviewer checks in a Mailroom pull request.
- Take every rule from AGENTS.md. For each, say whether a test, pyright, the checks workflow or only a person can catch a break of it.
- Put the rules that only a person can catch first, each with one example of a break.
- End with what a reviewer must never approve: a changed expected answer in a test, a widened recipient or host guard, a secret, a new retry on a 4xx.
- Keep it under one page.
Add to AGENTS.md under Behaviors: reviewers read REVIEW.md.
Open it as a pull request with evidence. Don't merge.
```

**Then you do this yourself:** run `/install-github-app` in Claude Code and
follow its steps (it adds the API key as a repository secret). Then:

```
On a new branch, add a workflow that has Claude review every pull request against REVIEW.md, as lesson 15.7 shows. The review cites the REVIEW.md rule for each finding. Give it read access to the code and write access only to pull-request comments. Open it as a pull request with evidence.
```

**Why upgraded:** each rule is tagged with *who* can catch a break, which is
this step's whole lesson · a "never approve" list covers the changes that
would quietly undo the safety work · the review must cite the rule it uses.

**Check** *(fresh session)*

```
Check the review setup. Read-only: don't change any files.
1. Read REVIEW.md. Does each rule match one in AGENTS.md? List any rule in one file but not the other.
2. List the workflows in .github/workflows, what each runs, when, and with which permissions.
3. Find the latest pull request Claude reviewed. Does its review cite a REVIEW.md rule?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about what a reviewer adds to the checks.
```

---

## Step 23 · A person for risky changes *(15.9)*

**Prediction:** 🟨 the files that could do real harm: ___

```
I have now completed up to 15.9. Update How I learn in AGENTS.md.

On a new branch, add .github/CODEOWNERS so these need approval from 🟨 @classmate-github-name:
- the sending code, the recipient and host guards, and the retry code (name the real file paths)
- .github/ itself, so nobody can weaken the checks or CODEOWNERS without approval
Open it as a pull request with evidence, and merge it when the checks pass.
Then update main's protection: one approving review is required, it must come from a code owner, and a new push dismisses an old approval. Show me what GitHub reports back.
```

**Then:** add your classmate as a collaborator, and they add you. Open two small pull requests, one that changes the sending code and one that changes only an issue. Which one waits for your classmate?

> **Working alone?** GitHub does not let you approve your own pull request.
> Use a second GitHub account you own as the "classmate", or skip the
> protection change and keep only CODEOWNERS.

**Why upgraded:** `.github/` is owned too, because otherwise a pull request
could quietly delete CODEOWNERS · stale approvals are dismissed, so code
changed after approval is reviewed again.

**Check** *(fresh session)*

```
Check the approvals. Read-only: don't change any files.
1. Read .github/CODEOWNERS. Which files need whose approval? Does each path match a file that exists?
2. Read main's protection with gh api. Is a code owner's review required? Are stale approvals dismissed?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why not every change needs the same approval.
```

---

## Step 24 · After the merge *(15.10)*

```
I have now completed up to 15.10. Update How I learn in AGENTS.md.
Set the version in pyproject.toml to 1.0.0 through a pull request. When it is merged, tag main as v1.0 and create a GitHub release with gh release create, with notes made from the merged pull requests (--generate-notes).
```

🟥 **Break it** (paste exactly)

```
A bad change: on a branch, add issues/issue-02.md, a copy of issue-01 with its link changed from https:// to http://. Open a pull request and merge it when the checks pass. Then undo it with a revert, as its own pull request.
```

**Then make it impossible**

```
Tests first, as a pull request: the check requires every link to start with https://.
Decision: 🟨 an http:// link is a problem of its own. So an issue with two links, one of them http://, has two problems. If an older test disagrees, stop and show me the test and both answers; I decide.
Add a test that runs the check on the exact issue-02.md from the reverted pull request (take it from git history into a test fixture) and expects one problem.
Merge it when the checks pass, set the version to 1.0.1, and release v1.0.1.
Add to AGENTS.md under Behaviors: undo a bad merge with a revert pull request, then add the test that would have caught it.
```

**Why upgraded:** the version in pyproject.toml matches the tag ·
`--generate-notes` builds notes from the real pull requests · the regression
test uses the *actual* bad file, not a new example of it.

**Check** *(fresh session)*

```
Check the releases. Read-only: don't change any files.
1. Run gh release list, and compare each tag with the version in pyproject.toml at that tag.
2. Find the revert pull request and the https test. Does uv run pytest pass on main?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about how a bad merge is undone.
```

---

# Part E · Into your studio

## Step 25 · A guard for Claude Code

**Prediction:** 🟨 what the guard must read from the hook's JSON: ___

```
On a new branch, add mailroom guard. It reads one Claude Code hook event as JSON from standard input.
- The tool name is in tool_name and its arguments in tool_input. A tool counts as a send if the last part of its name, after the last "__", is 🟨 send-email or send-batch-emails. That covers MCP names like mcp__resend__send-email.
- For a send, collect every address in to, cc and bcc, whether each is a single text or a list, and for a batch, in every email of the batch. Accept the "Name <address>" form.
- Check each address with the same recipient rule function the send code uses. Do not copy it.
- If any address fails, print to standard error which address and why, and exit 2. Otherwise exit 0.
- Any other tool: exit 0, silently.
- Decision: 🟨 if the input is not valid JSON, or a send has no recipients at all, exit 2 (fail closed).
Also add --subscribers <file> to every command that reads subscribers.
Tests first:
- 🟨 send-email to sara.ali@gmail.com: exit 2, and the reason names sara.ali@gmail.com
- 🟨 send-email to delivered@resend.dev: exit 0
- 🟨 mcp__resend__send-email with bcc sara.ali@gmail.com: exit 2
- 🟨 send-batch-emails with one bad address in the third email: exit 2
- 🟨 a Read tool call: exit 0
- 🟨 not JSON: exit 2
Open it as a pull request with evidence, merge it when the checks pass, set the version to 1.1.0, and release v1.1.
```

**Why upgraded:** MCP tool names carry a prefix, so a plain name match would
let every real send through · `bcc` and batch emails are covered · bad input
fails *closed*, which is safer for a guard · the rule is imported, not copied,
which is the whole point of this step.

**Check** *(fresh session)*

```
Test the guard. Read-only: don't change any project files.
1. Pipe a sample hook JSON for send-email to sara.ali@gmail.com into uv run mailroom guard. Show the exit code and the message.
2. Do the same for delivered@resend.dev, and for mcp__resend__send-email with sara.ali@gmail.com in bcc.
3. Pipe the text "hello" into it. What exit code?
4. Search the code: how many places define the recipient rule?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about why one copy of a rule beats two.
```

---

## Step 26 · Mailroom guards the studio

**Before:** open Claude Code in your `my-email-studio` folder.

```
Install my Mailroom tool from my release: uv tool install git+https://github.com/ItsRanaJee/pana-mailroom@v1.1. Show me mailroom --help to prove it is on the PATH.
Add a PostToolUse hook for Write and Edit in .claude/settings.json. It reads the hook's JSON from standard input and takes tool_input.file_path. When the file is a Markdown email under campaigns/ (match with forward and back slashes, since this is Windows), it runs mailroom check on it. If the check exits 1, print its problems to standard error and exit 2 so you see them. If mailroom itself is missing, say so on standard error and exit 2.
Make .claude/hooks/send-guard.mjs pass the whole tool call to mailroom guard on standard input, and use its exit code and message as its answer. Remove the old copy of the recipient rule from the script.
Update CLAUDE.md: practice sends go only to @example.com and @resend.dev, and Mailroom's guard decides. Fixed rules are checked by Mailroom. Claude handles the judgment.
Show me the hook config and the diff, then commit.
```

**Why upgraded:** Windows paths use `\`, so a `campaigns/` match alone would
never fire here · a missing `mailroom` now blocks instead of silently passing ·
the old copy of the rule is removed, not left beside the new one.

**Check** *(fresh session in the studio)*

```
Test Mailroom inside this studio. Don't change files you did not make for this test.
1. Run mailroom --help.
2. Write a temporary email under campaigns/test/emails/ with a 56-character subject. Did the hook report it? Quote it. Then delete the file.
3. Run mailroom check on every email under campaigns/.
4. Pipe a send-email call to sara.ali@gmail.com into the send-guard script. What does it answer?
For each test, show the command and its real output. If something fails, show the full error and stop.
Give me a table: Test | Command | Pass or Fail | What you found.
Then ask me two quick questions, one at a time, about which rules belong in code and which in Claude's judgment.
```
