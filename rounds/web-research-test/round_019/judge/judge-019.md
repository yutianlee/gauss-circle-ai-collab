## Selected main route

Source basis: uploaded Round 19 prompt/context and active Round 19 materials, including the judge packet.

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

This is a conditional reduction, not a proof of the Gauss circle conjectural bound. Round 19 proves no new exponent. The residual side of the finite Vaaler route is provisionally controlled by H4 plus R5-Full, conditional on final source-normalization and proof-draft bookkeeping. The active analytic bottleneck remains M9: the fixed-Vaaler-coefficient reciprocal main sums.

The accepted arithmetic identity is:

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

Blocks with $D<X^{1/4}$ should be removed before invoking Vaaler and bounded trivially by $|\psi_F|\le 1/2$, giving an acceptable contribution after dyadic summation.

The remaining open analytic target is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for all dyadic $D$ in the active range, with the actual Vaaler coefficients

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

Explicitly,

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

the second main term can also be written as

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_d w_D(d)e(hX/(4d)).
$$

No Round 19 output proves M9.

## Useful fragments by source

### From A1

A1 provides the strongest proof-draft consolidation. The useful core is the conditional bridge:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

A1's H4 normalization is the current official proof-draft statement. With $e(t)=e^{2\pi i t}$,

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin\pi(H+1)t}{\sin\pi t}\right)^2,
$$

and

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
\qquad
|R_H^F(t)|\le \frac1{2H+2}K_H(t).
$$

The source translation should be recorded with Vaaler Theorem 6, printed page 192, equation (2.28), for the coefficient function, and Vaaler Theorem 18, printed page 210, equations (7.13)--(7.17), especially (7.14), for the residual inequality. Section 7 definitions of $i_N,j_N,k_N$ occur on printed page 207. A3's page references should be corrected to this form in the proof draft.

A1 also gives the cleanest R5-Full proof. With

$$
H\asymp D X^{-1/4},
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

the Fejer bound

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right)
$$

implies

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

Define

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

Grouping by $n=md$ gives multiplicity at most $\tau(n)$, so

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
\qquad
\rho\in\{1,3\},
$$

is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing $\ell=4m-\rho$ gives $n=d\ell$ with $\ell\equiv-\rho\pmod 4$, and the congruence restriction only reduces divisor multiplicity. The same product-count proof applies.

A1's Li--Yang range map is the current guardrail. With $D=X^\delta$ and $H=X^\beta$, the Vaaler endpoint height is

$$
\beta_V=\delta-\frac14.
$$

Li--Yang's final record-exponent reduction has

$$
\beta_*=\delta-\theta^*,
\qquad
\theta^*=0.3144831759741\cdots.
$$

At $D=X^{1/2}$, this gives

$$
\beta_V=\frac14,
\qquad
\beta_*=0.1855168240259\cdots,
$$

so black-box Li--Yang import falls short of the endpoint by

$$
\theta^*-\frac14=0.0644831759741\cdots.
$$

The shifted-$F$ formulation of M9b should also be kept. Instead of treating $\chi_4(h)$ as a rough periodic weight, write

$$
e(hX/(4d))(e(h/4)-e(3h/4))
=
e\left(h\left(\frac{X}{4d}+\frac14\right)\right)
-
e\left(h\left(\frac{X}{4d}+\frac34\right)\right).
$$

After setting $d=Dz$, compare with

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\}.
$$

The derivative nondegeneracy is unchanged:

$$
F'F'''-3(F'')^2=-\frac3{8z^6}.
$$

This is a theorem-extension target, not an available theorem application.

### From A2

A2's useful contribution is the bounded-scope signed-statistic diagnostic for M9a.

Under the frozen weighted Cauchy--Schwarz normalization, define

$$
K_{d_1,d_2}^{(|\alpha|)}
=
w_D(d_1)w_D(d_2)
\sum_{1\le |h|\le H_D}
|\alpha_{h,H_D}|
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right),
$$

on the odd denominator set

$$
\mathcal D_{\rm odd}=\{d:D\le d<2D,\ 2\nmid d\}.
$$

The signed off-diagonal statistic is

$$
\mathcal S_{\rm signed}
=
\sum_{\substack{d_1,d_2\in\mathcal D_{\rm odd}\\d_1\ne d_2}}
\chi_4(d_1)\chi_4(d_2)K_{d_1,d_2}^{(|\alpha|)}.
$$

A2 correctly proves the following sufficient implication under this one fixed normalization:

$$
|\mathcal S_{\rm signed}|\ll_\epsilon X^{1/2+\epsilon}
\Longrightarrow
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is useful because it converts the vague instruction "preserve signs before norm extraction" into a finite, testable target. However, this is only for M9a. It does not yet address $\mathcal M_2$.

A2's Q1-Spectral diagnostic is correct in its stated scope. Let

$$
U=\operatorname{diag}(\chi_4(d))
$$

on $\ell^2(\mathcal D_{\rm odd})$. Then $U$ is a diagonal unitary involution and

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Thus a method that inserts $\chi_4(d)$ only through diagonal unitary conjugation and then estimates by operator norm, spectral radius, Frobenius norm, Schur/Gershgorin, absolute-value matrix, or pure cyclic trace is character-blind. This is a proved diagnostic, not a universal no-go theorem.

The cyclic trace version is similarly narrow:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

It blocks pure conjugacy-invariant cyclic trace methods, but not open-path moments, non-conjugacy traces, cross-residue statistics, or direct signed bilinear estimates.

A2's H13-Dual diagnostic should remain conditional. The statement "if the post-transform spacing step reduces to diagonal unitary conjugation, then Q1 reappears" is correct. What is not proved is that the actual H13 transform, including stationary amplitude, endpoint contributions, nonstationary terms, and boundary regimes, necessarily reduces to that form.

A2's Round 19 style is much improved: conservative, formula-level, and explicitly scoped. The next task is to extend the exact finite-statistic framework to M9b without overclaiming.

### From A3

A3's strongest contribution is formula auditing and implementation readiness.

A3 correctly records the coefficient conjugacy

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

and the exact-resonance-safe R5 kernel $W_\Delta$. A3 also gives the paired real formulas for numerical regression. For real dyadic weights,

$$
A_h(D;X)=\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

then

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}\operatorname{Im}A_h(D;X).
$$

Similarly, with

$$
B_h(D;X)=\sum_d w_D(d)e(hX/(4d)),
$$

one has

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}\chi_4(h)\operatorname{Re}B_h(D;X).
$$

These paired formulas should be treated as implementation lemmas and must be regressed numerically against the raw two-sided complex definitions.

A3's Li--Yang source audit is useful as a theorem-application guardrail. The local TeX labels for the sum $S$, derivative conditions on $F$, Case A/B height restrictions, and final target $S/H\lesssim T^{\theta^*+\epsilon}$ should be retained. But A3's table should be checked against the typeset PDF because the local TeX contains a likely ambiguity in Case A, where a condition involving $T^{-7/16}$ appears inconsistent with the later argument using $T^{7/16}$.

A3's H13 computation is useful at the formal level. The modulo-4 Poisson transform preserves a dual character, the stationary point satisfies

$$
u_0=2\sqrt{\frac{hX}{m}},
\qquad
m\asymp \frac{hX}{D^2},
$$

and the leading dual phase is

$$
\sqrt{hXm}.
$$

The continuous Hessian of

$$
\Phi(h,m)=\sqrt{Xhm}
$$

has determinant zero. This keeps the established guardrail: generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly to the dual phase.

A3 should now move from protocols to executed data. Its speculative suggestion about a nonstandard $q$-norm or sequence-space large sieve should not be added as a lemma unless an actual inequality with hypotheses is stated. As written, it is only an exploratory sentence.

