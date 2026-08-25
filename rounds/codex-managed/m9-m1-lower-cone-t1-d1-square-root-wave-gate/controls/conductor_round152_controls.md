# Round 152 conductor controls

- Campaign: `m9-m1-lower-cone-t1-d1-square-root-wave-gate`
- Round: 152
- Starting graph: `d09d0f8c1e7058a1e423e5249d3cf28b08d8478cff55ddd1c85b1d59bb177b2c`
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| `literal_square_root_wave` | GREEN. The positive odd support, $\chi_4$, $\ell^{-3/4}$, literal actual profile, zero extension, endpoint convention, $N=\lfloor X\rfloor$, and the accepted phase are retained. |
| `owned_range_exclusion` | GREEN. Bounded $M$, the older TTY range, and the new $M^{449}\gg R^{780}$ owner are subtracted exactly once; no overlap is counted as new progress. |
| `actual_profile_and_B11_coefficient` | GREEN. The accepted normalized BV bound is used only after an unweighted interval theorem, and $B_{1,U}(1)$ remains attached to $S_U$. |
| `adjacent_odd_character_pairing` | GREEN/no gain. Exact adjacent pairing keeps the full phase difference, which can approach an integer and is not replaced by a smooth derivative. |
| `A_process_character_survival` | GREEN/no gain. Every legal shift is $2h$ and $\chi_4(\ell+2h)\chi_4(\ell)=(-1)^h$; the variable character is erased. |
| `squarefree_kernel_and_exact_square_resonance` | GREEN. The unique $\ell=\tau s^2$ representation inserts no coprimality; the exact ray, small nonzero defects, and large square factors are summed completely. |
| `Mellin_conductor_and_dual_length` | GREEN/no gain. Spectral scale is $\sqrt{NM}$, root number is $+1$, AFE length is $\asymp RM^{1/4}$, and the unbalanced additive dual length is $\asymp R^2M^{-1/2}$. |
| `boundary_complete_transform` | GREEN. The accepted compact-profile error, endpoints, tails, transitions, and external coefficient remain; only the principal transform is called a self-return. |
| `derivative_and_exponent_pair_power` | GREEN. The one-$A$ bound, second and third derivative bounds, Bourgain, TTY, $D$, and $BD$ powers all rederive exactly. |
| `source_theorem_square_root_match` | GREEN for the $BD$ range. The model phase has $\sigma=1/2$, $T/H\gg R$, interval uniformity, and Abel-after-unweighted ordering. Audited alternatives are only scoped no-matches. |
| `absolute_capacity_vs_signed_sum` | GREEN. Raw term count, actual weighted capacity, character mass, exact resonance mass, and the open signed survivor are kept distinct. |
| `bounded_intermediate_TTY_endpoint` | GREEN. The new boundary is $M=R^{780/449}$, strictly below the old $M=R^{1424/819}$ boundary, and the bounded/top owners are unchanged. |
| `N_parity_and_near_square_controls` | GREEN. The prime-power quadratic-root proof includes $p=2$, both parities of $N$, the no-tie argument, the sub-$N$ $k$ interval, the ceiling split, and actual endpoints. |
| `D_L_generic_tge2_cross_and_downstream_scope` | GREEN. No $D>1$, $L>1$, generic, original $t\ge2$, cross, M1/M2, endpoint, M9, bridge, target, or exponent conclusion is promoted. |

## 2. Arithmetic pruning controls

For every $N$ and nonzero $j$,

$$
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)},
 \qquad
 \sum_{1\le|j|\le J}\rho_N(j)
 \ll_\varepsilon JX^\varepsilon.
$$

The local proof separates $v_p(j)\ge a$, odd $v_p(j)<a$, and even
$v_p(j)=2b<a$, with at most two odd-prime and four two-adic unit roots.
Because the $k$ interval has length $O(\sqrt{NM})<N$, one residue class
contains only $O(1)$ supported $k$.  At $J=M^{3/4}$ the actual
$M^{-3/4}$ weight makes the nonzero-small-defect owner target-safe.

The exact ray is present only for the odd squarefree kernel of $N$ and
has mass $O_\varepsilon(M^{-1/4}n_0^{-1/2}X^\varepsilon)$.  The tail
$s\ge\lceil M^{1/4}\rceil$ contains $O(M^{3/4})$ supported terms.  Its
intersection with $|j|>M^{3/4}$ is disjoint from the first two owners.
The residual condition is therefore exact and exhaustive.

