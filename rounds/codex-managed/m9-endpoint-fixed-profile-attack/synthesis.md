# Round 6 synthesis: balanced endpoint fixed-profile attack

Campaign: `m9-endpoint-fixed-profile-attack`  
Round type: endpoint mechanism attack  
Graph SHA-256: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`

## Conductor decision

Round 6 is closed as a productive reduction round, but without a graph
mutation. The balanced endpoint

\[
D\asymp X^{1/2},\qquad 1<L<X^{1/4}
\]

remains open. The best proved dual envelope is

\[
|\mathcal T_{L,L}|\ll_\varepsilon X^\varepsilon
\min(L^2,X^{1/4}L^{1/2}),
\]

whose largest relative loss against \(L^{3/2}\) is \(X^{1/12}\) at
\(L=X^{1/6}\).

The round nevertheless made three precise advances.

## 1. Actual profile normalization is explicit

The fixed functions

\[
\eta(t)=q(2(t-1)),\qquad W(t)=\eta(t)-\eta(2t)
\]

give an exact nonnegative telescoping partition of
\(1\le d\le y=\lfloor\sqrt X\rfloor\). For
\(D_j=2^{-j}y\), every active block satisfies uniformly

\[
\|w_j\|_\infty+\sum_d|w_j(d+1)-w_j(d)|\le4,
\qquad
\sum_d|w_j(d)|\ge D_j/8,
\]

and with \(H_{D_j}=\lfloor D_jX^{-1/4}\rfloor\),

\[
\tfrac12D_jX^{-1/4}\le H_{D_j}\le D_jX^{-1/4}.
\]

All interior active blocks are full smooth rescalings. The only continuum
non-smoothness is the final finite endpoint block
\(W(d/y)\mathbf 1_{d\le y}\), whose sequence still has uniform discrete BV
and sampled mass. Thus the TTY/B1/W-1 normalization seam is a candidate for
closure, while smooth Poisson retains one explicit endpoint boundary seam.

## 2. Direct fixed-profile absolute methods are saturated

For either odd residue class and either one-sided first annulus, a fixed
nonzero smooth profile has average and occasional subtotal size
\(\gg D/L\). Therefore residue separation, one-sided estimation, or taking
absolute values cannot improve the endpoint bound. This is not a lower bound
for the full signed block: cancellation between classes, sides, and annuli is
still possible and is exactly what a proof must exploit.

At \(X_\tau=4N^2+\tau N\), \(d=N+m\), the exact identity

\[
\frac{hX_\tau}{4d}=h(N-m)+h\left(
\frac{m^2}{N+m}+\frac{\tau N}{4(N+m)}\right)
\]

shows that the perfect-square local pattern is nonuniform under a relative
\(O(N^{-1})\) perturbation. The resulting local windows remain below the
global target and neither prove nor refute it.

## 3. The endpoint obstruction is a signed small-gcd packet

For

\[
\mathcal T_{L,L}(R)=\sum_{h,k\asymp L}
\chi_4(h)a(h,k)e(R\sqrt{hk}),
\]

product multiplicity, exact squares, \(R^{-1}\)-near-squares, any one
squarefree ray, and the sector \((h,k)\ge L^{1/2}\) are all already below the
target scale. The remaining core has \(h=ga,k=gb,(a,b)=1\) and
\(G=g<L^{1/2}\). Poisson summation in \(g\) preserves the character as a
difference of quarter-resonance packets:

\[
\mathcal T_G=\frac{G}{2i}\mathcal Q_G(R).
\]

The weakest direct successor is

\[
\sum_{G<L^{1/2}}G|\mathcal Q_G(R)|
\ll_\varepsilon L^{3/2}X^\varepsilon,
\]

or the weaker fixed-partition version with the absolute value outside the
\(G\)-sum. This estimate retains \(\chi_4(a)\), the difference of the two
quarter packets, and the actual Fourier kernels. It is unproved.

The exact Kowalski--Robert--Wu bilinear theorem was checked from the primary
source and does not improve the accepted envelope. A GL(2)/\(r_2\) Voronoi
transform returns the same first-annulus problem and would require
circle-remainder strength at exponent \(1/4\), so it is not a shortcut.

## Controls and resource use

- Both frequency signs and the actual Vaaler amplitude were retained.
- Special square \(X\) was separated from uniform real \(X\).
- Character-blind counts were not promoted to signed estimates.
- One bounded Python diagnostic tested the exact-square coherence model and
  found no finite coherent growth; it is archived as diagnostic-only and was
  not used in any proof.
- The round remained overwhelmingly analytical/algebraic and within the
  80/20 policy.

## State effect and next round

No accepted obligation changes in Round 6. The profile certificate, exact
packet reduction, and scoped fixed-profile obstructions require routed seam
review and statement-only independent rederivation. Round 7 will validate
those kernels before any State Patch. The endpoint theorem and the global
Gauss-circle target remain open.
