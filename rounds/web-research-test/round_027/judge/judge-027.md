## Selected main route

Source basis: the uploaded Round 27 judge packet and Stage A/B materials. External metadata remains stable: Vaaler's source is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc. (N.S.)* 12(2):183--216, April 1985. Li--Yang is Xiaochun Li and Xuerui Yang, "An Improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem," arXiv:2308.14859v2, whose abstract states the Bombieri--Iwaniec / first-spacing / Huxley second-spacing mechanism.

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

The conservative Round 27 bridge remains:

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

This is a conditional reduction only. Round 27 proves no new Gauss circle exponent. The active analytic bottleneck is still M9, especially $\mathcal M_2$.

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

Blocks with $D<X^{1/4}$ are removed before Vaaler expansion and bounded trivially.

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
C_h
\sum_{d\asymp D}
w_D(d)e(hX/(4d)),
$$

where

$$
C_h=e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

The required endpoint-strength estimate is

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over active dyadic $D$.

Round 27 should be recorded as a proof-infrastructure and finite-statistic round. Its main useful output is not a new estimate; it is the stabilization of the proof draft and a sharper set of finite-statistic objects for $\mathcal M_2$.

## Useful fragments by source

### From A1

A1's strongest contribution is the conservative proof-draft state:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

with M9 explicitly open.

A1 correctly keeps H4 as an external theorem dependency, source-normalized in substance but still requiring final rendered-page transcription. The repo form is:

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
\frac{\sin\pi(H+1)t}{\sin\pi t}
\right)^2.
$$

The endpoint convention is correct and must remain in the proof draft:

$$
V_H(n)=0,
\qquad
\psi_F(n)=-\frac12,
\qquad
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

A1 also gives the current final form of R5-Full. For active $D$ and $H\asymp D X^{-1/4}$, set

$$
\Delta=\frac{D}{H}\asymp X^{1/4}.
$$

The Fejer bound

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right)
$$

gives

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first leg, choosing $m$ nearest to $X/d$ yields

$$
\left\|\frac Xd\right\|
\asymp
\frac{|X-md|}{D},
\qquad d\asymp D.
$$

Thus

$$
\frac1H K_H(X/d)
\ll
W_\Delta(X-md),
$$

where

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min(1,\Delta^2/u^2),&u\ne0.
\end{cases}
$$

Grouping by $n=md$ gives divisor multiplicity at most $\tau(n)$, hence

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon
X^\epsilon
\sum_{n\asymp X}W_\Delta(X-n)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the shifted second legs, near-integrality of

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
\ell=4m-\rho,
\qquad
\ell\equiv-\rho\pmod4,
$$

again gives a divisor-product count. The congruence condition only reduces multiplicity.

A1's B-process/Hardy-collapse audit is also valuable. For the inner $\mathcal M_2$ sum, Poisson/stationary phase gives a square-root phase. For $h>0$,

$$
I_{h,n}
=
\int w_D(u)e\left(\frac{hX}{4u}-nu\right)\,du.
$$

The active stationary sign is $n=-m<0$, with

$$
u_0=\frac12\sqrt{\frac{hX}{m}},
\qquad
m\asymp \frac{hX}{D^2},
$$

and leading phase

$$
\sqrt{hXm}.
$$

Substituting $q=hm$ gives a Hardy-like phase $e(\sqrt{Xq})$, but the coefficient is not a standard Hardy/Voronoi coefficient. It is a local divisor-window coefficient:

$$
X^{1/4}q^{-3/4}
\sum_{\substack{h\mid q\\h\asymp D\sqrt{q/X}}}
h\beta_h
w_D\left(\frac12\sqrt{\frac{h^2X}{q}}\right),
\qquad
\beta_h=\alpha_{h,H_D}C_h.
$$

This is a useful negative audit: the B-process gives a square-root phase, but not a controlled one-dimensional Hardy-series reduction.

### From A2

A2's strongest Round 27 contribution is the finite-statistic packet for $\mathcal M_2$.

The correct convention is the two-sided convention

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
\beta_h=\alpha_{h,H_D}C_h,
$$

so that

$$
\mathcal M_2(D;X)=4S_2(D;X).
$$

