# Actual balanced divisor waves: reciprocal transform, exact resonance count, and no complete gain

Round231 bounded prelaunch task `balanced_reciprocal_attack`; claimant/deriver; 2026-10-11. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. The authoritative campaign remains closed Round230. This report is candidate evidence, not a State Patch.

## 1. Result

There is a self-contained, character-sensitive estimate for a smooth actual bilinear rectangle. If `DM~N`, `1<=N<=T^(3/2)`, and the smooth amplitude has the scale of `(dm)^(-3/4)`, then, uniformly for every real `R in [T/2,2T]`,

    |sum_(d,m>=1) chi4(d) a(d,m) e(R sqrt(dm))|
       <<_epsilon T^epsilon [(T/N)^(1/2)+T^(-1/2)].       (1)

Here the precise derivative hypotheses are in Section2. The estimate preserves chi4 until after Poisson summation in m. The transformed phase is `R^2 d/(4h)`, its amplitude is `R sqrt(d)/(sqrt(2)h^(3/2))`, and the positive reciprocal frequencies have `h~RD/sqrt(N)`. Exact and near quarter-frequency resonances are counted by factoring integers near `R^2`. No two-dimensional nondegenerate stationary-phase assertion is used.

Summing (1) proves the smooth actual high-norm estimate `(T/Y)^(1/2)` and, by an exact identity with the previously paid U_* owner, also pays the actual sharp adaptive balanced owner above `Y=T^(99/125)` at twelfth-moment exponent29/25. Every adaptive-cutoff correction is accounted for. This leaves the exact balanced owner in `T^(52/125)<n<2T^(99/125)` unestimated at the target power.

**No complete moment improvement is proved.** The smooth high-norm estimate and exponent99/125 were already reviewed in Round205, and appear again in Round208. This report supplies an independent reciprocal-divisor proof and an explicit quarter-frequency control; it must not be counted as new complete progress or a new high-norm localization. The reciprocal method at this level returns to the historical difficult middle band. A uniform square-root estimate for each remaining character sum is false, as shown below.

## 2. Exact statement and hypotheses

Write `e(t)=exp(2 pi i t)`. Use the actual `rho,Psi,w,B_T,beta,X0,Z,x(n),D_T(x),U_*,W_*` in the assigned interface. In particular `X0=T^(52/125)`, `Z=T^(3/2)`, `D_T(x)=T^(-533/5250)x^(29/84)`, and `B_T=H_X0+U_*+W_*+E_Z` exactly. Coefficients are fixed as R varies. The accepted distribution for a fixed divisor-bounded vector is used only after an independent ceiling has been proved for that vector.

For (1), let `D,M>=1/2`, `DM~N`, and let a be a smooth function supported where `cD<d<CD`, `cM<m<CM`, for fixed positive support constants. Require for every fixed derivative order needed below

    |partial_d^j partial_m^k a(d,m)| <= C_(j,k) N^(-3/4)D^(-j)M^(-k). (2)

The constants and support ratios are independent of T,R,D,M. The conclusion applies also with a common additional amplitude factor `L`, multiplying the right side by L. The d,m sums run over positive integers. T bounded by a sufficiently large fixed constant is absorbed into the implicit constant.

The actual examples are smooth dyadic factors in d,m and n=dm, the original `Psi(sqrt(n/T))`, and a fixed smooth cutoff `eta(n/Y)` with eta=0 on `[0,1]`, eta=1 on `[2,infinity)`. On every dyadic norm shell the cutoff satisfies (2), including shells crossing its transition. Schwartz decay supplies `(1+N/T)^(-A)` for any fixed A, after increasing derivative constants. Smooth adaptive factors such as `theta(d/D_T(dm))theta(m/D_T(dm))` also satisfy (2) when theta is fixed and smooth, but no replacement of the actual sharp W_* by those factors is needed in the restoration below.

