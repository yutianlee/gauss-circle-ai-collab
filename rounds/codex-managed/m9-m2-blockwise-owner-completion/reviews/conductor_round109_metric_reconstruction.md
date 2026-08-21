# Conductor review: exact smooth metric reconstruction

Campaign: `m9-m2-blockwise-owner-completion`

Starting graph SHA-256:
`f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d`

## Exact finite identity

Write (d(t)=\|t\|\in[0,1/2]).  Fix a nonincreasing
(\eta\in C^\infty([0,\infty))) which is one on
([0,1/2]) and zero on ([1,\infty)).  For dyadic (R\ge1), put

\[
 V_R(t)=\eta(Rd(t)),\qquad W_R(t)=V_R(t)-V_{2R}(t).
\tag{109.M1}
\]

The functions are smooth and period one.  In particular (V_1=1)
on the whole circle.  On a lift block (g\asymp G), choose a dyadic
(G_*\asymp G).  Finite telescoping gives

\[
 1=\sum_{\substack{1\le R<G_*\\R\ {\rm dyadic}}}W_R+V_{G_*}.
\tag{109.M2}
\]

Consequently the exact punctured identity on the sampled arithmetic
set is

\[
 \boxed{
 1_{t\notin\mathbb Z}
 =\sum_{R<G_*}W_R(t)+V_{G_*}(t)-1_{t\in\mathbb Z}.}
\tag{109.M3}
\]

The last term is a point selector, not an (L^2) Fourier multiplier.
It is the separate exact-centre owner.  The terminal smooth member
(V_{G_*}) equals one at the centre, and (109.M3) subtracts that one
copy.  This resolves the continuity defect in a purported smooth
terminal window satisfying (W(0)=0).

## Fourier scale and density

For every fixed (M\ge0), periodization and rescaling give

\[
 |\widehat W_R(\nu)|+|\widehat V_R(\nu)|
 \ll_M R^{-1}(1+|\nu|/R)^{-M},
\tag{109.M4}
\]

apart from the harmless bounded (R=1) member.  Their means are
(O(R^{-1})), and the active annuli have comparable positive means.
For odd (g\asymp G) and every (R\le G_*\asymp G), (109.M4) gives

\[
 \sum_\nu|\widehat W_R(\nu)|,|g-2\nu|^{1/2}
 \ll\sqrt G,
 \qquad
 \sum_\nu|\widehat W_R(\nu)|,|g-2\nu|^{-1/2}
 \ll G^{-1/2},
\tag{109.M5}
\]

and the same two estimates for (V_{G_*}).  Oddness excludes a zero
denominator at the nearest mode.  Thus the terminal member satisfies
the same accepted half-moment ledger as every ordinary annulus.

## Placement in the owner identity

Apply (109.M3) with (t=\Lambda/k).  The exact-centre point selector
is owned before all nonexact metric members.  Square exact centres use
the divisor bound; nonsquare exact centres use the accepted Round-79
rigidity bound.  Every remaining point occurs with total smooth weight
one, including the deep region (0<\|\Lambda/k\|\ll G^{-1}).

The metric density is the Fourier coefficient at frequency zero inside
each (W_R) or (V_{G_*}).  It remains in the completed coefficient.
It is unrelated to the original Round-77 Poisson zero mode.

The smooth terminal construction is stronger than defining a sharp
deep indicator and then reconstructing it by subtraction.  Either is
algebraically valid, but (109.M1)--(109.M5) keep the terminal in the
same smooth Fourier class and avoid any endpoint Fourier convention.

## Scope

This review supplies an exact one-count metric reconstruction and the
Fourier seminorms needed by the owner estimates.  It gives no estimate
for a residual nonsquare completed directional block.  In particular,
it creates no \(\rho\)-saving and does not close the canonical hard
energy, either smooth M2 packet, (M9\! -\! M2), (M9\! -\! M1),
(M9), endpoint uniformity, or the exponent.
