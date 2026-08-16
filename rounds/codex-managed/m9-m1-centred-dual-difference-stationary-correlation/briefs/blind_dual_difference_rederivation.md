# Task Brief: blind_dual_difference_rederivation

- Campaign: `m9-m1-centred-dual-difference-stationary-correlation`
- Research round: `84` (`m9_m1_centred_dual_difference_stationary_correlation`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `b744aa885442ec9be13913782471cf65a94cd794579f8c6a8fbb2854ce52e271`
- Generated: `2026-08-16T10:02:06.184651+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact stationary Fourier weights force any fixed B-power saving in the centred nonzero dual-difference Kloosterman-product correlation on J^(13/18)<C<=J^(3/4)?

## Reference formula and distinctions

For M in {4b,2b,b}, prove M^(-2) sum_(b asymp B) sum_(d!=0) sum_n (S(n+d,K;M)conj(S(n,K;M))-c_M(d)) I_b(n+d)conj(I_b(n)) << X^epsilon J^2/T, or isolate a strictly smaller exact signed survivor.

- J=X^(1/2), Q=J^(2/5), T=J^(3/5), B=C/T
- first residual band J^(13/18)<C<=J^(3/4)
- g_kappa M_kappa=4b and A_(kappa,b)=(sqrt(bX)+sqrt(kappa k/b))^2
- stationary n asymp Q^2
- exact critical phase (sqrt(X)+sqrt(kappa k)/b)sqrt(|n|)
- d=0 removed once; d!=0 with d=0 mod M retained
- delta=1/2 reaches C=J^(56/75); delta=5/9 closes the band

## Assigned target

Independently derive the complete stationary form of I_b(n), test signed cancellation across d!=0, and either prove a range gain or identify the first exact survivor without reading claimant or source material.

## Permitted context

- `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/derivation_packet.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all prior-round reports and reviews`
- `all sibling Round-84 reports`
- `all source cards and web sources`

## Required controls

- `external_normalization`
- `all_class_local_units`
- `poisson_measure`
- `stationary_sign_phase_gaussian`
- `saddle_support_and_tails`
- `d_zero_removed_once`
- `nonzero_modulus_multiples`
- `ramanujan_subtraction`
- `gcd_prime_power_modes`
- `actual_symbol_derivatives`
- `difference_range_and_edges`
- `progression_integer_resonance`
- `perfect_power_adversarial_controls`
- `complete_transform_self_return`
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
