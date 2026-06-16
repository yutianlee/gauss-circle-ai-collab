## Summary

Round 11 is a precision and audit round. It does **not** prove a new Gauss circle exponent.

The conservative Round 11 judgment is:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

where

$$
P(X)=N(\sqrt X)-\pi X.
$$

The residual side of the finite Vaaler route should now be treated as **provisionally controlled**, not as the active bottleneck, provided H4 is source-normalized correctly and R5-Full is written cleanly. The remaining hard analytic problem is M9: the fixed-Vaaler-coefficient main sums. This is not a cosmetic distinction: arbitrary-coefficient versions of H5a/H5b are stronger stress tests, but they are not the actual dependency created by the Vaaler reduction.

External source status: Vaaler’s paper is Jeffrey D. Vaaler, “Some extremal functions in Fourier analysis,” *Bulletin of the American Mathematical Society* 12(2), 183--216, 1985; metadata is available through Project Euclid and AMS. Li--Yang’s paper is Xiaochun Li and Xuerui Yang, “An improvement on Gauss’s Circle Problem and Dirichlet’s Divisor Problem,” arXiv:2308.14859; the arXiv abstract states that it uses the Bombieri--Iwaniec method, a new first-spacing estimate, and Huxley’s second-spacing results.

## Selected main route

Keep the balanced arithmetic hyperbola/Vaaler route as the selected main route:

$$
P(X)
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{fixed-coefficient reciprocal main sums}.
$$

The exact arithmetic foundation remains:

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

with

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

For each dyadic denominator block $d\asymp D$ with

$$
X^{1/4}\le D\le X^{1/2},
$$

use the local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ must be excluded from Vaaler truncation because the natural height may be $0$; they are handled trivially using $|\psi|\le 1/2$, giving total contribution $O(X^{1/4})$ up to logarithms.

The official remaining analytic target is M9:

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

the second sum may also be written as

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

The M9 target is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over dyadic $D$. No agent proved this target.

## Useful fragments by source

### From A1

A1’s main contribution is the clean Round 11 reduction:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

A1 also gives the most complete R5 proof. The Fejer kernel is

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin \pi(H+1)t}{\sin \pi t}\right)^2.
$$

The standard pointwise bound is

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right),
$$

hence

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg, with $m$ nearest to $X/d$ and $d\asymp D$,

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

Set

$$
\Delta=\frac{D}{H}\asymp X^{1/4}.
$$

Then

$$
\frac1H K_H(X/d)
\ll
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by $n=md$ gives at most $\tau(n)$ representations. Thus

$$
\frac1H\sum_{d\asymp D}K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

This last step does **not** need Shiu’s short-interval theorem: the pointwise divisor bound

$$
\tau(n)\ll_\epsilon n^\epsilon
$$

and

$$
\sum_{n\in\mathbb Z}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll \Delta+1
$$

already suffice.

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
\ell=4m-\rho,\qquad \ell\equiv-\rho\pmod 4,
$$

again gives a product $n=d\ell$, and the congruence restriction only reduces the number of admissible factorizations. The same divisor-counting argument applies.

A1’s H5b-Shift formulation is also valuable. Splitting

$$
h=4q+r,\qquad r\in\{1,3\},
$$

gives

$$
\chi_4(4q+r)e((4q+r)X/(4d))
=
\chi_4(r)e((q+r/4)X/d).
$$

Thus M9b requires a theorem for fixed fractional frequency shifts

$$
e((q+\beta)X/d),
\qquad
\beta\in\left\{\frac14,\frac34\right\}.
$$

This is a real theorem-extension gap, not an automatic consequence of the M9a phase.

### From A2

A2’s most useful contribution is Q1-Spectral, the operator-norm character-blindness diagnostic. If the spatial character enters a spacing matrix only through a diagonal unitary matrix

$$
U=\operatorname{diag}(\chi_4(d)),
$$

then

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Therefore any method that bounds the signed quadratic form only through an operator norm, Schur bound, Gershgorin-type estimate, or absolute-value matrix cannot exploit the $\chi_4(d)$ signs. This should be added to the lemma bank as a **proved diagnostic for operator-norm-only methods**.

