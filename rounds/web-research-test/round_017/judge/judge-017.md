## Summary

Round 17 is a proof-infrastructure, formula-audit, and diagnostic round. It does **not** prove a new Gauss circle exponent. Source basis: uploaded Round 17 packet and reviews in `judge_17.md` plus A1/A2/A3 Round 17 outputs.

The selected route remains the balanced arithmetic hyperbola/Vaaler framework:

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

The current conservative bridge is still:

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

This is a conditional reduction, not a proof of the conjectural Gauss circle bound, because `M9` remains open. The residual side is provisionally controlled by `H4 + R5-Full`. The active analytic bottleneck is now cleanly isolated as `M9`: the fixed-Vaaler-coefficient reciprocal main sums with the actual coefficients $\alpha_{h,H_D}$, not arbitrary coefficient stress tests.

Round 17 made useful checkable progress:

1. `H4` is now essentially source-normalized against Vaaler's finite periodic sawtooth approximation, with the Fejer residual constant and integer jump convention identified.
2. `R5-Full` has a corrected exact-resonance-safe product-count proof using the piecewise weight $W_\Delta$.
3. The correct coefficient conjugacy is fixed as $\alpha_{-h,H}=\overline{\alpha_{h,H}}$.
4. The paired real formulas for `M9` are now usable computational targets.
5. `Q1-Spectral-R17` and `H12-R17` are valid bounded-scope diagnostics for operator-norm and pure cyclic-trace character blindness.
6. `H13` remains only a falsifiable exploratory transform: it preserves a dual character but has a Hessian-degenerate dual phase and may re-enter diagonal-unitary character blindness after a standard Cauchy--Schwarz step.
7. Black-box Li--Yang/Bombieri--Iwaniec import still fails at the endpoint Vaaler height.

## Selected main route

Keep the balanced arithmetic hyperbola/Vaaler route.

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

For dyadic blocks in the active range

$$
X^{1/4}\le D\le X^{1/2},
$$

use local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ should be removed before Vaaler is invoked and bounded directly by $|\psi_F|\le 1/2$, giving an acceptable $O(X^{1/4+\epsilon})$ contribution after dyadic summation.

The finite Vaaler coefficient should be frozen as

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1.
$$

The official remaining `M9` targets are:

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

The required endpoint-strength estimate is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over $X^{1/4}\le D\le X^{1/2}$. No Round 17 output proves this.

## Useful fragments by source

### From A1

A1 supplied the strongest proof-infrastructure synthesis. The most useful items are:

1. **H4 source-normalization.** Vaaler's notation is mapped to repo notation as $N\leftrightarrow H$, $k_N\leftrightarrow K_H$, and $\widehat J_{N+1}(h)\leftrightarrow\Phi(|h|/(H+1))$. The residual inequality is the periodic sawtooth inequality

$$
|\psi*j_N(x)-\psi(x)|\le (2N+2)^{-1}k_N(x),
$$

giving repo residual constant $(2H+2)^{-1}$.

2. **Integer jump convention.** Vaaler's centered sawtooth has value $0$ at integers, while the arithmetic identity uses $\psi_F(n)=-1/2$. This is covered exactly because

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

3. **R5-Full proof architecture.** The Fejer residual is controlled by product counting, not by arbitrary reciprocal-sum estimates. The key bound is

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right),
$$

hence

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

4. **Li--Yang subrange map.** For $D=X^\delta$ and $H=X^\beta$, the Vaaler endpoint height is

$$
\beta_V=\delta-\frac14.
$$

The currently audited Li--Yang ranges remain below this endpoint; at $D=X^{1/2}$, the endpoint is $\beta_V=1/4$, while the audited Case A gives $33/164\approx0.2012$, Case B gives at most $1/6$ in the binding branch, and the final $\theta^*$ range gives $\beta_*=1/2-\theta^*\approx0.1855$. Thus Li--Yang is structurally relevant but not a black-box proof of `M9`.

### From A2

A2's strongest contribution is the bounded-scope character-blindness diagnostic.

Let

$$
\mathcal D_{\rm odd}=\{d:D\le d<2D,\ 2\nmid d\},
\qquad
\mathcal V_D=\ell^2(\mathcal D_{\rm odd}),
$$

