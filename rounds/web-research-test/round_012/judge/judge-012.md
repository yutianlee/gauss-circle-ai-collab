## Selected main route

Source basis: Round 12 prompt, Stage A outputs, and Stage B reviews are in the uploaded judge packet. External literature metadata and claims were checked separately: Vaaler's paper metadata is verified as Jeffrey D. Vaaler, "Some extremal functions in Fourier analysis," *Bull. Amer. Math. Soc.* 12(2), 183--216, 1985. Li--Yang's arXiv paper states the theorem-level exponent $\theta^*=0.314483\ldots$ for both the circle and divisor problems, and the abstract says the proof uses the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley's second-spacing results.

Keep the balanced arithmetic hyperbola/Vaaler route as the selected main route:

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{fixed-coefficient reciprocal main sums}.
$$

The current proof-infrastructure reduction is:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is not a proof of the conjectural bound, because M9 remains open. The correct Round 12 status is:

- H1--H3: proved floor-compatible arithmetic reductions from earlier rounds.
- H4: external Vaaler theorem dependency; coefficient and residual formula are very likely correct, but page/theorem normalization still needs a source-level check.
- R5/R5-Full: product-count residual bound; mathematically sound conditional on H4, but still needs a complete proof-draft write-up.
- M9: official remaining analytic bottleneck.

The finite Vaaler main terms should now be frozen with the actual coefficients

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1.
$$

For each dyadic block $d\asymp D$ with

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4},
$$

the remaining M9 targets are:

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_d
\chi_4(d)w_D(d)e(hX/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_d
w_D(d)e(hX/(4d))
\ll_\epsilon X^{1/4+\epsilon}.
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the second target is equivalently

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_d
w_D(d)e(hX/(4d)).
$$

The fixed Fejer residual should no longer be treated as the central bottleneck. It is provisionally cleared by R5, conditional on H4 and full dyadic bookkeeping. Arbitrary-coefficient H5a/H5b and H5r-B/H5r-L1 remain stress tests only.

## Useful fragments by source

### From A1

A1 supplied the strongest proof-infrastructure packet.

The most valuable contribution is the complete R5 product-count mechanism. The Fejer kernel is

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(\frac{\sin \pi(H+1)t}{\sin \pi t}\right)^2,
$$

with pointwise bound

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right),
$$

hence

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
\frac{|X-md|}{D},
\qquad d\asymp D.
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

Grouping by $n=md$ gives multiplicity at most $\tau(n)$, and therefore

$$
\frac1H\sum_{d\asymp D}K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the shifted second leg,

$$
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad \rho\in\{1,3\},
$$

near-integrality becomes

$$
X\approx d(4m-\rho).
$$

Writing

$$
\ell=4m-\rho,
\qquad
\ell\equiv-\rho\pmod 4,
$$

again gives a product-count problem with at most divisor-function multiplicity. This is the key reason R5 should be accepted as the residual-control mechanism once H4 is verified.

A1 also correctly isolates M9b as a shifted-frequency theorem-extension problem. Splitting $h=4q+r$, $r\in\{1,3\}$, gives

$$
\chi_4(4q+r)e((4q+r)X/(4d))
=
\chi_4(r)e((q+r/4)X/d).
$$

Thus M9b is not automatically the same theorem as M9a. It requires either an arithmetic-progression-in-$h$ theorem or a fixed fractional-frequency theorem for phases

$$
e((q+\beta)X/d),
\qquad
\beta\in\left\{\frac14,\frac34\right\}.
$$

A1's Li--Yang audit is also useful. Li--Yang's paper defines the problem with $R(X)$ and $\Delta(X)$ and states the conjectural lower endpoint $\theta=1/4$; it proves $\theta^*=0.314483\ldots$ instead. Their Case A and Case B height restrictions include $H\le MT^{-49/164}$ and $H\le \min(M^{35/69}T^{-2/23},B_0M^{3/2}T^{-1/2})$, respectively. Their final reduction asks for $S/H\lesssim_\epsilon T^{\theta^*+\epsilon}$ and restricts $H\le MT^{-\theta^*}$, not the endpoint $H\le MT^{-1/4}$.

### From A2

A2's best contribution is Q1-Spectral, a precise operator-norm character-blindness diagnostic.

Let

$$
\mathcal D_{\rm odd}=\{d:D\le d<2D,\ 2\nmid d\},
\qquad
\mathcal V_D=\ell^2(\mathcal D_{\rm odd}),
$$

