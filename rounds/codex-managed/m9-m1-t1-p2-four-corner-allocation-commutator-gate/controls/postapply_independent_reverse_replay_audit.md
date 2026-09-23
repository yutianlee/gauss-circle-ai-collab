# Round 197 post-apply independent reverse/replay audit

## 1. Result

**PASS.**  The final authoritative graph at SHA256

`8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69`

reverses exactly to the declared starting graph at SHA256

`B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`

under the final State Patch at SHA256

`A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`.

Replay through the current repository applicator reproduces every
mathematical and evidence field of the authoritative graph.  Before actual
metadata normalization it differs only in the created node's timestamp:
the original application time is `2026-08-31T00:13:15`, whereas the later
hygiene correction records `2026-08-31T00:16:13`.  Normalizing that one
metadata field reproduces the final live object and final live hash exactly.
An independent normalized replay gives the same result.  No shared-state
file was edited.

## 2. Exact statement and hypotheses

Let (G_1) be the parsed final live `state/proof_obligations.yml`, let (P)
be the parsed final `state_patch.json`, and let (R_P) perform the inverse
declared in `P.reversibility`.  The actual metadata are

| datum | actual value |
|---|---|
| application round | `197` |
| update/rejection application timestamp | `2026-08-31T00:13:15` |
| created-node hygiene timestamp | `2026-08-31T00:16:13` |
| caller `judge_ref` | `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_adjudication.md` |

Then:

1. (R_P(G_1)) serializes to the exact starting hash above;
2. applying (P) to (R_P(G_1)) with round 197, the original application
   timestamp, and the actual `judge_ref` reproduces (G_1) except for the
   created node's later hygiene timestamp;
3. replacing only that replayed timestamp by its actual hygiene timestamp
   gives (G_1) exactly;
4. the only changed pre-existing obligation is
   `M9-M1-hard-top-high-radical-small-t-residual-estimate`;
5. the old rejected-claim list is an exact ordered prefix of the final list;
   and
6. all dependency, evidence, rejection, and `no_change` effects have exactly
   the patch footprint.

The current applicator's caller-evidence guard is part of the replay
hypothesis: when `judge_ref` is already present in any evidence bucket, it is
not inserted again as inconclusive evidence on a created node.

## 3. Proof or derivation

### Final ledger and hygiene state

The final hashes equal the values above, and the patch's
`starting_graph_sha256` equals the declared starting hash.  The operation
ledger is exactly

| operation | count |
|---|---:|
| `create` | 1 |
| `update` | 1 |
| `correct_rejected` | 0 |
| `reject` | 22 |
| `no_change` | 28 |

The final graph has 396 obligations and 1797 rejected claims.  The created
node is

`M9-M1-hard-top-t1-rho-large-P2-common-cell-allocation-commutator-sector`.

After removing only its round and timestamp metadata, this node equals the
patch's `create[0]` payload exactly.  Its evidence counts are 14 positive, 0
negative, and 11 inconclusive.  Each bucket is internally duplicate-free,
all three pairwise bucket intersections are empty, and
`conductor_round197_adjudication.md` occurs only in `positive`.  The claimed
post-apply hygiene correction is therefore present exactly: the duplicate
inconclusive classification is gone, while the already-positive
adjudication remains.

The created node has the later hygiene timestamp `00:16:13`.  The updated
pre-existing node and every rejected suffix record retain the original
application timestamp `00:13:15`.  This is a metadata-only distinction; the
created mathematical payload equals the final patch payload exactly.

### Exact reverse

On an in-memory copy of (G_1), I executed only the declared inverse:

1. remove the one created obligation;
2. remove the exact 22-record rejected-claim suffix;
3. remove the sole dependency suffix from the updated obligation;
4. remove its exact 25-entry inconclusive-evidence suffix;
5. restore its recorded old `next_action`; and
6. restore `last_updated_round=196` and
   `last_updated_at=2026-08-30T12:00:58`.

The recovered graph has 395 obligations and 1775 rejected claims.  Its exact
repository serialization has SHA256

`B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`.

Thus reversal recovers the cryptographically identified pre-apply graph,
not merely an object with matching counts.  The recovered graph validates
with zero issues, and the patch validates against it with zero issues.

### Exact final footprint

Comparison with the recovered starting object finds one and only one changed
pre-existing obligation:

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

