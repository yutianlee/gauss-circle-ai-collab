## Summary

Source basis: Round 16 Stage A/B material in the uploaded judge packet, including A1/A2/A3 outputs and cross-reviews. The retrieved Round 16 packet says M9 remains the active bottleneck and no new Gauss circle exponent was proved; it also records the conditional bridge
$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The same packet records the next-round requirement to keep the bridge conditional, correct the R5 and H13 formulas, and treat M9 as the sole active analytic bottleneck. External source checks remain consistent with the literature anchors: Vaaler's 1985 paper is the relevant finite sawtooth/Fejer source, and Li--Yang's arXiv paper states a Bombieri--Iwaniec/first-spacing/Huxley-second-spacing improvement with exponent $\theta^*=0.314483\ldots$, not the conjectural $\theta=1/4$.

Round 16 is best recorded as a **formula-audit and verification round**, not an exponent-improvement round. The residual side of the Vaaler route remains provisionally controlled by H4 plus R5-Full, after correcting the exact-resonance handling. The active mathematical problem is still M9: fixed-Vaaler-coefficient reciprocal main sums.

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

The accepted arithmetic identity remains

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

For dyadic blocks

$$
X^{1/4}\le D\le X^{1/2},
$$

use the local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Blocks with $D<X^{1/4}$ should still be removed before Vaaler expansion and bounded trivially using $|\psi_F|\le 1/2$.

The official conditional bridge is:

$$
\boxed{
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
}
$$

This is not a proof of the Gauss circle conjecture, because M9 is open.

The active M9 target uses the actual Vaaler coefficients

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
\qquad
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
0<u<1.
$$

Define

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_{d\asymp D}
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

one may equivalently write

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\asymp D}
w_D(d)e(hX/(4d)).
$$

The open endpoint target is

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly for $X^{1/4}\le D\le X^{1/2}$.

## Useful fragments by source

### From A1

A1 supplied the strongest proof-infrastructure synthesis. The main useful item is the conditional bridge theorem and the insistence that arbitrary-coefficient versions remain stress tests, not active dependencies.

A1 also gives the correct positive/negative frequency pairing. Since

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}},
$$

not $-\overline{\alpha_{h,H}}$, the paired real forms should be frozen for numerical work. If

$$
A_h(D;X)=\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
$$

then

$$
\mathcal M_1(D;X)
=
\frac4\pi
\sum_{1\le h\le H_D}
\frac{\Phi(h/(H_D+1))}{h}
\Im A_h(D;X).
$$

If

$$
B_h(D;X)=\sum_{d\asymp D}w_D(d)e(hX/(4d)),
$$

then

$$
\mathcal M_2(D;X)
=
-\frac8\pi
\sum_{\substack{1\le h\le H_D\\2\nmid h}}
\frac{\Phi(h/(H_D+1))}{h}
\chi_4(h)\Re B_h(D;X).
$$

This paired form is now the preferred implementation target for M9 computations.

A1's shifted-$F$ formulation of M9b is also important. Instead of treating $\chi_4(h)$ as a nonsmooth periodic $h$-weight, use

$$
e(hX/(4d))(e(h/4)-e(3h/4))
=
e\left(h\left(\frac{X}{4d}+\frac14\right)\right)
-
e\left(h\left(\frac{X}{4d}+\frac34\right)\right).
$$

After writing $d=Dz$, compare with Li--Yang-type phases using

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\}.
$$

The derivative nondegeneracy is unchanged:

$$
F'F'''-3(F'')^2=-\frac3{8z^6}.
$$

This is a theorem-comparison formulation, not a theorem application.

### From A2

A2's main useful contribution is the bounded-scope Q1-Spectral diagnostic. On

$$
\mathcal V_D=\ell^2(\{d:D\le d<2D,\ 2\nmid d\}),
$$

with

$$
U=\operatorname{diag}(\chi_4(d)),
$$

one has $U^*U=I$ and hence

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Therefore any M9a method that inserts $\chi_4(d)$ only through diagonal unitary conjugation and then estimates by operator norm, spectral radius, Schur/Gershgorin, Frobenius norm, cyclic trace, or absolute-value matrix is character-blind. This is a proved diagnostic under its stated hypothesis. It is not a global obstruction to signed bilinear or open-path methods.

