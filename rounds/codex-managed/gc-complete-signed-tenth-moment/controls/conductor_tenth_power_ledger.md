# Round209 conductor: complete tenth-moment diagnostics

Campaign: gc-complete-signed-tenth-moment. Date: 2026-09-27.
Role: conductor analytic derivation; candidate evidence pending independent review.
Graph SHA256: 4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
All mathematics below is analytical, with no numerical experiments.

## 1. Result

The selected complete tenth-moment gate has two distinct deficiencies in
the available distribution certificate. Even hypothetical removal of its
V^-2 term does not suffice over the entire required band. An explicit
two-parameter sufficient replacement is quantified below; it remains
unproved for the actual coefficients. The positive close-frequency
obstruction also persists at EVERY fixed interior exponent of the newly
selected band, after exact resonances are removed. Neither fact is a
lower bound for the actual signed moment.

## 2. Exact statement and hypotheses

Use the actual H_N and centered shell Z_N, real T>=2, I, J, fixed smooth
nonnegative partition v and mollifier Psi from the reviewed round-208
bridge. Put N=T^alpha, b=83/650, q=136/13 and
omega=min(alpha/4,beta,(1-alpha)/2),
beta=2theta_LY-1/2=(50sqrt(1717)-297)/13762.
This accepted value satisfies b<beta<1/6. In particular 4beta<1-2beta,
and both omega breakpoints lie inside the required band. This specific
range, not merely the abstract condition b<min(beta,1/6), is used below.
The entire required open band is 4b<alpha<1-2b. Set

U=T^(10b)N^(-1/2),
D(V)=measure{R in I: |H_N(R)|>V},
W=T^(omega+epsilon).

The reviewed inputs are D(V)<<T N^(-1/2)V^-2 for V>0 and
D(V)<<V^-2+T V^-q for V>=1, with arbitrarily small epsilon losses,
and the supremum W. Required moment M10<<U is transferred to the
complete K10 target and pointwise102/325 only by the reviewed208 bridge.
All comparisons below concern sufficient certificates, not necessary
conditions for a true pointwise estimate.

## 3. Derivation

### The two missing powers

The reviewed variance/distribution intersection yields

M10 << T^epsilon [T N^(-3/110)+T^(8omega)].                 (C1)

Relative to U their excess exponents are

dA=1-10b+(26/55)alpha,
dB=8omega-10b+alpha/2.                                    (C2)

The independent208 review already establishes dB>dA throughout the
required band and max dB=7beta-101/130, at alpha=1-2beta.
However deleting the second summand in (C1) leaves a positive excess
dA whenever

alpha>(10b-1)55/26=99/169.                                (C3)

This lies strictly inside the required band. At its upper endpoint,
dA=1342/17875>0. Thus removal of the full Gram/localization term alone
does not prove the frozen target using the unchanged remaining input.
This statement is about that particular certificate; it does not prove
that an arithmetic proof must improve two separately identifiable terms.

The variance already pays low amplitudes V<=L=T^(9/260), because

integral_(|H_N|<=L) |H_N|^10 <= L^8 M2
 << T^(1+72/260)N^-1/2=U.                                (C4)

For an exact high-level decomposition, do not omit the boundary term:

integral_(|H_N|>L)|H_N|^10
 =L^10 D(L)+10 integral_L^infinity V^9 D(V)dV.

The boundary is paid by the same variance calculation. Consequently
the complete target is equivalent, up to constants and epsilon losses,
to the corresponding bound on this nonnegative high-level integral.
This is a precise outstanding estimate, not a new distribution theorem.

### A costed sufficient two-parameter improvement

Suppose, solely as an explicit hypothesis, that for all V>=1 the actual
distribution admits

D(V)<<T^epsilon[T^(-sigma)V^-2 + T N^(-lambda)V^-q],       (C5)

with 0<=lambda<=1/2 and sigma>=0, together with the unchanged variance
and W. Intersect with variance at
V0=N^((1/2-lambda)/(q-2))>=1. Below V0 integrate variance down to0;
above V0 integrate both terms of (C5), retaining all endpoints. The
result, also valid if W<V0, is

M10 << T^epsilon[
 T N^(-3/110-(52/55)lambda)+T^(-sigma+8omega)].            (C6)

The first exponent follows from
-1/2+8(1/2-lambda)/(q-2)=-3/110-(52/55)lambda.
The V0 boundary terms agree. No subunit use of (C5) is made.
For all scales in the required band, the sufficient conditions are

lambda>=61/572,
sigma>=7beta-101/130.                                    (C7)

Indeed the first condition is the supremum of
(55/52)[26/55-(10b-1)/alpha], increasing in alpha, evaluated at
alpha=242/325. It equals (55/52)(61/605)=61/572.
The second is exactly the maximum of dB. These are conditions for this
chosen separable family of distribution bounds only. No claim of
necessity, availability, or ease of proving (C5) is made.

Alternatively, retaining lambda=0 but replacing q by q'>10, the first
integrated term is T N^(-(q'-10)/(2(q'-2))). It meets U over the whole
band precisely when the worst endpoint inequality
4alpha/(q'-2)<=10b-1 holds. A sufficient threshold is
q'>=574/45. The V^-2 contribution still remains and must be treated.
No new exponent pair or external large-value theorem is asserted.

### Local exact mass, with every non-pairing relation

For any nonnegative weights 0<=b_n<=C tau(n)n^-3/4 supported in [N,4N], put
A_d=sum_s b_(d s^2), with d squarefree. For any small eta>0,

A_d << N^(-3/4+eta) sqrt(N/d)
    = N^(-1/4+eta)d^-1/2, for d<=4N.

The bound includes the endpoint case with one admissible integer s,
since sqrt(N/d)>=1/2 there. Therefore
S=sum_d A_d^2 << N^(-1/2+2eta)log(2N).
The accepted exact-resonance kernel K1, applied to 2k labels, gives
the all-sign exact mass O_(k,epsilon)(N^(-k/2+epsilon)). It groups
labels by squarefree class, not just pairings, so all non-pairing
relations are included. For k=5 the exact tenth integral costs only
O(T N^(-5/2+epsilon)), smaller than U on the entire selected band.
This localization is also being independently derived by the isolated
task, without access to this proof or the historical kernel.

### A positive majorant cannot attain the new gate

On the selected band N/T tends to0 uniformly, so Psi(sqrt(n/T))>=1/2
on support for large T. Since v is positive on an interior subinterval,
the elementary disk-area count yields total positive coefficient mass
sum a_n >= c N^(1/4). Form all ordered five-root sums, with product
weights, and bin an interval of length O(sqrt(N)) into intervals of
length h/T. There are O(T sqrt(N)) bins. Weighted Cauchy shows that
the total product mass of close ordered pairs is at least c N^2/T.
Choose fixed h>0 with Re w_hat(xi)>c_w>0 for |xi|<=h, where w>=0
is a nonzero smooth fixed window. Subtract the ENTIRE exact mass just
bounded. Thus the full termwise absolute tenth expansion satisfies

A10 >= c N^2-C_epsilon T N^(-5/2+epsilon).                (C8)

For every fixed alpha in the required open band the second term is
negligible, and the ratio of the first term to U is

N^2/U=T^((5/2)(alpha-166/325)).                           (C9)

It is a positive power at every fixed interior alpha. Choosing epsilon
smaller than that power rules out a uniform U-sized bound for this
particular majorant. There is no uniform fixed margin as alpha tends
to the lower boundary. In particular no endpoint conclusion has been
smuggled into this comparison. Exact-frequency removal does not repair
the absolute estimate.

The same control applies after replacing r2(n) by r2(n)-pi in the
physical frequency coefficient, if that representation is used. Since
r2(n) belongs to4Z, |r2(n)-pi|>=4-pi>0 for every n. Absolute coefficient
mass on the positive v-subinterval is again at least c N^(1/4), and
the same divisor envelope bounds exact mass. Such centering can change
signed correlations; it does not improve this termwise absolute bound.
This last centering observation was communicated to the high-value
analyst after that analyst independently proposed the discrete mean split.

## 4. First unproved step

The actual signed high-value integral displayed after (C4), or an estimate strong
enough to imply it, remains unproved. Neither (C5) nor any positive
arithmetic saving in (C6) has been established. Close-frequency
majorant lower bounds cannot be used as lower bounds for M10, K10,
or cancellation after aggregation. Exact mass is harmless but does
not bound any nonzero-frequency remainder.

## 5. Controls and outcomes

Real endpoints and the full open scale band are retained; the already
safe endpoint scales belong to the208 complements. The high-level
layer-cake boundary L^10D(L) is included. (C5) is only used at V>=1.
All sign patterns and squarefree non-pairings enter the exact bound.
The band majorant uses actual coefficients, not an arbitrary array.
A displaced smooth continuum Fourier transform is rapidly small while
its positive close-pair majorant is large; thus deleting other signed
terms cannot give a signed lower bound. An independent explicit control
is requested from the isolated task. No mathematical experiments used.

## 6. Dependencies and exact artifacts

protocol.md; current209 frozen manifest and strategy; reviewed208
controls/conductor_bandlimited_strategy.md and its independent hierarchy
review; accepted204 complete-large-values kernel; reviewed206 sixth-power
ledger; proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md;
proofs/kernels/gc_physical_twelfth_moment_absolute_majorant_obstruction.md.
The graph and prior208 archive hashes were verified before launch.
No new external theorem or web source is imported.

## 7. Recommended state effect

Retain as complete-power and obstruction evidence after independent review.
No promotion of a recovered exact-mass variant or another moment identity
is proposed. If the arithmetic tasks prove no gain, use an identity State
Patch, retain all399 graph nodes and the proof draft, and record the exact
failed mechanisms. Do not call this a proof of the desired moment or of
the Gauss circle problem.
