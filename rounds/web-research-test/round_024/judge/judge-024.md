## Summary

Round 24 is a productive precision round, not an exponent-improvement round. It does **not** prove a new Gauss circle exponent, and it does not prove M9. The conservative bridge remains

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

where $P(X)=N(\sqrt X)-\pi X$. The uploaded Round 24 packet explicitly records that neither A2 nor A3 proves M9 and that the route remains conditional.

The residual side of the Vaaler route remains provisionally controlled by H4 plus R5-Full. The active bottleneck is still M9: the fixed-Vaaler-coefficient main sums $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$. Round 24's most useful new content is the finite-statistic framework for $\mathcal M_2$: a two-sided fourth-moment object $\mathcal Q_4$, a cleared-denominator resonance integer $N$, and a CRI falsification statistic. These are algebraic and diagnostic tools, not estimates.

External anchors remain stable: Vaaler's paper is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc.* 12(2), 183--216, 1985. Li--Yang's arXiv paper states a Bombieri--Iwaniec / first-spacing / Huxley-second-spacing improvement for the Gauss circle and divisor problems, but it does not supply the endpoint theorem needed for M9.

## Selected main route

Keep the balanced arithmetic hyperbola/Vaaler framework:

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

For active dyadic denominator blocks,

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ are removed before Vaaler expansion and bounded directly by $|\psi_F|\le 1/2$.

Freeze M9 with the actual Vaaler coefficients

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

The official main terms are

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

for odd $h$ and vanishes for even $h$, the second sum may also be written as

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

The open target remains

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for $X^{1/4}\le D\le X^{1/2}$. The Round 24 packet states this explicitly as the active open problem.

## Useful fragments by source

### From A1

A1 provides the strongest proof-draft consolidation. The useful pieces are:

1. **H4-R24 source normalization.** The Vaaler approximation is recorded in repo notation as

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

with

$$
|R_H^F(t)|\le\frac1{2H+2}K_H(t),
$$

and

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

The source anchors in the packet are Vaaler Theorem 6, equation (2.28), Section 7 equations (7.1)--(7.3), and Theorem 18, especially equation (7.14). The final proof draft should still check the rendered page/equation labels.

2. **Endpoint convention.** At integers,

$$
V_H(n)=0,
\qquad
\psi_F(n)=-\frac12,
\qquad
\frac{K_H(0)}{2H+2}=\frac12,
$$

so the Fejer majorant covers the floor-compatible half-jump exactly.

3. **R5-Full-R24.** With

$$
H\asymp D X^{-1/4},
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

A1 uses

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right)
$$

and the exact-resonance-safe cap

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min(1,\Delta^2/u^2),&u\ne0.
\end{cases}
$$

For the first residual leg,

$$
\frac1H K_H(X/d)\ll W_\Delta(X-md),
$$

where $m$ is nearest to $X/d$. Grouping $n=md$ gives divisor multiplicity at most $\tau(n)$, hence

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)W_\Delta(X-n)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For shifted residual legs, near-integrality of $(X/d+\rho)/4$ is equivalent to $X\approx d(4m-\rho)$, so writing $\ell=4m-\rho$ gives the same product-counting bound with a congruence restriction. The packet records this as the current residual mechanism.

4. **Conditional bridge.** A1's Bridge-R24 is exactly the right proof skeleton: H1--H3, H4, R5-Full, and M9 imply the conjectural-scale bound, but M9 is open, so no theorem is proved.

5. **Implementation formulas.** For real $w_D$, A1 and A3 record the paired formulas

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{h=1}^{H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}
\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_d w_D(d)e(hX/(4d)).
$$

These are implementation formulas only; they require real dyadic weights and raw-vs-paired numerical regression.

### From A2

A2 provides the main new analytic object for Round 24: a finite-statistic framework for $\mathcal M_2$.

Let

$$
C_h=e(h/4)-e(3h/4),
\qquad
\beta_h=\alpha_{h,H_D}C_h,
$$

and define

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

up to the scalar $4^4=256$.

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

The character signs are retained through

$$
C_{h_1}\overline{C_{h_2}}C_{h_3}\overline{C_{h_4}},
$$

rather than being lost as $|C_h|^2$ at the second-moment stage. Clearing denominators gives the exact resonance integer

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

