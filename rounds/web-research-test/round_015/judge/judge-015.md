## Summary

Round 15 is a proof-infrastructure and diagnostic round. It does **not** prove a new Gauss circle exponent.

The current conservative reduction remains:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

where $P(X)=N(\sqrt X)-\pi X$. The residual side of the finite Vaaler route is now provisionally controlled by H4 plus R5-Full. The active analytic bottleneck is M9: the fixed-Vaaler-coefficient reciprocal main sums. Arbitrary-coefficient main sums and $L^1$ variants remain stress tests only.

Source basis: uploaded Round 15 packet, local source audits, and web metadata checks. Vaaler's source is Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc.* 12(2), 183--216, 1985; Project Euclid/AMS metadata confirms the publication. Li--Yang is arXiv:2308.14859v2, Xiaochun Li and Xuerui Yang, last revised 14 September 2023; the arXiv page states the Bombieri--Iwaniec / first-spacing / Huxley second-spacing mechanism and gives DOI `10.48550/arXiv.2308.14859`.

The local audit note is incorporated: A2's official Stage A response is the cleaned `A2-015.md`; A2's second pass is supplemental only. A2's review is useful but below the configured target by local count, and its high-certainty wording must be downgraded unless backed by exact hypotheses and proof. The correct Vaaler coefficient conjugacy is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

Any negative-conjugate recombination is an algebra error.

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

The exact arithmetic input remains:

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

For dyadic blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

use the local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ should be removed before applying Vaaler and bounded trivially by $|\psi_F|\le 1/2$.

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

Thus

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

one may equivalently write

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

The required endpoint-strength estimate is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over dyadic $D$.

## Useful fragments by source

### From A1

A1 supplies the canonical proof-infrastructure packet.

The strongest contribution is H4 source normalization. In repo notation, the finite Vaaler statement should be:

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
|R_H^F(t)|\le \frac{1}{2H+2}K_H(t),
$$

where

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin \pi(H+1)t}{\sin \pi t}\right)^2.
$$

The source anchors remain Vaaler Theorem 18, equations (7.13)--(7.16), especially (7.14), for the residual inequality, and Theorem 6, equation (2.28), for the Fourier coefficient function. The final proof draft still needs exact page/equation transcription and notation translation.

A1 also gives the decisive R5 product-count mechanism. The Fejer bound

$$
K_H(t)\ll \min\left(H,\frac{1}{H\|t\|^2}\right)
$$

implies

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac{1}{H^2\|t\|^2}\right).
$$

For the first residual leg, choose $m$ nearest to $X/d$. Since $d\asymp D$,

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

With

$$
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

one obtains

$$
\frac1H K_H(X/d)
\ll
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by $n=md$ gives divisor multiplicity at most $\tau(n)$, hence

$$
\frac1H\sum_{d\asymp D}K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the shifted second residual legs,

$$
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\},
$$

near-integrality is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing $\ell=4m-\rho$ again gives a product-counting problem, with the congruence restriction $\ell\equiv-\rho\pmod4$ only reducing divisor multiplicity. This clears the Vaaler residual at the conjectural scale, conditional on H4.

A1's M9b shifted-$F$ formulation is the preferred theorem-comparison form. Instead of treating $\chi_4(h)$ as a rough bounded-variation weight, use

$$
e(hX/(4d))(e(h/4)-e(3h/4))
=
e\left(h\left(\frac{X}{4d}+\frac14\right)\right)
-
e\left(h\left(\frac{X}{4d}+\frac34\right)\right).
$$

After setting $d=Dz$, compare to phases with

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\}.
$$

The derivative nondegeneracy is unchanged:

$$
F'F'''-3(F'')^2=-\frac3{8z^6}.
$$

The open theorem question is whether a Bombieri--Iwaniec/Li--Yang-type theorem permits this $D,X$-dependent constant shift and the fixed Vaaler $h$ weights at endpoint height.

### From A2

