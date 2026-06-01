You are GPT Pro Thinking, acting as broad strategist, proof synthesizer, and test judge.

Review the other agents' Round 8 outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

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

## Review-Stage Guardrail

This is Stage B cross review for Round 8.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet, not continuing your own proof attempt, and not producing next-round instructions except as recommendations at the end.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



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

Generated after round 7 in run `web-research-test`.

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

Responses, reviews, and judge synthesis are archived under `rounds/web-research-test/round_007/`.

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

## Outputs To Review

--- OUTPUT FROM gemini_deep_think ---
Summary:
Round 8 executes the judge's directives by formalizing the non-majorizing algebraic and dualization structures, explicitly confirming that Mellin-Perron and two-coset dual representations do not bypass the core analytic barriers. First, we extend the rational-collision observation into an exact Near-Collision Character Factorization (Lemma Q1-Ext), proving that $\chi_4$ never acts as pseudorandom noise across near-collision gaps; it is highly deterministic, either tracking a frozen sign or forming a stable alternating block-weight. Second, we verify the two-coset Parity Collapse (Lemma C3-Ext), proving algebraically that translation-invariant spacing completely strips the odd-lattice dual of its parity oscillation, invariant of representation. Third, we develop the Mellin-Perron route to theorem-dependency level, mapping it analytically to the Hardy-Voronoi series and demonstrating it deterministically reconstructs the Hessian-degenerate phase $\sqrt{Xhd}$ and the $X^{1/2}$ dual-length scaling barrier.

Main claim or direction:
The arithmetic Vaaler reduction remains the correct diagnostic framework, with the parity residual H5r-F as the central bottleneck. We must formally downgrade the continuous Mellin-Perron contour approach from a "potential bypass" to an "analytic isomorphism" that securely returns the problem to the degenerate Poisson-Bessel track. Consequently, the problem must be confronted in the discrete parameter space. For the spatial-character main sum (H5a), the new factorization (Q1-Ext) proves that Bombieri-Iwaniec rational spacing matrices naturally preserve the character without premature absolute values. The immediate direction must be testing whether Li-Yang or Huxley frameworks can successfully sum over the near-collision gap $\Delta$ to explicitly exploit the $(-1)^{\Delta/2}$ or strict alternation isolated by Q1-Ext.

Detailed reasoning:
**1. Near-Collision Character Factorization (Q1-Ext):**
In Bombieri-Iwaniec spacing matrices, we evaluate bilinear structures over near-collisions $d_1 b - d_2 a = \Delta$ for coprime slope variables $a,b$. To evaluate H5a, we must evaluate the character product $\chi_4(d_1)\chi_4(d_2)$ for odd denominator variables $d_1, d_2$.
- *Case 1 ($a, b$ both odd):* The difference of odd products implies $\Delta$ is strictly even.
Modulo 4, we have $d_1 b \equiv d_2 a + \Delta \pmod 4$. Multiplying by $b$ (since $b^2 \equiv 1 \pmod 4$) gives $d_1 \equiv d_2 a b + \Delta b \pmod 4$.
Multiplying by $d_2$ gives $d_1 d_2 \equiv d_2^2 a b + \Delta b d_2 \equiv a b + \Delta \pmod 4$ (because $d_2^2 \equiv 1 \pmod 4$, $\Delta$ is even, and $b, d_2$ are odd, so $\Delta b d_2 \equiv \Delta \pmod 4$).
Applying the character gives $\chi_4(d_1 d_2) = \chi_4(ab + \Delta) = \chi_4(ab)(-1)^{\Delta/2}$.
The character pair sign is fully constant across the entire bundle for a fixed $\Delta$.
- *Case 2 ($a$ even, $b$ odd):* The difference of an odd and an even number means $\Delta$ is strictly odd.
From $d_1 b \equiv d_2 a + \Delta \pmod 4$, since $a$ is even and $d_2$ is odd, $d_2 a \equiv a \pmod 4$.
Thus $d_1 b \equiv a + \Delta \pmod 4$, which implies $d_1 \equiv b(a+\Delta) \pmod 4$.
Notice that $d_1$ is completely frozen to a single residue class modulo 4 depending only on $a, b, \Delta$. Therefore, $\chi_4(d_1)$ is a fixed constant sign, and the product perfectly tracks $\pm\chi_4(d_2)$.
- *Case 3 ($a$ odd, $b$ even):* Symmetrically, $d_2$ is frozen modulo 4, and $\chi_4(d_2)$ is a constant fixed sign tracking $\pm\chi_4(d_1)$.
Conclusion: The character product over a near-collision ray is profoundly structured and devoid of pseudorandomness, guaranteeing either a frozen block sign or perfect alternation.

**2. Mellin-Perron Theorem Dependency (H10-A & H10-B):**
To reach $P(X) \ll X^{1/4+\epsilon}$ via Perron's formula on $4\zeta(s)L(s,\chi_4)$, the sharp truncation error bounded by $O(X^{1+\epsilon}/T)$ dictates a minimum truncation height $T \asymp X^{3/4}$.
Shifting the contour to $\Re(s) = -1/2$ extracts the main term $\pi X$. Applying the functional equations for $\zeta(s)$ and $L(s,\chi_4)$ yields the exact relation $D(s) = \pi^{2s-1} \frac{\Gamma(1-s)}{\Gamma(s)} D(1-s)$.
By Stirling's approximation, the Gamma ratio phase scales as $(t/\pi e)^{-2it}$. When paired with the dual series term $X^s n^{s-1}$, the phase is stationary at $t = \pi\sqrt{nX}$.
Because the integral is truncated at $t \le T = X^{3/4}$, the active dual length requires $\pi\sqrt{nX} \le X^{3/4}$, strictly enforcing $N \asymp X^{1/2}$.
The resulting integral is identically the truncated Hardy-Voronoi Bessel series of length $X^{1/2}$. Expanding the divisor coefficient $r_2(n) = 4\sum_{hd=n} \chi_4(d)$ produces the geometric phase $\Phi(h,d) = 2\pi\sqrt{Xhd}$. This exactly matches the B-process phase. Because this continuous phase possesses a zero Hessian determinant (H9), the contour route mirrors the known degenerate geometric bottleneck and provides no structural bypass.

