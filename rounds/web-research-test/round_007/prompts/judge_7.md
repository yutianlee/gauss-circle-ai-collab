You are the judge agent: GPT Pro Thinking.

Synthesize Round 7. Prefer precise, checkable progress over impressive prose.

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

Generated after round 6 in run `web-research-test`.

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

Responses, reviews, and judge synthesis are archived under `rounds/web-research-test/round_006/`.

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

--- RECENT HUMAN NOTE: human/inbox/20260531-212136_constraint_web-model-modes-and-conversation-policy.md ---
# Web model modes and conversation policy

Kind: constraint
Timestamp: 2026-05-31T21:21:36

For web-agent tests and formal rounds, use ChatGPT Extended Pro for gpt_pro_thinking and Gemini Pro Deep Think for gemini_deep_think. Prefer one persistent conversation per agent per run, so each web AI has continuity across reasoning, review, judge/next-round prompts. The public repo and reading_packet.md remain the authoritative memory; web conversation memory is helpful but not authoritative.

## Agent Responses

--- RESPONSE FROM gpt_pro_thinking ---
Summary:

Source anchors: Round 6 packet and current state bundle from the uploaded prompt:. Uploaded background survey used only as non-proof background:. For the Vaaler dependency, the next repo audit should verify the exact theorem against Vaaler's original paper; a reference note points to Vaaler's "Some Extremal Functions in Fourier Analysis", Bull. AMS 12(2), 1985, pp. 183--216, beginning around p. 206, and records a representative Vaaler polynomial/Fejer-kernel formulation.

This is a Round 7 Stage A independent-reasoning packet for `gpt_pro_thinking`.

No new exponent for the Gauss circle problem is proved here. The main contribution is a precise norm-level theorem for the Vaaler residual H5r, a corrected conditional C1 diagnostic, a convention-fixed Poisson formula for the odd-lattice residual C2, and a comparison of Vaaler, signed Fourier truncation, and Mellin--Perron alternatives.

The principal conclusion is:

H5r-F is the minimal fixed-Fejer residual estimate naturally required by the current Vaaler proof. H5r-B is a stronger sufficient estimate; in the stated arbitrary-coefficient form it is essentially equivalent to a dyadic termwise $L^1$ estimate by duality. H5r-F is enough to make the Vaaler residual $O_\epsilon(X^{1/4+\epsilon})$ after summing dyadic denominator blocks, but H5r-F itself is an endpoint-strength reciprocal-sum input and remains unproved.

Main claim or direction:

The next proof draft should record the following dependency chain as a theorem schema:

$$
\text{H5r-B} \Longrightarrow \text{H5r-F} \Longrightarrow
\text{Vaaler residual contribution} \ll_\epsilon X^{1/4+\epsilon}.
$$

The fixed-Fejer target H5r-F is the correct minimum target for the current positive-majorant Vaaler route. The arbitrary bounded coefficient target H5r-B is convenient for comparison with bilinear or Bombieri--Iwaniec/Li--Yang-type estimates, but it is stronger than the proof strictly needs.

The conditional C1 diagnostic should be recorded in the corrected form:

If the only available estimates for H5r are character-blind reciprocal-sum estimates with exponent $\theta$, normalized as

$$
\sum_{k\sim K_0} v_k S_\star(k,D)
\ll_\epsilon
K_0 X^{\theta+\epsilon},
$$

then the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs, assuming the main Vaaler families H5a and H5b are already controlled at the conjectural scale. This is not a lower bound and not an impossibility theorem.

The C2 odd-lattice Poisson transform is valid, but only as a transformation lemma. The alternating dual coefficient $(-1)^m$ appears under one convention, while an equivalent two-coset formulation also exists. Therefore C2/C3 should remain diagnostic, not a proved obstruction.

Detailed reasoning:

## 1. Baseline arithmetic identity

Retain the proved floor-compatible reduction:

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
\psi(t)=t-\lfloor t\rfloor-\frac12,
\qquad
e(t)=e^{2\pi i t}.
$$

This identity is an arithmetic/floor identity, not a Fourier identity. The endpoint convention is

$$
\psi(n)=-\frac12
\qquad
(n\in\mathbb Z).
$$

The Vaaler step must therefore be treated as an approximation to this floor-compatible sawtooth, with its residual retained.

## 2. Vaaler input used in the proof skeleton

Use the following theorem dependency, pending exact reference audit.

For every integer $H\ge 1$, there is a trigonometric polynomial

$$
A_H(t)=\sum_{1\le |h|\le H}\alpha_{h,H}e(ht),
\qquad
\alpha_{h,H}\ll \frac1{|h|},
$$

such that

$$
\psi(t)=A_H(t)+R_H(t)
$$

and

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t),
$$

where the Fejer kernel is

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

Write

$$
\eta_{k,H}=1-\frac{|k|}{H+1}.
$$

Then

$$
K_H(t)=
1+\sum_{1\le |k|\le H}\eta_{k,H}e(kt).
$$

This is the exact point where the positive majorant loses the original $\chi_4$ sign structure in the residual.

## 3. Dyadic localization and local height

Insert a smooth nonnegative dyadic partition of unity in the denominator variable. Let $w_D$ be supported on $d\asymp D$, with

$$
X^{1/4}\le D\le X^{1/2}.
$$

Use the local Vaaler height

$$
H_D\asymp D X^{-1/4}.
$$

For $D<X^{1/4}$, the sawtooth sums have length $O(D)$, so their total contribution over all short dyadic blocks is

$$
\ll X^{1/4+\epsilon}
$$

by trivial estimation and dyadic summation. Thus H5r is only needed for

$$
X^{1/4}\le D\le X^{1/2}.
$$

## 4. First-leg residual and H5r-F

The first leg is

$$
-4\sum_d \chi_4(d) w_D(d)\psi(X/d).
$$

After Vaaler,

$$
\psi(X/d)=A_{H_D}(X/d)+R_{H_D}(X/d).
$$

The residual contribution is bounded by

$$
\sum_d |\chi_4(d)|w_D(d)|R_{H_D}(X/d)|.
$$

Since

$$
|\chi_4(d)|=1_{2\nmid d},
$$

the Fejer majorant gives

$$
\sum_d |\chi_4(d)|w_D(d)|R_{H_D}(X/d)|
\ll
\frac1{H_D}
\sum_{\substack{d\\2\nmid d}}w_D(d)K_{H_D}(X/d).
$$

Define

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\\2\nmid d}}w_D(d)e(kX/d).
$$

Then the residual is bounded by

$$
\frac1{H_D}
\left[
S_{\mathrm{odd}}(0,D)
+
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_{\mathrm{odd}}(k,D)
\right].
$$

The zero mode is

$$
\frac1{H_D}S_{\mathrm{odd}}(0,D)
\ll
\frac{D}{H_D}
\asymp
X^{1/4}.
$$

Therefore the required nonzero-mode fixed-Fejer target is:

**H5r-F, first leg.** For every dyadic $D$ in the local range,

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_{\mathrm{odd}}(k,D)
\right|
\ll_\epsilon
X^{1/4+\epsilon}.
$$

This is exactly sufficient for the first-leg residual.

## 5. Second-leg residual and H5r-F

The second leg is

$$
4\sum_d w_D(d)
\left[
\psi\left(\frac{X/d+1}{4}\right)
-
\psi\left(\frac{X/d+3}{4}\right)
\right].
$$

The main Vaaler polynomial keeps the frequency-character transfer

$$
e(h/4)-e(3h/4)=2i\chi_4(h).
$$

The residual does not keep this signed transfer if we use the pointwise majorant. Instead,

$$
\left|
R_{H_D}\left(\frac{X/d+\rho}{4}\right)
\right|
\le
\frac1{2H_D+2}
K_{H_D}\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\}.
$$

Define

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_d w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

Then the second residual is bounded by zero modes of size

$$
\ll D/H_D\asymp X^{1/4}
$$

plus the two fixed-Fejer nonzero sums

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\rho(k,D)
\right|.
$$

Thus:

**H5r-F, second leg.** For $\rho\in\{1,3\}$,

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\rho(k,D)
\right|
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Together, the first- and second-leg H5r-F estimates imply that the full Vaaler residual over one dyadic denominator block is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Summing over $O(\log X)$ dyadic blocks gives

$$
\ll_\epsilon X^{1/4+\epsilon}
$$

after absorbing logarithms into $X^\epsilon$.

## 6. H5r-B implies H5r-F

State the stronger arbitrary bounded dyadic target:

**H5r-B.** For every dyadic $K_0\le H_D$, every $|v_k|\le 1$, and each residual family $S_\star\in\{S_{\mathrm{odd}},S_1,S_3\}$,

$$
\sum_{k\sim K_0} v_k S_\star(k,D)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

Then decompose

$$
1\le |k|\le H_D
$$

into dyadic blocks $K_0$. On each block, take

$$
v_k=\eta_{k,H_D}
$$

or the corresponding phase-adjusted bounded coefficient. Since $|\eta_{k,H_D}|\le 1$,

$$
\sum_{k\sim K_0}\eta_{k,H_D}S_\star(k,D)
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

Therefore

$$
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\ll_\epsilon
\frac1{H_D}
\sum_{K_0\le H_D}K_0X^{1/4+\epsilon}
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Hence

$$
\text{H5r-B}\Longrightarrow\text{H5r-F}.
$$

## 7. Relation between H5r-B and H5r-L1

There are two possible meanings of H5r-L1, and the repo should distinguish them.

### Global fixed-range H5r-L1

If one assumes only

$$
\frac1{H_D}
\sum_{1\le |k|\le H_D}|S_\star(k,D)|
\ll_\epsilon
X^{1/4+\epsilon},
$$

then this directly implies H5r-F by the triangle inequality. It does not automatically imply the dyadic arbitrary-coefficient estimate H5r-B for every sub-block $K_0$ unless the same estimate is available locally on each dyadic interval.

### Dyadic H5r-L1

If one assumes, for every $K_0\le H_D$,

$$
\sum_{k\sim K_0}|S_\star(k,D)|
\ll_\epsilon
K_0X^{1/4+\epsilon},
$$

then it is equivalent to H5r-B up to constants. Indeed:

- dyadic H5r-L1 implies H5r-B by the triangle inequality;
- H5r-B implies dyadic H5r-L1 by choosing

$$
v_k=
\begin{cases}
\overline{S_\star(k,D)}/|S_\star(k,D)|,&S_\star(k,D)\ne0,\\
0,&S_\star(k,D)=0.
\end{cases}
$$

Thus, in the arbitrary bounded coefficient formulation, H5r-B is not meaningfully weaker than dyadic termwise $L^1$. It is stronger than the fixed-Fejer target H5r-F.

This matters because a proof of H5r-F may exploit the exact Fejer coefficients and possible cancellation between $k$-frequencies. A proof of H5r-B cannot exploit that fixed coefficient structure.

## 8. Corrected C1 diagnostic

Assume the main Vaaler families H5a and H5b are controlled at the target scale:

$$
B_i(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon},
\qquad i=1,2.
$$

Assume also that the only available residual input is a character-blind reciprocal estimate with exponent $\theta$:

$$
\sum_{k\sim K_0}v_kS_\star(k,D)
\ll_\epsilon
K_0X^{\theta+\epsilon}
$$

for each residual family $S_\star$.

Then the same proof as above gives

$$
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\ll_\epsilon
X^{\theta+\epsilon}.
$$

The zero mode contributes

$$
D/H_D\asymp X^{1/4}.
$$

Therefore the Vaaler residual is controlled by

$$
X^{\max(1/4,\theta)+\epsilon}.
$$

Consequently the whole route gives, from these inputs,

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}.
$$

This is the corrected C1 statement. The incorrect product-like scaling $X^{1/4+\theta}$ should not be used.

## 9. Convention-fixed C2 Poisson formula

Let

$$
F(u)=w_D(u)e(kX/u),
$$

where $w_D$ is smooth and supported on positive $u\asymp D$.

Use the Fourier transform convention

$$
\widehat F(\xi)=\int_{\mathbb R}F(u)e(-\xi u)\,du.
$$

Then

$$
\sum_{d\in\mathbb Z}F(d)
=
\sum_{m\in\mathbb Z}\widehat F(m).
$$

The odd-lattice sum is

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{2\nmid d}F(d).
$$

### Form 1: odd sublattice

Writing $d=2\ell+1$ and applying Poisson in $\ell$ gives

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\in\mathbb Z}
(-1)^m
\int_{\mathbb R}
w_D(u)
e\left(\frac{kX}{u}-\frac{mu}{2}\right)
\,du.
$$

This proves the alternating-factor representation under the stated convention.

### Form 2: integer minus half-integer dual frequencies

Since

$$
1_{2\nmid d}=\frac12(1-e(d/2)),
$$

one also has

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\in\mathbb Z}
\left[
\widehat F(m)-\widehat F(m-1/2)
\right].
$$

Equivalently,

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\in\mathbb Z}
\int_{\mathbb R}w_D(u)e(kX/u)
\left[
e(-mu)-e(-(m-1/2)u)
\right]
\,du.
$$

These two formulas are equivalent by reindexing and Poisson normalization. Therefore the appearance of $(-1)^m$ is real, but it is representation-dependent. It should not be promoted to an unconditional obstruction by itself.

## 10. Stationary phase for C2

For

$$
I_m(k,D)
=
\int_{\mathbb R}
w_D(u)
e\left(\frac{kX}{u}-\frac{mu}{2}\right)
\,du,
$$

the phase is

$$
\phi_m(u)=\frac{kX}{u}-\frac{mu}{2}.
$$

Then

$$
\phi_m'(u)=-\frac{kX}{u^2}-\frac m2.
$$

A stationary point exists only when $m<0$. Write $m=-\ell$, $\ell>0$. Then

$$
u_0=\left(\frac{2kX}{\ell}\right)^{1/2}.
$$

Since $w_D$ is supported on $u\asymp D$, the active dual length is

$$
\ell\asymp \frac{kX}{D^2}.
$$

At the stationary point,

$$
\phi_{-\ell}(u_0)
=
\frac{kX}{u_0}+\frac{\ell u_0}{2}
=
\sqrt{2kX\ell}.
$$

Also,

$$
\phi_{-\ell}''(u_0)
=
\frac{2kX}{u_0^3}
\asymp
\frac{kX}{D^3}.
$$

Thus the expected stationary-phase amplitude is

$$
\asymp
\left(\frac{kX}{D^3}\right)^{-1/2}
=
\frac{D^{3/2}}{(kX)^{1/2}},
$$

up to a smooth amplitude depending on

$$
\frac{\ell D^2}{kX}.
$$

A formal stationary-phase lemma should have the shape

$$
I_{-\ell}(k,D)
=
\frac{D^{3/2}}{(kX)^{1/2}}
a\left(\frac{\ell D^2}{kX}\right)
e\left(\sqrt{2kX\ell}+\frac18\right)
+
\text{lower-order terms},
$$

where $a$ is smooth and supported on a compact subinterval of $(0,\infty)$ determined by $w_D$. The sign of the $1/8$ phase depends on the Fourier and stationary-phase conventions and must be checked before committing.

For $m$ outside the active range, repeated integration by parts should give rapid decay. The boundary regimes remain nontrivial, especially

$$
D\asymp X^{1/2},\qquad k\asymp 1,
$$

where the active dual length is $O(1)$.

## 11. H10: non-majorizing comparison

| Method | Replacement for H5r | What it preserves | Current status |
|---|---|---|---|
| Vaaler with Fejer majorant | Fixed-Fejer residual H5r-F, or stronger H5r-B/H5r-L1 | Pointwise control of sawtooth; loses $\chi_4$ in residual after absolute values | Exact route but central bottleneck |
| Signed Fourier truncation | High-frequency signed tail beyond $H_D$ | May preserve $\chi_4$ or signed cancellation longer | Not yet useful; the tail is not absolutely convergent and may require estimates at larger frequencies |
| Mellin--Perron | Truncation error plus contour integral for $4\zeta(s)L(s,\chi_4)X^s/s$ | Preserves arithmetic Dirichlet-series structure | Standard reformulation; likely leads to moment/subconvexity or Voronoi/Bessel sums |
| Smoothed Perron | Weighted contour integral with faster vertical decay | Preserves arithmetic structure and reduces sharp cutoff error | Gives smoothed discrepancy; unsmoothing may reintroduce boundary losses |
| Poisson--Bessel calibration | Bessel/radial frequency sums | Good normalization and recovery of $R^{2/3}$ | Calibration route, not a new endpoint path |

