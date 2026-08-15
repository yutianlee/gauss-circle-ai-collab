# Task Brief: blind_hyperbola_floor_rederivation

- Campaign: `m9-m1-top-block-signed-hyperbola-floor`
- Research round: `58` (`signed_hyperbola_floor_sawtooth`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `1a73979db8bdcec9273d277238a6bd6b6a6c13ce8603cb917cca38fa7ce6fcbb`
- Generated: `2026-08-13T19:13:26.942695+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact matched-plus-unmatched high-shell selector be rewritten as a finite hyperbola-floor/sawtooth Fourier sum and estimated with square-root strength across h, without taking rowwise absolute values?

## Reference formula and distinctions

P_J=sum_(R/4<h<=R/2) sum_(q odd,hq in [A,B]) chi_4(q) A_X(h,q)e(sqrt(Xhq)), with Y=R^2 asymp sqrt(X), B-A+1<=R, and exact actual A_X.

- exact odd-lattice endpoint floors
- zero Fourier mode
- nonzero Fourier modes and truncation
- character parity projector
- cross-h phase after endpoint Fourier expansion
- actual amplitude profile and star jumps
- perfect-fourth-power resonances
- unweighted sqrt(R) target

## Assigned target

Using only the Round-58 packet, independently derive the exact floor selector, Fourier modes, endpoint ledger, and capacity.

## Permitted context

- `rounds/codex-managed/m9-m1-top-block-signed-hyperbola-floor/derivation_packet.md`

## Excluded context

- `proof graph`
- `proof draft`
- `prior reports and syntheses`
- `other Round-58 reports`

## Required controls

- `exact_floor_selector`
- `zero_mode`
- `fourier_truncation`
- `character_projector`
- `cross_h_phase`
- `actual_amplitude`
- `endpoint_and_stars`
- `perfect_fourth_power`
- `target_ledger`
- `downstream_scope`

## Required deliverables

- seven-section statement-only report
- independent identity or no-go
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
