# Round 197 final-kernel formalization/provenance/scope review

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Verdict: **REPAIR**
- Durable kernel SHA-256:
  `D3D6AC897E8A193BE83820136EAB28D0B55EAFF030351D060E72B4524D413CC9`
- Final candidate SHA-256:
  `285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0`
- Shared-state mutation: none

## 1. Result

**REPAIR, for durable-artifact provenance packaging only.**  The kernel is
an exact mathematical transplant of the final reviewed candidate: the diff
changes only the title, the artifact-status line, and a terminal blank line.
Its definitions and operators are closed and typed, its four accepted
dependency edges point in the safe direction, its owner and protected scope
are exact, its terminal label is frozen correctly, and its exponent records
remain quarantined.

The kernel nevertheless omits the exact final-candidate path and hash from its
header.  It also retains campaign-relative claimant paths, unnamed diagnostic
controls, two stale references to “this candidate,” and the candidate-stage
heading “Proposed state effect.”  Those are local formalization/provenance
defects in a durable proof artifact.  They must be repaired before the kernel
is cited by a State Patch.  No formula or mathematical claim needs repair.

## 2. Exact statement and hypotheses

The audited kernel proves exactly the final candidate's subordinate result on
the symmetric physical common-cell mask

\[
 P_{\rm cc}
 =P_0\mathbf 1_{\{\mathfrak c_{N,\sigma}(m,g\alpha)
                    =\mathfrak c_{N,\sigma}(\alpha,gm)\}},
\]

and on its exact intersection with the Round-195 open packet.  The common-cell
predicate is evaluated from the two physical lower allocations; it contains
no coefficient value or coefficient-nonvanishing test.  The closed sharp code
uses only the accepted named literal fields, with a distinguished dead code,
and the selector is fixed independently of the allocation.  Thus common-cell
membership is a non-tautological physical/literal mask, not a retrospectively
chosen nonzero-coefficient sector.

The exact Boolean complement remains

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\rm lit}
       \ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}.
\]

The kernel proves no estimate for the last three pieces and no complete
$P_0$, complete $P_2$, full four-corner rectangle, or complete original
$t=1$ result.  The fixed packet, physical $\kappa$ in both charts, projective
band $J$, outer assembly, cap/open split, and the operators
$\mathscr H_{\rm out}$ and $\mathscr S_{\le192,{\rm out}}$ have exactly the
same types as in the final candidate.

## 3. Proof or derivation

### 3.1 Candidate-to-kernel transport

A line diff between

`rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md`

and the durable kernel has only three nonmathematical changes: title,
artifact-status wording, and a final blank line.  Sections 1--7, including all
numbered formulas, dependencies, scope exclusions, graph instructions, and the
terminal label, are otherwise byte-identical.  This proves that no hypothesis,
operator, mask, coefficient factor, or conclusion changed during transport.

### 3.2 Dependency provenance and graph direction

Section 6 names exactly four accepted theorem interfaces and their durable
kernels:

1. Round 184 supplies the selector, literal factor ledger, common-cell
   smooth/BV rules, and named sharp fields.
2. Round 185 supplies the total endpoint, primitive charts, and monotone/low
   height exit.
3. Round 193 supplies the finite-$g$ lemma and transported-mask rule.
4. Round 195 supplies the physical count, deletion-stable masked-operator
   passage, packet estimate, outer ledger, and cap/open split.

These are all older accepted ancestors.  The proposed new Round-197 node
depends on them.  Section 7 expressly leaves those four nodes unchanged and
records the refined remainder only on the new node and the still-open owner's
`next_action`.  There is no edge from Round 195 to Round 197 and therefore no
Round-197/Round-195 cycle.  The dependency direction is suitable for replay.

### 3.3 Owner, terminal label, and quarantine

The only downstream consumer is the open
`M9-M1-hard-top-high-radical-small-t-residual-estimate`, and only as
strict-sector evidence.  The kernel neither closes nor rewrites that owner.
Both M1 parents, GAR, all M2 parents, endpoint uniformity, M9, both bridges,
and the Gauss-circle target are protected explicitly.

The closing label is exactly the frozen label
`p2_four_corner_orbit_boundary_self_return_no_go`.  It does not substitute an
unfrozen common-cell success label.  The internal $1/3$, accepted external
$0.3144831759740614\ldots$, and target $1/4$ records are all stated to be
unchanged.  No estimate is promoted across any of those exponent boundaries.

### 3.4 Durable provenance defect

The kernel header records campaign, round, and starting-graph hash, but not
the exact source candidate or its verified hash.  Consequently a future
reader cannot verify the durable transplant from the kernel alone.  Section 6
also gives the four Round-197 claimant/reconciliation paths only as
`reports/...` and `reviews/...`, “relative to this campaign directory,” and
mentions the finite diagnostic without naming its three files.  That is less
than exact repository-level provenance after the artifact has moved to
`proofs/kernels/`.

The minimal self-contained repair is:

1. add to the header the exact final-candidate path above and SHA-256
   `285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0`;
