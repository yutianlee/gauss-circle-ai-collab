# Task Brief: lower_height_kernel_hostile_audit

- Campaign: `m9-m1-global-lower-height-kernel-gate`
- Research round: `121` (`m9_m1_global_lower_height_kernel_gate`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
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

Hostilely audit the exact pairing, boundary and floor ledger, resonance capacity, false analogues, comparison with prior return maps, and every claimed implication of the global lower height-kernel route.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-lower-radial-phase-diagram/synthesis.md`
- `rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/synthesis.md`
- `rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/synthesis.md`
- `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/synthesis.md`
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md`
- `rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md`
- `rounds/codex-managed/m9-m1-unmatched-crossing-fourier-modes/synthesis.md`
- `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/synthesis.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md`
- `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/synthesis.md`
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/derivation_packet.md`

## Required controls

- `literal_lower_reciprocal_antecedent`
- `external_R_normalization`
- `global_profile_height_kernel`
- `mod_four_pairing_identity`
- `amplitude_seam_BV`
- `phase_increment_joint_height_kernel`
- `resonant_nonresonant_capacity`
- `floor_star_hard_bottom_boundaries`
- `old_return_map_nonduplication`
- `unsigned_adversarial_control`
- `full_lower_range_scope`
- `one_count_downstream_scope`

## Required deliverables

- A seven-section hostile report.
- A pass/fail seam table and adversarial capacity controls.
- The maximal safe theorem or the fatal correction and smallest survivor.
- A precise state recommendation.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