Define the exact high and low balanced vectors, including their original norm endpoints, by

    W_hi(R)=sum_(X0<n<=Z) w_*(n) eta(n/Y) n^(-3/4)Psi(sqrt(n/T)) cos(2pi R sqrt(n)-3pi/4),
    W_lo=W_*-W_hi,             Y=T^(99/125).             (3)

Then the proved restoration is

    sup |W_hi| << T^(13/125+epsilon),
    M12(W_hi) << T^(29/25+epsilon),
    B_T=H_X0+U_*+W_lo+W_hi+E_Z.                         (4)

The remaining vector W_lo is supported on `X0<n<2Y`, retains the original sharp patch-dependent divisor ownership, and is divisor bounded. This is a paid reduction, not a bound for W_lo.

## 3. Proof or derivation

### 3.1 Exact one-variable Poisson and its stationary term

For fixed positive integer d apply ordinary Poisson summation to the compactly supported smooth m function. With `lambda=R sqrt(N)` and `H=lambda/M~RD/sqrt(N)`, the exact transformed integral is

    I_h(d)=integral a(d,v)e(R sqrt(dv)-hv) dv,
    sum_m a(d,m)e(R sqrt(dm))=sum_(h in Z) I_h(d).        (5)

The phase derivative is `R sqrt(d)/(2sqrt(v))-h`. Thus only positive h comparable to H can be stationary. For such h the stationary point, phase and curvature are exactly

    v_h=R^2 d/(4h^2),
    R sqrt(d v_h)-h v_h=R^2 d/(4h),
    f''(v_h)=-2h^3/(R^2 d).                             (6)

Uniform stationary phase on a fixed compact normalized v/M interval gives

    I_h(d)=b_h(d)e(R^2 d/(4h)-1/8)+O(N^(-3/4)M lambda^(-3/2)),
    b_h(d)=a(d,v_h)R sqrt(d)/(sqrt(2)h^(3/2)).           (7)

This elementary version follows by scaling v=M u, partitioning near and away from the unique critical point, and using the smooth change of variable that makes the phase quadratic near that point. The quadratic Gaussian integral gives the displayed leading term; the next even Taylor term and its integral remainder are `O(lambda^(-3/2))`. Away from the critical point, repeated integration by parts gives arbitrary inverse powers. All normalized derivatives are bounded by (2), the normalized second derivative stays bounded away from zero, and support is smooth. A stationary point crossing the support boundary is covered by extending the amplitude by zero smoothly; there is no omitted endpoint term. The assertion is uniform over an enlarged fixed h/H interval. For h outside it, integration by parts yields `O_A(N^(-3/4)M(lambda+|h|M)^(-A))`, after choosing the enlargement to separate the derivative from zero.

There are O(D) values of d and O(H) relevant h. Consequently the entire stationary error is

    O(N^(-3/4)D H M lambda^(-3/2))
     =O(D R^(-1/2)N^(-1))=O(R^(-1/2)).                (8)

We used `D<=C N`, because M is bounded below. The total nonstationary h tail is smaller by taking A large. This is a sum of absolute errors; no cancellation is assumed there. In particular even a rectangle with one factor of order one is covered. The condition `N<=T^(3/2)` ensures `H>>T^(1/4)`, so no small-dual-length exception is hidden.

For each fixed h the d symbol satisfies

    ||b_h||_infinity+integral |b'_h(d)| dd
       << A0,        A0=N^(-3/4)R sqrt(D)H^(-3/2).     (9)

Indeed `v_h` is proportional to d, and the derivative bounds in (2) give exactly one factor D^(-1). Neither the curvature factor nor evaluation at the stationary point adds a rapidly varying d phase.

### 3.2 The actual character and its reciprocal resonances

The exact identity

    chi4(d)=(e(d/4)-e(-d/4))/(2i)