The trace version is similarly useful but narrow:

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m)
$$

for pure conjugacy-invariant cyclic traces. It does not block non-conjugacy signed forms, open-path moments, cross-residue moments, or bilinear estimates that keep signs before norm extraction.

A2's H13 and BSOS material should be retained only as falsification infrastructure. The H13 claim that post-transform Cauchy--Schwarz necessarily recreates Q1 must be downgraded until the actual post-H13 kernel and amplitudes are written. BSOS is not a lemma yet; it is a candidate statistic requiring a finite definition, a target inequality, and an implication to M9 or a falsification criterion.

### From A3

A3's useful contribution is formula auditing. The following items should be kept:

1. The coefficient conjugacy is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

2. The integer jump is covered exactly. The Vaaler polynomial has centered value $0$ at integers, while $\psi_F(n)=-1/2$, and

$$
K_H(0)=H+1,
\qquad
\frac{K_H(0)}{2H+2}=\frac12.
$$

3. The Li--Yang endpoint mismatch remains a valid theorem-application guardrail. At the raw endpoint block

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$

the quoted Li--Yang ranges fall short of $X^{1/4}$; hence the theorem cannot be imported as a black box. Round 16 explicitly asks for a subrange table and shifted-$F$ uniformity audit rather than a phase-shape assertion.

4. H13 has the correct dual length

$$
M_{\rm dual}\asymp \frac{hX}{D^2}.
$$

Under the convention

$$
\phi_n(u)=hX/u-nu/4,
$$

with $n=-m$, the stationary point is

$$
u_0=2\sqrt{\frac{hX}{m}},
$$

and the phase value is

$$
\phi_{-m}(u_0)=\sqrt{hXm}.
$$

The earlier $2\sqrt{hXm}$ normalization is incorrect under this convention.

A3's weak point is that most computations remain toy-scale or protocol-level. Round 17 should require actual high-precision tables, not more prose protocols.

## Rejected or risky ideas

1. **Reject any claim that Round 16 proves a new Gauss circle exponent.** No agent supplied M9.

2. **Reject treating R5 as unconditional until H4 is source-normalized.** R5-Full is mathematically sound conditional on the exact Vaaler theorem and must still be written with edge cases.

3. **Reject the erroneous R5 `max` display.** The correct residual counting kernel is the exact-resonance cap plus

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min\left(1,\frac{\Delta^2}{u^2}\right),&u\ne0,
\end{cases}
$$

not a formula that becomes undefined or inflates every term.

4. **Reject H13 as a proof route by itself.** The transform preserves a dual character formally, but the resulting phase is Hessian-degenerate and the first natural norm extraction may erase the character.

5. **Reject A2's H13-Dual as "proved" in its strong form.** It is a conditional diagnostic until the actual post-H13 kernel, stationary amplitudes, support restrictions, and first Cauchy--Schwarz step are written.

6. **Reject BSOS as a lemma.** It is a proposed finite statistic and falsification object. No bound and no implication to M9 were proved.

7. **Reject generic operator-norm, Frobenius, Schur, Gershgorin, cyclic-trace, or absolute-value-matrix arguments as character-aware proofs for M9a when the character enters only as $U^*KU$.** Q1-Spectral shows these are character-blind.

8. **Reject black-box Li--Yang endpoint use.** Li--Yang is structurally relevant but does not cover the raw Vaaler endpoint height without additional theorem work.

9. **Reject treating the M9b $\chi_4(h)$ form as automatically admissible for theorems requiring smooth or bounded-variation $h$ weights.** Use the shifted-phase formulation instead.

## Known gaps

1. **H4 source-normalization.** The proof draft still needs exact page, theorem, and equation labels from Vaaler; notation must be translated from $N,j_N,k_N,\widehat J$ to $H,K_H,\Phi,\alpha_{h,H}$.

2. **R5-Full final proof.** The proof must include exact resonances, real $X$, nearest-integer ties, shifted legs $\rho=1,3$, positivity of $\ell=4m-\rho$, dyadic weights, short blocks, both frequency signs, zero Fejer mode, and dyadic logarithmic losses.

3. **M9 remains open.** No estimate of

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