A2’s trace-cycle observation is useful but narrower. If the signed object is literally a conjugate $U^*KU$, then cyclic traces are invariant:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This proves blindness for pure conjugacy-invariant trace statistics. It does **not** rule out all signed forms, open-path moments, residue-interference estimates, or non-conjugacy signed kernels.

A2 also raised the H8/B-process-first or “twisted Voronoi” exploration. This should be kept, but heavily downgraded. The useful core is: apply Poisson summation modulo $4$ to the spatial-character sum before Cauchy--Schwarz, identify the dual length

$$
m\asymp \frac{hX}{D^2},
$$

and check whether the dual character survives an actual spacing estimate. The overclaim is that this automatically produces a symmetric or more tractable endpoint. For general $D$ the dual length is not uniformly $X^{1/4}$; at the critical block $D\asymp X^{1/2}$ and $h\asymp X^{1/4}$ it is $m\asymp X^{1/4}$, but outside that endpoint the geometry changes.

A2’s factorial-alignment obstruction should be rejected in its current form. Taking $X=N!$ does not give many critical denominators $d\in[X^{1/4},X^{1/2}]$ dividing $X$; for large $N$, $X^{1/4}$ is vastly larger than $N$. Also, cancellation of $\sum_{d\sim D}\chi_4(d)$ does not require the prime number theorem in arithmetic progressions: $\chi_4$ is periodic modulo $4$, so unsmoothed interval sums are $O(1)$ and smooth weighted sums are controlled by elementary summation by parts.

### From A3

A3’s strongest contribution is theorem-dependency discipline. A3 correctly keeps R5 conditional on H4, keeps M9 open, and separates phase compatibility with Li--Yang from theorem-level applicability.

A3’s Li--Yang audit is useful and should be retained. Li--Yang’s double sum has the form

$$
S
=
\sum_{H\le h\le 2H}g(h/H)
\sum_{M\le m\le 2M}G(m/M)
e\left(\frac{hT}{M}F(m/M)\right),
$$

with $g,G$ of bounded variation and $F\in C^3([1,2])$ satisfying derivative lower and upper bounds and

$$
|F^{(1)}F^{(3)}-3(F^{(2)})^2|\ge C_4^{-1}.
$$

The raw endpoint substitution is

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4}.
$$

Li--Yang Case A requires

$$
H\le MT^{-49/164}=X^{33/164}\approx X^{0.2012},
$$

while Case B gives

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}=X^{1/6}.
$$

Both are below $X^{1/4}$. Therefore their theorem cannot be quoted directly on the raw endpoint block. This is a theorem-application guardrail, not a no-go theorem for all Bombieri--Iwaniec methods.

A3’s C2-SPU stationary-phase outline is useful as a technical module, but it must remain a transform/asymptotic lemma rather than an estimate of the full sum. For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

with $\xi=-m<0$,

$$
u_0=\sqrt{\frac{kX}{m}},
\qquad
\phi(u_0)=2\sqrt{kXm},
\qquad
\phi''(u_0)=\frac{2m}{u_0}.
$$

The active dual length is

$$
M_{\mathrm{dual}}\asymp \frac{kX}{D^2},
$$

whereas the stationary-phase large parameter is

$$
\Lambda\asymp \frac{kX}{D}.
$$

These two scales must not be conflated. A3 correctly warned that non-analytic weights give rapid integration-by-parts decay, not exponential decay.

A3’s numerical plan is appropriate: test R5 first and second legs, then test $\mathcal M_1,\mathcal M_2$ with the actual Vaaler coefficients, and compare against arbitrary-coefficient and $L^1$ stress versions. One correction: for

$$
\Phi(u)=\pi u(1-|u|)\cot(\pi u)+|u|,
$$

one has

$$
\Phi(1/2)=1/2,
$$

not $1$. Also $\Phi(1/4)$ and $\Phi(3/4)$ are not equal. This matters for any M9 numerical implementation.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.**  
Round 11 gives a sharper reduction and obstruction map. It does not prove M9 and therefore does not prove

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

