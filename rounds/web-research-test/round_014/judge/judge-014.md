## Selected main route

Source basis: Round 14 agent outputs and reviews are in `judge_14.md`; the relevant retrieved passages state that no Round 14 output proves M9 or a new Gauss circle exponent, that the residual side is provisionally controlled by H4 plus R5-Full, and that the active bottleneck remains fixed-coefficient M9. The same packet records the Vaaler source anchors: Theorem 18, equation (7.14), for the residual inequality and Theorem 6, equation (2.28), for the Fourier transform formula for $J$. A web check confirms Li--Yang's arXiv metadata and abstract-level mechanism: Xiaochun Li and Xuerui Yang, arXiv:2308.14859, using Bombieri--Iwaniec with a new first-spacing estimate and Huxley second-spacing results.

Keep the balanced arithmetic hyperbola/Vaaler route as the selected framework:

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

The current proof-infrastructure bridge is:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is not a proof of the Gauss circle conjecture. H1--H3 are the accepted arithmetic reductions. H4 is now source-located and formula-consistent with Vaaler's periodic approximation, but the proof draft still needs the final page/equation notation translation. R5-Full should be treated as proved conditional on H4. M9 remains open and is the active analytic bottleneck.

The exact arithmetic input remains:

$$
P(X)
=
-4\sum_{d\le y}\chi_4(d)\psi(X/d)
+
4\sum_{d\le y}
\left[
\psi\left(\frac{X/d+1}{4}\right)
-
\psi\left(\frac{X/d+3}{4}\right)
\right]
+
O(1),
$$

where

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi(n)=-\frac12.
$$

For dyadic blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

use local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ should be removed before Vaaler is invoked and bounded trivially by $|\psi|\le 1/2$, giving an acceptable $O(X^{1/4})$ contribution up to logarithms.

The official remaining M9 targets use the actual Vaaler coefficients only:

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

Define

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
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

one may also write

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

The required endpoint-strength estimate is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over dyadic $D$.

## Useful fragments by source

### From A1

A1 supplied the canonical proof-infrastructure packet.

The strongest contribution is the H4 normalization against Vaaler. The repo form should be:

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H(t),
$$

with

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t),
$$

where

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(\frac{\sin \pi(H+1)t}{\sin \pi t}\right)^2.
$$

The floor-compatible conversion is correct in structure: Vaaler's centered polynomial has value $0$ at integers, while the repo sawtooth has $\psi_F(n)=-1/2$, and

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12
$$

covers exactly the half-jump. This is an endpoint convention that must be written in the proof draft.

A1's R5-Full product-count proof is the round's main mathematical consolidation. The Fejer bound

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
\frac{|X-md|}{D}
$$

on $d\asymp D$. With

$$
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

one obtains

$$
\frac1H K_H(X/d)
\ll
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by $n=md$ and using $\tau(n)\ll_\epsilon n^\epsilon$ gives

$$
\frac1H\sum_{d\asymp D}K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the shifted second residual legs, near-integrality of

$$
\frac{X/d+\rho}{4},
\qquad
\rho\in\{1,3\},
$$

is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing $\ell=4m-\rho$ again gives a product-counting problem, with a congruence restriction that only reduces multiplicity. This clears the Vaaler residual at the conjectural scale, conditional on H4 and dyadic bookkeeping.

A1's preferred M9b comparison formulation is also important. Instead of treating $\chi_4(h)$ as a nonsmooth periodic $h$-weight, write

$$
e(hX/(4d))(e(h/4)-e(3h/4))
=
e\left(h\left(\frac{X}{4d}+\frac14\right)\right)
-
e\left(h\left(\frac{X}{4d}+\frac34\right)\right).
$$

After scaling $d=Dz$, compare to Li--Yang-type sums using

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\}.
$$

This shifted-$F$ formulation is safer than absorbing $\chi_4(h)$ into bounded-variation weights.

### From A2

A2's best contribution is Q1-Spectral, a bounded-scope character-blindness diagnostic.

