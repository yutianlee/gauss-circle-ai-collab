# Task Brief: hybrid_zeta_l_source_hostile_audit

- Campaign: `m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate`
- Research round: `168` (`m9_m2_hard_top_t1_pre_mobius_mellin_euler_product_gate`)
- Role: `source_auditor`
- Access mode: `selected_context`
- Graph SHA-256: `a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`
- Generated: `2026-08-26T09:06:13.527080+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete literal selector-free t=1 scalar be proved at L^(3/2)X^epsilon by retaining its squarefree, coprime, odd-first-leg chi_4 family as one two-variable Euler product through exact Mellin inversion and functional equations, or where is the first exact pole, hard-boundary, hybrid-moment, or self-return obstruction?

## Reference formula and distinctions

Prove S_{L,1}=sum chi_4(d_1) A_{L,X}(d_1,d_2)e(J sqrt(d_1d_2)) <<_epsilon L^(3/2)X^epsilon over d_1 odd and d_1d_2 squarefree, with every literal shell, profile, cone, floor, star, hard value, endpoint, and zero extension retained. The accepted XOR sector may be subtracted exactly only after a full-scalar estimate.

- The exact arithmetic series is D(s_1,s_2)=sum chi_4(d_1)d_1^(-s_1)d_2^(-s_2) over squarefree coprime legs with d_1 odd.
- The local-factor candidate is D=L(s_1,chi_4)zeta(s_2)G, with G_2=1-2^(-2s_2) and G_p=(1+x_p+y_p)(1-x_p)(1-y_p) for odd p.
- The quadratic start of G suggests absolute convergence only for min(Re s_1,Re s_2)>1/2; continuation and every crossed singularity must be proved.
- A literal Mellin, Perron, or Stieltjes representation must reproduce half-open and hard endpoint values exactly.
- The square-root phase concentrates the radial Mellin frequency t_1+t_2 at scale JL; the entire transform length and angular tails must be paid.
- Round 162's termwise Möbius--Poisson route produced a rank-one product collar and sqrt(JL) positive capacity. Any functional-equation self-return to it must be identified exactly.
- Even a full t=1 proof closes only the residual after the exact accepted XOR subtraction and leaves all other hard-TOP channels and downstream parents open.

## Assigned target

Hostilely audit exact primary theorems for the zeta(s_2)L(s_1,chi_4) contour, hybrid moment, subconvexity, Perron, and approximate-functional-equation inputs required by the literal Round-168 transform. Decide whether any source yields the complete target after the actual transform length, pole residue, hard endpoints, and G factor are restored.

## Permitted context

- `protocol.md`
- `state/active_campaign.yml`
- `strategy/round168_m2_hard_top_t1_pre_mobius_mellin_euler_strategy.md`
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/barrier_packet.md`

## Required controls

- `exact_Euler_local_factors_including_p2`
- `G_absolute_convergence_and_singularities`
- `hard_half_open_profile_BV_endpoints`
- `zeta_pole_and_residue`
- `radial_angular_frequency_support`
- `full_transform_length_and_tail`
- `no_absolute_hybrid_moment_inflation`
- `functional_equation_AFE_self_return`
- `round162_product_collar_comparison`
- `arbitrary_real_centre_floors_and_stars`
- `target_L_three_halves_power_ledger`
- `primary_source_exact_hypotheses`
- `downstream_scope_and_no_exponent_promotion`
- `no_in_round_pivot`

## Required deliverables

- A seven-section hostile source report satisfying the repository report contract.
- Exact primary-source theorem statements, dates, hypotheses, parameter maps, transform lengths, residues, and restored powers.
- A target-safe source placement or the narrowest rigorous source-interface no-go.
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
