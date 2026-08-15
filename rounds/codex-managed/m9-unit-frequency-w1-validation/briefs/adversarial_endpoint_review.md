# Task Brief: adversarial_endpoint_review

- Campaign: `m9-unit-frequency-w1-validation`
- Research round: `2` (`seam_validation`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `3c06ffad9c2847b329c57a8954d0758e443ee55be2da01c00ce5731bad3d6b5f`
- Generated: `2026-08-11T08:40:58.695560+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 90%.
- Numerical/experimental effort: at most 10%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Is the unit-frequency W-1 lower bound correct with all constants, hypotheses, exact-resonance subtraction, dyadic-weight transfer, and endpoint ranges explicit?

## Reference formula and distinctions

Candidate: assuming |beta_{1,H}|>=b_0 and Sigma_abs(N=0)<=C_epsilon D^2 X^epsilon, one has Sigma_abs(0<|N|<=M)>=c min(D^4,MD)-C_epsilon D^2 X^epsilon for 1<=M<<D^3. At M=D^4/X this gives cD^5/X-C_epsilon D^2X^epsilon and a power obstruction for D>=X^(1/3+delta).

- weight-blind nonzero tuple count
- absolute beta-weighted nonzero mass
- chi_4-removed unsigned mass
- full true signed mass, which is excluded from the claimed lower bound

## Assigned target

Try to break the candidate lower bound. Check window partition and pair multiplicity, exact N=0 subtraction, constants, D and M ranges, epsilon quantifiers, sharp/smooth weights, and scope across raw, absolute, chi-removed, and true signed quantities. Compare the blind and claimant arguments without voting.

## Permitted context

- `state/proof_obligations.yml`
- `state/control_models.md`
- `state/validation_matrix.yml`
- `rounds/codex-managed/m9-weighted-mass-adjudication/reports/blind_weighted_upper_bound.md`
- `rounds/codex-managed/m9-weighted-mass-adjudication/reports/hostile_lower_bound_audit.md`
- `rounds/codex-managed/m9-weighted-mass-adjudication/reports/conductor_independent_analysis.md`
- `rounds/codex-managed/m9-weighted-mass-adjudication/synthesis.md`

## Required controls

- `raw-vs-weighted`
- `signed-vs-unsigned`
- `dyadic-endpoints`
- `exact-vs-near-resonance`
- `support-and-degeneracy`

## Required deliverables

- seam-by-seam verdict
- strongest surviving statement
- counterexample attempts
- first doubtful step
- accept/revise/reject recommendation

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
