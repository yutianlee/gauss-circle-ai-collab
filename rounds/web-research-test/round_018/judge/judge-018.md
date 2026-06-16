## Selected main route

Source basis: Round 18 packet and active outputs from A1, A2, and A3 in the uploaded audit bundle. The retrieved Round 18 materials record the same conservative bridge, the M9 bottleneck, the Q1/BSOS diagnostics, and the next-round verification requirements.

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

The current conservative bridge remains:

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

This is **not** a proof of the Gauss circle conjectural bound. Round 18 proves no new exponent. The residual side of the Vaaler reduction is now provisionally controlled by `H4 + R5-Full`, conditional on final source-normalization of Vaaler's theorem and complete proof-draft edge-case bookkeeping. The active analytic bottleneck remains `M9`, the fixed-Vaaler-coefficient main sums.

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

For dyadic denominator blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

use local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ should be removed before Vaaler expansion and bounded directly by $|\psi_F|\le 1/2$.

The active M9 target uses the actual Vaaler coefficients

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

The raw main terms are:

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_d
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_d
w_D(d)e(hX/(4d)).
$$

The required endpoint-strength estimate is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for all dyadic $D$ in $X^{1/4}\le D\le X^{1/2}$. No Round 18 output proves this.

## Useful fragments by source

### From A1

A1 supplied the strongest proof-draft consolidation.

The useful core is the proof-draft form of:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

A1's `H4-R18` formulation is the current official statement, pending final page/equation transcription from Vaaler:

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
\frac1{2H+2}K_H(t),
$$

where

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin\pi(H+1)t}{\sin\pi t}\right)^2.
$$

The centered-to-floor-compatible endpoint convention is correctly handled:

$$
V_H(n)=0,\qquad
\psi_F(n)=-\frac12,\qquad
K_H(0)=H+1,\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

A1 also gives the cleanest `R5-Full-R18` proof. With

$$
H\asymp D X^{-1/4},
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

the Fejer kernel bound

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right)
$$

gives

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg, choosing $m$ nearest to $X/d$ gives

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

Define

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min\left(1,\Delta^2/u^2\right),&u\ne0.
\end{cases}
$$

Then

$$
\frac1H K_H(X/d)
\ll
W_\Delta(X-md).
$$

Grouping by $n=md$ gives divisor multiplicity at most $\tau(n)$, hence

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)W_\Delta(X-n)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the shifted residual legs, near-integrality of

$$
\frac{X/d+\rho}{4},
\qquad
\rho\in\{1,3\},
$$

is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing $\ell=4m-\rho$ gives $n=d\ell$, with the congruence restriction $\ell\equiv-\rho\pmod4$ only reducing multiplicity. The same divisor-counting proof applies.

A1's Li--Yang range table is useful as a guardrail. Writing

$$
D=X^\delta,\qquad H=X^\beta,
$$

the Vaaler endpoint height is

$$
\beta_V=\delta-\frac14.
$$

The final Li--Yang record-exponent range has

$$
\beta_*=\delta-\theta^*,
\qquad
\theta^*=0.3144831759741\cdots.
$$

At $D=X^{1/2}$, the Vaaler endpoint is $\beta_V=1/4$, while the final Li--Yang range reaches only

$$
\beta_*=1/2-\theta^*
=
0.1855168240259\cdots.
$$

The gap is

$$
\beta_V-\beta_*=\theta^*-\frac14
=
0.0644831759741\cdots.
$$

Thus Li--Yang/Bombieri--Iwaniec technology remains structurally relevant, but it cannot be imported as a black box at the endpoint Vaaler height.

A1's `M9b-Shift` formulation is the right theorem-comparison form for the second main term. Instead of treating $\chi_4(h)$ as a rough periodic $h$-weight, use

$$
e(hX/(4d))(e(h/4)-e(3h/4))
=
e\left(h\left(\frac{X}{4d}+\frac14\right)\right)
-
e\left(h\left(\frac{X}{4d}+\frac34\right)\right).
$$

After setting $d=Dz$, the phase comparison uses

$$
F_{\rho,D}(z)
=
\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\}.
$$

The derivative nondegeneracy is unchanged:

$$
F'F'''-3(F'')^2=-\frac3{8z^6}.
$$

The theorem-extension gap is whether an applicable theorem permits the parameter-dependent additive shift, fixed Vaaler $h$ weights, and endpoint height.

### From A2

A2's main contribution is the bounded-scope character-blindness diagnostic for the actual M9a matrix route.

