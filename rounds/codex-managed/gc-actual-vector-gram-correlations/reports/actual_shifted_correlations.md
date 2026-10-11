# Round221: actual pair increments and a completed divisor correlation

Campaign: `gc-actual-vector-gram-correlations`; task:
`actual_shifted_correlations`; discovery, selected context, NONBLIND.
Date: 2026-09-28. Graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Prior218--220 roles in this reused agent are disclosed. One mechanism:
pair increments, exact two-adic divisor hyperbola, and progression
completion. No experiments, new external theorem or sibling context.

## 1. Result: a small principal mode, but no complete gain

The complete signed target is not proved. For the actual masked
correlation on a block `n~N`, the mechanism gives an exact decomposition

    C_h^Q(R)=P_h(R)+A_h(R)+S_h(R)+D_h^Q(R),  1<=h<N,       (1)

where P is the zero progression-Poisson mode, A is the ENTIRE nonzero
mode package with endpoint corrections, S is the exact hyperbola square
correction, and D is the exact small-class deletion. Uniformly for
`R~T`, `Q=floor(T^(2/5))`, `Q<2N<=2T^(3/2)`, their proved prices are

    |P_h| << T^epsilon/(T h),
    |A_h| << T^epsilon N^(-1/2),
    |S_h| << T^epsilon N^-1,
    |D_h^Q| << T^epsilon Q^(1/2)N^-1.                      (2)

All carry the appropriate Schwartz decay for `N>T`. The first bound
uses the absolute radius anchor `R~T`; it is not a difference-only
operator estimate. The class mask is never differentiated or called
smooth. No shifted-convolution asymptotic is assumed.

The available estimate on A erases the arithmetic phase and leaves
the full pair-correlation capacity. Fejer reconstruction returns the
`N^(1/4)` block ceiling. More precisely, the resulting phase-erased
Fejer ceiling times actual second-moment certificate has cost

    c T N^2 <= certificate <= C_epsilon T N^(2+epsilon)   (3)

for every differencing length on actual positive blocks `N<=cT`,
`Q=o(N)`. Its complete block-summed price is `T^(3+epsilon)` and
has an actual-coefficient certificate lower bound `cT^3`. At the
critical block `N~T^(2/3)` its price is `T^(7/3+epsilon)`.
These are certificate bounds, not lower bounds on signed I12 or a
physical twelfth moment. The small principal mode alone does not
price the full arithmetic correlation.

Combining the attempted estimate with the stronger accepted fallback
leaves exactly `M12(B_T)<<T^(10 beta+epsilon)`, with
`beta=2 theta_LY-1/2`. There is no complete gain at `29/25` and no
pointwise exponent improvement.

## 2. Exact statement and hypotheses

Use the fixed actual mollifier and window of216, and

    a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    m_Q(n)=1_(sf(n)>Q),
    F_Q(R)=sum_(n>=1)a_n m_Q(n)e(R sqrt(n)),
    Z_Q(R)=Re(e(-3/8)F_Q(R)),
    M_p(G)=integral w(R/T)|G(R)|^p dR.

The accepted216 result pays the complete head at `T^(15/13+epsilon)`
and gives

    |M12(Z_Q)-I12(T,Q)| << T^(8 beta-1/5+epsilon).          (4)

Thus a complete estimate of M12(Z_Q) is an authorized route to I12.
No individual repeated-class term is assumed harmless: the collective
bound (4) is the dependency. The unique representation `n=d s^2`
with d squarefree retains every harmonic and every large class.

For a finite dyadic block, or any literal partial interval within it,
write `f_N(x)=x^-3/4 Psi(sqrt(x/T))` on its positive support, and put

    c_n=r2(n) f_N(n)m_Q(n)1_(n in the block),
    F_N(R)=sum_n c_n e(R sqrt(n)),
    C_h^Q(R)=sum_n c_n c_(n+h)e(R[sqrt(n+h)-sqrt(n)]),
    E_N=sum_n c_n^2.

Zero extension is literal. Coefficients are real and may have either
sign outside the positive control block. Negative increments satisfy
`C_-h=conjugate(C_h)`. The diagonal h=0 is E_N, treated separately.

Fix any integer `1<=H<=N`, with a harmless ambient integer interval
of length N for a partial block. The exact Fejer inequality is

    |F_N(R)|^2 <= (N+H-1)/H * B_H(R),
    B_H=E_N+2 Re sum_(1<=h<H)(1-h/H)C_h^Q(R)>=0.          (5)

It follows by writing each term H times in translated length-H sums
and applying Cauchy; `B_H=H^-1 sum_j|sum_(r=0)^(H-1)
c_(j+r)e(R sqrt(j+r))|^2`. Zero entries outside the positive block
are interpreted as zero, so no square root at a nonpositive integer
is required. This is finite algebra, including H=1 and empty masks.

All real cosine signs remain before an explicit sufficient enlargement:
if `Z_N=Re(e(-3/8)F_N)`, then exactly

    Z_N^2=(|F_N|^2-Im(F_N^2))/2,        |Z_N|<=|F_N|.     (6)

Thus the sum-frequency branch has its actual negative sine sign; it is
not discarded as a small term. Using the second inequality of (6)
dominates the complete real twelfth power, including all its sign
patterns. It is a stated upper-norm loss, not an identity between the
balanced complex moment and each real signed component.

## 3. Derivation, complete arithmetic costs and restoration

### 3.1 Exact divisor hyperbola with every two-adic class

For `n=2^s u` with u odd, complementary divisors give the finite identity

    r2(n)=4(1+chi4(u)) sum_(d|u,d<sqrt(u))chi4(d)
                          +4 1_(u square)chi4(sqrt(u)).  (7)

Indeed `chi4(u/d)=chi4(u)chi4(d)` for odd divisors. The first part
vanishes for `u=3 mod4`; for `u=1 mod4` it has coefficient8. The
second part is the single unpaired square divisor, with its actual
sign. This formula remains correct even when r2 vanishes.

Denote these two exact parts by B(n) and S(n). The condition for a
bulk divisor can be expressed as

    d odd,   n>2^s d^2,
    n=2^s d^2 (mod 2^(s+2)d).                            (8)

The congruence forces the exact two-adic valuation s and the odd
quotient `1 mod4`. Thus s does not introduce duplicate copies.
Opening B(n)B(n+h) gives coefficient `64 chi4(d)chi4(e)` and two
congruences of the form (8), with the second applied to n+h.

Put `g=gcd(d,e)`. Compatibility is the full condition

    4*2^min(s,t)*g divides 2^t e^2-2^s d^2-h.            (9)

In particular the exact two-adic residues are `n=2^s (mod 2^(s+2))`
and `n+h=2^t (mod 2^(t+2))`. For s=t they require
`2^(s+2)|h`. Condition (9), not merely `g|h`, is the necessary and
sufficient full CRT compatibility condition; otherwise the progression
is empty. Each compatible pair gives exactly one residue b modulo

    ell=lcm(2^(s+2)d,2^(t+2)e)
        =4*2^max(s,t)*de/g.                             (10)

There is no extra residue multiplicity. Its interval J is the
intersection of the original n and n+h supports with
`n>2^s d^2`, `n+h>2^t e^2`. It is one interval, possibly empty,
with the original strict/inclusive endpoint choices. The ranges are
`d<sqrt(2N/2^s)`, `e<sqrt(2N/2^t)` and finite s,t. This is the full
hyperbola, not a selected balanced-divisor subrange.

### 3.2 Exact progression completion and use of the radius anchor

For a compatible progression define

    G_h(x;R)=f_N(x)f_N(x+h)e(R phi_h(x)),
    phi_h(x)=sqrt(x+h)-sqrt(x).

Its progression sum has the exact half-endpoint Fourier completion

    sum_(n=b mod ell,n in J)^star G_h(n;R)
      =lim_(r up to1) ell^-1 sum_(nu in Z)r^|nu| e(nu b/ell)
             integral_J G_h(x;R)e(-nu x/ell)dx.          (11)

Here star means half the boundary values. Fourier periodization and
the Poisson kernel give (11) for the piecewise smooth compact function;
at a jump the limit is the average of the two one-sided values.
Adding or subtracting at most O(1) half-boundary values gives precisely
the original interval. Coincident endpoints and empty intervals are
handled by the same one-sided convention. The original literal value,
not a new starred convention, is restored.

Equation (11) is used with its entire Abel limit. No absolute sum of
the sharp-endpoint `1/nu` tails is claimed. Define P_h as the sum of
the nu=0 integrals, with all coefficients and compatibilities from
(7)--(10). Define A_h as the entire remaining Abel limit plus those
endpoint corrections. This is an exact finite-progression decomposition.

For `1<=h<N`, on the common support both x and x+h are comparable
to N. The derivative is negative and monotone, with

    |R phi_h'(x)|~T h N^(-3/2).

For each fixed B>0 let `W_B(N)=(1+N/T)^(-B)`. Schwartz seminorms
give `sup|f_N(x)f_N(x+h)|+TV(f_N(x)f_N(x+h))
<< N^(-3/2)W_B(N)^2`, where variation is inside J; its endpoints
are included separately in (11). Integration by parts with the
monotone first derivative consequently gives

    |integral_J G_h(x;R)dx| << W_B(N)^2/(T h).           (12)

This cancellation occurs before the coefficient norm. It uses
`R in[T/2,2T]`, and would not hold with that factor at R=0.

To sum the modulus factors, write `d=g alpha,e=g beta`, with
`(alpha,beta)=1`. Dropping restrictions only for an upper bound,

    sum_(s,t,d,e compatible) ell^-1
      <= C sum_(s,t)2^(-max(s,t))
              sum_(g|h)g^-1 (sum_(alpha<=sqrt(2N)/g)alpha^-1)^2
      << tau(h)log^2(2N).                               (13)

Both the two-adic sum and the displayed arithmetic multiplicity are
paid. Thus (12)--(13) prove the bound on P in (2), including every
unequal divisor pair and endpoint interval. No local-density asymptotic
or independence of the two divisor conditions is used.

### 3.3 Complete price of nonzero modes, squares and the actual mask

The available estimate on the WHOLE A_h is explicit. There are at most
`N/ell+1` integers per progression. The main counting term is bounded
by `N tau(h)log^2(2N)` using (13). The terminal count satisfies

    sum_(s,t) #{d<sqrt(2N/2^s),e<sqrt(2N/2^t)}
      << N sum_(s,t)2^(-(s+t)/2) << N.                   (14)

Hence, preserving all endpoints and all nonzero modes together,

    |A_h| <= |C_h^bulk|+|P_h|
      <<_epsilon W_B(N)^2 N^(-1/2+epsilon).             (15)

In the last step `h<=N<=T^(3/2)` and `T>=N^(2/3)` make the
principal-mode bound smaller than the displayed capacity, after
adjusting epsilon. This is a complete remainder estimate, although
far too large. It does not leave an unestimated Fourier tail or
silently sum the endpoint series absolutely. The loss occurs when
the actual character-weighted progression sums are replaced by the
count `N/ell+1`; (14) is one explicit source of the retained capacity.
No lower bound for A_h is inferred from this counting price.

The set where the odd part of n is a square contains O(sqrt(N))
integers in a block: sum the bounds `sqrt(N/2^s)` over s. Since
`|S(n)|<=4` and `|B(n)|<=r2(n)+4<<N^epsilon`, all three product
corrections `B(n)S(n+h),S(n)B(n+h),S(n)S(n+h)` total

    |S_h| <<_epsilon W_B(N)^2 N^(-1+epsilon).            (16)

For the class mask, use the exact factor

    m_Q(n)m_Q(n+h)-1
      =-1_(sf(n)<=Q)-1_(sf(n+h)<=Q)
                         +1_(both small).              (17)

There are at most `C sqrt(NQ)` small-class integers in the relevant
block when `Q<2N`, by summing `n=d u^2`, `d<=Q`; squarefreeness can
be dropped for this upper count. With the divisor bound on both
representation counts, (17) gives

    |D_h^Q| <<_epsilon W_B(N)^2 Q^(1/2)N^(-1+epsilon).   (18)

This is an exact signed correction before its stated norm. There is
no replacement of the arithmetic mask by a smooth function. If
`Q>=2N`, the masked block is empty and needs no such estimate.
Equations (11), (16) and (17) prove (1) with every coefficient and
multiplicity restored.

### 3.4 Fejer restoration of the entire joint correlation

Insert all four pieces of (1) in the signed bracket (5), and only
then apply the bounds above. Together with
`E_N<<T^epsilon W_B(N)^2 N^-1/2`, this yields

    |F_N(R)|^2 << T^epsilon W_B(N)^2
       [N^(1/2)/H + N log(2H)/(T H)
                         +N^(1/2)+1+Q^(1/2)].          (19)

Since `Q<2N`, the available complete bound is
`|F_N|<<T^epsilon W_B(N)N^(1/4)`, for every H. The principal
mode is small, and the exact mask correction would cost only the
amplitude `Q^(1/4)=T^(1/10+o(1))` in this restoration. Its gap below
the retained physical level `V0=T^(13/125)` is `1/250` in amplitude.
But neither observation deletes the `N^(1/2)` term supplied by A_h.

Thus this joint arithmetic opening has not beaten the old ceiling.
Obtaining a better signed estimate for the summed nonzero modes,
including their common progression residues and characters, is the
first missing analytic step. It is not granted as a shifted-convolution
theorem or relabeled as a proved smaller objective.

### 3.5 An actual-coefficient limitation of the phase-erased closure

The conductor suggested the unphased positive shifted-correlation
control; the following derives it and its complete certificate cost.
Choose an actual block `(N,2N]` with `N<=cT`, c fixed small enough
that `Psi>=1/2`, and assume `Q=o(N)`. Its retained coefficients are
nonnegative. Elementary lattice area comparison and the accepted
small-class mass bound give

    M=sum_n c_n ~ N^(1/4),
    E_N>=M^2/N >> N^-1/2,
    E_N<<_epsilon N^(-1/2+epsilon).                     (20)

In detail, full block mass is comparable to N^(1/4), while discarded
mass is at most C Q^(1/4)=o(N^(1/4)). This uses the actual r2 vector,
not a freely chosen or modulated example.

Put `U_h=sum_n |c_n c_(n+h)|` and define the positive ceiling

    Pi_(N,H)=(N+H-1)/H
                  [E_N+2 sum_(1<=h<H)(1-h/H)U_h].       (21)

For H>=2, partition the integer block into bins of length at most
`max(1,floor(H/2))`. There are O(N/H) bins. All pairs in the same
bin have Fejer weight at least1/2. Weighted Cauchy and (20) therefore
give the bracket in (21) at least

    c M^2/(N/H) >> H N^-1/2.

For H=1, (20) gives the same assertion directly. Conversely,
`U_h<<_epsilon N^(-1/2+epsilon)` from the divisor envelope, so

    c N^(1/2)<=Pi_(N,H)<=C_epsilon N^(1/2+epsilon)       (22)

uniformly for every `1<=H<=N`. A different choice of differencing
length does not save a power once the actual correlations are unphased.

The displaced second moment also has a direct uniform evaluation at
the precision needed here. Root spacing in the block gives
`|sqrt(n+h)-sqrt(n)|>=c |h|/sqrt(N)`. Fourier expansion of the smooth
window and `2|c_n c_m|<=c_n^2+c_m^2` imply, for any fixed A>1,

    M2(F_N)=T w-hat(0)E_N
                +O_A(T E_N (sqrt(N)/T)^A).             (23)

This follows by summing the Schwartz Fourier bound over all nonzero
integer differences h. Since `N<=T^(3/2)`, the error is uniformly
smaller than the main term for large T. No spacing or sign assumption
on the surviving mask is needed beyond deletion of indices.

The precise failed block certificate is

    C_(N,H)=Pi_(N,H)^5 M2(F_N),
    M12(Z_N)<=M12(F_N)<=C_(N,H).                         (24)

Equations (20)--(23) prove (3). Its lower bound is on the explicitly
positive right side of (24), NOT on its left side. It is therefore
compatible with substantial signed cancellation at radii R~T and
does not refute the desired physical moment. It also does not prove
a lower bound for the separate A_h package. The control diagnoses
exactly the phase-erased closure used to obtain (19).

### 3.6 All blocks, tails, levels and the final exponent

The upper part of (24) holds on every block with the Schwartz factors:

    M12(F_N)<<_epsilon T^(1+epsilon)N^2 W_B(N)^12.        (25)

For the full finite truncation `n<=T^(3/2)`, Minkowski gives

    ||sum_N F_N||_12
      <<T^(1/12+epsilon)sum_N N^(1/6)W_B(N)
      <<T^(1/4+epsilon),                               (26)

on choosing fixed B>1. The dyadic sum is O(T^(1/6)); literal partial
blocks only delete indices. Thus the complete attempted certificate
costs `T^(3+epsilon)`. It includes every unequal block through the
norm inequality, not an equal-block-only expansion. A dyadic block
`N~cT` satisfying (20) makes this particular block-summed certificate
at least cT^3. At `N~T^(2/3)`, (3) specializes to T^(7/3).

The full remaining `n>T^(3/2)` series is `O_A(T^-A)` uniformly in
R by the actual Schwartz/divisor envelope. Its twelfth norm and all
mixed terms are paid by Minkowski. The singleton, real top cutoff
and endpoint convention remain exact. Equations (4) and the head
moment then restore the full B_T and I12 bounds at the attempted
power3, with no unestimated complement.

This is weaker than the inherited COMPLETE estimate, so the strongest
conclusion of the attempt uses the accepted204/216 fallback. The
masked finite proof supplies

    D_(Z_Q)(V)<<T^epsilon(V^-2+T V^(-136/13)),  V>=1,
    sup_(R~T)|Z_Q(R)|<<T^(beta+epsilon),                 (27)

the latter from the actual B_T bound plus the paid head, not an
arbitrary-mask supremum theorem. Layer cake pays every level. Below
`V0=T^(13/125)`, the bound is
`T^epsilon[T+V0^10+T V0^(20/13)]<<T^(29/25+epsilon)`.
Above V0, with `W=T^(beta+epsilon)`, BOTH inherited high-level
terms remain:

    T^epsilon[W^10+T W^(20/13)+V0^10+T V0^(20/13)]
                          <<T^(10 beta+epsilon).       (28)

The paid head15/13 and repeated-class error8beta-1/5 are smaller.
Hence the complete outcome remains the original `10 beta` bound;
the missing improvement is `10 beta-29/25`. Neither the small P_h
term nor the mask correction eliminates either high-level obligation.

## 4. First doubtful or unproved step

There is no asserted target-sized shifted-convolution asymptotic.
The first unproved analytic input would be enough cancellation in
the complete character-weighted nonzero-mode package A_h, jointly
with its Fejer h weights and actual radius, to improve the full
twelfth norm. The established bound (15) is insufficient, and its
complete restoration is (25)--(28).

The positive control (22)--(24) proves that recovering a saving from
the same phase-erased pair correlations, merely by choosing H, cannot
work at the required power. It does not forbid a signed bound before
that erasure. Keeping the actual vector through (1) is useful only
if that remaining arithmetic phase is estimated; the exact identity
and small zero mode alone are not a complete gain.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Actual coefficients and class mask | Exact r2 hyperbola including the square divisor; exact mask correction(17), never treated as smooth. |
| Absolute radius anchor | Principal integral(12) uses R~T explicitly; it would not have this price at R=0. |
| All real signs | Exact real identity(6), with negative sum-sine branch; the complete norm domination is explicit and costs no omitted sign sector. |
| Multiplicities and singular cases | Full condition(9), one CRT residue, modulus(10), all two-adic valuations; h=0 separately, empty progressions/masks and H=1 valid. |
| Endpoints and aliases | Original strict/inclusive endpoints restored from Abel-completed half values; every integer nu remains in A_h. No absolute sharp-endpoint Fourier tail. |
| Complete levels, blocks and tails | Equations(25)--(28), full Schwartz tail, partial blocks and every unequal-block term paid. |
| Fixed vector versus operator | No arbitrary-vector operator grant. The certificate obstruction uses actual coefficients; no rephasing is used to refute actual high points. |
| No unproved source import | All new steps are finite divisor algebra, CRT, elementary Fourier completion, first-derivative integration and counting. Only accepted204/216 bounds are reused. |
| Statement-only rederivation | Not claimed by this discovery report. The displayed finite hyperbola/CRT and positive-certificate statements are available for the conductor's independent seam. No sibling packet was read. |
| Full goal | No complete gain. A future fixed twelfth success gives102/325 only; unbounded fixed orders or another complete route still needed for quarter. |

The raw positive-correlation lead came from the conductor. Its actual
binding, uniform-H version and extension to the full certificate cost
were derived above. Zero numerical or symbolic experiments were used.

## 6. Dependencies and exact artifacts

Read only the assigned brief and listed context; prior role history is
disclosed, not represented as blind access. SHA256 snapshots:

| Artifact | SHA256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `5ebf8c192da5f6cd10f15ce459b7968066dde913aedc155c1e72f5903057872d` |
| `strategy/round221_actual_vector_gram_and_correlations.md` | `a40cfd0421cb6c59c1c5121a7d1eef7f2f6ebcc9ef5ba3f904aebb7b369347a5` |
| `strategy/gauss_circle_strategy_checkpoint_round220_2026-09-28.md` | `6fc4b67a5de62a449527f62877933856635a9f6b0501a45f63539f05de6a5460` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md` | `603aa69cb4b757707d6eb89bb8290b05190b6b6d5cae83be52ddc19658ef68bb` |
| `rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md` | `8fb9d01885057aa2981da9a746890968212a73103b7a079fcbc65e640d598df9` |
| `rounds/codex-managed/gc-complete-signed-radical-kernel/synthesis.md` | `d34cf58dd298f4d50641c5135f24bec222106129d2d827929f16eafc6b49c814` |
| `rounds/codex-managed/gc-full-goal-arithmetic-source-review/synthesis.md` | `01939952d6f21510f1ed0b3ab069b2cc3b67d6c542d80ef31b22bc908db4a0b5` |
| Current task brief | `7c94e4b7e20195a8216e49a5ab093bf5996ec19fd6b85767a258eb1e7772e526` |

No source named inside those files was separately imported. The
new calculations do not rely on an unproved density formula for
r2(n)r2(n+h), on smooth arithmetic masks, or on the218 absolute
dual-tuple closure.

## 7. Recommended state effect

**No change** to the accepted graph, complete moment exponent, proof
draft or full-proof obligations. Retain the exact pair-correlation
decomposition and the narrowly scoped phase-erasure certificate
limitation as candidate method evidence, subject to independent review.
Do not promote the small principal mode as a complete estimate.

The signed I12 target stays open, as do every original M1/M2/GAR
and endpoint obligation. The sufficient family of unbounded FIXED
even orders at `I_p(T,floor(T^(1/p)))<=T^(5/4+epsilon)` remains
unproved; its conditional exponent is `1/4+7/[8(p+1)]`. Nothing
here permits p to grow with T or proves the quarter theorem.

Exit: `complete_actual_correlation_attempt_no_new_bound`. Only this
assigned report was written. Stop after its final hash; no successor
or shared-state artifact is started.
