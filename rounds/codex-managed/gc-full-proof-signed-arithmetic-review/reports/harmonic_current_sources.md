# Round 208: current harmonic sources and complete signed high values

Campaign: `gc-full-proof-signed-arithmetic-review`. Task: `harmonic_current_sources`.
Role: source auditor; selected-context, nonblind candidate report.
Date checked: 2026-09-27. Starting graph SHA256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Effort: analytical/algebraic/source inspection 100%; numerical experimentation 0%.
No graph promotion or successor design is made here.

## 1. Result: a costed method obstruction, with the actual estimate still open

The bounded current primary-source search supplies no verified new complete
arithmetic estimate improving the accepted distribution. In particular, the
September 2026 Gauss-circle item located in this search is numerical evidence,
not a new asymptotic upper-bound theorem. Both previously identified withdrawals
remain withdrawn. This is a statement about the inspected corpus, not a claim
that no other paper exists.

Two exact harmonic interfaces are costed below, both from the current
Guth--Maldague v2: the small-cap parabola theorem and its amplitude-dependent
parabola envelope theorem. These are distinct applications, not newly published
results. The exact square-root lift preserves the physical coefficients, but
ordinary small-cap decoupling followed by a paid line trace gives only

\[
 \int_{R\asymp T}|S_N(R)|^{12}\,dR
       \ll_\varepsilon T^{1+\varepsilon}N^2
 \tag{H1}
\]

for an actual dyadic square-root sum. Complete recombination gives
\(M_{12}\ll T^{3+\varepsilon}\), hence a sharp-discrepancy moment
\(\int|P(x)|^{12}dx\ll Y^{5+\varepsilon}\). This is inferior to the
accepted bound, not a lower bound or a no-go theorem for all decoupling methods.
The amplitude-dependent theorem exposes an exact arithmetic envelope inequality
but supplies no bound for that envelope on these actual coefficients.

The useful complete target remains the **actual signed high-value remainder**
in (H4) below. It retains all frequencies and exceptional peaks. It is an
equivalent milestone after the already proved low-value contribution is paid;
it is not an easier theorem already furnished by the literature. Its full-proof
analogue must control arbitrarily high fixed moments, not only order twelve.

## 2. Exact statements and hypotheses

Use the accepted mollifier, window, and inclusive discrepancy conventions:

\[
 B_T(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
           \cos(2\pi R\sqrt n-3\pi/4),\qquad
 D_T(V)=\int w(R/T)1_{|B_T(R)|>V}\,dR.
\]

Here \(T\ge2\) is real, \(w\) is fixed, bounded and nonnegative, supported
in a fixed positive compact interval. For sharp reconstruction take \(w=1\)
on \([1/\sqrt2,\sqrt3]\) and the Fourier transform of a nonnegative radial
smooth unit-mass disk-supported mollifier for \(\Psi\). Let

\[
 \theta=\frac{3292+25\sqrt{1717}}{13762},\quad
 \beta=2\theta-\frac12,\quad q=\frac{136}{13},\quad a=\frac{13}{125}.
\]

The accepted input, including its full tail and real endpoints, is

\[
 D_T(V)\ll T^\varepsilon(V^{-2}+TV^{-q}),\quad V\ge1,
 \qquad \|B_T\|_\infty\ll T^{\beta+\varepsilon}.
 \tag{H2}
\]

The exact milestone is

\[
 M_{12}(T):=\int w(R/T)|B_T(R)|^{12}dR
                  \ll T^{29/25+\varepsilon}.
 \tag{H3}
\]

At epsilon-loss level, using (H2), this is equivalent to

\[
 \boxed{\quad
  \int_{T^a}^{\infty} V^{11}D_T(V)\,dV
                         \ll T^{29/25+\varepsilon}.
 \quad}                                                   \tag{H4}
\]

Writing infinity avoids an unjustified deletion at exactly \(T^\beta\):
the known supremum permits replacement only by
\(C_\eta T^{\beta+\eta}\), for any fixed \(\eta>0\).

For the source applications put

\[
 S_N(R)=\sum_{N<n\le2N}a_n e(R\sqrt n),\qquad
 a_n=r_2(n)n^{-3/4}\Psi(\sqrt{n/T})\zeta_N(n),
 \tag{H5}
\]

where \(\zeta_N\) is a bounded smooth dyadic cutoff, or a sharp/partial
block zero-extended to this interval. For any fixed \(K\), with a harmless
change of Schwartz seminorms,

\[
 A_N:=\sum|a_n|\ll_\eta N^{1/4+\eta}(1+N/T)^{-K},\qquad
 E_N:=\sum|a_n|^2\ll_\eta N^{-1/2+\eta}(1+N/T)^{-K}.
 \tag{H6}
\]

The two audited source specializations are as follows. They are statements of
external analytic tools, not accepted new project nodes.

* **Interface I:** [Guth--Maldague, arXiv:2206.01093v2, Theorem 5](https://arxiv.org/html/2206.01093v2),
  specialized to \(p=12,q=2\). For a Schwartz function Fourier-supported in
  an \(\mathcal R^{-1}\)-neighborhood of the truncated parabola, partitioned
  into \(\mathcal R^{-b}\times\mathcal R^{-1}\) caps, \(1/2\le b\le1\),
  it gives
  \[
   \int_{B_{\mathcal R}}|f|^{12}
   \ll_\varepsilon\mathcal R^\varepsilon
    (2+\mathcal R^{5b-1})
      \left(\sum_\gamma\|f_\gamma\|_{12}^2\right)^6.
   \tag{H7}
  \]
  The theorem's admissibility condition is \(3/p+1/q\le1\), met here.
* **Interface II:** [the same v2, Theorem 4](https://arxiv.org/html/2206.01093v2).
  With the same Fourier support, canonical caps \(\vartheta\), and
  envelopes \(U\) of dimensions \(W\times\mathcal R\),
  \(\sqrt{\mathcal R}\le W\le\mathcal R\), define
  \[
   \mathcal E_f(v)=\sum_{W,\tau}\sum_{U\in\mathcal G_\tau(v)}
      |U|^{-1}\left\|\left(\sum_{\vartheta\subset\tau}
                    |f_\vartheta|^2W_U\right)^{1/2}\right\|_2^4.
  \]
  Here \(\mathcal G_\tau(v)\) retains envelopes whose average square
  function is at least \(v^2/(\#\tau)^2\), up to the source's
  \(C_\varepsilon\mathcal R^\varepsilon\), with \(\#\tau\) counting
  occupied coarse caps at that scale. Then
  \(v^4|\{|f|>v\}|\ll_\varepsilon\mathcal R^\varepsilon\mathcal E_f(v)\).

The exact source statement was inspected in the introduction, Theorems 4--5;
the version header is 13 August 2022. The source's cone theorem is not silently
substituted for its parabola theorem. The calculations that follow are our
application ledger, not claims printed in that paper.

## 3. Derivations and complete restored costs

### A. Existing distribution versus the remaining arithmetic inequality

Layer cake and (H2) give, below \(V_0=T^a\),

\[
 \int_0^{V_0}V^{11}D_T(V)dV
 \ll T^{1+\varepsilon}+T^{10a+\varepsilon}
                 +T^{1+(12-q)a+\varepsilon}
 \ll T^{29/25+\varepsilon},
\]

because \(10a=26/25\), \(12-q=20/13\), and
\(1+(20/13)a=29/25\). Positivity of layer cake gives the converse
implication (H3) => (H4). Thus (H4) loses neither the low values nor a rare
peak. The present complete bound for its right side is

\[
 T^{10\beta+\varepsilon}+T^{1+(20/13)\beta+\varepsilon},
\]

whose first term dominates because \(\beta(q-2)>1\). The required net
moment saving is therefore \(10\beta-29/25>0\), not a saving in a selected
spacing count or a transformed summand. For the particular sufficient
two-term distribution improvement

\[
 D_T(V)\ll T^\varepsilon
     (T^{-\sigma}V^{-2}+T^{1-\tau}V^{-q})\quad(V\ge T^a),
\]

the necessary power conditions for this certificate are
\(\sigma\ge10\beta-29/25\) and
\(\tau\ge(20/13)\beta-4/25\). Neither improvement is established.

The amplitude and Jacobian in sharp reconstruction are

\[
 P(R^2)=\pi^{-1}\sqrt R B_T(R)+O(T^{1/2+\varepsilon}),\qquad
 dx=2R\,dR.
\]

Consequently (H3) yields \(T^{7+29/25}=Y^{102/25}\) for the sharp
twelfth moment, including a smoothing-error moment \(O(Y^{4+\varepsilon})\).
The monotonicity bridge then gives \(102/325\), not \(1/4\).
For fixed \(p\), a radius moment \(M_p\ll T^{E_p+\varepsilon}\) gives,
with \(E_p^*=\max(1,E_p)\) retaining the sharp reconstruction error,

\[
 \rho_p=\frac{p/4+(1+E_p^*)/2}{p+1}
        =\frac14+\frac{1/4+E_p^*/2}{p+1}.
 \tag{H8}
\]

Thus \(E_p=o(p)\) along arbitrarily large fixed orders is sufficient for
the quarter theorem. The accepted \(E_p=\max(1,(p-2)\beta)\) tends back
to \(\theta\). Constants may depend on fixed \(p\); no moment order
growing with \(T\) is used. This is a nonblind verification of the hierarchy;
the independent statement-only review belongs to the conductor's other task.

### B. Interface I: exact parabola lift, transverse trace, and scales

The finite weighted lift is

\[
 F_N(x,t)=\sum_{N<n\le2N}a_n
       e\left(x\frac n{2N}+t\sqrt{\frac n{2N}}\right),
 \quad t=\sqrt{2N}\,R.
 \tag{H9}
\]

Its frequencies, after swapping coordinates, are
\((\xi_n,\xi_n^2)\) with \(\xi_n=\sqrt{n/(2N)}\in[1/\sqrt2,1]\).
They have separation comparable to \(1/N\). This is an exact lift, with
\(dt=\sqrt{2N}\,dR\); there is no Taylor approximation or integer-radius
restriction. In particular, its trace is not an ambient mean.

For \(2\le N\le T^{3/2}\), set \(L\asymp T\sqrt N\) and
\(\mathcal R\asymp\min(L,N^2)\), with fixed constants adjusted for the
window. Cover the \(t\)-interval by
\(O(1+L/\mathcal R)\) intervals of length \(\mathcal R\). On each,
multiply by a fixed Schwartz cutoff at scale \(\mathcal R\), with Fourier
support a sufficiently small ball of radius \(\mathcal R^{-1}\), bounded
below on the central physical ball. A translation only modulates the
coefficients and preserves (H6). This supplies exactly the required Fourier
support and Schwartz hypothesis.

Choose cap width comparable to \(1/N\), so
\(b=\log N/\log\mathcal R\in[1/2,1]\). If \(N\ll T^{2/3}\), use
\(\mathcal R\asymp N^2\) and many intervals; if
\(N\gg T^{2/3}\), use \(\mathcal R\asymp L\) and boundedly many.
At the transition either choice works. Each cap contains boundedly many
frequencies. Hence

\[
 \left(\sum_\gamma\|f_\gamma\|_{12}^2\right)^6
       \ll\mathcal R^2 E_N^6,
 \qquad
 2+\mathcal R^{5b-1}\ll N^5/\mathcal R.
\]

The area factor \(\mathcal R^2\) is retained. Inserting (H6) gives the
per-interval ambient bound
\(\mathcal R^{1+\varepsilon}N^{2+\varepsilon}\), with the corresponding
Schwartz decay when \(N>T\).

For completeness, the paid trace uses a one-dimensional reproducing kernel
in \(x\). The \(x\)-frequency support is in a fixed compact interval, so
Holder gives
\(|F_N(0,t)|^{12}\ll\int |F_N(x,t)|^{12}(1+|x|)^{-K}dx\).
On \(|x|\ll\mathcal R\) the localized function above dominates the
integrand up to a fixed constant. The remaining integral is
\(O_K(A_N^{12}\mathcal R^{-K})\); choose a fixed sufficiently large
\(K\) and sum it over the intervals. This avoids assuming a compactly
supported function can simultaneously have compact Fourier support.
The source estimate is applied on a fixed enlargement of its ball.

The final line integral is therefore

\[
 \begin{aligned}
 \int_{R\asymp T}|S_N(R)|^{12}dR
 &\ll T^\varepsilon N^{-1/2}
       (1+L/\mathcal R)\mathcal R N^2\\
 &\ll T^{1+\varepsilon}N^2 .
 \end{aligned}                                             \tag{H10}
\]

All ceilings are included. The finitely many bounded \(N\) blocks cost
\(O(T)\). Coefficient weights have not been replaced by unweighted sums.
The cosine is \(\Re(e(-3/8)S_N)\), so bounding its norm by the complex
norm handles both original phases, at the price of a sufficient stronger
estimate. No exceptional set is discarded.

Using the Schwartz factors in (H6), Minkowski over all dyadic blocks up
to \(T^{3/2}\) yields \(M_{12}\ll T^{3+\varepsilon}\): the largest
scale contribution is \(TN^2\) at \(N\asymp T\), with a summable
decaying tail above. The remaining infinite tail is \(O_K(T^{-K})\)
by the accepted complete-series kernel. Hence this complete import produces
\(Y^{5+\varepsilon}\), and its pointwise certificate is \(5/13\).
For a single middle scale \(N=T^\alpha\), its radius exponent is
\(1+2\alpha\), already larger than \(29/25\) throughout
\(52/125<\alpha<99/125\). Capping this certificate by the accepted bound
recovers the existing exponent and supplies no gain.

### C. Interface II: exact amplitude-dependent trace cost

Use (H9) localized at scale \(L\asymp T\sqrt N\) over the entire radius
window, and call the result \(f_N\). For \(|S_N(R)|>V\), the bound
\(|\partial_xF_N|\ll A_N\) preserves a fixed fraction of its amplitude
on an \(x\)-interval of length \(cV/A_N\), whenever \(0<V\le A_N\).
The cutoff is bounded below there. Thus the ambient level measure is at least
\(c\sqrt N(V/A_N)D_N(V)\), where
\(D_N(V)=|\{R\text{ in the window}:|S_N(R)|>V\}|\).
Theorem 4 consequently gives

\[
 \boxed{D_N(V)\ll_\varepsilon
    T^\varepsilon\frac{A_N}{\sqrt N}\,V^{-5}
            \mathcal E_{f_N}(cV).}                         \tag{H11}
\]

The \(V^{-5}\), \(A_N\), and \(N^{-1/2}\) are the full trace cost;
one cannot insert the ambient \(V^{-4}\) bound directly into a radius
distribution. For example, a sufficient arithmetic envelope inequality for
a block's twelfth-moment contribution over all its levels is

\[
 \frac{A_N}{\sqrt N}\int_0^{A_N}
          V^6\mathcal E_{f_N}(cV)dV
                \ll T^{29/25+\varepsilon}.                \tag{H12}
\]

Alternatively, to certify the pointwise level bound
\(D_N(V)\ll T^{29/25+\varepsilon}V^{-12}\), it suffices to prove
\(\mathcal E_{f_N}(cV)\ll
 T^{29/25+\varepsilon}\sqrt N A_N^{-1}V^{-7}\).
For a typical undecayed block the prefactor \(\sqrt N/A_N\) is
\(N^{1/4}\) up to subpowers. These are **unproved arithmetic requirements**,
not conclusions of the source. They include every retained coarse envelope,
every occupied cap, and every narrow or aligned packet.

Summing valid block bounds costs only powers of \(\log T\), but proving
(H12) is stronger than the signed cosine target and is not justified by
the coefficient energy (H6). There is consequently no numerical exponent
improvement to restore from Interface II: the final arithmetic norm is open.
The complete achieved bound after taking the minimum with existing input
remains \(T^{10\beta+\varepsilon}\), hence
\(Y^{1+10\theta+\varepsilon}\). This does not improve pointwise \(\theta\).

## 4. First doubtful or unproved step

For the direct complete route the first missing statement is exactly (H4),
with the fixed arithmetic \(r_2(n)\), the actual cosine phase, the full
Schwartz series, and no removed exceptional set. In the amplitude-envelope
application it is (H12), or an adequate integrated substitute; a broad/narrow
decomposition does not estimate its narrow part.

There is a rigorous coefficient-uniform obstruction to claiming such a gain
from energy and generic harmonic estimates alone. For
\(a_n=N^{-3/4}e(-R_0\sqrt n)\) on \((N,2N]\), the value at \(R_0\)
is comparable to \(N^{1/4}\), persisting on an interval of length
\(cN^{-1/2}\). Its twelfth moment is at least \(cN^{5/2}\).
Taking \(N\asymp T^{4\beta}\) respects the same coefficient energy and
supremum scales and yields \(T^{10\beta}\), above the milestone.
This synthetic coefficient family is not an arithmetic counterexample;
it identifies precisely why removing the one-peak term requires additional
information about the actual family.

The Round 207 lower bound \(X^3H\) is likewise only a lower bound for a
specified termwise absolute majorant. It cannot replace (H4) by a signed
lower bound, and does not rule out cancellation after grouping equal total
frequencies. Neither this report nor the source theorem provides that missing
arithmetic cancellation.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `full_quarter_scope` | Pass as a scope audit: (H8) distinguishes a fixed p12 milestone from arbitrarily high fixed moments. The quarter theorem remains open. |
| `complete_ranges` | Pass for the stated ledgers: both decoupling scale regimes, bounded blocks, zero-extended partial blocks, all dyadic blocks and the infinite tail are paid. (H4) includes every high level. |
| `actual_coefficients` | Pass: (H5)--(H6) retain r2 and the exact cutoff; generic energy alone is explicitly inadequate for the desired saving. |
| `signed_absolute_distinction` | Pass: norms use the actual sum before absolute values; the complex block route is labeled stronger. Round 207's majorant is not treated as a signed lower bound. |
| `all_costs_restored` | Pass: cap norms, ambient area, interval count, trace, dt, dx, amplitude, smoothing and full tail are explicit. Achieved Interface I exponent is Y^5, not an improvement. Interface II has an unproved final arithmetic norm. |
| `real_endpoints` | Pass: arbitrary real windows and radius endpoints are covered; inclusive count jumps remain paid by the accepted reconstruction. No integer sampling theorem is substituted. |
| `source_versions_hypotheses` | Pass for the two stated analytic interfaces; current records and exact theorem statements were inspected. Metadata and statement screens below are not imports. No claim of a complete independent proof audit of the external paper. |
| `independent_hierarchy` | This report is nonblind and does not satisfy the separate independent-review gate. It supplies explicit formulas for comparison with the conductor's isolated rederivation. |

No mathematical numerical experiment was run. The adversarial peak test above
is analytic. The current-source search and file/schema reads are not numerical
evidence for an asymptotic theorem.

## 6. Dependencies, exact artifacts, and bounded source log

Internal files actually used:

* `protocol.md` and the assigned `briefs/harmonic_current_sources.md`;
* `state/active_campaign.yml`;
* `state/proof_obligations.yml`, selectively: `GC-target`, `M9-M1`, `M9-M2`,
  `GC-complete-square-root-large-values-moment-bound`,
  `GC-external-Li-Yang-theta-star`, and related source-status search hits;
* `strategy/round208_full_proof_strategy_review.md`;
* `strategy/gauss_circle_strategy_review_2026-09-23.md`;
* `strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md`;
* `rounds/codex-managed/gc-signed-rational-filter-attack/synthesis.md`;
* `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.

No other task's report or statement-only packet was read. Historical evidence
paths appearing inside the graph or these permitted documents were not opened.

The source corpus was bounded to the records below, plus the stated theorem
text. All record refreshes occurred on 27 September 2026. Searches restricted
to arxiv.org used: `Gauss circle problem improvement 2026 Li Yang withdrawn
arxiv`; `square root exponential sums moments Xiao 2026`; `Guth Maldague
amplitude dependent cone small cap decoupling theorem`; `"Gauss" "circle"
"2026" "improvement"`; `"Gauss" "circle" "September 2026"`; `Gauss circle
discrepancy decoupling large values 2026 site:arxiv.org/abs`; `"circle problem"
"September" "2026"`; `"Gauss circle problem" 2026`; and `"circle problem"
"2026" "Li"`. Some broad queries produced irrelevant or empty hits; those
were not evidence. Known primary record URLs were opened directly to verify
versions and withdrawals. No secondary literature claim is used as a theorem.

| Primary source/version | Inspection level and decision |
|---|---|
| [Li--Yang 2308.14859v2](https://arxiv.org/abs/2308.14859v2), 14 September 2023 | Current official record unchanged. Metadata refresh only; the benchmark comes from the accepted graph's repaired final application. The printed general Proposition 3.1, Case B theorem, and Theorem 4.2 are not imported. No publication status is inferred from absent metadata. |
| [Bourgain--Watt 1709.04340v2](https://arxiv.org/abs/1709.04340v2), 16 July 2023 | Official withdrawal checked: defects in the spacing/reduction arguments remove Theorems 1--3 as dependencies. No theorem import. |
| [Dong--Robles--Zeindler 2601.00292v2](https://arxiv.org/abs/2601.00292v2), 5 January 2026 | Official withdrawal checked: the omitted L^2 factor changes L^5 to L^7 and defeats the claimed improvement. No theorem import. |
| [Guth--Maldague 2206.01093v2](https://arxiv.org/html/2206.01093v2), 13 August 2022 | Full relevant statement inspection, Theorems 4--5, followed by the two application ledgers above. Version refreshed via the official abstract record. |
| [Guth--Maynard 2405.20552v2](https://arxiv.org/abs/2405.20552v2), 7 April 2026 | Current record refresh only. This remains a Dirichlet-polynomial large-values paper; no square-root phase transfer is asserted. The permitted Round205 checkpoint already records the costly packet transfer. Not a third theorem audit here. |
| [Kim--Ko 2511.04503v2](https://arxiv.org/abs/2511.04503v2), 20 December 2025 | Current metadata refresh only. No new weighted-wave-envelope application is imported beyond the limitations retained in the permitted checkpoint. |
| [Xiao 2606.28986v1](https://arxiv.org/html/2606.28986v1), 27 June 2026 | Statement screen: Theorems 1.1--1.2 concern unweighted sums at integer h; second moments require H>=n^(1/2+delta), fourth moments additionally H<=n^(2/3), 0<delta<1/6. For R~T and effective n~T, the fourth-moment upper range fails; actual weights, real sampling and p12 are also absent. No application or extrapolation. |
| [Lamzouri 2410.03652v1](https://arxiv.org/abs/2410.03652v1), 4 October 2024 | Current metadata refresh only. The permitted checkpoint's good-set/large-deviation limitations are retained, not independently reaudited here. No exceptional peak is deleted on its authority. |
| [Yamaguchi--Fujima--Kuratsubo--Nakai--Yoneda 2609.04725v1](https://arxiv.org/abs/2609.04725v1), 4 September 2026 | Current title/abstract/version screen: numerical experiments supporting Hardy's conjecture. It supplies no asymptotic theorem dependency. Its computations were not run. |
| [Gao 2604.23918v1](https://arxiv.org/abs/2604.23918v1), 27 April 2026 | Metadata/abstract screen: representation-weighted smooth-number asymptotics. No unrestricted circle remainder estimate is imported. |
| [Edwin--Lin 2412.05485v1](https://arxiv.org/abs/2412.05485v1), 7 December 2024 | Metadata/abstract screen: Fourier-quasicrystal discrepancy. No new fixed-lattice quarter estimate is inferred. |

The benchmark's exact repairs and nonimplications remain those in
`GC-external-Li-Yang-theta-star`. The current source screen neither strengthens
that qualified accepted statement nor rejects its independently repaired use.

## 7. Recommended state effect

**No change** to accepted mathematics, pointwise exponent, full moment graph,
M1/M2 parents, or proof draft. Retain the external-source qualifications and
withdrawal exclusions. Treat (H10)--(H12) as review evidence requiring the
normal seam checks before any possible graph action.

For the conductor's strategy comparison, select the complete actual estimate
(H4), or the already equivalent complete signed middle-band shell moment, as
the success criterion for an arithmetic attack. Reject ordinary small-cap
decoupling plus generic trace as an improvement mechanism at the priced norms.
Retain amplitude-dependent envelopes only conditionally on an explicit proof
of their missing arithmetic integral; a transform or a broad/narrow split
alone should not trigger another claimed gain.

This recommendation does not prefer a new subdivision and does not start a
successor. It preserves the independent full M1 HARD/SMOOTH and M2
TOP/BAL/UNBAL frontier. A p12 gain would be worthwhile but would still leave
the full quarter theorem and the arbitrarily-high-fixed-moment task open.
