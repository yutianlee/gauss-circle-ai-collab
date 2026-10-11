# Round 231: nonauthor seam review of the cell obstruction

## 1. Result

**PASS at the repaired candidate hash.** The complete T-sized-shell lower bound and the smaller-shell N=T^(4beta) lower bound are proved within the stated perturbation class. The complete infinite baseline is retained. Both smaller-shell signs satisfy the inherited pointwise ceiling on its actual radius window, and at least one fixed sign has twelfth moment at least c T^(10beta).

This is a nonauthor line and interface review, not a blind rederivation of the smaller-shell extension. The earlier statement-only report remains frozen and covers only its original isolated problem.

- Campaign: round231_local_arithmetic_admission.
- Task: cell_obstruction_seam_review.
- Review time: 2026-10-11, following the 06:08:56 UTC context-hash check and subsequent final-candidate verification.
- Original candidate reviewed: `strategy/round231_local_arithmetic_admission/conductor_cell_obstruction.md`, SHA256 `83e85c027049f2c52200345bc35125e3b3dd6284c1646e496c76a29cf7f2fc91`.
- **Final candidate verified:** same path, SHA256 `09548d3a7f039258bdb60e34e6faedcc560f8b76b84b17bfd3cb088ba7ab12f2`.
- Frozen statement-only report: SHA256 `001465ba0e7e73d99f75e0375df449b7cddcc0d2a362cfb5baba06e649e35fec`, unchanged.
- Authoritative graph provenance: SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`, verified unchanged.

Two local repairs were requested and verified in the final candidate: positivity of Psi on the whole interval [0,sqrt(b)], and explicit restriction of every inherited complete-wave ceiling to R in [T/2,2T]. No mathematical gap remains in the repaired candidate's stated obstruction. Its limitation to perturbations, rather than exact r2, is essential.

## 2. Exact reviewed statement and hypotheses

Use the packet's fixed nonnegative radial smooth unit-mass mollifier, supported in the unit disk, and its real even Schwartz transform Psi. Use the fixed nonnegative smooth w supported in [1/2,2] and equal to one on [1/sqrt(2),sqrt(3)]. Define the complete actual baseline

$$
B_T(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
\cos(2\pi R\sqrt n-3\pi/4).
$$

The final candidate chooses fixed 0<a<b and p_0>0 with Psi(s)>=p_0 for every s in [0,sqrt(b)]. Fix a nondegenerate compact interval J strictly inside (1/sqrt(2),sqrt(3)). For either N=T, or any N=N(T) tending to infinity with N<=T, partition the represented integers aN<=n<=bN into K<=N^(1-delta) nonempty disjoint cells, independently of R, with fixed delta>0.

For all sufficiently large T there exists a finite real perturbation d=d(T,partition), supported in this shell, such that |d_n|<=r2(n)/2 and every cell sum of d is zero. Write

$$
D_{N,T}(R)=\sum_nd_nn^{-3/4}\Psi(\sqrt{n/T})
\cos(2\pi R\sqrt n-3\pi/4),
\qquad B_T^\sigma=B_T+\sigma D_{N,T}.
$$

Then

$$
\|D_{N,T}\|_\infty\le C N^{1/4},\qquad
D_{N,T}(R_0)\ge cN^{1/4}\quad\text{for some }R_0/T\in J,
$$

$$
\|D_{N,T}'\|_\infty\le CN^{3/4},\qquad
M_{12}(D_{N,T})\ge cN^{5/2},\qquad
\max_{\sigma\in\{-1,1\}}M_{12}(B_T^\sigma)\ge cN^{5/2}.
$$

Here the unrestricted suprema apply to the finite perturbation only, and M12 is the complete weighted integral with w(R/T). For N=T, one sign selected at R_0 also retains a peak interval of physical width comparable to T^(-1/2) after the entire baseline is appended.

For the fixed accepted exponent beta=2theta_LY-1/2 and N=T^(4beta), both perturbed waves satisfy

$$
\sup_{R\in[T/2,2T]}|B_T^\sigma(R)|\ll_\epsilon T^{\beta+\epsilon}
\quad\text{for every fixed }\epsilon>0,
$$

while one sign has M12(B_T^sigma)>=cT^(10beta). The number of preserved cells in this specialization is K<=T^(4beta(1-delta)), not the larger T-sized-shell cell budget.

The constants are uniform over all admissible partitions and over 1<=N<=T once N is sufficiently large. They may depend on fixed a,b,p_0,J,w,Psi,delta and the requested epsilon in the imported pointwise estimate. The coefficient vector and chosen sign may depend on T and the partition. They are fixed while R varies. No single perturbation sequence or sign valid simultaneously for all T is asserted. For delta>1 the nonempty-cell condition is eventually impossible; that range is vacuous.

## 3. Proof and seam verification

**Actual r2 mass and support: PASS.** Let A(x)=sum_(1<=n<=x)r2(n). The elementary unit-square comparison for the disk gives A(x)=pi x+O(sqrt(x)+1). Taking the difference at bN and the left limit at aN gives

$$
\sum_{aN\le n\le bN}r_2(n)=\pi(b-a)N+O(\sqrt N+1).
$$

If aN is an integer, its endpoint atom is also O(sqrt(N)+1), either by a direct bound on the number of possible first coordinates or by the divisor bound. Thus inclusive endpoints do not change the mass asymptotic. The identity r2(n)=4 sum_(d|n)chi4(d) gives 0<=r2(n)<=4tau(n), and the elementary divisor bound yields max_(aN<=n<=bN)r2(n)<<_eta N^eta for every fixed eta>0. No positive density theorem for the represented integers is needed: their weighted mass is comparable to N, which is the quantity actually used.

**Uniform profile and exact normalization: PASS after the positivity repair.** For x in [a,b] and N<=T,

$$
v_{N,T}(x)=x^{-3/4}\Psi(\sqrt{Nx/T})
$$

satisfies p_0 b^(-3/4)<=v_(N,T)(x)<=a^(-3/4)||Psi||_infinity. Crucially,

$$
N^{-3/4}v_{N,T}(n/N)
=n^{-3/4}\Psi(\sqrt{n/T}),
$$

so changing the construction scale from T to N preserves the exact complete-wave coefficient normalization. The phase remains the real cosine at the literal square root. No derivative in N or T is taken; the family of profiles needs only these uniform bounds.

**Radius averaging and cell projection: PASS.** The average is over TJ, of length comparable to T, even when n is of size N. Direct trigonometric integration gives, uniformly for distinct n,m in the shell,

$$
\left|\operatorname{Avg}_{TJ}q_nq_m\right|
\le C\frac{\sqrt N}{T|n-m|},\qquad
\operatorname{Avg}_{TJ}q_n^2=\frac{v_{N,T}(n/N)^2}{2}
+O\left(\frac1{T\sqrt N}\right),
$$

where q_n=v_(N,T)(n/N)cos(2pi R sqrt(n)-3pi/4). The real product formula includes both difference and sum frequencies; neither is discarded. The candidate's harmonic-sum bound is valid:

$$
\operatorname{Avg}_{TJ}\left(\sum_{n\in C}c_nq_n\right)^2
\le C\left(1+\frac{\sqrt N\log(2N)}T\right)\sum_{n\in C}c_n^2.
$$

Since T>=N, the parenthesis is uniformly bounded. Division by cell mass W_C>0 and summation costs at most C K c_max. Choosing eta=delta/2 once gives Kc_max<<N^(1-delta/2)=o(N), uniformly over partitions. Small cell masses create no uncontrolled denominator because sum_C c_n^2/W_C<=c_max.

Equivalently, the weighted pairwise-variance identity from the frozen report applies at the new averaging length: every distinct-pair averaged squared difference is bounded below by a fixed positive constant for large N, because sqrt(N)/T<=N^(-1/2). This confirms the new scale without importing an unproved orthogonality assumption. This verification is a nonauthor seam calculation, not a claim that the extension appeared in the blind brief.

**Construction, signs, and finite width: PASS.** The fixed vector

$$
d_n=\frac{c_n}{4C}\bigl(q_n(R_0)-m_C(R_0)\bigr)
$$

has |d_n|<=c_n/2 and zero sum in each cell. Its value at R_0 is N^(-3/4) times a fixed positive multiple of residual energy, hence at least cN^(1/4). Its global absolute value is at most CN^(-3/4)sum c_n<=CN^(1/4), and differentiating the literal cosine gives derivative at most CN^(-3/4)sqrt(N)sum c_n<=CN^(3/4). Thus it remains large on an interval of physical width cN^(-1/2). The rescaled width is c/(T sqrt(N)), which tends to zero; J's fixed margin places the whole interval where w=1. The moment is at least cN^3 N^(-1/2)=cN^(5/2).

All coefficients d_n are frozen before this differentiation. Both raw coefficient vectors satisfy r2(n)/2<=r2(n)+sigma d_n<=3r2(n)/2. Every zero of r2 remains zero, every positive raw coefficient stays positive, every prescribed finite cell total is unchanged, and every coefficient outside the shell is exactly unchanged.

**Entire baseline and tail: PASS.** The required derivative estimate is genuinely for the complete series:

$$
\sum_{n\ge1}r_2(n)n^{-1/4}|\Psi(\sqrt{n/T})|\ll T^{3/4}.
$$

For n<=T this follows by partial summation from A(x)<<x. For n in a dyadic interval [2^kT,2^(k+1)T], k>=0, use |Psi(s)|<=C_L(1+|s|)^(-L). The contribution is at most

$$
C_LT^{3/4}2^{k(3/4-L/2)}.
$$

The sum converges for any fixed L>3/2, exactly as stated. This gives absolute and uniform-in-R convergence of the derivative series for each fixed T. The original series is also absolutely uniformly convergent. Termwise differentiation and the global bound ||B_T'||_infinity<<T^(3/4) are therefore justified without dropping an infinite tail or paying an unspecified epsilon. For N=T, selecting the sign at R_0 and applying this derivative bound to B_T+sigma D proves the complete peak-interval lower bound.

**Smaller-shell baseline addition: PASS by convexity, not by inherited narrow width.** For any real B,D,

$$
2|D|^{12}\le|B+D|^{12}+|B-D|^{12}.
$$

This is midpoint convexity applied to B+D and D-B. Multiplying by w>=0 and integrating the complete waves gives one fixed sign with M12(B+sigma D)>=M12(D). Both integrals are finite, because w has compact support and the series are uniformly convergent for fixed T. The sign is selected after integration and is independent of R.

When N<T, the known baseline derivative is only O(T^(3/4)), so it would not justify preserving an N^(-1/2) interval for the complete perturbed wave. The candidate explicitly avoids that invalid inference. Its smaller-shell conclusion needs only the integrated sign inequality; it does not assert that its moment sign preserves the original radius R_0 or the finite perturbation's entire interval.

**Accepted ceiling and exponent substitution: PASS.** The selectively checked graph nodes accept the actual-wave input only through the qualified final Li--Yang application and the actual sharp/smoothed reconstruction. They give the ceiling on R in [T/2,2T] for the precise mollifier used here. Algebraically,

$$
\beta=2\theta_{LY}-\frac12
=\frac{50\sqrt{1717}-297}{13762},\qquad
\frac18<\beta<\frac{27}{208}<\frac14.
$$

Thus N=T^(4beta) tends to infinity, is at most T, and satisfies N^(1/4)=T^beta and N^(5/2)=T^(10beta). For each sign the triangle inequality on the correct window gives

$$
\sup_{[T/2,2T]}|B_T+\sigma D|
\le C_\epsilon T^{\beta+\epsilon}+CT^\beta
\ll_\epsilon T^{\beta+\epsilon}.
$$

Both signs obey this ceiling before the moment sign is chosen. Convexity then supplies the claimed T^(10beta) lower bound for one of them. The new perturbations do not require a new pointwise theorem for arbitrary coefficient masks.

For any proposed exponent gamma<10beta, fix 0<epsilon<10beta-gamma. A bound M12<=C_epsilon T^(gamma+epsilon) uniform over this admitted coefficient class contradicts the exhibited lower bound for large T. In particular 10beta>5/4>29/25, so the complete target exponent cannot follow from these data alone. This inference concerns a uniform family that permits T-dependent coefficients. It does not refute estimates for a single prescribed arithmetic sequence whose proof uses additional identities.

## 4. First doubtful or unproved step and repair disposition

In the original hash, positivity only on sqrt([a,b]) did not literally establish the claimed positive lower bound for every profile v_(N,T) with N/T in (0,1]. Its argument may fall below sqrt(a). The final candidate repairs this by requiring Psi>=p_0>0 on the whole [0,sqrt(b)], which is available from continuity at zero and Psi(0)=1. The required bound is now explicit and sufficient. Even before this repair, the specialization N=T^(4beta) eventually lies in a positive neighborhood of zero, but that observation alone would not have justified the full uniform N<=T paragraph.

The original smaller-shell ceiling displayed an unqualified supremum after citing a window-restricted actual estimate. The final candidate explicitly restricts both that triangle inequality and the resulting complete-wave supremum to [T/2,2T]. Unrestricted supremum bounds remain only where independently proved for D or derivatives. This repair is verified.

No doubtful step remains in the final candidate's stated lower-bound obstruction. The first unsupported step beyond its scope would be replacing the perturbed coefficient family with the exact r2 sequence, or claiming that all arithmetic hypotheses are preserved. The candidate expressly declines both inferences. Neither this review nor the accepted distinct-radical reduction supplies the missing actual signed moment estimate.

The source theorem itself is not re-audited here. Reliance is on the unchanged accepted graph node, with all its recorded repairs: M<T^(7/16), H=MT^x, the corrected square root in (5.27), the exact two-sign circle identity, the corrected Lemma 4.1 verification bypassing false printed (4.9), the required beta_2 condition, and absorption of the missing logarithm. No broader printed proposition is imported.

## 5. Required controls and outcomes

1. **Singleton cells: PASS.** They force d=0. But their number is at least (sum c_n)/c_max>>N^(1-eta), incompatible with K<=N^(1-delta) for eta<delta and large N. No nonzero singleton perturbation is asserted.
2. **Zero coefficients and actual support: PASS.** Zero r2 values receive d=0; positive entries remain between one-half and three-halves of their original values. This is raw coefficient support, with the same smoothing factors at the same frequencies.
3. **Nonnegativity and exact cell sums: PASS for both signs.** The perturbation cap and weighted centering prove them algebraically before selecting a sign.
4. **Endpoints and real T,N: PASS.** The shell uses inclusive integer endpoints, and the area-count error pays them. N=T^(4beta) may be real; no integer-valued N assumption enters. Cell boundaries require unique ownership.
5. **Fixed coefficients: PASS.** Partition and coefficients remain fixed over the radius integration. Dependence on T and the partition is explicitly permitted.
6. **Physical width: PASS.** D has physical width N^(-1/2), not unit width and not that width in R/T. The complete baseline shares the needed derivative scale only in the T-sized-shell proof. The smaller-shell proof uses convexity instead.
7. **Infinite tail: PASS.** Its absolutely convergent derivative sum is estimated with any Schwartz order L>3/2. No upper cutoff or discarded complement enters either lower bound.
8. **Quantifiers and constants: PASS.** Fixed eta=delta/2 pays projection loss. Constants are independent of partition and admissible N,T after thresholds. The chosen sign need not be the same for different T. The no-go conclusion is explicitly for uniform coefficient-class estimates.
9. **Inherited ceiling: PASS after repair.** The window is [T/2,2T], and the actual source qualifications and fixed mollifier are retained. Both signs satisfy the ceiling, so integrated sign choice introduces no incompatibility.
10. **Residue complexity: PASS with the stated shell budget.** Residues modulo L intersected with H disjoint intervals give at most LH cells; coarser divisor moduli follow by summing cells. For the smaller-shell conclusion the applicable condition is LH<=N^(1-delta)=T^(4beta(1-delta)). No arbitrary collection of moduli, all prefix sums, or cost-free least common multiple is preserved.
11. **Actual arithmetic scope: PASS.** These are generally real, nonintegral perturbations that need not preserve divisor-character identities or multiplicativity. There is no claimed counterexample for exact r2, the accepted distinct-class target, or the circle conjecture.

Every control is analytical. No numerical experiment was used.

## 6. Dependencies and exact artifacts used

- `protocol.md`, already read for the isolated assignment.
- `strategy/round231_local_arithmetic_admission/conductor_cell_obstruction.md`: original hash `83e85c027049f2c52200345bc35125e3b3dd6284c1646e496c76a29cf7f2fc91`; repaired and finally verified hash `09548d3a7f039258bdb60e34e6faedcc560f8b76b84b17bfd3cb088ba7ab12f2`.
- `strategy/round231_local_arithmetic_admission/reports/blind_cell_control.md`: frozen hash `001465ba0e7e73d99f75e0375df449b7cddcc0d2a362cfb5baba06e649e35fec`; its existing proof is used only for the finite-cell interface, and its frozen scope is not extended retrospectively.
- `strategy/round231_local_arithmetic_admission/briefs/complete_target.md`: hash `4cd95ec7203420e99e51a4dbf3e0de5c3732fe1e589ed9e3344bb0b96b1fd8d6`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`: hash `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.
- `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`: hash `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee`.
- `state/proof_obligations.yml`: hash `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`; targeted checks of `GC-complete-square-root-large-values-moment-bound`, `GC-complete-distinct-radical-twelfth-reduction`, and `GC-external-Li-Yang-theta-star`. Only these nodes are used as graph dependencies.

The packet's complete target was located under `briefs/`; an initial attempt at a packet-root path returned file-not-found and supplied no content. No sibling report, prior strategy packet, external source, or other claim is used as evidence. The graph's linked source cards were not opened. Hashing is provenance verification, not a mathematical experiment.

Only this assigned seam review was written. The isolated report, candidate, graph, proof draft, validation matrices, and synthesis were not modified by this reviewer. Candidate repairs were made by the conductor and then checked against the final hash above.

## 7. Recommended state effect

**Retain the final candidate at reviewed prelaunch evidence level**, bound to SHA256 `09548d3a7f039258bdb60e34e6faedcc560f8b76b84b17bfd3cb088ba7ab12f2`. Both requested local repairs are complete; no further repair is required for the reviewed claims.

Do not promote a new actual arithmetic estimate or change the graph on this review alone. The valid conclusion is that exact totals in the specified number of fixed cells, actual represented support, bounded nonnegative coefficient comparison, the unchanged complete complement, and the actual pointwise ceiling still admit a perturbation family with M12>=cT^(10beta). That conclusion rules out only uniform arguments based on those data. It neither estimates the exact actual moment from below nor closes the 29/25 target.

The original isolated report remains frozen. This separate nonauthor review covers the additional full-baseline and smaller-shell seams and completes the assigned task without opening another round.
