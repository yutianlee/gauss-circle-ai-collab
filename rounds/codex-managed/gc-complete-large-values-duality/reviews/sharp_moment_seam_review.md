# Round 204 sharp reconstruction, moment, and scope seam review

## 1. Result

**GREEN for the assigned seam, conditional on candidate (L1).** The fixed smoothing argument, inclusive sharp reconstruction, all-fixed-p layer cake, endpoint comparison, twelfth-moment exponent, and generic-control scope in Sections 1, 6, and 7 are valid. No mathematical correction is required in those sections.

Campaign: `gc-complete-large-values-duality`. Role: independent analytic seam reviewer. Task: `sharp_moment_seam_review`. Generated: 2026-09-26 UTC. Analytical/algebraic allocation: 100%; numerical experiments: none.

Reviewed candidate: `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, SHA256 **942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212**, verified directly. The conductor supplied this revision after adding the singleton n=1 in Section 5; Sections 1, 6, and 7 are unchanged from initially supplied hash `5f0c1efcdb230b7ba73206dc960a95a58a6fd03166deb8340f00ed46ab532c6e`. This report binds to the revised hash, not merely the earlier text.

Starting/current graph hash verified: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`.

The conclusion is a moment gain conditional on the separately reviewed distribution bound. It is neither certification of L1 by this reviewer nor a pointwise circle-exponent gain.

## 2. Exact statement and hypotheses

