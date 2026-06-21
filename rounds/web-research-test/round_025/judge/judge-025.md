## Selected main route

Source basis: uploaded Round 25 judge packet and Round 25 A1/A2/A3 materials, created on 2026-06-21. The judge packet requires a Stage C synthesis with selected route, useful fragments, rejected/risky ideas, known gaps, new lemmas, counterexample checks, research adjustment, and next-round prompts for A1/A2/A3. The active-agent constraint is A1, A2, and A3 only.

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

Round 25 proves no new Gauss circle exponent and does not prove M9. The conservative bridge remains

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

Here M9 is still open. This is the central state update.

The accepted arithmetic identity remains

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

For active dyadic blocks,

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ are removed before Vaaler expansion and bounded directly by $|\psi_F|\le 1/2$.

The Vaaler coefficients are now frozen as

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1.
$$

The official M9 targets are

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
e(h/4)-e(3h/4)=2i\chi_4(h)
$$

for odd $h$ and is $0$ for even $h$, one may also write

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

The target

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

remains unproved.

External anchors remain stable. Vaaler's source is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc.* 12(2), 183--216, 1985. Project Euclid and AMS metadata verify the paper and bibliographic data. Li--Yang is Xiaochun Li and Xuerui Yang, "An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem," arXiv:2308.14859v2; the abstract states that the proof uses Bombieri--Iwaniec, a new first-spacing estimate, and Huxley second-spacing inputs.

## Useful fragments by source

### From A1

A1 supplies the canonical proof-draft consolidation for Round 25.

The most important contribution is H4 source normalization. The judge prompt required A1 to quote Vaaler Theorem 6, Section 7 equations (7.1)--(7.3), and Theorem 18 equation (7.14), then insert the finite approximation with

$$
\psi_F(t)=\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

$$
|R_H^F(t)|\le\frac1{2H+2}K_H(t).
$$

That assignment and formula are explicitly present in the Round 25 packet. A1's response records the rendered-source anchors as Theorem 6, printed p. 192, equation (2.28), Section 7, printed p. 207, equations (7.1)--(7.3), and Theorem 18, printed p. 210, equations (7.13)--(7.17), especially equation (7.14).

The Fejer kernel is

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

A1 correctly handles the floor-compatible endpoint. At integers, the Vaaler centered polynomial has value $0$, while $\psi_F(n)=-1/2$, and

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

Thus the Fejer residual exactly covers the half-jump.

A1's R5-Full proof remains the residual mechanism. With

$$
H\asymp D X^{-1/4},
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

use

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right),
$$

so

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

Define

$$
W_\Delta(u)
=
\begin{cases}
1,&u=0,\\
\min(1,\Delta^2/u^2),&u\ne0.
\end{cases}
$$

Then

$$
\frac1H K_H(X/d)\ll W_\Delta(X-md).
$$

Grouping by $n=md$ gives multiplicity at most $\tau(n)$, hence

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)W_\Delta(X-n)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the shifted legs, near-integrality of

$$
\frac{X/d+\rho}{4},
\qquad
\rho\in\{1,3\},
$$

is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing $\ell=4m-\rho$ gives $n=d\ell$ and the congruence $\ell\equiv-\rho\pmod4$, which only reduces divisor multiplicity.

A1 also freezes the paired implementation formulas for real dyadic weights. Let

$$
A_h(D;X)=\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
B_h(D;X)=\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Then

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im} A_h(D;X),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re} B_h(D;X).
$$

These are implementation identities, not estimates. They require real $w_D$ and raw two-sided complex regression.

A1's coefficient algebra should be promoted:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

$$
C_h=e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h,
\end{cases}
$$

and

$$
\Phi(u)+\Phi(1-u)=1.
$$

Thus $\Phi(1-u)=\Phi(u)$ is false except at $u=1/2$.

A1 also correctly keeps Li--Yang as a guardrail. The endpoint Vaaler height is

$$
H_D\asymp D X^{-1/4}.
$$

Li--Yang's final record-exponent range corresponds to

$$
H\le MT^{-\theta^*},
\qquad
\theta^*=0.3144831759741\cdots,
$$

not to $H\le MT^{-1/4}$. Therefore black-box endpoint import remains unavailable.

### From A2

