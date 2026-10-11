# Actual physical residual: paid factor strips and surviving coefficient energy

Round231 prelaunch task `actual_residual_attack`; claimant/deriver; 2026-10-11.
Starting graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
The authoritative campaign remains closed Round230. This is bounded admission evidence, not a State Patch.

## 1. Result

The actual divisor structure gives a stronger, completely paid physical decomposition than retaining every pair with both factors at least `x_j^(1/20)`. For the fixed patch starts in the interface, let the unbalanced owner contain every divisor pair with at least one factor below `x_j^alpha`, and let `W_alpha` contain the remaining balanced pairs. The unbalanced owner has the proved complete supremum

    sup |U_alpha| << T^(gamma_alpha+epsilon),
    gamma_alpha = 13/84 + (52/125)(-29/168+alpha/2),

for each fixed `0<alpha<29/84`. Its twelfth moment is bounded by

    M12(U_alpha) << T^(b_alpha+epsilon),
    b_alpha = max(1, 10 gamma_alpha, 1+20 gamma_alpha/13).

Two useful choices are:

* `alpha=17/168`: `gamma_alpha=13/125` and `b_alpha=29/25`. Thus all pairs with a factor smaller than approximately `n^0.10119` are paid at the preferred complete target budget.
* `alpha=11/50`: `gamma_alpha=33787/262500` and `b_alpha=33787/26250=1.2871238095... <10 beta=1.2896635194...`. Thus all pairs outside the central range approximately `n^0.22 <=d,m<=n^0.78` are paid at a strictly improved budget relative to the accepted complete exponent.

This is an actual signed physical-phase component estimate, with the quotient character, patch boundaries, real endpoints, and tails paid. It uses no unnamed source constant. The correction from the original approximant to this larger unbalanced owner is paid in full.

The remaining central balanced wave has not been estimated sufficiently. Its coefficients do not acquire a power saving merely by restricting to this balanced range: on a fixed annulus `n~cT`, actual same-character semiprimes prove coefficient energy at least `T^(-1/2)/log^2 T`, for both the original residual and `W_alpha` for every fixed `alpha<1/2`. Consequently the coefficient-energy-only improvement of the diagonal/Gram certificate fails. This does not lower-bound the desired complete twelfth moment or reject signed cancellation.

The strongest complete restored upper bound proved or inherited here is still `M12(B_T)<<T^(10 beta+epsilon)`. The new result is a narrower actual owner and a scoped certificate obstruction, not a complete gain.

## 2. Exact statement and hypotheses

Use exactly `rho,Psi,w,B_T,X0=T^(52/125),Z=T^(3/2)`, and the radius-independent ordered patch starts `x(n)=x_j` from `briefs/residual_interface.md`. The half-open ownership of each integer is unchanged. Take `T>=T0` large enough that every retained start exceeds one; the same bounded-parameter convention as the prior main report handles `2<=T<T0` by increasing constants.

For `X0<n<=Z` define

    u_alpha(n)=4 sum_(d|n, d<x(n)^alpha) [chi4(d)+chi4(n/d)],
    w_alpha(n)=4 sum_(dm=n, d>=x(n)^alpha, m>=x(n)^alpha) chi4(d).

Since `alpha<1/2`, `x(n)^(2alpha)<n`. The two excluded regions are disjoint, including their strict boundaries, so exactly

    r2(n)=u_alpha(n)+w_alpha(n).                         (1)

Let `U_alpha,W_alpha` be the real cosine waves with these coefficients, multiplied by `n^(-3/4)Psi(sqrt(n/T))`. Their complex analogues use `e(R sqrt(n))`, with `e(t)=exp(2 pi i t)`. The new supremum for `U_alpha` applies also to its complex analogue; the inherited actual `T^beta` supremum is used only for real waves after exact restoration.

The coefficients are fixed as `R` varies and are divisor bounded. All constants may depend on fixed `alpha`, the original partition comparability constants, the fixed functions, and epsilon.

