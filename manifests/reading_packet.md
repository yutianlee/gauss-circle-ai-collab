# Reading Packet

Generated for active campaign `m9-m2-top-endpoint-signed-offset-energy`.

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

## Selected Target Obligations

- `M9-near-collision-absolute-lower-bounds` (derived_under_assumptions, historical steward `A4`): Absolute near-collision lower bounds obstruct endpoint GNC
  Next action: Treat the actual weighted absolute W-1 obstruction as applicable to every active block of the chosen partition. It remains conditional on the matching exact-N=0 closure and remains unsigned/absolute only.
- `M9-near-collision-estimate` (proposed, historical steward `A2`): Weighted near-collision estimate for M2 fourth moment
  Next action: Do not seek universal numerator-residue cancellation. Either prove denominator-level cancellation in the two-adically locked sector or prefer a direct pointwise frequency-block estimate on the remaining (D,L) region.
- `M9-M2-character-factor` (open, historical steward `A2`): M2 frequency-side character factor
  Next action: Use the exact chi_4(r_d) sine kernel or retain chi_4(h) in the dual product phase. The two shifts reinforce odd frequencies; they do not cancel each other.

## Do-Not-Claim Rules

- Do not claim `M9` or the final Gauss circle target.
- Do not treat computation as proof; computation evidence is diagnostic only.
- Do not use Li-Yang, Vaaler, Huxley, or Bourgain-Watt as theorem dependencies without completed source cards.
- Do not promote a claim without exact statement, dependencies, evidence, and remaining caveats.

## Active Subagent Campaign

Use `state/next_campaign.md` and `state/active_campaign.yml` for current task briefs.

Campaign rules:
- Codex is the persistent coordinator and the only writer of shared proof state.
- Temporary subagents receive narrow, context-isolated briefs selected by mathematical interface.
- Use at most three concurrent subagents; use functional roles rather than permanent identities.
- Do not vote. Validate the smallest candidate kernel by seam and blind rederivation.
- A rigorous no-go result is useful progress.

Diagnostic execution policy:
- Computation is `diagnostic_only` and must include exact code, runtime output, parameters, pass/fail criteria, and limitations.
- The coordinator must reproduce important diagnostics locally before they count as positive diagnostic evidence.
- Passing numerics cannot promote an asymptotic claim; a failed control may reject one.

## Relevant Files

- `state/proof_obligations.yml`
- `state/project_summary.md`
- `state/active_campaign.yml`
- `state/current_round.md`
- `state/round_ledger.yml`
- `state/next_campaign.md`
- `state/failure_ledger.md`
- `state/control_models.md`
- `state/validation_matrix.yml`
- `state/best_proof_draft.md`
- `sources/vaaler_1985.md`
- `sources/li_yang_2023.md`
- `manifests/reading_packet.md`

## Last State Patch

No State Patch applied. Campaign preparation changes workflow artifacts only.

## Active Obligation Briefs

### M9-near-collision-absolute-lower-bounds: Absolute near-collision lower bounds obstruct endpoint GNC

- Status: `derived_under_assumptions`
- Track: `M9_analytic`
- Historical steward: `A4` (non-binding)
- Next action: Treat the actual weighted absolute W-1 obstruction as applicable to every active block of the chosen partition. It remains conditional on the matching exact-N=0 closure and remains unsigned/absolute only.

### M9-near-collision-estimate: Weighted near-collision estimate for M2 fourth moment

- Status: `proposed`
- Track: `M9_analytic`
- Historical steward: `A2` (non-binding)
- Next action: Do not seek universal numerator-residue cancellation. Either prove denominator-level cancellation in the two-adically locked sector or prefer a direct pointwise frequency-block estimate on the remaining (D,L) region.

### M9-M2-character-factor: M2 frequency-side character factor

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `A2` (non-binding)
- Next action: Use the exact chi_4(r_d) sine kernel or retain chi_4(h) in the dual product phase. The two shifts reinforce odd frequencies; they do not cancel each other.

### GC-target: Gauss circle conjectural exponent target

- Status: `open`
- Track: `proof_infrastructure`
- Historical steward: `A1` (non-binding)
- Blockers: `M9`
- Next action: Keep the target explicitly conditional until all bridge dependencies, especially M9, are proved.

### Li-Yang-source-audit: Li-Yang theorem and rendered-PDF audit

- Status: `source_audit_required`
- Track: `source_audit`
- Historical steward: `A1` (non-binding)
- Next action: Complete the rendered-PDF source card, resolve the apparent M<T^(-7/16) versus M<T^(7/16) threshold inconsistency, and transcribe all auxiliary conditions. Record that the published output exponent exceeds 1/4 even in height-admissible regions.

