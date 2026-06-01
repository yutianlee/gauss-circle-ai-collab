# Reading Packet

Generated after round 10 in run `web-research-test`.

## Current State

# Current Research State

No completed rounds yet.

The first round should focus on strategy selection, known barriers, and a clean decomposition of the Gauss circle error term.

## Round 1 Update

Timestamp: 2026-05-31 22:51:21

See `rounds/web-research-test/round_001/judge/judge.md`.

Selected main route:

Adopt a **two-track decomposition, with the arithmetic hyperbola/sawtooth route as the main analytic route and the smoothed Poisson--Bessel route as a normalization and sanity-check route**.

The main Round 2 objective should not be "prove the conjecture."It should be to produce a verified, endpoint-safe reduction from

$$
E(R)=N(R)-\pi R^2
$$

to balanced dyadic sums coming from the identity

$$
r_2(n)=4\sum_{d\mid n}\chi_4(d),
$$

with $X=R^2$ and target

$$
P(X):=N(\sqrt X)-\pi X=O_\epsilon(X^{1/4+\epsilon}).
$$

The selected analytic route is:

1. Prove an exact **symmetric Dirichlet hyperbola identity** for

$$
T(X):=\sum_{ab\le X}\chi_4(a),
\qquad
N(\sqrt X)=1+4T(X).
$$

2. Convert this identity into sawtooth terms using

$$
\psi(t)=t-\lfloor t\rfloor-\frac12
$$

with explicit endpoint conventions.

3. Apply Vaaler truncation only after the hyperbola cut, so the sums have length about $\sqrt X$ rather than $X$.

4. Derive the exact dyadic exponential-sum target, expected to involve sums of the schematic form

$$
\sum_{h\sim H}\frac{1}{h}
\sum_{d\sim D} c_d e\left(\frac{hX}{d}\right),
\qquad D\le X^{1/2},
$$

with $c_d$ equal either to $\chi_4(d)$ or to coefficients arising from the second hyperbola leg.

Useful fragments by source:

**From `gpt_pro_thinking`:**

The strongest contribution is the normalization into two complementary forms: a smoothed Poisson--Bessel decomposition and an arithmetic sawtooth decomposition using $r_2(n)=4\sum_{d\mid n}\chi_4(d)$. This is the right first-round foundation. The Poisson--Bessel side should remain in the repo because it gives a checkable smoothing/unsmoothing framework and recovers the classical $R^{2/3}$ estimate from trivial radial-sum bounds.

The proposed conditional benchmark

$$
A_M(R)
=
\sum_{k\ne 0}w(|k|/M)e(R|k|)
\ll_\epsilon M^{3/2}R^\epsilon
$$

is useful as a diagnostic criterion, not as a likely direct proof route. It quantifies what type of cancellation the smoothed geometric formulation would need.

The arithmetic identity

$$
P(X)
=
-4\sum_{d\le X}\chi_4(d)\psi(X/d)+O(1)
$$

is valuable as a compact exact reduction, but it should not be the final analytic form for Vaaler truncation. Before estimation, the sum should be shortened by the Dirichlet hyperbola method.

The literature-status discipline is also valuable: record Huxley, Bourgain--Watt, Li--Yang, and ANTEDB separately, and do not use any record exponent as a black-box dependency until the theorem statement and hypotheses are checked.

**From `gemini_deep_think`:**

The most useful mathematical warning is that the raw geometric phase

$$
R\sqrt{x^2+y^2}
$$

and the homogeneous model phase

$$
R\sqrt{ab}
$$

have rank-deficient Hessian. Therefore any proposed proof that applies a generic full-rank two-dimensional stationary phase or decoupling theorem directly to these phases is invalid.

The proposed symmetric hyperbola route is also useful. The exact formula as stated by Gemini should not be marked proved, but the idea of replacing the length-$X$ sawtooth sum with a balanced hyperbola decomposition is correct and should become the main Round 2 task. Gemini's review also correctly flags the analytic cost of applying Vaaler directly to the unbalanced $d\le X$ identity.

Gemini's "character blindness"warning is worth preserving as a gap: after reduction to exponential sums, one must know whether $\chi_4$ is actually being exploited or merely discarded by absolute values. However, this warning needs to be converted into precise coefficient classes and estimates.

**From `gpt_pro_thinking` Stage B review:**

The review correctly demotes Gemini's exact hyperbola formula from "proved"to "proposed."It also gives the right next-step decomposition: split the hyperbola assertion into smaller lemmas H1--H4, separating exact counting, periodic partial sums, main-term cancellation, and Vaaler truncation.

Rejected or risky ideas:

1. **Reject as proved: Gemini's exact hyperbola formula.**
   The formula

$$
E(R)
=
-4\sum_{a\le R}\chi_4(a)\psi(R^2/a)
+
4\sum_{b\le R}
\left[
\psi\left(\frac{R^2/b+1}{4}\right)
-
\psi\left(\frac{R^2/b+3}{4}\right)
\right]
+
O(1)
$$

is plausible in spirit, but it was not proved in Round 1. It must be derived from an exact hyperbola identity with $y=\lfloor \sqrt X\rfloor$, explicit endpoint conventions, and a verified bounded residual.

2. **Reject: "nonzero Hessian unlocks modern decoupling"as a theorem.**
   For the phase

$$
\Phi(h,d)=\frac{hX}{d},
$$

the formal Hessian determinant in continuous variables is nonzero. That calculation is correct, but it does not by itself imply that Bourgain--Watt, Bombieri--Iwaniec, or any decoupling theorem applies. The needed theorem, coefficient hypotheses, dyadic ranges, spacing conditions, and loss factors must be stated.

3. **Reject: abandoning Bessel methods entirely.**
   The Bessel route is risky as a direct source of new exponents because of radial degeneracy. It is still useful for smoothing, unsmoothing, checking notation, and recovering the classical $R^{2/3}$ sanity bound.

4. **Reject: "smoothing artificially erases point-mass spikes."**
   Smoothing without an unsmoothing argument is dangerous. Standard smoothing with a sandwich lemma is legitimate and should remain in the technical toolkit.

5. **Treat as risky: the radial benchmark $A_M(R)\ll M^{3/2}R^\epsilon$.**
   It is a clean sufficient condition, but not a near-term lemma. The Hessian warning suggests that generic two-dimensional nondegenerate tools are unavailable for this raw radial phase.

Known gaps:

1. **Endpoint conventions for $\psi$.**
   The identity

$$
\lfloor t\rfloor=t-\psi(t)-\frac12
$$

is exact if $\psi(t)=t-\lfloor t\rfloor-\frac12$, including $\psi(n)=-1/2$ at integers. Fourier series and Vaaler approximations usually behave differently at discontinuities. This must be recorded explicitly.

2. **Exact symmetric hyperbola identity.**
   The repo needs a proved identity for

$$
T(X)=\sum_{ab\le X}\chi_4(a)
$$

with $y=\lfloor\sqrt X\rfloor$:

$$
T(X)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y),
$$

where

$$
S(u)=\sum_{a\le u}\chi_4(a).
$$

3. **Periodic partial-sum formula.**
   One needs a fully checked formula for $S(u)$, for real $u$, including integer endpoints. A likely exact formula is

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
- \left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right),
$$

with the same floor-compatible convention for $\psi$.

4. **Main-term cancellation after the symmetric cut.**
   After substituting the floor and $S(u)$ formulas, the nonoscillatory terms must be shown to equal $\pi X/4+O(1)$ at the level of $T(X)$. This is the critical algebraic step behind Gemini's proposed formula.

5. **Vaaler truncation error.**
   The truncation error must be derived with full dependence on the length $D$, Fourier height $H$, and endpoint/jump terms. The heuristic "error is length divided by $H$"is not enough.

6. **Dyadic parameter map.**
   The route needs a precise map from the hyperbola formula to dyadic ranges $D,H,T$, with $T=X$, $D\le X^{1/2}$, and $H$ chosen according to the actual Vaaler error. This must precede any appeal to Bombieri--Iwaniec-type estimates.

7. **Coefficient handling.**
   The role of $\chi_4(d)$ must be explicit. The repo should distinguish estimates that exploit the character from estimates that merely bound $|c_d|\le 1$.

8. **Literature audit.**
   Record-exponent claims should be audited from primary sources before being treated as dependencies.

New lemmas to add:

**Lemma H1: Exact symmetric hyperbola identity.**
Status: proposed, expected standard.

For $X\ge 1$, set $y=\lfloor\sqrt X\rfloor$ and

$$
S(u)=\sum_{1\le a\le u}\chi_4(a).
$$

Then

$$
\sum_{ab\le X}\chi_4(a)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

This should be proved by covering the region $ab\le X$ by the union of $a\le y$ and $b\le y$, noting that no pair with $a>y$ and $b>y$ can satisfy $ab\le X$.

**Lemma H2: Exact periodic formula for $S(u)$.**
Status: proposed, elementary.

For real $u\ge 0$,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
- \left\lfloor\frac{u+1}{4}\right\rfloor.
$$

Equivalently, with $\psi(t)=t-\lfloor t\rfloor-\frac12$,

$$
S(u)
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right).
$$

Endpoint conventions must be checked at $u\in\mathbb Z$ and at $u\equiv 1,3\pmod 4$.

**Lemma H3: Balanced sawtooth formula.**
Status: proposed, not proved.

For $X=R^2\ge 1$, $y=\lfloor\sqrt X\rfloor$, and $P(X)=N(\sqrt X)-\pi X$,

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
O(1).
$$

This is the corrected version of Gemini's proposed formula, with $a,b\le y=\lfloor\sqrt X\rfloor$ rather than informal $a,b\le R$. It must not be marked proved until the $O(1)$ residual is derived.

**Lemma H4: Vaaler truncation for balanced hyperbola sums.**
Status: proposed technical target.

For truncation height $H$, express each sawtooth term in H3 as a finite Fourier sum plus a controlled residual. The output should have the schematic form

$$
P(X)
=
\sum_{1\le |h|\le H}\alpha_h
\sum_{a\le y}\chi_4(a)e(hX/a)
+
\sum_{1\le |h|\le H}\beta_h
\sum_{b\le y}
\left[
e\left(\frac{h(X/b+1)}{4}\right)
-
e\left(\frac{h(X/b+3)}{4}\right)
\right]
+
\mathcal E(X,H),
$$

where $\alpha_h,\beta_h\ll 1/|h|$, and $\mathcal E(X,H)$ is explicitly bounded.

**Lemma H5: Dyadic exponential-sum criterion.**
Status: target.

Find explicit conditions on dyadic estimates of the form

$$
\sum_{h\sim H_0}\frac{1}{h}
\sum_{d\sim D}c_d e(hX/d)
$$

that imply

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

This criterion should state the allowed ranges of $D,H_0$, the coefficient class $c_d$, and the loss permitted after summing over dyadic blocks.

**Lemma B1: Smoothed Poisson--Bessel sanity check.**
Status: standard/proposed for proof.

For a fixed smooth compactly supported radial mollifier $\rho$, prove the smoothed Poisson--Bessel formula and sandwich inequality, then recover

$$
E(R)\ll R^{2/3}
$$

from the trivial bound on dyadic radial sums. This is not the selected main route but should be retained as a calibration test.

Counterexample checks to run:

1. **Boundary test for H1--H3.**
   Check $X$ in the following classes:

* $0<X<1$,
   * $X=1,2,3,4,5$,
   * $X=n$ a square,
   * $X=n$ not a square,
   * $X$ noninteger near an integer,
   * $R=\sqrt X$ integer and noninteger.

2. **Endpoint convention test for $\psi$.**
   Compare the floor-compatible $\psi(t)=t-\lfloor t\rfloor-1/2$ with the Fourier-centered sawtooth convention at integer arguments. Record exactly where each convention is used.

3. **Numerical test of Gemini's proposed formula.**
   Compute

$$
E(R)-\left[
-4\sum_{a\le \lfloor R\rfloor}\chi_4(a)\psi(R^2/a)
+
4\sum_{b\le \lfloor R\rfloor}
\left(
\psi\left(\frac{R^2/b+1}{4}\right)
-
\psi\left(\frac{R^2/b+3}{4}\right)
\right)
\right]
$$

for many $R$ and verify whether it is uniformly bounded.

4. **Unbalanced versus balanced Vaaler cost.**
   Estimate the residual size when Vaaler is applied to $d\le X$ versus after the hyperbola cut $d\le X^{1/2}$. This should be done symbolically and numerically.

5. **Radial phase false-start guardrail.**
   Record that the Hessian determinant of $R\sqrt{x^2+y^2}$ vanishes. Any future claim using generic full-rank two-dimensional stationary phase on this phase should be automatically flagged.

6. **Character-blindness check.**
   For each proposed exponential-sum estimate, mark whether it uses cancellation from $\chi_4$ or only the bound $|\chi_4|\le 1$.

Next round instructions:

**For `gemini_deep_think`:**

Reformulate "character blindness"as a precise dyadic estimate. Specify the coefficient class, the dyadic ranges, and what bound would be needed to reach $X^{1/4+\epsilon}$. Avoid claims that nonzero Hessian alone implies decoupling applicability.

**For `gpt_pro_thinking`:**

Write the unified Round 2 reading packet: arithmetic hyperbola as the selected main route, Bessel smoothing as a calibration route, and the exact gap list H1--H5. Include a short literature-audit checklist for Huxley, Bourgain--Watt, Li--Yang, and ANTEDB.

Confidence:

High confidence in selecting the **balanced arithmetic hyperbola/sawtooth route** as the main Round 2 direction.

High confidence that the Poisson--Bessel route remains useful for smoothing, unsmoothing, and the $R^{2/3}$ sanity check.

Moderate confidence that Gemini's balanced formula is correct up to $O(1)$ after endpoint repair; it still requires proof.

Low confidence that formal Hessian nondegeneracy of $\Phi(h,d)=hX/d$ is enough to invoke modern decoupling or Bombieri--Iwaniec estimates without substantial additional work.

Overall Round 1 judgment: productive, but no theorem improving the Gauss circle bound has been proved. The next round should verify the arithmetic foundation before attempting any high-powered exponential-sum estimate.

## Round 2 Update

Timestamp: 2026-05-31 23:34:11

See `rounds/web-research-test/round_002/judge/judge.md`.

Selected main route:

Continue with the **balanced arithmetic hyperbola/sawtooth route as the main analytic route**, and retain the **smoothed Poisson--Bessel route only as a calibration route**. The active Round 2 judge prompt asks for a Stage C synthesis with selected route, useful fragments, rejected ideas, gaps, lemmas, counterexample checks, next-round tasks, and confidence.

The selected proof skeleton is:

$$
N(\sqrt X)-\pi X
\longrightarrow
\text{symmetric hyperbola identity}
\longrightarrow
\text{balanced sawtooth formula}
\longrightarrow
\text{finite Vaaler expansion}
\longrightarrow
\text{character-aware reciprocal sums}.
$$

Here

$$
X=R^2,\qquad P(X)=N(\sqrt X)-\pi X,
$$

and the target is

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Round 2 made real checkable progress: H1 and H2 should be promoted to **proved**; H3 should be promoted to **plausibly proved / pending independent endpoint audit**; H4 and H5 should be rewritten to incorporate the Leg 2 character transfer

$$
e(h/4)-e(3h/4)=2i\chi_4(h).
$$

No improvement to the Gauss circle exponent has been proved. The result of Round 2 is a cleaner reduction and a sharper target.

Useful fragments by source:

**From `gpt_pro_thinking`:**

The main useful contribution is the explicit derivation of the balanced sawtooth formula. With

$$
\chi=\chi_4,\qquad
T(X)=\sum_{ab\le X}\chi(a),\qquad
S(u)=\sum_{1\le a\le u}\chi(a),\qquad
y=\lfloor X^{1/2}\rfloor,
$$

Round 2 derived

$$
T(X)
=
\sum_{a\le y}\chi(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

It also used

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
- \left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right),
$$

with the floor-compatible convention

$$
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

The derived oscillatory part is

$$
W(X)
=
-4\sum_{a\le y}\chi(a)\psi(X/a)
+
4\sum_{b\le y}
\left[
\psi\left(\frac{X/b+1}{4}\right)
-
\psi\left(\frac{X/b+3}{4}\right)
\right].
$$

The exact residual was isolated as

$$
P(X)-W(X)
=
1+
4X\left(\sum_{a\le y}\frac{\chi(a)}{a}-\frac{\pi}{4}\right)
+
2y-2S(y)-4yS(y).
$$

Using the four-case tail estimate

$$
L(1,\chi_4)-\sum_{a\le y}\frac{\chi(a)}{a}
=
\frac{1-2S(y)}{2y}
+
O(y^{-2}),
$$

this gives $P(X)-W(X)=O(1)$ after checking small $y$ and endpoint cases. The uploaded Round 2 material explicitly identifies this residual calculation and the Fejer-weighted Vaaler residual as the major rigorous contribution.

The second useful contribution is the correction that Vaaler truncation does **not** leave only a scalar $O(y/H)$ error. The residual contains Fejer-weighted reciprocal exponential sums of essentially the same type as the main sums, so those residuals must be included in H4/H5. This prevents a standard false proof pattern.

**From `gemini_deep_think`:**

The most useful contribution is the Leg 2 character transfer. In the formal Fourier expansion,

$$
\psi\left(\frac{X/b+1}{4}\right)
-
\psi\left(\frac{X/b+3}{4}\right)
$$

produces the coefficient

$$
e(h/4)-e(3h/4)
=
2i\sin(\pi h/2)
= 2i\chi_4(h).
$$

Thus Leg 1 carries $\chi_4(a)$ on the spatial variable, while Leg 2 carries $\chi_4(h)$ on the frequency variable. The Round 2 review correctly says H4/H5 should be updated to record this rather than treating the second leg as a generic bounded coefficient.

Gemini also correctly withdrew the earlier overclaim that nonzero Hessian alone supplies a decoupling theorem. The continuous phase $\Phi(h,d)=hX/d$ has local nondegeneracy, but global rational collisions and spacing obstructions remain the real Bombieri--Iwaniec difficulty.

**From `gpt_pro_thinking` Stage B review:**

The most useful synthesis is to split H5 into two distinct target families rather than one generic coefficient class. It also correctly downgrades Gemini's "character-blindness barrier"from "proved theorem"to " diagnostic obstruction heuristic."
Rejected or risky ideas:

1. **Reject: H6 as a proved theorem.**
   The claim that every character-blind method strictly requires the Exponent Pair Conjecture is not proved. It is a useful warning about one natural exponent-pair calculation, but it does not rule out all large-sieve, bilinear, spacing, or decoupling variants. Keep H6 only as a diagnostic heuristic. The Stage B review explicitly flags this overclaim.

2. **Reject: "H$ must be exactly $X^{1/4+\epsilon}$."**
   The correct statement is that $H$ must be at least about $X^{1/4}$ if the zeroth-order Vaaler residual $X^{1/2}/H$ is to be at the conjectural scale. Larger $H$ may be allowed, but it enlarges the frequency range and changes the analytic target.

3. **Reject: treating the two character placements as analytically identical.**
   Leg 1 has a spatial character:

$$
   \sum_{a\sim D}\chi_4(a)e(hX/a).
$$

Leg 2 has a frequency character:

$$
   \sum_{h\sim H_0}\chi_4(h)u_h
   \sum_{b\sim D}e(hX/(4b)).
$$

These are not interchangeable under Cauchy--Schwarz, differencing, completion, or spacing estimates. The Stage B review explicitly warns against collapsing them into a single "symmetric"estimate.

4. **Reject: "exploit Deligne/Weil"from $\chi_4(a)\chi_4(a+q)$ without a complete-sum formulation.**
   Since $\chi_4$ has modulus $4$, shifted products are often just periodic patterns. There may be useful arithmetic structure, but not a deep complete-sum gain until an actual complete sum and modulus are specified.

5. **Reject: generic full-rank stationary phase on the geometric Bessel phase.**
   The earlier guardrail remains: do not apply generic full-rank two-dimensional stationary phase to $R|k|$ or $R\sqrt{ab}$. The Bessel route remains useful for smoothing and the classical $R^{2/3}$ calibration, not as the selected route to a new exponent.

6. **Reject: current-record claims without audit.**
   Li--Yang's arXiv abstract states that their improvement uses Bombieri--Iwaniec, a new first-spacing estimate, and Huxley's second-spacing results. ([arXiv][1]) ANTEDB is a living database for analytic-number-theory exponents, so record-status claims should remain in the literature-audit queue rather than be treated as permanent facts. ([Teorth][2])

Known gaps:

1. **H3 endpoint audit.**
   The balanced sawtooth formula is strongly supported, but before marking it proved in the public lemma bank, the repo should verify all endpoint conventions: $X$ integer, $X$ noninteger near an integer, $X=n^2$, $X=n^2\pm\eta$, and small $y$. The Fourier-centered sawtooth and floor-compatible sawtooth differ at discontinuities.

2. **Exact four-case Gregory tail estimate.**
   The needed estimate

$$
   L(1,\chi_4)-\sum_{a\le y}\frac{\chi_4(a)}{a}
=
\frac{1-2S(y)}{2y}+O(y^{-2})
$$

should be written as an explicit four-case lemma for $y\equiv 0,1,2,3\pmod 4$, with a uniform constant.

3. **Finite Vaaler polynomial conventions.**
   The formal infinite Fourier series gives the clean Leg 2 character transfer. A finite Vaaler polynomial has modified coefficients and a residual majorant. The exact statement must distinguish:

* main Vaaler coefficients;
   * jump/discontinuity behavior;
   * Fejer majorant terms;
   * whether the Leg 2 factor remains exactly $2i\chi_4(h)$ in every nonzero main coefficient.

4. **Fejer residual estimates.**
   The residual is not only $O(X^{1/2}/H)$. It also contains nonzero-frequency sums. The next H5 must include estimates for these residual-weighted sums, or explicitly prove that they are dominated by H5a/H5b.

5. **Dyadic criterion strength.**
   The target

$$
   B_i(H_0,D;X)\ll_\epsilon H_0X^{1/4+\epsilon}
$$

is sufficient but likely very strong. The repo must compare it against known Bombieri--Iwaniec and Li--Yang parameter ranges rather than assuming it is reachable. Li--Yang's stated result improves both the Gauss circle and divisor problems through a new first-spacing estimate combined with Huxley's second-spacing work. ([arXiv][1])

6. **Character exploitation.**
   Every future estimate must be labelled:

* character-aware;
   * character-blind;
   * character only in an $\ell^2$ norm;
   * character used through congruence or correlation structure.

7. **Bessel calibration route.**
   The smoothed Poisson--Bessel formula, sandwich/unsmoothing lemma, and $R^{2/3}$ sanity check should still be proved in the repo, but this remains a secondary track.

New lemmas to add:

**H1. Exact symmetric hyperbola identity.**
Status: proved.

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$, and

$$
S(u)=\sum_{1\le a\le u}\chi_4(a),
$$

one has

$$
\sum_{ab\le X}\chi_4(a)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

Proof: the region $ab\le X$ is covered by $a\le y$ and $b\le y$, because $a>y$ and $b>y$ imply $ab>(y+1)^2>X$. The overlap is $a\le y$, $b\le y$, contributing $yS(y)$.

**H2. Exact periodic formula for $S(u)$.**
Status: proved.

For real $u\ge 0$,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
- \left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right),
$$

where $\psi(t)=t-\lfloor t\rfloor-\frac12$.

**H3. Balanced sawtooth formula.**
Status: plausibly proved; pending independent endpoint audit.

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$,

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
O(1).
$$

The exact residual before the final $O(1)$ bound is