The packet correctly treats this as a proposed exploratory/falsification target. The missing proof is a complete taxonomy and estimate of exact $N=0$ configurations, near-collision bands, denominator-paired singular cases, truncation-boundary cases, and signed versus absolute mass.

A2 also formalizes the CRI statistic. Under a one-sided paired real convention, define

$$
\Sigma_r^R(D;X)
=
\sum_{\substack{1\le h\le H_D\\h\equiv r\pmod4}}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Re}
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
\qquad r\in\{1,3\}.
$$

Then

$$
\mathcal M_2(D;X)
=
-\frac8\pi\left(\Sigma_1^R(D;X)-\Sigma_3^R(D;X)\right),
$$

so the relevant falsification ratio is

$$
R_{\rm CRI}
=
\frac{|\Sigma_1^R-\Sigma_3^R|^2}
{|\Sigma_1^R|^2+|\Sigma_3^R|^2}.
$$

This ratio satisfies $0\le R_{\rm CRI}\le2$ when the denominator is nonzero. Values near $0$ indicate strong cancellation in $\Sigma_1^R-\Sigma_3^R$; values near $1$ are neutral; values near $2$ are bad for cancellation. CRI is not a theorem-level sufficient target.

A2's near-collision warning is useful but should remain heuristic. The suggested top-block absolute weighted mass $X^{5/4}$ depends on uniformity of the cleared-denominator map, typical-frequency weighting, and absence of arithmetic clustering. It is a warning against absolute majorization, not a lower bound.

### From A3

A3's useful contribution is formula auditing and verification discipline, but it still under-executes numerically.

A3 verifies or independently checks:

- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$;
- $C_{-h}=\overline{C_h}$;
- $\Phi(1-u)=\Phi(u)$ is false;
- the paired real formulas for real weights;
- R5 exact-resonance handling via $W_\Delta(0)=1$;
- weighted $h$-Cauchy sign loss for $\mathcal M_2$;
- $d$-Cauchy diagonal scaling;
- the final-exponent Li--Yang endpoint mismatch.

A3's main weakness is that the output remains protocol-level. The Round 24 materials explicitly state that A3 needs reproducible data: R5 residual tables, raw-vs-paired regressions, CRI ratios, and fourth-moment bin tables.

### From Stage B reviews

The Stage B reviews converge on the following:

- A1's proof-draft consolidation is accurate and should be merged into the best proof draft.
- A2 is the strongest new analytic contributor because the $\mathcal M_2$ fourth-moment and CRI framework gives concrete finite objects.
- A3 is useful for audit discipline but should produce tables, not more protocols.
- The next round should remain narrow and verification-forward.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** M9 is open; no Round 24 output proves

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

2. **Reject treating the bridge as a proof.** The implication

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

is conditional.

3. **Reject arbitrary-coefficient main-sum stress tests as active dependencies.** The Vaaler reduction uses the fixed coefficients $\alpha_{h,H_D}$.

4. **Reject scalar Vaaler residuals.** The residual is handled by H4 plus R5-Full product counting. Dropping Fejer modes is still a false-proof pattern.

5. **Reject $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$.** The correct relation is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

6. **Reject $\Phi(1-u)=\Phi(u)$.** The correct identity is

$$
\Phi(u)+\Phi(1-u)=1,
$$

so equality under $u\mapsto1-u$ holds only at $u=1/2$.

7. **Reject unweighted $h$-Cauchy for $\mathcal M_2$ as viable at the endpoint.** Its diagonal contribution gives $D H_D\asymp D^2X^{-1/4}$, which equals $X^{3/4}$ at $D\asymp X^{1/2}$, above the squared endpoint target $X^{1/2+\epsilon}$.

8. **Reject weighted $h$-Cauchy for $\mathcal M_2$ as character-preserving.** Its diagonal is acceptable, but it replaces $C_h$ by $|C_h|^2$, losing the $\chi_4(h)$ sign and retaining only odd-frequency support.

9. **Reject CRI as sufficient by itself.** The whole expression

$$
|\Sigma_1-\Sigma_3|^2
=
|\Sigma_1|^2+|\Sigma_3|^2
-
2\operatorname{Re}(\Sigma_1\overline{\Sigma_3})
$$

needs to be controlled. A small cross term alone is not enough.

10. **Reject the fourth-moment route as proved.** A2's object is useful, but exact-resonance taxonomy, denominator-paired singular cases, signed-frequency conventions, and near-collision estimates remain incomplete.

