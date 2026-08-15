# Task Brief: critical_radial_terminal_transfer_attack

- Campaign: `m9-m1-critical-radial-terminal-return`
- Research round: `60` (`critical_radial_terminal_mellin_transfer`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `f029f8b805e59fab88500cf2128e3128c2304409fdb87b83ea6b10143420a2c5`
- Generated: `2026-08-13T20:23:08.506149+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For a fixed smooth critical radial cutoff V(n/sqrt(X)) of constant relative width, does Mellin separation convert the exact GAR sector into terminal M1 blocks already bounded by O_epsilon(1+D/L), including floors, the hard top, stars, and transform errors?

## Reference formula and distinctions

G_V(X)=sum_(n<=16sqrt(X)) V(n/sqrt(X)) C_X^*(n)n^(-3/4)e(sqrt(Xn)); prove the fixed GAR real projection for every fixed V in C_c^infinity((c,C)) with 0<c<C<16; the existing factor 1_(h<=H_j) owns the upper terminal endpoint.

- R=X^(1/4), Y=sqrt(X)=R^2
- exact C_X^*(n) and Omega_X^*(n,h)
- stationary identity n=4Xh^2/d^2
- Mellin convention V(z)=(2pi)^(-1) integral Vhat(t)z^(it)dt
- terminal support h asymp H_j=floor(D_j/R)
- mode weights h^(2it) and d^(-2it)
- BV cost (1+|t|)/H_j
- terminal bound 1+D_j/H_j asymp R
- interior and one-sided B-process constants and errors
- hard-top boundary, height floors, profiles, and equality stars
- external factor -(4/pi)R Re(e(1/8) dot) exactly once

## Assigned target

Construct the exact Mellin-separated primal antecedent, apply the terminal divisor theorem, transfer through the interior/top B-process, and prove the smooth critical radial GAR sector or isolate the first exact seam.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-critical-radial-terminal-return/derivation_packet.md`
- `rounds/codex-managed/m9-m1-top-block-quadratic-divisor-completion/synthesis.md`
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`
- `rounds/codex-managed/m9-top-endpoint-transform/reports/one_sided_poisson_derivation.md`

## Required controls

- `Mellin_normalization`
- `terminal_support`
- `frequency_BV`
- `denominator_mode`
- `Bprocess_constant`
- `hard_top_boundary`
- `floors_profiles_stars`
- `small_height`
- `scale_one_count`
- `error_sum`
- `GAR_implication_scope`
- `downstream_scope`

## Required deliverables

- seven-section report
- exact sector identity and normalization
- critical-sector theorem or first sharp obstruction

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
