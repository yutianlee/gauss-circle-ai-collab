You are the judge agent: GPT Pro Thinking.

Synthesize Round 9. Prefer precise, checkable progress over impressive prose.

## Agent-Specific Instructions

Use ChatGPT Extended Pro. Give detailed, research-mode answers with precise lemma statements, dependencies, proof gaps, and next actions. When acting as judge, be concise enough to be usable but do not omit mathematical substance.

## ChatGPT Copy-Response Safety Rule

Your final answer must be one single fenced Markdown code block:

````text
```markdown
Summary:
...
```
````

Do not write anything before or after that outer fence. Inside the fence, write normal Markdown and raw LaTeX source using `$...$` and `$$...$$`.

Do not use additional triple-backtick fences inside your answer. This rule is required because ChatGPT web Copy response can corrupt rendered display math, turning `=` into `====` and minus/fraction bars into long dashed lines.

## Active Agents For This Run

Only these agents are active in this test:

- `gpt_pro_thinking` (GPT Pro Thinking): broad strategist, proof synthesizer, and test judge
- `gemini_deep_think` (Gemini Deep Think): independent alternative strategist and obstacle finder
- `deepseek_api` (DeepSeek API): API-based algebra checker, obstruction auditor, and alternative-route stress tester

Do not mention, score, or assign tasks to inactive agents. If older state text refers to inactive agents, treat it as historical noise and reassign any still-useful mathematical check to one of the active agents.

## Protocol

# Multi-AI Mathematical Research Protocol

## Round Structure

Rounds use a strict barrier synchronization rule:

- Stage B cannot begin until every agent has completed Stage A.
- Stage C cannot begin until every agent has completed Stage B.
- Stage D cannot begin until the judge synthesis is complete.
- The next round cannot begin until Stage D has been committed and pushed.

### Stage A: Independent Reasoning

Each agent receives:

- the problem statement,
- the current reading packet,
- the current lemma bank,
- the current gap register,
- the prior judge decision if available,
- the agent-specific task.

The agent must output:

```text
Summary:
Main claim or direction:
Detailed reasoning:
Dependencies:
Potential gaps:
Counterexample or obstruction search:
Useful lemmas:
What should be tested next:
Confidence:
```

### Stage B: Cross Review

Each agent reviews all other agents' Stage A outputs.

The review must output:

```text
Most valuable input from others:
Claims that look correct:
Claims that need proof:
Possible errors or hidden assumptions:
Suggested synthesis:
Score by agent:
Next-round recommendation:
```

### Stage C: Judge Synthesis

The judge reads all Stage A outputs and Stage B reviews.

The judge must output:

```text
Selected main route:
Useful fragments by source:
Rejected or risky ideas:
Known gaps:
New lemmas to add:
Counterexample checks to run:
Next round instructions:
Confidence:
```

### Stage D: State Update

The orchestrator updates:

- `state/current_state.md`: compact current research state.
- `state/lemma_bank.md`: proposed, proved, and rejected lemmas.
- `state/gap_register.md`: known gaps and possible failure points.
- `state/best_proof_draft.md`: best current proof skeleton.
- `manifests/reading_packet.md`: the compact packet for the next round.

## Public Repo Rule

The public GitHub repo is the permanent log. Every completed round should be committed and pushed.

Agents should normally read `manifests/reading_packet.md`, not the full repo. Full round files remain available for audit and later reconstruction.

## Human Intervention Rule

Human intervention is allowed at any time between stages or rounds.

Human input can appear in:

- `human/current_directives.md`
- `human/goals.md`
- `human/ideas.md`
- `human/references.md`
- `human/inbox/*.md`
- GitHub issues or comments that are manually copied into the files above

Human instructions override previous AI suggestions when they change the target, introduce a reference, reject a route, add a constraint, or change the success criterion.

Agents must explicitly acknowledge relevant human interventions in their next output.

## Mathematical Safety Rules

- Do not mark a claim as proved unless the proof is explicit.
- Preserve failed attempts; they help avoid repeated false starts.
- When a proof step uses an external theorem, name the theorem and state the needed hypotheses.
- Require counterexample search for any new lemma.
- Prefer small checkable lemmas over broad vague routes.
- Keep notation stable across rounds.

## Markdown Output Rule

Return clean Markdown source. For mathematics, use only:

- inline math: `$...$`
- display math:

```text
$$
...
$$
```

Do not use rendered-equation copy formats. Do not use bare bracket math like `[ ... ]`.
Avoid `\[ ... \]` and `\( ... \)` because some web copy tools drop the backslashes.

## Research-Mode Quality Rubric

This is a research-mode run, not a smoke test. Take enough time to reason carefully before answering. Prefer correctness, explicit assumptions, rigorous gap detection, and precise lemma statements over speed or brevity.

Before writing the final response, internally check your proposal against known barriers, missing hypotheses, possible counterexamples, and literature-status uncertainty. In the final answer, report the refined result rather than hidden chain-of-thought.

For reasoning stages, include: main route, precise lemmas, theorem dependencies, hidden assumptions, obstruction or counterexample checks, what would falsify the route, and confidence.

For review stages, include: valuable ideas from other agents, claims that look correct, claims needing proof, likely false or underspecified claims, missing hypotheses, and concrete synthesis recommendations.

For judge stages, include: selected route, useful fragments by source, rejected or risky ideas, exact gaps, new lemma statements, next-round tasks, and confidence.



## Problem

# Gauss Circle Problem

## Problem

Let

```text
N(R) = #{(m,n) in Z^2 : m^2 + n^2 <= R^2}.
```

The classical Gauss circle problem asks for the best possible exponent in the error term

```text
N(R) = pi R^2 + E(R).
```

The conjectural bound is

```text
E(R) = O_epsilon(R^{1/2 + epsilon})
```

for every epsilon > 0.

## Research Goal For This Repo

Use a multi-AI collaborative workflow to explore strategies, partial lemmas, obstacles, and proof sketches related to improving or understanding the Gauss circle problem error term.

The immediate goal is not to claim a solution, but to build a rigorous research log:

- identify plausible approaches,
- isolate precise lemmas,
- track gaps,
- test claims against known barriers,
- maintain a best current proof skeleton.

## Initial Directions To Consider

- Poisson summation and Bessel function expansions.
- Exponential sum bounds and exponent pairs.
- Smoothing and unsmoothing arguments.
- Lattice point discrepancy methods.
- Connections to the divisor problem.
- Lower-bound obstructions and omega results.
- Computational checks for small or structured ranges.


## Current State Bundle

--- FILE: state/current_state.md ---
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

--- FILE: state/lemma_bank.md ---
# Lemma Bank

## Proposed

No proposed lemmas yet.

## Plausibly Proved

None yet.

## Rejected Or Risky

None yet.

--- FILE: state/gap_register.md ---
# Gap Register

No gaps registered yet.

--- FILE: state/best_proof_draft.md ---
# Best Proof Draft

No proof draft yet.

--- FILE: manifests/reading_packet.md ---
# Reading Packet

Generated after round 8 in run `web-research-test`.

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

Responses, reviews, and judge synthesis are archived under `rounds/web-research-test/round_008/`.

--- FILE: rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex ---
\documentclass[11pt]{amsart}

\usepackage{xcolor}
\usepackage{amssymb,latexsym,amsmath,extarrows}
%\usepackage{showkeys}
\numberwithin{equation}{section}
%\usepackage[utf8]{inputenc}
\usepackage{url}
\usepackage{mathrsfs}
\usepackage{bbm}
%\usepackage{amssymb}
%\usepackage{hyperref}
\usepackage{amsmath}
%\usepackage{bigints}
%\usepackage{bbold}
\usepackage{mathabx}
\usepackage{graphicx}
\usepackage{pgfplots}

