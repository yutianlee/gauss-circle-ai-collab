# Round 202 statement-only packet

Role: independent blind rederiver. Read this packet and protocol.md
only; do not read the graph, strategy, manifest, other reports, or
claimant derivations. Starting graph SHA-256 for provenance:
`682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c`.

Let r_2(n)=#{(u,v) in Z^2:u^2+v^2=n}. Fix real even Schwartz Psi
with Psi(0)=1, and a nonzero nonnegative w in C_c^infinity((0,infinity)).
Set a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)), T>=2, and
w-hat(xi)=integral w(u)exp(-2pi i u xi)du.

Prove or refute the following candidate, with exact hypotheses and
constants. There exist fixed 0<a<b and h,c>0 such that, for all
sufficiently large real T, the ordered balanced twelve-root sum

T sum_{aT<=n_j<=bT, 0<|Delta|<=h/T}
       product_j a_(n_j)(T) Re w-hat(-T Delta)

is at least c T^(5/2), where
Delta=sqrt(n_1)+...+sqrt(n_6)-sqrt(n_7)-...-sqrt(n_12).
All coefficients on the chosen band must be nonnegative. Do not omit
the requirement Delta!=0. The consequence to audit is that replacing
the full all-sign moment expansion term by term by its absolute value
cannot yield O(T^(1+2eta+epsilon)) when eta<3/4. The outside modulus of
the complete signed aggregate is a different object.

You may use the following already accepted statement without reading
its proof: for fixed k and b_n<=C tau(n)n^(-3/4), the full weighted
exact-resonance sum over signs and indices with sum epsilon_j sqrt(n_j)=0
is bounded uniformly in every cutoff. This supplies only Delta=0.
You may prove elementary circle-area counting by covering lattice
points with unit squares. No global exponent theorem is needed.

Controls: finite versus infinite sums, floor/real T endpoints, support
and positivity of Psi and Re w-hat, ordered multiplicities, removal
of exact resonances, and the distinction between a positive spectral
subsum and the total signed displaced moment. If useful, state the
general balanced 2k power and check low orders against known moment
possibility without importing a new theorem. No numerical experiments.

Write only
rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/blind_physical_near_resonance_mass.md
with the seven required sections; stop after the assigned report.
