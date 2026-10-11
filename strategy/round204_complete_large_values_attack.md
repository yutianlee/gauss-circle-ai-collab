# Round 204: complete actual large-value distribution

Date: 2026-09-23. Round203 is closed with an identity State Patch.
Previous goal turn classification: progress. It completed two bounded
analytic attempts and independent controls, establishing that their
full remainders retain the open target and changing the next action
to an actual distribution estimate. It proved no improved exponent.

## Frozen objective

For the same actual tail
\[
 B_T(R)=\sum_{n>\lfloor T^{1/2047}\rfloor}
 r_2(n)n^{-3/4}\Psi(\sqrt{n/T})\cos(2\pi R\sqrt n-3\pi/4),
\]
and fixed nonnegative displaced window w=chi^2, attack
\[
 D_T(V):=\int w(R/T)1_{|B_T(R)|>V}\,dR
 \ll_\epsilon T^{29/25+\epsilon}V^{-12},
 \quad T^{54/775}\le V\le T^{\beta+\epsilon},
 \quad\beta=2\theta_{LY}-1/2.
\]
This is the complete high-value estimate needed by the twelfth-moment
route. Low values are covered by the inherited q0=262/27 benchmark.
The milestone would give102/325 only; the full goal remains one quarter.

## Concrete mechanism and subinterfaces

Use a finite sample duality/Gram argument for actual dyadic square-root
sums, followed by exact level-set covering and full-tail recombination.
Derive a distribution inequality, not only the layer-cake equivalence.
Keep the diagonal contribution and the ceiling in the number of local
intervals, including when the chosen interval is longer than T.

One candidate estimate to prove or refute is
\[
 D_T(V)\ll_\epsilon T^\epsilon
       (V^{-2}+T V^{-136/13}),\qquad V\ge1.
\]
It is not the frozen target and is not assumed. Its proposed source
is the already graph-accepted global Bourgain2017 exponent-pair
interface, after a fresh square-root phase audit, together with the
elementary second-derivative bound. Their geometric interpolation
formally suggests the unweighted correlation bound
\[
 |\sum_{N<n\le2N}e(u\sqrt n)|
 \ll T^\epsilon\sqrt N(|u|^{13/55}+|u|^{-1}).
\]
All small-u, intermediate and source-valid large-u regimes must be
proved. The resulting Gram estimate must retain the complete V^-2
term. Any stronger coefficient-sensitive step must account for the
actual r2 weights instead of being asserted from this generic bound.

The source task also audits the original large-values trail and
whether the printed q0 is fixed by an older supremum exponent.
No endpoint is enlarged by substitution alone. A proved complete
distribution bound may justify a better moment estimate even if it
does not improve the pointwise exponent; distinguish those outcomes.

## Bounded tasks and controls

1. Actual distribution derivation, including covering, coefficients,
   all dyadic blocks and infinite upper tail; then confront the target.
2. Primary source and square-root hypothesis audit, including exact
   admissibility, source ranges and the original moment endpoint trail.
3. Statement-only independent Gram/covering derivation and an aligned
   coefficient control. It receives no source, graph or claimant proof.

Conductor work independently derives the correlation interpolation,
the diagonal and local-interval terms, and all moment exponents.
Resource budget: three bounded reports and one seam-review/repair
cycle;100 percent analytical/source reasoning, no numerical experiments.

Exit only after reports, statement-only control, exact-hash independent
seams and mechanically valid State Patch. Promote a complete proved
inequality only; retain source/interface qualifications and all open
parents. No generic coefficient counterexample refutes actual r2.
The mandatory broad strategy/current-literature review is Round205,
after this round closes. Do not start it inside Round204.
