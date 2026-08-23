# Round 130 conductor controls

Campaign: `gc-w7-16-post-inner-outer-bilinear-gate`

Starting graph SHA-256:
`354f5ca462467d091a9a50c8dbc1173ffba56516963274f9fc232ea11890d20e`

| Control | Outcome | Conductor finding |
|---|---|---|
| `literal_post_inner_dictionary` | pass | Both complete ray coefficients, every Stieltjes threshold, the Möbius progression, determinant taper, centre phases, M1 denominator branches, M2 numerator character, stars, and owners occur before the remaining triangles. |
| `outer_ray_and_increment_counts` | pass with refinement | Outer Cauchy gives $\sum_r|A_i(r)|\ll D$. After exact threshold recombination, shell support gives $\#a'\ll LB/D$, not the crude $L$. |
| shell ledger | pass | $D(LB/D)(K_B/L)=BK_B$; lower shells gain $B/D$ and the top shell retains $DK_D=Y^{35/48}$. |
| `outer_l2_dual_or_Gram` | pass after correction | Atom-space energy is $\mathbf1^*H^*H\mathbf1$ and physical resolved energy is $b^*K_{B,+}^*K_{B,+}b$. $b^*G^2b$ belongs only to a fully completed symmetric row. |
| `phase_aligned_false_control` | required fail | A support- and norm-matched aligned family reaches $LDK_B^2$ energy and $DK_B$ scalar capacity. It is a marginal-hypothesis obstruction, not a literal lower bound. |
| `scalar_vs_positive_energy` | pass | Positive energy optimizes over every outer phase direction and is strictly stronger than the single physical scalar. |
| determinant-residue chart | pass with scope | For fixed primitive top-shell outer ray, $n=aq-bp$ makes $p$ a bounded-multiplicity residue lift when its physical span is $O(|a|)$. No global or lower-shell multiplicity is claimed. |
| `actual_character_placement` | pass | M1 retains denominator quarter phases; M2 retains the fixed $\epsilon_{\rm sgn}\chi_4(|a+p|)$ factor. Inversion restores $\chi_4(d')$ and $\epsilon_{\rm sgn}\chi_4(|h'|)$ respectively. |
| `M1_M2_increment_orientation` | pass | M1 and M2 quarter shifts act in different literal coordinates and are never interchanged. |
| `product_window_resonance_return` | pass as no-go | Same-denominator physical packets remain aligned. Full all-owner inversion returns the accepted $Y^{37/48}$ theorem; isolated top-shell $p$-first modulus returns $D^2/L=Y^{40/48}$. |
| `unit_Hessian_sequential_transform_return` | pass as no-go | The top pre-Möbius ratio phase has unit Hessian, quarter shifts translate aliases, and aliaswise modulus returns $DQ_*=Y^{43/48}$. This is not a physical lower bound. |
| `Mobius_threshold_and_owner_ledger` | pass | Support is imposed after Stieltjes recombination; Möbius pieces reconstruct physical primitivity and are not extra determinant representations. |
| `strict_weak_star_and_support_faces` | pass | Threshold equality, determinant diagonal, numerator exits, hard sample, shell faces, and opposite orientation have distinct one-count owners. |
| `capacity_before_and_after` | pass | Shells range from $Y^{9/16}$ to $Y^{35/48}$; the complete top-dominated block stays $Y^{35/48}$ against target $Y^{1/2}$. |
| `no_exponent_or_M9_promotion` | pass | The complete correlation exponent is not below $9/16$. Internal $1/3$, the audited external benchmark, both M9 components, endpoint uniformity, M9, and the quarter target remain unchanged. |

## Mechanical validation

- Campaign status `complete` validates against the starting graph.
- The proposed State Patch validates before application.
- Six of six unit tests pass.
- Bytecode compilation of `math_collab` and `tests` succeeds.
- All 16 campaign artifacts are strict UTF-8 and contain no forbidden C0
  byte, replacement character, trailing whitespace, conflict marker, or
  malformed merge delimiter.
- All seven JSON-backed campaign/state files parse.
- `git diff --check` succeeds with line-ending warnings only.

The campaign was 100% analytical/algebraic.  No numerical experiment or
external theorem was used.
