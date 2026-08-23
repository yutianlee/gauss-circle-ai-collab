# Conductor review: separate parent capacity and literal labels

Campaign: `m9-m1-direct-parent-minimax-gate`

Starting graph SHA-256:
`c3498daad3bdceb7c69c0e47a616e03ebfa12ccaf42f8df42958aa227f50fd91`

## Accepted menu on the residual

For a literal M1 block set

\[
 a=\delta-\ell.
\]

The frequency-first row has exponent (a).  The two nonconstant
second-derivative exponents are

\[
 g_1={1+\ell-\delta\over2}={1-a\over2},\qquad
 g_2={3\delta-1-\ell\over2}.
\]

On the active triangle,

\[
 g_2-g_1=2\delta-1-\ell\leq0,
\]

so the second-derivative row is governed by (g_1).  The trivial row is
dominated by the frequency-first row.  After retaining the TTY row, the
exact exponent capacity is therefore

\[
 c(\delta,\ell)=
 \min\left\{a,{1-a\over2},
 {89(1+\ell)+819\delta\over1282}\right\}.
\tag{119.R1}
\]

The elementary part of (119.R1) is at most (1/3), with equality only at
(a=1/3).  Adding the TTY row can only decrease the capacity.  Thus every
literal hard or smooth residual block has accepted-menu capacity at most
(X^{1/3+\varepsilon}).

## Literal hard and first-smooth witnesses

Let

\[
 y=\lfloor\sqrt X\rfloor,qquad D_0=y,qquad D_1=y/2,qquad
 H_j=\lfloor D_jX^{-1/4}\rfloor.
\]

The (j=0) denominator profile is the unique hard profile and (j=1) is
a full smooth profile.  For (j=0,1), choose an actual dyadic frequency
label (L_j=2^{-r_j}H_j) with

\[
 X^{1/6}\leq L_j<2X^{1/6}.
\tag{119.R2}
\]

Such (r_j) exists for all sufficiently large (X), because
(H_j\asymp X^{1/4}).  Moreover (r_j\to\infty), so this is not the
clipped terminal label.  It is a full frequency shell and is far from the
bounded-height cases.

For either (j), (D_j\asymp X^{1/2}) and (L_j\asymp X^{1/6}).  Hence
the numerical right sides of the two elementary estimates obey

\[
 1+{D_j\over L_j}\asymp X^{1/3},
\]

and

\[
 1+\sqrt{L_jX/D_j}+{D_j^{3/2}\over\sqrt{L_jX}}
 \asymp X^{1/3}+X^{1/6}\asymp X^{1/3}.
\tag{119.R3}
\]

At the limiting exponent point ((\delta,\ell)=(1/2,1/6)), the TTY row is

\[
 {770\over1923}={1\over3}+{43\over641}>{1\over3}.
\tag{119.R4}
\]

The floor and fixed factor (1/2) perturb (119.R4) by only
(O(1/\log X)), so its numerical bound remains a fixed positive power
larger than (119.R3).  Consequently the minimum of all accepted direct
right sides is (\asymp X^{1/3}) on both literal families.

The two labels belong to the residual.  They satisfy
(\ell<\delta-1/4); they are not ((1/2,0)); and

\[
 178\ell+1638\delta\longrightarrow {2546\over3}>463.
\]

Thus neither the terminal, full second-derivative target point, nor TTY
wedge owns them.  Bottom and R5 own different pieces and do not remove
these main blocks.

It follows that the supremum of the accepted direct-menu capacity is
separately (X^{1/3+o(1)}) on the hard parent and on the smooth parent.
Equivalently, no fixed (X^{-\eta}) improvement over (X^{1/3}) for
either whole parent follows by selecting among accepted direct rows.
This is a minimax statement about proved upper-bound formulas, not a lower
bound for either arithmetic sum.

## Hard-cone normalization

The accepted one-sided transform gives, on a hard shell (h,n\asymp L),

\[
 \mathcal M^+_{1,\mathrm{end},L}
 =-{2e(1/8)\over\pi}X^{1/4}L^{-3/2}\mathcal T^{M1}_L
 +O_\varepsilon(X^{1/4+\varepsilon}).
\tag{119.R5}
\]

The coefficient-blind cone ledger has (O(L^2)) lattice capacity, while
the required normalized target is (L^{3/2}X^\varepsilon).  At
(L\asymp X^{1/6}), the physical triangle capacity in (119.R5) is

\[
 X^{1/4}L^{-3/2}L^2
 =X^{1/4}L^{1/2}\asymp X^{1/3}.
\]

Thus the hard and smooth critical labels both miss the quarter target by
the same factor

\[
 X^{1/12}=L^{1/2}.
\]

This equality is a capacity comparison only.  It supplies no identity
between the two sums.

## Decision

The separate-parent minimax passes.  The smallest hard survivor is one
literal middle/lower shell of the unique hard profile with
(L\asymp X^{1/6}), including its normalized product cone.  The smallest
smooth survivor is one full (j=1) label with (D=y/2) and
(L\asymp X^{1/6}).  No accepted direct owner shrinks either survivor.

Promote only this normalization/minimax certificate.  Retain both analytic
parents open, and do not change M9-M1 or any global exponent.
