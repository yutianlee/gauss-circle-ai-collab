# Round 190 independent pre-application reverse and scope audit

**Audit date:** 2026-08-29 (Asia/Shanghai)  
**Verdict:** **GREEN**  
**Patch SHA-256:** `b19a92efe86341400e0d6c75868f2e652164d0a34682b9bae93cf00066c948b9`

## 1. Result

**Independent pre-application replay lemma.**  The proposed Round-190
State Patch has exact effect

\[
 \boxed{0/1/0/23/27}
\]

in the order
`create/update/correct_rejected/reject/no_change`.  Its declared starting
graph hash equals the current authoritative graph hash:

`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`.

An independent implementation, which did not import or call the repository
State Patch validator, replayed the patch in memory with round index 190
and the standard synthesis judge reference.  It found exactly these
semantic mutations:

1. ten new, unique **inconclusive** evidence paths on
   `M9-M1-hard-top-high-radical-small-t-residual-estimate`;
2. a replacement of that same open node's `next_action`;
3. that node's `last_updated_round` and `last_updated_at` metadata;
4. twenty-three new rejected-claim records; and
5. no mutation for the twenty-seven `no_change` entries.

The replay changed no obligation status, statement, dependency,
implication, blocker, source dependency, or exponent field.  Applying the
embedded reversibility data, removing exactly the introduced evidence and
rejected records, recovered both semantic equality and byte equality with
the canonical starting graph.  The reversed SHA-256 is again
`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`.

The patch was **not applied**, and no shared state was edited.

## 2. Exact statement and hypotheses

The audit reads the patch according to the repository mutation semantics,
but implements those semantics independently:

- `create` appends obligations: there are none;
- `update` mutates an existing obligation, append-uniquely merging an
  `evidence_added` bucket: there is exactly one;
- `correct_rejected` mutates an existing rejected record: there are none;
- a `reject` ID matching no obligation creates a rejected-claim record:
  all twenty-three IDs are new and have this effect;
- `no_change` records a decision in the application result but makes no
  graph mutation: all twenty-seven IDs exist;
- round index 190 overwrites the updated node's round metadata and is
  attached to each new rejected record;
- the standard judge reference
  `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/synthesis.md`
  is already one of the ten `evidence_added.inconclusive` paths, so
  append-unique merging adds no eleventh node-evidence value.

The only updated obligation is currently `open`.  Its pre-patch metadata
and `next_action` agree exactly with the patch's embedded restore values:

| Field | Starting value / check |
|---|---|
| `id` | `M9-M1-hard-top-high-radical-small-t-residual-estimate` |
| `status` | `open` |
| `last_updated_round` | `189` |
| `last_updated_at` | `2026-08-29T19:34:43` |
| restored `next_action` | byte-for-byte equal to the current node value |
| restored metadata | byte-for-byte equal to the current node values |
| pre-existing inconclusive evidence | 126 entries |
| proposed evidence already present | none |

The new `next_action` is strategy-only: it restates the accepted strict
Rounds 187--189 sectors, freezes the still-open fast complement and signed
height-jump objective, requires recovery of (Y/(H_Bm)) before positive
norms, and explicitly leaves original (t\ge2) and large-(G)
near-resonant incidences open.  It changes neither the node statement nor
its implication to `M9-M1-top-endpoint-signed-cone`.

## 3. Proof or derivation

### 3.1 Full-graph and operation census

The authoritative file was parsed in full as JSON-compatible YAML.  It
contains 391 obligations and 1,644 pre-patch rejected claims.  Obligation
IDs and rejected-claim IDs are each unique.  Every existing dependency,
implication, and blocker reference resolves to an obligation ID.

The patch has the following static census:

| Operation | Count | ID validity | Scope consequence |
|---|---:|---|---|
| `create` | 0 | vacuous | no node creation |
| `update` | 1 | unique, existing | one open node; only inconclusive evidence, next action, and metadata |
| `correct_rejected` | 0 | vacuous | no old rejected record is altered |
| `reject` | 23 | unique; absent from both obligations and old rejected claims | append new rejected-claim records; no obligation is set to `rejected` |
| `no_change` | 27 | unique, existing | application makes no graph mutation |

There are no ID collisions within an operation or across the five
operation lists.  Every rejected and no-change reason is a nonempty
string.  The twenty-seven no-change nodes have the exact starting-status
census: 15 `open`, 9 `proved_internal`, 2
`derived_under_assumptions`, and 1 `proved_external_dependency`.

### 3.2 Evidence-path audit

All ten proposed evidence paths exist as regular files, are unique, and
are absent from the node's starting inconclusive bucket:

| Evidence path | SHA-256 |
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

Every displayed path is relative to
`rounds/codex-managed/full-proof-round187-189-strategy-literature-review/`.

### 3.3 Rejected-reason audit

All twenty-three records reject overclaims rather than accepted
obligations.  Each ID is new, its reason matches the adjudicated scope,
and none can change a proof status:

| New rejected-claim ID | Reason-scope check |
|---|---|
| `Round190-report-agreement-proves-fast-complement` | report agreement is not analytic cancellation |
| `Round190-positive-variation-is-signed-coboundary` | positive separate variation is not the joint signed seam |
| `Round190-joint-jump-packet-proves-orientation-pairing` | no orientation involution is proved |
| `Round190-joint-jump-packet-proves-projective-difference` | height difference is not a neighboring-slope identity |
| `Round190-Abel-identity-proves-fast-cancellation` | algebraic Abel relocation is not cancellation |
| `Round190-pointwise-bound-proves-signed-jump-seam` | pointwise control retains the (Y/(H_Bm)) deficit |
| `Round190-height-masks-are-invariant` | literal masks and birth/death fields may jump |
| `Round190-centered-kernel-has-uniform-polylog-prefixes` | the odd-prime linear-prefix control falsifies this |
| `Round190-positive-transforms-gain-fast-deficit` | positive transforms return capacity without prior signed cancellation |
| `Round190-fixed-power-deficit-is-epsilon-absorbable` | a fixed positive power is not a logarithmic loss |
| `Round190-positive-capacity-is-literal-lower-mass` | positive capacity is an upper ledger, not literal lower mass |
| `Round190-fast-complement-closes-complete-small-t-owner` | (t\ge2) and near-resonant leaves remain |
| `Round190-fast-complement-closes-hard-M1-or-M9-M1` | the remaining owner and smooth M1 remain |
| `Round190-fast-complement-closes-M9-or-quarter-target` | M2, endpoint, assembly, and bridges remain |
| `Round190-GAR-and-direct-M1-may-be-spliced` | the routes are a logical OR, not a splice |
| `Round190-GAR-bypasses-M9-M2` | the GAR route still requires all M9-M2 |
| `Round190-K17a-or-K26-is-complete-hard-TOP` | both are subordinate residual attacks |
| `Round190-critical-BAL-alone-closes-BAL` | remaining-label/exact-square BAL is independent |
| `Round190-Shen-imports-to-fast-complement` | source coefficient/modulus/norm architecture fails |
| `Round190-MRS-imports-to-fast-complement` | the complete prime-power Kloosterman-product object differs |
| `Round190-source-audit-is-universal-literature-nonexistence` | no-import is dated and corpus-scoped |
| `Round190-strategy-review-improves-global-exponent` | no analytic theorem or exponent is proved |
| `Round190-in-round-pivot-is-authorized` | the next frozen seam must first close or be diagnosed |

### 3.4 Independent replay, scope diff, and reversal

The replay used an audit-only timestamp.  Since the application timestamp
is intentionally nondeterministic, only the field's scope matters; its
starting value is restored exactly.  The replay increased rejected claims
from 1,644 to 1,667, left the obligation count at 391, and changed only the
four target-node keys `evidence`, `next_action`, `last_updated_round`, and
`last_updated_at`.  The evidence delta was exactly ten.

Across all 391 obligations, snapshots of `status`, `statement_tex`,
`dependencies`, `implies`, `blockers`, `source_card`, `exponent`, and
`certified_exponent` were identical before and after replay.  Top-level
keys and the complete ordered obligation-ID list were also identical.

Reversal then:

1. removed the ten patch-listed inconclusive evidence paths;
2. restored the selected node's `next_action` from
   `reversibility.restore_next_action`;
3. restored its round and time metadata from
   `reversibility.restore_metadata`; and
4. removed the twenty-three patch-listed rejected-claim IDs.

The result was equal as a parsed graph, equal as canonical serialized
bytes, and equal to the starting file bytes.  The starting file itself is
already the canonical serializer output, so “byte-equivalent semantic
graph content” is literal here, not merely equality after key sorting.

## 4. First doubtful or unproved step

The first remaining step is operational: the conductor has not yet
applied the patch.  To preserve the exact replayed scope, application must
use `--round-index 190` and either omit `--judge-ref` or use the already
listed synthesis path.  The standard safe application is:

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/full-proof-round187-189-strategy-literature-review/state_patch.json --apply --round-index 190 --judge-ref rounds/codex-managed/full-proof-round187-189-strategy-literature-review/synthesis.md
```

An unlisted alternative `--judge-ref` would append an eleventh
inconclusive evidence value not named by the embedded reversal rule.  That
would be an application-scope change and would require a new reverse audit.
This is not a defect for the standard command above because `synthesis.md`
is already in `evidence_added` and append-unique merging is idempotent.

Mathematically, the first doubtful step remains the unproved joint signed
height-jump estimate; the patch correctly records it only in `next_action`
and inconclusive evidence.  Nothing in the patch certifies that estimate.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Starting graph SHA-256 | **PASS:** exact declared/current match at `15c770...a98568` |
| Full graph parse | **PASS:** 391 obligations, 1,644 rejected claims |
| Exact effect census | **PASS:** `0/1/0/23/27` |
| Unique IDs | **PASS:** graph IDs, existing rejected IDs, each operation list, and cross-operation IDs are collision-free |
| Update target | **PASS:** exactly one existing open obligation |
| Update field whitelist | **PASS:** patch keys are only `id`, `evidence_added`, `next_action`, `last_updated_round`; application adds only time metadata |
| Evidence existence/uniqueness | **PASS:** ten regular files, ten unique paths, none pre-existing on the node |
| Reject semantics | **PASS:** all 23 IDs are new claims, not obligations; all reasons are nonempty and scope-correct |
| No-change semantics | **PASS:** all 27 IDs exist; no graph mutation; status census retained |
| Protected-field diff | **PASS:** no status, statement, dependency, implication, blocker, source-card, or exponent change |
| Owner/parent/bridge scope | **PASS:** only the small-(t) owner's next action changes; all parents, endpoints, bridges, and target nodes are untouched |
| Exponent quarantine | **PASS:** internal (1/3), external Li--Yang benchmark, and target (1/4) nodes are no-change |
| Independent replay | **PASS:** only expected target keys and 23 appended rejected records changed |
| Embedded reverse | **PASS:** parsed semantic equality, canonical byte equality, and starting-file byte equality |
| Reverse hash | **PASS:** `15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568` |
| Shared-state mutation | **PASS:** no patch application and no shared-state edit performed |

## 6. Dependencies, exact artifacts, commands, and results

Artifacts read in full:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `reviews/conductor_round190_adjudication.md`;
- `controls/conductor_round190_launch_validation.md`;
- `controls/conductor_round190_controls.md`;
- `synthesis.md`;
- `state_patch.json`;
- `math_collab/proof_obligations.py` and
  `math_collab/validate_state_patch.py` for the documented mutation
  semantics only.

The decisive hash command and result were:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath state/proof_obligations.yml
```

```text
15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568
```

The independent audit was run as an in-memory standard-library script,
without importing `math_collab`:

```powershell
@'
import copy, hashlib, json, pathlib
gp=pathlib.Path('state/proof_obligations.yml')
pp=pathlib.Path('rounds/codex-managed/full-proof-round187-189-strategy-literature-review/state_patch.json')
raw=gp.read_bytes(); before=json.loads(raw.decode('utf-8'))
patch=json.loads(pp.read_text(encoding='utf-8')); ops=patch['proof_obligations']
after=copy.deepcopy(before); by={x['id']:x for x in after['proof_obligations']}
stamp='AUDIT-REPLAY-TIMESTAMP'; judge_ref='rounds/codex-managed/full-proof-round187-189-strategy-literature-review/synthesis.md'
for upd in ops['update']:
    node=by[upd['id']]; inc=node.setdefault('evidence',{}).setdefault('inconclusive',[])
    for value in upd['evidence_added']['inconclusive']:
        if value not in inc: inc.append(value)
    if judge_ref not in inc: inc.append(judge_ref)
    node['next_action']=upd['next_action']; node['last_updated_round']=190; node['last_updated_at']=stamp
for item in ops['reject']:
    after['rejected_claims'].append({'id':item['id'],'reason':item['reason'],'last_updated_at':stamp,'last_updated_round':190,'evidence':[judge_ref]})
target=ops['update'][0]['id']; rev=copy.deepcopy(after)
rnode=next(x for x in rev['proof_obligations'] if x['id']==target)
added=set(ops['update'][0]['evidence_added']['inconclusive'])
rnode['evidence']['inconclusive']=[x for x in rnode['evidence']['inconclusive'] if x not in added]
rnode['next_action']=patch['reversibility']['restore_next_action'][target]
for key,value in patch['reversibility']['restore_metadata'][target].items(): rnode[key]=value
new_ids={x['id'] for x in ops['reject']}
rev['rejected_claims']=[x for x in rev['rejected_claims'] if x['id'] not in new_ids]
canon=lambda x:(json.dumps(x,indent=2,ensure_ascii=True)+'\n').encode('utf-8')
print('counts',*[len(ops[k]) for k in ('create','update','correct_rejected','reject','no_change')])
print('reverse_semantic_equal',rev==before)
print('reverse_to_start_file_byte_equal',canon(rev)==raw)
print('reverse_sha256',hashlib.sha256(canon(rev)).hexdigest())
'@ | python -
```

Its terminal summary was:

```text
counts 0 1 0 23 27
reverse_semantic_equal True
reverse_to_start_file_byte_equal True
reverse_sha256 15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568
```

A separate protected-field diff produced:

```text
obligation_count_before_after 391 391
rejected_count_before_after 1644 1667
protected_fields_equal True
changed_obligation_ids ['M9-M1-hard-top-high-radical-small-t-residual-estimate']
changed_target_keys ['evidence', 'last_updated_at', 'last_updated_round', 'next_action']
inconclusive_delta 10
rejected_appended_ids_exact True
after_unique_obligation_ids True
after_unique_rejected_ids True
after_all_dep_refs_exist True
```

## 7. Recommended state effect

**Recommendation: GREEN for application with the exact standard command
in section 4.**

The patch is strategy-only and reversibility-complete under that command.
It may be applied after this audit without changing any analytic theorem,
status, statement, dependency, implication, blocker, source dependency,
parent, endpoint, bridge, or certified exponent.  After application, the
conductor should independently re-hash and reverse/replay the written graph
once more, because this report is deliberately pre-application and does
not certify filesystem state that has not yet been created.
