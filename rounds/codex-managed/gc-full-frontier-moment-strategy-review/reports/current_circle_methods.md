# Round 205: current circle, large-value and harmonic-analysis audit

Campaign: `gc-full-frontier-moment-strategy-review`. Task: `current_circle_methods`. Role: source auditor, selected context. Date: 2026-09-26. Starting graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`. Candidate strategy evidence only. Entire effort analytical/algebraic and primary-source inspection; no experiments.

## 1. Result: three checked interfaces, no certified arithmetic gain

The three substantive interfaces checked are Guth--Maynard's Dirichlet-polynomial large-value theorem, Guth--Maldague's amplitude-dependent cone estimate, and Kim--Ko's newer weighted parabola estimate. None supplies the missing full-series arithmetic estimate. In particular, an improvement in generic off-diagonal/sample-count terms does not remove the retained one-peak contribution. The project saving certified by this audit is zero.

There is a useful new exact interface: the square-root block can be lifted to a parabola in two dimensions, with a fixed-line trace represented by a bounded weight. This avoids requiring a three-dimensional lattice lift merely to obtain curvature. However, the checked weighted theorem has only orders 2 through 4; its coarse-scale weight parameter can remain order one. It provides a reusable reduction, not a twelfth-moment gain.

The best next arithmetic objective at this task's scope is the **complete high-value remainder** in (4) below. The actual entire series is retained there. No checked external theorem supplies an affordable method for that objective. I recommend retaining the weighted lift as a precisely delimited exploratory interface, and declining a direct Dirichlet-polynomial import. This is not a no-go theorem against future adaptations of those methods.

Both named withdrawals remain in force. The Li--Yang record remains v2, and all graph qualifications on its narrowly repaired final application remain necessary.

## 2. Exact statement and hypotheses

Use the accepted entire series

\[
B_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4),\qquad
a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),
\tag{1}
\]

where \(T\ge2\) is real and \(\Psi\) is the Fourier transform of the fixed radial smooth mollifier in the accepted kernel. Let \(w\ge0\) be fixed, bounded and supported in \([c,C]\subset(0,\infty)\). Put \(D_T(V)=\int w(R/T)1_{|B_T(R)|>V}\,dR\), \(M_{12}=\int w(R/T)|B_T(R)|^{12}\,dR\), and

\[
\theta=\frac{3292+25\sqrt{1717}}{13762},\quad
\beta=2\theta-\frac12,\quad q=\frac{136}{13}.
\]

The accepted input is

\[
D_T(V)\ll T^\epsilon(V^{-2}+TV^{-q}),\quad V\ge1,
\qquad \|B_T\|_\infty\ll T^{\beta+\epsilon}.
\tag{2}
\]

Consequently \(M_{12}\ll T^{10\beta+\epsilon}\). The desired milestone is

\[
M_{12}\ll T^{29/25+\epsilon},\qquad
\|\chi(R/T)B_T(R)^6\|_2\ll T^{29/50+\epsilon},
\tag{3}
\]

with the appropriate fixed \(w=\chi^2\). The remaining squared-norm exponent deficit is \(10\beta-29/25\); the norm deficit is \(5\beta-29/50=0.0648317597\ldots\).

One concrete sufficient *complete arithmetic* objective is

\[
\boxed{\int_{|B_T(R)|>T^{13/125}}
w(R/T)|B_T(R)|^{12}\,dR
\ll_\epsilon T^{29/25+\epsilon}.}
\tag{4}
\]

This is an unproved proposed objective, not an external consequence. The accepted distribution controls the complementary truncated moment: layer cake up to \(V_0=T^{13/125}\) gives powers \(1\), \(10(13/125)=26/25\), and \(1+(12-q)(13/125)=29/25\). Thus (4) suffices for (3). Its event is defined using the full signed cosine series; no independent supremum bound for a discarded block is substituted.

The complete original-\(t=1\) source remains \(Q_R=D+2\Re C_{\rm even}\), with \(D\ll L^2X^\epsilon\), generic bound \(Q_R\ll LD\), and target \(Q_R\ll L^2X^\epsilon\). None of the three external theorems directly bounds that physical Fejer correlation. Solving it would still leave the other hard-M1 incidences, independent smooth M1, M2 TOP/BAL/UNBAL and real endpoint assembly. GAR likewise still requires M2.

## 3. Derivation and current primary-source audit

### A. Guth--Maynard: exact theorem and paid logarithmic-phase transfer

[Guth--Maynard, arXiv:2405.20552v2, Theorem 1.1](https://arxiv.org/html/2405.20552v2#S1.Thmtheorem1) assumes \(|b_n|\le1\) and 1-separated \(t_j\in[0,\tau]\) at which \(|\sum_{N\le n\le2N}b_nn^{it_j}|\ge A\). It gives

\[
J\ll\tau^{o(1)}
\left(N^2A^{-2}+N^{18/5}A^{-4}
+\tau N^{12/5}A^{-4}\right).
\tag{5}
\]

The [current record](https://arxiv.org/abs/2405.20552) is v2, 7 April 2026. The paper explicitly requires the coefficient sup norm, not just its energy. The author repository also records publication in *Annals of Mathematics* 203(2), 623--675, DOI [10.4007/annals.2026.203.2.6](https://doi.org/10.4007/annals.2026.203.2.6). Those facts do not make (5) a theorem about square-root frequencies.

Here is independent transfer accounting. Write a complex physical block as

\[
S_N(R)=N^{-3/4}\sum_{n\asymp N}b_ne(R\sqrt n),\qquad
|b_n|\ll T^\epsilon.
\tag{6}
\]

The harmless coefficient normalization is legal for (5), using the divisor bound, including zero extension for a partial dyadic block. The phase is the obstruction. On a radius interval \(R=R_0+u\), \(|u|\le L\), and a frequency packet \(n=M+h\), \(|h|\le H\), freeze \(e(R_0\sqrt n)\) into the coefficients. Direct Taylor expansion gives

\[
2\pi u(\sqrt{M+h}-\sqrt M)
-\pi\sqrt M\,u\log(1+h/M)
=\frac{\pi u h^2}{4M^{3/2}}
+O(|u|H^3/N^{5/2}).
\tag{7}
\]

Consequently the elementary smooth-residual reduction requires
\(LH^2N^{-3/2}\lesssim1\), hence

\[
H\lesssim N^{3/4}L^{-1/2},\quad
K\asymp\max(1,N/H),\quad
\tau\asymp L\sqrt N,\quad dt\asymp\sqrt N\,dR.
\tag{8}
\]

An exact separated expansion of the smooth bounded residual can be obtained after smooth packet localization; treating it as zero is not justified. Hard cutoffs need zero extension or the corresponding bounded-variation accounting. Crucially, (5) still sees integers of size \(N\); it does not become a length-\(H\) theorem for a high-origin short interval by renaming the length. Replacing \(n\) by \(h\) changes \(\log n\).

Even if that residual expansion and all masks cost only \(T^\epsilon\), triangle inequality across \(K\) packets lowers the Dirichlet threshold to \(A\asymp VN^{3/4}/K\). A union over packets and the \(O(1+T/L)\) radius intervals, followed by maximal separated-point covering, gives the following cost *from the first term of (5)*:

\[
(1+T/L)\,K\,N^{-1/2}
\,N^2(VN^{3/4}/K)^{-2}
\asymp(1+T/L)K^3V^{-2}.
\tag{9}
\]

This is an upper-bound obstruction for this transfer, not a lower bound for the physical series. At the transition \(N\asymp T\), taking \(L=T\) forces \(H\lesssim T^{1/4}\), \(K\gtrsim T^{3/4}\). The putative threshold becomes \(A\asymp V\), far below the large-amplitude regime \(N^{7/10}\), while (9) costs \(T^{9/4}V^{-2}\). Choosing smaller \(L\) changes the ledger but cannot remove the one-interval term. Even an unrealistically lossless identification with one polynomial, with \(A=VN^{3/4}\) and Jacobian \(N^{-1/2}\), leaves exactly \(V^{-2}\).

An unrestricted Mellin expansion is another representation, not a free transfer: stationary phase for the dyadic Mellin kernel of \(e(R\sqrt n)\) has frequency span \(\asymp R\sqrt N\), individual magnitude \(\asymp(R\sqrt N)^{-1/2}\), and typical absolute-integral size \((R\sqrt N)^{1/2}\). The coefficient kernel also depends on \(R\). A cancellation estimate for that kernel would itself be a new input. The packet calculation (7)--(9) is already enough to reject the direct cheap import.

### B. Guth--Maldague: amplitude restriction still has a trace cost

[Guth--Maldague, arXiv:2206.01093v2, Theorem 2](https://arxiv.org/html/2206.01093v2) gives, for Schwartz \(f\) supported in frequency in an \(\mathcal R^{-1}\)-neighborhood of the truncated cone in \(\mathbb R^3\),

\[
\alpha^4|\{|f|>\alpha\}|\ll_\epsilon\mathcal R^\epsilon
\sum_s\sum_{\tau\in\mathbf S_s}
\sum_{U\in\mathcal G_\tau(\alpha)}
|U|^{-1}\|S_Uf\|_2^4,
\tag{10}
\]

where \(\mathcal G_\tau(\alpha)\) retains envelopes whose normalized square-function energy is at least \(\alpha^2/(\#\tau)^2\), up to the stated \(\mathcal R^\epsilon\) constant. The [record](https://arxiv.org/abs/2206.01093) remains v2, 13 August 2022. The associated small-cap theorem requires \(\beta_1\in[1/2,1]\), \(\beta_2\in[0,1]\). Its measure is three-dimensional.

For independent normalization accounting, open \(r_2(n)\) as lattice multiplicity and form

\[
G_N(x,R)=\sum_{N<|v|^2\le2N}
|v|^{-3/2}\Psi(|v|/\sqrt T)
e(x\cdot v+R|v|),\quad x\in\mathbb R^2.
\tag{11}
\]

Then \(G_N(0,R)=S_N(R)\). Rescale \(y=\sqrt N x\), \(t=\sqrt N R\), with \(\mathcal R\asymp T\sqrt N\), and insert a band-limited Schwartz envelope at that scale. Fixed constants bring the frequency surface into the source's truncated cone. These operations retain the actual coefficients. A reproducing kernel in the two spatial coordinates gives the trace-to-weighted-moment cost \(N\) in the original \(x\) variables; it cannot be replaced by a spatial average of total mass one without that normalization.

There is also an elementary superlevel version. The divisor/lattice bound gives \(\|\nabla_xG_N\|_\infty\ll N^{3/4+\epsilon}\). A physical level \(|G_N(0,R)|>V\) therefore persists in a disk of radius \(\gg V N^{-3/4-\epsilon}\). Thus

\[
D_N(V)\ll N^{3/2+\epsilon}V^{-2}
\,\operatorname{vol}_3\{|G_N|>V/2\}
\tag{12}
\]

on the appropriate enlarged cylinder. In normalized \((y,t)\) coordinates the volume Jacobian is \(N^{3/2}\), so the prefactor becomes \(T^\epsilon V^{-2}\). Combining with (10) still requires bounding the *actual retained envelope sum*; in normalized variables the sufficient target is that this sum be \(\ll T^{29/25+\epsilon}V^{-6}\). No such arithmetic estimate is supplied by (10). This explicitly prices the trace instead of denying that a trace inequality is possible. All localization tails and real radius windows must also be restored.

### C. Kim--Ko: a direct weighted parabola interface

[Kim--Ko, arXiv:2511.04503v2, Theorem 1.1, equations (3)--(4)](https://arxiv.org/html/2511.04503v2) assumes \(2\le p\le4\), \(0\le H\le1\), and Fourier support in the \(\mathcal R^{-1}\)-neighborhood of \(\{(s,s^2):|s|\le1\}\). It gives

\[
\|f\|_{L^p(H)}\ll_\epsilon\mathcal R^\epsilon
\left(\max_U\kappa_{p,H}(U)+\mathcal R^{-100}\right)
\left\|\left(\sum_\vartheta|f_\vartheta|^2\right)^{1/2}\right\|_p,
\tag{13}
\]

\[
\kappa_{p,H}(U)=
\max_{Q\subset U}
\left(\frac{H(Q)}{|Q|}\right)^{1/4}
\left(\frac{H(U)}{|U|}\right)^{1/p-1/4}.
\tag{14}
\]

At scale \(s\), \(Q\) has dimensions \(s^{-1}\times s^{-2}\), and \(U\) has dimensions \(\mathcal R s\times\mathcal R\). The [record](https://arxiv.org/abs/2511.04503) remains v2, 20 December 2025; v2 replaces a polylogarithmic loss by a subpower loss. Theorem 1.4, (8), gives its unsupremized weighted envelope form. No order above four is asserted.

Here is a reusable project lift, derived directly. For \(N<n\le2N\), put

\[
s_n=\sqrt{n/(4N)},\quad
F_N(x,t)=\sum_{N<n\le2N}a_n(T)e(t s_n+x s_n^2).
\tag{15}
\]

Up to interchanging the two physical coordinates, its frequencies lie on the source's parabola, and

\[
F_N(0,2\sqrt N R)=S_N(R),\quad
dt=2\sqrt N\,dR,\quad \mathcal R\asymp T\sqrt N.
\tag{16}
\]

Multiplication by a Schwartz envelope whose Fourier support has radius \(c/\mathcal R\), and which is bounded below on the needed line segment, supplies the source's Schwartz/localized function. A fixed reproducing kernel in \(x\), equal to one in Fourier space on all the \(x\)-frequencies of the localized lift, gives by Holder

\[
|f_N(0,t)|^p\le C_p\int k(x)|f_N(x,t)|^pdx,
\quad k\ge0\text{ fixed Schwartz},\quad k\le1
\tag{17}
\]

after absorbing a fixed constant. For any measurable physical radius set \(E\), use the legitimate bounded weight
\(H_E(x,t)=k(x)1_{2\sqrt N E}(t)\). This proves a trace bound with the explicit factor \((2\sqrt N)^{-1}\) on returning to \(R\). It also works for arbitrarily small or disconnected real level sets; it does not require translating a line integral into a spatial average by assumption.

This interface has two quantitative limits. First, at \(p=4\), (14) depends only on the largest local density \(H_E(Q)/|Q|\). If \(E\) contains a normalized interval of fixed positive length, a coarse-scale unit \(Q\) can have density bounded below independently of \(\mathcal R\). Total sparsity of \(E\) therefore supplies no automatic saving in the supremized theorem. Second, even granting the already accepted sharp full fourth moment \(M_4\ll T^{1+\epsilon}\), interpolation with the accepted supremum gives only

\[
M_{12}\le\|B_T\|_\infty^8 M_4
\ll T^{1+8\beta+\epsilon},
\tag{18}
\]

which is weaker than \(T^{10\beta+\epsilon}\). Applying (13) to \(F_N^3\) does not repair the order: sums of three parabola frequency points do not lie in a thin parabola neighborhood.

For clarity, the unsupremized formula supplies a testable sufficient *new* arithmetic estimate. If \(E_N(V)=\{R:|S_N(R)|>V\}\) and \(\mathcal W_N(H_{E_N})\) denotes the exact right-hand envelope sum of source Theorem 1.4 at \(p=4\), then (16)--(17) give

\[
V^4|E_N(V)|\ll_\epsilon
N^{-1/2}\mathcal R^\epsilon\mathcal W_N(H_{E_N}).
\tag{19}
\]

Thus \(\mathcal W_N(H_{E_N})\ll N^{1/2}T^{29/25+\epsilon}V^{-8}\), uniformly for all necessary blocks and their actual masks, would be sufficient after a logarithmic dyadic recombination. It is **unproved and may be too strong**: the coarse-scale positive envelope must be tested before selecting it as a research target. The paper supplies no arithmetic suppression of that term. In particular, this report does not recommend replacing the signed full moment by an unchecked positive envelope majorant.

### D. Gap ledger, ranking and dated screens

At \(V=T^v\), dividing the two accepted distribution terms by \(T^{29/25}V^{-12}\) gives powers

\[
10v-\frac{29}{25},\qquad
\frac{20}{13}v-\frac4{25}.
\tag{20}
\]

At \(v=\beta\), a hypothetical gain \(T^{-a}\) in the first term and \(T^{-b}\) in the second would need respectively
\(a\ge10\beta-29/25\) and \(b\ge(20/13)\beta-4/25\). Improving only the second term cannot overcome the first. The first deficit is about 0.12966 in the moment exponent. These are necessary for that particular two-term envelope to certify the milestone, not lower bounds for actual coefficients. Any new exponent claim also needs the full smoothing identity, its \(T^7\) twelfth-moment factor, and its \(O(T^{8+\epsilon})\) error. The milestone implies \(102/325\), not one quarter.

Ranked recommendation:

1. **Keep (4) as the complete arithmetic objective.** It isolates exactly what the accepted proof does not control. Any viable proof must retain the actual \(r_2\), both phases and infinite tail, and save against both powers in (20). The presently checked literature supplies no certified method; do not advertise a source-backed success probability or launch a campaign from this report.
2. **Retain the weighted parabola lift (15)--(19) as a bounded exploratory interface.** It is exact and prices trace, coefficients and scale. Its first test must be the coarse positive envelope, before attempting arithmetic packet estimates. Certified saving: zero; surviving hypothetical gain must exceed (20).
3. **Retain amplitude-sensitive cone envelopes only with a priced arithmetic envelope estimate.** Formula (12) pays the missing trace, but the physical envelope sum remains open. Certified saving: zero.
4. **Reject a direct cheap Guth--Maynard import.** Formula (9) worsens the one-interval term; even a lossless fantasy transfer preserves it. This does not reject a future new arithmetic adaptation of their argument.

Fresh primary records on 2026-09-26:

- [Bourgain--Watt, 1709.04340](https://arxiv.org/abs/1709.04340): withdrawn v2, 16 July 2023; the notice removes theorem status from Theorems 1--3.
- [Dong--Robles--Zeindler, 2601.00292](https://arxiv.org/abs/2601.00292): withdrawn v2, 5 January 2026; the missing \(L^2\) factor changes \(L^5\) to \(L^7\) and removes the claimed gain.
- [Li--Yang, 2308.14859](https://arxiv.org/abs/2308.14859): v2, 14 September 2023. No newer arXiv version appears. This is a record check; the accepted source card's five repairs, restricted small-cap range and Case-B logarithm remain intact.
- [Lamzouri, 2605.21476v1](https://arxiv.org/abs/2605.21476), 20 May 2026: abstract/version screen only. It concerns signed Omega results using a phase-compatible sectorial resonance kernel. It supplies lower-value constructions, not the required upper high-value estimate; no theorem is imported here.
- [Yamaguchi--Fujima--Kuratsubo--Nakai--Yoneda, 2609.04725v1](https://arxiv.org/abs/2609.04725), 4 September 2026: numerical-evidence paper; no asymptotic upper bound imported.
- [Gao, 2604.23918v1](https://arxiv.org/abs/2604.23918), 27 April 2026: smooth-number-restricted representation sum; no unrestricted-circle upper theorem imported.

This is a bounded current search and three-interface audit. It does not certify completeness of the worldwide literature or re-audit every theorem in the inherited modular source report.

## 4. First doubtful or unproved step

For (4), the missing step is arithmetic suppression of actual high peaks beyond the coefficient-uniform diagonal/one-interval bound. There is no such new estimate in this report.

For (5), the first mismatch is \(\sqrt n\) versus \(\log n\). The explicit elementary repair incurs (8)--(9), and the diagonal remains even before those losses. For (10), the spatial trace can be paid, but the retained physical envelope is not bounded at the target size. For (13), the lift and trace exist, but the coarse weight maximum and fourth-order restriction give no twelfth-moment gain; (19)'s positive envelope is a new, unvalidated estimate.

The exact-resonance contribution already controlled in the graph is not the diagonal of every new operator. Nor is a large positive near-resonance sum a lower bound for the signed complete moment. Neither confusion can close (4).

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `complete_source_scope` | Pass for audit: (1)--(4) concern the entire series. Block lifts are explicitly intermediate; all blocks, partial cutoffs, singleton and Schwartz tail must be reassembled. |
| `actual_arithmetic_coefficients` | Pass: all lifts preserve \(r_2(n)n^{-3/4}\Psi\); generic coefficient assertions are separately labelled. No arbitrary vector is substituted for physical \(r_2\). |
| `current_primary_hypotheses` | Pass within three-interface scope: inspected current full theorem text, coefficient norm, phase, separation, ambient dimension and exponent range. No theorem inferred from metadata. |
| `withdrawals_and_versions` | Pass for named records: both withdrawals unchanged; dates and current v2 records recorded above. |
| `all_costs_restored` | Pass as audit: frequency packets, radius cover, threshold loss, ambient polynomial length, Jacobians, trace and envelope costs explicit. Unproved packet/envelope savings are not set to zero cost. |
| `signed_absolute_distinction` | Pass: the high-value event uses the full signed cosine sum. Positive envelope objectives are marked stronger and unvalidated. |
| `independent_gain_frontier` | Formula (20) independently checked algebraically from the accepted statement. This is not the round's isolated blind review; that remains the conductor's gate. |
| `real_endpoint_uniformity` | Retained: real level sets and fixed windows in trace formulas; accepted reconstruction pays inclusive jumps. No integer-only or averaged-radius theorem is substituted. |
| `full_proof_scope` | Pass: complete twelfth moment is an intermediate milestone; original t=1 is only one internal sector. M1/M2 and arbitrarily high fixed moments remain distinguished. |
| `no_unproved_import` | Pass: no external application, new exponent, graph node or parent closure is asserted. |

The aligned arbitrary-coefficient example in the accepted kernel survives every proposed coefficient-uniform lift: it produces a peak of height \(N^{1/4}\), width \(N^{-1/2}\), and twelfth moment \(\gg N^{5/2}\). Taking \(N\asymp T^{4\beta}\) gives \(T^{10\beta}\). It rules out removing the one-peak term by generic norm/restriction arguments alone, while saying nothing false about the fixed arithmetic coefficient family. The actual positive-majorant obstruction from the supplied Round202 checkpoint is also retained.

## 6. Dependencies and exact artifacts used

Read-only local context was the task brief and exactly its permitted list:

- `protocol.md`.
- `state/proof_obligations.yml`; relevant records extracted for `GC-target`, `M9`, `M9-M1`, `M9-M2`, `GC-external-Li-Yang-theta-star`, `GC-complete-square-root-large-values-moment-bound`.
- `state/active_campaign.yml`.
- `strategy/round205_full_frontier_strategy_review.md`.
- `rounds/codex-managed/gc-complete-large-values-duality/synthesis.md`.
- `strategy/gauss_circle_strategy_checkpoint_round202_2026-09-23.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/current_primary_methods_audit.md`.
- `sources/li_yang_2023.md`.

External primary theorem texts: Guth--Maynard 2405.20552v2, Theorem 1.1 and surrounding coefficient warning; Guth--Maldague 2206.01093v2, Theorem 2 and its envelope definition; Kim--Ko 2511.04503v2, Theorem 1.1, equations (3)--(4), and Theorem 1.4, equation (8). URLs and source dates occur above. Additional papers were record/abstract screens only. Discovery searches used Gauss-circle moments/large-values/improvement, Dirichlet-polynomial large values, amplitude-dependent cones and weighted wave envelopes; unrelated/nonprimary search hits were not used as evidence.

No sibling derivation was read. No source card, state file, matrix, synthesis, draft, legacy artifact or successor plan was edited. Only this assigned report was written.

## 7. Recommended state effect

**No change** to accepted graph mathematics or the pointwise exponent. **Retain** the exact weighted-parabola lift as candidate strategy evidence. **Reject** an unpriced direct application of the Dirichlet-polynomial theorem and any proposed automatic deletion of the generic peak term. **Retain** all source qualifications and the full quarter target.

The task's exit is `strategy_review_no_source_compatible_gain`. The conductor may select a complete arithmetic objective using the independent frontier reports, but this report neither opens the next round nor certifies a new theorem. The full high-value remainder (4) is concrete and complete; a costed arithmetic proof of it remains to be found.
