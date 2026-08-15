# Task Brief: h4_weight_normalization_review

- Campaign: `m9-unit-frequency-w1-validation`
- Research round: `2` (`seam_validation`)
- Role: `source_auditor`
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

Locate and audit the primary Vaaler 1985 source for the exact coefficient Phi, sawtooth convention, odd-frequency beta algebra, positivity on u in (0,1/2], and a uniform beta_1 lower envelope. Separately determine the weakest dyadic-weight hypothesis that transfers the sharp-block lower bound to the actual M2 block.

## Permitted context

- `sources/vaaler_1985.md`
- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `Gauss circle problem.tex`
- `rounds/codex-managed/m9-weighted-mass-adjudication/reports/conductor_independent_analysis.md`

## Required controls

- `support-and-degeneracy`
- `coefficient-adversary`
- `raw-vs-weighted`

## Required deliverables

- primary-source bibliography and links
- exact theorem/equation transcription within quotation limits
- notation map
- beta_1 proof or blocker
- dyadic-weight transfer lemma
- source-card recommendation

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
