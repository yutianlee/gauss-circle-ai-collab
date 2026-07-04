# Reading Packet

Generated after round 8 in run `obligation-main`.

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
  Next action: Use the signed lift-cancellation B1 lemma and c_chi target to preserve the chi_4(h) structure in upper-range near-collision analysis. Do not use character-blind absolute norms past D=X^(3/8).
- `M9-near-collision-taxonomy` (open, owner `A2`): M2 fourth-moment near-collision taxonomy
  Next action: Record that the exact N=0 arm is conditionally closed under H4. Keep the obligation open for 0<|N|~T near-collision bands, endpoint uniformity, and pointwise upgrade.
- `M9-regression-raw-vs-paired` (diagnostic_only, owner `A3`): Raw-vs-paired numerical stress test for M9
  Next action: Correct the complex-weight test: cosine pairing can hold for shared complex d-weights, while the Re B_h shortcut fails. Execute and archive script, command, table, precision log, and report.

## Do-Not-Claim Rules

- Do not claim `M9` or the final Gauss circle target.
- Do not treat computation as proof; computation evidence is diagnostic only.
- Do not use Li-Yang, Vaaler, Huxley, or Bourgain-Watt as theorem dependencies without completed source cards.
- Do not promote a claim without exact statement, dependencies, evidence, and remaining caveats.

## Agent Assignments

Use `state/next_round_prompts.md` for any judge-assigned A1/A2/A3/A4 tasks.

Default target split:
- `A1`: synthesis, proof-draft maintenance, source-card discipline, and State Patch authoring.
- `A2`: conservative obstruction analysis for the selected M9 obligations.
- `A3`: executable diagnostics or source-card artifacts, not prose-only plans.
- `A4`: independent analytic proof-surgery for narrow sublemmas and route repair.

## Relevant Files

- `state/proof_obligations.yml`
- `state/next_round_prompts.md`
- `state/best_proof_draft.md`
- `sources/vaaler_1985.md`
- `sources/li_yang_2023.md`
- `manifests/reading_packet.md`

## Last State Patch

created: M9-M2-interval-URES-strip-identity, M9-M2-interval-URES-strip-count, M9-near-collision-absolute-lower-bounds, M9-M2-signed-lift-cancellation-B1, M9-M2-signed-fat-band-constant; updated: M9-near-collision-estimate, M9-M2-GM4-from-exact-plus-graded, M9-M2-fourth-moment-average-to-pointwise, M9-M2-exact-N0-total-mass, M9-M2-URES-representation-divisor-bound, M9-M2-URES-energy-reduction, M9-M2-unpaired-residual-URES, M9-M2-character-factor, M9-fourth-moment-enumeration, M9-regression-raw-vs-paired, H4-source-audit; rejected: A1-R8-global-GNC-low-for-all-D, A1-R8-full-range-GNC-Abs, A2-R8-M9-M2-absolute-mass-obstruction-proved-internal, A2-R8-URES-interval-factorization-as-written, A2-R8-Poisson-B-Process-Transform-proved, A3-R8-diagnostics-as-proof; no_change: M9, M9-M1, M9-M2, M9-endpoint-uniformity, GC-target, Conditional-bridge, H4, R5-Full, Li-Yang-source-audit; round score: 6; Round 8 makes real proof-graph-safe progress by refuting the old absolute near-collision route in upper dyadic ranges, adding interval URES strip infrastructure, and defining the signed fat-band target. It does not prove M9, M9-M2, M9-M1, H4, or the Gauss circle endpoint.

## Active Obligation Briefs

### M9-M2-character-factor: M2 frequency-side character factor

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Use the signed lift-cancellation B1 lemma and c_chi target to preserve the chi_4(h) structure in upper-range near-collision analysis. Do not use character-blind absolute norms past D=X^(3/8).

### M9-near-collision-taxonomy: M2 fourth-moment near-collision taxonomy

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-near-collision-estimate`, `M9-M2-N0-diagonal-core-bound`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`, `M9-M2-unpaired-residual-URES`, `M9-M2-unpaired-reduced-paired-bound`, `M9-M2-NF-participation-rigidity`
- Next action: Record that the exact N=0 arm is conditionally closed under H4. Keep the obligation open for 0<|N|~T near-collision bands, endpoint uniformity, and pointwise upgrade.

### M9-regression-raw-vs-paired: Raw-vs-paired numerical stress test for M9

- Status: `diagnostic_only`
- Track: `computation`
- Owner: `A3`
- Next action: Correct the complex-weight test: cosine pairing can hold for shared complex d-weights, while the Re B_h shortcut fails. Execute and archive script, command, table, precision log, and report.

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
- Next action: Promote only after the Vaaler source card is physically updated and validated; until then use H4-dependent lemmas as derived_under_assumptions.

### H4-source-audit: Rendered source audit for Vaaler 1985

