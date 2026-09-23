# Round 181 post-application independent graph and reverse audit

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Task: `round181_postapply_graph_audit`
- Round: 181
- Role: independent post-application graph, scope, evidence, and exact-reverse auditor
- Generated: `2026-08-27T09:14:48.4311139Z`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Applied graph SHA-256: `fec130bc66641cbdad18c832de10077a7825f1caaf5d10170a67ef65c0b27196`
- Exact context files: enumerated in Section 6
- Direct machinery dependencies: `math_collab/proof_obligations.py` and
  `math_collab/validate_state_patch.py`
- Claimant/reviewer/blind status: independent reviewer; not a claimant and
  not blind; this audit made no graph, patch, synthesis, candidate, kernel,
  validation-matrix, or other shared-state edit

## 1. Result

**GREEN.** The actually applied Round-181 graph is exactly the graph produced
by the reviewed `state_patch.json`. Its raw bytes equal the repository's
canonical serialization, and both have SHA-256

`fec130bc66641cbdad18c832de10077a7825f1caaf5d10170a67ef65c0b27196`.

The graph contains 385 obligations and 1,515 rejected-claim records and
passes the official graph validator with zero issues. The realized operation
ledger is exactly

\[
 \boxed{3\ \mathrm{create}/4\ \mathrm{update}/0\
 \ \mathrm{correct\text{-}rejected}/13\ \mathrm{reject}/18\
 \ \mathrm{no\text{-}change}}.
\]

An operation-derived inverse recovers a valid graph with 382 obligations,
1,502 rejected claims, canonical bytes hashing exactly to the declared
starting SHA-256. Reapplying the official applicator at the observed frozen
time `2026-08-27T17:11:21`, with Round index 181 and the conductor
adjudication as `judge_ref`, reproduces the current graph object, bytes,
operation order, and hash exactly. No unauthorized drift, new cycle, parent
promotion, bridge promotion, theorem promotion, or exponent change occurred.

## 2. Exact statement and hypotheses

