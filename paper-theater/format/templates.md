# paper-theater :: templates.md (v1.0)

Verbatim starting points. Replace `{{placeholders}}`; never restate these in a
SKILL.md. Conventions (discs, caps, labels, directories) live in `format.md`.

## stage main file — `staging/stage-NNN-slug.tex`

```latex
\documentclass[10pt,a4paper]{article}
\input{preamble}

% --- document-set macros (define BEFORE \begin{document}) ---
\newcommand{\protonum}{{{NNN}}}
\newcommand{\protofield}{{{econ / OR / IS}}}
\newcommand{\protodate}{\today}
\newcommand{\prototitle}{{{working title}}}
\newcommand{\protosubtitle}{{{one-line framing}}}
\newcommand{\protopunch}{{{the ONE-LINE mechanism — what the paper buys you}}}
\newcommand{\protospine}{Lemma~\ref{lem:{{key}}} $\to$ Proposition~\ref{prop:{{key}}}
  $\Rightarrow$ Claim~\ref{clm:{{key}}}}  % full names, real \ref's

\renewcommand{\theaterstamp}{paper-theater \textperiodcentered\ stage \textperiodcentered\ v1.0}
\begin{document}
\stagehead   % compact header — no cover page; body starts here

\begin{abstract}
\noindent {{The hook, not a summary: the question; what is new; why it matters.}}
\end{abstract}

\section{Setup}\label{sec:setup}
% Run-in \paragraph modules, in this order; add extras only as the model needs.
\paragraph{Players.}\noindent {{agents and their primitives}}
\paragraph{Timing.}\noindent {{who moves when}}
\paragraph{Strategies.}\noindent {{choice sets}}
% optional: \paragraph{Payoffs.} \paragraph{Information.} \paragraph{Solution concept.}

\begin{assumption}[{{v|p|h|c}}]\label{ass:{{key}}}{{the load-bearing restriction}}\end{assumption}
\Intuition {{why this is the natural minimal restriction — <= 2 sentences}}

\section{Building blocks}\label{sec:blocks}

% ---- one block per spine node; blocks are nodes, not quotas ----
\blocktag{BLOCK {{n}} \textperiodcentered\ {{short name}}}
\begin{proposition}[{{v|p|h|c}}]\label{prop:{{semantic-key}}}
{{tight statement — primitives in, claim out}}
\end{proposition}
\Intuition {{the real mechanism, <= 2 sentences, never a restatement}}

{\footnotesize\Proofsketch {{the move, one line}}. Check \checkmark\ (symbolic):
{{exactly what staging/checks/ established}}.\par}

{\footnotesize\Risk {{the single step most likely to break}}.\par}

\Uses Assumption~\ref{ass:{{key}}}.
\Next {{<= 1 sentence: what this feeds and why to keep reading}}.
% ---- end block ----

\section*{Open joints}
\begin{itemize}\setlength{\itemsep}{1pt}
  \item {{what has no full argument yet}} (would promote \disc{p}$\to$\disc{v}).
  \item \textbf{Load-bearing:} Assumption~\ref{ass:{{key}}} — {{what fails without it}}.
  \item \textbf{Could break:} {{the joint most likely to fail under scrutiny}}.
\end{itemize}

\appendix
\input{proofs}
\input{skeleton}

\bibliographystyle{plainnat}
\bibliography{refs}   % omit if no source is actually leaned on
\end{document}
```

## script main file — `scripts/<slug>/script-<slug>.tex`

```latex
\documentclass[10pt,a4paper]{article}
\input{preamble}
\newcommand{\protodate}{\today}
\newcommand{\prototitle}{{{paper title}}}
\newcommand{\protosubtitle}{{{Authors \textperiodcentered\ Venue \textperiodcentered\ Year}}}
\renewcommand{\theaterstamp}{paper-theater \textperiodcentered\ script \textperiodcentered\ v1.0}
\begin{document}
\scripthead

\noindent{\footnotesize\textbf{QUESTION.}\ {{the paper's question, one line}}\quad
\textbf{ANSWER.}\ {{its answer, one line}}\par}

\section*{Spine (in the paper's own order)}

% ---- one block per load-bearing element, s = proved in paper, o = imported ----
\blocktag{{{Section 3}} \textperiodcentered\ {{short name}}}
\begin{proposition}[s]\label{prop:{{semantic-key}}}
{{FAITHFUL restatement — bugs and overclaims included}}
\end{proposition}
\Anchor{{{Prop 2, eq. (14), p. 9}}}\\
\Role {{one line: what work this does in the paper}}
\Next {{optional, <= 1 sentence}}
% ---- end block ----

\section*{Open joints (reader's notes)}
\begin{itemize}\setlength{\itemsep}{1pt}
  \item {{gaps, suspected errors, silent assumptions — FLAGGED, never fixed}}
\end{itemize}

\input{skeleton}   % optional: one-page map, s/o discs
\end{document}
```

## `proofs.tex` (stage)

```latex
% staging/proofs.tex — sketch tier, not full rigour. Whole section footnotesize.
\section{Proof sketches}\label{app:proofs}
\begingroup\footnotesize
\begin{myproof}{Proposition}{\ref{prop:{{semantic-key}}}}
{{step sequence; the key mechanism explicit; the hard step flagged}}.
Check \checkmark\ (symbolic): {{what checks/{{file}}.py established}}.
\end{myproof}
\endgroup
```

