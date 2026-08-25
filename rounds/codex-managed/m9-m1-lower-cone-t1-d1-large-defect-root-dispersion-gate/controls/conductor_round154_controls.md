# Round 154 conductor controls

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Round: 154
- Starting graph: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Resulting graph: `84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| `literal_direct_large_defect_wave` | GREEN. The positive odd quotient, $\chi_4$, $n^{-3/4}$, literal zero-extended profile, strict defect mask, endpoints, and external $B_{1,U}(1)$ seam are retained. |
| `owned_range_and_mask_order` | GREEN. Round-152 exact and small defects are restored only at scalar level; no mask is deleted inside Cauchy or a correlation. |
| `exact_root_defect_bijection` | GREEN. There is no tie; $j=k^2-Nn$ gives the exact cell $-k\le j\le k-1$, converse, positivity, quotient parity, and multiplicity one. |
| `nearest_cell_endpoints_and_converse` | GREEN. Both asymmetric endpoints are literal and consecutive cells partition the positive integers after scalar restoration. |
| `support_injectivity_and_unique_residue` | GREEN. On support $k\asymp\sqrt{NM}$, the $k$-span is $O(\sqrt{NM})<N$, $2k<N$, and each residue class occurs at most once. |
| `mod4N_quotient_character_completion` | GREEN. The exact selector has factor $-i/(2N)$, odd frequencies modulo $4N$, and the correct $\chi_4(h)$ sign. |
| `all_parity_two_adic_imprimitive_Gauss` | GREEN. The root count includes $p=2$; ambient completion retains $d=(h,N)$, $q'=4N/d$, the even-dual condition, and the mandatory $d\sqrt{q'}$ factor. |
| `positive_negative_and_dyadic_defects` | GREEN. Both signs and all $M^{3/4}<|j|\le\sqrt{NM}$ blocks are retained; only a fixed-polylogarithmic first collar is closed. |
| `K_J_N_h_power_ledger` | GREEN. The selected linearization error is priced on $O(M)$ selected points, and the fully restored DFI block is $M^{-3/4}V+M^{-1/4}$. |
| `actual_profile_endpoints_and_B11` | GREEN. Actual bounded variation, zero extension, transitions, endpoints, and the external coefficient seam are explicit. |
| `Cauchy_diagonal_and_collision_survival` | GREEN/no gain. Post-selection odd-frequency rows have rank one and normalized Cauchy is equality; this is not transferred to lawful ambient rows. |
| `completion_remainder_and_outer_sums` | GREEN/no all-scale gain. Nonzero modes, zero mode, gcd strata, defect signs, endpoints, and outer sums restore before the displayed bound is used. |
| `source_theorem_quadratic_root_match` | GREEN/scoped. DFI Lemma 6.1 exactly bounds the theta-multiplier Kloosterman block; it does not bound the remaining coupled outer-defect family. |
| `absolute_capacity_vs_signed_sum` | GREEN. Root counts and positive terms in upper bounds are not treated as signed lower bounds. |
| `D_L_generic_tge2_cross_and_downstream_scope` | GREEN. No $D>1$, $L>1$, generic, $t\ge2$, cross, M2, endpoint, M9, bridge, target, or exponent owner is promoted. |

## 2. Root-cell and collar control

The conductor independently retains

$$
 -k\le j\le k-1,\qquad N\mid k^2-j,\qquad
 n=(k^2-j)/N>0\ \mathrm{odd},
\tag{154.K1}
$$

with no tie and an exact converse. On the selected graph,

$$
 -\frac{j}{k+\sqrt{k^2-j}}
 =-\frac{j}{2k}
 -\frac{j^2}{2k(k+\sqrt{k^2-j})^2},
\tag{154.K2}
$$

so the total phase-replacement error is
$O_\varepsilon(N^{-1/2}M^{-1/4}X^\varepsilon)$. It is not priced over
the ambient $k,j$ rectangle. The all-parity root bound and its divisor
sum prove

$$
 M^{3/4}<|j|\le M^{3/4}(\log(2X))^A
\tag{154.K3}
$$

is $O_{\varepsilon,A}(X^\varepsilon)$ for every fixed $A>0$. The same
argument leaves $M^\delta$ unabsorbed for a positive-power collar.

## 3. Selector, completion, and source controls

The post-selection rows satisfy $T_h=\pm iQ_U$, so normalized frequency
Cauchy is exactly $|Q_U|^2$. The lawful ambient completion remains
nondegenerate and has normalized form

$$
 -\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt{q'}
 \sum_{v\bmod(q'/2)}\widehat B_j(2dv)K(-v^2,-j;q'),
 \qquad q=4N,\quad q'=q/d.
\tag{154.K4}
$$

DFI Lemma 6.1 applies with $q'\equiv0\pmod4$. Restoring the BV Fourier
ledger, all $d$, zero and nonzero dual modes, both signs, and outer defect
blocks gives

$$
 |Q_U(V)|\ll_\varepsilon
 (M^{-3/4}V+M^{-1/4})X^\varepsilon.
\tag{154.K5}
$$

The official DFI erratum does not alter Lemma 6.1. The source review treats
the absence of a theorem for the remaining nonseparable coefficient as a
direct no-match only, not a literature-impossibility result.

## 4. Terminal review gate

Three orthogonal terminal reviews are GREEN:

- independent mathematical normalization, cell, power, and endpoint review;
- hostile method, mask-order, capacity, and downstream-scope review; and
- independent primary-source and theorem-hypothesis review.

The accepted kernel includes the corrected $d\sqrt{q'}$ normalization,
distinguishes post-selection from ambient rows, and limits the direct
$Q_U$ scope correctly. The principal full-cell saddle is accepted only as
the Round-151/152 reciprocal self-return with the inherited remainder and
endpoint ledger.

## 5. Pre-mutation validation

Before graph mutation:

- active campaign validation: PASS;
- starting graph validation and SHA-256 check: PASS;
- State Patch JSON parse and dry validation: PASS for 3 creates, 5 updates,
  21 rejections, and 8 no-change decisions;
- strict campaign UTF-8/LF, control-character, zero-width, final-newline,
  equation-tag, and display-delimiter scan: PASS on all 17 pre-mutation
  artifacts, with 237 equation tags unique per file and 270 balanced
  double-dollar delimiters; and
- Python compilation: PASS; unit tests: 6/6 PASS; whitespace diff check:
  PASS with repository line-ending warnings only and no whitespace error.

## 6. State mutation and post-validation

The dry-validated State Patch applied:

- 3 obligations created;
- 5 obligations updated;
- 21 false inferences rejected; and
- 8 downstream obligations recorded unchanged.

Resulting graph SHA-256:
`84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`.

The patch tool performed immediate post-application graph validation. The
accepted proof draft is refreshed only from this graph. Complete closure
validation was repeated after the manifest and state records were updated:

- completed campaign and patched graph validators: PASS;
- seven structured JSON/YAML campaign and state files: PASS;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- whitespace diff check: PASS, with repository line-ending policy warnings
  only;
- strict campaign scan: PASS on all 18 final artifacts, with 242 equation
  tags unique per file and 280 balanced double-dollar delimiters; and
- expanded closure scan: PASS on 29 campaign, graph, proof-draft,
  validation, directive, and round-state files, with 544 equation tags
  unique per file and 1042 balanced double-dollar delimiters.

Both strict scans found no invalid UTF-8, BOM, forbidden C0 or DEL byte,
carriage return, replacement character, zero-width or directional code
point, malformed comma-before-`\qquad` artifact, missing final newline,
duplicate
per-file equation tag, or unbalanced display delimiter.

## 7. Downstream decision

Close under `strict_large_defect_root_range`. Promote the exact root cell,
selected-graph linearization, and fixed-polylogarithmic collar, together
with the scoped theta-completion and reciprocal-self-return obstruction.
Retain the signed outer-defect family beyond the collar, every other M1 and
M2 owner, endpoint uniformity, M9, the bridge, the quarter target, the
internal exponent $1/3$, and the audited external Li--Yang exponent as
open or unchanged.
