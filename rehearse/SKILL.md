---
name: rehearse
version: 1.0.0
description: Part of the paper-theater suite. rehearse turns a THEORY PAPER (economics / OR / IS) into an iPad-ready STUDY file — it identifies every load-bearing math tool the paper runs on (envelope theorem, normal–normal updating, supermodularity, fixed-point arguments, ...) and builds one TOOL PAGE per technique: minimal clean statement, exactly how THIS paper uses it, a stripped worked example, a pitfall, and 2–3 exercises with full solutions at the back — compiled at 12pt with a wide right margin for Apple Pencil working, to rehearsal/rehearse-<slug>.pdf. TRIGGER when the user wants to study / learn / drill / "understand the math behind" a paper, asks "what tools does this paper use and teach me them", or wants a study companion for reading-group prep. SKIP for stripping a paper's logical spine (that is script — rehearse teaches TECHNIQUES, script maps STRUCTURE); SKIP for prototyping (stage), verification (tryout), and anything about music, theater or sports rehearsal outside academic-paper study.
---

# Purpose

Produce `rehearsal/rehearse-<slug>.tex → .pdf`: the paper's technique
curriculum — every math tool it stands on, taught one per page, sized and
margined for iPad + Apple Pencil study. The reader who works through the
rehearsal can then read the paper's proofs as moves they recognize rather
than magic. Layout conventions live in
`~/.claude/skills/paper-theater/format/rehearsal-preamble.tex` and
`templates.md` — read them at the start of every run.

# Procedure

## Step 0. Announce and read

Print 2–3 lines: rehearse extracts a paper's math tools into a study file
with exercises; it needs the paper (PDF, .tex, or path). Read the paper
end-to-end, PROOFS INCLUDED — the tools live in the proofs, not the
statements.

## Step 1. Identify the tools

List every load-bearing technique: the named theorems invoked (envelope,
Berge, Topkis, Banach, ...), the standard manipulations done silently
(conditional-variance decomposition, FOC + envelope, change of measure,
coupling), and the field folklore assumed (single-crossing arguments,
supermodular comparative statics). Rank by how much of the paper stands on
each; keep the tools a competent reader of THIS paper must actually execute —
typically 4–8. Cut background a graduate course already guarantees unless the
paper uses it in a non-obvious way. Confirm the tool list with the author
before building ("these 6, in this order — right?") — one wrong tool wastes a
page, one missing tool defeats the purpose.

## Step 2. Build one tool page per technique

Per templates.md, each `\toolpage`:

- **Statement** — the minimal clean general form, not the most general known.
- **In this paper** — the paper's exact instantiation, in the paper's own
  notation, pointing at where it fires ("this is the step from (12) to (13)").
  This section is the skill's whole reason to exist — a generic textbook page
  would not need the paper.
- **Worked example** — stripped to the smallest instance that still exercises
  the mechanism; every line followable, no "clearly".
- **Pitfall** — the standard misuse, omit if none is real.
- **2–3 exercises** — the first solvable from the page alone; the last
  connecting to the paper's actual use (e.g. "reproduce the step from (12) to
  (13) with these simplified primitives"). Difficulty ascends.

Order the pages so tools build on each other where they genuinely do.

## Step 3. Solutions — verified, at the back

Full worked solutions in the `\solutionsection`, one per exercise. **Verify
every solution before shipping it**: run the algebra through sympy (or a
quick numeric check) wherever the solution is checkable — a study file with a
wrong solution teaches the error with authority. An exercise whose solution
cannot be verified gets rewritten until it can, or cut.

## Step 4. Compile and hand off

Copy `format/rehearsal-preamble.tex` into `rehearsal/`, build per
templates.md, `latexmk -pdf` twice. Confirm: one tool per page, exercises on
the tool pages, solutions at the back, wide right margin rendering. Hand
back: tool list, page count, and the suggestion to script the same paper if
its STRUCTURE (not just its techniques) is worth mapping.

# Constraints

- **Exercises must be solvable from the page.** The tool page plus the stated
  prerequisites — no hidden dependence on the full paper or outside courses.
- **No unverified solution ships.** Checkable → checked (sympy or numeric);
  uncheckable → rewritten or cut.
- **"In this paper" is mandatory on every tool page.** Without it the file is
  a generic worksheet; the paper-specific instantiation is the product.
- **Tools, not results.** rehearse teaches the techniques; the paper's own
  propositions belong to script. A tool page never restates the paper's
  contribution as an exercise answer.
- **One tool per page; the margin stays empty.** The white space IS the
  product — it is where the reader works.
- **4–8 tools, confirmed with the author.** Twenty pages of background is a
  textbook, not a rehearsal.