$$
P(X)-W(X)
=
1+
4X\left(\sum_{a\le y}\frac{\chi_4(a)}{a}-\frac{\pi}{4}\right)
+
2y-2S(y)-4yS(y).
$$

This should be placed in the best proof draft with a warning: "not final until small cases and discontinuities are checked."
**H4. Finite Vaaler expansion with dual-character bookkeeping.**
Status: proposed technical lemma.

For a valid finite Vaaler approximation,

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
\mathcal R_H(t),
\qquad
\alpha_h\ll \frac1{|h|},
$$

the main terms from H3 are

$$
\sum_{1\le |h|\le H}\alpha_h
\sum_{a\le y}\chi_4(a)e(hX/a)
$$

and

$$
\sum_{1\le |h|\le H}\alpha_h
\left(e(h/4)-e(3h/4)\right)
\sum_{b\le y}e(hX/(4b)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the second main family is frequency-character-twisted. The residual $\mathcal R_H$ must be expanded or bounded with Fejer terms, not discarded as a scalar $O(y/H)$.

**H5a. Spatial-character dyadic target.**
Status: sufficient target, not known.

For $D\le X^{1/2}$, $H_0\le H$, smooth dyadic $w$, and $|u_h|\le 1$, define

$$
B_1(H_0,D;X)
=
\sum_{h\sim H_0}u_h
\sum_{a\sim D}\chi_4(a)w(a/D)e(hX/a).
$$

A sufficient target is

$$
B_1(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

**H5b. Frequency-character dyadic target.**
Status: sufficient target, not known.

Define

$$
B_2(H_0,D;X)
=
\sum_{h\sim H_0}u_h\chi_4(h)
\sum_{b\sim D}w(b/D)e(hX/(4b)).
$$

A sufficient target is

$$
B_2(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

This is not the same analytic problem as H5a.

**H5r. Fejer-residual dyadic variants.**
Status: required target family.

For the Fejer residual coefficients from Vaaler, formulate parallel dyadic estimates. These may have weights of size $O(1/H)$ rather than $O(1/h)$ and may require absolute values outside some inner sums. The next round should state them exactly.

**H6. Character-blindness diagnostic.**
Status: obstruction heuristic, not proved.

A method is character-blind if, after dyadic decomposition, it replaces $\chi_4(a)$ or $\chi_4(h)$ by coefficient bounds and estimates only untwisted reciprocal phases. Such a method should not be accepted as a route to $X^{1/4+\epsilon}$ unless it states a theorem strong enough to handle the corresponding untwisted divisor-type reciprocal sums. This preserves Gemini's useful warning without asserting a universal impossibility theorem.

**B1. Poisson--Bessel calibration lemma.**
Status: secondary route.

Prove the smoothed Poisson--Bessel formula, the smoothing/unsmoothing sandwich, and the classical $E(R)\ll R^{2/3}$ estimate from trivial radial-sum bounds. This remains a calibration test, not the selected new-exponent route.

Counterexample checks to run:

1. **H3 exact-residual test.**
   Compute $P(X)-W(X)$ and the explicit residual formula for:

* $0<X<1$;
   * $X=1,2,3,4,5$;
   * integer squares;
   * integer nonsquares;
   * $X=n^2\pm 10^{-k}$;
   * $X$ just below and just above an integer.

2. **Sawtooth convention test.**
   Compare the floor-compatible convention

$$
   \psi(t)=t-\lfloor t\rfloor-\frac12
$$

against the Fourier midpoint convention at integer arguments. Record exactly where the finite Vaaler approximation differs.

3. **Leg 2 Fourier transfer test.**
   Verify for finite Vaaler coefficients that the main coefficient factor is exactly

$$
   e(h/4)-e(3h/4)=2i\chi_4(h),
$$

and identify which parts of the residual do or do not inherit the same character factor.

4. **Fejer-residual stress test.**
   Numerically evaluate the Fejer residual sums for structured $X$, especially squares and near-squares, to check whether bounding them by the main H5a/H5b criterion is plausible.

5. **Character-aware versus character-blind test.**
   For each candidate estimate, produce two versions:

* with $\chi_4$ retained;
   * with $|\chi_4|\le 1$ substituted.

Compare the resulting predicted exponent in the critical range $D\sim X^{1/2}$, $H_0\sim X^{1/4}$.

6. **A-process caution test.**
   If applying Weyl differencing to

$$
   \sum_a\chi_4(a)e(f(a)),
$$

compute the shifted character product

$$
   \chi_4(a)\chi_4(a+q)
$$

explicitly by $q\pmod 4$. Do not claim Deligne/Weil-type cancellation unless a genuine complete-sum problem appears.

Next round instructions:

**For `gemini_deep_think`:**

Rewrite H6 as a diagnostic obstruction, not a theorem. Redo the exponent-pair scaling using a precisely named exponent-pair theorem and the standard parameter convention for $f(d)=hX/d$. State what the calculation proves and what it does not prove.

**For `gpt_pro_thinking`:**

Update the reading packet and best proof draft with H1, H2, H3, H4, H5a, H5b, H5r, and H6 as classified above. Then compare H5a/H5b/H5r with the actual Bombieri--Iwaniec and Li--Yang first-spacing framework. The audit should identify whether the current H5 targets are stronger than known technology, equivalent to a known spacing estimate, or malformed.

Confidence:

High confidence in the selected route: balanced arithmetic hyperbola plus Vaaler plus character-aware reciprocal sums.

High confidence in H1 and H2.

Moderate-to-high confidence in H3, conditional on endpoint and small-case audit.

Moderate confidence in the Leg 2 character transfer for the main Fourier terms.

Low confidence that the present H5a/H5b targets are reachable by known methods without substantial new input.

No exponent improvement has been proved in Round 2. The concrete gain is a cleaner, balanced reduction and a more accurate analytic target.

[1]: https://arxiv.org/abs/2308.14859?utm_source=chatgpt.com "An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem"
[2]: https://teorth.github.io/expdb/?utm_source=chatgpt.com "Analytic Number Theory Exponent Database"

## Round 3 Update

Timestamp: 2026-06-01 03:40:56

See `rounds/web-research-test/round_003/judge/judge.md`.

# Selected main route

Continue the **balanced arithmetic hyperbola/sawtooth route** as the main analytic route. Retain the smoothed Poisson--Bessel route only as a calibration route for smoothing, unsmoothing, and recovery of the classical $R^{2/3}$-scale sanity check.

The active Round 3 prompt asks for a Stage C judge synthesis and restricts this run to two active agents, `gpt_pro_thinking` and `gemini_deep_think`; older references to inactive agents should be ignored as historical state noise.

The current proof skeleton is:

$$
P(X)=N(\sqrt X)-\pi X
\longrightarrow
\text{symmetric hyperbola}
\longrightarrow
\text{floor-compatible sawtooth}
\longrightarrow
\text{finite Vaaler}
\longrightarrow
\text{local dyadic reciprocal sums}.
$$

The target remains:

$$
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

equivalently

$$
E(R)\ll_\epsilon R^{1/2+\epsilon}.
$$

Round 3 makes one real promotion and one strategic correction:

1. **Promote H7 to proved.** The shifted product $\chi_4(d)\chi_4(d+q)$ degenerates to a parity-supported constant after a direct A-process. This is an explicit algebraic obstruction.

2. **Downgrade H6.** The one-dimensional exponent-pair obstruction is useful, but only as a conditional diagnostic. The inequality $p+2q\le 1$ should not be entered as final until the exponent-pair normalization is fixed. Under the standard reciprocal-phase scaling $T\asymp hX/D$, the endpoint calculation instead gives the condition $3p+2q\le 1$.

No improvement to the Gauss circle exponent has been proved. The concrete Round 3 gain is a sharper obstruction map around the character $\chi_4$ and a better local dyadic target.

# Useful fragments by source

## From `gpt_pro_thinking`

The main useful contribution is the completed balanced reduction. The current state now supports treating H1, H2, and H3 as proved floor-compatible identities, with numerical checks still useful as guardrails.

Let

$$
\chi=\chi_4,\qquad
T(X)=\sum_{ab\le X}\chi(a),\qquad
S(u)=\sum_{1\le a\le u}\chi(a),\qquad
y=\lfloor X^{1/2}\rfloor.
$$

Then

$$
N(\sqrt X)=1+4T(X),
$$

and

$$
T(X)
=
\sum_{a\le y}\chi(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

Also,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
- \left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right),
$$

where

$$
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

Thus the oscillatory part is

$$
W(X)
=
-4\sum_{a\le y}\chi(a)\psi(X/a)
+
4\sum_{b\le y}
\left[
\psi\left(\frac{X/b+1}{4}\right)
-
\psi\left(\frac{X/b+3}{4}\right)
\right].
$$

The exact residual is

$$
P(X)-W(X)
=
1+
4X\left(\sum_{a\le y}\frac{\chi(a)}a-\frac{\pi}{4}\right)
+
2y-2S(y)-4yS(y).
$$

The four-case Gregory-tail estimate

$$
L(1,\chi_4)-\sum_{a\le y}\frac{\chi(a)}a
=
\frac{1-2S(y)}{2y}
+
O(y^{-2})
$$

then gives

$$
P(X)-W(X)=O(1).
$$

This is the current best exact arithmetic foundation.

The second useful contribution is the **local Vaaler cutoff**. For a dyadic denominator block $d\sim D$, the zeroth-order Vaaler residual is $D/H_D$. To keep it at the conjectural scale $X^{1/4}$, choose

$$
H_D\asymp D X^{-1/4}
$$

for

$$
X^{1/4}\le D\le X^{1/2}.
$$

Blocks with $D<X^{1/4}$ are already short enough for separate treatment. This local range is now preferred over a global $H\le X^{1/4}$ range. The Round 3 review explicitly recommends replacing the global H5 range by this local cutoff and adding H5r for Fejer residuals.

## From `gemini_deep_think`

Gemini's strongest Round 3 contribution is **H7: A-process modulus degeneracy for $\chi_4$**. After Weyl differencing,

$$
\chi_4(d)\chi_4(d+q)
=
\begin{cases}
1_{2\nmid d},& q\equiv 0\pmod 4,\
-1_{2\nmid d},& q\equiv 2\pmod 4,\
0,& q\equiv 1,3\pmod 4.
\end{cases}
$$

This is algebraically correct. It means a direct A-process destroys the nontrivial mod-$4$ oscillation and leaves only a parity restriction. Gemini's own output states that this collapse is conditional on applying the A-process directly to the spatial variable before dualization or summation over $h$.

Gemini's second useful contribution is the softened H6 diagnostic: if a method first takes absolute values over $h$, then applies only a one-dimensional exponent-pair bound to the inner $d$-sum, it is unlikely to reach the conjectural endpoint. The useful part is the hypothesis list: absolute values over $h$, one-dimensional treatment of $d$, and no two-variable cross-cancellation. The overclaim is the specific inequality and any universal conclusion.

Gemini's third useful contribution is the **B-process-first escape route**. Since H7 only blocks A-process-first methods, one possible next route is to apply twisted Poisson/B-process to the $\chi_4(d)$-twisted spatial sum before differencing, and then check whether $\chi_4$ becomes a Gauss-sum factor in the dual variable. This is proposed, not proved.

## Literature calibration

Li--Yang's paper states that it improves both the Gauss circle and Dirichlet divisor problems using the Bombieri--Iwaniec method, with a new first-spacing estimate combined with Huxley's second-spacing results. It proves $R(X),\Delta(X)=O_\epsilon(X^{\theta^*+\epsilon})$ with $\theta^*=0.3144831759741\ldots$, while the conjectural target is $\theta=1/4$.

ANTEDB records Li--Yang 2023 as the current sharpest listed two-dimensional Gauss-circle upper bound, $\theta_2^{\operatorname{Gauss}}\le 2\alpha$ with $\alpha=0.31448\ldots$, and lists Huxley 2003 at $131/208$ in $R$-notation. ([Teorth][1])

# Rejected or risky ideas

1. **Reject H6 as a proved theorem.**
   H6 should not say "character-blind methods require $p+2q\le 1$"as a final theorem. That condition depends on the exponent-pair convention. Under the standard convention for $f(d)=hX/d$ with derivative scale $T\asymp hX/D$, an exponent pair $(p,q)$ gives

$$
   \sum_{d\sim D}e(hX/d)\ll (hX/D)^pD^q.
$$

At the endpoint $D\asymp X^{1/2}$ and $h\asymp X^{1/4}$ this is

$$
   X^{3p/4+q/2}.
$$

Since the raw dyadic target permits only $X^{1/4+\epsilon}$ for the inner sum after trivial $h$-summation, the condition becomes

$$
   3p+2q\le 1.
$$

This still forces endpoint-level strength, but the lemma bank must use a named theorem and a fixed normalization.

2. **Reject H7 as a universal impossibility theorem.**
   H7 proves only that **A-process first** destroys the $\chi_4$ oscillation. It does not rule out B-process-first, residue interference, two-dimensional spacing, double large sieve, VMVT-type estimates, or completion methods.

3. **Reject "B-process first is mandatory"as a theorem.**
   B-process first is now a serious proposed route, but no transformed sum has yet been written with exact ranges, Gauss factors, or stationary phase. It belongs in the gap register as H8, not in the proved lemma bank.

4. **Reject scalar Vaaler residuals.**
   The finite Vaaler residual is not merely $O(D/H_D)$. The Fejer majorant contributes nonzero-frequency reciprocal sums. Any proof skeleton that omits H5r is incomplete.

5. **Reject "residue splitting proves no advantage"as a theorem.**
   Splitting $\chi_4(d)$ into $d\equiv 1,3\pmod 4$ often converts H5a into a finite combination of Li--Yang-type reciprocal sums. This suggests limited character advantage, but it does not prove impossibility. Interference between residue-class sums may still matter.

6. **Reject Deligne/Weil claims from shifted $\chi_4$ products.**
   Since H7 shows the shifted product is just $0,\pm 1$ on parity sublattices, there is no deep complete character sum at that stage. Any Weil/Deligne claim must first exhibit a genuine complete sum with a nontrivial modulus.

# Known gaps

1. **Finite Vaaler theorem with floor-compatible discontinuities.**
   H3 is an exact identity for the floor-compatible sawtooth. The finite Fourier/Vaaler approximation uses centered trigonometric conventions. The next proof draft must state precisely how discontinuity points are handled.

2. **Exact H5r residual formulation.**
   The Fejer residual terms must be written explicitly, not schematically. The main open question is whether the residual can be dominated by the same H5a/H5b estimates, or whether it forces absolute values that activate the H6 diagnostic.

3. **B-process-first transformation.**
   H8 needs a concrete formula. The next step is to transform

$$
   \sum_{d\sim D}\chi_4(d)w(d/D)e(hX/d)
$$

by a twisted Poisson/B-process step, identify the dual phase, identify any Gauss-sum factor, and record the resulting dual length and derivative scales.

4. **Li--Yang dictionary.**
   The repository needs a precise dictionary from the local H5 ranges

$$
   X^{1/4}\le D\le X^{1/2},
   \qquad
   H_0\le D X^{-1/4}
$$

to Li--Yang's double sums of the form

$$
   \sum_{h\sim H}\sum_{m\sim M} e(-hT/m)
$$

and their more general $F(m/M)$ setup. Li--Yang explicitly identify such reciprocal double sums as typical for the circle and divisor problems.

5. **Known-technology gap.**
   Li--Yang reaches $\theta^*=0.314483\ldots$, not $\theta=1/4$. The current H5 target is therefore stronger than what has been established by existing Li--Yang technology. Any claim that H5 is "available"must specify a new first-spacing, second-spacing, or orthogonality improvement.

6. **Bessel calibration still absent.**
   The Poisson--Bessel route remains secondary, but the repo should still contain a clean proof of the smoothed formula, sandwich/unsmoothing lemma, and $R^{2/3}$ sanity check.

7. **Numerical stress tests still missing.**
   H3 has an explicit proof, but boundary tests should still be run to prevent transcription or convention errors.

# New lemmas to add

## H1. Exact symmetric hyperbola identity

**Status: proved.**

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$, and

$$
S(u)=\sum_{1\le a\le u}\chi_4(a),
$$

one has

$$
\sum_{ab\le X}\chi_4(a)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

Proof: every pair $(a,b)$ with $ab\le X$ has $a\le y$ or $b\le y$, since $a,b>y$ implies $ab>(y+1)^2>X$. The overlap is the rectangle $a\le y$, $b\le y$.

## H2. Exact periodic formula for $S(u)$

**Status: proved.**

For real $u\ge 0$,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
- \left\lfloor\frac{u+1}{4}\right\rfloor.
$$

Equivalently,

$$
S(u)
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right),
$$

with

$$
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

## H3. Balanced sawtooth formula

**Status: proved as an $O(1)$ floor-compatible identity.**

For $X\ge 1$,

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

where $y=\lfloor X^{1/2}\rfloor$.

The proof goes through the exact residual

$$
P(X)-W(X)
=
1+
4X\left(\sum_{a\le y}\frac{\chi_4(a)}a-\frac{\pi}{4}\right)
+
2y-2S(y)-4yS(y),
$$

and the four-case tail estimate

$$
L(1,\chi_4)-\sum_{a\le y}\frac{\chi_4(a)}a
=
\frac{1-2S(y)}{2y}+O(y^{-2}).
$$

## H4. Finite Vaaler with dual-character bookkeeping

**Status: proposed technical lemma.**

For each dyadic block $d\sim D$, choose

$$
H_D\asymp D X^{-1/4}
$$

when $D\ge X^{1/4}$.

For a finite Vaaler main polynomial

$$
\psi(t)=\sum_{1\le |h|\le H_D}\alpha_h e(ht)+\mathcal R_{H_D}(t),
\qquad
\alpha_h\ll |h|^{-1},
$$

the first leg contributes main terms

$$
\sum_{1\le |h|\le H_D}\alpha_h
\sum_{a\sim D}\chi_4(a)w(a/D)e(hX/a).
$$

The second leg contributes main terms

$$
\sum_{1\le |h|\le H_D}
\alpha_h
\left(e(h/4)-e(3h/4)\right)
\sum_{b\sim D}w(b/D)e(hX/(4b)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the second main family is frequency-character-twisted. The residual $\mathcal R_{H_D}$ must be handled separately.

## H5a. Spatial-character local dyadic target

**Status: sufficient target, not known.**

For

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le D X^{-1/4},
$$

define

$$
B_1(H_0,D;X)
=
\sum_{h\sim H_0}u_h
\sum_{d\sim D}\chi_4(d)w(d/D)e(hX/d),
\qquad |u_h|\le 1.
$$

A sufficient target is

$$
B_1(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

## H5b. Frequency-character local dyadic target

**Status: sufficient target, not known.**

For the same range,

$$
B_2(H_0,D;X)
=
\sum_{h\sim H_0}u_h\chi_4(h)
\sum_{d\sim D}w(d/D)e(hX/(4d)).
$$

A sufficient target is

$$
B_2(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

Equivalently, using

$$
\chi_4(h)=\frac{e(h/4)-e(3h/4)}{2i},
$$

this is a finite combination of phase-shifted reciprocal sums.

## H5r. Fejer-residual local dyadic target

**Status: required but not yet exact.**

The next round must derive the exact residual target from the chosen Vaaler theorem. The expected schematic form is:

$$
\frac{1}{H_D}
\sum_{H_0\le H_D}
\left|
\sum_{h\sim H_0}v_h
\sum_{d\sim D}c_d e(\lambda hX/d+\mu h)
\right|
\ll_\epsilon X^{1/4+\epsilon},
$$

with $c_d$ representing the spatial-character, residue-class, or untwisted coefficient classes arising from the two legs. This is only schematic until the exact Vaaler majorant is fixed.

## H6. Conditional one-dimensional exponent-pair diagnostic

**Status: diagnostic, not proved theorem.**

Assume a method bounds $B_1$ by taking absolute values over $h$ and applying a one-dimensional exponent-pair theorem to the inner $d$-sum. Under the standard reciprocal scaling $T\asymp hX/D$, the endpoint block

$$
D\asymp X^{1/2},
\qquad
H_0\asymp X^{1/4}
$$

requires

$$
3p+2q\le 1
$$

to reach the conjectural dyadic target.

If another exponent-pair convention is used, the inequality must be recomputed from the stated theorem. Do not record $p+2q\le 1$ as final without a named convention.

## H7. A-process modulus degeneracy for $\chi_4$

**Status: proved algebraic lemma.**

For every integer $q$,

$$
\chi_4(d)\chi_4(d+q)
=
\begin{cases}
1_{2\nmid d},& q\equiv 0\pmod 4,\
-1_{2\nmid d},& q\equiv 2\pmod 4,\
0,& q\equiv 1,3\pmod 4.
\end{cases}
$$

Corollary: Weyl differencing applied directly to the spatial-character sum removes the nontrivial mod-$4$ oscillation. This blocks naive claims of Weil/Deligne savings from shifted $\chi_4$ products. The Round 3 review independently identifies this as the key algebraic obstruction.

## H8. B-process-first character-dualization route

**Status: proposed.**

Before applying A-process or Cauchy--Schwarz, apply twisted Poisson/B-process to

$$
\sum_{d\sim D}\chi_4(d)w(d/D)e(hX/d).
$$

Required output:

1. exact transformed sum;
2. dual length;
3. dual phase;
4. Gauss-sum factor, if present;
5. comparison with H7;
6. comparison with Li--Yang/Bombieri--Iwaniec spacing hypotheses.

# Counterexample checks to run

1. **H3 boundary check.**
   Evaluate both sides of H3 for:

* $0<X<1$;
   * $X=1,2,3,4,5$;
   * integer squares;
   * integer nonsquares;
   * $X=n^2\pm 10^{-k}$;
   * $X$ just below and just above an integer.

2. **Sawtooth convention check.**
   Compare the floor-compatible value $\psi(n)=-1/2$ with the Fourier midpoint convention at discontinuities. Record exactly where Vaaler changes the value.

3. **Finite Vaaler residual check.**
   For several dyadic $D$, compute the zeroth-order residual $D/H_D$ and representative Fejer nonzero-frequency residual sums. Confirm whether H5r dominates them.

4. **H6 scaling check.**
   Recompute the endpoint condition under two conventions:

* $T\asymp hX/D$;
   * $\lambda\asymp hX/D^2$.

The lemma bank should contain only the version attached to a named exponent-pair theorem.

5. **H7 symbolic check.**
   Verify $\chi_4(d)\chi_4(d+q)$ for $q\bmod 4$ and $d\bmod 4$. This is simple but should be included as a permanent guardrail.

6. **B-process toy check.**
   Apply completion or Poisson summation to a compactly supported model sum

$$
   \sum_{d}\chi_4(d)w(d/D)e(hX/d)
$$

in a range where stationary phase is valid. Determine whether the dual sum genuinely avoids H7 or merely repackages the same parity restriction.

7. **Residue-class interference test.**
   Split

$$
   \sum_{d\sim D}\chi_4(d)e(hX/d)
$$

into $d=4m+1$ and $d=4m+3$. Determine whether any cancellation between the two residue classes survives standard absolute values or spacing reductions.

# Next round instructions

## For `gpt_pro_thinking`

Update the best proof draft and reading packet with the following status changes:

* H1, H2, H3: proved floor-compatible reductions.
* H4: proposed finite Vaaler lemma with dual-character bookkeeping.
* H5a/H5b: local dyadic targets with $H_0\le D X^{-1/4}$.
* H5r: required Fejer-residual target, not yet exact.
* H6: conditional one-dimensional diagnostic; recompute the exponent-pair inequality under a named convention.
* H7: proved algebraic obstruction.
* H8: proposed B-process-first route.

Then write the exact Vaaler lemma needed for H4/H5r, including the residual majorant and the discontinuity convention.

## For `gemini_deep_think`

Focus on H8. Write the B-process-first transformation for the spatial-character sum

$$
\sum_{d\sim D}\chi_4(d)w(d/D)e(hX/d).
$$

The output must state the transformed sum, dual length, dual phase, and whether $\chi_4$ becomes a Gauss-sum factor or only a residue-class selector. It should explicitly check whether the transformed problem avoids H7 or simply delays the same parity degeneration.

Also redo H6 with one named exponent-pair theorem and one fixed normalization. The output should say whether the correct endpoint inequality is $p+2q\le 1$, $3p+2q\le 1$, or something else under that theorem.

# Confidence

High confidence in the selected main route: balanced hyperbola, floor-compatible sawtooth, finite Vaaler, and local dyadic reciprocal sums.

High confidence in H1, H2, H3, and H7.

Moderate confidence in the local cutoff $H_D\asymp D X^{-1/4}$ as the right conjectural-scale dyadic calibration.

Moderate confidence that H5a/H5b can be matched structurally to Li--Yang-type reciprocal sums after residue and phase-shift bookkeeping.

Low confidence that current Bombieri--Iwaniec/Li--Yang technology reaches the $X^{1/4+\epsilon}$ target without a new input. Li--Yang's published target exponent is $\theta^*=0.314483\ldots$, while the conjectural endpoint is $\theta=1/4$.

Low confidence that $\chi_4$ alone gives a usable saving after a standard A-process, because H7 shows that direct differencing collapses the character to parity.

[1]: https://teorth.github.io/expdb/blueprint/gauss-circle-chapter.html "The Gauss circle problem and its generalizations"

## Round 4 Update

Timestamp: 2026-06-01 04:38:34

See `rounds/web-research-test/round_004/judge/judge.md`.

Selected main route:

Continue the arithmetic route:

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

The smoothed Poisson--Bessel route remains secondary: it should still be kept as a calibration route for smoothing/unsmoothing and for recovering the classical $R^{2/3}$ sanity bound, but it is not the selected main analytic route.

The active Round 4 state has only two agents, `gpt_pro_thinking` and `gemini_deep_think`; older inactive-agent references should be ignored as historical noise. The uploaded Round 4 prompt also requires strict separation of proved claims, proposed lemmas, rejected routes, and next actions.

Round 4 made useful but non-solution progress:

1. H4 is now more precise: the Vaaler truncation must be used with a Fejer-kernel residual majorant, not with a scalar residual.
2. H5r is now an explicit required residual target, involving parity-supported and untwisted reciprocal sums.
3. H6 is now correctly normalized under the standard reciprocal-phase exponent-pair convention; the endpoint obstruction is $3\kappa+2\lambda\le 1$.
4. H8, the B-process-first route, has a clear Poisson transform and dual length.
5. H9 is a new proved diagnostic: the B-process dual phase $\sqrt{Xhm}$ has zero continuous Hessian, so generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly.

No improvement to the Gauss circle exponent has been proved.

Useful fragments by source:

## From `gpt_pro_thinking`

The most useful Round 4 contribution is the exact formulation of the finite Vaaler step and its residual.

Use

$$
e(t)=e^{2\pi i t},
\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

The proved floor-compatible identity remains:

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
y=\lfloor X^{1/2}\rfloor.
$$

For finite Vaaler, the correct structure is:

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
\qquad
\alpha_h\ll |h|^{-1},
$$

with residual bounded by a Fejer majorant

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t),
$$

where

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2.
$$

This resolves a persistent false-proof risk: one may not replace the Vaaler residual by a scalar $O(D/H_D)$ after summing over $d\sim D$. The nonzero Fourier modes of $K_H$ create further reciprocal sums.

The local dyadic Vaaler cutoff is:

$$
H_D\asymp D X^{-1/4}
$$

for

$$
X^{1/4}\le D\le X^{1/2}.
$$

Blocks with $D<X^{1/4}$ should be handled separately by trivial or short-sum estimates.

The main Vaaler families are:

$$
B_1(H_0,D;X)
=
\sum_{h\sim H_0}u_h
\sum_d
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
B_2(H_0,D;X)
=
\sum_{h\sim H_0}u_h\chi_4(h)
\sum_d
w_D(d)e(hX/(4d)).
$$

The required local ranges are:

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le H_D\asymp D X^{-1/4}.
$$

A sufficient endpoint-strength target is:

$$
B_i(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon},
\qquad i=1,2.
$$

The important Round 4 refinement is H5r. The first-leg Vaaler residual requires estimates for parity-supported sums

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d),
$$

and the second-leg residual requires estimates for shifted untwisted sums

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

A sufficient residual target is:

$$
C_1(K_0,D;X),\ C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}
$$

uniformly for $K_0\le H_D$.

This is likely one of the hardest remaining bottlenecks because H5r is character-blind or only parity-supported.

The second useful contribution is the corrected H6 diagnostic. Under the standard exponent-pair convention for one-dimensional sums, if $f^{(r)}(d)\asymp T D^{-r}$ on $d\asymp D$ and $(\kappa,\lambda)$ is an exponent pair, then

$$
\sum_{d\asymp D}e(f(d))
\ll_\epsilon
T^\kappa D^\lambda X^\epsilon.
$$

For

$$
f(d)=hX/d,
$$

the correct scale is

$$
T\asymp \frac{hX}{D}.
$$

At the endpoint

$$
D\asymp X^{1/2},
\qquad
h\asymp H_0\asymp X^{1/4},
$$

this gives

$$
\sum_{d\asymp D}e(hX/d)
\ll_\epsilon
X^{3\kappa/4+\lambda/2+\epsilon}.
$$

If the outer $h$-sum is treated trivially, the H5 target requires the inner sum to be $\ll X^{1/4+\epsilon}$, hence

$$
3\kappa+2\lambda\le 1.
$$

This should be recorded only as a conditional diagnostic. It does not rule out bilinear, spacing, large-sieve, or Bombieri--Iwaniec methods.

The third useful contribution is the preliminary H8 transform. For

$$
S_\chi(h,D)
=
\sum_d \chi_4(d)w(d/D)e(hX/d),
$$

Poisson summation after splitting modulo $4$ gives

$$
S_\chi(h,D)
=
\frac{i}{2}
\sum_{n\in\mathbb Z}
\chi_4(n)
\int_{\mathbb R}
w(u/D)e(hX/u-nu/4)\,du,
$$

up to the usual Poisson-normalization conventions.

The phase

$$
\phi_n(u)=hX/u-nu/4
$$

has a stationary point only for $n<0$. Writing $n=-m$ with $m>0$ gives

$$
u_0=2\sqrt{\frac{hX}{m}},
$$

so the dual length is

$$
m\asymp \frac{hX}{D^2}.
$$

Thus B-process-first preserves $\chi_4$ as a dual character, but it does not yet produce a saving.

## From `gemini_deep_think`

Gemini's strongest Round 4 contribution is the confirmation and sharpening of H8. It independently identifies the same B-process-first structure: Poisson summation modulo $4$ transfers $\chi_4$ from the original denominator variable to a dual Gauss factor, hence to $\chi_4(n)$ in the dual variable.

The Gauss factor is:

$$
\sum_{r\bmod 4}\chi_4(r)e(nr/4)
=
e(n/4)-e(3n/4)
=
2i\chi_4(n).
$$

This should be kept as a real structural fact: B-process-first does not immediately discard the character.

Gemini's second useful contribution is H9. After stationary phase, the dual phase has the form

$$
\Phi(h,m)=\sqrt{Xhm}
$$

up to a nonzero constant and fixed phase shift. Its Hessian is degenerate:

$$
\Phi_{hh}=-\frac14 X^{1/2}m^{1/2}h^{-3/2},
$$

$$
\Phi_{mm}=-\frac14 X^{1/2}h^{1/2}m^{-3/2},
$$

$$
\Phi_{hm}=\frac14 X^{1/2}h^{-1/2}m^{-1/2}.
$$

Therefore

$$
\det\nabla^2\Phi
=
\frac{X}{16hm}
-
\frac{X}{16hm}
=
0.
$$

This is a proved diagnostic. It blocks any future claim that the B-process dual form can be treated by generic full-rank two-dimensional stationary phase or decoupling. It does not block discrete Bombieri--Iwaniec spacing methods.

Gemini also correctly notes that H8 only delays the H7 obstruction. If one applies a direct A-process in the dual variable $m$, then

$$
\chi_4(m)\chi_4(m+q)
$$

again degenerates to a parity-supported factor, by H7.

Rejected or risky ideas:

1. Reject scalar Vaaler residuals.

The statement "Vaaler error is $O(D/H_D)$"is incomplete. The Fejer majorant contains nonzero frequencies. The residual generates sums of the same reciprocal type and must be included as H5r.

2. Reject H8 as a proof route by itself.

B-process-first preserves the character, but it moves the problem to a dual phase $\sqrt{Xhm}$ with zero Hessian. It also leaves open endpoint terms, nonstationary frequencies, and the reappearance of H7 after differencing. H8 is a diagnostic/proposed route, not a proof of cancellation.

3. Reject generic full-rank tools on the B-process dual phase.

H9 proves that the continuous Hessian determinant of $\sqrt{Xhm}$ is zero. Generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly.

4. Reject treating H6 as a general impossibility theorem.

H6 applies only to methods that first take absolute values or trivial summation in $h$ and then use a one-dimensional exponent-pair estimate in $d$. It does not address bilinear, double-large-sieve, spacing, or decoupling methods.

5. Reject $p+2q\le 1$ as the endpoint diagnostic under the standard convention.

With $T\asymp hX/D$, the endpoint condition is

$$
   3\kappa+2\lambda\le 1.
$$

Any other inequality must be tied to a different explicitly named exponent-pair normalization.

6. Reject "\chi_4$ gives Deligne/Weil savings after A-process."
H7 shows that direct differencing gives

$$
   \chi_4(d)\chi_4(d+q)
   =
   \begin{cases}
   1_{2\nmid d},& q\equiv 0\pmod 4,\\
   -1_{2\nmid d},& q\equiv 2\pmod 4,\\
   0,& q\equiv 1,3\pmod 4.
   \end{cases}
$$

There is no deep complete character sum at that stage.

7. Reject merging H5a, H5b, and H5r.

H5a has $\chi_4$ in the denominator variable. H5b has $\chi_4$ in the Fourier variable. H5r is parity-supported or untwisted. These are different analytic objects and should remain separate.

Known gaps:

1. Exact stationary-phase lemma for H8.

The current H8 transform is structurally correct but incomplete. It needs:
   - exact Poisson normalization modulo $4$;
   - exact dual phase, including sign and constants;
   - exact main amplitude;
   - dual length and support restrictions;
   - integration-by-parts bounds for nonstationary frequencies;
   - transition treatment near support boundaries;
   - uniformity for $X^{1/4}\le D\le X^{1/2}$ and $1\le h\le D X^{-1/4}$.

2. H5r may be the dominant obstruction.

The residual families

$$
   C_1(K_0,D;X)
$$

and

$$
   C_{2,\rho}(K_0,D;X)
$$

are character-blind or only parity-supported. They may force the problem back to divisor-type reciprocal sums even if H5a has some character structure.

3. H8 does not yet help H5r.

H8 was derived for the spatial-character main family H5a. The residual H5r includes untwisted/parity sums. It is not yet clear whether B-process-first provides any useful mechanism for H5r.

4. Relation to Li--Yang/Bombieri--Iwaniec remains only structural.

The main sums fit Li--Yang-type reciprocal phases with

$$
   T=X,\qquad M=D,\qquad H=H_0,\qquad F(x)=1/x.
$$

The derivative nondegeneracy condition is satisfied:

$$
   F'(x)=-x^{-2},
   \qquad
   F''(x)=2x^{-3},
   \qquad
   F'''(x)=-6x^{-4},
$$

hence

$$
   F'(x)F'''(x)-3F''(x)^2
   =
   -6x^{-6}.
$$

But Li--Yang prove exponent $\theta^*=0.314483\ldots$, not the conjectural $\theta=1/4$. The current H5 targets are endpoint-strength targets, not known estimates.

5. Endpoint and discontinuity conventions remain fragile.

H3 uses the floor-compatible sawtooth

$$
   \psi(t)=t-\lfloor t\rfloor-\frac12.
$$

Vaaler uses continuous trigonometric polynomials plus a residual majorant. The residual is exactly what absorbs half-jump discrepancies at integers. Omitting it invalidates the argument.

6. Poisson--Bessel calibration route is still incomplete.

The repo should still contain the smoothed Poisson--Bessel formula, sandwich/unsmoothing lemma, and $R^{2/3}$ recovery from trivial dyadic radial estimates.

7. Numerical stress tests are still missing.

The exact identities H1--H3 are now well supported, but boundary tests should still be run to catch convention/transcription mistakes.

New lemmas to add:

## H1. Exact symmetric hyperbola identity

Status: proved.

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$, and

$$
S(u)=\sum_{1\le a\le u}\chi_4(a),
$$

one has

$$
\sum_{ab\le X}\chi_4(a)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

## H2. Exact periodic formula for $S(u)$

Status: proved.

For real $u\ge 0$,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
-
\left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right).
$$

## H3. Balanced sawtooth formula

Status: proved as an $O(1)$ floor-compatible identity.

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$,

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
O(1).
$$

## H4. Finite Vaaler with residual majorant

Status: theorem dependency; statement now precise enough for the proof draft, but should be checked against a standard Vaaler reference.

For $H\ge 1$,

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
\qquad
\alpha_h\ll |h|^{-1},
$$

and

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t),
$$

with

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

This lemma must be invoked with the residual retained.

## H5a. Spatial-character local dyadic target

Status: sufficient target, not known.

For

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le D X^{-1/4},
$$

define

$$
B_1(H_0,D;X)
=
\sum_{h\sim H_0}u_h
\sum_d
\chi_4(d)w_D(d)e(hX/d).
$$

A sufficient target is:

$$
B_1(H_0,D;X)
\ll_\epsilon H_0X^{1/4+\epsilon}.
$$

## H5b. Frequency-character local dyadic target

Status: sufficient target, not known.

For the same ranges,

$$
B_2(H_0,D;X)
=
\sum_{h\sim H_0}u_h\chi_4(h)
\sum_d
w_D(d)e(hX/(4d)).
$$

A sufficient target is:

$$
B_2(H_0,D;X)
\ll_\epsilon H_0X^{1/4+\epsilon}.
$$

## H5r. Fejer-residual local dyadic targets

Status: required target family, not known.

First-leg residual:

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d).
$$

Second-leg residual:

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

A sufficient target is:

$$
C_1(K_0,D;X),\ C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

This is not a cosmetic residual; it is part of the analytic core.

## H6. Conditional one-dimensional exponent-pair diagnostic

Status: diagnostic, not theorem.

Under the standard reciprocal-phase convention

$$
T\asymp hX/D,
$$

a method that estimates the inner $d$-sum by a one-dimensional exponent pair and treats $h$ trivially must satisfy

$$
3\kappa+2\lambda\le 1
$$

at the endpoint block

$$
D\asymp X^{1/2},
\qquad
H_0\asymp X^{1/4}.
$$

## H7. A-process modulus degeneracy for $\chi_4$

Status: proved.

For every integer $q$,

$$
\chi_4(d)\chi_4(d+q)
=
\begin{cases}
1_{2\nmid d},& q\equiv 0\pmod 4,\\
-1_{2\nmid d},& q\equiv 2\pmod 4,\\
0,& q\equiv 1,3\pmod 4.
\end{cases}
$$

## H8. B-process-first character-dualization

Status: partially derived; requires uniform stationary phase before it can be used as a lemma.

For smooth compact support away from zero,

$$
S_\chi(h,D)
=
\sum_d\chi_4(d)w(d/D)e(hX/d)
$$

has the Poisson-dual form

$$
S_\chi(h,D)
=
\frac{i}{2}
\sum_n\chi_4(n)
\int w(u/D)e(hX/u-nu/4)\,du,
$$

up to normalization convention. Stationary phase localizes to $n=-m<0$ with

$$
m\asymp hX/D^2.
$$

The dual character is preserved, but no saving has yet been proved.

## H9. B-process dual Hessian degeneracy

Status: proved diagnostic.

For

$$
\Phi(h,m)=\sqrt{Xhm},
$$

one has

$$
\det\nabla^2\Phi=0.
$$

Therefore generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly to the B-process dual phase.

## B1. Poisson--Bessel calibration lemma

Status: secondary route; still to be written.

The repo should prove the smoothed Poisson--Bessel formula, the smoothing/unsmoothing sandwich, and the classical $E(R)\ll R^{2/3}$ estimate from trivial radial-sum bounds.

Counterexample checks to run:

1. H3 boundary and convention tests.

Evaluate both sides for:
   - $0<X<1$;
   - $X=1,2,3,4,5$;
   - integer squares;
   - integer nonsquares;
   - $X=n^2\pm 10^{-k}$;
   - $X$ just below and above an integer.

2. Vaaler discontinuity tests.

Choose $X,d$ such that one of

$$
   X/d,\qquad
   \frac{X/d+1}{4},\qquad
   \frac{X/d+3}{4}
$$

is integral. Verify that the Fejer residual majorant covers the half-jump discrepancy.

3. H5r stress tests.

Numerically compare

$$
   \frac1{H_D}
   \sum_{1\le k\le H_D}
   \left|
   \sum_d 1_{2\nmid d}w_D(d)e(kX/d)
   \right|
$$

against the conjectural scale $X^{1/4}$ for square and near-square $X$.

4. H8 stationary-phase verification.

Check:
   - sign of the dual variable;
   - exact phase constant;
   - amplitude scale;
   - nonstationary integration-by-parts bounds;
   - behavior near dyadic support boundaries.

5. H9 guardrail check.

Any proposed proof using full-rank two-dimensional stationary phase on $\sqrt{Xhm}$ should be rejected automatically unless it explains why H9 is irrelevant.

6. H7 post-H8 check.

Apply direct differencing to the dual character $\chi_4(m)$ and verify that the same parity collapse occurs. This tests whether H8 really avoids H7 or only delays it.

7. Li--Yang dictionary check.

For $F(x)=1/x$, verify all derivative hypotheses in the relevant Li--Yang setup and record exactly which estimate would need to improve from $\theta^*=0.314483\ldots$ to $\theta=1/4$.

Next round instructions:

## For `gpt_pro_thinking`

Produce the Stage A packet for the next round with three concrete tasks:

1. Insert H4 and H5r into the best proof draft as actual dependencies, not optional refinements.
2. State the Vaaler theorem from a standard reference with exact coefficients or with a clearly cited majorant version sufficient for the proof.
3. Compare H5r, not only H5a/H5b, with the Li--Yang/Bombieri--Iwaniec framework. Determine whether H5r is structurally inside the same known reciprocal-sum class or whether the absolute values in the residual create a strictly harder target.

Also keep the Bessel calibration route alive by writing the minimal Poisson--Bessel/sandwich lemma set needed to recover $E(R)\ll R^{2/3}$.

## For `gemini_deep_think`

Refine H8 into a formal stationary-phase lemma. The output should include:

1. exact Poisson normalization modulo $4$;
2. exact dual phase, including constants and signs;
3. main amplitude;
4. dual length $M_D\asymp hX/D^2$;
5. integration-by-parts bounds for nonstationary frequencies;
6. endpoint and transition treatment;
7. uniformity for

$$
   X^{1/4}\le D\le X^{1/2},
   \qquad
   1\le h\le D X^{-1/4}.
$$

Then explicitly test whether the resulting dual sums help H5r or only H5a. This is the key next question.

Confidence:

High confidence in H1, H2, H3, H6 under stated hypotheses, H7, and H9.

High confidence that H5r must be included and cannot be replaced by a scalar Vaaler error.

Moderate confidence in the H8 Poisson-dual structure and dual length; exact constants, amplitudes, and endpoint terms still need proof.

Moderate confidence that H5a/H5b/H5r are structurally related to Li--Yang/Bombieri--Iwaniec reciprocal sums.

Low confidence that H8 alone gives a route to the conjectural exponent, because the dual phase is Hessian-degenerate and H7 reappears after direct differencing.

Low confidence that current known technology reaches the required H5 endpoint. The present state is a sharpened reduction and obstruction map, not a proof of a new exponent.

## Round 5 Update

Timestamp: 2026-06-01 05:56:58

See `rounds/web-research-test/round_005/judge/judge.md`.

Selected main route:

Keep the current arithmetic route, but explicitly downgrade its status from "promising proof route"to "structured reduction plus obstruction map."
The selected route remains:

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

Here $X=R^2$, and the conjectural target is

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The active Round 5 judge prompt requires synthesis only for the two active agents, `gpt_pro_thinking` and `gemini_deep_think`; inactive-agent references are historical noise.

Round 5 changes the research state in one important way: **H5r is now the central bottleneck.** The Vaaler residual is not a removable technical nuisance. Its Fejer-majorant expansion produces parity-supported and untwisted reciprocal sums, which are structurally close to divisor-problem sums and may dominate the route.

The next round should therefore pursue two tracks in parallel:

1. **Complete the Vaaler route honestly**, with H5r treated as a mandatory endpoint-strength target.
2. **Explore non-majorizing alternatives**, because the positive Fejer majorant may be the mechanism that destroys the useful $\chi_4$ sign structure.

No improvement to the Gauss circle exponent has been proved.

Useful fragments by source:

## From `gpt_pro_thinking`

The most useful contribution is the clean insertion of H4 and H5r into the proof skeleton.

The proved arithmetic foundation remains:

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

This is a floor-compatible identity, not a Fourier identity. The value at integers is $\psi(n)=-1/2$.

The Vaaler dependency is now explicit. For $H\ge 1$,

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
\qquad
\alpha_h\ll |h|^{-1},
$$

with pointwise residual majorant

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t),
$$

where

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

The important point is that the residual must be expanded through $K_H$; it cannot be replaced by a scalar $O(D/H_D)$ before summing over $d$.

For a dyadic denominator block $d\asymp D$, the local Vaaler height remains

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

Short blocks $D<X^{1/4}$ are harmless by the trivial estimate.

The Vaaler main terms lead to the two endpoint-strength targets:

$$
B_1(H_0,D;X)
=
\sum_{h\sim H_0}u_h
\sum_d
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
B_2(H_0,D;X)
=
\sum_{h\sim H_0}u_h\chi_4(h)
\sum_d
w_D(d)e(hX/(4d)).
$$

A sufficient target is

$$
B_i(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon},
\qquad i=1,2,
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le D X^{-1/4}.
$$

The decisive Round 5 refinement is the explicit residual family H5r. The first residual produces parity-supported sums

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d),
$$

and the second residual produces shifted untwisted sums

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

A sufficient residual target is

$$
C_1(K_0,D;X),\ C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon},
$$

uniformly for $K_0\le H_D$.

This is now part of the analytic core. It is not optional.

The second useful contribution is the comparison of H5r with Li--Yang/Bombieri--Iwaniec-type reciprocal sums. After residue splitting, H5r has the same broad phase class

$$
e\left(\frac{kX}{d}\right)
=
e\left(\frac{kT}{M}F(d/M)\right),
\qquad
F(x)=1/x,
$$

with $T=X$ and $M=D$. The usual derivative checks are clean:

$$
F'(x)=-x^{-2},
\qquad
F''(x)=2x^{-3},
\qquad
F'''(x)=-6x^{-4},
$$

and

$$
F'(x)F'''(x)-3F''(x)^2
=
-6x^{-6}.
$$

Thus the phase is structurally in the Li--Yang reciprocal-sum class. The problem is the exponent: known technology reaches $\theta^*=0.314483\ldots$ in $X$-notation, while the conjectural target is $\theta=1/4$.

