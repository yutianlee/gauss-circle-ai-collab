## Selected main route

Source basis: the uploaded Round 26 judge packet asks A1 to synthesize Round 26 under the Stage C schema, with active agents A1, A2, and A3 only; it also requests one fenced Markdown block for the final answer. The same packet records that Round 27 should remain validation-forward, that A1 should lock down the proof draft, A2 should freeze the $\mathcal M_2$ convention and deliver A3-ready formulas, and A3 should produce committed tables and scripts. Round 25 had already assigned Round 26 to be a verification-execution round, with the residual side treated as controlled by H4 plus R5-Full and with M9, especially $\mathcal M_2$, as the active bottleneck.

Keep the balanced arithmetic hyperbola/Vaaler framework as the selected route:

$$
P(X)=N(\sqrt X)-\pi X
\longrightarrow
\text{symmetric hyperbola}
\longrightarrow
\text{floor-compatible sawtooth}
\longrightarrow
\text{finite Vaaler}
\longrightarrow
\text{fixed-coefficient reciprocal main sums}.
$$

The conservative Round 26 bridge remains:

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

This is a conditional reduction only. Round 26 proves no new Gauss circle exponent. M9 remains open.

The accepted arithmetic identity remains:

$$
P(X)
=
-4\sum_{d\le y}\chi_4(d)\psi_F(X/d)
+
4\sum_{d\le y}
\left[
\psi_F\left(\frac{X/d+1}{4}\right)
-
\psi_F\left(\frac{X/d+3}{4}\right)
\right]
+
O(1),
$$

where

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
\psi_F(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi_F(n)=-\frac12.
$$

For active dyadic denominator blocks,

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ are removed before Vaaler expansion and bounded directly using $|\psi_F|\le 1/2$.

The official M9 target remains fixed-coefficient only. Use

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1.
$$

The two active main sums are:

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_{d\asymp D}
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h,
\end{cases}
$$

one may also write

$$
\mathcal M_2(D;X)
=
8i
\sum_{\substack{1\le |h|\le H_D\\2\nmid h}}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

The open endpoint-strength estimate is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for all active dyadic $D$.

External anchors remain stable. Vaaler's source is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc. (N.S.)* 12(2), 183--216, 1985. Li--Yang's paper is Xiaochun Li and Xuerui Yang, "An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem," arXiv:2308.14859v2; the arXiv abstract says the proof uses the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley's second-spacing results. Li--Yang remains a theorem-application guardrail, not an endpoint input for M9.

## Useful fragments by source

### From A1

A1 supplies the strongest proof-draft consolidation. The most useful contributions are H4 source normalization, R5-Full edge-case handling, the conditional bridge, frozen M9 definitions, paired implementation formulas, and algebraic guardrails. The Round 26 prompt assigned A1 exactly this proof-draft/state-update role, including H4-R25, R5-Full-R25, Bridge-R25, M9-R25, lemma-bank updates, gap-register updates, an A3 table template, and a one-page $\Delta$-method or shifted-convolution checklist.

The Vaaler statement to carry forward is:

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

with

$$
|R_H^F(t)|\le \frac1{2H+2}K_H(t),
$$

where

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2.
$$

The source labels to preserve are Vaaler Theorem 6, printed p. 192, equation (2.28), for $\widehat J$; Section 7, printed p. 207, equations (7.1)--(7.3), for $i_N,j_N,k_N$; and Theorem 18, printed p. 210, equations (7.13)--(7.17), especially equation (7.14), for the residual inequality. This remains a source-normalized proof-draft item; final rendered-page transcription should still be verified.

The endpoint conversion is correct and important. Vaaler's centered trigonometric polynomial has value $0$ at integers, while the arithmetic sawtooth has $\psi_F(n)=-1/2$. The Fejer majorant covers the discrepancy because

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

A1's R5-Full product-count proof remains the official residual mechanism. With

$$
H\asymp D X^{-1/4},
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

the standard Fejer bound gives

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg, choose $m$ nearest to $X/d$. Since $d\asymp D$,

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

Using

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min(1,\Delta^2/u^2),&u\ne0,
\end{cases}
$$

one has

$$
\frac1H K_H(X/d)\ll W_\Delta(X-md).
$$

Grouping by $n=md$ gives divisor multiplicity at most $\tau(n)$, hence

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)W_\Delta(X-n)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For shifted residual legs, near-integrality of

