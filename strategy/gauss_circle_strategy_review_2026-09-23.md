# Gauss circle project: progress review and full-proof strategy

Date: 23 September 2026

## Scope and status

The request refers to completed Round 200. The live repository checked for this review still reports **Round 199 complete**. The reviewed main commit is `7a4999a5df90bc2a9f6ea4f84fae3a4aa1b99c39`, merged on 23 September 2026. No Round-200 reasoning was located in the inspected branches, open pull requests, or available file searches. This document therefore evaluates the published state through Round 199, not an unseen Round-200 increment.

This is a strategy memorandum, not a State Patch. Repository statements described as accepted have not all been independently reproved in this review. The Round-199 finite allocation algebra was inspected; the complete historical dependency graph and computational validation suite were not rerun.

Use the squared-radius normalization

$$
P(X)=\#\{(m,n)\in\mathbb Z^2:m^2+n^2\le X\}-\pi X.
$$

The target is $P(X)\ll_\varepsilon X^{1/4+\varepsilon}$ for every positive $\varepsilon$.

## 1. Evaluation

The project has made genuine progress in exact reductions, preservation of coefficients, identification of endpoint and mask errors, and local estimates. It has not yet achieved a new global pointwise exponent. Its accepted internal exponent remains $1/3$; its accepted external benchmark is the repaired Li–Yang application with

$$
\theta_{\mathrm{LY}}=\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots.
$$

The principal strategic risk is now fragmentation: repeated subdivision of a signed sum can produce many correct local statements without reducing the hardest remaining power loss. Counting completed rounds, accepted kernels, or increasingly specific failures is not a useful measure of proximity to the target.

### Recent positive and negative results

Round 195 obtains the required outer $L^2X^\varepsilon$ bound for all $\kappa\ge D_L$ packets and, for $\kappa<D_L$, those satisfying

$$
\min(Y,D_L)\le H_B\mathfrak m\kappa.
$$

Round 197 obtains that bound on the exact common-cell lower-swap sector. It does not assert that this sector has positive density or carries a specified portion of the original sum.

Rounds 196 and 199 rule out specified cancellation mechanisms. They do not prove that the actual desired estimate is false. In particular, an upper bound of size $D_LL^2X^\varepsilon$ is not a lower bound of that size.

The remaining Round-198/199 $P_2$ domain is

$$
\{\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}
\cap(P_{\partial\mathrm{lit}}\dot\cup P_{\mathrm{sf}}\dot\cup P_{\mathrm{gf}}).
$$

Even its complete solution would leave the $P_1$ domain, other original-$t=1$ terms, original-$t\ge2$ small-$G$ terms, and large-$G$ near-resonant terms in hard M1. Smooth M1 is independent and still has an $X^{1/12}$ deficit at its first critical bound. M2 still requires its TOP, BAL, and UNBAL components. The total-M1 GAR alternative does not eliminate M2.

**Recommendation:** preserve all accepted results, but redirect the next analytic campaigns toward a complete remaining signed contribution and an inequality with a quantified net power saving.

## 2. What Round 199 says about the decomposition

In the notation of its kernel, three allocation states contribute

$$
\Sigma=u_0\overline{\ell_0}+t u_1\overline{\ell_0}
+tp u_1\overline{\ell_1},\qquad p,t\in\{-1,1\}.
$$

Exactly,

$$
\Sigma=(u_0+t u_1)\overline{(\ell_0+p\ell_1)}
-pu_0\overline{\ell_1}.
$$

On the aligned character-reversing face, $p=-1$, so the omitted term has coefficient $+1$. The fourth allocation needed to complete the product changes the gcd from $A$ to $Aq$ and lies in the lower-first-failure region $P_1$. Thus the chosen $P_2$ partition is not closed under the cancellation being attempted.

This motivates testing the original signed contribution containing both $P_1$ and $P_2$, before packetwise norms. It does **not** imply that the completed product is small: its endpoint difference may retain a unit jump.

For a common zero-extended domain, a partition of unity $\sum_jM_j=I$, and one genuine transport $U$, the identity

$$
\sum_j[M_j,U]=0
$$

shows why boundary terms introduced only by a partition should be recombined before estimation. This identity supplies no analytic saving by itself. It is inapplicable when different sectors use incompatible transports or projectors. Every change of gcd, phase, support, endpoint, orientation, and multiplicity must be accounted for.

The next coupled-source test should end with either an actual complete-source inequality or an explicit statement of the analytic estimate still missing. Do not replace the current three-way complement with an indefinite sequence of smaller unestimated complements.

## 3. A useful elementary lemma: moving interval masks cost a logarithm

