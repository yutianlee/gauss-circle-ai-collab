# Task brief: dyadic r2 recombination attack

Campaign: `m9-m1-dual-r2-recombination`  
Round: 14  
Role: global algebraic attacker

Read `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`,
`rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/reports/ordered_cell_cancellation_attack.md`,
`rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`,
`state/best_proof_draft.md`, and `state/control_models.md`.
Do not read another Round-14 report. Do not edit shared state.

Carry out the full global recombination of RCS over $L$ and $D$. Start with
$n=hq$ and exploit the exact power cancellation. Determine the resulting
restricted divisor coefficient and its relation to
$\sum_{q\mid n}\chi_4(q)=r_2(n)/4$. Use the explicit telescoping dyadic
profile and the actual $H_D=\lfloor DX^{-1/4}\rfloor$; quantify every floor,
frequency partition, hard-top, and transform-error term. Test whether
$\Phi(u)+\Phi(1-u)=1$ or a complementary angular sector yields an exact
completion. If a global $n$-sum emerges, prove precisely how a bound for it
feeds the original M1 contribution without requiring each block separately.
If it is only the classical radial sum in disguise, prove that return map
and isolate any leftover asymmetric sector. Use at most one bounded exact
computation, solely to falsify a concrete finite coefficient identity.

Write only
`rounds/codex-managed/m9-m1-dual-r2-recombination/reports/dyadic_r2_recombination_attack.md`
with the full seven-part report contract.