and define

$$
U=\operatorname{diag}(\chi_4(d)).
$$

On odd denominators, $U$ is a diagonal unitary involution. Therefore for every matrix $K$,

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

This proves that any method which inserts $\chi_4(d)$ only by diagonal conjugation and then estimates by operator norm, spectral radius, Frobenius norm, Schur/Gershgorin, absolute-value matrices, or pure cyclic trace is character-blind. This is a diagnostic, not a universal no-go theorem.

A2 also supplied the narrow trace diagnostic:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This blocks pure conjugacy-invariant cyclic trace statistics from seeing $\chi_4$, but it does not block open-path moments, non-conjugacy signed forms, cross-residue statistics, or bilinear estimates that keep signs before norm extraction.

A2's `BSOS` statistic is useful only as a falsification metric at this stage. It is not yet a lemma because its exact implication to `M9a` has not been derived under one fixed Cauchy--Schwarz normalization.

### From A3

A3's strongest contribution is formula auditing.

The coefficient conjugacy is:

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

This is now a stable algebraic fact. Any computation using $\alpha_{-h,H}=-\overline{\alpha_{h,H}}$ is wrong.

A3 also corrected the exact-resonance handling in `R5` by replacing any singular or malformed expression with

$$
W_\Delta(u)
=
\begin{cases}
1,&u=0,\\
\min\left(1,\Delta^2/u^2\right),&u\ne0,
\end{cases}
\qquad
\Delta=\frac{D}{H}\asymp X^{1/4}.
$$

This is the right product-counting cap for exact Fejer spikes.

A3's H13 stationary-phase constants are also useful. For

$$
\phi_\xi(u)=\frac{hX}{u}-\frac{\xi u}{4},
$$

the stationary point occurs for $\xi=-m<0$ with

$$
u_0=2\sqrt{\frac{hX}{m}},
$$

and the leading phase is

$$
\phi_{-m}(u_0)=\sqrt{hXm}.
$$

The active dual length is

$$
m\asymp \frac{hX}{D^2}.
$$

At the endpoint $D\asymp X^{1/2}$ and maximal $h\asymp X^{1/4}$, this gives $m\asymp X^{1/4}$, which is the only naturally balanced H13 regime.

A3 also independently records that

$$
\det\nabla^2\sqrt{Xhm}=0,
$$

so H13 cannot be justified by generic full-rank two-dimensional stationary phase or full-rank decoupling.

## Rejected or risky ideas

1. **Reject any claim of a new Gauss circle exponent.** Round 17 proves no estimate for `M9`, so it proves no new upper bound for $P(X)$.

2. **Reject treating the bridge theorem as a proof.** The implication

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

is useful only as a conditional reduction. The unproved item is exactly `M9`.

3. **Reject arbitrary-coefficient versions as active dependencies.** Arbitrary-coefficient `H5a/H5b` and $L^1$ stress norms remain diagnostics only. The actual Vaaler reduction requires fixed coefficients $\alpha_{h,H_D}$.

4. **Reject scalar Vaaler residual arguments.** The residual must be handled through the Fejer majorant and product counting. The residual is provisionally controlled by `R5-Full`, not by an informal scalar $D/H$ estimate alone.

5. **Reject black-box Li--Yang import.** Phase compatibility is not theorem applicability. The audited height restrictions do not cover endpoint Vaaler height.

6. **Reject generic full-rank stationary phase or decoupling on H13.** The H13 dual phase has zero Hessian determinant.

7. **Reject route-closing language for Q1-Spectral.** Q1-Spectral blocks only methods that pass to unitarily invariant or absolute-value matrix bounds after diagonal conjugation. It does not block direct signed bilinear forms, residue interference, open-path moments, or a new signed spacing theorem.

8. **Reject `BSOS` as a proved lemma.** It is currently a finite falsification statistic. It needs one fixed normalization, a target bound, and an implication to `M9a`.

9. **Reject tiny finite examples as asymptotic evidence.** Small $X=100$-scale checks are useful for formula regression only. They do not validate asymptotic estimates by themselves.

10. **Reject the claim that the paired $\mathcal M_2$ formula with $\Re B_h$ is wrong.** A direct recomputation confirms the $\Re B_h$ formula below. Still, it should be regression-tested numerically against the raw two-sided complex formula.

For $h>0$, write

$$
\alpha_{h,H}=\frac{i}{2\pi h}\Phi\left(\frac{h}{H+1}\right),
\qquad
B_h=\sum_d w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h)
$$

for odd $h$, and since $\chi_4(-h)=-\chi_4(h)$, pairing $h$ and $-h$ gives

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}\chi_4(h)\Re B_h(D;X).
$$

Thus the real-part form is algebraically consistent under the stated convention. The raw complex form should remain the authoritative definition if any convention is changed.

## Known gaps

1. **`M9` is open.** This is the only active analytic bottleneck in the selected route.

2. **H4 proof-draft citation still needs exact transcription.** The theorem, page, equation numbers, and notation map must be copied into the proof draft from Vaaler's original paper, even though the mathematical normalization is now stable.

3. **R5-Full must be inserted into the proof draft.** The proof should explicitly include exact resonances, real $X$, nearest-integer tie rules, shifted legs, positivity of $4m-\rho$, zero mode, dyadic weights, short blocks, both frequency signs, and logarithmic losses.

4. **M9b shifted-$F$ theorem compatibility is unproved.** The preferred comparison phase is

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\}.
$$

Its derivative determinant is fine, but theorem applicability at endpoint height with $D,X$-dependent additive shifts and Vaaler $h$-weights remains open.

5. **Q1-Spectral has not yet been applied to the exact M9 proof attempt.** The actual first Cauchy--Schwarz or spacing kernel must be written before declaring a proposed method character-blind.

6. **H13 lacks a uniform transform lemma.** The stationary, nonstationary, boundary, and short-dual-length regimes must be stated separately. One-integral stationary phase must not be promoted into a double-sum estimate.

7. **H13-Dual remains conditional.** It becomes Q1-like only if the post-transform first step places $\chi_4(m)$ into diagonal unitary conjugation and then takes an operator norm or similar invariant bound.

8. **BSOS has no implication theorem.** Its target normalization must be derived from one fixed Cauchy--Schwarz setup; otherwise it remains a diagnostic.

9. **Executed numerical data are still missing.** Round 17 supplies formulas and protocols but not high-precision tables.

10. **Bessel calibration remains secondary.** The Poisson--Bessel sanity route should remain in the repository, but it is not the selected active route for `M9`.

## New lemmas to add

### H4-R17. Finite Vaaler approximation with floor-compatible residual

**Status:** external theorem dependency, source-normalized up to final proof-draft transcription.

For $H\ge1$ and all real $t$,

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

Here

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac1{H+1}
\left(\frac{\sin\pi(H+1)t}{\sin\pi t}\right)^2.
$$

At integers, the half-jump is covered exactly by $K_H(0)/(2H+2)=1/2$.

### CCoef-R17. Vaaler coefficient conjugacy

**Status:** proved algebraic lemma.

For $1\le h\le H$,

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

### R5-Full-R17. Fejer residual product-count bound

**Status:** proved conditional on H4.

Let

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H\asymp D X^{-1/4},
\qquad
\Delta=D/H\asymp X^{1/4}.
$$

Then for bounded dyadic weights,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and, for $\rho\in\{1,3\}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The proof uses

$$
W_\Delta(u)
=
\begin{cases}
1,&u=0,\\
\min(1,\Delta^2/u^2),&u\ne0,
\end{cases}
$$

and multiplicity at most $\tau(n)$ after grouping by $n=md$ or $n=d(4m-\rho)$.

### Bridge-R17. Conditional endpoint reduction

**Status:** conditional theorem.

If H1--H3, H4-R17, R5-Full-R17, and M9 hold, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

### M9-Pair-R17. Paired real formulas

**Status:** proved algebraic reformulation for real dyadic weights.

Let

$$
A_h(D;X)=\sum_d\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
B_h(D;X)=\sum_d w_D(d)e(hX/(4d)).
$$

Then

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\Im A_h(D;X),
$$

and

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\Re B_h(D;X).
$$

If weights are complex or conventions change, revert to the raw two-sided complex definitions.

### M9b-Shifted-F-R17

**Status:** open theorem-extension target.

The second main term can be compared with reciprocal-sum theorems through

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\}.
$$

Its derivative determinant is

$$
F_{\rho,D}'F_{\rho,D}'''-3(F_{\rho,D}'')^2
=
-\frac3{8z^6}.
$$

The gap is theorem applicability at endpoint height with parameter-dependent additive shift and fixed Vaaler $h$ weights.

### LY-Map-R17

**Status:** theorem-application guardrail.

For $D=X^\delta$, $1/4\le\delta\le1/2$, the endpoint Vaaler height exponent is

$$
\beta_V=\delta-\frac14.
$$

The currently audited Li--Yang ranges give lower height exponents:

$$
\beta_A=\delta-\frac{49}{164},
$$

$$
\beta_{B1}=\frac{35}{69}\delta-\frac{2}{23},
$$

$$
\beta_{B2}=\frac32\delta-\frac12,
$$

and

$$
\beta_*=\delta-\theta^*.
$$

These do not cover the endpoint Vaaler height. Li--Yang remains a comparison template, not an available endpoint theorem.

### Q1-Spectral-R17

**Status:** proved bounded-scope diagnostic.

If the character enters as $U=\operatorname{diag}(\chi_4(d))$ and the proof estimates $U^*KU$ by an operator norm or related unitarily invariant/absolute-value bound, then the character is not used:

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

### H12-R17

**Status:** proved bounded-scope diagnostic.

For pure cyclic traces,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

This does not block open-path or non-conjugacy statistics.

### H13-Dual-R17

**Status:** conditional diagnostic.

After B-process-first, the dual sum has active length

$$
m\asymp \frac{hX}{D^2}
$$

and leading phase

$$
\sqrt{hXm}.
$$

If the next step inserts $\chi_4(m)$ only through diagonal conjugation and takes an operator norm, Q1-Spectral reappears. This does not prove H13 useless; it specifies a falsification test.

### BSOS-R17

**Status:** falsification metric, not a lemma.

A possible signed off-diagonal statistic is

$$
\mathcal S_{\rm signed}
=
\sum_{d_1\ne d_2}
\chi_4(d_1)\chi_4(d_2)K_{d_1,d_2}.
$$

It should be compared with an unsigned form, an absolute majorant, and an operator-norm comparator. Its target normalization and implication to `M9a` are not yet proved.

## Counterexample checks to run

1. **H4 citation check.** Quote Vaaler's theorem/page/equation labels and verify $\Phi$, coefficient sign, Fejer kernel normalization, residual constant, and integer convention.

2. **H4 jump regression.** Verify

$$
V_H(n)=0,
\qquad
K_H(0)=H+1,
\qquad
K_H(0)/(2H+2)=1/2.
$$

3. **Coefficient pairing regression.** Compute $\mathcal M_1,\mathcal M_2$ using both raw two-sided complex formulas and paired real formulas. They must agree.

4. **R5 exact resonance tests.** Evaluate cases with

$$
X/d\in\mathbb Z
$$

and

$$
(X/d+\rho)/4\in\mathbb Z,
\qquad \rho\in\{1,3\}.
$$

Confirm the proof uses $W_\Delta(0)=1$.

5. **R5 raw tables.** Compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

and

$$
\frac1{H_D}\sum_{d\asymp D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right)
$$

for square, near-square, nonsquare, and divisor-rich $X$, normalized by $X^{1/4}$.

6. **M9 fixed-coefficient tables.** For $D=X^\delta$ with $\delta=1/4,3/8,1/2$, compute

$$
|\mathcal M_i(D;X)|/X^{1/4}.
$$

Compare exact Vaaler coefficients with arbitrary-coefficient and $L^1$ stress norms.

7. **Actual M9a Q1 test.** Construct the natural post-Cauchy--Schwarz M9a kernel and verify whether the character appears only as $U^*KU$.

8. **BSOS normalization test.** Derive the precise target for $\mathcal S_{\rm signed}$ from one fixed Cauchy--Schwarz inequality. Do not use an unproved $H_D^{-1}$ factor.

9. **Actual post-H13 test.** Build the endpoint H13 kernel with stationary amplitudes and supports. Decide whether $\chi_4(m)$ appears by diagonal unitary conjugation or in a non-conjugacy statistic.

10. **H13 uniform stationary phase.** Treat separately interior stationary points, support-boundary stationary points, nonstationary integration by parts, and $M_{\rm dual}\asymp1$.

11. **Li--Yang shifted-$F$ audit.** Check whether the theorem permits

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

with uniform constants, endpoint height, and Vaaler $h$ weights.

## Research strategy adjustment

Continue the balanced hyperbola/Vaaler route. Do not pivot.

The residual side should now be treated as provisionally cleared by `H4 + R5-Full`, pending final proof-draft transcription and numerical regression. The next mathematical work should concentrate on `M9`.

Allocation for the next round:

- **60% proof-draft consolidation:** final H4 source table, R5-Full proof, bridge theorem, and exact M9 definitions.
- **25% computation:** high-precision R5 tables, paired M9 tables, Q1-Spectral matrices, and BSOS/absolute-majorant comparisons.
- **15% exploration:** one endpoint H13/BSOS signed-vs-unsigned test near $D\asymp X^{1/2}$.

Assessment of A2: useful diagnostics, especially Q1-Spectral and H12. Risk remains in overbroad language around H13-Dual and in the unproved BSOS target normalization. A2 should produce one precise finite signed statistic with a derived target or explicitly label it as only a falsification metric.

Assessment of A3: useful formula audit, especially corrected R5 kernel, H13 phase constants, Li--Yang subrange map, and M9 paired forms. A3 must now move from protocols and toy checks to executed high-precision or exact tables and scripts. Tiny examples should be labeled as formula checks, not asymptotic evidence.

Assessment of A1: strongest proof-infrastructure consolidation. A1 should now turn the conditional bridge, H4, R5-Full, and M9 definitions into proof-draft text and keep all claims conservative.

## Next-round prompts by agent

### For A1

Produce the Round 18 proof-draft synthesis.

Objectives:

1. **Finalize H4 in proof-draft form.**
   Quote Vaaler's exact theorem/page/equation labels for Theorem 18 and Theorem 6. Translate $N,j_N,k_N,\widehat J_{N+1}$ into $H,V_H,K_H,\Phi,\alpha_{h,H}$. State the centered-to-floor-compatible convention at integers.

2. **Insert R5-Full as a completed lemma.**
   Include first leg, shifted legs $\rho=1,3$, real and integer $X$, nearest-integer tie rules, exact resonance $W_\Delta(0)=1$, congruence $\ell=4m-\rho$, positivity of $\ell$, zero Fejer mode, both signs of frequency, dyadic weights, short blocks, and logarithmic losses.

3. **State Bridge-R18 only conditionally.**
   Use exactly:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Do not imply `M9` has been proved.

4. **Freeze M9.**
   Give raw complex definitions of $\mathcal M_1,\mathcal M_2$ with actual $\alpha_{h,H_D}$ only. Put arbitrary-coefficient variants in a stress-test appendix.

5. **Record paired formulas with a regression warning.**
   Include the paired real forms for real dyadic weights and state that all computations must be checked against the raw two-sided complex definitions.

6. **Complete the M9b shifted-$F$ theorem-extension statement.**
   List exact hypotheses needed: parameter-dependent additive shift, derivative constants, smooth weight class, Vaaler $h$ coefficient variation, endpoint height, and positive/negative frequency pairing.

7. **Produce a Li--Yang covered/uncovered range table.**
   Use $D=X^\delta$, $H=X^\beta$ and compare $\beta_V,\beta_A,\beta_{B1},\beta_{B2},\beta_*$. Identify the uncovered high-frequency endpoint range.

Exploratory allocation: write a one-page H13 falsification checklist that begins from the exact post-transform kernel and specifies which first step would reduce the dual character to Q1-Spectral diagonal conjugation.

### For A2

Produce a proof-draft-ready signed-diagnostic packet with no broad route-closing language.

Objectives:

1. **Freeze one Cauchy--Schwarz normalization for M9a.**
   Choose either weighted or unweighted Cauchy--Schwarz. Write the exact resulting kernel $K_{d_1,d_2}$, including coefficient weights.

2. **Derive the exact BSOS target.**
   Define $\mathcal S_{\rm signed}$, $\mathcal S_{\rm abs}$, and $\mathcal S_{\rm op}$. Prove what bound on $\mathcal S_{\rm signed}$ would imply $\mathcal M_1(D;X)\ll X^{1/4+\epsilon}$, or explicitly state that no implication has been proved.

3. **State Q1-Spectral only for the exact kernel.**
   Prove whether the chosen kernel has the form $U^*KU$ with $U=\operatorname{diag}(\chi_4(d))$. List exactly which methods this blocks and what it does not block.

4. **Write H12 narrowly.**
   Keep only the pure cyclic trace identity and explicitly exclude open-path and non-conjugacy statistics from the conclusion.

5. **Repair H13-Dual as a conditional test.**
   Start from the actual post-H13 kernel near $D\asymp X^{1/2}$, include stationary amplitudes and support. State whether $\chi_4(m)$ appears only by diagonal unitary conjugation after the first proposed step.

Exploratory allocation: give one finite signed-vs-unsigned test plan for the M9a kernel or the H13 endpoint kernel. Do not introduce a new broad route.

### For A3

Prioritize executed computations, scripts, and exact citations over additional exposition.

Objectives:

1. **H4 source table.**
   Produce a table with Vaaler theorem/equation/page, Vaaler object, repo object, coefficient sign, residual constant, and jump convention. Use the uploaded Vaaler PDF directly.

2. **R5 raw-form tables.**
   With exact or high-precision arithmetic, compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

and

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}\left(\frac{X/d+\rho}{4}\right),
\qquad \rho\in\{1,3\},
$$

for square, near-square, nonsquare, and divisor-rich $X$ and for $D\asymp X^{1/4},X^{3/8},X^{1/2}$. Report normalization by $X^{1/4}$.

3. **M9 fixed-coefficient tables.**
   Compute $\mathcal M_1,\mathcal M_2$ using exact Vaaler coefficients. Report $|\mathcal M_i|/X^{1/4}$ and compare with arbitrary-coefficient and $L^1$ stress norms.

4. **Paired-form regression.**
   Verify the paired real formulas against the raw two-sided complex definitions for multiple $X,D,H_D$.

5. **Q1-Spectral test.**
   Build the actual M9a post-Cauchy--Schwarz matrix and verify $\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}$ numerically.

6. **BSOS/absolute-majorant test.**
   Once A2 fixes the statistic and normalization, compute signed, unsigned, absolute-majorant, and operator-norm comparators.

7. **H13 endpoint matrix.**
   Construct the post-H13 matrix near $D\asymp X^{1/2}$ including stationary amplitudes and support. Compare signed and unsigned dual-character forms.

8. **Li--Yang line audit.**
   Record exact TeX labels or line references for $S$, Case A, Case B, Theorem 4.3, final reduction, allowed weights, and allowed $F$. Test the shifted-$F$ formulation against the actual hypotheses.

## Confidence

High confidence in the selected balanced hyperbola/Vaaler route as the current reduction framework.

High confidence that Round 17 proves no new Gauss circle exponent.

High confidence that H1--H3 remain the exact arithmetic foundation.

High confidence that H4 is mathematically normalized correctly, with final proof-draft citation still required.

High confidence that R5-Full controls the Fejer residual at $X^{1/4+\epsilon}$ conditional on H4.

High confidence that `M9` fixed-coefficient sums are the active analytic bottleneck.

High confidence that $\alpha_{-h,H}=\overline{\alpha_{h,H}}$ is the correct coefficient conjugacy.

High confidence that the paired $\mathcal M_1$ and $\mathcal M_2$ formulas above are correct under real-weight conventions, but they should be regression-tested against raw complex definitions.

High confidence that black-box Li--Yang/Bombieri--Iwaniec technology does not cover endpoint Vaaler height.

High confidence in Q1-Spectral and H12 as bounded-scope diagnostics.

Moderate confidence in H13-Dual as a conditional obstruction if the first post-transform step is Cauchy--Schwarz plus operator norm.

Low-to-moderate confidence in BSOS until its target normalization is derived.

Low confidence that H13, BSOS/CRI, signed Fourier truncation, Mellin--Perron, or current printed Li--Yang technology proves `M9` without a genuinely new signed or endpoint-strength estimate.