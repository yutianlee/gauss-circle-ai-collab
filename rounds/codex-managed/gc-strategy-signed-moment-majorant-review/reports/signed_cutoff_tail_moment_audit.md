# Round 202: signed cutoff and full-tail moment audit

Campaign: gc-strategy-signed-moment-majorant-review. Task: signed_cutoff_tail_moment_audit. Role: discovery; selected-context access. Generated: 2026-09-23. Candidate evidence only. Starting graph SHA-256, independently checked: 682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c. This resumed task independently verifies the conductor's unaccepted interim observations. No sibling report was read. Only this assigned report was written. Effort was analytical/algebraic and primary-source inspection; no numerical experiment was performed.

## 1. Result: a complete cutoff interface and a restricted interpolation no-go

Write \(H_T=A_{T,U}+B_{T,U}\), where the actual fixed coefficients with \(n\le U\) form \(A_{T,U}\), and **every** coefficient with \(n>U\) forms \(B_{T,U}\). There is a rigorous, conservative cutoff
\[
 U=\lfloor T^{1/2047}\rfloor
 \tag{1}
\]
at which
\[
 \int w(R/T)|A_{T,U}(R)|^{12}\,dR\ll T.
 \tag{2}
\]
The proof treats all signs, repeated indices, dependent squareclasses, perfect squares, and all exact resonances. It does not assume that twelve radicals generate a field of degree \(4096\).

At this cutoff the entire outstanding estimate is the signed nonzero-frequency sum with \(\max n_j>U\), defined in (18). A sufficient target is
\[
 |\mathcal C_{12}(T,U)|\ll_\varepsilon T^{1+2\eta+\varepsilon},
 \qquad 0\le\eta<13\theta_{LY}-4.
 \tag{3}
\]
This includes all mixed head/tail strata. Alternatively, the full physical-tail moment \(\int w|B_{T,U}|^{12}\ll T^{1+2\eta+\varepsilon}\) suffices, with all mixed terms then controlled by Hölder.

The audited lower-order residual mechanism supplies no improvement over
\[
 \eta_0=(12-q_0)(\theta_{LY}-1/4)
       =\frac{62}{27}(\theta_{LY}-1/4),\qquad q_0=\frac{262}{27}.
 \tag{4}
\]
Even granting the favorable residual \(q_0\)-moment throughout any contemplated range \(U=T^u\le T\), interpolation from the residual second moment and inherited supremum produces no exponent below \(1+2\eta_0\). This is a no-go for that specified interpolation mechanism, not a lower bound for the true twelfth moment. At (1), the favorable residual \(q_0\) endpoint follows directly from (2) and the printed full-circle benchmark, so the comparison is an actual complete bound there.

## 2. Exact statement and hypotheses

Use the inclusive discrepancy
\[
 P(x)=\#\{m\in\mathbb Z^2:|m|^2\le x\}-\pi x,\qquad T=\sqrt Y.
\]
The radial mollifier and fixed window are exactly those in the permitted Round-201 analytic report: \(\rho\ge0\), radial, smooth, compactly supported, integral one; \(\Psi(s)=\widehat\rho(se_1)\) is real, even and Schwartz, with \(|\Psi|\le1\); \(w\ge0\) is smooth, compactly supported in fixed \([c,C]\subset(0,\infty)\), and equals one on the radius window needed for reconstruction. Neither \(w\) nor the coefficients vary with \(R\). Set
\[
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\quad
 H_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4),
\]
\[
 A_{T,U}(R)=\sum_{n\le U}a_n(T)\cos(2\pi R\sqrt n-3\pi/4),
 \qquad B_{T,U}=H_T-A_{T,U}.
 \tag{5}
\]
Unless stated otherwise \(1\le U\le T\) is an integer. Put \(d\mu_T(R)=w(R/T)dR\), a positive measure of mass \(T\|w\|_1\). Moment exponents, functions, and cutoff powers are fixed; constants may depend on them and \(\varepsilon\), but not on real \(T,R\).

The accepted graph input is the repaired real-variable bound with
\[
 \theta=\theta_{LY}=\frac{3292+25\sqrt{1717}}{13762},\qquad
 \beta=2\theta-\frac12>0.
 \tag{6}
\]
The full exact-resonance mass is controlled by the accepted node GC-weighted-square-root-exact-resonance-mass. The complete smoothing identity remains the specific Round-201 interface,
\[
 P(R^2)=\frac{\sqrt R}{\pi}H_T(R)+O_\varepsilon(T^{1/2+\varepsilon})
 \quad(R\asymp T).
 \tag{7}
\]
Its hypotheses and errors are inherited explicitly; this report does not promote that candidate interface by citation alone.

The printed circle absolute-moment input is
\[
 \int_1^X|P(x)|^{q_0}dx\ll_\varepsilon X^{1+q_0/4+\varepsilon}.
 \tag{8}
\]
Equation (8) is the Round-201 source-reviewed benchmark, freshly checked below. No new endpoint is obtained by inserting \(\theta\) into an uninspected source argument.

## 3. Proof, derivation, and source audit

### 3.1. Actual coefficients, full infinite tails, and the residual second moment

For each fixed \(\kappa>0\), \(r_2(n)\le4d(n)\ll_\kappa n^\kappa\) gives
\[
 \sum_n|a_n(T)|\ll T^{1/4+\kappa},\quad
 \sum_{n\le U}|a_n(T)|\ll U^{1/4+\kappa},\quad
 \sum_{n>U}|a_n(T)|^2\ll_\kappa U^{-1/2+2\kappa}.
 \tag{9}
\]
For a temporary upper cutoff \(V\ge T\), Schwartz decay gives
\[
 \sum_{n>V}|a_n(T)|\ll_{\rho,L,\kappa}
 T^{L/2}V^{1/4+\kappa-L/2}.
 \tag{10}
\]
Choose fixed \(0<\alpha<1\) and \(V=\lfloor T^{1+\alpha}\rfloor\), adjusting bounded values if needed. Taking \(L\) sufficiently large makes (10) \(O(T^{-K})\) for any prescribed fixed \(K\). Any twelfth-product integral with at least one discarded index has absolute total at most
\[
 C T\left(\sum_n|a_n|\right)^{11}
       \left(\sum_{n>V}|a_n|\right)
 \ll T^{15/4+11\kappa-K}.
 \tag{11}
\]
This controls all infinite head/tail expansions and mixed strata. A cutoff at \(n=T\) alone has no such justification.

For the second moment of \(B_{T,U}\), expand the cosines through \(V\). Its diagonal is \((T/2)\widehat w(0)\sum_{U<n\le V}a_n^2\). For distinct \(m,n\le V\),
\[
 T|\sqrt m-\sqrt n|\ge\frac{T|m-n|}{2\sqrt V}
 \gg T^{(1-\alpha)/2}|m-n|.
\]
The absolute difference-frequency kernel has row sums \(O(T^{-L(1-\alpha)/2})\) for any sufficiently large fixed \(L\). Using \(2|a_ma_n|\le a_m^2+a_n^2\), the offdiagonal is bounded by this row sum times \(T\sum_{n>U}a_n^2\). Sum frequencies satisfy \(\sqrt m+\sqrt n\ge2\), so their contribution is rapidly small by Fourier decay and (9). Restore (10). Uniformly for \(1\le U\le T\), for each fixed \(K>0\),
\[
 \int |B_{T,U}|^2d\mu_T
 =\frac T2\widehat w(0)\sum_{n>U}a_n(T)^2+O_K(T^{-K})
 \ll_\varepsilon T^{1+\varepsilon}U^{-1/2}.
 \tag{12}
\]
This proves the physical mollified-tail estimate independently of any divisor-to-circle transfer.

From (7), the accepted pointwise bound, and (9),
\[
 \|H_T\|_{\infty,[cT,CT]}\ll_\varepsilon T^{\beta+\varepsilon},
 \quad
 \|B_{T,U}\|_{\infty,[cT,CT]}
 \ll_\varepsilon T^\varepsilon(T^\beta+U^{1/4}).
 \tag{13}
\]
The \(U^{1/4}\) cost must be retained when subtracting the head.

### 3.2. Separation with dependent radicals and perfect squares

Fix twelve positive integers \(n_j\le U\) and a nonzero signed difference \(\Delta=\sum_j\sigma_j\sqrt{n_j}\). Form the polynomial over formal variables
\[
 F(z;x_1,\ldots,x_{12})
 =\prod_{\epsilon\in\{-1,1\}^{12}}
       \left(z-\sum_{j=1}^{12}\epsilon_jx_j\right).
\]
It has integer coefficients and is invariant under each independent \(x_j\mapsto-x_j\), since this permutes its factors. Every monomial therefore has even exponent in every \(x_j\), so
\[
 F(z;\sqrt{n_1},\ldots,\sqrt{n_{12}})\in\mathbb Z[z]
\]
is monic of degree \(4096\). This uses formal sign permutations, not nonexistent independent field automorphisms for dependent radicals.