and define

$$
U_{d_1,d_2}=\delta_{d_1,d_2}\chi_4(d_1).
$$

On odd denominators, $\chi_4(d)^2=1$, so $U$ is a diagonal unitary involution. Therefore, for any matrix $K$,

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

This proves that operator-norm-only, spectral-radius-only, Schur/Gershgorin, Frobenius, and absolute-value matrix arguments cannot exploit $\chi_4(d)$ if the character enters only by diagonal unitary conjugation. This is a proved diagnostic with restricted scope, not a no-go theorem.

A2's trace-cycle observation is also correct in its restricted form:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This blocks pure conjugacy-invariant trace statistics from seeing the character, but does not block non-conjugacy signed forms, open-path statistics, cross-residue moments, or a bilinear estimate that keeps signs before norm extraction.

A2's H13 B-process-first transform is the serious exploratory fragment. Splitting the spatial-character M9a sum modulo $4$ and applying Poisson should produce a dual Gauss factor, hence a dual $\chi_4$ factor, with stationary length

$$
m\asymp \frac{hX}{D^2}.
$$

At maximal Vaaler height $h\asymp H_D\asymp DX^{-1/4}$ and $D=X^\delta$, this becomes

$$
m\asymp X^{3/4-\delta},
\qquad
1/4\le\delta\le 1/2.
$$

Thus the transform is roughly balanced only near $D\asymp X^{1/2}$. For smaller $D$, it lengthens the dual variable. The resulting leading phase is of square-root type,

$$
\Phi(h,m)\asymp \sqrt{Xhm},
$$

and

$$
\det\nabla^2\Phi=0.
$$

Therefore H13 is not a route to generic full-rank stationary phase or generic full-rank decoupling. It remains a possible sign-preserving transform requiring a discrete spacing theorem.

A2's weaker parts are also important to flag. The Cross-Residue Interference statistic is only a proposed object; no estimate is supplied. Some C3-Affine/Rational statements remain stylized parity diagnostics unless connected to actual M9/H13 variables. The factorial-alignment example should be removed or replaced by the divisor-bound statement

$$
\#\{d\in[X^{1/4},X^{1/2}]:d\mid X\}\le \tau(X)\ll_\epsilon X^\epsilon.
$$

### From A3

A3 gave the strongest audit and verification packet.

The most useful concrete checks are the special values of $\Phi$:

$$
\Phi(1/2)=\frac12,
$$

$$
\Phi(1/4)=\frac{3\pi}{16}+\frac14,
$$

and

$$
\Phi(3/4)=-\frac{3\pi}{16}+\frac34.
$$

Thus $\Phi(1/4)\ne \Phi(3/4)$, and numerical implementations of M9 must not assume symmetry between these coefficient values.

A3 also correctly checks the integer-discontinuity convention. At an integer $n$,

$$
\psi(n)=-\frac12,
$$

whereas the centered Vaaler polynomial satisfies $V_H(n)=0$. Since

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12,
$$

the residual majorant exactly covers the floor-compatible half-jump. This should be placed in the proof draft because it prevents a common endpoint-convention error.

A3's Li--Yang audit usefully confirms that black-box theorem import fails at the raw endpoint block. With

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H=H_D\asymp X^{1/4},
$$

Case A gives

$$
H\le MT^{-49/164}=X^{33/164},
$$

and Case B gives

$$
H\le M^{35/69}T^{-2/23}=X^{23/138},
$$

both below $X^{1/4}$. This is a theorem-application guardrail, not a proof that all Bombieri--Iwaniec methods fail.

A3's C2/H13 stationary-phase bookkeeping is useful but not complete. For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

the active sign is $\xi<0$. Writing $\xi=-m$ gives

$$
u_0=\sqrt{\frac{kX}{m}},
\qquad
\phi(u_0)=2\sqrt{kXm},
\qquad
\phi''(u_0)=\frac{2m}{u_0}.
$$

The dual length is

$$
M_{\rm dual}\asymp \frac{kX}{D^2},
$$

while the large stationary-phase parameter after scaling is

$$
\Lambda\asymp \frac{kX}{D}.
$$

These two scales must remain distinct. A3 is right that smooth nonanalytic weights give rapid integration-by-parts decay, not exponential decay. However, the uniform boundary and transition estimates are not yet proved.