The third useful contribution is the minimal Poisson--Bessel calibration module. This should remain in the repo as a sanity check:

$$
S_\delta(R)-\pi R^2
=
R\sum_{k\ne 0}
\frac{J_1(2\pi R|k|)}{|k|}
\widehat\rho(\delta k),
$$

together with the smoothing sandwich

$$
E(R)
\ll
R\delta+
\sup_{|t-R|\le C\delta}|S_\delta(t)-\pi t^2|.
$$

Using trivial dyadic bounds gives

$$
E(R)\ll R\delta+R^{1/2}\delta^{-1/2},
$$

and balancing at $\delta=R^{-1/3}$ recovers

$$
E(R)\ll R^{2/3}.
$$

This is a calibration route, not the main analytic route.

## From `gemini_deep_think`

The most useful contribution is the "Fejer Majorant DDP Trap" diagnostic.

The point is precise: the Vaaler residual is controlled by a nonnegative Fejer kernel. After expanding the majorant, the first residual family contains $1_{2\nmid d}$ rather than $\chi_4(d)$. Thus the signed two-square character has been replaced by parity support.

This makes H5r structurally divisor-like. That does not prove an impossibility theorem, but it identifies the likely bottleneck of the Vaaler route.

Gemini's second useful contribution is the dual parity collapse check. If one applies a B-process to the parity residual

$$
\sum_d 1_{2\nmid d}w(d/D)e(kX/d),
$$

then splitting modulo $2$ should produce a dual factor essentially $(-1)^m$. A direct A-process in the dual variable gives

$$
(-1)^m(-1)^{m+q}=(-1)^q,
$$

which is constant in $m$.

This is the parity analogue of H7. It says that B-process-first may preserve $\chi_4$ for the signed main term H5a, but it does not obviously rescue the parity residual H5r.

Gemini's third useful contribution is the non-majorizing truncation suggestion. The claim should not be accepted as a theorem, but the route is worth testing: if the positive Fejer majorant is the mechanism that destroys $\chi_4$, then one should compare Vaaler against signed finite Fourier truncations, Perron/Mellin methods, or exact discrete transforms.

Rejected or risky ideas:

1. **Reject: "H5r is just an error term."**

   H5r is part of the analytic core. Without endpoint-strength bounds for $C_1$ and $C_{2,\rho}$, the Vaaler route does not imply the conjectural bound.

2. **Reject: "The Vaaler residual is only $O(D/H_D)$."**

   The zeroth Fejer mode gives $D/H_D$, but the nonzero modes give reciprocal sums. Omitting them is a false proof.

3. **Reject: "H5a success would solve the route."**

   Even if the signed spatial-character main family $B_1$ is controlled, the parity/untwisted residual H5r may still block the argument.

4. **Reject: "Fejer Majorant DDP Trap is a theorem."**

   It is currently a diagnostic obstruction, not a proved lower bound or equivalence. To become a theorem, it would need a formal reduction from H5r to a divisor-problem endpoint estimate, or a lower-bound construction showing unavoidable size.

5. **Reject: "Continuous Fourier truncation methods are exhausted."**

   Positive-majorant Vaaler creates a serious problem, but there may be signed truncations, blockwise cancellation among Fejer modes, Perron/Mellin formulations, or bilinear methods that avoid the crude majorant loss.

6. **Reject: "B-process-first solves the character problem."**

   H8 preserves $\chi_4$ in the dual variable for the signed main term, but direct differencing in the dual variable triggers H7 again. For the parity residual, B-process appears to produce an alternating dual factor whose direct differencing collapses immediately.

7. **Reject: "H6 rules out all character-blind methods."**

   H6 only applies to methods that treat the outer frequency variable trivially and then apply a one-dimensional exponent-pair estimate to the inner reciprocal sum. It does not rule out double large sieve, Bombieri--Iwaniec spacing, bilinear estimates, or decoupling-type methods that preserve the two-variable structure.

8. **Reject: "Current Li--Yang technology reaches H5."**

   Li--Yang-type methods provide the correct structural comparison class, but current known exponents remain above $1/4$ in $X$-notation. H5a, H5b, and H5r are endpoint-strength targets.

Known gaps:

1. **External Vaaler theorem verification.**

   The exact coefficient formula and residual majorant should be verified against a standard reference before H4 is marked as an imported theorem dependency. The proof draft may use the majorant form, but it must cite the theorem precisely.

2. **H5r-to-Li--Yang dictionary.**

   For $C_1$ and $C_{2,\rho}$, the repo must write the exact transformation to Li--Yang-type sums:
   - residue splitting;
   - phase $F(x)$;
   - local range $K_0\le D X^{-1/4}$;
   - smoothness and bounded variation of $v_k,w_D$;
   - where absolute values enter;
   - whether the theorem being invoked permits these weights.

3. **Absolute-value placement in H5r.**

   The intended H5r target should use smooth dyadic $k$-weights and at most one block-level absolute value. A termwise absolute value over $k$ is too crude and may artificially create the DDP trap.

4. **C1 is not yet a theorem.**

   The Fejer Majorant DDP Trap must be formulated conditionally. A correct statement is:

   If H5r is bounded only by known character-blind reciprocal-sum estimates with exponent $\theta$, then the Vaaler route gives at best $P(X)\ll_\epsilon X^{\theta+\epsilon}$.

   This is not a lower bound and not a proof that H5r cannot reach $\theta=1/4$.

5. **C2 parity-dual calculation needs proof.**

   The claim that B-process maps $1_{2\nmid d}$ to an alternating dual factor should be verified by an explicit Poisson calculation modulo $2$, including normalization, nonstationary terms, and possible zero-frequency contributions.

6. **Non-majorizing truncation alternatives are undeveloped.**

   The three main alternatives need exact error terms:
   - signed finite Fourier truncation;
   - Perron/Mellin formula for $4\zeta(s)L(s,\chi_4)$;
   - exact discrete or arithmetic transform avoiding positive pointwise majorants.

7. **H8 still lacks a uniform stationary-phase lemma.**

   The Poisson-dual formula for

$$
   \sum_d\chi_4(d)w(d/D)e(hX/d)
$$

   has been structurally derived, with dual length $m\asymp hX/D^2$, but constants, endpoint errors, transition ranges, and uniformity over the local Vaaler range remain unchecked.

8. **H9 degeneracy remains a guardrail.**

   The B-process dual phase

$$
   \Phi(h,m)=\sqrt{Xhm}
$$

   has zero continuous Hessian. Therefore generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly. This does not rule out discrete Bombieri--Iwaniec spacing.

9. **Poisson--Bessel calibration is not yet committed as a checked module.**

   The calibration proof should be inserted into the repo to stabilize smoothing and normalization conventions.

New lemmas to add:

## H1. Exact symmetric hyperbola identity

Status: proved.

For $X\ge 1$, $y=\lfloor X^{1/2}\rfloor$, and

$$
S(u)=\sum_{1\le a\le u}\chi_4(a),
$$

one has

$$
\sum_{ab\le X}\chi_4(a)
=
\sum_{a\le y}\chi_4(a)\left\lfloor\frac Xa\right\rfloor
+
\sum_{b\le y}S(X/b)
-
yS(y).
$$

## H2. Exact periodic formula for $S(u)$

Status: proved.

For real $u\ge 0$,

$$
S(u)
=
\left\lfloor\frac{u+3}{4}\right\rfloor
-
\left\lfloor\frac{u+1}{4}\right\rfloor
=
\frac12+
\psi\left(\frac{u+1}{4}\right)
-
\psi\left(\frac{u+3}{4}\right).
$$

## H3. Balanced sawtooth formula

Status: proved as an $O(1)$ floor-compatible identity.

For $X\ge 1$,

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
O(1).
$$

## H4. Finite Vaaler with Fejer residual

Status: external theorem dependency; exact reference still to verify.

Use a finite approximation

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
\qquad
\alpha_h\ll |h|^{-1},
$$

with

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t).
$$

The proof draft must retain the Fejer residual.

## H5a. Spatial-character local dyadic target

Status: sufficient target, not known.

For

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le H_0\le D X^{-1/4},
$$

prove

$$
B_1(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

## H5b. Frequency-character local dyadic target

Status: sufficient target, not known.

For the same range, prove

$$
B_2(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

## H5r. Fejer-residual local dyadic targets

Status: required sufficient target, not known.

For smooth Fejer/dyadic weights, prove

$$
C_1(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon},
$$

and

$$
C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

The first target is parity-supported; the second is untwisted with a frequency shift. These are likely the central bottleneck.

## H6. Conditional one-dimensional exponent-pair diagnostic

Status: diagnostic, not theorem.

Under the standard reciprocal-phase convention $T\asymp hX/D$, a method that treats $h$ trivially and applies only a one-dimensional exponent-pair estimate in $d$ must satisfy

$$
3\kappa+2\lambda\le 1
$$

at the endpoint block $D\asymp X^{1/2}$, $H_0\asymp X^{1/4}$.

## H7. A-process modulus degeneracy for $\chi_4$

Status: proved.

For every integer $q$,

$$
\chi_4(d)\chi_4(d+q)
=
\begin{cases}
1_{2\nmid d},& q\equiv 0\pmod 4,\\
-1_{2\nmid d},& q\equiv 2\pmod 4,\\
0,& q\equiv 1,3\pmod 4.
\end{cases}
$$

## H8. B-process-first character-dualization

Status: partially derived; not yet a proof input.

For smooth compact support away from zero,

$$
\sum_d\chi_4(d)w(d/D)e(hX/d)
$$

has a Poisson-dual form with dual character $\chi_4(n)$ and dual length

$$
|n|\asymp hX/D^2.
$$

It preserves the character but does not prove cancellation.

## H9. B-process dual Hessian degeneracy

Status: proved diagnostic.

For

$$
\Phi(h,m)=\sqrt{Xhm},
$$

one has

$$
\det\nabla^2\Phi=0.
$$

Generic full-rank two-dimensional stationary phase or decoupling cannot be applied directly to this dual phase.

## C1. Fejer Majorant DDP Trap

Status: diagnostic obstruction heuristic, not theorem.

The Vaaler residual majorant produces parity-supported or untwisted reciprocal sums, especially $C_1$ and $C_{2,\rho}$, which no longer contain $\chi_4(d)$. These should be compared to divisor-problem reciprocal sums. A proof that C1 is a barrier requires a formal reduction or lower-bound example.

## C2. Dual parity degeneration for H5r

Status: proposed algebraic lemma pending Poisson normalization.

If B-process sends $1_{2\nmid d}$ to an alternating dual factor $(-1)^m$, then direct differencing gives

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

Thus the parity factor carries no usable oscillation after an A-process. This is the H5r analogue of H7.

## H10. Non-majorizing truncation requirement

Status: proposed strategic route.

Seek an alternative to positive-majorant Vaaler residuals that preserves sign information in the truncation error. Candidate directions:
- signed finite Fourier truncation;
- Perron/Mellin formula for $4\zeta(s)L(s,\chi_4)$;
- exact discrete transforms.

For each candidate, state the exact error term replacing H5r.

## B1. Poisson--Bessel calibration module

Status: secondary proof module to add.

Prove the smoothed Poisson--Bessel formula, the smoothing sandwich, and recovery of $E(R)\ll R^{2/3}$ from trivial dyadic estimates.

Counterexample checks to run:

1. **Fejer spike test.**

   Test $X,d$ such that one of

$$
   X/d,\qquad
   \frac{X/d+1}{4},\qquad
   \frac{X/d+3}{4}
$$

   is near an integer. Then $K_H$ can be large, and H5r must cover the resulting contribution.

2. **Residual absolute-value placement test.**

   Compare three residual treatments:
   - scalar $D/H_D$ only;
   - blockwise absolute values after dyadic $k$-decomposition;
   - termwise absolute values in $k$.

   The first is incomplete. The third is too crude. The second is the intended formulation.

3. **H5r-to-Li--Yang dictionary test.**

   For $C_1$ and $C_{2,\rho}$, write the exact $F(x)$, weights, local ranges, and derivative checks. Verify that the coefficients fit any theorem being invoked.

4. **C2 Poisson check.**

   Apply Poisson summation modulo $2$ to

$$
   \sum_d1_{2\nmid d}w(d/D)e(kX/d).
$$

   Identify the dual factor, stationary phase, dual length, and nonstationary terms.

5. **Dual A-process collapse test.**

   After C2, apply direct differencing to the dual alternating factor and verify that it collapses to $(-1)^q$.

6. **Non-majorizing truncation comparison.**

   Compare Vaaler, signed Fourier truncation, and Perron/Mellin approaches. For each, record whether the replacement error preserves $\chi_4$ or loses it.

7. **Bessel calibration check.**

   Insert the Poisson--Bessel smoothing module and verify that it recovers $E(R)\ll R^{2/3}$ without relying on the arithmetic route.

Next round instructions:

## For `gpt_pro_thinking`

Produce a Stage A packet focused on H5r and non-majorizing alternatives.

Tasks:

1. Formalize C1 as a conditional proposition:

   If H5r is bounded only by character-blind Li--Yang-type estimates with exponent $\theta$, then the Vaaler route gives at best $P(X)\ll_\epsilon X^{\theta+\epsilon}$.

   State the proof of this implication.

2. Write the full H5r-to-Li--Yang dictionary for $C_1$ and $C_{2,\rho}$:
   - residue classes;
   - phase $F(x)$;
   - local range;
   - smooth weights;
   - absolute-value placement;
   - theorem hypotheses needed.

3. Start the non-majorizing truncation comparison. For Vaaler, signed Fourier truncation, and Mellin-Perron, state exactly what error term replaces H5r.

4. Add the Poisson--Bessel calibration module to the best proof draft.

## For `gemini_deep_think`

Produce a Stage A packet focused on C2 and H10.

Tasks:

1. Prove or refute C2 by explicit Poisson summation modulo $2$ for

$$
   \sum_d1_{2\nmid d}w(d/D)e(kX/d).
$$

   Identify the dual factor, dual phase, dual length, and error terms.

2. Test whether B-process-first helps H5r or only transforms it into another parity-degenerate problem.

3. Sketch the Mellin-Perron alternative at lemma level:
   - exact Perron formula for $4\zeta(s)L(s,\chi_4)$;
   - contour shift;
   - residues;
   - truncation error;
   - analytic estimates needed to reach $X^{1/4+\epsilon}$.

Confidence:

High confidence in H1, H2, H3, H6, H7, and the necessity of H5r.

High confidence that the Vaaler residual cannot be treated as scalar $O(D/H_D)$.

High confidence that C1 identifies a real obstruction in the current Vaaler route.

Moderate confidence that H5r is structurally divisor-like after residue splitting.

Moderate confidence that C2 is correct, but it still needs the explicit Poisson calculation.

Low confidence that C1 is a proved barrier; it is currently a diagnostic.

Low confidence that non-majorizing truncation or Mellin-Perron avoids importing estimates as hard as the original conjecture.

No new exponent has been proved. The concrete Round 5 result is a sharper and more honest proof skeleton: the route now visibly depends on endpoint-strength bounds for H5r, and the next round must either handle those residual sums or replace the Vaaler truncation with a sign-preserving alternative.

## Round 6 Update

Timestamp: 2026-06-01 08:01:08

See `rounds/web-research-test/round_006/judge/judge.md`.

Summary:

Round 6 did not prove a new Gauss circle exponent. Its main value is a sharper obstruction map around the Vaaler residual H5r and a correction of the parity-dual C2 discussion.

The selected route remains the balanced arithmetic route

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{local dyadic reciprocal sums},
$$

with

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

as the conjectural target. The immediate next objective is not to improve the exponent, but to state the exact norm theorem required for H5r and determine whether any non-majorizing replacement avoids the same reciprocal-sum difficulty.

Source anchors: uploaded Round 6 packet and cross-reviews.

Selected main route:

Keep the arithmetic hyperbola/Vaaler route, but treat it as a **structured reduction plus bottleneck diagnosis**, not as a proof route presently near completion.

The current proof skeleton is:

1. Use the proved balanced sawtooth formula

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
y=\lfloor X^{1/2}\rfloor,\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

2. Apply finite Vaaler only blockwise, with local height

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

3. Keep three separate analytic targets:

- H5a: spatial-character main sums with $\chi_4(d)$;
- H5b: frequency-character main sums with $\chi_4(h)$;
- H5r: Fejer-residual sums that are parity-supported or untwisted.

4. Make H5r the central Round 7 target. The proof must identify exactly which of the following norms is actually needed:

- fixed Fejer coefficients;
- arbitrary bounded dyadic $k$-coefficients;
- termwise $L^1$ over $k$.

Do not pivot exclusively to Bombieri--Iwaniec rational-collision matrices yet. First settle the exact H5r norm requirement and the corrected C2 Poisson lemma.

Useful fragments by source:

## From `gpt_pro_thinking`

The main useful contribution is the H5r-to-Li--Yang/Bombieri--Iwaniec dictionary.

For the first residual family, write

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d).
$$

Splitting $d=2n+1$ and scaling $n\asymp D/2$ keeps the phase in the reciprocal class

$$
e\left(\frac{kX}{D}F_{2,1}(x)\right),
\qquad
F_{2,1}(x)=\frac{1}{x+1/D}.
$$

The derivative determinant relevant to the Bombieri--Iwaniec/Li--Yang phase class is

$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
=
-6(x+1/D)^{-6}\ne 0.
$$

Thus the parity residual is not a pathological new phase; structurally it is an ordinary reciprocal-sum phase, hence close to the Dirichlet divisor problem class.

For the second residual family,

$$
S_{\rho}(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
\qquad \rho\in\{1,3\},
$$

the phase is again reciprocal, up to the harmless frequency shift $e(k\rho/4)$.

The second useful contribution is the corrected C1 formulation. If H5r is bounded only by character-blind reciprocal-sum estimates at exponent $\theta$, normalized so that dyadic residual blocks satisfy

$$
\sum_{k\sim K_0}v_k S_{\star}(k,D)
\ll_\epsilon
K_0 X^{\theta+\epsilon},
\qquad |v_k|\le 1,
$$

then the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs. The $X^{1/4}$ term is forced by the zero Fejer mode $D/H_D\asymp X^{1/4}$. This is a conditional upper-bound implication, not a lower bound and not an impossibility theorem.

The third useful contribution is the non-majorizing comparison table:

| Method | Replacement for H5r | Status |
|---|---|---|
| Vaaler with Fejer majorant | parity/untwisted reciprocal residual H5r | exact route, central bottleneck |
| signed Fourier truncation | high-frequency signed reciprocal tail | possible sign-preserving alternative, but tail may be too large |
| Mellin--Perron | contour integral and moment/subconvexity problem for $4\zeta(s)L(s,\chi_4)$ | standard reformulation, not yet an escape |

The Poisson--Bessel calibration module is also useful and should be retained as a secondary check: smoothing plus Poisson/Bessel estimates recover the classical sanity bound

$$
E(R)\ll R^{2/3}.
$$

## From `gemini_deep_think`

The strongest useful fragment is the explicit Poisson computation for the parity-supported residual. For

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{2\nmid d}w_D(d)e(kX/d),
$$

one valid convention gives

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\in\mathbb Z}
(-1)^m
\int_{\mathbb R}
w_D(u)
e\left(\frac{kX}{u}-\frac{mu}{2}\right)\,du,
$$

up to the sign convention in the Fourier transform. Stationary phase then has active dual length

$$
|m|\asymp \frac{kX}{D^2}.
$$

This is valuable, but it must be recorded carefully: the same transform can also be represented as a difference of integer and half-integer dual Poisson transforms. Therefore the alternating factor $(-1)^m$ is representation-dependent. It is not, by itself, a proved obstruction.

Gemini's second useful fragment is the warning that the boundary range

$$
D\asymp X^{1/2},\qquad k\asymp 1
$$

has dual length $O(1)$. Uniform stationary phase cannot be assumed there.

Gemini's third useful fragment is the Mellin--Perron/Voronoi comparison. The formula involving

$$
4\zeta(s)L(s,\chi_4)
$$

preserves the arithmetic character at the Dirichlet-series level and avoids Fejer positivity. But after truncation, contour shifting, and functional equations, it appears to reintroduce classical Voronoi/Hardy-type oscillatory sums. This is a useful diagnostic, not a theorem that all contour methods must fail.

## From `deepseek_api`

The strongest useful contribution is the insistence that H5r must be stated at the exact norm level needed in the proof. DeepSeek correctly challenged any synthesis that silently replaces the fixed Fejer residual by either an arbitrary-coefficient estimate or a termwise $L^1$ estimate without proving the implication.

DeepSeek also usefully pressed against overpromoting C2. The correct synthesis is between the two extremes:

- Gemini is too strong if it marks C2/C3 as a proved obstruction.
- DeepSeek is too strong if it says no alternating dual factor appears.

The invariant statement is that the odd-lattice Poisson transform admits both a $(-1)^m$ representation and a two-coset representation. The obstruction strength of the subsequent A-process is unresolved.

DeepSeek's proposed numerical and algebraic checks are also useful:

- compute Fejer residuals in square and near-square cases;
- compare fixed Fejer coefficients versus arbitrary coefficients versus termwise $L^1$;
- verify the $m\asymp kX/D^2$ dual length in boundary regimes;
- audit whether Li--Yang's theorem can be applied directly to $C_1$ and $C_{2,\rho}$.

Rejected or risky ideas:

1. **Reject: scalar Vaaler residuals.**

The Vaaler residual is not just $O(D/H_D)$. The zero Fejer mode gives that size, but nonzero Fejer modes create reciprocal sums. Any future proof that discards H5r should be rejected automatically.

2. **Reject: H5r as optional.**

Even complete success on H5a and H5b would not prove the route unless H5r is controlled at endpoint strength or replaced by a sign-preserving truncation with a better error term.

3. **Reject: C2 as a proved obstruction in Gemini's strong form.**

The formula with $(-1)^m$ is a valid representation, but it is equivalent to a two-coset dual formulation. The statement

$$
(-1)^m(-1)^{m+q}=(-1)^q
$$

shows only that direct A-process on the coefficient alone gives no deep parity cancellation. It does not prove that the full two-coset dual phase has no usable spacing information.

4. **Reject: DeepSeek's categorical claim that C2 is false.**

The alternating factor does appear in one correct Poisson parametrization. What is false is the stronger inference that this factor alone proves an analytic obstruction.

5. **Reject: Fejer Majorant DDP Trap as an unconditional lower bound.**

C1 is a conditional diagnostic: if the only H5r input is a character-blind reciprocal-sum bound with exponent $\theta$, then the route inherits that exponent. It is not a theorem that no better H5r estimate exists.

6. **Reject: Mellin--Perron/Voronoi circularity as an impossibility theorem.**

Applying functional equations to Perron integrals recovers Voronoi/Hardy-type structures, but that does not rule out moment, spectral, bilinear, or smoothed-contour inputs on other lines.

7. **Reject: termwise $L^1$ over $k$ is necessary.**

Termwise $L^1$ is sufficient and may be convenient for stress testing, but the actual Vaaler proof may only require the fixed Fejer-coefficient residual. Round 7 must prove exactly which norm suffices.

8. **Reject: current Li--Yang/Bombieri--Iwaniec technology already reaches H5r at $\theta=1/4$.**

The phase class matches, but the needed endpoint bound is stronger than known record technology unless a precise theorem says otherwise.

9. **Reject: generic full-rank two-dimensional stationary phase or decoupling on the B-process dual phase.**

The earlier guardrail remains:

$$
\Phi(h,m)=\sqrt{Xhm}
\quad\Longrightarrow\quad
\det\nabla^2\Phi=0.
$$

Known gaps:

1. **Exact H5r norm theorem.**

The main missing item is a theorem of the following form: given the Vaaler residual majorant, prove precisely which residual estimate implies

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The theorem must distinguish:

- fixed Fejer coefficients;
- arbitrary dyadic $v_k$;
- termwise $L^1$ over $k$.

2. **C2 convention and stationary phase.**

The odd-lattice Poisson formula needs a convention-fixed statement with:

- sign normalization;
- equivalence of the $(-1)^m$ and two-coset formulations;
- active sign of $m$;
- dual length $|m|\asymp kX/D^2$;
- amplitude;
- endpoint and transition regimes;
- nonstationary integration-by-parts bounds.

3. **C3 obstruction strength.**

It is not yet known whether the two-coset formulation retains spacing information that the one-sequence $(-1)^m$ representation hides. This must be tested before claiming that B-process-first fails for H5r.

4. **H5r-to-Li--Yang theorem audit.**

The dictionary is structural. The repo still needs to identify a precise theorem, with hypotheses, that applies to

$$
S_{\mathrm{odd}}(k,D)
$$

and

$$
S_\rho(k,D),
$$

including allowed $k$-weights, smoothness, dyadic ranges, and where absolute values are placed.

5. **Signed Fourier truncation tail.**

A signed truncation may preserve sign information better than the Fejer majorant, but its high-frequency tail must be estimated. No usable bound has been proved.

6. **Mellin--Perron error quantification.**

The repo needs exact statements for:

- sharp Perron truncation;
- smoothed Perron truncation;
- contour shift and residues;
- functional-equation/Voronoi transform;
- moment or subconvexity input needed to reach $X^{1/4+\epsilon}$.

7. **Boundary ranges.**

The range

$$
D\asymp X^{1/2},\qquad k\asymp 1
$$

has very short dual length after C2. The range

$$
D\asymp X^{1/4}
$$

has $H_D\asymp 1$. Both require separate treatment.

8. **Numerical Fejer residual stress tests.**

No numerical evidence yet measures the loss from Fejer positivity or compares the fixed-Fejer, arbitrary-coefficient, and termwise-$L^1$ norms.

New lemmas to add:

## H5r-F. Fixed Fejer residual target

Status: required exact target, not yet proved.

Let

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2},
$$

