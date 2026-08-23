# Task Brief: blind_lower_height_kernel_rederivation

- Campaign: `m9-m1-global-lower-height-kernel-gate`
- Research round: `121` (`m9_m1_global_lower_height_kernel_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`
- Generated: `2026-08-21T17:42:50.931043+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 99%.
- Numerical/experimental effort: at most 1%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

After summing every exact dyadic denominator profile into one floor-perturbed height kernel before applying a norm, does mod-four denominator pairing yield a target-safe joint height inequality for the complete lower-radial antecedent, or what is the smallest exact survivor?

## Reference formula and distinctions

B_low^+=sum_j sum_(h<=H_j) Phi(h/(H_j+1))/h sum_d chi_4(d)w_j(d)V_low(4R^2h^2/d^2)e(hX/d)=sum_(h,d)chi_4(d)A_X(h,d)V_low(4R^2h^2/d^2)e(hX/d)/h, target B_low^+<<R X^epsilon, R=X^(1/4).

- X large real, R=X^(1/4), Y=sqrt X, y=floor(sqrt X)
- D_j=2^(-j)y and H_j=floor(D_j/R), with empty heights omitted
- exact hard top and smooth profiles w_j, inactive bottom kept separate
- A_X(h,d)=sum_j 1_(h<=H_j)Phi(h/(H_j+1))w_j(d)
- fixed physical V_low from the proved radial one-count partition
- mod-four pair F_X(4m+1)-F_X(4m+3) with zero-extended boundaries
- amplitude seam and joint phase increment Delta_d=2X/(d(d+2))
- all floors, profile stars, stationary stars, hard sample, product half tie, and both signs
- accepted one-sided-divisor, Appell, product-wavelet, crossing, and conductor barriers
- full lower range, including the part above the small-angle replacement threshold

## Assigned target

Independently rederive the complete lower reciprocal antecedent, its exact profile-first and mod-four-paired kernels, and prove a bound, strict subpackage, or smallest survivor without using nonblind history.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-61 through Round-121 nonblind artifacts`
- `all Round-121 sibling reports`

## Required controls

- `literal_lower_reciprocal_antecedent`
- `external_R_normalization`
- `global_profile_height_kernel`
- `mod_four_pairing_identity`
- `amplitude_seam_BV`
- `phase_increment_joint_height_kernel`
- `resonant_nonresonant_capacity`
- `floor_star_hard_bottom_boundaries`
- `unsigned_adversarial_control`
- `full_lower_range_scope`
- `one_count_downstream_scope`

## Required deliverables

- A seven-section statement-only report.
- An exact one-count and paired-kernel derivation.
- A complete bound, strict target-safe package, signed saving, or smallest exact survivor.
- A promote, retain, revise, reject, or no-change recommendation.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
