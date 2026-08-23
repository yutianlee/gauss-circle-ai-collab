# Task Brief: blind_structured_v2_curvature_feasibility

- Campaign: `gc-w7-16-joint-stieltjes-reciprocal-curvature-gate`
- Research round: `129` (`gc_w7_16_joint_stieltjes_reciprocal_curvature_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
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

Determine whether the displayed V2-weighted reciprocal-curvature inequality is valid for the exact abstract Stieltjes-character threshold class. Prove it, give a structured counterexample, or isolate a sharp additional hypothesis, while separately deriving the generic V2 dual obstruction.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-95 through Round-129 nonblind artifacts`
- `all Round-129 sibling reports`

## Required controls

- `generic_V2_dual_countermodel`
- `single_threshold_birth_phase`
- `character_before_modulus`
- `M1_quarter_phase_aliases`
- `reciprocal_second_derivative_and_stationary_lattice`
- `threshold_superposition_and_Minkowski`
- `V2_endpoint_terms`
- `actual_vs_phase_adapted_coefficients`
- `N_rho_square_root_stop_rule`
- `theta_two_thirds_capacity_threshold`
- `no_exponent_or_M9_promotion`

## Required deliverables

- A seven-section statement-only report.
- An exact dual-norm calculation for generic V2 amplitudes.
- A proof, structured counterexample, or minimal repaired theorem for the supplied threshold class.
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
