# Round 197 conductor report reconciliation

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Starting graph SHA-256:
  `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
- Status: conductor selection of the smallest candidate; not accepted
  mathematics before independent seam review and a valid State Patch

## 1. Common exact algebra

All three reports independently recover the same four gcds.  If

\[
 d=g\alpha,\qquad d'=g\beta,\qquad (\alpha,\beta)=1,
\]

then at the four proposed allocation corners they are

\[
 g,\qquad g(m,\beta),\qquad g(\alpha,m'),\qquad g(m,m').
\tag{197.R1}
\]

Thus the displayed three cross-coprimalities are necessary and sufficient
for a same-\(g\) rectangle.  The swaps then commute, preserve the two
endpoint products, and preserve the two physical defects.  Relative to
the original character weight the four multipliers are

\[
 (1,s_0,s_1,s_0s_1),\qquad
 s_0=\chi_4(\alpha m),\quad s_1=\chi_4(\beta m').
\tag{197.R2}
\]

On \(s_0=s_1=-1\) the table is the alternating rectangle, multiplied by
the common corner sign \(\chi_4(\alpha\beta)\).  The common sign must be
retained but has no power cost.  This sector implies \(4\mid r\); the
converse is false because \(s_0=s_1=+1\) also gives \(4\mid r\).

For the actual zero-extended endpoint values the rectangle factors
exactly:

\[
 \{\lambda_{N+r}(g\beta)-\lambda_{N+r}(gm')\}
 \overline{\{\lambda_N(g\alpha)-\lambda_N(gm)\}}.
\tag{197.R3}
\]

This is an algebraic identity even when an endpoint value is zero.  Zero
extension does not, however, turn a support jump into a smooth
difference, and it cannot replace a corner whose recomputed gcd differs
from \(g\).

## 2. Exact scope restriction

The full rectangle is much narrower than the launch shadow.  In the plus
primitive chart

\[
 (\alpha,m')=(\kappa U,\kappa v)=\kappa,
\]

and in the minus chart

\[
 (m,\beta)=(\kappa v,\kappa U)=\kappa.
\]

Therefore every genuine opposing four-corner orbit has

\[
 \boxed{\kappa=1.}
\tag{197.R4}
\]

It cannot estimate the open packets \(2\le\kappa<D_L\).  This is the
first exact boundary of the full four-corner proposal.

## 3. Strongest lawful repair

The lower edge of the rectangle needs fewer hypotheses.  On

\[
 P_0=P_2\mathbf1_{(m,\beta)=1}
          \mathbf1_{\chi_4(\alpha m)=-1},
\tag{197.R5}
\]

the lower allocation swap is a two-cycle and gives the exact actual-
coefficient difference

\[
 \lambda_{N+r}(g\beta)
 \overline{\lambda_N(g\alpha)-\lambda_N(gm)}.
\tag{197.R6}
\]

The conductor selects only the symmetric common-sharp-cell submask
\(P_{\rm cc}\subset P_0\).  It requires the two lower allocation inputs
\((m,g\alpha)\) and \((\alpha,gm)\) to have the same explicitly named
sharp literal code: support, shell, cone, profile branch, floor, star,
half weight, hard sample, cell, crossing, endpoint trace, sign, and every
other discontinuous or zero-extension state.  The code is defined from
literal predicates, not from whether the complete coefficient happens to
vanish.  The Round-184 selector and the normalized one-dimensional BV
profile are treated separately.

On this submask the certified smooth part has difference
\(O_\varepsilon(D_L/L\,X^\varepsilon)\).  The raw physical count is

\[
 D_L\sum_{\kappa\ll L}(1+L/\kappa)^2
 \ll D_LL^2X^\varepsilon.
\tag{197.R7}
\]

Hence the smooth term costs

\[
 {D_L\over L}\,D_LL^2X^\varepsilon
 =D_L^2LX^\varepsilon\ll L^2X^\varepsilon.
\tag{197.R8}
\]

For the normalized BV profile, telescoping gives

\[
 \sum_{|a-b|\le D_L}|\eta(a)-\eta(b)|
 \ll D_L^2\operatorname{Var}(\eta).
\tag{197.R9}
\]

There are \(O(LX^\varepsilon)\) upper completions per lower pair, so the
BV term has the same \(D_L^2L X^\varepsilon\) target.  The residual
selector is invariant except when exactly one selected prime lies in the
bounded integer \(g\); the accepted logarithmic-gap audit removes this
case for all large \(L\), and the finitely many remaining shells are paid
absolutely.

The pairing is made on the complete outer physical even-shift aggregate.
Monotone and low-height orbit exits are already absolutely target-safe.
The accepted Round-193/Round-195 masked-operator passage permits every
Round-187--Round-192 safe projector to be rerun on \(P_{\rm cc}W\), with
the transported mask commutator, births, deaths, carries, both \(T\)
branches, full anchors, cells, crossings, phases, conjugation, and zero
extensions retained.  Subtracting the deletion-stable Round-195 safe
packet union then also proves the exact intersection of this physical
sector with the open packet complement.

## 4. Exact complement and the no-go boundary

The physical first-failure partition is

\[
\begin{aligned}
 P_{g\mathrm f}&=P_2\mathbf1_{(m,\beta)>1},\\
 P_{s\mathrm f}&=P_2\mathbf1_{(m,\beta)=1}
              \mathbf1_{\chi_4(\alpha m)\ne-1},\\
 P_{\partial\mathrm{lit}}&=P_0(1-C_{\mathrm{lit}}),
\end{aligned}
\tag{197.R10}
\]

and

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\mathrm{lit}}
       \ \dot\cup\ P_{s\mathrm f}\ \dot\cup\ P_{g\mathrm f}.
\tag{197.R11}
\]

No report proves any of the last three terms target-safe.  In particular,
a sharp ratio face aligned with the swap-fixed line has

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)<0
 \qquad(\alpha\ne m),
\tag{197.R12}
\]

so every one of the \(O(LD_L)\) lower-close pairs may cross it.  After
upper completion this restores the full \(D_LL^2X^\varepsilon\)
capacity.  The current literal interface contains neither a complete
face-by-face transversality theorem uniform in real \(X\) nor branch
continuity across every aligned face.  This falsifies an automatic
\(O(D_L^2)\) sharp-face collar claim.  It is a method-capacity statement,
not a lower bound or nonvanishing claim for the actual coefficient.

## 5. Reconciliation decision

The blind report correctly identifies the first unsupported whole-sector
step: a support or sharp-field exit leaves an undifferenced endpoint
coefficient.  The hostile report independently confirms the gcd table,
the \(\kappa=1\) restriction, the common-cell repair, and the aligned-face
self-return.  The literal report supplies the missing outer count,
normalized-BV ledger, selector audit, masked-core passage, and exact
Round-195 subtraction for the narrow repair.

Accordingly the smallest candidate is the common-sharp-cell lower
allocation commutator sector, together with the route-scoped no-go for
the full four-corner and full \(P_0\) sectors.  No nonemptiness, density,
or positive coefficient mass is asserted.  The candidate must receive
independent algebra/literal and power/operator/scope reviews before any
graph mutation.

Because the frozen exit-label list contains no common-cell-specific
label, the round's truthful terminal label is
`p2_four_corner_orbit_boundary_self_return_no_go`.  A subordinate strict
sector may still be promoted if it passes review.  The label
`strict_p2_four_corner_allocation_commutator_sector` is not used for the
whole rectangle.
