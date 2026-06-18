## Summary

Source basis: Round 23 prompt, human strategy revision, A1/A2/A3 Stage A outputs, and Stage B reviews in the uploaded Round 23 bundle. The Round 23 materials explicitly keep the balanced arithmetic hyperbola/Vaaler reduction, state that M9 remains open, and record that no new Gauss circle exponent has been proved.

Round 23 is a proof-infrastructure and finite-statistic round. It does not establish a new estimate for the Gauss circle problem. The conservative bridge remains:

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

Here

$$
P(X)=N(\sqrt X)-\pi X.
$$

The residual side is provisionally controlled by H4 plus R5-Full. The active analytic bottleneck remains M9: the fixed-Vaaler-coefficient main sums $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$.

Round 23 adds three useful items:

1. A1 has now made H4/R5/Bridge/M9 proof-draft-ready in substance, with Vaaler source anchors, edge-case handling, and the correct coefficient algebra.
2. A2 gives the main new analytic direction: precise $\mathcal M_2$ Cauchy--Schwarz diagnostics, an exact fourth-moment candidate $\mathcal Q_4$, and a CRI falsification statistic.
3. A3 gives useful formula auditing and verification discipline, but still mostly supplies protocols and tiny examples; the next round needs reproducible data, especially for R5, M9 paired regression, CRI, and fourth-moment bins.

The most important strategic update is that Round 24 should be narrow and empirical-formulaic. Keep the balanced hyperbola/Vaaler route as the main line while converting the finite statistics into executable objects and testing them before expanding to more speculative alternatives.

## Selected main route

Keep the balanced arithmetic hyperbola/Vaaler framework:

$$
P(X)=N(\sqrt X)-\pi X
\longrightarrow
\text{symmetric hyperbola}
\longrightarrow
\text{floor-compatible sawtooth}
\longrightarrow
\text{finite Vaaler}
\longrightarrow
\text{fixed-coefficient reciprocal main sums}.
$$

The accepted arithmetic identity is still

$$
P(X)
=
-4\sum_{d\le y}\chi_4(d)\psi_F(X/d)
+
4\sum_{d\le y}
\left[
\psi_F\left(\frac{X/d+1}{4}\right)
-
\psi_F\left(\frac{X/d+3}{4}\right)
\right]
+
O(1),
$$

where

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
\psi_F(t)=t-\lfloor t\rfloor-\frac12,
\qquad
\psi_F(n)=-\frac12.
$$

For active dyadic denominator blocks,

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ are removed before Vaaler expansion and bounded directly by $|\psi_F|\le 1/2$.

The Vaaler coefficients are frozen as

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

The official open M9 target is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for $X^{1/4}\le D\le X^{1/2}$, where

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_d
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_d
w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

one may also write

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_d
w_D(d)e(hX/(4d)).
$$

No Round 23 output proves M9.

## Useful fragments by source

### From A1

A1 supplies the strongest proof-draft consolidation.

The useful bridge remains:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

A1's H4 source normalization should be adopted. The Vaaler anchors are:

- Theorem 6, printed page 192, equation (2.28), for $\widehat J$.
- Section 7, printed page 207, equations (7.1)--(7.3), for $i_N,j_N,k_N$.
- Theorem 18, printed page 210, especially equation (7.14), for the residual inequality.

In repo notation,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

with

$$
|R_H^F(t)|\le \frac1{2H+2}K_H(t),
$$

and

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

The endpoint conversion is correct: Vaaler's centered polynomial has value $0$ at integers, while $\psi_F(n)=-1/2$, and

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

A1's R5-Full mechanism remains the right way to remove the Fejer residual from the active path. With

$$
H\asymp D X^{-1/4},
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

the Fejer estimate gives

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg, choose $m$ nearest to $X/d$ and use

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

The exact-resonance-safe cap is

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min(1,\Delta^2/u^2),&u\ne0.
\end{cases}
$$

Then

$$
\frac1H K_H(X/d)\ll W_\Delta(X-md).
$$

Grouping by $n=md$ gives divisor multiplicity at most $\tau(n)$, hence

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)W_\Delta(X-n)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the shifted residual legs,

$$
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\},
$$

near-integrality is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing $\ell=4m-\rho$ again gives a product-counting problem, and the congruence restriction $\ell\equiv-\rho\pmod4$ only reduces divisor multiplicity.

A1's algebra checks should also be promoted:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

and

$$
\Phi(u)+\Phi(1-u)=1.
$$

Thus $\Phi(1-u)=\Phi(u)$ is false in general.

