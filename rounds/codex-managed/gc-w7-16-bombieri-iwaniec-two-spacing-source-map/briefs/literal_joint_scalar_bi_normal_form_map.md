# Task Brief: literal_joint_scalar_bi_normal_form_map

- Campaign: `gc-w7-16-bombieri-iwaniec-two-spacing-source-map`
- Research round: `133` (`gc_w7_16_bombieri_iwaniec_two_spacing_source_map`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `465093c00a388ff9e49583a8016e0e580f74beea4656b15884fdd9dc9247be5a`
- Generated: `2026-08-23T12:08:23.736910+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact Li--Yang/Bombieri--Iwaniec standard sum, double-large-sieve inequality, and first/second-spacing machinery be mapped without changing coefficient ownership or absolute-value placement to the literal Round-131 top-shell determinant correlation and produce a complete fixed-block exponent below 27/48; if not, what is the first exact source or normal-form mismatch?

## Reference formula and distinctions

Estimate the literal fixed-centre scalar O_(i,D)^+(c)=sum_(r=(a,b))^lit A_i(r) sum_(r'=(a',b'))^lit B_i(r,r') e(ca/(kappa_i b)-ca'/(kappa_i b')), with n=ab'-a'b>0, the taper 1-Wn/(kappa_i bb'), kappa_1=1 and kappa_2=4, and every primitive lift, threshold, Stieltjes/Mobius profile, quarter or chi_4 carrier, reciprocal alias, taper, star, cell, sign, and owner retained. The candidate single-wave phase map is h=a, m=b, H_LY=L, M_LY=D, T_LY=c/kappa_i, F(z)=1/z; this map must be checked rather than assumed to extend to the joint correlation.

- project scales W=Y^(7/16), D=Y^(1/2), L=Y^(1/6), c asymp Y, |a| and |a'| asymp L, b and b' asymp D
- 0<n=ab'-a'b lesssim kappa_i bb'/W, fixed-outer bounded determinant-lift multiplicity, complete capacity Y^(35/48+epsilon)
- ideal one-term-per-ray persistence threshold Y^(27/48+epsilon), determinant target Y^(24/48+epsilon)
- candidate Li--Yang parameters H_LY=Y^(1/6), M_LY=Y^(1/2), T_LY=Y, so H_LY/M_LY=T_LY^(-1/3)
- source derivative approximants a_BI/r_BI and project primitive rays (a,b) are different variable roles until an exact bijection is proved

## Assigned target

Starting from the literal Round-131 scalar and accepted Round-132 chart, verify the exact single-wave Li--Yang phase map and then derive or refute a complete owner-preserving map of the joint determinant correlation to Li--Yang S or the underlying double-large-sieve/two-spacing normal form. Compute every source parameter, spacing coordinate, coefficient norm, owner cost, and resulting Y exponent.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0823_full_proof_strategy.md`
- `sources/li_yang_2023.md`
- `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`
- `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/synthesis.md`
- `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/reports/literal_induced_residue_weight_derivation.md`
- `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/synthesis.md`
- `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/reviews/conductor_round132_hyperbolic_decoupling_adjudication.md`

## Required controls

- `single_wave_phase_and_derivative_map`
- `source_parameter_power_ledger`
- `project_ray_vs_derivative_approximant_roles`
- `joint_coefficient_BV_projective_norm_and_absolute_value_direction`
- `major_minor_arc_and_short_interval_ownership`
- `first_spacing_vector_and_norm`
- `second_spacing_four_coordinates_and_modular_inverses`
- `same_denominator_M1_M2_aligned_packets`
- `S_over_H_to_Y_capacity`
- `capacity_35_27_24_over_48`
- `no_positive_energy_or_global_promotion`

## Required deliverables

- A seven-section analytic report.
- An exact project-to-source variable, phase, coefficient, spacing, and exponent table.
- A legal applicable stratum with complete margin, one exact missing hypothesis, or a source-level no-go.
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