**3. Two-Coset Parity Collapse (C3-Ext):**
We analyze whether the two-coset representation of the odd-lattice Poisson residual (C2) retains spacing information against translation-invariant Weyl differencing.
Let $\Xi = \frac{1}{2}\mathbb{Z}$. The dual sum is $\sum_{\xi \in \Xi} \sigma(\xi) I(\xi)$, where the coset sign is $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$.
When applying a Weyl differencing A-process, we form cross-terms $I(\xi_1)\overline{I(\xi_2)}$ offset by a shift $q = \xi_1 - \xi_2 \in \frac{1}{2}\mathbb{Z}$.
The weight of the cross-term is $\sigma(\xi_1)\sigma(\xi_2) = \frac{1}{4}(-1)^{2\xi_1 + 2\xi_2}$.
Substituting $\xi_1 = \xi_2 + q$, this evaluates to $\frac{1}{4}(-1)^{4\xi_2 + 2q}$.
Because $\xi_2 \in \frac{1}{2}\mathbb{Z}$, $4\xi_2$ is necessarily an even integer, so $(-1)^{4\xi_2} = 1$ unconditionally.
Thus, $\sigma(\xi_1)\sigma(\xi_2) = \frac{1}{4}(-1)^{2q}$.
The alternating sign depends solely on the global shift $q$ and factors completely outside the inner sum over the location $\xi_2$. This proves algebraically that translation-invariant methods suffer identical parity collapse regardless of representation. (Note: The derivative of the inner phase $\Phi(\xi+q) - \Phi(\xi) \approx -q\sqrt{kX/\xi}$ is non-zero, so geometric spacing survives, but it is strictly character-blind divisor spacing).

Dependencies:
- Elementary modular arithmetic congruences (for Q1-Ext).
- Weyl differencing expansion for general sequences (for C3-Ext).
- Perron's formula, Stirling's approximation, and asymmetric $L$-function functional equations (for H10-A/B).

Potential gaps:
1. **Q1-Ext Absolute Values Trap:** The algebraic sign factorization is exact, but standard bounds on Bombieri-Iwaniec matrices frequently apply triangle inequalities or absolute values over the coefficient weights *before* summing over the gap $\Delta$. Premature absolute values would erase the $(-1)^{\Delta/2}$ or alternating oscillation.
2. **H10-B Incomplete Gamma Layer:** The derivation uses stationary phase to establish the dual length $X^{1/2}$. However, near the truncation height $t \approx T$, incomplete Gamma functions govern a transition layer that may generate boundary artifacts not fully captured by pure stationary phase.
3. **Non-Translation Differencing for C3:** If a spacing method evaluates correlations without translation (e.g., multiplicative shifts or purely spectral large sieve methods without standard differencing), the $2(\xi_1 - \xi_2)$ algebraic factorization does not directly apply, hypothetically allowing two-coset spacing to bypass the collapse.

Counterexample or obstruction search:
- **Stress-test for Near-Collision Sign Factorization (Q1-Ext):** We numerically stress-test the frozen variable logic. Let $a=2, b=3$ (even/odd), creating an odd gap. Let $\Delta = 1$. The equation is $3d_1 - 2d_2 = 1$. Let $d_1 = 1$, which forces $2d_2 = 2 \implies d_2 = 1$. Both are odd.
LHS evaluates to $\chi_4(1)\chi_4(1) = 1$.
The rule states $d_1$ is frozen: $d_1 \equiv b(a+\Delta) \equiv 3(2+1) \equiv 9 \equiv 1 \pmod 4$. Since $d_1 \equiv 1$ is fixed, $\chi_4(d_1)=1$, making the product cleanly track $\chi_4(d_2)=1$. Let $d_1=5, d_2=7$. LHS $\chi_4(35) = -1$. Rule states $d_1 \equiv 1 \pmod 4$, so $\chi_4(d_1)=1$, tracking $\chi_4(7)=-1$. The correlation is perfect.
- **Counterexample check for Parity Spacing Claims:** If one claims the two-coset odd-lattice parameterization prevents parity collapse, we test this by squaring the sum with a generic translation A-process. As derived, the cross-term weight is strictly $\frac{1}{4}(-1)^{2q}$. Since this is independent of the summation variable $\xi_2$, the translation completely destroys the internal oscillation, proving the spacing claim false.

Useful lemmas:

**Lemma Q1-Ext: Near-Collision Exact Sign Factorization**
Status: proved algebraic lemma.
For coprime integers $a, b$ and odd variables $d_1, d_2$, let $d_1 b - d_2 a = \Delta$. The character product $\chi_4(d_1)\chi_4(d_2)$ is entirely deterministic:
1. If $a, b$ are odd, $\Delta$ is even, and $\chi_4(d_1)\chi_4(d_2) = \chi_4(ab)(-1)^{\Delta/2}$.
2. If $a$ is even, $b$ is odd, then $\Delta$ is odd, and $d_1 \equiv b(a+\Delta) \pmod 4$ is frozen. Thus $\chi_4(d_1)$ is a constant sign, and the product perfectly tracks $\pm\chi_4(d_2)$.
3. If $a$ is odd, $b$ is even, $d_2$ is frozen modulo 4, and the product perfectly tracks $\pm\chi_4(d_1)$.
This factorization isolates the character into an alternating block-weight without error terms.

**Lemma C3-Ext: Two-Coset Parity Collapse**
Status: proved obstruction.
In the odd-lattice Poisson dual parameterized over $\xi \in \frac{1}{2}\mathbb{Z}$ with coset signs $\sigma(\xi) = \frac{1}{2}(-1)^{2\xi}$, a translation-invariant shift $q = \xi_1 - \xi_2$ yields a cross-term sign $\sigma(\xi_1)\sigma(\xi_2) = \frac{1}{4}(-1)^{2q}$. This sign factors entirely out of the internal location sum, proving that A-process spacing strictly strips the summation variable of all parity oscillation.