### M9: Endpoint bound for fixed Vaaler reciprocal main sums

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `A2` (non-binding)
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`, `M9-endpoint-uniformity`
- Next action: Formulate and attack the M2 fourth-moment or near-collision subproblem with the C_h=e(h/4)-e(3h/4) factor retained.

### M9-M1: M1 fixed-coefficient reciprocal-sum estimate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `A2` (non-binding)
- Blockers: `M9-endpoint-uniformity`
- Next action: Attack the exact global angular symbol by Mellin separation, while separately auditing whether the final bridge may use the global M1 aggregate instead of every dyadic M1 block.

### M9-M1-alpha-bounded-zeta-high-transition-bound: Connector-completed alpha-bounded zeta-high transition bound

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: First solve the physical signed short twisted-divisor core. The exact endpoint Fourier reduction supplies no connector or height-limit estimate.

### M9-M1-cross-product-odd-kernel-discrepancy: Cross-product odd-kernel discrepancy estimate for the M1 residual corridor

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Prove PSC or a weaker whole-sum ordered-denominator estimate on U_1. Opposite-offset reflection is only a reindexing and cannot supply the saving termwise.

### M9-M1-dual-restricted-convolution-RCS: Dual restricted-convolution estimate for M1 resonance cells

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Use the exact coefficient self-return to distinguish full terminal sectors from short moving strips; product completion alone supplies no signed estimate.

### M9-M1-global-angular-radial-estimate: Global angular radial estimate for the active M1 aggregate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: The fixed-interior residual is now the exact actual-unit off-diagonal H for J^(32/45)<C<=J, together with the upper axes. Prove that correlation, then reconcile cone edges and the remaining radial sectors; no global exponent follows from the reduction alone.

### M9-M1-maximal-angular-sign-kernel: Maximal actual-profile angular-sign radial correlation

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Use the exact finite vector identity; the swept transition/horizontal operator is now the principal reflected-mode blocker.

### M9-M1-post-FE-vector-kernel: Uniform vector-valued reflected Hankel kernel estimate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Estimate the connector-completed beta transition first, then the alpha transition; the finite partial-FE identities alone do not control the vector kernel.

### M9-M1-renormalized-radial-boundary-operator: Renormalized radial endpoint and diagonal vector-Hilbert operator

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Prove the connector-completed projected alpha trace; all radial endpoint, R1 arithmetic, radial-side, and beta-owned interfaces remain closed.

### M9-M1-shifted-divisor-correlation-PSC: Annular paired shifted-divisor correlation for M1

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: The delta/Kloosterman reformulation retains the same H/L-sized deficit in a short moving numerator. Standard complete-sum estimates do not prove PSC; a genuinely joint signed near-product theorem remains necessary.

### M9-M1-swept-transition-horizontal-operator: Swept single-transition and horizontal-side vector operator

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Close the explicit projected alpha cosine-Cauchy/GAR-return obligation; the beta branch is already closed and must not be reopened.

### M9-M1-top-Perron-angular-correlation: Reflected angular-mode correlation with top Perron maximal control

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Retain the two axial residues and estimate the exact matching profile projection; the vanished joint antisymmetric residue is not enough.

### M9-M1-top-endpoint-signed-cone: Signed product-phase cone estimate for the top M1 block

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: The terminal h-shell is proved by the direct divisor estimate. Prove only the middle/lower hard-top shells, equivalently the intersection of this cone with U_1.

### M9-M2: M2 fixed-coefficient reciprocal-sum estimate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `A2` (non-binding)
- Blockers: `M9-M2-character-factor`, `M9-near-collision-taxonomy`, `M9-M2-denominator-paired-weighted-bound`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`
- Next action: For the hard top block attack the exact alternating transposed-row energy. Smooth interior small-gcd packets and the fourth-moment/pointwise interface remain separate.

### M9-M2-GM4-from-exact-plus-graded: Global fourth-moment route from exact resonance plus graded near-collision

- Status: `proposed`
- Track: `M9_analytic`
- Historical steward: `A1` (non-binding)
- Blockers: `M9-near-collision-estimate`, `M9-M2-LFM-pointwise-equivalence`
- Next action: Do not use exact N=0 plus an absolute graded estimate to promote M9-M2. The absolute fat-band target is false for D > X^(3/8+delta), and a global L4 estimate plus crude derivative propagation gives only D^(3/5)X^(3/20+epsilon). Any viable route now needs signed fat-band control and a large-value or direct pointwise theorem.
