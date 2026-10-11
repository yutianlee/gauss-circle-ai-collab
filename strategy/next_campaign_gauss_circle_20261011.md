# Gauss circle research: revised campaign directive

Date: 11 October 2026
Reviewed main-branch snapshot: `7a4999a5df90bc2a9f6ea4f84fae3a4aa1b99c39` (published 23 September 2026).
Latest completed round visible in this snapshot: 199.
This is a proposed strategy, not a State Patch, a proof of a parent obligation, or a claim that newer unpublished work was inspected.

## 1. Objective and fixed status

Write

\[
P(X)=\#\{(m,n)\in\mathbb Z^2:m^2+n^2\leq X\}-\pi X.
\]

The full target is `P(X) <<_epsilon X^(1/4+epsilon)` for every real X >= 2.
The snapshot reports the internal uniform exponent 1/3, the accepted external Li--Yang comparison exponent

\[
\theta_{\rm LY}=(3292+25\sqrt{1717})/13762
=0.3144831759740614\ldots,
\]

and an internally reconstructed mean-square/density-one theorem. Its independent M1 and M2 parents, the necessary target-scale endpoint assembly, and the quarter theorem remain open or conditional. The repository's narrow repairs to the Li--Yang source chain were not independently reproduced in this review.

A sector result is useful only when its contribution to the remaining parent bound is quantified. Improving the internal 1/3 architecture is not the same achievement as improving the external comparison exponent.

## 2. What Round 199 actually rules out

The whole-allocation B--E--C triangle preserves the displayed P2 sector, but its character holonomy is +1. With the notation of the kernel,

\[
\Sigma_{BEC}=(u_0+t u_1)\overline{(\ell_0+p\ell_1)}
-pu_0\overline{\ell_1}.
\]

On p=-1, deleting the fourth corner leaves a coefficient-one endpoint term. Adding that corner changes the recomputed gcd from A to Aq and enters the unproved P1 sector. Partial factor transfers also generate transported-mask commutators.

This is a no-go for the specified cancellation mechanism, not a lower bound for the literal sum or a counterexample to the desired theorem. In particular, the D_L L^2 positive upper capacity is not physical lower mass.

Do not launch another P2-only cellular variation unless a new analytic estimate for its actual boundary is supplied. A full-allocation-orbit proposal must first restore all affected P1/P2 terms with their original weights and zero extensions. Completing the orbit does not by itself remove sharp-code jumps or prove cancellation.

## 3. Selected next proof exercise: low-loss transfer of an M1 Kloosterman operator

Return to an exact M1 Kloosterman representation already justified in the accepted reductions. Do not assume that the currently active P2 triangle is the appropriate representation for this source input.

### Candidate external input

Blomer--Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311v1, 27 July 2026, Theorem 1.1.
For intervals I,J of lengths at most sqrt(c), a invertible modulo c, and the primitivity condition (m,n,c)=1, their theorem gives

\[
\left|\sum_{m\in I,n\in J\atop(m,n,c)=1}
\alpha_m\beta_n S(am,n;c)\right|
\ll \|\alpha\|_2\|\beta\|_2 c^{31/32+o(1)}.
\]

The source's general length-dependent theorem must be used outside this range. Do not drop the primitivity condition on arbitrary shifted intervals. The source is a candidate dependency: this directive does not certify the entire external proof or its application to M1.

### Elementary sharp-mask lemma

For any complex M-by-N matrix T and integers 0 <= a_m <= b_m <= N, let

\[
W_{mn}=\mathbf 1_{a_m<n\leq b_m}.
\]

Then

\[
\|W\odot T\|_{\ell^2\to\ell^2}
\ll \log(2N)\|T\|_{\ell^2\to\ell^2}.
\]

Proof: take Q=4N+1 and the periodic indicator h of {-N,...,0} modulo Q. For n in {1,...,N} and b in {0,...,N}, h(n-b)=1_{n<=b}. Its normalized Fourier coefficients satisfy

\[
\sum_{k\bmod Q}|\widehat h(k)|\ll\log(2N).
\]