A2's useful core is the bounded-scope operator-norm diagnostic.

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

On odd denominators, $U$ is a diagonal unitary involution. Hence for every matrix $K$,

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Thus any method that inserts $\chi_4(d)$ only as diagonal unitary conjugation and then bounds by operator norm, spectral radius, Schur/Gershgorin, Frobenius norm, or absolute-value matrix is character-blind. This is a proved diagnostic under the stated hypothesis, not a global obstruction.

A2's H12 trace observation is also correct in restricted form:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This blocks pure conjugacy-invariant cyclic trace statistics, but not open-path statistics, non-conjugacy signed forms, cross-residue moments, or bilinear estimates that keep signs before norm extraction.

A2's H13 transform is worth one more falsification-focused round. Splitting M9a modulo $4$ and applying Poisson should yield

$$
\sum_d\chi_4(d)w_D(d)e(hX/d)
=
\frac{i}{2}
\sum_n\chi_4(n)
\int w_D(u)e(hX/u-nu/4)\,du,
$$

under the convention $e(t)=e^{2\pi i t}$, up to a global sign depending on the Fourier transform convention. The stationary sign must be fixed explicitly: for the displayed phase

$$
hX/u-nu/4,
$$

one has a stationary point only when $n<0$. Writing $n=-m$,

$$
u_0=2\sqrt{\frac{hX}{m}},
\qquad
m\asymp\frac{hX}{D^2}.
$$

At maximal Vaaler height $h\asymp H_D\asymp DX^{-1/4}$ and $D=X^\delta$,

$$
m\asymp X^{3/4-\delta},
\qquad
1/4\le\delta\le1/2.
$$

Thus H13 is roughly balanced only near $D\asymp X^{1/2}$ and lengthens the dual variable for smaller $D$. The leading phase is of square-root type,

$$
\Phi(h,m)\asymp \sqrt{Xhm},
$$

and

$$
\det\nabla^2\Phi=0.
$$

So H13 cannot be followed by generic full-rank two-dimensional stationary phase or decoupling. It remains an exploratory sign-preserving transform requiring a discrete signed-spacing theorem.

A2's BSOS proposal is not yet a lemma. It is useful only as an executable signed-statistic candidate. It needs a finite definition, a derivation from M9, a target bound, an absolute-majorant comparator, and a falsification criterion.

A2's Round 15 review should be used selectively. It is structurally useful, but local audit found it below the configured target despite its self-check, and several formulations are too conclusive. Round 16 must require a literal low-temperature standard: accurate local word-count self-check, neutral formula-level verification, fewer high-certainty verbs, and no route-closing claims without exact hypotheses.

### From A3

A3 provides useful source and computation checks, but some numerical claims require correction before use.

The valuable H4 audit identifies Vaaler Theorem 18 and Theorem 6 as the right source anchors. A3 also correctly checks the integer jump:

$$
V_H(n)=0,
\qquad
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12,
$$

which exactly covers the difference between the centered trigonometric value and the floor-compatible value $\psi_F(n)=-1/2$.

A3's special values of $\Phi$ are useful for code validation:

$$
\Phi(1/2)=\frac12,
$$

$$
\Phi(1/4)=\frac{3\pi}{16}+\frac14,
$$

$$
\Phi(3/4)=-\frac{3\pi}{16}+\frac34.
$$

Therefore $\Phi(1/4)\ne\Phi(3/4)$, and M9 code must not impose false coefficient symmetry.

A3 also supports the Li--Yang endpoint non-import. With

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H=H_D\asymp X^{1/4},
$$

Li--Yang Case A gives

$$
H\le MT^{-49/164}=X^{33/164}<X^{1/4},
$$

and Case B gives

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}=X^{1/6}<X^{1/4}.
$$

Their final range reaches

$$
H\le MT^{-\theta^*},
\qquad
\theta^*=0.3144831759741\ldots,
$$

not

$$
H\le MT^{-1/4}.
$$

