# Round 218 joint divisor kernel: complete attempt and quantitative diagnosis

## 1. Result

Campaign: `gc-complete-signed-radical-kernel`; task: `joint_divisor_kernel`.
Role: discovery, NONBLIND, selected-context only. Generated 2026-09-28
(Asia/Shanghai). Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
This is candidate evidence, not accepted mathematics.

The complete actual bound

    I12(T,floor(T^(2/5))) <= C_epsilon T^(29/25+epsilon)

is NOT proved. The joint divisor calculation does give a precise diagnosis
of the proposed dimension saving, with the original character, cosine
phases, displaced radius window, and every complement accounted for.

The elementary results established below are:

* Joint character Poisson summation has odd-quarter dual labels a/4,
  with coefficient (i/2)chi4(a), and stationary dual radius sqrt(a k).
  The actual cosine pairing produces an odd sine shell, not a positive
  centered bump. This cancellation is retained before taking a norm.
* For twelve divisor pairs and the common radius, the stationary phase
  has rank 14 in 25 variables and nullity 11 whenever the radial balance
  has an interior solution. Treating it as a nondegenerate 25-dimensional
  phase is false. An actual positive-profile packet realizes its scale.
* After the common radius is integrated and every integer dual label is
  counted, the paired-packet absolute closure has unequal-block upper
  cost T^(7+epsilon) product_j N_j^(-1/2). On one actual positive divisor
  box with N comparable to T^(2/3), its precise positive certificate is
  at least c T^3. This is a lower bound for that certificate only.
* Combining the valid block envelopes with the original signed second
  moments gives the complete bound M12(B_T) << T^(7/3+epsilon). It is
  weaker than the inherited complete bound T^(10 beta+epsilon), so the
  best complete result and all accepted exponents remain unchanged.

Thus this is a complete joint-kernel attempt with no new bound. It does
not reject signed joint divisor cancellation. Its first missing input is
an actual signed twelfth moment of the complete dual divisor shell sum,
spelled out in Section 4. No local fragment replaces the frozen objective.

## 2. Exact statement and hypotheses

Use exactly the actual mollifier rho, Psi, window w, a_n, B_T, Q, L_Q,
Z_Q, E12 and I12 in the accepted distinct-radical reduction. In particular
rho is nonnegative, real, radial, smooth, compactly supported in the unit
disk, with integral 1; Psi(s)=rho-hat(s e1); and w is nonnegative smooth,
supported in [1/2,2], and is 1 on [1/sqrt(2),sqrt(3)]. Put

    e(t)=exp(2 pi i t),
    g_T(n)=n^(-3/4) Psi(sqrt(n/T)),
    beta=(50 sqrt(1717)-297)/13762.

T is real and at least 2. Every moment here uses w(R/T)dR, including its
displacement. Constants may depend on the fixed profiles and on the fixed
order 12. No assertion is made for order growing with T.

The permitted full-moment route is used. Its exact, already paid transfer is

    M12(L_Q) << T^(15/13+epsilon),
    |M12(Z_Q)-I12| << T^(8 beta-1/5+epsilon),
    M12(B_T) << T^(29/25+epsilon) iff
    |I12| << T^(29/25+epsilon).

The first two powers are below 29/25; specifically 29/25-15/13=2/325,
and 8 beta-1/5<21/25. The equivalence uses norm inequalities, not an
additive approximation of M12(B_T). These facts pay the small-class head,
all repeated-class configurations, and their mixed terms. The squarefree
mask is never extended to a differentiable function.

For the calculation, take a fixed nonnegative smooth dyadic partition of
the positive integer d and m variables. A divisor box has d comparable
to D, m comparable to M, and N=DM. An additional smooth norm partition
can be inserted, with only finitely many overlaps. All profiles have fixed
scaled derivative bounds. Write A(d,m) for their product. Its support is
inside positive d,m, including smooth extensions below 1 when D or M is
bounded; its sampled values give exactly the required positive-integer
partition. No integer is removed or assigned an incorrect endpoint.

The local wave is

    F_A(R)=4 sum_(d,m>=1) chi4(d) g_T(dm) A(d,m)
                            cos(2 pi R sqrt(dm)-3 pi/4).