Under one weighted Cauchy--Schwarz normalization, A2 defines

$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right).
$$

On

$$
\mathcal V_D=\ell^2(\mathcal D_{\rm odd}),
\qquad
\mathcal D_{\rm odd}=\{d:D\le d<2D,\ 2\nmid d\},
$$

let

$$
U=\operatorname{diag}(\chi_4(d)).
$$

Since $\chi_4(d)\in\{\pm1\}$ on odd $d$, $U$ is unitary and

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

This proves that any method which inserts $\chi_4(d)$ only as diagonal unitary conjugation and then estimates by operator norm, Frobenius norm, singular spectrum, Schur/Gershgorin, cyclic trace, or absolute-value matrix is character-blind. This is a rigorous diagnostic under its stated hypothesis; it is not a global no-go theorem.

A2 also gives the narrow cyclic-trace identity:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This blocks only pure conjugacy-invariant trace statistics. It does not block open-path moments, non-conjugacy signed forms, cross-residue statistics, or direct signed bilinear estimates.

A2's `BSOS-R18` is useful as a finite diagnostic. For the same frozen weighted kernel, define

$$
\mathcal S_{\rm signed}
=
\sum_{d_1\ne d_2}
\chi_4(d_1)\chi_4(d_2)K_{d_1,d_2},
$$

with comparators

$$
\mathcal S_{\rm abs}
=
\sum_{d_1\ne d_2}|K_{d_1,d_2}|,
$$

and

$$
\mathcal S_{\rm op}
=
|\mathcal D_{\rm odd}|\|K_{\rm off}\|_{\operatorname{op}}.
$$

A bound of the form

$$
|\mathcal S_{\rm signed}|
\ll_\epsilon X^{1/2+\epsilon}
$$

is a plausible sufficient target for the weighted Cauchy--Schwarz path to M9a, after accounting for the diagonal term and logarithmic losses. But it should not be called necessary for all approaches to M9a, and BSOS remains a falsification statistic until the implication is written with one frozen normalization and no hidden loss.

A2's `H13-Dual` warning is useful but conditional. If B-process-first is followed by a spacing step that gives a dual quadratic form

$$
v^*\widetilde U^*\widetilde K\widetilde Uv,
\qquad
\widetilde U=\operatorname{diag}(\chi_4(m)),
$$

then Q1-Spectral reappears in the dual variable. The exact post-H13 amplitude, support, active sign, and kernel must be written before this diagnostic is promoted.

### From A3

A3's useful contribution is formula auditing, plus correction pressure on implementation details.

A3 independently verifies:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

and gives the paired real forms for real dyadic weights. If

$$
A_h(D;X)
=
\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
$$

then

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\Im A_h(D;X).
$$

If

$$
B_h(D;X)
=
\sum_{d\asymp D}w_D(d)e(hX/(4d)),
$$

then

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\Re B_h(D;X).
$$

These formulas are useful for computation, but the raw two-sided complex definitions remain canonical. Every implementation must regression-test raw and paired forms.

A3's H13 constants are useful after fixing one convention. With

$$
\phi_k(u)=\frac{hX}{u}-\frac{ku}{4},
$$

the stationary terms are $k=-m<0$ and

$$
u_0=2\sqrt{\frac{hX}{m}},
\qquad
\phi_{-m}(u_0)=\sqrt{hXm},
\qquad
m\asymp \frac{hX}{D^2}.
$$

At maximal Vaaler height $h\asymp D X^{-1/4}$ and $D=X^\delta$, this gives

$$
m\asymp X^{3/4-\delta}.
$$

The transform is near-balanced only at $\delta=1/2$. The dual phase

$$
\Phi(h,m)=\sqrt{Xhm}
$$

has zero continuous Hessian determinant, so generic full-rank two-dimensional stationary phase or decoupling is unavailable.

A3 also flags the implementation priority: move from protocols and tiny toy checks to executed high-precision or exact tables. This is the right next step. Tiny examples are formula checks, not asymptotic evidence.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** M9 is still open, so the conditional bridge does not prove $P(X)\ll_\epsilon X^{1/4+\epsilon}$.

2. **Reject treating R5-Full as unconditional.** R5-Full is a proof-draft lemma conditional on H4, the finite Vaaler theorem with correct source normalization and endpoint convention.

3. **Reject arbitrary-coefficient M9 and residual targets as active dependencies.** They are stress tests only. The active M9 targets use fixed Vaaler coefficients.

