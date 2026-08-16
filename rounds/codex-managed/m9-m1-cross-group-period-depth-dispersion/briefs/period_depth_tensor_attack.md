# Task Brief: period_depth_tensor_attack

- Campaign: `m9-m1-cross-group-period-depth-dispersion`
- Research round: `88` (`m9_m1_cross_group_period_depth_dispersion`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `e2346245d09d22ba66e17037ad57e85cf56808d9ca70526657f78d94e52809be`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation

- Analytical/algebraic effort: at least 80%.
- Numerical/experimental effort: at most 20%; computation is diagnostic only.
- Read every permitted file completely before acting. Do not read sibling Round-88 reports.

## Frozen question

Can the exact cross-group deep \(M9\!-\!M1\) Fejer off-diagonal be bounded target-safely after separating partial-period lower-conductor returns from genuinely aperiodic local traces?

## Reference formula and distinctions

Build an exact full-prime-power and \(2\)-adic period-depth decomposition for

\[
 \mathcal G_{\rm cross}(D)
 =\sum_{b\asymp B}\int |D_D(\theta)|^2
 \sum_{(S,\alpha)\ne(S',\alpha'),\,u\ne0}
 H_{b,S,\alpha}\overline{H_{b,S',\alpha']}
\]

and prove the target \(X^\varepsilon(D/B)J^{14/5}\), or a nonempty target-safe subaggregate with an exact smaller survivor.

- Never insert a second \(M^{-2}\).
- Preserve \(U=D\), \(Q^{-5/12}\), global \(u=0\) ownership, and the Round-87 same-group deletion.
- Any period reduction must retain the unit-domain indicator, bad primes, nonunit \(K\), and the full \(2\)-part.

## Assigned target

Construct the exact period-depth/tensor routing, estimate partial-period and aperiodic pieces against the actual fourfold stationary symbol, and identify the first unproved inequality.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0816_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/derivation_packet.md`
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/synthesis.md`
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/aligned_mode_aggregate_attack.md`
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_normalization.md`
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_crt_fejer.md`

## Excluded context

- all sibling Round-88 reports

## Required controls

- external normalization; full-factor ownership; global diagonal one-count;
- \(U=D\), physical \(Q^{-5/12}\), partial-period depth, bad primes and full \(2\)-part;
- actual fourfold symbol, aperiodic trace operator, negative and modulus-multiple differences;
- Ramanujan terms, deep support/errors, perfect powers, transform self-return, downstream scope.

## Required deliverable

Write only `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reports/period_depth_tensor_attack.md`.

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