This lemma is a reusable consequence of a bilinear operator bound. No novelty claim is made.

### Lemma

Let $K(m,n)$ be a complex matrix on a finite row set $I$ and the ordered columns $1,\ldots,N$. Suppose that, for all complex vectors $a,b$,

$$
\left|\sum_{m\in I}\sum_{n=1}^N a_m b_n K(m,n)\right|
\le B\|a\|_2\|b\|_2.
$$

For any function $f:I\to\{0,1,\ldots,N\}$, one has

$$
\left|\sum_m\sum_{n\le f(m)}a_m b_n K(m,n)\right|
\le (1+\lceil\log_2N\rceil)B\|a\|_2\|b\|_2.
$$

A row-dependent interval costs at most twice this bound. A union of at most $J$ row-dependent intervals costs at most $2J$ times this bound.

### Proof

Pad the column interval with zeros to length a power of two. Decompose every prefix $[1,f(m)]$ into its canonical disjoint dyadic intervals. There is at most one interval at each dyadic scale in the decomposition of a given prefix.

For a dyadic interval $Q$, let $E_Q$ be the set of rows whose prefix decomposition selects $Q$. The masked matrix is the sum of its restrictions to rectangles $E_Q\times Q$. At a fixed scale, the sets $E_Q$ are pairwise disjoint, and the intervals $Q$ are pairwise disjoint. The assumed bilinear inequality and Cauchy–Schwarz therefore give

$$
\begin{aligned}
\sum_{Q\text{ at one scale}}
\left|\sum_{m\in E_Q,n\in Q}a_mb_nK(m,n)\right|
&\le B\sum_Q\|a1_{E_Q}\|_2\|b1_Q\|_2\\
&\le B\|a\|_2\|b\|_2.
\end{aligned}
$$

Sum over the dyadic scales. An interval is the difference of two prefixes. For a union of intervals, sum the interval estimates. This proves the lemma.

### Consequences and limitations

The threshold $f(m)$ need not be monotone or independent of the row. Consequently, a moving sharp boundary alone is not a sufficient reason to reject an $\ell^2$ bilinear theorem.

This does not treat arbitrary two-variable phases or arbitrary masks with a power-sized number of components. It does not establish the initial bound $B$. In the project, one must first isolate the correct arithmetic kernel and determine which remaining masks have interval sections in its summation variable.

The relevant practical question is:

> Can the complete actual phase and amplitude be separated with subpower cost, leaving only a bounded or subpower number of row-interval masks?

That is more precise than asking whether every moving selector is smooth.

## 4. Current bilinear and spectral methods: an exact import test

Blomer–Pascadi, arXiv:2607.24311v1, Theorem 1.1, gives in the critical interval-length range at most $\sqrt c$

$$
\left|\sum_{\substack{m\in I,n\in J\\(m,n,c)=1}}
\alpha_m\beta_n S(am,n;c)\right|
\ll \|\alpha\|_2\|\beta\|_2c^{1-1/32+o(1)},
$$

where $a$ is a unit modulo $c$ and $S$ is the unnormalized Kloosterman sum. This applies to all moduli. The coprimality condition cannot generally be deleted for arbitrary intervals. Its unequal-length alternatives must be used for genuinely unbalanced sums.

The preceding elementary lemma extends this estimate to row-interval masks with logarithmic loss, provided the remaining coefficients are still a product. This is a conditional application interface, not a verified import into M1 or M2.

For an actual mixed amplitude $A_{mn}$, define

$$
\|A\|_\pi=
\inf_{A_{mn}=\sum_j u_j(m)v_j(n)}
\sum_j\|u_j\|_2\|v_j\|_2.
$$

Any product-vector estimate extends by the triangle inequality with $\|A\|_\pi$ in place of the product norm. This is useful only when that norm is controlled at the correct normalization. A decomposition into many products is not automatically cheap.

For each import, record: the exact kernel; modulus and unit conditions; variable lengths; physical coefficients; tensor or product norm; number of interval components; completion costs; every discarded or exceptional term; and the location of the outer absolute value.

If $c\asymp X^\gamma$, the theorem saves $c^{-\delta}$, and all additional costs relative to the old bound total $X^a$, the net saving is $X^{-(\gamma\delta-a)}$. It is this exponent, not $\delta$ alone, that must be compared with the open deficit.

Pascadi's non-abelian amplification, arXiv:2511.08445v2, supplies a stronger $c^{-1/12}$ saving for products of two comparably sized primes in the critical range. It should be tested on compatible factorization ranges, not substituted for an all-moduli result. Milićević–Qin–Wu, arXiv:2511.07550, offers another all-moduli bilinear framework, including unequal-length ranges.

For M2 UNBAL, the first task is to preserve the full vector of coefficients rather than reduce to a scalar inverse-residue bound already known to lose a boundary factor.

## 5. Algebraic geometry and prime-power analysis

Fouvry–Kowalski–Michel–Sawin, *Bilinear forms with trace functions*, arXiv:2511.09459v3, provides a relevant prime-field framework under geometric monodromy hypotheses.

Its useful role here is to identify the exact exceptional parameter loci where a completed correlation degenerates. The project should distinguish generic geometric cancellation from aligned, reducible, repeated-root, or prime-power configurations. The exceptional part needs its own arithmetic estimate; an upper bound for its size is not enough if that bound exhausts the desired power saving.

For every proposed trace-function application, specify the sheaf or trace function, conductor, twists, geometric symmetries, exceptional locus, and reduction from the actual weights. For composite moduli, identify separately the squarefree, prime-power, and 2-adic issues. Existing aligned controls must survive as test cases.

Milićević–Robinson–Shupe, arXiv:2608.21346, was already included in the repository's August literature audit. Its invariant-weight hypotheses cannot be enlarged without proof. Repeating the paper's name is not a new mechanism.

## 6. Fourier analysis, decoupling, and uniform asymptotics

The Li–Yang argument combines a first-spacing estimate with Huxley's second-spacing analysis. Guth–Maldague's amplitude-dependent cone estimates and small-cap decoupling give a useful model for preserving amplitude information.

The project should test a broad–narrow decomposition of the actual phase, with a quantified transversality parameter. Transverse packets may be treated by an applicable decoupling estimate; aligned rational packets must retain their arithmetic coefficients. No saving from the broad part can be credited to the narrow part without a separate argument.

Uniform asymptotics should preserve the phase and endpoint information needed by these estimates. A stationary point approaching an endpoint generally calls for a uniform endpoint/stationary-point treatment; Airy approximations are appropriate only for the corresponding coalescing-critical-point geometry. The normal form must be derived from the actual phase.

A Fourier transform, theta functional equation, or stationary-phase substitution is not itself a gain. The deliverable must be an inequality whose restored power is smaller.

### A whole-discrepancy Poisson–Bessel formulation

Here is a self-contained normalization check and alternative analytic interface. Let $\rho\ge0$ be a fixed smooth radial function supported in the unit disk, with integral one. Use the Fourier transform $\widehat f(\xi)=\int f(x)e^{-2\pi i x\cdot\xi}\,dx$, and put $\Psi(s)=\widehat\rho(se_1)$.

For radius $R\ge2$, choose $\delta=R^{-1/2}$ and define

$$
S_\delta(R)=\sum_{m\in\mathbb Z^2}(1_{B_R}*\rho_\delta)(m).
$$

The difference from the sharp lattice count is supported in the annulus of width $\delta$. Since $r_2(n)\ll_\varepsilon n^\varepsilon$, its contribution is

$$
|N(R)-S_\delta(R)|\ll_\varepsilon (R\delta+1)R^\varepsilon
\ll_\varepsilon R^{1/2+\varepsilon}.
$$

Poisson summation gives the absolutely convergent identity

$$
S_\delta(R)-\pi R^2=
R\sum_{n\ge1}\frac{r_2(n)}{\sqrt n}
\Psi(\delta\sqrt n)J_1(2\pi R\sqrt n).
$$

Using the standard large-positive-argument expansion of $J_1$, whose summed remainder is $O(R^{-1/2})$, yields

$$
N(R)-\pi R^2=
\frac{R^{1/2}}{\pi}\mathcal H_\rho(R)
+O_\varepsilon(R^{1/2+\varepsilon}),
$$

where

$$
\mathcal H_\rho(R)=
\sum_{n\ge1}\frac{r_2(n)}{n^{3/4}}
\Psi(\sqrt{n/R})
\cos(2\pi R\sqrt n-3\pi/4).
$$

The full conjecture is equivalent, at the $\varepsilon$-loss level, to bounding this particular sum by $R^\varepsilon$. The effective transition is $n\asymp R$. This is not a weaker conjecture or a claimed solution; it isolates the arithmetic oscillation after a target-safe smoothing error. Do not replace its fixed arithmetic coefficients by arbitrary bounded coefficients.

## 7. A separate full-proof route through moments

The following bridge is elementary and is included to quantify the value of potential moment improvements.

### Moment-to-pointwise lemma

Assume for a fixed $p>0$ and $\eta_p\ge0$ that

$$
\int_{Y/2}^{3Y}|P(x)|^p\,dx
\ll_{p,\varepsilon}Y^{1+p/4+\eta_p+\varepsilon}.
$$