- Status: `source_audit_required`
- Track: `source_audit`
- Owner: `A1`
- Next action: Finalize sources/vaaler_1985.md with DOI, local PDF path, Theorem 6 equation (2.28), Section 7 equations (7.1)-(7.3), Theorem 18 equations (7.13)-(7.17), coefficient sign, Fejer normalization, residual constant, floor-compatible endpoint convention, Phi regularity, beta lower envelope, and M2 parity support.

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
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`
- Next action: Do not promote from AP, DP scoping, or paired/fraction subfamilies. Supply a pointwise M2 estimate, a local fourth-moment estimate valid at endpoint, or a sign-preserving direct estimate with uniformity.

### M9-M2-GM4-from-exact-plus-graded: Global fourth-moment route from exact resonance plus graded near-collision

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A1`
- Blockers: `M9-near-collision-estimate`, `M9-M2-LFM-pointwise-equivalence`
- Next action: Do not use exact N=0 plus an absolute graded estimate to promote M9-M2. The absolute fat-band target is false for D > X^(3/8+delta), and a global L4 estimate plus crude derivative propagation gives only D^(3/5)X^(3/20+epsilon). Any viable route now needs signed fat-band control and a large-value or direct pointwise theorem.

### M9-M2-direct-signed-bilinear-lemma: Direct signed bilinear estimate for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `M9-M2-reciprocal-SPD-route`
- Next action: Recast as a precise sign-preserving discrepancy or spacing theorem. Require A3 signed-vs-unsigned evidence before allocating major proof effort.

### M9-M2-fourth-moment-average-to-pointwise: Average-to-pointwise upgrade for M2 fourth-moment estimates

- Status: `open`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `M9-M2-local-fourth-moment-LFM`, `M9-M2-subcoherence-window-multiplier`, `M9-M2-LFM-pointwise-equivalence`
- Next action: Record the frozen-coefficient derivative obstruction: global L4 plus |S2'| << H_D gives only |S2(D;X0)| << D^(3/5) X^(3/20+epsilon), equal to X^(9/20+epsilon) at D=X^(1/2). Require a stronger large-value theorem, local signed cancellation theorem, or direct signed pointwise estimate.

### M9-M2-local-fourth-moment-LFM: Everywhere-local fourth-moment estimate for S2 on coherence windows

- Status: `open`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `M9-near-collision-estimate`, `M9-endpoint-uniformity`, `M9-M2-local-fourth-moment-kernel`, `M9-M2-subcoherence-window-multiplier`, `M9-M2-LFM-pointwise-equivalence`
- Next action: Do not treat coherence-window LFM as a relaxed average route. Any proof must provide full h,d-space cancellation, replace LFM by global moment plus large-value propagation, or split off endpoint blocks with a direct signed estimate.

### M9-M2-reciprocal-SPD-route: Sign-preserving reciprocal discrepancy route for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A4`
- Blockers: `H4-source-audit`, `Li-Yang-source-audit`
- Next action: State the exact SPD-1 discrepancy theorem and SPD-J jump/near-jump convention; separate integer-X exact jumps from real-X near-jumps; require A3 true-vs-unsigned-vs-random-vs-adversarial diagnostics before major proof investment.

### M9-M2-sign-preserving-poisson-voronoi-route: Sign-preserving Poisson or B-process route for M2

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`, `Li-Yang-source-audit`
- Next action: Restate as a smooth-weight stationary-phase obligation with exact constants, boundary terms, k=0 terms, nonstationary ranges, support-edge stationary points, and a signed post-transform estimate.

### M9-M2-signed-fat-band-constant: Signed fat-band constant for M2 global fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Blockers: `H4-source-audit`, `M9-M2-fourth-moment-average-to-pointwise`
- Next action: State the exact frozen-coefficient identity, define c_chi and its unsigned analogue, and prove a bound or produce signed diagnostic evidence showing failure.

### M9-endpoint-uniformity: Endpoint uniformity over active dyadic D

- Status: `open`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Require each M2 route to isolate the endpoint D=X^(1/2), where the AP/local-average bridge degenerates to pointwise control.

### M9-near-collision-estimate: Weighted near-collision estimate for M2 fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Owner: `A2`
- Next action: Replace the old full-range absolute GNC target. For D <= X^(3/8+o(1), audit restricted absolute or structured estimates using interval URES. For D > X^(3/8), pursue signed mechanisms such as c_chi or a sign-preserving Poisson/B-process estimate. Keep exact N=0, absolute lower bounds, signed estimates, and pointwise upgrade as separate obligations.

### Conditional-bridge: Conditional bridge from accepted reductions to the target

- Status: `derived_under_assumptions`
- Track: `proof_infrastructure`
- Owner: `A1`
- Blockers: `M9`, `H4-source-audit`
- Next action: Maintain the bridge in the proof draft, but do not promote the final theorem while M9 remains open.