11. **Reject the $X^{5/4}$ weighted near-collision warning as a theorem.** It is a heuristic model to be tested numerically and sharpened analytically.

12. **Reject pointwise Lindelof, Kuznetsov, Mellin--Perron, signed Fourier, or H13 as main pivots.** They remain comparison or falsification modules unless they produce an exact theorem-level reduction to M9.

13. **Reject black-box Li--Yang endpoint import.** Li--Yang is structurally relevant, but the final exponent gap and unresolved Case A/B transcription prevent using it as an endpoint theorem.

## Known gaps

1. **M9 remains open.** Neither $\mathcal M_1$ nor $\mathcal M_2$ has an endpoint-strength estimate.

2. **H4 still needs final rendered-page transcription.** The theorem anchors are stable, but the proof draft should verify exact page/equation labels against the rendered Vaaler PDF.

3. **Li--Yang Case A/B ambiguity remains.** The detailed theorem-range comparison should use the typeset PDF, not just TeX fragments.

4. **Fourth-moment exact-resonance taxonomy is incomplete.** A2 lists displayed families, but not every denominator pattern, sign-symmetric variant, mixed pattern, or unclassified residue is controlled.

5. **Near-collision bands are unproved.** The key bands $|N|\sim T$ require signed and absolute mass estimates with coefficient weights, gcd structure, parity, and dyadic cutoffs.

6. **Denominator-paired singular cases are unresolved.** Cases such as $h_1=ac$, $h_3=-bc$, or values near truncation boundaries may amplify coefficient weights and should be separated.

7. **CRI convention should be frozen before computation.** One-sided paired real and two-sided complex conventions are both legitimate, but constants and conjugations differ.

8. **A3 has not yet produced the required tables.** The next round should contain reproducible data, not only protocols.

9. **H13 remains only an endpoint falsification test.** Its dual phase is Hessian-degenerate, and the key question is whether the dual $\chi_4(m)$ survives the first real norm extraction.

## New lemmas to add

### H4-R24. Finite Vaaler approximation with floor-compatible residual

**Status:** external theorem dependency; source-located, final rendered-page transcription pending.

For $H\ge1$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}
-\frac{\Phi(|h|/(H+1))}{2\pi i h}e(ht)
+
R_H^F(t),
$$

with

$$
|R_H^F(t)|\le \frac1{2H+2}K_H(t).
$$

At integers,

$$
V_H(n)=0,
\qquad
\psi_F(n)=-\frac12,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

### Alpha-Conjugacy-R24

**Status:** proved algebraic lemma.

For $1\le h\le H$,

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### C-TwoSided-Convention-R24

**Status:** proved algebraic lemma.

With

$$
C_h=e(h/4)-e(3h/4),
$$

one has

$$
C_{-h}=\overline{C_h}.
$$

For odd $h$,

$$
C_h=2i\chi_4(h),
$$

and for even $h$, $C_h=0$.

### Phi-Asymmetry-R24

**Status:** proved algebraic lemma.

For $0<u<1$,

$$
\Phi(u)+\Phi(1-u)=1.
$$

Thus $\Phi(1-u)=\Phi(u)$ is false except at $u=1/2$.

### R5-Full-R24

**Status:** proved conditional on H4 and $\tau(n)\ll_\epsilon n^\epsilon$.

For active dyadic blocks and $H\asymp D X^{-1/4}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon},
\qquad \rho\in\{1,3\}.
$$

### Bridge-R24

**Status:** conditional theorem.

If H1--H3, H4, R5-Full, and M9 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

M9 is open, so this is not a proof of the conjecture.

### M9-R24

**Status:** open analytic target.

For $X^{1/4}\le D\le X^{1/2}$ and $H_D\asymp D X^{-1/4}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-Pair-R24

**Status:** proved implementation lemma for real weights only.

For real $w_D$,

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}
\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_d w_D(d)e(hX/(4d)).
$$

### M2-CS-Normalizations-R24

**Status:** proved bounded-scope diagnostic.

Weighted $h$-Cauchy has acceptable diagonal but loses $\chi_4(h)$ sign through $|C_h|^2$. Unweighted $h$-Cauchy has endpoint diagonal $X^{3/4}$ and is too crude.

### M2-Q4-Expansion-R24

