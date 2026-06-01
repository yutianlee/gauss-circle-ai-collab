Summary:

Round 7 did not prove any improvement to the Gauss circle exponent. It did make real checkable progress: the Vaaler-residual bottleneck H5r is now norm-level explicit, the minimal fixed-Fejer target H5r-F has been separated from stronger arbitrary-coefficient and termwise-$L^1$ targets, the odd-lattice Poisson transform C2 has been clarified, and the Mellin--Perron and rational-collision tracks have been downgraded to comparison/diagnostic roles where appropriate. Source anchors:

Selected main route:

Keep the balanced arithmetic hyperbola/Vaaler route as the main **reduction and diagnostic framework**, but do not present it as a near-proof of the conjectural bound. The proof skeleton remains:

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

The target is still

$$
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

equivalently

$$
E(R)\ll_\epsilon R^{1/2+\epsilon}.
$$

The Round 7 change is that **H5r-F should now be the official minimal residual target** for the Vaaler route. H5r-B and H5r-L1 remain useful stronger sufficient targets and stress-test norms, but replacing H5r-F by them too early may discard fixed-Fejer coefficient structure.

The current analytic dependencies should be recorded in this order:

$$
\text{H5r-B}
\Longrightarrow
\text{H5r-F}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

The reverse implication is not proved and should not be assumed. In particular, H5r-F may be weaker than H5r-B because it uses the fixed Fejer coefficients

$$
\eta_{k,H_D}=1-\frac{|k|}{H_D+1}.
$$

However, Gemini's Abel-summation warning creates a serious possible obstruction: because these weights are positive and monotone, bounding H5r-F may still reduce to bounding partial sums close to H5r-B unless a method exploits the exact Fejer averaging more subtly.

Useful fragments by source:

## From `gpt_pro_thinking`

The most valuable contribution is the precise norm hierarchy for the Vaaler residual.

The main dependency chain is:

$$
\text{H5r-B}
\Longrightarrow
\text{H5r-F}
\Longrightarrow
\text{Vaaler residual contribution}\ll_\epsilon X^{1/4+\epsilon}.
$$

Here H5r-F is the fixed-Fejer target naturally produced by the positive-majorant Vaaler proof, while H5r-B is a stronger arbitrary-coefficient target. In the arbitrary complex coefficient formulation, H5r-B is essentially equivalent to dyadic termwise $L^1$ control:

$$
\sum_{k\sim K_0}|S_\star(k,D)|
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

This is an important distinction: H5r-B is safe but may be too destructive.

The corrected C1 diagnostic is also valuable. If H5r can only be bounded by character-blind reciprocal-sum estimates at exponent $\theta$, normalized as

$$
\sum_{k\sim K_0} v_k S_\star(k,D)
\ll_\epsilon K_0X^{\theta+\epsilon},
$$

then, assuming H5a/H5b are already handled at the conjectural scale, the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}.
$$

This replaces the incorrect multiplicative scaling $X^{1/4+\theta}$ and should be entered as the official C1 formulation.

The non-majorizing comparison is useful but still undeveloped. Vaaler produces H5r; signed Fourier truncation replaces H5r by a high-frequency signed tail; Mellin--Perron replaces it by contour, moment, and functional-equation estimates for

$$
4\zeta(s)L(s,\chi_4).
$$

None is currently an escape route.

## From `deepseek_api`

The most valuable contribution is the algebraic clarification of C2 and the sharper H5r structural audit.

For a smooth dyadic weight $w_D$ and

$$
F(u)=w_D(u)e(kX/u),
$$

the odd-lattice residual

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
$$

admits both an alternating representation and a two-coset representation:

$$
S_{\mathrm{odd}}(k,D)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
=
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu),
$$

where

$$
I(\xi)=\int_{\mathbb R}w_D(u)e(kX/u-\xi u)\,du.
$$

This is a transformation lemma, not an obstruction theorem. The stationary range has scale

$$
|\xi|\asymp \frac{kX}{D^2}.
$$

DeepSeek also usefully identifies the boundary regime

$$
D\asymp X^{1/2},\qquad k\asymp 1,
$$

