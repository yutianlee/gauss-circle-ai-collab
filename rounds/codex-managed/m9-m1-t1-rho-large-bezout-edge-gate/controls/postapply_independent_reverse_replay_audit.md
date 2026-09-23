# Round 192 postapplication independent reverse/replay audit

## 1. Result

**PASS.** The live authoritative graph is the exact production application
of the locked Round-192 State Patch.

- Live graph SHA-256:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`.
- Independently recovered starting SHA-256:
  `75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13`.
- State Patch SHA-256:
  `fe6718748100c26c1bd56b3c16e02be1827fde513a2a6f133cbbca06c091e9e0`.
- Preapplication audit SHA-256:
  `16b3f864b1592bdafb206a01a2b83b0fa9986dd52ef4e537187fb1ad14166be1`.
- Actual application timestamp recovered from the live graph:
  `2026-08-30T00:29:16`.
- Actual judge reference recovered from the live graph:
  `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/conductor_round192_adjudication.md`.

The exact effect inventory is \(1/1/0/15/24\) in the order
create/update/correct/reject/no-change.

The declared inverse recovers the exact canonical starting bytes and hash.
Reapplying the patch with the production mutation routine, round index 192,
the recovered judge reference, and the recovered timestamp reproduces the
live bytes and hash exactly. No repair is required.

## 2. Exact statement and hypotheses

This audit treats `state/proof_obligations.yml` as authoritative and the
patch operations as the complete mutation specification. The sole created
obligation is

`M9-M1-hard-top-t1-rho-large-farey-covector-reduction`.

It is a `candidate_lemma` on track `M9_analytic`, has status
`proved_internal`, owner `Codex conductor`, empty `implies` and `blockers`,
and exactly two direct dependencies:

- `M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction`;
- `Divisor-bound-elementary`.

Both dependencies exist live and are `proved_internal`. The created node
retains the nonempty core as open and asserts only the strict Farey union,
exact core reduction, coverage corollaries, and scoped method boundary.

The sole updated obligation is

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

It is `open` in both the recovered starting graph and the live graph. Its
only substantive changes are one appended subordinate dependency, nineteen
appended `inconclusive` evidence paths, and the declared narrowed
`next_action`; its two update metadata fields carry round 192 and the actual
application timestamp. No status, statement, implication, blocker, owner,
parent, bridge, theorem, or exponent field is changed.

The fifteen patch rejections are new rejected-claim records, not rejected
proof obligations. Each live record has exactly the patch reason, round 192,
timestamp `2026-08-30T00:29:16`, and the single recovered judge reference as
evidence. No existing rejected claim is corrected or overwritten.

## 3. Proof and derivation

### Recovery of application metadata

The created node, updated owner, and all fifteen new rejected records have
one common `last_updated_at` value and one common `last_updated_round` value:
`2026-08-30T00:29:16` and 192. Every new rejected record has the same
one-element evidence list. That path is also exactly the additional
`inconclusive` value present on the created node beyond the create payload.
These two independent live-graph traces recover the judge reference quoted
in Section 1.

### Exact inverse

Starting from the live parsed graph, I inverted the operations in memory:

1. removed the one created obligation;
2. removed exactly the fifteen rejected-claim records named by `reject`;
3. removed the one `dependencies_added` value from the updated owner;
4. removed every `evidence_added.inconclusive` value from that owner;
5. restored the old `next_action` from `restore_next_action`;
6. restored `last_updated_round=191` and
   `last_updated_at=2026-08-29T22:59:10` from `restore_metadata`.

The obligation count changes from 393 live to 392 recovered, and the
rejected-claim count from 1,697 live to 1,682 recovered. Production canonical
serialization of the recovered object gives exact SHA-256

`75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13`.

### Production replay

I passed that recovered graph and the unchanged patch to
`math_collab.proof_obligations.apply_state_patch`, using round index 192 and
the recovered judge reference. For deterministic audit only, the routine's
`datetime.now()` boundary was supplied the recovered application time; no
source or state file was modified. The production result lists have exact
lengths (1/1/0/15/24) and exact IDs in patch order.

The replayed Python object is deeply equal to the live parsed graph.
`dump_graph` serialization is byte-for-byte equal to the live file and has
SHA-256

`7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`.

The live file itself is already exact production-canonical serialization;
the replay does not merely match a normalized semantic object.

### Relations, cycles, and paths

The production graph validator returns zero issues on the recovered,
live, and replayed graphs, and patch-against-recovered validation returns
zero issues. Every `dependencies`, `implies`, and `blockers` target resolves
in both recovered and live graphs. The new node has no implication or
blocker edge, while the updated owner has exactly the new dependency path

`owner -> Farey-covector reduction -> accepted Round-191 reduction / divisor bound`.

The dependency graph has exactly the same three nontrivial strongly
connected components before and after application:

1. `M9-M1-lower-far-cone-microscopic-cell-reduction` with
   `M9-M1-lower-post-collar-smoothed-far-alias-reduction`;
2. `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` with
   `M9-M1-lower-incomplete-fibre-dispersion-obstruction`;
3. `M9-M2-hard-top-product-fibre-mean-obstruction` with
   `M9-M2-hard-top-product-fibre-transform-self-return`.

Neither the created node nor the owner enters a new cycle. The patch contains
38 evidence references to 19 unique paths; all 19 are present, nonempty, and
strict UTF-8. The recovered judge path is among those same 19 paths.

### Protected owner and exponent scope

Among all 392 pre-existing obligations, only the declared owner differs
between recovered and live graphs. Its differing keys are exactly
`dependencies`, `evidence`, `next_action`, `last_updated_round`, and
`last_updated_at`. All twenty-four `no_change` obligations are deeply equal;
their status inventory remains 10 `proved_internal`, 11 `open`, 2
`derived_under_assumptions`, and 1 `proved_external_dependency`.

In particular, `M9-M1`, `M9-M2`, `M9-endpoint-uniformity`, `M9`, and
`GC-target` remain open; both bridges remain `derived_under_assumptions`;
`GC-partial-one-third` remains `proved_internal`; and
`GC-external-Li-Yang-theta-star` remains
`proved_external_dependency`. Their complete records are deeply equal, so
the internal (1/3), external
(0.3144831759740614\ldots), and target (1/4) exponent scopes are unchanged.

## 4. First doubtful or unproved step

No postapplication mechanics, metadata, inverse, replay, relation, cycle,
path, or protected-scope defect was found.

The first mathematical step still unproved is exactly the nonempty-core
estimate

\[
 \Re\mathscr R_{\rm core,Y,Q}^{\sigma}
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\]

or the stronger fixed-packet estimate

\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\]

The live owner remains open and continues to require the gain
(Y/(H_Bm)) before positive norms. The application does not promote this
core, complete (t=1), any (t\ge2) range, a parent, bridge, theorem, or
exponent.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| live graph identity | PASS: exact required SHA-256 and production-canonical bytes. |
| patch and preaudit identities | PASS: both exact required SHA-256 values. |
| application metadata recovery | PASS: one timestamp, round 192, and one judge reference across all live mutation traces. |
| operation inventory | PASS: patch and production result both give (1/1/0/15/24), with exact IDs and order. |
| inverse operation completeness | PASS: one node, fifteen rejected records, one dependency, nineteen evidence values, action, and metadata reverse exactly. |
| recovered starting bytes | PASS: canonical SHA-256 is `75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13`. |
| production replay | PASS: deep equality, byte equality, and exact live SHA-256. |
| created node | PASS: exact ID, `proved_internal`, conductor owner, two proved-internal dependencies, empty implies/blockers. |
| updated owner | PASS: open before and after; only the five declared keys differ. |
| rejected claims | PASS: fifteen exact new records; no correction or overwrite. |
| relation closure | PASS: zero missing dependency, implication, or blocker targets. |
| cycle integrity | PASS: the same three pre-existing two-node SCCs; no new cycle. |
| evidence path integrity | PASS: 38 references, 19 unique paths, all present/nonempty/strict UTF-8. |
| no-change deep equality | PASS: all 24 exact, with unchanged status inventory. |
| owner/bridge/theorem/exponent quarantine | PASS: every protected record is deeply equal and retains its prior status. |
| graph validators | PASS: zero recovered/live/replay graph issues and zero patch-against-recovered issues. |
| byte hygiene | PASS: live graph, patch, and preaudit are strict UTF-8, LF-only, have exactly one final LF, and contain no forbidden C0, CR, or NUL byte. |
| mutation discipline | PASS: no state, patch, lifecycle, validator, kernel, or synthesis file was written. |

## 6. Dependencies and exact artifacts used

The audit used only:

1. `protocol.md` — SHA-256
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `state/proof_obligations.yml` — SHA-256
   `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`;
3. `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/state_patch.json`
   — SHA-256
   `fe6718748100c26c1bd56b3c16e02be1827fde513a2a6f133cbbca06c091e9e0`;
4. `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/controls/preapply_independent_reverse_replay_audit.md`
   — SHA-256
   `16b3f864b1592bdafb206a01a2b83b0fa9986dd52ef4e537187fb1ad14166be1`;
5. `math_collab/proof_obligations.py` — SHA-256
   `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437`;
6. `math_collab/validate_state_patch.py` — SHA-256
   `cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8`.

Evidence paths were opened only for existence, nonemptiness, and strict
UTF-8 decoding; their contents were not used as new mathematical evidence or
instructions. No other campaign, state, graph, history, lifecycle, strategy,
or synthesis artifact was inspected.

## 7. Recommended state effect

**Retain the live Round-192 application unchanged.** It creates only the one
strict proved-internal Farey-covector subordinate reduction, updates only the
still-open hard-M1 small-(t) owner, adds the fifteen scoped rejected claims,
and preserves all twenty-four protected obligations exactly.

No graph rollback, correction patch, lifecycle repair, owner promotion,
bridge/theorem promotion, or exponent change is warranted. The conductor may
complete the remaining Round-192 closure gates against live graph SHA-256
`7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`.

**PASS**
