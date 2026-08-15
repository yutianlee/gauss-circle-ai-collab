# Task brief: M1 terminal arithmetic attack

Campaign: `m9-m1-frequency-phase-diagram`  
Round: 10  
Role: analytic mechanism attacker

Read:

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-generic-band-signed-correlation/reports/top_block_two_shift_attack.md`
- `rounds/codex-managed/m9-combined-top-cones/synthesis.md`
- `rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_hostile_audit.md`

Do not read another Round-10 report. Do not edit shared state.

## Assigned target

Attack the terminal M1 frequency range \(L\asymp H_D=DX^{-1/4}\), including
the hard endpoint \(D\asymp X^{1/2}\). Work in whichever exact coordinate is
strongest:

\[
\sum_{h\asymp L}\frac{\Phi(h/(H_D+1))}{h}
\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
\]

the two additive quarter shifts for \(\chi_4(d)\), or the accepted top M1
product-phase cone. Seek a divisor regrouping, two-shift kernel, parity
projection, large-sieve estimate, or an exact obstruction. Keep the actual
profile and Vaaler weight until the final inequality.

Required controls: endpoint jump; shifted residues \(1,3\pmod4\); both
frequency signs; exact-square resonances; arbitrary-weight proves-too-much
test; boundary/error terms; and comparison with the target
\(X^{1/4+\varepsilon}\). At most a small symbolic or finite falsification
check may be used; it remains diagnostic only.

## Report contract

Write only
`rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`.
Include: Result; exact statement/hypotheses; proof; first doubtful or unproved
step; controls and outcomes; exact dependencies; recommended state effect.
A rigorous obstruction is a successful result.
