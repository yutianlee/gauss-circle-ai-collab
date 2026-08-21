# Round 109 synthesis: blockwise scalar owner completion

Campaign: m9-m2-blockwise-owner-completion

Starting graph SHA-256:
f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d

Resulting graph SHA-256 after the validated State Patch:
33bf8e043cb8a1e0852b7f98941ee6186f798ed40124525de3d0373269019397

## 1. Frozen objective

The round asked whether every previously proved hard-top \(M2\) owner can
be inserted and subtracted on each fixed dyadic scalar block with

\[
 \mathfrak Q_B^{\mathrm{res}}
 =\mathfrak Q_B^{\mathrm{comp}}-\sum_\nu\mathfrak O_{B,\nu},
 \qquad
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.
\]

This is stronger than the accepted signed aggregate owner bound and is
the exact norm required to make fixed-\(K\) linear completion lawful.
The fixed-\(a\) Gram, either completed directional estimate, and all
smooth packets were excluded from promotion.

The campaign produced one statement-only norm rederivation, one literal
owner formalization, one hostile seam audit with a terminal-metric
follow-up, four conductor reviews, and a complete control ledger.

## 2. Abstract norm gate

For

\[
 \Delta_B=\sum_\nu O_{B,\nu},\qquad
 D_{\mathrm{block}}=\sum_B|\Delta_B|,\qquad
 C_{\mathrm{own}}=\sum_{B,\nu}|O_{B,\nu}|,
\]

one only has

\[
 \left|\sum_{B,\nu}O_{B,\nu}\right|
 \le D_{\mathrm{block}}\le C_{\mathrm{own}}.
\]

Finite countermodels show that a signed aggregate, an unnormalized row
energy, or a positive Gram estimate does not reverse either inequality.
Thus no earlier aggregate estimate licenses completion. The successful
proof instead estimates every literal owner in the required scalar
norm.

## 3. Exact metric reconstruction

Let \(d(t)=\|t\|\). Choose a fixed smooth nonincreasing \(\eta\), equal
to one on \([0,1/2]\) and zero on \([1,\infty)\), and define

\[
 V_R(t)=\eta(Rd(t)),\qquad W_R(t)=V_R(t)-V_{2R}(t).
\]

For dyadic \(G_*\asymp G\), one has pointwise

\[
 \boxed{
 1_{t\notin\mathbb Z}
 =\sum_{\substack{1\le R<G_*\\R=2^j}}W_R(t)
   +V_{G_*}(t)-1_{t\in\mathbb Z}.}
\tag{109.1}
\]

The last term is the exact-center scalar atom. All other members are
smooth, including the terminal \(V_{G_*}\), and

\[
 |\widehat W_R(\nu)|+|\widehat V_R(\nu)|
 \ll_M R^{-1}(1+|\nu|/R)^{-M}.
\tag{109.2}
\]

For odd \(g\asymp G\) and \(R\le G_*\asymp G\), the required Fourier
half-moments are \(O(G^{1/2})\) and \(O(G^{-1/2})\). This settles the
prior terminal reconstruction seam. The metric density is the zero
Fourier coefficient of a smooth member; it is not the original
Round-77 Poisson zero mode.

## 4. Literal one-count owner table

Use one orientation \(a<b\) and one outer \(2\Re\). On the common finite
atom space \(z=(B,a,b,k,g)\), with the same complete collared coefficient
and the same half-open \(k\)-lattice, apply the first matching predicate:

1. Round-77 endpoint, collar, original-mode, equality, or nonstationary
   complement;
2. primitive square ray, including its metric and exact-center pieces;
3. primitive nonsquare exact center;
4. positive-safe block, with the fixed \(\rho\)-boundary and equality on
   the safe side;
5. residual singleton \(q=1\);
6. residual prescribed-polylogarithmic \(q>1\) shell;
7. residual.

The Round-75 diagonal is separate. This priority proves coefficient by
coefficient

\[
 \mathfrak Q_B^{\mathrm{res}}
 =\mathfrak Q_B^{\mathrm{comp}}-\sum_\nu\mathfrak O_{B,\nu}.
\tag{109.3}
\]

Physical completion is only zero extension of the unchanged collared
coefficient. It does not erase moving collars, alter endpoint weights,
or evaluate a sharp owner at a noninteger saddle.