**Status:** proved algebraic identity.

For

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}C_h
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
$$

the fourth moment

$$
\mathcal Q_4(D;X)=|S_2(D;X)|^4
$$

expands as above, with resonance integer

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

### M2-Q4-DisplayedDiagonal-R24

**Status:** derived-under-assumptions.

The exact diagonal and pair-swapped diagonal have weighted mass $\asymp D^2$, hence are compatible with the fourth-moment target in the top block. This does not control all exact-resonance families.

### M2-Q4-NearCollision-Heuristic-R24

**Status:** heuristic diagnostic.

The band

$$
0<|N|\le D^4/X
$$

may have typical absolute weighted mass $X^{5/4}$ at $D\asymp X^{1/2}$ under a uniform-fiber model. This is a warning against absolute majorization, not a lower bound.

### CRI-Identity-R24

**Status:** proved algebraic identity under a fixed convention.

Under the paired real convention,

$$
\mathcal M_2(D;X)
=
-\frac8\pi(\Sigma_1^R-\Sigma_3^R),
$$

so

$$
|\mathcal M_2(D;X)|^2
=
\frac{64}{\pi^2}
|\Sigma_1^R-\Sigma_3^R|^2.
$$

Under the two-sided convention, constants should be recomputed before use.

### CRI-Ratio-Convention-R24

**Status:** falsification metric.

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}.
$$

Small values are promising, values near $1$ are neutral, and values near $2$ are adverse.

## Counterexample checks to run

1. **H4 rendered-page check.** Verify Vaaler's Theorem 6, equation (2.28), Section 7 equations (7.1)--(7.3), and Theorem 18, equation (7.14), against the rendered PDF.

2. **R5 exact-resonance tests.** For square, near-square, nonsquare, and divisor-rich $X$, compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

and

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}\left(\frac{X/d+\rho}{4}\right),
\qquad \rho\in\{1,3\},
$$

normalized by $X^{1/4}$.

3. **Raw-vs-paired M9 regression.** For real weights, compute raw complex two-sided $\mathcal M_i$ and paired real formulas for $i=1,2$ and verify agreement to high precision.

4. **M9 fixed-coefficient stress comparison.** Compute fixed Vaaler coefficients, random phase coefficients of the same magnitude, adversarial phase heuristics, and $L^1$ stress norms for $D=X^{1/4},X^{3/8},X^{1/2}$.

5. **M2 Cauchy kernel tests.** For weighted and unweighted $h$-Cauchy, report diagonal mass, off-diagonal mass, operator norm, absolute majorant, and signed/unsigned comparison.

6. **CRI endpoint tests.** Compute $R_{\rm CRI}$ for $X=10^6$ and $X=10^8$ at $D\asymp X^{1/2}$ and at intermediate scales.

7. **Fourth-moment exact bins.** Enumerate $N=0$ configurations and split into pair-swapped, semi-diagonal, denominator-paired, mixed, sign-symmetric, and unclassified bins. Report signed and absolute weighted mass.

8. **Near-collision bands.** Bin $|N|\sim T$ at endpoint scale. Compare observed signed and absolute masses against the heuristic $X^{5/4}$ weighted warning.

9. **Denominator-paired singular checks.** Isolate cases where $h_1=ac$, $h_3=-bc$, or values lie near truncation boundaries.

10. **Li--Yang typeset audit.** Resolve the Case A exponent ambiguity from the PDF and record exact hypotheses for $F,g,G,H,M,T$, allowed weights, and absolute-value placement.

11. **H13 endpoint test.** Run exactly one endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes; compare signed dual statistic, unsigned statistic, and diagonal-unitary operator norm.

## Research strategy adjustment

Round 25 should remain narrow and verification-forward. Keep the balanced hyperbola/Vaaler framework as the primary route while using the new alternatives as audited comparison modules.

The active work is no longer residual control. The residual side should remain recorded as provisionally controlled by H4 plus R5-Full. The active bottleneck is M9, especially $\mathcal M_2$.

Recommended effort split:

- **60% A3 execution:** actual tables for R5 residuals, raw-vs-paired M9, M2 kernels, CRI ratios, and fourth-moment bins.
- **25% A2 analytic cleanup:** exact-resonance taxonomy, denominator-paired singular cases, and near-collision band targets with explicit statuses.
- **15% A1 synthesis:** proof-draft updates, lemma-bank/gap-register updates, and source-level cleanup.

