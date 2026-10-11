# Round227 conductor complete-frontier review

## 1. Result

GREEN for the scoped exact spectral interfaces, scalar transforms and
complete norm-cost assessment. No complete wave or moment bound and no
pointwise exponent improves. The original all-shift target (F) is unproved.
The two spectral reports receive reciprocal nonauthor reviews; the isolated
Mellin lemma and conductor application have separate nonauthor reviews.
This conductor review reproduces the normalization and full restoration.

## 2. Exact statement and hypotheses

Use the frozen complete packet: T>=2, every real R in [cT,CT], every dyadic
2<=N<=P<2T^(3/2), actual r2, actual real smooth g_N with signed fixed Psi,
A=(1+N/T)^(-J), and all 1<=h<2N. The sufficient raw target is
2Re sum_h(1-h/(2N))(C_h-rho_h integral W_h)<=A^2 N^(3/2)T^epsilon.
It includes every discrete and continuous overlap. All Schwartz orders
and differentiation counts are fixed after selecting epsilon and tail order.
The inherited beta applies to the complete REAL wave only.

## 3. Independent algebra and analytical restoration

For the first report, Mellin inversion measures n+h. The expression
h^(1-s)/(s-1)=integral_h^infinity y^(-s)dy is exactly the constant-density
transform. On Re(s)=2, the Dirichlet series and its centered atom/density
bracket are absolutely controlled. The atom vanishes only after full
inversion because W_h(0)=0; keeping its finite-contour term is necessary.
Substitution z=it in HKLDW(3.10) gives precisely the report's continuous
coefficient and three-cusp integral. No contour movement or omitted residue
occurs. Its compact-contour spectral sum is taken before the outer limit.

Here is a second elementary derivation of the inverse kernel. Set
a=1/2-it, b=1/2+it. Multiply the beta integrals for
Gamma(s-a)/Gamma(s) and Gamma(s-b)/Gamma(s). Change their product
variable to x=1/(uv)>1 and set v=1/(xu). The resulting Mellin density is
x/[Gamma(a)Gamma(b)] times
integral_0^1 r^(b-1)(1-r)^(a-1)(1+(x-1)r)^(-a)dr.
Euler's integral identifies this as x P_(-1/2+it)(2x-1).
Consequently G(s,it)=integral_1^infinity P(2x-1)x^(-s)dx,
and inversion against q_h gives K_h(t)=h^(-1/2) integral W_h(x)
P(1+2x/h)dx. The powers of h and N therefore agree. This per-mode
identity does not exchange an infinite spectrum with a Mellin limit.

For the second report, the matrix in its (5) has determinant h/4 and
Frobenius square 2(h/4)+n. Thus u(Mi,i)=n/h. Its inverse recovers all
parity-matched quadruples. At odd h, the unhalved matrix has determinant h,
Frobenius square 2h+4n and again u=n/h; the two allowed reductions modulo2
form the conjugate of Gamma0(2). Sign quotienting supplies factor2 in
both cases. Applying the normalized Hecke operator to the smooth radial
automorphic kernel therefore gives the prefactor2sqrt(m), not a borrowed
bound for a disk test. The point stabilizer remains counted by the orbit
sum. The test may be complex by linearity. Its smooth spectral expansion
and all continuous cusps are present before taking any norms.

Independently iterate the pointwise parity recurrence at h=2^k h0. For
k>=2 it gives 2 sum_{a=0}^{k-2}(-1)^a A_{h/2^a}[W_h(2^a x)]
+(-1)^(k-1) S_{h0}[W_h(2^k x)]. In each A term write
m=h/2^(a+2); its radial argument is 2^(a+2)m u=h u.
The final odd term also has argument h u. This proves the common test
and all coefficients in (9), including k=0 and1 separately. The constants
3/pi and1/pi and H_h(i/2)=4pi I_h/h give
48/h sum_{a=0}^{k-2}(-1)^a sigma1(h/2^(a+2))
+8(-1)^(k-1)sigma1(h0)/h.
Using sigma1(2^j h0)=(2^(j+1)-1)sigma1(h0) reduces this to
8(2^(k+1)-3)sigma1(h0)/h for k>=2. At k=1 it is4sigma1(h0)/h0;
for odd h it is8sigma1(h)/h. All are the prescribed rho_h. Conversion
from probability to area-orthonormal eigenfunctions multiplies the stated
point fourth norm by a fixed volume factor, not a growing parameter.

Both formulations give the same scalar Legendre transform. Put
x=h sinh^2(r/2). Then dx/dr=sqrt(x(x+h)), sinh r=2sqrt(x(x+h))/h,
and the physical phase is exactly2pi R sqrt(h)exp(-r/2).
On the overlap r>log3, the r-window has bounded length. The positive
Legendre branch has a stationary point at
t=pi R(sqrt(x+h)-sqrt x), with curvature t/2. Its phase equals
2t+t log(pi^2 R^2 h/t^2). The scalar amplitude is
g(x+h)g(x)sqrt(h sqrt(x(x+h)))/t: the Legendre and stationary
pi/4 factors cancel. This verifies the stated scale t~Rh/sqrt(N).
The exact transform and uniform symbol estimates treat the small-shift
transition; the interior separate-Stirling computation alone cannot.
At t comparable to Lambda_h, |J_h|/sqrt(h)<=A^2 sqrt(N)/Lambda_h.
Nonstationary integration with fixed higher derivatives pays the low and
far spectral tails, including a shrinking smoothly zero-extended overlap.

The isolated Mellin calculation is consistent: log-coordinate curvature
is -L y g_d'(y)>0, where -g_d'>=1/(8y^(3/2)). Its weighted absolute
transform mass costs L^(b+1/2); matching lower order needs a fixed nonzero
interior amplitude. Inverse Fourier reconstruction can instead vanish.
The nonauthor application review records the universal gamma factor -i,
which changes neither critical equations nor the reduced phase. It also
confirms tau-t~Rh^2/N^(3/2); a large tau alone does not justify Stirling
for both numerator gamma factors.

The first report's fixed-contour tails are sufficient independently of
any normalized theta-pairing bound. Integration by parts gives Mellin
tail A^2N^(2+eta)(1+R sqrt(N))^B L^(1-B). At spectral height U>=4L,
gamma decay, normalized Fourier second moments and ordinary Parseval give
an exponentially small tail times fixed powers of L,U,N. Taking
L=T^Q(1+R sqrt(N)), U=4L and fixed large B,Q pays every discarded term.
The retained finite rectangle is not reduced for free to its stationary
part. Ordinary Parseval does not bound the exponentially renormalized
theta pairings; the reversed-limit full Legendre sum stays unasserted.

The whole-functional Heegner formulation bypasses that exchange and the
false coefficientwise point identification. For h~M and U~TM/sqrt(N),
sqrt(m)|H_h|<=A^2 sqrt(N)/U times sqrt(m/h). The geometric sum of the
parity factors is bounded. The stated fixed-point fourth norm is U^(1+eps)
after a square root, and the individual Hecke second norm is U^(1+eps)
because U^2 dominates sqrt(m). Minkowski therefore gives vector norm
A^2 M sqrt(N)T^eps and raw pair price A^2 T M^2 T^eps. The local-Weyl
continuous majorant gives the same price without an invented Eisenstein
fourth moment. The h- and t-dependent vector cannot be inserted into a
fixed-coefficient sieve without paying separation. Even the explicitly
hypothetical fixed-sieve-size norm A^2 sqrt(NM) would cost A^2 T M^(3/2)
in the fourth-moment pairing. Sum all shift bands: respectively
A^2 T N^2 and A^2 T N^(3/2). Neither proves (F).

At M=N the sufficient vector size for this positive method is A^2 N/T,
versus its available upper certificate A^2 N^(3/2). Their ratio is
T sqrt(N), not an actual-vector lower bound. At N=T the hypothetical
sieve still misses a factor T. These observations do not exhaust
phase-sensitive methods or forbid cancellation in the exact signed sum.

Finally the original coefficients cap the full raw remainder by A^2N^(2+eta).
One integration by parts gives |I_h|<=A^2 N^(3/2)/(Th). The normalized
Fejer inequality has multiplier (7N/2-2)/(2N)<2, diagonal A^2N^(-1/2+eta),
density A^2T^(-1)N^eta log(2N), and capped remainder A^2N^(1/2+eta).
Square roots and the complete dyadic sum give complex T^(1/4+epsilon),
including n=1 and the original Schwartz tail above P. Physical restoration
is3/8. The uncapped and hypothetical menus give respectively5/8 and1/2.
All are weaker than the inherited qualified complete REAL benchmark.
If (F) held, the same reconstruction would give complex T^epsilon and
physical1/4; no such estimate is established. The prior complex13/56
certificate is a separate weaker benchmark than the real target, not a
new result here or a per-block beta estimate.

