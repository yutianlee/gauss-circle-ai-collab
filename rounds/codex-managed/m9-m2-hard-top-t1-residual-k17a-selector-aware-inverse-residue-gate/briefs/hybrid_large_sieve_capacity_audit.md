# Task Brief: hybrid_large_sieve_capacity_audit

- Campaign: `m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate`
- Research round: `177` (`m9_m2_hard_top_t1_residual_k17a_selector_aware_inverse_residue_gate`)
- Role: `barrier_no_go`
- Access mode: `selected_context`
- Graph SHA-256: `e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8`
- Generated: `2026-08-27T01:20:45.608816+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete literal low-cross-gcd K17a complement gain the missing factor L through a selector-aware signed hybrid inverse-residue estimate retaining v, n, t, every Fourier alias, and both orientations before every modulus, or does that mechanism have an exact diagonal, reduced-conductor, selector-variation, restored-capacity, or self-return obstruction?

## Reference formula and distinctions

For fixed 0<delta<1/2, prove Re C_rem_(R_log<r<R_0,2,opp,(d,d')<gamma L,kappa_*<delta L) <<_(delta,gamma,epsilon) L^2 X^epsilon. Equivalently, after the exact anchor DFT, prove a target-strength signed hybrid block estimate with the full literal amplitude.

- The literal coefficient is lambda_N(d)=omega_L(N)rho_N(d)A_N(d), retaining the squarefree shell, normalization, canonical neither/both or no-pair selector, both parity branches, profiles, floors, stars, hard values, endpoints, and zero extension.
- Round 176 already proves every fixed-proportion sector kappa_*>=delta L; only the exact complement kappa_*<delta L is in scope.
- For fixed kappa and u, literal support has v approximately L/kappa, n at most a constant times L/kappa, and O(1+kappa) fibre sites, so the raw v,n,t capacity is L^2/kappa.
- The anchor DFT coefficients c_u(k) have l1 norm logarithmic, l2 norm one, and constant-size near-half aliases; the near-half packet cannot be discarded.
- The sufficient local scale is L: a c_u-weighted fixed-(kappa,u) bound O(L X^epsilon), or the stronger uniform aliaswise bound, sums to L^2 X^epsilon after logarithms.
- The exact primitive modulus is u/(u,n); every gcd multiplicity, incomplete interval, diagonal, off-diagonal, selector switch, phase-stationary mode, endpoint, and orientation must be restored.
- Success closes only the remaining K17a complement and complete residual scalar through accepted implications; all broader owners and every exponent remain separate.

## Assigned target

Hostilely audit every reciprocal large-sieve, TT*, primitive-modulus, alias-energy, and two-orientation power seam. Validate a target route or prove the narrowest exact restored-capacity or self-return obstruction.

## Permitted context

- `protocol.md`
- `state/active_campaign.yml`
- `strategy/round177_m2_hard_top_t1_residual_k17a_selector_aware_inverse_residue_strategy.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/barrier_packet.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/joint_fibre_capacity_hostile_audit.md`
- `strategy/round173_selection/k26_actual_symbol_mechanism_audit.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md`

## Required controls

- `literal_residual_coefficient`
- `exact_low_cross_gcd_complement`
- `both_opposing_orientations`
- `anchor_DFT_and_near_half_alias`
- `hybrid_v_n_t_capacity`
- `primitive_modulus_and_gcd_multiplicity`
- `k_zero_and_imprimitive_aliases`
- `incomplete_v_interval`
- `large_sieve_diagonal_offdiagonal`
- `squarefree_Mobius_progressions`
- `parity_and_two_adic_branches`
- `selected_and_no_pair_rows`
- `short_cross_gcd_fibres`
- `stationary_and_dechirped_modes`
- `endpoints_and_zero_extension`
- `false_coefficient_controls`
- `residual_only_owner_scope`
- `no_in_round_pivot`

## Required deliverables

- A seven-section hostile report satisfying the repository report contract.
- A mechanism-by-mechanism exact identity, diagonal/off-diagonal ledger, countermodel, or restored-power table.
- The narrowest justified no-go, if any, with every unexcluded route named.
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
