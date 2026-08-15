# Round 73 conductor adjudication

## Decision

Promote only an exact residual off-diagonal reduction.  Do not extend the
target-safe conductor range beyond

\[
 T\leq C\leq J^{32/45}=X^{16/45}.
\]

For the remaining fixed-interior range

\[
 J^{32/45}<C\leq J,
\]

the energy diagonal is already target-safe.  The complete obstruction is
therefore the signed accumulation of the actual off-diagonal layers.  The
round isolates that correlation exactly, but proves no estimate for it.
The fourth-derivative, continuous-Hessian, exponent-pair, reciprocal-fraction,
and phase-matched spectral routes all fail at an explicitly audited seam.

## Exact accepted reduction

For a fixed compatible nonaxial \(k=\rho\sigma=O(1)\), local class
\(\kappa\in\{1/4,1/2,1\}\), and endpoint orientation, let
\(\mathcal Z_b\) be the half-open one-count set of exact cells in (73.3),
put

\[
 c_{b,z}=r+4b\ell,
 \qquad
 a_{b,z}=u_{b,r,k}^{(\kappa)}
 w_{b,r,\nu,k}^{(\kappa)}(\ell),
\]

and write

\[
 \mathcal E_{C,k}^{(\kappa)}
 =\sum_{b\asymp C/T}
 \left|\sum_{z\in\mathcal Z_b}
 a_{b,z}e\!\left(\pm A_{\kappa,b}/c_{b,z}\right)\right|^2.
\]

Exact expansion gives

\[
 \mathcal E_{C,k}^{(\kappa)}
 =\mathcal D_{C,k}^{(\kappa)}
  +\mathfrak H_{C,k}^{(\kappa)},
\]

where

\[
 \mathcal D_{C,k}^{(\kappa)}
 =\sum_b\sum_z|a_{b,z}|^2
 \ll_\varepsilon X^\varepsilon BC
 =X^\varepsilon C^2/T
 \leq X^\varepsilon J^2/T,
\]

and

