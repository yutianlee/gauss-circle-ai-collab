# 1. Result and verdict

**Verdict: GREEN. First defect: none.**

The live Round-189 graph is exactly the production result of applying
the frozen State Patch with round index \(189\), timestamp
`2026-08-29T19:34:43`, and the declared adjudication path. The realized
create/update/correct-rejected/reject/no-change counts are exactly

\[
 \boxed{1/1/0/15/22}.
\]

An operation-derived inverse recovers the canonical 2,052,996-byte
starting stream with SHA-256
`338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`.
Production replay from that recovered object reproduces the live object
and all 2,067,773 live bytes exactly, with SHA-256
`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`.

There is no extra mutation. Exactly one proved subordinate obligation is
added, exactly one inherited open owner changes in the five declared
fields, exactly fifteen rejected-overclaim records form a new suffix,
and all twenty-two no-change obligations remain deeply equal. Graph
validation, relation-target checks, cycle comparison, evidence-path
checks, judge injection, inverse recovery, and deterministic replay all
pass.

# 2. Exact audited inputs and realized effect

This verdict is bound to the following exact inputs and production
metadata:

- live `state/proof_obligations.yml`: 2,067,773 bytes, SHA-256
  `15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`;
- Round-189 `state_patch.json`: 17,922 bytes, SHA-256
  `88c3a1d944e618e75b8c0bfecd7bd3e8dcffa5f0fdbb054f319906fc2c68024b`;
- frozen starting graph SHA-256
  `338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`;
- `round_index = 189`;
- actual production timestamp `2026-08-29T19:34:43`; and
- judge reference
  `rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/conductor_round189_adjudication.md`.

The live graph has 391 obligations and 1,644 rejected-claim records,
versus 390 and 1,629 in the recovered start. The sole added obligation is
`M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction`, with
status `proved_internal`. Its direct dependencies are exactly

1. `M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction`;
2. `Divisor-bound-elementary`.

Both dependency nodes already exist in the recovered start and have
status `proved_internal`.

The sole changed inherited obligation is
`M9-M1-hard-top-high-radical-small-t-residual-estimate`. It remains
`open`. Its changed keys are exactly

\[
 \{\texttt{dependencies},\texttt{evidence},\texttt{next\_action},
   \texttt{last\_updated\_round},\texttt{last\_updated\_at}\}.
\]

Its dependency count is \(6\to7\), and its
positive/negative/inconclusive evidence counts are
\(0/0/108\to0/0/126\). Its `status`, `statement_tex`, `implies`,
`blockers`, `owner`, `id`, `type`, `track`, and `title` are unchanged.
At graph top level, only `proof_obligations` and `rejected_claims`
change.

The production result counters are:

| Effect | Exact count |
|---|---:|
| created | 1 |
| updated | 1 |
| corrected_rejected | 0 |
| rejected | 15 |
| no_change | 22 |

The fifteen new rejection records are exactly the patch-order suffix
`Round189-U-over-Y-is-unique-maximal-cutoff` through
`Round189-strict-projective-sector-improves-global-exponent`. Each has
only the production fields `id`, `reason`, `last_updated_at`,
`last_updated_round`, and `evidence`; its metadata is the actual
Round-189 timestamp and round, and its evidence is exactly the singleton
judge-reference list. No obligation is changed to rejected status.

# 3. Derivation and checks

## 3.1 Strict parsing and canonical live bytes

The live graph and patch were decoded as strict UTF-8 and parsed with
`json.loads` using a duplicate-key-rejecting `object_pairs_hook`. Both
parses succeed, all obligation and rejected-claim IDs are unique, and
the patch has exact operation-list sizes \(1,1,0,15,22\). The patch's
`starting_graph_sha256` is the frozen starting hash. Production
`dump_graph` serialization of the parsed live object is byte-for-byte
equal to the raw live file.

The audit used the unchanged production implementation in
`math_collab/proof_obligations.py`: `validate_graph`,
`validate_patch_against_graph`, `apply_state_patch`, and `dump_graph`.
No production mutation rule was reimplemented for replay.

## 3.2 Exact evidence and judge realization

The patch contains 39 create/update evidence occurrences over 21 unique
paths: 21 entries on the created node and 18 additions on the inherited
owner. All 21 unique paths exist as regular files and decode as strict
UTF-8. Every owner evidence addition is novel relative to the recovered
start.

The patch-created node has evidence buckets \(17/0/4\). Production
judge injection adds the adjudication path once to its inconclusive
bucket, so the live buckets are exactly \(17/0/5\), with 22 total
entries. Production also injects the exact singleton judge evidence
into each of the fifteen new rejection records. Thus the applied
operations realize 55 evidence occurrences in all:

\[
 39\text{ patch occurrences}+1\text{ created-node judge injection}
 +15\text{ rejection judge injections}=55.
\]

The created node is deeply equal to the patch create record plus only
`last_updated_round = 189`, `last_updated_at = 2026-08-29T19:34:43`,
and the production judge merge. The rejection suffix is deeply equal to
the exact records generated by the production rejection branch with the
same metadata and judge path.