### From Stage B reviews

The reviews correctly converge on three points.

First, A1's proof infrastructure should be merged into the best proof draft: H4-R19, R5-Full-R19, Bridge-R19, M9-R19, M9-Pair-R19, M9b-ShiftedF-R19, and LY-Map-R19.

Second, A2's signed-statistic diagnostics should be added only with exact hypotheses. Q1-Spectral and H12 are proved bounded-scope diagnostics. BSOS is a sufficient target for M9a under one frozen Cauchy--Schwarz normalization; it is not an estimate and not yet a full M9 framework.

Third, A3 must execute computations rather than only specify protocols: R5 tables, M9 raw-versus-paired regression, Q1 matrix checks, and BSOS falsification tests.

## Rejected or risky ideas

1. **Reject: Round 19 proves or improves a Gauss circle exponent.**
   No estimate for M9 was proved. The conditional bridge is valuable, but the unproved item is exactly the endpoint-strength main-term estimate.

2. **Reject: treating arbitrary-coefficient sums as active dependencies.**
   Arbitrary $u_h$ versions and termwise $L^1$ stress norms are useful tests. They are not the actual Vaaler main terms and should not replace M9.

3. **Reject: black-box Li--Yang import at endpoint height.**
   Li--Yang's reciprocal-sum framework is structurally relevant, but the audited height ranges do not reach $H_D\asymp D X^{-1/4}$, and the final exponent is $\theta^*>1/4$.

4. **Reject: operator-norm methods as character-aware if the character enters only by diagonal conjugation.**
   Q1-Spectral shows such methods are character-blind. Any proposed M9 proof following that pattern must be flagged.

5. **Reject: BSOS as a proved estimate.**
   A2 proves only a conditional implication to M9a. There is no proof that

$$
|\mathcal S_{\rm signed}|\ll_\epsilon X^{1/2+\epsilon}.
$$

6. **Reject: BSOS as covering M9b.**
   The current BSOS target is only for $\mathcal M_1$. The $\mathcal M_2$ leg has a different character placement or shifted-phase form and needs its own kernel.

7. **Reject: H13 as a route without a post-transform signed theorem.**
   H13 formally preserves a dual $\chi_4$ factor, but the dual phase is Hessian-degenerate and the character may again be erased by a standard Cauchy--Schwarz plus operator-norm step.

8. **Reject: generic full-rank stationary phase or decoupling on $\sqrt{Xhm}$.**
   The Hessian determinant is zero.

9. **Reject: a nonstandard $q$-norm large sieve as a lemma.**
   A3's exploratory suggestion is not an argument until a precise inequality, proof, and implication to M9 are supplied.

10. **Reject: source tables with inconsistent Vaaler page references.**
   The proof draft should use the corrected Vaaler references: Theorem 6 printed page 192, equation (2.28); Section 7 definitions printed page 207; Theorem 18 printed page 210, especially equation (7.14).

## Known gaps

1. **M9 is open.**
   The target

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

remains the sole active analytic bottleneck.

2. **M9b theorem-extension gap.**
   The shifted phase

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

has the right derivative nondegeneracy, but no theorem has been verified that allows the parameter-dependent additive shift, exact Vaaler $h$ weights, and endpoint Vaaler height.

3. **Final H4 proof-draft citation.**
   The normalization is substantially settled, but the best proof draft must quote exact Vaaler page/equation labels directly and reconcile centered versus floor-compatible sawtooth conventions.

4. **Li--Yang Case A ambiguity.**
   The local TeX source appears to contain a likely typo involving $T^{-7/16}$ versus $T^{7/16}$. The typeset PDF must be consulted before finalizing the range table.

5. **BSOS diagonal/log bookkeeping.**
   Under the frozen Cauchy--Schwarz normalization,

$$
L=\sum_{1\le |h|\le H_D}|\alpha_{h,H_D}|\asymp \log H_D,
$$

and the diagonal part is

$$
\mathcal S_{\rm diag}\asymp D\log H_D.
$$

Thus the diagonal contribution to $|\mathcal M_1|$ is about

$$
D^{1/2}\log H_D,
$$

up to constants, not $D^{1/2}(\log H_D)^{1/2}$. This is harmless under $X^\epsilon$ but must be corrected in proof-draft wording.

6. **BSOS for $\mathcal M_2$ absent.**
   A separate kernel must be defined, preferably using the shifted-$F$ formulation rather than a rough $\chi_4(h)$ weight.

7. **H13 uniform stationary phase missing.**
   The formal transform and stationary point are known, but no complete uniform lemma covers interior stationary points, boundary regimes, nonstationary integration by parts, small dual length, and amplitude errors.

8. **Numerical evidence missing.**
   Round 19 still mostly supplies protocols, not executed tables. The project now needs actual finite tests.

9. **Dyadic weight conventions.**
   Paired real formulas require real weights and symmetric positive/negative frequency pairing. Complex weights or altered cutoffs require rederivation.

10. **R5 shifted-leg positivity edge.**
   The proof should explicitly handle the positivity of $\ell=4m-\rho$ in the active range and absorb bounded small $X$ cases into constants.

## New lemmas to add

### H4-R19: finite Vaaler approximation with floor-compatible residual

Status: external theorem dependency, source-normalized.

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

The endpoint convention is covered because $V_H(n)=0$, $\psi_F(n)=-1/2$, and $K_H(0)/(2H+2)=1/2$.

### R5-Full-R19: Fejer residual product-count bound

Status: proved conditional on H4 and the standard divisor bound.

For $X^{1/4}\le D\le X^{1/2}$ and $H\asymp D X^{-1/4}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### Bridge-R19: conditional endpoint reduction

Status: proved conditional reduction.

If H1--H3, H4-R19, R5-Full-R19, and M9-R19 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This is not a solution because M9-R19 is open.

### M9-R19: fixed-coefficient main-term target

Status: open analytic target.

For $X^{1/4}\le D\le X^{1/2}$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-Pair-R19: paired real implementation formulas

Status: proved algebraic implementation lemma for real dyadic weights.

For real $w_D$,

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\operatorname{Im}
\sum_d \chi_4(d)w_D(d)e(hX/d),
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

### M9b-ShiftedF-R19: shifted-phase theorem-extension target

Status: open theorem-extension target.

Use

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\},
$$

and verify whether a Bombieri--Iwaniec/Li--Yang-type theorem permits the parameter-dependent additive shift and endpoint height.

### Q1-Spectral-R19: operator-norm character-blindness

Status: proved bounded-scope diagnostic.

If $\chi_4(d)$ enters only through $U=\operatorname{diag}(\chi_4(d))$ and the proof estimates $U^*KU$ by a unitarily invariant or absolute-value matrix norm, then the bound is character-blind.

### H12-R19: pure cyclic trace invariance

Status: proved bounded-scope diagnostic.

For pure cyclic traces,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

### BSOS-M9a-R19: signed off-diagonal sufficient target

Status: conditional implication, no estimate proved.

Under the frozen $|\alpha_h|$-weighted Cauchy--Schwarz normalization, a bound

$$
|\mathcal S_{\rm signed}|\ll_\epsilon X^{1/2+\epsilon}
$$

implies

$$
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### H13-Falsification-R19

Status: falsification checklist.

H13 is useful only if the dual character $\chi_4(m)$ survives the first spacing step in a non-conjugacy signed statistic. If it appears only as diagonal unitary conjugation before an operator-norm estimate, H13 is sign-blind at that step.

### LY-Map-R19

Status: theorem-application guardrail.

Li--Yang's theorem is structurally relevant but does not cover endpoint Vaaler height by black-box invocation.

## Counterexample checks to run

1. **H4 endpoint check.**
   At $t=n\in\mathbb Z$, verify

$$
V_H(n)=0,\qquad
\psi_F(n)=-\frac12,\qquad
K_H(0)/(2H+2)=\frac12.
$$

2. **R5 exact resonance.**
   For $d\mid X$, verify

$$
K_H(X/d)=H+1,
\qquad
\frac1H K_H(X/d)\ll 1,
$$

and that the proof uses $W_\Delta(0)=1$ rather than a singular expression.

3. **R5 shifted resonance.**
   For $X=d(4m-\rho)$, verify that $\ell=4m-\rho$ is positive in the active range and satisfies $\ell\equiv-\rho\pmod4$.

4. **Divisor-rich $X$ stress test.**
   Test R5 for square, near-square, nonsquare, and highly composite or divisor-rich $X$. The divisor-bound proof predicts no obstruction beyond $X^\epsilon$.

5. **M9 raw-versus-paired regression.**
   Compute $\mathcal M_1,\mathcal M_2$ from both raw two-sided complex formulas and paired real formulas. Values must agree for real weights.

6. **Fixed-coefficient versus stress-norm comparison.**
   Compare actual Vaaler coefficients against arbitrary coefficient and termwise $L^1$ versions. This tests whether fixed coefficients carry cancellation not captured by stress norms.

7. **Q1 matrix test.**
   Construct $K^{(|\alpha|)}$, compute $U^*KU$, and numerically verify

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

8. **BSOS falsification.**
   Compute

$$
\mathcal S_{\rm signed},\qquad
\mathcal S_{\rm abs},\qquad
|\mathcal D_{\rm odd}|\|K_{\rm off}\|_{\operatorname{op}}.
$$

If $|\mathcal S_{\rm signed}|$ is comparable to the absolute or operator-norm comparator, BSOS is unlikely to help.

9. **M9b BSOS check.**
   Build the $\mathcal M_2$ analogue of the BSOS kernel using the shifted-$F$ formulation. Do not reuse the M9a kernel.

10. **H13 endpoint test.**
   Near $D\asymp X^{1/2}$, construct the post-H13 dual kernel with stationary amplitude and compare signed versus unsigned statistics.

11. **Li--Yang typeset audit.**
   Resolve the Case A $T^{7/16}$ versus $T^{-7/16}$ ambiguity using the typeset PDF, not only the TeX source.

12. **Floating-point safety.**
   Fejer resonance tests should use exact rational/modular checks or high precision, not ordinary sine evaluation near integer arguments.

## Research strategy adjustment

Continue the balanced hyperbola/Vaaler route. The residual side is no longer the main research bottleneck; it should be finalized in the proof draft and then treated as infrastructure. The next round should concentrate on M9.

The research allocation should be:

- **A1:** proof-draft finalization and theorem-source audit.
- **A2:** exact signed-statistic development for M9b and refinement of M9a-BSOS assumptions.
- **A3:** executed computations, not protocols.

Do not pivot to Mellin--Perron, signed Fourier truncation, or Bessel methods as primary routes. Keep them as comparison modules only. Do not open new speculative routes until the current finite diagnostics have been executed.

A2's diagnostics are useful and now appropriately scoped. Keep A2 in low-temperature referee mode: exact hypotheses, no route-closing claims, and separate M9a from M9b.

A3's role should shift from algebraic auditing to computation: high-precision R5 tables, M9 paired-regression tables, Q1 norm tests, and BSOS signed-versus-unsigned ratios.

## Next-round prompts by agent

### For A1

Write a proof-draft update for the repo.

Objectives:

1. Insert H4-R19, R5-Full-R19, Bridge-R19, M9-R19, M9-Pair-R19, M9b-ShiftedF-R19, Q1-Spectral-R19, H12-R19, BSOS-M9a-R19, and LY-Map-R19 into the appropriate proof-draft, lemma-bank, and gap-register style.

