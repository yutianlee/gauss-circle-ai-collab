# Round219 independent sharp-interval dispersion review

## 1. Result and exact-hash verdict

Reviewer: `actual_anchor_incidence` in the reused `joint_lattice_kernel`
agent; NONBLIND same-round seam, 2026-09-28.
Campaign: `gc-complete-anchored-divisor-energy`; round219.

**GREEN for the stated sharp transform, complete error price, modular
energy identities, and insufficient generic closure.** The signed
arithmetic estimate(14) remains unproved. No substantive transform
gap requiring conditional mathematical status was found.

Reviewed artifact:
`rounds/codex-managed/gc-complete-anchored-divisor-energy/reports/joint_cofactor_dispersion.md`.
Independently reproduced SHA256:
`cbb7e8de456bb37c871eafaf21ffb4ecedeb36e7aac50b1719275d13cb1fef81`.
The first dispatch contained a transcription typo in the hash. The
conductor's corrected 64-digit hash agrees with the independently read
file; the file was not changed. This review binds the verified hash.

Two terse proof passages are made precise below: the Gaussian integral
has factor sqrt(2/a), and uniform odd-sine harmonic bounds follow by
reducing to complete sine harmonic sums. The report's displayed main
constants already incorporate the correct Gaussian factor. These are
exposition clarifications, not changes to its claimed formulas or powers.
No report or shared-state edit was made.

## 2. Exact hypotheses and claims reviewed

The input is the actual real half-open rectangle of the permitted216
anchored report: N,D dyadic, 1<=D<=N<=T^(3/2), K=N/D>=1,
k a positive integer in[K/2,2K), R in[T/2,2T], and the actual
coefficient (N/(dk))^(3/4)Psi(sqrt(dk/T)) on its literal support.
The support in d is an interval whose moving endpoints can coincide,
be integers, or approach a saddle arbitrarily closely. The physical
high points and sigma_j=sign H(R_j) are those of the frozen objective.

The claims checked are:

- Uniform divisor-transform error O(log(2T)+D/sqrt(T sqrt(N)))
  per(R,k), with real stars and all symmetric character-Poisson tails.
- The exact main sine coefficient and its normalized moving weight.
- Complete cofactor error absorption with relative power-221/2625,
  and preservation of actual high-wave alignment.
- The real reciprocal-anchor energy, including every difference and
  sum alias modulo the integer cofactor lattice, with the original
  diagonal still distinguished from the transformed one.
- The sufficient input(14), complete generic estimate(15), restored
  cost(16), and unchanged full unconditional moment.

All constants concern fixed smooth mollifier seminorms and fixed
twelfth order. No arithmetic mask is smoothed and no arbitrary high-point
signs or unproved source theorem are granted.

## 3. Independent derivation and complete seam audit

### A. Character Poisson, exact quadratic phase and constants

Under the minus-exponent Fourier convention,

    chi4(d)=(e(d/4)-e(-d/4))/(2i)

gives coefficient(i/2)chi4(a) at odd-quarter frequency a/4. The
numerators4h-1 have character-1 and coefficient-i/2; the numerators
4h+1 have character+1 and coefficient+i/2. A starred finite interval
is the symmetric Fourier-series value of the periodized BV function.
Changing a star back to its literal included/excluded integer endpoint
costs at most the bounded value of that endpoint. This costs O(1),
including the bounded initial boxes and a singleton.

For the positive original branch f(d)=R sqrt(kd), the stationary point,
value and second derivative are

    d_a=4R^2 k/a^2,
    f(d_a)-a d_a/4=R^2 k/a,
    f''(d_a)=-a^3/(32R^2 k).

Set x=sqrt(d) and x_a=2R sqrt(k)/a. Then the phase is EXACTLY

    R^2 k/a-(a/4)(x-x_a)^2.

The exact Gaussian normalization is

    integral_R e(-a y^2/4)dy=sqrt(2/a)e(-1/8),    a>0.

Multiplying this by p(x_a)=2x_a g_k(x_a^2) gives
sqrt(32R^2 k/a^3)g_k(d_a)e(-1/8). Thus the displayed coefficient in
equation(5) is correct. The report's prose describing only an a^(-1/2)
scale should be read with this sqrt(2) constant, which is already in(5).