## 3.3 Relations, protected scope, and validation

Relation inventories are:

| Relation | Recovered start | Live | Delta |
|---|---:|---:|---:|
| dependencies | 1,388 | 1,391 | +3 |
| implies | 326 | 326 | 0 |
| blockers | 70 | 70 | 0 |

The three added dependency edges are exactly the created node's two
direct dependencies and the owner's dependency on the created node.
There is no missing relation target and no duplicate dependency,
implication, or blocker entry.

The dependency strongly connected components of size greater than one
are exactly the same three inherited pairs before and after. The
`implies` and `blockers` graphs remain acyclic. No new cycle is
introduced. Production graph validation returns zero issues for the
recovered start, live graph, and replay, and patch-against-recovered-start
validation returns zero issues.

The inherited status histogram changes only by adding one
`proved_internal` node: that count is \(311\to312\). The counts of
`open`, `derived_under_assumptions`, `proved_external_dependency`,
`proposed`, `diagnostic_only`, and `rejected` obligations are unchanged.
All twenty-two no-change IDs exist in the recovered start and are deeply
unchanged in the live graph. No theorem, bridge, parent, or exponent
node has any field drift.

## 3.4 Operation-derived inverse and actual-time replay

The inverse was derived from the five patch operation lists, the
declared reversibility record, and the actual application metadata:

1. assert that the live created node equals the exact production-created
   record, then remove that node;
2. remove the one exact `dependencies_added` value and all eighteen
   exact `evidence_added` values from the owner;
3. restore the owner's exact prior `next_action`,
   `last_updated_round = 188`, and
   `last_updated_at = 2026-08-29T17:36:08` from the declared
   reversibility record;
4. assert that the final fifteen rejected-claim records equal the exact
   production-generated suffix, then remove that suffix.

The recovered object canonically serializes to 2,052,996 bytes and the
exact frozen starting SHA-256
`338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`.
The reversibility record agrees exactly with all three recovered owner
values.

The production clock alone was then frozen to the actual timestamp and
`apply_state_patch` was invoked on the recovered object with round 189
and the exact judge path. Its `PatchResult` is exactly \(1/1/0/15/22\).
The replayed object equals the live parsed object, and its canonical
2,067,773-byte stream equals the raw live file byte for byte. Its hash is
the exact live hash
`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`.

# 4. First defect or open step

First mechanical defect: **none**. No defect occurs in the input hashes,
strict parsing, canonical bytes, operation counts, actual metadata,
judge injection, evidence files, dependencies, protected fields,
no-change nodes, rejected suffix, graph validation, inverse, or replay.

The first mathematical open step is unchanged by this State Patch:
prove the exact one-outer-real-part fast complement

\[
 j_q(a,v)>
 \min\!\left\{\frac{q-1}{2},
              \left\lfloor\frac{H_Bmq}{Y}\right\rfloor\right\}
\]

through the actual fixed-\(a\), dyadic-\(J\) coefficient-variation bound
at scale \(H_Bm\kappa uJ/q\), or a genuinely joint signed substitute
with the same ledger. The live owner remains open and its Round-189
`next_action` retains that boundary.

# 5. Controls and exact outcomes

| Control | Outcome |
|---|---|
| live graph hash and canonical bytes | PASS: `15c77002...a98568`, 2,067,773 bytes |
| patch hash and strict JSON | PASS: `88c3a1d9...8024b`, 17,922 bytes |
| duplicate-key and duplicate-ID checks | PASS |
| realized production effect | PASS: exact \(1/1/0/15/22\) |
| created-node equality | PASS: patch record plus only exact production metadata and judge merge |
| owner mutation scope | PASS: one open owner, exactly five changed keys |
| no-change obligations | PASS: all 22 deeply unchanged |
| rejected suffix | PASS: exact 15 generated records in patch order |
| evidence paths | PASS: 39 references, 21 unique existing strict-UTF-8 files |
| judge injection | PASS: one created-node merge and 15 singleton rejection references |
| dependencies and relations | PASS: exact \(+3/0/0\), no missing targets or duplicates |
| cycle comparison | PASS: no new cycle |
| protected graph scope | PASS: no status, statement, implication, blocker, owner, theorem, bridge, or exponent drift |
| graph and patch validation | PASS: zero issues |
| operation-derived inverse | PASS: exact 2,052,996-byte starting fingerprint recovered |
| actual-time production replay | PASS: byte-identical live graph and hash |
| authoritative nonmutation by audit | PASS: graph and patch hashes remain frozen |

All machine work was exact parsing, hashing, path checking, object
comparison, production in-memory replay, relation analysis, and
operation-derived inversion. No numerical theorem experiment or
external source was used.

# 6. Dependencies, evidence paths, and hashes

