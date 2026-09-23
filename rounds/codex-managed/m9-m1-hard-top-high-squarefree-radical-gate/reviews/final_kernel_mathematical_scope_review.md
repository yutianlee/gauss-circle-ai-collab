# Round 181 final kernel mathematical and scope review

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Task: `round181_final_kernel_review`
- Role: independent final mathematical, connector, and artifact-scope review
- Generated: `2026-08-27T09:02:45.2613141+00:00`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Claimant/reviewer/blind status: independent reviewer; not a claimant and
  not blind; no graph or shared-state edit authorized
- Dependencies: `M9-M1-top-endpoint-transform`, `H4-Phi-regularity`,
  `M9-M2-dyadic-weight-nondegeneracy`, and
  `Divisor-bound-elementary`

## 1. Result

**GREEN.**  The repaired formal candidate and durable kernel agree with
the three task reports, the independent/hostile/blind reviews, and the
starting graph.  They prove exactly the product/squarefree reduction, two
disjoint target-safe sectors, the small-\(t\) residual owner, and the
all-\(L\) Möbius self-return.  They keep coefficient-uniform capacity
separate from literal lower mass, scope the Mellin observation to the
central/full-divisor shortcut, and state the hard-parent connector in the
correct two steps.  The durable kernel is now explicitly signwise for
every \(\sigma\in\{+1,-1\}\).  No parent, bridge, theorem, or exponent
promotion is licensed.

## 2. Exact statement and hypotheses audited

For one literal residual shell of the unique hard M1 profile, the complete
coefficient is zero-extended off its exact support.  For each fixed
\(\sigma\in\{+1,-1\}\), the candidate correctly defines

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\
                   r/h\ {\rm odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\mathrm{lit},\sigma}(h,r/h)
\]

and groups the literal cone as

\[
 \mathcal T_{L,\sigma}^{M1}
 =\sum_r C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})
 =\sum_{\substack{s\geq1\\\mu^2(s)=1}}\sum_{t\geq1}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}).
\]

The audit assumes only the accepted bounded literal normalization, fixed
hard-cone constants, the exact endpoint/zero-extension conventions, the
elementary divisor bound, and the starting graph named in the header.  It
does not assume multiplicativity, smoothness across literal boundaries,
or cancellation for an arbitrary coefficient family.

## 3. Proof and derivation audit

The mathematical kernel checks out.

For a literal incidence, put \(G=(h,n)\), remove the gcd, and take the
unique squarefree parts of the two coprime quotients.  This gives

\[
 h=Gda^2,\qquad n=Geb^2,\qquad s=de,\qquad t=Gab,
 \qquad (da,eb)=1,
\]

with \(d,e\) squarefree and the original oddness/literal-support tests
retained.  Hence \(G\mid t\), and \(hn=st^2\asymp L^2\).  The
parametrization and the product regrouping preserve incidences; they do
not assert that a product fibre is a singleton.

The divisor estimate gives
\(|C_{L,X}^{\sigma}(r)|\ll_\varepsilon X^\varepsilon\).  Counting
\(O(1+L/\sqrt s)\) possible multipliers for fixed \(s\) proves