For Mellin--Perron, the formal sharp cutoff is

$$
\sum_{n\le X}r_2(n)
=
\frac{1}{2\pi i}
\int_{c-iT}^{c+iT}
4\zeta(s)L(s,\chi_4)\frac{X^s}{s}\,ds
+
\text{truncation error},
\qquad c>1.
$$

The pole at $s=1$ gives the main term $\pi X$. To reach

$$
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

one would need either a contour/moment input strong enough after shifting, or a functional-equation/Voronoi transformation whose resulting oscillatory sums are no harder than the original H5 targets. At present this is a comparison route, not an escape.

Dependencies:

1. H1--H3 are used as proved floor-compatible reductions.

2. The Vaaler theorem is used only in the majorant form

$$
|R_H(t)|\le (2H+2)^{-1}K_H(t).
$$

The exact coefficient formula for $\alpha_{h,H}$ is not needed for H5r, but it is needed for the main terms H5a/H5b and should be audited.

3. The dyadic partition should be nonnegative for the clean residual-majorant argument. If signed dyadic partitions are used, the proof must replace $w_D$ by $|w_D|$ in the residual families.

4. The local height

$$
H_D\asymp D X^{-1/4}
$$

is required to make the Fejer zero mode exactly conjectural scale:

$$
D/H_D\asymp X^{1/4}.
$$

5. H5a and H5b are not proved here. The norm theorem only handles the residual implication once the relevant H5r estimate is supplied.

6. The C2 formula depends on the Fourier convention

$$
\widehat F(\xi)=\int F(u)e(-\xi u)\,du.
$$

Changing this convention reverses signs in the dual phase.

Potential gaps:

1. **Exact Vaaler citation.** The repo still needs the precise theorem statement from Vaaler or a standard analytic-number-theory reference. The coefficient formula and majorant normalization should be checked before marking H4 as an imported theorem.

2. **Discontinuity convention.** H3 uses $\psi(n)=-1/2$, while trigonometric approximations encode midpoint behavior through a residual. The proof is safe only if the residual majorant is retained at all discontinuities.

3. **H5r-F may be much easier than H5r-B.** H5r-F has fixed Fejer coefficients. H5r-B permits arbitrary bounded coefficients and is equivalent to dyadic $L^1$. Future estimates should not silently replace H5r-F by H5r-B unless the stronger target is intended.

4. **Absolute-value placement.** The Vaaler residual proof uses pointwise positivity, then one block-level absolute value for the nonzero Fejer sum. Termwise absolute values in $k$ are sufficient but may be too destructive.

5. **C2 obstruction status.** The alternating factor $(-1)^m$ appears, but the two-coset formulation may retain spacing information. C3 is therefore only a diagnostic.

6. **Boundary stationary phase.** The C2 dual length

$$
M\asymp kX/D^2
$$

can be $O(1)$ at the edge $D\asymp X^{1/2}$ and $k\asymp1$. Such cases require separate estimates.

7. **Mellin--Perron may be circular.** The contour route may reproduce Voronoi/Hardy/Bessel sums after the functional equation. This is a diagnostic, not a proof of failure.

8. **Known technology gap.** H5r lies structurally in the reciprocal-sum/divisor-problem class after residue splitting. Existing record exponents do not by themselves provide the endpoint $1/4$ estimate.

Counterexample or obstruction search:

1. **Fejer spike cases.** Test $X,d$ for which

$$
X/d,\qquad
\frac{X/d+1}{4},\qquad
\frac{X/d+3}{4}
$$

is near an integer. These are exactly where $K_H$ can spike and where scalar residual estimates fail.

2. **Fixed Fejer versus arbitrary coefficients.** Numerically compare

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
$$

against

$$
\frac1{H_D}\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

A large separation would indicate that H5r-F is meaningfully weaker than H5r-B/L1.

3. **Odd-lattice Poisson convention check.** Verify directly on compactly supported test functions that

$$
\sum_{2\nmid d}F(d)
=
\frac12
\sum_m(-1)^m
\int F(u)e(-mu/2)\,du
$$

matches

$$
\frac12
\sum_m
\left[
\widehat F(m)-\widehat F(m-1/2)
\right].
$$

4. **C3 two-coset A-process test.** Apply differencing in both C2 representations. Determine whether the two-coset phases retain spacing information that the one-sequence $(-1)^m$ coefficient representation hides.

5. **Stationary-phase constants.** For

$$
I_m=\int w_D(u)e(kX/u-mu/2)\,du,
$$

check the active sign of $m$, the stationary point, the phase constant, and the $e(1/8)$ signature.

6. **H5r-to-Li--Yang audit.** Write $S_{\mathrm{odd}}$ and $S_\rho$ in the exact form required by a candidate Bombieri--Iwaniec/Li--Yang theorem, including weights and absolute-value placement. Do not assume theorem compatibility from phase shape alone.

7. **Signed Fourier tail.** Test whether a signed truncation of

$$
\psi(t)=-\sum_{h\ne0}\frac{e(ht)}{2\pi i h}
$$

after hyperbola cutting produces a controllable high-frequency tail or simply moves H5r to larger $h$.

Useful lemmas:

## Lemma R1. Fixed-Fejer residual sufficiency

Status: proved conditional lemma.

Assume H5r-F for $S_{\mathrm{odd}}$, $S_1$, and $S_3$ on every dyadic denominator block

$$
X^{1/4}\le D\le X^{1/2}.
$$

Then the total Vaaler residual in the balanced sawtooth formula is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

Proof: zero Fejer modes contribute $D/H_D\asymp X^{1/4}$ per block. Nonzero Fejer modes are bounded by H5r-F. There are $O(\log X)$ blocks, absorbed into $X^\epsilon$.

## Lemma R2. Arbitrary bounded coefficients imply fixed Fejer

Status: proved conditional lemma.

H5r-B implies H5r-F.

Proof: dyadically decompose $1\le |k|\le H_D$ and use $v_k=\eta_{k,H_D}$ on each block. Divide by $H_D$ and sum the dyadic lengths.

## Lemma R3. H5r-B and dyadic H5r-L1 equivalence

Status: elementary.

If H5r-B is stated for all complex coefficients $|v_k|\le1$, then it is equivalent to the dyadic termwise $L^1$ estimate

$$
\sum_{k\sim K_0}|S_\star(k,D)|
\ll_\epsilon
K_0X^{1/4+\epsilon}.
$$

The implication from H5r-B to dyadic H5r-L1 follows by choosing $v_k$ to match the phase of $S_\star(k,D)$.

## Lemma C1. Corrected Fejer Majorant DDP diagnostic

Status: conditional diagnostic.

If H5r is bounded only by character-blind reciprocal estimates at exponent $\theta$, then the Vaaler route gives

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs, assuming H5a/H5b are handled at the target scale.

## Lemma C2. Odd-lattice Poisson transform

Status: transformation proved up to Fourier convention.

For

$$
F(u)=w_D(u)e(kX/u)
$$

and

$$
\widehat F(\xi)=\int F(u)e(-\xi u)\,du,
$$

one has

$$
\sum_{2\nmid d}F(d)
=
\frac12
\sum_m(-1)^m
\int F(u)e(-mu/2)\,du
=
\frac12
\sum_m
\left[
\widehat F(m)-\widehat F(m-1/2)
\right].
$$

The stationary range is

$$
|m|\asymp kX/D^2.
$$

## Lemma C3. Dual parity A-process diagnostic

Status: diagnostic only.

In the one-sequence C2 representation, direct differencing of the coefficient gives

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

This shows that the coefficient alone has no nontrivial residual mod-$2$ oscillation under direct A-process. It does not rule out two-coset spacing arguments.

What should be tested next:

1. Commit Lemmas R1--R3 and C1--C3 to the lemma bank with the statuses above.

2. Insert H5r-F, not only H5r-B, into the best proof draft as the minimal residual dependency.

3. Audit the exact Vaaler theorem and record the coefficient formula and majorant normalization.

4. Run numerical H5r norm comparisons for square, nonsquare, and near-square $X$:

$$
\text{fixed Fejer}
\quad \text{vs.} \quad
\text{dyadic arbitrary coefficients}
\quad \text{vs.} \quad
\text{termwise }L^1.
$$

5. Have `gemini_deep_think` focus on the C2 two-coset formulation and whether spacing information survives differencing.

6. Have `deepseek_api` verify the C2 Poisson signs, stationary-phase constants, and boundary regimes, and run the H5r numerical tests.

7. Continue the Mellin--Perron comparison, but do not promote it until its truncation error is shown to be different from H5r or from the standard Voronoi/Bessel difficulty.

Confidence:

High confidence in the implication

$$
\text{H5r-F}\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

High confidence that H5r-B implies H5r-F.

High confidence that arbitrary-coefficient H5r-B is essentially equivalent to dyadic termwise $L^1$ by duality.

High confidence in the corrected C1 normalization

$$
X^{\max(1/4,\theta)+\epsilon}.
$$

Moderate-to-high confidence in the C2 Poisson formula under the stated Fourier convention.

Moderate confidence in the stationary-phase shape and dual length

$$
|m|\asymp kX/D^2.
$$

Low confidence that the Vaaler route reaches the conjectural exponent without a genuinely new endpoint reciprocal-sum estimate for H5r-F or a sign-preserving replacement for the Fejer majorant.

No claim here improves the known Gauss circle exponent.

--- RESPONSE FROM gemini_deep_think ---
Summary:
In response to the Round 6 judge instructions, this Round 7 analysis formally downgrades "continuous exhaustion of Fourier truncations" and the "Voronoi circularity trap" to diagnostic heuristics. To advance the Mellin-Perron route to a formal theorem-dependency level, I explicitly formulate the exact sharp truncation error and determine that bounding the critical-line integral via absolute values strictly blocks the conjectural $X^{1/4+\epsilon}$ endpoint. Reaching the target analytically forces the deployment of the functional equation, which maps the contour integral identically back to dyadic Voronoi/Bessel reciprocal sums of length $X^{1/2}$. Furthermore, I resolve the C3 two-coset dual parity debate: applying Weyl differencing (an A-process) to the dual parity expansion algebraically factors the alternating phase out of the continuous summation entirely, demonstrating that direct differencing destroys the mod-2 spacing advantage. Finally, I execute a rational-collision matrix test on the primal phase $e(kX/d)$. This reveals that the spatial character $\chi_4(d)$ does not randomize on exact rational collisions; instead, it collapses into a uniform block-constant sign $\chi_4(ab)$. This pinpoints the exact locus of character-blindness: the character is discarded not by the rational parameterization itself, but by subsequent absolute-value matrix norms.

Main claim or direction:
The arithmetic hyperbola/Vaaler formulation remains the mandatory structural reduction framework. The Mellin-Perron approach should be retained strictly as an analytic mirror, since avoiding the positive Fejer majorant simply trades the residual for a contour truncation error that reconstructs the exact same reciprocal-sum bottlenecks. The two-coset dual parity route appears analytically sterile under direct differencing. The most promising structural direction is to focus on the Bombieri-Iwaniec rational-collision matrix for the spatial character (H5a). Because $\chi_4$ is preserved as block-constant weights rather than pseudo-random noise, there is a theoretical opening to develop a signed bilinear matrix estimate that avoids trivially bounding the character by absolute values, provided near-collisions maintain this rigid sign structure.

Detailed reasoning:

**1. Diagnostic Downgrades for Continuous Exhaustion**
Per instructions, the "Fejer Majorant DDP Trap" and "Voronoi Circularity Trap" are formally downgraded from impossibility theorems to conditional diagnostic heuristics. They accurately map standard failure modes--specifically that positive pointwise majorants erase signs, and that contour shifting typical Dirichlet series cyclically recovers divisor-problem geometry--but they do not unconditionally rule out bespoke signed finite-truncations or novel offline contour paths.

**2. Mellin-Perron Route: Exact Truncation and T-Scale**
Let $Z(s) = 4\zeta(s)L(s,\chi_4)$. For $X \notin \mathbb{Z}$ and $c = 1+1/\log X$, the sharp truncated Perron formula provides:
$$ \sum_{n \le X} r_2(n) = \frac{1}{2\pi i} \int_{c-iT}^{c+iT} Z(s) \frac{X^s}{s} ds + O_\epsilon\left( \frac{X^{1+\epsilon}}{T} \right). $$
To achieve the Gauss circle target error of $O(X^{1/4+\epsilon})$, bounding the truncation error strictly requires $T \gg X^{3/4-\epsilon}$.

**3. The Critical Line Barrier for Mellin-Perron**
If we shift the contour to the critical line $\Re(s) = 1/2$, the pole at $s=1$ extracts the main term $\pi X$. The absolute value of the remaining integral is bounded by:
$$ \ll X^{1/2} \int_{-T}^T \left| Z(1/2+it) \right| \frac{dt}{1+|t|}. $$
By standard Dirichlet series lower bounds (and even conditionally assuming the Lindelof hypothesis $|Z(1/2+it)| \ll |t|^\epsilon$), this integral is unconditionally bounded below by $\gg X^{1/2}$. Thus, employing absolute-value bounds (like subconvexity) on the critical line fails by a massive margin to reach $X^{1/4+\epsilon}$.

**4. Structural Isomorphism via Functional Equation**
To reach the endpoint, one must integrate the oscillation of $X^{it}$ against the phase of $Z(1/2+it)$. This mathematically necessitates applying the asymmetric functional equation for $Z(s)$, yielding a series of Gamma factors that, under stationary phase, recreate the classical Voronoi/Bessel reciprocal expansion. For truncation height $T \asymp X^{3/4}$, the dual summation length is $N \asymp T^2/X = X^{1/2}$. This precisely matches the dyadic length $D \asymp X^{1/2}$ of the Vaaler residual bottleneck, indicating the two routes are structurally isomorphic.

**5. Two-Coset Parity-Dual A-Process Analysis (C3)**
The odd-lattice Poisson transform of $1_{2 \nmid d}$ yields a dual evaluation on half-integers $\mu = m/2 \in \frac{1}{2}\mathbb{Z}$. The corresponding coefficient is $c_\mu = (-1)^{2\mu}$, which perfectly outputs $+1$ for integer $\mu$ and $-1$ for half-integer $\mu$.
Applying a Weyl difference (A-process) by a shift $q \in \frac{1}{2}\mathbb{Z}$ produces a cross-term coefficient:
$$ c_\mu c_{\mu+q} = (-1)^{2\mu} (-1)^{2\mu+2q} = (-1)^{4\mu + 2q}. $$
Because $\mu \in \frac{1}{2}\mathbb{Z}$, the term $4\mu$ is always an even integer, meaning $(-1)^{4\mu} = 1$. The product simplifies exactly to $(-1)^{2q}$. This sign depends only on the outer shift $q$ and factors completely out of the inner continuous summation over $\mu$. The inner sum is thus perfectly stripped of the alternating parity, algebraically confirming the parity collapse.

**6. Rational-Collision Matrix Test for Primal Phases**
Consider the spatial character sum H5a: $\sum_d \chi_4(d) w_D(d) e(kX/d)$. When standard spacing methods (like Bombieri-Iwaniec) are applied, variables $d_1, d_2$ are grouped into rational collisions where $d_1/d_2 \approx a/b$. We investigate the exact collisions $d_1 b = d_2 a$.

**7. Exact Collision Block-Sign Factorization**
For exact collisions with $(a,b)=1$, we must have $d_1 = a c$ and $d_2 = b c$ for some integer $c$. The Gram matrix contains the bilinear character product $\chi_4(d_1)\chi_4(d_2)$.
Because $\chi_4(d)$ is supported entirely on odd integers, $d_1$ and $d_2$ are odd, which strictly forces $a, b,$ and $c$ to be odd. Therefore, $\chi_4(c) \in \{\pm 1\}$, which guarantees $\chi_4(c)^2 = 1$.
The character product reduces exactly to:
$$ \chi_4(d_1)\chi_4(d_2) = \chi_4(ac)\chi_4(bc) = \chi_4(a)\chi_4(b)\chi_4(c)^2 = \chi_4(ab). $$

**8. Mechanism of Character-Blindness**
This proves that inside the rational collision matrix, the $\chi_4$ character does not randomize into pseudo-random noise. Instead, it forms a uniform, constant block-sign $\chi_4(ab)$ that applies to the entire $(a,b)$ collision trajectory. Character blindness occurs explicitly downstream, when analytic matrix bounds (such as the Schur test or Frobenius norm) take absolute values of these off-diagonal blocks, effectively forcing $|\chi_4(ab)| \to 1$.