## 4. First doubtful or unproved step

The full signed pairing (10) in the Heegner report, equivalently (25) in
the first report with paid finite truncations, is still unproved at
A^2 N^(3/2)T^epsilon. A named sufficient positive norm requires the
quantified saving above, but that certificate is stronger than necessary.
The next meaningful test must use the actual h^(it) vector together with
the common spectral phase and complete spectra. An exact inversion,
fixed-coefficient sieve with an unpriced twist, or another local sector
does not close this obligation. No all-method impossibility is certified.

## 5. Required controls and outcomes

Final-hash nonauthor reviews are GREEN within scope. Source hypotheses,
zero atoms, constant densities, parity descendants, spectral measures,
all cusps, literal empty overlaps, low/high tails and reconstruction
powers are checked. Source printing defects are not silently corrected.
No current source role read the blind report before freeze; the blind
initial role had only its statement packet and protocol. Its later
application review discloses retained history and does not review itself.
The root application has that separate nonauthor review. Zero mathematical
experiments; at least95 percent analytical/algebraic work. All complete
M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR lower ownership through159 and
endpoint alternatives persist. Both terms of the accepted distribution
bound persist. Fixed twelfth29/25 gives102/325, not quarter; the sufficient
unbounded sequence of fixed even orders remains open.

## 6. Dependencies and exact bindings

- rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/joint_shift_spectral_attack.md: 9df8afa574a54a6d9c7ca587030aeaec00a7daa345594d224116a93e823d3560.
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/heegner_joint_norm_audit.md: cc921c6d04fb7015e68915000badffa82ff284734460e0be57b2260197443909.
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/blind_mellin_phase.md: 31553bbee7f049e3b2cbea58f04634854bfe4551ac484fb85d308cbce07d96e2.
- rounds/codex-managed/gc-complete-joint-spectral-remainder/controls/conductor_mellin_phase_application.md: 1a519e5624ef72b28544a9762584f88a26b000377b572b308f7100d7f527cef4.
- rounds/codex-managed/gc-complete-joint-spectral-remainder/briefs/blind_mellin_phase_statement.md: 8f4f90d6cb580fc9485729690753d76c7bc64b7d79085e5e710e7fbd5f9ae49a.
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reviews/conductor_mellin_phase_review.md: c50783c84248f1bd27f10ae8f1c079f0edbf3f8cebed0165e6280d50191dabdd.
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reviews/independent_spectral_attack_review.md: f4cf5c138c03175f9a54eacb665617183fa26fce7de0f02fbb4e85ee7826ce3c.
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reviews/independent_heegner_norm_review.md: a641c8cfc267658bbc1ca82f7633b682d5ea2e9d46a035271455e6a3b52475c2.
- rounds/codex-managed/gc-complete-joint-spectral-remainder/reviews/independent_mellin_application_review.md: 5a0150efbbfcf564b5ed16b4c6f54997a12e41d6c50995855ccb12fb5dbc1e1d.

Root primary checks: HKLDW1705.04771v3 equations(3.7),(3.10) and Lemma3.4;
HKLDW1703.10347v3 Lemma6.1's Fourier bound only; AH2607.13518v1
Theorem1.2 and equation(8); Chamizo2022 Proposition2.2 and its group,
Hecke and density conventions. Exact links and hypothesis cards are in
the reviewed reports. No new external theorem was promoted. AH's
fourth-moment statement is an explicit external premise, not a completed
proof audit of its supporting printed sieve. Source defects do not imply
that separately stated theorem is false. The root independently derived
the algebra and prices above; historical ownership remains graph-controlled.

## 7. Recommended state effect

Identity State Patch only. Retain these exact complete interfaces and
scope-limited norm/phase controls as reviewed evidence. No new accepted
estimate, graph mutation, proof-draft edit or exponent change. Close227
after mechanical validation, leave228 pending design of a bounded actual
signed spectral estimate, and retain broad strategy/current-primary
review229. The full goal remains active.
