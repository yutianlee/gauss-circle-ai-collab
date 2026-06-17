## Selected main route

Source basis: Round 20 prompt/context and active A1/A2/A3 materials in the uploaded `judge_20.md` packet, especially the required Stage C schema, Round 20 review convergence, BSOS/M9b verification targets, and confidence statements.

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

This is **not** a proof of the Gauss circle conjectural bound. Round 20 proves no new exponent. The residual side remains provisionally controlled by `H4 + R5-Full`, conditional on final source-level normalization of Vaaler and proof-draft edge-case bookkeeping. The active analytic bottleneck remains `M9`: the fixed-Vaaler-coefficient reciprocal main sums.

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

For dyadic denominator blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

use the local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ should be removed before invoking Vaaler and bounded trivially by $|\psi_F|\le 1/2$.

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

The two official main sums are

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

The endpoint-strength target remains open:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for $X^{1/4}\le D\le X^{1/2}$.

## Useful fragments by source

### From A1

A1's proof-draft consolidation remains the strongest infrastructure contribution. It correctly keeps the bridge theorem conditional and keeps `M9` as the sole unproved analytic input.

A1's `H4-R20` normalization should be merged into the proof draft. The finite Vaaler statement is:

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}
\alpha_{h,H}e(ht)
+
R_H^F(t),
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

The endpoint convention is correct: the Vaaler centered polynomial has value $0$ at integers, while $\psi_F(n)=-1/2$, and

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

The coefficient conjugacy is also settled:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

The relation $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$ remains rejected.

A1's `R5-Full-R20` proof should be accepted as the proof-draft residual mechanism conditional on H4. With

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

For the first residual leg, choosing $m$ nearest to $X/d$ gives

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

Use the exact-resonance-safe cap

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min\left(1,\Delta^2/u^2\right),&u\ne0.
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

For the shifted residual legs, near-integrality of

$$
\frac{X/d+\rho}{4},
\qquad \rho\in\{1,3\},
$$

is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing $\ell=4m-\rho$ gives $n=d\ell$ with $\ell\equiv-\rho\pmod 4$, and the congruence restriction only reduces multiplicity.

A1's Li--Yang range audit remains a guardrail, not a proof input. With $D=X^\delta$ and $H=X^\beta$, the Vaaler endpoint height is

$$
\beta_V=\delta-\frac14.
$$

Li--Yang's final record-exponent range has

$$
\beta_*=\delta-\theta^*,
\qquad
\theta^*=0.3144831759741\cdots.
$$

At $D=X^{1/2}$,

$$
\beta_V=\frac14,
\qquad
\beta_*=0.1855168240259\cdots,
$$

so black-box Li--Yang import falls short of the endpoint. The Case A ambiguity involving $T^{-7/16}$ versus $T^{7/16}$ must still be resolved from the typeset paper or source before any theorem-level claim.

### From A2

A2's main useful contribution is the finite signed statistic for `M9a`.

Under the frozen $|\alpha_h|$-weighted Cauchy--Schwarz normalization, define

$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right)
$$

on

$$
\mathcal D_{\rm odd}
=
\{d:D\le d<2D,\ 2\nmid d\}.
$$

Then define

$$
\mathcal S_{\rm signed}
=
\sum_{\substack{d_1,d_2\in\mathcal D_{\rm odd}\\d_1\ne d_2}}
\chi_4(d_1)\chi_4(d_2)K_{d_1,d_2}^{(|\alpha|)}.
$$

Let

$$
L=\sum_{1\le |h|\le H_D}|\alpha_{h,H_D}|\asymp \log H_D.
$$

A2's derivation gives

$$
|\mathcal M_1|^2
\le
16L(\mathcal S_{\rm diag}+\mathcal S_{\rm signed}),
$$

with

$$
\mathcal S_{\rm diag}\asymp D L.
$$

Since $D\le X^{1/2}$, the diagonal contribution is acceptable after logarithmic absorption:

$$
D(\log H_D)^2\ll_\epsilon X^{1/2+\epsilon}.
$$

Thus the following implication is correct as a sufficient target:

$$
|\mathcal S_{\rm signed}|\ll_\epsilon X^{1/2+\epsilon}
\Longrightarrow
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Status: useful finite target and falsification statistic, not an estimate.

A2's `Q1-Spectral` and `H12` diagnostics remain valid in their bounded scope. If the character enters a matrix argument only through

$$
U=\operatorname{diag}(\chi_4(d))
$$

on the odd denominator support, then

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}},
$$

so operator-norm, Frobenius, Schur, Gershgorin, absolute-value matrix, and pure cyclic-trace methods are character-blind under that reduction. This does not block direct signed bilinear forms, non-conjugacy traces, open-path statistics, or a new signed spacing theorem.

A2's `M9b` warning is serious but should remain conditional. In the shifted-$F$ formulation, after Cauchy--Schwarz over $h$, the phase shift $\rho/4$ cancels inside the off-diagonal kernel. The correct combined kernel to study is

$$
\sum_{1\le |h|\le H_D}
|\alpha_h|
|e(h/4)-e(3h/4)|^2
e\left(\frac{hX}{4}\left(\frac1{d_1}-\frac1{d_2}\right)\right).
$$

Because

$$
|e(h/4)-e(3h/4)|^2
=
\begin{cases}
4,&2\nmid h,\\
0,&2\mid h,
\end{cases}
$$

this leaves an odd-$h$ restricted, character-blind reciprocal kernel in the $d$ variables. This is a strong warning for standard Cauchy--Schwarz/spacing approaches to $\mathcal M_2$, not a theorem that $\mathcal M_2$ is impossible.

A2's diagonal obstruction for alternative Cauchy--Schwarz choices should not be promoted beyond the stated assumptions until the required uniform stationary-phase lemma is supplied.

### From A3

A3's useful contribution is verification infrastructure, but Round 20 still falls short of the requested executed numerical certificate.

Useful pieces to retain:

1. A3 confirms the coefficient convention

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

2. A3 gives paired implementation formulas for real weights. With

$$
A_h(D;X)=\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

one has

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}A_h(D;X).
$$

With

$$
B_h(D;X)=\sum_d w_D(d)e(hX/(4d)),
$$

one has

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\operatorname{Re}B_h(D;X).
$$

These are implementation formulas only. They must be regressed numerically against the raw two-sided complex definitions for real weights.

3. A3's Q1 matrix check is a useful sanity check, but the tested matrices are too small to serve as evidence about asymptotic cancellation.

4. A3's R5 toy data are formula checks only. They do not constitute asymptotic evidence. Future tests must use high precision or exact resonance detection, because near integers the sine quotient formula for $K_H(t)$ is numerically unstable.

5. A3's H13 formulas remain useful at the formal level. The modulo-$4$ Poisson transform preserves a dual character, the stationary point satisfies

$$
u_0=2\sqrt{\frac{hX}{m}},
\qquad
m\asymp \frac{hX}{D^2},
$$

and the leading dual phase is

$$
\sqrt{hXm}.
$$

The phase

$$
\Phi(h,m)=\sqrt{Xhm}
$$

has zero Hessian determinant, so generic full-rank two-dimensional stationary phase or full-rank decoupling still cannot be invoked.

A3's next contribution must be executed computation: R5 tables, raw-versus-paired M9 regression, Q1 norm checks, and BSOS signed/absolute/operator-norm ratios using A2's exact weighted kernel.

## Rejected or risky ideas

1. **Reject: Round 20 proves or improves a Gauss circle exponent.**
No estimate for `M9` was proved. The bridge theorem remains conditional.

2. **Reject: treating the conditional bridge as a proof.**
The unproved analytic assertion is exactly

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

3. **Reject: arbitrary-coefficient variants as active dependencies.**
Random, arbitrary, or $L^1$ stress norms are diagnostic tests only. The actual Vaaler reduction uses the fixed coefficients $\alpha_{h,H_D}$.

4. **Reject: black-box Li--Yang import at endpoint height.**
The phase class is relevant, but the audited theorem ranges do not reach $H_D\asymp D X^{-1/4}$, and Li--Yang's exponent $\theta^*>1/4$ remains above the conjectural target.

5. **Reject: operator-norm methods as character-aware when the character enters only by diagonal conjugation.**
`Q1-Spectral` shows such routes are character-blind.

6. **Reject: BSOS-M9a as a proved estimate.**
A2 proved only a conditional implication from an off-diagonal target to $\mathcal M_1$. No bound for $\mathcal S_{\rm signed}$ was proved.

7. **Reject: BSOS-M9a as a framework for $\mathcal M_2$.**
The $\mathcal M_2$ leg has a different kernel. It needs its own exact combined shifted-expression matrix.

8. **Reject: M9b-CS-Cancellation as a no-go theorem.**
It is a warning for a class of standard Cauchy--Schwarz/spacing routes. It does not rule out non-conjugacy traces, direct signed estimates, or a new two-variable estimate.

9. **Reject: H13 as a proof route without a post-transform signed theorem.**
The B-process transform preserves a dual character formally, but the dual phase is Hessian-degenerate and a standard norm step can erase the character again.

10. **Reject: generic full-rank tools on $\sqrt{Xhm}$.**
The Hessian determinant is zero.

11. **Reject: toy-scale numerical checks as asymptotic evidence.**
They are regression checks only. They should not affect exponent claims.

12. **Reject: using ordinary floating sine evaluation near Fejer resonances.**
Exact rational/modular checks or high precision are needed.

## Known gaps

1. **M9 remains open.**
No bound is known in the repo for

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over $X^{1/4}\le D\le X^{1/2}$.

2. **BSOS-M9a estimate missing.**
The finite statistic

$$
\mathcal S_{\rm signed}
$$

has a derived sufficient target, but no proof or convincing numerical evidence yet.

3. **M9b exact finite matrix missing.**
A2 identified the correct combined kernel to study, but the next round must write the full matrix including actual $|\alpha_h|$, odd-$h$ restriction, diagonal size, and off-diagonal target.

4. **M9b theorem audit missing.**
The odd-$h$ restricted character-blind kernel must be compared to a precise printed divisor-type reciprocal-sum theorem, not merely to the record exponent.

5. **Li--Yang Case A ambiguity unresolved.**
The apparent $T^{-7/16}$ versus $T^{7/16}$ discrepancy must be checked against the typeset PDF or author source before any theorem-level range map is finalized.

6. **H4 final page-image verification still needed.**
The Vaaler source normalization is stable in substance, but the proof draft still needs rendered-page verification for Theorem 6, Section 7 definitions, and Theorem 18.

7. **R5 numerical regression missing.**
The product-count proof is sound, but numerical tables are still useful to catch implementation and resonance mistakes.

8. **M9 raw-versus-paired regression missing.**
The paired formulas must be tested against the raw complex definitions at nontrivial $X,D$ values.

9. **H13 uniform stationary phase incomplete.**
The stationary formula is known formally, but support-boundary, nonstationary, short-dual-length, and amplitude-uniformity estimates are not complete.

10. **H13 post-transform kernel not tested.**
No executed finite matrix test yet decides whether the dual character survives the first realistic spacing step.

11. **A3 computation gap.**
A3 has supplied formula audits and toy checks but not the larger exact/high-precision tables now needed.

## New lemmas to add

### Lemma H4-R20: finite Vaaler approximation with floor-compatible residual

Status: external theorem dependency, source-normalized in substance.

For $H\ge1$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}
\alpha_{h,H}e(ht)
+
R_H^F(t),
$$

where

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
|R_H^F(t)|
\le
\frac1{2H+2}K_H(t).
$$

The Fejer kernel is

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

At integers, $K_H(0)/(2H+2)=1/2$ covers $\psi_F(n)=-1/2$.

### Lemma R5-Full-R20: Fejer residual product-count bound

Status: proved conditional on H4.

For $X^{1/4}\le D\le X^{1/2}$ and $H\asymp D X^{-1/4}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and, for $\rho\in\{1,3\}$,

$$
\frac1H
\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

Use

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min\left(1,\Delta^2/u^2\right),&u\ne0,
\end{cases}
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4}.
$$

### Lemma Bridge-R20: conditional reduction to M9

Status: conditional proof skeleton.

If H1--H3, H4-R20, R5-Full-R20, and M9-R20 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### Lemma M9-R20: fixed-coefficient main-term target

Status: open target.

For all dyadic $D$ with $X^{1/4}\le D\le X^{1/2}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The sums must use the actual $\alpha_{h,H_D}$.

### Lemma M9-Pair-R20: paired real implementation formulas

Status: implementation lemma for real weights; must be regressed numerically.

For real $w_D$,

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}\operatorname{Im}A_h(D;X),
$$

where

$$
A_h(D;X)=\sum_d\chi_4(d)w_D(d)e(hX/d).
$$

Also

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

### Lemma BSOS-M9a-R20: sufficient signed-statistic target

Status: derived sufficient target, not an estimate.

Define

$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right)
$$

and

$$
\mathcal S_{\rm signed}
=
\sum_{\substack{d_1,d_2\in\mathcal D_{\rm odd}\\d_1\ne d_2}}
\chi_4(d_1)\chi_4(d_2)K_{d_1,d_2}^{(|\alpha|)}.
$$

Then under the frozen $|\alpha_h|$-weighted Cauchy--Schwarz normalization,

$$
|\mathcal S_{\rm signed}|\ll_\epsilon X^{1/2+\epsilon}
\Longrightarrow
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### Lemma Q1-Conjugacy-Blindness-R20

Status: proved diagnostic under stated matrix-reduction hypotheses.

Let $U=\operatorname{diag}(\chi_4(d))$ on odd denominators. If a method replaces a signed quadratic form by a unitarily invariant bound for $U^*KU$, then

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}},
$$

and the method cannot exploit the spatial character.

### Lemma H12-Cyclic-Trace-Blindness-R20

Status: proved diagnostic under stated hypotheses.

For pure cyclic trace statistics,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This does not block open-path or non-conjugacy signed statistics.

### Lemma M9b-CS-Cancellation-R20

Status: diagnostic, derived under the standard Cauchy--Schwarz-over-$h$ route.

The combined post-Cauchy--Schwarz kernel for $\mathcal M_2$ is

$$
\sum_{1\le |h|\le H_D}
|\alpha_h|
|e(h/4)-e(3h/4)|^2
e\left(\frac{hX}{4}\left(\frac1{d_1}-\frac1{d_2}\right)\right).
$$

Since the prefactor is $4$ for odd $h$ and $0$ for even $h$, this is an odd-$h$ restricted, character-blind reciprocal kernel. It is a warning for standard spacing routes, not an impossibility theorem.

### Lemma H13-Falsification-R20

Status: exploratory diagnostic.

The modulo-$4$ Poisson transform preserves a dual character and yields a dual phase of square-root type,

$$
\sqrt{hXm},
\qquad
m\asymp \frac{hX}{D^2}.
$$

But

$$
\det\nabla^2\sqrt{Xhm}=0.
$$

A useful H13 route must therefore supply a discrete signed-spacing theorem or non-conjugacy statistic, not generic full-rank stationary phase or decoupling.

## Counterexample checks to run

1. **H4 source-image check.**
Verify Vaaler Theorem 6, Section 7 definitions, and Theorem 18 directly from rendered page images or exact source transcription.

2. **R5 exact resonance check.**
For integer and near-integer $X/d$ and $(X/d+\rho)/4$, verify that

$$
K_H(0)=H+1,
\qquad
\frac1H K_H(0)=1+\frac1H=O(1),
$$

and that the proof's use of $W_\Delta(0)=1$ retains the correct implicit constant.

3. **R5 raw tables.**
Compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

and

$$
\frac1{H_D}\sum_{d\asymp D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right)
$$

for square, near-square, nonsquare, and divisor-rich $X$, normalized by $X^{1/4}$.

4. **M9 raw-versus-paired regression.**
Compute $\mathcal M_i$ from raw two-sided complex definitions and from paired real formulas. Report absolute error, relative error, and $|\mathcal M_i|/X^{1/4}$.

5. **Fixed-coefficient versus stress norms.**
Compare exact Vaaler coefficients with random/arbitrary coefficients and $L^1$ stress norms.

6. **M9a BSOS matrix test.**
Compute

$$
|\mathcal S_{\rm signed}|,
\qquad
\mathcal S_{\rm abs},
\qquad
\mathcal S_{\rm op}=|\mathcal D_{\rm odd}|\|K_{\rm off}\|_{\operatorname{op}}.
$$

If $|\mathcal S_{\rm signed}|$ is consistently comparable to the absolute or operator-norm comparators, deprioritize this Cauchy--Schwarz-over-$h$ route for $\mathcal M_1$.

7. **M9b exact combined kernel test.**
Verify numerically and symbolically that the shifted-$F$ $\rho/4$ terms cancel in the combined Cauchy--Schwarz kernel and leave the odd-$h$ restricted reciprocal kernel.

8. **M9b theorem audit.**
Identify whether any precise divisor-problem or reciprocal-sum theorem applies to the odd-$h$ restricted kernel with $|\alpha_h|$ weights at endpoint height. Record its exponent.

9. **Li--Yang Case A ambiguity check.**
Resolve the $T^{-7/16}$ versus $T^{7/16}$ issue from the typeset PDF, author source, or proof context.

10. **H13 stationary-phase uniformity.**
Treat interior stationary points, support-boundary stationary points, nonstationary integration by parts, and $M_{\rm dual}\asymp1$ separately.

11. **H13 post-transform signed test.**
Near $D\asymp X^{1/2}$, build the finite post-transform kernel with stationary amplitudes and decide whether $\chi_4(m)$ appears by diagonal conjugation or in a non-conjugacy statistic.

12. **Floating-point safety.**
Use exact rational/modular detection or high precision near Fejer resonances. Ordinary sine quotient evaluation is unsafe near integers.

## Research strategy adjustment

Continue the balanced hyperbola/Vaaler route. Do not pivot to Mellin--Perron, signed Fourier truncation, or Bessel methods as primary routes.

The residual side should now be finalized in the proof draft and treated as infrastructure:

$$
\text{H4}+\text{R5-Full}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

The active bottleneck is still M9.

Round 21 should narrow rather than broaden:

- A1 should record the proof draft and lemma-bank state conservatively.
- A2 should focus on $\mathcal M_2$, especially the exact combined post-Cauchy--Schwarz kernel and a theorem-hypothesis audit for the resulting odd-$h$ restricted reciprocal kernel.
- A3 should execute exact/high-precision computations rather than write more protocols.

Recommended allocation:

- 45% proof-draft and theorem-source finalization;
- 35% executable numerical verification;
- 20% bounded exploration, limited to M9b non-conjugacy statistics and one endpoint H13 test near $D\asymp X^{1/2}$.

## Next-round prompts by agent

### For A1

Write the Round 21 proof-draft/state update.

Objectives:

1. Insert `H4-R20`, `R5-Full-R20`, `Bridge-R20`, `M9-R20`, `M9-Pair-R20`, `BSOS-M9a-R20`, `Q1-Conjugacy-Blindness-R20`, `H12-Cyclic-Trace-Blindness-R20`, `M9b-CS-Cancellation-R20`, `H13-Falsification-R20`, and `LY-Map-R20` into the best proof draft, lemma bank, and gap register with the statuses stated above.

2. Keep `Bridge-R20` explicitly conditional:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Do not imply that M9 has been proved.

3. Quote Vaaler precisely, after page-image verification if possible:
   - Theorem 6 for $\widehat J$ and $\Phi$;
   - Section 7 definitions of $i_N,j_N,k_N$;
   - Theorem 18, especially the residual inequality.
   If the page image is still not verified, mark the citation as source-located but pending rendered-page check.

4. Write `R5-Full-R20` with all edge cases: real $X$, integer $X$, nearest-integer ties, exact resonances, shifted resonances, zero mode, dyadic weights, short blocks, both frequency signs, and logarithmic dyadic summation.

5. Freeze `M9` as the only active analytic target. Keep arbitrary coefficients and $L^1$ variants in a stress-test appendix only.

6. Record the paired formulas only as implementation lemmas for real weights and require raw-versus-paired regression.

7. Update the Li--Yang map only after resolving the Case A ambiguity; until then, state that black-box endpoint import remains unavailable.

8. Write a short comparison paragraph explaining why Mellin--Perron, signed Fourier, and Bessel smoothing remain comparison modules, not primary routes.

Exploratory allocation: formulate one candidate non-conjugacy statistic for $\mathcal M_2$, but do not promote it unless it has a finite definition, a target bound, and a route to the M9b estimate.

### For A2

Focus on $\mathcal M_2$ and keep all obstruction language conditional.

Objectives:

1. Derive the exact combined post-Cauchy--Schwarz kernel for $\mathcal M_2$ from the raw definition

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_d w_D(d)e(hX/(4d)).
$$

Do not analyze only the two separated shifted pieces. Include:
   - actual $|\alpha_{h,H_D}|$ weights;
   - the factor $|e(h/4)-e(3h/4)|^2$;
   - odd-$h$ restriction;
   - diagonal contribution;
   - exact off-diagonal statistic;
   - target size needed to imply $\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}$.

2. Determine whether the combined $\mathcal M_2$ kernel is exactly character-blind under this normalization. If yes, state it as a diagnostic for this route, not as a no-go theorem.

3. Compare the combined kernel to a precise divisor-type reciprocal-sum theorem. State the theorem hypotheses needed:
   - $|\alpha_h|$ weights;
   - odd-$h$ restriction;
   - smooth dyadic $d$ weight;
   - endpoint height $H_D\asymp D X^{-1/4}$;
   - block-level absolute values or fixed coefficients.
   If no known theorem reaches the endpoint, state the exact missing strength.

4. Recheck the diagonal blow-up claims for Cauchy--Schwarz over $d$ and post-H13 Cauchy--Schwarz. Do not promote them until the required uniform stationary-phase or exact finite-kernel estimates are written.

5. Propose one non-conjugacy statistic for $\mathcal M_2$ that could preserve information lost by the combined kernel. It must have:
   - finite definition;
   - target inequality;
   - explanation of how it would imply an M9b bound;
   - one numerical falsification test.

6. Keep `Q1-Spectral` and `H12` in bounded-scope form. Explicitly list methods not blocked: direct signed bilinear forms, open-path moments, non-conjugacy traces, residue interference, and new signed spacing theorems.

Exploratory allocation: one endpoint H13 variant is allowed only if the post-transform amplitude and exact finite kernel are written before any conclusion about sign survival.

### For A3

Execute computations and source checks. Avoid adding new prose-only diagnostics.

Objectives:

1. Produce page-image or exact-source verification for Vaaler:
   - Theorem 6 and the formula for $\widehat J$;
   - Section 7 definitions of $i_N,j_N,k_N$;
   - Theorem 18 and the residual inequality;
   - translation to $H,K_H,\Phi,\alpha_{h,H}$;
   - integer jump convention.

2. Run high-precision or exact-resonance-safe `R5` tables for $X=10^6$ and, if feasible, $X=10^8$, using:
   - square $X$;
   - near-square $X$;
   - nonsquare $X$;
   - divisor-rich $X$;
   - dyadic blocks $D\asymp X^{1/4},X^{3/8},X^{1/2}$;
   - first residual leg and shifted legs $\rho=1,3$.
   Report values normalized by $X^{1/4}$.

3. Run `M9` raw-versus-paired regression:
   - compute $\mathcal M_1,\mathcal M_2$ from raw two-sided complex sums;
   - compute them from paired real formulas;
   - report absolute difference, relative difference, and $|\mathcal M_i|/X^{1/4}$.

4. Run fixed-coefficient versus stress-norm comparisons:
   - exact Vaaler coefficients;
   - random phase coefficients with the same magnitudes;
   - arbitrary adversarial signs if computationally feasible;
   - $L^1$ stress norm.

5. Implement A2's exact weighted `BSOS-M9a` kernel, not a simplified $1/h$ proxy. Report:

$$
|\mathcal S_{\rm signed}|,
\qquad
\mathcal S_{\rm abs},
\qquad
\mathcal S_{\rm op}=|\mathcal D_{\rm odd}|\|K_{\rm off}\|_{\operatorname{op}}.
$$

Normalize ratios so the judge can decide whether BSOS is worth further work.

6. Implement the exact combined $\mathcal M_2$ kernel once A2 supplies it. Test the shift-cancellation claim numerically and symbolically.

7. Resolve the Li--Yang Case A ambiguity using the typeset PDF or source comparison. Record the exact statement, not only a derived exponent table.

8. For H13, do only one endpoint test first:
   - $D\asymp X^{1/2}$;
   - exact stationary amplitude;
   - finite post-transform kernel;
   - signed versus unsigned comparison;
   - operator-norm invariance check if the character appears by diagonal conjugation.

9. All numerical code should use high precision or exact modular/rational handling near Fejer resonances. Ordinary double-precision sine quotient evaluation is not acceptable near integers.

## Confidence

High confidence:

- The balanced hyperbola/Vaaler framework is the right current reduction framework.
- H1--H3 are stable.
- H4 is normalized correctly in substance, with final page-image citation still useful.
- R5-Full controls the fixed Fejer residual at $X^{1/4+\epsilon}$ conditional on H4.
- $\alpha_{-h,H}=\overline{\alpha_{h,H}}$ is correct.
- M9 is open and remains the active bottleneck.
- Black-box Li--Yang import fails at endpoint height.
- Q1-Spectral and H12 are correct in their stated bounded scope.

Moderate confidence:

- BSOS-M9a is a correct sufficient target under the frozen normalization.
- The paired formulas are correct for real weights, pending raw/paired regression at nontrivial sizes.
- M9b-CS-Cancellation is a serious warning for standard Cauchy--Schwarz-over-$h$ routes.
- H13 is worth one endpoint-focused finite test.

Low confidence:

- BSOS-M9a will actually be small enough to prove $\mathcal M_1$.
- The M9b obstruction rules out all viable approaches.
- H13 produces an endpoint estimate without a new signed-spacing theorem.
- Current Li--Yang/Bombieri--Iwaniec technology proves M9.
- Any route in the repo currently proves a new Gauss circle exponent.