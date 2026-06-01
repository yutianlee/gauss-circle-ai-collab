Summary:

Round 10 is a genuine precision round, not an exponent-improvement round. Source anchor: uploaded Round 10 packet and agent outputs; background overview packet.

The main state update is:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

where H1--H3 are the proved balanced hyperbola/sawtooth reductions, H4 is the finite Vaaler theorem with Fejer residual majorant, R5-Full is the total Fejer residual bound, and M9 is the pair of fixed-Vaaler-coefficient main-term estimates.

Round 10 strongly supports moving the fixed Fejer residual H5r-F off the critical path, conditional on a page-level verification of H4 and a complete write-up of R5-Full. The remaining hard problem is now sharply isolated as the fixed-coefficient Vaaler main sums. No new Gauss circle exponent has been proved.

Selected main route:

Keep the balanced arithmetic hyperbola/Vaaler reduction as the primary framework:

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

The proved arithmetic identity remains:

$$
P(X)
=
-4\sum_{a\le y}\chi_4(a)\psi(X/a)
+
4\sum_{b\le y}
\left[
\psi\left(\frac{X/b+1}{4}\right)
-
\psi\left(\frac{X/b+3}{4}\right)
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

For each dyadic block $d\asymp D$ in

$$
X^{1/4}\le D\le X^{1/2},
$$

use the local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Short blocks $D<X^{1/4}$ remain trivially bounded by $O(X^{1/4})$ after summing over dyadic ranges.

The selected proof skeleton after Round 10 is:

1. Apply H4 blockwise to the two sawtooth legs.
2. Bound all Fejer residuals directly by R5 product-counting, not by arbitrary $k$-coefficient reciprocal sums.
3. Reduce the conjectural bound to the fixed main-term estimates M9:

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_{d\sim D}
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_{d\sim D}
w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the second main term may be written as

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\sim D}
w_D(d)e(hX/(4d)).
$$

The target is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over dyadic $D$, with logarithmic losses absorbed into $X^\epsilon$.

Useful fragments by source:

## From `gpt_pro_thinking`

The main useful contribution is the complete lemma-level R5 proof and residual bridge.

The required Vaaler theorem was stated in the precise form needed for the repo. With

$$
e(t)=e^{2\pi i t},
$$

define

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2.
$$

Let

$$
\Phi(u)=\pi u(1-|u|)\cot(\pi u)+|u|,
\qquad
0<|u|<1,
$$

with continuous extension $\Phi(0)=1$. The required imported theorem is:

$$
\psi(t)
=
-\sum_{1\le |h|\le H}
\frac{\Phi(h/(H+1))}{2\pi i h}e(ht)
+
R_H(t),
$$

with

$$
|R_H(t)|\le \frac1{2H+2}K_H(t).
$$

Thus

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h},
\qquad
|\alpha_{h,H}|\ll |h|^{-1}.
$$

This theorem still needs a page-level source audit, especially for the constant, coefficient convention, and discontinuity value $\psi(n)=-1/2$.

The R5 proof uses the standard pointwise Fejer bound

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right),
$$

hence

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg,

$$
\frac1H
\sum_{d\sim D}
K_H(X/d),
$$

choose $m$ nearest to $X/d$. For $d\asymp D$,

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

the summand is bounded by

$$
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by $n=md$ gives at most $\tau(n)$ representations, so

$$
\frac1H\sum_{d\sim D}K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The last estimate uses

$$
\tau(n)\ll_\epsilon n^\epsilon
$$

and

$$
\sum_{n\in\mathbb Z}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll \Delta+1.
$$

This is uniform for real $X$.

For the second residual leg,

$$
\frac1H
\sum_{d\sim D}
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad \rho\in\{1,3\},
$$

near-integrality is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing

$$
\ell=4m-\rho
$$

again gives a product $n=d\ell$ with only a congruence restriction on $\ell$, so the ordinary divisor bound still applies. This is the correct mechanism for clearing the shifted second leg.

