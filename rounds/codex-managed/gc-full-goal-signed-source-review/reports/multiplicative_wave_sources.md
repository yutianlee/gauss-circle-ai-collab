# 1. Result

Round223, campaign gc-full-goal-signed-source-review; role multiplicative_wave_sources; selected-context source audit, 2026-09-28.

**No complete frontier improves from the two audited source interfaces.** Robles2609.11070v1 does not directly cover \(g=r_2/4\): its required fixed linear mean-square bound fails. Fixed multiplicative damping repairs that premise, but supplies no fixed-power saving at the actual block scale. Granville–Lamzouri2604.02306v1 offers a different large-value mechanism, retaining a large-prime main term, but does not estimate the masked square-root wave or its exceptional frequencies.

This is a rigorous coefficient-premise rejection and a scoped transfer audit, not a counterexample to either source, the actual signed moment, or the quarter conjecture. Section7 recommends one complete, exactly source-compatible signed spectral inequality. It remains unproved; no successor task is started.

# 2. Exact statements and hypotheses

Write \(e(t)=\exp(2\pi it)\). The actual accepted204/216 normalization is
\[
a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\qquad
B_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4).
\]
Here \(T\ge2\) is real; \(\Psi(s)=\widehat\rho(se_1)\) for the fixed nonnegative radial unit-mass smooth compactly supported mollifier; \(w\ge0\) is the fixed smooth radius window from216. In particular, \(\Psi\) is real even Schwartz, \(|\Psi|\le1\), but need not be nonnegative. Let \(\operatorname{sf}(n)\) denote the squarefree part and \(m_Q(n)=1_{\operatorname{sf}(n)>Q}\). All harmonics, both cosine signs, unequal and mixed dyadic blocks, and real radii in the complete window are retained.

**Source interface R.** [Robles, v1](https://arxiv.org/html/2609.11070v1), Theorem1.1/Corollary1.1 and their exceptional-set consequence §7.2:
\[
\mathcal F_A=\{f\text{ multiplicative}:f(1)=1,\ |f(p)|\le A,\
 \sum_{n\le x}|f(n)|^2\le A^2x\ (x\ge1)\}.
\]
For \(N\ge3,\ L=\log N,\ Q_0=N/L^3,\ (a,r)=1,\ 1\le r\le Q_0\),
\[
\alpha=a/r+b,\quad |b|\le(rQ_0)^{-1},\quad B=\max(1,N|b|):
\quad |S_f(N,\alpha)|\le C(A)\{N/L+N/\sqrt{\varphi(r)B}\}.
\]
Alternatively, \(|\alpha-a_0/q|\le q^{-2},\ (a_0,q)=1,\ 3\le H\le q\le N/H\) gives
\[
|S_f(N,\alpha)|\ll_A N/L+NH^{-1/2}\sqrt{\log\log(3H)}.
\]
The simultaneous set \(\mathcal E_A(N,\lambda)=\{\alpha:\exists f\in\mathcal F_A,\ |S_f|>\lambda N\}\) has
\[
|\mathcal E_A|\le K_A/(N\lambda^4),\qquad c_A/L\le\lambda\le1.
\]
One can take \(c_A=\max(6,2C(A))\), \(K_A=2C_\varphi(2C(A))^4\). Constants are computable, not numerically supplied; no exceptional real character is excluded. The [current record](https://arxiv.org/abs/2609.11070) has only v1, 10 September2026, without withdrawal.

**Source interface GL.** [Granville–Lamzouri, v1](https://arxiv.org/html/2604.02306v1), Theorem1.1/Corollary1.1. For sufficiently large \(x\), multiplicative \(|f|\le1\), fixed \(0<\delta<1/10\), coprime \(a,q\),
\[
|\alpha-a/q|\le(qx)^{-1},\qquad
(\log x)^{2+\delta}\le q\le x/(\log x)^{3+\delta},\quad
\mathcal L=\exp\sqrt{\log x\log\log x},
\]
put \(P_M=\sum_{m\le M}f(m)\sum_{x/M<p\le x/m}f(p)e(mp\alpha)\). Then
\[
S_f(x,\alpha)=P_M+
\begin{cases}
O_\delta(x/(\sqrt M\log x)),&q\le x^{1-\delta},\\
O_\delta(x\sqrt{\log M}/(\sqrt M\log x)),&q\ge x^{1-\delta},
\end{cases}
\]
respectively for integers \(M\ge2\) bounded by constant multiples of
\[
\min\{q^{1-\delta/4}/(\log x)^2,\mathcal L^{1/2-\delta}\},
\quad
\min\{\sqrt{x/q}/\log x,\ x/[q\log(2x/q)(\log x)^3],\mathcal L^{1-\delta}\}.
\]
At fixed \(0<c<1\), \(|S_f|\ge cx/\log x\) forces a prime-block bias, for
\[
h\ll c^{-2}\log(1/c),\quad c^2x/\log(1/c)\ll z\le x/(2h),\quad
\left|\sum_{z<p\le2z}f(p)e(hp\alpha)\right|\gg
\frac{c^3z}{\log(1/c)\log z}.
\]
The [current record](https://arxiv.org/abs/2604.02306) has only v1, 2 April2026, without withdrawal. No introductory conjecture is imported.

These are two theorem interfaces, with the displayed corollaries audited as their consequences; there is no third full audit.

# 3. Proof and complete cost ledger

**The actual coefficient obstruction.** Since \(g=1*\chi_4\), its prime-power values are
\[
g(2^k)=1,\qquad g(p^k)=k+1\ (p\equiv1\bmod4),\qquad
g(p^k)=1_{2\mid k}\ (p\equiv3\bmod4).
\]
Thus \(|g(p)|\le2\), but, for real \(s>1\),
\[
D(s):=\sum_{n\ge1}\frac{g(n)^2}{n^s}
=\frac{\zeta(s)^2L(s,\chi_4)^2}{\zeta(2s)(1+2^{-s})}.
\tag{1}
\]
Indeed the respective local factors are \((1-z)^{-1}\), \((1+z)/(1-z)^3\), and \((1-z^2)^{-1}\), \(z=p^{-s}\). Since \(L(1,\chi_4)=1-1/3+1/5-\cdots=\pi/4\), (1) has
\[
\lim_{s\downarrow1}(s-1)^2D(s)=1/4.
\]
If \(\sum_{n\le x}g(n)^2\le A^2x\) held with fixed \(A\), Abel summation would give \(D(s)\le A^2s/(s-1)\), a contradiction. This uses no conjectural mean-square asymptotic.

For an upper ledger, write \(D=(\zeta L)^2H\), \(H=[\zeta(2s)(1+2^{-s})]^{-1}\). Its coefficients satisfy \(\sum|h(d)|/d<\infty\). The elementary disk count gives \(\sum_{n\le x}g(n)\ll x\), hence
\(\sum_{n\le x}(g*g)(n)\ll x\log(2x)\), and convolution yields
\[
\sum_{n\le x}g(n)^2\ll x\log(2x).
\tag{2}
\]
A length-dependent mean-square constant inferred from (2) is not membership in a fixed global \(\mathcal F_A\). Nor has a permitted growth rate for \(C(A_N)\), all thresholds, and exceptional constants been proved here.

Consequently the actual dyadic coefficients, also after masking, satisfy
\[
\sum_{N<n\le2N}|a_n(T)|\ll_J N^{1/4}(1+N/T)^{-J},\qquad
\sum_{N<n\le2N}|a_n(T)|^2\ll_J N^{-1/2}\log(2N)(1+N/T)^{-J}.
\]
These are upper norms, not a cancellation estimate for their prescribed phases.

**Two legal damping alternatives.** For any fixed \(\eta>0\),
\(f_\eta(n)=g(n)n^{-\eta}\) is multiplicative and belongs to some fixed \(\mathcal F_{A_\eta}\). For \(0<\eta<1/2\), dyadic summation in (2) bounds its mean square by
\(O_\eta(x^{1-2\eta}\log(2x))=O_\eta(x)\); larger \(\eta\) follows by domination. Prime values remain at most2. Constants may depend on this fixed \(\eta\); choosing it to vanish with \(T\) is not authorized.

In a favorable *linear-phase* dyadic block, partial summation restores the weight \(n^{-3/4+\eta}\Psi(\sqrt{n/T})\). If \(3\le H\le q\le N/H\) and the corollary's approximation holds, it holds for every prefix length \(u\in[N,2N]\), so
\[
\left|\sum_{N<n\le2N}g(n)n^{-3/4}\Psi(\sqrt{n/T})e(n\alpha)\right|
\ll_{\eta,J}N^{1/4+\eta}(1+N/T)^{-J}
\left\{\frac1{\log N}+\frac{\sqrt{\log\log(3H)}}{\sqrt H}\right\}.
\tag{3}
\]
Bounded \(N\) is paid trivially. The multiplier and its total variation are
\(O_{\eta,J}(N^{-3/4+\eta}(1+N/T)^{-J})\). Even its first term supplies no fixed-power saving. Selecting a small fixed \(\eta\) after the requested epsilon is legal; treating \(1/\log N\) as \(N^{-\sigma}\) is not.

The alternative \(f_{3/4}=gn^{-3/4}\) is actually 1-bounded: for \(p\equiv1\bmod4\),
\(k+1\le2^k\le p^{3k/4}\), and all other prime factors are at most1. Both source coefficient premises then hold. Their generic length-scale term, however, exceeds the actual dyadic absolute mass \(O(N^{1/4})\). Multiplication by \(N^{3/4}\) does not repair this: it breaks the normalization \(f(1)=1\) and multiplicativity. For small \(\eta<\log2/\log5\), \(f_\eta(5)>1\), so the useful small damping from (3) is not in GL's class.

**Mask and nonlinear transfer.** The mask is not multiplicative. For \(Q\ge2\), choose an odd prime \(p\equiv1\bmod4\), \(p>Q\): the masked coefficient vanishes at2 but not at \(p\) or \(2p\). Also \(m_Q(1)=0\). Its arithmetic jumps have not been given a bounded-variation multiplier norm. Smooth \(\Psi\) can be paid as in (3); this does not grant the squarefree mask. Subtracting the complete small-class wave \(L_Q\) is legal only with its accepted cost.

The phase is \(R\sqrt n\), not \(n\alpha\). On an interval of length \(M\) around \(n_0\asymp N\), tangent subtraction leaves variation on the scale \(TM^2N^{-3/2}\). Bounded residual variation therefore requires \(M\lesssim N^{3/4}T^{-1/2}\). When that length is at least1, as many as \(T^{1/2}N^{1/4}\) pieces arise; otherwise singleton partitioning already exhausts the sum. Translating \(n=n_0+m\) does not preserve multiplicativity, so the source length cannot become \(M\). This is a diagnostic of the missing transfer, not a new round220 result. No arbitrary-vector phase-deletion or continuous-to-discrete norm grant is made.

The prime-main-term identity cannot remove this problem. At permitted subpower \(M\), its very large prime factor has a unique complementary factor, so the retained main term is meaningful, but it is still an oscillatory sum requiring estimation. Even the largest allowed \(M\) only makes its generic remainder \(x^{1-o(1)}\), rather than \(x^{1-\sigma}\) for fixed \(\sigma>0\). Applying the source to \(\chi_4\) after \(g=1*\chi_4\) leaves all complementary divisors, the phase \(R\sqrt{ab}\), and the actual mask. None is free.

**Exceptional and complementary frequencies.** For interface R, the exceptional-set control is with respect to \(\alpha\) on the unit circle. Even with a legal fixed coefficient, bounding its bad part by the trivial \(AN\) gives the explicit price
\[
\int_{\mathcal E_A}|S_f(N,\alpha)|^p\,d\alpha
\le A^pK_A N^{p-1}\lambda^{-4}.
\]
At \(\lambda=c_A/\log N\), the good part is bounded by
\(c_A^pN^p/(\log N)^p\), and the bad part by
\(O_{A,p}(N^{p-1}(\log N)^4)\). Neither estimate is an \(R\)-measure statement for the nonlinear wave. In a signed kernel representation the required bad contribution is \(\int_{\mathcal E_A}S_fK\,d\alpha\), not its unweighted measure. Without a kernel estimate it remains in full.

For GL, the complementary rational-denominator ranges, especially fixed small moduli, remain. In the \(\chi_4\) convolution, an exact control is
\[
\sum_{n\le x}\chi_4(n)e(n/4)=i\,\#\{n\le x:n\text{ odd}\}
=ix/2+O(1).
\]
Thus deleting the modulus4 region as negligible is already false for a legitimate linear factor. This is not a lower bound for the complete radial sum. Conversely, the physical level \(T^\beta\) at a block \(N\asymp T\) is far below \(cN/\log N\) for fixed \(c>0\) in the \(f_{3/4}\) normalization. Sending \(c\) to zero with \(N\) without paying all dependencies would not supply the missing implication.

**Full physical restoration.** Put \(q_*=136/13\) and
\(\beta=2\theta_{\rm LY}-1/2\), with the accepted qualified Li–Yang input. For fixed \(p>q_*\), accepted204 retains
\[
M_p(B_T)\ll T^\epsilon
\{T+W^{p-2}+TW^{p-q_*}\},\qquad W\ll T^{\beta+\epsilon}.
\tag{4}
\]
Below level1 use measure \(O(T)\); at \(p=q_*\) the last integral is logarithmic, and for \(p<q_*\) it is bounded. At \(p=12\), neither \(W^{10}\) nor \(TW^{20/13}\) can be removed by this audit. With \(V_0=T^{13/125}\), the corresponding low-end prices are \(V_0^{10}=T^{26/25}\) and \(TV_0^{20/13}=T^{29/25}\). The surviving ceiling terms prevent the milestone.

Accepted216 pays \(M_{12}(L_Q)\ll T^{15/13+\epsilon}\) and
\[
|M_{12}(Z_Q)-I_{12}(T,Q)|\ll T^{8\beta-1/5+\epsilon},
\qquad Q=\lfloor T^{2/5}\rfloor.
\]
Thus the one-sided signed target \(I_{12}\le T^{29/25+\epsilon}\) is complete, but would yield only \(102/325\).

For the quarter goal a sufficient family is, for an unbounded sequence of fixed even \(p\),
\[
Q_p=\lfloor T^{1/p}\rfloor,\qquad
I_p(T,Q_p)\le C_{p,\epsilon}T^{5/4+\epsilon}.
\tag{5}
\]
The class mass estimate \(A_d\ll r_2(d)d^{-3/4}\) implies
\(\sum_{d>Q_p}A_d^j\ll Q_p^{1-3j/4+\epsilon}\), \(j\ge2\).
Expanding the distinct-class identity, every repeated partition contains such a power sum and a lower power of the *same* \(Z\). Young's inequality absorbs that lower power into a small multiple of \(M_p(Z)\); the remaining terms cost \(O_{p,\epsilon}(T^{1+\epsilon})\). Also \(M_p(L_{Q_p})\ll TQ_p^{p/4}=T^{5/4}\). Hence (5) suffices without estimates at every intermediate order. Constants may depend on fixed \(p\), but no \(p(T)\) is asserted.

Restoring amplitude and \(dx=2R\,dR\) costs
\[
\int_{Y/2}^{3Y}|P(x)|^pdx
\ll T^{1+p/2}M_p(B_T)+T^{2+p/2+\epsilon},\qquad Y=T^2.
\]
A bound \(M_p\ll T^{5/4+\epsilon}\), followed by the accepted one-sided persistence argument, gives pointwise exponent
\[
\frac{5/4+1+p/2}{2(p+1)}
=\frac14+\frac7{8(p+1)}.
\]
Arbitrarily large *fixed* orders therefore suffice; the twelfth milestone alone does not.

# 4. First doubtful or unproved step

For undamped \(g\), the first source premise is false by (1). After legal damping, the first missing application is a quantitatively useful signed transfer from the linear source to the full actual square-root phase and large-class mask, including its exceptional frequencies. The exact formula in Section7 supplies an identity, not its requisite estimate.

For the second interface, the original \(g\) is not 1-bounded. Damping enough to enter that class gives the wrong generic normalization. Even were this repaired, estimating the retained prime contribution, its smooth complement, and all omitted rational regimes in the complete physical norm is unproved.

There is no actual signed-wave lower bound here. Failures of generic constants, an absolute transfer, a positive certificate, or a rephased vector do not rule out an arithmetic signed cancellation mechanism.

# 5. Required controls and outcomes

All controls are analytical; zero experiments.

| Control | Outcome |
|---|---|
| Current primary versions | Both exact v1 texts and live arXiv histories checked; no withdrawal shown. |
| Actual coefficient class | Prime bound passes for \(g\); fixed linear mean square fails. Fixed damping is legal with its displayed costs. |
| Phase, norms, mask | Actual \(\sqrt{n/T}\) mollifier scale and \(R\sqrt n\) phase retained. No multiplicative mask, translated coefficient, or free row/phase multiplier. |
| Major and exceptional frequencies | Modulus4 control survives; all source-exceptional and out-of-range regions remain inside the signed quantity. |
| Infinite tails and mixed blocks | With cutoff \(H_T=\lfloor T^{3/2}\rfloor\), accepted204 gives masked absolute tail \(O_A(T^{-A})\). The singleton, partial terminal block and \(O(\log T)\) blocks remain; fixed-\(p\) norm inequalities cost only logarithmic powers. No diagonal-only truncation. |
| Full powers | Both terms in (4), head/repeated-class costs and sharp reconstruction are retained. No logarithmic gain is counted as a fixed-power gain. |
| Actual versus enlarged scope | Closed221 phase-blind certificate floors and closed222 unrestricted Fourier/rectangle prices are not actual signed lower bounds; no such claim is reused here. |
| Fixed-order scope | Same-order absorption suffices at an unbounded sequence of fixed even orders. No growing-order constants or intermediate-order bootstrap assumed. |

Every full-proof alternative remains available, with no new estimate from these sources:

| Complete owner | Retained target and scope |
|---|---|
| M1 HARD | Actual \(\chi_4(n)\) cone \(4h<n<16h\), \(h\asymp L\), phase \(e(\sqrt{Xhn})\), target \(L^{3/2}X^\epsilon\); all original near-resonant, small-\(G\), large-\(G\), \(t=1\) and \(t\ge2\) pieces. |
| M1 SMOOTH | Every physical \(B_1(D,L;X)\ll X^{1/4+\epsilon}\), with original profiles, floors and stars. The recorded critical \(X^{1/3}\) price still has \(X^{1/12}\) deficit. |
| M2 TOP | Full outer real combination \(E_{\rm top}=E_{\rm owned}+2\Re C_{\rm comp}\), requiring \(\Re C_{\rm comp}\ll L^2X^\epsilon\), with literal endpoints; no replacement by separate absolute summands. |
| M2 BAL | Complete \(|\sum_G GP_G|\ll L^{3/2}X^\epsilon\), all \(1\le K/L\le16\), actual symbol, quarter shifts and boundary companions. |
| M2 UNBAL | Actual \(\sum_{h\asymp L,k\asymp K}\chi_4(h)a(h,k)e(\sqrt{Xhk})\ll(LK)^{3/4}X^\epsilon\), \(K=XL/D^2\), \(K/L>16\). Restore \(X^{1/4}(LK)^{-3/4}\) and the owned smooth transform error. Strict flat identities do not discharge hard endpoints. |
| GAR / whole moment | GAR retains its actual total angular coefficient \(C_X^*(n)\), the real phased sum through \(16\sqrt X\), all M2 and endpoint companions. That coefficient is not \(r_2\). The independent complete moment route retains (5). |

All \(X,D,L,K,R\) are in their original real ranges; a source for unrestricted multiplicative linear sums does not close any table row. The anchored divisor-energy option likewise retains the actual sine/character weights, moving cutoffs and every \(R_j^2/a\pm R_\ell^2/b-m\) alias. Neither audited interface estimates that complete energy. No new standalone angular, flat, or small-denominator fragment is counted as frontier progress.

# 6. Dependencies, exact artifacts and provenance

This is NONBLIND selected-context literature/application review. The agent slot retains rounds217–222 history, including earlier finite statement-only and subsequent application reviews. It is not a fresh history-free agent. No current sibling report, current blind packet, or unlisted application was read. Primary-source theorem statements were checked directly rather than accepted from the conductor's lead. Two full source interfaces were audited; preliminary nonlinear/random-model screens yielded no additional imported theorem.

Exact local SHA256 values at review time:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 6cc4fe7f244bfde385951ab4c4450a5f9c1360686970427df8610c2745cc74f4 |
| strategy/round223_full_goal_signed_source_review.md | 0eb762f10cd11866047cf4974251ca0a8f3bdaa76076d7b54e6a80cbf2eac5be |
| strategy/gauss_circle_strategy_review_2026-09-23.md | 0729f1d9c596867e7a06bdcd096847b32e6747653235706b01275a153bd617c6 |
| strategy/gauss_circle_strategy_checkpoint_round220_2026-09-28.md | 6fc4b67a5de62a449527f62877933856635a9f6b0501a45f63539f05de6a5460 |
| rounds/codex-managed/m9-m2-complete-unbalanced-vector/synthesis.md | 829f1ed9af8ca637345332028707723b5bce22cb7268238f40a1a1a9bcc64377 |
| rounds/codex-managed/gc-actual-vector-gram-correlations/synthesis.md | 93413bbc466cd48bc9fe4ebeede40c62bb218bb077f8afda1750c23805fb05dd |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/full_frontier_sources.md | 76343a1c8b33a9764b3498bf3fa8d919466d4476296ba4f9035ea6e3a6341ba0 |
| rounds/codex-managed/gc-full-goal-signed-source-review/briefs/multiplicative_wave_sources.md | c50be6f37a28aa7e98da90cac70ba8e98b8986353a11f08af77ba2d5f5f77ad5 |

External dependencies are precisely the linked versioned primary texts and their status pages in Section2. Arithmetic calculations (1)–(3), the mask control and the following spectral identity were derived here. Accepted204/216 supply only their stated physical, tail and finite-power interfaces. No source theorem or report is promoted merely by citation.

# 7. Recommended state effect and one complete next inequality

**Retain** the coefficient obstruction and the two scoped source audits as evidence; **reject** a direct undamped Robles import and any free damping, masking, nonlinear-phase or exceptional-set transfer. **No change** to accepted exponents, moments, M1/M2/GAR, endpoints or quarter status.

If this source direction is pursued, the complete reviewable target should be the following single family, not another isolated minor-arc estimate. Fix once and for all \(0<\eta<1/10\), put \(H_T=\lfloor T^{3/2}\rfloor\), and define
\[
F_{\eta,H_T}(\alpha)=\sum_{n\le H_T}g(n)n^{-\eta}e(n\alpha),
\]
\[
K_{T,R,Q}(\alpha)=
\sum_{n\le H_T}m_Q(n)n^{-3/4+\eta}\Psi(\sqrt{n/T})
 \cos(2\pi R\sqrt n-3\pi/4)e(-n\alpha).
\]
The factor \(F_{\eta,H_T}\) is exactly a legal Robles coefficient prefix. Orthogonality, with no absolute-value transfer, gives
\[
Z_Q(R)=4\Re\int_0^1F_{\eta,H_T}(\alpha)K_{T,R,Q}(\alpha)\,d\alpha
+O_A(T^{-A}).
\tag{6}
\]
The recommendation is to prove, for an unbounded sequence of fixed even \(p\),
\[
\boxed{\displaystyle
\int_{\mathbb R}w(R/T)
\left[4\Re\int_0^1F_{\eta,H_T}(\alpha)
 K_{T,R,\lfloor T^{1/p}\rfloor}(\alpha)\,d\alpha\right]^p dR
\ll_{p,\epsilon,\eta}T^{5/4+\epsilon}.}
\tag{7}
\]
Every exceptional, major-arc, transition and minor-arc contribution and all mixed products stay inside this same real power. The kernel keeps the complete mask and both signs; no \(\|K\|_1\) estimate is implied. Thus (7) is source-compatible without pretending that its full kernel is multiplicative. It is an exact change of representation, **not an established improvement or a demonstrated new cancellation mechanism**.

For completeness, \(\|Z_Q\|_\infty\ll T^{1/4+\epsilon}\) follows by the actual absolute coefficient mass. In (6), choosing fixed \(A>(p-1)/4+2\) makes the moment error harmless. The omitted small-class moment costs \(TQ^{p/4}\le T^{5/4}\), so (7), including its entire frequency complement, would yield the full physical family and the pointwise restoration in Section3. A future attempt must either prove (7) with these costs or record its first failure; another logarithmic bound for \(F\) alone is insufficient. The conductor owns whether to attempt it. Stop after this report.
