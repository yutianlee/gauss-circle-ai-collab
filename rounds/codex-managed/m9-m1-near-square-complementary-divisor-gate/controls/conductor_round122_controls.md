# Round 122 conductor controls

Campaign: `m9-m1-near-square-complementary-divisor-gate`

Starting graph SHA-256:
`3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`

Resulting graph SHA-256:
`d29ae6c0f398cc2df699b15ee2901b525290263b6cde5eecece49cdeee095bb1`

## Mathematical control ledger

| Control | Outcome |
|---|---|
| Exact Round-121 antecedent | Passed. The proof starts from the accepted all-integer floor discrepancy and one-sided sample-exact wavelet. |
| Uniform wavelet envelope | Passed. The (1/y) lower transition and (1/R) radial transition are disjoint and separately priced; the middle (1/|k|) range remains. |
| Far Fourier tail | Passed. With (K_\delta=yX^\delta), explicit derivative norms give (O_{A,\delta}(RX^{-A})). |
| Positive retained window | Passed. (K_\delta=o(X)), so every integer in every retained oriented interval is positive. |
| Central Fourier window | Passed in modulus at (O_\varepsilon(RX^\varepsilon)). |
| Centering seam | Passed. The exact identity (sum kW(k)=J(0)=0) and the uniform high-order tail control its localized leakage. |
| High two-adic projection | Passed. The projection applies to every cumulative increment, and (2^{A_0}\geq R=y/R+O(R^{-1})) makes its total target-safe. |
| Low/high/core overlap | Passed. The exact identities (122.C15a) and (122.C29a)--(122.C29b) count the central window, centering, high valuation, and half-central correction once. |
| Character-preserving complement | Passed. For (m=2^an), the complement is (d\leftrightarrow n/d), and every odd residue class is retained. |
| Strict and hard boundaries | Passed. The tail uses (q<n/y); the inclusive (d=y) sample and its excluded equality partner occur once. |
| Square fixed points | Passed. The equality (n=y^2) contributes (chi_4(y)) once; all other square ties have the correct one-count. |
| Even thresholds | Passed. For (a\geq1), (n<y^2) and the threshold is (y/2^a+O(X^\delta/2^a)), so no false near-square band is asserted. |
| Odd central factor pairs | Passed. The ordered occurrence map is injective into a box of side (O(1+X^\delta)), and its cumulative wavelet cost is target-safe for (delta<1/8). |
| Exact smallest survivor | Passed. The piecewise increment (\mathscr V_\delta) removes only proved packages and retains every unresolved full/complement branch. |
| Full coefficient and complement one-count | Passed as an identity and rejected as a gain. Recombination restores the original (d\leq y) cone. |
| Circle noncircularity | Passed. No estimate for the remaining (r_2/4) wave is imported. |
| Self-return scope | Passed. The negative-character identity is an algebraic mechanism obstruction, not a signed lower bound. |
| Downstream scope | Passed. Lower GAR, GAR, both direct M1 parents, all M2 parents, endpoint uniformity, M9, and every exponent improvement remain open. |

## Mechanical validation

- Three required reports and all three second-stage audits: present.
- Campaign validation: passed with status complete.
- State Patch dry run and application: passed; two creates, six updates,
  ten rejected shadows, and six explicit no-change nodes.
- Patched graph validation: passed at the resulting hash above.
- Unit tests: six of six passed; `compileall` passed.
- Structured state files: JSON parsing passed for the campaign, State
  Patch, round ledger, and validation matrix.
- Artifact audit: all 14 campaign files are UTF-8 decodable and LF-only,
  with no C0 controls, replacement characters, or trailing whitespace,
  after mechanical normalization of generated files.
- `git diff --check`: no whitespace error; only repository line-ending
  conversion warnings were emitted.
- Numerical allocation: zero; no experiment is used as proof evidence.
- External-source allocation: zero new imports.

## Decision

Every mathematical and mechanical gate passes after the displayed
centering, projection-overlap, central-cumulative, and exact-survivor
repairs.  Round 122 is closed.
