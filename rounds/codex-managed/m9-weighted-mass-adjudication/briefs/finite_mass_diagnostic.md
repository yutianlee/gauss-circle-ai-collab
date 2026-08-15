# Task Brief: finite_mass_diagnostic

- Campaign: `m9-weighted-mass-adjudication`
- Research round: `1` (`discovery_and_adjudication`)
- Role: `numerical_falsifier`
- Access mode: `selected_context`
- Graph SHA-256: `3c06ffad9c2847b329c57a8954d0758e443ee55be2da01c00ce5731bad3d6b5f`
- Generated: `2026-08-11T08:33:32.357283+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Which Round 9 conclusions apply to a weight-blind tuple count, which apply to the actual absolute beta-weighted mass, and which require the signed chi_4 structure?

## Reference formula and distinctions

For S_2(D;X)=sum_{1<=|h|<=H_D} beta_{h,H_D} sum_{d~D} w_D(d)e(hX/(4d)), beta_{h,H}=-Phi(|h|/(H+1)) chi_4(h) 1_{2 not divides h}/(pi h), and N=h_1d_2d_3d_4-h_2d_1d_3d_4+h_3d_1d_2d_4-h_4d_1d_2d_3, keep the raw count, absolute coefficient-weighted mass, true signed mass, and unsigned mass distinct.

- weight-blind count of tuples in a specified nonzero N-band
- sum of |beta_{h_1} beta_{h_2} beta_{h_3} beta_{h_4}| over that band
- sum of beta_{h_1} beta_{h_2} beta_{h_3} beta_{h_4} over that band
- the comparison obtained after removing chi_4 signs

## Assigned target

Implement exact finite comparisons of raw count, 1/|h|-weighted absolute mass, true beta-signed mass, and unsigned beta mass across representative dyadic scales, including the X^(1/2) endpoint. Seek falsification and normalization mistakes, not asymptotic confirmation.

## Permitted context

- `state/best_proof_draft.md`
- `state/proof_obligations.yml`
- `state/control_models.md`
- `rounds/obligation-main/round_003/artifacts/m9_regression`

## Required controls

- `raw-vs-weighted`
- `signed-vs-unsigned`
- `dyadic-endpoints`
- `real-vs-complex-pairing`

## Required deliverables

- script
- command
- parameter table
- machine-readable results
- precision or exact-arithmetic log
- pass/fail rules
- limitations
- report

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