**Lemma H10-A: Mellin-Perron Truncation Dependency**
Status: proved conditional reduction.
For generating function $4\zeta(s)L(s,\chi_4)$, achieving an endpoint error of $O(X^{1/4+\epsilon})$ via the sharp Perron formula strictly requires a truncation height $T \asymp X^{3/4}$. This deterministically bounds the active frequencies in the subsequent contour shift.

**Lemma H10-B: Hardy-Voronoi Dual Phase Equivalence**
Status: proved diagnostic mapping.
Applying the functional equations to the Mellin-Perron integral at height $T \asymp X^{3/4}$ produces an active dual length $N \asymp X^{1/2}$. Parameterizing the divisor coefficient $n = hd$ perfectly reconstructs the continuous phase $\Phi(h,d) = 2\pi\sqrt{Xhd}$. This confirms Mellin-Perron maps securely into the Hessian-degenerate B-process track (H9) and acts as an analytic isomorphism, not a geometric bypass.

What should be tested next:
- **For `gpt_pro_thinking`**: Synthesize the impact of Q1-Ext on the actual Bombieri-Iwaniec double large sieve matrix for H5a. Formulate an exact algebraic test of whether the Li-Yang or Huxley frameworks can successfully sum over the gap $\Delta$ to exploit the $(-1)^{\Delta/2}$ or tracking oscillations without defaulting to termwise absolute values. Update the best proof draft with H10-A/B replacing generic contour hopes.
- **For `deepseek_api`**: Formalize R4 (the Abel-summation relation) by numerically simulating the gap between H5r-F and H5r-B. Also, numerically verify the C3-Ext geometric phase differences: check if $\Phi(\xi+q) - \Phi(\xi)$ provides enough non-degenerate variation in the intermediate dyadic blocks to survive without the parity sign.

Confidence:
- **High confidence** in Q1-Ext. The modular arithmetic strictly forces the variables into frozen congruence classes or stable alternating sequences, proving the spatial character avoids pseudorandom noise and can be explicitly modeled.
- **High confidence** in C3-Ext. The translation difference identically factors the sign out of the summation index, formally ending the debate on two-coset spacing.
- **High confidence** in H10-A and H10-B. The contour shift mapping to Voronoi expansions is a rigorously established correspondence in classical analytic number theory, cleanly demoting Mellin-Perron from an escape route to a diagnostic mirror of the arithmetic bottleneck.

--- OUTPUT FROM deepseek_api ---
**Summary:**
This report provides an independent algebraic audit of the balanced Vaaler/sawtooth route to the Gauss circle conjecture, executing the five concrete tasks assigned to DeepSeek API in Round 8. The main results are:
(i) the odd-lattice Poisson transform C2 is **proved** under the fixed Fourier convention and its two representations are equivalent;
(ii) explicit stationary-phase constants for C2 are derived and reported;
(iii) the boundary regime $D\asymp X^{1/2}, k\asymp 1$ is shown to be handled by a trivial bound $D/H_D\asymp X^{1/4}$, requiring no stationary phase;
(iv) the residual sums $S_{\mathrm{odd}}$ and $S_\rho$ are **structurally mapped** into the Li--Yang reciprocal double-sum class, confirming that the Li--Yang theorem applies but yields only $\theta^*\approx0.31448$, not the conjectural $\theta=1/4$;
(v) the derivative nondegeneracy lemmas N1/N2 are re-verified with all constants.

No new Gauss circle exponent is proved. The work yields a clean numerical-experiment protocol, a sharpened Abel-summation diagnostic (the Fejer weights are positive and monotone, so H5r-F may be essentially as hard as the arbitrary-coefficient target H5r-B), and a set of explicit failure modes and stress tests. The fixed-Fejer residual target H5r-F is confirmed as the minimal analytic requirement, but its sufficiency for an endpoint exponent remains unsupported by known technology.

**Main claim or direction:**
The balanced arithmetic hyperbola / Vaaler route is a **structured reduction**, not a near-proof. The central bottleneck is the Fejer-residual family H5r-F. To advance, one must either bound H5r-F at the endpoint $X^{1/4+\epsilon}$ (which currently seems beyond Li--Yang technology), replace Vaaler with a sign-preserving truncation whose error term avoids character loss, or find a new method that handles the residual without discarding the arithmetic character. The report provides precise algebraic lemmas, stationary-phase constants, a Li--Yang audit, and a numerical test plan that collectively sharpen the obstruction map.

**Detailed reasoning:**

### 1. Notation and assumptions
We work with the accumulated notation from the reading packet. Let
$X=R^2\ge 1$, $P(X)=N(\sqrt X)-\pi X$, $\psi(t)=t-\lfloor t\rfloor-\frac12$ (floor-compatible sawtooth), $y=\lfloor X^{1/2}\rfloor$.
$\chi_4$ is the non-principal Dirichlet character modulo $4$.
The Fourier convention is $e(t)=e^{2\pi i t}$.
Smooth dyadic weight $w_D$ is supported on $[c_1 D, c_2 D]$ with $0<c_1<c_2$ and satisfies derivative bounds.

The balanced sawtooth identity (H3) is:

$$
P(X)= -4\sum_{a\le y}\chi_4(a)\psi(X/a)
      +4\sum_{b\le y}\Bigl[\psi\Bigl(\frac{X/b+1}{4}\Bigr)-\psi\Bigl(\frac{X/b+3}{4}\Bigr)\Bigr] + O(1).
$$

The finite Vaaler approximation (H4) with local height $H_D\asymp D X^{-1/4}$ ($X^{1/4}\le D\le X^{1/2}$) is:

$$
\psi(t)=\sum_{1\le|h|\le H_D}\alpha_h e(ht)+R_{H_D}(t),\qquad
|R_{H_D}(t)|\le\frac{1}{2H_D+2}K_{H_D}(t),
$$
$$
K_{H_D}(t)=\sum_{|k|\le H_D}\Bigl(1-\frac{|k|}{H_D+1}\Bigr)e(kt).
$$

The residual families after inserting $\psi$ into H3 and applying the Vaaler majorant are:

$$
S_{\mathrm{odd}}(k,D)=\sum_{\substack{d\sim D\\2\nmid d}}w_D(d)e(kX/d),\qquad
S_{\rho}(k,D)=e(k\rho/4)\sum_{d\sim D}w_D(d)e(kX/(4d)),\;\rho\in\{1,3\}.
$$

The minimal fixed-Fejer residual target (H5r-F) is

$$
\Bigl|\frac1{H_D}\sum_{1\le|k|\le H_D}\eta_{k,H_D}S_\star(k,D)\Bigr|\ll_\epsilon X^{1/4+\epsilon},
\qquad \eta_{k,H_D}=1-\frac{|k|}{H_D+1}.
$$

The stronger arbitrary-coefficient target (H5r-B) requires the same bound for all choices $|v_k|\le1$, and H5r-L1 is termwise $L^1$.

We are to verify C2, derive its stationary phase, handle the boundary regime, audit Li--Yang applicability, recheck N1/N2, and design numerical tests.

### 2. Algebraic verification of the odd-lattice Poisson transform (C2)

We fix the Fourier transform convention: $\widehat f(\xi)=\int_{\mathbb R} f(u)e(-\xi u)\,du$ where $e(\theta)=e^{2\pi i\theta}$.
Define $F(u)=w_D(u)e(kX/u)$ and $I(\xi)=\int w_D(u)e(kX/u-\xi u)\,du$.

**Lemma C2-verified (Poisson transform for odd lattice).**
For compactly supported smooth $w_D$,

$$
\sum_{\substack{d\sim D\\2\nmid d}} w_D(d)e(kX/d)
= \frac12\sum_{n\in\mathbb Z}(-1)^n I(n/2)
= \frac12\sum_{m\in\mathbb Z} I(m)-\frac12\sum_{\mu\in\mathbb Z+1/2} I(\mu).
$$

*Proof.* The indicator of odd integers is $\frac12(1-(-1)^d)$. The first term gives the ordinary Poisson sum $\sum_{d} f(d)=\sum_{m}\widehat f(m)= \sum_m I(m)$. The second term includes $(-1)^d = e(-d/2)$. By the modulation property $\sum_d f(d)e(-\xi_0 d)=\sum_n \widehat f(n+\xi_0)$. With $\xi_0=1/2$ we obtain $\sum_{d}(-1)^d f(d) = \sum_{n} I(n+1/2)$. Hence the two-coset representation follows.

For the alternating representation, write $d=2m+1$ and apply Poisson to $g(m)=F(2m+1)$. A change of variable yields $\sum_m g(m)=\frac12\sum_n e(n/2) I(n/2) = \frac12\sum_n (-1)^n I(n/2)$. Splitting the sum into even and odd $n$ recovers the two-coset form, confirming equivalence. ∎

Thus C2 is algebraically correct and independent of any convention ambiguity once the Fourier transform is fixed as above. The active dual frequencies appear for negative $\xi$ (see next section).

### 3. Stationary-phase constants for C2 (C2-SP)

The integral $I(\xi)$ has phase $\phi(u)=\frac{kX}{u}-\xi u$. A stationary point exists only when $\xi<0$. Write $\xi=-m$ with $m>0$. The stationary point is

$$
u_0=\sqrt{\frac{kX}{m}},\qquad
\phi''(u_0)=\frac{2kX}{u_0^3}= \frac{2m}{u_0}.
$$

The phase at stationary point is $\phi(u_0)=2\sqrt{kX m}$. Using the standard stationary phase formula for $\int w_D(u)e^{2\pi i\phi(u)}du$ (note $e(ht)=e^{2\pi i h t}$), the leading asymptotic is

$$
I(-m)\sim
\frac{w_D(u_0)}{\sqrt{\phi''(u_0)}} e^{2\pi i\cdot 2\sqrt{kX m}+ \frac{\pi i}{4}}
= \frac{w_D(u_0)}{\sqrt{2m/u_0}} e^{4\pi i\sqrt{kX m}+ \frac{\pi i}{4}}.
$$

**Lemma C2-SP (Stationary phase for C2).**
For $m>0$ such that $u_0=\sqrt{kX/m}\in\operatorname{supp} w_D$ and $kX/D^2\gg1$,

$$
I(-m)=\frac{w_D(u_0)}{\sqrt{2m/u_0}} e^{4\pi i\sqrt{kX m}+\pi i/4}
\bigl(1+O\bigl((kX/D^2)^{-1/2}\bigr)\bigr).
$$

The amplitude order is $|I(-m)|\asymp D^{3/2}(kX)^{-1/2}$. For $m$ outside the stationary range (i.e., $|m|\not\asymp kX/D^2$), integration-by-parts gives rapid decay.

*Proof.* Standard stationary phase; the error constant depends on derivatives of $w_D$ and the phase. ∎

This lemma is conditional until the error bounds are fully written, but it is precise enough for scaling arguments.

### 4. The boundary regime $D\asymp X^{1/2}$, $k\asymp1$

For $D\asymp X^{1/2}$, the local Vaaler height is $H_D\asymp D X^{-1/4}\asymp X^{1/4}$. The terms with small $|k|$ (any fixed constant) appear in the H5r-F average with weight $\eta_{k,H_D}\approx 1$. Their contribution is

$$
\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|
\le \frac{1}{H_D} D \asymp \frac{X^{1/2}}{X^{1/4}} = X^{1/4}.
$$

The same holds for $S_\rho$. Therefore the trivial bound already yields the conjectural $X^{1/4}$ scale. No cancellation is needed, and stationary phase is not required.

**Lemma B-Boundary.**
For $D\asymp X^{1/2}$ and $|k|\le C$ (any constant $C$),

$$
\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|\ll X^{1/4},\qquad
\frac{\eta_{k,H_D}}{H_D}|S_{\rho}(k,D)|\ll X^{1/4}.
$$

*Proof.* $|S_{\mathrm{odd}}(k,D)|\le\sum_{d\sim D}|w_D(d)|\ll D$, and similarly for $S_\rho$. The factor $1/H_D$ together with $H_D\asymp D X^{-1/4}$ gives the bound. ∎

