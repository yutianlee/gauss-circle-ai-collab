# Task Brief: blind_m1_capacity_rederivation

- Campaign: `m9-m1-capacity-self-return-fork`
- Research round: `90` (`m9_m1_capacity_self_return_fork`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `bd5eed1e732c8872b37c0ea51bc9cea65419fe3241c17a981df3c2a36cd2c0f1`
- Generated: `2026-08-17T00:02:41.284804+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the complete surviving first-band M1 actual-symbol operator self-return at equal capacity to the Round-82 coherent nonzero-offset correlation, or is there a first non-returning signed degree of freedom with a strict power gain?

## Reference formula and distinctions

For Cap_M1(E)=X^epsilon D B^3 Delta T^4 Q^(-5/6) and Gamma_M1=Delta B^4 J^(-11/15), prove literal equal-capacity self-return of the complete R82--R89 reassembly, or isolate an exact residual with Gamma=o(J^(1/6)) at B=J^(3/20).

- J=X^(1/2), Q=J^(2/5), T=J^(3/5), B=C/T
- J^(13/18)<C<=J^(3/4), M asymp B
- normalized row size TQ^(-5/24); four-row energy factor Q^(-5/6)
- target X^epsilon(D/B)J^(14/5)
- strict support D1<|d|<Delta_b-J^(3/4), R_*>rho_*
- top full-degree gap Gamma=J^(1/6)

## Assigned target

Independently derive the capacity ledger and test whether the frozen statement proves equal-capacity self-return, a strict non-return, or exposes a named underdetermined seam.

## Permitted context

- `rounds/codex-managed/m9-m1-capacity-self-return-fork/derivation_packet.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all prior reports and reviews`
- `all sibling Round-90 reports`
- `all source cards and web sources`

## Required controls

- `capacity_ledger`
- `Q_power_normalization`
- `complete_cell_reassembly`
- `completed_descent_inverse_transform`
- `global_diagonal_one_count`
- `prior_package_ownership`
- `all_class_sign_modulus_multiple`
- `actual_stationary_symbol_support`
- `top_J_one_sixth_control`
- `literal_self_return_or_strict_nonreturn`
- `downstream_scope`

## Required deliverables

- Exactly seven numbered report sections.
- A capacity table and a sharp verdict.
- Write only rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/blind_m1_capacity_rederivation.md.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
