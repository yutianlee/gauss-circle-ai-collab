# 1. Result

Round231 central-balanced packet; task `review_hankel_and_owner`; nonauthor analytic/source-seam review, 2026-10-11. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. This is the single assigned review cycle, not a new research round.

**PASS** for the isolated smooth actual tail theorem and the conductor's combined norm-and-factor owner at the frozen hashes listed in Section 6. No mathematical repair is required. The full second Bessel term, summable error, scale-separated sine estimate, zero mode, all dual frequencies, arbitrary real radii, and the three independently paid complementary owners are accounted for.

The proper conclusion is a rigorously paid recombination of the inherited norm band and the recent adaptive factor cutoff. The tail and general norm-band principle were already present in reviewed historical evidence. The middle balanced physical moment remains unproved, and this packet gives no complete moment or pointwise gain.

# 2. Exact statement and hypotheses checked

For the fixed real radial nonnegative unit-mass smooth mollifier rho, its real even Fourier transform Psi, fixed eta in [0,1] with eta=0 on (0,1] and eta=1 on [2,infinity), real T>=2, T/2<=R<=2T and 1<=Y<=T, the blind report proves

    |sum_(n>=1) r2(n)n^(-3/4)Psi(sqrt(n/T))eta(n/Y)
         cos(2pi R sqrt(n)-3pi/4)| << T^epsilon sqrt(T/Y).

The proof does not require eta to be monotone or Psi to be nonnegative. Its constants are uniform in fractional parts and the distance of R^2 from an integer.

For every fixed 13/125<=gamma<beta, the conductor defines

    X=T^(4gamma), Y=T^(1-2gamma),
    phi(n)=eta(n/X)-eta(n/Y),
    D(x)=T^(2gamma-13/42)x^(29/84),

and retains the actual balanced divisor coefficient w_gamma(n) on the support of phi. The reviewed assertion is

    M12(B_T-C_gamma) << T^(m(gamma)+epsilon),
    m(gamma)=max(1,10gamma,1+20gamma/13),

with C_gamma the exact real wave having coefficient phi(n)w_gamma(n). Consequently the target upper bounds for B_T and C_gamma at m(gamma) are equivalent. This is not a comparison of their moments by a small additive error.

The original patch starts x(n), actual quotient-character treatment, and fixed-divisor interval estimate are inherited exactly from the assigned predecessor context. No unproved arbitrary-mask supremum is assumed.

# 3. Proof audit and independent checks

**Hankel amplitudes and scale separation — PASS.** Put A=sqrt(Y), B=sqrt(T), w(u)=Psi(u/B)eta(u^2/A^2). The estimates |w^(j)(u)|<=C_j u^(-j), uniformly in B/A, follow term by term from Schwartz derivative bounds and the fixed transition support of eta. Thus for a_p=u^(-p)w,

    ||a_p^(k)||_1 << A^(1-p-k) when p+k>1.

The p=1, k=0 integral could contain log(B/A), but the report never bounds it uniformly. Instead its sine transform is bounded at low frequency by splitting at U=max(A,1/|s|). Below U the sine gives O(|s|U); above U one integration by parts gives O((|s|U)^(-1)). At s=0 the integral is exactly zero. High-frequency integration by parts then proves |S(s)|<<_K(1+A|s|)^(-K). The cosine transform is used only at R+v>0, where derivative bounds suffice. This resolves the potentially dangerous scale dependence.

**Poisson normalization and zero frequency — PASS.** The radial test f(x)=|x|^(-3/2)w(|x|)cos(2pi R|x|-3pi/4) is identically zero near the origin and Schwartz for each fixed parameter triple. Its spatial lattice sum is exactly the actual r2 sum. Angular integration gives the factor2pi in the radial Fourier integral. At dual frequency0, two integrations by parts of u^(-1/2)w(u) yield R^(-2)A^(-3/2); no missing constant, spatial origin, or zero mode remains.

**Second Bessel term and phase algebra — PASS.** The DLMF coefficients are a1(0)=-1/8, a2(0)=9/128, a3(0)=-75/1024. For z=2pi vu the first two terms are

    cos(2pi vu-pi/4)/(pi sqrt(vu))
      + sin(2pi vu-pi/4)/(16pi^2(vu)^(3/2)).

Multiplying by the radial angular factor2pi and the exact product-to-sum factor1/2 gives respectively the coefficients v^(-1/2) and v^(-3/2)/(16pi) in the blind report's equation(16). Directly expanding the phases gives the leading pair

    sin(2pi(R-v)u)-cos(2pi(R+v)u),

