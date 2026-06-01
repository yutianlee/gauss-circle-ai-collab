Summary:
Round 8 Stage A should focus on the Vaaler residual bottleneck rather than on claiming any new exponent. The main analytic route remains the balanced arithmetic hyperbola/Vaaler reduction, but the decisive unresolved object is now the fixed-Fejer residual target H5r-F.

The main contribution of this packet is:

1. formalizing the Abel-summation relation between fixed Fejer averages and partial sums;
2. clarifying that this relation is a diagnostic, not an equivalence between H5r-F and H5r-B;
3. comparing Vaaler, signed Fourier truncation, Perron variants, and Poisson--Bessel smoothing by the error term they create and by whether they preserve the $\chi_4$ sign structure;
4. deriving the signed Fourier high-frequency tail after the hyperbola cut and identifying the precise place where absolute values recreate an H5r-type obstruction;
5. restating R1--R3 and C1 in proof-draft form with correct statuses.

This response uses the current Round 7 state bundle and uploaded background survey as context. Source anchors:

Main claim or direction:
The current Vaaler route should be treated as a conditional reduction:

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

would follow from endpoint-strength control of the Vaaler main families H5a/H5b and the fixed-Fejer residual family H5r-F. However, H5r-F is now the most important bottleneck. It is weaker than arbitrary-coefficient H5r-B as a formal hypothesis, but Abel summation shows that any proof of H5r-F relying only on generic partial-sum bounds is likely to inherit the same character-blind divisor-problem difficulty as H5r-B.

The most useful next analytic fork is not "Vaaler versus no Vaaler" in the abstract. It is:

- either prove H5r-F using fixed Fejer structure in a way that does not reduce to H5r-B/L1;
- or replace Vaaler by a non-majorizing truncation whose error keeps enough signed $\chi_4$ structure to avoid parity-supported or untwisted residual sums.

Detailed reasoning:

## 1. Current exact arithmetic foundation

The proved floor-compatible reduction is:

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

This identity is an arithmetic identity with floor-compatible endpoint convention. It is not yet a Fourier identity. Any finite Fourier step must account for discontinuities and residual majorants.

After dyadic decomposition in the denominator variable $d\sim D$, the important range is

$$
X^{1/4}\le D\le X^{1/2}.
$$

For $D<X^{1/4}$, the trivial bound for the denominator block is already at or below the conjectural scale after logarithmic losses.

The local Vaaler height is

$$
H_D\asymp D X^{-1/4}.
$$

This makes the zero Fejer mode contribute

$$
D/H_D\asymp X^{1/4}.
$$

Thus the zero mode is exactly calibrated to the conjectural scale; all difficulty is in the nonzero Fejer modes.

## 2. Vaaler residual and the three H5r norms

The Vaaler residual is controlled by a Fejer majorant. With

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt),
$$

one uses a bound of the schematic form

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t).
$$

After insertion into the balanced sawtooth formula, the residual families are of the following types:

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d),
$$

and

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

The minimal fixed-Fejer target is:

$$
\mathrm{H5r\text{-}F:}\qquad
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
\ll_\epsilon X^{1/4+\epsilon},
$$

where

$$
\eta_{k,H_D}=1-\frac{|k|}{H_D+1},
$$

and $S_\star$ denotes either $S_{\mathrm{odd}}$ or $S_\rho$.

A stronger sufficient target is arbitrary bounded dyadic control:

$$
\mathrm{H5r\text{-}B:}\qquad
\sum_{k\sim K_0}v_kS_\star(k,D)
\ll_\epsilon K_0X^{1/4+\epsilon},
\qquad |v_k|\le 1,
$$

uniformly for

$$
1\le K_0\le H_D.
$$

A still more visibly destructive version is the termwise $L^1$ estimate:

$$
\mathrm{H5r\text{-}L1:}\qquad
\frac1{H_D}
\sum_{1\le |k|\le H_D}|S_\star(k,D)|
\ll_\epsilon X^{1/4+\epsilon}.
$$

For complex arbitrary coefficients, H5r-B is essentially equivalent to dyadic $L^1$ control, because one may choose $v_k$ to match the conjugate phase of $S_\star(k,D)$.

The correct implication chain is:

$$
\mathrm{H5r\text{-}B}
\Longrightarrow
\mathrm{H5r\text{-}F}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

The reverse implications are not proved.

## 3. Formal Abel-summation diagnostic R4

The fixed Fejer coefficients are positive and monotone on $1\le k\le H$. This produces the following diagnostic.

Let

$$
A(t)=\sum_{1\le k\le t}S_\star(k,D)
$$

for one sign of $k$; the negative $k$ range is handled analogously. Let

$$
\eta_k=1-\frac{k}{H+1}
$$

for $1\le k\le H$. Then Abel summation gives

$$
\sum_{1\le k\le H}\eta_k S_\star(k,D)
=
\eta_H A(H)
+
\sum_{1\le t< H}A(t)(\eta_t-\eta_{t+1}).
$$

Since

$$
\eta_H=\frac1{H+1},
\qquad
\eta_t-\eta_{t+1}=\frac1{H+1},
$$

this becomes

$$
\sum_{1\le k\le H}\eta_k S_\star(k,D)
=
\frac{1}{H+1}A(H)
+
\frac{1}{H+1}\sum_{1\le t< H}A(t).
$$

Thus

$$
\left|
\frac1H\sum_{1\le k\le H}\eta_k S_\star(k,D)
\right|
\le
\frac{1}{H(H+1)}
\left(
|A(H)|+\sum_{1\le t<H}|A(t)|
\right).
$$

This proves the following conditional diagnostic:

If one proves only the generic partial-sum estimate

$$
A(t)\ll_\epsilon tX^{1/4+\epsilon}
$$

for all $1\le t\le H$, then H5r-F follows, but the method has not used anything stronger than H5r-B-type partial-sum control.

More sharply, H5r-F asks for cancellation in the Fejer-weighted average

$$
\sum_{1\le k\le H}\eta_k S_\star(k,D),
$$

not for uniform cancellation in every partial sum $A(t)$. Therefore Abel summation does not prove H5r-F equivalent to H5r-B. It proves only that a proof of H5r-F by monotone partial-sum domination will likely inherit the same divisor-type obstruction.

This is the correct status of R4:

**R4 is a diagnostic lemma, not an obstruction theorem.**

It identifies what a successful proof of H5r-F must avoid: it must exploit the fixed Fejer averaging or the joint $(k,d)$ structure directly, rather than pass through crude partial sums or arbitrary coefficients.

## 4. Non-majorizing comparison with character preservation

| Method | Replacement for H5r | Character preservation | Main risk | Status |
|---|---|---|---|---|
| Vaaler with Fejer majorant | Fixed Fejer residual H5r-F; stronger variants H5r-B/L1 | Main terms preserve $\chi_4$ as spatial or frequency character; residual loses it and becomes parity-supported or untwisted | H5r is divisor-like and may dominate | Current main reduction; bottleneck explicit |
| Signed Fourier truncation | High-frequency signed reciprocal tail beyond $H_D$ | Formally preserves the signs in the original sawtooth expansion longer than Fejer majorization | Tail is not pointwise controlled; bounding absolutely recreates H5r/L1-type difficulty | Candidate non-majorizing route, undeveloped |
| Sharp Perron | Truncation error for $4\zeta(s)L(s,\chi_4)X^s/s$ | Preserves arithmetic in the Dirichlet series | Sharp truncation likely needs large height and delicate endpoint control | Comparison route, not an escape yet |
| Smoothed Perron | Smoothed contour integral with controllable kernel decay | Preserves arithmetic at Dirichlet-series level; smoothing changes endpoint problem | Functional equation likely reconstructs Voronoi/Bessel reciprocal sums | Useful comparison; theorem dependencies needed |
| Poisson--Bessel calibration | Smoothed physical-space annulus error plus Bessel frequency tail | Geometric route; does not use $\chi_4$ directly | Gives only classical $E(R)\ll R^{2/3}$ by trivial dyadic bounds | Sanity-check module, not main route |

## 5. Signed Fourier truncation after the hyperbola cut

The formal Fourier expansion for the centered sawtooth away from discontinuities is

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi ih}.
$$

Suppose one truncates at height $H_D$ on a denominator block $d\sim D$ without replacing the tail by a positive Fejer majorant.

