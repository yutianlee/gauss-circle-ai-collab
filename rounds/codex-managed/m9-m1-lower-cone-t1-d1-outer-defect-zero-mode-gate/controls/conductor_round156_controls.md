# Round 156 conductor controls

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Round: 156
- Starting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Resulting graph: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| literal_zero_row | GREEN. The exact ambient phase, actual profile, zero extension, strict mask, asymmetric cell, both signs, endpoints, and external coefficient seam remain. |
| arbitrary_N_and_all_odd_d | GREEN. No squarefree or odd-$N$ assumption is used; every odd $d\mid N$ is retained. |
| primitive_and_induced_characters | GREEN. Both fundamental discriminants, the exact induced formula, conductor one, and every extra unit prime are present. |
| odd_prime_power_and_two_adic_factors | GREEN. Conductors $1$, $4$, and $8$, phases, support, squareful shells, and half-support cancellation are checked. |
| literal_Bhat0_BV | GREEN. Monotone sampling, zero extension, residual-phase derivative, transitions, endpoints, and $O(K)$ physical support prove the stated norm. |
| all_d_recombination | GREEN. The exact quotient projector and gcd partition produce $\mathscr S_N$ without losing imprimitive strata. |
| physical_root_identity | GREEN. The difference $\rho_{4N}(j+N)-\rho_{4N}(j+3N)$ independently checks the recombination. |
| finite_Fourier_interval_theorem | GREEN. Even frequencies vanish, odd frequencies have the exact gcd magnitude, and finite inversion gives the signed interval bound. |
| independent_fixed_d_control | GREEN. Nonzero additive unit frequencies and geometric sums give $c\log(2c)$ uniformly. |
| exact_normalization_and_power | GREEN. The exterior factor becomes $(4N)^{-1}$ after recombination and Abel gives $M^{-1/4}X^\varepsilon$. |
| source_and_method_legality | GREEN. The proof is elementary after the accepted Gauss identities; optional character bounds are not required. |
| nonzero_matrix_scope | GREEN/open. No zero-row identity is transferred to $\widehat B_j(2dv)K(-v^2,-j;c)$ for $v\ne0$. |
| downstream_scope | GREEN. No complete defect range, other owner, M9 statement, bridge, target, or exponent is promoted. |

## 2. Exact zero-row proof kernel

For

$$
 \mathscr S_N(j)=
 \sum_{x\bmod4N}{\bf1}_{N\mid x^2-j}
 \chi_4\!\left(\frac{x^2-j}{N}\right),
\tag{156.K1}
$$

the exact recombination is

$$
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt{\frac{4N}{d}}\,
 K\!\left(0,-j;\frac{4N}{d}\right).
\tag{156.K2}
$$

Its interval sums satisfy

$$
 \sup_{\substack{I\ \mathrm{consecutive}\\|I|\le4N}}
 \left|\sum_{j\in I}\mathscr S_N(j)\right|
 \ll\sqrt N\,\tau(N)\log(2N).
\tag{156.K3}
$$

The literal coefficient obeys

$$
 \sup_j|\widehat B_j(0)|
 +\operatorname {Var}_j\widehat B_j(0)
 \ll_\varepsilon\sqrt{NM}\,M^{-3/4}X^\varepsilon.
\tag{156.K4}
$$

Therefore

$$
 \mathcal Z_U(V)=\frac1{4N}
 \sum_{V<|j|\le2V}\widehat B_j(0)\mathscr S_N(j)
 \ll_{\varepsilon,A}M^{-1/4}X^\varepsilon.
\tag{156.K5}
$$

All identities and powers were independently rederived.

## 3. Terminal review and source gate

Three orthogonal terminal reviews are GREEN:

- independent character, recombination, Fourier, normalization, and
  power mathematics;
- independent source and legal-method audit; and
- hostile literal-profile, transition, cell, endpoint, and downstream
  scope review.

The initial direct-source no-match is superseded only for $v=0$, because
the missing literal progression-BV norm is proved internally. It remains
a route-scoped warning for the nonzero matrix, not an impossibility
theorem.

## 4. Pre-mutation validation

Before graph mutation:

- active campaign validation: PASS;
- starting graph SHA-256 check: PASS;
- State Patch parse and dry validation: PASS for 1 create, 7 updates,
  18 rejections, and 8 no-change decisions;
- strict campaign scan: PASS on 17 artifacts with 233 per-file-unique
  equation tags and 72 balanced double-dollar delimiters; and
- whitespace and strict UTF-8/LF hygiene checks: PASS.

No numerical experiment was used.

## 5. State mutation

The dry-validated State Patch applied:

- 1 obligation created;
- 7 obligations updated;
- 18 false inferences rejected; and
- 8 downstream obligations recorded unchanged.

The graph validator immediately passed. The resulting SHA-256 is
3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea.
The accepted proof draft was refreshed only after this mutation.

## 6. Complete closure validation

After the manifest, ledger, validation matrix, proof draft, failure
ledger, directives, synthesis, and controls were closed:

- completed campaign and patched graph validators: PASS;
- seven structured JSON/YAML files: 7/7 parse;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- whitespace diff check: PASS, with repository line-ending policy
  warnings only;
- strict final campaign scan: PASS on 19 artifacts with 254
  per-file-unique equation tags and 82 balanced double-dollar
  delimiters; and
- expanded closure scan: PASS on 34 files with 598 per-file-unique
  equation tags and 898 balanced double-dollar delimiters.

Both scans require valid UTF-8, LF-only files, no BOM, forbidden C0 or
DEL byte, replacement, zero-width or directional code point, malformed
comma-before-TeX spacing command, missing final newline, duplicate
per-file equation tag, or unbalanced display delimiter.

## 7. Downstream decision

Close under outer_defect_zero_mode_target. Promote the exact character
local factors, literal zero-coefficient BV, all-divisor recombination,
finite signed interval theorem, independent fixed-divisor control, and
the full $M^{-1/4}X^\varepsilon$ zero-row estimate. Retain the incomplete
nonzero matrix, every complete positive-power defect range, all other M1
and M2 owners, endpoint uniformity, M9, the bridge, the quarter target,
the internal exponent $1/3$, and the audited external Li--Yang exponent
as open or unchanged.
