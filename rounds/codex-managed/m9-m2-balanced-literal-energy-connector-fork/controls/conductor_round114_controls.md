# Conductor Round-114 controls

Campaign: `m9-m2-balanced-literal-energy-connector-fork`

| Control | Outcome |
|---|---|
| Literal packet recombination | Green. The complete internal gcd telescope is summed before the modulus and gives `Z_B=2i T_B^low` coefficientwise. |
| Gcd lifts | Green. Both lifts survive until the full product `hk=g^2uv`; the phase diagonal is `g^2uv=g'^2u'v'`. |
| Equal full product | Green. Fibre Cauchy and the divisor bound give `O(L^2X^epsilon)`. |
| Radial corridor | Green. `|h'k'-hk|<=U` has absolute mass `O(L^2(U+1)X^epsilon)`. |
| Determinant corridor | Green. Lattice-line counting gives `|hk'-h'k|<=Q` absolute mass `O(L^2(Q+1)X^epsilon)`. |
| Threshold interface | Green. `U=Q=L` makes the union target-safe at the exact `L^3` energy budget; no extra saving is claimed. |
| Literal ray identity | Green. Rationalization gives the exact `rho^2` tangent remainder for `rho=hk'-h'k`. |
| Double-invariant chart | Green as an identity, no gain. Fixed nonaxial `(Delta,rho)` has divisor multiplicity, but the invariant range retains `L^4` capacity. |
| Full-symbol mean-square connector | Green as an implication only. The old `h`-outer full-symbol mean square implies BAL after Cauchy and the high-gcd owner; the estimate itself remains open. |
| Mean-square scope | Repaired. The gcd-masked Gram is distinct from the old full-symbol node, and the old node cannot imply the independent TOP parent. |
| Character placement | Green. The direct energy retains `chi_4(h)chi_4(h')`; the old `h`-outer mean square intentionally erases the outer character, while the opposite Gram retains it. |
| Coefficient adversary | Green no-go. A phase-adapted bounded array has double-far energy `asymp L^4`, so coefficient-uniform transversality is false. |
| Owner scope | Green. High gcd, square, near square, transform error, and the `j=2` boundary occur once; no cross-block cancellation is used. |
| Linear/energy capacity | Green. `L^(3/2)` and `L^3` are never interchanged. |
| Downstream scope | Green. BAL, TOP, UNBAL, M9-M2, M9-M1, uniformity, M9, and the quarter theorem remain open. |

The bounded exact-arithmetic and finite-count diagnostics are archived in
`controls/conductor_round114_prechecks.md`; they are `diagnostic_only` and
were not used to certify the asymptotic counts.

Validation commands and outcomes:

```text
python -m unittest discover -s tests -p 'test_*.py'
......
Ran 6 tests
OK

python -m math_collab.campaigns validate --manifest state/active_campaign.yml --graph state/proof_obligations.yml
Campaign OK

python -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/state_patch.json --round-index 114 --judge-ref rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md
Patch OK

git diff --check
exit 0; line-ending conversion warnings only
```

Artifact hygiene is green: all fourteen campaign Markdown/JSON artifacts
decode as strict UTF-8; Markdown is LF-only; there are no forbidden control
bytes or trailing whitespace; all display-TeX delimiters balance; and each
of the three reports has all seven required sections.
