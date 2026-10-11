# Round 231: nonauthor physical-phase and inverse-interface review

Task: `review_physical_inverse`; reviewer: the completed statement-only arithmetic agent, now under a separate nonauthor review assignment. Date: 2026-10-11T15:04:43+08:00. Supplied graph identifier: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`; the graph was not read. The isolated original report is unchanged. This review is candidate evidence and makes no state mutation.

## 1. Result

**PASS** for the physical quartic empty-major-arc lemma, actual Type I_2 application, common-exponent obstruction, fixed-degree optimization, and the complete **conditional** implication with exponents A=3, B=4. No mathematical repair is required for these scoped statements. Some implicit fixed-constant and endpoint details are made explicit below.

**UNPROVED** for the numerical source premise A=3, B=4 and therefore for an unconditional complete moment exponent 23/18. The report correctly distinguishes these statuses. This review does not certify explicit source powers.

## 2. Exact statement, hypotheses, and scope

The target reviewed is `reports/source_constant_extraction.md` at the frozen hash recorded in Section 6. Its polynomial, physical radii R in [T/2,2T], nominal patch length H=c0 x^(9/10)T^(-1/5), norm range T^(52/125) <= x <= T^(3/2), exact decomposition, and supplied coefficient-uniform distribution input are retained.

The reviewed conditional interface is: a maximal sum with the actual r2 coefficients of size at least delta H implies either H <= K delta^(-A)x^(1/3), or a nonzero integer character of size at most K delta^(-B) and smoothness norm at most K delta^(-B). Here K is a fixed multiplicative constant; A and B are exponents. The common-C obstruction concerns an inverse theorem for the entire admissible Type I_2 class, not merely the one physical phase or only r2.

The primary source was independently checked at [arXiv2204.03754v4, Section 4](https://arxiv.org/html/2204.03754v4#S4), Definition 4.1(iii) and Theorem 4.2(iv), together with [Section 2](https://arxiv.org/html/2204.03754v4#S2), Definition 2.1 and the smoothness definition in Section 2.2. The source permits H <= X, uses maximal progression subsums, and supplies finite unspecified exponent losses. Its smoothness norm includes scaled backward differences at every integer in the interval, so the report's positive third difference is a valid direct lower bound. No value 3 or 4 for the relevant losses is provided by those statements.

## 3. Derivation and line audit by seam

### A. Actual Type I_2 membership — PASS

For alpha=4*1_(n=1), beta1=1 and beta2=chi4, the convolution is exactly r2. The square-mean bound for alpha is at most 16, hence at most delta^(-1)A for every A>=1 when delta<=1/16. With modulus four the two variation norms are respectively 4 and 2: each residue-class sequence is constant, so its norm is just its absolute value. Thus delta<=1/16 pays both norms and the modulus. The fixed circle test has bounded Lipschitz norm and zero mean; a further fixed upper bound on delta pays any circle normalization. These restrictions alter multiplicative constants only, not inverse exponents.

This application concerns actual coefficients directly and does not discard the already defined approximant when recovering V.

### B. Third difference and empty major arcs — PASS

Writing u=n-x, backward differences give Delta^3(u^3)=6 and Delta^3(u^4)=24u-36. Consequently the report's identity is exactly

    Delta^3 P_R(n) = 3R/(8x^(5/2)) - 15R(u-3/2)/(16x^(7/2)).

Uniformly in the physical range, H/x=c0 x^(-1/10)T^(-1/5) tends to zero. The displayed difference is therefore between positive constant multiples of T/x^(5/2), including integers next to either real endpoint. Backward differences evaluate the same polynomial outside the patch; no assumption on the original phase outside the patch is needed.

If 1<=q<=Q and Q<=c1 x^(5/2)/T, sufficiently small fixed c1 forces 0<q Delta^3P<1/2. Thus its distance to the nearest integer is its actual value. Since q>=1, the smoothness norm is at least c2 T H^3/x^(5/2). A second fixed choice c1<c2 then excludes norm <=Q whenever Q<=c1 T H^3/x^(5/2). This proves exact emptiness and hence zero measure and zero components. The argument is uniform in all physical R; there is no exceptional-start substitution.

The exponent calculations also check:

    ell = 17/30 - 1/(5 sigma),
    b1 = 5/2 - 1/sigma,
    b2 = 1/5 + 2/(5 sigma),
    min(b1-ell) = 2/195,  min(b2-ell) = 1/30.

The minima occur at the appropriate endpoints of 52/125 <= sigma <= 3/2. Both gaps are strictly positive.

### C. Common-C counterexample — PASS

The class member f=1 has alpha=1_(n=1), beta1=1_(n=1), beta2=1. At modulus one their variation norms are 2 and 1, and the alpha square-mean norm is harmless. Thus it is admissible for delta=1/(2p).

For fixed integer d>=2, prime p>d, and P(n)=n^d/p^d, write n=a+p^(d-1)b. Modulo p^d, every binomial term of degree at least two in b vanishes, while the first produces the b-phase d a^(d-1)b/p. Its complete b-sum vanishes unless p divides a. Every surviving n is divisible by p and has integral P(n); there are p^(d-1) survivors. The complete sum is exactly p^(d-1), with no unestimated error term.

Take a fixed integer K>=d sufficiently large and X=H=p^K. The interval contains complete periods, so its sum is exactly H/p. Also delta<1/log X eventually. If a proposed common C<d is used, K can satisfy both 2K/3>C and Kd-d>C. These strict inequalities defeat every fixed multiplicative constant in the length and norm bounds.

A nonzero allowed q has |q|<=O(p^C)<p^d/d! eventually. Since p>d, d! is invertible modulo p and d!q/p^d is nonintegral. Its distance to an integer is at least p^(-d). Thus the d-th difference forces norm >=H^d/p^d, contradicting the proposed smoothness bound. Both inverse alternatives fail. The necessary conclusion C_d>=d is valid. It does not impose A>=d when the exponents are separate.

### D. Optimization over fixed degree — PASS, scoped to the certificate

At x approximately T, the Taylor remainder allows H approximately T^(1-3/(2(d+1))). The common-C length condition can supply at most

    s_d = (4d-5)/(6d(d+1)).

Direct subtraction gives

    s_(d+1)-s_d = (10-4d)/(6d(d+1)(d+2)).

Hence the integer maximum for d>=2 is s_3=7/72; s_4=11/120. Degree one does not escape this argument: its maximal patch is only T^(1/4), below the required x^(1/3) even before a saving. Constant phases likewise supply no useful physical Taylor patch. The strict comparison 7/72 < 1/4-beta holds.

This rules out improvement by this common-C ceiling/distribution certificate, even when granting favorable degree availability. It does not rule out a better inverse statement with separate powers, a direct signed moment argument, or cancellation between patches.

The supplementary margin arithmetic checks as well: the full-range margin is the minimum of 2/3-151/[52(d+1)] and 7/[6(d+1)]. It peaks at d=5 with value 19/104, and for d=4 is 67/780. These are length margins, not numerical savings.

### E. Conditional A=3, B=4 complete restoration — PASS for the implication

For sufficiently small fixed eta>0, delta=x^(-k+eta) with k=min(ell/A,b1/B,b2/B) is eventually below every fixed source threshold and 1/log x, uniformly in the compact sigma-range. Its exponent margin absorbs K, c1, c0 and strict inequalities. For A=3,B=4 all three bounds defining k are positive on this range.

The fifth Taylor remainder has size and total variation O(T x^(-9/2)H^5)=O(c0^5); its oscillatory factor can therefore be absorbed by partial summation. The smooth amplitude costs O_L(x^(-3/4)(1+x/T)^(-L)). Maximal prefix bounds permit full nominal padding of each boundary fragment. With O(N/H) patches this gives the claimed shell ceiling.

Independently computing its three T-exponents gives

    11 sigma/180 + 1/15,
    1/4 - 3 sigma/8,
    sigma/5 - 1/10.

On [52/125,1], the respective maxima are 23/180, 47/500 and 1/10. For sigma>1 the Schwartz factor subtracts L(sigma-1), so any fixed L larger than the slopes prevents a new maximum. Summing the logarithmically many shells costs only the permitted epsilon loss.

The distribution input and ceiling S=T^(23/180+epsilon) yield, by layer-cake integration, the three owners

    T,  S^10,  T S^(20/13),

with exponents 1, 23/18 and 140/117. Both D and V have coefficient vectors fixed as R varies; for V the local starts and logarithmic divisor weights also remain fixed, and are divisor bounded. Thus the supplied coefficient-uniform distribution input is the applicable one. No masked version of the actual supremum theorem is used.

The head exponent 29/25 and approximant exponent 3044/2625 are below 23/18. Their ceilings are also below 23/180, so V=D-Ssharp has the needed conditional ceiling. For the remaining actual tail, divisor boundedness and Schwartz decay give, for arbitrarily large fixed L,

    sum_(n>Z) |r2(n)| n^(-3/4)|Psi(sqrt(n/T))|
      << T^L Z^(1/4+epsilon-L),   Z=T^(3/2),

which is arbitrarily small after increasing L. A finite twelfth-power inequality then pays every mixed term of the complete decomposition. The conditional exponent is consequently 23/18 < 10 beta. The numerical inverse premise remains unproved throughout.

## 4. First doubtful or unproved step

The first unproved step required for a new complete bound is assigning the separate powers A=3 and B=4. The source theorem establishes some finite powers but does not identify this pair. This review checks the source interface and the resulting conditional algebra; it does not independently reconstruct every quantitative loss in Section 8 or its imported Vinogradov lemma. Therefore it does not certify the report's proposed constant extraction target as achieved.

No gap was found in the preceding physical empty-arc lemma or the common-C no-go theorem. Above the displayed empty-arc threshold, no exceptional-radius estimate has been supplied or inferred.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Source uses the same backward-difference convention and includes the third difference | PASS |
| Genuine r2 Type I_2 representation with explicit fixed variation and square-mean constants | PASS |
| Positive third difference, no modular wrap, all physical radii and real endpoints | PASS |
| Prime-power sum with p>d, exact complete periods, K>=d, and nonzero integer q | PASS |
| Common-C contradiction defeats arbitrary fixed multiplicative constants | PASS |
| All fixed degrees, including failure of degree-one source length | PASS for the stated certificate |
| Conditional shell maximum, distribution integration, head, approximant, boundary pieces and infinite tail | PASS for the implication |
| Claim that A=3,B=4 is supplied by the paper | UNPROVED; correctly not asserted |
| Original isolated report preserved | PASS; unchanged SHA256 below |

These are analytical and exact algebraic controls. No numerical experiment was performed.

## 6. Dependencies and checked hashes

Only the assigned context and exact primary source were read. The checked hashes are:

```
protocol.md
f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a

