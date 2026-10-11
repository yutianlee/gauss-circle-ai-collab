# Task Brief: actual_symbol_norm_power_audit

- Campaign: `m9-m1-t1-complete-source-coefficient-mask-analysis`
- Research round: `200` (`complete_source_coefficient_mask_analysis`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`
- Generated: `2026-09-23T11:45:02.347606+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete original-t=1 residual even-shift source, with P1 and P2 recombined, be bounded at L^2 X^epsilon; otherwise what exact coefficient norm or unmasked analytic estimate is missing after every mask and reconstruction cost?

## Reference formula and distinctions

C_even=sum_(0<r<R0, 2|r)(1-r/R0) sum_N c_(N+r,sigma)^rem conjugate(c_(N,sigma)^rem) e(sigma sqrt(X) r/(sqrt(N+r)+sqrt(N))), R0=ceil(L). Target Re C_even << L^2 X^epsilon; c and total zero-extended lambda are exactly K185.1--3. E_R<=2D+4Re C_even and scalar prefactor O(L).

- Complete source precedes P_cl/P1/P2, both opposing orientations, all gcd/height/packet splits and later T branches.
- A partition identity removes artificial partition boundaries only for a common genuine transport; it provides no analytic saving.
- Geometric interval masks require a proved unmasked all-vector bilinear estimate and a controlled product or projective norm.
- No t>=2, complete M1/M2, bridge, target or exponent conclusion is implied by a t=1 result.

## Assigned target

Independently audit the full actual source coefficients, all masks and a quantitative product/projective-norm interface. Determine which geometric row sections are intervals, which arithmetic masks remain inside the kernel/amplitude, and whether an affordable norm is actually proved. Give raw L^3 correlation capacity versus L^2 target, high-h Y loss only as a subsidiary ledger, and scalar reconstruction. Display an explicit all-cost conditional inequality for a source-compatible bilinear import; do not claim a Kloosterman kernel or imported saving without proof. Follow exact symbol antecedents as needed and log them. Write only your assigned report.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round200_complete_source_coefficient_mask_strategy.md`
- `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`
- `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`
- `strategy/gauss_circle_strategy_review_2026-09-23.md`

## Required controls

- `complete_source_multiplicity`
- `actual_coefficients_only`
- `literal_endpoint_zero_extension`
- `partition_recombination`
- `row_interval_vs_arithmetic_masks`
- `product_and_projective_norms`
- `even_parity_connector`
- `one_outer_real_part`
- `net_power_ledger`
- `no_capacity_lower_bound`
- `no_unverified_theorem_import`
- `protected_parent_and_exponent_scope`

## Required deliverables

- Seven-section protocol report with exact hypotheses, proof, first open step, controls, dependencies and state recommendation.
- No shared-state edits; stop after the assigned report.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
