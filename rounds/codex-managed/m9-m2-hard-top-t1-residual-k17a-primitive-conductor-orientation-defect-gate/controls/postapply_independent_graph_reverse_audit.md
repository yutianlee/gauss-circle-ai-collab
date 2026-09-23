# Round 179 post-application independent graph and reverse audit

## 1. Result

**Verdict: GREEN.**  The applied Round 179 State Patch is exactly the
reviewed patch.  The raw and canonically serialized post-application graph
are byte-identical and have SHA-256

`e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`.

The official graph validator reports zero issues.  Independent inversion of
the applied graph recovers a valid graph with 380 obligations, 1,472 rejected
claims, and exact canonical SHA-256

`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`,

which is the patch's declared starting hash.  Reapplying the reviewed patch
in memory with Round index 179, the recorded application time
`2026-08-27T13:28:40`, and the adjudication as `judge_ref` reproduces the
current post-application object and bytes exactly.

The realized operation ledger is

\[
\boxed{1\ \mathrm{create}/2\ \mathrm{update}/0\ \mathrm{correct\text{-}rejected}/14\ \mathrm{reject}/18\ \mathrm{no\text{-}change}}.
\]

No unauthorized status, statement, owner, implication, blocker, theorem, or
exponent change occurred.  This audit did not edit authoritative state; its
only write is this report.

## 2. Exact statement and hypotheses

The audited input is the already-applied canonical
`state/proof_obligations.yml`, not the pre-application graph.  The authorized
patch has starting hash
`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`
and the following exact graph effect:

1. create
   `M9-M2-hard-top-t1-residual-k17a-primitive-conductor-parity-self-return`
   as one subordinate `proved_internal` reduction;
2. update only
   `M9-M2-hard-top-t1-residual-k17a-primitive-alias-conductor-reduction`
   and `M9-M2-top-endpoint-signed-cone`;
3. append exactly the 14 `Round179-*` mechanism-level rejected claims;
4. mutate none of the 18 named `no_change` obligations; and
5. preserve every pre-existing status and theorem statement, including all
   parent, bridge, target, and exponent owners.

The patch's mathematical scope, as stated consistently by the adjudication
and synthesis, is only the exact primitive projector, target-safe trace, and
all-conductor centered self-return.  The complete literal centered defect
(179.K19), equivalently (177.K34) after safe terms, remains open.  The audit
therefore treats the new proved node as a subordinate reduction and does not
infer complete K17a, hard TOP, M9--M2, M9, either bridge, the quarter theorem,
or an exponent improvement.

## 3. Proof and exact derivation

### 3.1 Raw post-application validity

The current graph parses under the repository loader and passes
`validate_graph` with zero issues.  The repository's official graph command
also returns `Graph OK`.  The file has 381 obligations and 1,486 rejected
claims.  Canonical serialization is byte-for-byte identical to the raw file,
so the reported post hash is both the raw-file and canonical-object hash.

The created node has exactly one dependency, on the accepted primitive-alias
reduction.  It has Round index 179, application time
`2026-08-27T13:28:40`, the 12 declared positive evidence paths, and the
adjudication inserted once as inconclusive `judge_ref` evidence.

### 3.2 Exact realized scope

Among all 380 pre-existing obligations, exactly two objects differ from the
reconstructed starting graph:

- `M9-M2-hard-top-t1-residual-k17a-primitive-alias-conductor-reduction`
  changes only `evidence.inconclusive`, `next_action`,
  `last_updated_round`, and `last_updated_at`.  Exactly the six declared
  inconclusive evidence paths were appended.
- `M9-M2-top-endpoint-signed-cone` changes only `dependencies`,
  `evidence.inconclusive`, `next_action`, `last_updated_round`, and
  `last_updated_at`.  Exactly the one declared dependency and six declared
  inconclusive evidence paths were appended.

Both next actions equal the patch text exactly, and both metadata records
have Round index 179 and the common observed application time.  There is no
pre-existing `status` or `statement_tex` change.  All 18 `no_change`
obligations compare exactly equal before and after application.

Exactly 14 new rejected-claim IDs occur, and their ID set equals the patch's
`reject` array.  Every new record has the patch's reason, Round index 179,
the common application time, and the adjudication as its sole evidence
entry.  No pre-existing rejected-claim record changed.

The exponent-bearing obligations
`GC-partial-one-third`, `GC-external-Li-Yang-theta-star`, and `GC-target`
are byte-identical to their reconstructed starting versions.  Thus the
internal exponent remains \(1/3\), the audited external benchmark remains
\(0.3144831759740614\ldots\), and the target remains \(1/4\), with no graph
promotion.

### 3.3 Dependency and cycle delta

