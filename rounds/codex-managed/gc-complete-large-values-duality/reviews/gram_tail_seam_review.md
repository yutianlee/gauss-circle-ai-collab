# Round204: finite Gram and complete-tail seam review

## 1. Result and verdict

**Campaign:** `gc-complete-large-values-duality`. **Task:** `gram_tail_seam_review`. **Role:** post-report line reviewer, restricted to candidate Sections 4–5. **Generated:** 2026-09-26 01:18:35 UTC. **Method:** 100% analytical review; no mathematical experiments.

**PASS for the revised artifact**, conditional on the correlation estimate (L4) and the elementary coefficient/divisor inputs. Sections 4–5 establish (L1) uniformly in every real lower cutoff `U >= 0` and every level `V >= 1`. The finite argument also permits every block level `v > 0`, which is necessary after the logarithmic pigeonhole step.

The reviewed revised candidate has SHA256

`942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.

The original supplied candidate had SHA256

`5f0c1efcdb230b7ba73206dc960a95a58a6fd03166deb8340f00ed46ab532c6e`.

Its Section 5 omitted an explicit treatment of `n=1`: blocks `(N,2N]` with `N >= 1` cannot contain that integer. I reported this precise local omission to the conductor. The revised candidate explicitly introduces the singleton `{1}`, its kernel, diagonal and energy bound. I inspected that repair; it resolves the omission without changing the stated exponents. No unresolved error was found in the assigned seams.

This verdict neither verifies the external source for (L4) nor assesses Section 6. It is a mathematical seam verdict, not a graph decision or a vote.

## 2. Exact statement and hypotheses

Retain the candidate's parameters `T >= 2`, `1 <= N <= T^(3/2)`, `kappa = 13/55`, and a fixed interval-length constant `C1`. Put `e(x)=exp(2 pi i x)` and

\[
S(R)=\sum_{N<n\leq2N}a_ne(R\sqrt n),\qquad
E=\sum|a_n|^2\leq A N^{-1/2},\qquad A\geq1.
\]

For every nonzero difference in the range `|u| <= C1 T`, assume

\[
|K_N(u)|\leq A\sqrt N\bigl(|u|^\kappa+|u|^{-1}\bigr).
\]

For an arbitrary real interval `I` of length at most `C1 T`, the finite conclusion is

\[
|\{R\in I:|S(R)|>v\}|
\ll A^2\log(2+T\sqrt N)
\left(v^{-2}+T A^{2/\kappa}v^{-q}\right),
\qquad v>0,\qquad q=2+2/\kappa=136/13.
\]

Coefficients may be arbitrary complex numbers and may be zero on any subset of the ambient block. The complete arithmetic consequence assumes a fixed real even Schwartz function `Psi`, the bound `r_2(n) <= 4 d(n) <<_eta n^eta`, and a fixed bounded nonnegative measurable window `w` supported in `[c,C]`, where `0<c<C<infinity`. Measurability is the usual implicit condition in the definition of a window integral. It gives

\[
\int w(R/T)\,1_{|B_{T,U}(R)|>V}\,dR
\ll_\epsilon T^\epsilon\left(V^{-2}+TV^{-q}\right)
\]

for every real `U >= 0`, `V >= 1` and `epsilon > 0`. Constants may depend on the fixed window, epsilon, and fixed Schwartz seminorms, but not on `T,U,V`.

## 3. Derivation and line audit

**Finite alignment and the full diagonal (candidate lines 144–179).** Let

\[
m=\#\{n\in\mathbb Z:N<n\leq2N\}.
\]

For real `N >= 1`, `m <= N+1 <= 2N`. Given `J >= 1` selected large-value points, choose unit numbers `z_j` so that `z_j S(R_j)=|S(R_j)|`. The candidate's Cauchy inequality follows directly from

\[
Jv<\sum_j |S(R_j)|=\sum_n a_n\sum_jz_je(R_j\sqrt n).
\]

The expanded square has exactly `Jm` diagonal terms, so division by `J` leaves the diagonal contribution `Em <= 2A sqrt(N)`. It is present for `J=1`; the singular off-diagonal expression is never applied at `u=0`.

For `delta=N^(-1/2)` and points in an interval of length at most `h`, ordering the neighbors of a fixed point gives

\[
\sum_{k\ne j}|R_j-R_k|^{-1}
\leq 2\delta^{-1}H_{J-1},\qquad
\sum_{k\ne j}|R_j-R_k|^\kappa\leq(J-1)h^\kappa.
\]

Consequently the slightly more explicit finite inequality is

\[
Jv^2\leq 2A\sqrt N
  +A^2\left((J-1)h^\kappa+2\delta^{-1}H_{J-1}\right).
\]

This proves (L7), including its powers of `A`. It also proves the `J=1` case directly. The coefficient phases have no effect on this estimate.

**Localization and the complete number of intervals (lines 156–159, 181–197).** With the candidate's

\[
h=\left(\frac{v^2}{4C_2A^2}\right)^{1/\kappa},
\]

the `A^2 J h^kappa` contribution is absorbed on the left after choosing the fixed `C2` sufficiently large. Every actual sample difference remains at most `|I| <= C1 T`, even when `h` is greater than that range. Thus an oversized localization length does not require an extension of the assumed correlation range.

For a local interval one has `J <= 1+C1 T/delta`. Hence

\[
Jv^2\ll A^2\sqrt N\log(2+T\sqrt N).
\]

For nondegenerate `I`, the required number of pieces is `ceil(|I|/h)`, which is at most `1+C1 T/h`. It is exactly one when `h >= |I|`; no fractional piece is substituted. Since

\[
h^{-1}=(4C_2)^{1/\kappa}A^{2/\kappa}v^{-2/\kappa},
\]

the two final coefficient factors are exactly `A^2` and `A^(2+2/kappa)=A^q`. There is no hidden additional power of `A`.

**Finite covering of the real level set (lines 161–166, 185–189).** A bounded interval contains at most `1+|I|/delta` mutually delta-separated points. Start from any point of the level set and add a point whenever possible; this process must terminate after finitely many additions. At termination every level-set point is within distance less than delta of a selected point. This proves the required covering for open, closed or half-open intervals and for the strict level inequality, without compactness of the level set.

Its measure is at most `2 delta J`. Multiplying the last displayed bound for `J` by `2 delta` gives the asserted local bound. Summing over the full number of local pieces gives (L6). Empty level sets and degenerate intervals have zero measure. If `h < delta`, there is at most one selected point per piece, and the same diagonal and covering argument remains valid. There is no claim that large values persist throughout any covering neighborhood.

**Infinite upper tail (lines 201–211).** Choose fixed `eta > 0` and a Schwartz decay order `L` with `L/2 > 1/4+eta`. Then, with `Z=T^(3/2)`,

\[
\begin{aligned}
\sum_{n>Z}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
&\ll_{\eta,L}T^{L/2}\sum_{n>Z}n^{-3/4+\eta-L/2}\\
&\ll_{\eta,L}T^{L/2}Z^{1/4+\eta-L/2}\\
&=T^{3/8+3\eta/2-L/4}.
\end{aligned}
\]

Taking `L > 4K+3/2+6eta` gives (L9) with room to spare. This is an absolute bound, uniform in `R`. Restricting further to `n>U` only decreases it. In particular, if `U>=Z`, the complete series is smaller than `1/2` for sufficiently large `T` after a fixed choice of `K`, and all levels `V>=1` are empty. For each fixed `T`, the same absolute convergence makes `B` continuous, so the level sets used in the proof are measurable.

**Singleton and partial blocks (revised lines 212–225).** The revised singleton has

\[
a_1=1_{1>U}\,4\Psi(T^{-1/2}),\qquad K(u)=e(u),\qquad K(0)=1.
\]

Its energy is bounded by the fixed number `16||Psi||_infinity^2`. For every `u!=0`, `|u|^kappa+|u|^(-1)>=1`: the first term is at least one when `|u|>=1`, and the second when `|u|<=1`. With `N=1` and a fixed enlargement of `A`, all ingredients of the finite proof hold. That proof uses only the finite index set, its diagonal count, its coefficient energy and its correlation bound; its conclusion therefore applies verbatim to `{1}`. This is an explicit extension by the proved argument, not a claim that `{1}` equals `(1,2]`.

The remaining integers are covered by `(2^j,2^(j+1)]`, starting at `j=0`, with coefficients set to zero for `n<=U` and `n>Z`. Each ambient `N=2^j` can be chosen at most `Z`. Zero extension preserves the full unweighted correlation kernel and can only decrease coefficient energy. There is no integrality assumption on `U` or `Z`. If the lower and upper cutoffs lie in the same ambient block, both restrictions are implemented by the same zeroing operation.

For every nonsingleton block,

\[
\sum|a_n|^2\ll_\eta
\sum_{N<n\leq2N}n^{-3/2+2\eta}
\ll_\eta N^{-1/2+2\eta}
\leq T^{3\eta}N^{-1/2}
\]

up to a fixed constant. The singleton obeys the same final bound with `N=1`. No weighted exponential-sum theorem is used.

**Cosines, arbitrary levels and finite recombination (lines 227–237).** Since the arithmetic coefficients are real, each cosine block is precisely `Re(e(-3/8)S(R))`; its absolute value is at most `|S(R)|`. This accounts for both exponential phases without making two unrelated estimates.

Let `b <= C log T` be the number of blocks, including the singleton. For sufficiently large `T`, arrange the absolute remainder to be at most `1/2`. At any level `V>=1`, `|B(R)|>V` implies

\[
\sum_{j=1}^{b}|S_j(R)|>V-1/2\geq V/2.
\]

Thus at least one `|S_j(R)|` exceeds `V/(2b)`. This block level can be less than one; Section 4 is expressly valid for all positive `v`. The union bound is therefore legitimate for the entire stated range of `V`, including arbitrarily large `V`.

Here is explicit epsilon bookkeeping. Fix the requested output `epsilon>0`, put `sigma=epsilon/(2q)`, use the input correlation estimate with exponent `sigma`, and choose the divisor exponent `eta=sigma/3`. One common value

\[
A=C_{\sigma,\Psi}T^\sigma\geq1
\]

then bounds every block energy and correlation. Since `N<=T^(3/2)`, the logarithm in (L6) is `O(log T)`. Summing (L6) at the block threshold yields

\[
\ll_{\sigma,\Psi}
T^{2\sigma}(\log T)^4V^{-2}
+T^{1+q\sigma}(\log T)^{q+2}V^{-q}.
\]

Both fixed logarithmic powers are `O_epsilon(T^(epsilon/2))`. The second power is exactly `1+epsilon`; the first is at most `epsilon`, because `2sigma+epsilon/2=epsilon/q+epsilon/2<=epsilon`. This proves the claimed epsilon uniformity without an implicit restriction on `V` or `U`.

Finally multiply by `||w||_infinity` on `[cT,CT]`. For `2<=T<=T0`, absolute summability gives a uniform bound `|B_{T,U}(R)|<=M`, independent of `U` and `R`. The distribution is zero for `V>=M`. For `1<=V<M`, its trivial bound `O(T)` is at most `O(max(1,M^q) T V^(-q))`. Enlarging the fixed constant therefore covers the entire bounded `T` range.

## 4. First doubtful or unproved step

The first omission in the original assigned sections was the instruction to partition **all** integers `1<=n<=Z` into the previously defined dyadic blocks. With their stipulated `N>=1`, they omit `n=1`. The revised lines 212–218 explicitly repair this, and the verification is given above.

No doubtful or unproved step remains within Sections 4–5 of the revised artifact under their stated inputs. The first input not proved by this review is the uniform correlation estimate (L4). Its source validity, phase specialization and exponent-pair interpolation belong to another seam. The validity of the subsequent pointwise and moment consequences is also outside this review.

The standalone finite statement inherits `T>=2`, `N>=1`, positive `kappa`, and the kernel difference range from the preceding candidate definitions. Reading Section 4 in isolation without those inherited hypotheses would require restating them; it does not create a gap in the complete candidate.

## 5. Required controls and outcomes

- **Diagonal and one selected point — pass.** With integer `N` and aligned coefficients `a_n=N^(-3/4)e(-R0 sqrt(n))`, the energy is `N^(-1/2)` and `|S(R0)|^2=sqrt(N)`. The exact diagonal inequality for `J=1`, `A=1` is equality. Deleting that contribution would fail this admissible example.
- **One localized interval — pass.** When `h>=|I|`, the partition has one piece and yields the `A^2 v^(-2)` contribution. It is never replaced by the fraction `|I|/h`. The aligned peak has width comparable to `N^(-1/2)` and height comparable to `N^(1/4)`, so a `v^(-2)` term has the correct scale for that control.
- **Very short pieces, empty sets, and real sample points — pass.** Pieces shorter than delta contain at most one selected point. Empty sample sets are handled before division by `J`. Greedy finite covering applies to arbitrary real positions and endpoint conventions. No persistence assertion is required.
- **Singleton `n=1` — pass after repair.** Its exact kernel has modulus one, its diagonal is one, and its uniformly bounded energy fits the proof with `N=1`. The original partition omission is resolved.
- **Arbitrary lower cutoff and partial final blocks — pass.** Real `U`, `U=0`, `U` at an integer, both cutoffs in one block, `U` close to `Z`, and `U>=Z` are all covered by zero extension or the absolute tail estimate.
- **Upper infinite tail — pass.** The exponent `3/8+3eta/2-L/4` can be made less than any prescribed `-K` by a fixed Schwartz order. The estimate is uniform in `R` and survives every lower cutoff.
- **Small block levels and arbitrarily large global levels — pass.** All `v>0` are allowed in (L6). Hence a global level `V=1` causes no unsupported lower-level application after division by `O(log T)`. The same union argument is valid without an upper restriction on `V`.
- **Epsilon budget and bounded `T` — pass.** The explicit budget in Section 3 absorbs `A^q` and all recombination logarithms. A uniformly bounded absolute sum covers bounded `T` independently of `U`.

These are exact analytical controls. No numerical experiment or empirical asymptotic check was performed.

## 6. Dependencies and exact artifacts used

Only the following files were read:

1. `protocol.md`, SHA256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, initially SHA256 `5f0c1efcdb230b7ba73206dc960a95a58a6fd03166deb8340f00ed46ab532c6e`, then the conductor's repaired version SHA256 `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`. All candidate line references in this report refer to the repaired version.
3. `rounds/codex-managed/gc-complete-large-values-duality/reports/blind_gram_covering_audit.md`, SHA256 `340eed3ddd8bfb329a77d8583bdb32e00bf45cbbbfa58f4c322f0c1c0266db16`.

The completed statement-only report was read before this line audit. Its spacing `A sqrt(N)/m` and sharper implicit logarithm differ from the candidate's choice `N^(-1/2)` and ambient logarithm; both are valid. The present report directly rechecks the candidate's actual choices rather than treating the prior verdict as evidence by agreement.

The candidate prints starting graph SHA256 `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`. That value is recorded solely as supplied metadata; the graph and active campaign were not accessed under the conductor's isolation restriction. No other report, strategy file, source card, web source, or shared state was consulted.

Mathematical dependencies are the assumed (L4), the elementary divisor estimate, Schwartz decay, finite Cauchy–Schwarz, ordered harmonic sums, finite separated covering, elementary integral comparison, and a finite union bound. Source and moment seams remain external to this report. File hashes are artifact verification, not mathematical experiments.

The only written artifact is this assigned review. I did not edit the candidate, graph, proof draft, validation matrix, synthesis, or State Patch.

## 7. Recommended state effect

**Retain the revised candidate and mark the Sections 4–5 seam passed.** The original local `n=1` omission has been repaired in the exact revised hash above. Conditional on acceptance of (L4) and completion of the other required reviews, the derivation of (L1) has no remaining obstruction identified by this audit.

There is **no direct proof-state promotion by this report**. The arithmetic stronger distribution target, its associated pointwise objective, and other obligations receive no automatic state effect. The conductor owns any eventual validated State Patch. This task stops at this report and does not open or design another round.
