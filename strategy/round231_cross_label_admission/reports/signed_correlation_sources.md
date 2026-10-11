# Prelaunch231: signed correlation source audit

## 1. Result

**No source admitted.** Four targeted search batches and two theorem audits found no applicable, proved cancellation estimate for the complete signed distinct-squarefree-class twelfth correlation in the frozen interface. This is a bounded search result, not a claim that no such theorem exists anywhere.

The closest finite correlation theorem located is Lamzouri's Proposition 3.1. Its twelfth-order cutoff, in this project's radius variable, is

\[
 M\leq T^{1/2072}/144.
\]

It therefore contains **no** class with \(d>Q=\lfloor T^{2/5}\rfloor\), once \(T\) is sufficiently large. The theorem's excellent finite-truncation error does not estimate the requested residual. The closest complete circle-moment theorem audited, Zhai's Theorem 3, needs an optimal absolute moment at an order strictly greater than twelve before giving a twelfth-moment asymptotic.

The complete retained exponent remains \(10\beta=1.289663519481\ldots\). Neither the moment-improvement gate \(b<10\beta\), the pointwise-improvement gate \(b<13\beta-1/2\), nor the concrete \(29/25\) target is met by a new input.

## 2. Exact statements and hypotheses

**Frozen target.** All quantities, smoothing, real radius windows, harmonics, and signs are those in `briefs/complete_target.md`. In particular

\[
 a_n=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\qquad
 f_d(R)=\sum_{s\geq1}a_{ds^2}
 \cos(2\pi R s\sqrt d-3\pi/4),
\]

and \(I_{12}\) sums the integrals of products over ordered, pairwise distinct squarefree \(d_j>Q\). The required bound is one-sided, \(I_{12}\leq T^{29/25+\varepsilon}\), with the inherited paid partners retained. No new assertion about those partners is made here.

