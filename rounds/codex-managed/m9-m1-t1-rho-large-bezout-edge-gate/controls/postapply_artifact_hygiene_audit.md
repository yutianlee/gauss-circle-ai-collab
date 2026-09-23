# Round 192 postapplication artifact and evidence hygiene audit

- Campaign: m9-m1-t1-rho-large-bezout-edge-gate
- Round: 192
- Audit role: independent postapplication artifact/evidence hygiene
- Live graph SHA-256:
  7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9
- Frozen State Patch SHA-256:
  fe6718748100c26c1bd56b3c16e02be1827fde513a2a6f133cbbca06c091e9e0
- Durable kernel SHA-256:
  301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325
- Numerical theorem evidence: none

## 1. Result and verdict

**Verdict: PASS.** The live graph contains exactly one created Round-192
Farey-covector node with the frozen patch statement, dependencies, status,
owner, next action, and positive/negative evidence. Every graph evidence
path exists and every current evidence byte stream passes strict UTF-8,
C0/DEL, LF-only, and exactly-one-final-LF checks.

The three finite diagnostic artifacts remain inconclusive only and are not
positive or negative theorem evidence. The patch/adjudication/kernel/
candidate hash chain is current. The updated hard-M1 small-\(t\) owner
remains `open`, contains the new node as a dependency, carries all Round-192
additions as inconclusive evidence, and retains the exact core action. No
repair is required.

## 2. Exact live statement and hypotheses

The created node is

`M9-M1-hard-top-t1-rho-large-farey-covector-reduction`.

Its live fields match the frozen create operation exactly for ID, type,
track, title, `proved_internal` status, statement, owner, next action,
dependencies, implies, blockers, positive evidence, and negative evidence.
It depends only on

- `M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction`; and
- `Divisor-bound-elementary`.

It implies no node and has no blocker. Its statement retains the piecewise
selector

\[
 P_A=0\quad(T=0),
\]

and, only for \(T\geq1\), the simultaneous exact core conditions

\[
 |\rho|\geq(A+1)(T+1),
 \qquad
 |c\beta-d\rho|>T
 \quad((c,d)\in\mathcal F_A).
\tag{192.A1}
\]

It preserves every literal field under one outer real part and leaves the
nonempty-core estimate open.

The updated owner is

