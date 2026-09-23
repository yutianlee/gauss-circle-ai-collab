# Round 183 post-application independent graph and reverse audit

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: `183`
- Role: independent post-application graph, scope, evidence, and reverse auditor
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Applied graph SHA-256:
  `a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`
- Patch SHA-256:
  `76dc7056223137d9525ecb3c58b66077ec4986530d1bc547a741a1735b460052`
- Application metadata time: `2026-08-27T20:38:45`

## 1. Result and verdict

**GREEN.**  The current canonical graph is exactly the graph produced by
the audited Round-183 patch with `round_index=183` and no `judge_ref`.
Raw bytes equal canonical serialization and hash to the declared applied
SHA-256.  The realized ledger is exactly

\[
 \boxed{1\ \mathrm{create}/2\ \mathrm{update}/0\
 \ \mathrm{correct\text{-}rejected}/13\ \mathrm{reject}/24\
 \ \mathrm{no\text{-}change}}.
\]

An operation-derived inverse recovers the exact starting graph, and
official reapplication with the clock frozen to the observed application
time reproduces the current object, bytes, operation arrays/order, and hash.
No unauthorized field, status, statement, edge, cycle, parent, bridge,
theorem, or exponent drift occurred.

## 2. Exact applied statement and hypotheses

The sole created obligation is
`M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector`.  Its actual
object equals the patch object exactly, plus only
`last_updated_round: 183` and
`last_updated_at: 2026-08-27T20:38:45`.

It is `proved_internal` only for the literal **incidence-level** sector

\[
 G\geq\lceil L^{1/4}\rceil,
 \qquad
 \operatorname{dist}(2\sqrt{Xuv},\mathbb Z+\tfrac12)
 \geq(10\log(2X))^{-1},
\]

after expanding the exact divisor coefficient.  Its exact incidence
complement is the small-(G) and near-resonant union and contains the
complete (t=1) face.  The node has five proved dependencies, no
implication, and no blocker.

The complete small-(t) obligation remains `open`.  It gains the created
sector as one prerequisite, exact inconclusive evidence, and a next action
for the still-open complement.  The pre-existing
Mobius/Mellin/joint-(t) obstruction remains `proved_internal`; its
statement is refined only by the proved two-cutoff kernel, target-safe
large-divisor tail, and small-core self-return.  Fixed-row Fejer correlation
remains an unproved stronger sufficient mechanism and is not PSC or an
owner.

## 3. Proof and exact derivation

### 3.1 Actual object and evidence delta

The applied graph validates with 386 obligations and 1,544 rejected-claim
records.  The created obligation is the final obligation in patch order.
The thirteen new rejected records are the final thirteen records in patch
order; each equals its patch ID/reason plus exactly the generated round and
application-time fields.  No judge-evidence field was added, confirming the
authorized no-`judge_ref` application.

After constructing the exact inverse, comparison with the current graph
shows only these inherited deltas:

1. `M9-M1-hard-top-high-radical-small-t-residual-estimate` changes only
   `dependencies`, `evidence`, `next_action`, `last_updated_round`, and
   `last_updated_at`; it gains exactly one dependency and thirteen
   inconclusive paths;
2. `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction` changes only
   `statement_tex`, `evidence`, `next_action`, `last_updated_round`, and
   `last_updated_at`; it gains exactly ten positive paths.

Both metadata pairs are exactly round 183 at `2026-08-27T20:38:45`.
Every other inherited obligation is deeply equal to the recovered starting
object.  All twenty-four no-change objects are deeply equal, and the first
1,531 rejected records form an unchanged prefix.

The created node has exactly the eleven declared positive paths.  Across
the patch there are 34 evidence-path occurrences and 13 distinct paths;
all thirteen still exist.  Candidate, durable kernel, and patch hashes
remain respectively
`e23d4135401c81c263026fddf19df4d46536eaabaa33fa9a7a0d8b287ea82f91`,
`f8898d48d1d8db3fcb767399b9825568d27a0fd32bb45b1b3de02a51154692d1`,
and
`76dc7056223137d9525ecb3c58b66077ec4986530d1bc547a741a1735b460052`.

### 3.2 Dependency, implication, blocker, and cycle audit

The exact relation delta is:

| relation | before | after | dangling before/after | added | removed | cyclic SCCs before/after |
|---|---:|---:|---:|---:|---:|---:|
| dependencies | 1,362 | 1,368 | 0 / 0 | 6 | 0 | 3 / 3 |
| implications | 326 | 326 | 0 / 0 | 0 | 0 | 0 / 0 |
| blockers | 70 | 70 | 0 / 0 | 0 | 0 | 0 / 0 |
| normalized combined proof flow | 1,474 | 1,480 | 0 / 0 | 6 | 0 | 4 / 4 |

