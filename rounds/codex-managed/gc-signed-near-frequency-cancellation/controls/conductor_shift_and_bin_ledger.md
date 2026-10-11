# Round210 conductor: signed-transfer costs and the Abel-certificate barrier

Campaign: gc-signed-near-frequency-cancellation. Date: 2026-09-27.
Role: conductor analytic derivation, candidate evidence pending review.
Graph SHA256:4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
No mathematical numerical experiments or new external theorem imports.

## 1. Result

Two complete sufficient interfaces retain the signed problem: a joint
Sobolev energy for internally modulated rational bins, and a fifth moment
of the positive part of the signed Fejer shift aggregate. Neither input
is proved here. The latter interface has a definite minimum useful shift
length. A different shortcut, transferring an unweighted cumulative
correlation error through absolute Abel variation, cannot attain the
pointwise target even if its continuous mean term is free and its error
bound is of constant size. This is a statement about a specified positive
certificate, not about the actual shifted correlations or signed moment.

## 2. Exact objects and hypotheses

Keep T real, N=T^alpha, b=83/650, gamma=10b=83/65,
166/325<alpha<242/325. The required physical energy is
U=T^gamma N^-1/2; the required rational energy is G=T^6 U.
The word energy means the integral of a square, or the original tenth
moment, not its square root. Original H_N, Z_N, rational Q_N and all
outer ranges/errors are exactly those reviewed in208--209.

For the centered alternative, let c_n=r2(n)-pi, and
f(t)=t^-3/4 Psi(sqrt(t/T))v(t/N), supported in[N,4N]. Set
u_n(R)=c_n f(n)e(Rsqrt(n)), F(R)=sum_n u_n(R).
The discrete mean is pointwise safe by the reviewed209 estimate; a
bound for F supplies a sufficient centered pointwise route. It is not
asserted equivalent to the unmodified physical tenth gate.
The fixed real v is nonzero and has a sign-definite interior interval;
for large T, Psi is positive on its support. The proof below only needs
f(t)f(t+h)>0 on that common interior interval, regardless of the sign of v
elsewhere. Constants absorb bounded T,N.
Choose a small fixed delta>0 preserving a common positive subinterval
for f(t)f(t+h) whenever1<=h<=delta N.

For integer2<=L<=delta N, zero extend u_n and define
D(R)=sum_n|u_n(R)|^2 and
C_h(R)=sum_n u_(n+h)(R)conjugate(u_n(R)),
S_L(R)=2 Re sum_(1<=h<L)(1-h/L) C_h(R).
D is independent of R. The divisor envelope gives D<<N^-1/2+epsilon;
the centered atom lower bound gives D>>N^-1/2.

## 3. Derivation and complete costs

### A. A lawful phase-preserving bin transfer

For a finite frequency family on a slightly enlarged x-interval J*,
define F_0(x)=sum_mu C_mu(x)e(mu x), bins j/X<=mu<(j+1)/X and
B_j(x)=sum_(mu in bin j)C_mu(x)e((mu-j/X)x).
Then F_0=sum_j e(jx/X)B_j exactly. If B_j are absolutely continuous
with square-integrable derivatives, a fixed smooth cutoff gives

