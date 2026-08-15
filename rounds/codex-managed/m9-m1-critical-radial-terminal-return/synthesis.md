# Round 60 synthesis: smooth critical radial sectors are terminal

Campaign: `m9-m1-critical-radial-terminal-return`

## Conductor decision

Promote the exact Mellin transfer from every fixed smooth critical radial
sector to the already proved terminal M1 divisor theorem.  The result is
stronger than the frozen real-projection target: the accepted unpaired
positive-frequency transform gives the complex modulus

\[
 \left|\sum_{n\le16\sqrt X}V(n/\sqrt X)\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn})\right|\ll_{\varepsilon,V}X^\varepsilon
\]

for every fixed (V\in C_c^\infty((c,C))), (0<c<C<16).

## Mechanism

Writing (R=X^{1/4}), (Y=\sqrt X), the stationary relation is

\[
 n={4Xh^2\over d^2}.
\]

On (V(n/Y)\ne0), this forces (h\gg_VH_j\), while the exact inherited
condition (h\le H_j\) supplies the upper edge.  Mellin inversion gives
the separable coefficient

\[
 \eta_j(h)\mathbf1_{h\le H_j}{\Phi(h/(H_j+1))\over h}h^{2it}
 \quad\hbox{and}\quad
 \chi_4(d)w_j(d)d^{-2it}.
\]

Its frequency sup-plus-variation norm is
\(O_V((1+|t|)/H_j)\), and its denominator coefficient is bounded.
The terminal theorem therefore bounds the full positive antecedent by
\(O_{\varepsilon,V}(RX^\varepsilon)\).

At (d_*=2\sqrt{hX/q}\), the Mellin mode becomes exactly

\[
 (4X/Y)^{it}h^{2it}d_*^{-2it}=(hq/Y)^{it},
\]

and

\[
 (hX)^{1/4}q^{-3/4}h^{-1}=R(hq)^{-3/4}.
\]

Thus the accepted positive-frequency interior and one-sided top
transforms give

\[
 \sum_j\mathcal B_{j,V}
 ={e(1/8)\over i}R\mathcal G_V+O_V(\log^2X),
\]

with the hard-top cotangent boundary retained separately as (O_V(1)\).
All floors, profile overlaps, hard samples, and stars retain exact
one-count ownership.  Dividing by (R\) proves the modulus.  Pairing
frequency signs recovers the frozen real GAR projection and the exact
external coefficient (-4R/\pi\).

## Scope

This is a genuine estimate, not a return-map restatement, because the
positive antecedent is bounded directly before transformation.  It closes
all fixed smooth (n\asymp\sqrt X\) sectors compactly inside
\((0,16\sqrt X)\).  It does not close the endpoint at (16\sqrt X\), a
sharp radial window, the limit (n/\sqrt X\to0\), the alpha transition,
full GAR, blockwise M9-M1, M9, or the final exponent.

No numerical experiment or new external theorem was used; the round was
entirely analytic.