A3's proposed numerical protocols are valuable, but no actual data have yet been committed. Round 13 must produce tables or scripts.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.**
Round 12 gives proof infrastructure, diagnostics, and theorem-audit improvements. It does not prove M9.

2. **Reject treating H4 as fully source-normalized.**
The Vaaler coefficient formula and residual constant are plausible and internally consistent, but the repo still lacks a page-level theorem citation. The Vaaler paper metadata is verified, but exact theorem normalization is still a dependency.

3. **Reject arbitrary-coefficient H5a/H5b as the active target.**
The active target is M9 with actual Vaaler coefficients $\alpha_{h,H_D}$. Arbitrary bounded coefficients and $L^1$ variants are stress tests only.

4. **Reject H5r-B/H5r-L1 as active dependencies.**
R5 controls the positive Fejer residual directly. H5r-B and H5r-L1 are now diagnostic comparisons only.

5. **Reject black-box Li--Yang endpoint import.**
Li--Yang's theorem is structurally relevant but does not cover $H\asymp MT^{-1/4}$ at the raw Vaaler endpoint. The printed Case A/B ranges and final $S/H$ target stop short of the conjectural endpoint.

6. **Reject global no-go statements about Bombieri--Iwaniec or spacing methods.**
The raw theorem mismatch is proved. A new signed spacing estimate, a different dissection, or a theorem adapted to fixed Vaaler coefficients is not ruled out.

7. **Reject absorbing $\chi_4(h)$ into a bounded-variation weight without proof.**
A periodic weight $\chi_4(h)$ has total variation $\asymp H$ on an interval of length $H$. Unless the theorem explicitly allows this, M9b must be handled by residue splitting or a fractional-frequency extension.

8. **Reject treating Q1-Spectral as a universal obstruction.**
It only blocks methods that pass through diagonal-unitary-invariant operator norms or absolute-value matrices. It does not block signed bilinear estimates or non-conjugacy statistics.

9. **Reject treating H13 as an estimate.**
H13 is a transform plus a phase-geometry diagnostic. It gives no endpoint bound without a summation theorem for the dual square-root phase and character.

10. **Reject C2-SPU as proved.**
The leading stationary phase is credible, but uniform estimates across stationary, nonstationary, boundary, and $M_{\rm dual}\asymp1$ regimes are still missing.

11. **Reject the factorial-alignment example.**
The relevant obstruction is simply bounded by divisor multiplicity in the dyadic window; PNT in arithmetic progressions is unnecessary for $\chi_4$, whose interval sums are elementary periodic sums.

12. **Reject pivoting to Mellin--Perron or signed Fourier as the main route.**
They remain comparison modules. Neither currently supplies a better replacement for M9.

## Known gaps

1. **H4 source-normalization gap.**
Need an exact page/theorem citation and notation match for the finite Vaaler approximation, including $\Phi$, the sign of $\alpha_{h,H}$, the normalization of $K_H$, and the residual constant.

2. **R5-Full proof-draft gap.**
Need a complete proof covering first leg, both shifted second legs, real and integer $X$, tie-breaking for nearest integer choices, dyadic weights, dyadic overlaps, zero Fejer mode, both signs of $k$, short blocks $D<X^{1/4}$, and small-$X$ endpoint cases.

3. **M9 main-term gap.**
No agent proved

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is the central analytic bottleneck.

4. **M9b fractional-frequency gap.**
After $h=4q+r$,

$$
e(hX/(4d))=e((q+r/4)X/d).
$$

A theorem must handle fixed fractional frequencies $\beta\in\{1/4,3/4\}$ or arithmetic progressions in $h$ without uncontrolled BV loss.

5. **Li--Yang subrange map gap.**
The raw endpoint block fails. The repo still needs an exact map of which $D,H$ subranges are covered by existing Li--Yang technology and which portion of

$$
MT^{-\theta^*}<H\le MT^{-1/4}
$$

remains uncovered.

6. **Signed spacing gap.**
Q1-Spectral explains why operator norms fail to see $\chi_4$. The repo still lacks a signed-form estimate that preserves $\chi_4(d_1)\chi_4(d_2)$ or $\chi_4(h)$ through a useful inequality.

7. **H13 uniform transform gap.**
Need exact Poisson normalization modulo $4$, dual Gauss factor, leading amplitude, nonstationary integration-by-parts estimates, boundary terms, and a range table for all $D=X^\delta$, $1/4\le\delta\le1/2$.

