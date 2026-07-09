# paper-theater :: format.md — the single source of truth (v1.5)

Every paper-theater skill (script, rehearse, stage, restage, tryout, canon, blocking) READS
this file and the assets beside it. **No skill may restate, quote, or re-embed
these conventions in its own SKILL.md** — that is how forge v0.x drifted into
three divergent copies of its own format. If a convention needs to change, it
changes HERE, and the version bumps HERE.

## The suite, in one line each

| skill    | verb                                                        | writes to            |
|----------|-------------------------------------------------------------|----------------------|
| script   | strip any paper to its bare spine (faithful, source-anchored) | `scripts/<slug>/`   |
| rehearse | extract a paper's math tools into an iPad-ready study file  | `rehearsal/`         |
| stage    | build a lean 2–4pp prototype of a NEW idea, glue included   | `staging/`           |
| restage  | rebuild a staging after the math changed (disc invalidation) | `staging/`          |
| tryout   | verify a staging: symbolic + numeric + blind skeptic        | `staging/` (discs only) |
| canon    | browse/manage the global exemplar library                   | `~/.claude/paper-theater/canon/` |
| blocking | map a model's moving parts into an interactive HTML explorer + chat walk | `blocking/` |

Lineage: stage/restage supersede **forge**; tryout supersedes **temper**. The
legacy skills stay installed and own the legacy `proto/` directory — paper-theater
skills never touch `proto/`, and forge/temper never touch `staging/`.

## Directory contract

```
<project>/
  staging/                     owned by stage; restage edits; tryout edits DISCS ONLY
    preamble.tex               copied verbatim from format/preamble.tex — never rewritten
    stage-NNN-slug.tex         main file, 2–4pp body  (compiles to .pdf, latexmk twice)
    proofs.tex                 \input-ed appendix — footnotesize proof sketches
    skeleton.tex               \input-ed last — the one-page dependency-flow map
    checks/                    sympy scripts, one per checkable result (stage's symbolic pass)
    verification.md            handoff contract to tryout — one row per result
    tryout/                    tryout's workspace: verify.py, skeptic notes, tryout-report.md
    refs.bib                   only sources actually leaned on (no source in hand → no \cite)
  scripts/<slug>/              owned by script: script-<slug>.tex → .pdf (+ preamble copy)
  rehearsal/                   owned by rehearse: rehearse-<slug>.tex → .pdf (+ rehearsal-preamble copy)
  blocking/                    owned by blocking: graph.json (the extracted graph — the record of a run)
    blocking-<slug>.html       the self-contained interactive explorer (template + injected graph.json)
  inputs/                      read-only ore (drafts, notes); inputs/literature/ = leaned-on sources

~/.claude/paper-theater/       the global home (cross-project)
  index.md                     the stagings registry — one row per staging ever built
  canon/index.md               the canon shelf list — one row per exemplar
  canon/entries/<slug>.md      one entry per canonized paper
  blocking/index.md            the map library registry — one row per model map ever built
  blocking/maps/<slug>.html    self-contained copies of every emitted map
  blocking/library.html        the shelf front-end (regenerated from index.md each run)
```

Skills create missing directories silently. `inputs/` is never edited in place.

## Registry (stagings)

`~/.claude/paper-theater/index.md` — append one row per completed staging:

```
| id  | slug | field | date | V/P/H/C | project path |
```

Take the next 3-digit id (`001`, `002`, …) by scanning existing rows. The main
file is `stage-NNN-slug.tex`. Real dates only, never placeholders.

## Discs — the confidence vocabulary

One public LaTeX macro: `\disc{v|p|h|c|s|o}`. Result environments carry the key
in the note slot: `\begin{proposition}[p]`. Word ↔ letter, one-to-one:

| letter | word        | colour | earned by |
|--------|-------------|--------|-----------|
| v | **Verified**    | green  | complete symbolic proof (stage) OR clean numeric confirmation + surviving the skeptic (tryout) |
| p | **Plausible**   | blue   | the load-bearing step symbolically checked; rest sketched |
| h | **Heuristic**   | orange | intuition or analogy only; nothing checked |
| c | **Conjectured** | red    | believed; no argument yet |
| s | **Stated**      | gray   | script mode only: proved in the source paper (we did not re-verify) |
| o | **Outside**     | light gray | script mode only: cited/imported from elsewhere by the source paper |

Rules that never bend:
- v/p/h/c describe OUR verification state and appear only in stage/restage/tryout artifacts (and script runs on the author's OWN drafts). s/o describe someone else's paper and appear only in script artifacts on external papers. Never mix the two alphabets in one document.
- A disc is tied to EVIDENCE, never to confidence. An unearned green is the one failure mode the whole suite exists to prevent.
- The header tally is auto-computed from the disc keys via the `.aux` (totcount); NOBODY hand-edits a tally. Flip the key, recompile twice.
- tryout changes disc TOKENS only — the `[x]` note argument in the main file and the matching `\disc{x}` in skeleton.tex. It never edits a statement, a proof, or an inequality.

### Evidence ladder for tryout (probe → ceiling)

- Limiting case by number passes → supports **p** (necessary, not sufficient).
- Broad random-instance coverage passes, no failure → **v**-eligible.
- Counterexample hunt clean over the stated domain → strongest numeric evidence.
- Blind skeptic fails to break the statement → corroborating; a skeptic HIT demotes to the level the surviving evidence supports (usually c or h) and the breaking instance is documented.
- Non-numeric claims (pure existence/structure) → `inconclusive`; do not invent a probe that proves nothing.
- **v requires**: (complete symbolic proof) OR (broad random coverage AND clean hunt), AND no unresolved skeptic hit.

## Block anatomy (stage / restage; script uses the reduced form)

Each building block, in order — every brick starts flush-left (`\noindent`; the
helper macros already do this):

1. `\blocktag{BLOCK n \textperiodcentered\ short name}` — the card separator.
2. Result environment with `[disc]` and a `\label` — statement TIGHT: primitives in, claim out, no prose padding.
3. `\Intuition` — **≤ 2 sentences.** The real mechanism, never a restatement of the claim.
4. `{\footnotesize\Proofsketch ...}` — the move, not the steps, ending with `Check \checkmark\ (symbolic): <what checks/ established>` or an honest `Check $\times$: unverified` (and a disc that matches).
5. `{\footnotesize\Risk ...}` — the one step most likely to break.
6. `\Uses` — the labels this block stands on (omit if only Setup).
7. `\Next` — **≤ 1 sentence.** Forward glue: what this block feeds and why the reader should keep going. Omit on the final block.

**Glue caps are hard caps.** Intuition ≤ 2 sentences, Next ≤ 1. Glue that grows
turns the staging back into a paper — the exact failure the caps exist to stop.

Script's reduced block: `\blocktag` + result env `[s|o]` + one-line role glue
(what work this does in the paper) + source anchor. No Risk/Uses/Next required;
a `\Next` line is allowed where it genuinely helps the read.

## Fidelity rules (script only)

- Every block is a FAITHFUL restatement of what the source paper actually claims — bugs, gaps, and overclaims included. Improving, repairing, or tightening a claim while extracting it is falsification.
- **Hypothesis completeness.** A restated result carries ALL of the source's hypotheses — every assumption reference, every side condition, every "if additionally". Compression may abbreviate a hypothesis ("under A1, A3–A4"), never drop one. A dropped condition is the canonical fidelity failure: the compressed statement claims MORE than the paper proved. (v1.1 rule — the maiden run dropped an "exactly one zero" condition under compression.)
- Every block carries a **source anchor**: the paper's own numbering plus the finest location the source permits — equation number and page for PDFs (`[Thm 2, eq. (14), p. 9]`); for .tex sources, the result's own number/label plus section is acceptable (the label is greppable), equation numbers still preferred where the block leans on one.
- Blocks appear in the PAPER'S order (linear, wrapped around its structure). Script never reorders into a "better" logical sequence.
- A gap or suspected error in the source is FLAGGED in the Open joints list, never silently fixed and never silently smoothed over.
- **Headers.** External papers → `\scripthead` (s/o legend). The author's own drafts → `\scriptheadown` (v/p/h/c legend + auto-tally; discs are OUR verification state, claimed-proved enters at `p`). Both live in `preamble.tex`; never hand-roll a header.
- **Length scales with the source.** The 1–3pp guideline fits typical papers (≤10 numbered results). For dense papers, budget ≈1 script page per 8–10 source pages and keep every load-bearing block — NEVER cut blocks to hit a page count; fidelity outranks brevity.

## Label & ID scheme (what makes restage possible)

- Every result environment gets a stable semantic label at birth: `lem:engine`, `prop:screening`, `clm:tail-bound` — named for CONTENT, never for position (`prop:2` is forbidden; positions move).
- Labels are immutable. A block whose meaning changes materially gets a NEW label; the old one dies. Cosmetic edits keep the label.
- All cross-references (`\Uses`, `\Next`, `\protospine`, skeleton nodes) use real `\ref`/`\Cref` on these labels, full object names spelled out (`Proposition~\ref{...}`, never `Prop`). Hand-typed numbers are forbidden — they go stale silently.

### Restage invalidation semantics

For each label, compare old vs new statement + proof-sketch content:
- **Unchanged** (cosmetic only: wording, spacing, notation-consistent renames) → the earned disc SURVIVES.
- **Changed** (any primitive, bound, condition, direction, or proof mechanism) → the disc RESETS: to `c`, or `h` if a still-valid heuristic argument survives the change. Stage's symbolic pass may then re-earn p/v in the same run — but only by re-running the check.
- **New label** → enters at whatever stage's symbolic pass earns (usually c/h/p).
- **Deleted label** → its skeleton node and registry memory go; note it in the changelog.
- Every restage ends with a `Restage changelog` block in the report: kept / reset / new / deleted, one line each. A green disc surviving changed math is the lie the whole mechanism exists to prevent.

## The skeleton page (one page, 20-second rule)

`skeleton.tex`, `\input`-ed last, its own page: a vertical dependency-flow map
written as a logic story — read down; each step follows from those above. Two-line
bricks: line 1 `<disc> <Full Object Name via \ref, bold> — <plain-English role>`;
line 2, indented smaller, one concrete detail (key condition/formula), with
`(needs <Full Name>)` only for a non-adjacent dependency. Between steps a centered
`$\downarrow$ so / then / and / still open`. Disc legend line at top, tcolorbox
container, one page, readable in ~20 seconds or it has failed.

## verification.md (the stage → tryout contract)

One table row per result:

```
| label | Current disc (WORD) | Symbolic check already run (checks/ file) | Proposed numeric check |
```

plus a Notes block: cheap vs expensive checks, the result most likely to break,
any `inputs/` code that already backs a result. tryout reads this file and
nothing else of stage's intent; tryout writes earned discs back (word → letter)
and its report to `staging/tryout/tryout-report.md`.

## Canon — entry schema and shelf discipline

`~/.claude/paper-theater/canon/entries/<slug>.md`:

```markdown
---
slug: <kebab-slug>
title: <paper title>
authors: <surnames>
venue: <journal/conf>   year: <YYYY>
field: econ | OR | IS
shelf: <subfield tag, e.g. info-design, queueing, mechanism-design>
techniques: [<envelope>, <normal-updating>, ...]
shape: <spine shape: single-engine | ladder | characterization-then-welfare | ...>
portable: yes | no        # is the Lesson structural (travels across shelves) or field-bound?
added: <YYYY-MM-DD>
source: <path to script PDF or DOI>
---
## Lesson
<1–2 lines: the structural move worth stealing>
## Spine
<compressed chain, plain text: Lemma 1 (role) -> Prop 1 (role) => Thm 1 (payoff)>
```

`canon/index.md` — one row per entry: `| slug | venue year | field/shelf | shape | portable | lesson (short) |`.

Admission discipline:
- The gate question is never "is this paper good?" — it is "**would I imitate its structure?**" Venue already answers quality; the canon stores structural taste.
- Human-gated, always: script OFFERS admission ("Canon-worthy?"), the author decides. No auto-admission.
- External published papers only. The author's own unpublished drafts are never exemplars.
- Retrieval is by shelf: stage pulls exemplars whose field/shelf/techniques match the new idea; `portable: yes` lessons may cross shelves, field-bound ones may not.

## Blocking graphs — the suite's one interactive artifact (v1.4, blocking only)

The suite is LaTeX→PDF everywhere except here: blocking emits a SINGLE
self-contained HTML explorer. That is deliberate — the map is an instrument you
click, not read. (v1.3: real KaTeX math, `params` table for constants,
paper-order `sec` columns, `spine` marking — the v1.2 tier layout and
HTML-`<sub>` math are retired.)

**Nodes are machinery, not symbols.** Pure constants (scales, costs, weights)
do NOT get nodes — they live in the `params` table and appear as chips in the
dossiers of the nodes they enter. A symbol earns a node only if it is a MOVE
(a control variable someone chooses) or the headline structural parameter the
paper is about. Node roles:
- **source** — structural assumptions and the few parameter-nodes that qualify; no parents; where the deepest criticisms live.
- **machine** — derived intermediates.
- **assembly** — payoffs/objectives; high in-degree is expected; expandable into sub-term child nodes.
- **result** — theorems; sinks.

**Schema** (`blocking/graph.json`):

```
{ meta:  { title, slug, source, date, mode: own|external,
           sections: [ordered column headers, the paper's own order],
           order: [node ids, narrative walk],
           game: { players, timing: [steps], strategies?, information?, solution } },
  params:[{ id, tex, meaning, feeds: [node ids] }],
  defs:  [{ id, term, aliases?, tex?, def }],
  nodes: [{ id, label, tex, sec, role, kind, disc, short, detail,
            choice?, parent?, params?, spine?, sym? }],
  edges: [{ from, to, type, spine? }],
  flags: [{ id, target, class, severity, one_line, note }] }

params = ingredient symbols that are NOT machinery; tex = the symbol in LaTeX;
         feeds lists every node the symbol enters (drives where-used highlight)
label = plain-text name; tex = the node's defining formula (LaTeX, no $-fences),
        rendered inside the card; sec = one of meta.sections (column placement)
role  = source | machine | assembly | result
kind  = parameter | assumption | variable | mechanism | objective | theorem
disc  = v|p|h|c (own) or s|o (external) or null — same alphabet, same rules, same
        RGB as preamble.tex; discs are carried in, never re-graded by blocking
choice = the modeling choice + 1–2 alternatives (source/assembly nodes only)
parent = assembly id; sub-term nodes author their own in-edges, the explorer
         routes them to the parent while collapsed
params = ids into the params table (renders ingredient chips in the dossier)
spine  = true on the nodes/edges of the load-bearing chain (drawn bold)
game   = the game form (players / timing / strategies / information / solution
         concept). Rendered THREE ways: a framed Setting card opening the
         canvas (before the first section column), the explorer's DEFAULT
         dossier (one Esc away at all times), and beat 0 of presentation mode
         (curtain up on who plays before any machinery); prose may embed $...$
         Presentation mode ignores role/disc/flagged filters — the walk always
         tells the whole story.
defs   = the glossary: technical vocabulary (latent state, screening, i.i.d.,
         ...) with a plain-language definition and optional LaTeX. Terms and
         their aliases AUTO-LINK wherever they appear in dossier prose
         (hover = definition tooltip, click = Glossary tab); write defs for
         every term a smart non-specialist would stumble on
sym    = the symbol this node DEFINES, in LaTeX (string, or array of aliases
         like ["\\Delta_t","\\Delta_t^*"]). Powers hover-definitions: every
         occurrence of the symbol in ANY rendered formula becomes hoverable
         (tooltip = who defines it + one-line meaning) and clickable (jumps to
         the defining card / lights the parameter). params entries participate
         automatically. Give latent states and other stray symbols a params
         entry (feeds may be empty) so nothing in a formula is undefined.
type  = feeds (->) | payoff (=>)          edge id = "from->to"
class = structural | non-structural   severity = load-bearing | fragile | cosmetic
target = a node id, an edge id, or `param:<id>` — every flag pins to the part
         it attacks (a dead/normalizable constant is flagged on its param entry)
```

Node ids are semantic and immutable, same discipline as labels (`delta-s`,
never `node7`); where a part has a `\label` in the source, the id derives from
it. Math is LaTeX everywhere: `tex` fields hold bare LaTeX; `short`/`detail`/
`choice`/`note`/`meaning` prose may embed `$...$` inline math. Rendering is
KaTeX, embedded from `assets/vendor/katex-inline.html` (fonts inlined as data
URIs; rebuild only to upgrade, via `assets/build_vendor.py`).

**The artifact.** Template at `~/.claude/skills/blocking/assets/explorer.html`;
a run replaces the payload of `<script id="graph-data"
type="application/json">` and the `<!--KATEX-->` marker with the vendor
fragment. Fully self-contained and CSP-safe: inline CSS/JS/fonts, no CDN or
fetch; light/dark theme-aware. Layout: columns follow `meta.sections` (the
paper's own order), edges flow left→right, the `spine` chain is drawn bold.
Built-ins that ship with every map: pan/zoom canvas with ⟲ reset (also
double-click the background), dependency-cone highlight (hover preview, click
to lock), clickable edges with their own dossier (a flag on an arrow is
reachable), symbol hover-definitions in every formula (from `sym` + params),
problem overlay, Parameters tab with where-used highlighting, load-bearing
heatmap, role/disc filters, presentation mode stepping `meta.order`, a 💾 save
mode (snapshot copy with view state baked in) and ⇓ json export, print
stylesheet, and per-node "Ask Claude" prompts — the HTML never chats; it hands
the user the exact prompt for the chat side.

**The library.** Every emitted map is also SHELVED globally: the self-contained
HTML is copied to `~/.claude/paper-theater/blocking/maps/<slug>.html`, one row
per map goes in `blocking/index.md`
(`| slug | title | date | parts | flags | source | project |` — slug keyed:
re-running a model updates its row and file, never duplicates), and
`blocking/library.html` — the shelf front-end, generated from the index via the
`assets/library.html` template — lists them all with search and open links.
The index is the source of truth; file management is deliberately thin: add by
running blocking, remove/rename through the chat (file + row + regenerate,
always together, so the shelf never lies).

**Registry.** blocking does not write to the stagings registry (that registry
is stagings-only); `blocking/index.md` and `blocking/graph.json` are the
durable records of a run.

## Compile discipline

`latexmk -pdf`, **run twice** (the `.aux` round-trip settles cross-references and
the auto-tally). Fix LaTeX, never math, until it builds. A document that does not
compile is not a thinking instrument — it is a text file. Footer stamps: each
artifact carries `paper-theater \textperiodcentered\ <skill> \textperiodcentered\ v1.0`
via `\theaterstamp` (skills `\renewcommand` the middle word only).

## Importance ladder (calibrated to the author's actual usage)

1. **theorem** — a genuine centrepiece; often zero per staging. Never reached for to impress.
2. **proposition** — the headline results; the spine is carried here.
3. **lemma** — stepping stones; the engine lemma lives here.
4. **claim** — the workhorse for granular local assertions; reach for this first.
5. **corollary** — free consequences. 6. **definition/assumption** — setup. 7. **remark** — asides.

Billing a claim as a proposition oversells the spine; the rung chosen is itself a signal.