All d,m and all divisor incidences have their original multiplicity.
The full B_T is their sum. For the finite transform calculation retain a
smooth upper cutoff equal to 1 up to T^(3/2) and zero past 2T^(3/2).
The discarded full wave has supremum O_K(T^-K) for any fixed K. This
follows from the actual divisor bound and Schwartz decay. Its L12 norm
is O_K(T^(1/12-K)); it is paid, not silently omitted.

There are O(log^2 T) relevant divisor boxes, with N between fixed positive
constants and O(T^(3/2)). This restriction is an auxiliary transform
device, not a restriction of the objective. In this range

    H_N=T/sqrt(N) >> T^(1/4),

which also pays the +1 in each integer dual-shell count.

## 3. Proof or derivation

### 3.1 Exact joint character expansion

For any smooth compactly supported F on positive d,m, with Fourier
convention F-hat(u,v)=integral F(d,m)e(-u d-v m)dd dm, one has

    chi4(d)=[e(d/4)-e(-d/4)]/(2i),
    sum_(d,m in Z) chi4(d) F(d,m)
       =(i/2) sum_(a odd,k in Z) chi4(a) F-hat(a/4,k).       (1)

Indeed the first exponential gives u=h-1/4 and coefficient 1/(2i),
while the second gives u=h+1/4 and coefficient -1/(2i). Their odd
numerators are respectively 3 and 1 modulo 4, proving the sign in (1).
Poisson here follows by periodizing a smooth compactly supported function
and taking its absolutely convergent Fourier series; no arithmetic theorem
is being imported.

For sigma=+1 or -1 put

    J_sigma(R;a,k)=integral g_T(dm) A(d,m)
                 e(sigma R sqrt(dm)-a d/4-k m) dd dm.

The exact transformed local cosine wave is

    F_A(R)=i sum_(sigma=+1,-1) e(-3 sigma/8)
                         sum_(a odd,k in Z) chi4(a) J_sigma(R;a,k). (2)

At twelve factors, (1) is simply applied in the genuine 24 arithmetic
variables. Before integrating R, it gives precisely the product of these
transforms. Integrating w(R/T) afterward is exact, and retains the same
complex displaced Fourier kernel as the original signed expansion.
There is no character orthogonality assertion and no absolute value in
(1) or (2). All 2^12 signs and all ordered products remain.

### 3.2 Divisor stationary geometry and the sine shell

Set d=r exp(t), m=r exp(-t); then dd dm=2r dr dt. For a,k positive let

    lambda=sqrt(a k),    t0=(1/2)log(4k/a).

The positive-sign phase is exactly

    R r-r[(a/4)exp(t)+k exp(-t)]
       =(R-lambda)r-lambda r[cosh(t-t0)-1].                 (3)

The positive stationary branch has a,k>0; the negative branch has
a,k<0 and is its conjugate. Wrong signs and zero k have no stationary
point in a positive divisor box. The necessary scales are

    a D comparable to T sqrt(N),
    k M comparable to T sqrt(N),
    lambda comparable to T.

These scales retain unbalanced divisor boxes, including D or M bounded.

There is an elementary uniform transverse calculation: put
v=2 sinh((t-t0)/2). Then cosh(t-t0)-1=v^2/2 exactly, and dt/dv is
(1+v^2/4)^(-1/2). Taylor expansion of the smooth amplitude at v=0,
the one-dimensional Gaussian integral, and integration by parts off a
fixed neighborhood give

    J_+(R;a,k)=e(-1/8) K_A(R;a,k)+E_A(R;a,k),               (4)

where

    K_A(R;a,k)=2 lambda^(-1/2) integral_0^infinity
       r^(-1) Psi(r/sqrt(T)) A(r exp(t0),r exp(-t0))
                                     e((R-lambda)r) dr.   (5)

A smooth cutoff in lambda/T, equal to 1 on an enlargement of the R/T
window, may be included in (5); the omitted terms are nonstationary.
The factor e(-1/8) is the negative transverse Hessian's Gaussian phase.
For every fixed A0, with sufficiently many fixed profile seminorms,

    |K_A(R;a,k)|
      <= C T^(-1/2) C_N (1+sqrt(N)|R-lambda|)^(-A0),
    |E_A(R;a,k)|
      <= C T^(-3/2) N^(-1/2) C_N
                            (1+sqrt(N)|R-lambda|)^(-A0). (6)

