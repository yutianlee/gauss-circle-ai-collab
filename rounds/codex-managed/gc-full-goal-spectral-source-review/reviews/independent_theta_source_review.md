# Round226 independent theta source/application review

## 1. Result

**GREEN, with the claimant's stated finite scope.** This is a nonauthor review of
`reports/theta_wave_full_frontiers.md` in
`gc-full-goal-spectral-source-review`, final claimant SHA256
`e5e95a4d49ab5220b0533e52a92f6d2fb727d3f4b475ce4813ab3ab698d69c79`.

The two exact source applications, the dimension-three lift and its paid trace/time costs, the complex Poisson identity, damping removal and complete absolute closure are valid. They give no new complete exponent or moment bound. The proposed final real integral is sufficient for quarter and remains unproved. The weak upper certificates are not actual signed lower bounds or exclusions of every possible spectral method. No repair to the frozen claimant is requested.

This review independently derives the application calculations below; it does not re-prove either source's full theorem or certify a new cancellation mechanism.

## 2. Exact hypotheses and source binding

The current primary records show Gan--He--Li--Wu [2502.05973v2](https://arxiv.org/html/2502.05973v2), Theorem1.3, revised4 January2026 with four authors, and Edwin--Lin [2412.05485v1](https://arxiv.org/html/2412.05485v1), Theorem1.1, submitted7 December2024. The [first version record](https://arxiv.org/abs/2502.05973) lists v2 as current; the [second](https://arxiv.org/abs/2412.05485) lists only v1. Neither inspected record displays withdrawal. No other source theorem was audited.

For the first theorem, dimension three gives \(p(3)=10/3\),
\(s_p=1-2/p\), and any \(\sigma<1/p\). The displacement and velocity Sobolev indices are respectively \(1-2/p-\sigma\) and \(-2/p-\sigma\), exactly as quoted. Constants are for a fixed manifold and fixed finite \(p,\sigma\). The theorem does not itself assert the dimension-two compact case, the exact \(\sigma=1/p\) endpoint, or point evaluation.

The second theorem uses the displayed Fourier-quasicrystal identity and polynomial coefficient growth. Its conclusion is
\(\#(\Lambda\cap B_r)=c_0\pi r^2+O(r^{1-1/(2P-1)})\).
For \(\Lambda=S=\mathbb Z^2\), \(c_s=1\), the correct growth exponent is \(P=2\), and the source's ball is closed. Thus the application is uniform through lattice-radius crossings and gives \(P(X)\ll X^{1/3}\), not a quarter bound.

The application throughout retains the fixed actual mollifier, real even Schwartz \(\Psi\), every real \(R\in[cT,CT]\), and the prescribed real rotation. In particular \(\Psi\) is not assumed positive.

## 3. Independent derivation of the application and costs

**Lift and both traces.** Put \(\lambda=\sqrt N\). On the unit flat three-torus, the modes \((m_1,m_2,0)\) have eigenvalues \(4\pi^2|m|^2\). Hence the claimant's \(e(m\cdot x+t|m|)\) solves the wave equation exactly. Grouping at \(x=0\) gives \(r_2(n)\); the coefficients are one per lattice vector, with no arithmetic replacement.

There are \(O(\lambda^2)\) modes in the fixed annulus, each of size
\(O_J(\lambda^{-3/2}E_J)\), where \(E_J=(1+N/T)^{-J}\).
Consequently
\[
 \|F\|_2\ll\lambda^{-1/2}E_J,\qquad
 \|U(t_0)\|_p\ll\lambda^{1-2/p}\|F\|_2
               \ll\lambda^{1/2-2/p}E_J
\]
for every real \(t_0\). The latter is two-dimensional Bernstein on the active variables, not an assertion that evolution preserves the initial \(L^p\) norm. Translation preserves \(L^2\) and the finite frequency support.

For \(\sigma=1/p-\varepsilon\), the theorem charges
\(\lambda^{1-3/p+\varepsilon}\). Initial velocity is
\(i\sqrt{-\Delta}U(t_0)\), so its extra \(\lambda\) cancels its one lower Sobolev index. This gives the unit-time space-time norm
\[
 \|U\|_{L^p_{t,x}}\ll
 \lambda^{3/2-5/p+\varepsilon}E_J.
\]
Reinitializing before each translated unit interval is legitimate with the preceding uniform norm.

Spatial evaluation at zero costs \(\lambda^{2/p}\). To verify temporal evaluation rather than assume it, let \(g(t)=U(t,0)\) on an enlarged bounded interval. The same source estimate applied to \(\partial_tU\) gives
\(\|g'\|_p\ll\lambda\) times the bound for \(\|g\|_p\). The elementary one-dimensional inequality
\[
 \|g\|_\infty\ll_p
 \|g\|_p+\|g\|_p^{1-1/p}\|g'\|_p^{1/p}
\]
therefore costs \(\lambda^{1/p}\). The final power is
\(\lambda^{3/2-2/p+\varepsilon}\), minimized in the available range at
\(p=10/3\), namely \(N^{9/20+\varepsilon}\). At this endpoint the untraced space-time power is zero, but the two point traces remain compulsory.

Without temporal evaluation, the full interval \(R\asymp T\) consists of \(O(T)\) unit intervals, yielding exactly
\[
 \int_{cT}^{CT}|U(t,0)|^pdt
 \ll T\,N^{3p/4-3/2+\varepsilon}E_J^p.
\]
For completeness, Minkowski and Schwartz summation of every block give the whole complex moment price
\(T^{3p/4-1/2+\varepsilon}\), for fixed \(p\ge10/3\), apart from smaller singleton/tail terms. This is an unbounded family of weak estimates, not the required \(T^{5/4+\varepsilon}\) family. Thus the claimant's statement that this route supplies no sufficient unbounded-order family is correct.

Dyadic summation of the point bounds gives complex \(T^{9/20+\varepsilon}\); coefficient triangle gives complex \(T^{1/4+\varepsilon}\). The corresponding physical exponents are \(19/40\) and \(3/8\). The quasicrystal theorem and the accepted bridge give complete real \(T^{1/6+\varepsilon}\). Closed225's complex \(T^{13/56+\varepsilon}\) ceiling gives \(41/112\). All are weaker than the inherited complete real \(T^{\beta+\varepsilon}\); none implies a complex or individual-block \(\beta\) estimate.

**Poisson identity and boundary approach.** For real \(z>0\), Gaussian subordination followed by Gaussian Poisson summation gives
\[
 \sum_{m\in\mathbb Z^2}e^{-z|m|}
 =2\pi z\sum_{k\in\mathbb Z^2}
            (z^2+4\pi^2|k|^2)^{-3/2}.
\]
The \(2\pi\) agrees with the Fourier convention \(e(-x\cdot\xi)\).
For \(\Re z>0\), each denominator is nonzero and has the analytic branch continuing its positive-real value. Both series converge normally on compact subsets: the original side has positive real exponential decay, and the dual tail is \(O(|k|^{-3})\) in dimension two. The identity theorem therefore establishes the claimed continuation. No nearly imaginary substitution into a potentially divergent real-\(t\) subordination integral is made.

The marginal \(h(u)=\int\rho(u,y)dy\) has integral one and
\(\Psi(s)=\int h(u)e(-su)du\). With \(z=s+\delta-2\pi i(R-u/\sqrt T)\), original-side absolute convergence for \(\delta>0\) justifies the interchanges. Integration against \(s^{1/2}/\Gamma(3/2)\) produces
\(|m|^{-3/2}=n^{-3/4}\), with the positive phase \(e(R\sqrt n)\). Subtracting the \(m=0\) term gives exactly the claimant's damped series. The real rotation \(e^{-3\pi i/4}\) matches the actual cosine.

Since \(1-e^{-\delta\sqrt n}\le\delta\sqrt n\),
\[
 |{\cal W}_{T,0}-{\cal W}_{T,\delta}|
 \ll_\varepsilon\delta T^{3/4+\varepsilon}.
\]
Thus \(\delta=T^{-1}\) costs \(T^{-1/4+\varepsilon}\), uniformly in real \(R\). Removing the \(u\)-average before estimating instead removes \(\Psi\) and permits only the displayed absolute \(O(\delta^{-1/2-\varepsilon})\) price. This is not claimed sharp for the signed expression.

**Resonance and both integral/dual tails.** Write \(a=s+\delta\), \(r=R-u/\sqrt T\). For large \(T\), uniformly over the fixed \(u\)-support and \(s\le S\asymp\log T\),
\[
 z^2+4\pi^2m=a^2+4\pi^2(m-r^2)-4\pi iar,
\quad
 |z^2+4\pi^2m|\asymp |m-r^2|+Ta.
\]
The harmless \(a^2\) is bounded by a constant times \(Ta\). Crucially \(Ta\) remains when \(r^2\) is an integer. For every real \(b\) and \(A>0\),
\[
 \sum_{m\in\mathbb Z}(|m-b|+A)^{-3/2}
       \ll A^{-3/2}+A^{-1/2}.
\]
Applying this with \(A=Ta\), numerator \(O(T)\), and
\(r_2(m)\ll_\varepsilon T^\varepsilon\) on the resonant annulus gives precisely
\[
 T^\varepsilon(T^{-1/2}a^{-3/2}+T^{1/2}a^{-1/2}).
\]
The first term owns the nearest integer, including exact resonance. Separated interior and exterior annuli each cost \(O(1)\).
Integrating with \(s^{1/2}\) gives the stated
\[
 T^\varepsilon\big[T^{-1/2}\log(2+S/\delta)
                     +T^{1/2}S+S^{3/2}\big]
 \ll T^{1/2+\varepsilon}.
\]
The finite-interval subtraction of1 is included in \(S^{3/2}\).

For \(s>S\ge1\), the original lattice series bounds the **grouped**
\({\cal P}(z)-1\) by \(O(e^{-s})\), so its integral is
\(O(S^{1/2}e^{-S})\). For \(s\le S\), at the actual
\(\delta=T^{-1}\), \(|z|=O(T)\) and the omitted \(|k|>K\gg T+S\)
dual terms cost \(O(TS^{3/2}/K)\). Choosing fixed powers of \(T\) as in the claimant pays both tails arbitrarily far below target. Bounded \(T\) is absorbed in constants. The isolated constant is never integrated absolutely to infinity.

Finally the original \(n>T^{3/2}\) Schwartz tail costs
\(T^{3/8-J/4+\varepsilon}\), the singleton is \(O(1)\), and a genuine overlapping smooth dyadic partition has bounded multiplicity. These facts complete the wave reconstruction. The boxed claimant target is exactly the whole damped real wave with these paid errors; it is sufficient and unproved.

## 4. First doubtful or unproved step

There is no unchecked applicability step in the two restricted source uses or the representation proved above. The first new analytical demand is the claimant's final boxed **signed** integral estimate at \(T^\varepsilon\), retaining the entire dual sum, the subtraction, the actual \(u\)-average and the final real part together.

Neither modular inversion nor the separate absolute estimate proves this bound. Conversely the \(T^{1/2+\varepsilon}\) absolute certificate does not disprove it. No claim of an established cancellation mechanism is certified.

For local smoothing, the missing improvement concerns the actual rephased input and spatial trace after the uniform norms already paid. The theorem by itself supplies no free point trace, global-in-time constant, or growing-\(p\) uniformity.

## 5. Controls and complete-frontier restoration

All required controls pass within that scope: legal dimension, actual coefficients, fixed translated data norms, both traces, the \(T\) time factor, the nonendpoint Sobolev gain, all real radii, exact resonance, analytic branches, origin subtraction, damping and every tail. There were zero experiments.

The graph's M1 HARD high-radical small-\(t\) residual and independent M1 SMOOTH physical blocks remain separate. M2 TOP's one outer real part at \(L^2X^\varepsilon\), BAL's complete \(G\)-sum at \(L^{3/2}X^\varepsilon\), and UNBAL's actual symbol at \((LK)^{3/4}X^\varepsilon\) are accurately retained. The UNBAL restoration \(X^{1/4}(LK)^{-3/4}\) is consistent.

The displayed GAR coefficient, \(e(1/8)\) rotation and physical multiplier
\(-4X^{1/4}/\pi\) match the accepted graph. Its floors, stars, all lower scales and later lower-owner dependencies are not replaced by \(r_2\). GAR controls total active M1 only, with M2/endpoints still needed; its \(X^{1/12}\) inherited capacity is not a lower bound.

Accepted204 retains both distribution terms \(V^{-2}\) and
\(TV^{-136/13}\), and the resulting two ceiling contributions in high moments. Accepted216 retains the head \(T^{15/13+\varepsilon}\) and repeated-class \(T^{8\beta-1/5+\varepsilon}\) costs. The fixed \(29/25\) twelfth milestone gives only \(102/325\), not quarter.

The full physical moment conversion is correct:
\[
 \int_{Y/2}^{3Y}|P(x)|^pdx
 \ll T^{1+p/2}M_p(B_T)+T^{2+p/2+\varepsilon},\quad Y=T^2.
\]
A complete \(M_p\ll T^{5/4+\varepsilon}\) gives physical integral exponent
\(p/4+9/8\) in \(Y\), and persistence gives
\(1/4+7/[8(p+1)]\). An unbounded sequence of fixed even \(p\), with its fixed-order constants and the accepted \(Q_p=T^{1/p}\) absorption bridge, therefore suffices. No \(p(T)\) substitution or source-proved such family is asserted. The benchmark and every complete owner remain unchanged.

## 6. Dependencies and provenance

I am the author of this round's separate shifted-source report, frozen at
`1bcb14e1899138097a3ab0e273060f2deaa800e3eb732e2924afb2f1f02d25bc`,
and retain rounds217--225 task history. I did not author the theta claimant. This is a post-freeze, nonblind application/source review, not a history-free statement-only task, and does not independently validate my own shifted-source claims.

Exact local dependencies used:

| Artifact | SHA256 |
|---|---|
| Current reports/theta_wave_full_frontiers.md | e5e95a4d49ab5220b0533e52a92f6d2fb727d3f4b475ce4813ab3ab698d69c79 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 3f136e86091b999d4abf7db0b2141f4bced2e80480ee90a360c319c48b6e0d92 |
| Current briefs/conductor_complete_spectral_interfaces.md | 8e9cb720ca0495aafc003434877dcd0067779993fc1edd5657b93d35ef9e77e5 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md | c4324e2b8c75b8cb972ccf6a9e4f762ed9d8d648299acf7df77aff2b9b1546c7 |
| rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md | d5a94b25e876714c8e17602a497812afef3b42724a75dd4cc1501583d12fe98f |

The exact two primary versions and theorem numbers are linked in Section2. Other references appearing in the claimant were not audited or imported. No sibling review, checkpoint or conductor control was read for this review. No claimant, original report, state, synthesis or successor file was edited.

## 7. Recommended state effect

**GREEN for the frozen claimant's two scoped source applications, exact representation, paid upper-bound limitations and conditional implication.** No correction is required.

Retain that evidence; make no change to exponents, moments, M1/M2/GAR owners or quarter status. The complete signed Poisson-integral target remains an explicitly unproved candidate equivalent at the requested strength to the actual real wave up to the paid damping error. It is not a new source gain. Stop after the review hash.