and geometric summation, followed by summation by parts using (9), give

    |sum_d chi4(d)b_h(d)e(alpha_h d)|
       << A0 sum_(sigma=+1,-1) min(D,||alpha_h+sigma/4||^(-1)),
    alpha_h=R^2/(4h).                                  (10)

At distance zero the minimum means D. Replacing chi4 by arbitrary signs would invalidate (10).

For `0<delta<=1/2`, the number of h in any fixed positive interval `[cH,CH]` satisfying one of the two resonance conditions is

    #{h: ||R^2/(4h)+sigma/4||<=delta}
       <<_epsilon (H delta+1)T^epsilon.                (11)

Here is a direct proof, including arbitrary real R. The condition supplies an integer k with

    |R^2-h(4k-sigma)|<=4CH delta.                      (12)

Because `H<<R sqrt(N)<<R^2` in the stated range for large T, the odd integer `q=4k-sigma` is positive. Thus `v=hq` is a positive integer in an interval of length O(H delta) around R^2. There are O(H delta+1) possible integers v, each has O(T^epsilon) possible positive divisors h by the elementary divisor bound, and the parity condition only reduces the count. All v are comparable to R^2. This proves (11), with no equidistribution assumption and no deletion of exact resonances. At delta=0 there are no solutions unless R^2 is an integer; when it is, they are the divisors h of R^2 for which R^2/h has the required odd congruence.

Split distances into dyadic intervals starting at D^(-1), counting the closest interval by (11). This gives

    sum_(h~H) min(D,||alpha_h+sigma/4||^(-1))
       <<_epsilon T^epsilon (H log(2D)+D).             (13)

If D is bounded, the same bound follows immediately. Multiplication by A0 is particularly simple:

    A0 H ~ R^(1/2)N^(-1/2),
    A0 D ~ R^(-1/2).                                  (14)

Equations (8)--(14) prove (1). All formulas use one-dimensional stationary phase. The original two-dimensional phase is homogeneous of degree one and has a rank-one Hessian; no nonexistent determinant is divided by.

### 3.3 Assembling the actual smooth high norm owner

Insert smooth dyadic partitions in d and m in

    B_hi^C(R)=4 sum_(d,m>=1) chi4(d)(dm)^(-3/4)Psi(sqrt(dm/T))eta(dm/Y)e(R sqrt(dm)).

The partitions can be chosen to sum to one on all positive integer arguments, including d=1 and m=1. Only O(log T) factor rectangles occur per retained norm shell. Their derivative bounds are (2). All n below Y are absent. Summing (1) over the dyadic norm shells from a constant multiple of Y through Z yields

    sup |B_hi^C| <<_epsilon T^epsilon [(T/Y)^(1/2)+T^(-1/2)]. (15)

For shells above Z, use the actual absolute divisor bound and Schwartz decay directly. On n~N their absolute contribution is `O_A(N^(1/4+epsilon)(1+N/T)^(-A))`; summed over N>Z this is an arbitrary negative power of T after taking A large. This is the full infinite tail, not a deleted truncation. The real wave is `Re(e(-3/8)B_hi^C)`, so (15) controls it. At Y=T^(99/125), its ceiling is T^(13/125+epsilon).

The sum over h was bounded in absolute value only AFTER exact cancellation in the d character sum. The output is therefore genuinely sensitive to the actual character. It nevertheless does not exploit cancellation between the remaining reciprocal frequencies.

### 3.4 Sharp patch boundaries and all owners

Let U_hi be exactly U_* with the same multiplier eta(n/Y), and E_hi the actual eta-multiplied tail n>Z. Since Y>X0, the head vanishes under eta. The exact original divisor identity gives, without any smoothing of its arithmetic boundary,

    W_hi=B_hi-U_hi-E_hi.                              (16)

The previous U_* proof survives this multiplier: for each fixed small divisor the original sharp condition still gives one proper interval; eta times the original smooth norm amplitude has bounded variation at the same scale. The two character placements are treated by the same period-four residue split as in the assigned prior report. Thus independently

    sup |U_hi| << T^(13/125+epsilon).                   (17)

