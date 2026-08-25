# Round 158 State Patch scope review

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Reviewed patch: `state_patch.json`
- Starting graph: `3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f`
- Role: terminal independent graph, evidence, and scope audit

## 1. Result

**Verdict: GREEN; no patch repair is required.** The patch is a faithful
encoding of `conductor_round158_adjudication.md`. It creates exactly one
proved-internal, route-scoped obstruction; updates exactly eight existing
records; corrects exactly one Round 157 rejected record; creates exactly
twenty-five new rejected records; and records exactly eight no-change
decisions.

The patch promotes only the exact moving-cell-trace reduction, its direct
zero/Nyquist trace-piece estimates, its endpoint face, and its calibrated
strict residual-mask frontier. It does not promote the strict trace target,
either Abel outer term, either profile-bulk remainder, the paired interior
matrix, a positive-power complete range, M9-M1, M9, the quarter target, or a
global exponent. Source conclusions retain the repaired cutoff-dated
no-match polarity.

The raw file hash of the current proof graph equals the campaign's starting
hash, so the patch was checked against the intended graph. A non-mutating
validation and an in-memory application with round index 158 and the
adjudication as judge reference both pass. The post-application graph has
zero schema or source-card issues.

## 2. Exact statement and patch census

The sole created record is

`M9-M1-lower-cone-t1-d1-paired-interior-cell-trace-obstruction`,

of type `obstruction`, track `M9_analytic`, and status
`proved_internal`. Its statement agrees with the accepted kernel:

\[
 \mathcal C_{\mathrm{int},U}(V)
 =\sum_{\ell\ge1}\chi _4(\ell)
 \bigl[\eta_+(\ell)W_+(\kappa(\ell))
      +\eta_-(\ell)W_-(\kappa(\ell))\bigr]
 +O_\varepsilon(M^{-1/4}X^\varepsilon),
\]

where

\[
 W_+(k)=w_U((k^2-k+1)/N)e(\sqrt{k^2-k+1}-k),
 \qquad
 W_-(k)=w_U((k^2+k)/N)e(\sqrt{k^2+k}-k).
\]

It explicitly distinguishes these boundary arguments from the selected
quotient \(\ell=(k^2-s)/N\), states that the trace is zero unless
\(V\asymp K=\sqrt{NM}\), and correctly retains capacity \(M\) on the
possibly nonzero block. The scalar target is
\(O_\varepsilon(X^\varepsilon)\), equivalently raw
\(M^{3/4}X^\varepsilon\); raw square root is described only as a stronger
sufficient estimate.

The eight updates are exactly:

1. `M9-M1-lower-cone-t1-d1-root-defect-logarithmic-collar-reduction`;
2. `M9-M1-d1-theta-kloosterman-source-audit`;
3. `M9-M1-lower-cone-t1-d1-root-dispersion-obstruction`;
4. `M9-M1-d1-outer-defect-spectral-source-audit`;
5. `M9-M1-lower-cone-t1-d1-complete-theta-inversion-obstruction`;
6. `M9-M1-lower-cone-t1-d1-nonzero-centering-nyquist-fold`;
7. `M9-M1-lower-cone-t1-squarefree-large-wrap-collar-obstruction`; and
8. `M9-M1-global-lower-radial-signed-estimate`.

All eight already exist. None receives a status promotion. The eight
no-change records also all exist and are exactly `M9-M1`, `M9-M2`,
`M9-endpoint-uniformity`, `M9`, `Conditional-bridge`,
`GC-partial-one-third`, `GC-external-Li-Yang-theta-star`, and
`GC-target`; their present statuses are preserved.

## 3. Proof of patch fidelity

### 3.1 Evidence paths and polarity

There are 37 evidence/source-card path occurrences, representing ten
distinct repository paths. Every one exists. The accepted kernel,
discovery report, strict-survivor control, finite-algebra reconciliation,
trace-mathematics review, hostile power review, and adjudication are
positive evidence for the narrow internal obstruction.

The unreconciled blind report is correctly placed in the new record's
`inconclusive` bucket: its finite algebra is useful, but its conditional
Weil capacities, initial normalization doubt, sparse-statement localization,
and target calibration are not promoted. Its reconciliation review is
positive only for the finite algebra it validates.

