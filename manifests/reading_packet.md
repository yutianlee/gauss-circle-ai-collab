# Reading Packet

Generated for active campaign `m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation`.

## Current Theorem Target

Target: `P(X)=N(sqrt(X))-pi X <<_epsilon X^(1/4+epsilon)`.

Current status: conditional only. No new Gauss circle exponent has been proved.

## Current Route

H1-H3 + H4 + R5-Full + M9 imply P(X) <<_epsilon X^(1/4+epsilon).

## Active Bottleneck

`M9`: open.

For X large and X^(1/4) <= D <= X^(1/2), the fixed-coefficient reciprocal sums M_1(D;X), M_2(D;X) satisfy M_i(D;X) <<_epsilon X^(1/4+epsilon), uniformly in all active dyadic D.

Current blockers:
- `M9-endpoint-uniformity` (open): Endpoint uniformity over active dyadic D
- `M9-M1-top-endpoint-signed-cone` (open): Signed product-phase cone estimate for the top M1 block
- `M9-M1-direct-smooth-residual-blockwise-estimate` (open): Literal smooth residual blockwise M1 estimate
- `M9-M2-top-endpoint-density-discrepancy-energy` (open): Canonical joint density-discrepancy energy for the residual hard top M2 cone
- `M9-M2-smooth-balanced-quarter-packet-estimate` (open): Balanced smooth residual signed quarter-packet estimate
- `M9-M2-smooth-unbalanced-three-quarter-estimate` (open): Unbalanced smooth residual product-phase three-quarter estimate

## Selected Target Obligations

- `M9-near-collision-absolute-lower-bounds` (derived_under_assumptions, historical steward `A4`): Absolute near-collision lower bounds obstruct endpoint GNC
  Next action: Treat the actual weighted absolute W-1 obstruction as applicable to every active block of the chosen partition. It remains conditional on the matching exact-N=0 closure and remains unsigned/absolute only.
- `M9-near-collision-estimate` (proposed, historical steward `A2`): Weighted near-collision estimate for M2 fourth moment
  Next action: Do not seek universal numerator-residue cancellation. Either prove denominator-level cancellation in the two-adically locked sector or prefer a direct pointwise frequency-block estimate on the remaining (D,L) region.
- `M9-M2-character-factor` (proved_internal, historical steward `A2`): M2 frequency-side character factor
  Next action: Use the exact chi_4 factor as a proved no-erasure normalization guardrail. It is not an analytic estimate and no longer blocks M9-M2.

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

### GC-W7-16-actual-reduced-determinant-correlation: Actual signed reduced-determinant correlation at W=Y^(7/16)

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Seek a phase-sensitive determinant or additive-divisor estimate with the literal character placements, or prove a fixed power saving in Popov's additive local-discrepancy term.

### GC-nonsubcoherent-actual-cluster-local-moment: Non-subcoherent actual M1/M2 cluster local moment

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: At W=Y^(7/16), the exact remaining block theorem is GC-W7-16-actual-reduced-determinant-correlation. Do not repeat coefficient-blind Farey spacing; seek literal signed phase/character cancellation or a power saving in the additive full-discrepancy term.

### GC-target: Gauss circle conjectural exponent target

- Status: `open`
- Track: `proof_infrastructure`
- Historical steward: `A1` (non-binding)
- Blockers: `M9`
- Next action: Close either the standard blockwise Conditional-bridge or the alternative GAR plus M9-M2 bridge. No quarter estimate is currently proved.

### M9: Endpoint bound for fixed Vaaler reciprocal main sums

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `A2` (non-binding)
- Blockers: `M9-endpoint-uniformity`, `M9-M1-top-endpoint-signed-cone`, `M9-M1-direct-smooth-residual-blockwise-estimate`, `M9-M2-top-endpoint-density-discrepancy-energy`, `M9-M2-smooth-balanced-quarter-packet-estimate`, `M9-M2-smooth-unbalanced-three-quarter-estimate`
- Next action: On the standard route, prove the two direct M1 and three M2 analytic parents and retain endpoint uniformity. Alternatively, prove GAR and M9-M2 through GC-global-M1-alternative-bridge without claiming blockwise M9.

### M9-M1: M1 fixed-coefficient reciprocal-sum estimate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `A2` (non-binding)
- Blockers: `M9-M1-top-endpoint-signed-cone`, `M9-M1-direct-smooth-residual-blockwise-estimate`
- Next action: Prove the residual hard top signed cone and literal smooth residual estimate, or one alternative whole-U_1 theorem. The canonical global Gram has no direct blockwise implication.

### M9-M1-alpha-bounded-zeta-high-transition-bound: Connector-completed alpha-bounded zeta-high transition bound

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: First solve the physical signed short twisted-divisor core. The exact endpoint Fourier reduction supplies no connector or height-limit estimate.

### M9-M1-canonical-hard-actual-symbol-Gram-estimate: Canonical hard actual-symbol Fejer-Gram estimate on the first residual M1 band

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Blockers: `M9-M1-canonical-hard-actual-vector-directional-estimate`
- Next action: Close the fixed actual-vector directional estimate with the complete two-adic unitary convolution retained. Constant-character, lower-period, long-return aligned or reversal, and maximal-period blocks all remain unless a prior owner applies.

### M9-M1-canonical-hard-actual-vector-directional-estimate: Fixed actual-vector directional estimate for the canonical hard Gram

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Prove cancellation in the exact full two-adic fixed-vector scalar after the odd labels and conductor rows are summed before absolute value. The local operator is unitary and its affine Fourier support supplies no J^(-1/6) norm gain.

### M9-M1-cross-product-odd-kernel-discrepancy: Cross-product odd-kernel discrepancy estimate for the M1 residual corridor

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Prove PSC or a weaker whole-sum ordered-denominator estimate on U_1. Opposite-offset reflection is only a reindexing and cannot supply the saving termwise.

### M9-M1-direct-smooth-residual-blockwise-estimate: Literal smooth residual blockwise M1 estimate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Prove the literal smooth residual estimate, or replace it and the hard child by one whole-U_1 theorem such as the exact odd-kernel or RCS target. Do not import the global canonical Gram without a block-local inverse.

### M9-M1-dual-restricted-convolution-RCS: Dual restricted-convolution estimate for M1 resonance cells

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Use the exact coefficient self-return to distinguish full terminal sectors from short moving strips; product completion alone supplies no signed estimate.

### M9-M1-global-angular-radial-estimate: Global angular radial estimate for the active M1 aggregate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Blockers: `M9-M1-global-lower-radial-signed-estimate`, `M9-M1-global-radial-interface-estimate`
- Next action: Prove the exact lower-radial and sharp-interface parents. Canonical, alpha, near-product, and conductor programs are alternative nested attacks, not conjunctive GAR dependencies.

### M9-M1-global-lower-radial-signed-estimate: Exact lower-radial signed aggregate for global M1

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Prove the exact lower-radial signed aggregate. Treat alpha and product-wavelet/conductor decompositions as alternative refinements, not simultaneous owners.

### M9-M1-global-radial-interface-estimate: Sharp radial endpoint and interface estimate for global M1

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Prove the exact sharp radial/top interface package without extending the compact critical theorem to its excluded endpoint.

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
