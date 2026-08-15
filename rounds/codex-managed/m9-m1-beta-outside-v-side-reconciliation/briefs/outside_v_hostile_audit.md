# Task Brief: outside_v_hostile_audit

- Campaign: `m9-m1-beta-outside-v-side-reconciliation`
- Research round: `29` (`beta_outside_v_side_reconciliation`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `2a5a8ac3d40fc39cef58d677ee339ec474c3eb88ca1f4ab5755fec6b73c67a0c`
- Generated: `2026-08-12T22:58:10.342742+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the exact oriented sum of the finite v-vertical, its two outside-v sides, and the v=0/u=0/corner ledger cancel the logarithmic moving hard-top edge uniformly in L=alpha-beta, and does the resulting amplitude satisfy the scaled C^2 bounds required by the accepted two-saddle Fresnel lemma?

## Reference formula and distinctions

At finite height C_(a,V)(L)=int_(-V)^V H_b(nu)/(a+i(L-nu))dnu has C_(a,V)(V)=-iH_b(V)log(1/a)+O(1). Start from the exact finite vector contour rule: moving the v-line retains the upper left-to-right side minus the lower left-to-right side, plus the v=0 residue and the u=0/v=0 corner when crossed. Keep the omega-recombined radial factor and take no whole-line PV limit before deriving this oriented identity.

- finite v-vertical with moving pole
- upper and lower oriented outside-v sides
- v=0 height residue
- u=0 top residue and joint corner
- omega-recombined G/E1/R1 factor
- logarithmic edge coefficient and sign
- uniform L and alpha derivatives
- nested U,V,S exhaustion
- scaled C^2 Fresnel amplitude or exact obstruction

## Assigned target

Hostilely audit side orientation, moving-pole endpoint convention, Plemelj signs, axial/top/corner double counting, omega recombination, order of limits, and uniform derivatives. Construct an actual-profile falsifier or certify the narrowest exact reconciliation.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/reports/blind_finite_vector_kernel.md`
- `rounds/codex-managed/m9-m1-partial-functional-equation-transitions/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-uniform-stationary-patching/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-uniform-stationary-patching/reports/transition_patching_hostile_audit.md`

## Required controls

- `signed-vs-unsigned`
- `support-and-degeneracy`
- `residue-and-normalization`
- `endpoint-uniformity`
- `order-of-limits`
- `coefficient-adversary`

## Required deliverables

- Independent sign/residue/order audit
- Counterexample or scoped certification
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