2. **Reject treating R5 as unconditional before H4 is source-normalized.**  
The R5 product-count argument is sound once the Vaaler residual majorant is accepted. The H4 theorem still needs a page-level citation and convention check.

3. **Reject H5r-B/H5r-L1 as active proof dependencies.**  
The residual is controlled directly by the positive Fejer kernel and R5. Arbitrary bounded coefficients and termwise $L^1$ are now stress tests only.

4. **Reject black-box Li--Yang endpoint import.**  
The Li--Yang phase class overlaps structurally with M9, but their raw Case A/B restrictions and final exponent do not provide the endpoint height needed here.

5. **Reject global no-go language for Bombieri--Iwaniec or spacing methods.**  
The raw theorem mismatch is proved. A future signed spacing estimate or different dissection is not ruled out.

6. **Reject A2’s factorial-alignment counterexample.**  
It does not apply to the critical dyadic range as stated and uses unnecessary PNT-in-AP reasoning for $\chi_4$ interval cancellation.

7. **Reject A2’s “twisted Voronoi symmetric dualization” as a proved route.**  
It is a potentially useful H8-style exploratory transform, but it needs exact Poisson normalization, stationary phase, dual ranges for all $D$, amplitude, boundary estimates, and a post-transform bilinear/spacing theorem.

8. **Reject treating Q1-Spectral as a universal obstruction.**  
It blocks operator-norm-only and absolute-value matrix methods. It does not block direct signed-form estimates that do not factor through diagonal-unitary-invariant quantities.

9. **Reject using C2-SPU as an endpoint bound.**  
Stationary phase for a single integral does not prove cancellation in the full double sum over $k$ and the dual variable. C2-SPU is a transform lemma, not a summation theorem.

10. **Reject treating Mellin--Perron or signed Fourier as a primary pivot.**  
Both remain comparison modules. Signed Fourier may preserve signs formally, but discontinuity neighborhoods still have to be controlled. Mellin--Perron likely reconstructs Hardy--Voronoi--Bessel phases; exact kernels and truncation errors remain unwritten.

## Known gaps

1. **H4 source-normalization gap.**  
Need a precise citation for the finite Vaaler theorem with coefficient function, Fejer kernel normalization, residual constant, and sawtooth convention. The proof must state exactly how the centered trigonometric convention covers the floor-compatible value $\psi(n)=-1/2$.

2. **R5-Full write-up gap.**  
The proof must include first leg, shifted second leg, integer and noninteger $X$, nearest-integer choices, signed or non-positive dyadic weights handled by $|w_D|$, zero mode, both frequency signs, short blocks $D<X^{1/4}$, and dyadic logarithms.

3. **M9 remains open.**  
No endpoint estimate for $\mathcal M_1$ or $\mathcal M_2$ was supplied. This is the main analytic bottleneck.

4. **M9b shifted-frequency theorem gap.**  
The phase

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\},
$$

must be accepted by the intended spacing theorem, or an alternate representation of M9b must be chosen.

5. **Li--Yang subrange map incomplete.**  
The raw endpoint block fails. The repo still needs a precise map of which $D,H$ subranges are covered by existing Li--Yang technology and which high-frequency ranges remain uncovered.

6. **Character-preserving spacing gap.**  
Q1-Spectral shows what cannot work. The repo still lacks a signed estimate that actually preserves $\chi_4(d_1)\chi_4(d_2)$ or $\chi_4(h)$ through a useful spacing or bilinear inequality.

7. **H8/B-process-first uniform transform gap.**  
The transform must be stated uniformly for all $D\in[X^{1/4},X^{1/2}]$ and $1\le h\le H_D$, not only at the endpoint $D\asymp X^{1/2}$.

8. **C2-SPU boundary and summation gap.**  
Need support-boundary stationary phase, nonstationary integration-by-parts, $M_{\mathrm{dual}}\asymp1$ transitions, and then a separate summation theorem if the transform is to estimate anything.

9. **Numerical evidence gap.**  
No actual R5 or M9 data have been committed. The next round should produce tables or scripts, not only protocols.

10. **Poisson--Bessel calibration remains secondary.**  
It is useful for normalization and the $R^{2/3}$ sanity check, but it should not displace M9.

