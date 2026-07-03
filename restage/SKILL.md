---
name: restage
version: 1.0.0
description: Part of the paper-theater suite. restage REBUILDS an existing staging/ after the underlying math changed — new assumption, changed bound, reworked mechanism, added or dropped result — re-deriving the affected spine while applying the disc-invalidation rules; unchanged blocks KEEP their earned confidence discs, changed blocks RESET (a green disc must never survive a change to the math it verified), and every run ends with a kept/reset/new/deleted changelog. TRIGGER when a staging/ directory with a stage-NNN-*.tex already EXISTS and the user wants to rederive / rebuild / update / rework the prototype after changing the model — "restage this", "I changed the assumption, rebuild", "rederive with the new cost function". The existing staging is a hard precondition: with no staging/, do NOT fire — point at stage. SKIP for first-time prototyping (stage), for verification only with no math change (tryout), and for anything about git, deployments, or staging environments.
---

# Purpose

Rebuild `staging/` after the math moved, WITHOUT destroying earned
verification. restage is stage's update mode with one extra duty: honest
cache invalidation of the confidence discs. All conventions live in
`~/.claude/skills/paper-theater/format/format.md` (§Label & ID scheme,
§Restage invalidation semantics) — read it and `templates.md` every run;
never restate them.

# Procedure

## Step 0. Announce and load the old staging

Print 2–3 lines: restage rebuilds an existing staging after a math change,
preserving discs on untouched blocks. Require `staging/stage-NNN-*.tex`; if
absent, stop and point at stage. Read the ENTIRE old staging (main file,
proofs.tex, skeleton.tex, verification.md, checks/) and take a snapshot of
every label → (statement, proof-sketch, disc). Then confirm with the author
what changed and why — the change list drives everything downstream.

## Step 1. Re-derive the affected spine

Apply the change to the model and re-derive from the point of impact
downstream, exactly as stage's Step 2–3 would (engine, results, dependencies;
sympy checks in `staging/checks/` for everything touched — new or re-derived
results earn discs only through evidence, per format.md). Untouched upstream
blocks are not re-derived — they are carried.

## Step 2. Apply the invalidation rules (the heart of the skill)

For every label, old vs new, per format.md §Restage invalidation semantics:

- **Unchanged** (cosmetic only) → disc SURVIVES, checks/ script kept.
- **Changed** (any primitive, bound, condition, direction, or proof mechanism)
  → disc RESETS to `c` (or `h` if a still-valid heuristic argument survives);
  the old checks/ script is stale — delete or rewrite it; a fresh symbolic
  check this run may re-earn `p`/`v`.
- **Materially different meaning** → NEW label; the old label dies.
- **Deleted** → remove its block, skeleton node, and verification.md row.

When in doubt whether a change is cosmetic, it is not — reset. The one
unforgivable outcome is a green disc riding on math it never verified.

## Step 3. Rebuild the artifacts

Update the main file (blocks, glue, spine macro), `proofs.tex`,
`skeleton.tex`, and `verification.md` rows for every touched label — same
anatomy, caps, and templates as stage. Keep `\protonum` (same staging, new
state); update `\protodate`. Compile `latexmk -pdf` twice.

## Step 4. Changelog and handoff

Append the **Restage changelog** (templates.md) to the console summary —
kept / reset / new / deleted, one line each — and update the registry row's
disc tally in `~/.claude/paper-theater/index.md`. End by stating which discs
were reset and ask: "reset discs need re-verification — run tryout now?"

# Constraints

- **Never let an earned disc survive changed math.** Reset on doubt. This
  rule outranks every other consideration in the skill.
- **Never reset an untouched block's disc.** Gratuitous resets destroy the
  value of verification just as surely as stale greens — the ledger must be
  exact in both directions.
- **Labels are immutable; meaning-changes get new labels.** No reuse of a
  dead label for different content.
- **The changelog is mandatory.** A restage without a kept/reset ledger is
  indistinguishable from a silent rewrite.
- **Everything stage forbids, restage forbids** — unearned discs, glue-cap
  violations, hand-typed numbers, fabricated citations, writing into
  `proto/`, restating format.md.
