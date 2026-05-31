Summary:

This is the Stage A packet for the next round of the Gauss-circle workflow. The active instruction for `gpt_pro_thinking` is to insert H4 and H5r into the proof draft as real dependencies, state the Vaaler theorem needed for H4/H5r, compare H5r with the Li--Yang/Bombieri--Iwaniec reciprocal-sum framework, and keep the Poisson--Bessel calibration route alive. The current active-agent constraint remains `gpt_pro_thinking` and `gemini_deep_think`; inactive-agent references are historical noise.

The main conclusion is that H5r is not an optional technicality. Once the floor-compatible sawtooth identity is truncated by Vaaler, the Fejer-kernel residual produces parity-supported and untwisted reciprocal sums. These residual sums are structurally in the same broad Li--Yang reciprocal-sum class after residue splitting and smooth dyadic decomposition, but they are character-blind and require endpoint-strength estimates. Thus H5r may be the decisive obstruction, not merely an error term.

No improvement to the Gauss circle exponent is proved here. The result is a cleaner proof skeleton and a sharper statement of the endpoint estimates still missing.

Main claim or direction:

Continue the selected arithmetic route:

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{local dyadic reciprocal sums}.
$$

Here

$$
X=R^2,
\qquad
P(X)=N(\sqrt X)-\pi X,
$$

and the conjectural target is

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The proof draft should now be organized around four layers.

First, use the proved balanced sawtooth identity:

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

where

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

Second, split $1\le d\le y$ into smooth dyadic blocks $d\asymp D$.

Third, for long blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

use local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Short blocks $D<X^{1/4}$ are already at or below the conjectural scale by the trivial bound $|\psi|\le 1/2$.

Fourth, reduce the problem to three endpoint-strength local dyadic target families:

$$
B_1(H_0,D;X),
\qquad
B_2(H_0,D;X),
\qquad
C_1(K_0,D;X),\ C_{2,\rho}(K_0,D;X).
$$

The first two are Vaaler main terms. The last two are Fejer-residual terms. H5r must be treated as part of the analytic core.

Detailed reasoning:

## 1. Current proved arithmetic foundation

The following identities should now be in the proof draft as proved reductions.

Let

$$
\chi=\chi_4,
\qquad
T(X)=\sum_{ab\le X}\chi(a),
\qquad
S(u)=\sum_{1\le a\le u}\chi(a),
\qquad
y=\lfloor X^{1/2}\rfloor.
$$

By Jacobi's identity,

$$
N(\sqrt X)=1+4T(X).
$$

The symmetric hyperbola identity is

$$
T(X)
=
\sum_{a\le y}\chi(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

The periodic partial-sum identity is

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
-
\left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right).
$$

The resulting balanced sawtooth formula is

$$
P(X)
=
-4\sum_{a\le y}\chi(a)\psi(X/a)
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

This is H3. It is a floor-compatible identity. It is not a Fourier identity. The value at integers is

$$
\psi(n)=-\frac12,
$$

and this convention must be preserved until the Vaaler residual is inserted.

## 2. Vaaler theorem needed for H4/H5r

Use the following standard Vaaler approximation for the sawtooth function. This is the version needed in the proof draft.

For an integer $H\ge 1$, define the Fejer kernel

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2,
$$

with the limiting value at $t\in\mathbb Z$. Then

$$
K_H(t)\ge 0,
\qquad
K_H(0)=H+1.
$$

Let

$$
\Phi(u)=\pi u(1-|u|)\cot(\pi u)+|u|,
\qquad
0<|u|<1,
$$

and set $\Phi(0)=1$. Then there are coefficients

$$
\alpha_h
=
-\frac{1}{2\pi i h}
\Phi\left(\frac{h}{H+1}\right),
\qquad
1\le |h|\le H,
$$

such that

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
$$

with pointwise residual bound

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t).
$$

This is the form usually referred to as Vaaler's trigonometric approximation to the sawtooth function; the source to verify for the proof draft is Vaaler's paper "Some extremal functions in Fourier analysis."

