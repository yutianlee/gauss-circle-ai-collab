Summary:
This is the Round 9 Stage B cross review of the Stage A outputs from `gemini_deep_think` and `deepseek_api`. Source packet:

Both agents correctly keep the balanced hyperbola/Vaaler route as a reduction and obstruction framework, not as a proof route. The main mathematical advance in the reviewed outputs is the theorem-level clarification that the raw H5r-F double sum at the endpoint block

$$
D\asymp X^{1/2},\qquad H_D\asymp D X^{-1/4}\asymp X^{1/4}
$$

does not fit the raw parameter hypotheses of Li--Yang's main exponential-sum theorem. This should be recorded as a serious false-proof guardrail, but not as an unconditional theorem that all Bombieri--Iwaniec/Li--Yang-style dissections fail. A full dissection could change the effective parameters, although present technology still only gives the Li--Yang exponent $\theta^*>1/4$, not the conjectural endpoint.

Most valuable input from others:

From `gemini_deep_think`:

1. **Li--Yang endpoint parameter clash.** Gemini correctly identifies the central numerical obstruction for a raw invocation of Li--Yang at the endpoint:
$$
   H_D\asymp X^{1/4}
$$
   while Case A gives
$$
   H\le M T^{-49/164}
$$
   and for $M\asymp X^{1/2}$, $T=X$, this is
$$
   H\le X^{1/2-49/164}=X^{33/164}\approx X^{0.2012}.
$$
   Case B is even more restrictive in the first upper bound:
$$
   H\le M^{35/69}T^{-2/23}\asymp X^{23/138}\approx X^{0.1667}.
$$
   This is a useful hard check against the false move "quote Li--Yang directly on H5r-F."

2. **Mellin--Perron dual-length diagnostic.** Gemini's H10-M computation correctly points toward the standard phenomenon: after applying the functional equation and stationary phase to the Perron integral for
$$
   4\zeta(s)L(s,\chi_4),
$$
   the saddle condition produces a dual phase of the form
$$
   2\pi\sqrt{nX}
$$
   and a dual length roughly
$$
   n\lesssim T^2/X.
$$
   If one chooses Perron height $T\asymp X^{3/4}$, this gives $n\lesssim X^{1/2}$, matching the Hardy/Voronoi/Bessel scale. This is valuable as a comparison diagnostic.

3. **Near-collision congruence bookkeeping.** Gemini's Q1-Ext is a useful algebraic lemma. For odd $d_1,d_2$ satisfying
$$
   d_1b-d_2a=\Delta,\qquad (a,b)=1,
$$
   the case $a,b$ both odd gives
$$
   \chi_4(d_1)\chi_4(d_2)=\chi_4(ab)(-1)^{\Delta/2}.
$$
   This is a genuine piece of signed matrix bookkeeping for future Bombieri--Iwaniec collision or near-collision analysis.

4. **Multiplicative parity-collapse test.** Gemini's C3-Mult observation is useful in the narrow setting where one models the two-coset dual coefficient by
$$
   \sigma(\xi)=\frac12(-1)^{2\xi},\qquad \xi\in \frac12\mathbb Z.
$$
   Under integer dilation $\xi_2=a\xi_1$, the coefficient product is
$$
   \sigma(\xi_1)\sigma(a\xi_1)
   =
   \frac14(-1)^{2\xi_1(1+a)}.
$$
   For odd $a$, this collapses to $1/4$. This is a valid algebraic diagnostic for one stylized spacing operation.

From `deepseek_api`:

1. **Exact C2 Poisson normalization.** DeepSeek gives the cleanest algebraic statement of the odd-lattice Poisson transform. With
$$
   e(t)=e^{2\pi i t},\qquad
   \widehat f(\xi)=\int_{\mathbb R}f(u)e(-\xi u)\,du,
$$
   and
$$
   f(u)=w_D(u)e(kX/u),
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
   This should be promoted as the official C2 algebraic transform.

2. **Correct stationary sign and scale separation.** For $\xi=-m<0$,
$$
   \widehat f(-m)=
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
   m\asymp kX/D^2.
$$
   DeepSeek also correctly separates the dual length
$$
   M_{\mathrm{dual}}\asymp kX/D^2
$$
   from the stationary-phase large parameter
