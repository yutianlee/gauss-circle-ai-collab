# Task brief: endpoint tail and arithmetic symmetry attack

Campaign: `m9-top-endpoint-transform`  
Task: `endpoint_tail_symmetry_attack`  
Role: arithmetic structure attacker  
Graph SHA-256: `7b5a7c93190fa88305d91bb1f2e64788921fe2f4cbbd02eddb8e60e654d64d58`

Read `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`,
H1--H3 in `state/best_proof_draft.md`, the Round-7 profile report, and the
Round-5 smooth transform. Do not edit shared state. Write only
`rounds/codex-managed/m9-top-endpoint-transform/reports/endpoint_tail_symmetry_attack.md`.

## Objective

Attack the hard top profile by extending \(W(d/y)\) smoothly past \(y\)
and analyzing the tail \(y<d\ll y\), or by using the balanced hyperbola
symmetry before Fourier expansion. Seek an exact pairing, correction, or
cone parametrization that makes the endpoint boundary target-sized.

In transformed coordinates inspect the expected lattice condition
\(4k>h\) and the odd integers \(j=4k-h\). Check the exact relation between
\(\chi_4(h)\) and \(\chi_4(j)\), whether \((h,j)\)-symmetry produces real
cancellation, and whether any claimed pairing preserves phase and actual
amplitude. A clean no-go theorem is acceptable.

Do not use an extension beyond \(d\le\sqrt X\) unless the correction is
proved. Do not conflate a transformed cone with a saving. Check both M2
shifts, full real frequencies, and any interaction with M1 or the H1
hyperbola overlap.

The report must contain result, exact statement, proof/derivation, first
unproved step, controls, dependencies, and recommended state effect.
