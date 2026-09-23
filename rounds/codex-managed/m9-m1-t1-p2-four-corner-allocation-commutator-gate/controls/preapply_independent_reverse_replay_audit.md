# Round 197 pre-apply independent reverse/replay audit

## 1. Result

**GREEN.**  The final State Patch with SHA256

`A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`

is mechanically valid against the live graph with SHA256

`B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`.

An independent in-memory implementation of the patch operations produced
exactly the same graph object as the repository applicator.  The declared
inverse recovered the live graph exactly, including its serialized SHA256,
and a deterministic replay reproduced the first simulated application
exactly.  No file in `state/` was written.

The operation ledger is exactly

| operation | count |
|---|---:|
| `create` | 1 |
| `update` | 1 |
| `correct_rejected` | 0 |
| `reject` | 22 |
| `no_change` | 28 |

The simulated counts are (395\to396) proof obligations and
(1775\to1797) rejected-claim records.

## 2. Exact statement and hypotheses

Let (G_0) be the parsed object in `state/proof_obligations.yml` at the live
hash above, and let (P) be the parsed final `state_patch.json` at the hash
above.  Apply (P) with `round_index=197` under the semantics of
`math_collab.proof_obligations.apply_state_patch`.  For byte-comparable
apply/inverse/replay testing, hold the applicator clock fixed; the chosen
clock value is immaterial.

Then:

1. the independent and repository applications agree exactly;
2. the only changed pre-existing obligation is
   `M9-M1-hard-top-high-radical-small-t-residual-estimate`;
3. its only changed fields are `dependencies`, `evidence`, `next_action`,
   `last_updated_round`, and `last_updated_at`;
4. the original rejected-claim list is an exact ordered prefix of the
   result, followed by exactly the 22 requested records;
5. all 28 `no_change` ids are distinct, exist in (G_0), and remain
   byte-for-byte unchanged;
6. executing the inverse prescribed in `reversibility` gives exactly
   (G_0); and
7. replaying (P) from that inverse gives exactly the first applied object.

The direct raw-patch application tested here supplies no external
`judge_ref`.  If a caller supplies one, the applicator injects it only into
the newly created obligation and newly created rejected records.  Those
records are wholly removed by the declared inverse, so this optional caller
feature cannot change the pre-existing-node footprint or obstruct exact
reversal.  Exact replay must, as usual, reuse the same clock value and the
same caller arguments.

## 3. Proof or derivation

### Hash and referential checks

The patch's `starting_graph_sha256` equals the live graph hash exactly.  The
created id is absent from both live obligations and live rejected claims.
The update id exists.  Every rejected id is new to both collections.  All 28
`no_change` ids exist, are unique, and are disjoint from the create, update,
and reject operation sets.  The newly added protection is present exactly
once:

`M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors` remains
`no_change`, with the explicit statement that the accepted Round-195
safe/open packet theorem and historical statement are unchanged and that no
reverse dependency is added.

The repository validator reports `Patch OK`.  Validation of the live graph,
the patch against the live graph, and the simulated applied graph returned
zero issues in all three cases.

### Independent apply and mutation footprint

I implemented the five operation classes independently on a deep copy:
append the created obligation; append-uniquely the requested dependency and
evidence; replace the requested `next_action`; append the 22 new rejection
records; and treat `no_change` as a zero-mutation ledger.  Round and timestamp
metadata were then added exactly where the repository applicator adds them.
The resulting object was exactly equal to the object returned by
`apply_state_patch` under the same fixed clock.

Comparison by pre-existing obligation id found one and only one mutation:

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

Every other pre-existing obligation is exactly unchanged.  Every top-level
field other than `proof_obligations` and `rejected_claims` is exactly
unchanged, and every old rejected-claim record is exactly unchanged.

For the updated obligation, the old dependency list is an exact prefix and
the sole ordered suffix is

`M9-M1-hard-top-t1-rho-large-P2-common-cell-allocation-commutator-sector`.

