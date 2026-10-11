# Round223 conductor review: isolated Fourier transfer

## 1. Result

GREEN for the fixed-profile analytic lemma and its explicitly limited
application interface. The continuous absolute Fourier mass is comparable
to sqrt(lambda), whereas the exact signed periodization and discrete
functional need not have that size. No arithmetic estimate is promoted.

## 2. Exact statement and hypotheses

Reviewed the entire final isolated report under its stated fixed compact
smooth nonzero complex amplitude, real smooth phase of uniformly nonzero
curvature, lambda >= 1, and any real N >= 1. The amplitude has a positive
gap from the support interval endpoints. Coefficients have finite integer
support. Family uniformity additionally requires the explicit common
support, curvature, derivative and positive L2-mass conditions. Literal
hard cutoffs are excluded from the absolute-integrability assertion.

## 3. Independent derivation and line audit

For g=lambda*phi-u*x, continuity and nonzero curvature make g' monotone.
The region |g'|<=t has length at most 2t/(lambda*c0). Integrating by parts
on its at most two complementary intervals gives a bound of constant
times (||W||infinity+||W'||1)*(t/(lambda*c0)+1/t). Choosing
t=sqrt(lambda*c0) gives the uniform Fourier supremum O(lambda^(-1/2)).
Outside lambda*phi'([a,b]), the support gap bounds |g'| below by a fixed
multiple of lambda plus the distance to that interval. Repeated integration
by parts has no support-boundary term and bounds the two tails by
O(lambda^(1-q)). The stationary band has length O(lambda); hence the L1
upper bound is O(sqrt(lambda)). Fourier inversion followed by absolute
Fubini gives Parseval here. Since |W*e(lambda*phi)|=|W|, the nonzero L2
mass and the supremum bound give the matching lower L1 bound for all
lambda >= 1. This works for complex W without a positivity assumption.

Changing variables u=N(alpha+m) in the nth periodized Fourier coefficient
gives F(n/N), since exp(-2*pi*i*n*m)=1 for integer n even when N is real.
Thus G(alpha)=sum_n F(n/N)e(-n*alpha), a finite sum. Integrating against
sum_n c_n e(n*alpha) has neither a conjugation nor an extra factor of N.
Tonelli separately gives integral A=||Fhat||1 for the absolute
periodization A. Only |G|<=A follows pointwise. A bound for the arithmetic
polynomial on a subset must retain the weighted complementary integral.

With N=1 and support inside (1/2,3/2), the only sample is n=1.
For phi=sqrt(x), G=W(1)e(lambda)e(-alpha), so its L1 norm is constant
while integral A grows like sqrt(lambda). The finite coefficient lp dual
norm is exactly the l(p') norm of the sampled |W|, independent of lambda.
These are decisive controls against an automatic signed/discrete lower
transfer, but they are not lower or upper estimates for fixed arithmetic
coefficients at growing N. For a hard [1,2] cutoff, the stated endpoint
term has the correct sign and a periodic numerator of positive mean
absolute value; its 1/|u| tail indeed prevents absolute integrability.

## 4. First doubtful or unproved step

None in the fixed-profile assertions. Applying them to a new moving
family requires its uniform hypotheses; using a linear-sum theorem still
requires the actual coefficient class and all exceptional frequencies.
No sqrt(lambda) lower bound is available for G or for the actual sum from
this lemma alone. This review supplies no complete analytic gain.

## 5. Controls and outcomes

GREEN: monotone curvature, full stationary band, both tails, complex
amplitude, inversion and absolute Fubini, real N and Fourier signs,
exceptional-set retention, one-sample alias cancellation, optimal finite
coefficient norm, moving-profile limitations, hard endpoints. All checks
are analytical; no numerical experiments or source imports were used.

## 6. Dependencies and provenance

Conductor NONBLIND review, round223, 2026-09-28. The conductor independently
derived the principal mass and periodization application before reading
the complete report; the report's progress message had disclosed its
lower-bound conclusion. This review does not claim statement-only
isolation. The claimant's current packet isolation and prior history
remain as disclosed in its report. Final bindings:

- reports/blind_oscillatory_transfer.md:
  2d630317cdf25d30fbec3705941ee6aa4fe664b457cc6acfdea9992913595f0e.
- briefs/blind_oscillatory_transfer_statement.md:
  8f22f707e3ee85bb8438e11eff55613cba31a227a7b5a3b113bf35b12a087ea5.

Both paths are relative to this campaign directory. Protocol and the
frozen round223 strategy govern scope; no other candidate proof is used
to certify this lemma. Starting graph SHA256 is
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

## 7. Recommended state effect

No graph change. Retain this reviewed standard analytic infrastructure
and its exact scope controls as round evidence. Do not promote an
arithmetic bound, moment gain, complete M1/M2 estimate or quarter target.