## 6.1 Core audit artifacts

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| live `state/proof_obligations.yml` | `15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568` |
| `state/active_campaign.yml` | `4d8661258570c3152d464f38d76798f1aadd271e9f4e221c80011d3ec60d68f5` |
| Round-189 `state_patch.json` | `88c3a1d944e618e75b8c0bfecd7bd3e8dcffa5f0fdbb054f319906fc2c68024b` |
| `math_collab/proof_obligations.py` | `384070a83b4ce1f56ebdceb0711680a6e889d4d43af3a40a8b6002319114a437` |
| `math_collab/validate_state_patch.py` | `cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8` |
| preapplication independent audit | `0f28599dd992ea46824588b374c2bf12358903175bb039b996ba52a58bb6122e` |

## 6.2 Unique patch evidence paths

All hashes below were recomputed from the current files during this
audit.

| Evidence path | SHA-256 |
|---|---|
| `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md` | `31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58` |
| `candidates/formalized_hard_m1_t1_high_h_dual_frequency_projective_reduction.md` | `123d697198c3c20d710fe5880db75f09423ff457820694dd8671e5b8564e1e28` |
| `reports/dual_height_frequency_signed_attack.md` | `65636c38a3b0c3dbd4a26839dbc89daa88ef78dee5638d02d0de1192b9bdfd38` |
| `reports/height_variation_projective_hostile_audit.md` | `b8ec876aebcc6668646880813bad0abf576063f58e71518d29c8e5778d371608` |
| `reports/blind_dual_frequency_rederivation.md` | `13169505840f9033fb8ddaac6eba62d12988a669127f593a8bc48438543621a3` |
| `reviews/conductor_round189_report_reconciliation.md` | `f7486ccf02a7fb43e1bde82e94e7da410a1d691fc8b629f2b877bc40ca6a902e` |
| `reviews/dual_frequency_normalization_projective_power_seam_review.md` | `5af4ffb3fd3da05287cf217a9ffad412dd888aea716686466bd76fe90c4b8b95` |
| `reviews/literal_variation_centered_kernel_scope_seam_review.md` | `7b9bd94ba4e229d76b1eca96a0e7d25aa98d6e66c4c81e5c40e07d85c8744d3e` |
| `reviews/blind_post_unmask_owner_scope_seam_review.md` | `37cee21325ed7b1e4892aff6e433f642cac9936cf10ce42e25c53496fd712a93` |
| `reviews/blind_post_unmask_quantifier_post_repair_verification.md` | `3594bef3890c41d26eb36bdfcae4b5a8f761a5b203b5289ba2889eae91382dda` |
| `reviews/final_candidate_normalization_post_quantifier_verification.md` | `2b85de501fb60e34eadb212c94843b40e8abcde124ef4fe40aecfecfe9ae25e0` |
| `reviews/final_candidate_literal_formalization_post_quantifier_verification.md` | `c2c7135ad43bc98c8b4b26f98779cd5b3601892cca018d3659a0367efdc997ad` |
| `reviews/final_kernel_candidate_consistency_review.md` | `ef069ca04efa6f0f8913dc75ea6faad6648b891b7d710d61e24565e5a0fcc684` |
| `reviews/final_kernel_power_literal_owner_scope_review.md` | `e19a1a0f3a23e14bfb40636425cbd698a5b5fef2d4707d1b21c08ca19e3d1354` |
| `reviews/final_kernel_formalization_provenance_hygiene_review.md` | `d4e2667a8bf41c35fd6f646338e688d1982afd06809e5d7a67a7bd850baff69e` |
| `reviews/conductor_round189_adjudication.md` | `37f62c5d974aafb240c599cfe8ee1b79370ef05b56f064aa553039b27550c613` |
| `synthesis.md` | `6f66eae59a464e8ebff99222320f21bd9d7b8f57ddaa8d021d04e22aa8506fb1` |
| `controls/conductor_round189_analytic_controls.md` | `2ed8b5a67efb51543239467ec55e285b0f9432b5fc245080b387fec267dd7ffd` |
| `controls/conductor_round189_wolfram_dual_frequency_check.md` | `35bddf8080ceef4acbc6290abe689175f94fc90745a28c707f8147bb5c08adbf` |
| `controls/dual_frequency_projective_check.wls` | `481e7054cce6ad9922f818ff33d11c77265c653608acccbb380a804f34870fff` |
| `controls/conductor_round189_candidate_tex_byte_repair.md` | `ece198a579b537723f07a3c775d6386ec0de88ce39b9f2c091cb8051476d1cba` |

Paths abbreviated within the Round-189 campaign in this table are all
relative to
`rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/`.
The adjudication path is both a patch evidence path and the exact
production judge reference.

# 7. Recommended state effect

Accept the live graph at SHA-256
`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`
as the exact authorized application of Round-189 patch SHA-256
`88c3a1d944e618e75b8c0bfecd7bd3e8dcffa5f0fdbb054f319906fc2c68024b`
to frozen starting graph SHA-256
`338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`.

The accepted scope is only the strict dual-frequency projective
subordinate node, its attachment and evidence on the still-open
small-\(t\) owner, the owner's narrowed `next_action`, fifteen calibrated
overclaim records, and twenty-two no-change decisions. No complete
residual, M1/M2 parent, endpoint-uniformity owner, M9 node, bridge,
theorem, or exponent is promoted. No graph repair is recommended.
