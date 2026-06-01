You are the judge agent: GPT Pro Thinking.

Synthesize Round 6. Prefer precise, checkable progress over impressive prose.

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

Generated after round 5 in run web-research-test.

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

Responses, reviews, and judge synthesis are archived under
ounds/web-research-test/round_005/.

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

This is the Round 6 Stage A output for `gpt_pro_thinking`. The active Round 6 instruction is to continue from the current state, make concrete progress on the prior judge instructions, and explicitly separate proved claims from proof gaps. The current reading packet says Round 5 downgraded the arithmetic route from a promising proof route to a structured reduction plus obstruction map, with H5r now the central bottleneck.

Concrete progress in this response:

1. I formalize C1 as a conditional proposition, not as a theorem or lower bound.
2. I give the exact H5r-to-Li--Yang dictionary for $C_1$ and $C_{2,\rho}$, including residue splitting, phase functions, local ranges, derivative checks, and absolute-value placement.
3. I prove the core algebraic part of C2 by Poisson summation modulo $2$: the parity residual $1_{2\nmid d}$ dualizes to the factor $(-1)^m$, and direct A-process differencing collapses it to a constant.
4. I compare three truncation frameworks: Vaaler with Fejer majorant, signed Fourier truncation, and Mellin--Perron. The conclusion is that Vaaler makes H5r explicit, signed Fourier moves the problem to uncontrolled high-frequency tails, and Mellin--Perron replaces H5r by moment/subconvexity requirements for $\zeta(s)L(s,\chi_4)$.
5. I keep the Poisson--Bessel calibration route as a secondary proof module, not as a main route.

No exponent improvement is proved.

Main claim or direction:

The main arithmetic route should remain in the repository, but only as a precise reduction and obstruction map:

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

The current decisive obstruction is H5r. The Vaaler residual produces parity-supported and untwisted reciprocal sums. These are structurally in the same broad reciprocal-sum class as the sums in the Gauss/divisor Bombieri--Iwaniec framework, but they no longer carry the signed $\chi_4$ structure. Li--Yang's paper states that their improvement for both Gauss and divisor uses Bombieri--Iwaniec, a new first-spacing estimate, and Huxley's second-spacing work; their exponent is $\theta^*=0.314483\ldots$, while this project's target is $\theta=1/4$.

Therefore the next viable work should split into two parallel tracks:

1. Complete the Vaaler route honestly, with H5r treated as a mandatory endpoint-strength target.
2. Develop non-majorizing or sign-preserving alternatives, and determine exactly what replaces H5r.

Detailed reasoning:

## 1. C1 as a conditional proposition

The current Vaaler route uses the proved floor-compatible identity

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

For dyadic $d\asymp D$, the local Vaaler height is

$$
H_D\asymp D X^{-1/4}
$$

for

$$
X^{1/4}\le D\le X^{1/2}.
$$

The Vaaler residual produces the H5r families

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d),
$$

and

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

Here $v_k$ should be a smooth dyadic Fejer/dyadic weight, not arbitrary signs. The residual contribution has the form

$$
\frac{D}{H_D}
+
\frac{1}{H_D}
\sum_{K_0\le H_D}
\left|C_i(K_0,D;X)\right|
$$

up to harmless logarithmic losses.

**C1, precise conditional form.**
Suppose the only available estimates for the H5r families are character-blind reciprocal-sum bounds of exponent $\theta$, namely

$$
C_1(K_0,D;X),\ C_{2,\rho}(K_0,D;X)
\ll_\epsilon
K_0 X^{\theta+\epsilon}
$$

uniformly for

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le K_0\le H_D.
$$

Then the Vaaler route gives at best, from these inputs,

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon},
$$

assuming the main Vaaler families H5a and H5b are no worse.

Proof: the zeroth Fejer mode contributes

$$
\frac{D}{H_D}\asymp X^{1/4}.
$$

The nonzero residual modes contribute

$$
\frac{1}{H_D}
\sum_{K_0\le H_D}
K_0X^{\theta+\epsilon}
\ll_\epsilon
X^{\theta+\epsilon}
$$

after dyadic summation. Therefore if $\theta>1/4$, the residual blocks the endpoint $X^{1/4+\epsilon}$ within this proof skeleton.

This proves only a conditional limitation of the Vaaler proof route. It does not prove that H5r cannot satisfy the endpoint bound, and it does not prove equivalence to the Dirichlet divisor problem.

## 2. H5r-to-Li--Yang dictionary

The local H5r ranges are

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le K_0\le H_D\asymp D X^{-1/4}.
$$

The relevant reciprocal phase template is

$$
\sum_{k\sim K_0}g(k/K_0)
\sum_{m\sim M}G(m/M)
e\left(\frac{kX}{M}F(m/M)+\mu k\right),
$$

with $M\asymp D$ and $F$ smooth on a fixed compact subinterval of $(0,\infty)$.

Li--Yang describe double exponential sums of this general reciprocal type as standard in the circle and divisor problems, using the Bombieri--Iwaniec method and spacing estimates.

### 2.1 Dictionary for $C_1$

Start with

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_d
1_{2\nmid d}w_D(d)e(kX/d).
$$

Split the parity condition as $d=2m+1$. Put $M=D/2$ and $m\asymp M$. Then

$$
\frac{kX}{d}
=
\frac{kX}{D}
F_{2,1}\left(\frac{m}{M}\right),
$$

where, taking $D=2M$ for notation,

$$
F_{2,1}(x)=\frac{D}{2Mx+1}
=
\frac{1}{x+1/D}.
$$

Thus

$$
C_1(K_0,D;X)
=
\sum_{k\sim K_0}v_k
\sum_{m\sim M}W(m/M)
e\left(\frac{kX}{D}F_{2,1}(m/M)\right).
$$

Derivative check:

$$
F_{2,1}'(x)=-(x+1/D)^{-2},
$$

$$
F_{2,1}''(x)=2(x+1/D)^{-3},
$$

$$
F_{2,1}'''(x)=-6(x+1/D)^{-4}.
$$

Therefore

$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2
=
6(x+1/D)^{-6}
-
12(x+1/D)^{-6}
=
-6(x+1/D)^{-6},
$$

which is uniformly bounded away from zero on fixed dyadic support away from $0$.

So $C_1$ is structurally a Li--Yang/Bombieri--Iwaniec reciprocal sum after parity splitting. The obstruction is not malformed phase geometry. The obstruction is that $C_1$ is character-blind except for parity support.

### 2.2 Dictionary for $C_{2,\rho}$

Start with

$$
C_{2,\rho}(K_0,D;X)
=
\sum_{k\sim K_0}v_k e(k\rho/4)
\sum_d
w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

This already has no denominator congruence condition. It fits the same template with

$$
\frac{kX}{4d}
=
\frac{kX}{D}
F_2(d/D),
$$

where

$$
F_2(x)=\frac{1}{4x}.
$$

The factor $e(k\rho/4)$ is a harmless additive phase in the $k$ variable; it may be absorbed into the outer weight if the theorem allows smooth or bounded-variation oscillatory $k$-weights, or treated as a fixed phase shift.

Derivative check:

$$
F_2'(x)=-\frac{1}{4}x^{-2},
$$

$$
F_2''(x)=\frac{1}{2}x^{-3},
$$

$$
F_2'''(x)=-\frac{3}{2}x^{-4}.
$$

Then

$$
F_2'F_2'''-3(F_2'')^2
=
\frac{3}{8}x^{-6}
-
\frac{3}{4}x^{-6}
=
-\frac{3}{8}x^{-6},
$$

again uniformly nonzero on fixed dyadic support.

Thus both $C_1$ and $C_{2,\rho}$ fit the same broad reciprocal phase class as the main terms. The distinction is arithmetic: H5r lacks the signed $\chi_4$ structure.

### 2.3 Absolute-value placement

The intended H5r formulation should use block-level absolute values:

$$
\frac{1}{H_D}
\sum_{K_0\le H_D}
\left|
C_i(K_0,D;X)
\right|.
$$

It should not use termwise absolute values in $k$:

$$
\frac{1}{H_D}
\sum_{k\le H_D}
\left|
\sum_d c_d w_D(d)e(kX/d)
\right|.
$$

The termwise version discards the two-variable structure and activates the one-dimensional H6 obstruction too early. The blockwise version still asks for endpoint-strength double-sum estimates.

## 3. C2: Poisson calculation for the parity residual

Let

$$
S_{\mathrm{odd}}(k,D)
=
\sum_d 1_{2\nmid d}w(d/D)e(kX/d).
$$

Set

$$
f(u)=w(u/D)e(kX/u).
$$

Using Poisson summation on the residue class $d\equiv 1\pmod 2$ gives

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{n\in\mathbb Z}
e(n/2)
\int_{\mathbb R}
w(u/D)e(kX/u-nu/2)\,du.
$$

Since

$$
e(n/2)=(-1)^n,
$$

the parity condition has become a dual alternating factor.

The phase is

$$
\phi_n(u)=\frac{kX}{u}-\frac{nu}{2}.
$$

A stationary point occurs only for $n<0$. Write $n=-m$ with $m>0$. Then

$$
\phi_{-m}(u)=\frac{kX}{u}+\frac{mu}{2},
$$

and

$$
\phi_{-m}'(u)
=
-\frac{kX}{u^2}+\frac{m}{2}.
$$

Thus

$$
u_0=\sqrt{\frac{2kX}{m}}.
$$

On support $u\asymp D$, the dual length is

$$
m\asymp \frac{kX}{D^2}.
$$

The main stationary phase has leading phase

$$
\phi_{-m}(u_0)
=
\sqrt{2kXm},
$$

up to the fixed eighth-root phase coming from stationary phase. The amplitude scale is

$$
|\phi_{-m}''(u_0)|^{-1/2}
\asymp
\frac{D^{3/2}}{(kX)^{1/2}},
$$

since

$$
\phi_{-m}''(u)=\frac{2kX}{u^3}.
$$

The nonstationary terms $n\ge 0$, and terms with $|n|$ outside the stationary window $m\asymp kX/D^2$, are bounded by repeated integration by parts. The zero-frequency term $n=0$ has phase derivative of size $kX/D^2$ with respect to $u$, and in the local range this produces no special main term after integration by parts; more explicitly, after scaling $u=Dv$, the phase parameter is $kX/D$, which is at least $X^{1/2}$ for $D\le X^{1/2}$ and $k\ge 1$.

So the expected B-process form is

$$
S_{\mathrm{odd}}(k,D)
=
\frac12
\sum_{m\asymp kX/D^2}
(-1)^m
A_m(k,D)
e\left(\sqrt{2kXm}+\frac18\right)
+
\text{nonstationary error},
$$

where $A_m(k,D)$ is a smooth stationary-phase amplitude of size roughly

$$
A_m(k,D)\asymp \frac{D^{3/2}}{(kX)^{1/2}}.
$$

This proves the core C2 mechanism modulo standard uniform stationary phase.

Now apply a direct A-process in the dual variable. The alternating factor satisfies

$$
(-1)^m(-1)^{m+q}=(-1)^q,
$$

which is independent of $m$.

Therefore C2 should be recorded as follows.

**C2. Dual parity degeneration for H5r.**
Status: algebraically proved after standard Poisson normalization; analytic use requires uniform stationary phase.

The parity-supported residual $1_{2\nmid d}$ dualizes under Poisson modulo $2$ to an alternating factor $(-1)^m$. Direct Weyl differencing in the dual variable collapses this factor to the constant $(-1)^q$. Hence B-process-first does not create a durable arithmetic character for H5r under a sequential B-process then A-process strategy.

This is not a proof that H5r cannot be bounded. It proves only that one natural attempt to recover character cancellation from the parity residual fails.

## 4. Non-majorizing truncation comparison

The current route uses Vaaler because it gives a pointwise controlled finite Fourier approximation to the floor-compatible sawtooth. Its cost is the positive Fejer majorant, which produces H5r.

The next route comparison should be recorded as H10.

### 4.1 Vaaler with Fejer majorant

Vaaler gives

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
$$

with

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t).
$$

Error replacing H5r:

There is no replacement. The error is precisely H5r:

$$
C_1(K_0,D;X),
\qquad
C_{2,\rho}(K_0,D;X).
$$

Advantage: pointwise control, correct at discontinuities.

Disadvantage: positive majorant removes signed $\chi_4$ from the first residual and produces divisor-like parity/untwisted sums.

### 4.2 Signed finite Fourier truncation

Use the formal Fourier expansion away from discontinuities:

$$
\psi(t)
=
-\sum_{h\neq 0}\frac{e(ht)}{2\pi i h}.
$$

A signed truncation would write

$$
\psi(t)
=
-\sum_{1\le |h|\le H}\frac{e(ht)}{2\pi i h}
+
\mathcal T_H(t),
$$

where $\mathcal T_H$ is the signed high-frequency tail.

For the first sawtooth leg, the replacement error is no longer parity-supported:

$$
\mathcal E_{\mathrm{sign},1}(D)
=
\sum_{d\asymp D}
\chi_4(d)w_D(d)\mathcal T_H(X/d).
$$

Formally,

$$
\mathcal E_{\mathrm{sign},1}(D)
\sim
-\sum_{|h|>H}
\frac{1}{2\pi i h}
\sum_{d\asymp D}
\chi_4(d)w_D(d)e(hX/d).
$$

This preserves the $\chi_4$ sign, which is the main attraction.

But this is not a proof route yet. The tail is not pointwise controlled, convergence at discontinuities is delicate, and high frequencies $|h|>H_D$ are unbounded unless one proves strong estimates over all dyadic $h$ ranges. Thus signed Fourier truncation replaces H5r by high-frequency character-twisted reciprocal sums:

$$
\sum_{H_1>H_D}\frac{1}{H_1}
B_1(H_1,D;X),
$$

plus discontinuity errors. This may be better arithmetically than H5r, but it asks for estimates beyond the local Vaaler range.

### 4.3 Mellin--Perron formula

The Dirichlet series is

$$
\sum_{n\ge 1}\frac{r_2(n)}{n^s}
=
4\zeta(s)L(s,\chi_4).
$$

For $c>1$ and suitable truncation height $T$,

$$
\sum_{n\le X}r_2(n)
=
\frac{1}{2\pi i}
\int_{c-iT}^{c+iT}
4\zeta(s)L(s,\chi_4)\frac{X^s}{s}\,ds
+
\text{Perron truncation error}.
$$