4. **Reject black-box Li--Yang endpoint import.** The phase class is relevant, but published Li--Yang ranges do not reach $H_D\asymp D X^{-1/4}$ in the endpoint region.

5. **Reject treating Q1-Spectral as a global no-go theorem.** It blocks only routes that reduce the signed structure to diagonal-unitary conjugation followed by unitarily invariant or absolute-value norm estimates.

6. **Reject treating BSOS as a proof lemma.** BSOS is a proposed finite diagnostic or conditional sufficient target. It becomes a lemma only after the exact implication to M9a is proved under one frozen Cauchy--Schwarz normalization.

7. **Reject mixing Cauchy--Schwarz kernels.** The kernel with $|\alpha_h|$, a kernel with $|\alpha_h|^2$, and an unweighted $h$ kernel are different. Each has a different target normalization. Round 19 must freeze the official diagnostic kernel before computation.

8. **Reject H13 as an endpoint estimate.** H13 is a transform and falsification tool. It preserves a dual $\chi_4$ factor at the Poisson stage, but gives no bound without a signed spacing estimate.

9. **Reject generic full-rank tools on H13.** The phase $\sqrt{Xhm}$ has degenerate Hessian.

10. **Reject unsafe Fejer numerics near exact resonances.** Use $K_H(0)=H+1$, $H^{-1}K_H(0)\le2$, exact modular checks, or high precision. Do not use floating sine quotients alone.

11. **Reject treating toy computations as evidence.** Small examples are regression tests for formula correctness only.

12. **Reject pivoting to Mellin--Perron, signed Fourier truncation, or generic Bessel methods as the main route.** Keep them as comparison modules until M9 diagnostics have been executed.

## Known gaps

1. **H4 final citation gap.** The Vaaler source anchors are identified, but the proof draft still needs exact page/equation transcription and a final coefficient-sign check in the convention $e(t)=e^{2\pi it}$.

2. **M9 main-term gap.** There is no endpoint estimate for $\mathcal M_1(D;X)$ or $\mathcal M_2(D;X)$.

3. **M9b theorem-extension gap.** The shifted functions

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

pass derivative tests, but an actual theorem must allow the parameter-dependent additive shift, fixed Vaaler $h$ weights, endpoint height, and positive/negative frequency pairing.

4. **Frozen Cauchy--Schwarz normalization gap.** The official matrix diagnostic must choose one kernel: $|\alpha_h|$, $|\alpha_h|^2$, or another weight. Do not mix them.

5. **BSOS implication gap.** A precise statement is needed: what bound on $\mathcal S_{\rm signed}$, under which exact kernel and diagonal term, implies M9a? Until then BSOS is a falsification metric.

6. **H13 kernel gap.** The post-transform main term must include exact modulo-$4$ Poisson constant, active sign, stationary amplitude, support, transition regimes, and the first intended spacing step.

7. **Li--Yang line-audit gap.** The TeX source should be audited with exact labels and line ranges for the definition of $S$, the conditions on $F$, Case A, Case B, final $S/H$ bound, main theorem, final argument, and goal. The current phase-shape comparison is not theorem applicability.

8. **R5 edge-case write-up gap.** The proof must explicitly include real $X$, integer $X$, nearest-integer ties, exact resonances, shifted-leg positivity of $\ell=4m-\rho$, short blocks, dyadic weights, and bounded-overlap logarithmic losses.

9. **Numerical evidence gap.** No Round 18 output supplies executed endpoint-scale tables for R5, M9, Q1, BSOS, or H13. Protocols are not data.

10. **Signed-spacing gap.** The project lacks a positive estimate that preserves $\chi_4(d_1)\chi_4(d_2)$ or $\chi_4(h)$ through a useful non-conjugacy inequality.

## New lemmas to add

### H4-R18. Finite Vaaler approximation with floor-compatible residual

**Status:** external theorem dependency; source-normalized in substance, final citation pass pending.

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
|R_H^F(t)|\le \frac1{2H+2}K_H(t).
$$

At integers, $K_H(0)/(2H+2)=1/2$ covers $\psi_F(n)=-1/2$.

### CCoef-R18. Vaaler coefficient conjugacy

**Status:** proved algebraic lemma.

For all $1\le h\le H$,

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### R5-Full-R18. Fejer residual product-count bound

**Status:** provisionally proved conditional on H4.

For $X^{1/4}\le D\le X^{1/2}$ and $H\asymp D X^{-1/4}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### Bridge-R18. Conditional endpoint reduction

**Status:** proof skeleton.

