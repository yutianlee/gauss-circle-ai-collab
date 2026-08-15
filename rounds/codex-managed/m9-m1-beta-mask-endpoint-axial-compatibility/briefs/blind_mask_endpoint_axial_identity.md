# Task Brief: blind_mask_endpoint_axial_identity

- Campaign: `m9-m1-beta-mask-endpoint-axial-compatibility`
- Research round: `33` (`beta_mask_endpoint_axial_compatibility`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
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

Independently derive the finite mask-by-mask compatibility identity for the hierarchical beta mask Theta_beta=psi(beta). Start from the accepted finite vector kernel, endpoint Cauchy identity, and one-edge Cauchy--Green formula. List terminal, radial-side, arithmetic, v=0, u=0, joint-corner, and finite-height connector shares with signs. Decide whether the endpoint-free residual has E_own=0; if the permitted statements do not define a needed share, isolate the first exact missing coefficient. Do not read any Round-33 claimant report.

## Permitted context

- `protocol.md`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md`
- `rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/synthesis.md`

## Excluded context

- `all Round-33 claimant reports`
- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/reviews`

## Required controls

- `hierarchical-versus-disjoint-mask`
- `cauchy-green-orientation`
- `endpoint-artificial-arithmetic-ledger`
- `axial-residue-and-corner-count`
- `rho-ownership-defect`

## Required deliverables

- Exact finite compatibility identity or first definition obstruction
- Complete orientation and one-count residue ledger
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