strategy/round231_residual_saving/briefs/review_physical_inverse.md
5ba5146972fdcd73bc704b955417c96c14e972db2d590d22da67af442a30820c

strategy/round231_residual_saving/reports/source_constant_extraction.md
fb2eda32f5667262f00e4a51e94cdd25d7121659dbdd9578142fcff092a6b954

strategy/round231_residual_saving/briefs/residual_interface.md
bd57b6e13b85ee0d15905ff74a66ca4326cfe00c0020a11b4b4a7608eb994bad

strategy/round231_residual_saving/reports/blind_residual_control.md
c78fa696c881c3068541a38ae807fc1de9a58817c87c30716524e471478a2d2b
```

The original statement brief and coordinator messages remain provenance from the completed first assignment, but the arithmetic residual obstruction is not needed to validate this report's physical inverse proof. Primary source version: Matomaki--Shao--Tao--Teravainen, arXiv:2204.03754v4, 28 February 2024; source locations are linked in Section 2. Supplied accepted moment and distribution estimates are treated as interface dependencies, not independently re-proved here.

## 7. Recommended state effect

**Retain** the physical empty-arc lemma and common-C obstruction as positively reviewed candidate evidence. **Retain** 23/18 only as a conditional implication with the numerical source premise explicitly open. No repair is requested for the frozen report.

**No graph change** follows from this review alone: the conductor still owns promotion gates, source cards, any additional required seam evidence, and mechanical State Patch validation. No shared file, original report, synthesis, or successor-round artifact was edited.
