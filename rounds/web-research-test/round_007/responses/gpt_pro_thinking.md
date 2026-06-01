Summary:

Source anchors: Round 6 packet and current state bundle from the uploaded prompt:. Uploaded background survey used only as non-proof background:. For the Vaaler dependency, the next repo audit should verify the exact theorem against Vaaler's original paper; a reference note points to Vaaler's "Some Extremal Functions in Fourier Analysis", Bull. AMS 12(2), 1985, pp. 183--216, beginning around p. 206, and records a representative Vaaler polynomial/Fejer-kernel formulation.

This is a Round 7 Stage A independent-reasoning packet for `gpt_pro_thinking`.

No new exponent for the Gauss circle problem is proved here. The main contribution is a precise norm-level theorem for the Vaaler residual H5r, a corrected conditional C1 diagnostic, a convention-fixed Poisson formula for the odd-lattice residual C2, and a comparison of Vaaler, signed Fourier truncation, and Mellin--Perron alternatives.

The principal conclusion is:

H5r-F is the minimal fixed-Fejer residual estimate naturally required by the current Vaaler proof. H5r-B is a stronger sufficient estimate; in the stated arbitrary-coefficient form it is essentially equivalent to a dyadic termwise $L^1$ estimate by duality. H5r-F is enough to make the Vaaler residual $O_\epsilon(X^{1/4+\epsilon})$ after summing dyadic denominator blocks, but H5r-F itself is an endpoint-strength reciprocal-sum input and remains unproved.

Main claim or direction:

The next proof draft should record the following dependency chain as a theorem schema:

$$
\text{H5r-B} \Longrightarrow \text{H5r-F} \Longrightarrow
\text{Vaaler residual contribution} \ll_\epsilon X^{1/4+\epsilon}.
$$

The fixed-Fejer target H5r-F is the correct minimum target for the current positive-majorant Vaaler route. The arbitrary bounded coefficient target H5r-B is convenient for comparison with bilinear or Bombieri--Iwaniec/Li--Yang-type estimates, but it is stronger than the proof strictly needs.

The conditional C1 diagnostic should be recorded in the corrected form:

If the only available estimates for H5r are character-blind reciprocal-sum estimates with exponent $\theta$, normalized as

$$
\sum_{k\sim K_0} v_k S_\star(k,D)
\ll_\epsilon
K_0 X^{\theta+\epsilon},
$$

then the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs, assuming the main Vaaler families H5a and H5b are already controlled at the conjectural scale. This is not a lower bound and not an impossibility theorem.

The C2 odd-lattice Poisson transform is valid, but only as a transformation lemma. The alternating dual coefficient $(-1)^m$ appears under one convention, while an equivalent two-coset formulation also exists. Therefore C2/C3 should remain diagnostic, not a proved obstruction.

Detailed reasoning:

## 1. Baseline arithmetic identity

Retain the proved floor-compatible reduction:

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
\psi(t)=t-\lfloor t\rfloor-\frac12,
\qquad
e(t)=e^{2\pi i t}.
$$

This identity is an arithmetic/floor identity, not a Fourier identity. The endpoint convention is

$$
\psi(n)=-\frac12
\qquad
(n\in\mathbb Z).
$$

The Vaaler step must therefore be treated as an approximation to this floor-compatible sawtooth, with its residual retained.

## 2. Vaaler input used in the proof skeleton

Use the following theorem dependency, pending exact reference audit.

For every integer $H\ge 1$, there is a trigonometric polynomial

$$
A_H(t)=\sum_{1\le |h|\le H}\alpha_{h,H}e(ht),
\qquad
\alpha_{h,H}\ll \frac1{|h|},
$$

such that

$$
\psi(t)=A_H(t)+R_H(t)
$$

and

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t),
$$

where the Fejer kernel is

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

Write

$$
\eta_{k,H}=1-\frac{|k|}{H+1}.
$$

Then

$$
K_H(t)=
1+\sum_{1\le |k|\le H}\eta_{k,H}e(kt).
$$

This is the exact point where the positive majorant loses the original $\chi_4$ sign structure in the residual.

## 3. Dyadic localization and local height

Insert a smooth nonnegative dyadic partition of unity in the denominator variable. Let $w_D$ be supported on $d\asymp D$, with

