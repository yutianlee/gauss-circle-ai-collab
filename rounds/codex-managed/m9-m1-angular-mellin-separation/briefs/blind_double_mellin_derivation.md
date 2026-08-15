# Task brief: blind double-Mellin derivation

Campaign: `m9-m1-angular-mellin-separation`  
Round: 15  
Role: statement-only exact deriver

Read only `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`,
`rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`,
and `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`.
Do not read another Round-15 report. Do not edit shared state.

For each actual denominator scale (j), Mellin-invert both

\[
w_j(2h\sqrt{X/n})
\quad\hbox{and}\quad
\mathbf1_{h\le H_j}\Phi(h/(H_j+1)).
\]

Derive the exact double-contour representation, including all scale powers,
the product cutoff, odd (q), endpoint stars, and the floor
(H_j=\lfloor D_jX^{-1/4}\rfloor). Prove the arithmetic identity

\[
\sum_n\tau_{\chi_4,z}(n)n^{-s}
=\zeta(s+z)L(s,\chi_4)
\]

in its correct half-plane for your Mellin convention. State contour decay
and justify every interchange. Treat the one-sided hard top separately and
quantify the loss caused by its jump. Determine the smallest exact
twisted-radial estimate that would imply GAR. No web and no numerics.

Write only
`rounds/codex-managed/m9-m1-angular-mellin-separation/reports/blind_double_mellin_derivation.md`
using the full seven-part report contract.
