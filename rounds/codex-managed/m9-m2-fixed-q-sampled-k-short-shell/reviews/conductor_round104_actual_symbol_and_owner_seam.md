# Conductor review: actual-symbol sampled variation and owners

Campaign: m9-m2-fixed-q-sampled-k-short-shell

Starting graph SHA-256:
d2502a33224fbcb1fe3b8ffe0ea1227b953112fa0c98216597e8b0ccfa887372

## Decision

The uniform fixed-\(q\) actual-row theorem is certified. The proof is
specific to the literal coefficient and remains uniform at the collapsing
edge \(b/a\to4^{-}\).

For \(b=a+2q\asymp A\), \(q\asymp D\), rationalization gives

\[
 \delta_q\asymp {D\over\sqrt A},\qquad
 \Lambda_q={X\delta_q^2\over2}\asymp {J^2D^2\over A},
 \qquad K\asymp {JD\over A},\qquad G\asymp {L\over A}.
\]

The complete centered integral has the exact form

\[
 \mathfrak B^\circ_{a,q,k}(g)
 =\int Q_{a,q,g}(y)
 e\!\left(gk\left(y-{J\delta_q\over2k}\right)^2\right)dy.
\]

Its decisive identity is

\[
 k\partial_k e\!\left(gk(y-r_k)^2\right)
 ={y+r_k\over2}\partial_y e\!\left(gk(y-r_k)^2\right),
 \qquad r_k={J\delta_q\over2k}.
\]

It turns saddle motion into one physical derivative and proves, with the
literal homogeneous profile and both physical collars retained,

\[
 \sup_k|B_{a,q,g}(k)|+\operatorname{Var}_kB_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon\sqrt{AL\over JD}.
\]

The collar resolution is

\[
 {w_c^2\over(gK)^{-1}}\asymp {JD\over AL}\ge1.
\]

Thus the general-\(q\) factor improves rather than harms collar
resolution. This is not an arbitrary bounded-coefficient statement: a
phase-conjugated sequence can violate it.

## Collapsing-cone audit

Writing \(s=\sqrt{b/a}\in(1,2)\), the exact reciprocal interval has

\[
 |I_{a,q}|={J(s-1)(2-s)\over2s},
\]

while its saddle traverses a physical interval of length
\(\sqrt a(2-s)/2\). Both shorten together. The proof uses only
\(k\asymp K\) and \(\#(I_{a,q}\cap\mathbb Z)\ll K\), never a
reverse bound for the interval length. Overlapping collars retain the
same product seminorms; empty and singleton fibres are handled by zero
extension and the supremum bound. No factor \((2-s)^{-1}\) occurs.

## Owner audit

No previously accepted owner inserts a jagged exterior \(k\)-mask.

- \(q=0\) is the disjoint Round-75 diagonal.
- Primitivity, the square-ray owner, dyadic ownership, and the
  positive-safe condition are fixed once \((a,q)\) is fixed.
- At an exact nonsquare metric centre, the punctured factor is already
  zero, so the redundant deletion creates no variation jump.
- The metric annulus is opened as the complete periodic factor \(W_R\),
  rather than left as a sharp multiplier.
- Profiles, floors, stars, finite lift support, orientations, physical
  collars, and entry/exit are retained in the complete coefficient.
- The original reciprocal support is one open interval, and its zero
  extension has exactly two jumps.

The owner seam therefore passes on the literal interface.

## Row theorem

For one metric Fourier mode, \(n=|2\nu\mp g|\ge1\) because \(g\) is
odd, and

\[
 |f''_{\nu,g}(k)|\asymp {nA^2\over JD}.
\]

Weighted second derivative estimation gives

\[
 \sum_kB_{a,q,g}(k)e(f_{\nu,g}(k))
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{ALn}+\sqrt{L/A}\,n^{-1/2}\right).
\]

The complete Fourier half-moments cost \(\sqrt G\) and \(G^{-1/2}\).
The density mode \(\nu=0\) is included and has \(n=g\). Hence one
lift costs \(O_\varepsilon(X^\varepsilon(L+1))\), and the \(O(G)\)
actual lifts give

\[
 \boxed{|F_a(q)|\ll_\varepsilon X^\varepsilon {L^2\over A}}.
\]

This theorem is uniform for real \(X\), all active fixed-\(q\) rows,
both orientations, and the cone edge. No external theorem is imported.

## Scope

The proof certifies the fixed-\(q\) row and its row-energy consequence.
It does not estimate the signed correlation between distinct \(q\)-rows
and does not close a polynomial \(q\)-shell, the canonical M2 energy,
M9-M2, M9, or a new global exponent.
