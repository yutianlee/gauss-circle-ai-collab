# Round 194 postapplication independent reverse/replay audit

- Campaign: `full-proof-round191-193-strategy-literature-review`
- Applied State Patch SHA-256:
  `918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`
- Observed live-graph SHA-256:
  `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`
- Actual application timestamp: `2026-08-30T02:58:26`
- Audit mode: bounded read-only in-memory inverse and canonical replay; no
  graph, patch, synthesis, validation-matrix, or proof-draft mutation and no
  full test suite

## 1. Result

**Verdict: PASS.**  The live postapplication graph is the exact canonical
image of the repaired Round-194 patch under:

- `round_index = 194`;
- `last_updated_at = 2026-08-30T02:58:26`; and
- judge reference
  `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`.

The exact normalized patch counts and returned application counts are both

`0 / 1 / 0 / 20 / 26`

for create/update/correct-rejected/reject/no-change.  The declared inverse
recovers the byte-identical starting graph at SHA-256

`cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`.

Replaying with the actual timestamp and judge reference returns a graph
deeply and bytewise identical to the live graph, at SHA-256

`815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`.

## 2. Exact statement and hypotheses

Let \(G_1\) be the live `state/proof_obligations.yml` at the observed hash
above, and let \(P\) be
`rounds/codex-managed/full-proof-round191-193-strategy-literature-review/state_patch.json`
at SHA-256
`918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`.

The audit tests:

1. that \(G_1\) is a valid graph and has the exact postapplication counts;
2. that all actual patch mutations have the specified IDs, ordering,
   reasons, evidence, round, timestamp, and judge reference;
3. that the patch's stated inverse reconstructs the exact canonical
   preimage \(G_0\);
4. that \(P\) validates against recovered \(G_0\); and
5. that applying \(P\) to \(G_0\) with the actual metadata reproduces
   \(G_1\) by deep equality and byte equality.

All operations were performed on deep in-memory copies through the
repository's canonical parser, validator, applicator, indexer, and
serializer.

## 3. Proof and derivation

### 3.1 Live postimage

The live graph has 394 obligations and 1,732 rejected-claim records.  Its
raw file and canonical serialization are both 2,136,028 bytes and both
have SHA-256

`815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`.

The repository graph validator reports `Graph OK`, and direct
`validate_graph` returns no issue.

The sole updated obligation is
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.  It has:

- status `open`;
- `last_updated_round: 194`;
- `last_updated_at: 2026-08-30T02:58:26`.

Relative to the recovered preimage, its complete changed-key set is exactly

`{evidence, next_action, last_updated_round, last_updated_at}`.

No status, dependency, implication, blocker, statement, title, type, track,
positive evidence, or negative evidence changes.

### 3.2 Counts, evidence, rejects, and protected nodes

Repository normalization gives exact patch scope
`0/1/0/20/26`.  Canonical replay returns arrays with those same counts and
the exact patch order.

All 10 `evidence_added.inconclusive` paths occur exactly once on the live
owner.  The judge reference is one of those paths, so uniqueness-preserving
merge does not duplicate it.

The live graph contains exactly the 20 patch-specified new rejected
records, in patch order.  Every record has:

- the exact patch reason;
- `last_updated_round: 194`;
- `last_updated_at: 2026-08-30T02:58:26`; and
- evidence equal to the one-element list containing the exact adjudication
  judge reference.

All 1,712 pre-existing rejected records are an unchanged prefix.  Every one
of the 26 `no_change` nodes is deeply equal to its recovered-preimage
dictionary.  More strongly, all 393 pre-existing obligations other than the
single updated owner are deeply equal.

### 3.3 Exact inverse

The stated inverse was executed in memory:

1. remove the 20 new rejected records by their exact IDs;
2. remove the 10 added inconclusive evidence values from the updated owner;
3. restore the stored prior `next_action`; and
4. restore `last_updated_round: 193` and
   `last_updated_at: 2026-08-30T02:10:41`.

The stored prior next action and metadata equal the reconstructed values
exactly.  The inverse graph has 394 obligations and 1,712 rejected records.
It validates with zero issues.  Its 2,125,317 canonical bytes have SHA-256

`cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`,

which is the exact Round-194 frozen starting hash.  The 10 added evidence
paths are absent from the recovered owner, and no other evidence or graph
field is removed.

### 3.4 Exact replay

The repaired patch validates against the recovered preimage with zero
issues.  The applicator clock was then fixed to the **actual observed**
timestamp `2026-08-30T02:58:26` and the patch was applied with
`round_index = 194` and the exact adjudication judge reference.

The applicator left its preimage input deeply unchanged.  Its replay has
2,136,028 canonical bytes and SHA-256

`815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`.

The replay is deeply equal to \(G_1\), and its canonical bytes are identical
to the live graph's raw bytes.  Replay graph validation returns zero issues.
Thus both required identities hold exactly:

\[
 P^{-1}(G_1)=G_0,\qquad P(G_0)=G_1.
\]

## 4. First doubtful or unproved step

None within the assigned postapplication reverse/replay scope.  Unlike the
preapplication reproducibility witness, this audit uses the actual applied
timestamp, so the replay hash is the observed live graph hash rather than a
hypothetical fixed-time hash.

This control does not re-adjudicate the mathematics in the evidence files.
It verifies the applied patch's exact graph semantics, reversibility,
metadata, judge reference, counts, and byte-deterministic replay.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Repaired patch hash | **PASS:** `918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`. |
| Live raw/canonical hash | **PASS:** both `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`. |
| Live graph validation | **PASS:** zero issues; `Graph OK`. |
| Exact operation counts | **PASS:** patch and returned arrays both `0/1/0/20/26`. |
| Actual metadata | **PASS:** round 194 and timestamp `2026-08-30T02:58:26`. |
| Updated owner | **PASS:** remains `open`; exactly four keys change. |
| No-change IDs | **PASS:** 26/26 deep equalities. |
| All other obligations | **PASS:** 393/393 deep equalities. |
| Evidence additions | **PASS:** 10/10 occur exactly once on the owner. |
| Rejected records | **PASS:** 20/20 exact IDs, order, reasons, metadata, and judge evidence. |
| Rejected prefix | **PASS:** all 1,712 prior records unchanged. |
| Stored inverse metadata | **PASS:** prior next action, round, and timestamp exact. |
| Recovered preimage | **PASS:** deep/byte equality at `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`. |
| Patch on recovered graph | **PASS:** zero validation issues. |
| Actual-metadata replay | **PASS:** deep/byte equality at `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`. |
| Shared-state mutation | **PASS:** none. |
| Full test suite | **NOT RUN, as required.** |

## 6. Dependencies and exact artifacts used

This audit used:

1. `protocol.md`;
2. live `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/state_patch.json`;
5. `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/conductor_round194_adjudication.md`;
6. `math_collab/proof_obligations.py`; and
7. `math_collab/validate_state_patch.py`.

No web source, numerical theorem experiment, graph write, patch write,
validation-matrix write, proof-draft write, synthesis write, or full test
suite was used.

## 7. Recommended state effect

Accept this postapplication reverse/replay gate as **PASS**.  The repaired
Round-194 patch at SHA-256
`918a9ff96cdeb0a603ee56646b9aa728c33fd45c242de761a5d593c6e8fccfe6`
was applied with the exact intended scope and actual metadata.  Its inverse
recovers the frozen preimage `cbbb68b5...cdd9e`, and actual-metadata replay
recovers the live postimage `815c15c4...00c89` byte-for-byte.  This audit
itself authorizes and performs no further shared-state mutation.