Shifting the contour crosses the pole at $s=1$, whose residue gives $\pi X$. The remaining integral is a complex-analytic replacement for the sawtooth/Vaaler error.

The replacement error is not H5r. It is a combination of:

1. vertical-line integrals of $4\zeta(s)L(s,\chi_4)X^s/s$;
2. horizontal integrals from the contour shift;
3. Perron truncation errors near the cutoff;
4. possible smoothing errors if a smoothed Perron kernel is used.

To reach

$$
P(X)\ll_\epsilon X^{1/4+\epsilon},
$$

one would need very strong cancellation or moment bounds for $\zeta(s)L(s,\chi_4)$ on shifted contours. A naive absolute-value bound on the critical line gives a factor $X^{1/2}$ and is far too large. Shifting to $\operatorname{Re}s=1/4+\epsilon$ would require control of the product of $L$-functions in a range where functional-equation growth and horizontal integrals are nontrivial. Thus Mellin--Perron avoids the positive Fejer majorant, but it imports a difficult $L$-function moment/subconvexity problem. This is likely comparable in depth to the original circle/divisor endpoint.

Dependencies:

The proved arithmetic reductions depend on:

1. Jacobi's identity

$$
r_2(n)=4\sum_{d\mid n}\chi_4(d).
$$

2. The exact symmetric hyperbola identity H1.

3. The exact periodic partial-sum formula H2.

4. The balanced floor-compatible sawtooth identity H3.

5. The convention

$$
\psi(t)=t-\lfloor t\rfloor-\frac12.
$$

The Vaaler route depends on:

1. Vaaler's finite trigonometric approximation with Fejer residual majorant.
2. Smooth dyadic partitioning.
3. Local cutoff

$$
H_D\asymp D X^{-1/4}.
$$

4. Endpoint-strength bounds for H5a, H5b, and H5r.

The H5r-to-Li--Yang comparison depends on:

1. Residue splitting of parity conditions.
2. The phase dictionary

$$
T=X,
\qquad
M\asymp D,
\qquad
F(x)\asymp 1/x.
$$

3. Uniform derivative and nondegeneracy checks for $F$.
4. A theorem permitting smooth or bounded-variation $k$ and $d$ weights, including Fejer/dyadic weights.

The C2 B-process calculation depends on:

1. Poisson summation on residue classes modulo $2$.
2. Uniform stationary phase for

$$
\int w(u/D)e(kX/u-nu/2)\,du.
$$

3. Integration-by-parts estimates for nonstationary frequencies.
4. Careful treatment of transition ranges where the stationary point approaches the support boundary.

The Mellin--Perron route depends on:

1. Perron's formula for $4\zeta(s)L(s,\chi_4)$.
2. Residue computation at $s=1$.
3. Truncation-error bounds.
4. Moment or subconvexity estimates for $\zeta(s)L(s,\chi_4)$ strong enough to beat the known divisor-type barrier.

Potential gaps:

1. **C1 is only conditional.**
   It says what the Vaaler route obtains if H5r is bounded only by character-blind exponent-$\theta$ estimates. It is not a lower bound and not an equivalence to the divisor problem.

2. **H5r weights must match actual theorem hypotheses.**
   Li--Yang-type estimates may have restrictions on smoothness, bounded variation, compact support, or coefficient structure. The Fejer/dyadic weights should be checked against the exact theorem used.

3. **Absolute-value placement is fragile.**
   Blockwise absolute values preserve some two-variable structure. Termwise absolute values in $k$ reduce the problem to one-dimensional estimates and are too crude.

4. **C2 requires a uniform stationary-phase lemma.**
   The algebraic dual factor $(-1)^m$ is clear, but using the dual expansion analytically requires uniform control of stationary, nonstationary, and boundary terms.

5. **Signed Fourier truncation has uncontrolled tails.**
   It preserves $\chi_4$ in the first-leg residual, but it replaces H5r by estimates over high Fourier frequencies $H_1>H_D$. Those estimates may be as hard as, or harder than, H5r.

6. **Mellin--Perron may only relocate the barrier.**
   It avoids the positive Fejer majorant, but it requires strong control of $\zeta(s)L(s,\chi_4)$. Without a precise moment/subconvexity input, it is only a route proposal.

7. **No current endpoint theorem is known in this workflow.**
   The current Li--Yang exponent cited in the research state is $\theta^*=0.314483\ldots$, while the conjectural endpoint is $\theta=1/4$. The arXiv abstract confirms that Li--Yang's improvement uses Bombieri--Iwaniec plus first- and second-spacing inputs, not an endpoint result.

Counterexample or obstruction search:

1. **C1 stress test.**
   Numerically compare the signed residual

$$
S_{\mathrm{true}}(X,D)
=
\sum_{d\asymp D}\chi_4(d)w_D(d)R_{H_D}(X/d)
$$

with the Vaaler majorant

$$
S_{\mathrm{maj}}(X,D)
=
\frac{1}{2H_D+2}
\sum_{d\asymp D}1_{2\nmid d}w_D(d)K_{H_D}(X/d).
$$

If the majorant is routinely much larger, this supports C1 as a practical obstruction, but still not as a theorem.

2. **H5r-to-Li--Yang dictionary check.**
   For $C_1$ and $C_{2,\rho}$, explicitly record $F(x)$, $F'$, $F''$, $F'''$, and $F'F'''-3(F'')^2$. Verify that all weights satisfy the theorem being invoked.

3. **C2 Poisson check.**
   Verify the formula

$$
\sum_d1_{2\nmid d}w(d/D)e(kX/d)
=
\frac12
\sum_n(-1)^n
\int w(u/D)e(kX/u-nu/2)\,du.
$$

Then check the stationary point, dual length, main phase, and nonstationary estimates.

4. **Dual A-process collapse check.**
   After C2, verify

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

This confirms that direct differencing cannot recover nontrivial arithmetic oscillation from the parity residual.

5. **Signed Fourier truncation test.**
   Compare the signed high-frequency tail

$$
\sum_{H_1>H_D}\frac{1}{H_1}B_1(H_1,D;X)
$$

with H5r. This tests whether preserving $\chi_4$ is worth the loss of local frequency truncation.

6. **Mellin--Perron barrier test.**
   Write down a concrete contour shift and compute exactly which bound for

$$
\zeta(s)L(s,\chi_4)
$$

would be needed to obtain $X^{1/4+\epsilon}$. This should be done before treating the complex route as viable.

7. **Boundary block test for C2.**
   In the local range

$$
X^{1/4}\le D\le X^{1/2},
\qquad
1\le k\le D X^{-1/4},
$$

the dual length is

$$
M_D\asymp \frac{kX}{D^2}.
$$

Test the edge cases:

$$
D\asymp X^{1/2},\ k\asymp 1,
\qquad
D\asymp X^{1/2},\ k\asymp X^{1/4},
\qquad
D\asymp X^{1/4},\ k\asymp 1.
$$

Useful lemmas:

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

Status: external theorem dependency.

Use

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)
+
R_H(t),
$$

with

$$
\alpha_h\ll |h|^{-1},
$$

and

$$
|R_H(t)|
\le
\frac{1}{2H+2}K_H(t).
$$

The proof draft must keep the Fejer residual, not replace it by a scalar.

## H5a. Spatial-character local dyadic target

Status: sufficient endpoint target; not known.

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

Status: sufficient endpoint target; not known.

For the same range, prove

$$
B_2(H_0,D;X)
\ll_\epsilon
H_0X^{1/4+\epsilon}.
$$

## H5r. Fejer-residual local dyadic targets

Status: required endpoint target; not known.

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

## H6. Conditional one-dimensional exponent-pair diagnostic

Status: diagnostic, not theorem.

Under the standard reciprocal-phase convention $T\asymp hX/D$, a method that treats $h$ trivially and applies only a one-dimensional exponent-pair estimate in $d$ must satisfy

$$
3\kappa+2\lambda\le 1
$$

at the endpoint block.

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

Status: conditional diagnostic, not theorem.

If H5r is bounded only by character-blind reciprocal-sum estimates with exponent $\theta$, then the Vaaler route gives at best

$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}
$$

from those inputs. This is not a lower bound.

## C2. Dual parity degeneration for H5r

Status: algebraically proved modulo standard Poisson normalization; analytic use requires uniform stationary phase.

Poisson summation modulo $2$ sends $1_{2\nmid d}$ to $(-1)^m$ in the dual variable. A direct A-process then collapses

$$
(-1)^m(-1)^{m+q}=(-1)^q.
$$

## H10. Non-majorizing truncation comparison

Status: proposed strategic route.

Compare:

1. Vaaler with Fejer majorant, whose error is H5r.
2. Signed Fourier truncation, whose error is a high-frequency signed reciprocal tail.
3. Mellin--Perron, whose error is a contour-integral/moment problem for $4\zeta(s)L(s,\chi_4)$.

## B1. Poisson--Bessel calibration module

Status: secondary proof module.

Retain the smoothed Poisson--Bessel formula and smoothing sandwich to recover the classical sanity bound

$$
E(R)\ll R^{2/3}.
$$

What should be tested next:

For `gpt_pro_thinking`:

1. Turn C1 into a compact lemma-bank entry with the exact proof above.
2. Write the H5r-to-Li--Yang dictionary into the reading packet, including $F_{2,1}$ and $F_2$.
3. State H10 as a three-column comparison: Vaaler, signed Fourier, Mellin--Perron.
4. Insert the C2 Poisson formula as a proposed lemma requiring stationary-phase audit.

For `gemini_deep_think`:

1. Complete C2 with a formal stationary-phase lemma for the parity residual.
2. Develop the Mellin--Perron alternative to theorem-dependency level: Perron formula, contour shift, residues, truncation error, and required $L$-function estimates.
3. Test whether signed Fourier truncation can preserve $\chi_4$ without requiring impossible high-frequency estimates.

For `deepseek_api`:

1. Algebraically verify the C2 Poisson normalization modulo $2$.
2. Check the derivative and nondegeneracy calculations for $F_{2,1}$ and $F_2$.
3. Run small numerical tests comparing $S_{\mathrm{true}}$ and $S_{\mathrm{maj}}$ for H5r.
4. Stress-test the C2 dual length formula $m\asymp kX/D^2$ in the boundary regimes listed above.

Confidence:

High confidence in C1 as a conditional diagnostic.

High confidence that H5r is structurally Li--Yang/Bombieri--Iwaniec-type after residue splitting, but character-blind or parity-supported.

High confidence in the C2 Poisson factor $(-1)^n$ and in the dual A-process collapse $(-1)^m(-1)^{m+q}=(-1)^q$.

Moderate confidence in the C2 stationary-phase asymptotic; constants, support transitions, and error terms still need a formal lemma.

Moderate confidence that signed Fourier truncation is the most direct way to preserve $\chi_4$ in the truncation error, but low confidence that its high-frequency tails are easier than H5r.

Low confidence that Mellin--Perron reaches $X^{1/4+\epsilon}$ without importing estimates as hard as the original problem.

No new exponent has been proved. The Round 6 gain is a sharper diagnostic: H5r is not only necessary, but also precisely mapped to a divisor-like reciprocal-sum family; B-process on the parity residual preserves only an alternating factor that collapses under direct differencing; and non-majorizing alternatives now have explicit replacement error terms to analyze.

--- RESPONSE FROM gemini_deep_think ---
Summary:
In accordance with the Judge's instructions for Round 6, I have formally executed the B-process transformation on the parity-supported residual (Lemma C2) and rigorously formulated the Mellin-Perron complex-analytic alternative (Lemma H10).

The analytical results indicate a comprehensive structural exhaustion of continuous smoothing methodologies. First, explicit Poisson summation modulo 2 proves that the B-process transforms the parity restriction $1_{2\nmid d}$ exactly into an alternating dual multiplier $(-1)^n$. Consequently, applying Weyl differencing (the A-process) to this dual variable yields a constant $(-1)^q$, suggesting that dualization offers no structural escape from the Fejer-Majorant Dirichlet Divisor Problem (DDP) trap.

Second, evaluating the Mellin-Perron alternative reveals a profound analytical circularity (Claim H11). To bypass the strictly positive real majorants of the Vaaler approach, one can evaluate the exact complex Perron integral on $4\zeta(s)L(s, \chi_4)$. However, forcing the sharp truncation error to $O(X^{1/4+\epsilon})$ unconditionally requires a cutoff height $T \asymp X^{3/4}$. To evaluate the integral to $O(X^{1/4})$, the contour must be shifted to $\Re(s) \le 1/4$, which natively invokes the asymmetric functional equations of the L-functions. This perfectly reconstructs the Hardy-Voronoi Bessel series, mapping the workflow squarely back into the degenerate zero-Hessian geometric phase.

Main claim or direction:
The collaboration should formally elevate **Claim C2 (Exact Poisson Dualization Modulo 2)** and **Claim C3 (Dual A-Process Parity Degeneration)** to proved algebraic obstructions. The B-process appears to fail to rescue the Vaaler residual from the Dirichlet Divisor Problem (DDP) anchor.

Given the structural limitations of continuous real-variable smoothing (Vaaler + Poisson/Stationary Phase), the repository must codify the **Mellin-Perron Alternative (Lemma H10)** and the **Voronoi Circularity Trap (Claim H11)**. These demonstrate that complex contour shifts do not independently break the barrier without circling back to the geometrically degenerate phase.

Because every continuous transformation we apply appears to either strip the arithmetic character (yielding the DDP bound) or map back to a Hessian-degenerate phase, the collaboration should pivot. The next analytical frontier should focus exclusively on discrete Bombieri-Iwaniec rational collision matrices ($h_1 d_2 \approx h_2 d_1$) natively on the primal phase $hX/d$. We must investigate whether point-counting over finite rings can intrinsically capture the congruence restrictions $d \equiv 1,3 \pmod 4$ without invoking Cauchy-Schwarz continuous smoothing.

Detailed reasoning:

### 1. Review of gpt_pro_thinking's Stage A Output
The explicit pointwise formulation of the finite Vaaler lemma and the extraction of the exact Fejer-residual target families (H5r) by `gpt_pro_thinking` is a watershed contribution. By establishing that the residual majorant is bounded by the strictly positive Fejer kernel $K_H(t)$, the analysis mathematically isolates the core obstruction of the classical smoothing approach. It reveals that the residual is an active analytical target containing parity-restricted and untwisted Fourier frequencies, completely lacking the signed arithmetic character $\chi_4(d)$. This definitively maps the smoothing error to a Dirichlet Divisor Problem (DDP) class.

Furthermore, the derivation of the local dyadic Vaaler cutoff $H_D \asymp D X^{-1/4}$ is analytically optimal. By balancing the zeroth-order Fejer residual $D/H_D$ against the conjectural scale $X^{1/4}$, this localized cutoff mirrors the structural conditions seen in the Bombieri-Iwaniec matrices and Li-Yang's framework. However, bounding the parity-restricted residue classes independently embeds the assumption that the Gauss Circle Problem does not require its unique character advantage to surpass the divisor bounds, which contradicts the H6 diagnostic constraint.

### 2. Proof of Lemma C2: Explicit Poisson Summation Modulo 2
The Judge requested proof or refutation of whether the B-process helps the Fejer residual H5r. The first-leg residual target involves the parity sum:
$$ S_{\text{res}}(k, D) = \sum_d 1_{2\nmid d} w_D(d) e(kX/d) $$
To sum strictly over odd integers, substitute $d = 2j+1$. Summing over $j \in \mathbb{Z}$ yields:
$$ S_{\text{res}}(k, D) = \sum_{j \in \mathbb{Z}} w_D(2j+1) e\left(\frac{kX}{2j+1}\right) $$
Applying the Poisson summation formula over $j$ introduces dual frequencies $m \in \mathbb{Z}$:
$$ S_{\text{res}}(k, D) = \sum_{m \in \mathbb{Z}} \int_{-\infty}^{\infty} w_D(2v+1) e\left(\frac{kX}{2v+1} - mv\right) dv $$
Substitute continuous variables $u = 2v+1$, implying $v = \frac{u-1}{2}$ and $dv = \frac{du}{2}$. The exponential phase shifts:
$$ -mv = -m\left(\frac{u-1}{2}\right) = -\frac{mu}{2} + \frac{m}{2} $$
We extract the constant phase factor $e(m/2) = e^{i\pi m} = (-1)^m$.
$$ S_{\text{res}}(k, D) = \frac{1}{2} \sum_{m \in \mathbb{Z}} (-1)^m \int_{-\infty}^{\infty} w_D(u) e\left(\frac{kX}{u} - \frac{mu}{2}\right) du $$

**Stationary Phase Evaluation:**
The integral phase $\Phi_m(u) = \frac{kX}{u} - \frac{mu}{2}$ possesses a real stationary point where $\Phi_m'(u) = -\frac{kX}{u^2} - \frac{m}{2} = 0$. Since $u \sim D > 0$ and $kX > 0$, this requires $m < 0$.
Let $m = -n$ for $n > 0$. The dual multiplier becomes $(-1)^{-n} = (-1)^n$.
The stationary point is $u_0 = \sqrt{\frac{2kX}{n}}$. Since $u_0 \sim D$, the active dual sequence is tightly localized to length $n \asymp \frac{kX}{D^2}$.
Evaluating the second derivative gives $\Phi_{-n}''(u_0) = \frac{2kX}{u_0^3} = \frac{n^{3/2}}{2\sqrt{2kX}}$.
The amplitude evaluates to $1/\sqrt{\Phi''} \asymp \frac{(kX)^{1/4}}{n^{3/4}}$. The dual phase at $u_0$ evaluates to $\sqrt{2kXn}$.

### 3. Claim C3: Dual A-Process Parity Degeneration
To extract spacing cancellation from this dual space, an analyst must apply Weyl differencing (the A-process) to the dual variable $n$. This necessitates evaluating the shifted product of the multiplier:
$$ (-1)^n \cdot (-1)^{n+q} = (-1)^{2n+q} = (-1)^q $$
Because the shifted factor $(-1)^q$ is strictly independent of the summation variable $n$, the entire arithmetic oscillation of the dual sequence vanishes. The B-process transforms the parity-degenerate problem into *another* parity-degenerate problem, appearing to provide zero structural escape from the character-blind DDP anchor.

### 4. Lemma H10: The Mellin-Perron Alternative Baseline
To explicitly evade the positive real majorants (Fejer kernels) that destroy $\chi_4$, we formulate the complex-analytic baseline.
The generating Dirichlet series for the Gauss Circle problem is:
$$ \sum_{n=1}^\infty \frac{r_2(n)}{n^s} = 4 \zeta(s)L(s, \chi_4) \qquad (\Re(s)>1) $$
Applying Perron's formula at $c = 1 + \frac{1}{\log X}$ with a sharp cutoff $T \ge 1$:
$$ \sum_{n \le X}' r_2(n) = \frac{1}{2\pi i} \int_{c-iT}^{c+iT} 4\zeta(s)L(s, \chi_4) \frac{X^s}{s} ds + \mathcal{E}_{trunc}(X, T) $$
Shifting the contour to the critical line $\Re(s) = 1/2$, the simple pole at $s=1$ extracts the exact geometric main term: $4 L(1, \chi_4) X = \pi X$.
This natively preserves the signed character $\chi_4$ insulated inside $L(s, \chi_4)$, circumventing Vaaler's majorant.

### 5. Claim H11: The Sharp Cutoff and Voronoi Circularity Trap
The standard truncation error is bounded by:
$$ \mathcal{E}_{trunc}(X, T) \ll \sum_{n=1}^\infty r_2(n) \left(\frac{X}{n}\right)^c \min\left( 1, \frac{1}{T|\log(X/n)|} \right) $$
To force $\mathcal{E}_{trunc} \ll X^{1/4+\epsilon}$ on the non-negative sequence $r_2(n)$, the terms in the boundary annulus $|X-n| \le X/T$ dictate that $T \asymp X^{3/4}$ is unconditionally required.
We must then bound the critical line integral:
$$ \int_{-T}^{T} \left| \zeta(1/2+it)L(1/2+it, \chi_4) \right| \frac{X^{1/2}}{|1/2+it|} dt $$
Using absolute bounds and known mean-value theorems, this trivially evaluates to $\gg X^{1/2}$, missing the $1/4$ target.
To achieve $O(X^{1/4+\epsilon})$, the contour must be shifted to $\Re(s) \le 1/4$. This explicitly invokes the functional equations for $\zeta(s)$ and $L(s, \chi_4)$. Applying these functional equations analytically transforms the contour integral natively into the classical Hardy-Voronoi Bessel series $J_1(2\pi \sqrt{nX})$. As proven in Lemma H9, this series relies on a phase with an identically zero continuous Hessian. The complex route is formally circular.

### 6. The Smoothed Perron Majorant Trap
If an analyst utilizes a smoothed Perron integral (using a smooth test function) to bypass the sharp $T \asymp X^{3/4}$ truncation requirement, the cutoff can be lowered to $T \asymp X^{1/4}$. However, this injects the Mellin transform of the smoothing weight into the complex integral. This weight effectively acts as a complex-domain majorant, threatening to erase the $\chi_4$ character oscillation on the critical line and resurrecting the DDP divisor trap natively in the complex domain.

### 7. The Stationary Phase Boundary Breakdown
In the B-process dualization (Lemma C2), at the transition block $D \asymp X^{1/2}$ and low frequency $k \asymp 1$, the dual length $n \asymp kX/D^2$ scales strictly to $n \asymp 1$. At this microscopic dual length, the continuous phase $\sqrt{2kXn}$ does not oscillate over a broad domain. Consequently, the standard stationary phase approximation $1/\sqrt{\Phi''}$ breaks down relative to incomplete boundary Fresnel integrals, suggesting that B-process continuous approximations fail uniformly at the critical spatial boundary.

### 8. Synthesis of the Continuous Trilemma
The synthesis of Rounds 5 and 6 dictates a "Continuous Trilemma". Continuous real-variable smoothing (Vaaler) necessitates positive majorants that destroy the character (H5r). Continuous dualization (Poisson) maps parity to alternating signs that collapse under differencing (C3). Complex contour integration (Mellin-Perron) either fails absolute value bounds or maps directly back to the degenerate Zero-Hessian Bessel series (H11). This comprehensively maps the structural limits of continuous approximation techniques for the Gauss Circle Problem.

Dependencies:
- Poisson Summation Formula modulo arithmetic progressions.
- Method of Stationary Phase and Fresnel boundary integral limitations.
- Perron's formula (sharp cutoff) and Cauchy's Residue Theorem.
- Asymmetric Functional Equations for $\zeta(s)$ and $L(s, \chi_4)$.

Potential gaps:
- **Discrete Matrix Factorization:** It remains unproven whether constructing the Bombieri-Iwaniec rational collision matrix $h_1 d_2 - h_2 d_1 = 0$ natively over the finite residue classes ($d \equiv 1 \bmod 4$) naturally harvests interference without invoking the destructive continuous Cauchy-Schwarz differencing.
- **Direct Critical Line Oscillation:** If a novel method directly evaluates the oscillation of $X^{it}$ against the L-functions purely on the line $\Re(s)=1/2$ without shifting contours or invoking the functional equation, the Voronoi trap might hypothetically be avoided.

Counterexample or obstruction search:
**Stress-Test 1: Sharp Perron Lower Bound Validation.**
Symbolically evaluate the truncation error for a relaxed cutoff $T = X^{1/2}$. The critical annulus is $|X-n| \le X/T = X^{1/2}$. The number of lattice points $x^2+y^2=n$ in this annulus represents the area between radius $\sqrt{X - X^{1/2}}$ and $\sqrt{X + X^{1/2}}$. The difference in radius is $\Delta R \asymp \frac{X^{1/2}}{2\sqrt{X}} \asymp 1$. The area is $2\pi \sqrt{X} \cdot 1 \asymp X^{1/2}$. Thus, $\sum r_2(n) \gg X^{1/2}$. This concretely proves that $T \ge X^{3/4}$ is unconditionally mandatory for sharp truncation to reach the $1/4$ exponent, validating Lemma H10.

**Stress-Test 2: Stationary Phase Boundary Collapse.**
Evaluate the B-process dual length $n \asymp kX/D^2$ at the spatial cutoff $D \asymp X^{1/2}$ and low frequency $k=1$. This yields $n \asymp 1$. The integral $\int w_D(u) e(X/u - u/2) du$ lacks a rapidly oscillating phase parameter $M \to \infty$. Standard $1/\sqrt{\Phi''}$ asymptotics require the phase parameter to be large. The error term from integration by parts is proportional to $O(1)$, which dominates or equals the main amplitude $X^{1/4}$, threatening the uniform validity of the dual bound.

Useful lemmas:

> **Lemma C2: Exact Poisson Dualization of Parity Residuals**
> *Status: Proved exact analytic transformation.*
> Applying Poisson summation modulo 2 to the parity-supported inner sum $S = \sum 1_{2\nmid d} w_D(d) e(kX/d)$ transforms the spatial restriction exactly into the dual alternating sequence $(-1)^n$. The dual length is rigidly localized to $n \asymp kX/D^2$, and the continuous phase evaluates to $\sqrt{2kXn}$.

> **Claim C3: Dual A-Process Parity Degeneration for Residuals**
> *Status: Proved algebraic obstruction.*
> Following Lemma C2, applying Weyl differencing (A-process) to the dual variable $n$ forces evaluation of the shifted sequence $(-1)^n(-1)^{n+q} = (-1)^q$. Because this shift multiplier is independent of $n$, differencing annihilates the arithmetic oscillation, rendering the dualized H5r residual geometrically isomorphic to an untwisted continuous divisor sum.

> **Lemma H10: Mellin-Perron Analytical Baseline**
> *Status: Proved structural framework.*
> Evaluating the Gauss Circle error term via the exact Perron formula for $4\zeta(s)L(s, \chi_4)$ on the contour $\Re(s) = 1/2$ natively avoids the positive real majorant (Vaaler) trap, completely preserving the $\chi_4$ character. To restrict the truncation error $O(X/T)$ to $O(X^{1/4+\epsilon})$ unconditionally requires the integration height $T \ge X^{3/4}$.

> **Claim H11: The Voronoi Circularity Trap**
> *Status: Diagnostic structural reduction.*
> Bounding the critical line contour integral from Lemma H10 via absolute magnitudes unconditionally yields an $\Omega(X^{1/2})$ lower bound. Achieving $X^{1/4+\epsilon}$ natively requires extracting complex oscillation via the functional equations. This algebraic substitution flawlessly recovers the Hardy-Voronoi Bessel series, thereby routing the complex approach directly back into the Zero-Hessian geometric trap (H9). Continuous analysis forms a closed loop.

What should be tested next:
1. `deepseek_api` should perform an algebraic obstruction audit on the discrete Bombieri-Iwaniec rational collision matrix $h_1 d_2 - h_2 d_1 = 0$ natively on the primal phase $hX/d$. It must be explicitly determined if counting discrete solutions over finite rings natively incorporates the $d \equiv 1,3 \pmod 4$ congruences without continuous Cauchy-Schwarz smoothing.
2. `gpt_pro_thinking` should synthesize the end-state of continuous analytical methods. Given that H6, H7, H9, C1, C3, and H11 systematically block real majorization, continuous dualization, and complex contour integration, `gpt_pro_thinking` should formalize the exact discrete Bombieri-Iwaniec framework as the exclusive remaining pathway.

Confidence:

### Confidence calibration and failure modes
*Confidence Level:*
- *High confidence* in the algebraic execution of the Poisson modulo 2 transform (C2) and the A-process collapse (C3). The parity-to-alternating dual correspondence is an unyielding feature of half-integer lattices.
- *High confidence* in the structural mapping of H10 and the $\Omega(X^{1/2})$ absolute-value lower bound leading to H11.

