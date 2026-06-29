# Evaluation1: Strategy Revision Scores

This evaluation scores the three strategy revisions as proof strategies for the endpoint target

```text
P(X) <<_epsilon X^(1/4+epsilon),
```

not merely as brainstorming documents.

| File | Insight score | Feasibility score | Overall rank | Judgment |
|---|---:|---:|---:|---|
| `strategy-revised1.md` | 9.2 / 10 | 6.6 / 10 | 1 | Best current route: aligned with repo state, aimed at the real bottleneck, and actionable. |
| `strategy-revised4.md` | 8.4 / 10 | 5.8 / 10 | 2 | Strong risk audit and state-hygiene note; less concrete as a proof route. |
| `strategy-revised2.md` | 4.5 / 10 | 1.8 / 10 | 3 | Creative but too speculative; lacks theorem-level bridges to the current bottleneck. |

## 1. `strategy-revised1.md`: Best Chance

This is the strongest of the three. It correctly says the balanced hyperbola/Vaaler reduction is mature and that the real problem is the fixed-coefficient `M9` estimate, especially `M9-M2`. It also keeps the conditional bridge

```text
H1-H3 + H4 + R5-Full + M9
  => P(X) <<_epsilon X^(1/4+epsilon)
```

rather than claiming a proof.

Its main insight is to attack `M9-M2` by a signed fourth moment. This is the right instinct because `M9-M2` contains the frequency character

```text
C_h = e(h/4) - e(3h/4) = 2i chi_4(h)
```

on odd `h`, and standard weighted Cauchy in `h` destroys this character by replacing `C_h conjugate(C_h)` with `|C_h|^2`. The proposed fourth-moment expansion keeps the actual coefficients `beta_h = alpha_h C_h` and clears denominators to

```text
N = h1 d2 d3 d4 - h2 d1 d3 d4
  + h3 d1 d2 d4 - h4 d1 d2 d3.
```

That is exactly the object the recent judge packets have been converging toward.

The feasibility score is limited because the hard estimate is still missing. The file is honest about this: the algebraic fourth-moment identity is not an estimate, and exact diagonals, semi-diagonals, denominator-paired cases, truncation edges, and near-collisions still need to be separated and bounded.

Verdict: use this as the primary strategy. Its next task should be narrow: prove one fourth-moment subfamily, then write the first genuine Delta-method or shifted-convolution object for the near-collision band.

## 2. `strategy-revised4.md`: Strong Audit, Weaker Proof Route

This file is a good architecture audit. It correctly reconstructs the route

```text
P(X)
  -> symmetric hyperbola
  -> floor-compatible sawtooth
  -> finite Vaaler
  -> local dyadic chi_4-twisted reciprocal sums.
```

It also correctly states that after H1-H4 the difficulty is concentrated in `M9`, at the endpoint/self-dual scale `D <= X^(1/2)`.

Its best contribution is caution. It flags `R5-Full` as something that must be reconciled with the older Fejer-residual / divisor-problem-trap diagnosis, and it correctly says that the fourth-moment attack on `M9-M2` has a no-slack wall: diagonal terms are already at the conjectural fourth-moment size, so every off-diagonal and near-collision family must be controlled sharply.

It also gives good alternative-route hygiene. Incremental Li--Yang-style reproduction, mean-square/large-values, exact Voronoi--Bessel/Hardy, additive energy of `sqrt(n)`, and omega-side guardrails are all useful to track, but none should replace the active route without a theorem-level bridge.

The reason it ranks below `strategy-revised1.md` is that it is mainly a risk audit, not a proof plan. Its strongest recommendation is to keep `obligation-main` focused on M9-M2 and near-collision estimates, which is correct, but it gives less concrete next-step analytic content than revised1.

Verdict: keep this as the audit checklist. It should govern proof hygiene, state updates, and false-proof detection, while revised1 should drive the next mathematical attack.

## 3. `strategy-revised2.md`: Creative But Least Feasible

This file recommends pivoting from symbolic exponential-sum work toward AI-driven structural exploration: reinforcement learning for discrete `l^2` decoupling partitions, neural optimization of mollifiers/test functions, and symbolic regression for L-function amplifiers.

The ideas are not worthless. Nonstandard smoothing, decoupling partitions, and coefficient search may be useful exploratory tools. But the file does not connect those ideas to the repo's conditional bridge, H4/R5, or fixed-coefficient `M9` bottleneck. The concrete current target is not "find a better generic mollifier" or "search for amplifier coefficients"; it is to prove endpoint estimates for the exact Vaaler main sums with their actual coefficients and character placement.

The main weakness is overclaiming. No theorem-level bridge is supplied from those optimization objects back to

```text
M1(D;X), M2(D;X) <<_epsilon X^(1/4+epsilon).
```

Without such a bridge, this is a research-infrastructure pitch, not a viable proof strategy.

Verdict: archive as divergent ideation. It may inspire side experiments, but it should not steer the main proof effort.

## Final Recommendation

Use:

```text
strategy-revised1.md as the main route,
strategy-revised4.md as the audit / guardrail document,
strategy-revised2.md as speculative background only.
```

For the next round, allocate roughly 70% to the signed fourth-moment / near-collision program from `strategy-revised1.md`, 25% to the R5/M9 proof-audit and state hygiene from `strategy-revised4.md`, and 5% or less to `strategy-revised2.md`-style exploratory AI optimization.