Here C_N can have any requested fixed decay (1+N/T)^(-A1), by taking
enough Schwartz seminorms. In (6), radial integration by parts supplies
sqrt(N)|R-lambda|. Differentiating its amplitude on the r~sqrt(N)
scale costs only fixed seminorms, since each angular remainder gains
(lambda r)^(-1). This also justifies radial differentiation of the
remainder. Stationary t0 crossing a support edge is harmless because
the extended cutoff is smooth and vanishes with all derivatives there.

For completeness of the summation: outside the displayed dual scale
box, a scaled d- or m-derivative of the phase is bounded away from zero
on its support. Repeated integration by parts gives arbitrary powers
of T sqrt(N) and summable decay in aD and kM. Within that box but away
from lambda~R, (3) gives radial integration by parts. The scale box has
O(T^2) labels, all scales are polynomially bounded in T, and the
number of original boxes is logarithmic. Thus increasing a fixed
integration order pays their entire nonstationary sum by O_K(T^-K).
No unpriced dual tail or zero-frequency face remains.

Now pair sigma=+1,a,k>0 with sigma=-1,-a,-k. Since chi4(-a)=-chi4(a),
(2) and (4) give the paired leading contribution

    2 chi4(a) Im K_A(R;a,k).                              (7)

In particular, the actual cosine and character phases turn the kernel
into a sine transform in R-lambda. It vanishes at its exact center in
the leading approximation. Replacing it with a positive centered bump
before pairing would miss an actual cancellation. That cancellation
does not remove its natural width N^(-1/2) or its off-center size
T^(-1/2).

### 3.3 The full joint Hessian and its sharp scale

On a stationary dual branch for twelve coordinates, write a_j,k_j
with sign sigma_j and positive lambda_j=sqrt(|a_j k_j|). At their
angular saddles, the full phase in r_j,t_j,R has equations

    t_j=t0_j,    lambda_j=R for every j,
    sum_j sigma_j r_j=0.                                (8)

If all signs agree, (8) is impossible. For mixed signs it is possible
only when the indicated radial ranges overlap after taking their
signed sums. No stationary set is manufactured for an impossible
unequal-block configuration.

Where (8) has an interior solution, the twelve angular Hessian entries
are -sigma_j R r_j and are nonzero. Their mixed derivatives with the
radial variables vanish at t_j=t0_j. The remaining block in
(r_1,...,r_12,R) is

    [ 0_(12 by 12)   sigma ]
    [ sigma^t          0   ],

which has rank 2. Therefore the complete Hessian has rank 12+2=14,
and nullity 25-14=11. The null vectors are precisely the radial
variations satisfying sum sigma_j delta r_j=0, with delta R=0.
This is an exact algebraic calculation, not a dimensional heuristic.

For equal N the normalized large parameter is T sqrt(N). The local
measure and original amplitude supply T N^3, and rank 14 supplies
(T sqrt(N))^(-7), giving

    T^(-6) N^(-1/2)                                     (9)

per matched joint packet. Equivalently, each transverse integral has
size T^(-1/2), and the common radius occupies width N^(-1/2).
Both computations give (9). A claim of full rank would invent
eleven absent Gaussian directions.

This scale is sharp even with actual positive profiles. Choose an
equal divisor box D=M~sqrt(N), with a nonnegative interior profile,
N~T^(2/3), and positive odd a~2T, k~T/2 in small fixed relative
intervals. Then t0 is in the interior of that box, lambda/T is in
the region w=1, and Psi(r/sqrt(T)) is positive and bounded below for
large T. For

    c1/sqrt(N) <= R-lambda <= c2/sqrt(N),

choose fixed 0<c1<c2 small enough that sin(2pi(R-lambda)r) is positive
and bounded below on a fixed interior r subinterval. Formula (5)
then gives Im K_A >= c T^(-1/2). For twelve identical packets,
chi4(a)^12=1 and the integrated twelfth power is at least the scale
(9). This tests the stationary geometry. It is not a lower bound
for the sum of different signed arithmetic packets, or for I12.

### 3.4 Integer dual multiplicity and a precise certificate obstruction

For fixed R~T, the shell |sqrt(a k)-R|<=L/sqrt(N) has

    |a k-R^2| <= C (L T/sqrt(N)+L^2/N).

