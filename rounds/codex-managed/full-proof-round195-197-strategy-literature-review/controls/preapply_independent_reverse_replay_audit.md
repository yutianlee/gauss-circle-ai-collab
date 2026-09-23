# Round-198 pre-apply independent reverse/replay audit

## 1. Result

**GREEN, with one inherited advisory.** The State Patch at SHA-256
`70aabc822cf23a1fc3f70953bbd3455b9cc9e73e10983578773ccf1eececc279`
is mechanically valid against the live graph at SHA-256
`8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69`.

Repository and independent in-memory applications agreed exactly. The
declared inverse recovered the starting parsed graph and its exact
repository serialization; deterministic replay reproduced the first
application. All 11 added evidence paths exist. No file under `state/` was
written.

An independent dependency-cycle scan found one already-present two-node
cycle,
`M9-M2-hard-top-product-fibre-mean-obstruction` ↔
`M9-M2-hard-top-product-fibre-transform-self-return`. The patch changes no
dependency, implication, or blocker edge, so it neither creates nor alters
this cycle. The repository validator, whose graph-validity contract does
not include acyclicity, reports zero issues on both the live and simulated
graphs.

## 2. Exact statement and hypotheses

Let \(G_0\) be the parsed live graph and \(P\) the parsed Round-198 patch.
Apply \(P\) with `round_index=198`, no external `judge_ref`, and the fixed
test clock `2026-08-31T12:34:56`. The fixed clock makes apply and replay
byte-comparable; it is not a proposed production timestamp.

The exact operation census is:

| operation | count |
|---|---:|
| `create` | 0 |
| `update` | 1 |
| `correct_rejected` | 0 |
| `reject` | 23 |
| `no_change` | 30 |

The sole update target is
`M9-M1-hard-top-high-radical-small-t-residual-estimate`. The inverse must
remove the 23 introduced rejected claims and 11 added inconclusive evidence
paths, then restore that node's recorded `next_action`,
`last_updated_round=197`, and
`last_updated_at=2026-08-31T00:13:15`.

## 3. Proof or derivation

### Hashes and control bytes

| artifact | bytes | SHA-256 | LF | byte controls |
|---|---:|---|---:|---|
| `state/proof_obligations.yml` | 2,190,394 | `8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69` | 31,509 | no BOM, CRLF, or NUL; final LF |
| `state_patch.json` | 13,619 | `70aabc822cf23a1fc3f70953bbd3455b9cc9e73e10983578773ccf1eececc279` | 174 | no BOM, CRLF, or NUL; final LF |
| `conductor_round198_adjudication.md` | 7,326 | `905efb8375e684337d0a10e7ed2457fbd543ce699af33b96649f1df4af9dd745` | 184 | no BOM, CRLF, or NUL; final LF |
| `synthesis.md` | 4,934 | `ac05cf84483d619fe8153c7abbdf7c1cdf06a50b50e7c423025e6d47e2490a6a` | 120 | no BOM, CRLF, or NUL; final LF |

The patch's declared starting hash equals the live raw-file hash. The
repository serializer reproduces the live graph bytes exactly.

### Apply and mutation footprint

The repository validator returned `Patch OK`. Live-graph, patch-against-
graph, and simulated-applied-graph validation each returned zero issues.
An independent implementation of all operation classes produced exactly
the repository applicator object and serialized bytes.

Counts changed as follows:

- proof obligations: \(396\to396\);
- rejected claims: \(1797\to1820\);
- target-node inconclusive evidence: \(275\to286\).

Exactly one pre-existing obligation changed. Its changed fields were
`evidence`, `next_action`, `last_updated_round`, and
`last_updated_at`. Its status, dependencies, implications, blockers, and
all other fields were unchanged. Every other pre-existing obligation,
including all 30 `no_change` nodes, was exactly unchanged. The old
1,797-entry rejected list is an exact ordered prefix of the result, and
the 23-record suffix has exactly the patch ids and reasons plus the fixed
Round-198 timestamp metadata.

All patch ids are internally unique. The update id exists exactly once;
all 23 rejected ids are new; all 30 `no_change` ids exist and are unique;
the 11 evidence paths are unique, absent from the old evidence list, and
exist as files.

### Inverse and replay

The fixed-clock simulated applied serialization has SHA-256
`3b54e42590c4efa7930fad40276cc3289ae578e6d260433ad47b850b2cbb271a`.
The independent and repository applied hashes are identical.

Executing only the declared inverse returned an object exactly equal to
\(G_0\). Its serialized SHA-256 is
`8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69`,
and its bytes equal the live file exactly. Reapplying \(P\) with the same
clock and caller arguments reproduced
`3b54e42590c4efa7930fad40276cc3289ae578e6d260433ad47b850b2cbb271a`
exactly.

The patch payload also agrees with the adjudication and synthesis: it
changes only strategy evidence and the one open node's next action, freezes
the complete three-piece \(P_2\) remainder, and promotes no status, parent,
endpoint theorem, bridge, target, or exponent.

## 4. First doubtful or unproved step

There is no unresolved patch-local apply, inverse, replay, path, or
repository-validation step.

Two boundaries remain outside this control. First, a production apply uses
its runtime clock, so its applied serialization hash will differ from the
fixed-clock hash above; exact replay requires the same clock and caller
arguments. Supplying a `judge_ref` would add it only to newly created
rejection records here, all of which the inverse removes.

Second, acyclicity is not checked by the repository validator. The
independent scan's inherited two-node dependency cycle is unchanged by this
strategy-only patch. If a later conductor gate requires the entire graph to
be a DAG rather than repository-valid under the current contract, that
baseline issue needs a separate correction patch; it is not licensed here.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| starting raw hash | **PASS**, exact patch precondition |
| patch census and id collision checks | **PASS**, \(0/1/0/23/30\) |
| repository patch validation | **PASS**, zero issues |
| live and applied graph validation | **PASS**, zero repository issues |
| repository versus independent apply | **PASS**, exact object and bytes |
| intended pre-existing mutation footprint | **PASS**, one node and four fields |
| old rejected-prefix/new suffix order | **PASS**, exact |
| evidence-prefix/suffix order | **PASS**, exact \(275+11\) |
| evidence-path existence | **PASS**, 11/11 files |
| `no_change` preservation | **PASS**, 30/30 exact |
| declared inverse | **PASS**, exact baseline object and raw hash |
| deterministic replay | **PASS**, exact first-applied object and hash |
| dependency-edge preservation | **PASS**, no edge mutation |
| independent DAG advisory | **INHERITED**, one unchanged baseline two-cycle |
| adjudication/synthesis consistency | **PASS**, strategy-only scope |

All tests ran in memory. The live graph remains untouched.

## 6. Dependencies and exact artifacts used

The audit used:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/state_patch.json`;
4. `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/reviews/conductor_round198_adjudication.md`;
5. `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/synthesis.md`;
6. `math_collab/proof_obligations.py`;
7. `math_collab/validate_state_patch.py` and
   `math_collab/validate_round.py`.

The independent implementation did not call the repository applicator.
Its result was compared afterward with the repository implementation under
the same fixed clock. A prior Round-197 control was consulted only to locate
the repository validation interface; none of its test results or graph
claims was imported.

## 7. Recommended state effect

**Authorize conductor application of the Round-198 State Patch under the
current repository validity contract.** Its precondition, operation census,
mutation scope, evidence paths, inverse, and deterministic replay are
GREEN. This report itself changes no shared state.

The inherited two-node dependency-cycle advisory must not be represented as
created or repaired by Round 198. The patch remains strategy-only and must
leave every analytic status and exponent unchanged.
