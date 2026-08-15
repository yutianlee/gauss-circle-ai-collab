# Round 14 synthesis: exact angular recombination, not an (r_2) collapse

Campaign: `m9-m1-dual-r2-recombination`  
Round type: global recombination discovery  
Graph SHA-256 before patch: `ba43cb4e073a06640030a9090df6b57cc4ad8564feada6a0698aa777d1378b14`

## Conductor decision

Promote the exact full-active-M1 product recombination and its global
angular coefficient. Promote two scoped obstructions: M1 alone does not
collapse to (r_2(n)/4), and a hypothetical completion to the full radial
(r_2)-sum is exactly the classical Hardy–Voronoi return map, equivalent
to the desired Gauss estimate up to target-sized errors. Retain the global
angular radial estimate as an open, logically weaker alternative to the
current blockwise M9-M1 formulation.

The blind derivation and the independent hostile/source audit agree on the
stationary constant, the product range, parity, endpoint convention,
divisor-dependent multiplier, and return-map conclusion. The third attack
exceeded its bounded brief after two interventions and was terminated
without a report; no claim relies on it. No numerical experiment was used.

## Exact recombination

Let (D_j=2^{-j}\lfloor\sqrt X\rfloor),
(H_j=\lfloor D_jX^{-1/4}\rfloor), and let (w_j) be the accepted exact
dyadic denominator partition, including the one-sided top block. Summing
the actual positive-frequency shell partition first, applying the accepted
interior and top one-sided transforms, and pairing negative frequencies
gives

\[
 \boxed{
 \sum_j\mathcal M_1(D_j;X)
 =-\frac4\pi X^{1/4}\operatorname{Re}\!\left\{
 e(1/8)\sum_{n\le16\sqrt X}
 \mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})
 \right\}+O_W(\log^2X).}
 \tag{14.1}
\]

The exact coefficient is

\[
 \boxed{
 \mathcal C_X^*(n)=
 \sum_{\substack{h\mid n\\q=n/h\ {m odd}}}
 \chi_4(q)\Omega_X^*(n,h),}
 \tag{14.2}
\]

where

\[
 \boxed{
 \Omega_X^*(n,h)=\sum_j
 \mathbf1_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{\frac Xn}\right)\right]^*.}
 \tag{14.3}
\]

The star retains stationary endpoint half weights; the one-sided hard-top
cotangent boundary is kept separately and is already target-safe. The
inactive bottom denominator range contributes the previously accepted
(O(X^{1/4})) before Fourier expansion.

The radial power in (14.1) is an exact cancellation:

\[
 (hX)^{1/4}q^{-3/4}\frac{\Phi(h/(H_j+1))}{h}
 =X^{1/4}(hq)^{-3/4}\Phi(h/(H_j+1)).
\]

Thus the artificial (L)-partition disappears exactly. The (D)-sum does
not: (Omega_X^*(n,h)) retains the divisor angle (h/\sqrt n), the exact
height floors, the Vaaler profile, and the hard angular cone.

## Strictly weaker global interface

Equation (14.1) shows that the single real-part estimate

\[
 \boxed{
 \operatorname{Re}\!\left\{e(1/8)
 \sum_{n\le16\sqrt X}\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn})\right\}
 \ll_\varepsilon X^\varepsilon}
 \tag{GAR}
\]

is sufficient for the total active M1 contribution. It is strictly weaker
than uniform blockwise M9-M1 because it permits cancellation between the
actual (D)- and (L)-pieces. It does not imply the present blockwise node,
so the conditional bridge must not be silently changed. Analytically, GAR
is still the original global active M1 sum in exact transformed
coordinates; Round 14 proves no new cancellation estimate for it.

## Exact obstruction to (r_2/4)

At (X=y^2), take (n=7). The factorization ((h,q)=(1,7)) has
(d=2y/\sqrt7<y), is active away from the endpoint, and has nonzero
multiplier with (chi_4(7)=-1). The complementary factorization
((h,q)=(7,1)) has (d=2\sqrt7,y>y) and is absent. Hence

\[
 \mathcal C_X^*(7)\ne0,
 \qquad
 \frac{r_2(7)}4=\chi_4(1)+\chi_4(7)=0.
\]

This exact control falsifies a full (r_2(n)/4) factorization for M1
alone. Spatial telescoping cannot repair it because each spatial weight is
multiplied by the scale-dependent (Phi(h/(H_j+1))), height cutoff, and
endpoint convention.

## Hardy–Voronoi return map

Popov's primary-source Theorem 5 gives, for (N\ge3,x\ge3),

\[
 P(x)=-\frac{x^{1/4}}\pi\sum_{n\le N}
 \frac{r_2(n)}{n^{3/4}}
 \cos\!\left(2\pi\sqrt{nx}+\frac\pi4\right)
 +O\!\left(\sqrt{\frac xN}\,\overline r(x)
 +\overline r(N)\log N\right),
\]

where (overline r(t)=t^{o(1)}). At (N\asymp X^{1/2}) the error is
(O_\varepsilon(X^{1/4+\varepsilon})). Restoring the exact M1 stationary
constant shows that a hypothetical completion of (14.2) to the full
(r_2(n)/4) coefficient reproduces this cosine sum exactly. Bounding that
complete radial sum at the target scale is therefore equivalent to the
Gauss-circle target up to a target-sized error, not an easier imported
lemma.

Primary source: [Popov, Theorem 5](https://www.mathnet.ru/eng/rm10162),
with the project audit in `sources/popov_2024_voronoi_gauss.md`.

## State effect

- Accept (14.1)–(14.3), including constants, product cutoff, parity,
  floors, and endpoint stars.
- Record GAR as open and sufficient only for the total active M1 aggregate.
- Reject the M1-only (r_2/4) collapse and any claim that the completed
  radial sum is independently easier.
- Keep RCS, blockwise M9-M1, M9-M2, M9, and the Gauss target open.

The next useful interface is a two-variable Mellin separation of the exact
angular symbol (Omega_X^*(n,h)), with the floor perturbation and hard top
isolated explicitly. The point is to obtain genuinely twisted divisor
coefficients, not to replace them by (r_2).