and let

$$
\eta_{k,H_D}=1-\frac{|k|}{H_D+1}.
$$

For residual families $S_\star(k,D)$ equal to either

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
$$

or

$$
S_{\rho}(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
\qquad \rho\in\{1,3\},
$$

the minimal fixed-Fejer target is

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
\ll_\epsilon X^{1/4+\epsilon}.
$$

The zero mode separately contributes

$$
D/H_D\asymp X^{1/4}.
$$

Round 7 must verify that H5r-F is exactly sufficient for the Vaaler residual.

## H5r-B. Arbitrary bounded dyadic coefficient target

Status: sufficient target, stronger than H5r-F.

For all $1\le K_0\le H_D$ and $|v_k|\le 1$, require

$$
\sum_{k\sim K_0}v_k S_\star(k,D)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

This implies H5r-F after dyadic decomposition and division by $H_D$, but it may be stronger than the proof needs.

## H5r-L1. Termwise residual target

Status: sufficient but probably too crude.

Require

$$
\frac1{H_D}
\sum_{1\le |k|\le H_D}
|S_\star(k,D)|
\ll_\epsilon X^{1/4+\epsilon}.
$$

This is useful for numerical stress tests, but should not be assumed necessary.

## C1. Corrected Fejer Majorant DDP diagnostic

Status: conditional diagnostic, not a theorem.

If the only available estimates for H5r are character-blind reciprocal-sum estimates with normalized exponent $\theta$,

$$
\sum_{k\sim K_0}v_k S_\star(k,D)
\ll_\epsilon
K_0X^{\theta+\epsilon},
$$

then the Vaaler route gives only

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs.

This is not a lower bound. It only says that the Vaaler route cannot beat the exponent supplied to H5r.

## C2. Corrected odd-lattice Poisson lemma

Status: partially proved transformation; stationary phase still needed.

For a smooth dyadic weight $w_D$,

$$
\sum_{2\nmid d}w_D(d)e(kX/d)
=
\frac12
\sum_{m\in\mathbb Z}
(-1)^m
\int_{\mathbb R}
w_D(u)e\left(\frac{kX}{u}-\frac{mu}{2}\right)\,du,
$$

up to Fourier sign conventions.

Equivalently, the same expression is a difference of integer and half-integer dual Poisson transforms. Stationary phase localizes to

$$
|m|\asymp \frac{kX}{D^2}.
$$

This is a transformation lemma, not an obstruction theorem.

## C3. Dual parity A-process diagnostic

Status: proposed diagnostic, not proved obstruction.

If the C2 dual is forcibly represented as one sequence with coefficient $(-1)^m$, then direct differencing collapses the coefficient product:

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

This shows that the coefficient alone carries no deep mod-$2$ cancellation under a direct A-process. It does not rule out two-coset spacing gains.

## H10. Mellin--Perron non-majorizing comparison

Status: standard reformulation; not yet a proof route.

For $c>1$ and a suitable truncation convention,

$$
\sum_{n\le X}r_2(n)
=
\frac{1}{2\pi i}
\int_{c-iT}^{c+iT}
4\zeta(s)L(s,\chi_4)\frac{X^s}{s}\,ds
+
\text{truncation error}.
$$

The pole at $s=1$ gives the main term $\pi X$. The route avoids Fejer positivity but replaces H5r by contour-integral, moment, subconvexity, or Voronoi/Bessel estimates. It should be kept as a comparison route unless it yields a genuinely different endpoint target.

## H11. Voronoi/Perron circularity diagnostic

Status: diagnostic only.

Applying functional equations to the Mellin--Perron integral leads toward Voronoi/Hardy-type oscillatory expansions. This explains why the route may circle back to known Bessel/reciprocal-sum difficulties. It is not an impossibility theorem.

## H6. Exponent-pair endpoint diagnostic

Status: proved conditional calculation under stated convention, not a general obstruction.

Under the standard convention for reciprocal phases,

$$
f(d)=hX/d,\qquad T\asymp hX/D,
$$

an exponent-pair estimate gives

$$
\sum_{d\sim D}e(hX/d)
\ll_\epsilon
T^\kappa D^\lambda X^\epsilon.
$$

At

$$
D\asymp X^{1/2},
\qquad
h\asymp X^{1/4},
$$

this becomes

$$
X^{3\kappa/4+\lambda/2+\epsilon}.
$$

If the $h$-sum is treated trivially, reaching the endpoint requires

$$
3\kappa+2\lambda\le 1.
$$

Counterexample checks to run:

1. **H5r norm comparison.**

For representative $X,D,H_D$, compute:

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|,
$$

$$
\sup_{|v_k|\le 1}
\left|
\frac1{H_D}
\sum_{k\sim K_0}v_kS_\star(k,D)
\right|,
$$

and

$$
\frac1{H_D}\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

Compare fixed Fejer, arbitrary bounded coefficients, and termwise $L^1$.

2. **Fejer spike test.**

Test $X,d$ such that one of

$$
X/d,\qquad
\frac{X/d+1}{4},\qquad
\frac{X/d+3}{4}
$$

is near an integer. These are the cases where $K_H$ may spike.

3. **C2 convention test.**

Verify explicitly that

$$
\frac12\sum_m(-1)^mI(m/2)
$$

matches the difference of integer and half-integer dual Poisson transforms, with the same Fourier convention.

4. **C2 stationary-phase test.**

For

$$
I_m=\int w_D(u)e\left(\frac{kX}{u}-\frac{mu}{2}\right)\,du,
$$

check:

- active sign of $m$;
- stationary point location;
- amplitude;
- phase constant;
- dual length $|m|\asymp kX/D^2$;
- boundary behavior when $kX/D^2\asymp 1$.

5. **C3 two-coset A-process test.**

Apply differencing both to the one-sequence $(-1)^m$ formulation and to the two-coset formulation. Determine whether any spacing distinction survives in the phases.

6. **H5r-to-Li--Yang audit.**

For $F_{2,1}(x)=1/(x+1/D)$ and $F_2(x)=1/(4x)$, verify all derivative hypotheses in the precise Li--Yang theorem being considered. Record whether the theorem accepts:

- smooth $k$-weights;
- arbitrary bounded $v_k$;
- blockwise absolute values;
- parity or residue-class coefficients.

7. **Signed Fourier truncation tail test.**

For a finite signed Fourier approximation to $\psi$, estimate the high-frequency tail after the hyperbola cut. Record whether the tail preserves $\chi_4$ or becomes character-blind.

8. **Mellin--Perron truncation test.**

Write the sharp and smoothed Perron errors with explicit $T$-dependence. Test what $T$ and what moment/subconvexity input would be needed for $X^{1/4+\epsilon}$.

9. **Bessel calibration test.**

Commit the Poisson--Bessel smoothing module and verify that it recovers

$$
E(R)\ll R^{2/3}
$$

without invoking the arithmetic Vaaler route.

Next round instructions:

## For `gpt_pro_thinking`

1. Write the exact H5r norm theorem.

State and prove the implications:

$$
\text{H5r-B}\Rightarrow \text{H5r-F}\Rightarrow
\text{Vaaler residual}\ll X^{1/4+\epsilon}.
$$

Also state whether H5r-L1 is stronger, weaker, or merely different from H5r-B in the required dyadic setup.

2. Write C1 as a clean lemma-bank entry with the corrected normalization:

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}.
$$

Do not use the incorrect $X^{1/4+\theta}$ scaling.

3. Produce the convention-fixed C2 Poisson lemma, including the two equivalent formulations and a list of stationary-phase hypotheses still missing.

4. Update H10 as a comparison table with exact replacement errors for Vaaler, signed Fourier truncation, and Mellin--Perron.

## For `gemini_deep_think`

1. Downgrade all "continuous exhaustion" and "Voronoi circularity trap" language to diagnostic status.

2. Develop the Mellin--Perron route to theorem-dependency level:

- exact Perron formula;
- sharp truncation error;
- smoothed Perron alternative;
- contour shift and residue extraction;
- moment/subconvexity estimates required;
- resulting dyadic sums after the functional equation.

3. Analyze C3 in the two-coset formulation. Determine whether the phase shift between integer and half-integer dual transforms can survive an A-process or spacing argument.

4. Provide a rational-collision matrix test for the primal phase

$$
e(kX/d)
$$

that keeps track of the congruence classes $d\equiv 1,3\pmod 4$ without prematurely discarding signs.

## For `deepseek_api`

1. Algebraically verify the C2 Poisson normalization modulo $2$ and reconcile the $(-1)^m$ and two-coset formulas.

2. Run numerical tests for H5r-F, H5r-B, and H5r-L1 on square, nonsquare, and near-square $X$.

3. Check the derivative determinant calculations for $F_{2,1}$ and $F_2$.

4. Audit the exact Li--Yang/Bombieri--Iwaniec theorem: determine whether it applies directly to $S_{\mathrm{odd}}$ and $S_\rho$ with the weights and absolute-value placement required by H5r.

5. Independently verify the stationary-phase constants and boundary regimes for C2.

Confidence:

High confidence in the selected main route as a reduction and diagnostic framework.

High confidence that H5r is mandatory and cannot be replaced by a scalar $O(D/H_D)$ residual.

High confidence that H5r is structurally in the reciprocal-sum / divisor-problem phase class after residue splitting.

High confidence that C1 is valid as a conditional diagnostic when normalized as

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}.
$$

Moderate confidence in the C2 Poisson formula up to Fourier sign conventions.

Moderate confidence that the alternating-factor A-process collapse is a useful diagnostic, but low confidence that it is a full obstruction because of the two-coset formulation.

Moderate confidence that Mellin--Perron is a useful non-majorizing comparison route.

Low confidence that Mellin--Perron or signed Fourier truncation currently avoids a problem as hard as H5r.

Low confidence that any current route in the repo proves an exponent improvement. The Round 6 gain is precision: the Vaaler route now has an exact bottleneck to formulate, C2 has been corrected from a vague obstruction to a convention-dependent Poisson transform, and non-majorizing alternatives have explicit error terms to test.

## Round 7 Update

Timestamp: 2026-06-01 09:10:10

See `rounds/web-research-test/round_007/judge/judge.md`.

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

## Round 8 Update

Timestamp: 2026-06-01 10:07:17

See `rounds/web-research-test/round_008/judge/judge.md`.

Summary:

Round 8 is a precision round, not an exponent-improvement round. No new bound for the Gauss circle problem has been proved.

The main conclusion is that the balanced hyperbola/Vaaler route should remain the primary reduction framework, but its status is now: **structured reduction with a sharply identified bottleneck**, not a near-proof. The central bottleneck is the fixed-Fejer residual target H5r-F. Round 8 adds several useful algebraic and analytic diagnostics around that bottleneck:

1. R4 gives an exact Abel-summation identity for Fejer weights, clarifying why fixed Fejer averages may behave like partial-sum estimates unless their special averaging is exploited directly.
2. C2 gives a convention-fixed odd-lattice Poisson transform.
3. C2-SP gives the correct leading stationary-phase form, but the uniform error bookkeeping still needs repair, especially distinguishing dual length $M\asymp kX/D^2$ from stationary-phase parameter $\Lambda\asymp kX/D$.
4. B-Boundary shows the very small-$k$ boundary regime is harmless after the $1/H_D$ Vaaler normalization.
5. Q1-Ext gives a useful exact congruence factorization for near-collision character products, but it is an algebraic input, not an analytic saving until inserted into an actual Bombieri--Iwaniec/Li--Yang matrix.
6. C3-Ext gives a coefficient-collapse lemma for translation-invariant differencing in the two-coset odd-lattice dual model, but it is not a universal obstruction to all spacing methods.
7. Mellin--Perron should remain a comparison route, not a primary pivot. The sharp-Perron and functional-equation diagnostics suggest it reconstructs Hardy/Voronoi/Bessel-type sums, but the exact smoothed theorem and kernel analysis remain unwritten.

Source anchor: uploaded Round 8 packet and cross-reviews.

Selected main route:

Keep the selected route:

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

The target remains

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The official local Vaaler scale remains

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

The official minimal residual target remains H5r-F. For residual families

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
$$

and

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\},
$$

H5r-F asks for

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
\ll_\epsilon X^{1/4+\epsilon},
$$

where

$$
\eta_{k,H_D}=1-\frac{|k|}{H_D+1}.
$$

The correct implication chain is still

$$
\mathrm{H5r\text{-}B}
\Longrightarrow
\mathrm{H5r\text{-}F}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

Do not reverse either implication. H5r-F is formally weaker than H5r-B, but Round 8 sharpened the warning that many plausible proofs of H5r-F may silently pass through partial-sum or arbitrary-coefficient estimates and thereby lose the fixed-Fejer advantage.

The next round should not pivot away from this bottleneck. It should audit it more strictly:

1. reference-check H4, the exact Vaaler theorem;
2. prove the full two-sided residual-to-H5r-F implication with constants;
3. test whether H5r-F is genuinely easier than H5r-B/L1;
4. only then compare signed Fourier and Mellin--Perron alternatives.

Useful fragments by source:

## From `gpt_pro_thinking`

The most valuable contribution is the precise R4 Abel-summation diagnostic.

For one-sided positive frequencies, define

$$
A(j)=\sum_{1\le k\le j}a_k.
$$

Then

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac1{H+1}
\sum_{j=1}^{H}A(j).
$$

Applied to $a_k=S_\star(k,D)$, this proves that any proof of H5r-F based only on bounding all partial sums

$$
A(j)=\sum_{1\le k\le j}S_\star(k,D)
$$

inherits the same type of difficulty as H5r-B. This is a diagnostic, not an equivalence theorem: H5r-F may still be easier if a proof exploits the fixed Fejer averaging or the joint $(k,d)$ phase structure directly.

The second useful contribution is the clean comparison of truncation mechanisms:

| Method | Replacement error | Character preservation | Status |
|---|---|---|---|
| Vaaler with Fejer majorant | H5r-F, or stronger H5r-B/L1 | Main terms retain $\chi_4$; residual becomes parity-supported or untwisted | Main reduction; central bottleneck |
| Signed Fourier truncation | High-frequency signed reciprocal tail | Formally preserves $\chi_4$ longer | No endpoint tail estimate |
| Sharp Perron | Truncation error for $4\zeta(s)L(s,\chi_4)X^s/s$ | Preserves arithmetic in Dirichlet series | Comparison route; sharp truncation likely costly |
| Smoothed Perron | Smoothed contour kernel | Preserves arithmetic before functional equation | Theorem dependencies unwritten |
| Poisson--Bessel calibration | Smoothing annulus plus Bessel tail | Geometric, not $\chi_4$-driven | Sanity check only |

The third useful contribution is the signed Fourier tail formula. For the first leg, after truncating

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi i h},
$$

one obtains the formal high-frequency tail

$$
\mathcal T_1(D)
=
4\sum_{|h|>H_D}
\frac{1}{2\pi i h}
\sum_{d\sim D}
\chi_4(d)w_D(d)e(hX/d).
$$

For the second leg,

$$
\mathcal T_2(D)
=
-4\sum_{|h|>H_D}
\frac{e(h/4)-e(3h/4)}{2\pi i h}
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the signed tails formally preserve character structure. But no valid endpoint-strength tail estimate is known. If the tail is bounded absolutely, the route likely recreates an H5r/L1-type obstruction.

The Poisson--Bessel calibration module is also useful and should be inserted as a secondary sanity check:

$$
E(R)\ll R\delta+R^{1/2}\delta^{-1/2},
$$

and choosing

$$
\delta=R^{-1/3}
$$

recovers

$$
E(R)\ll R^{2/3}.
$$

This is not part of the main proof route.

## From `gemini_deep_think`

The most valuable contribution is Q1-Ext, the near-collision character factorization.

Let $(a,b)=1$, let $d_1,d_2$ be odd, and suppose

$$
d_1b-d_2a=\Delta.
$$

Then:

1. If $a,b$ are odd, then $\Delta$ is even and

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ab)(-1)^{\Delta/2}.
$$

2. If $a$ is even and $b$ is odd, then $\Delta$ is odd and

$$
d_1\equiv b(a+\Delta)\pmod 4.
$$

Thus $\chi_4(d_1)$ is frozen by $a,b,\Delta$, and the product is a fixed sign times $\chi_4(d_2)$.

3. If $a$ is odd and $b$ is even, then symmetrically $d_2$ is frozen modulo $4$, and the product is a fixed sign times $\chi_4(d_1)$.

This is a real algebraic refinement of the earlier exact-collision lemma. Its correct status is: **proved congruence lemma, analytic use pending**. It does not by itself prove cancellation. The next test is whether the $\Delta$-dependent sign survives the first Cauchy--Schwarz, double large sieve, or spacing-matrix absolute-value step in a Bombieri--Iwaniec/Li--Yang framework.

The second useful contribution is C3-Ext. In the two-coset odd-lattice dual representation, write

$$
\xi\in \frac12\mathbb Z,
\qquad
\sigma(\xi)=\frac12(-1)^{2\xi}.
$$

For a translation shift

$$
q=\xi_1-\xi_2,
$$

one has

$$
\sigma(\xi_1)\sigma(\xi_2)
=
\frac14(-1)^{2q}.
$$

Thus the coefficient parity sign factors out of the internal location variable in translation-invariant differencing. Correct status: **proved coefficient-collapse lemma for translation-invariant A-process arguments; diagnostic, not a universal obstruction**.

The third useful contribution is the Mellin--Perron diagnostic. Sharp Perron suggests that to force endpoint error one needs height around

$$
T\asymp X^{3/4}
$$

under the usual sharp truncation heuristic. Applying functional equations plausibly produces a Hardy/Voronoi-type dual length

$$
N\asymp X^{1/2}
$$

and a degenerate phase of the form

$$
\Phi(h,d)\asymp \sqrt{Xhd}.
$$

This is useful as a warning, but it should not be recorded as a proved "analytic isomorphism." The smoothed kernel, incomplete gamma transition, residues, and uniform stationary phase must be written before H10 can be promoted.

## From `deepseek_api`

The strongest contribution is the convention-fixed C2 odd-lattice Poisson transform. With

$$
F(u)=w_D(u)e(kX/u)
$$

and

$$
I(\xi)=\int_{\mathbb R}w_D(u)e(kX/u-\xi u)\,du,
$$

one has

$$
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
=
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu).
$$

This should be promoted as an algebraic transform.

The second useful contribution is the leading stationary-phase calculation. For $\xi=-m<0$,

$$
u_0=\sqrt{\frac{kX}{m}},
\qquad
\phi(u_0)=2\sqrt{kXm},
\qquad
\phi''(u_0)=\frac{2m}{u_0}.
$$

Thus the expected leading term is

$$
I(-m)
\sim
\frac{w_D(u_0)}{\sqrt{2m/u_0}}
e\left(2\sqrt{kXm}+\frac18\right),
$$

with amplitude

$$
|I(-m)|\asymp D^{3/2}(kX)^{-1/2}
$$

when

$$
m\asymp \frac{kX}{D^2}.
$$

However, the error term and uniformity must be recomputed with the two parameters separated:

$$
M\asymp \frac{kX}{D^2}
\quad\text{dual length,}
$$

and

$$
\Lambda\asymp \frac{kX}{D}
\quad\text{large stationary-phase parameter after scaling }u=Dv.
$$

Round 8 correctly identifies the scale, but the lemma bank should not yet record the claimed relative error as final.

The third useful contribution is B-Boundary. If

$$
D\asymp X^{1/2}
$$

and $|k|\le C$ is bounded, then

$$
\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|
\ll
\frac{D}{H_D}
\asymp X^{1/4},
$$

and the same holds for $S_\rho$. This handles the very small-$k$ edge without stationary phase.

The fourth useful contribution is N1: derivative nondegeneracy for shifted reciprocal phases. For

$$
F_{2,1}(x)=\frac1{x+1/D}
$$

one has

$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
=
-6(x+1/D)^{-6}\ne0.
$$

For

$$
F_2(x)=\frac1{4x},
$$

one has

$$
F_2'F_2'''-3(F_2'')^2
=
-\frac38x^{-6}\ne0.
$$

This confirms structural compatibility with reciprocal-sum phase classes.

N2, however, must be downgraded. It is correct that $S_{\mathrm{odd}}$ and $S_\rho$ map structurally into a Li--Yang/Bombieri--Iwaniec reciprocal double-sum phase class. It is not yet proved in the repo that the exact theorem applies to H5r-F with the required fixed coefficients, weights, absolute-value placement, local ranges, and endpoint strength. Record N2 as **structural compatibility pending theorem-level audit**.

Rejected or risky ideas:

1. **Reject: any claim of a new Gauss circle exponent.**

Round 8 proves no estimate of the form

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

and no improvement over existing known exponents.

2. **Reject: H5r-F is equivalent to H5r-B.**

R4 shows that monotone Fejer weights can be expressed through partial sums. It does not prove that fixed Fejer averaging is equivalent to arbitrary bounded coefficients or dyadic $L^1$. A direct method may still exploit the fixed Fejer structure.

3. **Reject: H5r-F is automatically easier than H5r-B.**

Because

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac1{H+1}\sum_{j=1}^{H}A(j),
$$

proofs via partial sums may inherit H5r-B-type difficulty. This remains a serious diagnostic obstruction.

4. **Reject: the Vaaler positive-majorant route is unconditionally "analytically blocked."**

It is blocked only under current character-blind or Li--Yang-level reciprocal-sum inputs. The formal possibility remains that fixed Fejer averaging admits a stronger direct estimate.

