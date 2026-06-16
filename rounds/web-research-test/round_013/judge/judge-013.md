## Selected main route

Source anchors: Round 13 packet; Vaaler's periodic majorant theorem and Fejer residual framework are in *Some extremal functions in Fourier analysis*, especially Theorem 18 and the surrounding definitions of $j_N,k_N$ ; Li--Yang's arXiv page verifies the paper metadata, authors, v2 date, DOI, and abstract statement that the proof uses Bombieri--Iwaniec, a new first-spacing estimate, and Huxley's second-spacing results.

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

The Round 13 bridge remains:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is **not** a proof of the Gauss circle conjecture. H1--H3 are the accepted exact arithmetic reductions; H4 is now substantially source-located in Vaaler's periodic approximation theorems but still needs exact notation translation into the repo's convention; R5-Full is a proof-draft-level product-count residual bound conditional on H4; M9 remains open and is the active analytic bottleneck.

The proof should use the floor-compatible sawtooth

$$
\psi(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi(n)=-\frac12.
$$

The exact arithmetic input remains

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
y=\lfloor X^{1/2}\rfloor.
$$

For dyadic blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

use local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ should be handled trivially before invoking Vaaler, using $|\psi|\le 1/2$.

The official remaining target is M9 with actual Vaaler coefficients:

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

one may also write

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

The required endpoint-strength estimate is

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over dyadic $D$.

The fixed Fejer residual is no longer the central bottleneck. It is provisionally controlled by R5/R5-Full, conditional on H4 and complete dyadic bookkeeping. Arbitrary-coefficient residual targets H5r-B and H5r-L1 should remain stress tests only.

## Useful fragments by source

### From A1

A1's main contribution is the proof-infrastructure packet. The valuable claim is the conditional bridge

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

A1 also gives the clean R5 mechanism. The Fejer kernel is

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin \pi(H+1)t}{\sin \pi t}\right)^2,
$$

and

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right).
$$

Therefore

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg, choose $m$ nearest to $X/d$. For $d\asymp D$,

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

one gets

$$
\frac1H K_H(X/d)
\ll
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by $n=md$ and using $\tau(n)\ll_\epsilon n^\epsilon$ gives

$$
\frac1H\sum_{d\asymp D}K_H(X/d)
\ll
\sum_{n\asymp X}
\tau(n)
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The dyadic-tail justification is elementary: the central range $|X-n|\le \Delta$ contributes $O(\Delta X^\epsilon)$, and the dyadic annulus $2^{j-1}\Delta<|X-n|\le 2^j\Delta$ contributes $O(2^{-j}\Delta X^\epsilon)$.

For the second residual leg,

$$
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad \rho\in\{1,3\},
$$

near-integrality is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing

$$
\ell=4m-\rho,
\qquad
\ell\equiv-\rho\pmod4,
$$

again produces a product-counting problem. The congruence restriction only reduces divisor multiplicity.

A1's shifted-$F$ formulation of M9b is useful but should be recorded carefully. The identity

$$
e(hX/(4d))(e(h/4)-e(3h/4))
=
e\left(h\left(\frac{X}{4d}+\frac14\right)\right)
-
e\left(h\left(\frac{X}{4d}+\frac34\right)\right)
$$

rewrites M9b as two $h$-linear sums with phase functions

$$
F_{\rho,D}(z)=\frac{1}{4z}+\frac{\rho D}{4X},
\qquad \rho\in\{1,3\}.
$$

This is the preferred formulation for Li--Yang comparison because it avoids inserting a nonsmooth periodic $\chi_4(h)$ weight into the $h$-amplitude. However, theorem-level applicability is still open: one must verify that the intended Bombieri--Iwaniec/Li--Yang theorem permits this $D,X$-dependent constant shift uniformly.

### From A2

A2's strongest contribution is Q1-Spectral, a precise character-blindness diagnostic. On the odd denominator space

$$
\mathcal V_D=\ell^2(\mathcal D_{\rm odd}),
\qquad
\mathcal D_{\rm odd}=\{d:D\le d<2D,\ 2\nmid d\},
$$

define

$$
U=\operatorname{diag}(\chi_4(d)).
$$

