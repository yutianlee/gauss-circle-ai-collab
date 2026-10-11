# Conductor: exact norm-and-factor owner, with provenance correction

Round231 central-balanced packet; conductor; 2026-10-11. Starting graph a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. Candidate synthesis lemma, not a State Patch or a new cancellation gain.

## 1. Result

The smooth high-norm estimate independently recovered in this packet was already reviewed in Rounds203/205, and the general required norm band was already recorded in208. It must not be counted as a new estimate. Combining that inherited bound with the recently reviewed adaptive divisor cutoff does give an exact, fully paid description of the central signed owner.

For every fixed 13/125<=gamma<beta, put m(gamma)=max(1,10gamma,1+20gamma/13). There is an exact real wave C_gamma, supported on

    T^(4gamma)<n<2T^(1-2gamma),
    d,m>=T^(2gamma-13/42)x(n)^(29/84), dm=n,

such that M12(B_T-C_gamma)<<T^(m(gamma)+epsilon). In particular, M12(B_T)<<T^(m(gamma)+epsilon) if and only if M12(C_gamma)<<T^(m(gamma)+epsilon), at epsilon-loss level.

This is an equivalence of upper bounds, not an equality or approximation between moments. It does NOT estimate the remaining owner. The present reciprocal and generic bilinear estimates have not reduced its accepted baseline exponent10beta.

## 2. Exact hypotheses and definition

Use the actual rho,Psi,w,B_T, original ordered patch starts x(n), and finite interface range X0<n<=Z from briefs/balanced_interface.md. Let eta be any one fixed smooth function, zero on(0,1], one on[2,infinity), with values in[0,1]. It need not be monotone. Set

    X_gamma=T^(4gamma), Y_gamma=T^(1-2gamma),
    phi_gamma(n)=eta(n/X_gamma)-eta(n/Y_gamma),
    D_gamma(x)=T^(2gamma-13/42)x^(29/84).

For large T, 2X_gamma<Y_gamma and 2Y_gamma<Z, while X_gamma>=X0. Hence phi_gamma is nonnegative and supported inside the original patch domain. On its support set

    u_gamma(n)=4 sum_(d|n,d<D_gamma(x(n)))[chi4(d)+chi4(n/d)],
    w_gamma(n)=4 sum_(dm=n,d,m>=D_gamma(x(n)))chi4(d).

C_gamma is the real cosine wave with coefficient phi_gamma(n)w_gamma(n), times the original n^(-3/4)Psi(sqrt(n/T)). All vectors are fixed as R varies. Bounded T is absorbed into the fixed constants; no asymptotic patch construction is asserted at unavailable small parameters.

## 3. Derivation and complete restoration

Since beta<1/6 and gamma<=beta, the claimed norm windows are separated. Also 2gamma-13/42<0, and

    D_gamma(x)/sqrt(x)=T^(2gamma-13/42)x^(-13/84)<1.

Thus D_gamma(x(n))^2<n. The two unbalanced hyperbola regions are disjoint, and swapping the two factors in one region proves r2=u_gamma+w_gamma exactly. Strict cutoff equality is assigned to w_gamma.

At x approximately X_gamma the T exponent of D_gamma is

    (142gamma-13)/42>0,

because gamma>=13/125>13/142. Monotonicity therefore makes all retained cutoffs exceed one for large T. Constants from patch comparability do not change any exponent.

Decompose B exactly as

    B=L_gamma+H_gamma+U_gamma+C_gamma,

where L_gamma has coefficient(1-eta(n/X_gamma))r2(n), H_gamma has coefficient eta(n/Y_gamma)r2(n), and U_gamma has coefficient phi_gamma(n)u_gamma(n). H_gamma includes the ENTIRE infinite tail. There is no discarded far-norm contribution or omitted transition strip.

The low component is supported on n<=2X_gamma. Its absolute divisor bound gives sup|L_gamma|<<X_gamma^(1/4+epsilon)=T^(gamma+epsilon). The independently rederived smooth radial estimate gives sup|H_gamma|<<T^epsilon sqrt(T/Y_gamma)=T^(gamma+epsilon), uniformly in all real R. The source version and history of this estimate are recorded in the packet's blind and source reports; its proof uses actual r2 coefficients.

For U_gamma, each fixed divisor sees one interval because D_gamma and the patch starts are increasing. Its smooth multiplier phi_gamma has bounded total variation, uniformly in the scale separation, since it is the difference of two fixed rescalings. The original amplitude and the actual quotient character are treated exactly as in the predecessor factor proof. The resulting shell bound is

    sup|U_gamma,N| << T^epsilon(1+N/T)^(-A)
      [T^(13/84)N^(-29/168)D_gamma(N)^(1/2)+T^(-1)N^(-1/4)]
      << T^(gamma+epsilon).

The first equality of exponents is exact: 13/84+(2gamma-13/42)/2=gamma, and the N powers cancel. The reciprocal term is smaller. The logarithmically many norm shells and every partial endpoint are absorbed by the output epsilon. No new estimate for a mask is imported from the actual B supremum.

Each complementary coefficient vector is fixed and divisor bounded, so the accepted coefficient-uniform distribution theorem applies. The three separately proved ceilings give

    M12(L_gamma), M12(H_gamma), M12(U_gamma)
       << T^epsilon[T+T^(10gamma)+T^(1+20gamma/13)].

The finite L12 norm inequality proves the claimed bound for B-C_gamma and both directions of the upper-bound equivalence. Since gamma<beta, the actual B supremum and the exact identity imply only sup|C_gamma|<<T^(beta+epsilon); its generic distribution reproduces the unchanged10beta moment.

Some exact parameter choices:

| gamma | moment budget | lower norm X_gamma | upper scale Y_gamma | D_gamma(x) |
|---|---|---|---|---|
|13/125|29/25|T^(52/125)|T^(99/125)|T^(-533/5250)x^(29/84)|
|1/8|5/4|T^(1/2)|T^(3/4)|T^(-5/84)x^(29/84)|
|16/125|32/25|T^(64/125)|T^(93/125)|T^(-281/5250)x^(29/84)|

The last budget32/25=1.28 is strictly below10beta. Its small positive improvement is NOT obtained: it requires the same1.28 estimate for C_(16/125), which is open. The middle row supplies a simpler, stronger sufficient target but likewise no bound for its owner.

## 4. First unproved step and tested method price

The missing statement is a signed moment estimate for C_gamma at m(gamma), or any other complete bound below10beta. Recovering the old norm-band localization or merely imposing both norm and factor cutoffs does not prove it.

The actual reciprocal transform creates near products h(4k+/-1) approximately R^2. Exact quarter-frequency resonances survive the chi4 Fourier expansion. Their termwise counting gives the classical sqrt(T/N) ceiling; the sign must be retained across different products to improve it in the middle range.

The primary KRW rectangle certificate contains the aspect-independent term T^(1/8)N^(1/16). Even the optimistic envelope of that term with sqrt(T/N) reaches T^(1/6) at N=T^(2/3), above T^beta. This is a price of those upper-bound expressions, not a lower bound for the actual wave and not a rejection of all bilinear or averaged methods. The exact source application and mask costs are audited separately in the source report.

## 5. Controls

All coefficients, character placements, cutoff equalities, real endpoints and tails are explicit. The low and high norm transitions are exactly owned by eta, and their supports separate for fixed gamma<beta<1/6. All three complementary ceilings are proved independently before applying the generic distribution. The source/band history has been corrected forward before closure. Exact rational arithmetic checks the table and the1/6 crossover; it is diagnostic, not proof of an asymptotic estimate.

## 6. Exact dependencies and provenance

- protocol.md and briefs/balanced_interface.md.
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md, finite coefficient-uniform distribution and infinite-tail treatment.
- strategy/round231_residual_saving/conductor_adaptive_factor_cutoff.md and its nonauthor review, for the fixed-divisor proper-interval estimate and character placements.
- reports/blind_hankel_tail.md, independently frozen before any historical disclosure, SHA25603b30638eb6da7242343731ac03b425e2f09e16749f73685adc343a357cd01d5.
- strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md section5; rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md, explicitly citing the earlier203 Poisson proof; strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md sections1 and4. These establish that the norm-tail and general band were already reviewed evidence.
- reports/balanced_source_audit.md for the primary competitor, subject to its assigned nonauthor review.

The conductor initially investigated the tail as a candidate fresh contribution, then searched the research history and found its existing proof. Both nonisolated analysts were immediately given the precise205/208 context and required to correct attribution; the blind initial report remained isolated and unchanged. No previously frozen artifact was rewritten.

## 7. Recommended state effect

Retain this combined owner ledger as a clarification of the current arithmetic interface, not a new complete theorem or new norm-tail gain. Retain any separately reviewed reciprocal or source controls at their exact scope. Do not launch or promote from this recombination alone. No State Patch, accepted proof-draft change or successor round.