Assessments:

- **A2:** strongest new analytic contributor in Round 24. The fourth-moment expansion and CRI identity are valuable, but exact-resonance taxonomy and near-collision estimates are incomplete. A2 should not use route-closing language.
- **A3:** useful formula auditor, but under-executed. The next A3 output should contain tables and scripts, not another protocol-only response.
- **A1:** proof infrastructure remains reliable. A1 should keep the bridge conditional and promote only algebraic identities or bounded-scope diagnostics.

Keep Mellin--Perron, signed Fourier, Kuznetsov, Lindelof comparison, and H13 secondary. H13 gets exactly one endpoint falsification test unless the computed data justifies more.

## Next-round prompts by agent

### For A1

Produce the Round 25 proof-draft consolidation and state update.

Objectives:

1. Finalize H4 source normalization from the rendered Vaaler PDF. Quote exact theorem, page, and equation labels for:
   - Theorem 6 and equation (2.28) for $\widehat J$;
   - Section 7 equations (7.1)--(7.3) for $i_N,j_N,k_N$;
   - Theorem 18 and equation (7.14) for the residual inequality.

2. Insert H4-R24 into the best proof draft using

$$
\psi_F(t)=\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
|R_H^F(t)|\le\frac1{2H+2}K_H(t).
$$

3. Insert R5-Full-R24 with all edge cases:
   - nearest-integer tie convention;
   - exact resonance $W_\Delta(0)=1$;
   - shifted-leg product $X\approx d(4m-\rho)$;
   - positivity of $\ell=4m-\rho$ in the large active range;
   - small-$X$ separation;
   - short blocks $D<X^{1/4}$;
   - dyadic bounded overlap;
   - logarithmic losses.

4. State Bridge-R24 only conditionally:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Explicitly state that M9 is open.

5. Freeze M9-R24 with actual Vaaler coefficients. Keep arbitrary-coefficient variants only in a stress-test appendix.

6. Insert M9-Pair-R24 as an implementation lemma for real weights only, with a raw-vs-paired regression warning.

7. Insert Alpha-Conjugacy-R24, C-TwoSided-Convention-R24, and Phi-Asymmetry-R24.

8. Insert M2-CS-Normalizations-R24 as a bounded-scope diagnostic.

9. Insert M2-Q4-Expansion-R24 and CRI-Ratio-Convention-R24 only as proposed/falsification targets. Do not promote them to theorem-level M9 estimates.

10. Resolve the Li--Yang Case A ambiguity using the typeset PDF. Update the Li--Yang subrange map, but keep it as a guardrail unless theorem-level endpoint applicability is proved.

11. Add a Round 25 verification table template for A3's results, so future state updates can record data consistently.

12. Keep H13 as one endpoint falsification test only.

### For A2

Focus on $\mathcal M_2$ finite statistics. Produce a proof-draft-ready fourth-moment and CRI packet.

Objectives:

1. Freeze exactly one $h$ convention: either one-sided positive $h$ using the paired real formulas, or two-sided $1\le |h|\le H_D$. State how constants and conjugations change.

2. Define

$$
S_2(D;X)
=
\sum_h\alpha_{h,H_D}C_h
\sum_d w_D(d)e(hX/(4d)),
$$

and

$$
\mathcal Q_4(D;X)=|S_2(D;X)|^4.
$$

If using $\mathcal M_2=4S_2$, display the scalar factor $4^4=256$.

3. Write the full expansion with actual coefficients $\alpha_{h,H_D}$, actual $C_h$, dyadic weights, and exact phase.

4. Use the cleared denominator integer

$$
N
=
h_1d_2d_3d_4-h_2d_1d_3d_4
+h_3d_1d_2d_4-h_4d_1d_2d_3.
$$

5. Classify exact $N=0$ families:
   - pair-swapped;
   - exact diagonal;
   - semi-diagonal;
   - denominator-paired;
   - mixed denominator patterns;
   - sign-symmetric variants;
   - unclassified residue.

6. Repair denominator-paired endpoint/singularity cases. Explicitly separate cases such as $h_1=ac$, $h_3=-bc$, and values near truncation boundaries.

7. For every family, assign one of these statuses only: `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`.

8. Define near-collision bands $|N|\sim T$ and state the exact signed or absolute bound required over these bands to imply

