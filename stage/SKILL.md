---
name: stage
version: 1.0.0
description: Part of the paper-theater suite; successor to forge. stage turns an UNPROVEN research idea for a THEORY PAPER (economics / OR / IS) into a lean 2–4pp LaTeX→PDF staging in staging/ — a legible spine of building blocks with capped glue (Intuition ≤2 sentences, Next ≤1) between them, a confidence disc (Verified/Plausible/Heuristic/Conjectured) on every result earned by an actual sympy check in staging/checks/, a one-page skeleton map, and a verification.md handoff to tryout — calibrated against matching exemplars retrieved from the canon. TRIGGER when the user wants to prototype / sketch / scaffold / spine-out / "see if the logic holds" / "get this onto paper" for a NEW model-and-results idea, from a one-line question, scattered notes, or ore dropped into inputs/. SKIP when a staging already exists and the math changed (that is restage); SKIP for stripping an EXISTING paper to its bones (script); SKIP for verification (tryout), full paper writing, copy-editing, referee responses (rr-ignite), lit reviews, slides, or pure empirical work; SKIP anything about git staging, deployment stages, or staging environments — this skill only ever fires on theory-paper prototyping.
---

# Purpose

Produce `staging/`: a compilable 2–4pp staging of a theory paper — compact
`\stagehead` (no cover page), abstract-as-hook, Setup in run-in modules,
building blocks with capped glue, `\input`-ed proofs and skeleton, sympy
checks, and the `verification.md` contract for tryout. The artifact is a
THINKING INSTRUMENT: read in under ten minutes, judged on one question — does
the spine hold? Optimize, in order: graspability, a legible spine, honesty
about weak joints. All conventions live in
`~/.claude/skills/paper-theater/format/format.md` — read it and `templates.md`
at the start of every run; never restate them.

# Procedure

## Step 0. Announce and take stock

Print 2–3 lines: stage builds a lean prototype from an idea; it needs a seed
(a one-line research question, notes, or ore in `inputs/`); tryout verifies
afterwards. Then scan `inputs/` (create it and `inputs/literature/` if
absent), inventory out loud, and confirm the centre of gravity before
building. No seed → ask; never invent a topic. **Stance: raw ore** — keep the
load-bearing content, cut filler, re-derive the spine yourself, flag weak
logic rather than smoothing it (exception: "stay close to this draft" switches
the stance off). Prose is ideas; code in `inputs/` is evidence and can promote
a disc, cited in verification.md.

Claim the next id from `~/.claude/paper-theater/index.md` (create from
format.md §Registry if absent). Main file: `staging/stage-NNN-slug.tex`.

## Step 1. Retrieve from the canon

Read `~/.claude/paper-theater/canon/index.md` (if it exists). Pull the 1–3
entries whose field/shelf/techniques match the idea; `portable: yes` lessons
may cross shelves, field-bound ones may not. Use them to CALIBRATE — block
granularity, lemma-to-proposition ratio, where the engine sits, the structural
lessons — never to copy content. Say which exemplars you drew on (or that the
canon is empty/no shelf matches — then proceed uncalibrated and say so).

## Step 2. Find the spine

Extract the minimal load-bearing chain: the **engine** (the one lemma or
mechanism everything rests on), the **headline results** it produces, the free
**corollaries**, the **dependencies**. Pick the field flag (econ / OR / IS)
and follow format.md's importance ladder — propositions headline, claims do
the work, theorem is reserved.

## Step 3. Verify symbolically, then disc every result

Never assert a result you have not derived or checked. For every checkable
result, write and run a sympy script in `staging/checks/` (one per result,
named by label): derivatives, signs, thresholds, monotonicity, limits —
settled SYMBOLICALLY on the domain, not at sampled points. Then assign discs
per format.md: a complete symbolic proof earns `v`; a checked key step earns
`p`; nothing checked → honest `h`/`c` and a `Check ✗: unverified` line. A
fresh staging is mostly red/orange/blue by design — resist inflation.

## Step 4. Build the body

Per templates.md: header macros, abstract-as-hook (if you cannot write it, the
spine is not clear yet — back to Step 2), Setup as run-in `\paragraph` modules
(Players / Timing / Strategies, extras only as needed), then one building
block per spine node — format.md §Block anatomy, glue caps hard
(Intuition ≤ 2 sentences, Next ≤ 1). Labels are semantic and immutable
(`lem:engine`, never `prop:2`) — restage depends on this. Statements tight;
blocks flush-left; body 2–4pp; blocks are nodes, not quotas. Close with
**Open joints**. Citations only with the source in `inputs/literature/` —
no source in hand, no `\cite`.

## Step 5. Proofs, skeleton, contract

`proofs.tex`: one `myproof` sketch per result — the move and mechanism, the
symbolic check cited, the risky step flagged; no ε-δ rigour. `skeleton.tex`:
the one-page map per format.md (20-second rule). `verification.md`: one row
per result per templates.md — this is tryout's entire input; write the
proposed numeric checks as if briefing a hostile examiner.

## Step 6. Compile, register, hand off

Copy `format/preamble.tex` into `staging/`; `latexmk -pdf` twice; fix LaTeX,
never math. Append the registry row (real date, actual disc tally). Then end
with three moves: (1) state which discs are not yet confirmed and that
**tryout** charges them green — the artifact's header already says so;
(2) ask "verification contract written — run tryout now?"; (3) offer the
refine door, opt-in: "want to challenge the weak blocks or rework the spine?"

# Constraints

- **No unearned disc, ever.** Evidence per format.md, or the disc drops. An
  unearned green is the one failure mode the suite exists to prevent.
- **Glue caps are hard caps.** Intuition ≤ 2 sentences, Next ≤ 1. Growing glue
  is how a staging silently becomes a paper.
- **No cover page, no rarity stars, no paper card.** The compact `\stagehead`
  is the whole ceremony. (forge's card was retired deliberately.)
- **Semantic, immutable labels.** Position-named labels break restage.
- **Do not write into `proto/`** (forge/temper's legacy dir) and never edit
  `inputs/` in place.
- **Body ≤ 4 pages.** Past four it is a paper — downstream work stage does
  not do. Full proofs never inline.
- **Intuition carries the mechanism**, never a restatement of the claim.
- **No hand-typed cross-reference numbers, no hand-edited tally.** Real
  `\ref`s; flip disc keys and recompile.
- **No fabricated citations, no invented literature review.**
- **Do not restate format.md** — read it each run; it is the single source of
  truth, and re-embedding it is how forge drifted.