For lambda~T, dyadically increasing L and using the decay in (6)
therefore gives

    sum_(a odd>0,k>0) (1+sqrt(N)|R-sqrt(a k)|)^(-A0)
          1_(allowed ratio)
      << T^epsilon (1+T/sqrt(N)).                         (10)

For each positive integer q=a k there are at most tau(q) choices;
q~T^2 makes that T^epsilon. The real endpoints cost the explicit +1.
The ratio restriction can only reduce this upper count. Because
N<=O(T^(3/2)), (10) is O(T^(1+epsilon)N^(-1/2)). It is not a
volume argument overlooking integer multiplicity.

From (6), the leading absolute packet sum is at most

    T^(1/2+epsilon) N^(-1/2) C_N,                         (11)

and the summed first angular remainder is at most

    T^(-1/2+epsilon) N^(-1) C_N.                          (12)

Summing (12) over all original boxes costs only T^epsilon, so the
complete leading representation differs from B_T by a wave of
supremum O(T^(-1/2+epsilon)), in addition to the already paid tails.
Its twelfth moment is O(T^(-5+epsilon)); norm inequalities pay all
mixed terms. One may retain more angular terms for an arbitrarily
small supremum error, but that is unnecessary for the target norm.

For twelve possibly unequal boxes, the literal joint positive closure
is

    integral w(R/T) product_j
            sum_(a_j odd>0,k_j>0) |2 Im K_(A_j)(R;a_j,k_j)| dR
      << T^(7+epsilon) product_j N_j^(-1/2) product_j C_(N_j). (13)

It can be obtained by (10) at the common R, or by fixing the narrowest
radius packet and counting all remaining shell intersections. The
common-R integration saves a width, but the free common dual center
and the other eleven integer shells restore exactly the power in (13).
Calling that width alone a joint saving is incorrect.

Here is a matching, rigorously positive lower control for the equal
box used above. Define the specific certificate

    C12_A=integral w(R/T)
               (sum_(a odd>0,k>0) |2 chi4(a) Im K_A(R;a,k)|)^12 dR. (14)

There are c T^2 admissible pairs a,k in the small fixed rectangles
described after (9). Each contributes at least
c T^(-1/2)N^(-1/2) to its integrated modulus. Hence the L1 integral
of the nonnegative sum in (14) is at least
c T^(3/2)N^(-1/2). Jensen with the measure w(R/T)dR, whose mass is
comparable to T, proves

    C12_A >= c T^7 N^(-6).                               (15)

All a are odd, so |chi4(a)|=1. The original Psi and profiles are
positive on the chosen block; no arbitrary coefficient substitute is
used. All sign pairing has already been performed in (7). At
N~T^(2/3), (15) is c T^3. Together (13) and (15) price this
particular certificate up to T^epsilon. The certificate still discards
the outer signed arithmetic sum, and is NOT the actual moment.
This is not a lower bound on I12, and does not assert that every
possible joint dispersion argument has this cost.

### 3.5 Complete norm restoration, including unequal blocks and tails

Regroup original boxes into smooth norm blocks n~N. The absolute
original coefficient bound and (11) give respectively

    sup_R |B_N(R)| << T^epsilon C_N
                      min(N^(1/4),T^(1/2)N^(-1/2)).      (16)

The derivative cost of the original square-root phase has already been
paid in (3)--(6); (16) does not apply Abel summation to a fast phase
while ignoring its variation. It is exactly the classical envelope,
now recovered from the joint character calculation.

The actual block coefficient energy is O(T^epsilon N^(-1/2)).
The separated frequencies sqrt(n) have spacing at least c/sqrt(N).
Expanding against smooth w gives a Gram kernel bounded by
T(1+T|sqrt(n)-sqrt(m)|)^(-A0). Its row sum is O(T), since
T/sqrt(N)>>1. The opposite cosine-sign kernel has still larger
frequency. Therefore, with every original coefficient retained,

    M2(B_N) << T^(1+epsilon) N^(-1/2) C_N^2.              (17)

No independence of the arithmetic coefficients is assumed in (17).
For this particular upper bound one could equivalently use the
elementary separated-frequency large sieve.

Using (16)^10 times (17) gives

    M12(B_N) << T^epsilon C_N^12 times
       T N^2                    if N<=T^(2/3),
       T^6 N^(-11/2)            if N>=T^(2/3).            (18)