For the coefficient-energy assertion there are fixed `0<c1<c2`, depending only on the fixed mollifier, such that for all large real `T`,

    sum_(c1 T<=n<=c2 T) |v(n)n^(-3/4)Psi(sqrt(n/T))|^2
       >> T^(-1/2)/log^2 T,                              (2)

where `v=r2-rsharp` is the literal original residual coefficient. The same holds with `v` replaced by `w_alpha` for every fixed `alpha<1/2`. The annulus lies wholly inside `(X0,Z]`; no coefficient outside its assigned domain is used.

## 3. Proof and complete restoration

### 3.1 Whole-fibre payment of the enlarged unbalanced owner

Work on one ambient shell `n~N`. For each fixed divisor `d`, the condition `d<x(n)^alpha` is monotone in the ordered patch starts. Its intersection with the shell and the global lower and upper cutoffs is one interval. After `n=dm`, the allowed `m` therefore form one proper interval in an ambient interval of length comparable to `N/d`. There is no loss equal to the number of patches.

The fixed smooth amplitude has size plus total variation

    <<_A N^(-3/4)(1+N/T)^(-A).

Restriction to a divisor's support adds at most two jumps of this size. This remains true for an empty interval, a singleton, and shortened first and last pieces.

Put `k=13/84,l=55/84`. The already accepted proper-interval exponent-pair specialization to `R sqrt(dm)`, as rechecked for the prior main, gives

    |sum_m e(R sqrt(dm))|
       << T^epsilon [T^(13/84)N^(97/168)d^(-1/2)
                      +N^(1/2)/(Td)].                   (3)

Here the phase-size parameter is comparable to `T sqrt(N)` and the ambient length is `N/d`. The ratio is at most `sqrt(N)/(dT)<=T^(-1/4)/d` because `N<=T^(3/2)`. All derivatives are those of the fixed square-root monomial. For the quotient-character term, split `m` into its two nonzero residue classes modulo four. The shifted square-root phase has exactly the same admissible monomial derivative pattern, and (3) follows with a fixed additional factor. No arbitrary-weight exponent-pair estimate is used.

Summation by parts and `d<<(2N)^alpha` give

    sup_R |U_(alpha,N)(R)|
      <<_(A,epsilon) T^epsilon(1+N/T)^(-A)
          [T^(13/84)N^(-29/168+alpha/2)+T^(-1)N^(-1/4)]. (4)

The first exponent in `N` is negative when `alpha<29/84`. Summing shells from `X0` to `Z` proves the stated `gamma_alpha` bound; the reciprocal term is smaller. Schwartz decay pays the full actual tail beyond `Z` separately. This proof exchanges the divisor and norm sums before estimation, and retains the actual periodic character in each fibre.

The accepted finite coefficient-uniform distribution theorem applies to the assembled `u_alpha` vector, since it is fixed and divisor bounded. Thus

    D_(U_alpha)(V)<<T^epsilon(V^(-2)+T V^(-136/13)), V>=1.

Layer cake up to the independently proved `T^gamma_alpha` ceiling gives

    M12(U_alpha)<<T^epsilon
      [T+T^(10 gamma_alpha)+T^(1+20 gamma_alpha/13)].      (5)

The epsilon inputs are chosen as sufficiently small fixed multiples of the desired output epsilon. Formula (5) is not obtained by granting an arbitrary mask the actual circle supremum.

For `alpha=17/168`, the slope is `-29/168+17/336=-41/336`; substitution gives `gamma=13/125`. The controlling term in (5) is `1+20 gamma/13=29/25`.

For `alpha=11/50`, the slope is `-263/4200`, so

    gamma=13/84-(52/125)(263/4200)=33787/262500.

This exceeds `13/110`, so `10 gamma` dominates `1+20 gamma/13`. Also

    beta-gamma=0.00025397099...>0.

The strict inequality can be checked directly using the exact beta from the interface, without relying on the printed decimals.

### 3.2 The original residual and every correction