The second important contribution is the replacement of the old arbitrary-coefficient H5a/H5b by fixed-coefficient M9. This prevents the repo from requiring a stronger theorem than the actual Vaaler reduction needs.

The third useful contribution is the careful Li--Yang comparison. H5a-fix is structurally compatible with Li--Yang/Bombieri--Iwaniec reciprocal phases after splitting $d\bmod 4$, but the published theorem does not reach the endpoint Vaaler height. H5b-fix also has an additional theorem-extension gap because $\chi_4(h)$ either gives a non-smooth periodic $h$-weight or, after splitting $h\bmod 4$, a shifted-frequency phase $e((q+\beta)X/d)$.

## From `deepseek_api`

The strongest useful contribution is independent verification of R5 and the Li--Yang source audit.

DeepSeek confirmed the R5 product-count mechanism for both legs and correctly emphasized that H5r-F is provisionally cleared only after H4 is source-verified and R5-Full is written into the proof draft.

DeepSeek also extracted the relevant Li--Yang parameter mismatch. In the raw endpoint block,

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H=H_D\asymp X^{1/4}.
$$

Li--Yang Case A imposes

$$
H\le MT^{-49/164}=X^{33/164}\approx X^{0.2012},
$$

and Case B imposes

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}=X^{1/6}.
$$

Both are below $X^{1/4}$. Therefore Li--Yang cannot be quoted directly on the raw endpoint Vaaler block. This is a theorem-application guardrail, not a no-go theorem for every possible Bombieri--Iwaniec dissection.

DeepSeek also kept C2-SPU in the correct status: the leading stationary-phase scale is understood, but the uniform lemma is not fully proved. For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

the active sign is $\xi<0$. Writing $\xi=-m$, the stationary point is

$$
u_0=\sqrt{\frac{kX}{m}},
$$

and the active dual length is

$$
m\asymp \frac{kX}{D^2}.
$$

The leading size in the interior is

$$
|I(-m)|\asymp D^{3/2}(kX)^{-1/2}.
$$

Uniform boundary, transition, and nonstationary estimates are still missing.

## From `gemini_deep_think`

The most useful contribution is Q1-Spectral, the operator-norm character-blindness diagnostic.

For a spacing matrix

$$
K_{d_1,d_2}
=
\sum_h e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right),
$$

the spatial character enters through the test vector

$$
v_d=\chi_4(d)w_D(d).
$$

On odd $d$, multiplication by $\chi_4(d)$ is a diagonal unitary operator $U$. Thus

$$
v^*Kv
=
w^*(U^*KU)w,
$$

but

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Therefore any method that bounds the signed quadratic form only through an operator norm, Schur bound, Gershgorin-type bound, or absolute-value matrix cannot exploit the diagonal $\chi_4$ signs. This is an important guardrail for future spacing arguments.

This should be recorded as a diagnostic, not as an impossibility theorem. It does not rule out signed bilinear estimates, trace/cycle estimates, residue-interference methods, or a Bombieri--Iwaniec dissection that estimates the signed form directly.

Gemini also contributed useful C3 parity diagnostics. Integer translations in the two-coset odd-lattice model erase parity oscillation:

$$
\sigma(\xi)=\frac12(-1)^{2\xi},
\qquad
\sigma(\xi)\sigma(\xi+q)=\frac14
$$

for integer $q$, up to the fixed convention. But the rational-dilation variants need to be rewritten carefully and connected to actual spacing transformations before they become proof-relevant.

Gemini's Mellin--Perron analysis should be kept as a comparison module. The contour/functional-equation route appears to reconstruct Hardy--Voronoi--Bessel phases of type

$$
2\pi\sqrt{nX}
$$

with dual length about

$$
n\lesssim T^2/X.
$$

