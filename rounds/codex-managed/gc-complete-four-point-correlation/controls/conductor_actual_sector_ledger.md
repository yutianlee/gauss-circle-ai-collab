# Round212 conductor: actual safe sectors and a sharp small-phase control

Campaign:gc-complete-four-point-correlation. Date:2026-09-28.
Graph SHA256:4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Conductor analytical work; candidate evidence pending independent review.
No new external theorem or mathematical numerical experiment.

## 1. Result

The actual repeated-shift sector h=k and the complete small-phase sector
Thk/N^(3/2)<=1 are target-safe without a density hypothesis. Moreover,
on fixed interior scales above N=T^(2/3), the actual small-phase mass
supplies a lower bound of order N^(5/2)/(T L K), not merely a lower bound
on an absolute upper certificate. It approaches the target power at the
upper band edge: the actual small-phase sector has no uniform fixed power
saving below T^(4b) over the whole open band. This does not identify a
smooth-density main term or exclude an o(T^(4b)) bound at a moving edge.
It is consistent with the conjectured A4 bound.

Separately, local interval discrepancy would reduce the global Abel loss.
The required arithmetic statement is stronger than a global prefix bound
and is not proved here. A local square-root input would pay the band at
b=83/650; the complete actual estimate remains open.

## 2. Exact statement and hypotheses

Use the frozen212 actual s_n=r2(n)g_N(n)e(Rsqrt(n)), D_(h,k) and A4,
with g_N(t)=(t/N)^(-3/4)Psi(sqrt(t/T))v(t/N), real nonzero fixed smooth
v supported in[1,4], Psi(0)=1, real R in I and b=83/650. Write

    U=N^(3/2)/T, Lambda_(h,k)=hk/U,
    L=max(2,ceil(N^(1/2)T^(-2b))),
    K=max(2,ceil(N T^(-4b))).

The upper sector bounds hold uniformly throughout the whole required band.
For the actual lower control fix alpha0>2/3 and alpha1<1-2b with
alpha0<=alpha1 and restrict T^alpha0<=N<=T^alpha1. Constants may depend
on those margins and on the fixed nonzero mask. Then for sufficiently
large T, uniformly in R in I,

    A4 >= c N^(5/2)/(T L K) >= c' N T^(6b-1).            (R212.1)

The same lower bound holds for the small-phase sector alone, because the
proof uses only a square box with hk<=U. This lower bound concerns A4,
which already has a modulus per complete
n-correlation. It is not a lower bound for the original signed wave or
circle discrepancy and does not refute their target bounds.

## 3. Proof and complete powers

### A. Pay the repeated and small-product sectors

The actual divisor envelope gives |D_(h,k)|<<N T^epsilon for every
allowed shift. Since K>=L, at most L-1 pairs have h=k. Their contribution
to A4 is at most N T^epsilon/K<=T^(4b+epsilon).

If U<1, no positive integer pair satisfies hk<=U. If U>=1, the complete
count, even without the rectangular restriction, is
sum_(h<=U)floor(U/h)<<U log(2U). Thus all hk<=U contribute at most

    T^epsilon N U/(L K)
       <<T^epsilon N T^(6b-1)<=T^(4b+epsilon).

The overlap of these two safe sectors may be assigned once; summing both
upper bounds is harmless. Every remaining pair has h!=k and Lambda>1.
These estimates use actual r2 coefficients and no smooth main density.

### B. Nonoscillatory actual mass in a small square shift box

Put a_n=r2(n)|g_N(n)| and zero extend. It is nonnegative, supported in an
integer interval of length M<=3N+2, and sum_n a_n>=cN for large T.
Indeed a fixed interior interval [u1,u2] of the nonzero mask has |v|>=c;
Psi(sqrt(t/T)) tends uniformly to1 since N/T<=T^-2b. The elementary
unit-square cover of a disk gives sum_(n<=x)r2(n)=pi x+O(sqrt(x)+1).
Taking the difference at u1N,u2N yields the required positive mass.
Only this elementary area error is used, not a conjectural circle bound.
Also max a_n<<N^epsilon and sum a_n^4<<N^(1+epsilon).

