# Round 190 independent post-application graph, scope, and reverse audit

- Campaign: `full-proof-round187-189-strategy-literature-review`
- Round: `190`
- Audit mode: post-application, read-only, independently implemented
- State Patch SHA-256:
  `b19a92efe86341400e0d6c75868f2e652164d0a34682b9bae93cf00066c948b9`
- Declared starting graph SHA-256:
  `15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`
- Applied graph SHA-256:
  `306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`
- Verdict: **GREEN**

## 1. Result

**Independent post-application replay lemma.**  The written authoritative
graph is exactly the result prescribed by the Round-190 State Patch.  Its
operation census is

\[
 \boxed{0/1/0/23/27}
\]

in the order
`create/update/correct_rejected/reject/no_change`.

The applied graph contains 391 obligations and 1,667 rejected-claim
records, compared with 391 and 1,644 in the graph reconstructed from the
embedded reversal data.  The exact semantic delta is:

1. one existing open obligation is updated;
2. ten unique inconclusive evidence paths are appended to that obligation;
3. its `next_action`, `last_updated_round`, and `last_updated_at` are
   changed to the Round-190 strategy values;
4. twenty-three new rejected-overclaim records are appended; and
5. the twenty-seven `no_change` entries make no graph mutation.

No obligation is created, corrected, rejected, or deleted.  No status,
statement, dependency, implication, blocker, source card, exponent, or
certified-exponent field changes.  The graph remains canonical JSON bytes,
has unique obligation and rejected IDs, and has no unresolved dependency,
implication, or blocker reference.

Removing exactly the ten added evidence paths and twenty-three new rejected
records and restoring the embedded target-node values recovers canonical
bytes with SHA-256

`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`.

Reapplying the exact observed Round-190 metadata and records to that
reconstructed start recovers the current graph byte-for-byte with SHA-256

`306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`.

The post-application verdict is therefore **GREEN**.

## 2. Exact statement and hypotheses

The audit interprets the patch operations independently, using only their
literal JSON content and the written graph:

- `create`: append a new proof obligation; count zero;
- `update`: append-uniquely merge the listed evidence and replace the
  displayed strategy/metadata fields; count one;
- `correct_rejected`: alter an old rejected record; count zero;
- `reject`: append a new rejected-claim record because each listed ID is
  absent from both the reconstructed starting obligations and rejected
  claims; count twenty-three;
- `no_change`: validate an existing node but make no graph mutation; count
  twenty-seven.

The only changed obligation is

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

Its applied values are:

| Field | Applied value / check |
|---|---|
| status | `open`, unchanged |
| inconclusive evidence count | 136, exactly 126 reconstructed-start values plus 10 patch values |
| `next_action` | byte-for-byte equal to the patch update |
| `last_updated_round` | `190` |
| `last_updated_at` | `2026-08-29T20:38:31` |
| changed keys versus reconstructed start | exactly `evidence`, `next_action`, `last_updated_round`, `last_updated_at` |

The embedded reversal restores:

| Field | Restored value / check |
|---|---|
| `next_action` | exact post-Round-189 fast-complement/variation instruction embedded in `restore_next_action` |
| `last_updated_round` | `189` |
| `last_updated_at` | `2026-08-29T19:34:43` |
| inconclusive evidence count | 126 after removing exactly the ten listed paths |

Every new rejected record has the exact patch ID and reason,
`last_updated_round: 190`, `last_updated_at: 2026-08-29T20:38:31`, and
the single evidence value

`rounds/codex-managed/full-proof-round187-189-strategy-literature-review/synthesis.md`.

The audit treats the graph's existing canonical serializer as

\[
 \operatorname{canon}(G)
 =\bigl(\texttt{json.dumps}(G,\texttt{indent}=2,
 \texttt{ensure\_ascii}=\texttt{True})+\texttt{"\\n"}\bigr)_{\rm UTF8}.
\]

The current file is already exactly `canon(current)`.

## 3. Proof or derivation

### 3.1 Current graph and operation census

The graph and patch parse strictly as JSON.  The patch operation lengths
are exactly

\[
 (|\mathrm{create}|,|\mathrm{update}|,
 |\mathrm{correct\_rejected}|,|\mathrm{reject}|,
 |\mathrm{no\_change}|)=(0,1,0,23,27).
\]

All 391 obligation IDs and all 1,667 applied rejected-claim IDs are unique.
Every value in every obligation's `dependencies`, `implies`, and `blockers`
arrays resolves to an obligation ID.  Obligation order and top-level key
order are unchanged under reversal.

The twenty-seven no-change nodes exist and have the expected status census:

\[
 15\ \texttt{open},\qquad
 9\ \texttt{proved\_internal},\qquad
 2\ \texttt{derived\_under\_assumptions},\qquad
 1\ \texttt{proved\_external\_dependency}.
\]

None differs between the reconstructed starting graph and the applied
graph.

### 3.2 Evidence audit

All ten added paths exist as regular files, occur exactly once in the
applied target node, and are absent after exact reversal:

| Added inconclusive evidence | SHA-256 |
|---|---|
| `reports/full_graph_frontier_reconstruction.md` | `acc925d2d3fd45d99847f6f9416086329daeee4d6003bb806e3ade327f887881` |
| `reports/current_primary_literature_reassessment.md` | `d96229160d7277b0f8e19c0a49035b79ce94edddb70c06f61a64f3aee5732725` |
| `reports/blind_round191_frontier_selection.md` | `9900f9c9a4310758cc5367a8ac077ac5aa8c85de81545bbc9d51dacbf4d0ad24` |
| `reviews/conductor_round190_report_reconciliation.md` | `4edb8ae8cbfe695486bafcffe67617cc4dbebd7d22f75d8d49bb092e361da060` |
| `reviews/dependency_power_selection_seam_review.md` | `ac26088b80c50285821a52150c73446a98ec1992d5db199a2150e21d939af331` |
| `reviews/source_hypotheses_currency_interface_review.md` | `2a9d3d366cfdad560f494de4397d392092450f7f7e3a8945a1969e9dfad0b132` |
| `reviews/blind_post_unmask_frontier_selection_review.md` | `af606e23debadac4b79b6f1b0f4a18a8df80416cd1a8af2b98b22c1051993619` |
| `reviews/conductor_round190_adjudication.md` | `66c520732bee3426aa5892afbb5885f495b9f9bc7685a9618289ff5ce207e387` |
| `controls/conductor_round190_controls.md` | `ca3d1ec61cbdf097c6f07062591d68c43325f0e9dfebb0f74da3f27bd3ff9d51` |
| `synthesis.md` | `f7e09d8902de4147d285705b2c191d5c0e3d7da2a6af9bc2f39b57548189c5d8` |

Each displayed path is rooted at
`rounds/codex-managed/full-proof-round187-189-strategy-literature-review/`.
The synthesis judge reference is already one of these ten values; the
applied evidence delta is therefore ten, not eleven.

### 3.3 Rejected-record audit

The exact set difference between applied and reconstructed rejected IDs is
the twenty-three IDs in the patch's `reject` array.  For every one:

- the applied reason equals the patch reason byte-for-byte;
- the round and timestamp are the common applied values stated in Section
  2;
- the evidence is exactly the synthesis path;
- the ID is absent from all obligations; and
- removing it is sufficient for exact reversal.

The records reject overclaims only: report agreement as proof, positive
variation as a signed seam, Abel identity as cancellation, height-mask
invariance, centered-prefix and positive-transform shortcuts, epsilon
absorption of a fixed deficit, owner/bridge/exponent overreach, route
splicing, source over-import, universal no-literature claims, and in-round
pivots.  No accepted obligation is assigned status `rejected`.

### 3.4 Protected-field and exponent audit

Comparing every applied obligation with the reversed starting obligation
gives no difference in any of

`status`, `statement_tex`, `dependencies`, `implies`, `blockers`,
`source_card`, `exponent`, or `certified_exponent`.

In particular:

- `GC-partial-one-third` remains `proved_internal` at exponent \(1/3\);
- `GC-external-Li-Yang-theta-star` remains
  `proved_external_dependency` at
  \(0.3144831759740614\ldots\);
- `GC-target` remains open at exponent \(1/4\);
- M9--M1, M9--M2, endpoint uniformity, and M9 remain open; and
- both final bridges remain `derived_under_assumptions`.

Thus the State Patch is strategy/source evidence only and preserves every
parent, endpoint, bridge, theorem, and exponent boundary.

### 3.5 Reverse and exact replay

Starting from the applied graph, the independent reversal did exactly:

1. remove the ten patch-listed inconclusive evidence values from the one
   updated node;
2. restore that node's `next_action`, `last_updated_round`, and
   `last_updated_at` from `reversibility`;
3. remove the twenty-three patch-listed rejected IDs; and
4. leave all other graph content and ordering unchanged.

The reconstructed object has 391 obligations and 1,644 rejected claims.
Its canonical SHA-256 is

`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`,

exactly the embedded start hash.

For replay, the audit appended the ten evidence values in patch order,
restored the patch `next_action`, copied the actual applied round/time
metadata, and appended the exact twenty-three applied rejected records in
patch order.  The canonical result is byte-for-byte equal to the written
graph and has SHA-256

`306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`.

