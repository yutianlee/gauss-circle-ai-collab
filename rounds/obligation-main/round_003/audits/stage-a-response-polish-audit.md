# Round 3 Stage A Response Polish And Audit

Run: `obligation-main`

Round: `round_003`

## Intake Status

Archived Stage A responses:

- `rounds/obligation-main/round_003/responses/A1-003.md`
- `rounds/obligation-main/round_003/responses/A2-003.md`
- `rounds/obligation-main/round_003/responses/A3-003.md`

Generated review prompts:

- `rounds/obligation-main/round_003/prompts/A1_review_3.md`
- `rounds/obligation-main/round_003/prompts/A2_review_3.md`
- `rounds/obligation-main/round_003/prompts/A3_review_3.md`

Current barrier:

- A3 API review has been generated at `rounds/obligation-main/round_003/reviews/A3.md`.
- A1 and A2 review handoff files are placeholders. Stage B is waiting for the human-saved web reviews.

## Polish Actions

- Normalized A1, A2, and A3 response Markdown.
- Repaired A1 mojibake in the proposed patch reason.
- Repaired A1 archived evidence paths.
- Materialized and executed A3's diagnostic bundle:
  - `computations/m9_regression/run.py`
  - `outputs/table_small.csv`
  - `computations/m9_regression/precision.log`
  - `computations/m9_regression/report.md`
- Mirrored the executable diagnostic bundle into the Round 3 archive for Stage D auto-publish:
  - `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`
  - `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`

## Agent Audit Summary

| Agent | Main value | Main risk | State treatment |
|---|---|---|---|
| A1 | Calibrated beta algebra, raw/paired formulas, fourth-moment numerator, open N0 lemma statement | Still depends on H4 source audit | Accept as proof infrastructure; no endpoint promotion |
| A2 | Useful exact-resonance and bilinear-route ideas | Overclaims total `N=0` closure and direct route proof | Reject proposed promotions unless reviewers supply missing proofs |
| A3 | Executable diagnostic plan, now materialized and run locally | Provisional kernel and small finite tests | Accept as diagnostic evidence only |

## Key Mathematical Takeaways

1. A1 and A3 agree on the core algebra:

```text
C_h = e(h/4) - e(3h/4) = 2i chi_4(h) 1_{2 notmid h}
beta_{-h,H} = beta_{h,H}
```

conditional on H4.

2. The corrected fourth-moment numerator remains:

```text
N = h1 d2 d3 d4 - h2 d1 d3 d4 + h3 d1 d2 d4 - h4 d1 d2 d3.
```

3. A2's claimed `O(D^2)` bound for all exact `N=0` mass is not yet graph-safe. The additive-energy estimate it relies on needs a theorem statement or proof.

4. The local A3 diagnostic supports the raw-vs-paired regression:

```text
M1 real raw-vs-paired diff: 7.412e-13
M2 real raw-vs-paired diff: 2.349e-12
M2 complex paired mismatch: 1.012e+00
N0 unclassified finite mass: 0.0127084
```

5. The nonzero unclassified finite mass is a useful warning against declaring the exact `N=0` taxonomy resolved.

## Review Instructions

Stage B reviewers should:

- Compare A2's `O(D^2)` additive-energy claim against A1's open obligation statement and A3/Codex's finite unclassified mass warning.
- Treat A2's Gallagher derivative penalty as a warning about one extraction route, not a theorem that blocks every fourth-moment strategy.
- Treat A2's direct signed bilinear route as proposed, pending exact exponent-pair/stationary-phase estimates.
- Accept A3's local files only as diagnostic evidence for formula normalization and regression behavior.
- Keep `M9`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open unless a review supplies a complete missing proof.

## Bottom Line

Round 3 Stage A improved the workflow evidence: A1 is calibrated, A2 is idea-rich but overpromoted, and A3 now has actual executable diagnostics. The analytic bottleneck is still open.
