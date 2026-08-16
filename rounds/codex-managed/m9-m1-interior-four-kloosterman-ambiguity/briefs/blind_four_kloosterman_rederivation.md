# Task Brief: blind_four_kloosterman_rederivation

- Campaign: `m9-m1-interior-four-kloosterman-ambiguity`
- Research round: `86` (`m9_m1_interior_four_kloosterman_ambiguity`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `910950f389c49a17cc188c8e0ad9b18e4d83d4a7f580fa0baacca97d39195fe6`
- Generated: `2026-08-16T14:46:01.215141+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact continuously twisted physical-row ambiguity or the literal d-A-process four-Kloosterman off-diagonal bound the remaining M1 interior differences while retaining Q^(-5/12)?

## Reference formula and distinctions

Bound M^(-2) sum_(b asymp B) sum_(D0<|d|<Delta_b-E*) sum_n (S(n+d,K;M)conj(S(n,K;M))-c_M(d)) I_b(n+d)conj(I_b(n)) by X^epsilon J^2/T, or isolate a strictly smaller exact signed survivor.

- J=X^(1/2), Q=J^(2/5), T=J^(3/5), B=C/T
- J^(13/18)<C<=J^(3/4)
- D0=floor(J^(17/30)), E*=floor(Q^2J^(-1/20))=floor(J^(3/4))
- Delta_b asymp Q^2 and D0<|d|<Delta_b-E*
- physical row TQ^(-5/24), energy factor Q^(-5/12)
- B^(-1/2) reaches C=J^(56/75); B^(-5/9) closes the endpoint

## Assigned target

Independently derive the exact ambiguity and d-A-process interfaces and test whether any retained cancellation proves a B-power or a smaller middle survivor.

## Permitted context

- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/derivation_packet.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all prior-round reports and reviews`
- `all sibling Round-86 reports`
- `all source cards and web sources`

## Required controls

- `external_normalization`
- `all_class_local_units`
- `physical_row_energy_factor`
- `middle_difference_ownership`
- `negative_and_modulus_multiple_differences`
- `ramanujan_cross_and_square_terms`
- `prime_power_gcd_modes`
- `fejer_prefactor_and_diagonal`
- `four_kloosterman_offdiagonal`
- `actual_stationary_symbol`
- `entry_exit_and_error_ownership`
- `integer_and_perfect_power_resonance`
- `complete_transform_and_uM_self_return`
- `downstream_scope`

## Required deliverables

- One seven-section statement-only report at the assigned path.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