Since $\chi_4(d)^2=1$ on odd $d$, $U$ is a diagonal unitary involution. Therefore for any matrix $K$,

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Thus an argument that first places $\chi_4(d)$ into a diagonal conjugation and then estimates by operator norm, spectral radius, Schur/Gershgorin, Frobenius norm, or absolute-value matrix cannot exploit the spatial character. This is a useful proved diagnostic, but only under its stated matrix-reduction hypotheses.

A2's trace observation is also correct in its restricted form:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This blocks pure conjugacy-invariant trace statistics from seeing the character. It does not block non-conjugacy signed forms, cross-residue statistics, open-path moments, or any method that estimates the signed form before passing to a unitarily invariant norm.

A2's H13 transform remains the serious exploratory fragment. Splitting M9a modulo $4$ and applying Poisson summation should give a dual Gauss factor

$$
e(n/4)-e(3n/4)=2i\chi_4(n),
$$

and a transform of schematic form

$$
\sum_d\chi_4(d)w_D(d)e(hX/d)
=
c\sum_n\chi_4(n)
\int w_D(u)e(hX/u-nu/4)\,du,
$$

with convention-dependent constant $c$. For the active sign, writing $n=-m$ gives dual length

$$
m\asymp \frac{hX}{D^2}.
$$

At maximal height $h\asymp H_D\asymp DX^{-1/4}$ and $D=X^\delta$,

$$
m\asymp X^{3/4-\delta},
\qquad
1/4\le\delta\le1/2.
$$

Thus H13 is roughly balanced only near $D\asymp X^{1/2}$ and lengthens the dual variable for smaller $D$. The leading phase is square-root type,

$$
\Phi(h,m)\asymp \sqrt{Xhm},
$$

and

$$
\det\nabla^2\Phi=0.
$$

So H13 is not a route to generic full-rank stationary phase or generic full-rank decoupling. It is an exploratory transform that needs a discrete signed spacing theorem after transformation.

A2's replacement of the old factorial-alignment heuristic by

$$
\#\{d\in[X^{1/4},X^{1/2}]:d\mid X\}
\le \tau(X)\ll_\epsilon X^\epsilon
$$

is correct and should be preserved. The earlier factorial obstruction should be removed.

A2's CRI statistic is not yet a lemma. It is a proposed signed statistic that needs a normalization, a derivation from M9, and a falsification test.

### From A3

A3's best contribution is audit discipline. A3 correctly keeps H4 source-normalization pending, R5 conditional on H4, and M9 open. A3 also correctly verifies the endpoint mismatch for Li--Yang's raw Case A/B restrictions and separates the C2/H13 dual length

$$
M_{\rm dual}\asymp \frac{kX}{D^2}
$$

from the stationary-phase large parameter

$$
\Lambda\asymp \frac{kX}{D}.
$$

A3's exact values of the Vaaler coefficient function are useful for numerical implementation:

$$
\Phi(1/2)=\frac12,
$$

$$
\Phi(1/4)=\frac{3\pi}{16}+\frac14,
$$

$$
\Phi(3/4)=-\frac{3\pi}{16}+\frac34.
$$

Thus $\Phi(1/4)\ne \Phi(3/4)$; M9 numerics must not assume symmetry.

A3's integer-jump check is correct. If the Vaaler polynomial vanishes at integer arguments and

$$
K_H(0)=H+1,
$$

then the residual majorant with coefficient $(2H+2)^{-1}$ gives

$$
\frac{K_H(0)}{2H+2}=\frac12,
$$

which exactly covers the discrepancy between the trigonometric midpoint value and the floor-compatible value $\psi(n)=-1/2$.

A3's Li--Yang audit is useful. Li--Yang define a double sum of the schematic form

$$
S=
\sum_{H\le h\le2H}g(h/H)
\sum_{M\le m\le2M}G(m/M)
e\left(\frac{hT}{M}F(m/M)\right),
$$

with bounded-variation weights and derivative/nondegeneracy hypotheses on $F$. The uploaded TeX audit records Case A, Case B, and the final circle/divisor reduction. At the raw endpoint block

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H=H_D\asymp X^{1/4},
$$

Case A gives

$$
H\le MT^{-49/164}=X^{33/164}<X^{1/4},
$$

and Case B gives

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}=X^{1/6}<X^{1/4}.
$$