## `skeleton.tex` (stage and, optionally, script)

```latex
% staging/skeleton.tex — the one-page dependency-flow map (20-second rule).
\clearpage
\section*{Skeleton}
\begin{tcolorbox}[colback=gray!2, colframe=gray!55, boxrule=0.6pt, arc=3pt]
{\footnotesize \disc{v}~Verified \textperiodcentered\ \disc{p}~Plausible
 \textperiodcentered\ \disc{h}~Heuristic \textperiodcentered\ \disc{c}~Conjectured
 \hfill read top-to-bottom: each step follows from those above\par}
\medskip

\noindent\disc{{{key}}} \textbf{Assumption~\ref{ass:{{key}}}} — {{plain-English role}}\\
{\footnotesize\hspace*{1em}{{one concrete detail: the key condition or formula}}}\par
\begin{center}$\downarrow$ {\footnotesize so}\end{center}
\noindent\disc{{{key}}} \textbf{Lemma~\ref{lem:{{key}}}} — {{role}}\\
{\footnotesize\hspace*{1em}{{detail}} {{(needs \textbf{Assumption~\ref{...}}) — only if non-adjacent}}}\par
\begin{center}$\downarrow$ {\footnotesize then}\end{center}
\noindent\disc{{{key}}} \textbf{Proposition~\ref{prop:{{key}}}} — {{role}}\\
{\footnotesize\hspace*{1em}{{detail}}}\par
\end{tcolorbox}
```

## `verification.md` (stage → tryout)

```markdown
# Verification contract — stage-NNN-slug (v1.0)

| label | Current disc | Symbolic check run (checks/) | Proposed numeric check |
|-------|--------------|------------------------------|------------------------|
| prop:{{key}} | Plausible | {{checks/prop_{{key}}.py: what it settled}} | {{random instances over {{domain}}; hunt near {{boundary}}}} |

## Notes
- Cheap: {{...}}  Expensive: {{...}}
- Most likely to break: {{label}} — {{why}}
- Existing evidence: {{inputs/ code that already backs a result, if any}}
```

## `tryout-report.md` (tryout)

```markdown
# Tryout report — stage-NNN-slug — {{date}}

| label | probes run | outcome | skeptic verdict | disc before → after |
|-------|-----------|---------|-----------------|---------------------|

## Breaking instances
{{label}}: {{parameter point, seeded; what failed; suggested fix (NOT applied)}}

## Confidence distribution
before: {{V/P/H/C}} → after: {{V/P/H/C}}
```

## Restage changelog (appended to the run's console summary and the registry row)

```markdown
## Restage changelog — stage-NNN-slug — {{date}}
- kept   : {{label}} (unchanged; disc {{x}} survives)
- reset  : {{label}} ({{what changed}}; {{x}} → c, re-earned {{y}} this run)
- new    : {{label}} (entered at {{x}})
- deleted: {{label}} ({{why}})
```

## Canon entry — `~/.claude/paper-theater/canon/entries/<slug>.md`

(Schema in format.md §Canon. Frontmatter + `## Lesson` + `## Spine`.)

## rehearse main file — `rehearsal/rehearse-<slug>.tex`

```latex
\documentclass[12pt,a4paper]{article}
\input{rehearsal-preamble}
\begin{document}

\noindent{\Large\bfseries Rehearsal: {{paper short title}}}\\
{\itshape\color{gray!75}{{Authors \textperiodcentered\ Venue \textperiodcentered\ Year}}}\par
\medskip
\noindent {{2–3 sentences: what the paper does and which tools it runs on.}}\par
\medskip
\noindent\textbf{Tools in this rehearsal:}\ {{tool 1}} \textperiodcentered\ {{tool 2}} \textperiodcentered\ ...

\toolpage{{{Tool name, e.g. Normal--normal updating}}}{{{one line: where the paper uses it}}}
\Statement {{minimal clean statement, general form}}\par\medskip
\InThisPaper {{the paper's exact instantiation — its notation, its special case}}\par\medskip
\Worked {{a stripped numeric/symbolic example a reader can follow line by line}}\par\medskip
\Pitfall {{the standard way this tool is misused — omit if none}}\par\medskip
\begin{exercise} {{solvable from THIS page alone}} \end{exercise}
\begin{exercise} {{one step harder; connects to the paper's actual use}} \end{exercise}

% ... more \toolpage's, one tool per page ...

\solutionsection
\begin{solution}{1} {{full worked solution}} \end{solution}
\begin{solution}{2} {{...}} \end{solution}
\end{document}
```

## `verify.py` harness skeleton (tryout)

```python
"""tryout harness — stage-NNN-slug. Seeded; each check returns a verdict dict."""
import numpy as np
rng = np.random.default_rng(20260703)

def check_prop_key():
    """<label>: <claim in one line>. Probes: limiting / random / hunt."""
    fails = []
    # 1) limiting case by number ...
    # 2) random instances over the stated domain ...
    # 3) counterexample hunt: grid -> random -> optimizer toward the boundary ...
    return {"label": "prop:key", "verdict": "pass|fail|inconclusive",
            "earned": "v|p|h|c", "coverage": "...", "breaking": fails[:3]}

if __name__ == "__main__":
    for check in [check_prop_key]:
        print(check())
```
