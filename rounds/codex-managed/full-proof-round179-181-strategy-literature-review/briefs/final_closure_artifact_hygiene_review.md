# Task Brief: Round 182 final closure and artifact-hygiene review

- Campaign: `full-proof-round179-181-strategy-literature-review`
- Round: `182`
- Role: independent final campaign-closure, state-consistency, and artifact-hygiene reviewer
- Starting graph: `fec130bc66641cbdad18c832de10077a7825f1caaf5d10170a67ef65c0b27196`
- Closed graph: `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`

Audit the complete current Round-182 packet and lifecycle after the GREEN
post-application reverse audit.  Verify:

1. campaign manifest and plan are `complete`, all three discovery tasks are
   `completed`, and the closing label/effect/hash are exact;
2. round ledger has Round 182 `closed`, all tasks completed,
   `active_round: null`, the exact closing assessment, and next round 183;
3. current/next-round, current-state, project-summary, human-directive,
   last-validation, validation-report, and validation-matrix files agree on
   the exact selected theorem, graph hash, patch effect, owner scope, and
   unchanged exponent ledger;
4. the proof draft has no Round-182 analytic promotion and requires no
   strategy-only edit;
5. the patch, preapply inverse, postapply inverse/frozen-time replay,
   source repair chain, dependency/power seam, blind post-unmask seam,
   controls, adjudication, and synthesis are internally consistent;
6. every relevant JSON/JSON-compatible state file parses, campaign and
   graph validators pass, compilation and all repository tests pass; and
7. all Round-182 and modified lifecycle artifacts are strict UTF-8, have no
   forbidden control/replacement characters or trailing whitespace, and
   have balanced Markdown fences, code spans, TeX delimiters/environments,
   braces, and final newlines.

Recompute the current graph and key artifact hashes.  Computation is
mechanical control only.  If any defect exists, report its first exact file
and line and return REPAIR.

Write only
`reviews/final_closure_artifact_hygiene_review.md`, using the seven-section
contract and an explicit GREEN/REPAIR verdict.  Do not edit the graph,
patch, reports, reviews by other authors, controls, synthesis, lifecycle,
proof draft, validation artifacts, or any shared-state file.
