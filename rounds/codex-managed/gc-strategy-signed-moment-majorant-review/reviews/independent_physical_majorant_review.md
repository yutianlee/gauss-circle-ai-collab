# Independent seam review: physical twelfth-moment absolute majorant

## 1. Result

**GREEN.** The reviewed kernel proves the claimed nonzero-frequency lower bound for the termwise absolute majorant with the actual circle coefficients. The stated qualification at general order, the infinite-series passage, and the continuum control are valid. It proves no lower bound for the complete signed displaced moment.

- Round: 202.
- Campaign: `gc-strategy-signed-moment-majorant-review`.
- Task/role: `physical_majorant_review`; independent seam reviewer, not claimant or statement-only rederiver.
- Generated: 2026-09-23T20:52:30+08:00.
- Starting graph SHA-256, copied from the reviewed kernel without opening the graph: `682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c`.
- Exact reviewed kernel SHA-256: `23e1185f00300bde4c48ee3add34741c767cc9337c79b67a744a8cc0f94c315b`.
- Isolation: only `protocol.md`, the named kernel, and the conductor-supplied accepted exact-resonance statement were used. No sibling or blind report, graph, strategy file, source proof, or numerical experiment was consulted.

## 2. Exact statement and hypotheses

Let `Psi` be real, even, Schwartz, with `Psi(0)=1`, and let `w` be nonnegative, nonzero, smooth, and compactly supported in `(0,infinity)`. With `r_2(n)` counting ordered signed representations, set

`a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T))`, for real `T>=2`.

There are constants `0<a<b`, `h>0`, and `c>0`, depending only on the fixed data, such that for all sufficiently large real `T`, the coefficients on `I_T=[aT,bT] intersect N` are nonnegative, and

`T sum_{n_1,...,n_12 in I_T; 0<|Delta|<=h/T} (product_j a_{n_j}(T)) Re(w-hat(-T Delta)) >= c T^(5/2)`,

where `Delta=sum_{j=1}^6 sqrt(n_j)-sum_{j=7}^{12} sqrt(n_j)` and `w-hat(xi)=integral w(u)e(-u xi)du`.

All tuples are ordered and allow repetition. The exact frequencies are deleted. The all-sign infinite termwise absolute majorant with factor `T/2^12` is consequently at least a positive constant times `T^(5/2)`. For any fixed `eta<3/4`, this contradicts a bound `O_epsilon(T^(1+2eta+epsilon))` asserted for every positive `epsilon`.

The input about exact resonances is the accepted statement for every fixed integer `j>=2`: if `b_n>=0`, `A_d=sum_{s>=1} b_{ds^2}` for squarefree `d`, and `S=sum_d A_d^2<infinity`, then the full ordered exact mass over all `2^j` sign vectors is at most `2^j B_j S^(j/2)`, where `B_j` counts partitions with no singleton blocks. In particular `b_n<=C tau(n)n^(-3/4)` implies `S<=C^2 zeta(3/2)^10`, uniformly under all finite or unequal cutoffs and for the infinite sequence. This statement includes nonpairing exact resonances.

## 3. Proof and seam audit

**Physical mass and real endpoints.** Continuity and `Psi(0)=1` allow a fixed positive interval `[a,b]` on which `Psi(sqrt(u))>=1/2`. The elementary disk covering with unit squares gives `N(R)=pi R^2+O(R+1)` for every real `R`, including the boundary convention. Therefore

`sum_{aT<n<=bT} r_2(n)=N(sqrt(bT))-N(sqrt(aT))=pi(b-a)T+O(sqrt(T)+1)`.

The origin cancels in this difference. An integer lower endpoint is excluded by the difference exactly as written; the closed band in the theorem can only add a nonnegative atom. For all sufficiently large real `T`, one may take

`M_T=sum_{n in I_T}a_n(T) >= alpha T^(1/4)`, with `alpha=pi(b-a)b^(-3/4)/4>0`.

Thus the mass uses the actual `r_2(n)` and actual cutoff values, with no assumed positive density of represented integers or pointwise lower bound for their representation counts.

