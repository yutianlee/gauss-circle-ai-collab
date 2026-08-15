# Round 13 synthesis: ordered cells are the M1 B-process cone

Campaign: `m9-m1-ordered-denominator-resonance-cells`  
Round type: ordered-denominator mechanism attack  
Graph SHA-256 before patch: `beb0966bb239cd503dd4edde9ac6949bce5e75077d1dbd038043ee3c08972485`

## Conductor decision

Promote the exact two-step odd-denominator decomposition and its optimal
elementary resonance-cell bound. Promote the scoped capacity result:
estimating the cells separately is exactly the one-dimensional
second-derivative or B-process loss and closes no point of the residual
corridor \(\mathcal U_1\). Record the transformed signed restricted
convolution RCS as the open kernel.

All three reports independently obtain the same increment, cell count,
bound, exponent verdict, hard-top control, and B-process identification.
The literature audit found no directly applicable theorem beyond the
already accepted exponent-pair wedge. It verified that the real-variable
Kusmin--Landau and van der Corput hypotheses match the fixed-BV profiles,
while finite-field reciprocals, modular inverses, and separable multilinear
analogies do not.

## Exact ordered-denominator identity

For one positive M1 frequency and odd \(d\),

\[
 \chi_4(d)=-i e(d/4),\qquad
 g_h(d)=\frac{hX}{d}+\frac d4.
\]

Hence

\[
 \boxed{
 g_h(d+2)-g_h(d)
 =\frac12-\frac{2hX}{d(d+2)}.}
\]

Equivalently, two consecutive odd-denominator terms satisfy

\[
 \begin{aligned}
 &\chi_4(d)w_D(d)e(hX/d)
 +\chi_4(d+2)w_D(d+2)e(hX/(d+2))\\
 &\quad=\chi_4(d)e(hX/d)
 \left\{w_D(d)-w_D(d+2)
 e\!\left(-\frac{2hX}{d(d+2)}\right)\right\}.
 \end{aligned}
\]

Thus literal two-term cancellation is favorable near integral values of
\(2hX/(d(d+2))\). The bad cells for the absorbed phase are instead the
half-integral resonances

\[
 \operatorname{dist}\!\left(
 \frac{2hX}{d(d+2)},\mathbb Z+\frac12\right)<\eta.
\]

This sign distinction is essential.

## Cell count and exact capacity

Put

\[
 R_h=\frac{hX}{D^2}.
\]

On \(d\asymp D\), the resonance function has derivative of size
\(R_h/D\), and its range meets \(O(R_h+1)\) half-integers. Therefore

\[
 \#\mathcal E_h(\eta)
 \ll \min\{D,\eta D+R_h+1\}.
\]

The complement has \(O(R_h+1)\) monotone components. Exact discrete
summation by parts, equivalently the Kusmin--Landau bound followed by Abel
summation through the fixed-BV profile, gives

\[
 |S_h|
 \ll \eta D+R_h+1+\frac{R_h+1}{\eta}.
\]

Optimizing and using the trivial bound in the lattice-scale regime yields

\[
 \boxed{
 |S_h(D;X)|
 \ll_\varepsilon X^\varepsilon
 \min\!\left(D,\sqrt{\frac{hX}{D}}\right).}
\]

Since the actual dyadic Vaaler coefficient has \(\ell^1\)-mass \(O(1)\)
on \(h\asymp L\),

\[
 \boxed{
 |B_{1,L}(D;X)|
 \ll_\varepsilon X^\varepsilon
 \min\!\left(D,\sqrt{\frac{LX}{D}}\right).}
\]

For \(D=X^\delta,L=X^\ell\), the exponents are \(\delta\) and
\((1+\ell-\delta)/2\). The first meets \(1/4\) only at the lower active
edge, and the second only at \((\delta,\ell)=(1/2,0)\), already accepted
and removed from \(\mathcal U_1\). No new exponent region is proved.

## Exact dual restricted convolution

The stationary cells are the ordinary odd-lattice B-process modes. For a
smooth interior profile, with the top endpoint treated one-sided, put

\[
 d_{h,q}=2\sqrt{\frac{hX}{q}},\qquad q\ \text{odd}.
\]

Up to the already controlled endpoint and transform errors, the remaining
sum is

\[
 \boxed{
 \mathfrak R_{D,L}(X)=
 \sum_{h\asymp L}u_{L,H}(h)(hX)^{1/4}
 \sum_{\substack{q\ \mathrm{odd}\\
 d_{h,q}\in\operatorname{supp}w_D}}^{*}
 \frac{\chi_4(q)}{q^{3/4}}w_D(d_{h,q})
 e(\sqrt{Xhq}).}
 \tag{RCS}
\]

The RCS target is

\[
 |\mathfrak R_{D,L}(X)|
 \ll_\varepsilon X^{1/4+\varepsilon}.
\]

Grouping \(n=hq\) gives

\[
 \mathfrak R_{D,L}(X)
 =\sum_n A^*_{D,L}(n;X)e(\sqrt{Xn}),
\]

where

\[
 \begin{aligned}
 A^*_{D,L}(n;X)=
 \sum_{\substack{hq=n,\ h\asymp L,\ q\ \mathrm{odd}\\
 2\sqrt{hX/q}\in\operatorname{supp}w_D}}
 &u_{L,H}(h)(hX)^{1/4}q^{-3/4}\chi_4(q)\\
 &\times w_D(2\sqrt{hX/q}).
 \end{aligned}
\]

The phase \(\sqrt{Xhq}\) has rank-one Hessian and is constant on every
product fiber \(hq=n\). Divisor multiplicity plus a triangle inequality
recovers exactly \(\sqrt{LX/D}\). Hence a genuine advance must exploit the
actual signed restricted convolution \(A^*\), or cancellation between
distinct products; generic two-variable curvature does not exist.

## Controls and source audit

- The fixed spatial BV mismatch and all denominator endpoints contribute
  \(O(1)\) per Vaaler shell; the one-sided top transform error is at most
  target scale.
- At \(X=y^2,D=y\), the known family \(d=y-s\) lies near integral, not
  half-integral, increments. Its ordered \(\chi_4\)-cancellation remains a
  positive nonresonant control but says nothing about the bad cells.
- One ordinary differencing step removes the \(d\)-dependent character and
  adds no point of \(\mathcal U_1\).
- The primary sources used for method validation were Arias de Reyna's
  [Kuzmin--Landau note](https://arxiv.org/abs/2002.05982), Vandehey's
  [van der Corput transform paper](https://arxiv.org/abs/1205.0090),
  Heath-Brown's [higher-derivative estimate](https://arxiv.org/abs/1601.04493),
  and the already audited [Tao--Trudgian--Yang exponent-pair paper](https://arxiv.org/abs/2501.16779).
  None supplies cancellation in RCS beyond the accepted wedge.

M9-M1, PSC, RCS, M9-M2, M9, and the Gauss-circle target remain open. No
numerical experiment was used.
