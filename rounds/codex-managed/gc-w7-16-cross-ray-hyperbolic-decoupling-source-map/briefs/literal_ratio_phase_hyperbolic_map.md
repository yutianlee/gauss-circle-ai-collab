# Task Brief: literal_ratio_phase_hyperbolic_map

- Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`
- Research round: `132` (`gc_w7_16_cross_ray_hyperbolic_decoupling_source_map`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `328a885e71415a8e3509466c46849129248594334dc17df8940bbcd3f12a0fe9`
- Generated: `2026-08-23T11:35:30.658773+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can Demeter--Wu's bilinear ell^2 or refined bilinear decoupling for the hyperbolic paraboloid be mapped, without changing absolute-value placement or coefficient ownership, to the actual Round-131 variable-modulus top-shell scalar and give a complete exponent below 27/48; if not, what is the first exact missing hypothesis or source-level no-go?

## Reference formula and distinctions

Estimate the literal fixed-centre scalar O_{i,D}^+=sum_r^lit A_i(r) sum_{n>0}^lit W_{i,r}(n), equivalently the residual R_i^res(c)=sum_r^lit A_i(r)R_{i,r}^phys(c), where n=ab'-a'b, the phase is e(cn/(kappa_i b b'))=e(ca/(kappa_i b)-ca'/(kappa_i b')), kappa_1=1 and kappa_2=4, and every primitive lift, threshold, Stieltjes/Mobius coefficient, quarter carrier or chi_4 factor, reciprocal alias, taper, star, cell, sign, and owner is retained. No positive energy, arbitrary-coefficient operator norm, or averaged-centre quantity substitutes for this scalar.

- W=Y^(7/16), D=Y^(1/2), L=Y^(1/6), c asymp Y, |a| and |a'| asymp L, b and b' asymp D
- 0<n=ab'-a'b lesssim D^2/W=Y^(27/48), with O(1) literal p-lifts for fixed outer ray and n
- local phase Phi(u,v)=-cu/(kappa_i v) has det Hess Phi=-(c/(kappa_i v^2))^2 asymp -1 on the top shell
- outer coefficients satisfy sum_r |A_i(r)| lesssim D and sum_r |A_i(r)|^2 lesssim D/L
- capacity_before=D K_D=Y^(35/48+epsilon), K_D=Y^(11/48+o(1))
- ideal one-term-per-ray persistence threshold=D K_D/L=Y^(27/48+epsilon)=Y^(9/16+epsilon)
- determinant target=D=Y^(24/48+epsilon); after ideal per-ray collapse it still requires cross-ray Y^(-1/16)

## Assigned target

Starting from the exact Round-131 physical scalar, derive the literal phase-surface normalization and project parameter map into the Demeter--Wu framework. Compute R, cap scales, transversality, coefficient norms, broad/narrow pieces, fixed-centre localization losses, owner errors, and the final Y-capacity, or isolate the first exact mismatch.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0823_full_proof_strategy.md`
- `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/blind_statement.md`
- `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/synthesis.md`
- `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reviews/conductor_round131_residue_mode_adjudication.md`
- `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/literal_induced_residue_weight_derivation.md`
- `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/synthesis.md`

## Required controls

- `hyperbolic_surface_normalization`
- `transversality_in_both_coordinates`
- `Fourier_support_thickness_and_cap_scale`
- `fixed_centre_scalar_vs_bilinear_L4_integral`
- `actual_coefficient_norm_and_absolute_value_direction`
- `broad_narrow_ruling_partition`
- `same_denominator_M1_M2_aligned_packets`
- `variable_primitive_moduli_thresholds_and_owners`
- `capacity_35_27_24_over_48`
- `no_positive_energy_or_global_promotion`

## Required deliverables

- A seven-section analytic report.
- An exact coordinate, scale, cap, norm, and owner table from project variables to source variables.
- A priced applicable stratum, one exact missing hypothesis, or a source-level no-go.
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