A1's Li--Yang conclusion remains a guardrail: structural similarity to Li--Yang reciprocal sums is not theorem applicability. At the endpoint block, the printed/current audited ranges fall below $H_D\asymp D X^{-1/4}$, so Li--Yang cannot be imported as a black-box proof of M9.

### From A2

A2 provides the main new analytic direction for Round 23.

The first important result is the $\mathcal M_2$ Cauchy--Schwarz diagnosis. Write

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}\alpha_{h,H_D}C_hB_h(D;X),
$$

where

$$
C_h=e(h/4)-e(3h/4),
$$

and

$$
B_h(D;X)=\sum_{d\asymp D}w_D(d)e(hX/(4d)).
$$

For odd $h$,

$$
C_h=2i\chi_4(h),
$$

and for even $h$,

$$
C_h=0.
$$

A2 proves two bounded-scope diagnostics:

1. The unweighted $h$-Cauchy normalization gives a diagonal contribution

$$
D H_D\asymp D^2X^{-1/4}.
$$

At $D\asymp X^{1/2}$ this is $X^{3/4}$, which exceeds the squared target $X^{1/2+\epsilon}$.

2. The $|\alpha_h|$-weighted $h$-Cauchy normalization fixes the diagonal:

$$
D\log^2 H_D\ll_\epsilon X^{1/2+\epsilon},
$$

but it replaces $C_h$ by $|C_h|^2$, losing the sign of $\chi_4(h)$ and retaining only odd-frequency support. This is a proved diagnostic for that normalization, not a global no-go theorem.

The second useful contribution is A2's fourth-moment candidate. If

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}\alpha_{h,H_D}C_hB_h(D;X),
$$

then a fourth-moment target of the form

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}
$$

would imply

$$
\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

up to the fixed scalar $4^4$ if one defines the fourth moment for $S_2$ rather than $\mathcal M_2$ itself.

The exact expansion uses variables $h_1,h_2,h_3,h_4$ and $d_1,d_2,d_3,d_4$, with phase

$$
\frac{X}{4}
\left(
\frac{h_1}{d_1}
-\frac{h_2}{d_2}
+\frac{h_3}{d_3}
-\frac{h_4}{d_4}
\right).
$$

The character factor

$$
C_{h_1}\overline{C_{h_2}}C_{h_3}\overline{C_{h_4}}
$$

preserves $\chi_4(h_i)$ signs before absolute-value majorization. A2 gives provisional estimates for the displayed pair-swapped, semi-diagonal, and denominator-paired families. These estimates are not yet a proof: the exact-resonance taxonomy is incomplete and near-collisions remain the central issue.

The third useful contribution is the CRI statistic. Define

$$
\Sigma_r
=
\sum_{\substack{1\le h\le H_D\\h\equiv r\pmod4}}
\alpha_{h,H_D}
\sum_d w_D(d)e(hX/(4d)),
\qquad r\in\{1,3\}.
$$

The relevant falsification metric is

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}{|\Sigma_1|^2+|\Sigma_3|^2}.
$$

Values near $1$ indicate little useful residue-class interference; values substantially below $1$ justify further proof work. CRI is not yet a sufficient theorem.

### From A3

A3's main value is formula auditing and verification discipline.

A3 verifies, or at least independently checks in small symbolic models, the following items:

- H4 source anchors and the integer-jump convention.
- R5-Full's exact-resonance handling.
- Raw-vs-paired M9 equivalence for real weights.
- Q1-Spectral consistency.
- M2 weighted $h$-Cauchy sign loss.
- M2 $d$-Cauchy diagonal scaling.
- Li--Yang endpoint mismatch.
- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- $\Phi(1-u)=\Phi(u)$ is false.

The paired real formulas for implementation are:

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{h=1}^{H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}
\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_d w_D(d)e(hX/(4d)).
$$

These formulas require real dyadic weights. They are implementation formulas, not estimates.

A3's weak point is that too much of the output remains protocol-level or tiny-example verification. Also, A3's statement that A2 had not supplied exact fourth-moment formulas is stale in the reviewed Round 23 bundle. In Round 24, A3 should use A2's displayed fourth-moment formula and produce reproducible tables rather than more protocols.

### From Stage B reviews

A1's review correctly identifies A2 as the strongest new analytic contributor and A3 as useful but under-executed. It scores A2 at 8.0 and A3 at 7.0, with A2 needing a complete exact-resonance taxonomy for $\mathcal Q_4$ and A3 needing high-precision tables rather than hand examples.

A2's review of A1/A3 correctly validates A1's proof-draft consolidation, A3's $\Phi$ asymmetry check, and the need to keep the bridge conditional. It also flags endpoint/singularity gaps in A2-type denominator-paired estimates and the need for exact two-sided $h$ conventions.

A3's review correctly states that A1's proof infrastructure and A2's $\mathcal M_2$ finite statistics complement each other. It recommends that A2 expand $\mathcal Q_4$ and that A3 execute high-precision R5, raw-vs-paired M9, Q1, and Li--Yang checks.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** Round 23 proves no endpoint estimate for M9 and therefore proves no bound

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

2. **Reject treating M9 as proved.** The bridge remains conditional:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

3. **Reject arbitrary-coefficient main-sum stress tests as active dependencies.** The Vaaler reduction uses fixed coefficients $\alpha_{h,H_D}$. Arbitrary $u_h$ or $L^1$ variants are useful stress tests only.

4. **Reject scalar Vaaler residuals.** The residual is controlled by H4 plus R5-Full product counting. Dropping the Fejer kernel modes would be a false proof.

5. **Reject $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$.** The correct relation is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

6. **Reject $\Phi(1-u)=\Phi(u)$.** The correct identity is

$$
\Phi(u)+\Phi(1-u)=1.
$$

7. **Reject unweighted $h$-Cauchy for $\mathcal M_2$ as viable at the endpoint.** Its diagonal gives $D^2X^{-1/4}$, equal to $X^{3/4}$ at $D\asymp X^{1/2}$.

8. **Reject weighted $h$-Cauchy for $\mathcal M_2$ as character-preserving.** Its diagonal is acceptable, but it replaces $C_h$ by $|C_h|^2$ and loses the $\chi_4(h)$ sign.

9. **Reject CRI as a sufficient target by itself.** The relevant quantity is

$$
|\Sigma_1-\Sigma_3|^2
=
|\Sigma_1|^2+|\Sigma_3|^2
-
2\operatorname{Re}(\Sigma_1\overline{\Sigma_3}),
$$

not merely the cross term.

10. **Reject the fourth-moment route as proved.** A2's finite object is useful, but the exact-resonance taxonomy, denominator-paired singular cases, signed-frequency handling, and near-collision bounds remain incomplete.

11. **Reject the human note's fourth-moment near-collision mass as a theorem.** The claimed $X^{9/4}$ absolute near-collision heuristic ignores coefficient weights, gcd structure, signs, parity, dyadic cutoffs, and nonuniformity of the cleared-denominator map. It should be tested, not accepted.

12. **Reject the human note's pointwise Lindelof comparison as a theorem.** The claimed relation between unaveraged M9 control and Lindelof-strength bounds for $L(1/2+it,\chi_4)$ needs a stationary-phase/Dirichlet-polynomial derivation.

13. **Reject variable-$\theta$ balancing as an endpoint solution.** Setting

$$
H_D=D X^{-\theta}
$$

with $\theta\approx0.314$ changes the success criterion. It may be a proof-of-known-exponent compatibility track, not a proof of the conjectural $\theta=1/4$ endpoint.

14. **Reject H13/Voronoi collapse as proved.** The proposed recombination into a Hardy--Voronoi/Bessel-like sum still needs exact modulo-$4$ Poisson normalization, amplitude, boundary, dyadic, and character-survival checks. The human strategy note explicitly says these details are missing.

15. **Reject Kloosterman-spectral arithmetization as a near-term pivot.** It may be worth one literature map, but it requires a substantial Kuznetsov/level/conductor theorem stack and no current reduction matches M9.

16. **Reject black-box Li--Yang/Bombieri--Iwaniec endpoint import.** The printed/current audited height ranges do not cover $H_D\asymp D X^{-1/4}$ at the top block. The guardrail remains necessary.

17. **Reject small numerical examples as asymptotic evidence.** They are regression and falsification tools only.

## Known gaps

1. **M9 endpoint estimate.** The open analytic problem remains:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

2. **Proof-draft insertion.** H4-R23 and R5-Full-R23 are source-normalized in substance, but the proof draft still needs final rendered-page transcription, small-$X$ threshold language, and dyadic-overlap bookkeeping.

3. **M9a signed statistic.** The BSOS-M9a sufficient target exists, but no estimate proves it:

$$
|\mathcal S_{\rm signed}(D;X)|
\ll_\epsilon X^{1/2+\epsilon}
\Longrightarrow
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

4. **M9b fourth-moment taxonomy.** A2's $\mathcal Q_4$ needs a complete exact-resonance classification, including pair-swapped, semi-diagonal, denominator-paired, mixed denominator, sign-symmetric, and unclassified families.

5. **Denominator-paired singular cases.** The parameterization involving expressions such as $h_1-h_2=ac$ and $h_3-h_4=-bc$ creates potential singular cases when denominators like $|h_1-ac|$ vanish or lie near truncation boundaries. These need to be separated.

6. **Near-collision bands.** Exact resonance $N=0$ is not enough. After clearing denominators,

$$
N
=
h_1d_2d_3d_4-h_2d_1d_3d_4
+h_3d_1d_2d_4-h_4d_1d_2d_3.
$$

At $D\asymp X^{1/2}$, nonoscillatory or weakly oscillatory bands can extend to $|N|\lesssim X$. Signed and absolute masses in these bands should be measured.

7. **CRI implication.** Need a precise theorem-level condition on

$$
\Sigma_1,\Sigma_3,\operatorname{Re}(\Sigma_1\overline{\Sigma_3})
$$

that implies $\mathcal M_2\ll X^{1/4+\epsilon}$.

8. **Two-sided versus one-sided $h$ conventions.** A2's formulas sometimes use $1\le h\le H_D$ and sometimes $1\le |h|\le H_D$. This affects conjugation and constants in the fourth moment and CRI. Freeze one convention before computation.

9. **A3 numerical execution.** A3 should move from tiny examples to reproducible tables for R5, M9 regression, M2 kernels, CRI, and fourth-moment bins.

10. **Li--Yang Case A/B audit.** The unusual Case A condition involving $T^{-7/16}$ should be resolved from the typeset PDF/source. The endpoint non-import conclusion does not depend on this lower branch, but theorem-level citation requires exact transcription.

11. **Variable-$\theta$ track.** Need a separate map showing what exponent would follow if one chooses $H_D=D X^{-\theta}$ and imports a valid Li--Yang-type theorem. This track should be kept separate from the conjectural endpoint program.

12. **H13 endpoint test.** Need exact Poisson modulo $4$, stationary amplitude, boundary and nonstationary regimes, and a signed-versus-operator-norm comparison near $D\asymp X^{1/2}$.

13. **Pointwise Lindelof comparison.** Need an exact derivation or refutation of the human note's claim that pointwise M9 control maps to Lindelof-strength estimates.

14. **Kuznetsov/Kloosterman arithmetization.** Need a literature map only: exact Kuznetsov formula, nebentypus $\chi_4$, level $4$, test function, conductor dependence, and match to M9 ranges. No pivot yet.

## New lemmas to add

### H4-R23. Finite Vaaler approximation with floor-compatible residual

**Status:** external theorem dependency, source-normalized.

For $H\ge1$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}
-\frac{\Phi(|h|/(H+1))}{2\pi i h}e(ht)
+
R_H^F(t),
$$

with

$$
|R_H^F(t)|\le \frac1{2H+2}K_H(t).
$$

At integers,

$$
V_H(n)=0,
\qquad
\psi_F(n)=-\frac12,
\qquad
K_H(0)/(2H+2)=1/2.
$$

Thus the Fejer majorant covers the half-jump.

### Alpha-Conjugacy-R23

**Status:** proved algebraic lemma.

For $1\le h\le H$,

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### Phi-Asymmetry-R23

**Status:** proved algebraic lemma.

For $0<u<1$,

$$
\Phi(u)+\Phi(1-u)=1.
$$

Thus $\Phi(1-u)=\Phi(u)$ is false in general. Endpoint limits are

$$
\Phi(0^+)=1,
\qquad
\Phi(1^-)=0.
$$

### R5-Full-R23

**Status:** proved conditional on H4 and $\tau(n)\ll_\epsilon n^\epsilon$.

For active blocks and $H\asymp D X^{-1/4}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### Bridge-R23

**Status:** conditional theorem.

If H1--H3, H4, R5-Full, and M9 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is not a proof of the conjectural Gauss circle bound because M9 remains open.

### M9-R23

**Status:** open analytic target.

For $X^{1/4}\le D\le X^{1/2}$ and $H_D\asymp D X^{-1/4}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-Pair-R23

**Status:** proved implementation lemma for real weights only.

For real $w_D$,

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}
\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)
\operatorname{Re}
\sum_d w_D(d)e(hX/(4d)).
$$

### M9a-BSOS-R23

**Status:** sufficient finite target, not an estimate.

Under the frozen $|\alpha|$-weighted Cauchy--Schwarz normalization, define

$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right),
$$

on odd denominators, and

$$
\mathcal S_{\rm signed}
=
\sum_{\substack{d_1\ne d_2\\d_i\in\mathcal D_{\rm odd}}}
\chi_4(d_1)\chi_4(d_2)K_{d_1,d_2}^{(|\alpha|)}.
$$

Then

$$
|\mathcal S_{\rm signed}(D;X)|\ll_\epsilon X^{1/2+\epsilon}
\Longrightarrow
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M2-CS-Normalizations-R23

**Status:** proved bounded-scope diagnostic.

For $\mathcal M_2$:

- Unweighted $h$-Cauchy gives diagonal size $D^2X^{-1/4}$, too large at $D\asymp X^{1/2}$.
- $|\alpha_h|$-weighted $h$-Cauchy gives acceptable diagonal $D\log^2 H_D$, but loses the sign of $\chi_4(h)$ through $|C_h|^2$.

This proves character loss for the displayed normalizations only.

### M2-FourthMoment-Target-R23

**Status:** proposed exploratory/falsification target.

Let

$$
S_2(D;X)=
\sum_{1\le |h|\le H_D}\alpha_{h,H_D}C_h
\sum_d w_D(d)e(hX/(4d)).
$$

A sufficient target is

$$
|S_2(D;X)|^4\ll_\epsilon X^{1+\epsilon}.
$$

The exact expansion should retain the character product

$$
C_{h_1}\overline{C_{h_2}}C_{h_3}\overline{C_{h_4}}.
$$

The current diagonal-family analysis is provisional; near-collisions remain open.

### CRI-M2-R23

**Status:** proposed falsification statistic, not a theorem.

For

$$
\Sigma_r
=
\sum_{\substack{1\le h\le H_D\\h\equiv r\pmod4}}
\alpha_{h,H_D}
\sum_d w_D(d)e(hX/(4d)),
\qquad r\in\{1,3\},
$$

define

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}.
$$

Values near $1$ falsify useful CRI cancellation; values significantly below $1$ justify further proof work.

### H13-Endpoint-Falsification-R23

**Status:** secondary exploratory diagnostic.

Near $D\asymp X^{1/2}$, derive the post-Poisson stationary-phase kernel including amplitude and test whether the dual $\chi_4$ survives a non-conjugacy statistic or collapses to diagonal-unitary blindness.

### LY-Theta-Map-R23

**Status:** optional theorem-compatibility map, separate from endpoint goal.

For variable cutoff

$$
H_D=D X^{-\theta},
$$

audit which Li--Yang-type theorem ranges could prove a bound $P(X)\ll X^{\theta+\epsilon}$. This may reproduce known-exponent technology but does not address the endpoint $\theta=1/4$ unless the theorem covers that height.

### Kuznetsov-Map-R23

**Status:** speculative literature-mapping target only.

Identify whether any Kuznetsov formula for $\Gamma_0(4)$ with nebentypus $\chi_4$ can naturally produce the M9 dyadic ranges. No proof route is asserted.

## Counterexample checks to run

1. **H4 source check.** Verify from rendered Vaaler pages the exact coefficient function, coefficient sign, Fejer kernel normalization, residual constant, and integer-jump convention.

2. **H4 integer test.** Test

$$
V_H(n)=0,
\qquad
K_H(0)=H+1,
\qquad
K_H(0)/(2H+2)=1/2.
$$

3. **R5 exact-resonance tests.** Use exact rational/modular handling for $X/d\in\mathbb Z$ and $(X/d+\rho)/4\in\mathbb Z$. Verify the cap $W_\Delta(0)=1$.

4. **R5 residual tables.** For $X=10^6,10^8$ and $D\asymp X^{1/4},X^{3/8},X^{1/2}$, compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

and the shifted analogues for $\rho=1,3$. Include square, nonsquare, near-square, and divisor-rich $X$.

5. **Raw-vs-paired M9 regression.** For real weights, compute $\mathcal M_1,\mathcal M_2$ from both raw two-sided definitions and paired formulas. Differences should be roundoff only.

6. **M9 fixed-versus-stress comparison.** Compare fixed Vaaler coefficients with arbitrary phase coefficients and $L^1$ stress norms. This is diagnostic only.

7. **M9a BSOS test.** Compute $\mathcal S_{\rm signed}$, unsigned comparator, absolute majorant, and operator-norm comparator for the exact $|\alpha|$-weighted kernel.

8. **M2 Cauchy kernels.** For $D\asymp X^{1/4},X^{3/8},X^{1/2}$, compute the weighted and unweighted $h$-Cauchy kernels, diagonal mass, off-diagonal mass, operator norm, and absolute majorant.

9. **M2 $d$-Cauchy diagonal.** Verify the $D^2$ diagonal scaling at large $D$.

10. **CRI endpoint test.** Compute

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}
$$

on endpoint blocks. Values near $1$ should deprioritize CRI.

11. **Fourth-moment exact bins.** Enumerate

$$
N
=
h_1d_2d_3d_4-h_2d_1d_3d_4
+h_3d_1d_2d_4-h_4d_1d_2d_3.
$$

Split $N=0$ into pair-swapped, semi-diagonal, denominator-paired, mixed, and unclassified bins. Report signed and absolute masses.

12. **Fourth-moment near-collision bands.** Bin $|N|\sim T$ up to at least $T\lesssim X$ at endpoint scale. Test the human note's $X^{9/4}$ absolute near-collision heuristic, but include coefficient weights, gcd structure, parity, dyadic cutoffs, and signs.

13. **Denominator-paired singular cases.** Test cases where $h_1=ac$, $h_3=-bc$, or corresponding values lie near truncation endpoints.

14. **Li--Yang audit.** Resolve Case A/B statements from the typeset PDF and record exact theorem hypotheses for $F,g,G,H,M,T$, weights, and absolute-value placement.

15. **Variable-$\theta$ map.** For $H_D=D X^{-\theta}$, compute the residual size $X^\theta$, the M9 height range, and exact Li--Yang compatibility. Keep endpoint and known-exponent tracks separate.

16. **Pointwise Lindelof comparison.** Derive or refute the map from pointwise M9 estimates to a Dirichlet-polynomial or $L(1/2+it,\chi_4)$ object.

17. **H13 endpoint test.** Near $D\asymp X^{1/2}$, derive one post-transform kernel with stationary amplitude and compare signed dual statistic, unsigned statistic, and diagonal-unitary operator norm.

18. **Kuznetsov map check.** Identify the exact $\Gamma_0(4)$, nebentypus, test function, spectral large sieve, and conductor dependencies that would be needed for the Kloosterman-spectral idea. Do not attempt a proof without this map.

## Research strategy adjustment

Keep the balanced hyperbola/Vaaler route as the main line. The state is now:

$$
\text{residual side controlled conditionally by H4+R5-Full;}
\qquad
\text{M9 is the active analytic bottleneck for the endpoint program.}
$$

Round 24 should be a finite-statistics verification round centered on $\mathcal M_2$, while preserving the proof-draft infrastructure.

The human strategy revision is useful as hypothesis generation, not as proved mathematics. Its influence on Round 24 should be:

1. **Fourth moment:** Test the near-collision heuristic directly. Do not accept fourth-moment impossibility or success without exact bins and signed/absolute data.
2. **CRI:** Treat CRI as a falsification statistic until the ratio $R_{\rm CRI}$ shows useful cancellation and a theorem-level implication is written.
3. **Variable $\theta$:** Give A1 a small side task to map Li--Yang compatibility for $H_D=D X^{-\theta}$, but keep it separate from the endpoint program.
4. **H13/Voronoi:** Run one endpoint test with amplitude. Do not promote H13 until exact stationary phase and character-survival are verified.
5. **Kloosterman/Kuznetsov:** Keep as a narrow literature map only. It should not displace finite-statistic M9 work.

The practical next-round division is:

- A1: proof-draft and lemma-bank consolidation plus a small variable-$\theta$/Lindelof/Kuznetsov mapping appendix.
- A2: exact $\mathcal M_2$ fourth-moment/CRI taxonomy and falsification criteria.
- A3: high-precision and exact-modular computations using A2's formulas.

## Next-round prompts by agent

### For A1

Produce the Round 24 proof-draft consolidation and small literature/parameter appendix.

Objectives:

1. Insert H4-R23 into the proof draft with exact Vaaler source anchors:
   - Theorem 6, printed page 192, equation (2.28), for $\widehat J$.
   - Section 7, printed page 207, equations (7.1)--(7.3), for $i_N,j_N,k_N$.
   - Theorem 18, printed page 210, especially equation (7.14), for the residual inequality.

2. Insert the floor-compatible endpoint conversion:

$$
V_H(n)=0,
\qquad
\psi_F(n)=-\frac12,
\qquad
K_H(0)/(2H+2)=1/2.
$$

3. Insert Alpha-Conjugacy-R23 and Phi-Asymmetry-R23:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

and

$$
\Phi(u)+\Phi(1-u)=1.
$$

4. Insert R5-Full-R23 with all edge cases:
   - nearest-integer tie convention;
   - exact resonance $W_\Delta(0)=1$;
   - shifted-leg product $X\approx d(4m-\rho)$;
   - positivity of $\ell=4m-\rho$ in the large active range;
   - small-$X$ separation;
   - short blocks $D<X^{1/4}$;
   - dyadic bounded overlap.

5. State Bridge-R23 only conditionally:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Explicitly state that M9 is open.

6. Insert M9-R23 and M9-Pair-R23 as implementation formulas for real weights only. Include a raw-vs-paired regression warning.

7. Insert M2-CS-Normalizations-R23 as a bounded-scope diagnostic, not a global obstruction.

8. Add M2-FourthMoment-Target-R23 and CRI-M2-R23 as proposed/falsification targets only.

9. Add a short variable-$\theta$ appendix. For

$$
H_D=D X^{-\theta},
$$

derive the residual size $D/H_D=X^\theta$, map Li--Yang's final height range $H\le D X^{-\theta^*}$, and state exactly which exponent would follow if M9-type bounds were imported. Keep this separate from the endpoint $\theta=1/4$ program.

10. Add a short Lindelof-comparison note. Derive or refute the human note's claim that pointwise M9 control maps to $L(1/2+it,\chi_4)$ with $t\asymp hX/D$. Include coefficients, lengths, smoothing, and losses.

11. Add a one-page Kloosterman/Kuznetsov map. Identify the exact Kuznetsov formula, level, nebentypus, test function, conductor, and whether it naturally matches M9 dyadic ranges. Mark it speculative unless a precise theorem applies.

12. Keep H13 as one endpoint falsification test only.

### For A2

Focus on $\mathcal M_2$ finite statistics. Produce a proof-draft-ready fourth-moment and CRI packet.

Objectives:

1. Freeze one $h$ convention: either one-sided positive $h$ using paired real formulas or two-sided $1\le |h|\le H_D$. State how constants and conjugations change.

2. Define

$$
S_2(D;X)
=
\sum_{h}\alpha_{h,H_D}C_h
\sum_d w_D(d)e(hX/(4d)),
$$

and define the fourth moment as

$$
\mathcal Q_4(D;X)=|S_2(D;X)|^4.
$$

If instead using $\mathcal M_2=4S_2$, explicitly include the scalar factor $4^4=256$.

3. Write the full expansion with actual coefficients $\alpha_{h,H_D}$, actual $C_h$, dyadic weights, and the exact phase.

4. Write the cleared denominator integer

$$
N
=
h_1d_2d_3d_4-h_2d_1d_3d_4
+h_3d_1d_2d_4-h_4d_1d_2d_3.
$$

5. Classify exact $N=0$ families:
   - pair-swapped;
   - semi-diagonal;
   - denominator-paired;
   - mixed denominator patterns;
   - sign-symmetric variants;
   - unclassified residue.

6. Repair denominator-paired endpoint/singularity cases. Explicitly separate cases such as $h_1=ac$, $h_3=-bc$, and values near the truncation boundary.

7. State proved or assumed bounds for each family. Use only the statuses `[PROVED]`, `[DERIVED-UNDER-ASSUMPTIONS]`, `[HEURISTIC]`, `[CONJECTURED]`, `[ASSUMED]`, or `[LIKELY-FALSE]`.

8. Define near-collision bands $|N|\sim T$ and state the exact bound needed over these bands to imply

$$
\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

9. Evaluate the human note's $X^{9/4}$ absolute near-collision heuristic. State what it ignores and what A3 should measure.

10. Define CRI precisely:

$$
\Sigma_r
=
\sum_{\substack{h\\h\equiv r\pmod4}}
\alpha_{h,H_D}
\sum_d w_D(d)e(hX/(4d)),
\qquad r\in\{1,3\}.
$$

Give the exact identity relating $\mathcal M_2$ to $\Sigma_1-\Sigma_3$ under your convention.

11. State a theorem-level CRI sufficient condition, or label CRI only as a falsification metric. The target should involve the whole expression

$$
|\Sigma_1|^2+|\Sigma_3|^2
-
2\operatorname{Re}(\Sigma_1\overline{\Sigma_3}).
$$

12. Supply A3-ready formulas for:
   - weighted and unweighted M2 Cauchy kernels;
   - CRI ratio;
   - fourth-moment exact bins;
   - near-collision banding;
   - denominator-paired singular checks.

13. Keep H13 and variable-$\theta$ discussion secondary. Do not claim that fourth moment or CRI proves M9.

### For A3

Execute computations and source checks. Do not write another protocol-only response.

Objectives:

1. **H4 source verification.** Use the rendered Vaaler PDF. Confirm Theorem 6/equation (2.28), Section 7/equations (7.1)--(7.3), and Theorem 18/equation (7.14), including coefficient sign and residual constant.

2. **H4 integer check.** For several $H$, verify

$$
V_H(n)=0,
\qquad
K_H(0)/(2H+2)=1/2.
$$

3. **R5 tables.** Compute first-leg and shifted residuals for $X=10^6$ and $X=10^8$ with

$$
D\asymp X^{1/4},\quad X^{3/8},\quad X^{1/2}.
$$

Use square, nonsquare, near-square, and divisor-rich $X$. Use exact modular/rational detection for Fejer spikes.

4. **Raw-vs-paired M9 regression.** For real weights, compute raw two-sided $\mathcal M_1,\mathcal M_2$ and paired formulas. Report absolute and relative errors.

5. **Fixed-versus-stress M9.** Compare actual Vaaler coefficients with arbitrary phase coefficients and $L^1$ stress norms.

6. **M9a BSOS matrix.** Build the exact $|\alpha|$-weighted kernel. Report:
   - $\mathcal S_{\rm signed}$;
   - unsigned comparator;
   - absolute majorant;
   - operator-norm comparator;
   - ratios.

7. **M2 Cauchy kernels.** Compute weighted and unweighted $h$-Cauchy kernels for $\mathcal M_2$. Report diagonal mass, off-diagonal mass, absolute majorant, and operator norm for $D\asymp X^{1/4},X^{3/8},X^{1/2}$.

8. **M2 $d$-Cauchy diagonal.** Verify the $D^2$ diagonal scaling.

9. **CRI ratio.** Using A2's convention, compute

$$
R_{\rm CRI}
=
\frac{|\Sigma_1-\Sigma_3|^2}
{|\Sigma_1|^2+|\Sigma_3|^2}.
$$

Run endpoint blocks and record whether the ratio is near $1$ or significantly below $1$.

10. **Fourth-moment exact bins.** Use A2's formula. Enumerate $N=0$ and split into pair-swapped, semi-diagonal, denominator-paired, mixed, and unclassified bins. Report signed and absolute masses.

11. **Near-collision bands.** For small-to-moderate $X$, bin $|N|\sim T$ up to the nonoscillatory scale. Report signed and absolute mass by bin.

12. **Denominator-paired singular checks.** Test cases flagged by A2, especially $h_1=ac$ and $h_3=-bc$.

13. **Li--Yang source/PDF audit.** Resolve the Case A/B ambiguity from the typeset PDF and record exact theorem hypotheses for $F,g,G,H,M,T$ and absolute-value placement. Preserve the endpoint non-import conclusion unless a precise theorem covers $H_D\asymp D X^{-1/4}$.

14. **H13 endpoint test.** Run exactly one endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes. Compare signed dual statistic, unsigned statistic, and diagonal-unitary operator-norm comparator. Do not promote H13 from the result alone.

15. Preserve raw tables and scripts, including precision settings and exact-resonance detection rules.

## Confidence

High confidence:

- The balanced hyperbola/Vaaler framework remains the correct reduction framework.
- H1--H3 remain accepted arithmetic reductions.
- H4-R23 is correct in substance and now source-normalized.
- The floor-compatible endpoint is covered by the Fejer majorant.
- R5-Full-R23 controls the fixed Fejer residual conditional on H4.
- Bridge-R23 is a valid conditional reduction.
- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- $\Phi(1-u)=\Phi(u)$ is false, and $\Phi(u)+\Phi(1-u)=1$.
- M9 remains open and is the active analytic bottleneck.
- A2's M2 Cauchy diagnostics are correct for the displayed normalizations.
- Black-box Li--Yang endpoint import is not justified.
- No Round 23 output proves a new Gauss circle exponent.

Moderate confidence:

- The paired M9 formulas are correct for real weights and suitable for implementation regression.
- BSOS-M9a is a useful finite signed statistic for $\mathcal M_1$.
- A2's fourth-moment and CRI objects are useful falsification/proof-search targets for $\mathcal M_2$.
- The displayed exact diagonal fourth-moment families may be controllable at $X^{1+\epsilon}$ after endpoint repair.
- H13 is worth one endpoint-focused falsification test.
- A variable-$\theta$ Li--Yang map may be useful as a separate known-exponent compatibility track.

Low confidence:

- BSOS-M9a is asymptotically small enough to prove $\mathcal M_1$.
- CRI or the fourth-moment statistic will prove $\mathcal M_2$ without a new signed spacing theorem.
- H13 avoids character erasure after the first serious norm extraction.
- The pointwise Lindelof comparison is a theorem rather than a heuristic.
- Kuznetsov/Kloosterman arithmetization matches M9 without major new machinery.
- Current published Bombieri--Iwaniec/Li--Yang technology proves M9 at endpoint height.
- Any route in the current repository proves a new exponent.