Then

$$
P(X)\ll_{p,\varepsilon}
X^{\theta_p+\varepsilon},\qquad
\theta_p=\frac14+\frac{3/4+\eta_p}{p+1}.
$$

### Proof

Let $X\in[Y,2Y]$ and $V=|P(X)|$. Monotonicity of the lattice count gives

$$
P(X+h)\ge P(X)-\pi h,\qquad
P(X-h)\le P(X)+\pi h\quad(h\ge0).
$$

If $P(X)>0$, use the first inequality on $0\le h\le V/(2\pi)$; if $P(X)<0$, use the second. In either case, $|P|\ge V/2$ on a one-sided interval of length $V/(2\pi)$. Any available sublinear bound ensures this interval lies in $[Y/2,3Y]$ for sufficiently large $Y$. Therefore

$$
\int_{Y/2}^{3Y}|P(x)|^p\,dx
\ge \frac{V^{p+1}}{2^{p+1}\pi}.
$$

The conclusion follows by taking the $(p+1)$st root.

For the conjectured moment order, $\eta_p=0$, the exponents are

| Moment order | Pointwise exponent supplied by this bridge |
|---|---:|
| $p=8$ | $1/3$ |
| $p=10$ | $7/22$ |
| $p=12$ | $4/13$ |
| arbitrarily large fixed $p$ | $1/4+\varepsilon$ |

One needs arbitrarily large fixed moments, not constants uniform in $p\sim\log X$. Conversely, the pointwise conjecture supplies those moment bounds. Thus this is an alternative formulation of the full difficulty, not a consequence of existing low moments.

A concrete intermediate target is

$$
\int_{Y/2}^{3Y}|P(x)|^{12}\,dx
\ll_\varepsilon Y^{4+\eta+\varepsilon}.
$$

It improves the stated Li–Yang benchmark whenever

$$
\eta<13\theta_{\mathrm{LY}}-4
=0.0882812876628\ldots.
$$

No such new twelfth-moment estimate is established in this review.

### Combinatorial and probabilistic input

The Robert–Sargos four-root spacing estimate, as stated in Zhai's Lemma 1, is

$$
\#\{n_j\asymp N:
|\sqrt{n_1}+\sqrt{n_2}-\sqrt{n_3}-\sqrt{n_4}|<\Delta\}
\ll_\varepsilon (\Delta N^{7/2}+N^2)N^\varepsilon.
$$

A high-moment program needs weighted higher-order analogues, unequal ranges, exact-resonance terms, near-resonances, and controlled tails. Write $n=ds^2$ with $d$ squarefree. Exact resonances include non-pairing relations within the same squarefree class, so Gaussian pairings alone are insufficient. After averaging over a displaced interval, retain the oscillatory off-diagonal kernel until its phase has been used; replacing every term by a positive count can reintroduce the lost power.

Xiao's 2026 work gives second- and fourth-moment estimates for unweighted square-root sums over specified integer-frequency ranges. It supplies a useful comparison problem, not the required twelfth moment or a fixed-center estimate. Lester–Wigman's distributional work provides a model for arithmetic dependence and separated configurations. Independence heuristics must be converted into deterministic correlation estimates before they can contribute to a uniform theorem.

## 8. Instructions for the next campaigns

### Campaign A: complete-source coefficient and mask analysis

First read the actual Round-200 increment when available and reconcile it with this pinned state. Then formulate one question about a complete surviving source, preferably the coupled original-$t=1$ contribution indicated by the missing-corner calculation.

Derive every amplitude, phase, mask, gcd change, support condition, and multiplicity on a common domain. Test whether the actual row masks are unions of few intervals. Apply the elementary mask lemma only after establishing the requisite unmasked bilinear estimate and coefficient factorization. The outcome must identify the exact source of any remaining power loss.

### Campaign B: one quantitative external-theorem application

Choose the one source-compatible kernel exposed by Campaign A. Map it to an exact Blomer–Pascadi, Pascadi, Milićević–Qin–Wu, or trace-function theorem. Include unequal-length ranges and exceptional moduli as needed. Produce the net exponent after every norm, completion, partition, and reconstruction cost. A resemblance of phases does not count.

A positive result must cover a complete quantified range and its complement must already be bounded or explicitly remain open. A negative result must identify the first failed hypothesis and stop that exact import attempt.

### Campaign C: whole-discrepancy large values

Keep this separate from the M1/M2 dependency chain. Establish the exact weighted moment expansion with all truncation errors. Reproduce a known low-order estimate as a normalization check, then target the first higher-order correlation bound capable of improving the twelfth-moment loss below the threshold above. Do not claim that a fourth-moment result extrapolates to order twelve.

