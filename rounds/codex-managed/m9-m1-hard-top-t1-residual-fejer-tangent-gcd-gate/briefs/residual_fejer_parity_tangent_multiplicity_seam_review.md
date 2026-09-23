# Task Brief: residual Fejer/parity/tangent/multiplicity seam review

- Campaign: `m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate`
- Round: 185
- Role: claimant-independent seam reviewer
- Starting graph SHA-256:
  `f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`
- Candidate SHA-256:
  `791c6f3b6999991ac78198b55a106fa5e2b7767469702e853119d52b50e17385`
- Status: review evidence only; do not edit the candidate or shared state

## Objective

Independently audit (185.C1)--(185.C12) and (185.C32)--(185.C36): the
exact residual, full-line Fejer normalization, parity connector for both
parities of (R), terminal even gaps, Cauchy endpoint factor,
multiplicity-one divisor opening, tangent/product/character identities,
monotone count, opposing partition, endpoint conjugation, phase, and one
outer real part.

Do not assume the candidate's derivation.  Recompute the identities and
give the first failing line if any.  Check both signs and all literal
zero-extension fields.  Do not review the joint-(h) counting power; a
separate reviewer owns that seam.

## Context

- `protocol.md`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/blind_statement.md`

## Output contract

Write only
`rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/residual_fejer_parity_tangent_multiplicity_seam_review.md`.
Use seven sections: result/verdict, exact statement and hypotheses, proof
or line audit, first doubtful step, controls and outcomes, exact artifacts
used, recommended state effect.  Return exactly one verdict: GREEN,
REPAIR, or RED.  Stop after the report and do not start another round.

