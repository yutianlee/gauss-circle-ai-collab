# Round 148 conductor controls

- Campaign: m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate
- Round: 148
- Starting graph SHA-256: bb43abb1e0fbd719b18ebf91f4c7e477bf18e46e7b5225faaa88a7fb38d31352
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| exact_one_sided_B_process_and_q_amplitude | GREEN. Finite character-Poisson gives \(i/2\); the positive saddle gives phase \(e(Nd\ell/q)\), global unit \(e(1/8)\), amplitude \(N^{-1/4}(d\ell)^{-1}\), and \(q\asymp\ell Q\). |
| Q_length_and_RD_target_normalization | GREEN as a reduction. \(Q=2\sqrt{ND/E}\asymp D\sqrt{N/M}\), and the exact transformed target is \(RD X^\varepsilon\); that target remains open. |
| squarefree_both_variables_coprime_parity_character_cone | GREEN. The exact finite set \(\mathcal P(d)\) retains both squarefree expansions, coprimality, odd \(e,\alpha,b,q\), \(\chi_4\), strict cone, and all profiles. |
| Mobius_square_divisor_signed_decomposition | GREEN. Every \(\mu(\alpha)\mu(b)\) sign remains inside the reciprocal scalar; no progression triangle is used in the identity. |
| near_divisor_j_parameter_and_multiplicity | GREEN after correction. The coordinate is \(j=NL-Aq_0\), with \(q_0\mid NL-j\); the original \(j=N-Aq\) is only the unexpanded \(\ell=1\) cell. |
| dispersion_diagonal_offdiagonal_common_divisor | GREEN as a scoped obstruction. A long-prefix unrecombined progression-cell Cauchy with separately positive \(d\)-diagonal loses \(R\). Pre-Cauchy regrouping and signed cross-cell energies remain open. |
| q_divides_N_small_j_and_zero_frequency | GREEN as retained. Character-Poisson \(q=0\) vanishes, while reciprocal \(j=0\) forces a divisor of \(N\) after reduction and is target-safe; all nonzero \(j\) remain. |
| arbitrary_q_coefficient_phase_alignment_falsifier | GREEN for rejection. At \(D=1\), adversarial outer coefficients align the reciprocal phase and violate the all-scale target below \(M=R^2\); the actual \(\chi_4(q)\mathscr W(q)\) is not tested by that countermodel. |
| squarefree_absolute_QplusD_feasibility | OPEN. The analogue is neither proved nor refuted. Mobius expansion under triangle gives only \(Q\sqrt D+D\). |
| source_theorem_phase_modulus_coefficient_match | GREEN as a no-match audit. Small pointwise progression ranges are already target-safe; variance, inverse-square, inverse-fraction, and separable large-sieve interfaces do not match the actual varying-\(q\), coupled-profile sum. |
| H_resonance_interface_translation | GREEN as a mismatch. \(\ell\) need not be powerful, and the reciprocal \(LQ\) band is a factor \(D\) wider than the formal \(H\)-band. Complete reconstruction does not give a termwise coefficient identity. |
| all_M_D_E_Q_power_ledger | GREEN. The bare, \(\mu^2(d)\)-triangle, full progression-mass, early Cauchy-diagonal, and Round-147 \(H\)-menu capacities are distinguished. Every loss is an upper capacity, not a lower bound. |
| clipped_prefix_profile_collar_polar_boundary | GREEN. Product and cone collars are priced in the primal scalar; the finite \(K=6\) remainder, four frequency ranges, scaled derivative, finite cell mass, and dyadic tail sum give \(O(X^\varepsilon)\). Direct character-Poisson has no pole. |
| D1_prime_even_exact_radical_and_slow_family | GREEN as controls. \(D=1\), primes, even squarefree inputs, exact radicals, and slow phases remain literal and yield neither target proof nor signed counterexample. |
| individual_positive_direction_and_fixed_centre | GREEN. Only the individual positive physical phase and fixed \(N=\lfloor X\rfloor\) are used. |
| Round138_cross_tge2_and_downstream_scope | GREEN. The cross owner, every \(t\ge2\) layer, lower GAR, M9--M1, M9--M2, endpoint, M9, bridge, quarter target, and exponents remain separate. |

## 2. Exact analytic and diagonal controls

1. The missing finite-support condition was repaired before promotion:
   \(\alpha^2\le e_+\ll E\), and only nonempty original progressions
   enter \(\mathcal P(d)\).

2. The exact Gaussian remainder convention contains the localized
   Taylor error, complementary polynomial subtraction, and extended
   domain tail.  With \(\Lambda=\sqrt{NM}\), the order-six radial and
   cone remainders use

$$
   M^{-1/2}(M/\Lambda)^6,\qquad
   {\bf1}_{M\asymp D^2}D^{-1/2}(D/\Lambda)^6.
