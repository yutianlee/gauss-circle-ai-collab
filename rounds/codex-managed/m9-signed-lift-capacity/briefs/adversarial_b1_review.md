# Task Brief: adversarial_b1_review

- Campaign: `m9-signed-lift-capacity`
- Research round: `3` (`mechanism_capacity`)
- Role: `seam_reviewer`
- Access mode: `selected_context`
- Graph SHA-256: `feaeb32971492ea8f0adb245a996f4deb3085ab4e63749da98b5d2b2903f157d`
- Generated: `2026-08-11T09:02:10.123211+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 90%.
- Numerical/experimental effort: at most 10%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Is the signed lift envelope A_chi(p/q)<<q/(D|p|) correct with exact support and weight hypotheses, and can that pointwise envelope alone control the signed M2 fat-band energy?

## Reference formula and distinctions

For reduced p/q, A_chi(p/q)=sum_{gq in [D,2D), 1<=|gp|<=H_D} beta_{gp,H_D} w_D(gq), with beta_{h,H}=-Phi(|h|/(H+1))chi_4(|h|)1_{2 not divides h}/(pi|h|). The candidate B1 estimate is A_chi=0 for even p and |A_chi(p/q)|<<q/(D|p|) for odd p under a fixed smooth or bounded-variation dyadic profile.

- individual signed reduced-fraction lift weight A_chi(p/q)
- l1 and l2 capacity implied by the B1 envelope
- signed off-diagonal global fourth-moment fat-band form
- absolute or adversarial envelope analogues
- pointwise S_2(D;X), explicitly excluded from any moment-only conclusion

## Assigned target

Attack both B1 and its proposed energy use. Test arbitrary bounded weights, sharp cutoffs, fixed smooth profiles, BV weights, short truncation intervals, p/q boundary cases, D=X^(1/3), X^(3/8), X^(1/2), and unsigned/adversarial coefficient controls. Identify the weakest surviving statement.

## Permitted context

- `sources/vaaler_1985.md`
- `state/proof_obligations.yml`
- `state/control_models.md`
- `state/best_proof_draft.md`
- `rounds/obligation-main/round_008/responses/A4-008.md`
- `rounds/obligation-main/round_008/reviews/A1.md`
- `rounds/codex-managed/m9-unit-frequency-w1-validation/synthesis.md`

## Required controls

- `signed-vs-unsigned`
- `coefficient-adversary`
- `support-and-degeneracy`
- `proves-too-much`

## Required deliverables

- seam-by-seam verdict
- counterexamples
- strongest surviving B1 statement
- energy-use verdict
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
