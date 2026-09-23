# Round 169 downstream graph and scope review

## 1. Result

**PASS.**  The reviewed conductor candidate, SHA-256

\[
\texttt{9edceafb9db77a2b2e2dcbb6e8c5b8e0308874fbf51048b883d363ac6d0013df},
\]

supports exactly one new `proved_internal` reduction.  The appropriate
graph object is an exact joint-functional-equation/double-Poisson
self-return for the complete literal hard-TOP \(t=1\) scalar, with the
finite-zero/full-residue correction retained.  Its positive clauses are
homogeneous: the coefficient law, completed-function kernels, physical
double-Poisson formula, residue correction, and Round-162 comparison are
successive descriptions of the same scalar and the same open signed
aggregate.  The route-scoped no-go is a consequence of that reduction,
not a second owner or a universal impossibility theorem.

Round 169 may therefore close only under
`t1_joint_FE_spectral_self_return_no_go`.  It does not prove
`hard_top_t1_signed_two_height_target` or
`strict_t1_joint_FE_spectral_sector`.  No scalar owner, hard-TOP owner,
BAL or UNBAL owner, M9--M2, M9, bridge, quarter theorem, or exponent is
closed or promoted.

## 2. Exact statement and hypotheses

Create one node with the proposed ID

`M9-M2-hard-top-t1-joint-functional-equation-double-poisson-self-return`.

Its type should be `reduction`, its status `proved_internal`, its track
`M9_analytic`, and both `implies` and `blockers` should be empty.  Its
direct dependencies should be exactly:

1. `M9-M2-hard-top-t1-mellin-euler-polylog-and-signed-moment-reduction`;
2. `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.

The node must retain

\[
J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
H=\lfloor yX^{-1/4}\rfloor,\qquad 1\ll L\ll H,
\]

the exact Round-168 disjoint-cardinal interpolant \(\mathcal B\), and
every inherited shell, real-centre floor, profile, cone edge, star,
parity branch, endpoint transition, and zero extension.  Write

\[
G(s_1,s_2)=\sum_{Q,R\geq1}g(Q,R)Q^{-s_1}R^{-s_2}.
\]

The statement may record the exact local table and weighted mass, or
equivalently the collapsed law

\[
g(Q,R)=\chi _4(Q)
 \sum_{\substack{u,v,c\geq1;\ u,c\ \mathrm{odd}\\
                 [u^2,c]=Q,\ [v^2,c]=R}}
 \mu(u)\mu(v)\mu(c),
\]

including \(G_2=1-2^{-2s_2}\), and

\[
\sum_{Q,R}\frac{|g(Q,R)|}{Q^{1/2+\eta}R^{1/2+\eta}}
\asymp \eta^{-3}\qquad(0<\eta\leq1/4).
\]

The reviewed candidate now defines the finite physical block set from
the pre-Poisson convolution and defines its rectangular cutoffs by the
positive support suprema of \(\mathcal B\).  This removes the former
“diameter” ambiguity.  It also explicitly fixes the Fourier convention

\[
\widetilde{\mathcal B}(\xi,\upsilon)
=\iint_{\mathbb R^2}\mathcal B(x,z)e(-\xi x-\upsilon z)\,dx\,dz,
\]

so every sign and scaling in the following identity is determinate.

With that convention, the exact identity is

\[
\mathcal S_{L,1}
=\frac i2\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}{QR}
 \sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}\chi _4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).
\tag{G169.1}
\]

If \(Z_{\rm phys}\) is its \(\ell=0\) part and \(R_\zeta\) is the full
Round-168 Mellin residue, then

\[
E_0=Z_{\rm phys}-R_\zeta,
\qquad
Z_{\rm phys}\ll \frac{L^2}{J},
\qquad
E_0\ll \frac{L^2}{J}.
\tag{G169.2}
\]

The weaker \(O_\varepsilon(L^2J^{-1}X^\varepsilon)\) form would also be
enough for the graph.  The stronger displayed form is justified by
applying the same one-cell integration by parts to the exact full-residue
formula, not merely by quoting the slackened Round-168 statement.
Consequently

\[
\mathcal I_\eta
=E_0+\frac i2\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi _4(k)
 \sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).
\tag{G169.3}
\]

Substitution of the collapsed coefficient law into (G169.1) must be
stated as the exact Round-162 Möbius opening followed by character
Poisson and ordinary Poisson, including the even second leg and the
two-adic branch.  The first open estimate remains the complete signed
nonzero-frequency aggregate in (G169.3).

## 3. Proof, residue seam, and graph implication

The finite-zero/full-residue distinction is correct and essential.  Let
\(\mathscr P\) denote the chosen finite physical block set.  Split the
Poisson expansion of those blocks as

\[
\mathcal S_{L,1}=Z_{\mathscr P}+N_{\mathscr P}.
\]

If all \(R\)-blocks are inserted before frequencies are split, the full
zero-mode sum is

\[
Z_{\rm all}=R_\zeta
=\sum_{Q}\sum_{R\geq1}\frac{g(Q,R)}R
  \sum_m\chi _4(m)\int\mathcal B(Qm,z)\,dz.
\]

Every added block has zero complete pre-Poisson lattice sum, but its
zero and nonzero ordinary-Poisson modes need not vanish separately.
Writing `out` for the added blocks gives

\[
Z_{\rm out}+N_{\rm out}=0,
\qquad
E_0=Z_{\mathscr P}-Z_{\rm all}=-Z_{\rm out}=N_{\rm out}.
\]

It follows exactly that

\[
\mathcal I_\eta
=\mathcal S_{L,1}-R_\zeta
=N_{\mathscr P}+E_0=N_{\rm all}.
\]

Thus the sign of the correction in the candidate is right.  In
particular, neither \(Z_{\rm phys}=R_\zeta\) nor cancellation of each
out-of-support Poisson mode is being assumed.

At \(x=Qm\), cardinal disjointness leaves one \(x\)-cell.  There are
\(O(L/Q)\) possible \(m\)'s and \(O(L)\) supported \(z\)-cells, and on
each such cell the \(z\)-phase derivative is \(\asymp J\).  Hence

\[
\left|\sum_m\chi _4(m)\int\mathcal B(Qm,z)\,dz\right|
\ll \frac{L^2}{QJ}.
\]

Since

\[
\sum_{Q,R}\frac{|g(Q,R)|}{QR}<\infty,
\]

this proves the bounds in (G169.2) for both the finite zero mode and the
full residue, and hence for their difference.  The correction is
therefore genuinely target-safe and does not hide an endpoint or
infinite-tail owner.

The coefficient identity is also exact: the eight odd-prime binary
states of the three Möbius variables give the six nonzero local entries,
the two \((2,2)\) entries cancel, and at \(2\) only
\((v_2(Q),v_2(R))=(0,0),(0,2)\) remain.  Character and ordinary Poisson
then give (G169.1) with the factors \(i/2\), \(1/Q\), and \(1/R\).
The completed \(L(s,\chi _4)\) and zeta kernels yield respectively the
odd sine and cosine transforms, so no gamma, root-number, conductor, or
orientation term remains unaccounted for in the comparison.

The stationary equations retain

\[
k\ell=XQR,
\qquad
Q\ell\leq Rk\leq4Q\ell,
\]

and the favorable smooth interior collar has the already accepted
positive capacity \(\sqrt{JL}X^\varepsilon\).  This proves an exact
self-return, not the target estimate for the literal cardinal array.

Graphically, the new reduction points only to the two accepted upstream
nodes.  Add it as a dependency of
`M9-M2-top-endpoint-signed-cone`; there is no reverse path, so this
attachment is acyclic.  Do not add an `implies` edge.  The
density-discrepancy energy has no proved connector from this scalar
identity and should not receive a new dependency merely by analogy.

## 4. First doubtful or unproved step

The first unproved mathematical statement is exactly

\[
E_0+\frac i2\sum_{Q,R}^{\rm phys}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi _4(k)\sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right)
\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{G169.4}
\]

Because \(E_0\) is target-safe, the open part is precisely the complete
signed Round-162 family in collapsed coordinates.  Neither the
functional equations nor the rank-one phase supplies cancellation among
\((Q,R)\), nearby products, or the \(O(L^2)\) cardinal cells.  A smooth
radial block of length \(L\) cannot replace the literal unit-cell array
without a separately proved endpoint-lawful recombination theorem.

This is the first open step, not evidence of a physical lower bound.
The candidate rules out only bare dualization, an infinite post-shift
absolute resummation of \(G\), the favorable positive collar placement,
and the dated audited source placements.  A bespoke signed spectral,
reciprocity, or other joint-aggregate theorem remains logically open.
Even a future proof of (G169.4) would settle only the complete \(t=1\)
face; the other hard-TOP channels and collars, BAL, UNBAL, and the M1
owners would remain.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Starting graph and node collision | **PASS.** The authoritative graph SHA-256 is `a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`, matching the campaign, and the proposed node ID is unused. |
| Homogeneous one-node reduction | **PASS.** All positive clauses are exact interfaces for the same literal scalar; the scoped no-go is retained as route scope, not made a second owner. |
| Finite zero mode versus full residue | **PASS.** The candidate has the correct correction \(E_0=Z_{\rm phys}-R_\zeta\), the correct sign, the full \(R\)-tail, and a target-safe bound. |
| Exact Round-162 self-return | **PASS.** The Möbius multiplicities collapse coefficientwise to \(g(Q,R)\); \(p=2\), the even second leg, transform constants, parities, profiles, and frequencies are retained. |
| Unsigned control | **PASS as a falsifier.** Removing \(\chi _4\) changes the coefficient/kernel but leaves the rank-one product resonance and positive collar; the transform alone proves no unsigned target. |
| Aligned control | **PASS as a falsifier.** Artificial phase alignment can saturate the termwise-positive capacity, so no cancellation is inferred from the geometric identity alone. |
| \(G=1\) control | **PASS as a falsifier.** It freezes \(Q=R=1\) but leaves the same product collar; the claimed gain cannot come merely from two GL(1) functional equations. |
| No early norm or common height | **PASS.** The two independent Fourier variables remain signed through the exact phase calculation. |
| No universal no-go | **PASS.** The candidate expressly leaves bespoke signed spectral or reciprocity estimates open. |
| Owner closure | **PASS with no promotion.** (G169.4), the general \(t=1\) scalar and residual, other hard-TOP channels, BAL, UNBAL, and both M1 routes remain open. |
| Parent and exponent scope | **PASS.** `M9-M2-physical-one-count-assembly`, `M9-M2`, `M9`, both bridges, `GC-target`, `GC-partial-one-third`, `GC-external-Li-Yang-theta-star`, and `M9-direct-menu-one-third-optimality` remain unchanged. |
| No in-round pivot | **PASS.** Round 169 closes the frozen mechanism under its self-return label and does not begin a replacement attack. |
| Mandatory Round 170 | **PASS only with explicit scheduling.** The next round must be the required strategy/current-literature review before another analytic attack on (G169.4). |

No numerical experiment is used or needed; this review is analytical,
algebraic, and graph-mechanical.

## 6. Dependencies and exact artifacts used

The mathematical and graph audit used:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `proofs/kernels/m9_m2_hard_top_t1_mellin_euler_polylog_signed_moment_reduction.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/candidates/conductor_round169_joint_fe_double_poisson_self_return.md`;
7. `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/candidates/conductor_round168_mellin_euler_polylog_and_signed_moment_reduction.md`;
8. `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reviews/conductor_candidate_graph_scope_review.md`;
9. `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reviews/downstream_graph_scope_review.md`.

The Round-168 conductor candidate was consulted only to verify that its
explicit residue formula and one-cell integration-by-parts proof support
the unslackened \(O(L^2/J)\) bound.  The accepted Round-168 and Round-163
graph-scope reviews were consulted only for existing dependency,
inconclusive-parent-evidence, and strict nonpromotion conventions; no
additional estimate was imported from them.

The graph was parsed read-only to verify the starting hash, dependency
statuses, incoming edges, node-ID uniqueness, downstream owners, and
acyclicity.  No shared state, campaign, candidate, report, synthesis,
validation matrix, proof draft, or file other than this assigned review
was edited.

## 7. Recommended state effect

**CREATE.**  Create exactly the reduction node specified in Section 2.
Its accepted statement should include the exact \(g\)-law and \(p=2\)
branch, the completed-function kernels, (G169.1)--(G169.3), the explicit
finite-zero/full-residue correction, the coefficientwise Round-162
self-return, and the restricted route no-go.  Give it no implication
edge and no blocker.  Its next action should be to estimate the single
signed aggregate (G169.4) before every positive norm, with the literal
cardinal/endpoints retained or replaced only by a proved recombination
identity.

**UPDATE ONE OPEN OWNER.**  Add the new node only as a dependency of
`M9-M2-top-endpoint-signed-cone`, and add the Round-169 artifacts as
inconclusive evidence for that still-open owner.  Keep its statement,
status, blocker, and implication edge unchanged.  Its next action may be
refined to name (G169.4), while expressly retaining all other \(t=1\)
and few-point channels.

**RETAIN HISTORICAL SCOPE.**  Preserve the Round-168 rejection saying
that Round 168 itself did not prove an FE/AFE self-return.  Round 169
supplies the coefficient, two-adic, gamma, residue, truncation, and
literal-profile bridge that was absent there; this does not make the
historical Round-168 evidence claim false.

**REJECT STRONGER READINGS.**  Record, or preserve, rejection of the
claims that:

1. the finite physical zero mode is literally the full Mellin residue;
2. bare joint functional equations prove (G169.4);
3. the infinite \(G\)-series may be absolutely resummed after the left
   contour shift;
4. the favorable length-\(L\) collar estimates the literal cardinal
   array;
5. the self-return excludes every future signed spectral or reciprocity
   theorem;
6. any unsigned, aligned, or \(G=1\) control acquires the missing signed
   gain from dualization alone; or
7. this reduction closes a parent, bridge, theorem, or improves either
   exponent ledger.

**NO CHANGE.**  Do not mutate
`M9-M2-top-endpoint-density-discrepancy-energy`, either smooth M2 packet,
`M9-M2-physical-one-count-assembly`, `M9-M2`, either direct M1 parent,
GAR, endpoint uniformity, `M9`, either bridge, `GC-target`, or either
internal/external exponent node.

Finally, close Round 169 before opening anything else, and schedule
Round 170 as the mandatory strategy and current-literature review of a
genuinely signed theorem for (G169.4).  The next round must not be a
silent continuation or an in-round pivot.
