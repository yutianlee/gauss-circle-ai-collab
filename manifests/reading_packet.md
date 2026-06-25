# Reading Packet

Generated after round 2 in run `obligation-main`.

## Current Theorem Target

Target: `P(X)=N(sqrt(X))-pi X <<_epsilon X^(1/4+epsilon)`.

Current status: conditional only. No new Gauss circle exponent has been proved.

## Current Route

H1-H3 + H4 + R5-Full + M9 imply P(X) <<_epsilon X^(1/4+epsilon).

## Active Bottleneck

`M9`: open.

For X large and X^(1/4) <= D <= X^(1/2), the fixed-coefficient reciprocal sums M_1(D;X), M_2(D;X) satisfy M_i(D;X) <<_epsilon X^(1/4+epsilon), uniformly in all active dyadic D.

Current blockers:
- `M9-M2-character-factor` (open): M2 frequency-side character factor
- `M9-near-collision-taxonomy` (open): M2 fourth-moment near-collision taxonomy
- `M9-endpoint-uniformity` (open): Endpoint uniformity over active dyadic D

## Round Target Obligations

- `M9-M2-character-factor` (open, owner `A2`): M2 frequency-side character factor
  Next action: Use the exact beta_h algebra and the h-Cauchy sign-loss diagnostic to pursue the M2 fourth-moment route first; keep CRI and direct signed bilinear estimates as secondary diagnostics.
- `M9-near-collision-taxonomy` (open, owner `A2`): M2 fourth-moment near-collision taxonomy
  Next action: Complete the exact N=0 taxonomy using the corrected numerator N and actual beta_h weights. Resolve or explicitly preserve the unclassified class, prove or downgrade denominator-paired estimates, and formulate near-collision bands using |N| lesssim D^4/X.
