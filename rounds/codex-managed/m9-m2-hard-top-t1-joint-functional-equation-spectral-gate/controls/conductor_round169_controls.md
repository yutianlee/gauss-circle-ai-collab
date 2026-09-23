# Round 169 conductor controls

- Campaign: `m9-m2-hard-top-t1-joint-functional-equation-spectral-gate`
- Starting graph: `a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`
- Allocation: 100% analytical/algebraic, 0% numerical
- Terminal candidate: `t1_joint_FE_spectral_self_return_no_go`

| Required control | Outcome |
|---|---|
| `literal_signed_two_height_integral` | **GREEN.** The exact identity is \(\mathcal I_\eta=E_0+N_{\mathrm{phys}}\), with the finite nonzero-frequency aggregate and the residue correction retained. |
| `G_local_coefficients_and_p2` | **GREEN.** All six odd-prime coefficients, cancellation of the two \((2,2)\) states, and \((0,0),(0,2)\) at two are verified independently. |
| `G_weighted_l1_eta_cost` | **GREEN.** The exact mass is \(\asymp\zeta(1+2\eta)^3\asymp\eta^{-3}\); the mass at \((1,1)\) converges. |
| `zeta_completed_function_and_pole` | **GREEN.** Even conductor-one completion, root number one, poles at zero and one, and the full \(s_2=1\) residue are explicit. |
| `chi4_completed_function_parity_root_number` | **GREEN.** Odd primitive conductor four, Gauss sum \(2i\), root number one, and entire completion are explicit. |
| `joint_contour_orientation_and_gamma_factors` | **GREEN.** Both gamma quotients, sine/cosine kernels, the pole-zero cancellation at zero, contour reversal, and the prohibition on post-shift absolute resummation of \(G\) are recorded. |
| `exact_cardinal_cell_or_endpoint_lawful_replacement` | **GREEN as identity; OPEN as estimate.** Exact cardinal cells are transformed without alteration.  No global smooth replacement is claimed. |
| `dual_coefficients_phase_lengths_and_normalization` | **GREEN.** The coefficient is \(ig(Q,R)\chi_4(k)/(2QR)\), the frequencies are \(k/(4Q),\ell/R\), and the product/cone equations are exact. |
| `no_l1_over_G_or_dual_variables_before_joint_phase` | **GREEN.** The signed aggregate is retained through its joint phase.  Positive placement appears only as a scoped capacity diagnostic. |
| `no_common_height_substitution` | **GREEN.** The independent sine and cosine variables are never identified. |
| `no_absolute_or_positive_moment_inflation` | **GREEN.** No positive norm is used as the missing signed theorem. |
| `spectral_exceptional_main_and_continuous_terms` | **GREEN as source audit; OPEN as placement.** The audited sources retain their full spectra and main terms, but none has a literal target-safe map. |
| `functional_equation_AFE_Round162_self_return` | **GREEN.** The collapsed coefficient law proves an exact Round-162 self-return for the full scalar and a return up to \(E_0\) for \(\mathcal I_\eta\). |
| `arbitrary_real_centre_floors_stars_profiles_and_p2_branch` | **GREEN.** All remain inside the exact cardinal values; the even second leg is represented by the two-adic \(R\)-branch. |
| `target_sqrtJ_gain_and_epsilon_order` | **OPEN at the target.** The favorable Mellin absolute placement retains \(\sqrt J\); the active smooth collar retains \(H/L\).  Neither is absorbed into epsilon. |
| `primary_source_exact_hypotheses` | **GREEN.** The source report records exact additive-shift, level, cusp, modular, smoothness, spectral, and norm hypotheses for the dated primary theorem set. |
| `statement_only_independence` | **GREEN.** The blind rederivation independently recovered the coefficient, gamma, Fourier, and rank-one self-return data. |
| `false_unsigned_aligned_and_G_equals_one_controls` | **GREEN as falsifiers.** The rank-one product collar survives all three controls, so dualization alone is not credited with arithmetic cancellation. |
| `downstream_scope_and_no_exponent_promotion` | **GREEN.** The full scalar, parents, bridges, theorem, and both exponent ledgers remain unchanged. |
| `no_in_round_pivot` | **GREEN.** The round stops at the frozen joint-FE/spectral mechanism. |
| `Round170_strategy_literature_review_due` | **GREEN only by scheduling.** Round 170 is the mandatory next round before another analytic attack. |

## Residue seam reproduction

Let \(Z_{\mathrm{phys}}\) be the finite physical \(\ell=0\) term.
The full Mellin residue has the same finite \(Q\)-range but the complete
\(R\ge1\) coefficient sum.  Hence they are not identical.  Cell
disjointness, one \(z\)-integration by parts, and

\[
 \sum_{Q,R}|g(Q,R)|/(QR)<\infty
\]

give

\[
 Z_{\mathrm{phys}},\ R_\zeta,
 \ E_0:=Z_{\mathrm{phys}}-R_\zeta\ll L^2/J.
\]

For an out-of-support \(R\)-block, its complete physical sum is zero but
its zero and nonzero Poisson modes cancel only together.  Thus the
block-completed nonzero-frequency formula and the finite formula plus
\(E_0\) agree exactly.

## Conductor decision

All identity, coefficient, residue, transform, source-scope, false-control,
and graph-scope gates pass.  The target-strength signed estimate does not.
The selected homogeneous result is the exact internal self-return kernel;
the round closes under `t1_joint_FE_spectral_self_return_no_go` with no
parent or exponent promotion.

## Closure validation

- State Patch dry validation: **PASS**.
- State Patch application: **PASS**; one create, one update, seven rejects,
  and 22 explicit no-change decisions.
- Independent applied-patch review: **PASS**; reversing only the authorized
  effects recovers the starting graph hash.
- Authoritative graph validation: **PASS**.
- Completed campaign validation: **PASS**.
- Structured artifact parsing: **7/7 PASS**.
- Python compilation and unit tests: **PASS, 6/6**.
- Round artifact UTF-8, control-byte, replacement-character, trailing-
  whitespace, and final-newline hygiene: **20/20 PASS**.
- Diff check: **PASS**, with line-ending notices only.
- Resulting graph SHA-256:
  `111809875d911d279ae22bee2ce44f0dba97130eeedcdca0dc65f53f163283ae`.