$$
\frac{X/d+\rho}{4},
\qquad \rho\in\{1,3\},
$$

is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing

$$
\ell=4m-\rho
$$

gives $n=d\ell$ and $\ell\equiv-\rho\pmod 4$, with the congruence restriction only reducing multiplicity. This removes the fixed Fejer residual from the active bottleneck, conditional on H4.

The stable algebraic guardrails are:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

and

$$
\Phi(u)+\Phi(1-u)=1.
$$

Thus $\Phi(1-u)=\Phi(u)$ is false except at $u=1/2$.

For real dyadic weights, the paired implementation formulas should remain:

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{h=1}^{H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}
A_h(D;X),
$$

where

$$
A_h(D;X)
=
\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\operatorname{Re}B_h(D;X),
$$

where

$$
B_h(D;X)
=
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

These are implementation identities only. They require real $w_D$ and raw two-sided complex regression.

### From A2

A2 supplies the strongest new analytic object: the two-sided $\mathcal M_2$ fourth-moment framework. The A1 review identifies A2's fourth-moment expansion and cleared-denominator resonance integer as the right finite object for testing whether the $\chi_4(h)$ signs survive beyond second-moment Cauchy.

Use the two-sided convention

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
\beta_h=\alpha_{h,H_D}C_h,
$$

where

$$
C_h=e(h/4)-e(3h/4).
$$

Then

$$
\mathcal M_2(D;X)=4S_2(D;X).
$$

A sufficient fourth-moment target is

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}.
$$

The exact fourth-moment phase is

$$
\frac{X}{4}
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right),
$$

and the cleared-denominator resonance integer is

$$
N
=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

Promote this expansion and the resonance integer as proved algebraic identities. Do not promote the taxonomy as complete. Named diagonal and pair-swapped families appear compatible with the fourth-moment target, but denominator-paired singular cases, mixed denominator patterns, truncation-edge cases, and near-collision bands remain unresolved.

A2's CRI statistic is useful under a fixed convention. Define

$$
\Sigma_r(D;X)
=
\sum_{\substack{1\le |h|\le H_D\\h\equiv r\pmod4}}
\alpha_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad r\in\{1,3\}.
$$

Then, under the two-sided convention,

$$
S_2(D;X)=2i(\Sigma_1-\Sigma_3),
$$

and

$$
|S_2(D;X)|^2=4|\Sigma_1-\Sigma_3|^2.
$$

The ratio

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}
$$

is a falsification statistic, not a theorem-level sufficient condition. Values near $1$ are neutral; values near $0$ justify more proof work; values near $2$ are adverse.

A2's $\Delta$-method direction should remain exploratory. The useful minimum artifact is an exact transformed off-diagonal object of the form

$$
\sum_{c\le Q}\frac1c
\sum_{a\bmod c}^{*}
e\left(\frac{aN}{c}\right)
\mathcal W_c(N),
$$

with $N$ replaced by the actual fourth-moment expression and with the $h$-weights $\beta_h=\alpha_hC_h$ retained. The Round 26 reviews agree that A2's current $\Delta$-method sketch is not theorem-level and needs exact normalization, modulus structure, weight functions, error terms, and an implication to M9.

### From A3

A3 finally moved partway from protocol to execution. The A1 review records A3's checks of coefficient conjugacy, special values of $\Phi$, integer-jump handling, tiny R5 residuals, toy raw-vs-paired M9 regression, weighted $h$-Cauchy sign loss for $\mathcal M_2$, a small CRI computation, a toy fourth-moment enumeration, and an H13 endpoint model.

The following A3 checks should be retained as formula-regression evidence only:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

$$
\Phi(u)+\Phi(1-u)=1,
$$

and

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

A3 also correctly flags that paired M9 formulas require real dyadic weights; complex-weight tests should fail against the paired real formulas unless the raw two-sided definitions are used.

A3's current weakness is still scale and reproducibility. Toy examples at small $X$ are useful for catching sign and convention errors, but they do not test near-collision density, endpoint behavior, or asymptotic plausibility. The Stage B reviews identify one raw-vs-paired table as having a possible real/imaginary reporting error and call for larger reproducible tables.

### From the Round 26 strategy addendum

The Round 26 packet includes an actionable possible strategic shift: audit whether Poisson summation in $d$ can relate the primal $\mathcal M_2$ structure to a one-dimensional Hardy-series analogue

$$
X^{1/4}\sum_n n^{-3/4}r_2(n)e(\sqrt{Xn}),
$$

then compare the associated square-root near-collision problem with known one-dimensional spacing frameworks.

This is worth testing, but not as a route pivot. It should enter Round 27 as a bounded validation task: A1 writes the formal B-process/Hardy-collapse derivation with all truncations and weights; A2 compares this object with the existing eight-variable $\mathcal Q_4$ and with a shifted-convolution object; A3 checks a small-scale numerical identity only after A1 supplies an exact formula.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** Round 26 proves no estimate for M9.

2. **Reject treating the bridge as a theorem proving the conjectural bound.** The implication

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

is conditional.

3. **Reject arbitrary-coefficient main sums as active dependencies.** The Vaaler reduction uses fixed coefficients $\alpha_{h,H_D}$. Arbitrary phases, adversarial signs, and $L^1$ norms are stress tests only.

4. **Reject scalar Vaaler residuals.** The residual is controlled by H4 plus R5-Full product counting. Dropping the Fejer kernel would recreate a known false-proof pattern.

5. **Reject $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$.** The correct identity is $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.

6. **Reject $\Phi(1-u)=\Phi(u)$.** The correct identity is $\Phi(u)+\Phi(1-u)=1$.

7. **Reject weighted $h$-Cauchy for $\mathcal M_2$ as character-preserving.** Weighted $|\alpha|$ Cauchy has acceptable diagonal size but replaces $C_h$ by $|C_h|^2$, losing the $\chi_4(h)$ sign.

8. **Reject unweighted $h$-Cauchy for $\mathcal M_2$ as endpoint-viable.** Its endpoint diagonal remains too large.

9. **Reject CRI as sufficient by itself.** CRI is a falsification statistic unless paired with a denominator-scale bound.

10. **Reject the fourth-moment route as proved.** The exact expansion is algebraic; the exact-resonance taxonomy and near-collision estimates are not complete.

11. **Reject the current $\Delta$-method sketch as a theorem dependency.** It needs an exact delta-symbol theorem, modulus range, smooth weight, error term, and transformed sums with the actual $\beta_h$ coefficients.

12. **Reject H13, Mellin--Perron, signed Fourier, Kuznetsov, Lindelof, or the proposed 1D Hardy-collapse route as primary pivots unless one supplies a theorem-level reduction to M9.**

13. **Reject A3 toy-scale computations as asymptotic evidence.** They are formula-regression checks only.

## Known gaps

1. **M9 remains open.** Neither $\mathcal M_1(D;X)$ nor $\mathcal M_2(D;X)$ is proved to be $O_\epsilon(X^{1/4+\epsilon})$.

2. **Rendered Vaaler source transcription.** H4 is source-normalized in substance, but the final proof draft should still verify the theorem, page, and equation labels against the rendered PDF.

3. **R5-Full final drafting.** The product-count proof needs final proof-draft insertion with nearest-integer tie rules, exact resonances, shifted products, short blocks, small-$X$ separation, and dyadic overlap.

4. **$\mathcal M_2$ convention freezing.** A2 and A3 computations need one fixed convention: two-sided $h$ or one-sided paired real. Constants should be reconciled.

5. **Exact-resonance taxonomy for $\mathcal Q_4$.** Named diagonal and pair-swapped families are not a full classification of $N=0$.

6. **Denominator-paired singular cases.** Cases such as $h_1=ac$, $h_3=-bc$, truncation-boundary cases, and zero or near-zero denominators need separate proofs.

7. **Near-collision bands.** Bounds for $0<|N|\sim T$ are not established. The $X^{5/4}$ or $X^{9/4}$ absolute-mass heuristics should be tested, not cited as theorems.

8. **CRI sufficiency gap.** The identity involving $\Sigma_1-\Sigma_3$ is exact under convention, but no theorem converts small CRI into M9.

9. **Li--Yang Case A/B ambiguity.** The typeset PDF should be checked before recording final theorem-range tables.

10. **A3 data gap.** Larger reproducible tables are missing for R5 residuals, M9 raw-vs-paired regression, coefficient-stress tests, M2 Cauchy kernels, CRI, fourth-moment bins, near-collision bands, and H13 endpoint comparison.

11. **B-process/1D Hardy-collapse gap.** The formal Poisson route to a one-dimensional Hardy-series analogue is unproved. Stationary phase amplitudes, Vaaler weights, truncation errors, boundary ranges, and the $n=hk$ aggregation should be written before numerical tests are meaningful.

## New lemmas to add

### H4-R26. Finite Vaaler approximation with floor-compatible residual

**Status:** external theorem dependency, source-normalized in substance; final rendered-page check pending.

For $H\ge1$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

with

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
|R_H^F(t)|
\le
\frac1{2H+2}K_H(t).
$$

At integers, the Fejer majorant covers the half-jump from centered value $0$ to $\psi_F(n)=-1/2$.

### R5-Full-R26. Fejer residual product-count bound

**Status:** proved conditional on H4.

For all active dyadic blocks and for first and shifted sawtooth legs, the Vaaler Fejer residual contributes

$$
O_\epsilon(X^{1/4+\epsilon}).
$$

The proof uses $W_\Delta(0)=1$, product grouping, $\tau(n)\ll_\epsilon n^\epsilon$, shifted products $X\approx d(4m-\rho)$, and short-block separation.

### Bridge-R26. Conditional endpoint reduction

**Status:** conditional theorem.

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

M9 is open, so this is not a proof of the conjectural bound.

### M9-R26. Fixed-coefficient main-term target

**Status:** open analytic target.

For $X^{1/4}\le D\le X^{1/2}$ and $H_D\asymp D X^{-1/4}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

Use actual Vaaler coefficients only.

### M9-Pair-R26. Paired implementation formulas

**Status:** proved implementation identity for real $w_D$.

For real dyadic weights, use the paired formulas for $\mathcal M_1$ and $\mathcal M_2$ stated above. For complex weights, use raw two-sided definitions.

### Alpha-Conjugacy-R26

**Status:** proved algebraic lemma.

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### Phi-Asymmetry-R26

**Status:** proved algebraic lemma.

$$
\Phi(u)+\Phi(1-u)=1.
$$

### C-TwoSided-Convention-R26

**Status:** proved algebraic lemma.

$$
C_h=e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

### M2-CS-Normalizations-R26

**Status:** bounded-scope diagnostic.

Unweighted $h$-Cauchy is too large at the endpoint. Weighted $|\alpha|$ Cauchy has acceptable diagonal size but loses the $\chi_4(h)$ sign through $|C_h|^2$.

### M2-Q4-Expansion-R26

**Status:** proved algebraic identity; analytic estimate open.

For $S_2=\mathcal M_2/4$,

$$
|S_2(D;X)|^4
$$

expands with resonance integer

$$
N
=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

The sufficient target

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

is unproved.

### M2-Q4-Named-Diagonal-Mass-R26

**Status:** proved or derived only for named diagonal and pair-swapped families, depending on the exact family proof.

Named diagonal families appear compatible with the fourth-moment target. This does not classify all $N=0$ configurations.

### M2-Q4-Denominator-Paired-R26

**Status:** derived under assumptions; proof incomplete.

Needs singular-case repair and boundary analysis.

### CRI-Identity-R26

**Status:** proved under a fixed convention; diagnostic only.

Under the two-sided convention,

$$
S_2(D;X)=2i(\Sigma_1-\Sigma_3).
$$

The ratio $R_{\rm CRI}$ is a falsification metric, not a theorem-level sufficient condition.

### Delta-Method-OffDiagonal-R26

**Status:** exploratory only.

Any promotion requires an exact delta-symbol formula, an explicit transformed off-diagonal object, coefficient preservation, and an implication to M9.

### HardyCollapse-Audit-R26

**Status:** exploratory audit target.

Before claiming a reduction from $\mathcal M_2$ to a one-dimensional Hardy-series analogue, derive the Poisson/B-process transform, stationary phase, truncation, Vaaler-weight transfer, and $n=hk$ aggregation with controlled errors.

## Counterexample checks to run

1. **R5 exact-resonance tests.** Use square, near-square, nonsquare, and divisor-rich $X$. Compute first and shifted residuals normalized by $X^{1/4}$.

