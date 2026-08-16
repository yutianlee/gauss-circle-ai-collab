# Task Brief: blind_cross_group_tensor_rederivation

- Campaign: `m9-m1-cross-group-period-depth-dispersion`
- Research round: `88` (`m9_m1_cross_group_period_depth_dispersion`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `e2346245d09d22ba66e17037ad57e85cf56808d9ca70526657f78d94e52809be`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%; computation is diagnostic only.
- Do not browse or read any source, graph, strategy, prior report, review, or sibling Round-88 report.

## Frozen question

Can the exact cross-group deep \(M9\!-\!M1\) Fejer off-diagonal be bounded target-safely after separating partial-period lower-conductor returns from genuinely aperiodic local traces?

## Reference formula and distinctions

Derive from the packet whether

\[
 \mathcal G_{\rm cross}(D)
 \ll_\varepsilon X^\varepsilon {D\over B}J^{14/5},
\]

or isolate an exact target-safe nonempty component and the first smaller signed survivor.

- Keep normalized rows \(M^{-1}\sum_n I_b(n)e_M(nx)e(n\theta)\); their product already contains \(M^{-2}\).
- Keep \(U=D\), the Fejer weights, \(Q^{-5/12}\), and the global \(u=0\) diagonal exactly once.
- Round 87 already owns every same-group full-prime-power package.
- The task is cross-group \(u\ne0\) only.

## Assigned target

Independently derive the cross-group tensor/period-depth structure and decide whether a target-safe signed estimate follows from the packet.

## Permitted context

- `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/derivation_packet.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- all strategy files
- all prior-round reports and reviews
- all sibling Round-88 reports
- all source cards and web sources

## Required controls

- external normalization; full-factor ownership; global diagonal one-count;
- \(U=D\), physical \(Q^{-5/12}\), full prime-power period depth, bad primes and full \(2\)-part;
- actual fourfold symbol, aperiodic trace operator, negative and modulus-multiple differences;
- Ramanujan terms, deep support/errors, perfect powers, transform self-return, downstream scope.

## Required deliverable

Write only `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reports/blind_cross_group_tensor_rederivation.md`.

## Report contract

Use exactly seven top-level numbered sections:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control tests and outcomes.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

A rigorous no-go is successful evidence. Stop after the report; do not design a later round.
