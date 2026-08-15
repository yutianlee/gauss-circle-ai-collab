# Task Brief: mask_endpoint_axial_attack

- Campaign: `m9-m1-beta-mask-endpoint-axial-compatibility`
- Research round: `33` (`beta_mask_endpoint_axial_compatibility`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `62d2197f75b5d0ca1a8c2c320573c678328e8d36bbdad8dba5c997d0c97a2d29`
- Generated: `2026-08-13T00:28:46.591198+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

For the hierarchical beta mask at finite U,V,S, does endpoint collapse followed by finite v-axis displacement give exactly the same boundary, arithmetic, axial, connector, and corner ownership as performing those operations before masking, so that the residual terminal share has E_own=0?

## Reference formula and distinctions

Write one mask-by-mask identity for the beta terminal vertical plus its Cauchy--Green area connector. It must route T_xi+S_xi+P_xi=D_xi-A_xi, the cancelling artificial R1 residue, the recombined R1 arithmetic residue, the v=0 vector residue on every contour stratum, the u=0 share, the joint corner, and both finite height connectors exactly once. Prove E_own=H_G-H_E1-H_R1=0 for the endpoint-free residual, or isolate the first explicit nonzero masked boundary operator. No terminal symbol estimate is part of this round.

- hierarchical mask Theta_beta=psi(beta) and its one-edge Cauchy--Green connector
- finite endpoint identity T_xi+S_xi+P_xi=D_xi-A_xi
- G=E1+R1 artificial-pole cancellation under the same mask
- full versus masked A=0 arithmetic residue share
- terminal, radial-side, and arithmetic v=0 vector residues
- u=0 axial share and joint u=v=0 corner
- finite v-horizontal connectors and orientations
- endpoint stars, profiles, floors, and external X^(1/4) normalization
- rho ownership defect E_own and its physical L derivative

## Assigned target

Construct the exact commuting diagram between hierarchical beta masking, Cauchy--Green displacement, M=1 endpoint collapse, and finite v-axis displacement. Recombine complementary mask and connector shares before invoking proved unmasked endpoint/arithmetic modules. Prove E_own=0 for the side-collapsed endpoint-free terminal operator, or write the smallest explicit masked boundary/axial survivor including its normalization and dependencies.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md`
- `rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-transition-connector/reports/blind_beta_connector_identity.md`
- `rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md`
- `rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/reviews/conductor_endpoint_ownership_map.md`
- `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/reviews/conductor_axial_vector_ownership.md`
- `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/synthesis.md`

## Required controls

- `hierarchical-versus-disjoint-mask`
- `cauchy-green-orientation`
- `endpoint-artificial-arithmetic-ledger`
- `axial-residue-and-corner-count`
- `finite-height-connector-ownership`
- `rho-ownership-defect`
- `profile-star-normalization`

## Required deliverables

- Exact commuting identity or smallest explicit survivor
- Mask, endpoint, axial, connector, corner, and normalization ledger
- Seven-section report at the assigned path

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