8. **H13 summation gap.**
Even after stationary phase, the dual phase $\sqrt{Xhm}$ is Hessian-degenerate. A discrete spacing theorem or signed bilinear estimate is needed; generic full-rank tools are unavailable.

9. **A2 cross-residue statistic gap.**
The proposed statistic is not yet a lemma. It needs a precise finite matrix, normalization, a bound to be proved, and a falsification test.

10. **C3 relevance gap.**
C3-Affine/Rational parity-collapse claims must be tied to actual M9 or H13 variables before being treated as more than diagnostics.

11. **Numerical evidence gap.**
Round 12 still provides protocols rather than data. The repo needs actual R5 and M9 tables.

12. **Poisson--Bessel calibration gap.**
The calibration route remains useful for normalization and $R^{2/3}$ sanity checks, but it was not advanced in Round 12.

## New lemmas to add

### H4. Vaaler finite approximation with Fejer residual

**Status:** external theorem dependency; internally consistent, source-normalization pending.

For $H\ge1$,

$$
\psi(t)=V_H(t)+R_H(t),
$$

where

$$
V_H(t)=
\sum_{1\le |h|\le H}
\alpha_{h,H}e(ht),
$$

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u.
$$

The desired residual majorant is

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t),
$$

where

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

At integers, $V_H(n)=0$ and $K_H(0)/(2H+2)=1/2$, so the residual covers the floor-compatible value $\psi(n)=-1/2$.

### R5. Fejer product-count residual bound

**Status:** proved conditional on H4.

For $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp DX^{-1/4}$, and $|w_D|\le1$ supported on $d\asymp D$,

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

### R5-Full. Total Vaaler residual bound

**Status:** conditional bridge lemma; proof-draft write-up still required.

Assuming H4 and R5 on all dyadic long blocks, all Vaaler residual contributions arising from H3 are

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Short blocks $D<X^{1/4}$ are handled by $|\psi|\le1/2$.

### M9. Fixed-coefficient main-term criterion

**Status:** official remaining open target.

If, for every dyadic $D$ with $X^{1/4}\le D\le X^{1/2}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon},
$$

with the actual coefficients $\alpha_{h,H_D}$, then

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### H5b-Shift. Fractional-frequency theorem-extension problem

**Status:** open theorem-extension problem.

For $\beta\in\{1/4,3/4\}$, prove or cite an estimate for sums of the form

