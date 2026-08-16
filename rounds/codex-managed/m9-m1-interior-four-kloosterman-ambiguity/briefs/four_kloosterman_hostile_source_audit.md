# Task Brief: four_kloosterman_hostile_source_audit

- Campaign: `m9-m1-interior-four-kloosterman-ambiguity`
- Research round: `86` (`m9_m1_interior_four_kloosterman_ambiguity`)
- Role: `source_auditor`
- Access mode: `selected_context`
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

Falsify or certify a literal weighted four-Kloosterman/ambiguity estimate and audit current primary-source applicability for arbitrary composite and prime-power moduli.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/derivation_packet.md`
- `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/synthesis.md`
- `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reports/large_difference_source_hostile_audit.md`
- `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/kloosterman_energy_source_hostile_audit.md`
- `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reports/offset_trace_source_hostile_audit.md`

## Excluded context

- `all sibling Round-86 reports`

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
- `source_hypothesis_map`
- `downstream_scope`

## Required deliverables

- One seven-section hostile/source report at the assigned path.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
