# Task Brief: blind_collision_bound

- Campaign: `gc-connected-cumulant-test`
- Research round: `234` (`bounded_actual_connected_correlation_test`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
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

Solve only isolated_collision.md. About10 minutes; provide independent proof or counterexample, uniformity and domination, exact control, then freeze and stop.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/gc-connected-cumulant-test/briefs/isolated_collision.md`

## Excluded context

- `All except protocol.md, isolated_collision.md and own brief; no graph, application or sibling.`

## Required controls

- `signed_collision_sum`
- `blind_isolation`

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

Write ONLY `rounds/codex-managed/gc-connected-cumulant-test/reports/blind_collision_bound.md`. Freeze and stop.