$$
\sum_{q\asymp Q}a_{q,\beta}
\sum_{d\asymp D}w_D(d)e((q+\beta)X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

where $Q\le H_D/4$ and $a_{q,\beta}$ is inherited from $\alpha_{4q+r,H_D}\chi_4(r)$.

### LY-Raw-Mismatch

**Status:** proved theorem-application guardrail.

Li--Yang's published Case A/B restrictions do not cover the raw endpoint Vaaler block. At

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H\asymp X^{1/4},
$$

Case A gives $H\le X^{33/164}$ and Case B gives $H\le X^{23/138}$, both below $X^{1/4}$.

### LY-Endpoint-Gap

**Status:** diagnostic, not no-go theorem.

Li--Yang's final circle/divisor reduction asks for

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\ldots,
$$

with $H\le MT^{-\theta^*}$, while the endpoint Vaaler range asks for $H\le MT^{-1/4}$.

### Q1-Spectral

**Status:** proved diagnostic for operator-norm-only methods.

On odd denominators, $U=\operatorname{diag}(\chi_4(d))$ is unitary, and

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Thus operator-norm-only estimates do not exploit the spatial character.

### H12-Trace-Invariance

**Status:** proved diagnostic for pure conjugacy-invariant trace methods.

If the signed matrix is exactly $U^*KU$, then

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This does not rule out non-conjugacy signed statistics.

### H13. B-process-first transform for M9a

**Status:** exploratory technical route; transform structure derived, no bound proved.

Apply Poisson summation modulo $4$ to

$$
\sum_d\chi_4(d)w_D(d)e(hX/d).
$$

Expected output:

$$
\sum_m \chi_4(m)
\int w_D(u)e(hX/u-mu/4)\,du,
$$

up to convention-dependent constants and signs. Stationarity gives

$$
m\asymp \frac{hX}{D^2}.
$$

At maximal height $h\asymp DX^{-1/4}$ and $D=X^\delta$,

$$
m\asymp X^{3/4-\delta}.
$$

The leading dual phase is square-root type and Hessian-degenerate:

$$
\Phi(h,m)\asymp\sqrt{Xhm},
\qquad
\det\nabla^2\Phi=0.
$$

### C2-SPU / H13-SPU. Uniform stationary phase

**Status:** required technical lemma; not proved.

For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

prove uniform stationary, nonstationary, boundary, and short-dual-length estimates, with separate tracking of

$$
M_{\rm dual}\asymp \frac{kX}{D^2},
\qquad
\Lambda\asymp \frac{kX}{D}.
$$

### CRI. Cross-Residue Interference statistic

**Status:** proposed diagnostic object, not a lemma.

After splitting

$$
S_D(h)=S_1(h)-S_3(h),
$$

with

$$
S_r(h)=\sum_m w_D(4m+r)e(hX/(4m+r)),
\qquad r\in\{1,3\},
$$

consider

$$
\mathcal S_{\rm CRI}
=
\sum_h w_H(h)S_1(h)\overline{S_3(h)}.
$$

This is a candidate non-conjugacy signed statistic. It requires a normalization, a target bound, and numerical falsification before promotion.

### D-Align

**Status:** replacement for rejected factorial-alignment heuristic.

For integer $X$,

$$
\#\{d\in[X^{1/4},X^{1/2}]:d\mid X\}
\le \tau(X)
\ll_\epsilon X^\epsilon.
$$

Therefore exact divisor alignment alone cannot create a dense critical-block obstruction.

### Phi-Special-Values

**Status:** proved algebraic lemma for computation.

For

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
$$

one has

$$
\Phi(1/2)=1/2,
$$

$$
\Phi(1/4)=3\pi/16+1/4,
$$

and

$$
\Phi(3/4)=-3\pi/16+3/4.
$$

## Counterexample checks to run

1. **H4 source check.**
Extract the exact Vaaler or Montgomery--Vaughan statement: coefficient formula, sign convention, $K_H$ normalization, residual constant, and integer convention.

2. **H4 integer jump test.**
Verify numerically and symbolically that $V_H(n)=0$ and $K_H(0)/(2H+2)=1/2$ for integer $n$.

3. **R5 first-leg stress test.**
Compute

$$
R_1(D;X)=\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

for square, near-square, nonsquare, and divisor-rich $X$.

4. **R5 shifted-leg stress test.**
For $\rho\in\{1,3\}$ compute

$$
R_{2,\rho}(D;X)=
\frac1{H_D}\sum_{d\asymp D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right).
$$

5. **R5 continuous $X$ test.**
Use noninteger $X=N+\eta$, including very small $\eta$, and verify that the product-count kernel

$$
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
$$

remains uniformly summable.

6. **R5 dyadic bookkeeping test.**
Check zero mode, both signs of $k$, all dyadic blocks, smooth partition overlap, and $D<X^{1/4}$ short-block handling.

7. **M9 fixed-coefficient numerics.**
Compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ with exact $\alpha_{h,H_D}$ and report

$$
|\mathcal M_i(D;X)|/X^{1/4}.
$$

8. **M9 stress comparison.**
Compare fixed-coefficient values to arbitrary-coefficient and $L^1$ stress norms.

9. **M9b fractional-shift matrix test.**
Compare toy spacing matrices for

$$
e(qX/d)
$$

and

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\}.
$$

Identify which rational-collision steps are stable under the shift.

10. **Li--Yang line audit.**
Record exact source labels for $S$, Case A, Case B, final $S/H$ reduction, allowed $F$ hypotheses, and weight/BV hypotheses. Do not treat phase similarity as theorem applicability.

11. **Q1-Spectral matrix test.**
Construct the actual Cauchy--Schwarz kernel arising from M9a and compare the signed quadratic form with the operator-norm bound.

12. **CRI numerical falsification.**
Compute $\mathcal S_{\rm CRI}$ and compare it with the corresponding absolute/cyclic trace statistic. If it shows no reduction, deprioritize CRI.

13. **H13 Poisson normalization test.**
Derive the exact modulo-$4$ Poisson formula under $e(t)=e^{2\pi it}$, including constants and Gauss factors.

14. **H13 stationary-phase uniformity test.**
Check the regimes $M_{\rm dual}\asymp1$, $M_{\rm dual}\gg1$, stationary point near support edge, and nonstationary tails.

