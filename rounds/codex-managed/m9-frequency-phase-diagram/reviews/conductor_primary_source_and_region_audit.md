# Conductor audit: primary exponent-pair wedge and dual normalization

## Decision

The accepted elementary estimates are supplemented by one rigorously sourced
exponent-pair region.  This is a genuine enlargement of the proved
pointwise region, but it does not close the M2 frequency triangle.

No numerical exponential sum is used.  All computations below are exact
rational conversions of published estimates.

## 1. Coordinates and the accepted elementary region

Put

\[
D=X^\delta,\qquad L=X^\ell,\qquad
\Omega=\left\{\frac14\leq\delta\leq\frac12,
0\leq\ell\leq\delta-\frac14\right\}.
\]

The independently checked elementary estimates have exponents

\[
E_{\rm T2S}=\delta-\ell,
\qquad
E_{2,1}=\frac{1+\ell-\delta}{2},
\qquad
E_{2,2}=\frac{3\delta-1-\ell}{2},
\qquad E_{\rm triv}=\delta.
\]

At target \(1/4\), these cover the terminal line

\[
\ell=\delta-\frac14
\]

and the isolated point \((\delta,\ell)=(1/2,0)\).  The left vertex is already
part of the terminal line.

## 2. Primary-source exponent-pair certificate

Tao--Trudgian--Yang, arXiv:2501.16779, Definition ``Exponent pair'' gives

\[
\sum_{n\in I} e(TF(n/N))
\ll (T/N)^{\kappa+o(1)}N^{\lambda+o(1)}
\]

for model reciprocal phases, and their theorem ``New exponent pairs'' proves

\[
(\kappa,\lambda)=\left(\frac{89}{1282},\frac{997}{1282}\right).
\tag{P1}
\]

For fixed \(h\asymp L\), write

\[
e\!\left(\frac{hX}{4d}\right)
=\overline{e\!\left(TF(d/D)\right)},
\qquad T\asymp\frac{hX}{D},\qquad F(u)=-\frac1u.
\]

Here \(F'(u)=u^{-2}\), so \(F\) is a model phase with source parameter
\(\sigma=2\). Thus \(T/N\asymp hX/D^2\), and partial summation for a fixed
scale-normalized BV denominator profile gives

\[
\sum_{d\asymp D}w_D(d)e\!\left(\frac{hX}{4d}\right)
\ll_\varepsilon X^\varepsilon
\left(\frac{hX}{D^2}\right)^\kappa D^\lambda.
\]

The total \(1/h\)-mass on \(h\asymp L\) is \(O(1)\). Therefore

\[
|B_L(D;X)|
\ll_\varepsilon
X^{\kappa(1+\ell-2\delta)+\lambda\delta+\varepsilon}.
\tag{2.1}
\]

For (P1), the target condition is exactly

\[
\frac{89(1+\ell)+819\delta}{1282}\leq\frac14,
\]

or

\[
\boxed{178\ell+1638\delta\leq463.}
\tag{2.2}
\]

The transfer is not asserted for arbitrary bounded denominator weights.  It
requires the fixed normalized smooth/BV block profile already contemplated by
the project; endpoint blocks must be merged or verified with the same uniform
variation bound.

The new wedge reaches the bottom edge through

\[
\delta\leq\frac{463}{1638}=0.28266\ldots,
\]

and covers the entire vertical section of \(\Omega\) through

\[
\delta\leq\frac{1015}{3632}=0.27946\ldots.
\]

The second number is obtained by intersecting (2.2) with the terminal line.

Consequently the exact region left after the certified pair, T2S, and the
second-derivative endpoint is

\[
\boxed{
\mathcal U=
\left\{(\delta,\ell)\in\Omega:
0\leq\ell<\delta-\frac14,
\ 178\ell+1638\delta>463
\right\}
\setminus\left\{\left(\frac12,0\right)\right\}.}
\tag{2.3}
\]

The paper's piecewise bounds for its exponent-sum growth function can sharpen
small parts of the boundary, but they are not needed for this clean promotion.
The globally stated pair (P1) is the source-minimal certificate.

## 3. Formal Poisson/B-process normalization

For the denominator sum, Poisson frequencies with a stationary point satisfy

\[
k\asymp K:=\frac{XL}{D^2}.
\]

At the stationary point, the phase is a constant multiple of

\[
\sqrt{Xhk},
\]

and the stationary-phase amplitude, after including the Vaaler coefficient
\(1/h\), is of size

\[
P:=\frac{D^{3/2}}{X^{1/2}L^{3/2}}.
\]

Thus the formal main term is \(P\) times a double sum of lengths \(L,K\), and

\[
LK=\frac{XL^2}{D^2}.
\]

The proposed estimate

\[
\sum_{h\asymp L}\sum_{k\asymp K}
a(h,k)e(c\sqrt{Xhk})
\ll_\varepsilon (LK)^{3/4}X^\varepsilon
\tag{3.1}
\]

has exactly the needed normalization, because

\[
P(LK)^{3/4}=X^{1/4}.
\]

This identity establishes sufficiency, not validity. Grouping by \(m=hk\)
turns (3.1) into a square-root phase sum with a short-range,
character-weighted divisor coefficient

\[
a_m=\sum_{\substack{h\mid m\\h\asymp L\\m/h\asymp K}}
\text{(smooth symbol)}\,\chi_4(h).
\]

Classical unweighted exponent-pair bounds do not apply to this irregular
coefficient.  Absolute summation recovers the first term of the ordinary
second-derivative estimate, so it supplies no new region.  A promotion of
(3.1) therefore requires either a coefficient-sensitive bilinear theorem or
new cancellation in this actual divisor symbol.

## 4. Research consequence

The smallest honest next target is no longer the whole triangle.  It is the
corridor (2.3), with two distinct possible mechanisms:

1. improve the direct reciprocal-phase estimate by exploiting the
   \(\chi_4(h)\) average across \(h\), rather than bounding each \(h\)
   separately; or
2. prove a scoped version of (3.1) for the actual stationary-phase symbol.

Neither the published exponent pair nor formal Poisson transformation alone
proves M9-M2.

## Sources audited

- T. Tao, T. Trudgian, A. Yang, *New exponent pairs, zero density estimates,
  and zero additive energy estimates: a systematic approach*,
  arXiv:2501.16779, especially the definitions of \(\beta\) and exponent
  pairs and the theorem ``New exponent pairs.''
- J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
  arXiv:1408.5794, for the older pair \((13/84,55/84)\); it is superseded for
  the clean wedge above by (P1).
