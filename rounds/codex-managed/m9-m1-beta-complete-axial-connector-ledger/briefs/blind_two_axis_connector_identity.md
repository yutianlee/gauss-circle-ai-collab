# Task Brief: blind_two_axis_connector_identity

- Campaign: `m9-m1-beta-complete-axial-connector-ledger`
- Research round: `34` (`beta_complete_axial_connector_ledger`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `09d4a1cb1664719cb8df255f371d496b5bbcb112f5611d63c742055bf495f193`
- Generated: `2026-08-13T00:53:06.119398+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

After global endpoint collapse but before any local polar subtraction, can the actual finite endpoint-free beta operator be expanded under both u- and v-axis shifts with every face, area connector, connector-axis residue, mixed psi''/4 stratum, and joint corner assigned exactly once and independently of shift order?

## Reference formula and distinctions

For the actual endpoint-free finite kernel Q_beta=psi(beta)Q on the terminal, renormalized-side, and residual arithmetic strata, define the v-transfer by H_(v,+)-H_(v,-)+2pi i Res_(v=0)(psi(beta)Q)+(1/2)intint psi'(beta)Q, and analogously in u. Expand X_u X_v Q_beta and X_v X_u Q_beta completely. Include the u-shift of v-horizontals, v=0 residue, and v-area connector, hence connector boundaries, connector-axis residues, mixed +(1/4)intintintint psi''(beta)Q, and the joint corner once. Prove the two expansions agree or isolate the first explicit mismatch. No size estimate is included.

- actual endpoint-free terminal R1 vector integrand
- renormalized radial-side and residual arithmetic strata before licensed limits
- finite u- and v-horizontal faces with orientations
- filtered u=0 and v=0 vector residues
- u and v mask-area connectors
- connector-axis residues and connector boundary faces
- mixed derivative partial_mu partial_nu Theta_beta=psi''(beta)/4
- joint u=v=0 corner under one fixed convention
- artificial-pole, collision, profile, floor, star, and X^(1/4) ledger
- equivalence of u-then-v and v-then-u expansions

## Assigned target

Independently derive the finite two-axis Cauchy--Green formula for a separately meromorphic Q(u,v) multiplied by Theta=psi(t-(mu+nu)/2). Expand v then u and u then v, including all horizontal faces, area connectors, connector-axis residues, mixed psi''/4 term, and one joint corner. Fix one residue convention and prove equality or isolate the first sign mismatch. Then state exactly how the abstract identity acts stratumwise on an endpoint-free vector kernel. Do not read Round-34 claimant reports.

## Permitted context

- `protocol.md`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/synthesis.md`

## Excluded context

- `all Round-34 claimant reports`
- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/reviews`

## Required controls

- `one-axis-orientation-and-area-sign`
- `two-axis-mixed-derivative-sign`
- `connector-axis-and-boundary-strata`
- `corner-inclusion-exclusion`
- `shift-order-commutation`

## Required deliverables

- Complete abstract two-axis finite identity or first mismatch
- Term-by-term order-reversal and corner ledger
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
