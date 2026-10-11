# Task Brief: complete_factor_norm_audit

- Campaign: `gc-complete-logarithmic-convolution`
- Research round: `225` (`complete_circle_logarithmic_convolution`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`
- Generated: `2026-09-27T22:28:30.221932+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 95%.
- Numerical/experimental effort: at most 5%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact logarithmic convolution and finite prime-factor decomposition yield a complete uniform bound for the actual circle wave better than the inherited beta, ultimately at T^epsilon?

## Reference formula and distinctions

sup_(R in [cT,CT]) |sum_(n>=1) r2(n)n^(-3/4)Psi(sqrt(n/T)) cos(2pi R sqrt(n)-3pi/4)| << T^epsilon.

- Fixed accepted mollifier Psi, every real T and R, n=1, all dyadic scales and complete infinite Schwartz tail.
- f=1*chi4=r2/4; f log=f*((1+chi4)Lambda); literal Vaughan cutoffs U,V and both branches with every prime power.
- Actual character/Mobius/divisor vectors and nonlinear phase R sqrt(product), product masks, all norms and both real signs.
- Complete inherited real exponent beta=2theta_LY-1/2; a complex bound is stronger and is not inherited.
- P(R^2)=sqrt(R)/pi B_T(R)+O(T^(1/2+epsilon)); target suffices for full quarter, intermediate gamma gives 1/4+gamma/2.
- Independent M1/M2/GAR and moment owners remain until a validated complete theorem discharges the target.

## Assigned target

Independently derive and quantitatively test the COMPLETE logarithmic-convolution/Vaughan decomposition of the actual real circle wave in the conductor packet. Audit all f/chi4/Mobius/Lambda factors, short and long ranges, their actual l1/l2 norms, literal cutoff masks, logs, repeated prime powers, real-R uniformity, singleton and full Schwartz tail. Attempt a full nonlinear Type-I/Type-II estimate; if norms are used give the exact resulting exponent and compare to inherited beta. Identify actual signed arithmetic information lost in each closure; any adverse generic vector is not an arithmetic counterexample. All remaining terms must be bounded or explicitly left in the one complete missing inequality; do not create a chain of local survivors. The accepted unweighted exponent-pair kernel may be used only on a legal unweighted interval, with remaining norms restored. One narrow primary theorem audit is permitted if essential and coordinated with conductor; otherwise none. Seven sections, zero experiments. No current sibling/blind packet, shared edits or successor. Assigned report only; stop at final hash.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round225_complete_circle_logarithmic_convolution.md`
- `rounds/codex-managed/gc-complete-logarithmic-convolution/briefs/conductor_complete_circle_wave.md`
- `strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md`
- `rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md`
- `rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md`
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`
- `sources/bourgain_2017_exponent_pair.md`
- `rounds/codex-managed/gc-full-goal-signed-source-review/synthesis.md`

## Required controls

- `complete_actual_circle_wave`
- `logarithmic_identity`
- `both_character_branches`
- `literal_vaughan_cutoffs`
- `prime_powers_and_two`
- `singleton_log_division`
- `actual_product_norms`
- `all_type_i_ii_ranges`
- `real_radius_uniformity`
- `cosine_and_complex_scope`
- `schwartz_tail_and_mixed_scales`
- `physical_sharp_reconstruction`
- `statement_only_derivation`
- `actual_vs_generic_control`
- `source_hypotheses_if_used`
- `full_goal_scope`

## Required deliverables

- Seven numbered protocol sections: result, exact hypotheses, proof/derivation, first gap, controls, dependencies/provenance, state effect.
- Assigned report only, no shared edits, sibling access or successor; stop at final SHA256.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
