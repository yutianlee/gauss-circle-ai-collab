# Round 181 pre-application independent reverse audit

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Task: `round181_patch_reverse_audit`
- Round: 181
- Role: independent State Patch, graph, evidence, and exact-reversal auditor
- Generated: `2026-08-27T09:06:21.5598901Z`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Exact context files: enumerated in Section 6
- Direct machinery dependencies: `math_collab/proof_obligations.py` and
  `math_collab/validate_state_patch.py`
- Claimant/reviewer/blind status: independent reviewer; not a claimant and
  not blind; no graph, patch, synthesis, candidate, kernel, or shared-state
  edit was made

## 1. Result

**GREEN.** The proposed `state_patch.json` validates against the exact
frozen Round-181 graph, applies cleanly in memory with round index 181, and
has exactly the authorized inventory

\[
 \boxed{3\ \mathrm{create}/4\ \mathrm{update}/0\
 \ \mathrm{correct\text{-}rejected}/13\ \mathrm{reject}/18\
 \ \mathrm{no\text{-}change}}.
\]

The simulated post-patch graph passes the repository validator and reverses
operation by operation, byte for byte, to

`6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`.

All referenced evidence now exists, including the final independent GREEN
kernel review. The repaired candidate and durable kernel are explicitly
signwise, contain the exact all-\(L\) correction, list exact context and
dependencies, and state the connector in two steps. The patch creates only
a subordinate proved reduction, an explicit open residual, and a
mechanism-scoped proved obstruction. It promotes no parent, bridge,
theorem, or exponent.

## 2. Exact audit statement and hypotheses

The audited input is the raw current file
`state/proof_obligations.yml`. Its SHA-256 is exactly the starting hash in
the patch, and loading it with the repository parser and serializing it
with the canonical graph serializer reproduces the original bytes. The
starting graph contains 382 obligations and 1,502 rejected-claim records.

The patch was checked both with the official read-only validator and by an
independent in-memory application using `round_index=181` and
`reviews/conductor_round181_adjudication.md` as the judge reference. The
audit covers operation inventory, ID ownership, evidence paths and
classification, dependency and implication direction, dangling
references, cycle delta, exact mutation scope, exponent quarantine, and an
inverse derived only from the declared patch operations and reversibility
data.

No external theorem, web source, or numerical experiment is used in this
audit. The mathematical classification is checked only against the
complete Round-181 packet and the accepted graph interfaces named in
Section 6.

## 3. Proof and derivation

### 3.1 Inventory, IDs, paths, and classification

The three create IDs are absent from both starting obligation and
rejected-claim namespaces. The four update IDs and all eighteen no-change
IDs exist. All thirteen reject IDs are new overclaim records, not existing
obligations. There is no duplicate inside an operation array and no ID
appears in two operation arrays.

The patch contains 49 evidence-path occurrences representing 12 distinct
files. Every file exists. No within-bucket duplicate occurs, and none of
the 19 values added to inherited evidence was already present in any
evidence bucket of its target. The bucket counts are exact:

- the proved reduction has 12 positive, zero negative, and zero
  inconclusive entries;
- the open small-\(t\) residual has zero positive, zero negative, and
  seven inconclusive entries;
- the proved mechanism obstruction has 11 positive, zero negative, and
  zero inconclusive entries; and
- the four inherited nodes receive respectively 7, 5, 3, and 4 new
  inconclusive entries.

This classification matches the evidence. Exact regrouping, unique
squarefree coordinates, the low-radical sector, the disjoint
high-radical large-multiplier sector, and the all-\(L\) self-return are
proved. The literal small-\(t\) sum remains open. Adversarial
\(t=1\) capacity is used only to delimit coefficient-uniform mechanisms,
not as literal lower mass. The thirteen reject records are precisely the
audited overclaims excluded by that distinction.

### 3.2 Edges, cycles, and mutation scope

The proved reduction has exactly four accepted prerequisites:
`M9-M1-top-endpoint-transform`, `H4-Phi-regularity`,
`M9-M2-dyadic-weight-nondegeneracy`, and
`Divisor-bound-elementary`. The open residual depends on that reduction
and implies `M9-M1-top-endpoint-signed-cone`; the owner receives the
reciprocal dependency. In normalized proof-flow direction both encodings
run from the residual toward the owner. The mechanism obstruction depends
on the reduction and the five named inherited, already-proved M1
capacity/scope obstructions and minimax ledger. It has no implication or
blocker edge. Every post-patch reference resolves.

The dependency graph has three cyclic strongly connected components both
before and after simulation. The implication graph has zero before and
after. The normalized combined dependency/blocker/implication graph has
four before and after. No new cyclic component is introduced.

The simulated graph has 385 obligations and 1,515 rejected claims. Among
the 382 inherited obligations, exactly four objects change:

1. `M9-M1-top-endpoint-signed-cone` changes only `dependencies`,
   `evidence.inconclusive`, `next_action`, and its two update-metadata
   fields;
2. `M9-M1-direct-hard-smooth-separate-one-third-minimax` changes only
   `evidence.inconclusive`, `next_action`, and metadata;
3. `M9-M1-physical-one-count-assembly` changes only those same fields;
   and
4. `M9-M1` changes only those same fields.

No inherited status, statement, title, type, track, owner, implication,
blocker, promotion rule, or promotion reason changes. Every no-change
object is deeply identical before and after simulation. In particular,
`GC-partial-one-third`, `GC-external-Li-Yang-theta-star`, and `GC-target`
are unchanged: the internal exponent remains \(1/3\), the accepted
external benchmark remains
\(0.3144831759740614\ldots\), and the target remains \(1/4\).

### 3.3 Exact inverse

Starting from the simulated post-patch object, I reversed only the
declared operations:

1. removed the three created obligations;
2. removed the one added owner dependency;
3. removed the 7, 5, 3, and 4 added inconclusive evidence values;
4. restored the four exact prior `next_action` strings;
5. restored each updated node to Round 119 at
   `2026-08-22T00:55:39`; and
6. removed the thirteen appended rejected-claim records.

The no-change and assessment arrays write no graph data. Judge-reference
evidence occurs only on newly created or newly rejected objects and is
therefore removed with those objects. The reconstructed graph is deeply
equal to the starting object; canonical serialization is byte-for-byte
equal to the starting file and has the exact frozen SHA-256.

## 4. First doubtful or unproved step

There is no remaining State Patch defect. The first mathematical step not
proved by Round 181 is exactly

\[
 \left|\sum_{\substack{s>L,\ \mu^2(s)=1\\
                        1\le t<\lceil\sqrt L\rceil}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\]

already on \(t=1\). Proving it together with the two paid sectors would
prove only `M9-M1-top-endpoint-signed-cone`; the accepted transform would
then discharge only the hard residual child. The independent smooth M1
parent and all downstream owners remain open.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Frozen hash and canonical bytes | **PASS.** Exact starting hash and byte-stable canonical serialization. |
| Official graph and patch validators | **PASS.** `Graph OK`/`Patch OK`; simulated post-patch graph also validates. |
| Exact operation inventory | **PASS.** \(3/4/0/13/18\), with no duplicate or cross-operation ID. |
| Evidence existence and novelty | **PASS.** 49 occurrences, 12 distinct existing files, no duplicate or pre-existing addition. |
| Mathematical evidence classification | **PASS.** Proved reduction/obstruction and open residual match the final GREEN review. |
| Dependency, implication, and dangling references | **PASS.** All directions are owner-correct and every reference resolves. |
| Cycle delta | **PASS.** Counts remain \(3/0/4\) in the dependency, implication, and normalized combined graphs. |
| Existing-object mutation quarantine | **PASS.** Exactly four permitted updates; no status, statement, bridge, theorem, or exponent mutation. |
| Exact operation-derived inverse | **PASS.** Deep equality, byte equality, and frozen SHA-256 recovered. |
| Artifact hygiene | **PASS.** Patch plus all 12 distinct evidence files are strict UTF-8, LF-terminated, and free of BOM, replacement characters, disallowed C0 bytes, trailing whitespace, unbalanced fences, TeX delimiters, or environments. |
| Numerical/external-source scope | **PASS.** None used. |

## 6. Dependencies and exact artifacts used

This audit used exactly:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `strategy/round181_selection/conductor_round181_selection_decision.md`;
5. `strategy/round181_m1_hard_top_high_squarefree_radical_strategy.md`;
6. `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/plan.json`;
7. the Round-181 `state_patch.json` and `synthesis.md`;
8. all three files under that campaign's `reports/` directory;
9. `candidates/formalized_hard_m1_squarefree_radical_reduction.md`;
10. every Round-181 file under that campaign's `reviews/` directory,
    including `final_kernel_mathematical_scope_review.md` and
    `conductor_round181_adjudication.md`;
11. `proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`;
12. `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/reviews/conductor_round119_capacity_and_labels.md`;
13. `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md`;
14. `math_collab/proof_obligations.py`; and
15. `math_collab/validate_state_patch.py`.

The evidence packet was assessed analytically. In-memory application,
graph traversal, canonical serialization, exact reversal, path checks,
and byte/markup hygiene were used only as mechanical controls.

## 7. Recommended state effect

Approve this exact State Patch for conductor application with
`round_index=181` and the Round-181 conductor adjudication as judge
reference. Apply no additional dependency, implication, blocker, status,
statement, bridge, theorem, or exponent mutation.

After application, preserve the literal small-\(t\) residual as open,
especially its \(t=1\) face. Round 181 is strict subordinate progress,
not a proof of the hard M1 parent or an improvement of the global Gauss
circle exponent.
