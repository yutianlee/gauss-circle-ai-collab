# Task Brief: prescribed_centre_wave_hostile_source_audit

- Campaign: `m9-m2-unbalanced-prescribed-centre-wave-gate`
- Research round: `118` (`m9_m2_unbalanced_prescribed_centre_wave_gate`)
- Role: `source_auditor`
- Access mode: `selected_context`
- Graph SHA-256: `d4e626708a04680cc97b043835466948204c6e123a1dc9fd569b50377349feeb`
- Generated: `2026-08-21T15:58:10.775648+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 98%.
- Numerical/experimental effort: at most 2%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the exact smooth unbalanced M2 prescribed-centre truncated divisor wave satisfy O(X^(1/4+epsilon)), admit a target-safe strict subrange or quantified actual-sign saving, fail by a rigorous literal coherent countermodel, or reduce to a smaller signed survivor after the proposed falsification controls?

## Reference formula and distinctions

R_(D,L)(X)=sum_s sum_(r|s,r odd) chi_4(r) W(X/(rD)) Q_L(r(X-s)/(4X)), with Q_L(y)=int q_L(h)h^(-1)e(hy)dh, r asymp X/D, |s-X| rapidly restricted to D/L, absolute capacity (D/L)X^epsilon, and target X^(1/4+epsilon). Equivalently R=sum_(r odd)chi_4(r)W(X/(rD))sum_k q_L(4Xk/r^2)k^(-1)e(Xk/r), modulo the accepted flat-smooth normalization and target-safe stationary remainder.

- X large real; D=X^delta and L=X^ell in the strict residual unbalanced region
- 1/4<=delta<1/2, 0<=ell<delta-1/4, and 178ell+1638delta>463
- K=XL/D^2, M=LK, F=XL/D, Delta=D/L, missing factor H_D/L=D/(LX^(1/4))
- literal nonnegative q_L and smooth W profiles with inherited Vaaler height taper
- chi_4 remains on the odd complementary divisor r; the truncated coefficient is not r_2/4
- exact centre s=X is divisor-bounded and cannot alone falsify the target
- a positive or coherent subset is not a lower bound without controlling every complementary signed term
- Round 117 exposes an analogous prescribed-centre product wave but supplies no automatic exponent transfer
- sharp, starred, hard, and arithmetic-owner endpoints lie outside a flat-smooth claim unless their exact kernels are retained

## Assigned target

Hostilely audit every proposed upper bound and countermodel for complement cancellation, transform self-return, false positivity, endpoint loss, and exact primary-source theorem fit; determine whether the pointwise wave strategy remains viable.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/synthesis.md`
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reports/unbalanced_product_source_hostile_audit.md`
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reviews/conductor_round107_recombination_and_capacity.md`
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_involution_product_and_source.md`
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/derivation_packet.md`
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/candidates/conductor_wave_probe.md`
- `sources/popov_2024_voronoi_gauss.md`

## Required controls

- `literal_wave_and_physical_normalization`
- `product_and_reciprocal_row_equivalence`
- `exact_centre_and_tie`
- `near_centre_kernel_sign`
- `prime_square_fourth_power_divisor_rich`
- `coherent_run_selector_and_complement`
- `character_residue_and_both_signs`
- `profile_support_and_endpoint_kernels`
- `capacity_before_after_each_norm`
- `actual_symbol_vs_unsigned_adversary`
- `strict_residual_exponent_region`
- `external_theorem_hypothesis_fit`
- `round117_transfer_scope`
- `downstream_scope`

## Required deliverables

- A seven-section hostile/source report.
- A pass/fail table for normalization, arithmetic controls, complement, capacity, endpoints, sources, and scope.
- A rigorous named no-go, verified countermodel, or the exact theorem still required.
- A precise state recommendation.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