The audited post-state is the current canonical
`state/proof_obligations.yml`. The authorized patch starts from
`6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
and permits only the following effects:

1. create the proved squarefree-radical sector reduction, the open
   high-radical small-\(t\) residual, and the proved mechanism-scoped
   Möbius/Mellin/joint-\(t\) obstruction;
2. update exactly four inherited M1 obligations, adding one owner dependency
   only to `M9-M1-top-endpoint-signed-cone`;
3. append exactly thirteen `Round181-*` rejected-overclaim records;
4. leave all eighteen named `no_change` obligations deeply unchanged; and
5. preserve every inherited status and theorem statement, especially the
   M1 and M2 parents, M9, both bridges, and all exponent owners.

The official application is hypothesized only to add Round 181, one common
timestamp, and the adjudication reference in the manner specified by
`apply_state_patch`. The audit reconstructs rather than assumes those
generated fields and checks the exact resulting objects.

## 3. Proof and exact derivation

### 3.1 Raw graph, operation inventory, and created objects

The current raw file parses successfully, and `dump_graph` reproduces its
bytes exactly. Raw and canonical SHA-256 are therefore both the applied hash
above. The official validator reports `Graph OK`; an independent reference
scan finds no dangling dependency, implication, or blocker reference.

All operation IDs are distinct within and across arrays. The three created
objects occupy the final three obligation positions in patch order and match
their patch objects exactly, apart from the official generated fields:

1. `M9-M1-hard-top-squarefree-radical-sector-reduction` is
   `proved_internal`, has exactly four declared dependencies, no implication
   or blocker, twelve positive evidence paths, and the single
   applicator-added inconclusive adjudication reference;
2. `M9-M1-hard-top-high-radical-small-t-residual-estimate` is `open`, depends
   only on the reduction, implies only `M9-M1-top-endpoint-signed-cone`, and
   has exactly seven inconclusive paths. The adjudication was already one of
   those seven, so unique merging correctly introduces no duplicate; and
3. `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction` is
   `proved_internal`, has exactly the six declared dependencies, no
   implication or blocker, eleven positive paths, and the single
   applicator-added inconclusive adjudication reference.

Every title, type, track, status, statement, dependency, implication,
blocker, owner, next action, and evidence value in those objects equals the
patch value exactly. All three have `last_updated_round: 181` and
`last_updated_at: 2026-08-27T17:11:21`. All twelve distinct files among the
patch's 49 non-null evidence-path occurrences exist.

### 3.2 Exact inherited-object and rejected-claim deltas

Among the 382 inherited obligations, exactly four objects differ from the
reconstructed starting graph:

1. `M9-M1-top-endpoint-signed-cone` changes only `dependencies`,
   `evidence.inconclusive`, `next_action`, `last_updated_round`, and
   `last_updated_at`; it gains exactly the open residual dependency and the
   seven declared inconclusive paths;
2. `M9-M1-direct-hard-smooth-separate-one-third-minimax` changes only
   `evidence.inconclusive`, `next_action`, and the two metadata fields, with
   exactly five evidence additions;
3. `M9-M1-physical-one-count-assembly` changes only those same four fields,
   with exactly three evidence additions; and
4. `M9-M1` changes only those same four fields, with exactly four evidence
   additions.

The four new next actions equal the patch text exactly, and all four metadata
pairs equal Round 181 at the common observed time. No update receives an
implicit judge-reference addition; its evidence delta is exactly its
declared `evidence_added` list.

The final thirteen rejected-claim records are in patch order. Each equals
the patch ID and reason plus exactly `last_updated_round: 181`, the common
timestamp, and the one-element evidence list containing
`reviews/conductor_round181_adjudication.md` at its full campaign-relative
path. Every one of the 1,502 inherited rejected-claim records is deeply
unchanged. All eighteen `no_change` obligations are also deeply unchanged.

### 3.3 Edge, cycle, scope, and exponent controls

In stored owner-to-dependency orientation, the patch adds exactly twelve
dependency edges: four from the reduction, one from the residual, six from
the obstruction, and the residual dependency on the signed-cone owner. It
adds the residual-to-signed-cone implication and removes no edge. All edge
deltas are thus exhausted by created-node fields and the one declared owner
update.

Tarjan comparison gives three cyclic dependency components before and after,
zero cyclic implication components before and after, and four cyclic
components in the normalized combined proof-flow graph before and after.
The component sets themselves are unchanged, so the patch introduces and
removes no cycle.

Every inherited `status` and `statement_tex` is unchanged. The complete
inherited mutation set is exhausted by the four field deltas in Section 3.2.
In particular, `M9-M1`, `M9-M2`, `M9`, `Conditional-bridge`,
`GC-global-M1-alternative-bridge`, `GC-partial-one-third`,
`GC-external-Li-Yang-theta-star`, and `GC-target` have no unauthorized
status or statement mutation. The strongest internally proved exponent
remains \(1/3\), the accepted external benchmark remains
\(0.3144831759740614\ldots\), and the target \(1/4\) remains open.

### 3.4 Operation-derived inverse and frozen-time official replay

The inverse was built in memory solely from the patch and its recorded
reversibility data:

1. remove the three created obligations;
2. remove the one added owner dependency and the respective 7, 5, 3, and 4
   inherited-node evidence additions;
3. restore the four recorded prior next actions;
4. restore all four prior metadata pairs to Round 119 at
   `2026-08-22T00:55:39`; and
5. remove the thirteen appended rejected-claim records.

The result passes `validate_graph`, contains 382 obligations and 1,502
rejected claims, and canonically hashes exactly to
`6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`.

The repository's official `apply_state_patch` was then run in memory on that
recovered object with its clock frozen to `2026-08-27T17:11:21`, Round index
181, and judge reference
`rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/conductor_round181_adjudication.md`.
Its five returned ID arrays equal the patch arrays in content and order. The
replayed object, canonical bytes, and SHA-256 are exactly the current graph,
including the judge-evidence merge behavior described above.

## 4. First doubtful or unproved step

There is no doubtful or unproved step in the mechanical graph scope,
operation realization, evidence merge, exact inversion, or frozen-time
replay. **First mechanical defect: NONE.**

The first mathematical step still unproved is the literal signed residual

\[
 \left|\sum_{\substack{s>L,\ \mu^2(s)=1\\
                        1\le t<\lceil\sqrt L\rceil}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\]

already on the mandatory \(t=1\) face. Round 181 represents a strict
subordinate reduction and mechanism obstruction, not a proof of the hard M1
parent or an exponent improvement.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Raw applied hash | **PASS.** `fec130bc66641cbdad18c832de10077a7825f1caaf5d10170a67ef65c0b27196`. |
| Raw/canonical byte equality | **PASS.** Exact byte equality. |
| Official and independent graph validity | **PASS.** Zero issues and zero dangling references. |
| Applied graph counts | **PASS.** 385 obligations and 1,515 rejected claims. |
| Realized operation inventory | **PASS.** Exact `3/4/0/13/18`, including order. |
| Three created objects | **PASS.** Exact patch fields plus only official Round/time/judge effects. |
| Four inherited updates | **PASS.** Exact fields, evidence additions, next actions, dependency, and metadata. |
| Judge evidence | **PASS.** Exact unique merge on creates and exact one-element evidence on all thirteen reject records. |
| Rejected-claim quarantine | **PASS.** Thirteen exact appended records; all 1,502 inherited records unchanged. |
| No-change scope | **PASS.** All eighteen objects deeply equal. |
| Status and statement quarantine | **PASS.** Zero inherited drift. |
| Edge and cycle scope | **PASS.** Twelve dependency and one implication additions, no removals, no SCC change. |
| Parent, bridge, theorem, and exponent quarantine | **PASS.** No promotion or statement change. |
| Exact inverse validity and count | **PASS.** 382 obligations, 1,502 rejected claims, zero validation issues. |
| Exact inverse SHA-256 | **PASS.** `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`. |
| Frozen-time official replay | **PASS.** Exact object, bytes, operation arrays, and applied hash. |
| Authoritative-state mutation by this audit | **PASS.** None. |

No numerical theorem experiment, web source, or external theorem was used.

## 6. Dependencies and exact artifacts used

This audit used exactly:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/plan.json`;
5. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/state_patch.json`;
6. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/synthesis.md`;
7. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/conductor_round181_adjudication.md`;
8. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/reviews/final_kernel_mathematical_scope_review.md`;
9. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/controls/preapply_independent_reverse_audit.md`;
10. the twelve distinct evidence files referenced by the State Patch;
11. `math_collab/proof_obligations.py`; and
12. `math_collab/validate_state_patch.py`.

The official validator, independent object and field comparison, evidence
existence scan, edge scan, Tarjan SCC comparison, operation-derived inverse,
and frozen-time official replay were read-only with respect to authoritative
state.

## 7. Recommended state effect

Retain the applied Round-181 graph exactly as written. No corrective State
Patch is needed. Preserve the high-radical small-\(t\) residual, especially
its \(t=1\) face, as open; preserve the independent smooth M1 parent, M9-M1,
M9-M2, M9, endpoint uniformity, both bridges, the quarter theorem, and all
exponent owners at their inherited status.

**GREEN -- first exact defect: NONE.**