For an integer Q>=2 define w_Q(j)=(1-|j|/Q)_+ and

    C_(h,k)=sum_n a_n a_(n+h)a_(n+k)a_(n+h+k),
    B_Q=Q^-2 sum_(|h|<Q,|k|<Q)w_Q(h)w_Q(k)C_(h,k).

For each k, set z_n=a_n a_(n+k). The exact moving-sum identity and
Cauchy, with at most M+Q starting indices, give

    Q^-1 sum_h w_Q(h)sum_n z_n z_(n+h)
       =Q^-2 sum_x (sum_(j=0)^(Q-1)z_(x+j))^2
       >= (sum_n z_n)^2/(M+Q).

Average this inequality in k using w_Q(k)/Q, whose total mass is1, and
apply Jensen. Apply the same moving-sum identity once more to a_n:

    B_Q >= (M+Q)^-1[Q^-1sum_k w_Q(k)sum_n a_n a_(n+k)]^2
         >= (sum_n a_n)^4/(M+Q)^3 >= cN                 (R212.2)

provided Q<=N. All sums are finite and no periodic extension is used.
The h=0 or k=0 axes contribute at most O(N^(1+epsilon)/Q), by Holder
and sum a_n^4. On any Q growing by a fixed positive power of T, take a
sufficiently small divisor epsilon: the axes are o(N).

Changing the sign of h or k is a reindexing of C_(h,k), so the four
strict quadrants have equal mass. Hence (R212.2), after removing axes,
implies

    sum_(1<=h<Q,1<=k<Q)w_Q(h)w_Q(k)C_(h,k)>=c N Q^2.  (R212.3)

This is a proved actual coefficient mass bound, not an assumed
four-point asymptotic. It remains true despite local residue obstructions.

### C. Restore the actual small phase and possible sign changes of v

Choose fixed sufficiently small eta>0 and
Q=floor(eta sqrt(U)). Throughout the fixed interior range in Section2,
Q grows by a uniform positive power of T, Q^2 is comparable to U,
and Q<=L<=K for large T. In fact

    sqrt(U)/L << N^(1/4)T^(2b-1/2)
                   <=T^((6b-1)/4),

which tends to zero because b<1/6. Q<=N also holds.

On the support n>=N, the exact second-difference identity is

    phi_(h,k)(n)=R integral_0^h integral_0^k
                         (-1/4)(n+u+v)^(-3/2)dv du.

For h,k<Q, its modulus is at most C TQ^2/N^(3/2)<=C eta^2. Choose
eta so that cos(2pi phi)>=3/4 uniformly over the full R-window.

If the four real g_N factors have nonnegative product, the real part of
the corresponding summand is at least3/4 of its absolute amplitude.
If their product is negative, continuity gives a zero of g_N between
the first and last argument. Since ||g_N'||_infinity<<N^-1, all four
values then have modulus O(Q/N). Their product is O((Q/N)^4).
The actual coefficient product is at most N^epsilon, so summing every
possibly negative term gives the uniform error O(N^(1+epsilon)(Q/N)^4).
Therefore

    Re D_(h,k)>= (3/4)C_(h,k)
                          -O(N^(1+epsilon)(Q/N)^4).    (R212.4)

Since Q/N tends to zero by a fixed power, its weighted sum over the
positive square box is negligible relative to (R212.3). Positivity of
the weights and |D|>=Re D yield

    sum_(h<Q,k<Q)|D_(h,k)|>=cNQ^2>=cNU.

This proves (R212.1). It does not require the mask itself to be globally
nonnegative. The same argument does not lower-bound a signed sum across
different h,k phases outside this small box.

At N=T^alpha its exponent is alpha+6b-1. The target exponent is4b;
their gap is1-2b-alpha, positive at each fixed interior scale and tending
to zero toward the upper edge. For any proposed uniform fixed saving
delta>0 below4b, choose one fixed alpha within delta of the upper edge
and above2/3; the proved lower bound contradicts that saving. This is a
power statement only. It does not identify a smooth-density main term
and does not exclude an o(T^(4b)) estimate at a moving exact edge.

