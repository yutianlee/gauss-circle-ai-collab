Selected main route:

Continue the arithmetic route:

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

The smoothed Poisson--Bessel route remains secondary: it should still be kept as a calibration route for smoothing/unsmoothing and for recovering the classical $R^{2/3}$ sanity bound, but it is not the selected main analytic route.

The active Round 4 state has only two agents, `gpt_pro_thinking` and `gemini_deep_think`; older inactive-agent references should be ignored as historical noise. The uploaded Round 4 prompt also requires strict separation of proved claims, proposed lemmas, rejected routes, and next actions.

Round 4 made useful but non-solution progress:

1. H4 is now more precise: the Vaaler truncation must be used with a Fejer-kernel residual majorant, not with a scalar residual.
2. H5r is now an explicit required residual target, involving parity-supported and untwisted reciprocal sums.
3. H6 is now correctly normalized under the standard reciprocal-phase exponent-pair convention; the endpoint obstruction is $3\kappa+2\lambda\le 1$.
4. H8, the B-process-first route, has a clear Poisson transform and dual length.
5. H9 is a new proved diagnostic: the B-process dual phase $\sqrt{Xhm}$ has zero continuous Hessian, so generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly.

No improvement to the Gauss circle exponent has been proved.

Useful fragments by source:

## From `gpt_pro_thinking`

The most useful Round 4 contribution is the exact formulation of the finite Vaaler step and its residual.

Use

$$
e(t)=e^{2\pi i t},
\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

The proved floor-compatible identity remains:

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
y=\lfloor X^{1/2}\rfloor.
$$

For finite Vaaler, the correct structure is:

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
\qquad
\alpha_h\ll |h|^{-1},
$$

with residual bounded by a Fejer majorant

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t),
$$

where

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2.
$$

This resolves a persistent false-proof risk: one may not replace the Vaaler residual by a scalar $O(D/H_D)$ after summing over $d\sim D$. The nonzero Fourier modes of $K_H$ create further reciprocal sums.

The local dyadic Vaaler cutoff is:

$$
H_D\asymp D X^{-1/4}
$$

for

$$
X^{1/4}\le D\le X^{1/2}.
$$

Blocks with $D<X^{1/4}$ should be handled separately by trivial or short-sum estimates.

The main Vaaler families are:

$$
B_1(H_0,D;X)
=
\sum_{h\sim H_0}u_h
\sum_d
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
B_2(H_0,D;X)
=
\sum_{h\sim H_0}u_h\chi_4(h)
\sum_d
w_D(d)e(hX/(4d)).
$$

The required local ranges are:

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le H_D\asymp D X^{-1/4}.
$$

A sufficient endpoint-strength target is:

$$
B_i(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon},
\qquad i=1,2.
$$

The important Round 4 refinement is H5r. The first-leg Vaaler residual requires estimates for parity-supported sums

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d),
$$

and the second-leg residual requires estimates for shifted untwisted sums

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

A sufficient residual target is:

$$
C_1(K_0,D;X),\ C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}
$$

uniformly for $K_0\le H_D$.

This is likely one of the hardest remaining bottlenecks because H5r is character-blind or only parity-supported.

The second useful contribution is the corrected H6 diagnostic. Under the standard exponent-pair convention for one-dimensional sums, if $f^{(r)}(d)\asymp T D^{-r}$ on $d\asymp D$ and $(\kappa,\lambda)$ is an exponent pair, then

$$
\sum_{d\asymp D}e(f(d))
\ll_\epsilon
T^\kappa D^\lambda X^\epsilon.
$$

For

$$
f(d)=hX/d,
$$

the correct scale is

$$
T\asymp \frac{hX}{D}.
$$

At the endpoint

$$
D\asymp X^{1/2},
\qquad
h\asymp H_0\asymp X^{1/4},
$$

this gives

$$
\sum_{d\asymp D}e(hX/d)
\ll_\epsilon
X^{3\kappa/4+\lambda/2+\epsilon}.
$$

If the outer $h$-sum is treated trivially, the H5 target requires the inner sum to be $\ll X^{1/4+\epsilon}$, hence

$$
3\kappa+2\lambda\le 1.
$$

This should be recorded only as a conditional diagnostic. It does not rule out bilinear, spacing, large-sieve, or Bombieri--Iwaniec methods.

The third useful contribution is the preliminary H8 transform. For

$$
S_\chi(h,D)
=
\sum_d \chi_4(d)w(d/D)e(hX/d),
$$

Poisson summation after splitting modulo $4$ gives

$$
S_\chi(h,D)
=
\frac{i}{2}
\sum_{n\in\mathbb Z}
\chi_4(n)
\int_{\mathbb R}
w(u/D)e(hX/u-nu/4)\,du,
$$

up to the usual Poisson-normalization conventions.

The phase

$$
\phi_n(u)=hX/u-nu/4
$$

has a stationary point only for $n<0$. Writing $n=-m$ with $m>0$ gives

$$
u_0=2\sqrt{\frac{hX}{m}},
$$

so the dual length is

$$
m\asymp \frac{hX}{D^2}.
$$

Thus B-process-first preserves $\chi_4$ as a dual character, but it does not yet produce a saving.

## From `gemini_deep_think`

Gemini’s strongest Round 4 contribution is the confirmation and sharpening of H8. It independently identifies the same B-process-first structure: Poisson summation modulo $4$ transfers $\chi_4$ from the original denominator variable to a dual Gauss factor, hence to $\chi_4(n)$ in the dual variable.

The Gauss factor is:

$$
\sum_{r\bmod 4}\chi_4(r)e(nr/4)
=
e(n/4)-e(3n/4)
=
2i\chi_4(n).
$$

This should be kept as a real structural fact: B-process-first does not immediately discard the character.

Gemini’s second useful contribution is H9. After stationary phase, the dual phase has the form

$$
\Phi(h,m)=\sqrt{Xhm}
$$

up to a nonzero constant and fixed phase shift. Its Hessian is degenerate:

$$
\Phi_{hh}=-\frac14 X^{1/2}m^{1/2}h^{-3/2},
$$

$$
\Phi_{mm}=-\frac14 X^{1/2}h^{1/2}m^{-3/2},
$$

$$
\Phi_{hm}=\frac14 X^{1/2}h^{-1/2}m^{-1/2}.
$$

Therefore

$$
\det\nabla^2\Phi
=
\frac{X}{16hm}
-
\frac{X}{16hm}
=
0.
$$

This is a proved diagnostic. It blocks any future claim that the B-process dual form can be treated by generic full-rank two-dimensional stationary phase or decoupling. It does not block discrete Bombieri--Iwaniec spacing methods.

Gemini also correctly notes that H8 only delays the H7 obstruction. If one applies a direct A-process in the dual variable $m$, then

$$
\chi_4(m)\chi_4(m+q)
$$

again degenerates to a parity-supported factor, by H7.

Rejected or risky ideas:

1. Reject scalar Vaaler residuals.

The statement “Vaaler error is $O(D/H_D)$” is incomplete. The Fejer majorant contains nonzero frequencies. The residual generates sums of the same reciprocal type and must be included as H5r.

2. Reject H8 as a proof route by itself.

B-process-first preserves the character, but it moves the problem to a dual phase $\sqrt{Xhm}$ with zero Hessian. It also leaves open endpoint terms, nonstationary frequencies, and the reappearance of H7 after differencing. H8 is a diagnostic/proposed route, not a proof of cancellation.

3. Reject generic full-rank tools on the B-process dual phase.

H9 proves that the continuous Hessian determinant of $\sqrt{Xhm}$ is zero. Generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly.

4. Reject treating H6 as a general impossibility theorem.

H6 applies only to methods that first take absolute values or trivial summation in $h$ and then use a one-dimensional exponent-pair estimate in $d$. It does not address bilinear, double-large-sieve, spacing, or decoupling methods.

5. Reject $p+2q\le 1$ as the endpoint diagnostic under the standard convention.

With $T\asymp hX/D$, the endpoint condition is

$$
   3\kappa+2\lambda\le 1.
$$

Any other inequality must be tied to a different explicitly named exponent-pair normalization.

6. Reject “$\chi_4$ gives Deligne/Weil savings after A-process.”

H7 shows that direct differencing gives

$$
   \chi_4(d)\chi_4(d+q)
   =
   \begin{cases}
   1_{2\nmid d},& q\equiv 0\pmod 4,\\
   -1_{2\nmid d},& q\equiv 2\pmod 4,\\
   0,& q\equiv 1,3\pmod 4.
   \end{cases}
$$

There is no deep complete character sum at that stage.

7. Reject merging H5a, H5b, and H5r.

H5a has $\chi_4$ in the denominator variable. H5b has $\chi_4$ in the Fourier variable. H5r is parity-supported or untwisted. These are different analytic objects and should remain separate.

Known gaps:

1. Exact stationary-phase lemma for H8.