The discontinuity convention is important. At $t\in\mathbb Z$, the finite trigonometric polynomial is continuous while the floor-compatible sawtooth has value $-1/2$. The residual bound is exactly large enough to absorb this, since

$$
\frac{1}{2H+2}K_H(0)=\frac12.
$$

Therefore no midpoint convention is being silently substituted. The Vaaler residual is the mechanism that reconciles the floor-compatible identity with a finite Fourier approximation.

## 3. Local dyadic Vaaler decomposition

Choose a smooth dyadic partition of unity on $1\le d\le y$:

$$
1=\sum_D w_D(d),
$$

where $w_D$ is supported on $d\asymp D$ and has uniformly controlled derivatives after scaling.

For blocks

$$
D<X^{1/4},
$$

use the trivial estimate

$$
\sum_{d\asymp D}|\psi(\cdots)|\ll D.
$$

Summed over dyadic $D<X^{1/4}$, this contributes

$$
O(X^{1/4}\log X),
$$

which is acceptable inside $X^{1/4+\epsilon}$.

For blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

choose

$$
H_D=\lfloor cD X^{-1/4}\rfloor
$$

with a fixed constant $c>0$, or simply write

$$
H_D\asymp D X^{-1/4}.
$$

This choice balances the zeroth Fejer residual term:

$$
\frac{D}{H_D}\asymp X^{1/4}.
$$

## 4. Vaaler main terms: H5a and H5b

On a long block $d\asymp D$, the first sawtooth leg gives

$$
M_1(D)
=
-4
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_d
\chi_4(d)w_D(d)e(hX/d).
$$

After dyadic subdivision $h\sim H_0$ and factoring $\alpha_h\ll 1/H_0$, a sufficient target is:

$$
B_1(H_0,D;X)
=
\sum_{h\sim H_0}u_{H_0}(h)
\sum_d
\chi_4(d)w_D(d)e(hX/d)
\ll_\epsilon
H_0X^{1/4+\epsilon},
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le H_D.
$$

Here $u_{H_0}$ should be a smooth or bounded-variation dyadic weight, not an arbitrary coefficient sequence unless a later theorem explicitly supports arbitrary coefficients.

The second sawtooth leg gives

$$
M_2(D)
=
4
\sum_{1\le |h|\le H_D}
\alpha_h
\left(e(h/4)-e(3h/4)\right)
\sum_d
w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the second main target is

$$
B_2(H_0,D;X)
=
\sum_{h\sim H_0}u_{H_0}(h)\chi_4(h)
\sum_d
w_D(d)e(hX/(4d))
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

This should not be merged with H5a. H5a has the character in the denominator variable. H5b has the character in the Fourier variable.

## 5. Fejer residual terms: H5r

This is the main update to the proof draft.

The first-leg residual on a block $D$ is bounded by

$$
R_1(D)
\ll
\sum_d
1_{2\nmid d}w_D(d)
\frac{1}{H_D}K_{H_D}(X/d).
$$

Expanding the Fejer kernel gives

$$
R_1(D)
\ll
\frac{D}{H_D}
+
\frac{1}{H_D}
\sum_{1\le |k|\le H_D}
\left|
\sum_d
1_{2\nmid d}w_D(d)e(kX/d)
\right|
$$

in a crude form. A sharper dyadic form keeps the Fejer coefficients as smooth weights. For $K_0\le H_D$, define

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_{K_0}(k)
\sum_d
1_{2\nmid d}w_D(d)e(kX/d),
$$

where $v_{K_0}$ is a smooth dyadic weight incorporating the Fejer coefficient $1-|k|/(H_D+1)$ and possibly one global unit phase from taking the absolute value of the dyadic block.

A sufficient residual target is

$$
C_1(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}
$$

for all

$$
1\le K_0\le H_D.
$$

Then

$$
\frac1{H_D}
\sum_{K_0\le H_D}
|C_1(K_0,D;X)|
\ll_\epsilon
X^{1/4+\epsilon}.
$$

