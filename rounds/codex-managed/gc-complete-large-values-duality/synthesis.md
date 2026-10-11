# Round 204 synthesis: complete large values and moment gain

Campaign: `gc-complete-large-values-duality`. Closed by the conductor
on 2026-09-26, subject to the accompanying successful closure validation.
Starting graph SHA256:
`abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`.
Final proof kernel SHA256:
`942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.
Terminal label: `complete_distribution_gain_target_open`.

## Complete result

The full actual smoothed square-root series, including any hard lower
cutoff U>=0, satisfies

\[
D_{T,U}(V)\ll_\epsilon T^\epsilon
\left(V^{-2}+TV^{-136/13}\right),\qquad V\ge1.
\]

The bound includes all r2 coefficients, the singleton n=1, partial
dyadic blocks and the entire infinite upper tail. The source theorem
is applied to an unweighted correlation kernel in its exact derivative
class; the physical coefficients remain in the finite Gram argument.
Every diagonal, local interval and real level-set cover is retained.

For the fixed radial mollifier, let theta=theta_LY and beta=2theta-1/2.
Sharp reconstruction and the accepted pointwise bound give, for every
fixed p>=2,

\[
\int_{Y/2}^{3Y}|P(x)|^pdx
\ll_{p,\epsilon}Y^{1+p/4+\epsilon}
 +Y^{1+(p-2)\theta+\epsilon}.
\]

At p=12 the exponent is1+10theta=4.1448317597..., improving the
project's previously recorded comparison exponent4.148072478... .
The conjectural-order moment endpoint is now2+1/beta>262/27.
No literature novelty is asserted. This is a complete moment result,
not an exponent claim obtained from an omitted remainder.

## Quantified remaining gap

The frozen target sought radius moment T^(29/25+epsilon), equivalently
the sixth-power norm T^(29/50+epsilon). The new complete radius bound
is T^(10beta+epsilon), and its norm exponent is5beta=0.6448317597...
against the target0.58. The remaining norm deficit is0.0648317597... .

At V=T^v, the two distribution terms divided by the frozen target have
powers10v-29/25 and(20/13)v-4/25. The envelope certifies the required
bound only through v=13/125, leaving its high-value range open.
This is a limitation of an upper bound, not a lower bound for actual r2.

The resulting pointwise persistence exponent(1+10theta)/13 exceeds
theta by(1-3theta)/13. For all higher fixed moments this argument
approaches the inherited theta, not one quarter. No pointwise exponent,
M1/M2 obligation, or final target is improved by this closure.

## What changed after independent review

The three original reports supplied the actual distribution attack,
the primary-source match, and an isolated statement-only Gram derivation.
After resume, three distinct reviews checked source/correlation,
Gram/covering/tails, and sharp reconstruction/moments against the exact
candidate. The Gram reviewer found that the original partition omitted
an explicit n=1 treatment. The conductor repaired it by a singleton
block, and every final review binds to the repaired hash above.

The source review verifies global Bourgain Theorem6, the exact s=1/2
model and all small/intermediate/large frequency regimes. The source
audit also corrects the published262/27 provenance to Ivic's1985 book.
No enlarged endpoint is imported from an uninspected original proof:
the new endpoint is derived from the full distribution proved here.

The aligned generic coefficient family attains a peak of heightN^(1/4)
and widthN^(-1/2), giving twelfth momentN^(5/2). This requires keeping
the diagonal/one-interval term in a coefficient-uniform proof. The fixed
arithmetic family is not that example. The bounded weighted-Gram
attempt preserves the phase derivative in its Stieltjes remainder;
the accepted pointwise estimate for P alone supplies no new saving.

## State decision and validation scope

The State Patch creates only
`GC-complete-square-root-large-values-moment-bound`. All398 prior
nodes, existing external source qualifications and pointwise exponents
remain unchanged. The proof draft is appended only after validation
gates and graph mutation succeed. Exact-hash reviews, accepted new
dependency cone, protected Round200--203 archives, frozen plan/briefs,
original-byte restoration and replay are checked by the closure script.
Its output is recorded in `controls/closure_validation.json`.

This validation certifies the new claim within its audited dependency
scope. It does not reprove every historical graph node or erase legacy
advisories. All mathematical work was analytical/algebraic or primary
source inspection; there were no mathematical numerical experiments.
The finite Gram identity is isolated for possible formalization, with
no machine-formal proof claimed.

## Next required round

Round205 is the mandatory broad strategy/current-literature review after
Rounds202--204. Design it from this closed result and the complete
accepted graph. Reassess both the whole-discrepancy route and the full
internal M1/M2 frontier. Select one complete arithmetic objective with
a quantified restored saving; do not repeat generic diagonal deletion,
positive twelve-root majorants, or unpriced transform remainders.
No successor task is frozen in this synthesis. The full goal remains
P(X)<<X^(1/4+epsilon), and it is unproved.

## Evidence

- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- The campaign's three original seven-section reports.
- `reviews/gram_tail_seam_review.md`.
- `reviews/source_correlation_seam_review.md`.
- `reviews/sharp_moment_seam_review.md`.
- `reviews/conductor_round204_reconciliation.md`.
- `controls/conductor_round204_independent_analysis.md`.
- `state_patch.json` and `controls/closure_validation.json`.

All abbreviated paths except the durable kernel are relative to this
campaign. The frozen strategy and prior user strategy memo remain unchanged.
