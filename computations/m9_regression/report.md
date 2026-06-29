# M9 Regression: Raw-vs-Paired Diagnostic Report

**Status**: `diagnostic_only`
**Run command**: `python computations/m9_regression/run.py`
**Kernel**: provisional triangular Fejer placeholder pending `H4-source-audit`.

## Results

| Test | Observed | Status |
|---|---:|---|
| T0a C_h character factor | 3.001e-15 | PASS |
| T0b beta evenness | 0.000e+00 | PASS |
| T1 M1 raw vs paired (real) | 7.412e-13 | PASS |
| T2 M2 raw vs paired (real) | 2.349e-12 | PASS |
| T3 M2 raw vs paired (complex) | 1.012e+00 | FAIL_EXPECTED |
| T4a 4th moment N=0 diagonal mass | 0.0397446 | INFO |
| T4b 4th moment N=0 pair-swapped mass | 0.0282277 | INFO |
| T4c 4th moment N=0 sign-symmetric mass | 0.0167109 | INFO |
| T4d 4th moment N=0 unclassified mass | 0.0127084 | WATCH |
| T4e 4th moment near-collision mass | 0 | INFO |
| T4f 4th moment far mass | 2.12363 | INFO |
| T5 CRI ratio | 1.57915 | INFO |
| T6a gradient minimum angle | 3.75855e-05 | INFO |
| T6b gradient mean angle | 0.0130038 | INFO |

## Interpretation

- The real-weight raw and paired formulas agree within tolerance for both M1 and M2.
- The complex-weight paired-real M2 check mismatches, as expected, so paired formulas must stay scoped to real weights.
- Fourth-moment bin masses are small finite diagnostics only; they do not prove an asymptotic bound.
- Any nonzero `N0_unclass` mass remains a taxonomy warning, not a theorem.

## Files

- `outputs/table_small.csv`
- `computations/m9_regression/precision.log`
- `computations/m9_regression/report.md`
