# Task brief: blind_inverse_congruence_interface_audit

- Campaign: `m9-m2-unbalanced-kloosterman-dispersion-source-map`
- Round: 135
- Role: blind statement-only rederiver
- Graph SHA-256: `f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`
- Evidence status: candidate only; do not edit shared state.
- Allocation: 100% analytical/algebraic work, 0% numerical experimentation.

## Isolation

Read only:

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/blind_statement.md`

Do not read the proof graph, proof draft, strategies, Rounds 107--135
nonblind artifacts, sibling reports, or conductor notes.

## Objective

Independently determine whether the supplied ordinary-fraction wave admits
an exact coefficient-independent inverse-phase or fixed-residue dispersion
interface covered by the two supplied theorems and strong enough for the
quarter target. Derive the map and exponent if it exists. Otherwise identify
the first exact missing equality or hypothesis and the smallest remaining
signed survivor.

Test direct `m=1`, modular-inverse reindexing, completion, moving-profile
separation, real-centre integrality, divisibility/coprimality, fixed-centre
versus modulus averaging, and the full exponent region. Do not turn a
coefficient adversary into a lower bound for the literal array.

## Output contract

Write only
`rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md`.
Use exactly seven numbered sections:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

Recommend one of `promote`, `retain`, `revise`, `reject`, or `no change`.
Do not edit any other file.
