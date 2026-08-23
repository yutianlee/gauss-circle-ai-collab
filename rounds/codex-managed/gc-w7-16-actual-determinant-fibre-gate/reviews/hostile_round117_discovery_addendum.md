# Hostile addendum: audit of the Round-117 discovery bounds

Campaign: `gc-w7-16-actual-determinant-fibre-gate`

Artifact audited:
`reports/actual_character_determinant_attack.md`, specifically
(117.14a)--(117.14g) and (117.15)--(117.21).

Starting graph SHA-256:
`a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9`

## Decision

**Pass, with one formal clarification and no fatal mathematical flaw
found.**  The full-block estimate

\[
 \mathcal C_i(c),\ |\mathfrak O_i|
 \ll_\varepsilon
 \left({D^2\over L^2}+{WD\over L}\right)Y^\varepsilon
\tag{A.1}
\]

is valid for the stated fixed literal block and real centre.  The
bounded-lift top reduced-denominator estimate

\[
 |\mathfrak O_{i,B\asymp D}|
 \ll_\varepsilon D
 \min\left(Q_*,Q_*\sqrt\lambda+\lambda^{-1/2}\right)Y^\varepsilon
\tag{A.2}
\]

also passes, provided the finite-lift weight is explicitly extended to
nonprimitive pairs before the Möbius identity is applied.  This extension
is harmless and has the claimed bounded variation, but it should be stated
in the conductor version of the lemma.

At minimax these remain (Y^{37/48+\varepsilon}) and
(Y^{35/48+\varepsilon}), respectively.  Neither reaches the
(Y^{1/2+\varepsilon}) target or changes the pointwise exponent.

## Full-block product-window audit

For one cell and one fixed denominator, its intersection with a literal
dyadic numerator support is a union of (O(1)) integer intervals of total
length

\[
 T_0\ll\min(L,D/W),
\]

with an additional fixed factor four in (M2).  After extracting
(L^{-1}), the Vaaler/profile weight has bounded discrete supremum plus
variation.  Hard support entry, exit, and a prescribed endpoint sample
add only bounded jumps.  Discrete Abel therefore proves (117.14c) and
(117.14d) without smoothing or a Poisson endpoint convention.

The real-centre count in (117.14e) is sound.  If

\[
 \|c/d\|<\eta,
\]

then an integer (r) satisfies

\[
 |c-rd|\ll\eta D.
\]

The interval about the real number (c) contains
(O(1+\eta D)) integers, and each such integer has
(O_\varepsilon(Y^\varepsilon)) admissible divisor pairs.  For (M2),

\[
 \left\|{c\over4d}\mathbin\pm{1\over4}\right\|<\eta
\]

gives the same product window with (r) in one odd residue class modulo
four.  This can only reduce the count.  Dyadic layer-cake summation gives

\[
 T_0N(T_0^{-1})+
 \sum_{T_0^{-1}\lesssim\eta\le1/2}
 \eta^{-1}N(2\eta)
 \ll_\varepsilon (D+T_0)Y^\varepsilon
 \ll_\varepsilon DY^\varepsilon,
\]

which is (117.14e), uniformly for arbitrary real (c\asymp Y).

No denominator, lift, or character cancellation is assumed after this
count: the original ((h,d)) sum already contains every lift, and the
remaining denominator weights are bounded before taking their triangle.
Thus every cell costs (D/L).  The positive and negative frequency bands
meet at most

\[
 O(1+WL/D)
\]

cells for every random shift; if they share a cell, the elementary
two-term square inequality costs only a constant.  Squaring the uniform
cell bound and integrating the random shift proves (117.14g).

Finally,

\[
 \mathcal C_i=\mathcal E_{i,=}+\mathfrak O_i,
 \qquad \mathcal E_{i,=}\ll_\varepsilon D/L.
\]

Hence

\[
 |\mathfrak O_i|\le \mathcal C_i+\mathcal E_{i,=}.
\]

Because (L\le DY^{-1/4}), one has (D/L\ge1), so
(D/L\le D^2/L^2).  The diagonal is therefore absorbed in (A.1).  The
absolute-value deduction is valid, although this absorption should be
shown when (A.1) is quoted independently.

## Bounded-lift top-shell audit