The current H8 transform is structurally correct but incomplete. It needs:
   - exact Poisson normalization modulo $4$;
   - exact dual phase, including sign and constants;
   - exact main amplitude;
   - dual length and support restrictions;
   - integration-by-parts bounds for nonstationary frequencies;
   - transition treatment near support boundaries;
   - uniformity for $X^{1/4}\le D\le X^{1/2}$ and $1\le h\le D X^{-1/4}$.

2. H5r may be the dominant obstruction.

The residual families

$$
   C_1(K_0,D;X)
$$

and

$$
   C_{2,\rho}(K_0,D;X)
$$

are character-blind or only parity-supported. They may force the problem back to divisor-type reciprocal sums even if H5a has some character structure.

3. H8 does not yet help H5r.

H8 was derived for the spatial-character main family H5a. The residual H5r includes untwisted/parity sums. It is not yet clear whether B-process-first provides any useful mechanism for H5r.

4. Relation to Li--Yang/Bombieri--Iwaniec remains only structural.

The main sums fit Li--Yang-type reciprocal phases with

$$
   T=X,\qquad M=D,\qquad H=H_0,\qquad F(x)=1/x.
$$

The derivative nondegeneracy condition is satisfied:

$$
   F'(x)=-x^{-2},
   \qquad
   F''(x)=2x^{-3},
   \qquad
   F'''(x)=-6x^{-4},
$$

hence

$$
   F'(x)F'''(x)-3F''(x)^2
   =
   -6x^{-6}.
$$

But Li--Yang prove exponent $\theta^*=0.314483\ldots$, not the conjectural $\theta=1/4$. The current H5 targets are endpoint-strength targets, not known estimates.

5. Endpoint and discontinuity conventions remain fragile.

H3 uses the floor-compatible sawtooth

$$
   \psi(t)=t-\lfloor t\rfloor-\frac12.
$$

Vaaler uses continuous trigonometric polynomials plus a residual majorant. The residual is exactly what absorbs half-jump discrepancies at integers. Omitting it invalidates the argument.

6. Poisson--Bessel calibration route is still incomplete.

The repo should still contain the smoothed Poisson--Bessel formula, sandwich/unsmoothing lemma, and $R^{2/3}$ recovery from trivial dyadic radial estimates.

7. Numerical stress tests are still missing.

The exact identities H1--H3 are now well supported, but boundary tests should still be run to catch convention/transcription mistakes.

New lemmas to add:

## H1. Exact symmetric hyperbola identity

Status: proved.

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$, and

$$
S(u)=\sum_{1\le a\le u}\chi_4(a),
$$

one has

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

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$,

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

## H4. Finite Vaaler with residual majorant

Status: theorem dependency; statement now precise enough for the proof draft, but should be checked against a standard Vaaler reference.

For $H\ge 1$,

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
\qquad
\alpha_h\ll |h|^{-1},
$$

and

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t),
$$

with

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

This lemma must be invoked with the residual retained.

## H5a. Spatial-character local dyadic target

Status: sufficient target, not known.

For

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le D X^{-1/4},
$$

define

$$
B_1(H_0,D;X)
=
\sum_{h\sim H_0}u_h
\sum_d
\chi_4(d)w_D(d)e(hX/d).
$$

A sufficient target is:

$$
B_1(H_0,D;X)
\ll_\epsilon H_0X^{1/4+\epsilon}.
$$

## H5b. Frequency-character local dyadic target

Status: sufficient target, not known.

For the same ranges,

$$
B_2(H_0,D;X)
=
\sum_{h\sim H_0}u_h\chi_4(h)
\sum_d
w_D(d)e(hX/(4d)).
$$

A sufficient target is:

$$
B_2(H_0,D;X)
\ll_\epsilon H_0X^{1/4+\epsilon}.
$$

## H5r. Fejer-residual local dyadic targets

Status: required target family, not known.

First-leg residual:

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d).
$$

Second-leg residual:

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

A sufficient target is:

$$
C_1(K_0,D;X),\ C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

This is not a cosmetic residual; it is part of the analytic core.

## H6. Conditional one-dimensional exponent-pair diagnostic

Status: diagnostic, not theorem.

Under the standard reciprocal-phase convention

$$
T\asymp hX/D,
$$

a method that estimates the inner $d$-sum by a one-dimensional exponent pair and treats $h$ trivially must satisfy

$$
3\kappa+2\lambda\le 1
$$

at the endpoint block

$$
D\asymp X^{1/2},
\qquad
H_0\asymp X^{1/4}.
$$

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

Status: partially derived; requires uniform stationary phase before it can be used as a lemma.

For smooth compact support away from zero,

$$
S_\chi(h,D)
=
\sum_d\chi_4(d)w(d/D)e(hX/d)
$$

has the Poisson-dual form

$$
S_\chi(h,D)
=
\frac{i}{2}
\sum_n\chi_4(n)
\int w(u/D)e(hX/u-nu/4)\,du,
$$

up to normalization convention. Stationary phase localizes to $n=-m<0$ with

$$
m\asymp hX/D^2.
$$

The dual character is preserved, but no saving has yet been proved.

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

Therefore generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly to the B-process dual phase.

## B1. Poisson--Bessel calibration lemma

Status: secondary route; still to be written.

The repo should prove the smoothed Poisson--Bessel formula, the smoothing/unsmoothing sandwich, and the classical $E(R)\ll R^{2/3}$ estimate from trivial radial-sum bounds.

Counterexample checks to run:

1. H3 boundary and convention tests.

Evaluate both sides for:
   - $0<X<1$;
   - $X=1,2,3,4,5$;
   - integer squares;
   - integer nonsquares;
   - $X=n^2\pm 10^{-k}$;
   - $X$ just below and above an integer.

2. Vaaler discontinuity tests.

Choose $X,d$ such that one of

$$
   X/d,\qquad
   \frac{X/d+1}{4},\qquad
   \frac{X/d+3}{4}
$$

is integral. Verify that the Fejer residual majorant covers the half-jump discrepancy.

3. H5r stress tests.

Numerically compare

$$
   \frac1{H_D}
   \sum_{1\le k\le H_D}
   \left|
   \sum_d 1_{2\nmid d}w_D(d)e(kX/d)
   \right|
$$

against the conjectural scale $X^{1/4}$ for square and near-square $X$.

4. H8 stationary-phase verification.

Check:
   - sign of the dual variable;
   - exact phase constant;
   - amplitude scale;
   - nonstationary integration-by-parts bounds;
   - behavior near dyadic support boundaries.

5. H9 guardrail check.

Any proposed proof using full-rank two-dimensional stationary phase on $\sqrt{Xhm}$ should be rejected automatically unless it explains why H9 is irrelevant.

6. H7 post-H8 check.

Apply direct differencing to the dual character $\chi_4(m)$ and verify that the same parity collapse occurs. This tests whether H8 really avoids H7 or only delays it.

7. Li--Yang dictionary check.

For $F(x)=1/x$, verify all derivative hypotheses in the relevant Li--Yang setup and record exactly which estimate would need to improve from $\theta^*=0.314483\ldots$ to $\theta=1/4$.

Next round instructions:

## For `gpt_pro_thinking`

Produce the Stage A packet for the next round with three concrete tasks:

1. Insert H4 and H5r into the best proof draft as actual dependencies, not optional refinements.
2. State the Vaaler theorem from a standard reference with exact coefficients or with a clearly cited majorant version sufficient for the proof.
3. Compare H5r, not only H5a/H5b, with the Li--Yang/Bombieri--Iwaniec framework. Determine whether H5r is structurally inside the same known reciprocal-sum class or whether the absolute values in the residual create a strictly harder target.

Also keep the Bessel calibration route alive by writing the minimal Poisson--Bessel/sandwich lemma set needed to recover $E(R)\ll R^{2/3}$.

## For `gemini_deep_think`

Refine H8 into a formal stationary-phase lemma. The output should include:

1. exact Poisson normalization modulo $4$;
2. exact dual phase, including constants and signs;
3. main amplitude;
4. dual length $M_D\asymp hX/D^2$;
5. integration-by-parts bounds for nonstationary frequencies;
6. endpoint and transition treatment;
7. uniformity for

$$
   X^{1/4}\le D\le X^{1/2},
   \qquad
   1\le h\le D X^{-1/4}.
$$

Then explicitly test whether the resulting dual sums help H5r or only H5a. This is the key next question.

Confidence:

High confidence in H1, H2, H3, H6 under stated hypotheses, H7, and H9.

High confidence that H5r must be included and cannot be replaced by a scalar Vaaler error.

Moderate confidence in the H8 Poisson-dual structure and dual length; exact constants, amplitudes, and endpoint terms still need proof.

Moderate confidence that H5a/H5b/H5r are structurally related to Li--Yang/Bombieri--Iwaniec reciprocal sums.

Low confidence that H8 alone gives a route to the conjectural exponent, because the dual phase is Hessian-degenerate and H7 reappears after direct differencing.

Low confidence that current known technology reaches the required H5 endpoint. The present state is a sharpened reduction and obstruction map, not a proof of a new exponent.