The largest power in (18) is T^(7/3). Holder's finite-sum inequality
or the L12 triangle inequality pays every mixed unequal-block term
with only fixed powers of log T. The singleton and bounded initial
blocks have moment O(T); the full Schwartz upper tail was paid in
Section 2; bounded T is handled by the absolute coefficient sum.
Consequently the complete result of this closure is

    M12(B_T) << T^(7/3+epsilon).                          (19)

This is not a claim that (19) is sharp for the actual wave. The accepted
complete large-values input is stronger:

    M12(B_T) << T^(10 beta+epsilon).

Thus taking the best valid complete estimate leaves exactly the
inherited power 10 beta; the outstanding moment exponent saving is
10 beta-29/25, and the outstanding sixth-power norm saving is
5 beta-29/50. No complete exponent has improved. Equations (13)--(19)
also explain why recovering a scalar envelope from a multivariable
identity is not new progress past the Round203 barrier.

## 4. First doubtful or unproved step

Define the COMPLETE normalized signed dual sum, over every retained
divisor box and every positive odd a and positive k, by

    D_T(R)=sum_A sum_(a odd>0,k>0)
                         chi4(a) T^(1/2) Im K_A(R;a,k).

The smooth lambda cutoff and all original box profiles are those in
Section 3. The preceding remainder accounting gives, on the actual
radius window,

    B_T(R)=2 T^(-1/2) D_T(R)+O(T^(-1/2+epsilon)).          (20)

The error in (20), its tails, and all mixed terms are target-safe in
L12. Therefore the first missing signed arithmetic input is exactly

    integral w(R/T)|D_T(R)|^12 dR
                              << T^(179/25+epsilon).     (21)

Since 179/25=6+29/25, (21) is equivalent to the complete B_T target
through (20), and hence to the original I12 target through the paid
Round216 reduction. This is a reformulation, not a new lemma that
estimates the unknown quantity. Bounds for the separate boxes would
be sufficient after their summation but are not asserted necessary.

The needed new information is cancellation among actual chi4(a)
weighted nearby products a k, with the odd sine kernels and their
common R preserved. It does not follow from the rank computation,
from tau(q)<<q^epsilon, or from the vanishing of each leading sine
kernel at one point. Those facts yield only the costs already priced.

This is the first unproved step of the proposed successful route.
Replacing the signed sum by (14) cannot prove it: (15) gives the
precise obstruction to that replacement. Keeping the signed sum in
(21) could still succeed. No lower bound for that signed sum or the
actual target is claimed.

## 5. Control tests and outcomes

1. `actual_coefficients`: PASS. The only arithmetic opening is the exact
   identity r2=4(1*chi4); all divisor incidences and the actual Psi remain.
   The positive certificate control uses Psi>0 on an actual small norm
   block, not a random or adversarial coefficient model.
2. `all_distinct_class_masks`: PASS by the accepted full-moment
   equivalence, with the head T^(15/13) and repeated-class
   T^(8 beta-1/5) explicitly paid. No derivative of a squarefree mask is
   taken. The calculation does not claim the full B and I12 expansions
   are termwise equal.
3. `full_signed_kernel`: PASS for identities; TARGET OPEN. Equation (2)
   retains every cosine phase and the complex displaced Fourier kernel.
   The paired kernel is the actual odd sine shell. The positive
   certificate is named separately at the exact point modulus is taken.
4. `joint_stationary_geometry`: PASS locally. Rank 14, nullity 11,
   mixed-sign radial balance, absent all-equal-sign saddles, and the
   actual packet sharpness are derived. No ambient-dimension gain is
   asserted. If unequal supports exclude balance, this only improves
   that sector and does not pay the balanced complete complement.
5. `unequal_blocks`: PASS. Equations (6), (10), and (13) retain each
   separate N_j; (18)--(19) recombine all norm blocks by a norm
   inequality. No equal-scale estimate is substituted for that assembly.
6. `all_harmonics_signs_tails`: PASS. Full B retains every harmonic;
   both signs are paired exactly before further estimates. The original
   Schwartz tail, every dual tail, zero k, wrong-sign branch, and
   angular remainder are explicitly paid.
7. `real_endpoints`: PASS. T is real; the original smooth partition
   samples every positive integer, including bounded first boxes. The
   dual shell has its +1 term. The literal floor Q survives in the
   accepted transfer. No integer-center or even-window assumption occurs.
