# Round 102 conductor review: normalization and determinant

Starting graph SHA-256:
fbe0e9b9e4db078128f75d97b790dd78a6adc8216c7b0b14c4fad928925637ca

## Exact Gram

All three reports independently recover

\[
 \mathcal G_H^{\rm act}
 =H E_{\rm act}
 +2\Re\sum_{1\le s<H}(H-s)(-1)^s C_s^{\rm act}.
\]

Zero extension owns every support entry and exit. The bridge

\[
 \left|\sum_{a,q}(-1)^qF_a(q)\right|^2
 \ll {A(D_{\rm ray}+H)\over H^2}\mathcal G_H^{\rm act}
\]

and

\[
 E_0\asymp LJD_{\rm ray}^2,\qquad
 \rho={AJD_{\rm ray}^3\over L^3}
\]

return exactly the desired \(L^4\) squared linear target. No power is
missing in the frozen normalization.

If the diagonal is bounded separately by \(HE_0\), then it fits only
when \(H\gtrsim\rho\). Since \(H\le D_{\rm ray}\), a post-diagonal
absolute-value proof is confined to \(\rho\lesssim D_{\rm ray}\).

## Carrier and complete metric phase

For

\[
 b=a+2q,\qquad b_s=b+2s,\qquad
 \Lambda_q={X(\sqrt b-\sqrt a)^2\over2},
\]

the extracted carrier satisfies

\[
 \Psi_s''(q)
 =-{X\sqrt a\over2}
 \left({g'\over k'b_s^{3/2}}-{g\over kb^{3/2}}\right)
\]

up to the harmless reversal from conjugating both orientations. This
is an exact carrier identity.

It is not the full density-discrepancy phase unless the complete metric
factor remains in the amplitude. Expanding

\[
 W_R(t)=\sum_{\ell\in\mathbb Z}\widehat W_R(\ell)e(\ell t)
\]

replaces \(g,g'\) by the effective odd parameters
\(g-2\ell,g'-2\ell'\). The complete determinant is therefore

\[
 {g'-2\ell'\over k'b_s^{3/2}}
 -{g-2\ell\over kb^{3/2}}.
\]

This correction is mandatory. Round 77 gives bounded variation in the
odd lift \(g\), not in \(q\), so the unexpanded complete metric factor,
moving intervals, primitive and owner masks, and centred entry/exit
integrals are not a lawful slow \(q\)-amplitude.

## Exact zero and spacing

For the density carrier, write \(N=GK\). Exact zero is equivalent to

\[
 b=dx^2,\qquad b_s=dy^2,\qquad
 d(y^2-x^2)=2s,\qquad
 g'kx^3=gk'y^3
\]

for one squarefree \(d\). For fixed \(a,s\), there are
\(O_\varepsilon(s^\varepsilon)\) base points and
\(O_\varepsilon(NX^\varepsilon)\) lift quadruples per base point.
This was proved independently in the conductor candidate, blind
post-isolation audit, discovery addendum, and hostile addendum.

For \(0<\eta\le1\),

\[
 \#\left\{(g,k,g',k'):
 \left|{g'k\over gk'}-\left({b_s\over b}\right)^{3/2}\right|
 \le\eta\right\}
 \ll_\varepsilon X^\varepsilon(\eta N^2+N).
\]

On common dyadic boxes, \(|\Delta_0|\le\lambda\) corresponds to

\[
 \eta\asymp \lambda {K\over G}A^{3/2}.
\]

At the natural quadratic threshold
\(\lambda\asymp(X\sqrt A D_{\rm ray}^2)^{-1}\), the raw density-mode
count is \(O_\varepsilon(NX^\varepsilon)\) per fixed base. This is a
real incidence saving, but it is neither coefficient-weighted nor
mode-resolved.

Nonzero algebraic rationalization gives only

\[
 |\Delta_0|\gg (GK^3A^{9/2})^{-1},\qquad
 |\Psi_s''|\gg(LJD_{\rm ray}^3)^{-1}.
\]

Thus the guaranteed quadratic phase change on a length-\(D_{\rm ray}\)
row is only \((LJD_{\rm ray})^{-1}\), below one.

At a density-carrier zero with \(s>0\),

\[
 |\Psi_s'''(q)|
 ={3X\sqrt a\over2}c\left({1\over b}-{1\over b_s}\right)
 \asymp {JL s\over D_{\rm ray}A^3},
\]

where
\[
 c={g\over kb^{3/2}}={g'\over k'b_s^{3/2}}.
\]

This is exact under the common-block comparabilities. It diagnoses a
simple carrier crossing but does not yield a derivative estimate for
the complete moving mode-resolved multiplier.

## Decision

The normalization, carrier derivative, exact-zero classification, raw
near-incidence, and simple-crossing algebra pass. No complete actual
Gram estimate follows. The graph may record these facts only inside a
narrow route-obstruction or auxiliary statement.
