# Task Brief: blind_quadratic_completion_rederivation

- Campaign: `m9-m1-top-block-quadratic-divisor-completion`
- Research round: `59` (`short_twisted_divisor_quadratic_completion`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `84ef4ee035b0da8c2672d60ce0580918e54ae08696b5bb13e70b0aba8117ab07`
- Generated: `2026-08-13T19:46:35.586430+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does exact additive completion of chi_4(n/h)1_(h|n), followed by a coefficient-preserving radial B-process, prove square-root cancellation in the length-R high-shell twisted-divisor sum, or does the dual reciprocal strip rigorously return to an equivalent-hard kernel?

## Reference formula and distinctions

P_J=sum_(A<=n<=B)e(sqrt(Xn)) sum_(h|n,R/4<h<=R/2,n/h odd) chi_4(n/h) Omega_X^*(n,h), where Y=R^2 asymp sqrt(X), |J|<=R, and the unweighted target is X^epsilon sqrt(R).

- exact additive character-divisibility projector modulo 4h
- radial B-process stationary and nonstationary terms
- dual variables r=4hk-a and r=4Kh+s
- dual strip phase Xh/r and exact Hessian determinant
- chi_4 character under the r-to-s change
- raw dual target R before the R^(-1/2) stationary normalization
- actual profiles, height floors, hard top, and stars
- perfect-fourth-power and quarter-frequency resonances

## Assigned target

Using only the Round-59 packet, independently derive the projector, stationary dual strip, normalization, Hessian, and best rigorously justified capacity.

## Permitted context

- `rounds/codex-managed/m9-m1-top-block-quadratic-divisor-completion/derivation_packet.md`

## Excluded context

- `proof graph`
- `proof draft`
- `prior reports and syntheses`
- `other Round-59 reports`

## Required controls

- `projector_constant`
- `Bprocess_normalization`
- `dual_strip_geometry`
- `Hessian_and_rank`
- `character_resonance`
- `actual_amplitude`
- `endpoints_and_stars`
- `perfect_fourth_power`
- `target_ledger`
- `source_applicability`
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
