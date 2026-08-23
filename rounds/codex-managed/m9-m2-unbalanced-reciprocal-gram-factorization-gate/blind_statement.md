# Round 123 blind statement: integer-centred reciprocal Gram

This statement is self-contained. Treat every displayed profile as literal
data. Do not replace the truncated coefficient by a complete divisor or
circle coefficient, and do not use the desired Gauss-circle estimate.

Let \(X\ge 2\) be real, \(N=\lfloor X\rfloor\), and

\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 R={X\over D},\qquad K={XL\over D^2},\qquad \Delta={D\over L},
\]

where

\[
 {1\over4}\leq\delta<{1\over2},\qquad
 0\leq\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463.
\tag{123.B1}
\]

Let \(q_L\) be the fixed nonnegative smooth Vaaler/frequency profile,
supported on a fixed dyadic multiple of \(L\), and let \(W\) be the fixed
real smooth spatial profile. Put

\[
 \mathcal Q_L(y)=\int_0^\infty {q_L(h)\over h}e(hy)\,dh.
\tag{123.B2}
\]

The literal flat-smooth unbalanced wave is

\[
 \mathscr R_X=
 \sum_{\substack{r\asymp R\\r\ {\mathrm{odd}}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \sum_{k\asymp K}{q_L(4Xk/r^2)\over k}e(Xk/r).
\tag{123.B3}
\]

Its accepted product form is

\[
 \mathscr R_X=
 \sum_{\substack{r\asymp R\\r\ {\mathrm{odd}}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \sum_d \mathcal Q_L\!\left({r(X-rd)\over4X}\right),
\tag{123.B4}
\]

up to the already target-safe flat-smooth normalization and rapidly
decaying tail. The required estimate is

\[
 \mathscr R_X\ll_\varepsilon X^{1/4+\varepsilon}.
\tag{123.B5}
\]

Define the phase-integerized row, with every amplitude still frozen at
the real parameter \(X\), by

\[
 \mathscr R_N^\sharp=
 \sum_{\substack{r\asymp R\\r\ {\mathrm{odd}}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \sum_{k\asymp K}{q_L(4Xk/r^2)\over k}e(Nk/r).
\tag{123.B6}
\]

First determine rigorously whether

\[
 \mathscr R_X-\mathscr R_N^\sharp\ll_\varepsilon X^\varepsilon
\tag{123.B7}
\]

holds uniformly. A termwise triangle in (123.B3) is not admissible unless
its full cost is charged. The coefficientwise Poisson identity for
(123.B6) has physical kernel

\[
 \sum_d \mathcal Q_L\!\left({r(N-rd)\over4X}\right),
\tag{123.B8}
\]

with the same \(q_L,W,X,D,L\). All tails, support entries, integer ties,
and the possible value \(K\asymp1\) must be included.

For the integerized row write

\[
 A_{r,k}=W\!\left({X\over rD}\right)q_L(4Xk/r^2),
\qquad
 B_k=\sum_{\substack{r\asymp R\\r\ {\mathrm{odd}}}}
 \chi_4(r)A_{r,k}e(Nk/r).
\tag{123.B9}
\]

Derive the smallest lawful weighted Cauchy or Gram identity for
\(\sum_k B_k/k\), retaining the actual character and both sampled
profiles. In particular audit the signed kernel

\[
 \mathcal K_{r,s}=
 \sum_{k\asymp K}{q_L(4Xk/r^2)q_L(4Xk/s^2)\over k}
 e\!\left(Nk\left({1\over r}-{1\over s}\right)\right).
\tag{123.B10}
\]

Do not discard the off-diagonal signs. Quantify the diagonal and state
exactly what bound for the complete signed Gram is sufficient for
(123.B5).

For every off-diagonal pair let \(j\in\mathbb Z\) be the nearest alias
to \(N(1/r-1/s)\), with ties treated explicitly, and define

\[
 E=N(s-r)-jrs.
\tag{123.B11}
\]

Prove the exact factorization

\[
 (N-jr)(N+js)-N^2=jE
\tag{123.B12}
\]

and derive the localization scale for \(E\) from (123.B10). Write
\(N=2^tN_0\), with \(N_0\) odd. Audit every parity branch, including
\(N=0\) if it is not excluded by the stated range, \(j=0\), exact
collisions \(E=0\), near collisions, negative aliases, and the residue
classes of \(r,s\) modulo four. Determine whether the actual factor
\(\chi_4(r)\chi_4(s)\) becomes a useful alternating defect sign or merely
reconstructs the original quarter shift.

Required outcome: prove (123.B5), a nonempty target-safe strict exponent
region, a quantified actual-sign saving, an inverse theorem for the
remaining near-product packets, or a rigorous no-go whose smallest signed
survivor is explicit. An absolute near-product count, an unsigned large
sieve, a positive diagonal alone, or another invertible Poisson/B-process
return is not a proof. State the first doubtful step and the precise scope
for flat smooth UNBAL, complete UNBAL, M9-M2, M9, and every exponent.
