# Round 119 conductor controls

Campaign: `m9-m1-direct-parent-minimax-gate`

Starting graph SHA-256:
`c3498daad3bdceb7c69c0e47a616e03ebfa12ccaf42f8df42958aa227f50fd91`

## Mathematical control ledger

| Control | Outcome |
|---|---|
| Literal M1 block | Passed. The actual Vaaler taper, (1/h), (chi_4(d)), denominator profile, signs, floors, stars, support crossings, and real (X) remain attached. |
| Owner priority | Passed. Bottom and R5 are disjoint earlier owners; terminal, the isolated second-derivative point, and TTY are removed before lifting the residual. |
| Exact residual | Passed. Both critical families have limiting slack (1/6<1/4) and (2546/3>463), and neither is ((1/2,0)). |
| Hard/smooth split | Passed. Only (j=0) contains (lfloor\sqrt X\rfloor); (j=1) remains smooth despite exponent (1/2+o(1)). |
| Frequency shell existence | Passed. Since (H_j/X^{1/6}\asymp X^{1/12}), both (j=0,1) have full nonterminal (L\asymp X^{1/6}) shells. |
| Frequency-first row | Passed. It has capacity (X^{1/3+o(1)}) on both witnesses. |
| Full second-derivative row | Passed. The leading term is (X^{1/3+o(1)}), the companion is (X^{1/6+o(1)}), and the companion inequality holds on the whole active triangle. |
| TTY row | Passed. Its critical exponent is (770/1923=1/3+43/641), so it fits but does not shrink either witness. |
| Hard physical normalization | Passed after statement-only repair. Normalized (L^2) becomes physical (X^{1/4}L^{1/2}) under the factor (X^{1/4}L^{-3/2}); it is not a physical (2\ell) row. |
| Menu versus lower bound | Passed. Every (X^{1/3}) statement is explicitly about the minimum of available upper-bound formulas, never an arithmetic lower bound. |
| Adjacent-profile connector | Passed as a no-go. The exact telescope retains height differences and both boundary owners; the original scale atoms have no alternating profile sign. |
| Canonical scope | Passed. No block-local inverse exists from the open post-global Gram to either direct parent. |
| GAR scope | Passed. GAR owns only total active M1 through a separate bridge and does not imply blockwise M9-M1 or M9. |
| Downstream scope | Passed. Both direct parents, both GAR parents, M9-M1, M9-M2, endpoint uniformity, M9, every improved exponent, and the quarter target remain open. |

## Mechanical validation

- `python -m math_collab.campaigns validate`: passed with all three tasks
  completed and all reports present.
- State Patch dry run with `python -m math_collab.validate_state_patch`:
  passed for two creates, five updates, and ten rejected shadows.
- State Patch application: passed; the resulting graph hash is
  `daa3c03b4b08ab062fa78724813fd2beff02ad92df8bf25d32407b1ce7f91177`.
- `python -m unittest discover -s tests -v`: six of six tests passed.
- `python -m compileall -q math_collab tests`: passed.
- The three reports each contain exactly the seven required numbered
  sections.
- Campaign artifact audit: 15 files are UTF-8 decodable and LF-only, with
  no C0 controls, replacement characters, or trailing whitespace.
- `git diff --check`: passed. Its only output was the repository's existing
  Windows line-ending warning.
- Numerical allocation: zero. No numerical experiment is used as evidence.
- External-source allocation: zero new imports. TTY is used only through
  its already accepted, source-audited fixed-profile node.

## Decision

The validation matrix is green for the separate-parent menu frontier and
the scoped adjacent-profile connector no-go. The State Patch was applied
without changing an analytic parent or any global exponent.
