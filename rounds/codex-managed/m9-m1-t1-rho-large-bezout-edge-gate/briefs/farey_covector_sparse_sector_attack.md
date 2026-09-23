# Task Brief: farey_covector_sparse_sector_attack

- Campaign: `m9-m1-t1-rho-large-bezout-edge-gate`
- Research round: `192` (`m9_m1_t1_rho_large_farey_covector_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13`
- Generated: `2026-08-29T15:30:32.530462+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 96%.
- Numerical/experimental effort: at most 4%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact Round-191 rho-large remainder be reduced further by a target-safe union of small unimodular Farey covectors of the canonical inverse matrix, with an exact badly-approximable core, and can that core be estimated by a genuinely literal phase/carry mechanism or shown to resist the proposed iteration?

## Reference formula and distinctions

Fix Q=H_B, U=mq>4Q, q>Q, Qm<Y, the exact Round-189 fast projective condition, and the Round-191 remainder |rho_U(v)|>T=min((U-1)/2,floor(QmU/Y)) after its terminal and isolated Fejer projections. For v0=[v]_U define rho v0-beta U=1. For 1<=c< U and 0<=d<=c define ell_(c,d)=c beta-d rho, so rho(c v0-dU)=c+U ell_(c,d). With A=min(U-1,floor(Q^C0)), prove the union T>=1 and min_(c,d coprime,c<=A)|ell_(c,d)|<=T target-safe at fixed scale Qm kappa u X^epsilon and through the exact outer ledger, or locate the first exact failure.

- The canonical beta uses v0=[v]_U in 1,...,U-1. It is not the actual transport quotient gamma=(rho v-1)/U for a noncanonical literal representative.
- For fixed c,d,ell the exact identity rho(c v0-dU)=c+U ell converts residue classes into divisor pairs; c<U prevents a zero right side.
- The Farey family has O(Q^(2C0)) members, a fixed polylogarithmic cost that may be absorbed only through a fresh epsilon budget.
- The T=0 sector is defined empty; isolated ell=0 classes may not be called target-safe when the density budget is below one residue class.
- The inherited literal v support has total length O(u), U divides u, and each residue class occurs O(u/U+1)=O(u/U) times; projective bands and literal masks only delete rows.
- Both orientations, all remaining jump sources, every endpoint field, phase, carry, mask, and zero extension remain in one complex aggregate before the final real part.
- A full-core claim needs cancellation for the fixed literal coefficients. Farey separation alone supplies no cancellation for arbitrary bounded arrays.
- Even complete rho-large success closes at most the exact original-t=1 residual through accepted connectors; every original t>=2 range, near resonance, smooth M1, M2, endpoint, bridge, theorem, and exponent remains separate.

## Assigned target

Prove the widest exact target-safe Farey-covector sector of the Round-191 remainder. Derive the factorization and divisor count, define a disjoint or union-safe complex projection, restore the full fixed and outer ledgers, prove every valid small-U or edge/central coverage corollary, and leave one exact literal core if the full target is not reached.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/failure_ledger.md`
- `strategy/round192_m1_t1_rho_large_farey_covector_strategy.md`
- `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`
- `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/synthesis.md`
- `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reviews/conductor_round191_adjudication.md`

## Required controls

- `exact_round191_rho_large_remainder`
- `round191_terminal_and_Fejer_already_removed`
- `canonical_v0_vs_literal_v_vs_transport_gamma`
- `signed_least_inverse_and_beta_signs`
- `exact_unimodular_covector_factorization`
- `c_strictly_less_than_U_nonzero_rhs`
- `T_zero_sector_empty`
- `ell_zero_and_floor_cases`
- `divisor_pair_multiplicity`
- `Farey_family_size_polylogarithmic`
- `literal_residue_class_multiplicity_U_divides_u`
- `fast_projective_band_only_deletes`
- `one_outer_real_part_both_orientations`
- `safe_projection_union_no_double_count`
- `exact_badly_approximable_core`
- `small_U_coverage_corollary`
- `exact_m_inverse_cq_lift_and_outer_divisor_ledger`
- `Q_L_Y_X_power_and_epsilon_budget`
- `original_t1_only_downstream_scope`
- `exponent_quarantine`

## Required deliverables

- A seven-section analytical report satisfying the repository report contract.
- An exact covector-sector lemma, proof, outer power ledger, safe projection, and complement, or the first failed inequality with a quantitative deficit.
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
