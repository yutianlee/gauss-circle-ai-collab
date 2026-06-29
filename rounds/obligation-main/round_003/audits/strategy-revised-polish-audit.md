# Round 3 Strategy-Revised Polish And Audit

Sources:

- `handoff/obligation-main/round_003/human/strategy-revised1.md`
- `handoff/obligation-main/round_003/human/strategy-revised2.md`

Archived copies:

- `rounds/obligation-main/round_003/human/strategy-revised1.md`
- `rounds/obligation-main/round_003/human/strategy-revised2.md`

## Polish Actions

- Normalized copied web Markdown in both strategy files.
- Archived both files into the active Round 3 `human/` directory so the judge prompt can see them.
- Repaired obvious formatting artifacts in `strategy-revised1.md`:
  - restored the missing minus sign in the cleared numerator `N`;
  - repaired the `cases` line break for `C_h`;
  - repaired the substack line break in the near-collision theorem template.

## Audit Summary

`strategy-revised1.md` is broadly aligned with the current proof graph. It should be used as the serious strategic steering note.

`strategy-revised2.md` is a broad, speculative architecture/strategy proposal. It contains useful exploration themes, but it should not redirect the current proof workflow unless its ideas are converted into precise obligations, theorem statements, source audits, or executable diagnostics.

## Strategy-Revised1

### Accept As Main Steering

- Keep the balanced hyperbola/Vaaler/Fejer residual framework as the selected reduction.
- Stop spending primary effort on the reduction itself; treat `M9`, especially the fixed-coefficient `M9-M2` leg, as the bottleneck.
- Use the actual Vaaler coefficients and preserve the `chi_4(h)` sign in `M2`.
- Continue with the signed fourth-moment route for `M2`, centered on the corrected numerator

```text
N = h1 d2 d3 d4 - h2 d1 d3 d4 + h3 d1 d2 d4 - h4 d1 d2 d3.
```

- Prioritize exact `N=0` subfamilies before broad near-collision estimates: diagonal core, denominator-paired, semi-diagonal, sign-symmetric, and unclassified families.
- Keep computation diagnostic only, especially signed-vs-absolute fourth-moment bins and CRI ratios.

### Accept As Backup Only

- `M9-coupled`: a coupled `M1+M2` estimate is a plausible backup obligation because the exact balanced formula combines the two legs. It should be added only as `proposed` or `open`, not as a replacement for separate `M9`.
- Tailored Li--Yang/Bombieri--Iwaniec fixed-coefficient route: useful after source audit, not as a black-box theorem.
- B-process/Hardy-window route: useful exploratory route, but it must track dual length, stationary amplitude, boundary terms, and character retention.
- Mellin--Perron/L-function route: useful as conditional comparison, unlikely to be the next unconditional proof step.
- Poisson--Bessel/radial decoupling: calibration only unless a precise smoothed/unsmoothed bridge is supplied.

### Caveats

- The signed fourth-moment theorem target is a goal, not evidence:

```text
|S2(D;X)|^4 << X^(1+epsilon)
```

must not be recorded as progress until the exact and near-collision masses are proved.

- The `Delta`-method proposal is promising but currently underspecified. A future prompt must require modulus range, smooth detector, transformed sums, and the exact location where `chi_4(h)` survives.
- `M1` should not be ignored permanently. It can be deferred while `M2` is the bottleneck, but the conditional bridge still requires both legs unless a coupled target is proved.
- Li--Yang claims remain source-audit-required. The arXiv paper is relevant, but theorem hypotheses, ranges, weights, and absolute-value placement are not imported.

## Strategy-Revised2

### Useful Ideas

- Treat the AI workflow as a structural exploration system, not only a prose generator.
- Keep long-horizon exploratory tracks for:
  - decoupling/partition search;
  - optimized smoothing or mollifier families;
  - L-function/amplifier heuristics;
  - formal or executable verification of candidate inequalities.

### Downgrade For Current Workflow

- Do not pivot the active proof route to RL/NN decoupling, mollifier optimization, or amplifier search in Round 3.
- Do not treat claims like "will work", "dead end", or "immediately drop the exponent" as mathematical evidence.
- Do not add architecture-heavy tooling requirements such as Lean/Isabelle/RL agents to the current round unless a specific executable task is defined.
- Do not use "current world record" or historical claims as proof-state facts without source audit.

### Main Gaps

- No precise theorem statements.
- No dependency list.
- No parameter ranges.
- No executable diagnostics.
- No bridge from optimized smooth objects back to the hard unsmoothed circle problem.
- No proof-obligation patch schema.

## Recommended Judge Treatment

Use `strategy-revised1.md` to sharpen the next round:

- primary route: `M2` signed fourth moment and exact-resonance taxonomy;
- immediate A2 task: one narrow weighted denominator-paired or semi-diagonal proof;
- immediate A1 task: H4 source audit and near-collision lemma statement;
- immediate A3 task: diagnostic scaling and post-H4 kernel replacement.

Use `strategy-revised2.md` only for a low-priority exploration backlog:

- `M9-structural-exploration-backlog` may be created as `proposed` only if the judge wants to track these ideas.
- No endpoint, M9, or source-audit status should change because of `strategy-revised2.md`.

## Bottom Line

The two strategy revisions should not conflict. The project should stay on the current balanced hyperbola/Vaaler route, focus near-term work on `M9-M2` exact-resonance estimates, and reserve the broader AI-structural ideas for exploratory probes after they are made precise.
