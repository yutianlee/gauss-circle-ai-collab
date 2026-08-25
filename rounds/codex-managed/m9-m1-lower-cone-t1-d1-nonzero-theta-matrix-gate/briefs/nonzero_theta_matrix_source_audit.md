# Task brief: nonzero theta matrix source audit

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Research round: 157
- Role: source auditor
- Access mode: selected context
- Graph: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Status: candidate evidence only; do not edit shared proof state

## Frozen question

Does a primary theorem match the literal centered nonzero fixed-modulus
theta matrix with enough power to prove the target or a strict complete
range?

## Assigned target

Audit fixed-modulus incomplete quadratic-root sums, theta-multiplier
Kloosterman bilinear forms, quadratic large sieves, dispersion,
Kuznetsov, and half-integral spectral large sieves. For every theorem,
record modulus and averaging variables, coefficient class, nonzero
frequency hypotheses, spectral pieces, folds, signs, endpoints, and the
translated \(N,M,V,d\) power. Supply a source-legal target or range, or
the first precise interface mismatch.

## Required controls

- literal coefficient remains coupled;
- zero row is closed and removed exactly once;
- all odd divisor strata, nonzero modes, complementary representatives,
  and folds remain;
- fixed modulus is not replaced by a modulus average;
- principal, Eisenstein, exceptional, and endpoint pieces are retained;
- every theorem right side is fully normalized; and
- no literature-impossibility or downstream-exponent claim.

## Context files

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- strategy/round157_d1_nonzero_theta_matrix_strategy.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/barrier_packet.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/candidates/conductor_round157_centered_seed.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/theta_bilinear_spectral_source_audit.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/independent_spectral_source_review.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/independent_source_round156_final.md

## Output contract

Write only
rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/nonzero_theta_matrix_source_audit.md.
Use exactly seven numbered sections: Result; Exact statement and
hypotheses; Proof or derivation; First doubtful or unproved step; Control
tests and outcomes; Dependencies and artifacts used; Recommended state
effect. Preserve exact citations and distinguish source no-match from
impossibility.