Their final range also only reaches

$$
H\le MT^{-\theta^*},
\qquad
\theta^*=0.314483\ldots,
$$

not the endpoint

$$
H\le MT^{-1/4}.
$$

The arXiv page verifies that Li--Yang's paper is arXiv:2308.14859v2, by Xiaochun Li and Xuerui Yang, last revised 14 September 2023, and states the Bombieri--Iwaniec / first-spacing / second-spacing mechanism.

A3's weakness is execution: Round 13 still contains scripts and protocols, not numerical tables. The next round must run the tests or provide reproducible scripts with actual output.

## Rejected or risky ideas

1. **Reject any claim of a new exponent.**
Round 13 proves no estimate for M9, hence does not prove

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

2. **Reject treating R5-Full as unconditional before H4 is fully normalized.**
The product-count proof is sound conditional on the Vaaler residual theorem. The Vaaler source is now located more precisely in the periodic approximation section of Vaaler's paper, but the repo still needs a clean notation translation from $N,j_N,k_N$ to $H,\alpha_{h,H},K_H$.

3. **Reject H5r-B and H5r-L1 as active dependencies.**
The residual is controlled directly by the positive Fejer kernel and product counting. Arbitrary bounded coefficients and termwise $L^1$ residual norms are stress tests only.

4. **Reject black-box Li--Yang endpoint import.**
The phase class is structurally related, but the raw Case A/B and final $\theta^*$ restrictions do not reach the endpoint Vaaler height. This is a theorem-application guardrail, not a no-go theorem.

5. **Reject global no-go claims for Bombieri--Iwaniec, Li--Yang, or decoupling.**
Q1-Spectral only blocks arguments that reduce to diagonal-unitary conjugation followed by unitarily invariant norms or absolute-value matrices. It does not rule out all signed estimates or all decoupling formulations.

6. **Reject CRI as a proved escape.**
CRI is a proposed cross-residue statistic. It may avoid the literal $U^*KU$ conjugacy model, but no bound or reduction to M9 is supplied. A standard operator-norm bound on the off-diagonal block may still erase signs.

7. **Reject H13 as an endpoint estimate.**
H13 is a formal transform, not a sum bound. It preserves $\chi_4$ at the Poisson/Gauss-factor level, but the dual phase is Hessian-degenerate and direct differencing may collapse the dual character again.

8. **Reject the factorial-alignment obstruction.**
Exact alignments inside $[X^{1/4},X^{1/2}]$ are bounded by $\tau(X)\ll_\epsilon X^\epsilon$. They do not produce a dense obstruction.

9. **Reject unsafe float-only numerical tests near Fejer spikes.**
Evaluating $K_H(X/d)$ with ordinary floating-point sine near integer or near-integer arguments can create artificial blowups or miss exact resonances. R5 and M9 numerical tests should use high precision or exact modular/rational handling for resonance checks.

10. **Reject the textual claim $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$.**
With the coefficient convention above,

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

Numerical code that uses the conjugate may still be correct, but the proof text must be fixed.

11. **Reject treating M9b as automatically covered by M9a.**
The shifted-$F$ representation is preferable, but theorem-level applicability still has to be checked. The fractional-frequency representation

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\},
$$

and the shifted-$F$ representation are algebraically related but have different theorem-hypothesis risks.

12. **Reject pivoting to Mellin--Perron or signed Fourier as the main route.**
Both remain comparison modules. Neither currently replaces M9.

## Known gaps

1. **H4 notation translation.**
Vaaler's Theorem 18 states the periodic approximation and residual bound

$$
|\psi*j_N(x)-\psi(x)|\le (2N+2)^{-1}k_N(x),
$$

and Theorem 6 gives the Fourier transform coefficient shape for $J$. This strongly supports H4. The repo still needs to translate Vaaler's $N,j_N,k_N,\widehat J_{N+1}(n)$ notation into

$$
\psi(t)=\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H(t),
\qquad
|R_H(t)|\le (2H+2)^{-1}K_H(t),
$$

with exact conventions.

2. **H4 floor-compatible conversion.**
Vaaler's periodic $\psi$ is the centered sawtooth. The proof draft must explicitly state why the floor-compatible convention $\psi(n)=-1/2$ is covered by the residual majorant at integer points.