The only new dependency edges, in the graph's stored owner-to-dependency
orientation, are

\[
\begin{aligned}
&\text{primitive-conductor parity self-return}
  \to \text{primitive-alias conductor reduction},\\
&\text{hard-TOP signed-cone owner}
  \to \text{primitive-conductor parity self-return}.
\end{aligned}
\]

No dependency edge was removed, no implication edge was added, and there is
no dangling dependency, blocker, or implication reference before or after
the patch.  Tarjan comparison finds zero cyclic-SCC delta.  The same three
inherited two-node dependency cycles occur before and after:

- `M9-M1-lower-far-cone-microscopic-cell-reduction` with
  `M9-M1-lower-post-collar-smoothed-far-alias-reduction`;
- `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` with
  `M9-M1-lower-incomplete-fibre-dispersion-obstruction`; and
- `M9-M2-hard-top-product-fibre-mean-obstruction` with
  `M9-M2-hard-top-product-fibre-transform-self-return`.

There is likewise no new cyclic component in the implication graph or in the
normalized combined dependency/blocker/implication graph.

### 3.4 Exact inverse and forward replay

The independent inverse was constructed in memory directly from the patch's
recorded reversal data:

1. remove the one created obligation;
2. remove the one added dependency;
3. remove the six added inconclusive evidence values from each updated node;
4. restore both recorded pre-Round-179 next actions;
5. restore their exact prior metadata, namely Round 178 at
   `2026-08-27T11:49:51` and Round 177 at
   `2026-08-27T10:20:58`; and
6. remove the 14 new rejected-claim records.

The inverse graph validates with zero issues and canonically hashes to the
declared starting hash exactly.  A second, independent forward replay used
the repository's `apply_state_patch` implementation with the observed
timestamp frozen.  Its result IDs agree in both content and order with all
five patch operation arrays, and its entire serialized output equals the
current state file byte-for-byte.  This establishes both exact reversal and
exact realized application, rather than only semantic equivalence.

## 4. First doubtful or unproved step

There is no doubtful or unproved step in the patch application, realized
scope, dependency delta, or reverse reconstruction.  **First mechanical
issue: NONE.**

The first remaining mathematical issue is outside this mechanical audit:
the complete literal centered high-conductor defect (179.K19), equivalently
(177.K34) after the safe trace and low-conductor packet are removed, is still
unproved.  Nothing in the applied graph claims otherwise.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Raw post graph SHA-256 | **PASS.** `e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`. |
| Raw/canonical byte equality | **PASS.** Exact equality. |
| Official graph validity | **PASS.** Zero issues; `Graph OK`. |
| Graph counts | **PASS.** 381 obligations and 1,486 rejected claims. |
| Operation counts and exact IDs | **PASS.** `1/2/0/14/18`, including order. |
| Created-node scope | **PASS.** One subordinate reduction with its declared dependency and evidence. |
| Existing mutation scope | **PASS.** Exactly two declared nodes and only authorized fields. |
| Rejected-claim scope | **PASS.** Exactly 14 appended records; zero old-record drift. |
| No-change directives | **PASS.** All 18 objects are exactly unchanged. |
| Existing statuses/statements | **PASS.** Zero drift. |
| Exponent quarantine | **PASS.** All three exponent owners are byte-identical. |
| Dangling references | **PASS.** Zero before and after. |
| Dependency-cycle delta | **PASS.** Zero added or removed cyclic SCC. |
| Implication/combined-cycle delta | **PASS.** Zero new cyclic SCC. |
| Exact inverse count | **PASS.** 380 obligations and 1,472 rejected claims. |
| Exact inverse validity | **PASS.** Zero graph issues. |
| Exact inverse hash | **PASS.** `e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`. |
| Frozen-time forward replay | **PASS.** Exact post object and byte equality. |
| Authoritative-state mutation by audit | **PASS.** None. |

No numerical theorem experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

This audit used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/state_patch.json`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reviews/conductor_round179_adjudication.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/controls/preapply_independent_reverse_audit.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reviews/final_post_repair_verification.md`;
- `math_collab/proof_obligations.py`; and
- `math_collab/validate_state_patch.py`.

The official validator, independent object comparisons, a direct inverse,
Tarjan SCC comparison, and frozen-time forward replay were all read-only with
respect to authoritative state.

## 7. Recommended state effect

Retain the applied Round 179 graph exactly as written.  The application is
mechanically sound and reversible, and no corrective State Patch is needed.
Preserve (179.K19), (177.K34), complete K17a, every parent and bridge, the
quarter theorem, and all exponent owners at their inherited status.  The
conductor may proceed with Round 179 closure using this post-application
GREEN audit.

**GREEN — first issue: NONE.**
