---
name: tryout
version: 1.0.0
description: Part of the paper-theater suite; successor to temper (which stays untouched and owns legacy proto/ prototypes). tryout puts an existing staging/ through its out-of-town tryout — THREE verification passes on every checkable result: (A) analytical, completing/auditing the symbolic derivations in sympy; (B) numeric, a seeded verify.py harness of limiting cases, random instances over the stated domain, and an active counterexample hunt; (C) blind skeptic, each result's STATEMENT with the proof withheld handed to a fresh adversarial agent whose only goal is to break it — then updates the confidence discs to their EARNED values and writes staging/tryout/tryout-report.md. On failure it shows the breaking instance and SUGGESTS fixes; it never edits the math. TRIGGER ONLY when staging/verification.md EXISTS and the user wants to verify / stress-test / confirm / harden the staging, turn discs green, or hunt counterexamples. Hard precondition: no staging/verification.md → do not fire; a proto/ directory is temper's lane, not tryout's. SKIP fixing the math (stage/restage), generic checks on standalone scripts, and systematic assumption-relaxation (the future ledger).
---

# Purpose

Deliver the verdict on a staging: every checkable result attacked three ways —
symbolically, numerically, and by a skeptic who never saw the proof — and every
disc moved to the value the evidence earns. tryout reads and updates the
artifact; it does not own its conventions, does not touch the math, and stops
at the verdict. All conventions live in
`~/.claude/skills/paper-theater/format/format.md` (§Discs, §Evidence ladder,
§verification.md) — read it and `templates.md` every run; never restate them.

# Procedure

## Step 0. Announce and load the contract

Print 2–3 lines: tryout runs the three passes and charges discs to earned
values; it needs `staging/verification.md`. If absent, stop — nothing to try
out; point at stage (or at temper if the user has a legacy `proto/`). Read
`verification.md` end-to-end: it is the ONLY statement of stage's intent.
Honour each row's proposed check; extend a check only when it is too weak to
settle a disc.

## Pass A — analytical (sympy)

For each result whose symbolic story is incomplete (disc below `v`, or a
`Check ✗` line): attempt to COMPLETE the derivation in sympy — full
derivation, sign/threshold/monotonicity settled on the stated domain, not at
points. Audit, don't trust: re-run stage's existing `checks/` scripts rather
than believing their claimed output. A completed symbolic proof makes the
result `v`-eligible (still subject to Pass C). Work in `staging/checks/`
(extending stage's scripts) — clearly marked `# tryout pass A` blocks.

## Pass B — numeric (verify.py)

Write ONE self-contained `staging/tryout/verify.py` per templates.md: one
function per label, seeded RNG (breaking instances must reproduce), and the
three probe kinds with their ceilings per format.md §Evidence ladder —
limiting cases (→ supports `p`), broad random instances (→ `v`-eligible),
counterexample hunt: grid sweep, then random search, then a small optimizer
pushed toward the constraint boundary (strongest evidence; a hit demotes and
produces the instance). Non-numeric claims → `inconclusive`, honestly — never
invent a probe that proves nothing. Prefer numpy; scipy only when a check
needs an optimizer or solver. Run it; capture the per-label table.

## Pass C — blind skeptic

For each result at `p` or above after A+B: hand the STATEMENT ONLY — with the
Setup primitives it needs, but the proof, intuition, and risk flag withheld —
to a fresh adversarial agent (Agent tool, general-purpose) whose sole
instruction is: *construct a counterexample or a concrete failure argument;
default to skepticism*. Withholding the proof is the point — an agent that
reads the proof searches where the proof looks; one that doesn't searches
where the statement is weak. Triage each verdict as a LEAD, not a ruling:
check any claimed counterexample numerically (add it to verify.py) before it
demotes anything. In an environment without subagents, run the skeptic as a
maximally separated fresh pass — statement only, adversarial framing — and
say so in the report.

## Step 4. Charge the discs

Map each result's combined evidence to its earned disc per format.md
(`v` requires: complete symbolic proof OR broad coverage + clean hunt, AND no
unresolved skeptic hit; failures demote to what the surviving evidence
supports, with the breaking instance documented). Edit ONLY the disc tokens —
the `[x]` note argument in the main file and the matching `\disc{x}` in
`skeleton.tex`, matched via `\label` — then `latexmk -pdf` twice so the
header tally recomputes. Update the registry row's tally in
`~/.claude/paper-theater/index.md`.

## Step 5. Report and stop

Write `staging/tryout/tryout-report.md` per templates.md: per-label probes,
outcomes, skeptic verdicts, disc before → after, breaking instances with
suggested fixes (NOT applied), confidence distribution before → after. Hand
back in ≤6 lines: report path, discs charged green, anything that broke and
the cheapest suggested fix, and — if reds/oranges remain — "restage to apply
a fix, or open the discuss loop." Then stop. Applying fixes is
stage/restage's lane; systematic assumption-relaxation is the future ledger's.

# Constraints

- **Never edit the math.** Statements, intuitions, sketches, inequalities —
  untouchable. Disc tokens only. The boundary is what makes the verdict
  trustworthy.
- **Never assign green on intuition, and never skip Pass C for a `v`.** A
  green disc means: proven or broadly confirmed, AND survived a skeptic who
  never saw the proof.
- **Skeptic output is a lead, not a verdict.** Every claimed counterexample
  is checked numerically before it moves a disc.
- **Seed everything.** An unreproducible breaking instance is a rumor.
- **`inconclusive` is an honest answer.** A probe that tests a trivial
  corollary and calls the result Verified is a green facade — the failure
  mode the suite exists to prevent.
- **Do not apply fixes, do not hand-edit tallies, do not touch `proto/`**
  (temper's lane), **do not restate format.md.**
