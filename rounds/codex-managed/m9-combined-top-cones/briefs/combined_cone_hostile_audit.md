# Task brief: hostile combined-cone audit

Campaign: `m9-combined-top-cones`  
Task: `combined_cone_hostile_audit`  
Role: hostile falsifier  
Graph SHA-256: `d155bdcc1ef62728419694f98c40a1cd4fe9664d6cc7e74528b282f8dc69fa2b`

Read `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`,
H1--H4, the Round-8 endpoint transform synthesis and hostile report, and
the exact M1/M2 definitions. Work independently before reading other
Round-9 reports. Write only
`rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_hostile_audit.md`.

## Objective

Try to refute the combined-cone idea. Independently compute enough of the
M1 transform to audit:

- all factors of \(4\), \(i\), \(\pi\), and \(e(1/8)\);
- which variable carries \(\Phi(\cdot/(H+1))\) and \(\chi_4\);
- the exact inequality defining the stationary cone;
- endpoint half-weights and additive-character boundary series;
- whether cone complementarity survives \(q=X/y^2\ne1\);
- whether any pairing preserves the actual weights or only an artificial
  symmetric model.

Construct an exact coefficient or special-\(X\) countermodel to any false
cancellation. If an identity survives, state its narrowest correct scope
and the first remaining analytic estimate. No numerical work is expected.

Give result/no-go, proof, first doubtful line, controls, dependencies, and
recommended state effect.
