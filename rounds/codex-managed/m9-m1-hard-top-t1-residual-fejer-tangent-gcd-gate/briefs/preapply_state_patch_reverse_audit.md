# Round 185 preapplication State Patch and reverse-audit brief

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Role: independent graph, scope, and exact-reversibility auditor
- Starting graph SHA-256:
  f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- State Patch SHA-256:
  2d4734c8a4b61acdd2081a4cad785ab56d05aac112c464935cf6916a3e9d6e4e
- Adjudication SHA-256:
  f69030851b6c187e3428d27870367804b486541537387ea3b52a10a784a33914
- Synthesis SHA-256:
  611651ecdda5a3c773228299929cf9fde5b2e807dfe5bf3c479f2947b9141f72
- Expected operation inventory: create 1, update 1, correct 0,
  reject 20, no_change 31
- Output:
  controls/preapply_independent_reverse_audit.md

Read completely: `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`, the patch, adjudication, synthesis, durable
kernel, and all three final kernel reviews.  Verify frozen hashes first.

Independently parse and simulate the patch without modifying the graph.
Audit the exact operation inventory; every created, updated, rejected, and
protected ID; every dependency and evidence path; dependency direction;
dangling references; duplicate IDs; implication and blocker drift; SCC or
cycle drift; protected inherited statuses and statements; parent, bridge,
target, and exponent quarantine; and exact agreement with the adjudication.
Construct and test the stated inverse in memory, including removal of the
created node and rejected records, removal of added dependency/evidence,
and restoration of next_action and metadata.  Require byte-identical
recovery of the starting graph under its canonical serialization.

Write one seven-section report only to the assigned output.  Return GREEN
only if validation, scope, and exact reversibility all pass.  Otherwise
return REPAIR with the first failing item.  Do not apply the patch and do
not edit any graph, campaign, validation matrix, proof draft, synthesis,
patch, or other shared state.
