# Task Brief: literal_lift_coefficient_variation_attack

- Campaign: `gc-w7-16-local-transverse-lift-variation-gate`
- Research round: `128` (`gc_w7_16_local_transverse_lift_variation_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `1a5c8c8b4b6c6c0dcf3d0e05a1607b3d29dfe22f66748d401405d1c0f7b474d6`
- Generated: `2026-08-23T04:59:15.741477+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For every literal M1/M2 complete-lift coefficient on one moving reciprocal window at W=Y^(7/16), is its local V^2 norm O_epsilon(J_B^(1/2)L^(-1)Y^epsilon), or does an exact coefficient package force a larger variation and stop the selected route?

## Reference formula and distinctions

On b' asymptotic B, write G=D/B, Q_B=min(B,BD/(WL)), J_B=1+DQ_B/B^2, b'=rho v, and U_(i,rho)(v)=sum_(g in I_(i,rho)(v))^* chi_4(g) omega_i(g,a',rho v). Prove ||U_(i,rho)||_(V^2(I)) <<_epsilon J_B^(1/2)L^(-1)Y^epsilon uniformly, including endpoint values, or isolate the first literal counterterm.

- W=Y^(7/16), D=Y^(1/2), L=Y^(1/6), D/L <= B <= D
- Q_B=BD/(WL)=Y^(log_Y B-5/48) on the critical block
- J_B=1+DQ_B/B^2=1+Y^(19/48-log_Y B)
- V^2(I)=|U(v_-)|^2+sum_(v,v+1 in I)|U(v+1)-U(v)|^2+|U(v_+)|^2
- The desired exponent theta=1/2 is useful only because theta<2/3; full-shell G^(1/2) variation is insufficient
- A proof of this coefficient norm alone does not prove the subsequent oscillatory inequality or any exponent improvement

## Assigned target

Reconstruct the exact M1/M2 complete-lift coefficient on a moving B-shell window and prove the local J_B^(1/2)/L V^2 bound package by package, or isolate the first literal residual or counterterm.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/synthesis.md`
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reports/actual_character_determinant_attack.md`
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/hostile_round117_discovery_addendum.md`
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_actual_savings.md`
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/synthesis.md`
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md`
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reviews/conductor_round127_frontier_selection_adjudication.md`

## Required controls

- `literal_complete_lift_dictionary`
- `local_window_and_birth_count`
- `V2_endpoint_terms`
- `continuous_weight_variation`
- `character_partial_sum_before_modulus`
- `mobius_divisor_progressions`
- `floors_stars_hard_faces_and_support`
- `cross_shell_owner_and_no_duplication`
- `theta_two_thirds_capacity_threshold`
- `finite_stop_rule`
- `no_exponent_or_M9_promotion`

## Required deliverables

- A seven-section analytic report.
- An exact literal coefficient dictionary before any variation estimate.
- A packagewise V^2 proof, strict partial theorem plus exact residual, or literal no-go.
- The first doubtful step and a precise state recommendation without editing shared state.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
