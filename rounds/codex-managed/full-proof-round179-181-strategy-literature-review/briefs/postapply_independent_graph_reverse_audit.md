# Task Brief: Round 182 post-application graph and reverse audit

- Campaign: `full-proof-round179-181-strategy-literature-review`
- Round: `182`
- Role: independent post-application graph, scope, inverse, and frozen-time replay auditor
- Starting graph: `fec130bc66641cbdad18c832de10077a7825f1caaf5d10170a67ef65c0b27196`
- Expected applied graph: `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Audited patch: `f28c7776fd5c3db6910907ca032952bd6806b219412a57bf890159fd34a3b9e1`

Audit the actual post-application graph against the frozen graph and the
exact patch.  Verify:

1. current graph hash and official graph validation;
2. realized operation inventory `0/1/0/16/21`;
3. exactly the selected open node changed, only by twelve inconclusive
   evidence paths, its reviewed `next_action`, and Round-182 metadata;
4. exactly sixteen rejected-overclaim records were appended and every
   no-change obligation is deeply unchanged;
5. no status, statement, dependency, implication, blocker, cycle, bridge,
   theorem, or exponent drift;
6. operation-derived exact inverse to the frozen graph, including byte and
   SHA-256 equality; and
7. frozen-time replay of the exact patch, using the actual application
   timestamp, reproduces the current graph byte-for-byte.

Check current graph/patch integrity and report the actual update timestamp.
All computation is mechanical control only.

Write only
`controls/postapply_independent_graph_reverse_audit.md`, using the
seven-section contract and an explicit GREEN/REPAIR verdict.  Do not edit
the graph, patch, reports, reviews, synthesis, lifecycle, proof draft,
validation matrix, or any shared-state file.
