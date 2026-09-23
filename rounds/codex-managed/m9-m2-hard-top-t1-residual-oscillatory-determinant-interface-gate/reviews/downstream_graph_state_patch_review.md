# Round 167 downstream graph and State Patch review

## 1. Result

**Verdict: PASS BEFORE APPLY.**

The mathematical graph placement is correctly scoped.  The proposed patch
creates one homogeneous `proved_internal` reduction, adds it only as an
inconclusive prerequisite of the two open hard-TOP parents, records eighteen
fresh rejected claims, and changes no existing status or exponent.  The
official patch validator returns `Patch OK`, and an in-memory dry application
leaves the structural graph validator green.

The two earlier pre-application defects are repaired.  The Round-167
`synthesis.md` now exists, so all thirteen unique evidence paths resolve.
The active campaign and plan snapshot are complete, the round ledger is
closed, every Round-167 validation gate is green with an existing artifact,
and the generated current-round file records `complete`.  The validation
matrix now has the consistent top-level status
`round_167_closed_internal_determinant_endpoint_polylog_reduction_validated_pending_state_patch_application_no_parent_or_exponent_change`.
No further repair is required before State Patch application.

## 2. Exact statement and hypotheses

The authoritative graph hash is

`9d93f058c3623b7b278aa1ccba99adcf264c2e1d45af95ffbf993a123cfa1f76`,

which exactly matches the Round-167 starting hash.  The patch has:

- one create;
- three updates;
- zero corrected rejected claims;
- eighteen rejects; and
- seventeen no-change records.

The created node is
`M9-M2-hard-top-t1-residual-determinant-endpoint-polylog-shift-reduction`,
of type `reduction`, track `M9_analytic`, and status `proved_internal`.  Its
statement contains only:

1. the multiplicity-one ordered determinant dictionary;
2. the free left-orbit opening;
3. the exact endpoint quadratic-form identity with the target real part
   outside the full shift aggregate;
4. the Schur upper capacity \(L^3X^\varepsilon\); and
5. the complete fixed-\(B\) polylogarithmic-shift estimate
   \(O_{\varepsilon,B}(L^2X^\varepsilon)\).

It explicitly leaves the non-polylogarithmic K17a range, the complete
residual scalar, every parent and bridge, and every exponent conclusion
open.  Its sole dependency is
`M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`; that accepted
Round-165 node already depends on the Round-164 residual transport node.
Thus the shorter dependency list is transitively complete.

The three updates add evidence and a next action to the Round-165 reduction,
then add the new node as a dependency of the still-open
`M9-M2-top-endpoint-density-discrepancy-energy` and
`M9-M2-top-endpoint-signed-cone` nodes.  No update contains a `status` field.

## 3. Proof and derivation of the graph audit

### 3.1 Homogeneous provenance and evidence polarity

The final kernel is an internal finite argument.  It invokes no external
source theorem, source power estimate, bare-orbit main-term theorem, or
source-dependent no-go.  Source-facing conclusions remain in the conductor
adjudication and rejected-route records.  This resolves the earlier
candidate's mixed-provenance recommendation.

The new reduction's positive evidence supports its finite identity,
multiplicity, Schur bound, and strict sector.  At the inherited Round-165
node, the internal kernel and adjudication are positive, while the hostile
source report and source-interface reviews are inconclusive.  At both open
parents, Round-167 material is inconclusive only.  No source audit is used
as proof of K17a or a parent.

Across all patch evidence fields there are thirteen unique paths, and all
thirteen exist.  In particular, the synthesis referenced once by each open
parent is now present.

### 3.2 Dependency direction and cycles

Reading an arrow from prerequisite to consumer, the new local graph is

\[
\text{Round 164 transport}
\longrightarrow
\text{Round 165 parity/gcd/scale}
\longrightarrow
\text{Round 167 endpoint/polylog reduction}
\longrightarrow
\text{density-discrepancy parent}
\longrightarrow
\text{signed-cone parent},
\]

with an additional direct arrow from the Round-167 reduction to the
signed-cone parent.  Every referenced obligation exists.  Neither the new
node nor either antecedent acquires a dependency on a downstream parent.
Consequently the added edges introduce no directed cycle.

