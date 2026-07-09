---
name: blocking
version: 1.3.1
description: Part of the paper-theater suite. blocking turns a theory MODEL (economics / OR / IS) — the author's own .tex, a paper being read, or an existing staging/ / scripts/<slug>/ / proto/ skeleton — into an INTERACTIVE dependency graph of its MOVING PARTS. Nodes are the MACHINERY, not theorem-blocks and not every symbol — structural assumptions, choice variables, derived quantities, objective functions (expandable into their TERMS), results — laid out in the PAPER'S OWN section columns with the load-bearing spine drawn bold, every formula rendered in real KaTeX, constants relegated to a clickable parameters table, discs reused as confidence marks, and PROBLEMS (structural + modeling) pinned to the exact node, edge, or parameter they attack. Output: a self-contained HTML explorer at blocking/blocking-<slug>.html (+ graph.json), then a Claude-side "walk the graph" chat (open <node> / flags / present) that doubles as a presentation scaffold. TRIGGER when the user wants to "map the model", "graph the moving parts", "what depends on what", "pin the criticisms to the parts they hit", an interactive model explorer, or a narrative walk of the mechanism for a talk. SKIP for stripping a paper to a linear spine PDF (script), prototyping a NEW idea (stage), verification (tryout), studying a paper's math tools (rehearse); SKIP stagecraft — actors, cameras, choreography — this skill only ever fires on theory models.
---

# Purpose

Produce `blocking/`: the model rendered as a fine-grained dependency graph —
`graph.json` (nodes / edges / flags) injected into the explorer template at
`~/.claude/skills/blocking/assets/explorer.html` to yield one self-contained
`blocking-<slug>.html` — followed by a chat loop that walks the graph with the
full source model in context. The artifact is the MAP; Claude is the GUIDE.
The map answers "what stands on what, and what breaks if this breaks" in one
screen; the guide argues. The graph schema, node roles, edge types, flag
classes, and the interactive-artifact conventions live in
`~/.claude/skills/paper-theater/format/format.md` §Blocking graphs — read it
each run; never restate it.

# Procedure

## Step 0. Announce and take stock

Print 2–3 lines: blocking maps a model's moving parts into an interactive
explorer plus a chat walk; it needs a model source. Locate it: the user's own
draft `.tex`, an external paper, or an existing skeleton
(`staging/skeleton.tex`, `scripts/<slug>/`, legacy `proto/`). Prefer existing
suite artifacts as pre-parsed ground truth — `skeleton.tex`, `verification.md`,
review notes carry the spine, the discs, and half the flags already; the
source model is still read in full. Classify own draft vs external paper —
this fixes the disc alphabet per format.md (v/p/h/c vs s/o). No model → ask;
never invent one.

## Step 1. Extract the graph

Walk the model and emit one node per MOVING PART — every structural
assumption, derived quantity, payoff / objective function, result — but NOT
every symbol: pure constants go to the `params` table (format.md says which
symbols earn nodes). Give every node its `tex` (the defining formula, bare
LaTeX), its `sec` (the paper section — this IS the column layout, so the map
reads as the paper), and mark the load-bearing chain `spine`. Nodes that
define a symbol carry `sym` (aliases allowed) so every formula hover-defines
its variables; stray symbols (latent states, noise terms) get params entries
for the same reason — no glyph on the map should be undefined. Fill
`meta.game` (players / timing / strategies / solution — the default dossier)
and `defs` (the glossary; terms auto-link in all prose) — no term a reader
would stumble on should go undefined either. Objectives
additionally get sub-term child nodes (`parent` field) — e.g. Π → benefit
term, harm term — with in-edges authored at the term level (the template
routes them to the parent when collapsed). Assign each node its role
(source / machine / assembly / result), kind, and disc per format.md
§Blocking graphs. Harvest identities mechanically,
no heavy parser: real `\label` keys, `\Uses` / `\protospine` lists (`->` feeds,
`=>` payoff), `(needs \ref{...})` cross-links; parameters and assumptions get
semantic ids of the same discipline. Discs are CARRIED from the source
artifact or entered per format.md's own-draft rule — blocking never re-grades
one. Source and assembly nodes carry a `choice` line: the modeling choice made
plus 1–2 live alternatives.