3. **R5-Full write-up details.**
The proof must include nearest-integer tie rules, real and integer $X$, second-leg congruences $\ell=4m-\rho$, positivity/size of $\ell$, zero mode, both frequency signs, dyadic weights, bounded overlap, short blocks, and logarithmic losses.

4. **M9 remains open.**
No endpoint proof is supplied for $\mathcal M_1(D;X)$ or $\mathcal M_2(D;X)$.

5. **M9b theorem-extension gap.**
The shifted functions

$$
F_{\rho,D}(z)=\frac{1}{4z}+\frac{\rho D}{4X}
$$

have the same derivative nondegeneracy as $1/(4z)$, but Li--Yang applicability with this $D,X$-dependent constant shift must be checked line by line. If using the fractional-frequency representation instead, the theorem must handle $q+\beta$ with $\beta\in\{1/4,3/4\}$.

6. **Li--Yang subrange map incomplete.**
The endpoint block fails. The repo still needs a full $(D,H)$ map showing which subranges are covered by existing estimates and which remain in the high-frequency gap.

7. **Character-preserving spacing gap.**
Q1-Spectral tells us what fails. The repo still lacks an actual signed spacing inequality that keeps $\chi_4$ or the fixed Vaaler coefficients alive long enough to gain cancellation.

8. **H13-SPU uniform transform gap.**
H13 needs exact constants, signs, active dual sign, stationary phase, amplitude, nonstationary integration by parts, boundary stationary points, and short-dual-length regimes. It then needs a summation theorem; stationary phase of one integral is not enough.

9. **CRI normalization gap.**
CRI must state the exact bilinear/moment it controls, the target scale needed to imply M9, and a falsification test. As written, it is only a proposed statistic.

10. **Numerical evidence gap.**
A3 supplied plans and code sketches but not executed tables. Round 14 should produce actual R5/M9 values.

11. **Numerical robustness gap.**
Fejer and M9 tests must use exact or high-precision phase evaluation near rational resonances. The code must handle $H_D\ge1$, short-block exclusion, negative frequencies, and the correct $\alpha_{-h,H}$ relation.

12. **Dyadic-weight specification.**
The proof draft must define the dyadic partition $w_D$, its bounded overlap, and how signed weights are replaced by $|w_D|$ only in the positive residual estimate.

## New lemmas to add

### H4-R13. Vaaler periodic finite approximation with Fejer residual

**Status:** external theorem now source-located; repo-normalization still pending.

Vaaler's Theorem 18 gives a trigonometric polynomial approximation to the periodic sawtooth with residual bounded by a Fejer-type kernel:

$$
|\psi*j_N(x)-\psi(x)|\le (2N+2)^{-1}k_N(x).
$$

Together with the Fourier coefficient formula for $J$,

$$
\widehat J(t)=\pi t(1-|t|)\cot(\pi t)+|t|
\qquad (0<|t|<1),
$$

this supports the repo form

$$
\psi(t)
=
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

The next draft must explicitly map $N$ to $H$ and $k_N$ to $K_H$.

### R5-R13. Fejer product-count residual bound

**Status:** proved conditional on H4.

For $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp D X^{-1/4}$, and $|w_D|\le1$ supported on $d\asymp D$,

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

### R5-Full-R13. Total Vaaler residual bound

**Status:** conditional bridge lemma.

Assuming H4-R13 and R5-R13 for every dyadic block, all Vaaler residuals arising from H3 contribute

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Short blocks $D<X^{1/4}$ are handled trivially.

### Bridge-R13. Conditional endpoint reduction

**Status:** proved conditional theorem.

If H1--H3, H4-R13, R5-Full-R13, and M9 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-R13. Fixed-coefficient main-term criterion

**Status:** official remaining open target.

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

### M9b-ShiftedF-R13

**Status:** open theorem-extension target; preferred formulation.

For $\rho\in\{1,3\}$ define

$$
F_{\rho,D}(z)=\frac{1}{4z}+\frac{\rho D}{4X}.
$$

Then

$$
\frac{hX}{D}F_{\rho,D}(d/D)
=
h\left(\frac{X}{4d}+\frac{\rho}{4}\right).
$$