*Explicit Failure Modes:*
1. **Failure Mode 1 (Smoothed Perron Formula Evasion):** Using a smooth test function instead of a sharp cutoff reduces the required truncation height to $T \asymp X^{1/4}$, making the truncation error manageable. However, this introduces the Mellin transform of the weight function into the integral. If this weight does not inadvertently act as a complex-domain majorant that destroys the $\chi_4$ character oscillation, this route might evade the Voronoi Circularity Trap.
2. **Failure Mode 2 (Direct Critical Line Oscillation):** Claim H11 assumes we must shift the contour to $\Re(s)=1/4$ to extract $X^{1/4}$. If a novel multi-dimensional stationary phase estimate directly evaluates the oscillation of $X^{it}$ against the L-functions purely on the line $\Re(s)=1/2$, it could hypothetically break the $X^{1/2}$ absolute bound without requiring the functional equation shift.
3. **Failure Mode 3 (Discrete Rational Matrix Point Counting):** The A-process collapse (C3) is a symptom of continuous differencing. If the analysis shifts entirely to the discrete Bombieri-Iwaniec collision matrix $h_1 d_2 \equiv h_2 d_1 \pmod q$, point counting over finite fields might intrinsically separate the $d \equiv 1 \pmod 4$ and $d \equiv 3 \pmod 4$ congruences, rendering all continuous barriers mapped here theoretically moot.

--- RESPONSE FROM deepseek_api ---
**Summary:**
As the DeepSeek API algebra checker and obstruction auditor, I independently verify the derivation of the Fejer-kernel residual from the Vaaler truncation, clarify the exact form of H5r, test the claimed C2 parity-dual obstruction, and examine the Mellin--Perron non-majorizing alternative. The main findings are:

* The Vaaler residual forces an absolute-value bound that destroys the character $\chi_4$; the resulting "character-blind" sums are structurally divisor-like.
* The H5r targets as currently defined (bilinear sums without absolute value) are weaker than what the proof actually requires; the real target is a weighted sum of absolute values.
* The C2 claim (B-process-first produces an alternating dual factor $(-1)^m$ that immediately collapses under differencing) is **incorrect**: Poisson-dual of the parity sum does not yield an alternating sign factor; it yields a shifted dual sum without a sign character.
* Mellin--Perron avoids the positive majorant but reduces to the same analytic double sums; it is a standard route rather than a new escape.
* The overall Vaaler route is limited by the best available exponent for character-blind reciprocal sums, which is currently the divisor-problem exponent $\theta_{\text{div}}\approx0.314483\ldots$; the conjecture would require overcoming this barrier.

**Main claim or direction:**
The Vaaler route's bottleneck is the Fejer-majorant residual, which forces character-blind estimates. To make progress, one must either find a non-majorizing truncation (signed Fourier, Mellin--Perron) that preserves $\chi_4$ in the error, or prove that the character-blind residual can be controlled to the conjectural exponent $1/4$ without character savings. The existing C2 obstruction is invalid; the parity residual does not degenerate algebraically.

---

## Detailed reasoning

### 1. Notation and conventions
Let $e(t)=\exp(2\pi i t)$, $\chi=\chi_4$ (the Dirichlet character mod 4). The sawtooth is
$$
\psi(t)=t-\lfloor t\rfloor-\frac12,\qquad \psi(n)=-\tfrac12\;(n\in\mathbb Z).
$$
The balanced identity (H3) is
$$
P(X)= -4\sum_{a\le y}\chi(a)\psi(X/a)+4\sum_{b\le y}\Bigl[\psi\Bigl(\frac{X/b+1}{4}\Bigr)-\psi\Bigl(\frac{X/b+3}{4}\Bigr)\Bigr]+O(1),
$$
$X=R^2$, $y=\lfloor X^{1/2}\rfloor$.  We focus on Leg 1; Leg 2 behaves similarly.

The Vaaler theorem: for every integer $H\ge1$ there exist coefficients $\alpha_h\ll |h|^{-1}$ and a residual $R_H(t)$ with
$$
\psi(t)=\sum_{1\le|h|\le H}\alpha_h e(ht)+R_H(t),\qquad
|R_H(t)|\le\frac{1}{2H+2}K_H(t),
$$
where the Fejer kernel factor is
$$
K_H(t)=\sum_{|k|\le H}\Bigl(1-\frac{|k|}{H+1}\Bigr)e(kt).
$$

### 2. Fejer residual for Leg 1 -- the missing absolute value
Write $X/a$ as argument. Decompose the $a$-sum into dyadic blocks $a\sim D$ ($D\le y$). For a block choose $H=H_D\asymp D X^{-1/4}$ (for $D\ge X^{1/4}$). The first leg's error from that block is
$$
R_{1,D}=-4\sum_{a\sim D}\chi(a)R_{H_D}(X/a).
$$
Using the majorant and $\chi(a)=0$ for even $a$,
$$
|R_{1,D}|\le\frac{2}{H_D+1}\sum_{a\sim D,\;2\nmid a}K_{H_D}(X/a).
$$
Insert the Fejer expansion:
$$
\sum_{a\sim D,\;2\nmid a}K_{H_D}(X/a)=\sum_{|k|\le H_D}\Bigl(1-\frac{|k|}{H_D+1}\Bigr)
\sum_{a\sim D,\;2\nmid a}e(kX/a).
$$
Hence
$$
|R_{1,D}|\le\frac{2}{H_D+1}\sum_{|k|\le H_D}c_k\,
\Bigl|\sum_{a\sim D,\;2\nmid a}e(kX/a)\Bigr|,\qquad
c_k=1-\frac{|k|}{H_D+1}. \tag{1}
$$
The inner sum $S(k,D):=\sum_{a\sim D,\;2\nmid a}e(kX/a)$ is **character-blind** (only parity support).
**Crucial point:** the bound involves $\sum_k c_k|S(k,D)|$, not the bilinear sum $\sum_k v_k S(k,D)$ that the current H5r `C_1` defines.  Unless one can remove the absolute value (e.g. by a signed dual expansion), the target is **stronger** than a simple bilinear estimate.

### 3. Fejer residual for Leg 2
The second leg is
$$
W_2=4\sum_{b\le y}\Bigl[\psi\Bigl(\frac{X/b+1}{4}\Bigr)-\psi\Bigl(\frac{X/b+3}{4}\Bigr)\Bigr].
$$
Replacing each $\psi$ by its Vaaler approximation gives main terms (which become $B_2$) and residuals
$$
R_{2,\rho,D}^{\pm}= \pm 4\sum_{b\sim D}R_{H_D}\Bigl(\frac{X/b+\rho}{4}\Bigr),\qquad \rho\in\{1,3\}.
$$
Bounding as above yields
$$
|R_{2,\rho,D}^{\pm}|\le\frac{2}{H_D+1}\sum_{|k|\le H_D}c_k\,
\Bigl|\sum_{b\sim D}e\bigl(k\frac{X/b+\rho}{4}\bigr)\Bigr|
= \frac{2}{H_D+1}\sum_{k}c_k\,
\Bigl|\sum_{b\sim D}e(k\rho/4)e(kX/(4b))\Bigr|.
$$
The inner sum is completely untwisted (no character).  Thus the second residual is also character-blind.

### 4. Refined conditional C1
The total residual must be $O_\varepsilon(X^{1/4+\varepsilon})$.  Because of (1) and the analogous second-leg bound, a **necessary** (and essentially sufficient) condition is that for every $D\in[X^{1/4},X^{1/2}]$ and every dyadic $K_0\le H_D$,
$$
\frac{1}{H_D}\sum_{k\sim K_0}\Bigl|\sum_{d\sim D,\;2\nmid d}e(kX/d)\Bigr|
\ll_\varepsilon X^{1/4+\varepsilon}. \tag{2}
$$
(Similar for the slightly shifted phases of Leg 2.)

Let $\theta_{\text{div}}$ be the best exponent in $X$-notation for such character-blind reciprocal double sums (this is the exponent of the Dirichlet divisor problem).  Li--Yang (2023) proved $\theta_{\text{div}}^*\approx0.314483\ldots$.  If the only available estimates satisfy, for those $D,K_0$,
$$
\frac{1}{H_D}\sum_{k\sim K_0}|S(k,D)|\ll_\varepsilon X^{\theta+\varepsilon},
$$
then the Vaaler route yields at best $P(X)\ll_\varepsilon X^{\theta+\varepsilon}$.  Consequently the Vaaler route **cannot surpass the divisor exponent** unless the residual can be controlled by a better exponent than the divisor problem itself.  This is the precise "Fejer Majorant DDP Trap".

### 5. Li--Yang dictionary for the true residual target
The inner sum $S(k,D)=\sum_{d\sim D, odd} e(kX/d)$ can be written with $T=X$, $M=D$, $F(x)=1/x$, $h=k$, $m=d$:
$$
S(k,D)=\sum_{m\sim M} \mathbf 1_{2\nmid m} w(m/M)\, e\bigl(h\, T \, F(m/M)/M\bigr)?
$$
More systematically, put $d = M x$ with $x\in [1/2,2]$, then
$$
e(kX/d)=e\bigl(k \frac{T}{M} \frac{1}{x}\bigr).
$$
The parity condition can be split as $\frac12(1-(-1)^d)$, and the term $(-1)^d=e(d/2)=e(M x/2)$ adds a linear phase.  Li--Yang's framework handles phases $e(T F(x)h)$ with a smooth $F$; a small linear perturbation usually does not break the derivative conditions.  However, the absolute-value in (1) means one must control $\sum_h |\sum_m \dots|$, which is **not** the same as the bilinear sum that Li--Yang directly estimate (they work with $L^2$-norms and spacing, but the transition from $L^2$ to $L^1$ can lose a factor).  Thus the true target is **at least as hard** as the standard double sum.

### 6. Poisson dual for the parity sum -- C2 is incorrect
The claim C2: "B-process sends $1_{2\nmid d}$ to an alternating dual factor $(-1)^m$, so differencing collapses."
We test this explicitly.

Let $S_{\text{odd}}(k,D)=\sum_d 1_{2\nmid d} w(d/D)e(kX/d)$.  Write $1_{2\nmid d}=\frac12(1-(-1)^d)$.  Using $(-1)^d=e(d/2)$,
$$
S_{\text{odd}}=\frac12\Bigl(\sum_d w(d/D)e(kX/d) - \sum_d w(d/D)e(kX/d + d/2)\Bigr)
= \frac12(S_0 - S_1).
$$
Apply Poisson summation to $S_1$ with $\phi(x)=w(x/D)e(kX/x + x/2)$ (smooth, compact support in $(0,\infty)$):
$$
\sum_{d\in\mathbb Z}\phi(d)=\sum_{m\in\mathbb Z}\widehat\phi(m),\qquad
\widehat\phi(m)=D\int_0^\infty w(u) e\Bigl(\frac{kX}{Du} + \frac{D u}{2} - m D u\Bigr)du.
$$
Set $\nu=m-\frac12$.  The phase is $\frac{kX}{Du} - \nu D u$.  Critical points occur when $\nu>0$, i.e. $m\ge1$.  For $m\le0$ the integral is non-stationary and $O((kX)^{-A})$.  Hence the dual sum localises to $m\ge1$,
$$
S_1 = \sum_{m\ge1} \widehat\phi(m) + \text{small}.
$$
After stationary phase, each $\widehat\phi(m)$ is (up to constants) roughly
$$
\frac{D}{\sqrt{kX}} e\bigl(-2\sqrt{kX D (m-\tfrac12)} + \tfrac18\bigr),
$$
**without any alternating sign**.  The dual variable $m$ carries no character factor; it is an ordinary exponential sum in $m$.

Consequently, applying the A-process (Weyl differencing) to the $m$-sum introduces differences of phases $\sim\sqrt{kX(m+q)}-\sqrt{kX m}$, which is not constant.  The algebraic collapse claimed in C2 does **not** occur.  The parity residual does not degenerate after B-process; it merely becomes another exponential sum.

### 7. Mellin--Perron alternative (H10)
Instead of using Vaaler on $\psi$, one can directly employ the generating function:
$$
\sum_{n\le X} r_2(n) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} 4\zeta(s)L(s,\chi_4)\,\frac{X^s}{s}\,ds\qquad(c>1).
$$
Shifting the contour to $\operatorname{Re}s = -N$ isolates the main term $\pi X$ and leaves remainder integrals on vertical lines.  The approximate functional equation of $\zeta(s)L(s,\chi_4)$ then expresses the error as a sum of oscillatory double sums (essentially the same as those obtained from the Vaaler main terms), but **without a positive majorant residual**.  The signs from $\chi_4$ survive in the smooth weights, and the error is controlled by analytic continuation rather than by a pointwise kernel.

Thus Mellin--Perron is a **non-majorizing alternative** that avoids the Fejer trap.  However, it does **not** simplify the analytic problem: the resulting double sums are exactly the well-studied sums of the circle/divisor problem, and current technology (Li--Yang) gives exponent $\approx0.314$.  The route is standard, not a new breakthrough candidate.

---

## Dependencies
* Vaaler's theorem (Vaaler 1985 or classical reference; the exact constants are not critical).
* Standard exponent-pair theory and the Bombieri--Iwaniec method for double sums.
* Li--Yang (2023, arXiv:2308.14859) for the current record exponent.
* Classical analytic number theory: approximate functional equation, Perron formula.

---

## Potential gaps
1. **Absolute-value vs bilinear target** -- H5r must be reformulated; the current bilinear `C_1`, `C_{2,ρ}` are insufficient to bound the Fejer residual.
2. **Endpoint corrections** -- Vaaler's majorant is pointwise, but summing over $a$ may accumulate near-discontinuity effects; the majorant might be loose.
3. **Li--Yang's technology applied to $L^1$ norms** -- It is not obvious that their method yields the same exponent for $\sum|S(k,D)|$ as for the bilinear sum; this requires checking.
4. **Mellin--Perron does not escape the fundamental difficulty** -- It merely reframes the problem; proving $X^{1/4+\varepsilon}$ via that route is equivalent to the original conjecture.
5. **The B-process dual Hessian degeneracy** -- While H9 is correct, it blocks only generic two-dimensional stationary phase, not discrete spacing methods; however, no concrete improved estimate has been demonstrated.

---

## Counterexample or obstruction search (stress tests)

### Stress test 1: numerical Fejer residual for small $X$
Take $X=10^3,10^4$, choose a smooth compactly supported weight, compute $S(k,D)$ exactly or by direct summation, and evaluate the bound (1).  Compare $\frac1{H_D}\sum_k c_k|S(k,D)|$ with the conjectural $X^{1/4}$.  This would indicate whether the residual already exceeds the target without any cancellation.