**Audit 1: finite truncation.** [Y. Lamzouri, Proposition 3.1](https://arxiv.org/html/2410.03652v1#S3), arXiv:2410.03652v1, 4 October 2024. For real uniformly bounded coefficients \(c_m\), fixed real \(\alpha_0\ne0,\beta_0\), integer \(0\leq h\leq(\log\log U)/4\), and \(M\leq U^{1/(2^h+4h)}/h^2\),

\[
 \frac1U\int_U^{2U}\left(\sum_{m\leq M}c_m
 \cos(2\pi\alpha_0\sqrt{mt}+\beta_0)\right)^h dt
 =\mathbb E\left(\sum_{dr^2\leq M}c_{dr^2}
 \cos(2\pi rX_d+\beta_0)\right)^h+O(U^{-1/4}),
\]

where the \(X_d\) are independent uniform variables, indexed by squarefree \(d\). Its proof bounds nonzero root frequencies using
\( |\sum_{j=1}^h\epsilon_j\sqrt{n_j}|\geq(h\sqrt M)^{-(2^{h-1}-1)}\).
The same paper's distribution results and exceptional-set Laplace transforms are not complete twelfth-moment estimates. No extra theorem from that paper is imported.

**Audit 2: complete circle moment, conditional beyond its range.** [W. Zhai, Theorem 3](https://www.impan.pl/shop/en/publication/transaction/download/product/83024), *Acta Arithmetica* **114** (2004), 35–54, DOI [10.4064/aa114-1-3](https://doi.org/10.4064/aa114-1-3), pp. 36,39. Assume \(A_0>9\) and \(\int_1^U|P(x)|^{A_0}dx\ll U^{1+A_0/4+\varepsilon}\). For integers \(3\leq k<A_0\),

\[
 \int_1^U P(x)^kdx
 =\frac{(-1)^kB_k(r_2)}{(1+k/4)2^{k-1}\pi^k}U^{1+k/4}
 +O(U^{1+k/4-\delta_1(k,A_0)+\varepsilon}),
\]

\[
 B_k(f)=\sum_{\ell=1}^{k-1}\binom{k-1}{\ell}s_{k;\ell}(f)
 \cos\frac{\pi(k-2\ell)}4,\qquad
 s_{k;\ell}(f)=\sum_{\sum_{j\leq\ell}\sqrt{n_j}=\sum_{j>\ell}\sqrt{n_j}}
 \frac{\prod_jf(n_j)}{(\prod_jn_j)^{3/4}}.
\]

Here \(K_0\) is the least even integer \(\geq A_0\), \(b(k)=2^{k-2}+(k-6)/4\), and

\[
 \delta_1=\frac{\sigma}{2b(K_0)},\qquad
 \sigma=\begin{cases}1/4,&k-1<A_0/2,\\
 (A_0-k)/(2(A_0-2)),&A_0/2+1\leq k<A_0.
 \end{cases}
\]

The circle theorem states unconditional integers \(3\leq k\leq9\), using \(A_0=184/19\), with error saving \(\delta_2=\sigma/(2b(k)+2\sigma)\). The note added in proof explicitly upgrades the **divisor** Theorem 2; it is not treated here as a separately stated circle upgrade.

## 3. Derivation and complete power restoration

### Literal signed frequency quantity

Use \(\widehat w(\xi)=\int w(u)e(-u\xi)du\). Absolute convergence at each fixed \(T\), from the Schwartz factor, allows the exact expansion

\[
 I_{12}=\frac{T}{2^{12}}
 \sum_{\substack{d_1,\ldots,d_{12}>Q\ {
 \rm squarefree}\\d_i\ne d_j}}
 \sum_{s_1,\ldots,s_{12}\geq1}
 \prod_{j=1}^{12}a_{d_js_j^2}
 \sum_{\epsilon\in\{\pm1\}^{12}}
 e^{-3\pi i\sum_j\epsilon_j/4}
 \widehat w\left(-T\sum_j\epsilon_js_j\sqrt{d_j}\right).
\]

Pairing opposite sign vectors makes the expression real. Six-versus-six has phase multiplier one, but is only one portion of the expansion. Mixed sign patterns, all harmonics, and their smooth frequency kernel still require payment. Linear independence of distinct squarefree radicals removes exact zero frequencies here; it does not control the signed mass in the slab of thickness \(T^{-1}\).

This distinguishes four objects: unsigned near-root counts; exact resonant constants; finite-support equidistribution; and the finite-\(T\), moving-support signed discrepancy above. A theorem about the first three is usable only with an explicit estimate for their difference from the fourth.

### Audit 1 applied without a hidden change of scale

Put \(U=T^2\), \(h=12\), \(\alpha_0=1\), and \(\beta_0=-3\pi/4\). The coefficient hypothesis is satisfied by the actual \(a_n\): for example \(r_2(n)\leq4\tau(n)\leq8\sqrt n\) and \(|\Psi|\leq1\) give \(|a_n|\leq8\). The source's fixed phase convention is consequently compatible; no coefficient identity or positivity assumption is needed.

The cutoff becomes

\[
 M\leq\frac{(T^2)^{1/(4096+48)}}{144}
 =\frac{T^{1/2072}}{144}\ll Q.
\]

Every \(n=ds^2\) in this truncation has \(d\leq M<Q\). Thus its projection to the actual distinct-large-class target is identically empty. Replacing \(M\) by \(T\) violates the theorem by a power of \(T\), not a logarithm. Replacing it by \(Q\) already violates the same condition.

The radial weight is not silently transferred from an unweighted interval theorem. One can directly reproduce the proof's off-diagonal step for the present smooth window: integration by parts gives

\[
 \left|\int w(R/T)e(R\eta)dR\right|
 \ll_w\min(T,|\eta|^{-1}).
\]

For twelve terms with \(n_j\leq M\), the cited separation estimate has exponent \(2^{11}-1=2047\). Also \(\sum_{n\leq M}|a_n|\ll_\varepsilon M^{1/4+\varepsilon}\). Hence the entire weighted off-diagonal contribution is at most

\[
 O_{w,\varepsilon}\left(M^{3+\varepsilon}M^{2047/2}\right)
 =O_{w,\varepsilon}\left(M^{2053/2+\varepsilon}\right).
\]

At the legal cutoff this is \(T^{2053/4144+\varepsilon}\), approximately \(T^{0.49541506+\varepsilon}\). This independently restores the unnormalized radial error scale (the source's \(U^{-1/4}\) normalized error likewise becomes \(T^{1/2}\)). It does not extend the cutoff.

For completeness the random diagonal of this legal truncation is uniformly bounded before multiplication by the length \(T\). Indeed the sup norm of its class \(d\) is \(O_\varepsilon(d^{-3/4+\varepsilon})\), uniformly in the truncation and smoothing, because the harmonic sum in \(s^{-3/2+2\varepsilon}\) converges. The class variables are independent and centered. In their twelfth moment every surviving class has multiplicity at least two, and each corresponding class sum converges. This proves \(M_{12}(B_{\leq M})\ll T\) at the legal cutoff. It says nothing comparable about \(B-B_{\leq M}\).

For the **complete** wave, elementary absolute summation, including the Schwartz tail, only gives \(\sum_n|a_n|\ll T^{1/4+\varepsilon}\) and \(M_{12}(B)\ll T^{4+\varepsilon}\). Using the admitted inherited estimate instead leaves \(T^{10\beta+\varepsilon}\). The finite-truncation source provides no new complete exponent.

### Audit 2 and the missing hypothesis

At \(k=12\), the theorem requires \(A_0>12\). This is not merely convergence of an exact root-relation constant. It is an optimal finite-interval **absolute** moment hypothesis. It already implies, by Holder,

\[
 \int_U^{2U}|P(x)|^{12}dx
 \leq U^{1-12/A_0}
 \left(\int_U^{2U}|P(x)|^{A_0}dx\right)^{12/A_0}
 \ll U^{4+\varepsilon}.
\]

With \(F(R)=R^{-1/2}P(R^2)\), the Jacobian \(dx=2R\,dR\) gives \(\int_{T}^{2T}|F(R)|^{12}dR\ll T^{1+\varepsilon}\). Thus assuming this hypothesis to solve the requested problem would assume an even stronger complete-moment input first. No smoothing transfer is claimed from this observation; the obstruction arises before that seam.

Even granting all favorable transfer seams from its stated \(A_0=184/19\) circle bound, interpolation with the inherited \(T^\beta\) cap gives only

\[
 b_{12}=1+(12-184/19)\beta=1+\frac{44}{19}\beta
 =1.298658920301\ldots>10\beta.
\]

This is a generous comparison, not a new imported theorem for \(B\). It is already weaker than the accepted complete moment.

The independent restoration formula supplied by the checkpoint is
\(\theta_{12}=1/4+(b_{12}+1/2)/26\). The complete accounting is:

| Input | Complete radial exponent \(b_{12}\) | Restored physical exponent |
|---|---:|---:|
| Legal finite truncation alone | No bound for its complete complement | No complete implication |
| Full elementary absolute sum | \(4\) | \(11/26=0.4230769231\ldots\) |
| Favorable old-moment interpolation | \(1+(44/19)\beta\) | \(0.3191791892\ldots\) |
| Retained accepted complete moment | \(10\beta\) | \(0.3188332123\ldots\) |
| Required concrete milestone | \(29/25\) | \(102/325=0.3138461538\ldots\) |

The benchmark pointwise exponent is \(1/4+\beta/2=0.314483175974\ldots\), so its strict twelfth-moment gate is \(13\beta-1/2=1.176562575326\ldots\). No row supplied by the source search beats it.

### Why a smooth density subtraction needs a further estimate

Already for the first harmonic of the squarefree measure, write \(A(x)=\sum_{d\leq x}\mu^2(d)r_2(d)=\kappa x+E(x)\), with the permitted coarse bound \(E(x)\ll x^\sigma\), \(1/2<\sigma<1\). On a smooth dyadic block \(d\asymp N\), Abel summation against
\(g(d)=d^{-3/4}\Psi(\sqrt{d/T})e(R\sqrt d)\) costs, for \(N\asymp T\),

\[
 \int g\,dE\ll N^{\sigma-3/4}(1+R\sqrt N)
 \ll T^{\sigma+3/4}\qquad(R\asymp T).
\]

This is worse than its elementary \(T^{1/4+\varepsilon}\) absolute sum. It is a bound for this attempted use of coarse summatory information, not a lower bound for the actual residual. Exact annihilation of a continuous main term, if independently established, does not improve the bound for \(\int g\,dE\). None of the two audited theorems supplies the required moving-support residual estimate.

## 4. First doubtful or unproved step

There is no new candidate theorem for promotion. The first illegal step in using Audit 1 is letting its truncation reach even \(Q\), much less the complete support \(n\asymp T\), or dropping the entire complement after proving its finite head is equidistributed. The first missing hypothesis in Audit 2 is an optimal absolute moment of order \(A_0>12\).

For the proposed density-subtraction approach, the first unproved step is a signed estimate for the arithmetic remainder at frequency resolution \(1/T\), retaining the real-window kernel and the full harmonic/sign pairing. A continuous cancellation identity alone does not provide it. The reviewed harmonic-absolute lower bound \(T^{5/2}\) in the frozen brief remains an obstruction to that absolute certificate only; it is not a lower bound for signed \(I_{12}\).

## 5. Required controls and outcomes

1. **Cutoff/unit control — passed.** The source variable is squared radius. Setting \(U=T\) would give the wrong scale. Correctly setting \(U=T^2\) gives \(1/2072\), still far below \(2/5\). The high-class truncation is empty, exactly.

2. **Coefficient/sign control — passed as a limitation.** Audit 1 permits arbitrary uniformly bounded real coefficients. Its root-separation mechanism does not distinguish the actual arithmetic weights from bounded adversarial ones. Its restricted support explains why this does not contradict the supplied full-support adversarial control. No arithmetic-specific gain is hidden in this theorem.

3. **Rare-spike control for distribution-to-moment transfer — failed implication.** On a radius window of length \(T\), put a test spike of height \(T^\beta\) on a set of measure \(T^{-2\beta}\). Its normalized distribution mass is \(T^{-1-2\beta}\), smaller than any inverse power of \(\log T\); its unnormalized second moment is one. Nevertheless its twelfth moment is \(T^{10\beta}\). Its \(A_0\)-moment is \(T^{(A_0-2)\beta}\leq T\) whenever \(A_0\leq2+1/\beta=9.753960509\ldots\), including \(184/19\). Thus low moments, a sharp cap, limiting laws, and logarithmic distribution discrepancy do not force the needed twelfth-moment gain. This is a logical countermodel to that inference, not a model asserted to arise from circle coefficients.

4. **All-partners control — passed.** The finite head, all omitted high harmonics/classes, the real window, and all sign patterns were kept distinct. No estimate for one was assigned to its complement. Smooth density subtraction was tested directly by Abel summation rather than treated as a residual bound.

5. **Bounded arithmetic diagnostic — passed, diagnostic only.** Two short PowerShell scalar evaluations checked \(10\beta\), \(13\beta-1/2\), \(1/2072\), \(2053/4144\), and the restoration table. No simulation or asymptotic inference was used; the displayed algebra supplies the derivations. Analytical effort exceeded 95 percent.

## 6. Exact provenance and isolation

Campaign/task: `prelaunch231 / signed_correlation_sources`; role: targeted primary-literature auditor; status: source applicability report, not claimant of an accepted theorem. Written 2026-10-11, approximately 03:26 UTC. Frozen graph provenance tag supplied by the brief: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

Only the assigned brief and its permitted local contexts were read. The proof graph, active campaign, sibling reports, legacy rounds, synthesis, and validation matrix were not read or edited; statement isolation follows the narrower conductor brief. A conductor progress message about a prospective continuum identity was received, but its asserted identity was not imported as a proved dependency.

| Local artifact | SHA256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `strategy/round231_cross_label_admission/briefs/signed_correlation_sources.md` | `5be53ac038b65d1deb2cdc8477d818bf76ded5056f92dc18bb20ecd2eb271b0e` |
| `strategy/round231_cross_label_admission/briefs/complete_target.md` | `8ee37ee007ff58b8cda6db3d33205c0896639099a44be159ff930a7e86b19809` |
| `strategy/gauss_circle_strategy_checkpoint_round230_2026-10-11.md` | `d8dadae0d42e0b84a31fda14a132556e3fd2fdccfdf6b37c782564c4721fc34b` |

Primary source records, all accessed 2026-10-11:

- Lamzouri, *On the distribution of the error terms in the divisor and circle problems*: [version record](https://arxiv.org/abs/2410.03652), [fixed v1 text](https://arxiv.org/html/2410.03652v1). The record lists v1, 4 October 2024. Audited Proposition 3.1 and its proof; surrounding distribution statements were classified only. This is the closest located theorem to signed six-versus-six finite correlations, because its proof explicitly includes mixed \(k,\ell\) moments with \(k+\ell\leq h\).
- Zhai, *On higher-power moments of Delta(x) (II)*: [publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/114/1/83024/on-higher-power-moments-of-mit-delta-x-ii), [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83024), [arXiv record](https://arxiv.org/abs/0805.1270). Audited publisher Theorem 3, definitions on pp.35–36, and its range. The publisher article is 2004; its later arXiv upload is not a theorem revision established here.

Search ledger, exactly four batches (three queries each):

1. `"circle problem" "twelfth moment"`; `"sum" "square roots" "six" "spacing" moment`; `"circle problem" "higher moments" Zhai`.
2. `"On higher-power moments" "II" Zhai circle arxiv`; `"square roots" "spacing" "Robert" "Sargos"`; `"circle problem" "limiting distribution" "moments" Heath-Brown`.
3. `"On the Distribution of the Error Terms in the Divisor and Circle Problems" arxiv`; `"square roots" "sixth" "spacing" number theory`; `"square roots" "twelfth" moment exponential sums`.
4. `"square roots" "correlations" "r(n)" circle`; `"circle problem" "signed" "moments"`; `"square roots" "spacing" "twelve"`.

Several spacing searches returned irrelevant material or four-root leads. No additional spacing theorem was audited or imported. No secondary source was used as mathematical evidence. Web opens and one network retry retrieved the two selected primary sources; they were not additional search batches. This deliberately did not repeat the broad Round230 source survey.

## 7. Recommended state effect

**No change.** Retain the accepted complete moment and all open obligations. Record the exact finite-truncation cutoff obstruction and the circular high-moment hypothesis as source-admission failures. Neither result rules out genuine signed arithmetic cancellation. No analytic successor, graph promotion, proof-draft change, or source-based exponent improvement is recommended from this bounded audit alone.
