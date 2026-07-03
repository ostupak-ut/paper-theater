---
name: canon
version: 1.0.0
description: Part of the paper-theater suite. canon manages the global exemplar library at ~/.claude/paper-theater/canon/ — the papers whose STRUCTURE the author has decided is worth imitating, each stored as a spine + shelf tags (field/subfield/techniques/shape) + a 1–2 line LESSON marked portable or field-bound. Admission normally happens through script's end-of-run gate; canon is the librarian: browse ("show my canon", "what's on the info-design shelf"), retrieve exemplars for a new idea ("which exemplars fit a screening model with Poisson arrivals"), add an entry directly from a paper the user names (delegating extraction to script), edit tags/lessons, and retire entries. TRIGGER on any request to view, search, query, curate, add to, or prune the canon / exemplar library, and on "is X in my canon?". SKIP for actually stripping a paper (script does that, including the admission gate); SKIP for generating prototypes (stage — stage does its own canon retrieval); SKIP for literary/religious/fandom canon questions and anything outside the exemplar library.
---

# Purpose

Keep the canon browsable, retrievable, and small enough to trust. The canon
is the author's structural taste made machine-readable — the mechanism by
which their curation, not the model's generic prior, steers what stage
builds. Schema and admission discipline live in
`~/.claude/skills/paper-theater/format/format.md` §Canon — read it every run;
never restate it.

# Procedure

## Step 0. Locate

Home: `~/.claude/paper-theater/canon/` (`index.md` + `entries/*.md`). If
absent, create both per format.md — an empty canon is a valid state; say so
rather than inventing entries.

## Browse / query

"Show my canon" → the index as a compact table (slug, venue+year,
field/shelf, shape, portable?, lesson-short). Shelf or technique queries →
filter rows, and offer the full entries on request. "Is X in my canon?" →
check by slug/title, answer directly.

## Retrieve (the operation stage depends on)

Given an idea or model description: match its field/shelf/techniques against
the index; return the 1–3 best entries WITH their lessons, flagging which
lessons are `portable: yes` (may cross shelves) vs field-bound (may not).
No match → say "no exemplars on this shelf yet" and name the nearest shelf —
never stretch a bad match; a wrong exemplar mis-calibrates stage worse than
none.

## Add

Direct additions delegate the spine work: if no script of the paper exists,
run (or offer to run) **script** on it, which ends in the admission gate.
Never write an entry from memory of a paper — the spine comes from an actual
extraction pass. The gate question is always format.md's: not "is it good"
but "**would you imitate its structure?**" — and the author answers it, not
the model.

## Edit / retire

Update tags, lessons, or portability on request (fix the entry AND its index
row — they never diverge). Retiring: move the entry to
`entries/retired/` rather than deleting, and drop the index row; taste
changes, and a retired entry documents that it changed. Periodically (any run
that touches ≥3 entries), sanity-check shelf discipline: a shelf with 20+
entries or an entry whose lesson no longer says anything ("well organized")
is flagged to the author for pruning.

# Constraints

- **No auto-admission, no entries from memory.** Every entry traces to a
  script run and an explicit author yes. The canon's value IS the human gate.
- **External published papers only.** The author's own unpublished drafts
  never enter (format.md rule) — pen-testing artifacts are not exemplars.
- **Entry and index never diverge.** Every edit updates both.
- **Retrieval is shelf-disciplined.** Field-bound lessons do not cross
  shelves; no match beats a stretched match.
- **The lesson is the payload.** An entry whose lesson is generic gets
  flagged, not padded — if there is nothing to steal, the paper does not
  belong on the shelf.
- **Do not restate format.md.** Schema lives there.
