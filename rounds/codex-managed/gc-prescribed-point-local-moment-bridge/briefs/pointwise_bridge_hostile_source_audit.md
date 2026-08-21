# Task Brief: pointwise_bridge_hostile_source_audit

- Campaign: `gc-prescribed-point-local-moment-bridge`
- Research round: `94` (`prescribed_point_local_moment_bridge`)
- Role: `source_auditor`
- Access mode: `selected_context`
- Graph SHA-256: `6b7b5b681890edd49b0e0a525fe813044943d4072dd7fc90e27620615d2e93ae`
- Generated: `2026-08-17T04:02:22.683041+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 90%.
- Numerical/experimental effort: at most 10%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Starting only from the accepted global real mean square, prove the exact one-sided persistence and discrete exceptional-set consequences, then determine and attack the weakest uniform short-window actual-coefficient moment that would upgrade a prescribed point to the quarter exponent.

## Reference formula and distinctions

If M=|P(x)|, monotonicity gives M^2*min(H,M/(2*pi)) << sup_(|I|=H) int_I|P|^2. Audit whether the standard local scale H Y^(1/2+epsilon) for H=Y^(1/4+o(1)), or the stronger total scale Y^(3/4+epsilon) on a fixed longer window, can be proved from the literal moving M1/M2 expansion; otherwise isolate the exact signed rational-frequency cluster survivor.

- P(t)=N(sqrt(t))-pi*t with inclusive integer jumps
- Round-93 global moment int_Y^(2Y)|P(t)|^2 dt << Y^(3/2+epsilon)
- one-sided persistence length M/(2*pi)
- one-separated sampling sum_x|P(x)|^2
- local bridge M << Q^(1/3)+(Q/H)^(1/2) for local mass Q
- target window H=Y^(1/4+sigma)
- frequency cells |h/(4d)-nu/H| << H^(-1)
- top denominator D=Y^(1/2) and actual height |h|<<D Y^(-1/4)

## Assigned target

Try to break every persistence, sampling, local-moment, endpoint, and implication normalization; audit primary short-interval or large-value sources and decide whether any literal theorem beats the top-scale cluster barrier.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `state/gap_register.md`
- `state/active_campaign.yml`
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/derivation_packet.md`
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/candidates/conductor_persistence_and_local_bridge.md`
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/candidates/conductor_exact_cluster_kernel.md`
- `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/synthesis.md`
- `strategy/conductor_0817_full_proof_strategy.md`

## Required controls

- `positive_right_persistence`
- `negative_left_persistence`
- `integer_jump_convention`
- `dyadic_boundary_windows`
- `bounded_overlap_sampling`
- `integer_exceptional_count`
- `local_bridge_exponent`
- `additive_error_ledger`
- `unit_window_equivalence`
- `moving_height_floor`
- `hard_top_and_stars`
- `chi4_and_two_sided_frequency`
- `exact_rational_clusters`
- `M1_M2_R5_ownership`
- `top_scale_spacing_capacity`
- `canonical_core_nonimplication`
- `source_hypothesis_map`

## Required deliverables

- Exactly seven numbered report sections.
- A hostile seam table, literal primary-source map, sharp controls, and a promote/revise/reject recommendation.
- Write only rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reports/pointwise_bridge_hostile_source_audit.md.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