\[
 \sum_{s\leq L}\sum_t|C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

For fixed \(t\), the supported \(s\)-interval contains
\(O(1+L^2/t^2)\) integers.  Summing for
\(t\geq\lceil\sqrt L\rceil\), while using
\(s>L\Rightarrow t\ll\sqrt L\), proves the disjoint second sector

\[
 \sum_{\substack{s>L\\t\geq\lceil\sqrt L\rceil}}
 |C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The exact complement is therefore
\(s>L\), \(1\leq t<\lceil\sqrt L\rceil\).  At \(t=1\), one has
\(G=a=b=1\), so the retained face is the coprime squarefree literal
cone.  Its \(L^2\) statement is only geometric/adversarial capacity, not
literal lower mass.

For

\[
 K_L(b,u)=\sum_{\substack{a\mid u\\a^2b>L}}\mu(a),
\]

finite Möbius inversion gives exactly

\[
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF_\sigma(st^2)
 =\sum_{b,u}K_L(b,u)F_\sigma(bu^2).
\]

Since \(K_L(b,u)=\mathbf 1_{u=1}\) for \(b>L\), the exact all-\(L\)
correction is

\[
 E_{L,\sigma}=
 \sum_{\substack{b\leq L\\u\geq1}}K_L(b,u)F_\sigma(bu^2)
 -\sum_{r\leq L}F_\sigma(r).
\]

Both terms are target-safe; in particular the required
\(-\sum_{r\leq L}F_\sigma(r)\) term is present in the repaired candidate
and kernel.  Joint \((s,t)\) lifting is a permutation of product indices.
The full-orientation Mellin factor is correct, including the retained
\(2^{-ik\tau}\) prefactor at \(p=2\); an odd
\(p\equiv3\pmod4\) exponent kills only \(\tau=0\), not the noncentral
modes of the literal truncated cone.

## 4. First doubtful or unproved step

The first genuinely unproved mathematical step remains

\[
 \left|\sum_{\substack{s>L,\ \mu^2(s)=1\\
                        1\leq t<\lceil\sqrt L\rceil}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\]

already on \(t=1\).  No report, review, candidate, or kernel proves this
literal \(L^{1/2}\) contraction.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact product regrouping and multiplicity | **PASS.** |
| Unique \(r=st^2\) and \((G,d,e,a,b)\) parametrization | **PASS.** |
| Low-\(s\) target-safe sector | **PASS.** |
| Disjoint high-\(s\), large-\(t\) target-safe sector | **PASS.** |
| Exact small-\(t\) complement and mandatory \(t=1\) | **PASS.** |
| All-\(L\) Möbius correction | **PASS.** The negative \(r\leq L\) sum is present. |
| Joint-\(t\), capacity, and literal/adversarial scope | **PASS.** No literal lower mass is claimed. |
| Mellin and prime-2 scope | **PASS.** Only the central/full-divisor shortcut is parked. |
| Hard-parent connector | **PASS.** The small-\(t\) theorem plus the two safe sectors proves `M9-M1-top-endpoint-signed-cone`; the accepted transform then discharges only the hard residual child of `M9-M1-physical-one-count-assembly`. |
| Both frequency signs in durable kernel | **PASS.** The repaired statement, coefficient, phase, Möbius variable, and scope are explicitly signwise. |
| UTF-8 and control characters in candidate/kernel | **PASS.** Both decode as strict UTF-8, contain no replacement character, and contain no disallowed control byte. |
| TeX command integrity in candidate/kernel | **PASS.** No lost-backslash tab, carriage-return, or form-feed corruption was found. |
| Protocol metadata | **PASS.** Campaign/task, graph hash, generated time, exact context paths, dependencies, role, and review status are present. |

No numerical evidence or external theorem was used.

## 6. Dependencies and exact artifacts used

This review used exactly:

1. `protocol.md`;
2. `state/proof_obligations.yml` at the starting hash in the header;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_high_radical_signed_attack.md`;
5. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_radical_connector_capacity_audit.md`;
6. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/blind_hard_m1_radical_rederivation.md`;
7. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/independent_reduction_and_self_return_review.md`;
8. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/literal_scope_capacity_owner_review.md`;
9. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/blind_post_unmask_radical_review.md`;
10. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/conductor_report_reconciliation.md`;
11. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/product_squarefree_connector_review.md`;
12. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/literal_capacity_mellin_scope_review.md`;
13. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/conductor_round181_adjudication.md`;
14. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/candidates/formalized_hard_m1_squarefree_radical_reduction.md`;
15. `proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`.

The starting graph nodes checked were
`M9-M1-top-endpoint-transform`, `H4-Phi-regularity`,
`M9-M2-dyadic-weight-nondegeneracy`, `Divisor-bound-elementary`,
`M9-M1-top-endpoint-signed-cone`,
`M9-M1-direct-hard-smooth-separate-one-third-minimax`,
`M9-M1-physical-one-count-assembly`, `M9-M1`, and the named inherited
product-fibre, ordered-cell, canonical-Gram, and complete-Möbius
obstructions.

## 7. Recommended state effect

**Promote the narrow kernel only.**  The graph may receive one subordinate
proved reduction containing the exact coordinates, the two target-safe
sectors, and their exact small-\(t\) complement; one explicit open
small-\(t\) obligation; and one mechanism-scoped obstruction containing
the all-\(L\) Möbius correction, joint-coordinate self-return,
central-Mellin limitation, and coefficient-uniform \(t=1\) capacity.  The
small-\(t\) owner, hard signed-cone owner, independent smooth M1 parent,
M9-M1, every M2 owner, endpoint uniformity, M9, both bridges, the quarter
theorem, and all exponents must remain unchanged.
