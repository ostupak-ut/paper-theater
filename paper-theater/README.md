# paper-theater

**Miniature stagings of theory papers, as Claude Code skills.**

Nineteenth-century toy theaters were full productions in miniature — stages
printed on paper, sold as kits, made to test whether the play works before
anyone builds the real set. paper-theater does the same for theory papers in
economics, operations research, and information systems: small, complete,
honest stagings of the logic, before you write the paper.

> *script the paper, rehearse its moves, stage your own, tryout before
> opening night — the survivors join the canon.*

## The six acts

| skill | what it does |
|---|---|
| **script** | strips any paper — yours or the literature's — to its bare spine: assumptions, lemmas, results, in the paper's own order, every block faithfully restated and source-anchored (`[Thm 2, eq. (14), p. 9]`). A 30-page paper becomes a 2-page read. Published papers end with the **canon gate**. |
| **rehearse** | extracts the math tools a paper runs on (envelope theorem, normal–normal updating, supermodularity, …) into an iPad-ready study file: one tool per page — statement, *how this paper uses it*, worked example, exercises — with verified solutions at the back and a wide margin for Apple Pencil working. |
| **stage** | turns a new idea into a lean 2–4pp prototype: building blocks with capped glue (Intuition ≤ 2 sentences, Next ≤ 1), a confidence disc on every result **earned by an actual sympy check**, a one-page skeleton map, and a verification contract — calibrated against exemplars retrieved from your canon. |
| **restage** | rebuilds a staging after the math changes, with honest cache invalidation: unchanged blocks keep their earned discs, changed blocks reset. A green disc never survives a change to the math it verified. |
| **tryout** | the out-of-town tryout, three passes per result: **analytical** (complete the symbolic derivation in sympy), **numeric** (seeded harness — limiting cases, random instances, counterexample hunt), **blind skeptic** (the statement, *proof withheld*, handed to a fresh adversarial agent told to break it). Discs move to what the evidence earns. It never edits the math. |
| **canon** | your exemplar library — papers whose *structure* you would imitate, each stored as spine + shelf tags + a 1–2 line lesson ("the move worth stealing"). Human-gated, shelf-disciplined, and the thing that makes stage sound like you rather than like a language model. |

## The confidence discs

Every result carries one: 🟢 **Verified** (complete symbolic proof, or numeric
confirmation + surviving the skeptic) · 🔵 **Plausible** (key step checked) ·
🟠 **Heuristic** (intuition only) · 🔴 **Conjectured** (no argument yet).
Script mode adds ⚫ **Stated** / ⚪ **Outside** for other people's papers.
Discs are tied to evidence, never to confidence; tallies are auto-computed;
nobody — human or model — hand-edits one.

## Design principles

1. **One source of truth.** Every convention (discs, glue caps, labels,
   directories, schemas) lives in `paper-theater/format/` — skills read it and
   are forbidden to restate it. (The predecessor suite kept three copies of
   its own format and they drifted; never again.)
2. **The verdict is taken away from the author.** The model that wrote a
   proof is the worst judge of it. Symbolic checks go through sympy, numeric
   checks through a seeded harness, and the skeptic never sees the proof —
   prover ≠ checker, and the final word belongs to things that can't be
   persuaded.
3. **Glue is capped.** A prototype must read in ten minutes. Two sentences of
   intuition and one of forward glue per block — hard caps, because glue that
   grows turns the staging back into a paper.
4. **Curation is human.** Nothing enters the canon without your explicit yes.

## Install

```bash
git clone https://github.com/ostupak-ut/paper-theater
cp -R paper-theater/{script,rehearse,stage,restage,tryout,canon,paper-theater} ~/.claude/skills/
```

Requires: Claude Code, LaTeX (`latexmk`, `libertine`, `newtxmath`,
`tcolorbox`, `totcount`), Python (`sympy`, `numpy`; `scipy` optional).

Runtime data lives in `~/.claude/paper-theater/` (stagings registry + canon).

## Layout

```
paper-theater/            shared: format/format.md (the law), preamble.tex,
                          rehearsal-preamble.tex, templates.md
script/    rehearse/      SKILL.md each — procedure + constraints only;
stage/     restage/       no skill embeds a convention
tryout/    canon/
```

## Lineage

paper-theater succeeds **forge** and **temper** (still installable; they own
the legacy `proto/` format). What changed: extraction-first (script is the
daily driver, not the generator), capped narrative glue, the collectible-card
cover retired, disc invalidation on rebuild, a blind-skeptic verification
pass, and the canon.

*prototype · paper-theater · v1.0*