Thus M9b can be treated as the difference of two reciprocal sums with shifted phase functions. The derivative determinant remains

$$
F'F'''-3(F'')^2=-\frac{3}{8}z^{-6},
$$

but theorem-level applicability remains open.

### M9b-FractionalFrequency-R13

**Status:** equivalent stress formulation; theorem gap.

Splitting $h=4q+r$, $r\in\{1,3\}$, yields phases

$$
e((q+r/4)X/d).
$$

This formulation is useful for numerical testing and for checking whether spacing matrices are invariant under fixed fractional shifts.

### Alpha-Conjugacy-R13

**Status:** correction lemma.

With

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

one has

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

Numerical and algebraic reductions over positive $h$ must use this relation.

### LY-Raw-Mismatch-R13

**Status:** proved theorem-application guardrail.

For

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$

Li--Yang Case A allows only

$$
H\le X^{33/164},
$$

and Case B gives

$$
H\le X^{23/138}=X^{1/6}.
$$

Both are below $X^{1/4}$. Therefore their raw theorem cannot be imported for the endpoint Vaaler block.

### LY-FinalGap-R13

**Status:** diagnostic.

Li--Yang's final circle/divisor reduction reaches

$$
H\le MT^{-\theta^*},
\qquad
\theta^*=0.314483\ldots,
$$

whereas the Vaaler endpoint requires

$$
H\le MT^{-1/4}.
$$

At $D=M=X^{1/2}$, the gap is roughly

$$
X^{0.1855\ldots}\lesssim H\lesssim X^{1/4}.
$$

### Q1-Spectral-R13

**Status:** proved diagnostic with restricted hypotheses.

If the spatial character enters only as a diagonal unitary conjugation

$$
K\mapsto U^*KU,
\qquad
U=\operatorname{diag}(\chi_4(d)),
$$

then operator-norm-only or absolute-value matrix estimates cannot exploit the character:

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

### H12-Trace-R13

**Status:** proved diagnostic with restricted hypotheses.

For pure conjugacy-invariant traces,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This blocks only pure conjugacy-cycle statistics, not all signed statistics.

### H13-R13. B-process-first M9a transform

**Status:** formal transform / exploratory target.

Modulo-$4$ Poisson summation for M9a should produce a dual $\chi_4$ factor and dual length

$$
m\asymp \frac{hX}{D^2}.
$$

At maximal height and $D=X^\delta$,

$$
m\asymp X^{3/4-\delta}.
$$

The leading phase is $\sqrt{Xhm}$ and has zero Hessian determinant. H13 needs a uniform transform and a signed spacing theorem before it becomes useful for M9.

### CRI-R13. Cross-residue interference statistic

**Status:** proposed falsification object, not a lemma.

Split

$$
S_\chi(h,D)=S_1(h,D)-S_3(h,D),
$$

where $S_r$ sums over $d\equiv r\pmod4$. A possible statistic is a cross-residue bilinear form involving $S_1\overline{S_3}$. It must be normalized and shown to imply a bound for M9 before promotion.

### D-Align-R13

**Status:** proved elementary guardrail.

Exact divisibility alignments in the critical interval satisfy

$$
\#\{d\in[X^{1/4},X^{1/2}]:d\mid X\}
\le \tau(X)\ll_\epsilon X^\epsilon.
$$

## Counterexample checks to run

1. **H4 source-normalization check.**
Extract from Vaaler the exact definitions of $\psi$, $j_N$, $k_N$, $\widehat J$, and the residual inequality. Map them to $H,\alpha_{h,H},K_H$.

2. **H4 integer-jump test.**
Check directly that the Vaaler polynomial vanishes at integer arguments and that

$$
\frac{K_H(0)}{2H+2}=\frac12
$$

covers $|\psi(n)|=1/2$.

3. **R5 first-leg stress test.**
Compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

for square, nonsquare, near-square, and divisor-rich $X$.

4. **R5 shifted-leg stress test.**
For $\rho\in\{1,3\}$ compute

$$
\frac1{H_D}
\sum_{d\asymp D}K_{H_D}\left(\frac{X/d+\rho}{4}\right).
$$

5. **R5 nearest-integer tie check.**
Test cases where $X/d$ or $(X/d+\rho)/4$ lies exactly halfway between integers. Fix a deterministic tie rule and verify the divisor-count proof remains valid.

