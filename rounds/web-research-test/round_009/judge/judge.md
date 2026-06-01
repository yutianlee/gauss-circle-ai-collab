Summary:

Round 9 does **not** prove a new Gauss circle exponent. It does, however, make a significant internal reduction improvement. The fixed-Fejer Vaaler residual H5r-F, previously treated as the central bottleneck, now appears controllable at the conjectural scale by an elementary product-counting lemma R5, conditional on the standard Vaaler Fejer-majorant theorem H4. This shifts the main unresolved analytic burden back to the Vaaler **main terms** H5a/H5b, and specifically to their **fixed Vaaler coefficient** forms rather than arbitrary-coefficient stress-test versions.

Source anchors: Round 9 packet and Stage A/B outputs are in `judge_9.md`; the retrieved snippets include the R5 product-count formulation, the Li--Yang endpoint non-import statement, and the C2 odd-lattice Poisson transform.

Selected main route:

Keep the balanced arithmetic hyperbola/Vaaler route as the main reduction framework:

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{fixed-coefficient reciprocal sums}.
$$

The target remains

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The Round 9 route should now be recorded as:

$$
\text{H1--H3}
+
\text{H4}
+
\text{R5}
+
\text{H5a-fix/H5b-fix}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Here:

- H1--H3 are the proved balanced sawtooth reductions.
- H4 is the finite Vaaler approximation with Fejer residual majorant; the exact reference and normalization still need to be verified.
- R5 is the new product-count bound for the fixed Fejer residual.
- H5a-fix and H5b-fix are the remaining hard main-term estimates with the actual Vaaler coefficients $\alpha_h$, not arbitrary coefficients.

The local scale remains

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4}.
$$

The residual target H5r-F should be demoted from "central open bottleneck" to "provisionally resolved by R5, pending exact H4 reference and complete write-up." The stronger H5r-B and H5r-L1 norms should be retained only as stress tests; they are no longer active dependencies unless R5 fails.

Useful fragments by source:

## From `gpt_pro_thinking`

The most important contribution is R5, the Fejer product-count lemma. Instead of expanding the Vaaler residual into arbitrary-coefficient reciprocal sums, the fixed Fejer residual is kept as a positive kernel:

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2.
$$

Using

$$
K_H(t)\ll \min\left(H,\frac{1}{H\|t\|^2}\right),
$$

one has

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac{1}{H^2\|t\|^2}\right).
$$

For the first residual leg,

$$
\frac1H
\sum_{d\sim D}
w_D(d)K_H(X/d),
$$

choose $m$ nearest to $X/d$. Then

$$
\|X/d\|\asymp \frac{|X-md|}{D}
$$

for $d\asymp D$, up to harmless endpoint conventions. With

$$
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

the summand is bounded by

$$
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by $n=md$ and using

$$
\tau(n)\ll_\epsilon n^\epsilon
$$

gives

$$
\frac1H
\sum_{d\sim D}
w_D(d)K_H(X/d)
\ll_\epsilon
X^\epsilon
\sum_{n\asymp X}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

The same argument should apply to the shifted second-leg kernels

$$
\frac1H
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\},
$$

after writing the near-integrality condition as

$$
X\approx d(4m-\rho).
$$

This introduces only a congruence restriction on the complementary factor, hence is bounded by the ordinary divisor function.

The second important contribution is the Li--Yang source audit. The H5r, H5a, and H5b phases are structurally compatible with Li--Yang-type reciprocal sums, but Li--Yang does not supply the endpoint theorem needed here. Their final target has the form

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\cdots,
$$

with truncation range

$$
H\le MT^{-\theta^*}.
$$

This does not reach the endpoint Vaaler range

$$
H\le MT^{-1/4}.
$$

The third important correction is that H5a/H5b should be reformulated with exact Vaaler coefficients. The prior arbitrary-coefficient versions are overstrong. The actual main terms involve

$$
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
\qquad
|\alpha_h|\ll |h|^{-1},
$$

and

$$
\sum_{1\le |h|\le H_D}
\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

These should become H5a-fix and H5b-fix.

## From `deepseek_api`

The most useful contribution is the exact odd-lattice Poisson transform C2-Alg. With

$$
e(t)=e^{2\pi i t},
\qquad
\widehat f(\xi)=\int_{\mathbb R}f(u)e(-\xi u)\,du,
$$