Original cosine contributes1/2, and character Poisson contributes i/2.
The positive Gaussian branch has e(-3/8)e(-1/8)=-1. Its contribution
is therefore(-i/4)chi4(a) times the real positive Gaussian amplitude
times e(R^2k/a). The negative original/dual branch contributes its
conjugate with chi4(-a)=-chi4(a). Their sum is

    chi4(a) 2sqrt(2)R sqrt(k)a^(-3/2)g_k(d_a)
                                         sin(2pi kR^2/a),

which is exactly the POSITIVE sine in(7). No parity or evenness of
the displaced physical window is invoked.

### B. Uniform saddle/endpoint error, including very short intervals

Write U=T sqrt(N), A=U/D and b0=D/sqrt(U). For central a~A,
x and x_a lie in one fixed positive enlargement of x~sqrt(D).
The actual smooth coefficient obeys |D^r g_k^(r)|<=C_r there.
Consequently p=2xg_k(x^2) has bounds

    |p|<<sqrt(D),    |p'|<<1,    |p''|<<D^(-1/2).

For q(x)=(p(x)-p(x_a))/(x-x_a), with its continuous value at x_a,
the integral representation through p' proves |q|<<1 and
|q'|<<D^(-1/2). Integrating q(x)(x-x_a) against the derivative of
e(-a(x-x_a)^2/4) gives O(1/a) from its two boundary terms and
O(1/a) from its integral. This is O(D/U), uniformly when the saddle
crosses an endpoint. Smooth extension is used only on this fixed
enlargement; its derivative constants remain uniform.

The constant Gaussian part is the full integral, half the integral,
or zero according as the saddle is interior, is one distinct boundary,
or is exterior. Its difference from the finite interval integral is
bounded by its two truncated Gaussian tails. For a boundary x_e,

    tail << min(a^(-1/2),1/(a|x_e-x_a|)).