where the dual length is $O(1)$ and uniform stationary phase cannot be assumed.

The derivative checks for shifted reciprocal phases should be retained. For

$$
F_{2,1}(x)=\frac1{x+1/D}
$$

and

$$
F_2(x)=\frac1{4x},
$$

the nondegeneracy expression

$$
F'F'''-3(F'')^2
$$

is nonzero on compact subintervals of $(0,\infty)$. This supports the structural claim that H5r sits inside the same broad reciprocal-sum phase class as Li--Yang/Bombieri--Iwaniec-type estimates. It does **not** prove that any existing theorem applies with the needed coefficients, weights, absolute-value placement, and endpoint strength.

DeepSeek's Fejer-spike warning is useful as a testable failure mode: square and near-square $X$ may align many terms near spikes of the Fejer kernel. This should be tested numerically before treating the Vaaler majorant as harmless.

## From `gemini_deep_think`

The most useful contribution is the rational-collision sign lemma for the spatial-character family H5a. For exact rational collisions

$$
d_1b=d_2a,\qquad (a,b)=1,
$$

one has

$$
d_1=ac,\qquad d_2=bc.
$$

If

$$
\chi_4(d_1)\chi_4(d_2)\ne0,
$$

then $a,b,c$ are odd and

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ac)\chi_4(bc)
=
\chi_4(a)\chi_4(b)\chi_4(c)^2
=
\chi_4(ab).
$$

Thus $\chi_4$ is not random on exact collision lines; it becomes a block-constant sign indexed by the rational slope $a/b$. The loss happens later if matrix norms or absolute values replace $\chi_4(ab)$ by $1$. This is a narrow but genuinely useful algebraic lemma for future signed Bombieri--Iwaniec bookkeeping.

Gemini's Mellin--Perron analysis is also valuable after downgrading its rhetoric. Sharp Perron truncation suggests a height near

$$
T\gg X^{3/4}
$$

to force truncation error at the $X^{1/4+\epsilon}$ scale. Applying the functional equation plausibly reconstructs Voronoi/Bessel reciprocal sums of length about

$$
T^2/X\asymp X^{1/2}.
$$

This is a strong diagnostic that Mellin--Perron mirrors the same difficulty, but it is not a theorem until the smoothed contour, residues, functional equation, and stationary phase are written explicitly.

Gemini's C3 parity-collapse calculation is a useful diagnostic but was overstated. In the one-sequence representation, direct differencing of the alternating coefficient gives

$$
(-1)^m(-1)^{m+q}=(-1)^q,
$$

so the coefficient alone carries no persistent mod-$2$ oscillation under translation differencing. But the two-coset representation may retain phase-spacing information not visible in the one-sequence coefficient model. Therefore C3 is diagnostic, not a global obstruction.

Rejected or risky ideas:

1. **Reject: H5r can be replaced by a scalar Vaaler error.**

The residual is not just $O(D/H_D)$. The zero Fejer mode contributes

$$
D/H_D\asymp X^{1/4},
$$

but the nonzero Fejer modes create actual reciprocal sums. Any proof discarding them is incomplete.

2. **Reject: H5r-B is the minimal target.**

H5r-B is sufficient, but H5r-F is the actual fixed-Fejer target forced by the residual. H5r-B may be too strong and may effectively reduce the problem to termwise $L^1$ or character-blind divisor-type estimates.

3. **Reject: H5r-F is automatically easier than H5r-B.**

This is not proved. Because Fejer coefficients are positive and monotone, Abel summation may force H5r-F to depend on partial sums resembling H5r-B. This is now an explicit gap, not a resolved advantage.

4. **Reject: C2/C3 proves B-process-first fails for H5r.**

C2 is a Poisson transformation lemma. C3 shows coefficient parity collapse in one representation under direct A-process. It does not rule out two-coset spacing gains or non-translation-invariant spacing arguments.

5. **Reject: Li--Yang compatibility as theorem-level applicability.**

The phase shape matches reciprocal-sum classes, but the exact theorem audit remains incomplete. The repo must check weights, coefficient classes, blockwise absolute values, parity restrictions, dyadic ranges, and whether the theorem gives only $\theta^*\approx0.31448$ rather than $1/4$.