5. **Reject: Li--Yang theorem-level applicability has been fully audited.**

The phase shape matches. The exact theorem hypotheses, coefficient classes, allowed weights, local parameter ranges, and norm placement still need to be checked. Do not record "Li--Yang directly applies to H5r-F" as proved.

6. **Reject: C3-Ext ends the two-coset question.**

C3-Ext proves parity coefficient collapse for translation-invariant differencing. It does not rule out non-translation, multiplicative, spectral, or spacing methods that use more than the coefficient sign.

7. **Reject: Mellin--Perron is an analytic isomorphism or a definitive dead end.**

Sharp Perron and functional-equation diagnostics suggest the route reconstructs Hardy/Voronoi/Bessel sums. But no full smoothed Perron theorem with kernel analysis and endpoint bounds has been written. Keep H10 as a comparison route.

8. **Reject: signed Fourier truncation is a failed candidate.**

It is undeveloped and likely difficult, but not falsified. The correct status is: character-preserving formal alternative with no endpoint tail bound.

9. **Reject: C2-SP is fully proved with uniform errors.**

The leading stationary point, phase, and amplitude are correct at scaling level. Uniform error terms, endpoint transitions, and dependence on $M$ versus $\Lambda$ remain gaps.

10. **Reject: Q1-Ext alone provides analytic cancellation.**

Q1-Ext is exact congruence arithmetic. It becomes analytically useful only if a spacing or large-sieve argument preserves the $\Delta$-dependent sign rather than applying absolute values too early.

Known gaps:

1. **Exact H4 Vaaler theorem reference.**

The proof draft still needs a standard, reference-checked finite Vaaler theorem with:

- exact coefficients;
- exact Fejer majorant normalization;
- treatment of $\psi(n)=-1/2$ at discontinuities;
- two-sided handling of positive and negative frequencies.

2. **Full H5r-F sufficiency with constants.**

ALG-1 is correct at the scaffold level, but the proof draft must sum over:

- both sawtooth legs;
- both residual families $S_{\mathrm{odd}}$ and $S_\rho$;
- $k>0$ and $k<0$;
- all dyadic $D$;
- zero and nonzero Fejer modes;
- endpoint blocks.

3. **H5r-F versus H5r-B/L1 gap.**

R4 is exact, but the key unresolved question is whether fixed Fejer averaging gives real cancellation beyond partial-sum estimates. This must be tested both numerically and theoretically.

4. **C2-SP uniformity.**

The leading stationary phase should be rewritten in scaled variables:

$$
u=Dv,
\qquad
\Lambda\asymp \frac{kX}{D},
\qquad
M\asymp \frac{kX}{D^2}.
$$

The error term, transition layer, support-boundary behavior, and integration-by-parts decay must be stated uniformly for

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le k\le H_D.
$$

5. **Boundary and transition ranges.**

B-Boundary handles bounded $k$ when $D\asymp X^{1/2}$. It does not by itself cover all regimes where

$$
kX/D^2\asymp 1
$$

or where the stationary point is close to the edge of support.

6. **Li--Yang/Bombieri--Iwaniec theorem audit.**

The structural phase map is not enough. The exact theorem must be checked against:

- fixed Fejer coefficients versus arbitrary coefficients;
- smooth dyadic $w_D$;
- parity coefficients;
- frequency shifts $e(k\rho/4)$;
- local ranges $K_0\le D X^{-1/4}$;
- blockwise absolute values;
- whether the theorem yields the required $X^{1/4+\epsilon}$ scale or only a larger exponent in the current packet.

7. **Q1-Ext in actual spacing matrices.**

The sign

$$
\chi_4(ab)(-1)^{\Delta/2}
$$

or the frozen-residue alternatives must be inserted into a real rational-collision or near-collision matrix. The main question is whether summation over $\Delta$ preserves the sign or whether standard matrix norm estimates erase it.

8. **C3 beyond translation differencing.**

Need to test non-translation or two-coset spacing arguments. C3-Ext only covers translation-invariant A-process models.

9. **Signed Fourier tail.**

The formal tails $\mathcal T_1(D)$ and $\mathcal T_2(D)$ preserve character structure, but no summability or high-frequency cancellation theorem has been stated. This is the main gap for the non-majorizing Fourier alternative.

10. **Mellin--Perron comparison module.**

Need exact sharp and smoothed Perron formulas for

$$
4\zeta(s)L(s,\chi_4),
$$

including contour shifts, residues, truncation errors, functional equation, gamma factors, incomplete-kernel transition, and resulting dual sums.

11. **Numerical stress tests.**

No actual numerical tests have been run yet for H5r-F, H5r-B, H5r-L1, Fejer spikes, signed Fourier tails, or near-collision sign persistence.

New lemmas to add:

## R4. Fejer averaging / Abel-summation identity

**Status:** proved algebraic identity; diagnostic use only.

For any sequence $a_k$ and

$$
A(j)=\sum_{1\le k\le j}a_k,
$$

one has

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac1{H+1}\sum_{j=1}^{H}A(j).
$$

Application: H5r-F can be proved from partial-sum bounds, but such a proof may inherit H5r-B-type difficulty. This does not prove equivalence between H5r-F and H5r-B.

## ALG-1. Vaaler residual leads to H5r-F

**Status:** proved conditional on H4.

Assuming the Vaaler residual satisfies the Fejer majorant with the normalization used in the proof draft, each dyadic residual block is bounded by the zero mode

$$
D/H_D\asymp X^{1/4}
$$

plus fixed-Fejer combinations of $S_{\mathrm{odd}}(k,D)$ and $S_\rho(k,D)$. Therefore H5r-F is the minimal fixed-coefficient target naturally produced by the Vaaler route.

## C2. Odd-lattice Poisson transform

**Status:** proved algebraic transform under fixed Fourier convention.

With

$$
I(\xi)=\int_{\mathbb R}w_D(u)e(kX/u-\xi u)\,du,
$$

one has

$$
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
=
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu).
$$

## C2-SP. Leading stationary phase for C2

**Status:** leading term accepted; uniform error pending.

For $\xi=-m<0$,

$$
u_0=\sqrt{\frac{kX}{m}},
\qquad
I(-m)
\sim
\frac{w_D(u_0)}{\sqrt{2m/u_0}}
e\left(2\sqrt{kXm}+\frac18\right),
$$

with active dual length

$$
m\asymp \frac{kX}{D^2}
$$

and amplitude

$$
|I(-m)|\asymp D^{3/2}(kX)^{-1/2}.
$$

The final lemma must distinguish this dual length from the stationary-phase parameter

$$
\Lambda\asymp \frac{kX}{D}.
$$

## B-Boundary. Small-$k$ residual boundary

**Status:** proved elementary lemma.

For

$$
D\asymp X^{1/2},
\qquad
|k|\le C,
$$

one has

$$
\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|
\ll X^{1/4},
$$

and similarly for $S_\rho$. More generally, $O(X^\epsilon)$ such frequencies are harmless after absorbing $X^\epsilon$.

## N1. Reciprocal derivative nondegeneracy

**Status:** proved algebraic lemma.

For

$$
F_{2,1}(x)=\frac1{x+1/D},
$$

one has

$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
=
-6(x+1/D)^{-6}.
$$

For

$$
F_2(x)=\frac1{4x},
$$

one has

$$
F_2'F_2'''-3(F_2'')^2
=
-\frac38x^{-6}.
$$

## N2. H5r-to-reciprocal-sum structural compatibility

**Status:** structural mapping; theorem-level audit pending.

The sums $S_{\mathrm{odd}}$ and $S_\rho$ lie in the reciprocal phase class after residue splitting and scaling. This supports comparison with Bombieri--Iwaniec/Li--Yang-type estimates. It does not yet prove that the precise theorem applies to H5r-F with the required weights and norms.

## Q1-Ext. Near-collision character factorization

**Status:** proved congruence lemma; analytic use pending.

Let $(a,b)=1$, let $d_1,d_2$ be odd, and suppose

$$
d_1b-d_2a=\Delta.
$$

Then:

- if $a,b$ are odd,

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ab)(-1)^{\Delta/2};
$$

- if $a$ is even and $b$ is odd, then $d_1\bmod4$ is fixed by $a,b,\Delta$ and the product is a fixed sign times $\chi_4(d_2)$;
- if $a$ is odd and $b$ is even, then $d_2\bmod4$ is fixed by $a,b,\Delta$ and the product is a fixed sign times $\chi_4(d_1)$.

This lemma should be tested inside actual spacing matrices.

## C3-Ext. Two-coset parity coefficient collapse

**Status:** proved for translation-invariant differencing; diagnostic only.

For

$$
\xi\in \frac12\mathbb Z,
\qquad
\sigma(\xi)=\frac12(-1)^{2\xi},
$$

translation differencing gives

$$
\sigma(\xi_1)\sigma(\xi_2)
=
\frac14(-1)^{2(\xi_1-\xi_2)}.
$$

The sign is independent of the inner location variable. This blocks coefficient-level parity gains for direct translation A-process models, but it does not rule out non-translation or spectral spacing methods.

## SF1. Signed Fourier truncation tail

**Status:** formal comparison lemma; no bound proved.

The signed Fourier route replaces H5r by high-frequency tails $\mathcal T_1(D)$ and $\mathcal T_2(D)$ that formally preserve $\chi_4$. Its viability depends on proving endpoint-strength tail cancellation without absolute values.

## H10-A. Sharp Perron truncation diagnostic

**Status:** conditional diagnostic.

For the Dirichlet series

$$
4\zeta(s)L(s,\chi_4),
$$

sharp Perron truncation suggests height around

$$
T\asymp X^{3/4}
$$

to target $X^{1/4+\epsilon}$ errors under standard crude truncation heuristics. This must be replaced by exact sharp and smoothed Perron statements before use.

## H10-B. Mellin--Perron / Hardy--Voronoi comparison

**Status:** proposed diagnostic mapping, not theorem.

Applying functional equations plausibly reconstructs dual Bessel/Voronoi sums of length about

$$
X^{1/2}
$$

and phase

$$
\sqrt{Xhd}.
$$

This supports the warning that Mellin--Perron may mirror the same hard reciprocal/Bessel structure. It is not an impossibility theorem.

Counterexample checks to run:

1. **H5r norm comparison.**

For square, nonsquare, and near-square $X$, compute

$$
R_F(D)
=
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
$$

and compare it with

$$
R_{L1}(D)
=
\frac1{H_D}
\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

A persistent gap would support the possibility that fixed Fejer averaging helps. Comparable sizes would support the H5r-B bottleneck.

2. **Fejer spike test.**

Choose $X,d$ such that one of

$$
X/d,
\qquad
\frac{X/d+1}{4},
\qquad
\frac{X/d+3}{4}
$$

is close to an integer. Check whether $K_{H_D}$ spikes produce large residual blocks.

3. **R4 partial-sum simulation.**

Compute

$$
A(j)=\sum_{1\le k\le j}S_\star(k,D)
$$

and verify numerically whether

$$
\frac1{H_D(H_D+1)}\sum_{j\le H_D}A(j)
$$

behaves closer to fixed Fejer cancellation or to arbitrary-coefficient/L1 norms.

4. **C2 convention test.**

Numerically or symbolically verify

$$
\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
=
\frac12\sum_{m\in\mathbb Z}I(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}I(\mu)
$$

for compactly supported test weights.

5. **C2 stationary-phase test.**

For

$$
I(-m)=\int w_D(u)e(kX/u+mu)\,du,
$$

test the leading approximation

$$
\frac{w_D(u_0)}{\sqrt{2m/u_0}}
e\left(2\sqrt{kXm}+\frac18\right)
$$

with

$$
u_0=\sqrt{kX/m}.
$$

Separate tests by regimes:

$$
M=\frac{kX}{D^2}\asymp 1,
\qquad
M\gg1,
\qquad
\Lambda=\frac{kX}{D}\gg1.
$$

6. **B-Boundary test.**

For $D\asymp X^{1/2}$ and $1\le |k|\le X^\epsilon$, verify that the total contribution after division by $H_D$ is

$$
\ll X^{1/4+\epsilon}.
$$

7. **Q1-Ext stress test.**

For near-collisions

$$
d_1b-d_2a=\Delta,
$$

test the predicted character signs over many coprime $(a,b)$ and gaps $\Delta$. Then insert those signs into a mock spacing matrix and determine whether Cauchy--Schwarz or absolute values erase them.

8. **C3 two-coset spacing test.**

Apply both translation differencing and a non-translation/multiplicative differencing model to the two-coset dual expression. Check whether any phase-spacing distinction survives after the parity sign factors out.

9. **Signed Fourier tail test.**

Attempt to bound

$$
\mathcal T_1(D)+\mathcal T_2(D)
$$

without absolute values. Record exactly where any proof is forced to reintroduce H5r-like character-blind sums.

10. **Mellin--Perron reconstruction test.**

Write sharp and smoothed Perron formulas for

$$
4\zeta(s)L(s,\chi_4),
$$

shift contours, extract the pole at $s=1$, apply functional equations, and derive the resulting dual Bessel/Voronoi sums. Determine whether $\chi_4$ remains usable or is reorganized into the same hard reciprocal/Bessel structure.

11. **Li--Yang theorem audit.**

Take the precise theorem statement and check it against:

$$
K_0\le H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2},
$$

with fixed Fejer weights, parity restrictions, smooth $d$-weights, frequency shifts, and blockwise absolute values.

Next round instructions:

## For `gpt_pro_thinking`

1. Produce a reference-checked H4 statement, including exact Vaaler coefficients, Fejer majorant normalization, and discontinuity convention for the floor-compatible sawtooth.

2. Rewrite ALG-1 as a full proof over all dyadic blocks, both signs of $k$, both H3 legs, zero mode, and nonzero mode. State exactly where H5r-F enters.

3. Insert R1--R4, ALG-1, C1, C2, B-Boundary, N1, Q1-Ext, C3-Ext, SF1, H10-A, and H10-B into the best proof draft with the statuses above.

4. Build the actual H5a spacing-matrix test using Q1-Ext. The output should show whether the $\Delta$ sign survives through the first Cauchy--Schwarz / double-large-sieve reduction.

5. Keep Mellin--Perron as a comparison module, not a primary replacement route, until a smoothed Perron theorem and functional-equation kernel analysis are written.

## For `gemini_deep_think`

1. Redraft Q1-Ext with all parity assumptions explicit and downgrade any analytic conclusion to "pending insertion into a spacing estimate."

2. Redraft C3-Ext as "translation-invariant coefficient collapse," not as a proof that all two-coset spacing fails.

3. Develop the H10 Mellin--Perron module with exact sharp and smoothed Perron truncation errors, residues, functional equation, and kernel transition terms. Avoid terms such as "isomorphism" unless an actual equivalence theorem is proved.

4. Test whether non-translation differencing or multiplicative shifts can preserve information in the two-coset formulation after C3-Ext.

## For `deepseek_api`

1. Run numerical comparisons of H5r-F, H5r-B, and H5r-L1 for square, nonsquare, and near-square $X$.

2. Verify the C2 stationary phase under the convention $e(t)=e^{2\pi i t}$, but separate the two scales

$$
M\asymp \frac{kX}{D^2}
$$

and

$$
\Lambda\asymp \frac{kX}{D}.
$$

3. Formulate a uniform transition lemma for C2, including support-boundary stationary points and the regime $M\asymp1$.

4. Audit the exact Li--Yang/Bombieri--Iwaniec theorem and state whether it applies to H5r-F itself, only to H5r-B, or only to a still stronger norm.

5. Recheck N2 with exact parameter normalization. Do not state theorem-level applicability until the coefficient and norm hypotheses have been matched line by line.

Confidence:

High confidence in the continued selection of the balanced hyperbola/Vaaler route as the main reduction and diagnostic framework.

High confidence that no exponent improvement has been proved.

High confidence that H5r-F remains the official minimal residual target.

High confidence in R4 as an exact algebraic identity and as a useful diagnostic.

High confidence in C2 as a convention-fixed Poisson transform.

High confidence in B-Boundary for bounded or $X^\epsilon$ many small frequencies after Vaaler normalization.

High confidence in Q1-Ext and C3-Ext as algebraic lemmas under their stated hypotheses.

Moderate confidence in the C2-SP leading stationary-phase formula; lower confidence in the stated error terms until the $M$ versus $\Lambda$ bookkeeping is fixed.

Moderate confidence that H5r residual sums are structurally reciprocal/divisor-like.

Low confidence that current Li--Yang/Bombieri--Iwaniec inputs reach the endpoint H5r-F target as needed here.

Low confidence that signed Fourier truncation can be made to work without recreating H5r-type absolute-value losses.

Low confidence that Mellin--Perron avoids the same Hardy/Voronoi/Bessel bottleneck, but it remains useful as a comparison module.

Overall Round 8 judgment: successful obstruction mapping and lemma cleanup. The next round should not claim a pivot or a solution. It should lock down H4/ALG-1, run the H5r norm tests, audit Li--Yang at theorem level, and test whether Q1-Ext survives inside an actual signed spacing matrix.

## Round 9 Update

Timestamp: 2026-06-01 11:05:51

See `rounds/web-research-test/round_009/judge/judge.md`.

Summary:

Round 9 does **not** prove a new Gauss circle exponent. It does, however, make a significant internal reduction improvement. The fixed-Fejer Vaaler residual H5r-F, previously treated as the central bottleneck, now appears controllable at the conjectural scale by an elementary product-counting lemma R5, conditional on the standard Vaaler Fejer-majorant theorem H4. This shifts the main unresolved analytic burden back to the Vaaler **main terms** H5a/H5b, and specifically to their **fixed Vaaler coefficient** forms rather than arbitrary-coefficient stress-test versions.

Source anchors: Round 9 packet and Stage A/B outputs are in `judge_9.md`; the retrieved snippets include the R5 product-count formulation, the Li--Yang endpoint non-import statement, and the C2 odd-lattice Poisson transform.

Selected main route:

Keep the balanced arithmetic hyperbola/Vaaler route as the main reduction framework:

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{fixed-coefficient reciprocal sums}.
$$

The target remains

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

The Round 9 route should now be recorded as:

$$
\text{H1--H3}
+
\text{H4}
+
\text{R5}
+
\text{H5a-fix/H5b-fix}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

Here:

- H1--H3 are the proved balanced sawtooth reductions.
- H4 is the finite Vaaler approximation with Fejer residual majorant; the exact reference and normalization still need to be verified.
- R5 is the new product-count bound for the fixed Fejer residual.
- H5a-fix and H5b-fix are the remaining hard main-term estimates with the actual Vaaler coefficients $\alpha_h$, not arbitrary coefficients.

The local scale remains

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4}.
$$

The residual target H5r-F should be demoted from "central open bottleneck" to "provisionally resolved by R5, pending exact H4 reference and complete write-up." The stronger H5r-B and H5r-L1 norms should be retained only as stress tests; they are no longer active dependencies unless R5 fails.

Useful fragments by source:

## From `gpt_pro_thinking`

The most important contribution is R5, the Fejer product-count lemma. Instead of expanding the Vaaler residual into arbitrary-coefficient reciprocal sums, the fixed Fejer residual is kept as a positive kernel:

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2.
$$

Using

$$
K_H(t)\ll \min\left(H,\frac{1}{H\|t\|^2}\right),
$$

one has

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac{1}{H^2\|t\|^2}\right).
$$

For the first residual leg,

$$
\frac1H
\sum_{d\sim D}
w_D(d)K_H(X/d),
$$

choose $m$ nearest to $X/d$. Then

$$
\|X/d\|\asymp \frac{|X-md|}{D}
$$

for $d\asymp D$, up to harmless endpoint conventions. With

$$
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

the summand is bounded by

$$
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by $n=md$ and using

$$
\tau(n)\ll_\epsilon n^\epsilon
$$

gives

$$
\frac1H
\sum_{d\sim D}
w_D(d)K_H(X/d)
\ll_\epsilon
X^\epsilon
\sum_{n\asymp X}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

The same argument should apply to the shifted second-leg kernels

$$
\frac1H
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\},
$$

after writing the near-integrality condition as

$$
X\approx d(4m-\rho).
$$

This introduces only a congruence restriction on the complementary factor, hence is bounded by the ordinary divisor function.

The second important contribution is the Li--Yang source audit. The H5r, H5a, and H5b phases are structurally compatible with Li--Yang-type reciprocal sums, but Li--Yang does not supply the endpoint theorem needed here. Their final target has the form

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\cdots,
$$

with truncation range

$$
H\le MT^{-\theta^*}.
$$

This does not reach the endpoint Vaaler range

$$
H\le MT^{-1/4}.
$$

The third important correction is that H5a/H5b should be reformulated with exact Vaaler coefficients. The prior arbitrary-coefficient versions are overstrong. The actual main terms involve

$$
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
\qquad
|\alpha_h|\ll |h|^{-1},
$$

and

$$
\sum_{1\le |h|\le H_D}
\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

These should become H5a-fix and H5b-fix.

## From `deepseek_api`

The most useful contribution is the exact odd-lattice Poisson transform C2-Alg. With

$$
e(t)=e^{2\pi i t},
\qquad
\widehat f(\xi)=\int_{\mathbb R}f(u)e(-\xi u)\,du,
$$

and

$$
f(u)=w_D(u)e(kX/u),
$$

one has

$$
\sum_{2\nmid d} f(d)
=
\frac12\sum_{m\in\mathbb Z}\widehat f(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
$$

This should be promoted as the official convention-fixed C2 algebraic lemma.

DeepSeek also correctly identified the stationary-phase sign and scale. For $\xi=-m<0$,

$$
\widehat f(-m)
=
\int w_D(u)e(kX/u+mu)\,du,
$$

with phase

$$
\phi(u)=kX/u+mu.
$$

The stationary point is

$$
u_0=\sqrt{kX/m},
$$

and the active dual length is

$$
m\asymp \frac{kX}{D^2}.
$$

The leading amplitude scale is

$$
|\widehat f(-m)|
\asymp
D^{3/2}(kX)^{-1/2}
$$

in the interior stationary range. This should be entered as C2-SP0, with uniform error estimates deferred to C2-SPU.

DeepSeek also correctly handled the small-$k$ boundary. When

$$
D\asymp X^{1/2},
\qquad
|k|\le X^\epsilon,
$$

the trivial bound

$$
|S_\star(k,D)|\ll D
$$

combined with

$$
H_D\asymp D X^{-1/4}
$$

gives

$$
\frac1{H_D}|S_\star(k,D)|
\ll X^{1/4}.
$$

Thus $X^\epsilon$ many such frequencies remain harmless.

The Li--Yang audit from DeepSeek is also valuable because it distinguishes phase compatibility from theorem applicability. For the raw endpoint block

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H=H_D\asymp X^{1/4},
$$

Li--Yang Case A gives

$$
H\le MT^{-49/164}
=
X^{33/164}
\approx X^{0.2012},
$$

and Case B gives a still smaller principal bound

$$
H\le M^{35/69}T^{-2/23}
=
X^{23/138}
=
X^{1/6}.
$$

Both are below $X^{1/4}$. Therefore Li--Yang cannot be quoted directly on the raw endpoint block.

## From `gemini_deep_think`

Gemini's most useful contribution is the sharpened Li--Yang parameter-domain warning. The conclusion should be recorded carefully:

$$
\text{raw Li--Yang theorem invocation fails at the endpoint block.}
$$

It should **not** be recorded as:

$$
\text{all Bombieri--Iwaniec/Li--Yang-type methods are impossible.}
$$

A full dissection could change effective parameters, but current published technology still reaches $\theta^*>1/4$, not the conjectural $1/4$.

Gemini's Mellin--Perron diagnostic is also useful. Applying a Perron/functional-equation route to

$$
4\zeta(s)L(s,\chi_4)
$$

with height

$$
T\asymp X^{3/4}
$$

leads by stationary phase to a dual condition roughly

$$
t_0\asymp \sqrt{nX},
\qquad
n\lesssim T^2/X\asymp X^{1/2},
$$

and phase of Hardy/Voronoi/Bessel type

$$
2\pi\sqrt{nX}.
$$

This supports treating Mellin--Perron as a comparison route that likely reconstructs the same hard oscillatory scale. It is not yet a no-go theorem.

Gemini's Q1-Ext near-collision congruence bookkeeping is a useful algebraic input. For odd $d_1,d_2$ satisfying

$$
d_1b-d_2a=\Delta,
\qquad
(a,b)=1,
$$

the case $a,b$ both odd gives

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ab)(-1)^{\Delta/2}.
$$