and

$$
f(u)=w_D(u)e(kX/u),
$$

one has

$$
\sum_{2\nmid d} f(d)
=
\frac12\sum_{m\in\mathbb Z}\widehat f(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
$$

This should be promoted as the official convention-fixed C2 algebraic lemma.

DeepSeek also correctly identified the stationary-phase sign and scale. For $\xi=-m<0$,

$$
\widehat f(-m)
=
\int w_D(u)e(kX/u+mu)\,du,
$$

with phase

$$
\phi(u)=kX/u+mu.
$$

The stationary point is

$$
u_0=\sqrt{kX/m},
$$

and the active dual length is

$$
m\asymp \frac{kX}{D^2}.
$$

The leading amplitude scale is

$$
|\widehat f(-m)|
\asymp
D^{3/2}(kX)^{-1/2}
$$

in the interior stationary range. This should be entered as C2-SP0, with uniform error estimates deferred to C2-SPU.

DeepSeek also correctly handled the small-$k$ boundary. When

$$
D\asymp X^{1/2},
\qquad
|k|\le X^\epsilon,
$$

the trivial bound

$$
|S_\star(k,D)|\ll D
$$

combined with

$$
H_D\asymp D X^{-1/4}
$$

gives

$$
\frac1{H_D}|S_\star(k,D)|
\ll X^{1/4}.
$$

Thus $X^\epsilon$ many such frequencies remain harmless.

The Li--Yang audit from DeepSeek is also valuable because it distinguishes phase compatibility from theorem applicability. For the raw endpoint block

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H=H_D\asymp X^{1/4},
$$

Li--Yang Case A gives

$$
H\le MT^{-49/164}
=
X^{33/164}
\approx X^{0.2012},
$$

and Case B gives a still smaller principal bound

$$
H\le M^{35/69}T^{-2/23}
=
X^{23/138}
=
X^{1/6}.
$$

Both are below $X^{1/4}$. Therefore Li--Yang cannot be quoted directly on the raw endpoint block.

## From `gemini_deep_think`

Gemini's most useful contribution is the sharpened Li--Yang parameter-domain warning. The conclusion should be recorded carefully:

$$
\text{raw Li--Yang theorem invocation fails at the endpoint block.}
$$

It should **not** be recorded as:

$$
\text{all Bombieri--Iwaniec/Li--Yang-type methods are impossible.}
$$

A full dissection could change effective parameters, but current published technology still reaches $\theta^*>1/4$, not the conjectural $1/4$.

Gemini's Mellin--Perron diagnostic is also useful. Applying a Perron/functional-equation route to

$$
4\zeta(s)L(s,\chi_4)
$$

with height

$$
T\asymp X^{3/4}
$$

leads by stationary phase to a dual condition roughly

$$
t_0\asymp \sqrt{nX},
\qquad
n\lesssim T^2/X\asymp X^{1/2},
$$

and phase of Hardy/Voronoi/Bessel type

$$
2\pi\sqrt{nX}.
$$

This supports treating Mellin--Perron as a comparison route that likely reconstructs the same hard oscillatory scale. It is not yet a no-go theorem.

Gemini's Q1-Ext near-collision congruence bookkeeping is a useful algebraic input. For odd $d_1,d_2$ satisfying

$$
d_1b-d_2a=\Delta,
\qquad
(a,b)=1,
$$

the case $a,b$ both odd gives

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ab)(-1)^{\Delta/2}.
$$

This is potentially useful for signed spacing matrices, but no analytic saving follows until the sign is inserted into an actual Bombieri--Iwaniec near-collision matrix before absolute values erase it.

Gemini's C3-Mult parity-collapse observation is also useful in a narrow model. For

$$
\sigma(\xi)=\frac12(-1)^{2\xi},
\qquad
\xi\in \frac12\mathbb Z,
$$

an odd integer dilation $\xi_2=a\xi_1$ gives

$$
\sigma(\xi_1)\sigma(a\xi_1)
=
\frac14.
$$

This is a diagnostic for parity loss under one class of spacing transformations. It is not a universal obstruction to all two-coset spacing methods.

Rejected or risky ideas:

1. **Reject any claim of a new Gauss circle exponent.**

Round 9 improves the internal reduction and likely removes the residual bottleneck. It does not prove

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

because H5a-fix and H5b-fix remain open.

2. **Reject treating R5 as fully unconditional before H4 is cited precisely.**

R5 is conditionally proved from the standard Fejer-kernel majorant and the divisor bound. The repository still needs the exact Vaaler theorem statement, coefficient formula, Fejer normalization, and discontinuity convention. Once H4 is verified, R5 should be promoted to proved.

3. **Reject H5r-B and H5r-L1 as active proof dependencies.**

They are stronger than needed. H5r-B with arbitrary complex coefficients is essentially a dyadic $L^1$ target and is much harder than the actual fixed Fejer residual. Keep H5r-B/L1 as stress tests only.

4. **Reject a raw black-box invocation of Li--Yang on endpoint Vaaler blocks.**

The raw endpoint block violates Li--Yang Case A and Case B parameter ranges. Structural phase compatibility is insufficient.

5. **Reject a global no-go theorem for Li--Yang/Bombieri--Iwaniec methods.**

The raw theorem mismatch is proved. A full Bombieri--Iwaniec dissection has not been written for H5a-fix/H5b-fix. Do not claim all spacing methods fail.

6. **Reject Gemini's bounded-variation parity penalty as an obstruction after residue splitting.**

Inserting $1_{2\nmid d}$ directly as a continuous Li--Yang weight is invalid, but residue splitting $d=2m+1$ restores smooth/BV weights. The BV issue is a false-proof warning, not a fundamental obstruction.

7. **Reject Mellin--Perron "isomorphism" or "circular trap" language as theorem-level.**

The saddle computation is a useful diagnostic. A full theorem still requires sharp and smoothed Perron formulas, contour shifts, functional equations, kernel estimates, and transition analysis.

8. **Reject C3-Mult as a universal parity-loss theorem.**

It covers one stylized odd-dilation model. It does not rule out two-coset spacing, rational transformations, or signed matrix methods.

9. **Reject permanent retirement of signed Fourier truncation.**

R5 makes signed Fourier truncation lower priority, but it remains a comparison route. It should be de-prioritized, not deleted, until the main-term route is clearer.

Known gaps:

1. **Exact H4 reference and normalization.**

The proof needs a standard Vaaler theorem of the form

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)+R_H(t),
\qquad
|\alpha_h|\ll |h|^{-1},
$$

with

$$
|R_H(t)|\le \frac{C}{H}K_H(t)
$$

or the sharper normalization

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t).
$$

The exact constant is harmless for exponents but must be cited correctly.

2. **Complete R5 proof integration.**

The proof draft must explicitly handle:

- first leg $K_H(X/d)$;
- second leg $K_H((X/d+1)/4)$ and $K_H((X/d+3)/4)$;
- the zero Fejer mode;
- both signs of $k$;
- all dyadic $D$ blocks;
- short blocks $D<X^{1/4}$;
- possible signed or non-positive dyadic partitions, using $|w_D|$ if needed;
- small $X$ and endpoint cases.

3. **Main fixed-coefficient sums are open.**

After R5, the hard analytic targets are H5a-fix and H5b-fix:

$$
\mathcal M_1(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

The needed target is

$$
\mathcal M_i(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

per dyadic block, up to logarithmic losses.

4. **High-frequency gap after Li--Yang.**

Li--Yang's final circle/divisor range reaches only

$$
H\le D X^{-\theta^*},
\qquad
\theta^*=0.314483\cdots,
$$

whereas the endpoint Vaaler range requires

$$
H\le D X^{-1/4}.
$$

The uncovered range is

$$
D X^{-\theta^*}
\lesssim H
\lesssim
D X^{-1/4}.
$$

At $D\asymp X^{1/2}$, this is roughly

$$
X^{0.1855}
\lesssim H
\lesssim
X^{0.25}.
$$

Raw Case A/B constraints are even more restrictive. The next audit should focus on H5a-fix/H5b-fix, not residual H5r.

5. **C2-SP uniformity.**

The leading stationary phase is accepted, but a uniform lemma must handle:

$$
M_{\mathrm{dual}}\asymp kX/D^2\asymp 1,
$$

support-boundary stationary points, nonstationary tails, and derivative dependence of $w_D$.

6. **Q1-Ext analytic use is unproved.**

The sign

$$
\chi_4(ab)(-1)^{\Delta/2}
$$

must be inserted into a concrete spacing matrix. The key issue is whether matrix norm estimates preserve this sign or erase it by absolute values.

7. **H10 Mellin--Perron comparison remains incomplete.**

Need exact sharp/smoothed Perron errors, residue at $s=1$, functional equation for $4\zeta(s)L(s,\chi_4)$, Gamma factors, saddle analysis, and transition kernel estimates.

8. **Numerical tests remain mostly unrun.**

DeepSeek supplied a test plan, not data. The repo still lacks numerical evidence for R5, Fejer spikes, second-leg shifts, main-term sizes, signed Fourier tails, and Q1-Ext sign persistence.

New lemmas to add:

## R5. Fejer product-count bound for H5r-F

**Status:** provisionally proved conditional lemma; promote to proved after H4 is cited and the second leg is written explicitly.

Let $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, and

$$
H\asymp D X^{-1/4}.
$$

Let $w_D$ be a dyadic weight supported on $d\asymp D$ with $|w_D(d)|\le 1$. Then for every $\epsilon>0$,

$$
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
|w_D(d)|K_H(X/d)
\ll_\epsilon
X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H
\sum_{d\sim D}
|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Dependency: H4 plus $\tau(n)\ll_\epsilon n^\epsilon$.

Proof mechanism: reduce Fejer spikes to near-products $md\approx X$ or $(4m-\rho)d\approx X$ with interaction width

$$
\Delta=D/H\asymp X^{1/4}.
$$

Then group by the product and use the divisor bound.

## R5-Full. Total Vaaler residual bound

**Status:** proposed bridging lemma.

Assume H4 and R5 for every dyadic block. Then the total residual contribution from Vaaler in the balanced sawtooth formula is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof requirements: sum over all dyadic $D$, both sawtooth legs, both shifts $\rho=1,3$, signs of $k$, and short blocks. The number of dyadic blocks is $O(\log X)$ and is absorbed by $X^\epsilon$.

## M9. Fixed-coefficient main-term targets

**Status:** proposed exact replacement for overstrong H5a/H5b.

For

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2},
$$

define

$$
\mathcal M_1(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

The desired local target is

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The old arbitrary-coefficient versions remain stress tests only.

## LY-Raw-Mismatch

**Status:** proved guardrail.

For the raw endpoint block

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$

Li--Yang Case A requires

$$
H\le MT^{-49/164}=X^{33/164},
$$

and Case B requires at least

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}.
$$

Both are below $X^{1/4}$. Therefore Li--Yang's main theorem cannot be quoted directly on the raw Vaaler endpoint block.

This does not preclude a full Bombieri--Iwaniec dissection or future stronger theorem.

## L9.1. Li--Yang endpoint non-import

**Status:** proved source-audit lemma.

The relevant reciprocal phases fit Li--Yang's broad phase form after residue splitting, but the theorem used for the circle/divisor problem gives

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\cdots,
$$

and does not supply the endpoint exponent $1/4$ or the full endpoint height

$$
H\le MT^{-1/4}.
$$

Also, Li--Yang's bounded-variation weights do not imply arbitrary-coefficient H5r-B or H5r-L1.

## C2-Alg. Odd-lattice Poisson transform

**Status:** proved algebraic lemma under fixed Fourier convention.

With

$$
e(t)=e^{2\pi i t},
\qquad
\widehat f(\xi)=\int f(u)e(-\xi u)\,du,
$$

one has

$$
\sum_{2\nmid d}f(d)
=
\frac12\sum_{m\in\mathbb Z}\widehat f(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
$$

## C2-SP0. Leading stationary phase for C2

**Status:** leading term accepted; uniform error not proved.

For

$$
\widehat f(-m)
=
\int w_D(u)e(kX/u+mu)\,du,
\qquad
m>0,
$$

the stationary point is

$$
u_0=\sqrt{kX/m}.
$$

In the interior range

$$
m\asymp kX/D^2,
$$

one has leading phase

$$
2\sqrt{kXm}
$$

and size

$$
|\widehat f(-m)|
\asymp
D^{3/2}(kX)^{-1/2}.
$$

## C2-SPU. Uniform C2 stationary phase

**Status:** required technical lemma, not proved.

Provide uniform estimates for C2-SP0 including:

- $m\asymp kX/D^2$ interior;
- $m$ outside the stationary range;
- $m\asymp 1$ boundary;
- stationary point near support boundary;
- derivative losses from $w_D$.

## B-Boundary. Small-frequency boundary bound

**Status:** proved elementary lemma.

For $D\asymp X^{1/2}$ and $1\le |k|\le X^\epsilon$,

$$
\frac1{H_D}|S_\star(k,D)|
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof: use $|S_\star(k,D)|\ll D$ and $H_D\asymp D X^{-1/4}$.

## Q1-Ext. Near-collision character factorization

**Status:** proved algebraic lemma; analytic use pending.

If $(a,b)=1$ and odd $d_1,d_2$ satisfy

$$
d_1b-d_2a=\Delta,
$$

then in the both-odd slope case,

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ab)(-1)^{\Delta/2}.
$$

This must be inserted into a real spacing matrix before it can be counted as analytic progress.

## C3-Mult. Multiplicative parity-collapse diagnostic

**Status:** proved in a narrow model; diagnostic only.

For

$$
\sigma(\xi)=\frac12(-1)^{2\xi},
\qquad
\xi\in\frac12\mathbb Z,
$$

odd integer dilation $\xi_2=a\xi_1$ gives

$$
\sigma(\xi_1)\sigma(a\xi_1)=\frac14.
$$

This diagnoses parity loss for odd-dilation models, not for all spacing methods.

## H10-M. Mellin--Perron dual-length diagnostic

**Status:** comparison lemma, not a no-go theorem.

A sharp Perron height near

$$
T\asymp X^{3/4}
$$

leads after functional equation and stationary phase to dual length

$$
n\lesssim T^2/X\asymp X^{1/2}
$$

and phase of type

$$
2\pi\sqrt{nX}.
$$

The exact contour theorem remains unwritten.

Counterexample checks to run:

1. **R5 Fejer product-count numerical test.**

For square, nonsquare, near-square, and divisor-rich $X$, compute

$$
\frac1{H_D}
\sum_{d\sim D}K_{H_D}(X/d)
$$

for several $D$, especially

$$
D\asymp X^{1/2}
$$

and

$$
D\asymp X^{3/8}.
$$

Compare with $X^{1/4}$.

2. **Second-leg shift test.**

Compute

$$
\frac1{H_D}
\sum_{d\sim D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\},
$$

and verify that divisibility/congruence spikes remain within $X^{1/4+\epsilon}$.

3. **Vaaler discontinuity test.**

At arguments where

$$
X/d\in\mathbb Z
$$

or

$$
\frac{X/d+\rho}{4}\in\mathbb Z,
$$

check that the Fejer majorant covers the discrepancy between the floor-compatible sawtooth value and the trigonometric polynomial.

4. **R5 full-block summation test.**

Verify that short blocks $D<X^{1/4}$, dyadic boundaries, both signs of $k$, zero modes, and both H3 legs sum to $O_\epsilon(X^{1/4+\epsilon})$.

5. **Li--Yang raw block audit.**

Record exact source constraints for Case A, Case B, the definition of $S$, the conditions on $F$, and the target $S/H$. Check both residual and main-term parameter substitutions.

6. **Li--Yang dissection map for main terms.**

Carry out an actual Bombieri--Iwaniec dissection for H5a-fix/H5b-fix. Determine effective parameters and identify exactly where the high-frequency gap persists.

7. **Main-term size numerics.**

For H5a-fix and H5b-fix, compute the fixed-coefficient sums with $\alpha_h$ for representative $X,D$. Compare against $X^{1/4}$ and against arbitrary-coefficient/L1 stress norms.

8. **Q1-Ext signed matrix test.**

Build a toy rational-collision matrix with entries retaining

$$
\chi_4(ab)(-1)^{\Delta/2}.
$$

Compare its spectral norm with the absolute-value matrix. Identify whether standard Cauchy--Schwarz erases the sign.

9. **C2-SP transition test.**

Numerically and symbolically test the regime

$$
kX/D^2\asymp 1
$$

where dual length is short and uniform stationary phase is delicate.

10. **Mellin--Perron comparison test.**

Write sharp and smoothed Perron errors with explicit $T$-dependence, apply the functional equation, and verify the dual length $T^2/X$ including boundary kernels.

Next round instructions:

## For `gpt_pro_thinking`

1. Write a complete proof of R5.

Include:

- exact Fejer-kernel pointwise bound;
- first-leg product-count proof;
- second-leg shifted proof with $4m-\rho$ congruence;
- divisor-bound summation;
- treatment of $X$ noninteger;
- constants absorbed by $X^\epsilon$;
- dyadic block summation;
- zero mode and both signs of $k$.

2. Verify H4 from a standard reference.

State the precise Vaaler theorem and the exact normalization of $K_H$. Do not rely on an informal "standard Vaaler" citation.

3. Insert R5 and R5-Full into the best proof draft.

Move H5r-F from "central bottleneck" to "cleared conditional on H4/R5 verification." Move H5r-B and H5r-L1 to optional stress-test status.

4. Formulate H5a-fix and H5b-fix as the official main-term targets.

Use the actual Vaaler coefficients $\alpha_h$, including signs and $1/h$ decay.

5. Compare H5a-fix/H5b-fix with Li--Yang.

Identify which subrange, if any, current Li--Yang technology covers, and isolate the high-frequency gap

$$
D X^{-\theta^*}
\lesssim H
\lesssim
D X^{-1/4}.
$$

## For `deepseek_api`

1. Run numerical R5 stress tests.

Compute first-leg and second-leg Fejer product-count sums for square, nonsquare, near-square, and divisor-rich $X$.

2. Verify the Li--Yang source constraints independently.

Record the exact TeX labels and the conditions used in LY-Raw-Mismatch and L9.1.

3. Audit possible main-term complete-sum mechanisms.

Check whether residue splitting, Gaussian integers, or complete sums modulo auxiliary moduli can create genuine character cancellation for H5a-fix/H5b-fix. Explicitly avoid invoking Weil/Deligne unless a genuine complete character sum with a nontrivial modulus is written.

4. Finish C2-SPU.

Provide uniform stationary-phase estimates for the odd-lattice Poisson transform, including short dual length and boundary stationary points.

## For `gemini_deep_think`

1. Insert Q1-Ext into an actual signed spacing matrix.

Determine whether the factor

$$
\chi_4(ab)(-1)^{\Delta/2}
$$

survives matrix norm estimates or is erased by absolute values.

2. Refine C3-Mult.

Analyze even dilations and more realistic rational/unimodular spacing transformations. Keep the conclusion diagnostic unless a full spacing model is proved.

3. Develop H10-M to theorem-dependency level.

Write exact sharp and smoothed Perron formulas for

$$
4\zeta(s)L(s,\chi_4),
$$

then derive the dual phase and length with all error terms.

4. Soften impossibility language.

Use "raw theorem mismatch," " diagnostic," and "unproved obstruction" unless a precise theorem is supplied.

## General state update

Update:

- `state/current_state.md`;
- `state/lemma_bank.md`;
- `state/gap_register.md`;
- `state/best_proof_draft.md`;
- `manifests/reading_packet.md`.

Record Round 9 as a progress round that likely clears the fixed Fejer residual and redirects attention to fixed-coefficient main sums. Preserve the no-exponent-improvement status.

Confidence:

High confidence in the selected route as the correct reduction framework.

High confidence that R5 is mathematically sound **conditional on the standard Fejer majorant H4**.

Moderate-to-high confidence that R5 clears H5r-F after the second leg and full dyadic summation are written carefully.

High confidence that H5r-B and H5r-L1 are overstrong and should not be active dependencies.

High confidence that Li--Yang cannot be quoted directly on the raw endpoint Vaaler block.

High confidence that Li--Yang's published exponent $\theta^*=0.314483\cdots$ does not supply the conjectural endpoint $1/4$.

High confidence in C2-Alg under the stated Fourier convention.

Moderate confidence in C2-SP0 leading stationary phase; low-to-moderate confidence in uniform C2-SPU until transition and boundary estimates are written.

Moderate confidence that Mellin--Perron reconstructs the Hardy/Voronoi/Bessel scale; low confidence that it gives an escape route without new moment or kernel estimates.

Moderate confidence that Q1-Ext is algebraically useful; low confidence that it gives analytic savings until tested in an actual spacing matrix.

Low confidence that current known technology proves H5a-fix/H5b-fix at the endpoint. The hard problem has moved from the residual to the fixed-coefficient main sums, not disappeared.
