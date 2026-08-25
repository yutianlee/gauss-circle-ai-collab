# Round 162 synthesis: character Poisson, the scaled product collar, and the signed local-divisor frontier

Round 162 closes under
**`hard_top_t1_close_factor_bilinear_no_go`**.  The validated State Patch
creates one proved-internal obstruction, updates two open hard-TOP parents
with inconclusive evidence, records twelve rejected overclaims, and
preserves sixteen explicit no-change decisions.  The resulting graph is
`700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358`.

## What was proved

For the literal (t=1) squarefree, coprime close-factor scalar, the exact
projector is

\[
\mu^2(d_1)\mu^2(d_2)\mathbf1_{(d_1,d_2)=1}
=\sum_{a^2\mid d_1}\mu(a)
 \sum_{b^2\mid d_2}\mu(b)
 \sum_{c\mid(d_1,d_2)}\mu(c).
\]

Writing (Q=[a^2,c]), (R=[b^2,c]), (d_1=Qm), and (d_2=Rn), only
the first leg is forced odd; the even-(d_2) branch survives.  Exact
character Poisson is

\[
 \boxed{
 \sum_m\chi_4(m)g(m)
 =\frac i2\sum_{s\ \mathrm{odd}}\chi_4(s)\widehat g(s/4).}
\]

The character is transferred to the odd dual variable, not removed.  Its
positive saddle is

\[
 d_1^*=\frac{4XQ^2d_2}{s^2},\qquad
 F_s(d_1^*/Q)=\frac{XQd_2}{s},\qquad
 JQ\le s\le2JQ,
\]

with exact profile (W(XQ/(ys))) and normalized stationary factor

\[
 \frac{2L^{3/2}J^{-1/2}}{Qd_2}.
\]

The exact character transform is involutive.  Fourier scaling, the two
(i/2) factors, and odd character reflection return the original sum, so
a second bare transform supplies no contraction.

The product phase has rank-one Hessian and radial null direction.  On
every compact smooth interior cell of a fixed opening, simultaneous
dualization gives

\[
 s\ell=XQR,\qquad Q\ell\le Rs\le4Q\ell,
\]

and physical radial length (L) gives the product collar

\[
 \boxed{|s\ell-XQR|\ll QRJ/L.}
\]

The collar has at most

\[
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon
\]

factor pairs, while one smooth-interior coefficient has scale

\[
 \frac{L^{3/2}}{QR\sqrt J}.
\]

The (QR)-powers cancel.  Termwise positive control therefore has
capacity

\[
 \sqrt{JL}\,X^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)X^\varepsilon.
\]

The favorable coefficient-insensitive comparison is

\[
 \min\{L^2,\sqrt{JL}\}
 =L^{3/2}\min\{L^{1/2},H/L\}(1+o(1)).
\]

This is a route capacity, not a bound or lower mass for the complete
physical scalar.

Grouping by (N=s\ell) isolates the exact moving near-square window

\[
 \sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\mathcal K_{Q,R}(N;s).
\]

Completing it to (r_2(N)/4) adds an uncontrolled complementary divisor
window.  Standard positive differencing also supplies no character gain,
because (\chi_4(d+2h)\chi_4(d)=(-1)^h) is constant in (d).

## What was ruled out

The round parks the following direct continuations:

- exact Möbius opening followed by termwise positive one- or two-variable
  Poisson control;
- a second bare character transform;
- standard differencing followed by positive norms;
- free (Q,R)-summation or completion of the local divisor window;
- the audited direct Bombieri--Iwaniec, Kowalski--Robert--Wu,
  Robert--Sargos, Duke--Friedlander--Iwaniec, Bettin--Chandee, and
  Dong--Robles--Zeindler placements.

The direct real-monomial cards fail after power restoration.  The DFI and
DRZ cards have no uniform literal placement for the arbitrary-real
ordinary reciprocal.  Bettin--Chandee has a formal degenerate placement
on an integral subcase, but its printed parameter factor is already
((JL)^{1/2}), before the remaining powers and physical normalization.
These statements exclude only the audited placements, not future or
bespoke coefficient-sensitive theorems.

The accepted kernel deliberately does not claim that all literal hard
edges are target-safe.  Nonzero zero-extension endpoints, saddle-edge
transitions, stars, profile entries and exits, nonstationary pieces, and
opened boundary cancellations remain inside the open signed aggregate.

## Proof status

The (t=1) target remains open:

\[
 \boxed{|\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon.}
\]

The first required new input is a target-strength theorem for the entire
signed Möbius-coupled (Q,R)-scaled local divisor family, with the
arbitrary-real centre, even-(d_2) branch, actual profiles, hard edges,
floors, stars, endpoint transitions, collar tails, and nonstationary
pieces retained before every positive norm.  It must recover the factor

\[
 \min\{L^{1/2},H/L\}
\]

missed by the favorable positive ledger.

Even a proof of that face would leave the compatible
(L\ll D\ll L^2), (t\ll\sqrt L) few-point radical channels and their
near-collision collars open.  Therefore hard TOP remains open.

The three mandatory M9--M2 parents remain:

1. hard-TOP density-discrepancy/signed-cone control;
2. balanced smooth quarter-packet control;
3. unbalanced smooth three-quarter control.

M9--M1 also remains open, with its two direct blockwise parents or the
alternative global-M1/GAR route still incomplete.  Endpoint uniformity,
M9, the conditional bridge, and the quarter theorem remain open.

The strongest internally proved global exponent remains (1/3).  The
separately audited external benchmark remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\]

No global exponent improved in Round 162.

## Reviews and state effect

The statement-only rederivation, post-unmask coefficient/collar review,
independent power/involution review, primary-source/graph review,
conductor adjudication, and terminal State Patch audit are GREEN.  No
numerical experiment was used.

The accepted kernel is

`proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`.

The State Patch creates:

- `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.

It attaches that node only as a dependency and inconclusive evidence to
the two open hard-TOP parents.  No accepted antecedent, smooth packet,
downstream theorem, bridge, target, or exponent is promoted.

## Next research interface

The next admissible attack on this face is the exact signed near-square
divisor aggregate before Möbius separation and positive norms.  A useful
new route must exploit a property of the actual (\chi_4)-weighted,
squarefree product coefficient that fails on coefficient-uniform arrays;
another bare transform, divisor completion, or positive collar count is
already certified as a self-return or power loss.
