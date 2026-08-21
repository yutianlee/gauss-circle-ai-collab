# Conductor candidate: exact short-window cluster kernel

## Fixed exponential polynomial

Let

\[
 S(t)=\sum_{\lambda\in\Lambda}a_\lambda e(\lambda t),
 \qquad e(z)=e^{2\pi iz},
\]

with finite \(\Lambda\).  For an interval \(I\) of length \(H\) and
centre \(c\), put

\[
 K(u)=\left({\sin\pi u\over\pi u}\right)^2.
\]

Since \(K(u)\ge4/\pi^2\) for \(|u|\le1/2\) and
\(\widehat K(\xi)=(1-|\xi|)_+\),

\[
 \int_I|S(t)|^2\,dt
 \le {\pi^2\over4}H
 \sum_{\lambda,\mu}
 a_\lambda\overline{a_\mu}
 e((\lambda-\mu)c)
 (1-H|\lambda-\mu|)_+.
 \tag{94.K1}
\]

The right side is a positive quadratic form but retains the centre phase
and every coefficient sign.

## Exact random-cell identity

For \(\vartheta\in[0,1)\), set

\[
 C_{\nu,\vartheta}
 =\left[{\nu+\vartheta\over H},{\nu+1+\vartheta\over H}\right).
\]

Two frequencies at distance \(r\) lie in the same randomly shifted cell
with measure \((1-Hr)_+\).  Hence, with
\(b_\lambda=a_\lambda e(\lambda c)\),

\[
 \sum_{\lambda,\mu}b_\lambda\overline{b_\mu}
 (1-H|\lambda-\mu|)_+
 =\int_0^1\sum_{\nu\in\mathbb Z}
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}b_\lambda\right|^2
 \,d\vartheta.
 \tag{94.K2}
\]

Thus no heuristic cluster replacement is needed: the target local moment
is reduced exactly to a signed rational-frequency cluster square.

## M1/M2 specialization

The moving coefficients can first be reduced to fixed-symbol strata on a
Round-94 window of length \(W\le Y^{1/2}\).  Uniformly for
\(D_j\le Y^{1/2}\),

\[
 \sqrt{x+W}-\sqrt x<1,
 \qquad
 D_j\bigl| (x+W)^{-1/4}-x^{-1/4}\bigr|<1.
 \tag{94.K3}
\]

Thus the denominator prefix and each dyadic height floor have only
\(O(1)\) changes.  Across all dyadic scales their union partitions the
window into \(O(\log Y)\) fixed-symbol strata.  A height change contributes
the exact increment \(\gamma_{h,r}\), and

\[
 \sum_{0<|h|\le r}|\gamma_{h,r}|\ll r^{-1},
 \qquad r\asymp D_jY^{-1/4},
\]

so its pointwise block cost is \(O(D_j/r)=O(Y^{1/4})\).  Equivalently, one
may apply a uniform fixed-symbol cluster estimate separately on the
\(O(\log Y)\) strata and absorb the resulting logarithms.  Equality
samples are measure zero in the local integral and their prescribed-point
values remain with the original star convention.  Hence the strict local
survivor may use one fixed actual coefficient on each stratum; this
reduction does not replace it by an arbitrary bounded symbol.

For a fixed actual prefix/profile stratum, write

\[
 \lambda_i={h\over \kappa_i d},
 \qquad \kappa_1=1,\quad \kappa_2=4,
 \qquad |h|\ll D Y^{-1/4},
 \qquad d\asymp D,
\]

and \(a_{i,\lambda}\) is the sum of every exact equal-frequency lift with
its literal M1 or M2 character, Vaaler coefficient, profile, sign, and
star.  The factor \(\kappa_i\) must not be suppressed: M1 has phase
\(e(hX/d)\), whereas M2 has phase \(e(hX/(4d))\).  The within-block cell
condition is

\[
 \left|{h\over \kappa_i d}-{h'\over \kappa_i d'}\right|
 \ll H^{-1},
 \qquad
 |hd'-h'd|\ll {\kappa_i dd'\over H}.
 \tag{94.K4}
\]

If M1 and M2 are assembled before applying the kernel, their two literal
frequency sets are retained in the same union; one may not replace both by
\(h/(4d)\) without explicitly relabelling the M1 frequency and its
coefficient support.

At \(H=Y^{1/4+\sigma}\), the whole active frequency interval contains
only \(O(1+Y^\sigma)\) cells.  In the limiting target regime
\(\sigma\downarrow0\), (94.K2) is therefore pointwise-strength: the
missing input is cancellation inside a bounded number of large arithmetic
clusters.

There is an even sharper direct-menu control.  The accepted uniform
one-third minimax point is

\[
 D=Y^{1/2},\qquad L=Y^{1/6}.
\]

On that dyadic frequency block the band diameter is \(L/D=Y^{-1/3}\)
for M1 and \(L/(4D)\) for M2.  Every window \(H=Y^\alpha\) with
\(\alpha<1/3\) satisfies

\[
 H{L\over D}=o(1).
 \tag{94.K4a}
\]

The triangular multiplier therefore supplies no power decay on the worst
block; it leaves one coherent signed cluster.  A standard-scale local
moment at \(H=Y^{1/3}\) would already imply the full-discrepancy exponent
\(5/18+o(1)\), while on this coherent block the multiplier offers no
averaging gain at all.  Thus such a theorem is not a soft bridge around the
minimax obstruction: it must prove new actual-coefficient cancellation
inside that coherent cluster.  The subcoherence no-go ends at
\(\alpha=1/3\).  The sharp persistence bridge can still improve the
one-third exponent throughout \(1/3<\alpha<1/2\), where the minimax band
occupies \(Y^{\alpha-1/3}\) cells and a genuine cluster estimate remains
possible in principle.

## Required signed inequality

After the exact moving-prefix/BV decomposition and M1/M2/R5 ownership, a
sufficient local theorem is

\[
 \int_0^1\sum_\nu
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}
 a_\lambda(c)e(\lambda c)\right|^2d\vartheta
 \ll_\varepsilon Y^{1/2+\varepsilon}
 \tag{94.K5}
\]

for every centre \(c\asymp Y\) and every target window.  This is sufficient
at \(H=Y^{1/4+o(1)}\).  At a fixed
\(H=Y^{1/4+\sigma}\), a strict quarter conclusion requires the stronger
right side \(Y^{1/2-\sigma+o(1)}\), equivalently total local mass
\(Y^{3/4+o(1)}\).  Arbitrary bounded
coefficients falsify this scale, so the proof must use the actual character
and phase.  The frozen separated-frequency theorem gives only
\((H+D^2)D\asymp Y^{3/2}\) at \(D=Y^{1/2}\); it does not prove (94.K5).

## Scope

Equations (94.K1)--(94.K4) and the one-jump reduction are exact.  A complete
Round-94 proof must still audit the equality stars, cross-block assembly,
and R5 ownership, then prove (94.K5).  No canonical-core or pointwise
conclusion is asserted here.
