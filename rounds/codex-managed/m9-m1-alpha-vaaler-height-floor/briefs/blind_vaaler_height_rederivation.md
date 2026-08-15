# Task Brief: blind_vaaler_height_rederivation

- Campaign: `m9-m1-alpha-vaaler-height-floor`
- Research round: `52` (`alpha_vaaler_height_floor_type_and_variation`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `76a480a78ae30353d4f9cbe26c0e17337c1b89318c4a15758a6ffe0c34051fea`
- Generated: `2026-08-13T16:08:02.784936+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Is H_j=floor(D_j X^(-1/4)) a moving alpha-contour seam, or a fixed discrete parameter; and what is the exact adjacent-height variation of its Vaaler coefficient family?

## Reference formula and distinctions

a_H(h)=1_(1<=h<=H) Phi(h/(H+1)), Phi(u)=pi u(1-u)cot(pi u)+u, alpha_(h,H)=i a_H(h)/(2 pi h), and Omega_X^*(n,h)=sum_j a_(H_j)(h)[w_j(2h sqrt(X/n))]^*.

- zero or nonzero contour velocities of H_j
- exact Delta_H a(h)=a_(H+1)(h)-a_H(h)
- unweighted, 1/h-weighted, and power-weighted h norms
- new endpoint h=H+1
- simultaneous D_j, dyadic-profile, support, and star changes
- possible implication for alpha lattice jump capacity

## Assigned target

Using only the Round-52 packet, independently decide the variable type and derive sharp adjacent-height variation bounds.

## Permitted context

- `rounds/codex-managed/m9-m1-alpha-vaaler-height-floor/derivation_packet.md`

## Excluded context

- `proof graph`
- `proof draft`
- `prior reports and syntheses`
- `other Round-52 reports`

## Required controls

- `variable_type`
- `exact_Phi_formula`
- `right_endpoint_taper`
- `adjacent_height_identity`
- `weighted_norms`
- `actual_scale_coupling`
- `star_ownership`
- `alpha_capacity_scope`
- `downstream_scope`

## Required deliverables

- seven-section statement-only report
- independent proof
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
