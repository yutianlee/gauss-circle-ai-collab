# Task Brief: large_values_primary_source_audit

- Campaign: `gc-complete-large-values-duality`
- Research round: `204` (`complete_large_values_analytic_attack`)
- Role: `source_auditor`
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

Audit primary sources for this specific complete large-values attempt. Check Bourgain2017 global Theorem6 on f(n)=u sqrt(n), its derivative class, proper intervals and all source parameter ranges; compare interpolation with the elementary second derivative estimate and the proposed exponent13/55. Independently audit the original circle large-values/moment trail (Ivic1990, published Tsang-Zhai q0 benchmark, or directly accessible primary proof) for whether q0=262/27 is fixed by an older pointwise exponent and exactly what an update would require. Prioritize at most two full primary proofs. Do not guess a new endpoint. Report applicability, exact theorem locations and costs, including negative conclusions. Seven sections, write only report and stop.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round204_complete_large_values_attack.md`
- `rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md`
- `sources/bourgain_2017_exponent_pair.md`
- `rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/reports/circle_moment_primary_source_audit.md`
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