Let

$$
\mathcal D_{\rm odd}=\{d:D\le d<2D,\ 2\nmid d\},
\qquad
\mathcal V_D=\ell^2(\mathcal D_{\rm odd}),
$$

and define

$$
U=\operatorname{diag}(\chi_4(d)).
$$

On odd denominators, $U$ is a diagonal unitary involution. Therefore, for every matrix $K$,

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Thus any proof that places $\chi_4(d)$ into diagonal unitary conjugation and then estimates only by operator norm, spectral radius, Schur, Gershgorin, Frobenius, or an absolute-value matrix cannot exploit the spatial character. This should be added as a proved diagnostic, not as a global no-go theorem.

A2's H12 trace observation is correct in the same restricted sense:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This blocks pure conjugacy-invariant cyclic trace statistics. It does not block non-conjugacy signed forms, open-path statistics, cross-residue moments, or bilinear estimates that keep signs before norm extraction.

A2's H13/B-process-first transform remains the serious exploratory track. Splitting M9a modulo $4$ and applying Poisson should transfer $\chi_4$ to a dual Gauss factor. The dual length is

$$
m\asymp \frac{hX}{D^2}.
$$

At maximal Vaaler height $h\asymp H_D\asymp DX^{-1/4}$ and $D=X^\delta$,

$$
m\asymp X^{3/4-\delta},
\qquad
1/4\le\delta\le 1/2.
$$

Hence the transform is approximately balanced only near $D\asymp X^{1/2}$ and lengthens the dual variable for smaller $D$. The leading phase is square-root type,

$$
\Phi(h,m)\asymp \sqrt{Xhm},
$$

with

$$
\det\nabla^2\Phi=0.
$$

So H13 is not a route to generic full-rank stationary phase or generic full-rank decoupling. It remains a possible sign-preserving transform that requires a discrete signed-spacing theorem after transformation.

A2's CRI and BSOS proposals are not proof inputs yet. They are useful only if made executable: finite matrix, normalization, target bound, relation to M9, and falsification by comparison with an absolute majorant and an operator-norm bound.

### From A3

A3's best contribution is verification discipline.

The coefficient conjugacy check is correct:

$$
\alpha_{-h,H}
=
\overline{\alpha_{h,H}}.
$$

This is necessary for combining positive and negative frequencies correctly. The opposite textual claim

$$
\alpha_{-h,H}=-\overline{\alpha_{h,H}}
$$

must be rejected.

The special values

$$
\Phi(1/2)=\frac12,
$$

$$
\Phi(1/4)=\frac{3\pi}{16}+\frac14,
$$

and

$$
\Phi(3/4)=-\frac{3\pi}{16}+\frac34
$$

should be added as code-validation tests. In particular, $\Phi(1/4)\ne\Phi(3/4)$, so numerical M9 implementations must not impose a false symmetry.

A3 also correctly separates the H13 dual length

$$
M_{\rm dual}\asymp \frac{kX}{D^2}
$$

from the stationary-phase large parameter

$$
\Lambda\asymp \frac{kX}{D}.
$$

These two scales must not be conflated. Single-integral stationary phase remains a transform/asymptotic lemma, not a double-sum estimate.

A3's Li--Yang audit remains useful. In the raw endpoint substitution

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H=H_D\asymp X^{1/4},
$$

the audited restrictions give, for example,

$$
H\le MT^{-49/164}=X^{33/164}<X^{1/4}
$$

in Case A and

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}=X^{1/6}<X^{1/4}
$$

in Case B. Their final range reaches

$$
H\le MT^{-\theta^*},
\qquad
\theta^*=0.314483\ldots,
$$

not

$$
H\le MT^{-1/4}.
$$

Therefore Li--Yang cannot be imported as a black box at the endpoint Vaaler height. This is a theorem-application guardrail, not a global no-go theorem for Bombieri--Iwaniec methods.

A3's computations are still too small-scale to serve as endpoint evidence. They are useful for formula debugging and high-precision Fejer evaluation, but the next round must provide tables at meaningful dyadic sizes.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** Round 14 does not prove M9 and therefore does not prove $P(X)\ll_\epsilon X^{1/4+\epsilon}$.

2. **Reject treating R5-Full as unconditional before H4 is fully source-normalized.** R5 is mathematically sound conditional on Vaaler's residual theorem. The exact proof draft still needs the final notation translation from $N,j_N,k_N,\widehat J$ to $H,K_H,\alpha_{h,H}$.

3. **Reject arbitrary-coefficient M9 or residual targets as active dependencies.** The active targets use fixed Vaaler coefficients. Arbitrary bounded coefficients and $L^1$ stress norms remain diagnostics only.

4. **Reject black-box Li--Yang endpoint import.** The phase class is relevant, but the printed Case A/B restrictions and final $\theta^*$ range do not cover $H_D\asymp D X^{-1/4}$ at the endpoint.

5. **Reject global no-go claims for Bombieri--Iwaniec, Li--Yang, spacing, or decoupling.** Q1-Spectral blocks only routes that pass through diagonal-unitary conjugation followed by unitarily invariant or absolute-value norms.

6. **Reject H13 as an endpoint estimate.** H13 is a transform plus diagnostic. It preserves a dual character at the Gauss-factor level but gives no bound without a signed-spacing theorem.

7. **Reject generic full-rank stationary phase on the H13 dual phase.** The phase $\sqrt{Xhm}$ has degenerate Hessian.

8. **Reject CRI or BSOS as proved escapes.** They are proposed signed statistics. They need finite definitions, normalization, target inequalities, and numerical falsification tests.

9. **Reject treating $\chi_4(h)$ in M9b as a harmless bounded-variation weight.** Its total variation is $\asymp H$ on an interval of length $H$. Use shifted-$F$ or arithmetic-progression formulations unless a theorem explicitly accepts such weights.

10. **Reject the factorial-alignment obstruction.** Exact divisor alignments in the critical window satisfy

$$
\#\{d\in[X^{1/4},X^{1/2}]:d\mid X\}
\le \tau(X)\ll_\epsilon X^\epsilon.
$$

They do not create a dense obstruction.

11. **Reject unsafe floating-point-only Fejer tests near resonances.** Near integer arguments of $K_H$, ordinary sine evaluation can miss exact spikes or create artificial blowups. Use high precision or exact rational/modular checks.

12. **Reject pivoting to Mellin--Perron or signed Fourier as the main route.** They remain comparison modules. Neither currently replaces M9.

## Known gaps

1. **H4 proof-draft citation gap.** The correct source anchors appear to be Vaaler Theorem 18, equations (7.13)--(7.17), especially (7.14), and Theorem 6, equation (2.28). The final proof draft must quote exact page/equation references and translate notation.

2. **H4 convention gap.** The proof must explicitly distinguish Vaaler's centered value at integers from the repo's floor-compatible value $\psi(n)=-1/2$.

3. **R5-Full bookkeeping gap.** The proof must explicitly include first leg, shifted legs $\rho=1,3$, real and integer $X$, nearest-integer tie rules, sign and positivity of $\ell=4m-\rho$, zero Fejer mode, both frequency signs, dyadic weights, bounded overlap, short blocks $D<X^{1/4}$, and logarithmic losses.

4. **M9 main-term gap.** No endpoint estimate is known for $\mathcal M_1(D;X)$ or $\mathcal M_2(D;X)$.

5. **M9b theorem-extension gap.** The shifted functions

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

have the same derivative nondegeneracy as $1/(4z)$, but an actual theorem must allow the $D,X$-dependent constant term and the Vaaler dyadic $h$ weights.

6. **Li--Yang subrange map gap.** The raw endpoint block fails. The repo still needs a precise covered/uncovered map over all $D=X^\delta$ and $H\le H_D$ using the exact Li--Yang theorem hypotheses.

7. **Signed-spacing gap.** Q1-Spectral explains why operator norms lose $\chi_4$. The repo still lacks a positive signed-form estimate that preserves $\chi_4(d_1)\chi_4(d_2)$ or $\chi_4(h)$ through a useful inequality.

8. **H13 transform gap.** Need exact modulo-$4$ Poisson normalization, constant, Gauss factor, active sign, stationary point, leading amplitude, boundary terms, nonstationary integration by parts, and a range table for $D=X^\delta$.

9. **H13 summation gap.** Even after stationary phase, a discrete signed-spacing theorem is required for the Hessian-degenerate square-root phase.

10. **CRI/BSOS gap.** These statistics need a precise finite matrix or bilinear form, localization weight, normalization, target bound, and evidence that they do not collapse to $U^*KU$ or an absolute-value majorant.

11. **Numerical evidence gap.** Round 14 includes useful small checks and protocols. It does not yet include endpoint-scale tables for R5, M9 fixed coefficients, stress norms, shifted M9b matrices, or H13 signed/unsigned comparisons.

12. **Poisson--Bessel calibration gap.** The calibration route remains useful for normalizations and the $R^{2/3}$ sanity check, but it was not advanced in Round 14.

## New lemmas to add

### H4-R14. Vaaler finite approximation with floor-compatible residual

**Status:** external theorem dependency, source-located; proof-draft notation translation still pending.

For $H\ge1$,

$$
\psi_F(t)=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H(t),
$$

where

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
$$

and

$$
|R_H(t)|\le \frac1{2H+2}K_H(t).
$$

At integers, $K_H(0)/(2H+2)=1/2$ covers $\psi_F(n)=-1/2$.

### R5-R14. Product-count Fejer residual bound

**Status:** proved conditional on H4.

For $X^{1/4}\le D\le X^{1/2}$ and $H\asymp D X^{-1/4}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and, for $\rho\in\{1,3\}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The proof uses the product-count substitution $n=md$ in the first leg and $n=(4m-\rho)d$ in the shifted legs, plus $\tau(n)\ll_\epsilon n^\epsilon$.

### Bridge-R14. Conditional endpoint reduction

**Status:** proved conditional theorem.

If H1--H3, H4-R14, R5-R14, and M9 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is the current best proof skeleton.

### M9-R14. Fixed-coefficient main-term target

**Status:** open analytic target.

For every dyadic $D$ with $X^{1/4}\le D\le X^{1/2}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

Arbitrary-coefficient variants are stress tests only.

### M9b-Shifted-F. Shifted phase formulation for the second main term

**Status:** algebraic reformulation; theorem-extension gap open.

Use

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\},
$$

to compare M9b with reciprocal double-sum theorems. Do not treat $\chi_4(h)$ as a harmless bounded-variation weight unless a theorem explicitly permits it.

### Q1-Spectral-R14. Diagonal-unitary operator-norm blindness

**Status:** proved diagnostic with restricted scope.

On odd denominators, $U=\operatorname{diag}(\chi_4(d))$ is unitary, and

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

This blocks only methods that reduce to such an operator-norm or absolute-value matrix estimate.

### H12-R14. Pure cyclic trace blindness

**Status:** proved diagnostic with restricted scope.

For pure conjugacy-invariant cyclic traces,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This does not block open-path or non-conjugacy signed statistics.

### H13-R14. B-process-first transform for M9a

**Status:** exploratory transform; not an estimate.

Modulo-$4$ Poisson should transfer $\chi_4(d)$ to a dual Gauss factor and yield dual length

$$
m\asymp \frac{hX}{D^2}.
$$

At maximal height and $D=X^\delta$,

$$
m\asymp X^{3/4-\delta}.
$$

The leading phase is square-root type with degenerate Hessian. H13 is useful only if a subsequent signed-spacing step avoids Q1-Spectral blindness.

### Phi-R14. Vaaler coefficient checks

**Status:** proved algebraic/computational guardrails.

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

and

$$
\Phi(1/2)=\frac12,\qquad
\Phi(1/4)=\frac{3\pi}{16}+\frac14,\qquad
\Phi(3/4)=-\frac{3\pi}{16}+\frac34.
$$

### Divisor-Alignment-R14

**Status:** proved guardrail.

For integer $X$,

$$
\#\{d\in[X^{1/4},X^{1/2}]:d\mid X\}
\le \tau(X)\ll_\epsilon X^\epsilon.
$$

Exact divisor alignment alone is not a dense critical-block obstruction.

## Counterexample checks to run

1. **H4 page-level source check.** Verify Vaaler Theorem 18 and Theorem 6 against the PDF: coefficient sign, $\Phi$, Fejer normalization, residual constant, and notation translation.

2. **H4 integer jump test.** Symbolically and numerically verify $V_H(n)=0$, $K_H(0)=H+1$, and $K_H(0)/(2H+2)=1/2$.

3. **R5 first-leg stress test.** Compute

$$
R_1(D;X)=\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

for square, near-square, nonsquare, and divisor-rich $X$.

4. **R5 shifted-leg stress test.** For $\rho\in\{1,3\}$ compute

$$
R_{2,\rho}(D;X)=
\frac1{H_D}\sum_{d\asymp D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right).
$$

5. **R5 continuous-$X$ test.** Use $X=N+\eta$ with very small positive and negative $\eta$ and verify uniform summability of

$$
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right).
$$

6. **R5 dyadic bookkeeping test.** Check zero mode, both frequency signs, all dyadic $D$, bounded partition overlap, and short-block removal.

7. **M9 fixed-coefficient numerics.** Compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ using actual $\alpha_{h,H_D}$ and report

$$
|\mathcal M_i(D;X)|/X^{1/4}.
$$

8. **M9 stress comparison.** Compare fixed coefficients with arbitrary phase coefficients and $L^1$ stress norms.

9. **M9b shifted-$F$ theorem audit.** Verify whether candidate theorems allow

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

uniformly in $D,X$.

10. **M9b fractional-frequency matrix test.** Compare phases

$$
e(qX/d)
$$

and

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\},
$$

in actual toy spacing matrices.

11. **Li--Yang line audit.** Record exact TeX/PDF labels for $S$, Case A, Case B, main theorem, final $S/H$ target, theorem prerequisites, allowed weights, and allowed $F$ forms.

12. **Q1-Spectral matrix test.** Construct the Gram matrix arising from a Cauchy--Schwarz step on M9a and verify whether the character enters only as $U^*KU$.

13. **CRI/BSOS falsification test.** Build one concrete signed statistic, compare it with its absolute-value majorant and operator-norm bound, and deprioritize it if no stable advantage appears.

14. **H13 transform constants.** Verify the modulo-$4$ Poisson constant, active sign, stationary point, leading phase, amplitude, and dual length.

15. **H13 first-spacing falsification.** After H13, apply the first intended Cauchy--Schwarz or spacing step and check whether $\chi_4(m)$ survives as a signed statistic or becomes a diagonal-unitary factor erased by an operator norm.

16. **H13 endpoint-range test.** Focus on $D\asymp X^{1/2}$, where the dual length is closest to the original Vaaler height.

17. **High-precision Fejer test.** Evaluate $K_H(t)$ near exact resonances using high precision or exact rational handling.

18. **Mellin--Perron/signed Fourier comparison.** Keep these only as comparison modules and test whether their replacement errors reduce to M9-like or R5-like structures.

## Research strategy adjustment

Round 14 should be recorded as a proof-infrastructure and M9-diagnostic round.

The residual side is no longer the active bottleneck:

$$
\text{H4}+\text{R5-Full}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon},
$$

conditional on final H4 source-normalization and dyadic bookkeeping.

The active work is now M9: fixed Vaaler coefficients, exact character placement, and endpoint-strength reciprocal double sums. Do not revert to arbitrary coefficient formulations except in stress-test sections.

