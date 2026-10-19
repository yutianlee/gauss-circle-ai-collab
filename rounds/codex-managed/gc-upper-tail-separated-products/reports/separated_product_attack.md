# Separated products: a large-gcd payment and the unresolved small-gcd signed sum

Round232; campaign `gc-upper-tail-separated-products`; task `separated_product_attack`; discovery analyst. Generated2026-10-12 Asia/Shanghai. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Candidate evidence only. Selected-context assignment; no current-round sibling report or review read. No successor designed.

## 1. Result: component gain and a scoped failure of the shift argument

There is a further rigorously payable sector beyond close products. In the actual all-rectangle product expansion, let `g=gcd(h,h')`, and retain only pairs with distinct product centers. Their absolute contribution on the actual full-wave exceptional set E, restricted to `g>=G`, satisfies

    C_(>=G)^abs << T^(1-6gamma+epsilon)/G,
    gamma=16/125, 1<=G<=T^(1-2gamma).                 (1)

In particular, `G=T^(1/4)` gives `C_(>=G)^abs<<T^(-9/500+epsilon)`. This is below the sufficient target `T^(-a*+epsilon)`, where `a*=10beta-32/25=0.009663519481...`. The proof uses divisibility of both product centers by g, elementary counting of distinct multiples in one short interval, the exact divisor multiplicity, and the known measure of E. It does not assume a signed cancellation or a slow exceptional-set indicator.