This is potentially useful for signed spacing matrices, but no analytic saving follows until the sign is inserted into an actual Bombieri--Iwaniec near-collision matrix before absolute values erase it.

Gemini's C3-Mult parity-collapse observation is also useful in a narrow model. For

$$
\sigma(\xi)=\frac12(-1)^{2\xi},
\qquad
\xi\in \frac12\mathbb Z,
$$

an odd integer dilation $\xi_2=a\xi_1$ gives

$$
\sigma(\xi_1)\sigma(a\xi_1)
=
\frac14.
$$

This is a diagnostic for parity loss under one class of spacing transformations. It is not a universal obstruction to all two-coset spacing methods.

Rejected or risky ideas:

1. **Reject any claim of a new Gauss circle exponent.**

Round 9 improves the internal reduction and likely removes the residual bottleneck. It does not prove

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

because H5a-fix and H5b-fix remain open.

2. **Reject treating R5 as fully unconditional before H4 is cited precisely.**

R5 is conditionally proved from the standard Fejer-kernel majorant and the divisor bound. The repository still needs the exact Vaaler theorem statement, coefficient formula, Fejer normalization, and discontinuity convention. Once H4 is verified, R5 should be promoted to proved.

3. **Reject H5r-B and H5r-L1 as active proof dependencies.**

They are stronger than needed. H5r-B with arbitrary complex coefficients is essentially a dyadic $L^1$ target and is much harder than the actual fixed Fejer residual. Keep H5r-B/L1 as stress tests only.

4. **Reject a raw black-box invocation of Li--Yang on endpoint Vaaler blocks.**

The raw endpoint block violates Li--Yang Case A and Case B parameter ranges. Structural phase compatibility is insufficient.

5. **Reject a global no-go theorem for Li--Yang/Bombieri--Iwaniec methods.**

The raw theorem mismatch is proved. A full Bombieri--Iwaniec dissection has not been written for H5a-fix/H5b-fix. Do not claim all spacing methods fail.

6. **Reject Gemini's bounded-variation parity penalty as an obstruction after residue splitting.**

Inserting $1_{2\nmid d}$ directly as a continuous Li--Yang weight is invalid, but residue splitting $d=2m+1$ restores smooth/BV weights. The BV issue is a false-proof warning, not a fundamental obstruction.

7. **Reject Mellin--Perron "isomorphism" or "circular trap" language as theorem-level.**

The saddle computation is a useful diagnostic. A full theorem still requires sharp and smoothed Perron formulas, contour shifts, functional equations, kernel estimates, and transition analysis.

8. **Reject C3-Mult as a universal parity-loss theorem.**

It covers one stylized odd-dilation model. It does not rule out two-coset spacing, rational transformations, or signed matrix methods.

9. **Reject permanent retirement of signed Fourier truncation.**

R5 makes signed Fourier truncation lower priority, but it remains a comparison route. It should be de-prioritized, not deleted, until the main-term route is clearer.

Known gaps:

1. **Exact H4 reference and normalization.**

The proof needs a standard Vaaler theorem of the form

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)+R_H(t),
\qquad
|\alpha_h|\ll |h|^{-1},
$$

with

$$
|R_H(t)|\le \frac{C}{H}K_H(t)
$$

or the sharper normalization

$$
|R_H(t)|\le \frac{1}{2H+2}K_H(t).
$$

The exact constant is harmless for exponents but must be cited correctly.

2. **Complete R5 proof integration.**

The proof draft must explicitly handle:

- first leg $K_H(X/d)$;
- second leg $K_H((X/d+1)/4)$ and $K_H((X/d+3)/4)$;
- the zero Fejer mode;
- both signs of $k$;
- all dyadic $D$ blocks;
- short blocks $D<X^{1/4}$;
- possible signed or non-positive dyadic partitions, using $|w_D|$ if needed;
- small $X$ and endpoint cases.

3. **Main fixed-coefficient sums are open.**

After R5, the hard analytic targets are H5a-fix and H5b-fix:

$$
\mathcal M_1(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

The needed target is

$$
\mathcal M_i(D;X)\ll_\epsilon X^{1/4+\epsilon}
$$

per dyadic block, up to logarithmic losses.

4. **High-frequency gap after Li--Yang.**

Li--Yang's final circle/divisor range reaches only

$$
H\le D X^{-\theta^*},
\qquad
\theta^*=0.314483\cdots,
$$

whereas the endpoint Vaaler range requires

$$
H\le D X^{-1/4}.
$$

The uncovered range is

$$
D X^{-\theta^*}
\lesssim H
\lesssim
D X^{-1/4}.
$$

At $D\asymp X^{1/2}$, this is roughly

$$
X^{0.1855}
\lesssim H
\lesssim
X^{0.25}.
$$

Raw Case A/B constraints are even more restrictive. The next audit should focus on H5a-fix/H5b-fix, not residual H5r.

5. **C2-SP uniformity.**

The leading stationary phase is accepted, but a uniform lemma must handle:

$$
M_{\mathrm{dual}}\asymp kX/D^2\asymp 1,
$$

support-boundary stationary points, nonstationary tails, and derivative dependence of $w_D$.

6. **Q1-Ext analytic use is unproved.**

The sign

$$
\chi_4(ab)(-1)^{\Delta/2}
$$

must be inserted into a concrete spacing matrix. The key issue is whether matrix norm estimates preserve this sign or erase it by absolute values.

7. **H10 Mellin--Perron comparison remains incomplete.**

Need exact sharp/smoothed Perron errors, residue at $s=1$, functional equation for $4\zeta(s)L(s,\chi_4)$, Gamma factors, saddle analysis, and transition kernel estimates.

8. **Numerical tests remain mostly unrun.**

DeepSeek supplied a test plan, not data. The repo still lacks numerical evidence for R5, Fejer spikes, second-leg shifts, main-term sizes, signed Fourier tails, and Q1-Ext sign persistence.

New lemmas to add:

## R5. Fejer product-count bound for H5r-F

**Status:** provisionally proved conditional lemma; promote to proved after H4 is cited and the second leg is written explicitly.

Let $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, and

$$
H\asymp D X^{-1/4}.
$$

Let $w_D$ be a dyadic weight supported on $d\asymp D$ with $|w_D(d)|\le 1$. Then for every $\epsilon>0$,

$$
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
|w_D(d)|K_H(X/d)
\ll_\epsilon
X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H
\sum_{d\sim D}
|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Dependency: H4 plus $\tau(n)\ll_\epsilon n^\epsilon$.

Proof mechanism: reduce Fejer spikes to near-products $md\approx X$ or $(4m-\rho)d\approx X$ with interaction width

$$
\Delta=D/H\asymp X^{1/4}.
$$

Then group by the product and use the divisor bound.

## R5-Full. Total Vaaler residual bound

**Status:** proposed bridging lemma.

Assume H4 and R5 for every dyadic block. Then the total residual contribution from Vaaler in the balanced sawtooth formula is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof requirements: sum over all dyadic $D$, both sawtooth legs, both shifts $\rho=1,3$, signs of $k$, and short blocks. The number of dyadic blocks is $O(\log X)$ and is absorbed by $X^\epsilon$.

## M9. Fixed-coefficient main-term targets

**Status:** proposed exact replacement for overstrong H5a/H5b.

For

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2},
$$

define

$$
\mathcal M_1(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
\sum_{1\le |h|\le H_D}
\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

The desired local target is

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The old arbitrary-coefficient versions remain stress tests only.

## LY-Raw-Mismatch

**Status:** proved guardrail.

For the raw endpoint block

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$

Li--Yang Case A requires

$$
H\le MT^{-49/164}=X^{33/164},
$$

and Case B requires at least

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}.
$$

Both are below $X^{1/4}$. Therefore Li--Yang's main theorem cannot be quoted directly on the raw Vaaler endpoint block.

This does not preclude a full Bombieri--Iwaniec dissection or future stronger theorem.

## L9.1. Li--Yang endpoint non-import

**Status:** proved source-audit lemma.

The relevant reciprocal phases fit Li--Yang's broad phase form after residue splitting, but the theorem used for the circle/divisor problem gives

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\cdots,
$$

and does not supply the endpoint exponent $1/4$ or the full endpoint height

$$
H\le MT^{-1/4}.
$$

Also, Li--Yang's bounded-variation weights do not imply arbitrary-coefficient H5r-B or H5r-L1.

## C2-Alg. Odd-lattice Poisson transform

**Status:** proved algebraic lemma under fixed Fourier convention.

With

$$
e(t)=e^{2\pi i t},
\qquad
\widehat f(\xi)=\int f(u)e(-\xi u)\,du,
$$

one has

$$
\sum_{2\nmid d}f(d)
=
\frac12\sum_{m\in\mathbb Z}\widehat f(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
$$

## C2-SP0. Leading stationary phase for C2

**Status:** leading term accepted; uniform error not proved.

For

$$
\widehat f(-m)
=
\int w_D(u)e(kX/u+mu)\,du,
\qquad
m>0,
$$

the stationary point is

$$
u_0=\sqrt{kX/m}.
$$

In the interior range

$$
m\asymp kX/D^2,
$$

one has leading phase

$$
2\sqrt{kXm}
$$

and size

$$
|\widehat f(-m)|
\asymp
D^{3/2}(kX)^{-1/2}.
$$

## C2-SPU. Uniform C2 stationary phase

**Status:** required technical lemma, not proved.

Provide uniform estimates for C2-SP0 including:

- $m\asymp kX/D^2$ interior;
- $m$ outside the stationary range;
- $m\asymp 1$ boundary;
- stationary point near support boundary;
- derivative losses from $w_D$.

## B-Boundary. Small-frequency boundary bound

**Status:** proved elementary lemma.

For $D\asymp X^{1/2}$ and $1\le |k|\le X^\epsilon$,

$$
\frac1{H_D}|S_\star(k,D)|
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof: use $|S_\star(k,D)|\ll D$ and $H_D\asymp D X^{-1/4}$.

## Q1-Ext. Near-collision character factorization

**Status:** proved algebraic lemma; analytic use pending.

If $(a,b)=1$ and odd $d_1,d_2$ satisfy

$$
d_1b-d_2a=\Delta,
$$

then in the both-odd slope case,

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ab)(-1)^{\Delta/2}.
$$

This must be inserted into a real spacing matrix before it can be counted as analytic progress.

## C3-Mult. Multiplicative parity-collapse diagnostic

**Status:** proved in a narrow model; diagnostic only.

For

$$
\sigma(\xi)=\frac12(-1)^{2\xi},
\qquad
\xi\in\frac12\mathbb Z,
$$

odd integer dilation $\xi_2=a\xi_1$ gives

$$
\sigma(\xi_1)\sigma(a\xi_1)=\frac14.
$$

This diagnoses parity loss for odd-dilation models, not for all spacing methods.

## H10-M. Mellin--Perron dual-length diagnostic

**Status:** comparison lemma, not a no-go theorem.

A sharp Perron height near

$$
T\asymp X^{3/4}
$$

leads after functional equation and stationary phase to dual length

$$
n\lesssim T^2/X\asymp X^{1/2}
$$

and phase of type

$$
2\pi\sqrt{nX}.
$$

The exact contour theorem remains unwritten.

Counterexample checks to run:

1. **R5 Fejer product-count numerical test.**

For square, nonsquare, near-square, and divisor-rich $X$, compute

$$
\frac1{H_D}
\sum_{d\sim D}K_{H_D}(X/d)
$$

for several $D$, especially

$$
D\asymp X^{1/2}
$$

and

$$
D\asymp X^{3/8}.
$$

Compare with $X^{1/4}$.

2. **Second-leg shift test.**

Compute

$$
\frac1{H_D}
\sum_{d\sim D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\},
$$

and verify that divisibility/congruence spikes remain within $X^{1/4+\epsilon}$.

3. **Vaaler discontinuity test.**

At arguments where

$$
X/d\in\mathbb Z
$$

or

$$
\frac{X/d+\rho}{4}\in\mathbb Z,
$$

check that the Fejer majorant covers the discrepancy between the floor-compatible sawtooth value and the trigonometric polynomial.

4. **R5 full-block summation test.**

Verify that short blocks $D<X^{1/4}$, dyadic boundaries, both signs of $k$, zero modes, and both H3 legs sum to $O_\epsilon(X^{1/4+\epsilon})$.

5. **Li--Yang raw block audit.**

Record exact source constraints for Case A, Case B, the definition of $S$, the conditions on $F$, and the target $S/H$. Check both residual and main-term parameter substitutions.

6. **Li--Yang dissection map for main terms.**

Carry out an actual Bombieri--Iwaniec dissection for H5a-fix/H5b-fix. Determine effective parameters and identify exactly where the high-frequency gap persists.

7. **Main-term size numerics.**

For H5a-fix and H5b-fix, compute the fixed-coefficient sums with $\alpha_h$ for representative $X,D$. Compare against $X^{1/4}$ and against arbitrary-coefficient/L1 stress norms.

8. **Q1-Ext signed matrix test.**

Build a toy rational-collision matrix with entries retaining

$$
\chi_4(ab)(-1)^{\Delta/2}.
$$

Compare its spectral norm with the absolute-value matrix. Identify whether standard Cauchy--Schwarz erases the sign.

9. **C2-SP transition test.**

Numerically and symbolically test the regime

$$
kX/D^2\asymp 1
$$

where dual length is short and uniform stationary phase is delicate.

10. **Mellin--Perron comparison test.**

Write sharp and smoothed Perron errors with explicit $T$-dependence, apply the functional equation, and verify the dual length $T^2/X$ including boundary kernels.

Next round instructions:

## For `gpt_pro_thinking`

1. Write a complete proof of R5.

Include:

- exact Fejer-kernel pointwise bound;
- first-leg product-count proof;
- second-leg shifted proof with $4m-\rho$ congruence;
- divisor-bound summation;
- treatment of $X$ noninteger;
- constants absorbed by $X^\epsilon$;
- dyadic block summation;
- zero mode and both signs of $k$.

2. Verify H4 from a standard reference.

State the precise Vaaler theorem and the exact normalization of $K_H$. Do not rely on an informal "standard Vaaler" citation.

3. Insert R5 and R5-Full into the best proof draft.

Move H5r-F from "central bottleneck" to "cleared conditional on H4/R5 verification." Move H5r-B and H5r-L1 to optional stress-test status.

4. Formulate H5a-fix and H5b-fix as the official main-term targets.

Use the actual Vaaler coefficients $\alpha_h$, including signs and $1/h$ decay.

5. Compare H5a-fix/H5b-fix with Li--Yang.

Identify which subrange, if any, current Li--Yang technology covers, and isolate the high-frequency gap

$$
D X^{-\theta^*}
\lesssim H
\lesssim
D X^{-1/4}.
$$

## For `deepseek_api`

1. Run numerical R5 stress tests.

Compute first-leg and second-leg Fejer product-count sums for square, nonsquare, near-square, and divisor-rich $X$.

2. Verify the Li--Yang source constraints independently.

Record the exact TeX labels and the conditions used in LY-Raw-Mismatch and L9.1.

3. Audit possible main-term complete-sum mechanisms.

Check whether residue splitting, Gaussian integers, or complete sums modulo auxiliary moduli can create genuine character cancellation for H5a-fix/H5b-fix. Explicitly avoid invoking Weil/Deligne unless a genuine complete character sum with a nontrivial modulus is written.

4. Finish C2-SPU.

Provide uniform stationary-phase estimates for the odd-lattice Poisson transform, including short dual length and boundary stationary points.

## For `gemini_deep_think`

1. Insert Q1-Ext into an actual signed spacing matrix.

Determine whether the factor

$$
\chi_4(ab)(-1)^{\Delta/2}
$$

survives matrix norm estimates or is erased by absolute values.

2. Refine C3-Mult.

Analyze even dilations and more realistic rational/unimodular spacing transformations. Keep the conclusion diagnostic unless a full spacing model is proved.

3. Develop H10-M to theorem-dependency level.

Write exact sharp and smoothed Perron formulas for

$$
4\zeta(s)L(s,\chi_4),
$$

then derive the dual phase and length with all error terms.

4. Soften impossibility language.

Use "raw theorem mismatch," " diagnostic," and "unproved obstruction" unless a precise theorem is supplied.

## General state update

Update:

- `state/current_state.md`;
- `state/lemma_bank.md`;
- `state/gap_register.md`;
- `state/best_proof_draft.md`;
- `manifests/reading_packet.md`.

Record Round 9 as a progress round that likely clears the fixed Fejer residual and redirects attention to fixed-coefficient main sums. Preserve the no-exponent-improvement status.

Confidence:

High confidence in the selected route as the correct reduction framework.

High confidence that R5 is mathematically sound **conditional on the standard Fejer majorant H4**.

Moderate-to-high confidence that R5 clears H5r-F after the second leg and full dyadic summation are written carefully.

High confidence that H5r-B and H5r-L1 are overstrong and should not be active dependencies.

High confidence that Li--Yang cannot be quoted directly on the raw endpoint Vaaler block.

High confidence that Li--Yang's published exponent $\theta^*=0.314483\cdots$ does not supply the conjectural endpoint $1/4$.

High confidence in C2-Alg under the stated Fourier convention.

Moderate confidence in C2-SP0 leading stationary phase; low-to-moderate confidence in uniform C2-SPU until transition and boundary estimates are written.

Moderate confidence that Mellin--Perron reconstructs the Hardy/Voronoi/Bessel scale; low confidence that it gives an escape route without new moment or kernel estimates.

Moderate confidence that Q1-Ext is algebraically useful; low confidence that it gives analytic savings until tested in an actual spacing matrix.

Low confidence that current known technology proves H5a-fix/H5b-fix at the endpoint. The hard problem has moved from the residual to the fixed-coefficient main sums, not disappeared.

## Round 10 Update

Timestamp: 2026-06-01 12:02:25

See `rounds/web-research-test/round_010/judge/judge.md`.

Summary:

Round 10 is a genuine precision round, not an exponent-improvement round. Source anchor: uploaded Round 10 packet and agent outputs; background overview packet.

The main state update is:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

where H1--H3 are the proved balanced hyperbola/sawtooth reductions, H4 is the finite Vaaler theorem with Fejer residual majorant, R5-Full is the total Fejer residual bound, and M9 is the pair of fixed-Vaaler-coefficient main-term estimates.

Round 10 strongly supports moving the fixed Fejer residual H5r-F off the critical path, conditional on a page-level verification of H4 and a complete write-up of R5-Full. The remaining hard problem is now sharply isolated as the fixed-coefficient Vaaler main sums. No new Gauss circle exponent has been proved.

Selected main route:

Keep the balanced arithmetic hyperbola/Vaaler reduction as the primary framework:

$$
P(X)=N(\sqrt X)-\pi X
\to
\text{symmetric hyperbola}
\to
\text{floor-compatible sawtooth}
\to
\text{finite Vaaler}
\to
\text{fixed-coefficient reciprocal sums}.
$$

The proved arithmetic identity remains:

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

with

$$
y=\lfloor X^{1/2}\rfloor,
\qquad
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

For each dyadic block $d\asymp D$ in

$$
X^{1/4}\le D\le X^{1/2},
$$

use the local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

Short blocks $D<X^{1/4}$ remain trivially bounded by $O(X^{1/4})$ after summing over dyadic ranges.

The selected proof skeleton after Round 10 is:

1. Apply H4 blockwise to the two sawtooth legs.
2. Bound all Fejer residuals directly by R5 product-counting, not by arbitrary $k$-coefficient reciprocal sums.
3. Reduce the conjectural bound to the fixed main-term estimates M9:

$$
\mathcal M_1(D;X)
=
-4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\sum_{d\sim D}
\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\mathcal M_2(D;X)
=
4\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}
\left(e(h/4)-e(3h/4)\right)
\sum_{d\sim D}
w_D(d)e(hX/(4d)).
$$

Since

$$
e(h/4)-e(3h/4)=2i\chi_4(h),
$$

the second main term may be written as

$$
\mathcal M_2(D;X)
=
8i\sum_{1\le |h|\le H_D}
\alpha_{h,H_D}\chi_4(h)
\sum_{d\sim D}
w_D(d)e(hX/(4d)).
$$

The target is:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}
$$

uniformly over dyadic $D$, with logarithmic losses absorbed into $X^\epsilon$.

Useful fragments by source:

## From `gpt_pro_thinking`

The main useful contribution is the complete lemma-level R5 proof and residual bridge.

The required Vaaler theorem was stated in the precise form needed for the repo. With

$$
e(t)=e^{2\pi i t},
$$

define

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

Let

$$
\Phi(u)=\pi u(1-|u|)\cot(\pi u)+|u|,
\qquad
0<|u|<1,
$$

with continuous extension $\Phi(0)=1$. The required imported theorem is:

$$
\psi(t)
=
-\sum_{1\le |h|\le H}
\frac{\Phi(h/(H+1))}{2\pi i h}e(ht)
+
R_H(t),
$$

with

$$
|R_H(t)|\le \frac1{2H+2}K_H(t).
$$

Thus

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h},
\qquad
|\alpha_{h,H}|\ll |h|^{-1}.
$$

This theorem still needs a page-level source audit, especially for the constant, coefficient convention, and discontinuity value $\psi(n)=-1/2$.

The R5 proof uses the standard pointwise Fejer bound

$$
K_H(t)\ll \min\left(H,\frac1{H\|t\|^2}\right),
$$

hence

$$
\frac1H K_H(t)
\ll
\min\left(1,\frac1{H^2\|t\|^2}\right).
$$

For the first residual leg,

$$
\frac1H
\sum_{d\sim D}
K_H(X/d),
$$

choose $m$ nearest to $X/d$. For $d\asymp D$,

$$
\left\|\frac Xd\right\|
=
\frac{|X-md|}{d}
\asymp
\frac{|X-md|}{D}.
$$

With

$$
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

the summand is bounded by

$$
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Grouping by $n=md$ gives at most $\tau(n)$ representations, so

$$
\frac1H\sum_{d\sim D}K_H(X/d)
\ll
\sum_{n\asymp X}\tau(n)
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

The last estimate uses

$$
\tau(n)\ll_\epsilon n^\epsilon
$$

and

$$
\sum_{n\in\mathbb Z}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right)
\ll \Delta+1.
$$

This is uniform for real $X$.

For the second residual leg,

$$
\frac1H
\sum_{d\sim D}
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad \rho\in\{1,3\},
$$

near-integrality is equivalent to

$$
X\approx d(4m-\rho).
$$

Writing

$$
\ell=4m-\rho
$$

again gives a product $n=d\ell$ with only a congruence restriction on $\ell$, so the ordinary divisor bound still applies. This is the correct mechanism for clearing the shifted second leg.

The second important contribution is the replacement of the old arbitrary-coefficient H5a/H5b by fixed-coefficient M9. This prevents the repo from requiring a stronger theorem than the actual Vaaler reduction needs.

