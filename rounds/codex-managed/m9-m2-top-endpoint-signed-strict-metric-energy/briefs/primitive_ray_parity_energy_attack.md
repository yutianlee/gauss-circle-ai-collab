# Task Brief: primitive_ray_parity_energy_attack

- Campaign: `m9-m2-top-endpoint-signed-strict-metric-energy`
- Research round: `80` (`m9_m2_top_endpoint_signed_strict_metric_energy`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `cb007911c1e9d407d9adbc8919ce44cc3eaab411a212d0925e1176f5a154a43a`
- Generated: `2026-08-16T07:08:04.956367+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

After removing primitive square rays, exact nonsquare centers, and the positive-safe blocks AJD^3<<L^3, can the remaining complete-coefficient strict-metric nonsquare sum be bounded by L^2 X^epsilon through a signed primitive-ray or fiber argument?

## Reference formula and distinctions

For q=(b-a)/2, theta=Lambda/k=X(sqrt(b)-sqrt(a))^2/(2k), g=2n+1, the exact combined phase is (-1)^q e(-g theta/2). If ell is the nearest integer and eta=theta-ell, it is (-1)^(q+ell)e(-g eta/2). Bound the dyadic strict-metric sum with AJD^3>>L^3 and 0<|eta| asymp 1/R while retaining B^circ_(a,b,k)(g).

- The exact square family, exact nonsquare centers, and blocks AJD^3<<L^3 are already removed.
- The residual window has ordinary density 1/R; density and centered discrepancy must be controlled together.
- The literal outer sign is (-1)^(q+ell) after nearest-integer reduction and may not be discarded.
- The complete Round-77 centered integral, finite odd lift support, floors, stars, profiles, and saddle transitions remain inside the sum.
- The target is L^2 X^epsilon after all dyadic A,D,K,G,R blocks, with no absolute sum over primitive rays or reciprocal modes.

## Assigned target

Exploit the exact (-1)^(q+ell) fiber parity, complete odd-lift transform, and density/discrepancy decomposition to prove the residual signed energy or isolate its smallest actual-symbol correlation.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0816_full_proof_strategy.md`
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/derivation_packet.md`
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/briefs/primitive_ray_parity_energy_attack.md`
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md`
- `rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reviews/conductor_round78_adjudication.md`
- `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reviews/conductor_round79_adjudication.md`

## Excluded context

- `all sibling Round-80 reports`

## Required controls

- `external_normalization`
- `round78_round79_exclusions`
- `primitive_parity`
- `combined_odd_lift_phase`
- `nearest_integer_sign`
- `strict_metric_one_count`
- `density_and_discrepancy`
- `complete_actual_coefficient`
- `lift_support_and_step_two_variation`
- `fiber_product_parity`
- `safe_block_boundary`
- `near_square_and_Pell`
- `perfect_power_metric_recurrence`
- `endpoints_stars_and_collars`
- `coefficient_adversary`
- `rank_one_self_return`
- `downstream_scope`

## Required deliverables

- One seven-section analytic report at the assigned path.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