This is a theorem-application guardrail, not a proof that all Bombieri--Iwaniec methods fail.

A3's numerical section needs correction. In particular:

- The coefficient relation must be

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

not $-\overline{\alpha_{h,H}}$.

- The R5 toy table appears to double-divide by $H$ after already listing $K_H/H$ terms. The small example should not be used as evidence until recomputed from the raw definition.

- The H13 stationary sign must match the displayed Fourier convention. For $hX/u-nu/4$, the active index has $n<0$.

A3's toy computations are useful as protocols, not endpoint evidence. Round 16 must produce reproducible tables or scripts with exact formulas and high precision.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.**  
Round 15 does not prove M9 and therefore does not prove

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

2. **Reject treating H4 as fully finalized before final notation transcription.**  
The source anchors are correct, but the proof draft still needs the exact conversion from Vaaler's $N,j_N,k_N,\widehat J$ notation to $H,K_H,\alpha_{h,H}$, including page/equation references.

3. **Reject reopening H5r-B or H5r-L1 as active dependencies.**  
The residual is controlled directly by the positive Fejer kernel and R5. Arbitrary bounded coefficients and $L^1$ residual norms are stress tests only.

4. **Reject arbitrary-coefficient M9 as the official target.**  
The active target is fixed-coefficient M9 with actual $\alpha_{h,H_D}$. Arbitrary coefficients are useful for stress testing but are not created by the Vaaler reduction.

5. **Reject black-box Li--Yang endpoint import.**  
The phase class is relevant, but the published Case A/B ranges and final $\theta^*$ range do not cover endpoint height $H_D\asymp D X^{-1/4}$.

6. **Reject global no-go claims for Bombieri--Iwaniec, Li--Yang, spacing, or decoupling.**  
Q1-Spectral blocks only routes that factor the character into diagonal-unitary conjugation and then use unitarily invariant or absolute-value bounds. It does not block all signed estimates.

7. **Reject treating H13 as an endpoint estimate.**  
H13 is a transform plus a falsification framework. It does not supply a double-sum bound.

8. **Reject generic full-rank stationary phase or decoupling on the H13 dual phase.**  
The phase $\sqrt{Xhm}$ has degenerate Hessian.

9. **Reject BSOS as a proved escape.**  
BSOS is a proposed signed statistic. It needs a proof that its target implies M9 and a numerical comparison with absolute-majorant and operator-norm bounds.

10. **Reject using $\chi_4(h)$ in M9b as a harmless bounded-variation weight.**  
Its total variation is $\asymp H$ on an interval of length $H$. Use the shifted-$F$ representation or residue splitting unless a theorem explicitly allows such weights.

11. **Reject unsafe floating-point-only Fejer and M9 tests.**  
Near resonances, ordinary sine evaluation can miss exact spikes or create artificial blowups. Use high precision or exact rational/modular checks.

12. **Reject A3's negative-conjugate M9 recombination.**  
The correct identity is $\alpha_{-h,H}=\overline{\alpha_{h,H}}$. Any numerical table using the opposite relation must be recomputed.

## Known gaps

1. **H4 final citation and notation gap.**  
Need exact page/equation references and a proof-draft dictionary from Vaaler's notation to repo notation.

2. **H4 convention gap.**  
The proof must explicitly distinguish Vaaler's centered sawtooth from the floor-compatible $\psi_F(n)=-1/2$ and show that the Fejer residual covers the half-jump.

3. **R5-Full bookkeeping gap.**  
The final proof must cover first leg, shifted legs $\rho=1,3$, real and integer $X$, nearest-integer tie rules, sign and positivity of $\ell=4m-\rho$, zero Fejer mode, both signs of frequency, dyadic weights, bounded overlaps, short blocks, and logarithmic losses.

4. **M9 main-term gap.**  
No endpoint estimate is known for $\mathcal M_1(D;X)$ or $\mathcal M_2(D;X)$.