## New lemmas to add

### H4. Vaaler finite approximation with Fejer residual

**Status:** external theorem dependency; statement likely correct, source-normalization pending.

For $H\ge1$,

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H(t),
$$

with

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1,
$$

and

$$
|R_H(t)|\le \frac1{2H+2}K_H(t),
$$

where

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

The convention check at integers is essential: the Vaaler polynomial cancels symmetrically at integer $t$, while the residual majorant has size $1/2$ because

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

### R5. Fejer product-count residual bound

**Status:** proved conditional on H4.

For $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp D X^{-1/4}$, and $|w_D|\le1$ supported on $d\asymp D$,

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

### R5-Full. Total Vaaler residual bound

**Status:** conditional bridge lemma; should be written into the proof draft.

Assume H4 and R5 on every dyadic block. Then all finite Vaaler residuals arising from H3 contribute

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9. Fixed-coefficient main-term criterion

**Status:** official remaining target.

If, for every dyadic $D$ with $X^{1/4}\le D\le X^{1/2}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon},
$$

with the actual Vaaler coefficients $\alpha_{h,H_D}$, then H1--H4 and R5-Full imply

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### H5b-Shift. Shifted-frequency theorem-extension problem

**Status:** open theorem-extension problem.

For $\beta\in\{1/4,3/4\}$, $Q\asymp H_D$, prove or cite an endpoint estimate of the form