I also independently verify the proposed close-pair payment `T^(-3/250+epsilon)`. All exterior and negative product tails, every rectangle, the stationary error and its cross term are paid below. Thus one may reduce the sufficient target further to the signed pairs

    |hq-h'q'|>sqrt(T),  gcd(h,h')<T^(1/4).            (2)

The explicit attempted cancellation in this remaining sector is summation by parts in the reduced product difference or, in the mixed-parity case, along its odd-solution progression. It does not give a saving: the actual weights are isolated on the progression, or jump with the Chinese-remainder representative, instead of varying slowly. An actual positive smooth coefficient component supplies a small-gcd, separated-product control that rules out the proposed uniform pointwise variation saving. It gives no lower bound on E and does not refute aggregate cancellation across h,h'.

The complete sufficient estimate remains open. The best resulting complete twelfth-moment exponent stays `10beta`, not `32/25`.

## 2. Exact statement and hypotheses

Use the frozen actual full band without alteration:

    gamma=16/125, X=T^(64/125), Y=T^(93/125),
    phi(n)=eta(n/X)-eta(n/Y),
    F(R)=sum_n phi(n)r2(n)n^(-3/4)Psi(sqrt(n/T))
                         cos(2pi R sqrt(n)-3pi/4),
    dmu=w(R/T)dR, E={R in supp(w(R/T)): |F(R)|>T^gamma}.

Here `T>=2` is real; rho, Psi, eta and w are the fixed functions in the frozen interface. In particular, `w>=0`, is supported in `[1/2,2]`, and is one on `[1/sqrt(2),sqrt(3)]`. Retain the accepted bounds

    mu(E)<<T^(-2gamma+epsilon),
    Q_E(F)=int_E |F|^2 dmu<<T^epsilon,
    ||F||infinity<<T^(beta+epsilon),
    beta=(50sqrt(1717)-297)/13762.

For every actual smooth rectangle j, `D_j M_j asymp N_j`, `X/constant<N_j<constant Y`, put

    W_j=T/sqrt(N_j), H_j=T D_j/sqrt(N_j), s=R^2,
    U_(j,h,q)(R)=4 T^(-1/2)chi4(q)
                         K_(j,h,R)((s-hq)/W_j),
    P_p=sum_(j,h: h|p, p/h odd) U_(j,h,p/h),
    S(R)=sum_(p nonzero) P_p(R), F=S+e_T,
    ||e_T||infinity<<T^(-1/2+epsilon).                (3)

The h ranges are the fixed enlarged positive stationary ranges, h comparable to H_j; q runs over every odd integer, including negative integers. Each atom contains the actual kernel

    b_h(d,R)=a_j(d,R^2d/(4h^2)) R sqrt(d)/(sqrt(2)h^(3/2)),
    K_(j,h,R)(u)=(sqrt(T)/2) int b_h(d,R)
                                       sin(pi W_j u d/(2h)) dd.

The factor4 owns `r2=4(1*chi4)` exactly once. The real kernels are odd Schwartz functions with uniform fixed seminorms; their slow R derivatives are retained. This report uses their envelope, not an arbitrary replacement coefficient sequence. There are `O(log^2T)` rectangles and all cross-rectangle pairs remain present.

Let `L=sqrt(T)` and `G=T^(1/4)`. Define the one-sided signed remainder

    C_<G=2 sum_(j,j') sum_(h,h': gcd(h,h')<G)
          sum_(q,q' odd: hq<h'q', h'q'-hq>L)
                 int_E U_(j,h,q) U_(j',h',q') dmu.   (4)

The sufficient, still unproved inequality is `C_<G<<T^(-a*+epsilon)`. This is an upper bound on the signed sum, not an assertion that the restricted band of its matrix is positive semidefinite. Define `C_>=G` by the complementary gcd condition; its absolute expansion is bounded by (1). The close sector includes both orderings and the product diagonal.

## 3. Proof, explicit summation attempt, and full costs

### 3.1 Exterior products, negative q, and safe local truncation

On the radius window, `T^2/4<=s<=4T^2`. First restrict product centers to the fixed enlarged interval `[T^2/8,8T^2]`; its complement has `|s-hq|>>T^2`. For a fixed h and rectangle, summation of the Schwartz envelope on the q lattice gives, for any fixed A>2,

    sum_(q odd, hq exterior) (1+|s-hq|/W_j)^(-A)
        << (1+W_j/h)(1+T^2/W_j)^(-(A-1)).           (5)

The spacing is 2h; `W_j/h` is bounded because the factor scale D_j is bounded below. There are only polynomially many h (`H_j<<T sqrt(Y)`), so increasing A makes the entire exterior atomic l1 sum `O(T^(-K))` for any fixed K. This proves the assertion for all negative q as well, without using a divisor estimate at unbounded p. There is no q=0 mode.

Inside this enlarged interval, `p asymp T^2`; for each p the number of contributing h is at most `d(|p|)<<T^epsilon`. Including all rectangles and their cross terms, the atomic absolute envelope therefore satisfies

    A_p(R):=sum_(j,h|p) |U_(j,h,p/h)(R)|
        << T^(-1/2+epsilon)(1+|s-p|/Wmax)^(-A),
    Wmax asymp T^(1-2gamma)=T^(93/125).              (6)

For any small fixed eta>0 truncate further to `|s-p|<=U`, where `U=T^eta Wmax`. The discarded atomic l1 sum is at most

    T^(-1/2+epsilon) Wmax T^(-eta(A-1)),

and hence is `O(T^(-K))` after choosing A. The retained l1 sum is polynomially bounded by `T^(-1/2+epsilon)Wmax`. Consequently the squares and every cross term involving either discarded tail are rapidly negligible even on the entire radius window. This moving truncation is used only in absolute upper bounds; it is not a new wave or exceptional set. Choose eta sufficiently small relative to the final epsilon before A. No ceiling for a mask is used.

### 3.2 Independent close-pair payment

Apply (6), using only that its decaying factor is at most one and that its integer sum is `O(Wmax+1)`. Then, uniformly in R,

    sum_(|p-p'|<=L) A_p A_p'
        <<T^(-1+epsilon)(L+1)Wmax.                  (7)

Integration on the same actual E gives

    C_close^abs <<T^(-2gamma+epsilon)(L+1)Wmax/T
                  <<T^(1/2-4gamma+epsilon)
                   =T^(-3/250+epsilon).             (8)

For the exact product diagonal `p=p'`, the same calculation with L=0 gives `T^(-4gamma+epsilon)`. Equation (7) pays all cross-rectangle and same-product divisor terms before making a signed subtraction. The close-pair matrix is not assumed positive.

### 3.3 Distinct multiples give a large-gcd saving

Work inside the local interval I=`[s-U,s+U]`. If `g=gcd(h,h')`, then g divides both p=hq and p'=h'q'. For p distinct from p', necessarily `g<=|p-p'|<=2U`. For each fixed g, let n_g be the number of multiples of g in I. When `n_g>=2`, one has g<=2U and

    n_g(n_g-1) <= (2U/g+1)(2U/g) << U^2/g^2.        (9)

For `n_g<=1` the left side is zero. Thus the number of ordered distinct-center pairs counted with all possible common divisors at least G is bounded by

    sum_(G<=g<=2U) n_g(n_g-1) << U^2/G.              (10)

The exact number of h,h' pairs above each p,p' is at most `d(p)d(p')`, with the logarithmic rectangle multiplicity already paid. Counting every common divisor in (10) overcounts the exact gcd classes and is therefore lawful for an absolute upper bound. Each atomic product is `O(T^(-1))`, and divisor/rectangle losses are `T^epsilon`. Hence

    sum_(p!=p', gcd(h,h')>=G) |U_(j,h,q) U_(j',h',q')|
                      << T^(-1+epsilon) U^2/G.       (11)

Integrate (11) over E, absorb the local enlargement into epsilon, and restore the rapid tails from Section3.1. This proves

    C_(>=G)^abs <<T^(-1-2gamma+epsilon)Wmax^2/G
                  =T^(1-6gamma+epsilon)/G.          (12)

This bound even pays distinct products closer than L in the large-gcd sector; its application to the separated sector is weaker and therefore valid. For `G=T^(1/4)`, its exponent is `1-96/125-1/4=-9/500`. More generally, a choice `G=T^delta` works below the target when `delta>1-6gamma+a*=0.241663519481...`. The argument removes a component; it does not estimate the small-gcd signed sum.

### 3.4 Reduced gcd arithmetic and the attempted shift summation

Fix j,j',h,h', put `h=ga,h'=gb`, `(a,b)=1`, and set `r=aq-bq'`. Then `p-p'=gr`. For odd a,b the odd solutions have r even and

    chi4(q)chi4(q')=chi4(ab)(-1)^(r/2).              (13)

For opposite-parity a,b, r is odd and the sign alternates along the odd-solution progression `(q,q') -> (q+2b,q'+2a)`. These statements include all boundaries and do not change the smooth kernels.

For odd a,b write r=2t. Choose an odd solution q_t,q'_t of `a q_t-b q'_t=2t` when it exists and put p_t=ga q_t. The full covariance weight at fixed s is

    A_t(s)=sum_(k in Z)
       K_(j,h,sqrt(s))((s-p_t-2gabk)/W_j)
       K_(j',h',sqrt(s))((s-p_t+2gt-2gabk)/W_j').     (14)

Every admissible pair is present exactly once in (14); choosing another representative merely shifts k. The separation condition is `|2gt|>L`. The character factor in front of (14) is `chi4(ab)(-1)^t`. The E indicator remains `1_E(sqrt(s))`, independent of how solutions are parametrized.

Summation by parts against `(-1)^t` costs endpoints plus

    sum_t |A_(t+1)(s)-A_t(s)|.                       (15)

The hoped-for estimate making this useful was a small variation factor of order g/W on the right side of (15), rather than its full absolute mass. It is not justified by kernel smoothness: solving the congruence advances q_t by `2 inverse(a) mod b`, so p_t generally jumps a substantial fraction of `2gab`. The representatives do not move by O(g) as t advances. Smoothness in the kernel argument therefore gives no slow variation in t.

In the mixed-parity case, the alternating progression has center spacing `2gab=2 lcm(h,h')`. For the entire small-gcd sector, the factor scales imply

    h,h' >> T/sqrt(Y)=T^(157/250),
    2gab >> T^(2*(157/250)-1/4)=T^(503/500).

This is much larger than `Wmax=T^(372/500)`, and remains so after the small T^eta enlargement. Thus for fixed r and fixed s there is at most one local progression element; an alternating sign cannot cancel such an isolated term. Averaging over s would require a new estimate for its product with the actual `1_E(sqrt(s))`; no variation or equidistribution of that indicator has been established.

Taking absolute values in (15), or in the mixed-parity progression, simply returns

    int_E (sum_p A_p)^2 dmu
        <<T^(-1-2gamma+epsilon)Wmax^2
         =T^(29/125+epsilon).                        (16)

The bound is worse than the accepted total energy. The exact decomposition `Q_E(S)=C_close+C_>=G+C_<G`, together with (8), (12), and `Q_E(S)<<T^epsilon`, caps the one-sided remainder at `C_<G<<T^epsilon`; it produces no negative power. This records the complete cost of the attempted elementary shift mechanism, rather than only its sign identity.

### 3.5 Actual separated, small-gcd control for the failed pointwise step

Here is an algebraic control using an actual smooth component, not arbitrary signs. Let T tend through odd integers, take `N=T^(2/3)`, `D=M=T^(1/3)`, and set `h=T,h'=T+4`, so g=1 and a,b are odd. Insert fixed nonnegative smooth factor cutoffs into the actual divisor amplitude with d/D in a small interval about 1 and m/D in a small interval about 1/4. This component and its complementary amplitude sum back to the original band. On this support phi=1 for large T and `Psi(sqrt(dm/T))` is positive, since Psi(0)=1. Both stationary amplitudes are positive for R/T close to one, and their kernel sine is positive for sufficiently small positive detuning u.

Put `W=T^(2/3)`. Choose an integer u with `8u-16` in `[cW,2cW]`, for a sufficiently small fixed c>0; set

    q=T+2u, q'=q-4,
    p=Tq, p'=(T+4)(q-4), p'-p=8u-16.                (17)

Both q,q' are odd, have the same character, and `gcd(h,h')=1`. The difference in (17) exceeds sqrt(T) for large T. Choose s just above p', so both `(s-p)/W` and `(s-p')/W` are fixed positive small numbers in the positive sine range. Then each actual kernel is bounded below by a positive constant and their covariance atom, including its character sign, is positive of size comparable to `T^(-1)`.

For these fixed h,h' and s, the q spacing moves a center by 2h, and the q' spacing by 2h'; both are much larger than W. The chosen pair is therefore the only local pair, while every other pair is rapidly small by the Schwartz envelope. In (14) it is an isolated positive weight at one t. Its alternating sum is comparable to its absolute sum, and its discrete variation is comparable to that sum, not smaller by g/W. This disproves a uniform positive-power pointwise saving based solely on alternation and smoothness, even after both the near-product and large-gcd sectors have been removed.

This is a control for an actual coefficient component at ordinary real radii. It does not assert that these radii belong to E, does not transfer the full F ceiling to the component, and does not show a lower bound for the full band, its exceptional energy, or its moment. Cancellation after summing h,h', or a genuinely E-dependent estimate, is not excluded.

### 3.6 Error and complete-moment ledger

The original stationary error satisfies

    int_E |e_T|^2 dmu<<T^(-1-2gamma+epsilon).

Using the accepted `Q_E(F)<<T^epsilon`, the difference between the leading and original restricted energies is

    |Q_E(S)-Q_E(F)|
       <=2 Q_E(F)^(1/2)||e_T||_(L2(E))+||e_T||_(L2(E))^2
       <<T^(-1/2-gamma+epsilon).                    (18)

The exponent `-1/2-gamma=-157/250` is below -a*. All exterior/local discarded product tails are rapidly negligible by Section3.1. Consequently (4) at exponent -a* would indeed imply the sufficient actual estimate `Q_E(F)<<T^(-a*+epsilon)` using (8), (12), and (18).

Below the threshold `V0=T^gamma`, the accepted distribution pays the full twelfth budget

    max(1,10gamma,1+20gamma/13)=32/25,

including the threshold boundary. Above it, the unchanged quadratic second tail is `T^(-27/325+epsilon)`; the first tail still only gives `T^epsilon`. Assuming the open estimate (4), the actual ceiling pays the high twelfth tail by `T^(10beta)Q_E(F)<<T^(32/25+epsilon)`. Without it the high first tail remains `T^(10beta+epsilon)`. The unchanged twelfth second tail is `T^(1+20beta/13+epsilon)`, below32/25.

The exact outer decomposition is `B=L+F+H`; both complementary owners have full twelfth budget32/25 and the infinite high norm tail belongs to H. No factor-restricted C+U substitution is used: every U contribution remains in F. Every epsilon loss is chosen after the output epsilon, including the actual ceiling loss. The accepted Bessel and sharp smoothing remainders belong to the existing reconstruction and are not reclassified as a signed gain. Even the conditional complete32/25 result would be a moment improvement only; it does not improve the current pointwise benchmark or close the quarter theorem.

## 4. First doubtful or unproved step

The first invalid attempted shortcut is a small-variation bound for (15), or a cancellation factor for the isolated mixed-parity progression. Section3.5 gives an actual small-gcd separated-product control against the former; the spacing calculation gives the reason the latter has no pointwise cancellation. Neither a CRT parametrization nor the alternating character supplies the needed estimate.

After the rigorously paid sectors, the precise remaining unproved statement is

    2 sum_(j,j',h,h',q,q': gcd(h,h')<T^(1/4),
                            h'q'-hq>sqrt(T))
        int 1_E(R) w(R/T) U_(j,h,q)(R)U_(j',h',q')(R)dR
                       <<T^(-a*+epsilon).            (19)

Here E is selected by the entire original F. It cannot be replaced by a rectangle event, a smooth test, an independent set, or a mask inheriting F's ceiling. The elementary signed attempt has not estimated (19) beyond the zero-power energy cap. This is a failed bounded mechanism, not a no-go theorem for (19), target A, or every aggregate dispersion argument.

## 5. Required controls and outcomes

- `actual_packet_definition`: pass. Every original amplitude, divisor factor4, all odd Fourier modes, real branch, and rectangle owner are retained in (3).
- `same_product_and_near_pairs`: pass analytically. Exact products cost `T^(-4gamma+epsilon)`; absolute near payment costs `T^(-3/250+epsilon)`. No pairwise decorrelation is asserted.
- `separated_signed_target`: partially paid. The distinct-product `g>=T^(1/4)` sector costs `T^(-9/500+epsilon)`; (19) remains open.
- `selected_set_not_slow_test`: pass. All proved payments use only the actual E and its known measure; the failed averaging step is identified explicitly.
- `all_scales_tails_errors`: pass at the stated inherited-symbol interface. Equations (5)-(6) pay exterior and negative q, local tails, all cross terms and every rectangle. Equation (18) pays the first-transform error on E.
- `non_psd_band_control`: pass by absolute payment. Positivity is used only for total `Q_E(S)`, never for a selected close or separated matrix band. A simple independent control is the three-center close matrix `[[1,1,0],[1,1,1],[0,1,1]]`: on vector `(1,-sqrt(2),1)` its quadratic form is `4-4sqrt(2)<0`.
- `both_tail_complete_budget`: pass conditionally. Threshold boundary, quadratic second tail `-27/325`, high first owner10beta, second twelfth owner `1+20beta/13`, and both complementary32/25 owners are explicit. No complete gain follows yet.
- `blind_isolation`: pass for this selected-context task. No current-round sibling report, review, or blind packet was accessed. The historical named reports were permitted context.
- `graph_and_history_preservation`: no shared state, proof draft, matrix, synthesis, or legacy file edited. Only the assigned report was written. The current graph hash agrees with the starting hash.

No numerical experiment or external theorem was used; the argument and the finite matrix control are algebraic. Analytical effort exceeds95 percent. File reads and cryptographic hashes are provenance operations, not mathematical experiments.

## 6. Dependencies and exact artifacts used

The accepted distribution kernel supplies the generic distribution/energy input. The frozen interface and reviewed Round231 artifacts supply the exact actual packet representation, uniform symbols, stationary error, actual ceiling and full complementary moment ledger. All newly claimed counting and gcd-sector inequalities are proved here. No unlisted source theorem, source card, or sibling claim is used. The conductor's one mid-task message independently confirmed the distinct-multiples count and requested the full small-gcd ledger; it supplied no missing signed estimate.

The initial broad graph display was truncated; the authoritative `GC-target` and `GC-complete-square-root-large-values-moment-bound` entries were then read by exact JSON selection. No neighboring claim was imported. Exact authorized-context hashes:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 9725379d3b9003f322ce541776a886aa3d493511da4a0b75316e4211d10e80cf |
| rounds/codex-managed/gc-upper-tail-separated-products/briefs/separated_product_attack.md | c67d5a03c75b25fc62b260341a63120aef90e36aba195a6f8d83c8f55f521aac |
| rounds/codex-managed/gc-upper-tail-separated-products/briefs/actual_interface.md | c52e963aa8836fc7663c0528e170f4271396a907eafbee1ecc682db5d5885607 |
| rounds/codex-managed/gc-actual-upper-tail-a/synthesis.md | 8f8e7a07d2238728b4f672cc3694ad3431d8c146b7689738c0210452434784a3 |
| rounds/codex-managed/gc-actual-upper-tail-a/reports/signed_upper_tail_attack.md | ccd6592b215eecd1c38909fb088d40de2f0ea0b1916b1e568a58d54ba3c94e20 |
| rounds/codex-managed/gc-actual-upper-tail-a/reports/resonance_hostile_controls.md | 89693f8519e735dbdd9582850e5465c85fef30835aeab50e398b16fe34f837e8 |
| rounds/codex-managed/gc-actual-upper-tail-a/reviews/independent_signed_tail_review.md | dbcb1eb37c35c50e9cf69220ed235708de8252e9fde7737f79809bd6c93e8235 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |

## 7. Recommended state effect

Retain the independently derived near-product payment, the distinct-product large-gcd bound (12), and the precise residual (19) as candidate component evidence, subject to nonauthor seam review. Retain the actual small-gcd control as a rejection of the specified pointwise alternation/variation shortcut only. Do not promote target A, complete32/25, a pointwise improvement, any M1/M2 parent, or the quarter target. No accepted graph or proof-draft change is recommended by this report. Freeze the report, return its SHA256, and stop.
