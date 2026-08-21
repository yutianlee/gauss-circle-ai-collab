# Round 109 blind statement: blockwise owner completion

Let \(J=X^{1/2}\), \(1\le L\le J^{1/2}\), and let
\(\mathcal B_L\) be a family of \(X^\varepsilon\)-many dyadic blocks
\(B=(A,D,K,G,R,\sigma)\).  For each block suppose an oriented scalar
hard contribution has the exact form

\[
 Q_B^{\mathrm{hard}}
 =Q_B^{\mathrm{full}}-\sum_{\nu\in\mathcal O}O_{B,\nu}.
\tag{109.1}
\]

Here \(Q_B^{\mathrm{full}}\) is obtained by completing a moving open
\(k\)-interval to a fixed dyadic lattice and by restoring physical
collars, entry/exit terms, equality modes, nonstationary modes, square
rays, exact centres, and already safe blocks exactly once.  The owner
sets are disjoint in the original scalar expansion.

The accepted information supplied to this task is only

\[
 E_L^{\mathrm{top}}
 =E_{\mathrm{owned},L}
  +2\Re\sum_{B\in\mathcal B_L}Q_B^{\mathrm{hard}},
\qquad
 E_{\mathrm{owned},L}\ll_\varepsilon L^2X^\varepsilon,
\tag{109.2}
\]

plus the fact that some individual owner families have separately
proved scalar or energy estimates.  The desired blockwise completion
gate is

\[
 \boxed{\quad
 \sum_{B\in\mathcal B_L}\sum_{\nu\in\mathcal O}
 |O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.
 \quad}
\tag{109.3}
\]

If (109.3) holds, any estimate
\(\sum_B|Q_B^{\mathrm{full}}|\ll_\varepsilon L^2X^\varepsilon\)
implies the same estimate for the hard residual.  A signed aggregate
bound for \(\sum_{B,\nu}O_{B,\nu}\), or a positive bound for
\(E_{\mathrm{owned},L}\), is not declared to imply (109.3).

At the algebraic separation level, smooth difference cutoffs have
bounded Fourier \(L^1\)-cost and the primitive condition may be
expanded by Möbius inversion with an absolutely summable weighted
cost.  Sharp pair-dependent owners need not be one-coordinate
projectors.  The exact question is whether the literal accepted owner
families admit (109.3), or whether one family supplies a rigorous
counterexample/no-go to that inference.

Derive the weakest sufficient owner-completion lemma, distinguish
scalar, row-energy, and Gram ownership, and identify the first
unsupported implication.  Do not use the Round-109 derivation packet,
candidate, proof graph, strategy, or another Round-109 report.
