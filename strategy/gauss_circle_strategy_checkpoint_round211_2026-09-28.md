# Strategy checkpoint after rounds208--210

Review round:211. Campaign:gc-full-source-method-review. Date:2026-09-28.
This records a conditional research decision; it is not a new graph theorem.
The pinned23September memo and the full quarter target remain in force.

## 1. Decision: a complete four-point arithmetic target

Select the complete shift-averaged four-point oscillatory correlation as
the candidate for the next bounded attack. Its finite two-stage transfer
and full powers have been independently reviewed. It is a sufficient
pointwise route; it is not equivalent to the previously selected tenth
moment. That signed moment remains an alternative open target.

Use T>=2, R in the full positive comparison window, b=83/650 and every
dyadic T^(166/325)<N<T^(242/325). With the actual fixed smooth functions,

    g_N(n)=(n/N)^(-3/4)Psi(sqrt(n/T))v(n/N),
    s_n=r2(n)g_N(n)e(Rsqrt(n)),
    L=max(2,ceil(N^(1/2)T^(-2b))),
    K=max(2,ceil(N T^(-4b))),
    D_(h,k)=sum_n s_(n+h+k)conjugate(s_(n+k))conjugate(s_(n+h))s_n,

the candidate is the complete uniform inequality

    sup_R (1/(LK))sum_(1<=h<L,1<=k<K)|D_(h,k)(R)|
                 << T^(166/325+epsilon).                         (S211)

All sequences are zero extended; every overlap, repeated factor h=k,
small shift product and real R endpoint is included. The modulus is
outside the full arithmetic n-sum. There is no unpriced shift complement.
The lengths obey L,K<=delta N for sufficiently large T; bounded T is
paid trivially. The primary coefficient is r2(n), not an arbitrary array
or a centered surrogate. A centered alternative needs its own complete
transfer and is not silently substituted.

Two finite Fejer inequalities and Cauchy give, for
F_N=N^(-3/4)sum_n s_n,

    |F_N|^4 << T^epsilon[N/L^2+N/K+A4],
    A4=(LK)^(-1)sum_(h,k)|D_(h,k)|.

The two diagonal terms are at most T^(4b). Thus (S211) would bound the
entire block by T^b. Closed208 supplies both complementary scale ranges,
the equality endpoints, singleton, infinite tail and smoothing error.
Full reconstruction would give P(X)<<X^(102/325+epsilon). No such gain
has been obtained. This fixed milestone is not the full quarter theorem.

## 2. Price the arithmetic remainder and the known barriers

If a proof genuinely supplies densities rho_(h,k)<<T^epsilon, write
D_(h,k)=rho_(h,k)I_(h,k)+R_(h,k), where I is the full smooth integral
with phase

    R[sqrt(t+h+k)-sqrt(t+k)-sqrt(t+h)+sqrt(t)].

Its derivative is R times the integral of (3/8)(t+u+v)^(-5/2) over
0<=u<=h,0<=v<=k. Repeated integration by parts therefore gives
|I_(h,k)|<<N(1+Thk/N^(3/2))^-A. Summing every small product gives

    (LK)^(-1)sum|rho I| << T^epsilon N^(5/2)/(T L K)
                          <=T^(4b+epsilon).

An averaged bound of the same size on the actual oscillatory R_(h,k)
is therefore sufficient. The densities and that bound are both unproved.
Choosing rho=0 is legal and leaves exactly (S211); it creates no saving.

An unweighted cumulative error E costs E[1+Thk/N^(3/2)] after Abel
summation. A uniform error certificate needs E<<T^(10b-1)=T^(18/65).
The conjectural square-root error N^(1/2) is not enough for that transfer
above N=T^(36/65), and loses T^(31/325) at the upper edge. In contrast,
a square-root bound on the already oscillatory remainder would suffice
throughout this band. This comparison is conditional, not a claimed
correlation theorem. It identifies precisely the phase-variation loss
that the next attack must avoid or improve by a proved average.

Round210's constant-error obstruction concerned a different one-stage
positive certificate. The two-stage route can accommodate a constant
unweighted envelope at this b; it does not prove such an envelope. Below
b=1/10 the centered constant-floor absolute-Abel certificate again fails.
All these failures concern specified positive upper certificates. None
is a lower bound on the actual signed correlation or circle discrepancy.

## 3. Current primary sources and complete costs

The review is bounded and current through27September2026 UTC. Full source
statements, versions, coefficients and independent checks are archived in
the211 source reports and reviews. No exhaustive literature claim is made.