Dependencies:
*   Sharp truncated Perron formula and associated Riemann zeta moment bounds.
*   The asymmetric functional equation for $\zeta(s)L(s,\chi_4)$.
*   Mechanics of Weyl differencing (van der Corput A-process) and stationary phase evaluation.
*   Bombieri-Iwaniec rational collision matrix mapping $d_1/d_2 \approx a/b$.

Potential gaps:
*   The A-process parity collapse strictly applies to standard uniform shifts $\mu \to \mu+q$. If a method employs non-translation-invariant spacing metrics (e.g., specific scaling transforms) or pairs frequencies unevenly, the relative signs of the half-integer cosets might theoretically survive.
*   The exact collision block-sign property assumes $d_1 b = d_2 a$. For near-collisions where $d_1 b - d_2 a = \Delta \neq 0$, the simple factorization may fail, introducing complex residue-class interactions that degrade the block-sign uniformity.
*   The Mellin-Perron critical line limit assumes integration along standard vertical lines. Utilizing complex contours weaving through the critical strip could hypothetically lower absolute bounds, though this is far beyond current analytic tractability.

Counterexample or obstruction search:
1.  **Rational Collision Sign Stress Test:** We must numerically test the $\chi_4(d_1)\chi_4(d_2)$ behavior for near-collisions. Fix $a=1, b=3$ (so $\chi_4(ab) = -1$). For $D \sim 1000$, iterate all pairs $(d_1, d_2) \sim D$ such that $3d_1 - d_2 = \Delta$ for small values of $\Delta \in [-10, 10]$. Evaluate whether the average sign $\mathbb{E}[\chi_4(d_1)\chi_4(d_2) | \Delta]$ decays to 0, or if it remains heavily biased. If it remains biased, a signed matrix norm is theoretically viable.
2.  **Subconvexity Integral Stress Test:** Numerically integrate $I(T) = \int_1^T |\zeta(1/2+it)L(1/2+it, \chi_4)| t^{-1} dt$ for $T$ up to $10^5$. Check the asymptotic growth curve to verify that it does not decay and instead grows at least as fast as a constant (or $\log T$), empirically confirming the absolute-value barrier.

Useful lemmas:

```text
**Lemma M1: Mellin-Perron Exact Truncation Target**
Status: Proposed theorem dependency.
For $Z(s) = 4\zeta(s)L(s,\chi_4)$ and sharp cutoff height $T$, the Perron integral error is $O(X^{1+\epsilon}/T)$. Achieving the endpoint error $O(X^{1/4+\epsilon})$ strictly requires truncation at $T \gg X^{3/4-\epsilon}$. A smoothed Mellin transform with transition width $\asymp X^{1/4}$ similarly necessitates integration up to an effective support $T \asymp X^{3/4}$.

--- RESPONSE FROM deepseek_api ---
# Summary
This Stage A output independently executes the main Round 7 tasks assigned to `deepseek_api` by the judge:
- algebraic verification of the C2 Poisson normalization modulo 2 and reconciliation of the $(-1)^m$ and two-coset representations;
- explicit computation of the derivative determinants for the shifted phases $F_{2,1}$ and $F_2$;
- a detailed stationary-phase analysis of the C2 dual integrals, including boundary regimes;
- a plan for numerical stress tests of the three H5r norms (H5r-F, H5r-B, H5r-L1) with square, nonsquare, and near-square $X$;
- a precise audit of the Li--Yang/Bombieri--Iwaniec theorem's applicability to the residual sums $S_{\mathrm{odd}}$ and $S_\rho$;
- identification of the fresh **Fejer spike** as a quantitative failure mode that can break the Vaaler route for square $X$.

All algebraic identities and derivative checks are **proved**. The stationary-phase results are **contingent on a rigorous transition analysis** (now explicitly flagged). The numerical plan is **fully specified but not yet executed**. No improvement of the Gauss circle exponent is claimed; the report sharpens the obstruction map and provides the exact lemmas and stress-test protocols needed to either validate or disqualify the Vaaler route.

# Main claim or direction
Continue the balanced arithmetic hyperbola/Vaaler route as a **reduction and diagnostic framework**, not as a near-complete proof. The central analytical obstacle remains H5r (Fejer-residual reciprocal sums). The new findings confirm that:
- the C2 Poisson transform is algebraically unambiguous and admits two equivalent representations;
- the residual sums are structurally inside the Li--Yang reciprocal-sum class, so any future exponential-sum advance will directly improve the Gauss circle bound;
- a *positive non-negativity* of the Fejer majorant can cause catastrophic alignment when $X$ is a perfect square, potentially destroying the conjectural $O_\epsilon(X^{1/4+\epsilon})$ bound **if** no further cancellation is exploited. This is a concrete, testable failure mode.

# Detailed reasoning

## 1. Conventions and notation
Let $e(t)=e^{2\pi i t}$. The floor-compatible sawtooth is $\psi(t)=t-\lfloor t\rfloor-\frac12$; note $\psi(n)=-\frac12$ for $n\in\mathbb Z$. For a dyadic block $d\sim D$ we use a smooth compactly supported weight $w_D$ with $w_D(x)=0$ for $x\notin[c_1 D, c_2 D]$ and $w_D(x)=1$ for $x$ in a subinterval, with all derivatives uniformly bounded. The Fourier transform is $\widehat f(\xi)=\int_{\mathbb R}f(u)e(-\xi u)\,du$, so Poisson summation reads $\sum_{n\in\mathbb Z}f(n)=\sum_{\ell\in\mathbb Z}\widehat f(\ell)$ when both sides are suitably regularized.

The parameter $X=R^2\ge 1$, $y=\lfloor X^{1/2}\rfloor$. The local Vaaler height for a denominator block of size $D$ is
$$
H_D\asymp D X^{-1/4},\qquad X^{1/4}\le D\le X^{1/2}.
$$

## 2. Algebraic verification of C2 (odd-lattice Poisson transform)
### 2.1 Derivation
Write the odd-index filter as
$$
1_{2\nmid d}= \frac{1-(-1)^d}{2}.
$$
For $k\ge 1$,
$$
S_{\mathrm{odd}}(k,D)=\sum_{d}1_{2\nmid d}w_D(d)e(kX/d)
= \frac12\sum_{d}w_D(d)e(kX/d)-\frac12\sum_{d}(-1)^d w_D(d)e(kX/d).
$$
Define the integral
$$
I(\xi)=\int_{\mathbb R}w_D(u)\,e\!\left(\frac{kX}{u}-\xi u\right)du,\qquad \xi\in\mathbb R.
$$

**First term: all integers.** Apply Poisson summation to $f(d)=w_D(d)e(kX/d)$ (after smoothing for absolute convergence):
$$
\sum_{d}w_D(d)e(kX/d)= \sum_{m\in\mathbb Z} I(m).
$$

**Second term: sign-alternating.** $(-1)^d = e^{\pi i d}$, so $(-1)^d e(kX/d) = e(kX/d+\pi i d)$. The Fourier kernel for $e( (kX/d) + \frac12 d)$ shifted by integer frequencies gives
$$
\sum_{d}(-1)^d w_D(d)e(kX/d)= \sum_{m\in\mathbb Z} I(m-\tfrac12).
$$
Equivalently, letting $\mu=m-\frac12$ run over half-integers,
$$
\sum_{d}(-1)^d w_D(d)e(kX/d)= \sum_{\mu\in\mathbb Z+\frac12} I(\mu).
$$

Therefore the **two-coset representation** is
$$
\boxed{ S_{\mathrm{odd}}(k,D)=\frac12\sum_{m\in\mathbb Z}I(m)-\frac12\sum_{\mu\in\mathbb Z+\frac12}I(\mu). } \tag{2.1}
$$

### 2.2 Reconciliation of the $(-1)^m$ form
Consider the singly-indexed sum
$$
\sum_{n\in\mathbb Z}(-1)^n I(n/2).
$$
When $n$ is even, $n=2m$, $(-1)^{2m}=1$, $I(m)$; when $n$ is odd, $n=2m+1$, $(-1)^{2m+1}=-1$, $I(m+\frac12)$. Hence
$$
\sum_{n\in\mathbb Z}(-1)^n I(n/2)=\sum_{m\in\mathbb Z}I(m)-\sum_{m\in\mathbb Z}I(m+\tfrac12).
$$
The second sum is exactly $\sum_{\mu\in\mathbb Z+\frac12}I(\mu)$. Comparing with (2.1) yields the **single-sum representation**
$$
\boxed{ S_{\mathrm{odd}}(k,D)=\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2). } \tag{2.2}
$$
Both representations are algebraically identical and can be freely interchanged. There is no inherent "obstruction'' in either form; differences arise only when applying subsequent analytic operations (e.g., stationary phase) under different conventions.

### 2.3 Lemma C2 (proved)
> **Lemma C2 (Odd-lattice Poisson transform).**
> For a smooth weight $w_D$ supported on $[c_1 D, c_2 D]\subset(0,\infty)$ and any $k\ge 1$,
> $$
> \sum_{\substack{d\sim D\\2\nmid d}} w_D(d)\,e\!\left(\frac{kX}{d}\right)
> =\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
> =\frac12\sum_{m\in\mathbb Z}I(m)-\frac12\sum_{\mu\in\mathbb Z+\frac12}I(\mu),
> $$
> where $I(\xi)=\int_{\mathbb R}w_D(u)e(kX/u-\xi u)\,du$. Both sides converge absolutely after inserting a Gaussian regulator and letting its width tend to zero.
>
> *Proof.* Direct algebraic manipulation and standard Poisson summation. ∎

## 3. Derivative determinant calculations for $F_{2,1}$ and $F_2$
The Li--Yang (Bombieri--Iwaniec) framework requires a phase $F$ satisfying the non-degeneracy condition
$$
F'(x)F'''(x)-3\bigl(F''(x)\bigr)^2\neq 0
$$
on the relevant interval.

### 3.1 Odd-index residual $C_1$
After isolating $d=2n+1$ and scaling $x=n/D$, the phase becomes
$$
e\!\left(\frac{kX}{2n+1}\right)=e\!\left(\frac{kX}{D}\cdot\frac{1}{(2n+1)/D}\right).
$$
Define $F_{2,1}(x)=1/(x+1/D)$ for $x$ in a compact interval of $(0,\infty)$. Then
$$
F_{2,1}'(x)=-\frac{1}{(x+1/D)^2},\quad
F_{2,1}''(x)=\frac{2}{(x+1/D)^3},\quad
F_{2,1}'''(x)=-\frac{6}{(x+1/D)^4}.
$$
Hence
$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
= \frac{6}{(x+1/D)^6}-\frac{12}{(x+1/D)^6}
= -\frac{6}{(x+1/D)^6}\neq 0.
$$

### 3.2 Frequency-shifted residual $C_{2,\rho}$
The sum is $S_\rho(k,D)=e(k\rho/4)\sum_d w_D(d)e(kX/(4d))$ with $\rho\in\{1,3\}$. Scaling $x=d/D$ gives the phase function $F_2(x)=1/(4x)$. Derivatives:
$$
F_2'(x)=-\frac{1}{4x^2},\quad
F_2''(x)=\frac{1}{2x^3},\quad
F_2'''(x)=-\frac{3}{2x^4}.
$$
Thus
$$
F_2'F_2'''-3(F_2'')^2
= \frac{3}{8x^6}-\frac{3}{4x^6}
= -\frac{3}{8x^6}\neq 0.
$$

### 3.3 Lemma N1 (proved)
> **Lemma N1 (Phase non-degeneracy for residual families).**
> The phase functions $F_{2,1}(x)=1/(x+1/D)$ and $F_2(x)=1/(4x)$ satisfy the Li--Yang non-degeneracy condition uniformly on any compact subinterval of $(0,\infty)$. Consequently the residual sums $C_1$ and $C_{2,\rho}$ belong to the same structural class as the standard reciprocal phase $1/x$.

*Proof.* By direct differentiation. ∎

## 4. Stationary-phase analysis of the C2 dual integrals
### 4.1 Correct sign and stationary points
The integral $I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du$ has phase derivative $-kX/u^2-\xi$, which is *negative for all $u$* when $\xi>0$. Therefore **stationary points exist only for $\xi<0$**. Write $\xi=-m$ with $m>0$:
$$
J(m):=I(-m)=\int w_D(u)\,e\!\left(\frac{kX}{u}+m u\right)du.
$$
The stationary phase condition is
$$
-\frac{kX}{u^2}+m=0\;\Longrightarrow\; u_0=\sqrt{\frac{kX}{m}}.
$$
For $u_0$ to lie inside the support of $w_D$ (size $\asymp D$) we need
$$
m\asymp \frac{kX}{D^2}. \tag{4.1}
$$
If $m$ is much smaller or larger, $u_0$ is outside the support or the quadratic approximation fails, and the integral must be estimated by other means.

### 4.2 Asymptotic expansion (formal)
Near $u_0$, expand $f(u)=kX/u+mu$:
$$
f(u_0)=2\sqrt{kX m},\qquad
f''(u_0)=\frac{2kX}{u_0^3}=\frac{2 m^{3/2}}{\sqrt{kX}}.
$$
Applying the standard stationary-phase formula,
$$
J(m)\sim w_D(u_0)\, e^{2\pi i(2\sqrt{kX m}+1/8)} \sqrt{\frac{2\pi}{|f''(u_0)|}} \Bigl(1+O(m^{-1})\Bigr).
$$
The amplitude is $\approx D^{3/2}(kX)^{-1/2}$ up to constants.

### 4.3 Boundary regime $D\asymp X^{1/2},\; k\asymp 1$
Then $m\asymp 1$. The stationary point $u_0\approx\sqrt{kX}$ is comparable to the upper end of the $d$-range ($D\sim X^{1/2}$), so it may lie at or beyond the edge of the effective support. A uniform asymptotic expansion requires a more delicate analysis (Fresnel-type integrals) or a separate treatment (direct A-process). This regime **cannot** be handled by a naive stationary-phase lemma; it is a known fragile point.

### 4.4 Non-stationary bounds
For $m$ outside a constant multiple of the critical range, standard integration by parts gives $|J(m)|\ll_A (|m|+1)^{-A}$ for any $A>0$.

### 4.5 Lemma C2-SP (stationary-phase parameters, provisional)
> **Lemma C2-SP (Dual stationary phase).**
> Let $m>0$ and assume $w_D$ is smooth, compactly supported on $[c_1 D, c_2 D]$, and $D$ is large.
> (i) If $c_1 \frac{kX}{D^2}\le m\le c_2\frac{kX}{D^2}$, then the stationary point $u_0=\sqrt{kX/m}$ lies in the effective support, and
> $$
> |J(m)| \asymp \frac{D^{3/2}}{\sqrt{kX}}.
> $$
> (ii) If $m$ is outside this range by a factor $>c>1$, then $|J(m)|\ll_A (|m|+1)^{-A}$.
> (iii) When $m\asymp 1$ and $D\asymp X^{1/2}$, no uniform asymptotic can be asserted without additional information about the support of $w_D$; the estimate must be obtained by a direct analysis (e.g., A-process or explicit evaluation).
>
> *Proof.* Standard stationary phase and integration by parts; the boundary case requires separate handling. ∎

## 5. Numerical stress-test methodology for the three H5r norms
We propose an explicit computational protocol to measure the size of the residual families. Because the full range $X\to\infty$ is inaccessible, the tests should be performed for moderately large $X$ (e.g., $10^6$--$10^8$) and for several dyadic blocks $D$. The required quantities are:

**Definition of the norms.** For a given residual family $S_\star(k,D)$ (either $S_{\mathrm{odd}}$ or $S_\rho$), set $H_D=\lfloor D X^{-1/4}\rfloor$ and $\eta_{k,H_D}=1-\frac{|k|}{H_D+1}$. Define:
- H5r-F (fixed Fejer):
$$
  \mathcal E_F(D,X)=\frac{1}{H_D}\Bigl|\sum_{1\le |k|\le H_D}\eta_{k,H_D}S_\star(k,D)\Bigr|.
$$
- H5r-B (worst-case bounded coefficients):
$$
  \mathcal E_B(D,X)=\max_{K_0\le H_D}\frac{1}{K_0}\sup_{|v_k|\le 1}\Bigl|\sum_{k\sim K_0}v_k S_\star(k,D)\Bigr|,
$$
  which can be upper-bounded by $\max_{K_0}\frac{1}{K_0}\sum_{k\sim K_0}|S_\star(k,D)|$ (the termwise-$L^1$ per block).
- H5r-L1 (global mean absolute value):
$$
  \mathcal E_{L1}(D,X)=\frac{1}{H_D}\sum_{1\le |k|\le H_D}|S_\star(k,D)|.
$$

**Test scenarios.** We must examine at least the following cases:
1. **Square $X$:** $X=n^2$. Then many $d$ divide $X$, and $X/d$ is integer, causing the exponential sum to be large. The Fejer kernel $K_H(t)$ attains its maximum $H+1$ at integers, so the residual majorant can spike.
2. **Non-square integer $X$:** e.g., $X=n^2+1$.
3. **Near-square $X$:** $X=n^2+\delta$ with $\delta=\pm1,\pm2,\dots$, to test how quickly the spike subsides.
4. **Large $D$ vs. small $D$.** Evaluate for $D\approx X^{1/2}$, $D\approx X^{1/3}$, $D\approx X^{1/4}$.

**Implementation outline (pseudocode).**
For a chosen $X$, loop over dyadic $D$. For each $D$, construct a smooth weight $w_D$ (e.g., a bump function with support $[D/2,2D]$). Compute $H_D$. For each $k=1,\dots,H_D$, compute $S_\star(k,D)$ exactly by summation over $d$ (trivial summation is feasible for moderate $D$). Then compute the three norms. Compare to the target $C X^{1/4}$ with $C$ a reasonable constant. For square $X$, also record the contribution of the $d$ that divide $X$ separately.

**Heuristic expectations.** For generic $X$, the exponential sums should exhibit square-root cancellation, so $|S_\star(k,D)|\lesssim \sqrt{D}$. Then $\mathcal E_{L1}\lesssim\sqrt{D}\approx X^{1/4}$ in the critical range, meeting the target. However, for square $X$, the terms with $d\mid X$ are purely additive, potentially giving $|S_\star(k,D)|\gg D^\alpha$ with $\alpha>1/2$ when $k$ aligns. This could make $\mathcal E_{L1}\gg X^{1/4}$. The stress test must determine whether the Fejer weights $\eta_{k,H_D}$ and the averaging over $k$ suppress these spikes sufficiently. **If they do not**, the Vaaler route is invalid for square $X$ unless a separate argument is supplied.

## 6. Audit of the Li--Yang/Bombieri--Iwaniec theorem applicability
### 6.1 Statement of the relevant theorem (Li--Yang 2023, simplified)
Li and Yang (arXiv:2308.14859) prove, among other results, that for $T\ge 1$,
$$
\sum_{h\sim H}\sum_{m\sim M} a_h b_m\, e\!\left(\frac{h T}{m}\right)
\ll_\epsilon T^{\theta^*+\epsilon}\bigl(H M\bigr)^{\frac12},
$$
with $\theta^*=0.314483\dots$, under suitable conditions: $|a_h|,|b_m|\le 1$, smooth weights, $H,M$ in certain ranges, and the phase must satisfy the non-degeneracy conditions (which it does). The theorem is stated for dyadic blocks and requires the weights to be smooth and supported away from $0$.

### 6.2 Mapping of our residual sums
**First residual $C_1=S_{\mathrm{odd}}$.** After substituting $d=2n+1$, the sum becomes
$$
\sum_{n\asymp D/2} w_{D,1}(n)\, e\!\left(\frac{kX}{2n+1}\right).
$$
We can absorb the shift into the weight and the phase: set $M=D$, $T=X$, $h=k$, $m=n$, and $F(x)=\frac{1}{x+1/D}$ (or effectively $1/x$ after a small change of variable). The coefficients $v_k$ are bounded by $1$, and the inner weight $w_{D,1}$ is smooth. All derivative non-degeneracy conditions are satisfied by Lemma N1. The absolute value in H5r-B is taken only after dyadic blocking in $k$, which is compatible with standard bilinear applications (Cauchy--Schwarz in $k$ reduces the $|\sum v_k S|$ to an $L^2$ mean over $k$; the resulting triple sum can be handled by spacing inequalities).

**Second residual $C_{2,\rho}=S_\rho$.** Here
$$
S_\rho(k,D)=e(k\rho/4)\sum_{d\sim D} w_D(d)\, e\!\left(\frac{kX}{4d}\right).
$$
After scaling $d=Dx$, the inner sum is of the form
$$
\sum_{x} e\!\left(\frac{k (X/4)}{D x}\right),
$$
so it fits the Li--Yang framework with $T=X/4$, $M=D$, and an extra factor $e(k\rho/4)$ that can be absorbed into the coefficient $v_k$. The phase $F_2(x)=1/(4x)$ is non-degenerate (Lemma N1).

### 6.3 Hypotheses check
The Li--Yang theorem assumes:
- Coefficients $a_h,b_m$ are complex with $|a_h|,|b_m|\le 1$. Our $v_k$ satisfy this.
- The sums are over dyadic intervals with smooth weights. Our $w_D$ can be chosen smooth.
- The double sum is over $h\sim H$, $m\sim M$ with $H,M$ in a permissible range (typically $X^\varepsilon\le H,M\le X^{1-\varepsilon}$). Our ranges: $k\sim K_0\le H_D\asymp D X^{-1/4}\le X^{1/4}$ (for $D\sim X^{1/2}$ this is $X^{1/4}$), and $d\sim D\le X^{1/2}$. These are inside the allowed range for large $X$.
- The theorem delivers a bound of the form $O_\epsilon(T^{\theta+\epsilon}(HM)^{1/2})$. The exponent $\theta^*$ is the best known. The factor $(HM)^{1/2}$ is the trivial $\ell^2$ bound; the improvement is in the power of $T$.

### 6.4 Gap in exponent
For our required H5r target, we need the double sum to be $\ll K_0 X^{1/4+\epsilon}$. Even after applying the Li--Yang bound with $\theta^*\approx0.3145$, the resulting estimate for $P(X)$ would be $\approx X^{0.3145+\epsilon}$, not $X^{1/4}$. Thus the theorem does **not** reach the conjectural endpoint; it only confirms that the residual sums belong to a class where progress is possible. The gap is quantitative, not structural.

> **Lemma N2 (Li--Yang compatibility).**
> The residual sums $S_{\mathrm{odd}}(k,D)$ and $S_\rho(k,D)$ can be represented as instances of the bilinear phases treated by Li--Yang (2023) after a smooth dyadic decomposition. All required derivative hypotheses are satisfied (Lemma N1). A direct application of Li--Yang's theorem yields an exponent $\theta^*\approx0.31448$ for $P(X)$, which is above $1/4$.

## 7. Fejer spike: a quantitative failure mode
### 7.1 Mechanism
The Vaaler residual majorant is $|R_H(t)|\le \frac{1}{2H+2}K_H(t)$ with
$$
K_H(t)=\sum_{|k|\le H}\Bigl(1-\frac{|k|}{H+1}\Bigr)e(kt)
      =\frac{1}{H+1}\Bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\Bigr)^2.
$$
This kernel is non-negative and, crucially, **equals $H+1$ when $t\in\mathbb Z$**. For the first leg, the residual feeds on $t=X/d$. If $X$ is a perfect square, many $d\le y$ divide $X$, making $X/d$ an integer. Then $K_{H_D}(X/d)=H_D+1$, and the residual majorant gives a contribution of order $O(H_D)$ rather than the average $O(1/H_D)$.

### 7.2 Impact on the sum over $d$
After expanding the majorant, the Fejer-weighted residual for the first leg becomes (schematically)
$$
\frac{1}{2H_D+2}\sum_{d\le y} \Bigl|\chi_4(d)\Bigr| K_{H_D}(X/d)
$$
(or something similar after accounting for signs). The term-by-term contribution at the divisors $d\mid X$ can be as large as $O(1)$ per divisor (since $K_{H_D}/(2H_D+2)\approx 1/2$ at integer points). There are roughly $X^{o(1)}$ divisors, but they may accumulate to a noticeable effect. More importantly, the **Fourier expansion of the majorant reintroduces the reciprocal sums $S_{\mathrm{odd}}$ etc. with Fejer weights**; but the spike phenomenon means that *even the optimal bound for those residual sums* might be larger at square $X$ because the Fejer weights heavily emphasize frequencies where the primal sum is large.

### 7.3 A concrete worst-case scenario
Suppose $X=Q^2$ is a large square. Take $D=Q$ (the maximum $d$). For every $k$, $kX/d = kQ$ is integer, so $S_{\mathrm{odd}}(k,D) = \sum_{2\nmid d\sim D} w_D(d)$ (all phases aligned). This sum is $\asymp D$ (weighted length). Then $\mathcal E_{L1}\approx D / H_D \approx X^{1/2}/X^{1/4}=X^{1/4}$, which matches the target! Wait, let's check: if all phases are 1, then $S_{\mathrm{odd}}(k,D)\approx D/2$ (tight bound). Then $\mathcal E_{L1}\approx (D/2) H_D/H_D = D/2 \approx X^{1/2}/2$, far exceeding $X^{1/4}$. Actually the residual target H5r-F is an average of $S_{\mathrm{odd}}$ with Fejer weights; if each $S_{\mathrm{odd}}\approx D$, then the average $\approx D$, which is $X^{1/2}$, not $X^{1/4}$. That would be fatal for the Vaaler route. However, the Fejer residual majorant is applied *before* summing over $d$ in the original proof skeleton. The Vaaler step is done inside the sum over $a$ or $b$. That is: we approximate $\psi(X/a)$ by a finite Fourier series plus residual, and then sum over $a$. The residual bound is $|R_H(X/a)|\le \frac{1}{2H+2}K_H(X/a)$. So the total residual contribution from the first leg is
$$
\Bigl|\sum_{a\le y}\chi_4(a)R_{H_D}(X/a)\Bigr|
\le \frac{1}{2H_D+2}\sum_{a\le y} K_{H_D}(X/a).
$$
Because $K_H$ is non-negative, we cannot exploit any further sign cancellation. Therefore the residual contribution from all $a$ that are divisors of $X$ (or near divisors) could be enormous. In the square case $X=Q^2$, we have $a=Q$ itself giving a spike. But there are many other $a$ such that $X/a$ is integer: all divisors. The number of divisors is $\ll X^{o(1)}$, but each such $a$ contributes about $O(1)$ from the majorant. The remaining $a$ produce smaller values. So the total residual could be as large as $\gg \tau(X)\approx X^{o(1)}$, still possibly harmless because $X^{o(1)}\ll X^{1/4}$. However, the spike may be more severe for the *Fourier* expansion of $K_H$: the residual after inserting the Fejer expansion yields sums like $C_1$ where the $k$-weights are not uniform but heavily concentrate near $k=0$ because of the Fejer shape. This requires a detailed quantitative estimate. I will formulate a precise failure scenario:

**Failure mode F1:** If for square $X$ the Fejer-weighted average $\frac{1}{H_D}\sum_{|k|\le H_D}\eta_{k,H_D} S_{\mathrm{odd}}(k,D)$ is not $\ll X^{1/4}$ but rather $\gg X^{1/4+\delta}$ for some $\delta>0$, then the Vaaler route **fails** for those $X$ (and hence cannot prove the uniform bound unless those $X$ are excluded or a separate treatment is found). This is testable by numerical experiments.

## 8. Character-aware vs. character-blind stress test
To assess the value of $\chi_4$, we propose to compare two versions of the main dyadic target H5a:
- Version A: $B_1^{\chi}(H_0,D;X)=\sum_{h\sim H_0}u_h\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d)$.
- Version B: $B_1^{\mathrm{abs}}(H_0,D;X)=\sum_{h\sim H_0}u_h\sum_{d\sim D}w_D(d)e(hX/d)$ (i.e., replacing $\chi_4(d)$ by $1$).

Compute both for moderate $X$ and typical $h$-ranges. The ratio of their magnitudes will indicate whether the character provides any cancellation beyond generic square-root behavior. Since H7 shows A-process eliminates the character, the advantage must be exploited before differencing. This test gives a baseline for how much "free'' saving can be expected from the mere presence of $\chi_4$.

## 9. Additional failure modes
We list five distinct failure modes that could derail the arithmetic/Vaaler route.

1. **Fejer spike for square $X$ (F1).** As described in §7, the non-negative Fejer majorant yields an uncontrollable residual when $X$ is a square, because many $X/d$ values are integers. Without a supplementary cancellation mechanism (e.g., an alternating sign of $\chi_4$ that survives the residual bound), the proof cannot achieve $O(X^{1/4})$ for all $X$.

2. **Insufficient stationary-phase control at boundary (F2).** For $D\asymp X^{1/2}$ and $k\asymp 1$, the dual C2 integral is not amenable to uniform stationary phase. Any proof relying on asymptotic expansions must provide an alternative estimate for this region; otherwise the bound fails.

3. **The H5r residual matches the divisor problem's true size (F3).** The sums $C_1$ and $C_{2,\rho}$ are structurally identical to the sums appearing in the Dirichlet divisor problem after residue splitting. If the divisor problem's error term genuinely requires an exponent $>1/4$ (which is generally believed to be false, but the *known* bounds are larger), then H5r cannot be improved without a breakthrough in the divisor problem itself.

4. **Character-blind methods cannot reach $\theta=1/4$ (F4).** H6 states that a simple one-dimensional exponent-pair approach would need $3\kappa+2\lambda\le 1$. The best known exponent pair gives $>1/4$. If every method that respects the Fejer majorant's loss of sign effectively reduces to a character-blind estimate, then the Vaaler route inherits this barrier.

5. **Mellin--Perron routes are circular (F5).** The Mellin--Perron alternative, while avoiding Fejer positivity, reintroduces exponential sums through the functional equation that are as hard as the original problem. If no new "non-majorizing'' truncation can be found that provides a genuinely better error term, the entire arithmetic route collapses back to the classical Voronoi/Hardy difficulties.

## 10. Useful lemmas
We collect the precise lemma statements that are either proved in this report or upgraded to proved status.

### Lemma C2 (Proved)
> Under the conventions of §1, for any $k\ge 1$,
> $$
> \sum_{\substack{d\sim D\\2\nmid d}} w_D(d)\,e\!\left(\frac{kX}{d}\right)
> =\frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
> =\frac12\sum_{m\in\mathbb Z}I(m)-\frac12\sum_{\mu\in\mathbb Z+\frac12}I(\mu),
> $$
> with $I(\xi)=\int_{\mathbb R} w_D(u)e(kX/u-\xi u)\,du$. The identities hold after inserting a Gaussian regulator and letting its width tend to zero.

### Lemma C2-SP (Stationary-phase parameters, conditional)
> For $m>0$, let $J(m)=I(-m)$.
> (i) If $c_1\frac{kX}{D^2}\le m\le c_2\frac{kX}{D^2}$, then $|J(m)|\asymp D^{3/2}(kX)^{-1/2}$.
> (ii) If $m$ is outside this range by a constant factor, $|J(m)|\ll_A(|m|+1)^{-A}$.
> (iii) For $m\asymp 1$ and $D\asymp X^{1/2}$, no uniform asymptotic expansion is valid without further restrictions on the support.
> **Status:** Part (i) and (ii) are standard; (iii) is a warning that the boundary requires separate treatment.

### Lemma N1 (Proved)
> The functions $F_{2,1}(x)=1/(x+1/D)$ and $F_2(x)=1/(4x)$ satisfy $F'F'''-3(F'')^2\neq 0$ on any compact subinterval of $(0,\infty)$.

### Lemma N2 (Li--Yang compatibility, structural)
> The sums $S_{\mathrm{odd}}(k,D)$ and $S_\rho(k,D)$ can be written as bilinear sums of the type treated by Li--Yang (2023) after a smooth dyadic decomposition and scaling. All derivative hypotheses are satisfied. A direct application of Li--Yang's theorem to the residual blocks would give $P(X)\ll_\epsilon X^{\theta^*+\epsilon}$ with $\theta^*\approx0.31448$, which does **not** reach $1/4$.

### Lemma H5r-F (Fixed Fejer target, exact)
> For $H_D\asymp D X^{-1/4}$ and $\eta_{k,H_D}=1-\frac{|k|}{H_D+1}$, the exact requirement forced by the Vaaler majorant is
> $$
> \Bigl|\frac{1}{H_D}\sum_{1\le|k|\le H_D} \eta_{k,H_D} S_\star(k,D)\Bigr|
> \ll_\epsilon X^{1/4+\epsilon},
> $$
> where $S_\star$ represents either $S_{\mathrm{odd}}$ or $S_\rho$. The zero-frequency term ($k=0$) already contributes $D/H_D\asymp X^{1/4}$ and need not be inside the sum.

### Lemma H5r-B (Bounded coefficient target, sufficient)
> For all $|v_k|\le 1$ and dyadic $K_0\le H_D$,
> $$
> \Bigl|\sum_{k\sim K_0} v_k S_\star(k,D)\Bigr|
> \ll_\epsilon K_0 X^{1/4+\epsilon}.
> $$
> This implies H5r-F after dyadic decomposition.

### Lemma H5r-L1 (Termwise $L^1$ target, sufficient but crude)
> $$
> \frac{1}{H_D}\sum_{1\le|k|\le H_D} |S_\star(k,D)|
> \ll_\epsilon X^{1/4+\epsilon}.
> $$

### Lemma H7 (Proved, A-process degeneracy)
> For every integer $q$,
> $$
> \chi_4(d)\chi_4(d+q)=
> \begin{cases}
> 1_{2\nmid d},& q\equiv0\pmod4,\\
> -1_{2\nmid d},& q\equiv2\pmod4,\\
> 0,& q\equiv1,3\pmod4.
> \end{cases}
> $$

These lemmas augment the bank; their statuses are as indicated.

## 11. Dependencies
- The entire arithmetic reduction relies on **H1--H3** (proved floor-compatible identities).
- The Vaaler step relies on **H4**, which references an external theorem (Vaaler's approximation with Fejer majorant). The exact statement of that theorem must be verified against a standard reference; here we assume its validity.
- The analytic targets **H5a, H5b, H5r** are currently not known; the present work only formulates them precisely and checks their compatibility with existing technology.
- The Li--Yang theorem (or Bombieri--Iwaniec spacing method) is the most advanced known technique for such sums; our audit depends on its published statement.

## 12. Potential gaps
1. **The Fejer spike for square $X$** is a concrete gap: no proof has been given that the residual remains $O(X^{1/4})$ in that case.
2. **Boundary stationary-phase region** for $D\asymp X^{1/2}$, $k\asymp 1$ is untreated.
3. **The Li--Yang theorem's exact exponent** is insufficient, and no path to improve it has been identified.
4. **Signed Fourier truncation** has not been developed into a viable alternative with better error.
5. **Numerical evidence** for H5r is completely absent; the feasibility of the conjectural bounds is unverified.
6. **The B-process route (H8)** still suffers from Hessian degeneracy (H9) and does not currently offer a new estimate.

## 13. Counterexample or obstruction search
- **Square $X$:** we formally predict that $P(X)$ might exhibit larger than expected error due to Fejer spikes. Computational search for small squares ($X\le 10^4$) can test this.
- **Rational collisions in the primal sum:** when $kX/d$ is near a rational with small denominator, the sum can peak. Our stress tests should scan for such $k,d$ pairs.
- **Parity-only sums:** the odd-lattice sum without $\chi_4$ may behave similarly to the divisor sum; known $\Omega$-results suggest that an exponent $\le 1/4$ is plausible but not proven. Thus H5r may be fundamentally as hard as the divisor problem, which would mean the Vaaler route has not simplified the problem.

## 14. What should be tested next
1. **Numerical H5r norms** for square, nonsquare, and near-square $X$ using the protocol of §5.
2. **Fejer spike scenario** specifically for $X$ a perfect square, with $D$ set to the maximal divisor $D=X^{1/2}$.
3. **Stationary-phase boundary** by direct integration for $D\sim X^{1/2}$, $k=1$, and compare with the asymptotic formula.
4. **Character-aware vs. character-blind** comparison for H5a to quantify the benefit of $\chi_4$.
5. **Exact Li--Yang theorem audit** with full hypotheses written out, verifying that our $v_k$ and $w_D$ satisfy all smoothness and support conditions.

## 15. Confidence calibration and failure modes
**Overall confidence in the arithmetic reduction (H1--H3):** High. The identities are algebraic and have been verified.

**Confidence in the necessity of H5r:** High. The Vaaler residual cannot be simplified to a scalar error.

**Confidence in the algebraic lemmas C2, N1, H7:** High; they are proved by direct calculation.

**Confidence in the stationary-phase analysis (C2-SP):** Moderate for the asymptotic regime, low at the boundary; rigorous transition estimates are missing.

**Confidence that the Li--Yang framework applies structurally:** High; the mapping is explicit. Confidence that it can yield $X^{1/4}$: Very low; it currently gives $>0.314$.

**Confidence that the Fejer spike is a real obstruction:** Moderate-high; it is a clear mechanism by which the Vaaler route could fail for square $X$. Numerical tests will either confirm or refute its severity.

**Confidence that a non-majorizing truncation can circumvent H5r:** Low; currently no alternative has been formulated with a provably better error term.

**Main failure modes (ranked by severity):**
1. Fejer spike for square $X$ (quantifiable, testable).
2. Boundary stationary-phase gap (requires additional analysis).
3. Character-blind residual (H5r) is as hard as the divisor problem and cannot be proved with known technology.
4. Mellin--Perron is circular and offers no advantage.
5. B-process first fails to break the character parity degeneracy.

## 16. Prioritized next-action list
1. **Run numerical stress tests** (§5) for H5r-F, H5r-B, H5r-L1 on squares and near-squares; report the measured exponent.
2. **Formulate a rigorous lemma** for the C2 integral in the boundary regime $m\asymp 1$ (either by a direct A-process or by exact evaluation with Fresnel integrals).
3. **Complete the Li--Yang theorem audit** by extracting the precise hypotheses from the paper and matching our residual sums exactly.
4. **Develop a signed Fourier truncation** with explicit error estimates and compare its residual to the Vaaler residual.
5. **Propose a new mechanism** (if any) that could avoid the Fejer spike, e.g., by exploiting cancellation across different $k$ modes before applying the majorant.
6. **Integrate the Poisson--Bessel calibration module** into the repo as a secondary check, to stabilize notation and provide the classical $R^{2/3}$ baseline.

**No improvement of the Gauss circle exponent is proved.** The present report serves as a precise diagnostic and a foundation for the next round of targeted computational and analytic tests.

## Cross Reviews

--- REVIEW FROM gpt_pro_thinking ---
Most valuable input from others:

Source anchor: reviewed the Round 7 Stage A outputs for `gemini_deep_think` and `deepseek_api` under the supplied `## Outputs To Review`, following the required Stage B schema.

