# Round-193 gcd-scaled orientation diagnostic output

- Role: bounded exact-integer falsification control
- Evidence level: `diagnostic_only`
- Engine: WolframScript 1.2.0.0
- Script:
  `controls/gcd_scaled_orientation_involution_diagnostic.wl`
- Script SHA-256:
  `0dbb94d86c08778d3390c9327a766f1057ee9b7f777ae1b51c41f1d925e244c2`
- Command: WolframScript `-file` on the named script
- Exit code: 0

## Parameters

The finite enumeration used odd

\[
 1\le\kappa\le9,\quad 1\le g\le15,\quad
 1\le U,v\le25,
\]

and (1\le S,w\le12), with (L_0=2000) and
(D_0=\lceil\sqrt{L_0}\rceil).  It retained the primitive gcd conditions,
positive determinant, squarefree and allocation-coprime endpoint products,
cofactor gcd one, and (r\equiv2\pmod4).

## Exact output

```text
round=193
status=diagnostic_only
enumerated_valid_tuples=13843
enumerated_close_tuples=2562
identity_failures=0
mask_truth_table_failures=0
limitations=no_asymptotic_count_no_literal_profile_no_BV_or_collar_proof_no_core_projection_no_density
```

## Pass rule and result

PASS required zero failures for preservation of both products, shift,
original gcd and cofactor gcd one, involution, opposing orientation,
oddness, character reversal, transformed primitive coordinates and
coprimalities.  On close tuples it also required the two derived
(S+w) and \(|\kappa(v-U)|\) bounds and invariance of both close
conditions.  The residual (1,0,0,1) truth table was checked under fixing
or complementing each selected-prime bit according to membership in (g).
All finite tests passed.

## Limitation

This control proves no asymptotic count, no literal profile or endpoint
regularity, no BV or collar estimate, no deletion stability, no masked
Round-192 core identity, no density, and no theorem.  It can falsify the
finite algebra only.
