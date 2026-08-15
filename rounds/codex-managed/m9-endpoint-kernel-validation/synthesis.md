# Round 7 synthesis: endpoint-kernel validation

Campaign: `m9-endpoint-kernel-validation`  
Round type: seam validation  
Graph SHA-256 before patch: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`

## Conductor decision

Promote the independently rederived dyadic profile certificate and the
smooth-interior signed quarter-packet reduction. Retain the packet estimate,
the hard top endpoint, `M9-M2`, and the Gauss-circle target as open.

The hostile review found two material scope corrections, which are part of
the accepted statements below:

1. the \(D/L\) fixed-profile annulus result concerns a fixed one-sign,
   endpoint-interior subtotal, not the whole class sum or the moving hard
   endpoint;
2. \(\sum_GG|\mathcal Q_G|\) is a stronger shellwise target. The logically
   weakest signed interface is
   \(\left|\sum_GG\mathcal Q_G\right|\ll L^{3/2}X^\varepsilon\).

## Accepted profile infrastructure

There is an explicit nonnegative telescoping partition of
\(1\le d\le y=\lfloor\sqrt X\rfloor\) into dyadic bands plus a bottom
remainder. Every active band \(D\ge X^{1/4}\) satisfies

\[
\|w_D\|_\infty+sum_d|w_D(d+1)-w_D(d)|\le4,
\qquad
\sum_d|w_D(d)|\ge D/8,
\]

and for \(H_D=\lfloor DX^{-1/4}\rfloor\),

\[
\tfrac12DX^{-1/4}\le H_D\le DX^{-1/4}.
\]

The inactive remainder is supported on \(d\ll X^{1/4}\) and costs
\(O(X^{1/4})\) before Fourier expansion. Consequently the actual profile
hypotheses for B1, W-1, and the TTY wedge are now proved for every active
band. The profile/rounding inputs for the Fejer treatment are also proved,
but `R5-Full-reconciliation` is untouched.

Every interior active band is a full fixed \(C_c^\infty\) rescaling, so the
accepted smooth Poisson transform applies there. Exactly one top band has a
continuum jump at \(d=y\); discrete BV does not license smooth Poisson for
that band.

## Accepted smooth-interior packet reduction

For a uniformly smooth balanced symbol

\[
\mathcal T_A(R,L)=
\sum_{h,k}\chi_4(h)A(h/L,k/L)e(R\sqrt{hk}),
\qquad 1\le L\le R^{1/2},
\]

the following preliminary sectors are at or below target:

- \(\sum_mr_L(m)^2\ll L^2\log(2L)\);
- exact squares and \(R^{-1}\)-near-squares contribute
  \(O_\varepsilon(L^{1+\varepsilon})\) absolutely;
- \((h,k)\ge L^{1/2}\) contributes \(O(L^{3/2})\) absolutely.

Use a fixed smooth dyadic partition of \(g=(h,k)\). On
\(g\asymp G<L^{1/2}\), write \(h=gu,k=gv,(u,v)=1\). Then
\(\chi_4(h)=\chi_4(g)\chi_4(u)\), and Poisson in \(g\), with
\(\widehat F(\xi)=\int F(t)e(-t\xi)dt\), gives exactly

\[
\mathcal T_G=\frac{G}{2i}\mathscr P_G,
\]

where \(\mathscr P_G\) retains the outer \(\chi_4(u)\) and the signed
difference of the \(3/4\)- and \(1/4\)-resonance packets. Sharp gcd cutoffs
require additional endpoint and \(1/\xi\)-tail control and are not part of
this statement.

The exact weakest remaining small-gcd target is

\[
\left|\sum_{G<L^{1/2}}G\mathscr P_G(R,L)\right|
\ll_\varepsilon L^{3/2}X^\varepsilon.
\]

It is unproved and is exactly equivalent to the remaining smooth small-gcd
signed sum. The shellwise \(\ell^1\) variant is a stronger sufficient
target, not a weaker one. The hard top denominator block is outside this
smooth packet statement.

## Accepted scoped direct obstruction

For a fixed one-sign spatial slice staying a fixed distance inside the
active endpoint and for a nonterminal frequency block, each residue class
and one side of the first annulus has average and occasional subtotal size
\(\gg D/L\). This rules out absolute or separately localized estimation.
It does not lower-bound the whole class sum or the full signed block.

The exact square/near-square expansion is retained only as a local-window
identity with admissible support point and height-rounding scope. It gives no
global obstruction.

## Promotion and open seam

The dyadic-weight normalization blocker is closed. Hence the previously
conditional TTY wedge and Round-5 phase diagram are now unconditional for
the chosen actual dyadic decomposition. The residual region is still

\[
\mathcal U=
\{(\delta,\ell):1/4\le\delta\le1/2,
0\le\ell<\delta-1/4,
178\ell+1638\delta>463\}\setminus\{(1/2,0)\}.
\]

At the balanced endpoint, the smooth interior core is now represented by
the outside-absolute quarter-packet target. The top band additionally needs
an endpoint transform or direct estimate. No endpoint range is newly closed.

No numerical evidence was used in Round 7. The round satisfies the 90/10
validation budget.
