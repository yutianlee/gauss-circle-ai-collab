# Round 162 conductor controls

- Campaign: `m9-m2-hard-top-t1-close-factor-bilinear-gate`
- Round: 162
- Starting graph:
  `8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422`
- Resulting graph:
  `700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358`
- Terminal label: `hard_top_t1_close_factor_bilinear_no_go`
- Allocation: 100% analytic, algebraic, and primary-source verification;
  0% numerical experimentation

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| literal_t1_coefficient_and_orientation | GREEN. The normalized close-factor scalar, cone orientation, profiles, floors, stars, endpoints, and zero extension are retained. |
| squarefree_coprime_even_d2_branch | GREEN. The exact squarefree/coprime projector gives the lcm scales (Q=[a^2,c]), (R=[b^2,c]); only the first variable is forced odd, so even (d_2) remains. |
| chi4_preserved_before_positive_norms | GREEN. Character Poisson transfers (chi_4) exactly to odd dual frequencies with the factor (i/2). |
| product_phase_rank_one_hessian | GREEN. The Hessian of (J\sqrt{xz}) has rank one and the radial direction is null. |
| one_variable_character_poisson_self_return | GREEN/scoped. The saddle, phase, profile, normalization, and bare transform involution are exact; this supplies no target saving. |
| two_variable_dual_hyperbola | GREEN on smooth interiors. The exact stationary product is (s\ell=XQR) with the rescaled cone retained. |
| dual_product_collar_width_and_mass | GREEN/scoped. The collar has width (QRJ/L), the per-pair scale is (L^{3/2}/(QR\sqrt J)), and the resulting positive capacity is (\sqrt{JL}). |
| mobius_opening_and_rescaled_support_cost | GREEN. Every Möbius coefficient, lcm scale, support change, and (Q,R) power is charged before a positive norm. |
| local_divisor_return | GREEN/scoped. Product grouping yields a near-square local (chi_4)-divisor window; completion to (r_2/4) adds an uncontrolled complement. |
| standard_differencing | NO SAVING. Even-step correlation is constant, so the tested differencing erases rather than exploits the character. |
| hard_cone_profiles_floors_endpoints | OPEN and quarantined. Hard-edge transforms may have only reciprocal-frequency tails and saddle-edge transitions. |
| source_theorem_literal_match | GREEN named-route audit. The exact hypotheses and restored powers of the tested sources give no uniform literal target-strength placement. |
| physical_coefficient_vs_diagnostic | GREEN. Positive collar capacity is neither a physical upper bound nor a physical lower bound. |
| remaining_few_point_and_downstream_scope | GREEN. No t=1 target, hard-TOP parent, M2, M1, endpoint, M9, bridge, or exponent is promoted. |

## 2. Accepted kernel and open interface

The accepted result is an exact character-preserving transformation and
power ledger, not the desired estimate. On smooth interiors it produces
the scaled product collar


\[
 |s\ell-XQR|\ll \frac{QRJ}{L},
 \qquad Q\ell\le Rs\le4Q\ell,
\]

whose termwise positive capacity is (\sqrt{JL}). The decay in (QR)
is repaid by the collar width. The first affirmative statement still
needed is a bound for the full signed Möbius-coupled near-square divisor
aggregate at an arbitrary real centre, before any positive norm and with
all hard-edge leakage included.

## 3. Independent reviews

- the statement-only rederivation independently recovered the literal
  coefficient, even-(d_2) branch, character sign, rank-one geometry,
  collar scale, missing power, and open-boundary qualification;
- the post-unmask review rejected the blanket hard-edge estimate and
  verified the repaired literal scope;
- the power/involution review verified both character transforms, saddle
  normalization, collar width, multiplicity, and physical-scope limits;
- the source/downstream review calibrated Bombieri--Iwaniec,
  Karatsuba--Robert--Wu, Robert--Sargos, DFI/DRZ, and Bettin--Chandee and
  licensed only the scoped parent evidence; and
- the terminal State Patch review verified exactly one creation, two open
  parent updates, twelve rejected inferences, and sixteen no-change nodes.

## 4. State mutation

The dry State Patch validator and all seam reviews passed before mutation.
The applied patch made:

- 1 obligation creation;
- 2 obligation updates;
- 12 rejected-inference records; and
- 16 downstream obligations recorded unchanged.

The graph validator passes after mutation. The proof draft was refreshed
only after the accepted graph changed.

## 5. Mechanical validation

- starting and resulting graph hashes: PASS;
- State Patch scope review, applied graph validation, and completed-campaign
  validation: PASS;
- seven structured JSON/YAML files: 7/7 parse;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- `git diff --check`: PASS, with line-ending conversion notices only;
- pre-controls campaign/kernel/strategy hygiene: PASS on 19 Markdown files,
  with 261 per-file-unique equation tags, 420 balanced bracket-display
  pairs, zero double-dollar tokens, and no strict UTF-8, BOM, C0/DEL,
  replacement, zero-width, directional, CR, final-newline,
  trailing-whitespace, duplicate-tag, or display-delimiter issue; and
- pre-controls preview generation: PASS on all 19 Markdown files.

- final campaign/kernel/strategy hygiene, including this record: PASS on
  20 Markdown files, with 261 per-file-unique equation tags, 421 balanced
  bracket-display pairs, zero double-dollar tokens, and no byte,
  whitespace, equation-tag, or display-delimiter issue; and
- final preview generation: PASS on all 20 Markdown files.

Final validation after all closure metadata repeats the graph, campaign,
seven-file structured-state, compile, six-unit-test, and diff checks.

## 6. Downstream decision

Close under `hard_top_t1_close_factor_bilinear_no_go`. Park the tested
positive collar, standard differencing, and named source routes. The
proposed Round-163 interface is the full signed near-square local divisor
aggregate with complementary-divisor involution and all leakage priced.
The strongest internally proved global exponent remains (1/3), and the
audited external benchmark remains (0.3144831759740614\ldots).