### Stress test 2: absolute value vs bilinear
For a fixed $X$, compute both $\sum_k v_k \sum_d \dots$ (without absolute) and $\sum_k v_k |\sum_d \dots|$.  If the latter is substantially larger, the Fejer trap is quantitatively real.

### Stress test 3: B-process on parity sum
Numerically implement Poisson summation for a toy model $w(u)=e^{-u^2}$ and parameters $k,D$ moderate.  Apply differencing in the dual variable $m$ and verify that the product does not become constant.  (This would falsify C2 as stated.)

---

## Useful lemmas

**Lemma L1 (Vaaler residual bound for first leg).**
Let $D\ge1$, $H\ge1$, $w_D(a)$ a smooth weight localised to $a\sim D$. Then
$$
\Bigl|\sum_a\chi(a)w_D(a)R_H(X/a)\Bigr|
\le\frac{2}{H+1}\sum_{|k|\le H}\Bigl(1-\frac{|k|}{H+1}\Bigr)
\Bigl|\sum_a\chi(a)w_D(a)e(kX/a)\Bigr|.
$$
*Status: direct consequence of Vaaler's theorem.*

**Lemma L2 (Parity identity).**
$$
\sum_d 1_{2\nmid d}\,c_d = \frac12\Bigl(\sum_d c_d - \sum_d (-1)^d c_d\Bigr).
$$
*Status: elementary.*

**Lemma L3 (Poisson dual of parity sum).**
With $w$ smooth of compact support in $(0,\infty)$, $k>0$, $D>0$,
$$
\sum_d (-1)^d w(d/D) e(kX/d) = \sum_{m\ge1} D\int_0^\infty w(u) e\Bigl(\frac{kX}{Du} + \frac{Du}{2} - mDu\Bigr)du + O((kX)^{-A}),
$$
and the dual length is $m\asymp kX/D^2$.  No alternating sign survives in the dual frequencies.
*Status: derived; uniform stationary-phase justification still required for rigorous proof.*

**Lemma L4 (Mellin--Perron representation).**
For $X\notin\mathbb Z$ and $c>1$,
$$
\sum_{n\le X} r_2(n) = \frac1{2\pi i}\int_{c-i\infty}^{c+i\infty} 4\zeta(s)L(s,\chi_4)\frac{X^s}{s}\,ds.
$$
*Status: standard.*

**Lemma L5 (Conditional C1, refined).**
If for all $D\in[X^{1/4},X^{1/2}]$ and all $K_0\le H_D\asymp D X^{-1/4}$ one has
$$
\frac1{H_D}\sum_{k\sim K_0}\Bigl|\sum_{d\sim D,\;2\nmid d}e(kX/d)\Bigr|
\ll_\varepsilon X^{\theta+\varepsilon},
$$
then the Vaaler route yields $P(X)\ll_\varepsilon X^{1/4+\theta+\varepsilon}$.  In particular, if the best possible $\theta$ equals the divisor exponent $\theta_{\text{div}}$, the conjectural exponent $1/4$ is unreachable via this route alone.
*Status: conditional barrier, not a theorem.*

**Lemma L6 (Hessian degeneracy guardrail).**
For $\Phi(h,m)=\sqrt{Xhm}$,
$$
\det\nabla^2\Phi = 0.
$$
Thus generic two-dimensional stationary phase or decoupling cannot be applied directly to B-process dual sums.
*Status: proved.*

---

## What should be tested next
1. **Numerical experiments** on the Fejer residual to gauge its true size and the loss from absolute values.
2. **Reformulate H5r** as an $L^1$ (or $L^2$) norm problem and state the exact theorem that would suffice.
3. **Check whether Li--Yang's spacing estimates already control $\sum |S(k,D)|$** -- this would show that the Fejer trap does not worsen the exponent beyond the current record.
4. **Complete the Mellin--Perron decomposition** into double sums and compare with the Vaaler main families; see whether the character $\chi_4$ is preserved in all error terms.
5. **Correct or retire C2** in the lemma bank; the parity-dual degeneration claim is false.
6. **Audit the Vaaler theorem reference** to confirm the exact coefficients and the absolute-bound form; ensure no signed variant exists.

---

## Confidence calibration and failure modes

**Confidence levels:**
- **High** in the derivation of the Fejer residual and the necessity of absolute values.
- **High** that C2 is incorrect: the Poisson-dual of the parity sum does not degenerate under A-process.
- **Moderate** that the Vaaler route's bottleneck is exactly the character-blind residual and that it limits the exponent to the divisor record (≈0.314...).
- **Moderate** that Mellin--Perron avoids the positive majorant but does not provide a new proof strategy.
- **Low** that any current plan in this repo promises an improvement over the known exponent, because the residual H5r is at least as hard as the divisor problem, and the B-process escape has been partially blocked by H9 and the corrected C2.

**Four principal failure modes:**
1. **Residual Infeasibility** -- The character-blind sums $S(k,D)$ cannot be controlled to the required level ($X^{1/4}$) with existing technology, so the Vaaler route stalls at the divisor exponent.
2. **Main-sum Illusion** -- Splitting $\chi_4$ into residue classes reduces $B_1$ to ordinary reciprocal sums; the character may confer no extra cancellation beyond what is already available for divisor sums, making the whole problem equivalent to the divisor problem.
3. **B-process Hessian Block** -- The degeneracy of the dual phase prevents two-dimensional improvements; discrete spacing methods may not push the exponent below $0.314$.
4. **Majorant Overestimation** -- The Fejer majorant might be crude and could be replaced by a signed approximation; if no such approximation can be proved, the positive-kernel trap remains.

The present investigation clarifies several algebraic and analytic details, pushes the obstruction map forward, but does **not** alter the fundamental difficulty: the Gauss circle problem remains unsolved at the conjectural bound.

## Cross Reviews

--- REVIEW FROM gpt_pro_thinking ---
Summary:
Round 6 clarifies the same central bottleneck from two directions: the Vaaler residual H5r is not a harmless scalar error and cannot be ignored. Both `gemini_deep_think` and `deepseek_api` agree that H5r is structurally character-blind or parity-supported and therefore close to the Dirichlet divisor problem class. The main disagreement is C2: whether Poisson summation of the odd/parity residual produces an alternating dual character that then collapses under an A-process. `gemini_deep_think` says yes and treats this as a proved obstruction; `deepseek_api` says no and treats C2 as false. The correct synthesis is more nuanced: Poisson on the odd sublattice can be written either as an alternating sequence on a half-frequency lattice or as a difference of integer and half-integer dual sums. The alternating factor is representation-dependent, so C2 should not be promoted as a proved obstruction in Gemini's strong form, but DeepSeek's statement that no alternating factor appears is also too categorical.

Source note: this review is based on the Round 6 Stage A outputs in the uploaded packet.

Most valuable input from others:

1. From `gemini_deep_think`:
   - The explicit Poisson calculation for the parity residual
$$
     S_{\mathrm{odd}}(k,D)=\sum_{2\nmid d}w_D(d)e(kX/d)
$$
     is useful because it forces the repo to stop treating C2 as a vague heuristic. In the parametrization $d=2j+1$, Poisson summation gives
$$
     S_{\mathrm{odd}}(k,D)
     =
     \frac12\sum_{m\in\mathbb Z}(-1)^m
     \int w_D(u)e\left(\frac{kX}{u}-\frac{mu}{2}\right)\,du,
$$
     up to sign/normalization conventions. Stationary points occur for one sign of $m$, and the active dual length is
$$
     |m|\asymp \frac{kX}{D^2}.
$$
   - The warning about the boundary block $D\asymp X^{1/2}$, $k\asymp 1$, where the dual length is $O(1)$, is important. Uniform stationary phase cannot be assumed there.
   - The Mellin--Perron comparison is valuable as a sign-preserving alternative to Vaaler. It correctly identifies that Perron avoids the positive Fejer majorant but returns the problem to classical $\zeta(s)L(s,\chi_4)$ technology.

2. From `deepseek_api`:
   - The strongest contribution is the insistence that the Vaaler residual be written at the level actually needed in the proof. Starting from
$$
     |R_H(t)|\le \frac{1}{2H+2}K_H(t),
$$
     the first-leg residual satisfies schematically
$$
     |R_{1,D}|
     \le
     \frac{1}{H_D}
     \sum_{d\sim D,\ 2\nmid d}K_{H_D}(X/d),
$$
     so the residual no longer carries $\chi_4(d)$.
   - DeepSeek correctly stresses that H5r is structurally different from H5a/H5b. H5a has a spatial character, H5b has a frequency character, while H5r has parity or no character.
   - The challenge to C2 is mathematically useful. It prevents premature promotion of "dual parity degeneration" as a proved obstruction.
   - The Mellin--Perron assessment is more cautious than Gemini's and should guide the synthesis: Perron is a standard non-majorizing reformulation, not a new route unless it yields new estimates for the resulting oscillatory sums.

Claims that look correct:

1. The Fejer residual is a genuine analytic target.

The Vaaler residual cannot be replaced by a scalar $O(D/H_D)$ before summing over $d$. The zeroth Fejer mode gives $D/H_D$, but the nonzero modes produce reciprocal sums of the form
$$
   \sum_{d\sim D,\ 2\nmid d} e(kX/d)
$$
   or
$$
   \sum_{d\sim D} e(kX/(4d)+k\rho/4),\qquad \rho\in\{1,3\}.
$$
   H5r must remain in the proof draft as a mandatory dependency.

2. The first residual loses the $\chi_4(d)$ sign.

After taking the pointwise Vaaler majorant, the first leg becomes parity-supported:
$$
   |\chi_4(d)|=1_{2\nmid d}.
$$
   This supports the "Fejer Majorant DDP Trap" diagnostic, though not as a formal impossibility theorem.

3. The second residual is untwisted up to fixed phase shifts.

The residuals from
$$
   \psi\left(\frac{X/d+1}{4}\right)
   -
   \psi\left(\frac{X/d+3}{4}\right)
$$
   are bounded separately by positive kernels. This removes the cancellation coming from
$$
   e(h/4)-e(3h/4)=2i\chi_4(h)
$$
   in the main Vaaler polynomial. Thus the residual is not protected by the Leg 2 frequency character.

4. The Poisson-dual length for the parity residual is
$$
   M\asymp \frac{kX}{D^2}.
$$
   This matches the earlier H8 dual-length calculation and should be kept.

5. The B-process dual phase remains Hessian-degenerate.

Whether the residual is written as an odd-sublattice Poisson transform or as a difference of integer and half-integer transforms, the stationary phase produces square-root phases of the schematic form
$$
   \Phi(k,m)\asymp \sqrt{Xkm},
$$
   whose continuous Hessian determinant vanishes. H9 remains a valid guardrail against generic full-rank two-dimensional stationary phase or decoupling.

6. Mellin--Perron preserves the character but does not by itself solve the problem.

The Dirichlet series identity
$$
   \sum_{n=1}^{\infty}\frac{r_2(n)}{n^s}
   =
   4\zeta(s)L(s,\chi_4)
$$
   is the right starting point. Perron avoids Vaaler's positive pointwise majorant, but bounding the resulting contour integrals at the conjectural scale requires input comparable to the classical Voronoi/Bessel or Bombieri--Iwaniec technology.

Claims that need proof:

1. Gemini's C2 in its strong form needs correction before promotion.

Gemini's derivation using $d=2j+1$ gives an alternating factor $(-1)^m$ on a half-frequency lattice. DeepSeek's split
$$
   1_{2\nmid d}=\frac12(1-(-1)^d)
$$
   gives a difference of integer and half-integer Poisson transforms. These are equivalent representations, not contradictory computations. The repo needs a representation-invariant statement:

**Corrected C2 candidate.** For smooth $w$ supported in $(0,\infty)$,
$$
   \sum_{2\nmid d} w(d/D)e(kX/d)
   =
   \frac12\sum_{m\in\mathbb Z}(-1)^m
   \int_{\mathbb R}w(u/D)e\left(\frac{kX}{u}-\frac{mu}{2}\right)\,du.
$$
   Equivalently, it is the difference between integer-frequency and half-integer-frequency Poisson transforms. Stationary phase localizes to $|m|\asymp kX/D^2$ for the appropriate sign of $m$.

What is not proved is Gemini's stronger obstruction claim that the factor $(-1)^m$ yields a meaningful A-process collapse that blocks all B-process use. After splitting into the two cosets, there is no multiplicative character left; there are instead two shifted smooth phase families.

2. DeepSeek's "no alternating sign survives" claim also needs correction.

It is true in the integer/half-integer split formulation, but false in the odd-sublattice formulation. The issue is not whether $(-1)^m$ appears; it does. The issue is whether it is intrinsic and useful. It appears to be a bookkeeping artifact of indexing the two dual cosets as one sequence.

3. The exact H5r norm required by the proof needs to be restated.

DeepSeek says the proof requires
$$
   \frac1{H_D}\sum_{k\sim K_0}
   \left|
   \sum_{d\sim D,\ 2\nmid d}e(kX/d)
   \right|
   \ll X^{1/4+\epsilon}.
$$
   This is a sufficient termwise $L^1$ target, but it may be stronger than necessary. From the Fejer expansion,
$$
   \sum_{d\sim D,\ 2\nmid d}K_H(X/d)
   =
   \sum_{|k|\le H}
   \left(1-\frac{|k|}{H+1}\right)
   \sum_{d\sim D,\ 2\nmid d}e(kX/d).
$$
   Therefore a blockwise bilinear estimate with the actual Fejer coefficients, or uniformly for bounded coefficients $v_k$, may suffice:
$$
   \left|
   \sum_{k\sim K_0}v_k
   \sum_{d\sim D,\ 2\nmid d}e(kX/d)
   \right|
   \ll_\epsilon K_0X^{1/4+\epsilon}.
$$
   If this is required uniformly in arbitrary $|v_k|\le 1$, it implies the $L^1$ version by choosing $v_k$ to match phases. If $v_k$ is fixed to the Fejer weights, the target is weaker and may preserve some $k$-cancellation. The next synthesis must distinguish these three versions:
   - fixed Fejer coefficients;
   - uniform bounded coefficients;
   - termwise $L^1$ absolute values.

4. Gemini's sharp Perron height claim needs a precise formulation.

