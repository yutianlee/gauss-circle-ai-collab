# Round-198 post-apply independent reverse/replay audit

## 1. Result

**GREEN for the applied Round-198 patch.** The live graph has the supplied
SHA-256
`63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5`.
Its exact inverse serializes to the declared starting graph SHA-256
`8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69`.
Reapplying with production timestamp `2026-08-31T01:31:33`,
`round_index=198`, and the actual adjudication `judge_ref` reproduces the
live graph object and bytes exactly.

The actual footprint is exactly one changed pre-existing obligation, 11
ordered inconclusive-evidence additions, and 23 ordered rejected-claim
records. No status, dependency, implication, blocker, parent, bridge,
target, or exponent changed.

Advisory refinement: an exhaustive dependency scan finds three inherited
two-node cycles, not one. The pre-apply scan stopped after its first cycle.
The restored starting graph and live graph have identical cycle sets, so
this is not a patch mismatch or a reason to reverse this strategy-only
application under the current repository validator.

## 2. Exact statement and hypotheses

Let \(G_1\) be the parsed live graph, \(P\) the Round-198 State Patch, and
\(J\) the relative adjudication path

`rounds/codex-managed/full-proof-round195-197-strategy-literature-review/reviews/conductor_round198_adjudication.md`.

The production applicator semantics are:

- `round_index=198`;
- clock `2026-08-31T01:31:33`;
- `judge_ref=J`;
- operation census \(0/1/0/23/30\) for
  `create/update/correct_rejected/reject/no_change`.

The declared inverse removes the 23 patch rejection ids and the 11 added
inconclusive paths, then restores the selected node's prior `next_action`,
`last_updated_round=197`, and
`last_updated_at=2026-08-31T00:13:15`.

Normalized replay means applying \(P\) to that restored object with the
same production clock, round index, and `judge_ref`. This normalization is
necessary because the helper adds \(J\) to every newly created rejected
record.

## 3. Proof or derivation

### Hash and byte controls

| artifact | bytes | SHA-256 | LF | byte controls |
|---|---:|---|---:|---|
| live `state/proof_obligations.yml` | 2,202,271 | `63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5` | 31,727 | no BOM, CRLF, or NUL; final LF |
| `state_patch.json` | 13,619 | `70aabc822cf23a1fc3f70953bbd3455b9cc9e73e10983578773ccf1eececc279` | 174 | no BOM, CRLF, or NUL; final LF |
| pre-apply audit | 8,103 | `ee8b54e2b8001a7c0d348f46cc86ce9955b8c7630f8812e77adba6b7b4f27bf9` | 176 | no BOM, CRLF, or NUL; final LF |
| adjudication | 7,326 | `905efb8375e684337d0a10e7ed2457fbd543ce699af33b96649f1df4af9dd745` | 184 | no BOM, CRLF, or NUL; final LF |
| `math_collab/proof_obligations.py` | 26,686 | `bf57807d107a36d23d4912caec63933d75cbca6a31e814b6bf0bb9fe987e6d06` | 681 | no BOM, CRLF, or NUL; final LF |

The live raw bytes equal the repository serializer output.

### Actual footprint

Counts are \(396\to396\) proof obligations,
\(1797\to1820\) rejected claims, and \(275\to286\) inconclusive evidence
entries on
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

That node is the only changed pre-existing obligation. Its changed fields
are exactly `evidence`, `next_action`, `last_updated_round`, and
`last_updated_at`. Its live status remains `open`. Its 275 old
inconclusive paths are an exact prefix and the patch's 11 paths are the
exact suffix. All 11 exist.

The old 1,797 rejected records are an exact ordered prefix of the live
list. The 23-record suffix is in patch order and each record has exactly:

- the patch id and reason;
- `last_updated_at=2026-08-31T01:31:33`;
- `last_updated_round=198`;
- `evidence=[J]`.

All 30 `no_change` obligations are exactly unchanged. Proof-obligation and
rejected-claim ids remain unique.

### Exact inverse and normalized replay

Applying only the declared inverse to \(G_1\) gives a parsed object whose
repository serialization has SHA-256
`8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69`,
the exact starting hash. Repository validation reports zero issues on the
restored and live objects, and patch-against-restored validation reports
zero issues.

Repository replay from the restored object under the production clock and
\(J\) has SHA-256
`63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5`
and equals the live bytes exactly. A separate independent applicator
produces the same object and hash. Omitting \(J\) instead gives
`9a04c19d6acec5627dfc03e58a9c9a583cb2d5ef04b7cb8e6dbfc8d451551d95`,
confirming that the replay matched the actual judge behavior rather than
only the timestamp.

## 4. First doubtful or unproved step

There is no unresolved apply-footprint, inverse, serialization, timestamp,
judge-reference, evidence-path, or deterministic-replay step.

The first boundary outside this control is graph acyclicity. The repository
validator does not test it. An exhaustive scan finds these same inherited
cycles before and after the patch:

1. `M9-M2-hard-top-product-fibre-mean-obstruction` ↔
   `M9-M2-hard-top-product-fibre-transform-self-return`;
2. `M9-M1-lower-post-collar-smoothed-far-alias-reduction` ↔
   `M9-M1-lower-far-cone-microscopic-cell-reduction`;
3. `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` ↔
   `M9-M1-lower-incomplete-fibre-dispersion-obstruction`.

The patch changes no edge, so correcting or formally accepting those
cycles would require a separate authorized state action.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| supplied live hash | **PASS**, exact raw SHA-256 |
| live repository serialization | **PASS**, exact bytes |
| actual operation census | **PASS**, \(0/1/0/23/30\) |
| actual old-node mutation footprint | **PASS**, one node/four fields |
| evidence prefix and 11-entry suffix | **PASS**, exact order; 11/11 files |
| rejected prefix and 23-entry suffix | **PASS**, exact order and metadata |
| production timestamp | **PASS**, all changed/new records use the supplied value |
| production `judge_ref` behavior | **PASS**, exact \(J\) on all 23 new rejections |
| 30 `no_change` records | **PASS**, exact |
| live and restored repository validation | **PASS**, zero issues |
| declared inverse | **PASS**, exact starting object and hash |
| normalized repository replay | **PASS**, exact live object and bytes |
| independent normalized replay | **PASS**, exact live object and bytes |
| protected analytic/status scope | **PASS**, no forbidden mutation |
| exhaustive cycle comparison | **INHERITED**, three identical baseline/live cycles |

All reverse and replay tests were in memory. No shared-state file was
modified.

## 6. Dependencies and exact artifacts used

This audit used exactly:

1. the live `state/proof_obligations.yml`;
2. `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/state_patch.json`;
3. `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/controls/preapply_independent_reverse_replay_audit.md`;
4. `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/reviews/conductor_round198_adjudication.md`;
5. `math_collab/proof_obligations.py`.

The helper was used for repository parsing, validation, serialization, and
the comparison replay. The inverse and second replay implementation were
written independently in memory.

## 7. Recommended state effect

**Retain the applied Round-198 graph.** Its actual footprint, declared
inverse, production metadata, judge evidence, and normalized replay are
exact. This control supports no additional proof-state mutation.

Do not describe the three inherited dependency cycles as introduced or
repaired by Round 198. If project policy later requires a DAG beyond the
current repository validator's contract, address them in a separate
coordinator-owned patch.
