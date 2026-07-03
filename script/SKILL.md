---
name: script
version: 1.1.0
description: Part of the paper-theater suite. script strips a THEORY PAPER (economics / OR / IS) down to its script — the bare spine of assumptions, definitions, lemmas, propositions and theorems, in the paper's own order, each block a FAITHFUL restatement with a source anchor [Thm 2, eq. (14), p. 9] and one line of role glue — compiled to a 1–3pp LaTeX→PDF in scripts/<slug>/. Works on OTHER PEOPLE'S papers (reading instrument; blocks marked Stated/Outside, and the run ends with the canon gate — "Canon-worthy?") and on the author's OWN drafts (pen-testing backbone; confidence discs allowed, no canon gate). TRIGGER when the user wants to strip / x-ray / skeleton-ize / spine-out / "get the bare bones of" an EXISTING paper or draft, wants a fast structural read of a paper, or wants to compare two drafts structurally. SKIP for building a prototype of a NEW idea (that is stage); SKIP for studying a paper's math tools (that is rehearse); SKIP for verifying results (tryout) and for prose work; SKIP anything about shell/Python/film scripts or screenwriting — this skill only ever fires on academic theory papers.
---

# Purpose

Produce `scripts/<slug>/script-<slug>.tex → .pdf`: the paper reduced to its
load-bearing blocks, readable in minutes, auditable against the original in
seconds. The script is a READING instrument, not a rewrite: what the paper
*actually says*, stripped of prose. All conventions live in
`~/.claude/skills/paper-theater/format/format.md` — read it (plus
`templates.md`) at the start of every run; never restate it.

# Procedure

## Step 0. Announce, locate, classify

Print 2–3 lines: what script does, what it needs (a paper: PDF, .tex, or a
path). Then classify the input — this decides the whole run:

- **External paper** (someone else's, usually published) → markers `[s]`
  Stated / `[o]` Outside; canon gate at the end.
- **Author's own draft** → confidence discs `[v|p|h|c]` initialized from the
  draft's claimed status (a result with a full appendix proof enters as `p` —
  *claimed*-proved is not *verified*); NO canon gate (own drafts are never
  exemplars).

If the input is ambiguous, ask which it is. Read the paper end-to-end before
writing anything — a script of a half-read paper is a guess.

## Step 1. Extract the blocks — fidelity above all

Walk the paper in ITS order. For each load-bearing element (assumption,
definition doing real work, lemma, proposition, theorem, corollary, key
identity), write one reduced block per format.md: `\blocktag` (tagged by the
paper's own section) + result environment `[s|o]` (or disc) + `\Anchor{...}` +
`\Role` (one line: what work this does in the paper) + optional `\Next` (≤1
sentence) where it genuinely helps the read.

The fidelity rules in format.md §Fidelity are the heart of this skill:
faithful restatement (bugs included), **hypothesis completeness** (every
assumption reference and side condition survives compression — abbreviate,
never drop), source anchor on every block at the finest granularity the
source permits, the paper's order, gaps flagged in Open joints — never
silently repaired. Notation may be lightly normalized ONLY when the paper's
own notation is inconsistent, and any such change is noted. After drafting
all blocks, run a **hypothesis audit pass**: re-open each source result and
tick off its conditions against the restated block, one by one — this is
the single highest-yield check in the skill.

What to cut: literature reviews, motivation, robustness prose, empirical
sections (note their existence in one line), anything not load-bearing. What
never to cut: an assumption that a proof actually uses, even if the paper
buries it in a footnote — surfacing those is half the value.

## Step 2. Head matter and open joints

Fill the QUESTION/ANSWER line (one line each — if you cannot, you have not
understood the paper; re-read). Close with **Open joints (reader's notes)**:
gaps, silent assumptions, steps that look fragile, claims stronger than their
proofs. This is the reader's honest margin, clearly separated from what the
paper says.

Optionally (papers with ≥5 blocks): add the one-page `skeleton.tex` map per
templates.md, with s/o discs.

## Step 3. Compile

Copy `format/preamble.tex` into `scripts/<slug>/`, build per templates.md,
`latexmk -pdf` twice, fix LaTeX never content.

## Step 4. The canon gate (external published papers only)

End the run with a short structural assessment: spine shape, technique tags,
what the paper does structurally that is worth imitating. Then ask ONE
question:

> **Canon-worthy?** — not "is it good" (the venue answered that) but "would
> you imitate its structure?" If yes: shelf = {{suggestion}}, techniques =
> {{...}}, shape = {{...}}, lesson = "{{1–2 lines: the move worth stealing}}",
> portable = {{yes/no}}. Add / edit / skip?

On yes: write the entry per format.md §Canon to
`~/.claude/paper-theater/canon/entries/<slug>.md`, append the index row,
creating directories as needed. On skip: nothing — no auto-admission, ever.

For the author's own drafts, replace the gate with a one-line handoff: the
script is the pen-testing backbone; offer to go block-by-block.

# Constraints

- **Never improve while extracting.** A repaired claim, a tightened bound, a
  smoothed gap — each is a falsification of the source. Flag in Open joints;
  extract what is written.
- **Never drop a hypothesis while compressing.** A statement missing one of
  its source's conditions claims more than the paper proved — the worst kind
  of unfaithful, because it reads as MORE authoritative. Abbreviate
  ("under A1, A3–A4"), never omit; audit every block's conditions before
  shipping (format.md §Fidelity).
- **Never reorder into a "better" sequence.** The paper's order is data.
- **No block without an anchor.** Unanchored blocks cannot be audited and do
  not ship.
- **Never mix alphabets.** s/o for external papers; v/p/h/c only on the
  author's own drafts. And a claimed proof enters at `p`, never `v` — script
  verifies nothing.
- **The canon gate is a question, not an action.** No entry is written without
  an explicit yes. Own drafts get no gate at all.
- **Do not restate format.md.** Read it each run; conventions live there.
