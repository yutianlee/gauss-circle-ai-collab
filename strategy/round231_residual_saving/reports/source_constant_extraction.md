# Quantitative source constants and the physical Taylor phase

Round231 prelaunch admission evidence; task `source_constant_extraction`; source auditor; 2026-10-11. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. This is a candidate report, not accepted mathematics. The active campaign read was the completed Round230 campaign. No state file is changed.

## 1. Result

There is a useful phase-specific replacement for the source's unspecified uniform residual constant: **the actual quartic Taylor phases have no source major arcs below explicit thresholds, for every physical radius**. The actual function `r2=4(1*chi4)` already belongs to Type I_2 with auxiliary support parameter one. Thus the inverse theorem can be applied directly to actual coefficients; no Type II branch or additional arithmetic approximation is necessary.

However, combining all inverse-theorem powers into one constant loses too much. I prove that a common inverse exponent `C_d` necessarily satisfies `C_d>=d`. Even allowing arbitrary fixed Taylor degree, the corresponding ceiling certificate can save at most `7/72`, below `1/4-beta`. This is a rigorous obstruction to that certificate, not to the actual phase-specific estimate.

Keeping the inverse powers separate produces a concrete admission target. If the length exponent were `A=3` and both character/smoothness exponents were `B=4`, then the same exact complete decomposition would give

`M12(B_T) << T^(23/18+epsilon)`,

strictly improving `T^(10 beta+epsilon)`. **The source does not establish these numerical values.** Its first unresolved numerical dependencies are identified below. No complete gain is claimed.

## 2. Exact statements and hypotheses

All actual coefficients, `rho,Psi,w,B_T,beta`, real radii, and accepted moment/distribution inputs are those in `briefs/residual_interface.md`. Keep `X0=T^(52/125)`, `Z=T^(3/2)`, the existing ordered quartic patches, and the exact local approximant with cutoff `z=x^(1/20)`. Write

`H=c0 x^(9/10) T^(-1/5)`, `x~N=T^sigma`, `52/125<=sigma<=3/2`,

with fixed sufficiently small `c0>0`. Comparability constants and bounded T are absorbed into constants. The degree-four Taylor polynomial at x is

`P_R(x+u)=R sqrt(x)+R u/(2 sqrt(x))-R u²/(8x^(3/2))+R u³/(16x^(5/2))-5R u⁴/(128x^(7/2))`.

For `Q>=1`, define the actual radius major-arc set

`E_x(Q)={R in [T/2,2T]: exists integer 1<=q<=Q with ||qP_R||_(C-infinity(x,x+H])<=Q}`.

The source norm uses scaled finite differences; any fixed equivalent degree-four norm only changes constants. There is an absolute fixed `c1>0` such that

`E_x(Q)=empty` if `Q<=c1 min(x^(5/2)/T, T H³/x^(5/2))`.                 (2.1)

In particular its Lebesgue measure and its number of connected components are both exactly zero under (2.1). This concerns physical R, not an exceptional set of interval starts.

For constant extraction, use the following explicit interface for the degree-four, dimension-one, `A_I2=1` source inverse theorem. If a maximal actual polynomial sum is at least `delta H`, then either

`H<=K delta^(-A) x^(1/3)`,                                         (2.2)

or there is an integer `1<=q<=K delta^(-B)` with

`||qP_R||_(C-infinity(x,x+H])<=K delta^(-B)`.                        (2.3)

Here K is fixed. The source implies existence of finite positive A,B, but supplies no stated numerical pair. Allowing separate powers for q and the norm is an additional possible refinement; choosing the larger one as B is enough here. All inequalities in applications below include an arbitrarily small fixed exponent margin.

## 3. Proof, source trace, and complete restoration

### Primary source dependency trace