Write `A_0=u_(1/20)` and let `M_mid` be the logarithmic middle-divisor term of the original approximant, including its factor four. Then exactly

    rsharp=A_0+M_mid,
    V=W_(1/20)-M_mid.                                  (6)

The previous whole-fibre proof bounds `M_mid` separately by the same main exponent `5447/52500`; its complete moment is at most `T^(3044/2625+epsilon)`. This is a separate payment, not an inference that a component inherits its sum's cancellation.

For general alpha define `Q_alpha=U_alpha-Ssharp` as an exact signed wave. Equations (1) and the original definition give

    V=W_alpha+Q_alpha.                                 (7)

The norm inequality and the separately proved moments give

    M12(Q_alpha)<<T^(max(b_alpha,3044/2625)+epsilon).     (8)

Thus increasing the divisor cutoff does not discard the middle term or add an unpaid arithmetic correction. It also does not introduce rational-polynomial means needing a separate source theorem.

With the original norm head and actual far tail,

    B_T=H_X0+U_alpha+W_alpha+E_Z.                       (9)

The head costs `T^(29/25+epsilon)` as in the interface. The far tail has supremum `O_A(T^(-A))`, hence twelfth moment `O_A(T^(1-12A))`. The head supremum is `O(T^(13/125+epsilon))`. For either displayed alpha, (9) and the inherited actual full-wave supremum therefore imply `sup|W_alpha|<<T^(beta+epsilon)`. Applying its coefficient-uniform distribution then recovers only `M12(W_alpha)<<T^(10 beta+epsilon)`.

Every mixed term in (7)--(9) is paid by the finite `L12` norm inequality. No signed cancellation between owners is assumed. The complete restored bound remains `T^(10 beta+epsilon)`; the sharp-discrepancy restoration remains the inherited `Y^(1+10 theta_LY+epsilon)`, with no new pointwise exponent.

The larger choice `alpha=11/50` pays the enlarged unbalanced owner below the old complete exponent but not at `29/25` by this proof. One cannot use its `1.287123...` main estimate to claim the preferred `1.16` target. The choice `17/168` preserves that preferred budget.

### 3.3 What direct fibre bounds do on the central balanced region

Apply exact hyperbola ownership to `W_alpha`: either `d<=m`, or `m<d`. In each branch the smaller factor is at most `sqrt(2N)`, with the diagonal assigned only to the first branch. For each fixed smaller factor, its support combines `n>=d^2` (or the corresponding strict inequality) with the monotone patch-cutoff condition, so it is still an interval. The inner character is either constant or periodic modulo four. Applying (3) and summing the smaller factor gives

    sup |W_(alpha,N)|
      << T^epsilon(1+N/T)^(-A)
            [T^(13/84)N^(13/168)+T^(-1)N^(-1/4)].       (10)

The lower factor cutoff removes only the lower end of `sum d^(-1/2)`; for fixed `alpha<1/2` its upper-end bound still has size `N^(1/4)`. After shells are recombined, the displayed certificate is `T^(13/56+epsilon)`, worse than the inherited `T^beta` ceiling. This compares proved upper-bound expressions; it is not a lower bound on `W_alpha`.

A Cauchy step across the outer factor replaces the periodic sign by its square and creates cross-fibre correlations. Their signs must be used before absolute values to improve (10). Retaining those correlations is legitimate, but no estimate for them sufficient for the full moment is proved here.

### 3.4 Actual semiprime energy; elementary counting only

Here is a self-contained weak Chebyshev input adequate for the control. For all sufficiently large `y`,

    (1/4)y/log y <= pi(y) <= 8y/log y.                 (11)

For the lower bound, let `n=floor(y/2)`. The central binomial coefficient is at least `4^n/(2n+1)`. For each prime `p<=2n`, its valuation in this coefficient is at most `floor(log(2n)/log p)`: in the factorial valuation formula each difference of floors is zero or one. Therefore the binomial coefficient is at most `(2n)^pi(2n)`. Taking logarithms proves the lower bound in (11) for large `y`.