The second-leg residual comes from the two terms

$$
R_H\left(\frac{X/d+1}{4}\right),
\qquad
R_H\left(\frac{X/d+3}{4}\right).
$$

It requires estimates for

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_{K_0}(k)e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

A sufficient target is

$$
C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}
$$

uniformly for

$$
\rho\in\{1,3\},
\qquad
1\le K_0\le H_D,
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

Important correction: H5r should not be formulated with completely arbitrary $v_k$ unless one is deliberately asking for a stronger theorem. The actual Fejer residual supplies smooth dyadic weights. The absolute value of a dyadic block only introduces one global phase, not arbitrary signs in $k$.

Thus H5r is not malformed, but it is endpoint-strength and character-blind.

## 6. Comparison of H5r with Li--Yang/Bombieri--Iwaniec

Li--Yang's paper states that it improves both the Gauss circle and Dirichlet divisor problems by using the Bombieri--Iwaniec method, deriving a new first-spacing estimate, and combining it with Huxley's second-spacing results. The arXiv record gives the title, authors, revision history, and abstract with this method description.

The ANTEDB Gauss-circle chapter records the current sharpest listed two-dimensional Gauss-circle upper bound as Li--Yang 2023, with

$$
\theta_2^{\operatorname{Gauss}}\le 2\alpha,
\qquad
\alpha=0.31448\ldots,
$$

and lists Huxley 2003 at $131/208$ in $R$-notation.

The local H5 targets match the broad Li--Yang reciprocal-sum template. In the notation

$$
T=X,
\qquad
M=D,
\qquad
H=H_0\text{ or }K_0,
$$

the relevant phase is

$$
e\left(\frac{hX}{d}\right)
=
e\left(\frac{hT}{M}F(d/M)\right),
\qquad
F(x)=\frac1x,
$$

up to harmless signs and constants.

For

$$
F(x)=\frac1x
$$

on a fixed dyadic interval $x\asymp 1$,

$$
F'(x)=-x^{-2},
\qquad
F''(x)=2x^{-3},
\qquad
F'''(x)=-6x^{-4}.
$$

The Li--Yang nondegeneracy expression is

$$
F'(x)F'''(x)-3F''(x)^2
=
6x^{-6}-12x^{-6}
=
-6x^{-6},
$$

so it is uniformly bounded away from zero on $1\le x\le 2$.

H5r is therefore structurally inside the same reciprocal-sum family after simple residue splitting:

- The parity-supported first residual $1_{2\nmid d}$ is a finite sum over residue classes modulo $2$.
- The second residual is untwisted, with an additive shift $e(k\rho/4)$ in the Fourier variable.
- Constant factors such as $1/4$ in $e(kX/(4d))$ are absorbed into $T$ or into $F$.

The critical distinction is not the phase class. The distinction is the exponent. Li--Yang reaches

$$
\theta^*=0.314483\ldots
$$

in $X$-notation, while this project's conjectural endpoint requires

$$
\theta=\frac14.
$$

Thus H5a/H5b/H5r are endpoint-strength targets that are stronger than currently cited Li--Yang technology. They are not known estimates.

## 7. H6 diagnostic under named convention

Use the standard exponent-pair convention for one-dimensional sums:

If $(\kappa,\lambda)$ is an exponent pair and $f$ on $d\asymp D$ satisfies

$$
f^{(r)}(d)\asymp T D^{-r}
$$

for the relevant derivative range, then

$$
\sum_{d\asymp D} e(f(d))
\ll_\epsilon
T^\kappa D^\lambda X^\epsilon.
$$

For

$$
f(d)=\frac{hX}{d},
$$

one has

$$
f^{(r)}(d)\asymp hX D^{-r-1},
$$

so the exponent-pair scale is

$$
T\asymp \frac{hX}{D}.
$$

At the endpoint block

$$
D\asymp X^{1/2},
\qquad
h\asymp H_0\asymp X^{1/4},
$$

this gives

$$
T\asymp X^{3/4},
$$

and therefore

$$
\sum_{d\asymp D}e(hX/d)
\ll_\epsilon
X^{3\kappa/4+\lambda/2+\epsilon}.
$$

If the outer $h$-sum is treated trivially, the inner sum must be

$$
\ll X^{1/4+\epsilon}
$$

to reach the H5 target. Hence the required condition is

$$
\frac{3\kappa}{4}+\frac{\lambda}{2}\le \frac14,
$$

or

$$
3\kappa+2\lambda\le 1.
$$

This is H6. It is only a conditional diagnostic. It rules out a naive method that takes absolute values in $h$ and then applies only a one-dimensional exponent-pair estimate to the $d$-sum. It does not rule out bilinear estimates, double large sieve, Bombieri--Iwaniec spacing, or decoupling-like estimates that retain the two-variable structure.

## 8. Minimal Poisson--Bessel calibration route

The secondary route should be written into the proof draft as a calibration module, not as the main analytic route.

Let $\rho\in C_c^\infty(\mathbb R^2)$ be nonnegative, radial, supported in a fixed ball, and normalized by

$$
\int_{\mathbb R^2}\rho(x)\,dx=1.
$$

Set

$$
\rho_\delta(x)=\delta^{-2}\rho(x/\delta),
$$

and define the smoothed count

$$
S_\delta(R)
=
\sum_{m\in\mathbb Z^2}
(1_{B_R}*\rho_\delta)(m).
$$

### B1a. Smooth sandwich

If $\operatorname{supp}\rho\subseteq B_C(0)$, then

$$
S_\delta(R-C\delta)\le N(R)\le S_\delta(R+C\delta).
$$

Consequently,

$$
E(R)
\ll
R\delta+
\sup_{|t-R|\le C\delta}
|S_\delta(t)-\pi t^2|
+
O(\delta^2).
$$

### B1b. Poisson--Bessel formula

Poisson summation gives

$$
S_\delta(R)-\pi R^2
=
R
\sum_{k\in\mathbb Z^2\setminus\{0\}}
\frac{J_1(2\pi R|k|)}{|k|}
\widehat \rho(\delta k).
$$

### B1c. Recovery of the classical $R^{2/3}$ sanity bound

Using

$$
J_1(t)\ll t^{-1/2}
$$

for $t\gg 1$, rapid decay of $\widehat\rho(\delta k)$ for $|k|\gg \delta^{-1}$, and trivial dyadic counting of lattice points, one obtains

$$
S_\delta(R)-\pi R^2
\ll
R^{1/2}\delta^{-1/2}
$$

up to harmless lower-order terms.

The sandwich then gives

$$
E(R)
\ll
R\delta+R^{1/2}\delta^{-1/2}.
$$

Balancing at

$$
\delta=R^{-1/3}
$$

recovers

$$
E(R)\ll R^{2/3}.
$$

This module is useful because it checks smoothing conventions and normalizations. It should not be used to claim a new exponent.

Dependencies:

1. Jacobi's two-square formula:

$$
r_2(n)=4\sum_{d\mid n}\chi_4(d).
$$

2. The proved symmetric hyperbola identity H1.

3. The proved periodic partial-sum identity H2.

4. The proved balanced sawtooth identity H3.

5. Vaaler's trigonometric approximation to the sawtooth function, with Fejer residual majorant.

6. Smooth dyadic partitioning with uniform derivative control.

7. Endpoint-strength reciprocal-sum estimates H5a, H5b, and H5r.

8. For comparison only, Li--Yang/Bombieri--Iwaniec reciprocal-sum technology. Li--Yang currently supplies an exponent $\theta^*=0.314483\ldots$, not the endpoint $\theta=1/4$.

9. For the calibration route, Poisson summation, the Fourier transform of the disk, standard Bessel bounds, and the smoothing/unsmoothing sandwich.

Potential gaps:

1. **Vaaler theorem verification.**
   The exact coefficient formula with $\Phi(u)$ should be checked against a standard reference before H4 is marked as an imported theorem dependency in the lemma bank.

2. **H5r smooth-weight formulation.**
   The residual target should be formulated with the actual smooth Fejer/dyadic weights. If the target is stated with arbitrary bounded $v_k$, it becomes stronger than needed and may no longer match Li--Yang-type hypotheses.

3. **Endpoint strength.**
   Even after H5r is placed inside the Li--Yang reciprocal-sum class, it asks for the conjectural endpoint $\theta=1/4$, beyond the current Li--Yang exponent $\theta^*=0.314483\ldots$.

4. **Absolute values in residuals.**
   The residual proof takes absolute values at the dyadic block level. This is acceptable if only one global phase per block is introduced. Taking absolute values term-by-term in $k$ would destroy the double-sum structure and should be rejected.

5. **Parity-supported residuals.**
   H5r contains $1_{2\nmid d}$ rather than $\chi_4(d)$. This is closer to the divisor-problem side than to a genuinely character-exploiting sum. It may be the main obstruction.

6. **Boundary blocks.**
   The transition around $D\asymp X^{1/4}$ and the final block near $D\asymp y$ need explicit partition conventions.

7. **B-process-first route does not currently solve H5r.**
   H8 was derived for the spatial-character main family H5a. H5r is parity-supported or untwisted, so H8 may not help the residual obstruction.

8. **Poisson--Bessel calibration is not yet in the repo as a checked proof.**
   It should be added, but kept secondary.

Counterexample or obstruction search:

1. **Fejer spike test.**
   Test $X,d$ for which $X/d$ or $(X/d+\rho)/4$ is very close to an integer. Then $K_H(\cdot)$ may be as large as $H+1$. The residual majorant is designed for this, but the resulting sums must still be covered by H5r.

2. **Residual absolute-value trap.**
   Compare three bounds for the residual:
   - scalar $D/H_D$ only;
   - dyadic block absolute values;
   - termwise absolute values over $k$.

   The first is incomplete. The third is too crude. The second is the intended H5r route.

3. **Parity loss.**
   In $C_1$, split

$$
1_{2\nmid d}
$$

into residue classes. Verify that no $\chi_4$ cancellation remains.

4. **Endpoint H6 stress test.**
   At

$$
D\asymp X^{1/2},
\qquad
H_0\asymp X^{1/4},
$$

a one-dimensional exponent-pair method requires

$$
3\kappa+2\lambda\le 1.
$$

This should be used as a diagnostic against proposed character-blind inner-sum estimates.

5. **Li--Yang matching test.**
   For each of $B_1,B_2,C_1,C_{2,\rho}$, write the exact $F(x)$ after residue splitting and verify:
   - smoothness on $1\le x\le 2$;
   - $|F'|,|F''|,|F'''|$ of the correct size;
   - $F'F'''-3(F'')^2$ bounded away from zero;
   - no arbitrary coefficients incompatible with the theorem being invoked.

6. **B-process limitation test.**
   Apply the H8 transform to H5a and then directly difference the dual $\chi_4$ variable. H7 reappears. This confirms that H8 delays, but does not eliminate, the character-collapse obstruction.

Useful lemmas:

## H1. Exact symmetric hyperbola identity

Status: proved.

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$,

$$
\sum_{ab\le X}\chi_4(a)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

## H2. Exact periodic formula for $S(u)$

Status: proved.

For real $u\ge 0$,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
-
\left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right).
$$

## H3. Balanced sawtooth formula

Status: proved as an $O(1)$ floor-compatible identity.

For $X\ge 1$,

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

## H4. Finite Vaaler with Fejer residual

Status: external theorem dependency; exact statement proposed above.

The proof draft must retain

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t).
$$

It must not replace the residual by a scalar before summing over $d$.

## H5a. Spatial-character local dyadic target

Status: sufficient target; not known.

For

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le D X^{-1/4},
$$

prove

