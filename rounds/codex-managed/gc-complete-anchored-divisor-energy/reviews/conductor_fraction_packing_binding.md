# Round219 conductor: isolated fraction lemma and actual binding

## 1. Result

GREEN for the isolated proof and its actual inverse-certificate binding.
The complete signed energy target remains open.

Reviewed isolated report SHA256:
29d9182a310da6bf2e3bbfb87f1df8aefb7001f4b81977759d6ea11683425c93.
Reviewed conductor control SHA256:
b5ccf3e2c362203568885fcc60c39836e5f455a2f6197e8d4dc673b8eb1831bf.

## 2. Exact hypotheses

The isolated count has separated real centers, positive real X,D,A>=1,
integer d,e in the literal half-open dyadic interval, and positive
width c'A/X. Its constants depend only on the two fixed spacing/width
constants. It is a positive counting lemma without character input.

## 3. Mathematical review and actual application

The exact gcd multiplicity is the number of positive integers in
[D/min(a,b),2D/max(a,b)). Its ceiling formula and bound2D/max(a,b)
are valid even below length one. Reduced fractions in denominator
shell Q are separated by1/(4Q^2), while original nonreduced pairs
have already been accounted for by that multiplicity.

Counting first by fractions gives O(AQ^2); counting first by centers
gives O(J+JAQ^2/X). Their minimum, weighted by D/Q, sums to
D sqrt(JA)+JAD^2/X. Both geometric tails are controlled when
sqrt(J/A) is outside the denominator range. Summing2^(-m) at A=2^m
gives D sqrt(J)+(JD^2/X)log(2+B), with no missing first-term log.

For each fixed actual anchor j, choose X=T sqrt(N) and
z_l=(R_l/R_j)^2. Differentiation of this scalar map on[T/2,2T]
and the actual N^(-1/2) separation give fixed spacing c/X.
Squaring the near radical difference, with d,e~D, gives width
C A/X. Thus the isolated count bounds all actual near pairs with
abs(u^-)<=A/sqrt(K), even though it may also count extra pairs.
Use B comparable to T sqrt(N), then multiply by K and sum over j.
This is the conductor control's JN sqrt(J)+J^2D sqrt(N)log T/T.
For plus arguments the direct lower bound u^+>=cT sqrt(D)
gives the second cost without its logarithm. Exact zero differences
are in the A=1 bin and never enter an inverse of zero.

The physical weights have bounded variation by216, so Abel losses
are bounded; its arbitrarily small source powers are chosen before
Young's inequality and fit the final requested epsilon. Young yields
an arbitrarily small fraction of J^2v^2D sqrt(N) plus
JN sqrt(N)/(Dv^2). Actual high rectangles satisfy N<=T^(1+delta)
up to a fixed constant by Schwartz decay and the stated high level.
The pre-Cauchy necessary D bound then gives169/3500+epsilon, with
the exact margin13/420 to208/2625. This step uses high-value
nonemptiness, not a new effective cutoff imposed on every rectangle.

## 4. First unproved step

The surviving positive-power oscillatory certificate and actual signed
minus/plus aggregate are not estimated at the target size. The packing
lemma proves no signed cancellation. The application is only a bound
on the explicit inverse envelope, not a decomposition of the exact
kernel into two canonically signed pieces.

## 5. Controls and outcomes

The isolated J=1, z=1 example retains D exact gcd multiples. The
D=1 and crossover-outside-range checks are correct. Very wide windows
are covered by the bulk term, and the proof permits real endpoints.
Removing center separation or allowing A to tend to zero without an
additional1 term would invalidate the isolated statement, as shown by
its controls. The actual binding only uses A>=1. No experiment is used.

## 6. Dependencies and provenance

reviews/isolated_fraction_packing_rederivation.md and
controls/conductor_anchor_packing.md at the hashes above; isolated
packet SHA256445f82a9a20accc126798dd9dac406500e973ef41c8d3b305cf0c8131054e74b;
the closed216 exact energy and scalar estimate. The isolated reviewer
had no conductor proof/application access for this derivation; its
prior-task history is disclosed. This document is the conductor's
independent application seam.

## 7. Recommended state effect

Retain checked evidence; no graph or proof-draft change. Improving this
component does not improve a complete parent estimate or exponent.
