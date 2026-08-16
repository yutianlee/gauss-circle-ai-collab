# Accepted beta off-diagonal product-cell kernel

Status: `proved_internal` as
`M9-M1-beta-off-diagonal-smooth-product-cell-bound` in
`state/proof_obligations.yml`. This file is a readable proof kernel; the
graph remains authoritative.

## Statement

Fix the legal terminal line \(c'=5/4\), bounded \(\beta\), one actual
signed large-\(\alpha\) cell, and

\[
\lambda=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
c_0\lambda\le |L+\beta|\le C_0\lambda.
\]

After the accepted endpoint, side, arithmetic, artificial, axial,
collision, connector, corner, and height-limit routing, remove the
canonical signed stationary phase and its \(\lambda^\kappa\) amplitude.
The remaining singular and smooth products are

\[
K_\Delta(L,\nu)=G(L)\frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)},\qquad
K_W(L,\nu)=G(L)\frac{p(\nu)W(L-\nu)}{D(L,\nu)},       \tag{1}
\]

where

\[
D=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right),\qquad
p(\nu)=e^{i\gamma\nu}\widehat\phi(b+i\nu),\qquad
\gamma=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}.       \tag{2}
\]

For \(m\le2\), the normalized gamma symbol satisfies

\[
|\partial_L^mG(L)|\ll P_X\lambda^{-m},               \tag{3}
\]

and, for the required finite orders,

\[
|p^{(m)}(\nu)|\ll P_X(1+|\nu|)^{-3},\qquad
|W^{(m)}(y)|\ll_{m,N}P_X(1+|y|)^{-N},               \tag{4}
\]

with \(P_X\ll\log^C(2X)\). Then, uniformly on both signed saddle,
entry, and exit cells,

\[
\begin{aligned}
&\sup_L\int_{\mathbb R}|K(L,\nu)|\,d\nu
+\int\!\!\int|\partial_L^\nu K(L,\nu)|\,d\nu\,dL\\
&\quad+\sup_{U,V}\sum_{\gamma_{\rm mov}}
\int|K(L,\gamma_{\rm mov}(L))|\,dL
+\|\mathfrak r_{\rm Morse}[K]\|_{L^1(d\nu)}
\ll P_X\lambda^{-2}                                  \tag{5}
\end{aligned}
\]

for \(K=K_\Delta\) and each \(K=K_W\).

## Exact derivative

Put

\[
Q=\frac{p(\nu)-p(L)}{L-\nu},\qquad
R=\frac{p(L)-p(\nu)-p'(L)(L-\nu)}{(L-\nu)^2}.
\]

At fixed physical height \(\nu\),

\[
\boxed{\partial_L^\nu K_\Delta
=\frac{G'Q+GR}{D}+\frac{iGQ}{2D^2}.}                  \tag{6}
\]

Formula (6) is the cancellation-preserving endpoint second divided
difference. The equivalent \(F_{Ly},F_{yy}\) integral representation is
signed and must not be majorized term by term.

## Proof

The raw unit phases split exactly as

\[
\begin{aligned}
 &(L-\nu)\log\frac{D_j}{2\sqrt X}+\nu\log(H_j+1)
-L\log q-\beta\log(hq)-\frac12(L+\nu+2\beta)\log x\\
 &=L\log\frac{D_j}{2q\sqrt{Xx}}
+\nu\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}
-\beta\log(hqx).                                      \tag{7}
\end{aligned}
\]

The accepted exact diagonal gamma factorization and differentiated
two-sided Stirling give (3) after removing the canonical phase
\(\Psi'(L)=\log(|L+\beta|/\lambda)\). Compact fixed dyadic profiles,
and the top decomposition

\[
\widehat W_+(u)=\frac1u-\frac1u\int_0^1W'(t)t^u\,dt,
\]

give (4) by vertical integration by parts. The \(1/u\) share is the
singular top and is excluded from the smooth seminorm.

For (1), divide physical height into neighborhoods of the separated
centers

\[
\nu=0,\qquad \nu=L,\qquad \nu=-L-2\beta.              \tag{8}
\]

At \(\nu=0\), the two denominators have size \(\lambda\) and the
\(L^1\) height profile gives the limiting \(\lambda^{-2}\) value. Near
\(\nu=L\), use local Taylor formulas; cubic profile decay and
\(|D|\asymp\lambda\) give a smaller contribution. Near
\(\nu=-L-2\beta\), both profile endpoints are \(O(P_X\lambda^{-3})\),
the divided difference adds \(\lambda^{-1}\), and the \(D^{-1}\) ridge
costs only \(\log(2+\lambda)\). The complement has two separated
denominators or cubic decay. Applying the same partition to (6) proves
the value and fixed-height derivative terms in (5). The smooth cell is
smaller because its translated \(W\)-ridge is disjoint from the physical
and radial centers.

On a moving face \(\nu=L-c\), use

\[
\frac{p(L-c)-p(L)}c,\qquad
|D(L,L-c)|\asymp1+|L-c/2+\beta|.                    \tag{9}
\]

The three possible trace centers remain separated, proving the trace
term in (5). Upper moving faces have positive Leibniz sign, lower faces
negative sign; fixed faces have zero velocity, affine switches agree, and
collapsed sections vanish.

Under the exact signed Morse change, \(J/\sqrt\lambda\) has bounded
supremum and variation on each fixed-ratio interval. The bounded Fresnel
primitive and Stieltjes integration bound the exact varying-amplitude
remainder by the value, integrated derivative, and trace terms already
proved. This works for both Hessian signs and when the saddle enters or
exits; an endpoint saddle gives the exact half-Fresnel coefficient.

## Ownership and exclusions

The common artificial package is simplified before estimation:

\[
\omega G_{\rm com}+(1-\omega)R_1-\omega E_1=R_1.
\]

The accepted routing places connector-axis, crossed artificial residue,
endpoint, side, arithmetic, axial, collision, and corner modules outside
this local product cell. A retained compact beta multiplier changes only
\(P_X\). The signed diagonal kernel
\(-iH(L,L)/(2AD)\) is excluded from (5); its exact Cauchy section must be
formed before absolute values and Morse localization.

The character, stationary numerator, real coefficient monomial, radial
integral, contour constants, floors, stars, and external \(X^{1/4}\)
factor remain outside (1). This kernel proves no bounded-alpha,
double-bounded, complete transition, M9-M1, M9, or Gauss-circle bound.

## Validation

- Discovery proof: rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/reports/off_diagonal_mixed_norm_attack.md.
- Independent rederivation: rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/reports/independent_product_norm_rederivation.md.
- Hostile audit: rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/reports/product_cell_hostile_audit.md.
- Conductor reviews: the three Round-41 files under reviews/.
- Numerical work: none.

