# Task brief: blind M1 top transform

Campaign: `m9-combined-top-cones`  
Task: `blind_m1_top_transform`  
Role: statement-only deriver  
Graph SHA-256: `d155bdcc1ef62728419694f98c40a1cd4fe9664d6cc7e74528b282f8dc69fa2b`

Do not read the conductor's combined-cone speculation or another Round-9
report before finishing the derivation. Read `protocol.md`,
`state/proof_obligations.yml`, `state/active_campaign.yml`, H1--H4 and the
M1 definition in `state/best_proof_draft.md`, the Round-7 profile report,
and the accepted Round-8 endpoint transform only for conventions.

Write only
`rounds/codex-managed/m9-combined-top-cones/reports/blind_m1_top_transform.md`.
Do not edit shared state.

## Objective

Derive from first principles a one-sided transform for the actual top M1
positive-frequency block

\[
-4\sum_{h>0}\alpha_{h,H}
\sum_{d\le y}\chi_4(d)W(d/y)e(hX/d),
\qquad y=\lfloor\sqrt X\rfloor.
\]

Use the exact additive decomposition of \(\chi_4(d)\), keep the full
endpoint convention, and determine every stationary Poisson frequency,
cone boundary, phase, character, leading constant, and normalized
amplitude. Bound all boundary and transform errors after the actual
\(\alpha_{h,H}\) weights. Treat negative frequencies by exact conjugacy.

Required controls: \(X=y^2\), \(h=1\), \(h\asymp H_y\), endpoint derivative
separation for both additive shifts, and even/odd dual variables.

Give the exact result, hypotheses, proof, first unproved step, controls,
dependencies, and recommended state effect.
