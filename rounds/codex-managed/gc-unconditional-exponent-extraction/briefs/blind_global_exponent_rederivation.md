# Task Brief: blind_global_exponent_rederivation

- Campaign: `gc-unconditional-exponent-extraction`
- Research round: `91` (`unconditional_exponent_extraction`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
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

Independently decide whether the frozen statement proves the uniform one-third theorem, and identify the first missing seam if it does not.

## Permitted context

- `rounds/codex-managed/gc-unconditional-exponent-extraction/derivation_packet.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all prior reports and reviews`
- `all sibling Round-91 reports`
- `all source cards and web sources`

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
- `downstream_scope`

## Required deliverables

- Exactly seven numbered report sections.
- An exact region proof, end-to-end implication ledger, and sharp verdict.
- Write only rounds/codex-managed/gc-unconditional-exponent-extraction/reports/blind_global_exponent_rederivation.md.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