For the first leg, the block contribution has the formal decomposition

$$
-4\sum_{d\sim D}\chi_4(d)w_D(d)\psi(X/d)
=
4\sum_{1\le |h|\le H_D}
\frac{1}{2\pi ih}
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d)
+
\mathcal T_1(D),
$$

where the signed high-frequency tail is formally

$$
\mathcal T_1(D)
=
4\sum_{|h|>H_D}
\frac{1}{2\pi ih}
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d).
$$

For the second leg,

$$
4\sum_{d\sim D}w_D(d)
\left[
\psi\left(\frac{X/d+1}{4}\right)
-
\psi\left(\frac{X/d+3}{4}\right)
\right]
$$

has main frequencies

$$
-4\sum_{1\le |h|\le H_D}
\frac{e(h/4)-e(3h/4)}{2\pi ih}
\sum_{d\sim D}w_D(d)e(hX/(4d)),
$$

and since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the main part retains the frequency character. The high-frequency tail is

$$
\mathcal T_2(D)
=
-4\sum_{|h|>H_D}
\frac{e(h/4)-e(3h/4)}{2\pi ih}
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

The apparent advantage is that $\mathcal T_1(D)$ still contains $\chi_4(d)$ and $\mathcal T_2(D)$ still contains $\chi_4(h)$. Thus signed truncation does not immediately create the parity-supported residual $S_{\mathrm{odd}}$.

However, there is a serious problem: the sawtooth Fourier series is only conditionally convergent and behaves badly at discontinuities. A signed tail bound of the form

$$
\mathcal T_i(D)\ll_\epsilon X^{1/4+\epsilon}
$$

would require cancellation over high frequencies

$$
|h|>H_D.
$$

If one bounds the tail absolutely, then for the first leg one gets

$$
|\mathcal T_1(D)|
\le
\sum_{|h|>H_D}\frac1{|h|}
\left|
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d)
\right|.
$$

There is no useful endpoint bound from this expression unless one has very strong high-frequency reciprocal-sum estimates. Worse, the sum over $h$ is long, and the coefficient $1/h$ is not summable at the needed scale without cancellation.

A naive truncation tail cannot be bounded by the elementary estimate

$$
\left|
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d)
\right|
\le D,
$$

because

$$
\sum_{h>H_D}\frac{D}{h}
$$

diverges unless an artificial upper cutoff is inserted, and with a cutoff it is far too large.

Thus signed Fourier truncation is only useful if one can prove a genuine high-frequency cancellation theorem for the signed tail, preferably using summation in $h$ and $d$ jointly. If one inserts a smoothing kernel to make the tail summable, then the kernel's error term must be stated; it may simply reintroduce a Fejer/de la Vallee Poussin type majorant and hence recreate H5r.

The signed truncation route therefore has the following precise status:

- It may preserve $\chi_4$ better than Vaaler at the formal algebraic level.
- It currently lacks a valid endpoint tail estimate.
- Any proof that bounds the signed tail by absolute values is likely to fall back into an H5r-B/L1-type problem.
- The route is worth keeping only if the next packet states an exact smoothing or summability method for the high-frequency tail.

## 6. R1--R3 and C1 proof-draft insertions

### R1. Fixed-Fejer residual sufficiency

**Status:** proved conditional lemma.

Assume H5r-F for every dyadic block $D$ with

$$
X^{1/4}\le D\le X^{1/2},
$$

and for each residual family $S_\star$ equal to $S_{\mathrm{odd}}$ or $S_\rho$. Then the total Vaaler residual contribution is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof sketch. The zero Fejer mode contributes

$$
D/H_D\asymp X^{1/4}
$$

on each block. H5r-F controls the nonzero Fejer modes on each block. There are $O(\log X)$ dyadic denominator blocks and finitely many residual families, so logarithmic losses are absorbed into $X^\epsilon$.

### R2. Arbitrary bounded coefficients imply fixed Fejer

**Status:** proved conditional lemma.

Assume H5r-B:

$$
\sum_{k\sim K_0}v_kS_\star(k,D)
\ll_\epsilon K_0X^{1/4+\epsilon}
$$

for all $|v_k|\le1$ and all dyadic $K_0\le H_D$. Decompose $1\le |k|\le H_D$ into dyadic $K_0$ blocks and take

$$
v_k=\eta_{k,H_D}
$$

on each block. Then

$$
\sum_{k\sim K_0}\eta_{k,H_D}S_\star(k,D)
\ll_\epsilon K_0X^{1/4+\epsilon}.
$$

Summing over $K_0\le H_D$ gives

$$
\sum_{1\le |k|\le H_D}\eta_{k,H_D}S_\star(k,D)
\ll_\epsilon H_DX^{1/4+\epsilon},
$$

after absorbing logarithmic losses. Dividing by $H_D$ proves H5r-F.

### R3. Complex H5r-B and dyadic L1 equivalence

**Status:** elementary.

If H5r-B is required for all complex coefficients $|v_k|\le1$, then it is equivalent to

$$
\sum_{k\sim K_0}|S_\star(k,D)|
\ll_\epsilon K_0X^{1/4+\epsilon}.
$$

The implication from L1 to H5r-B is immediate by the triangle inequality. Conversely, choose

$$
v_k=
\begin{cases}
\overline{S_\star(k,D)}/|S_\star(k,D)|,& S_\star(k,D)\ne0,\\
0,& S_\star(k,D)=0.
\end{cases}
$$

Then

$$
\sum_{k\sim K_0}v_kS_\star(k,D)
=
\sum_{k\sim K_0}|S_\star(k,D)|.
$$

Thus arbitrary complex H5r-B is not a mild strengthening of H5r-F; it is essentially dyadic termwise $L^1$ control.

### C1. Corrected Fejer Majorant DDP diagnostic

**Status:** conditional diagnostic, not a lower bound.

Assume H5a and H5b are controlled at the conjectural scale. Suppose the only available estimates for H5r are character-blind reciprocal-sum bounds with exponent $\theta$, normalized as

$$
\sum_{k\sim K_0}v_kS_\star(k,D)
\ll_\epsilon K_0X^{\theta+\epsilon}.
$$

Then the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from these inputs.

Reason: the zero Fejer mode contributes $X^{1/4}$ after the choice $H_D\asymp DX^{-1/4}$, and the nonzero residual modes contribute $X^\theta$ by hypothesis after division by $H_D$ and dyadic summation. The larger of these exponents controls the resulting bound.

This is not a theorem that H5r cannot be improved. It is only a bookkeeping statement: the Vaaler route cannot output a better exponent than the exponent inserted into the residual estimate.

## 7. Poisson--Bessel calibration module

The smoothed geometric route remains useful as a normalization check.

Let $\rho$ be a fixed nonnegative smooth compactly supported radial mollifier with integral $1$, and define

$$
\rho_\delta(x)=\delta^{-2}\rho(x/\delta).
$$

Let

$$
S_\delta(R)=\sum_{n\in\mathbb Z^2}(1_{B_R}*\rho_\delta)(n).
$$

Poisson summation gives

$$
S_\delta(R)
=
\sum_{k\in\mathbb Z^2}\widehat{1_{B_R}}(k)\widehat{\rho_\delta}(k).
$$

The zero frequency is

$$
\widehat{1_{B_R}}(0)\widehat{\rho_\delta}(0)=\pi R^2.
$$

For $k\ne0$,

$$
\widehat{1_{B_R}}(k)
=
R\frac{J_1(2\pi R|k|)}{|k|}
$$

under the convention $e(t)=e^{2\pi it}$. Hence

$$
S_\delta(R)-\pi R^2
=
R\sum_{k\ne0}
\frac{J_1(2\pi R|k|)}{|k|}
\widehat{\rho}(\delta k).
$$

Using

$$
J_1(t)\ll t^{-1/2}
$$

for $t\ge1$, and rapid decay of $\widehat\rho$, one obtains

$$
S_\delta(R)-\pi R^2
\ll
R^{1/2}\sum_{k\ne0}|k|^{-3/2}(1+\delta |k|)^{-A}.
$$

Estimating the lattice sum by a radial integral gives

$$
\sum_{k\ne0}|k|^{-3/2}(1+\delta |k|)^{-A}
\ll
\delta^{-1/2},
$$

so

$$
S_\delta(R)-\pi R^2
\ll
R^{1/2}\delta^{-1/2}.
$$

The smoothing sandwich gives

$$
N(R)
\le S_\delta(R+C\delta)
$$

and

$$
N(R)
\ge S_\delta(R-C\delta)
$$

for a constant $C$ depending on the support of $\rho$. The main area changes by

$$
\pi(R+C\delta)^2-\pi R^2
\ll R\delta+\delta^2.
$$

Thus

$$
E(R)
\ll
R\delta+R^{1/2}\delta^{-1/2}.
$$

Balancing

$$
R\delta=R^{1/2}\delta^{-1/2}
$$

gives

$$
\delta=R^{-1/3}
$$

and therefore

$$
E(R)\ll R^{2/3}.
$$

This module proves no new exponent. It verifies the normalization and recovers the classical scale.

Dependencies:

1. The proved balanced sawtooth identity H3.
2. A precise imported Vaaler theorem with Fejer majorant. The coefficient normalization still needs verification against a standard reference.
3. Dyadic partition of unity on $d\le X^{1/2}$.
4. The local Vaaler height choice $H_D\asymp DX^{-1/4}$.
5. Endpoint-strength estimates for H5a, H5b, and H5r-F if the conjectural bound is to be reached.
6. For the Poisson--Bessel calibration: Poisson summation, the Fourier transform of the disk, the Bessel bound $J_1(t)\ll t^{-1/2}$, rapid decay of the mollifier transform, and a smoothing sandwich.

Potential gaps:

1. The exact Vaaler theorem still needs a reference-checked statement, including coefficient formula, residual normalization, and discontinuity convention.
2. H5r-F has not been proved. It is the minimal residual target but remains an endpoint-strength reciprocal-sum estimate.
3. R4 does not prove H5r-F equivalent to H5r-B. It only shows that partial-sum methods may lose the fixed-Fejer advantage.
4. Signed Fourier truncation has no valid high-frequency tail bound yet.
5. If signed truncation is regularized by a smoothing kernel, the new error term may recreate a Fejer-like residual.
6. H5r-to-Li--Yang compatibility is still structural, not theorem-level. The exact theorem must accept the needed weights, parity coefficients, ranges, and absolute-value placement.
7. The C2 odd-lattice Poisson transform still needs stationary-phase constants and boundary analysis.
8. Mellin--Perron remains a comparison route. Its truncation and functional-equation analysis may reconstruct the same reciprocal-sum difficulty.
9. The Poisson--Bessel calibration should be committed as a separate module and not confused with the arithmetic route.

Counterexample or obstruction search:

1. **Abel-summation trap.**
   Try to prove H5r-F using only bounds for partial sums

$$
   A(t)=\sum_{1\le k\le t}S_\star(k,D).
$$

   If this is the only mechanism, the proof likely reduces to H5r-B-type difficulty.

2. **Fejer spike test.**
   Test square and near-square $X$ where many values of $X/d$ or $(X/d+\rho)/4$ approach integers. The Fejer kernel can spike in these cases.

3. **Fixed Fejer versus L1 numerical gap.**
   Compare

$$
   \left|
   \frac1{H_D}
   \sum_{1\le |k|\le H_D}\eta_{k,H_D}S_\star(k,D)
   \right|
$$

   with

$$
   \frac1{H_D}
   \sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

   A persistent large gap would suggest that fixed Fejer averaging retains useful cancellation. Comparable sizes would support the H5r-B bottleneck concern.

4. **Signed Fourier tail obstruction.**
   Check whether the signed high-frequency tail can be summed by cancellation over $h$ and $d$. If every available proof bounds it absolutely, signed truncation probably does not improve on Vaaler.

5. **C2 boundary test.**
   In the odd-lattice Poisson transform, the boundary regime

$$
   D\asymp X^{1/2},
   \qquad
   k\asymp1
$$

   has dual length $O(1)$. Stationary phase must not be applied blindly there.

6. **Mellin--Perron circularity diagnostic.**
   After applying the functional equation to $4\zeta(s)L(s,\chi_4)$, check whether the resulting oscillatory sums are essentially Voronoi/Bessel reciprocal sums of length $X^{1/2}$. If yes, the route is likely a reformulation, not an escape.

Useful lemmas:

## R4. Abel-summation diagnostic for H5r-F

**Status:** proposed diagnostic lemma.

For one-sided positive frequencies, let

$$
A(t)=\sum_{1\le k\le t}S_\star(k,D),
\qquad
\eta_k=1-\frac{k}{H+1}.
$$

Then

$$
\sum_{1\le k\le H}\eta_kS_\star(k,D)
=
\frac{1}{H+1}A(H)
+
\frac{1}{H+1}\sum_{1\le t<H}A(t).
$$

Therefore H5r-F follows from sufficiently strong partial-sum estimates, but such a proof may inherit H5r-B-type difficulty. The lemma does not prove H5r-F equivalent to H5r-B.

## R1. Fixed-Fejer residual sufficiency

**Status:** proved conditional lemma.

H5r-F on every dyadic denominator block and residual family implies that the total Vaaler residual is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

## R2. Arbitrary bounded coefficients imply fixed Fejer

**Status:** proved conditional lemma.

H5r-B implies H5r-F by dyadic decomposition in $k$ and division by $H_D$.

## R3. Complex H5r-B equals dyadic L1

**Status:** elementary.

For arbitrary complex coefficients $|v_k|\le1$, H5r-B is equivalent to dyadic $L^1$ control of $S_\star(k,D)$.

## C1. Corrected Fejer Majorant DDP diagnostic

**Status:** conditional diagnostic.

If H5r is bounded only by character-blind reciprocal estimates with exponent $\theta$, then the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs.

## SF1. Signed Fourier truncation tail

**Status:** proposed comparison lemma.

After truncating

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi ih}
$$

at $H_D$, the first-leg tail is

$$
\mathcal T_1(D)
=
4\sum_{|h|>H_D}
\frac{1}{2\pi ih}
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
$$

and the second-leg tail is

$$
\mathcal T_2(D)
=
-4\sum_{|h|>H_D}
\frac{e(h/4)-e(3h/4)}{2\pi ih}
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

These preserve character structure formally but currently lack endpoint tail estimates.

## B1. Poisson--Bessel calibration lemma

**Status:** standard calibration module.

Smoothing and Poisson summation yield

$$
E(R)\ll R\delta+R^{1/2}\delta^{-1/2},
$$

and choosing $\delta=R^{-1/3}$ gives

$$
E(R)\ll R^{2/3}.
$$

What should be tested next:

1. Numerically compare H5r-F, H5r-B, and H5r-L1 for square, nonsquare, and near-square $X$.
2. Test whether fixed Fejer weights produce cancellation not visible in arbitrary-coefficient or L1 norms.
3. Derive a rigorous stationary-phase statement for the C2 odd-lattice Poisson transform, including constants and boundary cases.
4. Audit a precise Li--Yang/Bombieri--Iwaniec theorem against H5r-F, not only against schematic reciprocal sums.
5. Attempt to bound the signed Fourier tail $\mathcal T_1(D)+\mathcal T_2(D)$ without absolute values. If impossible, record exactly where H5r reappears.
6. Write sharp and smoothed Perron truncation errors for $4\zeta(s)L(s,\chi_4)$ and identify the height/moment input needed for $X^{1/4+\epsilon}$.
7. Commit the Poisson--Bessel calibration module as a secondary normalization proof.
8. Keep H5r-F as the official minimal residual target; do not silently replace it by H5r-B unless the stronger loss is intentional.

Confidence:
High confidence that H5r-F is the correct minimal residual target for the Vaaler route.

High confidence in the implication chain

$$
\mathrm{H5r\text{-}B}
\Longrightarrow
\mathrm{H5r\text{-}F}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

High confidence that complex H5r-B is equivalent to dyadic $L^1$ control.

Moderate-to-high confidence that R4 correctly captures the Abel-summation diagnostic and should be added as a proposed lemma, not as a theorem-level obstruction.

Moderate confidence that signed Fourier truncation preserves character structure formally, but low confidence that its high-frequency tail can be bounded at endpoint strength without recreating H5r.

Moderate confidence that the Poisson--Bessel calibration proof is standard and should be included as a sanity check.

Low confidence that the current route proves any exponent improvement. The present contribution is a sharper map of the residual bottleneck and a clearer set of alternatives to test.
