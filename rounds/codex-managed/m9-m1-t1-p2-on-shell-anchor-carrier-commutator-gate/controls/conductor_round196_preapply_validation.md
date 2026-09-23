# Conductor Round-196 preapply validation

- Starting graph SHA-256:
  f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2
- Terminal State Patch SHA-256:
  013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d
- Terminal candidate SHA-256:
  5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380
- Durable kernel SHA-256:
  51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb
- Intended scope:
  0 create / 2 update / 0 corrected rejection / 20 reject /
  27 no change

## Result

PASS.  The official graph-patch validator accepts the State Patch against
the exact live starting graph.  In-memory Round-196 application produces
zero graph issues.  The six repository unit controls pass, campaign
validation passes, and Python bytecode compilation passes.

Every one of the 24 evidence paths exists and is duplicate-free within
each update.  The two updated nodes retain their status, statement,
dependencies, implications, blockers, positive evidence, and negative
evidence.  Only their inconclusive evidence, next action, and
round/timestamp metadata change.  All 20 rejection IDs are fresh and
distinct from the 395 proof-obligation IDs and 1,755 prior rejected
claims.

The conductor's independent in-memory simulation obtains:

- exact apply/reverse recovery of the canonical starting graph;
- deep equality of every proof-obligation node outside the two updates;
- deep equality of all 27 declared no-change objects;
- unchanged original rejected-claim prefix; and
- operation counts \(0/2/0/20/27\).

Three independent preapply audits pass:

1. controls/preapply_independent_reverse_replay_audit.md, SHA-256
   ba0fb7cbc85bf80bdd9c7ca3cccf807525a47cd1d1f7069aba7870babae12c23;
2. controls/preapply_hostile_scope_protected_state_audit.md, SHA-256
   77aaa5647716ceb624ccd033d4c49755d1d82a2c58703b351b3d4b795a404553;
3. controls/preapply_evidence_provenance_hygiene_audit.md, SHA-256
   2109891abf0d55678884f4861b7d787ab310274e195f1ef28b7a87db2ec009b7.

The entire campaign, terminal kernel, candidate, State Patch, and audit
set pass strict UTF-8, LF-only, no-BOM, no-tab, and C0 hygiene after a
mechanical LF normalization of the generated plan and three generated
briefs.  No mathematical content changed.

The patch is approved for mechanical application at Round 196 with the
conductor adjudication as judge reference.