### 3.3 Reject records

All eighteen `Round167-*` reject IDs are fresh and unique relative to both
current obligations and rejected claims.  Every record has a nonempty,
claim-specific reason.  The reasons correctly distinguish:

- exact representation from cancellation;
- Schur capacity from target saving;
- a polylogarithmic strict sector from K17a;
- the bare orbit cancellation from selector-dependent coefficients;
- the low-gcd witness's exact gamma and support scope;
- continuous rank-one nonseparability from universal interpolation failure;
- conditional source ledgers from a proved target;
- raw Part-I kernels from discrepancy kernels; and
- the audited source-interface no-go from all determinant methods.

No existing rejected claim requires correction.

### 3.4 Downstream nonpromotion

The only promoted status is the newly created strict reduction.  Both
hard-TOP parents remain `open`; the physical M2 assembly remains only a
proved conditional reduction; hard TOP, BAL, UNBAL, and M9--M2 remain open.
Both direct M1 parents, GAR, endpoint uniformity, M9, the standard and GAR
bridges, and the quarter theorem retain their current states.  The internal
\(1/3\) theorem and external Li--Yang benchmark are unchanged.  The patch
therefore contains no K17a, complete-residual, parent, bridge, or exponent
promotion.

## 4. First doubtful or unproved step

Mathematically, the first open step remains the non-polylogarithmic part of

\[
 \Re\mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\]

The endpoint form has only \(L^3X^\varepsilon\) positive capacity, so this
range still needs one factor \(L\) of genuine signed cancellation.  Nothing
in the patch asserts otherwise.

There is no remaining doubtful step in the graph packaging.  The synthesis,
campaign, ledger, plan snapshot, generated current-round file, and validation
gates are complete and mutually consistent; the only remaining action is
the conductor-owned State Patch application.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Starting graph provenance | **PASS.** The live graph hash equals the frozen Round-167 hash. |
| Official patch validation | **PASS.** `validate_state_patch` returns `Patch OK`. |
| In-memory dry application | **PASS.** One create, three updates, eighteen rejects, and seventeen no-change records produce no post-apply structural issue. |
| Node ID and dependency references | **PASS.** The created ID is fresh and every referenced obligation exists. |
| Dependency direction and local acyclicity | **PASS.** Antecedents feed the new reduction, which feeds only downstream open parents. |
| Homogeneous node provenance | **PASS.** Only internally proved finite claims enter the created node. |
| Evidence polarity | **PASS.** Parent attachments are inconclusive; source-route evidence does not promote an analytic owner. |
| Evidence-path existence | **PASS.** All thirteen unique paths exist, including the synthesis referenced by both parents. |
| Reject IDs and reasons | **PASS.** All eighteen are fresh, unique, nonempty, and correctly scoped. |
| K17a/residual/parent promotion | **PASS.** None occurs. |
| Endpoint, bridge, and exponent scope | **PASS.** All remain unchanged. |
| Protocol closure gate | **PASS.** Campaign and plan are complete, the ledger is closed, all ten Round-167 gates are green, and current-round output is complete. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/current_round.md`;
- `state/validation_matrix.yml`;
- `state/round_ledger.yml`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/plan.json`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_determinant_endpoint_polylog_shift_reduction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reviews/conductor_round167_adjudication.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reviews/final_internal_kernel_verification.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/synthesis.md`; and
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/state_patch.json`.

The official validator and a read-only in-memory application were used to
check schema, operation counts, and the post-patch graph.  No shared state
or proof artifact was edited.

## 7. Recommended state effect

**Apply the State Patch as written.**

The evidence path and closure-gate repairs are complete.  Campaign validation
returns `Campaign OK`; the State Patch dry run returns `Patch OK`; all
Round-167 validation artifacts resolve; and no open or downstream status is
promoted.

Apply exactly the proposed mathematical scope: create the proved internal
endpoint/polylogarithmic reduction, attach it inconclusively to the two open
hard-TOP parents, record the scoped rejections, and make no K17a, residual,
parent, bridge, quarter-theorem, or exponent promotion.  After application,
run the ordinary resulting-graph validator and record the applied graph hash.
