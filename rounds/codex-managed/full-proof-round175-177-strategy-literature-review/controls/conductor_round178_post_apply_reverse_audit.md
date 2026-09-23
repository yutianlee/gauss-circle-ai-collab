# Round 178 canonical post-application reverse audit

- Campaign: `full-proof-round175-177-strategy-literature-review`
- Round: 178
- Role: independent canonical post-application reverse auditor
- Starting graph SHA-256:
  `47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7`
- Reviewed patch SHA-256:
  `654ce2c4a45ce3268fed04a8c95d68e57cef0766bec8c6c7c0bad22096cbc3cd`
- Actual applied graph SHA-256:
  `e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`
- Verdict: **GREEN**

## 1. Result

The authoritative Round-178 graph is the exact canonical result of the
reviewed strategy-only State Patch.  It validates with zero issues, its
canonical serializer output is byte-for-byte equal to the on-disk file, and
its SHA-256 is exactly

`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`.

The applied effect is exactly the reviewed `0/1/0/16/20` ledger: no create,
one update, no corrected rejection, sixteen new rejected-overclaim records,
and twenty declarative no-change records.  The application timestamp is
`2026-08-27T11:49:51`.

An inverse derived from the operation preimages, rather than from an
unreviewed snapshot, recovers a valid canonical graph with 380 obligations
and 1,456 rejected claims.  Its 1,914,347 serialized bytes have exact
SHA-256

`47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7`,

the certified Round-178 starting hash.  Reapplying the patch in memory with
the observed timestamp reproduces the authoritative object, bytes, and
actual hash exactly.  An ordinary reapplication is identical after
normalizing only the seventeen application-generated `last_updated_at`
values.

The authoritative state remained at the actual applied hash before and
after every audit step.  No state file was edited.

## 2. Exact statement and hypotheses

Let (G_1) be the current canonical `state/proof_obligations.yml`, let
(P_{178}) be the reviewed Round-178 `state_patch.json`, and let (G_0) be
the graph obtained by applying the operation-derived inverse to (G_1).
The audit freezes:

1. (H(G_0)=)
   `47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7`;
2. (H(P_{178})=)
   `654ce2c4a45ce3268fed04a8c95d68e57cef0766bec8c6c7c0bad22096cbc3cd`;
3. (H(G_1)=)
   `e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`;
4. round index 178;
5. application timestamp `2026-08-27T11:49:51`; and
6. no judge reference, consistent with the ten declared evidence additions
   and the absence of a judge-evidence field on the sixteen new rejected
   records.

The repository's canonical graph serialization is

`json.dumps(graph, indent=2, ensure_ascii=True) + "\n"`.

The sole updated obligation is

`M9-M2-hard-top-t1-residual-k17a-primitive-alias-conductor-reduction`.

Its exact preimage is independently determined by the Round-177 create
object, the certified Round-177 application metadata
`last_updated_round: 177` and `last_updated_at: 2026-08-27T10:20:58`, and
the Round-177 conductor-adjudication path inserted into
`evidence.inconclusive`.  This reconstruction is the complete preimage
object, including field order under canonical serialization; it is not an
approximation formed from selected scalar fields.

The remaining inverse operations are forced by the reviewed patch:

- remove the ten Round-178 paths appended to the target's inconclusive
  evidence ledger by restoring that complete preimage;
- restore the Round-177 next action and last-updated metadata through the
  same preimage;
- delete exactly the sixteen fresh rejected records, which occupy the final
  sixteen positions in patch order; and
- perform no inverse for `create`, `correct_rejected`, or `no_change`, since
  those classes respectively contain zero, zero, and no mutating operations.

## 3. Proof or derivation

### 3.1 Authoritative applied graph

The actual file contains 380 obligations and 1,472 rejected claims.  It is
strict UTF-8, has no BOM or forbidden control byte, parses as duplicate-free
JSON-compatible state, passes repository graph validation, and is already
in canonical byte form.

The final sixteen rejected records have exactly the sixteen patch IDs in
patch order.  Every record has exactly the patch's `id` and `reason`,
`last_updated_round: 178`, and
`last_updated_at: 2026-08-27T11:49:51`; none has an undeclared evidence
field.  The preceding 1,456 rejected records form the unchanged starting
prefix.

Exactly one obligation differs between (G_0) and (G_1), namely the
declared primitive alias-conductor reduction.  Its changed keys are exactly:

1. `evidence`;
2. `next_action`;
3. `last_updated_round`; and
4. `last_updated_at`.

Its inconclusive evidence count changes from one to eleven, with the ten
reviewed Round-178 paths appended once and in patch order.  Its status
remains `proved_internal`.  Across all 380 obligations there are zero
changes to `status`, `statement_tex`, `dependencies`, `implies`, or
`blockers`.  All twenty `no_change` records are object-identical, as are the
complete protected records for `GC-partial-one-third`,
`GC-external-Li-Yang-theta-star`, `GC-target`, `M9`, `M9-M1`, `M9-M2`,
`Conditional-bridge`, and `GC-global-M1-alternative-bridge`.

### 3.2 Canonical inverse

The inverse was executed entirely in memory:

1. locate the sole updated obligation at its existing list position and
   replace it by the independently reconstructed Round-177 preimage;
2. verify that the last sixteen rejected IDs equal the patch's sixteen
   fresh IDs in exact order; and
3. remove that exact tail while preserving every earlier rejected record
   and its order.

The resulting (G_0) has 380 obligations and 1,456 rejected claims.  It
passes graph validation, and the reviewed patch validates against it with
zero issues.  Canonical serialization produces 1,914,347 bytes and exact
starting SHA-256

`47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7`.

This matches the frozen canonical starting bytes certified by the
pre-application audit and the Round-177 post-application audit.  Therefore
no undeclared Round-178 mutation survives the inverse.

### 3.3 Controlled reapplication

The repository application engine was run on (G_0), in memory only, with
round index 178, no judge reference, and its clock fixed to the observed
`2026-08-27T11:49:51`.  It returned exactly:

- create: 0;
- update: 1;
- correct rejected: 0;
- reject: 16; and
- no change: 20.

The replayed graph equals (G_1) as a structured object.  Its canonical
bytes are byte-for-byte equal to the authoritative file, and its SHA-256 is
exactly
`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`.

A second application using the ordinary wall clock generated a different
timestamp, as expected.  After replacing only the updated obligation's one
Round-178 timestamp and the sixteen new rejected-record timestamps by a
common sentinel in both objects, the ordinary replay and (G_1) are exactly
equal.  Thus reapplication equivalence holds modulo precisely seventeen
generated timestamp values and no substantive field.

### 3.4 Scope and exponent quarantine

Because no status, theorem statement, dependency, implication, or blocker
edge changes, the application cannot promote a theorem or alter a proof
tree.  The new next action selects only the still-unproved aggregate
high-conductor K17a estimate (177.K34), explicitly excludes an in-round
pivot to the stronger (177.K35), and limits any future success to the
residual K17a route pending separate connectors and review.

The exponent ledger remains

\[
 \theta_{\rm internal}=\frac13,
 \qquad
 \theta_{\rm external}=0.3144831759740614\ldots,
 \qquad
 \theta_{\rm target}=\frac14.
\]

The Gauss circle quarter target remains open.

## 4. First doubtful or unproved step

There is no doubtful application, inverse, canonical-serialization,
timestamp, operation-count, or authoritative-hash step.

The first unproved mathematical step remains (177.K34): the required signed
high-reduced-conductor estimate with full literal selectors, physical lifts,
both orientations, endpoints, and the final outer absolute value.  This
post-application audit certifies only that Round 178 recorded that strategy
without promoting the estimate, a parent, a bridge, or an exponent.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| reviewed patch hash | **GREEN:** exact `654ce2...bc3cd` |
| authoritative applied hash | **GREEN:** exact `e04380...d4e27` |
| canonical authoritative bytes | **GREEN:** serializer output equals file |
| authoritative graph validation | **GREEN:** zero issues |
| exact application timestamp | **GREEN:** `2026-08-27T11:49:51` on all 17 generated fields |
| exact operation counts | **GREEN:** `0 / 1 / 0 / 16 / 20` |
| changed obligations | **GREEN:** sole declared update target |
| changed target keys | **GREEN:** evidence, next action, round, timestamp only |
| evidence append | **GREEN:** exact ten paths, one to eleven |
| fresh rejected tail | **GREEN:** exact 16 IDs, reasons, order, round, and timestamp |
| prior rejected prefix | **GREEN:** all 1,456 records identical |
| no-change records | **GREEN:** all 20 object-identical |
| status/statement changes | **NONE** |
| dependency/implication/blocker changes | **NONE** |
| theorem/exponent owner drift | **NONE** |
| preimage derivation | **GREEN:** Round-177 create object plus certified metadata and judge insertion |
| reverse graph validation | **GREEN:** zero issues |
| patch validation on recovered start | **GREEN:** zero issues |
| canonical starting-byte recovery | **GREEN:** 1,914,347 bytes at exact `47c628...609f7` |
| fixed-clock reapplication object equality | **GREEN** |
| fixed-clock reapplication byte equality | **GREEN** |
| fixed-clock reapplication hash | **GREEN:** exact `e04380...d4e27` |
| ordinary replay modulo timestamp | **GREEN:** only 17 generated timestamps differ |
| authoritative state preservation | **GREEN:** actual hash unchanged after audit |

## 6. Dependencies and exact artifacts used

This audit used, read-only:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/state_patch.json`;
4. `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/controls/preapply_independent_reverse_audit.md`;
5. `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/briefs/postapply_reverse_audit.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/state_patch.json` for the complete Round-177 create preimage;
7. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/controls/conductor_round177_post_apply_reverse_audit.md` for the certified Round-177 metadata and judge-reference insertion; and
8. the loader, validator, application, and canonical serializer in
   `math_collab/proof_obligations.py`.

All inverse and replay work existed only as in-memory objects.  No graph,
patch, report, review, synthesis, validation matrix, proof draft, or other
shared-state artifact was edited.

## 7. Recommended state effect

**Retain the applied Round-178 graph with no corrective patch.**  Record this
audit as the canonical post-application reversibility control.  The only
accepted Round-178 state effect remains:

1. ten inconclusive strategy/source artifacts on the already proved
   primitive alias-conductor reduction;
2. the narrowed residual-only (177.K34) Round-179 next action;
3. Round-178 update metadata;
4. sixteen fresh rejected-overclaim records; and
5. twenty explicit no-change decisions.

Do not infer proof of (177.K34), complete K17a, any hard-TOP/BAL/UNBAL or M1
parent, GAR, endpoint uniformity, M9, either bridge, the quarter theorem, or
an exponent improvement.

**Final verdict: GREEN.**