The heuristic that standard sharp Perron truncation needs $T\gtrsim X^{3/4}$ to make boundary-window mass $O(X^{1/4})$ is plausible for uniform sharp cutoff bounds. But the exact statement should be limited to the standard absolute truncation estimate. It is not a theorem that all Perron-type approaches require $T=X^{3/4}$, because smoothing, endpoint avoidance, or cancellation in the truncation kernel can change the conclusion.

5. Gemini's H11 "Voronoi Circularity Trap" is diagnostic, not proved.

Applying the functional equations to $\zeta(s)L(s,\chi_4)$ does connect Perron to Voronoi/Hardy Bessel expansions. But the claim that any successful contour method must shift to $\Re(s)\le 1/4$ and therefore must fall into the zero-Hessian trap is too strong. A method could attempt cancellation on $\Re(s)=1/2$ through spectral, moment, or bilinear input. No impossibility theorem has been shown.

6. DeepSeek's Lemma L5 has a scaling issue.

It states that if
$$
   \frac1{H_D}\sum_{k\sim K_0}|S(k,D)|
   \ll X^{\theta+\epsilon},
$$
   then the Vaaler route yields
$$
   P(X)\ll X^{1/4+\theta+\epsilon}.
$$
   This does not match the usual notation. If the residual target itself is $X^{\theta+\epsilon}$ after the $1/H_D$ normalization, then the route gives $P(X)\ll X^{\theta+\epsilon}$, not $X^{1/4+\theta+\epsilon}$. If instead $\theta$ is meant to measure saving relative to a trivial $X^{1/4}$ factor, the lemma must define that normalization explicitly.

Possible errors or hidden assumptions:

1. Overclaim in Gemini: "structural exhaustion of continuous smoothing methodologies."

The outputs establish obstructions for specific transformations: Vaaler with positive Fejer majorant, Poisson/B-process followed by naive differencing, and standard Perron/Voronoi reformulation. They do not exhaust all continuous or harmonic-analytic methods. This should be downgraded to a "continuous trilemma diagnostic," not a conclusion.

2. Overclaim in Gemini: "C2 and C3 should be formally elevated to proved algebraic obstructions."

C3 is only true for the coefficient factor in one representation of the dual odd-lattice sum. Since the same Poisson transform can be written as two shifted untwisted dual sums, the claimed collapse is not a representation-invariant obstruction.

3. Overclaim in DeepSeek: "The H5r proof actually requires a weighted sum of absolute values."

The proof requires bounding a positive Fejer-kernel sum. Bounding it by termwise $L^1$ in $k$ is sufficient but may not be necessary. A blockwise bilinear estimate with Fejer coefficients may be enough. The repo should avoid accidentally strengthening H5r beyond what Vaaler demands.

4. Hidden assumption in both outputs: Li--Yang/divisor estimates automatically apply to H5r.

H5r contains parity restrictions, shifted phases, Fejer weights, and possibly blockwise absolute values. A clean dictionary to Li--Yang must verify:
   - allowed $h$ and $d$ ranges;
   - smoothness of $w_D$ and $v_k$;
   - whether the theorem controls fixed-coefficient bilinear sums, $L^2$ averages, or $L^1$ sums;
   - whether parity splitting adds a linear phase outside the theorem's hypotheses;
   - whether the local cutoff $H_D\asymp DX^{-1/4}$ falls in the stated parameter ranges.

5. Hidden assumption in Gemini: Perron sharp truncation lower bounds are unavoidable.

The boundary-annulus heuristic shows that standard absolute truncation estimates are expensive. It does not rule out smoothed Perron, explicit formulas with carefully chosen kernels, or cancellation in the Perron tail.

6. Hidden assumption in DeepSeek: Mellin--Perron "reduces to the same analytic double sums."

This is likely correct at the level of standard approximate functional equations or Voronoi summation, but it should be proved by writing the transformed sum, its phase, its weights, and its dyadic ranges. Until then it is a strong structural expectation, not a checked lemma.

7. Possible sign and normalization fragility in both Poisson computations.

The sign of the stationary variable depends on whether the Fourier transform convention is $e(-mx)$ or $e(mx)$ and whether the phase is $e(kX/u-mu/2)$ or $e(kX/u+mu/2)$. The final obstruction does not depend strongly on this, but the lemma bank should not record exact phases until the convention is fixed.

Suggested synthesis:

The next state should not choose between Gemini and DeepSeek wholesale. It should combine DeepSeek's residual-norm correction with a corrected version of Gemini's Poisson-dual calculation.

Recommended lemma/status updates:

1. **H5r. Fejer residual target, corrected.**
   Status: required target; exact norm still to decide.

For $X^{1/4}\le D\le X^{1/2}$, $H_D\asymp DX^{-1/4}$, the first residual is bounded by
$$
   |R_{1,D}|
   \ll
   \frac1{H_D}
   \sum_{d\sim D,\ 2\nmid d}K_{H_D}(X/d).
$$
   Expanding $K_H$ gives a zero mode $D/H_D$ and nonzero reciprocal sums
$$
   \frac1{H_D}
   \sum_{1\le |k|\le H_D}
   c_k
   \sum_{d\sim D,\ 2\nmid d}e(kX/d).
$$
   A sufficient dyadic target is
$$
   \left|
   \sum_{k\sim K_0}v_k
   \sum_{d\sim D,\ 2\nmid d}e(kX/d)
   \right|
   \ll_\epsilon K_0X^{1/4+\epsilon}
$$
   for the needed coefficient class $v_k$. The judge should decide whether $v_k$ must be arbitrary bounded coefficients or only Fejer-type smooth coefficients.

2. **C2. Poisson dual of parity residual, corrected.**
   Status: partially proved transformation; not an obstruction theorem.

The odd restriction can be dualized as
$$
   \sum_{2\nmid d}w_D(d)e(kX/d)
   =
   \frac12\sum_{m\in\mathbb Z}(-1)^m
   \int w_D(u)e\left(\frac{kX}{u}-\frac{mu}{2}\right)\,du.
$$
   Equivalently, it is a difference of integer and half-integer Poisson transforms. Stationary phase gives dual length
$$
   |m|\asymp \frac{kX}{D^2}
$$
   and square-root phase. The alternating factor is not yet a useful obstruction because it can be absorbed into the two-coset formulation.

3. **C3. Dual A-process parity degeneration.**
   Status: proposed diagnostic; do not mark proved.

If the dual odd-lattice sum is forcibly represented as one sequence indexed by $m$ with coefficient $(-1)^m$, then the shifted coefficient product is
$$
   (-1)^m(-1)^{m+q}=(-1)^q.
$$
   This shows that direct A-process does not extract deep mod-$2$ cancellation from the coefficient alone. It does not prove that B-process-first is useless, because the phase and two-coset structure remain nontrivial.

4. **H10. Mellin--Perron non-majorizing route.**
   Status: standard reformulation; useful comparison route.

Record the exact Perron formula for
$$
   4\zeta(s)L(s,\chi_4)
$$
   and compare three errors:
   - sharp Perron truncation;
   - smoothed Perron truncation;
   - Voronoi/Hardy transform after the functional equation.

The route avoids Fejer positivity but imports classical contour-integral or Bessel-sum estimates. It should not be advertised as an escape unless it preserves $\chi_4$ through all error terms and yields a new dyadic target different from H5r.

5. **H11. Voronoi circularity diagnostic.**
   Status: diagnostic only.

It is true that applying functional equations to the Perron integral recovers Voronoi/Hardy-type oscillatory expansions. It is not proved that every successful Perron method must pass through the zero-Hessian obstruction.

Score by agent:

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|---|---:|---|---|
| `gemini_deep_think` | 7 | Strong explicit Poisson-on-odd-lattice calculation and useful Perron/Voronoi diagnostic, but overpromotes C2/C3 and H11 from diagnostics to proved obstructions. | Reconcile the $(-1)^m$ odd-lattice formula with the integer/half-integer dual-coset formula; downgrade "continuous exhaustion" and prove only the invariant Poisson statement. |
| `deepseek_api` | 8 | Best identification of the Fejer residual as the central bottleneck and strongest challenge to C2; useful insistence that H5r's norm be formulated exactly. | Correct the overstatement that termwise $L^1$ in $k$ is necessary; fix the scaling in conditional C1/L5; clarify that C2's alternating factor exists in one representation but is not invariantly obstructive. |

Next-round recommendation:

The next round should focus on a precise H5r norm theorem and a corrected C2 lemma. Do not pivot yet to "exclusive discrete Bombieri-Iwaniec matrices"; first settle what the Vaaler residual actually requires.

Concrete recommended tasks:

1. Write H5r in three versions and classify them by strength:
   - fixed Fejer coefficients;
   - arbitrary bounded dyadic coefficients $v_k$;
   - termwise $L^1$ over $k$.
   Then prove exactly which version is sufficient for the Vaaler proof.

2. Produce a convention-fixed Poisson lemma for
$$
   \sum_{2\nmid d}w(d/D)e(kX/d),
$$
   showing explicitly the equivalence between:
$$
   \frac12\sum_m (-1)^m I(m/2)
$$
   and the difference of integer and half-integer dual transforms.

3. Test whether an A-process applied after this Poisson step genuinely loses all parity information or whether the two-coset phase shift leaves a usable spacing distinction.

4. Rework the Mellin--Perron route as a comparison module, not as a barrier theorem. The required output should be:
   - exact Perron formula;
   - standard sharp truncation estimate and its $T$-dependence;
   - smoothed Perron alternative;
   - functional-equation/Voronoi transformation;
   - resulting dyadic sums and whether they match H5a/H5b/H5r.

5. Keep the current research status conservative: no new exponent has been proved; H5r remains the central bottleneck; C2 is unresolved in obstruction strength; Mellin--Perron is useful mainly as a non-majorizing control experiment.

--- REVIEW FROM gemini_deep_think ---
This is the Stage B cross review for Round 6.

### Most valuable input from others

**From `gpt_pro_thinking`:**
The most valuable input is the flawless algebraic execution of both the **H5r-to-Li--Yang Phase Dictionary** and the **C2 Poisson Transform**. By computing the exact Bombieri--Iwaniec spacing determinant $F'F''' - 3(F'')^2 = -6(x+1/D)^{-6} \neq 0$ for the parity-split phase $F_{2,1}(x)$, `gpt_pro_thinking` demonstrates structurally that the character-blind residual is not a pathological phase, but belongs precisely to the standard Dirichlet divisor problem (DDP) reciprocal-sum class.

**From `deepseek_api`:**
While `deepseek_api`'s review contains severe algebraic errors (detailed below), its structural observation regarding the **Mellin--Perron alternative (H10)** is conceptually valuable. It correctly points out that bypassing the Vaaler majorant via complex integration naturally preserves the $\chi_4$ character via the approximate functional equation, but doing so shifts the difficulty to a subconvexity/moment problem for $\zeta(s)L(s,\chi_4)$ that appears analytically equivalent to the original 2D exponential sum endpoint.

### Claims that look correct

1. **C1 (Fejer Majorant DDP Trap):** `gpt_pro_thinking`'s formulation of C1 as a conditional proposition is rigorously calibrated. Bounding the pointwise positive Vaaler majorant evaluates the GCP error terms into character-blind parity sums, which appears to lock the route at the divisor exponent $\theta_{\text{div}} \approx 0.314$ unless a broader DDP spacing breakthrough occurs.
2. **C2 (Parity-Dual Collapse):** `gpt_pro_thinking`'s demonstration that a sequential B-process then A-process on the parity residual degenerates algebraically is correct. The alternating sign generated by the parity condition collapses under Weyl differencing.
3. **H10 (Non-majorizing equivalence):** The recognition by both agents that escaping the DDP trap relies on evaluating either Mellin--Perron contours or signed Fourier truncations is well-founded.

### Claims that need proof

1. **Signed Fourier High-Frequency Tails:** While signed truncations preserve $\chi_4$, they produce conditionally convergent high-frequency tails $\sum_{|h|>H_D} \frac{1}{h} B_1(h, D; X)$. It remains not yet established whether these tails are analytically more tractable than the divisor-like residual H5r, especially given Gibbs phenomenon spikes near hyperbola integer discontinuities.
2. **Uniform Stationary Phase for C2:** While the algebraic sign $(-1)^n$ is correct for the dual parity sum, making operational use of the lemma requires establishing uniform nonstationary and transition-range bounds where the dual frequency $m \asymp kX/D^2$ is small.
3. **Character Survival under Cauchy-Schwarz:** Even if non-majorizing truncations (Mellin--Perron) preserve $\chi_4$, it requires showing that modern 2D spacing matrices can exploit this sign *before* applying Cauchy--Schwarz, which evaluates $|\chi_4(d)|^2 = 1_{2\nmid d}$ and instantly reverts the terms to character-blind parity sums.

### Possible errors or hidden assumptions

This round surfaced two massive mathematical "false negative" review errors by `deepseek_api`, which must be strictly corrected to protect the repository's structural integrity:

**1. False Refutation by Parametrization / Sign Error (The C2 Error):**
`deepseek_api` claims that `gpt_pro_thinking`'s C2 calculation is incorrect and that the dual of the parity sum yields NO alternating sign. `deepseek_api` splits the sum into $S_0 - S_1$. For $S_1$, the phase is derived as $kX/Du - (m-1/2)Du$.
*Correction:* `deepseek_api` makes a fatal calculus sign error, claiming the derivative root requires $m-1/2 > 0 \implies m \ge 1$. The derivative of $1/u$ is $-1/u^2$. The stationary condition is $-kX/(Du^2) - (m-1/2)D = 0$, which strictly forces $m-1/2 < 0 \implies m \le 0$. Thus $S_1$ generates negative half-integer frequencies $\{-1/2, -3/2, -5/2, \dots\}$. $S_0$ generates negative integer frequencies $\{-1, -2, -3, \dots\}$. By scaling by $-1$ to view positive frequencies $N/2$, $S_0$ contributes the even numerators $N=2, 4, 6 \dots$ with a positive sign (since it is added). $S_1$ contributes the odd numerators $N=1, 3, 5 \dots$ with a negative sign (since it is subtracted). This interleaves perfectly into the sequence $-1, +1, -1, +1 \dots$, which evaluates identically to $(-1)^N$. `gpt_pro_thinking` is 100% correct: the alternating character exists, and A-process differencing collapses it to a constant.

