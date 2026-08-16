# Task Brief: aligned_mode_aggregate_attack

- Campaign: `m9-m1-deep-exceptional-strata-dispersion`
- Research round: `87` (`m9_m1_deep_exceptional_strata_dispersion`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `909b828c22ae9db75aabae375794d288259429d742c2b5f5fffcb0a97b84e167`
- Generated: `2026-08-16T15:22:28.923649+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the divisor-aligned and prime-power exceptional strata in the deep M1 four-Kloosterman ambiguity be summed target-safely against the actual stationary symbol, leaving a quantitatively controllable generic remainder?

## Reference formula and distinctions

Bound M^(-2) sum_(b asymp B) sum_(D1<|d|<Delta_b-E*) sum_n (S(n+d,K;M)conj(S(n,K;M))-c_M(d)) I_b(n+d)conj(I_b(n)) by X^epsilon J^2/T, or isolate a strictly smaller exact signed survivor after exceptional-stratum extraction.

- J=X^(1/2), Q=J^(2/5), T=J^(3/5), B=C/T
- J^(13/18)<C<=J^(3/4)
- D1=floor(J^(87/140)), E*=floor(Q^2J^(-1/20))
- D1<|d|<Delta_b-E*, Delta_b asymp Q^2
- physical row TQ^(-5/24), energy factor Q^(-5/12)
- exact exceptional branches h1=h2=0 locally or v=0,h1=h2 locally, with u divisible by the same local factor

## Assigned target

Derive an exact p-adic/CRT exceptional-strata decomposition and exploit the actual stationary phase to prove its aggregate target-safe or isolate a smaller signed survivor.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0816_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/derivation_packet.md`
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/synthesis.md`
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reports/twisted_ambiguity_attack.md`
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_cubic_shell_normalization.md`
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_rational_completion.md`

## Excluded context

- `all sibling Round-87 reports`

## Required controls

- `external_normalization`
- `all_class_local_units`
- `physical_row_energy_factor`
- `deep_difference_ownership`
- `negative_and_modulus_multiple_differences`
- `ramanujan_cross_and_square_terms`
- `prime_power_and_2adic_strata`
- `squarefree_divisor_aligned_modes`
- `fejer_prefactor_and_diagonal`
- `actual_fourfold_stationary_symbol`
- `generic_trace_remainder`
- `entry_exit_and_error_ownership`
- `integer_and_perfect_power_resonance`
- `complete_transform_self_return`
- `downstream_scope`

## Required deliverables

- One seven-section analytic report at the assigned path.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
