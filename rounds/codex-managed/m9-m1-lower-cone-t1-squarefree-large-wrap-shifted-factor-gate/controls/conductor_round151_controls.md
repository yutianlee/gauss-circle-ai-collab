# Round 151 conductor controls

- Campaign: `m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate`
- Round: 151
- Starting graph: `521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f`
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| `literal_large_wrap_residual` | GREEN. Both exact $B$ coefficients, prefixes, profiles, incidence masks, squarefree rows, common gcd, imprimitive denominators, centered wrap, reciprocal phase, character, coprimality, and support conditions remain literal. |
| `accepted_small_packet_exclusion` | GREEN. Every shifted-factor residual excludes only the accepted packet $\mathcal K_0$; new owners are intersected with, then subtracted from, earlier exact and fixed-wrap owners. |
| `two_adic_character_transfer` | GREEN. The transfer uses the odd quotients $x,y$, covers both signs of $k$, every parity of $N$, all relations of $\nu_2(k)$ to $\nu_2(N)$, and the convention $\nu_2(0)=+\infty$ for $\delta=0$. |
| `shifted_factor_positivity_and_recovery` | GREEN. Exact one-factor identities prove positivity, including $q_i\mid N$; the inverse is a bijection only after the divisor fibre $h\mid g$ and every original test are retained. |
| `joint_k_rho_h_summation` | GREEN/open split. High-two-adic wraps and the two source-legal row corridors are fully summed in their scope. The low-adic isolated residual outside them remains open and the $h$ fibre is not dropped. |
| `high_two_adic_sparse_range` | GREEN. Multiples of $2^{J_*}\asymp N/R^2$ inside $|k|\ll N/Q$ form $O(1+R^2/Q)$ classes and cost $O(R^2D X^\varepsilon)$ by the accepted arbitrary fixed-wrap theorem. |
| `D1_L1_reciprocal_scalar` | GREEN in the Bourgain and TTY strict ranges; open below them after the bounded-$M$ owner. At $D=1$, all centered nonexact pairs lie in the collar. |
| `exact_character_fourier_identity` | GREEN. $\chi_4(q)=(e(q/4)-e(-q/4))/(2i)$ holds on all integers and kills even $q$. |
| `boundary_complete_B_process` | GREEN. The actual compact-smooth Round-148 profile, zero extension, literal coefficient, endpoint convention, transition buffers, tails, and target-safe error are retained; the square-root dual main is not called an error. |
| `actual_profile_derivative_ledger` | GREEN at every scale. Bulk, radial, cone, product, component, sampling, zero-extension, and prefix-owner contributions give $O_\varepsilon(X^\varepsilon)$ supremum plus variation. |
| `dual_self_return_vs_gain` | GREEN as a no-go. The phase and principal stationary symbol self-return, while lower symbols and endpoints retain their accepted ledger. The direct/dual capacities are not an automatic gain or a signed lower bound. |
| `tuple_absolute_signed_separation` | GREEN. Wrap-class counts, coefficient-weighted absolute ranges, recombined row energies, isolated signed collar subsets, and elementary transform capacities remain distinct. |
| `source_theorem_large_wrap_match` | GREEN for Bourgain and TTY on recombined rows. GREEN as direct no-matches for Duke--Friedlander--Iwaniec, Cowan, Blomer--Harcos, and Bettin--Chandee on the isolated recovery-weighted collar. |
| `all_M_D_E_Q_L_h_k_rho_power_ledger` | GREEN. The exact conditions are $D^{84}R^{52}\ll M^{29}$ and $M^{819}\gg R^{1424}D^{1816}L_0^{534}$; all bounded, top, $D=1$, $L_0=1$, and $M\asymp R^2$ specializations agree. |
| `prime_parity_prefix_imprimitive_controls` | GREEN. Even squarefree rows, all odd-prime masks, both parities of $N$, exact prefixes, common factors, imprimitive fractions, $q_i\mid N$, both wrap signs, and $\delta=0$ remain covered. |
| `generic_tge2_cross_and_downstream_scope` | GREEN. Whole-row versus isolated-collar scope is explicit; the high-row square, low-high cross, growing-$M$ generic sector, all $t\ge2$, Round-138 cross, M1, M2, endpoint, M9, bridge, target, and exponents remain open or unchanged. |

## 2. Review gate

The three terminal independent reviews are:

- `reviews/independent_conductor_round151_math_review.md`: GREEN after
  explicit repairs restoring all coefficient restrictions, the
  $\nu_2(0)$ convention, nonduplicated $B$-coefficient notation,
  positive-$q$ zero extension, and source-card/graph-node wording;
- `reviews/source_conductor_round151_final.md`: GREEN for the Bourgain
  Theorem-4/Theorem-6 correction, TTY theorem, derivative class, proper
  intervals, $\mathcal T\ge H$ convention, Mobius normalization,
  Abel-after-unweighted order, exact powers, $B$-process source, and four
  direct no-matches; and
