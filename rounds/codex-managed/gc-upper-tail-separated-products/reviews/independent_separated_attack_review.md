# Independent review of the separated-product attack

Round232; campaign `gc-upper-tail-separated-products`; nonauthor reviewer `actual_near_product_payment`. Generated2026-10-12 Asia/Shanghai. Claimant: `reports/separated_product_attack.md`, SHA256 `e8974ef88d0c24e675cbfaf3328655a9cdff292fbff2999e5b9b79019be5fffc`, verified on read. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. This is the one authorized review after the reviewer's initial report was frozen.

## 1. Result and precise verdict

**Pass for the high-gcd component payment, tails, exact residual reduction, and the stated unsuccessful complete attempt.** The distinct-product sector with gcd(h,h')>=G satisfies

    C_(>=G)^abs << T^(1-6gamma+epsilon)/G,
    1<=G<=T^(1-2gamma), gamma=16/125.

At G=T^(1/4), the exponent is -9/500 and is strictly below the required -a*. The all-q tails, cross-rectangle costs, real endpoints and selected-set error do not spoil this saving. The correct unpaid sector is the signed sum with product gap>sqrt(T) and gcd(h,h')<T^(1/4).

**Pass for the actual g=1 control, with the certificate scope made precise here.** It disproves a pointwise positive-power alternation/variation saving asserted uniformly across actual smooth coefficient components, including fixed smooth refinements. It does not refute the actual exceptional-set target, an estimate after summing h,h', or a special estimate restricted to the unsplit frozen rectangle that does not claim stability under refinement. The claimant repeatedly states the component and pointwise scope; this review supplies the exact quantifier needed to interpret its informal “uniform” certificate. No numerical or algebraic correction to the frozen claimant is required.

No complete moment improvement is proved. The remaining estimate is substantive and is correctly left open.

## 2. Exact statement and hypotheses reviewed

Use the literal full F and E={|F|>T^gamma} from the frozen actual interface, dmu=w(R/T)dR, with real T>=2 and R in [T/2,2T]. The accepted/reviewed inputs are

    mu(E)<<T^(-2gamma+epsilon), Q_E(F)<<T^epsilon,
    F=S+e_T, ||e_T||infinity<<T^(-1/2+epsilon),
    S=sum_(j,h,q odd) U_(j,h,q),
    U_(j,h,q)=4T^(-1/2)chi4(q)
                       K_(j,h,R)((R^2-hq)/W_j),
    W_j=T/sqrt(N_j), h~H_j=TD_j/sqrt(N_j).

Every K is the actual real odd Schwartz kernel; all fixed seminorms are uniform, all q are genuine second-Poisson modes, and the O(log^2 T) smooth rectangles remain in the sum. The divisor factor4 is included once. Factor scales are bounded below, cX<N_j<CY, and X=T^(64/125), Y=T^(93/125). Let Wmax~T^(93/125), L=sqrt(T), G=T^(1/4).

For the exact decomposition in this review, C_close denotes the signed **ordered** atom sum with |p-p'|<=L, including p=p'; C_>=G and C_<G denote **twice the p<p' sums with p'-p>L**, split by the two complementary gcd conditions. The claim's stronger absolute high-gcd theorem covers all p!=p', but that stronger sector is not inserted wholesale into the identity: doing so would double count high-gcd near pairs.

The sufficient open statement is C_<G<<T^(-a*+epsilon), with a*=10beta-32/25. The statement is one-sided; none of these selected matrix bands is assumed positive semidefinite.

## 3. Independent derivation and seam review

### 3.1 All-q exterior and local tails

Put s=R^2. Outside [T^2/8,8T^2], one has |s-p|>=cT^2 for every R in the fixed window. A nonnegative decreasing Schwartz envelope summed on any shifted lattice of spacing2h satisfies

    sum_(|s-hq|>=cT^2) (1+|s-hq|/W_j)^(-A)
      << (1+W_j/h)(1+T^2/W_j)^(-(A-1)).

This follows by bounding at most one nearest point on each side separately and the rest by the tail integral divided by the spacing. It applies to the odd lattice and to negative q. Since W_j/h~1/D_j=O(1), H_j<<T sqrt(Y), and the number of rectangles is logarithmic, arbitrarily large fixed A pays the full exterior atomic l1 tail to every negative power of T. No divisor estimate with p~T^2 is applied to unbounded p.

Inside the fixed enlarged interval, each p has at most d(p) possible positive h, hence T^epsilon atomic multiplicity including rectangles. Therefore

    A_p=sum_(j,h|p)|U_(j,h,p/h)|
       <<T^(-1/2+epsilon)(1+|s-p|/Wmax)^(-A).

Its full lattice l1 sum is O(T^(-1/2+epsilon)Wmax). Restricting to |s-p|<=U, U=T^eta Wmax, discards an l1 tail at most

    T^(-1/2+epsilon)Wmax T^(-eta(A-1)).

For each desired output error, choose fixed eta>0 small relative to its epsilon and then choose A large. The retained total l1 mass is polynomial; multiplying it by either discarded tail pays every tail-core and tail-tail quadratic term, even on the full O(T) radius interval. Thus the absolute local truncation used in the count is valid. It is only an upper-bound device and never defines a new exceptional set or inherits F's ceiling.

### 3.2 Independent distinct-multiples count and high-gcd payment

Let I=[s-U,s+U], with arbitrary real s,U. If n_g counts the multiples of the positive integer g in I, then n_g<=2U/g+1. When n_g>=2, necessarily g<=2U and n_g-1<=2U/g; hence

    n_g(n_g-1)<=(2U/g+1)(2U/g)<=8U^2/g^2.

When n_g<=1 its distinct-pair contribution is zero. Summing over integer g>=G gives

    sum_(g>=G)n_g(n_g-1)<<U^2/G, for every real G>=1.

Each atomic pair whose exact gcd(h,h') is at least G gives one of these distinct multiple pairs, since g divides p=hq and p'=h'q'. Conversely, overcounting a center pair by every large common divisor is harmless for an upper bound. For a fixed p,p', the number of possible h,h' and rectangle choices is at most T^epsilon. Each atom product is O(T^(-1)). Therefore the absolute high-gcd sum is

    <<T^(-1+epsilon)U^2/G

pointwise, with all cross-rectangle multiplicities retained. Multiplying by mu(E), absorbing 2eta into epsilon, and restoring the rapid tails yields

    C_(>=G)^abs<<T^(-1-2gamma+epsilon)Wmax^2/G
                   =T^(1-6gamma+epsilon)/G.

The diagonal p=p' must be excluded: a single center can have divisors above2U, and the n_g(n_g-1) estimate does not count it. The claimant excludes it explicitly and pays it in the close sector. Thus no lost “+1” term invalidates the estimate.

At G=T^(1/4), 1-6gamma-1/4=29/125-1/4=-9/500. More generally strict slack below -a* requires delta>29/125+a*=0.241663519481... for G=T^delta. All real rounding effects are absorbed in the elementary interval count, not in an asymptotic density assertion.

### 3.3 Close sector, exact residual identity and errors

The inequality 2A_pA_p'<=A_p^2+A_p'^2 and at most2floor(L)+1 partners give

    sum_(|p-p'|<=L)A_pA_p'<<T^(-1+epsilon)(L+1)Wmax.

On E this costs T^(-3/250+epsilon) for L=sqrt(T), including every same-product and cross-rectangle pair. Uniform absolute convergence justifies the exact atom expansion

    Q_E(S)=C_close+C_>=G+C_<G

with the disjoint definitions in Section2. The broad absolute high-gcd bound can then bound the separated C_>=G without changing that identity.

Since int_E|e_T|^2dmu<<T^(-1-2gamma+epsilon), Cauchy against the accepted Q_E(F) gives

    |Q_E(S)-Q_E(F)|<<T^(-1/2-gamma+epsilon)
                         =T^(-157/250+epsilon).

It follows that

    Q_E(F)=C_<G+O(T^(-3/250+epsilon)
                     +T^(-9/500+epsilon)
                     +T^(-157/250+epsilon)).

The three paid exponents all lie below -a*. This is the claimed conditional reduction. Its baseline only gives C_<G<<T^epsilon and a small negative lower allowance; it supplies no new negative upper power. The selected-set error and mixed term are paid on the same original E.

### 3.4 Small-gcd progression spacing and the exact arithmetic

Write h=ga,h'=gb with (a,b)=1. If a,b are odd, all odd solutions to aq-bq'=2t differ by (2b,2a); their centers differ by2gab and their character product is chi4(ab)(-1)^t. Thus the claimant's A_t(s) parametrizes every admissible odd pair once and is independent of the representative chosen. If a,b have opposite parity, r is odd and the same admissible progression changes the character product's sign.

The fixed factor lower bound gives h,h'>>T/sqrt(Y)=T^(157/250). On g<G=T^(1/4),

    2gab=2hh'/g>>T^(503/500),
    Wmax~T^(372/500).

Choose eta<131/500 as well as sufficiently small relative to output epsilon. Then the progression spacing exceeds the entire local width2U. At fixed r and s, at most one progression element can have even its first center in that local interval. Hence the mixed-parity alternation offers no pointwise cancellation between two retained progression elements. This is a local structural statement; it does not rule out cancellation after integration against the actual E.

For odd a,b, changing t by1 gives the congruence increment q_(t+1)-q_t=2a^(-1) modulo2b, so a representative can jump across a substantial part of the center period2gab. Kernel smoothness alone does not make A_t slowly varying. Summation by parts against (-1)^t needs endpoints plus the actual discrete variation, as the claimant states. Bounding that variation by the absolute mass returns the stated T^(29/125+epsilon) certificate before the total-energy cap; all powers match.

### 3.5 Actual g=1 separated control and what it refutes

Take odd integral T, h=T,h'=T+4, W=T^(2/3), and the fixed nonnegative smooth component with d/T^(1/3) near1 and m/T^(1/3) near1/4. Its norm scale is a fixed multiple of T^(2/3), inside the plateau of phi for large T. Psi tends uniformly to1 on that support. For R/T near1 both stationary lines meet the positive amplitude interior, so the exact normalized K is bounded below on a fixed sufficiently small positive detuning interval. Its support and derivative bounds are uniform in T.

Choose integral u such that 8u-16 lies in [cW,2cW]. Such u exists for every sufficiently large odd T. Set q=T+2u and q'=q-4. Then

    gcd(T,T+4)=1, chi4(q)chi4(q')=1,
    (T+4)q'-Tq=8u-16~W>sqrt(T).

Choose s=p'+lambda W with fixed small lambda>0 and sufficiently small c. Both normalized detunings lie in the positive K interval, and R/T tends to1, inside the plateau of w. The chosen atom product is positive of size comparable to T^(-1).

For these fixed h,h', the other q and q' centers are separated from the chosen ones by at least2T and2(T+4), respectively. Since T/W=T^(1/3), every other pair has at least one rapidly decaying factor. Summing those tails on their lattices is O(T^(-K)) for any fixed K after choosing fixed derivative order. Thus for the unscaled A_t in the claimant's formula there is one t0=-(8u-16)/2=-4u+8 with

    A_(t0)>=c0>0,
    sum_(t!=t0)|A_t|=O_K(T^(-K)),
    sum_t|A_(t+1)-A_t|=2A_(t0)+O_K(T^(-K)),
    sum_t(-1)^t A_t=A_(t0)+O_K(T^(-K)).

Here t0 is even, and |2t0|>sqrt(T), so the principal term and its two variation jumps survive the separated restriction. This verifies the control quantitatively, including its other modes.

In precise terms, for any fixed delta>0, this control refutes both component-uniform certificates

    |sum_t(-1)^t A_t| << (g/W)^delta sum_t|A_t|,
    sum_t|A_(t+1)-A_t| << (g/W)^delta sum_t|A_t|,

on separated small-gcd weights of this smooth-component class. A conclusion allegedly derived only from alternation and uniform symbol smoothness would apply to these components and therefore fails. The control does **not** establish that its radii belong to E, a lower bound for F, or an obstruction to cancellations involving other h,h' or the complementary component. A certificate formulated only for an unsplit frozen rectangle with additional special information is not refuted by inserting a new refinement unless refinement stability is part of that certificate. This is the exact scope qualification required for the claimant's no-go language.

## 4. First doubtful or unproved step

The first unproved global statement remains the actual signed C_<G bound at -a*. The reviewed count proves an absolute payment only for the high-gcd component. The pointwise control rejects only the generic small-variation/alternation shortcut specified above, not the target.

No correction is required to the high-gcd exponent, distinct-pair count, all-q summation, cross-rectangle ledger, residual identity or error estimate. The necessary precision clarification is to attach the smooth-component-uniform quantifier to the claimed pointwise no-go. Reading that sentence as a theorem about the full frozen F or its E would exceed the evidence; the claimant's explicit final scope exclusions prevent that promotion.

## 5. Required controls and outcomes

- **High-gcd count: pass.** The n_g(n_g-1) bound is valid at every real endpoint, requires distinct products, and sums to U^2/G without a missing diagonal or additive term.
- **All modes and cross rectangles: pass.** Exterior and negative q are paid before the local divisor estimate; local tails are paid in atomic l1 and hence in all quadratic mixed terms. Logarithmic rectangle multiplicity is included.
- **Exact residual ownership: pass with definitions stated in Section2.** Close, separated high gcd and separated low gcd are disjoint. The stronger all-distinct high-gcd estimate is used only as a bound, not as an overlapping identity sector.
- **Small-g spacing and parity: pass.** The lower spacing exponent503/500 exceeds372/500 by131/500; eta can satisfy this and all epsilon budgets. The odd-odd and mixed-parity signs are correctly separated.
- **Actual g=1 control: pass at component scope.** Positivity, character, gcd, gap, real radius and rapid other-mode tails are all verified. It refutes the precise pointwise certificates above and no actual-E theorem.
- **Non-PSD and selected-set controls: pass.** Only total energy is positive. The actual E remains unchanged in every proved payment; no test-function replacement or mask ceiling occurs.
- **Complete budget: pass conditionally.** Near/high-gcd/error payments lie below -a*; the quadratic second tail is -27/325. Below-threshold twelfth terms, its boundary, the unchanged second upper tail, both complementary32/25 owners and the infinite tail remain paid. The missing first-tail saving is not concealed. Complete10beta remains the accepted result.
- **Isolation and preservation: pass for this review.** The claimant was frozen before access; this reviewer is its nonauthor. Only original authorized context and the claimant were read. Only this review was written; no claimant, state, graph, draft, matrix, synthesis or historical file was changed. No numerical experiment or external source was used.

## 6. Dependencies and exact artifacts used

The only newly read artifact was the frozen claimant `rounds/codex-managed/gc-upper-tail-separated-products/reports/separated_product_attack.md`, verified SHA256 `e8974ef88d0c24e675cbfaf3328655a9cdff292fbff2999e5b9b79019be5fffc`. Original authorized context and hashes were already recorded in this reviewer's initial report `rounds/codex-managed/gc-upper-tail-separated-products/reports/actual_near_product_payment.md`, frozen SHA256 `a4943d33174f49270506dcde6fb81a58412870daeec3dcf2c2686e175985a92a`; that initial artifact was not edited and is not a newly accepted premise.

The direct input scopes remain the same: the actual packet interface and Round231 nonauthor review supply the representation and symbol/error ledger; the accepted complete large-values kernel supplies the baseline distribution, actual ceiling and sharp restoration. The distinct-multiples count, spacing, arithmetic control and tail costs were checked independently above. No other Round232 sibling or blind report was read, and no graph promotion is assumed.

## 7. Recommended state effect

Retain the high-gcd component bound and refined signed residual as positively reviewed candidate evidence. Retain the pointwise no-go only with the precise component-uniform scope in Section3.5. No repair to the frozen mathematical formulas is required; any synthesis should carry that qualification explicitly.

Retain the actual small-gcd separated bound, target A, complete32/25, pointwise improvements and all quarter-target parents as open. This review licenses no complete theorem promotion. Freeze the review and stop; no successor or additional research task is proposed.
