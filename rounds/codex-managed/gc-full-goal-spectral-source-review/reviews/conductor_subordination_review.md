# Round226 conductor isolated-subordination review

## 1. Result

GREEN for the finite identity, exact convergence sector and boundary
qualification, absolute-ray multiplier and its optimal order. The
conductor is not the claimant of the reviewed statement-only report.
No infinite theta or arithmetic estimate is accepted by this review.

## 2. Exact hypotheses

Finite complex coefficients on positive integers; z=sigma-i omega with
sigma>0, omega>=0. Rays point outward at -pi/2<theta<pi/2, with continuous
principal t^(-3/2). For norm comparison the support is integer[N,2N],
N>=1, and its coefficient norm is l1. No nonnegative-coefficient or
asymptotic arithmetic hypothesis is introduced.

## 3. Independent verification

The scalar Gaussian integral has constant2sqrt(pi)/w; differentiating
J(c)=integral exp(-v^2-c^2/v^2) gives J'=-2J after the reciprocal
substitution. Its initial value sqrt(pi)/2 fixes the constant.
Holomorphic continuation for |arg w|<pi/4 and Re lambda>0 is justified
on compact parameter sets by exponential endpoint domination.
Putting w=z exp(-i theta/2), lambda=n exp(i theta) gives
w sqrt(lambda)=z sqrt(n). The ray differential contributes precisely
exp(-i theta/2); it cancels against the prefactor and square root.

Writing alpha=atan(omega/sigma), the strict condition is
D=|z|^2 cos(2alpha+theta)>0, equivalently
-pi/2<theta<pi/2-2alpha in the stipulated angular family.
For a nonzero finite H, its finite vanishing order m at zero shows
absolute integrability there is controlled by
u^(m-3/2)exp(-D/(4u)). Thus D<0 is impossible, whereas at D=0
one needs m>=1, exactly sum a_n=0. That exceptional boundary identity
uses domination of the combined sum, not individual exponentials.
The empty sequence is separately zero. All strict-ray contour arcs
vanish with the estimates in the report.

The coefficient envelope A exp(-N cos(theta)u) gives
Q=|z|D^(-1/2)exp(-sqrt(ND cos(theta))) exactly.
The independent square identity
D cos(theta)=sigma^2-(sigma sin(theta)+omega cos(theta))^2
and D<=2sigma omega for omega>=2sigma give the reported lower
comparison. On theta=-alpha, D=sigma|z| and cos(theta)=sigma/|z|,
so Q=sqrt(|z|/sigma)exp(-sigma sqrt(N)). The two bounds differ
by at most sqrt2 and do not require an exact minimizing angle.

For a single coefficient at N the original value and exact l1
functional norm are exp(-sigma sqrt(N)). Consequently the certificate
loss is not an actual-value lower bound. When omega=0 the positive
real ray is optimal. The D->0 and cos(theta)->0 boundaries have the
distinct behaviors stated in the report; a finite-sequence limit at
the imaginary ray supplies no infinite-series assertion.

## 4. First unproved step

No gap found in the finite claims. An infinite theta series or an
actual weighted application requires new convergence and uniform
parameter estimates. This review does not provide them.

## 5. Controls and outcome

GREEN: all constants and orientations, strict sector, zero-sum
boundary exception, empty sequence, omega=0, singleton norm, both
angular limits and sigma approaching zero. Zero experiments.
Current two-file isolation and retained-history disclosure are explicit.

## 6. Exact bindings and provenance

Conductor, round226, nonclaimant review.

- reports/blind_complex_subordination.md:
  35b28a172e791013cab241a44d47c43b0aea8fd6f7e372be3665b48146a45c0e.
- briefs/blind_complex_subordination_statement.md:
  5666b5ab44da69ab9b35dbcd28658cd9a9e9ba5dd454d25fe1df8ef21222b39a.
- protocol.md:
  f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.

The first two paths are relative to
rounds/codex-managed/gc-full-goal-spectral-source-review.
The conductor also derived a separate application control; that
control requires its own nonauthor review, not self-certification here.

## 7. Recommended state effect

Retain GREEN scoped finite evidence. No complete analytic bound,
graph promotion, draft edit or successor follows from this identity.
