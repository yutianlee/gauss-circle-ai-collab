# Task Brief: blind_outer_bilinear_dual_feasibility

- Campaign: `gc-w7-16-post-inner-outer-bilinear-gate`
- Research round: `130` (`gc_w7_16_post_inner_outer_bilinear_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `354f5ca462467d091a9a50c8dbc1173ffba56516963274f9fc232ea11890d20e`
- Generated: `2026-08-23T06:17:32.505563+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

After the Round-129 K_rho/L inner reciprocal/lift theorem, can one obtain a genuine signed contraction across the remaining reduced-numerator increments and/or outer rays, or does the exact outer dual, phase alignment, or unit-Hessian geometry force a capacity self-return?

## Reference formula and distinctions

For one half-open B-shell, O_(i,B)^+=sum_(r=(a,b)) A_i(r)e(ca/(kappa_i b)) F_i(r), where F_i(r)=sum_(a') sum_(rho|a') sum_(eta) S_(i,r,a',rho,eta), and every S retains its exact threshold/plateau formula. Accepted bounds are sup|A_i|<<L^(-1)Y^epsilon, sum_r|A_i(r)|^2<<D/L Y^epsilon, #r<<LD, #a'<<L, and |S|<<K_B/L Y^epsilon. Outside triangles give D K_B=Y^(35/48), while target is D=Y^(1/2). Test a direct bilinear estimate or the target-scale outer energy sum_r|F_i(r)|^2<<LD Y^epsilon without replacing the actual coefficients by an arbitrary matrix family.

- W=Y^(7/16), D=Y^(1/2), L=Y^(1/6), D/L<=B<=D
- Q_B=min(B,BD/(WL)), lambda_B=YL/(DB^2), K_B=min(Q_B,Q_B sqrt(lambda_B)+lambda_B^(-1/2))=Y^(11/48+o(1))
- current complete block D K_B=Y^(35/48+epsilon), target D=Y^(1/2+epsilon), missing factor K_B=Y^(11/48)
- outer ray energy sum|A_i|^2<<D/L and pointwise scale L^(-1) are exact actual-coefficient facts
- a'=a+p lies in O(L) literal increments, with determinant taper, M1/M2 characters, Mobius divisors, threshold data, and shell owners retained
- a strict fixed-power saving is bankable, but no global pointwise improvement follows until the complete correlation exponent drops below 9/16

## Assigned target

Compute the exact outer dual/Gram implied by the supplied post-inner bilinear statement. Prove the proposed target-scale outer energy, give a support-matched phase-aligned countermodel, or state the sharp additional actual-family property required.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-95 through Round-130 nonblind artifacts`
- `all Round-130 sibling reports`

## Required controls

- `outer_l2_dual_or_Gram`
- `phase_aligned_false_control`
- `outer_ray_and_increment_counts`
- `scalar_vs_positive_energy`
- `unit_Hessian_sequential_transform_return`
- `capacity_before_and_after`
- `no_exponent_or_M9_promotion`

## Required deliverables

- A seven-section statement-only report.
- An exact dual/Gram calculation and support-matched control.
- A proof, minimal repaired inequality, or rigorous no-go.
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
