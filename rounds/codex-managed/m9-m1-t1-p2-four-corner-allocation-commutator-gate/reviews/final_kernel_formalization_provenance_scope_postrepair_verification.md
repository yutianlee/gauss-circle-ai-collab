# Round 197 final-kernel formalization/provenance/scope post-repair verification

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Verdict: **GREEN**
- Repaired durable kernel SHA-256:
  `6CAF8DC3A027A4548C7059546F117868B45CE51C23F05A5148B78AA995415467`
- Final candidate SHA-256:
  `285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0`
- Shared-state mutation: none

## 1. Result

**GREEN.**  The repaired durable kernel implements exactly the five local
provenance and wording corrections required by
`final_kernel_formalization_provenance_scope_review.md`.  Its mathematical
body remains the reviewed final candidate without alteration.  Source
identity, dependency paths, diagnostic role, durable-kernel wording, and the
proof-state boundary are now self-contained and replayable.

The accepted dependency direction, still-open owner, protected parents and
bridges, frozen terminal label, and exponent quarantine all remain unchanged.
No further formalization or provenance repair is required before a mechanically
valid State Patch.

## 2. Exact statement and hypotheses

The kernel still proves only the symmetric physical common-cell sector
$P_{\rm cc}$ and its exact intersection with the Round-195 open packets.  The
closed sharp code and selector remain independent of coefficient values and
coefficient nonvanishing.  The exact disjoint complement inside $P_2$ remains

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\rm lit}
       \ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}.
\]

The fixed packet, physical $\kappa$ in both charts, projective band $J$, outer
assembly, cap/open split, and the operators $\mathscr H_{\rm out}$ and
$\mathscr S_{\le192,{\rm out}}$ retain their final-candidate definitions and
types.  No complement, complete $P_0$, complete $P_2$, full rectangle, or
complete original-$t=1$ estimate has been added.

## 3. Proof or derivation

The repaired kernel has the requested SHA-256.  Its diff against the final
candidate contains only the durable-artifact changes already authorized:

1. the proof-kernel title and durable status line;
2. the exact final-candidate repository path and verified SHA-256 in the
   header;
3. “this kernel” in the two durable-scope sentences;
4. full repository-relative paths for the three claimant reports, the
   reconciliation, and all three diagnostic controls, together with the
   explicit `diagnostic_only` classification; and
5. the Section 7 heading “Dependencies and proof-state boundary.”

All cited paths exist.  The candidate file still hashes to
`285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0`,
and the starting graph still hashes to
`B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`.
No numbered formula, proof paragraph, dependency interface, scope exclusion,
state-effect item, or terminal label changed.

The graph direction remains new Round 197 node $\longrightarrow$ accepted
Rounds 184, 185, 193, and 195.  The Round-195 node is explicitly left
unchanged, so no reverse edge or Round-197/Round-195 cycle is introduced.
Only the open
`M9-M1-hard-top-high-radical-small-t-residual-estimate` may consume the new
strict-sector evidence.

## 4. First doubtful or unproved step

No post-repair formalization or provenance defect remains.  The first unproved
mathematical region is still the declared physical complement
$P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}$, including the
sharp-face self-return obstruction.  This is the intended open boundary, not a
kernel defect, and the kernel makes no estimate there.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| repaired kernel hash | **PASS.** Exact requested SHA-256 verified. |
| final-candidate source identity | **PASS.** Exact path and matching hash are in the header. |
| mathematical-body preservation | **PASS.** No formula, hypothesis, operator, or conclusion changed. |
| claimant/reconciliation paths | **PASS.** All four are full repository-relative paths and exist. |
| diagnostic provenance | **PASS.** Script, output, and report are named and explicitly `diagnostic_only`. |
| durable wording | **PASS.** Both stale “candidate” nouns are now “kernel.” |
| proof-state heading | **PASS.** Section 7 is the durable dependency/proof-state boundary. |
| dependency direction and cycle | **PASS.** Only older accepted ancestors are prerequisites; no reverse edge is proposed. |
| owner and protected scope | **PASS.** The hard-small-$t$ owner remains open; parents, endpoint uniformity, M9, bridges, and target remain unchanged. |
| frozen terminal label | **PASS.** `p2_four_corner_orbit_boundary_self_return_no_go` is unchanged. |
| exponent quarantine | **PASS.** $1/3$, $0.3144831759740614\ldots$, and $1/4$ remain unchanged. |

## 6. Dependencies and exact artifacts used

1. `proofs/kernels/m9_m1_hard_top_t1_p2_common_cell_allocation_commutator_sector.md`,
   SHA-256
   `6CAF8DC3A027A4548C7059546F117868B45CE51C23F05A5148B78AA995415467`.
2. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md`,
   SHA-256
   `285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0`.
3. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/final_kernel_formalization_provenance_scope_review.md`.
4. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_report_reconciliation.md`.
5. `state/proof_obligations.yml`, SHA-256
   `B9B95784B097B3E30BED95F418AE14E57BF5F03A4A52975BEEEFA8DB85B7F8AE`.
6. `protocol.md`.

The four accepted prerequisite kernels and every Round-197 evidence/control
path named by the repaired kernel were checked for existence.  No kernel,
candidate, reconciliation, graph, validation matrix, synthesis, or shared-state
file was edited.

## 7. Recommended state effect

**GREEN for formalization, provenance, dependency direction, and scope.**  The
repaired kernel may support a State Patch creating exactly one subordinate
`proved_internal` common-cell node and attaching it only as strict-sector
evidence to the still-open hard-small-$t$ owner.

Leave Rounds 184/185/193/195 unchanged, do not promote the complement or close
the owner, retain the frozen terminal label
`p2_four_corner_orbit_boundary_self_return_no_go`, and leave every parent,
bridge, theorem, and exponent record unchanged.
