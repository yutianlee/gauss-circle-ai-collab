# Round227 conductor statement-only phase review

## 1. Result

GREEN for the isolated phase lemma, uniform upper bound, fixed-amplitude
mass asymptotic and explicitly scoped lower bounds. The conductor is not
the report's claimant. No arithmetic or whole-wave estimate is accepted.

## 2. Exact hypotheses

Smooth zero-extended a_d on d+1/2<y<2, 0<d<3/2, all fixed derivatives
uniformly bounded, L>=1 and every real tau. Weighted exponent b>=0 is
fixed. The precise asymptotic fixes d and amplitude before L tends to
infinity. Uniform lower bounds require the stated quantitative interior
nonvanishing. These are not assumptions on the actual arithmetic vector.

## 3. Independent derivation and checks

Rationalizing f_d gives 1/(sqrt(y)+sqrt(y-d)). Differentiation yields
g_d=-y f_d'=sqrt(y)/(2sqrt(y-d)(sqrt(y)+sqrt(y-d))). Its integral
formula gives -g_d'=1/8 integral_0^1 (y+2theta d)(y-theta d)^(-5/2)dtheta.
Thus g_d decreases strictly, remains between 1/(4sqrt2) and sqrt2/3,
and -g_d'>=1/(8y^(3/2)). These formulas independently agree with the
conductor's pre-report calculation in u=sqrt(1-d/y).

In log coordinate v, F''=-y g_d'>=1/(8sqrt2). The tau term is linear
and does not affect curvature. Splitting where the first derivative
is <=sqrt(L), and integrating by parts on the two monotone complements,
proves uniform L^-1/2 without an interior-point assumption. Outside the
fixed positive cone, the derivative is comparable to L+|tau|; repeated
parts has no boundary contribution because of smooth zero extension.
These prove the entire weighted upper mass L^(b+1/2).

The interior quadratic change of variable has positive Hessian
-g_d'(y)/y. Its Gaussian coefficient is
a_d(y)*sqrt(2pi y/(L[-g_d'(y)])) with phase correction +pi/4.
The normalized reduced phase differentiates to log(y) and then
1/(y g_d'(y))<0. The proof of the L^-3/2 error via v^2 times a smooth
amplitude is valid; cutoff margins are explicit and fixed where used.

For fixed d, rescale tau=Lr. The uniform L^-1/2 bound dominates on
the fixed cone, while the rapid outside-cone tail is integrable after
rescaling. Pointwise stationary phase at every interior r, ignoring
the two endpoint r values of measure zero, and dr=g_d'(y)dy give exactly
sqrt(2pi) integral g_d(y)^b |a_d(y)|sqrt(-y g_d'(y))dy. This is positive
for every fixed nonzero smooth amplitude. The uniform version follows
only under the stated lower amplitude, interval length and margin.

Taylor's integral formula from a zero-extension endpoint gives
||a_d^(j)||infinity<=A_(j+M)(3/2-d)^M/M!. It correctly prices shrinking
overlap without changing the L exponent. The exact endpoint estimate
uses arbitrary flatness to compensate each inverse derivative; choosing
flatness order >=2N+1 after N integrations makes the remaining power
integrable uniformly. It is not a false endpoint stationary asymptotic.

Fourier inversion has the stated factor1/(2pi) and negative frequency
sign. The explicit d=1/2 bump vanishes at y=1, so its signed frequency
integral is exactly zero despite mass of order sqrt(L). This is a valid
control separating absolute transform mass from signed reconstruction.

## 4. First unproved step

No gap found in the scoped elementary lemma. A lower bound for an
arbitrary amplitude family or the actual wave would be an invalid extra
step. No external spectral coefficient, transform pairing or complete
arithmetic estimate is derived here.

## 5. Required controls and outcome

GREEN: empty/zero amplitude, positive-frequency sign, tau=0, limiting
d=0 phase and coefficient, moving and exact endpoints, shrinking overlap,
fixed interior example, inverse Fourier constant and all-frequency tails.
Zero experiments. Initial report used only the two authorized files and
records its statement-only isolation accurately.

## 6. Exact artifacts and provenance

Conductor, nonclaimant, Round227. Reviewed report SHA256:
31553bbee7f049e3b2cbea58f04634854bfe4551ac484fb85d308cbce07d96e2.
Path: rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/blind_mellin_phase.md.
Statement packet SHA256:
8f4f90d6cb580fc9485729690753d76c7bc64b7d79085e5e710e7fbd5f9ae49a.
Path: rounds/codex-managed/gc-complete-joint-spectral-remainder/briefs/blind_mellin_phase_statement.md.
Protocol SHA256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
The conductor independently derived the main curvature and application
before reading this report. Its separate application requires nonauthor
review and is not certified by this artifact alone.

## 7. Recommended state effect

Retain GREEN finite/analytic evidence. No graph or proof-draft promotion,
no complete bound, and no actual signed lower bound. The independently
derived phase facts can inform the full kernel review within their scope.
