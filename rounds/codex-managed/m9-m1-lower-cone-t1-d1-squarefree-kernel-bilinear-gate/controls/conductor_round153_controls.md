# Round 153 conductor controls

- Campaign: `m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate`
- Round: 153
- Starting graph: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| `literal_Pstar_survivor` | GREEN. The positive odd support, $\chi_4$, $n^{-3/4}$, literal zero-extended profile, endpoints, strict large-defect mask, and external $B_{1,U}(1)$ seam are retained. |
| `owned_range_and_owner_exclusion` | GREEN. The open side is $M^{449}\ll R^{780}$; Round-152 exact, small-defect, large-square-factor, and strict-range owners are not recounted as new progress. |
| `squarefree_kernel_uniqueness` | GREEN. Every odd $n$ has one $n=\tau s^2$ with $\tau$ squarefree and $s$ odd, without any inserted coprimality. |
| `exact_Mobius_inversion` | GREEN. $\mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a)$ is inserted over all odd $\tau$ and every sign survives until exact recombination. |
| `a1_short_divisor_seam` | GREEN/open. The $a=s=1$ contribution survives with coefficient one and is the returned direct wave. |
| `dyadic_A_B_s_power_ledger` | GREEN/no gain. $A^2Bs^2\asymp M$ and the corrected exponent-pair powers are exact; absolute block ownership destroys the divisor cancellation. |
| `actual_profile_mask_and_B11` | GREEN. The mask is kept in the algebra and dropped only in a positive boundary upper bound; $B_{1,U}(1)$ stays external. |
| `Cauchy_coefficient_survival` | GREEN/scoped. The surviving $\chi_4$ or Mobius products are explicit. Coefficient-blind positive majorants are not promoted to signed statements. |
| `diagonal_and_pigeonhole_capacity` | GREEN/scoped. Diagonals and ambient pigeonhole counts are upper capacities, not lower bounds and not proof that literal weights occupy the relevant fibres. |
| `exact_and_near_frequency_collisions` | GREEN. Exact square rays, zero-product fibres, algebraic spacing, and optimistic all-$B$ controls are distinguished. |
| `TypeI_TypeII_signed_bilinear_target` | OPEN. Complete recombination self-returns, but a future coefficient-sensitive signed bilinear theorem is not ruled out. |
| `source_theorem_bilinear_match` | GREEN/no direct match. The one-variable BD boundary is unchanged; Robert--Sargos and the other audited sources do not directly close the literal survivor. |
| `absolute_capacity_vs_signed_sum` | GREEN. Every term count and theorem RHS is used only as an upper bound. |
| `N_parity_endpoints_and_transitions` | GREEN. The reindexing never divides by $N$; all parities, ceiling equality, zero extension, transitions, and endpoints remain literal. |
| `D_L_generic_tge2_cross_and_downstream_scope` | GREEN. No broader owner, theorem, or exponent is promoted. |

## 2. Exact recombination control

The conductor independently reproduces

$$
 P_U^*=\sum_{r\ {
m odd}}
 \left(\sum_{\substack{a\mid r\\r/a<S}}\mu(a)\right)
 \sum_{b\ {
m odd}}F_U(r^2b).
\tag{153.K1}
$$

For $r<S$ the inner coefficient is ${\bf1}_{r=1}$. For $r\ge S$,
divisor-bounded multiplicity, $r^2b\asymp M$, and the actual
$M^{-3/4}$ weight give

$$
 \ll_\varepsilon
 \left(M^{-1/4}+M^{1/4}/S\right)X^\varepsilon
 \ll_\varepsilon X^\varepsilon.
\tag{153.K2}
$$

The independent review checks the stronger identity between this boundary
and the negative of the Round-152 large-square-factor owner. This catches
the additive sign and owner-overlap seams.

## 3. Bilinear and source controls

For the relevant BD pair,

$$
 \lambda-\kappa=\frac{275}{796}<\frac12,
 \qquad
 1-2\lambda+2\kappa=\frac{123}{398}>0.
\tag{153.K3}
$$

Thus the corrected Type-I ledger has an absolute dyadic factor
$(AS_0)^{123/398}$ after the $s$-block is summed. Neither that ledger nor
either Cauchy placement supplies a new range. The source reviewer verifies
the exact Robert--Sargos translation and the lower size of a term on its
upper-bound right-hand side,

$$
 R^{1/2}M^{-1/4}\gg R^{59/898}
 \qquad(M^{449}\ll R^{780}).
\tag{153.K4}
$$

This controls only that printed theorem application. It is not a signed
lower bound. The source-review wording corrections concerning
Robert--Sargos Theorem 2 and Lemma 8, Kaczorowski--Perelli notation,
Heath-Brown's $M+N$ factor, and the current Baier follow-up title are
accepted for future reuse and do not change the round decision.

## 4. Terminal review gate

Three orthogonal terminal reviews are GREEN:

- independent algebra and seam review;
- hostile bilinear-method and downstream-scope review; and
- independent primary-source and theorem-hypothesis review.

The reports were corrected before terminal review. The false generic
exponent-pair sign, overbroad fixed-fibre spacing interpretation, ambient
pigeonhole inevitability, mask deletion inside correlation, and future
method impossibility wording are absent from the accepted kernel.

## 5. Pre-mutation validation

Before graph mutation:

- active campaign validation: PASS;
- starting graph validation and SHA-256 check: PASS;
- State Patch JSON parse and dry validation: PASS for 1 create, 4 updates,
  18 rejections, and 8 no-change decisions;
- strict campaign UTF-8/LF, control-character, zero-width, final-newline,
  equation-tag, and display-delimiter scan: PASS on all 17 pre-mutation
  artifacts, with 275 equation tags unique per file and 270 balanced
  double-dollar delimiters; and
- Python compilation: PASS; unit tests: 6/6 PASS; whitespace diff check:
  PASS with repository line-ending warnings only and no whitespace error.

## 6. State mutation and post-validation

The complete pre-mutation gate is GREEN. The dry-validated State Patch
applied:

- 1 obligation created;
- 4 obligations updated;
- 18 false inferences rejected; and
- 8 downstream obligations recorded unchanged.

Resulting graph SHA-256:
`6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`.

The patch tool performed immediate post-application graph validation. The
accepted proof draft is refreshed only from this mutated graph. Complete
closure validation is repeated after the manifest and state records are
updated. That closure validation passes:

- completed campaign and patched graph validators: PASS;
- seven structured JSON/YAML state and campaign files: PASS;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- whitespace diff check: PASS, with line-ending policy warnings only;
- strict campaign scan: PASS on all 17 artifacts; and
- expanded closure scan: PASS on 25 campaign, graph, proof-draft,
  validation, directive, and round-state files, with no invalid UTF-8, BOM,
  forbidden C0, carriage return, replacement character, zero-width code
  point, malformed comma-before-`\qquad` artifact, missing final newline,
  duplicate per-file
  equation tag, or unbalanced display delimiter.

## 7. Downstream decision

Close only the exact complete-Mobius recombination route. Retain the literal
one-variable large-defect wave below $M^{449}\asymp R^{780}$, every other
M1 and M2 owner, endpoint uniformity, M9, the bridge, the quarter target,
the internal exponent $1/3$, and the audited external Li--Yang exponent.