## Step 2. Flag problems

Structural flags fall out of the topology: a load-bearing node or edge whose
removal disconnects a large descendant cone; a dead / normalizable parameter
(near-zero out-degree, never interacts); an over-connected assembly node (one
objective doing too many jobs); an implicit assumption (used by a derivation
but declared by no source node — a missing in-edge); a cycle where a DAG is
implied. Non-structural flags come from the review notes / `verification.md`
plus light reasoning: a fragile functional form doing structural work, a
missing in-edge that economics says should exist, an interpretation stretch.
Every flag targets one node or one edge (`from->to`) with class, severity, a
one-liner, and a note per the schema. Few sharp flags beat many weak ones.

## Step 3. Emit the map

Write `blocking/graph-<slug>.json` (per-slug, NEVER a shared graph.json — a
project may hold many maps). Emit = template with THREE substitutions: the
payload of `<script id="graph-data" type="application/json">` becomes the
graph, the `<!--KATEX-->` marker becomes the vendor fragment
`assets/vendor/katex-inline.html` (self-contained math; never link a CDN),
and `{{LIBHREF}}` becomes the absolute file:// URL of the library page;
write `blocking/blocking-<slug>.html`. Verify before shipping: JSON parses;
every edge endpoint, flag target (node, edge, or `param:`), `sec`, param id,
and sub-term parent resolves; the collapsed graph is a DAG. Then OPEN the map
in the user's browser without being asked — `open
blocking/blocking-<slug>.html` (macOS; use the platform equivalent elsewhere)
— and note the built-in 💾 save mode (a state-baked snapshot copy) and ⇓ json
export. On a re-run over an existing map, remind the user to refresh the tab
instead of opening a duplicate. Then SHELVE the map in the global library per
format.md §Blocking: copy the emitted HTML to
`~/.claude/paper-theater/blocking/maps/<slug>.html`, add or update the row in
`index.md` beside it, and regenerate `library.html` from the index using
`assets/library.html` (same payload-injection pattern). Removing or renaming
a map happens here in chat: delete/rename the file AND its row, regenerate.

## Step 4. Enter the guide

Announce the map is live and hold a thin loop — the intelligence is reasoning
over the model, not a menu. `open <node-id>` (or any named part): explain it
from its dossier PLUS the full source model, trace its cone, attack and defend
the modeling choice, propose alternatives, or draft slide / speaker-note
content for it. `flags`: list the problems, sharpest first. `present`: narrate
the graph in `meta.order`, source → result, one part per beat — the same order
the explorer's presentation mode steps through. Each dossier's "Ask Claude"
block generates exactly these prompts, so a user arriving from the HTML lands
in this loop seamlessly.

# Constraints

- **Honor the map/guide split.** The HTML never pretends to chat; every
  dossier hands over a ready-to-paste prompt instead. The guide never
  redescribes what the map already shows — it argues.
- **Parts, not blocks.** If nodes are theorem-sized the extraction has failed;
  script owns that altitude. ρ is a node; "Section 2" is not.
- **Few sharp flags beat many weak ones.** Every flag targets a specific node
  or edge; an untargeted or hedged flag does not ship.
- **Self-contained or dead.** No CDN, fonts, fetch, or external anything — the
  artifact must render offline and under strict CSP, exactly as shipped.
- **Data-driven template.** Any model must render. Never hand-edit the emitted
  HTML beyond the graph-data payload; template fixes go to `assets/` (bump
  this skill's version).
- **Reuse the disc alphabet.** Ring colors are the suite's v/p/h/c/s/o at the
  preamble's exact RGB. blocking never changes a disc — that is tryout's lane;
  never mix alphabets in one graph.
- **Do not restate format.md.** Read it each run; the schema and conventions
  live there.