Assessment of A2: A2 contributed valuable Q1-Spectral, H12, and H13 diagnostics. The useful part is the precise diagnosis of operator-norm blindness. The risky part is overbroad obstruction language and undeveloped CRI/BSOS claims. Next round should require proof-draft-ready statements, no route-closing language, and one executable statistic with falsification data.

Assessment of A3: A3 contributed useful verification: coefficient conjugacy, $\Phi$ values, integer-jump check, Li--Yang endpoint mismatch, and scale separation in H13. The weak point is that several computations are still toy-scale or protocol-level. Next round should require executed tables, exact source line labels, and high-precision Fejer/M9 data.

The next round should not expand the route set. It should finish H4/R5 proof infrastructure, make M9 theorem comparison sharper, and run falsifiable sign-preservation tests.

## Next-round prompts by agent

### For A1

Produce the Round 15 proof-infrastructure and theorem-comparison packet.

Objectives:

1. **Finalize H4 source-normalization.**
   - Quote Vaaler's exact page, theorem, and equation numbers.
   - Translate $N,j_N,k_N,\widehat J_{N+1}$ into $H,K_H,\alpha_{h,H}$.
   - Verify the sign of $\alpha_{h,H}$.
   - Verify the residual constant.
   - State the centered-to-floor-compatible conversion at integers.

2. **Insert R5-Full into the proof draft.**
   Include first leg, shifted legs $\rho=1,3$, real and integer $X$, nearest-integer tie rules, congruence $\ell=4m-\rho$, dyadic weights, zero mode, frequency signs, short blocks, and logarithmic losses.

3. **Write the bridge theorem in final proof-draft form.**
   State:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

4. **Freeze M9 as the only active analytic target.**
   Use actual $\alpha_{h,H_D}$ only. Move arbitrary-coefficient variants to a stress-test appendix.

5. **Write the M9b theorem-extension problem precisely.**
   Use the shifted-$F$ formulation

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}.
$$

   State what theorem hypotheses must be checked: allowed $D,X$ dependence, dyadic $h$ weights from $\alpha_{h,H}$, derivative constants, and endpoint height.

6. **Produce the Li--Yang subrange map.**
   For $D=X^\delta$ and $H\le H_D$, table the ranges covered by raw Case A, raw Case B, and final $\theta^*$ reduction. Identify the uncovered high-frequency interval.

Exploratory allocation: write a one-page H13 falsification checklist. The checklist should say exactly where H13 becomes unhelpful if the first post-transform step collapses to $U^*KU$.

### For A2

Produce a conservative proof-draft-ready diagnostics and signed-statistic packet.

Objectives:

1. **Rewrite Q1-Spectral as a bounded-scope lemma.**
   Define the finite space, $U=\operatorname{diag}(\chi_4(d))$, prove

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}},
$$

   and list exactly which methods this blocks and does not block.

2. **Rewrite H12 trace invariance narrowly.**
   Prove only

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m)
$$

   for pure cyclic traces. Do not claim this blocks non-conjugacy signed forms.

3. **Repair C3 claims.**
   State exact variables, lattice hypotheses, odd/even dilation cases, and whether each claim is connected to M9/H13 or merely a diagnostic model.

4. **Formalize H13.**
   Give exact modulo-$4$ Poisson summation under $e(t)=e^{2\pi i t}$, Gauss factor, active sign, stationary point, leading amplitude, dual length $m\asymp hX/D^2$, range table for $D=X^\delta$, and Hessian-degeneracy check.

5. **Perform the H13 first-step falsification.**
   After the transform, apply the first intended Cauchy--Schwarz or spacing step. Decide whether $\chi_4(m)$ survives in a non-conjugacy statistic or collapses to a diagonal-unitary operator-norm pattern.

6. **Define one executable sign-preserving statistic.**
   CRI or BSOS is acceptable only if it includes:
   - finite matrix or bilinear form;
   - localization weight;
   - normalization;
   - proposed target bound;
   - relationship to M9;
   - absolute-majorant comparator;
   - falsification criterion.

Exploratory allocation: focus the signed-statistic test near $D\asymp X^{1/2}$, where H13 is most balanced.

### For A3

Execute verification and computation tasks. Prioritize tables, scripts, exact formulas, and line labels.

Objectives:

1. **Verify H4 against Vaaler.**
   Provide exact page/equation references for Theorem 18 and Theorem 6. Confirm $\Phi$, $\alpha_{h,H}$, $K_H$, residual constant, and integer-jump convention.

2. **Run R5 numerical tables.**
   Include first leg and shifted legs $\rho=1,3$ for square, near-square, nonsquare, and divisor-rich $X$, across $D\asymp X^{1/4},X^{3/8},X^{1/2}$. Normalize by $X^{1/4}$.

3. **Run M9 fixed-coefficient numerics.**
   Compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ using exact $\alpha_{h,H_D}$. Compare fixed coefficients, arbitrary phase coefficients, and $L^1$ stress norms. Report $|\mathcal M_i|/X^{1/4}$.

4. **Use high precision near Fejer spikes.**
   Avoid float-only sine evaluations near integer arguments. Use high precision or exact rational/modular checks.

5. **Complete Li--Yang line audit.**
   Record exact labels and line/page locations for $S$, Case A, Case B, the main theorem, final $S/H$ reduction, theorem prerequisites, allowed weights, and allowed $F$ hypotheses. Treat any suspected typo as a source-audit issue unless conclusively resolved.

6. **Test M9b shifted-$F$.**
   Check derivative constants for

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
$$

   and compare fractional-frequency toy matrices with unshifted matrices.

7. **Verify H13 constants and regimes.**
   Confirm the modulo-$4$ Poisson constant, active sign, stationary point, leading phase, amplitude, $M_{\rm dual}\asymp hX/D^2$, $\Lambda\asymp hX/D$, nonstationary decay, support-boundary cases, and $M_{\rm dual}\asymp1$ transition.

8. **Implement Q1/CRI/BSOS tests.**
   Once A2 gives a finite statistic, compute signed, unsigned, absolute-majorant, and operator-norm comparators.

Exploratory allocation: run H13 signed-vs-unsigned matrix tests near $D\asymp X^{1/2}$ and report whether the dual character survives the first spacing step.

## Confidence

High confidence in the balanced hyperbola/Vaaler framework as the current reduction and diagnostic route.

High confidence that no new Gauss circle exponent was proved in Round 14.

High confidence that H1--H3 remain the correct arithmetic foundation.

High confidence that R5-R14 proves the blockwise Fejer residual bound conditional on H4.

Moderate-to-high confidence that H4 has the correct source anchors and formula translation, but the final proof-draft citation and notation check should still be completed.

High confidence that R5-Full removes the Vaaler residual from the active bottleneck after dyadic bookkeeping.

High confidence that M9 fixed-coefficient main sums remain open and are the active analytic bottleneck.

High confidence that arbitrary-coefficient residual and main-term variants are stress tests, not active dependencies.

High confidence that direct Li--Yang black-box import fails in the endpoint Vaaler height range.

High confidence that Q1-Spectral is correct as a restricted operator-norm blindness diagnostic.

Moderate confidence that the shifted-$F$ formulation is the right official M9b theorem-comparison formulation.

Moderate confidence that H13 is worth one more focused, falsifiable exploration round.

Low confidence that H13, CRI, BSOS, signed Fourier truncation, Mellin--Perron, or current printed Li--Yang technology proves M9 without a new signed or endpoint-strength estimate.

Overall Round 14 judgment: productive and conservative. The concrete progress is a cleaner H4 normalization, a complete conditional R5 residual proof, a bridge theorem ready for proof-draft insertion, sharper M9/M9b targets, and stronger diagnostics for when character signs are erased by norm-based methods. The conjectural Gauss circle bound remains unproved.