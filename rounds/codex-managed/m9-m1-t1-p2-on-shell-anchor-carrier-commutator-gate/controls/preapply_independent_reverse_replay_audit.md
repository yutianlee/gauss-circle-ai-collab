# Round 196 pre-apply independent reverse/replay audit

## 1. Result

**PASS.**  The current `state_patch.json` is exactly reversible against the graph whose raw SHA-256 it records.  Its operation counts are

| operation | count |
|---|---:|
| create | 0 |
| update | 2 |
| correct_rejected | 0 |
| reject | 20 |
| no_change | 27 |

There are no duplicate IDs within an operation family, no ID shared by two operation families, and no collision between a new rejection ID and either the starting obligation IDs or the starting rejected-claim IDs.

An independent in-memory apply/reverse/replay at frozen timestamp `2026-08-30T12:34:56` gave

\[
G_0\xrightarrow{P}G_1\xrightarrow{P^{-1}}G_0
\xrightarrow{P}G_1,
\]

with byte-canonical hashes

| graph image | canonical SHA-256 | canonical bytes |
|---|---|---:|
| starting graph `G_0` | `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2` | 2,154,204 |
| frozen-time postimage `G_1` | `c7c8af79af2c6011a101315a016985f2d8764b4e7adeb80b35b359912b34d982` | 2,169,843 |
| reversed graph | `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2` | 2,154,204 |
| frozen-time replay | `c7c8af79af2c6011a101315a016985f2d8764b4e7adeb80b35b359912b34d982` | 2,169,843 |

The reversed canonical byte string is exactly the original raw `state/proof_obligations.yml` byte string.  The replay canonical byte string is exactly the first frozen-time postimage byte string.  Thus recovery is stronger than semantic equality: it is byte-canonical equality.  The only prospective nondeterminism is the apply-time `last_updated_at` value; the patch records the exact old timestamp needed for reversal, so that nondeterminism does not weaken recovery.

## 2. Exact statement and hypotheses

Let `G_0` be the current `state/proof_obligations.yml`, let `P` be the current Round 196 `state_patch.json`, and use the repository implementation `math_collab.proof_obligations.apply_state_patch` with

- `round_index = 196`;
- judge reference `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_adjudication.md`;
- one common frozen diagnostic timestamp `2026-08-30T12:34:56` for the first apply and the replay.

The audited claim is:

1. the raw SHA-256 of `G_0` equals `P.starting_graph_sha256`;
2. `P` passes the repository patch validator;
3. the declared operation counts and all relevant ID-disjointness conditions are correct;
4. apply changes only the two declared obligations and appends exactly the twenty declared rejected-claim records;
5. the `reversibility` payload, together with deletion of the patch-introduced rejection records and evidence values, reconstructs `G_0` exactly;
6. applying `P` again to that reconstruction at the same frozen timestamp reproduces the first postimage exactly;
7. all graph validators pass before apply, after apply, after reverse, and after replay.

This is a structural and byte-recovery audit.  It does not independently prove the mathematical conclusions referenced by the evidence or adjudication artifacts.

## 3. Proof or derivation

### 3.1 Frozen inputs and canonical encoding

The audited patch has raw SHA-256

`013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`

and length 20,244 bytes.  Re-encoding its parsed object by the repository's canonical JSON convention (`indent=2`, ASCII escaping, terminal newline) returns the identical raw byte string.

The audited graph has raw SHA-256

`f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`

and length 2,154,204 bytes.  This equals both `P.starting_graph_sha256` and the SHA-256 of the canonical bytes emitted by `dump_graph`; the raw graph is already canonical.  The official dry validator returned exactly `Patch OK`.

### 3.2 Operation and ID audit

The parsed family sizes are exactly `0/2/0/20/27` for create/update/correct-rejected/reject/no-change.  Strict duplicate-key parsing found no repeated JSON object key.  Set-size checks found no repeated ID within any family and no cross-family ID intersection.

The two update IDs are

1. `M9-M1-hard-top-high-radical-small-t-residual-estimate`;
2. `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`.

Both exist exactly once in the starting obligation list.  The twenty reject IDs are absent from both starting ID namespaces.  All twenty are pairwise distinct.  The twenty-seven no-change IDs all exist exactly once in the starting obligation list.  Independently, the starting graph has 395 pairwise distinct obligation IDs and 1,755 pairwise distinct rejected-claim IDs, with no ID shared across those two graph namespaces.

### 3.3 Evidence and restore-data preconditions

Each update adds the same ordered set of twenty-four paths to its `evidence.inconclusive` bucket.  This intentional repetition across two different owners is not an ID collision.  The audit checked all forty-eight path occurrences: they resolve to twenty-four distinct repository files, every file exists and is nonempty, and the judge reference is included in each owner set.

None of those twenty-four paths was already present in either target's starting `inconclusive` bucket.  Consequently the inverse instruction “remove every `evidence_added` value” is information-preserving here: it cannot delete a pre-patch occurrence.  The repository's unique-append operation also cannot create an accidental duplicate.

For each update, `reversibility.restore_next_action[id]` matches the starting node's `next_action` character for character.  Each matching metadata object equals the starting pair

```yaml
last_updated_round: 195
last_updated_at: '2026-08-30T04:40:21'
```

The adjudication file exists, is nonempty, has length 6,714 bytes, and has SHA-256 `e760c0685789b583e16775fa812320faf608d16775f1abee78d38a610e7ce90d`.

### 3.4 Exact apply boundary

The apply was executed in memory from a freshly parsed copy of `G_0`; the workspace graph was never supplied as an output target.  At the frozen timestamp, each update changes exactly these four top-level fields:

`evidence`, `last_updated_at`, `last_updated_round`, and `next_action`.

The first target remains status `open`; the second remains status `proved_internal`.  No status, statement, hypotheses, dependency, or proved/rejected evidence field is changed.  All 393 non-target pre-existing obligation records, including every one of the twenty-seven no-change nodes, are deeply equal before and after apply.

The pre-existing 1,755 rejected-claim records remain an identical ordered prefix.  The postimage has 1,775 rejected records, and its twenty-record suffix has exactly the patch's reject IDs, reasons, and order.  Each new record has `last_updated_round: 196`, the frozen `last_updated_at`, and evidence exactly equal to the singleton list containing the judge reference.

### 3.5 Inverse construction from recorded data

No inverse data external to `P` were used.  The inverse performed the patch's declared rule:

1. from each updated obligation, remove each value named by that update's `evidence_added.inconclusive` list;
2. restore `next_action` from `reversibility.restore_next_action`;
3. restore `last_updated_round` and `last_updated_at` from `reversibility.restore_metadata`;
4. remove every rejected-claim record whose ID is introduced by `proof_obligations.reject`;
5. perform no create or correct-rejected reversal, because both families are empty;
6. perform no action for the no-change family.

Because the evidence values were absent before apply, the rejection IDs were absent in both starting namespaces, and the old mutable fields are recorded exactly, every changed datum has a unique inverse.  The resulting object is deeply equal to `G_0`; canonical dumping gives 2,154,204 bytes and reproduces the original raw bytes exactly.

### 3.6 Replay and timestamp mechanics

Applying the same patch to the recovered graph with the same frozen timestamp reproduces the first postimage by deep equality and byte equality.  This tests not just the inverse but the adequacy of the recovered preimage for a second actual apply.

In an ordinary real apply, `apply_state_patch` obtains a wall-clock timestamp, so its prospective postimage SHA-256 is not fixed by `P` alone.  The frozen `G_1` hash is therefore a reproducibility witness, not a prediction of the eventual committed postimage hash.  Exact reverse recovery is timestamp-independent: the generated timestamp occurs only on the two updated nodes and twenty new rejection records; the inverse restores the two old timestamps from the patch and deletes the new records wholesale.

### 3.7 Validation closure and non-mutation

Repository graph validation returned no issues for `G_0`, the frozen postimage, the reversed graph, or the replayed postimage.  Patch-structure validation also returned no issues.  A final raw-hash check of the workspace graph after the diagnostic run still returned the starting hash, confirming that the simulation did not mutate shared state.

## 4. First doubtful or unproved step

There is no doubtful step in the recorded inverse on the audited inputs.  Every mutation class is either backed by exact restore data or deletes a record/value proved absent before apply.

The first qualification is only timestamp mechanics: without freezing the wall clock, two forward applications need not have the same postimage bytes.  That does not impair reversal because the old metadata are explicitly recorded and all timestamped new rejection records are removed.  Mathematical correctness of the Round 196 evidence remains outside this control's scope.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| Raw graph hash equals patch anchor | PASS |
| Raw graph equals canonical `dump_graph` bytes | PASS |
| Raw patch equals canonical JSON bytes | PASS |
| Official dry patch validator | PASS: `Patch OK` |
| Operation counts `0/2/0/20/27` | PASS |
| Duplicate JSON keys | PASS: none |
| Duplicate IDs within operation families | PASS: none |
| Cross-family operation-ID collisions | PASS: none |
| Starting graph duplicate obligation/rejection IDs | PASS: none |
| Update/no-change owners exist uniquely | PASS |
| Reject IDs are fresh in both starting namespaces | PASS |
| Added evidence paths exist and are nonempty | PASS: 48 occurrences, 24 distinct paths |
| Added evidence absent from both starting owner buckets | PASS |
| Judge present once per update after unique append | PASS |
| Restore actions exactly match starting actions | PASS |
| Restore metadata exactly match starting metadata | PASS |
| Only declared obligation fields mutate | PASS |
| No-change and all non-owner obligations remain identical | PASS |
| Old rejected list remains an identical prefix | PASS |
| New rejected suffix exactly matches patch order/content | PASS |
| Inverse object equals starting object | PASS |
| Inverse canonical bytes equal starting raw bytes | PASS |
| Frozen-time replay equals first postimage in object and bytes | PASS |
| Graph validation at start/post/reverse/replay | PASS: no issues |
| Workspace graph unchanged by diagnostic | PASS |

## 6. Dependencies and exact artifacts used

The audit used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/state_patch.json`;
- `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_adjudication.md`;
- `math_collab/proof_obligations.py`;
- `math_collab/validate_state_patch.py`.

The twenty-four evidence files named by each update were checked exactly as listed in the patch: the normalization kernel; the formal candidate; the three discovery reports; the operator-normalization analysis and report reconciliation; the blind, normalization, power-owner, candidate-consistency, final-kernel, adjudication, launch-validation, and synthesis artifacts under the current Round 196 campaign.  Their role in this control was existence/nonemptiness and correct path membership only; their mathematical contents were not re-adjudicated.

All computation was bounded, diagnostic, and in-memory.  No shared state, patch, strategy, synthesis, kernel, candidate, or review artifact was edited by this audit.

## 7. Recommended state effect

**No change by this control.**  Mark the pre-apply reversibility gate **PASS**: the current patch is structurally valid, count-correct, duplicate-free, and exactly reversible to the starting canonical graph modulo forward wall-clock timestamp mechanics.  The conductor may apply it subject to the ordinary final graph-hash and campaign-policy checks; this report itself does not authorize or perform the state mutation.
