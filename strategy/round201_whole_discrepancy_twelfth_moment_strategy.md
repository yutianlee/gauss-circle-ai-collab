# Round 201: whole-discrepancy twelfth moment

Date: 2026-09-23. Predecessor: Round 200, closed with its actual-vector
correlation estimate open. Starting graph SHA-256:
2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5.

The preceding goal turn counts as progress: it completed the requested
strategy adaptation and independent complete-source analysis, which
changed the next action. It did not prove a new analytic estimate.

## Selection

Use Campaign C of the supplied strategy review. Round 200 exposes no
source-compatible Kloosterman import, so Campaign B is not yet concrete.
The present route treats the full discrepancy, independently of M1/M2.
It does not abandon those obligations or infer their solution from a
moment identity.

## Frozen objective

For P(x)=N(sqrt(x))-pi x, seek a complete bound

\[
 \int_{Y/2}^{3Y}|P(x)|^{12}\,dx
 \ll_\varepsilon Y^{4+\eta+\varepsilon},
 \qquad \eta<13\theta_{LY}-4.
\]

The existing accepted theta_LY=(3292+25sqrt(1717))/13762 gives threshold
about 0.0882812876628. A negative/incomplete result must expose the exact
remaining signed correlation and the complete exponent deficit. A lower
moment or exact-resonance result does not stand in for the twelfth moment.

Use a fixed smoothing scale over an entire radius window: T=sqrt(Y),
delta=T^(-1/2), rather than a radius-dependent coefficient in a moment
expansion. Choose a fixed radial C-infinity nonnegative mollifier rho of
unit integral and compact disk support, and Psi(s)=rho-hat(s e1). The
coefficient sequence is a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)). For a fixed
smooth nonnegative w supported away from zero and equal to one on
[1/sqrt(2),sqrt(3)], derive the exact weighted moment of

\[
 H_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4).
\]

Verify every smoothing error, real-radius jump, Bessel normalization,
tail, and change of variables. Retain the displaced Fourier kernel
w-hat(-T sum epsilon_j sqrt(n_j)) with its phase. The target weighted
moment is O(T^(1+2eta+epsilon)); positive spacing counts alone are not
credited with this bound.

## Orthogonal tasks and budget

1. Whole-source Poisson/Bessel moment derivation, second-moment
   normalization, and an attack on the complete twelfth moment.
2. Statement-only exact-resonance derivation including every nonpairing
   relation in a squarefree class, and no probabilistic independence
   assumption about a finite radius interval.
3. Primary-source audit of available circle moment bounds, precise p=12
   implications and thresholds, and the first failed transfer hypothesis.

Three reports, at most one bounded repair/review cycle, at most three
subagents; 100% analytic/algebraic research is planned. No numerical
experiments. The conductor independently verifies normalization,
moment-to-pointwise persistence, and coefficient powers. Source searches
are targeted to this interface; Round 202 still performs the scheduled
full strategy/current-literature checkpoint after Rounds 199--201.

## Exit and proof-state discipline

Terminal labels are `whole_discrepancy_twelfth_moment_improvement` only
after a complete valid inequality, or
`whole_discrepancy_moment_reduction_open_offdiagonal` when the complete
expansion and first open estimate are explicit. A genuinely proved
exact-resonance kernel can be independently reviewed for subordinate
promotion; it has no automatic implication to the whole moment or
pointwise theorem. No numerical or arbitrary-coefficient control can
certify the physical target. No agent starts Round 202.