$$
B_1(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

## H5b. Frequency-character local dyadic target

Status: sufficient target; not known.

For the same range, prove

$$
B_2(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

## H5r. Fejer-residual local dyadic targets

Status: required sufficient target; not known.

For smooth Fejer/dyadic weights, prove

$$
C_1(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon},
$$

and

$$
C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

This target is structurally Li--Yang-type after residue splitting, but endpoint-strength and character-blind.

## H6. Conditional one-dimensional exponent-pair diagnostic

Status: diagnostic, not theorem.

Under the standard reciprocal-phase convention

$$
T\asymp hX/D,
$$

a method that treats $h$ trivially and applies only a one-dimensional exponent-pair bound in $d$ must satisfy

$$
3\kappa+2\lambda\le 1
$$

at the endpoint block.

## H7. A-process modulus degeneracy for $\chi_4$

Status: proved.

For every integer $q$,

$$
\chi_4(d)\chi_4(d+q)
=
\begin{cases}
1_{2\nmid d},& q\equiv 0\pmod 4,\\
-1_{2\nmid d},& q\equiv 2\pmod 4,\\
0,& q\equiv 1,3\pmod 4.
\end{cases}
$$

## H8. B-process-first character-dualization

Status: partially derived; not used as a proof input yet.

For smooth compact support away from zero,

$$
\sum_d\chi_4(d)w(d/D)e(hX/d)
$$

has a Poisson-dual form with dual character $\chi_4(n)$ and dual length

$$
|n|\asymp hX/D^2.
$$

It preserves the character but does not yet prove cancellation.

## H9. B-process dual Hessian degeneracy

Status: proved diagnostic.

For

$$
\Phi(h,m)=\sqrt{Xhm},
$$

one has

$$
\det\nabla^2\Phi=0.
$$

Thus generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly to the B-process dual phase.

## B1. Poisson--Bessel calibration module

Status: secondary route; proposed proof module.

Add the smooth sandwich, Poisson--Bessel formula, and $E(R)\ll R^{2/3}$ recovery as a calibration check.

What should be tested next:

1. Verify the Vaaler statement from a standard source and record the exact theorem in the lemma bank as H4.

2. Rewrite the best proof draft so that H5r appears immediately after H4. It should be impossible to read the draft and think the Vaaler residual is only $O(D/H_D)$.

3. Match $C_1$ and $C_{2,\rho}$ explicitly to the Li--Yang sum template after residue splitting. Record the resulting $F(x)$ functions and derivative checks.

4. Determine whether Li--Yang's actual theorem permits the smooth Fejer/dyadic weights needed in H5r. If it requires stricter smoothness or compact support, update the weight construction.

5. Run numerical stress tests for H5r at square and near-square $X$.

6. Keep H8 separate. H8 may help H5a but currently does not solve H5r.

7. Add the Poisson--Bessel calibration module and verify the $R^{2/3}$ sanity bound.

Confidence:

High confidence in the selected arithmetic route and in H1--H3 as floor-compatible reductions.

High confidence that the Vaaler residual must be represented by a Fejer-kernel majorant and that H5r is a necessary part of the proof skeleton.

High confidence that, under the standard reciprocal-phase exponent-pair convention, H6 gives the endpoint diagnostic condition

$$
3\kappa+2\lambda\le 1.
$$

Moderate confidence that H5r is structurally within the Li--Yang/Bombieri--Iwaniec reciprocal-sum class once formulated with smooth dyadic Fejer weights rather than arbitrary coefficients.

Low confidence that existing Li--Yang technology reaches the H5 endpoint. The current cited record is still above the conjectural exponent, with Li--Yang giving $\theta^*=0.314483\ldots$ in $X$-notation while the target is $\theta=1/4$.

No new exponent has been proved. The concrete progress is a stricter proof draft: H4 and H5r are now mandatory dependencies, H5r is properly compared to Li--Yang-type sums, and the Poisson--Bessel route is retained as a calibration module rather than a main proof route.