**Fourier positivity.** Put `W_0=integral w>0`. Continuity gives fixed `h>0` with `Re(w-hat(xi))>=W_0/2` on `|xi|<=h`. No Fourier positivity away from zero is used.

**Ordered weighted counting and exponents.** The six-root sums occupy an interval of length `L sqrt(T)`, where `L=6(sqrt(b)-sqrt(a))`. Bins of length `h/T`, including a possible terminal endpoint bin, number at most `(L/h)T^(3/2)+2`. For `T>=2`, this is at most `C_J T^(3/2)` with `C_J=L/h+1`. The nonnegative total weight of the ordered six-tuples is `M_T^6`. Weighted Cauchy therefore gives close-pair mass at least

`M_T^12/J >= beta T^(3/2)`, where `beta=alpha^12/C_J>0`.

A bin pair is exactly an ordered twelve-tuple. There is no factorial or permutation correction. Same-bin differences satisfy the required inequality, and the extra cross-bin terms are nonnegative.

**Exact-frequency deletion.** The two-square identity gives `r_2(n)<=4 tau(n)`. Thus the fixed positive envelope `b_n=4 C_Psi tau(n)n^(-3/4)`, where `C_Psi=sup |Psi|`, dominates `|a_n(T)|` simultaneously for every `T`. The accepted statement at `j=12` bounds the entire exact mass by a finite constant `E_12` independent of `T`, and hence bounds this band and this one balanced sign pattern. It covers every exact resonance, not merely diagonal permutations. The remaining close-pair mass is at least `beta T^(3/2)-E_12`, and is at least `(beta/2)T^(3/2)` once `T` is large enough. Multiplying by `T W_0/2` proves the claimed lower bound, for example with `c=beta W_0/4`.

**All-sign majorant and exponent obstruction.** For the retained balanced sign pattern, the band coefficients are nonnegative and `|w-hat(-T Delta)|>=Re(w-hat(-T Delta))`. Consequently this one pattern alone contributes at least `2^(-12)cT^(5/2)` to the defined all-sign majorant. The balanced cosine phase is one for the common circle cosine phase because the sum of the signs is zero; that observation is also unnecessary to the absolute-value lower bound. If `0<epsilon<3/2-2eta`, then `1+2eta+epsilon<5/2`, proving the stated contradiction with a uniform asymptotic upper bound.

**Infinite sequence.** Schwartz decay gives, at each fixed `T`, an arbitrarily strong negative power of `n` in `Psi(sqrt(n/T))`. Together with the divisor envelope, this makes `sum_n |a_n(T)|` finite. Since `|w-hat|<=||w||_1`, the full twelve-fold absolute sum is bounded by `||w||_1(sum_n |a_n(T)|)^12` times its finite sign and prefactor constants. The moment expansion and its integration over the fixed-`T` compact window are justified by absolute convergence. No uniform-in-`T` summability assertion is needed here.

**General order.** At order `2k`, the total weighted close-pair mass before the outside factor `T` is at least a constant times `M_T^(2k)T^(-3/2)`, hence a constant times `T^((k-3)/2)`. The accepted exact lemma at `j=2k` removes at most a fixed `E_(2k)`. Multiplication by the Fourier lower bound and by `T` yields precisely `c_k T^((k-1)/2)-C_k T`. For fixed `k>=4` the first exponent exceeds one; for `k=2,3` this argument supplies no guaranteed positive asymptotic remainder. The kernel states this limitation correctly.

## 4. First doubtful or unproved step

There is no unresolved mathematical step in the reviewed lower bound, conditional on the explicitly accepted exact-resonance statement. That accepted input is the only substantive imported lemma; its proof was outside this review's assigned context.

The first unproved downstream step remains a coefficient-preserving estimate for the complete signed displaced sum, or an appropriate complete signed cutoff-tail estimate. Discarding the complementary Fourier terms would not supply it. The kernel explicitly excludes this inference.

## 5. Required controls and outcomes

