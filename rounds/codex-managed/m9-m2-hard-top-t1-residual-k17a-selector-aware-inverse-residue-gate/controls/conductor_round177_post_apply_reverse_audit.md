# Round 177 post-application reverse audit

## 1. Result

**GREEN.**

The applied Round-177 graph is the exact canonical result of the reviewed State Patch. Its byte SHA-256 is
47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7,
and the repository graph validator returns Graph OK.

The application has exactly one create, four updates, sixteen new rejected-claim records, and eighteen no-change decisions. The declared inverse canonically recovers starting hash
e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8.
A timestamp-controlled reapplication is object-identical and byte-identical to the authoritative current graph and recovers current hash
47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7.
There is no patch-local dependency-SCC or normalized-implication-SCC delta.

## 2. Exact statement and hypotheses

Let G1 be the current canonical state/proof_obligations.yml, P177 the current Round-177 state_patch.json with SHA-256
35c3b85ace8693be59d1da4dfbabd23fb2b834a0899afa1172b2e99098e1b9b8,
and G0 the in-memory graph obtained by applying P177's declared inverse to G1.

The audit fixes the observed application controls:

- round index: 177;
- application timestamp: 2026-08-27T10:20:58; and
- judge reference:
  rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reviews/conductor_round177_adjudication.md.

Under those controls, the claim is:

1. G1 differs from G0 only by the exact 1/4/16/18 operation ledger of P177 and the repository applicator's documented metadata and judge-reference insertions;
2. canonical serialization of G0 has the patch's starting hash;
3. controlled application of P177 to G0 reproduces G1 exactly; and
4. the dependency-only and dependency-plus-normalized-implication strongly connected component sets are unchanged from G0 to G1.

## 3. Proof or derivation

### 3.1 Exact applied effect

The current graph has 380 obligations and 1,456 rejected claims. Removing the one created obligation and the sixteen patch-created rejected claims gives the starting totals 379 and 1,440. The sole obligation-status change is:

| Status | G0 | G1 | Delta |
|---|---:|---:|---:|
| proved_internal | 301 | 302 | +1 |
| open | 33 | 33 | 0 |
| derived_under_assumptions | 15 | 15 | 0 |
| proved_external_dependency | 19 | 19 | 0 |
| proposed | 7 | 7 | 0 |
| diagnostic_only | 2 | 2 | 0 |
| rejected obligations | 2 | 2 | 0 |

The created obligation is exactly
M9-M2-hard-top-t1-residual-k17a-primitive-alias-conductor-reduction.
After removing application metadata and the applicator-added judge reference, every field is exactly the create object in P177. Its current evidence ledger is sixteen positive paths, zero negative paths, and one inconclusive judge-reference path. The adjudication path appears in the positive packet supplied by the patch and in the inconclusive bucket supplied by the applicator; this cross-bucket repetition is expected application provenance, not an accidental duplicate within either bucket.

The four updates are exact:

| Updated obligation | New evidence | New dependency | Other changed fields |
|---|---:|---:|---|
| M9-M2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-reduction | 5, each once | 0 | next_action and application metadata |
| M9-M2-hard-top-t1-residual-determinant-endpoint-polylog-shift-reduction | 5, each once | 0 | next_action and application metadata |
| M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction | 5, each once | 0 | next_action and application metadata |
| M9-M2-top-endpoint-signed-cone | 5, each once | 1, exactly the new reduction | next_action and application metadata |

Thus the updates add exactly twenty evidence entries and one dependency entry. Each updated object's next action equals P177, and every one has last_updated_round 177 and last_updated_at 2026-08-27T10:20:58. The first three statuses remain proved_internal; the top signed-cone owner remains open. No owner, title, statement, implication, blocker, required output, or other field changed.

All sixteen new rejected-claim records are exact. Each has the patch ID and reason, round 177, timestamp 2026-08-27T10:20:58, and the adjudication as its sole evidence path. None replaced an obligation or an older rejected claim. All eighteen no-change objects are byte-logically identical between G0 and G1. Every obligation outside the create and four update IDs is likewise identical.

### 3.2 Canonical inverse

The inverse was executed entirely in memory:

1. delete the created obligation;
2. remove the five added evidence values from each updated obligation;
3. remove the sole added top-owner dependency;
4. restore the four next actions and the eight saved last-updated scalar values;
5. delete the sixteen appended rejected-claim records; and
6. serialize with the repository's canonical graph serializer.

The inverse graph has zero graph-validation issues. P177 has zero validation issues against that graph. Its canonical SHA-256 is exactly
e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8,
equal to starting_graph_sha256. This byte equality proves that no unrecorded mutation remains after inversion.

### 3.3 Timestamp-controlled reapplication

The repository applicator was then run in memory on G0 with round index 177, judge reference equal to the conductor adjudication, and its clock fixed at 2026-08-27T10:20:58. It reported exactly 1 create, 4 updates, 16 rejects, and 18 no-change records.

The reapplied graph equals G1 as a structured object. Its canonical bytes equal the authoritative state/proof_obligations.yml bytes. Its SHA-256 is exactly
47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7.
This closes the forward/reverse round trip at both object and byte levels.

### 3.4 SCC and implication audit

The dependency-edge count rises from 1,342 to 1,344, exactly because the created node has one prerequisite and the top owner receives one provenance dependency. Despite those two intended edges, the dependency-only nontrivial SCC set is identical before and after: the same three inherited two-node components and no new component.

For implication normalization, every statement A implies B is represented by prerequisite edge B to A. Under this convention, the before/after nontrivial SCC sets are again identical: the three inherited dependency components plus the inherited
M9-M2-LFM-endpoint-degeneracy / M9-endpoint-uniformity component.

The implication-edge count is 325 both before and after. The created node has empty implies, and no update changes implies. In the dependency-only graph the new node reaches 24 ancestors and the top owner reaches 47, with neither reaching itself. In the normalized graph those counts are 29 and 53, again with no self-return. Therefore both the patch-local SCC delta and implication delta are exactly zero.

## 4. First doubtful or unproved step

There is no doubtful State-Patch application, inverse, metadata, or cycle step.

The first unproved mathematical step remains the literal high-reduced-conductor estimate (177.K34), or the stronger aliaswise estimate (177.K35). The applied graph leaves those estimates, complete K17a, the hard-TOP and physical parents, all bridges, and all exponent improvements open.

The four inherited normalized SCCs remain global graph debt. They are unchanged by Round 177 and do not weaken this patch-local GREEN verdict.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Authoritative current hash | GREEN: exact 47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7. |
| Canonical current serialization | GREEN: serializer output is byte-identical to the file. |
| Current graph validation | GREEN: Graph OK. |
| Operation counts | GREEN: exact 1/4/16/18. |
| Created node | GREEN: exact patch fields plus round, timestamp, and judge reference. |
| Four updates | GREEN: exact evidence, dependency, next_action, and metadata changes only. |
| Sixteen rejects | GREEN: exact IDs, reasons, evidence, round, and timestamp. |
| Eighteen no-change owners | GREEN: unchanged. |
| Status ledger | GREEN: only proved_internal increases by one; open remains 33. |
| Canonical inverse | GREEN: exact starting hash e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8. |
| Reverse graph and patch validation | GREEN: zero issues. |
| Controlled reapplication | GREEN: exact current object, bytes, counts, and hash. |
| Dependency SCC delta | GREEN: zero; three inherited components before and after. |
| Normalized implication SCC delta | GREEN: zero; four inherited components before and after. |
| Implication-edge delta | GREEN: 325 to 325. |
| Parent and exponent quarantine | GREEN: unchanged. |

## 6. Dependencies and exact artifacts used

This audit used exactly:

1. state/proof_obligations.yml;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/state_patch.json;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reviews/state_patch_scope_cycle_review.md;
4. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reviews/final_state_patch_post_path_verification.md;
5. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reviews/conductor_round177_adjudication.md;
6. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/controls/conductor_round177_controls.md; and
7. math_collab/proof_obligations.py.

All inverse and reapplication work was in memory. No graph, patch, kernel, synthesis, review, or other shared-state artifact was edited.

## 7. Recommended state effect

**Retain the applied Round-177 graph with no corrective patch.** Record this audit as the post-application reversibility and cycle control. Do not infer any closure beyond the single proved-internal primitive-alias-conductor reduction, and preserve the open high-conductor gate, parents, bridges, and exponent owners.
