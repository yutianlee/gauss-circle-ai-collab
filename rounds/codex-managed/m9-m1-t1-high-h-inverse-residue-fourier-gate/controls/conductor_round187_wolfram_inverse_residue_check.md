# Conductor Round-187 Wolfram inverse-residue check

- Campaign: `m9-m1-t1-high-h-inverse-residue-fourier-gate`
- Round: 187
- Role: bounded finite diagnostic; not theorem evidence
- Starting graph SHA-256:
  `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`
- Script:
  `controls/inverse_residue_exact_check.wls`
- Runtime: WolframScript on Windows
- Allocation: a bounded normalization test within the campaign's 10%
  experimental ceiling

## Purpose and pass rule

For every odd \(3\le U\le31\), the script evaluated the following finite
identities at 100-digit working precision:

\[
 \widehat E_U(k)=\frac{2}{1+e(-k/U)},\qquad
 E_U(a)=\frac1U\sum_{k\bmod U}\widehat E_U(k)e(ka/U),
\]

the coefficient normalization
\(c_U(k)=\widehat E_U(k)/U\), the residue mean
\(\sum_{a\bmod U}E_U(a)=1\), the unit-residue orientation identity
\(E_U(a)+E_U(-a)=0\), and every divisor alias fold

\[
 \sum_{j=0}^{U/U_0-1}c_U(\ell+jU_0)=c_{U_0}(\ell)
 \qquad(U_0\mid U).
\]

The diagnostic passed only if every numerical residual was below
\(10^{-60}\) and every exact integer mean was one.

## Command and outcome

The conductor ran:

```powershell
& 'C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe' -file 'rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/controls/inverse_residue_exact_check.wls'
```

Output ended with `allPass=True`. Across all tested moduli, the displayed
Fourier, coefficient, inversion, and alias-fold residuals were numerical
zeros with at least 96 decimal digits of precision; every residue mean was
exactly one and every orientation error was exactly zero. Exit code was
zero.

## Interpretation and limitation

This check detects sign, normalization, inversion, orientation, and alias
fold mistakes in the finite formulas used to design the campaign. It does
not prove those identities for arbitrary \(U\), does not test the literal
M1 endpoint coefficient, and supplies no asymptotic cancellation or
factor-\(Y\) estimate. Every promoted statement still requires an
algebraic proof and independent seam review.
