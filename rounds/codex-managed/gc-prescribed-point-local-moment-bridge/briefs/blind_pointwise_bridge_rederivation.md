# Task Brief: blind_pointwise_bridge_rederivation

- Campaign: `gc-prescribed-point-local-moment-bridge`
- Research round: `94` (`prescribed_point_local_moment_bridge`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
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

Independently prove or refute the persistence, one-separated sampling, integer exceptional-set, and local-moment implication package, and identify the strongest conclusion available from the global moment alone.

## Permitted context

- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/derivation_packet.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all prior reports, candidates, reviews, syntheses, source cards, and sibling Round-94 reports`
- `all web sources`

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
- `canonical_core_nonimplication`

## Required deliverables

- Exactly seven numbered report sections.
- A full proof or exact first failure for every bridge statement, with no local-frequency claimant context.
- Write only rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reports/blind_pointwise_bridge_rederivation.md.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