For the upper bound, primes in `(n,2n]` divide that binomial coefficient, so `theta(2n)-theta(n)<=2n log 2`. Summation on dyadic integer arguments, followed by monotonicity, gives `theta(y)<=4(log 2)y`. Split primes at `sqrt(y)` to obtain `pi(y)<=sqrt(y)+2 theta(y)/log y`, which is at most the upper bound in (11) for large `y`.

Take the fixed `a=1/256`. Since `log(aY)>=log Y/2` for large `Y`, (11) implies

    pi(Y)-pi(aY) >= (3/16)Y/log Y.

All these primes are odd. At least half have the same `chi4` sign, say `s in {1,-1}`. Their unordered distinct pairs give at least `cY^2/log^2 Y` distinct products `n=pq` in `[a^2Y^2,Y^2]`, by unique factorization.

Choose a fixed `c>0` small enough that `Psi(t)>=1/2` for `0<=t<=sqrt(c)`, which is possible since `Psi(0)=1` and Psi is continuous. Set `Y=sqrt(cT)`. Every selected product lies in a fixed annulus inside `(X0,Z]` for all large `T`. Both primes exceed every source middle-divisor cutoff `x(n)^(1/10)` and every enlarged cutoff `x(n)^alpha` for fixed `alpha<1/2`. The only divisor below these cutoffs is one. Consequently

    r2(pq)=4(1+s)^2,
    rsharp(pq)=u_alpha(pq)=4(1+chi4(pq))=8,
    v(pq)=w_alpha(pq)=8s.                              (12)

The middle-divisor band is empty on these atoms. There are `>>T/log^2 T` such distinct atoms, and each squared wave coefficient is at least a fixed positive constant times `T^(-3/2)`. This proves (2) for the literal residual and enlarged balanced coefficient.

This lower bound is for coefficients, not a signed radius integral. It shows that even after all the proved factor-strip payments, the normalized coefficient energy in a top-scale annulus cannot be bounded by `T^(-delta)` for any fixed `delta>0` relative to the usual `N^(-1/2)` scale. A finite dyadic subdivision gives the same conclusion on at least one top-scale shell. Therefore no power gain in the generic diagonal constant is available solely from that coefficient norm. The actual physical phases can still cancel; (12) does not preclude such cancellation.

## 4. First doubtful or unproved step

The first unproved improvement is a signed cross-fibre or radius-moment estimate for the central balanced owner, beyond (10) and the generic distribution argument. More concretely, on `N~T` and balanced `D M~N` with `D,M>=N^alpha`, the fibre estimate permits the unnormalized size `T^(55/56+epsilon)`. To obtain a pointwise route to a strict complete gain, one sufficient new input would control the coherently assembled central blocks by `T^(3/4+beta-eta+epsilon)` for some fixed `eta>0`, while retaining the full hyperbola endpoints and both character placements. No such estimate has been established here. A direct signed physical moment bound can bypass this stronger pointwise requirement.

At `alpha=11/50`, any proved `M12(W_alpha)<<T^(10 beta-eta+epsilon)` would yield the complete exponent `max(29/25,33787/26250,10 beta-eta)<10 beta`. This restoration statement is not offered as a new estimate: the proven content is the full factor-strip payment (4)--(8), and the actual coefficient control (12).

No error has been identified in these asserted lemmas, subject to nonauthor review. The clear limitation is that neither the direct fibre bound nor coefficient-energy Cauchy controls the remaining signed cross terms. The report rejects only the proposed power saving from balanced support plus coefficient energy, not the residual problem, physical major-arc analysis, or signed balanced correlations.

## 5. Required controls and outcomes