$$
\sum_{q\asymp Q}a_{q,\beta,H_D}
\sum_{d\asymp D}w_D(d)e((q+\beta)X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

where

$$
a_{q,\beta,H_D}\ll\frac1{q+1}
$$

and $a_{q,\beta,H_D}$ comes from $\alpha_{4q+r,H_D}\chi_4(r)$.

### LY-Raw-Mismatch

**Status:** proved theorem-application guardrail.

For the raw endpoint block

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$

Li--Yang Case A gives

$$
H\le X^{33/164},
$$

and Case B gives

$$
H\le X^{23/138}.
$$

Neither reaches $X^{1/4}$. This only blocks black-box import.

### Q1-Spectral

**Status:** proved diagnostic.

If $\chi_4$ enters only as a diagonal unitary conjugation $U^*KU$, then operator-norm-only estimates cannot exploit it:

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

### H12-Trace-Invariance

**Status:** proved diagnostic for pure conjugacy-invariant trace methods; not a universal obstruction.

If the signed matrix is literally $U^*KU$, then

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This does not rule out non-conjugacy signed statistics.

### H13. B-process-first / twisted dual M9a transform

**Status:** exploratory target; not proved.

Apply Poisson summation modulo $4$ to the spatial-character M9a sum before Cauchy--Schwarz. Required output:

1. exact transform and constants under $e(t)=e^{2\pi i t}$;
2. dual character or Gauss factor;
3. stationary point and phase;
4. dual length $m\asymp hX/D^2$;
5. amplitude and boundary terms;
6. validity range for every $D\in[X^{1/4},X^{1/2}]$;
7. explicit statement of whether the dual phase is compatible with any known spacing theorem.

### C2-SPU. Uniform odd-lattice stationary phase

**Status:** technical lemma pending.

For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

prove uniform estimates in the stationary, nonstationary, boundary, and short-dual-length regimes. This lemma must not be used as a summation bound by itself.

## Counterexample checks to run

1. **H4 integer jump test.**  
Verify directly that the chosen Vaaler polynomial has value $0$ at integer arguments and that the residual majorant exactly covers the floor-compatible discrepancy $|\psi(n)-0|=1/2$.

2. **R5 first-leg stress test.**  
Compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

for square, near-square, nonsquare, and divisor-rich $X$.

3. **R5 shifted-leg stress test.**  
For $\rho\in\{1,3\}$ compute

$$
\frac1{H_D}
\sum_{d\asymp D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right).
$$

4. **Short-block check.**  
Verify that all blocks with $D<X^{1/4}$ are handled before Vaaler is invoked and contribute $O(X^{1/4})$.

5. **M9 fixed-coefficient numerics.**  
Compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ using the exact $\alpha_{h,H_D}$, including the correct values of $\Phi(u)$.

6. **M9 stress comparison.**  
Compare the fixed-coefficient sums to arbitrary-coefficient and $L^1$ stress norms. The question is whether the actual Vaaler coefficients give significant cancellation.

7. **H5b fractional shift test.**  
Compare phases

$$
e(qX/d)
$$

and

$$
e((q+\beta)X/d)
$$

inside a toy spacing dissection. Identify which rational approximation steps are shift-invariant.

8. **Q1-Spectral matrix test.**  
Build the actual Cauchy--Schwarz kernel from M9a and compare bounds for $K$ and $U^*KU$.

9. **Signed-form toy test.**  
Test a bilinear form that is not reduced to $\|K\|_{\operatorname{op}}$. Determine whether $\chi_4(d_1)\chi_4(d_2)$ survives any useful statistic before absolute values enter.

10. **H13 dual transform test.**  
Carry out the B-process-first transform for several dyadic $D$ values. Verify that the claimed symmetric scale occurs only in the endpoint subrange.

11. **C2-SPU transition test.**  
Numerically and symbolically test $kX/D^2\asymp1$, support-boundary stationary points, and nonstationary tails.

12. **Li--Yang line audit.**  
Record exact labels, assumptions, Case A/B restrictions, allowed $F$ forms, and final $S/H$ target from the arXiv source. Do not treat phase similarity as theorem applicability.

## Research strategy adjustment

Round 11 should be recorded as a **diagnostic M9 round**, not as a route breakthrough. The residual obstacle has likely been cleared by R5-Full, conditional on H4. The main work now is to determine whether the fixed Vaaler coefficients and $\chi_4$ signs can be exploited before standard norm estimates erase them.

The next round should split labor as follows:

- A1 should lock down the proof infrastructure: exact H4 source, R5-Full, bridge theorem, M9 definitions, and Li--Yang mapping.
- A2 should repair and formalize the character-blindness diagnostics without overclaiming, then build one exact signed model or one exact H13 dual transform.
- A3 should execute the computational and formula audits: actual Vaaler coefficients, R5 stress tests, M9 fixed-coefficient numerics, C2-SPU constants, and Li--Yang line matching.

Do not pivot to Mellin--Perron or signed Fourier as the main route. Keep them as comparison modules. The only exploratory track that should receive serious next-round allocation is H13/B-process-first for M9a, because it directly tests whether a sign-preserving transform can change the M9 geometry.

## Next-round prompts by agent

### For A1

Write the proof-infrastructure packet for Round 12.

Objectives:

1. Verify H4 from a standard source. State the exact theorem with:
   - coefficient function $\Phi$;
   - coefficient formula $\alpha_{h,H}$;
   - Fejer kernel normalization;
   - residual constant;
   - convention for the centered sawtooth;
   - explicit conversion to the floor-compatible convention $\psi(n)=-1/2$.

2. Write R5-Full as a complete proof:
   - first leg $K_H(X/d)$;
   - second shifted legs $K_H((X/d+\rho)/4)$ for $\rho=1,3$;
   - noninteger and integer $X$;
   - dyadic weights and bounded overlap;
   - zero mode;
   - both signs of frequency;
   - short blocks $D<X^{1/4}$;
   - logarithmic losses absorbed into $X^\epsilon$.

3. Insert the bridge theorem into the proof draft:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

4. Freeze M9 as the official remaining target. Use actual Vaaler coefficients only. Do not revert to arbitrary $u_h$ except in a clearly marked stress-test section.

5. Give a theorem-level Li--Yang compatibility map for M9a and M9b:
   - exact $S$ form;
   - $F$ functions;
   - Case A/B restrictions;
   - final $S/H$ target;
   - covered and uncovered $D,H$ ranges;
   - whether shifted $F$ forms or fractional-frequency shifts cover M9b.

Exploratory allocation: include a short “H13 feasibility note” stating what exact transform A2 should prove and what would falsify it.

### For A2

Produce a conservative formula-level obstruction and exploration packet. Use low-temperature referee style and avoid route-closing language.

Objectives:

1. Formalize Q1-Spectral as a proved diagnostic:
   - specify the finite vector space;
   - define $U=\operatorname{diag}(\chi_4(d))$ on odd denominators;
   - prove $\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}$;
   - list exactly which methods this blocks;
   - list signed-form methods it does not block.

