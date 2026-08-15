# Conductor review: exact phase and profile factorization

Campaign: `m9-m1-beta-off-diagonal-product-cell`  
Round: 41  
Allocation: 100% analytical/algebraic

## Verdict

The frozen post-routing terminal numerator has the exact product structure
needed for the Round-41 estimate.  No arithmetic, radial, contour, floor,
star, or external physical normalization is absorbed into the local symbol.

Put

\[
 u=a+i(L-\nu),\qquad v=b+i\nu,\qquad
 s=\frac54+i\left(\frac L2+\beta\right).
\]

The unit-modulus powers in the raw numerator combine as

\[
\begin{aligned}
 &(L-\nu)\log\frac{D_j}{2\sqrt X}
 +\nu\log(H_j+1)-L\log q-\beta\log(hq)
 -\frac12(L+\nu+2\beta)\log x\\
 &=L\log\frac{D_j}{2q\sqrt{Xx}}
 +\nu\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}
 -\beta\log(hqx).
\end{aligned}                                      \tag{41.C1}
\]

Thus the true height profile is

\[
 p(\nu)=e^{i\gamma\nu}\widehat\phi(b+i\nu),\qquad
 \gamma=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x},       \tag{41.C2}
\]

not merely \(\widehat\phi(b+i\nu)\).  The actual scale ranges give
\(|\gamma|\ll\log(2X)\).

The accepted exact diagonal gamma factorization separates the bounded
\(\beta\)-ratio from the large \(\alpha=L+\beta\) ratio.  On either fixed
signed ratio cell \(|\alpha|\asymp\lambda\), where
\(\lambda=\pi q\sqrt{Xx}/D_j\), remove the canonical signed Stirling
main phase \(\Psi_\pm\), characterized by
\(\Psi_\pm'(L)=\log(|L+\beta|/\lambda)\), together with
\(\lambda^\kappa\), with
\(\kappa=3/4+(a+b)/2\).  Differentiated Stirling then gives

\[
 |\partial_L^mG_\pm(L;\lambda)|\ll_m\lambda^{-m},
 \qquad 0\le m\le2,                                  \tag{41.C3}
\]

uniformly through fixed-ratio entry and exit collars.  The bounded beta
ratio and compact mask derivatives contribute only polylogarithmic factors.

For the height profile, the accepted Vaaler transform satisfies, for the
orders used here,

\[
 |\partial_\nu^m p(\nu)|
 \ll b^{-C_m}(1+|\gamma|)^{m}(1+|\nu|)^{-3},
 \qquad 0\le m\le3.                                  \tag{41.C4}
\]

The required smooth spatial condition is the finite seminorm

\[
 \sup_{0<a\le a_b}\sup_{y\in\mathbb R}
 (1+|y|)^N|\partial_y^m\mathscr W_j(a+iy)|<\infty,
 \qquad m\le2,                                       \tag{41.C5}
\]

for one fixed sufficiently large \(N\).  It holds uniformly in the actual
interior dyadic family because every interior profile is the same fixed
\(C_c^\infty\) rescaling.  It also holds for the top regular remainder:

\[
 \widehat W_+(u)=\frac1u-\frac1u\int_0^1W'(t)t^u\,dt,  \tag{41.C6}
\]

and \(W'\) is smooth with compact support away from both endpoints, so
vertical integration by parts gives (41.C5).  The isolated \(1/u\) term is
the singular hard-top share and is not included in (41.C5).

Consequently the post-routing local cells are exactly finite sums of

\[
 G(L)p(\nu),\qquad G(L)p(\nu)W(L-\nu),                 \tag{41.C7}
\]

up to a bounded compact-beta coefficient.  The common artificial package
must first be simplified by

\[
 \omega G_{\rm com}+(1-\omega)R_1-\omega E_1=R_1,
 \qquad G_{\rm com}=E_1+R_1.                          \tag{41.C8}
\]

The accepted ownership graph has already routed connector-axis, crossed
artificial-residue, endpoint, side, arithmetic, axial, collision, and corner
modules outside this local terminal cell.  Reintroducing them into (41.C7)
would double count the global decomposition.  A retained pure beta mask or
beta connector changes only the bounded compact coefficient.

The factors left outside (41.C7) are exactly: \(\chi_4(q)\), the real
\(h,q,D_j,H_j,x\) monomial, the stationary numerator
\((D_j/q)\lambda\), radial and beta integrations, residual contour
constants, floors, stars, the oscillatory radial phase, and
\(-(4/\pi)X^{1/4}\operatorname{Re}\{e(1/8)\,\cdot\}\).

## Scope

This review certifies the large-\(|\alpha|\) post-routing product
factorization and uniform profile seminorms only.  Bounded-alpha,
double-bounded, and complete transition assembly are not included.
