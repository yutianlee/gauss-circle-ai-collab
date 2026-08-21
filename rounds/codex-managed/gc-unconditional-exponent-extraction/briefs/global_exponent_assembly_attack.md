# Task Brief: global_exponent_assembly_attack

- Campaign: `gc-unconditional-exponent-extraction`
- Research round: `91` (`unconditional_exponent_extraction`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `b3a0a086608be2df3b56c6c9f996206796998b3afdf750b6162d760c614a811b`
- Generated: `2026-08-17T00:43:44.131894+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Do the accepted hyperbola--Vaaler reduction, pointwise Fejer product count, and direct M1/M2 block menu prove P(X)<<_epsilon X^(1/3+epsilon) uniformly for real X?

## Reference formula and distinctions

With x=delta-ell, use T2S when x<=1/3 and the full second-derivative bound when x>=1/3; then audit R5, dyadic assembly, hard endpoints, and all actual coefficients.

- Omega: 1/4<=delta<=1/2, 0<=ell<=delta-1/4
- T2S exponent delta-ell
- second-derivative exponents (1+ell-delta)/2 and (3delta-1-ell)/2
- R5 pointwise residual X^(1/4+epsilon)
- candidate global exponent theta=1/3

## Assigned target

Build the literal H1--H4 plus R5 plus direct-block assembly, prove the strongest unconditional exponent it yields, and prepare a validator-ready theorem statement.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `state/active_campaign.yml`
- `strategy/conductor_0817_full_proof_strategy.md`
- `rounds/codex-managed/gc-unconditional-exponent-extraction/derivation_packet.md`
- `rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/synthesis.md`
- `rounds/obligation-main/round_004/responses/A1-004.md`
- `rounds/obligation-main/round_004/reviews/A4.md`
- `rounds/web-research-test/round_027/judge/judge-027.md`
- `sources/vaaler_1985.md`
- `sources/tao_trudgian_yang_2025.md`

## Required controls

- `exact_block_normalization`
- `one_third_region_optimization`
- `second_derivative_small_curvature`
- `actual_M1_M2_coefficients`
- `R5_pointwise_product_count`
- `exact_product_and_floor_endpoint`
- `hard_top_BV`
- `small_denominator_owner`
- `dyadic_frequency_and_denominator_assembly`
- `real_X_uniformity`
- `dependency_status_and_source_map`
- `downstream_scope`

## Required deliverables

- Exactly seven numbered report sections.
- A complete implication diagram, exponent table, and proposed graph effect.
- Write only rounds/codex-managed/gc-unconditional-exponent-extraction/reports/global_exponent_assembly_attack.md.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
