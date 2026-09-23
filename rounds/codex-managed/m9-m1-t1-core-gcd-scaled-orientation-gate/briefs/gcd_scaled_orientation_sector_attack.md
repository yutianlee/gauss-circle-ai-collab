# Task Brief: gcd_scaled_orientation_sector_attack

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Research round: `193` (`m9_m1_t1_core_gcd_scaled_orientation_involution_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- Generated: `2026-08-29T17:20:26.766989+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 98%.
- Numerical/experimental effort: at most 2%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact Round-192 jointly signed core be reduced by a gcd-scaled involution between the two opposing opened endpoint allocations, on the cofactor-coprime r=2 mod 4 close-allocation sector, while preserving every literal field and the accepted Fourier/core decomposition; or does the first mask, BV, collar, projection, or power seam rigorously block the mechanism?

## Reference formula and distinctions

For one opened opposing incidence N=dm, N+r=d'm' with d,d' odd, 0<r<R_0, 2|r, put g=(d,d') and k=(m,m'). On k=1 define tau_g(d,m,d',m')=(gm,d/g,gm',d'/g). With D_L=ceil(sqrt(L)), test the invariant sector r=2 mod 4, |d-gm|<=D_L, |d'-gm'|<=D_L. Prove the tau-paired physical block, then its exact restriction P_swap R_core=P_swap F-P_swap S_<=192, at O_(B,epsilon)(L^2 X^epsilon), or locate the first exact failure.

- The exact Round-192 core is retained: T=0 means the whole inherited rho-large remainder; for T>=1 every retained row has |rho|>=(A+1)(T+1) and |c beta-d rho|>T for every allowed primitive covector.
- The tuple order after tau_g is character divisor, complementary factor, upper character divisor, upper complementary factor; no divisor/cofactor notation may be silently swapped.
- Because d,d' are odd and r is even, m,m' have the same parity; k=1 forces both odd. The map must preserve g and k=1 and be an actual involution, not a remembered-label map.
- On r congruent to 2 mod 4, chi_4(d')chi_4(d)=-chi_4(gm')chi_4(gm); this sign must be derived before any absolute value.
- In plus coordinates d=kappa gU, d'=g(kappa U+2S), m'=kappa v, m=kappa v+2w, the proposed image is the minus tuple (U',v',S',w')=(v,U,w,S). Canonical gcd and coprimality hypotheses must be checked.
- The close inequalities imply S+w=O(D_L/g) and |kappa(v-U)|=O(D_L/g). The complete count, normalized dyadic BV multiplicity, and every literal face/collar must be priced at L^2 X^epsilon with no hidden Y.
- For the Round-184 residual selector, complementing all primes outside g preserves the 1,0,0,1 truth table unless exactly one selected prime lies in g. The fixed-g close-prime exception must be proved absent or target-safe.
- The complete anchor Fourier sum must be recombined before using orientation sign reversal. Every inherited safe projection may be restricted only if its absolute proof is stable under deletion of the physical atoms.
- Both orientations, signs, products, phases, Fejer weight, endpoint ordering and conjugation, masks, cells, crossings, births, deaths, and zero extensions remain inside one complex aggregate before the final real part.
- Even complete success closes only a strict sector of the exact original-t=1 residual. Original t>=2, near resonance, smooth M1, M2, endpoint, bridge, theorem, and exponent scopes remain separate.

## Assigned target

Prove the widest exact target-safe gcd-scaled orientation sector of the Round-192 core. Derive the opened-tuple involution, r=2 mod 4 sign reversal, primitive-coordinate map, selector and literal-field ledger, close-sector count, common-cell/BV/collar estimate, masked physical-to-core identity, exact complement, and complete L,Y,Q,X power restoration. If D_L=ceil(sqrt(L)) is too wide, prove the widest non-tautological scale and identify the first lost power.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/failure_ledger.md`
- `strategy/round193_m1_t1_core_gcd_scaled_orientation_involution_strategy.md`
- `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`
- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/synthesis.md`
- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/conductor_round192_adjudication.md`

## Required controls

- `exact_round192_core_and_T_zero_scope`
- `opened_endpoint_tuple_order`
- `cofactor_gcd_one_forces_odd_cofactors`
- `scaled_map_integrality_and_involution`
- `g_and_cofactor_gcd_preservation`
- `opposing_orientation_bijection_and_multiplicity`
- `primitive_coordinate_image_and_coprimality`
- `product_shift_phase_and_Fejer_preservation`
- `r_two_mod_four_character_reversal`
- `endpoint_order_and_lower_conjugation`
- `tau_invariant_close_mask`
- `active_support_bounds_g`
- `residual_selector_truth_table_under_g_complement`
- `selected_pair_intersects_g_exception`
- `literal_common_cell_difference`
- `dyadic_BV_lift_multiplicity`
- `all_boundary_collar_floor_star_endpoint_fields`
- `complete_close_sector_power_no_hidden_Y`
- `complete_anchor_Fourier_recombination_before_pairing`
- `inherited_safe_projection_deletion_stability`
- `exact_masked_core_identity_no_double_count`
- `exact_first_failure_complement`
- `original_t1_only_downstream_scope`
- `exponent_quarantine`

## Required deliverables

- A seven-section analytical report satisfying the repository report contract.
- An exact sector lemma and proof with involution, coefficient commutator, arithmetic/literal masks, close count, BV/collars, masked core projection, complement, and outer power ledger, or the first exact failed seam with quantified deficit.
- Write only the assigned report and any explicitly named diagnostic under this campaign; make no graph or shared-state edit.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
