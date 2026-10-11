# Round221 independent shifted-correlation review

## 1. Result and exact-hash verdict

Campaign `gc-actual-vector-gram-correlations`, round221.
Reviewer: reused `joint_divisor_kernel` agent, NONBLIND independent
cross-review, 2026-09-28. I authored the separate actual anchored
Gram-chain report in this round; earlier218--220 history is also
disclosed. No statement-only isolation is claimed.

**GREEN for the exact arithmetic decomposition, complete cost bounds,
uniform-H positive certificate obstruction and no-gain conclusion.**
Reviewed claimant:
`rounds/codex-managed/gc-actual-vector-gram-correlations/reports/actual_shifted_correlations.md`.
Independently verified SHA256:
`6e0c9a229fa81d37c137c87197e66d2bfc6eddc4bb231f8eef256f51bf9fdbca`.

No substantive repair is required. The one-sided meaning of an Abel
star at a zero-length interval is made explicit below: its Fourier
value is zero, and an original included singleton is restored as a
finite endpoint correction. This clarifies the claimant's existing
one-sided convention; it changes neither the decomposition nor a cost.

The complete actual signed I12 estimate remains unproved. In particular,
the positive certificate lower bounds T N^2 and T^3 are not lower
bounds for any actual signed integral or physical twelfth moment.

## 2. Exact quantities and hypotheses reviewed

Use the actual real coefficients
a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)), the fixed actual window w and
Q=floor(T^(2/5)). On a finite literal interval within(N,2N], put

    c_n=a_n 1_(sf(n)>Q)1_(n in the interval),
    F_N(R)=sum_n c_n e(R sqrt(n)),
    Z_N(R)=Re(e(-3/8)F_N(R)),
    C_h^Q(R)=sum_n c_n c_(n+h)e(R(sqrt(n+h)-sqrt(n))),
    E_N=sum_n c_n^2.

Zero extension is literal. The arithmetic opening concerns
1<=h<N, R in[T/2,2T], N<=T^(3/2). The diagonal h=0 is E_N;
negative h are conjugates. Empty masked blocks when Q>=2N require
no correlation estimate. For the Fejer step, 1<=H<=N is integral
and N is the ambient integer block length, with harmless enlargement
where an endpoint is partial.

The report claims an exact decomposition into principal Poisson mode,
the entire remaining mode/endpoint package, hyperbola-square terms,
and the class-deletion correction. It claims complete upper prices
for all four, not an asymptotic formula for r2(n)r2(n+h).

The accepted204 and216 kernels are used only for their already
established coefficient bounds, full distribution/ceiling, paid head
and collectively repeated-class reduction. No new external source
or shifted-convolution estimate is being imported in this review.

## 3. Independent derivation and complete seam audit

### A. Real signs and the exact Fejer formula

Since e(-3/8)^2=e(-3/4)=i, direct expansion gives

    Z_N^2=(|F_N|^2+Re(i F_N^2))/2
          =(|F_N|^2-Im(F_N^2))/2.                       (R1)

Thus the claimed negative sum-sine sign is correct. The subsequent
inequality |Z_N|<=|F_N| is an explicit sufficient enlargement of the
WHOLE real moment. It does not identify a balanced component with
the real signed expansion or dismiss the other signs as negligible.

Let x_n=c_n e(R sqrt(n)), and set
t_j=sum_(r=0)^(H-1)x_(j+r), interpreting every zero-extended entry
directly as zero. Then sum_j t_j=H sum_n x_n, there are at most
N+H-1 potentially nonzero t_j, and

    H^(-1)sum_j |t_j|^2
       =E_N+2 Re sum_(1<=h<H)(1-h/H)C_h^Q(R).           (R2)

Although expansion can first produce conjugate C_h, its real part
is unchanged. Cauchy gives exactly the claimant's prefactor
(N+H-1)/H. Equation(R2) also proves nonnegativity of the bracket.
H=1 gives |F_N|^2<=N E_N; empty supports give zero throughout.

### B. Hyperbola identity, square correction and full CRT data

For n=2^s u with u odd, r2(n)=4 sum_(d|u)chi4(d). Pair the divisors
d and u/d on the strict side d<sqrt(u). Complete multiplicativity
on odd integers gives chi4(u/d)=chi4(u)chi4(d). If u is a square,
the unpaired divisor contributes exactly chi4(sqrt(u)). Hence

    r2(n)=4(1+chi4(u))sum_(d|u,d<sqrt(u))chi4(d)
                         +4 1_(u square)chi4(sqrt(u)).  (R3)

The square term can be negative; it is not replaced by its absolute
value in this identity. For example u=9 has bulk8 and square term-4,
giving the correct r2=4. For u congruent3 mod4 the bulk vanishes
and u cannot be a square. The identity also handles u=1 correctly.

A nonzero bulk contribution has u congruent1 mod4. For an odd
divisor d, write u=dv. Then v congruent d mod4, so the exact condition
on n is

    n congruent 2^s d^2 mod 2^(s+2)d,
    n>2^s d^2.                                        (R4)

This congruence forces valuation exactly s, not merely divisibility
by2^s. Conversely (R4) gives an odd u congruent1 mod4 with d|u
and d<sqrt(u). Thus no valuation or divisor copies are introduced.

For the second factor n+h use t,e. The gcd of the two moduli is
4*2^min(s,t)*g, g=gcd(d,e), and their lcm is

    ell=4*2^max(s,t)*de/g.                              (R5)

CRT compatibility is exactly

    4*2^min(s,t)*g divides 2^t e^2-2^s d^2-h.            (R6)

For each compatible pair there is one residue modulo ell. In
particular g|h, but that odd-divisor condition alone is insufficient.
The two-adic residues are n congruent2^s mod2^(s+2) and
n+h congruent2^t mod2^(t+2); when s=t they require
2^(s+2)|h. Equations(R5)--(R6) retain the complete compatibility,
including unequal valuations. The bulk coefficient is exactly
64 chi4(d)chi4(e).

Intersecting the original two supports with both strict inequalities
in(R4) gives one literal interval J, possibly empty or degenerate.
The ranges d<sqrt(2N/2^s), e<sqrt(2N/2^t) include the full
hyperbola; this is not a chosen divisor subrange.

### C. Abel completion, sharp endpoints and principal mode

For smooth G on J, periodize G 1_J at period ell. Its Fourier
coefficients are ell^(-1) integral_J G(x)e(-nu x/ell)dx.
Evaluation at residue b, with Abel multipliers r^|nu| as r tends
to1 from below, gives

    ell^(-1)lim_(r to1-)sum_nu r^|nu|e(nu b/ell)
                                  integral_J G(x)e(-nu x/ell)dx. (R7)

The limit is the average of the one-sided periodized values at each
jump. For a nondegenerate interval this assigns the usual half-value
at a boundary sampled point. For a zero-length support the integral
and Fourier/Abel value are zero; an original included singleton is
then restored wholly by the finite endpoint correction. Treating
both coincident half-corrections together gives that full value.
This is consistent with the report's stated one-sided convention.

Only O(1) boundary values per progression are changed when the
original strict/inclusive support is restored. The principal mode is
nu=0. The entire other Abel limit PLUS these literal corrections is
the A_h package. There is no absolute summation of the 1/nu boundary
tails. Its final norm estimate is obtained from the finite original
progression sum minus its principal mode, so no unpriced infinite
tail remains.

For G=f_N(x)f_N(x+h)e(R phi_h(x)),
phi_h=sqrt(x+h)-sqrt(x), the derivative is negative and increasing,
and |R phi_h'| is comparable to T h N^(-3/2). The smooth amplitude
has supremum plus variation at most
N^(-3/2)W_B(N)^2, W_B=(1+N/T)^(-B). One integration by parts with
the monotone nonvanishing derivative therefore gives

    |integral_J G(x)dx|<<W_B(N)^2/(T h),                (R8)

uniformly in short or moving intervals. This really uses R~T.
There is no claim that the same principal price holds at R=0.

Writing d=g alpha,e=g beta and dropping restrictions only for an
upper bound yields

    sum_compatible ell^(-1)
      <<sum_(s,t)2^(-max(s,t))
          sum_(g|h)g^(-1)(sum_(alpha<=sqrt(2N)/g)alpha^(-1))^2
      <<tau(h)log^2(2N).                               (R9)

The two-adic double sum converges. Equation(R9) uses the necessary
g|h derived from the FULL compatibility condition; it does not
replace that condition in the exact decomposition. Together(R8)--(R9)
give the claimed principal-mode price with all divisor multiplicities.

### D. Whole nonzero-mode, square and mask prices

For each compatible progression, the number of original sampled
integers is at most C(N/ell+1). The main N/ell counts are paid by
(R9), and

    sum_(s,t) #{d<sqrt(2N/2^s),e<sqrt(2N/2^t)}
       <<N sum_(s,t)2^(-(s+t)/2)<<N.                    (R10)

Multiplication by the amplitude N^(-3/2)W_B^2 pays the entire bulk
capacity at W_B^2 N^(-1/2+epsilon). As A_h=C_h^bulk-P_h exactly,
this also pays A_h: 1/(Th)<=N^(-1/2) on N<=T^(3/2), after
the harmless divisor losses. Thus the claimant has bounded the
WHOLE alias and endpoint package, albeit by an insufficient count.

Integers in(N,2N] whose odd part is a square number at most
sum_s sqrt(2N/2^s)<<sqrt(N). Since the square correction has
magnitude at most4 and the bulk magnitude at most r2+4, all three
cross/square products cost W_B^2 N^(-1+epsilon). The square
coefficient sign from(R3) is preserved until this stated bound.

The class deletion uses the exact product identity

    m_Q(n)m_Q(n+h)-1
      =-1_(sf(n)<=Q)-1_(sf(n+h)<=Q)+1_(both small).       (R11)

There are at most C sqrt(NQ) relevant small-class integers, by
summing n=d s^2 over d<=Q and dropping squarefreeness only for an
upper count. With the divisor bound this costs
W_B^2 Q^(1/2)N^(-1+epsilon). No derivative of m_Q occurs.

Inserting these prices in(R2) produces respectively
N^(1/2)/H, N log(2H)/(TH), N^(1/2), 1 and Q^(1/2), all multiplied
by T^epsilon W_B^2. These are exactly the report's five terms.
Q<2N permits the overall ceiling N^(1/4)W_B up to epsilon.
The principal mode and class-deletion contribution are individually
smaller, but the complete A_h price remains. The zero mode alone
does not establish a target-sized shifted correlation.

### E. Uniform-H actual positive certificate and second moment

On an actual block N<=cT with c small and Q=o(N), Psi>=1/2.
Elementary annular lattice mass and the paid small-class mass give
M=sum c_n comparable to N^(1/4). All c_n are nonnegative. Hence
E_N>=M^2/N>>N^(-1/2), while the divisor bound gives
E_N<<N^(-1/2+epsilon).

For U_h=sum|c_n c_(n+h)| the positive Fejer bracket equals
sum_(n,m)(1-|n-m|/H)_+ c_n c_m on this block. If H>=2,
partition into bins of length max(1,floor(H/2)). There are at most
C N/H bins and all their within-bin pairs have weight at least1/2.
Cauchy on the bin masses gives bracket>=c H M^2/N.
Multiplication by(N+H-1)/H yields Pi_(N,H)>=cN^(1/2).
H=1 follows directly from Pi=N E_N.

The reverse bound is also uniform: U_h<=E_N by Cauchy and zero
extension, and 1+2sum_(1<=h<H)(1-h/H)=H. Thus

    c N^(1/2)<=Pi_(N,H)<=(N+H-1)E_N
                              <<N^(1/2+epsilon)         (R12)

for every H. No assumption on density at any individual increment
is required by this argument.

The smooth-window second moment expands exactly in endpoint
differences. Since |sqrt(n)-sqrt(m)|>=c|n-m|/sqrt(N), the Schwartz
row sum away from the diagonal is O_A((sqrt(N)/T)^A). Applying
2|c_n c_m|<=c_n^2+c_m^2, rather than counting all pairs by a
common maximum, gives

    M2(F_N)=T w-hat(0)E_N
                   +O_A(T E_N(sqrt(N)/T)^A).            (R13)

There is no dimension factor. It holds for arbitrary deleted indices
and real coefficient signs; the lower positive-block estimate then
uses w-hat(0)>0 and E_N>>N^(-1/2). On the entire truncation the
relative error tends to zero uniformly because N<=T^(3/2).

The pointwise Fejer ceiling gives the complete certificate

    M12(Z_N)<=M12(F_N)<=Pi_(N,H)^5 M2(F_N).              (R14)

Combining(R12)--(R13) proves c T N^2<=the right side of(R14)
<=C_epsilon T N^(2+epsilon), uniformly in H on the actual positive
block. This is a lower bound ONLY for that positive certificate.
It does not lower-bound its left side, the separate A_h package or
any signed Fourier contribution.

### F. Complete restoration and unchanged goal

For every block, not just positive ones, the upper certificate has
the Schwartz factors and is at most
T^(1+epsilon)N^2 W_B(N)^12. Taking twelfth roots and summing all
dyadic blocks gives

    T^(1/12+epsilon)sum_N N^(1/6)W_B(N)
                         <<T^(1/4+epsilon),             (R15)

because the dyadic sum is O(T^(1/6)) for fixed B>1. Thus the
complete attempted moment price is T^(3+epsilon). All unequal
blocks are paid by Minkowski. A positive dyadic block N~cT
provides a cT^3 lower bound for this same block-summed certificate;
Q=T^(2/5)=o(N) there. At N~T^(2/3), its price is T^(7/3).

The full n>T^(3/2) tail is uniformly O_A(T^-A) by the actual
Schwartz/divisor envelope. Its mixed terms, the singleton, partial
blocks and real top cutoff are paid by the same norm inequality.
The accepted216 head15/13 and repeated-class error8 beta-1/5
restore B_T and I12 without a missing complement.

This is weaker than the accepted204/216 fallback. Its masked
distribution v^-2+T v^(-136/13) and the actual Z_Q ceiling from
B_T-L_Q pay every level. The low part through V0=T^(13/125)
costs T+V0^10+T V0^(20/13)<=T^(29/25+epsilon). The high part
keeps all four terms W^10+T W^(20/13)+V0^10+T V0^(20/13),
with W=T^(beta+epsilon), and remains T^(10 beta+epsilon).
Neither inherited high-level contribution is removed by the small
principal mode. The one-sided signed target stays open.

## 4. First unproved step and repair status

The first missing analytic estimate is sufficient signed cancellation
in the complete nonzero progression-mode aggregate, together with
its Fejer increment weights, actual characters, class corrections and
absolute radius. The stated capacity estimate is a complete bound
for that package, not a target-sized estimate. Its exact failure is
fully restored in(R14)--(R15).

No additional theorem is needed for the written decomposition or
certificate bounds. No substantive repair was found. For clarity,
the degenerate endpoint convention in Section3.C should always be
read as the average of one-sided limits; a literal singleton is a
finite correction, not a nonzero integral over a point. This prevents
an ambiguous double-star notation without changing any claimed bound.

The positive control forbids gaining a power merely by tuning H after
the same correlation phases are erased. It does not forbid a signed
arithmetic estimate before that erasure, and it does not reject the
actual target or imply actual high-point saturation.

## 5. Required controls and outcomes

- Exact real cosine identity and negative sum-sine sign: GREEN.
- Complementary-divisor pairing, signed square divisor, u=1 and
  u congruent3 mod4 cases: GREEN.
- Exact two-adic valuations, full CRT compatibility, single residue
  multiplicity and lcm modulus: GREEN.
- Abel completion, every integer mode, one-sided endpoint limits,
  singleton restoration and no absolute sharp-tail assertion: GREEN.
- Anchored principal integral, full reciprocal-modulus sum, all
  terminal progression counts, square and mask corrections: GREEN.
- Fejer constants, H=1, empty masks, uniform-H positive lower/upper
  certificate and dimension-free displaced M2 estimate: GREEN.
- Whole block sum, every mixed block, full tail, all levels, retained
  head/repeated-class costs and unchanged10 beta: GREEN.
- Actual-versus-certificate distinction: GREEN. No lower bound on
  I12, a physical twelfth moment or the separate signed A_h follows.
- Full goal: GREEN scope control only. A future29/25 success would
  yield102/325; the sufficient unbounded fixed-order family and all
  original M1/M2/GAR and endpoint obligations remain unproved.

All checks are algebraic/analytical. Zero experiments or new source
audits were performed. GREEN validates the bounded failure report,
not a complete new arithmetic estimate.

## 6. Dependencies and exact provenance

Only the assigned claimant, protocol and accepted204/216 kernels
were used for this seam, alongside disclosed prior history. Exact
artifact hashes:

| Artifact | SHA256 |
|---|---|
| rounds/codex-managed/gc-actual-vector-gram-correlations/reports/actual_shifted_correlations.md | 6e0c9a229fa81d37c137c87197e66d2bfc6eddc4bb231f8eef256f51bf9fdbca |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |

My authorship of the separate current Gram-chain report is disclosed
but is not used to validate this claimant. No current sibling review,
isolated packet or new-round artifact was inspected. Only this review
file was written; claimant and shared-state artifacts were not edited.

## 7. Recommended state effect

Close this exact-hash review seam **GREEN**. Retain the exact
decomposition and scoped positive-certificate limitation as method
evidence; make no accepted estimate, exponent or graph promotion.
Keep the complete actual signed target and full-quarter objective open.
This reviewer stops after the assigned report.
