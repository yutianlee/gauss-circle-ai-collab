# Round 158 synthesis

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Starting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f
- Terminal label: paired_interior_cell_trace_no_go
- Graph mutation: applied
- Resulting graph: 8a0f917fb8117e9dbaf287d9f773046ff201729d2d8d8c3df1a51bca7815574b

## Outcome

Round 158 proves the exact sign-adapted moving-cell trace inside the
paired interior (D=d=L=1) nonzero theta matrix.  Positive-prefix and
negative-suffix Abel summation put the moving atom in with a positive
sign on both signed blocks.  The exact positive right outer endpoint,
negative left outer endpoint, and two profile-bulk remainders are
displayed and quarantined.

Complete half-period inversion gives

\[
\begin{aligned}
 \mathcal C_+^{\mathrm{full}}
 &=\sum_{j=a_+}^{b_+-1}F_j(j+1)
   \sum_{s=a_+}^{j}G_N((j+1)^2-s),\\
 \mathcal C_-^{\mathrm{full}}
 &=\sum_{j=a_-+1}^{b_-}F_j(-j)
   \sum_{s=j}^{b_-}G_N(j^2-s).
\end{aligned}
\tag{158.Y1}
\]

The individual (v=0) and (v=H/2) Abel-trace pieces are proved
directly, without transferring their whole-row theorems:

\[
 |\mathcal Z_{\mathrm{tr}}|+|\mathcal F_{\mathrm{tr}}|
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
\tag{158.Y2}
\]

## Endpoint face and strict survivor

The full-frequency endpoint face has polynomials (j^2+j+1) and
(j(j-1)).  The latter has two roots modulo every prime power.  The
former has no (2)-adic root, one root modulo (3) but none modulo
(9), and two simple roots modulo every (p^\nu) exactly for
(p\ne2,3) with (p\equiv1\pmod3).  Thus the endpoint face costs

\[
 O_\varepsilon(M^{-3/4}X^\varepsilon).
\tag{158.Y3}
\]

Deleting it, put

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell.
\tag{158.Y4}
\]

The exact strict selectors are

\[
\begin{aligned}
 \eta_+(\ell)&=
 \mathbf 1_{a_++1\le\kappa(\ell)\le b_+}
 \mathbf 1_{a_+\le r(\ell)\le\kappa(\ell)-2},\\
 \eta_-(\ell)&=
 \mathbf 1_{-b_-\le\kappa(\ell)\le-a_--1}
 \mathbf 1_{-\kappa(\ell)+1\le r(\ell)\le b_-}.
\end{aligned}
\tag{158.Y5}
\]

Their literal weights are

\[
\begin{aligned}
 W_+(k)&=w_U\!\left(\frac{k^2-k+1}{N}\right)
 e(\sqrt{k^2-k+1}-k),\\
 W_-(k)&=w_U\!\left(\frac{k^2+k}{N}\right)
 e(\sqrt{k^2+k}-k).
\end{aligned}
\tag{158.Y6}
\]

The character is evaluated at the quotient (ell), while the two
profile arguments lie on opposite sides of (ell).  They are neither
equal nor conjugate.  The accepted exact reduction is

\[
\boxed{
 \mathcal C_{\mathrm{int},U}(V)
 =\sum_{\ell\ge1}\chi_4(\ell)
 \left[\eta_+(\ell)W_+(\kappa(\ell))
      +\eta_-(\ell)W_-(\kappa(\ell))\right]
 +O_\varepsilon(M^{-1/4}X^\varepsilon).}
\tag{158.Y7}
\]

## Target calibration and qualified no-go

The strict support satisfies

\[
 L_{\mathrm{str}}(V)
 \ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{158.Y8}
\]

Literal boundary support makes the moving trace zero unless
(V\asymp K=\sqrt{NM}).  On that range (V\gg M), so the support
can still have size (M) and absolute summation gives only
(M^{1/4}X^\varepsilon).

The scalar target is (O_\varepsilon(X^\varepsilon)), not
(M^{-1/4}X^\varepsilon).  After removing the atom scale, the first
open trace theorem is raw

\[
 \left|\sum_{\ell\asymp M}\chi_4(\ell)
 \left[\eta_+(\ell)\widetilde W_+(\kappa(\ell))
      +\eta_-(\ell)\widetilde W_-(\kappa(\ell))\right]\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{158.Y9}
\]

Raw square-root cancellation would be sufficient but stronger.  The
explicit dyadic survivor proves only that a strict arithmetic selected
point may have a nonresonant endpoint; it is not a lower bound.

The named second-derivative, classical exponent-pair, and incomplete
quadratic placements require (M\ge N^{2/3}).  Even after favorable
fixed-endpoint, unit-BV, and residual-phase-BV grants, the most favorable
stated audited transformed line requires

\[
 M\ge N^{390/703}>N^{1/2}.
\tag{158.Y10}
\]

No audited primary theorem through 25 August 2026 matches the literal
root-indexed coefficient, both moving strict selectors, arbitrary even
composite modulus, quotient sign, and restored target.  The residual
boundary phases remain (k)-dependent coefficients, not fixed Fourier
shifts.  These are route-scoped upper capacities and a cutoff-dated
source no-match, not a lower bound or universal impossibility theorem.

## Remaining seams and proof status

The first open trace object is (158.Y9).  The positive right and
negative left Abel outer endpoints and both profile-bulk remainders are
separate open seams.  Therefore the full paired interior matrix and
every complete positive-power (D=1) range remain open.

The fixed-polylogarithmic collar is still the last proved complete
(D=1) range.  Every (D>1), (L>1), generic (t=1), original
(t\ge2), cross, remaining M1, and M2 owner remains separate.
Endpoint uniformity, M9, and the unconditional bridge remain open.

The internally proved global exponent remains (1/3).  The separately
audited external Li--Yang exponent remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{158.Y11}
\]

No global exponent changes in Round 158.

## Reviews and state effect

The independent blind reconciliation, independent trace mathematics,
hostile profile/power, repaired independent source, and terminal State
Patch scope reviews are GREEN for the narrow package.  The blind
report's conditional Weil capacities are not promoted.  The source
report was repaired so that residual phases remain inside the
coefficient and (390/703) is limited to the explicitly audited
favorable model.

The validated State Patch creates one proved-internal obstruction;
updates eight obligations; corrects one stale Round 157 rejected
record; rejects twenty-five new overbroad inferences; and records eight
principal downstream obligations unchanged.  The resulting graph is
8a0f917fb8117e9dbaf287d9f773046ff201729d2d8d8c3df1a51bca7815574b.
