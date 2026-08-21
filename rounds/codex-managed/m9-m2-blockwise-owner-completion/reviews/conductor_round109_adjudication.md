# Conductor adjudication: blockwise scalar owner completion

Campaign: m9-m2-blockwise-owner-completion

Starting graph SHA-256:
f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d

## Decision

Promote one narrow internal connector: the positive-orientation
hard-top M2 scalar admits an exact fixed-\(K\), unchanged-collar owner
completion with target-sized outside-absolute owner cost.  Also record
the weaker global signed completion as a corollary.  Do not promote an
estimate for the completed vector.

The statement-only report proves the sharp abstract norm hierarchy

\[
 \left|\sum_{B,\nu}O_{B,\nu}\right|
 \le \sum_B\left|\sum_\nu O_{B,\nu}\right|
 \le \sum_{B,\nu}|O_{B,\nu}|,
\]

and correctly rejects every aggregate-to-blockwise inference.  The
promotion instead uses literal owner-specific proofs: Round 77 is
absolute per ordered pair, square rays receive a new metric-resolved
scalar estimate, exact centres are absolute, safe blocks are positive,
and the short-row energies are converted with their exact Cauchy
factors.

## Exact metric and orientation normalization

Use one representative \(a<b\) and one outer \(2\Re\).  The conjugate
orientation is not separately summed.  Every dyadic lattice is
half-open, reciprocal saddle intervals are open, and genuine integer
equalities retain their inherited star or half weight.

For \(d(t)=\|t\|\), choose a fixed smooth decreasing \(\eta\), equal to
one on \([0,1/2]\) and zero on \([1,\infty)\), and put

\[
 V_R(t)=\eta(Rd(t)),\qquad W_R(t)=V_R(t)-V_{2R}(t).
\]

If \(G_*\asymp G\) is dyadic, then pointwise

\[
 \boxed{
 1_{t\notin\mathbb Z}
 =\sum_{\substack{1\le R<G_*\\R\ {\rm dyadic}}}W_R(t)
  +V_{G_*}(t)-1_{t\in\mathbb Z}.}
\tag{109.A1}
\]

The last term is the exact-centre scalar atom.  All other members are
smooth, including the terminal \(V_{G_*}\), and satisfy

\[
 |\widehat W_R(\nu)|+|\widehat V_R(\nu)|
 \ll_M R^{-1}(1+|\nu|/R)^{-M}.
\tag{109.A2}
\]

For odd \(g\asymp G\), \(R\le G_*\asymp G\), their two half-moments are
\(O(G^{1/2})\) and \(O(G^{-1/2})\).  Thus the metric density is retained
as the zero Fourier coefficient, while the original Round-77 Poisson
zero mode remains a different owner.  The hostile follow-up certifies
(109.A1)--(109.A2), including the terminal member and Round-108
functional calculus.

## One-count owner identity

On the common finite atom space \(z=(B,a,b,k,g)\), retain the same
complete collared coefficient and use the first applicable predicate:

1. Round-77 endpoint/collar/original-mode/equality/nonstationary
   complement;
2. primitive square ray, including its metric and exact-centre pieces;
3. primitive nonsquare exact centre;
4. positive-safe block, with the fixed \(\rho\)-boundary and equality
   assigned to the safe side;
5. residual singleton \(q=1\);
6. residual prescribed polylogarithmic \(q>1\) shell;
7. residual.

The Round-75 diagonal is separate and is never inserted into the
oriented sum.  With \(\mathfrak O_{B,\nu}\) the complete scalar sum on
one owner fibre, the priority partition proves coefficient by
coefficient

\[
 \mathfrak Q_B^{\rm res}
 =\mathfrak Q_B^{\rm comp}
  -\sum_\nu\mathfrak O_{B,\nu}.
\tag{109.A3}
\]

Physical completion means only zero extension of the unchanged
collared coefficient.  It does not erase a moving collar or evaluate an
owner at a noninteger saddle.

## Owner norm

The exact ledger is:

- Round 77: \(O(1)\) endpoint/collar capacity and
  \(O(\log(2+L))\) equality/nonstationary capacity per ordered pair,
  before the pair sum.  Dyadic subdivision costs only logarithms.
- Square metric members: after Fourier expansion the phase frequency is
  \(n=|g-2\nu|\ge1\).  Sampled \(k\)-BV, reciprocal
  second-derivative summation, and (109.A2) give
  \(O_\varepsilon((L+1)X^\varepsilon)\) per actual lifted triple.
  The \(O(L\log L)\) triple count is target-safe.
- Exact square centres: divisor counting and the Round-78 supremum give
  \(O_\varepsilon(L^{3/2}X^\varepsilon)\), hence \(O(L^2X^\varepsilon)\).
  Exact nonsquare centres have the accepted
  \(O_\varepsilon(LX^\varepsilon)\) absolute bound.
- Safe blocks: \(A\sqrt G\sqrt J D^{3/2}
  =\sqrt{ALJD^3}\ll L^2\) on the fixed bounded-safe side.
- Short rows:

\[
 \left|\sum_{a\asymp A}F_a(1)\right|
 \le A^{1/2}\left(\sum_a|F_a(1)|^2\right)^{1/2}
 \ll_\varepsilon L^2X^\varepsilon,
\]

\[
 \left|\sum_{a,q}(-1)^qF_a(q)\right|
 \le(AD)^{1/2}
 \left(\sum_{a,q}|F_a(q)|^2\right)^{1/2}
 \ll_\varepsilon DL^2X^\varepsilon.
\]

The latter is used only for one fixed prescribed polylogarithmic range.
The smooth terminal member obeys the same half-moment proof; equivalently
the full multiplier one has \(n=g\ne0\).

Smooth difference localization has bounded Fourier \(L^1\)-cost and
Möbius separation costs \(\sum_d d^{-3/2}<\infty\).  These preserve the
proved scalar norms and are not used to factor a sharp owner.  Therefore

\[
 \boxed{
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon.}
\tag{109.A4}
\]

Equations (109.A3)--(109.A4) give

\[
 \sum_B|\mathfrak Q_B^{\rm res}|
 \le\sum_B|\mathfrak Q_B^{\rm comp}|
    +O_\varepsilon(L^2X^\varepsilon).
\tag{109.A5}
\]

Summing before absolute values also gives the distinct global signed
corollary

\[
 \left|\sum_B\mathfrak Q_B^{\rm res}\right|
 \le\left|\sum_B\mathfrak Q_B^{\rm comp}\right|
    +O_\varepsilon(L^2X^\varepsilon).
\tag{109.A6}
\]

## Remaining theorem and scope

Neither

\[
 \sum_B|\mathfrak Q_B^{\rm comp}|
 \ll_\varepsilon L^2X^\varepsilon
\quad\hbox{nor}\quad
 \left|\sum_B\mathfrak Q_B^{\rm comp}\right|
 \ll_\varepsilon L^2X^\varepsilon
\]

is proved.  Owner completion is linear; it neither commutes owners with
a Fejér/Gram operator nor supplies cross energies.  Round 108 still
shows that Gaussian functional calculus has unchanged capacity.

Accordingly the fixed-\(a\) Gram, canonical hard
density-discrepancy estimate, hard signed cone, balanced and unbalanced
smooth M2 packets, \(M9\!-\!M2\), \(M9\!-\!M1\), endpoint uniformity,
\(M9\), the quarter target, and every global exponent remain unchanged.
