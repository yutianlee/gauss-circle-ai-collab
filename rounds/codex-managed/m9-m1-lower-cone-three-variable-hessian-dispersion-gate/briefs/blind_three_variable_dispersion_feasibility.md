# Task Brief: blind_three_variable_dispersion_feasibility

- Campaign: `m9-m1-lower-cone-three-variable-hessian-dispersion-gate`
- Research round: `146` (`m9_m1_lower_cone_three_variable_hessian_dispersion_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d`
- Generated: `2026-08-23T22:53:27.287174+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the exact Round-145 small-t survivor admit a genuinely nondegenerate three-variable dispersion estimate in the t-d-e variables that makes a strict intermediate-t range target-safe, or even proves the target; if not, what is the first exact coefficient, mask, aspect-ratio, boundary, theorem-hypothesis, transform-return, or power obstruction?

## Reference formula and distinctions

Let R=X^(1/4), N=floor X, I_M=N intersect [M,B_M), B_M<=2M, k_(s,t)=floor(t sqrt(Ns)+1/2), and j_(s,t)=k_(s,t)^2-Nst^2. The exact open scalar is sum_M sum_(1<=t<M^(1/4)) sum_(s squarefree, st^2 in I_M, |j_(s,t)|>M^(3/4)) (st^2)^(-3/4)V_low(R^2st^2/N)C(st^2)e(t sqrt(Ns)), where C(st^2) has the accepted multiplicity-one squarefree-common-kernel and full-gcd formulas. On de=s the phase is f(t,d,e)=sqrt(N)t sqrt(de).

- On a dyadic box t asymp T, d asymp D, e asymp E with DE asymp M/T^2, the coefficient-blind weighted upper price is X^epsilon M^(1/4)/T. Any target claim must account for every box and the logarithmic assembly.
- In relative coordinates ordered as t,d,e, the scaled Hessian f^(-1)diag(t,d,e)(nabla^2 f)diag(t,d,e) equals [[0,1/2,1/2],[1/2,-1/4,1/4],[1/2,1/4,-1/4]] and has determinant 1/4. This algebraic nondegeneracy is only a candidate interface, not an estimate.
- The exact coefficient for fixed t,d,e contains the gamma,a,b factor count, parity, character, coprimality, and strict cone. Treating it as a smooth separable amplitude, arbitrary bounded coefficient, or independent tensor requires proof.
- The nearest-square mask is a discontinuous condition depending on t,d,e. It may be removed or smoothed only with an owner-complete boundary estimate; the Round-144 target-safe small-displacement result does not control a new internal partition automatically.
- The t=1 and bounded-t faces collapse the three-variable box and remain mandatory. A theorem requiring all three side lengths to grow can at most prove a strict intermediate-t reduction unless the boundary is handled separately.
- The exact family N=sL^2+1 produces surviving slowly rotating phases and must be tested against any derivative lower bound, dual separation, or uniform Diophantine hypothesis.
- The individual positive direction e(+t sqrt(Nde)) at the fixed centre N=floor X is required. Cosine, conjugate-pair, centre-average, mean-square, or coefficient-blind estimates do not substitute.
- Round 141 already found rank-one behavior in the two-variable product phase. This round may use the new t-direction only if the complete three-variable coefficient and boundary ledger survive the operation.
- The independent Round-138 collar-tail cross owner remains outside the campaign. No result here alone proves lower GAR, either direct M1 parent, any M2 owner, endpoint uniformity, M9, the bridge, or a global exponent.

## Assigned target

Independently determine whether the literal small-t squarefree-kernel scalar gains from the nondegenerate t-d-e Hessian. Reconstruct the coefficient and mask interfaces from the statement, price every aspect ratio and boundary face, and give a target proof, strict intermediate-t reduction, or exact no-go.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-138 through Round-146 nonblind artifacts`
- `all Round-146 sibling reports`

## Required controls

- `exact_t_d_e_coefficient_and_multiplicity`
- `squarefree_coprimality_parity_character_and_cone`
- `literal_profile_mask_and_block_endpoints`
- `three_variable_scaled_Hessian_determinant`
- `aspect_ratio_and_short_face_ledger`
- `M_T_D_E_capacity_and_dyadic_assembly`
- `t_equals_one_and_bounded_t_boundary`
- `exceptional_slow_frequency_family`
- `individual_complex_direction_and_fixed_centre`
- `strict_survivor_complement_target_safety`
- `Round138_cross_owner_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report.
- A self-contained Hessian, short-face, coefficient, and capacity analysis.
- A target estimate, strict intermediate-t survivor, or first rigorous no-go.
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
