# Round 204: square-root correlation and circle endpoint source audit

Campaign: `gc-complete-large-values-duality`. Task: `large_values_primary_source_audit`. Role: source auditor; selected-context access. Generated: 2026-09-23T13:40:43Z. Starting graph SHA-256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`. Candidate evidence only. All reasoning was analytical/algebraic and source inspection; no numerical experiments. Only this assigned report was written, and no sibling report was read.

## 1. Result: valid correlation specialization; no automatic moment update

For every fixed epsilon > 0, every real N >= 1, every interval I contained in (N,2N], and every nonzero real u,
\[
 \left|\sum_{n\in I\cap\mathbb Z}e(u\sqrt n)\right|
 \ll_\varepsilon (2+N+|u|)^\varepsilon\sqrt N
       (|u|^{13/55}+|u|^{-1}).                         \tag{1}
\]
Here e(t)=exp(2 pi i t). This follows from the accepted global Bourgain exponent pair, a fresh exact derivative-class match, and elementary first- and second-derivative estimates. The exponent 13/55 is legitimate. Formula (1) is an **unweighted correlation estimate**, not a theorem for representation-number-weighted sums or their level sets. At u=0 the separate exact diagonal is # (I intersect Z), of size N for a full block.

The published circle benchmark q0=262/27 is expressly tied to the older pointwise exponent 131/416. Its citation in Tsang--Zhai is Ivić's **1985 book**, not his 1990 article. That publication provides the stated fixed endpoint; it does not state a theorem parameterized by an arbitrary newer pointwise exponent. The original Ivić proof was not made readable in this bounded audit, so no enlarged endpoint is imported by substitution.

The complete candidate distribution in the frozen strategy would, if separately proved, permit an independently justified moment update. Its diagonal contribution still prevents that candidate envelope alone from giving the frozen twelfth-moment target. Sections 3.5--3.6 give the exact conditional accounting, without asserting that the distribution has been proved here.

## 2. Exact statement and hypotheses

For (1), I may have arbitrary real endpoints and may be a proper subinterval of its ambient dyadic interval. The implied constant is independent of N, u, and the endpoints. Small bounded N is absorbed by the trivial bound. Negative u is handled by complex conjugation. No differentiability or variation condition is imposed on I beyond being an interval.

In the campaign, T is real and at least 2, U=floor(T^(1/2047)), and
\[
 B_T(R)=\sum_{n>U}a_n(T)\cos(2\pi R\sqrt n-3\pi/4),\qquad
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}).                \tag{2}
\]
The fixed real even Schwartz function Psi is the radial mollifier transform from the permitted Round-202 report, with |Psi|<=1. The fixed nonnegative smooth window w has compact support in [c,C] contained in (0,infinity); dmu_T=w(R/T)dR. In particular R is comparable to T, but no integrality condition is imposed on R, T, or a difference of sample points.

Write
\[
 \theta=\frac{3292+25\sqrt{1717}}{13762},\quad
 \beta=2\theta-\frac12,\quad q_0=\frac{262}{27}.
                                                               \tag{3}
\]
The repaired real-variable pointwise bound is graph accepted. Transferring it to (2) additionally uses the inherited, specific smoothing interface
\[
 P(R^2)=\pi^{-1}\sqrt R\,H_T(R)+O_\varepsilon(T^{1/2+\varepsilon}),
 \qquad H_T=A_{T,U}+B_T.                              \tag{4}
\]
This report does not promote (4) by citing a different sharp truncation formula. The inherited small-head result is int |A_(T,U)|^12 dmu_T << T. The full exact-resonance mass and the Gram diagonal are different objects and must both retain their stated roles.

## 3. Proof, derivation, and exact primary-source trail

### 3.1. Bourgain source interface and ranges

Jean Bourgain, *Decoupling, exponential sums and the Riemann zeta function*, JAMS 30 (2017), 205--224, DOI 10.1090/jams/860: [arXiv v2 primary text](https://arxiv.org/html/1408.5794v2), [PDF](https://arxiv.org/pdf/1408.5794v2). The imported interface is Section 5, Theorem 6, PDF pp.20--21: the pair (13/84+epsilon,55/84+epsilon), for the standard derivative class, M<=A, and proper intervals. Section 3, (3.1), only bounds derivatives two through four away from zero; that condition alone does not license the global theorem. Section 4 explicitly requires more.

The proof's alpha=log(M)/log(A) coverage is:

| Source regime | Location/method |
|---|---|
| 0<=alpha<=13/42 | Trivial estimate preceding (4.1). |
| 13/42<alpha<17/42 | (4.1)--(4.2); the coverage [0,11/28] union (12/31,332/819] includes this interval. |
| 17/42<=alpha<=1/2 | Theorem 4, (3.19). |
| 1/2<alpha<=1 | Section 5: comparable-square rescaling, extreme long lengths by (1/2,1/2), and the B-process for remaining lengths. |
| Proper intervals | Section 5 extension and Sargos's partial-sum device; logarithmic loss. |

The [version record](https://arxiv.org/abs/1408.5794) lists v2, 22 February 2016. The theorem text, rather than the abstract's differing exponent, determines this import. This is the single-author Bourgain source, not Bourgain--Watt.

### 3.2. Exact phase matching and the source-legal range

Put M=2N and A=|u|sqrt(M). On [M/2,M], write
\[
 f(x)=u\sqrt x=A F(x/M),\qquad F(t)=\operatorname{sgn}(u)\sqrt t.
                                                               \tag{5}
\]
For positive u,
\[
 f'(x)=\frac u2 x^{-1/2},\qquad
 f^{(j)}(x)=u\prod_{h=0}^{j-1}(1/2-h)x^{1/2-j}.        \tag{6}
\]
Thus the derivative approximating monomial is exact: y=u/2, s=1/2. Every required finite-order derivative error relative to that monomial is zero. On [1/2,1], |F''|>=1/4, |F'''|>=3/8, and |F''''|>=15/16. All fixed higher derivatives are bounded, and the relevant signs are fixed. This verifies the stronger standard monomial derivative class, not merely (3.1). The same explicit phase already extends to the entire ambient interval, so no extension constant depends on the length of I.

The condition M<=A is precisely |u|>=sqrt(M). In this regime the pair gives, absorbing its interval logarithm into epsilon,
\[
 |S_I(u)|\ll_\varepsilon A^\varepsilon
   (A/M)^{13/84}M^{55/84}
 \ll_\varepsilon (2+N+|u|)^\varepsilon
   |u|^{13/84}N^{97/168}.                            \tag{7}
\]
The epsilon in the last expression is obtained by first choosing a smaller source epsilon. The direct Theorem-4 window alone would only cover, up to fixed comparable constants,
\[
 M^{3/2}\le |u|\le M^{67/34};                       \tag{8}
\]
it would miss most small sample separations. Formula (7) uses the global theorem in its legally matched class. There is no source claim here when A<M.

### 3.3. All elementary regimes and interpolation

It suffices to take u>0. For 0<u<=sqrt(N), f' is monotone with
\[
 \frac{u}{2\sqrt{2N}}\le f'(x)\le\frac{u}{2\sqrt N}\le\frac12.
\]
The elementary first-derivative estimate, obtained by summation by parts of the successive phase increments, therefore gives
\[
 |S_I(u)|\ll\min(N,\sqrt N/u).                       \tag{9}
\]
For u below N^(-1/2), the trivial member of (9) is enough; the inverse-u term in (1) is then at least N. There is no claim that a bound vanishes as u approaches zero.

For all u>0, |f''(x)| is comparable to u N^(-3/2), so the elementary second-derivative estimate on an interval of length at most N yields
\[
 |S_I(u)|\ll u^{1/2}N^{1/4}+u^{-1/2}N^{3/4}.         \tag{10}
\]
For sqrt(N)<=u<=sqrt(2N), this is O(sqrt(N)); it covers the narrow gap between (9) and the exact source condition in (7). For u>=sqrt(2N), the second term in (10) is at most a constant times the first. Combine (7) and (10), using min(X,Y)<=X^(13/55)Y^(42/55). The exponents are exactly
\[
 \frac{13}{55}\frac14+\frac{42}{55}\frac{97}{168}=\frac12,
 \qquad
 \frac{13}{55}\frac12+\frac{42}{55}\frac{13}{84}=\frac{13}{55}.
                                                               \tag{11}
\]
This proves (1) in the remaining range. For extremely large u the trivial bound remains available; once u>=N^(55/26), sqrt(N)u^(13/55)>=N. No upper frequency range is silently excluded.

The elementary derivative estimates used above are the usual estimates with a monotone first derivative away from integers and a second derivative of constant sign and comparable size. Their hypotheses have been exhibited explicitly. No r2 weight has entered them. A deterministic bounded-variation weight g can enter through Abel summation at cost ||g||_infinity+Var(g); r2(n) has not been shown to possess a small such cost. It belongs in the finite vector's coefficient norm when using an unweighted Gram correlation.

### 3.4. Polynomial truncation, tails, and the exact diagonal

The epsilon factor in (1) becomes T^epsilon only after restricting N and |u| to fixed powers of T. Sample differences satisfy |u|<=C_1 T on the displaced window. For the infinite coefficient tail, fix any delta>0, truncate at L=T^(1+delta), and use, for arbitrary fixed A and small fixed kappa>0,
\[
 \sum_{n>L}|a_n(T)|
 \ll_{A,\kappa}T^{A/2}L^{1/4+\kappa-A/2}.           \tag{12}
\]
This follows directly from the divisor envelope and Schwartz decay. Increasing A makes (12) O(T^(-K)) for any prescribed K. Hence finitely many dyadic blocks with N<=L suffice, provided the complete argument restores this error. In a level-set bound, |B-B_finite|<=T^(-K) requires a threshold adjustment, for example {|B|>V} contained in {|B_finite|>V/2} for V>=1 and large T. A cutoff merely at n=T has no corresponding power-saving justification.

At u=0, the Gram entry is exactly the number of indices, without oscillatory cancellation. For a block vector with coefficients c_n,
\[
 \|c\|_2^2=\sum |c_n|^2,
 \qquad G_{jj}=\sum_{n\in I}1.
\]
For the actual coefficients, sum_(n~N)|a_n(T)|^2 << N^(-1/2+epsilon), with additional Schwartz decay above T if needed. Formula (1) only bounds off-diagonal entries. It cannot delete G_jj, a one-point localized configuration, or the +1 in a covering count O(1+T/H). These finite identities require no source theorem.

### 3.5. Published circle endpoint and exact provenance

K.-M. Tsang and W. Zhai, *Sign changes of the error term in Weyl's law for Heisenberg manifolds*, Trans. AMS 364 (2012), 2647--2666: [published institutional PDF](https://hub.hku.hk/bitstream/10722/156281/1/Content.pdf), Section 1.1, pp.2647--2648, (1.3), (1.5), and its following sentence. Their flat-torus eigenvalues give R_I(t)=P(t/(4pi^2)). They state the absolute-moment bound
\[
 \int_1^X|P(x)|^{q_0}\,dx\ll_\varepsilon X^{1+q_0/4+\varepsilon},
 \qquad q_0=262/27,                                  \tag{13}
\]
by applying Huxley's exponent 131/416 in Ivić's machinery. Reference [15], p.2665, is *The Riemann zeta-function* (1985). Their Heisenberg statements are not imported. A constant change of variable verifies (13); countable boundary-convention changes do not affect its Lebesgue moment.

The [Ivić 1990 publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/56/22/106579/large-values-of-certain-number-theoretic-error-terms) was independently reached. Its [official download](https://www.impan.pl/shop/en/publication/transaction/download/product/106579) returned HTTP 403. An author-upload scan was discoverable but yielded no readable mathematical text in this audit. No assertion about its internal theorem hypotheses or proof is made. The conductor explicitly ended further access attempts. The full original 1985/1990 machinery remains unaudited here.

For a precise consistency check of the older endpoint, our algebra gives
\[
 \beta_H=2\frac{131}{416}-\frac12=\frac{27}{208},
 \qquad 2+\frac1{\beta_H}=\frac{262}{27}.             \tag{14}
\]
This identifies a possible diagonal/supremum mechanism and confirms that the numbers fit it. It does **not** reconstruct Ivić's missing proof or certify a theorem with beta replaced by beta_LY.

An update requires an explicit real-sample large-values inequality, with every admissible height and separation range, all diagonal terms, localization ceilings, truncation and smoothing errors, and the final layer-cake integral. Alternatively, it requires auditing those exact steps in the original argument before changing its pointwise input. A newly proved complete inequality for (2) can furnish the update independently; (13) alone cannot.

### 3.6. Conditional net moment and pointwise accounting

This subsection is an implication, not a claimed result from Tsang--Zhai. Suppose the actual complete distribution is independently proved to satisfy, for every V>=1,
\[
 D_T(V)\ll_\varepsilon T^\varepsilon(V^{-2}+T V^{-p}),
 \qquad p=136/13,                                   \tag{15}
\]
and suppose (4) supplies ||B_T||_infinity << T^(beta+epsilon). The head subtraction costs U^(1/4+epsilon); it is dominated here since 1/8188<beta. The measure of the whole window is O(T). For fixed q>2, layer cake gives
\[
 \int|B_T|^q d\mu_T
 \ll_\varepsilon T^\varepsilon\left[
 T+T^{\beta(q-2)}+
 \begin{cases}
 T,&q<p,\\
 T\log T,&q=p,\\
 T^{1+\beta(q-p)},&q>p.
 \end{cases}\right].                               \tag{16}
\]
Thus conjectural-size normalized moments follow from this implication only subject to q<=p and beta(q-2)<=1. The V^-2 term survives; dropping it fabricates a larger moment range. Formula (14) is consistent with precisely that restriction, but (16) is derived here from the explicit assumed (15), not imported as Ivić's theorem.

At order twelve, (16) is
\[
 \int|B_T|^{12}d\mu_T
 \ll_\varepsilon T^\varepsilon
   (T+T^{10\beta}+T^{1+(20/13)\beta}).                \tag{17}
\]
For the accepted theta, beta>13/110, so the largest displayed exponent is 10 beta. Together with the inherited head bound, the leading amplitude in (4) contributes T^6, the squared-radius Jacobian contributes T, and the smoothing error contributes T^(8+epsilon). Consequently the corresponding whole squared-radius moment would be
\[
 \int_{Y/2}^{3Y}|P(x)|^{12}dx
 \ll_\varepsilon Y^{1+10\theta+\varepsilon},\qquad Y=T^2.
                                                               \tag{18}
\]
It would yield pointwise exponent (1+10 theta)/13 via the inclusive persistence bridge. This exceeds theta, because theta<1/3. It is therefore potentially a moment improvement, not a pointwise improvement.

The frozen normalized target has exponent 29/25. We have 10 beta>29/25, so (17) falls short. More finely, at V=T^v, the two terms in (15) are each below T^(29/25)V^(-12) only when respectively v<=29/250 and v<=13/125. Above 13/125 the candidate envelope itself cannot certify the frozen target throughout the required range. This is an insufficiency of that upper envelope, not a counterexample to the actual arithmetic distribution.

## 4. First doubtful or unproved step

There is no unresolved range in the unweighted specialization (1). The first analytic gap between it and the frozen objective is the complete actual level-set argument: the coefficient norm, full Gram matrix, sampling/covering, and every dyadic and infinite-tail recombination must all be supplied. This source task does not claim to have proved (15).

Even granting (15), the stronger high-value distribution remains unproved by the calculation in Section 3.6. Its failure to imply the target is quantitative; it does not prove the target false. For the literature route, the first unverified step is the original parameter-dependent large-values proof underlying a proposed replacement of q0. The published fixed endpoint and the numerical identity (14) do not fill that gap.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| actual_coefficients | PASS as a scope check: (2) remains actual; the imported correlation is unweighted. No small variation of r2 is asserted. |
| complete_distribution | OPEN here: (15) is an explicit premise only; the source theorem alone does not prove it. |
| full_diagonal_and_ceiling | PASS: u=0 is treated separately and exactly; O(1+T/H) cannot become O(T/H) when H>T. |
| source_hypotheses | PASS for (1): exact s=1/2 monomial class, every proper interval, and M<=A are checked; (3.1) alone is not used as the global hypothesis. Original Ivić proof remains unaudited. |
| all_tails_and_ranges | PASS for the source interface: (9)--(11) cover every u; (12) supplies a lawful polynomial truncation with threshold adjustment. Complete large-value recombination remains assigned elsewhere. |
| real_uniformity | PASS: all phase parameters, sample differences, endpoints and T are real; constants depend only on fixed epsilon, windows and mollifier data. |
| net_moment_and_pointwise_powers | PASS conditionally: (16)--(18) retain the diagonal term, amplitude, Jacobian and smoothing floor. The candidate distribution would not improve theta. |
| independent_statement_only_control | This is the selected-context source role, not the campaign's blind role. No sibling read occurred. The derivative/interpolation and endpoint arithmetic were independently derived; separate blind Gram review is still required. |
| no_parent_overclaim | PASS: no claimed proof of the actual distribution, frozen twelfth moment, M1, M2, M9, or quarter exponent. |

Additional exact controls: as u tends to zero, (9) is capped by N; at u=sqrt(N), (10) is O(sqrt(N)); at u=sqrt(2N), the source condition is met with equality; beyond u=N^(55/26), the target correlation bound is already trivial. A one-point Gram matrix still has its full positive diagonal. These are symbolic controls, not numerical experiments.

## 6. Dependencies and exact artifacts used

Read-only permitted local context:

- `protocol.md`.
- `state/proof_obligations.yml`, including `Bourgain-2017-reciprocal-exponent-pair-source-audit`, `GC-external-Li-Yang-theta-star`, `Li-Yang-source-audit`, `GC-weighted-square-root-exact-resonance-mass`, and `GC-physical-twelfth-moment-absolute-majorant-obstruction`.
- `state/active_campaign.yml`, Round 204.
- `strategy/round204_complete_large_values_attack.md`.
- `rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md`.
- `sources/bourgain_2017_exponent_pair.md`.
- `rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/reports/circle_moment_primary_source_audit.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md`.
- This task's assigned brief.

Primary source statements, exact theorem locations, URLs and access limitations appear in Sections 3.1 and 3.5. At most two primary proof trails were pursued: Bourgain's applicable Sections 3--5 and Ivić's original large-values trail. The latter was stopped at its access/verification limit. Tsang--Zhai was checked for its published benchmark and bibliography, not treated as a full reproof of Ivić. No source card, shared state, synthesis, matrix or successor artifact was edited.

## 7. Recommended state effect

**Retain** the accepted Bourgain source dependency. **Retain as candidate subordinate evidence** the fresh square-root specialization (1), with its complete small-u cover and separate exact diagonal. It is suitable for the conductor's source seam, not independent certification of an entire distribution theorem.

**Retain** q0=262/27 as the verified printed circle benchmark with the inherited source status. **Revise** any provenance that treats Tsang--Zhai's [15] as Ivić1990, or treats its fixed endpoint as a parameterized theorem. **Reject** an endpoint update by substitution alone. An update derived from a separately proved complete (15) would be a new argument with the conditional costs (16)--(18).

Keep the frozen distribution target, twelfth-moment improvement and all pointwise/internal parents open unless another complete proof passes the conductor's prescribed gates. This bounded source task stops after this report.
