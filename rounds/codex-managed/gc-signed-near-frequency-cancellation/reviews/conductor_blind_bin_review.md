# Round210 conductor review of the isolated bin transfer

Campaign: gc-signed-near-frequency-cancellation. Date: 2026-09-27.
Role: conductor mathematical review, after the isolated report completed.
Reviewed SHA256:
81e4afa4cd9df504c5ba75072a923ff9e39400d89edcf6269d1f5d884f544b2e.

## 1. Result

GREEN for the analytic transfer, prefix accounting and explicitly generic
countercontrols. No actual arithmetic energy bound follows or is refuted.

## 2. Statement and hypotheses

Finite real frequencies, fixed scaled intervals I subset interior I*, a
smooth cutoff, and absolutely continuous bin functions with finite H1
energy suffice. Infinite right side makes the bound vacuous. The prefix
must be measurable, an appropriate explicit clarification. The conductor
clarified only that G is a squared L2 threshold; this did not supply
arithmetic data or a claimant proof. Original statement-only access lasted
through completion and is not retroactively changed by later reviews.

## 3. Mathematical verification

After t=x/X, the Fourier transform of sum_j e(jt)g_j is the sum of
shifted transforms ghat_j(xi-j). Weighted Cauchy uses the uniformly bounded
series sum_j(1+4pi^2(xi-j)^2)^-1. Plancherel gives the sum of H1 norms
with no frequency-count factor. Cutoff differentiation and dx=Xdt yield
exactly |B_j|^2+X^2|B_j'|^2. The weak-derivative argument covers precisely
the stated finite-energy absolutely continuous functions.

The carrier-canceling example C_(j/X)=e(-jx/X) produces a factor M loss
if derivatives are discarded. The two constant coefficients at0 and1/(2X)
have zero bin-zero sum and nonzero internally phased sum. Both examples
are valid on every nondegenerate fixed scaled interval. Neither claims
to use actual arithmetic coefficients.

The dyadic prefix contains at most d=1+ceil(log2 L) complete intervals.
Pointwise Cauchy costs d, then dropping selection indicators before
integrating leaves the full dyadic energy. The report correctly refuses
to differentiate a jumping prefix and correctly separates the optional
second logarithm, which needs a separate per-level estimate. Labels1,-1
give an exact cancellation control against substitution of full unmasked
energy. Its full sum vanishes while its singleton prefix does not.

In the generic cluster, M comparable to T^8 points with spacing T^-10
fit inside a small fraction of an X^-1 bin. The chosen c bounds every
phase on I*, including negative intervals, so the sum has magnitude
at least M/2. Its chosen amplitude gives exact diagonal energy E0 and
bin/direct energy of order M E0. Since G/E0 has power18/65, the comparison
excess502/65 is correct. This example only tests the explicitly supplied
energy and spacing data. It does not realize the arithmetic rational
frequency set, its denominator constraints, or its coefficient values.
The separate single-frequency example diagnoses derivative energy and
does not falsely claim that modulation increases |F|.

## 4. First unproved step

The actual joint signed bin and derivative energy, with every prefix
interval, remains to be bounded. Neither diagonal energy nor the minimum
separation proves it. The sufficient transfer is not a gain by itself.

## 5. Controls and outcomes

All scale factors, cutoff terms, internal modulation, prefix measurability,
dyadic multiplicities and the squared-norm convention pass. Counterexamples
are finite, analytic and explicitly generic. No experiment, external
theorem import, actual signed lower bound or claimed pointwise gain occurs.

## 6. Artifacts read

protocol.md; the frozen210 isolated packet; the report at the hash above;
the conductor's separately derived transfer for comparison. No external
source or other agent's unfinished result is used to validate this report.

## 7. Recommended state effect

Retain as independently validated interface evidence, with no graph
promotion of the arithmetic target. Preserve the complete signed goal,
the accepted exponent and full-proof scope.