A2's fourth-moment expansion is a useful algebraic identity:

$$
|S_2(D;X)|^4
=
\sum_{\mathbf h,\mathbf d}
\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
\prod_{j=1}^4w_D(d_j)
e\left(
\frac X4
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

The sufficient fourth-moment target is

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon},
$$

but this is not proved.

A2's CRI identity is also useful under the fixed convention. If

$$
\Sigma_r(D;X)
=
\sum_{\substack{1\le |h|\le H_D\\h\equiv r\pmod4}}
\alpha_{h,H_D}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad r\in\{1,3\},
$$

then

$$
S_2(D;X)=2i(\Sigma_1-\Sigma_3)
$$

under the appropriate two-sided convention. The ratio

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}
$$

is a falsification metric, not an endpoint estimate.

A2's exact-resonance taxonomy is useful but incomplete. Diagonal and pair-swapped families appear compatible with the fourth-moment target. Semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified $N=0$ families still need line-by-line analysis. Denominator-paired singular cases and near-collision bands remain open.

A2's $\Delta$-method suggestion is useful only if made exact. A future promotion requires a delta-symbol identity, modulus range, smooth weights, transformed complete sums, coefficient preservation for $\beta_h$, and a theorem-level implication to M9.

### From A3

A3's value is verification discipline and executable-spec design. A3 supplies useful formulas for:

- R5 residual tables;
- raw two-sided versus paired real M9 regression;
- complex-weight failure tests;
- fixed-coefficient versus random/adversarial/L1 stress comparisons;
- weighted and unweighted $\mathcal M_2$ Cauchy kernels;
- CRI ratios;
- fourth-moment exact bins;
- near-collision banding;
- denominator-paired singular checks;
- Li--Yang rendered-PDF audit;
- B-process/Hardy-collapse local-divisor-window tests.

A3 correctly treats formula regression as formula regression only. No numerical table supplied by A3 should be interpreted as asymptotic evidence unless it is accompanied by scale variation, exact coefficient handling, and high-precision resonance safety.

A3's raw-vs-paired warning should be promoted. For real $w_D$,

$$
A_{-h}=\overline{A_h},
\qquad
B_{-h}=\overline{B_h},
\qquad
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

Thus paired real formulas are valid implementation identities only under real weights. For complex $w_D$, the paired formulas generally fail and the raw two-sided definitions must be used.

A3's Li--Yang source audit remains a guardrail, not an endpoint theorem. Li--Yang's theorem is structurally relevant but does not supply the conjectural endpoint height $H_D\asymp D X^{-1/4}$. The rendered-PDF audit of Case A/B ranges and absolute-value placement is still pending.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** Round 27 does not prove M9.

2. **Reject treating the bridge as unconditional.** The correct statement is only

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

3. **Reject treating arbitrary-coefficient M9 as the active target.** The actual Vaaler reduction creates fixed coefficients $\alpha_{h,H_D}$ and $C_h$, not arbitrary bounded coefficients.

4. **Reject reopening H5r-B or H5r-L1 as proof dependencies.** H4 plus R5-Full controls the fixed Fejer residual directly. Stronger residual norms remain stress tests only.

5. **Reject paired real formulas outside their hypotheses.** They require real $w_D$. Complex weights must use raw two-sided definitions.

6. **Reject $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$.** The correct relation is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

7. **Reject $\Phi(1-u)=\Phi(u)$.** The correct identity is

$$
\Phi(u)+\Phi(1-u)=1.
$$

8. **Reject unweighted $h$-Cauchy for $\mathcal M_2$ as endpoint-viable.** Its diagonal is too large at $D\asymp X^{1/2}$.

9. **Reject weighted $h$-Cauchy as character-preserving.** The diagonal is better, but $C_h\overline{C_h}=|C_h|^2$ loses the $\chi_4(h)$ sign.

10. **Reject CRI as a sufficient target without a theorem.** The identity $S_2=2i(\Sigma_1-\Sigma_3)$ is algebraic; it does not bound $S_2$.

11. **Reject the fourth-moment route as proved.** A2's expansion is correct, but the $N=0$ taxonomy and near-collision bounds are incomplete.