was proved.

4. **M9 theorem comparison remains incomplete.** The shifted-$F$ formulation passes the derivative determinant check, but allowed $D,X$ dependence, weight classes, endpoint height, and fixed Vaaler $h$ weights must be checked against the theorem being invoked.

5. **Actual M9a Cauchy--Schwarz kernel not yet frozen.** Q1-Spectral should be applied to the actual first-step kernel, not to an abstract placeholder.

6. **Post-H13 kernel not yet frozen.** The actual dual kernel, amplitudes, support, and first spacing step must be written before declaring character preservation or collapse.

7. **Uniform H13 stationary phase is incomplete.** Need nonstationary terms, boundary stationary points, transition zones, and $M_{\rm dual}\asymp1$.

8. **BSOS has no proved implication.** It needs a finite formula, a target inequality, and either a proof that it implies a useful M9 bound or a falsification threshold.

9. **Executed numerics are missing.** Round 16 produced toy computations and protocols, not high-precision R5/M9/H13/BSOS tables.

## New lemmas to add

### Bridge-R16. Conditional Vaaler bridge

**Status: conditional proof skeleton.**

If H1--H3, H4, R5-Full, and M9 hold in the forms stated below, then

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This should be placed in `best_proof_draft.md` as a conditional theorem, not as an unconditional result.

### H4-R16. Finite Vaaler approximation with floor-compatible residual

**Status: external theorem dependency; source-located, final notation transcription pending.**

For $H\ge1$,

$$
\psi_F(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H^F(t),
$$

with

$$
\alpha_{h,H}
=
-\frac{\Phi(|h|/(H+1))}{2\pi i h},
$$

and

$$
|R_H^F(t)|\le \frac1{2H+2}K_H(t),
$$

where

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

At integers the residual majorant covers the half-jump because $K_H(0)/(2H+2)=1/2$.

### CCoef-R16. Vaaler coefficient conjugacy

**Status: proved algebraic lemma.**

For $1\le h\le H$,

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

This replaces all negative-conjugate pairings.

### R5-Full-R16. Fejer residual product-count bound

**Status: proved conditional on H4; proof-draft write-up still needed.**

Let

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H\asymp D X^{-1/4},
\qquad
\Delta=D/H\asymp X^{1/4}.
$$

Then, for dyadic $w_D$ with bounded overlap,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and, for $\rho\in\{1,3\}$,

$$
\frac1H\sum_{d\asymp D}|w_D(d)|K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

For the first leg, choose $m$ nearest to $X/d$ and use

$$
\left\|\frac Xd\right\|=\frac{|X-md|}{d}\asymp \frac{|X-md|}{D}.
$$

Then

$$
\frac1H K_H(X/d)
\ll
W_\Delta(X-md),
$$

where

$$
W_\Delta(u)=
\begin{cases}
1,&u=0,\\
\min\left(1,\frac{\Delta^2}{u^2}\right),&u\ne0.
\end{cases}
$$

Grouping by $n=md$ and using $\tau(n)\ll_\epsilon n^\epsilon$ gives the bound. For shifted legs, near-integrality gives $X\approx d(4m-\rho)$; write $\ell=4m-\rho$ and use the same product-count argument with a congruence restriction.

### M9-R16. Fixed-coefficient main-term target

**Status: open analytic target.**

For all dyadic $D$ in the active range,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

This is the sole active analytic bottleneck.

### M9-Pair-R16. Paired real form

**Status: proved algebraic reformulation.**

With $A_h$ and $B_h$ as above,

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

### M9b-Shift-R16. Shifted-phase formulation

**Status: proved algebraic reformulation; theorem applicability open.**

The second main term can be compared to reciprocal sums with

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X},
\qquad
\rho\in\{1,3\},
$$

and

$$
F'F'''-3(F'')^2=-\frac3{8z^6}.
$$

The open question is whether a Bombieri--Iwaniec/Li--Yang-type theorem permits this $D,X$-dependent shift and the fixed Vaaler weights at endpoint height.

### Q1-Spectral-R16. Operator-norm character-blindness

**Status: proved diagnostic under stated hypothesis.**

If $\chi_4(d)$ enters a spacing matrix only through

$$
K\mapsto U^*KU,
\qquad
U=\operatorname{diag}(\chi_4(d)),
$$

on odd denominators, then

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

The same blindness holds for Frobenius norm, Schur/Gershgorin after absolute values, spectral radius, and pure cyclic conjugacy traces. This does not block non-conjugacy signed forms.

### H12-Trace-R16. Pure cyclic trace invariance

**Status: proved diagnostic under stated hypothesis.**

For pure cyclic traces,

$$
\operatorname{Tr}((U^*KU)^m)=\operatorname{Tr}(K^m).
$$

No broader claim should be made.

### H13-Mod4-R16. B-process-first modulo-$4$ transform

**Status: derived under smoothness and convention hypotheses; uniform lemma not proved.**

Poisson summation modulo $4$ transfers the spatial character to a dual Gauss factor. Under the convention

$$
\phi_n(u)=hX/u-nu/4,
$$

the active sign is $n=-m$, the stationary point is

$$
u_0=2\sqrt{\frac{hX}{m}},
$$

the dual length is

$$
m\asymp \frac{hX}{D^2},
$$

and

$$
\phi_{-m}(u_0)=\sqrt{hXm}.
$$

The resulting square-root phase has zero Hessian determinant, so generic full-rank two-dimensional stationary phase or decoupling is unavailable.

### H13-Q1-Dual-R16

**Status: conditional diagnostic, not proved obstruction.**

If the first post-H13 spacing or Cauchy--Schwarz step puts the dual $\chi_4(m)$ only into a diagonal unitary conjugation, then Q1-Spectral applies again and the character is erased. This must be checked on the actual post-H13 kernel.

### BSOS-R16

**Status: heuristic/falsification statistic.**

BSOS may be tested as a signed off-diagonal statistic, but it is not a lemma until it has:

1. an exact finite definition;
2. a target bound;
3. a proof that the target implies a useful M9 estimate, or a clear falsification criterion;
4. comparison with unsigned, absolute-majorant, and operator-norm quantities.

## Counterexample checks to run

1. **H4 page/equation audit.** Quote Vaaler Theorem 18 and Theorem 6 with printed page and equation labels. Verify coefficient sign, Fejer kernel normalization, residual constant, and jump convention.

2. **R5 exact-resonance test.** Evaluate cases where $X/d\in\mathbb Z$ or $(X/d+\rho)/4\in\mathbb Z$. Confirm the bound uses the finite value $(H+1)/H\le2$, not division by zero.

3. **R5 raw-form tables.** Compute

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d)
$$

and the shifted analogues for square, nonsquare, near-square, and divisor-rich $X$, normalized by $X^{1/4}$.

4. **M9 paired-frequency regression.** Compute $\mathcal M_1,\mathcal M_2$ using both the two-sided raw formula and the paired real formula. They must agree numerically.

5. **M9 fixed-coefficient tables.** Use at least $\delta=1/4,3/8,1/2$ with $D=X^\delta$, multiple $X$, and report

$$
|\mathcal M_i(D;X)|/X^{1/4}.
$$

Compare against arbitrary-coefficient and $L^1$ stress norms.

6. **Li--Yang subrange map.** For $D=X^\delta$, table

$$
\beta_V=\delta-\frac14,
\qquad
\beta_A=\delta-\frac{49}{164},
$$

$$
\beta_{B1}=\frac{35}{69}\delta-\frac{2}{23},
\qquad
\beta_{B2}=\frac32\delta-\frac12,
$$

and

$$
\beta_*=\delta-\theta^*.
$$

Identify the uncovered high-frequency interval.

7. **Shifted-$F$ uniformity audit.** Verify whether the theorem being compared permits

$$
F_{\rho,D}(z)=\frac1{4z}+\frac{\rho D}{4X}
$$

with uniform constants and the actual Vaaler $h$ weights.

8. **Actual M9a Q1 test.** Construct the first natural Cauchy--Schwarz kernel from M9a and verify whether the character enters only as $U^*KU$.

9. **Actual post-H13 Q1 test.** Construct the endpoint post-H13 kernel for $D\asymp X^{1/2}$ and verify whether the dual character survives beyond diagonal unitary conjugation.

10. **H13 stationary-phase test.** Check the constant, sign, active $m$ range, boundary stationary points, $M_{\rm dual}\asymp1$, and nonstationary integration-by-parts tails.

11. **BSOS falsification.** Implement one finite odd-denominator statistic and compute signed value, unsigned value, absolute majorant, and operator-norm comparator. If no stable signed gain appears, deprioritize BSOS.

12. **Short-block check.** Verify that all $D<X^{1/4}$ blocks are removed before Vaaler and bounded by $O(X^{1/4}\log X)$ or better.

## Research strategy adjustment

Do not expand the route set. Round 17 should be narrower and more executable.

The main route remains the conditional Vaaler reduction, with M9 as the active bottleneck. The residual side should be treated as provisionally cleared but still audited: finish H4 and R5-Full in proof-draft form. The analytic work should now focus on fixed coefficients, not arbitrary coefficients.

Use Q1-Spectral as a filter: any proposed M9 proof that immediately passes to an operator norm, Frobenius norm, Schur/Gershgorin estimate, absolute-value matrix, or cyclic conjugacy trace should be deprioritized unless it explains how $\chi_4$ is used before that step.

Allocate one limited exploratory slot to H13 near $D\asymp X^{1/2}$, where

$$
m\asymp h\asymp X^{1/4}
$$

at maximal height. If the endpoint signed-dual test shows immediate character erasure or no signed gain, demote H13 to a comparison module.

A2 and A3 should be assessed separately as follows:

- **A2:** valuable for Q1/H12 diagnostics and for proposing falsifiable signed statistics; overclaims around H13-Dual and BSOS must be downgraded. Next A2 output should be shorter, proof-draft-ready, and tied to actual M9/H13 kernels.
- **A3:** valuable for coefficient, endpoint, Li--Yang, and H13 formula audits; next A3 output should prioritize executed tables and corrected scripts over further expository protocols.

## Next-round prompts by agent

### For A1

Produce the Round 17 proof-infrastructure and theorem-comparison packet.

Objectives:

1. **Finalize H4-R16 source-normalization.**
   - Quote Vaaler's exact page, theorem, and equation numbers.
   - Translate $N,j_N,k_N,\widehat J_{N+1}$ into $H,K_H,\Phi,\alpha_{h,H}$.
   - Verify the sign of $\alpha_{h,H}$.
   - Verify the residual constant $1/(2H+2)$.
   - State the centered-to-floor-compatible conversion at integers.

2. **Insert R5-Full-R16 into proof-draft form.**
   Include:
   - first leg $K_H(X/d)$;
   - shifted legs $K_H((X/d+\rho)/4)$ for $\rho=1,3$;
   - integer and real $X$;
   - nearest-integer ties;
   - exact resonances using $W_\Delta(0)=1$;
   - $\ell=4m-\rho$ and positivity of $\ell$;
   - zero Fejer mode;
   - dyadic weights and bounded overlap;
   - frequency signs;
   - short blocks $D<X^{1/4}$;
   - logarithmic losses.

3. **Write Bridge-R16 in final conditional form.**
   State only:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Do not imply M9 is proved.

4. **Freeze M9 and the paired formulas.**
   Put arbitrary-coefficient variants into a stress-test appendix. Use the paired real formulas for all numerical and theorem-comparison work.

5. **Build the full Li--Yang subrange map.**
   For all $\delta\in[1/4,1/2]$, compare $\beta_V,\beta_A,\beta_{B1},\beta_{B2},\beta_*$. Identify exactly where the endpoint Vaaler height is uncovered.

6. **State the shifted-$F$ theorem-extension problem for M9b.**
   List the theorem hypotheses that must be checked: $D,X$-dependent additive shift, derivative constants, weight class, dyadic $h$ coefficient variation, and endpoint frequency height.

Exploratory allocation: write a one-page H13 falsification checklist specifying the exact first post-transform step that would reduce to Q1-Spectral.

### For A2

Produce a proof-draft-ready signed-diagnostic packet. Avoid broad route-closing language.

Objectives:

1. **Write Q1-Spectral-R17 for the actual M9a first-step kernel.**
   Define the finite index set, the actual kernel arising from the first Cauchy--Schwarz or spacing step, and prove whether the character enters as $U^*KU$.

2. **Write H12-R17 narrowly.**
   Prove only the pure cyclic trace identity and list what it does not block.

3. **Downgrade and repair H13-Dual.**
   Construct the actual endpoint post-H13 kernel at $D\asymp X^{1/2}$. Include the stationary amplitude weights. State precisely whether the dual $\chi_4(m)$ appears by diagonal unitary conjugation or in a non-conjugacy form.

4. **Make BSOS executable or discard it.**
   Provide:
   - one finite matrix definition;
   - signed statistic;
   - unsigned comparator;
   - absolute-majorant comparator;
   - operator-norm comparator;
   - target bound;
   - proof or clear statement of what bound would imply for M9.

   If the implication to M9 is unavailable, label BSOS only as a falsification statistic.

5. **Connect or retire C3.**
   Keep C3 only if the half-integer translation/dilation variables are explicitly mapped to M9 or H13 variables. Otherwise move it to a diagnostic appendix.

Exploratory allocation: one endpoint H13/BSOS signed-vs-unsigned test plan, not a general alternative route.

### For A3

Prioritize corrected scripts, tables, and exact citations over prose.

Objectives:

1. **H4 source table.**
   Produce a table with:
   - Vaaler theorem/equation/page;
   - object in Vaaler notation;
   - repo object;
   - coefficient sign;
   - residual constant;
   - jump convention.

2. **Corrected R5 raw-form tables.**
   Use exact or high-precision arithmetic. Compute both residual legs from raw definitions:

$$
\frac1{H_D}\sum_{d\asymp D}K_{H_D}(X/d),
\qquad
\frac1{H_D}\sum_{d\asymp D}K_{H_D}\left(\frac{X/d+\rho}{4}\right),
$$

for $\rho=1,3$, without double division and without the erroneous `max` expression.

3. **M9 fixed-coefficient numerical tables.**
   For at least $\delta=1/4,3/8,1/2$, and for square, nonsquare, near-square, and divisor-rich $X$, report:

$$
|\mathcal M_1(D;X)|/X^{1/4},
\qquad
|\mathcal M_2(D;X)|/X^{1/4}.
$$

Also compare fixed coefficients with arbitrary-coefficient and $L^1$ stress norms.

4. **H13 constant and stationary-phase verification.**
   Under the convention $\phi_n(u)=hX/u-nu/4$, verify:

$$
u_0=2\sqrt{\frac{hX}{m}},
\qquad
\phi_{-m}(u_0)=\sqrt{hXm},
\qquad
m\asymp \frac{hX}{D^2}.
$$

Include nonstationary and boundary regimes as separate rows.

5. **Li--Yang subrange and shifted-$F$ audit.**
   Produce the full $\delta$ table and a separate checklist for whether $F_{\rho,D}$ is allowed uniformly.

6. **Q1/H13/BSOS numerical tests.**
   Build:
   - actual M9a first-step matrix;
   - endpoint post-H13 matrix;
   - one BSOS matrix.

   Report signed, unsigned, absolute-majorant, and operator-norm quantities.

## Confidence

High confidence in the balanced hyperbola/Vaaler route as the correct current reduction framework.

High confidence that H1--H3 remain valid arithmetic reductions.

Moderate-to-high confidence that H4 is correctly located and formula-consistent with Vaaler, but final source-normalized proof text is still required.

High confidence that R5-Full controls the Fejer residual at the conjectural scale once H4 is accepted and exact resonance handling is corrected.

High confidence that the correct Vaaler pairing is

$$
\alpha_{-h,H}=\overline{\alpha_{h,H}}.
$$

High confidence that M9 fixed-coefficient main sums are open and are the sole active analytic bottleneck.

High confidence that Li--Yang cannot be imported as a black box at the endpoint Vaaler height.

High confidence that Q1-Spectral is a valid diagnostic for diagonal-unitary/operator-norm methods, but low confidence that it rules out all signed methods.

Moderate confidence that H13 is worth exactly one more endpoint-focused falsification round.

Low confidence that BSOS, H13, signed Fourier, Mellin--Perron, or current printed Li--Yang technology proves M9 without a genuinely new signed or spacing estimate.

No new Gauss circle exponent has been proved in Round 16.