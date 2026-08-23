# Task Brief: literal_alias_local_energy_attack

- Campaign: `m9-m2-balanced-nonzero-alias-defect-gate`
- Research round: `116` (`m9_m2_balanced_nonzero_alias_defect_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `6421d27cb531be922b11ec48b51002ba568f235d510d16ac28a7d84881d66dad`
- Generated: `2026-08-21T14:28:28.995602+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 98%.
- Numerical/experimental effort: at most 2%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the Round-115 zero-subtracted double-far remainder admit an explicit joint signed half-shifted-alias or local-energy inequality of total cost O(L^3 X^epsilon), after retaining the literal gcd masks, slanted symbols, determinant projector, full shift family, and fixed physical block; or can the proposed one-alias defect mechanism be rigorously parked with its smallest surviving kernel named?

## Reference formula and distinctions

R_B^osc=sum_df a_B^<(h,k) conjugate(a_B^<(h',k')) [e(R(sqrt(hk)-sqrt(h'k')))-1], with R=sqrt X asymp L^3, h,k,h',k' asymp L, |h'k'-hk|>L, and |hk'-h'k|>L. In increments h'=h+2s and k'=k+q the character is e(s/2). For the oscillatory summand, formal Poisson in s has positive half-integer alias lambda=1/2-m, stationary point x=h'=X(k+q)/lambda^2, dual phase R sqrt(hk)-X(k+q)/(2lambda)-lambda h/2. With lambda_0=R sqrt(k/h), this equals -h(lambda-lambda_0)^2/(2lambda)-Xq/(2lambda). The round must make this formal chart literal, price its errors and norms, and determine whether it yields the missing factor L.

- X>=4096 real, R=sqrt X, persistent j=1, L asymp R^(1/3), and 1<=K/L<=16
- one fixed physical block B with the exact Round-113 real slanted symbol, floors, tapers, stars, crossings, and support
- a_B^<(h,k)=chi_4(h) eta(gcd(h,k)/(sqrt L/2)) A_B(h,k)
- double-far gates |Delta|=|h'k'-hk|>L and |rho|=|hk'-h'k|>L
- capacity_before L^4, claimed_gain one factor L, target and survivor capacity L^3
- the phase-free term is already owned and may be subtracted exactly once
- no residuewise, shiftwise, divisorwise, aliaswise, or shellwise absolute value may be hidden
- any stationary-phase or Poisson formula must retain boundary, gcd-expansion, gate-crossing, and nonstationary errors

## Assigned target

Make the conductor half-shift alias defect chart literal and use it to prove the strongest signed local-energy or reciprocal-frequency large-sieve estimate available at the exact L^3 budget, or isolate the first irreducible alias norm.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md`
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reviews/conductor_round115_identity_and_zero_mode.md`
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/derivation_packet.md`
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/candidates/conductor_half_shift_alias_defect.md`

## Required controls

- `literal_half_shift_poisson_legality`
- `gcd_expansion_and_character_progressions`
- `stationary_alias_range_and_amplitude`
- `dual_phase_square_completion`
- `radial_and_determinant_gate_images`
- `reciprocal_q_frequency_resonance_count`
- `signed_alias_norm_without_l1`
- `large_sieve_spacing_and_diagonal_cost`
- `boundary_and_nonstationary_errors`
- `actual_symbol_vs_arbitrary_coefficients`
- `fixed_block_and_owner_scope`
- `critical_j1_and_exact_square_j2_boundary`
- `external_theorem_hypothesis_fit`
- `linear_vs_energy_capacity`
- `downstream_scope`

## Required deliverables

- A seven-section discovery report.
- A literal transformed kernel with every amplitude, alias range, and error priced.
- The best proved target, subrange, saving, or precisely named survivor.
- A precise state recommendation.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
