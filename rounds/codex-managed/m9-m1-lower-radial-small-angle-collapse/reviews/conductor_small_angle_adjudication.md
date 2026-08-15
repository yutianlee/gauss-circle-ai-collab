# Round 62 conductor adjudication

Campaign: `m9-m1-lower-radial-small-angle-collapse`

## Decision

Promote the subcritical small-angle reduction and its inclusive
two-fifths replacement range.  Do not promote the remaining signed
one-sided divisor sum, the full lower-radial estimate, M9-M1, M9, or a
new Gauss-circle exponent.

## Accepted kernel

Put \(R=X^{1/4}\), \(Y=\sqrt X\), \(y=\lfloor\sqrt X\rfloor\), and
\(d_{n,h}=2h\sqrt{X/n}\).  For the accepted exact angular multiplier,

\[
 \Omega_X^*(n,h)=\mathbf 1_{d_{n,h}\leq y}^{*}
   +O\!\left(\min\{1,n/Y\}\right).
\]

The floor-, activity-, bottom-, partition-, and star-safe proof is
nontrivial on \(n\leq9Y/4\).  On a fixed subcritical block
\(n\asymp N=X^\nu\), \(0<\nu<1/2\), the hard coefficient is eventually
exactly

\[
 \mathcal D(n)=
 \sum_{\substack{hq=n\\q\ {m odd}\\q>4h}}\chi_4(q)
 =\sum_{\substack{q\mid n\\q\ {m odd}\\q>2\sqrt n}}\chi_4(q).
\]

The smooth radial replacement error is

\[
 \ll_V \frac{N^{5/4}\log(2N)}{Y}.
\]

It is power-saving for fixed \(\nu<2/5\), logarithmic and therefore
\(X^\varepsilon\)-safe at \(\nu=2/5\), and power-losing under triangle
inequality for fixed \(\nu>2/5\).

## Evidence reconciliation

All three reports independently agree on the multiplier collapse, the
exact height-floor inequality, automatic activity, bottom exclusion,
one-count hard star, divisor multiplicity, and the inclusive endpoint
\(\nu=2/5\).  The hostile audit strengthens the finite coefficient:
the floor perturbation and equality star disappear exactly throughout
each fixed subcritical block because \(q\) is odd whereas \(4h\) is
even.

The discovery report's global \(O(\min(1,n/Y))\) formulation is
accepted only as a coefficient comparison; the useful asymptotic
replacement and its radial summation are kept in the stated
subcritical range.  The limiting coefficient is an incomplete
one-sided character-divisor prefix, not \(r_2(n)/4\).

## Remaining obstruction

The first open analytic statement is

\[
 \sum_n V(n/N)\mathcal D(n)n^{-3/4}e(\sqrt{Xn})
 \ll_{\varepsilon,V}X^\varepsilon.
\]

Prime coefficients and incidence counting give polynomial absolute
mass, so coefficientwise absolute values cannot prove it.  Popov's
full \(r_2\) Voronoi formula does not apply to this one-sided cone.
No signed lower bound was proved, so the target remains viable.

## Next interface

The exact cone has the ordinary generating function

\[
 \sum_{n\geq1}\mathcal D(n)z^n
 =\sum_{h\geq1}\frac{z^{4h^2+h}}{1+z^{2h}},\qquad |z|<1.
\]

This identity follows directly by writing odd \(q=4m+1\) and
\(q=4m+3\), with \(m\geq h\).  It is not promoted in this round; it
sets the next frozen objective: determine whether the resulting
partial-theta/Appell-type kernel admits a coefficient-preserving
transformation or a signed radial estimate.