### Working rules

Keep one conductor and up to three temporary roles: analytic attack, independent derivation/counterexample search, and parameter/norm audit. Freeze the mathematical statement, rather than treating an arbitrarily selected mechanism as the only possible proof method. Formal acceptance still requires an independently checked proof and exact dependencies.

Measure progress by a complete parent estimate, a strictly better worst-case exponent, or an essential new reduction that enables such an estimate. Archive repetitive mechanism-specific failures instead of treating each as another step toward an endpoint proof. Preserve all counterexamples on the actual physical coefficients; counterexamples for enlarged arbitrary-array classes do not refute the original target.

## 9. Sources and provenance

### Repository sources (all at the pinned commit unless noted)

- `state/current_round.md` (live default branch rechecked): Round 199 complete.
- `state/project_summary.md`: accepted internal and external exponents; historical reductions.
- `state/best_proof_draft.md`: standard conditional proof and M1/M2 formulas.
- `strategy/conductor_0823_full_proof_strategy.md`: earlier warnings on within-ray gains and incomplete exponent transfers.
- `strategy/round198_full_proof_strategy_current_literature_review.md`.
- `rounds/codex-managed/full-proof-round195-197-strategy-literature-review/synthesis.md`.
- `rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/synthesis.md`.
- `proofs/kernels/m9_m1_hard_top_t1_p2_cross_gcd_cellular_boundary_self_return.md`.

Repository: https://github.com/yutianlee/gauss-circle-ai-collab/tree/7a4999a5df90bc2a9f6ea4f84fae3a4aa1b99c39

### Primary literature

1. X. Li and X. Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*, arXiv:2308.14859v2 (14 September 2023), Theorem 1.2. https://arxiv.org/abs/2308.14859
2. L. Guth and D. Maldague, *Amplitude dependent wave envelope estimates for the cone in R3*, arXiv:2206.01093v2. https://arxiv.org/abs/2206.01093
3. V. Blomer and A. Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311v1 (27 July 2026), Theorem 1.1 and unequal-length Theorem 5.5. https://arxiv.org/abs/2607.24311
4. A. Pascadi, *Non-abelian amplification and bilinear forms with Kloosterman sums*, arXiv:2511.08445v2 (21 June 2026), Theorem 1.2 and Example 1.3. https://arxiv.org/abs/2511.08445
5. D. Milićević, X. Qin, X. Wu, *Bilinear forms with Kloosterman sums to general moduli*, arXiv:2511.07550. https://arxiv.org/abs/2511.07550
6. E. Fouvry, E. Kowalski, P. Michel, W. Sawin, *Bilinear forms with trace functions*, arXiv:2511.09459v3 (11 March 2026). https://arxiv.org/abs/2511.09459
7. D. Milićević, C. Robinson, C. Shupe, *Sums of products of Kloosterman sums to prime power moduli*, arXiv:2608.21346. Exact applicability restrictions here are reported from the repository's primary-source audit, not from a fresh full-paper verification. https://arxiv.org/abs/2608.21346
8. Y. Xiao, *Moment Estimates and Discrepancy for Sums of Square Roots Modulo One*, arXiv:2606.28986v1. https://arxiv.org/abs/2606.28986
9. S. Lester and I. Wigman, *Around the Gauss circle problem: Hardy's conjecture and the distribution of lattice points near circles*, arXiv:2305.03549. https://arxiv.org/abs/2305.03549
10. W. Zhai, *On higher-power moments of Delta(x) (III)*, Acta Arithmetica 118 (2005), 263–281; arXiv:0805.1523, Lemma 1 and Corollary 1. https://arxiv.org/abs/0805.1523
11. O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, Journal für die reine und angewandte Mathematik 591 (2006), 1–20. DOI: 10.1515/CRELLE.2006.012.

**Withdrawal warning:** A. Dong, N. Robles, and D. Zeindler, arXiv:2601.00292v2, is withdrawn. Its stated improvement cannot be used: the authors report a missing factor $L^2$ in equation (2.53). https://arxiv.org/abs/2601.00292

## Conclusion

The most valuable next change is not another notation system or a finer partition. It is a theorem on a complete actual signed sum, with a verified coefficient norm and a positive power margin after reconstruction. The row-interval lemma gives a specific way to test whether moving masks are genuinely an obstacle to new bilinear estimates. The whole-discrepancy moment bridge gives a separate, quantitatively meaningful route to an improved exponent and eventually to the full target. Both routes still require new analytic estimates; neither is claimed complete here.
