# Round 142 conductor controls

Campaign: m9-m1-lower-cone-rational-additive-spectrum-gate

Starting graph SHA-256:
de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76

## Mathematical seam matrix

| Frozen control | Exact test | Outcome |
|---|---|---|
| exact_cone_hyperbola_endpoints_and_parity | Keep \(4h^2<M\), first odd \(4h+1\), upper \(\lfloor M/h\rfloor\), and \(\chi_4=0\) on evens. | Green. No endpoint relaxation enters the row theorem. |
| reduced_rational_frequency_and_q_mod_4_cases | Solve \(ah/q\equiv\pm1/4\pmod1\) for reduced \(a/q\). | Green. A row mean exists exactly when \(4\mid q\). |
| row_mean_residue_classes_sign_and_constant | For \(q=4Q\), audit the two height classes and Gregory sum. | Green. Classes \(Q,3Q\pmod{4Q}\) have opposite means and give \(i\pi\chi_4(a)/(2q)\). |
| fixed_q_versus_growing_q_error_uniformity | Sum reciprocal root spacings over full height periods and compare main/error. | Green. Uniform error is \(O((\sqrt M+q)\log(2q))\); \(q\log(2q)=o(\sqrt M)\) is sufficient for dominance. |
| rational_spectrum_convergence_and_reconstruction | Check fixed-height DFT, finite omitted modes, coefficient masses, hard cutoff, and Abel grouping. | Green obstruction. Finite cutoffs retain every omitted mode; masses are \(\asymp Q\) and \(\asymp\log Q\); denominator-Abel completion is \(r_2/4\), not \(C\). |
| gauss_mobius_abel_constants | Recompute \(\tau(\chi_4)\), the unit Möbius inversion, frequency reversal, and \(L(1,\chi_4)\). | Green. Constants are \(2i\), \(\pi/4\), and the Abel limit has unit normalization. |
| negative_character_residual | Put \(m=2^\nu n\), \(n\) odd, \(\chi_4(n)=-1\). | Green obstruction. \(\sigma_{\chi_4}(m)=0\), so \(C-r_2/4=C\) on the full sector. |
| moving_cone_boundary | Freeze \(4h^2<M\) on \([M,2M)\) and unfold the omitted wedge. | Green obstruction. Its unsigned weighted incidence is \(\asymp M^{1/4}\), hence \(R^{1/2}\) at the top scale. |
| local_derivative_arc_width_overlap_and_multiplicity | Compute curvature length, Farey order, thickened overlap, half-open cells, and singleton transition. | Green. \(L_M\asymp M^{3/4}/R\), \(Q_M\asymp L_M\), overlap \(O(L_M)\), and \(M\lesssim R^{4/3}\) is singleton. |
| nonresonant_phase_value_versus_slope_distinction | Rationalize \(|\Phi'(m)-u/q|\) using the nonzero integral numerator. | Green. The lower separation is only \(\gg(q^2\sqrt{NM})^{-1}\), far below \(L_M^{-1}\). |
| residual_additive_partial_sum_hypothesis | Insert the number of cells and the \(M^{-3/4}\) weight. | Open owner identified. Absolute assembly requires \(X^\varepsilon\sqrt M/R\), while the prefix theorem has \(\sqrt M\)-scale error. |
| periodic_branch_all_dyadic_R_and_q_power_ledger | Use the real-variable second-derivative estimate and exact coefficient mass. | Green as an insufficient upper ledger. One branch is \(\ll\min(M^{1/4},RM^{-1/2}+R^{-1})\); all fixed-height denominators cost owner scale. |
| source_theorem_coefficient_q_range_and_direction | Check exact locations, hypotheses, coefficient class, smoothing, and complex direction in Jutila, Kaneko, and Banerjee--Khurana. | Green after repair. No source theorem applies to the incomplete moving cone or supplies the local residual theorem. |
| canonical_transform_self_return_and_downstream_scope | Audit \(k-\beta>0\), \(z>0\), both saddle signs/amplitudes, and branchwise error ownership. | Green only at principal-symbol level. The phase/character return, but both branchwise remainders and the hard endpoint/Fresnel transition remain open. |
| raw_capacity_versus_fixed_centre_signed_scalar | Separate coefficient mass, wedge incidence, and stationary capacity from the complex scalar. | Green. No capacity is used as a bound or lower bound for the target. |

## Independent seam reviews

| Review | Assigned seam | Final outcome |
|---|---|---|
| blind post-unmask rational reconstruction | Statement-only row theorem, DFT, reconstruction, wedge, cells, phase/slope, stationary sign | Green after replacing one unsupported neighborhood-density phrase and auditing the added Gauss--Möbius--Abel identities. |
| source post-unmask Abel/B-process | Gauss and Möbius constants, hard/Abel distinction, negative-character residual, saddle positivity, signs, amplitudes, \(R/q\) ledger | Green after the candidate made \(N^{-1/4}\), \(k-\beta>0\), and \(z>0\) exact. |
| discovery post-unmask source/B-process | Primary theorem locations and hypotheses, direct branch bound, complex direction, second-transform error scope | Initially red, then green after correcting the Jutila and Banerjee--Khurana cards and downgrading the transform to principal-symbol algebra. |

No reviewer certifies its own principal discovery.  Every requested
candidate or source-report repair is present in the final artifacts.

## Exit-gate decision

- `target_bound`: not met;
- `strict_rational_spectrum_reduction`: not met, because neither a
  target-safe reconstruction residual nor all extracted masked branches
  are proved;
- `rational_major_arc_self_return_no_go`: met.

The first open estimate remains

\[
\sum_M\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\ll_\varepsilon X^\varepsilon.
\]

## Resource and artifact controls

- Analytical/algebraic/source work: 100 percent.
- Numerical or symbolic experiments: none.
- Centre averages, positive energies, arbitrary arrays, and desired
  circle estimates: none.
- Primary reports: three of three present, each with exactly seven
  numbered sections.
- Post-unmask reviews: three of three present, each with exactly seven
  numbered sections and a final green verdict.
- Candidate and conductor adjudication: present with exactly seven
  numbered sections.

- Artifact hygiene: all 16 campaign files and all eight seven-section
  research artifacts have zero standalone carriage returns, forbidden
  controls, replacement or zero-width characters, trailing whitespace,
  conflict markers, malformed spacing-command tokens, or TeX delimiter defects.
- State Patch: dry-validated before application; one create, four
  updates, 23 rejects, and eight no-change decisions applied.
- Resulting graph:
  `7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789`;
  graph validation passes.
- Repository validation: campaign and all JSON-backed state parse; six
  of six unit tests pass; bytecode compilation succeeds.

## Downstream status

The exact rational spectrum is now known, but the fixed-centre
nonresonant cone scalar is still open.  Lower GAR, both direct M1
parents, M9-M1, hard TOP, BAL, all required UNBAL owners, M9-M2,
endpoint uniformity, M9, the conditional bridge, and the quarter target
remain open.

The strongest internally proved exponent remains \(1/3\).  The
separately audited external Li--Yang exponent remains

\[
{3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots.
\]
