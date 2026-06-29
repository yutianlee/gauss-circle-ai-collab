# Human Steering Note: Round 3 Stage B Review Audit

Use this note when writing the Round 3 judge synthesis.

## Consensus

- Accept A1's M2 algebraic normalization under H4:
  - `C_h = 2i chi_4(h) 1_{2 notmid h}`;
  - real-even `beta_h`;
  - raw two-sided M2 formula;
  - paired formula only under its stated weight hypotheses;
  - corrected fourth-moment numerator `N`.
- Accept A3/Codex artifacts only as `diagnostic_only` evidence:
  - `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`
- Reject A2's Stage A promotions:
  - no `proved_internal` status for `M9-M2-N0-diagonal-core-bound`;
  - no resolved status for `M9-near-collision-taxonomy`;
  - no proved or derived status for the direct exponent-pair/Poisson route.

## Important Caution

A2's Stage B review gives a useful denominator-paired unweighted count stress test:

```text
unweighted denominator-paired count ~ D^4 X^(-3/4) log D,
at D = X^(1/2): ~ X^(5/4) log X.
```

Treat this as a promising stress-test claim, not as final graph evidence unless the judge verifies the counting argument. Its safe conclusion is that trivial unweighted counting is insufficient and the next proof must use actual reciprocal `beta_h` weights, signs, or a weighted energy theorem.

## Recommended State Treatment

- Keep open: `M9`, `M9-M1`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `M9-endpoint-uniformity`, and `GC-target`.
- Keep source-audit-required: `H4-source-audit`, `Li-Yang-source-audit`.
- `M9-regression-raw-vs-paired`: may become `diagnostic_only`, or remain `proposed` with the Round 3 artifact files attached as positive diagnostic evidence. Do not promote it to theorem evidence.

## Next Round

- A1: H4 source audit and precise near-collision lemma statement.
- A2: one narrow weighted denominator-paired proof, with all gcd cases and reciprocal beta weights.
- A3: post-H4 diagnostic rerun, larger exact `N=0` and near-collision tables, and optional complex-weight generalized cosine regression.