Let \(z^m\) be the largest zero-root factor. Dividing by it gives a monic integer polynomial \(Q(z)\) with \(Q(0)\ne0\). Its remaining roots, with multiplicity, are the nonzero signed sums; their number \(D\) satisfies \(2\le D\le4096\). Global sign reversal retains two distinct roots \(\Delta,-\Delta\), even when other sums coincide or vanish. Every root has modulus at most \(M=12\sqrt U\). Thus
\[
 1\le|Q(0)|\le|\Delta|^2M^{D-2}
                \le|\Delta|^2M^{4094},
 \qquad |\Delta|\ge(12\sqrt U)^{-2047}.
 \tag{14}
\]
This includes rational roots, repeated indices, all squares, and dependencies such as \(\sqrt8=2\sqrt2\). A field-degree bound alone would not justify the paired small factors or nonzero integer constant; the polynomial supplies both.

Expand \(A_{T,U}^{12}\) with all signs. Its exact part is \(O(T)\) by the accepted resonance node applied after hard support restriction. For fixed \(L>0\), (14), Fourier decay and (9) give the **absolute bound for the head alone**
\[
 |\mathcal O_{\le U}(T)|
 \ll_{\varepsilon,L}T U^{3+\varepsilon}
       (1+c_{12}TU^{-2047/2})^{-L},
 \qquad c_{12}=12^{-2047}.
 \tag{15}
\]
At (1), \(TU^{-2047/2}\ge T^{1/2}\), so (15) is \(O(T^{-K})\) for any fixed \(K\) on taking \(L\) sufficiently large. This proves (2). More generally every fixed \(U=\lfloor T^u\rfloor\), \(0<u<2/2047\), works; the boundary \(u=2/2047\) is not covered by this conclusion.

### 3.3. What the primary residual source provides