**Continuum cancellation control: PASS, analytically.** Write `A_f=integral f>0` for a fixed nonnegative nonzero `f` supported compactly inside `(a,b)`. For

`F_T(R)=T^(1/4) integral f(u)e(R sqrt(T) sqrt(u))du`,

the phase derivative in `u` is bounded away from zero up to the factor `R sqrt(T)` on this support. Repeated integration by parts has no boundary terms and proves `|F_T(R)|<=C_A T^(1/4)|R sqrt(T)|^(-A)`. On the support of `w(R/T)`, `R` is between two fixed positive multiples of `T`. Thus

`integral w(R/T)|F_T(R)|^12 dR = O_A(T^(4-18A))`,

which is smaller than any prescribed negative power after choosing `A` sufficiently large.

Choose a fixed `c_*>0` so small that `2pi c_* sqrt(b)<=pi/3`. If `|R|<=c_*/sqrt(T)`, the real part of the oscillatory factor is at least `1/2`; therefore `(A_f/2)T^(1/4)<=|F_T(R)|<=A_f T^(1/4)`. The twelfth moment over that origin interval is consequently comparable to `T^3 T^(-1/2)=T^(5/2)`, as claimed.

The frequency measure obtained by pushing `T^(1/4)f(u)du` to `sqrt(Tu)` has the same total-mass and support-length scalings as the discrete band measure. The weighted bin argument therefore gives the same positive close-difference subsum. Exact equality has measure zero: after fixing the other eleven variables, the twelfth variable solves a strictly monotone equation at at most one point. Hence the continuum control really combines a positive nonzero close-difference contribution of order `T^(5/2)` with a rapidly decreasing complete displaced moment. Complementary signed Fourier contributions cancel it. This is a control for the inference, not an approximation to the arithmetic sequence.

**Endpoint and multiplicity control: PASS.** The interval difference uses the exact open/closed endpoints, the terminal bin assigns every tuple once, and the weighted pairing uses ordered tuples throughout. Repeated indices are permitted both in the lower count and in the exact upper bound.

**Low-order control: PASS.** Exact-frequency removal costs `O(T)` after the outside factor. The general-order lower bound is therefore inconclusive at `k=2,3`; it cannot be promoted to a spurious positive offdiagonal lower bound there. No claim about the second-moment signed theorem follows from the displayed argument.

No numerical experiment was run. All controls are analytical, so they do not serve as numerical certification of an asymptotic theorem.

## 6. Dependencies and exact artifacts used

1. `protocol.md`: research authority, isolation, reporting, and promotion rules.
2. `proofs/kernels/gc_physical_twelfth_moment_absolute_majorant_obstruction.md`: exact reviewed bytes, SHA-256 `23e1185f00300bde4c48ee3add34741c767cc9337c79b67a744a8cc0f94c315b`.
3. The conductor's statement-only message supplying accepted `GC-weighted-square-root-exact-resonance-mass` for every fixed `j>=2`, including the divisor envelope and uniform finite/infinite cutoff forms, reproduced in Section 2. Its proof and source artifact were not opened.
4. Elementary facts explicitly used in the kernel: disk area comparison, the two-square identity and divisor bound, Cauchy--Schwarz, Fourier continuity, Schwartz decay, and integration by parts. No external source was introduced.

The kernel's statement that other Round202 review artifacts are recorded is provenance outside this isolated audit, not a mathematical dependency checked here. This report does not certify the existence or content of another review.

## 7. Recommended state effect

**Promote the narrow obstruction, subject to the conductor's complete validation gates.** Record that actual circle coefficients force a nonzero-frequency termwise absolute twelfth-moment Fourier majorant of order at least `T^(5/2)` on a fixed positive cutoff band, and therefore preclude the specified smaller majorant target when `eta<3/4`.

Retain every signed moment, pointwise, M1, and M2 obligation in its existing state. Neither the positive selected subsum nor the continuum diagnostic is a lower bound for the full arithmetic signed displaced moment. This reviewer has made no graph, draft, validation-matrix, synthesis, or kernel edit.