Its changed fields are exactly `dependencies`, `evidence`, `next_action`,
`last_updated_round`, and `last_updated_at`.  Its old 11-entry dependency
list is an exact prefix of the final list; the sole suffix is the new
Round-197 node id.  Its old 250-entry inconclusive-evidence list is an exact
prefix of the final 275-entry list; the ordered 25-entry suffix equals
`update[0].evidence_added.inconclusive` exactly.  Positive and negative
evidence remain unchanged.

All 28 `no_change` obligation objects are exactly equal before and after.
All top-level fields other than `proof_obligations` and `rejected_claims`
are exactly equal.  The 1775 recovered rejected records form an exact
ordered prefix of the final list.  The 22-record suffix is in patch order;
every record has exactly the requested id and reason, round 197, timestamp
`00:13:15`, and the one-element actual caller-evidence list.

### Actual-metadata-normalized replay

I replayed the patch from the recovered object through the current
`apply_state_patch`, fixing the runtime clock to the actual application time
`00:13:15` and supplying the actual caller reference.  The repaired
cross-bucket guard recognized that this reference was already positive and
did not add an inconclusive duplicate.  The replayed graph matches the final
graph everywhere except the created node's `last_updated_at`: replay gives
the application time, while the final graph correctly records the later
hygiene time.

Changing only that field to `2026-08-31T00:16:13` produces exact object
equality with (G_1) and serialized SHA256

`8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69`.

A separate direct implementation of the replay, including the evidence
hygiene guard and the two actual timestamps, also equals (G_1) exactly.

## 4. First doubtful or unproved step

There is no unresolved mechanical step in the reverse/normalized-replay
claim.  The first unproved boundary is semantic: this control does not
re-prove the mathematical theorem in the created node or independently
reclassify its evidence.  It verifies that the already adjudicated payload,
scope, and hygiene classification are represented exactly.

The patch alone does not encode the later correction timestamp.  Therefore
a byte-identical historical replay necessarily uses the actual two-stage
metadata normalization documented above.  This is not a graph defect: the
timestamp is non-mathematical, the final evidence buckets are hygienic, and
the exact inverse is independent of the created node's timestamp because
that node is removed wholesale.

## 5. Required control test and outcome

| control | outcome |
|---|---|
| final graph hash and validation | **PASS**, exact hash and zero issues |
| reverse actual create/reject/dependency/evidence effects | **PASS** |
| recovered starting serialization | **PASS**, exact `B9B95784...` hash |
| rejected-prefix preservation | **PASS**, exact 1775-record prefix and 22-record suffix |
| target evidence/dependency suffixes | **PASS**, exact order and content |
| pre-existing-node mutation footprint | **PASS**, exactly one node and five fields |
| all 28 `no_change` records | **PASS**, exact object equality |
| created evidence hygiene | **PASS**, 14/0/11 and no cross-bucket overlap |
| repository replay before timestamp normalization | **PASS**, only the expected created-node timestamp differs |
| actual-metadata-normalized repository replay | **PASS**, exact final object/hash |
| independent normalized replay | **PASS**, exact final object/hash |

All reversal and replay operations ran on in-memory copies.  The final live
graph remained unchanged throughout the audit.

## 6. Dependencies and exact artifacts used

The audit used only:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `state/proof_obligations.yml` at SHA256
   `8AEA2AB5B088A0B29A434347FFC4509C70E79F53E450814920E3C83165A1AB69`;
4. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/state_patch.json`
   at SHA256
   `A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`;
5. `math_collab/proof_obligations.py` at SHA256
   `B9331F52552A65FA56614C647B8ABAE331102E6AACDF5E6AF949D226E50706B2`;
6. `math_collab/validate_state_patch.py` at SHA256
   `CFA914C54BFA172CC94354DC7E904E866D4E69C96CD8BE7BFBF68B5A295080E8`;
7. `math_collab/validate_round.py`; and
8. `tests/test_proof_obligations.py`.

The caller-reference path was checked for exact propagation and existence,
but its content was not used as mathematical authority.  No candidate,
kernel, synthesis, sibling report, or earlier control was used to establish
this post-apply mechanical result.

## 7. Recommended state effect

**Retain the final applied graph unchanged.**  Verdict: **PASS**, not
`REPAIR`.  The final graph has the intended hygienic evidence
classification, exact operation footprint, exact rejected prefix and
suffix, exact reversibility, and exact actual-metadata-normalized replay.
No corrective graph patch is needed.
