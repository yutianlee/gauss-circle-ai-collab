# Task Brief: rational_energy_source_audit

- Campaign: `m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate`
- Research round: `149` (`m9_m1_lower_cone_t1_squarefree_gcd_lift_energy_gate`)
- Role: `source_auditor`
- Access mode: `selected_context`
- Graph SHA-256: `8f1912eeda4843718379213478a839b30fb2694d6b169ac8decbab5ca3561176`
- Generated: `2026-08-24T11:59:34.439266+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

After summing the Round-148 Mobius cells with the same lcm and then every gcd lift with the same reduced fraction ell/q=L/q_0, does the exact compressed coefficient satisfy a uniform square norm and does its complete joint d-energy satisfy E_U<<R^2 D X^epsilon, thereby proving |T|<<RD X^epsilon; if not, what is the first exact cutoff, d-dependence, alignment, near-collision, source-hypothesis, boundary, or all-scale obstruction?

## Reference formula and distinctions

Let C_d(n)=sum_{b|d,[alpha^2,b]=n}mu(alpha)mu(b), with odd squarefree alpha,b and the exact nonempty-progression indicator kappa_(d,U)(n). For ell=gL, q=gq_0, (L,q_0)=1, define B_(d,U)(L)=sum_g C_d(gL)kappa_(d,U)(gL)/g. The candidate exact row is G_U(d)=sum_((L,q_0)=1) chi_4(Lq_0)B_(d,U)(L)W_(d,U)(L/q_0)e(NdL/q_0)/L, supported on q_0 asymp LQ, and T=sum_d mu^2(d)(D/d)G_U(d). The target follows from sum_d mu^2(d)|G_U(d)|^2<<R^2 D X^epsilon.

- For d_o=d/(d,2), prove locally that C_d(n)=mu(u)mu(v) for n=uv^2, odd u|d_o, odd u,v with mu^2(uv)=1, and (v,d)=1, and is zero otherwise; the odd p|d_o, p^2|n cancellation is compulsory and p=2 is absent from the lcm ledger.
- The exact prefix indicator kappa_(d,U)(n) is finite and may be irregular near the endpoint. No continuous cutoff may silently replace it.
- The chi_4 factors of the common odd gcd lift cancel as chi_4(g)^2=1, while the phase and saddle profile depend only on L/q_0. Every other g-dependence must be displayed.
- Test the uniform truncated-lift norm sum_L |B_(d,U)(L)|^2/L<<X^epsilon before invoking the joint energy.
- The literal equal-cell diagonal should cost DQX^epsilon and is target-safe because Q<=R^2; prove this with the actual d-dependent coefficient.
- The off-diagonal must retain Delta=L_1q_(0,2)-L_2q_(0,1), the congruence NDelta=0 mod q_(0,1)q_(0,2), near alignments, common divisors, and imprimitive reductions.
- A classical large sieve with d-independent coefficients does not apply verbatim to B_(d,U)(L)W_(d,U)(L/q_0).
- Audit D=1, L=1, q_0|N, odd primes dividing d_o, even squarefree d, small reduced denominators, balanced and extreme aspects, short prefixes, and every M<=R^2.
- The Round-147 H correlation is an alternative only after exact Euler recombination; no termwise lcm-to-powerful-index map is allowed.
- Every t>=2 layer and the independent Round-138 cross owner remain separate.

## Assigned target

Audit primary rational large-sieve, Farey-spacing, additive squarefree-correlation, Kloosterman-fraction, and dispersion results against the exact compressed Round-149 energy. Supply a theorem with complete power translation or the first exact coefficient-dependence, spacing, denominator, averaging, diagonal, smoothness, prefix, or all-scale mismatch.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round149_gcd_lift_energy_strategy.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/barrier_packet.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/squarefree_progression_source_audit.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/source_conductor_round148_final.md`
- `rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/reports/conductor_signed_reciprocal_energy_analysis.md`
- `rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/reports/conductor_RSLS_source_hostile_audit.md`
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/candidates/conductor_round138_scalar_rows_and_resonance_fibres.md`
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/candidates/conductor_round139_curvature_collar_and_quadratic_obstruction.md`

## Required controls

- `exact_progression_coefficient_collapse`
- `gcd_lift_character_phase_profile_recombination`
- `truncated_lift_square_norm`
- `joint_d_energy_target_normalization`
- `literal_equal_cell_diagonal`
- `offdiagonal_determinant_and_near_collision`
- `N_dependent_exact_alignments`
- `common_divisor_and_imprimitive_denominator`
- `d_dependent_arithmetic_coefficient`
- `source_theorem_energy_match`
- `all_M_D_E_Q_power_ledger`
- `D1_L1_qdividesN_prime_and_prefix_controls`
- `H_interface_and_transform_self_return`
- `Round138_cross_tge2_and_downstream_scope`

## Required deliverables

- A seven-section primary-source audit.
- Exact theorem cards with coefficient, spacing, denominator, averaging, diagonal, smoothness, and translated R-M-D-E-Q hypotheses.
- A source-legal target theorem or the first precise source and power obstruction.
- Write only the assigned report and make no graph or shared-state edit.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
