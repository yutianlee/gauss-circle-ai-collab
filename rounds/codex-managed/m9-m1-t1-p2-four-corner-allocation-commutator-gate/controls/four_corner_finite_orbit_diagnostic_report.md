# Round 197 finite four-corner orbit diagnostic

## Purpose

This bounded computation tests only whether the proposed four-corner arithmetic
conditions are jointly nonempty in a small finite search.  It is a falsification
control for an immediately empty model sector, not evidence for an asymptotic
estimate.

## Exact procedure

The archived script
`controls/four_corner_finite_orbit_diagnostic.py` uses integer arithmetic and
searches the shells

\[
40,60,80,120,160,240,320.
\]

For each shell it checks the displayed dyadic-size and cone inequalities, odd
and squarefree restrictions, the lower-close and upper-far inequalities,
coprimality needed by the two independent swaps, the two negative character
ratios, a positive even shift, and the opposing-sign condition at all four
formal corners.  The exact command and stdout are preserved in
`controls/four_corner_finite_orbit_diagnostic_output.txt`.

## Outcome

Pass for the deliberately weak control criterion: at least one tuple survives
all coded conditions.  Three examples were found, at shells 160, 240, and 320.
The first is

\[
(L,D_L,g,U,v,w,S,H,r)=(160,13,5,71,57,8,10,2,20),
\]

with four corners

\[
\begin{aligned}
&(355,73,455,57),\qquad (365,71,455,57),\\
&(355,73,285,91),\qquad (365,71,285,91).
\end{aligned}
\]

## Interpretation and limits

The diagnostic establishes only finite combinatorial compatibility of the
conditions implemented by the script.  It does not verify the literal
coefficient formula, nonzero support of every allocation, projector/source
membership, selector-cell stability, bounded-variation seam estimates, an
exact complement decomposition, positive density, or any uniform asymptotic
bound.  The search ranges are truncated and the dyadic shell model is only a
finite proxy.  Accordingly this output cannot certify any lemma or alter the
claim graph; it is retained solely as a control result for Round 197.
