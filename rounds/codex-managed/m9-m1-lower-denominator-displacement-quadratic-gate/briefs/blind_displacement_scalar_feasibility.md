# Task Brief: blind_displacement_scalar_feasibility

- Campaign: `m9-m1-lower-denominator-displacement-quadratic-gate`
- Research round: `139` (`m9_m1_lower_denominator_displacement_quadratic_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `5e82825804e5bb2de43779e7121e76bcfaa4b89d7ac0977ca2ceb84a33be8552`
- Generated: `2026-08-23T16:55:00.790514+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact prescribed-centre lower scalar be bounded at R X^epsilon after the centre-constrained substitution N=y^2+q and d=y-v by a genuinely noninvertible quadratic Gauss or Salie cancellation in the physical displacement variable; if not, what is the first exact Taylor, completion, alias, boundary, self-return, or capacity obstruction?

## Reference formula and distinctions

Let R=X^(1/4), y=floor(sqrt X), N=floor X, q=N-y^2 with 0<=q<=2y. The exact scalar is F_N=sum_(h>=1)h^(-1)sum_(0<=v<y)chi_4(y-v)V_low(4R^2h^2/(y-v)^2)e(h(q+v^2)/(y-v)), with literal zero extension and target |F_N|<<_epsilon R X^epsilon.

- The identity N/(y-v)=y+v+(q+v^2)/(y-v) is exact; the discarded term h(y+v) is integral.
- For y-v odd, the complete physical phase is h(q+v^2)/(y-v)+(y-v-1)/4; even y-v terms vanish.
- The exact quadratic-core expansion has correction h v(q+v^2)/(y(y-v)); it may not be dropped or bounded outside its proved range.
- The literal profile restricts h relative to y-v and must remain smooth with every endpoint and zero-extension owner.
- Round 138 already deletes complete denominator rows and both y^(-2) carrier collars; the present mechanism must either estimate the full scalar or map its gain back to that exact residual.
- The scalar has y^(1+o(1)) absolute capacity and target R; any partial modulus, completion, or dyadic sum must return to R.
- Fourth-power q=0, maximal q=2y, small v, v near y, half-integer stationary aliases, both parities of y, and both scalar signs are mandatory controls.

## Assigned target

Independently decide from the exact displacement statement whether its physical mod-four phase and rational quadratic core yield an R-bound, a strict signed reduction, or a rigorous completion or alias obstruction.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-121 through Round-139 nonblind artifacts`
- `all Round-139 sibling reports`

## Required controls

- `exact_N_y2_q_and_displacement_bijection`
- `literal_profile_support_zero_extension_and_both_signs`
- `physical_mod_four_carrier_and_y_parity`
- `exact_quadratic_core_and_Taylor_correction`
- `small_v_and_terminal_v_boundaries`
- `dyadic_h_v_capacity_ledger`
- `quadratic_Gauss_Salie_completion_cost`
- `stationary_alias_and_half_integer_tubes`
- `q_zero_q_max_and_real_centre_uniformity`
- `map_back_to_round138_exact_residual`
- `noninvertibility_directionality_and_self_return`
- `lower_GAR_and_downstream_scope`

## Required deliverables

- A seven-section statement-only report.
- A self-contained proof attempt with exact completion and falsification controls.
- A target estimate, strict displacement survivor, or first exact no-go step.
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
