# Round 145 conductor controls

- Campaign: `m9-m1-lower-cone-squarefree-kernel-linearization-gate`
- Round: `145`
- Starting graph SHA-256: `cc5e1b2597d6d233702d566f49884dc0530d0fa62395ce03684d2f55ae19e756`
- Generated: `2026-08-24T06:38:36+08:00`
- Evidence allocation: 100% analytic/algebraic/source; 0% numerical

| Required control | Outcome | Accepted evidence |
|---|---|---|
| `unique_squarefree_kernel_decomposition_and_block_endpoints` | **GREEN.** \(m=st^2\) is bijective.  Every block is \(\mathbb N\cap[M,B_M)\), with the literal terminal endpoint retained. | Candidate Sections 1 and 3; blind and discovery final GREEN reviews. |
| `exact_C_st2_cone_parity_character_parameterization` | **GREEN.** Both the squarefree-common-kernel formula and the full-gcd formula are multiplicity one; their distinct common factors, all overlaps, oddness, \(\chi_4\), and the strict cone are exact. | Candidate Section 2; both fibre reports; all three final GREEN reviews. |
| `large_square_part_t_tail_absolute_ledger` | **GREEN/target-safe.** A fixed \(t\) supports at most \(3M/t^2\) kernels, giving \(X^\varepsilon M^{1/4}/T\); \(t\geq\lceil M^{1/4}\rceil\) is target-safe after all blocks. | Candidate (145.C9)--(145.C12); adjudication (145.J3)--(145.J4). |
| `small_t_large_s_survivor_and_multiplicity` | **GREEN as a reduction; OPEN as an estimate.** The literal survivor has \(t<M^{1/4}\), \(s>M^{1/2}\), and exact coefficient multiplicity. | Candidate (145.C2)--(145.C3); final GREEN reviews. |
| `j_mask_nearest_integer_sign_tie_and_exact_radical` | **GREEN.** Ties are impossible, the sign and denominator are exact, and \(s={\rm sf}(N)\) is precisely the excluded exact-radical fibre. | Candidate (145.C13)--(145.C16); blind final GREEN. |
| `quadratic_irrational_Pell_and_continued_fraction_exceptions` | **GREEN/no-go.** Nonexact fibres are generalized Pell norms.  The exact \(N=sL^2+1\) family survives the mask with arbitrarily slow phase rotation, so no uniform frequency-gap or bounded-quotient inference is legal. | Candidate (145.C16)--(145.C19); discovery final GREEN. |
| `t_equals_one_and_bounded_t_capacity` | **GREEN/no-go.** The isolated \(t=1\) layer receives no \(t\)-cancellation and has only an \(M^{1/4+o(1)}\) available upper capacity; \(C(p)=\chi_4(p)\ne0\) is nonvacuity only. | Candidate (145.C19)--(145.C21); cross-reviews and final GREEN reviews. |
| `individual_complex_direction_and_fixed_centre` | **GREEN.** Every exact scalar retains \(e(+t\sqrt{Ns})\) at \(N=\lfloor X\rfloor\); no cosine, conjugate, mean square, or centre average is substituted. | Candidate throughout; source final GREEN. |
| `primary_source_coefficient_support_and_frequency_match` | **GREEN/no applicable theorem.** Every theorem card has an exact coefficient, phase, uniformity, or power mismatch. | Source report and source final GREEN review. |
| `full_R_M_s_t_power_and_dyadic_assembly` | **GREEN.** The tail price is \(M^{1/4}/T\), \(M\ll_VR^2\), and the top small-\(t\) upper capacity is \(R^{1/2+o(1)}\).  Audited source powers remain positive. | Candidate Sections 3 and 5; source power review. |
| `Round144_owner_and_Round138_cross_term_separation` | **GREEN.** Only the Round-144 strict cone survivor is reduced.  The exact-radical ledger and independent Round-138 collar-tail cross owner are not recounted. | Candidate Sections 1 and 6; adjudication. |
| `downstream_M1_M2_endpoint_M9_and_exponent_scope` | **GREEN.** No lower GAR, direct M1 parent, M9-M1, M2 owner, endpoint, M9, bridge, quarter theorem, or exponent is promoted. | Candidate Sections 1, 6, and 7; all final GREEN reviews. |
| text and patch hygiene | **GREEN.** The repaired candidate and conductor artifacts have literal endpoints, explicit exceptional-family quantifiers, no embedded forbidden control characters, and no malformed `qquad` token. | Definitive discovery and blind GREEN confirmations; conductor reproduction. |

## Exit-gate result

All required seams are GREEN.  The exact terminal label is
`strict_squarefree_kernel_reduction`.  The graph may accept the exact
coefficient identities and target-safe large-square complement, together
with the scoped linearization/source obstruction.  The small-\(t\),
large-\(s\) signed scalar and every downstream theorem remain open.

## Repository closure

- The State Patch validated before application and applied two creates,
  seven updates, nine rejections, and eight no-change decisions.
- The resulting proof graph validates at
  `7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d`.
- The completed campaign manifest and campaign plan parse and validate.
- All six unit tests pass, and the `math_collab` package compiles.
- A byte scan of every Round-145 artifact finds no embedded carriage
  return, form feed, NUL, or other forbidden control. The authoritative
  candidate, adjudication, controls, and synthesis contain no malformed
  literal `,qquad` token.
- The accepted proof draft, ledger, validation matrix, failure ledger,
  and validation reports were updated only after the graph patch applied.