This proves both exact reverse recovery and exact written-state replay.

## 4. First doubtful or unproved step

There is no unresolved graph-application or reversal step in this audit.
The first mathematical step remains the unproved joint literal signed
height-jump estimate recorded only in the updated `next_action`.  The
applied graph correctly treats the reports, source audit, Abel identity,
coefficient ledger, and proposed seam as inconclusive strategy evidence.

The audit does not certify that future filesystem changes will preserve the
applied hash.  Its conclusion is exact for the graph bytes read after the
Round-190 application and for State Patch SHA-256
`b19a92efe86341400e0d6c75868f2e652164d0a34682b9bae93cf00066c948b9`.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Patch identity | **PASS:** SHA-256 `b19a92...c948b9` |
| Written applied graph hash | **PASS:** `306425...a573fa` |
| Embedded starting hash | **PASS:** `15c770...a98568` |
| Exact effect census | **PASS:** `0/1/0/23/27` |
| Current/start counts | **PASS:** obligations 391/391; rejected 1667/1644 |
| Updated obligation | **PASS:** exactly one existing open node |
| Changed target keys | **PASS:** exactly evidence, next action, round metadata, and timestamp |
| Evidence delta | **PASS:** exactly ten unique existing files, 126 to 136 entries, no extra judge value |
| Rejected delta | **PASS:** exactly 23 patch IDs/reasons; round 190; common applied timestamp; synthesis evidence only |
| No-change semantics | **PASS:** all 27 IDs exist and are unchanged |
| Protected fields | **PASS:** no status, statement, dependency, implication, blocker, source-card, or exponent mutation |
| Owner/parent/bridge scope | **PASS:** only the subordinate small-\(t\) owner's strategy evidence and next action change |
| Graph integrity | **PASS:** canonical bytes, unique IDs, all references resolve, obligation order/top-level keys preserved |
| Exponent quarantine | **PASS:** internal \(1/3\), external \(0.3144831759740614\ldots\), target \(1/4\) unchanged |
| Exact reverse | **PASS:** reconstructed SHA-256 `15c770...a98568` |
| Exact replay | **PASS:** byte equality and SHA-256 `306425...a573fa` |
| Shared-state mutation by auditor | **PASS:** none; audit was read-only |

## 6. Dependencies, exact artifacts, and commands

Artifacts read in full or mechanically parsed as requested:

- `protocol.md`, SHA-256
  `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
- `state/proof_obligations.yml`, applied SHA-256
  `306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`;
- `state_patch.json`, SHA-256
  `b19a92efe86341400e0d6c75868f2e652164d0a34682b9bae93cf00066c948b9`;
- `controls/preapply_independent_reverse_audit.md`, SHA-256
  `c1b63741df7d28d783ef09c45497cffea45013aa3b33580733b86f2761e9b1a7`;
- `reviews/conductor_round190_adjudication.md`, SHA-256
  `66c520732bee3426aa5892afbb5885f495b9f9bc7685a9618289ff5ce207e387`;
- `controls/conductor_round190_controls.md`, SHA-256
  `ca3d1ec61cbdf097c6f07062591d68c43325f0e9dfebb0f74da3f27bd3ff9d51`;
- `controls/conductor_round190_launch_validation.md`, SHA-256
  `24343cdcc0a8c0413a5ab9e8ef9a78232d7c5ae55d125fa9b09213caf1579d5c`.

The decisive current-state hash command was

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath state/proof_obligations.yml
```

and returned

```text
306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa
```

The reverse/replay audit was an inline, read-only Python standard-library
script.  It did not import the repository validator and wrote no file.  Its
decisive output was

```text
counts_effect [0, 1, 0, 23, 27]
current_counts [391, 1667]
reversed_counts [391, 1644]
current_canonical_byte_equal true
changed_obligations [M9-M1-hard-top-high-radical-small-t-residual-estimate]
changed_target_keys [evidence, last_updated_at, last_updated_round, next_action]
protected_diffs []
target_evidence_counts [126, 136]
reject_all_exact true
reverse_sha256 15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568
replay_sha256 306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa
replay_current_byte_equal true
```

No graph, proof draft, validation matrix, synthesis, campaign manifest, or
other shared state was modified.

## 7. Recommended state effect

**Verdict: GREEN.**  Accept the written Round-190 graph as the exact applied
result of the audited State Patch.  The post-application graph hash is

`306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`.

The embedded reversal and exact replay are complete.  The patch changes
only inconclusive strategy/source evidence, one open subordinate owner's
next action and metadata, and rejected-overclaim records.  It promotes no
analytic theorem and changes no protected proof or exponent field.

No further graph or shared-state mutation is recommended by this audit.
