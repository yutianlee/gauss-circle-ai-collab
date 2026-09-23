# Round 196 postapplication independent reverse/replay audit

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Role: independent postapplication State Patch audit
- Starting graph SHA-256: `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Terminal State Patch SHA-256: `013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`
- Live applied graph SHA-256: `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`

## 1. Result

**Verdict: PASS.**

The canonical live graph is byte-for-byte the production application of the current Round 196 patch at the metadata recovered from the live records:

- round index: `196`;
- timestamp: `2026-08-30T12:00:58`;
- judge reference: `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_adjudication.md`.

An independent in-memory inverse using only `state_patch.json`'s removal rule and restore payload produced 2,154,204 canonical bytes with SHA-256

`f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`,

exactly the declared starting graph hash.  Production replay at the recovered live timestamp produced 2,169,843 bytes byte-identical to the current live graph, with SHA-256

`b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`.

Operation counts and ordered result IDs are exactly

\[
(0\ \mathrm{create},\ 2\ \mathrm{update},\ 0\ \mathrm{correct\_rejected},\ 20\ \mathrm{reject},\ 27\ \mathrm{no\_change}).
\]

Each updated owner contains exactly the twenty-four declared inconclusive evidence additions as an ordered suffix, with each value occurring once.  No authoritative state was edited by this audit.

## 2. Exact statement and hypotheses

Let `G_live` be the current `state/proof_obligations.yml` and `P` the current campaign `state_patch.json`.  The audit asserts, under the repository parser, merger, validator, and canonical JSON serializer, that:

1. `G_live` is canonical and has the stated live SHA-256;
2. the one timestamp common to both updated obligations and all twenty new rejected-claim records is the production timestamp for this application;
3. deleting the patch-introduced evidence and rejected records, then restoring the recorded actions and metadata, yields a valid canonical graph at `P.starting_graph_sha256`;
4. invoking `apply_state_patch` on that recovered graph with round 196, the recovered timestamp, and the adjudication judge reference yields exact ordered result lists and a serialization identical to `G_live`;
5. the application contains exactly the declared evidence additions and no undeclared obligation mutation.

The two updated obligations are

1. `M9-M1-hard-top-high-radical-small-t-residual-estimate`;
2. `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`.

This is a mechanical state-transition audit.  It does not re-adjudicate the mathematical evidence named by the patch.

## 3. Proof or derivation

### 3.1 Canonical live image and recovered application metadata

The raw live graph has 2,169,843 bytes.  Parsing it and serializing it with `dump_graph` reproduces the raw byte string exactly.  Its full SHA-256 is

`b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`.

Both updated obligations carry `last_updated_round: 196` and `last_updated_at: 2026-08-30T12:00:58`.  Exactly twenty rejected-claim records have IDs from the patch's reject family; all twenty carry the same round and timestamp.  They form the exact final twenty-record suffix, in patch order.  Thus the live application metadata are uniquely read from all twenty-two mutated or introduced records, rather than inferred from a single node.

The live graph has 395 obligations and 1,775 rejected-claim records.  Their ID counts are respectively 395 and 1,775, with no duplicate within either namespace and no overlap between the two namespaces.

### 3.2 Operation counts and ID integrity

Strict patch parsing found no duplicate JSON key.  The declared family sizes and unique-ID counts coincide:

| family | entries | unique IDs |
|---|---:|---:|
| create | 0 | 0 |
| update | 2 | 2 |
| correct_rejected | 0 | 0 |
| reject | 20 | 20 |
| no_change | 27 | 27 |

No ID is shared between two patch operation families.  The production replay returned those same five counts and the exact ordered ID list for every family.

### 3.3 Exact evidence-addition check

Each update declares twenty-four pairwise distinct additions to `evidence.inconclusive`.  The lists are intentionally the same across the two different owners, so the patch contains forty-eight owner placements over twenty-four distinct paths.

For each owner independently:

- all twenty-four paths occur exactly once in the live `inconclusive` bucket;
- they are the exact ordered suffix of that bucket;
- removing them leaves none of the twenty-four values in the recovered bucket;
- the live bucket equals the recovered bucket followed by the patch list, with no missing, extra, reordered, or duplicated value;
- the adjudication path occurs exactly once.  Although production application also supplies it as `judge_ref`, `_append_unique` correctly avoids a duplicate because the patch already includes it.

All twenty-four distinct evidence paths exist and are nonempty.  The adjudication file is 6,714 bytes and has SHA-256 `e760c0685789b583e16787fa812320faf608d16775f1abee78d38a610e7ce90d`.

### 3.4 Independent inverse

Starting from a deep in-memory copy of `G_live`, the inverse used only `P`:

1. remove from each updated node every value in its `evidence_added.inconclusive` list;
2. restore each target's exact `next_action` from `reversibility.restore_next_action`;
3. restore each target's `last_updated_round` and `last_updated_at` from `reversibility.restore_metadata`;
4. remove every rejected-claim record whose ID appears in `proof_obligations.reject`;
5. make no create or correct-rejected inverse change because those operation families are empty;
6. make no mutation for the no-change family.

The recovered graph has 395 obligations and 1,755 rejected-claim records.  Its canonical serialization is 2,154,204 bytes and hashes to

`f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`,

exactly `P.starting_graph_sha256`.  The recovered graph passes `validate_graph`, and `P` passes `validate_patch_against_graph` on that recovered preimage.

### 3.5 Production replay at the live timestamp

The production `apply_state_patch` function was invoked on the recovered graph with its clock frozen to the observed live timestamp `2026-08-30T12:00:58`, `round_index=196`, and the exact adjudication path as `judge_ref`.

The replay object equals the parsed live object.  Its canonical byte string equals the raw live file byte for byte, has length 2,169,843, and has SHA-256 `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`.

For both updated obligations, the exact changed keys relative to the recovered graph are

`evidence`, `last_updated_at`, `last_updated_round`, and `next_action`.

The first target remains status `open`; the second remains status `proved_internal`.  All 393 non-target obligations, including all twenty-seven no-change nodes, are deeply identical between the recovered and replayed graphs.  The old 1,755 rejected-claim records remain a deeply identical prefix.  Each of the twenty suffix records equals its patch ID and reason plus exactly the production round, timestamp, and singleton judge-evidence list.

### 3.6 Validation and non-mutation control

`validate_graph` returns no issue for either the recovered preimage or the replay.  Patch validation against the recovered preimage returns no issue.  A final raw read of the workspace graph after all diagnostics still hashes to `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`, confirming that reversal and replay occurred only in memory.

## 4. First doubtful or unproved step

There is no doubtful step or application defect in the audited state transition.

The only scope boundary is mathematical: byte-identical replay proves that the live graph is exactly the declared production mutation, not that every cited Round 196 mathematical conclusion is independently true.  That adjudication belongs to the proof and seam-review artifacts, not this mechanical control.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| Terminal patch hash/canonical JSON | PASS: `013eae5d...c9d`; 20,244 bytes; canonical raw bytes |
| Live graph hash/canonical bytes | PASS: `b9b95784...f8ae`; 2,169,843 bytes; canonical raw bytes |
| Live application metadata | PASS: round 196 and common timestamp `2026-08-30T12:00:58` on all 22 affected records |
| Operation counts | PASS: exact `0/2/0/20/27` |
| Operation IDs and order | PASS: exact on replay |
| Duplicate and cross-family IDs | PASS: none |
| Evidence additions | PASS: 24 distinct paths per owner, 48 placements total, exact ordered suffixes |
| Evidence duplication | PASS: every added value occurs once per owner; judge occurs once |
| Evidence path existence | PASS: all 24 distinct files exist and are nonempty |
| Rejected-claim additions | PASS: exact 20-record suffix; old prefix identical |
| Canonical reverse | PASS: 2,154,204 bytes at exact starting SHA `f1f6bd2c...cce2` |
| Recovered graph/patch validation | PASS: no issues |
| Production replay | PASS: byte-identical to live graph at `b9b95784...f8ae` |
| Owner mutation boundary | PASS: only evidence, action, and last-update metadata changed |
| No-change/non-target obligations | PASS: all deeply identical |
| Authoritative-state mutation by audit | PASS: none |

## 6. Dependencies and exact artifacts used

This audit used:

1. `protocol.md`, SHA-256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `state/active_campaign.yml`, SHA-256 `85654069c131a81ab0ff18bde22214a27a0012c15ff85f2187a4901803df6aac`;
3. the live `state/proof_obligations.yml`, SHA-256 `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`;
4. the current campaign `state_patch.json`, SHA-256 `013eae5d57e3854acf2ef9d4c9d72ab94fa9da2af64e97f27b43c701cdeb7c9d`;
5. `math_collab/proof_obligations.py`, SHA-256 `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437`;
6. `math_collab/validate_state_patch.py`, SHA-256 `cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8`;
7. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_adjudication.md`, SHA-256 `e760c0685789b583e16787fa812320faf608d16775f1abee78d38a610e7ce90d`;
8. all twenty-four evidence paths named by each update, checked for exact membership, existence, nonemptiness, and live-bucket placement.

The reconstructed starting graph and replay were held only in memory.  Computation was bounded and diagnostic.  No shared state, patch, strategy, synthesis, kernel, candidate, report, or review artifact was edited.

## 7. Recommended state effect

**Retain the applied Round 196 graph unchanged** and record this control as postapplication **PASS** evidence.  The live graph is the exact application of the terminal patch, the patch reverses to the declared starting SHA, and replay at the recorded live timestamp returns the current graph byte for byte.  This control makes no additional proof promotion and authorizes no further state mutation.
