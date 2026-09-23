# Reading Packet

Generated for active campaign `m9-m1-t1-p2-cross-gcd-cellular-boundary-gate`.

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
  Next action: Retain chi_4(g) outside and chi_4(n) inside the modulus sum exactly. The internal cusp identity embeds chi_4(n) arithmetically but supplies no analytic saving; no positive norm may erase either character direction before a signed estimate.

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
- Next action: The best complete bound remains Y^(35/48). The direct Demeter--Wu and direct or factor-first Li--Yang/BI interfaces are parked. Continue only with a genuinely new joint signed theorem that retains the literal coefficient before positive norms and has a complete capacity below Y^(27/48), or rotate to a distinct accepted proof frontier.

### GC-nonsubcoherent-actual-cluster-local-moment: Non-subcoherent actual M1/M2 cluster local moment

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: The first actual complete-block saving is certified, but Y^(37/48) is still above the Y^(1/2) cluster target and yields no improved pointwise exponent. Continue only through the prescribed-centre truncated product-wave/UNBAL probe or a new joint signed inequality.

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
- Next action: On the direct route, prove the hard high-radical small-t residual and the independent smooth residual parent. On the alternative route, prove both global radial parents and GAR, then use only the separate total-M1 bridge. The Round-181 strict sectors and mechanism no-go close neither route.

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
- Next action: The first smooth profile D=floor(sqrt X)/2 with L asymp X^(1/6) has accepted menu capacity X^(1/3+o(1)), missing X^(1/12). Prove a new actual-symbol saving uniformly on all smooth U_1 labels, or one whole-U_1 theorem with an exact owner bridge.

### M9-M1-dual-restricted-convolution-RCS: Dual restricted-convolution estimate for M1 resonance cells

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Use the exact coefficient self-return to distinguish full terminal sectors from short moving strips; product completion alone supplies no signed estimate.

### M9-M1-global-angular-radial-estimate: Global angular radial estimate for the active M1 aggregate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Blockers: `M9-M1-global-lower-radial-signed-estimate`
- Next action: GAR remains open on the Round-122 low-two-adic survivor. The complementary-divisor gate is parked absent a genuinely joint signed inequality.

### M9-M1-global-lower-radial-signed-estimate: Exact lower-radial signed aggregate for global M1

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: The full D=d=L=1 paired-interior Abel package self-returns to the accepted common-profile hard defect wave; its raw M^(3/4) signed variable-mask estimate remains open beyond the fixed-polylogarithmic collar. Prove it plus D>1, L>1, generic t=1, every t>=2 layer, and the independent cross owner before global assembly.

### M9-M1-hard-top-high-radical-small-t-residual-estimate: Hard-M1 high-radical small-square-multiplier residual estimate

- Status: `open`
- Track: `M9_analytic`
- Historical steward: `Codex conductor` (non-binding)
- Next action: Rounds 187-197 accepted Fourier, lift, projective, signed-inverse, Farey, double-close, P2 absolute-capacity, and P2 common-cell sectors remain valid. Round 199 rules out only the specified cross-gcd cellular completion: the lawful P2 triangle has a nonzero constant-endpoint incidence, its unique fourth product corner is a P1 allocation, and partial-block moves generate physical-mask commutators. The exact P2 boundary/sign/gcd complement remains open. Do not retry assigned-sign, partial-block, deleted-corner, or fixed-packet variants of this mechanism. The next analytic round should either prove a genuinely non-cellular coefficient-sensitive joint outer estimate for the remaining P2 complement or freeze the disjoint P1 owner. Complete original t=1, every original t>=2 small-G incidence, the large-G near-resonant complement, smooth M1, GAR, every M2 parent, endpoint uniformity, M9 and both bridges remain open.

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