\[
 \mathfrak H_{C,k}^{(\kappa)}
 =\sum_b\sum_{z\ne z'}a_{b,z}\overline{a_{b,z'}}
 e\!\left(\pm A_{\kappa,b}
 \left(c_{b,z}^{-1}-c_{b,z'}^{-1}\right)\right).
\]

Consequently the residual energy is reduced, without changing a coefficient,
to

\[
 \mathfrak H_{C,k}^{(\kappa)}
 \ll_\varepsilon X^\varepsilon J^2/T.
\]

Every fixed nonzero denominator-offset layer has the same safe absolute
capacity \(O_\varepsilon(X^\varepsilon BC)\); the open issue is their
coherent accumulation.  This is a strictly smaller exact target than the
unexpanded row energy.

## Audited failures of elementary upgrades

On one exact cell,

\[
 |f^{(4)}(\ell)|\asymp J^2/T^5=Q^{-5/2}.
\]

One more \(A\)-process gives, after all \(O(Q)\) Farey pieces are retained,

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \{CQ^{-5/28}+C^{3/4}Q^{3/7}+C^{1/2}Q^{1/2}+Q\}.
\]

The tempting first term cannot be isolated: the second term would meet the
energy target only for \(C\leq J^{116/175}<J^{32/45}\).  Taking the
cellwise minimum with the accepted third-derivative bound gives no extension
at the current boundary.

The exact continuous phase has

\[
 \det\nabla^2(A_{\kappa,b}/c)
 =\frac{J^4}{c^4}(3\eta-1)(1+\eta)^3,
 \qquad \eta=\frac{\sqrt{\kappa k}}{bJ}=o(1),
\]

so it is uniformly nondegenerate in the actual range.  This does not prove a
lattice estimate: absolute summation of the two-dimensional Poisson aliases
has capacity \(J^2/T\), equal to the original point count at \(C=J\), and
the exact inverse/even local unit cannot be discarded.

The statement-only rederivation independently verifies that Farey-neighbor
labels are ownership labels, not orthogonality variables.  Even an optimistic
separate square-root gain over residues and over \(b\) leaves a further
factor \(J^{1/30}\) at \(C=J\).  This is a mechanism budget, not a claimed
lower bound.

## Exponent-pair and transition seam

Bourgain's primary exponent pair
\((13/84+\varepsilon,55/84+\varepsilon)\) applies to the pure reciprocal
phase on one ambient-\(T\) progression and, by Abel summation, to one actual
BV cell.  Its cap is

\[
 H_{\rm Bou}=Q^{13/42}T^{55/84}=J^{31/60}.
\]

The accepted packet gives BV separately on \(O(Q)\) cells, not a globally
glued BV weight on each of the \(O(B)\) residue progressions.  The lawful
row bound is therefore only

\[
 |S_b|\ll_\varepsilon X^\varepsilon
 \min\{C,QH_{\rm Bou}\}
 =X^\varepsilon\min\{C,J^{11/12}\}.
\]

The stronger \(CQ^{-5/24}\) row, and the resulting range
\(C\leq J^{13/18}\), are conditional on the unproved gluing estimate

\[
 \sum_{r\bmod4b}
 \bigl(\|W_{b,r}\|_\infty+\operatorname{Var}W_{b,r}\bigr)
 \ll_\varepsilon BX^\varepsilon.
\]

Thus no exponent-pair range is promoted.

## Phase-matched spectral return

In an ideal smooth odd model, \(c\)-Poisson with \(q=4b\) has
\(n\asymp Q^2\).  One Kuznetsov branch cancels the secondary phase, and
the remaining spectral coefficient sum is

\[
 V_f=\sum_{n\asymp Q^2}
 \lambda_{f,\mathfrak a}(n)V_f(n/Q^2)e(-J\sqrt n).
\]

The exact level-four Voronoi normalization switches cusps and localizes the
dual index to

\[
 |m-X|\ll T,
\]

with transform factor \(Q^{3/2}/J^{1/2}\).  The required input becomes the
pointwise short-coefficient estimate

\[
 \sum_{|m-X|\ll T}\lambda_{f,\mathfrak b}(m)\Psi_{f,C}(m)
 \ll_\varepsilon J^{1/2+\varepsilon}=X^{1/4+\varepsilon}.
\]

The trivial length \(T\) misses this by
\(T/\sqrt J=J^{1/10}=X^{1/20}\), independently of \(C\).  The audited
primary resonance formula has the same error scale; current Kloosterman
moments, fixed-modulus bilinear estimates, reciprocal-fraction estimates,
and spectral large sieves do not prove the required moving level-four
short sum.  Moreover the actual cell weights have not yet been glued into
the common smooth Kuznetsov test, the even lifts need separate cusps, and
the zero-index axes remain open.  This spectral chain is retained only as a
conditional model reduction, not as accepted all-class algebra.

## Evidence reconciliation and state recommendation

The discovery report supplies the fourth-derivative, Hessian, Poisson,
Kuznetsov, and Voronoi ledgers.  The clean statement-only report verifies
the diagonal, near-diagonal, ownership, budget, and actual-range Hessian
controls without reading claimant material.  The hostile/source report
independently verifies Bourgain's ambient-scale scope, the transition
gluing failure, the exact level-four switched-cusp resonance, and the
hypothesis failures of every proposed imported theorem.  The three reports
therefore agree on a narrow exact reduction and on independently identified
failure seams; no estimate is selected by vote.

Create a proved internal reduction for the exact off-diagonal target.
Record the fourth-derivative, Hessian-only, cellwise Bourgain-gluing, and
black-box spectral-combination failures.  Keep
\(J^{32/45}<C\leq J\), the upper axial band, cone edges, the complete
fixed-interior wavelet, \(M9\!-!M1\), \(M9\!-!M2\), \(M9\), and the
Gauss-circle exponent open.

