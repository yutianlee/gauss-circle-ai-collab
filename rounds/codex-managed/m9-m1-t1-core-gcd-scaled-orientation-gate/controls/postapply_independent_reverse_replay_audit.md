# Round 193 post-apply independent reverse/replay audit

## 1. Result

**PASS.** The live graph is the exact canonical production application of the declared Round 193 State Patch. An independent in-memory inverse recovers the declared canonical starting hash, and production replay with the recovered generated inputs reproduces the live bytes exactly. No shared graph or state file was mutated.

- Patch SHA-256: `dda2bc4af723b3e1d20c850904c6cca64360708927c80f836c0c857d91c4057a`
- Declared and recovered starting graph SHA-256: `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- Live and replayed graph SHA-256: `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`
- First defect: **none**

## 2. Recovered application inputs

The generated metadata was recovered independently from the created obligation, the updated owner, and all 15 newly rejected-claim records:

- Round index: `193`
- Application timestamp: `2026-08-30T02:10:41`
- Judge reference: `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/conductor_round193_adjudication.md`

Every affected record carries the same recovered round and timestamp. The judge reference is the sole extra inconclusive entry on the created node relative to its patch payload and is also the evidence reference on every new rejected-claim record. This uniquely identifies the production `judge_ref` input.

## 3. Exact operation and delta audit

The patch and the production replay both report exactly:

| Operation | Count |
|---|---:|
| create | 1 |
| update | 1 |
| correct rejected claim | 0 |
| reject | 15 |
| no change | 25 |

The obligation count changes from 393 to 394, and the rejected-claim count changes from 1697 to 1712. Among the 393 pre-existing obligations, exactly one deep object changes:

`M9-M1-hard-top-high-radical-small-t-residual-estimate`

That is the sole declared update owner. The one created ID was absent from the inverse graph, all 15 rejected IDs were absent from its rejected-claim register, and all introduced records appear in patch order under production application.

All 25 declared no-change obligations resolve and are deep-equal between the recovered starting graph and the live graph. This includes the protected accepted Round 187--192 sector nodes, M9-M1 and M9-M2 parents and assemblies, M9, both bridges, the endpoint node, both accepted exponent nodes, the target, and the elementary divisor bound.

## 4. Evidence and dependency audit

The patch contains 23 unique repository evidence paths, and all 23 exist. The recovered judge reference also exists and is already one of those 23 unique paths; production adds it in the additional evidence locations described above. Evidence bucket contents and ordering in the live graph are reproduced exactly.

The created node depends on `M9-M1-hard-top-t1-rho-large-farey-covector-reduction`, and the owner gains the created node as its one new dependency. Both dependency endpoints exist, neither edge was present in the recovered start graph, and the replay reproduces the live dependency lists exactly.

No new dependency cycle is introduced. The live graph and recovered starting graph each have the same three pre-existing cyclic strongly connected components:

1. `M9-M2-hard-top-product-fibre-mean-obstruction` / `M9-M2-hard-top-product-fibre-transform-self-return`
2. `M9-M1-lower-far-cone-microscopic-cell-reduction` / `M9-M1-lower-post-collar-smoothed-far-alias-reduction`
3. `M9-M1-lower-height-alias-rank-one-product-fibre-obstruction` / `M9-M1-lower-incomplete-fibre-dispersion-obstruction`

Neither the created node nor its owner belongs to a cyclic component, and the set of cycles is unchanged by this patch.

## 5. Owner and exponent quarantine

The owner remains `open` before and after application. Its live delta is limited to the declared dependency, the 23 inconclusive evidence paths, the declared next action, and generated Round 193 metadata. The created result remains the subordinate `proved_internal` candidate lemma and explicitly disclaims completion of the remaining core, owner, parent, endpoint theorem, bridge, target, or exponent.

The protected nodes `GC-partial-one-third`, `GC-external-Li-Yang-theta-star`, `GC-target`, `Conditional-bridge`, `GC-global-M1-alternative-bridge`, `M9-M1`, `M9-M2`, and `M9` are all among the 25 deep-equal no-change objects. Thus no exponent, bridge, theorem, or parent promotion occurred.

## 6. Independent inverse and production replay

The inverse was performed wholly in memory:

1. Remove the one created obligation and 15 introduced rejected-claim records.
2. Remove the declared dependency and evidence additions from the owner.
3. Restore the owner's exact stored `next_action`, `last_updated_round: 192`, and `last_updated_at: 2026-08-30T00:29:16`.
4. Serialize with the repository's canonical graph serializer.

The resulting canonical bytes have SHA-256 `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`, exactly the patch's starting hash. Both the recovered starting graph and live graph pass the repository graph validator, and the patch passes validation against the recovered start.

I then invoked the production `apply_state_patch` logic in memory with round index 193, the recovered judge reference, and the recovered timestamp fixed as the production clock input. Canonical serialization has SHA-256 `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e` and is byte-for-byte equal to the live graph file.

## 7. State-effect recommendation

**Retain the applied Round 193 patch.** The application is exact, evidence-complete, dependency-safe relative to the pre-apply graph, reversible, replayable, and quarantined from exponent or parent promotion. This audit made no shared-state mutation.
