# Round 120 conductor controls

Campaign: `m9-m1-gar-radial-interface-reconciliation`

Starting graph SHA-256:
`daa3c03b4b08ab062fa78724813fd2beff02ad92df8bf25d32407b1ce7f91177`

Resulting graph SHA-256:
`54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`

## Mathematical control ledger

| Control | Outcome |
|---|---|
| Literal global coefficient | Passed. The exact (hq=n), odd (q), (chi_4(q)), profile sum, (H_j+1), floors, internal stars, hard sample, outer half tie, and both signs remain attached. |
| Terminal frequency BV | Passed. The sampled weight (vartheta(h/H_j)Phi(h/(H_j+1))/h) has sup-plus-variation (O(H_j^{-1})), including both zero-extension jumps. |
| Active floors | Passed. (H_j=0) scales are empty; on every atom (D_j/(2R)le H_jle D_j/R). |
| Terminal antecedent | Passed. The accepted frequency-first theorem gives (O(RX^epsilon)) after the logarithmic scale sum. |
| Positive transform and normalization | Passed. The coefficientwise smooth/hard transforms give exactly one external (R), the Gaussian unit (e(1/8)/i), and the literal terminal coefficient. |
| Hard boundary and errors | Passed. The full hard sample is retained, the cotangent boundary has (O(1)) terminal mass, and absolute transform errors total (O(log^2 X)). |
| Both frequency signs | Passed. The positive identity proves complex modulus; real coefficients make the negative sign its exact conjugate. |
| Profile support | Passed after repair. The certified closed interval is ([1/2,3/2]), not a smaller fixed interval. |
| Terminal geometry | Passed. The terminal coefficient equals the original above (s_0) and vanishes below (s_0/144), with all floors and stars literal. |
| Localized terminal transfer | Passed after repair. A fixed auxiliary multiplier compact inside ((0,16)) is inserted at the reciprocal antecedent before Mellin separation. |
| Whole nonlower complement | Passed. Full terminal minus lower-weighted terminal equals ((1-V_low)C_X^*) coefficientwise. |
| Old interface owner | Passed after owner repair. The whole nonlower complement minus the already proved compact critical cells is exactly the Round-98 interface. |
| Endpoint prefix | Passed as a nonidentification. Its constant phase differs from the varying radial-collar phase. |
| Endpoint and R1 ownership | Passed. These are alternative-route modules with multiplicity zero here, not hard-transform errors. |
| Physical versus finite height | Passed. No arbitrary finite Perron/Mellin-height endpoint theorem, (C upward 16) limit, or moving seminorm is used. |
| Lower parent | Passed as a disjointness gate. The exact lower-radial signed aggregate is untouched and becomes the sole GAR analytic parent. |
| Downstream scope | Passed. GAR, both blockwise M1 parents, all three M2 parents, endpoint uniformity, M9, every improved exponent, and the quarter target remain open. |

## Mechanical validation

- Campaign validation: passed with all three reports present.
- State Patch dry run and application: passed; one create, six updates,
  eight rejected shadows, and five explicit no-change nodes.
- Patched graph validation: passed at the resulting hash above.
- Unit tests: six of six passed; `compileall` passed.
- Campaign artifact audit: all 14 files are UTF-8 decodable and LF-only,
  with no C0 controls, replacement characters, or trailing whitespace,
  after mechanical normalization of five generated CRLF files.
- `git diff --check`: passed apart from repository line-ending warnings.
- Numerical allocation: zero. No numerical experiment is used as evidence.
- External-source allocation: zero new imports.

## Decision

The terminal-height whole-nonlower theorem and the exact sharp
radial/interface consequence pass every mathematical and mechanical gate.
Round 120 is closed.
