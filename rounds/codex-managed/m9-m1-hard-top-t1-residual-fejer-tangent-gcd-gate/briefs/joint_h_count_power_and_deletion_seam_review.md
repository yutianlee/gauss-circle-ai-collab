# Task Brief: joint-h count, power, and deletion seam review

- Campaign: `m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate`
- Round: 185
- Role: claimant-independent mathematical seam reviewer
- Starting graph SHA-256:
  `f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`
- Candidate SHA-256:
  `791c6f3b6999991ac78198b55a106fa5e2b7767469702e853119d52b50e17385`
- Status: review evidence only; do not edit the candidate or shared state

## Objective

Independently audit (185.C13)--(185.C31) and (185.C38)--(185.C39).
Verify both cross orientations, the implications of squarefreeness and
coprimality, (g=(d,d')=(u,n)), (r=2\kappa gh), primitive
multiplicity, the (t)-interval length, every fixed-parameter count,
the double harmonic sum, polylogarithmic absorption, the explicit
(\gamma^{-1},\delta^{-1}) powers, and the exact complement.

Reproduce the finite deletion example by exact arithmetic, including
both ratio inequalities, squarefreeness, character flip, (g), and
(h).  Determine whether it proves only a mechanism no-go, as claimed.
Do not rely on vote or on the blind report's authority; rederive the
count from the candidate's hypotheses.

## Context

- `protocol.md`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md`
- `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/controls/conductor_round185_exact_fibre_deletion_control.md`

## Output contract

Write only
`rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/joint_h_count_power_and_deletion_seam_review.md`.
Use seven sections: result/verdict, exact statement and hypotheses, proof
or line audit, first doubtful step, controls and outcomes, exact artifacts
used, recommended state effect.  Return exactly one verdict: GREEN,
REPAIR, or RED.  Stop after the report and do not start another round.

