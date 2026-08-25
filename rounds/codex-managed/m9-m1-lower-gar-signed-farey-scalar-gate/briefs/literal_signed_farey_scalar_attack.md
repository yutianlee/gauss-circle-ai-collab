# Task Brief: literal_signed_farey_scalar_attack

- Campaign: `m9-m1-lower-gar-signed-farey-scalar-gate`
- Research round: `138` (`m9_m1_lower_gar_signed_farey_scalar_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `56de446648dfb7a492fbb4b46c38d840fb14ac306df61bf61d466d26abfbe797`
- Generated: `2026-08-23T15:51:21.052531+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact lower-GAR scalar be bounded by R X^epsilon in its reduced-Farey form, or can its exact scalar square be reduced to a strictly smaller signed nonzero-determinant survivor, without passing through the rejected separated k-square function; if not, what is the first exact resonance, completion, stationary, directionality, self-return, or capacity obstruction?

## Reference formula and distinctions

F_N=sum_(2<=b<=y, b odd) lambda_b sum_(1<=a<b,(a,b)=1) e(aN/b)J_(R,y)(a/b), lambda_b=chi_4(b)b^(-1)sum_(g<=y/b)chi_4(g)/g, R=X^(1/4), y=floor(sqrt(X)), N=floor(X), with target |F_N|<<_epsilon R X^epsilon. Its exact square has phase e(N(ab'-a'b)/(bb')) and target R^2=y.

- J_(R,y)(t)=eta(yt)V_low(4R^2t^2)/t on the small positive arc, extended smoothly by zero and periodically, with J(0)=0
- F_N is termwise identical to sum_(d<=y)chi_4(d)sum_(h>=1)h^(-1)V_low(4R^2h^2/d^2)e(hN/d)
- reducing h/d=a/b aggregates all odd lifts into lambda_b before any norm
- the b=1 centre vanishes because J(0)=0; determinant zero in the exact scalar square is equality of reduced fractions
- the diagonal target is O(yX^epsilon); same-denominator unequal numerators remain off diagonal and require a separate control
- the exact scalar has absolute capacity y=R^2 and target R; its exact square has absolute capacity y^2 and target y
- the Round-127 uncentered k-energy is false and the centered k-energy is a stronger separated norm; neither is the frozen mechanism
- all floors, primitive numerators, lift character, literal profile, support endpoints, both signs, and real-X uniformity are retained

## Assigned target

Derive and exploit the exact reduced-Farey scalar and its actual scalar-square determinant form to prove the R target, a strict smaller signed survivor, or the first exact arithmetic or transform obstruction.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0823_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md`
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/lower_gar_wavelet_feasibility.md`
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reviews/conductor_round127_frontier_selection_adjudication.md`
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/blind_statement.md`

## Required controls

- `literal_flat_cone_to_reduced_farey_scalar`
- `lift_character_and_b1_centre`
- `profile_floor_support_and_both_signs`
- `exact_scalar_square_and_diagonal`
- `same_denominator_unequal_numerators`
- `cross_denominator_determinant_arithmetic`
- `exact_and_near_phase_one_families`
- `character_pairing_and_stationary_dual_modes`
- `scalar_capacity_and_directionality`
- `transform_contraction_or_self_return`
- `real_centre_and_boundary_uniformity`
- `lower_GAR_and_downstream_scope`

## Required deliverables

- A seven-section analytic report.
- An exact scalar and scalar-square dictionary with a complete R-power ledger.
- A target estimate, strict owner-complete signed survivor, or first exact scalar obstruction.
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
