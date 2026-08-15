# Round 41 synthesis: the large-alpha beta product cell closes

Campaign: m9-m1-beta-off-diagonal-product-cell

Graph SHA-256 before patch:
d58c8024e4a71946b4741660fb7048bc1dc24047e0fe94dca3c1122205048095

## Conductor decision

Round 41 proves the missing large-\(|\alpha|\) terminal product-cell
estimate. The discovery proof, hostile audit, corrected statement-only
rederivation, and conductor calculations agree after three normalization
corrections:

1. the physical-height profile retains its exact modulation;
2. the canonical signed Stirling main phase, rather than the full exact
   gamma argument, is removed;
3. the Vaaler height profile is used only with its genuine cubic tail,
   while arbitrary polynomial decay is reserved for smooth spatial
   Mellin profiles.

The initially assigned blind run disclosed graph exposure. It is retained
as a contaminated independent report and is not counted as the
statement-only gate. The replacement independent rederivation obeyed its
isolation contract and passed after its phase, fixed-height derivative,
and height-seminorm formulas were corrected.

## Exact product normalization

At

\[
u=a+i(L-\nu),\qquad v=b+i\nu,\qquad
s=\frac54+i\left(\frac L2+\beta\right),
\]

the raw unit phases split exactly as

\[
\begin{aligned}
 &(L-\nu)\log\frac{D_j}{2\sqrt X}+\nu\log(H_j+1)
-L\log q-\beta\log(hq)-\frac12(L+\nu+2\beta)\log x\\
 &=L\log\frac{D_j}{2q\sqrt{Xx}}
+\nu\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}
-\beta\log(hqx).
\end{aligned}                                                   \tag{41.1}
\]

Hence the actual height profile is

\[
p(\nu)=e^{i\gamma\nu}\widehat\phi(b+i\nu),\qquad
\gamma=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}.                  \tag{41.2}
\]

The exact diagonal gamma factorization has one bounded-\(\beta\) quotient
and one large-\(\alpha=L+\beta\) quotient. On a signed fixed-ratio cell
\(|\alpha|\asymp\lambda\), with

\[
\lambda=\frac{\pi q\sqrt{Xx}}{D_j},
\]

remove the canonical phase

\[
\Psi'(L)=\log\frac{|L+\beta|}{\lambda},\qquad
\Psi''(L)=\frac1{L+\beta},
\]

and the real factor \(\lambda^\kappa\), where
\(\kappa=3/4+(a+b)/2\). The exact lower Stirling corrections remain in
the symbol \(G\), and differentiated Stirling gives

\[
|\partial_L^mG(L;\lambda)|\ll P_X\lambda^{-m},\qquad 0\le m\le2. \tag{41.3}
\]

Here \(P_X\ll\log^C(2X)\). The height profile and its first three
derivatives have \(L^1\) norm and cubic pointwise decay bounded by \(P_X\).
This cubic order is sharp enough; no false higher height moment is used.
Every interior spatial Mellin profile, and the regular part in

\[
\widehat W_+(u)=\frac1u-\frac1u\int_0^1W'(t)t^u\,dt,
\]

has arbitrary polynomial vertical decay with finitely many derivatives.

After the global ownership operations, the local singular off-diagonal
and smooth cells are

\[
K_\Delta=G(L)\frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)},\qquad
K_W=G(L)\frac{p(\nu)W(L-\nu)}{D(L,\nu)},                       \tag{41.4}
\]

\[
D(L,\nu)=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right).
\]

The character, stationary numerator \((D_j/q)\lambda\), real coefficient
monomial, radial integration, contour factors, floors, stars, and external
\(X^{1/4}\) normalization remain outside (41.4).

## Cancellation-preserving mixed norm

Put

