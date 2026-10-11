# Round208 conductor: a complete bandlimited peak gate

Campaign:gc-full-proof-signed-arithmetic-review. Date:2026-09-27.
Role:conductor analytical derivation; strategy evidence pending review.
Graph SHA256:4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
No mathematical numerical experiments.

## 1. Result

A local reproduction inequality for the actual frequency blocks changes
the sufficient arithmetic gate for a pointwise improvement. It avoids
forcing that improvement through a complete twelfth moment. The new gate
is strictly weaker than the206 sixth-moment certificate wherever the
new gate is needed, and its complementary ranges are already bounded.
No new arithmetic bound is proved here. Comparing the available even
orders then selects the tenth moment, whose current certificate has a
smaller worst deficit than the sixth-moment version. This is a method
choice, not evidence that ten-factor cancellation is easier to prove.
The strategy is to attack the complete local-moment gate, not to count
an additional transform as gain.

## 2. Exact statement and hypotheses

Retain the exact fixed mollifier and partition of205: T>=2, X=T^2,
I=[T/sqrt(2),sqrt(3)T], J=[X/2,3X], and

H_N(R)=sum_n r2(n)n^(-3/4)Psi(sqrt(n/T))v(n/N)
 cos(2pi R sqrt(n)-3pi/4),

where v is smooth supported in[1,4]. Each H_N is a finite exponential
polynomial with Fourier support contained in[-2sqrt(N),2sqrt(N)].
Uniformly for real R, |H_N(R)|<<N^(1/4+epsilon) for1<=N<=T.
The reviewed205/206 bounds on I give
|H_N|<<T^epsilon min(N^(1/4),T^beta,(T/N)^(1/2)), beta=2theta_LY-1/2.
For N>=T the reviewed full radial transform and Schwartz tail give
sum_N>=T |H_N|<<T^epsilon. The singleton is bounded.
The complete reconstruction is
P(R^2)=sqrt(R)H_T(R)/pi+O(T^(1/2+epsilon)).

For the middle scales assume the following bridge, using the exact centered signed shell Z_N of206,
including its actual K, h(x)=2sqrt(x)/sqrt(N), and all m>=1:
H_N(R)=R^(-1/2)Z_N(R^2)+E_N(R),
|E_N|<<T^(-1/2+epsilon)N^(-1)+O_A(T^-A).
Set K_(2k)(N)=integral_J |Z_N(x)|^(2k) dx for fixed integer k>=2.
For the concrete gate(B5) its entire band is within the reviewed206
range. For general b, the displayed bridge and complementary estimates
are explicit hypotheses on the required band; extensions beyond that
reviewed range are not silently accepted here.

Fix0<b<min(beta,1/6). A sufficient complete gate is

K_(2k)(N)<<T^(k+1+2kb+epsilon)N^(-1/2)                 (B1)

for every dyadic T^(4b)<N<T^(1-2b), uniformly in real T.
Together with the stated complementary bounds this implies
P(x)<<x^(1/4+b/2+epsilon) for all real x. The constants may depend on
fixed b,k and epsilon. This is a conditional implication only.

## 3. Derivation

### Local reproduction with no sampling assumption

Choose a Schwartz function eta with Fourier transform equal to1 on
[-2,2]. Put eta_N(u)=sqrt(N)eta(sqrt(N)u). Finite Fourier inversion
gives H_N=eta_N*H_N exactly. If R0 in[T,sqrt(2)T], its distance from
the complement of I is at least cT. Holder on I with p=2k gives

|integral_I eta_N(R0-R)H_N(R)dR|
 <<N^(1/(4k)) (integral_I|H_N|^(2k))^(1/(2k)).        (B2)

Indeed ||eta_N||_(p')=N^(1/(2p))||eta||_(p'). The integral off I is
bounded using the GLOBAL trivial coefficient norm N^(1/4+epsilon)
and the Schwartz tail of eta_N; for N<=T it is O_A(T^-A) after choosing
a sufficiently large fixed seminorm. This retains both radius endpoints
and every real R0. No derivative estimate for the discontinuous P is used.

The actual shell error yields, with dx=2R dR,

integral_I |H_N|^(2k)
 <<T^(-k-1)K_(2k)(N)+T^(1-k+epsilon)N^(-2k)+O_A(T^-A). (B3)

Consequently

|H_N(R0)|<<T^(-(k+1)/(2k))N^(1/(4k))K_(2k)^(1/(2k))
 +T^((1-k)/(2k)+epsilon)N^(-1+1/(4k))+O_A(T^-A).     (B4)

For k>=2 and N>=1 the explicit error is O(T^epsilon), hence harmless.
Substitution of(B1) makes the first term T^(b+epsilon); the N powers
cancel exactly. Thus every middle block is controlled pointwise.

### Complement and complete pointwise reconstruction

For N<=T^(4b), use N^(1/4). For T^(1-2b)<=N<=T, use(T/N)^(1/2).
The endpoints are included in these known bounds. Sum the O(log T)
middle blocks with epsilon losses, then the two geometric outer sums,
the singleton and the reviewed N>=T infinite tail. This gives
|H_T(R0)|<<T^(b+epsilon) uniformly on[T,sqrt(2)T]. Sharp reconstruction
then gives |P(R0^2)|<<T^(1/2+b+epsilon), namely exponent1/4+b/2 in x.
Every x>=4 is covered, for example by choosing T=sqrt(x).

### Concrete comparison with the206 sufficient gate

Choose b=83/650, so1/4+b/2=102/325. For k=3,(B1) becomes

K6(N)<<T^(1549/325+epsilon)N^(-1/2),
T^(166/325)<N<T^(242/325).                           (B5)

The previous complete p12 gate required every
T^(52/125)<N<T^(99/125) and K6<<T^(129/25-6omega+epsilon),
omega=min(alpha/4,beta,(1-alpha)/2), N=T^alpha.
The new band is strictly contained in the old. On the new band omega>b.
Subtracting the old allowable exponent from the new allowable exponent
gives 6b-29/25-alpha/2+6omega. Its minimum is at one of the two new
band endpoints or an omega breakpoint. On the alpha/4 branch its
slope is+1, on the beta branch -1/2, and on the(1-alpha)/2 branch -7/2.
At the lower endpoint it is10b-29/25=38/325>0; at the upper endpoint
it is13b-83/50=0. The other extrema cannot be smaller. Hence(B5) is
weaker than the old sufficient certificate throughout its required
open band; equality occurs only at the upper endpoint already safe.
It is not equivalent to the old p12 target and does not claim that target.

The retained206 upper bound K6<<T^5N^(-29/110) still exceeds(B5).
Its missing saving is

g_b(alpha)=1-6b+(13/55)alpha,
6338/17875<g_b(alpha)<7326/17875.                     (B6)

Both bounds are positive. They concern a deficit of current certificates,
not a lower bound on the actual signed moment. The upper endpoint is the
supremum of the deficit over the new band. No numerical proof is used.

### Compare orders before selecting the arithmetic task

For2<p<q, intersect the reviewed variance Chebyshev estimate
D_N(V)<<TN^-1/2 V^-2 with D_N(V)<<V^-2+TV^-q. Split at
V0=N^(1/(2(q-2)))=N^(13/220), and retain W=T^(omega+epsilon).
Integration below V0 is valid down to0 for p>2. Above V0 the two terms
give W^(p-2) and T V0^(p-q). If W<V0 use only the lower integral.
Uniformly in the complete new band this proves

M_p(H_N)<<T^epsilon[T N^(-(q-p)/(2(q-2)))+T^((p-2)omega)]. (B7)

For p=10 this is M10<<T N^(-3/110)+T^(8omega), with epsilon losses.
The second term must NOT be deleted: it can exceed the first here.
The conditional k=5 gate(B1) is equivalently certified by

K10(N)<<T^(473/65+epsilon)N^-1/2,
T^(166/325)<N<T^(242/325),                            (B8)

or directly M10(H_N)<<T^(83/65+epsilon)N^-1/2.
The tiny shell errors in(B3), also in its inverse direction, are harmless
at these displayed powers. The existing additive bound is
K10<<T^7 N^(-3/110)+T^(6+8omega), retaining BOTH terms.
Subtracting the target exponent in(B8) gives the two deficits

d_A=1-10b+(26/55)alpha,
d_B=8omega-10b+alpha/2.                              (B9)

Throughout the required band d_B>=d_A. At the lower endpoint their
values are0 and -634/17875, respectively. On the first omega branch
d_B-d_A increases; on the middle branch it also increases. On the
last branch it decreases, but at the upper endpoint it is748/17875>0.
There d_A=1342/17875 and d_B=38/325. Thus the needed improvement of
this current certificate has exact profile d_B, positive on the open
band, and worst value

max d_B=7beta-101/130                                (B10)

at alpha=1-2beta. It is positive and less than13/100, using the accepted
exact beta. For comparison the sixth profile has supremum7326/17875;
the eighth-order analogue has a larger worst deficit than(B10): its
first term alone at the upper endpoint is
1-8b+(39/110)(1-2b)>24/100.
These comparisons are between certified upper bounds, not optimality
claims over all possible moment arguments. No extrapolation beyond
p<q is used in(B7).

The sixth and tenth versions of the NEW direct peak gate are not
logically ordered merely by those deficits. There is, however, a direct
implication from the OLD206 p12-sufficient K6 certificate to(B8): it gives
M6(H_N)<<T^(29/25-6omega), hence M10<=W^4 M6<<T^(29/25-2omega),
with the explicit bridge errors retained and negligible. The slack
relative to the desired M10 exponent is
10b-29/25-alpha/2+2omega. It is38/325 on the first omega branch,
decreases on the next two, and is0 at the upper safe endpoint.
Thus the old full-band sufficient condition implies the new complete
gate; no converse or optimality is asserted. This comparison uses the
actual moment interpolation, not a comparison of unrelated numerical gaps.

The conductor therefore selects(B8), on the full displayed band, as the
next candidate objective. This is a ten-factor signed arithmetic problem;
its higher correlation order may be harder than sixth order despite the
smaller missing power. A phase-sensitive level-set method is also allowed
if it establishes the complete M10 gate. Repeating variance, discarding
the W^8 term, or merely expanding a fifth rational convolution is not a
successful outcome. The complete coefficient sum and all masks/errors
must be estimated before a power gain is claimed.

### Full proof scope and a Gaussian hierarchy

If the Gaussian-scale estimate K_(2k)<<X H^k, H=T/sqrt(N), held on all
needed bands, it would imply(B1) whenever
1-2kb-alpha(k-1)/2<=0. The worst required alpha approaches4b, so for
k>=2 it suffices that b>=1/(4k-2). For k=3 this would give b=1/10 and
pointwise exponent3/10, provided the ENTIRE band T^(2/5)<N<T^(4/5)
and its complements are controlled. Assuming Gaussian sixth only on
the old205 band gives instead b=13/125 and exponent151/500; it does
not justify adding the small missing ranges by assertion.

Arbitrarily large fixed k make1/(4k-2) tend to0 and would prove the
full quarter theorem, once the bridge and complements are verified on
each enlarged required band. Constants uniform in k~log T are unnecessary.
One fixed k leaves a positive exponent gap through this certificate.
These implications do not assert Gaussian necessity or refute a more
efficient use of a fixed moment with additional arithmetic information.

## 4. First unproved step

The new sufficient bound(B8), with exact actual coefficients and every
middle block, is unproved. It is the proposed next arithmetic objective;
(B5) remains a sixth-order comparison, not the selected gate.
Even a proof would give only102/325, not the quarter theorem. The full
program retains(B1) for b tending to0 and unbounded fixed k, or another
complete direct proof. The M1/M2 graph parents remain independently open.

The proposed method test is signed aggregation of the complete fifth
rational convolution before taking squared norms, or an estimate
directly on the actual shell. Both hyperbola arms, width and prefix
must stay coupled unless separate estimates are proved at(B8). An exact
convolution identity alone is not progress; it must yield the saving(B9).
The207 termwise-majorant obstruction forbids that particular absolute
closure, not signed aggregation. No current imported theorem has yet
been shown to establish(B8).

## 5. Controls and outcomes

Band reproduction: global finite Fourier support and GLOBAL coefficient
bound pay the off-window tail; a moment on a window with no margin would
not justify(B2). Jacobian:T^(-k-1) in(B3) is retained. Shell error is
explicitly propagated, not silently multiplied by a large supremum.
All endpoints are real and assigned; no arithmetic averaging of x is
substituted for the final pointwise bound. Full infinite series is restored.

An arbitrary Fourier polynomial aligned at R0 can saturate(B2) at a
width N^-1/2; therefore generic deletion of its N^(1/(4k)) factor is
invalid. The fixed-k Gaussian hierarchy leaves b>=1/(4k-2) in this
argument. Neither control is a counterexample on the actual r2 weights.
No new exponent or theorem is inferred from these conditional controls.

## 6. Dependencies and exact artifacts

- protocol.md; selected relevant graph nodes in state/proof_obligations.yml;
  state/active_campaign.yml and strategy/round208_full_proof_strategy_review.md.
- strategy/gauss_circle_strategy_review_2026-09-23.md.
- strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md.
- rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md.
- rounds/codex-managed/gc-full-frontier-moment-strategy-review/reviews/independent_middle_band_review.md.
- rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md.
- rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_bridge_power_review.md.
- rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md.
- rounds/codex-managed/gc-signed-rational-filter-attack/synthesis.md.
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md.

This proof is elementary Fourier reproduction, Holder, exact substitutions
and geometric summation; it imports no new external theorem. Its source
inputs must be independently checked before use outside strategy evidence.

## 7. Recommended state effect

Retain accepted graph/draft without change. After independent verification,
adopt(B8) after the order comparison as the selected COMPLETE sufficient
gate for the same pointwise milestone. Preserve the broader all-k hierarchy and full
quarter goal. Do not claim an improved arithmetic moment or exponent.
