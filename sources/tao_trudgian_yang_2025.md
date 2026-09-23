# Tao--Trudgian--Yang 2025 source card

## Bibliography

Terence Tao, Tim Trudgian, Andrew Yang, *New exponent pairs, zero density
estimates, and zero additive energy estimates: a systematic approach*,
arXiv:2501.16779v1 (submitted 28 January 2025; the 24 August 2026 date
records the project's audit, not an arXiv revision).

- Abstract page: https://arxiv.org/abs/2501.16779
- Primary source inspected: current arXiv TeX source.

## Statements used by this project

Their definition of an exponent pair \((k,\ell)\) gives, for a model phase
\(F\), \(T\geq N\geq1\), and \(I\subset[N,2N]\),

\[
\sum_{n\in I}e(TF(n/N))
\ll (T/N)^{k+o(1)}N^{\ell+o(1)}.
\]

The theorem labelled `New exponent pairs` states that the following are
exponent pairs:

\[
\left(\frac{89}{1282},\frac{997}{1282}\right),\qquad
\left(\frac{652397}{9713986},\frac{7599781}{9713986}\right),
\]

\[
\left(\frac{10769}{351096},\frac{609317}{702192}\right),\qquad
\left(\frac{89}{3478},\frac{15327}{17390}\right).
\]

The paper derives these via its exponent-sum growth function, exponent-pair
duality, classical exponent-pair processes, and a computer-assisted polytope
optimization over recorded hypotheses.

Lemma 13 records the classical $B$-process

\[
 B(k,\ell)=(\ell-1/2,k+1/2).
\]

Lemma 14 records Sargos's $D$-process in the form

\[
 \beta(\alpha)\le
 \max\left\{
 k_1+\alpha(\ell_1-k_1),\frac1{12}+\frac23\alpha
 \right\},
\]

\[
 D(k,\ell)=(k_1,\ell_1)=
 \left(
 \frac{5k+\ell+2}{8(5k+3\ell+2)},
 \frac{29k+21\ell+10}{8(5k+3\ell+2)}
 \right).
\]

Lemma 15 identifies global exponent pairs with their affine upper bounds
for $\beta(\alpha)$.  For Bourgain's pair, Table 1 records

\[
 D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right)
\]

and the bound

\[
 \beta(\alpha)\le
 \frac{18}{199}+\frac{521}{796}\alpha
\]

on

\[
 \frac{1508}{3825}\le\alpha<
 \frac{62831}{155153}.
\]

The $D$-line dominates the auxiliary line in Lemma 14 on
$0\le\alpha\le1/2$, because their difference is

\[
 \frac{17-29\alpha}{2388}\ge\frac5{4776}.
\]

Together with the $\beta$ symmetry and Lemma 15, this licenses the global
pair above and its $B$-dual

\[
 BD\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right).
\]

## Exact project specialization

For

\[
e\!\left(\frac{hX}{4d}\right),\qquad d\asymp D,\quad h\asymp L,
\]

take \(N=D\), \(T\asymp hX/D\), and, after complex conjugation,
\(F(u)=-u^{-1}\). Since \(F'(u)=u^{-2}\), this is a model phase with
source parameter \(\sigma=2\). Then

\[
T/N\asymp hX/D^2.
\]

For a fixed scale-normalized smooth/BV denominator weight, partial summation
transfers the unweighted interval estimate.  The first new pair therefore
gives

\[
B_L(D;X)
\ll_\varepsilon
X^{[89(1+\ell)+819\delta]/1282+\varepsilon},
\qquad D=X^\delta, L=X^\ell.
\]

It reaches the project target \(X^{1/4+\varepsilon}\) precisely when

\[
178\ell+1638\delta\leq463.
\]

For the Round-152 square-root wave

\[
 P_U=\sum_{\ell\ \operatorname{odd}}
 \chi_4(\ell)\ell^{-3/4}A_U(\ell)e(\sqrt{N\ell}),
\qquad \ell\asymp M,
\]

split the two residue classes modulo four before applying the source
theorem.  With $H\asymp M$ and $T\asymp\sqrt{NM}$, the phase is a model
phase with source parameter $\sigma=1/2$ and

\[
 T/H\asymp R^2M^{-1/2}\ge R.
\]

The pair $BD(13/84,55/84)$, followed by Abel summation with the actual
$M^{-3/4}$-normalized bounded-variation profile, gives

\[
 \boxed{
 |P_U|\ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 X^\varepsilon.}
\]

Hence the scalar target holds when

\[
 \boxed{M^{449}\gg R^{780}.}
\]

This strictly improves the older scalar TTY threshold because
$780/449<1424/819$.  In the reciprocal $\beta$ coordinate the crossing
is $\alpha=127/322$, which lies strictly inside the Table-1 cell printed
above.

## Scope controls

- The theorem is applied only to the reciprocal model phase, which is within
  the source's phase class, or to the square-root model phase with
  $\sigma=1/2$.
- Weighted transfer requires a uniform normalized BV profile; arbitrary
  bounded weights are not covered.
- The theorem gives a pointwise bound for a single dyadic frequency block.
- The Round-152 range is only the actual $D=d=L=1$ scalar.  It does not
  control $D>1$, $L>1$, the growing generic sector, or any downstream
  M9 obligation.
- It does not close the rest of the M2 parameter triangle and has no direct
  implication for the signed fourth-moment route.