15. **H13 signed-spacing test.**
After B-process-first, apply the first intended Cauchy--Schwarz or spacing step and determine whether the dual $\chi_4(m)$ survives or becomes a diagonal unitary erased by an operator norm.

## Research strategy adjustment

Round 12 should be recorded as a **proof-infrastructure and M9-diagnostic round**.

The residual side is now provisionally under control:

$$
\text{H4}+\text{R5-Full}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

The active work should no longer focus on arbitrary residual reciprocal sums. It should focus on the fixed Vaaler main sums M9 and on whether any method can exploit the exact coefficients and characters before norm estimates erase them.

The next round should keep the balanced hyperbola/Vaaler route as the main framework. It should not pivot to Mellin--Perron or signed Fourier, except as comparison modules. The serious exploratory allocation should be H13/B-process-first for M9a, because it is directly connected to the current bottleneck and may move $\chi_4$ into a place where a signed estimate can be tested.

Assessment of A2: A2 contributed useful algebraic diagnostics, especially Q1-Spectral and H13, but several statements remain overbroad or stylistically inflated. The next A2 prompt should require proof-draft-ready statements, no route-closing language, and one concrete signed statistic with a falsification test.

Assessment of A3: A3 contributed useful verification discipline, especially $\Phi$ values, Li--Yang endpoint mismatch, and C2 scale separation. The next A3 prompt should move from protocols to executed computations and line-by-line theorem matching. A3 should also treat M9b's BV/arithmetic-progression issue as a live gap, not as automatically covered.

## Next-round prompts by agent

### For A1

Write the Round 13 proof-infrastructure packet.

Objectives:

1. **Source-normalize H4.**
   Give the exact theorem/page/reference for the finite Vaaler approximation. Match:
   - the function $\Phi$;
   - the coefficient formula $\alpha_{h,H}$;
   - the sign convention for $\psi(t)=t-\lfloor t\rfloor-\frac12$;
   - the Fejer kernel normalization;
   - the residual constant;
   - the integer-discontinuity convention.

2. **Write R5-Full as a complete proof.**
   Include:
   - first leg $K_H(X/d)$;
   - shifted legs $K_H((X/d+\rho)/4)$ for $\rho=1,3$;
   - real and integer $X$;
   - nearest-integer tie rules;
   - positivity and congruence of $\ell=4m-\rho$;
   - dyadic weights and bounded overlap;
   - zero mode;
   - both signs of frequency;
   - short blocks $D<X^{1/4}$;
   - logarithmic losses absorbed into $X^\epsilon$.

3. **Insert the bridge theorem into the proof draft.**
   State and prove:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

4. **Freeze M9 as the official main target.**
   Use actual $\alpha_{h,H_D}$ only. Put arbitrary-coefficient versions in a stress-test appendix.

5. **Write the M9b theorem-extension problem precisely.**
   Decide whether the natural formulation is:
   - arithmetic progressions in $h$;
   - fractional-frequency phases $e((q+\beta)X/d)$;
   - or a theorem with periodic $h$-weights and controlled BV norm.

6. **Li--Yang subrange map.**
   Produce a table of covered and uncovered ranges in $(D,H)$ using the exact Li--Yang conditions, distinguishing raw Case A/B restrictions from the final $\theta^*$ reduction.

Exploratory allocation: include a short H13 falsification checklist. State which part of the transform or first signed-spacing step would make H13 unhelpful.

### For A2

Produce a conservative proof-draft-ready obstruction and H13 packet. Use low-temperature referee style and avoid route-closing language.

Objectives:

1. **Rewrite Q1-Spectral cleanly.**
   State the finite vector space, define $U=\operatorname{diag}(\chi_4(d))$, prove

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}},
$$

   and list exactly which methods this blocks and which it does not block.

2. **Rewrite H12 trace invariance narrowly.**
   Prove only

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

   Do not claim this blocks non-conjugacy signed forms.

3. **Repair C3-Affine/Rational.**
   State exact lattice variables, odd/even cases, and specify whether each statement is connected to M9/H13 or merely diagnostic.

4. **Formalize H13.**
   Give:
   - exact Poisson summation modulo $4$ under $e(t)=e^{2\pi it}$;
   - exact Gauss factor;
   - stationary point;
   - leading phase and amplitude;
   - dual length $m\asymp hX/D^2$;
   - range table for $D=X^\delta$, $1/4\le\delta\le1/2$;
   - Hessian-degeneracy check;
   - statement of the discrete spacing theorem that would be needed after transformation.

