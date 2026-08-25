# Task Brief: literal_t1_character_poisson_attack

- Campaign: `m9-m2-hard-top-t1-close-factor-bilinear-gate`
- Research round: `162` (`m9_m2_hard_top_t1_close_factor_bilinear_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422`
- Generated: `2026-08-25T13:19:44.109875+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the actual chi_4-weighted t=1 squarefree close-factor scalar be bounded by L^(3/2)X^epsilon at one arbitrary fixed real centre using character-preserving Poisson, differencing, or a literal coefficient-sensitive bilinear theorem before every positive norm; or do rank-one product-phase geometry, squarefree and coprime openings, dual hyperbola collars, boundary terms, source hypotheses, or restored powers repay the full L^(1/2-o(1)) gain?

## Reference formula and distinctions

S_(L,1)=sum_(d1 d2 asymp L^2, d1,d2 squarefree, (d1,d2)=1, d1 odd, d2<=d1<=4d2) chi4(d1)(L^2/(d1d2))^(3/4)eta_L(d1)Phi(d1/(H+1))W(sqrt(q_X d1/(4d2)))e(J sqrt(d1d2)), with all literal half-open supports, floors, profile entries and exits, cone endpoints, stars, and zero extension retained. The target is |S_(L,1)| <<_epsilon L^(3/2)X^epsilon.

- J=sqrt(X), y=floor(J), q_X=X/y^2, H=floor(y X^(-1/4)), and 1<<L<<H<=J^(1/2) is one half-open hard-TOP frequency block.
- The t=1 radical incidence forces g=u=v=1; hence d1,d2 are squarefree, coprime, d1 is odd, d2 may be even, and both variables are asymptotic to L on the cone.
- The positive or coefficient-uniform capacity is L^(2+o(1)); the target requires L^(1/2-o(1)) arithmetic signed gain.
- The phase f(x,z)=J sqrt(xz) has rank-one Hessian: det Hess(f)=0. Any claim of genuine two-variable curvature must address its radial null direction.
- Using chi4(x)=(e(x/4)-e(-x/4))/(2i), one-variable Poisson has stationary frequencies r=k-sigma/4 and saddle x_0=Xz/(4r^2), with transformed phase Xz/(4r); this must be compared literally with the accepted reciprocal self-return.
- Two-variable stationary equations imply (k-sigma/4)ell=X/4. Finite support broadens this to a dual product collar whose width and coefficient mass must be proved rather than guessed.
- No t=1 result transfers automatically to the remaining few-point channels, the hard-TOP parent, M9-M2, M9, the bridge, or a global exponent.

## Assigned target

Attack the complete physical t=1 scalar before every positive norm. Derive the exact character-preserving one- and two-variable Poisson or differencing formula, including squarefree and coprime restrictions, and prove the target, a complete signed sector, or the first exact self-return, dual-collar, endpoint, or restored-power obstruction.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round162_m2_hard_top_t1_close_factor_strategy.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/barrier_packet.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/candidates/conductor_round162_t1_poisson_seed.md`
- `proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md`
- `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/synthesis.md`
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md`
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/conductor_round137_product_fibre_adjudication.md`

## Required controls

- `literal_t1_coefficient_and_orientation`
- `squarefree_coprime_even_d2_branch`
- `chi4_preserved_before_positive_norms`
- `product_phase_rank_one_hessian`
- `one_variable_character_poisson_self_return`
- `two_variable_dual_hyperbola`
- `dual_product_collar_width_and_mass`
- `mobius_opening_and_rescaled_support_cost`
- `hard_cone_profiles_floors_endpoints`
- `missing_L_half_power`
- `physical_coefficient_vs_diagnostic`
- `remaining_few_point_and_downstream_scope`

## Required deliverables

- A seven-section analytic report satisfying the repository report contract.
- The literal coefficient and complete character-Poisson, dual-range, collar, boundary, and power ledger.
- A target theorem, complete signed sector, or first rigorous scoped obstruction.
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