The third useful contribution is the careful Li--Yang comparison. H5a-fix is structurally compatible with Li--Yang/Bombieri--Iwaniec reciprocal phases after splitting $d\bmod 4$, but the published theorem does not reach the endpoint Vaaler height. H5b-fix also has an additional theorem-extension gap because $\chi_4(h)$ either gives a non-smooth periodic $h$-weight or, after splitting $h\bmod 4$, a shifted-frequency phase $e((q+\beta)X/d)$.

## From `deepseek_api`

The strongest useful contribution is independent verification of R5 and the Li--Yang source audit.

DeepSeek confirmed the R5 product-count mechanism for both legs and correctly emphasized that H5r-F is provisionally cleared only after H4 is source-verified and R5-Full is written into the proof draft.

DeepSeek also extracted the relevant Li--Yang parameter mismatch. In the raw endpoint block,

$$
T=X,
\qquad
M=D\asymp X^{1/2},
\qquad
H=H_D\asymp X^{1/4}.
$$

Li--Yang Case A imposes

$$
H\le MT^{-49/164}=X^{33/164}\approx X^{0.2012},
$$

and Case B imposes

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}=X^{1/6}.
$$

Both are below $X^{1/4}$. Therefore Li--Yang cannot be quoted directly on the raw endpoint Vaaler block. This is a theorem-application guardrail, not a no-go theorem for every possible Bombieri--Iwaniec dissection.

DeepSeek also kept C2-SPU in the correct status: the leading stationary-phase scale is understood, but the uniform lemma is not fully proved. For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

the active sign is $\xi<0$. Writing $\xi=-m$, the stationary point is

$$
u_0=\sqrt{\frac{kX}{m}},
$$

and the active dual length is

$$
m\asymp \frac{kX}{D^2}.
$$

The leading size in the interior is

$$
|I(-m)|\asymp D^{3/2}(kX)^{-1/2}.
$$

Uniform boundary, transition, and nonstationary estimates are still missing.

## From `gemini_deep_think`

The most useful contribution is Q1-Spectral, the operator-norm character-blindness diagnostic.

For a spacing matrix

$$
K_{d_1,d_2}
=
\sum_h e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right),
$$

the spatial character enters through the test vector

$$
v_d=\chi_4(d)w_D(d).
$$

On odd $d$, multiplication by $\chi_4(d)$ is a diagonal unitary operator $U$. Thus

$$
v^*Kv
=
w^*(U^*KU)w,
$$

but

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

Therefore any method that bounds the signed quadratic form only through an operator norm, Schur bound, Gershgorin-type bound, or absolute-value matrix cannot exploit the diagonal $\chi_4$ signs. This is an important guardrail for future spacing arguments.

This should be recorded as a diagnostic, not as an impossibility theorem. It does not rule out signed bilinear estimates, trace/cycle estimates, residue-interference methods, or a Bombieri--Iwaniec dissection that estimates the signed form directly.

Gemini also contributed useful C3 parity diagnostics. Integer translations in the two-coset odd-lattice model erase parity oscillation:

$$
\sigma(\xi)=\frac12(-1)^{2\xi},
\qquad
\sigma(\xi)\sigma(\xi+q)=\frac14
$$

for integer $q$, up to the fixed convention. But the rational-dilation variants need to be rewritten carefully and connected to actual spacing transformations before they become proof-relevant.

Gemini's Mellin--Perron analysis should be kept as a comparison module. The contour/functional-equation route appears to reconstruct Hardy--Voronoi--Bessel phases of type

$$
2\pi\sqrt{nX}
$$

with dual length about

$$
n\lesssim T^2/X.
$$

For endpoint smoothing/truncation with $T\asymp X^{3/4}$ this gives dual length $X^{1/2}$. This is a useful diagnostic that Mellin--Perron likely mirrors known oscillatory difficulty, but it is not yet a theorem-level equivalence.

## From Stage B reviews

The cross-reviews agree on the main synthesis:

- R5 is the principal Round 10 mathematical advance.
- H5r-F should be demoted from active central bottleneck to provisionally cleared residual input.
- H5r-B and H5r-L1 should be retained only as stress tests.
- M9 fixed-coefficient main terms are now the hard target.
- Li--Yang cannot be used as a black box on the raw endpoint block.
- Q1-Spectral is valuable but must be phrased as an operator-norm-only diagnostic.
- No exponent improvement has been proved.

Rejected or risky ideas:

1. **Reject any claim of a new Gauss circle exponent.**

Round 10 clears or nearly clears the residual side of the Vaaler reduction, but the fixed-coefficient main sums M9 remain open. Therefore the conjectural estimate

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}
$$

has not been proved.

2. **Reject marking R5 as fully unconditional before H4 is source-verified.**

The product-counting proof is strong, but its use in the sawtooth approximation depends on H4. The exact Vaaler theorem, coefficient normalization, Fejer-kernel normalization, and discontinuity convention must be cited from a standard source.

3. **Reject keeping H5r-B and H5r-L1 as active dependencies.**

Those arbitrary-coefficient or termwise $L^1$ residual targets are stronger than what the Vaaler proof actually needs. R5 controls the positive Fejer majorant directly. H5r-B and H5r-L1 should remain stress tests only.

4. **Reject a black-box Li--Yang invocation at the endpoint.**

The raw endpoint Vaaler block violates the audited Case A/B height bounds. Structural phase compatibility is insufficient.

5. **Reject a global no-go theorem for Bombieri--Iwaniec/Li--Yang methods.**

The raw theorem mismatch is proved only for direct application. A full dissection could alter effective parameters, and a future first-spacing or signed-spacing input could change the situation. Do not state that all spacing methods fail.

6. **Reject overstrong Q1-Spectral language.**

Q1-Spectral shows that operator-norm-only arguments are character-blind. It does not prove that every signed spacing or trace method loses the character.

7. **Reject treating H5b-fix as automatically covered by H5a-fix technology.**

H5b-fix places $\chi_4$ in the frequency variable. Splitting $h\bmod 4$ creates shifted frequencies $q+\beta$, $\beta\in\{1/4,3/4\}$. A theorem permitting such fixed fractional shifts must be stated or proved.

8. **Reject treating signed Fourier truncation as an established escape.**

The high-frequency signed tail may preserve signs formally, but near discontinuities it appears to produce small-denominator barriers comparable to Fejer. No endpoint tail estimate has been proved.

9. **Reject Mellin--Perron "isomorphism" or "circular trap" as theorem-level.**

The saddle computation is valuable, but exact sharp/smoothed Perron errors, functional equation normalization, kernel estimates, and transition analysis are not yet written.

10. **Reject treating C2-SPU as proved.**

The leading stationary point and amplitude are accepted, but the uniform stationary-phase lemma with support-boundary and short-dual-length transitions remains open.

Known gaps:

1. **H4 source and convention audit.**

Need a precise citation for:

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H(t),
$$

with

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h}
$$

or the equivalent standard convention, and

$$
|R_H(t)|\le \frac1{2H+2}K_H(t)
$$

or another explicitly normalized $O(H^{-1}K_H)$ bound.

The source audit must verify that the floor-compatible convention $\psi(n)=-1/2$ is covered by the residual.

2. **R5-Full write-up gap.**

The proof draft must explicitly cover:

- first leg $K_H(X/d)$;
- second leg $K_H((X/d+1)/4)$ and $K_H((X/d+3)/4)$;
- integer and noninteger $X$;
- nearest-integer choices;
- possible small or finite endpoint cases;
- the zero Fejer mode;
- both signs of $k$;
- dyadic partitions with possibly signed weights, handled by $|w_D|$;
- short blocks $D<X^{1/4}$;
- absorption of $O(\log X)$ dyadic losses into $X^\epsilon$.

3. **Terminology gap: H5r-F versus direct Fejer-majorant bound.**

Earlier H5r-F was phrased as a fixed Fourier average over $k$. R5 bypasses that formulation by bounding the positive Fejer kernel directly. The proof draft should say explicitly that the residual is controlled by R5-Full; it need not continue treating H5r-F as an independent Fourier-sum target.

4. **M9 main-term estimates are open.**

The official target is now:

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon}.
$$

No agent supplied an endpoint proof for these sums.

5. **H5b-fix shifted-frequency theorem gap.**

After splitting $h\bmod 4$,

$$
\chi_4(h)e(hX/(4d))
$$

leads to sums with phase

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\}.
$$

A Bombieri--Iwaniec/Li--Yang theorem with this fixed fractional shift must be stated and verified, or this remains a separate obstruction.

6. **Li--Yang high-frequency gap.**

Known Li--Yang technology reaches a record exponent

$$
\theta^*=0.314483\cdots
$$

in the relevant $X$-notation, not the conjectural $1/4$. The endpoint Vaaler range requires

$$
H\le D X^{-1/4},
$$

while the final record-exponent range only reaches approximately

$$
H\le D X^{-\theta^*}.
$$

At $D\asymp X^{1/2}$, this leaves the gap

$$
X^{0.1855\cdots}
\lesssim H
\lesssim
X^{1/4}.
$$

The raw Case A/B restrictions are even more restrictive and must be kept distinct from this final-record range.

7. **Q1-Spectral exact-matrix gap.**

The diagonal-unitary argument must be attached to the actual spacing matrix used in a Bombieri--Iwaniec or large-sieve step. If the method already takes absolute values earlier, the result is even more directly character-blind; if not, a signed-form estimate may still be possible.

8. **Signed trace/cycle route undeveloped.**

The proposed escape route should define an actual signed spacing matrix and a concrete statistic, for example a trace or fourth moment, in which products of $\chi_4$ survive closed cycles. No such lemma has yet been proved.

9. **C2-SPU uniform stationary phase.**

Need a theorem covering:

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

including active sign, stationary point, leading phase, amplitude, nonstationary decay by integration by parts, support-boundary transitions, and short-dual-length cases.

10. **Mellin--Perron and signed Fourier comparison gaps.**

Both routes remain comparison tools. They need exact replacement error terms before they can be judged as genuine alternatives.

11. **Numerical data are still absent.**

The repo has test plans but not committed numerical output for R5, Fejer spikes, second-leg shifts, M9 fixed-coefficient sums, Q1-Spectral matrix norms, or C2 stationary phase.

New lemmas to add:

## H4. Vaaler finite approximation with Fejer residual

**Status:** external theorem dependency; statement precise, source normalization pending.

For $H\ge1$,

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_{h,H}e(ht)+R_H(t),
$$

where

$$
\alpha_{h,H}
=
-\frac{\Phi(h/(H+1))}{2\pi i h},
\qquad
|\alpha_{h,H}|\ll |h|^{-1},
$$

and

$$
|R_H(t)|\le \frac1{2H+2}K_H(t).
$$

The exact coefficient function and constant must be source-verified.

## R5. Fejer product-count residual bound

**Status:** provisionally proved conditional on H4; promote after H4 and R5-Full write-up.

Let $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp D X^{-1/4}$, and let $|w_D|\le1$ be supported on $d\asymp D$. Then

$$
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
|w_D(d)|K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and for $\rho\in\{1,3\}$,

$$
\frac1H
\sum_{d\sim D}
|w_D(d)|
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof dependencies: Fejer pointwise bound and $\tau(n)\ll_\epsilon n^\epsilon$.

## R5-Full. Total Vaaler residual bound

**Status:** conditional bridge lemma; write into best proof draft.

Assume H4 and R5 on every dyadic block. Then the full Vaaler residual contribution in H3 is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

This includes both sawtooth legs, both shifts $\rho=1,3$, zero modes, both signs of frequency, and short dyadic blocks.

## M9. Fixed-coefficient main-term criterion

**Status:** official remaining main analytic target.

Let

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

Define $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$ as above. If for every dyadic $D$,

$$
\mathcal M_1(D;X),\mathcal M_2(D;X)
\ll_\epsilon X^{1/4+\epsilon},
$$

then H1--H4 plus R5-Full imply

$$
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

## H5r-B/H5r-L1 demotion

**Status:** stress tests only.

The arbitrary-coefficient and termwise-$L^1$ residual targets are no longer active proof dependencies unless R5 fails. They remain useful for numerical comparison and for detecting whether fixed Fejer structure is essential.

## LY-Raw-Mismatch

**Status:** proved theorem-application guardrail.

For the raw endpoint block

$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$

Li--Yang Case A allows at most

$$
H\le MT^{-49/164}=X^{33/164},
$$

and Case B allows at most

$$
H\le M^{35/69}T^{-2/23}=X^{23/138}.
$$

Both are below $X^{1/4}$. Therefore the audited theorem cannot be quoted directly for the raw endpoint Vaaler block.

## LY-Endpoint-Gap

**Status:** diagnostic.

The final record-exponent range associated with Li--Yang reaches only

$$
H\le D X^{-\theta^*},
\qquad
\theta^*=0.314483\cdots,
$$

whereas the conjectural Vaaler endpoint requires

$$
H\le D X^{-1/4}.
$$

The uncovered high-frequency range is

$$
D X^{-\theta^*}
\lesssim H
\lesssim
D X^{-1/4}.
$$

This is not a no-go theorem.

## M9a-LY-Dictionary

**Status:** structural compatibility only.

After splitting $d\bmod4$, H5a-fix becomes a difference of reciprocal sums with smooth residue-class weights and phase

$$
e\left(\frac{hX}{4m+r}\right),
\qquad r\in\{1,3\}.
$$

This fits the broad reciprocal phase class, but endpoint theorem applicability is not established.

## M9b-Shift

**Status:** required theorem-extension gap.

After splitting $h\bmod4$, H5b-fix contains shifted-frequency phases

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\}.
$$

A theorem allowing these fixed fractional shifts in the relevant spacing framework must be proved or cited.

## Q1-Spectral

**Status:** proved diagnostic for operator-norm-only methods.

If the $\chi_4(d)$ signs enter only through a diagonal unitary conjugation of a spacing matrix, then estimates depending only on the operator norm cannot exploit those signs:

$$
\|U^*KU\|_{\operatorname{op}}=\|K\|_{\operatorname{op}}.
$$

This blocks character gains from operator-norm-only or absolute-value spacing estimates, but not from signed-form or trace/cycle estimates.

## H12. Signed spacing trace target

**Status:** proposed next route.

Define an actual signed spacing matrix $K^\chi$ arising from M9a, retaining the factor

$$
\chi_4(d_1)\chi_4(d_2).
$$

Formulate a trace or fourth-moment statistic, such as a signed analogue of $\operatorname{Tr}((KK^*)^2)$, and determine whether Q1-Ext signs survive closed collision cycles before absolute values are taken.

## C2-SPU. Uniform odd-lattice stationary phase

**Status:** required technical lemma, not proved.

For

$$
I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du,
$$

prove uniform estimates in all regimes, including

$$
|\xi|\asymp kX/D^2,
$$

nonstationary ranges, support-boundary transitions, and short-dual-length cases.

## H10-M. Mellin--Perron comparison module

**Status:** comparison route, not an escape.

A sharp or smoothed Perron formulation for

$$
4\zeta(s)L(s,\chi_4)
$$

should be developed far enough to show precisely which dual sums and kernels arise after the functional equation. Current saddle analysis suggests Hardy--Voronoi--Bessel phases, not an easier endpoint problem.

## SF1-Tail. Signed Fourier tail comparison

**Status:** diagnostic only.

For the formal signed tail after truncating

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi i h},
$$

derive a rigorous bound such as

$$
\left|\sum_{|h|>H}\frac{e(ht)}{h}\right|
\ll \frac{1}{H\|t\|}
$$

away from discontinuities, then compare the resulting $d$-sum with the Fejer residual. Do not claim equivalence until the discontinuity and summability conventions are fixed.

Counterexample checks to run:

1. **R5 first-leg numerical stress test.**

For square, nonsquare, near-square, and divisor-rich $X$, compute

$$
\frac1{H_D}
\sum_{d\sim D}K_{H_D}(X/d)
$$

for $D\asymp X^{1/4}$, $X^{3/8}$, and $X^{1/2}$.

2. **R5 second-leg shift test.**

For $\rho\in\{1,3\}$, compute

$$
\frac1{H_D}
\sum_{d\sim D}
K_{H_D}\left(\frac{X/d+\rho}{4}\right),
$$

especially when $X\approx d(4m-\rho)$ has many product representations.

3. **Vaaler discontinuity test.**

Test cases where

$$
X/d\in\mathbb Z
$$

or

$$
\frac{X/d+\rho}{4}\in\mathbb Z.
$$

Verify that the residual majorant covers the discrepancy between the floor-compatible sawtooth convention and the trigonometric approximation.

4. **R5-Full dyadic summation test.**

Check full summation over all dyadic $D$, including $D<X^{1/4}$, dyadic boundary overlaps, both sawtooth legs, and both signs of the Fejer frequencies.

5. **M9 fixed-coefficient numerics.**

Compute

$$
\mathcal M_1(D;X)
$$

and

$$
\mathcal M_2(D;X)
$$

with the actual Vaaler coefficients $\alpha_{h,H_D}$. Compare against $X^{1/4}$ and against arbitrary-coefficient or $L^1$ stress norms.

6. **H5b shifted-frequency test.**

Numerically and symbolically compare sums with phases

$$
e(qX/d)
$$

and

$$
e((q+\beta)X/d),
\qquad
\beta\in\{1/4,3/4\}.
$$

Identify which steps of a Bombieri--Iwaniec dissection are invariant under the shift and which are not.

7. **Li--Yang theorem audit.**

Record exact TeX labels, hypotheses, and parameter substitutions for the theorem. Distinguish raw Case A/B height restrictions from the final record-exponent range.

8. **Q1-Spectral matrix test.**

Construct the actual near-collision kernel

$$
K_{d_1,d_2}
=
\sum_{1\le |h|\le H_D}
|\alpha_h|^2
e\left(hX\left(\frac1{d_1}-\frac1{d_2}\right)\right)
$$

or the precise kernel generated by the intended Cauchy--Schwarz step. Compare bounds for $K$ and $U^*KU$.

9. **Signed trace/cycle toy model.**

Compute a toy fourth-moment or trace statistic retaining

$$
\chi_4(d_1)\chi_4(d_2)
$$

and test whether Q1-Ext signs survive beyond absolute-value majorization.

10. **C2-SPU transition test.**

Test numerically and symbolically the regimes

$$
kX/D^2\asymp 1,
$$

stationary point near support boundary, and nonstationary tails.

11. **Mellin--Perron comparison test.**

Write sharp and smoothed Perron errors with explicit $T$-dependence, apply the functional equation for $4\zeta(s)L(s,\chi_4)$, and verify the dual length $T^2/X$ and phase $2\pi\sqrt{nX}$ including transition kernels.

12. **Signed Fourier tail test.**

Compare the signed Fourier tail with the Fejer majorant for arguments close to integers. Determine whether sign preservation survives summation over $d$ or whether the same product-count/small-denominator structure reappears.

Next round instructions:

## For `gpt_pro_thinking`

1. Verify H4 from a standard reference.

State the exact theorem with coefficient function, Fejer kernel normalization, residual constant, and sawtooth convention. Do not rely on an informal "standard Vaaler" citation.

2. Write R5-Full as a complete proof in the best proof draft.

Include first leg, shifted second leg, real $X$, endpoint cases, dyadic partitions, zero mode, both frequency signs, short blocks, and absorption of logarithms.

3. Insert the Round 10 bridge theorem:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

4. Freeze M9 as the official main-term target.

Use the exact $\alpha_{h,H_D}$ coefficients and do not revert to arbitrary $u_h$ unless explicitly running a stress test.

5. Write the H5b-Shift theorem-extension problem.

State precisely what a Bombieri--Iwaniec/Li--Yang method must prove for phases $e((q+\beta)X/d)$.

## For `deepseek_api`

1. Independently verify the H4 source.

Check the coefficient formula, constant, and convention against Vaaler's paper or a reliable modern exposition.

2. Run R5 numerical stress tests.

Include first leg, second leg, squares, near-squares, nonsquares, and divisor-rich $X$.

3. Run M9 main-term numerics with actual $\alpha_h$.

Compare fixed-coefficient sums with arbitrary-coefficient and $L^1$ stress versions.

4. Verify the Li--Yang source constraints with exact labels.

Record raw Case A/B restrictions, final exponent range, function hypotheses, weight hypotheses, and whether shifted frequencies are allowed.

5. Continue C2-SPU.

Provide a complete uniform stationary-phase lemma, explicitly correcting any overstrong "exponential decay" language to rapid integration-by-parts decay unless analyticity is assumed.

## For `gemini_deep_think`

1. Formalize Q1-Spectral as a diagnostic lemma.

State exactly which operator-norm or large-sieve steps are character-blind and which signed-form estimates remain open.

2. Define a concrete H12 signed spacing/trace model.

Use the actual M9a near-collision kernel and the Q1-Ext character factors. Determine whether signs survive a fourth-moment or trace estimate before absolute values enter.

3. Repair and classify C3-Affine/C3-Rational.

Fix notation, state exact parity cases, and connect the transformations to actual two-coset spacing geometry. Keep conclusions diagnostic unless a theorem is proved.

4. Keep Mellin--Perron as a comparison route.

Develop sharp/smoothed Perron formulas and saddle analysis only to theorem-dependency level; avoid "isomorphism" or "no-go" language unless exact kernels and errors are proved.

5. Analyze signed Fourier truncation as a comparison, not a bypass.

State the exact tail bound and identify whether the high-frequency tail reduces to product-counting, Fejer-type, or genuinely sign-preserving estimates.

## General state update

Update the following files:

- `state/current_state.md`;
- `state/lemma_bank.md`;
- `state/gap_register.md`;
- `state/best_proof_draft.md`;
- `manifests/reading_packet.md`.

Record Round 10 as a progress round that provisionally clears the fixed Fejer residual and redirects the main analytic burden to M9 fixed-coefficient Vaaler main sums. Preserve the no-exponent-improvement status.

Confidence:

High confidence in the selected balanced hyperbola/Vaaler reduction as the correct current framework.

High confidence in H1--H3.

High confidence that R5 is mathematically sound conditional on the H4 Fejer majorant.

Moderate-to-high confidence that R5-Full clears the total Vaaler residual after a careful complete write-up.

High confidence that H5r-B and H5r-L1 are overstrong and should not be active dependencies.

High confidence that the official remaining targets are M9 fixed-coefficient main sums.

High confidence that Li--Yang cannot be imported as a black box for the raw endpoint Vaaler block.

Moderate confidence that H5a-fix is structurally inside a Bombieri--Iwaniec/Li--Yang reciprocal phase class after residue splitting.

Moderate-to-low confidence that H5b-fix can be handled by existing printed theorems without a shifted-frequency extension.

Moderate confidence that Q1-Spectral is a useful operator-norm guardrail; low confidence that it rules out all signed spacing approaches.

Moderate confidence in the C2 stationary-phase leading term; low-to-moderate confidence in the uniform C2-SPU until transition and boundary estimates are written.

Low confidence that current known technology proves M9 at the endpoint.

Overall Round 10 judgment: productive and mathematically meaningful. The Fejer residual bottleneck is provisionally cleared; the proof skeleton is now sharper. The hard problem has not vanished, but it has moved to a precise pair of fixed-coefficient main-term estimates and to the question of whether any sign-preserving spacing method can exploit $\alpha_h$ and $\chi_4$ before standard norm estimates erase them.

## Lemma Bank

# Lemma Bank

## Proposed

No proposed lemmas yet.

## Plausibly Proved

None yet.

## Rejected Or Risky

None yet.

## Gap Register

# Gap Register

No gaps registered yet.

## Best Proof Draft

# Best Proof Draft

No proof draft yet.

## Latest Round

Responses, reviews, and judge synthesis are archived under `rounds/web-research-test/round_010/`.