8. `complete_norm_cost`: PASS as a diagnosis, FAIL for target success.
   Complete method bound is T^(7/3), inherited best is T^(10 beta),
   target is T^(29/25). Restoring the normalized dual sum costs T^6
   in the twelfth moment, yielding the exact exponent 179/25 in (21).
9. `old_barrier_bypass`: NO BYPASS. The character and phase are kept
   through the joint calculation, but no bound exploiting their outer
   cancellation is proved. The new rank/certificate calculation explains
   the failed dimension inference; it is not relabeled success over
   Round203 scalar Poisson or Round210 absolute CRT. Round217's original
   distinct-class positive-certificate obstruction is neither weakened
   nor contradicted.
10. `statement_only_control`: READY FOR INDEPENDENT SEAM. This report
    is explicitly nonblind and has read no sibling report or isolated
    packet. The exact rank and packet-scale claim above is suitable for
    comparison with the conductor's separately isolated derivation.
    Independent validation is not self-certified here.
11. `fixed_order_full_goal_scope`: PASS. Even (21), if proved, would
    give only the fixed milestone 102/325. The checkpoint's sufficient
    full-quarter family requires an unbounded sequence of fixed even p
    with Q_p=floor(T^(1/p)) and I_p(T,Q_p)<=C_(p,epsilon)T^(5/4+epsilon),
    yielding discrepancy exponent 1/4+7/[8(p+1)]. No such family, no
    M1/M2/GAR parent, and no endpoint quarter theorem is established.

All mathematical work was analytical/algebraic. No numerical experiment,
symbolic computation, new external theorem, or primary theorem audit
was needed. File reads and cryptographic hashes are provenance checks,
not mathematical experiments.

## 6. Dependencies and exact artifacts used

Only the permitted context was read. The authoritative graph was first
read with output truncation, then its relevant GC complete-moment,
distinct-class, certificate, and parent entries were extracted exactly.
The graph hash matches the frozen brief. No sibling, successor, or
additional source file was read.

| Exact artifact | SHA256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `86bd9c5a8d329935b4c4cb944840b369149004ae706ae9c5b8f5d4ff41e07732` |
| `strategy/round218_complete_signed_radical_kernel.md` | `40185e8fbd2961087f93ce6141fe7801b36d57c0d1e9ee67e6f42ac2925800d4` |
| `strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md` | `39054e4123c11b85e55d9146794cfdd7453915ebeFD8a1286763e08b4ecabcd2` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md` | `603aa69cb4b757707d6eb89bb8290b05190b6b6d5cae83be52ddc19658ef68bb` |
| `rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md` | `6ea983ef7066a7dc1a7833bbf4a99889e79c75eef9c42190421a4248c104aa5a` |
| `rounds/codex-managed/gc-signed-near-frequency-cancellation/synthesis.md` | `b0f7d6e95b868c02fbc19d7bff0d7d0833867e9e527f1d349a44f5074c0cb86c` |

Also read the task's generated brief at
`rounds/codex-managed/gc-complete-signed-radical-kernel/briefs/joint_divisor_kernel.md`.

Accepted mathematical dependencies are the exact r2 divisor identity,
the elementary divisor bound, the actual Schwartz coefficient estimates,
the complete large-values moment bound (including its existing qualified
Li--Yang application), and the complete distinct-radical equivalence.
The character transform sign, divisor stationary geometry, natural shell
width, integer multiplicity restoration, and certificate lower control
are derived in this report. The prior syntheses are method barriers;
they are not treated as supplying a missing signed theorem.

## 7. Recommended state effect

RETAIN as bounded method evidence; NO CHANGE to accepted theorem state.
Reject only the proposed inference that joint 25-dimensional stationary
phase automatically yields a full-rank gain, or that the positive
paired-packet certificate (14) can meet the target. Neither rejection
applies to actual signed I12 or the complete dual signed sum (21).

Do not promote (21) as a new estimate or introduce another unestimated
sector node merely for this exact reformulation. Preserve the accepted
complete moment bound, all source qualifications, the full quarter goal,
and every independent parent. The conductor should reconcile the local
rank and application seams at this report's final hash before closing
Round218. This subagent stops here and designs no successor round.