The exact primary source is Matomäki–Shao–Tao–Teräväinen, [arXiv2204.03754v4](https://arxiv.org/html/2204.03754v4), 2024-02-28. The audited chain is Theorem1.1(iii), PropositionA.3, Lemma4.4, Theorem4.2(iv), and Proposition8.3. For k=2, only Type I and Type I_2 are needed; the abelian Type II alternative is irrelevant. Theorem1.1's proof after (4.23) chooses its small constant qualitatively. At (8.16), quartic composition with `(n0-ka)(m0+kq)` has degree eight and invokes Theorem2.7. That theorem retains unnamed effective powers. The downward induction (8.17) invokes Lemma2.3 twice per degree; its proof imports another unnamed power from reference19, Lemma4.5. No numerical A,B follow by reading these statements. This is a precise dependency bottleneck, not an assertion of ineffectivity. Theorem8.1's explicit hyperbola geometry does not remove it. [Source, Sections4.2 and8](https://arxiv.org/html/2204.03754v4#S8).

In that geometry the progression length is of order `(H³/x)^(1/4)`. Consequently a requirement that this length exceed `delta^(-E)` already turns into a length exponent `4E/3` in (2.2), before further losses are combined. Obtaining A=3 would require controlling that intermediate E and all other losses sufficiently sharply; it is not a value furnished by the source.

### Direct actual-coefficient application

In the Type I_2 definition take `alpha=4·1_{n=1}`, `beta1=1`, `beta2=chi4`. Their convolution is r2. The alpha square-mean condition and both variation conditions modulo4 hold for every sufficiently small delta, with fixed constants. In particular, there is no need for an arbitrary-coefficient estimate here. The fixed circle test `e(t)` has mean zero and bounded Lipschitz norm; its polynomial has degree four and coefficients may depend on R. Thus (2.2)--(2.3), including maximal prefixes, are a direct consequence of the source inverse theorem with some fixed A,B.

This bypasses the approximant only during estimation of the actual finite wave. It does not change the coefficient identity defining V. The already paid `Ssharp` remains present when passing back to V.

### Empty major arcs, with all radii retained

With the backward difference convention, put `u=n-x`. Direct algebra gives

`Delta³ P_R(n)=3R/(8x^(5/2)) - 15R(u-3/2)/(16x^(7/2))`.

Since `H/x` tends to zero uniformly over the specified norm range, and c0 is fixed small, this lies between two positive constant multiples of `T/x^(5/2)` for every relevant integer n and every `R in [T/2,2T]`. If `q<=Q<=c1 x^(5/2)/T`, then `0<q Delta³P_R(n)<1/2`; there is no wrap modulo one. Hence

`H³ ||q Delta³P_R(n)|| >= c2 T H³/x^(5/2)`.

Taking c1 smaller makes this exceed Q under the second inequality of (2.1), contradicting (2.3). This proves (2.1). Empty integer intervals do not occur in the asymptotic range; bounded parameters are paid separately.

Set

`ell(sigma)=17/30-1/(5sigma)`,

so `H/x^(1/3)` has x-exponent ell. The two empty-arc thresholds have x-exponents

`b1(sigma)=5/2-1/sigma`, `b2(sigma)=1/5+2/(5sigma)`.

Both exceed ell throughout the complete norm range. Their differences are respectively

`29/15-4/(5sigma)>=2/195`,

`-11/30+3/(5sigma)>=1/30`.

Thus common-constant use of the inverse theorem pays the length condition before any major arc arises. This proves a genuine all-radius statement, with no unestimated exceptional owner.

### Separate inverse exponents and the conditional complete gain

For every fixed small `eta>0`, apply the contrapositive with

`delta=x^(-k(sigma)+eta)`,

`k(sigma)=min(ell(sigma)/A, b1(sigma)/B, b2(sigma)/B)`.

Fixed constants, the source restriction `delta<1/log x`, and all strict inequalities hold for large x after the eta loss. The resulting maximal patch bound is `O(H x^(-k+eta))`. Partial summation against the exact Taylor remainder and the fixed smooth amplitude costs `O_L(x^(-3/4)(1+x/T)^(-L))`. Charge the full nominal source H on every short boundary fragment; the star estimate permits the necessary prefixes. The number of charged patches in one shell is `O(N/H)`. Thus the actual finite shell satisfies

`|D_N(R)| <<_(L,eta) (1+N/T)^(-L) N^(1/4-k(sigma)+eta)`.          (3.1)

Here D is the actual wave on `X0<n<=Z`; it is not an arbitrary mask imported into the actual supremum theorem. Its coefficient vector is fixed as R varies, so the accepted coefficient-uniform distribution estimate applies.

For A=3, B=4, the three possible shell exponents in powers of T are

`sigma/4-sigma ell/3 = 11sigma/180+1/15`,

`sigma/4-sigma b1/4 = 1/4-3sigma/8`,

`sigma/4-sigma b2/4 = sigma/5-1/10`.

On `52/125<=sigma<=1` their maximum is at most `23/180`, attained by the first at sigma=1. At the lower endpoint the second is `47/500`, also smaller. For sigma>1 choose the Schwartz-decay exponent L larger than all three slopes, so no larger T-power occurs. Consequently

`sup_R |D(R)| << T^(23/180+epsilon)`.

The head ceiling is `T^(13/125)` and its moment is paid at `29/25`. The paid approximant ceiling is `T^(5447/52500+epsilon)`. Both ceilings are smaller than `23/180`. Since `V=D-Ssharp` exactly on the same patches, the same new ceiling would hold for V. The original approximant, including its local cutoff and both character terms, is unchanged. The actual tail above `T^(3/2)` is arbitrarily small by fixed Schwartz decay. A finite twelfth-power norm inequality pays all mixed terms. Finally the accepted distribution gives

`M12(D), M12(V) << T^epsilon [T+T^(23/18)+T^(140/117)]`.

All complete owners therefore fit `23/18`, conditionally on A=3,B=4. The comparison `23/18<10beta` is strict. This proves the advertised conditional complete implication; it does not assert its unproved inverse constants.

### A rigorous obstruction to replacing A and B by one favorable C

Let d>=2 be fixed. Suppose the general degree-d inverse theorem could be written with one common exponent `C<d` in its length, character-size, and smoothness bounds. Test it on the admissible Type I_2 function `f=1`, represented by `alpha=1_{n=1}`, `beta1=1_{n=1}`, `beta2=1`. Take primes `p>d`, `P(n)=n^d/p^d`, and `X=H=p^K`, where the fixed integer K is sufficiently large. Set `delta=1/(2p)`.

The exact complete sum modulo `p^d` is `p^(d-1)`. To see this, group residues as `n=a+p^(d-1)b`, `0<=a<p^(d-1)`, `0<=b<p`. The sum in b vanishes unless `p|a`, since `p` does not divide d. Every surviving residue n is divisible by p, so its phase is integral. Thus the sum on `(X,X+H]` is exactly `H/p>=delta H`.

Choose K so large that `H/x^(1/3)=p^(2K/3)` exceeds every fixed multiple of `delta^(-C)`. The length alternative fails. Any nonzero horizontal integer q allowed by the character bound has `|q|<<p^C<p^d/d!` eventually. Since `p>d`, the leading difference obeys

`||Delta^d(qP)||=||d!q/p^d||>=p^(-d)`.

Therefore its C-infinity norm is at least `H^d/p^d=p^(Kd-d)`, exceeding the proposed `O(p^C)` smoothness bound. Both alternatives fail: contradiction. Hence every such common exponent must satisfy `C_d>=d`.

At the dominant physical scale N~T, a degree-d Taylor patch has `H~T^(1-3/(2(d+1)))`. The length-based saving of this common-C certificate is at most

`[2/3-3/(2(d+1))]/C_d <= (4d-5)/(6d(d+1))`.

Among integers d>=2 the maximum is `7/72` at d=3; the quartic value is `11/120`. This can be checked by subtracting consecutive terms, or direct differentiation followed by checking d=2,3,4. Both are less than `1/4-beta`. Thus neither choosing a larger polynomial degree nor optimistically extracting a common exponent can make this specific ceiling-plus-distribution certificate improve the complete moment. The test is an inverse-theorem control, not a counterexample to the actual square-root phase. In particular it does not impose A>=d separately; keeping A and B distinct is essential.

### Uniform source margin optimization and the conductor's control

For the unchanged maximal quartic patches, the largest uniform source margin is `epsilon0<67/780`, rather than the previous convenient `1/25`; the upper length condition is looser. For the maximal degree-d patches over the same full norm range, the limiting margin is

`min(2/3-151/(52(d+1)), 7/(6(d+1)))`.

It is maximized at d=5, giving `19/104`. These are margins, not savings: each is multiplied by its degree-dependent source constant. Shortening patches to also impose `H<=x^(1-epsilon0)` is legitimate and can allow margins approaching `1/3` at sufficiently large fixed degree; this does not justify a larger uniform residual saving.

The conductor supplied an independent zero-phase diagnostic during this task: for integer `z=1 mod4`, `x=z^20`, the fixed approximant has a mean defect of order `H/z`. Its complete proof and blind control are outside my allowed context, and I do not use it as an accepted dependency. It is consistent with, and distinct from, the common-inverse-exponent obstruction proved above. No alleged positive lower bound for an available source constant has been inferred from any upper obstruction.

## 4. First doubtful or unproved step

The exact primary theorem gives some A,B in (2.2)--(2.3), but the step **A=3,B=4** is unproved. Proposition8.3's degree-eight quantitative equidistribution at (8.16), followed by repeated Vinogradov concatenation in (8.17), is the first precise numerical dependency not resolved within the permitted source. The paper's effective `O_d(1)` notation cannot be assigned these values. Tracing it would require a new explicit proof, not another application of Theorem1.1(iii).

The empty-major-arc lemma and the conditional complete implication have proofs above. An averaged-radius theorem with larger denominator/smoothness ranges has not been proved here. Above (2.1), the major-arc owner remains unpaid; it has not been called negligible. No exceptional set in a norm-start variable has been reinterpreted as physical-radius measure.

## 5. Required controls and outcomes

- **Actual arithmetic:** `r2=4(1*chi4)` satisfies Type I_2 with support parameter one and fixed variation modulo4. PASS.
- **Phase and maximal boundary control:** The third backward difference is explicitly positive and small on every patch; real R, fixed patch starts, exact Taylor remainder, and full nominal padding are retained. PASS.
- **Major arcs:** In the claimed range, the exceptional radius set is exactly empty. No measure estimate is needed or silently substituted. PASS.
- **Inverse-constant adversary:** The exact prime-power monomial sum proves `C_d>=d` for the common-exponent interface. This is an algebraic test, not numerical evidence. PASS.
- **Complete restoration:** Under the explicitly hypothetical separate exponents, head, approximant, all finite norms, partial intervals, and the infinite actual tail give `23/18`; no actual-mask supremum is assumed. PASS for the implication; FAIL/UNPROVED for the numerical premise.
- **Degree/margin optimization:** The best common-C ceiling saving remains at most `7/72`, even under more favorable degree availability than the fixed head permits. Scope is that certificate only. PASS.
- **Effort allocation:** Analytical derivations and direct primary-source reads only; no numerical experiment or asymptotic simulation. PASS.

## 6. Dependencies and exact artifacts used

Local context was restricted to the task brief, protocol, active campaign, the two selected graph nodes, the residual interface, and the two named previous-packet reports. File hashes at access:

```
protocol.md
f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a
state/active_campaign.yml
fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa
state/proof_obligations.yml
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b
strategy/round231_residual_saving/briefs/source_constant_extraction.md
72ebfd4613b4b0860aa70ad1787985573cdc0d5540c351666d764a2eb5a1edd5
strategy/round231_residual_saving/briefs/residual_interface.md
bd57b6e13b85ee0d15905ff74a66ca4326cfe00c0020a11b4b4a7608eb994bad
strategy/round231_quadratic_signed_admission/reports/quadratic_source_audit.md
ce861af26fb579ecda5cf5f4a208f28a48ce13ea06744494045030a69c08ff67
strategy/round231_quadratic_signed_admission/reviews/source_restoration_seam_review.md
fdf35ef0fa82b9570fbbcaabf0d5083210e5ccf044d84ffa36c54e2acf38ce66
```

The two selected accepted graph nodes were `GC-complete-square-root-large-values-moment-bound` and `GC-complete-distinct-radical-twelfth-reduction`; no other graph claim was used. A filename-only search resolved the relative interface and previous-report paths. The previous source report was read with output truncation, so only visible passages and the fully read seam review are relied upon. No sibling report was opened. Primary reading was confined to the exact arXiv2204.03754v4 source and internal locations named above. The conductor's mathematical messages supplied the separately marked zero-phase diagnostic and independently checked the separate-exponent conditional arithmetic; they did not supply an unrecorded theorem proof.

## 7. Recommended state effect

Retain the proved empty-major-arc lemma and the common-inverse-exponent obstruction as candidate evidence pending nonauthor review. Revise source admission from an unspecified uniform c to the explicit separate-exponent interface (2.2)--(2.3), with A=3,B=4 a sufficient unproved complete-gain target. Retain every accepted complete bound and the exact approximant. Do not promote `23/18`, reject the actual residual target, or infer a full theorem. No state, proof draft, validation matrix, synthesis, or successor file is edited. Stop after this report and its externally communicated SHA256.
