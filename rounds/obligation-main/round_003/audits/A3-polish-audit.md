# A3 Round 3 Polish And Audit

Source: API response archived at `rounds/obligation-main/round_003/responses/A3-003.md`

Materialized diagnostic files:

- `computations/m9_regression/run.py`
- `outputs/table_small.csv`
- `computations/m9_regression/precision.log`
- `computations/m9_regression/report.md`

Round-local archival copy for Stage D auto-publish:

- `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`
- `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`
- `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`
- `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`

Run command:

```powershell
python .\computations\m9_regression\run.py
```

## Polish Notes

- Normalized smart punctuation in the A3 response and generated A3 review.
- A3 supplied an artifact bundle in the response body rather than actual files.
- Codex materialized a cleaned, standard-library implementation based on the A3 bundle and executed it locally.

## Polished Digest

A3 delivers the right type of contribution for `M9-regression-raw-vs-paired`: executable diagnostics, not theorem claims. The response and local materialization check the raw two-sided formulas against paired-real formulas, test complex-weight failure, enumerate a small fourth-moment bin, calculate a CRI ratio, and report a gradient-spacing diagnostic.

Local execution results:

| Test | Observed | Status |
|---|---:|---|
| `C_h` character factor | `3.001e-15` | PASS |
| beta evenness | `0.000e+00` | PASS |
| M1 raw vs paired, real weights | `7.412e-13` | PASS |
| M2 raw vs paired, real weights | `2.349e-12` | PASS |
| M2 raw vs paired, complex weights | `1.012e+00` | FAIL_EXPECTED |
| N=0 unclassified finite mass | `0.0127084` | WATCH |
| CRI ratio | `1.57915` | INFO |
| gradient minimum angle | `3.75855e-05` | INFO |

## Audit

### Strengths

- The response avoids claiming an endpoint theorem.
- It marks coefficient magnitudes as provisional pending H4.
- It supplies concrete code content and output schemas.
- The materialized run confirms the core algebraic regression: real-weight raw and paired formulas match, while complex-weight paired-real reduction fails as expected.
- The finite fourth-moment bin leaves a nonzero unclassified `N=0` mass, which supports the current decision to keep the taxonomy open.

### Caveats

1. The local diagnostic uses a provisional triangular Fejer kernel, not the final Vaaler kernel.

Magnitude-dependent rows are diagnostic only until `H4-source-audit` is complete.

2. The finite enumeration is small.

It is useful for catching formula mistakes and taxonomy holes. It does not prove an asymptotic `O(D^2)` bound.

3. The N=0 classification is still heuristic.

The nonzero `N0_unclass` row is a useful warning: exact taxonomy is not closed by diagonal, pair-swapped, and sign-symmetric bins alone.

4. A3's original response did not physically create files.

The executable evidence listed above is a Codex materialization of A3's proposed bundle. The judge should cite both A3's response and the round-local artifact files if accepting this as diagnostic evidence.

5. A3 review already exists, but Stage B is not complete.

The workflow is waiting for A1 and A2 reviews. Do not treat the round as ready for judge until both web review responses are saved.

## Recommended Use

For Stage B reviewers:

- Accept the raw-vs-paired regression as positive diagnostic evidence for `M9-regression-raw-vs-paired`.
- Keep the obligation status `proposed` or `diagnostic_only` until the final Vaaler kernel and larger parameter sweeps are added.
- Use the nonzero unclassified mass to challenge A2's claim that the exact `N=0` taxonomy is resolved.

## Bottom Line

A3 is the most useful computation-track response so far because it produced a runnable artifact plan, and Codex converted it into real files. The result supports algebraic normalization but does not close any analytic obligation.