- `M9-regression-raw-vs-paired` (proposed, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Produce committed or repository-ready artifacts: computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and computations/m9_regression/report.md. Use the official M1/M2 raw formulas and actual Vaaler coefficients; label all evidence diagnostic_only.

## Do-Not-Claim Rules

- Do not claim `M9` or the final Gauss circle target.
- Do not treat computation as proof; computation evidence is diagnostic only.
- Do not use Li-Yang, Vaaler, Huxley, or Bourgain-Watt as theorem dependencies without completed source cards.
- Do not promote a claim without exact statement, dependencies, evidence, and remaining caveats.

## Agent Assignments

Use `state/next_round_prompts.md` for any judge-assigned A1/A2/A3 tasks.

Default target split:
- `A1`: synthesis, proof-draft maintenance, source-card discipline, and State Patch authoring.
- `A2`: conservative obstruction analysis for the selected M9 obligations.
- `A3`: executable diagnostics or source-card artifacts, not prose-only plans.

## Relevant Files

- `state/proof_obligations.yml`
- `state/next_round_prompts.md`
- `state/best_proof_draft.md`
- `sources/vaaler_1985.md`
- `sources/li_yang_2023.md`
- `manifests/reading_packet.md`

## Last State Patch

created: M9-M2-N0-diagonal-core-bound; updated: M9-M2-character-factor, M9-near-collision-taxonomy, M9-regression-raw-vs-paired, M9-M2-fourth-moment-expansion; rejected: A2-R2-near-collision-taxonomy-promotion, A2-R2-denominator-paired-negligibility-proved, A2-R2-dual-length-explosion-route-closing, A2-R2-diagonal-core-one-sixteenth-union-constant, A3-R2-artifact-evidence-without-files, A3-R2-official-formula-normalization-unverified; no_change: M9, M9-M1, M9-M2, M9-near-collision-estimate, M9-endpoint-uniformity, GC-target, H4, H4-source-audit, Li-Yang-source-audit; round score: 3; Round 2 made useful algebraic and strategic progress on M2 and identified the fourth-moment route as primary, but no endpoint estimate, complete taxonomy, near-collision bound, or executable computation evidence was supplied.

## Active Obligation Briefs

### M9-M2-character-factor: M2 frequency-side character factor

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Use the exact beta_h algebra and the h-Cauchy sign-loss diagnostic to pursue the M2 fourth-moment route first; keep CRI and direct signed bilinear estimates as secondary diagnostics.

### M9-near-collision-taxonomy: M2 fourth-moment near-collision taxonomy

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`, `M9-M2-N0-diagonal-core-bound`
- Next action: Complete the exact N=0 taxonomy using the corrected numerator N and actual beta_h weights. Resolve or explicitly preserve the unclassified class, prove or downgrade denominator-paired estimates, and formulate near-collision bands using |N| lesssim D^4/X.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `proposed`
- Track: `computation`
- Owner: `A3`
- Next action: Produce committed or repository-ready artifacts: computations/m9_regression/run.py, outputs/table_small.csv, a precision log, and computations/m9_regression/report.md. Use the official M1/M2 raw formulas and actual Vaaler coefficients; label all evidence diagnostic_only.

### GC-target: Gauss circle conjectural exponent target

- Status: `open`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`
- Next action: Keep the target explicitly conditional until all bridge dependencies, especially M9, are proved.

### H4: Finite Vaaler approximation with floor-compatible residual

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Verify theorem labels, constants, residual convention, and integer values from rendered source pages.

### H4-source-audit: Rendered source audit for Vaaler 1985

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Complete the source card with rendered page/equation checks.

### Li-Yang-source-audit: Li-Yang theorem and rendered-PDF audit

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Resolve the Case A/B discrepancy from the rendered PDF and update the source card.

### M9: Endpoint bound for fixed Vaaler reciprocal main sums

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`, `M9-endpoint-uniformity`
- Next action: Formulate and attack the M2 fourth-moment or near-collision subproblem with the C_h=e(h/4)-e(3h/4) factor retained.

### M9-M1: M1 fixed-coefficient reciprocal-sum estimate

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-endpoint-uniformity`
- Next action: Separate any M1 estimate from M2 and state its coefficient hypotheses and D ranges.

### M9-M2: M2 fixed-coefficient reciprocal-sum estimate

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`
- Next action: Retain the two-sided convention and prove or refute the near-collision estimate with actual beta_h weights.

### M9-M2-N0-diagonal-core-bound: Diagonal-core bound for exact M2 fourth-moment resonances

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`
- Next action: Prove the bound with actual beta_h weights, bounded dyadic weights, explicit overlap conventions, and the H4 coefficient bound; do not use the incorrect 1/16 constant for the whole union.

### M9-endpoint-uniformity: Endpoint uniformity over active dyadic D

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Attach explicit D-range hypotheses to every proposed M1 or M2 estimate.

### M9-near-collision-estimate: Weighted near-collision estimate for M2 fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: After taxonomy, formulate this as an exact theorem with all coefficient weights and dyadic ranges.

### Conditional-bridge: Conditional bridge from accepted reductions to the target

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`, `H4-source-audit`
- Next action: Maintain the bridge in the proof draft, but do not promote the final theorem while M9 remains open.

### M9-M2-beta-algebra: Exact beta_h coefficient algebra for M2

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Verify the exact H4 coefficient convention from the Vaaler source card and then insert the beta_h algebra into the proof draft.

### M9-M2-fourth-moment-expansion: Algebraic fourth-moment expansion for M2 with retained character product

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`
- Next action: Use this only as an algebraic expansion. A2 should classify exact and near-collision configurations with actual beta_h weights; do not infer an analytic estimate from the expansion alone.

### M9-M2-h-cauchy-sign-loss: Weighted h-Cauchy loses the M2 frequency character sign

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Owner: `A1`
- Next action: Use this only as a diagnostic. A2 should test fourth moments, CRI, or direct signed bilinear estimates rather than treating this as a no-go theorem.

### R5-Full: Fejer residual product-count bound

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `H4-source-audit`
- Next action: Insert the proof with edge cases into the best proof draft after H4 source audit is complete.