6. **Short-block check.**
Verify that blocks $D<X^{1/4}$ are removed before Vaaler is invoked and contribute $O(X^{1/4})$ up to logarithms.

7. **M9 fixed-coefficient numerics.**
Compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ with exact $\alpha_{h,H_D}$ and report

$$
|\mathcal M_i(D;X)|/X^{1/4}.
$$

8. **M9 stress comparison.**
Compare fixed coefficients with arbitrary phase coefficients and dyadic $L^1$ stress norms.

9. **Coefficient-conjugacy test.**
Verify numerically and symbolically that positive/negative frequency recombination uses

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

10. **High-precision Fejer test.**
Evaluate Fejer kernels near exact resonances using high precision or exact modular arithmetic, not ordinary float-only sine calls.

11. **M9b shifted-$F$ theorem audit.**
Check whether the relevant Li--Yang theorem allows

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

uniformly in $D,X$ and whether all constants in derivative hypotheses remain admissible.

12. **M9b fractional-frequency matrix test.**
Compare matrices with phases

$$
e(qX/d),\qquad e((q+\beta)X/d),
\qquad \beta\in\{1/4,3/4\}.
$$

Check whether operator norms are merely diagonal-unitary conjugates, and whether any signed statistic changes.

13. **Q1-Spectral matrix test.**
Construct the actual Gram matrix arising after a Cauchy--Schwarz step on M9a and verify whether the character enters only as $U^*KU$.

14. **CRI falsification test.**
Compute the signed cross-residue statistic and compare it to the absolute majorant and to an operator-norm bound.

15. **H13 transform test.**
Derive exact constants and signs in the modulo-$4$ Poisson transform under $e(t)=e^{2\pi it}$.

16. **H13-SPU test.**
Prove or numerically test stationary, nonstationary, support-boundary, and $m\asymp1$ regimes for

$$
I(\xi)=\int w_D(u)e(hX/u-\xi u/4)\,du.
$$

17. **Li--Yang line audit.**
Record exact source labels and line numbers for the definition of $S$, Case A, Case B, the main theorem, and the final $S/H$ reduction.

18. **Mellin--Perron and signed Fourier comparison.**
Keep these as comparison modules only. Test whether their replacement errors reduce to M9-like or Fejer/product-count structures.

## Research strategy adjustment

Round 13 should be recorded as a proof-infrastructure and diagnostic round. No exponent improvement has been proved.

The residual side is provisionally controlled: R5 product-counting removes the fixed Fejer residual from the critical path, conditional on the Vaaler theorem and careful dyadic bookkeeping. The active mathematical bottleneck is now M9, with the exact Vaaler coefficients and the character placements preserved.

The next round should not expand the number of speculative routes. It should do three narrow things:

1. **Finish the proof infrastructure.**
Source-normalize H4 from Vaaler, write R5-Full as a complete lemma, and insert the bridge theorem into the best proof draft.

2. **Audit M9 against known technology.**
Use the shifted-$F$ M9b formulation and the original M9a formulation to create a theorem-level Li--Yang/Bombieri--Iwaniec map. Distinguish raw Case A/B restrictions, final $\theta^*$ restrictions, low-height ranges, and the uncovered endpoint range.

3. **Test sign-preserving possibilities before over-investing.**
Q1-Spectral should be used as a filter: any proposed signed method that immediately becomes an operator norm or absolute-value matrix should be deprioritized. H13 and CRI receive one more round of focused, falsifiable development.

A2 and A3 should be assessed separately:

- A2 contributed strong formula-level diagnostics, especially Q1-Spectral, H12, D-Align, and H13. The weakness is overpromotion of CRI/C3/open-path ideas before estimates exist. A2 should now produce proof-draft-ready, bounded-scope diagnostics and one falsifiable signed statistic.
- A3 contributed useful verification discipline, especially $\Phi$ values, Li--Yang endpoint mismatch, and scale separation in C2/H13. The weakness is that computations were not executed and some code/text details need correction. A3 should now produce actual tables and exact source-line audits.

## Next-round prompts by agent

### For A1

Write the proof-infrastructure update for Round 14.

Objectives:

1. **Source-normalize H4 from Vaaler.**
   Extract the exact page/theorem/equation data from Vaaler's paper. Translate Vaaler's notation into the repo notation:
   - Vaaler's periodic $\psi$ versus the repo's floor-compatible $\psi(t)=t-\lfloor t\rfloor-\frac12$;
   - $j_N,k_N$ versus the repo's Vaaler polynomial and $K_H$;
   - $\widehat J_{N+1}(h)$ versus $\Phi(|h|/(H+1))$;
   - the sign of $\alpha_{h,H}$;
   - the residual constant $(2H+2)^{-1}$;
   - the integer-discontinuity convention.

2. **Write R5-Full as a complete proof.**
   Include:
   - first leg $K_H(X/d)$;
   - shifted legs $K_H((X/d+\rho)/4)$ for $\rho=1,3$;
   - real $X$, integer $X$, and near-integer $X$;
   - nearest-integer tie rules;
   - the congruence $\ell=4m-\rho$ and admissible signs/sizes of $\ell$;
   - dyadic weights and bounded overlap;
   - zero mode and nonzero Fejer modes;
   - both frequency signs;
   - short blocks $D<X^{1/4}$;
   - the dyadic-tail proof for $\sum_n\tau(n)\min(1,\Delta^2/|X-n|^2)$;
   - logarithmic losses absorbed into $X^\epsilon$.

3. **Insert the bridge theorem into the proof draft.**
   State and prove:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

4. **Freeze M9 as the official target.**
   Use the exact $\alpha_{h,H_D}$ coefficients only. Put arbitrary-coefficient variants in a stress-test appendix.

5. **Write the M9b theorem-extension problem precisely.**
   Compare three formulations:
   - shifted phase functions $F_{\rho,D}(z)=1/(4z)+\rho D/(4X)$;
   - fractional-frequency phases $e((q+\beta)X/d)$;
   - periodic $h$-weights $\chi_4(h)$.

   Decide which formulation is official for theorem comparison and which remain stress formulations.

6. **Produce a Li--Yang subrange map.**
   Use exact conditions from the TeX source. Table the covered and uncovered regions for $D=X^\delta$ and $H=X^\eta$, distinguishing:
   - raw Case A;
   - raw Case B;
   - final $\theta^*$ reduction;
   - low-height fallback estimates;
   - the endpoint region needed for M9.

Exploratory allocation: add a short H13 falsification checklist. State exactly which first spacing, Cauchy--Schwarz, or norm step would make H13 character-blind.

### For A2

Produce a conservative signed-method diagnostics packet. Avoid route-closing language.

Objectives:

1. **Rewrite Q1-Spectral with exact hypotheses.**
   Specify:
   - the finite index set;
   - the Gram matrix context, especially if it arises after Cauchy--Schwarz over $h$;
   - the diagonal unitary $U=\operatorname{diag}(\chi_4(d))$;
   - the proof of $\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}$;
   - the exact methods blocked;
   - the signed-form methods not blocked.

2. **Rewrite H12 trace material narrowly.**
   Prove only

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m)
$$

for pure conjugacy-invariant traces. Do not describe it as a global obstruction.

3. **Repair C3 parity diagnostics.**
   State exact lattice hypotheses. Separate:
   - translation shifts;
   - odd dilations;
   - even dilations;
   - cases where the parity function is not defined on the image lattice.

   Connect each statement to M9 or H13, or label it diagnostic only.

4. **Make CRI falsifiable.**
   Define one cross-residue statistic with:
   - exact normalization;
   - the M9 quantity it is meant to control;
   - the target bound required;
   - an absolute-majorant comparator;
   - a numerical falsification test.

   Do not mark CRI as a lemma unless a proof is supplied.

5. **Develop H13 one step beyond the formal transform.**
   State:
   - exact modulo-$4$ Poisson transform;
   - dual Gauss factor;
   - stationary phase and amplitude;
   - dual length $m\asymp hX/D^2$;
   - range table for $D=X^\delta$;
   - Hessian degeneracy;
   - the first post-transform spacing or Cauchy step.

   The key deliverable is to decide whether that first post-transform step preserves $\chi_4(m)$ or collapses to Q1-Spectral.

