# Round 75 synthesis

Round 75 corrects the proposed top-(M2) near-product transform and
isolates an exact character-preserving replacement.

The quarter-shift phase algebra and leading coefficient are correct, but
the angular amplitude is not constant at the saddle.  Its first omitted
Gaussian term is (g''(t_0)/(8\pi ixl)), generally nonzero and only
(J^{-1}) below the leading normalized symbol on the narrowest collar.
Therefore (75.7)--(75.10) is not an all-orders identity as written.  An
exact Fresnel symbol or a finite stationary package can plausibly repair
it; the necessary complete seminorm theorem is not accepted here.

The exact finite replacement is obtained before any transform.  Define

\[
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
 \chi_4(h)a(h,m)e(\sqrt{Xhm}).
\]

Then

\[
 \mathcal T_L=\sum_mR_m,qquad
 |\mathcal T_L|^2\ll L\sum_m|R_m|^2.
\]

The diagonal of the energy is (O(L^2)), and its exact positive-offset
part is

\[
 2\Re\sum_{r\ge1}(-1)^r
 \sum_{\substack{h,h+2r\in\mathscr H_L}}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 a(h,m)\overline{a(h+2r,m)}
 e\!\left(-\frac{2r\sqrt{Xm}}{\sqrt h+\sqrt{h+2r}}\right).
\]

Thus the remaining sufficient estimate is

\[
 \sum_m|R_m|^2\ll_\varepsilon L^2X^\varepsilon.
\]

This reduction is exact, keeps the hard affine edges and actual profile,
and preserves the character through
(\chi_4(h)\chi_4(h+2r)=(-1)^r).

For a repaired dual symbol, periodized Parseval gives the diagonal (LJ)
and an alternating reciprocal overlap.  The active modes are negative;
the high-character B-process returns, with unit (e(-1/8)), to the same
transposed-row energy.  Hence the reciprocal energy is an adjoint return,
not a new source of cancellation.  Its signed off-diagonal remains open,
and no audited source supplies the missing bound.

State effect: promote the finite transposed-row reduction; reject the
literal leading-symbol all-orders claim and coefficient-only energy
shortcuts; retain the top cone, full (M2), (M9), and the exponent
open.  The next round should attack the alternating even-offset energy
directly, before taking absolute values over (r).