On (b,b'\asymp D) and (|a|,|a'|\asymp L), the simultaneous original
supports (gb\asymp D) and (g|a|\asymp L) restrict (g) to a fixed
finite set.  After expanding it, each (b')-weight at fixed (a') has
supremum plus total variation (O(L^{-1})).  Zero-extension counts each
profile or hard-top entry and exit once.  The triangular factor also has
bounded variation: on its clipped interval its derivative has total mass

\[
 \ll {WLQ_*\over D^2}\ll1.
\]

For fixed (a'), define the same finite-lift formula on all integer
(b'), not merely on primitive pairs.  Then

\[
 {\bf 1}_{(a',b')=1}
 =\sum_{\rho\mid a',\,\rho\mid b'}\mu(\rho)
\]

is a literal identity.  With (b'=\rho v), the interval length is
(O(Q_*/\rho)) and

\[
 \left|{d^2\over dv^2}\left(-{ca'\over\kappa_i\rho v}\right)\right|
 \asymp {YL\rho^2\over D^3}=\lambda\rho^2.
\]

The weighted second-derivative estimate therefore gives, for one divisor
progression,

\[
 {1\over L}\left(Q_*\sqrt\lambda+
 {1\over\rho\sqrt\lambda}\right).
\]

Summing the first term with \(\tau(a')\), the second with
\(\sigma_{-1}(a')\), and comparing with the similarly summed trivial
bound proves (117.21).  In M1, \(\rho\) is odd and
\(\chi_4(\rho v)\) supplies exactly the two linear quarter shifts; in
M2, no denominator character is inserted.  These shifts leave the
second derivative unchanged.  Both signs of (a') merely reverse the
curvature sign, not its magnitude, and (kappa_2=4) changes only fixed
constants.

There are (O(LD)) outer primitive rays, (O(L)) possible numerator
increments (p), outer coefficient size (O(L^{-1})), and inner bound
(V/L).  Their full triangle is exactly

\[
 (LD)\,L\,L^{-1}\,{V\over L}=DV.
\]

No missing Cauchy, gcd, lift, or boundary factor was found.  The proof is
restricted essentially to (B\asymp D); for (B<D), the lift set is no
longer finite and this BV argument does not apply.

## Pass/fail table and first seam

| Seam | Outcome | Reason |
|---|---|---|
| Real-centre product-window count | **Pass** | Integer products (rd) lie in a real interval of length (O(\eta D)); divisor bounds and layer cake give (D Y^\varepsilon). |
| M1/M2 phases and constants | **Pass** | M1 uses (c/d); M2 uses (c/(4d)\pm1/4). The factor four and odd residue classes are retained. |
| Profiles, hard endpoints, and stars in (117.14) | **Pass** | Discrete Abel needs only sampled BV; every endpoint is one bounded jump. No Poisson boundary is discarded. |
| Both frequency signs | **Pass** | Two bands cost a fixed factor, including the possible shared-cell case. |
| Random-cell squaring | **Pass** | The cell estimate is uniform in the random shift and only (O(1+WL/D)) cells are nonempty. |
| Deduction of (|\mathfrak O_i|) | **Pass** | Use (|\mathfrak O_i|\le\mathcal C_i+\mathcal E_{i,=}), and absorb (D/L) into (D^2/L^2). |
| Finite lift expansion at (B\asymp D) | **Pass** | Both original support conditions force (g=O(1)). |
| Möbius/gcd progressions | **Pass after clarification** | Define the finite-lift weight on nonprimitive pairs before inserting the coprimality indicator. |
| Reciprocal curvature and divisor sums | **Pass** | Length \(Q_*/\rho\), curvature \(\lambda\rho^2\), and \(\tau,\sigma_{-1}\) costs reproduce \(V/L\). |
| Outer-ray/increment capacity | **Pass** | The complete visible triangle is (DV); no claimed target closure follows. |
| Extension to (B<D) | **Fail, as already scoped** | Long lift ranges can contribute unowned variation (D/B); (A.2) must remain a top-shell lemma. |
| Global exponent or M9 implication | **Fail, as required** | (37/48) and (35/48) both exceed (1/2), and the graded block theorem is not an M9 parent. |

The first presentation seam is the nonprimitive extension needed in
(117.15); it is repairable and not a mathematical obstruction.  The first
genuine unproved step remains the long-lift lower-shell estimate or a
further joint signed saving beyond (A.2).  No state mutation is authorized
by this review alone.