6. **Reject: Mellin--Perron circularity as an impossibility theorem.**

The functional-equation route probably reconstructs Voronoi/Bessel/reciprocal sums, but this is currently a diagnostic. New contours, smoothing, or moment inputs are not ruled out.

7. **Reject: rational-collision sign structure displaces H5r.**

The exact-collision $\chi_4(ab)$ lemma is useful for H5a and signed matrix bookkeeping. It does not solve or bypass the central H5r residual bottleneck.

8. **Reject: any claim of exponent improvement.**

Round 7 sharpened the reduction and bottleneck. It did not prove

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

or any new upper exponent.

Known gaps:

1. **Exact Vaaler reference and normalization.**

The repo still needs the precise theorem statement for the Vaaler approximation being used, including the coefficient formula, Fejer majorant normalization, and discontinuity behavior. The proof uses the majorant form

$$
|R_H(t)|\le (2H+2)^{-1}K_H(t),
$$

but this should be checked against a standard reference before H4 is marked as fully imported.

2. **H5r-F sufficiency over the full proof.**

Round 7 gives the block-level implication, but the proof draft must explicitly sum over all dyadic $D$, both residual families, signs of $k$, the zero mode, endpoint blocks, and the two legs of H3.

3. **Abel-summation relation between H5r-F and H5r-B.**

The potential equivalence or near-equivalence between fixed Fejer averages and partial-sum estimates must be formulated precisely. The key question is whether monotonic Fejer weights force H5r-F to be controlled by H5r-B-type partial sums, or whether fixed coefficients provide exploitable cancellation.

4. **C2 stationary phase.**

C2 requires a convention-fixed statement with exact signs, active sign of $\xi$, stationary point, phase constant, amplitude, nonstationary integration-by-parts bounds, and transition estimates. The boundary case

$$
D\asymp X^{1/2},\qquad k\asymp1
$$

must be handled separately.

5. **C3 two-coset spacing.**

It is unknown whether the two-coset formulation retains spacing information lost in the one-sequence $(-1)^m$ representation. This must be tested before C3 is promoted beyond diagnostic status.

6. **H5r-to-Li--Yang theorem audit.**

Structural compatibility is not enough. The exact theorem must accept the relevant $k$-weights, $d$-weights, parity coefficients, shifts, blockwise absolute values, and ranges

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le K_0\le H_D\asymp DX^{-1/4}.
$$

7. **Signed Fourier truncation tail.**

A signed truncation might preserve $\chi_4$ better than the positive Fejer majorant, but no usable tail bound is known. If the tail must be bounded absolutely, the route likely recreates H5r.

8. **Mellin--Perron theorem-dependency.**

The repo needs exact sharp and smoothed Perron formulas, contour shifts, residue extraction, functional equation, stationary phase, and the moment/subconvexity inputs needed to reach $X^{1/4+\epsilon}$.

9. **Near-collision character behavior.**

The exact-collision lemma is proved only when $d_1b=d_2a$. It is unknown whether the block sign survives near-collisions

$$
d_1b-d_2a=\Delta\ne0.
$$

10. **Numerical stress tests.**

No numerical evidence yet compares H5r-F, H5r-B, and H5r-L1, especially for square and near-square $X$. This is now a priority.

New lemmas to add:

## R1. Fixed-Fejer residual sufficiency

**Status:** proved conditional lemma.

Assume H5r-F for each residual family $S_\star(k,D)$ on every dyadic block

$$
X^{1/4}\le D\le X^{1/2},
$$

where $S_\star$ is one of

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d),
$$

or

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
\qquad \rho\in\{1,3\}.
$$

With

$$
H_D\asymp DX^{-1/4},
$$

and

$$
\eta_{k,H_D}=1-\frac{|k|}{H_D+1},
$$

the hypothesis is

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
\ll_\epsilon X^{1/4+\epsilon}.
$$

Then the total Vaaler residual contribution is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof sketch: the zero mode contributes

$$
D/H_D\asymp X^{1/4}
$$

per dyadic block. The nonzero modes are bounded by H5r-F. The number of blocks is $O(\log X)$ and is absorbed into $X^\epsilon$.

## R2. Arbitrary bounded coefficients imply fixed Fejer

**Status:** proved conditional lemma.

For each dyadic block $K_0\le H_D$, suppose

$$
\sum_{k\sim K_0}v_kS_\star(k,D)
\ll_\epsilon K_0X^{1/4+\epsilon}
$$

uniformly for $|v_k|\le1$. Then H5r-F follows by dyadic decomposition of $1\le |k|\le H_D$ and taking $v_k=\eta_{k,H_D}$ on each dyadic block, followed by division by $H_D$ and summation over $K_0$.

## R3. Arbitrary complex H5r-B and dyadic H5r-L1 equivalence

**Status:** elementary.

If H5r-B is required for all complex coefficients $|v_k|\le1$, then it is equivalent to the dyadic $L^1$ estimate

$$
\sum_{k\sim K_0}|S_\star(k,D)|
\ll_\epsilon K_0X^{1/4+\epsilon}.
$$

The implication from H5r-B to $L^1$ follows by choosing $v_k$ to match the conjugate phase of $S_\star(k,D)$.

## R4. Abel-summation trap for H5r-F

**Status:** proposed diagnostic lemma.

Let

$$
A(t)=\sum_{1\le |k|\le t}S_\star(k,D)
$$

or the appropriate one-sided partial sum after separating signs. Since $\eta_{k,H}$ is positive and monotone on $1\le k\le H$, Abel summation expresses

$$
\sum_{1\le k\le H}\eta_{k,H}S_\star(k,D)
$$

as a controlled linear combination of partial sums $A(t)$. Therefore any proof of H5r-F by bounding partial sums only inherits an H5r-B-type difficulty. To beat this, a method must exploit more than generic partial-sum bounds.

This should be entered as a diagnostic, not as an impossibility theorem.

## C1. Corrected Fejer Majorant DDP diagnostic

**Status:** conditional diagnostic.

If the only available H5r estimate is a character-blind reciprocal-sum bound

$$
\sum_{k\sim K_0}v_kS_\star(k,D)
\ll_\epsilon K_0X^{\theta+\epsilon},
$$

then the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon},
$$

assuming H5a/H5b are controlled at the conjectural scale. This is not a lower bound.

## C2. Odd-lattice Poisson transform

**Status:** transformation proved up to convention; stationary-phase constants still pending.

For

$$
F(u)=w_D(u)e(kX/u),
$$

and

$$
I(\xi)=\int_{\mathbb R}w_D(u)e(kX/u-\xi u)\,du,
$$

one has

$$
\sum_{\substack{d\sim D\\2\nmid d}}w_D(d)e(kX/d)
=
\frac12\sum_{n\in\mathbb Z}(-1)^nI(n/2)
=
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu),
$$

under the fixed Fourier convention, after standard regularization if needed. The stationary scale is

$$
|\xi|\asymp \frac{kX}{D^2}.
$$

## C2-SP. Stationary-phase parameters for C2

**Status:** conditional/standard in interior; boundary unresolved.

For $m>0$ and $J(m)=I(-m)$, in the interior range

$$
m\asymp \frac{kX}{D^2},
$$

one expects

$$
|J(m)|\asymp D^{3/2}(kX)^{-1/2},
$$

with rapid decay outside the stationary range by integration by parts. At

$$
D\asymp X^{1/2},\qquad k\asymp1,
$$

the dual length is $O(1)$ and no uniform asymptotic may be invoked without a separate endpoint argument.

## C3. Dual parity A-process diagnostic

**Status:** diagnostic only.

In the one-sequence representation, direct differencing gives

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

This removes coefficient oscillation under a direct translation A-process. It does not rule out two-coset spacing arguments.

## N1. Shifted reciprocal derivative nondegeneracy

**Status:** proved algebraic lemma.

For

$$
F_{2,1}(x)=\frac1{x+1/D}
$$

and

$$
F_2(x)=\frac1{4x},
$$