5. **Define one concrete sign-preserving statistic.**
   The Cross-Residue Interference statistic is acceptable only if made executable:
   - finite matrix or bilinear form;
   - normalization;
   - target bound;
   - precise reason it is not just $U^*KU$ conjugacy;
   - falsification test.

6. **Remove or replace factorial-alignment material.**
   Use the divisor-bound replacement:

$$
\#\{d\in[X^{1/4},X^{1/2}]:d\mid X\}
\le \tau(X)\ll_\epsilon X^\epsilon.
$$

Exploratory allocation: propose one signed-spacing or open-path moment for H13 that survives the first Cauchy--Schwarz step. State exactly how to falsify it numerically.

### For A3

Execute verification and computation tasks. Prefer scripts, exact formulas, tables, and line labels over prose.

Objectives:

1. **Complete H4 source audit.**
   Extract the Vaaler theorem from a primary source or trusted standard exposition. Verify:
   - $\Phi(u)$;
   - coefficient formula;
   - residual constant;
   - Fejer kernel normalization;
   - integer convention;
   - sign conversion from $1/2-\{x\}$ to $\psi(t)=\{t\}-1/2$.

2. **Run R5 numerical tests.**
   Produce tables for:
   - first leg;
   - shifted second legs $\rho=1,3$;
   - square $X$;
   - near-square $X$;
   - nonsquare $X$;
   - divisor-rich $X$;
   - dyadic scales $D\asymp X^{1/4},X^{3/8},X^{1/2}$.

   Report values normalized by $X^{1/4}$.

3. **Run M9 fixed-coefficient numerics.**
   Compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ using exact $\alpha_{h,H_D}$. Compare:
   - fixed coefficients;
   - random/arbitrary stress coefficients;
   - $L^1$ stress norm.

   Report $|\mathcal M_i|/X^{1/4}$.

4. **Line-by-line Li--Yang audit.**
   Record exact labels and lines for:
   - definition of $S$;
   - Case A;
   - Case B;
   - final $S/H$ target;
   - $H,M,T$ restrictions;
   - allowed weight hypotheses;
   - allowed $F$ hypotheses.

   Determine whether M9b is best represented as an $h$-arithmetic progression, a fractional-frequency shift, or an impermissible BV weight.

5. **Finish C2/H13 stationary-phase uniformity.**
   Prove or clearly state the missing estimates for:
   - interior stationary range;
   - nonstationary integration by parts;
   - stationary point at support boundary;
   - $M_{\rm dual}\asymp1$;
   - dependence on $\Lambda\asymp kX/D$.

   Do not infer double-sum cancellation from one-integral estimates.

6. **Implement signed-spacing toy tests.**
   Build:
   - Q1-Spectral operator-norm comparison;
   - Cross-Residue Interference statistic if A2 specifies it;
   - M9b fractional-shift toy spacing matrix.

   Report numerical results and code-ready formulas.

Exploratory allocation: test H13 near $D\asymp X^{1/2}$, where the dual length is closest to the original Vaaler height. Compare the signed dual character case with the unsigned dual case.

## Confidence

High confidence in the selected balanced hyperbola/Vaaler route as the current reduction framework.

High confidence that no new Gauss circle exponent was proved in Round 12.

High confidence that H1--H3 remain valid proved reductions.

Moderate-to-high confidence that H4 is correctly stated, but only moderate confidence in exact source normalization until a page-level citation is supplied.

High confidence that R5 is mathematically sound conditional on H4.

Moderate-to-high confidence that R5-Full clears the full Vaaler residual after complete proof-draft bookkeeping.

High confidence that M9 fixed-coefficient main sums are now the official remaining bottleneck.

High confidence that Li--Yang cannot be imported as a black box for the raw endpoint Vaaler block.

High confidence in Q1-Spectral as a restricted operator-norm character-blindness diagnostic.

Moderate confidence that H13 is worth continued exploration, especially near $D\asymp X^{1/2}$.

Low confidence that H13, Cross-Residue Interference, Mellin--Perron, signed Fourier truncation, or current printed Li--Yang technology reaches the endpoint without new input.

Overall Round 12 judgment: productive, but not a proof round. The residual side is provisionally controlled; the hard work has been localized to M9 and to the search for a sign-preserving method that can exploit the actual Vaaler coefficients and $\chi_4$ before standard norm estimates erase them.