Thus each prefix mask is a linear combination, with that total coefficient mass, of row and column diagonal unitary multipliers of T. An interval is the difference of two prefixes. This proves the claim without smoothing or a boundary-error estimate.

A general sufficient transfer condition is a separated expansion

\[
w(m,n)=\sum_j a_j(m)b_j(n),\qquad
\mathcal A(w)=\sum_j\|a_j\|_\infty\|b_j\|_\infty.
\]

The weighted bilinear estimate costs at most A(w). The infimum over all such expansions can be used. A subpower cost preserves the candidate external power saving. This is a sufficient condition, not a necessary one; failure to find it is not a no-go for all Schur-multiplier methods.

### Required deliverable

Give an exact identity relating one complete, quantitatively important M1 parent packet to these matrices or to the cyclic fourth-moment operator in the external proof. Display every stationary-phase factor, modulus, summation length, gcd restriction, coefficient norm, actual oscillatory symbol, and sharp selector. Establish the total transfer cost.

A common word such as “four-Kloosterman” is not an identity: the cyclic product in the external paper and the M1 four-row Gram operator must be matched algebraically. A fourfold correlation cannot simply be replaced by a bilinear form. Include nonseparable oscillatory weights in the transfer budget, not only indicator masks.

Recompute the parent exponent after all Cauchy--Schwarz steps, modulus/packet sums, and endpoint terms. A raw c^(-1/32) gain is not a Gauss exponent gain. If a transfer costs c^rho, the bilinear-stage saving is only c^(-1/32+rho+o(1)), before the remaining assembly.

### Decisive tests and stop rule

Test actual coefficients on prime, squarefree composite, and prime-power moduli; on exact gcd-return families; and across literal sharp endpoints. Include both orientations and branches wherever the physical representation requires their joint sum.

If the external matrix cannot be matched, document the precise unmatched kernel. If the full cost consumes the saving at every bottleneck scale, reject this attachment, not the external theorem. Do not run repeated transforms that return the same normalized capacity.

## 4. Decoupling track: geometry plus arithmetic, not a generic black box

The withdrawn source is Bourgain--Watt, arXiv:1709.04340, withdrawn 16 July 2023. The notice identifies specific defects in spacing/reduction arguments. It is not a withdrawal of decoupling theory.

Use Li--Yang, arXiv:2308.14859v2, and Guth--Maldague, arXiv:2206.01093, as primary starting points. Li--Yang combine small-cap first-spacing estimates with second-spacing estimates and an outer pointwise argument. Decoupling can therefore contribute to a pointwise theorem; a mean-value estimate alone is not the complete bridge.

The first-spacing frequencies (l,kl,l sqrt(k)) satisfy xi_3^2=xi_1 xi_2. This explains the cone geometry. It does not establish that an arbitrary transformed M1/M2 packet has the same geometry or sampling scales.

First deliverable: a literal normal-form and scaling lemma for one complete unresolved block. Specify the frequency surface, physical integration box, cap dimensions, Jacobians, admissible exponent, Taylor remainders, and weighted symbols. Then identify the exact post-assembly power deficit.

Second deliverable: either a complete improved packet estimate or an arithmetic classification of configurations saturating the geometric bound that leads to a new signed estimate for the actual coefficients. Treat equal rays, near rays, prime-power degeneracies, and sharp endpoints explicitly. The general small-cap inequalities have sharp examples; excluding those examples for the literal arithmetic coefficients requires proof.

Do not turn a signed aggregate into absolute values of each shift or each divisor tuple merely to fit a theorem. Do not interpret unsigned incidence counts or coefficient-blind large-sieve capacity as cancellation.

## 5. Independent global large-values / moments track

This track targets the original P(X), rather than an unnecessarily strong separate-block estimate. It does not automatically reuse M1/M2 gains and it must include the exact truncation remainder.

For any fixed p>0, the bound

\[
\int_{Y/2}^{3Y}|P(t)|^p\,dt
\ll_{p,\epsilon}Y^{1+p/4+\lambda_p+\epsilon}
\]

implies

