# Conductor Round-162 adjudication

## 1. Result and terminal decision

**Terminal verdict:**
`hard_top_t1_close_factor_bilinear_no_go`.

Round 162 does not prove the literal (t=1) target, a strict hard-TOP
sector, or a physical lower bound.  It promotes one narrower obstruction:
the exact (\chi_4)-preserving transform, its exact Möbius scaling and
rank-one product collar, the resulting positive power loss, the bare
transform involution, standard differencing sign loss, and the scoped
failure of the named source placements.

The target remains

\[
 |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon,
\tag{162.A1}
\]

with all physical profiles and hard pieces retained.  Even a proof of
(162.A1) would leave the other few-point radical channels open.  No
hard-TOP parent, smooth M2 packet, M9--M2, M9--M1, endpoint-uniformity,
M9, bridge, quarter theorem, or global exponent changes.

## 2. Exact accepted statement and hypotheses

Let (J=\sqrt X), (y=\lfloor J\rfloor), (q_X=X/y^2),
(H=\lfloor yX^{-1/4}\rfloor), and (1\ll L\ll H).  The literal scalar
is

\[
\begin{aligned}
\mathcal S_{L,1}=\sum_{\substack{d_1d_2\asymp L^2\\
d_1,d_2\ \mathrm{squarefree},\ (d_1,d_2)=1\\
d_1\ \mathrm{odd},\ d_2\le d_1\le4d_2}}
&\chi_4(d_1)\left(\frac{L^2}{d_1d_2}\right)^{3/4}
\eta_L(d_1)\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right)
e(J\sqrt{d_1d_2}).
\end{aligned}
\tag{162.A2}
\]

Its exact projector opening is

\[
\begin{aligned}
&\mu^2(d_1)\mu^2(d_2)\mathbf1_{(d_1,d_2)=1}\\
&\quad=\sum_{a^2\mid d_1}\mu(a)
       \sum_{b^2\mid d_2}\mu(b)
       \sum_{c\mid(d_1,d_2)}\mu(c).
\end{aligned}
\tag{162.A3}
\]

For (Q=[a^2,c]), (R=[b^2,c]), and
(d_1=Qm,d_2=Rn), only (a,c,Q,m) are forced odd.  The even-(d_2)
branch survives, and

\[
 \chi_4(Qm)=\chi_4(Q)\chi_4(m).
\tag{162.A4}
\]

With (\widehat g(\xi)=\int g(x)e(-\xi x)\,dx), exact character
Poisson is

\[
 \boxed{
 \sum_m\chi_4(m)g(m)
 =\frac i2\sum_{s\ \mathrm{odd}}\chi_4(s)\widehat g(s/4).}
\tag{162.A5}
\]

For one opening, the positive saddle in the character leg is

\[
 m_s=\frac{4XQd_2}{s^2},\qquad
 d_1^*=\frac{4XQ^2d_2}{s^2},\qquad
 F_s(m_s)=\frac{XQd_2}{s},
\tag{162.A6}
\]

with (JQ\le s\le2JQ), exact profile (W(XQ/(ys))), and normalized
stationary factor

\[
 \frac{2L^{3/2}J^{-1/2}}{Qd_2}.
\tag{162.A7}
\]

The leading signed unit is (e(1/8)\chi_4(Q)\chi_4(s)).  The exact
character transform is involutive; a second bare transform returns the
original sum.

The product Hessian has determinant zero and radial null vector.  On a
compact smooth interior cell, simultaneous dualization gives

\[
 s\ell=XQR,\qquad Q\ell\le Rs\le4Q\ell,
\tag{162.A8}
\]

and radial length (L) broadens this to

\[
 |s\ell-XQR|\ll QRJ/L.
\tag{162.A9}
\]

There are at most

\[
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon
\tag{162.A10}
\]

factor pairs, each of smooth-interior scale

\[
 \frac{L^{3/2}}{QR\sqrt J}.
\tag{162.A11}
\]

Thus termwise positive control has capacity

\[
 \sqrt{JL}\,(XQR)^\varepsilon
 =L^{3/2}\frac{H+O(1)}{L}(XQR)^\varepsilon,
\tag{162.A12}
\]

independent of the opening scale at the power level.  The favorable
single-opening comparison

\[
 \min\{L^2,\sqrt{JL}\}
 =L^{3/2}\min\{L^{1/2},H/L\}(1+o(1))
\tag{162.A13}
\]

is a route capacity only, not a bound or lower mass for the complete
physical scalar.

Grouping (N=s\ell) gives the local signed window

\[
 \sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\mathcal K_{Q,R}(N;s).
\tag{162.A14}
\]

Completing it to (r_2(N)/4) adds the uncontrolled complementary
window.  Standard even-step differencing gives

\[
 \chi_4(d+2h)\chi_4(d)=(-1)^h,
\tag{162.A15}
\]

so a following positive norm loses the character.

## 3. Proof reproduction and review synthesis

The discovery, statement-only blind, and hostile-source reports
independently derived the projector, parity, character transfer, rank-one
geometry, scaled product collar, and unpaid power.  The conductor
recomputed every sign and scale in (162.A3)--(162.A15).

The post-unmask blind review and independent power/involution review both
returned GREEN.  They checked the coefficient (i\chi_4(s)/2), Gaussian
unit (e(1/8)), the exact reflection sign in the involution, the
(Q,R)-scaled saddle, the dual cone and collar, the per-pair amplitude,
the factor count, and cancellation of all positive (Q,R)-powers.

