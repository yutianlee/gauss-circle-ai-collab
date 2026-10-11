# Task Brief: arithmetic_signed_tail_attack

- Campaign: `gc-complete-signed-convolution-attack`
- Research round: `203` (`complete_signed_analytic_attack`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`
- Generated: `2026-09-23T13:10:41.565447+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can a complete coefficient-sensitive density or arithmetic estimate prove the actual signed filtered-convolution target with its full remainder?

## Reference formula and distinctions

||K_T*mu_(T,>floor(T^(1/2047)))^{*6}||_2 << T^(29/50+epsilon)

- Exact definitions in strategy/round203_complete_signed_convolution_attack.md.
- Target gives only intermediate102/325; quarter theorem remains full goal.
- All infinite tails, both cosine signs and sixfold/twelfth cross terms are retained.

## Assigned target

Attack the full actual signed tail twelfth moment using r_2(n)=4 sum_(d|n)chi_4(d) or radial lattice Poisson/stationary phase. Choose a concrete complete arithmetic approach and push its estimates to their quantitative limit. Preserve chi_4 and all weights, frequency signs, dyadic recombination, errors, endpoints and infinite tail. A transform alone is not a result: show a saving or explicitly derive the net loss/self-return and the first new inequality needed. Do not subdivide indefinitely or discuss unrelated external methods. Seven sections and stop.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round203_complete_signed_convolution_attack.md`
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/candidates/conductor_signed_convolution_interface.md`
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md`

## Required controls

- `actual_coefficients`
- `complete_tail_and_cross_terms`
- `signed_filter_preserved`
- `all_errors_priced`
- `real_uniformity`
- `net_exponent`
- `independent_statement_only_control`
- `no_parent_overclaim`

## Required deliverables

- Seven-section report with exact result, hypotheses, derivation, first gap, controls, dependencies, state effect.
- Write only assigned report. No graph, draft, matrix, synthesis, source cards or successor work.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
