# Round 133 conductor controls

Campaign: gc-w7-16-bombieri-iwaniec-two-spacing-source-map

Starting graph SHA-256:
465093c00a388ff9e49583a8016e0e580f74beea4656b15884fdd9dc9247be5a.

## Mathematical and source seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| official source version | Audit the official current arXiv v2 record and local TeX, including the source sum, both phase conditions, parameter definitions, DLS direction, both spacings, and final \(S/H\) target. | Green. The local TeX SHA-256 is 6fe6f9c0de7aa5c9f19365cdc92ffd2de7a1355582aa986e61efd53854793de1. |
| source equation numbering | Distinguish Lemma condition (4.6), \(N\) definition (4.8), and purported substitution (4.9). | Green after correction. Earlier references to the false substitution as (4.8) were rejected. |
| source-condition algebra | Substitute \(N_A\) into (4.6) with all signs and log powers. | Green repair. Printed (4.9) differs by \(T^2/M^6\) after common-power comparison. Corrected (5.23) verifies original (4.6) directly on the final range. |
| external-theorem scope | Retain all Round-95 literal and restricted-range repairs and test whether the new seam breaks the final exponent. | Green narrowly. The exponent is unchanged; general Theorem 4.2 remains uncertified as printed. |
| single-wave phase | Insert \(h=a,m=b,H=L,M=D,T=c/\kappa_i,F=1/z\). | Green exactly after finite sign splitting and conjugation. |
| both \(F\)-conditions | Differentiate \(1/z\) and compute \(F'F'''-3(F'')^2\). | Green uniformly on \([1,2]\). |
| M1 quarter carrier | Split \(b=4u+r\), make the carrier constant, and use \(F_r(z)=1/(4z+r/M')\). | Green at \(O(1)\) cost. The proposed mandatory \(D/L\) BV charge is false. |
| M2 character carrier | Expand \(\chi_4(a)\) into two Fourier branches and shift \(F\) by a constant. | Green at \(O(1)\) cost, with derivatives unchanged. |
| source parameter ledger | Recompute \(N_A,R,Q,L_{\rm sp},K_{\rm sp},\eta,Q_2\), including logarithms. | Green. Critical powers are \(67/300,83/600,[83/600,1/6],u-11/100,u-4/75,-17/150\). |
| repaired small-cap range | Test the printed condition and the missing \(\beta_2\ge0\) supplement. | Green for optimized \(q\), with margin \(17(6-q)/1200\). |
| \(q=4\) endpoint | Check the blind endpoint estimate against the source's separate \(G_4\) argument. | Green through \(G_4\); literal substitution into the \(q>4\) expression is rejected. |
| moving wedge | Keep the one-sided identity \(a'=(a/b)b'-n/b\) and recompute \(H_0,M_0,D/M_0\). | Green geometry: powers \(3/48,19/48,5/48\). Short support alone is not a source violation; moving nonseparability remains. |
| project ray versus approximant | Compare construction, ratio, and denominator scale. | Green no-conflation: project rays are original \((h,m)\); source derivative approximants are later variables of different size. |
| first-spacing vector | Compare the introduction, exact \(G_q\) norm, and Section-4 sketch. | Source seam retained: the former use \(l\), the latter prints \(k\). No project use is licensed before upstream audit. |
| second spacing | Retain both modular-inverse coordinates and both real coordinates. | Green source transcription, red project identification. The project determinant implies none of all four conditions. |
| joint coefficient and owners | Seek an exact source-compatible projective decomposition through physical and source owners. | Red for applicability. Primitive lifts, profiles, taper, wedge, aliases, stars, cells, signs, and owners remain joint. |
| absolute-value direction | Compare the signed scalar with the source arcwise sum of moduli and positive spacing quantities. | No-go. There is no reverse signed operator inequality. |
| two-wave black-box capacity | Grant zero connector cost and apply two normalized optimized source bounds. | Green diagnostic: \(2\Phi(-1/3)=(29+5\sqrt{170})/150=30.1414\ldots/48>27/48\). This is not a universal DLS no-go. |
| direct determinant collapse | Test \(h=n,m=bb'\) against source coefficients and Case A. | Red. The product fibre is not a source interval and \(M\asymp T,H\asymp T^{9/16}\) violates the large-\(M\) lower condition. |
| aligned packets | Retain the actual M1/M2 character and set \(b'=b\) at an aligned centre. | Green hostile control only. One-window \(30/48\) and complete \(35/48\) are upper capacities, not lower bounds. |
| downstream scope | Compare graph dependencies and capacity targets. | Green. The complete block, M9 parents, internal and external exponent values, bridge, and quarter target do not improve. |

## Post-unmask corrections

1. The false substituted source condition is equation (4.9), not (4.8).
2. The M1 denominator carrier costs \(O(1)\) progression pieces, not
   \(D/L\) in BV.
3. Short interval support is legal for a fixed BV cutoff; the moving wedge
   and absent projective norm are the actual coefficient seams.
4. The discovery first-coordinate power table is conditional on the later
   \(k\)-first sketch; the exact source norm is \(l\)-first.
5. The exponent \(2\Phi(-1/3)\) obstructs only a factor-first use of two
   independent source black boxes, not every possible joint BI argument.
6. The blind \(q=4\) estimate uses the separate endpoint theorem.
7. All aligned-packet quantities are upper-capacity controls only.

## Validation record

- State Patch validated and applied cleanly: 2 creates, 5 updates,
  16 rejections, and 7 explicit no-change records.
- Resulting graph SHA-256:
  40e83c20e83d542e43aa739931f4b89ea76f4541506fb44ef219ce31dca35024.
- Current graph: green under structural and evidence-path validation.
- Completed campaign manifest: green.
- Unit tests: six of six passed.
- Source compilation: math_collab and tests green.
- JSON parsing: active campaign, round ledger, validation matrix, and State
  Patch green.
- Artifact hygiene: 17 campaign files are valid UTF-8 with no replacement
  characters, embedded C0 controls, conflict markers, or trailing whitespace.
- Diff check: green, with line-ending warnings only.

No numerical experiment was used. The round was 100% source,
analytical, and algebraic.
