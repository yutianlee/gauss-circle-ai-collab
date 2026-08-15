# Task Brief: blind_critical_terminal_rederivation

- Campaign: `m9-m1-critical-radial-terminal-return`
- Research round: `60` (`critical_radial_terminal_mellin_transfer`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
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

Using only the Round-60 packet, independently test the support lemma, Mellin factorization, terminal bound, transform constant, errors, and exact logical scope.

## Permitted context

- `rounds/codex-managed/m9-m1-critical-radial-terminal-return/derivation_packet.md`

## Excluded context

- `proof graph`
- `proof draft`
- `prior reports and syntheses`
- `other Round-60 reports`

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

- seven-section statement-only report
- independent proof or no-go
- isolation ledger

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