$$
   \Lambda\asymp kX/D.
$$
   This distinction is essential for any uniform C2-SP lemma.

3. **Small-$k$ endpoint handling.** DeepSeek correctly observes that when
$$
   D\asymp X^{1/2},\qquad |k|\le X^\epsilon,
$$
   the dual length is $O(X^\epsilon)$ or smaller, so stationary phase is unnecessary. The primal trivial bound gives
$$
   |S_\star(k,D)|\ll D,
$$
   and after Vaaler normalization,
$$
   \frac{1}{H_D}|S_\star(k,D)|
   \ll
   \frac{D}{D X^{-1/4}}
   =
   X^{1/4}.
$$
   Thus $X^\epsilon$ many small frequencies remain harmless.

4. **More careful Li--Yang audit.** DeepSeek's audit is better calibrated than Gemini's. It distinguishes:
   - phase compatibility with Li--Yang's derivative hypotheses;
   - bounded-variation compatibility after residue splitting;
   - failure of raw Case A/Case B parameter ranges;
   - the need for a full Bombieri--Iwaniec dissection before invoking Li--Yang;
   - the fact that even after such a dissection, published technology gives $\theta^*>1/4$, not the endpoint.

Claims that look correct:

1. **Raw Li--Yang application fails at the endpoint block.**

With the raw identification
$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$
the endpoint H5r-F block violates both raw Case A and raw Case B frequency restrictions in Li--Yang's theorem. This is a correct and important guardrail.

2. **The H5r phases satisfy the derivative nondegeneracy condition.**

For
$$
F(z)=1/z,
$$
one has
$$
F'F'''-3(F'')^2=-6z^{-6}.
$$
For shifted/scaled variants such as
$$
F_{2,1}(z)=\frac{1}{z+1/D}
$$
and
$$
F_2(z)=\frac{1}{4z},
$$
the same nonvanishing structure remains on compact subintervals of $(0,\infty)$. Thus the obstruction is not phase smoothness or curvature in the Li--Yang sense; it is parameter range, norm, coefficient, and dissection structure.

3. **The parity indicator must be handled by residue splitting before any BV theorem.**

The raw function $1_{2\nmid d}$ is not a bounded-variation amplitude in Li--Yang's continuous $G(m/M)$ framework if inserted directly. After splitting $d=2n+1$, the parity is absorbed into the parametrization and the amplitude becomes smooth. This is the correct treatment.

4. **C2-Alg is correct.**

DeepSeek's odd-lattice Poisson formula reconciles the alternating representation and the two-coset representation. This should replace earlier informal versions of C2.

5. **The C2 stationary phase has active sign $\xi<0$.**

With the convention
$$
\widehat f(\xi)=\int f(u)e(-\xi u)\,du,
$$
the stationary phase for $e(kX/u-\xi u)$ occurs when $\xi<0$. Writing $\xi=-m$, $m>0$, gives
$$
u_0=\sqrt{kX/m}.
$$

6. **The leading C2 amplitude scale is correct.**

In the interior range
$$
m\asymp kX/D^2,
$$
the leading size is
$$
|\widehat f(-m)|\asymp D^{3/2}(kX)^{-1/2}.
$$
The exact error term still needs a uniform proof, but the main scale is right.

7. **R4 remains a central diagnostic.**

The Fejer identity
$$
\sum_{k=1}^{H}\left(1-\frac{k}{H+1}\right)a_k
=
\frac1{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j}a_k
$$
shows that any proof of H5r-F using only partial-sum bounds risks collapsing into H5r-B-type difficulty. This is not an equivalence theorem, but it is a serious methodological warning.

8. **Mellin--Perron likely reconstructs the Hardy/Voronoi/Bessel scale.**

The dual-length computation
$$
n\lesssim T^2/X
$$
after functional equation and stationary phase is a sound diagnostic. It supports keeping Mellin--Perron as a comparison route, not as an immediate escape from H5r.

Claims that need proof:

1. **That Li--Yang-derived methods cannot handle H5r-F after dissection.**

The raw parameter mismatch is proved. The stronger claim that current reciprocal-sum spacing technology "mathematically cannot evaluate" H5r-F is not proved until the full Bombieri--Iwaniec dissection is carried out with the Fejer weights and residual norms. The correct present status is:

$$
\text{raw Li--Yang theorem does not apply}
$$

not

$$
\text{all Li--Yang/Bombieri--Iwaniec technology is impossible here}.
$$

2. **That restricting $H$ to $X^{33/164}$ permanently forces exponent $0.2988$.**

Gemini's calculation
$$
X^{1/2}/X^{33/164}=X^{49/164}\approx X^{0.2988}
$$
is correct for the zero mode under a naive restriction of the local Vaaler height. But this is only a diagnostic for that truncation choice. It is not a theorem excluding alternative truncations, signed remainders, smoothing, or a different treatment of the fixed Fejer residual.

3. **Uniform C2-SP error term.**

DeepSeek's leading stationary-phase term is reliable, but the error
$$
O\bigl((kX)^{-1}D^{3/2}\bigr)
$$
should not be promoted without proof. A uniform lemma must distinguish:
$$
\Lambda\asymp kX/D,\qquad M_{\mathrm{dual}}\asymp kX/D^2,
$$
and handle:
- $M_{\mathrm{dual}}\asymp 1$;
- stationary points near support boundaries;
- nonstationary tails;
- dependence on derivatives of $w_D$.

4. **Mellin--Perron height necessity.**

The statement "targeting $X^{1/4}$ necessitates Perron height $T\asymp X^{3/4}$" is plausible for sharp Perron with standard coefficient bounds, but not yet theorem-level for smoothed Perron. Smoothed kernels, moment estimates, and contour choices can alter the truncation-error bookkeeping. Record the $T\asymp X^{3/4}$ calculation as sharp-Perron diagnostic, not as a universal necessity.

5. **H10-M as an exact equivalence.**

Gemini's H10-M should be demoted from "proved algebraic diagnostic mapping" if interpreted globally. What is proved is the saddle-point scale and phase under standard contour/functional-equation analysis. The exact theorem still needs:
- the precise completed functional equation for $4\zeta(s)L(s,\chi_4)$;
- residue extraction at $s=1$;
- smoothing kernel;
- treatment of horizontal and transition contributions;
- coefficient normalization in the dual sum.

6. **C3-Mult beyond integer dilations.**

Gemini proves collapse for odd integer dilations $a$. If the spacing relation uses rational slopes or matrix transformations not preserving $\frac12\mathbb Z$ in the same way, the lemma must be restated with the exact arithmetic domain. Even for even integer dilations, Gemini's statement that they "fail to lower the square-root degree of the phase" is not proved.

7. **Q1-Ext analytic usefulness.**

Q1-Ext is algebraically correct, but no saving follows until it is inserted into an actual near-collision or spacing matrix before absolute values erase the sign. The next step must build a toy matrix or a genuine Bombieri--Iwaniec off-diagonal expression retaining
$$
\chi_4(ab)(-1)^{\Delta/2}.
$$

8. **Fejer spike severity.**

Both agents treat Fejer spikes as a serious stress-test, correctly. But no lower bound or numerical result shows that spikes force H5r-F above $X^{1/4+\epsilon}$. The spike issue should remain a numerical and analytic stress test, not a proven obstruction.

Possible errors or hidden assumptions:

1. **Gemini overstates the Li--Yang obstruction.**

The phrase "current reciprocal-sum spacing theorems mathematically cannot evaluate the upper-frequency range" is too strong. The raw theorem with $M=D$, $H=H_D$ fails, but Li--Yang's actual proof pipeline involves dissection before theorem application. The correct conclusion is:

$$
\text{Direct quotation of Li--Yang on raw H5r-F is invalid.}
$$

A stronger no-go statement requires carrying through the dissection and showing that all resulting effective blocks remain outside the valid range or only yield $\theta^*$.

2. **Gemini's BV penalty is partly misleading.**

It is true that inserting $1_{2\nmid d}$ directly as a continuous $G$ creates an unacceptable variation issue. But the correct approach is to split into residue classes. After $d=2m+1$, the amplitude is smooth/BV and no $O(D)$ variation loss is intrinsic. Thus the "BV penalty" is a false-proof warning, not an obstruction after proper residue splitting.

3. **Gemini uses too much equivalence/isomorphism language for Mellin--Perron.**

The saddle calculation strongly suggests that Mellin--Perron returns to Voronoi/Bessel-type sums of length $X^{1/2}$, but "strictly limit" and "analytic isomorphism" are too strong without the complete contour theorem.

4. **Gemini's C3-Mult may not model the actual spacing transformation.**

Odd/even integer dilation is only one stylized operation. Bombieri--Iwaniec spacing matrices involve rational approximations and unimodular transformations; the parity coefficient may transform in a less elementary way. C3-Mult is a useful diagnostic, not a substitute for a matrix-level analysis.

5. **DeepSeek did not actually run the numerical tests.**

The assigned task included numerical tests comparing H5r-F, H5r-B, and H5r-L1. DeepSeek supplied a good test plan but no data. This is acceptable as a planning contribution, but it should not be scored as execution.

6. **DeepSeek's H5r-F compatibility with Li--Yang needs dyadic decomposition.**

Li--Yang's sum is over $H\le h\le 2H$ with a BV amplitude on $[1,2]$. H5r-F is a full triangular sum over $1\le |k|\le H_D$. To compare them line by line, one must decompose into dyadic $K\le H_D$ blocks and define
$$
g_K(k/K)=\eta_{k,H_D}
$$
on each block. The variation on each block is harmless, but this step should be explicit.

7. **DeepSeek's C2-SP error estimate is not yet validated.**

The leading constant and phase are plausible, but the stated error should not enter the lemma bank as proved. The repo should mark C2-SP as "leading term and scales checked; uniform stationary phase pending."

8. **Both agents risk confusing structural compatibility with theorem-level applicability.**

For H5r, the derivative hypotheses are easy. The hard questions are:
- allowed outer weights;
- fixed Fejer average versus dyadic arbitrary coefficients;
- blockwise absolute values;
- residue/parity coefficients;
- whether the theorem estimates $S$ or $S/H$ in the exact norm needed;
- whether the endpoint range $H_D\asymp X^{1/4}$ is reachable after all reductions.

Suggested synthesis:

1. **Promote the raw Li--Yang mismatch as a guardrail, not a no-go theorem.**

Add lemma:

**LY-Raw-Mismatch.**
For the raw H5r-F endpoint block
$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$
the raw double sum does not satisfy Li--Yang Case A or Case B. Specifically:
$$
H_D=X^{1/4}>X^{33/164}=M T^{-49/164}
$$
and
$$
H_D=X^{1/4}>X^{23/138}=M^{35/69}T^{-2/23}.
$$
Therefore Li--Yang's main theorem cannot be quoted directly on the raw Vaaler residual block.

Status: proved guardrail.

Add warning: this does not preclude a full Bombieri--Iwaniec dissection; it only blocks raw theorem invocation.

2. **Use DeepSeek's C2-Alg as the official C2 lemma.**

Record:

**C2-Alg.**
For $f(u)=w_D(u)e(kX/u)$ and $\widehat f(\xi)=\int f(u)e(-\xi u)\,du$,
$$
\sum_{2\nmid d}f(d)
=
\frac12\sum_{m\in\mathbb Z}\widehat f(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
$$

Status: proved algebraic lemma under the stated Fourier convention.

3. **Split C2-SP into leading-term and uniform versions.**

Record:

**C2-SP0.**
For $m>0$ with $m\asymp kX/D^2$,
$$
\widehat f(-m)
\sim
\frac{w_D(\sqrt{kX/m})}{\sqrt{2m/\sqrt{kX/m}}}
e(2\sqrt{kXm}+1/8),
$$
so
$$
|\widehat f(-m)|\asymp D^{3/2}(kX)^{-1/2}.
$$

Status: leading stationary phase accepted.

Then create a separate target:

**C2-SPU.**
Uniform stationary phase with boundary, nonstationary, and $M_{\mathrm{dual}}\asymp 1$ transition estimates.

Status: required, not proved.

4. **Demote H10-M to diagnostic comparison.**

Keep the saddle relation:
$$
t_0\asymp \sqrt{nX},\qquad n\lesssim T^2/X.
$$
If $T\asymp X^{3/4}$, then $n\lesssim X^{1/2}$. But do not call Mellin--Perron an exact isomorphism until the contour and functional-equation proof is written.

5. **Keep Q1-Ext as an algebraic input for signed spacing matrices.**

Promote Q1-Ext as an algebraic lemma, but add a dependency:

To become analytically useful, Q1-Ext must be inserted into an off-diagonal spacing expression before Cauchy--Schwarz or matrix norm bounds replace signs by absolute values.

6. **Keep C3-Mult as a narrow diagnostic.**

C3-Mult should be recorded as:

For the model coefficient $\sigma(\xi)=\frac12(-1)^{2\xi}$ on $\frac12\mathbb Z$, odd integer dilation collapses the coefficient product to a constant. This diagnoses one class of parity-loss mechanisms. It does not rule out general two-coset spacing methods.

7. **Make the next round computationally concrete.**

The highest-value empirical task remains the H5r norm comparison:
$$
R_F(D)=
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|,
$$
versus
$$
R_{L1}(D)=
\frac1{H_D}
\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$
This is the fastest way to test whether fixed Fejer averaging is materially easier than H5r-B/L1.

Score by agent:

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|---|---:|---|---|
| `gemini_deep_think` | 7.6 | Valuable high-level obstruction synthesis: raw Li--Yang frequency clash, Mellin--Perron dual-length diagnostic, Q1-Ext congruence bookkeeping, and C3-Mult parity test. Main weakness is overstatement: raw theorem mismatch is treated too close to a global no-go theorem, BV parity loss is overstated before residue splitting, and Mellin--Perron/C3 language is too strong for the proofs supplied. | Convert LY-Audit into a precise raw-mismatch lemma only; demote H10-M and C3-Mult to diagnostics; insert Q1-Ext into an actual signed spacing matrix before claiming analytic value. |
| `deepseek_api` | 8.5 | Strongest technical output: exact C2 Poisson normalization, correct two-coset/alternating reconciliation, reliable leading stationary-phase constants, small-$k$ boundary handling, and a more careful Li--Yang theorem-level audit distinguishing structural compatibility from raw parameter failure. Main weakness is that numerical tests were planned rather than run, and C2-SP uniform errors remain unproved. | Run the H5r-F/H5r-B/H5r-L1 numerical tests; write dyadic Fejer-to-Li--Yang normalization explicitly; prove or qualify the uniform C2-SP error term and boundary transition. |

Next-round recommendation:

1. **Do not pivot away from H5r-F.** The central target remains the fixed-Fejer residual. The next round should decide whether it is genuinely easier than H5r-B/L1 or only cosmetically weaker.

2. **Run the numerical H5r norm comparison.** This is the highest-priority concrete action. Use square, nonsquare, and near-square $X$; test both $D\asymp X^{1/2}$ and $D\asymp X^{3/8}$; report $R_F$, $R_{L1}$, and dyadic $L^1$ norms for $S_{\mathrm{odd}}$ and $S_\rho$.

3. **Add LY-Raw-Mismatch as a proved guardrail.** State explicitly that Li--Yang cannot be quoted directly on the raw endpoint H5r-F block. Also state explicitly that this does not prove failure after full Bombieri--Iwaniec dissection.

4. **Write the full Bombieri--Iwaniec dissection map for H5r-F.** The next analytic task is not another raw parameter comparison. It is to choose the dissection length, derive the effective $M,H,T,N,K,L$ parameters, and determine whether the Li--Yang theorem applies after dissection and what exponent it returns.

5. **Promote C2-Alg and split C2-SP.** C2-Alg should enter the lemma bank as proved. C2-SP should be split into a leading interior stationary-phase lemma and a separate uniform transition lemma.

6. **Keep Mellin--Perron as comparison only.** The next Mellin--Perron work should write exact sharp and smoothed Perron errors, then derive the dual length after the functional equation. Avoid calling it circular or isomorphic until the full contour argument is explicit.

7. **Test Q1-Ext inside a signed matrix.** Construct a toy near-collision sum retaining
$$
\chi_4(ab)(-1)^{\Delta/2}
$$
and identify the exact step where standard Cauchy--Schwarz or matrix norm methods erase the sign. This will show whether Q1-Ext is merely decorative or a possible source of new cancellation.

8. **Maintain the no-exponent-improvement status.** Round 9 supplies useful obstruction mapping and theorem-audit precision, but it proves no new Gauss circle bound.
