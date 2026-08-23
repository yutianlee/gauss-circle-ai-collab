# Task Brief: blind_m1_parent_minimax_rederivation

- Campaign: `m9-m1-direct-parent-minimax-gate`
- Research round: `119` (`m9_m1_direct_parent_minimax_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `c3498daad3bdceb7c69c0e47a616e03ebfa12ccaf42f8df42958aa227f50fd91`
- Generated: `2026-08-21T16:34:24.392280+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 99%.
- Numerical/experimental effort: at most 1%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

After every accepted direct owner is removed, what is the exact separate minimax capacity of the hard and smooth M9-M1 physical parents, and does any accepted theorem or literal adjacent-profile identity shrink either parent?

## Reference formula and distinctions

B_1(D,L;X)=sum_(h asymp L)Phi(h/(H_D+1))h^(-1) sum_(d asymp D)chi_4(d)w_D(d)e(hX/d), with residual U_1={ell<delta-1/4,178ell+1638delta>463} minus {(1/2,0)}. Direct bounds are 1+D/L, 1+sqrt(LX/D)+D^(3/2)/sqrt(LX), and the audited TTY exponent [89(1+ell)+819delta]/1282. The hard transformed parent has target L^(3/2) and coefficient-blind capacity L^2.

- X large real; D=X^delta, L=X^ell, 1/4<=delta<=1/2, 0<=ell<=delta-1/4
- accepted owner priority bottom, R5-Full, terminal, full second derivative, TTY, then residual U_1
- unique hard profile containing floor(sqrt X), every other denominator profile smooth
- hard parent M9-M1-top-endpoint-signed-cone on middle/lower residual shells
- smooth parent M9-M1-direct-smooth-residual-blockwise-estimate on every smooth U_1 label
- candidate hard witness D_0 asymp floor(sqrt X), L asymp X^(1/6)
- candidate smooth witness D_1 asymp floor(sqrt X)/2, L asymp X^(1/6)
- candidate critical capacity X^(1/3) versus target X^(1/4), deficit X^(1/12)=L^(1/2)
- canonical Gram and GAR are alternative routes, not accepted blockwise owners

## Assigned target

Independently derive the exact separate hard/smooth direct-menu minimax, verify the literal critical labels, and identify any lawful shrink or the first exact obstruction.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-91, Round-98, and Round-119 nonblind artifacts`
- `all Round-119 sibling reports`

## Required controls

- `literal_m1_block_and_profiles`
- `owner_priority_and_U1`
- `hard_smooth_physical_split`
- `frequency_first_capacity`
- `full_second_derivative_capacity`
- `TTY_exponent_and_hypotheses`
- `critical_hard_label`
- `critical_first_smooth_label`
- `floor_star_support_and_real_X`
- `hard_cone_physical_normalization`
- `adjacent_profile_telescope`
- `menu_optimality_vs_lower_bound`
- `canonical_Gram_and_GAR_nonimplication`
- `downstream_scope`

## Required deliverables

- A seven-section statement-only report.
- The exact separate minimax and literal witness families, or a proved shrink.
- A hard/smooth owner and capacity table.
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
