# Round 3 Stage B Review Polish And Audit

Sources:

- `rounds/obligation-main/round_003/reviews/A1.md`
- `rounds/obligation-main/round_003/reviews/A2.md`
- `rounds/obligation-main/round_003/reviews/A3.md`

## Polish Actions

- Normalized A1 and A2 web review Markdown.
- Removed ChatGPT web citation markers from A1.
- Archived A1 and A2 reviews through the orchestrator.
- Converted one Unicode arrow in A3's archived review to ASCII.
- Regenerated `rounds/obligation-main/round_003/prompts/judge_3.md`; the round is now waiting for judge synthesis.

## Polished Digest

The three Stage B reviews converge on a conservative synthesis:

1. A1's coefficient algebra and fourth-moment setup are the strongest graph-safe content.

Accepted under H4 dependency:

```text
C_h = e(h/4) - e(3h/4) = 2i chi_4(h) 1_{2 notmid h}
beta_{h,H} = - Phi(|h|/(H+1)) chi_4(|h|) 1_{2 notmid h} / (pi |h|)
```

The corrected fourth-moment numerator remains:

```text
N = h1 d2 d3 d4 - h2 d1 d3 d4 + h3 d1 d2 d4 - h4 d1 d2 d3.
```

2. A2's Stage A promotions must be rejected.

All reviewers reject or downgrade:

- `M9-M2-N0-diagonal-core-bound -> proved_internal`;
- `M9-near-collision-taxonomy -> derived_under_assumptions`;
- any state implication that `M9`, `M9-M2`, or `GC-target` advanced analytically;
- A2's direct exponent-pair/Poisson route as proved or derived.

3. A3's computation is now real diagnostic evidence, not theorem evidence.

The executable diagnostic bundle exists and has been run locally:

- `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`
- `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`
- `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`
- `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`

It supports `M9-regression-raw-vs-paired` only at `diagnostic_only` evidence level. It does not prove M9, M2, a taxonomy, or an endpoint estimate.

4. The exact `N=0` taxonomy remains open.

The finite diagnostic has nonzero `N0_unclass` mass (`0.0127084`). This does not prove an asymptotic obstruction, but it does warn that the diagonal, pair-swapped, and sign-symmetric bins are not a complete working taxonomy by themselves.

5. The denominator-paired family is now the key next subproblem.

A2's review contributes a useful unweighted count heuristic/derivation for denominator-paired exact resonances:

```text
unweighted count ~ D^4 X^(-3/4) log D,
endpoint D = X^(1/2): ~ X^(5/4) log X.
```

Treat this as a strong stress-test claim that the judge should scrutinize. It is not yet a graph-safe theorem unless the judge verifies the counting conventions, lower/upper bounds, and edge cases. Its safe use is: trivial unweighted counting is not enough; the next proof task must use the reciprocal `beta_h` weights, exact signs, or a sharper weighted energy theorem.

## Reviewer Audit

### A1 Review

A1 is the best calibrated review. It:

- accepts A2's useful algebraic objects and route ideas;
- rejects A2's proof promotions;
- flags the missing additive-energy theorem;
- catches the suspect endpoint Poisson dual-length claim (`hX/D^2`, not generally length 1 at the endpoint);
- accepts A3 artifacts only as diagnostic evidence;
- gives clear next tasks for A2 and A3.

Use A1's review as the main state-mutation guide.

### A2 Review

A2's review is much better calibrated than A2's Stage A response. It now keeps the full diagonal-core bound open and emphasizes weighted mass estimates for denominator-paired and semi-diagonal families.

Useful content:

- denominator-paired gcd threshold analysis;
- reminder that unweighted counts may exceed the target;
- complex-weight generalized cosine formula proposal;
- next-round focus on weighted denominator-paired and semi-diagonal bounds.

Caveats:

- The denominator-paired unweighted count is presented too conclusively. The judge should verify it before adding it as a formal obstruction.
- The phrase that A3's finite diagnostic "proves" taxonomy incompleteness should be read narrowly: it proves the current finite classifier finds non-diagonal exact examples, not an asymptotic taxonomy theorem.
- The generalized complex-weight cosine formula is a useful implementation note, but any proof use must specify whether the analytic weights are real or complex.

### A3 Review

A3 is conservative and useful. It:

- independently rejects A2's additive-energy shortcut;
- rejects A2's `[PROVED]` labels;
- keeps the fourth-moment route primary but narrows it to small-step exact-resonance proofs;
- recommends an open direct-exponential-sum route only if it receives a precise statement.

Small caveat: A3 says A3 "must produce" committed computation artifacts, but in the current local round those artifacts now exist under the round archive. The judge should cite the round-local artifact paths rather than treating A3 as still prose-only.

## Judge Instructions

### Accept Or Record

- Accept A1's `C_h`, `beta_h`, raw two-sided M2 formula, real-weight paired formula, and corrected `N` as H4-dependent algebraic infrastructure.
- Accept A3/Codex artifacts as positive diagnostic evidence for `M9-regression-raw-vs-paired`.
- Consider moving `M9-regression-raw-vs-paired` from `proposed` to `diagnostic_only`, or keep it `proposed` while attaching the artifact files as positive evidence. Do not move it to a proof status.
- Record A2's denominator-paired unweighted count as a stress-test or open subclaim only if the judge verifies the derivation.

### Reject Or Keep Open

- Keep `M9`, `M9-M1`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, and `GC-target` open.
- Keep `H4-source-audit` and `Li-Yang-source-audit` unresolved.
- Reject A2's total exact `N=0` closure.
- Reject A2's direct exponent-pair/Poisson route as proved or derived.
- Reject route-closing language about Gallagher derivative loss or fourth-moment failure.

### Next Round Tasks

- A1: complete or materially advance `H4-source-audit`; formulate the exact near-collision spacing lemma with all weight, coefficient, and threshold hypotheses.
- A2: prove one narrow weighted exact-resonance lemma, preferably denominator-paired, with all gcd cases and reciprocal `beta_h` weights.
- A3: update diagnostics after H4; add the complex-weight generalized cosine regression only as a formula diagnostic; scale exact `N=0` and near-collision tables while preserving `diagnostic_only`.

## Score Calibration

Suggested split scores for judge prose:

| Agent | Idea quality | State evidence | Calibration | Main reason |
|---|---:|---:|---:|---|
| A1 | 9 | 8 | 9 | Clean algebra, strong state judgment, good next tasks. |
| A2 | 7 | 3 | 6 | Better calibrated review and useful denominator-paired stress test, but new count needs verification. |
| A3 | 8 | 7 | 9 | Conservative review plus local diagnostic artifacts; still diagnostic only. |

The formal State Patch `mathematical_progress_score` should remain conservative: Round 3 improves algebraic confidence and diagnostic evidence, but it does not prove an analytic M9 estimate.

## Bottom Line

Stage B is ready for judge synthesis. The judge should credit Round 3 for clearer exact-resonance targeting and real diagnostic artifacts, while keeping all endpoint and M2 analytic obligations open.