Exploratory allocation: propose one non-operator-norm signed statistic and give a falsification test. If it cannot be tied to M9, mark it as a toy model only.

### For A3

Execute verification and computation tasks. Provide tables or reproducible scripts with output.

Objectives:

1. **H4 source audit.**
   Extract the precise Vaaler statement:
   - page and theorem/equation numbers;
   - definitions of $j_N,k_N$;
   - formula for $\widehat J$;
   - coefficient formula and sign;
   - residual bound;
   - convention at discontinuities.

   Verify the mapping to

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h}
$$

and

$$
|R_H(t)|\le (2H+2)^{-1}K_H(t).
$$

2. **Correct coefficient handling.**
   Explicitly verify

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

and implement negative frequencies accordingly.

3. **Run R5 numerical stress tests.**
   Include:
   - first leg;
   - shifted second legs $\rho=1,3$;
   - square, near-square, nonsquare, and divisor-rich $X$;
   - $D=X^{1/4},X^{3/8},X^{1/2}$ where feasible;
   - normalized values divided by $X^{1/4}$.

4. **Use high precision or exact resonance handling.**
   Do not rely on ordinary float-only sine evaluation near Fejer spikes. Use high precision, modular arithmetic, or exact special-case detection for integer arguments.

5. **Run M9 fixed-coefficient numerics.**
   Compute

$$
\mathcal M_1(D;X),\qquad \mathcal M_2(D;X)
$$

with actual $\alpha_{h,H_D}$ and report

$$
|\mathcal M_i(D;X)|/X^{1/4}.
$$

Also compare with arbitrary-coefficient and $L^1$ stress norms.

6. **Audit Li--Yang line by line.**
   Give exact source labels and line references for:
   - definition of $S$;
   - hypotheses on $F,g,G$;
   - Case A;
   - Case B;
   - main theorem;
   - final $S/H$ reduction;
   - final $H\le MT^{-\theta^*}$ range.

   Then test the shifted-$F$ M9b formulation against the actual hypotheses.

7. **Run Q1-Spectral and CRI toy tests.**
   Construct a small M9a Gram matrix, verify unitary invariance of the operator norm, and compare any proposed signed statistic with its absolute majorant.

8. **Complete C2/H13-SPU as a transform lemma.**
   State uniform bounds for

$$
I(\xi)=\int w_D(u)e(hX/u-\xi u/4)\,du
$$

in stationary, nonstationary, support-boundary, and short-dual-length regimes. Keep rapid integration-by-parts decay distinct from exponential decay.

Exploratory allocation: implement a small H13 transformed matrix near $D=X^{1/2}$ and test whether the dual $\chi_4(m)$ changes the signed quadratic form before norm extraction.

## Confidence

High confidence:

- The balanced hyperbola/Vaaler framework remains the correct reduction and diagnostic route.
- No new Gauss circle exponent has been proved.
- R5 product-counting controls the fixed Fejer residual conditional on the Vaaler theorem.
- H5r-B and H5r-L1 are overstrong stress tests, not active dependencies.
- M9 fixed-coefficient main sums are the official remaining bottleneck.
- Li--Yang cannot be imported as a black box for the raw endpoint Vaaler block.
- Q1-Spectral is a valid restricted diagnostic for operator-norm-only methods.

Moderate confidence:

- The H4 formula used in the repo matches Vaaler's Theorem 18 plus Theorem 6 after notation translation.
- R5-Full will survive a complete proof-draft write-up with all edge cases.
- The shifted-$F$ formulation is the best current M9b representation for theorem comparison.
- H13 is worth one focused exploratory round, especially near $D\asymp X^{1/2}$.

Low confidence:

- Existing printed Bombieri--Iwaniec/Li--Yang technology proves M9 at the endpoint.
- CRI or open-path statistics provide a usable endpoint saving without a new signed estimate.
- H13 gives an endpoint estimate after stationary phase; the dual phase is Hessian-degenerate and the first spacing step may still erase signs.
- Mellin--Perron or signed Fourier currently bypass M9.

Overall Round 13 judgment: useful proof-infrastructure progress. The Vaaler residual is provisionally under control, the exact M9 bottleneck is sharper, H4 has been source-located but still needs notation normalization, and the next round should prioritize executed verification plus one tightly scoped sign-preserving exploration.