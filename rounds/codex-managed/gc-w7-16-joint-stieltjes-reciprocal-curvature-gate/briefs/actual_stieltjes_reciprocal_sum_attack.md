# Task Brief: actual_stieltjes_reciprocal_sum_attack

- Campaign: `gc-w7-16-joint-stieltjes-reciprocal-curvature-gate`
- Research round: `129` (`gc_w7_16_joint_stieltjes_reciprocal_curvature_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `476b1445ef73d86627fd87de8bd2dd76a5efa53564a5b195230f2ad33ba2bbe8`
- Generated: `2026-08-23T05:33:38.626058+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For the exact character-split M1/M2 Stieltjes lift packages proved in Round 128, does the joint V2-weighted reciprocal-curvature inequality hold uniformly without an extra N_rho^(1/2), or is there a literal structured counterterm that stops the graded route?

## Reference formula and distinctions

U_(i,rho,eta)(v)=tau_i(v) sum_t c_t a'^(-1) sum_(g<=t/(rho v)) chi_4(g)g^(-1)P_(i,a')(g), with sum_t|c_t|<<1 and branch phase f(v)=-ca'/(kappa_i rho v)+vartheta_(i,eta)rho v. Test |sum_(v in I)^* U(v)e(f(v))| <<_epsilon ||U||_(V2(I)) min(N_rho,N_rho sqrt(lambda_B rho^2)+(lambda_B rho^2)^(-1/2))Y^epsilon.

- W=Y^(7/16), D=Y^(1/2), L=Y^(1/6), D/L<=B<=D
- Q_B=min(B,BD/(WL)), J_B=1+DQ_B/B^2, N_rho asymp Q_B/rho
- lambda_B=YL/(DB^2), b'=rho v, |a'| asymp LB/D, rho divides a'
- vartheta_(1,+)=1/4, vartheta_(1,-)=-1/4, vartheta_(2,0)=0
- The coefficient norm ||U||_(V2)<<J_B^(1/2)/L is already proved and must not be reproved as the oscillatory theorem
- Generic V2 partial summation loses N_rho^(1/2); a valid proof must exploit the actual threshold/character/reciprocal coupling
- Success gives only conditional complete-block Y^(73/96), whose persistence exponent 115/288 is worse than one third

## Assigned target

Attack the exact branchwise M1/M2 reciprocal sum after Stieltjes decomposition. Obtain the desired joint inequality, a strict shell theorem with the first residual, or a literal counterterm, without separating the lift character from the reciprocal variable.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/actual_rational_cluster_attack.md`
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reports/actual_character_determinant_attack.md`
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md`
- `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reports/literal_lift_coefficient_variation_attack.md`
- `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reviews/conductor_round128_literal_v2_adjudication.md`
- `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/synthesis.md`

## Required controls

- `branchwise_literal_dictionary`
- `single_threshold_birth_phase`
- `character_before_modulus`
- `M1_quarter_phase_aliases`
- `reciprocal_second_derivative_and_stationary_lattice`
- `threshold_superposition_and_Minkowski`
- `V2_endpoint_terms`
- `mobius_progressions`
- `floors_stars_taper_and_shell_owners`
- `N_rho_square_root_stop_rule`
- `theta_two_thirds_capacity_threshold`
- `no_exponent_or_M9_promotion`

## Required deliverables

- A seven-section analytic report.
- An exact sum formula before every norm and a shell-by-shell capacity ledger.
- A full proof, strict partial theorem plus exact residual, or literal structured no-go.
- No graph or shared-state edit.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