A2 provides the main Round 25 analytic object: the $\mathcal M_2$ fourth-moment and CRI finite-statistic framework. The Stage B review scored A2 at 8.3 and identified A2 as the strongest analytic contributor, while requiring completion of exact-resonance taxonomy, denominator-paired singular cases, and near-collision targets.

Define

$$
C_h=e(h/4)-e(3h/4),
\qquad
\beta_h=\alpha_{h,H_D}C_h,
$$

and

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

Then

$$
\mathcal M_2(D;X)=4S_2(D;X).
$$

A sufficient fourth-moment target is

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon},
$$

equivalently

$$
|\mathcal M_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

up to the fixed factor $4^4=256$.

The exact expansion is

$$
|S_2|^4
=
\sum_{\mathbf h}
\sum_{\mathbf d}
\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
\prod_{j=1}^4 w_D(d_j)
e\left(
\frac{X}{4}
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)
\right).
$$

The cleared-denominator resonance integer is

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

This is a useful algebraic object because it preserves the $C_h$ signs through the expansion and avoids the immediate sign loss of weighted $h$-Cauchy. A2's diagonal and pair-swapped mass computation is compatible with the target: the named diagonal families have total weighted mass $\asymp D^2\le X$. The packet records this as a proved mass check for those families only; it does not control all $N=0$ configurations.

A2's CRI identity is also useful after convention freezing. Under the two-sided convention,

$$
S_2(D;X)=2i(\Sigma_1-\Sigma_3),
$$

so

$$
|S_2(D;X)|^2=4|\Sigma_1-\Sigma_3|^2,
$$

and

$$
|\mathcal M_2(D;X)|^2=64|\Sigma_1-\Sigma_3|^2.
$$

The associated ratio

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}
$$

is a falsification statistic, not a theorem-level estimate. Small values are promising; values near $1$ are neutral; values near $2$ are adverse. It is not sufficient unless the denominator is also bounded at the right scale.

### From A3

A3's Round 25 output is useful as formula-regression and source-audit infrastructure. A3 explicitly states that Round 25 does not prove a new exponent or M9, and that the bridge remains conditional because the estimates for $\mathcal M_1,\mathcal M_2$ are open. The Stage B review scores A3 at 7.8: useful execution-oriented verification, but still toy-scale or formula-regression rather than asymptotic evidence.

A3's useful checks are:

- H4 notation and integer-jump convention were checked against Vaaler.
- R5 was tested in small-scale examples, including exact Fejer resonances.
- Raw two-sided complex definitions were regressed against paired real formulas.
- Fixed Vaaler coefficients were compared against random-phase and $L^1$ stress norms in small examples.
- M2 Cauchy kernels, CRI ratios, and fourth-moment bins were examined on very small parameter sets.
- Li--Yang was audited from local TeX.
- One endpoint H13 toy test was run with stationary amplitudes.

These results should be recorded as formula-regression evidence only. They should not be used as asymptotic support for M9.

### From Stage B reviews

The reviews converge on the following points:

1. No Round 25 output proves M9 or a new Gauss circle exponent.
2. A1's proof-draft consolidation should be merged into `best_proof_draft.md`, `lemma_bank.md`, and `gap_register.md`.
3. A2's $\mathcal M_2$ fourth-moment and CRI package is the strongest new analytic object.
4. A3 improved over prior rounds but still needs reproducible scripts and tables.
5. Li--Yang remains a theorem-application guardrail, not an endpoint input.
6. H13 remains one endpoint falsification test, not a primary proof route.

The Stage B recommendation explicitly says to promote only H4/R5/paired-formula algebra and finite-statistic identities, keep M9 open, and keep Li--Yang as a guardrail.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** M9 is open, so the bridge is conditional.

2. **Reject treating M9 as proved.** No agent proved

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

3. **Reject arbitrary-coefficient main-sum variants as active dependencies.** The Vaaler reduction uses the fixed coefficients $\alpha_{h,H_D}$. Arbitrary coefficients, random phases, adversarial signs, and $L^1$ norms are stress tests only.

4. **Reject scalar Vaaler residuals.** The residual is controlled by H4 plus R5-Full product counting. Dropping the Fejer modes remains a false-proof pattern.

5. **Reject $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$.** The correct identity is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

6. **Reject $\Phi(1-u)=\Phi(u)$.** The correct relation is

$$
\Phi(u)+\Phi(1-u)=1.
$$

7. **Reject unweighted $h$-Cauchy for $\mathcal M_2$ at the endpoint.** Its diagonal scale is

$$
D H_D\asymp D^2X^{-1/4},
$$

which equals $X^{3/4}$ at $D\asymp X^{1/2}$, above the squared endpoint target $X^{1/2+\epsilon}$.

8. **Reject weighted $|\alpha|$ $h$-Cauchy as sign-preserving for $\mathcal M_2$.** Its diagonal is acceptable, but it replaces $C_h$ by $|C_h|^2$, hence loses the $\chi_4(h)$ sign and retains only odd-frequency support.

9. **Reject CRI as sufficient by itself.** The full expression

$$
|\Sigma_1-\Sigma_3|^2
=
|\Sigma_1|^2+|\Sigma_3|^2
-
2\operatorname{Re}(\Sigma_1\overline{\Sigma_3})
$$

needs separate control.

10. **Reject the fourth-moment route as proved.** A2's expansion is algebraically useful, but exact-resonance taxonomy, denominator-paired singular cases, sign-symmetric patterns, and near-collision estimates remain incomplete.

11. **Reject the $X^{5/4}$ near-collision warning as a theorem.** It is a warning against absolute majorization and should be tested with actual weights, gcd structure, parity restrictions, and signs.

12. **Reject black-box Li--Yang endpoint import.** The final Li--Yang exponent $\theta^*>1/4$ leaves an endpoint-height gap. The Case A/B display ambiguity should still be resolved from the rendered PDF before any theorem-level range map is finalized.

13. **Reject H13, Mellin--Perron, signed Fourier, Lindelof, Kuznetsov, or $\Delta$-method ideas as active pivots.** They remain comparison or bounded exploratory modules unless an exact transformed object with hypotheses and target implication is supplied.

## Known gaps

1. **M9 remains open.** This is the only active theorem-level analytic bottleneck in the main route.

2. **A2's fourth-moment taxonomy is incomplete.** The exact $N=0$ classification still lacks full control of denominator-paired, mixed, sign-symmetric, truncation-boundary, and unclassified families.

3. **Near-collision bands are unproved.** The bands $|N|\sim T$ need signed and absolute weighted mass estimates. The target should include $\beta_h$ weights, dyadic support, gcd structure, parity, and endpoint truncation.

4. **Denominator-paired singular cases remain sensitive.** Cases such as $h_1=ac$, $h_3=-bc$, or values near truncation boundaries should be isolated and bounded.

5. **CRI convention should be frozen before comparing tables.** One-sided paired-real and two-sided complex conventions have different constants and conjugations.

6. **A3's numerical evidence remains formula-regression scale.** Larger reproducible scripts, raw tables, precision settings, and exact resonance handling are still required.

7. **Li--Yang Case A/B ambiguity remains unresolved at proof-draft level.** A3's local TeX audit is useful, but the rendered PDF still needs reconciliation before any final theorem-range statement.

8. **H13 is not a proof route yet.** The dual phase is Hessian-degenerate, and it is unknown whether the dual $\chi_4$ survives the first realistic norm or spacing extraction.

9. **Potential $\Phi$ taper effects are underused.** Most diagnostics treat $\alpha_h$ as $O(1/h)$. This is safe for upper-bound stress tests but may miss fixed-coefficient structure in actual M9.

10. **No current route supplies the missing signed spacing theorem.** Fourth moments, CRI, BSOS, H13, Kuznetsov, or $\Delta$-method proposals all need a precise theorem-level signed estimate before becoming proof inputs.

## New lemmas to add

### H4-R25. Finite Vaaler approximation with floor-compatible residual

**Status:** external theorem dependency, source-normalized in substance.

For $H\ge1$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}
\alpha_{h,H}e(ht)
+
R_H^F(t),
$$

where

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

The Fejer kernel is

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

At integers, $K_H(0)/(2H+2)=1/2$ covers $\psi_F(n)=-1/2$.

### R5-Full-R25. Fejer residual product-count bound

**Status:** proved conditional on H4.

For all active dyadic blocks and for the first and shifted sawtooth legs,

$$
\text{Vaaler residual contribution}\ll_\epsilon X^{1/4+\epsilon}.
$$

The proof uses $W_\Delta(0)=1$, divisor multiplicity, shifted products $X\approx d(4m-\rho)$, short-block separation, and dyadic bounded overlap.