12. **Reject denominator-paired estimates as proved.** The parametrization is plausible but still requires sign, zero-frequency, truncation-boundary, and singular-case repairs.

13. **Reject a $\Delta$-method sketch without an exact transformed object.** It must include the delta symbol, modulus range, smooth weights, complete sums, coefficient weights, and target implication.

14. **Reject a direct Hardy-collapse claim.** B-process produces a square-root phase, but the coefficient is a local divisor-window coefficient, not a standard Hardy coefficient.

15. **Reject black-box Li--Yang endpoint import.** Li--Yang reaches $\theta^*=0.314483\ldots$, not $\theta=1/4$, and its theorem hypotheses have not been matched to endpoint M9.

16. **Reject making H13, Mellin--Perron, signed Fourier, Kuznetsov, or Lindelof primary.** These remain comparison or falsification modules unless they produce a theorem-level reduction to M9.

## Known gaps

1. **M9 remains open.** No Round 27 output proves

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

2. **H4 final rendered-page transcription.** The Vaaler formula is source-normalized in substance, but the proof draft still needs final rendered page/equation verification.

3. **R5-Full proof-draft insertion.** The proof is stable, but the final draft must retain all edge cases: nearest-integer ties, exact resonance $W_\Delta(0)=1$, shifted products, positivity of $\ell=4m-\rho$, small-$X$ separation, short blocks, bounded dyadic overlap, and logarithmic losses.

4. **Two-sided M9 convention must be frozen.** A2 and A3 should use the raw two-sided convention for algebra. Paired formulas are implementation-only.

5. **$\mathcal M_2$ fourth-moment taxonomy incomplete.** The exact $N=0$ taxonomy still has unclassified residue and overlap issues.

6. **Denominator-paired singular cases incomplete.** Cases near $h_2+ac=0$, $h_3+bc=0$, small $|\Delta|$, and truncation boundaries need repair.

7. **Near-collision estimates missing.** The critical bands $0<|N|\sim T$ require signed and absolute weighted-mass bounds with actual $\beta_h$ coefficients.

8. **CRI sufficiency gap.** CRI is a falsification statistic unless a theorem shows that a bound for $R_{\rm CRI}$ or a related cross-residue quantity implies M9.

9. **Delta-method theorem gap.** No exact delta-symbol theorem or transformed off-diagonal object has been written for the fourth-moment near-collision problem.

10. **Hardy-collapse theorem gap.** A B-process/Hardy audit gives a structural square-root phase, but no uniform stationary-phase theorem, no controlled truncation, and no estimate for the local divisor-window coefficients.

11. **Li--Yang rendered-PDF audit gap.** TeX-source and local audits are useful, but exact theorem ranges, weights, and absolute-value placement still need PDF reconciliation before theorem-level use.

12. **A3 execution gap.** Round 27 still does not provide the desired committed tables. The next round must produce reproducible scripts or actual output.

13. **Numerical resonance safety gap.** Fejer and M9 computations must use high precision or exact rational handling near integer and shifted-integer resonances.

14. **Theorem-dependency gap for any new analytic route.** Any route using $\Delta$-methods, Kuznetsov, Lindelof, Hardy/Voronoi, or signed spacing must state an exact theorem with hypotheses and an implication to M9.

## New lemmas to add

### H4-R27. Finite Vaaler approximation with floor-compatible residual

**Status:** external theorem dependency; source-normalized in substance, final rendered-page transcription pending.

For $H\ge1$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
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

At integers,

$$
V_H(n)=0,
\qquad
\psi_F(n)=-\frac12,
\qquad
K_H(0)/(2H+2)=1/2.
$$

### R5-Full-R27. Fejer residual product-count bound

**Status:** proved conditional on H4.

For active $D$ and $H_D\asymp D X^{-1/4}$, all first and shifted Fejer residual blocks are

$$
O_\epsilon(X^{1/4+\epsilon}).
$$

The proof uses $W_\Delta(0)=1$, grouping by $n=md$ and $n=d(4m-\rho)$, divisor multiplicity, and short-block separation.

### Bridge-R27. Conditional endpoint reduction

**Status:** conditional theorem.

If H1--H3, H4-R27, R5-Full-R27, and M9-R27 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

M9 is open.

### M9-R27. Fixed-coefficient main-term target

**Status:** official open analytic target.

For every active dyadic $D$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon},
$$

with the actual Vaaler coefficients $\alpha_{h,H_D}$ and the actual $C_h$.

### M2-TwoSided-R27

**Status:** convention lemma.

Use

$$
S_2(D;X)
=
\sum_{1\le |h|\le H_D}
\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
\beta_h=\alpha_{h,H_D}C_h,
$$

and

$$
\mathcal M_2(D;X)=4S_2(D;X).
$$

This is the default algebraic convention.

### M9-Pair-R27

**Status:** implementation lemma for real weights only.

For real $w_D$, paired positive-frequency formulas are valid. For complex $w_D$, use raw two-sided definitions. Raw-vs-paired regression should be mandatory in code.

### Alpha-Conjugacy-R27

**Status:** proved algebraic lemma.

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### Phi-Asymmetry-R27

**Status:** proved algebraic lemma.

$$
\Phi(u)+\Phi(1-u)=1.
$$

Thus $\Phi(1-u)=\Phi(u)$ is false except at $u=1/2$.

### C-TwoSided-R27

**Status:** proved algebraic lemma.

$$
C_h=e(h/4)-e(3h/4)
=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

### M2-Q4-Expansion-R27

**Status:** proved algebraic identity; analytic estimate open.

For $S_2$ as above,

$$
|S_2(D;X)|^4
=
\sum_{\mathbf h,\mathbf d}
\beta_{h_1}\overline{\beta_{h_2}}
\beta_{h_3}\overline{\beta_{h_4}}
\prod_{j=1}^4w_D(d_j)
e\left(
\frac X4
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right)
\right).
$$

The resonance integer is

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

is unproved.

### M2-Q4-Taxonomy-R27

**Status:** partially classified; not an estimate.

Diagonal and pair-swapped families appear compatible with the target. Semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified $N=0$ configurations require proof-draft verification.

### M2-DenominatorPaired-R27

**Status:** derived under assumptions; incomplete.

The denominator-paired parametrization needs singular-case repair, zero-frequency handling, sign handling, truncation-boundary analysis, and actual $\beta_h$ weights.

### CRI-Identity-R27

**Status:** proved algebraic identity under fixed convention; diagnostic only.

Under the two-sided convention,

$$
S_2(D;X)=2i(\Sigma_1-\Sigma_3).
$$

The ratio $R_{\rm CRI}$ is a falsification metric unless paired with a theorem converting it into an M9 bound.

### M2-CS-Normalizations-R27

**Status:** bounded-scope diagnostic.

Unweighted $h$-Cauchy has too large an endpoint diagonal. Weighted $|\alpha|$ Cauchy has acceptable diagonal size but loses the $\chi_4(h)$ sign by replacing $C_h$ with $|C_h|^2$.

### DeltaMethod-OffDiagonal-R27

**Status:** exploratory only.

Promotion requires an exact delta-symbol formula, modulus range, transformed off-diagonal object, coefficient preservation, and implication to M9.

### HardyCollapse-Audit-R27

**Status:** exploratory negative audit.

B-process on $\mathcal M_2$ gives a square-root phase, but $q=hm$ yields local divisor-window coefficients, not a standard Hardy coefficient. No endpoint estimate follows.

### A3-VerificationHarness-R27

**Status:** computational specification, not evidence.

The R5, M9 regression, fixed-vs-stress, CRI, Q4-bin, near-collision, denominator-paired, Li--Yang, and Hardy-window tests should be implemented with high precision and committed output.

## Counterexample checks to run

1. **H4 source check.** Verify Vaaler's rendered PDF page/equation labels for Theorem 6, Section 7 definitions, and Theorem 18 residual inequality.

2. **H4 integer-jump check.** Verify

$$
V_H(n)=0,
\qquad
K_H(0)=H+1,
\qquad
K_H(0)/(2H+2)=1/2.
$$

3. **R5 exact-resonance tests.** Test square, near-square, nonsquare, and divisor-rich $X$ for first and shifted residual legs.