one has

$$
F'F'''-3(F'')^2\ne0
$$

on compact subintervals of $(0,\infty)$. This confirms structural reciprocal-sum compatibility, not theorem-level applicability.

## N2. Li--Yang compatibility

**Status:** structural, not theorem-level.

The sums $S_{\mathrm{odd}}(k,D)$ and $S_\rho(k,D)$ can be placed into a Li--Yang/Bombieri--Iwaniec-style reciprocal phase class after residue splitting and scaling. Existing technology appears to give an exponent around $\theta^*\approx0.31448$ in $X$-notation, not the endpoint $1/4$. This must be audited from the precise theorem before use.

## Q1. Exact rational-collision character factorization

**Status:** proved algebraic lemma.

Let $(a,b)=1$ and suppose

$$
d_1b=d_2a.
$$

Then $d_1=ac$, $d_2=bc$ for some integer $c$. If

$$
\chi_4(d_1)\chi_4(d_2)\ne0,
$$

then $a,b,c$ are odd and

$$
\chi_4(d_1)\chi_4(d_2)=\chi_4(ab).
$$

This is useful for signed rational-collision matrices but does not address near-collisions.

## H10. Mellin--Perron comparison route

**Status:** comparison module, not proof route.

For $c>1$,

$$
\sum_{n\le X}r_2(n)
=
\frac1{2\pi i}
\int_{c-iT}^{c+iT}
4\zeta(s)L(s,\chi_4)\frac{X^s}{s}\,ds
+
\text{truncation error}.
$$

The pole at $s=1$ gives $\pi X$. Sharp truncation suggests $T\gg X^{3/4}$ for endpoint error, while the functional equation likely reconstructs Voronoi/Bessel reciprocal sums of length $\asymp X^{1/2}$. This must be written with smoothing and endpoint conventions before being used.

Counterexample checks to run:

1. **H5r-F versus H5r-B/L1 numerical comparison.**

For square, nonsquare, and near-square $X$, compute

$$
R_F=
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|,
$$

and compare with

$$
R_{L1}=
\frac1{H_D}
\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

A large gap would show that fixed Fejer coefficients preserve useful cancellation. Comparable sizes would support the Abel-summation bottleneck concern.

2. **Fejer spike test.**

Test $X,d$ such that one of

$$
X/d,\qquad
\frac{X/d+1}{4},\qquad
\frac{X/d+3}{4}
$$

is close to an integer. These are where $K_H$ can spike and scalar residual bounds fail.

3. **C2 convention test.**

Verify directly on compactly supported test functions that

$$
\frac12\sum_{n\in\mathbb Z}(-1)^nI(n/2)
$$

equals

$$
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu)
$$

under the chosen Fourier convention.

4. **C2 stationary-phase constants.**

For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

check the active sign of $\xi$, stationary point, phase value, second derivative, amplitude, and signature factor. Treat separately the boundary regime

$$
kX/D^2\asymp1.
$$

5. **C3 two-coset A-process test.**

Apply differencing in both the alternating and two-coset forms. Determine whether cross-terms retain spacing information or merely modulate amplitudes.

6. **H5r-to-Li--Yang audit.**

Write $S_{\mathrm{odd}}$ and $S_\rho$ exactly in the form required by a candidate Li--Yang/Bombieri--Iwaniec theorem. Check support, smoothness, derivative hypotheses, $k$-weights, arbitrary coefficients, parity restrictions, absolute-value placement, and parameter ranges.

7. **Signed Fourier tail test.**

After the hyperbola cut, compare Vaaler truncation with the signed Fourier expansion

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi ih}
$$

truncated at height $H_D$. Determine whether the high-frequency tail can be bounded without termwise absolute values and whether it preserves $\chi_4$.

8. **Mellin--Perron truncation and functional-equation test.**

Write both sharp and smoothed Perron errors with explicit $T$-dependence. Shift contours, extract the pole at $s=1$, apply the functional equation, and derive the resulting dual length. Test whether the route genuinely differs from H5r or simply reconstructs the same reciprocal sums.

9. **Near-collision sign stress test.**

For small $\Delta$ in

