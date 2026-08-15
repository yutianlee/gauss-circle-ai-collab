# Conductor review: mixed norm, traces, and exact Morse passage

Campaign: `m9-m1-beta-off-diagonal-product-cell`  
Round: 41  
Allocation: 100% analytical/algebraic

## Verdict

The off-diagonal singular remainder and every smooth ordinary-height cell
obey the target \(X^\varepsilon\lambda^{-2}\) mixed norm.  The decisive
point is to differentiate the endpoint divided difference before taking
absolute values.

With

\[
 D=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right),
 \quad Q=\frac{p(\nu)-p(L)}{L-\nu},
\]

put

\[
 R=\frac{p(L)-p(\nu)-p'(L)(L-\nu)}{(L-\nu)^2}.
\]

Then, at fixed physical \(\nu\),

\[
 \partial_L^\nu\left(\frac{GQ}{D}\right)
 =\frac{G'Q+GR}{D}+\frac{iGQ}{2D^2}.                  \tag{41.C9}
\]

This is the product specialization of the accepted fixed-height translation
identity.  It is not lawful to majorize its two mixed-derivative integrals
separately.

On either signed fixed-ratio cell, \(|L+\beta|\asymp\lambda\), split the
height line around the three separated centers

\[
 \nu=0,\qquad \nu=L,\qquad \nu=-L-2\beta.             \tag{41.C10}
\]

At the physical center, \(|L-\nu|\asymp|D|\asymp\lambda\), so the
integrable part of \(p(\nu)\) gives the limiting
\(O(P_X\lambda^{-2})\) value and
\(O(P_X\lambda^{-3})\) derivative.  At the top diagonal, Taylor's formula
is local and the cubic height tail gives at most
\(O(P_X\lambda^{-3})\).  At the radial ridge, both endpoint profile values
are \(O(P_X\lambda^{-3})\), the quotient contributes another
\(\lambda^{-1}\), and integrating \(|D|^{-1}\) costs only
\(\log(2+\lambda)\).  The complementary region has two separated
denominators or cubic height decay.  Hence

\[
 \sup_L\int|K_\Delta(L,\nu)|\,d\nu
 \ll P_X\lambda^{-2},\qquad
 \sup_L\int|\partial_L^\nu K_\Delta(L,\nu)|\,d\nu
 \ll P_X\lambda^{-3}.                                \tag{41.C11}
\]

The cell length is \(O(\lambda)\), so the integrated derivative is also
\(O(P_X\lambda^{-2})\).  For a smooth cell

\[
 K_W=\frac{G(L)p(\nu)W(L-\nu)}{D(L,\nu)},             \tag{41.C12}
\]

the translated spatial ridge lies at \(\nu\asymp L\), where the height
profile is cubic; at the physical and radial centers, \(W(L-\nu)\) is
rapidly decreasing.  Thus its value and derivative have at least one spare
inverse power.

For a moving physical face \(\nu=L-c\), the exact trace quotient is

\[
 Q_c(L)=\frac{p(L-c)-p(L)}{c},\qquad
 |D(L,L-c)|\asymp1+|L-c/2+\beta|,                    \tag{41.C13}
\]

with the derivative value at \(c=0\).  The physical-center, top-diagonal,
and radial-ridge trace centers are again separated, so uniformly in \(c\)

\[
 \int_{I_\lambda}|K_\Delta(L,L-c)|\,dL
 \ll P_X\lambda^{-2}.                                \tag{41.C14}
\]

The smooth trace is smaller.  In the intersection
\([-V,V]\cap[L-U,L+U]\), the upper moving face has positive sign and the
lower moving face negative sign.  Fixed faces have zero velocity; min/max
switches agree and collapsed sections vanish.

Finally use the exact signed Morse coordinate on a fixed-ratio cell.  If
\(J=dL/d\tau\), then \(J/\sqrt\lambda\) has bounded supremum and variation.
The normalized varying-amplitude remainder is bounded by the Fresnel
primitive and Stieltjes integration:

\[
 \|\mathfrak r^{\rm Morse}[K]\|_{L^1(d\nu)}
 \ll \sup_L\|K(L,\cdot)\|_1
 +\int\|\partial_L^\nu K(L,\cdot)\|_1\,dL
 +\text{moving traces}.                              \tag{41.C15}
\]

Equations (41.C11)--(41.C14) prove the desired bound for both Hessian
signs and through saddle entry or exit.  At an endpoint saddle the leading
coefficient is exactly the half-Fresnel value; no varying amplitude is
replaced by a scalar.

The polylogarithmic quantity \(P_X\) is absorbed by \(X^\varepsilon\).
The signed diagonal Cauchy term is excluded from every absolute integral
above and must be formed before the Morse operation.

## Downstream seam

This proves only the phase-removed large-alpha local mixed norm.  It may be
composed with the signed diagonal section and the already proved conditional
coefficient sum.  It does not estimate bounded-alpha, the double-bounded
cell, or the alpha-bounded transition branch.