5. **M9b theorem-extension gap.**  
The shifted functions

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

have uniform derivative nondegeneracy, but a candidate theorem must allow the $D,X$-dependent constant shift and actual Vaaler $h$ weights at endpoint height.

6. **Li--Yang subrange map gap.**  
The raw endpoint block fails. The reading packet needs a table over $D=X^\delta$ and $H=X^\beta$ showing raw Case A, raw Case B, final $\theta^*$ range, and the uncovered Vaaler interval.

7. **Signed-spacing gap.**  
Q1-Spectral explains why operator-norm-only methods lose $\chi_4$. The repo still lacks a signed-form estimate that preserves $\chi_4(d_1)\chi_4(d_2)$ or $\chi_4(h)$ through a useful inequality.

8. **H13 transform gap.**  
Need exact modulo-$4$ Poisson normalization, active sign, stationary point, leading amplitude, nonstationary integration-by-parts bounds, boundary/transition regimes, and a post-transform signed statistic that avoids Q1-Spectral.

9. **BSOS/CRI gap.**  
No finite signed statistic has yet been shown to imply M9. A2's proposal needs normalization, target inequality, absolute comparator, and falsification data.

10. **Numerical reliability gap.**  
A3's current data are toy-scale and include normalization/sign issues. Round 16 needs reproducible high-precision computations.

## New lemmas to add

### H4-R15. Finite Vaaler approximation with floor-compatible residual

**Status:** external theorem dependency; source-located, final notation transcription pending.

For every integer $H\ge1$,

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

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
$$

and

$$
|R_H^F(t)|\le \frac1{2H+2}K_H(t).
$$

Here

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

The coefficient conjugacy is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### R5-R15. Fejer product-count residual bound

**Status:** proved conditional on H4.

For $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp D X^{-1/4}$, and $|w_D|\le C$ supported on $d\asymp D$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### R5-Full-R15. Total Vaaler residual bound

**Status:** proved conditional on H4 and dyadic bookkeeping.

Assuming H4-R15, all Vaaler residual terms arising from H3 contribute

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

### Bridge-R15. Conditional endpoint reduction

**Status:** proved conditional theorem.

If H1--H3, H4-R15, R5-Full-R15, and M9-R15 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-R15. Fixed-coefficient main-term criterion

**Status:** official open target.

For every dyadic

$$
X^{1/4}\le D\le X^{1/2},
$$

prove

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

with the actual coefficients $\alpha_{h,H_D}$.

### M9b-ShiftedF-R15. Shifted phase theorem-extension problem

**Status:** open theorem-extension target.

For

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\},
$$

one has

$$
\frac{hX}{D}F_{\rho,D}(d/D)
=
h\left(\frac{X}{4d}+\frac{\rho}{4}\right),
$$

and

$$
F'F'''-3(F'')^2=-\frac3{8z^6}.
$$

A candidate theorem must allow this shifted $F$, actual Vaaler $h$ weights, and endpoint height $H\le D X^{-1/4}$.

### LY-Subrange-R15. Li--Yang parameter comparison

**Status:** theorem-comparison map, not an obstruction theorem.

For $D=X^\delta$ and $H=X^\beta$,

$$
\beta_V=\delta-\frac14,
$$

$$
\beta_A=\delta-\frac{49}{164},
$$

$$
\beta_B=\min\left(\frac{3\delta}{2}-\frac12,\frac{35\delta-6}{69}\right),
$$

and

$$
\beta_*=\delta-\theta^*,
\qquad
\theta^*=0.3144831759741\ldots.
$$

Direct final Li--Yang range leaves the interval

$$
\max(0,\beta_*)<\beta\le\beta_V
$$

uncovered.

### Q1-Spectral-R15

**Status:** proved diagnostic, bounded scope.

If $\chi_4$ enters a matrix estimate only through

$$
K\mapsto U^*KU,
\qquad
U=\operatorname{diag}(\chi_4(d)),
$$