### D. Independent local-discrepancy transfer comparison

Suppose a genuine smooth mean mu_(h,k)(t) satisfies scaled derivative
bounds T^epsilon N^-j, and the actual error measure
dE=sum_n a_(h,k)(n)delta_n-mu_(h,k)(t)dt has every local prefix bounded
by T^epsilon N^eta ell^nu on cells of length ell=N/(1+Lambda).
Partition the full support into O(1+Lambda) adjacent real cells, with
all but the last of length ell. Boundary atoms are assigned once by
(u,v] conventions. Each cell's summation-by-parts boundary term is
retained, and the variation of W e(phi) there is O(1), since
||W'||<<N^-1 and |phi'|<<Lambda/N. Consequently

    |D-integral mu W e(phi)|
       << T^epsilon N^(eta+nu)(1+Lambda)^(1-nu).        (R212.5)

This argument requires the prefix input on each cell, not just at cell
endpoints. Arbitrary over-refinement is not free: the O(1+Lambda) cell
count is part of the hypothesis when a preselected partition is used.

The smooth mean is paid by the full small-product calculation of211,
with mu included in the amplitude. Since LK~N^(3/2)T^-6b,
Lambda_max~T^(1-6b), the full averaged remainder in(R212.5) is at most

    T^epsilon N^(eta+nu) T^((1-6b)(1-nu)).             (R212.6)

For 0<=nu<=1 and eta>=0 the worst power is at the upper N edge. The
displayed certificate pays the complete band if

    b >= (1+eta)/(10-4nu+2eta).                        (R212.7)

For nu=1/2,eta=0 this requires b>=1/8. At b=83/650 the remainder
cost is at most T^(1-4b+epsilon)=T^(159/325+epsilon), below the target
T^(166/325) by7/325. This is a different arithmetic hypothesis from
the global square-root error that failed in211. The proof of a local
input, even on only the non-safe shifts, remains missing. No actual
arithmetic theorem is inferred from(R212.5)--(R212.7).

## 4. First doubtful or unproved step

The complete A4 upper bound is unproved on the remaining oscillatory
shifts. In the localized route the first missing input is a genuine
uniform short-interval density and error estimate, or an adequate
average replacing it. The lower control uses actual mass but proves
only the size of an already safe contribution; it does not solve the
remaining signed arithmetic cancellation.

## 5. Controls and outcomes

Actual r2 mass follows from an elementary geometric first moment and its
divisor envelope. Finite Fejer identities include all axes before they
are bounded; no density is presumed. Small-phase rounding and the strict
fixed-interior restriction ensure the axis error is negligible. The
possible sign changes of the real smooth mask are explicitly paid.
All h=k and small products are retained and bounded in the original A4.
Local boundary atoms, partial prefixes, number of cells, mean derivatives
and the whole shift rectangle are required by the conditional transfer.
No numerical experiment was used. This is not a circle-error lower bound.

## 6. Dependencies and provenance

Read protocol.md, current graph/manifest, frozen212 strategy, the closed211
checkpoint, its conductor_two_stage_strategy.md and independent review.
The actual small-phase lower argument and the initial local transfer
calculation were developed by the conductor before seeing any sibling
report. Subsequent interim messages confirmed the elementary safe-sector
prices and the isolated local-transfer criterion; neither is evidence
for the still-open arithmetic input. Exact final claims require the
separate same-round review. No primary theorem beyond inherited divisor
growth is imported; the elementary disk-cover estimate is explained above.

## 7. Recommended state effect

Retain after independent review as actual sector control and a fully paid
conditional local transfer. No complete target, moment, pointwise exponent
or M1/M2 parent is promoted. The lower control excludes a uniform fixed
power improvement on the small-phase sector across the whole open band,
while leaving the selected upper bound possible. Choose a successor only
from closed212 evidence, preserving
the full quarter goal and the scheduled214 broad review.