| Audited source/interface | Complete restored consequence |
|---|---|
| [Bourgain1408.5794v2](https://arxiv.org/abs/1408.5794v2), Theorem6 | Its scalar exponent-pair theorem applies to the square-root phase after exact hyperbola splitting and residue-four handling. Both arms together cost T^kappa N^(lambda/2-1/4). No gain at the required band. |
| [Tao--Trudgian--Yang2501.16779v1](https://arxiv.org/abs/2501.16779v1), Theorem20 | The fixed model phase, partial intervals and current pairs are compatible with that same transfer. The named A/B/C/D and convex closure of the explicitly inventoried seeds lies in a proved invariant region and cannot beat the benchmark at alpha=7/10. This is not a theorem about every admissible pair. |
| [Wu1999](https://link.springer.com/article/10.1007/s006050050062), Theorem1 | Both real monomial exponents1/2 are legal. Actual product smoothing and the outer character can be retained. The balanced price T^((4K-2)/w)N^((K-k-1)/(2w)), K=2^k,w=20K-2k-14, has T exponent greater than1/5 and fails the target. |
| [Kowalski--Robert--Wu2007](https://ems.press/content/serial-article-files/38194), Proposition5 | Product-coefficient norms and smoothing separation cost O(1), but the first physical term is T^(1/8)N^(1/16). It is redundant against min(N^(1/4),(T/N)^(1/2)) on all1<=N<=T, before the stronger accepted cap. |

The statement-only derivation independently reproduces the full hyperbola
transfer, its exact cutoff and residuals. A formal pair would beat wave
threshold b precisely when 4kappa+2(1-2b)lambda<1+2b. A valid family
approaching(0,1/2) would suffice for quarter, but none is established.

The reviewed invariant region uses 2kappa+lambda>=8/9 and
kappa+2lambda>=25/18. It forces the scalar-hyperbola certificate exponent
at scale N=T^alpha to be at least7alpha/36. At alpha=7/10 this exceeds
both beta and b, while both elementary caps also exceed beta. The scope
is the listed seeds and maps, including explicitly optimistic grants for
screened Cushing/formal-D inputs; those grants are not imported theorems.

Primary metadata checks retain Li--Yang2308.14859v2 and the existing
repaired narrow graph application. Bourgain--Watt1709.04340v2 and
Dong--Robles--Zeindler2601.00292v2 remain withdrawn. The latter's missing
L^2 invalidates its advertised gain. Baier2605.01635v3,20July2026, is now
*Partial progress towards the large sieve for square moduli* and supersedes
the withdrawn2603.00768/2603.25814 manuscripts. Its modular roots do not
supply a theorem on the real phase R sqrt(dm). Numerical, friability,
almost-everywhere and modular screens supply no new uniform r2 estimate.

## 4. Preserve the full frontier and stop repeated certificates

The internal M1 HARD residual still includes every small t, not just t=1.
M1 SMOOTH is independent. M2 TOP, BAL, UNBAL and all endpoint quantifiers
remain open. GAR concerns only total active M1 and still needs M2. No
newly audited theorem closes or improves any of these parents.

The original tenth gate remains
integral_I|H_N|^10<<T^(83/65+epsilon)N^-1/2, equivalently the reviewed
signed shell gate T^(473/65+epsilon)N^-1/2. Its existing two-term bound
T N^-3/110+T^(8omega) is unchanged. Exact rational energy is already
safe; the complete signed off-diagonal is open. Generic bin estimates,
outer-absolute divisor CRT bounds and the one-step absolute error route
have been priced and are parked. Repeating them is not a new advance.

For the full target P(X)<<X^(1/4+epsilon), one needs a complete family
with b tending to zero, or a single stronger uniform theorem sufficient
for all those scales, or an independent full M1/M2 route. A sufficiently
strong four-point theorem at lengths comparable to N could in principle
do this; the fixed-b statement(S211) and the proposed square-root input
do not. No possible route is rejected merely because this milestone is
selected for the next bounded attempt.

## 5. Closure and successor constraint

Round211 closes only after final-hash seam reviews and the identity State
Patch validate. All399 graph nodes and proof-draft bytes remain unchanged.
The source exclusions and new complete sufficient interface are strategy
evidence, not accepted cancellation estimates.

Only after closure may212 be designed around(S211), allowing a different
complete gain if it has a fully paid bridge. Its first stress tests must
use actual arithmetic coefficients, small products, repeated shifts and
real parameter uniformity. Its exit must be a complete quantitative
estimate or a precise scoped obstruction, without promoting an unproved
four-point density. The next mandatory broad strategy/current-source
review is214 after211--213. This round used analysis, algebra and source
inspection; no mathematical numerical experiment was run.