$$
X^{1/4}\le D\le X^{1/2}.
$$

Use the local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

For $D<X^{1/4}$, the sawtooth sums have length $O(D)$, so their total contribution over all short dyadic blocks is

$$
\ll X^{1/4+\epsilon}
$$

by trivial estimation and dyadic summation. Thus H5r is only needed for

$$
X^{1/4}\le D\le X^{1/2}.
$$

## 4. First-leg residual and H5r-F

The first leg is

$$
-4\sum_d \chi_4(d) w_D(d)\psi(X/d).
$$

After Vaaler,

$$
\psi(X/d)=A_{H_D}(X/d)+R_{H_D}(X/d).
$$

The residual contribution is bounded by

$$
\sum_d |\chi_4(d)|w_D(d)|R_{H_D}(X/d)|.
$$

Since

$$
|\chi_4(d)|=1_{2\nmid d},
$$

the Fejer majorant gives

$$
\sum_d |\chi_4(d)|w_D(d)|R_{H_D}(X/d)|
\ll
\frac1{H_D}
\sum_{\substack{d\\2\nmid d}}w_D(d)K_{H_D}(X/d).
$$

Define

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\\2\nmid d}}w_D(d)e(kX/d).
$$

Then the residual is bounded by

$$
\frac1{H_D}
\left[
S_{\mathrm{odd}}(0,D)
+
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_{\mathrm{odd}}(k,D)
\right].
$$

The zero mode is

$$
\frac1{H_D}S_{\mathrm{odd}}(0,D)
\ll
\frac{D}{H_D}
\asymp
X^{1/4}.
$$

Therefore the required nonzero-mode fixed-Fejer target is:

**H5r-F, first leg.** For every dyadic $D$ in the local range,

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_{\mathrm{odd}}(k,D)
\right|
\ll_\epsilon
X^{1/4+\epsilon}.
$$

This is exactly sufficient for the first-leg residual.

## 5. Second-leg residual and H5r-F

The second leg is

$$
4\sum_d w_D(d)
\left[
\psi\left(\frac{X/d+1}{4}\right)
-
\psi\left(\frac{X/d+3}{4}\right)
\right].
$$

The main Vaaler polynomial keeps the frequency-character transfer

$$
e(h/4)-e(3h/4)=2i\chi_4(h).
$$

The residual does not keep this signed transfer if we use the pointwise majorant. Instead,

$$
\left|
R_{H_D}\left(\frac{X/d+\rho}{4}\right)
\right|
\le
\frac1{2H_D+2}
K_{H_D}\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\}.
$$

Define

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_d w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

Then the second residual is bounded by zero modes of size

$$
\ll D/H_D\asymp X^{1/4}
$$

plus the two fixed-Fejer nonzero sums

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\rho(k,D)
\right|.
$$

Thus:

**H5r-F, second leg.** For $\rho\in\{1,3\}$,

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\rho(k,D)
\right|
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Together, the first- and second-leg H5r-F estimates imply that the full Vaaler residual over one dyadic denominator block is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Summing over $O(\log X)$ dyadic blocks gives

$$
\ll_\epsilon X^{1/4+\epsilon}
$$

after absorbing logarithms into $X^\epsilon$.

## 6. H5r-B implies H5r-F

State the stronger arbitrary bounded dyadic target:

**H5r-B.** For every dyadic $K_0\le H_D$, every $|v_k|\le 1$, and each residual family $S_\star\in\{S_{\mathrm{odd}},S_1,S_3\}$,

$$
\sum_{k\sim K_0} v_k S_\star(k,D)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

Then decompose

$$
1\le |k|\le H_D
$$

into dyadic blocks $K_0$. On each block, take

$$
v_k=\eta_{k,H_D}
$$

or the corresponding phase-adjusted bounded coefficient. Since $|\eta_{k,H_D}|\le 1$,

$$
\sum_{k\sim K_0}\eta_{k,H_D}S_\star(k,D)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

Therefore

$$
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\ll_\epsilon
\frac1{H_D}
\sum_{K_0\le H_D}K_0X^{1/4+\epsilon}
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Hence

$$
\text{H5r-B}\Longrightarrow\text{H5r-F}.
$$

## 7. Relation between H5r-B and H5r-L1

There are two possible meanings of H5r-L1, and the repo should distinguish them.

### Global fixed-range H5r-L1

If one assumes only

$$
\frac1{H_D}
\sum_{1\le |k|\le H_D}|S_\star(k,D)|
\ll_\epsilon
X^{1/4+\epsilon},
$$

then this directly implies H5r-F by the triangle inequality. It does not automatically imply the dyadic arbitrary-coefficient estimate H5r-B for every sub-block $K_0$ unless the same estimate is available locally on each dyadic interval.

### Dyadic H5r-L1

If one assumes, for every $K_0\le H_D$,

$$
\sum_{k\sim K_0}|S_\star(k,D)|
\ll_\epsilon
K_0X^{1/4+\epsilon},
$$

then it is equivalent to H5r-B up to constants. Indeed:

- dyadic H5r-L1 implies H5r-B by the triangle inequality;
- H5r-B implies dyadic H5r-L1 by choosing

$$
v_k=
\begin{cases}
\overline{S_\star(k,D)}/|S_\star(k,D)|,&S_\star(k,D)\ne0,\\
0,&S_\star(k,D)=0.
\end{cases}
$$

Thus, in the arbitrary bounded coefficient formulation, H5r-B is not meaningfully weaker than dyadic termwise $L^1$. It is stronger than the fixed-Fejer target H5r-F.

This matters because a proof of H5r-F may exploit the exact Fejer coefficients and possible cancellation between $k$-frequencies. A proof of H5r-B cannot exploit that fixed coefficient structure.

## 8. Corrected C1 diagnostic

Assume the main Vaaler families H5a and H5b are controlled at the target scale:

$$
B_i(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon},
\qquad i=1,2.
$$

Assume also that the only available residual input is a character-blind reciprocal estimate with exponent $\theta$:

$$
\sum_{k\sim K_0}v_kS_\star(k,D)
\ll_\epsilon
K_0X^{\theta+\epsilon}
$$

for each residual family $S_\star$.

Then the same proof as above gives

$$
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\ll_\epsilon
X^{\theta+\epsilon}.
$$

The zero mode contributes

$$
D/H_D\asymp X^{1/4}.
$$

Therefore the Vaaler residual is controlled by

$$
X^{\max(1/4,\theta)+\epsilon}.
$$

Consequently the whole route gives, from these inputs,

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}.
$$

This is the corrected C1 statement. The incorrect product-like scaling $X^{1/4+\theta}$ should not be used.

## 9. Convention-fixed C2 Poisson formula

Let

$$
F(u)=w_D(u)e(kX/u),
$$

where $w_D$ is smooth and supported on positive $u\asymp D$.

Use the Fourier transform convention

$$
\widehat F(\xi)=\int_{\mathbb R}F(u)e(-\xi u)\,du.
$$

Then

$$
\sum_{d\in\mathbb Z}F(d)
=
\sum_{m\in\mathbb Z}\widehat F(m).
$$

The odd-lattice sum is

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{2\nmid d}F(d).
$$

### Form 1: odd sublattice

Writing $d=2\ell+1$ and applying Poisson in $\ell$ gives

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\in\mathbb Z}
(-1)^m
\int_{\mathbb R}
w_D(u)
e\left(\frac{kX}{u}-\frac{mu}{2}\right)
\,du.
$$

This proves the alternating-factor representation under the stated convention.

### Form 2: integer minus half-integer dual frequencies

Since

$$
1_{2\nmid d}=\frac12(1-e(d/2)),
$$

one also has

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\in\mathbb Z}
\left[
\widehat F(m)-\widehat F(m-1/2)
\right].
$$

Equivalently,

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\in\mathbb Z}
\int_{\mathbb R}w_D(u)e(kX/u)
\left[
e(-mu)-e(-(m-1/2)u)
\right]
\,du.
$$

These two formulas are equivalent by reindexing and Poisson normalization. Therefore the appearance of $(-1)^m$ is real, but it is representation-dependent. It should not be promoted to an unconditional obstruction by itself.

## 10. Stationary phase for C2

For

$$
I_m(k,D)
=
\int_{\mathbb R}
w_D(u)
e\left(\frac{kX}{u}-\frac{mu}{2}\right)
\,du,
$$

the phase is

$$
\phi_m(u)=\frac{kX}{u}-\frac{mu}{2}.
$$

Then

$$
\phi_m'(u)=-\frac{kX}{u^2}-\frac m2.
$$

A stationary point exists only when $m<0$. Write $m=-\ell$, $\ell>0$. Then

$$
u_0=\left(\frac{2kX}{\ell}\right)^{1/2}.
$$

Since $w_D$ is supported on $u\asymp D$, the active dual length is

$$
\ell\asymp \frac{kX}{D^2}.
$$

At the stationary point,

$$
\phi_{-\ell}(u_0)
=
\frac{kX}{u_0}+\frac{\ell u_0}{2}
=
\sqrt{2kX\ell}.
$$

Also,

$$
\phi_{-\ell}''(u_0)
=
\frac{2kX}{u_0^3}
\asymp
\frac{kX}{D^3}.
$$

Thus the expected stationary-phase amplitude is

$$
\asymp
\left(\frac{kX}{D^3}\right)^{-1/2}
=
\frac{D^{3/2}}{(kX)^{1/2}},
$$

up to a smooth amplitude depending on

$$
\frac{\ell D^2}{kX}.
$$

A formal stationary-phase lemma should have the shape

$$
I_{-\ell}(k,D)
=
\frac{D^{3/2}}{(kX)^{1/2}}
a\left(\frac{\ell D^2}{kX}\right)
e\left(\sqrt{2kX\ell}+\frac18\right)
+
\text{lower-order terms},
$$

where $a$ is smooth and supported on a compact subinterval of $(0,\infty)$ determined by $w_D$. The sign of the $1/8$ phase depends on the Fourier and stationary-phase conventions and must be checked before committing.

For $m$ outside the active range, repeated integration by parts should give rapid decay. The boundary regimes remain nontrivial, especially

$$
D\asymp X^{1/2},\qquad k\asymp 1,
$$

where the active dual length is $O(1)$.

## 11. H10: non-majorizing comparison

| Method | Replacement for H5r | What it preserves | Current status |
|---|---|---|---|
| Vaaler with Fejer majorant | Fixed-Fejer residual H5r-F, or stronger H5r-B/H5r-L1 | Pointwise control of sawtooth; loses $\chi_4$ in residual after absolute values | Exact route but central bottleneck |
| Signed Fourier truncation | High-frequency signed tail beyond $H_D$ | May preserve $\chi_4$ or signed cancellation longer | Not yet useful; the tail is not absolutely convergent and may require estimates at larger frequencies |
| Mellin--Perron | Truncation error plus contour integral for $4\zeta(s)L(s,\chi_4)X^s/s$ | Preserves arithmetic Dirichlet-series structure | Standard reformulation; likely leads to moment/subconvexity or Voronoi/Bessel sums |
| Smoothed Perron | Weighted contour integral with faster vertical decay | Preserves arithmetic structure and reduces sharp cutoff error | Gives smoothed discrepancy; unsmoothing may reintroduce boundary losses |
| Poisson--Bessel calibration | Bessel/radial frequency sums | Good normalization and recovery of $R^{2/3}$ | Calibration route, not a new endpoint path |

For Mellin--Perron, the formal sharp cutoff is

$$
\sum_{n\le X}r_2(n)
=
\frac{1}{2\pi i}
\int_{c-iT}^{c+iT}
4\zeta(s)L(s,\chi_4)\frac{X^s}{s}\,ds
+
\text{truncation error},
\qquad c>1.
$$

The pole at $s=1$ gives the main term $\pi X$. To reach

$$
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

one would need either a contour/moment input strong enough after shifting, or a functional-equation/Voronoi transformation whose resulting oscillatory sums are no harder than the original H5 targets. At present this is a comparison route, not an escape.

Dependencies:

1. H1--H3 are used as proved floor-compatible reductions.

2. The Vaaler theorem is used only in the majorant form

$$
|R_H(t)|\le (2H+2)^{-1}K_H(t).
$$

The exact coefficient formula for $\alpha_{h,H}$ is not needed for H5r, but it is needed for the main terms H5a/H5b and should be audited.

3. The dyadic partition should be nonnegative for the clean residual-majorant argument. If signed dyadic partitions are used, the proof must replace $w_D$ by $|w_D|$ in the residual families.

4. The local height

$$
H_D\asymp D X^{-1/4}
$$

is required to make the Fejer zero mode exactly conjectural scale:

$$
D/H_D\asymp X^{1/4}.
$$

5. H5a and H5b are not proved here. The norm theorem only handles the residual implication once the relevant H5r estimate is supplied.

6. The C2 formula depends on the Fourier convention

$$
\widehat F(\xi)=\int F(u)e(-\xi u)\,du.
$$

Changing this convention reverses signs in the dual phase.

Potential gaps:

1. **Exact Vaaler citation.** The repo still needs the precise theorem statement from Vaaler or a standard analytic-number-theory reference. The coefficient formula and majorant normalization should be checked before marking H4 as an imported theorem.

2. **Discontinuity convention.** H3 uses $\psi(n)=-1/2$, while trigonometric approximations encode midpoint behavior through a residual. The proof is safe only if the residual majorant is retained at all discontinuities.

3. **H5r-F may be much easier than H5r-B.** H5r-F has fixed Fejer coefficients. H5r-B permits arbitrary bounded coefficients and is equivalent to dyadic $L^1$. Future estimates should not silently replace H5r-F by H5r-B unless the stronger target is intended.

4. **Absolute-value placement.** The Vaaler residual proof uses pointwise positivity, then one block-level absolute value for the nonzero Fejer sum. Termwise absolute values in $k$ are sufficient but may be too destructive.

5. **C2 obstruction status.** The alternating factor $(-1)^m$ appears, but the two-coset formulation may retain spacing information. C3 is therefore only a diagnostic.

6. **Boundary stationary phase.** The C2 dual length

$$
M\asymp kX/D^2
$$

can be $O(1)$ at the edge $D\asymp X^{1/2}$ and $k\asymp1$. Such cases require separate estimates.

7. **Mellin--Perron may be circular.** The contour route may reproduce Voronoi/Hardy/Bessel sums after the functional equation. This is a diagnostic, not a proof of failure.

8. **Known technology gap.** H5r lies structurally in the reciprocal-sum/divisor-problem class after residue splitting. Existing record exponents do not by themselves provide the endpoint $1/4$ estimate.

Counterexample or obstruction search:

1. **Fejer spike cases.** Test $X,d$ for which

$$
X/d,\qquad
\frac{X/d+1}{4},\qquad
\frac{X/d+3}{4}
$$

is near an integer. These are exactly where $K_H$ can spike and where scalar residual estimates fail.

2. **Fixed Fejer versus arbitrary coefficients.** Numerically compare

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
$$

against

$$
\frac1{H_D}\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

A large separation would indicate that H5r-F is meaningfully weaker than H5r-B/L1.

3. **Odd-lattice Poisson convention check.** Verify directly on compactly supported test functions that

$$
\sum_{2\nmid d}F(d)
=
\frac12
\sum_m(-1)^m
\int F(u)e(-mu/2)\,du
$$

matches

$$
\frac12
\sum_m
\left[
\widehat F(m)-\widehat F(m-1/2)
\right].
$$

4. **C3 two-coset A-process test.** Apply differencing in both C2 representations. Determine whether the two-coset phases retain spacing information that the one-sequence $(-1)^m$ coefficient representation hides.

5. **Stationary-phase constants.** For

$$
I_m=\int w_D(u)e(kX/u-mu/2)\,du,
$$

check the active sign of $m$, the stationary point, the phase constant, and the $e(1/8)$ signature.

6. **H5r-to-Li--Yang audit.** Write $S_{\mathrm{odd}}$ and $S_\rho$ in the exact form required by a candidate Bombieri--Iwaniec/Li--Yang theorem, including weights and absolute-value placement. Do not assume theorem compatibility from phase shape alone.

7. **Signed Fourier tail.** Test whether a signed truncation of

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi i h}
$$

after hyperbola cutting produces a controllable high-frequency tail or simply moves H5r to larger $h$.

Useful lemmas:

## Lemma R1. Fixed-Fejer residual sufficiency

Status: proved conditional lemma.

Assume H5r-F for $S_{\mathrm{odd}}$, $S_1$, and $S_3$ on every dyadic denominator block

$$
X^{1/4}\le D\le X^{1/2}.
$$

Then the total Vaaler residual in the balanced sawtooth formula is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof: zero Fejer modes contribute $D/H_D\asymp X^{1/4}$ per block. Nonzero Fejer modes are bounded by H5r-F. There are $O(\log X)$ blocks, absorbed into $X^\epsilon$.

## Lemma R2. Arbitrary bounded coefficients imply fixed Fejer

Status: proved conditional lemma.

H5r-B implies H5r-F.

Proof: dyadically decompose $1\le |k|\le H_D$ and use $v_k=\eta_{k,H_D}$ on each block. Divide by $H_D$ and sum the dyadic lengths.

## Lemma R3. H5r-B and dyadic H5r-L1 equivalence

Status: elementary.

If H5r-B is stated for all complex coefficients $|v_k|\le1$, then it is equivalent to the dyadic termwise $L^1$ estimate

$$
\sum_{k\sim K_0}|S_\star(k,D)|
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

The implication from H5r-B to dyadic H5r-L1 follows by choosing $v_k$ to match the phase of $S_\star(k,D)$.

## Lemma C1. Corrected Fejer Majorant DDP diagnostic

Status: conditional diagnostic.

If H5r is bounded only by character-blind reciprocal estimates at exponent $\theta$, then the Vaaler route gives

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs, assuming H5a/H5b are handled at the target scale.

## Lemma C2. Odd-lattice Poisson transform

Status: transformation proved up to Fourier convention.

For

$$
F(u)=w_D(u)e(kX/u)
$$

and

$$
\widehat F(\xi)=\int F(u)e(-\xi u)\,du,
$$

one has

$$
\sum_{2\nmid d}F(d)
=
\frac12
\sum_m(-1)^m
\int F(u)e(-mu/2)\,du
=
\frac12
\sum_m
\left[
\widehat F(m)-\widehat F(m-1/2)
\right].
$$

The stationary range is

$$
|m|\asymp kX/D^2.
$$

## Lemma C3. Dual parity A-process diagnostic

Status: diagnostic only.

In the one-sequence C2 representation, direct differencing of the coefficient gives

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

This shows that the coefficient alone has no nontrivial residual mod-$2$ oscillation under direct A-process. It does not rule out two-coset spacing arguments.

What should be tested next:

1. Commit Lemmas R1--R3 and C1--C3 to the lemma bank with the statuses above.

2. Insert H5r-F, not only H5r-B, into the best proof draft as the minimal residual dependency.

3. Audit the exact Vaaler theorem and record the coefficient formula and majorant normalization.

4. Run numerical H5r norm comparisons for square, nonsquare, and near-square $X$:

$$
\text{fixed Fejer}
\quad \text{vs.} \quad
\text{dyadic arbitrary coefficients}
\quad \text{vs.} \quad
\text{termwise }L^1.
$$

5. Have `gemini_deep_think` focus on the C2 two-coset formulation and whether spacing information survives differencing.

6. Have `deepseek_api` verify the C2 Poisson signs, stationary-phase constants, and boundary regimes, and run the H5r numerical tests.

7. Continue the Mellin--Perron comparison, but do not promote it until its truncation error is shown to be different from H5r or from the standard Voronoi/Bessel difficulty.

Confidence:

High confidence in the implication

$$
\text{H5r-F}\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

High confidence that H5r-B implies H5r-F.

High confidence that arbitrary-coefficient H5r-B is essentially equivalent to dyadic termwise $L^1$ by duality.

High confidence in the corrected C1 normalization

$$
X^{\max(1/4,\theta)+\epsilon}.
$$

Moderate-to-high confidence in the C2 Poisson formula under the stated Fourier convention.

Moderate confidence in the stationary-phase shape and dual length

$$
|m|\asymp kX/D^2.
$$

Low confidence that the Vaaler route reaches the conjectural exponent without a genuinely new endpoint reciprocal-sum estimate for H5r-F or a sign-preserving replacement for the Fejer majorant.

No claim here improves the known Gauss circle exponent.