Both reviews required one conservative selection decision.  The
discovery report proposed a blanket target-safe ledger for transformed
hard edges, whereas the statement-only packet did not contain enough
literal profile data to certify every entry, exit, and endpoint.  The
accepted kernel leaves hard edges, stars, collar tails, and saddle-edge
transitions open.  This is consistent with the accepted Round-75 warning
that a leading moving-saddle formula is not automatically an all-orders
identity.  The smooth-interior route obstruction remains valid without
an affirmative boundary theorem.

The source/graph reviewer returned GREEN after calibrating the source
statements.  Bombieri--Iwaniec requires a separated coefficient.
Kowalski--Robert--Wu and Robert--Sargos restore, even after fictitious
cost-one separation,

\[
 J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}+J^{-1/2}L^{3/2}
\tag{162.A16}
\]

and

\[
 J^{1/4}L^{3/2}+L^{7/4}+L^{3/2}+J^{-1/2}L^{3/2},
\tag{162.A17}
\]

respectively.  The fixed-modulus/fixed-integral DFI and DRZ interfaces
have no uniform literal placement for (e(XQd_2/s)).  Bettin--Chandee
has a formal degenerate placement when the arithmetic parameters are
integral, but its printed factor is already

\[
 (1+|\vartheta|A/(MN))^{1/2}\asymp(JL)^{1/2}.
\tag{162.A18}
\]

These facts park only the named direct placements.

The graph reviewer confirmed that the new node is nonduplicate.  Round
137 owns the unprojected reciprocal self-return; Round 161 owns the
radical dictionary, long channels, exact collisions, and coarse
common-test/source obstruction.  Round 162 newly owns the exact mod-four
character transfer, literal lcm opening, scaled product collar,
(Q,R)-power repayment, exact character involution, and standard
differencing sign loss.

## 4. First doubtful or unproved step

The first affirmative step is a target-strength estimate for the full
signed Möbius aggregate whose smooth principal interface is

\[
\begin{aligned}
 \frac{L^{3/2}}{\sqrt J}
 \sum_{a,b,c}\frac{\mu(a)\mu(b)\mu(c)\chi_4(Q)}{QR}
 \sum_{N\approx XQR}
 \sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\mathcal K_{Q,R}(N;s),
\end{aligned}
\tag{162.A19}
\]

with arbitrary-real-centre uniformity, even (d_2), all profiles,
hard edges, floors, stars, endpoint transitions, nonstationary pieces,
and collar tails retained before every positive norm.  It must gain the
factor (\min\{L^{1/2},H/L\}) over the favorable positive ledger.

Equation (162.A19) is schematic only for the smooth principal family; it
does not own the omitted hard pieces.  No accepted artifact proves this
signed aggregate, and no accepted artifact proves its physical value is
large.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Literal coefficient, orientation, normalization | GREEN independently. |
| Squarefree/coprime opening and even (d_2) | GREEN independently. |
| Character retained before positive norms | GREEN; exact coefficient (i\chi_4(s)/2). |
| Character transform involution | GREEN including scaling, reflection, and Gaussian signs. |
| Rank-one Hessian | GREEN; no determinant division. |
| Scaled dual product and cone | GREEN: (162.A8). |
| Collar, count, and per-pair scale | GREEN for compact smooth interior cells. |
| (Q,R)-power ledger | GREEN; positive capacity is (\sqrt{JL}). |
| Local divisor completion | GREEN as obstruction; complement remains open. |
| Standard differencing | GREEN as a positive-route obstruction only. |
| Hard profiles and endpoints | OPEN and explicitly retained; no blanket safety claim promoted. |
| Source theorem hypotheses and powers | GREEN after formal-degenerate Bettin--Chandee calibration. |
| Physical coefficient versus capacity | GREEN; no physical lower bound. |
| Graph direction and nonduplication | GREEN: one new node, two inconclusive open-parent updates. |
| Downstream and exponent scope | GREEN; no target or exponent promotion. |
| Numerical allocation | GREEN; 100% analytic/algebraic/source work. |

## 6. Dependencies and selected evidence

The accepted proof kernel is

`proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`.

Primary reports:

- `reports/literal_t1_character_poisson_attack.md`;
- `reports/blind_t1_close_factor_rederivation.md`;
- `reports/t1_bilinear_source_hostile_audit.md`.

Selected candidate and control:

- `candidates/conductor_round162_t1_character_poisson_collar_obstruction.md`;
- `controls/conductor_round162_reproduction_and_selection.md`.

Independent reviews:

- `reviews/blind_post_unmask_character_collar_review.md`;
- `reviews/power_involution_and_physical_scope_review.md`;
- `reviews/source_and_downstream_graph_scope_review.md`.

Accepted antecedents are the Round-137 product-fibre transform
self-return and both Round-161 radical nodes.  No numerical experiment or
unreviewed source theorem is used.

## 7. State decision and next action

Apply a State Patch that:

1. creates
   `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`;
2. adds it only as a dependency and inconclusive evidence to
   `M9-M2-top-endpoint-signed-cone` and
   `M9-M2-top-endpoint-density-discrepancy-energy`;
3. rejects the physical, hard-edge, free-opening, transform-contraction,
   universal-source, parent, and exponent overclaims listed in the patch;
4. leaves all accepted antecedents and all downstream statuses unchanged.

The next admissible attack on this face must prove the signed local-divisor
aggregate (162.A19), including the boundary owners, before every positive
norm.  Alternatively, a later round may rotate to a mathematically
distinct remaining few-point, balanced, unbalanced, or M1 owner; it may
not relabel another bare transform or coefficient-uniform positive norm as
progress.