\[
|P(X)|\ll_{p,\epsilon}
X^{(1+p/4+\lambda_p)/(p+1)+\epsilon}.
\]

Proof: at P(x)=V>0, monotonicity of the counting function gives P(x+h)>=V-pi*h. At P(x)=-V<0 it gives P(x-h)<=-V+pi*h. Hence |P|>=V/2 on a one-sided interval of length V/(2*pi). The interval lies in an enlarged dyadic range using any elementary sublinear bound. Integrating gives V^(p+1) << integral |P|^p. This standard moment-to-pointwise mechanism is also discussed in Popov (2024), Section 6; it is not a newly discovered reduction.

Concrete target:

\[
\int_{Y/2}^{3Y}|P(t)|^{12}\,dt
\ll_\epsilon Y^{4+\lambda+\epsilon},\qquad
\lambda<13\theta_{\rm LY}-4=0.08828128766279786\ldots.
\]

Such a result would beat the comparison exponent. Lambda=0 would give 4/13. No such estimate is proved by this directive. An optimal absolute eleventh moment would already give 5/16, but even moments are more directly expanded algebraically.

Start with a primary-source inventory of existing high moments and large-value estimates, then derive the exact additional near-resonance estimate needed for the new target. Do not count rediscovery of known second/fourth moments or the repository's density-one theorem as new progress.

Probability must refer to a declared random parameter, e.g. X uniform on [Y,2Y]. A limiting distribution, pair decorrelation, or a model with independent signs is not a uniform high-moment bound. In a square-root phase expansion retain n=s a^2 correlations and the near-resonance scale fixed by the actual integration interval. The off-diagonal tail and truncation remainder are essential.

The family of optimal moment bounds for arbitrarily large fixed p would imply the quarter theorem. It is correspondingly strong; this is a research target, not a shortcut supplied by an existing central limit theorem.

## 6. Acceptance and reporting

Run at most three mathematical tracks: the selected Kloosterman/mask transfer; decoupling with arithmetic concentration; and global large values. Use independent audits of the selected transfer identity and its exponent budget rather than several agents making the same formal rearrangement.

Every report must contain an exact theorem or conditional lemma, a complete proof or the first unresolved step, an endpoint and coefficient audit, its parent implication, and a recalculated worst-scale exponent. Preserve the distinction between linear and squared/Gram deficits. Promote no parent on the strength of a strict subfamily alone.

Measure progress by the strongest assembled theorem, a genuinely stronger complete-parent estimate, or a reusable new arithmetic estimate with an explicit application. A proliferation of owner labels and mechanism-specific no-go statements is not a substitute for these outcomes.

## 7. Sources and evidence to reopen

Repository evidence at the fixed snapshot:
- README.md
- state/project_summary.md
- state/current_round.md
- state/best_proof_draft.md (header through Round 193; not the final Round-199 status)
- rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/synthesis.md
- proofs/kernels/m9_m1_hard_top_t1_p2_cross_gcd_cellular_boundary_self_return.md

Primary literature:
- Bourgain--Watt, arXiv:1709.04340: withdrawal notice, 16 July 2023.
- Li--Yang, arXiv:2308.14859v2: first/second spacing and the circle comparison bound.
- Guth--Maldague, arXiv:2206.01093: amplitude-dependent wave envelopes and sharp small-cap cone estimates.
- Pascadi, arXiv:2511.08445v2 (21 June 2026): non-abelian amplification and Kloosterman bilinear forms.
- Blomer--Pascadi, arXiv:2607.24311v1 (27 July 2026): quadratic characters and all-modulus Kloosterman bilinear bounds; especially Theorem 1.1 and Sections 1.4--1.5.
- Popov, Voronoi's formulae and the Gauss problem, Russian Mathematical Surveys 79(1) (2024), 53--126: Section 6 and short-interval results.
- Lester--Wigman, Around the Gauss circle problem: Hardy's conjecture and the distribution of lattice points near circles, Journal of the London Mathematical Society 110(3) (2024), e12977: statistical precedents, not a uniform quarter-exponent theorem.
