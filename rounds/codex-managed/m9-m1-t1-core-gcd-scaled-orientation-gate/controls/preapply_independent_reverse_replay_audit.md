# Round 193 pre-apply independent reverse/replay audit

## 1. Result

**PASS.** The draft State Patch is mechanically valid against the stated current graph, has the required bounded scope, and reverses to byte-equivalent canonical graph JSON in an independent in-memory production-semantics replay. No shared graph or state file was mutated.

- Patch: `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/state_patch.json`
- Patch SHA-256: `dda2bc4af723b3e1d20c850904c6cca64360708927c80f836c0c857d91c4057a`
- Pre-apply graph SHA-256: `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- First defect: **none**

## 2. JSON, schema, IDs, and operation scope

The patch parses as JSON and passes the repository State Patch validator against the current graph. The operation counts are exactly:

| Operation | Count |
|---|---:|
| create | 1 |
| update | 1 |
| correct rejected claim | 0 |
| reject | 15 |
| no change | 25 |

The created ID `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector` is absent pre-apply. The sole updated ID `M9-M1-hard-top-high-radical-small-t-residual-estimate` exists exactly once. All 15 rejection IDs are distinct and absent from the current rejected-claim register. All 25 no-change IDs are distinct and resolve to existing graph objects.

The new node's declared direct dependency `M9-M1-hard-top-t1-rho-large-farey-covector-reduction` exists. The update adds the new node as a dependency of its owner; that dependency is not already stored. A bounded reachability check found no path from the new dependency or new node back to the owner, so these additions introduce no dependency cycle.

## 3. Evidence existence and classification

The patch names 23 unique evidence paths. All 23 exist at audit time. In particular, the formerly pending `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/final_kernel_count_operator_consistency_review.md` is present, so there is no missing-evidence exception to flag.

For the created node, the evidence split is 13 positive, 0 negative, and 10 inconclusive. The durable kernel, terminal candidate/reviews, adjudication, and synthesis are classified as positive. Qualified blind material, superseded/pre-repair checks, and diagnostic computation artifacts remain inconclusive. The owner receives the 23 paths only as inconclusive evidence, correctly preventing a strict-sector result from being treated as proof of the full owner.

## 4. Stored owner state and reversibility metadata

Before application, the owner is `open`, with `last_updated_round: 192` and `last_updated_at: 2026-08-30T00:29:16`. The patch's `restore_next_action`, `restore_last_updated_round`, and `restore_last_updated_at` exactly match the stored pre-apply values. The listed added dependency and evidence paths are not pre-existing owner entries, so inverse removal is unambiguous.

The only intended owner-field changes are dependency addition, inconclusive-evidence addition, replacement of `next_action`, and the production update of round/timestamp metadata. Created and rejected records are wholly removable on inverse. The reversibility record is therefore complete for every mutation made by this patch.

## 5. Protected graph objects and scope quarantine

All 25 declared no-change objects were compared before and after the in-memory apply and remained deeply identical. They cover the accepted Round 187--192 kernels and the protected M9-M1/M9-M2 assemblies and parents, M9, both bridges, endpoint, target, and exponent nodes.

The created result is a subordinate `candidate_lemma` with status `proved_internal` on track `M9_analytic`. Its statement and state effect do not assert completion of the full hard core, its owner, M9-M1, M9, either bridge, the theorem, or any exponent. The owner remains open. No accepted exponent, bridge, or theorem node is changed.

## 6. Independent production apply/inverse/replay

I performed a bounded in-memory replay using the repository's production State Patch semantics with round index 193 and a fixed diagnostic timestamp `2030-01-02T03:04:05`; no graph file was written.

- Canonical pre-apply obligations/rejections: 393 / 1697.
- Simulated post-apply obligations/rejections: 394 / 1712.
- Diagnostic post-apply canonical SHA-256: `931ed6dcc3a666464ed93457c069598c645bd338dfcdc3ae6f98a578e695dbae` (timestamp-dependent).
- After inverse, obligations/rejections: 393 / 1697.
- Reversed canonical SHA-256: `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`.
- Reversed canonical bytes equal the original canonical bytes: **yes**.
- Reapplying from the reversed object reproduced the same fixed-timestamp canonical post-apply bytes: **yes**.

Thus both reverse equivalence and deterministic replay hold under the fixed production inputs.

## 7. State-effect recommendation

**Promote for conductor application.** The patch is schema-valid, evidence-complete, exactly scoped as 1 create / 1 update / 0 correction / 15 reject / 25 no-change, reversible, and quarantined from owner/exponent promotion. This audit made no shared-state mutation.