integral_J |F_0|^2 << sum_j integral_J*
 [|B_j|^2+X^2|B_j'|^2].                                 (C1)

Here J and J* have fixed lengths proportional to X and a positive
buffer. To verify the powers, put t=x/X and g_j(t)=eta(t)B_j(Xt).
Fourier transform sum_j e(jt)g_j(t). Cauchy at frequency xi, with
weights1+|xi-j|^2, uses the uniformly bounded sum
sum_j(1+|xi-j|^2)^-1. Plancherel bounds its squared norm by
C sum_j(||g_j||_2^2+||g_j'||_2^2). Multiplying by X returns (C1),
including cutoff derivatives. This is only an upper transfer.

Derivative energy cannot be discarded for arbitrary amplitudes:
B_j(Xt)=psi(t)e(-jt),1<=j<=M, makes the left side proportional to
M^2 X while the derivative-free sum is proportional to M X. Internal
bin modulation also cannot be discarded: two distinct frequencies in
one bin with opposite coefficients have zero coefficient sum but a
nonzero exponential sum. These are analytic controls, not actual
arithmetic counterexamples.

Here is the exact prefix used in the application. Keep the209 cutoff
D=floor(sqrt(ceil(6X))) and L_0=floor(ceil(6X)/(D+1)). Before rational
collision grouping, write the B arm as sum_(1<=ell<=L_0)1_(D ell<x)B_ell.
Its common integer prefix is
f_0(x)=min(L_0,max(0,ceil(x/D)-1)). At x=D ell this excludes label ell,
as required by the strict threshold. The A arm is label0 and is always
included; relabel0,...,L_0 as1,...,L_0+1 for the usual dyadic tree.

For an actual prefix with labels ell, group each fifth-product term by
its maximum original B-arm label, assigning the A-arm label0. All five
original strict conditions become one condition max ell_i<=f_0(x).
Set P_t=A+sum_(1<=ell<=t)B_ell for0<=t<=L_0 and P_-1=0. For a fixed
label interval Q=[a,b], its complete fifth-product polynomial is exactly
P_b^5-P_(a-1)^5. This also includes the A-only term when a=0.
Use J*=[X/3,4X], which has a fixed buffer around J. Extend each fixed
B_ell and A there by its same Fourier multiplier with h(x)=2sqrt(x)/sqrt(N),
without any selection indicator. These are smooth finite sums: take the
union of frequencies active anywhere on J*, whose denominators remain
bounded by max(D,4L_0). Products, collision grouping and complete fixed-Q
amplitudes therefore extend smoothly as well. Only the main representation
on J is used; no shell-tail assertion outside J is silently imported.
Thus no independent fivefold prefix decomposition is required. A prefix
has at most O(log L_0) canonical dyadic intervals Q in its label order.
For F_Q denoting the COMPLETE smooth maximum-label interval sum, pointwise
Cauchy and removal of selected-domain indicators give

integral_J |F_0|^2 << log(2L_0) sum_Q integral_J |F_Q|^2
 << log(2L_0) sum_(Q,j) integral_J*
 (|B_(Q,j)|^2+X^2|B_(Q,j)'|^2).                          (C2)

Fixed A-only terms can be included as label0. No distributional derivative
of the sharp prefix is taken. C2 retains the full dyadic interval energy;
it does not replace that energy by an unmasked sum that may cancel. For
example two equal and opposite label amplitudes have zero full sum but a
nonzero singleton interval energy. The actual joint signed energy at
scale G is a new unproved sufficient input, not a consequence of the
already-safe exact-frequency energy. The isolated task receives the
transfer statement without this proof; a separate analyst prices the
actual arithmetic input and any needed enlarged-window conventions.

### B. Differencing and its positive diagonal

The finite shift identity and Cauchy give the standard exact inequality

|F(R)|^2 << (N/L) [D+S_L(R)],                            (C3)

with a fixed support enlargement constant. The bracket is nonnegative:
D+S_L=(1/L)sum_m |sum_(0<=j<L)u_(m+j)|^2. Counting each original term
L times and using Cauchy over O(N+L) starting indices proves C3 directly.
No unweighted exponent-pair theorem is being applied to c_n.

Using (D+S_L)^5<=16[D^5+(S_L)_+^5] gives

integral_I |F|^10 << T N^(5/2+epsilon)L^-5
                   +(N/L)^5 integral_I (S_L)_+^5.        (C4)

Consequently a sufficient moment certificate at U requires payment of
the displayed diagonal by taking

L >= T^(-18/325)N^(3/5),                                (C5)

up to adjustable epsilon losses, and the actual signed input

integral_I (S_L)_+^5 << T^(83/65+epsilon)L^5 N^(-11/2).   (C6)

The equality scale in C5 is a positive power of T throughout the band
and is o(N), so integer rounding and L<=delta N cause no power problem.
C5 is necessary to this separated positive certificate, not to the
true moment: negative S_L may cancel D in the original bracket. No such
cancellation is assumed when C4 is used. C6 remains unproved.

### C. Why an unweighted cumulative error is not enough

For a fixed shift h define d_h(n)=c_(n+h)c_n. Suppose a chosen continuous
main term M_h(y) and cumulative remainder satisfy

sum_(N<n<=y)d_h(n)=M_h(y)+E_h(y),
sup_(N<=y<=4N)|E_h(y)|<=mathcal E_h.

The oscillatory coefficient in the corresponding correlation is
g_h(t)=f(t+h)f(t)e(R(sqrt(t+h)-sqrt(t))). On its smooth compact support,

||g_h||_infinity+integral |g_h'(t)|dt
 << N^-3/2 (1+T h/sqrt(N)).                             (C7)

Its phase derivative has magnitude comparable to T h N^-3/2 on the
common positive subinterval. Because the real amplitude and its phase
derivative are orthogonal real and imaginary components of g_h', the
variation is also at least c T h N^-2 on that subinterval. Endpoint
terms are included in the upper norm; exterior smooth values vanish.
Absolute Abel transfer therefore supplies an error bound with cost
O(mathcal E_h N^-3/2(1+T h/sqrt(N))). It cannot simply supply
O(mathcal E_h N^-3/2) without an oscillatory remainder estimate.

Every r2(n) is in4Z, so |c_n|>=4-pi and
|d_h(n)|>=(4-pi)^2. The continuous main term has no jumps. Taking
one-sided limits at any interior integer shows
mathcal E_h>=(4-pi)^2/2. This lower bound concerns the size of an
admissible UNWEIGHTED cumulative-error envelope, not the oscillatory
correlation. It holds for every h in the chosen range.

Define the rejected positive pointwise certificate precisely: retain the
positive term (N/L)D in C3, assign zero cost to the main-term contribution,
and sum the absolute Abel remainder costs. No negative main term or
remainder cancellation against D is credited. This optimistic certificate
has, apart from fixed
constants and arbitrary small losses, the two unavoidable budget terms

N^(1/2)/L,       T L/N.                                 (C8)

The first is the exact diagonal contribution; the second follows by
summing h~L with positive Fejer weights and the constant lower bound on
mathcal E_h. For both costs to be <=T^(2b) one would need

N^(1/2)T^(-2b) <= L <= N T^(2b-1),
and hence N >= T^(2-8b)=T^(318/325).                     (C9)

The required band ends at T^(242/325). With no trivial cap, the product
of the two costs also yields a best norm-certificate exponent at least
1/4-alpha/8, exceeding b by at least19/650 on the required closed band.
This is a lower bound for the computed positive certificate only.

We may further GRANT an error-only cap by the coefficient absolute bound.
This is an optimistic extra allowance, not a claimed upper bound on the
remainder after subtracting a nonzero main term. Even granting it does
not repair the shortcut. Its optimistic accumulated
budget has scale min(T L/N,N^(1/2)); the transition is at
L comparable to N^(3/2)/T. Below that transition C8--C9 apply; above it
the capped term N^(1/2) exceeds T^(2b) at every fixed interior
alpha>4b. The centered coefficient absolute bound has the same lower
power on a positive subinterval, so this cap is not smaller in the
specified data-only calculation. This does not preclude a smaller
correlation obtained by using its signs. A shift-dependent error bound
cannot remove the constant envelope floor without using a discontinuous
main term that already retains the missing atomic arithmetic.

## 4. First unproved step

The complete signed bin energy in C2 or the actual signed shift aggregate
in C6 must still be estimated at its stated scale. The Abel calculation
rules out only a transfer using uniform cumulative error and absolute
variation. It does not lower-bound the actual correlations, invalidate
differencing with oscillatory inputs, or establish a full arithmetic
no-go. Neither C1 nor C3 is itself a gain toward the final theorem.

## 5. Controls and outcomes

Both costs in the inherited tenth moment remain in force; no V^-2 term
or bulk deficit is erased. Smooth derivative control, internal bin phases,
maximum-label prefix intervals and their entire energy are all explicit.
Generic analytic cancellation examples test only the transfer lemma.
Centered atomic jumps provide the actual data for the Abel-envelope
floor. Real endpoints, integer shift rounding, support overlap and the
strict open scale band have their stated buffers. All reported lower
bounds apply to a certificate or envelope, never the signed moment.
Sharp reconstruction and the full quarter scope remain as in208--209.

## 6. Exact dependencies and provenance

protocol.md; frozen210 strategy and active manifest; closed209 synthesis,
actual_tenth_high_values.md and independent_high_values_review.md;
signed_fifth_convolution.md and independent_rational_tenth_review.md;
reviewed208 conductor_bandlimited_strategy.md; accepted204 complete
large-values kernel. The shift identity, elementary Abel variation and
Fourier/Sobolev transfer above are derived directly. No new external
theorem is imported. The conductor communicated the centered atom floor
and compatibility exponent to the shifted-correlation analyst after that
analyst independently obtained the phase-variation cost. Maximum-label
grouping was separately reached by the rational analyst.

## 7. Recommended state effect

Retain after independent review as scoped method evidence, without
promoting either unproved arithmetic input. If neither attack supplies a
complete gain, close with an identity State Patch and use the scheduled211
strategy/current-literature review to assess these fully costed residuals.
Full quarter, original K10 and all M1/M2 parents stay open.
