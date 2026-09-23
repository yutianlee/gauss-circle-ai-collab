# Round 185 postapplication graph reverse and frozen-time replay audit

## 1. Result / verdict

**Verdict: GREEN**

The actual graph, frozen State Patch, inverse, frozen-time replay, graph
validation, protected scope, and exponent quarantine all pass. The actual
graph has SHA-256

\[
 f43248060d7876a96d4554cd13372dbf267387bcbe44a832b87cd5f571801575,
\]

and the patch has SHA-256

\[
 2d4734c8a4b61acdd2081a4cad785ab56d05aac112c464935cf6916a3e9d6e4e.
\]

The exact inverse canonically recovers the 2,000,409-byte starting graph
with SHA-256

\[
 f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0.
\]

Reapplying the frozen patch to that recovered object at
2026-08-28T02:16:28, with Round 185 and the stated adjudication reference,
produces 2,017,343 canonical bytes that are byte-identical to the actual
graph.

## 2. Exact statement and hypotheses

The audit fixes:

- operation inventory
  \((\mathrm{create},\mathrm{update},\mathrm{correct},
  \mathrm{reject},\mathrm{no\_change})=(1,1,0,20,31)\);
- application round \(185\);
- application timestamp 2026-08-28T02:16:28; and
- judge reference
  rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/conductor_round185_adjudication.md.

The permitted delta is exactly:

1. create
   M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction, with the five
   stated dependencies, 15 positive evidence paths, the judge reference as
   application-level inconclusive evidence, and Round-185 metadata;
2. update only
   M9-M1-hard-top-high-radical-small-t-residual-estimate by appending one
   dependency and the 15 patch evidence paths, replacing its next action,
   and stamping the frozen round and time;
3. append the 20 patch rejection records, each with the frozen round, time,
   and sole judge-reference evidence; and
4. leave every other inherited record, including all 31 protected
   no-change obligations, untouched.

Canonical serialization means UTF-8, LF line endings, preserved object and
array order, two-space JSON indentation, ASCII escaping, and one terminal
newline.

## 3. Proof / delta, inverse, and replay derivation

### Frozen inputs and actual inventory

The actual graph and patch are already canonical serializations of their
parsed objects. The graph contains 388 uniquely identified obligations and
1579 uniquely identified rejected claims; the two ID namespaces are
disjoint. The patch inventory is exactly \(1/1/0/20/31\), with unique,
nonoverlapping create, update, reject, and protected ID sets.

The created ID occurs exactly once in the actual obligation list. The
updated and all protected IDs exist. Every one of the 20 rejected IDs
occurs exactly once, and none belonged to the recovered starting graph.
All 15 positive or added evidence paths exist as files.

### Created, updated, rejected, and judge-reference records

The created obligation agrees field for field with the patch. Its status is
proved_internal; its implication and blocker lists are empty; its five
dependencies are exactly

- M9-M1-hard-top-t1-comparable-factor-exchange-sector;
- M9-M1-top-endpoint-transform;
- M9-M1-frequency-phase-diagram-R10;
- M9-M2-dyadic-weight-nondegeneracy; and
- Divisor-bound-elementary.

All five dependencies exist and have status proved_internal. The created
record has exactly 15 positive evidence paths, no negative evidence, the
adjudication path as its sole inconclusive application evidence,
last_updated_round \(185\), and the frozen timestamp.

The updated owner changes in exactly five field locations:

\[
 \{\text{dependencies},\ \text{evidence.inconclusive},\
   \text{next_action},\ \text{last_updated_round},\
   \text{last_updated_at}\}.
\]

Its dependency count changes from three to four by appending only the new
subordinate node. Its inconclusive evidence count changes from 48 to 63 by
appending exactly the 15 patch paths. Its status remains open, and its
statement, implications, blockers, type, track, title, positive evidence,
negative evidence, and owner are unchanged.

Each of the 20 new rejected records has exactly the patch ID and reason,
then the frozen timestamp, Round 185, and a one-element evidence list
containing the judge reference. No inherited rejected record changes.

### References, direction, SCCs, and protected scope

There is no dangling dependency, implication, or blocker in either the
recovered starting graph or the actual graph. The new edge points from the
open residual owner to the new subordinate node. The subordinate node
points only to its five accepted inputs and has no reverse edge to its
owner.

The recovered graph has 384 dependency strongly connected components; the
actual graph has 385. Both have the same three pre-existing two-node cyclic
components. The new node is a singleton component, so no cycle or SCC merge
is introduced.

All 31 no-change obligation records are byte-semantically unchanged. More
strongly, among all inherited obligations only the named open residual
owner differs, and among inherited rejected claims none differs. The
following protected status and statement ledger is unchanged:

- the residual owner, hard signed cone, smooth residual parent, M9-M1,
  M9-M2, endpoint uniformity, M9, and GC-target remain open;
- M9-M1-physical-one-count-assembly remains proved_internal only in its
  inherited conditional-reduction sense;
- both bridge nodes remain derived_under_assumptions;
- GC-partial-one-third remains proved_internal; and
- GC-external-Li-Yang-theta-star remains
  proved_external_dependency.

Their implications and blockers are also unchanged. Hence the internal
\(1/3\), accepted external \(0.3144831759740614\ldots\), and target
\(1/4\) exponent records are quarantined exactly.

### Exact inverse

Starting from the actual parsed graph, the inverse:

1. removes the one created obligation;
2. removes each of the 20 new rejection records exactly once;
3. removes the new owner dependency exactly once;
4. removes each of the 15 added inconclusive evidence paths exactly once;
5. restores the owner's frozen prepatch next action; and
6. restores last_updated_round \(184\) and
   last_updated_at 2026-08-27T22:44:48.

The result has 387 obligations and 1559 rejected claims. Its canonical
serialization is 2,000,409 bytes, is stable under parse and reserialization,
and has the exact starting SHA-256. Thus no unlisted actual mutation can
remain: any such mutation would change the recovered canonical hash.

### Frozen-time replay

From the recovered starting object, the replay appends the created record,
adds the judge reference to its inconclusive application evidence, stamps
the frozen round and time, applies the single owner update in list order,
and appends the 20 rejection records with their judge and metadata fields
in canonical application order. The resulting object passes all reference,
ID, status, track, and SCC checks.

Its canonical serialization has the exact applied SHA-256 and is
byte-for-byte equal to the current state/proof_obligations.yml. This
separate replay verifies not merely object equivalence but exact ordering,
metadata, evidence roles, judge-reference placement, and frozen-time
serialization.

## 4. First doubtful or unproved step

There is no failing graph, inverse, replay, reference, scope, or exponent
step. The first unproved mathematical relation remains (K185.37), the
global dyadic high-height signed estimate requiring the full factor \(Y\).
The new subordinate node and the updated owner's next action identify that
relation as open; no status, implication, blocker, bridge, theorem, or
exponent claims it as proved.

## 5. Required controls and outcomes

1. **Frozen hashes.** Protocol, patch, adjudication, synthesis, durable
   kernel, and all three final-kernel reviews match their recorded hashes;
   the actual graph matches the applied hash. Outcome: passed.
2. **Inventory and IDs.** Counts are \(1/1/0/20/31\); actual and recovered
   obligation/rejection counts are \(388/1579\) and \(387/1559\);
   all IDs are unique and namespaces disjoint. Outcome: passed.
3. **Created and updated evidence.** The new node has \(15\) positive and
   one judge-reference inconclusive path; the owner changes from
   \(3\) to \(4\) dependencies and from \(48\) to \(63\) inconclusive
   paths. Outcome: passed.
4. **Rejected records.** All 20 IDs, reasons, timestamps, round fields, and
   judge-reference evidence lists match exactly; inherited rejections do
   not change. Outcome: passed.
5. **References and direction.** Zero dangling references occur before or
   after application, and the owner-to-subordinate edge has the required
   direction. Outcome: passed.
6. **SCC control.** Component counts are \(384\) before and \(385\) after;
   the same three pre-existing cycles remain, and the new node is a
   singleton. Outcome: passed.
7. **Protected scope.** All 31 no-change records and the complete owner,
   bridge, target, and exponent ledger retain their protected semantics.
   Outcome: passed.
8. **Exact inverse.** Canonical recovery gives 2,000,409 bytes and the
   frozen starting hash. Outcome: passed.
9. **Frozen-time replay.** Canonical replay gives 2,017,343 bytes, the
   frozen applied hash, and byte identity with the actual graph. Outcome:
   passed.

All simulations were bounded exact in-memory operations. No graph or shared
state was written.

## 6. Dependencies and exact artifacts used

- protocol.md, SHA-256
  f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a
- state/proof_obligations.yml, SHA-256
  f43248060d7876a96d4554cd13372dbf267387bcbe44a832b87cd5f571801575
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/postapply_graph_reverse_replay_audit.md
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/state_patch.json,
  SHA-256
  2d4734c8a4b61acdd2081a4cad785ab56d05aac112c464935cf6916a3e9d6e4e
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/controls/preapply_independent_reverse_audit.md,
  SHA-256
  a4c8780046e0c6bdb0f493aa12584037cccfc004bd1472afe8b62681dc27ef28
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/conductor_round185_adjudication.md,
  SHA-256
  f69030851b6c187e3428d27870367804b486541537387ea3b52a10a784a33914
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/synthesis.md,
  SHA-256
  611651ecdda5a3c773228299929cf9fde5b2e807dfe5bf3c479f2947b9141f72
- proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md,
  SHA-256
  4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/final_kernel_candidate_consistency_review.md,
  SHA-256
  c551077a045ee94157529c5f26d9288a59091cdac6ed65f34ca01ac83551899e
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/final_kernel_power_owner_scope_review.md,
  SHA-256
  056a1fdfc17f33bba70617a9d7b4b950e5b11dc8b261ae5fcd84a7f98658e8cd
- rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/final_kernel_formalization_provenance_hygiene_review.md,
  SHA-256
  c2c2051aef29030fd00e33967289d728a0854219604ff674900810d0f629b93d

No other artifact content, web source, or external theorem was used. The
entire graph was parsed and validated in memory; no temporary graph or
script file was created.

## 7. Recommended state effect

Accept the applied graph as the exact frozen Round-185 State Patch result
and accept this control as its independent postapplication reverse and
replay verification. Keep the new node strictly subordinate, retain
(K185.37) and every complete residual, owner, parent, endpoint-uniformity,
bridge, target, and exponent claim at its inherited open or
assumption-qualified status, and make no further state mutation from this
audit.