Zhai, *On higher-power moments of \(\Delta(x)\) (II)*, Acta Arith. **114** (2004), 35–54: [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83024), [arXiv v1](https://arxiv.org/pdf/0805.1270v1). Lemma 4.2, journal p.49, states for its sharp residual \(R_2\), squared-radius scale \(X\), and \(2<A<A_0\),
\[
 \int_X^{2X}|R_2(x)|^A dx
 \ll X^{1+A/4+\varepsilon}
 U^{-(A_0-A)/(2(A_0-2))},
 \quad X^\varepsilon\le U\le X^{1/(2b(K_0))},
 \tag{16}
\]
where \(K_0\) is the least even integer at least \(A_0\), and \(b(k)=2^{k-2}+(k-6)/4\). The proof interpolates second and \(A_0\) moments. Equations (4.18)–(4.19) enlarge the cutoff to \(X^{1/3}\) at \(A_0=184/19\), with large-values details omitted. The circle Theorem 3 requires \(k<A_0\). Its (5.1) incorrectly prints frequency \(4\pi\sqrt{nx}\); that display is not imported. The [record](https://arxiv.org/abs/0805.1270) lists only v1 and no withdrawal.

Tsang–Zhai, *Sign changes of the error term in Weyl's law for Heisenberg manifolds*, Trans. AMS **364** (2012), 2647–2666, [published PDF](https://hub.hku.hk/bitstream/10722/156281/1/Content.pdf), Section 1.1, (1.5) and the next sentence, explicitly supply (8). Their flat-torus error is \(R_I(t)=P(t/(4\pi^2))\), as follows from their eigenvalues \(4\pi^2(m^2+n^2)\). The endpoint is fixed \(q_0=262/27\); their other Heisenberg results are not used.

The original source trail is Ivić, *The Riemann zeta-function* (1985), Theorem 13.12, and Ivić, *Large values of certain number-theoretic error terms*, Acta Arith. **56** (1990), 135–159, [official record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/56/22/106579/large-values-of-certain-number-theoretic-error-terms), DOI 10.4064/aa-56-2-135-159. The latter's official download returned HTTP 403. The original full large-values proofs were not rederived or certified. This limitation cannot support an enlarged circle endpoint or residual theorem; the argument below needs neither.

The conversion for (16) is \(X=T^2\), \(x=R^2\), \(dx=2R\,dR\), followed by removal of the \(x^{1/4}\) amplitude. It changes \(X^{1+A/4}\) to \(T\), preserving the cutoff decay. At \(A_0=q_0\), \(K_0=10\), \(b(10)=257\), so the formal cutoff becomes \(U\le T^{1/257}\). The larger printed cutoff corresponds to \(U\le T^{2/3}\) at the older endpoint. These are bookkeeping implications, not new imports.

The source residual is a sharp discrepancy minus an unmodified truncated series. Our residual has \(\Psi(\sqrt{n/T})\) on every term and an infinite upper tail. Renaming the source \(R_2\) as \(B_{T,U}\) is unjustified. The normalized \(O(T^\varepsilon)\) error from (7) also cannot alone establish a decaying residual \(L^2\) norm: it contributes \(T^{1+\varepsilon}\). Equation (12) supplies the decay directly. At the safe cutoff, (2), (7)–(8), finite-measure Hölder and the triangle inequality give
\[
 \int |H_T|^{q_0}d\mu_T\ll T^{1+\varepsilon},\quad
 \int |A_{T,U}|^{q_0}d\mu_T\ll T,\quad
 \int |B_{T,U}|^{q_0}d\mu_T\ll T^{1+\varepsilon}.
 \tag{17}
\]
No unaudited residual transfer is needed for this actual safe-cutoff bound.

### 3.4. Complete signed target and all mixed strata

Put \(\Delta=\sum_{j=1}^{12}\sigma_j\sqrt{n_j}\), \(e(t)=e^{2\pi it}\), and
\[
 \mathcal C_{12}(T,U)=\frac{T}{2^{12}}\operatorname{Re}
 \sum_{\boldsymbol\sigma\in\{-1,1\}^{12}}
 e\!\left(-\frac38\sum_j\sigma_j\right)
 \sum_{\substack{\boldsymbol n\in\mathbb N^{12}\\
                 \max_j n_j>U,\ \Delta\ne0}}
 \left(\prod_j a_{n_j}(T)\right)\widehat w(-T\Delta).
 \tag{18}
\]
Both phases, all actual coefficients, physical nonzero near resonances, and infinite tails remain inside the aggregate. For a nonempty subset \(J\subseteq\{1,\ldots,12\}\), impose \(n_j>U\) exactly when \(j\in J\). These \(4095\) subsets partition its support without omission or multiplicity. Grouping by \(|J|=j\) corresponds in physical space to
\[
 \binom{12}{j}\int A_{T,U}^{12-j}B_{T,U}^j\,d\mu_T,
 \qquad1\le j\le12,
 \tag{19}
\]
with their zero-frequency portions removed in (18). The accepted exact mass bounds all removed portions, including mixed and nonpairing resonances, by \(O(T)\).

With \(\mathcal D_{12}\) the **full** exact contribution, exactly
\[
 \mathcal M_{12}(T)=\mathcal D_{12}(T)
                  +\mathcal O_{\le U}(T)+\mathcal C_{12}(T,U),
 \qquad0\le\mathcal D_{12}(T)\ll T.
 \tag{20}
\]
Thus the complete reconstruction is
\[
 \int_{Y/2}^{3Y}|P(x)|^{12}dx
 \ll_\varepsilon T^{8+\varepsilon}+T^7|\mathcal C_{12}(T,U)|
       +T^8U^{3+\varepsilon}(1+c_{12}TU^{-2047/2})^{-L}.
 \tag{21}
\]
Here \(T^6\) comes from the leading amplitude to power twelve, \(T\) from the Jacobian, and the full smoothing error is \(T^{8+\varepsilon}\). The upper truncation error (11), multiplied by \(T^7\), is arbitrarily small by taking \(K\) large. At (1), (3) yields \(Y^{4+\eta+\varepsilon}\), and inclusive one-sided persistence yields exponent \((4+\eta)/13\).

A stronger sufficient physical target is
\[
 \int|B_{T,U}|^{12}d\mu_T\ll T^{1+\delta+\varepsilon},
 \qquad0\le\delta<2(13\theta-4).
 \tag{22}
\]
Indeed (2) and Hölder bound each (19) in absolute value by \(O(T^{1+\delta j/12+\varepsilon})\), controlling the entire mixed sum. Absolute values here come after physical summation in \(B\); this is not a termwise Fourier-kernel majorant.

For explicit \(T,U\) gain accounting, a saving \(T^{-\sigma}U^{-\gamma}\) relative to the known scale has excess \(2\eta_0-\sigma-\gamma u\) at \(U=T^u\), subject to the \(O(T)\) exact floor. Strict pointwise improvement requires
\[
 \sigma+\gamma u>
 g:=2\eta_0-2(13\theta-4)=\frac{185-578\theta}{27}>0.
 \tag{23}
\]
At (1), a saving in \(U\) alone requires \(\gamma>2047g\). This quantifies the required new strength; it does not assert such a bound.

### 3.5. Optimization of the known residual mechanism

At the safe cutoff, (12), (13), and (17) are established subject to the declared benchmark and smoothing seam. Hölder gives, for \(2\le r\le q_0\),
\[
 \int |B|^r d\mu_T\ll_\varepsilon T^{1+\varepsilon}
 U^{-(q_0-r)/(2(q_0-2))}.
 \tag{24}
\]
The \(q_0\) endpoint has **zero** cutoff decay. This is derived here for actual coefficients, not by putting order twelve into (16).

For general \(U=T^u\le T\), grant optimistically the same residual \(q_0\) bound and hence (24), even beyond the safe range. Put \(s(u)=\max(\beta,u/4)\). Multiplication by the \((12-r)\)-th power of (13) gives
\[
 \int |B|^{12}d\mu_T\ll_\varepsilon T^{1+E(r,u)+\varepsilon},
 \quad E(r,u)=(12-r)s(u)-\frac{u(q_0-r)}{2(q_0-2)}.
 \tag{25}
\]
For \(u>0\),
\[
 \partial_rE=-s(u)+\frac{u}{2(q_0-2)}
 \le-\frac u4+\frac{u}{2(q_0-2)}<0,
\]
since \(q_0>4\); at \(u=0\), the derivative is \(-\beta<0\). Consequently
\[
 \min_{2\le r\le q_0}E(r,u)
 =(12-q_0)s(u)\ge(12-q_0)\beta=2\eta_0.
 \tag{26}
\]
Orders below two do not help: finite-measure interpolation from (12) gives excess \((12-r)s(u)-ur/4\), minimized at \(r=2\). Using the smaller endpoint \(184/19\) only weakens the comparison.

This restores the compensating supremum cost. Omitting \(U^{1/4}\) for \(u>4\beta\) can fabricate a saving; substituting \(r=12>A_0\) into (16) has no Hölder justification. Even the optimistic extended residual premise fails to improve the benchmark, so a larger cutoff alone cannot rescue this mechanism.

Lower moments also permit rare high values. As an abstract norm control on a measure space of size \(T\), a function of height \(T^\beta\) on a set of measure \(T^{1-q_0\beta}\) has \(q_0\)-moment \(T\), all lower moments \(O(T)\), and twelfth moment \(T^{1+(12-q_0)\beta}\). It also obeys (12) whenever \(u\le2(q_0-2)\beta\), including (1). This tests what the norms imply; it is not a circle-discrepancy counterexample.

## 4. First doubtful or unproved step

The first new analytic estimate is (3), with the complete aggregate (18), or the stronger full-tail estimate (22). Neither follows from the source residual theorem, exact-resonance summability, or the tail second moment. The required gain is strictly more than \(g\) in the \(T\) exponent.

The source barriers occur before any claimed gain: \(r<A_0\); no verified circle \(A_0>12\); no demonstrated replacement of the sharp residual by the mollified infinite tail at larger cutoffs; and no fresh original large-values argument supporting an endpoint guessed from \(\theta_{LY}\). At the safe cutoff the transfer issue is bypassed, but (26) leaves the entire saving unproved.

The tiny head is a complete reduction, not a twelfth-moment improvement. Transition indices \(n\asymp T\) and their nonzero near resonances remain in (18) with displaced Fourier phases intact. Positive near-resonance mass cannot be identified with a lower bound for this signed aggregate. No sibling conclusion is needed for the present no-go.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| complete_source_scope | PASS for the stated interface: (18) contains every non-head stratum, (11) restores the upper tail, and (21) reconstructs the whole discrepancy. |
| physical_coefficients | PASS: \(r_2(n)n^{-3/4}\Psi(\sqrt{n/T})\) is retained. No nonnegativity of \(\Psi\) is assumed. |
| current_primary_hypotheses | PASS as bounded audit; no enlarged theorem imported. Original Ivić full-proof access/rederivation is incomplete and not asserted as a new dependency. |
| withdrawals_and_versions | PASS for checked records: Zhai II v1 and published text agree on the residual range; Li–Yang remains v2 dated 14 September 2023. Dong–Robles–Zeindler 2601.00292 remains withdrawn; no claim from it is used. |
| signed_absolute_distinction | PASS: (18) keeps one outside modulus, all cosine phases and displaced \(\widehat w\). Absolute small-head control is limited to its proved separation range. Physical-space Hölder is not termwise Fourier majorization. |
| all_costs_restored | PASS: \(T^\beta+U^{1/4}\), \(U^{-1/2}\), (15), (11), leading amplitude, Jacobian and smoothing error are all explicit. |
| exact_nonzero_resonance_split | PASS: full mixed/nonpairing exact mass is removed separately. In (14) every zero root is deleted before using the integer constant. |
| real_endpoint_uniformity | PASS at reduction level: uniform real \(T,R\), fixed windows and hard integer cutoffs; inherited annulus error includes jumps. Bounded \(T\) is absorbed by constants. No new pointwise endpoint is proved. |
| independent_statement_only_control | This selected-context task is not the campaign blind role. No sibling report was read. Separation and interpolation were independently rederived; separate conductor-required blind review is still required. |
| full_proof_frontier | PASS as scope control: (3) remains open. Even an ideal order-twelve moment gives \(4/13\), not \(1/4\). M1, M2, M9 and endpoint obligations remain separate. |
| no_parent_or_exponent_overclaim | PASS: only a small-head reduction and specified interpolation no-go are proved; the full signed moment is neither proved nor refuted. |

Exact controls for (14): all \(n_j=1\) produce zero and repeated nonzero integer roots; these are handled by \(Q\). Dependencies such as \(n_j=8,2\) do not affect formal sign invariance. Global sign reversal retains \(\Delta,-\Delta\). No numerical experiment is involved.

The version checks use the primary [Li–Yang record](https://arxiv.org/abs/2308.14859) and [withdrawn Dong–Robles–Zeindler record](https://arxiv.org/abs/2601.00292), inspected on 2026-09-23. The latter records the omitted \(L^2\) factor in (2.53). Li–Yang is used only in the graph-certified repaired scope. This is a bounded corpus audit, not a universal newest-result claim.

## 6. Dependencies and exact artifacts used

Read-only local context:

- protocol.md.
- state/proof_obligations.yml, chiefly GC-external-Li-Yang-theta-star, Li-Yang-source-audit, GC-weighted-square-root-exact-resonance-mass, GC-target, and retained M1/M2 scope.
- state/active_campaign.yml, Round 202.
- strategy/round202_strategy_literature_signed_moment_review.md.
- rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/synthesis.md.
- rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/reports/whole_moment_analytic_attack.md.
- rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/reports/circle_moment_primary_source_audit.md.
- rounds/codex-managed/gc-strategy-signed-moment-majorant-review/briefs/signed_cutoff_tail_moment_audit.md.

The exact-resonance node is the accepted algebraic dependency. The fixed-window identity and \(q_0\) benchmark retain their stated Round-201 evidence status. Primary sources and the unavailable original-source download are identified in Section 3.3. No external radical-separation lemma is needed for (14); no experiment or sibling result is used.

## 7. Recommended state effect

**Retain** the full signed twelfth-moment objective and pointwise/internal parents as open. **Retain as candidate subordinate evidence** the complete cutoff interface (18)–(21), safe head bound (2), actual residual \(L^2\) estimate (12), and restricted interpolation obstruction (26), subject to independent seams.

**Reject** extrapolating order twelve from a theorem restricted to orders below \(A_0\), guessing a larger endpoint from the pointwise exponent, or claiming a cutoff gain while omitting \(U^{1/4}\) or the mixed strata.

This supports strategy_review_with_complete_signed_next_target as an interface artifact, and strategy_review_no_source_compatible_gain for the audited residual interpolation. The conductor owns the exit choice. No graph, draft, validation matrix, source card, synthesis, or next-round plan was edited. This bounded task ends here.