For endpoint smoothing/truncation with $T\asymp X^{3/4}$ this gives dual length $X^{1/2}$. This is a useful diagnostic that Mellin--Perron likely mirrors known oscillatory difficulty, but it is not yet a theorem-level equivalence.

## From Stage B reviews

The cross-reviews agree on the main synthesis:

- R5 is the principal Round 10 mathematical advance.
- H5r-F should be demoted from active central bottleneck to provisionally cleared residual input.
- H5r-B and H5r-L1 should be retained only as stress tests.
- M9 fixed-coefficient main terms are now the hard target.
- Li--Yang cannot be used as a black box on the raw endpoint block.
- Q1-Spectral is valuable but must be phrased as an operator-norm-only diagnostic.
- No exponent improvement has been proved.

Rejected or risky ideas:

1. **Reject any claim of a new Gauss circle exponent.**

Round 10 clears or nearly clears the residual side of the Vaaler reduction, but the fixed-coefficient main sums M9 remain open. Therefore the conjectural estimate

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

has not been proved.

2. **Reject marking R5 as fully unconditional before H4 is source-verified.**

The product-counting proof is strong, but its use in the sawtooth approximation depends on H4. The exact Vaaler theorem, coefficient normalization, Fejer-kernel normalization, and discontinuity convention must be cited from a standard source.

3. **Reject keeping H5r-B and H5r-L1 as active dependencies.**

Those arbitrary-coefficient or termwise $L^1$ residual targets are stronger than what the Vaaler proof actually needs. R5 controls the positive Fejer majorant directly. H5r-B and H5r-L1 should remain stress tests only.

4. **Reject a black-box Li--Yang invocation at the endpoint.**

The raw endpoint Vaaler block violates the audited Case A/B height bounds. Structural phase compatibility is insufficient.

5. **Reject a global no-go theorem for Bombieri--Iwaniec/Li--Yang methods.**

The raw theorem mismatch is proved only for direct application. A full dissection could alter effective parameters, and a future first-spacing or signed-spacing input could change the situation. Do not state that all spacing methods fail.

6. **Reject overstrong Q1-Spectral language.**

Q1-Spectral shows that operator-norm-only arguments are character-blind. It does not prove that every signed spacing or trace method loses the character.

7. **Reject treating H5b-fix as automatically covered by H5a-fix technology.**

H5b-fix places $\chi_4$ in the frequency variable. Splitting $h\bmod 4$ creates shifted frequencies $q+\beta$, $\beta\in\{1/4,3/4\}$. A theorem permitting such fixed fractional shifts must be stated or proved.

8. **Reject treating signed Fourier truncation as an established escape.**

The high-frequency signed tail may preserve signs formally, but near discontinuities it appears to produce small-denominator barriers comparable to Fejer. No endpoint tail estimate has been proved.

9. **Reject Mellin--Perron "isomorphism" or "circular trap" as theorem-level.**

The saddle computation is valuable, but exact sharp/smoothed Perron errors, functional equation normalization, kernel estimates, and transition analysis are not yet written.

10. **Reject treating C2-SPU as proved.**

The leading stationary point and amplitude are accepted, but the uniform stationary-phase lemma with support-boundary and short-dual-length transitions remains open.

Known gaps:

1. **H4 source and convention audit.**

Need a precise citation for:

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H(t),
$$

with

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h}
$$

or the equivalent standard convention, and

$$
|R_H(t)|\le \frac1{2H+2}K_H(t)
$$

or another explicitly normalized $O(H^{-1}K_H)$ bound.

The source audit must verify that the floor-compatible convention $\psi(n)=-1/2$ is covered by the residual.

2. **R5-Full write-up gap.**

The proof draft must explicitly cover:

- first leg $K_H(X/d)$;
- second leg $K_H((X/d+1)/4)$ and $K_H((X/d+3)/4)$;
- integer and noninteger $X$;
- nearest-integer choices;
- possible small or finite endpoint cases;
- the zero Fejer mode;
- both signs of $k$;
- dyadic partitions with possibly signed weights, handled by $|w_D|$;
- short blocks $D<X^{1/4}$;
- absorption of $O(\log X)$ dyadic losses into $X^\epsilon$.

3. **Terminology gap: H5r-F versus direct Fejer-majorant bound.**

Earlier H5r-F was phrased as a fixed Fourier average over $k$. R5 bypasses that formulation by bounding the positive Fejer kernel directly. The proof draft should say explicitly that the residual is controlled by R5-Full; it need not continue treating H5r-F as an independent Fourier-sum target.

4. **M9 main-term estimates are open.**

The official target is now:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

No agent supplied an endpoint proof for these sums.

5. **H5b-fix shifted-frequency theorem gap.**

After splitting $h\bmod 4$,

$$
\chi_4(h)e(hX/(4d))
$$

leads to sums with phase

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\}.
$$

A Bombieri--Iwaniec/Li--Yang theorem with this fixed fractional shift must be stated and verified, or this remains a separate obstruction.

6. **Li--Yang high-frequency gap.**

Known Li--Yang technology reaches a record exponent

$$
\theta^*=0.314483\cdots
$$

in the relevant $X$-notation, not the conjectural $1/4$. The endpoint Vaaler range requires

$$
H\le D X^{-1/4},
$$

while the final record-exponent range only reaches approximately

$$
H\le D X^{-\theta^*}.
$$

At $D\asymp X^{1/2}$, this leaves the gap

$$
X^{0.1855\cdots}
\lesssim H
\lesssim
X^{1/4}.
$$

The raw Case A/B restrictions are even more restrictive and must be kept distinct from this final-record range.

7. **Q1-Spectral exact-matrix gap.**

The diagonal-unitary argument must be attached to the actual spacing matrix used in a Bombieri--Iwaniec or large-sieve step. If the method already takes absolute values earlier, the result is even more directly character-blind; if not, a signed-form estimate may still be possible.

8. **Signed trace/cycle route undeveloped.**

The proposed escape route should define an actual signed spacing matrix and a concrete statistic, for example a trace or fourth moment, in which products of $\chi_4$ survive closed cycles. No such lemma has yet been proved.

9. **C2-SPU uniform stationary phase.**

Need a theorem covering:

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

including active sign, stationary point, leading phase, amplitude, nonstationary decay by integration by parts, support-boundary transitions, and short-dual-length cases.

10. **Mellin--Perron and signed Fourier comparison gaps.**

Both routes remain comparison tools. They need exact replacement error terms before they can be judged as genuine alternatives.

11. **Numerical data are still absent.**

The repo has test plans but not committed numerical output for R5, Fejer spikes, second-leg shifts, M9 fixed-coefficient sums, Q1-Spectral matrix norms, or C2 stationary phase.

New lemmas to add:

## H4. Vaaler finite approximation with Fejer residual

**Status:** external theorem dependency; statement precise, source normalization pending.

For $H\ge1$,

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H(t),
$$

where

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h},
\qquad
|\alpha_{h,H}|\ll |h|^{-1},
$$

and

$$
|R_H(t)|\le \frac1{2H+2}K_H(t).
$$

The exact coefficient function and constant must be source-verified.

## R5. Fejer product-count residual bound

**Status:** provisionally proved conditional on H4; promote after H4 and R5-Full write-up.

Let $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp D X^{-1/4}$, and let $|w_D|\le1$ be supported on $d\asymp D$. Then

$$
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H
\sum_{d\sim D}
|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof dependencies: Fejer pointwise bound and $\tau(n)\ll_\epsilon n^\epsilon$.

## R5-Full. Total Vaaler residual bound

**Status:** conditional bridge lemma; write into best proof draft.

Assume H4 and R5 on every dyadic block. Then the full Vaaler residual contribution in H3 is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

This includes both sawtooth legs, both shifts $\rho=1,3$, zero modes, both signs of frequency, and short dyadic blocks.

## M9. Fixed-coefficient main-term criterion

**Status:** official remaining main analytic target.

Let

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

Define $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ as above. If for every dyadic $D$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon},
$$

then H1--H4 plus R5-Full imply

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

## H5r-B/H5r-L1 demotion

**Status:** stress tests only.

The arbitrary-coefficient and termwise-$L^1$ residual targets are no longer active proof dependencies unless R5 fails. They remain useful for numerical comparison and for detecting whether fixed Fejer structure is essential.

## LY-Raw-Mismatch

**Status:** proved theorem-application guardrail.

For the raw endpoint block

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$

Li--Yang Case A allows at most

$$
H\le MT^{-49/164}=X^{33/164},
$$

and Case B allows at most

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}.
$$

Both are below $X^{1/4}$. Therefore the audited theorem cannot be quoted directly for the raw endpoint Vaaler block.

## LY-Endpoint-Gap

**Status:** diagnostic.

The final record-exponent range associated with Li--Yang reaches only

$$
H\le D X^{-\theta^*},
\qquad
\theta^*=0.314483\cdots,
$$

whereas the conjectural Vaaler endpoint requires

$$
H\le D X^{-1/4}.
$$

The uncovered high-frequency range is

$$
D X^{-\theta^*}
\lesssim H
\lesssim
D X^{-1/4}.
$$

This is not a no-go theorem.

## M9a-LY-Dictionary

**Status:** structural compatibility only.

After splitting $d\bmod4$, H5a-fix becomes a difference of reciprocal sums with smooth residue-class weights and phase

$$
e\left(\frac{hX}{4m+r}\right),
\qquad r\in\{1,3\}.
$$

This fits the broad reciprocal phase class, but endpoint theorem applicability is not established.

## M9b-Shift

**Status:** required theorem-extension gap.

After splitting $h\bmod4$, H5b-fix contains shifted-frequency phases

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\}.
$$

A theorem allowing these fixed fractional shifts in the relevant spacing framework must be proved or cited.

## Q1-Spectral

**Status:** proved diagnostic for operator-norm-only methods.

If the $\chi_4(d)$ signs enter only through a diagonal unitary conjugation of a spacing matrix, then estimates depending only on the operator norm cannot exploit those signs:

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

This blocks character gains from operator-norm-only or absolute-value spacing estimates, but not from signed-form or trace/cycle estimates.

## H12. Signed spacing trace target

**Status:** proposed next route.

Define an actual signed spacing matrix $K^\chi$ arising from M9a, retaining the factor

$$
\chi_4(d_1)\chi_4(d_2).
$$

Formulate a trace or fourth-moment statistic, such as a signed analogue of $\operatorname{Tr}((KK^*)^2)$, and determine whether Q1-Ext signs survive closed collision cycles before absolute values are taken.

## C2-SPU. Uniform odd-lattice stationary phase

**Status:** required technical lemma, not proved.

For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

prove uniform estimates in all regimes, including

$$
|\xi|\asymp kX/D^2,
$$

nonstationary ranges, support-boundary transitions, and short-dual-length cases.

## H10-M. Mellin--Perron comparison module

**Status:** comparison route, not an escape.

A sharp or smoothed Perron formulation for

$$
4\zeta(s)L(s,\chi_4)
$$

should be developed far enough to show precisely which dual sums and kernels arise after the functional equation. Current saddle analysis suggests Hardy--Voronoi--Bessel phases, not an easier endpoint problem.

## SF1-Tail. Signed Fourier tail comparison

**Status:** diagnostic only.

For the formal signed tail after truncating

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi i h},
$$

derive a rigorous bound such as

$$
\left|\sum_{|h|>H}\frac{e(ht)}{h}\right|
\ll \frac{1}{H\|t\|}
$$

away from discontinuities, then compare the resulting $d$-sum with the Fejer residual. Do not claim equivalence until the discontinuity and summability conventions are fixed.

Counterexample checks to run:

1. **R5 first-leg numerical stress test.**

For square, nonsquare, near-square, and divisor-rich $X$, compute

$$
\frac1{H_D}
\sum_{d\sim D}K_{H_D}(X/d)
$$

for $D\asymp X^{1/4}$, $X^{3/8}$, and $X^{1/2}$.

2. **R5 second-leg shift test.**

For $\rho\in\{1,3\}$, compute

$$
\frac1{H_D}
\sum_{d\sim D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right),
$$

especially when $X\approx d(4m-\rho)$ has many product representations.

3. **Vaaler discontinuity test.**

Test cases where

$$
X/d\in\mathbb Z
$$

or

$$
\frac{X/d+\rho}{4}\in\mathbb Z.
$$

Verify that the residual majorant covers the discrepancy between the floor-compatible sawtooth convention and the trigonometric approximation.

4. **R5-Full dyadic summation test.**

Check full summation over all dyadic $D$, including $D<X^{1/4}$, dyadic boundary overlaps, both sawtooth legs, and both signs of the Fejer frequencies.

5. **M9 fixed-coefficient numerics.**

Compute

$$
\mathcal M_1(D;X)
$$

and

$$
\mathcal M_2(D;X)
$$

with the actual Vaaler coefficients $\alpha_{h,H_D}$. Compare against $X^{1/4}$ and against arbitrary-coefficient or $L^1$ stress norms.

6. **H5b shifted-frequency test.**

Numerically and symbolically compare sums with phases

$$
e(qX/d)
$$

and

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\}.
$$

Identify which steps of a Bombieri--Iwaniec dissection are invariant under the shift and which are not.

7. **Li--Yang theorem audit.**

Record exact TeX labels, hypotheses, and parameter substitutions for the theorem. Distinguish raw Case A/B height restrictions from the final record-exponent range.

8. **Q1-Spectral matrix test.**

Construct the actual near-collision kernel

$$
K_{d_1,d_2}
=
\sum_{1\le |h|\le H_D}
|\alpha_h|^2
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right)
$$

or the precise kernel generated by the intended Cauchy--Schwarz step. Compare bounds for $K$ and $U^*KU$.

9. **Signed trace/cycle toy model.**

Compute a toy fourth-moment or trace statistic retaining

$$
\chi_4(d_1)\chi_4(d_2)
$$

and test whether Q1-Ext signs survive beyond absolute-value majorization.

10. **C2-SPU transition test.**

Test numerically and symbolically the regimes

$$
kX/D^2\asymp 1,
$$

stationary point near support boundary, and nonstationary tails.

11. **Mellin--Perron comparison test.**

Write sharp and smoothed Perron errors with explicit $T$-dependence, apply the functional equation for $4\zeta(s)L(s,\chi_4)$, and verify the dual length $T^2/X$ and phase $2\pi\sqrt{nX}$ including transition kernels.

12. **Signed Fourier tail test.**

Compare the signed Fourier tail with the Fejer majorant for arguments close to integers. Determine whether sign preservation survives summation over $d$ or whether the same product-count/small-denominator structure reappears.

Next round instructions:

## For `gpt_pro_thinking`

1. Verify H4 from a standard reference.

State the exact theorem with coefficient function, Fejer kernel normalization, residual constant, and sawtooth convention. Do not rely on an informal "standard Vaaler" citation.

2. Write R5-Full as a complete proof in the best proof draft.

Include first leg, shifted second leg, real $X$, endpoint cases, dyadic partitions, zero mode, both frequency signs, short blocks, and absorption of logarithms.

3. Insert the Round 10 bridge theorem:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

4. Freeze M9 as the official main-term target.

Use the exact $\alpha_{h,H_D}$ coefficients and do not revert to arbitrary $u_h$ unless explicitly running a stress test.

5. Write the H5b-Shift theorem-extension problem.

State precisely what a Bombieri--Iwaniec/Li--Yang method must prove for phases $e((q+\beta)X/d)$.

## For `deepseek_api`

1. Independently verify the H4 source.

Check the coefficient formula, constant, and convention against Vaaler's paper or a reliable modern exposition.

2. Run R5 numerical stress tests.

Include first leg, second leg, squares, near-squares, nonsquares, and divisor-rich $X$.

3. Run M9 main-term numerics with actual $\alpha_h$.

Compare fixed-coefficient sums with arbitrary-coefficient and $L^1$ stress versions.

4. Verify the Li--Yang source constraints with exact labels.

Record raw Case A/B restrictions, final exponent range, function hypotheses, weight hypotheses, and whether shifted frequencies are allowed.

5. Continue C2-SPU.

Provide a complete uniform stationary-phase lemma, explicitly correcting any overstrong "exponential decay" language to rapid integration-by-parts decay unless analyticity is assumed.

## For `gemini_deep_think`

1. Formalize Q1-Spectral as a diagnostic lemma.

State exactly which operator-norm or large-sieve steps are character-blind and which signed-form estimates remain open.

2. Define a concrete H12 signed spacing/trace model.

Use the actual M9a near-collision kernel and the Q1-Ext character factors. Determine whether signs survive a fourth-moment or trace estimate before absolute values enter.

3. Repair and classify C3-Affine/C3-Rational.

Fix notation, state exact parity cases, and connect the transformations to actual two-coset spacing geometry. Keep conclusions diagnostic unless a theorem is proved.

4. Keep Mellin--Perron as a comparison route.

Develop sharp/smoothed Perron formulas and saddle analysis only to theorem-dependency level; avoid "isomorphism" or "no-go" language unless exact kernels and errors are proved.

5. Analyze signed Fourier truncation as a comparison, not a bypass.

State the exact tail bound and identify whether the high-frequency tail reduces to product-counting, Fejer-type, or genuinely sign-preserving estimates.

## General state update

Update the following files:

- `state/current_state.md`;
- `state/lemma_bank.md`;
- `state/gap_register.md`;
- `state/best_proof_draft.md`;
- `manifests/reading_packet.md`.

Record Round 10 as a progress round that provisionally clears the fixed Fejer residual and redirects the main analytic burden to M9 fixed-coefficient Vaaler main sums. Preserve the no-exponent-improvement status.

Confidence:

High confidence in the selected balanced hyperbola/Vaaler reduction as the correct current framework.

High confidence in H1--H3.

High confidence that R5 is mathematically sound conditional on the H4 Fejer majorant.

Moderate-to-high confidence that R5-Full clears the total Vaaler residual after a careful complete write-up.

High confidence that H5r-B and H5r-L1 are overstrong and should not be active dependencies.

High confidence that the official remaining targets are M9 fixed-coefficient main sums.

High confidence that Li--Yang cannot be imported as a black box for the raw endpoint Vaaler block.

Moderate confidence that H5a-fix is structurally inside a Bombieri--Iwaniec/Li--Yang reciprocal phase class after residue splitting.

Moderate-to-low confidence that H5b-fix can be handled by existing printed theorems without a shifted-frequency extension.

Moderate confidence that Q1-Spectral is a useful operator-norm guardrail; low confidence that it rules out all signed spacing approaches.

Moderate confidence in the C2 stationary-phase leading term; low-to-moderate confidence in the uniform C2-SPU until transition and boundary estimates are written.

Low confidence that current known technology proves M9 at the endpoint.

Overall Round 10 judgment: productive and mathematically meaningful. The Fejer residual bottleneck is provisionally cleared; the proof skeleton is now sharper. The hard problem has not vanished, but it has moved to a precise pair of fixed-coefficient main-term estimates and to the question of whether any sign-preserving spacing method can exploit $\alpha_h$ and $\chi_4$ before standard norm estimates erase them.
