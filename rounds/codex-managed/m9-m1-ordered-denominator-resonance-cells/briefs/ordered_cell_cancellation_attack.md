# Task brief: ordered resonance-cell cancellation attack

Campaign: `m9-m1-ordered-denominator-resonance-cells`  
Round: 13  
Role: analytic mechanism attacker

Read `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`,
`rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`,
`rounds/codex-managed/m9-m1-near-product-character-kernel/reports/near_product_hostile_audit.md`,
`rounds/codex-managed/m9-m1-cross-product-offset-pairing/synthesis.md`, and
`rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`.
Do not read another Round-13 report. Do not edit shared state.

Attack the exact actual-profile ordered denominator sum. For odd \(d\),
absorb \(\chi_4(d)\) into

\[
g_h(d)=hX/d+d/4,
\qquad
g_h(d+2)-g_h(d)=1/2-2hX/(d(d+2)).
\]

Develop the strongest rigorous resonant/nonresonant decomposition available:
two-term pairing, discrete Abel, Kusmin--Landau, local quadratic cells, a
second differencing step, or a signed average across \(h\). Keep the actual
Vaaler coefficient and spatial profile. Sum all cell costs, including
frequency and denominator boundaries, and compare with
\(X^{1/4+\varepsilon}\) throughout \(\mathcal U_1\). If closure fails,
state the smallest exact residual resonance-cell estimate and prove a sharp
capacity obstruction for the simpler variants. Treat the hard endpoint and
exact-square cancellation family. Use no more than one bounded symbolic or
numerical falsification check, and only if it decides a concrete identity.

Write only
`rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/reports/ordered_cell_cancellation_attack.md`
with the full seven-part report contract.