The six dependency additions are exactly the created node's five declared
proved inputs and the open complete owner's dependency on the created
strict-sector fact.  This is the correct stored owner-to-prerequisite
direction.  The cyclic component sets, not merely their counts, are
unchanged for every relation and for normalized combined proof flow.

### 3.3 Protected status, statement, and exponent scope

The only new proof status is the authorized subordinate strict-sector
node.  Every inherited status is unchanged.  The complete owner and hard
signed cone remain open; smooth M1, GAR, M9-M1, all M2 owners, endpoint
uniformity, M9, and the quarter target remain open.  Both bridges remain
`derived_under_assumptions`.

The only inherited `statement_tex` mutation is the authorized refinement
of the already proved mechanism obstruction.  It explicitly denies a
literal-owner refutation or parent/exponent implication.  The complete
owner's statement, every protected parent/bridge/theorem statement, and all
implication edges are unchanged.

Therefore the strongest internally proved exponent remains (1/3), the
accepted external Li--Yang benchmark remains
(0.3144831759740614\ldots), and the target remains (1/4).

### 3.4 Exact inverse and frozen-time official replay

The inverse was constructed solely from the patch's operation arrays and
reversibility fields:

1. remove the created obligation;
2. remove the added owner dependency and the exact 13/10 evidence additions;
3. restore both old next actions, the obstruction's old `statement_tex`,
   and both old metadata pairs; and
4. remove the thirteen appended rejected records.

The reversed graph contains 385 obligations and 1,531 rejected claims,
passes validation, and canonically hashes exactly to

`5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`.

With the official applicator clock frozen to
`2026-08-27T20:38:45`, round 183, and no `judge_ref`, reapplication of the
same patch to that recovered graph returns the exact five operation arrays
in patch order.  The replayed graph is object-equal and byte-equal to the
current file and hashes exactly to

`a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`.

## 4. First doubtful or unproved step

There is no doubtful step in actual-operation realization, field scope,
evidence merge, metadata, edge/cycle comparison, exact inverse, or
frozen-time replay.  **First mechanical defect: none.**

The first unproved mathematical step remains the exact small-(G) and
near-half-integer-resonant incidence complement, especially the complete
(t=1) cone.  The fixed-row signed Fejer brace is likewise unproved at
(t=1).  The applied graph records these limitations rather than promoting
the complete owner.

## 5. Required controls and outcomes

| control | outcome |
|---|---|
| raw applied hash and canonical bytes | **PASS**; exact `a8e0e5d8...` |
| official graph validation | **PASS**; zero issues |
| applied counts | **PASS**; 386 obligations / 1,544 rejected claims |
| realized operation inventory/order | **PASS**; exact `1/2/0/13/24` |
| created object and metadata | **PASS**; exact patch plus round/time only |
| two inherited updates | **PASS**; exact authorized fields and evidence |
| rejected records | **PASS**; exact appended tail, no judge evidence |
| no-change objects / inherited prefix | **PASS**; deeply unchanged |
| evidence paths and frozen artifact hashes | **PASS** |
| dependency direction and exact edge delta | **PASS** |
| dangling references | **PASS**; zero before and after |
| dependency/implication/blocker/combined SCC delta | **PASS**; none |
| inherited status and statement quarantine | **PASS** |
| protected parents, bridges, theorems, exponents | **PASS** |
| exact inverse count/validation/hash | **PASS**; exact `5965e356...` |
| frozen-time reverse/reapply object and bytes | **PASS**; exact applied hash |
| authoritative-state mutation by this audit | **PASS**; none |

No numerical theorem experiment, web source, or external theorem was used.
All machine work was bounded graph, hash, path, field, SCC, reversal, and
deterministic-replay control.

## 6. Dependencies and exact artifacts used

This audit used:

1. `protocol.md`;
2. the current applied `state/proof_obligations.yml`;
3. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/state_patch.json`;
4. the hash-locked conductor candidate and durable kernel;
5. all thirteen evidence artifacts named by the patch;
6. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/conductor_round183_adjudication.md`;
7. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/synthesis.md`;
8. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/controls/preapply_independent_reverse_audit.md`;
9. `math_collab/proof_obligations.py`; and
10. `math_collab/validate_state_patch.py`.

No graph, patch, candidate, kernel, synthesis, review, validation matrix,
or lifecycle artifact was edited.

## 7. Recommended state effect

Retain the applied graph exactly as written.  No corrective State Patch is
needed.  Proceed to the proof-draft update, Round-183 lifecycle closure, and
final hygiene review while preserving the open exact complement.

The sole analytic promotion is the subordinate nonresonant primitive-ray
incidence-sector lemma; the only other proved mutation is the
mechanism-scoped truncated-Mobius self-return refinement.  No hard parent,
smooth M1 parent, GAR, M9-M1, M2 owner, endpoint claim, M9, bridge, theorem,
or exponent has changed.

**Final verdict: GREEN -- first exact defect: none.**
