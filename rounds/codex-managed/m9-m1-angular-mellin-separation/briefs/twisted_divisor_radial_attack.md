# Task brief: twisted divisor radial attack

Campaign: `m9-m1-angular-mellin-separation`  
Round: 15  
Role: analytic functional-equation attacker

Read `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`, `state/best_proof_draft.md`,
`rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`, and
`sources/popov_2024_voronoi_gauss.md`. Do not read another Round-15 report.
Do not edit shared state.

Independently derive a usable Mellin-mode representation with coefficients

\[
\tau_{\chi_4,z}(n)=\sum_{hq=n,q\ {m odd}}\chi_4(q)h^{-z}.
\]

Attack the resulting square-root radial sums uniformly in the relevant
complex shift (z), scale (j), and contour height. You may derive a
functional equation/Voronoi formula directly or use a primary theorem after
auditing its hypotheses. Calculate conductor, gamma factors, dual length,
poles/residues, and endpoint/truncation errors. Test the full unresolved
parameter range, not a single favorable mode. Either prove a new
target-sized range/global component or a rigorous return-map/capacity
theorem. No numerical certification; bounded symbolic checks are allowed.

Write only
`rounds/codex-managed/m9-m1-angular-mellin-separation/reports/twisted_divisor_radial_attack.md`
using the full seven-part report contract.