## 5. Outside-absolute owner norm

The owner-specific bounds are:

- Round 77 is absolute per ordered pair: endpoint and collar capacity is
  bounded, equality and nonstationary pieces cost at most logarithmically,
  and finite dyadic refinement adds only logarithms.
- On a primitive square ray, (109.1)--(109.2) turn every smooth metric
  member into a sampled-\(k\) phase of nonzero odd frequency
  \(n=|g-2\nu|\ge1\). Accepted sampled variation and reciprocal
  second-derivative summation give
  \(O_\varepsilon((L+1)X^\varepsilon)\) per lifted square triple, and
  the \(O(L\log L)\) triple count is target-safe.
- Exact square centers cost \(O_\varepsilon(L^{3/2}X^\varepsilon)\);
  exact nonsquare centers cost \(O_\varepsilon(LX^\varepsilon)\).
- Positive-safe blocks satisfy
  \(A\sqrt G\sqrt J D^{3/2}=\sqrt{ALJD^3}\ll L^2\).
- The singleton energy gives

\[
 \left|\sum_{a\asymp A}F_a(1)\right|
 \le A^{1/2}\left(\sum_a|F_a(1)|^2\right)^{1/2}
 \ll_\varepsilon L^2X^\varepsilon.
\]

- The fixed-\(q\) shell gives

\[
 \left|\sum_{a,q}(-1)^qF_a(q)\right|
 \le(AD)^{1/2}\left(\sum_{a,q}|F_a(q)|^2\right)^{1/2}
 \ll_\varepsilon DL^2X^\varepsilon,
\]

  used only for one prescribed polylogarithmic range and absorbed by
  \(X^\varepsilon\).

Smooth difference localization has bounded Fourier \(L^1\)-cost, and
Möbius separation costs \(\sum d^{-3/2}<\infty\). These preserve proved
scalar norms; no sharp pair owner is silently factorized. Therefore

\[
 \boxed{
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.}
\tag{109.4}
\]

Consequently

\[
 \sum_B|\mathfrak Q_B^{\mathrm{res}}|
 \le\sum_B|\mathfrak Q_B^{\mathrm{comp}}|
   +O_\varepsilon(L^2X^\varepsilon),
\tag{109.5}
\]

and, distinctly,

\[
 \left|\sum_B\mathfrak Q_B^{\mathrm{res}}\right|
 \le\left|\sum_B\mathfrak Q_B^{\mathrm{comp}}\right|
   +O_\varepsilon(L^2X^\varepsilon).
\tag{109.6}
\]

## 6. Conductor decision

Promote one narrow internal connector: exact smooth metric telescoping,
the disjoint scalar owner identity (109.3), the outside-absolute norm
(109.4), and its blockwise and signed corollaries (109.5)--(109.6).

Reject aggregate-owner bounds as substitutes for the blockwise norm,
double orientation counting, a smooth terminal without the exact-center
subtraction, deletion of moving collars during physical completion, and
commuting scalar completion through Fejér or Gram operators.

Neither completed estimate

\[
 \sum_B|\mathfrak Q_B^{\mathrm{comp}}|
 \ll_\varepsilon L^2X^\varepsilon,
 \qquad
 \left|\sum_B\mathfrak Q_B^{\mathrm{comp}}\right|
 \ll_\varepsilon L^2X^\varepsilon
\]

is proved. The exact metric functional calculus remains equal-capacity.

## 7. Global proof status and next interface

No global exponent changes. The strongest certified pointwise theorem
remains the repaired, source-audited Li--Yang exponent

\[
 \theta_{\mathrm{LY}}
 ={3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots,
\]

and the strongest uniform theorem proved entirely inside the project
remains exponent \(1/3\).

The fixed-\(a\) actual Gram, canonical hard density-discrepancy energy,
hard signed cone, balanced and unbalanced smooth \(M2\) packets,
\(M9\!-M2\), \(M9\!-M1\), endpoint uniformity, \(M9\), and the quarter
target remain open. The new connector removes the owner-completion
ambiguity: the next hard-top attack may use the completed directional
scalar vector, but it must prove real cross-\(q\) cancellation rather
than gain capacity from another invertible transform.