The source report and independent source review are conservatively
`inconclusive` evidence for the new internal obstruction, while they are
positive evidence for the two source-audit records whose claims they
actually establish. The independent review's repair-confirmation addendum
is present: the residual boundary phases remain \(k\)-dependent
coefficients, not fixed Fourier shifts, and \(390/703\) is only the best
threshold among the explicitly audited favorable-model lines. Thus the
patch's source polarity is exact rather than adverse or overclaiming.

### 3.2 Corrected rejected record

The corrected ID
`Round157-moving-cell-trace-has-absolute-cost-Mminusthreequarters`
exists in the current rejected-claim ledger. The replacement reason makes
the necessary distinction:

\[
 VM^{-3/4}X^\varepsilon
 \quad\hbox{is a generic pre-inversion capacity, whereas}\quad
 M^{-3/4}\min(M,V)X^\varepsilon
\]

is the exact selected-trace absolute capacity. Nonzero boundary support
forces \(V\asymp K\), hence \(\min(M,V)=M\) and the latter becomes
\(M^{1/4}X^\varepsilon\), still above the scalar target. The correction
does not manufacture signed cancellation or remove the rejection. Its
three evidence paths all exist.

### 3.3 Twenty-five new rejects

All twenty-five reject IDs are new: none collides with an obligation or an
existing rejected record, none is duplicated inside the patch, and none is
reused by another patch operation. Exhaustively, they cover:

- endpoint/profile/pairing overclaims: endpoint roots control the strict
  trace; boundary weight equals the profile at \(\ell\); the two boundary
  weights are equal or conjugate; the strict selectors pair automatically;
  and \(\ell,\ell+2\) pairing forces cancellation;
- capacity/target/method overclaims: support cardinality is signed
  cancellation; top localization proves the target; the target is
  \(M^{-1/4}\); raw square root is necessary; ordinary \(\chi _4\)-Abel
  controls the mask; profile BV gives diagonal BV; standard
  second-derivative discrepancy, the classical exponent pair, the audited
  transformed pair, or incomplete quadratic completion closes the cone;
  fixed-endpoint Vaaler applies literally; and the residual phase is a
  fixed Fourier shift;
- trace/seam overclaims: whole zero/Nyquist rows transfer to trace pieces;
  the endpoint face proves the trace; the explicit survivor is a signed
  lower bound; the Abel outer terms are target-safe; the cell trace controls
  profile bulk or the full matrix; and \(c=4\) has generic interior modes;
  and
- source/downstream overclaims: the audited no-match is a literature
  impossibility theorem, or the trace reduction changes a global exponent.

These are exactly the 5+12+6+2 IDs printed in the patch. Every reason has
the polarity and scope of the adjudication. Applied with the adjudication
as `judge_ref`, each becomes a rejected-claim record with that exact
evidence path.

### 3.4 Eight updates and eight no-change decisions

The first six updates refine only the existing \(D=d=L=1\) collar,
theta/source, dispersion, complete-inversion, and centering frontiers. The
last two add the new obstruction as a dependency of the squarefree
large-wrap collar and global lower-radial owner. Their next actions all
require the literal strict sum and separately quarantine both outer and
both profile-bulk terms.

The no-change decisions match the current graph: M9-M1, M9-M2,
endpoint uniformity, M9, and GC-target remain open; Conditional-bridge
remains derived under assumptions; the internal \(1/3\) theorem remains
proved; and the external Li--Yang exponent remains
\((3292+25\sqrt{1717})/13762\). No range or exponent is enlarged.

### 3.5 Dependency direction and cycles

The new obstruction depends on
`M9-M1-lower-cone-t1-d1-nonzero-centering-nyquist-fold`. It in turn
implies the squarefree large-wrap collar and global lower-radial owner, and
the patch adds the reciprocal dependency entries to exactly those two
downstream nodes. Every dependency and implication target exists. The
direction is therefore prerequisite \(\leftarrow\) new reduction
\(\leftarrow\) downstream owner, not the reverse.

