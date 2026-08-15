# Task Brief: blind_lower_radial_rederivation

- Campaign: `m9-m1-lower-radial-phase-diagram`
- Research round: `61` (`lower_radial_phase_diagram`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `ee3860a79ae0bb076d9de60151b1583aa9b9a71e85c2b7f6350dfa0eeac4fe1b`
- Generated: `2026-08-13T20:50:34.473835+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For a smooth radial block n asymp N=X^nu below sqrt X, what is the exact (delta,ell,nu) transfer, which blocks are already closed by terminal/TTY/V2 inputs, and what is the first genuinely uncovered radial exponent?

## Reference formula and distinctions

At stationary d=2sqrt(hX/q), n=hq=4Xh^2/d^2. For d asymp D=X^delta and n asymp N=X^nu, h lies at L asymp D sqrt(N/X)=X^(delta+(nu-1)/2). Derive all floor, support, normalization, and error consequences exactly.

- D=X^delta with 1/4<=delta<=1/2
- N=X^nu with 0<=nu<=1/2
- L=X^ell and ell=delta+(nu-1)/2
- active condition 1<=L<=H_D asymp X^(delta-1/4)
- terminal bound 1+D/L
- TTY exponent [89(1+ell)+819delta]/1282
- TTY target 178ell+1638delta<=463
- V2 endpoint (delta,ell)=(1/2,0)
- external radial normalization R=X^(1/4)
- exact floors, hard top, stars, and smooth radial cutoff errors

## Assigned target

Using only the Round-61 packet, independently derive the exponent map, coverage union, and first uncovered radial band.

## Permitted context

- `rounds/codex-managed/m9-m1-lower-radial-phase-diagram/derivation_packet.md`

## Excluded context

- `proof graph`
- `proof draft`
- `prior reports and syntheses`
- `other Round-61 reports`

## Required controls

- `stationary_exponent_map`
- `active_support`
- `floor_small_height`
- `terminal_translation`
- `TTY_translation`
- `V2_translation`
- `union_over_delta`
- `scale_sum`
- `transform_errors`
- `first_uncovered_band`
- `required_saving`
- `downstream_scope`

## Required deliverables

- seven-section statement-only report
- independent exact inequalities
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
