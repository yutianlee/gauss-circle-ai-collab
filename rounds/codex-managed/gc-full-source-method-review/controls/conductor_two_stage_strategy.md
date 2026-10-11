# Round211 conductor: a complete two-stage correlation interface

Campaign: gc-full-source-method-review. Date: 2026-09-28.
Conductor analytic derivation; candidate strategy evidence pending review.
Graph SHA256: 4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
No new external theorem and no mathematical numerical experiment.

## 1. Result

Two complete finite differencing steps give a sufficient pointwise input
involving the average absolute value of actual four-point oscillatory
correlations. At the already reviewed milestone, both differencing
diagonals and the complete smooth correlation main terms can be paid.
The remaining oscillatory four-point remainder is unproved.

Unlike the round210 one-step positive Abel certificate, this two-step
certificate can accommodate a constant unweighted correlation-error
envelope. A square-root unweighted error still loses too much variation on
part of the band. A square-root *oscillatory* remainder would be sufficient,
but no such arithmetic theorem is proved or imported here. The distinction
is the proposed reason for a different attack, not evidence of its success.

## 2. Exact statement and hypotheses

Let T>=2, R lie in a fixed positive compact multiple of T, and
T^(4b)<N<T^(1-2b), with fixed0<b<1/6. For the concrete milestone take
b=83/650, so the band is T^(166/325)<N<T^(242/325).
Set

    g_N(t)=(t/N)^(-3/4)Psi(sqrt(t/T))v(t/N),
    s_n(R)=c_n g_N(n)e(Rsqrt(n)),
    F_c(R)=N^(-3/4) sum_n s_n(R).

Here v is the fixed real smooth mask supported in[1,4], Psi is the fixed
mollifier transform, and c_n=r2(n) for the original route. The same finite
calculation also holds for c_n=r2(n)-pi, but that is an alternative
sufficient centered pointwise route, not a moment equivalence. Every
sequence is zero extended. All coefficients have the divisor envelope
|c_n|<<N^epsilon on the support; g_N has uniform scaled derivatives.

For integers2<=L,K<=delta N, with fixed small delta>0, define

    C_h(R)=sum_n s_(n+h)(R) conjugate(s_n(R)),
    D_(h,k)(R)=sum_n s_(n+h+k)(R) conjugate(s_(n+k)(R))
                          conjugate(s_(n+h)(R)) s_n(R),
    A4(R;L,K)=(1/(LK)) sum_(1<=h<L,1<=k<K)|D_(h,k)(R)|.

All overlaps and shift complements are those of the zero-extended sequence.
This definition includes repeated factors when h=k. The modulus is outside
the complete n-sum, before the shift average. It is not a termwise divisor
majorant. A4 is nonnegative and is a stronger sufficient input than the
original pointwise theorem.

## 3. Proof and restored powers

### 3.1 Two finite Fejer inequalities

The moving-sum identity and Cauchy on O(N+L) starting indices give

    |sum_n s_n|^2 << N^2 T^epsilon/L
                        +(N/L) sum_(1<=h<L)|C_h|.

Squaring and applying Cauchy to the h-sum gives

    |sum_n s_n|^4 << N^4 T^epsilon/L^2
                        +(N^2/L) sum_(1<=h<L)|C_h|^2.

Apply the same finite moving-sum inequality, now with length K, to
t_n=s_(n+h)conjugate(s_n). Its squared-coefficient diagonal is
O(N T^epsilon), uniformly in h. Consequently

    |C_h|^2 << N^2 T^epsilon/K
                        +(N/K)sum_(1<=k<K)|D_(h,k)|.

Substitution and division by N^3 prove the complete inequality

    |F_c(R)|^4 << T^epsilon[N/L^2+N/K+A4(R;L,K)].          (C1)

The harmless Fejer weights are at most one and were discarded only for an
upper bound. No unestimated h>=L or k>=K contribution remains: their entire
cost is already contained in the two moving-sum factors. C1 is not an
estimate of A4 and does not imply that the correlations are small.

Choose

    L=max(2,ceil(N^(1/2)T^(-2b))),
    K=max(2,ceil(N T^(-4b))).                              (C2)

Throughout the open band the unrounded quantities exceed1. Thus rounding
changes only fixed constants, LK is comparable to N^(3/2)T^(-6b), and
L,K=o(N) uniformly as T grows. Both diagonal prices in C1 are at most
T^(4b). The constraint L,K<=delta N therefore holds for sufficiently large
T depending on b and delta; bounded T is paid by the trivial finite sum.
The complete sufficient arithmetic target becomes

    sup_(R in I) A4(R;L,K) << T^(4b+epsilon)               (C3)

for every required dyadic N and the exact lengths(C2). Unlike a tenth
moment, this is a uniform pointwise shift-averaged four-point estimate.

### 3.2 Pay all smooth main terms before posing a remainder estimate

Write

    a_(h,k)(n)=c_n c_(n+h)c_(n+k)c_(n+h+k),
    W_(h,k)(t)=g_N(t)g_N(t+h)g_N(t+k)g_N(t+h+k),
    phi_(h,k)(t)=R[sqrt(t+h+k)-sqrt(t+k)-sqrt(t+h)+sqrt(t)].

Then D_(h,k)=sum_n a_(h,k)(n)W_(h,k)(n)e(phi_(h,k)(n))
exactly. If actual constants rho_(h,k) with |rho_(h,k)|<<T^epsilon are
available, define (without asserting any small remainder)

    I_(h,k)=integral_R W_(h,k)(t)e(phi_(h,k)(t))dt,
    R_(h,k)=D_(h,k)-rho_(h,k) I_(h,k).

Any such rho must be supplied or derived in a future arithmetic proof;
no singular-series formula is presumed here. Taking rho=0 is permissible
but simply leaves the original complete D as the remainder.

The exact finite-difference integral formula is

    phi'_(h,k)(t)=R integral_0^h integral_0^k
                          (3/8)(t+u+v)^(-5/2)dv du.

On the support it is positive and comparable to T h k N^(-5/2).
Higher derivatives have the corresponding scaled bounds uniformly for
h,k<=delta N. The amplitude is smooth with derivatives O_j(N^-j),
including every exterior overlap boundary. Continuous integration by parts,
after scaling t=N u, therefore gives for every fixed A

    |I_(h,k)| <<_A N(1+T h k/N^(3/2))^(-A).              (C4)

This is a continuous integral statement, not a discrete first-derivative
bound for the arithmetic coefficients. Put c=T/N^(3/2). For A>1,
monotonicity and integration from zero give

    sum_(k>=1)(1+c h k)^(-A) <= integral_0^infinity
                (1+c h t)^(-A)dt <<1/(c h).

Summing h<L yields O(c^-1 log(2L)) for the complete double sum. Hence

    (1/(LK))sum_(h<L,k<K)|rho_(h,k)I_(h,k)|
       << T^epsilon N^(5/2)/(T L K)
       << T^epsilon N T^(6b-1) <=T^(4b+epsilon),           (C5)

because N<=T^(1-2b). Small products hk, including h=k=1, are paid in
this calculation; none is deleted as a supposedly rare exception.
Thus another complete sufficient input is

    sup_(R in I) (1/(LK))sum_(h<L,k<K)|R_(h,k)(R)|
              << T^(4b+epsilon),                         (C6)

with genuinely established rho if nonzero means are subtracted. The
original r2 coefficient, the complete n-overlap, all shifts and the displaced
R-window must be retained. An estimate on a selected shift sector does not
prove C6 unless its complement is paid.

### 3.3 What an unweighted source would still cost

For comparison only, suppose an actual unweighted cumulative description
on the whole overlap is

    sum_(N<n<=y) a_(h,k)(n)=rho_(h,k)(y-N)+E_(h,k)(y),
    sup_y|E_(h,k)(y)|<=E_(h,k).

Real prefix endpoints are part of this hypothesis. Abel summation and the
derivative just computed give

    |R_(h,k)(R)| << E_(h,k)[1+T h k/N^(3/2)].             (C7)

There is no extra N^-3/2 amplitude here: g_N is normalized to size1.
Consequently a uniform envelope E_* supplies C6 if

    E_*[1+T L K/N^(3/2)] << T^(4b+epsilon).

Since b<1/6 and(C2) holds, a sufficient power condition is

    E_* << T^(10b-1+epsilon).                            (C8)

For b=83/650 this is T^(18/65). A uniform unweighted square-root error
N^(1/2) would meet C8 only for N<=T^(36/65); at the upper required
scale its certificate misses by T^(31/325). These are failed upper
certificate powers, not lower bounds on actual remainders.

In contrast, a uniform *oscillatory* remainder bound
|R_(h,k)(R)|<<N^(1/2)T^epsilon would imply C6 on the whole band whenever
b>=1/10, since N^(1/2)<=T^((1-2b)/2)<=T^(4b). This is a conditional
comparison, not a sourced or proved four-point estimate. It identifies the
phase-variation loss that the next arithmetic mechanism must avoid.

For centered coefficients every four-point atom has modulus at least
(4-pi)^4. An unweighted error against a continuous main term has a constant
floor on real prefixes. That floor is compatible with C8 at the concrete
b>1/10, unlike round210's one-step contradiction. As b decreases below
1/10, this particular constant-envelope absolute-Abel route fails: on a
common sign-definite interior interval, Psi(0)=1 gives W_(h,k) bounded below
for sufficiently small delta. Its real amplitude and imaginary phase
derivative imply an actual variation floor comparable to c h k. Summing
h comparable to L and k comparable to K (including bounded lengths by their
single positive shifts) gives a certificate price at least cLK, comparable
to T^(1-6b)>T^(4b). This is a lower bound on that specified absolute-envelope
certificate, not a necessity inferred merely from the sufficient C8 and not
a no-go for C3, C6 or the quarter theorem.

### 3.4 Complex blocks, complements and full-goal limits

The original real block is H_N=Re(e(-3/8)F_(r2)). A bound for F_(r2)
therefore suffices directly for H_N. Where a comparison needs the reverse
local supremum direction, choose a fixed smooth frequency multiplier chi
supported in(1/2,3), equal to1 on[1,2]. Its rescaled convolution kernel has
L1 norm O(1) and Schwartz tails at scale N^-1/2. Positive-frequency
projection gives exactly

    F_(r2)=2e(3/8) chi(D/sqrt(N))H_N.

On a compact positive R-window, the enlarged positive window contains a
fixed buffer comparable to T. Off-window convolution costs only the global
coefficient bound N^(1/4+epsilon) times an arbitrarily large inverse power
of T sqrt(N). Thus the reviewed real-block supremum controls its complex
counterpart locally, with no power loss, when the required larger window is
included. No pointwise Hilbert-transform L-infinity assertion is being used.

At the concrete b the closed208 bridge pays the ranges N<=T^(4b) and
N>=T^(1-2b), their equality endpoints, the singleton, the entire infinite
tail and the sharp smoothing error. A proof of C3 or C6 on the complete
middle band would therefore give P(X)<<X^(1/4+b/2+epsilon)
=X^(102/325+epsilon). This is a pointwise route; no claim is made that it
proves the original tenth moment.

One fixed-b instance of C3 or C6, including the proposed square-root
oscillatory remainder input, does not establish the full quarter theorem.
A hierarchy with b tending to zero and complete complements would suffice;
so could a single sufficiently strong uniform four-point theorem, for
example A4<<T^epsilon at L,K comparable to N in C1. An independent complete
M1/M2 proof is another route. No such stronger result is established here,
and the full target is not redefined to this milestone.

## 4. First doubtful or unproved step

The actual shift-average C3 is unproved. After a justified main term, C6 is
equally sufficient and also unproved. No theorem about unweighted prefixes,
fixed shift systems, logarithmic savings or independent random coefficients
is silently used as C6. C7--C8 are merely a cost test for possible sources.
The new finite algebra and comparison explain a potential change of method;
they provide no accepted moment or pointwise saving.

## 5. Controls and outcomes

Both finite Fejer identities retain every shift and zero-extended endpoint;
all diagonal powers, the N^-3 physical normalization and integer rounding
are displayed. Repeated factors h=k cause no exceptional deletion. The full
small-product main contribution is summed explicitly. Continuous and
discrete oscillation are distinguished. Centered atom floors apply only to
unweighted envelopes; no actual signed lower bound is asserted. Positive
frequency projection uses a smooth annular multiplier and paid window tails.
All full-quarter and M1/M2 parents stay open. No experiment was run.

## 6. Dependencies and provenance

Read: protocol.md; current graph and frozen211 strategy; closed210 synthesis,
actual_shifted_correlations.md and its independent review; closed208
conductor_bandlimited_strategy.md and strategy checkpoint; closed209 complete
high-value ledger for comparison. The two-stage finite algebra and derivative
calculations above are independent conductor work, not taken from any current
subagent report. The original isolated211 derivation is a different task and
does not receive this ledger before completion. No new external source is
needed for C1--C8. Source tasks separately audit actual literature applicability.

## 7. Recommended state effect

Retain after independent review as a fully costed new sufficient interface.
Do not promote C3, C6 or an exponent. If the source comparisons remain weaker,
consider this complete averaged four-point problem for the next bounded
attack only after211 closes. Preserve the actual signed tenth gate as an
alternative, all independent M1/M2 routes and the original full-quarter goal.
