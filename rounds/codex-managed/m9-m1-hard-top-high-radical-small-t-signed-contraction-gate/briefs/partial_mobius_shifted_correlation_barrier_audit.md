# Task Brief: partial_mobius_shifted_correlation_barrier_audit

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Research round: `183`
- Role: `barrier_no_go`
- Access mode: `selected_context`
- Graph SHA-256: `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Generated: `2026-08-27T19:17:03+08:00`
- Status: candidate evidence only; do not edit shared proof state

## Research allocation

- Analytical/algebraic effort: 100%.
- Numerical/experimental effort: 0%.
- Exact finite algebra and power checks are allowed only as mechanical
  controls.

## Frozen objective

The owner remains the complete one-absolute-value small-\(t\) aggregate at
\(L^{3/2}X^\varepsilon\), including \(t=1\), both signs, every literal
coefficient field, shell, crossing, and endpoint.  This task audits possible
mechanisms; it may not replace the owner by a fixed-row or correlation norm.

## Assigned target

Perform two exact hostile derivations.

1. Put \(F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})\), expand
   \(\mu^2(s)\), set \(s=a^2b\), \(u=at\), and prove the exact kernel
   \[
    K_{L,T_L}(b,u)=
    \sum_{\substack{a\mid u\\a^2b>L,\ u/a<T_L}}\mu(a).
   \]
   Audit every strict inequality, ceiling, product-support, multiplicity,
   and endpoint.  Test a truncation at the target scale near
   \(a\asymp\sqrt L\): identify all tails with restored powers and decide
   whether the remaining signed core is genuinely smaller or is the
   original hard cone plus target-safe corrections.
2. Derive the exact van der Corput/shifted-correlation sufficient condition
   for a fixed \(t\) row, with its diagonal, shift length, literal
   coefficient correlation, phase difference
   \(\sigma t\sqrt X(\sqrt{s+q}-\sqrt s)\), support intersections,
   endpoints, and target power.  Prove the connector to the sufficient
   three-quarter row estimate or identify the first failed inequality.
   Compare the resulting statement line by line with
   `M9-M1-shifted-divisor-correlation-PSC` and the accepted
   delta/Kloosterman deficit; determine whether it is genuinely new,
   stronger, equivalent, or a restatement.

Return the smallest exact lemma or mechanism no-go.  Do not claim the
aggregate unless the full connector is proved.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round183_m1_hard_top_high_radical_small_t_signed_contraction_strategy.md`
- `proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/candidates/formalized_hard_m1_squarefree_radical_reduction.md`
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reports/hard_m1_radical_connector_capacity_audit.md`
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/independent_reduction_and_self_return_review.md`
- `rounds/codex-managed/m9-m1-cross-product-offset-pairing/synthesis.md`
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/synthesis.md`
- `rounds/codex-managed/m9-m1-near-product-delta-salie/synthesis.md`
- `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/synthesis.md`

## Required controls

- `exact_mobius_kernel_both_inequalities`
- `ceil_sqrt_L_and_strict_t_boundary`
- `product_support_and_zero_extension`
- `partial_truncation_tail_power`
- `u_equals_one_original_cone_control`
- `complete_mobius_self_return_comparison`
- `large_t_sector_once_only`
- `fixed_t_van_der_Corput_constants_and_diagonal`
- `shift_range_and_support_intersection`
- `literal_correlation_phase_and_coefficient`
- `fixed_t_three_quarter_connector`
- `sum_over_t_restored_power`
- `old_PSC_interface_comparison`
- `delta_Kloosterman_H_over_L_deficit`
- `correlation_not_owner`
- `t1_and_endpoint_retention`
- `no_literal_lower_mass_from_adversarial_capacity`
- `downstream_and_exponent_quarantine`
- `no_in_round_pivot`

## Required deliverable

Write only
`reports/partial_mobius_shifted_correlation_barrier_audit.md`.  Use the
mandatory seven-section report contract.  Include the exact derivations,
first doubtful step, controls, dependencies, and recommended state effect.
Do not edit graph or shared state.
