# Round 129 conductor controls

Campaign: `gc-w7-16-joint-stieltjes-reciprocal-curvature-gate`

Starting graph SHA-256:
`476b1445ef73d86627fd87de8bd2dd76a5efa53564a5b195230f2ad33ba2bbe8`

| Control | Outcome | Conductor finding |
|---|---|---|
| `branchwise_literal_dictionary` | pass | Round-128's exact factorization gives one fixed sampled-BV lift factor, one sampled-BV denominator profile, the two M1 quarter phases, and the fixed M2 character. |
| `generic_V2_dual_countermodel` | required fail | The exact prefix-variance dual and an actual triangular threshold packet disprove the norm-relative claim by \(Y^{1/48}\). |
| `single_threshold_birth_phase` | pass | Literal floor plateaux retain the common character, reciprocal phase, and quarter shift jointly; no nonresonance is assumed. |
| `character_before_modulus` | pass | Bounded partial sums of \(\chi_4(g)\) are consumed by Abel before any lift modulus, giving scale \(L^{-1}\). |
| `M1_quarter_phase_aliases` | pass | Both shifted stationary lattices are covered by the weighted second-derivative estimate. |
| `reciprocal_second_derivative_and_stationary_lattice` | pass | \(|f''|\asymp\lambda_B\rho^2\) throughout each clipped interval; integer derivative crossings require no separate loss. |
| `threshold_superposition_and_Minkowski` | pass absolute, fail norm-relative | Exact Stieltjes mass preserves \(K_\rho/L\); it cannot be replaced by the possibly smaller completed \(V^2\) norm. |
| `V2_endpoint_terms` | pass/no-go robust | The direct theorem prices plateau and outer endpoints; the norm counterexample has both displayed endpoints zero. |
| `mobius_progressions` | pass | Prove uniformly for each \(\rho\mid a'\), then use divisor sums to obtain \(K_B/L\) with only \(Y^\varepsilon\). |
| `floors_stars_taper_and_shell_owners` | pass | Equality atoms are divisor-many, the exact taper is BV, and half-open shells give one owner. |
| `actual_vs_phase_adapted_coefficients` | pass with scope split | Phase adaptation defeats only the norm formulation; the direct fixed-mass theorem holds for the full displayed Stieltjes class. |
| `N_rho_square_root_stop_rule` | pass | The only birth endpoint term is absorbed by \(N_\rho\Lambda_\rho=L\rho(J_B-1)\); no \(N_\rho^{1/2}\) appears. |
| `theta_two_thirds_capacity_threshold` | pass strongly | The direct theorem has effective \(J_B\)-power \(\theta=0\). |
| outer ledger | pass after independent audit | \((LD)L L^{-1}(K_B/L)=DK_B\), with no added cross-shell factor. |
| fixed-block exponent | pass | Uniform \(K_B=Y^{11/48+o(1)}\) gives complete \(Y^{35/48+\varepsilon}\). |
| `no_exponent_or_M9_promotion` | pass | The new block is still \(Y^{11/48}\) above target and persists only to \(7/18>1/3\); all M9 parents and the global exponents are unchanged. |

The blind report, discovery report, hostile report, hostile addendum, and
conductor line audit agree on the direct theorem and disagree only with
the rejected norm normalization.  This is proof by compatible interfaces,
not by vote.  The campaign is 100% analytical/algebraic; no numerical
experiment or external theorem is used.