The tail E_hi is negligible. Equations (15)--(17) prove the independent ceiling in (4). The exact W_hi coefficient is fixed as R varies and divisor bounded, so the accepted distribution plus layer cake gives

    M12(W_hi)<<T^epsilon[T+T^(10*13/125)+T^(1+(20/13)*(13/125))]
              <<T^(29/25+epsilon).                    (18)

No actual full-wave ceiling was transferred to an arbitrary mask. No derivative or stationary-phase claim was made for the sharp patch-dependent mask. Its entire difference from the smooth full tail is the separately paid actual U_hi and E_hi in (16).

The exact restoration (4) pays all mixed terms by the finite L12 norm inequality. Consequently a bound `M12(W_lo)<<T^(b+epsilon)` would restore the full moment at `max(29/25,b)`. This implication does not prove a smaller b. The full accepted exponent remains10beta. The same reasoning bounds W_lo by T^beta using the accepted full ceiling and the already paid owners; applying the generic distribution then returns the unchanged10beta moment.

## 4. First doubtful or unproved step

The first missing numerical estimate is a genuinely stronger signed reciprocal-frequency or radius-averaged estimate on the remaining actual balanced middle owner. Its exact target is

    integral w(R/T)|W_lo(R)|^12 dR << T^(b+epsilon), b<10beta, (19)

with preferred `b<=29/25`, all real R and the sharp original factor ownership in (3). A smooth-block pointwise route would have to improve the reciprocal main term beyond the A0 times `(H log(2D)+D)` bound in (13), and separately transfer that result through every cutoff correction. The trivial coefficient bound and (1) on the full smooth norm block give only

    |B_N| << T^epsilon min(N^(1/4),(T/N)^(1/2)).         (20)

Their intersection is at N=T^(2/3), with ceiling T^(1/6), worse than the accepted beta. Thus the completed character/resonance calculation cannot itself deliver the requested complete gain. It is not legitimate to replace every remaining d sum in (10) by D^(1/2), to drop the exact resonances, to put modulus inside the original divisor sum, or to claim the rank-one phase is nondegenerate in two dimensions.

Equation (13) is an upper certificate, not a lower bound for the signed physical sum. The exact coherent-frequency control below does not rule out (19), since different h, blocks, and owners may cancel. No asymptotic lower bound for the full moment is claimed. The conclusion is a scoped no-gain result for the completed transform-plus-absolute-frequency certificate.

## 5. Required controls and outcomes

* **Stationary normalization: pass analytically.** Direct differentiation gives (6), hence the factor `1/sqrt(2)` and the phase shift `e(-1/8)`. The normalized amplitude is N^(-3/4); the summed remainder is R^(-1/2), not one uncounted error per divisor.
* **Exact quarter-frequency obstruction: pass analytically.** Take a positive odd integer L congruent1 modulo4, radius R=L and reciprocal frequency h=L. Then alpha_h=L/4 is congruent1/4 modulo1 and `v_h=d/4`. Choose smooth nonnegative rectangle weights with M comparable to D/4 and with `a(d,d/4)` bounded below on a fixed interior d interval. For odd d, `chi4(d)e(d/4)=i`; for even d it is zero. Therefore this one transformed d sum has magnitude comparable to A0 D. A uniform A0 D^(1/2+epsilon) estimate is false. These radii are within the requested real-radius range (take T=L), and D,M may both have order sqrt(N), well above the adaptive cutoff on retained central shells. This is a single reciprocal-frequency control only; it does not lower-bound the sum over h or M12.
* **Near and exact resonance count: pass analytically.** Equation (12) counts integer products, not approximate divisors of an assumed integer R^2. Real R is unrestricted. The +1 in (11) pays exact and exceptionally close frequencies. Congruence restrictions are retained, not replaced by a fictitious saving.
* **Sharp arithmetic boundary and endpoints: pass.** Identity (16) retains the exact equality convention in w_*, the nonuniform patch starts, and endpoints X0,Z. U_hi is separately proved by the inherited whole-fibre argument with bounded variation. No claim that an arbitrary mask inherits the actual circle ceiling is used.
* **All norm tails and mixed terms: pass.** The singleton factors appear in the factor partitions; eta removes only its specified low norms. The infinite actual tail is paid by Schwartz decay. The head, unbalanced owner, high balanced owner, and remaining low balanced owner have exact ownership, and (4) pays all cross terms by L12.
* **Historical and state control: pass.** The conductor's provenance intervention was checked against Round205 Section5 and Round208 Section1. The high cutoff99/125 and `(T/N)^(1/2)` block estimate are historical reviewed evidence, not new progress. This report's orthogonal derivation and explicit congruence control do not change the accepted exponent.
* **Resource control: pass.** This work is analytical/algebraic. No numerical experiment, external theorem import, or web search was used. The arithmetic equalities in (6), (8), (14), and (18) are the required reproducible symbolic controls, with their derivations displayed.

