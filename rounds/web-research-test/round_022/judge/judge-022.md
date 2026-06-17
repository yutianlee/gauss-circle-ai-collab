## Selected main route

Source basis: uploaded Round 22 packet `judge_22.md`, including A1/A2/A3 Stage A outputs and Stage B reviews.

Keep the balanced arithmetic hyperbola/Vaaler framework as the selected route:

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

The current conservative bridge remains:

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

This is a conditional reduction, not a proof of the conjectural Gauss circle bound. Round 22 proves no new exponent. The residual side remains provisionally controlled by `H4 + R5-Full`, conditional on final source-level normalization of Vaaler's theorem and proof-draft edge-case bookkeeping. The active analytic bottleneck remains `M9`: the fixed-Vaaler-coefficient reciprocal main sums.

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

Freeze `M9` with the actual Vaaler coefficients only:

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

The official main terms are

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

The open endpoint target is

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for all active dyadic $D$.

## Useful fragments by source

### From A1

A1 supplied the strongest proof-draft consolidation. The useful core is the conditional bridge

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

with `M9` explicitly left open.

A1's `H4-R22` is the current proof-draft Vaaler statement. With

$$
e(t)=e^{2\pi i t},
$$

the finite approximation is

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

with

$$
|R_H^F(t)|
\le
\frac1{2H+2}K_H(t),
$$

and

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin\pi(H+1)t}{\sin\pi t}\right)^2.
$$

The source anchors are Vaaler Theorem 6, equation (2.28), for the coefficient function, Section 7 equations (7.1)--(7.3) for $i_N,j_N,k_N$, and Theorem 18, especially equation (7.14), for the residual inequality. The final repo proof should still verify the printed page/equation labels against the rendered PDF.

A1 correctly handles the floor-compatible endpoint convention. Vaaler's centered sawtooth has value $0$ at integers, while the arithmetic sawtooth has $\psi_F(n)=-1/2$. The Vaaler polynomial has $V_H(n)=0$, and

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12,
$$

so the Fejer majorant covers the half-jump exactly.

A1's `R5-Full-R22` is the official residual mechanism. With

$$
H\asymp D X^{-1/4},
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

the Fejer bound

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right)
$$

gives

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg, choose $m$ nearest to $X/d$. Since $d\asymp D$,

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

Using

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min\left(1,\Delta^2/u^2\right),&u\ne0,
\end{cases}
$$

one obtains

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

For the shifted residual legs, near-integrality of

$$
\frac{X/d+\rho}{4},
\qquad \rho\in\{1,3\},
$$

is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing $\ell=4m-\rho$ gives $n=d\ell$ with $\ell\equiv-\rho\pmod4$, and the congruence restriction only reduces multiplicity. Under the displayed product-count reduction, this gives the same $X^{1/4+\epsilon}$ bound for the shifted residuals.

A1 also supplies the cleanest signed bilinear target for $\mathcal M_1$. Under the frozen $|\alpha|$-weighted Cauchy--Schwarz normalization, define on odd denominators

$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right),
$$

and

$$
\mathcal S_{\rm signed}(D;X)
=
\sum_{\substack{d_1,d_2\in\mathcal D_{\rm odd}\\d_1\ne d_2}}
\chi_4(d_1)\chi_4(d_2)
K_{d_1,d_2}^{(|\alpha|)}.
$$

Then

$$
|\mathcal S_{\rm signed}(D;X)|\ll_\epsilon X^{1/2+\epsilon}
\Longrightarrow
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is a useful finite target, not an estimate.

### From A2

A2's strongest contribution is the exact separation of $\mathcal M_2$ Cauchy--Schwarz normalizations.

Let

$$
C_h=e(h/4)-e(3h/4).
$$

Then

$$
C_h=
\begin{cases}
2i\chi_4(h),&2\nmid h,\\
0,&2\mid h,
\end{cases}
\qquad
|C_h|^2=
\begin{cases}
4,&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

In the weighted $|\alpha_h|$ normalization,

$$
|\mathcal M_2(D;X)|^2
\le
16L
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|\,|C_h|^2\,|B_h(D;X)|^2,
$$

where

$$
L=\sum_{1\le |h|\le H_D}|\alpha_{h,H_D}|\asymp \log H_D.
$$

After expansion, the kernel is

$$
K_{2;d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|\,|C_h|^2
e\left(\frac{hX}{4}\left(\frac1{d_1}-\frac1{d_2}\right)\right).
$$

The diagonal is acceptable, but the sign of $\chi_4(h)$ has been lost; only odd-frequency support remains. This is a bounded-scope obstruction to the standard second-moment route, not a global no-go theorem for $\mathcal M_2$.

A2's unweighted $h$-Cauchy normalization is a useful stress test. It has scalar factor $H_D$ and diagonal size $D H_D\asymp D^2X^{-1/4}$, which reaches $X^{3/4}$ at $D\asymp X^{1/2}$ and exceeds the squared endpoint target $X^{1/2+\epsilon}$.

A2 also records that Cauchy--Schwarz over the spatial variable $d$ preserves the $h$-character longer, but its diagonal size is $\asymp D^2$, hence $\asymp X$ at the top dyadic range. Such a route needs substantial off-diagonal cancellation and is not presently a proof.

A2's fourth-moment/open-path statistic for $\mathcal M_2$ is the main exploratory object. With

$$
S_h(D;X)=\sum_d w_D(d)e(hX/(4d)),
$$

and $\beta_h=\alpha_hC_h$, the exact fourth moment expands the signs through products of $\chi_4(h_i)$. The endpoint target is

$$
|\mathcal Q_4(D;X)|\ll_\epsilon X^{1+\epsilon},
$$

which would imply $\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}$ by fourth-root extraction. However, the diagonal, semi-diagonal, and near-collision configurations are not yet classified. The fourth-moment route remains proposed and computationally testable, not proved.

A2's CRI statistic for $\mathcal M_2$ remains useful only as a falsification or structure-detection metric. If

$$
\mathcal M_2=8i(\Sigma_1-\Sigma_3),
$$

then

$$
|\mathcal M_2|^2
=
64\left(|\Sigma_1|^2+|\Sigma_3|^2-2\Re(\Sigma_1\overline{\Sigma_3})\right).
$$

Therefore a bound for $\Sigma_1\overline{\Sigma_3}$ alone is not enough. CRI should be compared with $|\Sigma_1|^2+|\Sigma_3|^2$ and needs favorable sign information to become proof-relevant.

### From A3

A3's most valuable contribution is formula auditing.

A3 verifies the coefficient conjugacy

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

and rejects the algebra error

$$
\alpha_{-h,H}=-\overline{\alpha_{h,H}}.
$$

A3 also confirms that the symmetry

$$
\Phi(1-u)=\Phi(u)
$$

is false. For example,

$$
\Phi(1/3)=\frac{2\pi}{9\sqrt3}+\frac13,
\qquad
\Phi(2/3)=-\frac{2\pi}{9\sqrt3}+\frac23,
$$

so $\Phi(1/3)\ne\Phi(2/3)$. Future code should not fold coefficients using a false $u\mapsto 1-u$ symmetry.

A3 gives the paired implementation formulas for real weights:

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}A_h(D;X),
$$

where

$$
A_h(D;X)=\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\operatorname{Re}B_h(D;X),
$$

where

$$
B_h(D;X)=\sum_d w_D(d)e(hX/(4d)).
$$

These are implementation lemmas only. They should be regressed numerically against the raw two-sided complex sums before being used for experiments.

A3 also supplies the correct high-precision computational protocol for Fejer kernels: detect exact resonances first, set $K_H(t)=H+1$ at integral $t$, and otherwise use high precision for the sine-quotient expression. This is required because ordinary floating-point evaluation near Fejer spikes is unstable.

A3's Li--Yang audit is valuable but incomplete. It identifies a possible TeX/PDF ambiguity involving a Case A exponent such as $T^{-7/16}$ versus $T^{7/16}$ and confirms that black-box endpoint import remains unjustified. The ambiguity should be resolved from the typeset PDF before any theorem-level claim is made.

One correction to A3: the statement that $\Phi(0)=\Phi(1)=1$ by continuous extension is not correct at the right endpoint. For this $\Phi$,

$$
\Phi(0^+)=1,
\qquad
\Phi(1^-)=0.
$$

This does not affect Vaaler coefficients, since $1\le h\le H$ gives $h/(H+1)<1$, but implementation notes should be corrected.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** Round 22 gives proof infrastructure and diagnostics only.

2. **Reject treating `M9` as proved.** The bridge theorem remains conditional because no bound for $\mathcal M_1$ or $\mathcal M_2$ has been proved.

3. **Reject arbitrary-coefficient main-sum stress tests as active dependencies.** The actual Vaaler reduction uses fixed coefficients $\alpha_{h,H_D}$. Arbitrary-coefficient and $L^1$ variants are stress tests only.

4. **Reject scalar Vaaler residuals.** The Fejer residual should be controlled through H4 and R5-Full, including exact resonance and shifted-leg cases.

5. **Reject $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$.** The correct relation is $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.

6. **Reject $\Phi(1-u)=\Phi(u)$.** This symmetry is false. Only the $h\leftrightarrow -h$ conjugacy is valid.

7. **Reject standard $h$-Cauchy for $\mathcal M_2$ as character-preserving.** It replaces $C_h$ by $|C_h|^2$ and loses the sign of $\chi_4(h)$.

8. **Reject Cauchy over $d$ for $\mathcal M_2$ as sufficient without off-diagonal cancellation.** Its diagonal is too large at $D\asymp X^{1/2}$.

9. **Reject CRI as a sufficient target by itself.** It should be paired with estimates for $|\Sigma_1|^2+|\Sigma_3|^2$ and favorable sign information.

10. **Reject the fourth-moment route as proved.** The finite object is valid, but the diagonal, semi-diagonal, and near-collision taxonomy is incomplete.

11. **Reject H13 as a proof route at current precision.** The leading dual phase and support count are not enough. H13 still needs uniform stationary phase, amplitudes, boundary analysis, and a check that the dual character survives more than diagonal unitary conjugation.

12. **Reject black-box Li--Yang import at endpoint height.** Structural similarity to reciprocal sums is not theorem applicability.

13. **Reject using small numerical checks as asymptotic evidence.** They are regression and falsification tools only.

## Known gaps

1. **M9 endpoint estimate.** The active open problem is still

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

2. **Final H4 source transcription.** H4 is source-normalized in substance, but the proof draft should verify rendered page/equation labels for Vaaler Theorem 6, Section 7 definitions, and Theorem 18.

3. **H3 dependency.** Round 22 assumes the earlier balanced sawtooth identity. It does not re-audit H1--H3.

4. **R5 shifted-leg positivity and small-$X$ handling.** The proof is sound for large active ranges; the final proof draft should explicitly show $\ell=4m-\rho>0$ in the active range and separate bounded $X$.

5. **M2 fourth-moment classification.** Need a complete classification of diagonal, semi-diagonal, and near-collision configurations after clearing denominators.

6. **M2 CRI implication.** Need a precise statement of what bounds on $\Sigma_1$, $\Sigma_3$, and $\Re(\Sigma_1\overline{\Sigma_3})$ would imply $\mathcal M_2\ll X^{1/4+\epsilon}$.

7. **H13 uniform stationary phase.** Need exact amplitude, active sign, support restrictions, boundary stationary regimes, nonstationary tails, and short-dual-length treatment.

8. **Li--Yang theorem audit.** Need a line-by-line comparison of the TeX and typeset PDF for Case A/B ranges, the final $S/H$ target, allowed weights, allowed $F$, and endpoint height. The Case A exponent ambiguity should be resolved.

9. **A3 computation gap.** Round 22 still contains mostly protocols. R5 tables, raw-vs-paired regressions, BSOS ratios, M2 kernel tests, and H13 endpoint tests should be executed.

10. **Real-weight assumption in paired formulas.** The paired formulas for $\mathcal M_1,\mathcal M_2$ require real $w_D$. If complex weights are introduced, return to the raw two-sided definitions.

## New lemmas to add

### H4-R22. Finite Vaaler approximation with floor-compatible residual

Status: external theorem dependency, source-normalized in substance.

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

At integers, the Fejer majorant covers the half-jump because $K_H(0)/(2H+2)=1/2$.

### Alpha-Conjugacy-R22

Status: proved algebraic lemma.

For $1\le h\le H$,

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### Phi-Asymmetry-R22

Status: proved algebraic lemma.

The identity $\Phi(1-u)=\Phi(u)$ is false in general. In particular,

$$
\Phi(1/3)\ne\Phi(2/3).
$$

Also record the endpoint correction

$$
\Phi(0^+)=1,
\qquad
\Phi(1^-)=0.
$$

### R5-Full-R22. Fejer residual product-count bound

Status: proved conditional on H4 and standard divisor bounds.

For $X^{1/4}\le D\le X^{1/2}$ and $H\asymp D X^{-1/4}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### Bridge-R22

Status: conditional theorem.

Assume H1--H3, H4-R22, R5-Full-R22, and M9-R22. Then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-R22

Status: open analytic target.

For all active dyadic $D$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-Pair-R22

Status: implementation lemma for real weights.

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

### M9b-ShiftedF-R22

Status: theorem-extension target.

Use

$$
e(hX/(4d))(e(h/4)-e(3h/4))
=
e\left(h\left(\frac{X}{4d}+\frac14\right)\right)
-
e\left(h\left(\frac{X}{4d}+\frac34\right)\right),
$$

and after $d=Dz$ define

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad \rho\in\{1,3\}.
$$

Then

$$
F'F'''-3(F'')^2=-\frac3{8z^6}.
$$

The open question is theorem applicability at endpoint height with actual Vaaler weights and the parameter-dependent additive shift.

### M2-CS-Character-Blindness-R22

Status: proved diagnostic under standard $h$-Cauchy.

Weighted Cauchy--Schwarz over $h$ for $\mathcal M_2$ replaces $C_h$ by $|C_h|^2$, losing the sign of $\chi_4(h)$ and leaving only odd-frequency support.

### CS-d-Diagonal-Obstruction-R22

Status: proved diagonal-size diagnostic under the displayed normalization.

Cauchy--Schwarz over $d$ for $\mathcal M_2$ gives diagonal size $\asymp D^2$, which is too large at $D\asymp X^{1/2}$ unless substantial off-diagonal cancellation is exploited.

### BSOS-M9a-R22

Status: derived sufficient finite target, not an estimate.

For the frozen $|\alpha|$-weighted kernel,

$$
|\mathcal S_{\rm signed}(D;X)|
\ll_\epsilon X^{1/2+\epsilon}
\Longrightarrow
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M2-FourthMoment-OpenPath-R22

Status: proposed exploratory statistic.

The exact fourth moment of $\mathcal M_2$ retains the $C_h$ signs. Its endpoint target is

$$
|\mathcal Q_4(D;X)|\ll_\epsilon X^{1+\epsilon}.
$$

The proof draft should use the correct fourth-power scalar factor $4^4=256$ when constants are displayed, although constants do not affect exponent-level diagnostics.

### CRI-M2-R22

Status: falsification statistic, not a sufficient target.

The CRI statistic should be interpreted relative to $|\Sigma_1|^2+|\Sigma_3|^2$ and the sign of $\Re(\Sigma_1\overline{\Sigma_3})$.

### H13-Dual-Q1-Collapse-R22

Status: derived-under-assumptions diagnostic.

If H13 is followed by a matrix argument in which $\chi_4(m)$ enters only through diagonal unitary conjugation, then operator-norm, Frobenius, Schur/Gershgorin, absolute-value matrix, and cyclic-trace methods erase the character.

## Counterexample checks to run

1. **H4 source check.** Read the rendered Vaaler PDF at Theorem 6, Section 7 definitions, and Theorem 18. Confirm coefficient sign, residual constant, Fejer kernel normalization, and integer-jump convention.

2. **Exact resonance check.** Test cases with $X/d\in\mathbb Z$ and $(X/d+\rho)/4\in\mathbb Z$. Confirm $K_H(t)=H+1$ and $H^{-1}K_H(t)\ll W_\Delta(0)$.

3. **R5 residual tables.** Compute first-leg and shifted-leg residuals for $X=10^6,10^8$, with $D\asymp X^{1/4},X^{3/8},X^{1/2}$, using square, nonsquare, near-square, and divisor-rich $X$.

4. **Phi table regression.** Confirm exact values at $u=1/4,1/3,1/2,2/3,3/4$ and the endpoint limits $\Phi(0^+)=1$, $\Phi(1^-)=0$.

5. **Alpha conjugacy regression.** Verify code uses $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.

6. **Raw-vs-paired M9 regression.** For real weights, compare raw two-sided complex sums with paired formulas for $\mathcal M_1$ and $\mathcal M_2$. Differences should be numerical roundoff.

7. **M2 sign-loss test.** Compute the original $C_h$-weighted sum and the weighted $h$-Cauchy kernel. Verify that the kernel contains $|C_h|^2$ and only odd-frequency support.

8. **M2 d-Cauchy diagonal check.** Compute the $d$-Cauchy diagonal and confirm its $D^2$ scaling at large $D$.

9. **BSOS-M9a test.** Compute $\mathcal S_{\rm signed}$, unsigned comparator, absolute majorant, and operator-norm comparator for the exact $|\alpha|$-weighted kernel.

10. **M2 fourth-moment decomposition.** Compute diagonal, semi-diagonal, near-collision, and off-diagonal pieces separately. Compare signed and absolute versions.

11. **CRI test.** Compute $\Sigma_1,\Sigma_3,\Re(\Sigma_1\overline{\Sigma_3})$, and verify whether the CRI sign is favorable relative to $|\Sigma_1|^2+|\Sigma_3|^2$.

12. **H13 endpoint test.** Near $D\asymp X^{1/2}$, implement the post-transform kernel with stationary amplitudes and test whether the dual character survives as a non-conjugacy signed statistic or collapses into diagonal-unitary conjugation.

13. **Li--Yang source/PDF audit.** Resolve the Case A exponent ambiguity and record exact theorem hypotheses for $F$, weights, $H,M,T$, and absolute-value placement.

## Research strategy adjustment

Do not pivot away from the balanced hyperbola/Vaaler route. The route is now a well-structured reduction with one active analytic bottleneck: `M9`.

Round 23 should use a narrower division of labor:

1. **A1** should finish proof-draft infrastructure: exact H4 source citations, R5-Full with all edge cases, the conditional bridge, frozen M9 definitions, paired formulas, and signed bilinear M1 target.

2. **A2** should focus on $\mathcal M_2$ finite statistics. The highest-value task is not a new broad idea; it is a complete diagonal/semi-diagonal/near-collision taxonomy for the fourth moment and a precise statement of what cancellation hypothesis would imply M9b.

3. **A3** should execute computations rather than write more protocols. Priority tests are R5 tables, raw-vs-paired M9 regression, BSOS-M9a comparisons, M2 sign-loss/diagonal tests, and one H13 endpoint test with stationary amplitudes.

Keep H13 secondary. Run exactly one endpoint falsification test with amplitudes; do not let H13 displace the M9 finite-statistic work.

## Next-round prompts by agent

### For A1

Produce a proof-draft consolidation for Round 23.

Objectives:

1. Finalize H4 source normalization from the rendered Vaaler PDF. Quote exact theorem, page, and equation labels for:
   - Theorem 6 and equation (2.28) for $\widehat J$;
   - Section 7 equations (7.1)--(7.3) for $i_N,j_N,k_N$;
   - Theorem 18 and equation (7.14) for the residual inequality.

2. Insert H4-R22 into the best proof draft using:
$$
\psi_F(t)=\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$
$$
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$
and
$$
|R_H^F(t)|\le\frac1{2H+2}K_H(t).
$$

3. Insert R5-Full-R22 with all edge cases:
   - nearest-integer tie convention;
   - exact resonance $W_\Delta(0)=1$;
   - shifted-leg product $X\approx d(4m-\rho)$;
   - positivity of $\ell=4m-\rho$ in the large active range;
   - small-$X$ separation;
   - short blocks $D<X^{1/4}$;
   - dyadic bounded overlap.

4. State Bridge-R22 only conditionally:
$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

5. Freeze M9-R22 with actual Vaaler coefficients and explicitly state that M9 is open.

6. Insert M9-Pair-R22 as an implementation lemma for real weights only, with a regression warning for numerical code.

7. Insert Phi-Asymmetry-R22 and Alpha-Conjugacy-R22. Correct the endpoint note to $\Phi(0^+)=1$, $\Phi(1^-)=0$.

8. Preserve Li--Yang only as a guardrail unless the Case A/B theorem audit is completed. Do not claim endpoint theorem applicability.

### For A2

Focus on $\mathcal M_2$.

Objectives:

1. Rewrite the $\mathcal M_2$ fourth-moment statistic with exact constants and actual coefficients. Use $4^4=256$ if the scalar factor is displayed.

2. Classify configurations in the fourth moment:
   - exact diagonal;
   - pair-swapped diagonal;
   - semi-diagonal conditions such as $h_1+h_2=h_3+h_4$;
   - denominator-paired subfamilies;
   - near-collisions after clearing denominators:
$$
h_1d_2d_3d_4+h_2d_1d_3d_4-h_3d_1d_2d_4-h_4d_1d_2d_3.
$$

3. For each class, give either:
   - a proved bound at or below $X^{1+\epsilon}$ for the fourth moment, or
   - the exact cancellation hypothesis still needed.

4. State a precise theorem:
$$
\text{Fourth-moment class bounds} \Longrightarrow \mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon},
$$
or explicitly say which class blocks the implication.

5. Keep CRI as a falsification statistic unless you prove how it controls
$$
|\Sigma_1|^2+|\Sigma_3|^2-2\Re(\Sigma_1\overline{\Sigma_3}).
$$

6. Supply A3-ready formulas for:
   - the weighted $|\alpha_h|$ M2 kernel;
   - the unweighted M2 stress-test kernel;
   - the fourth-moment diagonal/semi-diagonal/off-diagonal decomposition;
   - the CRI statistic and its signed/absolute comparators.

7. Keep Q1/H12 bounded in scope. Avoid global no-go language.

### For A3

Execute verification tests; do not only write protocols.

Objectives:

1. Run R5 residual tables for $X=10^6$ and $X=10^8$, with
$$
D\asymp X^{1/4},\quad X^{3/8},\quad X^{1/2}.
$$
Include square, nonsquare, near-square, and divisor-rich $X$. Report first leg and shifted legs $\rho=1,3$. Use exact-resonance-safe arithmetic.

2. Verify the Fejer kernel exact-resonance rule:
$$
K_H(t)=H+1\quad(t\in\mathbb Z).
$$

3. Run raw-vs-paired M9 regression for real weights:
$$
\mathcal M_i^{\rm raw}(D;X)-\mathcal M_i^{\rm pair}(D;X),
\qquad i=1,2.
$$
Report absolute and relative errors.

4. Compute $\Phi$ values at
$$
u=1/4,1/3,1/2,2/3,3/4
$$
and endpoint limits. Confirm no code assumes $\Phi(1-u)=\Phi(u)$.

5. Implement the exact weighted `BSOS-M9a` kernel:
$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right).
$$
Report:
   - signed statistic;
   - unsigned statistic;
   - absolute majorant;
   - operator-norm comparator;
   - normalized ratios.

6. Implement the M2 weighted $h$-Cauchy kernel:
$$
K_{2;d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|\,|C_h|^2
e\left(\frac{hX}{4}\left(\frac1{d_1}-\frac1{d_2}\right)\right).
$$
Verify sign loss: $|C_h|^2$ leaves only odd-$h$ support.

7. Implement the M2 $d$-Cauchy diagonal test and report its $D^2$ scaling.

8. After A2 supplies exact fourth-moment formulas, compute diagonal, semi-diagonal, near-collision, and off-diagonal pieces separately. Report signed/absolute ratios.

9. Run one H13 endpoint test near $D\asymp X^{1/2}$ with stationary amplitudes included. Compare signed dual statistic, unsigned statistic, and diagonal-unitary operator-norm comparator.

10. Continue the Li--Yang source/PDF audit. Resolve the Case A exponent ambiguity and record exact theorem hypotheses before any theorem-import claim is made.

## Confidence

High confidence:

- H1--H3 remain stable accepted arithmetic reductions.
- H4-R22 is correct in substance, pending final citation transcription.
- The floor-compatible endpoint is covered by the Fejer majorant.
- R5-Full-R22 controls the fixed Fejer residual conditional on H4.
- Bridge-R22 is a valid conditional reduction.
- M9 remains open and is the active analytic bottleneck.
- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- $\Phi(1-u)=\Phi(u)$ is false.
- Standard weighted $h$-Cauchy for $\mathcal M_2$ loses the sign of $\chi_4(h)$.
- Cauchy over $d$ for $\mathcal M_2$ has a too-large diagonal at the top range.
- Black-box Li--Yang endpoint import is not justified.

Moderate confidence:

- The paired formulas are correct for real weights and suitable for implementation regression.
- BSOS-M9a is the right finite signed statistic for testing $\mathcal M_1$ beyond operator-norm blindness.
- The shifted-$F$ formulation is the cleanest theorem-comparison form for $\mathcal M_2$.
- The fourth-moment/open-path statistic is a useful falsification object for $\mathcal M_2$.
- H13 is worth exactly one endpoint falsification test with stationary amplitudes.

Low confidence:

- BSOS-M9a is asymptotically small enough to prove M9a.
- The fourth-moment statistic will yield M9b without a new spacing input.
- H13 avoids character erasure after the first serious spacing step.
- Current published Bombieri--Iwaniec/Li--Yang technology proves M9 at endpoint height.
- Any route in the current repo proves a new exponent.

No new Gauss circle exponent has been proved in Round 22.