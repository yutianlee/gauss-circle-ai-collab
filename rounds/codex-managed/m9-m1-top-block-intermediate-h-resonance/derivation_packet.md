# Round 56 derivation packet: discrete curvature resonances in the residual top-block core

This packet freezes the first unresolved range after the accepted Round-55
low-leg theorem. It asserts no new estimate.

## 1. Exact residual window

Let \(I_Y\subset[cY,CY]\cap\mathbb Z\), with

\[
 Y\asymp\sqrt X,\qquad R\asymp\sqrt Y,
\]

and let \(J\subseteq I_Y\) be consecutive with \(|J|\le R\), including
an edge window. Put \(L=(\log(2X))^B\). The residual coefficient is

\[
 W_J^{\rm core}=
 \sum_{\substack{hq\in J,\ q\ {m odd}\\h>L}}^{*}
 \chi_4(q)\Omega_X^*(hq,h)(hq)^{-3/4}e(\sqrt{Xhq}),
\tag{56.1}
\]

where

\[
 \Omega_X^*(hq,h)=\sum_j{\bf1}_{h\le H_j}
 \Phi\!\left({h\over H_j+1}\right)
 \left[w_j\!\left(2\sqrt{Xh/q}\right)\right]^*,
 \qquad H_j=\lfloor D_jX^{-1/4}\rfloor.
\tag{56.2}
\]

Actual support forces

\[
 q\ge4h,\qquad q\ge2\sqrt{hq},\qquad
 L<h\le {1\over2}\sqrt{hq}\asymp\sqrt Y.
\tag{56.3}
\]

The desired normalized window estimate is

\[
 |W_J^{\rm core}|\ll_\varepsilon X^\varepsilon Y^{-1/2}.
\tag{56.4}
\]

Equivalently, after removing \((hq)^{-3/4}\asymp Y^{-3/4}\), the
unweighted incidence sum must be \(O_\varepsilon(X^\varepsilon\sqrt R)\).

## 2. Exact fixed-h discrete phase

For fixed \(h\), split \(q=4m+\rho\), \(\rho\in\{1,3\}\), so
\(\chi_4(q)=\chi_4(\rho)\) is constant. Put

\[
 F_{h,\rho}(m)=\sqrt{Xh(4m+\rho)}.
\tag{56.5}
\]

The \(m\)-interval has length \(M_h\ll R/h+1\). In the top window,

\[
 |F_{h,\rho}''(m)|\asymp {h^2\over R},
 \qquad |F_{h,\rho}^{(3)}(m)|\asymp {h^3\over R^3}.
\tag{56.6}
\]

(The first comparison suppresses the fixed factor (4) created by the
step (q\mapsto q+4); only the scale is asserted.)

Round 55 used the continuous second-derivative estimate only for
\(h\le\sqrt R\) and the trivial length above it. The residual loss comes
from summing over many \(h\). For \(h>\sqrt R\), the continuous curvature
exceeds one and does not by itself imply cancellation on the integer
lattice. A legal new argument must work with exact discrete increments,
for example

\[
 \Delta F(m)=F(m+1)-F(m),\qquad
 \Delta^2F(m)=F(m+2)-2F(m+1)+F(m),
\tag{56.7}
\]

and retain their distance from integers, or use an exact completion/Weyl
inequality whose rational-approximation dependence is explicit.

## 3. Averaged-resonance target

The fixed-h family contains \(M_h\asymp R/h\) terms when nonempty. A
termwise \(O(\sqrt R)\) estimate is not summable over
\(L<h\ll\sqrt Y\). The candidate mechanism is to derive a bound

\[
 |T_h(J)|\le \mathcal R_X(h;J)
\tag{56.8}
\]

in which \(\mathcal R_X\) is small away from discrete quadratic
resonances, and then prove directly

\[
 \sum_{L<h\le\sqrt Y/2}\mathcal R_X(h;J)
 \ll_\varepsilon X^\varepsilon\sqrt R,
\tag{56.9}
\]

or a signed/bilinear analogue that is no stronger than necessary. The
average must be taken before replacing all resonance factors by their
worst case.

An acceptable no-go is an explicit infinite actual-profile family, away
from all hard/equality/product stars, for which the proposed resonance
majorant has larger capacity. Such a no-go must distinguish failure of
the majorant from a signed lower bound for (56.1).

## 4. Mandatory amplitude and boundary controls

- Carry (56.2), the height floors, the hard top, and all equality/radial
  stars. Round 55 proves sampled BV only on each fixed-leg product window;
  do not silently promote it to global BV in \(h\).
- Completion may add artificial endpoints. State their weights and costs;
  do not replace inherited stars by new half-weights.
- Treat \(X=K^4\) and centers near \(hq=K^2\). First derivatives can be
  integral or half-integral, and the discrete curvature can be close to a
  rational with small denominator.
- The already-proved \(h\le L\) margin must be excluded once. Do not
  reinsert it or double count the boundary \(h=L\).
- The result is physical. Alpha masks, connectors, Plemelj order, and
  outside-height limits remain separate.

No numerical experiment is needed. The round is 100% analytical.