2. Rewrite H12 trace/cycle material:
   - prove only the pure conjugacy-invariant trace statement;
   - do not call it a global obstruction;
   - define one non-conjugacy signed statistic that might still preserve signs.

3. Repair C3-Affine/C3-Rational:
   - state exact lattice hypotheses;
   - separate odd/even dilation cases;
   - connect, if possible, to an actual M9 or H13 transform;
   - label anything not connected to M9 as diagnostic only.

4. Develop H13, the B-process-first transform for M9a:
   - exact Poisson summation modulo $4$;
   - exact dual character/Gauss factor;
   - stationary phase with amplitude;
   - dual length $m\asymp hX/D^2$;
   - range table for $D=X^\delta$, $1/4\le\delta\le1/2$;
   - explicit check of the Hessian-degenerate phase $\sqrt{hXm}$;
   - statement of what kind of discrete spacing theorem would be needed after the transform.

5. Remove or repair the factorial-alignment example. If retained, it must use denominators actually lying in $[X^{1/4},X^{1/2}]$ and must not invoke PNT in AP for the elementary periodic sum of $\chi_4$.

Exploratory allocation: propose one sign-preserving statistic for M9 that is not an operator norm and not a cyclic conjugacy trace. State a falsification test.

### For A3

Execute verification and computation tasks. Prefer scripts, exact formulas, and tables over prose.

Objectives:

1. Independently source-check H4:
   - verify the coefficient formula and residual constant from Vaaler or a reliable standard exposition;
   - check the integer-discontinuity convention;
   - compute $\Phi(1/4)$, $\Phi(1/2)$, and $\Phi(3/4)$ correctly.

2. Run R5 numerical stress tests:
   - first leg;
   - shifted second legs;
   - square, near-square, nonsquare, and divisor-rich $X$;
   - multiple dyadic $D$ values;
   - compare to $X^{1/4}$.

3. Run M9 fixed-coefficient numerics:
   - compute $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ with actual $\alpha_{h,H}$;
   - compare against arbitrary-coefficient and $L^1$ stress norms;
   - report normalized values $|\mathcal M_i|/X^{1/4}$.

4. Complete the Li--Yang theorem line audit:
   - exact source labels for $S$, Case A, Case B, Theorem 4.3, final reduction, and allowed $F$ forms;
   - check whether M9b is better represented as shifted $F$ or fractional-frequency shift;
   - identify the exact uncovered high-frequency range.

5. Finish C2-SPU:
   - prove stationary, nonstationary, boundary, and $M_{\mathrm{dual}}\asymp1$ regimes;
   - keep rapid integration-by-parts decay distinct from exponential decay;
   - do not infer full double-sum cancellation from one-integral estimates.

Exploratory allocation: implement a small signed-spacing matrix test for M9a and compare the signed quadratic form with the corresponding unsigned/absolute form.

## Confidence

High confidence in the selected balanced hyperbola/Vaaler framework.

High confidence that no exponent improvement has been proved.

High confidence that R5 is mathematically sound conditional on H4.

Moderate-to-high confidence that R5-Full clears the total Vaaler residual once the proof is written carefully.

High confidence that M9 fixed-coefficient sums are now the official remaining bottleneck.

High confidence that Li--Yang cannot be imported as a black box for the raw endpoint Vaaler block.

High confidence that Q1-Spectral is a useful restricted diagnostic for operator-norm-only methods.

Moderate confidence that H13/B-process-first is worth exploring as a sign-preserving transform.

Low confidence that H13, Mellin--Perron, signed Fourier truncation, or current Li--Yang technology reaches the endpoint without new input.

Overall Round 11 judgment: productive and conservative. The residual side is provisionally under control; the hard problem has been localized to M9 and to whether any sign-preserving method can exploit the actual Vaaler coefficients and $\chi_4$ signs before standard norm estimates erase them.