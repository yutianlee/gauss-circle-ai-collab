# Round 163 conductor controls

- Campaign: m9-m2-hard-top-t1-near-square-divisor-involution-gate
- Round: 163
- Starting graph:
  700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358
- Resulting graph:
  81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306
- Terminal label: strict_t1_prime_toggle_sector
- Allocation: 100% analytic and algebraic reasoning; 0% numerical
  experimentation

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| literal_squarefree_product_grouping | GREEN. The exact supported N-sum, odd character divisor, upper near-square interval, normalization, product phase, and zero extension are retained. |
| odd_divisor_and_even_N_branch | GREEN. The exchange uses odd primes and preserves the even-N complement branch without treating an even divisor as character-bearing. |
| canonical_pair_selection | GREEN. At most one pair is selected from N,L,kappa independently of the divisor allocation; no density or nonemptiness is inferred. |
| exact_XOR_involution | GREEN. The prime exchange is integral, fixed-point-free, multiplicity one, sign reversing, and preserves N, parity, squarefreeness, and coprimality. |
| common_smooth_cell_variation | GREEN. The close-prime displacement is O_kappa(sqrt L), and accepted ordinary profile derivatives give an O_kappa(L^(-1/2)) amplitude difference. |
| profile_window_and_endpoint_leakage | GREEN. Cone, dyadic, profile, endpoint, star, ceiling, and zero-extension crossings occupy O_kappa(L^(3/2)+L) lattice collars. |
| arbitrary_real_centre_phase | GREEN. The exchange fixes N, so e(J sqrt(N)) is unchanged for every real centre. |
| single_prime_toggle_domain | NO SAVING. Multiplicative width two and p at least 3 make the two physical legs disjoint. |
| averaged_toggle_family | NO SAVING. Normalized averaging returns each original incidence with its original sign. |
| general_matching_and_cycles | GREEN/scoped. A perfect exchange matching requires sign-count balance; cycles only rewrite profile gradients and unmatched terms. |
| complementary_divisor_orientation | GREEN/scoped. Odd and even complements enter excluded lower windows and provide no physical upper-window symmetry. |
| full_divisor_vs_truncated_window | GREEN/scoped. Full-divisor vanishing leaves an uncontrolled profiled complement. |
| physical_coefficient_vs_diagnostic | GREEN. Raw semiprime and multiprime counts do not prove physical weighted mass or density. |
| missing_L_half_power | GREEN only on the selected XOR incidence sector, which is O_kappa(L^(3/2)); the complete residual remains open. |
| downstream_scope | GREEN. No remaining few-point channel, hard-TOP parent, smooth M2 packet, M9-M2, M9-M1, endpoint, M9, bridge, target, or exponent is promoted. |

## 2. Accepted result and residual

The accepted kernel proves the complete canonical close-opposite-prime
exactly-one incidence sector at target strength.  It does not quantify
how many products admit a selected pair.  The literal first survivor is

\[
 \mathcal S_{L,1}^{\mathrm{rem}}
 =\mathcal S_{L,1}-\mathcal S_{L,1}^{\mathrm{cp}},
\]

containing no-pair products and all neither-prime and both-prime
incidences.

## 3. Independent review

- the statement-only derivation independently recovered the product
  grouping, toggle and complement geometry, and the need for a missing
  profile interface;
- the post-unmask review verified the repaired N,L,kappa selector and
  strict-sector identity;
- the profile/boundary/power review verified the ordinary derivative,
  lattice-collar count, and L^(3/2) ledger;
- the hostile audit classified single toggles, averaged families,
  general matchings, cycles, complements, and full-divisor completion;
- the graph review licensed exactly one child node and two inconclusive
  parent attachments; and
- the terminal State Patch audit verified the exact operation counts,
  fresh identifiers, evidence, dependency direction, and cycle safety.

## 4. State mutation

All seam entries were green and the dry validator returned Patch OK before
mutation.  The applied State Patch made:

- 1 obligation creation;
- 2 obligation updates;
- 0 rejected-claim corrections;
- 16 fresh rejected-inference records; and
- 19 explicit no-change decisions.

The graph validator passes after mutation.  The proof draft was refreshed
only after the authoritative graph changed.

## 5. Mechanical validation

- starting and resulting graph hashes: PASS;
- dry and applied State Patch validation: PASS;
- terminal State Patch scope review: PASS;
- completed-campaign validation: PASS;
- seven structured JSON/YAML files: 7/7 parse;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- git diff check: PASS, with line-ending conversion notices only;
- pre-controls campaign/kernel/strategy hygiene: PASS on 19 Markdown
  files, with 160 per-file-unique equation tags, 231 balanced
  bracket-display pairs, zero double-dollar tokens, and no strict UTF-8,
  BOM, C0/DEL, replacement, zero-width, directional, lone-CR,
  final-newline, trailing-whitespace, duplicate-tag, or display-delimiter
  issue; and
- pre-controls preview generation: PASS on all 19 Markdown files.

Final validation including this record repeats the graph, campaign,
seven-file structured-state, compile, six-unit-test, diff, byte,
whitespace, equation-tag, display, and Markdown-preview checks.

## 6. Downstream decision

Close under strict_t1_prime_toggle_sector.  The complete residual remains
the next proposed interface; no Round-164 task is launched in this
closure.  The strongest internally proved exponent remains 1/3 and the
audited external benchmark remains 0.3144831759740614...