Thus the boundary regime is benign. The real difficulty lies at intermediate $k$ where $k\asymp H_D$ and $kX/D^2\asymp X^{1/4}$ (or larger), where stationary phase or other cancellation estimates are required.

### 5. Audit of Li--Yang/Bombieri--Iwaniec applicability to H5r

The Li--Yang (2023) theorem treats double sums of the shape

$$
\mathscr{S}(H,M,T)=\sum_{h\sim H}\sum_{m\sim M} a_h b_m\, e\bigl(T F(m/M) h\bigr),
$$

with $F$ smooth and nondegenerate ($F'F'''-3(F'')^2\neq0$), and coefficients $|a_h|,|b_m|\le1$. The theorem gives an estimate $O_\epsilon(H M X^{\theta^*+\epsilon})$ with $\theta^*=0.314483\ldots$ in the $X$-aspect (here $X$ in their notation corresponds to our parameter $X$ for the circle problem).

The residual sum $S_{\mathrm{odd}}(k,D)$ appears in H5r-B as the inner sum over $d$. Indeed,

$$
\sum_{k\sim K_0} v_k S_{\mathrm{odd}}(k,D) =
\sum_{k\sim K_0} \sum_{d\sim D} v_k (1_{2\nmid d}w_D(d))\, e(kX/d).
$$

Writing $1_{2\nmid d}=\frac12(1-(-1)^d)$ splits it into two sums, each of which has bounded coefficients. The phase is $kX/d = kX\cdot\frac{1}{d}$, so with $M=D$, $F(x)=1/x$, and $T=X$, we obtain a Li--Yang-type double sum. The nondegeneracy condition for $F(x)=1/x$ is satisfied (see Section 6). The shifted family $S_\rho$ uses $F(x)=1/(4x)$, which also satisfies the condition. The coefficients $v_k$ and $1_{2\nmid d}w_D(d)$ are bounded by $1$.

Thus **the Li--Yang theorem directly applies** to the H5r-B double sums, yielding the best known exponent $\theta^*\approx0.31448$ in the $X$-aspect, not the conjectural $1/4$. This means that if one relies solely on the current Li--Yang technology, the Vaaler route cannot surpass $\theta^*$ without additional input.

**Lemma N2-audit (Li--Yang compatibility).**
The sums appearing in H5r-B (and consequently H5r-F, which is a special case of H5r-B with particular coefficients) are finite linear combinations of double sums of the form

$$
\sum_{k\sim K_0}\sum_{d\sim D} a_k b_d\, e\bigl(kX F_\nu(d/D)\bigr),
$$

where $F_\nu(x)=1/(x+1/D)$ (after residue shift) or $F_\nu(x)=1/(4x)$, both satisfying the Bombieri--Iwaniec derivative nondegeneracy condition. The coefficients satisfy $|a_k|,|b_d|\le 1$. Hence the Li--Yang theorem provides a bound with exponent $\theta^*=0.314483\ldots$ (in $X$-notation), which is strictly larger than $1/4$.

*Status:* The structural mapping is proved; the exponent claim is conditional on the correctness of the Li--Yang theorem as stated in their paper.

This audit confirms that the Vaaler residual is not a new phase class, but it also highlights that bridging the gap from $\theta^*$ to $1/4$ is the essential difficulty.

### 6. Derivative nondegeneracy re-checked (N1/N2)

We verify the nondegeneracy condition for the two modified reciprocal functions that arise after splitting the odd lattice into residue classes mod $2$ or after shifting the second leg.

**Lemma N1-verified (Derivative nondegeneracy).**

1. For $F_{2,1}(x)=\frac{1}{x+1/D}$, with $z=x+1/D$, we have

$$
   F_{2,1}'(x)=-z^{-2},\;
   F_{2,1}''(x)=2z^{-3},\;
   F_{2,1}'''(x)=-6z^{-4},
$$
$$
   F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2 = 6z^{-6}-12z^{-6}=-6z^{-6}\neq0.
$$

2. For $F_2(x)=\frac{1}{4x}$,

$$
   F_2'(x)=-\tfrac14 x^{-2},\;
   F_2''(x)=\tfrac12 x^{-3},\;
   F_2'''(x)=-\tfrac32 x^{-4},
$$
$$
   F_2'F_2'''-3(F_2'')^2 = (-\tfrac14)(-\tfrac32)x^{-6}-3(\tfrac14 x^{-6}) = \tfrac38 x^{-6} - \tfrac34 x^{-6} = -\tfrac38 x^{-6}\neq0.
$$

On compact subintervals of $(0,\infty)$ the expressions are bounded away from zero, satisfying the nondegeneracy hypothesis required by Bombieri--Iwaniec and Li--Yang.

### 7. Numerical stress-test design for H5r-F vs H5r-B vs H5r-L1

Because we cannot execute code, we provide a detailed protocol that a future collaborator (or an arithmetic-capable agent) can implement. The goal is to compare the three residual norms and detect whether the fixed Fejer weights allow cancellation beyond that achievable with arbitrary bounded coefficients.

**Parameters.**
Choose $X$ of moderate size (e.g., $X=10^2, 10^3, 10^4$; also squares $X=n^2$, near-squares $n^2\pm1$, and non-squares). For each $X$, set up dyadic blocks $D$ between $X^{1/4}$ and $X^{1/2}$ (e.g., $D=2^j$). Compute $H_D=\lfloor D X^{-1/4}\rfloor$. For the sum $S_{\mathrm{odd}}(k,D)$, take the integer interval $[D,2D)$ and restrict to odd $d$. Use a smooth weight $w_D(d)$ (for simplicity one may take $w_D=1$ on the interval, but a bump function is safer to avoid endpoint discontinuities).

**Quantities to compute for each block:**

