# Round 155 conductor controls

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate
- Round: 155
- Starting graph: 84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a
- Resulting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| literal_outer_defect_block | GREEN. The selected and ambient blocks retain the actual profile, strict mask, asymmetric cell, both signs, endpoints, and external coefficient seam. |
| selected_ambient_equivalence_and_linearization_scope | GREEN. Linearization is charged only on the selected graph; the inverse identity is pointwise in the exact ambient $B_j$. |
| exact_Bj_and_nonseparable_coefficient | GREEN. No product surrogate replaces $\widehat B_j(2dv)$. |
| mod4N_selector_and_full_normalization | GREEN. The selector, Fourier factor, $d\sqrt c$, half-Gauss factor, and $dc=q$ restore exactly to $-i/(2N)$. |
| all_gcd_two_adic_and_multiplier_strata | GREEN. Every odd $d=(h,N)$ and all two-adic content of $c=4N/d$ are retained for arbitrary $N$. |
| zero_mode_and_exceptional_terms | GREEN/scoped. The zero row is explicit; all source spectral pieces remain; no upper capacity is called a lower bound. |
| complete_vs_truncated_v_transform | GREEN/no gain. Complete resummation self-returns, while a proper cutoff becomes $\eta(u-ax)$. |
| inverse_Gauss_self_return_test | GREEN. The exact half-period identity restores the original quotient selector. |
| positive_negative_defect_and_cell_endpoints | GREEN. Both signs and literal hard endpoints remain throughout. |
| N_M_V_d_power_ledger | GREEN. The zero row, nonzero termwise capacity, sampled norm, and hypothetical square-root threshold are fully restored. |
| actual_profile_transitions_and_B11 | GREEN. Transitions and zero extension stay in $B_j$; $B_{1,U}(1)$ stays external. |
| Cauchy_Parseval_diagonal_and_collision_scope | GREEN. Parseval folds modulo $2N/d$ and retains large-$d$ collisions. |
| fixed_modulus_vs_modulus_average_source_match | GREEN/no-match. DFI is termwise only; no audited joint theorem matches the literal fixed modulus and coefficient. |
| square_root_range_V_le_Mthreehalves | GREEN as capacity only. No range is promoted. |
| absolute_capacity_vs_signed_sum | GREEN. Every positive theorem right side and norm is treated only as an upper capacity. |
| D_L_generic_tge2_cross_and_downstream_scope | GREEN. No broader M1, M2, endpoint, M9, bridge, target, or exponent owner is promoted. |

## 2. Exact inverse, folds, and zero-row control

For $c=4N/d$ and $H=c/2$,

$$
 \sum_{v\bmod H}e_c(-\bar a v^2-2xv)
 =\frac{1-i}{2}\epsilon_a\left(\frac ca\right)
 \sqrt c\,e_c(ax^2).
\tag{155.K1}
$$

Consequently

$$
 \sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)
 =\frac{1-i}{2}\sqrt c
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
\tag{155.K2}
$$

The exterior constant restores to $-i/(2N)$ and the complete $d$-sum is
the original selector. Sampled Parseval has exact fold period $2N/d$:

$$
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 =H\sum_{r\bmod H}|C_{j,d}(r)|^2
 \ll_\varepsilon
 \left(\frac{N^{3/2}}{dM}+\frac{N}{M^{1/2}}\right)X^\varepsilon.
\tag{155.K3}
$$

The zero row has only

$$
 |\mathcal T_{0,U}(V)|\ll_\varepsilon
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon.
\tag{155.K4}
$$

All four displays were independently rederived. The circular flat-$j$
arc was also checked with both its near-zero and near-$c$ representatives.

## 3. Terminal review and source gate

Three orthogonal terminal reviews are GREEN:

- independent inverse-Gauss mathematics, normalization, folds, zero mode,
  and wrapped-arc review;
- independent primary-source theorem-hypothesis and translated-power
  review; and
- hostile blind-surrogate, capacity, endpoint, source-scope, and
  downstream-promotion review.

The source reviewer identified two nonfatal precision qualifications,
both incorporated before closure: DFI's weakened Theorem-2.5 option
retains its zero conditions, and Sun Theorem 3.3 is directly stated for
weights $1/2$ and $3/2$. The source conclusion remains a dated
direct-interface no-match, not an impossibility theorem.

## 4. Pre-mutation validation

Before graph mutation:

- active campaign validation: PASS;
- starting graph SHA-256 check: PASS;
- State Patch JSON parse and dry validation: PASS for 2 creates, 5
  updates, 20 rejections, and 8 no-change decisions;
- strict campaign scan: PASS on 17 artifacts, with 146 per-file-unique
  equation tags and 196 balanced double-dollar delimiters; and
- whitespace diff check: PASS with repository line-ending warnings only.

No numerical experiment was used.

## 5. State mutation

The dry-validated State Patch applied:

- 2 obligations created;
- 5 obligations updated;
- 20 false inferences rejected; and
- 8 downstream obligations recorded unchanged.

The patch tool immediately validated the resulting graph. Its SHA-256 is
f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6.
The accepted proof draft was refreshed only after this mutation.

## 6. Complete closure validation

After the manifest, ledger, validation matrix, proof draft, failure ledger,
directives, synthesis, and controls were closed:

- completed campaign and patched graph validators: PASS;
- seven structured JSON/YAML files: 7/7 parse;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- whitespace diff check: PASS, with repository line-ending policy warnings
  only;
- strict final campaign scan: PASS on 19 artifacts with
  158 per-file-unique equation tags and 220 balanced
  double-dollar delimiters; and
- expanded closure scan: PASS on 30 files with
  471 per-file-unique equation tags and 1006
  balanced double-dollar delimiters.

Both scans require valid UTF-8, LF-only files, no BOM, forbidden C0 or DEL
byte, replacement, zero-width or directional code point, malformed
comma-before-TeX spacing command, missing final newline, duplicate
per-file equation tag, or unbalanced display delimiter.

## 7. Downstream decision

Close under outer_defect_theta_dispersion_no_go. Promote the exact
complete-half-period inverse-Gauss self-return, folded sampled Parseval,
zero-mode and partial-transform upper ledgers, wrapped reciprocal-arc
localization, and scoped source boundary. Retain the signed zero row,
incomplete nonzero matrix, every positive-power range, all other M1 and
M2 owners, endpoint uniformity, M9, the bridge, the quarter target, the
internal exponent $1/3$, and the audited external Li--Yang exponent as
open or unchanged.
