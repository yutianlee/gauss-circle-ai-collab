# Conductor candidate: complete primitive dual-square transfer

Campaign: m9-m2-dual-square-actual-symbol-transfer

## Candidate kernel

For each maximal subinterval \(I\subset[D,2D)\), transform the literal
row only after exact Möbius decomposition. The candidate dual kernel is

\[
\begin{aligned}
 \mathcal D_{a,I}
 =\sum_{d\mid a}\mu(d)
 \sum_{g,\nu,\ell,s}
 \widetilde{\mathcal A}_{a,d,g,\nu,I}(\ell,s)
 e\!\left(
 -\left(J\sqrt{dn\ell/s}
 -{1\over2}\sqrt{as/d}\right)^2\right),
\end{aligned}
\]

where \(n=|2\nu\pm g|\) is odd, \(s\) is odd, and every literal actual
owner is transported into \(\widetilde{\mathcal A}\).

The first candidate normalization of the principal stationary symbol is

\[
 e(1/8)\,
 {g^{1/2}b_*^{3/4}\over
 dJ^{1/2}n^{3/4}\ell^{1/4}}\,
 A^\circ_{ga,gb_*}(g\ell/n),
 \qquad b_*={4d^2Xn\ell\over s^2}.
\]

This formula is not accepted until all three stationary operations and
their transition regimes are audited.

## Required gain

The desired bound is

\[
 \sup_I|\mathcal D_{a,I}|
 \ll_\varepsilon X^\varepsilon L^2/A.
\]

A mode-level \(\ell^2\) estimate gains only \(\sqrt D\), while the
fixed-\(a\) Gram requires the full factor \(D\) over rowwise capacity.
Any claimed saving must therefore use the literal dual character,
the actual profile geometry, or cancellation across metric modes and
owners before absolute values.

## Competing outcomes

1. The complete dual kernel is terminal under an existing exact theorem.
2. A new direct signed estimate closes a strict polynomial range.
3. The full transform reassembles owner by owner to the original weighted
   shift Gram at equal capacity.
4. A specific owner or transition prevents a uniform two-step transform,
   leaving a smaller exact mixed primal-dual kernel.

The campaign must distinguish these outcomes and may not treat scalar
Hessian full rank as an analytic estimate.