### Bridge-R25. Conditional endpoint reduction

**Status:** conditional theorem.

If H1--H3, H4, R5-Full, and M9 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

State this as an implication only.

### M9-R25. Fixed-coefficient main-term target

**Status:** open analytic target.

For $X^{1/4}\le D\le X^{1/2}$ and $H_D\asymp D X^{-1/4}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

Use actual Vaaler coefficients only.

### M9-Pair-R25. Paired real implementation formulas

**Status:** proved implementation identity for real $w_D$.

For real weights,

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{h=1}^{H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}A_h(D;X),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\operatorname{Re}B_h(D;X).
$$

### Alpha-Conjugacy-R25

**Status:** proved algebraic lemma.

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### C-TwoSided-Convention-R25

**Status:** proved algebraic lemma.

$$
C_h=e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

### Phi-Asymmetry-R25

**Status:** proved algebraic lemma.

For $0<u<1$,

$$
\Phi(1-u)=1-\Phi(u),
$$

so

$$
\Phi(u)+\Phi(1-u)=1.
$$

### M2-CS-Normalizations-R25

**Status:** bounded-scope diagnostic.

Unweighted $h$-Cauchy is too large at the endpoint. Weighted $|\alpha|$ $h$-Cauchy has acceptable diagonal size but loses the $\chi_4(h)$ sign.

### M2-Q4-Expansion-R25

**Status:** proved algebraic identity; analytic estimate open.

The fourth-moment expansion for $S_2=\mathcal M_2/4$ uses the resonance integer

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

The target

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

is sufficient but unproved.

### M2-Q4-Diagonal-Mass-R25

**Status:** proved for named families only.

The exact diagonal and pair-swapped diagonal families have total weighted mass $\asymp D^2\le X$, compatible with the fourth-moment target. This does not control all $N=0$ families.

### CRI-Identity-R25

**Status:** proved identity under fixed two-sided convention; diagnostic only.

Under the two-sided convention,

$$
S_2(D;X)=2i(\Sigma_1-\Sigma_3).
$$

The ratio

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}
$$

is a falsification metric, not a theorem-level sufficient condition.

### H13-Endpoint-Test-R25

**Status:** bounded exploratory test.

Run exactly one endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes. The test should compare signed dual statistic, unsigned statistic, and diagonal-unitary operator-norm comparator.

## Counterexample checks to run

1. **H4 rendered-page check.** Verify Vaaler Theorem 6, Section 7 equations (7.1)--(7.3), and Theorem 18 equation (7.14) against rendered PDF pages.

2. **Integer jump check.** Confirm

$$
V_H(n)=0,
\qquad
K_H(0)=H+1,
\qquad
K_H(0)/(2H+2)=1/2.
$$

3. **R5 residual tables.** Compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

and

$$
\frac1{H_D}\sum_{d\asymp D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\},
$$

normalized by $X^{1/4}$, for square, near-square, nonsquare, and divisor-rich $X$.

4. **High-precision Fejer resonance safety.** Use exact detection of integer arguments or high precision near $\sin\pi t=0$.

5. **Raw-vs-paired M9 regression.** For real weights, compute raw two-sided complex definitions and paired real formulas for $\mathcal M_1,\mathcal M_2$; report absolute and relative errors.

6. **Complex-weight failure check.** Deliberately test complex $w_D$ or state exclusion; paired real formulas do not apply unchanged.

7. **Fixed-coefficient stress comparison.** Compare actual Vaaler coefficients with random phases of the same magnitudes, adversarial signs, and termwise $L^1$ norms.

8. **M2 Cauchy kernel diagnostics.** Report diagonal mass, off-diagonal mass, operator norm, absolute majorant, and signed/unsigned comparison for both unweighted and weighted $h$-Cauchy.

9. **Fourth-moment exact bins.** Enumerate $N=0$ and split into diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, and unclassified bins.

10. **Near-collision bands.** Bin $|N|\sim T$ and report signed and absolute weighted masses with coefficient weights included.

11. **Denominator-paired singular checks.** Isolate cases near $h_1=ac$, $h_3=-bc$, truncation edges, and zero or near-zero denominator patterns.

12. **CRI endpoint tests.** Compute $R_{\rm CRI}$ at endpoint and intermediate $D$ scales. Values near $1$ should deprioritize CRI.

13. **Li--Yang PDF audit.** Resolve the Case A/B discrepancy using the rendered PDF and record exact hypotheses for $F,g,G,H,M,T$, allowed weights, and absolute-value placement.

14. **H13 endpoint falsification test.** Run one endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes; compare signed dual statistic, unsigned statistic, and diagonal-unitary operator-norm comparator.

15. **Structural alternative sanity check.** If a $\Delta$-method or shifted-convolution alternative is proposed, require one exact transformed off-diagonal object with additive characters, resulting Kloosterman or spectral sums, coefficient weights, and a target implication to M9b.

## Research strategy adjustment

Round 26 should be a verification-execution round, not a new-speculation round.

The main route stays unchanged. The residual side should be treated as infrastructure controlled by H4 plus R5-Full, pending final proof-draft transcription. The active bottleneck is M9, especially $\mathcal M_2$.

Recommended allocation:

- **A1: 20%.** Finalize proof-draft text and state update. Keep the bridge conditional. Insert only proved algebra, conditional reductions, and bounded diagnostics.
- **A2: 35%.** Complete $\mathcal M_2$ fourth-moment taxonomy and CRI convention. If exploring an alternative, write exactly one transformed off-diagonal object, preferably a $\Delta$-method or shifted-convolution model for a near-collision family.
- **A3: 45%.** Produce reproducible computation: R5 residual tables, raw-vs-paired M9 regression, fixed-vs-stress coefficient tables, M2 Cauchy kernels, CRI ratios, fourth-moment bins, near-collision bands, and one H13 endpoint test.

Keep Mellin--Perron, signed Fourier truncation, Kuznetsov, Lindelof, and H13 secondary to the main route. Use them as comparison modules or falsification tests unless they supply a theorem-level reduction to M9.

## Next-round prompts by agent

### For A1

Produce the Round 26 proof-draft and state-update packet.

Objectives:

1. Insert H4-R25 into `best_proof_draft.md` with exact Vaaler source labels:
   - Theorem 6, printed p. 192, equation (2.28), for $\widehat J$;
   - Section 7, printed p. 207, equations (7.1)--(7.3), for $i_N,j_N,k_N$;
   - Theorem 18, printed p. 210, equations (7.13)--(7.17), especially (7.14), for the residual inequality.
2. Insert R5-Full-R25 as a complete lemma with all edge cases:
   - exact resonance $W_\Delta(0)=1$;
   - nearest-integer tie rule;
   - shifted products $X\approx d(4m-\rho)$;
   - congruence $\ell\equiv-\rho\pmod4$;
   - positivity of $\ell$ in the large active range;
   - small-$X$ separation;
   - short blocks $D<X^{1/4}$;
   - dyadic bounded overlap;
   - logarithmic losses absorbed by $X^\epsilon$.
3. State Bridge-R25 only conditionally:
$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$
4. Freeze M9-R25 with actual Vaaler coefficients and explicitly keep arbitrary-coefficient variants in a stress-test appendix only.
5. Insert M9-Pair-R25, Alpha-Conjugacy-R25, C-TwoSided-Convention-R25, and Phi-Asymmetry-R25 into the lemma bank.
6. Insert M2-CS-Normalizations-R25, M2-Q4-Expansion-R25, M2-Q4-Diagonal-Mass-R25, and CRI-Identity-R25 with correct statuses.
7. Update the gap register with M9, exact-resonance taxonomy, near-collision bands, denominator-paired singular cases, CRI sufficiency failure, Li--Yang PDF ambiguity, and A3 data gaps.
8. Reconcile the Li--Yang Case A/B range from the rendered PDF before making any theorem-range table final.
9. Add an A3 table template to the reading packet for R5, M9 regression, M2 kernels, CRI, Q4 bins, near-collisions, and H13.
10. Exploratory allocation: write a one-page checklist for any future $\Delta$-method or shifted-convolution alternative. The checklist should require an exact transformed object and an implication to M9 before promotion.

### For A2

Focus on $\mathcal M_2$ and do not add broad new routes unless one exact transformed object is supplied.

Objectives:

1. Fix exactly one convention for $S_2$: two-sided $1\le |h|\le H_D$ or one-sided paired real. State constants and conjugations.
2. Write the full fourth-moment expansion for
$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}C_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$
3. Use the cleared-denominator integer
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
4. Classify $N=0$ into diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, and unclassified families.
5. For each family, assign one status only:
`[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`.
6. Repair denominator-paired singular and truncation-edge cases. State the exact size of each family with actual $\alpha_h$ and $C_h$ weights.
7. Define near-collision bands $|N|\sim T$ and state the signed and absolute bounds needed over those bands to imply M9b.
8. Freeze the CRI convention and write the exact finite formula for $\Sigma_1,\Sigma_3,R_{\rm CRI}$.
9. Provide A3-ready pseudocode for exact-bin enumeration and near-collision banding.
10. Exploratory allocation: draft one structural alternative for a single off-diagonal family. Preferred option: a $\Delta$-method or shifted-convolution transform. Derive the additive characters and any Kloosterman/spectral object explicitly. Label it exploratory unless it gives a theorem-level implication to M9b.

### For A3

Run executable verification. Do not submit another protocol-only response.

Objectives:

1. Produce reproducible R5 residual tables for square, near-square, nonsquare, and divisor-rich $X$, including first leg and shifted legs $\rho=1,3$, normalized by $X^{1/4}$.
2. Use exact resonance detection:
$$
K_H(t)=H+1
$$
when $t\in\mathbb Z$, and high precision near integer $t$.
3. Run raw-vs-paired M9 regression for real $w_D$ at $D=X^{1/4},X^{3/8},X^{1/2}$; report raw values, paired values, absolute error, relative error, and normalized $|\mathcal M_i|/X^{1/4}$.
4. Compare fixed Vaaler coefficients with random phase coefficients, adversarial signs, and termwise $L^1$ stress norms.
5. Implement the M2 unweighted and weighted $h$-Cauchy kernels. Report diagonal mass, off-diagonal mass, operator norm, absolute majorant, and signed/unsigned comparisons.
6. Implement A2's fourth-moment exact-bin enumeration for feasible ranges. Report signed and absolute mass for each family.
7. Implement near-collision bands $|N|\sim T$ and report signed and absolute weighted masses per band.
8. Compute $R_{\rm CRI}$ for endpoint and intermediate $D$ scales. Values near $1$ should be reported as neutral, not promising.
9. Resolve the Li--Yang Case A/B ambiguity from the rendered PDF. Record exact theorem hypotheses for $F,g,G,H,M,T$, allowed weights, and absolute-value placement.
10. Run exactly one H13 endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes. Compare signed dual statistic, unsigned statistic, and diagonal-unitary operator-norm comparator.
11. Preserve raw scripts, precision settings, random seeds, and table outputs in commit-ready form.
12. Exploratory allocation: if A2 supplies a $\Delta$-method transformed object, implement a tiny finite sanity check of the transformed variables and coefficient weights. Do not present it as evidence for an asymptotic theorem.

## Confidence

High confidence:

- The balanced hyperbola/Vaaler route remains the correct current reduction framework.
- H1--H3 remain accepted arithmetic reductions.
- H4 is source-normalized in substance.
- R5-Full controls the fixed Fejer residual conditional on H4.
- Bridge-R25 is valid as a conditional reduction.
- M9 remains open.
- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- $\Phi(u)+\Phi(1-u)=1$.
- A2's fourth-moment expansion is a useful algebraic identity.
- A2's CRI identity is useful under a fixed convention.
- A3's checks are formula-regression evidence only, not asymptotic evidence.
- Li--Yang cannot be imported as a black-box endpoint theorem.

Moderate confidence:

- The paired implementation formulas are correct for real weights.
- The named diagonal and pair-swapped fourth-moment masses are compatible with the fourth-moment target.
- A3's local TeX audit of Li--Yang is useful, but the rendered PDF still needs reconciliation.
- A $\Delta$-method or shifted-convolution formulation may be useful for near-collision families if written as an exact transformed object.

Low confidence:

- CRI or fourth moments prove $\mathcal M_2$ without a new signed spacing theorem.
- H13 survives realistic norm extraction.
- Current Bombieri--Iwaniec/Li--Yang technology reaches the endpoint Vaaler height.
- Signed Fourier, Mellin--Perron, Kuznetsov, Lindelof, or structural alternatives bypass M9 without reintroducing the same endpoint reciprocal-sum difficulty.

Overall Round 25 judgment: productive and conservative. The proof infrastructure is now stable, residual control is no longer the active bottleneck, and the next round should execute finite-statistic verification while keeping M9 explicitly open.
