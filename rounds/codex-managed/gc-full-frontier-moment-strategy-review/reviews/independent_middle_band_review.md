# Round 205: independent middle-band reduction review

Campaign: `gc-full-frontier-moment-strategy-review`. Role: bounded post-report line/seam reviewer, not blind. Date: 2026-09-26. Starting graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`. Final candidate reviewed at SHA-256 `f297dadc44d0113097d6549650228992b6e969740b75e25451eab3a514cebffb`. This is a same-round strategy review, not theorem promotion or a successor task.

## 1. Result

**Scoped GREEN for the complete strategy reduction (M1)--(M6), including all displayed powers and errors.** No mathematical correction to that reduction is required. The support enlargement from [1,2] to [1,4] is legitimate, the singleton and infinite original tail are retained, and both terms of the accepted distribution inequality are needed for the stated band boundaries.

The downstream exponent `102/325` is correct **when the prospective middle-band estimate holds on a radius window large enough to contain an interior target interval and its persistence neighborhoods**. Concretely, choose the moment window to contain `[T/sqrt(2), sqrt(3) T]` and seek pointwise control for `x` in `[T^2, 2T^2]`. The final candidate now explicitly states this permitted specialization and requires a majorizing weight for the weighted version. I re-read its added paragraph before binding this review to the final hash. No qualification remains missing from the reviewed candidate.

GREEN certifies only the reduction and conditional implication. The signed middle-band estimate (M6) remains unproved, and no accepted graph node or exponent changes.

## 2. Exact reviewed statement and hypotheses

The candidate is `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md` at the hash above. It assumes real `T>=2`, `R` in a fixed interval `I=[cT,CT]` with `0<c<C`, the actual fixed mollifier transform `Psi`, and a fixed smooth nonincreasing `phi` equal to one below 1 and zero above 2. Its multipliers are

\[
v(x)=\phi(x/2)-\phi(x),\qquad
H_N(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})v(n/N)
\cos(2\pi R\sqrt n-3\pi/4).
\]

Here `N=2^j`, `j>=0`, and the finite partition ends at `N_max=2^floor(log_2 T^(3/2))`. The middle sum contains precisely the scales

\[
T^{52/125}<N<T^{99/125}.
\]

The principal reduction is

\[
\int_I |H-H_{\rm mid}|^{12}\,dR\ll_\epsilon T^{29/25+\epsilon},
\tag{R1}
\]

where `H=B_(T,0)` is the complete actual series. The shell formulation uses

\[
L_{N,T}(z)=\int_0^\infty r^{-1}\Psi(r/\sqrt T)v(r^2/N)
\sin(2\pi zr)\,dr,
\quad
S_N(R)=\sum_{m\ge1}r_2(m)m^{-1/4}L_{N,T}(R-\sqrt m).
\]

The open moment of the sum of all middle `S_N` is equivalent, at the stated epsilon-loss level, to the complete milestone. Constants may depend on all fixed test functions, positive window endpoints and epsilon. No uniformity in a varying test function, shrinking radius window or growing moment order is claimed.

## 3. Independent derivation of the seams

### Exact partition, singleton and infinite tail

Monotonicity of `phi` gives `0<=v<=1`; its support lies in `[1,4]`. Its smoothness forces harmless vanishing at the support endpoints. For every integer `n>=2`, the sum telescopes exactly:

\[
\sum_{j=0}^J v(n/2^j)
=\phi(n/2^{J+1})-\phi(n)
=\phi(n/(2N_{\max})).
\]

For `n=1` all block multipliers vanish. Thus that term really must be restored separately, and its amplitude is uniformly bounded. The remaining multiplier for `n>=2` is `1-phi(n/(2N_max))`, bounded between zero and one and supported on `n>2N_max`. Since `N_max<=Z<2N_max`, `Z=T^(3/2)`, the entire residual is contained in `n>Z`. The accepted Schwartz/divisor bound gives its uniform absolute sum `O_K(T^-K)`. There is no last sharp block or unestimated upper collar.

This also covers the case where a dividing power of `T` is itself dyadic. The candidate explicitly assigns equality to the corresponding estimated outer band. Nothing depends on an endpoint avoiding the integers.

### Distribution for a smooth [1,4] block

On this support,

\[
\sum_n|r_2(n)n^{-3/4}\Psi(\sqrt{n/T})v(n/N)|^2
\ll_\eta N^{-1/2+2\eta}.
\]

Split the block into `(N,2N]` and `(2N,4N]`. Apply the accepted finite Gram/covering statement separately to each ambient interval with zero-extended coefficients. A large value of the sum entails a large value of at least one piece at half the threshold; that only changes a fixed constant. Taking a real part also causes no loss beyond inclusion of level sets in the complex modulus level set. Thus (M2) follows with both `V^-2` and `T V^(-136/13)` retained.

The second ambient length can reach `2N_max<=2T^(3/2)`. This uses precisely the fixed-enlargement convention stated immediately after (L4) in the accepted kernel; its proof has unchanged polynomial parameter bounds. It is not an extension to a new power of `T`. Small levels caused by halving a threshold are harmless because the finite covering statement (L6) holds for every positive level. No weighted exponent-pair assertion is used.

### Radial Poisson on the enlarged fixed support

The earlier radial proof scales `r=sqrt(N) t` and only needs `t` in a fixed compact subset of `(0,infinity)`. Replacing `[1,sqrt(2)]` by `[1,2]` changes no power, derivative condition or nonstationarity argument. All derivatives of
`Psi(sqrt(N/T) t) v(t^2)` are uniformly bounded there: when `N>T`, powers arising from differentiation are absorbed by Schwartz decay.

Taking `alpha=1/2` in the earlier range includes every `N<=T^(3/2)` now used. The first Bessel correction has the same decaying shell factor and sums using

\[
\sum_{\sqrt m\asymp T}r_2(m)
(1+\sqrt N|R-\sqrt m|)^{-A}
\ll_\epsilon T^\epsilon(1+T/\sqrt N).
\]

Only after retaining the `+1` does `N<=T^(3/2)<T^2` give `O(T^(1+epsilon)N^-1/2)`. The summed first correction and next Bessel remainder remain `O(T^(-1/2+epsilon)N^-1)`. The separate low-dual, zero-vector and high-dual nonstationary bounds remain summable and arbitrarily small. Hence the complete (M5) and its consequence (M3) extend as stated.

The exact trigonometric product still gives the **positive odd sine at `R-s`**, not a positive cosine kernel; grouping dual vectors still supplies `r_2(m)m^-1/4`. Therefore `L(0)=0` and the exact phase and multiplicity are correct even when `R^2` is an integer. Its rapid decay is uniform after the same rescaling.

### Both layer-cake terms and all threshold arithmetic

For any genuine bound `W>=max(1,sup_I|H_N|)`, layer cake gives

\[
\int_I|H_N|^{12}\ll_\epsilon
T^{1+\epsilon}+T^\epsilon W^{10}
+T^{1+\epsilon}W^{12-136/13}.
\]

The exponent of the last factor is exactly `20/13`. The additive error in (M3) is below a fixed constant after choosing its input epsilon small; it is absorbed in the `max(1,...)` choice of `W` and cannot generate a new band.

For low scales, `W\ll max(1,N^(1/4+eta))`. The nonconstant powers are `N^(5/2)` and `T N^(5/13)`. Each must separately be at most `T^(29/25)`; they impose `N<=T^(58/125)` and `N<=T^(52/125)`, respectively. At the chosen boundary, the two resulting powers are `T^(26/25)` and `T^(29/25)`.

For high scales, `W\ll max(1,T^(1/2+eta)N^-1/2)`. The powers are `T^5N^-5` and `T^(23/13)N^(-10/13)`, imposing `N>=T^(96/125)` and `N>=T^(99/125)`. At the latter boundary their powers are again `26/25` and `29/25`. Beyond `N=T`, the constant lower choice `W=1`, with harmless constants, leaves `O(T^(1+epsilon))`. All four displayed dividing fractions are correct.

Minkowski over `O(log T)` scales costs at most a fixed power of `log T` after taking the twelfth power. The singleton contributes `O(T)`, and the uniform original tail contributes `O_K(T^(1-12K))`. Choose the finite collection of input epsilon/eta parameters below suitable fixed multiples of the desired output epsilon. This proves (R1), with both dyadic and infinite reconstruction complete.

The candidate's warning about using only the outer supremum is correct: `T*(T^(13/125))^12=T^(281/125)`. The distribution estimate, not the supremum alone, is what makes the reduction work.

### Shell reformulation and complete middle baseline

Summing (M5)'s uniform errors over the middle blocks costs at most
`O(T^(-1/2+epsilon) log T)+O_K(T^-K log T)` in supremum, and in fact the `N^-1` factor makes this smaller. Their twelfth moment on `I` is negligible compared with `T^(29/25)`. Thus (M6) is equivalent to the prospective middle moment through physical `L^12` triangle inequalities. A uniform single-block bound is sufficient but genuinely stronger; the candidate correctly does not assume it.

The relation

\[
m-R^2=(\sqrt m-R)(\sqrt m+R)
\]

shows that the effective radial decay scale `N^-1/2` corresponds to squared-radius width `h\asymp T/sqrt(N)` around `R^2\asymp T^2`. The middle endpoints give `T^(151/250)<h<T^(99/125)` up to fixed window constants, or the stated powers `151/500` and `99/250` in `X=T^2`. These are effective decay widths, not compact support assertions about the dual sum. Its far tails remain present and paid.

The accepted complete baseline and (R1) imply the middle baseline by Minkowski, since `10 beta>29/25`. Thus the required net moment saving is exactly `10 beta-29/25`, half as large at the sixth-power `L^2` norm level. There is no cancellation assumption hidden in the subtraction of the outer portion.

### Sharp reconstruction, enlarged window and persistence

Suppose (M6) is proved on `I_+=[T/sqrt(2),sqrt(3) T]`, or on a fixed larger interval. Let `Y=T^2`. The supplied sharp reconstruction is

\[
P(R^2)=\frac{\sqrt R}{\pi}H(R)+O_\epsilon(T^{1/2+\epsilon}).
\]

The leading twelfth power and `dx=2R dR` therefore yield

\[
\int_{Y/2}^{3Y}|P(x)|^{12}dx
\ll T^7 T^{29/25+\epsilon}+T^{8+\epsilon}
\ll Y^{102/25+\epsilon}.
\tag{R2}
\]

For a point `x_0` in `[Y,2Y]`, write `A=|P(x_0)|`. Monotonicity of the inclusive count gives persistence to the right if `P(x_0)>0`, and to the left if `P(x_0)<0`, for distance `A/(2 pi)`, with `|P|>=A/2`. The inherited sublinear pointwise bound ensures this distance is `o(Y)`; consequently the entire one-sided interval lies in `[Y/2,3Y]` for large `Y`. Jumps at integer squared radii cause no exception: the argument uses only monotonicity, with the direction chosen according to the sign.

Thus (R2) dominates a fixed constant times `A^13`, and gives `A\ll Y^(102/325+epsilon)`. Finite small `Y` is absorbed in the constant. This proves the stated conditional downstream exponent on all real endpoints after dyadic coverage.

If the future hypothesis is instead written as a weighted moment, require `w>=1` on `[1/sqrt(2),sqrt(3)]`, or another fixed positive lower bound absorbed into constants. Boundedness and nonnegativity alone, including the possibility `w=0`, do not imply (R2). If only a smaller moment window is available, state pointwise control on a fixed compact interior subwindow, then rescale; do not use persistence across an unestimated boundary. This is the only scope clarification needed.

## 4. First doubtful or unproved step

No unproved step was found in (M1)--(M5) within the supplied accepted kernel and reviewed radial calculation. Their combination is a valid complete reduction. The first new unproved estimate is (M6): cancellation in the full signed arithmetic shell moment, including its cross-block products.

Oddness of `L`, an absolute shell bound, or another application of the same Poisson identity cannot supply it. The candidate makes no such inference. The conditional exponent further requires the enlarged-window or interior-window condition detailed above; this must be retained when freezing any future target.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Smooth partition and singleton | GREEN: exact telescope; `n=1` restored separately; endpoints covered. |
| Coefficient-uniform distribution | GREEN: actual bounded multipliers remain in the coefficient vector; two ambient dyadic intervals; full Gram diagonal retained. |
| Fixed support and length enlargement | GREEN: [1,4] is a fixed annulus; the second ambient length is at most `2T^(3/2)`, covered by the accepted fixed-enlargement convention. |
| Radial Poisson extension | GREEN: uniform amplitude derivatives, actual odd kernel, correct fourth-root dual factor. |
| Both layer-cake terms | GREEN: thresholds `52/125` and `99/125` are the stronger of their respective two constraints. |
| All tails and recombination | GREEN: original infinite residual, zero/low/high dual tails, finite block sum and all formula errors paid. |
| Real endpoints | GREEN: shell count retains `+1`; inclusive jumps allowed; exact lattice radii need no deletion. |
| Signed/absolute distinction | GREEN: positive bounds estimate only the discarded outer bands; the signed middle sum remains the open object. |
| Enlarged-window persistence | GREEN with explicit specialization `I_+` above; arbitrary nonnegative weighted versions alone do not license pointwise inference. |
| Full-proof scope | GREEN: strategy reduction only; `102/325` is conditional and remains above one quarter; no M1/M2 closure. |

No numerical experiment was used. File hashes and section checks are mechanical provenance checks, not mathematical evidence. This is a line audit, not the round's statement-only independent derivation.

## 6. Exact dependencies and hashes

Only the five authorized local files were read for this review:

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md` | `f297dadc44d0113097d6549650228992b6e969740b75e25451eab3a514cebffb` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |
| `rounds/codex-managed/gc-complete-signed-convolution-attack/controls/conductor_radial_poisson_analysis.md` | `b58b66f6231c3a3fe01d5f2851a9136f1aaf9c7f0c095b5997a2e57a66a1366a` |
| `rounds/codex-managed/gc-complete-signed-convolution-attack/reviews/independent_radial_poisson_review.md` | `68429791ce43b0331fbaa76dd1a345fffe7430092a451fab8e304fd9da8f191a` |

The older radial review binds to exactly the radial candidate hash listed here. Its source and graph status are retained. This review imports no new external theorem, consults no sibling report or additional local file, and does not rely on the previously completed source-audit report.

## 7. Recommended state effect

**Retain as independently reviewed strategy evidence; no graph or proof-draft change.** The conductor may use the complete middle-band reduction as the concrete interface selected at Round205 closure, preserving the enlarged-window condition for its conditional pointwise consequence.

The status is scoped GREEN for the reduction and conditional exponent, not for (M6). Only this assigned review was written. The completed source-audit report, candidate derivation, shared state and successor plans were not edited. The review task stops here.