Write
\[
 \theta=(3292+25\sqrt{1717})/13762,\qquad
 \beta=2\theta-\tfrac12,\qquad q=136/13.
\]
Use the accepted real-X inclusive discrepancy bound
\(P(X)=\#\{m\in\mathbb Z^2:|m|^2\le X\}-\pi X\ll_\eta X^{\theta+\eta}\)
for every real X>=2, and the elementary divisor bound. The elementary representation identity gives \(r_2(n)\le4d(n)\). This review does not reopen the external Li--Yang theorem.

Choose once and for all a nonnegative real radial \(\rho\in C_c^\infty(\mathbb R^2)\), supported in the unit disk, with integral one. Set \(\Psi(s)=\widehat\rho(se_1)\) under \(e(-x\cdot\xi)\). Thus Psi is real, even, Schwartz, and \(|\Psi|\le1\). For real T>=2 define the actual B_{T,U} exactly as in the candidate. Assume L1 for every fixed bounded measurable nonnegative w supported in a fixed interval [c,C] with 0<c<C, uniformly in U>=0 and V>=1.

Then, for each fixed real p>=2 and each epsilon>0,
\[
 M_p(T):=\int w(R/T)|B_{T,0}(R)|^p\,dR
 \ll_{p,\epsilon}T^{1+\epsilon}+T^{(p-2)\beta+\epsilon}.
\]
The same estimate holds with U=floor(T^(1/2047)). For real Y>=4 (and, by enlarging constants, Y>=2),
\[
 \int_{Y/2}^{3Y}|P(x)|^p\,dx
 \ll_{p,\epsilon}Y^{1+p/4+\epsilon}
                  +Y^{1+(p-2)\theta+\epsilon}.
\]
The fixed-p qualification matters: epsilon renaming and constants may depend on p. A measurable-window convention is implicit whenever its integrals are written.

## 3. Independent proof and derivation

### Fixed smoothing, closed annuli, and all real radii

Set delta=T^(-1/2) once for the whole radius window. Let
\(F_R=1_{B_R}*\rho_\delta\) and \(S_\delta(R)=\sum_mF_R(m)\).
Nonnegativity and integral one give 0<=F_R<=1. Away from the closed annulus
\(R-\delta\le|m|\le R+\delta\), the smoothed and inclusive sharp indicators agree. For sufficiently large T, R>=cT>delta, and the allowed squared radii lie in a closed interval of length 4R delta. The number of integer squared radii is at most 4R delta+2, including both endpoints. Each nonzero squared radius n is O(T^2), so its multiplicity is O_eta(T^(2 eta)). The origin, if needed in a bounded parameter range, costs only one. Therefore
\[
 |N(R)-S_\delta(R)|
 \ll_\eta (R\delta+1)T^{2\eta}
 \ll_\eta T^{1/2+2\eta}.
\]
No exclusion of integer R or integer R^2 occurs, and no half-weight convention is introduced. All bounded ranges of T are absorbed by constants depending on the fixed c,C and rho.

### Exact Poisson and Bessel normalization

F_R is smooth and compactly supported. Its periodization is a smooth periodic function; its Fourier series is absolutely convergent and can be evaluated at zero. This directly proves the required Poisson identity for each fixed real T,R without applying Poisson to a discontinuous disk indicator.

For s=|xi|>0, polar coordinates and the J0 integral give
\[
 \widehat{1_{B_R}}(\xi)=2\pi\int_0^R rJ_0(2\pi sr)\,dr
                 =\frac R sJ_1(2\pi Rs).
\]
The last identity follows from \((zJ_1(z))'=zJ_0(z)\), with zero lower endpoint. At xi=0 the transform is pi R^2. Consequently
\[
 S_\delta(R)-\pi R^2
 =R\sum_{n\ge1}r_2(n)n^{-1/2}\Psi(\sqrt{n/T})J_1(2\pi R\sqrt n).
\]
These standard identities were checked against primary NIST DLMF [10.9.1](https://dlmf.nist.gov/10.9.E1) and [10.6.6](https://dlmf.nist.gov/10.6.E6), the latter at k=nu=1.

For nu=1 and positive real z, [DLMF 10.17.3](https://dlmf.nist.gov/10.17.E3), with the positive-real error control in [10.17(iii)](https://dlmf.nist.gov/10.17.iii), gives
\[
 J_1(z)=\sqrt{2/(\pi z)}\cos(z-3\pi/4)+O(z^{-3/2}).
\]
Here nu is fixed, z=2pi R sqrt(n)>0, and for large T all such z are uniformly large; bounded T is handled separately. Inserting this yields the leading coefficient exactly
\[
 Rn^{-1/2}\sqrt{\frac2{\pi(2\pi R\sqrt n)}}
 =\frac{\sqrt R}{\pi}n^{-3/4}.
\]
The total remainder is bounded by
\[
 CR^{-1/2}\sum_{n\ge1}r_2(n)n^{-5/4}|\Psi(\sqrt{n/T})|
 \le CR^{-1/2}\sum_{n\ge1}r_2(n)n^{-5/4}
 \ll T^{-1/2},
\]
using a divisor exponent eta<1/4. This is an entire infinite-tail bound, independent of T inside the sum. The fixed smoothing already makes the original transformed sum absolutely convergent. Combining with the annulus estimate proves
\[
 P(R^2)=\pi^{-1}\sqrt R\,B_{T,0}(R)+O_\eta(T^{1/2+\eta}).
\]
In particular there is no R-dependent cutoff hidden in B_{T,0}.

### Pointwise cutoff and the small head

The accepted real-X pointwise estimate, division by sqrt(R), and the preceding formula give
\[
 |B_{T,0}(R)|\ll_\eta T^{2\theta-1/2+2\eta}+T^\eta
                  \ll_\eta T^{\beta+2\eta}.
\]
It holds throughout [cT,CT], including the sharp-count jumps. The head through U=floor(T^(1/2047)) is absolutely bounded by
\[
 \sum_{n\le U}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
 \ll_\eta U^{1/4+\eta}
 \ll_\eta T^{1/8188+\eta/2047}.
\]
Since 1/8188<beta, the tail B_{T,U} has the same supremum bound. This uses no head moment estimate.

For transparent exact comparisons, 41<sqrt(1717)<83/2 gives
\(5/16<\theta<131/416<1/3\) by rational cross multiplication. Hence
\[
 1/8<\beta<27/208,
 \qquad \beta(q-2)>\frac18\frac{110}{13}=\frac{55}{52}>1.
\]

### Layer cake with every endpoint

Let W=max(1,C_eta T^(beta+eta)) bound the supremum. Tonelli gives, for p>0,
\(M_p=p\int_0^W V^{p-1}D(V)\,dV\).
Below V=1 use D(V)<=||w||_infinity(C-c)T. Above V=1 use L1. For fixed p>2 the two integrals give
\[
 M_p\ll T+T^\eta W^{p-2}
       +T^{1+\eta}\int_1^W V^{p-q-1}\,dV.
\]
For p<q the last integral is bounded by 1/(q-p); at p=q it is log W; for p>q it is O_p(W^(p-q)). In the latter case,
\[
 1+\beta(p-q)=(p-2)\beta+[1-\beta(q-2)]<(p-2)\beta.
\]
Thus the displayed high contribution is dominated by the claimed high term. At p=2, the V^-2 term gives only T^eta log W, while the other integral is bounded because q>2. All logarithms and input eta losses fit any requested final epsilon after eta is chosen sufficiently small depending on p. This proves L2 at p=2, p=q, and every fixed real p in between or above.

The endpoint q_star=2+1/beta satisfies (q_star-2)beta=1 and q_star<q. Therefore M_p<<T^(1+epsilon) holds for 2<=p<=q_star, including equality. The exact comparison to the stated old endpoint is
\[
 q_\star-q_0=\frac1\beta-\frac{208}{27}
             =\frac{131-416\theta}{27\beta}>0,
 \qquad q_0=262/27.
\]
This establishes the algebraic comparison to the candidate's printed q0; no historical theorem is imported or updated without inspection.

### Inclusive sharp moment and exponent bookkeeping

For the final sharp interval choose one smooth nonnegative window equal to one on [1/sqrt(2),sqrt(3)]. With T=sqrt(Y), the physical inequality |a+b|^p<=2^(p-1)(|a|^p+|b|^p) and dx=2R dR give
\[
 \int_{Y/2}^{3Y}|P(x)|^p\,dx
 \ll_p T^{1+p/2}M_p+T^{2+p/2+p\eta}.
\]
All cross terms are included by this inequality on the complete function. Now
\[
 T^{1+p/2}T=T^{2+p/2}=Y^{1+p/4},
\]
\[
 T^{1+p/2}T^{(p-2)\beta}
 =T^{2+2(p-2)\theta}=Y^{1+(p-2)\theta}.
\]
The smoothing error has exactly the first permissible exponent after epsilon renaming. This proves L3 for real Y and fixed real p>=2.

At p=12, theta>5/16>3/10 implies 1+10theta>4, so the complete twelfth moment is O(Y^(1+10theta+epsilon)). Precisely, the sixth-power norm claimed in the candidate is
\[
 \|B_{T,0}^6\|_{L^2(w(R/T)\,dR)}=M_{12}^{1/2}
 \ll T^{5\beta+\epsilon},
\]
where the radius measure is not divided by T; it is the B-series that has had the sqrt(R)/pi amplitude removed. Its exponent is 5beta=10theta-5/2. The new loss from Y^4 is 10theta-3. Relative to the stated old loss,
\[
 \frac{62}{27}(\theta-\tfrac14)-(10\theta-3)
 =\frac{131-416\theta}{54}>0.
\]
No novelty or optimality claim for actual arithmetic moments follows from this comparison.

## 4. First doubtful or unproved step

No doubtful step remains in the assigned reconstruction/moment seam under L1. The first unproved input **for this report** is precisely L1: its independent correlation, duality, covering, source, and recombination reviews belong to other assigned seams. This report must not be used to replace them.

The frozen stronger actual-r2 distribution remains unproved. The sharp moment bound does not close the pointwise target. Indeed, monotonicity of N provides the usual direct implication: if |P(X)|=A, use a forward interval for P(X)>0 or a backward interval for P(X)<0 of length A/(2pi). On that interval |P|>=A/2. For X comparable to Y the accepted pointwise estimate ensures this interval stays within a fixed enlargement, giving A^(p+1) bounded by the local p-moment. The new moment would therefore give exponent
\[
 \frac{\max(1+p/4,\,1+(p-2)\theta)}{p+1}
 \ge\theta+\frac{1-3\theta}{p+1}>\theta
\]
for every fixed p>=2. In particular (1+10theta)/13>theta. Taking an unbounded p is outside the theorem's uniformity and would at best approach theta in this formula, not improve it.

## 5. Required controls and outcomes

**Closed-annulus/jump control: PASS.** The integer squared-radius count has a +2 endpoint allowance; n=0 is separately harmless. The proof treats inclusive N, both signs of P, real T,R,Y, and arbitrarily placed sharp jumps.

**Fixed-width/whole-tail control: PASS.** Delta=T^(-1/2) is independent of R. The Fourier cutoff is exactly Psi(sqrt(n/T)). The Bessel remainder is dominated by the full convergent sum of r2(n)n^(-5/4), and all high-moment mixed terms are retained through the norm inequality.

**Fixed-p endpoint control: PASS.** The cases p=2, p=q, and p=q_star are included explicitly. The tiny-head version uses the same L1 plus its own inherited supremum bound, rather than an unproved head high-moment theorem.

**Aligned generic control: PASS, with its proper scope.** Take integer N comparable to T^(4beta), an interior R0, and
\(a_n=N^{-3/4}e(-R_0\sqrt n)\) for N<n<=2N. Then
\(\sum|a_n|^2\asymp N^{-1/2}\), and the global supremum is at most CN^(1/4). If |R-R0|<=cN^(-1/2) with a sufficiently small absolute c, all residual phases have real part bounded below by a positive constant. Thus |S(R)|>=c'N^(1/4), and
\[
 \int |S(R)|^{12}\,dR\gg N^{-1/2}N^3=N^{5/2}
                                      \asymp T^{10\beta}.
\]
For a weighted lower bound choose an allowed window bounded below near R0/T; for example the window used in the sharp reconstruction. No positive lower bound is asserted for every arbitrary nonnegative window, which could vanish. This existential control is sufficient to test the generic mechanism. More generally the local p-moment is at least c_p T^((p-2)beta).

At V=c'N^(1/4), the level-set measure is at least cN^(-1/2), of the scale V^-2. The ratio of the competing term TV^-q to V^-2 is of order T^(1-beta(q-2)), which tends to zero by a fixed power. Thus deleting V^-2 is invalid for the coefficient-uniform data, even with sufficiently small epsilon losses. Also 4beta<27/52<3/2, so the block lies inside the polynomial block range used by the candidate. This is a complex aligned-coefficient construction, **not** an example with the actual fixed coefficients r2(n)n^(-3/4)Psi(sqrt(n/T)); it does not refute the arithmetic target.

**Exact frozen-target comparison: PASS.** Write V=T^alpha and compare to T^(29/25)V^-12, retaining both generic terms. Their ratios are
\[
 \frac{V^{-2}}{T^{29/25}V^{-12}}=T^{10\alpha-29/25},
 \qquad
 \frac{TV^{-136/13}}{T^{29/25}V^{-12}}
       =T^{-4/25+(20/13)\alpha}.
\]
The thresholds are respectively alpha=29/250 and alpha=13/125. They obey
\[
 \frac{54}{775}<\frac{13}{125}<\frac{29}{250}<\frac18<\beta.
\]
Consequently the complete generic envelope meets the frozen exponents only up to alpha=13/125; the second term ceases to suffice first. Beyond alpha=29/250 the diagonal term independently fails to imply the target, as the candidate states. In particular the upper allowed range near beta is not covered. This strengthens the detail of the candidate's correct one-term comparison without turning an insufficient upper bound into an arithmetic lower bound.

**Pointwise and scope control: PASS.** The moment gain and q_star comparison are real; the quarter theorem, frozen full distribution, and internal M1/M2/M9 obligations do not follow. No computation, generic alignment, or printed older endpoint is used as evidence to the contrary.

## 6. Dependencies, sources, and exact artifacts used

Repository reads were restricted to:

- `protocol.md`.
- `state/active_campaign.yml` for Round 204, the frozen target, and the 100% analytical restriction.
- `state/proof_obligations.yml`, extracting mathematical premises only from `H1-H3`, `Divisor-bound-elementary`, and `GC-external-Li-Yang-theta-star`. H1-H3 supplied accepted endpoint context; no additional analytical estimate was imported from its historical evidence. No historical evidence file or sibling report was read.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, final hash stated in Section 1. L1 is an explicitly assigned premise. The finite-kernel/exponent-pair proof is not certified by this seam.

Primary standard-function sources checked on 2026-09-26:

- NIST DLMF, [10.9.1](https://dlmf.nist.gov/10.9.E1): the order-zero integral needed for polar disk Fourier transformation.
- NIST DLMF, [10.6.6](https://dlmf.nist.gov/10.6.E6): the derivative relation, specialized to J, nu=1, k=1.
- NIST DLMF, [10.17.3](https://dlmf.nist.gov/10.17.E3) and [10.17(iii)](https://dlmf.nist.gov/10.17.iii): fixed-order positive-real Bessel expansion and remainder justification.

Only a smooth compactly supported periodization, elementary Fourier manipulation, Tonelli/layer cake, the divisor bound, and the assigned accepted pointwise theorem are used in addition to L1. File hash checks and exact rational algebra are bookkeeping, not numerical experimentation. No empirical asymptotic evidence is claimed.

## 7. Recommended state effect

**Promote the scoped reconstruction and moment consequence only after all required independent L1/source/covering reviews for hash 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 are green and the conductor's State Patch validates.** For this seam the verdict is GREEN with no required candidate correction.

Retain the accepted pointwise exponent theta unchanged. Retain the frozen arithmetic distribution and quarter-exponent target as open. Record the generic aligned control only as a limitation of coefficient-uniform methods. The extra alpha=13/125 threshold in this report is a precise envelope comparison, not a new obstruction theorem for actual r2 coefficients.

No graph, proof draft, validation matrix, synthesis, candidate, or successor-round file has been edited. This reviewer stops after the assigned report.
