# Round 194 independent preapplication State Patch reverse/replay audit

- Campaign: `full-proof-round191-193-strategy-literature-review`
- State Patch:
  `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/state_patch.json`
- Current State Patch SHA-256:
  `918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`
- Frozen starting-graph SHA-256:
  `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`
- Audit mode: bounded read-only canonical validation, apply, inverse, and
  replay; no graph, patch, synthesis, validation-matrix, or proof-draft
  mutation and no full test suite

## 1. Result

**Verdict: PASS.**  This audit was rerun from scratch after the patch's
`mfrak` repair.  The current patch has exact
create/update/correct-rejected/reject/no-change scope

`0 / 1 / 0 / 20 / 26`.

The sole updated obligation remains `open`.  All 26 protected
`no_change` obligations are deeply identical after simulated application,
all 20 rejected-claim IDs are genuinely new, and all 10 unique evidence
paths exist as nonempty files.  The stored inverse recovers the canonical
starting graph byte-for-byte.  Reapplication with identical frozen
canonical inputs is deterministic.

With the applicator's sole nondeterministic field frozen to
`last_updated_at = 2026-08-30T12:34:56`, the canonical postimage and replay
SHA-256 are both

`434ad6433ac7ce2b8ca20ba3998acedf31d8e55456b8ef2254d8bfc852b6655b`.

The inverse/recovered SHA-256 is exactly

`cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`.

## 2. Exact statement and hypotheses

Let \(G_0\) be `state/proof_obligations.yml` at the frozen hash above and
let \(P\) be the repaired Round-194 patch at the current patch hash.  The
canonical application parameters tested were:

- `round_index = 194`;
- judge reference
  `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`;
- frozen audit timestamp `2026-08-30T12:34:56`.

The timestamp is frozen only to test byte-deterministic replay.  A future
real application will generate its own `last_updated_at`, so its postimage
hash is expected to differ unless it uses the same timestamp.  This does
not affect scope, validation, or inverse recovery.

The bounded audit required:

1. exact normalized operation counts and unique/disjoint IDs;
2. exact existence and classification of every evidence path;
3. preservation of the updated owner's `open` status and every
   `no_change` node;
4. noncollision and correct judge evidence for every new rejected record;
5. exact agreement of `restore_next_action` and `restore_metadata` with
   \(G_0\);
6. exact inverse recovery of \(G_0\); and
7. deterministic canonical apply/inverse/replay under identical frozen
   inputs.

## 3. Proof and derivation

### 3.1 Frozen inputs and official validation

The live graph contains 394 obligations and 1,712 rejected-claim records.
Its 2,125,317 raw bytes and repository-canonical serialization both have
SHA-256

`cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`.

The repaired patch is 13,624 bytes.  Its raw and canonical JSON hashes are
both

`918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`.

The repository dry run returns exactly `Patch OK`.  Direct calls to
`validate_graph` and `validate_patch_against_graph` return no issue.

### 3.2 Exact operation scope

Parsing with the repository's `_patch_ops` normalization gives:

| Operation | Count | Unique IDs | Canonical effect |
|---|---:|---:|---|
| `create` | 0 | 0 | No obligation or dependency is created. |
| `update` | 1 | 1 | Update only `M9-M1-hard-top-high-radical-small-t-residual-estimate`. |
| `correct_rejected` | 0 | 0 | No existing rejected record is corrected. |
| `reject` | 20 | 20 | Append 20 new rejected-overclaim records. |
| `no_change` | 26 | 26 | Record protected scope only; mutate no node. |

Every operation family is internally unique, and the ID families are
pairwise disjoint.  The 20 rejected IDs are absent from both the 394 live
obligations and the 1,712 starting rejected records.  Canonical application
therefore appends records; it does not set any obligation's status to
`rejected` and does not overwrite a prior rejection.

### 3.3 Evidence and judge-reference audit

The update adds 10 inconclusive evidence paths.  They are 10 distinct
workspace-relative paths, none was already present in the owner's
inconclusive bucket, and all 10 resolve inside the repository to nonempty
files.  There is no positive or negative evidence addition.

The exact judge reference is one of those 10 paths:

`rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`.

It exists, is nonempty, and has SHA-256

`2a18f707f9f02caef8baf07909fb8719cdd7f6063112637ca47bbbc73cc6a13b`.

Because `_merge_evidence` preserves uniqueness, passing the same path as
`judge_ref` does not duplicate it on the updated owner.  Each of the 20
new rejected records receives exactly the one-element evidence list
containing that judge reference.

### 3.4 Mutation boundary and protected nodes

Before application the sole owner has status `open`; afterward it still
has status `open`.  Its complete changed-key set is exactly

`{evidence, next_action, last_updated_round, last_updated_at}`.

No status, dependency, implication, blocker, statement, title, type,
track, positive evidence, or negative evidence changes.  All 393 other
pre-existing obligation dictionaries are deeply equal before and after
application.  In particular, the declared 26 `no_change` nodes pass
26/26 exact deep equalities.

The prefix of 1,712 pre-existing rejected-claim records is also deeply
unchanged.  The simulated postimage has 394 obligations and 1,732 rejected
records; its only new rejected-state objects are the specified 20 records.

### 3.5 Reversibility payload

The stored `restore_next_action` is character-for-character equal to the
starting owner's next action.  The stored metadata is exact:

- `last_updated_round: 193`;
- `last_updated_at: 2026-08-30T02:10:41`.

The declared inverse covers every canonical mutation:

1. remove the 20 new rejected records;
2. remove the 10 `evidence_added.inconclusive` values from the updated
   owner;
3. restore the prior `next_action`; and
4. restore the two prior last-update metadata fields.

The judge-reference addition is fully covered: it is one of the 10 removed
owner evidence values, and its rejected-record copies disappear with their
new records.  No created node, dependency, status, implication, or blocker
needs inverse handling.

Applying this inverse in memory gives deep object equality with \(G_0\).
The canonical inverse dump is 2,125,317 bytes and has SHA-256

`cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`,

exactly the raw starting graph hash.

### 3.6 Canonical apply/inverse/replay

The repository's `apply_state_patch` was run only on in-memory objects.
Its returned arrays reproduce the exact patch order and counts
`0/1/0/20/26`, and its deep-copy contract leaves the input graph
unchanged.

At the frozen audit timestamp, the postimage is 2,136,028 canonical bytes
with SHA-256

`434ad6433ac7ce2b8ca20ba3998acedf31d8e55456b8ef2254d8bfc852b6655b`.

Two independent applications from \(G_0\) are deeply equal.  The declared
inverse returns exactly to \(G_0\), and reapplying \(P\) to that recovered
preimage returns a graph deeply and bytewise equal to the first postimage,
with replay SHA-256

`434ad6433ac7ce2b8ca20ba3998acedf31d8e55456b8ef2254d8bfc852b6655b`.

Graph validation returns zero issues for the start, postimage, inverse, and
replay.

### 3.7 Judge and repaired-text agreement

The repaired `next_action` now uses the literal text
`H_B \mathfrak m` and `Y/(H_B \mathfrak m)`; the stale `mfrak` text is
absent.  It freezes the complete Round-193 \(P_2\) lower-close/upper-far
physical complement as the sole Round-195 objective, with the fixed-packet
and outer targets, both \(T\)-branches, physical mask commutator, one outer
real part, full deficit recovery, and the conductor's stop rules.  This
agrees with the cited adjudication and `synthesis.md` at SHA-256

`b90bd466e048d64d87e49b669591995358975c9eb1b37eadbc1d2aab1446b4e4`.

The patch also records that Boolean first-failure order does not force
\(P_1\) first and that report agreement cannot prove \(P_2\).  The judge's
strategy choice therefore does not masquerade as an analytic promotion.
The round assessment and every protected reason leave all analytic
statuses, parents, endpoints, bridges, global theorems, and exponents
unchanged.

## 4. First doubtful or unproved step

None within the assigned patch-scope and reverse/replay audit.  The only
qualification is the canonical applicator's wall-clock timestamp: the
prospective postimage hash is not uniquely encoded by the patch.  The
reported replay hash is a reproducibility witness under the explicitly
frozen timestamp, while the recovered preimage hash is unconditional and
exact.

This control does not re-prove mathematical claims inside the evidence
artifacts.  It verifies patch validity, scope, path existence, judge
alignment, reversibility, and canonical graph semantics only.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Current patch SHA-256 | **PASS:** `918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`. |
| Starting graph hash | **PASS:** raw and canonical `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`. |
| Official dry run | **PASS:** `Patch OK`. |
| Exact operation scope | **PASS:** `0/1/0/20/26`; all IDs unique and disjoint. |
| Updated owner | **PASS:** exists and remains `open`; exactly four keys change. |
| Created dependency status | **PASS/NOT APPLICABLE:** no node or dependency is created. |
| Evidence paths | **PASS:** 10/10 unique paths exist, are nonempty, and are newly added. |
| Judge reference | **PASS:** exact adjudication path is added once to the owner and all 20 new rejects. |
| Rejected IDs | **PASS:** 20/20 unique and absent from both starting ID domains. |
| No-change IDs | **PASS:** 26/26 exist and are deeply equal after application. |
| All other obligations | **PASS:** 393/393 complete dictionaries are deeply equal. |
| Rejected-record prefix | **PASS:** all 1,712 pre-existing records remain deeply equal. |
| Reversibility metadata | **PASS:** prior next action and both metadata fields match \(G_0\) exactly. |
| Canonical inverse | **PASS:** recovered hash `cbbb68b5...cdd9e`. |
| Canonical replay | **PASS:** fixed-time replay hash `434ad643...b6655b`. |
| Repaired formula | **PASS:** escaped `\mathfrak m` appears in both required locations; `mfrak` is absent. |
| Shared-state mutation | **PASS:** none. |
| Full test suite | **NOT RUN, as required.** |

## 6. Dependencies and exact artifacts used

This audit used:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/state_patch.json`;
5. `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`;
6. `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/synthesis.md`;
7. `math_collab/proof_obligations.py`;
8. `math_collab/validate_state_patch.py`; and
9. the 10 patch-enumerated evidence paths, checked for exact existence,
   nonzero size, and judge-reference consistency.

No web source, numerical theorem experiment, graph application, graph
write, patch write, validation-matrix write, proof-draft write, synthesis
write, or full test suite was used.

## 7. Recommended state effect

Accept this independent preapplication gate as **PASS** for repaired State
Patch SHA-256
`918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`.
The patch lawfully updates inconclusive evidence and the next action of one
already-open owner, appends 20 new rejected overclaims, and preserves all
26 declared no-change obligations plus every other existing obligation.
The stated inverse is complete and exact.  This audit itself authorizes and
performs no shared-state mutation.