\[
Q=\frac{p(\nu)-p(L)}{L-\nu},\qquad
R=\frac{p(L)-p(\nu)-p'(L)(L-\nu)}{(L-\nu)^2}.
\]

At fixed physical height,

\[
\boxed{\partial_L^\nu K_\Delta
=\frac{G'Q+GR}{D}+\frac{iGQ}{2D^2}.}                          \tag{41.5}
\]

This is the exact endpoint second divided difference. Its two
\(F_{Ly},F_{yy}\) integrals are not separately majorized.

The three centers

\[
\nu=0,\qquad \nu=L,\qquad \nu=-L-2\beta
\]

are separated by \(\asymp\lambda\). The physical-center region reaches
the target value \(P_X\lambda^{-2}\); the top diagonal is continuous and
smaller; the radial ridge is
\(P_X\lambda^{-4}\log(2+\lambda)\); and the far region is summable.
Consequently

\[
\sup_L\int|K_\Delta|\,d\nu\ll P_X\lambda^{-2},\qquad
\sup_L\int|\partial_L^\nu K_\Delta|\,d\nu
\ll P_X\lambda^{-3}.                                      \tag{41.6}
\]

The cell length is \(O(\lambda)\), so the integrated derivative is
target-sized. Smooth cells have at least one spare inverse power because
their translated spatial ridge is disjoint from the physical and radial
centers.

The same separated-center calculation controls every moving physical
trace. Upper moving faces have positive Leibniz sign and lower moving
faces negative sign; fixed faces have zero speed, affine switches agree,
and collapsed sections vanish.

Under the exact signed Morse coordinate, the normalized Jacobian has
bounded supremum and variation. Stieltjes integration against the bounded
Fresnel primitive controls the exact varying-amplitude remainder by the
value, integrated derivative, and trace norms in (41.6). This holds for
both Hessian signs and through saddle entry or exit; an endpoint saddle
has the exact half-Fresnel coefficient.

Thus every off-diagonal or smooth product cell has mixed norm

\[
\ll_\varepsilon X^\varepsilon\lambda^{-2}.                    \tag{41.7}
\]

## Signed diagonal and ownership composition

For the complete product \(H(L,\nu)=C(\beta)G(L)p(\nu)\), the signed
diagonal section is

\[
C_{U,V}[H](L)=\frac{H(L,L)}{A(L)}
\{\Log D(L,q_{U,V})-\Log D(L,p_{U,V})\}.
\]

Since \(H(L,L)/A(L)\) has supremum
\(O(P_X\lambda^{-4})\) and variation
\(O(P_X\lambda^{-3})\), the exact affine-endpoint logarithm gives

\[
\|C_{U,V}[H]\|_\infty+\operatorname{Var}C_{U,V}[H]
+\mathfrak R_{\rm Morse}(C_{U,V}[H])
\ll_\varepsilon X^\varepsilon\lambda^{-2}.                    \tag{41.8}
\]

The section is formed before absolute values and before Morse
localization. The unintegrated diagonal kernel still has a nonzero
\(1/\nu\) tail.

The common artificial package is simplified before estimation:

\[
\omega G_{\rm com}+(1-\omega)R_1-\omega E_1=R_1.
\]

All cutoff derivatives cancel under identical ownership. The accepted
global three-mask, endpoint, axial, and sixteen-stratum ledgers already
place endpoint, side, arithmetic, connector-axis, axial, collision,
corner, and crossed artificial-residue modules outside the post-routing
terminal cell.

Combining (41.7), (41.8), and the accepted finite-section hybrid lemma
proves the axial-subtracted large-alpha terminal-symbol bound. The
already proved coefficient-sum reduction then gives

\[
O_\varepsilon(X^{1/4+\varepsilon})
\]

for the complete large-alpha beta saddle, entry, and exit package.

## State effect

- Promote the exact off-diagonal/smooth product-cell lemma.
- Extend the signed diagonal Cauchy lemma from the separated profile to
  the complete product cell.
- Promote the axial-subtracted large-alpha hybrid symbol bound.
- Record the resulting target-sized complete large-alpha beta package.
- Retain bounded-alpha, the double-bounded cell, complete beta-transition
  assembly, the alpha-bounded branch, M9-M1, M9-M2, M9, and the
  Gauss-circle target as open.

No numerical experiment or external theorem was used. The round
allocation was 100% analytical/algebraic.