2. **High-precision Fejer spike safety.** Use exact rational or modular detection near integer arguments. Do not rely on ordinary floating sine quotients near $\sin \pi t=0$.

3. **Raw-vs-paired M9 regression.** For real weights, compare raw two-sided complex definitions and paired real formulas for $\mathcal M_1,\mathcal M_2$. Report real and imaginary parts separately, absolute error, and relative error.

4. **Complex-weight failure check.** Deliberately test complex $w_D$ to confirm paired real formulas fail outside their hypothesis.

5. **Fixed-coefficient stress comparison.** Compare actual Vaaler coefficients with random phases, adversarial signs, and termwise $L^1$ norms.

6. **M2 Cauchy kernel tests.** For weighted and unweighted $h$-Cauchy, report diagonal mass, off-diagonal signed mass, off-diagonal absolute mass, operator norm, and signed/unsigned ratios.

7. **Fourth-moment exact bins.** Enumerate $N=0$ and split into diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified bins.

8. **Near-collision banding.** For $0<|N|\sim T$, report signed mass, absolute mass, and coefficient-weighted mass. Treat the $X^{5/4}$ or $X^{9/4}$ heuristic as a hypothesis to test.

9. **Denominator-paired singular checks.** Isolate $h_1=ac$, $h_3=-bc$, small $|\Delta|$, and truncation-boundary cases.

10. **CRI endpoint tests.** Compute $R_{\rm CRI}$ at endpoint and intermediate $D$ scales. Values near $1$ should deprioritize CRI.

11. **Li--Yang PDF audit.** Resolve the Case A exponent discrepancy from the typeset PDF and record exact hypotheses for $F,g,G,H,M,T$, weights, ranges, and absolute-value placement.

12. **DFI delta-method normalization.** Before using any $\Delta$-method sketch, write the exact delta-symbol theorem, modulus range, smooth weights, error term, and complete-sum structure.

13. **H13 endpoint falsification.** Run at most one endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes, comparing signed dual statistic, unsigned statistic, and diagonal-unitary operator norm.

14. **B-process/Hardy-collapse sanity check.** After A1 supplies the exact transform, test the claimed primal-to-dual identity at small scale. Report it as structural verification only, not asymptotic evidence.

## Research strategy adjustment

Round 27 should be a validation-execution round, not a speculation round. This is consistent with the Round 26 judge packet's recommendation that A1 lock the proof draft, A2 provide A3-ready $\mathcal M_2$ formulas, and A3 run committed tables and scripts.

Allocation:

- **A1: 25%.** Lock the proof draft and state update. Promote only proved algebraic identities, external theorem dependencies, conditional reductions, and bounded diagnostics. Add a short B-process/Hardy-collapse audit because the Round 26 packet contains a specific directive to test that possible structural shift.
- **A2: 35%.** Produce a proof-draft-ready $\mathcal M_2$ finite-statistic packet: one convention, exact fourth-moment expansion, exact resonance taxonomy, CRI identity, denominator-paired repairs, near-collision target bounds, and optional exact $\Delta$-method transformed object.
- **A3: 40%.** Execute reproducible computation. Tables and scripts are now more valuable than additional prose.

Keep Mellin--Perron, signed Fourier, Kuznetsov, Lindelof, H13, $\Delta$-method, and the 1D Hardy-collapse route secondary unless one supplies an exact theorem-level reduction to M9. The main state remains: H4 plus R5-Full provisionally controls the residual; fixed-coefficient M9 is open.

## Next-round prompts by agent

### For A1

Produce the Round 27 proof-draft/state-update and structural-audit packet.

Objectives:

1. Lock down H4-R26 in `best_proof_draft.md` with rendered Vaaler source citations:
   - Theorem 6, printed p. 192, equation (2.28), for $\widehat J$ and the coefficient function;
   - Section 7, printed p. 207, equations (7.1)--(7.3), for $i_N,j_N,k_N$;
   - Theorem 18, printed p. 210, equations (7.13)--(7.17), especially equation (7.14), for the residual inequality.
   Mark any remaining page-label uncertainty explicitly.