After multiplication by p(x_a), this is bounded by
min(b0,C/|f'(d_e)-a/4|), since
f'(d_e)-a/4=a(x_a-x_e)/(4x_e) and x_e~sqrt(D).
This proves the report's(6), including its interpretation at zero
denominator. If both endpoints are very close to a saddle, both tail
terms are kept. A zero-length interval has no integral/main interval
mass; any isolated sampled endpoint is in the preceding O(1) correction.

Summing over O(A) central odd labels gives O(1) for D/U, at most
O(b0+1) for the bounded number closest to each endpoint frequency,
and O(log(2+A)) for the rest. Thus no minimum distance of an endpoint
from an integer or a quarter frequency is being assumed.

Small positive labels below the enlarged central range also need to
be counted. There |f'-a/4|>=cA, so a first-derivative integration with
the bounded coefficient variation costs O(1/A) per label and O(1)
in total. The finite negative-label range has the same property.
This supplies explicitly the small positive range only tersely included
in the report's outside-range discussion.

### C. Infinite character-Poisson tail and convergence at jumps

For |a|>C A, one integration by parts uses denominator f'(d)-a/4.
Its expansion is -4/a+O(A/a^2). Bounded coefficient variation and
integral|f''|=O(A) make all O(A/a^2) terms summable with total O(1),
including endpoints, derivative integrals, and the differentiated
denominator. The remaining leading endpoint and g_k' terms contain
the SYMMETRIC series

    sum_(a odd)^sym chi4(a)e(-a x/4)/a.                  (R1)

Its positive/negative pairing is

    2 sum_(a positive odd) chi4(a)cos(pi a x/2)/a
      =sum_(a positive odd)
         [sin(pi a(1+x)/2)+sin(pi a(1-x)/2)]/a.          (R2)

For full harmonic partial sums S_M(theta)=sum_(n<=M)sin(n theta)/n,
reduce theta modulo2pi, split at the reciprocal distance to2piZ,
and apply summation by parts to the remaining geometric sums. This
proves a uniform bound in M and theta. Odd sums obey exactly

    sum_(n<=M,n odd)sin(n theta)/n
         =S_M(theta)-(1/2)S_floor(M/2)(2theta),

so their partial sums are uniformly bounded as well, including near
theta=pi. This gives a precise proof of the report's terse harmonic
claim without using an inappropriate absolute sum of1/a or overlooking
the odd-series behavior near pi.

Every symmetric tail partial sum of(R1) is therefore O(1), uniformly
in the real endpoint x and in the cutoff A. Its pointwise symmetric
limit exists, including jumps with their starred values. Multiplication
by bounded endpoint values costs O(1). Inside derivative integrals,
the uniform bound permits dominated convergence against |g_k'|,
whose integral is O(1). The original factor e(f(d)) has modulus1.
This verifies the whole infinite tail and its limiting endpoint
convention. It does not assert absolute convergence of(R1).

Together Sections B and C prove the claimed error O(log(2T)+b0)
uniformly for each actual(R,k), with all central, small and distant
integer labels paid. The proof is self-contained at the required
elementary level; no sharp B-process theorem is silently imported.

### D. Moving coefficient, actual alignment and aggregate error

At d_a=4R^2k/a^2, direct substitution gives

    2sqrt(2)R sqrt(k)a^(-3/2)g_k(d_a)
       =N^(3/4)/(sqrt(R)k) Psi(2Rk/(a sqrt(T))).

Since b0=D/(sqrt(T)N^(1/4)), multiplying the report's omega by b0
gives exactly this coefficient, with its original stationary star.
For fixed j,a, the conditions on d_a and d_a k are intersections of
monotone intervals in k. They have O(1) endpoints, even when two
endpoints coincide. Smooth differentiation costs O(1/K); the actual
Psi sign and the finite jumps remain. Isolated half-values change the
variation by only O(1). Products of two weights thus have bounded
variation, as required by the subsequent discrete Abel step.

The aggregate error is a sum of J actual signs times individually
bounded errors. With at most2K cofactors it has squared norm

    <<T^eta J^2K(1+b0^2).

Dividing by P0=J^2v^2N^(3/2)/(64K) gives, up to fixed constants,

    T^eta[sqrt(N)/(v^2D^2)+1/(T v^2)].

Using the actual necessary condition
D>>T^(-13/42-eta)v^2N^(29/84), and then N>>v^4, the first term is

    <<T^(13/21+eta)v^(-6)N^(-4/21)
     <<T^(13/21+eta)v^(-142/21)
     <<T^(-221/2625+eta).

The level logarithms are absorbed by choosing the input loss smaller.
The second term is smaller. Thus the claimed P0/100 error norm is
available for sufficiently large T. Cross terms require no separate
claim: Q<=2b0^2 E+2||e||_2^2 handles them completely.

The rectangle's scalar error divided by v has ordinary part bounded
by T^(13/42+eta)v^(-3)N^(-2/21), hence
T^(-221/5250+eta), and its b0 part is O(1/(sqrt(T)v)). This verifies
preservation of actual sigma_j at high points, including an anchor
arbitrarily close to a moving star crossing. It provides no alignment
claim for individual reciprocal frequencies.

### E. Every alias, diagonal, capacity cost and restored power

Real sine multiplication gives difference cosine MINUS sum cosine,
exactly as equation(11). Both modular arguments are R_j^2/a plus or
minus R_l^2/b. The original constant D0 remains separate; it cannot
be replaced by the transformed diagonal. The latter's upper scale
JAK does restore to JN because b0^2 A K=N.

Bounded variation and the finite integer geometric sum give
min(K,1/||xi||), also for a singleton or a star endpoint. When
||xi||=0, use K. Every positive and negative integer alias of the
difference and sum is therefore retained. The plus frequency's large
ordinary size has no bearing on its distance from an integer.

The normalization of sufficient input(14) is correct:
P0/b0^2=J^2v^2TK/64 and JN/b0^2=JAK. Its first term yields P0/2
after multiplication by2b0^2; the error supplies at mostP0/50.
Since D0>=0, this is sufficient for the original target, with its
displayed fixed slack. Necessity with those exact constants is not
asserted.

For the generic modulus cost, b~A traverses a reciprocal interval of
length O(B), derivative magnitude comparable to B/A. All relevant
integer target intervals, for either sum or difference with a fixed
constant, number O(B+1). Each inverse image has length O(delta A/B).
Thus their total integer occupancy is bounded by
min(CA,C(B+delta A)); B>>1 in every original rectangle. Dyadic
summation at distances beginning1/K proves

    sum_(b~A)min(K,1/||c+-R_l^2/b||)
        <<A log(2K)+K min(A,B).

After summing a,j,l, this is at most
T^eta J^2 A^2 min(D,K), because B/A=D/K and D,K>=1. Multiplication
by b0^2 gives T^eta J^2 T sqrt(N)min(D,K); the original Cauchy
factor gives T^eta J^2 T min(D,K)/D. These are the exact complete
costs in(15)--(16). The D<=sqrt(N) range retains threshold v^2>>T,
so the calculation cannot supply the required absorption at the actual
retained threshold. The reported sample powers satisfy only known
necessary constraints; they are correctly not labeled actual high points.

Finally, every rectangle, endpoint error and original Schwartz tail is
covered before the conditional restoration. If the missing complete
energy(14) were proved, the existing maximal-cover and high-event union
give113/125+42rho/13=29/25, with every mixed block and the lower
layer-cake boundary retained. Without it, both upper distribution
terms remain and the full moment is still T^(10 beta+epsilon).
No local transformed diagonal or paid error establishes the missing
signed dispersion estimate.

## 4. First unproved step and correction status

The first unproved arithmetic step remains equation(14) for the complete
actual reciprocal-anchor energy, with its real signs, moving weights,
and all integer aliases. The sharp-interval transform itself has a
sufficient proof once the terse details in Section3 of this review are
made explicit. There is no unresolved transform assumption requiring
the report's error absorption to be downgraded to a conditional claim.

The exact sqrt(2/a) Gaussian factor, reduction of odd harmonic sums to
full harmonic sums, and small positive nonstationary-label range are
recorded here as proof clarifications. The displayed transform constants
and downstream estimates need no correction. If the report is later
reissued, its brief prose on the Gaussian scale could include the exact
sqrt(2) to remove any possible ambiguity. No substantive defect or
current file edit is required by this review.

## 5. Required controls and outcomes

- Exact chi4 Fourier sign, starred Poisson identity, Gaussian main
  coefficient, cosine/conjugate pairing and positive sine: GREEN.
- Arbitrarily close stationary/endpoints, short intervals, literal
  sampled endpoints, finite wrong-sign/small labels, and conditional
  symmetric far-tail convergence: GREEN.
- Actual smooth-weight derivatives, moving k masks, stars as jumps,
  and actual high-sign preservation: GREEN.
- Complete cofactor error and cross terms, including-221/2625 and
  -221/5250 exponents: GREEN.
- All difference AND sum aliases, original/transformed diagonal
  distinction, energy normalization and full generic capacity: GREEN.
- Every rectangle, cofactor K=1, original Schwartz tail, mixed-block
  restoration, conditional29/25 and unchanged unconditional10 beta:
  GREEN for the stated scope.

The signed estimate itself is OPEN. GREEN does not certify a new
moment, the target rho, any M1/M2/GAR parent, or the quarter theorem.
The generic power example is not a counterexample built from actual
aligned high points. Zero experiments were performed.

## 6. Dependencies, provenance and isolation

The only newly read current-round artifact was the exact-hash report
identified in Section1. Its listed permitted dependencies already read
in this thread supplied the protocol, unchanged graph,219 manifest and
strategy, closed217 checkpoint, accepted204/216 kernels, the216 anchored
report, the closed218 synthesis, and the frozen218 divisor report.
No current sibling review, isolated packet, new external source, or
unlisted historical source was read. The earlier218 work and this
reviewer's own219 discovery work are disclosed NONBLIND history.

The conductor separately pointed out the small positive-label range
and corrected the dispatch hash typo. Both points were independently
checked above. The report's disclosed conductor normalization support
is not treated as independent validation of its proof.

Only this assigned review was written. The claimant report, graph,
proof draft, validation matrix, synthesis, legacy paths and every
successor-round artifact remain unedited. All reasoning was analytical;
file hashing is provenance checking, not a mathematical experiment.

## 7. Recommended state effect

Close this exact-hash seam GREEN and retain the report as a bounded,
fully priced failed dispersion attempt. No theorem or exponent promotion
is licensed. The uniform transform and paid error are valid method
components; their remaining complete signed arithmetic input is still
unproved. Keep the full anchored inequality, independent full-proof
parents and quarter goal open. This reviewer stops here and starts no
successor round.