$$
d_1b-d_2a=\Delta,
$$

measure the average of

$$
\chi_4(d_1)\chi_4(d_2)
$$

conditioned on the near-collision. Determine whether the exact-collision block sign $\chi_4(ab)$ persists statistically.

10. **Poisson--Bessel calibration check.**

Keep the secondary module that recovers

$$
E(R)\ll R^{2/3}
$$

from smoothing and Bessel/Poisson estimates. This remains a normalization check, not the selected proof route.

Next round instructions:

## For `gpt_pro_thinking`

1. Formalize R4, the Abel-summation relation between H5r-F and partial-sum/H5r-B estimates. State exactly what it proves and what it does not prove.

2. Extend the non-majorizing comparison table with a column for **character preservation**:
   - Vaaler with Fejer majorant;
   - signed Fourier truncation;
   - sharp Perron;
   - smoothed Perron;
   - Poisson--Bessel calibration.

3. For signed Fourier truncation, derive the exact high-frequency tail after the hyperbola cut and identify whether bounding it requires absolute values.

4. Insert R1--R3 and C1 into the best proof draft with their exact statuses.

5. Add the Poisson--Bessel calibration proof as a secondary sanity check, but do not let it displace H5r-F.

## For `deepseek_api`

1. Run numerical tests comparing H5r-F, H5r-B, and H5r-L1 for square, nonsquare, and near-square $X$.

2. Verify the C2 Fourier signs and stationary-phase constants under the convention

$$
e(t)=e^{2\pi it}.
$$

3. Investigate the boundary regime

$$
D\asymp X^{1/2},\qquad k\asymp1,
$$

where the dual length is $O(1)$. Decide whether direct one-dimensional estimates on the primal sum can handle this range.

4. Audit the exact Li--Yang/Bombieri--Iwaniec theorem and determine whether it applies to $S_{\mathrm{odd}}$ and $S_\rho$ with the weights and absolute values required by H5r.

5. Recheck N1/N2 with all constants and parameter dependencies.

## For `gemini_deep_think`

1. Formalize the rational-collision observation Q1 and then extend it, if possible, to a near-collision lemma with an explicit error or failure condition.

2. Develop the Mellin--Perron route to theorem-dependency level:
   - sharp and smoothed Perron formulas;
   - contour shift;
   - residue at $s=1$;
   - functional equation for $4\zeta(s)L(s,\chi_4)$;
   - stationary-phase derivation of the reciprocal dual sums;
   - exact comparison with H5r.

3. Downgrade all language such as "isomorphism," "sterile," and "circular trap" to diagnostic language unless a theorem is proved.

4. Analyze whether the two-coset C2 formulation retains any spacing information after A-process or whether it merely repackages the same parity collapse.

Confidence:

High confidence in the selected route as a reduction and diagnostic framework.

High confidence that H5r is mandatory and cannot be replaced by a scalar residual.

High confidence in the corrected norm hierarchy:

$$
\text{H5r-B}
\Longrightarrow
\text{H5r-F}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

High confidence that complex-coefficient H5r-B is equivalent to dyadic termwise $L^1$ control.

High confidence in the corrected C1 normalization:

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}.
$$

Moderate-to-high confidence in C2 as a Poisson transformation, up to convention-fixed signs.

Moderate confidence in the C2 stationary-phase length

$$
|\xi|\asymp kX/D^2.
$$

Moderate confidence that the rational-collision exact sign factorization is correct and useful for H5a.

Moderate confidence that Mellin--Perron reconstructs Voronoi/Bessel reciprocal sums after the functional equation, but this remains a theorem-dependency target.

Low confidence that current Li--Yang/Bombieri--Iwaniec technology proves the endpoint H5r-F bound.

Low confidence that signed Fourier truncation or Mellin--Perron currently avoids a problem as hard as H5r.

No new Gauss circle exponent has been proved. Round 7 should be recorded as a successful precision round: it identifies H5r-F as the central minimal bottleneck, separates stronger norms from the actual residual target, and provides concrete algebraic and numerical tests for deciding whether the Vaaler route has any remaining advantage.
