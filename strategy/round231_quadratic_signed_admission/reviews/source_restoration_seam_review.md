# Nonauthor review: polynomial source applicability and complete residual cost

Round231 prelaunch admission evidence; task `source_restoration_seam_review`; nonauthor source/restoration reviewer; 2026-10-11. Frozen graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Main attack report was frozen before the reviewed source report was opened. No state authority is claimed.

## 1. Result

**PASS for the assigned source and residual-restoration seam**, with an explicit boundary-patch implementation and a useful inherited-cap clarification below. The exact primary sources support the source report's arithmetic distinction: Source A applies to the actual `r2-r2sharp`, whereas Source B's audited theorem states a divisor-function result. Quartic patches with fixed margin `epsilon0=1/25` validly give

\[
 |V_N(R)|\ll_L(1+N/T)^{-L}N^{1/4-\kappa}
\]

for a fixed unspecified `kappa>0`, on the whole retained norm range. The dependence of the approximant on each patch's own left endpoint matches the conductor's coefficient vector exactly. No rational-denominator cost occurs in this source application.

The quantitative gates are correct for the stated supremum-plus-generic-distribution certificate: strict complete moment improvement requires `kappa>1/4-beta`; the `29/25` target requires `kappa>=73/500`. The published positive-constant assertion does not certify either numerical inequality. Those are certificate thresholds, not impossibility thresholds for the source method or for the actual remainder.

If the separately reviewed main estimate is accepted as component evidence, the exact decomposition also yields the lawful inherited residual cap `|V|<<T^(beta+epsilon)`. Thus the sharpest combined ceiling in this packet is `min(beta,1/4-kappa)`. This clarification leaves the two improvement gates unchanged. No improved complete moment is established.

## 2. Exact statements, primary versions, and review scope

The reviewed source report is `reports/quadratic_source_audit.md`, SHA256 `ce861af26fb579ecda5cf5f4a208f28a48ce13ea06744494045030a69c08ff67`. Its normalization is that of the assigned complete interface: actual coefficients, fixed mollifier and window, real radius `R in [T/2,2T]`, norm head `X0=T^(52/125)`, and upper truncation `Z=T^(3/2)`.

I checked the following exact primary locations directly:

- Source A: Matomäki–Shao–Tao–Teräväinen, *Higher uniformity of arithmetic functions in short intervals I. All intervals*, [arXiv2204.03754v4](https://arxiv.org/html/2204.03754v4), especially Theorem1.1(iii), equation(1.7), the maximal-sum definition(1.4), and [AppendixA.3, PropositionA.3](https://arxiv.org/html/2204.03754v4#A1.SS3). The [version record](https://arxiv.org/abs/2204.03754v4) confirms 2024-02-28.
- Source B: Matomäki–Radziwiłł–Shao–Tao–Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, [arXiv2411.05770v2](https://arxiv.org/html/2411.05770v2), Theorem1.1(v), definition(1.4), and the separately scoped Theorem1.8. The [version record](https://arxiv.org/abs/2411.05770v2) confirms 2026-01-23.

Source A gives the actual centered coefficient bound with a power `x^(-c epsilon0)` throughout `x^(1/3+epsilon0)<=H<=x^(1-epsilon0)`. Its constant `c=c_(2,d,1)` is positive but not numerically bounded below in the statement. Its supremum includes all degree-`d` circle polynomial sequences; its star includes all progression subsums. Source B's audited very-short-interval statement instead gives a fixed-eta qualitative divisor correlation outside a small set of starts. These are separate assertions, with no automatic transfer of the actual arithmetic extension from A to B.

The Type-I main regrouping and its inherited exponent-pair phase seam have a separate reviewer. This review checks its exact coefficient coupling, its stated exponent arithmetic, and the legality of combining that component estimate with the source residual. It does not replace that separate source-seam signoff.

## 3. Independent derivation and restoration audit

### Actual coefficients and the moving polynomial

The source's AppendixA.3 formula uses `z=x^(1/20)` and precisely the two divisor ranges appearing in the report and conductor candidate. The logarithmic multiplier is

\[
 (\log n-2\log z)/\log z=20\log n/\log x-2.
\]

Both character terms in the small-divisor range are present. Replacing the source base by a common shell parameter without proof would change the approximant. Neither reviewed artifact makes that replacement: on `(l_j,u_j]` the base is `x=l_j`, and the conductor's `c_T(n)` equals that source approximant on the same patch.

Choose the circle with its fixed degree-four filtration and the fixed character `e(t)`. Its dimension is one, and its Lipschitz norm and nilmanifold complexity are fixed; take a fixed sufficiently small source complexity parameter `delta`. A Taylor polynomial whose coefficients depend on `R` remains one of the polynomials in the source supremum. No size restriction on those polynomial coefficients or Diophantine denominator appears. The arithmetic approximant depends on `T` and the predetermined patches, not on `R`.

### Degree and source-length margins

For `f(x)=R sqrt(x)`, a degree-`d` Taylor polynomial at a point in a patch of width `H` has exact residual derivative bounded by `C_d T N^(-d-1/2)H^d`. The integrated residual variation is therefore at most

\[
 C_d T N^{-d-1/2}H^{d+1}.
\]

Taking `H_d=c0 N^(1-1/(2(d+1)))T^(-1/(d+1))` makes this bounded. For `N=T^sigma`, the lower source condition has a fixed power margin exactly when

\[
 \sigma>\frac{6}{4d+1-6(d+1)\epsilon_0}.
\]

Thus the claimed quadratic boundary is correct. At `sigma=2/3`, a quadratic patch has exponent `1/3` in `N`, without the required positive margin.

For `d=4`, the norm-head boundary has

\[
 {\log H_4\over\log N}={9\over10}-{1\over5(52/125)}
 ={109\over260}={1\over3}+{67\over780}.
\]

After subtracting `epsilon0=1/25`, the lower margin is `179/3900>0`. The exponent increases with `sigma`; at `sigma=3/2` it is `23/30`, below `1-1/25` by `29/150`. Constants from `l_j~N`, the chosen small `c0`, and rounding patch counts are swallowed by these strict margins for all sufficiently large `T`. This establishes both length hypotheses uniformly over the retained shells. Bounded `T` is harmless.

### Exact first and last partial intervals

The maximal-sum star is essential. For a patch starting at real `l`, choose a nominal source length `H_src~H_4` satisfying both source inequalities at that same `l`. Its actual interval may be `(l,u]` with `u-l<=H_src`, including a very short terminal shell fragment. Apply the theorem on `(l,l+H_src]` using the approximant based on `l`, and then restrict to each prefix `(l,y]`, `y<=u`, which is a progression subsum of common difference one. This gives the bound `O(H_src N^(-kappa))` for every such prefix, even when the actual prefix is much shorter than the source's lower threshold.

No theorem at the shortened length is asserted. At most `O(N/H_4+1)=O(N/H_4)` such nominal intervals are needed in an ambient shell, since `H_4<=cN`. Thus one boundary fragment charged at full nominal length is already included in the shell cost. This is also a precise implementation of the source report's final-patch prescription. If the conductor's phrase about equal patches is used when a whole first or last shell fragment is shorter than `H_4`, this padding convention is needed: it preserves the same left-base approximant and introduces no new owner.

Half-open intervals assign integer endpoint atoms exactly once. Empty prefixes contribute zero. The head ends at the real cutoff `X0`; the last finite interval ends at `Z`; the omitted actual norms are exactly `n>Z`.

### Residual shell estimate

On a patch define `v_j(n)=r2(n)-r_(2,l_j)^sharp(n)` exactly. Write the actual phase as its quartic polynomial plus the retained exact residual. The amplitude

\[
 x^{-3/4}\Psi(\sqrt{x/T})
           e(R\sqrt x-P_{j,4,R}(x))
\]

has endpoint size plus total variation at most `C_L N^(-3/4)(1+N/T)^(-L)`. Abel summation against the source's prefix bound yields a patch cost

\[
 C_L(1+N/T)^{-L}N^{-3/4}H_4N^{-\kappa},
 \qquad \kappa=c_{2,4,1}/25.
\]

Multiplication by `O(N/H_4)` gives the claimed `N^(1/4-kappa)` shell ceiling. The small multiplier caused by comparing `l_j^(-kappa)` with `N^(-kappa)` is fixed. Decrease the saving, if necessary, so `0<kappa<1/4`. No norm or dyadic count of size `N/H_4` has been omitted: that full factor is what changes a patch bound of order `H_4` to the shell exponent `1/4-kappa`.

All approximant multipliers on a patch are bounded because `n/l_j` is bounded. Therefore `|v_j(n)|+|r_(2,l_j)^sharp(n)|<=C tau(n)`, uniformly in the retained range. This proves the coefficient-energy hypothesis needed by the accepted finite Gram/distribution argument. The vector is fixed as `R` varies; irregularity at patch boundaries does not invalidate that finite argument.

### Dyadic summation, moment conversion, and the complete exponent

Put `gamma=1/4-kappa>0`. The dyadic residual supremum is bounded by

\[
 \sum_{X0\lesssim N\le Z}(1+N/T)^{-L}N^\gamma
 \ll T^\gamma
\]

for fixed `L>gamma`. For `N<=T` this is a geometric increasing sum; for `N>T` the Schwartz factor makes it decreasing. The actual omitted infinite tail is separately `O_K(T^(-K))`, exactly as in the accepted kernel. This is not an unproved extension of the source theorem to infinite intervals.

The generic distribution applies to the finite residual vector using its divisor bound. Its complete diagonal and localization ceiling remain. Layer cake from level one to the new ceiling gives

\[
 M_{12}(V)\ll_\epsilon T^\epsilon
 \left(T+T^{10\gamma}+T^{1+20\gamma/13}\right).                \tag{R1}
\]

The exponent `20/13` is `12-136/13`; hence this conversion is exact. No actual-circle supremum is imported into a coefficient mask here.

The conductor main's stated exponent is

\[
 g_s={13\over84}-{103\over840}{52\over125}
 ={13\over125}-{13\over52500}.
\]

Its third layer-cake exponent is `1+20g_s/13=29/25-1/2625`; its second is smaller. Subject to its separate main-source review, this component is therefore paid at the target. Its patch coefficients are exactly the ones subtracted in the source residual; there is no interface discrepancy or missing change-of-approximant term. The norm head is paid by `T+X0^(5/2)+T X0^(5/13)`, and the actual infinite tail has moment `O(T^(1-12K))`. The finite twelfth-power norm inequality pays every mixed contribution. Thus the proposed complete certificate is precisely

\[
 b_{12}^{\rm cert}=\max\{29/25,\ 10\gamma,\ 1+20\gamma/13\}.
                                                                    \tag{R2}
\]

There is also a legitimate sharper inherited fallback. The exact real-wave identity is `V=B_T-H_X-Ssharp-tail`. Since `|H_X|<<T^(13/125)`, `|Ssharp|<<T^(g_s+epsilon)`, and both exponents are smaller than `beta`, the inherited actual full-wave bound implies `|V|<<T^(beta+epsilon)`. Thus `gamma_eff=min(beta,1/4-kappa)` can replace `gamma` in (R1)--(R2), once the main estimate is available. This deduction uses the exact decomposition and separate component ceilings; it does not assume that arbitrary masks inherit the actual supremum. It guarantees that the combined evidence is never reported as weakening the inherited complete exponent.

### Quantitative gates

For strict improvement on `10beta`, the `10gamma` term in (R2) must be strictly smaller, hence `gamma<beta`. Conversely that inequality suffices for all three terms: the head exponent `29/25` is below `10beta`, while `1+20beta/13<10beta` is equivalent to `beta>13/110`, which holds. Therefore the exact gate for this certificate is

\[
 \kappa>1/4-\beta=0.121033648\ldots .                          \tag{R3}
\]

For the `29/25` target, the two residual terms respectively require `gamma<=29/250` and `gamma<=13/125`. The latter is stronger, giving

\[
 \kappa\ge 1/4-13/125=73/500.                                 \tag{R4}
\]

The inherited cap does not change either gate because the current `beta` lies above both target ceilings. An unspecified assertion `c>0` establishes neither (R3) nor (R4). This does not prove those inequalities false for any particular constant obtainable by a refined source proof; it establishes that the audited statement alone does not certify them.

### Source B and exceptional sets

Theorem1.1(v) is stated for `d_k-d_ksharp`, not `r2-r2sharp`; the circle phase does satisfy its additional one-bounded-test condition. Its fixed-eta conclusion cannot be used with `eta=N^(-c)` while leaving the implied constants unchanged. The exceptional set concerns real starts in a norm shell. A small Lebesgue measure alone gives no guarantee on a prescribed finite set of tiling starts: an exceptional set may contain all such starts without violating its measure bound. It is also not a measure estimate in the physical variable `R`.

The report correctly treats these as unpaid transfer issues, rather than as estimates on the actual remainder. Theorem1.8 is separately a fixed-linear-phase divisor theorem with power savings and an exceptional set. It does not provide the uniform moving quartic application required here. This review finds no hidden direct repair from either audited Source B statement.

## 4. First doubtful or unproved step

The source-to-quartic-residual transfer passes. The first missing quantitative input is a certified residual saving crossing (R3), or some different complete mechanism improving its moment without that pointwise gate. Neither the source's positivity of `c_(2,4,1)` nor the payment of the Type-I approximant proves it.

The separate Type-I fixed-shift exponent-pair review remains an explicit dependency of assertions involving its paid ceiling. This review does not promote that component merely because its source residual and coefficient coupling are valid. Source B additionally fails the direct actual-coefficient premise before any exceptional-set restoration is attempted.

## 5. Required controls and outcomes

- **Primary theorem and version:** Checked the exact source formulas and version records, not just abstracts. A.3 refers to the relevant power-saving part of Theorem1.1. PASS.
- **Actual approximant:** Both divisor ranges, both small-divisor character terms, and `z=l_j^(1/20)` match the conductor coefficient. PASS.
- **Degree and moving complexity:** Degree four and fixed circle complexity are valid uniformly in `R`. No denominator approximation is needed. PASS.
- **Length extremes:** Lower margin `179/3900` and upper margin `29/150` are strictly positive. Quadratic boundary still fails. PASS.
- **Short boundary control:** Pad at the same left endpoint and invoke the maximal prefix bound; charge the full nominal source length once. This supplies a concrete convention for arbitrarily short first/last fragments. PASS with stated implementation.
- **New vector versus actual supremum:** Generic distribution uses only the fixed vector's divisor bound. The improved fallback cap is deduced from the exact decomposition after main payment. No arbitrary-mask inference. PASS.
- **Complete restoration:** Dyadic shells, real projection, finite mixed terms, all endpoint atoms and actual infinite tail are retained. Gates (R3)--(R4) are scoped to the displayed certificate. PASS.
- **Almost-all control:** A set small in norm-start measure is not automatically small on a fixed tiling or in radius measure. Fixed qualitative eta is not a power saving. PASS for the source report's negative admission conclusion.
- **Analytical allocation:** No numerical experiment, source-constant guessing, or asymptotic simulation was used. Computation was limited to reading and hashing. PASS.

## 6. Dependencies and exact provenance

Local files used for this review are exactly the assigned source report, conductor main candidate, complete interface, review brief, and accepted complete moment kernel, together with the protocol and immutable session context already read before the earlier task. The primary exact versions are linked in Section2. No additional sibling report, validation matrix, shared synthesis, graph mutation, or successor file was accessed. The reviewer authored the separate quadratic attack before seeing this source report; that earlier authorship does not extend to the reviewed source or Type-I candidate.

Input hashes at review:

```
strategy/round231_quadratic_signed_admission/briefs/source_restoration_review.md
c464ffa185db015b3591bbd9ea98004dab2dffe65ec861f082d2532375041c7d
strategy/round231_quadratic_signed_admission/reports/quadratic_source_audit.md
ce861af26fb579ecda5cf5f4a208f28a48ce13ea06744494045030a69c08ff67
strategy/round231_quadratic_signed_admission/conductor_type_i_main.md
d2616bb4bd69588796f764d38e0c1cb3e9133b2e0808b95056892c6bb32fd6c5
strategy/round231_quadratic_signed_admission/briefs/complete_interface.md
abaa43deda1db65351578941aec47e2af0aadfedcf0942b95bfea4c8636de83d
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md
942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212
```

Remote sources were read through the version-pinned primary HTML pages. No claim is made that a web-response hash is a PDF hash; the source report's separately recorded response hashes were not independently recomputed here. The final review file hash is communicated after freezing.

## 7. Recommended state effect

Retain the Source A actual-coefficient application and the fully restored residual component as reviewed evidence, with the explicit boundary convention. Retain the precise quantitative admission failure and Source B exclusions. Record the inherited residual cap as a valid refinement once the independent Type-I main seam passes. Do not convert the unspecified saving into a numerical complete gain. No graph, proof-draft, validation, campaign, synthesis, or successor change is made or recommended by this bounded review alone. Stop after the review and its hash.

**Final-hash clarification acknowledgment, 2026-10-11.** I read the revised Section2 boundary and bounded-parameter paragraphs of `conductor_type_i_main.md` and verified its SHA256 `7b05d13908b116acf2a40320040b4a7614a4f80ec2fcfcde073eb5055957924f`. The nominal source interval keeps the same left-base approximant and pays each short boundary fragment using the maximal prefix estimate, exactly as required above. Setting the approximant to zero for the fixed compact range `2<=T<T0` is legitimate: the main is then zero, the exact residual definition remains available, and uniform divisor/Schwartz bounds on this bounded range permit the complete estimates after enlarging constants. PASS is affirmed for these clarifications, with all original scope qualifications unchanged. The earlier candidate hash in Section6 remains the historical input reviewed for the derivation; this acknowledgment binds the two clarified conventions to the final candidate hash.
