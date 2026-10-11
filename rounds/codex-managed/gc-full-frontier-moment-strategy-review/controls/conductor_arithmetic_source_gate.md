# Round 205 conductor: arithmetic correlations and probabilistic exceptions

Campaign: gc-full-frontier-moment-strategy-review. Date: 2026-09-26.
Role: conductor independent primary-source application audit.
Starting graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
100 percent analytical/source work; no numerical experiments.

## 1. Result

Two arithmetic-sensitive methods address the correct representation
function, but their printed theorems do not certify the proposed complete
middle-band moment. Linear-form correlation asymptotics do not supply
the requisite thin-box power error. The circle random-model theorem
controls fixed moments off an exceptional set whose size can contain
all of the currently problematic peaks. These are application gaps, not
impossibility theorems for either method or for the actual coefficients.

## 2. Exact primary statements and hypotheses

**Matthiesen.** [Correlations of representation functions of binary
quadratic forms, arXiv1205.4145v1, Theorem1.1, pp1--2]
(https://arxiv.org/pdf/1205.4145), current sole version18May2012,
extends the positive-definite treatment
[arXiv1106.4690](https://arxiv.org/abs/1106.4690).
For primitive irreducible binary quadratic forms (positive when definite),
pairwise affinely independent affine forms psi_i in d variables, and a
convex K contained in [-X,X]^d with positive arguments where needed,
the correlation of primary representation counts is a product of local
densities times volume, with error o(X^d). Constants may depend on the
forms and coefficients of the affine system. For x^2+y^2 and positive
arguments its primary count is r2/4, so the weight matches up to a fixed
factor. This theorem does not concern the indicator of representability.

**Lamzouri.** [On the distribution of the error terms in the divisor
and circle problems, arXiv2410.03652v1, Theorems1.5--1.6 and6.2]
(https://arxiv.org/pdf/2410.03652), current sole arXiv version4October2024;
published [IMRN2025(3), rnaf006,24January2025]
(https://doi.org/10.1093/imrn/rnaf006).
Theorem6.2 compares the complex exponential moment of x^(-1/4)P(x)
on a set A within [Y,2Y], whose complement is O(Y(log Y)^(-10)),
with the circle random series. Its allowed complex parameter range
eventually contains the fixed values +1 and -1. The comparison error
tends to zero. Theorem1.6 controls signed tails only up to an iterated-log
scale V=(log log Y)^(1/4)(log log log Y)^(O(1)), not Y^c for c>0.
These are actual circle statements with representation multiplicities.
The printed historical benchmark in that preprint does not supersede
the separately accepted repaired Li--Yang source.

All current records and these primary theorem texts were checked on
2026-09-26. No source theorem is promoted or strengthened here.

## 3. Derivation of the two import costs

The local arithmetic scale in the conductor's middle-band interface is
X=T^2, with h=T/sqrt(N), hence X^(151/500)<h<X^(99/250). Opening a
single twelfth shell moment and anchoring at one of its twelve integer
arguments produces affine forms

\[
 \psi_1(x,h_2,\ldots,h_{12})=x,\qquad
 \psi_i(x,h_2,\ldots,h_{12})=x+h_i\ (2\le i\le12).
\]

There are d=12 variables, not13. When the shifts vary independently,
these forms have nonproportional linear parts, and the basic positivity
condition holds on an interior box. Such a box has volume about Xh^11.
The cited error o(X^12) is not a quantitatively small error relative to
Xh^11: writing it as e(X)X^12, all one knows is e(X)->0, while the
ratio is e(X)(X/h)^11. No fixed power saving follows. Subdivision into
shorter boxes also needs uniformity in the translated coefficients and
an explicit error rate, neither supplied by this statement in the form
required here. A theorem with fixed shifts x+h_i in a single variable
instead has affinely dependent forms, outside that hypothesis.

Repeated shifts in a moment are additional diagonal configurations
and cannot be removed by declaring them generic. The actual odd kernel
weights, the curvature R-sqrt(m), local densities, and summation over
all shifts have still to be restored. In particular, a positive
unweighted asymptotic is not automatically a cancellation estimate for
those signed weights. This calculation identifies the missing input;
it makes no assertion that a thin-box refinement is false.

For the second method put F(x)=x^(-1/4)P(x). From the two fixed real
parameters in Theorem6.2, finiteness of their random exponential
moments, and

\[
 |u|^{12}\le12!(e^u+e^{-u}),
\]

one obtains \(\int_A|F(x)|^{12}dx\ll Y\). This is a direct positive
inequality, requiring no differentiation of a nonuniform error term.
If the source's summation convention omits the origin, its P differs
from the inclusive project P by1. The resulting O(Y^(-1/4)) change
in F preserves both fixed exponential bounds and this moment estimate.
With x=R^2, dx=2R dR and R~T, the corresponding good radius set has
the normalized actual-series moment O(T^(1+epsilon)); the reconstruction
error O(T^epsilon) is included. Use finitely many comparable intervals
to cover any chosen fixed enlarged window.

The bad radius set E has measure O(T(log T)^(-10)). Multiplying this
by the accepted supremum bound to the twelfth power costs

\[
 \int_E |H|^{12}dR\ll_\epsilon
 T^{1+12\beta+\epsilon}(\log T)^{-10},
\]

far above T^(29/25). Combining the bad-set measure with Round204's
distribution only recovers, without a new arithmetic input, the existing
high-level contribution T^(10beta+epsilon). At V about T^beta the
potential measure V^(-2) is T^(-2beta), much smaller than the allowed
bad set. Thus the exceptional set can contain every peak responsible
for the old upper bound. There is no license to discard it or to
transfer the random-model moment to the full interval.

Similarly the iterated-log range in Theorem1.6 is below T^(13/125)
for all sufficiently large T. It does not reach the fixed positive
power levels that remain in the complete high-value objective.

## 4. First unproved step and method choice

An arithmetic short-shell attack must retain the exact r2 divisor
identity and odd filter and obtain a quantitative signed correlation
bound on these thin ranges, including repeated shifts, with the restored
moment saving 10beta-29/25. This is the concrete first estimate, rather
than another reduction to an unspecified trace function.

A probabilistic alternative needs a target-sized twelfth moment on the
entire exceptional set. Its printed measure bound alone is insufficient.
Keep this as a comparison mechanism, not a second new unestimated
complement that replaces the complete moment target.

## 5. Required controls and outcome

- r2/4 representation count versus indicator: normalization checked.
- Twelve factors use twelve independent anchored variables; thin-volume
  and ambient-error exponents distinguished.
- Fixed-shift dependence and repeated-shift diagonals explicitly retained.
- Real-radius Jacobian, reconstruction error and finite interval cover paid.
- An exceptional-set measure does not control its high moments; the generic
  aligned and abstract monotone peak controls remain compatible with it.
- No new exponent or unconditional source import. No numerical experiment.

PASS as a bounded application audit, pending the independent source seam.

## 6. Dependencies and exact artifacts

Primary URLs and exact theorem locations appear in Section2. Local context:
protocol.md; state/proof_obligations.yml; state/active_campaign.yml;
strategy/round205_full_frontier_strategy_review.md;
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md;
rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/
conductor_middle_band_strategy.md. The historical circle bibliography
was searched for arithmetic correlations and actual representation-weight
random models; nonprimary discovery hits were not used as evidence.

## 7. Recommended state effect

No change. Retain the signed short-shell method as the proposed bounded
next attempt, with a compulsory complete power ledger and no theorem
credited in advance. Archive both failed direct imports as strategy
evidence only; the accepted graph and full quarter target are unchanged.