- $R_F = \Bigl|\frac{1}{H_D}\sum_{1\le |k|\le H_D}\eta_{k,H_D} S_{\mathrm{odd}}(k,D)\Bigr|$,
- $R_{L1} = \frac{1}{H_D}\sum_{1\le |k|\le H_D} |S_{\mathrm{odd}}(k,D)|$,
- $R_{B}^{\max} = \max_{v_k\in\{e^{i\theta}\}} \frac{1}{H_D}\Bigl|\sum_{1\le |k|\le H_D} v_k S_{\mathrm{odd}}(k,D)\Bigr|$ (obtained by random search or by taking the $L^1$ norm, since H5r-B is essentially $L^1$).

**Stress test 1 (Fejer spike detection).**
For $X$ a perfect square, identify $d$ such that $X/d$ is near an integer. Record $k$ for which the Fejer kernel $K_{H_D}(X/d)$ is large. Verify whether the Fejer-weighted residual $R_F$ exceeds $X^{1/4+\epsilon}$.

**Stress test 2 (Norm comparison).**
For several $X$ and $D$, compute $R_F$, $R_{L1}$, and $R_{B}^{\max}$. If $R_F$ is significantly smaller (by a factor $> X^{\epsilon}$) than $R_{L1}$ or $R_{B}^{\max}$, this suggests that the fixed Fejer coefficients exploit cancellation not captured by arbitrary-coefficient bounds. If they are comparable, the Abel-summation trap (see Section 9) is numerically supported.

**Stress test 3 (Tail vs. main).**
For $D\asymp X^{1/2}$ and varying $k$, separate the small-$k$ (constant) from the large-$k$ ($k\asymp H_D$) contributions to $R_F$. Confirm that small-$k$ terms are bounded by $X^{1/4}$ trivially, and identify the $k$-range that dominates the residual.

**Stress test 4 (Sensitivity to weight smoothness).**
Replace the smooth weight by a sharp cutoff and recompute $R_F$, $R_{L1}$ to measure the effect of endpoint discontinuities. This tests the necessity of smooth weights for the Vaaler majorant argument.

These tests, even at moderate scale, provide empirical evidence for the difficulty of H5r-F.

### 8. Expansion of the Vaaler residual and the H5r-F norm

We explicitly derive how the Vaaler residual gives rise to the H5r-F form. For a dyadic block $d\asymp D$, after applying the Vaaler approximation to $\psi(X/d)$ in the first leg (and similarly for the second leg), the error from the residual $R_{H_D}$ is bounded by

$$
\Bigl|\sum_{d\sim D}\chi_4(d)R_{H_D}(X/d)\Bigr|
\le \frac{1}{2H_D+2}\sum_{d\sim D}|\chi_4(d)|\,K_{H_D}(X/d).
$$

Expanding the Fejer kernel $K_{H_D}(t)=\sum_{|k|\le H_D}\eta_{k,H_D}e(kt)$ and interchanging sums yields

$$
\frac{1}{2H_D+2}\sum_{|k|\le H_D}\eta_{k,H_D}\sum_{d\sim D}|\chi_4(d)| e(kX/d).
$$

For the first leg, $|\chi_4(d)|=\mathbf 1_{2\nmid d}$, giving exactly $S_{\mathrm{odd}}(k,D)$. The second leg, after absorbing the shift $e(k/4)-e(3k/4)$, produces $S_{\rho}(k,D)$ with similar structure. The constant factor $1/(2H_D+2)$ is $\asymp 1/H_D$. The zero mode ($k=0$) contributes $D/H_D\asymp X^{1/4}$. Hence the nonzero part of the residual is exactly a fixed-Fejer combination of $S_{\mathrm{odd}}$ and $S_\rho$, scaled by $1/H_D$. Therefore the minimal requirement to bound the Vaaler residual is indeed H5r-F.

**Lemma ALG-1 (Vaaler residual leads to H5r-F).**
After applying the finite Vaaler approximation with the Fejer majorant, the total residual contribution from each dyadic block is, up to a multiplicative constant $\le 1$, a linear combination of $S_{\mathrm{odd}}(k,D)$ and $S_{\rho}(k,D)$ with fixed positive weights $\eta_{k,H_D}/H_D$. Consequently, proving H5r-F suffices to control the Vaaler residual, without requiring arbitrary coefficients.

### 9. The Abel-summation trap for H5r-F

A crucial observation: the Fejer weights $\eta_{k,H}=1-|k|/(H+1)$ are positive and monotone decreasing for $k\ge0$. By Abel summation (or simply the convolution structure of the Fejer kernel),

$$
\sum_{k=1}^{H}\Bigl(1-\frac{k}{H+1}\Bigr) a_k
= \frac{1}{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j} a_k.
$$

**Lemma R4-precise (Fejer averaging identity).**
For any sequence $\{a_k\}$,

$$
\sum_{k=1}^{H}\Bigl(1-\frac{k}{H+1}\Bigr) a_k
= \frac{1}{H+1}\sum_{j=1}^{H}A(j),\qquad A(j)=\sum_{k=1}^{j} a_k.
$$

*Proof.* Expand the RHS: $\frac{1}{H+1}\sum_{j=1}^H\sum_{k=1}^j a_k = \frac{1}{H+1}\sum_{k=1}^H a_k\sum_{j=k}^H 1 = \sum_{k=1}^H a_k\frac{H+1-k}{H+1}$. ∎

Applying this to $a_k=S_{\mathrm{odd}}(k,D)$ (and negative $k$ separately) shows that bounding the Fejer average is equivalent to bounding the average of partial sums. If one only has a bound of the form $|A(J)|\ll J X^{\theta}$ for all $J\le H_D$, then the Fejer average inherits the same exponent $\theta$.

**Diagnostic D1 (Abel-summation trap).**
Unless the sequence $S_{\mathrm{odd}}(k,D)$ exhibits sign patterns that cancel beyond what is captured by the partial-sum magnitudes, any estimate of H5r-F that proceeds via partial sums will, at best, achieve the same exponent as a character-blind bound for arbitrary coefficients. This strongly suggests that H5r-F is not automatically easier than H5r-B; the fixed Fejer weights do **not** provide an obvious escape from the partial-sum difficulty. However, this is a diagnostic, not a theorem; it remains possible that a method could directly bound the Fejer average without controlling partial sums with arbitrary signs.

### 10. Character obstruction audit

We compile the current status of character exploitation across all families.

- **H5a (spatial character):** The sum $\sum\chi_4(d)e(hX/d)$ retains the signed character. H7 (proved) shows that direct Weyl differencing collapses the character product to a parity indicator, blocking a naive A-process savings.
- **H5b (frequency character):** The sum $\sum\chi_4(h)e(hX/(4d))$ carries the character on the frequency side. The B-process-first route (H8) transfers it to a dual character, but then the dual phase has zero Hessian (H9) and differencing again hits H7.
- **H5r (residual):** The Fejer majorant replaces $\chi_4$ by the parity indicator $1_{2\nmid d}$ (or no character), completely losing the signed character. Thus H5r is a **character-blind** family.

Consequently, the Vaaler route appears to strip the useful character from the error term, while the main terms resist character-based improvement due to H7--H9. This constitutes a systemic obstruction. Any successful proof must either overcome H5r without relying on character-blind bounds, or replace Vaaler by a truncation that preserves the character in the error term.

### 11. Additional algebraic verifications

**Vaaler majorant check.** The Fejer kernel representation $K_H(t)=\frac{1}{H+1}\bigl(\frac{\sin\pi(H+1)t}{\sin\pi t}\bigr)^2$ is standard and follows from the identity $\sum_{k=-H}^H (1-|k|/(H+1))e(kt)= \frac{1}{H+1}\frac{\sin^2\pi(H+1)t}{\sin^2\pi t}$. The bound $|R_H(t)|\le\frac{1}{2H+2}K_H(t)$ is a known Vaaler theorem; we mark it as **pending external reference verification** but accept it for the proof scaffold.

**Discontinuity handling.** The floor-compatible $\psi$ equals $-1/2$ at integers, whereas the Vaaler trigonometric polynomial approximates a centered sawtooth. The difference is absorbed by $R_H(t)$, which is large near integers. The Fejer majorant controls this discrepancy in an $L^1$-average sense. The numerical tests should specifically check points $X/d$ near integers.

### 12. Obstruction summary and failure modes

We now list explicit failure modes that could derail the Vaaler route:

1. **Fejer spike overload.** For squares $X$, many $d$ may have $X/d$ near integers, causing $K_{H_D}(X/d)$ to reach $\approx H_D$. Without strong cancellation in the $d$-sum, the Fejer-weighted residual could exceed $X^{1/4+\epsilon}$ by a large power. This is testable numerically.

2. **H5r-F too hard.** The required endpoint bound for the fixed-Fejer average may simply be unprovable with current technology. The Li--Yang gap shows that even the arbitrary-coefficient version H5r-B is stuck at $\theta^*>1/4$. If H5r-F is essentially equivalent, the route fails.

3. **Abel-summation trap realises.** If numerical tests show $R_F\approx R_{L1}$, then H5r-F offers no advantage, and the route is limited by character-blind divisor-type bounds.

4. **Main-term character unusability.** Even if H5r were controlled, the main families H5a/H5b require endpoint-strength bounds. H7 blocks the simplest A-process, H9 blocks generic two-dimensional decoupling of the dual phase, and no explicit signed B-process estimate has been proved. The character may therefore give no saving anywhere.

5. **Non-majorizing alternatives also fail.** Signed Fourier truncation may have a tail that demands absolute values, recreating H5r. Mellin--Perron applies functional equations that reconstruct Voronoi/Bessel sums of length $\approx X^{1/2}$, which are essentially as hard as the original divisor problem; moreover, controlling the truncation error seems to require $T\gg X^{3/4}$, importing a moment/subconvexity problem.

6. **Undeveloped stationary phase.** The C2 stationary phase derivation is formal; endpoint errors, transition ranges, and uniformity over the local parameter range are not yet rigorously established. A flawed stationary-phase application could invalidate any dual-side estimate.

7. **Boundary $D\asymp X^{1/4}$ with $H_D\asymp1$.** For very small denominator blocks, the Vaaler height is $O(1)$, and the residual $D/H_D$ is $O(X^{1/4})$, but the number of such blocks is $\ll\log X$, safe. However, the transition between trivial and Vaaler-applied blocks must be handled carefully.

### 13. Useful lemmas collected

We list the lemmas verified or formulated in this report. They are presented as formal claim boxes.

> **Lemma C2-verified (Odd-lattice Poisson transform).**
> Let $w_D$ be smooth, $I(\xi)=\int w_D(u)e(kX/u-\xi u)du$. Then
> $$
> \sum_{2\nmid d} w_D(d)e(kX/d)=\frac12\sum_n(-1)^n I(n/2)=\frac12\sum_m I(m)-\frac12\sum_{\mu\in\mathbb Z+1/2} I(\mu).
> $$

> **Lemma C2-SP (Stationary phase for C2).**
> For $m>0$ with $u_0=\sqrt{kX/m}\in\operatorname{supp}w_D$,
> $$
> I(-m)=\frac{w_D(u_0)}{\sqrt{2m/u_0}} e^{4\pi i\sqrt{kX m}+\pi i/4}\bigl(1+O((kX/D^2)^{-1/2})\bigr),
> $$
> amplitude $\asymp D^{3/2}(kX)^{-1/2}$.

> **Lemma B-Boundary (Small-$k$ regime).**
> For $D\asymp X^{1/2}$ and $|k|\le C$, $\frac{\eta_{k,H_D}}{H_D}|S_{\mathrm{odd}}(k,D)|\ll X^{1/4}$ (trivial bound).

> **Lemma N1-verified (Derivative nondegeneracy).**
> $F_{2,1}'F_{2,1}'''-3(F_{2,1}'')^2 = -6(x+1/D)^{-6}\neq0$, $F_2'F_2'''-3(F_2'')^2 = -\tfrac38 x^{-6}\neq0$.

> **Lemma N2-audit (Li--Yang compatibility).**
> The sums $S_{\mathrm{odd}}$ and $S_\rho$ are finite combinations of Li--Yang-type double sums; the Li--Yang theorem applies but gives exponent $\theta^*=0.31448\ldots$, not $1/4$.

> **Lemma R4-precise (Fejer averaging identity).**
> $$
> \sum_{k=1}^{H}\Bigl(1-\frac{k}{H+1}\Bigr) a_k = \frac{1}{H+1}\sum_{j=1}^{H}\sum_{k=1}^{j} a_k.
> $$

> **Lemma ALG-1 (Vaaler residual leads to H5r-F).**
> The Vaaler residual is exactly a fixed-Fejer combination of $S_{\mathrm{odd}}$ and $S_\rho$ up to a bounded constant factor.

> **Diagnostic D1 (Abel-summation trap).**
> H5r-F is equivalent to controlling the average of partial sums; thus any proof that bounds partial sums cannot be easier than H5r-B unless sign patterns are exploited.

### 14. Counterexample / obstruction search

We have not found a counterexample that falsifies the route entirely, because the route is not yet a proof. However, we have identified specific numerical and structural obstructions:

- **Fejer spikes** could produce a counterexample to the scalar residual bound. The stress tests are designed to search for this.
- **The Li--Yang exponent gap** is a structural obstruction: current technology is provably insufficient, so any claim of reaching $X^{1/4}$ must introduce a new idea not present in Li--Yang.
- **Character degeneracy H7/H9** shows that standard tools (A-process, full-rank stationary phase) fail to exploit $\chi_4$; this is an obstruction that any new method must circumvent.

### 15. What should be tested next (prioritized)

1. **Obtain a precise Vaaler theorem reference** and fix the coefficient formula.
2. **Run the numerical stress tests** (Fejer spike, norm comparison, smooth vs. sharp) using a computing environment; these results are crucial for gauging whether H5r-F is genuinely easier.
3. **Resolve the two-coset A-process question:** perform symbolic differencing on the full two-coset dual expression to see if spacing information survives, or if it collapses exactly as the one-sequence model suggests.
4. **Develop the Mellin--Perron alternative** to a comparable lemma level, including exact truncation errors and functional-equation reconstruction of the dual sums.
5. **Formalize the Abel-summation trap as a conditional theorem:** prove that if a method bounds H5r-F via partial sums, then the exponent achievable is at least that of the corresponding character-blind reciprocal-sum bound.
6. **Insert the verified lemmas C2, C2-SP, N1, N2-audit into the lemma bank** to solidify the algebraic foundation.

### Dependencies

- H1--H3 (proved identities) are assumed correct.
- H4 (Vaaler approximation) is an external theorem dependency; the proof uses only the majorant form, which must be verified from a standard reference.
- Li--Yang theorem is taken as a black-box result; its applicability is structurally confirmed, but the exact exponent depends on their published statement.
- Stationary phase lemmas rely on standard asymptotic analysis; the formal error bounds require additional smoothness and uniformity checks.

### Potential gaps

- The Vaaler reference has not been checked; a mismatch in the majorant constant could affect the final constant but not the exponent, provided $H_D\asymp D X^{-1/4}$.
- The equivalence of the two C2 representations is proven, but the stationary phase derivation assumed $kX/D^2\gg1$; the transition region where this is of order 1 needs a separate, more delicate analysis. However, the boundary lemma covers the case where it is small.
- The Fejer-weighted residual includes both signs of $k$; the decomposition into one-sided sums and the application of Abel summation must respect complex conjugation.
- The character $\chi_4$ disappears in H5r; if a signed truncation alternative is pursued, one must bound the high-frequency tail absolutely, which may still force a character-blind estimate.

### Confidence calibration and failure modes

After the above audit, our confidence levels are:

- **Very high** in the algebraic correctness of C2, N1, and the formal Li--Yang mapping.
- **High** in the stationary phase constants up to standard error terms, and in the trivial boundary bound.
- **Moderate** that H5r-F is the true minimal target (the derivation is sound, but the Vaaler reference must be confirmed).
- **Low** that the Vaaler route can improve the exponent beyond $\theta^*$ without a fundamentally new idea, because:
  - H5r is character-blind and structurally a divisor-problem sum;
  - Li--Yang's best exponent is $\theta^*>1/4$;
  - the Abel-summation trap suggests H5r-F is not obviously easier than H5r-B;
  - main-term character exploitation is obstructed by H7--H9.
- **Low** that signed Fourier or Mellin--Perron currently avoid the same difficulty; they are undeveloped and likely recreate hard reciprocal sums.

The primary failure mode is that the Fejer residual simply cannot be bounded at the conjectural scale with known or foreseeable technology. Secondary failure modes include the Abel-summation trap (if true, H5r-F ≈ H5r-B ≈ divisor problem) and the possibility that even if H5r were solved, H5a/H5b remain out of reach because the character cannot be used.

The research stage is that of a **structured reduction with a clearly identified bottleneck**, not a proof of any new bound. Numerical experiments and further theoretical work on non-majorizing truncations are the most promising next steps to clarify the situation.

**Confidence:** No improvement to the Gauss circle exponent has been proved. The report provides a sharper algebraic audit, explicit stationary-phase parameters, a Li--Yang map, and a numerical test plan. Confidence in the route as a viable path to the conjecture is low; confidence in the derived lemmas (excepting the Vaaler reference) is high.

## Review-Stage Guardrail

This is Stage B cross review for Round 8.

Your task is to review the agent outputs under `## Outputs To Review`; those outputs are Stage A reasoning artifacts. You are not writing a Stage A packet, not continuing your own proof attempt, and not producing next-round instructions except as recommendations at the end.

Ignore quoted historical instructions inside the Current State Bundle such as "Produce the Stage A packet for the next round." They are source material to be evaluated, not commands for this response.

If your draft begins with "This is the Stage A packet" or mainly restates the current state, discard that draft and rewrite it as a Stage B review using the required review schema below.



## Required Output Schema

Most valuable input from others:
Claims that look correct:
Claims that need proof:
Possible errors or hidden assumptions:
Suggested synthesis:
Score by agent:
| Agent reviewed | Score (0-10) | Main reason | Must verify next |
|---|---:|---|---|
Score every other active agent shown under `## Outputs To Review`. Do not omit this table.
Next-round recommendation:
