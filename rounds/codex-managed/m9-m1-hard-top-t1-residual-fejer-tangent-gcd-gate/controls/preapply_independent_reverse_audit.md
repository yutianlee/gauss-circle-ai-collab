# Round 185 preapplication State Patch and exact reverse audit

## 1. Result / verdict

**Verdict: GREEN.**

The frozen starting graph, State Patch, adjudication, and synthesis hashes
match the brief exactly.  The patch has inventory

\[
 (\mathrm{create},\mathrm{update},\mathrm{correct},
   \mathrm{reject},\mathrm{no\_change})=(1,1,0,20,31).
\]

An independent in-memory application produced a graph with 388 unique
obligations and 1579 unique rejected-claim records, no dangling reference,
no new dependency cycle, and no protected semantic drift.  Applying the
stated inverse recovered the 387-obligation, 1559-rejection starting object
and its canonical bytes exactly, with SHA-256
`f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`.
No graph or shared-state file was modified.

## 2. Exact statement and hypotheses

The audit fixes the graph at SHA-256
`f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`
and the patch at SHA-256
`2d4734c8a4b61acdd2081a4cad785ab56d05aac112c464935cf6916a3e9d6e4e`.
The only permitted forward mutations are:

1. create
   `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction` with status
   `proved_internal`, five stated direct dependencies, empty implication and
   blocker lists, and 15 positive evidence paths;
2. update the still-open
   `M9-M1-hard-top-high-radical-small-t-residual-estimate` by adding only the
   created node as a dependency, the same 15 paths as inconclusive evidence,
   and the stated narrowed high-height next action, together with ordinary
   Round-185 last-updated metadata;
3. append the 20 stated rejected-claim records; and
4. leave all 31 `no_change` obligations unchanged.

The inverse must remove the created node and the 20 introduced rejection
records, remove the one added dependency and all 15 added evidence values,
restore the owner's exact previous `next_action`, restore
`last_updated_round: 184` and
`last_updated_at: 2026-08-27T22:44:48`, and recover the canonical starting
graph byte for byte.

## 3. Proof / forward-and-reverse derivation

### Frozen inputs and operation domains

The four controlling hashes reproduce exactly:

- graph: `f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`;
- patch: `2d4734c8a4b61acdd2081a4cad785ab56d05aac112c464935cf6916a3e9d6e4e`;
- adjudication: `f69030851b6c187e3428d27870367804b486541537387ea3b52a10a784a33914`;
- synthesis: `611651ecdda5a3c773228299929cf9fde5b2e807dfe5bf3c479f2947b9141f72`.

The starting graph parses as 387 uniquely identified obligations and 1559
uniquely identified rejected claims, with disjoint ID namespaces.  Every
starting dependency, implication, and blocker resolves to an obligation.
The created ID is absent initially; the updated and all protected IDs exist;
the 20 rejected IDs are new; and the create, update, reject, and protected
operation sets contain no internal duplicate or forbidden overlap.

Every one of the 15 evidence paths exists as a file.  The added dependency
and all 15 inconclusive evidence values are absent from the owner's starting
lists, so the inverse can remove them without deleting inherited data.  The
owner starts with three dependencies and 48 inconclusive evidence paths and
would end with four and 63, respectively.

### Dependency direction and graph integrity

All five direct dependencies of the created node exist and have status
`proved_internal`:

- `M9-M1-hard-top-t1-comparable-factor-exchange-sector`;
- `M9-M1-top-endpoint-transform`;
- `M9-M1-frequency-phase-diagram-R10`;
- `M9-M2-dyadic-weight-nondegeneracy`; and
- `Divisor-bound-elementary`.

The new edge is directed from the open owner to the new subordinate node;
the new node then points to those five accepted dependencies.  There is no
reverse edge to the owner and no new implication or blocker.  After the
simulation, obligation and rejection IDs remain unique and disjoint, and
all dependency, implication, and blocker references resolve.

The starting dependency graph has 384 strongly connected components,
including three pre-existing two-node cyclic components.  The simulated
graph has 385 components and exactly the same three cyclic components.  The
new node is a singleton component, so the patch introduces no cycle or SCC
merge.

### Scope and adjudication agreement

For every inherited obligation, the type, track, title, status, statement,
implications, blockers, and owner are unchanged.  Each of the 31 protected
records is wholly unchanged.  The updated residual owner remains `open`;
its statement, implications, and blockers are unchanged.  The new node has
empty `implies` and `blockers`, so it cannot mechanically close a parent.

The parent and exponent ledger remains:

- the hard residual owner, hard signed cone, smooth residual parent,
  `M9-M1`, `M9-M2`, endpoint uniformity, `M9`, and `GC-target` are `open`;
- `M9-M1-physical-one-count-assembly` remains `proved_internal` only as its
  existing conditional reduction;
- both bridges remain `derived_under_assumptions`;
- `GC-partial-one-third` remains `proved_internal`; and
- `GC-external-Li-Yang-theta-star` remains
  `proved_external_dependency`.

This is exactly the adjudication's decision: create one strict subordinate
finite-reduction/bounded-height node, add only subordinate inconclusive
evidence and a dependency to the open owner, narrow that owner's next
action to the high-\(h\) signed relation, record the audited overclaims, and
change no inherited theorem, status, implication, blocker, bridge, target,
or exponent.

### Exact inverse

In memory I removed each of the 20 introduced rejection records exactly
once, removed the added owner dependency exactly once, removed each of the
15 added inconclusive paths exactly once, restored the recorded
`next_action` and metadata, and removed the created obligation exactly
once.  The resulting parsed object equals the starting object.

The starting file is already its canonical serialization: UTF-8 without a
BOM, LF line endings, two-space JSON indentation, ASCII escaping, preserved
key order, and one terminal newline.  Canonically serializing the inverse
produced byte-for-byte equality with the 2,000,409-byte starting file and
the same frozen SHA-256.  The recovery is independent of the forward
application timestamp because all new records are deleted and the sole
inherited record's metadata is explicitly restored.

## 4. First doubtful or unproved step

There is no failing State Patch or reversibility step.  The first unproved
mathematical relation remains the dyadic high-height signed estimate
(K185.37), requiring the full factor \(Y\) for \(Y<h\leq2Y\).  The patch
does not promote that relation: it places it only in the new node's and the
open owner's `next_action` text.  This open mathematical boundary is
therefore not a graph-audit defect.

## 5. Required controls and outcomes

1. **Frozen hashes and canonical input:** all four required hashes match;
   the graph's raw bytes equal its canonical serialization.  Passed.
2. **Inventory:** create 1, update 1, correct 0, reject 20, no-change 31.
   Passed.
3. **IDs and evidence:** every operated ID is in the required starting
   domain, every evidence path exists, and no added dependency or evidence
   value pre-exists.  Passed.
4. **References and direction:** no dangling dependency, implication, or
   blocker occurs before or after the simulation; the owner-to-subordinate
   edge has the correct direction.  Passed.
5. **Duplicates and cycles:** no duplicate ID is introduced; the three
   pre-existing dependency cycles are unchanged and no cycle is added.
   Passed.
6. **Protected semantics:** all 31 protected full records and every
   inherited status, statement, implication, and blocker are unchanged.
   Passed.
7. **Owner, bridge, target, and exponent quarantine:** every stated parent,
   bridge, terminal target, and exponent record retains its starting status
   and statement.  Passed.
8. **Adjudication agreement:** the node, dependencies, evidence roles,
   narrowed next action, rejected claims, and non-promotions agree exactly
   with the adjudication and synthesis.  Passed.
9. **Reverse audit:** removal and restoration reproduce the starting object,
   canonical bytes, and SHA-256 exactly.  Passed.

The 20 individually checked rejected IDs are:

- `Round185-even-parity-connector-saves-a-power`;
- `Round185-monotone-tangent-sector-proves-the-residual`;
- `Round185-original-gcd-tail-with-shrinking-gamma-is-uniformly-target-safe`;
- `Round185-cross-gcd-tail-with-shrinking-delta-is-uniformly-target-safe`;
- `Round185-high-g-or-high-kappa-sectors-cover-the-opposing-complement`;
- `Round185-bare-affine-character-alternation-contracts-the-literal-fibre`;
- `Round185-rowwise-Abel-and-positive-recombination-prove-the-residual`;
- `Round185-O1-per-primitive-row-closes-the-correlation`;
- `Round185-positive-shift-triangle-proves-the-Fejer-target`;
- `Round185-M2-tangent-gcd-estimate-transfers-as-an-M1-theorem`;
- `Round185-positive-Poisson-Bprocess-or-alias-energy-closes-the-residual`;
- `Round185-primitive-conductor-centering-gains-the-missing-factor`;
- `Round185-orientation-reflection-or-complementary-factor-exchange-is-a-literal-self-return`;
- `Round185-residual-neither-both-pairing-self-returns-inside-the-hard-cone`;
- `Round185-exact-deletion-control-proves-literal-lower-mass`;
- `Round185-unrestricted-or-noncanonical-affine-sum-is-the-exact-complement`;
- `Round185-bounded-h-sector-proves-the-complete-t1-residual`;
- `Round185-dyadic-high-h-signed-relation-is-proved`;
- `Round185-complete-t1-would-prove-the-hard-small-t-owner`; and
- `Round185-strict-tangent-gcd-sector-improves-a-global-exponent`.

The 31 individually checked protected obligation IDs are:

- `M9-M1-hard-top-t1-comparable-factor-exchange-sector`;
- `M9-M1-hard-top-squarefree-radical-sector-reduction`;
- `M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector`;
- `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction`;
- `M9-M1-top-endpoint-transform`;
- `M9-M1-frequency-phase-diagram-R10`;
- `M9-M1-top-endpoint-signed-cone`;
- `M9-M1-shifted-divisor-correlation-PSC`;
- `M9-M1-direct-smooth-residual-blockwise-estimate`;
- `M9-M1-direct-hard-smooth-separate-one-third-minimax`;
- `M9-M1-physical-one-count-assembly`;
- `M9-M1-global-angular-radial-estimate`;
- `M9-M1-global-lower-radial-signed-estimate`;
- `M9-M1-global-radial-one-count-assembly`;
- `M9-M1`;
- `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`;
- `M9-M2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-reduction`;
- `M9-M2-hard-top-t1-residual-k17a-primitive-alias-conductor-reduction`;
- `M9-M2-hard-top-t1-residual-k17a-primitive-conductor-parity-self-return`;
- `M9-M2-top-endpoint-signed-cone`;
- `M9-M2-smooth-balanced-quarter-packet-estimate`;
- `M9-M2-smooth-unbalanced-three-quarter-estimate`;
- `M9-M2-physical-one-count-assembly`;
- `M9-M2`;
- `M9-endpoint-uniformity`;
- `M9`;
- `Conditional-bridge`;
- `GC-global-M1-alternative-bridge`;
- `GC-partial-one-third`;
- `GC-external-Li-Yang-theta-star`; and
- `GC-target`.

## 6. Dependencies and exact artifacts used

Only the context authorized by the brief was used:

- `protocol.md`, SHA-256
  `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
- `state/proof_obligations.yml`, SHA-256
  `f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0`;
- `state/active_campaign.yml`, SHA-256
  `d67f738e38fcd5288773d12b8b0dc6dd22440f9ebe98bbc0d020cd7b11c82ab6`;
- the controlling preapplication brief;
- `state_patch.json`, SHA-256
  `2d4734c8a4b61acdd2081a4cad785ab56d05aac112c464935cf6916a3e9d6e4e`;
- `reviews/conductor_round185_adjudication.md`, SHA-256
  `f69030851b6c187e3428d27870367804b486541537387ea3b52a10a784a33914`;
- `synthesis.md`, SHA-256
  `611651ecdda5a3c773228299929cf9fde5b2e807dfe5bf3c479f2947b9141f72`;
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`,
  SHA-256
  `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`;
- `reviews/final_kernel_candidate_consistency_review.md`, SHA-256
  `c551077a045ee94157529c5f26d9288a59091cdac6ed65f34ca01ac83551899e`;
- `reviews/final_kernel_power_owner_scope_review.md`, SHA-256
  `056a1fdfc17f33bba70617a9d7b4b950e5b11dc8b261ae5fcd84a7f98658e8cd`;
  and
- `reviews/final_kernel_formalization_provenance_hygiene_review.md`, SHA-256
  `c2c2051aef29030fd00e33967289d728a0854219604ff674900810d0f629b93d`.

All 15 evidence paths named by the patch were checked for file existence;
no additional artifact content was used.  The application, graph checks,
SCC comparison, and inverse were bounded exact in-memory operations.  No
web source, external theorem, or numerical theorem evidence was used.

## 7. Recommended state effect

Accept this control as the independent GREEN preapplication reverse audit.
The conductor may mechanically apply exactly the frozen State Patch.  It
must promote only the new strict subordinate finite-reduction and
bounded-height sector, keep the high-height signed relation and every
owner, parent, bridge, target, and exponent claim at their inherited
scope, and make no mutation beyond the audited operations.  This report
itself authorizes and performs no graph or shared-state edit.