4. **High-precision Fejer spike safety.** Use exact rational or modular detection near integer arguments. Do not rely on ordinary floating sine quotients near $\sin\pi t=0$.

5. **Raw-vs-paired M9 regression.** For real $w_D$, compare raw two-sided complex $\mathcal M_1,\mathcal M_2$ with paired real formulas. Report real part, imaginary part, absolute error, relative error, and normalized magnitude.

6. **Complex-weight failure check.** Deliberately test non-real $w_D$ and verify that paired real formulas fail outside their hypothesis.

7. **Fixed-coefficient stress comparison.** Compare actual Vaaler coefficients with random phases of the same magnitudes, adversarial signs, and termwise $L^1$ norms.

8. **$\mathcal M_2$ Cauchy kernel diagnostics.** For weighted and unweighted $h$-Cauchy, report diagonal mass, off-diagonal signed mass, off-diagonal absolute mass, operator norm, and signed/unsigned ratios.

9. **Fourth-moment exact bins.** Enumerate $N=0$ and split into diagonal, pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, truncation-edge, and unclassified bins.

10. **Near-collision banding.** For $0<|N|\sim T$, report signed mass, absolute mass, and coefficient-weighted mass with actual $\beta_h$.

11. **Denominator-paired singular checks.** Isolate cases near $h_2+ac=0$, $h_3+bc=0$, small $|\Delta|$, truncation edges, and zero or near-zero frequency patterns.

12. **CRI endpoint tests.** Compute $R_{\rm CRI}$ at endpoint and intermediate $D$. Values near $1$ should deprioritize CRI.

13. **Li--Yang rendered-PDF audit.** Resolve Case A/B ambiguity from the typeset PDF and record exact hypotheses for $F,g,G,H,M,T$, allowed weights, ranges, and absolute-value placement.

14. **Delta-method normalization.** Before accepting any $\Delta$-method sketch, write the exact delta-symbol theorem, modulus range, smooth weights, error term, and complete-sum structure.

15. **Hardy-window coefficient test.** After B-process, compute the local divisor-window coefficient $a_D(q)$ and compare signed and absolute masses.

16. **H13 endpoint falsification.** Run at most one endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes, comparing signed dual statistic, unsigned statistic, and diagonal-unitary operator-norm comparator.

17. **A3 reproducibility check.** Require scripts or tables, not only pseudocode. Record input choices, precision, dyadic weights, and coefficient conventions.

## Research strategy adjustment

Round 28 should be an execution-and-taxonomy round.

The main route stays unchanged. The residual side should remain proof infrastructure controlled by H4 plus R5-Full. The active bottleneck is M9, especially $\mathcal M_2$.

Recommended allocation:

- **A1:** conservative synthesis and proof-draft maintenance. Promote only proved algebraic identities, conditional reductions, and bounded diagnostics. Keep the bridge conditional.
- **A2:** finish the $\mathcal M_2$ fourth-moment taxonomy and formulate exact theorem-level near-collision targets. Provide one exact $\Delta$-method or shifted-convolution transformed object if using that route.
- **A3:** execute. Produce high-precision tables or reproducible scripts for R5, raw-vs-paired M9, fixed-vs-stress coefficients, Cauchy kernels, CRI ratios, fourth-moment bins, near-collision bands, denominator-paired singular checks, and Li--Yang PDF audit.

Do not pivot to Mellin--Perron, signed Fourier, Kuznetsov, Lindelof, H13, or Hardy-collapse as the main route. Keep them as comparison or falsification modules unless they supply a theorem-level implication to M9.

## Next-round prompts by agent

### For A1

Produce the Round 28 proof-draft and state-update packet.

Objectives:

1. **Finalize H4/R5/Bridge status.**
   State H4-R27, R5-Full-R27, Bridge-R27, and M9-R27 with exact statuses:
   - H4: external theorem dependency, source-normalized in substance, final rendered-page transcription pending;
   - R5-Full: proved conditional on H4;
   - Bridge: conditional theorem;
   - M9: open.

2. **Update the best proof draft.**
   Insert the floor-compatible Vaaler statement, the integer-jump convention, the product-count residual proof, and the conditional bridge. Keep arbitrary-coefficient variants in a stress-test appendix only.

3. **Freeze the M9 conventions.**
   Use the raw two-sided convention for $\mathcal M_1$ and $\mathcal M_2$. Include paired real implementation formulas only as a separate lemma for real weights.

4. **Add the algebraic lemmas.**
   Insert Alpha-Conjugacy-R27, Phi-Asymmetry-R27, C-TwoSided-R27, M9-Pair-R27, and M2-TwoSided-R27 with proof sketches and implementation warnings.

5. **Record A2's finite-statistic objects.**
   Add M2-Q4-Expansion-R27, the resonance integer $N$, CRI-Identity-R27, M2-CS-Normalizations-R27, and the current taxonomy status. Mark all analytic estimates open unless proved.

6. **Add the Hardy-collapse audit.**
   State clearly that B-process gives a square-root phase but local divisor-window coefficients, not a standard Hardy coefficient. Keep it exploratory.

7. **Write the Round 28 reading packet.**
   Make it validation-forward. The main next deliverables are A2's completed taxonomy and A3's executed tables.

8. **Literature/source audit.**
   Preserve Vaaler as the H4 source and Li--Yang as a guardrail only. Do not claim endpoint theorem applicability without a rendered-PDF theorem audit.

Exploratory allocation: write a concise checklist for what an exact $\Delta$-method transformed off-diagonal object would need to contain before it can be considered a serious M9 route.

### For A2

Complete the $\mathcal M_2$ finite-statistic and near-collision packet. Avoid route-closing language.

Objectives:

1. **Use the two-sided convention.**
   Work with

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}\beta_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad
\beta_h=\alpha_{h,H_D}C_h.
$$

2. **Rewrite the fourth moment with exact constants.**
   State the full expansion of $|S_2|^4$ and the cleared denominator integer

$$
N=
h_1d_2d_3d_4
-
h_2d_1d_3d_4
+
h_3d_1d_2d_4
-
h_4d_1d_2d_3.
$$

3. **Finish the $N=0$ taxonomy.**
   Classify:
   - exact diagonal;
   - pair-swapped;
   - semi-diagonal;
   - denominator-paired;
   - mixed denominator patterns;
   - sign-symmetric variants;
   - truncation-edge cases;
   - unclassified residue.

For every family, assign one of:
`[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, `[LIKELY-FALSE]`.

4. **Repair denominator-paired singular cases.**
   Explicitly handle signs of $h_i$, zero-frequency exclusions, truncation boundaries $|h_i|\le H_D$, small or zero shifted parameters, and dyadic restrictions on $d_i$.

5. **Define near-collision bands.**
   For $0<|N|\sim T$, state the exact signed or absolute coefficient-weighted bound needed to imply

$$
\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

6. **Evaluate the near-collision heuristic.**
   State exactly what the $X^{5/4}$ or $X^{9/4}$ warnings assume, what they ignore, and what A3 should measure.

7. **Formalize CRI.**
   Either prove a theorem-level sufficient condition involving CRI or label it only as a falsification statistic. Include the exact identity linking $S_2$ to $\Sigma_1-\Sigma_3$.

8. **Supply A3-ready formulas.**
   Provide formulas for:
   - weighted and unweighted M2 Cauchy kernels;
   - CRI ratio;
   - fourth-moment exact bins;
   - near-collision banding;
   - denominator-paired singular checks.

9. **Optional exploratory allocation.**
   Give exactly one $\Delta$-method or shifted-convolution transformed object. It must include delta symbol, modulus range, smooth weights, transformed exponential sums, coefficient weights $\beta_h$, and a target implication to M9. If this cannot be done exactly, keep it as a checklist.

10. **Hardy-collapse comparison.**
   Compare the existing eight-variable $\mathcal Q_4$ object with the B-process/local-divisor-window object. Do not assert equivalence unless constants, truncations, and errors are controlled.

### For A3

Execute computations and source checks. Do not produce another protocol-only response.

Objectives:

1. **R5 residual tables.**
   Provide high-precision tables for $X=10^6$ and $X=10^8$, plus at least one square, one near-square, one nonsquare, and one divisor-rich $X$. Include $D=X^{1/4},X^{3/8},X^{1/2}$ when feasible. Normalize by $X^{1/4}$.

2. **Raw-vs-paired M9 regression.**
   For the same samples, compute raw two-sided complex $\mathcal M_1,\mathcal M_2$ and paired real formulas using real dyadic weights. Report:
   - raw complex value;
   - paired real value;
   - real and imaginary parts;
   - absolute error;
   - relative error;
   - normalized $|\mathcal M_i|/X^{1/4}$.

3. **Complex-weight failure test.**
   Test non-real dyadic weights and confirm that paired real formulas do not apply unchanged.

4. **Fixed-coefficient stress comparison.**
   Compare actual $\alpha_{h,H_D}$ coefficients with random phases of the same magnitudes, adversarial signs, and termwise $L^1$ norms.

5. **M2 Cauchy kernel diagnostics.**
   For weighted and unweighted $h$-Cauchy, report diagonal mass, off-diagonal signed mass, off-diagonal absolute mass, operator norm, and signed/unsigned ratios.

6. **Fourth-moment bins.**
   Enumerate exact $N=0$ configurations and split them into A2's bins. Report signed and absolute coefficient-weighted mass.

7. **Near-collision bands.**
   For $0<|N|\sim T$, report signed mass, absolute mass, and coefficient-weighted mass. Compare to A2's heuristic only as a diagnostic.

8. **Denominator-paired singular checks.**
   Isolate the singular and truncation-edge cases identified by A2.

9. **CRI endpoint tests.**
   Compute $R_{\rm CRI}$ at endpoint and intermediate $D$ scales. Values near $1$ should deprioritize CRI.

10. **Li--Yang rendered-PDF audit.**
   Resolve the Case A/B discrepancy from the typeset PDF and record exact hypotheses for $F,g,G,H,M,T$, weights, ranges, and absolute-value placement.

11. **High-precision Fejer safety.**
   Use exact rational or modular detection near integer arguments. Do not use ordinary float-only sine quotients near $\sin\pi t=0$.

12. **B-process/Hardy-window test.**
   Compute the local divisor-window coefficient from the B-process model and compare signed and absolute masses. Treat this as structural verification only.

13. **Reproducibility requirement.**
   Provide scripts or tables with input parameters, precision settings, dyadic weights, and exact coefficient conventions. Every table should be reproducible.

Exploratory allocation: run one endpoint H13/B-process test near $D\asymp X^{1/2}$ only if the main R5/M9/Q4 tables are complete.

## Confidence

High confidence:

- The balanced hyperbola/Vaaler route remains the correct current reduction framework.
- H1--H3 remain accepted arithmetic reductions.
- H4 is source-normalized in substance.
- R5-Full controls the fixed Fejer residual conditional on H4.
- The bridge remains valid only as a conditional reduction.
- M9 remains open.
- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- $\Phi(u)+\Phi(1-u)=1$.
- A2's fourth-moment expansion and resonance integer are correct algebraic objects.
- A2's CRI identity is useful under a fixed convention.
- A3's planned checks are formula-regression and falsification tools, not asymptotic evidence.
- Li--Yang cannot be imported as a black-box endpoint theorem.

Moderate confidence:

- The paired implementation formulas are correct for real weights.
- Diagonal and pair-swapped fourth-moment families are compatible with the fourth-moment target.
- The B-process/Hardy audit correctly identifies a local divisor-window coefficient.
- A $\Delta$-method or shifted-convolution formulation may be useful if written as an exact transformed object.

Low confidence:

- CRI or fourth moments prove $\mathcal M_2$ without a new signed spacing theorem.
- H13 survives realistic norm extraction.
- Current Bombieri--Iwaniec/Li--Yang technology reaches the endpoint Vaaler height.
- Signed Fourier, Mellin--Perron, Kuznetsov, Lindelof, or structural alternatives bypass M9 without reintroducing the same endpoint reciprocal-sum difficulty.

Overall Round 27 judgment: productive and conservative. The proof infrastructure is stable, residual control is no longer the active bottleneck, and the next round should execute finite-statistic verification while keeping M9 explicitly open.