From `deepseek_api`, the most valuable contribution is the norm-level clarification of H5r. The right minimal residual target is the fixed-Fejer target H5r-F, not automatically the arbitrary-coefficient target H5r-B and not the termwise $L^1$ target. In block form, the relevant assertion is:

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D} S_\star(k,D)
\right|
\ll_\epsilon X^{1/4+\epsilon},
\qquad
\eta_{k,H_D}=1-\frac{|k|}{H_D+1},
$$

with the $k=0$ Fejer mode treated separately as

$$
D/H_D\asymp X^{1/4}.
$$

This correctly identifies H5r-F as the proof-relevant target. H5r-B remains a sufficient but stronger route; if one proves only H5r-B using existing character-blind reciprocal-sum technology, the resulting exponent is expected to remain above $1/4$.

DeepSeek's C2 calculation is also valuable. The odd-lattice residual

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d)
$$

admits both a two-coset Poisson representation and an alternating-sign representation:

$$
S_{\mathrm{odd}}
=
\frac12\sum_{m\in\mathbb Z}\widehat f(m)
-
\frac12\sum_{m\in\mathbb Z}\widehat f(m+\tfrac12),
$$

up to Fourier-sign convention, and equivalently

$$
S_{\mathrm{odd}}
=
\frac12
\sum_{m\in\mathbb Z}
(-1)^m
\int_{\mathbb R}
w_D(u)e\left(\frac{kX}{u}-\frac{mu}{2}\right)\,du.
$$

The stationary point calculation gives active dual length

$$
|m|\asymp \frac{kX}{D^2}.
$$

This is a clean transformation lemma, with the important caveat that boundary cases such as $D\asymp X^{1/2}$, $k\asymp 1$ have dual length $O(1)$ and cannot be hidden inside a generic stationary-phase estimate.

From `gemini_deep_think`, the most useful contribution is the rational-collision sign calculation for the spatial-character family H5a. For exact rational collisions

$$
d_1 b=d_2 a,\qquad (a,b)=1,
$$

we have $d_1=ac$, $d_2=bc$. If the character product is nonzero, then $a,b,c$ are odd and

$$
\chi_4(d_1)\chi_4(d_2)
=
\chi_4(ac)\chi_4(bc)
=
\chi_4(a)\chi_4(b)\chi_4(c)^2
=
\chi_4(ab).
$$

Thus $\chi_4$ does not behave randomly on exact collision lines; it becomes a block-constant sign indexed by the rational slope $a/b$. That is a useful structural observation for any Bombieri--Iwaniec-style Gram matrix or rational-spacing analysis. The real loss occurs when later matrix norms or absolute values replace $\chi_4(ab)$ by $1$.

Gemini's Mellin--Perron comparison is also useful as a diagnostic mirror. The claim that sharp Perron truncation forces roughly

$$
T\gg X^{3/4}
$$

to make the truncation error $O(X^{1/4+\epsilon})$ is plausible under the stated sharp-cutoff setup. The further claim that applying the functional equation reconstructs Voronoi/Bessel reciprocal sums of length about

$$
T^2/X\asymp X^{1/2}
$$

is a useful heuristic and likely directionally correct, but it should be recorded as a theorem-dependency target, not as proved in Round 7.

Claims that look correct:

1. H5r remains mandatory. The Vaaler residual cannot be discarded as a scalar $O(D/H_D)$ term. The zero Fejer mode contributes the target-scale term $D/H_D\asymp X^{1/4}$, while nonzero Fejer modes generate real reciprocal sums. This is now a stable conclusion across rounds.

2. H5r-F is the exact block-level target one should try to prove first. H5r-B and H5r-L1 are useful sufficient or stress-test norms, but the actual residual has fixed Fejer coefficients. Treating those coefficients as arbitrary bounded coefficients may lose the only remaining exploitable structure.

3. The C2 two-coset and alternating-sign Poisson formulas are both legitimate up to Fourier-sign normalization. The alternating factor $(-1)^m$ is not fictitious; it appears in one correct parametrization. At the same time, its obstruction strength is representation-dependent because the two-coset formulation may retain spacing information not visible in the one-sequence alternating model.

4. The stationary-phase scale for C2 is correct at the level of lengths:

$$
u_0\asymp D
\quad\Longleftrightarrow\quad
|m|\asymp \frac{kX}{D^2}.
$$

The constants and $2\pi$ phases still need normalization, but the scale is correct.

5. The derivative determinant check for shifted reciprocal phases is directionally correct. For $F(x)=1/(x+a)$,

$$
F'F'''-3(F'')^2=-6(x+a)^{-6}\ne 0.
$$

For $F(x)=c/x$,

$$
F'F'''-3(F'')^2=-6c^2x^{-6}\ne 0.
$$

Thus the H5r residual phases remain in the standard reciprocal-sum class, not a pathological new class.

6. Gemini's exact-collision character factorization is correct for exact collisions and should be added as a proved algebraic lemma with a narrow hypothesis. It is not yet a near-collision theorem.

7. A direct A-process on the alternating coefficient alone gives

$$
(-1)^m(-1)^{m+q}=(-1)^q,
$$

so the coefficient itself carries no persistent oscillation after translation differencing. This is a valid diagnostic for one representation, but not a universal obstruction.

8. The Mellin--Perron route should be kept as a comparison route, not promoted as an escape. The route avoids Fejer positivity at first, but likely reintroduces Voronoi/Bessel or reciprocal-sum difficulties after functional equation and stationary phase.

Claims that need proof:

1. DeepSeek's H5r-F sufficiency needs to be written as a formal lemma with all summations included:

- both residual families $S_{\mathrm{odd}}$ and $S_\rho$;
- both signs $k>0$ and $k<0$;
- the $k=0$ mode;
- dyadic summation over $D$;
- both hyperbola legs;
- the exact factor $(2H_D+2)^{-1}$ from the Vaaler majorant;
- logarithmic losses absorbed into $X^\epsilon$.

A correct lemma should read approximately:

If H5r-F holds uniformly for all dyadic $D$ with $X^{1/4}\le D\le X^{1/2}$ and all residual families produced by H4, then the total Vaaler residual is $O_\epsilon(X^{1/4+\epsilon})$.

2. H5r-B $\Rightarrow$ H5r-F is correct but must be stated with coefficient conventions. If H5r-B allows arbitrary complex $v_k$ with $|v_k|\le 1$, then on each dyadic $k$-block it is essentially equivalent to a dyadic $L^1$ estimate, since one may choose

$$
v_k=\overline{S_\star(k,D)}/|S_\star(k,D)|.
$$

Thus H5r-B should be described as an arbitrary-coefficient or dyadic-$L^1$ strength estimate, not merely as a mild strengthening of H5r-F.

3. The Li--Yang applicability claim needs a primary-source audit. DeepSeek's schematic formula omits the outer frequency in the phase as written. The relevant dictionary should be:

$$
e(kX/d)
=
e\left(k\frac{X}{D}F(d/D)\right),
\qquad
F(x)=1/x.
$$

Thus the Li--Yang/Bombieri--Iwaniec model must allow phases of the form

$$
e\left(h\frac{T}{M}F(m/M)\right)
$$

or equivalent, with $T=X$, $M=D$, $h=k$. It is not enough to write a double sum with phase $e(Tf(m/M))$ independent of $h$.

4. The assertion that Li--Yang gives $\theta^*\approx0.31448$ for H5r-B should remain conditional until the exact theorem statement is checked. The audit must verify coefficient class, smooth weights, dyadic ranges, absolute-value placement, first-spacing hypotheses, second-spacing input, and whether parity or shifted-frequency coefficients are allowed.

5. Gemini's Mellin--Perron functional-equation reconstruction needs a detailed derivation. In particular, the route must specify:

- sharp versus smoothed Perron cutoff;
- endpoint convention when $X\in\mathbb Z$;
- residue extraction at $s=1$;
- horizontal contour bounds;
- the functional equation for $4\zeta(s)L(s,\chi_4)$;
- stationary-phase derivation of the dual length $N\asymp T^2/X$;
- exact relationship between the dual sums and H5r/H5a/H5b.

6. Gemini's critical-line statement needs correction. It is not appropriate to say that the absolute-value integral is "bounded below" by $\gg X^{1/2}$ as if this were a theorem derived from standard upper-bound technology. The safe claim is: even under Lindelof-type upper bounds, estimating the critical-line integral by absolute values gives at best about $X^{1/2+\epsilon}$, up to logarithms, and therefore fails to reach $X^{1/4+\epsilon}$. That is an upper-bound limitation, not a rigorous lower bound on the signed Perron integral.

7. Gemini's C3 "resolved debate" language is too strong. The algebraic collapse is proved only for a direct translation A-process on the alternating one-sequence representation. The two-coset representation may alter the spacing geometry. A genuine obstruction theorem would need to show that no useful two-coset spacing survives.

8. Gemini's near-collision proposal is important but unproved. Exact collisions give $\chi_4(ab)$; near-collisions

$$
d_1b-d_2a=\Delta\ne0
$$

may have residue-class fluctuations depending on $\Delta$, $a$, $b$, and $c$-parametrization. This must be tested before claiming a signed matrix norm is viable.

Possible errors or hidden assumptions:

1. **Overpromotion of H5a relative to H5r.** Gemini ends by suggesting that the most promising direction is the H5a rational-collision matrix. That is useful, but it risks losing the main Round 6 conclusion: H5r is the central bottleneck. Even a strong H5a estimate does not close the Vaaler route unless H5r-F is handled or bypassed.

2. **Sharp Perron endpoint fragility.** Gemini states Perron for $X\notin\mathbb Z$. The original lattice problem necessarily includes discontinuities at integer $X$ values. A proof route must either use half-weight conventions, avoid integer endpoints, or use a smoothed Perron formula and then unsmooth.

3. **Critical-line absolute-value language.** As noted above, the "bounded below" phrasing should be rejected. The true point is that absolute-value upper bounds on the critical line are too weak, even under Lindelof.

4. **Functional-equation inevitability.** The statement "one must apply the functional equation" should be softened. To exploit oscillation in the Perron integral, a functional equation or equivalent spectral/Voronoi input is the standard mechanism, but this is not a logical necessity theorem.

5. **Fourier-sign conventions in C2.** DeepSeek writes

$$
\sum_d f(d)e(\alpha d)=\sum_m\widehat f(m+\alpha)
$$

under the convention

$$
\widehat f(\xi)=\int f(u)e(-\xi u)\,du.
$$

With this convention the usual formula gives $m-\alpha$ rather than $m+\alpha$. For $\alpha=1/2$ this only relabels the half-integer set, so the final two-coset result survives. Still, the convention should be fixed before the lemma is entered.

6. **Stationary-phase constants.** DeepSeek's stationary-phase amplitude uses ordinary $e^{i\pi/4}$ and $\sqrt{2\pi/|\varphi''|}$ language while the phase convention is $e(t)=e^{2\pi i t}$. Constants are not essential for dual length, but a theorem-level lemma must use the correct $e(\operatorname{sgn}\varphi''/8)$-type factor and the correct power of $|\varphi''|^{-1/2}$.

7. **Derivative determinant for $F_2$.** The nonzero conclusion is correct, but the displayed formula is imprecise. For $F_2(x)=1/(4x)$, the exact determinant is

$$
F_2'F_2'''-3(F_2'')^2
=
-\frac{3}{8}x^{-6}.
$$

8. **H5r-B versus H5r-L1.** If H5r-B allows arbitrary complex coefficients $v_k$, then it is effectively a dyadic $L^1$ bound. The hierarchy should be recorded carefully:

$$
\text{dyadic }L^1 \simeq \text{H5r-B with arbitrary complex }v_k
\Rightarrow
\text{H5r-F}.
$$

The global H5r-L1 average over all $1\le |k|\le H_D$ is a useful stress norm but is not identical to uniform dyadic H5r-B unless localized in $K_0$.

9. **Li--Yang black-box risk.** DeepSeek's claim that Li--Yang "applies" should not be accepted until the exact theorem is audited. The correct Stage B position is: structurally compatible, theorem-level applicability unverified.

10. **Numerical tests as evidence.** Both agents propose useful numerical tests. They should be treated as convention checks and heuristic size probes, not proof evidence for asymptotic cancellation.

Suggested synthesis:

The synthesis should make H5r-F the official Round 8 target while preserving two auxiliary tracks: C2 normalization and rational-collision character bookkeeping.

The proof skeleton should be updated as follows.

**Primary target: H5r-F.**

For each dyadic block $D$ with

$$
X^{1/4}\le D\le X^{1/2},
\qquad
H_D\asymp D X^{-1/4},
$$

and for each residual family $S_\star(k,D)$ arising from H4, prove or test

$$
\left|
\frac1{H_D}
\sum_{1\le |k|\le H_D}
\eta_{k,H_D}S_\star(k,D)
\right|
\ll_\epsilon X^{1/4+\epsilon}.
$$

The route should explicitly include the zero mode:

$$
\frac1{H_D}S_\star(0,D)\ll D/H_D\asymp X^{1/4}.
$$

Only after this exact target is formalized should the stronger H5r-B target be invoked.

**Norm hierarchy.**

Add a lemma clarifying:

$$
\text{H5r-B}_{\mathrm{complex}}
\Longleftrightarrow
\text{uniform dyadic }L^1\text{ control}
\Longrightarrow
\text{H5r-F}
\Longrightarrow
\text{Vaaler residual bound}.
$$

H5r-F is the target. H5r-B is a safe sufficient estimate but may be too pessimistic and may collapse the problem back to character-blind divisor-type bounds.

**C2 status.**

Promote C2 only as a transformation lemma:

- two-coset Poisson formula: proved after sign convention fixed;
- alternating-sign representation: proved after sign convention fixed;
- stationary phase: partially proved, constants and boundary regimes pending;
- C3 parity collapse: diagnostic only, not a global obstruction.

**Mellin--Perron status.**

Keep Mellin--Perron as H10 comparison, not as the selected route. Record:

- sharp Perron truncation suggests $T\gg X^{3/4}$;
- absolute-value bounds on $\Re s=1/2$ fail to reach $X^{1/4}$;
- functional-equation analysis likely reconstructs Voronoi/Bessel reciprocal sums;
- all of this requires proof with smoothing and endpoint conventions.

**Rational-collision character lemma.**

Add Gemini's exact-collision observation as a narrow proved algebraic lemma:

If $(a,b)=1$, $d_1=ac$, $d_2=bc$, and $\chi_4(d_1)\chi_4(d_2)\ne0$, then $a,b,c$ are odd and

$$
\chi_4(d_1)\chi_4(d_2)=\chi_4(ab).
$$

This should be attached to a new rational-collision bookkeeping track, but not allowed to displace H5r-F as the central bottleneck.

Score by agent:

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|---|---:|---|---|
| `gemini_deep_think` | 7.4 | Strong structural ideas: Mellin--Perron as mirror, direct parity-collapse diagnostic, and exact-collision character factorization. The exact-collision $\chi_4(ab)$ observation is genuinely useful for signed matrix bookkeeping. Main weakness is overstatement: critical-line "lower bound" language, C3 treated as more resolved than it is, and a drift toward H5a despite H5r remaining central. | Prove the Mellin--Perron functional-equation-to-reciprocal-sum dictionary with smoothing and endpoint conventions; test near-collision signs; restate C3 as diagnostic rather than obstruction. |
| `deepseek_api` | 8.6 | Best Round 7 contribution. It correctly localizes the exact H5r norm target, reconciles the two C2 Poisson representations, identifies the dual length $kX/D^2$, and separates H5r-F from stronger arbitrary-coefficient or $L^1$ targets. Main weakness is premature confidence in Li--Yang applicability and some normalization imprecision. | Fix Fourier-sign and stationary-phase constants; formalize H5r-F sufficiency through the full Vaaler residual; audit Li--Yang's exact theorem and correct the double-sum phase dictionary. |

Next-round recommendation:

1. Make H5r-F the official target in the lemma bank and proof draft. Prove the implication

$$
\text{H5r-F}\Rightarrow
\text{total Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}
$$

with all dyadic $D$ blocks, both residual families, negative frequencies, and the $k=0$ mode included.

2. Add a norm-hierarchy lemma:

$$
\text{H5r-B}_{\mathrm{complex}}
\simeq
\text{uniform dyadic }L^1
\Rightarrow
\text{H5r-F},
$$

and explicitly state that H5r-F may be substantially weaker because it keeps the fixed Fejer coefficients.

3. Finalize C2 as a convention-fixed Poisson lemma. Include both forms, fix whether the dual frequencies are $m+\alpha$ or $m-\alpha$, derive the stationary-phase constants under $e(t)=e^{2\pi it}$, and isolate boundary regimes where $kX/D^2=O(1)$.

4. Audit Li--Yang/Bombieri--Iwaniec only after the correct H5r-B dictionary is written:

$$
e(kX/d)
=
e\left(k\frac{X}{D}F(d/D)\right),
\qquad
F(x)=1/x.
$$

The audit must verify coefficients, weights, allowed absolute values, and parameter ranges. Until then, record compatibility as structural, not theorem-level.

5. Add Gemini's exact-collision character factorization as a proved algebraic lemma, then run the proposed near-collision stress test. The output should determine whether $\chi_4(ab)$-type block signs persist for small nonzero collision defects.

6. Keep Mellin--Perron as a comparison module. Replace the phrase "Voronoi circularity trap" by "Voronoi reconstruction diagnostic." The next useful deliverable is a smoothed Perron formula with explicit truncation error and a functional-equation stationary-phase derivation of the dual length.

7. Numerical tests should prioritize H5r-F versus H5r-B/L1, not just H3 identity checks. The key ratios are

$$
R_F/R_{L1}
\qquad\text{and}\qquad
R_F/R_B,
$$

for square, nonsquare, and near-square $X$. These tests will indicate whether fixed Fejer coefficients carry cancellation lost under arbitrary-coefficient estimates.

--- REVIEW FROM gemini_deep_think ---
This is a Stage B cross review for Round 7.

### Most valuable input from others

The most valuable input from `gpt_pro_thinking` is the meticulous formalization of the normative dependency chain for the Vaaler residual: H5r-B $\implies$ H5r-F $\implies O_\epsilon(X^{1/4+\epsilon})$. By isolating the zero-mode contribution ($D/H_D \asymp X^{1/4}$) from the oscillatory nonzero modes, the agent correctly re-normalizes the conditional C1 diagnostic to an additive limit $P(X) \ll_\epsilon X^{\max(1/4, \theta)+\epsilon}$. This structural clarity prevents dangerous multiplicative scaling overshoots in future estimates and establishes the exact analytic minimum required by the positive-majorant Vaaler truncation. Additionally, the observation that the arbitrary-coefficient H5r-B target is structurally equivalent to a dyadic termwise $L^1$ estimate via duality perfectly crystallizes the analytic bottleneck: targeting arbitrary bounded coefficients appears to mathematically equate to discarding phase cancellation across the frequency variable $k$.

The most valuable input from `deepseek_api` is the definitive algebraic reconciliation of the odd-lattice Poisson formulations. By verifying that the two-coset representation (integer minus half-integer dual frequencies) and the alternating-sign representation ($(-1)^m$ coefficient) are mathematically identical up to parametrization, the agent removes representation ambiguity. Furthermore, the rigorous calculation of the derivative non-degeneracy condition for the shifted residual phases ($F_{2,1}(x)$ and $F_2(x)$) confirms that the H5r residual sums structurally reside within the known Bombieri-Iwaniec / Li-Yang reciprocal-sum phase class, anchoring the problem to known geometry.

### Claims that look correct

**The H5r Dependency Hierarchy:** The assertion by `gpt_pro_thinking` that H5r-B implies H5r-F via dyadic block decomposition and pointwise multiplication by bounded weights $\eta_{k,H_D}$ appears algebraically and logically sound. The deduction that arbitrary-coefficient H5r-B is essentially equivalent to dyadic termwise $L^1$ via duality is also correct and provides a crucial limitation on character-blind estimation techniques.

**The C1 Diagnostic Scaling:** The maximum scaling $\max(1/4, \theta)$ perfectly models the additive components of the Vaaler residual under the given hypotheses. Because the zero-mode evaluates to exactly $X^{1/4}$ and the oscillatory modes are bounded by $X^\theta$, the total error naturally scales additively rather than multiplicatively. This correction is mathematically robust.

**The Equivalence of C2 Representations:** The proof by `deepseek_api` linking the two-coset Poisson transform to the $(-1)^m$ formulation via the $d=2n+1$ substitution is flawless. This demonstrates that the parity dual factor is an intrinsic property of the B-process acting on $S_{\mathrm{odd}}$, rather than merely an artifact of Fourier convention.

**The Boundary Regime Breakdown:** Both agents correctly evaluate the stationary phase parameters, locating the stationary point at $u_0 \asymp \sqrt{kX/\ell}$ and determining the active dual length to be $\ell \asymp kX/D^2$. They correctly identify that for the critical endpoint block where $D \asymp X^{1/2}$ and $k \asymp 1$, the dual length drops to $\ell = O(1)$. Under these hypotheses, continuous B-process and uniform spacing lemmas fail unconditionally, as the integrals lack sufficient oscillation.

### Claims that need proof

**The H5r-F Analytic Escape Hypothesis:** Both agents suggest that H5r-F serves as the minimal target and might be easier to bound than H5r-B because it retains fixed, known Fejer coefficients $\eta_{k,H_D}$. However, the precise mechanism by which exponential sum techniques can exploit these slowly varying, monotonic Fejer coefficients to achieve a bound strictly stronger than arbitrary block sums requires explicit proof. As discussed below, Abel summation presents a significant hurdle to this hypothesis.

**Uniformity of Li-Yang Spacing for Shifted Phases:** `deepseek_api` applies the Li-Yang (2023) bounds directly to the phase $F_{2,1}(x) = 1/(x+1/D)$. While the derivative non-degeneracy condition formally holds for fixed parameters, robust proof is needed to show that the implicit spacing matrices in Bombieri-Iwaniec theories maintain uniform, non-degrading bounds as the geometric shift $1/D \asymp X^{-1/2}$ becomes microscopically small near the integration boundary.

**The Signed Fourier Truncation High-Frequency Tail:** `gpt_pro_thinking` lists signed Fourier truncation as a potential non-majorizing alternative (H10). Using this alternative would require showing that its high-frequency tail is either absolutely convergent or analytically bounded without reverting to absolute values. If absolute values are required to bound the tail, it would discard the $\chi_4$ character and recreate the exact Fejer trap we are trying to escape.

### Possible errors or hidden assumptions

**The Abel Summation (Monotonicity) Trap:** There appears to be a severe hidden assumption that H5r-F genuinely offers an analytic advantage over H5r-B. The Fejer weights $\eta_{k,H} = 1 - |k|/(H+1)$ are strictly decreasing and positive. By applying Abel summation (summation by parts), the Fejer sum transforms into a weighted average of partial sums. Consequently, bounding the Fejer sum appears to reduce to bounding the supremum of the partial sums. Because a partial sum is merely a special case of H5r-B evaluated with step-function coefficients, H5r-F seems structurally bottlenecked by the exact same exponent barrier as H5r-B for any character-blind method.

**The Two-Coset A-Process Fallacy:** `deepseek_api` posits that the two-coset formulation of C2 might survive an A-process (Weyl differencing) better than the $(-1)^m$ formulation. This appears to rely on a hidden assumption that cross-terms vanish cleanly. Squaring the two-coset sum yields $|\hat{F}(m) - \hat{F}(m-1/2)|^2$, which generates a cross-term $-2\Re(\hat{F}(m)\overline{\hat{F}(m-1/2)})$. Applying an A-process to this cross-term produces an amplitude modulation, but it does not inherently reconstruct an off-diagonal spacing advantage over standard integer-lattice divisor sums.

### Explicit Lemma Audits

$$\text{\bf Lemma Box 1: Summation-by-Parts Equivalence of H5r-F and H5r-B}$$

> **Status:** Proposed algebraic constraint.
> **Statement:** Let $\eta_{k,H} = 1 - k/(H+1)$ for $1 \le k \le H$. By summation by parts, the Fejer-weighted residual sum $\sum_{k=1}^H \eta_{k,H} S(k,D)$ is analytically bounded by the maximal partial sum $\sup_{K \le H} |\sum_{k=1}^K S(k,D)|$. This maximal partial sum exactly matches the structure of H5r-B with a step-function coefficient.
> **Significance:** Escaping the H5r-B barrier ($\theta^* \approx 0.314$) by appealing to H5r-F would require demonstrating that the Fejer weights induce a specific phase correlation not present in raw partial sums, which appears highly unlikely for character-blind estimates.

$$\text{\bf Lemma Box 2: Equivalence of Parity Dual Representations (C2)}$$

> **Status:** Proved algebraic identity.
> **Statement:** For $F(u) = w_D(u)e(kX/u)$, the two-coset formulation $\frac{1}{2}\sum_m [\widehat{F}(m) - \widehat{F}(m-1/2)]$ and the alternating sign formulation $\frac{1}{2}\sum_m (-1)^m \int F(u)e(-mu/2)du$ are exact algebraic equivalents under the substitution $d = 2n+1$. Any A-process parity collapse acting on the $(-1)^m$ coefficient necessarily manifests as an identical phase-interference obstruction in the two-coset model.

$$\text{\bf Lemma Box 3: Shifted-Phase Derivative Non-Degeneracy}$$

> **Status:** Proved arithmetic check.
> **Statement:** The phase $F_{2,1}(x) = 1/(x+1/D)$ for $x \asymp 1$ possesses derivatives satisfying the Bombieri-Iwaniec non-degeneracy condition $F'_{2,1}F'''_{2,1} - 3(F''_{2,1})^2 = -6(x+1/D)^{-6} \neq 0$.
> **Significance:** Consequently, the parity residual is not blocked by a vanishing continuous Hessian, embedding it firmly in the classical Dirichlet Divisor Problem spacing class. However, uniform bounds over the parameter $D$ must still be verified.

$$\text{\bf Lemma Box 4: Boundary Dual Length Degeneration}$$

> **Status:** Proved asymptotic limit.
> **Statement:** For the dyadic block $D \asymp X^{1/2}$ and frequencies $k \le c_0$, the dual Poisson variable $\ell \asymp kX/D^2$ satisfies $\ell = O(1)$.
> **Significance:** Under these hypotheses, the error term in the continuous stationary phase expansion fails to decay relative to the main term, requiring the problem to be estimated via exact discrete partial summation or primal exponent pairs in this specific boundary regime.

### Confidence calibration and failure modes

**Confidence: High** that the Vaaler residual bottleneck (H5r) structurally reduces to a known reciprocal-sum/divisor-problem barrier. The algebraic equivalence derivations are exact.
**Confidence: Low** that H5r-F provides an analytical escape route from the H5r-B limit. This is due to the monotonicity of the Fejer kernel under Abel summation, which suggests that fixed weights offer no deep cancellation advantage.
**Confidence: Low** that uniform continuous stationary phase arguments succeed without severe modification in the $D \asymp X^{1/2}$ boundary range.

The analytic route faces the following concrete failure modes:

1. **The Abel Summation Collapse (Failure Mode 1):** Any attempt to exploit H5r-F over H5r-B fails if summation-by-parts transforms the Fejer-weighted sum directly into an average of partial sums. If known technology cannot bound the raw partial sums (step-function bounded coefficients) below $X^{0.314}$, the Fejer sum definitively cannot reach the conjectural $X^{1/4}$ endpoint.
2. **The Short-Dual Boundary Obstruction (Failure Mode 2):** The proof skeleton relies heavily on dualizing the residual to exploit dual oscillation. If $D \asymp X^{1/2}$ and $k \asymp 1$, the dual phase is non-oscillatory ($\ell \asymp 1$). The dual method provides no statistical cancellation here, forcing a fallback to trivial primal bounds which may unconditionally exceed $X^{1/4+\epsilon}$.
3. **Parameter-Shift Spacing Degeneration (Failure Mode 3):** The Bombieri-Iwaniec spacing lemma bounds rational points near the curve $y = F'(x)$. For $F_{2,1}(x) = 1/(x+1/D)$, the curve geometry depends strongly on $D$. If the rational curvature bounds degrade as the shift $1/D$ alters the domain, the quoted $\theta^* \approx 0.314$ may not be uniformly attainable across all dyadic blocks, potentially pulling the exponent even higher.

### Concrete counterexample or stress-test checks

1. **Abel Summation Monotonicity Verification (Symbolic/Numerical):**
Compute the exact discrete Fejer residual $R_F = \left| \frac{1}{H_D} \sum_{k=1}^{H_D} \eta_{k, H_D} S_{\mathrm{odd}}(k, D) \right|$ for $X=1000, D=30$. Compare this to the partial sum supremum $R_P = \max_{1 \le K \le H_D} \left| \frac{1}{K} \sum_{k=1}^K S_{\mathrm{odd}}(k, D) \right|$. Check whether $R_F \asymp R_P$ uniformly over a range of parameter values. If they scale identically, it empirically validates Lemma Box 1 and suggests that fixed Fejer weights offer no analytic salvation over arbitrary step weights.
2. **Boundary Phase Integral Evaluation:**
Numerically integrate $I_m = \int_{D/2}^{2D} w_D(u) e(X/(2u^2) - mu/2) du$ for $X=100, D=10, k=1, m=-1, -2$. Compare the exact numerical integral against the $D^{3/2}/(kX)^{1/2}$ stationary phase prediction. This will accurately measure the precise magnitude of the asymptotic breakdown where the dual length $\ell \asymp 1$, verifying the severity of Failure Mode 2.

### Suggested synthesis

The Round 7 outputs provide a complete and rigorous map of the Vaaler residual bottleneck. The arithmetic route is fully reduced to evaluating shifted reciprocal sums (H5r) that belong structurally to the Li-Yang phase class. Because summation-by-parts forces H5r-F to be bounded by the maximum of partial sums, the positive-majorant Vaaler route appears to offer no cancellation advantage over arbitrary step-coefficients, leaving it strictly stalled at the Dirichlet Divisor Problem barrier ($\theta^* \approx 0.31448$).

The synthesis should formalize the equivalence of H5r-F and H5r-B (via Abel summation) as a diagnostic lemma to prevent circular attempts to bound the Fejer majorant. The repository state must explicitly recognize that the positive-majorant Vaaler-based arithmetic route is analytically bottlenecked at current technology levels.

For the next round, the research effort should pivot aggressively to the non-majorizing alternatives (H10). We must explicitly formulate the Mellin-Perron contour integrals and functional equations for $4\zeta(s)L(s, \chi_4)$ to determine whether their resulting Voronoi error terms retain the arithmetic $\chi_4$ character or suffer the same positive-majorant sign-degeneration.

### Score by agent

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
| --- | --- | --- | --- |
| `gpt_pro_thinking` | 9 | Superb logical stratification of H5r-B vs H5r-F, precise isolation of the zero mode, and accurate additive correction of the C1 scaling. | Evaluate the high-frequency tail of signed Fourier truncation explicitly to check absolute convergence. |
| `deepseek_api` | 9 | Flawless algebraic reconciliation of the C2 Poisson representations and rigorous validation of derivative non-degeneracy for shifted reciprocal phases. | Check if the two-coset cross-terms genuinely evade the A-process parity collapse or simply modulate the amplitude. |

### Next-round recommendation

1. **For `gpt_pro_thinking`:** Formalize the "Abel Summation Equivalence" (Lemma Box 1), demonstrating that H5r-F appears analytically trapped by the bounds on H5r-B partial sums. Then, shift focus to H10: specify the exact high-frequency tail of a sign-preserving Fourier truncation and verify if it can be bounded without taking absolute values.
2. **For `deepseek_api`:** Investigate the boundary regime $D \asymp X^{1/2}, k \asymp 1$ where the dual length is $O(1)$. Determine if standard one-dimensional exponent pairs applied directly to the primal sum can theoretically satisfy $3\kappa + 2\lambda \le 1$ to bypass the stationary phase breakdown.
3. **For `gemini_deep_think` (Self-Correction/Next Steps):** Fully develop the Mellin-Perron contour approach. Write out the exact shifted contour, the residues, and the Voronoi-style functional equation for $4\zeta(s)L(s,\chi_4)$ to see if the oscillating $\chi_4$ sign survives truncation and contour shifting, or if it reverts to a classical Bessel obstruction.

--- REVIEW FROM deepseek_api ---
# Stage B Cross Review -- Round 7

**Reviewer:** `deepseek_api` (DeepSeek API)
**Role:** Algebra checker, obstruction auditor, and stress tester
**Round:** 7
**Agents reviewed:** `gpt_pro_thinking`, `gemini_deep_think`
**Mandate:** Judge instructions required a norm-level H5r theorem, a corrected C1, a convention-fixed C2 Poisson lemma, a non-majorizing comparison table, a Mellin-Perron development with exact truncation, analysis of the two-coset parity dual, and a rational-collision matrix test. This review evaluates the Stage A outputs against those mandates, identifies hidden assumptions, and proposes a synthesis.

---

## 1. Most Valuable Input from Others

**From `gpt_pro_thinking`:**
- A **precise hierarchy of residual targets**:
  - **H5r-F** -- the minimal fixed-Fejer average, shown to be *exactly sufficient* to bound the Vaaler residual at the conjectural scale (Lemma R1).
  - **H5r-B** -- a stronger, arbitrary-coefficient target, which by duality is essentially equivalent to a dyadic termwise   $L^1$ estimate (Lemma R3).
  - The logical chain $\text{H5r-B} \Rightarrow \text{H5r-F} \Rightarrow \text{Vaaler residual} \ll_\epsilon X^{1/4+\epsilon}$ is proved (Lemmas R1-R3).
- A **corrected conditional diagnostic C1**, with the proper scaling $X^{\max(1/4,\theta)+\epsilon}$ instead of the erroneous $X^{1/4+\theta}$.
- A **convention-fixed C2 Poisson lemma** for the odd-lattice sum, together with two equivalent representations and a preliminary stationary-phase analysis that yields dual length $m \asymp kX/D^2$.
- A **comparison table** of non-majorizing alternatives (Vaaler, signed Fourier, Mellin--Perron) that explicitly records which sign structures are preserved.

**From `gemini_deep_think`:**
- A **quantitative Mellin--Perron diagnostic**: the sharp Perron truncation requires $T \gg X^{3/4-\epsilon}$; any absolute-value treatment of the critical-line integral is $\gg X^{1/2}$ and thus blocks the conjectural endpoint; applying the functional equation regenerates reciprocal sums of length $\asymp X^{1/2}$ -- a structural "isomorphism" to the Vaaler bottleneck.
- A **rational-collision matrix analysis** showing that for exact collisions $(d_1,d_2)$ with $d_1 b = d_2 a$ and $(a,b)=1$, the character product reduces to $\chi_4(ab)$, i.e. a block-constant sign. The observation that character-blindness enters only when *matrix norms take absolute values* is a sharp diagnostic.
- An **algebraic check of the two-coset parity A-process**: writing the dual as half-integer frequencies $\mu = m/2$, the alternating factor $(-1)^{2\mu}$ collapses to $+1$ under a direct differencing shift $\mu \mapsto \mu+q$, confirming that direct A-process destroys the parity oscillation.

Both agents have delivered mathematically useful contributions that are largely complementary.

---

## 2. Detailed Assessment of `gpt_pro_thinking`

### 2.1 Correctness and Rigour

The arithmetic backbone (H1--H3) is used consistently. The floor-compatible sawtooth $\psi(t)=t-\lfloor t\rfloor-\frac12$ is carried through the whole derivation. The Vaaler approximation is invoked with the Fejer majorant:

$$
|R_H(t)|
\le \frac{1}{2H+2} K_H(t),\qquad
K_H(t) = 1 + \sum_{1\le|k|\le H} \eta_{k,H} e(kt),\;
\eta_{k,H}=1-\frac{|k|}{H+1}.
$$

The residual bound for the first leg is derived as

$$
\Bigl|\sum_d \chi_4(d) w_D(d) R_{H_D}(X/d)\Bigr|
\ll \frac{1}{2H_D+2}
\Bigl( S_{\mathrm{odd}}(0,D) + \sum_{1\le|k|\le H_D} \eta_{k,H_D} S_{\mathrm{odd}}(k,D) \Bigr),
$$

where $S_{\mathrm{odd}}(k,D) = \sum_{2\nmid d} w_D(d) e(kX/d)$. The second leg is treated analogously, giving families $S_\rho(k,D)$ for $\rho=1,3$. These algebraic reductions are **exact** under the pointwise majorant and the non-negativity of $w_D$.

The zero-mode term is $\asymp D/H_D \asymp X^{1/4}$. Hence the required **residual target** is the fixed-Fejer average of the nonzero modes:

$$
\boxed{\text{H5r-F: } \Bigl| \frac1{H_D} \sum_{1\le|k|\le H_D} \eta_{k,H_D} S_\star(k,D) \Bigr| \ll_\epsilon X^{1/4+\epsilon}}.
$$

This is a genuine **minimum requirement**; Lemma R1 proves that if H5r-F holds for every dyadic $D$ in $[X^{1/4},X^{1/2}]$, then the total Vaaler residual is $O_\epsilon(X^{1/4+\epsilon})$.

Lemmas R2 and R3 establish the implications

$$
\text{H5r-B} \;\Longrightarrow\; \text{H5r-F}, \qquad
\text{H5r-B} \;\Longleftrightarrow\; \text{dyadic } L^1 \text{ estimate}.
$$

These are elementary but crucial for clarifying what the proof actually needs.

The corrected C1 diagnostic states:

$$
P(X) \ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

under the assumption that the only available H5r bounds are character-blind reciprocal estimates at exponent $\theta$. This is logically sound; the "max" correctly reflects the zero-mode floor.

The C2 Poisson lemma is presented with a clear Fourier convention $\widehat F(\xi)=\int F(u)e(-\xi u)du$ and shown to have two equivalent forms. The stationary-phase sketch correctly identifies the active dual length $|m|\asymp kX/D^2$ and the phase shape $\sqrt{2kXm}$.

**Overall, the reasoning is transparent and logically rigorous. There are no over-reaching claims.**

### 2.2 Potential Issues or Hidden Assumptions

1. **Vaaler reference unverified.** The majorant constant $\frac1{2H+2}$ is plausible but should be checked against a standard source (Montgomery--Vaughan, *Multiplicative Number Theory I*, §6.2, or Vaaler, *Bull. AMS* 12 (1985), 183--216). The exact coefficient formula for the main terms (needed for H5a/H5b) also needs auditing.
2. **Dyadic partition non-negativity.** The residual majorant argument uses $w_D(d)\ge0$ to pass absolute values inside the sum. If a signed dyadic partition is used in the main terms, one must either replace it by $|w_D|$ in the residual or provide an additional bound. This is a minor technical point but must be recorded in the lemma bank.
3. **Stationary-phase constants.** The phase constant $e(1/8)$ is given without derivation; the amplitude prefactor is not spelled out. A complete stationary-phase lemma would need those together with uniform error terms. This is a known gap and is acknowledged.
4. **Boundary ranges.** The cases $D\asymp X^{1/2}$ with $k\asymp1$ (dual length $O(1)$) and $D\asymp X^{1/4}$ with $H_D\asymp1$ are noted but not treated quantitatively. They form a genuine analytical gap.
5. **Absolute-value placement in H5r-F.** The Fejer average is taken with a single outer absolute value after summation over $k$. This is the correct level for the Vaaler route; it is weaker than termwise absolute values and may permit cancellation between Fejer modes. The agent correctly distinguishes this from H5r-L1.

None of these issues invalidate the main contributions; they are implementational details.

---

## 3. Detailed Assessment of `gemini_deep_think`

### 3.1 Correctness and Rigour

The agent provides a series of diagnostic computations that are **largely correct** under their stated hypotheses.

- **Mellin--Perron truncation:** The sharp Perron formula with error $O(X^{1+\epsilon}/T)$ is standard, and the requirement $T\gg X^{3/4-\epsilon}$ for the endpoint error is correct.
- **Critical-line barrier:** Shifting to $\Re(s)=1/2$ and bounding the vertical integral by $X^{1/2}\int_{-T}^T |Z(1/2+it)| dt/(1+|t|)$ is sound. Even under Lindelof, this is $\gg X^{1/2}$, demonstrating that an absolute-value treatment fails by a large margin.
- **Functional-equation isomorphism:** The argument that applying the asymmetric functional equation for $4\zeta(s)L(s,\chi_4)$ and using stationary phase regenerates reciprocal sums of length $\sim T^2/X$, which for $T=X^{3/4}$ gives length $\sim X^{1/2}$, is a correct *heuristic*. It shows that the Mellin--Perron route is structurally tied to the same reciprocal-sum bottleneck.
- **Two-coset parity A-process:** Writing the dual as a sum over half-integers $\mu=m/2$ with coefficient $c_\mu=(-1)^{2\mu}$, the product $c_\mu c_{\mu+q}=(-1)^{2q}$ is indeed constant. Hence a direct Weyl differencing eliminates the alternating factor. Algebraically this is correct.
- **Rational-collision exact-collision sign:** For $d_1=ac$, $d_2=bc$ with $(a,b)=1$, oddness of $a,b,c$ forces $c$ to be odd, so $\chi_4(c)^2=1$ and $\chi_4(d_1)\chi_4(d_2)=\chi_4(ab)$. This is elementary and correct.

**Overall, the diagnostic computations are rigorous within their stated assumptions.** However, the interpretation occasionally crosses from " diagnostic" to "theorem" language, which needs careful demotion.

### 3.2 Potential Issues or Over-interpretations

1. **Near-collision sign behaviour.** The exact-collision analysis does **not** automatically apply to the actual Bombieri--Iwaniec setting, where one has $|d_1 b - d_2 a| \le \Delta$. The character product may well depend on the residues and could average to zero over a near-collision block. The claim that the character "forms a uniform, block-constant sign" for the *entire* collision trajectory is **unverified for near-collisions** and must be demoted to a **conjecture** until a near-collision lemma is proved.
2. **Two-coset A-process over-interpretation.** The algebraic collapse proves only that a *direct uniform differencing* destroys the alternating factor. It does **not** rule out bilinear or spacing arguments that exploit the parity structure before differencing. The conclusion should remain a **conditional diagnostic**, not a proof of analytic sterility.
3. **Mellin--Perron "structural isomorphism".** The path from the functional equation to Voronoi/Bessel reciprocal sums is well-known, but the statement that it "reconstructs the exact same reciprocal-sum bottlenecks" is an **informal equivalence**. A rigorous translation would require mapping the contour integral to a dyadic sum with explicit weights and proving equivalence in difficulty. The current phrasing can be misread as a theorem.
4. **Smoothed Perron parameter.** The claim that a smoothed Mellin transform with transition width $\asymp X^{1/4}$ requires effective support $T\asymp X^{3/4}$ is plausible but needs a precise lemma (e.g., using the exponential integral or a kernel with rapid decay). Currently it is only sketched.
5. **Lack of alignment with H5r-F.** The agent does not discuss the new H5r norm hierarchy, which is the central topic of Round 7. This limits direct synthesis with `gpt_pro_thinking`'s work, but it is not an error per se; the agent followed a different strand of the judge instructions.

---

## 4. Claims that Look Correct

- **H5r-F** is the correct minimal residual target for the current Vaaler route (derived correctly by `gpt_pro_thinking`).
- **Lemma R1**: $\text{H5r-F} \Rightarrow$ Vaaler residual $\ll_\epsilon X^{1/4+\epsilon}$ (proof sound).
- **Lemma R2**: $\text{H5r-B} \Rightarrow$ H5r-F (elementary, correct).
- **Lemma R3**: $\text{H5r-B}$ is equivalent (for complex $v_k$) to the dyadic $L^1$ estimate $\sum_{k\sim K_0}|S_\star(k,D)| \ll_\epsilon K_0 X^{1/4+\epsilon}$.
- **C1 corrected diagnostic**: $P(X) \ll_\epsilon X^{\max(1/4,\theta)+\epsilon}$ under character-blind H5r inputs (scaling now standard).
- **C2 Poisson formula**: the two equivalent representations of the odd-lattice sum are valid under the stated Fourier convention.
- **Dual length from C2**: $|m| \asymp kX/D^2$ is correct from stationary phase.
- **Mellin--Perron truncation**: $T\gg X^{3/4-\epsilon}$ is necessary for endpoint error; critical-line absolute-value integral is $\gg X^{1/2}$.
- **Exact-collision character product**: $\chi_4(d_1)\chi_4(d_2) = \chi_4(ab)$ when $d_1 b = d_2 a$ and $(a,b)=1$, with $a,b,c$ odd.
- **Dual-parity A-process algebra**: $c_\mu c_{\mu+q}=(-1)^{2q}$ is constant for shift $q$, showing collapse under direct differencing.

These claims are mathematically solid and should be promoted to the lemma bank with appropriate statuses.

---

## 5. Claims that Need Proof

- **H5r-F is endpoint-strength and unproved** -- it is a target, not a theorem. The repo must treat it as an open problem.
- **Near-collision block-constant sign** (gemini's exact-collision extension to $|\Delta|>0$). Needs a lemma with error term.
- **Mellin--Perron functional-equation mapping** -- requires a rigorous lemma translating the contour integral to explicit dyadic reciprocal sums, with error bounds and coefficient formulas.
- **Smoothed Perron effective support** -- needs a precise statement linking transition width to required truncation height.
- **C3 two-coset spacing viability** -- no proof yet that the half-integer dual phases retain usable spacing information after a B-process or other transform.
- **Stationary-phase constants for C2** -- the $e(1/8)$ phase and amplitude prefactor need derivation and verification.
- **Boundary regimes ($D\asymp X^{1/2}$, $k\asymp1$; $D\asymp X^{1/4}$)** -- these require separate analysis, not yet supplied.
- **Fejer average vs. dyadic $L^1$ separation** -- while the implication chain is proved, the question of whether H5r-F is *strictly easier* than H5r-B is an open empirical / theoretical question that needs stress testing.

---

## 6. Possible Errors or Hidden Assumptions

1. **Vaaler majorant constant.** The agent uses $\frac{1}{2H+2}$; a standard reference (e.g., Montgomery--Vaughan, p. 117) gives the Fejer kernel as $\frac{1}{H+1}\bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\bigr)^2$, and the majorant constant is often $\frac{1}{H+1}$. The factor 2 difference is harmless for asymptotics, but must be checked to avoid constants that might accumulate across $O(\log X)$ blocks.
2. **Positivity assumption for dyadic weights.** $w_D(d)\ge0$ is used in majorizing the residual. If the actual dyadic decomposition uses signed weights, the bound fails. Usually one can take $|w_D|$ for the residual argument, but this must be stated.
3. **Floor-compatible $\psi$ versus Fourier-centered sawtooth.** The discontinuous $\psi$ is approximated by a continuous Vaaler polynomial plus a residual. The agent's argument retains the residual pointwise, so the half-jump at integers is absorbed in the Fejer majorant. This is safe **provided** the sum over $d$ is taken before applying absolute values to the residual -- which is exactly what is done.
4. **Gemini's claim on "reconstructs the exact same reciprocal-sum bottlenecks".** This is a heuristic, not a rigorous theorem. If taken as a proven impossibility, it would be an overstatement.
5. **Over-promotion of parity A-process collapse.** The algebra shows only that direct differencing kills the alternating factor. A bilinear or matrix method might still exploit the parity before applying such a transform. This nuance is often lost in summary.
6. **Incomplete engagement with H5r-F by `gemini_deep_think`.** The judge instructions implicitly required all agents to address the new norm hierarchy, but `gemini` did not do so. This is a gap in coverage, not an error in the mathematics presented.
7. **Potential misuse of the term "isomorphism"** for the Mellin--Perron ↔ Voronoi connection. Without explicit coefficient-for-coefficient mapping, it remains a structural analogy.

Each of these should be explicitly flagged in the next round's reading packet.

---

## 7. Explicit Correction / Verification Items

1. **Vaaler theorem audit** -- retrieve the exact statement from a standard reference, verify the majorant constant and the coefficient formula for $\alpha_{h,H}$. Record as H4 in the lemma bank with source.
2. **Fourier convention check for C2** -- derive the $\frac12\sum_{m}(-1)^m$ formula step-by-step from the Poisson summation formula with the chosen $\widehat F(\xi)=\int F(u)e(-\xi u)du$. Verify equivalence with the two-coset representation.
3. **Stationary-phase constants** -- for $I_{-\ell} = \int w_D(u)e(kX/u + \ell u/2) du$, compute $u_0$, $\phi''(u_0)$, amplitude, and phase shift, including the $1/8$ term. Compare with a known theorem (e.g., Stein, *Harmonic Analysis*, §VIII.7) and test numerically.
4. **H5r-B ↔ dyadic $L^1$ equivalence proof (Lemma R3)** -- write the precise duality argument: for any $S_\star$, $\sup_{|v_k|\le1} |\sum_{k\sim K_0} v_k S_\star(k,D)| = \sum_{k\sim K_0} |S_\star(k,D)|$. Confirm that the Fejer coefficients $\eta_{k,H_D}$ are real and satisfy $|\eta_{k,H_D}|\le1$.
5. **Near-collision character product lemma** -- for $d_1 = a c + r$, $d_2 = b c + s$ with small $|r|,|s|$, derive $\chi_4(d_1)\chi_4(d_2)$ explicitly in terms of $\chi_4(ab)$, the residues $r,s$, and the parity of $c$. Determine under what range the block-sign remains stable.
6. **Mellin--Perron rigorous mapping** -- write the functional equation for $4\zeta(s)L(s,\chi_4)$ and perform the contour shift to $\Re(s)=\frac12$ with explicit error analysis. Derive the resulting dual sum and compare its structure (length, phase, coefficient class) with H5a/H5b/H5r.
7. **Numerical stress tests** (see Section 9) -- implement and report results.

---

## 8. Failure Modes

1. **H5r-F intractable** -- if the fixed-Fejer average proves to be as hard as the divisor-problem $L^1$ estimate, the current Vaaler route cannot reach $1/4$. The project would then need a sign-preserving truncation or a fundamentally different method.
2. **Near-collision sign randomness** -- if the character product $\chi_4(d_1)\chi_4(d_2)$ averages to zero for typical near-collisions, the block-constant sign escape hatch closes, and H5a/H5b must be treated as character-blind (or effectively character-blind after matrix norms).
3. **Discontinuity handling oversight** -- if the proof fails to account for the half-jump of $\psi$ at integers in a future streamlined version (e.g., by omitting the residual), the entire estimate could silently break. The current majorant approach is safe, but any simplification must retain the residual.
4. **Fejer majorant constants accumulation** -- if the dyadic partition and majorant constants are not controlled uniformly, the implicit logarithm may hide a larger constant that prevents a clean $X^{1/4+\epsilon}$ bound. This is unlikely to create an asymptotic obstruction but could affect small-$X$ explicit bounds.
5. **Gemini's "isomorphism" taken as a proof of impossibility** -- if the repo treats the Mellin--Perron circularity as a theorem, it might prematurely discard a viable pathway. The correct status is "strong diagnostic, not a theorem".
6. **C2/C3 over-promotion** -- if the parity collapse is interpreted as a proof that B-process-first always fails, the project might miss a spacing-based resolution of H5r using the two-coset formulation. This would be a false exclusion.

---

## 9. Stress Tests

1. **Fixed-Fejer versus termwise $L^1$ separation.** For moderate $X$ (e.g., $X=10^5$), $D\approx X^{1/2}$, $H_D = D X^{-1/4}$, compute:

$$
F_D = \frac1{H_D}\Bigl|\sum_{1\le|k|\le H_D} \eta_{k,H_D} S_{\text{odd}}(k,D)\Bigr|,\qquad
L_D = \frac1{H_D}\sum_{1\le|k|\le H_D} |S_{\text{odd}}(k,D)|.
$$

If $F_D \ll L_D$, then H5r-F is genuinely easier than $L^1$, justifying further work on the Fejer-weighted target. If $F_D \approx L_D$, the distinction is academic for practical purposes.

2. **C2 stationary-phase validation.** Use a smooth bump $w_D$ with $D=100$, $k=10$, $X=10^4$, and numerically evaluate $I_{-\ell}$ for $\ell$ around $kX/D^2$. Compare the amplitude and phase with the stationary-phase prediction. Check the $e(1/8)$ constant and verify that non-stationary $\ell$ give rapid decay. This tests the correctness of the derived dual-length formula and the phase constant.

3. **Near-collision sign bias test.** Fix $D=500$, $a=1$, $b=3$. For each small $\Delta \in [-5,5]$, collect all odd $d_1,d_2\sim D$ with $|3 d_1 - d_2| = \Delta$ and compute the empirical mean $\mathbb{E}[\chi_4(d_1)\chi_4(d_2)]$. A persistent nonzero mean would support the block-constant conjecture; rapid averaging to zero would indicate that the character acts like random noise at the near-collision scale.

4. **Mellin--Perron integral size.** Integrate numerically $I(T)=\int_1^T |\zeta(1/2+it)L(1/2+it,\chi_4)| dt / t$ for $T$ up to $10^5$. Verify that $I(T)$ does not decay and is consistent with $\gg \log T$ or constant, confirming the critical-line barrier.

---

## 10. Suggested Synthesis

The Round 7 outputs together sharpen the research state as follows:

- The **Vaaler route** is now fully specified: the exact residual target is **H5r-F**. No further ambiguity remains about which norm is required. The route is **logically complete** once H5r-F is supplied.
- The **Mellin--Perron diagnostic** correctly identifies that contour methods face the same reciprocal-sum bottleneck after the functional equation; thus it does not provide an escape, but it serves as a useful mirror.
- The **rational-collision block-sign property** suggests a potential new tool: if near-collisions also preserve a block-constant character sign, one might estimate the *signed* bilinear form directly, bypassing the Fejer majorant's sign-loss. This could either **replace H5r-F** with a signed truncation residual, or **strengthen** the H5a estimate.
- The **parity dual (C2/C3)** remains a diagnostic, not a closed door. While direct A-process collapses the alternating factor, the two-coset formulation may retain usable phase spacing.

**Recommended synthesis for the next round:**
- Promote the H5r norm hierarchy (Lemmas R1-R3, C1, C2) to the lemma bank with cleared statuses.
- Simultaneously pursue **two experimental lines**:
  1. **Numerical stress tests** on H5r-F vs. H5r-B/L1, Fejer spikes, and C2 stationary phase.
  2. **Theoretical development of the near-collision sign lemma**: can we prove that $\chi_4(d_1)\chi_4(d_2) \approx \chi_4(ab)$ for typical near-collisions? If positive, this could feed into a signed matrix estimate.
- Keep the Mellin--Perron route as a secondary diagnostic, but do not invest heavy effort unless a new contour idea (e.g., non-vertical paths, double-integrals) emerges.

---

## 11. Score by Agent

| Agent reviewed | Score (0--10) | Main reason | Must verify next |
|---|---:|---|---|
| **gpt_pro_thinking** | 9 | Highly detailed, rigorous norm hierarchy, clean implications, no overclaims. | Vaaler reference, stationary-phase constants, H5r-F numerical tests. |
| **gemini_deep_think** | 7 | Valuable structural diagnostics (Mellin--Perron, rational-collision); some claims need demotion (near-collision block-sign, parity A-process as full obstruction) and missing engagement with H5r-F hierarchy. | Near-collision sign lemma, rigorous Mellin--Perron mapping, two-coset spacing viability, align with H5r-F. |

---

## 12. Next-Round Recommendation

1. **Update lemma bank** with H5r-F, H5r-B, H5r-L1 and the implication lemmas R1-R3, C1, C2. Mark C3 as diagnostic only.
2. **Audit the Vaaler theorem** and commit H4 (with precise reference) to the lemma bank.
3. **Conduct numerical stress tests** (Fejer-average vs. L1, C2 stationary-phase, near-collision sign bias) and report the results.
4. **Task `gemini_deep_think`** to:
   - Formalise the rational-collision observation into a conditional lemma with error term for near-collisions.
   - Write a rigorous mapping from the Perron integral to dyadic reciprocal sums via the functional equation, with explicit constants and error bounds.
   - Downgrade the language of "isomorphism" and "sterile" to diagnostic status.
5. **Task `gpt_pro_thinking`** to:
   - Extend the non-majorizing comparison table with a column for "character preservation".
   - Explore whether a signed Vaaler-type polynomial (or signed Fourier truncation) could yield a residual that retains $\chi_4$, i.e., a signed residual target that might be easier than H5r-F.
   - Incorporate the Poisson-Bessel calibration proof as a secondary sanity check.
6. **Retain the Mellin--Perron route** as a secondary mirror, but avoid spending primary effort on it unless a novel contour idea is found.

---

## 13. Confidence Calibration and Failure Modes

- **H5r-F as the minimal target:** *High confidence* that this is the correct analytic requirement for the Vaaler route. *Low confidence* that it can be proved without a breakthrough, because it is an endpoint-strength reciprocal-sum input.
- **Mellin--Perron circularity:** *Moderate-high confidence* that the functional equation regenerates reciprocal sums of length $\asymp X^{1/2}$; this is a strong obstruction, but not yet a theorem that *all* Perron-type methods are doomed. New contour ideas could, in principle, avoid this.
- **Rational-collision block-sign:** *Low-to-moderate confidence* that the sign stability extends to near-collisions; the exact collision algebra is correct, but the transition to the required Bombieri--Iwaniec spacing regime is a major open gap.
- **Parity dual C2/C3:** *Moderate confidence* that direct A-process kills the alternating factor; *low confidence* that this precludes all spacing-based gains because the two-coset formulation may still encode useful phase shifts.
- **Overall project status:** The repo now has a crystal-clear proof skeleton and a precisely formulated central bottleneck. No exponent improvement has been proved; the present work is a high-quality **reduction and diagnostic map**.

**Potential catastrophic failure mode:** If H5r-F turns out to be strictly equivalent (in difficulty) to the full divisor-problem conjecture, then the Vaaler route adds no advantage over a direct attack on the divisor problem. The project would then need to hunt for a sign-preserving truncation or a different global method. The numerical stress tests are crucial to gauge this risk.

---

*End of Stage B Cross Review -- Round 7*

## Required Output Schema

Selected main route:
Useful fragments by source:
Rejected or risky ideas:
Known gaps:
New lemmas to add:
Counterexample checks to run:
Next round instructions:
Confidence:
