Summary:

Round 10 Stage A progress: I give a complete lemma-level proof of the Fejer product-count residual bound R5, formulate the full residual bridge R5-Full, state the precise Vaaler theorem needed as H4 with the standard coefficient function, and replace the overstrong arbitrary-coefficient H5a/H5b targets by the actual fixed-Vaaler-coefficient main-term targets. This supports the Round 9 route

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

where M9 denotes the two fixed-coefficient main-term estimates. No new Gauss circle exponent is proved, because M9 remains open.

Source anchors: the active Round 10 packet asks for independent reasoning and concrete progress with explicit proof gaps, while Round 9 identifies R5, H4, H5a-fix/H5b-fix, and the local scale as the next objects to settle. The uploaded background packet also records the standard Gauss circle discrepancy formulation and the $X=R^2$ exponent conversion. The remaining main-term and Li--Yang high-frequency gaps are explicitly listed in the Round 9 packet. The arXiv page for Li--Yang identifies version v2, dated 2023-09-14, and states that the method combines a new first-spacing estimate with Huxley's second-spacing results. ANTEDB records the Li--Yang 2023 Gauss-circle upper bound in the current exponent-database chapter.

Main claim or direction:

The residual bottleneck H5r-F should be reclassified from "central open bottleneck" to "conditionally cleared once H4 is reference-verified," because the fixed Fejer residual is controlled by a direct product-counting argument. The main analytic burden is now the pair of fixed Vaaler main sums

$$
\mathcal M_1(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_{d\sim D}
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\sim D}
w_D(d)e(hX/(4d)).
$$

The required target is

$$
\mathcal M_i(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4}.
$$

The old arbitrary-coefficient targets H5a/H5b are stronger stress tests, not the correct active dependencies.

Detailed reasoning:

1. Vaaler theorem needed as H4

Use

$$
e(t)=e^{2\pi i t},
\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

The standard Vaaler approximation needed here should be recorded as follows. For an integer $H\ge 1$, define

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2,
$$

with the usual limiting value $K_H(n)=H+1$ at integers. Define

$$
\Phi(u)=\pi u(1-|u|)\cot(\pi u)+|u|,
\qquad
0<|u|<1,
$$

with the continuous extension $\Phi(0)=1$. Then the required theorem is

$$
\psi(t)
=
-\sum_{1\le |h|\le H}
\frac{\Phi(h/(H+1))}{2\pi i h}e(ht)
+
R_H(t),
$$

where

$$
|R_H(t)|
\le
\frac1{2H+2}K_H(t).
$$

Thus in the notation used below,

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h},
\qquad
|\alpha_{h,H}|\ll |h|^{-1}.
$$

This is the precise form of H4 needed for the proof. I have not page-verified the normalization against the original Vaaler paper in this environment. The standard source to cite is Vaaler, "Some extremal functions in Fourier analysis," Bull. Amer. Math. Soc. 12 (1985), 183--216; the available web result identifies the paper but the Project Euclid PDF fetch failed here. The repo should still perform a page-level audit before marking H4 fully imported. For the reduction, however, any version with

$$
|R_H(t)|\le C H^{-1}K_H(t)
$$

and $|\alpha_{h,H}|\ll |h|^{-1}$ is exponent-equivalent.

2. Fejer kernel pointwise bound

For all real $t$,

$$
K_H(t)
\ll
\min\left(H,\frac1{H\|t\|^2}\right),
$$

where $\|t\|$ is distance to the nearest integer. Therefore

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

This is the only analytic input in R5 besides the divisor bound.

3. R5 first-leg proof

Let

$$
X\ge 2,\qquad
X^{1/4}\le D\le X^{1/2},
\qquad
H\asymp D X^{-1/4}.
$$

Let $w_D$ be supported on $d\asymp D$ and satisfy $|w_D(d)|\le 1$. We prove

$$
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The parity restriction can be ignored for an upper bound.

For each $d\sim D$, choose an integer $m=m(d)$ nearest to $X/d$. Then

$$
\|X/d\|
=
\left|\frac Xd-m\right|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

Set

$$
\Delta=\frac{D}{H}\asymp X^{1/4}.
$$

By the Fejer bound,

$$
\frac1H K_H(X/d)
\ll
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

For the chosen nearest integer $m$, one has $m\asymp X/D$ and $md\asymp X$. Put $n=md$. The number of pairs $(m,d)$ with product $n$ is at most $\tau(n)$. Hence

$$
\frac1H
\sum_{d\sim D}
K_H(X/d)
\ll
\sum_{n\asymp X}
\tau(n)
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right).
$$

Using $\tau(n)\ll_\epsilon n^\epsilon$ for $n\asymp X$ gives

$$
\frac1H
\sum_{d\sim D}
K_H(X/d)
\ll_\epsilon
X^\epsilon
\sum_{n\in\mathbb Z}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right).
$$

The last sum is $O(\Delta+1)$ for every real $X$: there are $O(\Delta+1)$ integers with $|X-n|\le \Delta$, and the tail is bounded by

$$
\Delta^2\sum_{j>\Delta}j^{-2}\ll \Delta.
$$

Thus

$$
\frac1H
\sum_{d\sim D}
K_H(X/d)
\ll_\epsilon
X^\epsilon(\Delta+1)
\ll_\epsilon X^{1/4+\epsilon}.
$$

This handles integer and noninteger $X$ uniformly. If $X$ is bounded, all contributions are absorbed into the implicit constant.

4. R5 second-leg proof

For $\rho\in\{1,3\}$ prove

$$
\frac1H
\sum_{d\sim D}
|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Choose $m=m(d)$ nearest to $(X/d+\rho)/4$. Then

$$
\left\|\frac{X/d+\rho}{4}\right\|
=
\left|
\frac{X/d+\rho}{4}-m
\right|
=
\frac{|X-d(4m-\rho)|}{4d}.
$$

Put

$$
\ell=4m-\rho.
$$

For large $X$, $\ell\asymp X/D$ and $\ell\equiv -\rho \pmod 4$. Small $X$ is harmless. The Fejer bound gives

$$
\frac1H
K_H\left(\frac{X/d+\rho}{4}\right)
\ll
\min\left(1,\frac{\Delta^2}{|X-d\ell|^2}\right),
$$

with the same $\Delta=D/H\asymp X^{1/4}$. Grouping by $n=d\ell$ gives at most $\tau(n)$ representations, even with the congruence condition on $\ell$. Hence

$$
\frac1H
\sum_{d\sim D}
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon
X^\epsilon
\sum_{n\in\mathbb Z}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

This proves the shifted second-leg R5 bound.

5. R5-Full: residual bridge

Apply H4 blockwise in the proved balanced sawtooth formula

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
O(1).
$$

For each dyadic $D$ with $X^{1/4}\le D\le X^{1/2}$, choose

$$
H_D\asymp D X^{-1/4}.
$$

The first-leg residual is bounded by

$$
\frac{C}{H_D}
\sum_{d\sim D}
|\chi_4(d)|\,|w_D(d)|K_{H_D}(X/d).
$$

Since $|\chi_4(d)|=1_{2\nmid d}$, this is exactly the first R5 estimate. The second-leg residual is bounded by a sum of the two shifted R5 estimates with $\rho=1,3$.

The zero Fejer mode is included in $K_H$. Equivalently, it contributes

$$
D/H_D\asymp X^{1/4}
$$

per dyadic block. Both signs of $k$ are also already included in the symmetric Fejer kernel $K_H$.

For dyadic blocks $D<X^{1/4}$, no Vaaler expansion is needed: the trivial bound for the sawtooth contribution is $O(D)$ per block, and summing over such blocks gives $O(X^{1/4})$. The number of dyadic blocks is $O(\log X)$ and is absorbed into $X^\epsilon$.

Therefore H4 plus R5 implies the total Vaaler residual bound

$$
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

This is a proved conditional lemma once H4 is source-verified.

6. Official replacement for H5a/H5b

The correct remaining main-term targets are not arbitrary-coefficient dyadic sums. They are the fixed Vaaler-coefficient sums.

Define

$$
\mathcal M_1(D;X)
=
-4
\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_d
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
4
\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_d
w_D(d)e(hX/(4d)).
$$

Using

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

this becomes

$$
\mathcal M_2(D;X)
=
8i
\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_d
w_D(d)e(hX/(4d)).
$$

The official M9 target is

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon
X^{1/4+\epsilon}
$$

for every dyadic $D$ in the local range. H5a-B/H5b-B, where arbitrary bounded coefficients are inserted in the $h$ variable, remain useful stress tests but are stronger than needed.

7. Li--Yang comparison for H5a-fix

For H5a-fix, split the spatial character into residue classes

$$
\chi_4(d)=1_{d\equiv 1\pmod 4}-1_{d\equiv 3\pmod 4}.
$$

On $d=4m+r$, $r\in\{1,3\}$,

$$
e(hX/d)=e\left(\frac{hX}{4m+r}\right).
$$

After scaling $m\asymp M\asymp D/4$, this fits a reciprocal phase of Li--Yang/Bombieri--Iwaniec type

$$
e\left(\frac{hT}{M}F_{r,M}(m/M)\right),
\qquad
T=X,
$$

with

$$
F_{r,M}(u)=\frac{1}{4}\frac{1}{u+r/(4M)}.
$$

The derivative hypotheses are uniform on compact subintervals of $(0,\infty)$, so this is structurally compatible with Li--Yang's class. However, theorem-level applicability is limited by the height and exponent restrictions. Li--Yang's final circle/divisor reduction seeks

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\cdots,
$$

whereas the conjectural Vaaler endpoint needs $X^{1/4+\epsilon}$ after the $1/h$ coefficient is accounted for. The arXiv source confirms the theorem's stated exponent and method, but not endpoint strength.

More concretely, in the raw endpoint block

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4}.
$$

Li--Yang Case A imposes

$$
H\le MT^{-49/164}=X^{33/164},
$$

and Case B includes

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}.
$$

Both are below $X^{1/4}$. The final application range

$$
H\le MT^{-\theta^*}
$$

only reaches $H\le X^{1/2-\theta^*}=X^{0.185516\cdots}$ at $D\asymp X^{1/2}$. Thus the uncovered high-frequency range remains

$$
D X^{-\theta^*}
\lesssim H
\lesssim
D X^{-1/4}.
$$

8. Li--Yang comparison for H5b-fix

H5b-fix is subtler than H5a-fix because the character is in the frequency variable:

$$
\chi_4(h).
$$

One may write

$$
\chi_4(h)=\frac{e(h/4)-e(3h/4)}{2i},
$$

but this introduces a periodic factor in the $h$ variable. Li--Yang's printed theorem uses a bounded-variation weight $g(h/H)$; a rapidly oscillating factor such as $e(h/4)$ is not bounded variation uniformly in $H$ when interpreted as a function of $h/H$.

Alternatively split $h=4q+r$, $r\in\{1,3\}$. Then

$$
e(hX/(4d))
=
e\left(\frac{(4q+r)X}{4d}\right)
=
e\left(\frac{(q+r/4)X}{d}\right).
$$

This creates a shifted-frequency reciprocal sum

$$
\sum_{q\asymp H/4}
\widetilde\alpha_{q,r}
\sum_{d\sim D}
w_D(d)
e\left(\frac{(q+\beta_r)X}{d}\right),
\qquad
\beta_r=r/4.
$$

It is plausible that Bombieri--Iwaniec machinery tolerates a fixed fractional shift $q+\beta_r$, but this is not literally the printed Li--Yang theorem. Treat this as a theorem-extension gap, not as verified applicability.

Dependencies:

1. H1--H3: proved balanced hyperbola and floor-compatible sawtooth reduction.

2. H4: Vaaler theorem with coefficients

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h}
$$

and Fejer residual majorant

$$
|R_H(t)|\le (2H+2)^{-1}K_H(t).
$$

This is a standard external theorem, but the exact page and normalization still require source verification.

3. Elementary Fejer bound:

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right).
$$

4. Divisor bound:

$$
\tau(n)\ll_\epsilon n^\epsilon.
$$

5. Dyadic partition with uniformly bounded weights $|w_D|\le 1$. Smoothness is not needed for R5, but it is needed for later main-term comparison with Li--Yang.

6. Li--Yang audit: the arXiv source is v2 from 2023-09-14 and states the method as Bombieri--Iwaniec plus first/second spacing. The theorem-level comparison must use the TeX source labels around `definition of S`, `condition on F 1`, `condition on F 2`, `main theorem`, and `goal`, as required by the human source-audit directive.

Potential gaps:

1. H4 source audit gap. The Vaaler statement above is the right theorem form, but the repo still needs a precise citation and normalization check. In particular, the coefficient function $\Phi$, the factor $(2H+2)^{-1}$, and the floor-compatible value $\psi(n)=-1/2$ must be checked against the source.

2. R5 uses a positive majorant. This is appropriate for the residual only. It must not be reused for the main Vaaler polynomial, where sign and cancellation are central.

3. R5 second-leg endpoint cases. For small $X$ or very small $X/d$, the factor $\ell=4m-\rho$ may require a finite-case cutoff. This is harmless for asymptotics but should be written explicitly in the proof draft.

4. Dyadic partition signs. If the partition weights are not nonnegative, R5 must be applied to $|w_D|$. This is valid for residuals but should be stated.

5. H5b-fix theorem mismatch. Frequency-character splitting creates either non-BV periodic $h$ weights or shifted-frequency sums $q+\beta$. Li--Yang's printed theorem does not directly state this extension.

6. Main-term estimates remain open. R5 only clears the Fejer residual. It does not give cancellation in

$$
\sum_h \alpha_h \sum_d \chi_4(d)e(hX/d)
$$

or in the frequency-character analogue.

7. Li--Yang endpoint gap. Existing Li--Yang technology gives $\theta^*=0.314483\cdots$, not $1/4$. The ANTEDB Gauss-circle chapter also records the Li--Yang bound as the sharpest listed upper bound rather than the conjectural endpoint.

Counterexample or obstruction search:

1. Fejer spike obstruction is neutralized for the residual. If $X/d$ is near an integer, then $md$ is near $X$. R5 counts such spikes by products $n=md$ and the divisor bound. Even divisor-rich $n$ contributes only $X^\epsilon$ multiplicity.

2. Noninteger $X$ does not break R5. The kernel sum reduces to

$$
\sum_{n\in\mathbb Z}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right),
$$

which is $O(\Delta+1)$ uniformly in real $X$.

3. Second-leg congruence spikes do not break R5. Near-integrality of $(X/d+\rho)/4$ becomes

$$
X\approx d(4m-\rho),
$$

with only a congruence restriction on the complementary factor. The ordinary divisor bound still dominates.

4. A possible false positive is to claim that R5 solves the main terms. It does not. The main terms have signed Fourier coefficients and are essentially the difficult oscillatory part of the sawtooth sum.

5. H5b-fix has a structural obstruction not yet fully recorded: the frequency character $\chi_4(h)$ is not a smooth bounded-variation $h$ weight. Splitting $h\bmod 4$ produces shifted-frequency sums, and this extension must be justified before importing Li--Yang-type estimates.

6. A raw Li--Yang invocation at the endpoint is falsified by the height constraints. At $D\asymp X^{1/2}$, the endpoint height is $X^{1/4}$, while raw Case A/B ranges are smaller. The Round 9 packet already records this as a high-frequency gap.

Useful lemmas:

## H4. Vaaler finite approximation with Fejer residual

Status: external theorem dependency; statement precise, source normalization pending.

For $H\ge 1$,

$$
\psi(t)
=
\sum_{1\le |h|\le H}
\alpha_{h,H}e(ht)+R_H(t),
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

## R5. Fejer product-count bound

Status: proved conditional on H4 only for its use in the residual.

For $X\ge 2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp D X^{-1/4}$, and $|w_D|\le 1$ supported on $d\asymp D$,

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

## R5-Full. Total Vaaler residual bound

Status: proved conditional on H4 and R5.

Inserting H4 blockwise into H3 and using $H_D\asymp D X^{-1/4}$ gives total residual

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Short blocks $D<X^{1/4}$ are handled trivially.

## M9. Fixed-coefficient main-term criterion

Status: proposed official main analytic target.

If for every dyadic $D$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon},
$$

then H1--H4 plus R5-Full imply

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

## LY-M9a. Spatial-character Li--Yang dictionary

Status: structural, not endpoint theorem.

After splitting $d\bmod 4$, H5a-fix fits reciprocal phases satisfying Li--Yang-type derivative hypotheses. The theorem does not supply the endpoint exponent or endpoint height.

## LY-M9b. Frequency-character shifted-frequency gap

Status: identified theorem-extension gap.

After splitting $h\bmod 4$, H5b-fix becomes a shifted-frequency reciprocal sum with phase

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\}.
$$

A Li--Yang/Bombieri--Iwaniec extension to fixed fractional shifts is plausible but not present in the printed theorem as currently audited.

## LY-Raw-Mismatch

Status: proved guardrail.

For $T=X$, $M=D\asymp X^{1/2}$, $H\asymp X^{1/4}$, Li--Yang's raw Case A/B height constraints do not reach the endpoint Vaaler height. Therefore the theorem cannot be quoted directly to prove M9.

What should be tested next:

1. Source-verify H4 exactly. The repo should quote Vaaler's theorem or a standard modern reference with the coefficient function $\Phi$, the Fejer kernel normalization, and the pointwise residual bound. The discontinuity value $\psi(n)=-1/2$ must be covered.

2. Insert R5 and R5-Full into `state/best_proof_draft.md`. Mark H5r-F as conditionally cleared and move H5r-B/H5r-L1 to stress-test status.

3. Run R5 numerical stress tests anyway. Test square $X$, near-square $X$, highly composite nearby products, and second-leg congruence spikes

$$
X\approx d(4m-\rho).
$$

4. Compute fixed main sums

$$
\mathcal M_1(D;X),
\qquad
\mathcal M_2(D;X)
$$

with actual $\alpha_{h,H_D}$, and compare them with arbitrary-coefficient and termwise $L^1$ versions. This tests whether fixed Vaaler coefficients give measurable cancellation.

5. Audit H5b-fix against Li--Yang carefully. Determine whether the Bombieri--Iwaniec proof survives the replacement $h\mapsto h+\beta$ with $\beta\in\{1/4,3/4\}$, or whether a new lemma is required.

6. For H5a-fix, complete the residue-class Li--Yang dictionary with exact $F_{r,M}$, derivative constants, allowed weights, and parameter substitutions.

7. Isolate the high-frequency range

$$
D X^{-\theta^*}
\lesssim H
\lesssim
D X^{-1/4}
$$

as the main analytic gap after known Li--Yang technology. The task is not to reprove Li--Yang but to determine what additional first-spacing, second-spacing, or fixed-coefficient cancellation would be needed in that range.

8. Preserve the no-solution status. The current proof skeleton proves a conditional reduction, not a new exponent.

Confidence:

High confidence in the R5 product-count proof, including the shifted second leg, conditional only on the standard Fejer majorant H4.

High confidence that R5-Full clears the fixed Fejer residual H5r-F after dyadic summation and short-block handling.

High confidence that H5r-B and H5r-L1 are overstrong and should not remain active proof dependencies.

Moderate-to-high confidence in the H4 theorem statement, but only moderate confidence in the exact normalization until a page-level source audit is completed.

High confidence that the correct remaining targets are M9 fixed-coefficient main sums.

High confidence that raw Li--Yang does not cover the endpoint Vaaler range.

Moderate confidence that H5a-fix is structurally inside Li--Yang's reciprocal phase class after residue splitting.

Moderate-to-low confidence that H5b-fix can be imported without a shifted-frequency extension; this is now an explicit theorem-level gap.

Low confidence that current known technology proves M9 at the endpoint. The Round 10 progress is a cleaner reduction: the residual appears controlled, and the hard problem has been localized to fixed-coefficient Vaaler main terms.
