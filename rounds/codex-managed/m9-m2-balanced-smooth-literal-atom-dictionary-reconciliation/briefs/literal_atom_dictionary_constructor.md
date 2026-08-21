# Task Brief: literal_atom_dictionary_constructor

- Campaign: `m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation`
- Research round: `113` (`m9_m2_balanced_smooth_literal_atom_dictionary_reconciliation`)
- Role: `formalizer`
- Access mode: `selected_context`
- Graph SHA-256: `9d560539df2db7d69e72dd6e7e6af7247f00237ee795ac13b053b3f34eae8efa`
- Generated: `2026-08-21T01:41:12.870065+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 98%.
- Numerical/experimental effort: at most 2%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the accepted denominator profile, clipped odd-frequency partition, Vaaler coefficient, smooth stationary transform, gcd partition, and prior-owner corrections be instantiated as one finite coefficientwise atom dictionary for every balanced smooth M2 residual block?

## Reference formula and distinctions

For each literal residual block B, define its normalized positive-frequency coefficient a_B(h,k), its exact smooth-gcd partition, the full quarter packet Q_B, and target-safe square, near-square, high-gcd, and transform-error corrections so that the physical block equals 8 Re[-e(1/8)X^(1/4)(LK)^(-3/4)T_B/(2pi)] and the residual T_B is exactly the full quarter packet minus the prior-owner corrections.

- y=floor(sqrt X), D_j=2^(-j)y, and the one hard plus full smooth denominator profiles
- H_D=floor(DX^(-1/4)) and an exact clipped positive-frequency partition including top and bottom pieces
- Phi(u)=pi u(1-u)cot(pi u)+u and the exact positive M2 normalization
- balanced ratio 1<=K/L<=16 with K=XL/D^2
- full slanted stationary symbol and smooth support crossings
- a fixed finite smooth gcd partition with an explicit high-gcd boundary owner
- square, near-square, high-gcd, transform-error, sign, and conjugacy tags
- one-count equality and scale-normalized seminorms uniform in real X

## Assigned target

Construct and prove the complete finite actual-symbol atom dictionary from the accepted dyadic profile, Vaaler coefficient, stationary transform, and Round-112 guardrails.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/derivation_packet.md`
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/candidates/conductor_literal_atom_dictionary.md`
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md`
- `rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md`
- `rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md`
- `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/reports/m2_outside_packet_assembly_attack.md`
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/synthesis.md`

## Required controls

- `denominator_telescoping_and_hard_profile`
- `frequency_telescoping_top_bottom_and_clipping`
- `height_floor_and_empty_block`
- `exact_Phi_and_positive_frequency_constant`
- `positive_negative_frequency_recombination`
- `balanced_ratio_boundary_and_real_X`
- `stationary_symbol_support_crossings_and_error`
- `smooth_gcd_one_count_and_boundary_owner`
- `square_near_square_and_large_gcd_priority`
- `finite_omega_and_no_cross_block_cancellation`
- `profile_seminorms_and_uniformity`
- `capacity_and_downstream_scope`

## Required deliverables

- A seven-section formalization report.
- A literal finite dictionary and exact one-count theorem.
- A complete list of any irreducible missing definitions.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