and the correction pair

    cos(2pi(R-v)u)-sin(2pi(R+v)u).

In particular, exact resonance kills the leading difference term but not the correction. The argument preserves this distinction.

**Globally summable Bessel remainder — PASS.** The real-positive DLMF error bound, with one term retained in each even/odd series, leaves O((vu)^(-5/2)); v,u>=1 ensure the stated range. Its radial integral is at most Cv^(-5/2)A^(-2). The sum of |m|^(-5/2) over nonzero m in Z^2 converges, so no differentiated-remainder or nonuniform dual cutoff is needed. Retaining only the leading Bessel term would not pass this absolute-summability check.

**Infinite dual sums and arbitrary real radii — PASS.** For q=1/2 and3/2, the central norm region contributes

    sum_(n~R^2) r2(n)n^(-q/2)(1+A|R-sqrt(n)|)^(-K)
       << R^(-q+2delta)(1+R/A).

This follows from |R-sqrt(n)|=|R^2-n|/(R+sqrt(n)) and the shifted integer-grid bound, including the nearest integer. Both scale-separated regions and the plus phase contribute at most A^(-K)R^(2-q-K+2delta). For delta<=1/8 and K=4, each infinite series converges absolutely, and this expression is dominated by the preceding bound. The lower radius R>=T/2>=1 is sufficient throughout.

The report's four-term assembly is therefore valid:

    R^(-1/2+2delta)(1+R/A)
    + A^(-1)R^(-3/2+2delta)(1+R/A)
    + A^(-2) + R^(-2)A^(-3/2).

Since1<=A<=sqrt(T), every term is O(T^(2delta)sqrt(T)/A). Choosing delta=min(epsilon/2,1/8) proves the claimed uniform tail, including Y=1 andY=T. The actual infinite primal tail is already inside this Schwartz test.

**Combined norm partition — PASS.** Since gamma<beta<1/6, 2X<Y for all sufficiently large T; also X>=X0 and2Y<Z. This ensures phi>=0 even for nonmonotone eta: only one transition can be active at a time, and the other cutoff equals0 or1. The identity

    (1-eta(n/X))+eta(n/Y)+phi(n)=1

holds for every n. Thus L_gamma owns the whole low transition, H_gamma the whole upper transition and infinite tail, and phi(r2)=phi(u_gamma+w_gamma) owns precisely the middle. No norm endpoint or mixed term is omitted.

**Factor partition and extrema — PASS.** Let a=2gamma-13/42<0. Then D(x)/sqrt(x)=T^a x^(-13/84)<1, so D(x(n))^2<n. The two unbalanced divisor regions are disjoint, their swap produces chi4(d)+chi4(n/d), and equality belongs to the balanced owner. Up to fixed patch-comparability constants, throughout the middle support the cutoff extrema have exponents

    D_min: (142gamma-13)/42,
    D_max: 55gamma/42+1/28.

The minimum is positive for gamma>=13/125>13/142, so the cutoff exceeds1 asymptotically. Each retained factor is at least a constant times T^((142gamma-13)/42), and the maximum possible complementary factor is O(T^(27/28-139gamma/42)). These assertions follow from the exact monotonic cutoff and comparability x(n)~n; no global smoothness of the stepped patch-start function is assumed.

**Complementary ceilings and distribution — PASS.** The low absolute bound is X^(1/4+epsilon)=T^(gamma+epsilon). The independently established actual high bound is sqrt(T/Y)=T^gamma. For the unbalanced component, d<D(x(n)) is one interval in n for fixed d. Multiplication by phi introduces only bounded total variation, uniformly in X/Y, and hence preserves the inherited proper-interval estimate. Its principal exponents cancel exactly:

    13/84+(2gamma-13/42)/2=gamma,
    -29/168+(29/84)/2=0.

The reciprocal term and finitely many shell endpoints are smaller or logarithmic. Each resulting coefficient vector is fixed as R varies and remains divisor bounded. The accepted finite Gram proof therefore gives the same distribution estimate to each vector. Applying layer cake to its separately proved ceiling gives T+T^(10gamma)+T^(1+20gamma/13). The L12 triangle inequality proves both implications of the target equivalence.

The actual full B ceiling is used for C_gamma only after subtracting these three independently controlled components. Since gamma<beta, this gives merely the unchanged beta ceiling and10beta moment.

**Parameter table — PASS.** The table's cutoff prefactors, norm exponents and budgets are exactly correct. On the reviewed gamma interval,

    m(gamma)=1+20gamma/13 for gamma<=13/110,
             10gamma for gamma>=13/110.