An independent before/after dependency traversal finds no patch-created
cycle. The current graph already contains three unrelated two-node cycles:

1. hard-top product-fibre mean obstruction / transform self-return;
2. lower post-collar smoothed far-alias reduction / far-cone microscopic
   cell reduction; and
3. lower-height rank-one product-fibre obstruction / incomplete-fibre
   dispersion obstruction.

The identical three cycles remain after an in-memory application; none
contains a Round 158 node or edge. They are pre-existing graph debt, not a
repair required in this patch.

## 4. First doubtful or unproved step

There is no doubtful patch mutation after the mechanical and scope checks.
The first unproved mathematical step remains the literal strict estimate

\[
 \left|\sum_{\ell\ge1}\chi_4(\ell)
 \bigl[\eta_+(\ell)W_+(\kappa(\ell))
      +\eta_-(\ell)W_-(\kappa(\ell))\bigr]\right|
 \ll_\varepsilon X^\varepsilon,
\]

equivalently raw \(M^{3/4}X^\varepsilon\). Even its proof would leave the
positive right Abel endpoint, negative left Abel endpoint, and two
profile-difference remainders as separate open seams before the full paired
matrix.

The only operational condition is to apply the patch with round index 158
and `reviews/conductor_round158_adjudication.md` as the judge reference, as
used in the in-memory validation. This attaches evidence to the 25 newly
created rejected records; it requires no JSON repair.

## 5. Required control tests and outcomes

- JSON parse and ordinary patch validation: **GREEN** (`Patch OK`).
- Starting-graph SHA-256: **GREEN**, exact campaign match.
- Census 1/8/1/25/8: **GREEN**.
- Existing targets for all updates, correction, and no-change entries:
  **GREEN**.
- New-ID and cross-operation collision tests: **GREEN**.
- Evidence/source-card existence, 37 occurrences and ten unique paths:
  **GREEN**.
- In-memory application and post-application graph validation:
  **GREEN**, zero issues; 362 obligations and 1165 rejected claims.
- Dependency and implication targets/directions: **GREEN**.
- Cycle delta: **GREEN**, zero new cycles; three unrelated legacy cycles
  unchanged.
- Source polarity and repaired residual-phase wording: **GREEN**.
- Scalar target \(X^\varepsilon\), raw threshold \(M^{3/4}\), stronger
  special-row error \(M^{-1/4}\), and absolute capacity \(M^{1/4}\):
  **GREEN**.
- \(V\asymp K\) localization treated only as a zero range and
  \(\min(M,V)=M\) on support: **GREEN**.
- Both Abel outer terms, both profile-bulk remainders, and external
  \(B_{1,U}(1)\) seam quarantined: **GREEN**.
- Positive-power range, whole-trace theorem, paired matrix, M9-M1, M9,
  bridge, quarter target, and exponent non-promotion: **GREEN**.

No numerical experiment, external write, or web theorem import was used.

## 6. Dependencies and exact artifacts used

This review used:

- `protocol.md`;
- `state/active_campaign.yml`;
- `state/proof_obligations.yml`;
- the campaign's `state_patch.json`;
- `reviews/conductor_round158_adjudication.md`;
- `proofs/kernels/m9_m1_d1_paired_interior_cell_trace_reduction.md`;
- `proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md`;
- `reports/cell_trace_source_audit.md` and the repaired
  `reviews/independent_source_round158.md`;
- `reviews/independent_blind_reconciliation_round158.md` and
  `reviews/independent_trace_math_round158.md`; and
- `math_collab/proof_obligations.py` and
  `math_collab/validate_state_patch.py` for non-mutating mechanical
  validation.

The ten distinct paths cited by the patch were also checked for existence.
No patch, shared state, proof draft, validation matrix, synthesis, candidate,
kernel, report, or other review was edited.

## 7. Recommended state effect

Apply the patch unchanged with the stated round index and judge reference.
It records a proved exact reduction and a route-scoped obstruction, not a
proof of the strict trace or of any downstream theorem. Preserve the three
pre-existing unrelated dependency cycles for a separate graph-hygiene task;
they are neither introduced nor touched here.

No exact required repairs.

**GREEN.**