- `reviews/independent_bprocess_candidate_final.md`: GREEN for the
  source-complete Round-148 boundary relation, exact $B_{1,U}(1)$ pair
  coefficient, principal-symbol-only self-return, no spurious integer-jump
  obstruction, all-$M$ capacities, and strict $D=d=1,L_1=L_2=1$ scope.

The earlier `independent_bprocess_endpoint_review.md` is retained as a RED
review of the blind report as written.  Its repairs are all present in the
conductor candidate and were independently rechecked in the terminal
GREEN review.  The preliminary TTY review is GREEN with its fixed
comparable second-derivative edge incorporated.

## 3. Primary-source controls

The corrected Bourgain card and terminal source review distinguish the
direct Theorem-4 window from the global Theorem-6 exponent pair.  The
long-length proof uses the source's near-square rescaling,
$(1/2,1/2)$ extreme range, remaining-range $B$-process, and proper-interval
extension.  The reciprocal phase satisfies the fixed derivative class.

Tao--Trudgian--Yang Definitions 5, 11, and 12 and Theorem 20 supply
$(89/1282,997/1282)$ for the reciprocal model phase.  In both applications,
coprimality and the two character classes are resolved first, the external
theorem is applied to unweighted interval sums, and the actual profile is
inserted only by Abel summation.  A fixed comparable edge with
$\mathcal T<H$ uses a project-side second-derivative estimate instead of
violating a source convention.

The shifted-divisor audit checks exact printed statements of
Duke--Friedlander--Iwaniec, Cowan, Blomer--Harcos, and Bettin--Chandee.
Their direct-specialization failures are confined to coefficient,
character, level, independence, determinant/shift-family, smoothness, or
power hypotheses.  No literature-impossibility conclusion is drawn.

## 4. Power and endpoint controls

For Bourgain,

$$
 \frac{E^{13/42}Q^{55/42}}{R^2}
 =\left(\frac{D^{84}R^{52}}{M^{29}}\right)^{1/84}.
$$

Thus $D=1$ starts at $M\gg R^{52/29}$ and the top scale permits
$D\ll R^{1/14}$.

For Tao--Trudgian--Yang,

$$
 \frac{E^{178/1282}Q^{1994/1282}L_0^{534/1282}}{R^2}
 =\left(
 \frac{R^{1424}D^{1816}L_0^{534}}{M^{819}}
 \right)^{1/1282}.
$$

Thus $D=L_0=1$ starts at $M\gg R^{1424/819}$, while at
$M\asymp R^2$ one has $D^{1816}L_0^{534}\ll R^{214}$.

At $D=L=1$,

$$
 Q\asymp R^2M^{-1/2},\qquad
 |S_U|_{\rm abs}\ll
 \min\{R^2M^{-1/2},RM^{1/4}\}X^\varepsilon.
$$

The dual capacity is target-sized only at bounded $M$, and the direct
length is target-sized only at the top scale.  The boundary-complete
transform reduces the intermediate endpoint to the signed square-root
wave; it does not estimate that wave.

## 5. Pre-mutation validation

Before graph mutation:

- active campaign validation: PASS;
- graph validation at the starting SHA-256: PASS;
- State Patch JSON parse and dry validation: PASS for 2 creates, 9 updates,
  14 rejections, and 8 no-change decisions;
- simulated post-patch graph validation: PASS;
- conductor candidate equation check: 59 tags, 59 unique tags, and 118
  balanced double-dollar delimiters;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- Round-151 strict UTF-8/LF scan: PASS for all 19 campaign artifacts after
  mechanical line-ending normalization, with no BOM, forbidden C0 byte,
  zero-width character, replacement character, or missing final newline;
- the corrected Bourgain source card passes the same strict byte scan; and
- whitespace diff check: PASS, with only repository line-ending policy
  warnings and no whitespace error.

The complete 20-file campaign-plus-source scan contains 286 unique
per-file equation tags and no unbalanced display delimiter.  The State
Patch was applied only after these checks and the terminal review gate were
GREEN.

## 6. State mutation and post-validation

After the terminal review gate and pre-mutation checks were GREEN, the
State Patch applied:

- 2 obligations created;
- 9 obligations updated;
- 14 false inferences rejected; and
- 8 downstream obligations recorded unchanged.

Resulting graph SHA-256:
`d09d0f8c1e7058a1e423e5249d3cf28b08d8478cff55ddd1c85b1d59bb177b2c`.

Post-application graph validation, completed-campaign validation,
structured parsing of every touched JSON/YAML state file, Python
compilation, all 6 unit tests, and whitespace checking pass.  The accepted
proof draft was updated only after graph mutation.  The final strict byte
and equation scans are repeated after all closure records are written.

## 7. Downstream decision

Close only the exact character coordinates, high-two-adic family,
actual-profile all-scale BV lemma, Bourgain full-row corridor, TTY low-row
corridor, and reciprocal principal-self-return boundary.  The next owner
is the low-two-adic recovered residual outside those corridors, or its
$D=L=1$ signed square-root-wave specialization.  The growing-$M$ generic
complement remains separate.  The global exponents do not change.
