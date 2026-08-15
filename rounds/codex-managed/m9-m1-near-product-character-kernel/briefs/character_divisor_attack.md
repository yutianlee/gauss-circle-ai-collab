# Task brief: character-divisor arithmetic attack

Campaign: `m9-m1-near-product-character-kernel`  
Round: 11  
Role: arithmetic mechanism attacker

Read:

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`
- `sources/method_strategy_review_2026-08-11.md`

Do not read another Round-11 report. Do not edit shared state.

## Assigned target

Attack the signed coefficient left by grouping near products \(n=dm\):
truncated sums of \(\chi_4(d)w_D(d)\) over divisors \(d\asymp D\), coupled
to the actual kernel at \((X-n)/d\). Seek exact factorization through the
sum-of-two-squares function, multiplicativity, complementary divisors,
Dirichlet series, short-interval mean square, large sieve, or a new divisor
pairing. The target is a pointwise estimate strong enough on a nonempty
subset of \(\mathcal U_1\), especially the hard-top middle frequencies.

Required controls: \(X\) integer/noninteger, exact squares, prime and highly
composite products, dyadic truncation, real fixed profile versus arbitrary
bounded weights, and both frequency signs. At most 10% bounded computation
may be used for falsification only.

Write only
`rounds/codex-managed/m9-m1-near-product-character-kernel/reports/character_divisor_attack.md`.
Include the full seven-part report contract. A sharp no-go theorem is a
successful result.