Thus the three rows give respectively29/25,5/4,32/25. Although32/25<10beta, the required bound on C_(16/125) is still missing. The KRW/Hankel expression crossover is exactly N=T^(2/3), gamma=1/6, a numerical limit of these upper-bound expressions rather than an arithmetic lower bound.

# 4. First doubtful or unproved step

No gap was found in either reviewed analytic statement under the named inherited inputs. The first unproved downstream step is

    M12(C_gamma) << T^(m(gamma)+epsilon)

for a chosen gamma in the reviewed interval, or another complete physical bound below10beta. Neither independent reproduction of the old tail nor intersecting norm and factor restrictions establishes this signed cancellation.

The blind report's isolated recommendation to promote its lemma predates disclosure of the historical evidence. The conductor correctly limits the present state effect to verification and recombination; this does not require changing the frozen blind report or attributing a new estimate to it.

# 5. Controls and outcomes

- **Exact resonance and second correction: PASS.** At R=sqrt(n0), the leading sine term vanishes while the correction's C2(0) survives with coefficient1/(16pi R^(3/2)).
- **Scale separation: PASS.** No estimate uses a uniform bound for the divergent-scale cosine integral at frequency0. The sine argument remains uniform as B/A grows.
- **All tails and endpoints: PASS.** Both primal infinity and the two infinite dual tails are paid; the shifted grid is uniform over all real R^2; eta transitions include every integer endpoint.
- **Arbitrary versus actual coefficients: PASS.** The tail uses the actual r2 radial lattice identity. Generic distribution is used only after the independent component ceilings. The proof does not imply a tail theorem for an arbitrary sign mask.
- **Fixed gamma and bounded T: PASS.** The separation thresholds may depend on fixed gamma; the finitely bounded remaining T range is covered by constants. No gamma varying with T is asserted.
- **Exact rational diagnostic: PASS; diagnostic_only.** Standard-library rational arithmetic independently reproduced all table entries, the switch13/110, and cutoff extrema. For gamma=13/125,1/8,16/125 the minimum D exponents are221/5250,19/168,647/5250; maximum D exponents are361/2100,67/336,61/300; maximum complementary-factor exponents are6511/10500,185/336,811/1500. These computations merely check displayed algebra. No numerical asymptotic experiment was used.
- **Historical attribution and state scope: PASS.** Round205 section5 already contains the99/125 tail cutoff and odd kernel; Round208 section1 uses the two-sided norm-band principle. The conductor states this explicitly and claims no complete gain.

# 6. Dependencies and exact artifact hashes

The assigned source-audit context and primary references were already read in the initial task and were not expanded here. Additional reads are exactly the review brief and the two authorized reports. Primary Bessel applicability was independently checked during the source audit; no new source application was introduced during review.

| Artifact | SHA256 |
| --- | --- |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| Assigned review brief | `e40d5f152cf0cec7b87f8dfd1912262a088ad7bb3100534929a44212ca2b1793` |
| `reports/blind_hankel_tail.md` | `03b30638eb6da7242343731ac03b425e2f09e16749f73685adc343a357cd01d5` |
| `conductor_combined_owner.md` | `9f5d9a31c0624e7ee97a21bcdfa2e638154fa313cc45cbab198856222366d76b` |
| My frozen `reports/balanced_source_audit.md` | `bd7beaa816e2443be41aaed903e92c8b884b1b827b1ea5b2fb1eb9004b0e9cd7` |
| `strategy/round231_residual_saving/conductor_adaptive_factor_cutoff.md` | `02727c91e64931a13d3707ca15df021418d3e96510e35894e0d96a70182506fa` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |
| Round205 checkpoint, previously authorized section5 | `03e05b85fcb0fc72fe0e65869f13e33763fea3dc503e9a85d6d1e883eebdcfc4` |
| Round208 checkpoint, previously authorized section1 | `ae22a1a096a380b28b4b409a478dd7f87e5b1d8727068a4231ceb31272e03cbf` |

Paths in the middle four rows are relative to `strategy/round231_balanced_cancellation/`. The authoritative graph remains at the starting hash in Section1. The predecessor nonauthor review and historical files named inside the conductor artifact were not additionally opened; their mathematical interface was supplied in the assigned predecessor and checkpoints.

# 7. Recommended state effect

**Retain**, at the two frozen hashes, the verified actual smooth-tail proof and combined-owner ledger as reviewed evidence. Record PASS for all reviewed seams. No repair, new cancellation claim, complete-bound promotion, graph mutation, proof-draft update, or successor follows from this review. Only the assigned review file was written; the source report, blind report and conductor artifact remain frozen.
