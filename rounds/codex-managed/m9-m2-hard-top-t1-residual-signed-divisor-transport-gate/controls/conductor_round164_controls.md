# Round 164 conductor controls

- Campaign: m9-m2-hard-top-t1-residual-signed-divisor-transport-gate
- Round: 164
- Starting graph:
  81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306
- Resulting graph:
  141bbc8c998981245e33f18c9c116ef12f309ecfc54898e3a1dbd4569e0f7ba0
- Terminal label: hard_top_t1_residual_transport_no_go
- Allocation: 100% analytic and algebraic reasoning; 0% numerical or
  symbolic experimentation

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| residual_exact_subtraction | GREEN.  The residual indicator is \((1,0,0,1)\) on selected-prime bits and exactly complements XOR. |
| odd_divisor_and_even_N_branch | GREEN.  The character-bearing factors remain odd and the factor \(2\) remains on the complementary leg. |
| sign_mass_and_unmatched_atoms | GREEN.  Selected mass is zero; no-pair mass is the exact Euler product and includes the all-positive branch. |
| ordered_divisor_abel_identity | GREEN.  The discrete identity and midpoint BV bound are exact with unequal mass. |
| regulated_endpoint_convention | GREEN after repair.  The full-line Stieltjes form has no duplicate terminal term and preserves isolated point values. |
| profile_jump_and_zero_extension_variation | GREEN.  The actual fixed profiles and finitely many hard faces give \(V_N\ll1\). |
| weighted_vs_unweighted_BV | GREEN after repair.  The literal target is weighted by \(V_N\); the unweighted sum is only the coefficient-uniform envelope. |
| semiprime_multiprime_capacity | GREEN/scoped.  Odd and even four-prime controls give \(L^2/(\log L)^4\) unit-profile capacity for every selector status. |
| prime_distribution_source | GREEN.  Bennett et al. is used only for fixed \(q=4\), reduced residues, fixed relative boxes, and large endpoints. |
| physical_coefficient_vs_diagnostic | GREEN.  The prime count is not a literal profile plateau or oscillatory lower bound. |
| outer_N_phase_preservation | GREEN.  The square-root phase remains in the aggregate short-shift correlation. |
| Fejer_window_identity | GREEN.  Pair multiplicity is \(R-r\), with exact \(2\Re\) and \(1-r/R\). |
| Fejer_endpoint_constant | GREEN.  Exactly at most \(M_L+R-1\) windows meet the zero-extended support. |
| missing_L_half_power | GREEN reduction, OPEN theorem.  \(M_L\asymp L^2\), \(R\asymp L\), and diagonal \(L^2\) give the target square if the aggregate off-diagonal is \(O(L^2)\). |
| additive_product_shift | GREEN reduction.  Opening supported rows gives \(d'm'-dm=r\) with multiplicity one. |
| additive_vs_multiplicative_geometry | GREEN after repair.  The short shift and rank-one character-Poisson collar are independent routes with only a power-warning comparison. |
| arbitrary_real_centre_phase | GREEN.  No exact phase opposition or unproved modulo-one spacing is assumed. |
| current_literature | GREEN/scoped.  No listed source supplies the open theorem; the five-repair Li--Yang narrow source status is retained. |
| downstream_scope | GREEN.  No residual target, full \(t=1\), parent, smooth packet, M9 component, bridge, quarter theorem, or exponent is promoted. |

## 2. Independent review and repairs

- The statement-only derivation independently reproduced the exact
  residual, sign-mass, Abel, BV, Fejer, endpoint, power, and product-shift
  algebra.
- Its post-unmask review required a full-line Stieltjes convention,
  \(M_L\asymp L^2\), one-sided inequality notation, and explicit
  supported-row selector scope.  All four were repaired and independently
  reverified.
- The transport/profile/power/source review required the weighted literal
  BV target, separation of additive and multiplicative geometries,
  shell-length precision, and five-repair Li--Yang/JNT wording.  All four
  were repaired and independently reverified.
- The graph review licensed exactly one reduction child, two inconclusive
  parent attachments, twenty-three rejected overclaims, twenty explicit
  no-change decisions, and no downstream mutation.
- Byte-hygiene rechecks removed all malformed control characters from the
  statement-only artifacts and verified the accepted kernel.

## 3. Accepted result and open theorem

The accepted kernel is
proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md.
It proves the exact algebra and the endpoint-safe reduction, but not the
residual target.  The first open theorem is the one-sided aggregate
actual-direction length-\(L\) short-shift bound displayed in the kernel.
No absolute value around an individual shift, divisor opening, selector
branch, or parity branch belongs to that theorem.

## 4. State mutation

Every required seam was green after repair and the dry validator returned
Patch OK before mutation.  The applied State Patch made:

- 1 obligation creation;
- 2 obligation updates;
- 0 rejected-claim corrections;
- 23 fresh rejected-inference records; and
- 20 explicit no-change decisions.

Both updated hard-TOP parents remain open and receive only a dependency,
inconclusive evidence, and a scoped next action.  The proof draft was
refreshed only after the authoritative graph changed.

## 5. Mechanical validation

- starting graph hash: PASS;
- dry and applied State Patch validation: PASS;
- resulting graph validation: PASS;
- completed-campaign validation: PASS;
- seven structured JSON/YAML files: 7/7 parse;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- git diff check: PASS, with line-ending conversion notices only;
- pre-controls campaign/kernel/strategy/source hygiene: PASS on 22
  Markdown files, with 213 per-file-unique equation tags, 287 balanced
  bracket-display pairs, zero double-dollar tokens, and no strict UTF-8,
  BOM, C0/DEL, replacement, zero-width, directional, bare-CR,
  final-newline, trailing-whitespace, duplicate-tag, or display-delimiter
  issue; and
- pre-controls MathJax preview generation: PASS on all 22 Markdown files.

Final validation including this record repeats the graph, campaign,
structured-state, compile, six-unit-test, diff, byte, whitespace,
equation-tag, display, and Markdown-preview checks.

## 6. Downstream decision

Close under hard_top_t1_residual_transport_no_go.  The literal residual
and its actual short-shift theorem remain open.  The complete \(t=1\)
face would still leave other few-point channels and near collars.  Hard
TOP, BAL, UNBAL, M9--M2, M9--M1, endpoint uniformity, M9, the bridge, and
the quarter target remain open.

There is no exponent change: internally proved \(1/3\), audited external
\(0.3144831759740614\ldots\), target \(1/4\).