**2. Premature Absolute Value / Triangle Inequality Fallacy (The H5r Error):**
`deepseek_api` falsely claims the Vaaler majorant requires termwise absolute values inside the $k$-sum (i.e., bounding $\sum c_k |\sum_d e(kX/d)|$), and attacks `gpt_pro_thinking` for proposing a bilinear sum.
*Correction:* The pointwise majorant inequality is $|R_H(t)| \le \frac{1}{2H+2}K_H(t)$. Summing over the parity support yields an error bounded by $\sum_d 1_{2\nmid d} K_H(X/d)$. Expanding the Fejer kernel yields exactly the bilinear double sum $\sum_k c_k \sum_d 1_{2\nmid d} e(kX/d)$. Because $K_H(t) \ge 0$, this evaluated 2D sum is already a real, non-negative number. It intrinsically equals its own absolute value. There is no mathematical law forcing the absolute value inside the $k$-sum. `gpt_pro_thinking`'s formulation of H5r as a structured bilinear sum is entirely rigorous.

### Explicit Lemma/Claim Audits

**Lemma H5r: Bilinear Residual Target**
*Status: Verified against false critique.*
The Vaaler residual contribution reduces exactly to evaluating the 2D bilinear sum: $\sum_{|k| \le H_D} c_k \sum_{d \sim D} 1_{2\nmid d} e(kX/d)$. Pushing the absolute value inside the $k$-sum is a premature application of the triangle inequality and is mathematically unnecessary because the spatial sum over the Fejer kernel is strictly non-negative.

**Lemma C2: Parity Dual Degeneration**
*Status: Algebraically verified.*
Applying Poisson summation to the parity-supported sequence $1_{2\nmid d} e(kX/d)$ yields a dual sum over frequencies $N/2$ ($N \ge 1$) with leading phase $\sqrt{2kXN}$ and an amplitude incorporating $(-1)^N$. A subsequent A-process (Weyl differencing) yields $(-1)^N (-1)^{N+q} = (-1)^q$. B-process-first does not protect the parity sequence from A-process arithmetic degeneration.

**Lemma C1: Fejer Majorant DDP Trap**
*Status: Verified conditional diagnostic.*
If one bounds the error term exclusively via the positive Vaaler truncation, the Gauss Circle error reduces to character-blind DDP sums. Therefore, the Vaaler proof route yields at best $P(X) \ll_\epsilon X^{\theta_{\text{div}} + \epsilon}$, suggesting the endpoint $1/4$ cannot be reached under this specific proof skeleton without a DDP spacing breakthrough.

**Lemma H10: Non-majorizing Truncation Equivalence**
*Status: Structural map.*
Mellin--Perron or signed Fourier truncation avoids the positive majorant trap but shifts the analytical requirement to endpoint-strength bounds on $\zeta(s)L(s,\chi_4)$ moments or conditionally convergent high-frequency character-twisted tails.

### Concrete counterexample and stress-test checks