2. Quote Vaaler's source exactly:
   - Theorem 6, printed page 192, equation (2.28), for $\widehat J$.
   - Section 7, printed page 207, equations (7.1)--(7.3), for $i_N,j_N,k_N$.
   - Theorem 18, printed page 210, equations (7.13)--(7.17), especially equation (7.14), for the residual bound.
   Verify the notation translation $N=H$, $k_N=K_H$, and $\widehat J_{N+1}(h)=\Phi(|h|/(H+1))$.

3. Write the R5-Full proof with all edge cases:
   - real $X$;
   - nearest-integer tie rule;
   - exact resonances;
   - shifted resonances;
   - zero Fejer mode;
   - dyadic weights;
   - short blocks $D<X^{1/4}$;
   - logarithmic dyadic summation.

4. State Bridge-R19 only conditionally. Do not imply M9 is proved.

5. Resolve the Li--Yang Case A ambiguity by checking the typeset PDF against the TeX source. Update the range map accordingly.

6. In the M9b shifted-$F$ theorem-extension section, list the exact hypotheses a theorem must satisfy:
   - $F_{\rho,D}$ allowed to depend on $D,X$ through an additive constant;
   - fixed Vaaler $h$ weights allowed;
   - endpoint height $H\asymp D X^{-1/4}$ allowed;
   - positive/negative frequency pairing allowed;
   - smooth dyadic weights allowed.

Verification tasks:

- Produce a short table showing raw Vaaler notation versus repo notation.
- Re-derive $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- Include the paired M9 formulas with the restriction "real weights only."
- Keep H13 as a falsification checklist only.

Exploratory allocation:

Use at most one short subsection to state whether signed Fourier or Mellin--Perron changes the active M9 target. Do not pivot.

### For A2

Extend the signed-statistic framework without overclaiming.

Objectives:

1. Keep the frozen $|\alpha_h|$-weighted Cauchy--Schwarz normalization for M9a, but correct the diagonal/log bookkeeping. Explicitly show:

$$
L=\sum_{1\le |h|\le H_D}|\alpha_{h,H_D}|\asymp\log H_D,
$$

$$
\mathcal S_{\rm diag}\asymp D\log H_D,
$$

and hence the diagonal contribution to $|\mathcal M_1|$ is $D^{1/2}\log H_D$ up to constants.

2. State BSOS-M9a as a conditional implication only:

$$
|\mathcal S_{\rm signed}|\ll_\epsilon X^{1/2+\epsilon}
\Longrightarrow
\mathcal M_1(D;X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Do not present this as an estimate.

3. Build the analogous finite signed-statistic framework for $\mathcal M_2$. Prefer the shifted-$F$ formulation

$$
e(hX/(4d))(e(h/4)-e(3h/4))
=
e\left(h\left(\frac{X}{4d}+\frac14\right)\right)
-
e\left(h\left(\frac{X}{4d}+\frac34\right)\right)
$$

rather than treating $\chi_4(h)$ as a rough periodic weight. Define the exact kernel, diagonal term, signed off-diagonal term, and sufficient target.

4. Clarify which methods Q1-Spectral blocks and which it does not. Keep the scope narrow:
   - blocks operator norm, Frobenius norm, Schur/Gershgorin, absolute-value matrix, pure cyclic trace after diagonal conjugation;
   - does not block open-path statistics, non-conjugacy forms, residue-sensitive bilinear forms, or direct signed estimates.

5. For H13, give only a conditional diagnostic unless you write the exact post-transform kernel with stationary amplitudes. Separate formal transform, stationary approximation, and spacing-kernel stage.

Verification tasks:

- Provide finite matrix definitions that A3 can implement directly for M9a and M9b.
- Specify the normalizations of $\mathcal S_{\rm signed}$, $\mathcal S_{\rm abs}$, and $\mathcal S_{\rm op}$.
- State exact falsification thresholds: what ratio would make BSOS look ineffective.

Exploratory allocation:

Use at most 20% of the response on H13 endpoint testing. The output must produce an executable finite test, not a route-closing claim.

### For A3

Execute the numerical and source-verification tasks. Move from protocols to data.

Objectives:

1. Produce a Vaaler source table from the PDF with exact printed page/equation references:
   - Theorem 6, page 192, equation (2.28);
   - Section 7 definitions, page 207, equations (7.1)--(7.3);
   - Theorem 18, page 210, equations (7.13)--(7.17), especially (7.14).
   Correct any earlier page-reference mismatch.

2. Implement R5-Full numerical tests:
   - $X=10^6$ and $X=10^8$ if feasible;
   - $D\asymp X^{1/4},X^{3/8},X^{1/2}$;
   - square, near-square, nonsquare, and divisor-rich $X$;
   - both first residual leg and shifted $\rho=1,3$ legs.
   Use exact rational/modular checks or high precision near Fejer resonances. Report normalized values divided by $X^{1/4}$ and by $X^{1/4}\log X$.

3. Implement M9 raw-versus-paired regression:
   - compute $\mathcal M_1,\mathcal M_2$ from raw two-sided complex definitions;
   - compute the paired real formulas;
   - report absolute and relative differences;
   - report $|\mathcal M_i|/X^{1/4}$.

4. Implement fixed-coefficient versus stress-norm comparison:
   - actual Vaaler coefficients;
   - random/adversarial coefficient tests with the same size profile;
   - termwise $L^1$ comparator.
   This is only diagnostic; do not infer a theorem.

5. Implement Q1-Spectral matrix tests:
   - build $K^{(|\alpha|)}$ for small odd denominator sets;
   - build $U=\operatorname{diag}(\chi_4(d))$;
   - verify $\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}$ numerically.

6. Implement BSOS falsification tests once A2 supplies the exact M9a and M9b kernels:
   - compute $\mathcal S_{\rm signed}$;
   - compute $\mathcal S_{\rm abs}$;
   - compute $\mathcal S_{\rm op}$;
   - report ratios.

7. Optional H13 endpoint test:
   - only near $D\asymp X^{1/2}$;
   - include stationary amplitude;
   - compare signed and unsigned dual statistics;
   - report whether diagonal-unitary blindness appears after the first spacing step.

Verification rules:

- Use high precision for Fejer kernels near integers.
- Use exact modular detection for exact resonances.
- Preserve raw data tables in a form that can be committed.
- Do not introduce new theoretical routes unless supported by a precise inequality.

Exploratory allocation:

At most one small endpoint H13 computation. The main deliverable is executed data for R5, M9, Q1, and BSOS.

## Confidence

High confidence:

- H1--H3 are the stable arithmetic foundation.
- H4 is correctly source-normalized up to final proof-draft transcription.
- The endpoint convention $\psi_F(n)=-1/2$ is covered by the Fejer majorant.
- R5-Full controls the fixed Fejer residual conditional on H4.
- The correct Vaaler coefficient conjugacy is $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
- M9 is the sole active analytic bottleneck.
- Q1-Spectral and H12 are valid bounded-scope diagnostics.
- Black-box Li--Yang import fails at endpoint Vaaler height.

Moderate confidence:

- The paired M9 formulas are correct for real weights, pending numerical regression.
- The shifted-$F$ formulation is the right way to compare M9b to reciprocal-sum theorems.
- BSOS-M9a is a useful finite target and falsification statistic.
- H13 is worth one endpoint-focused finite test.

Low confidence:

- Current technology can prove M9 without a genuinely new signed spacing or endpoint-strength estimate.
- BSOS will be small enough to imply M9a.
- H13 will provide a viable route after the first spacing step.

No new Gauss circle exponent has been proved in Round 19.