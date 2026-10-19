# Task Brief: signed_connected_attack

- Campaign: `gc-connected-cumulant-test`
- Research round: `234` (`bounded_actual_connected_correlation_test`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306`
- Generated: `2026-10-12T00:32:49.020996+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 95%.
- Numerical/experimental effort: at most 5%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does subtracting all disconnected lower correlations yield a quantitatively useful actual signed connected12 estimate at29/25? Test the stronger absolute-cluster mechanism against full-harmonic controls and pay the signed remainder.

## Reference formula and distinctions

I12=K12+D12; seek D12<<T^(1+eps), K12<=T^(29/25+eps); test C_conn at29/25 rather than assume it.

- p=12 fixed, Q=floor(T^(2/5)), probability weight w/(TW), all harmonics and signs.
- New complete gain requires signed K12 bound, not just paid D12.
- No automatic all-order estimate or third old upper-tail packet attempt.

## Assigned target

Attempt the actual signed connected aggregate. Prove or refute D12<<T^(1+epsilon) using precise mixed-radius collision algebra and lower actual moments, paying singleton/pair partitions and infinite tails. Then seek a genuinely quantitative bound on K12; state the exact first gap if unavailable. Give complete conditional restoration and controls. Do not read sibling reports.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/gc-connected-cumulant-test/briefs/actual_interface.md`
- `proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md`
- `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`

## Required controls

- `probability_normalization`
- `actual_full_harmonics`
- `rapid_single_pair`
- `signed_collision_sum`
- `connected_absolute_control`
- `complete_budget`
- `no_signed_lower_bound`
- `wolfram_local_exact`
- `blind_isolation`
- `history_preservation`

## Required deliverables

- Seven protocol sections, exact context hashes, proof or first gap, controls and state recommendation.
- Write only assigned report, hash and stop; no successor.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.

Write ONLY `rounds/codex-managed/gc-connected-cumulant-test/reports/signed_connected_attack.md`. Freeze and stop.
