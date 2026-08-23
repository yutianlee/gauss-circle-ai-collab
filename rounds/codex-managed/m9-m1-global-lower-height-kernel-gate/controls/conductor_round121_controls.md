# Round 121 conductor controls

Campaign: `m9-m1-global-lower-height-kernel-gate`

Starting graph SHA-256:
`54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`

Resulting graph SHA-256:
`3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`

## Mathematical control ledger

| Control | Outcome |
|---|---|
| Literal lower reciprocal antecedent | Passed. The exact profiles, \(H_j\), \(H_j+1\), Vaaler factor, hard sample, stars, lower multiplier, both signs, and one external \(R\) remain attached. |
| Profile-first aggregation | Passed as finite reordering only; no cancellation is credited. |
| Bottom exclusion | Passed after repair. The cutoff is chosen relative to the certified fixed bottom constant \(C_b\). |
| Exact active one-count | Passed on joint support, including the one-sided hard sample. |
| Vaaler error BV | Passed using both \(|\Phi-1|\ll u^2\) and \(|\Phi'|\ll u\). |
| Coupled radial separation | Passed after repair. Uniform high derivatives give a weighted two-dimensional Wiener norm; bare \(C^1\) summability is rejected. |
| Frequency-first transfer | Passed. Each dyadic shell costs \(X^\varepsilon(L/H_j)^2(1+D_j/L)\), summable to \(O(RX^\varepsilon)\) per profile. |
| Full lower range | Passed as a reduction, including the sector above \(n=X^{2/5}\); no signed estimate is inferred. |
| Integer phase | Passed with absolute error \(O(R)\), changing only the phase and retaining real-\(X\) amplitudes. |
| Fourier interpolation | Passed with an explicit sample-exact \(J_{R,y}\), zero near zero and periodic. Its growing seminorms are recorded. |
| Fourier sign and zero index | Passed. The congruence is \(d\mid N+k\), and every positive \(d\) divides zero. |
| Two-sided discrepancy | Passed. The floor formula holds for all \(k\in\mathbb Z\), including zero crossings. |
| Abel shift and boundaries | Passed. The difference weight is \(\widehat J(k)-\widehat J(k+1)\); fixed-\(X\) Schwartz decay removes boundaries. |
| Mod-four pair | Passed as an exact zero-extended identity, including unmatched top/bottom partner cells. |
| Amplitude seam | Passed at \(O(\log^2X)\) for the full profiles and \(O(\log X)\) for the flat cone. |
| Integer-increment subpackage | Passed at \(O(R\log X)\), hence target-safe after \(X^\varepsilon\) absorption. |
| Resonance capacity | Passed as a no-go. Disjoint half-integer tubes have post-tube-modulus capacity \(\gg R^{3/2}\); no signed lower bound is claimed. |
| Unsigned/adversarial analogue | Correctly fails. Actual-amplitude or phase-adversarial absolute capacity is \(\gg R^2\); the desired theorem must use global character/phase correlation. |
| Historical return | Passed. The sharp discrepancy globalizes the Round-64/65 unmatched-crossing return; invertible completion is not counted as saving. |
| Downstream scope | Passed. Lower GAR, GAR, blockwise M1, all M2 parents, endpoint uniformity, M9, and all exponent improvements remain open. |

## Mechanical validation

- Three required reports: present.
- Campaign validation: passed with status complete.
- State Patch dry run and application: passed; two creates, six updates,
  nine rejected shadows, and six explicit no-change nodes.
- Patched graph validation: passed at the resulting hash above.
- Unit tests: six of six passed; `compileall` passed.
- Artifact audit: all 14 campaign files are UTF-8 decodable and LF-only,
  with no C0 controls, replacement characters, or trailing whitespace,
  after mechanical normalization of generated CRLF files and one copied
  control character.
- Numerical allocation: zero; no experiment is used as proof evidence.
- External-source allocation: zero new imports.

## Decision

Every mathematical and mechanical gate passes after the two stated
repairs. Round 121 is closed.
