# My predictions

Write each prediction **before** the run. Never change it afterwards: if you
were wrong, add a line under "What happened" instead. Wrong guesses are the
most useful lines in this file.

---

## Step 0 · The base

**Newsletter name and who it is for:** Kettlebird Tea's Steep Club, a monthly tea-box club for home tea drinkers. *(Sample. Replace with your own if you like, and tell Claude to update AGENTS.md.)*

**Prediction:**

**What happened:**

---

## Step 1 · Count your subscribers

**Prediction:** total = 25· group counts = 3.

**What happened:**

---

## Step 2 · Who is new, and when do we send?

**Prediction:** None. I did not write one before the run. *(Recorded afterwards, so this is not a prediction.)*

**What happened:** With run date 2026-11-20, 3 subscribers joined in the last 30 days (Noah, Yuki, Sara). The next send is 2026-12-07, and after 2026-12-07 it is 2027-01-04.

---

## Step 3 · The 30th of February

**Prediction:** Yes, Mailroom will crash, because 2026-02-30 is not a real date (February never has 30 days).

**What happened:**

---

## Step 4 · Real tests

**Prediction:** 7 tests, one per behavior. *(Written after the run, so it is a record and not a true prediction.)*

**What happened:**

---

## Step 5 · Is this subject line OK?

**Prediction:** *(Drafted by Claude at my request, before any code exists. These are the cases I adopt as mine. I can edit any of them before the tests are written.)*

Rule 1: the subject is 50 characters or fewer. `check_subject(issue_text)` returns a list of problems, empty when the subject is fine.

| # | Subject | Length | Expected |
| --- | --- | --- | --- |
| 1 | `The Steep Club opens Monday` | 27 | no problems |
| 2 | `Your Steep Club box ships on Monday with new teas.` | 50 | no problems (the limit itself is allowed) |
| 3 | `Your Steep Club box ships on Monday with fresh teas` | 51 | one problem: too long |
| 4 | *(empty after `Subject:`)* | 0 | one problem: empty |
| 5 | *(spaces only)* | 0 after trimming | one problem: empty |
| 6 | *(no `Subject:` line at all)* | none | one problem: missing |

Also: `issues/issue-01.md` gives no problems.

**What happened:**

---

## Step 6 · The rest of the rules

**Prediction:** *(Drafted by Claude at my request, before any code exists, from the real `docs/email-rules.md`. I adopt these cases and can edit them.)*

`mailroom.py check <issue file>` prints every problem on its own line and exits 1, or prints `OK` and exits 0.

| Rule | Case | Expected |
| --- | --- | --- |
| 2 Preview | a preview of exactly 90 characters | no problems |
| 2 Preview | a preview of 91 characters | one problem: too long |
| 2 Preview | no `Preview:` line | one problem: missing |
| 3 Greeting | no `{{first_name}}` in the body | one problem |
| 3 Greeting | `Hi {{first_name}},` present | no problems |
| 4 One link | two `[text](https://...)` links | one problem: too many links |
| 4 One link | no link | one problem: no link |
| 4 One link | a link written `[text](http://...)` | still counts as a link, so no problem for the count |
| 5 Footer | no `You're getting this because` line | one problem |
| 5 Footer | no `Unsubscribe: {{unsubscribe_url}}` line | one problem |
| Two at once | no greeting and no footer lines | the problems are all listed, one per line, exit 1 |
| Whole issue | `issues/issue-01.md` | `OK`, exit 0 |

Note: `issue-01.md`'s preview is 86 characters, so it passes. `{{unsubscribe_url}}` and `{{company_address}}` are placeholders, not links.

**What happened:**

---