2. expand the three claimant-report paths and reconciliation path to full
   repository-relative paths under the Round-197 campaign;
3. name the three control files under that campaign's `controls/` directory
   and retain their role as `diagnostic_only`, not theorem evidence;
4. replace “prerequisites of this candidate” and “This candidate proves” by
   “prerequisites of this kernel” and “This kernel proves”; and
5. rename Section 7 to “Dependencies and proof-state boundary,” while leaving
   its numbered conditional state-effect list and frozen terminal label
   unchanged.

No dependency declaration, equation, proof paragraph, scope exclusion, or
State-Patch direction should otherwise change.

## 4. First doubtful or unproved step

The first defect is documentary rather than mathematical: the source identity
needed to authenticate the candidate-to-kernel transplant is absent from the
durable kernel header.  Until the final-candidate path and hash are inserted,
the kernel is not self-contained as a provenance-bearing artifact.

After that repair, the first unproved mathematical region is exactly the
declared complement
$P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}$, including the
sharp-face self-return obstruction.  The kernel correctly makes no estimate
or downstream claim there.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| requested kernel hash | **PASS.** It is exactly `D3D6AC897E8A193BE83820136EAB28D0B55EAFF030351D060E72B4524D413CC9`. |
| candidate-to-kernel mathematical identity | **PASS.** Only title/status/final-newline metadata differ. |
| closed sharp code and selector independence | **PASS.** No coefficient value or nonvanishing predicate enters the code, selector, or common-cell mask. |
| operator typing | **PASS.** Packet variables, both $\kappa$ charts, $J$, $C_0$, outer sums, $\mathscr H_{\rm out}$, and $\mathscr S_{\le192,{\rm out}}$ are defined before use. |
| exact complement | **PASS.** The four masks are disjoint and exhaustive inside $P_2$. |
| accepted dependency paths | **PASS.** All four kernel paths exist and point to accepted ancestors. |
| graph direction and cycle check | **PASS.** Round 197 depends on Round 195; no reverse edge or ancestor rewrite is proposed. |
| owner/protected scope | **PASS.** Only the open hard-small-$t$ owner consumes the strict evidence; parents, bridges, endpoint uniformity, M9, and target stay unchanged. |
| terminal label | **PASS.** The exact frozen label is used. |
| exponent quarantine | **PASS.** $1/3$, $0.3144831759740614\ldots$, and $1/4$ are unchanged. |
| durable source identity | **REPAIR.** Exact final-candidate path and hash are absent from the kernel. |
| repository-level evidence paths | **REPAIR.** Campaign-relative claimant paths and unnamed diagnostic files should be made exact. |
| durable proof-state wording | **REPAIR.** Two “candidate” nouns and the candidate-stage Section 7 heading remain. |

## 6. Dependencies and exact artifacts used

1. `proofs/kernels/m9_m1_hard_top_t1_p2_common_cell_allocation_commutator_sector.md`,
   SHA-256
   `D3D6AC897E8A193BE83820136EAB28D0B55EAFF030351D060E72B4524D413CC9`.
2. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md`,
   SHA-256
   `285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0`.
3. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_report_reconciliation.md`,
   SHA-256
   `DFF0651C22B56BEA4F34D2F65EDACC930265FBC231AFECC60805E49A2DBA3B47`.
4. `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`,
   SHA-256
   `3387615B5522DEEB4C63021FBDF4A665AFA2C405052F2FF0868BED40338E602F`.
5. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`,
   SHA-256
   `4603554DEC10748516C240123F1E847B8F7B3162FA399E94B061C3416FD2A160`.
6. `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`,
   SHA-256
   `470620B5171FD5055991C397B99E8B00C4400CC518E2BF2B9BD92C792CE53B83`.
7. `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`,
   SHA-256
   `4CE74B520C09B12BD1292DC16DBA98E2EC66059619AEB17B068836F0FEBD0009`.
8. `state/proof_obligations.yml`, SHA-256
   `B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`.
9. `state/active_campaign.yml`, SHA-256
   `E7C59EBCCE9FD2FA2F7FB4EA10CA15368937D98D16431B8DEFDC54191A0062FD`.
10. `protocol.md`, SHA-256
    `F26FB038496B5AE171B3352E7D02BA1A4B7DD808EF31BF8620E6D4930CEA9D5A`.

The three Round-197 claimant reports, earlier seam reviews, and diagnostic
controls were used through the final candidate and reconciliation audit trail.
No kernel, candidate, reconciliation, graph, validation matrix, synthesis, or
shared-state file was edited.

## 7. Recommended state effect

**REPAIR before formalization or State Patch.**  Apply only the five local
provenance/wording repairs in Section 3.4, then re-hash and reverify the kernel.
On successful reverification, promote it only as evidence for one subordinate
`proved_internal` common-cell node, attach that node only to the still-open
hard-small-$t$ owner, and preserve the dependency direction
Round 197 $\longrightarrow$ Rounds 184/185/193/195.

Do not modify an accepted ancestor, close the owner, promote any complement,
alter the frozen terminal label, or change a parent, bridge, theorem, or
exponent record.