If H1--H3, H4, R5-Full, and M9 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-R18. Fixed-coefficient main-term target

**Status:** open.

For all dyadic $D$ with $X^{1/4}\le D\le X^{1/2}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-Pair-R18. Paired real formulas

**Status:** proved algebraic implementation lemma for real dyadic weights.

For real $w_D$,

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\Im
\sum_{d\asymp D}
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\Re
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

Raw two-sided complex definitions remain canonical.

### M9b-ShiftedF-R18

**Status:** theorem-extension formulation.

The second main term can be compared to phases with

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\},
$$

and

$$
F'F'''-3(F'')^2=-\frac3{8z^6}.
$$

The theorem-applicability gap remains open.

### LY-Map-R18

**Status:** theorem-application guardrail.

For $D=X^\delta$, $H=X^\beta$, the endpoint Vaaler height is

$$
\beta_V=\delta-\frac14.
$$

Li--Yang's final record-exponent range gives

$$
\beta_*=\delta-\theta^*,
\qquad
\theta^*=0.3144831759741\cdots.
$$

At every $\delta$, the endpoint gap against the final range is

$$
\beta_V-\beta_*=\theta^*-\frac14>0.
$$

### Q1-Spectral-R18

**Status:** proved bounded-scope diagnostic.

If a spacing step puts the character only into

$$
U=\operatorname{diag}(\chi_4(d)),
$$

and the matrix becomes $U^*KU$, then every unitarily invariant norm estimate is character-blind:

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

### H12-R18

**Status:** proved bounded-scope diagnostic.

For pure cyclic traces,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

### M9a-CS-Kernel-R18

**Status:** algebraic formulation under frozen weighted Cauchy--Schwarz.

The weighted kernel is

$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right).
$$

Alternative kernels with $|\alpha_h|^2$ or unweighted coefficients must be recorded separately.

### BSOS-R18

**Status:** proposed falsification statistic / conditional target, not a proof lemma.

For the frozen kernel,

$$
\mathcal S_{\rm signed}
=
\sum_{d_1\ne d_2}
\chi_4(d_1)\chi_4(d_2)K_{d_1,d_2}.
$$

It becomes a usable lemma only after a precise implication to M9a is proved under the frozen normalization.

### H13-Dual-R18

**Status:** conditional diagnostic.

If the post-H13 first spacing step yields a dual diagonal conjugation

$$
\widetilde U=\operatorname{diag}(\chi_4(m)),
$$

then Q1-Spectral reappears. The exact post-H13 kernel and sign convention must be verified first.

## Counterexample checks to run

1. **H4 source and sign check.** Quote Vaaler's Theorem 18 and Theorem 6 with exact printed page/equation labels. Verify the coefficient sign under $e(t)=e^{2\pi it}$.

2. **Integer convention check.** Verify

$$
V_H(n)=0,\qquad
\psi_F(n)=-1/2,\qquad
K_H(0)/(2H+2)=1/2.
$$

3. **R5 exact-resonance check.** Test cases with

$$
X/d\in\mathbb Z
$$

and verify that implementations use

$$
K_H(0)=H+1,\qquad
H^{-1}K_H(0)\le2,
$$

not a singular sine quotient.

4. **R5 shifted-resonance check.** Test cases with

$$
\frac{X/d+\rho}{4}\in\mathbb Z,
\qquad
\rho\in\{1,3\}.
$$

Verify $X=d(4m-\rho)$ and $\ell=4m-\rho\equiv-\rho\pmod4$.

5. **R5 divisor-rich stress test.** Use square, near-square, nonsquare, and divisor-rich $X$ across

$$
D\asymp X^{1/4},\quad X^{3/8},\quad X^{1/2}.
$$

6. **Short-block check.** Confirm all $D<X^{1/4}$ blocks are handled before Vaaler expansion and contribute $O(X^{1/4+\epsilon})$.

7. **M9 raw/paired regression.** For several $X,D,H_D$, compute $\mathcal M_1,\mathcal M_2$ from both raw two-sided complex definitions and paired real formulas. They must agree to high precision.

8. **M9 fixed-versus-stress comparison.** Compare fixed Vaaler coefficients against arbitrary phase coefficients and $L^1$ stress norms.

9. **Freeze the Cauchy--Schwarz kernel.** Decide whether the official BSOS/Q1 test uses $|\alpha_h|$, $|\alpha_h|^2$, or another normalization. Do not mix kernels.

10. **Q1 matrix test.** Build the actual M9a Gram matrix for the frozen normalization and verify

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