## 3. Primary-source and power controls

Bourgain Theorem 6 is used as a global exponent pair, not restricted to
the direct Theorem-4 window.  Tao--Trudgian--Yang Lemma 14 gives

$$
 D(13/84,55/84)=(18/199,593/796).
$$

The difference between its affine line and the auxiliary maximum line is
$(17-29\alpha)/2388\ge5/4776$ on $[0,1/2]$.  Remark 16 and Lemma 15
make this pair global; Lemma 13 is then applied once to obtain

$$
 BD(13/84,55/84)=(195/796,235/398).
$$

Substitution into the exact weighted square-root formula gives

$$
 |P_U|\ll_\varepsilon
 R^{390/796}M^{-449/1592}X^\varepsilon
 =\left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon.
$$

The beta crossing is $\alpha=127/322$ inside the printed Table-1 cell.
The exact old-minus-new threshold gap is $556/367731>0$.

The source report was corrected to attribute the half-open endpoints to
Lutsko--Sourmelidis--Technau Theorem 1.3 and weighted partial summation to
Lemma 1.4.  It also attributes the 2026 Kaczorowski--Perelli constraint to
definition (1.3), while noting that their Theorem 1 is stated for $N\ge2$.
Neither bibliographic correction changes the no-match conclusion.

## 4. Review gate

Three orthogonal terminal reviews are GREEN:

- `reviews/independent_conductor_round152_math_review.md` rederives the
  pruning, actual-profile seam, character algebra, Mellin normalization,
  every exponent pair, the new range, and the beta cell after all notation
  and asymptotic repairs;
- `reviews/hostile_square_root_pruning_review.md` attacks the root count,
  parity, ceiling, support interval, endpoint, overlap, weight, and
  $B_{1,U}(1)$ seams and finds no defect; and
- `reviews/source_conductor_round152_final.md` independently verifies the
  global $D\to B$ source inference, theorem hypotheses, every power,
  Table-1 boundary, Mellin data, and all cited match/no-match interfaces.

The historical repairable RED inside the mathematical review is
superseded by its appended terminal GREEN recheck.  The hostile review is
GREEN for pruning only, exactly as scoped; it does not claim the open
$P_U^*$ estimate.

## 5. Pre-mutation validation

Before graph mutation:

- active campaign validation: PASS;
- starting graph validation and SHA-256 check: PASS;
- State Patch JSON parse and dry validation: PASS for 2 creates, 7 updates,
  15 rejections, and 8 no-change decisions;
- simulated post-patch graph validation: PASS;
- conductor candidate equation check: 51 tags, 51 unique tags, and 102
  balanced double-dollar delimiters;
- strict UTF-8/LF scan of the campaign plus corrected TTY source card:
  PASS, with no BOM, forbidden C0 byte, replacement character, $U+200E$,
  carriage return, duplicate per-file tag, unbalanced display delimiter,
  or missing final newline;
- Python compilation: PASS;
- unit tests: 6/6 PASS; and
- whitespace diff check: PASS, with only repository line-ending policy
  warnings and no whitespace error.

The State Patch is applied only after the validation matrix records these
pre-mutation gates as GREEN.

## 6. State mutation and post-validation

After the terminal review gate and every pre-mutation matrix entry were
GREEN, the State Patch applied:

- 2 obligations created;
- 7 obligations updated;
- 15 false inferences rejected; and
- 8 downstream obligations recorded unchanged.

Resulting graph SHA-256:
`9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`.

Post-application graph validation passes.  The accepted proof draft was
updated only from that mutated graph.  The completed campaign, structured
state, Python compilation, unit tests, whitespace, byte, equation-tag, and
display-delimiter checks are repeated after every closure record is
written.

## 7. Downstream decision

Close only the exact arithmetic pruning, the strict $BD$ scale range, and
the method-scoped character-loss/self-return/source boundary.  The next
owner is the large-defect, small-square-factor $P_U^*$ survivor below
$M^{449}\asymp R^{780}$, especially its $s=1$ odd-squarefree layer.
Every broader M1/M2, endpoint, M9, bridge, target, and global-exponent
obligation remains open or unchanged.
