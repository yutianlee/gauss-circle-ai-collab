# Task Brief: adjacent_pairing_hostile_audit

- Campaign: `m9-m1-top-block-signed-adjacent-odd-pairing`
- Research round: `57` (`signed_adjacent_odd_pairing`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `a460b66b30b01db14bb52d3891875f7e1a97ba2f0c73b77557eef1d60b599c0a`
- Generated: `2026-08-13T18:50:03.247901+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

On R/4<h<=R/2, can adjacent odd denominators q and q+2 be paired before splitting chi_4 residue classes to produce the missing signed square-root window bound, including unmatched endpoints and actual amplitude differences?

## Reference formula and distinctions

P_J=sum_(R/4<h<=R/2) sum_(q odd,hq in J) chi_4(q) A_X(h,q)e(sqrt(Xhq)), with Y=R^2 asymp sqrt(X), |J|<=R, and exact actual A_X.

- chi_4(q+2)=-chi_4(q)
- exact q-to-q+2 phase increment
- availability of both products in one window
- amplitude finite difference
- unmatched endpoint incidence
- cross-h phase of the paired row
- perfect-fourth-power coherence
- unweighted sqrt(R) target

## Assigned target

Try to falsify adjacent-odd cancellation using high-shell window geometry, unmatched singleton owners, top plateau rows, and fourth-power phase coherence.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/derivation_packet.md`
- `rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/synthesis.md`
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`

## Required controls

- `pairing_identity`
- `two_point_window_geometry`
- `phase_increment`
- `amplitude_difference`
- `unmatched_endpoints`
- `cross_h_aggregation`
- `perfect_fourth_power`
- `target_ledger`
- `lower_shell_scope`
- `downstream_scope`

## Required deliverables

- seven-section hostile report
- strict counterexample or certification
- recommended graph effect

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