$$

   The sixfold nonstationary bound contains the required
   \(\Lambda^{1/2}\) conversion factor.  The finite
   \(DQ\sqrt E\) cell mass and dyadic \(2^{-5v}\) tails make the
   complete error \(O(X^\varepsilon)\).

3. The long-prefix diagonal is not assumed.  A literal rectangle
   \(\mathcal J_d\times\mathcal J_e\), the points
   \(b=1,n=1,\alpha^2\in\mathcal J_e\), and a common interval for
   \(q/(\alpha^2Q)\) prove both \(\mathscr L\asymp Q\sqrt E\)
   and the uniform \(d\)-norm \(\gg D\).  Short collar-owned prefixes
   are excluded from that lower-mass claim.

4. Positive Cauchy weights satisfy

$$
   D\left(\sum_i|c_i|\rho_i\right)
    \left(\sum_i|c_i|\rho_i^{-1}\right)
   \ge D\left(\sum_i|c_i|\right)^2.
$$

   This is used only after the cell basis has been frozen and its
   diagonal separately made positive.

5. Equality of reduced fractions is distinguished from the
   \(N\)-dependent alignment congruence

$$
   N(\ell_1q_2-\ell_2q_1)\equiv0\pmod{q_1q_2}.
$$

   No completion-order or universal dispersion claim is made.

## 3. Source and false-analogue controls

1. The fully reduced additive denominator is

$$
   q_*=\frac q{(q,\ell N)}=\frac{q_0}{(q_0,N)}.
$$

   The total \(q_*\le Y\) stratum is \(DYX^\varepsilon\), hence safe
   for \(Y\le R\).

2. Nunes's three pointwise progression ranges and Mangerel's smooth
   range are separated from Nunes's fixed-modulus variance theorem.
   The exact unit and modulus hypotheses are retained in the source
   report.

3. Schlage--Puchta at the exact reduced denominator gives a valid but
   nonexhaustive specialization.  Exact multiples improve the
   \(q_*\le\sqrt D\) case; other admissible approximants are
   unclassified, and no source theorem aggregates them over the actual
   varying \(q\).

4. The large-sieve calculation is labeled a separable,
   \(q\)-independent-coefficient diagnostic and is not applied
   verbatim to \(\mathscr W_{d,\ell,U}(q)\).

5. The arbitrary-coefficient analogue is false.  The absolute
   squarefree \(Q+D\) analogue remains open.  Neither conclusion is
   transferred to the actual signed scalar.

## 4. Review gate

The initial transform and source reviews returned AMBER and forced
repairs to finite progression support, exact Gaussian remainder
bookkeeping, the summed remainder powers, common-rectangle diagonal
construction, source hypotheses, Schlage--Puchta scope, \(H\)
bandwidth, and no-go wording.

The terminal reviews are:

- source_conductor_round148_final.md: GREEN;
- blind_conductor_round148_candidate_final_v2.md: GREEN.

They authorize only the exact reciprocal-transform reduction and the
scoped progression-separated/source obstruction.  They do not
authorize the signed target, a strict range, a universal dispersion
no-go, any downstream theorem, or an exponent change.

## 5. Pre-mutation validation

The following checks completed successfully before graph mutation:

- campaign manifest validation: PASS;
- State Patch validation against starting graph
  `bb43abb1e0fbd719b18ebf91f4c7e477bf18e46e7b5225faaa88a7fb38d31352`:
  PASS;
- active campaign, round plan, ledger, graph, and State Patch parsing:
  PASS;
- normalized candidate equation check: 35 distinct tags, no duplicate
  tag, and 38 balanced display pairs;
- Python compile check for `math_collab`: PASS;
- unit tests: 6/6 PASS;
- complete 20-file Round-148 byte scan: strict UTF-8, 0 carriage-return
  bytes, 0 tabs or other forbidden C0 bytes, 0 U+200E characters,
  0 replacement characters, 0 BOMs, and every file ending in LF;
- git diff whitespace check for the Round-148 directory: PASS.

## 6. State-mutation result

The validated State Patch was applied with:

- 2 obligations created;
- 5 obligations updated;
- 12 false inferences rejected;
- 8 global obligations recorded unchanged.

Resulting graph SHA-256:
`8f1912eeda4843718379213478a839b30fb2694d6b169ac8decbab5ca3561176`.

Post-application graph and completed-campaign validation, structured-state
parsing, Python compilation, all 6 unit tests, equation checking,
Round-148 whitespace checking, and the complete 20-file byte scan all
passed. The byte scan found 0 carriage-return bytes, 0 tabs or other
forbidden C0 bytes, 0 U+200E or replacement characters, 0 UTF-8 errors,
0 BOMs, and no missing final LF.