$$
\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

9. Evaluate the $X^{5/4}$ weighted near-collision heuristic. State what it assumes, what it ignores, and exactly what A3 should measure.

10. Define CRI precisely under the chosen convention and state the exact identity linking $\mathcal M_2$ to $\Sigma_1-\Sigma_3$.

11. Either state a theorem-level CRI sufficient condition, with proof, or label CRI only as a falsification metric.

12. Supply A3-ready formulas for:
   - weighted and unweighted M2 Cauchy kernels;
   - CRI ratio;
   - fourth-moment exact bins;
   - near-collision banding;
   - denominator-paired singular checks.

13. Keep H13 and variable-$\theta$ discussion secondary. Do not claim that fourth moment or CRI proves M9.

### For A3

Execute computations and source checks. Do not produce another protocol-only response.

Objectives:

1. Provide high-precision R5 residual tables for $X=10^6$ and $X=10^8$, and at least one square, one near-square, one nonsquare, and one divisor-rich $X$. Include $D=X^{1/4},X^{3/8},X^{1/2}$ when feasible. Normalize results by $X^{1/4}$.

2. For the same samples, compute raw two-sided complex $\mathcal M_1,\mathcal M_2$ and paired real formulas. Report absolute and relative errors. Use real dyadic weights.

3. Compute fixed-coefficient M9 values

$$
|\mathcal M_i(D;X)|/X^{1/4}
$$

and compare with:
   - random phase coefficients of the same magnitudes;
   - adversarial coefficient heuristics;
   - termwise $L^1$ stress norms.

4. Implement the weighted and unweighted $\mathcal M_2$ Cauchy kernels. Report diagonal mass, off-diagonal mass, operator norm, absolute majorant, and signed/unsigned comparison.

5. Compute CRI ratios

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}{|\Sigma_1|^2+|\Sigma_3|^2}
$$

under the convention supplied by A2. If $R_{\rm CRI}\approx1$ at endpoint blocks, record CRI as deprioritized.

6. Enumerate fourth-moment exact-resonance bins for small feasible ranges. Report signed and absolute weighted mass by bin.

7. Bin near-collisions $|N|\sim T$ and compare observed masses to the $X^{5/4}$ weighted heuristic.

8. Test denominator-paired singular cases separately, especially near $h_1=ac$, $h_3=-bc$, and truncation boundaries.

9. Resolve the Li--Yang Case A ambiguity using the typeset PDF. Record exact theorem hypotheses for $F,g,G,H,M,T$, weights, and absolute-value placement.

10. Run one H13 endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes. Compare signed dual statistic, unsigned statistic, and diagonal-unitary operator-norm comparator.

11. Provide reproducible code snippets or exact pseudocode sufficient for audit. Label all small computations as verification data, not asymptotic evidence.

## Confidence

High confidence:

- The balanced hyperbola/Vaaler route remains the correct reduction framework.
- H1--H3 remain accepted arithmetic reductions for the current state.
- H4-R24 is correct in substance and source-located.
- The Fejer majorant covers the floor-compatible endpoint.
- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- $\Phi(u)+\Phi(1-u)=1$, so $\Phi(1-u)=\Phi(u)$ is false in general.
- R5-Full-R24 controls fixed Fejer residuals conditional on H4.
- Bridge-R24 is a valid conditional reduction.
- M9 remains open.
- Weighted and unweighted $\mathcal M_2$ Cauchy diagnostics are bounded-scope only.
- Black-box Li--Yang endpoint import is not justified.
- No new Gauss circle exponent is proved in Round 24.

Moderate confidence:

- The paired M9 formulas are correct for real weights and suitable for computation.
- The $\mathcal M_2$ fourth-moment object is the right next finite statistic to test.
- CRI is a useful falsification metric.
- The exact and pair-swapped diagonal mass estimates are compatible with the target after coefficient weights.
- H13 is worth exactly one endpoint falsification test.

Low confidence:

- The fourth moment or CRI will prove M9b without a new signed spacing theorem.
- BSOS-type signed statistics will prove M9a at the endpoint.
- H13 avoids character erasure after serious norm extraction.
- Lindelof for $L(1/2+it,\chi_4)$ directly implies M9.
- Kuznetsov/Kloosterman arithmetization matches M9 without substantial new machinery.
- Any current route in the repo proves a new exponent.