`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

Its live status is exactly `open`. Its next action is byte-for-byte equal to
the frozen update: for \(T=0\), attack the entire inherited rho-large
remainder; for \(T\geq1\), attack (192.A1), retaining both orientations,
all literal masks, unequal endpoint number/divisor translations, carries,
square-root phases, affine births/deaths, coprimality flips, cells,
crossings, and zero extensions under one outer real part, while gaining
\(Y/(H_Bm)\) before positive norms. It still says that complete
original-\(t=1\) success leaves every \(t\geq2\) small-\(G\) incidence and
the large-\(G\) near-resonant complement open.

## 3. Evidence, hash-chain, and byte audit

### 3.1 Live evidence classification

The created node has 14 positive entries, no negative entry, and 6
inconclusive entries, representing 19 unique paths. The five frozen
inconclusive paths are all present. The sole additional inconclusive entry
is the conductor adjudication, appended by the official application
`judge_ref` mechanism; that same path was already positive in the frozen
patch. This expected provenance duplication changes no mathematical claim.

All 19 Round-192 paths added to the still-open owner are present in its
inconclusive bucket. None appears in that owner's positive or negative
bucket as a Round-192 addition.

The diagnostic paths

- `controls/farey_covector_finite_diagnostic_report.md`;
- `controls/farey_covector_finite_diagnostic.wls`; and
- `controls/farey_covector_finite_diagnostic_output.txt`

occur only in the created node's inconclusive bucket. The synthesis and
adjudication also label finite computation diagnostic only. Diagnostic
quarantine therefore passes.

### 3.2 Exact evidence hashes and hygiene

Every row below exists and passes strict UTF-8 decoding without BOM, has no
disallowed C0/DEL byte, uses LF rather than CRLF, and ends in exactly one LF.

| SHA-256 | Live evidence path |
|---|---|
| `301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325` | `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md` |
| `9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5` | `candidates/formalized_hard_m1_t1_rho_large_farey_covector_reduction.md` |
| `c853502a8ae8721b17c3c862a4d9b8865a80e7b2697e15950cd748b05227e2a8` | `reports/farey_covector_sparse_sector_attack.md` |
| `9051b23d31cea5eff00a1aece7ef66f26d007c1c750d5ada2e2641808f771008` | `reports/central_core_phase_hostile_audit.md` |
| `186081c5acb3896598b36f9edc18e683df1b5f5162261a46dfb4da6ffc00a461` | `reports/blind_unimodular_covector_rederivation.md` |
| `b9f67f2645f11166d6f856f9936bbb375939bf8bb8899d91374c90a7a58b7d01` | `reviews/conductor_round192_report_reconciliation.md` |
| `428f35a30ca5277297f921edae7ca4bd7d6f0a8069504e36e393d482d1c42794` | `reviews/blind_post_unmask_farey_covector_verification.md` |
| `3b61fa78517748d1c8da2625c12f667934260aa819150d293b8262f63ad2e752` | `reviews/blind_post_unmask_farey_covector_postrepair_verification.md` |
| `8090cc7205ad3f5417c428354106216072171e2e2706e30a830ccdc6b40983d0` | `reviews/canonical_covector_divisor_power_seam_review.md` |
| `58513c536b712170afc3def8c1e2da7bdf8541205807daa38cff18b895e8e6ea` | `reviews/literal_phase_carry_core_owner_scope_seam_review.md` |
| `f2caf365553ea3c2245f19842118d13892047415df22399694293fe1155bdac1` | `reviews/final_kernel_candidate_power_consistency_review.md` |
| `3089849e8a4e37bca1c82b63c36c838e0ddb9343524c74a9c208c84c0451878e` | `reviews/final_kernel_candidate_power_postrepair_verification.md` |
| `a16dc5e673a9ec3023dec4b87791bf46d0f3044ddc96bcf2132e1c3c7cd40316` | `reviews/final_kernel_literal_owner_scope_review.md` |
| `ea24e607ee3dc97e2cc3ebd92222aa00187ee3a7326c08bd28c5be67584dce58` | `reviews/final_kernel_formalization_provenance_hygiene_review.md` |
| `4cd035ab0373ab437e5609fd967a93b800f4e27e76109fbedd65b23b9d6271d2` | `reviews/conductor_round192_adjudication.md` |
| `069e65120b789c81abfd1412a3f119211a538cecb59df90d274807da01f67fdd` | `synthesis.md` |
| `1cb1d9f6dde261209528b5b78dc5e38104518d3b941e028b595270ea51906e8b` | `controls/farey_covector_finite_diagnostic_report.md` |
| `f7b48f27f9998f0b20c473bf822d3dad1fc4bc9d7de40bc0e2d67cf4c5506148` | `controls/farey_covector_finite_diagnostic.wls` |
| `c13edaef6d30d0d82eb2dc78ab579995f91a65654f25c240b97c03d861edbb08` | `controls/farey_covector_finite_diagnostic_output.txt` |

Campaign-relative prefixes were suppressed in the table only for
readability; each live graph path is canonical, relative, and present.

### 3.3 Patch, adjudication, and kernel chain

The frozen patch remains at
`fe6718748100c26c1bd56b3c16e02be1827fde513a2a6f133cbbca06c091e9e0`.
The live created statement and all frozen create fields replay exactly from
that patch, apart from the expected application metadata and adjudication
`judge_ref` evidence described above.

The adjudication remains at
`4cd035ab0373ab437e5609fd967a93b800f4e27e76109fbedd65b23b9d6271d2`
and names kernel hash `301e51dc...c38325`. The synthesis has hash
`069e6512...f67fdd` and names the same kernel. The kernel names locked
candidate hash `9562954b...996cd5`. The adjudication's three final review
hashes also match their live files:

- candidate/power postrepair: `3089849e...51878e`;
- literal/core/owner: `a16dc5e6...40316`; and
- formalization/provenance/hygiene: `ea24e607...dce58`.

The chain is internally consistent.

## 4. First doubtful or unproved step

No postapplication artifact or evidence defect was found. The first
unproved mathematical step remains the exact nonempty-core estimate

\[
 \Re\mathscr R_{\rm core,Y,Q}^{\sigma}
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\tag{192.A2}
\]

or its sufficient fixed-packet strengthening

\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\tag{192.A3}
\]

The live owner assigns exactly this core work and does not treat it as
proved.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| live graph hash | PASS: exact assigned SHA-256 before and after all read-only checks. |
| official graph validation | PASS: `python -m math_collab.validate_state_patch` returned `Graph OK` with exit code 0. |
| created node replay | PASS: frozen statement and all non-application fields match exactly. |
| created-node evidence paths | PASS: 20 bucket entries, 19 unique paths, zero missing paths. |
| evidence hashes | PASS: all 19 unique live hashes are recorded in Section 3.2. |
| strict evidence byte hygiene | PASS: all 19 are UTF-8 without BOM, C0/DEL-clean, LF-only, and have exactly one terminal LF. |
| diagnostic quarantine | PASS: all three finite artifacts are inconclusive only and explicitly non-theorem evidence. |
| judge provenance | PASS: the sole extra inconclusive path is the official adjudication `judge_ref`. |
| patch/adjudication/kernel/candidate chain | PASS: every live hash and embedded reference agrees. |
| owner status | PASS: remains `open`; the patch did not promote it. |
| owner evidence | PASS: all 19 Round-192 additions are inconclusive and none was added as positive or negative. |
| owner next action | PASS: byte-exact frozen core action, including \(T=0\), \(T\geq1\), literal fields, missing gain, and downstream quarantine. |
| exponent quarantine | PASS: no parent, bridge, theorem, internal, external, or target exponent was changed. |

## 6. Dependencies and exact artifacts used

The audit used the live graph, frozen patch, official validator, and the 19
unique evidence paths and hashes listed in Section 3.2. Principal chain
artifacts were:

1. state/proof_obligations.yml — SHA-256
   7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9.
2. rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/state_patch.json
   — SHA-256
   fe6718748100c26c1bd56b3c16e02be1827fde513a2a6f133cbbca06c091e9e0.
3. proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md
   — SHA-256
   301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325.
4. rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/conductor_round192_adjudication.md
   — SHA-256
   4cd035ab0373ab437e5609fd967a93b800f4e27e76109fbedd65b23b9d6271d2.
5. rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/synthesis.md
   — SHA-256
   069e65120b789c81abfd1412a3f119211a538cecb59df90d274807da01f67fdd.
6. math_collab/validate_state_patch.py — SHA-256
   cfa914c54bfa172cc94354dc7e904e866d4e69c96cd8be7bfbf68b5a295080e8.

No sibling postapplication audit, proof draft, validation matrix, external
source, or numerical result beyond byte-level quarantine was read or used.

## 7. Recommended state effect

**No change.** Retain the live graph and all campaign artifacts exactly as
applied. Keep the created node subordinate and proved-internal, keep the
hard-M1 small-\(t\) owner open on the exact core action, and keep diagnostic
and exponent quarantine unchanged.

Postwrite hygiene: PASS for strict UTF-8/C0/DEL/LF/terminal-newline, TeX,
trailing-whitespace, conflict-marker, and path-scoped diff checks. No graph,
patch, campaign artifact, or lifecycle file was edited.
