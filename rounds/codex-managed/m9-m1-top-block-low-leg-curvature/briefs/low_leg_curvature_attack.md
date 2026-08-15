# Task Brief: low_leg_curvature_attack

- Campaign: `m9-m1-top-block-low-leg-curvature`
- Research round: `55` (`top_block_low_leg_curvature`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `4efbecf244fa2c1f071a7fd2fe5c1eda0ba2596d51c4c873eefc0b47ffca211f`
- Generated: `2026-08-13T17:55:53.080888+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

On the critical top radial block, can one-dimensional curvature prove target-sized control of all incidences with a polylogarithmically small angular leg h or character leg q, and what exact balanced bilinear core remains?

## Reference formula and distinctions

S_(Y;H,Q)=sum_(n asymp Y)^* n^(-3/4)e(sqrt(Xn)) sum_(hq=n,q odd,h<=H or q<=Q) chi_4(q)Omega_X^*(n,h), with Y asymp sqrt(X) and R asymp sqrt(Y).

- length-R moving product windows
- fixed-h odd-q phase sqrt(Xhq)
- fixed-q h phase sqrt(Xhq)
- profile and Vaaler sampled BV
- small-curvature versus trivial crossover at leg sqrt(R)
- hard top and angular stars
- H,Q exponent ledger
- balanced core h,q>polylog(X)

## Assigned target

Prove the strongest uniform fixed-leg moving-window estimate supported by the actual profiles, propagate it through Fejer, and isolate the balanced core.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-top-block-low-leg-curvature/derivation_packet.md`
- `rounds/codex-managed/m9-m1-global-angular-shifted-correlation/synthesis.md`
- `rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/synthesis.md`
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`

## Required controls

- `fixed_leg_phase`
- `curvature_trivial_crossover`
- `sampled_profile_BV`
- `height_floor_and_stars`
- `moving_window_edges`
- `perfect_fourth_power`
- `H_Q_ledger`
- `double_counting`
- `balanced_core_scope`
- `downstream_scope`

## Required deliverables

- seven-section report
- exact margin theorem or no-go
- balanced-core statement

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