11. **BSOS signed-vs-unsigned test.** Compute

$$
\mathcal S_{\rm signed},\qquad
\mathcal S_{\rm abs},\qquad
|\mathcal D_{\rm odd}|\|K_{\rm off}\|_{\operatorname{op}},
$$

and report ratios.

12. **M9b shifted-$F$ audit.** Check whether the intended theorem allows

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

uniformly in $D,X$, with the actual Vaaler $h$ weights and endpoint height.

13. **Li--Yang exact-source audit.** Record exact TeX labels and line numbers for the double sum $S$, conditions on $F$, Case A, Case B, final $S/H$ target, main theorem, and final argument.

14. **H13 sign convention check.** Under

$$
\phi_k(u)=hX/u-ku/4,
$$

verify active stationary index $k=-m<0$ and

$$
u_0=2\sqrt{\frac{hX}{m}},
\qquad
\phi_{-m}(u_0)=\sqrt{hXm},
\qquad
m\asymp hX/D^2.
$$

15. **H13 first-step falsification.** Build the endpoint post-H13 kernel near $D\asymp X^{1/2}$ and determine whether $\chi_4(m)$ appears only by diagonal-unitary conjugation or in a non-conjugacy signed statistic.

16. **High-precision Fejer/M9 computations.** Use exact rational/modular checks near Fejer resonances; do not rely on ordinary floating sine evaluations.

## Research strategy adjustment

Continue the balanced hyperbola/Vaaler route. Do not pivot.

The residual side should now stay provisionally cleared by `H4 + R5-Full`, pending final source citation and numerical regression. The active work is `M9`.

Recommended Round 19 allocation:

- **50% proof-draft consolidation:** final H4 source citations, corrected R5-Full proof with edge cases, exact M9 raw definitions, paired-form regression warnings, and Li--Yang shifted-$F$ audit.
- **30% numerical certificate:** high-precision R5 tables, fixed-coefficient M9 tables, Q1/BSOS matrix tests at $D=X^{1/4},X^{3/8},X^{1/2}$, and square/near-square/nonsquare/divisor-rich $X$.
- **20% bounded exploration:** one endpoint H13 signed-vs-unsigned test near $D\asymp X^{1/2}$, after fixing sign convention and stationary amplitude.

The key strategic change is to stop adding new diagnostics until the existing finite diagnostics are executed. A2 supplied a candidate signed statistic; A3 should compute it. A1 should consolidate proof text rather than broaden the route.

## Next-round prompts by agent

### For A1

Produce the Round 19 proof-draft consolidation.

Objectives:

1. Finalize `H4-R18` with exact Vaaler source labels. Quote the theorem/equation/page references for Theorem 18 and Theorem 6. Translate $N,j_N,k_N,\widehat J_{N+1}$ into $H,V_H,K_H,\Phi,\alpha_{h,H}$. Verify coefficient sign under $e(t)=e^{2\pi it}$.

2. Insert corrected `R5-Full-R18` into the best proof draft. Include first leg, shifted legs $\rho=1,3$, real and integer $X$, nearest-integer tie rules, exact resonance $W_\Delta(0)=1$, congruence $\ell=4m-\rho$, positivity of $\ell$, zero Fejer mode, both signs of frequency, dyadic weights, short blocks, and logarithmic losses.

3. State `Bridge-R18` only conditionally:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Do not imply M9 is proved.

4. Freeze `M9-R18` with raw complex definitions of $\mathcal M_1,\mathcal M_2$ using actual $\alpha_{h,H_D}$ only. Put arbitrary-coefficient variants in a stress-test appendix.

5. Record `M9-Pair-R18` only as an implementation lemma for real dyadic weights. Require regression against raw two-sided complex sums.

6. Complete `M9b-ShiftedF-R18` as a theorem-extension checklist: parameter-dependent additive shift, derivative constants, smooth weight class, actual Vaaler $h$ weights, endpoint frequency height, and positive/negative frequency pairing.

7. Build the exact Li--Yang source map from the local TeX: definition of $S$, conditions on $F$, Case A, Case B, final $S/H$ target, main theorem, final argument, and goal. Record the uncovered interval for $D=X^\delta$.

8. Keep H13 to a one-page falsification checklist only; do not attempt a broad transform route.

### For A2

Produce a proof-draft-ready signed-diagnostic note.

Objectives:

1. Freeze exactly one Cauchy--Schwarz normalization for M9a. Use either the $|\alpha_h|$ kernel or explicitly justify another kernel. Define the finite index set, kernel $K$, diagonal character operator $U$, and quadratic form.