The old `inconclusive` evidence list (250 entries) is an exact prefix and the
ordered suffix is exactly the 25 entries in
`update[0].evidence_added.inconclusive`, giving 275 entries.  All 25 are
distinct and absent from the old list.  The old positive and negative
evidence lists are unchanged.  The 25-entry suffix is exactly the created
node's 14 positive paths followed by its 11 inconclusive paths.

The created node itself has evidence counts

| class | count |
|---|---:|
| positive | 14 |
| negative | 0 |
| inconclusive | 11 |

Each class is internally duplicate-free, and all three pairwise class
intersections are empty.  Thus the earlier cross-class hygiene defect is not
present in this final hash.  Every referenced evidence file exists.  The
22 appended rejected-claim records occur in patch order and have exactly the
requested id and reason plus the applicator's Round-197 timestamp metadata;
the entire 1775-record live list is preserved as their exact prefix.

### Exact inverse and replay

Starting from the simulated applied graph, I performed only the operations
declared by `reversibility`:

1. remove the one created obligation;
2. remove the 22 introduced rejected-claim records;
3. remove the one `dependencies_added` value;
4. remove the 25 `evidence_added.inconclusive` values;
5. restore the recorded `next_action`; and
6. restore `last_updated_round=196` and
   `last_updated_at=2026-08-30T12:00:58`.

The restored object equals (G_0) exactly.  Serializing it with the
repository serializer gives SHA256
`B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`,
the live file hash.  Reapplying the patch from this restored object with the
same fixed clock reproduced the first applied object exactly.  This is an
exact object and serialization test, not merely a comparison of counts.

## 4. First doubtful or unproved step

There is no unresolved mechanical step in the apply/inverse/replay claim.
The first boundary outside this control is semantic: this audit does not
re-prove the mathematical theorem stored in the created obligation or
re-adjudicate whether each evidence path deserves its positive or
inconclusive label.  It proves only that the already adjudicated payload is
transferred, scoped, reversed, and replayed exactly.

The runtime timestamp is intentionally not predicted.  A later application
will use its actual current timestamp; the inverse remains exact because it
removes created records and restores the sole pre-existing node's original
metadata.  Byte-identical replay of an applied state necessarily requires
the same timestamp, which the deterministic control supplied.

## 5. Required control test and outcome

The required control was a dry, in-memory four-stage test:

| control | outcome |
|---|---|
| repository patch validation | **PASS**, zero issues |
| repository apply versus independent apply | **PASS**, exact object equality |
| rejected-prefix and evidence/dependency suffix checks | **PASS**, exact order and content |
| intended pre-existing mutation check | **PASS**, exactly one named node and five named fields |
| declared inverse | **PASS**, exact baseline object and live serialized hash |
| replay after inverse | **PASS**, exact first-applied object |
| post-apply graph validation | **PASS**, zero issues |

All tests ran on copies.  The patch was not applied to the live graph.

## 6. Dependencies and exact artifacts used

Only the following artifacts were used for this audit:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `state/proof_obligations.yml` at SHA256
   `B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`;
4. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/state_patch.json`
   at SHA256
   `A28050A9D157D7D956DA336BBDEAD4296C88EB1B8A3DEFEB90495B1B37CA2068`;
5. `math_collab/proof_obligations.py`;
6. `math_collab/validate_state_patch.py`;
7. `math_collab/validate_round.py`;
8. the State-Patch tests in `tests/test_proof_obligations.py`.

No candidate, durable-kernel, synthesis, sibling report, or prior control was
used as mathematical authority for this mechanical audit.

## 7. Recommended state effect

**Promote the State Patch to conductor-authorized application.**  Its
mechanical preconditions, scope, ordered suffixes, rejection-prefix
preservation, reversibility, and deterministic replay are all GREEN.  This
report itself makes no graph change; only the conductor may apply the patch
after the remaining protocol gates are green.