* **Exact hyperbola and equality ownership: pass.** Since the cutoff squared is strictly below `n`, the two unbalanced regions never overlap. Cutoff equalities stay in the balanced region. The later `d=m` hyperbola diagonal is assigned once.
* **Patch and endpoint control: pass.** Every fixed divisor sees one interval because starts are nondecreasing; no patch-count cost occurs. Arbitrarily short endpoint pieces are estimated with the accepted proper-interval theorem.
* **Actual signs: pass.** The two placements `chi4(d)` and `chi4(m)` are retained. Only the actual period-four structure permits the quotient-character fibre estimate. Replacing these signs by arbitrary variable weights would invalidate that step.
* **Correction and complete restoration: pass.** Equations (7)--(9) own the original middle term, the changed arithmetic approximant, head, and infinite tail explicitly. The larger cutoff has a larger paid moment budget, stated rather than hidden.
* **Actual coefficient-energy control: pass.** The semiprime products use no primes-in-progressions theorem; an elementary total-prime estimate and pigeonhole suffice. Both possible character signs produce nonzero residual magnitude eight. No finite sample is used as proof.
* **Certificate versus theorem: pass.** The lower bound (2) obstructs only a power saving in coefficient energy and its diagonal certificate. It is not an obstruction to the complete signed target. Likewise the exponent in (10) describes the available upper certificate, not actual large values.
* **Resource control: pass.** Work was analytical/algebraic. No numerical experiment or literature search was performed; exact symbolic fractions and elementary inequalities are displayed for independent checking.

## 6. Dependencies and exact artifacts used

Read the assigned brief and only its listed mathematical contexts:

* `protocol.md`, hash `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
* `state/active_campaign.yml`, hash `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa`.
* `state/proof_obligations.yml`, starting graph hash above; selected nodes `GC-complete-square-root-large-values-moment-bound` and `GC-complete-distinct-radical-twelfth-reduction`, both `proved_internal`. An initial broad text search incidentally displayed adjacent matching graph lines; they supply no dependency here.
* `strategy/round231_residual_saving/briefs/actual_residual_attack.md`, hash `6dfcab8ce727d0131f94a59878b2c8fb578c65f37981b6ee13a1cb4985c6196d`.
* `strategy/round231_residual_saving/briefs/residual_interface.md`, hash `bd57b6e13b85ee0d15905ff74a66ca4326cfe00c0020a11b4b4a7608eb994bad`.
* `strategy/round231_quadratic_signed_admission/conductor_type_i_main.md`, hash `7b05d13908b116acf2a40320040b4a7614a4f80ec2fcfcde073eb5055957924f`.
* `strategy/round231_quadratic_signed_admission/reports/quadratic_remainder_attack.md`, hash `abff6860790aba4cda537ad9e81af504c1f175844a2c252479e685077dd1eb24`.
* `strategy/round231_quadratic_signed_admission/reviews/type_i_main_and_resonance_review.md`, hash `a47dc8dbfda42b2003282ed0f4d00e9c3815b064df154d445f741adf6c661189`.
* `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, hash `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.

An attempted read of `strategy/round231_residual_saving/residual_interface.md` found no file; the actual listed context is under `briefs/`. Directory/path searches were used only to resolve assigned filenames. No sibling report was read.

The exponent-pair source is inherited through the accepted kernel and the assigned prior source review: Bourgain, arXiv:1408.5794v2, Section 5, Theorem 6 and proper-interval discussion. No new source theorem is imported. The Matomaki--Shao--Tao--Teravainen arXiv:2204.03754v4 formula enters only through the literal approximant supplied in the interface; its unnamed polynomial-uniformity constant is not used. The radical node is a scope check, not an estimate for this new norm-factor partition.

The conductor suggested using elementary total-prime counts and a character-sign pigeonhole for the semiprime control; the explicit constants and self-contained elementary proof are supplied above. All new derivations and the sole output file belong to this task. The final SHA256 is communicated after freezing rather than embedded in the file it hashes.

## 7. Recommended state effect

Retain the proved factor-strip estimates and exact fully paid correction as candidate evidence, subject to the assigned independent review. Retain the actual semiprime energy lower bound as a scoped obstruction to the coefficient-energy-only diagonal improvement. Do not promote a complete moment gain, a new pointwise exponent, a distinct-radical target estimate, or any M1/M2 parent. Recommend no change to the authoritative graph or proof draft. Stop after this assigned report and hash; no successor is designed.
