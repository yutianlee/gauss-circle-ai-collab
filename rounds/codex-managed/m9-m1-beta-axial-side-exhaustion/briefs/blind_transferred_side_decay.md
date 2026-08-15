# Task Brief: blind_transferred_side_decay

- Campaign: `m9-m1-beta-axial-side-exhaustion`
- Research round: `35` (`beta_axial_side_exhaustion_commutation`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `c3528645fda6be30f7a1411c200c96d05d3a9445d2da24fa3f162b60c9d619d1`
- Generated: `2026-08-13T01:26:07.419472+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does arbitrary-order endpoint subtraction make every one of the sixteen beta two-axis transfer images of the renormalized radial sides vanish under the already accepted nested S=S(X,U,V) exhaustion?

## Reference formula and distinctions

Use the fixed even mask psi in C_c^infinity(R), psi=1 on [-B0,B0] and supp psi subset [-2B0,2B0]. Let S_rad^(M)(U,V,S) be the upper-minus-lower radial-side functional with R_(M,v), and let X_uv be the proved finite sixteen-stratum transfer. First test the exact support separation |beta|>=S-(U+V)/2 on the reflected radial sides. If that does not close every stratum, prove lim_nested X_uv S_rad^(M)=0 for a single explicit sufficiently large M and polynomial nesting S(X,U,V), uniformly with all actual profiles, floors, stars, axial/artificial collisions, psi'/psi'' connectors, and the external normalization; or isolate one exact transferred stratum whose S-capacity cannot be removed. Do not address the endpoint/arithmetic physical-module commutator or a terminal-symbol estimate.

- arbitrary-order R_(M,v) value and u/v derivative bounds on s=lambda+/-iS
- upper-minus-lower radial-side orientation
- four pure face products
- pure u=0 and v=0 side residues and the joint corner
- connector boundary and connector-axis residues
- mixed psi''(beta)/4 product-area term
- actual W_j, phi, D_j, H_j, h,q,m, chi_4, floors, and stars
- artificial/axial collision residues under common ownership
- degree-two left-edge capacity and outside Mellin norms
- one explicit M and nested growth law S=S(X,U,V)

## Assigned target

From the frozen statement and permitted endpoint-subtraction/finite-transfer syntheses, independently derive sufficient value, derivative, and residue bounds for R_(M,v) on s=lambda+/-iS. Build a sixteen-stratum S-power table and decide whether one M and polynomial nesting remove every transferred side image. If definitions are insufficient, identify the first exact missing bound. Do not read Round-35 claimant reports.

## Permitted context

- `protocol.md`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-radial-endpoint-renormalization/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/synthesis.md`

## Excluded context

- `all Round-35 claimant reports`
- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/reports`

## Required controls

- `arbitrary_M_radial_remainder_decay`
- `u_v_derivative_and_residue_cost`
- `sixteen_stratum_power_table`
- `nested_exhaustion_uniformity`
- `collision_and_corner_scope`
- `no_physical_module_overreach`

## Required deliverables

- Independent transferred-side decay lemma or first missing coefficient
- Complete sixteen-stratum S-power table and explicit nesting condition
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