2. State `Q1-Spectral-R18` for that exact kernel and prove precisely what it blocks and what it does not block.

3. State `H12-R18` narrowly for pure cyclic traces. Explicitly list open-path moments and non-conjugacy signed forms as not blocked.

4. Define `BSOS-R18` with:
   - $\mathcal S_{\rm signed}$;
   - $\mathcal S_{\rm abs}$;
   - $\mathcal S_{\rm op}$;
   - diagonal contribution;
   - the exact target bound.

5. Prove the exact conditional implication from the BSOS target to M9a under the frozen Cauchy--Schwarz normalization, or explicitly relabel BSOS as a falsification statistic only. Avoid "must" or route-closing language unless a necessary condition has actually been proved.

6. Repair `H13-Dual-R18` as a conditional test. State the post-transform kernel only after fixing amplitude, support, and active sign. Say "if this kernel reduces to diagonal unitary conjugation, Q1 applies"; do not claim H13 fails globally.

7. Provide a finite signed-vs-unsigned test plan compatible with A3's computation.

### For A3

Prioritize executed computations, exact tables, and source citations over prose.

Objectives:

1. Produce an exact H4 source table from Vaaler's PDF:
   - theorem/equation/page;
   - Vaaler object;
   - repo object;
   - coefficient sign;
   - residual constant;
   - integer jump convention.

2. Run corrected R5 raw-form tables with exact or high-precision arithmetic:

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d),
\qquad
\frac1{H_D}\sum_{d\asymp D}K_{H_D}\left(\frac{X/d+\rho}{4}\right),
\quad \rho=1,3.
$$

Use square, near-square, nonsquare, and divisor-rich $X$; use $D\asymp X^{1/4},X^{3/8},X^{1/2}$.

3. Run paired-M9 regression tests. Compute $\mathcal M_1,\mathcal M_2$ both from raw two-sided complex definitions and paired real formulas. Report normalized values

$$
|\mathcal M_i(D;X)|/X^{1/4}.
$$

4. Run fixed-coefficient versus stress-norm comparisons: fixed Vaaler coefficients, arbitrary phase coefficients, and $L^1$ stress norms.

5. Build the official Q1/BSOS matrix once A2 freezes the kernel. Compute

$$
\|U^*KU\|_{\operatorname{op}},\quad
\|K\|_{\operatorname{op}},\quad
\mathcal S_{\rm signed},\quad
\mathcal S_{\rm abs},\quad
\mathcal S_{\rm op}.
$$

6. Complete the Li--Yang line audit from the local TeX source with exact labels and line numbers.

7. Fix H13 sign convention and produce an amplitude/dual-length table. Under $\phi_k(u)=hX/u-ku/4$, verify $k=-m<0$, $u_0=2\sqrt{hX/m}$, $\phi_{-m}(u_0)=\sqrt{hXm}$, and $m\asymp hX/D^2$.

8. Implement one endpoint H13 signed-vs-unsigned matrix test near $D\asymp X^{1/2}$ only after the sign and amplitude are fixed.

## Confidence

High confidence in the selected balanced hyperbola/Vaaler framework as the current proof-infrastructure route.

High confidence that Round 18 proves no new Gauss circle exponent.

High confidence in H1--H3, the coefficient conjugacy, Q1-Spectral-R18, and H12-R18 under their stated hypotheses.

Moderate-to-high confidence that H4-R18 is correctly normalized in substance, pending exact proof-draft source quotation.

Moderate-to-high confidence that R5-Full-R18 controls the fixed Fejer residual at $X^{1/4+\epsilon}$ after the exact-resonance wording and edge-case bookkeeping are repaired.

High confidence that M9 remains the sole active analytic bottleneck.

Moderate confidence in the M9b shifted-$F$ formulation as the right theorem-comparison object.

Moderate confidence that A2's BSOS framework is a useful finite diagnostic, but low confidence that it is a proof lemma until its exact implication is written and tested.

Moderate confidence that H13 will re-enter Q1 blindness after a standard Cauchy--Schwarz step, but low confidence until the exact post-transform kernel and sign convention are fixed.

Low confidence that existing Li--Yang/Bombieri--Iwaniec technology proves M9 at endpoint height.

Overall Round 18 judgment: productive and conservative. The proof skeleton is cleaner, the residual side is conditionally under control, the M9 bottleneck is sharply isolated, and the next round should move from further prose diagnostics to exact source transcription plus executable verification of M9/Q1/BSOS.