2. Insert R5-Full-R26 as a final proof-draft lemma with:
   - nearest-integer tie rule;
   - exact-resonance cap $W_\Delta(0)=1$;
   - shifted products $X\approx d(4m-\rho)$;
   - congruence $\ell\equiv-\rho\pmod4$;
   - positivity of $\ell$ in the large active range;
   - small-$X$ separation;
   - short blocks $D<X^{1/4}$;
   - dyadic bounded overlap;
   - logarithmic losses absorbed into $X^\epsilon$.

3. State Bridge-R26 only conditionally:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Explicitly state that M9 is open.

4. Freeze M9-R26 with actual Vaaler coefficients. Keep arbitrary coefficients, random phases, adversarial phases, and $L^1$ norms in a stress-test appendix only.

5. Insert or update the lemma bank entries:
   - H4-R26;
   - R5-Full-R26;
   - Bridge-R26;
   - M9-R26;
   - M9-Pair-R26;
   - Alpha-Conjugacy-R26;
   - Phi-Asymmetry-R26;
   - C-TwoSided-Convention-R26;
   - M2-CS-Normalizations-R26;
   - M2-Q4-Expansion-R26;
   - CRI-Identity-R26;
   - Delta-Method-OffDiagonal-R26 as exploratory only;
   - HardyCollapse-Audit-R26 as exploratory only.

6. Update the gap register with M9, exact-resonance taxonomy, near-collision bands, denominator-paired singular cases, CRI sufficiency failure, $\Delta$-method normalization, Li--Yang PDF ambiguity, A3 data gaps, and the unproved B-process/Hardy-collapse relation.

7. Write a one-page B-process/Hardy-collapse audit for $\mathcal M_2$:
   - start from the raw fixed-coefficient $\mathcal M_2$ definition;
   - apply Poisson or B-process in $d$ with exact constants under $e(t)=e^{2\pi it}$;
   - compute the stationary point and leading amplitude;
   - track the Vaaler coefficient $\alpha_{h,H_D}C_h$;
   - test whether substituting $n=hk$ actually yields a Hardy-series analogue;
   - state all error terms, truncations, boundary ranges, and weights still missing.
   Do not claim a reduction unless every step is controlled.

8. Update the reading packet so A2 and A3 use the same two-sided or one-sided $\mathcal M_2$ convention.

### For A2

Produce a proof-draft-ready $\mathcal M_2$ finite-statistic packet.

Objectives:

1. Freeze exactly one $h$ convention: either two-sided $1\le |h|\le H_D$ or one-sided positive $h$ using paired real formulas. State all constants and conjugations.

2. Define

$$
S_2(D;X)
=
\sum_h \alpha_{h,H_D}C_h
\sum_d w_D(d)e(hX/(4d)),
$$

and

$$
\mathcal Q_4(D;X)=|S_2(D;X)|^4.
$$

If using $\mathcal M_2=4S_2$, include the scalar factor $4^4=256$ in fourth-moment statements.

3. Write the complete fourth-moment expansion with actual coefficients $\alpha_{h,H_D}$, actual $C_h$, dyadic weights, conjugations, and exact phase.

4. Use the cleared denominator integer

$$
N
=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

5. Classify exact $N=0$ families:
   - exact diagonal;
   - pair-swapped;
   - semi-diagonal;
   - denominator-paired;
   - mixed denominator patterns;
   - sign-symmetric variants;
   - truncation-edge cases;
   - unclassified residue.

6. For every family, assign one of the statuses:
   `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`.

7. Repair denominator-paired singular cases. Explicitly handle $h_1=ac$, $h_3=-bc$, small $|\Delta|$, and values near the truncation boundary.

8. Define near-collision bands $0<|N|\sim T$ and state the exact signed or absolute bound required over these bands to imply

$$
\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

9. Evaluate the $X^{5/4}$ or $X^{9/4}$ weighted near-collision heuristic. State what it assumes, what it ignores, and exactly what A3 should measure.

10. Define CRI precisely under the chosen convention and state the exact identity linking $\mathcal M_2$ or $S_2$ to $\Sigma_1-\Sigma_3$. Either prove a theorem-level CRI sufficient condition or label CRI only as a falsification metric.

11. Supply A3-ready formulas for:
   - weighted and unweighted M2 Cauchy kernels;
   - CRI ratio;
   - fourth-moment exact bins;
   - near-collision banding;
   - denominator-paired singular checks.

12. Optional exploratory allocation: give exactly one $\Delta$-method or shifted-convolution transformed object. It should include the delta symbol, modulus range, smooth weights, transformed exponential sums, coefficient weights $\alpha_hC_h$, and a target implication to M9. Otherwise keep it as a checklist.

13. Compare the existing eight-variable $\mathcal Q_4$ object with the possible B-process/Hardy-collapse or shifted-convolution object supplied by A1. Do not assert equivalence unless constants, truncations, and errors are controlled.

### For A3

Execute computations and source checks. Do not write another protocol-only response.

Objectives:

1. Provide high-precision R5 residual tables for $X=10^6$ and $X=10^8$, plus at least one square, one near-square, one nonsquare, and one divisor-rich $X$. Include $D=X^{1/4},X^{3/8},X^{1/2}$ when feasible. Normalize results by $X^{1/4}$.

2. For the same samples, compute raw two-sided complex $\mathcal M_1,\mathcal M_2$ and paired real formulas. Use real dyadic weights. Report:
   - raw complex value;
   - paired real value;
   - real and imaginary parts separately;
   - absolute error;
   - relative error;
   - normalized $|\mathcal M_i(D;X)|/X^{1/4}$.

3. Test complex dyadic weights to confirm the paired real formulas do not apply unchanged.

4. Compare fixed Vaaler coefficients with:
   - random phase coefficients of the same magnitudes;
   - adversarial coefficient heuristics;
   - termwise $L^1$ stress norms.

5. Implement weighted and unweighted $\mathcal M_2$ Cauchy kernels. Report diagonal mass, off-diagonal mass, operator norm, absolute majorant, signed/unsigned comparison, and whether $\chi_4(h)$ survives.

6. Compute CRI ratios

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}{|\Sigma_1|^2+|\Sigma_3|^2}
$$

under the convention supplied by A2. If endpoint values are near $1$, record CRI as neutral or deprioritized.

7. Enumerate fourth-moment exact-resonance bins for feasible ranges. Report signed and absolute weighted mass by bin.

8. Bin near-collisions $0<|N|\sim T$ and compare observed masses to A2's stated heuristic. Use exact integer arithmetic for $N$.

9. Test denominator-paired singular cases separately, especially $h_1=ac$, $h_3=-bc$, small $|\Delta|$, and truncation boundaries.

10. Resolve the Li--Yang Case A ambiguity using the typeset PDF. Record exact theorem hypotheses for $F,g,G,H,M,T$, weights, ranges, and absolute-value placement.

11. Run at most one H13 endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes. Compare signed dual statistic, unsigned statistic, and diagonal-unitary operator-norm comparator.

12. If A1 supplies a B-process/Hardy-collapse formula, write a small-scale verification script for the claimed primal/dual identity. Use it only as formula-regression evidence.

13. Provide reproducible code snippets or exact pseudocode, precision settings, random seeds, and table outputs sufficient for audit.

## Confidence

High confidence:

- The balanced hyperbola/Vaaler route remains the right reduction framework.
- H1--H3 remain accepted arithmetic reductions.
- H4 is source-normalized in substance, pending final rendered-page transcription.
- R5-Full controls the fixed Fejer residual conditional on H4.
- The conditional bridge is valid.
- M9 remains open.
- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- $\Phi(u)+\Phi(1-u)=1$.
- A2's fourth-moment expansion and resonance integer are correct algebraic objects.
- A3's coefficient conjugacy, $\Phi$ asymmetry, integer-jump, and weighted $h$-Cauchy sign-loss checks are correct.
- Li--Yang cannot be imported as a black-box endpoint theorem.

Moderate confidence:

- The paired implementation formulas are correct for real weights.
- A2's named diagonal and pair-swapped fourth-moment families are compatible with the target.
- A2's denominator-paired estimates can likely be repaired into safe upper bounds.
- A3's toy computations are useful for formula regression.
- A bounded B-process/Hardy-collapse audit may clarify whether $\mathcal M_2$ has a lower-dimensional structural avatar.

Low confidence:

- CRI alone supplies an endpoint estimate.
- The fourth-moment route closes M9 without a new signed spacing theorem.
- The current $\Delta$-method sketch implies M9.
- H13 survives serious norm extraction.
- The proposed 1D Hardy-collapse route bypasses the same endpoint reciprocal-sum difficulty.

No exponent improvement should be recorded from Round 26.
