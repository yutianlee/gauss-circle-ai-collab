# Round 103 conductor normalization and sampled-\(k\) review

Starting graph SHA-256:
`902eb43bc0fc72b1c3e080dac5cd89757d17e2eaa1f72d606b89afbecff92935`

## Exact geometry

Rationalization gives

\[
 \delta_a^2={2\over a+1+\sqrt{a(a+2)}},\qquad
 \Lambda_a={X\over a+1+\sqrt{a(a+2)}}\asymp {J^2\over A}.
\]

The reciprocal interval is

\[
 I_a=\left({J\delta_a\over2\sqrt a},
            {J\delta_a\over\sqrt{a+2}}\right),
\]

so \(k\asymp K\asymp J/A\). With
\(r_k=J\delta_a/(2k)\), its two open endpoints map exactly to
\(r_k=\sqrt a\) and \(r_k=\sqrt{a+2}/2\). The factor \(1/2\), phase
orientation, and saddle entry/exit are correct.

## Complete-Fresnel normalization

After \(u=y^2\), the centered integral is a quadratic transform

\[
 T_{gk}q_{a,g}(r_k)
 =\int q_{a,g}(y)e(gk(y-r_k)^2)\,dy.
\]

The literal symbol has height and total variation
\(O_\varepsilon(X^\varepsilon g\sqrt A)\). Its physical collar has
width \((g\sqrt A)^{-1}\), while

\[
 gk(g\sqrt A)^{-2}\asymp {J\over AL}\ge1.
\]

The exact quadratic-kernel identities used in Round 78 therefore give

\[
 \sup_k|B_{a,g}(k)|+\operatorname {Var}_kB_{a,g}(k)
 \ll_\varepsilon X^\varepsilon{g\sqrt A\over\sqrt{gK}}
 \asymp X^\varepsilon\sqrt{AL/J}.
\]

This is a complete-integral estimate. It contains both incomplete-
Fresnel transitions and has no stationary-expansion remainder.

## Power ledger

For \(n=|2\nu-g|\), the reciprocal curvature is

\[
 |f''|\asymp nA^2/J.
\]

The second-derivative bound, multiplied by
\(V=\sqrt{AL/J}\), is

\[
 \sqrt{ALn}+\sqrt{L/A}\,n^{-1/2}.
\]

The two Fourier moments contribute \(\sqrt G\) and \(G^{-1/2}\),
respectively. Thus one lift costs \(L+1\), one row costs
\(G(L+1)\ll L^2/A\), and \(O(A)\) rows cost \(L^4/A\) in energy.
All powers and the singleton normalization pass.

## Decision

The normalization, complete-Fresnel sampled variation, Fourier moments,
and energy arithmetic are correct. The candidate is eligible for the
owner/control review; no exponent or longer-row implication is present.