\def\Xint#1{\mathchoice
{\XXint\displaystyle\textstyle{#1}}%
{\XXint\textstyle\scriptstyle{#1}}%
{\XXint\scriptstyle\scriptscriptstyle{#1}}%
{\XXint\scriptscriptstyle\scriptscriptstyle{#1}}%
\!\int}
\def\XXint#1#2#3{{\setbox0=\hbox{$#1{#2#3}{\int}$ }
\vcenter{\hbox{$#2#3$ }}\kern-.6\wd0}}
\def\ddashint{\Xint=}
\def\dashint{\Xint-}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}{Corollary}[theorem]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
%\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\theoremstyle{proposition}
\newtheorem{proposition}{Proposition}[section]

\begin{document}

\title[Improvement on the Circle and Divisor Problems]
{An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem}

\author{Xiaochun Li}

\address{Xiaochun Li\\
Department of Mathematics\\
University of Illinois at Urbana-Champaign\\
Urbana, IL, 61801, USA}

\email{xcli@illinois.edu}

\author{Xuerui Yang}

\address{ Xuerui Yang\\
Department of Mathematics\\
University of Illinois at Urbana-Champaign\\
Urbana, IL, 61801, USA}

\email{xueruiy3@illinois.edu}

\date{}

\begin{abstract}
Using Bombieri-Iwaniec method, we establish an improvement on both Gauss's Circle Problem and Dirichlet's Divisor Problem. More precisely, we derive a new estimate for the first spacing problem and combine it with Huxley's results on the second spacing problem.
\end{abstract}

\maketitle

\section{Introduction}

In the realm of number theory, certain fundamental problems have persisted as intricate challenges, captivating the minds of mathematicians for generations. Two such enigmas are Gauss's Circle Problem and the Dirichlet's Divisor Problem, which seek to uncover the distribution of integral points within circles and the distribution of divisors of integers, respectively.

%These seemingly innocent inquiries delve into the depths of number theory, carrying implications that extend across various mathematical disciplines and even touching the fringes of real-world applications.

Let
\begin{equation}  \label{circle problem}
R(X)=\sum_{m^2+n^2\le X} 1-\pi X
\end{equation}
and
\begin{equation}  \label{divisor problem}
\Delta(X)=\sum_{1\le n\le X} d(n) - X\log X -(2\gamma-1)X.
\end{equation}
Here $d(\cdot)$ is the divisor function
\[
d(n)=\sum_{s\mid n} 1,
\]
and $\gamma=0.5772\dots$ is Euler's constant. Gauss's Circle Problem and the Dirichlet's Divisor Problem seek for upper bounds of the following form:
\[
R(X)\lesssim_\epsilon X^{\theta+\epsilon},
\]
and
\[
\Delta(X)\lesssim_\epsilon X^{\theta+\epsilon},
\]
with $\theta$ as small as possible.

For a detailed account of the history and background of these two problems, we refer the readers to the comprehensive survey paper by B. C. Berndt, S. Kim, and A. Zaharescu \cite{Bruce}.  For both problems, attempts on the opposite direction
were made in a series of papers \cite{Hardy1},\cite{Hardy2} and \cite{Hardy3} by G. H. Hardy, who proved that both $R(X)$ and $\Delta(X)$ are
\begin{equation}\label{Ome-1}
\Omega ((X\log X)^{\frac{1}{4}}),
\end{equation}
where $f=\Omega(g)$ means that for any constant $C>0$, $|f|\ge C |g|$ infinitely often in the limit process. Since then, no one has been able to enlarge the exponent $\frac{1}{4}$ on $X$ in  (\ref{Ome-1}).  That naturally gives rise to the following conjecture:
\begin{conjecture}   \label{conj-1}
In Gauss's Circle Problem and Dirichlet's Divisor Problem,
\[
\theta=\frac{1}{4}.
\]
\end{conjecture}
More recently, the pursuit of these two famous problems has been invigorated by the Bombieri-Iwaniec method, which was initiated in \cite{BombieriIwaniec} to study the pointwise bound on $|\zeta(\frac{1}{2}+it)|$, where $\zeta(s)$ is the Riemann zeta function. Then it was adapted by H. Iwaniec and C. J. Mozzochi \cite{IwaniecMozzochi} to study Gauss's Circle Problem and Dirichlet's Divisor Problem.
Later on, M. N. Huxley refined and generalized the method in a series of papers \cite{HuxleyZeta1},\cite{HuxleyZeta4},\cite{HuxleyZeta5},\cite{HuxleyCircle1},\cite{Huxley03} and \cite{HuxleyRC}, addressing the pointwise estimate of $|\zeta(\frac{1}{2}+it)|$ and the Circle and Divisor Problems. Before our work, the best-known upper bound for $\theta$ was established by Huxley \cite{Huxley03} at $\theta=\frac{131}{416}\approx 0.3149\dots$.
%It seems that Bombieri-Iwaniec method is unable to surpass the threshold at $\theta=\frac{5}{16}=0.3125$.
The current record for an upper bound on $|\zeta(\frac{1}{2}+it)|$ was established by J. Bourgain \cite{BourgainZeta}, who proved that
\[
\Big|\zeta(\frac{1}{2}+it)\Big|\lesssim_\epsilon |t|^{\frac{13}{84}+\epsilon}.
\]
As a novel observation in \cite{BourgainZeta}, it was shown that the decoupling theory can be used to handle certain mean values of
exponential sums arising in the pointwise estimates of the zeta function.
Using this insight, Bourgain and N. Watt in \cite{BourgainWatt1st} were able to improve bounds for the mean square of $\big|\zeta(\frac{1}{2}+it)\big|$ on short intervals. \\

Combining those aforementioned methods, in this paper, we are able to strengthen Huxley's result as follows.

\begin{theorem}  \label{theorem in introduction}
\[
R(X)=O_\epsilon (X^{\theta^*+\epsilon}) \quad \text{ and} \quad \Delta(X)= O_\epsilon (X^{\theta^*+\epsilon})
\]
for all $\epsilon>0$, where
\[
\theta^*= 0.314483\cdots
\]
is defined below.
\begin{definition}  \label{theta}
$\theta^*= 0.3144831759741\cdots$ is defined in such a way that $-\theta^*$ is unique solution to the equation
\begin{equation}  \label{definition of theta}
-\frac{8}{25}x-\frac{1}{200}\Big(\sqrt{2(1-14x)}-5\sqrt{-1-8x}\Big)^2+\frac{51}{200}=-x
\end{equation}
on the interval $[-0.35,-0.3]$.

\begin{tikzpicture}
\begin{axis}[
    xlabel=$x$,
    ylabel=$y$,
    width=\textwidth, % Increased width by 150%
    xmin=-0.38, xmax=-0.3, % Narrowed down x range
    ymin=0.25, ymax=0.4, % Narrowed down y range
    axis lines=middle,
    grid=both,
    minor tick num=1,
    mark size=3pt,
    domain=-0.38:-0.3, % Narrowed down x range
    samples=100,
    legend style={at={(0.05,0.95)},anchor=north west},
]
\addplot[blue,smooth] {-x};
\addplot[red,smooth] {-(8/25)*x - (1/200)*((sqrt(2*(1-14*x))-5*sqrt(-1-8*x))^2) + (51/200)};

\coordinate (intersection) at (-0.35, 0.35);
\draw[fill=black] (intersection) circle (2pt) node[above right] {Intersection};

\node[blue] at (axis cs: -0.36, 0.375) {$g(x)=-x$};
\node[red] at (axis cs: -0.34, 0.295) {$f(x)=-\frac{8}{25}x-\frac{1}{200}\Big(\sqrt{2(1-14x)}-5\sqrt{-1-8x}\Big)^2+\frac{51}{200}$};

\end{axis}
\end{tikzpicture}
\end{definition}
\end{theorem}
%Let us elaborate more on the Bombieri-Iwaniec method, otherwise known as the discrete Hardy-Littlewood Circle method.

Let us outline some of ideas used in our proof.  Starting with the Bombieri-Iwaniec method, we dissect a long exponential sum $S$
such as
\begin{equation}\label{zeta1}%\tag{$|\zeta(\frac{1}{2}+it)|$ bound}
\sum_{m\sim M} e(T\log m) \,,\quad \quad \text{where } M\ll T,
\end{equation}
and
\begin{equation} \label{c-d}%\tag{Circle Problem and Divisor Problem}
\sum_{h\sim H}\sum_{m\sim M} e\Big(\frac{Th}{m} \Big) \,,\quad \text{where }  H\ll M\ll T,
\end{equation}
into an addition of short sums $\sum_j S_j$. A sum of the form (\ref{zeta1}) arises in the study of
$\Big|\zeta(\frac{1}{2}+it)\Big|$, and (\ref{c-d}) is the typical exponential sum encountered in both the Circle and Divisor Problems.
For each short sum $S_j$, a Taylor expansion is employed to replace intractable phase functions, like $\log m$ and $\frac{T}{m}$,
by cubic or quadratic polynomials in $m$. In other words, each short exponential sum can be transformed into a  standard Weyl sum, in which the coefficients are very close to
nice rational numbers via a use of the Dirichlet approximation theorem, a standard step in Hardy-Littlewood's circle method.
%Direct application of the Weyl sum bound at this stage will cost us the connections between different $S_j$.
For each short Weyl sum, we apply the Poisson summation formula, where the power of the Fourier transform is taken into account. Because of the rational approximations of the coefficients, the Poisson summation can be carried out in a neater way, and the phase functions in the consequent exponential sum will be more structured.  In Gauss's Circle Problem and Dirichlet's Divisor Problem,
usually only the linear term coefficient is approximated by a rational number, so that the way to decompose $S$ into short sums $S_j$'s is uniquely determined by the rational approximation.  Those short sums $S_j$'s can be classified
according to the size of the denominator $r$ of the rational approximation $a/r$ to the linear coefficient, corresponding to
major arcs and minor arcs in the Hardy-Littlewood circle method. The Poisson summation and the rational approximation lead our problem to the following exponential sum
\begin{equation}\label{inner}
\sum_{\frac{a}{r}} \Big| \sum_{(k,l)} e\Big(\Vec{x}_{\frac{a}{r}}\cdot \Vec{y}_{(k,l)}\Big) \Big|,
\end{equation}
where $\Vec{x}_{\frac{a}{r}}$ is a vector with entries related to the rational number $\frac{a}{r}$ from the minor arcs, and
\[
\Vec{y}_{(k,l)}=\Big(l,kl,l\sqrt{k},\frac{l}{\sqrt{k}}\Big).
\]
To handle (\ref{inner}), the standard way is to apply the double large sieve inequality as Bombieri and Iwaniec did.
After that, we run into Huxley-type first and second spacing problems. The first spacing problem involves estimating on the mean value of exponential sums associated to the vector $\Big(l,kl,l\sqrt{k},\frac{l}{\sqrt{k}}\Big)$.  When the exponent is an even integer, the first spacing problem is equivalent to counting solutions of a certain Diophantine system. However, it was observed by Bourgain  that it is indeed a decoupling problem, deeply connected with modern Fourier analysis.
This gives a new perspective to the first spacing problem.
The second spacing problem, roughly speaking,  is related to the distribution of integer points near a $C^3$-curve. Huxley gave some nice estimations on it (see \cite{Huxley03}).   \\

Our endeavor to the first spacing problem is fueled by the recent advancements in the field of Decoupling Theory, particularly the progress on small cap decoupling for the cone made by Guth and Maldague \cite{GuthMaldague}. This will be illustrated in Section \ref{first spacing problem}. Combining our efforts in the first spacing problem with Huxley's second spacing estimates  in \cite{Huxley1996}, \cite{Huxley03}, we can achieve an improvement. This will be the subject of Section \ref{bounds on exponential sum}. In Section \ref{final argument}, we establish Theorem \ref{theorem in introduction} using results from previous sections.\\

%Without doing any improvement on Huxley's second spacing estimation,
It seems that $\theta=\frac{5}{16}=0.3125$ is an unbeatable barrier of the existing methods.
%We are working on developing some new method to yield a new estimate on certain new second spacing problem.
It will be exciting if the obstacle $\theta=0.3125$ can be overcome.  Conjecture \ref{conj-1} is extremely challenging. Although it is effective to provide non-trivial decay estimates, the Bombieri-Iwaniec method creates an issue in the beginning when the long exponential sum is broken into short sums. The orthogonality between those short sums is retrieved partially through the large sieve method. However, we do not understand how to quantitatively capture the complete cancellation from those short sums. This makes it impossible to reach $\theta=1/4$  as conjectured.  Some new ideas must be needed if one wants to resolve the conjecture. \\

{\bf Acknowledgement} The authors thank Bruce C. Berndt for a careful reading of an earlier version of this paper and for some helpful suggestions that have increased readability of the paper.

The first author is supported by a Simons fellowship 2019-2020 and Simons collaboration grants.

\section{Notations} \label{notations}

$A\lesssim B$ (or $A=O(B)$) means $A \le C B$,  where $C$ is some positive constant, and $A\lesssim_\epsilon B$ (or $A=O_\epsilon(B)$) indicates that the implicit constant may depend on the subscript $\epsilon$.

$A\sim B$ denotes that we have both $A\lesssim B$ and $B\lesssim A$.

$A\asymp B$ represents that we have $B\le A\le 2B$.

In this paper, $\ll,\gg$ are not Vinogradov's notation.  Instead, $A\ll B$ (or $A\gg B$) suggests that $A$ is much smaller (or larger) than $B$.

$\|x\|$ is the distance between $x$ and the nearest integer to $x$.

For $e(x):=e^{2\pi i x}$, the Fourier transform and the inverse Fourier transform are defined as
\[
\begin{split}
\widehat{f}(\xi)& =\int f(x)e(-x\xi) dx,
\\ \widecheck {g}(x) &= \int g(\xi) e(x\xi) d\xi.
\end{split}
\]

$\frac{a}{r}$ is always assumed to be a reduced fraction in this paper.

Lastly, $\text{diam}(a_1,a_2,\dots, a_k)\le C$ indicates that $|a_i-a_j|\le C$ for any pair $(i,j)$, where $1\le i, j\le k$.

\section{Improvement on the first spacing problem} \label{first spacing problem}

\subsection{The first spacing problem} Bourgain and Watt first noticed that the double large sieve inequality can be derived using Holder's inequality (\cite{BourgainWatt1st} Section 5). In this way, there is a freedom to choose the exponent of the norm in the first spacing problem. We follow this observation and work with $q$ a little bit larger than $4$. More specifically, the first spacing problem is asking for a nice upper bound for the following norm:
\begin{equation} \label{original form}
G_q=\Big\|\sum_{k\sim K}\sum_{l\sim L} a_{kl}e(lx_1+klx_2+l\sqrt{k}x_3)\Big\|_{L^q_{\#}\Big[|x_1|\le 1,|x_2|\le 1,|x_3|\le \frac{1}{\eta L\sqrt{K}}\Big]},
\end{equation}
where $a_{kl}$ are arbitrary coefficients such that $|a_{kl}|\le 1$, $q\ge 4$, and the subscript $\#$ denotes the averaged norm:
\[
\|f\|_{L^p_{\#}(B)}=\bigg(\frac{1}{|B|}\int_{B}|f|^p\bigg)^{\frac{1}{p}}.
\]
In \eqref{original form}, the parameters $K,L$ are integers, $\eta>0$, and they satisfy
\begin{equation}  \label{relations between L,K,eta}
1\le L<K\le \frac{1}{\eta}\le KL.
\end{equation}
Throughout this paper, we only consider $q$ with the following constraints,
\begin{equation}   \label{range of q}
 4\le q\le 4.5.
\end{equation}

\quad

Analogous to the interpretation of the norm in Vinogradov's Mean Value Theorem, if we set $a_{kl}=1$ for all $k,l$ in \eqref{original form}, and let $q=2n$ be an even positive integer, then $G^q_q$ is equal to the number of integer solutions of the following system:

\begin{align}
l_1+\dots +l_n &=l_{n+1}+\dots +l_{2n},     \label{condition 1}
\\  k_1l_1+\dots +k_n l_n &=k_{n+1}l_{n+1}+\dots +k_{2n} l_{2n}, \label{condition 2}
\\ l_1\sqrt{k_1} +\dots + l_n\sqrt{k_n}&=l_{n+1}\sqrt{k_{n+1}}+\dots + l_{2n}\sqrt{k_{2n}}+O(\eta L\sqrt{K}),   \label{condition 3}
\\ k_i \sim K, l_i\sim L, & \quad \forall i=1,...,2n.  \label{condition 4}
\end{align}
For an even integer $q$, if we let $a_{kl}$ vary, then $G_q$ is maximum when all $a_{kl}=1$. Thus it suffices to look at this special case.

There are many trivial solutions to the above system. If we set $k_{i+n}=k_i$ and $l_{i+n}=l_i$ for all $i=1,...,n$, the system always holds, no matter what values $k_1,\dots,k_n,l_1,\dots,l_n$ we take. So the number of solutions is $\gtrsim K^n L^n$, which implies
\begin{equation}  \label{lower bound}
G_q\gtrsim K^{\frac{1}{2}} L^{\frac{1}{2}},
\end{equation}
when $q=2n\ge 2$. Since we have normalized the measure space in \eqref{original form}, by Holder's inequality, \eqref{lower bound} should be true for all real $q\ge 2$.

\subsection{Upper bound on the first spacing problem}

When Huxley worked on the first spacing problem, he considered the case $q=4$, and he derived essentially a sharp estimate (\cite{Huxley1996} Theorem. 13.2.4):
\[
G_4 \lesssim_{\epsilon} K^\epsilon (KL)^{\frac{1}{2}}.
\]
As stated before, we assume that $q$ is a little bit larger than $4$. We then obtain the following proposition:
\begin{proposition}[Upper bound on $G_q$]  \label{main proposition statment}
For $q\ge 4$, if $\eta$ satisfies
\begin{equation}  \label{main proposition assumption}
\Big(\frac{L}{K}\Big)^{\frac{q-2}{q-4}}\le \eta,
\end{equation}
then
\begin{equation}    \label{main proposition}
G_q \lesssim_\epsilon \eta^{-\epsilon} \eta^{\frac{q-4}{q(q-2)}} (KL)^{1-\frac{2}{q}}\Big(1+\eta^{\frac{2}{q-2}}K\Big)^{\frac{1}{q}}.
\end{equation}
\end{proposition}
\begin{remark}
1) In this proposition, the upper bound on $G_q$ is uniform for all choices of $a_{kl}$, as long as we assume that $|a_{kl}|\le 1$.

2) We note that \eqref{main proposition assumption} is satisfied when $q$ is sufficiently close to $4$, since $\frac{L}{K}< 1$.

3) In our ultimate application of this proposition in Section \ref{final argument}, the parameters satisfy
\[
\eta^{\frac{2}{q-2}}K \lesssim 1,
\]
which implies that the last term in \eqref{main proposition} is $1$. This is convenient for computation.
\end{remark}

\subsection{Proof of Proposition \ref{main proposition statment}}

To prove the proposition, we use the small cap decoupling theorem for a truncated cone proved by Guth and Maldague \cite{GuthMaldague}. Before stating and applying their theorem, we perform some transformations on \eqref{original form}. In this way, the exponential sum can be viewed as the inverse Fourier transform of some Schwartz function defined on a neighborhood of the truncated cone, which fits in the setting of the decoupling theorem.  \\

Let us  start with some definitions.
\begin{definition}[The truncated cone and its neighborhood]  \label{truncated cone}
Let
\begin{equation}   \label{cone definition}
\mathcal{C}=\{(\xi_1,\xi_2,\xi_3):\xi_1^2+\xi_2^2=\xi_3^2, \quad \xi_3\sim 1\}
\end{equation}
be the truncated cone, and let $\mathcal{N}_\eta(\mathcal{C})$ be a $\eta$-neighborhood of $\mathcal{C}$ in $\mathbb R^3$.
\end{definition}

We introduce a notation to denote rectangular box centered at the origin.

\begin{definition} \label{box centered at origin} Define
\[
B(A_1,A_2,A_3) :=\{(x_1,x_2,x_3)\in \mathbb R^3: |x_1|\le A_1,|x_2|\le A_2, |x_3|\le A_3\},
\]
where $A_1, A_2, A_3>0$.
\end{definition}

By the definition of $G_q$ \eqref{original form} and  periodicity in the first variable, we can extend the range of the variable $x_1$ and then write $G_q$ as
\begin{equation}  \label{first by periodicity}
G_q=\Big\|\sum_{k\sim K}\sum_{l\sim L} a_{kl}e(lx_1+klx_2+l\sqrt{k}x_3)\Big\|_{L^q_{\#}\Big(B(K,1,\frac{1}{\eta L\sqrt{K}})\Big)}.
\end{equation}
Then we normalize the variables $k,l$ by rescaling of variables $x_1,x_2,x_3$ in  (\ref{first by periodicity}) so that
\begin{equation}  \label{variance 1}
G_q=\Big\|\sum_{k\sim K}\sum_{l\sim L} a_{kl} e\Big(\frac{l}{L}x_1+\frac{kl}{KL}x_2+\frac{l\sqrt{k}}{L\sqrt{K}}x_3 \Big)\Big\|_{L^q_{\#}\Big(B(KL,KL,\frac{1}{\eta})\Big)}.
\end{equation}

\quad

It will be convenient to make a change of variable. Hence we let
\[
s=\frac{l}{L}\sim 1, \quad t=\frac{k}{K}\sim 1.
\]
Then
\[\Big(\frac{l}{L},\frac{lk}{LK},\frac{l\sqrt{k}}{L\sqrt{L}}\Big)=(s,st,s\sqrt{t})\,.\]
Performing the following affine transformation,
\begin{equation}\label{trans}
\xi_1=s\sqrt{t}, \quad \xi_2=\frac{t-1}{2}s,\quad \xi_3=\frac{t+1}{2}s\,,
\end{equation}
we see that  $(\xi_1, \xi_2, \xi_3)$ lies on the cone $\mathcal{C}$ \eqref{cone definition}, because
\begin{equation}   \label{reason for lying on the cone}
\Big(\frac{st+s}{2}\Big)^2 -\Big(\frac{st-s}{2}\Big)^2=s^2 t=(s\sqrt{t})^2.
\end{equation}

Replacing $s$ by $l/L$ and $t$ by $k/K$,  we know that the relations between $(k,l)$ and $\Vec{\xi}$ are given by
\begin{equation}  \label{change of variables 1}
\left\{\begin{array}{rcl}
\xi_1 &= & \frac{l}{L}\frac{\sqrt{k}}{\sqrt{K}} \,\,\,\, \sim 1,
\\ \xi_2 &= &\frac{l}{L} \frac{k/K-1}{2},
\\ \xi_3 &= & \frac{l}{L} \frac{k/K+1}{2}  \sim 1.
\end{array}\right.
\end{equation}

Define
\[
\Gamma=\big\{\Vec{\xi}: \Vec{\xi} \text{ is given by } \eqref{change of variables 1} \text{ for some }(k,l) \text{ s.t. }k\sim K, l\sim L \big\}.
\]
We note that the vectors $\Vec{\xi}\in \Gamma$ are $\frac{1}{K}$-separated in the circular direction and $\frac{1}{L}$-separated in the null direction. Also, it is easy to see that the map \eqref{change of variables 1} is bijective from $\{(k,l):k\sim K, l\sim L\}$ to $\Gamma$, so $a_{\Vec{\xi}}=a_{kl}$ can be defined correspondingly.\\

By \eqref{change of variables 1}, \eqref{variance 1} becomes
\[
\begin{split}
&\Big \|\sum_{\Vec{\xi}\in \Gamma}a_{\Vec{\xi}}\, e\Big((\xi_3-\xi_2)x_1+(\xi_3+\xi_2)x_2+\xi_1x_3\Big)\Big\|_{L^q_{\#}\Big(B(KL,KL,\frac{1}{\eta})\Big)}
\\ =& \Big\|\sum_{\Vec{\xi}\in \Gamma}a_{\Vec{\xi}} \,e\Big(\xi_1 x_3 +\xi_2(x_2-x_1)+\xi_3(x_1+x_2)\Big)\Big\|_{L^q_{\#}\Big(B(KL,KL,\frac{1}{\eta})\Big)}.
\end{split}
\]
Performing another change of variables, say,
\begin{equation}    \label{change of variables 2}
\left\{\begin{array}{rcl}
y_1 &=& x_3
\\ y_2 &= & x_2-x_1
\\ y_3 &=&  x_2+x_1\,,
\end{array}    \right.
\end{equation}
we find that
\begin{equation} \label{variance 2} G_q =\Big\|\sum_{\Vec{\xi}\in \Gamma}a_{\Vec{\xi}}\,e\Big(\xi_1 y_1+\xi_2 y_2+\sqrt{\xi_1^2+\xi_2^2}y_3\Big)\Big\|_{L^q_{\#}\Big( B(\frac{1}{\eta},KL,KL) \Big)}.
\end{equation}
%To conclude,
%\begin{equation}   \label{variance 2}
%G_q=\Big\|\sum_{\Vec{\xi}\in \Gamma}a_{\Vec{\xi}}\,e\Big(\xi_1 x_1+\xi_2 x_2+\sqrt{\xi_1^2+\xi_2^2}x_3\Big)\Big\|_{L^q_{\#}\Big(\frac{1}{\eta},KL,KL\Big)},
%\end{equation}
%and our changes of variables in $\Vec{x}$ from \eqref{original form} to \eqref{variance 2} are
%\begin{equation}    \label{change of variables 2}
%\left\{\begin{array}{rcl}
%x^{\text{new}}_1 &=&L\sqrt{K} x_3
%\\ x^{\text{new}}_2 &= &KL(x_2-x_1)
%\\ x^{\text{new}}_3 &=& KL(x_2+x_1).
%\end{array}    \right.
%\end{equation}
Now we are able to view the exponential sum in \eqref{variance 2} as a function whose Fourier transform is supported on $\mathcal N_\eta(\mathcal C)$, a $\eta$-neighborhood of the cone $\mathcal C$, since $\eta\ge \frac{1}{KL}$.  To see why this is true, we let $\psi$ be a smooth bump function supported in a neighborhood of $[-1,1]$ and taking the value $1$ on $[-1,1]$, and define
\[
\begin{split}
F(z_1,z_2,z_3)  = \frac{K^2L^2}{\eta} \sum_{\Vec{\xi}\in \Gamma}  a_{\Vec{\xi}} \,  \widehat{\psi}\Big(\frac{z_1-\xi_1}{\eta}\Big) \widehat{\psi}\Big(\frac{z_2-\xi_2}{\frac{1}{KL}} \Big)  \widehat{\psi}\Big(\frac{z_3-\sqrt{\xi_1^2+\xi_2^2}}{\frac{1}{KL}}\Big).
\end{split}
\]
Then its inverse Fourier transform is
\[
%\begin{split}
\widecheck{F}(y_1\!,y_2,\!y_3)\!= \!\!\sum_{\Vec{\xi}\in \Gamma}\!a_{\Vec{\xi}}\,e\Big(\!\xi_1 y_1\!+\xi_2 y_2\!+\sqrt{\xi_1^2+\xi_2^2}y_3\!\Big) \psi \Big( \frac{y_1}{\frac{1}{\eta}}\Big) \psi \Big(\frac{y_2}{KL}\Big) \psi\Big(\frac{y_3}{KL}\Big),
%\end{split}
\]
which is the sum on the right side of  \eqref{variance 2} with a Schwartz tail. From now on, by an abuse of notation, we change the dummy variables $(y_1,y_2,y_3)$ to $(x_1,x_2,x_3)$. \\

At this step, we can apply a small cap decoupling theorem of Guth and Maldague to \eqref{variance 2}. Before stating their result, we introduce some concepts first. A generic plate $\sigma$ of dimensions $\eta^{\beta_2}\times \eta^{\beta_1}\times \eta$ is a rectangular box in a $\eta$-neighborhood  of $\mathcal C$ such that $\eta^{\beta_2}$ is the length in the null direction, $\eta^{\beta_1}$ is the length in the circular direction, and $\eta$ is the thickness of the plate. $\mathcal N_\eta(\mathcal C)$ can be covered by essentially pairwise disjoint generic plates $\sigma$ of dimensions $\eta^{\beta_2}\times \eta^{\beta_1}\times \eta$,
where $\beta_2\in[0,1]$, $\beta_1\in [\frac{1}{2},1]$.  By the essential disjointness, we mean that those plates may have finite overlaps but can be divided into finitely many sets, each of which contains disjoint plates. Thus we can view the collection
of those essentially disjoint generic plates as a partition of $\mathcal N_\eta(\mathcal C)$. Given a Schwartz function $f$, we define $f_\sigma$ by setting its Fourier transform
\[
\widehat{f_\sigma}=\widehat{f} \cdot \chi_\sigma,
\]
where $\chi_\sigma$ is the characteristic function of $\sigma$. We now are ready to state Guth and Maldague's theorem.

\begin{theorem}[\cite{GuthMaldague}, Thm 3]\label{small cap decoupling}
Let $\beta_1\in [\frac{1}{2},1]$ and $\beta_2\in[0,1]$. For $q\ge 2$ and any Schwartz function $f:\mathbb R^3\to \mathbb C$ with Fourier transform supported in $\mathcal{N}_\eta(\mathcal{C})$, we have
\begin{equation}\label{sm-cap}
\int_{\mathbb R^3} |f|^q \lesssim_\epsilon \eta^{-\epsilon}  D^q_{\beta_1, \beta_2, q}   \sum_{\sigma} \|f_\sigma\|_{L^q(\mathbb R^3)}^q \,,
\end{equation}
where the decoupling constant $D_{\beta_1, \beta_2, q}$ is given by
\[
D_{\beta_1,\beta_2,q}=\eta^{-(\beta_1+\beta_2)(\frac{1}{2}-\frac{1}{q})}+\eta^{-(\beta_1+\beta_2)(1-\frac{2}{q})+\frac{1}{q}}+\eta^{-(\beta_1+\beta_2-\frac{1}{2})(1-\frac{2}{q})}   \,.
\]
\end{theorem}

Applying Theorem \ref{small cap decoupling} to the right side of  \eqref{variance 2}, we get the following lemma immediately.

\begin{lemma}
Let $\beta_1\in [\frac{1}{2},1]$ and $\beta_2\in[0,1]$. For $q\ge 4$,
\begin{equation}  \label{application of small cap decoupling}
G_q \lesssim_\epsilon \eta^{-\epsilon} D_{\beta_1,\beta_2,q}\Big(\sum_{\sigma}\Big\|\sum_{\Vec{\xi}\in \sigma} F_{\Vec{\xi}} \,(x_1,x_2,x_3)\Big\|^q_{L^q_{\#}\Big(B(\frac{1}{\eta},KL,KL)\Big)}\Big)^\frac{1}{q},
\end{equation}
where
\[
F_{\Vec{\xi}}\,(x_1,x_2,x_3)=a_{\Vec{\xi}}\,e\Big(\xi_1 x_1+\xi_2 x_2+\sqrt{\xi_1^2+\xi_2^2}x_3\Big).
\]
We note that $\Vec{\xi}\in \sigma$ in the right side of (\ref{application of small cap decoupling}) can be replaced by
 $\Vec{\xi}\in (\Gamma\cap \sigma)$ because only  those $ \Vec{\xi}\in\Gamma$ makes contributions.
\end{lemma}

We can simplify the decoupling constant $D_{\beta_1, \beta_2, q}$ when $q\geq 4$. In fact, notice that for $q\ge 4$,
\[
-(\beta_1+\beta_2)(1-\frac{2}{q})+\frac{1}{q}-[-(\beta_1+\beta_2-\frac{1}{2})(1-\frac{2}{q})]
%\\ = &\frac{1}{q}-\frac{1}{2}(1-\frac{2}{q})
= -\frac{1}{2}+\frac{2}{q}
\le 0,
\]
which implies
\[
\eta^{-(\beta_1+\beta_2)(1-\frac{2}{q})+\frac{1}{q}}\ge \eta^{-(\beta_1+\beta_2-\frac{1}{2})(1-\frac{2}{q})},
\]
because $0<\eta<1$. Thus for $q\ge 4$, up to a constant multiple,
\begin{equation}  \label{decoupling constant}
D_{\beta_1,\beta_2,q}=\eta^{-(\beta_1+\beta_2)(\frac{1}{2}-\frac{1}{q})}+\eta^{-(\beta_1+\beta_2)(1-\frac{2}{q})+\frac{1}{q}}.
\end{equation}

From (\ref{change of variables 1}), we see that each pair $(k, l)$ corresponds to a vector $\Vec{\xi}=\vec{\xi}(k, l)=
(\xi_1(l,k), \xi_2(l,k), \xi_3(l,k))$
such that $\xi_1(l,k)=\frac{l\sqrt{k}}{L\sqrt{K}} $, $ \xi_2(l,k)=\frac{l}{L} \frac{k/K-1}{2} $ and $\xi_3(l,k)=
 \frac{l}{L} \frac{k/K+1}{2}$.  Define
\begin{equation}
{\mathcal R}_\sigma := \bigg\{(k, l)\in\mathbb Z^2: k\sim K, l\sim L,  \vec{\xi}(k, l)\in\sigma\bigg\}\,.
\end{equation}

\begin{lemma}  \label{R-sigma}
 ${\mathcal R}_\sigma$ is contained a rectangle
\[
I_\sigma \times J_\sigma \subset \{(k,l)\in \mathbb Z^2: k\sim K,l\sim L\}
\]
of dimensions (up to constant multiples)
\[
(1+\eta^{\beta_2}K) \times (1+\eta^{\beta_1}L).
\]
\end{lemma}
\begin{proof} By \eqref{change of variables 1}, a variation of the vector $\Vec{\xi}=(\xi_1,\xi_2,\sqrt{\xi_1^2+\xi_2^2})$ in the null direction corresponds to a change in $\frac{l}{L}$. If $\Vec{\xi}$ moves in the null direction by length $\eta^{\beta_1}$, then $l$ moves by $\eta^{\beta_1}L$ units, so $l$ lies in an interval $J_\sigma$ of size $1+\eta^{\beta_1}L$.

Similarly,  if $\Vec{\xi}$ moves in the circular direction by length $\eta^{\beta_2}$, then $k$ moves by $\eta^{\beta_2}K$ units, so $k$ lies in an interval $I_\sigma$ of size $1+\eta^{\beta_2}K$.   \end{proof}

By Lemma \ref{R-sigma}, reversing the changes of variables \eqref{change of variables 1} and \eqref{change of variables 2}, we obtain
\begin{equation}   \label{change back}
\begin{split}
&\Big \|\sum_{\Vec{\xi}\in \sigma}F_{\Vec{\xi}}\,(x_1,x_2,x_3) \Big\|^q_{L^q_{\#}\Big(B(\frac{1}{\eta},KL,KL)\Big)}
\\ =&\Big\|\sum_{(k,l)\in {\mathcal R}_\sigma} a_{kl}e\Big(lx_1+klx_2+l\sqrt{k}x_3\Big)\Big\|^q_{L^q_{\#}\Big(B(1,1,\frac{1}{\eta L\sqrt{K}})\Big)}.
\end{split}
\end{equation}
Henceforth, by \eqref{application of small cap decoupling}, \eqref{decoupling constant} and \eqref{change back}, we can conclude the following lemma.
\begin{lemma}   \label{after small cap decoupling}
Let $\beta_1\in [\frac{1}{2},1]$ and $\beta_2\in[0,1]$. For $q\ge 4$,
\begin{equation}  \label{variance 3}
G_q\lesssim_\epsilon  \eta^{-\epsilon} \Big[\eta^{-(\beta_1+\beta_2)(\frac{1}{2}-\frac{1}{q})}+\eta^{-(\beta_1+\beta_2)(1-\frac{2}{q})+\frac{1}{q}}\Big] \cdot E_q(\beta_1,\beta_2),
\end{equation}
where
\begin{equation}  \label{definition of Eq}
E_q(\beta_1,\beta_2):=\Big(\sum_{\sigma}\Big\|\sum_{(k,l)\in \mathcal R_\sigma} a_{kl}e\Big(lx_1+klx_2+l\sqrt{k}x_3\Big)\Big\|^q_{L^q_{\#}\Big(B(1,1,\frac{1}{\eta L\sqrt{K}})\Big)}\Big)^{\frac{1}{q}}.
\end{equation}
\end{lemma}

In applications of Lemma \ref{after small cap decoupling}, we need to check that our choices of parameters $\beta_1,\beta_2$ are valid. Most importantly, we need to verify that
\begin{equation}   \label{beta1 da yu 1/2}
 \beta_1 \ge \frac{1}{2}.
\end{equation}
Moreover, we have to choose the parameters $\beta_1$ and $\beta_2$ to obey the following constraints,
\begin{equation}  \label{conditions on beta1,2}
\eta^{\beta_1}K\ge 1, \quad  \eta^{\beta_2}L\ge 1.
\end{equation}
Otherwise the intervals $I_\sigma,J_\sigma$ are of length $1$,  %$E_q(\beta_1,\beta_2)$ does not change,
and the decoupling constant $D_{\beta_1,\beta_2,q}$ gets bigger, which makes the right hand side of \eqref{variance 3} a worse upper bound. From now on, we assume \eqref{conditions on beta1,2} to be true. Of course, we need to check its validity after we make the choices of the parameters $\beta_1,\beta_2$.

With Lemma \ref{after small cap decoupling} in hand,  it remains to  estimate $E_q(\beta_1,\beta_2)$. We first consider the case when $q$ is an even integer $2n$ with $n\geq 2$. In this case,   because of Lemma \ref{R-sigma} and the fact that the $\mathcal R_\sigma$'s are disjoint, $E_q(\beta_1,\beta_2)^q$ is controlled by  the number of solutions of the following system, called System $(*)$,  containing the following equations and conditions
from (\ref{condition 1'}) to (\ref{condition 6'}).
\begin{align}
l_1+\dots +l_n &=l_{n+1}+\dots +l_{2n},     \label{condition 1'}
\\  k_1l_1+\dots +k_n l_n &=k_{n+1}l_{n+1}+\dots +k_{2n} l_{2n}, \label{condition 2'}
\\ l_1\sqrt{k_1} +\dots + l_n\sqrt{k_n}&=l_{n+1}\sqrt{k_{n+1}}+\dots + l_{2n}\sqrt{k_{2n}}+O(\eta L\sqrt{K}),   \label{condition 3'}
\\ k_i \sim K, l_i\sim L, & \quad \forall i=1,...,2n,   \label{condition 4'}
\\ \text{diam}(k_1,\cdots,k_{2n})&\lesssim \eta^{\beta_1}K ,  \label{condition 5'}
\\ \text{diam}(l_1,\cdots,l_{2n})&\lesssim \eta^{\beta_2}L . \label{condition 6'}
\end{align}
Here the notation $\text{diam}(a_1,\dots,a_k)$ was introduced in Section \ref{notations}.  \\

%In the above system, we replace the condition $(k_i,l_i)\in \mathcal R_\sigma$ by $(k_i,l_i)\in I_\sigma \times J_\sigma$. %Since it adds to the possible choices of $(k,l)$, this modification does not reverse the direction of our desired inequality.

Comparing with the system restricted by \eqref{condition 1}-\eqref{condition 4}, we simply add two more conditions \eqref{condition 5'}, \eqref{condition 6'} in System $(*)$. We call them ``localization conditions", since they localize the variables $k_i,l_i$. \\

For $q=4$, we have the following useful lemma.
\begin{lemma}  \label{Lemma number of solutions q=4}
\begin{equation} \label{number of solutions q=4}
E_4(\beta_1,\beta_2) \lesssim_\epsilon K^{\frac{1}{4}+\epsilon}L^{\frac{1}{4}} \Big( \eta^{2(\beta_1+\beta_2)}K^2 L+\eta^{2\beta_1}K^2+\eta^{2\beta_2}L^2 \Big)^{\frac{1}{4}}.
\end{equation}
\end{lemma}
Before we start the proof, we show that Lemma \ref{Lemma number of solutions q=4}, in combination with Lemma \ref{after small cap decoupling}, gives us an essentially sharp bound on $G_4$, namely, the following corollary.
\begin{corollary} \label{G_4}
\[
G_4 \lesssim_\epsilon K^{\frac{1}{2}+\epsilon}L^{\frac{1}{2}}.
\]
\end{corollary}
\begin{proof}[Proof of Corollary \ref{G_4}]
We insert \eqref{number of solutions q=4} into the bound on $G_4$ \eqref{variance 3}, and let $\beta_1+\beta_2=1$. Then
\begin{equation}  \label{G4 bound}
G_4\lesssim_\epsilon K^\epsilon\Big[ \eta^{\frac{1}{4}}K^{\frac{3}{4}}L^{\frac{1}{2}}+\eta^{-\frac{1}{4}}  K^{\frac{1}{4}+}L^{\frac{1}{4}}(\eta^{\beta_1}K+\eta^{\beta_2}L)^{\frac{1}{2}} \Big].
\end{equation}
We choose $\beta_1,\beta_2$ by setting
\begin{equation}  \label{definition of betas in q=4}
\eta^{\beta_1}K=\eta^{\beta_2}L.
\end{equation}
The equation \eqref{definition of betas in q=4} determines $\beta_1,\beta_2$, since we also have $\beta_1+\beta_2=1$. We can solve these two equations to get
\begin{equation} \label{solution of beta1}
\eta^{\beta_1}=\eta^{\frac{1}{2}} \Big(\frac{L}{K}\Big)^{\frac{1}{2}}.
\end{equation}
We recall from \eqref{relations between L,K,eta} that
\[
L\le K, 0<\eta<1.
\]
Hence we can conclude from \eqref{solution of beta1} that
\[
\beta_1 \ge \frac{1}{2}.
\]
In addition,  it follows from \eqref{solution of beta1} that
\begin{equation}  \label{check of parameters in q=4}
\eta^{\beta_1}K=\eta^{\beta_2}L= (\eta KL)^\frac{1}{2}\ge 1,
\end{equation}
which is what we expect in \eqref{conditions on beta1,2}.
Finally, we insert \eqref{check of parameters in q=4} back into \eqref{G4 bound} and get
\[
G_4\lesssim_\epsilon K^\epsilon ( \eta^{\frac{1}{4}} K^{\frac{3}{4}}L^{\frac{1}{2}}+K^{\frac{1}{2}}L^{\frac{1}{2}}) \lesssim K^{\frac{1}{2}+\epsilon}L^{\frac{1}{2}},
\]
where the last inequality follows from $\eta K\le  1$.
\end{proof}

We return to the proof of Lemma \ref{Lemma number of solutions q=4}:
\begin{proof} [Proof of Lemma \ref{Lemma number of solutions q=4}]
We follow Bourgain and Watt's idea in \cite[Proposition 7]{BourgainWatt1st}. In this case, $n=\frac{q}{2}=2$, and $E_4(\beta_1,\beta_2)^4$ is bounded by the number of solutions of the System ($*$) constrained by \eqref{condition 1'} to \eqref{condition 6'}. First, we disregard the third inequality \eqref{condition 3'} and focus on the two algebraic equations \eqref{condition 1'}, \eqref{condition 2'}. This move turns out to cost us negligible loss, which shows the power of the localization conditions \eqref{condition 5'}, \eqref{condition 6'}.

The first equation \eqref{condition 1'} tells us that $l_4$ is determined once we choose $l_1,l_2,l_3$. If we set $\Delta k_i=k_i-k_4$ for $i=1,2,3$, then $|\Delta k_i|\lesssim \eta^{\beta_1}K$ by \eqref{condition 5'}, indicating that
$\Delta k_i$  varies in a relatively small range.
There are $\sim K$ many choices of the variable $k_4$. Each $k_i$ with $i=\{1,2,3\}$, is determined uniquely by $k_4$ and $\Delta k_i$. Thus it suffices to consider how many $\Delta k_1, \Delta k_2,\Delta k_3$ we can take when $k_4$ is fixed.

Subtracting $\eqref{condition 1'}\times k_4$
from $\eqref{condition 2'}$, we obtain
\begin{equation}
 l_1\Delta k_1 + l_2\Delta k_2= l_3\Delta k_3\,,
\end{equation}
which implies
\begin{equation}     \label{variance of conditions 1}
 (l_1-l_3)\Delta k_1+(l_2-l_3)\Delta k_2=l_3(\Delta k_3-\Delta k_1-\Delta k_2).
\end{equation}

The main observation we will use is that a certain nonzero integer has only a few factors, namely,
\[
d(v)\lesssim_\epsilon v^\epsilon \quad \text{ for all } v\ge 1,
\]
where $\epsilon>0$ is any small number. If we can set up an equation about integers, and both sides are nonzero, then the number of divisors of one side can not exceed the number of divisors of the other side. For example, in \eqref{variance of conditions 1}, if both sides are nonzero and the left hand side is given, then we do not have many choices of $l_3$ and $\Delta k_3-\Delta k_1-\Delta k_2$. This simple observation will be used repeatedly in the following proof, and it is also useful for dealing with $E_{2n}(\beta_1,\beta_2)^{2n}$, where $n\ge 3$. \\

We examine \eqref{variance of conditions 1} and distinguish several cases: \\

\underline{Case (a)}: Both sides are not zero, which is equivalent to $\Delta k_3 \neq \Delta k_1+\Delta k_2$. For a given vector $(\Delta k_1, \Delta k_2, l_1-l_3,l_2-l_3)$, there are $O(K^\epsilon)$ many choices of  $l_3$ and $\Delta k_3$, because $K\ge L$ and
$l_3$ and $\Delta k_3-\Delta k_1-\Delta k_2$ are divisors of the given left side of (\ref{variance of conditions 1}).
Taking into account the number of ways to choose $\Delta k_1, \Delta k_2, l_1-l_3,l_2-l_3, k_4$, we conclude that in this case there are
\[
\lesssim_\epsilon K^\epsilon (\eta^{\beta_1}K)^2 (\eta^{\beta_2}L)^2 K=\eta^{2(\beta_1+\beta_2)}K^{3+\epsilon}L^2
\]
different solutions of the System ($*$). \\

\underline{Case (b)}: Both sides of \eqref{variance of conditions 1} are zero, which implies that $\Delta k_3=\Delta k_1+\Delta k_2$. Therefore, $\Delta k_3$ is determined once $\Delta k_1, \Delta k_2$ are given. In this case, \eqref{variance of conditions 1} implies that
\begin{equation}  \label{variance of conditions 2}
(l_1-l_3)\Delta k_1=(l_3-l_2)\Delta k_2,
\end{equation}
and we further consider two sub-cases as follows. \\

{\bf Sub-case} (b.i): Both sides of \eqref{variance of conditions 2} are nonzero. If $l_1$, $l_1-l_3,\Delta k_1$ are constant, then  $l_2,l_3,\Delta k_2$ are essentially determined as we did in Case a).  In this sub-case, we can select
\[
\Delta k_1,l_1-l_3, l_1, k_4,
\]
without any restriction. That leads to
\[
\lesssim_\epsilon \eta^{\beta_1+\beta_2} K^{2+\epsilon}L^2
\]
different solutions of the System ($*$). \\

{\bf Sub-case} (b.ii): Both sides of \eqref{variance of conditions 2} are zero. We consider the following three sub-sub-cases.\\

Sub-sub-case (b.ii.1): $\Delta k_1=l_3-l_2=0$ or $\Delta k_2=l_1-l_3=0$.

By symmetry, the analysis for these two scenarios is the same, and the total number of solutions is
\[
\lesssim \eta^{\beta_1+\beta_2} K^2 L^2.
\]

Sub-sub-case (b.ii.2): $\Delta k_1=\Delta k_2=0$, there are
\[
\lesssim \eta^{2\beta_2}KL^3
\]
distinct solutions.

Sub-sub-case (b.ii.3): $l_1-l_3=l_2-l_3=0$. There are
\[
\lesssim \eta^{2\beta_1}K^3 L
\]
distinct solutions.

Having taken all possible cases into consideration, we can summarize that, after simplification, there are
\[
\lesssim_\epsilon K^{1+\epsilon}L \Big( \eta^{2(\beta_1+\beta_2)}K^2 L+\eta^{2\beta_1}K^2+\eta^{2\beta_2}L^2 \Big)
\]
many solutions of the System ($*$) at $q=4$.
\end{proof}

\quad

At this stage, we have all the tools we need. To prove Proposition \ref{main proposition statment}, we still resort to Lemma \eqref{after small cap decoupling}, but unlike the case when $q=4$, we cannot reduce the estimate of a general $E_q(\beta_1,\beta_2)$ to a counting problem. However, there is a connection between $E_4(\beta_1,\beta_2)$ and $E_q(\beta_1,\beta_2)$.

\begin{lemma}   \label{lemma E4 and Eq}
If \eqref{conditions on beta1,2} holds, then for $q\ge 4$,
\begin{equation}  \label{E4 and Eq}
E_q (\beta_1,\beta_2) \lesssim (\eta^{\beta_1+\beta_2}KL)^{1-\frac{4}{q}} E_{4}(\beta_1,\beta_2)^\frac{4}{q}.
\end{equation}
\end{lemma}

\begin{proof}
By Lemma \ref{R-sigma} and \eqref{conditions on beta1,2}, for each $\sigma$,
\[
\Big\|\sum_{(k,l)\in \mathcal R_\sigma}a_{kl}e(lx_1+klx_2+l\sqrt{k}x_3)\Big\|_{L^\infty}
\le  |I_\sigma||J_\sigma| \lesssim \eta^{\beta_1+\beta_2}KL.
\]
Accordingly,
\begin{equation}   \label{q and 4}
\begin{split}
&\Big\|\sum_{(k,l)\in \mathcal R_\sigma} a_{kl}e\Big(lx_1+klx_2+l\sqrt{k}x_3\Big)\Big\|^q_{L^q_{\#}\Big(B(1,1,\frac{1}{\eta L \sqrt{K}})\Big)}
\\ \le & \Big\|\sum_{(k,l)\in \mathcal R_\sigma}a_{kl}e(lx_1+klx_2+l\sqrt{k}x_3)\Big\|_{L^\infty}^{q-4}
\\ \times & \Big\|\sum_{(k,l)\in \mathcal R_\sigma} a_{kl}e\Big(lx_1+klx_2+l\sqrt{k}x_3\Big)\Big\|^4_{L^4_{\#}\Big(B(1,1,\frac{1}{\eta L \sqrt{K}})\Big)}
\\ \lesssim & (\eta^{\beta_1+\beta_2}KL)^{q-4}
\\ \times & \Big\|\sum_{(k,l)\in \mathcal R_\sigma} a_{kl}e\Big(lx_1+klx_2+l\sqrt{k}x_3\Big)\Big\|^4_{L^4_{\#}\Big(B(1,1,\frac{1}{\eta L \sqrt{K}})\Big)}.
\end{split}
\end{equation}
Thence, by comparing the definition of $E_q(\beta_1,\beta_2)$, \eqref{definition of Eq} and \eqref{q and 4}, we find that
\begin{equation}  \label{E44 and Eqq}
E_q(\beta_1,\beta_2)^q\lesssim (\eta^{\beta_1+\beta_2}KL)^{q-4} E_4(\beta_1,\beta_2)^4.   \end{equation}
The inequality \eqref{E4 and Eq} follows by taking the $\frac{1}{q}$-th power on both sides of \eqref{E44 and Eqq}.
\end{proof}

Now comes the proof of our main Proposition.

\begin{proof}  [Proof of Proposition \ref{main proposition statment}]
We assume the validity of \eqref{conditions on beta1,2} and will verify it later. By Lemma \ref{Lemma number of solutions q=4} and Lemma \ref{lemma E4 and Eq}, $E_q(\beta_1,\beta_2)$ can be bounded as
\begin{equation}  \label{upper bound on Eq}
\begin{split}
E_q(\beta_1,\beta_2)\lesssim_\epsilon K^\epsilon &(\eta^{\beta_1+\beta_2}KL)^{1-\frac{4}{q}} (KL)^{\frac{1}{q}}
\\ \times & (\eta^{2(\beta_1+\beta_2)}K^2L +\eta^{2\beta_1}K^2+\eta^{2\beta_2}L^2)^{\frac{1}{q}}.
\end{split}
\end{equation}
We insert \eqref{upper bound on Eq} into \eqref{variance 3}, and deduce that
\begin{equation}   \label{q>4 before optimization}
\begin{split}
G_q\lesssim_\epsilon  \eta^{-\epsilon} &\Big[\eta^{-(\beta_1+\beta_2)(\frac{1}{2}-\frac{1}{q})}+\eta^{-(\beta_1+\beta_2)(1-\frac{2}{q})+\frac{1}{q}}\Big] (\eta^{\beta_1+\beta_2}KL)^{1-\frac{4}{q}}
\\  & \Big[  KL \Big(\eta^{2(\beta_1+\beta_2)}K^2L+\eta^{2\beta_1}K^2+\eta^{2\beta_2}L^2\Big)  \Big]^{\frac{1}{q}}.
\end{split}
\end{equation}
Notice that in \eqref{q>4 before optimization}, we hide $K^\epsilon$ in $\eta^{-\epsilon}$ since $\frac{1}{\eta}\ge K$. Next we choose the parameters $\beta_1,\beta_2$ in order to optimize the upper bound in \eqref{q>4 before optimization}. For simplification of notation, if we let $\beta_1+\beta_2=\beta$, \eqref{q>4 before optimization} becomes
\begin{equation}   \label{idk what to label}
\begin{split}
G_q \lesssim_\epsilon  \eta^{-\epsilon} & \Big[\eta^{-\beta(\frac{1}{2}-\frac{1}{q})}+\eta^{-\beta(1-\frac{2}{q})+\frac{1}{q}}\Big] (\eta^{\beta}KL)^{1-\frac{4}{q}}
\\ &\Big[KL(\eta^{2\beta}K^2L+\eta^{2\beta_1}K^2+\eta^{2\beta_2}L^2)\Big]^{\frac{1}{q}}.
\end{split}
\end{equation}
If we set
\begin{equation}  \label{choices of beta1 beta2 q}
\eta^{\beta_1}K=\eta^{\beta_2}L=(\eta^\beta KL)^{\frac{1}{2}},
\end{equation}
then \eqref{idk what to label} takes the form
\[
G_q \lesssim_\epsilon \eta^{-\epsilon} (KL)^{1-\frac{2}{q}} \Big[  \eta^{\beta(\frac{1}{2}-\frac{2}{q})}+ \eta^{\frac{1}{q}(1-\beta)}  \Big](1+\eta^\beta K)^{\frac{1}{q}}.
\]
Finally, if we set
\begin{equation}   \label{q>4 beta value}
\beta=\frac{2}{q-2} \le 1,
\end{equation}
we have
\[
G_q \lesssim_\epsilon \eta^{-\epsilon} \eta^{\frac{q-4}{q(q-2)}} (KL)^{1-\frac{2}{q}}(1+\eta^{\frac{2}{q-2}}K)^{\frac{1}{q}}.
\]
This is \eqref{main proposition}.

It remains to verify the conditions \eqref{beta1 da yu 1/2} and \eqref{conditions on beta1,2}. On one hand, we do not know what $q$ to choose at this step, so the values of $\beta$ and $\beta_1$ are unknown, and that is why we leave \eqref{beta1 da yu 1/2} as an assumption. By \eqref{choices of beta1 beta2 q} and the fact that $0<\eta<1$, it is easy to see that \eqref{beta1 da yu 1/2} is equivalent to the assumption \eqref{main proposition assumption} in Proposition \ref{main proposition statment}.
On the other hand, by \eqref{relations between L,K,eta},
\[
1\le \frac{1}{\eta} \le KL,
\]
and since $\beta \le 1$, we find that
\[
\eta^\beta KL \ge \eta KL \ge 1.
\]
Therefore
\[
\eta^{\beta_1}K=\eta^{\beta_2}L=(\eta^\beta KL)^{\frac{1}{2}}\ge 1,
\]
which is exactly \eqref{conditions on beta1,2}.

We have completed our proof of the main Proposition \ref{main proposition statment}.\\
\end{proof}

\section{Bounds on certain exponential sum using the Bombieri-Iwaniec Method}\label{bounds on exponential sum}

In this section, we derive an effective upper bound for a certain type of double exponential sum, which appears in the study of Gauss's Circle Problem and Dirichlet's Divisor Problem. \\

\subsection{Main theorem on bounds of the exponential sum}
Let us begin with some definitions and assumptions. Let $\epsilon>0$ and $C_1,C_2,\dots,C_5\ge 2$ be real constants. Let $F(x)$ be a real function that is three times continuously differentiable for $1\le x\le 2$, and let $g(x),G(x)$ be functions of bounded variation on the interval $[1,2]$. $M$ and $T$ denote large positive parameters and $H\ge 1$.  We set
\begin{equation}  \label{definition of S}
S :=\sum_{H\le h\le 2H} g\Big(\frac{h}{H}\Big) \sum_{M\le m\le 2M} G\Big(\frac{m}{M}\Big)e\Big(\frac{hT}{M}F\Big(\frac{m}{M}\Big)\Big),
\end{equation}
which is the standard form of the exponential sum encountered in the study of both the Circle and Divisor Problems. \\

Suppose moreover that, on the interval $[1,2]$, the derivatives $F^{(1)}(x)$, \\ $F^{(2)}(x)$,$F^{(3)}(x)$ satisfy:
\begin{equation}  \label{condition on F 1}
C_r\ge |F^{(r)}(x)|\ge C_{r}^{-1}  \quad (r=1,2,3)
\end{equation}
and
\begin{equation}  \label{condition on F 2}
|F^{(1)}(x)F^{(3)}(x)-3F^{(2)}(x)^2|\ge C_{4}^{-1},
\end{equation}
for some constant $C_4$.

We focus on the following two cases.

\begin{definition}  [Case (A)] \label{case A definition}
Let $H,M,T$ satisfy the three conditions:
\begin{equation}  \label{case A}
\begin{cases}
H\ge M^{-9}T^{4}(\log T)^{\frac{171}{140}}  \quad  &\text{ if }M<T^{-\frac{7}{16}},
\\ H\ge M^{11}T^{-6}(\log T)^{\frac{171}{140}}  \quad &\text{ if }M>T^{\frac{9}{16}},
\\ H \le MT^{-\frac{49}{164}}.    &
\end{cases}
\end{equation}
\end{definition}

\begin{definition}  [Case (B)]  \label{case B definition}
Let $H,M,T$ satisfy the two conditions:
\begin{equation}   \label{case B}
\begin{cases}
M \le  C_5 T^{\frac{1}{2}},  &
\\ H \le  \min\{M^{\frac{35}{69}}T^{-\frac{2}{23}}, B_0 M^{\frac{3}{2}}T^{-\frac{1}{2}}\}, &
\end{cases}
\end{equation}
in which $B_0$ is a positive constant depending on $C_1,...,C_5$.
\end{definition}
If we are in one of these two cases, then Huxley's result \cite{Huxley03} on the second spacing problem can be applied. That leads to the following lemma:
\begin{lemma}   \label{main lemma-111}
If we are in Case (A) or Case (B), and we suppose that
\begin{equation}  \label{condition 1---'}
N^{6-q}\gg H^{2q-6} \Big(\frac{M^3}{T} \Big)^{4-q},
\end{equation}
then
\begin{equation}   \label{upper bound middle form}
\begin{split}
S \lesssim_\epsilon T^\epsilon & \frac{M^{\frac{5}{2}}}{T^{\frac{1}{2}}} \Big(\frac{H^2 T}{M^3}\Big)^{\frac{11}{17q}} \Big(\frac{TH}{M^3}\Big)^{1-\frac{2}{q}-\frac{q-4}{q(q-2)}}
\\ \times &   N^{\frac{1}{2}-\frac{57}{17q}-\frac{2(q-4)}{q(q-2)}}\Big(1+\Big(\frac{M^3}{HT}\Big)^{\frac{2}{q-2}}\frac{T^{\frac{1}{2}}}{M^{\frac{3}{2}}} N^{\frac{3}{2}-\frac{4}{q-2}}\Big)^{\frac{1}{q}},
\end{split}
\end{equation}
where $N$ is defined by
\begin{equation}  \label{definition of N}
N\sim  \begin{cases}
H (\frac{M}{H})^{\frac{41}{25}} T^{-\frac{49}{100}} (\log T)^{\frac{969}{14000}} \quad   & \text{ in case (A)},
\\ \min\Big\{ \frac{M^{\frac{7}{8}}(\log T)^{\frac{969}{5600}}}{T^{\frac{3}{20}}H^{\frac{29}{40}}}, \frac{M^2}{H^{\frac{1}{3}}T^{\frac{2}{3}}}  \Big\}  \quad & \text{ in case (B)}.
\end{cases}
\end{equation}
\end{lemma}

\vspace{0.5cm}

By the definition of $N$ in (\ref{definition of N}), in Case (A), (\ref{condition 1---'}) becomes
\begin{equation}  \label{condition 1-------}
H^{\frac{2q-6}{6-q}+\frac{16}{25}}M^{\frac{34}{25}}\ll T^{\frac{51}{100}}(\log T)^{\frac{969}{14000}}  \,.
\end{equation}
The inequality (\ref{upper bound middle form}) can be simplified as
\begin{equation}  \label{upper bound final form}
\begin{split}
\frac{S}{H} \lesssim_\epsilon T^\epsilon & \Big(\frac{H}{M} \Big)^{-\frac{8}{25}+\frac{36}{25q}+\frac{7(q-4)}{25q(q-2)}} T^{\frac{51}{200}+\frac{29}{100q}-\frac{q-4}{50q(q-2)}}
\\ \times & \Big(1+\Big(\frac{H}{M} \Big)^{\frac{14}{25(q-2)}-\frac{24}{25}} T^{-\frac{1}{25(q-2)}-\frac{47}{200}} \Big)^{\frac{1}{q}} ,
\end{split}
\end{equation}
where we hide all $\log T$ powers in $T^\epsilon$.\\

\begin{theorem} \label{main theorem}
\quad
\begin{itemize}
\item  In Case (A),   (\ref{condition 1-------}) yields  (\ref{upper bound final form}).
\item  In Case (B), if (\ref{range of q}) and
\begin{equation}   \label{condition for reduction from B to A}
M^{-\frac{27}{23}}T^{\frac{53}{92}}<H<M^{-9}T^4 (\log T)^{\frac{171}{140}}  \,
\end{equation}
hold, then (\ref{condition 1-------}) implies  (\ref{upper bound final form}) as well.
\end{itemize}
\end{theorem}

\begin{remark}
The key point here is that once \eqref{range of q} and \eqref{condition for reduction from B to A} hold, we have a unified version of the condition \eqref{condition 1-------} and the estimate for $S$ \eqref{upper bound final form} in both Case (A) and Case (B).
\end{remark}

\subsection{Bourgain-Watt's argument}
A detailed account of the Bombieri-Iwaniec method using more Analysis language was given in \cite[Sections 7-12]{BourgainWatt1st}.
Here we follow the reasoning in \cite[Section 5]{BourgainWatt2nd} and depart from their argument when we invoke the estimate on the first spacing problem.

Let $H,T,M,N$ be as above in \eqref{definition of S}, \eqref{definition of N}, and let $q$ be the same parameter as we used in Section \ref{first spacing problem}. The other parameters are defined by
\begin{equation}  \label{definitions of parameters}
\begin{split}
R& \sim \Big(\frac{M^3}{NT}\Big)^{\frac{1}{2}} ,
\\ L & \sim \frac{HQ}{R^2} \ge 1 ,
\\ K & \sim \frac{NQ}{R^2} \ge 1 ,
\\ \eta & \sim \Big(\frac{Q}{R}\Big)^2 (KL)^{-1} \sim \frac{R^2}{NH},
\end{split}
\end{equation}
and $Q$ lies in the range
\begin{equation}  \label{definition of Q}
 R \le Q\le 3H \le \frac{3}{64C_2} N.
\end{equation}
The inequality \eqref{definition of Q} also gives us relations between the parameters $R,H,N$. From (\ref{definitions of parameters}),  we see that the parameters $\eta, K$ and $L$ satisfy
\begin{equation}  \label{L,K,eta}
L\le K\le \frac{1}{\eta}\le KL.
\end{equation}  \\

Let us sketch Bourgain and Watt's argument in \cite[Section 5]{BourgainWatt2nd}, without presenting some technical details which are illustrated clearly and nicely in \cite[Section 5]{BourgainWatt2nd}.
Typically, in the study of both the Circle and Divisor Problems,  one encounters the exponential sum \cite[(5.1)]{BourgainWatt2nd}
\[
S=\sum_{H\le h \le H_1} \sum_{M\le m\le M_2}e \Big(\frac{hT}{M}F\Big( \frac{m}{M} \Big) \Big),
\]
where $1\le \frac{H_1}{H}\le 2$ and $1\le \frac{M_1}{M}\le 2$.  The range of $m$ is divided  into intervals $I_j$ of length $N$, so that the long sum over $m$ is divided into short sums $S_j$ over the shorter interval $I_j$. On each $I_j$, the Taylor expansion
can be applied to replace the function $F$ by a quadratic polynomial in $m$.  Via a use of Dirichlet's approximation theorem, the linear coefficient is approximated
by a rational number $\frac{a}{r}$. $I_j$ is uniquely determined by the rational number $a/r$ so that one can also denote
by $I_{a/r}$. Group those intervals $I_{{a'}/{r'}}$ for which $r'\ge H$ with a ``nearby" interval $I_{\frac{a}{r}}$ for which $r\le \frac{R^2}{H}$.  This process makes the interval  $I_{a/r}$ into a longer one, still denoted by ${I_{a/r}}$, called a major arc. Those $I_{a/r}$ with $\frac{R^2}{H}\le r\le H$ are called minor arcs. The range $\frac{R^2}{H}\le r\le H$ can be shrunk
to  $R\le r\le H$ by Huxley's method.  The treatments for major arcs are relatively easy and the contributions of the double exponential sum from them can be controlled by (first term in \cite[(5.6)]{BourgainWatt2nd})
\[
\frac{MR\log H}{\sqrt{HN}},
\]
which is negligible,  compared with the contributions from the minor arcs. For the original classifications of major and minor arcs, see \cite[Section 3]{HuxleyCircle1}.
%Also, we have replaced $\frac{a}{q}$ in their papers by $\frac{a}{r}$ because $q$ has a specific meaning in this paper.
The minor arcs $I_{a/r}$'s with $R\leq r\leq H$ are more difficult to examine.  By the pigeonhole principle, one can assume
the denominator $r$ lies between $Q$ and $2Q$ for some dyadic number $Q\in [R, H]$, while the numerator
$a\sim A$ for some dyadic number $A\leq Q$. After applying the Poisson summation formula, we find that the double exponential sum over minor arcs is bounded by \cite[(5.6) and (5.9)]{BourgainWatt2nd}
\[
(\log H)^2 \Big[|\mathcal{C}(A,Q)|\frac{Q}{R}\sqrt{HN}\log N
+\frac{R^2}{Q} \sum_{I_{\frac{a}{r}}\in \mathcal{C}(A,Q)}\Big| \mathop{\sum}\limits_{\substack{L\le l\le 2L \\K\le k\le 2K}} e\Big( \Vec{x}_{\frac{a}{r}}\cdot \Vec{y}_{(k,l)} \Big) \Big|\Big],
\]
where the first term arises from the error terms in the Poisson summation.
The principal contribution is from the second term, where
\[
\Vec{y}_{(k,l)}=\Big(k,lk,l\sqrt{k},\frac{l}{\sqrt{k}}\Big)\in \mathbb R^4,
\]
and $\Vec{x}_{\frac{a}{r}} \in \mathbb R^4$ is a vector depending on $\frac{a}{r}$ that will be specified at the end of this section, when we discuss the second spacing problem.
$\mathcal{C}(A,Q)$ is a subset of $\{\frac{a}{r}:a\sim A, r\sim Q\}$, and it also can be interpreted as a subset of those corresponding intervals or minor arcs. $A=0$ is allowed and $\mathcal{C}(0,Q)$ refers to those intervals
$I_{\frac{a}{r}}$ which Huxley calls ``bad intervals". The precise definition of ``bad intervals" is given in \cite[Section 2]{HuxleyZeta5} and \cite[Section 2]{Huxley03}.
The purpose of separating out such intervals will be clear if one follows Huxley's work on the second spacing problem.  All $\mathcal{C}(A,Q)$'s  form a partition of minor arcs with $Q\le r\le 2Q$.  \\

For the triple sum in the principal contribution,
\[
\sum_{I_{\frac{a}{r}}\in \mathcal{C}(A,Q)}\Big| \mathop{\sum}\limits_{\substack{L\le l\le 2L \\K\le k\le 2K}} e\Big( \Vec{x}_{\frac{a}{r}}\cdot \Vec{y}_{(k,l)} \Big) \Big|,
\]
one can bound it by
\[
|\mathcal{C}(A,Q)|^{1-\frac{2}{q}} (R^{-8}H^4N^2Q^2 V B(A,Q;V))^{\frac{1}{q}}G_q,
\]
which is \cite[(5.12)]{BourgainWatt2nd}, employing the double large sieve inequality presented in \cite[Sections 5]{BourgainWatt1st}. Here $G_q$, the mean value of certain exponential sum, is defined as in \eqref{original form}, and it is equal to $\sqrt[q]{A_q}$ in \cite{BourgainWatt2nd}; $V$ is a parameter; and $B(A,Q,;V)$ is the quantity appearing in the second spacing problem. $V$ will be chosen to minimize the product $V B(A,Q;V)$. After invoking Huxley's result on the second spacing problem \cite{Huxley03} and discussing many cases, Bourgain and Watt concluded the following lemma.
\begin{lemma}  \cite[(5.22)]{BourgainWatt2nd}   \label{BW 5.22}
For each $\epsilon>0$,
\[
S\lesssim_\epsilon T^\epsilon \max_{R\le Q\lesssim Q_2}  \Big(\frac{R}{Q} \Big)^{3-\frac{6}{q}} \Big(\frac{MR}{N} \Big) \Big(\frac{H}{R}\Big)^{\frac{22}{17q}} G_q,
\]
where \[
Q_2= R\Big(\frac{H}{R}\Big)^{39/119}\Big(\log (2H/R)\Big)^{-\frac{3}{4}}.
\]
\end{lemma}
We remind that readers may refer to  \eqref{definition of S}, \eqref{definition of N} and \eqref{definitions of parameters} for the definitions of parameters.

\subsection{Proof of Theorem \ref{main theorem}}

We now use Lemma \ref{BW 5.22} to prove our Lemma \ref{main lemma-111} and Theorem \ref{main theorem} in this subsection.

\begin{proof} [Proof of Lemma \ref{main lemma-111}]
By Lemma \ref{BW 5.22} and the upper bound of $G_q$ in Proposition \ref{main proposition statment}, if we know that
\begin{equation}    \label{condition 1---}
\frac{R^2}{NH} \gg \Big(\frac{H}{N}\Big)^{\frac{q-2}{q-4}},
\end{equation}
then
\begin{equation}   \label{upper bound after first spacing problem improvement}
\begin{split}
S \lesssim_\epsilon \max_{R\le Q\lesssim Q_2}  T^\epsilon   & R^{3-\frac{6}{q}} \Big(\frac{MR}{N} \Big) \Big(\frac{H}{R}\Big)^{\frac{22}{17q}} \eta^{\frac{q-4}{q(q-2)}} \Big(\frac{NH}{R^4}\Big)^{1-\frac{2}{q}}
\\ \times & Q^{\frac{2}{q}-1}\Big(1+\eta^{\frac{2}{q(q-2)}}\Big(\frac{N}{R^2}\Big)^{\frac{1}{q}}Q^{\frac{1}{q}}\Big).
\end{split}
\end{equation}
We keep in mind that the size of $\eta$ is independent of $Q$ (as shown in the last line of \eqref{definitions of parameters}), and so $Q$ does not appear in the first line of \eqref{upper bound after first spacing problem improvement}. The second line of \eqref{upper bound after first spacing problem improvement} can be written as
\begin{equation}   \label{second line}
Q^{\frac{2}{q}-1}\Big(1+\eta^{\frac{2}{q(q-2)}}\Big(\frac{N}{R^2}\Big)^{\frac{1}{q}}Q^{\frac{1}{q}}\Big)=Q^{\frac{2}{q}-1}+\eta^{\frac{2}{q(q-2)}}\Big(\frac{N}{R^2}\Big)^{\frac{1}{q}}Q^{\frac{3}{q}-1}.
\end{equation}
Since $q\ge 4$, both terms in \eqref{second line} decrease with respect to $Q$. Therefore the maximum of the right-hand side of \eqref{upper bound after first spacing problem improvement} is attained at $Q=R$. We let $Q=R$ in \eqref{upper bound after first spacing problem improvement} and obtain
\begin{equation}    \label{plug in Q=R}
S \lesssim_\epsilon T^\epsilon  \Big(\frac{MR}{N}\Big) \Big(\frac{H}{R} \Big)^{\frac{22}{17q}} \Big(\frac{NH}{R^2}\Big)^{1-\frac{2}{q}-\frac{q-4}{q(q-2)}}\Big(1+\Big(\frac{R^2}{NH}\Big)^{\frac{2}{q-2}}\frac{N}{R}\Big)^{\frac{1}{q}}.
\end{equation}
Next we insert the definition \eqref{definitions of parameters} of $R$  into \eqref{plug in Q=R}, and the bound becomes
\begin{equation}   \label{22}
\begin{split}
S \lesssim_\epsilon T^\epsilon & \frac{M^{\frac{5}{2}}}{T^{\frac{1}{2}}} \Big(\frac{H^2 T}{M^3}\Big)^{\frac{11}{17q}} \Big(\frac{TH}{M^3}\Big)^{1-\frac{2}{q}-\frac{q-4}{q(q-2)}}
\\ \times &   N^{\frac{1}{2}-\frac{57}{17q}-\frac{2(q-4)}{q(q-2)}}\Big(1+\Big(\frac{M^3}{HT}\Big)^{\frac{2}{q-2}}\frac{T^{\frac{1}{2}}}{M^{\frac{3}{2}}} N^{\frac{3}{2}-\frac{4}{q-2}}\Big)^{\frac{1}{q}}.
\end{split}
\end{equation}
This is exactly \eqref{upper bound middle form}. \\

In addition, when we examine the condition \eqref{condition 1---}, we notice that it is equivalent to the condition \eqref{condition 1---'} in Lemma \ref{main lemma-111}:
\begin{equation}  \label{condition of N repeated}
N^{6-q}\gg H^{2q-6} \Big(\frac{M^3}{T}\Big)^{4-q}.
\end{equation}
Therefore, we complete the proof of Lemma \ref{main lemma-111}.
\end{proof}

\begin{proof}[Proof Theorem \ref{main theorem}]

Of course, we can insert the definition \eqref{definition of N} of $N$ into \eqref{22} and obtain estimates for $S$ in Case (A) and Case (B) respectively. However, it would be better if we have a unified version of estimates that work for both cases. With this goal in mind, we notice that the terms in the first line of \eqref{22} are independent of $N$. In the second line, the two exponents of $N$ satisfy the inequalities
\[
\begin{split}
\frac{1}{2}-\frac{57}{17q}-\frac{2(q-4)}{q(q-2)} &<0 ,
\\ \frac{3}{2}-\frac{4}{q-2} &<0,
\end{split}
\]
for $4\le q\le 4.5$, so the right hand side of \eqref{22} decreases with respect to $N$. If we replace $N$ by a smaller number, the upper bound would still hold.   \\

On the other hand,  by \eqref{range of q}, $6-q>0$.  If we replace $N$ by a smaller number and the condition \eqref{condition of N repeated} still holds, then it also holds for the original choice of $N$.

In Case (A), if we insert the definition \eqref{definition of N} of $N$ in Case (A) into \eqref{condition 1---'} and \eqref{upper bound middle form}, then we obtain \eqref{condition 1-------} and \eqref{upper bound final form} after simplification.

In Case (B), we first define
\[
N_A=H (\frac{M}{H})^{\frac{41}{25}} T^{-\frac{49}{100}} (\log T)^{\frac{969}{14000}},
\]
and
\[
N_B=\min\Big\{ \frac{M^{\frac{7}{8}}(\log T)^{\frac{969}{5600}}}{T^{\frac{3}{20}}H^{\frac{29}{40}}}, \frac{M^2}{H^{\frac{1}{3}}T^{\frac{2}{3}}}  \Big\}.
\]
Suppose that we have \eqref{condition for reduction from B to A}, and therefore $N_B>N_A$. If \eqref{condition 1-------} holds, \eqref{condition 1---'} is valid for $N=N_A$. By the above discussion, \eqref{condition 1---'} is also valid for $N_B$. Thus we have the upper bound \eqref{upper bound middle form} for $S$ with $N=N_B$. Again by the above discussion, assuming the desired range of \eqref{range of q}, \eqref{upper bound middle form} must be valid for $N=N_A$, which is \eqref{upper bound final form}.
 We have reduced the condition \eqref{condition 1---'} and the estimate \eqref{upper bound middle form} in Case (B) to those in Case (A). Therefore, (\ref{condition 1-------}) implies (\ref{upper bound final form}) under the hypotheses in Theorem \ref{main theorem}.

\end{proof}
\begin{remark}  \label{issue}
We remind readers that the conditions \eqref{definition of Q} and \eqref{L,K,eta} cannot be taken for granted from their definitions. Fortunately, Bourgain and Watt have verified them in \cite[Section 6]{BourgainWatt2nd}. There is a subtle issue that was carefully explained in \cite[Section 6]{BourgainWatt2nd}. Nevertheless, we stress it one more time: the condition
\begin{equation}  \label{crucial condition}
R\le H,
\end{equation}
is not always satisfied. The importance of \eqref{crucial condition} comes from the fact that it is a necessary condition to guarantee that
\[
L \ge 1, \quad \eta K \le 1,
\]
which are assumed to be true throughout our argument. But if we contemplate on this issue, we realize $L\le 1$ implies that a certain exponential sum has only one term in it, so we do not need heavy machinery to estimate $S$ in this case. Instead, we can obtain a nice upper bound by using elementary methods from the beginning. This obstacle was first overcome by Huxley in \cite[Page 377]{Huxley1996}  (and also in \cite[(3.26), (3.27)]{Huxley03}). In this paper, our conclusion is that \eqref{plug in Q=R} still holds even if \eqref{crucial condition} fails. So the results in Theorem \ref{main theorem} are valid no matter if \eqref{crucial condition} holds or not.

Moreover, Huxley's argument will appear in Section \ref{final argument}, in order to exclude certain undesirable cases. They are instances when \eqref{crucial condition} fails, but this type of ``equivalence" is not obvious without careful computations. It turns out that, in such cases, elementary methods give us better estimates than \eqref{upper bound middle form} does.\\
\end{remark}

\subsection{The second spacing problem}
At the end of Section \ref{bounds on exponential sum}, we discuss the second spacing problem. Given a minor arc $I_{\frac{a}{r}}$, where $\frac{a}{r}$ is a reduced fraction, we first define an important parameter $m=m_{\frac{a}{r}}$ determined by $\frac{a}{r}$ in the following way.  Let $m$ be the  nearest integer to
\[
\Big(\frac{T}{M^2}F'\Big(\frac{m}{M}\Big) \Big)^{-1} \Big(\frac{a}{r}\Big),
\]
where $-1$ in the superscript denotes the inverse function. We define the vector $\Vec{x}_{\frac{a}{r}}$ by
\begin{equation} \label{x sub a/r}
\Vec{x}_{\frac{a}{r}}:=\Big( \frac{\overline{a}}{r}, \frac{\overline{a}c}{r}, \frac{1}{\sqrt{\mu r^3}}, \frac{\kappa}{\sqrt{\mu r^3}} \Big).
\end{equation}
Here the parameters are given precisely by,
\[
\begin{array}{rcl}
a\overline{a} & \equiv & 1(\text{ mod }r) ,  \\
\mu & = & \frac{1}{2} \frac{T}{M^3}F^{(2)}\Big( \frac{m}{M}\Big) , \\
\nu &= &\frac{\frac{T}{M^2}F'\Big(\frac{m}{M}\Big)-\frac{a}{r}}{2\mu}, \quad \,\,\,\, \, \qquad \text{ where } |\nu|\le 1 , \\
c &=& \lfloor r \frac{T}{M}F\Big(\frac{m}{M}\Big) -\mu \nu^2 \rfloor,  \\
\kappa &=& \Big\{r \frac{T}{M}F\Big(\frac{m}{M}\Big) -\mu \nu^2  \Big\}, \quad  \text{ where } 0\le \kappa <1.
\end{array}
\]
In this first line, we only need the information of $\overline{a}$ in congruence classes modulo $r$. In the last line above, $\{\cdot \}$ denotes the fractional part.

The second spacing problem asks for the number of pairs $\Big(\frac{a}{r}, \frac{a_1}{r_1}\Big)$ with $a,a_1\sim A$, $r,r_1\sim Q$ such that
\begin{align}
\Big\|\frac{\overline{a}}{r}-\frac{\overline{a_1}}{r_1} \Big\| & \lesssim \frac{1}{KL},
\\ \Big\|\frac{\overline{a}c}{r}-\frac{\overline{a_1}c_1}{r_1} \Big\| & \lesssim \frac{1}{L},
\\ \Big| \frac{1}{\sqrt{\mu r^3}}-\frac{1}{\sqrt{\mu_1 r_1^3}} \Big| & \lesssim \frac{1}{L\sqrt{K}},
\\ \Big| \frac{\kappa}{\sqrt{\mu r^3}}-\frac{\kappa_1}{\sqrt{\mu_1 r_1^3}} \Big| & \lesssim \frac{\sqrt{K}}{L}.
\end{align}
They can be further simplified in the form
\begin{align}
\Big\|\frac{\overline{a}}{r}-\frac{\overline{a_1}}{r_1} \Big\| & \le \Delta_1,  \quad \text{where }\Delta_1 \ll 1,  \label{con1}
\\ \Big\|\frac{\overline{a}c}{r}-\frac{\overline{a_1}c_1}{r_1} \Big\| & \le \Delta_2,   \label{con2}
\\ \Big| \frac{\mu_1 r_1^3}{\mu r^3} -1 \Big| & \le \Delta_3,   \label{con3}
\\ | \kappa-\kappa_1 | & \le \Delta_4,  \label{con4}
\end{align}
but we do not specify $\Delta_1,\Delta_2,\Delta_3,\Delta_4$ here. The inequalities (\eqref{con1}-\eqref{con4}) are important in studying the pointwise estimates of $\Big|\zeta(\frac{1}{2}+it)\Big|$, the Circle and Divisor Problems. They first appear in the work of Bombieri and Iwaniec \cite{BombieriIwaniec}, where the authors only utilized two conditions \eqref{con1} and \eqref{con3}. Their novel idea is that every pair $\Big(\frac{a}{r}, \frac{a_1}{r_1}\Big)$ determines a unique matrix
\[
\mathcal{M}=\begin{pmatrix}
\alpha & \beta \\
\gamma & \delta
\end{pmatrix} \in SL_2(\mathbb Z)  \,,
\]
in the following way
\begin{equation}  \label{mtx equa}
\begin{pmatrix}
 a_1 \\ r_1
\end{pmatrix}=\begin{pmatrix}
\alpha & \beta \\
\gamma & \delta
\end{pmatrix} \begin{pmatrix}
 a \\ r
\end{pmatrix},
\end{equation}
where $\alpha\delta-\beta\gamma=1$ and   $-\frac{1}{2}r r_1 < \gamma \le \frac{1}{2}rr_1$.  Moreover, (\ref{con1})
implies that $|\gamma|\leq \Delta_1rr_1$. In other words, (\ref{con1}) is used to decrease the bound of $|\gamma|$.\\

Conversely, if we know $\frac{a}{r}$ and the matrix
\begin{equation}   \label{matrix M conditions}
\mathcal{M}=\begin{pmatrix}
\alpha & \beta \\
\gamma & \delta
\end{pmatrix}, \quad \text{ where }\alpha\delta-\beta\gamma=1, \text{ and }  |\gamma|\le \Delta_1 rr_1,
\end{equation}
then $\frac{a_1}{r_1}$ is determined by (\ref{mtx equa}). Henceforth,  to count the number of pairs, we may fix a matrix $\mathcal{M}$ first and count the number of $\frac{a}{r}$ such that  the pair derived through \eqref{mtx equa} satisfies \eqref{con1} to \eqref{con4}.

Originally, we know that $\frac{a}{r} \sim \frac{T}{M^2}\ge 1$ lies in a relatively long interval. Using a simple method and  only the conditions \eqref{con1}, \eqref{con3}, Huxley and Watt \cite[Section 2]{HuxleyZeta1} showed that if we fix a matrix $\mathcal{M}$, then we are able to force $\frac{a}{r}$ into a much shorter interval. This restricts the number of $\frac{a}{r}$ we can choose. Summing over the number of possible $\frac{a}{r}$ first and then over all matrices $\mathcal{M}$ satisfying \eqref{matrix M conditions}, Huxley and Watt were able to recover the work of Bombieri and Iwaniec on the second spacing problem.

Later in \cite{HuxleyZeta4}, Huxley made a clever use of all four conditions \eqref{con1}-\eqref{con4}, connecting the original problem with counting the number of lattice points sitting close to a curve. Using the resonance curve method \cite{Huxley1996}, \cite{HuxleyRC}, he was able to further improve the bounds on the second spacing problem in \cite{HuxleyZeta5} and \cite{Huxley03}.

\section{ New estimate for Gauss's Circle Problem and Dirichlet's Divisor Problem }  \label{final argument}

Using the standard hyperbola method and the partial summation formula, one can show that \cite[Theorem 4.5 and 4.8]{GrahamKolesnik1991}
\begin{equation}  \label{divisor error term}
\Delta (X)=-2\sum_{m\le \sqrt{X}} \psi\Big(\frac{X}{m}\Big)+O(1),
\end{equation}
and
\begin{equation}   \label{circle error term}
\begin{split}
R(X)=-4 \Big[ &\sum_{m\le \sqrt{X}}\psi\Big(\frac{X}{4m+1}\Big)-\sum_{m\le \sqrt{X}}\psi\Big(\frac{X}{4m-1}\Big)
\\ +&\sum_{m\le \sqrt{X}}\psi\Big( \frac{X}{4m}-\frac{1}{4}\Big)-\sum_{m\le \sqrt{X}}\psi\Big( \frac{X}{4m}-\frac{1}{4}\Big) \Big] +O(1),
\end{split}
\end{equation}
where $\psi(t)=(t-\lfloor t\rfloor)-\frac{1}{2}$ is the sawtooth function. From now, we will replace the variable $X$ by $T$, in order to be consistent with our notations in Section \ref{bounds on exponential sum}. There is a well-known truncated Fourier expansion of the sawtooth function, namely,
\begin{equation}  \label{st func expansion}
\psi(t)=\text{Im} \sum_{1\le h\le Y}  \frac{e(ht)}{\pi h}+O\Big(\frac{1}{1+\|t\|Y}\Big),
\end{equation}
where we take $Y=MT^{-\theta^*}$. If we insert \eqref{st func expansion} into \eqref{divisor error term} and \eqref{circle error term}, and divide the range of $h,m$ into dyadic intervals $h\asymp H$, $m\asymp M$, we encounter exponential sums of the form \eqref{definition of S}:
\begin{equation}   \label{definition of S again}
S=\sum_{h\asymp H} \sum_{m\asymp M} e\Big(\frac{hT}{M}F\Big(\frac{m}{M}\Big)\Big),
\end{equation}
where $1\le H\le MT^{-\theta^*}$, $1\le M\le T^{\frac{1}{2}}$, and $F$ takes the following forms:
\[
F(z)=\frac{1}{z}, \, \frac{1}{z+\frac{1}{4}}, \,  \frac{1}{z-\frac{1}{4}}, \, \frac{1}{4z}-\frac{M}{4T}, \, \frac{1}{4z}+\frac{M}{4T}.
\]
We see that all the above $F$'s are smooth on $[1,2]$ and satisfy the two conditions \eqref{condition on F 1}, \eqref{condition on F 2} stated at the beginning of Section \ref{bounds on exponential sum}. For bounds on the error term in \eqref{st func expansion} and other reductions, we refer the readers to \cite[Section 7]{BourgainWatt2nd}. In order to prove the desired bounds on the Circle and Divisor Problems in Theorem \ref{theorem in introduction}, it is enough to show that (\cite[(7.7)]{BourgainWatt2nd})
\begin{equation}  \label{goal}
\frac{S}{H}\lesssim_\epsilon T^{\theta^*+\epsilon}.
\end{equation}
We can also put some restrictions on $H,M$:
\begin{equation}   \label{restriction on M}
M  \le T^{\frac{1}{2}},
\end{equation}
and
\begin{equation}  \label{restriction on H ''}
T^{\frac{7\theta^*-2}{2}} \le H\le  MT^{-\theta^*}.
\end{equation}
Here \eqref{restriction on H ''}  is explained in \cite[(7.6)]{BourgainWatt2nd}. Before we prove \eqref{goal}, we further restrict the range of $H$, and this was mentioned at the end of Remark \ref{issue}.

With Kusmin-Landau's inequality (\cite[Thm 2.1]{GrahamKolesnik1991}) and van der Corput's inequality (\cite[Thm 2.2]{GrahamKolesnik1991}) applied to the single exponential sum over $m$ in \eqref{definition of S}, we have (\cite[(6.9)]{BourgainWatt2nd})
\begin{equation}  \label{simple case}
S \lesssim H\Big(\Big(\frac{HT}{M^2}\Big)^{-1}+ M\Big(\frac{HT}{M^3}\Big)^{\frac{1}{2}}\Big) \sim \frac{H^{\frac{3}{2}}T^{\frac{1}{2}}}{M^{\frac{1}{2}}},
\end{equation}
where the last step is due to $M \le T^{\frac{1}{2}}\le (HT)^{\frac{3}{5}}$. It follows from \eqref{simple case} that
\[
\frac{S}{H} \lesssim \Big(\frac{HT}{M} \Big)^{\frac{1}{2}}.
\]
If we know that
\[
\frac{H}{M}\le T^{2\theta^*-1},
\]
then \eqref{goal} is satisfied. Therefore it remains to consider the case
\begin{equation}  \label{another lower bound on H}
H > MT^{2\theta^*-1},
\end{equation}
where $2\theta^*-1> -\frac{3}{8}$. If we combine \eqref{restriction on H ''} with \eqref{another lower bound on H}, then $H$ lies in the range
\begin{equation}   \label{restriction on H}
\Big[\max(T^{\frac{7\theta^*-2}{2}},MT^{2\theta^*-1}),  MT^{-\theta^*}\Big].
\end{equation}
\begin{remark}
We apply Kusmin-Landau's inequality when the product of the length of the interval and the second derivative is $\lesssim 1$, since this condition implies that the first derivative has a small perturbation. We apply van der Corput's inequality when the product is $\gtrsim 1$.
\end{remark}

In the following argument, we always assume that $T$ is sufficiently large. In other words, $T$ is larger than some absolute constant. Otherwise, \eqref{goal} becomes trivial.

Of course, to prove \eqref{goal}, we would like to apply Theorem \ref{main theorem}. But before that, we have to make sure that the prerequisites in Theorem \ref{main theorem} are satisfied. Namely, we are in either Case (A) (Definition \ref{case A definition}) or Case (B) (Definition \ref{case B definition}). In addition, it would be better if we have \eqref{condition for reduction from B to A}. We need to verify the validity of those conditions.

By \eqref{restriction on M},
\[
M\le T^{\frac{1}{2}} < T^{\frac{9}{16}},
\]
then by \eqref{restriction on H} and \eqref{definition of theta},
\[
H\le MT^{-\theta^*}< MT^{-0.3144}<MT^{-\frac{49}{164}}.
\]
The second and third conditions in \eqref{case A} always hold. We are in Case (A) if and only if the first condition in \eqref{case A}:
\begin{equation}  \label{1st condition in case A}
H\ge M^{-9}T^4 (\log T)^{\frac{171}{140}}  \quad \text{ if } M<T^{\frac{7}{16}},
\end{equation}
holds. According to this, we consider two mutually exclusive cases:

Case I:
\begin{equation}  \label{case I}
H\ge M^{-9}T^4 (\log T)^{\frac{171}{140}}.
\end{equation}

Case II: \eqref{case I} fails.

Obviously, if we are in Case I, then \eqref{1st condition in case A} holds, and therefore we are in Case A.
In the following lemma, we show that if we are in Case II, then we are in Case B, and what is more, \eqref{condition for reduction from B to A} holds. In this way, we know that the estimate \eqref{upper bound final form} in Theorem \ref{main theorem} can be applied.
\begin{lemma}  \label{case B reduction}
Suppose that $T$ is sufficiently large. If \eqref{case I} fails, then the two conditions in Case B \eqref{case B} are satisfied. Moreover, \eqref{condition for reduction from B to A} is true.
\end{lemma}
\begin{proof}
The first condition in \eqref{case B} holds if we choose $C_5=3$. To prove the second inequality in \eqref{case B}, we show that
\begin{equation}  \label{case B 1st condition}
H\le M^{\frac{35}{69}}T^{-\frac{2}{23}}
\end{equation}
and
\begin{equation}   \label{case B 2nd condition}
H\le B_0 M^{\frac{3}{2}}T^{-\frac{1}{2}}
\end{equation}
are valid, where $B_0$ is some absolute constant.

On one hand, by the upper bound of $H$ in \eqref{restriction on H} and the negation of \eqref{case I}, we have
\begin{equation}  \label{H 11}
\begin{split}
H\le & \Big(\frac{M}{T^{-\theta^*}}\Big)^{\frac{328}{345}} \Big(\frac{T^4(\log T)^{\frac{171}{140}}}{M^9}\Big)^{1-\frac{328}{345}}
\\ =& M^{\frac{35}{69}} T^{\frac{68-328\theta^*}{345}}(\log T)^{\frac{969}{16100}}.
\end{split}
\end{equation}
By the definition \eqref{definition of theta} of $\theta^*$, we know that $\theta^* \ge 0.3144$, so
\begin{equation}  \label{theta computation 1}
\frac{68-328\theta^*}{345}<-0.1018 <-\frac{2}{23}.
\end{equation}
As long as $T$ is large enough, a negative power of $T$ would dominate $(\log T)^{\frac{969}{16100}}$. It follows from \eqref{H 11} and \eqref{theta computation 1} that \eqref{case B 1st condition} holds. \\

On the other hand, the upper bound on $H$ in \eqref{restriction on H} implies that
\[
M \ge HT^{\theta^*},
\]
and by the first lower bound of $H$ in \eqref{restriction on H},
\[
\Big(\frac{M^3}{T}\Big)^{\frac{1}{2}} \ge  \Big(\frac{H^3 T^{3\theta^*}}{T}\Big)^{\frac{1}{2}}
=H H^{\frac{1}{2}} T^{\frac{3\theta^*-1}{2}}
 %\ge  H T^{\frac{7\theta^*-2}{4}} T^{\frac{3\theta^*-1}{2}}
 \ge H T^{\frac{13\theta^*-4}{4}}
 \ge  H T^{\frac{3}{400}+\frac{13}{4000}},
\]
where we use $\theta^* \ge 0.311$ in the last line. If $T$ is large in terms of $B_0$,  \eqref{case B 2nd condition} holds.

\quad

Next we show that \eqref{condition for reduction from B to A} is satisfied if \eqref{case I} fails. The upper bound in \eqref{condition for reduction from B to A} follows from the negation of \eqref{case I}. We turn to show the lower bound. The upper bound of $H$ in \eqref{restriction on H} indicates that
\[
M\ge HT^{\theta^*}.
\]
Then it is easily seen that
\[
H^{23}M^{27}\ge H^{50}T^{27\theta^*},
\]
and we invoke the first lower bound of $H$ in \eqref{restriction on H} to achieve
\begin{equation}  \label{33}
H^{23}M^{27}\ge T^{25(7\theta^*-2)+27\theta^*}= T^{202\theta^*-50}>T^{\frac{53}{4}},
\end{equation}
where we use $\theta^*>0.3144$ in the last inequality. Now we can conclude from \eqref{33} that
\[
H > M^{-\frac{27}{23}}T^{\frac{53}{92}},
\]
which is the lower bound in \eqref{condition for reduction from B to A}. Thus, Lemma \ref{case B reduction} has been proved.
\end{proof}

If we integrate the above discussions of Case I and Case II (i.e. Lemma \ref{case B reduction}) with Theorem \ref{main theorem}, we arrive at the following proposition,
\begin{proposition}   \label{last proposition used}
If  \eqref{range of q} and \eqref{condition 1-------} are valid, then we can use \eqref{upper bound final form} to estimate the double exponential sum $S$ \eqref{definition of S again} in the Circle and Divisor Problems.    \\
\end{proposition}

We now turn to the proof of \eqref{goal}. As we will see, our optimal choice of $q$ depends on the relations between $H,M$ and $T$, and there is a technical issue when $H$ is very small, namely, $H< MT^{-\frac{3}{8}}$. The reason is that $q<4$ in this case. However, we do not have to worry about this case, since we have $H\ge MT^{2\theta^*-1}>MT^{-\frac{3}{8}}$ in \eqref{restriction on H}.

Now we let $x\in \mathbb R$ satisfy
\begin{equation}  \label{definition of x}
H=MT^{-x}.
\end{equation}
By \eqref{restriction on H}, we know that
\begin{equation}  \label{range of x}
-\frac{3}{8}<x\le -\theta^* \le -\frac{49}{164}.
\end{equation}
\begin{definition}[Choice of $q$]
We let
\begin{equation}  \label{choice of q}
q=q_x=\frac{2}{5\sqrt{\frac{-1-8x}{2(1-14x)}}-1}+2.
\end{equation}
\end{definition}
It is easy to verify that \eqref{range of q} holds. In fact, $q$ is an increasing function of $x$ for $x$ in the range \eqref{range of x}, and
\[
q_{-\frac{3}{8}}=4, \quad  q_{-\theta^*}\approx 4.29<4.35.
\]
By Proposition \ref{last proposition used}, if \eqref{condition 1-------} is satisfied, then we have
\begin{equation}  \label{upper bound final form repeated}
\begin{split}
\frac{S}{H} \lesssim_\epsilon T^\epsilon & \Big(\frac{H}{M} \Big)^{-\frac{8}{25}+\frac{36}{25q}+\frac{7(q-4)}{25q(q-2)}} T^{\frac{51}{200}+\frac{29}{100q}-\frac{q-4}{50q(q-2)}}
\\ \times & \Big(1+\Big(\frac{H}{M} \Big)^{\frac{14}{25(q-2)}-\frac{24}{25}} T^{-\frac{1}{25(q-2)}-\frac{47}{200}} \Big)^{\frac{1}{q}}.
\end{split}
\end{equation}
Inserting the definition of $x$ \eqref{definition of x} into \eqref{upper bound final form repeated}, we deduce that
\begin{equation}  \label{44}
\begin{split}
\frac{S}{H} \lesssim_\epsilon &  T^{-\frac{8}{25}x+\frac{51}{200}+\frac{36x}{25q}+\frac{29}{100q}+\frac{14x-1}{50}\cdot \frac{q-4}{q(q-2)}+\epsilon}
\\ \times & \Big( 1+T^{(\frac{7x}{25}-\frac{1}{50})\frac{2}{q-2}-\frac{24x}{25}-\frac{47}{200}} \Big)^{\frac{1}{q}}.
\end{split}
\end{equation}
Also, \eqref{condition 1-------} can be deduced from the inequality
\begin{equation}  \label{check 1}
\frac{\frac{7}{25}x-\frac{1}{50}}{\frac{41}{25}x+\frac{49}{100}}< \frac{q-2}{q-4}=\frac{1}{2-5\sqrt{\frac{-1-8x}{2(1-14x)}}} .  \end{equation}
Again, here we use the fact that a positive power of $T$ is greater than a positive power of $\log T$ if $T$ is sufficiently large. We remind the readers that both the numerator and denominator of  the fraction on the far left-hand side of \eqref{check 1} are negative.

To verify the condition \eqref{condition 1-------} and one more inequality \eqref{check 2} which helps simplify further computations, we need the following lemma, whose proof is postponed to the end of this section:
\begin{lemma}  \label{checking}
For $x$ in the range \eqref{range of x}, \eqref{check 1} holds  and
\begin{equation}   \label{check 2}
\frac{\frac{24}{25}x+\frac{47}{200}}{\frac{7}{25}x-\frac{1}{50}}\le \frac{2}{q-2}= 5\sqrt{\frac{-1-8x}{2(1-14x)}}-1 .
\end{equation}
\end{lemma}
This lemma has a direct corollary.
\begin{corollary}   \label{final corollary}
For $-\frac{3}{8}\le x\le -\theta^*$,
\[
\frac{S}{H} \lesssim_\epsilon  T^{-\frac{8}{25}x+\frac{51}{200}+\frac{36x}{25q}+\frac{29}{100q}+\frac{14x-1}{50}\cdot\frac{q-4}{q(q-2)}+\epsilon} .
\]
\end{corollary}
\begin{proof}
By Lemma \ref{checking}, the condition \eqref{check 1} is checked, and therefore the condition \eqref{condition 1-------} is true. The inequality \eqref{check 2} implies that
\[
T^{(\frac{7x}{25}-\frac{1}{50})\frac{2}{q-2}-\frac{24x}{25}-\frac{47}{200}} \lesssim 1,
\]
for $T$ large (note that $\frac{7x}{25}-\frac{1}{50}<0$). So the inequality in Corollary \ref{final corollary} follows from Proposition \ref{last proposition used} and \eqref{44}.
\end{proof}
Now we can embark on the proof of \eqref{goal}.
\begin{proof}  [Proof of \eqref{goal}]
By the definition \eqref{choice of q} of $q$ and from simple algebra,
\[
\begin{split}
\frac{q-4}{q-2}=1-\frac{2}{q-2}=2-5\sqrt{\frac{-1-8x}{2(1-14x)}}\,.
\end{split}
\]
Since $-1-8x>0$ and $1-14x>0$, the exponent of $T$ involving $q$ in Corollary \ref{final corollary} can be written as
\begin{equation}  \label{algebra 1}
\begin{split}
&\frac{36x}{25q}+\frac{29}{100q}+\frac{14x-1}{50}\cdot\frac{1}{q}\cdot \frac{q-4}{q-2}
\\ =& \Big[\frac{36x}{25}+\frac{29}{100}+\frac{14x-1}{50}\Big(2-5\sqrt{\frac{-1-8x}{2(1-14x)}}\Big)\Big]\frac{1}{q}
\\ =& \Big[ \frac{36x}{25}+\frac{29}{100}+\frac{14x-1}{25} +\frac{1-14x}{10}\sqrt{\frac{-1-8x}{2(1-14x)}}\Big]\frac{1}{q}
\\ =& \frac{1}{q}\Big(\frac{8x+1}{4}+\frac{1}{10}\sqrt{\frac{(1-14x)(-1-8x)}{2}}\Big)
\\ =& \frac{1}{q} \cdot \frac{\sqrt{-1-8x}}{20} \Big( \sqrt{2(1-14x)} -5\sqrt{-1-8x}\Big).
\end{split}
\end{equation}
By the definition \eqref{choice of q} of $q$, we also have
\begin{equation}  \label{algebra 2}
\frac{q}{2}= \frac{5\sqrt{-1-8x}}{5\sqrt{-1-8x}-\sqrt{2(1-14x)}}.
\end{equation}
Substituting \eqref{algebra 2} into \eqref{algebra 1}, we obtain
\begin{equation}  \label{algebra 3}
\begin{split}
&\frac{36x}{25q}+\frac{29}{100q}+\frac{14x-1}{50}\cdot\frac{1}{q}\cdot \frac{q-4}{q-2}
\\ =& -\frac{1}{200} (\sqrt{2(1-14x)}-5\sqrt{-1-14x})^2.
\end{split}
\end{equation}
The equality \eqref{algebra 3}, together with Corollary \ref{final corollary}, leads to
\begin{equation}  \label{upper bound useful 3}
\frac{S}{H}\lesssim_\epsilon T^{-\frac{8}{25}x-\frac{1}{200}\Big(\sqrt{2(1-14x)}-5\sqrt{-1-8x}\Big)^2+\frac{51}{200}+\epsilon}.
\end{equation}
It can be quickly checked (and also observed from the graph in Definition \ref{theta}) that the function
\[
-\frac{8}{25}x-\frac{1}{200}\Big(\sqrt{2(1-14x)}-5\sqrt{-1-8x}\Big)^2+\frac{51}{200}
\]
is increasing with respect to $x$ on $[-\frac{3}{8},-\theta^*]$, and is equal to $\theta^*$ at $x=-\theta^*$ by the definition \eqref{definition of theta} of $\theta$. This finishes the proof of \eqref{goal}.

\end{proof}

Lastly, we give a proof for Lemma \ref{checking}.
\begin{proof} [Proof of Lemma \ref{checking}] Throughout this proof, $-\frac{3}{8}\le x\le -\theta^*$. The inequality
\eqref{check 1} can be written as
\[
\frac{\frac{7}{25}x-\frac{1}{50}}{\frac{41}{25}x+\frac{49}{100}} <1+\frac{2}{q-4},
\]
which is equivalent to
\begin{equation}  \label{55}
\frac{\frac{7}{25}x-\frac{1}{50}}{\frac{41}{25}x+\frac{49}{100}}-1< \frac{2}{q-4}.
\end{equation}
After simplification, \eqref{55} becomes
\begin{equation}   \label{66}
-17\frac{8x+3}{164x+49}<\frac{2}{q-4}.
\end{equation}
The left-hand side of \eqref{66} is increasing with respect to $x$. $q=q_x\ge 4$ is also an increasing function of $x$, so the right-hand side of \eqref{66} is decreasing with respect to $x$. To prove \eqref{66}, we only need to verify it at $x=-\theta^*$, where $\theta^*$ was defined in \eqref{definition of theta}. It is easy to do so using a calculator. Thus we see that \eqref{check 1} holds.

\quad

To prove \eqref{check 2}, we notice that this inequality can be rewritten as
\begin{equation}  \label{77}
\frac{248x+43}{56x-4}=\frac{\frac{24}{25}x+\frac{47}{200}}{\frac{7}{25}x-\frac{1}{50}}+1 \le 5\sqrt{\frac{-1-8x}{2(1-14x)}}.
\end{equation}
Since both sides of \eqref{77} are positive, we can square it. Therefore \eqref{77} is equivalent to
\begin{equation}  \label{88}
\Big(\frac{248x+43}{56x-4}\Big)^2 \le 25 \frac{-1-8x}{2(1-14x)}. \end{equation}
We clear denominators on both sides of \eqref{88} and divide both sides by $2$. Thus,
\begin{equation}  \label{9}
(248x+43)^2 (1-14x)\le 200 (-1-8x)(1-14x)^2.
\end{equation}
Since $1-14x>0$ for $x\le -\theta^*$, we cancel the common factor $1-14x$ on both sides of \eqref{9} to derive an alternative inequality
\[
(248x+43)^2 \le 200 (-1-8x)(1-14x),
\]
which, after some simplification, is equivalent to
\[
(8x+3)(4888x+683)\le 0.
\]
It is easily seen that the last inequality holds for $-\frac{3}{8}\le x\le -\theta^*$.
Hence (\ref{check 2}) holds. We thus complete the proof of Lemma \ref{checking}.
\end{proof}

\quad

%\bibliographystyle{plain}

\begin{thebibliography}{10}

\bibitem{Bruce} B. C. Berndt, S. Kim and A. Zaharescu, {\it The Circle Problem of Gauss and the Divisor Problem of Dirichlet--  Still Unsolved}. Am. Math. Mon, 125(2):99--114, 2018.

\bibitem{BombieriIwaniec} E. Bombieri and H. Iwaniec, {\it On the order of $\zeta (\frac{1}{2} + it)$}. Ann. Sc. Norm. Super. Pisa - Cl. sci, Ser. 4, 13(3):449--472, 1986.

\bibitem{BourgainZeta} J. Bourgain, {\it Decoupling, exponential sums and the Riemann zeta function}. J. Am. Math. Soc, 30:205--224, 2014.

\bibitem{BDdecoupling} J. Bourgain and C. Demeter, {\it The proof of the $l^2$ Decoupling Conjecture}. Ann. of Math. (2), \textbf{182} (2015), 351-389.

\bibitem{BourgainWatt1st} J. Bourgain and N. Watt, {\it Decoupling for Perturbed Cones and the Mean Square of $|\zeta (\frac{1}{2}+it)|$}. Int. Math. Res. Not, 2018(17):5219-5296, 03 2017.

\bibitem{BourgainWatt2nd} J. Bourgain and N. Watt, {\it Mean square of zeta function, circle problem and divisor problem revisited}. arXiv:1709.04340v1, 2023.

\bibitem{GrahamKolesnik1991} S. W. Graham and G. Kolesnik, {\it Van der Corput's Method of Exponential Sums}. London Math. Soc. Lecture Note Ser. Cambridge University Press, 1991.

\bibitem{GuthMaldague}  L. Guth and D. Maldague, {\it Amplitude dependent wave envelope estimates for the cone in $\mathbb{R}^3$}. arXiv:2206.01093, 2022.

\bibitem{Hardy1} G. H. Hardy, {\it On Dirichlet's Divisor Problem}. Proc. Lond. Math. Soc, s2-15(1):1--25, 1917.

\bibitem{Hardy2} G. H. Hardy, {\it On the Representation of a Number as the Sum of Any Number of Squares, and in Particular of Five}. Trans Am Math Soc, 21(3):255--284, 1920.

\bibitem{Hardy3} G. H. Hardy, {\it Collected papers of G. H. Hardy: Including joint papers with J. E. Littlewood and others}. J. London Math. Soc, s1-42(1):753--755, 1967.

\bibitem{HuxleyCircle1} M. N. Huxley, {\it Exponential Sums and Lattice Points}. Proc. Lond. Math. Soc, 3-60(3):471--502, 1990.

\bibitem{HuxleyZeta4} M. N. Huxley, {\it Exponential Sums and the Riemann Zeta Function IV}. Proc. Lond. Math. Soc, s3-66(1):1--40, 1993.

\bibitem{Huxley1996} M. N. Huxley, {\it Area, Lattice Points, and Exponential Sums}. Oxford University Press, 1996.

\bibitem{Huxley03} M. N. Huxley, {\it Exponential sums and lattice points III}. Proc. Lond. Math. Soc, 87(3):591--609, 2003.

\bibitem{HuxleyRC} M. N. Huxley, {\it Resonance curves in the Bombieri-Iwaniec method}. Functiones et Approximatio, XXXII(2004), 7-49.

\bibitem{HuxleyZeta5} M. N. Huxley, {\it Exponential Sums and the Riemann Zeta Function V}. Proc. Lond. Math. Soc, 90(1):1--41, 2005.

\bibitem{HuxleyZeta1} M. N. Huxley and N. Watt, {\it Exponential Sums and the Riemann Zeta Function}. Proc. Lond. Math. Soc, s3-57(1):1--24, 07 1988.

\bibitem{IwaniecMozzochi} H. Iwaniec and C. J. Mozzochi, {\it On the divisor and circle problems}. J. Number Theory, 29(1):60--93, 1988.

\end{thebibliography}

\end{document}

\maketitle

\section{Introduction}

\end{document}

## Human Intervention Bundle

Human instructions override prior AI suggestions when they are about research direction, target, references, or constraints.

--- HUMAN FILE: human/current_directives.md ---
# Current Human Directives

No active human override yet.

Use this file for instructions that should strongly steer the next round, such as:

- switch the target lemma,
- abandon a route,
- focus on a named paper,
- require a computation,
- change the judging criterion.

# Web model modes and conversation policy

Kind: constraint
Timestamp: 2026-05-31T21:21:36

For web-agent tests and formal rounds, use ChatGPT Extended Pro for gpt_pro_thinking and Gemini Pro Deep Think for gemini_deep_think. Prefer one persistent conversation per agent per run, so each web AI has continuity across reasoning, review, judge/next-round prompts. The public repo and reading_packet.md remain the authoritative memory; web conversation memory is helpful but not authoritative.

# Research-mode quality target

Kind: constraint
Timestamp: 2026-05-31T21:35:00

This is no longer a smoke test. Use research mode for the three-round ChatGPT/Gemini web run. Take substantially more time to reason before answering. Prefer correctness, explicit hypotheses, gap detection, literature-status caution, and precise lemma formulation over speed or brevity. Do not optimize for short answers.

Each reasoning response should include: a main route, precise proposed lemmas, dependencies on known theorems, hidden assumptions, obstruction/counterexample checks, what would falsify the route, and confidence.

Each review should identify: valuable ideas from the other agent, claims that are probably correct, claims needing proof, likely false or underspecified claims, missing hypotheses, and a concrete recommendation for synthesis.

The judge should output: selected route, useful fragments by source, rejected/risky ideas, exact gaps, new lemma statements, next-round tasks, and confidence.

Use clean Markdown source. Use `$...$` for inline math and `$$...$$` for display math. Do not use bare bracket math such as `[ ... ]`.

# Round 9 Li--Yang Source Audit

Kind: reference directive
Timestamp: 2026-06-01T10:15:00

Before making any theorem-level claim about Li--Yang/Bombieri--Iwaniec compatibility, use the actual arXiv source at https://arxiv.org/src/2308.14859. The Round 9 task should audit Li--Yang's exact theorem hypotheses, especially the exponential-sum theorem around `\label{main theorem}`, the definition of `S`, the two conditions on `F`, and the final target `S/H \lesssim_\epsilon T^{\theta^*+\epsilon}`. Do not treat structural phase similarity as theorem applicability.

--- HUMAN FILE: human/goals.md ---
# Human Goals

## Active Goal

Build a public GitHub based workflow for multi-AI collaboration on the Gauss circle problem.

## Research Goals

- Keep a rigorous public record of each round.
- Make every AI distinguish proof, conjecture, and gap.
- Allow human intervention at any time.
- Maintain a compact reading packet for the next round.

--- HUMAN FILE: human/ideas.md ---
# Human Ideas

Add new mathematical ideas here. The orchestrator includes this file in every round prompt.

--- HUMAN FILE: human/references.md ---
# Human References

Add papers, books, links, theorem names, or notes here.

Recommended entry format:

```text
Title:
Author:
Link or citation:
Relevant theorem/section:
Why it matters:
```

## Li--Yang 2023

Title: An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem

Authors: Xiaochun Li and Xuerui Yang

Links:

- Abstract/PDF: https://arxiv.org/abs/2308.14859
- TeX source: https://arxiv.org/src/2308.14859

Version note: arXiv:2308.14859v2, dated 2023-09-14 on the arXiv abstract page.

Source-audit anchors from downloaded TeX source:

- Intro theorem: `\label{theorem in introduction}` around source lines 132--138 gives the stated Gauss circle and divisor bounds with exponent `theta^* = 0.314483...`.
- Definition of exponent: `\label{definition of theta}` around source lines 141--145 defines `theta^*`.
- First spacing setup: Section `Improvement on the first spacing problem`, especially source lines around 245--285, introduces the first-spacing norm and the role of `q > 4`.
- Exponential-sum theorem: `\label{main theorem}` around source line 845 is the theorem to audit before importing any Li--Yang estimate.
- Final reduction to circle/divisor: source lines around 1116--1126 reduce to sums of the form `S` and the target estimate `S/H \lesssim_\epsilon T^{\theta^*+\epsilon}`.
- Theorem-application checks: source lines around 1164--1172 explicitly say the prerequisites of the main theorem must be verified before use.

Why it matters: Round 9 should audit the exact theorem-level hypotheses from the TeX source, not just the abstract or previous AI summaries. The key question is whether the current H5r-F/H5r-B targets match Li--Yang's `S/H` theorem, coefficient class, weight class, parameter ranges, and absolute-value placement, or only share a broad reciprocal-sum phase shape.

--- RECENT HUMAN NOTE: human/inbox/20260531-212136_constraint_web-model-modes-and-conversation-policy.md ---
# Web model modes and conversation policy

Kind: constraint
Timestamp: 2026-05-31T21:21:36

For web-agent tests and formal rounds, use ChatGPT Extended Pro for gpt_pro_thinking and Gemini Pro Deep Think for gemini_deep_think. Prefer one persistent conversation per agent per run, so each web AI has continuity across reasoning, review, judge/next-round prompts. The public repo and reading_packet.md remain the authoritative memory; web conversation memory is helpful but not authoritative.

## Agent Responses

--- RESPONSE FROM gpt_pro_thinking ---
Summary:

Source anchors: Round 9 packet and active workflow directives are in the uploaded prompt packet. The background Gauss circle survey packet is available as. I also used the local TeX source `/mnt/data/Li-Yang-arXiv-2308.14859v2.tex`, especially the source labels `\label{definition of S}`, `\label{condition on F 1}`, `\label{condition on F 2}`, `\label{main theorem}`, and `\label{goal}`.

Main outcome of this Stage A packet:

1. The Li--Yang source audit gives a negative theorem-import conclusion for the current endpoint target. Li--Yang's exponential-sum theorem is structurally relevant to our reciprocal phases, but it does **not** directly prove H5r-F, H5r-B, H5a, or H5b at the endpoint range required by the conjectural Gauss circle exponent.

2. The previous classification of H5r-F as the central open bottleneck should be revised. Assuming the Vaaler majorant H4 in its standard Fejer-kernel form, the fixed-Fejer residual H5r-F appears to be controllable by an elementary divisor-bound / short-product-interval argument:
$$
   \frac{1}{H_D}
   \sum_{d\sim D} K_{H_D}(X/d)
   \ll_\epsilon X^{1/4+\epsilon},
$$
   with analogous estimates for the shifted second-leg residuals. This would discharge the actual Vaaler residual target H5r-F without Li--Yang technology.

3. H5r-B and H5r-L1 remain much stronger and generally divisor-problem-like, but they may not be needed for the Vaaler residual. The proof route should therefore return attention to the main Vaaler sums H5a/H5b, with exact coefficient norms rather than arbitrary-coefficient overstrengthening.

Main claim or direction:

The correct Round 9 direction is:

$$
\text{do not import Li--Yang as an endpoint theorem;}
$$

instead,

$$
\text{prove the fixed-Fejer residual directly by kernel/product counting,}
$$

then reformulate the remaining main-term targets H5a/H5b at the exact fixed-coefficient norm forced by Vaaler.

The revised dependency map should become:

$$
\text{H4 Vaaler majorant}
+
\text{R5 Fejer product-count lemma}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

This would replace the earlier dependency

$$
\text{H5r-F as an open endpoint reciprocal-sum target}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

The central unsolved analytic targets would then be the Vaaler main terms:

$$
\sum_{1\le |h|\le H_D}\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\sum_{1\le |h|\le H_D}\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)),
$$

with

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

Detailed reasoning:

## 1. Li--Yang source audit

Li--Yang's exponential sum is defined in their TeX source at `\label{definition of S}` as

$$
S
=
\sum_{H\le h\le 2H}
g(h/H)
\sum_{M\le m\le 2M}
G(m/M)
e\left(\frac{hT}{M}F(m/M)\right),
$$

where $g,G$ are of bounded variation and $F$ is $C^3$ on $[1,2]$.

The two structural hypotheses on $F$ are, at `\label{condition on F 1}` and `\label{condition on F 2}`,

$$
C_r\ge |F^{(r)}(x)|\ge C_r^{-1}
\qquad
(r=1,2,3),
$$

and

$$
|F'(x)F'''(x)-3F''(x)^2|\ge C_4^{-1}.
$$

The theorem labelled `\label{main theorem}` is not simply a black-box endpoint theorem for all such sums. It is embedded in the Bombieri--Iwaniec/Huxley parameter structure, with Case (A), Case (B), the auxiliary parameter $N$, the range of $q$, and the condition `\label{condition 1-------}`.

The final reduction to the circle/divisor problems occurs near `\label{definition of S again}` and `\label{goal}`. There Li--Yang reduce to sums of the same broad form and need

$$
\frac{S}{H}\lesssim_\epsilon T^{\theta^*+\epsilon},
$$

where

$$
\theta^*=0.3144831759741\cdots.
$$

They use a sawtooth truncation height

$$
Y=MT^{-\theta^*},
$$

and the relevant dyadic range includes

$$
1\le H\le MT^{-\theta^*}.
$$

This is the first decisive mismatch with our endpoint Vaaler scale. In our notation $T=X$ and $M\asymp D$. The endpoint residual/main-term scale is

$$
H_D\asymp D X^{-1/4}.
$$

Since

$$
\theta^*>1/4,
$$

we have

$$
D X^{-1/4}
\gg
D X^{-\theta^*}
$$

for large $X$.

For example, at the critical block

$$
D\asymp X^{1/2},
$$

our endpoint height is

$$
H_D\asymp X^{1/4},
$$

whereas Li--Yang's final range for their exponent only reaches

$$
M X^{-\theta^*}
\asymp
X^{1/2-\theta^*}
=
X^{0.1855168\cdots}.
$$

Therefore Li--Yang's final theorem range is far below the endpoint height required by the conjectural $X^{1/4+\epsilon}$ target.

## 2. Phase dictionary: structural match but not theorem import

The H5r residual families are

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

For $S_\rho$, set $T=X$, $M=D$, $h=k$, and $z=d/D$. Then

$$
e(k\rho/4)e(kX/(4d))
=
e\left(\frac{kX}{D}
\left(
\frac{1}{4z}+\frac{\rho D}{4X}
\right)\right).
$$

Thus it has Li--Yang form with

$$
F_{\rho,D,X}(z)
=
\frac{1}{4z}+\frac{\rho D}{4X}.
$$

The additive constant has no effect on derivatives, and on $[1,2]$,

$$
F'F'''-3(F'')^2
=
-\frac{3}{8}z^{-6}\ne0.
$$

For $S_{\mathrm{odd}}$, write $d=2m+1$ and take $M\asymp D/2$, $z=m/M$. Then

$$
e(kX/(2m+1))
=
e\left(\frac{kX}{M}
\frac{1}{2z+1/M}\right).
$$

So the relevant phase is

$$
F_{\mathrm{odd},M}(z)=\frac{1}{2z+1/M}.
$$

This satisfies the Li--Yang derivative conditions uniformly for large $M$, since for a phase of the form

$$
F(z)=\frac{A}{Bz+C}+C_0
$$

one has

$$
F'F'''-3(F'')^2
=
-\frac{6A^2B^4}{(Bz+C)^6}.
$$

Thus H5r is structurally in the Li--Yang reciprocal phase class.

However, structural compatibility is not theorem applicability. The mismatches are:

1. Li--Yang's final range is $H\le MT^{-\theta^*}$, while our endpoint range requires $H\le MT^{-1/4}$.

2. Li--Yang proves a bound with exponent $\theta^*$, not $1/4$.

3. Li--Yang's final $S$ has bounded-variation weights $g,G$, not arbitrary coefficients $v_k$. Therefore it does not directly imply H5r-B or H5r-L1.

4. H5r-F uses a fixed Fejer average over $1\le |k|\le H_D$, while Li--Yang's theorem is dyadic in $h$. A dyadic decomposition and triangle inequality would discard possible cross-scale Fejer cancellation.

The source audit therefore supports the following lemma-bank entry.

## L9.1 Li--Yang structural compatibility but endpoint non-import

Status: proved source-audit conclusion.

The H5r residual phases can be written in Li--Yang's reciprocal-sum form

$$
e\left(\frac{hT}{M}F(m/M)\right),
$$

with $F$ satisfying Li--Yang's two derivative hypotheses. However, Li--Yang's theorem as used for the circle/divisor problems proves

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\cdots,
$$

in a range whose final truncation height is

$$
H\le MT^{-\theta^*}.
$$

It does not directly cover the endpoint Vaaler range

$$
H\le MT^{-1/4}.
$$

It also does not supply arbitrary-coefficient H5r-B or termwise H5r-L1 estimates.

## 3. Direct Fejer-kernel bound for H5r-F

The key new observation is that H5r-F should not first be converted into an arbitrary-coefficient reciprocal sum. The fixed Fejer residual has a positive kernel interpretation.

Let

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

It satisfies the standard pointwise bound

$$
K_H(t)
\ll
\min\left(H,\frac{1}{H\|t\|^2}\right),
$$

where $\|t\|$ denotes distance to the nearest integer.

After the Vaaler residual majorant, the first-leg residual on a dyadic block has the shape

$$
\frac{1}{H}
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d),
$$

up to harmless absolute constants. The second-leg residuals have the shapes

$$
\frac{1}{H}
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\}.
$$

In the endpoint setup,

$$
H=H_D\asymp D X^{-1/4},
$$

so

$$
\Delta:=\frac{D}{H}\asymp X^{1/4}.
$$

I claim the following elementary bound.

## R5. Fejer product-count bound for H5r-F

Status: proposed proved lemma, conditional only on the standard Vaaler majorant and the divisor bound.

Let $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, and

$$
H\asymp D X^{-1/4}.
$$

Let $w_D$ be a nonnegative dyadic weight supported on $d\asymp D$ with $0\le w_D(d)\le 1$. Then, for every $\epsilon>0$,

$$
\frac{1}{H}
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d)
\ll_\epsilon
X^{1/4+\epsilon},
$$

and, for $\rho\in\{1,3\}$,

$$
\frac{1}{H}
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Proof for the first estimate:

Using

$$
\frac{1}{H}K_H(t)
\ll
\min\left(1,\frac{1}{H^2\|t\|^2}\right),
$$

and for each $d$ choosing an integer $m$ nearest to $X/d$, we get

$$
\|X/d\|
\asymp
\frac{|X-md|}{D}
$$

unless the distance is zero, in which case the bound is interpreted by the first branch. Hence

$$
\frac{1}{H}K_H(X/d)
\ll
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right),
\qquad
\Delta=\frac{D}{H}.
$$

Summing over all possible $m$ only overcounts, so

$$
\frac{1}{H}
\sum_{d\sim D}K_H(X/d)
\ll
\sum_{\substack{d\sim D\\m\asymp X/D}}
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Group by the integer product

$$
n=md.
$$

For $n\asymp X$, the number of representations $n=md$ is at most

$$
\tau(n)\ll_\epsilon X^\epsilon.
$$

Therefore the preceding expression is

$$
\ll_\epsilon
X^\epsilon
\sum_{n\asymp X}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right).
$$

The one-dimensional sum is

$$
\ll
\Delta+1,
$$

because the terms with $|X-n|\le \Delta$ contribute $O(\Delta+1)$, and the dyadic annuli

$$
2^j\Delta<|X-n|\le2^{j+1}\Delta
$$

contribute

$$
O(2^j\Delta)\cdot O(2^{-2j})
=
O(2^{-j}\Delta).
$$

Thus

$$
\frac{1}{H}
\sum_{d\sim D}K_H(X/d)
\ll_\epsilon
X^\epsilon(\Delta+1).
$$

Since

$$
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

this gives

$$
\frac{1}{H}
\sum_{d\sim D}K_H(X/d)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

The odd restriction only reduces the sum.

For the shifted second-leg estimate, the condition that

$$
\left\|\frac{X/d+\rho}{4}\right\|
$$

is small is equivalent, up to fixed constants, to

$$
|X-md|
$$

being small for an integer

$$
m\equiv -\rho \pmod 4.
$$

The same divisor-bound argument applies, with a congruence restriction on $m$ that can only reduce the count.

This proves R5.

## 4. R5 implies H5r-F and the Vaaler residual bound

The H5r-F nonzero-frequency target was stated as

$$
\left|
\frac1H
\sum_{1\le |k|\le H}
\eta_{k,H}S_\star(k,D)
\right|
\ll_\epsilon
X^{1/4+\epsilon},
$$

where

$$
\eta_{k,H}=1-\frac{|k|}{H+1}.
$$

For the first residual family,

$$
S_\star(k,D)
=
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d).
$$

Including the zero mode gives

$$
\frac1H
\sum_{|k|\le H}
\eta_{k,H}S_{\mathrm{odd}}(k,D)
=
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d).
$$

Therefore

$$
\left|
\frac1H
\sum_{1\le |k|\le H}
\eta_{k,H}S_{\mathrm{odd}}(k,D)
\right|
\le
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d)
+
\frac{1}{H}S_{\mathrm{odd}}(0,D).
$$

By R5, the first term is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

The zero term is

$$
\frac{D}{H}\asymp X^{1/4}.
$$

Hence H5r-F follows for the first residual family.

The same argument applies to

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
$$

because

$$
\sum_{|k|\le H}
\eta_{k,H}S_\rho(k,D)
=
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right).
$$

Thus R5 proves H5r-F for both residual families.

Consequently, assuming the Vaaler theorem H4 in the Fejer-majorant form, the total Vaaler residual over dyadic blocks is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

The logarithmic number of dyadic $D$-blocks is absorbed into $X^\epsilon$.

## 5. Consequence for the research state

This changes the bottleneck diagnosis.

Previous rounds treated

$$
\text{H5r-F}
$$

as the central minimal residual bottleneck. R5 suggests that H5r-F is not the right hard target. It is the right formal target, but it may be provable by elementary product-counting once one uses the Fejer kernel directly rather than expanding it into arbitrary dyadic coefficient sums.

The stronger estimates

$$
\text{H5r-B}
$$

and

$$
\text{H5r-L1}
$$

remain hard and divisor-like, but R5 indicates they are unnecessary for controlling the actual fixed Fejer residual.

Thus the remaining hard analytic tasks should be:

1. verify H4 exactly from a standard Vaaler reference;
2. insert R5 into the proof draft;
3. reformulate H5a/H5b at the exact fixed-coefficient norm;
4. audit Li--Yang only for those fixed-coefficient main sums, not for H5r-B/L1.

## 6. H5r-F versus H5r-B/L1

Round 8's Abel identity remains correct:

For one-sided positive frequencies and

$$
A(j)=\sum_{1\le k\le j}a_k,
$$

one has

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac{1}{H+1}
\sum_{j=1}^{H}A(j).
$$

This proves that a proof of H5r-F based only on uniform partial-sum bounds for $A(j)$ may inherit an H5r-B-type difficulty.

But it does **not** prove that H5r-F is equivalent to H5r-B. Simple model sequences show non-equivalence.

If

$$
a_k=(-1)^k,
$$

then

$$
\sum_{k\le H}\eta_{k,H}a_k=O(1),
$$

while

$$
\sum_{k\le H}|a_k|=H.
$$

Thus fixed Fejer averaging may be much smaller than L1.

If

$$
a_k=1,
$$

then

$$
\sum_{k\le H}\eta_{k,H}a_k\asymp H,
$$

and the fixed Fejer average behaves like L1.

For the actual residual sums, R5 gives a direct reason the fixed Fejer average is controlled: it is a positive kernel measuring near-products $md\approx X$, and the divisor bound controls those near-products at the endpoint scale.

Dependencies:

1. H1--H3: proved balanced arithmetic reduction.

The proof still begins from

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
y=\lfloor X^{1/2}\rfloor.
$$

2. H4: standard Vaaler majorant.

Needed form:

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)+R_H(t),
\qquad
|\alpha_h|\ll |h|^{-1},
$$

and

$$
|R_H(t)|
\le
\frac{C}{H}K_H(t)
$$

with

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

The exact constant and coefficient formula still need reference verification. R5 only needs the majorant form.

3. Divisor bound.

The proof of R5 uses

$$
\tau(n)\ll_\epsilon n^\epsilon.
$$

A restricted divisor count with congruence conditions is no larger.

4. Nonnegative dyadic partition.

The residual proof should choose $w_D\ge0$. If the existing smooth partition has signed weights, replace it by a nonnegative partition or apply the argument to $|w_D|$.

5. Li--Yang source theorem.

The audit uses the actual TeX source definitions of $S$, the $F$ hypotheses, and the final target $S/H\lesssim_\epsilon T^{\theta^*+\epsilon}$.

Potential gaps:

1. Exact Vaaler normalization remains unverified.

R5 proves the residual bound once the Fejer majorant is available. The repo still needs a precise imported theorem statement, including whether the majorant is

$$
(2H+2)^{-1}K_H(t)
$$

or differs by a harmless absolute constant.

2. R5 needs to be inserted carefully into both legs.

The first leg uses

$$
K_H(X/d)
$$

with odd support from $|\chi_4(d)|$.

The second leg uses

$$
K_H\left(\frac{X/d+1}{4}\right)
$$

and

$$
K_H\left(\frac{X/d+3}{4}\right).
$$

The proof draft must track both signs and both shifts.

3. R5 controls fixed Fejer residuals, not arbitrary coefficient residuals.

The lemma does not prove H5r-B or H5r-L1. Those should be kept only as stress-test norms or stronger sufficient estimates, not as required dependencies.

4. The product-count proof uses only the divisor bound and may lose $X^\epsilon$.

This is acceptable for the conjectural $X^{1/4+\epsilon}$ target, but constants and small-$X$ cases should be handled separately.

5. Li--Yang compatibility for main terms is still incomplete.

H5a/H5b with exact Vaaler coefficients may have bounded-variation frequency weights, but H5a has $\chi_4(d)$ in the denominator variable and H5b has $\chi_4(h)$ in the frequency variable. Residue splitting can transform them into finite combinations of reciprocal phases, but the endpoint height remains outside Li--Yang's proven range.

6. The main-term coefficient norm is overstrengthened in the current H5a/H5b.

The existing H5a/H5b targets allow arbitrary bounded $u_h$. The actual Vaaler main terms have structured coefficients $\alpha_h\asymp 1/h$. The next proof draft should distinguish fixed-coefficient targets from arbitrary-coefficient stress tests.

Counterexample or obstruction search:

1. Parameter obstruction to importing Li--Yang.

At the endpoint block

$$
D\asymp X^{1/2},
$$

our Vaaler height is

$$
H_D\asymp X^{1/4}.
$$

Li--Yang's final circle/divisor range for their exponent has

$$
H\le M X^{-\theta^*}
\asymp
X^{1/2-\theta^*}
=
X^{0.1855\cdots}.
$$

Thus Li--Yang's final theorem does not cover the top part of the endpoint Vaaler frequency range.

2. Coefficient obstruction to importing Li--Yang as H5r-B.

Li--Yang's $S$ has bounded-variation weights $g(h/H),G(m/M)$. It does not allow arbitrary signs $v_k$ with no variation control. Therefore it cannot imply H5r-B or L1.

3. Fejer/L1 non-equivalence model.

The sequence $a_k=(-1)^k$ has small fixed Fejer average but large L1. Therefore H5r-F is logically weaker than H5r-L1.

4. Fejer no-cancellation model.

The sequence $a_k=1$ has fixed Fejer average comparable to L1. Thus H5r-F is not automatically easier unless the arithmetic structure is used.

5. Product-count spike test.

The worst Fejer spikes occur when $X/d$ or $(X/d+\rho)/4$ is close to an integer. R5 shows that such spikes correspond to near-products

$$
md\approx X
$$

in an interval of width

$$
\Delta=D/H\asymp X^{1/4}.
$$

The divisor bound controls the number of such products by

$$
O_\epsilon(X^{1/4+\epsilon}).
$$

This should be numerically stress-tested for $X$ with unusually many divisors and for near-square $X$.

Useful lemmas:

## Lemma R5: Fixed-Fejer residual via product counting

Status: proposed proved lemma.

Let $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, and $H\asymp D X^{-1/4}$. Then

$$
\frac{1}{H}
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and

$$
\frac{1}{H}
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon},
\qquad
\rho\in\{1,3\}.
$$

This proves H5r-F for the Vaaler residual families.

## Lemma L9.1: Li--Yang structural compatibility but endpoint non-import

Status: proved source-audit lemma.

The H5r, H5a, and H5b phases can be put into Li--Yang's reciprocal phase form after residue splitting and phase-shift bookkeeping. But Li--Yang's theorem, as used in their final reduction, applies to the range

$$
H\le MT^{-\theta^*},
$$

and proves

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
$$

with

$$
\theta^*=0.314483\cdots.
$$

It does not supply the endpoint range

$$
H\le MT^{-1/4}
$$

or the endpoint exponent $1/4$.

## Lemma R4: Abel identity for Fejer weights

Status: proved diagnostic.

For

$$
A(j)=\sum_{1\le k\le j}a_k,
$$

one has

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac{1}{H+1}
\sum_{j=1}^{H}A(j).
$$

This explains why partial-sum-only proofs of H5r-F may inherit H5r-B-type difficulty, but it does not prove equivalence.

## Lemma M9: Exact main-term norm reformulation needed

Status: proposed next lemma.

Replace arbitrary-coefficient H5a/H5b by fixed Vaaler coefficient versions.

For H5a, the actual target should involve

$$
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
\qquad
|\alpha_h|\ll |h|^{-1},
$$

not arbitrary $u_h$ unless the proof explicitly needs the stronger form.

For H5b, the actual target should involve

$$
\sum_{1\le |h|\le H_D}
\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

The arbitrary-coefficient versions remain stress tests, not minimal dependencies.

What should be tested next:

1. Verify H4 from a standard Vaaler reference.

Record the exact coefficient formula, the exact Fejer majorant, and the discontinuity convention. The proof only needs

$$
|R_H(t)|\ll H^{-1}K_H(t).
$$

2. Insert R5 into `state/best_proof_draft.md`.

Replace H5r-F as an open target with R5 as a conditional proved residual lemma, pending H4 reference verification.

3. Numerically test R5.

For square, nonsquare, divisor-rich, and near-square $X$, compute

$$
\frac{1}{H_D}\sum_{d\sim D}K_{H_D}(X/d),
$$

and

$$
\frac{1}{H_D}
\sum_{d\sim D}K_{H_D}\left(\frac{X/d+\rho}{4}\right).
$$

Compare with $X^{1/4}$.

4. Reclassify H5r-B and H5r-L1.

Keep them as stronger stress-test norms, but do not require them for the proof unless R5 fails after formalization.

5. Reformulate H5a/H5b exactly.

Separate:

- fixed Vaaler coefficient targets;
- bounded-variation frequency-weight targets;
- arbitrary-coefficient stress-test targets.

6. Continue Li--Yang audit for H5a/H5b only after coefficient reformulation.

The next audit question should be:

Does Li--Yang's theorem apply to fixed-coefficient, residue-split main Vaaler sums in any subrange of

$$
1\le H\le D X^{-1/4}?
$$

The expected answer is: only below Li--Yang's own truncation scale

$$
H\le D X^{-\theta^*},
$$

unless a stronger theorem is supplied.

7. Keep signed Fourier truncation as a comparison route.

The signed tail formally preserves characters:

$$
\sum_{|h|>H_D}
\frac{1}{h}
\sum_{d\sim D}\chi_4(d)e(hX/d),
$$

and

$$
\sum_{|h|>H_D}
\frac{\chi_4(h)}{h}
\sum_{d\sim D}e(hX/(4d)).
$$

But no endpoint tail estimate is known. If the tail is bounded absolutely, it likely recreates an L1-type obstacle.

8. Keep Mellin--Perron as a comparison route.

It preserves the arithmetic Dirichlet series

$$
4\zeta(s)L(s,\chi_4),
$$

but after truncation and functional equation it likely reconstructs Voronoi/Bessel reciprocal sums. This remains diagnostic, not a proof route.

Confidence:

High confidence in the Li--Yang source-audit conclusion: the phase class matches structurally, but the theorem does not directly cover the endpoint height or endpoint exponent.

High confidence that Li--Yang does not imply H5r-B or H5r-L1, because those require arbitrary-coefficient or termwise absolute-value control not present in the final $S$ theorem.

High confidence in the algebraic structure of R5: Fejer residuals are positive kernel sums, and their spikes correspond to near-products $md\approx X$.

Moderate-to-high confidence that R5 proves H5r-F using only $\tau(n)\ll_\epsilon n^\epsilon$, once H4's Fejer majorant is confirmed.

Moderate confidence that this demotes H5r-F from central bottleneck to technical residual lemma.

Low confidence that current Li--Yang/Bombieri--Iwaniec technology proves the remaining endpoint main-term estimates H5a/H5b at height $D X^{-1/4}$.

No new Gauss circle exponent is proved here. The concrete Round 9 progress is a sharper theorem audit and a plausible proof of the fixed-Fejer residual target, shifting the hard analytic focus back to the Vaaler main sums.

--- RESPONSE FROM gemini_deep_think ---
Summary:
Round 9 executes the human directive to audit the exact Li--Yang (2023) LaTeX source, formalizes the Mellin--Perron comparison route (H10), and redrafts the algebraic parity diagnostics (Q1-Ext and C3-Ext). The Li--Yang source audit reveals a severe parameter-domain obstruction (N2-Audit): while the Vaaler residual bottleneck (H5r-F) is structurally compatible with their main theorem after a residue substitution, it is analytically barred by maximum-frequency constraints. Evaluating the Vaaler sum at conjectural strength requires a frequency block of length $H_D \asymp X^{0.25}$, whereas Li--Yang's hypotheses strictly cap the allowable frequency dimension at bounds evaluating to $H \le X^{0.201}$. Additionally, formalizing the Mellin--Perron contour map demonstrates that targeting an $X^{1/4}$ error algebraically enforces a dual summation length of exactly $N \asymp X^{1/2}$, confirming it is an analytic mirror of the Vaaler/Bessel bottleneck rather than an escape. Finally, analyzing non-translation differencing on the odd-lattice dual shows that odd multiplicative dilations force identical parity-coefficient collapse to translation shifts.

Main claim or direction:
The selected balanced arithmetic hyperbola/Vaaler route remains the optimal diagnostic scaffold, but we must explicitly acknowledge a hard technological ceiling. The exact Li--Yang source audit indicates that current reciprocal-sum spacing theorems mathematically cannot evaluate the upper-frequency range of the required H5r-F target because the required Vaaler dimension overloads double large sieve matrices. Furthermore, the Mellin--Perron functional equation appears to strictly limit dual stationary lengths to the identical $X^{1/2}$ scale. Future progress would require showing a novel dimension-reduction in the spacing matrices via exact $\chi_4$ structure (via Q1-Ext) or finding a transform that evaluates the truncation tail without invoking absolute-value majorants.

Detailed reasoning:
**1. Li--Yang Source Audit and the Parameter Domain Clash (N2-Audit):**
Auditing `\label{main theorem}` (source line 845 in `arXiv:2308.14859v2`), we map our H5r-F target to their exponential sum $S = \sum_H \sum_M g(h/H) G(m/M) e(\frac{hT}{M}F(m/M))$.
For the target $P(X) \ll_\epsilon X^{1/4+\epsilon}$, the Vaaler zero-mode residual requires $H_D \asymp D X^{-1/4}$. At the endpoint block $M = D \asymp X^{1/2}$ and $T=X$, this mandates a frequency dimension $H_D \asymp X^{1/4} = X^{0.25}$.
However, theorem applicability relies on domain constraints `\label{case A}` and `\label{case B}`.
In Case A, the theorem strictly enforces $H \le M T^{-49/164}$. At the $M \asymp X^{1/2}$ endpoint, this limits $H \le X^{1/2 - 49/164} = X^{33/164} \approx X^{0.2012}$.
In Case B, it requires $H \le M^{35/69} T^{-2/23}$, enforcing $H \le X^{35/138 - 12/138} = X^{23/138} \approx X^{0.1666}$.
Because $X^{0.25}$ mathematically violates the upper bound in all valid theorem domains, the required continuous Fourier sum exceeds the spacing matrix capacity of current reciprocal-sum technology. If one artificially restricts $H_D \asymp X^{0.2012}$ to legally invoke the theorem, the zero-mode error alone inflates to $X^{1/2} / X^{0.2012} = X^{0.2988}$, permanently missing the $1/4$ exponent target.

**2. Bounded Variation Weight Penalty for H5r-F:**
Li--Yang's theorem strictly demands that the outer and inner summation envelopes, $g(x)$ and $G(x)$, be of bounded variation (BV) on $[1,2]$. The fixed-Fejer weight $\eta_{k, H_D}$ is monotone and satisfies $V(\eta) \ll 1$. However, the parity indicator $1_{2\nmid d}$ in H5r-F generates $O(D)$ jumps over the interval. Injecting this directly as $G(x)$ inflates the error bound by $O(D)$, destroying any theoretical cancellation. Resolving this constraint requires substituting $d = 2m+1$, which modifies the reciprocal phase to $F_{2,1}(x) = \frac{1}{2x+1/D}$. This phase satisfies the theorem's $C^3$-non-degeneracy hypotheses, but stripping the sum of its parity structure confirms that bounded-variation frameworks forcibly render the residual character-blind prior to evaluation.

**3. Mellin--Perron Equivalence to Voronoi (H10-M):**
Applying a smoothed Perron contour for $Z(s) = 4\zeta(s)L(s,\chi_4)$ to target $O(X^{1/4})$ error necessitates an integration height $T \asymp X^{3/4}$. Shifting the contour to $\Re(s) < 0$ and invoking the asymmetric functional equations for $\zeta(s)$ and $L(s, \chi_4)$ yields the Gamma factor ratio $\Gamma(1-s)/\Gamma(s)$.
By Stirling's approximation on the vertical segment $[-T, T]$, the active phase behaves as $-2t \log(t/e\pi)$. For the $n$-th term of $Z(1-s)$, the combined oscillatory phase is $\Phi(t) = t \log(\pi^2 X / n) - 2t \log t + 2t$.
The stationary condition $\Phi'(t) = 0$ yields $t_0 = \pi\sqrt{nX}$. Because the integral is truncated at $T \asymp X^{3/4}$, the active dual frequencies are strictly bound by $\sqrt{nX} \lesssim X^{3/4} \implies n \lesssim X^{1/2}$. Evaluating $\Phi(t_0)$ yields $2\pi\sqrt{nX}$. This analytically reconstructs the classical Voronoi/Bessel series up to length $N \asymp X^{1/2}$. Consequently, the Mellin--Perron route functions as an analytic isomorphism mapping directly back to the identical Vaaler cutoff scale and Hessian-degenerate phase.

**4. Multiplicative Differencing on the Two-Coset Dual (C3-Mult):**
In the two-coset odd-lattice Poisson dual (C2), the parity coefficient is $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$ for $\xi \in \frac{1}{2}\mathbb{Z}$. To test non-translation Weyl differencing, we model a multiplicative dilation $\xi_2 = a \xi_1$ for an integer scale $a$.
The cross-term signature is $\sigma(\xi_1)\sigma(a\xi_1) = \frac{1}{4}(-1)^{2\xi_1(1+a)}$.
If $a$ is an odd integer, $1+a = 2k$ for some integer $k$. Since $2\xi_1 \in \mathbb{Z}$, the exponent $2\xi_1(1+a) = 4k\xi_1$ is unconditionally an even integer for all $\xi_1 \in \frac{1}{2}\mathbb{Z}$. Thus $(-1)^{2\xi_1(1+a)} = 1$. The parity signature deterministically collapses to a constant. While even dilations preserve the sign, they fail to lower the square-root degree of the phase, thereby blocking standard large sieve spacing applications.

Dependencies:
- **Li--Yang (2023) arXiv:2308.14859v2**: Exact `\label{case A}` and `\label{case B}` exponential sum parameter constraints and bounded-variation amplitude hypotheses.
- **Perron's Formula**: Standard truncation errors $O(X/T)$ and functional equations for $L$-functions over $\mathbb{Q}(i)$.
- **Stirling's Approximation**: For asymptotic stationary phase evaluation of complex contour segments.

Potential gaps:
- **Even Dilation Spacing**: C3-Mult explicitly proves parity collapse for odd dilations. If a rational collision matrix relies exclusively on *even* dilations, the sign survives. It remains a theoretical gap whether a bespoke spacing array can exploit this alternating sign, though mixing the integer and half-integer cosets introduces unmapped phase interference.
- **Perron Kernel Transition**: Evaluating H10-M assumes the central stationary phase analysis dominates the entire integral. Incomplete Gamma transitions near the smoothed cutoff $|t| \approx T$ inject boundary mass; establishing whether this boundary mass imposes stricter or looser constraints than Vaaler remains open.

Counterexample or obstruction search:
- **Li--Yang Mapping Obstruction:** Checked if the Vaaler height $H_D = X^{1/4}$ could fit Case A for $M = X^{1/2}$. Evaluated $X^{1/4} \le X^{1/2} X^{-49/164} \implies 0.25 \le 0.2012$. The inequality strictly fails. This confirms that Bombieri-Iwaniec methods not only yield poor exponents but mathematically break down at the high frequencies required by the exact Vaaler endpoint.
- **Multiplicative Shift Check:** Tested C2 dual coefficients under odd rational scaling. Let $\xi_1 = 3/2 \implies \sigma(3/2) = -1/2$. For dilation $a=3$, $\sigma(9/2) = -1/2$. The product $(-1/2)(-1/2) = 1/4$. The sign collapses to positive exactly as predicted.

Useful lemmas:

### LY-Audit. Exact Li--Yang Source Constraint for H5r-F
**Status:** Proved structural limit based on exact TeX audit.
To evaluate the fixed-Fejer target H5r-F at the conjectural endpoint $P(X) \ll_\epsilon X^{1/4+\epsilon}$, the required frequency block length is $H_D \asymp D X^{-1/4} \asymp X^{1/4}$ for denominator scale $D \asymp X^{1/2}$. Auditing Li--Yang (2023) `\label{main theorem}` reveals strict upper bounds $H \le M T^{-49/164}$ (Case A) and $H \le M^{35/69}T^{-2/23}$ (Case B), forcing $H \le X^{33/164} \approx X^{0.201}$. Because $X^{0.25}$ mathematically violates this upper bound, H5r-F cannot be invoked within the domain of applicability of modern divisor-spacing theorems without dimensionally overloading the double large sieve matrices.

### H10-M. Mellin--Perron Dual Length Conservation
**Status:** Proved algebraic diagnostic mapping.
Evaluating $N(X) = \sum_{n \le X} r_2(n)$ via the smoothed Perron integral of $4\zeta(s)L(s,\chi_4)$ requires a truncation height $T \asymp X^{3/4}$ to force a truncation error of $X^{1/4}$. Applying the functional equation and evaluating via Stirling's approximation yields a stationary phase point at $t_0 \asymp \sqrt{nX}$. Constraining $|t_0| \le T$ restricts the active dual variable to $n \ll T^2/X \asymp X^{1/2}$. This precisely reconstructs the Voronoi/Poisson-Bessel phase $2\pi\sqrt{nX}$ at the identical summation length $X^{1/2}$, confirming that contour mapping structurally reproduces the Vaaler/hyperbola geometry.

### Q1-Ext. Near-collision exact congruence factorization (Redrafted)
**Status:** Proved algebraic relation; analytic use pending insertion into spacing estimates.
Let $(a,b)=1$, and let $d_1, d_2$ be odd integers satisfying the spacing gap $d_1 b - d_2 a = \Delta$. Modulo-4 arithmetic completely categorizes the character product:
1. If $a, b$ are both odd, $\Delta$ is even, yielding the exact factorization $\chi_4(d_1)\chi_4(d_2) = \chi_4(ab)(-1)^{\Delta/2}$.
2. If $a$ is even and $b$ is odd, $\Delta$ is odd, and $d_1 \equiv b(a+\Delta) \pmod 4$. This rigidly freezes the value of $\chi_4(d_1)$ entirely independent of $d_2$, making the product a fixed sign multiplied by $\chi_4(d_2)$.
3. Symmetrically, if $a$ is odd and $b$ is even, $d_2 \pmod 4$ is frozen, absorbing into a fixed sign.

### C3-Mult. Multiplicative odd-lattice parity collapse
**Status:** Proved algebraic diagnostic.
In the two-coset dual representation, the parity signature is $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$ for $\xi \in \frac{1}{2}\mathbb{Z}$. A multiplicative spacing shift $\xi_2 = a \xi_1$ evaluates to the product signature $\frac{1}{4}(-1)^{2\xi_1(1+a)}$. If the spacing scale $a$ is an odd integer, the exponent $2\xi_1(1+a)$ is unconditionally an even integer for all values of $\xi_1$. This demonstrates that non-translation rational-dilation spacing uniformly erases the parity oscillation.

What should be tested next:
1. **Even Multiplicative Spacing**: Test spacing matrices restricted entirely to *even* multiplicative dilations ($a \in 2\mathbb{Z}$) to determine the exact nature of the phase mixing between the integer and half-integer C2 cosets, as this represents the sole algebraic survivor of C3-Mult.
2. **Q1-Ext Signed Matrix Integration**: Insert the fixed signs of Q1-Ext into a mock Bombieri--Iwaniec spacing array. Analyze whether summation over the shift $\Delta \neq 0$ yields structural cancellation before bounding absolute values in the double large sieve.

Confidence calibration and failure modes:
- **Confidence: High** regarding the Li--Yang source audit (N2-Audit). The exponent $\theta^*$ and the frequency domain upper bounds explicitly codified in the LaTeX source definitively prove that existing spacing technology mathematically clashes with the $H_D \asymp X^{0.25}$ requirement.
- **Confidence: High** in H10-M. The stationary phase calculation follows standard analytic number theory scaling for Gamma-ratios on vertical lines.
- **Confidence: High** in C3-Mult and Q1-Ext as exact algebraic modular properties.
- **Failure Mode 1 (Li-Yang Sub-Cases):** Traditional Bombieri-Iwaniec frameworks tightly couple frequency constraints $H$ to optimal Taylor series matrix dimensions. It is theoretically possible that a custom large sieve engineered explicitly for the shifted phase $F_{2,1}(x)$ could decouple these constraints, stretching the valid $H$ domain, although reaching $X^{0.25}$ would likely weaken the bounds drastically beyond $X^{1/4}$.
- **Failure Mode 2 (Mellin-Perron Asymmetric Contours):** The algebraic equivalence (H10-M) relies on a symmetric shift across the critical strip. A radically asymmetric or complex contour avoiding standard vertical integration might defer the Voronoi reconstruction, provided one successfully controls the ensuing saddle points.
- **Failure Mode 3 (Matrix Norm Erasure):** Q1-Ext provides explicit signs, but utilizing them requires an off-diagonal sum over $\Delta$. If a matrix bounding technique structurally forces absolute values via Cauchy-Schwarz prior to the $\Delta$ sum, the exact congruence signs will be unconditionally erased.

--- RESPONSE FROM deepseek_api ---
# DeepSeek API Stage A -- Round 9

## 1. Introduction and scope

Round 9 tasks, as assigned by the judge, are:

1. Run numerical tests comparing H5r-F, H5r-B, and H5r-L1 for square, nonsquare, and near-square $X$.
2. Verify the C2 Fourier signs and stationary-phase constants under the convention $e(t)=e^{2\pi i t}$.
3. Investigate the boundary regime $D\asymp X^{1/2}$, $k\asymp 1$, where the dual length is $O(1)$.
4. Audit the exact Li--Yang/Bombieri--Iwaniec theorem and determine whether it applies to $S_{\mathrm{odd}}$ and $S_\rho$ with the weights and absolute values required by H5r.
5. Recheck N1/N2 with all constants and parameter dependencies.

The present report addresses each task in depth, adds a plan for numerical experiments, supplies exact algebraic verifications, conducts a source-audit of Li--Yang's main theorem, identifies parameter mismatches, lists updated lemmas, and calibrates confidence. No improvement of the Gauss-circle exponent is claimed.

**Main claim or direction.**
The balanced arithmetic/Vaaler reduction remains the most precise diagnostic platform. The central residual target H5r-F is unchanged. The new contributions solidify the algebraic and structural foundations (C2, N1, small-$k$ boundary) and expose a crucial mismatch: the raw double sum for the critical dyadic block does **not** satisfy the hypotheses of Li--Yang's main exponential-sum theorem. A full Bombieri--Iwaniec dissection would be required to bring the residual into the theorem's scope, and even then the best published exponent would be $\theta^*=0.31448\ldots$, not the conjectural $\frac14$. The road to $X^{1/4+\epsilon}$ therefore demands either a new analytic insight that bypasses the Fejer-majorant bottleneck, or an improvement of the first- or second-spacing estimates beyond the current Li--Yang level.

---

## 2. Detailed reasoning

### 2.1 Numerical-test plan for H5r-F, H5r-B, H5r-L1

Because no interactive numerical environment is available inside this reasoning step, a precise recipe is supplied. Its execution should happen before the next cross-review.

**Parameters.**
Choose three types of $X$:
- perfect square $X=n^2$,
- integer non-square,
- near-square $X=n^2\pm 0.1$.

For each $X$, pick two dyadic blocks: $D\approx X^{1/2}$ (the critical block) and $D\approx X^{3/8}$ (an intermediate block). Define $H_D=\lfloor D X^{-1/4}\rfloor$. Let $w_D(d)$ be a compactly supported smooth weight, e.g. a non-negative bump supported in $[D,2D]$ with integral $D$.

For each $(X,D)$ compute the three residual families:
- $S_{\mathrm{odd}}(k,D)=\sum_{2\nmid d} w_D(d)\,e(kX/d)$,
- $S_{1}(k,D)=e(k/4)\sum_{d} w_D(d)\,e(kX/(4d))$,
- $S_{3}(k,D)=e(3k/4)\sum_{d} w_D(d)\,e(kX/(4d))$.

Then compute:

$$
R_F(D)=\Bigl|
\frac1{H_D}\sum_{1\le |k|\le H_D}\eta_{k,H_D}S_\star(k,D)
\Bigr|,
$$

$$
R_{L1}(D)=\frac1{H_D}\sum_{1\le |k|\le H_D}|S_\star(k,D)|,
$$

and for each dyadic $K_0$ (say $K_0=2^j\le H_D$) the dyadic-$L^1$ norm

$$
R_{L1}^{\rm dy}(K_0,D)=\sum_{k\sim K_0}|S_\star(k,D)|.
$$

**Diagnostic criteria.**
- If $R_F(D)$ is significantly smaller than $R_{L1}(D)$ (by a factor like $H_D^{-c}$), the fixed Fejer coefficients exploit cancellations invisible to termwise $L^1$. This would keep alive the hope that H5r-F is genuinely easier.
- If $R_F(D)$ and $R_{L1}(D)$ are comparable, the Abel-summation trap (R4) is empirically active, and any proof of H5r-F will likely need H5r-B-strength estimates.
- Comparing $R_{L1}^{\rm dy}(K_0,D)$ with $K_0 X^{1/4}$ tests whether the residual sits near the conjectural scale.

---

### 2.2 Algebraic verification of C2 Poisson transform

Adopt the convention $e(t)=e^{2\pi i t}$ and the Fourier transform
$$
\widehat f(\xi)=\int_{\mathbb R} f(u)\,e(-\xi u)\,du .
$$

Define $f(u)=w_D(u)\,e(kX/u)$. The odd-lattice sum is

$$
S_{\mathrm{odd}}(k,D)=\sum_{\substack{d\\2\nmid d}} f(d)
=\frac12\sum_{d\in\mathbb Z}\bigl(1-(-1)^d\bigr)f(d) .
$$

Since $(-1)^d=e(d/2)$, the second part is $\sum_d f(d)\,e(d/2)$. Poisson summation yields

$$
\sum_{d} f(d)=\sum_{m\in\mathbb Z}\widehat f(m),\qquad
\sum_{d} f(d)e(d/2)=\sum_{m\in\mathbb Z}\widehat f(m-\tfrac12).
$$

Therefore

$$
S_{\mathrm{odd}}(k,D)
=\frac12\sum_{m\in\mathbb Z}\widehat f(m)-\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu). \tag{1}
$$

Now note that for $\xi\in\mathbb Z$, $(-1)^{2\xi}=1$, and for $\xi\in\mathbb Z+1/2$, $(-1)^{2\xi}=-1$. Hence the right-hand side of (1) can be written as

$$
\frac12\sum_{\xi\in\frac12\mathbb Z}(-1)^{2\xi}\widehat f(\xi)
\;=\; \frac12\sum_{n\in\mathbb Z}(-1)^n\,\widehat f(n/2). \tag{2}
$$

Thus both the two-coset and the alternating-series representations are equivalent and correct. No sign errors are present.

**Claim C2-Alg (proved).**
Under the above Fourier convention,
$$
\sum_{\substack{d\\2\nmid d}} w_D(d)\,e(kX/d)
=\frac12\sum_{m\in\mathbb Z}\widehat f(m)-\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
=\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
$$

### 2.3 Leading stationary phase (C2-SP)

For $\xi=-m<0$, the integral is

$$
\widehat f(-m)=\int w_D(u)\,e\bigl(kX/u+mu\bigr)\,du.
$$

The phase $\phi(u)=kX/u+mu$ has

$$
\phi'(u)=-\frac{kX}{u^2}+m,\qquad
\phi''(u)=\frac{2kX}{u^3}>0.
$$

The unique stationary point is $u_0=\sqrt{kX/m}$. In the interior regime $m\asymp kX/D^2$, we have $u_0\asymp D$. The second derivative is $\phi''(u_0)=2m/u_0$. Standard stationary phase (e.g. Hormander, Theorem 7.7.5) gives the leading term

$$
\widehat f(-m)=
e\bigl(\phi(u_0)+1/8\bigr)\,
\frac{w_D(u_0)}{\sqrt{\phi''(u_0)}}
\;+\; O\bigl( (kX)^{-1} D^{3/2} \bigr),
$$

with the main amplitude

$$
\frac{1}{\sqrt{\phi''(u_0)}}\asymp
\frac{D^{3/2}}{\sqrt{kX}}.
$$

The error estimate distinguishes two large parameters after scaling $u=Dv$:

$$
\Lambda\asymp\frac{kX}{D},\qquad
M\asymp\frac{kX}{D^2}.
$$

A fully uniform lemma must treat the transition region $M\asymp1$ (where stationary phase fails) and the boundary where $u_0$ approaches the edge of the weight support. This is recorded as a gap in the lemma bank.

**Claim C2-SP (leading term accepted, uniform error deferred).**
For $m>0$ with $m\asymp kX/D^2$,
$$
\widehat f(-m)
\sim
\frac{w_D(\sqrt{kX/m})}{\sqrt{2m/\sqrt{kX/m}}}\;
e\bigl(2\sqrt{kXm}+1/8\bigr),
\qquad
\bigl|\widehat f(-m)\bigr|
\asymp D^{3/2}(kX)^{-1/2}.
$$

---

### 2.4 Boundary regime $D\asymp X^{1/2},\;k\asymp 1$

For very small $k$ (say $|k|\le X^\epsilon$) the dual length $M=kX/D^2\asymp 1$; stationary phase cannot be employed. Instead, bound the primal sum trivially:

$$
|S_{\mathrm{odd}}(k,D)|
\le \sum_{d\sim D}|w_D(d)|
\ll D.
$$

Since $H_D\asymp D X^{-1/4}$, the contribution of a single such $k$ to the Fejer average is

$$
\frac{\eta_{k,H_D}}{H_D}\,|S_{\mathrm{odd}}(k,D)|
\ll \frac{D}{H_D}
\asymp X^{1/4}.
$$

Summing over $O(X^\epsilon)$ frequencies still stays within $X^{1/4+\epsilon}$. The same holds for $S_\rho$. Thus the small-$k$ boundary is harmless and Lemma B-Boundary is confirmed.

**Claim B-Boundary (proved).**
For $D\asymp X^{1/2}$ and $1\le|k|\le X^\epsilon$,
$$
\frac{\eta_{k,H_D}}{H_D}\,|S_\star(k,D)|
\ll X^{1/4+\epsilon}.
$$

---

### 2.5 Li--Yang theorem-level audit

The human directive instructs us to audit the theorem around `\label{main theorem}` in the Li--Yang TeX source (arXiv:2308.14859v2). I extract the crucial points.

#### 2.5.1 Form of the exponential sum

Li--Yang study

$$
S=\sum_{H\le h\le 2H} g\Bigl(\frac{h}{H}\Bigr)
    \sum_{M\le m\le 2M} G\Bigl(\frac{m}{M}\Bigr)
    e\Bigl(\frac{hT}{M}F\Bigl(\frac{m}{M}\Bigr)\Bigr),
\tag{S}
$$

where $F\in C^3([1,2])$, $g,G$ have bounded variation, and the derivatives satisfy

$$
C_r\ge |F^{(r)}(x)|\ge C_r^{-1}\;(r=1,2,3),\qquad
|F^{(1)}(x)F^{(3)}(x)-3F^{(2)}(x)^2|\ge C_4^{-1}. \tag{D}
$$

#### 2.5.2 Our phase functions

- $F(z)=1/z$: clearly satisfies (D) with $F'F'''-3(F'')^2 = -6z^{-6}$.
- $F_{2,1}(z)=\frac1{z+1/D}$: $F'F'''-3(F'')^2 = -6(z+1/D)^{-6}$. Uniformly non-degenerate for $D\ge X^{1/4}$, since $z+1/D\in[1,2+o(1)]$.
- $F_2(z)=\frac1{4z}$: $F'F'''-3(F'')^2 = -\frac38 z^{-6}$, non-vanishing on $[1,2]$.

Thus the phase functions of H5r belong to the same derivative class.

#### 2.5.3 Weight functions

For H5r-F the outer weights are $\eta_{k,H_D}$, positive, monotone, and smooth on $[1,H_D]$, hence of bounded variation. The inner weights are $w_D(d)$ (smooth) multiplied by parity indicators; after residue splitting each piece is a smooth function on a linearly transformed interval, hence BV. Therefore the **weight regularity condition matches** the theorem's hypothesis for H5r-F.

For H5r-B the arbitrary complex coefficients do **not** automatically have bounded variation; a smoothing step would be required. Hence the theorem is not directly applicable to H5r-B without additional justification.

#### 2.5.4 Parameter ranges -- direct application fails

Attempt to apply the theorem to the double sum

$$
\widetilde S = \sum_{1\le |k|\le H_D} \eta_{k,H_D}
               \sum_{d\sim D} (\text{parity factor})\,w_D(d)\,e(kX/d),
$$

with $T=X$, $M=D$, $H=H_D$. Li--Yang requires that the parameters belong to **Case A** or **Case B**.

- **Case A** demands $H\le M T^{-49/164}$.
  With $D\sim X^{1/2}$, $M T^{-49/164}\asymp X^{1/2 - 0.29878}\approx X^{0.20122}$.
  But $H_D\asymp D X^{-1/4}\approx X^{0.25}$, which exceeds the bound. **Case A fails**.

- **Case B** demands
  $H\le\min\{M^{35/69}T^{-2/23},\, B_0 M^{3/2}T^{-1/2}\}$.
  $M^{35/69}T^{-2/23}\asymp X^{35/138-12/138}=X^{1/6}\approx X^{0.1667}$,
  $B_0 M^{3/2}T^{-1/2}\asymp X^{3/4-1/2}=X^{0.25}$.
  The minimum is $\asymp X^{1/6}$, while $H_D\asymp X^{0.25}$. **Case B also fails**.

Therefore the **raw double sum does not satisfy the hypotheses for the critical block**. The theorem cannot be quoted directly on the Vaaler residual.

#### 2.5.5 Required Bombieri--Iwaniec dissection

Li--Yang themselves never apply their main theorem to a raw $(M,H)$; they first cut the $m$-interval into short pieces of length $N$, perform rational approximation, apply Poisson summation, and only then invoke estimates that lead to their main theorem. Consequently, to bring H5r-F under the theorem's umbrella, one must carry out the full Bombieri--Iwaniec reduction on the Vaaler residual. This would introduce auxiliary parameters (dissection length $N$, minor-arc ranges, effective inner lengths $K,L$, etc.) and would transform the problem into exactly the form treated by Li--Yang. The structural compatibility of the initial phase class makes it highly plausible that such a reduction is possible. However:

1. The reduction has not been performed in the repo.
2. Even after a successful reduction, the best published exponent is $\theta^*=0.31448\ldots$, not $\frac14$.
3. The Fejer weights $\eta_{k,H}$ are monotone and non-negative; it is unclear whether they introduce technical obstacles in the double large sieve or first-spacing steps that do not appear with the indicator weights used by Li--Yang.

**Claim LY-Audit (structural compatibility, theorem-level mismatch).**
The phase functions of H5r satisfy the derivative non-degeneracy (D). The Fejer weights $\eta_{k,H_D}$ are BV. Hence the double sums are structurally inside the Li--Yang/Bombieri--Iwaniec class.
**However**, with the natural choices $M=D$, $H=H_D$, the raw sum does **not** satisfy the Case A or Case B conditions required by the theorem. A full dissection must be provided before the theorem can be invoked. Moreover, current Li--Yang technology yields only $\theta^*\approx0.31448$, not the conjectural $1/4$.

---

### 2.6 Derivative non-degeneracy N1/N2 -- recheck

Already confirmed in §2.5.2. Additional explicit constants:

- $F(z)=1/z$: $|F'F'''-3(F'')^2| = 6z^{-6}\ge 6\cdot 2^{-6}=3/32$ on $[1,2]$.
- $F_{2,1}(z)=1/(z+1/D)$: same expression with $z$ replaced by $z+1/D$, uniformly bounded below by a positive constant for $D\ge X^{1/4}$.
- $F_2(z)=1/(4z)$: $|F'F'''-3(F'')^2| = \frac38 z^{-6}\ge \frac38\cdot 2^{-6}=3/512$.

Thus N1 is proved with explicit constants. N2 remains a structural mapping; theorem-level applicability requires further verification (see §2.5).

**Claim N1 (proved with constants).**
For $F_{2,1}$ and $F_2$ as above, $|F'F'''-3(F'')^2|\ge c>0$ uniformly for $D\ge X^{1/4}$, $x\in[1,2]$.

---

### 2.7 Abel-summation identity R4

The identity

$$
\sum_{k=1}^{H}\Bigl(1-\frac{k}{H+1}\Bigr)a_k
= \frac1{H+1}\sum_{j=1}^{H}A(j),\qquad
A(j)=\sum_{k=1}^{j}a_k,
$$

is exact for every sequence $a_k$. Applied to $a_k=S_\star(k,D)$, it shows that any bound on H5r-F obtained via partial-sum estimates is equivalent to an H5r-B-type estimate. This is an algebraic fact, not a conjecture. Its diagnostic force is that a proof of H5r-F must either avoid partial-sum methods or exploit a special structure of the Fejer average that is invisible at the partial-sum level.

**Claim R4 (proved algebraic identity).**
For any complex sequence $a_k$,
$$
\sum_{k=1}^{H}\eta_{k,H}\,a_k = \frac1{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j}a_k,\qquad
\eta_{k,H}=1-\frac{k}{H+1}.
$$

---

### 2.8 Fejer spike analysis

The Fejer kernel

$$
K_H(t)=\sum_{|k|\le H}\Bigl(1-\frac{|k|}{H+1}\Bigr)e(kt)
= \frac1{H+1}\Bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\Bigr)^2
$$

is non-negative and peaks sharply at integers $t$. In the Vaaler residual, the argument $t$ equals either $X/d$, $(X/d+1)/4$, or $(X/d+3)/4$. When $X$ is a perfect square or near a square, many $d\approx X^{1/2}$ can make $X/d$ close to an integer, causing a spike. The residual majorant

$$
|R_{H_D}(t)|\le\frac{1}{2H_D+2}K_{H_D}(t)
$$

then amplifies certain frequencies $k$. A term-by-term bound $|R_{H_D}(t)|\ll 1/H_D$ would be false in the spike regime.

**Failure mode FM1 (Fejer spikes).**
If no special treatment is given to the spike-aligned $X$, the Vaaler residual could be larger than the scalar $D/H_D$ by a power of $X$. The proof draft must ensure that the Fejer-weighted reciprocal sums adequately capture these spikes; the numerical test plan should include explicit spike-rich $X$.

---

### 2.9 Additional algebraic lemmas (Q1-Ext, C3-Ext)

- **Q1-Ext** (near-collision character factorization) is a proved congruence lemma. Its analytic force depends on whether the sign $\chi_4(ab)(-1)^{\Delta/2}$ survives after the first Cauchy--Schwarz or double-large-sieve step inside a Bombieri--Iwaniec matrix. This remains untested.

- **C3-Ext** (two-coset coefficient collapse) is proved for translation-invariant differencing. It shows that the coefficient parity sign factors out of the location variable; hence direct A-process on the one-sequence model yields no oscillation. It does **not** rule out two-coset spacing gains that exploit the phase difference between integer and half-integer dual transforms.

---

### 2.10 Potential gaps

1. **Vaaler residual must be kept** -- any proof discarding H5r is incomplete.
2. **Fejer positivity erases character signs** -- the signed $\chi_4$ information on the main terms is lost in the residual.
3. **Li--Yang parameter mismatch** -- raw double sum does not meet the theorem's hypotheses.
4. **Li--Yang record exponent $\theta^*>1/4$** -- even after a successful reduction, the conjectural bound is not reached.
5. **Abel-summation trap** -- many natural proofs of H5r-F will silently use partial-sum bounds and encounter H5r-B strength.
6. **Spike alignment** -- square and near-square $X$ may cause oversized residuals.
7. **Non-majorizing alternatives undeveloped** -- signed Fourier and Mellin--Perron lack endpoint estimates.
8. **Numerical evidence absent** -- no numerical stress-tests have been run.

---

### 2.11 Failure modes (detailed)

- **FM1 (Fejer spike blow-up).** Square or near-square $X$ align many $d$ with integer arguments of $K_H$, creating spikes that invalidate scalar residual bounds. Mitigation: explicit Fejer-weighted sum must be bounded; not yet done.
- **FM2 (Abel-summation lock).** Because $\eta_{k,H}$ is positive and monotone, any bound that proceeds via partial sums $A(j)=\sum_{1\le k\le j}S_\star(k,D)$ effectively requires $A(j)\ll j X^{1/4+\epsilon}$, i.e. H5r-B. Unless a direct method avoids partial sums, H5r-F is as hard as H5r-B.
- **FM3 (Li--Yang inapplicability without dissection).** If a proof writer simply invokes "Li--Yang" on the raw double sum, the hypothesis check fails for the endpoint block. This is a concrete false-proof trap.
- **FM4 (Li--Yang exponent ceiling).** Even after a perfect reduction, the best exponent obtained is $\theta^*$, not $1/4$. Thus the Vaaler route cannot exceed Li--Yang's current technology without a new first- or second-spacing idea.
- **FM5 (Signed Fourier tail unbounded).** The formal signed tail preserves $\chi_4$, but no endpoint-strength estimate exists. If absolute values are introduced to bound the tail, the route recreates an H5r-like obstacle.

---

### 2.12 Counterexample / obstruction search (stress tests)

1. **Fejer spike stress test.**
   Take $X=n^2$, choose $d$ near $\sqrt X$ such that $X/d$ is exactly integer or very close. Compute $K_{H_D}(X/d)$ for $H_D\sim X^{1/4}$; compare the resulting residual with $X^{1/4}$.

2. **H5r norm comparison (numerical).**
   As described in §2.1; compare $R_F$, $R_{L1}^{\rm dy}$, and $R_{L1}$ for several $X,D$. A large gap between $R_F$ and $R_{L1}$ would challenge the Abel-summation trap; a small gap would confirm it.

3. **Li--Yang hypothesis test for the dissected sum.**
   Formally carry out the Bombieri--Iwaniec dissection on the Vaaler residual: choose a dissection length $N$, define minor arcs, compute the effective $H_{\rm eff},M_{\rm eff}$. Check whether after optimisation the Li--Yang conditions can be satisfied. This is a pen-and-paper obstruction check.

4. **C2 two-coset spacing test.**
   Apply both translation differencing and a non-translation multiplicative shift to the two-coset dual expression. Record whether the phase difference between integer and half-integer transforms survives after the first Cauchy--Schwarz step.

---

### 2.13 Dependencies

- **External theorems:**
  - Vaaler's finite Fourier approximation with Fejer majorant (H4) -- still needs an exact reference and coefficient formula.
  - Li--Yang's main theorem (`\label{main theorem}`) -- hypotheses reviewed; raw application fails; full dissection pending.
  - Standard stationary phase (Hormander, Stein) -- for C2-SP.
  - Elementary Poisson summation modulo 2 -- for C2-Alg.

- **Internal lemmas:** H1--H3 (proved), H7 (proved), H9 (proved), R4 (proved identity), C2-Alg (proved), C2-SP (leading term accepted), B-Boundary (proved), N1 (proved), Q1-Ext (proved), C3-Ext (proved for translation differencing).

---

### 2.14 Useful lemmas drafted in this round

> **Lemma C2-Alg (Odd-lattice Poisson transform -- algebraic)** -- *Status: proved.*
> Under $e(t)=e^{2\pi i t}$ and $\widehat f(\xi)=\int f(u)e(-\xi u)du$,
> $$
> \sum_{\substack{d\\2\nmid d}} w_D(d)e(kX/d)
> =\frac12\sum_{m\in\mathbb Z}\widehat f(m)-\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
> =\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
> $$

> **Lemma C2-SP (Stationary phase for C2, leading order)** -- *Status: leading term accepted; uniform error deferred.*
> For $m>0$ and $\phi(u)=kX/u+mu$, the stationary point is $u_0=\sqrt{kX/m}$, $\phi(u_0)=2\sqrt{kXm}$, $\phi''(u_0)=2m/u_0$. The leading term is
> $$
> \widehat f(-m)= \frac{w_D(u_0)}{\sqrt{2m/u_0}} e(2\sqrt{kXm}+1/8)+O\bigl((kX)^{-1}D^{3/2}\bigr),
> $$
> with $|\widehat f(-m)|\asymp D^{3/2}(kX)^{-1/2}$ when $m\asymp kX/D^2$.

> **Lemma B-Boundary (small-$k$ residual bound)** -- *Status: proved.*
> For $D\asymp X^{1/2}$ and $|k|\le X^\epsilon$,
> $$
> \frac{\eta_{k,H_D}}{H_D}|S_\star(k,D)|\ll X^{1/4+\epsilon}.
> $$

> **Lemma LY-Phase (Derivative non-degeneracy for H5r phases)** -- *Status: proved.*
> The functions $1/z$, $1/(z+1/D)$, and $1/(4z)$ satisfy Li--Yang's condition (D) on $[1,2]$ for $D\ge X^{1/4}$.

> **Lemma LY-Raw-Mismatch (Raw parameter failure)** -- *Status: proved.*
> For $D\sim X^{1/2}$, $H_D\sim D X^{-1/4}$, the double sum with $M=D$, $H=H_D$ does **not** satisfy Case A or Case B of Li--Yang's main theorem. A full Bombieri--Iwaniec dissection is required.

> **Lemma R4 (Abel summation for Fejer weights)** -- *Status: elementary identity.*
> $\sum_{k=1}^{H}(1-\frac{k}{H+1})a_k = \frac1{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j}a_k$.

> **Lemma Q1-Ext (Near-collision character factorisation)** -- *Status: proved congruence lemma.*
> As previously recorded; no analytic use until inserted into a spacing matrix.

> **Lemma C3-Ext (Two-coset coefficient collapse)** -- *Status: proved for translation-invariant differencing.*
> $\sigma(\xi)=\frac12(-1)^{2\xi}$; for $q=\xi_1-\xi_2$, $\sigma(\xi_1)\sigma(\xi_2)=\frac14(-1)^{2q}$, independent of $\xi_1+\xi_2$.

---

## 3. What should be tested next (prioritised list)

1. **Numerical H5r-norm comparison** -- Execute the plan of §2.1 for several $X,D$. Report $R_F$, $R_{L1}$, and dyadic $L^1$ bounds. This is the highest-priority empirical test.
2. **Bombieri--Iwaniec dissection for H5r-F** -- Write a detailed sketch: choose a dissection length $N$ for the $d$-sum, perform rational approximation, Poisson summation, and map the resulting parameters to Li--Yang's $M,H,T$. Determine whether the conditions of the main theorem can be satisfied after optimal choice of $N$, and compute the resulting $q$-dependent bound.
3. **Fejer spike simulation** -- For square $X$, evaluate $K_{H_D}(X/d)$ at $d$ making $X/d$ near an integer; compare the total residual after summation over $d$ with the scalar $D/H_D$.
4. **Signed Fourier tail numerical test** -- For a few $X,D$, compute the high-frequency tail $\mathcal T_1(D)$ and $\mathcal T_2(D)$ after truncating the signed Fourier series of $\psi$ at $H_D$. Measure whether the tail is smaller than the Fejer residual.
5. **Two-coset spacing test** -- Using the explicit C2 dual, apply both translation and multiplicative differencing and record whether the phase difference between the two cosets produces cancellation that survives a Cauchy--Schwarz bound.

---

## 4. Confidence calibration and failure modes

| Claim | Confidence | Remarks |
|-------|------------|---------|
| C2-Alg is exact under stated convention | High | Algebraic consequence of Poisson summation; verified. |
| C2-SP leading stationary phase constants | High | Standard stationary phase; constants checked. |
| Small-$k$ boundary harmless ($\ll X^{1/4}$) | High | Trivial bound; confirmed. |
| Derivative non-degeneracy for H5r phases (N1) | High | Exact differentiation; constants supplied. |
| Li--Yang phase class structurally compatible | High | Derivative checks pass. |
| Raw double sum fails Li--Yang Case A and B for $D\sim X^{1/2}$ | High | Numerical inequality verified. |
| Li--Yang's record exponent is $\theta^*>1/4$; the theorem does **not** prove H5r-F endpoint | High | Direct from Li--Yang paper. |
| A Bombieri--Iwaniec dissection could bring H5r-F into scope, but would give $\theta^*$ | Moderate | Requires constructing the dissection; plausible but not yet written. |
| H5r-F is genuinely weaker than H5r-B (i.e. Fejer averaging helps) | Moderate | Pending numerical test; R4 indicates potential equivalence. |
| Fejer spike risk is controlled by the Fejer-weighted residual sums | Low--Moderate | Needs numerical verification; spikes could exceed scalar bound. |
| Signed Fourier tail can be bounded without absolute values | Low | No known endpoint estimate; tail likely recreates H5r difficulty. |
| Mellin--Perron avoids the same bottleneck | Low | Functional-equation route reproduces Voronoi/Bessel structure; not a proven escape. |
| Current technology can reach $X^{1/4}$ via the Vaaler route | Low | Multiple obstructions (H5r, Abel trap, Li--Yang ceiling) are unresolved. |

**Principal failure modes:**

- **FM1** Fejer spikes for square $X$ cause residual much larger than $X^{1/4}$.
- **FM2** Abel-summation trap: any proof of H5r-F via partial sums reduces to H5r-B, which is equivalent to dyadic $L^1$ and known to be a divisor-type obstacle.
- **FM3** Incorrect invocation of Li--Yang on the raw double sum (hypothesis violation).
- **FM4** Even after a perfect Bombieri--Iwaniec reduction, Li--Yang's technology yields $\theta^*$, not $1/4$; a new first- or second-spacing result is required.
- **FM5** The signed Fourier tail cannot be controlled without absolute values, forcing a return to H5r-like estimates.

**Overall confidence in the route as a reduction framework:** High.
**Confidence that the route leads to a proof of the conjectural bound without a fundamentally new idea:** Low.

---

*End of Stage A report.*

## Cross Reviews

--- REVIEW FROM gpt_pro_thinking ---
Summary:
This is the Round 9 Stage B cross review of the Stage A outputs from `gemini_deep_think` and `deepseek_api`. Source packet:

Both agents correctly keep the balanced hyperbola/Vaaler route as a reduction and obstruction framework, not as a proof route. The main mathematical advance in the reviewed outputs is the theorem-level clarification that the raw H5r-F double sum at the endpoint block

$$
D\asymp X^{1/2},\qquad H_D\asymp D X^{-1/4}\asymp X^{1/4}
$$

does not fit the raw parameter hypotheses of Li--Yang's main exponential-sum theorem. This should be recorded as a serious false-proof guardrail, but not as an unconditional theorem that all Bombieri--Iwaniec/Li--Yang-style dissections fail. A full dissection could change the effective parameters, although present technology still only gives the Li--Yang exponent $\theta^*>1/4$, not the conjectural endpoint.

Most valuable input from others:

From `gemini_deep_think`:

1. **Li--Yang endpoint parameter clash.** Gemini correctly identifies the central numerical obstruction for a raw invocation of Li--Yang at the endpoint:
$$
   H_D\asymp X^{1/4}
$$
   while Case A gives
$$
   H\le M T^{-49/164}
$$
   and for $M\asymp X^{1/2}$, $T=X$, this is
$$
   H\le X^{1/2-49/164}=X^{33/164}\approx X^{0.2012}.
$$
   Case B is even more restrictive in the first upper bound:
$$
   H\le M^{35/69}T^{-2/23}\asymp X^{23/138}\approx X^{0.1667}.
$$
   This is a useful hard check against the false move "quote Li--Yang directly on H5r-F."

2. **Mellin--Perron dual-length diagnostic.** Gemini's H10-M computation correctly points toward the standard phenomenon: after applying the functional equation and stationary phase to the Perron integral for
$$
   4\zeta(s)L(s,\chi_4),
$$
   the saddle condition produces a dual phase of the form
$$
   2\pi\sqrt{nX}
$$
   and a dual length roughly
$$
   n\lesssim T^2/X.
$$
   If one chooses Perron height $T\asymp X^{3/4}$, this gives $n\lesssim X^{1/2}$, matching the Hardy/Voronoi/Bessel scale. This is valuable as a comparison diagnostic.

3. **Near-collision congruence bookkeeping.** Gemini's Q1-Ext is a useful algebraic lemma. For odd $d_1,d_2$ satisfying
$$
   d_1b-d_2a=\Delta,\qquad (a,b)=1,
$$
   the case $a,b$ both odd gives
$$
   \chi_4(d_1)\chi_4(d_2)=\chi_4(ab)(-1)^{\Delta/2}.
$$
   This is a genuine piece of signed matrix bookkeeping for future Bombieri--Iwaniec collision or near-collision analysis.

4. **Multiplicative parity-collapse test.** Gemini's C3-Mult observation is useful in the narrow setting where one models the two-coset dual coefficient by
$$
   \sigma(\xi)=\frac12(-1)^{2\xi},\qquad \xi\in \frac12\mathbb Z.
$$
   Under integer dilation $\xi_2=a\xi_1$, the coefficient product is
$$
   \sigma(\xi_1)\sigma(a\xi_1)
   =
   \frac14(-1)^{2\xi_1(1+a)}.
$$
   For odd $a$, this collapses to $1/4$. This is a valid algebraic diagnostic for one stylized spacing operation.

From `deepseek_api`:

1. **Exact C2 Poisson normalization.** DeepSeek gives the cleanest algebraic statement of the odd-lattice Poisson transform. With
$$
   e(t)=e^{2\pi i t},\qquad
   \widehat f(\xi)=\int_{\mathbb R}f(u)e(-\xi u)\,du,
$$
   and
$$
   f(u)=w_D(u)e(kX/u),
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
   This should be promoted as the official C2 algebraic transform.

2. **Correct stationary sign and scale separation.** For $\xi=-m<0$,
$$
   \widehat f(-m)=
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
   m\asymp kX/D^2.
$$
   DeepSeek also correctly separates the dual length
$$
   M_{\mathrm{dual}}\asymp kX/D^2
$$
   from the stationary-phase large parameter
$$
   \Lambda\asymp kX/D.
$$
   This distinction is essential for any uniform C2-SP lemma.

3. **Small-$k$ endpoint handling.** DeepSeek correctly observes that when
$$
   D\asymp X^{1/2},\qquad |k|\le X^\epsilon,
$$
   the dual length is $O(X^\epsilon)$ or smaller, so stationary phase is unnecessary. The primal trivial bound gives
$$
   |S_\star(k,D)|\ll D,
$$
   and after Vaaler normalization,
$$
   \frac{1}{H_D}|S_\star(k,D)|
   \ll
   \frac{D}{D X^{-1/4}}
   =
   X^{1/4}.
$$
   Thus $X^\epsilon$ many small frequencies remain harmless.

4. **More careful Li--Yang audit.** DeepSeek's audit is better calibrated than Gemini's. It distinguishes:
   - phase compatibility with Li--Yang's derivative hypotheses;
   - bounded-variation compatibility after residue splitting;
   - failure of raw Case A/Case B parameter ranges;
   - the need for a full Bombieri--Iwaniec dissection before invoking Li--Yang;
   - the fact that even after such a dissection, published technology gives $\theta^*>1/4$, not the endpoint.

Claims that look correct:

1. **Raw Li--Yang application fails at the endpoint block.**

With the raw identification
$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$
the endpoint H5r-F block violates both raw Case A and raw Case B frequency restrictions in Li--Yang's theorem. This is a correct and important guardrail.

2. **The H5r phases satisfy the derivative nondegeneracy condition.**

For
$$
F(z)=1/z,
$$
one has
$$
F'F'''-3(F'')^2=-6z^{-6}.
$$
For shifted/scaled variants such as
$$
F_{2,1}(z)=\frac{1}{z+1/D}
$$
and
$$
F_2(z)=\frac{1}{4z},
$$
the same nonvanishing structure remains on compact subintervals of $(0,\infty)$. Thus the obstruction is not phase smoothness or curvature in the Li--Yang sense; it is parameter range, norm, coefficient, and dissection structure.

3. **The parity indicator must be handled by residue splitting before any BV theorem.**

The raw function $1_{2\nmid d}$ is not a bounded-variation amplitude in Li--Yang's continuous $G(m/M)$ framework if inserted directly. After splitting $d=2n+1$, the parity is absorbed into the parametrization and the amplitude becomes smooth. This is the correct treatment.

4. **C2-Alg is correct.**

DeepSeek's odd-lattice Poisson formula reconciles the alternating representation and the two-coset representation. This should replace earlier informal versions of C2.

5. **The C2 stationary phase has active sign $\xi<0$.**

With the convention
$$
\widehat f(\xi)=\int f(u)e(-\xi u)\,du,
$$
the stationary phase for $e(kX/u-\xi u)$ occurs when $\xi<0$. Writing $\xi=-m$, $m>0$, gives
$$
u_0=\sqrt{kX/m}.
$$

6. **The leading C2 amplitude scale is correct.**

In the interior range
$$
m\asymp kX/D^2,
$$
the leading size is
$$
|\widehat f(-m)|\asymp D^{3/2}(kX)^{-1/2}.
$$
The exact error term still needs a uniform proof, but the main scale is right.

7. **R4 remains a central diagnostic.**

The Fejer identity
$$
\sum_{k=1}^{H}\left(1-\frac{k}{H+1}\right)a_k
=
\frac1{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j}a_k
$$
shows that any proof of H5r-F using only partial-sum bounds risks collapsing into H5r-B-type difficulty. This is not an equivalence theorem, but it is a serious methodological warning.

8. **Mellin--Perron likely reconstructs the Hardy/Voronoi/Bessel scale.**

The dual-length computation
$$
n\lesssim T^2/X
$$
after functional equation and stationary phase is a sound diagnostic. It supports keeping Mellin--Perron as a comparison route, not as an immediate escape from H5r.

Claims that need proof:

1. **That Li--Yang-derived methods cannot handle H5r-F after dissection.**

The raw parameter mismatch is proved. The stronger claim that current reciprocal-sum spacing technology "mathematically cannot evaluate" H5r-F is not proved until the full Bombieri--Iwaniec dissection is carried out with the Fejer weights and residual norms. The correct present status is:

$$
\text{raw Li--Yang theorem does not apply}
$$

not

$$
\text{all Li--Yang/Bombieri--Iwaniec technology is impossible here}.
$$

2. **That restricting $H$ to $X^{33/164}$ permanently forces exponent $0.2988$.**

Gemini's calculation
$$
X^{1/2}/X^{33/164}=X^{49/164}\approx X^{0.2988}
$$
is correct for the zero mode under a naive restriction of the local Vaaler height. But this is only a diagnostic for that truncation choice. It is not a theorem excluding alternative truncations, signed remainders, smoothing, or a different treatment of the fixed Fejer residual.

3. **Uniform C2-SP error term.**

DeepSeek's leading stationary-phase term is reliable, but the error
$$
O\bigl((kX)^{-1}D^{3/2}\bigr)
$$
should not be promoted without proof. A uniform lemma must distinguish:
$$
\Lambda\asymp kX/D,\qquad M_{\mathrm{dual}}\asymp kX/D^2,
$$
and handle:
- $M_{\mathrm{dual}}\asymp 1$;
- stationary points near support boundaries;
- nonstationary tails;
- dependence on derivatives of $w_D$.

4. **Mellin--Perron height necessity.**

The statement "targeting $X^{1/4}$ necessitates Perron height $T\asymp X^{3/4}$" is plausible for sharp Perron with standard coefficient bounds, but not yet theorem-level for smoothed Perron. Smoothed kernels, moment estimates, and contour choices can alter the truncation-error bookkeeping. Record the $T\asymp X^{3/4}$ calculation as sharp-Perron diagnostic, not as a universal necessity.

5. **H10-M as an exact equivalence.**

Gemini's H10-M should be demoted from "proved algebraic diagnostic mapping" if interpreted globally. What is proved is the saddle-point scale and phase under standard contour/functional-equation analysis. The exact theorem still needs:
- the precise completed functional equation for $4\zeta(s)L(s,\chi_4)$;
- residue extraction at $s=1$;
- smoothing kernel;
- treatment of horizontal and transition contributions;
- coefficient normalization in the dual sum.

6. **C3-Mult beyond integer dilations.**

Gemini proves collapse for odd integer dilations $a$. If the spacing relation uses rational slopes or matrix transformations not preserving $\frac12\mathbb Z$ in the same way, the lemma must be restated with the exact arithmetic domain. Even for even integer dilations, Gemini's statement that they "fail to lower the square-root degree of the phase" is not proved.

7. **Q1-Ext analytic usefulness.**

Q1-Ext is algebraically correct, but no saving follows until it is inserted into an actual near-collision or spacing matrix before absolute values erase the sign. The next step must build a toy matrix or a genuine Bombieri--Iwaniec off-diagonal expression retaining
$$
\chi_4(ab)(-1)^{\Delta/2}.
$$

8. **Fejer spike severity.**

Both agents treat Fejer spikes as a serious stress-test, correctly. But no lower bound or numerical result shows that spikes force H5r-F above $X^{1/4+\epsilon}$. The spike issue should remain a numerical and analytic stress test, not a proven obstruction.

Possible errors or hidden assumptions:

1. **Gemini overstates the Li--Yang obstruction.**

The phrase "current reciprocal-sum spacing theorems mathematically cannot evaluate the upper-frequency range" is too strong. The raw theorem with $M=D$, $H=H_D$ fails, but Li--Yang's actual proof pipeline involves dissection before theorem application. The correct conclusion is:

$$
\text{Direct quotation of Li--Yang on raw H5r-F is invalid.}
$$

A stronger no-go statement requires carrying through the dissection and showing that all resulting effective blocks remain outside the valid range or only yield $\theta^*$.

2. **Gemini's BV penalty is partly misleading.**

It is true that inserting $1_{2\nmid d}$ directly as a continuous $G$ creates an unacceptable variation issue. But the correct approach is to split into residue classes. After $d=2m+1$, the amplitude is smooth/BV and no $O(D)$ variation loss is intrinsic. Thus the "BV penalty" is a false-proof warning, not an obstruction after proper residue splitting.

3. **Gemini uses too much equivalence/isomorphism language for Mellin--Perron.**

The saddle calculation strongly suggests that Mellin--Perron returns to Voronoi/Bessel-type sums of length $X^{1/2}$, but "strictly limit" and "analytic isomorphism" are too strong without the complete contour theorem.

4. **Gemini's C3-Mult may not model the actual spacing transformation.**

Odd/even integer dilation is only one stylized operation. Bombieri--Iwaniec spacing matrices involve rational approximations and unimodular transformations; the parity coefficient may transform in a less elementary way. C3-Mult is a useful diagnostic, not a substitute for a matrix-level analysis.

5. **DeepSeek did not actually run the numerical tests.**

The assigned task included numerical tests comparing H5r-F, H5r-B, and H5r-L1. DeepSeek supplied a good test plan but no data. This is acceptable as a planning contribution, but it should not be scored as execution.

6. **DeepSeek's H5r-F compatibility with Li--Yang needs dyadic decomposition.**

Li--Yang's sum is over $H\le h\le 2H$ with a BV amplitude on $[1,2]$. H5r-F is a full triangular sum over $1\le |k|\le H_D$. To compare them line by line, one must decompose into dyadic $K\le H_D$ blocks and define
$$
g_K(k/K)=\eta_{k,H_D}
$$
on each block. The variation on each block is harmless, but this step should be explicit.

7. **DeepSeek's C2-SP error estimate is not yet validated.**

The leading constant and phase are plausible, but the stated error should not enter the lemma bank as proved. The repo should mark C2-SP as "leading term and scales checked; uniform stationary phase pending."

8. **Both agents risk confusing structural compatibility with theorem-level applicability.**

For H5r, the derivative hypotheses are easy. The hard questions are:
- allowed outer weights;
- fixed Fejer average versus dyadic arbitrary coefficients;
- blockwise absolute values;
- residue/parity coefficients;
- whether the theorem estimates $S$ or $S/H$ in the exact norm needed;
- whether the endpoint range $H_D\asymp X^{1/4}$ is reachable after all reductions.

Suggested synthesis:

1. **Promote the raw Li--Yang mismatch as a guardrail, not a no-go theorem.**

Add lemma:

**LY-Raw-Mismatch.**
For the raw H5r-F endpoint block
$$
T=X,\qquad M=D\asymp X^{1/2},\qquad H=H_D\asymp X^{1/4},
$$
the raw double sum does not satisfy Li--Yang Case A or Case B. Specifically:
$$
H_D=X^{1/4}>X^{33/164}=M T^{-49/164}
$$
and
$$
H_D=X^{1/4}>X^{23/138}=M^{35/69}T^{-2/23}.
$$
Therefore Li--Yang's main theorem cannot be quoted directly on the raw Vaaler residual block.

Status: proved guardrail.

Add warning: this does not preclude a full Bombieri--Iwaniec dissection; it only blocks raw theorem invocation.

2. **Use DeepSeek's C2-Alg as the official C2 lemma.**

Record:

**C2-Alg.**
For $f(u)=w_D(u)e(kX/u)$ and $\widehat f(\xi)=\int f(u)e(-\xi u)\,du$,
$$
\sum_{2\nmid d}f(d)
=
\frac12\sum_{m\in\mathbb Z}\widehat f(m)
-
\frac12\sum_{\mu\in\mathbb Z+1/2}\widehat f(\mu)
=
\frac12\sum_{n\in\mathbb Z}(-1)^n\widehat f(n/2).
$$

Status: proved algebraic lemma under the stated Fourier convention.

3. **Split C2-SP into leading-term and uniform versions.**

Record:

**C2-SP0.**
For $m>0$ with $m\asymp kX/D^2$,
$$
\widehat f(-m)
\sim
\frac{w_D(\sqrt{kX/m})}{\sqrt{2m/\sqrt{kX/m}}}
e(2\sqrt{kXm}+1/8),
$$
so
$$
|\widehat f(-m)|\asymp D^{3/2}(kX)^{-1/2}.
$$

Status: leading stationary phase accepted.

Then create a separate target:

**C2-SPU.**
Uniform stationary phase with boundary, nonstationary, and $M_{\mathrm{dual}}\asymp 1$ transition estimates.

Status: required, not proved.

4. **Demote H10-M to diagnostic comparison.**

Keep the saddle relation:
$$
t_0\asymp \sqrt{nX},\qquad n\lesssim T^2/X.
$$
If $T\asymp X^{3/4}$, then $n\lesssim X^{1/2}$. But do not call Mellin--Perron an exact isomorphism until the contour and functional-equation proof is written.

5. **Keep Q1-Ext as an algebraic input for signed spacing matrices.**

Promote Q1-Ext as an algebraic lemma, but add a dependency:

To become analytically useful, Q1-Ext must be inserted into an off-diagonal spacing expression before Cauchy--Schwarz or matrix norm bounds replace signs by absolute values.

6. **Keep C3-Mult as a narrow diagnostic.**

C3-Mult should be recorded as:

For the model coefficient $\sigma(\xi)=\frac12(-1)^{2\xi}$ on $\frac12\mathbb Z$, odd integer dilation collapses the coefficient product to a constant. This diagnoses one class of parity-loss mechanisms. It does not rule out general two-coset spacing methods.

7. **Make the next round computationally concrete.**

The highest-value empirical task remains the H5r norm comparison:
$$
R_F(D)=
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|,
$$
versus
$$
R_{L1}(D)=
\frac1{H_D}
\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$
This is the fastest way to test whether fixed Fejer averaging is materially easier than H5r-B/L1.

Score by agent:

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|---|---:|---|---|
| `gemini_deep_think` | 7.6 | Valuable high-level obstruction synthesis: raw Li--Yang frequency clash, Mellin--Perron dual-length diagnostic, Q1-Ext congruence bookkeeping, and C3-Mult parity test. Main weakness is overstatement: raw theorem mismatch is treated too close to a global no-go theorem, BV parity loss is overstated before residue splitting, and Mellin--Perron/C3 language is too strong for the proofs supplied. | Convert LY-Audit into a precise raw-mismatch lemma only; demote H10-M and C3-Mult to diagnostics; insert Q1-Ext into an actual signed spacing matrix before claiming analytic value. |
| `deepseek_api` | 8.5 | Strongest technical output: exact C2 Poisson normalization, correct two-coset/alternating reconciliation, reliable leading stationary-phase constants, small-$k$ boundary handling, and a more careful Li--Yang theorem-level audit distinguishing structural compatibility from raw parameter failure. Main weakness is that numerical tests were planned rather than run, and C2-SP uniform errors remain unproved. | Run the H5r-F/H5r-B/H5r-L1 numerical tests; write dyadic Fejer-to-Li--Yang normalization explicitly; prove or qualify the uniform C2-SP error term and boundary transition. |

Next-round recommendation:

1. **Do not pivot away from H5r-F.** The central target remains the fixed-Fejer residual. The next round should decide whether it is genuinely easier than H5r-B/L1 or only cosmetically weaker.

2. **Run the numerical H5r norm comparison.** This is the highest-priority concrete action. Use square, nonsquare, and near-square $X$; test both $D\asymp X^{1/2}$ and $D\asymp X^{3/8}$; report $R_F$, $R_{L1}$, and dyadic $L^1$ norms for $S_{\mathrm{odd}}$ and $S_\rho$.

3. **Add LY-Raw-Mismatch as a proved guardrail.** State explicitly that Li--Yang cannot be quoted directly on the raw endpoint H5r-F block. Also state explicitly that this does not prove failure after full Bombieri--Iwaniec dissection.

4. **Write the full Bombieri--Iwaniec dissection map for H5r-F.** The next analytic task is not another raw parameter comparison. It is to choose the dissection length, derive the effective $M,H,T,N,K,L$ parameters, and determine whether the Li--Yang theorem applies after dissection and what exponent it returns.

5. **Promote C2-Alg and split C2-SP.** C2-Alg should enter the lemma bank as proved. C2-SP should be split into a leading interior stationary-phase lemma and a separate uniform transition lemma.

6. **Keep Mellin--Perron as comparison only.** The next Mellin--Perron work should write exact sharp and smoothed Perron errors, then derive the dual length after the functional equation. Avoid calling it circular or isomorphic until the full contour argument is explicit.

7. **Test Q1-Ext inside a signed matrix.** Construct a toy near-collision sum retaining
$$
\chi_4(ab)(-1)^{\Delta/2}
$$
and identify the exact step where standard Cauchy--Schwarz or matrix norm methods erase the sign. This will show whether Q1-Ext is merely decorative or a possible source of new cancellation.

8. **Maintain the no-exponent-improvement status.** Round 9 supplies useful obstruction mapping and theorem-audit precision, but it proves no new Gauss circle bound.

--- REVIEW FROM gemini_deep_think ---
This is Stage B cross review for Round 9.

## 1. Executive Summary and Route Pivot

Round 9 introduces a fundamental paradigm shift in the repository's analytical approach to the Gauss Circle Problem. In previous rounds, the research state was heavily constrained by the "Fejer Majorant Trap"--the diagnostic assumption that bounding the positive residual generated by the finite Vaaler approximation necessitated complex, character-blind reciprocal-sum estimates at the unreachable exponent of $X^{1/4+\epsilon}$.

In this stage, `gpt_pro_thinking` completely circumvented this assumption with **Lemma R5**, supplying an elementary spatial-bounding argument that evaluates the fixed-Fejer residual directly via geometric divisor counting. Simultaneously, `deepseek_api` executed an exact parameter-level audit of the Li--Yang exponential sum theorem, providing a mathematical demonstration that the theorem cannot be invoked as a black box on our raw dyadic blocks because the parameters strictly violate the necessary constraints.

Consequently, the analytic path forward appears vastly clearer but technically steeper:

1. The Vaaler residual appears to be solved unconditionally at the conjectural scale $X^{1/4+\epsilon}$ via R5.
2. The entire burden of the exponent improvement now rests exclusively on extracting cross-variable character cancellation from the main oscillatory sums **H5a** and **H5b**.
3. Off-the-shelf literature (such as Li--Yang and Huxley) is structurally incapable of reaching the endpoint scale without fundamentally new spacing, large-sieve, or character-aware innovations.

## 2. Most valuable input from others

**From `gpt_pro_thinking`:**
The introduction of **Lemma R5 (Fejer product-count bound)** is the most valuable mathematical insight of the entire multi-round workflow to date. By evaluating the Vaaler majorant $K_H(X/d)$ directly in physical space rather than breaking it down into dyadic Fourier frequencies, `gpt_pro_thinking` prevents the artificial destruction of positivity. It elegantly reduces the reciprocal-sum problem to a trivial lattice-point count of near-products $md \approx X$. The resulting arithmetic yields an unconditional $O_\epsilon(X^{1/4+\epsilon})$ envelope via the absolute divisor bound $\tau(n) \ll_\epsilon n^\epsilon$. This completely bypasses the need for Bombieri--Iwaniec techniques on the residual and permanently clears the H5r bottleneck.

**From `deepseek_api`:**
The meticulous parameter-level audit of the Li--Yang TeX source (**Lemma LY-Raw-Mismatch**) is invaluable for maintaining repository hygiene. By algebraically mapping our dyadic parameters ($M \asymp X^{1/2}$, $H \asymp X^{1/4}$) against Li--Yang's explicit Case A and Case B constraints, `deepseek_api` incontrovertibly proved that the raw main sums fall far outside the theorem's valid analytic envelope. This halts a dangerous false-proof vector and forces the workflow to acknowledge the hard structural limits of discrete Hardy--Littlewood methods.

## 3. Detailed Assessment of `gpt_pro_thinking`

The Stage A packet submitted by `gpt_pro_thinking` provides a lateral mathematical breakthrough that rescues the workflow from a self-imposed local minimum.

The core of the contribution is **Lemma R5**. We supply the full proof of this lemma here to definitively establish its validity. The standard Fejer kernel obeys the pointwise inequality $K_H(t) \ll \min(H, \frac{1}{H\|t\|^2})$. Thus, the normalized residual majorant per term is bounded by $\frac{1}{H} K_H(t) \ll \min(1, \frac{1}{H^2\|t\|^2})$.
For a denominator $d \sim D$, the distance to the nearest integer is defined as $\|X/d\| = \min_{m \in \mathbb{Z}} |X/d - m| = \min_m \frac{|X-md|}{d}$.
Because $d$ is bounded by $2D$, we deduce $\|X/d\| \ge \frac{|X-md|}{2D}$.
Substituting this back into the envelope yields $\frac{4D^2}{H^2|X-md|^2} = \frac{4\Delta^2}{|X-md|^2}$, where the interaction width is defined as $\Delta = D/H$.
For the endpoint Vaaler scale, we have $H = H_D \asymp D X^{-1/4}$, which forces $\Delta \asymp X^{1/4}$.

Summing this pointwise bound over $d \sim D$ involves summing over pairs $(m,d)$ where the product $md = n$ lies in a neighborhood of $X$. The number of preimages $(m,d)$ for any specific integer $n$ is strictly bounded by the total divisor function $\tau(n)$. Since $\tau(n) \ll_\epsilon n^\epsilon \ll X^\epsilon$, the sum over $d$ is unconditionally bounded by the envelope $\sum_{n \asymp X} \tau(n) \min\left(1, \frac{4\Delta^2}{|X-n|^2}\right)$.

We evaluate this interval summation explicitly:

1. For the core interval $|X-n| \le 2\Delta$, the minimum evaluates to $O(1)$. Since the interval contains $O(\Delta)$ integers, and $\tau(n) \ll_\epsilon X^\epsilon$ uniformly, this core sum contributes $O(\Delta X^\epsilon)$.
2. For the dyadic annuli $2^j \Delta < |X-n| \le 2^{j+1} \Delta$, the minimum evaluates to $\le 4^{-j}$. The annulus length is $O(2^j \Delta)$. Summing the divisor bound gives $O(2^j \Delta X^\epsilon)$. Multiplying by the spatial decay $4^{-j}$ gives a contribution of $O(2^{-j} \Delta X^\epsilon)$.
3. Summing over all $j \ge 1$ forms a rapidly convergent geometric series, yielding a global unconditional bound of $O(\Delta X^\epsilon) = O(X^{1/4+\epsilon})$.

This derivation is immaculate. It proves that the Vaaler residual is unconditionally bounded at the conjectural scale by elementary arithmetic, bypassing the H5r-B arbitrary-coefficient trap entirely.

Furthermore, `gpt_pro_thinking` accurately assessed the Li--Yang parameters, recognizing that Li--Yang's final theorem truncates at $Y = M T^{-\theta^*}$. Because $\theta^* \approx 0.314 > 0.25$, their truncation falls structurally short of our required endpoint $M T^{-1/4}$. The agent's recommendation to deprecate arbitrary coefficients and focus strictly on exact Vaaler coefficients (Lemma M9) is the only viable path forward.

## 4. Detailed Assessment of `deepseek_api`

`deepseek_api` delivered a highly rigorous, formalistic packet that provides an essential parameter boundary for the repository. The agent focused heavily on algebraic hygiene, parameter verification, and boundary analysis.

The standout contribution is the formal **Li--Yang parameter audit**. We supply the explicit arithmetic proof here to validate the agent's claim that the raw dyadic blocks fail Li--Yang's constraints.

* **Case A Constraint:** Li-Yang requires $H \le M T^{-49/164}$. Evaluating this for our critical block $M \asymp X^{1/2}$ and $T=X$ yields a permissible ceiling of $H \le X^{1/2} X^{-49/164} = X^{82/164 - 49/164} = X^{33/164} \approx X^{0.2012}$. Since our endpoint requires a frequency height of $H_D \asymp X^{0.25}$, we exceed the theorem's bounds by a vast polynomial margin ($0.25 > 0.2012$).
* **Case B Constraint:** Li-Yang requires $H \le M^{35/69}T^{-2/23}$. Evaluating this term gives $X^{35/138} X^{-12/138} = X^{23/138} = X^{1/6} \approx X^{0.1667}$. Since $0.25 > 0.1667$, Case B definitively fails.

This evaluation incontrovertibly proves that the raw Vaaler main terms cannot be fed directly into Li--Yang's theorem as a black box.

Furthermore, `deepseek_api` provided **C2-Alg**, proving algebraically that the odd-lattice Poisson transform can be written equivalently as $\frac{1}{2} \sum_{n \in \mathbb{Z}} (-1)^n \widehat{f}(n/2)$ via the identity $1 - (-1)^d = 1 - e(d/2)$. This bridges the gap between the alternating-sequence and two-coset formulations. The agent's rigorous confirmation of **B-Boundary** (trivial bounds at small $k$) safely seals the low-frequency edge cases where standard stationary phase at $M \asymp 1$ breaks down.

However, `deepseek_api` missed the elementary geometric simplification of the residual found by `gpt_pro_thinking`, assuming incorrectly that H5r-F remains an overarching bottleneck subject to the "Abel-summation trap."

## 5. Claims that look correct

> **Lemma R5 (Fejer product-count bound for H5r-F)**
> The fixed-Fejer residual sum evaluates unconditionally to $\ll_\epsilon X^{1/4+\epsilon}$ via elementary divisor counting in the physical spatial domain.

> **Lemma LY-Raw-Mismatch (Li--Yang Parameter Domain Failure)**
> The raw double sum for the critical dyadic block strictly exceeds the permissible frequency height $H$ for both Case A and Case B of Li--Yang's theorem, confirming that $H_D \asymp X^{0.25}$ breaks current continuous spacing records.

> **Lemma C2-Alg (Odd-lattice Poisson transform parity)**
> The convention-fixed identities for the odd-lattice Poisson summation under $e(t) = e^{2\pi i t}$ are algebraically exact and properly reconcile the half-integer dual cosets.

> **Lemma M9 (Exact main-term norm implementation)**
> To prevent artificial $L^1$ inflation, the main terms must strictly lock in the trigonometric Vaaler coefficients $\alpha_h \asymp 1/h$, permanently deprecating arbitrary bounded variables $u_h$.

## 6. Claims that need proof

1. **Second-leg extension of Lemma R5:** The nearest integer formulation demands evaluating $\|(X/d + \rho)/4\|$. This distance is minimized by some integer $m$, yielding the absolute discrepancy $|X/d + \rho - 4m|/4 = |X - d(4m-\rho)| / (4d)$. Letting $n = d(4m-\rho)$, we are effectively counting the number of factorizations of an integer $n$ into a divisor $d$ and a co-divisor $m' = 4m-\rho$. This restricts the co-divisor to a specific residue class $m' \equiv -\rho \pmod 4$. We must formally document that this restricted divisor count is universally bounded by $\tau(n)$ to fully prove the second leg.
2. **Bombieri--Iwaniec Dissection for H5a/H5b:** Now that the residual is solved, the entire problem rests on the main terms. Because the raw sums do not fit Li--Yang, it would require showing that a Bombieri--Iwaniec rational dissection (cutting $D$ into intervals of length $N$) can bring the effective parameters into a regime where Q1-Ext (rational collision signs) can be exploited.
3. **C2-SP Uniform Error Bounds:** The leading stationary phase term derived by `deepseek_api` is correct, but uniform error bounds in the transition regime where the dual length $M = kX/D^2 \asymp 1$ remain unwritten. An incomplete Gamma transition lemma must bridge the gap between B-Boundary and the interior.

## 7. Claim-by-Claim Corrections and Verifications

1. **Verification of Lemma R5 Product-Count (`gpt_pro_thinking`):** The conversion of the Fejer kernel bound to divisor representations evaluates unconditionally to $O_\epsilon(X^{1/4+\epsilon})$. This elegantly sidesteps exponential sum cancellation entirely.
2. **Verification of LY-Raw-Mismatch (`deepseek_api`):** The algebraic substitution verifying the Li-Yang parameter failure is correct. The limit $X^{0.2012}$ falls vastly short of $X^{0.25}$.
3. **Correction to DeepSeek's FM1 (Fejer Spikes):** `deepseek_api` hypothesized that perfect squares $X=N^2$ create unmanageable Fejer spikes. This appears mathematically false. At exact divisors, $\|X/d\| = 0$ and $K_H(0) = H_D + 1$. The contribution is strictly bounded by $\frac{1}{H_D} \cdot (H_D+1) \cdot \tau(X) \ll_\epsilon X^\epsilon$, entirely absorbing the spike within the error envelope.
4. **Correction to DeepSeek's FM2 (Abel-Summation Trap):** `deepseek_api` hypothesized that any proof of H5r-F requires partial-sum bounds. This assumes a frequency-first approach. `gpt_pro_thinking` bypasses this by integrating the positive kernel in the spatial domain, effectively avoiding the trap.
5. **Verification of C2-Alg (`deepseek_api`):** The algebraic reconciliation of the one-sequence $(-1)^m$ and two-coset formulations is exact under the $e(t) = e^{2\pi i t}$ convention.
6. **Verification of Lemma B-Boundary (`deepseek_api`):** The trivial bounding of the small-$k$ boundary layer where $k \ll X^\epsilon$ correctly resolves the stationary-phase breakdown region via the $1/H_D$ prefactor scaling.
7. **Verification of Lemma N1 (`deepseek_api`):** The computation $|F'F''' - 3(F'')^2| = 6(z+1/D)^{-6} \ge 3/32$ establishes the derivative non-degeneracy with exact absolute lower bounds.
8. **Correction to GPT's Signed Fourier Alternative:** `gpt_pro_thinking` suggests retaining signed Fourier truncation as an alternative. Because R5 provides a complete majorant solution without losing signs on the main term, this alternative is obsolete and it is recommended to deprecate it permanently to reduce workflow drag.

## 8. Concrete Stress Tests

1. **ST1: R5 Exact Square Spike Simulation:** Set $X = N^2$. Numerically evaluate the sum $\frac{1}{H_D}\sum K_{H_D}(X/d)$ specifically over the exact divisors $d|N^2$. This tests whether the theoretical bound of $\tau(X) \ll X^\epsilon$ functionally suppresses the maximal Fejer spike as mathematically predicted, confirming FM1 is a phantom obstruction.
2. **ST2: Li-Yang B-Process Parameter Inversion Test:** Dualize the main term to produce a dual length $M_{dual} \asymp hX/D^2 \asymp X^{1/4}$. Check these new parameters against Li-Yang's Case A constraints to verify whether Poisson summation accidentally pushes the system into a valid analytic envelope. (Preliminary checks suggest $X^{0.5} \not\le X^{-0.048}$, meaning dualization worsens the mismatch).
3. **ST3: Spectral Trace of Q1-Ext Collision Matrix:** Construct a local rational collision spacing matrix using the Q1-Ext signs $\chi_4(ab)(-1)^{\Delta/2}$. Compute the maximal eigenvalue (spectral norm) directly, then recompute with absolute values over all entries. This tests whether Cauchy-Schwarz permanently erases the character cancellation.

## 9. Suggested synthesis

The research state has undergone a fundamental phase shift. The ghost bottleneck of the Vaaler residual appears to be fully solved. The repository synthesis must reflect this newly established clarity:

1. **Promote R5 to Proved:** The fixed-Fejer residual H5r-F appears unconditionally bounded by $O_\epsilon(X^{1/4+\epsilon})$. The Fejer Majorant DDP Trap (C1) and the Abel Summation Trap (R4) are bypassed.
2. **Retire Arbitrary Coefficients:** Lemmas H5r-B and H5r-L1 must be moved out of the active analytical path. The arbitrary-coefficient formulations artificially destroy the coherence of the positive Fejer kernel and invoke impossible $L^1$ barriers.
3. **Pivot to Lemma M9 (The Main Terms):** The entire weight of the Gauss Circle Problem now rests on the Vaaler main oscillatory terms. We must estimate $\sum_{1 \le |h| \le H_D} \alpha_h \sum_{d \sim D} \chi_4(d) w_D(d) e(hX/d)$ armed strictly with the exact Vaaler coefficients $\alpha_h \asymp 1/h$.
4. **Formalize the Li--Yang Boundary:** Record LY-Raw-Mismatch officially. Known continuous spacing technology maxes out at $\theta^* \approx 0.31448$. Reaching the conjectural target $0.25$ strictly limits black-box application and requires custom cross-cancellation that exploits the specific arithmetic of $\chi_4$.
5. **Next Strategic Action:** The immediate next step for the workflow is to explicitly construct the Bombieri--Iwaniec minor-arc rational collision matrix for the main sum H5a, injecting the rational collision lemma (Q1-Ext) into the spacing matrix to determine if the $\chi_4(ab)$ trace survives the large sieve.

## 10. Score by agent

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
| --- | --- | --- | --- |
| `gpt_pro_thinking` | 10 | Uncovered R5, an elementary proof that completely annihilates the residual bottleneck via spatial product counting. Brilliant lateral insight. | Formally write out the exact discontinuity match for the Vaaler majorant at integers. |
| `deepseek_api` | 9 | Provided an incontrovertible parameter audit proving that Li-Yang fails on our raw dyadic blocks, stopping a false proof trap. | Develop the exact Bombieri-Iwaniec dissection mapping parameters for H5a. |

## 11. Confidence calibration and failure modes

**Confidence:**

* **Confidence: High.** The proof of Lemma R5 evaluating the Fejer kernel via geometric product counting appears mathematically unconditional, relying solely on the $\tau(n) \ll_\epsilon X^\epsilon$ divisor bound.
* **Confidence: High.** The algebraic mapping of our parameters against the Li--Yang exponential sum theorem (LY-Raw-Mismatch) definitively proves that existing continuous spacing theorems cannot evaluate the block at $H_D \asymp X^{0.25}$.
* **Confidence: Moderate.** The custom Bombieri-Iwaniec dissection required to handle the main sums may map the parameters into a domain where spacing geometry becomes analytically viable, but it requires intricate new matrix construction.
* **Confidence: Low.** The assumption that standard large sieve theorems can bypass the $\theta^* \approx 0.314$ ceiling without taking absolute values that destroy the $\chi_4$ character seems highly improbable.

**Active Failure Modes (FM):**

1. **FM-Main-Term Character Erasure:** Applying standard double large sieve theorems typically requires taking absolute values over the matrix entries to construct a positive semi-definite bound. If a future synthesis takes absolute values, it appears to erase the $\chi_4(d)$ character, which would force the sum back to the $X^{0.314}$ divisor problem ceiling.
2. **FM-Discontinuity Jump Leakage:** At integers $X/d \in \mathbb{Z}$, the floor-compatible sawtooth jumps to $\psi(n) = -1/2$. The Vaaler polynomial evaluates to $0$. We must rigorously verify that the exact constants in the Fejer majorant exactly upper-bound the $1/2$ discrepancy without leaking a point mass anomaly.
3. **FM-Residue Class BV Destruction:** Li-Yang requires Bounded Variation (BV) frequency weights. Splitting $\chi_4(h)$ into positive and negative residue classes to satisfy this destroys the cross-cancellation inherent to the frequency character in H5b.
4. **FM-Stationary Phase Boundary Collapse:** In C2-SP, applying classical stationary phase when the dual length $M = kX/D^2 \asymp 1$ generates false asymptotic tails. This boundary layer would require showing rigorous incomplete Gamma or smooth cutoff transitions to avoid $L^1$ blowup.

## 12. Next-round recommendation

**For the Judge Synthesis (Stage C):**
Declare the H5r residual bottleneck completely solved. Retire diagnostics C1 and R4 as bypassed historical artifacts. Anchor the workflow completely on H5a and H5b. Acknowledge that the Gauss Circle Problem target exponent $X^{1/4+\epsilon}$ cannot be attained through blind application of state-of-the-art spacing theorems.

**For `gpt_pro_thinking`:**
Update the Best Proof Draft to formally incorporate Lemma R5, permanently clearing the Vaaler residual from the gap register. Explicitly write out the modulo arithmetic for the shifted second-leg bounds. State the exact targets for H5a and H5b with the precise Vaaler coefficients $\alpha_h$ (Lemma M9).

**For `deepseek_api`:**
Perform the exact B-process (twisted Poisson summation) on the newly formulated H5b main term, tracking the exact phase shifts, the extraction of the Gauss sum for $\chi_4(h)$, and the resulting dual variables. Determine if the dualized H5b exhibits the same zero-Hessian degeneracy as H5a.

**For `gemini_deep_think`:**
Execute the ST3 stress test. Take the proven Q1-Ext congruence lemma and insert it into a model double-large-sieve spacing matrix. Determine mathematically whether Cauchy-Schwarz permanently erases the $\chi_4$ character or if a signed quadratic form can salvage the cancellation.

--- REVIEW FROM deepseek_api ---
# Stage B Cross Review -- Round 9

**Reviewer:** `deepseek_api` (algebra checker, obstruction auditor, and stress tester)

This review evaluates the Stage A outputs from `gpt_pro_thinking` and `gemini_deep_think` for Round 9.
The task is a referee-style assessment: identify correct claims, flag gaps, detect hidden assumptions, propose synthesis, and assign scores.
The review is **not** a continuation of the proof.

---

## 1. Most valuable input from others

### From `gpt_pro_thinking`

* **Li--Yang source audit (L9.1).**
  The output correctly reads the actual LaTeX source and identifies the exact theorem hypotheses (`\label{definition of S}`, `\label{condition on F 1}`, `\label{condition on F 2}`, `\label{goal}`).
  The audit shows that Li--Yang's final circle/divisor application uses a truncation height $H\le M T^{-\theta^*}$, which at the critical denominator block $D\asymp X^{1/2}$ becomes $H\lesssim X^{0.1855...}$, far below the Vaaler endpoint height $H_D\asymp X^{1/4}$.
  Moreover, Li--Yang's theorem gives an exponent $\theta^*\approx0.31448 > 1/4$, so even if the range were extended, it does **not** supply the conjectural exponent.
  The audit also correctly notes that the theorem uses bounded-variation weights $g,G$, not arbitrary coefficients $v_k$; therefore it cannot imply the stronger residual norms H5r-B or H5r-L1.
  This is a decisive negative import result: **Li--Yang (2023) cannot be used as a black-box endpoint theorem for the Vaaler residual**.

* **Lemma R5 -- fixed-Fejer residual via product-counting.**
  This is the most original and potentially route-changing contribution of Round 9.
  The key idea is to evaluate the positive Fejer-kernel majorant of the Vaaler residual directly, without expanding it into dyadic arbitrary-coefficient reciprocal sums.
  The proof sketch uses the standard pointwise bound
  \[
  \frac1H K_H(t) \ll \min\!\Bigl(1,\frac1{H^2\|t\|^2}\Bigr),
  \]
  converts the sum over $d$ into a sum over product-pairs $(m,d)$ with $md\approx X$, exploits the divisor bound $\tau(n)\ll_\epsilon n^\epsilon$, and obtains the required $X^{1/4+\epsilon}$ bound.
  If this argument can be made rigorous (and the dependencies are only the Fejer-kernel estimate and the divisor bound), then **H5r-F is demolished as a bottleneck**.
  This is a major simplification of the proof sketch.

* **Norm overstrengthening of H5a/H5b recognised.**
  The output points out that the existing H5a/H5b targets assume arbitrary bounded coefficients $u_h$, while the actual Vaaler main-term coefficients satisfy $|\alpha_h|\ll 1/|h|$ with a definite sign pattern.
  This is a valuable corrective: the proof should work with the **exact fixed-coefficient** forms, not with the artificially stronger arbitrary-coefficient versions.  It may open the door to estimates that exploit the $1/h$ decay without requiring the full Li--Yang machinery.

### From `gemini_deep_think`

* **Li--Yang parameter-domain obstruction (N2-Audit).**
  Gemini goes further than the gpt audit by extracting the **domain restrictions** of Li--Yang's main theorem, namely Case A $H\le M T^{-49/164}$ and Case B $H\le M^{35/69}T^{-2/23}$.
  At the endpoint $M\asymp X^{1/2},\ T=X$, these force $H\le X^{33/164}\approx X^{0.2012}$ (Case A) and $H\le X^{23/138}\approx X^{0.1666}$ (Case B).  Since the Vaaler requirement is $H_D\asymp X^{1/4}=X^{0.25}$, the theorem's **hypothesis domain** is violated; it is not merely that Li--Yang gives a weaker exponent -- the theorem cannot even be legally invoked for the full Vaaler frequency range.
  This sharpens the obstruction and should be recorded as a permanent guardrail.

* **Mellin--Perron dual-length conservation (H10-M).**
  Gemini provides a step-by-step contour-shift and stationary-phase argument showing that targeting an $X^{1/4}$ error via a smoothed Perron integral of $4\zeta(s)L(s,\chi_4)$ forces a dual Voronoi-type sum with length $\asymp X^{1/2}$ and the degenerate phase $2\pi\sqrt{nX}$.  This formalises earlier diagnostic intuitions: the Mellin--Perron route **is not an escape**; it reconstructs the same reciprocal-Bessel obstacle.
  The argument is plausible and consistent with standard analytic-number-theory lore; it should be kept as a comparison lemma.

* **Algebraic parity-collapse diagnostics (C3-Mult).**
  The new observation that multiplicative (non-translation) differencing with odd dilations collapses the parity coefficient in the two-coset dual formulation is a nice algebraic fact.  It strengthens the H7/C3 family of obstructions: both translation and odd-rational-dilation differencing erase the character oscillation.  Even dilations survive formally, but they do not reduce the derivative order of the phase and are unlikely to provide spacing gains.

---

## 2. Claims that look correct

1. **Li--Yang source audit (both agents).**
   The statements about the final truncation height $Y=MT^{-\theta^*}$ and the domain constraints $H\le M T^{-49/164}$ are faithfully extracted from the LaTeX source and correctly evaluated numerically.  The conclusion that Li--Yang's theorem does not apply to the endpoint Vaaler height $X^{1/4}$ is therefore solid.

2. **R5 -- product-counting bound.**
   The overall structure of the argument is correct.
   The Fejer-kernel bound is standard.
   The change of variables $d\mapsto (m_d,d)$ and grouping by the product $n=m_d d$ is legitimate, because
   \[
   \|X/d\| = \frac{|X-m_d d|}{d} \asymp \frac{|X-n|}{D},
   \]
   and the number of divisor pairs $(m,d)$ with $md=n$ is at most $\tau(n)$.
   The subsequent dyadic-annulus estimate for $\sum_n \tau(n)\min(1,\Delta^2/|X-n|^2)$ with $\Delta=D/H\asymp X^{1/4}$ yields $O_\epsilon(X^{1/4+\epsilon})$; no subtle cancellation is required.
   Therefore, **if the Vaaler residual truly takes the form $\frac{C}{H}\sum_{d} |w_D(d)| K_H(X/d)$** (with $C$ absolute), then R5 proves H5r-F.

3. **Norm overstrengthening correction.**
   The identification that the actual Vaaler main-term coefficients are $\alpha_h\ll 1/|h|$ and not arbitrary bounded $u_h$ is mathematically correct and important.

4. **Gemini's Case-A/B extraction (N2-Audit).**
   The numbers $49/164$, $35/69$, $2/23$ are present in the LaTeX source (as earlier summarised in the reading packet) and the computed exponents $0.2012$ and $0.1666$ are accurate.

5. **Mellin--Perron dual length (H10-M).**
   The scaling argument that a truncation height $T\asymp X^{3/4}$ implies a dual length $N\asymp X^{1/2}$ is a standard consequence of Stirling's formula for the Gamma-ratio in the functional equation.  The phase $2\pi\sqrt{nX}$ is correctly derived.

6. **C3-Mult parity collapse for odd dilations.**
   The algebra $\sigma(\xi)=\frac12(-1)^{2\xi}$ and $\xi_2=a\xi_1$ with $a$ odd gives $2\xi_1(1+a)$ even, hence $\sigma(\xi_1)\sigma(a\xi_1)=1/4$.  This is a simple, provable congruence fact.

---

## 3. Claims that need proof (or further verification)

### 3.1 Lemma R5 -- complete rigorous proof

The gpt output gives a convincing sketch, but several details must be written down before the lemma can be promoted to "proved".

* **Exact Vaaler majorant constant.**
  The statement $|R_H(t)|\le \frac{1}{2H+2} K_H(t)$ must be verified against a standard reference (e.g., Vaaler's original paper or a textbook).  The proof draft should cite the precise theorem, including the normalisation of $K_H$ (often $K_H(t)=\frac{1}{H+1}\bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\bigr)^2$).  Minor differences in constants do not affect the $X^{1/4+\epsilon}$ target, but a careful check is needed for the exact residual bound.

* **Handling of the second-leg residual.**
  The gpt sketch says "the same argument works for $K_H((X/d+\rho)/4)$ with $n=(4m-\rho)d$".  A precise lemma should state:
  \[
  \frac1H\sum_{d\sim D} K_H\!\Bigl(\frac{X/d+\rho}{4}\Bigr) \ll_\epsilon X^{1/4+\epsilon},
  \]
  with a short proof that the congruence restriction on $m$ does not increase the divisor count beyond $2\tau(n)$.  This is elementary but should be explicit.

* **Divisor-bound uniformity.**
  The use of $\tau(n)\ll_\epsilon n^\epsilon$ in a sum over $n\asymp X$ is standard, but one must note that the implied constant in $\ll_\epsilon$ may depend on $\epsilon$; the final $X^\epsilon$ absorbs it.  A clean write-up will state: for any $\epsilon>0$, there exists $C(\epsilon)$ such that $\tau(n)\le C(\epsilon)n^\epsilon$ for all $n\ge1$.  Then the sum $\sum_{n\asymp X}\tau(n)\min(1,\Delta^2/|X-n|^2)\le C(\epsilon)X^\epsilon\sum_{n} \min(1,\Delta^2/|X-n|^2) \ll C(\epsilon)X^\epsilon\Delta$.  This requires that the $n$-range is $O(X)$, which is true because $md\asymp X$.  Good.

* **Non-negativity of the dyadic partition.**
  The proof uses $|w_D(d)|\le 1$; if the smooth dyadic partition includes complex-valued weights, the bound still holds with absolute values.  If the weight is allowed to be larger than $1$ on the overlap, the constant must be adjusted but does not affect the exponent.

* **Integration of R5 into the full proof skeleton.**
  The gpt correctly states that R5 implies H5r-F.  However, the full residual over all dyadic blocks, both signs of $k$, and the zero-mode must be explicitly summed.  The logarithmic number of blocks introduces $O(\log X)$ which is absorbed in $X^\epsilon$.  This needs a short bridging lemma.

### 3.2 Gemini's bounded-variation penalty for parity

Gemini claims that the odd-indicator $1_{2\nmid d}$ has $O(D)$ jumps and therefore violates Li--Yang's bounded-variation hypothesis if inserted directly as $G(m/M)$.
While technically correct, the gpt audit already removes the need to use Li--Yang on the residual, so this point loses its force.  Nevertheless, it should be recorded as a caution: **if** someone later attempts to feed $S_{\mathrm{odd}}$ into Li--Yang, they must first substitute $d=2m+1$ to restore continuity of the coefficient.  The substitution is possible and does not alter the essential difficulty, but the bounded-variation remark is not a fundamental obstruction.

### 3.3 Gemini's claim that "Li--Yang's hypotheses strictly cap ... mathematically cannot evaluate"

The wording "mathematically cannot evaluate" is slightly too strong.  The theorem as currently proved contains parameter restrictions; it does not prove that **no** Bombieri--Iwaniec argument could ever be extended to larger $H$.  A better formulation is: "the Li--Yang (2023) theorem, in its published form, imposes an upper bound $H\le M T^{-49/164}$ (Case A) or $H\le M^{35/69}T^{-2/23}$ (Case B); at the endpoint $M\asymp X^{1/2}$ these bounds are $X^{0.2012}$ and $X^{0.1666}$, respectively, and therefore the theorem cannot be invoked for the Vaaler height $H_D\asymp X^{1/4}$.  Whether a future generalisation could relax these bounds is an open research question, but no such theorem currently exists."  This qualifier prevents a false claim of absolute impossibility.

### 3.4 Mellin--Perron boundary transitions

The H10-M sketch assumes the stationary-phase analysis on the vertical contour dominates the integral.  In practice, the transition near the truncation cutoff $|t|\approx T$ (incomplete Gamma functions) and the possible contributions from horizontal segments after contour shifting must be checked.  The gist of the argument is standard, but before H10-M is entered as a lemma, a careful statement with error terms should be provided.  Until then, it remains a diagnostic.

### 3.5 C3-Mult even-dilation case

Gemini states that even dilations might preserve the sign but are not useful because they do not reduce the degree of the phase.  The claim about phase degree is plausible but not proved in the output; a more detailed analysis of the transformed phase under even multiplicative shifts would be needed to make this a rigorous obstruction lemma.  Currently it is a heuristic.

---

## 4. Possible errors or hidden assumptions

### 4.1 R5: Are we majorising away useful cancellation?

The residual bound uses the absolute-value form $|R_H(t)|\le \frac{C}{H}K_H(t)$, which is a **positive majorant**.  If the actual residual $R_H(t)$ takes both positive and negative values, summing the absolute kernel over a dyadic block might overestimate the total error.  However, an absolute upper bound on $P(X)$ is sufficient for proving $P(X)\ll X^{1/4+\epsilon}$; we do not need a sharp estimate, only an upper bound.  Therefore using a positive majorant is safe -- it may give a looser constant but does not falsify the desired inequality.  The only risk is if the constant $C$ is extremely large, but it is absolute (e.g. $1/(2H+2)$) and cannot break the power saving.

### 4.2 R5: Double-counting when $m_d$ is not unique

If $X/d$ is exactly halfway between two integers, there are two nearest integers.  The bound $\|X/d\|=1/2$ then $\min(1,\Delta^2/\|t\|^2)$ works with either choice, and both choices lead to the same $|X-md| = d/2$.  When summing over $d$, pairing both possibilities could artificially double the sum.  This is harmless because it at most doubles the constant, still absorbed into $X^\epsilon$.  The rigorous proof can avoid ambiguity by selecting the smaller $m$ (or any deterministic tie-break), and the bound still holds because $\|X/d\|\le |X-md|/d$ for any integer $m$; picking the nearest integer makes the inequality $\|X/d\| \le |X-md|/d$ true with equality up to the constant $1/2$?  Actually, $\|t\|$ is the distance to the nearest integer, so if $m$ is one of the two nearest integers, $|X/d - m|$ is either $\|X/d\|$ or $1-\|X/d\|$?  Wait: if $X/d = 5.5$, then distance to nearest integer $5$ is $0.5$, and to $6$ is $0.5$.  So both give $|X-md|=d/2$.  The inequality $\|X/d\| \le \frac{|X-md|}{d}$ is always true because $\|X/d\| = \min_{m\in\mathbb Z}|X/d - m|$.  So picking any integer $m$ gives $|X-md|/d \ge \|X/d\|$.  In the Fejer bound we use $\|X/d\|$, not $|X-md|/d$ directly.  The gpt argument uses $\|X/d\|\asymp |X-md|/d$ relying on the fact that for the nearest integer $|X-md| \le d/2$, so $\|X/d\| = |X-md|/d$.  That's correct.  If there are two nearest integers, both give the same value $|X-md| = d/2$, which is not "close" but it's not a problem because the Fejer kernel is large there anyway.  So no hidden error.

### 4.3 R5: The assumption that $d$ and $m$ are interchangeable with divisor pairs

When $d$ runs over a dyadic block, $m$ runs over integers around $X/D$.  For a given $n$, the number of representations $n=md$ with $d\sim D$ and $m$ an integer is bounded by $\tau(n)$, but we must also ensure that $m$ is the nearest integer to $X/d$ for that $d$.  However, in the sum we are free to choose $m$ as the nearest integer; for each $d$ we get a unique $m=m(d)$.  Then the map $d\mapsto n = m(d)d$ is many-to-one.  For each $n$, the set of $d$ such that $m(d)d=n$ is a subset of the divisors of $n$, hence of size $\le \tau(n)$.  So the inequality $\sum_{d} f(d) \le \sum_n \tau(n) \max$?  Actually we have $\sum_d \min(1,\frac{\Delta^2}{|X-m(d)d|^2}) = \sum_n \bigl( \sum_{d: m(d)d=n} \min(1,\frac{\Delta^2}{|X-n|^2}) \bigr) \le \sum_n \tau(n) \min(1,\frac{\Delta^2}{|X-n|^2})$.  This is valid.  The fact that $m(d)$ is not arbitrary but the nearest integer does not matter; we only need the bound, not equality.

### 4.4 Gemini's bounded-variation comment: potential confusion

Gemini says: "the parity indicator ... inflates the error bound by $O(D)$".  Actually, if one tries to apply Li--Yang's theorem with $G(d/D)=1_{2\nmid d}$, the theorem's proof would break because the Poisson summation step requires control of the Fourier transform; the indicator's many jumps produce large Fourier tails.  However, the theorem's hypothesis "$G$ is of bounded variation" is a sufficient condition; if the total variation of $G$ is $V$, then the error term usually involves $V$.  For $1_{2\nmid d}$ on interval $[M,2M]$, the total variation is $O(M)$, which is huge, so the bound would be too weak.  So indeed, using the indicator directly is invalid.  The resolution (substituting $d=2m+1$) absorbs the parity into the domain; the coefficient becomes $w_D(2m+1)$, which is smooth.  The phase becomes $F_{2,1}(x)= \frac{1}{2x+1/D}$ which is smooth.  So the theorem could then be applied.  Thus the "penalty" is not fatal; it just forces a change of variable.  Gemini's formulation might give the impression that the residuals cannot be evaluated at all, which is not true.  I will note this nuance in the review.

### 4.5 The claim that $X^{1/4}$ is an "endpoint" relative to Li--Yang

The gpt output says "Li--Yang's final range ... is far below the endpoint height".  The phrasing "endpoint" might be misinterpreted as "Li--Yang cannot handle any sum with $H$ that large".  But Li--Yang's theorem is designed for a specific parameter regime; it is possible that a different configuration of the Bombieri--Iwaniec machinery (e.g., different choice of $N$, $q$, or even a different decomposition) could extend the range.  However, the bound $H\le M T^{-49/164}$ is derived from the structure of the second spacing problem and the choice of $q$-ranges in their optimisation; it seems deeply embedded.  So the obstruction is strong, but it's still a theorem-specific restriction, not an absolute mathematical law.  The review should reflect this nuance.

---

## 5. Suggested synthesis

The most important outcome of Round 9 is the **potential elimination of the residual bottleneck** via R5.  The research direction should therefore shift:

**Previous state:**
The Vaaler residual H5r-F was considered the central hard target; every path seemed to require either Li--Yang-type reciprocal-sum estimates (not available at the endpoint) or a sign-preserving truncation (undemonstrated).  This created a gloomy outlook.

**Post-R5 state:**
If R5 is verified, then the fixed-Fejer residual can be bounded by a simple divisor-product argument, without any high-powered exponential-sum technology.  Consequently, the residual ceases to be the bottleneck.  The proof skeleton then depends **only** on:

* H1--H3 (balanced sawtooth reduction) -- already proved;
* H4 (finite Vaaler with Fejer majorant) -- reference check needed;
* R5 (product-counting for the residual) -- to be written rigorously;
* The **main Vaaler sums** H5a/H5b with exact coefficients -- the new central unsolved problem.

The main sums now become the sole analytic obstacle.  They have the form
\[
S_1 = \sum_{1\le|h|\le H_D} \alpha_h \sum_{d\sim D} \chi_4(d) w_D(d) e(hX/d),
\qquad
S_2 = \sum_{1\le|h|\le H_D} \alpha_h \chi_4(h) \sum_{d\sim D} w_D(d) e(hX/(4d)),
\]
with $H_D\asymp D X^{-1/4}$, $X^{1/4}\le D\le X^{1/2}$, and $|\alpha_h|\ll 1/|h|$.  The earlier arbitrary-coefficient targets H5a-B / H5b-B are **not required**; they should be retained only as stress-test norms.  The proof can aim for estimates that exploit the specific $\alpha_h$ decay and, if possible, the arithmetic of $\chi_4$, without having to control worst-case coefficients.

The Li--Yang theorem remains relevant **only** for the lower part of the $h$-range (perhaps $h\lesssim D X^{-0.3145}$) where it may be legally applied, but the high-frequency part $h\in [D X^{-0.3145}, D X^{-1/4}]$ needs a new idea -- possibly signed Bombieri--Iwaniec matrices incorporating Q1-Ext, or a B-process-first dualisation that avoids the A-process collapse (H7) while still giving some spacing gain.

**Synthesis proposal:**

1. **Promote R5** to a "proposed lemma, pending rigorous write-up and numerical validation".
2. **Downgrade H5r-F** from central bottleneck to "resolved conditional on R5".
3. **Rewrite H5a/H5b** as fixed-coefficient targets (call them H5a-fix, H5b-fix).
4. **Formalise the Li--Yang domain obstruction** (N2-Audit) as a permanent guardrail lemma, combined with the gpt L9.1.
5. **Keep the Mellin--Perron and signed Fourier truncation** as comparison routes, but do not allow them to distract from the main-sum challenge.
6. **Update the best proof draft** to reflect this new dependency tree.

---

## 6. Lemma / claim boxes (for auditing)

**Lemma R5 (Fejer-product residual bound).**
*Hypotheses:* $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, $H\asymp D X^{-1/4}$, $w_D$ a dyadic weight with $|w_D(d)|\le1$, $K_H(t)=\sum_{|k|\le H}(1-\frac{|k|}{H+1})e(kt)\ge0$, and the Vaaler residual satisfies $|R_H(t)|\le \frac{C}{H}K_H(t)$ for some absolute $C$.
*Conclusion:* $\frac1H \sum_{\substack{d\sim D\\2\nmid d}} |w_D(d)| K_H(X/d) \ll_\epsilon X^{1/4+\epsilon}$, and similarly for the shifted kernel $K_H((X/d+\rho)/4)$, $\rho=1,3$.
*Status:* Proposed; sketch given, full proof needs exact constant and rigorous divisor-sum estimate.

**Lemma N2-Audit (Li--Yang domain clash).**
*Statement:* In the Li--Yang (2023) exponential-sum theorem, the hypothesis includes $H\le M T^{-49/164}$ (Case A) or $H\le M^{35/69}T^{-2/23}$ (Case B).  For $M\asymp X^{1/2}$ and $T=X$, these force $H\le X^{0.2012}$ and $H\le X^{0.1666}$, respectively. The Vaaler endpoint $H\asymp X^{1/4}=X^{0.25}$ violates these bounds; hence the theorem cannot be applied to the full Vaaler frequency range without a new proof.  *Status:* Proved source-audit conclusion.

**Lemma L9.1 (Li--Yang non-import for residual).**
The Vaaler residual H5r-F/B/L1 cannot be directly deduced from Li--Yang (2023) because (i) the required $H$-range exceeds the theorem's domain, (ii) the theorem's exponent $\theta^*>1/4$, and (iii) the theorem's weight hypotheses (bounded variation) do not cover arbitrary coefficients or termwise $L^1$ norms.  *Status:* Proved from source.

**Lemma C3-Mult (Multiplicative parity collapse).**
In the two-coset dual, $\sigma(\xi)=\frac12(-1)^{2\xi}$.  For an integer $a$, $\sigma(\xi)\sigma(a\xi)=\frac14(-1)^{2\xi(1+a)}$.  If $a$ is odd, $2\xi(1+a)$ is an even integer for all $\xi\in\frac12\mathbb Z$; hence the product is identically $1/4$.  Thus odd-dilation differencing erases parity signs.  *Status:* Proved algebraic diagnostic.

**Lemma H10-M (Mellin--Perron dual length).**
For the smoothed Perron integral of $4\zeta(s)L(s,\chi_4)$ with truncation height $T\asymp X^{3/4}$, shifting the contour and applying Stirling's formula localises the active dual variable to $N\asymp X^{1/2}$ and yields a Voronoi/Bessel phase $2\pi\sqrt{nX}$.  Hence the Mellin--Perron route does not avoid the fundamental reciprocal-sum difficulty.  *Status:* Diagnostic scaling argument; explicit kernel and transition estimates needed for full lemma.

---

## 7. Failure modes (explicit enumeration)

1. **R5 fails because the Vaaler majorant constant is too large or not of the simple Fejer form.**
   If the actual Vaaler theorem in H4 uses a different kernel (e.g., a Dirichlet kernel with worse pointwise bound), the product-counting argument might need adjustment.  However, the Fejer-kernel form is standard for Cesaro means; as long as the majorant is still a non-negative kernel with $K_H(t)\ll \min(H, 1/(H\|t\|^2))$, the method works.

2. **R5 underestimates the influence of the second-leg difference.**
   The bound uses $|R_H(t_1)-R_H(t_2)|\le |R_H(t_1)|+|R_H(t_2)|$, which is safe.  If the two residuals cancel partially, the bound might be slightly weaker, but still a valid upper bound.  The $X^{1/4}$ target is unaffected.

3. **The divisor-bound argument implicitly assumes $n$ ranges over integers near $X$, but $m_d$ might be chosen such that $|X-m_d d|$ is not $|X-n|$ because $n=m_d d$ but $m_d$ may not be the integer nearest to $X/d$ in the strict sense?**  Already addressed: choosing the nearest integer ensures $\|X/d\| = |X-m_d d|/d$.  If there is a tie, either $m$ gives the same distance; the product $n$ may differ, but then $|X-n|$ is the same.  So the mapping to $n$ is well-defined up to a harmless finite multiplicity.  The argument remains valid.

4. **The main Vaaler sums H5a-fix cannot be estimated by any known method, and the entire route stalls.**
   This is not a failure of R5, but of the overall proof strategy.  The gpt output acknowledges that the main sums are the remaining hard problem, and that Li--Yang cannot cover the full range.  So this is a known gap, not a hidden error.

5. **Over-reliance on Li--Yang's domain bound may obscure the possibility that the same method could be adapted to larger $H$ by a different choice of $N$ or $Q$.**
   The Bombieri--Iwaniec framework has many adjustable parameters.  It is conceivable that a future paper could extend the range, but until such a paper exists, it is fair to say the current theorem is inapplicable.  The repo should record this as a "theorem-domain obstruction", not a "mathematical impossibility".

6. **C3-Mult's even-dilation case might be exploited in a way Gemini did not consider.**
   This is a theoretical possibility, but Gemini already notes that even dilations do not lower the phase degree, so they are unlikely to yield a spacing gain.  This remains an open sub-question, but not a high-risk failure for the current route.

---

## 8. Concrete stress tests (numerical)

1. **R5 Fejer-product simulation.**
   Write a small script that, for $X$ in a range (e.g., $10^6$ to $10^8$), computes
   \[
   R_F(D) = \frac{1}{H_D} \sum_{d\sim D} K_{H_D}(X/d)
   \]
   (with $H_D = \lfloor D X^{-1/4}\rfloor$, using the explicit Fejer kernel) and compare with $X^{1/4}$.  Do this for several $D$ values, including $D\approx X^{1/2}$, and for $X$ both square and non-square.  Check that the ratio $R_F(D)/X^{1/4}$ does not grow with $X$.

2. **Spike test near rational $X/d$.**
   For a fixed $X$, choose $d$ such that $X/d$ is extremely close to an integer (e.g., $X$ divisible by $d$).  Evaluate $K_H(X/d)$ termwise and see if the product-counting bound is tight or if the positive kernel causes an unexpectedly large contribution from many divisors.  This tests the divisor-bound pessimisation.

3. **Second-leg residual example.**
   Compute the average of $K_H((X/d+\rho)/4)$ over $d$ for a moderate $X$ and verify the bound numerically; pay special attention to $\rho$ that cause alignment with integers.

4. **Abel-summation diagnostic for H5r-F.**
   To test the strength of Fejer averaging versus $L^1$, compute
   \[
   L_1 = \frac1H\sum_{k}|S_\star(k,D)|,\qquad
   A_F = \sum_{k}\eta_{k,H}S_\star(k,D)
   \]
   for a model sum and see if $A_F$ is significantly smaller.  This can inform whether the fixed-Fejer target is genuinely weaker, as suggested by the odd-indicator example $a_k=(-1)^k$.

---

## 9. Confidence calibration and failure modes

* **Confidence in R5 as a correct bound:**
  **High** -- provided the Fejer-kernel majorant is correctly stated.  The product-counting method is elementary and robust; the divisor bound is a well-known theorem.  I see no fatal flaw.

* **Confidence that R5 eliminates H5r-F as a bottleneck:**
  **Moderate-to-High** -- the argument appears to directly bound the fixed-Fejer residual at the required scale.  Once the proof is written and checked against H4, this should be secure.  The only risk is an unforeseen constant factor that leaves a logarithmic loss, but $X^\epsilon$ can absorb logarithms.

* **Confidence that the Li--Yang theorem cannot be applied to the endpoint Vaaler range:**
  **High** -- the source code explicitly contains the parameter restrictions; the numerical violation is clear.  This should be recorded as a permanent lemma.

* **Confidence that the main Vaaler sums are the sole remaining obstacle:**
  **Moderate** -- after the residual is removed, the proof reduces to estimating those sums.  However, it is still possible that the Vaaler main-term decomposition introduces other technical issues (e.g., handling the dyadic partition of the range $D<X^{1/4}$, or the $O(1)$ term from H3).  Those are likely manageable.  The central difficulty is indeed the main reciprocal sums with $\chi_4$.

* **Confidence that the signed Fourier or Mellin--Perron routes provide an alternative:**
  **Low** -- both appear to reproduce the same fundamental obstacles.  They may serve as comparison diagnostics, but not as present proof strategies.

* **Overall confidence that Round 9 has improved the proof status:**
  **High** -- the residual bottleneck is much better understood and plausibly resolved.  This does not yet prove the conjectural bound, but it sharply focuses the effort.

---

## 10. Score by agent

| Agent reviewed        | Score (0--10) | Main reason | Must verify next |
|-----------------------|--------------|-------------|------------------|
| `gpt_pro_thinking`    | 9 | Provides the breakthrough R5 lemma that could remove the central residual bottleneck; precise Li--Yang audit; correct norm correction for H5a/H5b.  Clear, well-structured, and mathematically sound. | Full rigorous proof of R5 (product-counting steps, exact Vaaler majorant reference), numerical stress tests. |
| `gemini_deep_think`   | 7.5 | Supplies a sharper Li--Yang domain obstruction (Case A/B), a useful Mellin--Perron diagnostic, and new parity-collapse lemmas.  However, some statements slightly overstate impossibility and the bounded-variation penalty is not a fundamental barrier.  Less constructive than gpt on the main forward path. | Exact parameter bound extraction from source; clarify that even-dilation case is not proved impossible. |

**Score justification:**

* `gpt_pro_thinking` receives a high score because the R5 idea is genuinely original within the context of this multi-round research log, and if verified, it simplifies the problem dramatically.  The audit and norm recalibration are also useful.  The only minor deduction is for not fully expanding the residual transformation for the second leg, but the sketch is sufficient for Stage A.

* `gemini_deep_think` provides valuable confirmatory analysis, but its constructive forward-moving content is less impactful.  The Li--Yang domain analysis is a refinement of the gpt audit, but it is essentially a deeper investigation of the same obstruction.  The Mellin--Perron equivalence is useful but already conjectured in earlier rounds.  The parity-collapse lemmas are nice algebra but do not currently open a new avenue.  The slight overstatement of impossibility detracts from precision.  Nonetheless, solid work, earning a 7.5.

---

## 11. Next-round recommendation

The next round should focus on **consolidating the residual resolution and attacking the main sums**.  Specific tasks:

1. **For `gpt_pro_thinking`:**
   - Write a complete, rigorous proof of R5, including the exact Fejer-kernel constants, the handling of the second-leg shifts, and the divisor-bound summation.
   - Insert R5 into the best proof draft and explicitly demote H5r-B/L1 to optional stress-test norms.
   - Formulate the fixed-coefficient main-term targets (H5a-fix, H5b-fix) with the actual Vaaler coefficients $\alpha_h$ and the required ranges.
   - Compare these targets with Li--Yang's theorem for the sub-range where it applies ($H\le D X^{-0.3145}$) and identify the uncovered high-frequency gap $H\in [D X^{-0.3145},\, D X^{-1/4}]$.

2. **For `deepseek_api` (this agent):**
   - Run the numerical stress tests proposed in Section 8 to gain empirical confidence in R5.
   - Independently verify the Li--Yang domain constraints from the uploaded TeX source and compare with the range needed for the main sums.
   - Algebraically audit the candidate main-sum estimates: can residue-splitting plus Weil/Deligne complete sums give any saving in the high-frequency region?  Check if the character $\chi_4$ can be used through a finite field extension (e.g., Gaussian integers) to create a genuine complete character sum.

3. **For `gemini_deep_think`:**
   - Soften the impossibility rhetoric where appropriate.
   - Develop a more precise lemma for the Mellin--Perron route with explicit error terms.
   - Analyse whether the even-dilation case in C3-Mult can be turned into a spacing matrix that preserves sign and yields some cancellation; if impossible, explain the technical obstruction (e.g., the phase Hessian remains degenerate).
   - Examine the possibility of a "hybrid" method that applies Bombieri--Iwaniec spacing to the main sums with the exact coefficients and uses Q1-Ext signs to improve matrix norm bounds.

4. **General:**
   - Update the lemma bank and gap register to reflect the new status.
   - Keep the Poisson--Bessel calibration module as a secondary sanity check, but do not let it distract from the main arithmetic route.

**End of Review**

## Required Output Schema

Selected main route:
Useful fragments by source:
Rejected or risky ideas:
Known gaps:
New lemmas to add:
Counterexample checks to run:
Next round instructions:
Confidence:
