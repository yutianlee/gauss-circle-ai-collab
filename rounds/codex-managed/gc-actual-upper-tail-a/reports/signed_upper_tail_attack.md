# Actual upper tail: exceptional-set quadratic energy and the signed product seam

Round231, campaign `gc-actual-upper-tail-a`; task `signed_upper_tail_attack`; discovery/claimant. Generated 2026-10-11. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Candidate evidence only. Initial bounded analytic attempt; no sibling reports read and no successor designed.

## 1. Result: a sufficient quadratic target, and failure of the first-average route

Put gamma=16/125, V0=T^gamma, and

    a*=10 beta-32/25=0.009663519481... .

For the literal actual full band F in the frozen interface, the following **unproved quadratic estimate is sufficient** for the requested complete moment:

    Q_tail(F):=integral_(|F|>V0) |F(R)|^2 dmu_T(R)
                  <<_epsilon T^(-a*+epsilon).                 (Q)

The already accepted distribution proves only Q_tail(F)<<T^epsilon. Target A would prove the slightly stronger Q_tail(F)<<T^(-1/100+epsilon). Thus the missing saving has an exact quadratic exceptional-set formulation; one need not directly estimate a twelvefold product to make a sufficient attempt.

I attempted (Q) using the odd reciprocal kernels and radius averaging. The full signed first average does have arbitrarily strong smooth-window cancellation. Nevertheless the quadratic product of two odd kernels is even, and the actual high-level-set indicator is not a slow test. The averaging step required to replace it by a slow or constant test is unproved. The explicit, fully normalized missing inequality is (P) below, a signed covariance bound on the **actual exceptional set**, with required exponent 2-a* instead of the available 2. No new upper-tail saving is proved.

This is a scoped obstruction to the tested first-average/oddness argument, not an impossibility result for actual signed aggregate methods or target A. The report also gives an actual-coefficient mean-square control distinguishing strong signed first-average cancellation from small quadratic energy. It gives no actual high-tail lower bound.

## 2. Exact statement and hypotheses

Use exactly the fixed real radial rho, real Schwartz Psi, smooth nonnegative w, real T>=2, beta, and eta specified in `briefs/actual_interface.md`. In particular

    X=T^(64/125), Y=T^(93/125),
    phi(n)=eta(n/X)-eta(n/Y),
    F(R)=sum_n phi(n)r2(n)n^(-3/4)Psi(sqrt(n/T))
                        cos(2 pi R sqrt(n)-3 pi/4).

The coefficients are fixed as R varies. The accepted actual ceiling is

    ||F||infinity <<_delta T^(beta+delta),

obtained through the paid actual decomposition, never through arbitrary masks. Let E={R: |F(R)|>V0} within the support of w. The set E depends on the entire actual F. This dependence must be preserved in every restricted covariance below.

For the reciprocal formulas, decompose the exact identity r2(n)=4 sum_(dm=n)chi4(d) using smooth dyadic factor partitions. Every rectangle has DM comparable to N, X/constant<N<constant Y, and real amplitude a(d,m) supported in fixed dilates of D,M with

    |partial_d^j partial_m^k a| << N^(-3/4)D^(-j)M^(-k).

There are O(log^2 T) rectangles in total. This is the full smooth band, with singleton factor scales and both cutoff transitions retained. No sharp adaptive factor mask is introduced.

For an individual rectangle put W=T/sqrt(N), H=T D/sqrt(N), s=R^2. For the fixed enlarged positive range h comparable to H, set

    b_h(d,R)=a(d,R^2 d/(4h^2)) R sqrt(d)/(sqrt(2) h^(3/2)),
    K_(h,R)(u)=(sqrt(T)/2) integral b_h(d,R)
                             sin(pi W u d/(2h)) dd.          (K)

These are real odd Schwartz kernels, with uniformly bounded fixed Schwartz seminorms. Their R derivatives, with u held fixed, cost O(T^-1) per derivative. Rectangle indices on W,b,K are suppressed only in displays.

## 3. Proof and quantitative derivation

### 3.1 The quadratic sufficient condition and both inherited tails

Write q=136/13. The exact layer-cake identity is

    Q_tail=V0^2 D_F(V0)+2 integral_(V0)^infinity V D_F(V) dV.

Use the actual ceiling C_delta T^(beta+delta) as the upper endpoint. The accepted first term V^-2 contributes O(T^epsilon log T), including the threshold boundary. The unchanged second term contributes

    T V0^(2-q)=T^(1-(110/13)(16/125))=T^(-27/325).    (1)

Consequently Q_tail<<T^epsilon. If A is assumed, the same calculation gives Q_tail<<T^(-1/100+epsilon)+T^(-27/325+epsilon). All epsilon and ceiling losses can be chosen after fixing the desired output epsilon.

On E, |F|^12<=||F||infinity^10 |F|^2. Therefore (Q) implies

    integral_E |F|^12 dmu_T << T^(10 beta-a*+epsilon)
                                      =T^(32/25+epsilon).   (2)

Below V0 the old distribution and layer cake give the complete upper budget

    max(1,10 gamma,1+20 gamma/13)=32/25.

The threshold boundary in the twelfth-moment calculation is already included at that same budget. Hence (Q) proves the full F moment and the integrated excess target. The exactly paid L,H owners restore B at 32/25 by the finite L12 norm inequality. U is not used or omitted: it belongs to F because this task keeps the full band. If one subsequently uses C+U, the separately paid U has the same sufficient budget.

The first-tail slack in the displayed target A is

    1/100-a*=0.000336480519...>0.

The original second-tail contribution to the twelfth moment remains

    1+20 beta/13=1.198409772228...<32/25.

Nothing here improves the pointwise exponent. Complete 32/25 would have the known persistence consequence 207/650, which does not beat the accepted benchmark.

### 3.2 Exact reciprocal product covariance with every q owned

The inherited, reviewed one-variable stationary calculation gives

    I_h(d)=b_h(d,R)e(R^2 d/(4h)-1/8)+error.

Multiplication by the circle phase e(-3/8) makes the real leading term

    -Re sum_d chi4(d)b_h(d,R)e(s d/(4h)).               (3)

The negative branch is already the complex conjugate implicit in this real part. It is not an additional independent cancellation.

Apply exact Poisson summation to the smooth compact d amplitude in (3). With hat b(xi)=integral b(d)e(-xi d)dd and alpha=s/(4h),

    sum_d chi4(d)b_h(d)e(alpha d)
       =(i/2) sum_(q odd) chi4(q) hat b_h(q/4-alpha).

Thus (3) equals T^(-1/2) sum_(q odd)chi4(q)K_(h,R)((s-hq)/W). This q sum consists of distinct Fourier indices from a second Poisson formula. It does **not** sum repeated copies of the elementary identity obtained by choosing different nearest q labels for one fibre. All odd integer q are retained; far and negative q are rapidly decaying and may simply remain in the convergent sum.

Including the divisor factor 4 and every rectangle, define

    S_T(s)=4 sum_(rectangles j) sum_(h comparable H_j) sum_(q odd)
                  chi4(q)K_(j,h,sqrt(s))((s-hq)/W_j).

Then the actual full band satisfies

    F(R)=T^(-1/2) S_T(R^2)+E_T(R),
    ||E_T||infinity <<_epsilon T^(-1/2+epsilon).       (4)

For completeness, the per-rectangle stationary error before the d,h sum is N^(-3/4)M(R sqrt N)^(-3/2). The summed error is O(D R^(-1/2)N^-1), at most O(T^-1/2) because M is bounded below. Nonstationary frequencies are smaller by repeated integration by parts. O(log^2 T) rectangles only change epsilon. The full band is finite; the infinite complementary H tail is exactly owned and paid by the frozen interface. There is no new Bessel remainder in (4), which represents the already defined F; sharp-discrepancy restoration, if invoked, retains the accepted Bessel and smoothing errors separately.

Uniform kernel bounds follow from b having size T^-1/2 D^-1, d support length O(D), and Wd/h comparable to one. Smooth integration by parts in d proves rapid decay in u. At u=0 the kernel is exactly zero, but its size is generally order one at physical detuning |s-hq| comparable to W.

Let E_s={s: sqrt(s) belongs to E}. The exact normalized sufficient covariance target is

    integral_(E_s) w(sqrt(s)/T)|S_T(s)|^2 ds
                       <<_epsilon T^(2-a*+epsilon).       (P)

Indeed dR=ds/(2sqrt(s)), sqrt(s) comparable to T, and the extra amplitude squared in (4) is T^-1. Hence (P) gives (Q), up to the error discussed next. Expanding |S_T|^2 makes (P) a definite signed sum with signs chi4(q)chi4(q'), kernel products, and the same actual indicator 1_(E_s). It includes coincident products and coincident frequencies; none is removed.

The error cannot be paid using the whole radius interval if seeking negative-power Q_tail. Instead use the known measure of E:

    D_F(V0)<<T^(-2gamma+epsilon),
    integral_E |E_T|^2 dmu_T <<T^(-1-2gamma+epsilon).

This is smaller than T^-a*. The mixed term follows from Cauchy or |x+y|^2<=2|x|^2+2|y|^2. Conversely, the accepted Q_tail bound and (4) give only the corresponding bound T^(2+epsilon) in (P). The precise missing covariance saving is therefore a*, with no hidden normalization loss.

### 3.3 What signed radius averaging actually proves

For any one actual smooth norm shell F_N and every real interval [A,B] within the radius range, direct integration of its exact cosine expansion gives

    |integral_A^B F_N(R)dR| <<_epsilon N^(-1/4+epsilon). (5)

The endpoint primitive divides each coefficient by 2 pi sqrt(n), and sum_(n comparable N)r2(n)n^(-5/4)<<N^-1/4+epsilon. There is no endpoint or integer-radius exception. If v is a fixed smooth compact window, repeated integration by parts gives, for each fixed k,

    |integral v(R/T)F_N(R)dR|
               <<_(k,epsilon) T N^(1/4+epsilon)(T sqrt N)^(-k). (6)

These are strong signed first-average estimates on actual coefficients. They are compatible with a substantial actual quadratic diagonal. Choose any fixed nonzero smooth nonnegative shell inside the plateau 2X<n<Y, with N well inside that range. Since N/T tends to zero, Psi is bounded below there for large T. The elementary lattice-area count on a fixed annulus gives sum r2(n) comparable to N, so Cauchy yields

    sum_n |a_n|^2 >> N^-1/2.

Expanding F_N^2 on a fixed interval of length comparable to T, the difference-frequency off-diagonal is at most

    C sqrt(N) log(2N) sum_n |a_n|^2,

using |sqrt(n)-sqrt(m)|^(-1)<<sqrt(N)/|n-m| and 2|a_na_m|<=|a_n|^2+|a_m|^2. The sum-frequency part is O(N^epsilon), from |sqrt(n)+sqrt(m)|^-1<<N^-1/2 and the coefficient l1 bound. Since sqrt(N) log N=o(T),

    integral F_N(R)^2 dR >> T N^-1/2.                 (7)

This is an actual arithmetic control, not an adversarial coefficient model. It proves only that (5)-(6) cannot be interpreted as small unrestricted quadratic energy. It gives no lower bound on E, on Q_tail, or on a complete twelfth moment.

For product kernels the same obstruction is visible before summation: K is odd but K(u)K(u) is even and has a positive integral whenever K is nonzero. Reflection eliminates a signed first mean, not a covariance diagonal. Restricting to the actual E_s is even more delicate: no reflection invariance or slow variation of that set has been established.

The elementary period-four cancellation is also not a bound on one local product window. The near-product width gives

    q-window length W/h comparable to 1/D,
    h-window length W/q comparable to 1/M,

with q comparable to T sqrt(N)/D. These are bounded or subunit lengths, so summing complete character periods in a fixed fibre supplies no new power. This is the point at which the attempted local averaging proof of (P) stops.

## 4. First doubtful or unproved step

The first unproved claim is exactly (P), or another estimate strong enough to imply (Q). In expanded form it requires controlling the actual restricted signed correlations

    integral 1_(E_s) w(sqrt(s)/T)
       K_(j,h,sqrt(s))((s-hq)/W_j)
       K_(j',h',sqrt(s))((s-h'q')/W_j') ds

after summation with chi4(q)chi4(q'), with all rectangles retained. The desired total is T^(2-a*+epsilon). The accepted machinery pays only T^(2+epsilon).

Neither the small signed first averages (5)-(6), nor a whole-line covariance calculation, nor a slow-test covariance calculation can be substituted for this statement. The indicator is selected by the same full wave whose energy is being bounded. No independence, smoothness, reflection symmetry, or small boundary variation of that indicator has been proved. Applying Cauchy or absolute values before this correlation estimate reverts to the inherited certificate and supplies no a* saving.

This is a precise unsuccessful bounded attempt. The quadratic target itself is a conditional reduction, not newly accepted mathematics solving the target. The results do not assert an arithmetic lower bound saturating the old estimate or reject every possible covariance argument.

## 5. Required controls and outcomes

- Actual coefficients: retained r2=4(1*chi4), the fixed Psi and phi, and radius-independent factor partitions. No arbitrary mask inherits the actual ceiling.
- Real phase: the combined shifts give -Re exactly. Exact product detuning zero kills the leading odd kernel. Physical detuning of scale W does not; the inherited real-fibre control remains valid.
- q ownership and branches: q is a unique Fourier index in exact second Poisson, including its congruence sign. No nearest-q duplicates; the conjugate branch is contained in Re.
- Covariance control: the actual diagonal (7) and the even product of two odd kernels rule out interpreting mean cancellation as energy cancellation. They do not give a high-level-set lower bound.
- Endpoints and errors: sharp real interval endpoints are retained in (5); all stationary errors are summed in (4). Their high-tail energy is paid using D_F(V0), not the full O(T) measure.
- Both tails and threshold: (1) is -27/325; target A gives a quadratic saving 1/100. The sufficient saving a* is 0.009663519481.... The twelfth second-tail exponent is 1.198409772228....
- Full restoration: F contains all factors in the full band; L,H are paid at 32/25. The integrated tail boundary and finite norm inequality are explicit. No pointwise improvement is claimed.
- Isolation, scope and resource: no siblings or unlisted historical artifacts read; no external theorem imported; no numerical experiment used. Analytical effort exceeded 95 percent. Shared graph, proof draft, validation matrices and synthesis were not edited.

## 6. Dependencies and exact artifacts used

Only the task's named context and its own brief were read. An initial unbounded graph display was truncated; the three relevant nodes were then read by JSON selection. No neighboring graph claim is used. Exact context hashes at read time:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 9768ff5d6acd94099e74c3825860957ff4cf8ec780675a064bb865fb04aa056f |
| rounds/codex-managed/gc-actual-upper-tail-a/briefs/actual_interface.md | 8eaa7c1e67f5b1c5f6e1340abc5861756e3bfea54c9e1f1d0c96d1fbb90e23d7 |
| strategy/gauss_circle_upper_tail_strategy_2026-10-11.md | a4ac7bd99bd19cadf3ded1f525b20715afd5ff6093437ed8a9907e7fa393d15f |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| strategy/round231_balanced_cancellation/conductor_combined_owner.md | 9f5d9a31c0624e7ee97a21bcdfa2e638154fa313cc45cbab198856222366d76b |
| strategy/round231_balanced_cancellation/conductor_seam_repairs.md | e4dc22c726eb241e24a4e7c485202ea6b6b567ecc4e16a3708d435ddc82eab14 |
| strategy/round231_balanced_cancellation/reports/balanced_reciprocal_attack.md | fa63868418be5c8d24d30284394976fa3e0f1df077117dc3a9227441d55cf61f |

Used dependencies: accepted finite Gram distribution and actual ceiling; reviewed full-band complementary restoration; reviewed one-variable stationary formula with its repaired real phase. The distinct-radical node was inspected only for target scope. The second Poisson identity, quadratic layer cake and actual mean-square control are derived here. The conductor requested that the actual exceptional set be distinguished explicitly from slow tests; that request supplied no missing covariance estimate.

## 7. Recommended state effect

Retain this report as candidate evidence for the conditional exceptional-set quadratic interface and the scoped failure of first-average cancellation. Subject the phase, normalization, threshold/error and complete-restoration seams to independent review. Do not promote target A, complete 32/25, a pointwise improvement, any M1/M2 parent or the quarter target. Recommend no accepted graph or proof-draft change. Freeze this report, return its SHA256 and stop; no successor task is initiated.
