# Round 118 conductor controls

Campaign: `m9-m2-unbalanced-prescribed-centre-wave-gate`

Starting graph SHA-256:
`d4e626708a04680cc97b043835466948204c6e123a1dc9fd569b50377349feeb`

## Mathematical control ledger

| Control | Outcome |
|---|---|
| Literal product and reciprocal forms | Passed. The accepted coefficientwise Poisson identity retains the real centre, \(q_L\), \(W\), \(\chi_4\), and the flat-smooth physical normalization. |
| Product-window count | Passed. Abel summation plus the real-centre layer cake gives \((D/L)X^\varepsilon\), including divisor multiplicity. |
| Character parity | Passed after the hostile clarification: use the exact identity for \(\chi_4\) on all integers, or parametrize \(r=2n+1\); do not zero-extend the smooth amplitude. |
| Sampled BV and curvature | Passed on frozen flat smooth cells. The \(k^{-1}\)-weighted amplitude has supremum plus variation \(O(K^{-1})\), and \(f''\asymp LD/X\). |
| Exponent ledger | Passed. The envelope exponent is \(\min(a,(1-a)/2)\), saves only for \(a>1/3\), and is strictly above \(1/4\) at every strict residual point. |
| Same-residue run | Passed only in the repaired actual-scale form. Split at \(D^3=C_0X\), not at a nonuniform moving exponent comparison. Both branches are target-safe. |
| Central kernel constant and ties | Passed after shrinking the unspecified core constant below half the mod-four lattice gap. Exact and tied product levels are divisor-bounded. |
| Odd-\(r\) stationary normalization | Passed on an interior cell. The root number is \(e(-1/8)\chi_4(\nu)\) and the coefficient scale is \(\sqrt F/M\). |
| Integer phase-one sector | Passed with scope repair. The \(O(\sqrt M X^\varepsilon)\) count applies to integer \(X=bA^2\) and the interior leading phase-one sector. |
| Square-sector Euler sum | Passed for a uniformly compact scaled \(C^1\) literal profile family. The signed count is \(O(\sqrt M)\); the unsigned \(O(\sqrt M\log(2L))\) statement is an upper bound. |
| Arbitrary real-centre coherence | Not claimed. Nonzero root-of-unity sectors, transitions, endpoints, remainders, and the nonsquare complement remain explicit survivors. |
| Countermodel complement | Failed as a lower-bound route. Every selected positive or coherent sector leaves a larger signed complement uncontrolled. |
| Source hypotheses | Passed as a no-import audit. No checked primary theorem matches the literal truncated coefficient, prescribed centre, pointwise norm, profiles, power saving, and endpoints simultaneously. |
| Downstream scope | Passed. No hard TOP, BAL, complete UNBAL, M9 parent, endpoint-uniformity, exponent, or quarter claim is promoted. |

## Mechanical validation

- `python -m math_collab.campaigns validate`: passed after all three tasks
  were marked complete.
- State Patch dry run with `python -m math_collab.validate_state_patch`:
  passed for two creates, three updates, and ten rejected shadows.
- `python -m unittest discover -s tests -v`: six of six tests passed.
- Three reports contain exactly the seven required numbered sections.
- Campaign artifact audit: 16 files were UTF-8 decodable and LF-only, with
  no C0 controls, replacement characters, or trailing whitespace.
- `git diff --check`: passed. The only output was the repository's existing
  Windows line-ending warning.
- Numerical allocation: zero. No numerical experiment is evidence for any
  promoted statement.

## Decision

The validation matrix is green for the flat-smooth envelope, the repaired
same-residue run obstruction, and the scoped integer-centre phase-one
control. The complete joint selector and all endpoint/downstream claims
remain open. The State Patch may be applied without changing any global
exponent.