## 6. Dependencies and exact artifacts used

Read only the original named context and the two strategy checkpoints subsequently authorized by the conductor. An initial graph text search incidentally displayed neighboring matching nodes; those lines supply no mathematical dependency. No sibling report was read. The active campaign was used for status only. The two accepted nodes used are `GC-complete-square-root-large-values-moment-bound` and `GC-complete-distinct-radical-twelfth-reduction`; the latter is a scope/target check, not a bound for W_lo.

Hashes at the time of this report:

* `protocol.md`: `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
* `state/active_campaign.yml`: `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa`.
* `state/proof_obligations.yml`: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
* `strategy/round231_balanced_cancellation/briefs/balanced_reciprocal_attack.md`: `cfe1f3151c08660e8c69a87e2ba981e974663a3676413340103966f4fe920e58`.
* `strategy/round231_balanced_cancellation/briefs/balanced_interface.md`: `cb6f283b2de16774ff946c450acabd61001b39c39ba58c6e2ab719c14050e055`.
* `strategy/round231_residual_saving/conductor_adaptive_factor_cutoff.md`: `02727c91e64931a13d3707ca15df021418d3e96510e35894e0d96a70182506fa`.
* `strategy/round231_residual_saving/reports/actual_residual_attack.md`: `0d18fa59d915809427e1758ee478ba439303748738e8ec1f86d7e95060dd0bc5`.
* `strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md`, Section5: `03e05b85fcb0fc72fe0e65869f13e33763fea3dc503e9a85d6d1e883eebdcfc4`.
* `strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md`, Section1 (and the immediately following displayed deficit discussion returned in the same bounded read): `ae22a1a096a380b28b4b409a478dd7f87e5b1d8727068a4231ceb31272e03cbf`.

An attempted Round208 filename with date2026-09-26 did not exist; a filename-only search located the above September27 file. No other historical context was opened. The conductor supplied the exact U_hi boundary-payment identity and alerted this task to the historical high-tail precedent. The reciprocal derivation, divisor-product count, and coherent-frequency control above were independently derived here. Ordinary Poisson summation and one-dimensional smooth stationary phase were used with explicit phase, support, and error verification; no external source theorem with unverified hypotheses was imported.

## 7. Recommended state effect

Retain the reciprocal rectangle calculation and exact quarter-frequency example as candidate diagnostic evidence, subject to any assigned nonauthor review. Reject the proposed uniform square-root estimate for every reciprocal character fibre. Record no complete gain and no new tail-localization progress: the actual hard middle-band moment (19) remains open, and the smooth transform recovers a known certificate. Recommend no change to the authoritative graph, accepted exponents, proof draft, validation matrices, or M1/M2 parents. Stop after this assigned report and its SHA256; no successor is designed.
