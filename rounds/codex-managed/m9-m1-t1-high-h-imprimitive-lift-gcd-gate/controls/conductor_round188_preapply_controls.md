# Round 188 preapplication artifact and repository hygiene audit

## 1. Result and verdict

**RED.** The frozen preapplication snapshot failed one documentary hygiene
gate: `reports/blind_lift_gcd_rederivation.md` contained two lone carriage
return control bytes, each in place of the `\r` of an intended `\rm` command.
Every mathematical, isolated-application, owner-scope, exponent, diagnostic,
JSON, validation, test, compile, and diff check described below otherwise
passed.

The conductor repaired exactly those two bytes while this audit was in
progress. The repaired report is clean, and an in-memory reverse replay
recovers the historical report hash exactly. That repair necessarily changed
the report hash and therefore made the frozen final attestations stale. This
file records the failed historical snapshot and triggers a new post-repair
provenance and preapplication audit; it does not claim that the repaired
report still contains control bytes.

## 2. Exact audited claim and hypotheses

The audit opened against:

- authoritative graph SHA-256
  `be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`;
- frozen kernel SHA-256
  `0ea2b3c336795fe5290d0eed836f787a2165ed866ab7ffc9baea81ea144b8723`;
- frozen State Patch SHA-256
  `c4ee5bc84fbeb290d998d3e88f5807e31451e5abe51759c77a42c4654f293581`.

The patch proposes exactly `create/update/correct_rejected/reject/no_change =
1/1/0/15/21`. It creates only
`M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction` as
`proved_internal`; it updates only the still-open
`M9-M1-hard-top-high-radical-small-t-residual-estimate`; and it adds fifteen
new calibrated rejected-claim records.

The dry application was performed only in memory, with round index `188` and
judge reference
`rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/reviews/conductor_round188_adjudication.md`.
No authoritative graph write was made. The protected hypothesis is that the
complete high-height relation, complete original `t=1` residual, all
`t>=2`/near-resonant work, hard and smooth M1 parents, GAR, every M2 parent,
endpoint uniformity, M9, both bridges, GC target, and the internal/external
exponent records remain unchanged.

## 3. Comparison and checks

Strict duplicate-rejecting JSON parsing succeeded for the graph,
`state/active_campaign.yml`, `plan.json`, and `state_patch.json`. The active
campaign is deeply equal to `plan.json`'s `campaign` object. Its preapplication
state is `active` with the three task records still `assigned`, and the
official campaign validator accepts it.

The official State Patch dry-run returned `Patch OK`. Production patch logic
applied in memory returned exactly `1/1/0/15/21`; the patched graph validated
with zero issues. The input graph remained byte-identical. Among inherited
obligations, only the declared owner changed, and only its `dependencies`,
`evidence`, `next_action`, `last_updated_round`, and `last_updated_at` changed.
All twenty-one `no_change` obligations were deeply identical before and
after. Across every inherited obligation, `status`, `statement_tex`,
`implies`, `blockers`, and `owner` were identical.

The owner, M9-M1, M9-M2, endpoint uniformity, M9, and GC target remain
`open`; both bridges remain `derived_under_assumptions`;
`GC-partial-one-third` remains `proved_internal`; and the Li--Yang benchmark
remains `proved_external_dependency`. Their theorem/exponent statements are
byte-identical in the in-memory result. The status histogram changes only by
one new `proved_internal` node, from `310` to `311`; all other status counts
are unchanged.

All 18 paths carried by the patch and all 37 distinct repository paths
referenced anywhere in the Round 188 packet plus kernel exist. The finite
Wolfram report and script occur only in `inconclusive` evidence, while the
kernel and campaign explicitly label computation `diagnostic_only` and deny
it theorem status.

After the two-byte repair, the report/candidate/reconciliation/kernel chain
has current hashes:

- blind report: `a524bf81774ac9cdcdd0c423851320da6dc037b8feee5decba541952c996e3b6`;
- formal candidate: `c6f0939ffe5153d38ded0205ec4ee0f211f1de711ea81068194082dd66122f65`;
- reconciliation: `cd29b356a80f14fe35e06f067c13c345e5258a51a4012c48cd3010f319c01997`;
- kernel: `ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a`.

Replacing only the new blind hash by the old hash in the candidate and
reconciliation recovers their frozen hashes `683ad5bd...3808` and
`d67f5a7a...20b8`; replacing only the new blind and candidate hashes in the
kernel recovers `0ea2b3c3...8723`. Likewise, replacing only the new kernel
hash in the adjudication and synthesis recovers their prior hashes. Thus the
observed downstream edits are provenance-only, with no mathematical-content
drift.

## 4. First defect and exact repair

In the historical blind-report bytes, the first defect was the lone `0x0D`
at byte offset `3930` (logical line 102, column 49), in the intended fragment
`\mathfrak f\ {\rm as\ in}`. The second was at byte offset `13214`
(logical line 421, column 23), in `v,t\ {\rm live}`. At each site, replacing
the single `0x0D` byte by the two literal bytes `0x5C 0x72` restores `\rm`.
The repaired file is two bytes longer, has zero control bytes, and reversing
only those two sites yields SHA-256
`a8de6402d8a57d22a773d9b763e195f3e959a1a50cf084bb7ffab7205460231e`
with the original lone-CR offsets exactly.

Three supposedly decisive final attestations are now stale and cannot certify
the repaired current chain:

1. `reviews/final_kernel_candidate_consistency_review.md`, SHA-256
   `054fdb430868c337825529f4e22cfa4b3457a4d1c8fc9c6c5873154ee0a8603f`,
   binds the old blind report, candidate, reconciliation, and kernel;
2. `reviews/final_kernel_power_owner_scope_review.md`, SHA-256
   `3eaaf1327c6f54ffa2a731e3047537961dd4727617cb0d5141be873b19d1df98`,
   binds the old candidate and kernel;
3. `reviews/final_kernel_formalization_provenance_hygiene_review.md`,
   SHA-256
   `1ce46c6a984f6f1678042bc1f180b9a1e5a06e9b46d3e565fb0bbf76e15f53a6`,
   binds the old blind report, candidate, reconciliation, and kernel.

The current adjudication, SHA-256
`aea9de44bb8090200ef473d39d95a93db8096471bb1123c97218162be8e68406`,
binds the repaired kernel but still calls those three stale reviews decisive.
The earlier `controls/preapply_independent_reverse_audit.md`, SHA-256
`3778e9e3f761c70600844d0036ffacb13739971a2c8c7175ce4eceaa33b1c68a`,
also recommends application against the pre-repair provenance and must be
superseded. The original blind seam review is a legitimate historical review
of its named old snapshot; it must not be represented as a current-hash
attestation without an explicit post-repair connector.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Frozen graph and patch hashes | **PASS**: exact `be0eca9c...e5ff` and `c4ee5bc8...3581` |
| Frozen kernel at audit opening | **PASS**: exact `0ea2b3c3...8723` |
| Strict JSON and graph parse | **PASS**: no duplicate keys or parse failure |
| Campaign/plan deep equality and official validation | **PASS** |
| Official State Patch dry-run | **PASS**: `Patch OK` |
| In-memory production application | **PASS**: exact `1/1/0/15/21`, post-graph valid |
| Protected status, theorem, owner, bridge, and exponent scope | **PASS** |
| Diagnostic quarantine | **PASS**: finite artifacts are inconclusive/diagnostic only |
| Referenced paths | **PASS**: 18/18 patch paths and 37/37 packet paths exist |
| Historical UTF-8/control scan | **FAIL**: the two lone CR bytes above |
| Current post-repair UTF-8/control scan | **PASS**: all 27 packet/kernel text artifacts strict UTF-8, zero forbidden controls and zero lone CR |
| TeX/tag hygiene after repair | **PASS**: balanced inline/display delimiters and environments; no duplicate tags; kernel tags `188.K1`--`188.K23` occur exactly once in order |
| Unit tests | **PASS**: 6/6 |
| Compile smoke test | **PASS**: `math_collab` and `tests` |
| `git diff --check` | **PASS**: only line-ending notices |
| Current provenance chain | **FAIL**: three final reviews and the prior preapply recommendation attest the old snapshot |

The repository was already broadly dirty: immediately before this report it
had 15 modified and 718 untracked entries, and the Round 188 packet/kernel
were untracked. Therefore this audit asserts no clean-worktree baseline; it
asserts only that it made no shared proof/state edit and writes solely this
assigned control report.

## 6. Dependencies and exact artifacts

- `protocol.md`: `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`
- `state/proof_obligations.yml`: `be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`
- `state/active_campaign.yml`: `0e9e74a383cd32c327b13263c3e489f4bb1c096a54346c231e9a58f0fc1e7669`
- `plan.json`: `bd5905ccc68e0b13796bd5410d9548e57a123e5619e03ded9ce61ad6ffd08005`
- `state_patch.json`: `c4ee5bc84fbeb290d998d3e88f5807e31451e5abe51759c77a42c4654f293581`
- blind-report repair record:
  `5cf5cfce8dade96422d6f8971fc5a73a90e76c6f1e5e49d0000d7707d96c063e`
- repaired blind report:
  `a524bf81774ac9cdcdd0c423851320da6dc037b8feee5decba541952c996e3b6`
- repaired formal candidate:
  `c6f0939ffe5153d38ded0205ec4ee0f211f1de711ea81068194082dd66122f65`
- repaired reconciliation:
  `cd29b356a80f14fe35e06f067c13c345e5258a51a4012c48cd3010f319c01997`
- repaired durable kernel:
  `ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a`
- current adjudication:
  `aea9de44bb8090200ef473d39d95a93db8096471bb1123c97218162be8e68406`
- current synthesis:
  `014ba753442a53ec72ab92a28df452778ca98cf20ab2f0dd3e3770729b742647`
- bounded diagnostic script/report:
  `7bad1b482654e69325feaf844d359d1643a3245c8e990742ecfc83141e995b99` /
  `4d6173c31bfe63e158f5d07d90488808e65d6b81a58d5e428ed1e01ae69bcb42`

Direct mathematical dependencies remain exactly the accepted Round 187
inverse-residue conductor reduction and `Divisor-bound-elementary`; no
external theorem is introduced by the patch.

## 7. Recommended state effect

**Retain the State Patch unapplied.** Do not reject the mathematical
imprimitive-lift reduction: the failure is documentary and provenance-only.
First add or refresh focused candidate/kernel consistency, power/owner-scope,
and formalization/provenance reviews against the repaired hashes; then update
the adjudication's decisive-review bindings and supersede the old preapply
recommendation with a fresh independent audit. Recheck that the patch remains
byte-identical at `c4ee5bc8...3581`, rerun the official dry-run, campaign
validation, isolated protected-scope replay, hygiene scan, tests, compile, and
diff check. Promotion is justified only if that current-chain replay is
GREEN.
