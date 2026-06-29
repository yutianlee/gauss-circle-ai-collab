# Human Steering Note: Round 3 Stage A Audit

Use this note for Stage B review and judge synthesis.

Round 3 Stage A responses are archived and polished. A3 API reasoning completed automatically. A3's proposed diagnostic bundle was materialized and executed locally with:

```powershell
python .\computations\m9_regression\run.py
```

Local diagnostic outputs:

- `outputs/table_small.csv`
- `computations/m9_regression/precision.log`
- `computations/m9_regression/report.md`

Round-local archive copy for Stage D auto-publish:

- `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`
- `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`
- `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`
- `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`

Important audit conclusions:

- A1 is calibrated and should be accepted as proof infrastructure under the unresolved H4 source audit.
- A2's total exact `N=0` `O(D^2)` claim is not yet proved. The additive-energy estimate needs a theorem statement or proof.
- A2's proposed promotions for `M9-M2-N0-diagonal-core-bound` and `M9-near-collision-taxonomy` should be rejected unless a reviewer supplies the missing proof.
- A3/Codex diagnostics support raw-vs-paired formula normalization only. They are diagnostic, not theorem evidence.
- The finite diagnostic has nonzero `N0_unclass` mass (`0.0127084`), so do not declare the exact `N=0` taxonomy resolved.
- Keep `M9`, `M9-M2`, `M9-M2-N0-diagonal-core-bound`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, and `GC-target` open for now.
