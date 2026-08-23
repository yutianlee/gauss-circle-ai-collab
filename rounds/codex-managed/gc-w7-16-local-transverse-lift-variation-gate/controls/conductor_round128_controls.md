# Round 128 conductor controls

Campaign: `gc-w7-16-local-transverse-lift-variation-gate`

Starting graph SHA-256:
`1a5c8c8b4b6c6c0dcf3d0e05a1607b3d29dfe22f66748d401405d1c0f7b474d6`

| Control | Outcome | Conductor finding |
|---|---|---|
| `literal_complete_lift_dictionary` | pass after normalization | Round-95 (2.1)--(2.4), (3.4)--(3.7) gives frequency-only \(\Phi v_L\) times denominator-only \(\omega_D(gb')\); no mixed support remains. |
| `local_window_and_birth_count` | pass | The monotone threshold changes on \(O(1+DQ_B/B^2)=O(J_B)\) steps on the same physical \(Q_B\)-window. |
| `V2_endpoint_terms` | pass | Interval-uniform character Abel gives both endpoint values \(O(L^{-1})\) before Minkowski. |
| `continuous_weight_variation` | pass | Exact discrete Stieltjes decomposition represents the entire sampled-BV denominator profile, including hard and starred samples, by bounded-mass thresholds. |
| `character_partial_sum_before_modulus` | pass with required adversarial failure | The actual frequency factor is BV and permits Abel; a phase-conjugating lift weight has full \(G/L\) endpoint capacity. |
| `mobius_divisor_progressions` | pass | The estimate is uniform for \(b'=\rho v\); interval Abel handles skipped lifts and the later divisor sum costs only \(Y^\varepsilon\). |
| `floors_stars_hard_faces_and_support` | pass | Frequency faces are fixed in \(P\); every denominator face is contained in the zero-extended BV profile; clipped reduced-variable faces add \(O(1)\) jumps. |
| `cross_shell_owner_and_no_duplication` | pass | Half-open reduced-denominator shells and at most \(O(1)\) window splits give one inner owner; the original denominator profile remains inside the same lift sum. |
| abstract pointwise/birth inference | reject | The blind fixed-window and continuous-variation controls show that pointwise scale, \(\chi_4\), and \(J_B\) alone do not control \(V^2\). |
| unsplit M1 character | reject | On a top-shell one-lift packet it costs \(Q_B^{1/2}/L\) while \(J_B\asymp1\); exact quarter-phase splitting is mandatory. |
| M2 reduced character | pass | \(a'\) is fixed, so \(\chi_4(|a'|)\) is constant in the transverse variable. |
| `theta_two_thirds_capacity_threshold` | pass for coefficient gate | The proved branchwise loss is \(J_B^{1/2}/L\), so \(\theta=1/2<2/3\). |
| joint curvature inference | open | A generic \(V^2\) argument loses \(N_\rho^{1/2}\); no oscillatory theorem is inferred from the coefficient norm. |
| `finite_stop_rule` | pass | Continue only with the exact branchwise actual family; stop on a full-lift, reciprocal-window square-root, or owner-separation loss. |
| `no_exponent_or_M9_promotion` | pass | No fixed-block correlation saving, global exponent, M9 parent, endpoint theorem, M9, or quarter theorem is promoted. |

All controls are analytic.  No external result or numerical experiment is
used.