1. **Parametrization Sequence Equivalence Check (Refuting DeepSeek's C2 error):** Evaluate the dual frequencies of $S_0$ and $S_1$ via standard integration. Verify that the stationary roots yield $m \le 0$ and map perfectly to an interleaved half-integer lattice. Observe that subtracting the half-integer sequence generates the strictly alternating signs $(-1)^N$ over the combined integer index $N$.
2. **$L^1$ vs Bilinear Divergence Test:** Numerically evaluate $\sum_k c_k \sum_d e(kX/d)$ versus $\sum_k c_k |\sum_d e(kX/d)|$ for test bounds $X=10^4, D=30$. Confirm the latter is artificially larger, confirming that demanding an $L^1$ norm over $k$ is an unnecessary analytical handicap.
3. **Spatial Cauchy-Schwarz Degeneration Test:** Symbolically execute the first step of the Bombieri-Iwaniec spacing method on the signed main sum $\sum_{h} \sum_d \chi_4(d) e(hX/d)$. Observe if Cauchy-Schwarz over $h$ or $d$ unavoidably evaluates $|\chi_4(d)|^2 = 1_{2\nmid d}$, which would suggest that spacing methods are inherently character-blind regardless of the truncation method.

### Confidence calibration and failure modes

**Confidence:**

* **High** that C2 is algebraically correct and `deepseek_api`'s refutation was driven by a calculus sign error combined with a split-parameterization illusion.
* **High** that H5r does not require absolute values on the inner sum.
* **Moderate** that signed Fourier tails (H10) are analytically viable, as standard high-frequency convergence issues may render them harder than the DDP trap itself.

**Failure Modes:**

1. **False Refutation by Parametrization:** Reviewers may split an arithmetic sequence into sub-progressions, compute their duals separately, and fail to recognize that the combined dual frequencies naturally interleave to reconstruct global algebraic factors (like $(-1)^N$).
2. **Premature Absolute Value Trap:** Researchers may assume that applying a positive majorant like $K_H(t)$ to a sum forces the use of the triangle inequality on the Fourier coefficients $\sum |\hat{K}(k) S_k|$. Because the summed kernel is globally positive, one can evaluate the resulting signed bilinear double sum directly.
3. **Spatial Cauchy-Schwarz Character Loss:** Even if we preserve $\chi_4$ via Mellin--Perron, the analytic method used to bound the resulting sums might inherently strip the character during correlation steps, making the pursuit of non-majorizing truncations an analytic illusion.

### Suggested synthesis

We have mapped the structural boundary of the arithmetic hyperbola route: **The Gauss Circle Problem inherently contains the Dirichlet Divisor Problem at its discontinuities.** Because the sawtooth $\psi(X/a)$ is discontinuous at the hyperbola integers $ab=X$, any pointwise positive majorant (like Vaaler) forces an absolute-value-equivalent bound on $\chi_4(a)$, stripping the character and evaluating the GCP error term as a character-blind DDP error term.

The proof skeleton should explicitly bifurcate to reflect this:

1. **The DDP Barrier (Vaaler Track):** Pointwise positive majorants map GCP to DDP. Using Vaaler suggests accepting the divisor exponent $\theta^* \approx 0.314$ as a structural ceiling.
2. **The Signed Escape (Non-majorizing Track):** To preserve $\chi_4$ and attempt to reach $X^{1/4+\epsilon}$, one appears to require exact Fourier truncation or Mellin--Perron. This avoids the character-blind residual but introduces high-frequency tails or subconvexity targets.

The repo should formally demote the Vaaler route to an "obstruction map" and pivot to investigating whether preserving $\chi_4$ via H10 survives spatial Cauchy--Schwarz.

### Score by agent

| Agent reviewed | Score (0-10) | Main reason | Must verify next |
| --- | --- | --- | --- |
| `gpt_pro_thinking` | 9 | Superb phase dictionary execution and flawless algebraic derivation of the C2 Poisson transform and alternating collapse. | Verify uniform stationary phase bounds for the C2 dual sum near transition ranges. |
| `deepseek_api` | 4 | Introduced two severe "false negative" review errors by hallucinating an absolute value requirement on the Fejer majorant and failing a basic calculus derivative in its C2 refutation. | Must verify algebraic equivalences carefully before claiming an identity is false. |

### Next-round recommendation

1. **For the Judge:** Formalize the "Grand Synthesis": Pointwise positive majorants for the hyperbola method reduce the GCP to the DDP. Freeze the Vaaler route as an obstruction map.
2. **For the Agents:** Pivot entirely to H10. Write the exact replacement error for the signed Fourier truncation: the high-frequency tail $\sum_{|h|>H} \frac{1}{h} \sum_d \chi_4(d) e(hX/d)$. Execute the "Spatial Cauchy-Schwarz Degeneration Test" to determine if standard 2D spacing methods can actually exploit the preserved $\chi_4$, or if they instantly square it away, which would establish that the DDP barrier remains absolute across all current analytic spacing techniques.

--- REVIEW FROM deepseek_api ---
## 1. Introduction and scope

This is the Stage B cross-review for Round 6 of the Gauss circle project. The two active agents are
`gpt_pro_thinking` and `gemini_deep_think`; I (`deepseek_api`) act as algebra checker, obstruction auditor and independent reviewer.
I have read both outputs, compared them with the current lemma bank, gap register and reading packet, and performed independent algebraic checks on the critical formulas. The review is organised into the sections required by the protocol, includes explicit lemma/claim boxes, and calibrates confidence.

---

## 2. Overall synthesis and most valuable contributions

Both agents agree on the main bottleneck: the **Vaaler/Fejer residual H5r** now dominates the arithmetic route.
The most valuable output from `gpt_pro_thinking` is the exact *H5r-to-Li-Yang dictionary*, which shows that the residual sums are structurally reciprocal-phase sums of Bombieri--Iwaniec type, albeit without the signed character.
The most valuable output from `gemini_deep_think` is the sharp diagnostic that the positive Fejer majorant strips $\chi_4$ and reduces the first residual to a parity-supported divisor-like object; the dual parity collapse (C2) is then correctly identified as an algebraic obstacle.

I concur that **no improvement to the Gauss exponent has been proved** in this round. The concrete gain is a cleaner, more precise obstruction map.

---

## 3. Detailed assessment of `gpt_pro_thinking` (Stage A)

### 3.1 C1 as a conditional proposition
The formulation is logically sound:
If the only available bounds for the H5r families $C_1, C_{2,\rho}$ are "character-blind reciprocal-sum estimates" with exponent $\theta$, then the Vaaler route can deliver at best
$$
P(X)\ll_\epsilon X^{\max(1/4,\,\theta)+\epsilon}.
$$
This is a **conditional implication**, not a lower bound. It correctly depends on the hypothesis that the main families H5a/H5b are not worse. The statement should be recorded as
> **Claim C1 (conditional)** -- not as a theorem of impossibility.

*Potential gap*: "character-blind reciprocal-sum estimates" is not a precisely defined class. In practice it means bounding sums of the type $\sum_d a_d e(kX/d)$ with $|a_d|\le1$ using only the phase, without exploiting congruence patterns of the coefficients. The conditional remains meaningful if one specifies that the available theorem is, e.g., the Li--Yang bound applied to the parity-split sum. I recommend to make the hypothesis explicit.

### 3.2 H5r-to-Li-Yang dictionary
The derivation for $C_1$ and $C_{2,\rho}$ is algebraically correct and useful.
For $C_1$ the parity condition is translated into a smooth phase $F_{2,1}(x)=1/(x+1/D)$. The derivatives yield
$$
F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2 = -\frac{6}{(x+1/D)^6}\neq 0,
$$
so the phase is nondegenerate in the sense of Bombieri--Iwaniec.
For $C_{2,\rho}$ the phase $F_2(x)=1/(4x)$ gives a nonzero quantity $-3/(8x^6)$.

These checks confirm that the **geometric obstruction** is not malformed phase geometry; it is purely the arithmetic lack of $\chi_4$ in the residuals.

*Important remark*: The dictionary assumes smooth dyadic weights and block-level absolute values (not termwise). This is the correct delicate placement; termwise absolute values would prematurely destroy two-variable structure.

### 3.3 C2 Poisson calculation
The algebraic step is **correct**. The formula
$$
S_{\mathrm{odd}}(k,D)=\frac12\sum_{n\in\mathbb Z}e(n/2)\int_{\mathbb R} w(u/D)e\!\left(\frac{kX}{u}-\frac{nu}{2}\right)du
$$
follows from Poisson summation modulo $2$. I verified the derivation (see § 5.2). The conclusion that the dual alternating factor satisfies
$$
(-1)^m(-1)^{m+q}=(-1)^q
$$
after a direct A-process is exact. Hence B-process does not create a durable character for the parity residual.

*Gap*: the analytic use of this dual representation requires a **uniform stationary-phase lemma** with control of amplitudes, nonstationary frequencies, and transition regions. The algebraic part is proved; the analytic wrapper is still missing.

### 3.4 Non-majorizing truncation comparison (H10)
The three-way comparison (Vaaler, signed Fourier, Mellin--Perron) is a helpful taxonomy. It correctly notes that signed Fourier truncation replaces H5r by high-frequency signed reciprocal tails (which may be as hard), and that Mellin--Perron replaces H5r by a complex-analytic moment problem for $\zeta(s)L(s,\chi_4)$. Both are plausible escape routes but none is developed yet.

### 3.5 Poisson--Bessel calibration
The secondary calibration module is kept alive; no errors there.

---

## 4. Detailed assessment of `gemini_deep_think` (Stage A)

### 4.1 "Fejer Majorant DDP Trap" (C1)
Gemini pushes C1 to a stronger claim: the Vaaler skeleton "unconditionally anchors the Gauss Circle error term to the DDP limit". This is **not yet proved** as a mathematical impossibility. It is a highly plausible diagnostic, but to become a theorem one would need to show that the H5r sums cannot be smaller than the corresponding divisor-problem sums without breaking a known barrier. The current state is that H5r sums are **structurally divisor-like**, but that alone does not exclude a clever argument exploiting the specific origin of these sums (for instance, the Fejer coefficients have sign patterns, or interference between blocks). I therefore recommend keeping C1 as a **diagnostic obstruction**, not an unconditional anchor.

### 4.2 H6 normalization
Gemini correctly endorses the exponent-pair scaling $3\kappa+2\lambda\le1$ under the standard $T\asymp hX/D$ convention. The derivation is straightforward and can be regarded as a proved diagnostic (the inequality is a necessary condition for a character-blind 1D method to reach $X^{1/4}$). I agree that H6 can be **promoted to proved** under the explicit hypotheses stated in the lemma bank.

### 4.3 Dual Parity Degeneration (C2)
Gemini's derivation via Poisson modulo $2$ matches the algebraic core. The additional note that the B-process merely delays the H7-type collapse is pertinent. The explicit formula
$$
S_{\mathrm{res}}(k,D) = \frac12\sum_{m\in\mathbb Z}(-1)^m\int w_D(u)e\!\left(\frac{kX}{u}-\frac{m u}{2}\right)du
$$
is correct (up to a possible factor of $e(m/2)$ instead of $(-1)^m$; both are equivalent after reindexing). I verified the algebra; see § 5.2.

### 4.4 Mellin--Perron alternative (H10)
Gemini sketches the unsmoothed Perron formula for $4\zeta(s)L(s,\chi_4)$. The contour shift and truncation error are mentioned. However, no concrete error bound is derived. The statement that "standard absolute value bounding of the sharp Perron cutoff necessitates an absolute-value sum over $r_2(n)$ in the narrow boundary window" is **qualitatively correct** but needs quantitative development. The unsmoothed Perron formula has a well-known truncation error involving the tail of the generating series; to bound it at the scale $X^{1/4}$ would require very strong subconvexity or moment estimates. This is a serious gap.

### 4.5 Stress-test with Bourgain's decoupling pair
Gemini tests the H6 inequality with an extreme exponent pair $(13/84,55/84)$, obtaining $149/84>1$. This illustrates that even the best 1D restriction theory falls short, but it is not a proof of impossibility because H6 only applies to methods that use a **1D exponent pair**; Bombieri--Iwaniec methods are two-variable and not covered. Still, it is a useful sanity check.

---

## 5. Independent algebraic checks

### 5.1 H5r dictionary: derivative nondegeneracy
I recomputed the quantities for both $F_{2,1}$ and $F_2$ using the explicit formulas from §3.2 and obtained the same nonzero expressions. The derivatives are all bounded away from zero on fixed dyadic intervals away from the origin. Therefore the phase is nondegenerate in the sense required by the Bombieri--Iwaniec quadratic form condition.

**Conclusion**: The H5r sums belong to the same geometric class as the Li--Yang double sums. The only difference is the coefficient structure.

### 5.2 C2 Poisson normalization
Let $f(d)=w(d/D)e(kX/d)$. The standard Poisson summation for an arithmetic progression modulo $2$ gives
$$
\sum_{d\ \text{odd}} f(d)=\frac12\sum_{n\in\mathbb Z}\bigl(1-(-1)^n\bigr)\widehat f(n/2)
= \frac12\sum_{n\in\mathbb Z}e(n/2)\widehat f(n/2),
$$
where $\widehat f(\xi)=\int f(u)e(-\xi u)du$ with $e(t)=e^{2\pi i t}$. Indeed,
$$
\sum_{d}f(d)=\sum_{m}\widehat f(m),\qquad
\sum_{d}f(d)e(d/2)=\sum_{m}\widehat f(m-1/2),
$$
and subtraction yields the formula. Thus
$$
\sum_{d\ \text{odd}} f(d)=\frac12\sum_{n\in\mathbb Z}e(n/2)\int w(u/D)e\!\left(\frac{kX}{u}-\frac{nu}{2}\right)du.
$$
This is algebraically exact. After stationary phase, the dominant terms have $n=-m<0$ and the factor $e(-m/2)=(-1)^m$. Good.

### 5.3 Exponent-pair inequality
With $f(d)=hX/d$, $f'(d)\asymp hX/D^2$, interval length $D$, so $T\asymp hX/D$. If an exponent pair $(\kappa,\lambda)$ gives
$$
\sum_{d\asymp D}e(f(d))\ll T^\kappa D^\lambda X^\epsilon,
$$
then the inner sum is $\asymp X^{(3\kappa/4+\lambda/2)}$ at the endpoint $D=X^{1/2},h=X^{1/4}$. To satisfy the H5a target (i.e., the inner sum $\ll X^{1/4}$), one needs $3\kappa+2\lambda\le1$. The derivation is correct.

---

## 6. Hidden assumptions and possible errors

1. **C1 hypothesis:** The conditional assumes that the only bounds available are "character-blind reciprocal-sum estimates". If a method exists that exploits the specific Fejer coefficients or the cancellation between different $k$ blocks, the conditional does not apply. The current formulation is a **conditional proof**, not an impossibility theorem.

2. **H5r weights:** The dictionary uses smooth weights $v_k$ and $w_D$. Actual Fejer residual weights are $(1-|k|/(H+1))$, which are indeed smooth on the dyadic blocks. So this matches. However, the Li--Yang-type theorems may require compact support or specific smoothness; a careful match of hypotheses is still needed.

3. **Absolute-value placement:** In the H5r target, the block-level absolute value is used. Summing absolute values over dyadic blocks and then over $k$ is standard. The proof skeleton must not use termwise absolute value in $k$ because that would discard the two-variable structure. Both agents seem aware of this.

4. **Vaaler majorant exactness:** The stated inequality $|R_H(t)|\le \frac1{2H+2}K_H(t)$ is correct for the specific approximation $\psi(t)$ with coefficients $\alpha_h = -\frac1{2\pi i h}(1-|h|/(H+1))$? Actually standard Vaaler coefficients are often $\alpha_h = \frac{i}{2\pi h}$ with a different factor? I should check: Vaaler's theorem (Bull. London Math. Soc. 1985) gives a polynomial $P_H(t)$ such that $|\psi(t)-P_H(t)|\le \frac{1}{2H+2}K_H(t)$. The exact coefficients are not needed for the structure, only the bound. So it's acceptable as a theorem dependency. However, the lemma bank should cite a precise reference.

5. **Mellin--Perron unsmoothed:** The unsmoothed Perron formula with sharp cutoff is notoriously delicate; the truncation error is often of size $O(X/T + \text{...})$ and may require smoothing to control. The proposed route must eventually choose a smoothed version (e.g., Perron with a kernel) or confront the sharp-cutoff difficulties.

6. **Poisson--Bessel calibration:** Still not written; the repo lacks a complete proof of the classical $R^{2/3}$ bound, but that is a lower-priority task.

---

## 7. Lemma and claim boxes

### Lemma R1 (C2 Poisson identity)
**Status**: Algebraically proved.
For $f\in L^1(\mathbb R)$ smooth and rapidly decaying,
$$
\sum_{\substack{d\in\mathbb Z\\ d\ \text{odd}}} f(d) = \frac12\sum_{n\in\mathbb Z} e(n/2)\int_{\mathbb R} f(u) e(-nu/2)\,du.
$$
In particular, with $f(u)=w(u/D)e(kX/u)$, the right-hand side is $\frac12\sum_n (-1)^n\int w(u/D)e(kX/u - nu/2)du$.

### Lemma R2 (C1 conditional)
**Status**: Proved as conditional implication.
Let $\theta\ge 1/4$. Assume that for all $X^{1/4}\le D\le X^{1/2}$ and $1\le K_0\le H_D$, with $H_D\asymp D X^{-1/4}$, one has
$$
|C_1(K_0,D;X)|,\ |C_{2,\rho}(K_0,D;X)| \le C_\epsilon K_0 X^{\theta+\epsilon},
$$
with smooth Fejer/dyadic weights. Then the Vaaler route yields
$$
P(X)\ll_\epsilon X^{\max(1/4,\theta)+\epsilon}.
$$
*Proof*: The zeroth mode gives $D/H_D\asymp X^{1/4}$. The sum over nonzero frequencies is bounded by $\frac1{H_D}\sum_{K_0\le H_D} K_0 X^{\theta+\epsilon} \ll X^{\theta+\epsilon}$.

### Lemma R3 (Exponent-pair scaling)
**Status**: Proved under the stated conventions.
If an exponent pair $(\kappa,\lambda)$ is used in the sense $T\asymp \sup|f'|\cdot(\text{length})$ and the inner sum is estimated trivially over $h$, then the condition to reach the H5 target is
$$
3\kappa+2\lambda\le 1.
$$
This follows from the computation in § 5.3.

### Claim R4 (H5r nondegeneracy)
**Status**: Verified.
The phases $F_{2,1}$ and $F_2$ appearing in the H5r dictionary satisfy $F'F'''-3(F'')^2\neq0$ uniformly on dyadic intervals.

### Lemma R5 (Dual parity A-process collapse)
**Status**: Algebraically proved.
Let the alternating factor be $a_m=(-1)^m$. Then for any integer $q$,
$$
a_m a_{m+q}=(-1)^q,
$$
which is independent of $m$. Hence direct Weyl differencing in the dual variable annihilates the oscillation.

### Claim R6 (Vaaler majorant barrier -- diagnostic)
**Status**: Diagnostic heuristic; not a theorem.
Because the Vaaler residual is bounded by a positive Fejer kernel, the first residual family $C_1$ lacks the signed character $\chi_4$. Any proof that attempts to bound $C_1$ using only general reciprocal-sum technology (without exploiting the specific origin of the Fejer coefficients) is likely to face the same exponent barrier as the divisor problem. A proof that this barrier is *unconditional* would require a formal reduction.

---

## 8. Failure modes

1. **Fejer majorant over-pessimism.** The majorant bound is an inequality; the true residual may be much smaller than the majorant for certain structured $X$ (e.g., squares). If the majorant is not sharp, bounding H5r by the majorant could be unnecessarily weak. A direct estimate of the true residual without majorants might circumvent the DDP trap.

2. **Discrete spacing bypass.** The Bombieri--Iwaniec method often handles double sums directly without majorising the inner sum by a positive kernel. Applying spacing estimates to the original discrete sums may avoid the Fejer majorant altogether, because one would not use the continuous Vaaler approximation.

3. **Mellin--Perron subconvexity gap.** The contour-shift approach requires nontrivial bounds for $\zeta(\sigma+it)L(\sigma+it,\chi_4)$ for $\sigma<1$. Current technology (subconvexity) gives only modest improvements; reaching $X^{1/4}$ would require an enormous advance, possibly equivalent to the original problem.

4. **Signed Fourier truncation tail explosion.** The high-frequency tail $\sum_{H_1>H_D} \frac1{H_1} B_1(H_1,D;X)$ may actually be larger than H5r because the absence of the Fejer averaging forces one to sum many more terms without damping. This could be even harder.

---

## 9. Stress tests and counterexample checks

I propose the following numerical and symbolic tests to sharpen the diagnostics:

1. **True residual vs. majorant (small scale).**
   Choose $X$ up to $10^4$, compute the exact Vaaler residual
$$
   \sum_{d\le y}\chi_4(d)R_{H_D}(X/d)
$$
   and compare it with the majorant $\frac1{2H_D+2}\sum_{d}1_{2\nmid d}K_{H_D}(X/d)$. The ratio will indicate whether the majorant is excessively large in typical cases.

2. **C2 stationary-phase verification.**
   For a few pairs $(k,D)$ in the local ranges, compare the exact sum $\sum_{d\ \text{odd}} w(d/D)e(kX/d)$ with the stationary-phase approximation from the dual sum. Check that the main term is given by the $m$-range $m\asymp kX/D^2$ and that the error after including nonstationary contributions is controlled.

3. **Exponent-pair stress with known pairs.**
   List the current best exponent pairs (e.g., Huxley's pair $(\kappa,\lambda)=(1/13,8/13)$? Actually that's not correct; but use known pairs) and compute $3\kappa+2\lambda$. Show that none satisfy $\le1$. This demonstrates the severity of H6 even if not a proof of impossibility.

4. **Discrete spacing toy example.**
   Construct a small-scale model of the Bombieri--Iwaniec major arcs for the double sum $\sum_{h}\sum_{d}\chi_4(d)e(hX/d)$ and check whether the condition $h_1d_2=h_2d_1$ correlates with the parity of $d$. This would test Gemini's suggestion about rational collision matrices.

---

## 10. Confidence calibration

- **High confidence** in the algebraic correctness of H1, H2, H3, H6 (under stated conventions), H7, C2 (algebraic part), and the H5r dictionary derivative checks.
- **High confidence** that the Vaaler residual cannot be reduced to a scalar error; the Fejer majorant creates nontrivial reciprocal sums.
- **Moderate confidence** that C1 as a conditional statement is correctly proved; moderate confidence that H5r is structurally as hard as the divisor problem, but low confidence that this is a *rigorous barrier* (it's a strong diagnostic).
- **Low confidence** that signed Fourier truncation or Mellin--Perron avoid importing equally hard problems.
- **Low confidence** that B-process (H8) provides any saving, because the dual phase is Hessian-degenerate (H9) and the A-process collapse (C2) reappears.

Overall, the present state is a detailed obstruction map; **no new exponent has been proved**.

---

## 11. Score by agent

| Agent               | Score | Justification |
|---------------------|-------|---------------|
| `gpt_pro_thinking`  | 9.0/10 | Provided the exact H5r dictionary and a clean conditional C1; Poisson calculation correct; missing analytic stationary-phase lemma but that's not a flaw. |
| `gemini_deep_think` | 8.0/10 | Sharp diagnostic on the DDP trap; correctly emphasised dual parity collapse; overstates C1 as unconditional and makes unsupported claims about the Mellin--Perron alternative. |

---

## 12. Next-round recommendation

1. **For the judge (Stage C):**
   - Record C1 as a **conditional diagnostic**, not a theorem.
   - Promote H6 to **proved** under the explicit exponent-pair convention.
   - Keep C2 as algebraically proved; require a uniform stationary-phase lemma before it can be used analytically.
   - Mandate that any future proof must explicitly handle H5r; the scalar-residual shortcut must be rejected automatically.

2. **For `gpt_pro_thinking` (in next Stage A):**
   - Refine C1 by making the hypothesis precise: specify exactly which Li--Yang-type theorem would be applied to H5r, and state the needed exponent.
   - Write the stationary-phase lemma for C2 in full, including amplitude, error bounds, and uniformity over the local ranges.
   - Continue the non-majorizing truncation comparison: for signed Fourier, estimate the tail contribution; for Mellin--Perron, derive the exact truncation error and the required subconvexity bound.

3. **For `gemini_deep_think` (in next Stage A):**
   - Downgrade the Fejer Majorant DDP Anchor to a **diagnostic**; avoid unconditional language.
   - Develop the Mellin--Perron route to lemma level: state the precise Perron formula (with smoothing if needed), the contour shift, the residue extraction, and quantify the error term in terms of moments of $\zeta(s)L(s,\chi_4)$.
   - Provide the rational-collision matrix test for discrete spacing, as suggested.

4. **For `deepseek_api` (myself) in future rounds:**
   - Perform the numerical stress tests listed in § 9 and report.
   - Independently verify the stationary-phase constants for C2.
   - Audit the literature: confirm the Li--Yang setup and check whether their theorem can be applied directly to $C_1$ and $C_{2,\rho}$ without modification.

---

*End of Stage B review.*

## Required Output Schema

Selected main route:
Useful fragments by source:
Rejected or risky ideas:
Known gaps:
New lemmas to add:
Counterexample checks to run:
Next round instructions:
Confidence:
