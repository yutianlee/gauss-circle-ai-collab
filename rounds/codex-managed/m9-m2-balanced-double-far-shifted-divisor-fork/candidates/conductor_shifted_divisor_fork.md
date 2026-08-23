# Conductor candidate: shifted-divisor and increment fork

Campaign: m9-m2-balanced-double-far-shifted-divisor-fork

Status: candidate only.

## Candidate A: literal divisor coefficient

Substitution of the full products gives the exact candidate

\[
 \begin{aligned}
 C_B(n,r)=
 \sum_{\substack{h\mid n,\ h'\mid n+r\\
 h\asymp L,\ n/h\asymp K\\
 h'\asymp L,\ (n+r)/h'\asymp K\\
 \left|h(n+r)/h'-h'n/h\right|>L}}
 &\chi_4(h)\chi_4(h')\\
 {}\times&
 \eta\!\left({(h,n/h)\over G_0}\right)
 \eta\!\left({(h',(n+r)/h')\over G_0}\right)\\
 {}\times&
 A_B(h,n/h)A_B(h',(n+r)/h').
 \end{aligned}
\]

This identity should be checked coefficientwise. It exposes an incomplete,
weighted correlation of two divisor selectors; it is not yet a standard
binary additive-divisor sum because both factor choices and the
determinant deletion remain inside.

## Candidate B: even-increment character collapse

With \(h'=h+p\), \(k'=k+q\), only even \(p\) survives and

\[
 \chi_4(h)\chi_4(h+p)=(-1)^{p/2}.
\]

Thus the actual character offers an alternating sign across the even
\(p\)-shifts but no cancellation in \(h\) at fixed \(p\). A lawful
dispersion attack must preserve the \(p\)-sum long enough to use this
alternation; taking an absolute value over \(p\) discards the only visible
character mechanism.

The exact phase is

\[
 \Phi_{p,q}(h,k)=
 R\left(\sqrt{(h+p)(k+q)}-\sqrt{hk}\right).
\]

A Poisson or stationary decomposition in \(h,k\) must compute its zero
mode and boundary stationary points. The identities

\[
 r+\rho=q(2h+p),\qquad r-\rho=p(2k+q)
\]

may parameterize fixed modes, but divisor-bounded multiplicity for a
fixed pair \((r,\rho)\) does not save globally.

## Candidate tests

1. Sum over the even \(p\)-shift before absolute values and test whether
   \((-1)^{p/2}\) annihilates the zero mode of the actual smooth weight.
2. If it does not, compute the main term at the \(L^3\) or \(L^4\)
   scale before estimating the remainder.
3. If a dispersion inequality is used, record the diagonal it creates,
   the number of shifts, and every Cauchy factor. The output must act on
   the scalar \(E_{B,\rm df}\), not merely on a stronger unrelated norm.
4. If the determinant deletion is restored, charge its width-\(L\)
   corridor exactly once.

No cancellation statement is asserted in this candidate.
