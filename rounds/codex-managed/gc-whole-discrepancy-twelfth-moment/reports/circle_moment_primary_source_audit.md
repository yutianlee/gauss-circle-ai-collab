# Round 201: circle moment primary-source audit

Campaign: `gc-whole-discrepancy-twelfth-moment`. Task: `circle_moment_primary_source_audit`. Role: source auditor, selected-context access. Date: 2026-09-23. Starting graph SHA-256: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`. Candidate evidence only; no shared state changed. All work was source inspection and analytical/algebraic reasoning; no numerical experiments were performed. Decimal evaluations below merely display exact algebraic expressions.

## 1. Result: a complete benchmark and a restricted no-go

The strongest directly verified, explicitly circle-specific absolute-moment range located in this bounded audit is

\[
 \int_1^Z |P(x)|^q\,dx\ll_{q,\epsilon} Z^{1+q/4+\epsilon},
 \qquad 0\le q\le q_0:=262/27.
 \tag{1}
\]

The source is the published Tsang--Zhai paper, Section 1.1, formula (1.5) and its following sentence, after the exact normalization below. This is a verified printed external benchmark, not a new internal proof or a claim that the entire literature has been exhausted.

Combined with the accepted repaired Li--Yang exponent \(\theta=\theta_{LY}\), (1) gives the **complete** twelfth-moment bound

\[
 \int_{Y/2}^{3Y}|P(x)|^{12}\,dx
 \ll_\epsilon Y^{4+\eta_0+\epsilon},\qquad
 \eta_0=\frac{62}{27}\left(\theta-\frac14\right)
 =0.148072478162659\ldots.
 \tag{2}
\]

The target is \(\eta<13\theta-4=0.088281287662798\ldots\). Thus the verified interpolation misses the strict-improvement threshold by

\[
 \eta_0-(13\theta-4)
 =\frac{185-578\theta}{54}
 =0.059791190499861\ldots>0.
 \tag{3}
\]

This proves a no-go for claiming the desired improvement from these low moments by the supremum interpolation used here. It does not disprove the desired twelfth-moment theorem or any different large-values argument. No matching improving circle twelfth-moment theorem was found in the inspected primary corpus.

## 2. Exact statement and hypotheses

Use the inclusive whole discrepancy

\[
 P(x)=\#\{(m,n)\in\mathbb Z^2:m^2+n^2\le x\}-\pi x,
 \qquad x\ge2.
\]

Assume the already accepted, repaired external theorem

\[
 |P(x)|\ll_\epsilon x^{\theta+\epsilon},\qquad
 \theta=\frac{3292+25\sqrt{1717}}{13762}.
\]

Every moment order is fixed; constants may depend on it and on \(\epsilon>0\). There is no assertion uniform for an order tending to infinity. The moments are Lebesgue integrals in the squared-radius variable. A fixed bounded nonnegative weight of compact support in \([cY,CY]\), where \(0<c<C<\infty\), is allowed by domination. This does not supply estimates for arbitrary moving weights or point evaluation at an exceptional center.

In Tsang--Zhai the torus eigenvalues are \(4\pi^2(m^2+n^2)\), hence

\[
 R_I(t)=P\left(t/(4\pi^2)\right).
 \tag{4}
\]

The \(R_I\) bound therefore applies exactly after a constant change of variable. It is not the Heisenberg remainder \(R(t)\) from the other sections of that paper.

An origin convention can add a constant to a source discrepancy; half-weighting the boundary differs only at integer squared radii. Neither changes an absolute-moment upper exponent: use \(|u+O(1)|^q\ll_q|u|^q+1\), and a countable set has zero measure. The inclusive pointwise bridge is separately justified by monotonicity, not by identifying almost-everywhere values at jumps.

## 3. Proof, derivation, and primary-source cards

### Complete exponent accounting

On \([Y/2,3Y]\), use

\[
 |P(x)|^{12}\le
 \left(\sup_{Y/2\le u\le3Y}|P(u)|\right)^{12-q}
 |P(x)|^q.
\]

For any fixed admissible absolute order \(q\le12\), integration gives

\[
 M_{12}(Y)\ll Y^{1+q/4+(12-q)\theta+\epsilon}
 =Y^{4+(12-q)(\theta-1/4)+\epsilon}.
 \tag{5}
\]

Distribute a sufficiently small epsilon among the two input estimates before multiplying. The choice \(q=q_0\) minimizes the right-hand exponent among orders verified here, since \(\theta>1/4\). All terms of \(P\), including any convention-adjustment constant, have been included.

| Verified input used in (5) | Excess \(\eta\) at order twelve |
|---|---:|
| Absolute fourth moment | \(8(\theta-1/4)=0.515865407792491\ldots\) |
| Absolute eighth moment | \(4(\theta-1/4)=0.257932703896246\ldots\) |
| Absolute order \(184/19\) | \((44/19)(\theta-1/4)=0.149329460150458\ldots\) |
| Absolute order \(262/27\) | \((62/27)(\theta-1/4)=0.148072478162659\ldots\) |

The resulting moment-to-pointwise exponent is

\[
 \frac{4+\eta_0}{13}=0.319082498320205\ldots>\theta.
\]

Generally, an optimal-order input \(M_q(Y)\ll Y^{1+q/4+\epsilon}\) fed through (5) would improve \(\theta\) precisely when

\[
 q>\frac{3}{4(\theta-1/4)}-1
 =10.6309407635519\ldots.
 \tag{6}
\]

The actual verified range ends below this. Formula (6) is an algebraic criterion for this interpolation, not a theorem providing that range. In particular, one must not replace Huxley's input inside an uninspected large-values proof and announce a new admissible endpoint solely by guessing its dependence on \(\theta\).

For the campaign's radius variable, \(x=R^2\) and \(dx=2R\,dR\). On fixed windows \(R\asymp T=\sqrt Y\), a \(q\)-moment of \(P\) of squared-radius order \(Y^{1+q/4+\eta}\) corresponds to radius order \(T^{1+q/2+2\eta}\). Subject to the separately required uniform smoothing identity

\[
 P(R^2)=\pi^{-1}R^{1/2}H_T(R)+O_\epsilon(T^{1/2+\epsilon}),
\]

the complete bound (2) also yields

\[
 \int w(R/T)|H_T(R)|^{12}\,dR
 \ll T^{1+2\eta_0+\epsilon}.
 \tag{7}
\]

Indeed the reverse inequality bounds \(|H_T|^{12}\) by a constant times \(T^{-6}|P(R^2)|^{12}+T^\epsilon\), and the Jacobian costs \(T^{-1}\). The smoothing error contributes only \(O(T^{1+\epsilon})\). Equation (7) is conditional on that analytic seam, not a source theorem for a different smoothed sum.

### Source A: Zhai's actual fourth-moment circle corollary

W. Zhai, *On higher-power moments of Delta(x) (III)*, Acta Arith. **118** (2005), 263--281; [arXiv:0805.1523v1](https://arxiv.org/abs/0805.1523v1), deposited 11 May 2008; [full PDF](https://arxiv.org/pdf/0805.1523v1). The record lists only v1 and no withdrawal. Theorem 1 is a divisor fourth moment. **Corollary 1, (1.7), PDF page 3**, explicitly states

\[
 \int_2^Z P(x)^4\,dx=CZ^2+O_\epsilon(Z^{53/28+\epsilon}).
\]

This is an actual circle result; \(P^4=|P|^4\). Its main term implies an upper bound of order \(Z^2\). Lemma 1 is a four-root spacing theorem, not a twelve-root theorem. Theorem 2 treats the zeta mean-square remainder \(E(t)\). None of these statements yields an unassisted twelfth moment. The fixed-window weighted upper bound follows by positivity and domination, without importing an asymptotic for a new weight.

### Source B: Zhai's higher signed moments and absolute input

W. Zhai, *On higher-power moments of Delta(x) (II)*, Acta Arith. **114** (2004), 35--54; [arXiv:0805.1270v1](https://arxiv.org/abs/0805.1270v1), deposited 9 May 2008; [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83024). Both versions were inspected. **Theorem 3, (1.25)--(1.26), journal page 39**, assumes an absolute \(A_0>9\) moment of conjectural size and produces signed asymptotics for integers \(3\le k<A_0\). Its stated unconditional range is \(3\le k\le9\). Remark 1.5 explicitly gives the circle absolute input \(A_0=184/19\), referring to Ivić's Theorem 13.12. Odd signed asymptotics cannot be substituted for absolute moments. The later note improving \(A_0\) to \(262/27\) names the divisor formula; it alone is not our circle transfer. Warning: printed (5.1) has frequency \(4\pi\sqrt{nx}\); the disk normalization requires \(2\pi\sqrt{nx}\). That displayed expansion is not imported. The independent circle bound in Source C supplies the benchmark used here.

### Source C: a later explicit circle absolute range

K.-M. Tsang and W. Zhai, *Sign changes of the error term in Weyl's law for Heisenberg manifolds*, Trans. Amer. Math. Soc. **364** (2012), 2647--2666, [published PDF at the authors' institutional repository](https://hub.hku.hk/bitstream/10722/156281/1/Content.pdf), DOI [10.1090/S0002-9947-2012-05437-7](https://doi.org/10.1090/S0002-9947-2012-05437-7). **Section 1.1, pages 2647--2648, (1.5) and its following sentence**, states

\[
 \int_1^Z|R_I(t)|^A\,dt\ll Z^{1+A/4+\epsilon}
 \quad(0\le A\le262/27\text{ fixed}).
\]

This follows there by inserting Huxley's bound in Ivić's machinery. The paper explicitly identifies \(R_I\) with the flat-torus circle error, and its eigenvalues verify (4). This is the most useful circle-specific followup located here. The original Ivić large-values proof is not independently rederived in this report; the endpoint used is the published statement, unchanged. No claim about arbitrary-order Heisenberg moments is imported. The fixed-order constants and epsilon loss survive the constant rescaling.

### Source D: direct circle followup and the local-moment limitation

D. A. Popov, *Voronoi's formulae and the Gauss problem*, Russian Math. Surveys **79** (2024), 53--126, [publisher full text](https://www.mathnet.ru/eng/rm10162), DOI [10.4213/rm10162e](https://doi.org/10.4213/rm10162e). Section 6 distinguishes signed and absolute moments. Its historical (6.25) has exponent \((35k+38)/108\) for \(k\ge35/4\), which at twelve is \(229/54>4+\eta_0\). No improvement is imported from this historical summary. Theorem 10 supplies actual local circle estimates only at the listed orders 1, 2, 4, 6. Theorem 11 is a conditional moment-to-pointwise principle. Section 11 explicitly describes the stronger fourth-moment local hypothesis yielding exponent \(3/10\) as conjectural. These statements provide no improving twelfth-moment input.

### Source E: divisor-only followups

A. Ivić and W. Zhai, *Higher moments of the error term in the divisor problem*, [arXiv:0904.2271v3](https://arxiv.org/abs/0904.2271v3), 18 February 2010, [full text](https://arxiv.org/pdf/0904.2271v3). Its short-interval fourth-moment theorem concerns \(\Delta_k\) and uses four \(k\)-th roots. A large power of the divisor-order parameter is not a high moment of the circle error. No explicit circle twelfth-moment corollary was found in that paper.

W. Zhai, *A survey on moments of a class of error terms*, [arXiv:2607.17249v1](https://arxiv.org/abs/2607.17249v1), 19 July 2026, Adv. Math. (China) **55** (2026), 481--504, [PDF](https://arxiv.org/pdf/2607.17249v1). Its (2.7) and \(262/27\) discussion concern \(\Delta_2\), while its new theorems concern joint signs of \(\Delta_2,\Delta_3\). Its Selberg-class moment formulations are conjectures. It is current primary evidence about what this author states, but supplies no new circle theorem and is not used to certify the older circle bound.

### Source F: differently averaged and unweighted sums

X. Wu, *Higher Moments for Lattice Point Discrepancy of Convex Domains and Annuli*, [arXiv:2009.03208](https://arxiv.org/abs/2009.03208), J. Number Theory **235** (2022), 382--400; [PDF](https://arxiv.org/pdf/2009.03208). Its moments average over translations \(x\in\mathbb T^2\), at fixed radius. Theorem 2.2 also assumes a pointwise exponent uniform in both radius and translation. A translation average does not imply this task's centered radius average, and our accepted centered Li--Yang estimate does not furnish the uniform translation hypothesis.

Y. Xiao, *Moment Estimates and Discrepancy for Sums of Square Roots Modulo One*, [arXiv:2606.28986v1](https://arxiv.org/abs/2606.28986v1), 27 June 2026; [PDF](https://arxiv.org/pdf/2606.28986v1). Theorems 1.1--1.2 treat \(S(h,n)=\sum_{a\sim n}e(h\sqrt a)\), averaged over integer \(h\sim H\). The fourth moment requires \(n^{1/2+\delta}\le H\le n^{2/3}\), \(0<\delta<1/6\). The campaign transition has \(n\asymp T\), \(R\asymp T\), as well as representation-number weights and a continuous displaced window. These are already unmatched hypotheses. Higher moments are explicitly conjectural in Section 3.8, Conjecture 3.15. No twelfth-moment import is made.

### Version/currentness boundary

The bounded search was run on 2026-09-23 using circle moment, twelfth moment, higher-power, absolute-moment endpoint, and recent arXiv queries. Full primary theorem text, not search snippets, determined all imports. The July 2026 Zhai paper and June 2026 Xiao paper were inspected as current leads. This is a dated result for the named corpus, not a universal newest/best claim.

The [Li--Yang record](https://arxiv.org/abs/2308.14859) still lists v2 dated 14 September 2023. We retain only the repository's repaired application. The [Dong--Robles--Zeindler record](https://arxiv.org/abs/2601.00292) shows v2 withdrawn on 5 January 2026, with the authors reporting a missing \(L^2\) in (2.53); no claimed improvement from it is used. The local Li--Yang source card also excludes withdrawn Bourgain--Watt theorem imports.

## 4. First doubtful or unproved step

The first failed hypothesis in extrapolating Source B is \(k<A_0\) with an already proved absolute \(A_0\) input. Setting \(k=12\) would require \(A_0>12\); no such input has been verified. Source A stops at four. Sources E and F fail the arithmetic object, averaging variable, moment order, or parameter range before any power can be transferred.

For the campaign's own expansion, put

\[
 \Lambda(\boldsymbol\epsilon,\mathbf n)=
 \sum_{j=1}^{12}\epsilon_j\sqrt{n_j},\qquad e(u)=e^{2\pi i u}.
\]

For each fixed \(T\), Schwartz decay of \(\Psi\) and \(r_2(n)\ll_\epsilon n^\epsilon\) imply \(\sum_n|a_n(T)|<\infty\). Thus absolute convergence justifies the exact identity

\[
 \int w(R/T)H_T(R)^{12}\,dR=
 \frac{T}{2^{12}}\sum_{\boldsymbol\epsilon\in\{-1,1\}^{12}}
 e\left(-\frac38\sum_j\epsilon_j\right)
 \sum_{\mathbf n\in\mathbb N^{12}}
 \left(\prod_j a_{n_j}(T)\right)
 \widehat w\bigl(-T\Lambda(\boldsymbol\epsilon,\mathbf n)\bigr).
 \tag{8}
\]

If the separate exact-resonance task proves the entire \(\Lambda=0\) contribution is \(O(T^{1+\epsilon})\), the missing sufficient estimate is

\[
 \left|\frac{T}{2^{12}}\sum_{\boldsymbol\epsilon}
 e\left(-\frac38\sum_j\epsilon_j\right)
 \sum_{\Lambda\ne0}\left(\prod_j a_{n_j}(T)\right)
 \widehat w(-T\Lambda)\right|
 \ll_\epsilon T^{1+2\eta+\epsilon},
 \qquad \eta<13\theta-4.
 \tag{9}
\]

The single outside modulus in (9) is deliberate; this is not a sum of positive spacing counts. Opposite sign vectors ensure the sum is real. No fixed-window probabilistic independence is assumed. The named literature supplies neither (9) nor the desired complete moment. Relative to (7), the remaining saving at the threshold is \(Y^{0.059791190499861\ldots}\), equivalently \(T^{0.119582380999722\ldots}\), with an additional positive margin required for strict improvement.

## 5. Required controls and outcomes

| Control | Outcome in this source audit |
|---|---|
| `whole_discrepancy_scope` | Pass: (2) treats the full inclusive discrepancy; no M1/M2 block replacement. |
| `fixed_window_smoothing` | No source theorem certifies this seam. Formula (7) explicitly depends on the campaign's fixed-scale identity. |
| `inclusive_jump_error` | Pass for imported moment exponents: origin shifts and null-set boundary conventions are handled. Inclusive pointwise persistence uses one-sided monotonicity. |
| `bessel_and_fourier_normalization` | Source warning recorded: Zhai II (5.1) prints the wrong disk frequency. Formula (8) uses the campaign's \(2\pi R\sqrt n-3\pi/4\), not that display. |
| `uniform_tail_control` | Absolute convergence at each fixed \(T\) proves the exchange in (8); it does not prove a uniform truncation error. No such source import is claimed. |
| `all_sign_patterns` | Pass: all \(2^{12}\) signs appear in (8)--(9). |
| `nonpairing_exact_resonances` | Preserved: \(\Lambda=0\) is the full class, not only pairings. Its uniform bound awaits the assigned independent report. |
| `displaced_offdiagonal_phase` | Pass: complex \(\widehat w(-T\Lambda)\) and the cosine phase remain inside the sum. |
| `second_moment_normalization` | Pass at the exponent and constant-rescaling level: Zhai II (1.24) has \((3\pi^2)^{-1}\sum r_2(n)^2n^{-3/2}\) times \(Z^{3/2}\); (4) converts it to the coefficient \((6\pi^3)^{-1}\sum r_2(n)^2n^{-3/2}\) printed by Tsang--Zhai. |
| `moment_to_pointwise_exponents` | Pass: (5)--(6) and \((4+\eta_0)/13>\theta\) retain the full loss. |
| `primary_source_hypotheses` | Pass for the stated printed benchmark; full original Ivić proof not independently rederived. Conditional, signed, divisor, translation, and conjectural statements stay separate. |
| `no_parent_or_exponent_overclaim` | Pass: no global improvement, quarter exponent, M1, M2, M9, or endpoint theorem is promoted. |

The elementary inclusive bridge is compatible with these controls: if \(P(X)>0\), monotonicity gives \(P(X+h)\ge P(X)-\pi h\); for \(P(X)<0\), use \(P(X-h)\le P(X)+\pi h\). Hence a value of modulus \(V\) persists on a one-sided interval of length \(V/(2\pi)\), giving \(V^{13}\ll M_{12}(Y)\). The accepted sublinear bound places this interval within the enlarged window for large \(Y\).

## 6. Dependencies and exact artifacts used

Read-only local context:

- `protocol.md`.
- `state/proof_obligations.yml`, in particular `GC-target`, `GC-global-real-second-moment-density-one-quarter`, and `GC-external-Li-Yang-theta-star`.
- `state/active_campaign.yml`.
- `strategy/round201_whole_discrepancy_twelfth_moment_strategy.md`.
- `strategy/gauss_circle_strategy_review_2026-09-23.md`.
- `sources/li_yang_2023.md`.
- This task's exact brief, `rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/briefs/circle_moment_primary_source_audit.md`.

External imports are Source C's fixed \(262/27\) moment statement and the accepted repaired Li--Yang pointwise bound. Sources A--B provide independently identifiable lower-moment checks and order restrictions. Sources D--F are audit evidence for limitations, not dependencies of (2). The constant normalization check is explicit above. No candidate analytic or blind-agent report was used. No legacy evidence directory, source card, synthesis, validation matrix, graph, or proof draft was edited.

## 7. Recommended state effect

**Retain** the global target and whole twelfth-moment improvement as open. **Revise** any source summary equating a fourth-moment theorem, an odd signed asymptotic, a divisor result, a translation average, or a conjectural higher moment with the required circle twelfth moment. **Retain as candidate benchmark evidence** the lawful full bound (2), the exact deficit (3), the source normalization (4), and the first open signed correlation (9). Source C can support a conductor-owned external source card after the normal source seam review; this report does not itself promote it.

The applicable exit remains `whole_discrepancy_moment_reduction_open_offdiagonal` unless another assigned report proves the missing complete estimate. No next round is initiated.
