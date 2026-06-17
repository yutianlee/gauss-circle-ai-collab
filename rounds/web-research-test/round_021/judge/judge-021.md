# Round 21 Judge Synthesis -- Revised with Alternative-Strategy Addendum

## Summary

Source basis: Round 21 prompt, agent outputs, Stage B reviews, and the human steering addendum `A-strategy-revised.md`.

Round 21 proves no new Gauss circle exponent. Its value is diagnostic and proof-infrastructure refinement.

The current conditional bridge remains:

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

Here $P(X)=N(\sqrt X)-\pi X$. The residual side is provisionally controlled by H4 plus R5-Full, conditional on final source-normalization of Vaaler and complete edge-case bookkeeping. The active analytic bottleneck remains M9: the fixed-Vaaler-coefficient main sums $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$.

The revision from the alternative-strategy file is conservative:

1. Alternative A, a fourth-moment or open-path non-conjugacy statistic for $\mathcal M_2$, is adopted as the primary bounded exploratory task for A2 and A3.
2. Alternative B, an H13 Poisson-first/asymmetric-dual-Cauchy--Schwarz route, is kept only as one endpoint falsification test near $D\asymp X^{1/2}$.
3. The alternative file's strongest obstruction language is rejected. `M9b-CS-Cancellation` is a bounded-scope diagnostic for standard Cauchy--Schwarz-over-$h$ normalizations, not a global no-go theorem. H13 product collapse is a useful warning, not a proved analytic tautology.

The main Round 21 additions remain:

1. A sharper diagnosis of $\mathcal M_2$: standard Cauchy--Schwarz over $h$ turns the frequency character $\chi_4(h)$ into odd-$h$ support, losing the character sign.
2. A confirmed obstruction to Cauchy--Schwarz over $d$ for $\mathcal M_1$: the endpoint diagonal is $D^2\asymp X$, above the squared target $X^{1/2+\epsilon}$.
3. A modeled H13 warning: B-process-first preserves a dual $\chi_4$ formally, but standard norm extraction again places it as diagonal unitary conjugation and loses it.
4. A useful A3 verification packet, with one important correction: the claimed symmetry $\Phi(1-u)=\Phi(u)$ is false and should be removed.
5. Continued caution on Li--Yang: the final exponent gap $\theta^*-1/4>0$ blocks black-box endpoint import; any internal Case A/B range claim still requires exact source/PDF reconciliation before theorem-level use.

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

The accepted arithmetic identity remains:

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

For active dyadic blocks,

$$
X^{1/4}\le D\le X^{1/2},
$$

use local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ are removed before Vaaler expansion and bounded directly using $|\psi_F|\le 1/2$.

The Vaaler coefficients are frozen as:

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

The official open M9 targets are:

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

The required estimate remains:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for $X^{1/4}\le D\le X^{1/2}$. No Round 21 output proves this.

For real dyadic weights, the paired implementation formulas are:

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

These are implementation formulas only. They require real dyadic weights and regression against the raw two-sided complex definitions.

## Useful fragments by source

### From A1

A1 supplies the canonical proof-draft framework.

The useful bridge remains:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

A1 correctly keeps this conditional. The residual mechanism is:

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
\qquad
|R_H^F(t)|\le \frac1{2H+2}K_H(t),
$$

where

$$
K_H(t)
=
\sum_{|k|\le H}\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin\pi(H+1)t}{\sin\pi t}\right)^2.
$$

The endpoint convention is correct:

$$
V_H(n)=0,
\qquad
\psi_F(n)=-\frac12,
\qquad
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

A1's R5 product-count proof remains the official residual mechanism. With

$$
H\asymp D X^{-1/4},
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

one uses

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg, choose $m$ nearest to $X/d$ and define

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
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
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
X\approx d(4m-\rho),
$$

and the same product-count proof applies after writing $\ell=4m-\rho$.

A1's Li--Yang guardrail remains important. With $D=X^\delta$ and $H=X^\beta$, the endpoint Vaaler height is

$$
\beta_V=\delta-\frac14.
$$

Li--Yang's final record-exponent range gives

$$
\beta_*=\delta-\theta^*,
\qquad
\theta^*=0.3144831759741\cdots.
$$

At $D=X^{1/2}$, black-box Li--Yang reaches only $\beta_*=0.1855168240259\cdots$, below the Vaaler endpoint $\beta_V=1/4$. This is a theorem-application guardrail, not a no-go theorem for all Bombieri--Iwaniec variants.

### From A2

A2's main contribution is the $\mathcal M_2$ Cauchy--Schwarz diagnosis.

Let

$$
C_h=e(h/4)-e(3h/4)=2i\chi_4(h).
$$

Under a standard $|\alpha_h|$-weighted Cauchy--Schwarz step over $h$, the sign of $\chi_4(h)$ is lost because

$$
|C_h|^2=
\begin{cases}
4,&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

A consistent kernel version is:

$$
K_{2;d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
|C_h|^2
 e\left(
\frac{hX}{4}\left(\frac1{d_1}-\frac1{d_2}\right)
\right).
$$

Equivalently,

$$
K_{2;d_1,d_2}^{(|\alpha|)}
=
4w_D(d_1)w_D(d_2)
\sum_{\substack{1\le |h|\le H_D\\2\nmid h}}
|\alpha_{h,H_D}|
 e\left(
\frac{hX}{4}\left(\frac1{d_1}-\frac1{d_2}\right)
\right).
$$

The diagonal is acceptable, of size $D\log H_D$. The obstacle is not diagonal size in this normalization; the obstacle is that the frequency-character sign has become only parity support. This should be recorded as a bounded-scope diagnostic, not a no-go theorem.

A2 also correctly identifies that Cauchy--Schwarz over the spatial variable $d$ for $\mathcal M_1$ is too crude. Under that normalization, the endpoint diagonal contribution is

$$
D^2,
$$

which becomes $X$ at $D\asymp X^{1/2}$, exceeding the squared target $X^{1/2+\epsilon}$.

A2's Q1/H12 diagnostics remain useful. If $U=\operatorname{diag}(\chi_4(d))$ on odd denominators and a proof estimates $U^*KU$ by a unitarily invariant norm, then

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

For pure cyclic traces,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

These block only norm-only and pure cyclic-trace routes. They do not block direct signed bilinear forms, open-path moments, cross-residue statistics, or a new signed spacing theorem.

A2's CRI direction for $\mathcal M_2$ remains useful but not yet a lemma. The alternative-strategy file strengthens the motivation for this direction: the next version should either produce a finite fourth-moment/non-conjugacy statistic with an implication to $\mathcal M_2$, or explicitly label the statistic as a falsification metric.

### From A3

A3 supplies useful verification work:

1. H4 is traced to Vaaler's Theorem 6, Section 7 definitions, and Theorem 18.
2. R5 exact-resonance handling is checked with the cap $W_\Delta(0)=1$.
3. Raw-versus-paired formulas for $\mathcal M_1,\mathcal M_2$ are tested on small examples.
4. The BSOS matrix test confirms numerically that diagonal-unitary conjugation preserves operator norm.
5. The $\mathcal M_2$ shift cancellation after Cauchy--Schwarz over $h$ is verified symbolically.
6. The leading H13 post-transform model again places the dual character as diagonal unitary conjugation.

A3's verification packet should be used as a regression appendix, not as asymptotic evidence. Its small numerical examples validate formulas, not estimates.

A3 also contains one serious algebraic error: it claims or uses

$$
\Phi(1-u)=\Phi(u).
$$

This is false. In fact,

$$
\Phi(1-u)
=
1-u-\pi u(1-u)\cot(\pi u),
$$

so generally $\Phi(1-u)\ne\Phi(u)$. For example,

$$
\Phi(1/3)=\frac{2\pi}{9\sqrt3}+\frac13,
\qquad
\Phi(2/3)=-\frac{2\pi}{9\sqrt3}+\frac23.
$$

This error does not affect the coefficient conjugacy

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

because that relation only uses that $\Phi(|h|/(H+1))$ is real and that $h$ changes sign. It should be corrected before any further numerical implementation.

### From the alternative-strategy addendum

The alternative-strategy file is useful as a steering note, not as a replacement for the judge synthesis.

Alternative A is the strongest addition. It correctly targets the main defect of standard Cauchy--Schwarz over $h$ for $\mathcal M_2$: the sign $\chi_4(h)$ is destroyed when $|C_h|^2$ is formed. A fourth moment or open-path twisted trace may preserve signs longer. However, the file overstates the conclusion when it says the modulo-$4$ restrictions actively suppress diagonal blowup. That needs an explicit diagonal/semi-diagonal/off-diagonal classification.

Alternative B is a useful endpoint falsification test, but not a route pivot. H13 Poisson-first can preserve a dual character formally, but its leading phase has zero Hessian and standard norm extraction may again make the character a diagonal unitary. The claimed $k=hm$ collapse into a Hardy/Voronoi identity is a useful diagnostic model, not a lemma until stationary amplitude, support, boundary terms, and dyadic truncation are all written explicitly.

The addendum's proposal to elevate `M9b-CS-Cancellation` to a formal no-go lemma is rejected. The correct statement is bounded: standard Cauchy--Schwarz over $h$ for $\mathcal M_2$ loses the sign of $\chi_4(h)$; this does not rule out fourth moments, open-path statistics, paired-residue estimates, or non-conjugacy signed bilinear forms.

## Rejected or risky ideas

1. **Reject: Round 21 proves a new exponent.** No estimate for M9 is proved. The conditional bridge remains conditional.

2. **Reject: M9 is solved by H4 plus R5.** H4 plus R5 controls the Vaaler residual. It does not control the fixed-coefficient main sums.

3. **Reject: the false symmetry $\Phi(1-u)=\Phi(u)$.** This is algebraically false and should be removed from the lemma bank and code comments.

4. **Reject: using A3's small numerical checks as asymptotic evidence.** They are regression tests only.

5. **Reject: treating $\mathcal M_2$ Cauchy--Schwarz character-blindness as a global impossibility theorem.** It applies to the displayed standard Cauchy--Schwarz-over-$h$ normalizations. It does not rule out direct bilinear estimates, paired-residue statistics, fourth moments, open-path traces, or non-conjugacy methods.

6. **Reject: treating the H13 leading-term Q1-collapse as a full obstruction.** It is a leading stationary-phase diagnostic. Boundary terms, transition terms, nonstationary terms, and short dual ranges remain unaudited.

7. **Reject: treating H13 product collapse $k=hm$ as a proved analytic tautology.** Collapsing the leading model may reconstruct a Hardy/Voronoi-type object, but that claim is not a proof-draft lemma until amplitudes, weights, supports, boundary terms, and errors are written and checked.

8. **Reject: importing Li--Yang as an endpoint theorem.** Li--Yang's final exponent $\theta^*=0.314483\ldots$ is above $1/4$, and no checked internal theorem currently covers the Vaaler endpoint height $H_D\asymp D X^{-1/4}$.

9. **Reject: arbitrary-coefficient or $L^1$ stress norms as active dependencies.** They remain diagnostics. The proof route uses fixed Vaaler coefficients.

10. **Reject: ambiguous $\mathcal M_2$ Cauchy--Schwarz kernels.** The next proof draft should choose a consistent normalization or state both separately. Mixing the scalar factor and kernel placement of $|C_h|^2$ creates implementation errors.

11. **Reject: `4th moment works' as a theorem.** Alternative A is promising because it may preserve signs, but it also creates additional diagonal and near-diagonal configurations. Its value depends on an explicit finite expansion and diagonal classification.

## Known gaps

1. **M9 remains open.** Need endpoint-strength estimates for $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ with fixed Vaaler coefficients.

2. **H4 final source transcription.** The Vaaler theorem is source-located in substance, but the proof draft still needs exact rendered page/equation transcription and notation mapping.

3. **R5 final proof-draft edge cases.** Need to record nearest-integer ties, exact resonances, shifted-leg positivity of $\ell=4m-\rho$, small $X$ absorption, dyadic overlap, and real-valued/bounded dyadic weights.

4. **$\mathcal M_2$ Cauchy--Schwarz normalization.** Need one frozen normalization, or two explicitly separated versions, before A3 implements tests.

5. **BSOS-M9a is only a sufficient finite target.** No estimate for $\mathcal S_{\rm signed}$ has been proved.

6. **CRI-M2 and fourth-moment M2 statistics are only proposed.** Need a finite bilinear or four-variable definition, target inequality, implication to $\mathcal M_2$, and falsification criteria.

7. **H13 lacks a uniform stationary-phase lemma.** The modeled diagonal sizes depend on amplitude normalization, active stationary range, boundary terms, nonstationary tails, and the short-dual regime.

8. **H13 asymmetric dual-CS remains unverified.** It needs an exact endpoint kernel with stationary amplitudes and a diagonal/off-diagonal target. It should be treated as a falsification test until it implies a bound.

9. **Li--Yang internal theorem audit remains incomplete.** Exact Case A/B conditions, main theorem hypotheses, allowed weights, allowed $F$, final $S/H$ target, and endpoint range should be reconciled from TeX and typeset PDF.

10. **Numerical tests need scale and precision.** High-precision Fejer, M9, BSOS, M2, CRI/fourth-moment, and H13 tests are still pending at meaningful $X$.

11. **M9b shifted-$F$ theorem extension remains open.** The shifted functions

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

have the same derivative nondegeneracy, but theorem-level admissibility at endpoint height and with fixed Vaaler weights has not been established.

## New lemmas to add

### H4-R21. Finite Vaaler approximation with floor-compatible residual

Status: external theorem dependency, source-normalized in substance.

For every integer $H\ge1$ and every real $t$,

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

### R5-Full-R21. Fejer residual product-count bound

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

### Bridge-R21. Conditional reduction to M9

Status: conditional theorem.

Assume H1--H3, H4-R21, R5-Full-R21, and M9-R21. Then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-R21. Fixed-coefficient main-term target

Status: open.

For all active dyadic blocks,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The coefficients are the actual Vaaler coefficients $\alpha_{h,H_D}$, not arbitrary bounded coefficients.

### M9-Pair-R21. Paired implementation formulas

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

### BSOS-M9a-R21. Signed off-diagonal sufficient target

Status: derived sufficient target, not an estimate.

Under the frozen $|\alpha_h|$-weighted Cauchy--Schwarz normalization, define

$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
 e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right)
$$

on odd denominators. If

$$
\left|
\sum_{\substack{d_1\ne d_2\\d_i\in\mathcal D_{\rm odd}}}
\chi_4(d_1)\chi_4(d_2)
K_{d_1,d_2}^{(|\alpha|)}
\right|
\ll_\epsilon X^{1/2+\epsilon},
$$

then

$$
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M2-CS-Character-Blindness-R21

Status: proved diagnostic under fixed Cauchy--Schwarz normalization.

For $C_h=e(h/4)-e(3h/4)$, standard $h$-Cauchy--Schwarz replaces $C_h$ by $|C_h|^2$, and

$$
|C_h|^2=
\begin{cases}
4,&2\nmid h,\\
0,&2\mid h.
\end{cases}
$$

Thus the sign of $\chi_4(h)$ is lost and only an odd-$h$ restriction remains. This is not a global no-go theorem.

### M2-NonConjugacy-FourthMoment-R21

Status: proposed exploratory target, not a lemma.

Let

$$
S_h(D;X)=\sum_d w_D(d)e(hX/(4d)),
\qquad
C_h=e(h/4)-e(3h/4).
$$

A fourth-moment or open-path statistic should begin from the exact expansion of

$$
\left|
\sum_{1\le |h|\le H_D}\alpha_{h,H_D}C_hS_h(D;X)
\right|^4.
$$

The finite expansion contains variables $h_1,h_2,h_3,h_4$ and $d_1,d_2,d_3,d_4$ with character factor

$$
C_{h_1}\overline{C_{h_2}}C_{h_3}\overline{C_{h_4}},
$$

which on odd frequencies is a scalar multiple of

$$
\chi_4(h_1)\chi_4(h_2)\chi_4(h_3)\chi_4(h_4).
$$

A sufficient fourth-moment target would have scale

$$
\ll_\epsilon X^{1+\epsilon},
$$

because this would imply $\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}$. The next round should classify diagonal, semi-diagonal, and off-diagonal configurations before this can be promoted.

### CS-d-Diagonal-Obstruction-R21

Status: proved under displayed primal normalization.

Cauchy--Schwarz over $d$ in $\mathcal M_1$ produces endpoint diagonal size

$$
D^2\asymp X
$$

at $D\asymp X^{1/2}$, exceeding the squared endpoint target $X^{1/2+\epsilon}$.

### H13-Dual-Diagonal-Blowup-R21

Status: derived-under-assumptions diagnostic.

Under the modeled leading H13 stationary phase, Cauchy--Schwarz over $h$ or $m$ produces endpoint diagonal sizes above the squared endpoint target. This depends on the stationary-phase amplitude and support assumptions.

### H13-Asymmetric-Dual-CS-Falsification-R21

Status: proposed endpoint falsification test.

After applying H13 to the spatial-character sum, write the leading dual form with phase

$$
\Phi(h,m)\asymp \sqrt{Xhm}
$$

and dual length

$$
m\asymp \frac{hX}{D^2}.
$$

Near $D\asymp X^{1/2}$, test whether Cauchy--Schwarz over $m$ preserves a signed $h_1,h_2$ off-diagonal statistic involving $\chi_4(h_1)\chi_4(h_2)$ and whether its diagonal plus off-diagonal target is consistent with $X^{1/2+\epsilon}$ after squaring. This is not a theorem until the amplitude, boundary terms, and implication are explicit.

### H13-Product-Collapse-Diagnostic-R21

Status: diagnostic model, not a lemma.

If one collapses a leading H13 model by $k=hm$, the resulting expression may resemble a classical Hardy/Voronoi one-dimensional expansion. This warns against generic two-dimensional full-rank methods and against treating H13 as automatically new. It is not a proof-level statement until stationary amplitudes, dyadic support, boundary contributions, and errors are derived.

### H13-Dual-Q1-Collapse-R21

Status: derived-under-assumptions diagnostic.

In the modeled leading H13 kernel, the dual character $\chi_4(m)$ appears as diagonal unitary conjugation. Operator-norm extraction therefore loses it.

### Phi-Correction-R21

Status: proved algebraic correction.

The function

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u
$$

is not symmetric under $u\mapsto1-u$. In general,

$$
\Phi(1-u)=1-u-\pi u(1-u)\cot(\pi u)\ne \Phi(u).
$$

Coefficient conjugacy remains true:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

## Counterexample checks to run

1. **Corrected $\Phi$ table.** Compute exact/high-precision values for $u=1/4,1/3,1/2,2/3,3/4$ and verify that no symmetry $\Phi(1-u)=\Phi(u)$ is used.

2. **H4 rendered-page verification.** Verify Vaaler Theorem 6, Section 7 definitions, and Theorem 18 from rendered page images and exact equation numbers.

3. **R5 high-precision residual tables.** For $X=10^6,10^8$ and $D\asymp X^{1/4},X^{3/8},X^{1/2}$, compute first-leg and shifted-leg normalized residuals. Include exact-resonance and near-resonance cases.

4. **Raw-vs-paired M9 regression.** Compute raw two-sided complex definitions and paired real formulas for $\mathcal M_1,\mathcal M_2$ at several $X,D,H_D$. Require agreement to high precision.

5. **Fixed-coefficient versus stress-norm comparison.** Compare actual Vaaler coefficients with random/adversarial coefficients of the same magnitude profile and with termwise $L^1$ norms. Treat as diagnostic only.

6. **BSOS-M9a finite matrix test.** Compute $\mathcal S_{\rm signed}$, $\mathcal S_{\rm abs}$, and $|\mathcal D_{\rm odd}|\|K_{\rm off}\|_{\operatorname{op}}$ for endpoint-scale blocks. Track signed/absolute ratios.

7. **M2 combined-kernel regression.** Implement both consistent Cauchy--Schwarz normalizations. Show exactly where $|C_h|^2$ is placed and verify that both lose the sign of $\chi_4(h)$.

8. **M2 fourth-moment / CRI falsification test.** After A2 supplies a finite definition, compute signed statistic, unsigned comparator, absolute majorant, and operator-norm comparator for $D\asymp X^{1/4},X^{3/8},X^{1/2}$.

9. **H13 regime split.** Separate interior stationary, boundary stationary, nonstationary, and $M_{\rm dual}\asymp1$ regimes before drawing conclusions from H13.

10. **H13 endpoint asymmetric dual-CS test.** At most one test near $D\asymp X^{1/2}$, with stationary amplitudes included. Compare signed and unsigned dual statistics, and label the result as falsification data only.

11. **H13 product-collapse regression.** If A2 writes the exact leading H13 model, compare the uncollapsed $(h,m)$ expression with the collapsed $k=hm$ expression. Do not call numerical agreement an asymptotic proof.

12. **Li--Yang source audit.** Verify the Case A condition, Case B condition, main theorem hypotheses, final $S/H$ target, allowed weights, allowed $F$, and endpoint range from the TeX and typeset PDF. The abstract is not sufficient for internal theorem use.

## Research strategy adjustment

Continue the balanced arithmetic hyperbola/Vaaler route. Do not pivot.

The route should now be treated as proof infrastructure plus a sharply isolated open analytic problem:

$$
\text{M9}=\{\mathcal M_1,\mathcal M_2\text{ fixed-coefficient endpoint estimates}\}.
$$

The alternative-strategy file modifies the next round as follows:

1. Keep the conditional bridge and proof-infrastructure tasks as the main route.
2. Add Alternative A as the primary bounded exploratory task for $\mathcal M_2$: a fourth-moment or open-path non-conjugacy statistic.
3. Keep Alternative B/H13 as one endpoint falsification test only.
4. Replace all global no-go language with bounded-scope diagnostics.

Suggested effort split for Round 22:

- A1: primary proof-draft consolidation and lemma-bank/gap-register updates.
- A2: primary exact finite statistics for $\mathcal M_2$, especially fourth-moment/open-path/CRI statistics and consistent Cauchy--Schwarz kernels.
- A3: high-precision computational and source-audit verification.

Short-term priorities:

1. Finish proof-draft infrastructure: H4 exact citation, R5-Full edge cases, bridge theorem.
2. Make M9 diagnostics executable: BSOS for $\mathcal M_1$, repaired Cauchy--Schwarz kernels for $\mathcal M_2$, and a finite fourth-moment/CRI statistic if one can be made meaningful.
3. Keep all obstruction language bounded-scope. The diagnostics rule out certain norm-extraction routes, not all possible signed bilinear or spacing methods.
4. Use numerics only to verify formulas and falsify candidate finite statistics, not as evidence of an asymptotic theorem.
5. Keep Li--Yang as a theorem-application guardrail. Structural phase similarity is not theorem applicability.

## Next-round prompts by agent

### For A1

Produce a proof-draft consolidation for Round 22.

Objectives:

1. Insert H4-R21 with exact Vaaler page/equation citations and floor-compatible endpoint conversion.
2. Insert R5-Full-R21 with all edge cases: nearest-integer ties, exact resonances via $W_\Delta(0)=1$, shifted-leg positivity of $\ell=4m-\rho$, small $X$, dyadic overlap, and short blocks $D<X^{1/4}$.
3. State Bridge-R21 only conditionally:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Do not imply M9 is proved.

4. Freeze M9-R21 as the sole active analytic bottleneck with actual Vaaler coefficients.
5. Add M9-Pair-R21 as an implementation lemma for real weights, with a raw-vs-paired regression warning.
6. Add M2-CS-Character-Blindness-R21 only after fixing the Cauchy--Schwarz normalization. If both normalizations are useful, state them separately and show that both lose the sign of $\chi_4(h)$.
7. Add CS-d-Diagonal-Obstruction-R21 as proved under its displayed normalization.
8. Add H13-Dual-Diagonal-Blowup-R21, H13-Dual-Q1-Collapse-R21, and H13-Product-Collapse-Diagnostic-R21 only as derived-under-assumptions diagnostics.
9. Correct all $\Phi$ statements: explicitly reject $\Phi(1-u)=\Phi(u)$.
10. Add an `Alternative Strategy Status` subsection:
    - Alternative A: fourth-moment/open-path non-conjugacy statistic for $\mathcal M_2$, proposed and assigned mainly to A2.
    - Alternative B/H13: endpoint falsification test only.
    - M9b-CS character loss: bounded-scope diagnostic, not a global no-go theorem.

Verification tasks:

- Include a short algebra check for $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- Include a short check of $\Phi(1/3)$ and $\Phi(2/3)$ showing the false symmetry.
- State exactly which Li--Yang claims are safe: the final $\theta^*$ gap is safe; internal Case A/B theorem use remains pending source/PDF audit.
- Record H13 product collapse only as a diagnostic requiring a full stationary-phase and dyadic-support derivation before lemma-bank promotion.

Exploratory allocation:

Develop one exact direct signed bilinear formulation for $\mathcal M_1$ or $\mathcal M_2$ that avoids immediate operator-norm extraction. State the finite object, a target bound, and what would falsify it.

### For A2

Focus on $\mathcal M_2$ finite statistics and bounded-scope obstruction language.

Objectives:

1. Rewrite the $\mathcal M_2$ Cauchy--Schwarz derivation with one fixed normalization, or present two separate normalizations without mixing scalar and kernel factors.
2. For each normalization, give:
   - scalar factor;
   - exact kernel;
   - diagonal size;
   - off-diagonal target;
   - where $|e(h/4)-e(3h/4)|^2$ appears;
   - proof that the sign of $\chi_4(h)$ is lost.
3. Define `M2-NonConjugacy-FourthMoment-R22` as an explicit finite statistic over $h_1,h_2,h_3,h_4,d_1,d_2,d_3,d_4$ with actual Vaaler coefficients.
4. Classify diagonal, semi-diagonal, and off-diagonal configurations in that fourth-moment expansion.
5. State the exact target scale needed to imply

$$
\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

6. Either prove a conditional implication from the fourth-moment/CRI target to $\mathcal M_2$, or label it only as a falsification statistic.
7. Define `CRI-M2-Statistic-R22` as an explicit finite bilinear or cross-residue form if it is distinct from the fourth-moment statistic.
8. Revisit direct signed bilinear forms for $\mathcal M_1$ using rational-collision character factorization, explicitly avoiding operator-norm extraction.
9. Keep Q1-Spectral and H12 in bounded scope. Do not phrase them as global impossibility results.

Verification tasks:

- Supply A3-ready formulas for the M2 kernels and the fourth-moment/CRI statistic.
- State all normalizations with constants up to harmless absolute factors.
- Include a checklist of what a theorem would need to prove for the odd-$h$ character-blind kernel.
- Compare any H13 asymmetric-dual-CS proposal with the Round 21 modeled diagonal calculations and identify normalization mismatches.

Exploratory allocation:

Try one non-conjugacy statistic for $\mathcal M_2$ that pairs $h\equiv1\pmod4$ against $h\equiv3\pmod4$ before squaring destroys the sign. Give its finite formula, target scale, and falsification test.

### For A3

Run corrected high-precision verification and executable finite-statistic tests.

Objectives:

1. Correct the $\Phi$ table:
   - compute $\Phi(1/4),\Phi(1/3),\Phi(1/2),\Phi(2/3),\Phi(3/4)$;
   - explicitly verify that $\Phi(1-u)\ne\Phi(u)$ in general;
   - verify $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
2. Run raw-vs-paired M9 regressions for several $X,D,H_D$, including $D\asymp X^{1/4},X^{3/8},X^{1/2}$.
3. Produce high-precision R5 residual tables for $X=10^6,10^8$ and for first-leg plus shifted-leg residuals. Include exact resonance and near-resonance cases.
4. Implement fixed-coefficient versus stress-norm comparisons:
   - actual Vaaler coefficients;
   - random phase coefficients with the same magnitudes;
   - adversarial signs;
   - termwise $L^1$ comparator.
5. Implement BSOS-M9a tests:
   - $\mathcal S_{\rm signed}$;
   - $\mathcal S_{\rm abs}$;
   - $|\mathcal D_{\rm odd}|\|K_{\rm off}\|_{\operatorname{op}}$;
   - signed/absolute ratios.
6. Implement M2 combined-kernel tests for both consistent Cauchy--Schwarz normalizations after A2 supplies final formulas.
7. Implement the M2 fourth-moment/CRI tests only after A2 supplies an exact finite statistic.
8. Re-audit Li--Yang Case A/B from the TeX and typeset PDF with exact labels. Do not rely on a single TeX snippet outside the theorem's variable conventions.
9. For H13, distinguish interior stationary, boundary stationary, nonstationary, and $M_{\rm dual}\asymp1$ regimes. Do not infer a theorem from the leading stationary model alone.
10. Run at most one H13 endpoint asymmetric-dual-CS test near $D\asymp X^{1/2}$ with stationary amplitudes included. Compare signed and unsigned dual statistics, but label it explicitly as a falsification test.
11. If asked to test H13 product collapse, compare raw uncollapsed and collapsed leading-model sums only after A2 or A1 supplies the exact finite model. Do not describe numerical agreement as proof of an analytic identity.

Verification rules:

- Use high precision for Fejer kernels near integers.
- Use exact modular/resonance detection where possible.
- Preserve raw data tables in commit-ready form.
- Separate formula regression from asymptotic evidence.
- Report failures and unexpected growth plainly.

Exploratory allocation:

Prioritize Alternative A tests once A2 defines them. The single H13 endpoint test is secondary and should not displace R5/M9/BSOS/M2-kernel verification.

## Confidence

High confidence:

- H1--H3 are stable.
- H4 is normalized correctly in substance, pending final rendered-page citation.
- The endpoint convention $\psi_F(n)=-1/2$ is covered by the Fejer majorant.
- R5-Full controls the fixed Fejer residual conditional on H4.
- The correct Vaaler coefficient conjugacy is $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- M9 remains the sole active analytic bottleneck.
- Q1-Spectral and H12 are valid bounded-scope diagnostics.
- Standard Cauchy--Schwarz over $h$ for $\mathcal M_2$ loses the sign of $\chi_4(h)$.
- Black-box Li--Yang endpoint import is unavailable.
- Alternative A is worth converting into an exact finite statistic.

Moderate confidence:

- The paired M9 formulas are correct for real weights, pending broader regression.
- BSOS-M9a is a useful sufficient finite target.
- The Cauchy--Schwarz-over-$d$ diagonal obstruction is correct under the displayed normalization.
- H13 leading-term diagnostics correctly identify a likely character-blind norm-extraction trap.
- H13 product collapse is a useful diagnostic warning after a full leading-model derivation.
- A2's CRI/fourth-moment direction may be useful if converted to a precise finite statistic.

Low confidence:

- BSOS-M9a is small enough asymptotically to prove $\mathcal M_1$.
- CRI-M2 or the proposed fourth-moment statistic will imply $\mathcal M_2$.
- H13 can avoid diagonal-unitary blindness without a new signed spacing mechanism.
- Current published technology proves M9.
- Any route currently in the repo proves a new Gauss circle exponent.

Confidence that Round 21 proves a new Gauss circle exponent: 0.00.