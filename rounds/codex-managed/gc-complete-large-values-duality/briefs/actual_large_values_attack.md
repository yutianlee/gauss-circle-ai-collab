# Task Brief: actual_large_values_attack

- Campaign: `gc-complete-large-values-duality`
- Research round: `204` (`complete_large_values_analytic_attack`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`
- Generated: `2026-09-23T13:36:13.138408+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can actual finite-vector large-values analysis prove the complete high-value distribution required by the twelfth-moment target?

## Reference formula and distinctions

D_T(V)<<T^(29/25+epsilon)V^(-12) for T^(54/775)<=V<=T^(beta+epsilon), beta=2theta_LY-1/2

- Exact actual B_T and window in frozen strategy.
- Candidate weaker envelope T^epsilon(V^-2+T V^(-136/13)) must be proved, not assumed.
- Keep the complete diagonal, all localization intervals and upper tails; a generic aligned counterexample is not an arithmetic counterexample.

## Assigned target

Attack the frozen full actual large-value distribution using finite-vector duality and localized Gram matrices. Prove or refute the candidate D(V)<<T^epsilon(V^-2+T V^(-136/13)) by deriving the correlation interpolation from the accepted source card plus elementary derivatives, all small-u regimes, real level-set covering and full dyadic/tail recombination. Preserve all diagonal and ceiling terms. Then attempt the coefficient-sensitive improvement needed to reach the frozen target; identify exactly why any generic bound falls short. Derive the best complete moment consequence with the accepted pointwise exponent only after pricing its exact smoothing interface; do not just substitute into a printed endpoint. Seven sections and stop.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round204_complete_large_values_attack.md`
- `rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md`
- `sources/bourgain_2017_exponent_pair.md`
- `rounds/codex-managed/gc-complete-signed-convolution-attack/reports/arithmetic_signed_tail_attack.md`
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md`

## Required controls

- `actual_coefficients`
- `complete_distribution`
- `full_diagonal_and_ceiling`
- `source_hypotheses`
- `all_tails_and_ranges`
- `real_uniformity`
- `net_moment_and_pointwise_powers`
- `independent_statement_only_control`
- `no_parent_overclaim`

## Required deliverables

- Seven-section report: result, exact hypotheses, proof, first gap, controls, dependencies, state effect.
- Write only assigned report; no graph/draft/matrix/synthesis/source-card/successor edits.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