then

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

### H12-Trace-R15

**Status:** proved diagnostic, bounded scope.

For pure cyclic traces,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This does not apply to open-path or non-conjugacy signed statistics.

### H13-Mod4-R15

**Status:** transform lemma pending convention-finalization.

Under $e(t)=e^{2\pi i t}$ and a fixed Fourier convention,

$$
\sum_d\chi_4(d)w_D(d)e(hX/d)
=
\frac{i}{2}
\sum_n\chi_4(n)
\int w_D(u)e(hX/u-nu/4)\,du
$$

up to a global sign. For the displayed phase, the stationary contribution has $n=-m<0$ and

$$
m\asymp \frac{hX}{D^2}.
$$

### H13-Falsification-R15

**Status:** diagnostic checklist.

If the first post-H13 step sends the dual character into a diagonal unitary conjugation and then applies operator norm or an absolute-value bound, H13 is character-blind for that proof path. H13 remains viable only if a genuinely signed statistic survives.

### BSOS-R15

**Status:** proposed signed statistic, not a lemma.

A BSOS or CRI statistic is admissible only if it specifies a finite matrix or bilinear form, localization, normalization, target bound, implication to M9, absolute-majorant comparator, operator-norm comparator, and falsification criterion.

## Counterexample checks to run

1. **H4 source citation check.**  
Quote Vaaler Theorem 18 and Theorem 6 with exact printed page and equation numbers; transcribe the notation map.

2. **H4 integer-jump check.**  
Verify

$$
V_H(n)=0,
\qquad
K_H(0)=H+1,
\qquad
K_H(0)/(2H+2)=1/2.
$$

3. **Coefficient conjugacy check.**  
Symbolically and numerically verify

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

Recompute all paired-frequency formulas using this identity.

4. **R5 raw-form recomputation.**  
Compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

and the shifted analogues for $\rho=1,3$ without double division.

5. **R5 stress cases.**  
Test square, near-square, nonsquare, and divisor-rich $X$ across $D\asymp X^{1/4},X^{3/8},X^{1/2}$.

6. **M9 fixed-coefficient numerics.**  
Compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ with actual $\alpha_{h,H_D}$ and report

$$
|\mathcal M_i(D;X)|/X^{1/4}.
$$

7. **M9 stress comparison.**  
Compare fixed coefficients with arbitrary phase coefficients and dyadic $L^1$ stress norms.

8. **M9b shifted-$F$ audit.**  
Check theorem hypotheses for

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

with uniform constants.

9. **Li--Yang subrange table.**  
For $D=X^\delta$, table $\beta_V,\beta_A,\beta_B,\beta_*$ for at least $\delta=1/4,3/8,1/2$ and identify covered/uncovered intervals.

10. **Q1-Spectral matrix test.**  
Construct the Gram matrix arising from the first natural Cauchy--Schwarz step on M9a and verify whether the character appears only as $U^*KU$.

11. **H13 sign and constant check.**  
Fix the Fourier convention and verify the modulo-$4$ Poisson constant, active sign, stationary point, leading phase, amplitude, and dual length.

12. **H13 first-step falsification.**  
After H13, apply the intended first Cauchy--Schwarz or spacing step and record whether $\chi_4(m)$ survives or is erased by operator norm.

13. **BSOS/CRI finite test.**  
Compute signed statistic, unsigned statistic, absolute majorant, operator-norm bound, and ratio. Deprioritize BSOS if it behaves like the absolute/operator-norm comparator.

14. **High-precision Fejer tests.**  
Use high precision or exact rational/modular handling near resonances.

15. **A2 compliance check.**  
For Round 16, verify that A2's response and review include accurate local word-count self-checks and avoid unsupported high-certainty route-closing language.

## Research strategy adjustment

Round 15 should be recorded as a proof-infrastructure consolidation round.

The residual side is no longer the active bottleneck:

$$
\text{H4}+\text{R5-Full}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon},
$$

conditional on final H4 source-normalization and complete dyadic bookkeeping.

The active work is M9. Do not revert to arbitrary-coefficient versions except as stress tests. The main analytic question is whether the fixed Vaaler coefficients and character placements can be exploited before Cauchy--Schwarz, operator norms, or absolute values erase them.

Allocate the next round approximately as follows:

- 80%: finalize H4/R5 proof text, correct coefficient pairing, produce Li--Yang subrange maps, and compute M9 with exact coefficients.
- 20%: one falsifiable exploratory track, preferably H13/BSOS near $D\asymp X^{1/2}$.

Assessment of A2: useful diagnostics, but overclaim risk remains. Next round must enforce low-temperature review literally: formula-level verification, exact hypotheses, accurate self-count, no unsupported finality language.

Assessment of A3: useful audit and protocols, but current numeric results include sign and normalization issues. Next round must prioritize corrected scripts/tables over prose protocols.

## Next-round prompts by agent

### For A1

Produce the Round 16 proof-draft and theorem-comparison packet.

Objectives:

1. **Finalize H4 source-normalization.**
   Quote Vaaler's exact printed page, theorem, and equation numbers for Theorem 18 and Theorem 6. Translate $N,j_N,k_N,\widehat J$ into $H,V_H,K_H,\Phi,\alpha_{h,H}$. State the centered-to-floor-compatible convention at integers.

2. **Write R5-Full as a completed proof-draft lemma.**
   Include first leg, shifted legs $\rho=1,3$, real/integer $X$, tie rules for nearest integer, congruence $\ell=4m-\rho$, positivity of $\ell$, zero mode, both frequency signs, dyadic weights, short blocks, and logarithmic losses.

3. **State Bridge-R16 cleanly.**
   Write

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

4. **Correct all coefficient pairing.**
   Use only

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

Derive the real paired-frequency form of M9 from the raw definition.

5. **Freeze M9 as the active target.**
   Define $\mathcal M_1,\mathcal M_2$ using actual Vaaler coefficients only. Move arbitrary-coefficient variants to a stress-test appendix.

6. **Complete the M9b shifted-$F$ theorem-extension statement.**
   Specify the exact theorem hypotheses needed for

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}.
$$

7. **Produce the Li--Yang subrange map.**
   For $D=X^\delta$ and $H=X^\beta$, tabulate raw Case A, raw Case B, final $\theta^*$ range, endpoint Vaaler height, and the uncovered interval.

Exploratory allocation: write a one-page H13 falsification checklist focused on the endpoint $D\asymp X^{1/2}$ and explicitly identify when the dual character becomes a Q1-Spectral diagonal-unitary artifact.

### For A2

Produce a low-temperature, proof-draft-ready signed-diagnostic packet.

Mandatory style and audit constraints:

- Use the cleaned A2 Stage A as the baseline; do not rely on the second Gemini pass except as supplemental provenance.
- Perform an accurate local word-count self-check.
- Use neutral formula-level verification.
- Avoid high-certainty verbs and route-closing language unless exact hypotheses and proof are supplied.
- Label central claims as `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`.

Objectives:

1. **Rewrite Q1-Spectral narrowly.**
   Define $\mathcal V_D$, $U=\operatorname{diag}(\chi_4(d))$, and prove

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

List exactly which methods this blocks and which it does not block.

2. **Rewrite H12 trace invariance narrowly.**
   Prove only

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m)
$$

for pure cyclic traces.

3. **Repair C3 relevance.**
   State variables and hypotheses. Mark half-integer translation/dilation facts as model diagnostics unless explicitly connected to M9 or H13.

4. **Formalize H13 under one convention.**
   Give exact modulo-$4$ Poisson summation with $e(t)=e^{2\pi i t}$, active sign, stationary point, amplitude, dual length $m\asymp hX/D^2$, range table for $D=X^\delta$, and Hessian-degeneracy check.

5. **Run H13 first-step falsification symbolically.**
   After the transform, apply the first intended Cauchy--Schwarz or spacing step. State whether $\chi_4(m)$ becomes a diagonal-unitary conjugation or remains in a non-conjugacy signed statistic.

6. **Make BSOS or CRI executable.**
   Provide one finite statistic with localization, normalization, target inequality, implication to M9, absolute-majorant comparator, operator-norm comparator, and falsification criterion.

Exploratory allocation: focus the signed-statistic test near $D\asymp X^{1/2}$, where H13 is closest to balanced.

### For A3

Execute corrected verification and computation tasks. Prioritize scripts, tables, exact formulas, and line labels.

Objectives:

1. **Verify H4 against Vaaler with line/page labels.**
   Provide exact page/equation references for Theorem 18 and Theorem 6. Confirm $\Phi$, $\alpha_{h,H}$, $K_H$, residual constant, and the integer-jump convention.

2. **Correct the coefficient-sign issue.**
   Use

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

Recompute all M9 toy and moderate-scale tables from the raw definitions.

3. **Recompute R5 tables.**
   Avoid double division. Include first leg and shifted legs $\rho=1,3$ for square, near-square, nonsquare, and divisor-rich $X$ across $D\asymp X^{1/4},X^{3/8},X^{1/2}$. Normalize by $X^{1/4}$.

4. **Run M9 fixed-coefficient numerics.**
   Compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ with exact Vaaler coefficients. Compare fixed coefficients, arbitrary phase coefficients, and $L^1$ stress norms.

5. **Use high precision near Fejer spikes.**
   Avoid ordinary float-only sine evaluations near integer arguments. Use high precision or exact rational/modular checks.

6. **Complete the Li--Yang line audit.**
   Record exact labels and locations for the double sum $S$, Case A, Case B, main theorem, final $S/H$ target, allowed weights, and allowed $F$ hypotheses.

7. **Test M9b shifted-$F$.**
   Check derivative constants for

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
$$

and compare fractional-frequency toy matrices with unshifted matrices.

8. **Verify H13 constants and regimes.**
   Fix the convention, active sign, stationary point, leading phase, amplitude, $M_{\rm dual}\asymp hX/D^2$, $\Lambda\asymp hX/D$, nonstationary decay, support-boundary cases, and $M_{\rm dual}\asymp1$ transition.

9. **Implement Q1/BSOS tests.**
   Once A2 gives a finite signed statistic, compute signed, unsigned, absolute-majorant, and operator-norm comparators.

Exploratory allocation: run H13 signed-vs-unsigned matrix tests near $D\asymp X^{1/2}$ and report whether the dual character survives the first spacing step.

## Confidence

High confidence in the balanced hyperbola/Vaaler route as the current reduction framework.

High confidence that no new Gauss circle exponent was proved in Round 15.

High confidence that H1--H3 remain the correct arithmetic foundation.

Moderate-to-high confidence that H4 is source-located correctly in Vaaler; final proof-draft notation transcription remains necessary.

High confidence that R5-Full controls the Fejer residual at $X^{1/4+\epsilon}$ conditional on H4.

High confidence that M9 fixed-coefficient main sums remain open and are the active analytic bottleneck.

High confidence that $\alpha_{-h,H}=\overline{\alpha_{h,H}}$ is the correct conjugacy relation.

High confidence that black-box Li--Yang import fails at endpoint Vaaler height.

High confidence that Q1-Spectral is correct as a bounded operator-norm blindness diagnostic.

Moderate confidence that the shifted-$F$ formulation is the right M9b theorem-comparison form.

Moderate confidence that H13 deserves one more focused, falsifiable exploration near $D\asymp X^{1/2}$.

Low confidence that H13, BSOS/CRI, signed Fourier, Mellin--Perron, or current printed Li--Yang technology proves M9 without a genuinely new signed or endpoint-strength estimate.
